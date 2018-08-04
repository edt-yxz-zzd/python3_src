
path = r'E:/my_data/program_source/python3_src/internet/'
url = 'http://img1.comic.zongheng.com/comic/series/2013/4/xiefengmanhua/15/svol_20130506094816647724.jpg'


class a:
    def __init__(self):
        self.0 = ''

a()
raise 0

def a(*args, **k):
    print(args, k)

def b(*args):
    a(*args)

def c(*args, **k):
    b(*args, **k)

c(1,2,3)
b('', a='')#error

raise 0

import concurrent.futures
import urllib.request

# Retrieve a single page and report the url and contents
def load_url(url, timeout):
    conn = urllib.request.urlopen(url, timeout=timeout)
    return conn.readall()

print(load_url(url, timeout=1)[:20])

raise 0


with open(path+'log.txt', 'x') as log:
    log.write(url)
    log.write(0)

raise 0
def f(url):
    req = urllib.request.Request(url, headers=\
        {"Content-Type":"application/x-www-form-urlencoded;charset=utf-8",\
         'Accept': 'text/html, image/gif, image/jpeg, */*', \
         # if server return:
         #    Content-Length=106786028
         #    Accept-Ranges=bytes
         #    Content-Type=application/octet-stream
         #'RANGE': 'bytes=468500-', \
         }, method='HEAD')
    #req = urllib.request.Request(url, headers=\
    #    {"Content-Type":" application/x-www-form-urlencoded;charset=utf-8"}, method='HEAD')
    #req.info()
    #clen = 'Content-Length'
    
    '''
    'Content-Length'
    'Last-Modified'
    'Content-Type'
    ??'Accept-Ranges': 'bytes'
    '''
    with urllib.request.urlopen(req) as httpr:
        head = dict(httpr.headers)
        print(head)
        #if clen in head:
        #    print('{} = {}'.format(clen, head[clen]))
        file = httpr.readall()
        print(file)

    return txt



  
def f():
    with open(path+'tmp.dat', 'xb') as fout:
        fout.seek(1)
        fout.write(b'1')


def f():
    for i in range(5):
        if i: raise Exception()
        yield i

def t():
    for i in f():
        print(i)

t()



class base:
    def __init__(self):
        print('base', type(self))


class d(base):
    def __init__(self):
        print('d', type(self))
base()
d()

class c:
    def __init__(self):
        print(c)
        self.a()
    def a(self):
        self.b = '2'
e = c()
print(e.b)

class e(c, d):
    def __init__(self):
        print(e, e.__mro__)

class f(d,c):
    def __init__(self):
        print(f, f.__mro__)

e()
f()

class g(f):
    def __init__(self):
        print(g, g.__mro__)
        
        print('base')
        super(base).__init__()
        print('d')
        super(d).__init__()

        print('d, self')
        super(d, self).__init__()

g()

class g1(g):pass
class g2(g1):
    def __init__(self):
        print(g2, g2.__mro__)
        super().__init__()
        

g2()
print('g1.__init__ ==', g1.__init__)

for attr in dir(g1.__init__):
    print(attr, getattr(g1.__init__, attr))
g1.__init__.__qualname__

def f():
    class a:
        class b:
            def c(self):pass
        def rb(self):
            return a().b()
    d = a()
    return d.rb().c


def get_class_qualname(bounded_class_method):
    n = bounded_class_method.__name__
    q = bounded_class_method.__qualname__
    #g = bounded_method.__globals__
    class_qualname = q[:-1-len(n)]
    return class_qualname
print(get_class_qualname(g1.__init__))
def get_class(bounded_method):
    n = bounded_method.__name__
    q = bounded_method.__qualname__
    #g = bounded_method.__globals__
    c = q[:-1-len(n)]
    sub = bounded_method.__self__.__class__
    for t in sub.mro():
        print(t)
        if t.__qualname__ == c:
            return t
    raise ''
    #t = g[c]

get_class(g1.__init__)

print(get_class(f()))

class g(e,f): #MRO failed!!!
    def __init__(self):
        print(g, g.__mro__)


        
class c:
    def a(self): #error
        self.b = '2'
d = c()
print(d.b)

import collections
de = collections.deque([1,2])
ls = [3,4]
for e in de: #error
    if ls:
        de.append(ls.pop())

print(de)
    

class q(d):
    pass

print(issubclass(q,base))

class c(base, d): #fail!!!
    pass


