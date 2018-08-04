


'''
https://en.wikipedia.org/wiki/Bijective_numeration

Radix <- PInt
BiDigit = [1..Radix]
    # compare Digit = [0..Radix-1]

# little-endian
bidigitsLE2uint :: [BiDigit] -> UInt
bidigitsLE2uint ds = f ds 1 where
    f [] weight = 0
    f (h:ts) weight = h*weight + f ts (weight*Radix)
bidigitsLE2uint = f where
    f [] = 0
    f (h:ts) = h + (f ts) * Radix

bidivmod :: UInt -> PInt -> (UInt, PInt)
bidivmod n d = (q, r) where
    # q = ceil(n/d) - 1 = floor((n+d-1)/d) - 1 = floor((n-1)/d)
    q = (n-1)//d
    r = n - q*d
uint2bidigitsLE :: UInt -> [BiDigit]
uint2bidigitsLE = f where
    f 0 = []
    f n = r : f q where
        (q, r) = bidivmod n Radix


'''

__all__ = '''
    bidigits2uint__little_endian
    uint2bidigits__little_endian
    '''.split()

from .ArbitraryRadixNumber import \
    number2iter_arbitrary_radix_reprLE, arbitrary_radix_reprBE2number
def bidivmod(n, d):
    #ssert n >= 0
    #ssert d >= 1
    q, r = divmod(n-1, d)
    r += 1
    return q, r
    q = (n-1)//d
    r = n - q*d
def uint2iter_bidigitsLE(radix, u):
    assert u >= 0
    assert radix >= 1 # need not 2
    return number2iter_arbitrary_radix_reprLE(u, radix, 0, bidivmod)
    ''' bug: should comment below code to disable 'yield'!!
    while u > 0:
        u, r = bidivmod(u, radix)
        yield r
    '''
def uint2bidigitsLE(radix, u):
    return tuple(uint2iter_bidigitsLE(radix, u))
def bidigitsLE2uint(radix, bidigits):
    # little-endian
    assert all(1<=d<=radix for d in bidigits)
    return arbitrary_radix_reprBE2number(reversed(bidigits), radix, 0)
    u = 0
    for d in reversed(bidigits):
        u *= radix
        u += d
    return u
bidigits2uint__little_endian = bidigitsLE2uint
uint2bidigits__little_endian = uint2bidigitsLE

def test():
    for radix in range(1, 5):
        for u in range(100):
            bs = uint2bidigitsLE(radix, u)
            u_ = bidigitsLE2uint(radix, bs)
            #rint(u, bs, u_)
            assert u == u_
    from itertools import product
    for radix in range(1, 5):
        for L in range(5):
            for bs in product(range(1, radix+1), repeat=L):
                u = bidigitsLE2uint(radix, bs)
                bs_ = uint2bidigitsLE(radix, u)
                assert bs == bs_

if __name__ == '__main__':
    print('test BijectiveNumeration.py')
    test()



