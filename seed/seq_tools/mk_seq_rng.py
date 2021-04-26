
r'''
seed.seq_tools.mk_seq_rng
from seed.seq_tools.mk_seq_rng import mk_seq_rng, mk_seq_rng__len

-> (begin, end)
#'''

__all__ = '''
    mk_seq_rng__len
    mk_seq_rng
    '''.split()


def mk_seq_rng__len(seq_len, /, begin, end):
    if not type(seq_len) is int: raise TypeError
    if not seq_len >= 0: raise ValueError

    if begin is None:
        begin = 0
    if end is None:
        end = seq_len
    if not type(begin) is int: raise TypeError
    if not type(end) is int: raise TypeError

    if begin < 0:
        begin += seq_len
    if end < 0:
        end += seq_len

    if not begin >= 0: raise ValueError
    if not end >= 0: raise ValueError
    if not 0 <= begin <= end <= seq_len: raise ValueError
    return begin, end

def mk_seq_rng(seq, /, begin, end):
    return mk_seq_rng__len(len(seq), begin, end)




