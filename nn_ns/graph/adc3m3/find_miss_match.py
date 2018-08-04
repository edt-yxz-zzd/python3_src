
import sys

from graph.triconnected_planar_graph_isomorphism import \
     canonize_triconnected_planar_simple_graph
from graph.simple_undirected_graph import graph
from graph.graph_format_ascii_embedding import str2embedding


def _canon_label(s):
    embedding = str2embedding(s)
    g = graph(embedding)
    adj_ls, ordering = canonize_triconnected_planar_simple_graph(g)
    assert adj_ls[0][0] == 1
    #assert all(adj_ls[v][0] == v-1 for v in range(1, g.nv()))
    return repr(adj_ls)


def calc_lineno2pos(fin):
    
    fin.seek(0)
    ls = []
    while fin:
        ls.append(fin.tell())
        line = fin.readline()
        if not line:
            break
        
    else:
        print('not fin')
    ls.pop()

    print('bool(fin)', bool(fin))
    return ls


def decode(abc):
    assert abc[-1] == '\n'
    tupl = _canon_label(abc[:-1])+'\n'
    return tupl

def rnglen(rng):
    begin, end = rng
    return end-begin
def rngmid(rng):
    begin, end = rng
    return (end+begin)//2
def to_offset(rng, mid):
    begin, end = rng
    assert begin <= mid < end
    return mid-begin
def from_offset(rng, offset):
    begin, end = rng
    assert 0 <= offset < end-begin
    return begin+offset
    

def headtail(ls, rng):
    begin, end = rng
    if begin == end:
        return []
    if begin == end-1:
        return ls[begin]
    return ls[begin], ls[end-1]

def filepos2line(fin, pos):
    fin.seek(pos)
    return fin.readline()

def find_diff(cnn, tuple_no2pos, trng, txt, abc_no2pos, arng):
    tL = rnglen(trng)
    aL = rnglen(arng)
    if tL == aL:
        raise
        tht = headtail(tuple_no2pos, trng)
        aht = headtail(abc_no2pos, arng)
        bools = [filepos2line(cnn, tpos) == decode(filepos2line(txt, apos))
                 for tpos, apos in zip(tht, aht)]
        if all(bools):
            return None
        if not any(bools):
            raise ValueError('all miss match', trng, arng)
            
    elif tL > aL:
        raise logic-error
    else:
        
        assert tL + 1 == aL
        if tL == 0:
            return trng
        
        tmid = rngmid(trng)
        amid = from_offset(arng, to_offset(trng, tmid))

        t = filepos2line(cnn, tuple_no2pos[tmid])
        a = filepos2line(txt, abc_no2pos[amid])
        tbegin, tend = trng
        abegin, aend = arng
        if t != decode(a):
            b = filepos2line(txt, abc_no2pos[amid+1])
            assert t == decode(b)
            
            return find_diff(cnn, tuple_no2pos, (tbegin, tmid),
                             txt, abc_no2pos, (abegin, amid+1))
        else:
            return find_diff(cnn, tuple_no2pos, (tmid+1, tend),
                             txt, abc_no2pos, (amid+1, aend))
    raise


def diff_cnn_txt(cnn_fn, txt_fn):
    with open(cnn_fn) as cnn, open(txt_fn) as txt:
        tuple_no2pos = calc_lineno2pos(cnn)
        abc_no2pos = calc_lineno2pos(txt)
        tL = len(tuple_no2pos)
        aL = len(abc_no2pos)
        r = find_diff(cnn, tuple_no2pos, (0, tL), txt, abc_no2pos, (0, aL))
        return r

txt_fn = './-adc3m3[4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24].txt'
#txt_fn = './-adc3m3[4, 6, 8].txt'

cnn_fn = txt_fn + '.cnn'
print(diff_cnn_txt(cnn_fn, txt_fn))













    
    

