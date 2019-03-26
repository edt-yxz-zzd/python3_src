
'''
'''

__all__ = '''
    iter_continued_fraction_of_sqrt_of_UInt
    splited_periodic_continued_fraction_of_sqrt_of_UInt
    floor_sqrt_of_UInt
    '''.split()
    #_is_lt_0
    #one
    #zero

from ..floor_sqrt import floor_sqrt
from fractions import Fraction
from math import floor

one = Fraction(1)
zero = Fraction(0)
def iter_continued_fraction_of_sqrt_of_UInt(n):
    (non_periodic_digits, periodic_digits
    ) = splited_periodic_continued_fraction_of_sqrt_of_UInt(
        n, sqrt_coeff=one, constant=zero)
    yield from non_periodic_digits
    if periodic_digits:
        while True:
            yield from periodic_digits


def _is_lt_0(
    n, *, sqrt_coeff:Fraction, constant:Fraction
    , n_sqrt_coeff_2:Fraction, constant_2:Fraction
    ):
    '''x = sqrt(n)*sqrt_coeff + constant < 0?

[sqrt(n)*sqrt_coeff + constant < 0]
'''
    if not n >= 0: raise ValueError
    if n_sqrt_coeff_2 is None:
        n_sqrt_coeff_2 = n*sqrt_coeff**2
    if constant_2 is None:
        constant_2 = constant**2
    assert n_sqrt_coeff_2 >= 0
    assert constant_2 >= 0

    if not sqrt_coeff or not n:
        return constant < 0
    elif sqrt_coeff < 0:
        # [sqrt_coeff < 0]
        if constant <= 0:
            return True
        # [sqrt(n)*sqrt_coeff < 0][-constant < 0]!
        # [sqrt(n)*sqrt_coeff < -constant < 0]?
        # [n*sqrt_coeff^2 > constant^2 > 0]?
        return n_sqrt_coeff_2 > constant_2
    else:
        # [sqrt_coeff > 0]
        if constant >= 0:
            return False
        # [0 < sqrt(n)*sqrt_coeff][0 < -constant]!
        # [0 < sqrt(n)*sqrt_coeff < -constant]?
        # [0 < n*sqrt_coeff^2 < constant^2]?
        return n_sqrt_coeff_2 < constant_2

def floor_sqrt_of_UInt(
    n, *, sqrt_coeff:Fraction, constant:Fraction
    , n_sqrt_coeff_2:Fraction
    ):
    '''
x = sqrt(n)*sqrt_coeff + constant
bug: floor(x) = constant + floor_sqrt(n*sqrt_coeff^2)
floor(x) = floor(constant) + floor_sqrt(n*sqrt_coeff^2) + (0|1)

pseudo_floor(x) = floor(constant) + floor_sqrt(n*sqrt_coeff^2)
if _is_lt_0(x - pseudo_floor(x) -1):
    floor(x) = pseudo_floor(x)
else:
    floor(x) = pseudo_floor(x) + 1
    '''
    if n_sqrt_coeff_2 is None:
        n_sqrt_coeff_2 = n*sqrt_coeff**2
    pseudo_floor_x = floor(constant) + floor_sqrt(floor(n_sqrt_coeff_2))

    kwargs = dict(
                sqrt_coeff=sqrt_coeff
                , n_sqrt_coeff_2=n_sqrt_coeff_2
                , constant_2=None#vary!!!
                )
    if _is_lt_0(n, constant=constant-pseudo_floor_x-1, **kwargs):
        result = pseudo_floor_x
    else:
        result = pseudo_floor_x+1

    try:
        assert not _is_lt_0(n, constant=constant-result, **kwargs)
        assert _is_lt_0(n, constant=constant-result-1, **kwargs)
    except:
        print(n, kwargs, pseudo_floor_x, result)
        raise
    return result

def splited_periodic_continued_fraction_of_sqrt_of_UInt(
    n, *, sqrt_coeff:Fraction, constant:Fraction):
    '''UInt -> SInt -> SInt -> ([UInt], [UInt])

(non_periodic_digits, periodic_digits
) = splited_periodic_continued_fraction_of_sqrt_of_UInt n sqrt_coeff constant
input_number = sqrt(n)*sqrt_coeff + constant
continued_fraction_of input_number = non_periodic_digits + periodic_digits
'''
    assert type(n) is int
    assert type(sqrt_coeff) is Fraction
    assert type(constant) is Fraction
    assert n >= 0
    #assert sqrt_coeff != 0

    coeffs2idx = {}
    digits = []
    old_constant = constant
    old_sqrt_coeff = sqrt_coeff


    while True:
        coeffs = (sqrt_coeff, constant)
        maybe_idx = coeffs2idx.get(coeffs)
        if maybe_idx is not None:
            idx = maybe_idx
            non_periodic_digits = digits[:idx]
            periodic_digits = digits[idx:]
            assert periodic_digits
            break
        coeffs2idx[coeffs] = len(digits)
        n_sqrt_coeff_2 = n*sqrt_coeff**2

        floor_x = floor_sqrt_of_UInt(n
                    , sqrt_coeff=sqrt_coeff
                    , constant=constant
                    , n_sqrt_coeff_2=n_sqrt_coeff_2
                    )
        digits.append(floor_x)

        ### next round
        '''
        x' = 1/(x - floor_x(x))
            = 1/(sqrt(n)*sqrt_coeff + constant')
            = (-sqrt(n)*sqrt_coeff + constant')
             /(-n*sqrt_coeff^2 + constant'^2)
        '''
        constant -= floor_x
        D = constant**2 - n_sqrt_coeff_2
        if not D:
            non_periodic_digits = digits
            periodic_digits = []
            break
        sqrt_coeff = -sqrt_coeff/D
        constant /= D
    #del digits
    constant = old_constant
    sqrt_coeff = old_sqrt_coeff

    if (__debug__
        and periodic_digits
        and is_integer(sqrt_coeff)
        and is_integer(constant)
        ):
        # [constant is 0] ==>> cf = [a0; (ls++[2*a0])*+oo] and reverse(ls) == ls
        # cf = [constant+a0; (ls++[2*a0])*+oo] and reverse(ls) == ls

        d0 = digits[0]
        a0 = d0 - floor(constant)
        i = digits.index(2*a0, 1) # 2*a0 seems to be the largest digit
        period_at_most = i
        period = len(periodic_digits)
        assert period_at_most%period == 0
        assert period_at_most == period

        # constant is Integer
        L = len(non_periodic_digits)
        assert L <= 1
        assert (L == 0) is (d0 == 2*a0)
        if L == 1:
            assert d0 != 2*a0
            ls = periodic_digits[:-1]
        elif not L:
            # L == 0
            # [constant+a0; (ls++[2*a0])*+oo] == [constant+a0,...]*+oo
            assert d0 == 2*a0
            ls = periodic_digits[1:]
        else:
            raise logic-error
        [*rls] = reversed(ls)
        assert ls == rls

    del digits


    return non_periodic_digits, periodic_digits


def _t(n, sqrt_coeff, constant):
    r = (non_periodic_digits, periodic_digits
    ) = splited_periodic_continued_fraction_of_sqrt_of_UInt(n
        ,sqrt_coeff=sqrt_coeff, constant=constant
        )
    print(f'f(sqrt({n})*{sqrt_coeff}+{constant}) = {r}')
    print(f'len(non_periodic_digits)={len(non_periodic_digits)}')
    print(f'len(periodic_digits)={len(periodic_digits)}')

def is_odd(n:int):
    return n&1
def is_integer(r:Fraction):
    return abs(r.denominator) == 1

if __name__ == '__main__':
    _t(4, one, zero)
    _t(0, one, zero)
    _t(2, one, zero)
    _t(3, one, zero)
    _t(5, one, zero)
    _t(7, one, zero)
    _t(11, one, zero)
    _t(13, one, zero)
    _t(10005, 426880*one, zero)
        #len(non_periodic_digits)=1
        #len(periodic_digits)=78408


