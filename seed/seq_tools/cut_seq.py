#__all__:goto
r'''[[[
e ../../python3_src/seed/seq_tools/cut_seq.py

seed.seq_tools.cut_seq
py -m nn_ns.app.debug_cmd   seed.seq_tools.cut_seq
py -m nn_ns.app.adhoc_argparser__main__call8module   seed.seq_tools.cut_seq   @f
py -m nn_ns.app.doctest_cmd seed.seq_tools.cut_seq:__doc__ -v

from seed.seq_tools.cut_seq import cut_seq_, icut_seq_

#]]]'''
__all__ = r'''
    cut_seq_
    icut_seq_
'''.split()#'''
__all__

from seed.iters.icut_to import icut_to, icut_seq_to
from seed.seq_tools.mk_seq_rng import mk_seq_rng, mk_seq_rng__len

def cut_seq_(sz4block, seq, begin=0, end=None, /):
    return (*icut_seq_(sz4block, seq, begin, end),)
def icut_seq_(sz4block, seq, begin=0, end=None, /):
    (begin, end) = mk_seq_rng(seq, begin, end)
    sz_used = max(0, end-begin)
    q,r = divmod(sz_used,sz4block)
    if r:raise ValueError('LenError')
    return icut_seq_to(seq, sz4block, begin, end)


from seed.seq_tools.cut_seq import cut_seq_, icut_seq_
