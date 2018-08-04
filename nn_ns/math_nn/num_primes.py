

'''
num_primes_le(n) = |{p <= n | [prime p]}|

'''


from .prime2 import primes_lt, sorted_primes_endby_ge
from itertools import accumulate, chain
import operator

def num_primes_le(n):
    primes, i = sorted_primes_endby_ge(n)
    assert 0 <= i < len(primes)
    assert n <= primes[i]
    assert i == 0 or primes[i-1] < n
    return i+1 if n == primes[i] else i
def _num_primes_ls_le(n):
    num_primes_le(n)
    return [num_primes_le(i) for i in range(n)]


def num_primes_ls_le(n):
    ps = primes_lt(n)
    #ps.append(n)
    ps = chain(ps, [n])
    ls = [0]*n
    prev_count, prev_p = (0, 0)
    for count, p in enumerate(ps, 1):
        for i in range(prev_p, p):
            ls[i] = prev_count
        prev_count, prev_p = count, p
    return ls

_test_data = num_primes_ls_le(17+1)
#rint(_test_data)
[0, 0, 1, 2, 0, 3, 0, 4, 0, 0, 0, 5, 0, 6, 0, 0, 0, 7]
[0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7]
assert _test_data == [0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7]
#rint(_num_primes_ls_le(len(_test_data)))
assert _test_data == _num_primes_ls_le(len(_test_data))


def II(start, iterable, binop = None):
    if binop is None:
        binop = operator.mul
    for x in iterable:
        start = binop(start, x)
    return start
def II1(iterable, binop = None, default=1):
    it = iter(iterable)
    for h in it: break
    else: return default
    return II(h, it, binop)

from fractions import Fraction as F
def not_multiples_of_distinguish_primes(ps):
    fs = map(not_multiples_of, ps)
    return II(1, fs)
def not_multiples_of(p):
    return 1 - F(1, p)

if 0:
    def _t(n):
        assert n > 2
        ps = primes_lt(n)
        modulo = II(1, ps)
        count = num_primes_le(modulo)
        fr = not_multiples_of_distinguish_primes(ps)
        fr_ = float(fr)
        print(ps, modulo, count, fr, fr_, modulo.bit_length(), 'bits')


    for p in primes_lt(1+17):
        _t(1+p)
    '''
    (2,) 2 1 1/2 0.5 2 bits
    (2, 3) 6 3 1/3 0.3333333333333333 3 bits
    (2, 3, 5) 30 10 4/15 0.26666666666666666 5 bits
    (2, 3, 5, 7) 210 46 8/35 0.22857142857142856 8 bits
    (2, 3, 5, 7, 11) 2310 343 16/77 0.2077922077922078 12 bits
    (2, 3, 5, 7, 11, 13) 30030 3248 192/1001 0.1918081918081918 15 bits
    (2, 3, 5, 7, 11, 13, 17) 510510 42331 3072/17017 0.18052535699594524 19 bits
    '''

if 0:
    ps_ = primes_lt(1+53)
    for i in range(len(ps_)+1):
        ps = ps_[:i]
        modulo = II(1, ps)
        fr = not_multiples_of_distinguish_primes(ps)
        fr_ = float(fr)
        print(fr_, fr, modulo, modulo.bit_length(), 'bits', ps)
    '''
    1.0 1 1 1 bits ()
    0.5 1/2 2 2 bits (2,)
    0.3333333333333333 1/3 6 3 bits (2, 3)
    0.26666666666666666 4/15 30 5 bits (2, 3, 5)
    0.22857142857142856 8/35 210 8 bits (2, 3, 5, 7)
    0.2077922077922078 16/77 2310 12 bits (2, 3, 5, 7, 11)
    0.1918081918081918 192/1001 30030 15 bits (2, 3, 5, 7, 11, 13)
    0.18052535699594524 3072/17017 510510 19 bits (2, 3, 5, 7, 11, 13, 17)
    0.17102402241721126 55296/323323 9699690 24 bits (2, 3, 5, 7, 11, 13, 17, 19)
    0.16358819535559338 110592/676039 223092870 28 bits (2, 3, 5, 7, 11, 13, 17, 19, 23)
    0.15794722310195225 442368/2800733 6469693230 33 bits (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
    0.15285215138898603 13271040/86822723 200560490130 38 bits (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)
    0.1487210121622567 477757440/3212440751 7420738134810 43 bits (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    0.14509367040220164 19110297600/131710070791 304250263527210 49 bits (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41)
    0.14171939899749927 802632499200/5663533044013 13082761331670030 54 bits (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43)
    0.13870409263585035 1605264998400/11573306655157 614889782588491410 60 bits (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    0.13608703428423055 6421059993600/47183480978717 32589158477190044730 65 bits (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53)
    '''

