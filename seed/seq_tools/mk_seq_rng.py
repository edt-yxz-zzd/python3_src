
r'''
seed.seq_tools.mk_seq_rng
from seed.seq_tools.mk_seq_rng import mk_seq_rng, mk_seq_rng__len

-> (begin, end)

py -m nn_ns.app.debug_cmd   seed.seq_tools.mk_seq_rng
py -m nn_ns.app.doctest_cmd seed.seq_tools.mk_seq_rng:__doc__ -ff -v


>>> slice(-7,7).indices(5)
(0, 5, 1)
>>> slice(-5,5).indices(5)
(0, 5, 1)

>>> slice(-3,-3).indices(5)
(2, 2, 1)
>>> slice(-3,-4).indices(5)
(2, 1, 1)
>>> slice(-4,-3).indices(5)
(1, 2, 1)


>>> slice(-4,-3).indices(-5)
Traceback (most recent call last):
  ...
ValueError: length should not be negative
>>> slice(-4,-3).indices(0)
(0, 0, 1)

>>> slice(-9,-8).indices(5)
(0, 0, 1)
>>> slice(8,9).indices(5)
(5, 5, 1)











>>> mk_seq_rng__len(0, 0, 0)
(0, 0)
>>> mk_seq_rng__len(-1, 0, 0)
Traceback (most recent call last):
  ...
ValueError
>>> mk_seq_rng__len(0, -1, 0)
Traceback (most recent call last):
  ...
ValueError
>>> mk_seq_rng__len(0, 0, -1)
Traceback (most recent call last):
  ...
ValueError
>>> mk_seq_rng__len(0, 1, 0)
Traceback (most recent call last):
  ...
ValueError
>>> mk_seq_rng__len(0, 0, 1)
Traceback (most recent call last):
  ...
ValueError











>>> mk_seq_rng__len(0, 0, 0, strict=True)
(0, 0)
>>> mk_seq_rng__len(-1, 0, 0, strict=True)
Traceback (most recent call last):
  ...
ValueError
>>> mk_seq_rng__len(0, -1, 0, strict=True)
Traceback (most recent call last):
  ...
ValueError
>>> mk_seq_rng__len(0, 0, -1, strict=True)
Traceback (most recent call last):
  ...
ValueError
>>> mk_seq_rng__len(0, 1, 0, strict=True)
Traceback (most recent call last):
  ...
ValueError
>>> mk_seq_rng__len(0, 0, 1, strict=True)
Traceback (most recent call last):
  ...
ValueError
>>> mk_seq_rng__len(0, 1, 1, strict=True)
Traceback (most recent call last):
  ...
ValueError
>>> mk_seq_rng__len(0, -1, -1, strict=True)
Traceback (most recent call last):
  ...
ValueError
>>> mk_seq_rng__len(5, 0, 5, strict=True)
(0, 5)
>>> mk_seq_rng__len(5, 5, 0, strict=True)
Traceback (most recent call last):
  ...
ValueError
>>> mk_seq_rng__len(5, 4, 3, strict=True)
Traceback (most recent call last):
  ...
ValueError
>>> mk_seq_rng__len(5, 3, 3, strict=True)
(3, 3)
>>> mk_seq_rng__len(5, 3, 4, strict=True)
(3, 4)
>>> mk_seq_rng__len(5, None, 5, strict=True)
(0, 5)
>>> mk_seq_rng__len(5, 0, None, strict=True)
(0, 5)
>>> mk_seq_rng__len(5, -5, 5, strict=True)
(0, 5)
>>> mk_seq_rng__len(5, 0, -5, strict=True)
(0, 0)
>>> mk_seq_rng__len(5, 5, 5, strict=True)
(5, 5)
>>> mk_seq_rng__len(5, 0, 5, strict=True)
(0, 5)
>>> mk_seq_rng__len(5, -6, 5, strict=True)
Traceback (most recent call last):
  ...
ValueError
>>> mk_seq_rng__len(5, 0, -6, strict=True)
Traceback (most recent call last):
  ...
ValueError
>>> mk_seq_rng__len(5, 6, 5, strict=True)
Traceback (most recent call last):
  ...
ValueError
>>> mk_seq_rng__len(5, 0, 6, strict=True)
Traceback (most recent call last):
  ...
ValueError
>>> mk_seq_rng__len(5, 6, 6, strict=True)
Traceback (most recent call last):
  ...
ValueError
>>> mk_seq_rng__len(5, -6, -6, strict=True)
Traceback (most recent call last):
  ...
ValueError















>>> mk_seq_rng__len(0, 0, 0, strict=False)
(0, 0)
>>> mk_seq_rng__len(-1, 0, 0, strict=False)
Traceback (most recent call last):
  ...
ValueError
>>> mk_seq_rng__len(0, -1, 0, strict=False)
(0, 0)
>>> mk_seq_rng__len(0, 0, -1, strict=False)
(0, 0)
>>> mk_seq_rng__len(0, 1, 0, strict=False)
(0, 0)
>>> mk_seq_rng__len(0, 0, 1, strict=False)
(0, 0)
>>> mk_seq_rng__len(0, 1, 1, strict=False)
(0, 0)
>>> mk_seq_rng__len(0, -1, -1, strict=False)
(0, 0)
>>> mk_seq_rng__len(5, 0, 5, strict=False)
(0, 5)
>>> mk_seq_rng__len(5, 5, 0, strict=False)
(5, 0)
>>> mk_seq_rng__len(5, 4, 3, strict=False)
(4, 3)
>>> mk_seq_rng__len(5, 3, 3, strict=False)
(3, 3)
>>> mk_seq_rng__len(5, 3, 4, strict=False)
(3, 4)
>>> mk_seq_rng__len(5, None, 5, strict=False)
(0, 5)
>>> mk_seq_rng__len(5, 0, None, strict=False)
(0, 5)
>>> mk_seq_rng__len(5, -5, 5, strict=False)
(0, 5)
>>> mk_seq_rng__len(5, 0, -5, strict=False)
(0, 0)
>>> mk_seq_rng__len(5, 5, 5, strict=False)
(5, 5)
>>> mk_seq_rng__len(5, 0, 5, strict=False)
(0, 5)
>>> mk_seq_rng__len(5, -6, 5, strict=False)
(0, 5)
>>> mk_seq_rng__len(5, 0, -6, strict=False)
(0, 0)
>>> mk_seq_rng__len(5, 6, 5, strict=False)
(5, 5)
>>> mk_seq_rng__len(5, 0, 6, strict=False)
(0, 5)
>>> mk_seq_rng__len(5, 6, 6, strict=False)
(5, 5)
>>> mk_seq_rng__len(5, -6, -6, strict=False)
(0, 0)










#'''

__all__ = '''
    mk_seq_rng__len
    mk_seq_rng
    '''.split()


assert slice(-7,7).indices(5) == (0, 5, 1)
assert slice(-3,-3).indices(5) == (2, 2, 1)
assert slice(-3,-4).indices(5) == (2, 1, 1)
assert slice(-4,-3).indices(5) == (1, 2, 1)
assert slice(-9,-8).indices(5) == (0, 0, 1)
assert slice(8,9).indices(5) == (5, 5, 1)

def _bound_(m,M, i, /):
    '-> max(m,min(M,i))'
    assert m <= M
    if i < m:
        i = m
    elif M < i:
        i = M
    return i

def mk_seq_rng__len(seq_len, /, begin, end, *, strict=True):
    rng1 = _1_mk_seq_rng__len(seq_len, begin, end, strict=strict)
    rng2 = _2_mk_seq_rng__len(seq_len, begin, end)
    #if strict:
    if 1:
        assert rng1 == rng2
            #strict=False ==>> eqv
            #strict=True ==>> eqv or ^ValueError above
    return rng1
def _2_mk_seq_rng__len(seq_len, /, begin, end):
    begin, end, _ = slice(begin, end).indices(seq_len)
    return (begin, end)
def _1_mk_seq_rng__len(seq_len, /, begin, end, *, strict):
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
    if strict:
        if not begin >= 0: raise ValueError
        if not end >= 0: raise ValueError
        if not 0 <= begin <= end <= seq_len: raise ValueError
    else:
        begin = _bound_(0, seq_len, begin)
        end = _bound_(0, seq_len, end)
        # maybe [end < begin]
    return begin, end

def mk_seq_rng(seq, /, begin, end, *, strict=True):
    return mk_seq_rng__len(len(seq), begin, end, strict=strict)




