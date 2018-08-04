
import sys

from graph.triconnected_planar_graph_isomorphism import \
     canonize_triconnected_planar_simple_graph
from graph.simple_undirected_graph import graph
from graph.graph_format_ascii_embedding import str2embedding

fpath = './-adc3m3[4, 6, 8].txt'

def canon_c3(fname, from_line=0):
    fname_out = fname + '.cnn'
    with open(fname) as fin, open(fname_out, 'a') as fout:
        ifin = iter(fin)
        try:
            i = 0
            for i, line in enumerate(ifin, start=i):
                if i < from_line: continue
                s = _canon_label(line[:-1])
                fout.write(s+'\n')
        except:
            print('fail at line:', i, file=sys.stderr)
            raise
    return



def num2char(n):
    if not 0 <= n < 36:
        raise ValueError('not 0 <= n < 36')
    if n < 10:
        return chr(ord('0') + n)
    return chr(ord('A') + n)
    return num2char.table[n]

num2char.table = ''.join(chr(i) for i in range(ord('0'), ord('9')+1)) \
                 + ''.join(chr(i) for i in range(ord('A'), ord('Z')+1))

def char2num(c):
    i = ord(c)
    if ord('0') <= i <= ord('9'):
        return i - ord('0')
    
    if ord('A') <= i <= ord('Z'):
        return i - ord('A')
    raise ValueError('c should be [0-9A-Z]')


def adj_ls2str(adj_ls):
    ls = ['(']
    for ns in adj_ls:
        for v in ns:
            ls.append(num2char(v))
        ls.append(',')
    ls.append(')')
    return ''.join(ls)

    


def _canon_label(s):
    embedding = str2embedding(s)
    g = graph(embedding)
    adj_ls, ordering = canonize_triconnected_planar_simple_graph(g)
    assert adj_ls[0][0] == 1
    #assert all(adj_ls[v][0] == v-1 for v in range(1, g.nv()))
    return adj_ls2str(adj_ls) #repr(adj_ls)



canon_c3(fpath, from_line=0)
if 0:
    fpath = './-adc3m3[4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24].txt'
    #canon_c3(fpath, from_line=43771)
    canon_c3(fpath, from_line=398437)#293936)#251659)#36882)












    
