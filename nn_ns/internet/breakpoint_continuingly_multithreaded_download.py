

'''
url -> get (defaut_file_name, file_size, last_modified)
fname -> configure_file_name


block_size : correspond to one bit in bit_map_file -> bit_map_file_name
num_blocks_of_file_part
{
    block_size = min(block_size, file_size)
    num_blocks_of_file_part = min(num_blocks_of_file_part, ceil(file_size/block_size))
    file_part_size = num_block_of_file_part*block_size
    assert file_part_size <= file_size
    
    num_file_parts = ceil(file_size/file_part_size)
}

num_threads
'''

#from queue import Queue
from http_do import http_do, _request_headers
from my_exception import internet_except
import urllib.request, re
from ptask import *
from threading import Thread
import os

def get_head(url):
    r = http_do(url, method='HEAD')
    '''
    'Content-Length'
    'Last-Modified'
    'Content-Type'
    ??'Accept-Ranges': 'bytes' #'RANGE': 'bytes=468500-', \
    '''
    if r.reason != 'ok':
        raise internet_except('get_head fail: url = {}'.format(url))
    return r.head

content_range_pattern = re.compile('bytes\s*(\d+)-(\d+)/(\d+)')
def generate_content_range_header(rng):
    begin, end = rng
    assert 0 <= begin < end
    first, last = begin, end-1
    return ('RANGE', 'bytes={}-{}'.format(first, last)) # 0-499 is 500

def get_range_from_content_range_header(content_range_header):
    m = content_range_pattern.match(content_range_header)
    assert m != None
    first, last, total_size = m.group(1, 2, 3)
    first, last, total_size = int(first), int(last), int(total_size)
    assert 0 <= first <= last < total_size
    return (first, last+1), total_size


class range_download_head_info:
    def __init__(self, http_do_result_head):
        self.content_length = http_do_result_head['content-length']
        self.last_modified = http_do_result_head['last-modified']
        self.content_type = http_do_result_head['content-type']
        
        self.accept_ranges = http_do_result_head.get('accept-ranges') 
        self.content_encoding = http_do_result_head.get('content-encoding')

        self.info = {'content_length':self.content_length,\
                     'last_modified':self.last_modified,\
                     'content_type':self.content_type,\
                     'accept_ranges':self.accept_ranges,\
                     'content_encoding':self.content_encoding,\
                     }
        
def range_download(url, rng, total_size=None):
    n = rng[1] - rng[0]
    new_header = generate_content_range_header(rng)

    '''
    'Content-Length'
    'Last-Modified' -----> modified since last download???
    'Content-Type'  -----> .jpg or txt of gbk???
    'Content-Encoding' --> zipped???
    'Accept-Ranges': 'bytes'
    '''
    r = http_do(url, 'GET', [new_header])
    if r.status != 206: # 'Partial Content':
        raise internet_except('range_download fail: status = {}, reason = {}\n\turl = {}'\
                              .format(r.status, r.reason, url))

    head = r.head
    assert head['accept-ranges'] == 'bytes'
    
    _rng, _total_size = get_range_from_content_range_header(head['content-range'])
    if total_size: assert total_size == _total_size
    assert rng == _rng
    assert n == len(r.data)


    return r.data, range_download_head_info(r.head)


def get_log_file_name(fname):
    return fname+'.download_big_file_log.log'

def to_ranges(begin, end, step):
    rngs = list((fst, fst+step) for fst in range(begin, end, step))
    last_begin = rngs[-1][0]
    rngs[-1] = (last_begin, end)
    return rngs


def download_big_file_part1(url, log_block_size, block_per_task):
    assert 0 < log_block_size
    assert 0 < block_per_task
    assert block_per_task == 1
    
    size_per_task = log_block_size * block_per_task

    head = get_head(url)
    head_info = range_download_head_info(head)
    if head_info.content_length == 0:
        raise internet_except('content_length == 0 : url = {}'.format(url))
    if head_info.accept_ranges == None:
        raise internet_except('accept_ranges == None : url = {}'.format(url))
    size = head_info.content_length
    rngs = to_ranges(0, size, size_per_task)
    


    def worker(rng):
        data, info = range_download(url, rng, total_size=size)
        return data

    return size_per_task, head_info, size, rngs, worker




def _block_download(task_info, log, fout, max_workers):
    skip = 0
    for branch, info_ in ptask(task_info, max_workers=max_workers):
        if branch == except_branch:
            info, exc = info
            print('{} generated an exception: {}'.format(info, exc))
            skip += 1
        elif branch == except_else_branch:
            info, output = info_
            begin = info
            fout.seek(begin)
            fout.write(output)
            log.write('{}\n'.format(begin))
            log.flush()
        elif branch == finally_branch:
            pass
        else:
            raise unknown_case_except('ptask branch')

    return skip

def download_big_file_part2(url, worker, rngs, log, fout, max_workers):
    assert max_workers > 0
    task_info = (\
        ((worker, rng), rng[0])\
        for rng in rngs\
        )

    
    skip = _block_download(task_info, log, fout, max_workers=max_workers)
    if skip:
        raise internet_except('incomplete download : url = {}'.format(url))


def _init_log(log, url, total_size, log_block_size, head_info):
    log.write('{!r}\n'\
              .format(dict(url=url, total_size=total_size, \
                      log_block_size=log_block_size,\
                      head_info=head_info))\
              )

    log.flush()

def initially_download_big_file(url, fname, log_block_size=2**20, block_per_task = 1, max_workers=5):
    size_per_task, head_info, size, rngs, worker = download_big_file_part1(\
            url, log_block_size, block_per_task=block_per_task)
    log_name = get_log_file_name(fname)
    with open(fname, 'xb') as fout, open(log_name, 'x') as log:
        _init_log(log, url=url, total_size=size, log_block_size=log_block_size,\
                    head_info=head_info.info)
        download_big_file_part2(url, worker, rngs, log, fout, max_workers=max_workers)

    #os.rename(src, dst)
    os.remove(log_name)
    
                  


def _read_log(log, url=None):
    s = log.readline()
    log_head = eval(s)
    
    log_ls = []
    for line in log:
        log_ls.append(int(line))

    log_ls.sort()

    if url != None:
        assert url == log_head['url']
    
    log_block_size = log_head['log_block_size']
    assert log_block_size > 0
    for begin in log_ls:
        assert begin % log_block_size == 0
        
    return log_head, log_ls
    

def continue_download_big_file(fname, block_per_task = 1, max_workers=5, url=None):
    if not os.path.exists(fname):
        raise internet_except('file name not exists : fname = {}'.format(fname))

    log_name = get_log_file_name(fname)
    if not os.path.exists(log_name):
        raise internet_except('log file name not exists : log_name = {}'.format(log_name))
    
    with open(fname, 'ab') as fout, open(log_name, 'r+') as log:
        log_head, log_ls = _read_log(log, url=url)
        url = log_head['url']
        size = log_head['total_size']
        log_block_size = log_head['log_block_size']
        head_info = log_head['head_info']
        

        size_per_task, _head_info, _size, _rngs, worker = download_big_file_part1(\
            url, log_block_size, block_per_task=block_per_task)

        assert size == _size
        assert head_info['content_length'] == _head_info.content_length
        assert head_info['last_modified'] == _head_info.last_modified

        rngs = []
        iter_rngs = iter(_rngs)
        for beg in log_ls:
            for rng in iter_rngs:
                if rng[0] == beg:
                    break
                rngs.append(rng)
        else:
            for rng in iter_rngs:
                rngs.append(rng)

        download_big_file_part2(url, worker, rngs, log, fout, max_workers=max_workers)

    os.remove(log_name)


    
def download_big_file(url, fname, log_block_size=2**20, block_per_task = 1, max_workers=5):
    try:
        initially_download_big_file(url, fname, log_block_size=log_block_size, block_per_task=block_per_task, max_workers=max_workers)
    except:
        continue_download_big_file(fname, block_per_task=block_per_task, max_workers=max_workers, url=url)


if __name__ == "__main__":
    path = r'E:/my_data/program_source/python3_src/internet/'
    url = 'http://img1.comic.zongheng.com/comic/series/2013/4/xiefengmanhua/15/svol_20130506094816647724.jpg'

    range_download(url, (0,4))
    download_big_file(url, path+'tmp.jpg', log_block_size=2**20)
    


'''
import urllib.parse
import httplib2

http = httplib2.Http()

url = 'http://www.example.com/login'   
body = {'USERNAME': 'foo', 'PASSWORD': 'bar'}
headers = {'Content-type': 'application/x-www-form-urlencoded'}
response, content = http.request(url, 'POST', headers=headers, body=urllib.parse.urlencode(body))

headers = {'Cookie': response['set-cookie']}

url = 'http://www.example.com/home'   
response, content = http.request(url, 'GET', headers=headers)

'''
'''
import urllib.parse
import httplib2

path = 'E:/my_data/program_source/python3_src/internet/'
http = httplib2.Http(path+".cache")
url_home = 'http://tieba.baidu.com/'
'''


#response, content = http.request(url_home, 'GET')
#response is something like:
#{'content-length': '173627', 'status': '200', 'set-cookie': 'TIEBAUID=cb23caae14130a0d384a57f1; expires=Thu, 31-Dec-2020 15:59:59 GMT; path=/; domain=tieba.baidu.com, TIEBA_USERTYPE=f26212b24ac64c99ade85865; expires=Thu, 31-Dec-2020 15:59:59 GMT; path=/; domain=tieba.baidu.com, BAIDUID=A09909ABD46F4B87926F7D291BE95477:FG=1; expires=Sun, 23-Aug-15 07:17:33 GMT; max-age=31536000; path=/; domain=.baidu.com; version=1', 'content-location': 'http://tieba.baidu.com/', 'transfer-encoding': 'chunked', 'tracecode': '10531894860983224330082315, 10531894860294047754082315', 'server': 'Apache', 'vary': 'Accept-Encoding', 'connection': 'Keep-Alive', '-content-encoding': 'gzip', 'p3p': 'CP=" OTI DSP COR IVA OUR IND COM "', 'date': 'Sat, 23 Aug 2014 07:17:33 GMT', 'content-type': 'text/html; charset=GBK'}



'''

if 'set-cookie' in response:
    headers = {'Cookie': response['set-cookie']}
else:
    headers = {}
'''

'''
baidu_cookie = 'TIEBAUID=cb23caae14130a0d384a57f1; expires=Thu, 31-Dec-2020 15:59:59 GMT; path=/; domain=tieba.baidu.com, TIEBA_USERTYPE=f26212b24ac64c99ade85865; expires=Thu, 31-Dec-2020 15:59:59 GMT; path=/; domain=tieba.baidu.com, BAIDUID=A09909ABD46F4B87926F7D291BE95477:FG=1; expires=Sun, 23-Aug-15 07:17:33 GMT; max-age=31536000; path=/; domain=.baidu.com; version=1'

body = {'USERNAME': 'eggache_being', 'PASSWORD': '621823'}
headers = {'Content-type': 'application/x-www-form-urlencoded', 'Cookie': baidu_cookie}
response, content = http.request(url_home, 'POST', headers=headers, body=urllib.parse.urlencode(body))
baidu_cookie = response['set-cookie']
#response is something like:
#{'transfer-encoding': 'chunked', 'set-cookie': 'TIEBA_USERTYPE=e56b4cc791c1907ff1eb286e; expires=Thu, 31-Dec-2020 15:59:59 GMT; path=/; domain=tieba.baidu.com', 'server': 'Apache', 'content-type': 'text/html; charset=GBK', 'content-length': '173603', 'connection': 'Keep-Alive', '-content-encoding': 'gzip', 'date': 'Sat, 23 Aug 2014 07:37:01 GMT', 'tracecode': '22215348230230936586082315, 22215348230417386506082315', 'vary': 'Accept-Encoding', 'status': '200'}
'''


#baidu_cookie = 'TIEBA_USERTYPE=e56b4cc791c1907ff1eb286e; expires=Thu, 31-Dec-2020 15:59:59 GMT; path=/; domain=tieba.baidu.com'

'''
baidu_cookie = 'PROPS_MAGIC_GUIDE=true; BAIDU_DUP_lcr=http://www.sogou.com/sogou?query=%D4%F5%C3%B4%B5%C7%C2%BC+python&pid=AWNb5-0000; BAIDUID=07117187CF0FFB16D49088F82F2B55FA:FG=1; TIEBA_USERTYPE=9c139eef0c28464d9b629c0f; bdshare_firstime=1406772592914; dasense_show_10681=1; TIEBAUID=bcf772fd70c5de66d00abff1; BDUSS=nRHb1dmRG9sY3A4cFB1MmVEZUFiR2xWNjJEQm9vb0hJS0ZVN2dad0ItQU4yeDlVQVFBQUFBJCQAAAAAAAAAAAEAAACd2IsmuqOyztfUtPjPtNTovLwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1O-FMNTvhTM; dasense_show_10652=1; GET_TOPIC=646699165; dasense_show_10573=1; dasense_show_10679=1; dasense_show_10496=1; wise_device=0; Hm_lvt_287705c8d9e2073d13275b18dbd746dc=1408528971,1408700608,1408701929,1408783835; Hm_lpvt_287705c8d9e2073d13275b18dbd746dc=1408785701; H_PS_PSSID=7736_1443_7802_8234_8224_8057_8223_6506_8211_6017_7826_8332_7606_7798_8035_8319_7962_8129_8114; PMS_JT=%28%7B%22s%22%3A1408786668409%2C%22r%22%3A%22http%3A//tieba.baidu.com/f%3Fkw%3D%25D6%25BB%25D3%25D0%25C9%25F1%25D6%25AA%25B5%25C0%25B5%25C4%25CA%25C0%25BD%25E7%22%7D%29'
urllib.parse.unquote(baidu_cookie)
headers = {'Cookie': baidu_cookie}
response, content = http.request(url_home, 'GET', headers=headers)
response
#with open(path+'out_file.txt', 'xb') as fout: fout.write(content)
'''


