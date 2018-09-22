'''
min(range(len(seq)), key=seq.__getitem__)
'''

__all__ = '''
    max_index_of_seq
    min_index_of_seq
    swap_pop_max_of_seq
    swap_pop_min_of_seq
    '''.split()

from seed.tiny import echo
import operator # __lt__

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



