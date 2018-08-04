
from fractions import Fraction


def factorial(n):
    if n < 0:
        raise ValueError('n < 0')
    
    r = 1
    for i in range(1, n+1):
        r *= i
    return r

def choose(n, i):
    '''II(n-k for k in [0..i-1])/i!'''

    if i < 0:
        return 0

    if n < 0:
        return choose(-n+(i-1),i) * (-1)**i

    
    i = min(i, n-i)
    if i < 0:
        return 0

    r = 1
    for x in range(n, n-i, -1):
        r *= x

    #assert r == factorial(n)//factorial(n-i)
    return r // factorial(i)
    

    
    
    r = 1
    if n < 0:
        n = n-(i-1)
        n = -n
        if i % 2:
            r = -1 # (-1)**i
            
    if not 0 <= i <= n:
        return 0

    _i = n - i
    if i > _i:
        i = _i
        

    for x in range(n, n-i, -1):
        r *= x

    #assert r == factorial(n)//factorial(n-i)
    return r // factorial(i)

def choose_fraction(fraction, i):
    if type(fraction) is int:
        return choose(fraction, i)

##    if fraction.denominator == 1:
##        return choose(fraction.numerator, i)

    
    r = Fraction(1, 1)
    for x in range(i):
        r *= fraction - x

    return r / factorial(i)
    


def factorials(n):
    '''factorials(range(n))

assert len(factorials(n)) == n or n < 0'''


    if n < 1:
        return []
    
    ls = [1]
    for i in range(1, n):
        ls.append(ls[-1]*i)
    return ls

assert [] == factorials(0)
assert [1] == factorials(1)
assert [1,1,2,6] == factorials(4)


def binomials(n):
    '''(1+1)**n

assert len(binomials(n)) == n+1 or n < 0'''
    if n < 0:
        return []

    L = n+1
    fs = factorials(L)
    ls = [None]*L
    for i in range(L):
        ls[i] = fs[n] // (fs[i]*fs[n-i])
    return ls

assert [1] == binomials(0)
assert [1,1] == binomials(1)
assert [1,4,6,4,1] == binomials(4)

def test_factorials():
    for n in range(10):
        fs1 = factorials(n)
        fs2 = [factorial(i) for i in range(n)]
        assert fs1 == fs2
        
def test_binomials():
    for n in range(10):
        bs1 = binomials(n)
        bs2 = [choose(n, i) for i in range(n+1)]
        bs3 = [choose_fraction(Fraction(n,1), i) for i in range(n+1)]
        if not bs1 == bs2 == bs3:
            print(bs1, bs2, bs3)
        assert bs1 == bs2 == bs3


test_factorials()
test_binomials()













    
