from django.shortcuts import render

# Create your views here.

#new:
from django.http import HttpResponse
import urllib.request
import urllib.parse

'''
try:
    from .. import mzitu_com_project
    from ..mzitu_com_project.DATA import proxy_php_fname
except (ImportError, ValueError):
    import mzitu_com_project
    from mzitu_com_project.DATA import proxy_php_fname

from pathlib import PurePath as Path
proxy_php_path = Path(mzitu_com_project.__file__).parent / proxy_php_fname
proxy_php_bytes = proxy_php_path.read_bytes()
def proxy_php_file_as_view(request):
'''


'''
URI = scheme:[//authority]path[?query][#fragment]

authority
    authority = [userinfo@]host[:port]

query
    key1=value1&key2=value2
    key1=value1;key2=value2


ParseResult(scheme='http', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html',
            params='', query='', fragment='')

HTTP URL vs Django URL?
    ?? https://stackoverflow.com/questions/4591525/is-it-possible-to-pass-query-parameters-via-djangos-url-template-tag

    HTTP URL
        http://example.com/myview?office=foobar
        #                       ^^^
    Django URL
        http://example.com/myview/
        #??? http://example.com/myview/?office=foobar ???
        #                            ^^^
        #
        #
        # query is not part of Django URL!!!
        # SHOULD remove '?....' from urlpatterns
        # a fail example:
        #   Request URL: http://127.0.0.1:8000/echo_image/?url=https://i.meizitu.net/2018/12/28f02.jpg
        #   Using the URLconf defined in mzitu_com_project.urls, Django tried these URL patterns, in this order:
        #   1. admin/
        #   2. (?=old/|all/|new/)
        #   3. per/
        #   4. echo_image/ [?]url=.+$
        #   5. index/
        #   6. [name='main_index']
        #   The current path, echo_image/, didn't match any of these.

'''
def get_scheme_authority(url):
    r = urllib.parse.urlparse(url)
    parts = [r.scheme, r.netloc, '/', '', '', '']
    scheme_authority = urllib.parse.urlunparse(parts)
    return scheme_authority
def download_image_file_as_view(request):
    # from:
    #   https://blog.csdn.net/qq_33733970/article/details/77876675
    #   Python3爬虫之图片防盗链破解
    #
    #   https://blog.csdn.net/quikai1981/article/details/52494723
    #   python 3.3 下载带有防盗链的文件

    if request.method == 'GET':
        # http://www.../echo_image?url=<img_url>
        # 'User-Agent'
        # 'Referer'
        url = request.GET['url'] # ''imgurl' -> 'url'
        #print(type(url))
        #print(repr(url))
        #image_data = urllib.urlopen(url).read()
        opener = urllib.request.build_opener()


        #('User-Agent','Mozilla/5.0 (Linux; Android 4.4.4; en-us; Nexus 5 Build/JOP40D)
        #('Referer', 'http://www.python.org/')
        UserAgent = r'Mozilla/5.0 (Linux; Android 4.4.4; en-us; Nexus 5 Build/JOP40D)'
        Referer = get_scheme_authority(url)
        assert type(UserAgent) is str is type(Referer)

        opener.addheaders = [('User-Agent', UserAgent), ('Referer', Referer)]
        image_file = response = opener.open(url)
        image_data = image_file.read()
        #return HttpResponse(image_data, content_type='image/jpeg')
        #   hard code to 'image/jpeg'
        #

        # detect the orginal url content_type
        url_info = response.info()
        content_type = url_info.get_content_type()
        return HttpResponse(image_data, content_type=content_type)
    else:
        pass


