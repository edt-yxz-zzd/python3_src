
__all__ = '''
    is_sorted
    is_strict_sorted

    is_sorted__via_le
    is_sorted__via_lt
    '''.split()

import operator
from seed.iters.map_if import map_if
from seed.iters.zip_me import zip_me2
from itertools import starmap

def is_strict_sorted(iterable, *, key=None):
    #bug: return is_sorted__via_lt(iterable, key=key)
    it = map_if(key, iterable); del iterable
    __lt__ = operator.lt
    return all(starmap(__lt__, zip_me2(it)))

def is_sorted(iterable, *, key=None, before=None):
    return is_sorted__via_le(iterable, key=key, __le__=before)

def is_sorted__via_le(iterable, *, key = None, __le__ = None):
    it = map_if(key, iterable); del iterable
    if __le__ is None:
        __le__ = operator.le

    return all(starmap(__le__, zip_me2(it)))


def is_sorted__via_lt(iterable, *, key = None, __lt__ = None):
    it = map_if(key, iterable); del iterable
    if __lt__ is None:
        __lt__ = operator.lt

    return all(not __lt__(b,a) for a, b in zip_me2(it))


def _test(is_sorted):
    assert is_sorted([])
    assert is_sorted([0])
    assert is_sorted([0,0])
    assert is_sorted([0,0,1])
    assert not is_sorted([1,0])

    assert is_sorted([])
    assert is_sorted([None])
    assert is_sorted([1, 1])
    assert is_sorted([1, 1, 1])
    assert is_sorted([1, 2])
    assert is_sorted([1, 2, 3])
    assert is_sorted([1, 1, 2])
    assert is_sorted([1, 2, 2])
    assert not is_sorted([1, 2, 1])
    assert not is_sorted([1, 3, 2])
    assert not is_sorted([2, 1])



def _test_is_sorted(is_sorted, N=5):
    from itertools import permutations
    try:
        for n in range(N):
            it = iter(permutations(range(n)))
            std = tuple(range(n))
            assert is_sorted(std)
            for p in it:
                if p != std:
                    assert not is_sorted(p)
    except:
        print(p)
        raise

    #assert len(list(permutations([1,1,1]))) == 6
    return True

def _t():
    for is_sorted_x in [is_sorted__via_le, is_sorted__via_lt, is_sorted]:
        _test(is_sorted_x)
        _test_is_sorted(is_sorted_x)



if __name__ == '__main__':
    _t()


