

'''
H[n] = sum 1/i {i=1..n}

lg n = log n / log 2
UP(n) = floor(lg n) + 1 = n.bit_length()
UP(n)/2 < H[n] <= UP(n) for n >= 1


ln (n+1) = integrate 1/x {x=1->n+1} <= sum 1/i {i=1..n} = H[n]
ln n = integrate 1/x {x=1->n} >= sum 1/i {i=2..n} = H[n]-1 for n >= 1
ln n < ln (n+1) <= H[n] <= 1 + ln n, for n >= 1
ln n < H[n] < 1 + ln n, for n >= 2
floor H[n] = floor.ln (n+1) + [0 or 1], for n >= 0

'''

from fractions import Fraction
from .numberss import NumberList

fr = Fraction
one = Fraction(1)
zero = Fraction(0)

_data = [fr(0), fr(1), fr(3, 2), fr(11, 6), fr(25, 12), fr(137, 60), fr(49, 20), fr(363, 140), fr(761, 280), fr(7129, 2520), fr(7381, 2520)]

def H(n):
    return sum((fr(1, i) for i in range(1, n+1)), zero)

    r = zero
    for i in range(1, n+1):
        r += fr(1, i)

    return r

    
    
class HarmonicNumber(NumberList):
    def _calc_neg(self, n, nums):
        return 0
        raise NotImplementedError()
    def _calc_pos(self, n, nums):
        assert n > 0
        return nums[-1] + fr(1, n)
        raise NotImplementedError()
    def direct_calc(self, n):
        return H(n)
        raise NotImplementedError()

    
    def __init__(self):
        super().__init__([zero])

harmonic = harmonic_number = HarmonicNumber()

assert harmonic.get_first(len(_data)) == _data
assert all(harmonic.direct_calc(n) == harmonic(n) for n in range(-1, 5))

'''
_harmonic_numbers = [Fraction(0)]
def harmonic_numbers_least_len(L):
    ls = _harmonic_numbers
    if L > len(ls):
        pre = ls[-1]
        for n in range(len(ls), L):
            Hn = pre + one/n
            ls.append(Hn)
            pre = Hn
        assert len(ls) == L
    return ls

def harmonic_number(n):
    return harmonic_numbers_least_len(n+1)[n]

H = harmonic_number

_Hs = lambda L: harmonic_numbers_least_len(L)[:L]

assert harmonic_number(4) == Fraction(25, 12)
assert _Hs(11) == [fr(0), fr(1), fr(3, 2), fr(11, 6), fr(25, 12), fr(137, 60), fr(49, 20), fr(363, 140), fr(761, 280), fr(7129, 2520), fr(7381, 2520)]


#print([(UP_n/2 < H(n), H(n) <= UP_n, H(n), UP_n) for n in range(10) for UP_n in [n.bit_length()]])

'''








