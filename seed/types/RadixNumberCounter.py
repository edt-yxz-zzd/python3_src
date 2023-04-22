#__all__:goto
r'''[[[
e ../../python3_src/seed/types/RadixNumberCounter.py

seed.types.RadixNumberCounter
py -m nn_ns.app.debug_cmd   seed.types.RadixNumberCounter
py -m nn_ns.app.adhoc_argparser__main__call8module   seed.types.RadixNumberCounter   @f
py -m nn_ns.app.doctest_cmd seed.types.RadixNumberCounter:__doc__ -v
from seed.types.RadixNumberCounter import RadixNumberCounter
from seed.types.RadixNumberCounter import iter_words_in_one_period_, iter_words_in_one_period_with_idx_

>>> from seed.types.RadixNumberCounter import RadixNumberCounter
>>> from seed.types.RadixNumberCounter import iter_words_in_one_period_, iter_words_in_one_period_with_idx_

>>> RadixNumberCounter(0, 1)
Traceback (most recent call last):
    ...
TypeError
>>> cntr00 = RadixNumberCounter(0, 0)
>>> cntr00
RadixNumberCounter(0, 0)
>>> cntr00.inc()
True
>>> cntr00
RadixNumberCounter(0, 0)
>>> cntr10 = RadixNumberCounter(1, 0)
>>> cntr10
RadixNumberCounter(1, 0)
>>> cntr10.inc()
True
>>> cntr10
RadixNumberCounter(1, 0)
>>> cntr11 = RadixNumberCounter(1, 1)
>>> cntr11
RadixNumberCounter(1, 1)
>>> cntr11.inc()
True
>>> cntr11
RadixNumberCounter(1, 1)
>>> cntr12 = RadixNumberCounter(1, 2)
>>> cntr12
RadixNumberCounter(1, 2)
>>> cntr12.inc()
True
>>> cntr12
RadixNumberCounter(1, 2)
>>> cntr21 = RadixNumberCounter(2, 1)
>>> cntr21
RadixNumberCounter(2, 1)
>>> cntr21.inc()
False
>>> cntr21
RadixNumberCounter(2, [1])
>>> cntr21.inc()
True
>>> cntr21
RadixNumberCounter(2, 1)
>>> cntr22 = RadixNumberCounter(2, 2)
>>> cntr22
RadixNumberCounter(2, 2)
>>> cntr22.inc()
False
>>> cntr22
RadixNumberCounter(2, [1, 0])
>>> cntr22.inc()
False
>>> cntr22
RadixNumberCounter(2, [0, 1])
>>> cntr22.inc()
False
>>> cntr22
RadixNumberCounter(2, [1, 1])
>>> cntr22.inc()
True
>>> cntr22
RadixNumberCounter(2, 2)


>>> f = lambda *args:iter_words_in_one_period_with_idx_(*args, big_endian=False)
>>> [*f(2,2)]
[(0, (0, 0)), (1, (1, 0)), (2, (0, 1)), (3, (1, 1))]
>>> [*f(2,1)]
[(0, (0,)), (1, (1,))]
>>> [*f(1,2)]
[(0, (0, 0))]
>>> [*f(1,1)]
[(0, (0,))]
>>> [*f(1,0)]
[(0, ())]
>>> [*f(0,0)]
[(0, ())]
>>> [*f(0,1)]
Traceback (most recent call last):
    ...
TypeError


#]]]'''
__all__ = r'''
    RadixNumberCounter
    iter_words_in_one_period_
        iter_words_in_one_period_with_idx_
'''.split()#'''
__all__

from seed.tiny_.check import check_uint_lt, check_int_ge
from seed.helper.repr_input import repr_helper

#class RadixWordCounter:
class RadixNumberCounter:
    'little_endian'
    def __eq__(sf, ot, /):
        if type(ot) is not type(sf):return NotImplemented
        return (sf._all0 is ot._all0) and (sf._m == ot._m) and (sf._ds == ot._ds)
    def __repr__(sf, /):
        radix = sf.get_radix()
        if not sf:
            # all0
            sz = sf.get_num_digits()
            sz_or_digits = sz
        else:
            digits = [*sf]
                #xxx big_endian
                #now little_endian
            sz_or_digits = digits
        return repr_helper(sf, radix, sz_or_digits)
    def __init__(sf, radix, sz_or_digits, /):
        'little_endian digits'
        if type(sz_or_digits) is int:
            sz = sz_or_digits
            check_int_ge(0, sz)
            digits = [0]*sz
        else:
            digits = sz_or_digits
            digits = [*digits]
            #xxx digits.reverse()
                #little_endian
            sz = len(digits)

        assert sz == len(digits)
        check_int_ge(1 if sz else 0, radix)
        for u in digits: check_uint_lt(radix, u)

        all0 = not any(digits)
        sf._all0 = all0
        sf._m = radix
        sf._ds = digits
            #little_endian
        #sf._sz = sz

    def get_radix(sf, /):
        return (sf._m)
    def get_num_digits(sf, /):
        return len(sf._ds)
    def __bool__(sf, /):
        'not 0'
        return not sf._all0
    def __iter__(sf, /):
        'little_endian'
        return iter(sf._ds)
    def __reversed__(sf, /):
        'big_endian'
        return reversed(sf._ds)
    def iter_big_endian_digits_(sf, /, *, reverse=False):
        return sf.iter_digits_(not reverse)
    def to_big_endian_digit_tuple(sf, /, *, reverse=False):
        return sf.to_digit_tuple_(not reverse)
    def iter_little_endian_digits_(sf, /, *, reverse=False):
        return sf.iter_digits_(reverse)
    def to_little_endian_digit_tuple(sf, /, *, reverse=False):
        return sf.to_digit_tuple_(reverse)

    def iter_digits_(sf, /, reverse):
        if reverse:
            return reversed(sf)
        return iter(sf)
    def to_digit_tuple_(sf, /, reverse):
        return (*sf.iter_digits_(reverse),)
    def inc(sf, /):
        '-> overflow/bool'
        if (not sf._ds or sf._m==1):
            return True
        imay = sf._inc()
        digits = sf._ds
        overflow = imay == -1
        if overflow:
            all0 = not any(digits)
            assert all0
        else:
            assert not imay < 0
            i = imay
            assert digits[i]
        sf._all0 = overflow
        return overflow
    def _inc(sf, /):
        '-> imay_idx4nonzero_digit'
        ds = sf._ds
        sz = len(ds)
        #little_endian
        _max = sf._m -1
        assert _max >= 1
        for i in range(sz):
            d = ds[i]
            if not d == _max:
                d += 1
                ds[i] = d
                return i
            ds[i] = 0
        return -1


def iter_words_in_one_period_(radix, sz, /, *, big_endian):
    'radix/uint -> sz/uint -> (big_endian/uint) -> Iter [uint%radix]{len=sz}'
    check_int_ge(0, sz)
    check_int_ge(0, radix)
    cntr = RadixNumberCounter(radix, sz)
    assert not cntr
    to_digit_tuple_ = cntr.to_big_endian_digit_tuple if big_endian else cntr.to_little_endian_digit_tuple
    yield to_digit_tuple_()
    while not cntr.inc():
        yield to_digit_tuple_()
def iter_words_in_one_period_with_idx_(radix, sz, /, *, big_endian):
    'radix/uint -> sz/uint -> (big_endian/uint) -> Iter (idx, [uint%radix]{len=sz})'
    return enumerate(iter_words_in_one_period_(radix, sz, big_endian=big_endian))

from seed.types.RadixNumberCounter import RadixNumberCounter
from seed.types.RadixNumberCounter import iter_words_in_one_period_, iter_words_in_one_period_with_idx_
