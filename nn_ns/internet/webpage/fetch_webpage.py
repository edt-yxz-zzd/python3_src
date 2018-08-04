
__all__ = '''
    fetch_webpage
    open_webpage
    '''.split()

from urllib.request import urlopen # both http and https

def fetch_webpage(url):
    return open_webpage(url).read()
def open_webpage(url):
    assert url.startswith('http://') or url.startswith('https://')
    return urlopen(url)



