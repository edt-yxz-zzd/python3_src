'''
plantri -a [-u] [-V] -d -v -<c2x|c3>m3 <cubic_graph_order>d [output_file]



-a // for imbedding !!!! 
  ASCII CODE is a human-readable version of planar code.  The vertices of
     the graph are named by ASCII characters starting with 'a'.  Example:
        7 bcdefg,agfdc,abd,acbfe,adf,aedbg,afb
     This is a graph with 7 vertices a,b,c,d,e,f,g.  The neighbours of
     'a' in clockwise order are b,c,d,e,f,g; and so on.  Each graph occupies
     one line of output.  Ascii code is convenient if you just want to draw
     a few graphs by hand.
     To select ascii code use -a.

'''

import re

def _check_embedding(embedding):
    n = len(embedding)
    for neighbors in embedding:
        for j in neighbors:
            if not 0 <= j < n:
                return False

    return True


def _assert(b):
    if not b: raise 'not ASCII CODE format'
    
    
def str2embedding(g):
    m = re.search(r'^\d+ *', g)
    _assert(m != None)
    n = int(m.group())
    _assert(0 < n <= 26)

    ls = re.split(r'(,)', g[m.end():], n-1)
    _assert(len(ls) == n + n-1)
    embedding = tuple(tuple(ord(c)-ord('a') for c in s) for s in ls[::2])
    _assert(_check_embedding(embedding))
    return embedding



def embedding2str(embedding):
    _assert(_check_embedding(embedding))
    ls = [str(len(embedding)), ' ']
    for neighbors in embedding:
        tmp = list(chr(i + ord('a')) for i in neighbors)
        ls.append(''.join(tmp))
        ls.append(',')

    ls.pop()
    return ''.join(ls)
    
        
def read_file(path):
    ls = []
    with open(path) as f:
        for line in f:
            s = line[:-1]
            e = str2embedding(s)
            #w = embedding2str(e)
            #assert s == w
            ls.append(e)

    return ls

def write_file(path, iterable):
    with open(path, 'x') as f:
        for embedding in iterable:
            f.write(embedding2str(embedding))
            f.write('\n')

    

    
    
def t():
    print(read_file('txt/aVdc3m3_from4to16d.txt'))









