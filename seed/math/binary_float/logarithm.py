#__all__:goto
r'''[[[
e ../../python3_src/seed/math/binary_float/logarithm.py
    view ../../python3_src/seed/math/binary_float/binary_float_ops____using_LazyList.py
    view ../../python3_src/seed/math/continued_fraction/continued_fraction_ops____using_LazyList.py

[xf :: (cf|bf)]


seed.math.binary_float.logarithm
py -m nn_ns.app.debug_cmd   seed.math.binary_float.logarithm -x
py -m nn_ns.app.doctest_cmd seed.math.binary_float.logarithm:__doc__ -ff -v
py_adhoc_call   seed.math.binary_float.logarithm   @f
from seed.math.binary_float.logarithm import *
#]]]'''
__all__ = r'''
    log2_xf__gt0_
    log2_xf__ge1_
    log2_xf__gt1_lt2_
'''.split()#'''
    #bf5flatten_
__all__

from functools import wraps
from math import floor
from seed.math.floor_ceil import floor_log2

from seed.types.LazyList import LazyList, LazyListError
from seed.math.binary_float.binary_float_ops____using_LazyList import BinaryFloat, bf_0, positive_bf_digits5flatten_
    #mk_binary_float_digits5int_ as bf5int_
    #bf5int_ = BinaryFloat

def bf5flatten_(f, /):
    @wraps(f)
    def mk_bf_(*args, **kwds):
        it = f(*args, **kwds)
        lz = LazyList(it)
        bf_digits = positive_bf_digits5flatten_(lz)
        bf = BinaryFloat(bf_digits)
        return bf
    return mk_bf_

def log2_xf__gt0_(xf, /):
    'xf{xf>0} -> bf'
    assert xf > 0
    to_neg = xf < 1
    if to_neg:
        xf = 1/xf
        # [log2(xf) == -log2(1/xf)]
    r = log2_xf__ge1_(xf)
    if to_neg:
        r = -r
    return r
def log2_xf__ge1_(xf, /):
    'xf{xf>1} -> bf'
    assert xf >= 1
    to_rshift = xf >= 2
    if to_rshift:
        i = floor(xf)
        k = floor_log2(i)
        xf >>= k
        # [log2(xf) == k+log2(xf/2**k)]
    # [1 <= xf < 2]
    if xf == 1:
        # [1 == xf]
        r = bf_0
    else:
        # [1 < xf < 2]
        r = log2_xf__gt1_lt2_(xf)
    if to_rshift:
        #k = bf5int_(k)
        #r = bf_add(k, r)
        r += k
    return r

@bf5flatten_
def log2_xf__gt1_lt2_(xf, /):
    'xf{1<xf<2} -> bf'
    # using flatten require positive ==>> [xf > 1]
    assert 1 < xf < 2
    yield -1 # exp4msb 01
    while 1:
        # [1 < xf < 2]
        xf *= xf
        # [1 < xf < 4]
        if xf < 2:
            # [1 < xf < 2]
            yield 0
        else:
            # [2 <= xf < 4]
            yield 1
            xf >>= 1
            # [1 <= xf < 2]
            if xf == 1:break
            # [1 < xf < 2]
        # [1 < xf < 2]

def __():
    from itertools import islice
    r = log2_xf__gt0_(BinaryFloat(7))
    if 1:
        print(tuple(islice(r, 3)))
        sign0, exp4msb = r[0]
        r = iter(r)
        for i, bit in enumerate(r, -exp4msb):
            print(f'{i}:{bit}')
    else:
        it = iter(r.to_ContinuedFraction_())
        r = None
        for i, d in enumerate(it):
            print(f'{i}:{d}')
#__()
__all__


from seed.math.binary_float.logarithm import *

