



'''
use 'requests' 3-rd party module to POST!!!
r = requests.post(url, data=data, allow_redirects=True)
r.content

==========================
URI = scheme:[//authority]path[?query][#fragment]

authority
    authority = [userinfo@]host[:port]

query
    key1=value1&key2=value2
    key1=value1;key2=value2


ParseResult(scheme='http', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html',
            params='', query='', fragment='')
'''

__all__ = '''
    open_url
        url2content
        download_file_from_url_ex
            download_file_from_url
            url2content_data
    get_scheme_authority
    '''.split()

import urllib.request
import urllib.parse
#import json
from seed.tiny import print_err


from . import _configure_

def get_scheme_authority(url):
    # http://xxx.com:80/... -> http://xxx.com:80/
    r = urllib.parse.urlparse(url)
    parts = [r.scheme, r.netloc, '/', '', '', '']
    scheme_authority = urllib.parse.urlunparse(parts)
    return scheme_authority

def url2content_data(url, **kwargs):
    return download_file_from_url(url, **kwargs)
def download_file_from_url(url, **kwargs):
    (content_type, content_data, url_info
    ) = download_file_from_url_ex(url, **kwargs)
    return content_data


def open_url(url, *
    #, method
    , timeout, user_agent=None, referrer=None
    , data=None, encoding='utf8'
    ):
    #, cafile=None, capath=None, cadefault=False, context=None
    #print(type(url))
    #print(repr(url))
    #content_data = urllib.urlopen(url).read()
    opener = urllib.request.build_opener()

    # 'User-Agent'
    # 'Referer'

    #('User-Agent','Mozilla/5.0 (Linux; Android 4.4.4; en-us; Nexus 5 Build/JOP40D)
    #('Referer', 'http://www.python.org/')
    UserAgent = _configure_.UserAgent
    Referer = get_scheme_authority(url)
    assert type(UserAgent) is str is type(Referer)
    if user_agent is not None:
        UserAgent = user_agent
    if referrer is not None:
        Referer = referrer
    if data is not None:
        if url[-1:] != '/':
            url += '/'
            #https://stackoverflow.com/questions/3238925/python-urllib-urllib2-post

        try:
            # if data is Mapping
            #data = json.dumps(data)
            #https://docs.python.org/3/howto/urllib2.html
            data = urllib.parse.urlencode(data).encode(encoding=encoding)
        except Exception as e:
            # data is not Mapping
            #print_err(repr(e))
            pass
        #print_err(repr(data))

    opener.addheaders = [('User-Agent', UserAgent), ('Referer', Referer)]
    url_file = response = opener.open(url, timeout=timeout, data=data)
        #, cafile=cafile, capath=capath, cadefault=cadefault, context=context
    return url_file

def url2content(url, **kwargs):
    (content_type, content_data, url_info
    ) = download_file_from_url_ex(url, **kwargs)
    may_encoding = url_info.get_charset()
    #if may_encoding is None: raise Exception
    if may_encoding is None:
        encoding = 'utf8'
    else:
        encoding = may_encoding
    if type(encoding) is not str: raise Exception
    content = content_data.decode(encoding=encoding)
    return content
    with open_url(url, **kwargs) as response:
        url_info = response.info()
        content = url_info.get_payload(decode=True)
            #get_payload(): This is a legacy method. On the EmailMessage class its functionality is replaced by get_content() and iter_parts().
        if url_info.is_multipart():
            assert type(content) is list
            content = ''.join(content)
        try:
            assert type(content) is str
        except:
            print_err(type(content))#bytes???
            print_err((content))
            raise
        return content
        print(dir(url_info))
            ##url_info :: HTTPMessage <: email.message.Message
            #file:///storage/emulated/0/0my_files/unzip/py_doc/python-3.8.1-docs-html/library/email.compat32-message.html#email.message.Message
            #['__bytes__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_charset', '_default_type', '_get_params_preserve', '_headers', '_payload', '_unixfrom', 'add_header', 'as_bytes', 'as_string', 'attach', 'defects', 'del_param', 'epilogue', 'get', 'get_all', 'get_boundary', 'get_charset', 'get_charsets', 'get_content_charset', 'get_content_disposition', 'get_content_maintype', 'get_content_subtype', 'get_content_type', 'get_default_type', 'get_filename', 'get_param', 'get_params', 'get_payload', 'get_unixfrom', 'getallmatchingheaders', 'is_multipart', 'items', 'keys', 'policy', 'preamble', 'raw_items', 'replace_header', 'set_boundary', 'set_charset', 'set_default_type', 'set_param', 'set_payload', 'set_raw', 'set_type', 'set_unixfrom', 'values', 'walk']
        content = url_info.get_content()
            #AttributeError: 'HTTPMessage' object has no attribute 'get_content'
        return content

def download_file_from_url_ex(url, **kwargs):
    # url -> (content_type::str, content_data::bytes, url_info)
    #
    with open_url(url, **kwargs) as response:
        url_file = response
        content_data = url_file.read()
        #return HttpResponse(content_data, content_type='image/jpeg')
        #   hard code to 'image/jpeg'
        #

        # detect the orginal url content_type
        url_info = response.info()
        content_type = url_info.get_content_type()
        #url_info.get_content_type
        #url_info.get_content
        #url_info.get_content_charset
        return (content_type, content_data, url_info)


