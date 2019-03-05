
r'''
>>> Nothing = []
>>> power_of(3, 0, one=Nothing) is Nothing
True
>>> power_of(3, 4) == 3**4
True
>>> power_of(3, 4, mul=operator.__add__) == 3*4
True
>>> power_of(3, 4, power_modulus=5) == 3**4
True
>>> power_of(3, 4, power_modulus=3) == 3**1
True
'''

__all__ = '''
    power_of
    calc_power
    calc_power_ex
    '''.split()

import operator

__Nothing = object()
def power_of(T, power, *, one = __Nothing, mul=None, power_modulus=None):
    assert isinstance(power, int)
    return calc_power_ex(one, [T], power, mul=mul, power_modulus=power_modulus)


def calc_power_ex(I, T_2pow_ls, power:int, *, mul, power_modulus:int):
    '''
input:
    I :: M | Nothing
        I = T^0 | Nothing
    T_2pow_ls :: IN OUT [M]
        len(T_2pow_ls) >= 0
        T_2pow_ls = [T^(2^i) for i in [0..]]
    power :: int
        need not UInt! vs calc_power
    mul :: None | (M -> M -> M)
    power_modulus :: None | PInt
        power_modulus >= 0
output:
    T^power
'''
    if power_modulus is not None:
        power = power % power_modulus
    return calc_power(I, T_2pow_ls, power, mul=mul)

def calc_power(I, T_2pow_ls, power:int, *, mul):
    '''
input:
    I :: M | Nothing
        I = T^0 | Nothing
    T_2pow_ls :: IN OUT [M]
        len(T_2pow_ls) >= 0
        T_2pow_ls = [T^(2^i) for i in [0..]]
    power :: UInt
        power >= 0
    mul :: None | (M -> M -> M)
output:
    T^power
'''
    if not len(T_2pow_ls): raise ValueError
    if not power >= 0: raise ValueError
    if I is __Nothing and not power > 0: raise ValueError

    if mul is None:
        mul = operator.__mul__

    s01 = bin(power)[-1:1:-1]

    while len(T_2pow_ls) < len(s01):
        T = T_2pow_ls[-1]
        T_2pow_ls.append(mul(T, T))
    assert len(T_2pow_ls) >= len(s01)

    '''
    T = I
    for t, c in zip(T_2pow_ls, s01):
        if c == '1':
            T = T*t
    '''

    i = s01.find('1')
    if i == -1:
        return I

    R = T_2pow_ls[i]
    for TPOW, c in zip(T_2pow_ls[i+1:], s01[i+1:]):
        if c == '1':
            R = mul(R, TPOW)

    return R




if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


