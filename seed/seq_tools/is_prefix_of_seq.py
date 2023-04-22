r'''
seed.seq_tools.is_prefix_of_seq
view ../../python3_src/seed/seq_tools/mk_slice.py
view ../../python3_src/seed/types/view/SeqSliceView.py



from seed.seq_tools.is_prefix_of_seq import is_prefix_of_seq, is_suffix_of_seq
from seed.seq_tools.is_prefix_of_seq import seq_starts_with, seq_ends_with



from seed.seq_tools.is_prefix_of_seq import len_lcp_of, lcp_of
from seed.seq_tools.is_prefix_of_seq import view_seq_ex, len_lcp_of_ex
from seed.seq_tools.is_prefix_of_seq import len_lcp_of__lsls, len_lcs_of__lsls, lcp_of__lsls, lcs_of__lsls

----fwd:

from seed.seq_tools.lcp_of import len_lcp_of, lcp_of
from seed.seq_tools.lcp_of import view_seq_ex, len_lcp_of_ex
from seed.seq_tools.lcp_of import len_lcp_of__lsls, len_lcs_of__lsls, lcp_of__lsls, lcs_of__lsls





#'''

__all__ = '''
    is_prefix_of_seq
        seq_starts_with
    is_suffix_of_seq
        seq_ends_with

    len_lcp_of
    lcp_of
    view_seq_ex
    len_lcp_of_ex


    len_lcp_of__lsls
    len_lcs_of__lsls
    lcp_of__lsls
    lcs_of__lsls
    '''.split()

from seed.seq_tools.mk_seq_rng import mk_seq_rng, mk_seq_rng__len
from seed.seq_tools.mk_slice import mk_slice
from seed.types.view.SeqSliceView import SeqSliceView
from seed.tiny import echo, check_type_is
import operator

def seq_starts_with(seq, prefix):
    return is_prefix_of_seq(prefix, seq)

def is_prefix_of_seq(prefix, seq, begin=None, end=None, *, __eq__=None):
    (begin, end) = mk_seq_rng(seq, begin, end)
    if __eq__ is None:
        __eq__ = operator.__eq__

    return len(prefix) <= (end-begin) and all(__eq__(prefix[i], seq[begin+i]) for i in range(len(prefix)))


def seq_ends_with(seq, prefix):
    return is_suffix_of_seq(suffix, seq)

def is_suffix_of_seq(suffix, seq, begin=None, end=None, *, __eq__=None):
    (begin, end) = mk_seq_rng(seq, begin, end)
    offset = end - len(suffix)
    return begin <= offset <= end and is_prefix_of_seq(suffix, seq, offset, end, __eq__=__eq__)


assert min([1,2],default=0) == 1
assert min([],default=0) == 0
def len_lcp_of(seq, /, *seqs, __eq__=None, key=None):
    L = len(min(seq, *seqs, key=len))
    if not seqs:
        return L
    if __eq__ is None:
        __eq__ = operator.__eq__
    if key is None:
        key = echo
    for i in range(L):
        x = key(seq[i])
        for ls in seqs:
            y = key(ls[i])
            if not __eq__(x,y):
                return i
    return L

def lcp_of(seq, /, *seqs, __eq__=None, key=None):
    L = len_lcp_of(seq, *seqs, __eq__=__eq__, key=key)
    return seq[:L]


def view_seq_ex(seq_ex, /):
    check_type_is(tuple, seq_ex)
    def _(seq, begin=None, end=None, /):
        return SeqSliceView(seq, mk_slice[begin:end])
    return _(*seq_ex)

def len_lcp_of_ex(seq_exs, /, *, __eq__=None, key=None):
    'Iter ([x], may begin, may end) -> *__eq__ -> *key -> uint'
    seqs = (*map(view_seq_ex, seq_exs),)
    if not seqs:
        return 0
    L = len_lcp_of(*seqs, __eq__=__eq__, key=key)
    return L








def lcp_of__lsls(default, lsls, __eq__=None, key=None):
    'lcp - longest common prefix'
    L = len_lcp_of__lsls(lsls, __eq__=__eq__, key=key)
    if not lsls:
        return default
    return lsls[0][:L]
def lcs_of__lsls(default, lsls, __eq__=None, key=None):
    'lcs - longest common suffix'
    L = len_lcs_of__lsls(lsls, __eq__=__eq__, key=key)
    if not lsls:
        return default
    ls = lsls[0]
    return ls[len(ls)-L:]



def len_lcp_of__lsls(lsls, __eq__=None, key=None):
    'lcp - longest common prefix'
    n = len(lsls)
    if not n:
        return 0
    L = min(map(len, lsls))
    if n==1:
        return L

    if __eq__ is None:
        __eq__ = operator.__eq__
    if key is None:
        key = echo

    ls0 = lsls[0]
    for i in range(L):
        x = key(ls0[i])
        for j in range(1,n):
            y = key(lsls[j][i])
            if not __eq__(x,y):
                return i
    return L
def len_lcs_of__lsls(lsls, __eq__=None, key=None):
    'lcs - longest common suffix'
    n = len(lsls)
    if not n:
        return 0
    L = min(map(len, lsls))
    if n==1:
        return L

    if __eq__ is None:
        __eq__ = operator.__eq__
    if key is None:
        key = echo

    ls0 = lsls[0]
    for i in reversed(range(-L,0)):
        x = key(ls0[i])
        for j in range(1,n):
            y = key(lsls[j][i])
            if not __eq__(x,y):
                return -1-i
    return L

