



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
    with open_url(url, **kwargs) as response:
        url_info = response.info()
        content = url_info.get_content()
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


