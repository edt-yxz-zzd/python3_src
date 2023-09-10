#__all__:goto
raise 000
see:
    view ../../python3_src/seed/math/continued_fraction/continued_fraction_of_log_.py
        floor_log_ex_
            * Fraction
            * ContinuedFraction
                from seed.math.continued_fraction.continued_fraction_ops import ContinuedFraction
r'''[[[
e ../../python3_src/seed/math/floor_log__ops_.py
    #view ../../python3_src/seed/math/floor_log__Fraction_.py
        view ../../python3_src/seed/math/continued_fraction/continued_fraction_of_log_.py
    ###generic:
    floor_log__Fraction_ :: Fraction -> Fraction -> int
    floor_log__ops_ :: ops<real> -> real -> real -> int
        to impl:
            floor_log__cf_ :: cf_digits -> cf_digits -> int
                #continued_fraction_digits



seed.math.floor_log__ops_
py -m nn_ns.app.debug_cmd   seed.math.floor_log__ops_ -x
py -m nn_ns.app.doctest_cmd seed.math.floor_log__ops_:__doc__ -ff -v
py_adhoc_call   seed.math.floor_log__ops_   @f
from seed.math.floor_log__ops_ import *




#]]]'''
__all__ = r'''
'''.split()#'''
__all__
from seed.tiny import check_type_is

def __():
    from seed.tiny import ifNonef, ifNone, echo
    from seed.tiny import check_type_is, fst, snd, at
    from seed.tiny_.check import check_uint_lt, check_int_ge_lt, check_int_ge, check_int_ge_le
    from seed.tiny import print_err, mk_fprint, mk_assert_eq_f, expectError
    from seed.func_tools.fmapT.fmapT__tiny import dot, fmapT__dict, fmapT__list, fmapT__iter
    from seed.helper.repr_input import repr_helper

def __():
    from seed.abc.abc__ver1 import abstractmethod, override, abc, abc__no_slots
    from seed.helper.repr_input import repr_helper
    class _(abc):
        __slots__ = ()
        raise NotImplementedError
        ___no_slots_ok___ = True
        def __repr__(sf, /):
            #return repr_helper(sf, *args, **kwargs)
            #return repr_helper_ex(sf, args, ordered_attrs, kwargs, ordered_attrs_only=False)
            ...
if __name__ == "__main__":
    pass
__all__

from seed.abc.abc__ver1 import abstractmethod, override, abc, abc__no_slots
from seed.math.power_of import calc_power
#view ../../python3_src/seed/math/power_of.py
#def calc_power(I, T_2pow_ls, power:int, *, mul):


class IOps4floor_log(abc):
    __slots__ = ()
    @abstractmethod
    def lt(ops, lhs, rhs, /):
        'ops<real> -> real -> real -> bool'
    @abstractmethod
    def eq(ops, lhs, rhs, /):
        'ops<real> -> real -> real -> bool'


    @abstractmethod
    def add(ops, lhs, rhs, /):
        'ops<real> -> real -> real -> real'
    @abstractmethod
    def mul(ops, lhs, rhs, /):
        'ops<real> -> real -> real -> real'
    @abstractmethod
    def neg(ops, rhs, /):
        'ops<real> -> real -> real'
    @abstractmethod
    def inv(ops, rhs, /):
        'ops<real> -> real -> real'
    @abstractmethod
    def floor(ops, rhs, /):
        'ops<real> -> real -> int'
    @abstractmethod
    def real5int_ratio(ops, N, D, /):
        'ops<real> -> int -> int -> real'
    def real5int(ops, i, /):
        'ops<real> -> int -> real'
        return ops.real5int_ratio(i, 1)
    def get_zero(ops, /):
        'ops<real> -> real'
        return ops.real5int(0)
    def get_one(ops, /):
        'ops<real> -> real'
        return ops.real5int(1)

    def sub(ops, lhs, rhs, /):
        'ops<real> -> real -> real -> real'
        return ops.add(lhs, ops.neg(rhs))
    def truediv(ops, lhs, rhs, /):
        'ops<real> -> real -> real -> real'
        return ops.mul(lhs, ops.inv(rhs))
    def floordiv(ops, lhs, rhs, /):
        'ops<real> -> real -> real -> real'
        return ops.floor(ops.truediv(lhs, rhs))
    def divmod(ops, lhs, rhs, /):
        'ops<real> -> real -> real -> (int, real)'
        iq = ops.floordiv(lhs, rhs)
        q = ops.real5int(iq)
        r = ops.sub(lhs, ops.mul(rhs, q))
        return (iq, r)
    def mod(ops, lhs, rhs, /):
        'ops<real> -> real -> real -> real'
        (iq, r) = ops.divmod(lhs, rhs)
        return r
    def pow__int_(ops, lhs, idx, /, *, double_pows):
        'ops<real> -> real -> int -> real'
        check_type_is(int, idx)
        if idx <= 0:
            if idx == 0:
                if ops.eq_zero(lhs):
                    raise NaNError
                return ops.get_one()
            lhs = ops.inv(lhs)
            idx = -idx
        assert idx > 0
        double_pows = _init__double_pows(double_pows, lhs)
        r = calc_power(None, double_pows, idx, mul=ops.mul)
        return r

    def ne(ops, lhs, rhs, /):
        'ops<real> -> real -> real -> bool'
        return not ops.eq(lhs, rhs)
    def le(ops, lhs, rhs, /):
        'ops<real> -> real -> real -> bool'
        return not ops.gt(lhs, rhs)
    def ge(ops, lhs, rhs, /):
        'ops<real> -> real -> real -> bool'
        return not ops.lt(lhs, rhs)
    def gt(ops, lhs, rhs, /):
        'ops<real> -> real -> real -> bool'
        return  ops.lt(rhs, lhs)

    def gt_zero(ops, lhs, /):
        'ops<real> -> real -> bool'
        return ops.gt(lhs, ops.get_zero())
    def eq_zero(ops, lhs, /):
        'ops<real> -> real -> bool'
        return ops.eq(lhs, ops.get_zero())
    def eq_one(ops, lhs, /):
        'ops<real> -> real -> bool'
        return ops.eq(lhs, ops.get_one())
    def lt_one(ops, lhs, /):
        'ops<real> -> real -> bool'
        return ops.lt(lhs, ops.get_one())

def _init__double_pows(double_pows, lhs, /):
    if double_pows is None:
        double_pows = []
    if not double_pows:
        double_pows.append(lhs)
    if not double_pows[0] is lhs: raise logic-err
    return double_pows

def _prepare(ops, base, y, /):
    '-> ... if y==1 else (base, y)'
    if not ops.gt_zero(y): raise ValueError
    if not ops.gt_zero(base): raise ValueError
    # [base > 0][y > 0]
    if ops.eq_one(base): raise ValueError
    # [base > 0][base=!=1][y > 0]
    if ops.eq_one(y):
        # [base > 0][base=!=1][y == 1]
        return ...
    # [base > 0][base=!=1][y > 0][y =!= 1]
    if ops.lt_one(base):
        base = ops.inv(base)
        y = ops.inv(y)
    # [base > 1][y > 0][y =!= 1]
    return (base, y)
def floor_log__ops_(ops, base, y, /, *, _guess_first=False, double_pows=None, with_y_remain=False):
    'ops-version-floor_log_'
    r = _prepare(ops, base, y)
    if r is ...:
        # [base > 0][base=!=1][y == 1]
        return ops.real5int(0)
    (base, y) = r; del r
    # [base > 1][y > 0][y =!= 1]
    return _floor_log_(ops, base, y, _guess_first=_guess_first, double_pows=double_pows, with_y_remain=with_y_remain)

_near1 = 1+Fraction(1, 1<<4)
_near1_ND = _near1_ND.as_integer_ratio()
def _floor_log_(ops, base, y, /, *, _guess_first, double_pows, with_y_remain):
    'ops-version-floor_log_'
    # [base > 1][y > 0][y =!= 1]
    #   if not first round: [1 < base < y]
    double_pows = _init__double_pows(double_pows, lhs)
    if _guess_first:
        e = _floor_log__impl__guess_first_(ops, base, y, double_pows=double_pows, with_y_remain=with_y_remain)
    else:
        e = _floor_log__impl_(ops, base, y, double_pows=double_pows, with_y_remain=with_y_remain)
    #assert 1 <= y/base**e < base
        # [base**e <= y < base**(e+1)]
    return e
def _floor_log__impl__guess_first_(ops, base, y, /, *, , double_pows, with_y_remain):
    'ops-version-floor_log_ #guess a initial result at first'
    # [base > 1][y > 0][y =!= 1]
    #   if not first round: [1 < base < y]
    y0 = y
    _near1 = ops.real5int_ratio(*_near1_ND)
    trans = ops.lt(base, _near1)
    if trans:
        if ops.lt(y, base):
            return ops.get_zero() #0
        _1 = ops.get_one()
        # [base == 1+p]
        p = ops.sub(base, 1)
        # [y == base**x == (1+p)**x >= 1+x*p]
        # [x <= (y-1)/p]
        x_ = ops.floordiv(ops.sub(y0, _1), p)
            # [x_ :: int]
        if 0b00:
            print(f'_floor_log__impl__guess_first_:x_ = {x_}')
            if x_ > 100:
                # floor_log_result_is_big:here
                print(f'_floor_log__impl__guess_first_:x_ is big:{x_}')

        # [floor_log_(base; y) <= x_]
        # [[base**x_ < y0] -> [floor_log_(base; y) == x_]]
        y = ops.truediv(ops.pow__int_(base, x_, double_pows=double_pows), y0)
        if ops.lt_one(y):
            e = x_
                # [e :: int]
            y_remain = y
            return e, y_remain
        #assert y >= 1, (base, y0, x_)
        #if not y >= 1: raise logic-err
    e, y_remain = _floor_log__impl_(ops, base, y, double_pows=double_pows, with_y_remain=with_y_remain)
        # [e :: int]
    if trans:
        exact = ops.eq_one(y)
        # [e == floor_log_(base, base**x_/y0)]
        # [e == x_+floor_log_(base, 1/y0)]
        # [e == x_-ceil_log_(base, y0)]
        # [e == x_-floor_log_(base, y0) -[not exact]]
        # [e == x_-x -[not exact]]
        # [x == x_-e -[not exact]]
        x = x_-e -(not exact)
            # [x :: int]
        e = x
            # [e :: int]
    y = y0
    return e, y_remain

def _floor_log__impl_(ops, base, y, /, *, double_pows, with_y_remain):
    'ops-version-floor_log_'
    # [base > 1][y > 0][y =!= 1]
    #   if not first round: [1 < base < y]
    assert double_pows
    assert double_pows[0] is base

    base_is_int = ops.is_int(base)


    y0 = y
    #double_pows = [base, ...]
        # [double_pows[i] == base**2**i]

    i = 0
    for i, base_pow in enumerate(double_pows):
        if ops.le(y, base_pow):
            break
    else:
        i += 1

    if i == len(double_pows):
        #double_pows = [base, ...]
        while not ops.le(y, double_pows[-1]):
            last = double_pows[-1]
            double_pows.append(ops.mul(last, last))
        i = len(double_pows) - 1

    e = 0
    i += 1
    while not i == 0:
        i -= 1

        w = double_pows[i]
            # [w == base**2**i]
        if ops.ge(y, w):
            e += 1 << i
            if base_is_int:
                iy = ops.floordiv(y, w)
                y = ops.real5int(iy)
            else:
                y = ops.truediv(y, w)
                    # not floordiv unless [base :: int]
            #assert y < w
            # [y < w]
        # [y < w]
    #[y < base]

    y = y0
    #assert 1 <= y/base**e < base
        # [base**e <= y < base**(e+1)]
    return e

__all__

from seed.math.floor_log__ops_ import *
