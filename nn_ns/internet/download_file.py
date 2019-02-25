
r'''
# copy from nn_ns.app.Django.mzitu_com.mzitu_com_project_main.proxy_app.views.py


############################ URI
URI = scheme:[//authority]path[?query][#fragment]

authority
    authority = [userinfo@]host[:port]

query
    key1=value1&key2=value2
    key1=value1;key2=value2


ParseResult(scheme='http', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html',
            params='', query='', fragment='')



########################### Header #### RFC 2616
http://jkorpela.fi/http.html
https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html
part of Hypertext Transfer Protocol -- HTTP/1.1
RFC 2616 Fielding, et al.
14 Header Field Definitions
       ######################## request
       ...
       Range: bytes=21010-47021
       ...
       # <==>:
       #    assume len(file) == 47022
       #        #last 26012 bytes
       #        #file[-26012:]
       #    Range: bytes=21010-
       #    Range: bytes=21010-39999,40000-
       #    Range: bytes=21010-39999,-7022
       #    Range: bytes=-26012


       ######################## response
       HTTP/1.1 206 Partial content
       Date: Wed, 15 Nov 1995 06:25:24 GMT
       Last-Modified: Wed, 15 Nov 1995 04:58:08 GMT
       Content-Range: bytes 21010-47021/47022
       Content-Length: 26012
       Content-Type: image/gif

       ########################
       len(file) == 47022
       response = file[21010:47021+1]
       len(response) = 26012 = (47021+1)-21010



Expires: Thu, 01 Dec 1994 16:00:00 GMT
    HTTP/1.1 clients and caches MUST treat other invalid date formats, especially including the value "0", as in the past (i.e., "already expired").

    To mark a response as "already expired," an origin server sends an Expires date that is equal to the Date header value. (See the rules for expiration calculations in section 13.2.4.)

    To mark a response as "never expires," an origin server sends an Expires date approximately one year from the time the response is sent. HTTP/1.1 servers SHOULD NOT send Expires dates more than one year in the future.

'''

__all__ = '''
    get_scheme_authority
    parse_datetime_in_http_headers
    download_file
    '''.split()

import urllib.request
import urllib.parse
from .parse_datetime_in_http_headers import parse_datetime_in_http_headers


def get_scheme_authority(url):
    r = urllib.parse.urlparse(url)
    parts = [r.scheme, r.netloc, '/', '', '', '']
    scheme_authority = urllib.parse.urlunparse(parts)
    return scheme_authority

def download_file(url, *, maybe_begin, maybe_end, header_only:bool, maybe_output_path_or_fout, omode):
    '''

download_file(url, *, maybe_begin, maybe_end, header_only:bool, maybe_output_path_or_fout:'str|None|file', omode:str)

@legacy
urllib.request.urlretrieve(url, filename=None, reporthook=None, data=None) -> (local_filename, headers)
    # local_filename - may be temp file
    # headers - from response.info()

'''
    if omode.lower() not in ('wb', 'ab', 'xb'): raise ValueError
    if not isinstance(url, str): raise TypeError
    if not (maybe_begin is None or type(maybe_begin) is int): raise TypeError
    if not (maybe_end is None or (type(maybe_end) is int and maybe_end >= 0 and (maybe_begin is None or 0 <= maybe_begin < maybe_end))): raise TypeError

    if maybe_end is None:
        #allow maybe_begin < 0
        if maybe_begin is None:
            maybe_bytes_range_str = None
        else:
            begin = maybe_begin
            if begin == 0:
                maybe_bytes_range_str = None
            elif begin > 0:
                maybe_bytes_range_str = f'bytes={begin}-'
            elif begin < 0:
                maybe_bytes_range_str = f'bytes={begin}'
            else:
                raise logic-error
    else:
        #not allow maybe_begin < 0
        end = maybe_end
        if maybe_begin is None:
            begin = 0
        else:
            begin = maybe_begin

        if not 0 <= begin < end: raise ValueError
        last = end-1
        first = begin
        maybe_bytes_range_str = f'bytes={first}-{last}'
    ##################################################
    ##################################################

    #TARGET: file_data = urllib.urlopen(url).read()
    header_only = bool(header_only)
    request_method = 'HEAD' if header_only else 'GET'

    # 'User-Agent'
    # 'Referer'
    # 'Range'
    #
    #part of Hypertext Transfer Protocol -- HTTP/1.1
    #RFC 2616 Fielding, et al.
    #14 Header Field Definitions


    #('User-Agent','Mozilla/5.0 (Linux; Android 4.4.4; en-us; Nexus 5 Build/JOP40D)
    #('Referer', 'http://www.python.org/')
    UserAgent = r'Mozilla/5.0 (Linux; Android 4.4.4; en-us; Nexus 5 Build/JOP40D)'
    Referer = get_scheme_authority(url)
    assert type(UserAgent) is str is type(Referer)

    request_headers = [('User-Agent', UserAgent), ('Referer', Referer)]
    if maybe_bytes_range_str is not None:
        bytes_range_str = maybe_bytes_range_str
        request_headers.append(('Range', bytes_range_str))




    if True:
        request = urllib.request.Request(
                    url
                    , data=None
                    , headers=dict(request_headers)
                    , method=request_method
                    )
        #request.add_header()
        fin = response = urllib.request.urlopen(request)
    else:
        opener = urllib.request.build_opener()

        opener.addheaders = request_headers
        fin = response = opener.open(url)


    # detect the orginal url content_type
    url_info = response.info() #
        # .info() -> http.client.HTTPMessage <: email.message.Message
        # .geturl()
        # .getcode()

    header_dict = dict(url_info.items())
    content_type = url_info.get_content_type()
    content_length__str = url_info['Content-Length']
    if not content_length__str:
        content_length__str = None
        maybe_content_length = None
    else:
        maybe_content_length = int(content_length__str)

    try:
        last_modified_time__str = url_info['Last-Modified']
        if not last_modified_time__str:
            raise KeyError
    except KeyError:
        maybe_last_modified_time__str = None
        maybe_last_modified_time__datetime = None
        maybe_last_modified_time__float_seconds = None
    else:
        last_modified_time__datetime = parse_datetime_in_http_headers(last_modified_time__str)
        last_modified_time__float_seconds = last_modified_time__datetime.timestamp()
        #os.utime(ofname, (last_modified_time__float_seconds, last_modified_time__float_seconds))

        maybe_last_modified_time__str = last_modified_time__str
        maybe_last_modified_time__datetime = last_modified_time__datetime
        maybe_last_modified_time__float_seconds = last_modified_time__float_seconds




    if maybe_output_path_or_fout is None:
        file_data = content = fin.read()
        content_size = len(file_data)
        maybe_file_data = file_data
    else:
        output_path_or_fout = maybe_output_path_or_fout
        maybe_file_data = None

        def copy(*, fin, fout):
            content_size = 0
            while True:
                bs = fin.read(1024)
                if not bs: break
                fout.write(bs)
                content_size += len(bs)
            #bug: content_size = fout.tell()
            #   when omode == 'ab'
            return content_size

        try:
            fout = open(output_path_or_fout, omode)
        except OSError:
            if hasattr(output_path_or_fout, 'write'):
                fout = output_path_or_fout
                content_size = copy(fin=fin, fout=fout)
            else:
                raise
        else:
            with fout:
                content_size = copy(fin=fin, fout=fout)
    content_size
    maybe_file_data



    # may fail: assert len(content) == content_length
    if not ((header_only and not content_size) or (not header_only and (maybe_content_length is None or content_size == maybe_content_length))):
        # 21.6.24. Legacy interface::urlretrieve
        # The Content-Length is treated as a lower bound: if there's more data to read, urlretrieve reads more data, but if less data is available, it raises the exception.
        # the amount of data available may be less than the expected amount (which is the size reported by a Content-Length header). This can occur, for example, when the download is interrupted.
        content_length = maybe_content_length
        if header_only: raise logic-error
        elif maybe_content_length is None: raise logic-error
        elif content_size < content_length:
            raise IOError('the download is interrupted')
        else:
            assert content_size > content_length


    return dict(
        url_info=url_info
        ,url=response.geturl()
        ,code=response.getcode()

        ,header_dict=header_dict
        ,content_type=content_type
        ,maybe_last_modified_time__str=maybe_last_modified_time__str
        ,maybe_last_modified_time__datetime=maybe_last_modified_time__datetime
        ,maybe_last_modified_time__float_seconds=maybe_last_modified_time__float_seconds
        ,maybe_content_length=maybe_content_length
        #,content=content
        ,maybe_file_data=maybe_file_data
        ,content_size=content_size
        )



def _main():
    # assume:
    #   > cd /D path/to/http-server/cgi-example/
    #       # e.g. nn_ns/app/http-server/...
    #   path/to/http-server/cgi-example> py -m http.server 8000 --cgi --bind 127.0.0.2
    #

    url_root = 'http://127.0.0.2:8000/'
    url = url_root
    r = download_file(url
        , maybe_end=None, maybe_begin=None
        , header_only=True
        , maybe_output_path_or_fout=None, omode='xb'
        )
    print(r)

    print('\n'*5)
    r = download_file(url
        , maybe_end=None, maybe_begin=None
        , header_only=False
        , maybe_output_path_or_fout=None, omode='xb'
        )
    print(r)



    print('\n'*5)
    url = url_root + 'cgi-bin/hello.py'
    r = download_file(url
        , maybe_end=None, maybe_begin=None
        , header_only=True
        , maybe_output_path_or_fout=None, omode='xb'
        )
    print(r)


    print('\n'*5)
    url = url_root + 'cgi-bin/hello.py'
    r = download_file(url
        , maybe_end=None, maybe_begin=None
        , header_only=False
        , maybe_output_path_or_fout=None, omode='xb'
        )
    print(r)
if __name__ == '__main__':
    _main()

