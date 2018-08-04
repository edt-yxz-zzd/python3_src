
#from sand import top_level_import, to_names
#assert top_level_import(__name__, 'sand.forgot_import', args=('logic error',))


import fractions # .gcd
from fractions import Fraction
from numbers import Integral
from .integer.max_exp import max_exp, divides

__all__ = '''
    max_exp
    to_int
    is_int_factor
    II_base_exp
    divides
    factor_frac
    gcds
    lcms
    prime2exp_to_frac
    rational2int
    rational2pair
    signs
    '''.split()




def to_int(x):
    'why not int()? int(3.1) -> 3'
    if not isinstance(x, Integral):
        raise TypeError('not isinstance(x, Integral)')
    return int(x)

def is_int_factor(d, x):
    return x%d == 0


def II_base_exp(base_exp_ls):
    n = 1
    for base, exp in base_exp_ls:
        n *= base**exp
    return n


def factor_frac(f, factor_int):
    N, D = rational2pair(f)
    ns = factor_int(N)
    ds = factor_int(D)
    assert not (set(ns) & set(ds))
    ns.update((k,-v) for k,v in ds.items())
    return ns


def prime2exp_to_frac(prime2exp, frac_type=Fraction):
    f = frac_type(1)
    for p, e in prime2exp.items():
        #assert isinstance(e, Integral)
        if e > 0:
            f *= p**e
        elif e < 0:
            f /= p**-e
    return frac_type(f)

def rational2int(f):
    N, D = rational2pair(f)
    if D != 1:
        raise ValueError('not integer')
    return N
def rational2pair(f):
    f = Fraction(f)
    return f.numerator, f.denominator

def sign1(x):
    if x > 0:
        return 1
    if x == 0:
        return 0
    return -1
def signs(*xs):
    ss = tuple(map(sign1, xs))
    if not all(ss):
        return 0
    return (-1)**ss.count(-1)
def gcds(*xs):
    if any(abs(x)==1 for x in xs):
        return 1
    xs = (x for x in xs if x)
    
    r = 0
    for x in xs:
        r = abs(fractions.gcd(r, x))
        if r == 1:
            break
    return r

def __lcm(a, b):
    '(0,0) ==>> raise'
    return a*b//fractions.gcd(a,b)
def lcms(*xs):
    '0 in xs ==>> 0; result >= 0'
    if any(x==0 for x in xs):
        return 0
    xs = (abs(x) for x in xs)
    xs = (x for x in xs if x != 1)
    
    r = 1
    for x in xs:
        r = __lcm(r, x)
    return r
        
