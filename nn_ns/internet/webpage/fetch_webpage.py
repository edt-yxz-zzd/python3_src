
__all__ = '''
    fetch_webpage
    open_webpage
    '''.split()

from urllib.request import urlopen, Request # both http and https

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    # to avoid HTTP Error 403:Forbidden

def fetch_webpage(url):
    return open_webpage(url).read()
def open_webpage(url):
    assert url.startswith('http://') or url.startswith('https://')
    #return urlopen(url)
    req = Request(url=url, headers=headers)
    return urlopen(req)



