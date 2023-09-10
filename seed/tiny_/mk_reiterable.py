__all__ = '''
    mk_reiterable
    mk_reiterables
    mk_reiterable__depth_
    '''.split()

from operator import index as to_index
from seed.tiny_.verify import is_reiterable# is_iterable, is_iterator
from seed.tiny_.containers import null_str, null_bytes, null_int, null_tuple, null_frozenset, null_mapping_view, null_iter# mk_frozenset, mk_tuple


def mk_reiterable(xs, /):
    return mk_reiterable__depth_(0, xs)
def mk_reiterables(xss, /):
    return mk_reiterable__depth_(1, xss)
def mk_reiterable__depth_(depth, xs, /):
    'depth/uint -> xs* -> xs*'
    same, _xs = _mk_reiterable_ex__depth_(depth, xs)
    return _xs
def _mk_reiterable_ex__depth_(depth, xs, /):
    'depth/uint -> xs* -> (same/bool, xs*)'
    depth = to_index(depth)
    if depth < 0: raise TypeError
    elif depth > 0:
        ps = [_mk_reiterable_ex__depth_(depth-1, x) for x in xs]
        if all(same for same, _ in ps):
            _xs = xs
        else:
            _xs = tuple(_x for _, _x in ps)
    elif depth == 0:
        if is_reiterable(xs):
            _xs = xs
        else:
            _xs = tuple(xs)
    else:
        raise 000
    assert is_reiterable(_xs)
    same = _xs is xs
    return same, _xs

assert mk_reiterable([0, {}, null_iter]) == [0, {}, null_iter]
assert mk_reiterables([{}, null_iter, []]) == ({}, (), [])
assert mk_reiterables(iter([{}, null_iter, []])) == ({}, (), [])

from seed.tiny_.mk_reiterable import mk_reiterable, mk_reiterables, mk_reiterable__depth_
from seed.tiny_.mk_reiterable import *
