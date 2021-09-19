
__all__ = '''
    fetch_webpage
    open_webpage

    open_webpage_ex
    fetch_webpage__bytes
    fetch_webpage__str
    '''.split()

################ version1
from urllib.request import urlopen, Request # both http and https

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    # to avoid HTTP Error 403:Forbidden

def fetch_webpage(url):
    return open_webpage(url).read()#bytes!!!
def open_webpage(url):
    assert url.startswith('http://') or url.startswith('https://')
    #return urlopen(url)
    req = Request(url=url, headers=headers)
    return urlopen(req)


################ version2
from .download import open_url, url2content, url2content_data

def open_webpage(url, **kwargs):
    url_file, encoding = open_webpage_ex(url, **kwargs)
    return url_file
def fetch_webpage(url, **kwargs):
    return fetch_webpage__bytes(url, **kwargs)


def open_webpage_ex(url, **kwargs):
    url_file = response = open_url(url, **kwargs)
    url_info = response.info()
    encoding = url_info.get_content_charset()
    return url_file, encoding
def fetch_webpage__bytes(url, **kwargs):
    return url2content_data(url, **kwargs)
def fetch_webpage__str(url, **kwargs):
    return url2content(url, **kwargs)


