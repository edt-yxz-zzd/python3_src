#!py -2


# http_img_viewer

encoding = 'mbcs'

import sys
reload(sys)
#sys.setdefaultencoding('gb18030')
sys.setdefaultencoding(encoding)

import os

from twisted.web import http
from twisted.internet import reactor
from twisted.web.resource import Resource, NoResource
from twisted.web.server import Site
from twisted.web.static import File

path = r'E:\my_data\program_source\python3_src\root\internet\download_comic\getComic-master\yhzp'

home_page_tpl = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"> 
<html xmlns="http://www.w3.org/1999/xhtml"> 
<head> 
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" /> 
<title>{title}</title>
</head> 

<body>
<!-- list of links -->
{links}
</body> 
</html>
'''

home_page_link_tpl = r'<a href="{link}">{name}</a>'
chapter_page_link_tpl = r'<img src="{link}" alt="{name}" width="100%">'

def path2dirs(path):
    names = []
    for name in os.listdir(path):
        fname = os.path.join(path, name)
        if os.path.isdir(fname):
           names.append(name)
    return names

def path2files(path):
    names = []
    for name in os.listdir(path):
        fname = os.path.join(path, name)
        if not os.path.isdir(fname):
           names.append(name)
    return names


class HomePage(Resource):
    next_class = None
    link_tpl = home_page_link_tpl

    def path2names(self):
        return path2dirs(self.path)

    
    def __init__(self, path, title = 'view comics', prefix = ''):
        Resource.__init__(self)
        self.path = path
        self.prefix = prefix
        self.title = title

    def render_GET(self, request):
        #print('render_GET', type(self))

        #print(self.path)
        try:
            names = self.path2names()
        except:
            request.setResponseCode(http.NOT_FOUND)
            return None

        links = []
        for name in names:
            links.append(self.link_tpl.format(link = self.prefix + '/' + name, name = name))
            
        htm = home_page_tpl.format(title = self.title, links = '\n<p />\n'.join(links))
        #print(htm)
        return htm.encode('utf-8')

    def _child(self, path, title, prefix):
        return self.next_class(path, title, prefix)
    
    def getChild(self, name, request):
        #print('getChild', type(self))

        #name = name.encode('ascii')
        #print('name = ', name, type(name))
        name = bytearray(ord(c) for c in name)
        name = name.decode('utf-8')
        if name == self.prefix:
            return self

        try:
            fname = os.path.join(self.path, name)
            return self._child(fname, os.path.basename(name), name)
        
        except:
            return NoResource()


class ComicPage(HomePage):
    next_class = None


class ChapterPage(HomePage):
    link_tpl = chapter_page_link_tpl

    def path2names(self):
        #print('path2names')
        return path2files(self.path)


    def _child(self, path, title, prefix):
        #print(path, title, prefix)
        return File(path)
    


    

HomePage.next_class = ComicPage
ComicPage.next_class = ChapterPage

root = HomePage(path)
factory = Site(root)

reactor.listenTCP(8000, factory)
reactor.run()

