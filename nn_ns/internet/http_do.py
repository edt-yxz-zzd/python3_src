

import gzip, zlib

import urllib.request, socket
from sand import print_except



_request_headers = {\
    "Content-Type":"application/x-www-form-urlencoded;charset=utf-8",\
    'Accept': 'text/html, image/gif, image/jpeg, */*', \
    }


#zlib.decompressobj(wbits=15, zdict]) 
def gzip_decompressobj(wbits=15, zdict=None):
    wbits |= 16
    if zdict == None:
        return zlib.decompressobj(wbits)
    else:
        return zlib.decompressobj(wbits, zdict)



zip_method_name2decompress_method = \
    {'gzip':gzip.decompress, 'deflate':zlib.decompress}

zip_method_name2decompressobj = \
    {'gzip':gzip_decompressobj, 'deflate':zlib.decompressobj}

def lower_head(http_response_head):
    head = dict((key.lower(), v) for key, v in http_response_head.items())
    return head

class http_do_result:
    def __init__(self, status, reason, head, zdata, data):
        self.status, self.reason, self.head, self.zdata, self.data = \
                     status, reason, head, zdata, data


'''
def catch_http_do(http_do):
    def _f(url, method, more_headers=()):
        try:
            r = http_do(url, method, more_headers)
            return r
        except Exception as e:
            print(e)
            raise

    return _f

@catch_http_do
'''
@print_except
def http_do(url, method, more_headers=(), timeout=''):
    if timeout == '':
        timeout = socket.getdefaulttimeout() 

    req = urllib.request.Request(url, headers=_request_headers, method=method)
    for k, v in more_headers:
        req.add_header(k, v)
    with urllib.request.urlopen(req, timeout=timeout) as response:
        head = dict(response.headers)
        head = lower_head(head)
        if 'content-length' in head:
            head['content-length'] = int(head['content-length'])
        else:
            # ?? transfer-coding:chunked
            head['content-length'] = None
        zdata = response.readall()

        if 'content-encoding' in head:
            zip_method_name = head['content-encoding']
            if zip_method_name not in zip_method_name2decompress_method:
                raise internet_except('unknown zip_method_name = {}'.format(zip_method_name))
            data = zip_method_name2decompress_method[zip_method_name](zdata)
        else:
            data = zdata

        return http_do_result(response.status, response.reason.lower(), head, zdata, data)




'''

def http_do_inc(url, method, more_headers=(), chunk_size, ):
    req = urllib.request.Request(url, headers=_request_headers, method=method)
    for k, v in more_headers:
        req.add_header(k, v)
    with urllib.request.urlopen(req) as response:
        head = dict(response.headers)
        head = lower_head(head)
        head['content-length'] = int(head['content-length'])
        #zdata = response.readall()

        if 'content-encoding' in head:
            zip_method_name = head['content-encoding']
            if zip_method_name not in zip_method_name2decompressobj:
                raise internet_except('unknown zip_method_name = {}'.format(zip_method_name))
            inc = zip_method_name2decompressobj[zip_method_name]()
            xxxxxxxxxxxxxxxxxxxxxxx
            
        else:
            data = zdata

        return http_do_result(response.status, response.reason.lower(), head, zdata, data)
'''


if __name__ == "__main__":
    #url = r'http://mathworld.wolfram.com/CubicPolyhedralGraph.html'
    #url = r'http://www.baidu.com/s?wd=%CE%AA%CA%B2%C3%B4%CD%F8%D2%B3%D4%B4%CA%C7%C2%D2%C2%EB'
    #url = 'http://img1.comic.zongheng.com/comic/series/2013/4/xiefengmanhua/15/svol_20130506094816647724.jpg'
    url = r'http://www.bilibili.com/video/tv-drama-cn-41.html'
    http_do(url, 'GET')
    
