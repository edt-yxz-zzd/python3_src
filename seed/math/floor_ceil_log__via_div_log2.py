#__all__:goto
r'''[[[
e ../../python3_src/seed/math/floor_ceil_log__via_div_log2.py
mv -iv ../../python3_src/seed/math/floor_log__via_div.py ../../python3_src/seed/math/floor_ceil_log__via_div_log2.py
.+1,$s/__via_div\(_\?\)\>/__via_div_log2\1/g
.+1,$s/\<floor_log__via_div_log2\>/floor_ceil_log__via_div_log2/g

seed.math.floor_ceil_log__via_div_log2
py -m nn_ns.app.debug_cmd   seed.math.floor_ceil_log__via_div_log2 -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.floor_ceil_log__via_div_log2:__doc__ -ht # -ff -df


[[
[floor_log2(p) = p.bit_length()-1]

[log_(b; x) == log2(x)/log2(b)]
[log_(b; x) >= floor_div_(log2(b); log2(x)) >= floor_div_(ceil_log2(b); floor_log2(x))]
[log_(b; x) <= ceil_div_(log2(b); log2(x)) <= ceil_div_(floor_log2(b); ceil_log2(x))]
[floor_div_(ceil_log2(b); floor_log2(x)) <= log_(b; x) <= ceil_div_(floor_log2(b); ceil_log2(x))]

!! [ceil_log2(x) -floor_log2(x) <= 1]
!! [ceil_log2(b) -floor_log2(b) <= 1]
* [ceil_log2(b) -floor_log2(b) == 0]:
    [ceil_log2(b) == floor_log2(b) == log2(b)]
    [log_(b; x) == log2(x)/log2(b) == log2(x)/floor_log2(b)]
    [floor_log_(b; x) == floor_div_(floor_log2(b); log2(x)) == floor_div_(floor_log2(b); floor_log2(x))]
    [floor_log_(b; x) == floor_log2(x)//floor_log2(b)]

* [ceil_log2(b) -floor_log2(b) == 1]:
    [b =!= 2]
    * [b > 2][floor_log2(b)**2 >= ceil_log2(x) > 0]:
        !! [0 <= sqrt(floor_log2(x)) <= sqrt(ceil_log2(x)) <= floor_log2(b) <= ceil_log2(b)]
        !! [(ceil_log2(b) -floor_log2(b)) <= 1]
        [true_div_(floor_log2(b); ceil_log2(x)) -true_div_(ceil_log2(b); 1+floor_log2(x)) == true_div_(floor_log2(b); ceil_log2(x)) -true_div_(ceil_log2(b); ceil_log2(x)) <= (ceil_log2(b) -floor_log2(b)) <= 1]
        [true_div_(floor_log2(b); ceil_log2(x)) -true_div_(ceil_log2(b); floor_log2(x)) <= 1 +true_div_(ceil_log2(b); 1)]
        [ceil_div_(floor_log2(b); ceil_log2(x)) -floor_div_(ceil_log2(b); floor_log2(x)) <= (1-1/floor_log2(b))+true_div_(floor_log2(b); ceil_log2(x)) -(-(1-1/ceil_log2(b))+true_div_(ceil_log2(b); floor_log2(x))) <= (1-1/floor_log2(b)) +(1-1/ceil_log2(b)) +1 +true_div_(ceil_log2(b); 1) == (3-1/floor_log2(b))]
        !! [b > 2]
        [log2(b) > 1]
        [floor_log2(b) >= 1]
        [1/floor_log2(b) > 0]
        [ceil_div_(floor_log2(b); ceil_log2(x)) -floor_div_(ceil_log2(b); floor_log2(x)) <= (3-1/floor_log2(b)) < 3]

        [ceil_div_(floor_log2(b); ceil_log2(x)) < 3+floor_div_(ceil_log2(b); floor_log2(x))]
        !! [floor_div_(ceil_log2(b); floor_log2(x)) <= log_(b; x) <= ceil_div_(floor_log2(b); ceil_log2(x))]
        [0 <= log_(b; x) -floor_div_(ceil_log2(b); floor_log2(x)) < 3]
        [0 <= floor_log_(b; x) -floor_div_(ceil_log2(b); floor_log2(x)) <= 2]
        [floor_log_(b; x) == floor_log2(x)//ceil_log2(b) +(0|1|2)]

    * [b > 2][floor_log2(b)**2 < ceil_log2(x)]:
        ... ...
    * [b < 2]:
        ... ...

]]



floor_log__via_div_log2_
_validated_floor_log__via_div_log2_
>>> from itertools import product

>>> for b, with_floor_pow, x in product([2,3,17], [False, True], range(1, 300)):
...     __ = _validated_floor_ceil_log__via_div_log2_(b, x, with_floor_pow=with_floor_pow)
>>> for b, with_floor_pow, x in product([2,3,17], [False, True], range(1, 300)):
...     __ = _validated_ceil_log__via_div_log2_(b, x, with_floor_pow=with_floor_pow)




>>> for b, with_floor_pow, x in product([2,3,17], [False, True], range(1, 300)):
...     __ = _validated_floor_log__via_div_log2_(b, x, with_floor_pow=with_floor_pow)

>>> for b, x in product([3,17], range(1, 3000)):
...     __ = _validated_floor_log__via_div_log2_(b, x, with_floor_pow=False)


>>> for x in range(1, 100_0000): #doctest: +SKIP
...     __ = _validated_floor_log__via_div_log2_(3, x, with_floor_pow=False)



py_adhoc_call   seed.math.floor_ceil_log__via_div_log2   @f
]]]'''#'''
__all__ = r'''
FloorLogarithm
    floor_log__via_div_log2_
        floor_ceil_log__via_div_log2_
            ceil_log__via_div_log2_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from functools import cached_property


#from seed.math.floor_ceil import floor_div, ceil_div
#from seed.math.floor_ceil import floor_div_, ceil_div_
#from seed.math.floor_ceil import floor_log2, ceil_log2, floor_ceil_log2
#from seed.math.floor_ceil import floor_log_, ceil_log_, floor_ceil_log_
#assert (2, 2, 4) == (__:=floor_ceil_log_(2, 4, with_floor_pow=True)), __
#assert (1, 1, 2) == (__:=floor_ceil_log_(2, 2, with_floor_pow=True)), __
#assert (0, 0, 1) == (__:=floor_ceil_log_(2, 1, with_floor_pow=True)), __

from seed.math.floor_ceil import floor_log2, floor_ceil_log2

from seed.tiny_.check import check_type_is, check_int_ge
from seed.helper.repr_input import repr_helper
___end_mark_of_excluded_global_names__0___ = ...

_b2flgB = {}

class FloorLogarithm:
    def __new__(cls, base4logarithm, /):
        check_int_ge(2, base4logarithm)
        # [b >= 2]
        if cls is __class__:
            try:
                return _b2flgB[base4logarithm]
            except KeyError:
                pass

        sf = super(__class__, cls).__new__(cls)
        sf._b = b = base4logarithm
        e0b, e1b = floor_ceil_log2(base4logarithm, with_floor_pow=False)
        zpowb = e0b == e1b
        sf._ex = e0b, e1b, zpowb
        assert e1b-0==e0b>=1 if zpowb else (e1b-1==e0b>=1 and b > 2)
        if not zpowb and e0b == 1:
            assert b == 3, b
        #sf._m2 = None
        #sf._sq = None
        #return sf
        if cls is __class__:
            _b2flgB[base4logarithm] = sf
            return cls(base4logarithm)
        return sf
    @cached_property
    def _sq(sf, /):
        return FloorLogarithm(sf._b**2)
    @property
    def base4logarithm(sf, /):
        return sf._b
    def __repr__(sf, /):
        return repr_helper(sf, sf.base4logarithm)
    #def __call__(sf, x, /):
    def floor_ceil_log_(sf, x, /, *, with_floor_pow:bool):
        check_type_is(bool, with_floor_pow)
        ef, fl_pw = sf.floor_log_(x, with_floor_pow=True)
        ec = ef + (not x == fl_pw)
        if with_floor_pow:
            return (ef, ec, fl_pw)
        return (ef, ec)
    def ceil_log_(sf, x, /, *, with_floor_pow:bool):
        (ef, ec, *tmay_fl_pw) = sf.floor_ceil_log_(x, with_floor_pow=with_floor_pow)
        if with_floor_pow:
            [fl_pw] = tmay_fl_pw
            return (ec, fl_pw)
        return ec
    def floor_log_(sf, x, /, *, with_floor_pow:bool):
        check_type_is(bool, with_floor_pow)
        check_int_ge(1, x)
        e0b, e1b, zpowb = sf._ex
        b = sf._b

        # [b >= 2]
        if zpowb:
            # [ceil_log2(b) -floor_log2(b) == 0] => [floor_log_(b; x) == floor_log2(x)//floor_log2(b)]
            ef = floor_log2(x)//e0b
            if with_floor_pow:
                #fl_pw = b**ef
                fl_pw = 1 << (e0b*ef)
            #ef, ?fl_pw
        else:
            # [ceil_log2(b) -floor_log2(b) == 1]
            # [b > 2]
            e0x, e1x = floor_ceil_log2(x, with_floor_pow=False)
            #e1x = ceil_log2(x)
            if e0b**2 >= e1x:
                # [b > 2][floor_log2(b)**2 >= ceil_log2(x) > 0]
                # [floor_log_(b; x) == floor_log2(x)//ceil_log2(b) +(0|1|2)]
                ef = e0x//e1b
                fl_pw = b**ef
                for k in range(2):
                    cl_pw = b*fl_pw
                    if x < cl_pw:
                        break
                    fl_pw = cl_pw
                    ef += 1
                #ef, fl_pw
            else:
                # [b > 2][floor_log2(b)**2 < ceil_log2(x)]

                #.if e0b == 1:
                #.    assert b == 3, b
                #.    sq = _flg_9
                #.else:
                #.    assert b >= 5, b
                sq = sf._sq
                eh, fl_pw = sq.floor_log_(x, with_floor_pow=True)
                cl_pw = b*fl_pw
                ef = eh*2
                if not x < cl_pw:
                    fl_pw = cl_pw
                    ef += 1
                    cl_pw = None
                #ef, fl_pw
            #ef, fl_pw
            #ef, ?fl_pw
        #ef, ?fl_pw
        if with_floor_pow:
            return (ef, fl_pw)
        return ef
#_flg_9 = FloorLogarithm(3**2)

def floor_log__via_div_log2_(b, x, /, *, with_floor_pow:bool):
    return FloorLogarithm(b).floor_log_(x, with_floor_pow=with_floor_pow)

def floor_ceil_log__via_div_log2_(b, x, /, *, with_floor_pow:bool):
    return FloorLogarithm(b).floor_ceil_log_(x, with_floor_pow=with_floor_pow)

def ceil_log__via_div_log2_(b, x, /, *, with_floor_pow:bool):
    return FloorLogarithm(b).ceil_log_(x, with_floor_pow=with_floor_pow)


def _validated_floor_log__via_div_log2_(b, x, /, *, with_floor_pow:bool):
    r = floor_log__via_div_log2_(b, x, with_floor_pow=with_floor_pow)
    if with_floor_pow:
        (ef, fl_pw) = r
        assert fl_pw == b**ef, (b, x, with_floor_pow, r)
    else:
        ef = r
    ef
    assert b**ef <= x < b**(ef+1), (b, x, with_floor_pow, r)
    return r


def _validated_floor_ceil_log__via_div_log2_(b, x, /, *, with_floor_pow:bool):
    r = floor_ceil_log__via_div_log2_(b, x, with_floor_pow=with_floor_pow)
    if with_floor_pow:
        (ef, ec, fl_pw) = r
        assert fl_pw == b**ef, (b, x, with_floor_pow, r)
    else:
        ef, ec = r
    ef, ec
    assert ef <= ec <= ef+1, (b, x, with_floor_pow, r)
    assert b**ef <= x < b**(ef+1), (b, x, with_floor_pow, r)
    assert b**(ec-1) < x <= b**ec, (b, x, with_floor_pow, r)
    return r

def _validated_ceil_log__via_div_log2_(b, x, /, *, with_floor_pow:bool):
    r = ceil_log__via_div_log2_(b, x, with_floor_pow=with_floor_pow)
    if with_floor_pow:
        (ec, fl_pw) = r
        assert fl_pw == b**(ec-(b**ec > x)), (b, x, with_floor_pow, r)
    else:
        ec = r
    ec
    assert b**(ec-1) < x <= b**ec, (b, x, with_floor_pow, r)
    return r

__all__
from seed.math.floor_ceil_log__via_div_log2 import FloorLogarithm, floor_log__via_div_log2_, floor_ceil_log__via_div_log2_
from seed.math.floor_ceil_log__via_div_log2 import *
