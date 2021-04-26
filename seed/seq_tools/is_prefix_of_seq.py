r'''
seed.seq_tools.is_prefix_of_seq
from seed.seq_tools.is_prefix_of_seq import is_prefix_of_seq, is_suffix_of_seq
from seed.seq_tools.is_prefix_of_seq import seq_starts_with, seq_ends_with

#'''

__all__ = '''
    is_prefix_of_seq
        seq_starts_with
    is_suffix_of_seq
        seq_ends_with
    '''.split()

from seed.seq_tools.mk_seq_rng import mk_seq_rng, mk_seq_rng__len
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


