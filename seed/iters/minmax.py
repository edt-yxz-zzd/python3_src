
__all__ = '''
    minmax_default
    minmax_fdefault
    maybe_minmax
    UsingLeInsteadOfLt
'''.split()

#from seed.special_funcs import identity
from seed.tiny import echo
import operator

def minmax_default(default, iterable, *, key=None, __lt__=None):
    '''return (default, default) | (only_element, only_element) | (first_min, last_max)

not cmp with default

example:
    # default
    >>> minmax_default(None, [])
    >>> minmax_default((None, None), [])
    (None, None)
    >>> minmax_default((0, -1), [])
    (0, -1)

    # only_element
    >>> minmax_default(None, [1])
    (1, 1)
    >>> minmax_default(..., [None])
    (None, None)

    # (first_min, last_max)
    >>> minmax_default(None, [4,1,2,2,5,3])
    (1, 5)
    >>> minmax_default(None, [{}, (), []], key=len)
    ({}, [])
    >>> maybe_minmax([{}, (), [], {1}, (1,), [1]], key=len)
    ({}, [1])

    # (last_min, first_max)
    >>> minmax_default(None, [{}, (), []], key=len, __lt__=operator.le)
    ([], {})
    >>> minmax_default(None, [{}, (), [], {1}, (1,), [1]], key=len, __lt__=operator.le)
    ([], {1})

    # (last_max, first_min)
    >>> minmax_default(None, [{}, (), []], key=len, __lt__=operator.ge)
    ([], {})
    >>> minmax_default(None, [{}, (), [], {1}, (1,), [1]], key=len, __lt__=operator.ge)
    ([1], {})

    # (first_max, last_min)
    >>> minmax_default(None, [{}, (), []], key=len, __lt__=operator.gt)
    ({}, [])
    >>> minmax_default(None, [{}, (), [], {1}, (1,), [1]], key=len, __lt__=operator.gt)
    ({1}, [])
'''
    return minmax_fdefault(lambda:default, iterable, key=key, __lt__=__lt__)
def minmax_fdefault(fdefault, iterable, *, key=None, __lt__=None):
    'see minmax_default; where default=fdefault()'
    tpl_012 = maybe_minmax(iterable, key=key, __lt__=__lt__)
    L = len(tpl_012)
    assert 0 <= L < 3
    if L == 2:
        return tpl_012
    elif L == 1:
        return tpl_012 + tpl_012
    elif L == 0:
        return fdefault()
    raise logic-error

def maybe_minmax(iterable, *, key=None, __lt__=None):
    '''return () | (only_element,) | (first_min, last_max) if __lt__ | (last_min, first_max) if __le__

assume x(or key(x)) has __lt__
if not(x < x), then (first_min, last_max)
if x < x, then (last_min, first_max) # i.e. (<=) instead of (<)
why not (first_min, first_max)?
    if (first_min, first_max) then:
        input [x0,x1] where x0==x1, then result will be [x0,x0]


example:
    >>> maybe_minmax([])
    ()
    >>> maybe_minmax([None])
    (None,)
    >>> maybe_minmax([2,1,3,4])
    (1, 4)

    # (first_min, last_max)
    >>> maybe_minmax([{}, (), []], key=len)
    ({}, [])
    >>> maybe_minmax([{}, (), [], {1}, (1,), [1]], key=len)
    ({}, [1])

    # (last_min, first_max)
    >>> maybe_minmax([{}, (), []], key=len, __lt__=operator.le)
    ([], {})
    >>> maybe_minmax([{}, (), [], {1}, (1,), [1]], key=len, __lt__=operator.le)
    ([], {1})

    # (last_max, first_min)
    >>> maybe_minmax([{}, (), []], key=len, __lt__=operator.ge)
    ([], {})
    >>> maybe_minmax([{}, (), [], {1}, (1,), [1]], key=len, __lt__=operator.ge)
    ([1], {})

    # (first_max, last_min)
    >>> maybe_minmax([{}, (), []], key=len, __lt__=operator.gt)
    ({}, [])
    >>> maybe_minmax([{}, (), [], {1}, (1,), [1]], key=len, __lt__=operator.gt)
    ({1}, [])

'''
    if key is None: key = echo
    if __lt__ is None: __lt__ = operator.lt

    def val2pair(x):
        return (key(x), x)
    def pair2val(pair):
        return pair[1]
    def lt(pairL, pairR):
        return __lt__(pairL[0], pairR[0])
    pairs = map(val2pair, iterable); del iterable
    for fst in pairs:break
    else: return ()
    for snd in pairs:break
    else: return (pair2val(fst),)

    if lt(snd, fst):
        # min < max
        min, max = snd, fst
    else:
        # not (max < min)
        # min <= max # position invoke
        min, max = fst, snd
    while True:
        for fst in pairs:break
        else: break
        for snd in pairs:break
        else:
            if lt(fst, min):
                # new_min < old_min
                min = fst
            elif not lt(fst, max):
                # not (new_max < old_max)
                # old_max <= new_max
                max = fst
            break
        if lt(snd, fst):
            # snd < fst
            mid_min, mid_max = snd, fst
        else:
            # not (snd < fst)
            # fst <= snd
            mid_min, mid_max = fst, snd
        if lt(mid_min, min):
            # new_min < old_min
            min = mid_min
        if not lt(mid_max, max):
            # not (new_max < old_max)
            # old_max <= new_max
            max = mid_max

    return pair2val(min), pair2val(max)

def _t():
    assert maybe_minmax([]) == ()
    assert maybe_minmax([None]) == (None,)
    assert maybe_minmax([0,1]) == (0,1)
    assert maybe_minmax([1,0]) == (0,1)
    assert maybe_minmax([0,1,2]) == (0,2)
    assert maybe_minmax([0,2,1]) == (0,2)
    assert maybe_minmax([2,0,1]) == (0,2)
    assert maybe_minmax([1,0,2]) == (0,2)
    assert maybe_minmax([1,2,0]) == (0,2)
    assert maybe_minmax([2,1,0]) == (0,2)
    assert maybe_minmax([0,1,2,3]) == (0,3)
    assert maybe_minmax([0,1,3,2]) == (0,3)
    assert maybe_minmax([0,3,2,1]) == (0,3)
    assert maybe_minmax([3,1,2,0]) == (0,3)
    assert maybe_minmax([(0,3), (1,3), (2,3), (3,3)], key=lambda p:p[1]) == ((0,3),(3,3))

class UsingLeInsteadOfLt:
    # using (<=) instead of (<)
    def __init__(self, obj):
        self.obj = obj
    def __lt__(self, other):
        return self.obj <= other.obj
T = UsingLeInsteadOfLt
assert tuple(map(lambda t: (t[0], t[1].obj)
                , maybe_minmax([(0,T(3)), (1,T(3)), (2,T(3)), (3,T(3))]
                        , key=lambda p:p[1])
                )
            ) \
        == ((3,3),(0,3))
del T

if __name__ == "__main__":
    _t()
    import doctest
    doctest.testmod()


