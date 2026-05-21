'''
min(range(len(seq)), key=seq.__getitem__)

seed.seq_tools.min_index_of_seq
py -m nn_ns.app.debug_cmd   seed.seq_tools.min_index_of_seq -x
py -m nn_ns.app.doctest_cmd seed.seq_tools.min_index_of_seq:__doc__ -ht #  -ff -v -df
'''

__all__ = '''
    max_index_of_seq
    min_index_of_seq
    swap_pop_max_of_seq
    swap_pop_min_of_seq
    '''.split()

___begin_mark_of_excluded_global_names__0___ = ...
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.funcs import echo

#import operator # __lt__
___end_mark_of_excluded_global_names__0___ = ...

def max_index_of_seq(seq, *, key=None):#, __lt__=None):
    if key is None:
        key = echo
    return max(range(len(seq)), key=lambda i: key(seq[i]))
def min_index_of_seq(seq, *, key=None):#, __lt__=None):
    if key is None:
        key = echo
    return min(range(len(seq)), key=lambda i: key(seq[i]))
def swap_pop_max_of_seq(seq, *, key=None):
    idx = max_index_of_seq(seq, key=key)
    last = seq.pop()
    if idx+1 == len(seq):
        max = last
    else:
        seq[idx], max = last, seq[idx] # swap
    return max

def swap_pop_min_of_seq(seq, *, key=None):
    idx = min_index_of_seq(seq, key=key)
    last = seq.pop()
    if idx+1 == len(seq):
        min = last
    else:
        seq[idx], min = last, seq[idx] # swap
    return min



from seed.seq_tools.min_index_of_seq import max_index_of_seq, min_index_of_seq, swap_pop_max_of_seq, swap_pop_min_of_seq
from seed.seq_tools.min_index_of_seq import *
