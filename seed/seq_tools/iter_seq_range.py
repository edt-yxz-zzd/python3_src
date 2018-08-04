
__all__ = '''
    seq_islice
    enumerate_seq
    iter_seq_range
    std_seq_range
    '''.split()

from seed.tiny import ifNone

def seq_islice(seq, begin ,end, step=None, *, reverse=False):
    for i in iter_seq_range(len(seq), begin, end, step, reverse=reverse):
        yield seq[i]
def enumerate_seq(seq, begin ,end, step=None, *, reverse=False):
    for i in iter_seq_range(len(seq), begin, end, step, reverse=reverse):
        yield i, seq[i]

def iter_seq_range(L, begin ,end, step=None, *, reverse=False):
    if step is None:
        step = 1
    if step <= 0:
        return ValueError('step <= 0')
    begin, end = std_seq_range(L, begin, end)
    if reverse:
        return range(end-1, begin-1, -step)
    else:
        return range(begin, end, step)

def std_seq_range(L, begin, end):
    # input:
    #   L = len(seq)
    #   begin :: None | int
    #   end :: None | int
    # outpur:
    #   if empty range: return (0, 0)
    #   else:           return (begin', end') # [begin:end] /\ [0:L]
    #       where 0 <= begin' < end' <= L
    if L <= 0:
        if L == 0:
            return (0,0)
        return ValueError('seq len < 0')
    begin = ifNone(begin, 0)
    end = ifNone(end, L)

    if begin < 0:   begin += L
    if end < 0:     end += L
    if begin < 0 or end < 0: raise IndexError('begin or end out-of-range')

    if begin > L: begin = L
    if end > L: end = L
    if end <= begin:
        return (0,0)

    assert 0 <= begin < end <= L
    return (begin, end)
