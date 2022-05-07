#r"""[[[

r'''
py -m seed.int_tools.digits.radix_repr2uint
from seed.int_tools.digits.radix_repr2uint import radix_repr2uint, IRadixRepr2Uint, RadixRepr2Uint

!mkdir ../../python3_src/seed/int_tools/digits
e ../../python3_src/seed/int_tools/digits/radix_repr2uint.py

###outdated:
e ../../python3_src/seed/int_tools/radix_repr2uint.py
py -m seed.int_tools.radix_repr2uint
from seed.int_tools.radix_repr2uint import radix_repr2uint, uint2radix_repr
#'''
__all__ = '''
    radix_repr2uint

    IRadixRepr2Uint
        RadixRepr2Uint
            radix_repr2uint
                radix_repr2uint__little_endian
                radix_repr2uint__big_endian

    '''.split()
from seed.abc.abc import ABC, abstractmethod, override, ABC__no_slots
from seed.helper.check.checkers import check_int, check_type_is
from seed.int_tools.digits._common import _Int


class IRadixRepr2Uint(ABC):
    r'''
    eval poly
    #'''
    __slots__ = ()

    @abstractmethod
    def get_radix(sf, /):
        ...
    @abstractmethod
    def get_zero(sf, /):
        ...
    @abstractmethod
    def get_one(sf, /):
        ...
    @abstractmethod
    def add(sf, lhs, rhs, /):
        ...
    @abstractmethod
    def mul(sf, lhs, rhs, /):
        ...
    def radix_repr2uint(sf, digits, /,*, is_big_endian:bool, _merge_ver:'0|1|2'):
        f = sf.radix_repr2uint__big_endian if is_big_endian else sf.radix_repr2uint__little_endian
        return f(digits, _merge_ver=_merge_ver)
    def radix_repr2uint__big_endian(sf, digits, /,*, _merge_ver:'0|1|2'):
        if _merge_ver==0:
            return sf.radix_repr2uint__big_endian__plain(digits)
        else:
            return sf.radix_repr2uint__big_endian__merge(digits, _merge_ver=_merge_ver)
    def radix_repr2uint__little_endian(sf, digits, /,*, _merge_ver:'0|1|2'):
        if _merge_ver==0:
            return sf.radix_repr2uint__little_endian__plain(digits)
        else:
            return sf.radix_repr2uint__little_endian__merge(digits, _merge_ver=_merge_ver)

    def radix_repr2uint__little_endian__merge(sf, digits, /,*, _merge_ver:'1|2'):
        iter_digits = iter(digits); del digits
        zero = sf.get_zero()
        for digit_LSB in iter_digits:
            break
        else:
            return zero

        one = sf.get_one()
        base = sf.get_radix()
        mul = sf.mul
        add = sf.add
        level2may_digit = [[digit_LSB]]
        level2radix = [base]

        for digit in iter_digits:
            for level, may_digit in enumerate(level2may_digit):
                if may_digit:
                    [low_digit] = may_digit
                    may_digit.clear()
                    high_digit = digit
                    next_level_digit =  add(low_digit, mul(high_digit, level2radix[level]))
                    #next round
                    digit = next_level_digit
                    continue
                else:
                    low_digit = digit
                    may_digit.append(low_digit)
                    #stop without new level
                    break
            else:
                #new level
                low_digit = digit
                level2may_digit.append([low_digit])
                last_level_radix = level2radix[-1]
                new_level_radix = mul(last_level_radix, last_level_radix)
                level2radix.append(new_level_radix)
        else:
            if _merge_ver==1:
                u = zero
                for level_radix, may_level_digit in zip(level2radix, level2may_digit):
                    if may_level_digit:
                        [level_digit] = may_level_digit
                        u =  add(level_digit, mul(u, level_radix))
            elif _merge_ver==2:
                weight = one
                u = zero
                for level_radix, may_level_digit in zip(reversed(level2radix), reversed(level2may_digit)):
                    if may_level_digit:
                        [level_digit] = may_level_digit
                        u =  add(u, mul(level_digit, weight))
                        weight = mul(weight, level_radix)
            else:
                raise Exception(f'unknown _merge_ver={_merge_ver}')
            u
        return u
    def radix_repr2uint__big_endian__merge(sf, digits, /,*, _merge_ver:'1|2'):
        iter_digits = iter(digits); del digits
        zero = sf.get_zero()
        for digit_MSB in iter_digits:
            break
        else:
            return zero

        one = sf.get_one()
        base = sf.get_radix()
        mul = sf.mul
        add = sf.add
        level2may_digit = [[digit_MSB]]
        level2radix = [base]

        for digit in iter_digits:
            for level, may_digit in enumerate(level2may_digit):
                if may_digit:
                    [high_digit] = may_digit
                    may_digit.clear()
                    low_digit = digit
                    next_level_digit =  add(low_digit, mul(high_digit, level2radix[level]))
                    #next round
                    digit = next_level_digit
                    continue
                else:
                    low_digit = digit
                    may_digit.append(low_digit)
                    #stop without new level
                    break
            else:
                #new level
                low_digit = digit
                level2may_digit.append([low_digit])
                last_level_radix = level2radix[-1]
                new_level_radix = mul(last_level_radix, last_level_radix)
                level2radix.append(new_level_radix)
        else:
            if _merge_ver==1:
                u = zero
                for level_radix, may_level_digit in zip(reversed(level2radix), reversed(level2may_digit)):
                    if may_level_digit:
                        [level_digit] = may_level_digit
                        u =  add(level_digit, mul(u, level_radix))
            elif _merge_ver==2:
                weight = one
                u = zero
                for level_radix, may_level_digit in zip(level2radix, level2may_digit):
                    if may_level_digit:
                        [level_digit] = may_level_digit
                        u =  add(u, mul(level_digit, weight))
                        weight = mul(weight, level_radix)
            else:
                raise Exception(f'unknown _merge_ver={_merge_ver}')
            u
        return u






    def radix_repr2uint__little_endian__plain(sf, digits, /):
        u = sf.get_zero()
        weight = sf.get_one()
        base = sf.get_radix()
        mul = sf.mul
        add = sf.add

        for d in digits:
            u = add(mul(d, weight), u)
            weight = mul(weight, base)
        return u
    def radix_repr2uint__big_endian__plain(sf, digits, /):
        u = sf.get_zero()
        base = sf.get_radix()
        mul = sf.mul
        add = sf.add

        for d in digits:
            u = add(mul(u, base), d)
        return u
class RadixRepr2Uint(IRadixRepr2Uint, ABC__no_slots):
    def __init__(sf, radix, /):
        check_int(radix, min=2)
        sf.__radix = radix

    @override
    def get_radix(sf, /):
        return sf.__radix
    @override
    def get_zero(sf, /):
        return 0
    @override
    def get_one(sf, /):
        return 1
    @override
    def add(sf, lhs, rhs, /):
        return lhs+rhs
    @override
    def mul(sf, lhs, rhs, /):
        return lhs*rhs

class _RadixRepr2Uint(IRadixRepr2Uint, ABC__no_slots):
    def __init__(sf, radix, /):
        check_type_is(_Int, radix)
        check_int(radix.i, min=2)
        sf.__radix = radix

    @override
    def get_radix(sf, /):
        return sf.__radix
    @override
    def get_zero(sf, /):
        return _Int(0)
    @override
    def get_one(sf, /):
        return _Int(1)
    @override
    def add(sf, lhs, rhs, /):
        return _Int(lhs.i+rhs.i)
    @override
    def mul(sf, lhs, rhs, /):
        return _Int(lhs.i*rhs.i)
def radix_repr2uint__little_endian(radix, digits, /,*, _merge_ver:'0|1|2'=0):
    return RadixRepr2Uint(radix).radix_repr2uint__little_endian(digits, _merge_ver=_merge_ver)
def radix_repr2uint__big_endian(radix, digits, /,*, _merge_ver:'0|1|2'=0):
    return RadixRepr2Uint(radix).radix_repr2uint__big_endian(digits, _merge_ver=_merge_ver)
def radix_repr2uint(radix_or_an_IRadixRepr2Uint, digits, /,*, is_big_endian:bool, _merge_ver:'0|1|2'=0, input_is_an_IRadixRepr2Uint_not_radix=False):
    if input_is_an_IRadixRepr2Uint_not_radix:
        an_IRadixRepr2Uint = radix_or_an_IRadixRepr2Uint
    else:
        radix = radix_or_an_IRadixRepr2Uint
        an_IRadixRepr2Uint = RadixRepr2Uint(radix)
    return an_IRadixRepr2Uint.radix_repr2uint(digits, is_big_endian=is_big_endian, _merge_ver=_merge_ver)




def _t0():
    for _merge_ver in range(3):
        assert 1573 == radix_repr2uint__little_endian(10, reversed([1,5,7,3]), _merge_ver=_merge_ver)
        assert 1573 == radix_repr2uint__big_endian(10, [1,5,7,3], _merge_ver=_merge_ver)
        assert 1573 == radix_repr2uint(10, reversed([1,5,7,3]), is_big_endian=False, _merge_ver=_merge_ver)
        assert 1573 == radix_repr2uint(10, [1,5,7,3], is_big_endian=True, _merge_ver=_merge_ver)
_t0()
    #################################
    #################################
def _t1():
    radix = _Int(7)
    sf = _RadixRepr2Uint(radix)
    for i in range(30):
        digits = range(1, i+1)
        for is_big_endian in (True, False):
            rs = [
                radix_repr2uint(sf, map(_Int, digits), is_big_endian=is_big_endian, _merge_ver=_merge_ver, input_is_an_IRadixRepr2Uint_not_radix=True)
                for _merge_ver in range(3)
                ]
            assert len(set(rs)) == 1



def _t_xxx():
    radixes = [8,16,32,64,10,12,24,36]
    digits = [1,5,7,3]
    for radix in radixes:
        u = radix_repr2uint__big_endian(radix, digits)
        print(f'{u} = radix_repr2uint__big_endian({radix}, {digits})')
        r'''
891 = radix_repr2uint__big_endian(8, [1, 5, 7, 3])
5491 = radix_repr2uint__big_endian(16, [1, 5, 7, 3])
38115 = radix_repr2uint__big_endian(32, [1, 5, 7, 3])
283075 = radix_repr2uint__big_endian(64, [1, 5, 7, 3])
1573 = radix_repr2uint__big_endian(10, [1, 5, 7, 3])
2535 = radix_repr2uint__big_endian(12, [1, 5, 7, 3])
16875 = radix_repr2uint__big_endian(24, [1, 5, 7, 3])
53391 = radix_repr2uint__big_endian(36, [1, 5, 7, 3])
        #'''

if __name__ == '__main__':
    #_t_xxx()
    _t1()
#]]]"""


