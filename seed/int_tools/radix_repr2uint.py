
r'''
py -m seed.int_tools.radix_repr2uint





#'''

__all__ = '''
    radix_repr2uint
        radix_repr2uint__little_endian
        radix_repr2uint__big_endian

    IRadixRepr2Uint
        RadixRepr2Uint
    '''.split()

from seed.abc.abc import ABC, abstractmethod, override


class IRadixRepr2Uint(ABC):
    @abstractmethod
    def get_radix(sf):
        ...
    @abstractmethod
    def get_zero(sf):
        ...
    @abstractmethod
    def get_one(sf):
        ...
    @abstractmethod
    def add(sf, lhs, rhs):
        ...
    @abstractmethod
    def mul(sf, lhs, rhs):
        ...
    def radix_repr2uint(sf, digits, /,*, is_big_endian:bool):
        f = sf.radix_repr2uint__big_endian if is_big_endian else sf.radix_repr2uint__little_endian
        return f(digits)

    def radix_repr2uint__little_endian(sf, digits, /):
        u = sf.get_zero()
        weight = sf.get_one()
        base = sf.get_radix()
        mul = sf.mul
        add = sf.add

        for d in digits:
            u = add(mul(d, weight), u)
            weight = mul(weight, base)
        return u
    def radix_repr2uint__big_endian(sf, digits, /):
        u = sf.get_zero()
        base = sf.get_radix()
        mul = sf.mul
        add = sf.add

        for d in digits:
            u = add(mul(u, base), d)
        return u

class RadixRepr2Uint(IRadixRepr2Uint):
    def __init__(sf, radix, /):
        sf.__radix = radix

    @override
    def get_radix(sf):
        return sf.__radix
    @override
    def get_zero(sf):
        return 0
    @override
    def get_one(sf):
        return 1
    @override
    def add(sf, lhs, rhs):
        return lhs+rhs
    @override
    def mul(sf, lhs, rhs):
        return lhs*rhs
def radix_repr2uint__little_endian(radix, digits, /):
    return RadixRepr2Uint(radix).radix_repr2uint__little_endian(digits)
def radix_repr2uint__big_endian(radix, digits, /):
    return RadixRepr2Uint(radix).radix_repr2uint__big_endian(digits)
def radix_repr2uint(radix, digits, /,*, is_big_endian:bool):
    return RadixRepr2Uint(radix).radix_repr2uint(digits, is_big_endian=is_big_endian)




assert 1573 == radix_repr2uint__little_endian(10, reversed([1,5,7,3]))
assert 1573 == radix_repr2uint__big_endian(10, [1,5,7,3])
assert 1573 == radix_repr2uint(10, reversed([1,5,7,3]), is_big_endian=False)
assert 1573 == radix_repr2uint(10, [1,5,7,3], is_big_endian=True)



def _t():
    radixes = [8,16,32,64,10,12,24,36]
    digits = [1,5,7,3]
    for radix in radixes:
        u = radix_repr2uint__big_endian(radix, digits)
        print(f'{u} = radix_repr2uint__big_endian({radix}, {digits})')

if __name__ == '__main__':
    _t()


