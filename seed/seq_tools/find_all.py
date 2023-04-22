#__all__:goto
r'''[[[
e ../../python3_src/seed/seq_tools/find_all.py
seed.seq_tools.find_all

py -m nn_ns.app.debug_cmd   seed.seq_tools.find_all
py -m nn_ns.app.adhoc_argparser__main__call8module   seed.seq_tools.find_all   @f
py -m nn_ns.app.doctest_cmd seed.seq_tools.find_all:__doc__ -v


from seed.seq_tools.find_all import find_all_, iter_all_

>>> from seed.seq_tools.find_all import find_all_, iter_all_
>>> whole = 'ababababa'
>>> sub = 'aba'
>>> find_all_(sub, whole)
[0, 4]
>>> find_all_(sub, [*whole])
[0, 4]



#]]]'''
__all__ = r'''
    find_all_
    iter_all_
'''.split()#'''
__all__

from seed.tiny import null_iter, check_callable
from seed.seq_tools.mk_seq_rng import mk_seq_rng# mk_seq_rng__len
from seed.iters.find import iter_search_subseq_on_seq, iter_search_subseq_on_stream
#def iter_search_subseq_on_seq(seq, subseq, *, overlap:bool, last_pos2restart_pos=None, _ver=None, offset=0):
#def iter_search_subseq_on_stream(istream, subseq, *, overlap:bool, last_pos2restart_pos=None, _ver=None, offset=0):

def _():
  def find_all_(sub, whole, /):
    L = max(1,len(sub))
    N = len(whole)
    ls = []
    i = whole.find(sub, 0)
    while 0 <= i <= N:
        ls.append(i)
        i = whole.find(sub, i+L)
    return ls
def find_all_(sub, whole, begin=None, end=None, /, *, finder=None, _max_sz4direct_search=None):
    return [*iter_all_(sub, whole, begin, end, finder=finder, _max_sz4direct_search=_max_sz4direct_search)]
def iter_all_(sub, whole, begin=None, end=None, /, *, finder=None, _max_sz4direct_search=None):
    sub[:0]
    whole[:0]
    (begin, end) = mk_seq_rng(whole, begin, end)
    if end < begin or len(whole) < len(sub):
        return null_iter
    if not sub:
        return iter(range(begin, end+1))

    if finder is None:
        finder = getattr(type(whole), 'find', None)
    if not finder is None:
        check_callable(finder)

    if _max_sz4direct_search is None:
        _max_sz4direct_search = 9
    if not (finder is None or _max_sz4direct_search < len(sub)):
        t0 = type(whole)
        t1 = type(sub)
        if t0 is str is t1 or {t0,t1} <= {bytes, bytearray}:
            return _iter_all__1(finder, sub, whole, begin, end)
        else:
            pass
    else:
        pass
    return _iter_all__2(sub, whole, begin, end)


def _iter_all__2(sub, whole, begin, end, /):
    L = len(sub)
    ilast = end-L
    for i in iter_search_subseq_on_seq(whole, sub, overlap=False, offset=begin):
        if ilast < i:
            break
        yield i
def _iter_all__1(finder, sub, whole, begin, end, /):
    L1 = max(1,len(sub))
    i = finder(whole, sub, begin, end)
    while not i < 0:
        yield i
        i = finder(whole, sub, i+L1, end)
    return




from seed.seq_tools.find_all import find_all_, iter_all_

