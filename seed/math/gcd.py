#__all__:goto
r'''
from seed.math.gcd import gcd, gcd_many, are_coprime

[deprecated]:
from fractions import gcd
ImportError: cannot import name 'gcd' from 'fractions' (/data/data/com.termux/files/usr/lib/python3.10/fractions.py)


py -m nn_ns.app.debug_cmd   seed.math.gcd -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.gcd:__doc__ -ht # -ff -df


>>> from itertools import product
>>> for a, b in product(range(-50, 51), repeat=2):
...     assert py_std_gcd(a, b) == gcd_via_halve_(a, b), (a,b)
>>> for a, b in product(range(-50, 51), repeat=2):
...     assert are_coprime__using_py_std_gcd_(a, b) is are_coprime__detect_via_halve_(a, b), (a,b)

>>> gcd is py_std_gcd
True
>>> are_coprime is are_coprime__using_py_std_gcd_
True
>>> gcd_many([36, 81, 72])
9
>>> gcd_ex(36, 81)
(4, 9, 9)
>>> gcd_ex(36, 45)
(4, 9, 5)

>>> gcdext(36, 45)
(9, ((4, 4), (-3, 5)))



>>> def call_(f, kwds4f, args4product, /, *, to_unbox, to_show, kwds4product={}):
...     for us in product(*args4product, **kwds4product):
...         r = f(*(us if to_unbox else [us]), **kwds4f)
...         if to_show:
...             print(us, r, sep=':')


>>> gcdext(36, 45)
(9, ((4, 4), (-3, 5)))
>>> call_(gcdext, dict(validate=True), [range(-60,1+60), range(-60,1+60)], to_unbox=True, to_show=False)
>>> call_(gcdext, dict(validate=True), [range(-2,1+2), range(-2,1+2)], to_unbox=True, to_show=True)
(-2, -2):(2, ((0, -1), (-1, -1)))
(-2, -1):(1, ((0, -2), (-1, -1)))
(-2, 0):(2, ((-1, -1), (0, 0)))
(-2, 1):(1, ((0, -2), (1, 1)))
(-2, 2):(2, ((0, -1), (1, 1)))
(-1, -2):(1, ((1, -1), (-1, -2)))
(-1, -1):(1, ((0, -1), (-1, -1)))
(-1, 0):(1, ((-1, -1), (0, 0)))
(-1, 1):(1, ((0, -1), (1, 1)))
(-1, 2):(1, ((1, -1), (1, 2)))
(0, -2):(2, ((0, 0), (-1, -1)))
(0, -1):(1, ((0, 0), (-1, -1)))
(0, 0):(0, ((0, 0), (1, 1)))
(0, 1):(1, ((0, 0), (1, 1)))
(0, 2):(2, ((0, 0), (1, 1)))
(1, -2):(1, ((1, 1), (0, -2)))
(1, -1):(1, ((0, 1), (-1, -1)))
(1, 0):(1, ((1, 1), (0, 0)))
(1, 1):(1, ((0, 1), (1, 1)))
(1, 2):(1, ((1, 1), (0, 2)))
(2, -2):(2, ((0, 1), (-1, -1)))
(2, -1):(1, ((0, 2), (-1, -1)))
(2, 0):(2, ((1, 1), (0, 0)))
(2, 1):(1, ((0, 2), (1, 1)))
(2, 2):(2, ((0, 1), (1, 1)))


>>> gcdext_many([])
(0, ())
>>> gcdext_many([36])
(36, ((1, 1),))
>>> gcdext_many([36, 45])
(9, ((4, 4), (-3, 5)))
>>> gcdext_many([36, 45, 81])
(9, ((4, 4), (-3, 5), (0, 9)))
>>> gcdext_many([36, 45, 21])
(3, ((-4, 12), (0, 15), (7, 7)))
>>> gcdext_many([36, 45, 21, 7])
(1, ((-6, 36), (0, 45), (0, 21), (31, 7)))
>>> gcdext_many([0])
(0, ((1, 1),))
>>> gcdext_many([0, 0])
(0, ((0, 0), (1, 1)))
>>> gcdext_many([0, 0, 0])
(0, ((0, 0), (0, 0), (1, 1)))


fancy=True
>>> call_(gcdext_many, dict(fancy=True, validate=True), [range(0,1+60), range(0,1+30)], to_unbox=False, to_show=False)
>>> call_(gcdext_many, dict(fancy=True, validate=True), [range(0,1+30), range(0,1+30), range(0,1+30)], to_unbox=False, to_show=False)
>>> call_(gcdext_many, dict(fancy=True, validate=True), [range(0,1+10), range(0,1+10), range(0,1+10), range(0,1+10)], to_unbox=False, to_show=False)

fancy=False
>>> call_(gcdext_many, dict(fancy=False, validate=True), [range(0,1+60), range(0,1+30)], to_unbox=False, to_show=False)
>>> call_(gcdext_many, dict(fancy=False, validate=True), [range(0,1+30), range(0,1+30), range(0,1+30)], to_unbox=False, to_show=False)
>>> call_(gcdext_many, dict(fancy=False, validate=True), [range(0,1+10), range(0,1+10), range(0,1+10), range(0,1+10)], to_unbox=False, to_show=False)










noncoprime_part_of_to_
    coprime_part_of_to_
>>> noncoprime_part_of_to_(-1, 2*3*5*7)
1
>>> noncoprime_part_of_to_(16, 2*3*5*7)
16
>>> noncoprime_part_of_to_(16*17, 2*3*5*7)
16
>>> noncoprime_part_of_to_(-16*9*5*17, 2*3*5*7)
720


>>> coprime_part_of_to_(-1, 2*3*5*7)
1
>>> coprime_part_of_to_(16, 2*3*5*7)
1
>>> coprime_part_of_to_(16*17, 2*3*5*7)
17
>>> coprime_part_of_to_(-16*9*5*17, 2*3*5*7)
17








'''#'''


__all__ = r'''
noncoprime_part_of_to_
    coprime_part_of_to_

gcdext
    gcdext_many

gcd_ex
gcd
    gcd_many

are_coprime
    py_std_gcd
    are_coprime__using_py_std_gcd_

    gcd_via_halve_
    are_coprime__detect_via_halve_
    '''.split()#'''


from math import gcd as py_std_gcd
#import functools # reduce

def are_coprime__using_py_std_gcd_(a, b, /):
    if a&1 == 0 == b&1:
        # (even, even) # (0, 0)
        return False
    return 1 == py_std_gcd(a, b)
gcd = py_std_gcd or gcd_via_halve_
are_coprime = are_coprime__using_py_std_gcd_ or are_coprime__detect_via_halve_

def gcd_many(iterable):
    #only for int
    return gcd(*iterable)
    #return functools.reduce(gcd, iterable, 0)
def gcd_ex(a, b, /):
    g = gcd(a, b)
    a_g = a//g
    b_g = b//g
    return (a_g, g, b_g)




def _factor_out_odd(n, /):
    assert n > 0
    e2 = 0
    while not n&1:
        n >>= 1
        e2 += 1
    odd = n
    return (odd, e2)
def gcd_via_halve_(a, b, /):
    a = abs(a)
    b = abs(b)
    if b == 0:
        return a
    if a == 0 or a == b:
        return b
    (a, eA) = _factor_out_odd(a)
    (b, eB) = _factor_out_odd(b)
    e2 = min(eA, eB)
    if a > b:
        a, b = b, a
    return _gcd_odds_via_halve(a, b) << e2

def _gcd_odds_via_halve(a, b, /):
    assert 1 <= a <= b, (a, b)
    assert 1 == a&1 == b&1, (a, b)
    if a == 1:
        return 1
    # [1 < a <= b]
    # [1 == a%2 == b%2]
    while 1:
        # [1 < a <= b]
        # [1 == a%2 == b%2]
        d = b - a
        # [d >= 0]
        # [d%2 == 0]
        if not d:
            return a
        # [d >= 1]
        # [d%2 == 0]
        (b, e2) = _factor_out_odd(d)
        assert e2
        # [e2 > 0][new-b < old-b] => loop-halt
        # [b >= 1]
        # [1 == b%2]
        # [a <?> b]

        # [1 == a%2 == b%2]
        # [1 < a]
        if b < a:
            # [1 <= b < a]
            a, b = b, a
            # [1 <= a < b]
            if a == 1:
                return 1
            # [1 < a < b]
        else:
            # [a <= b]
            # [1 < a <= b]
            pass
        # [1 < a <= b]
        # [1 == a%2 == b%2]


def are_coprime__detect_via_halve_(a, b, /):
    if a&1 == 0 == b&1:
        # (even, even) # (0, 0)
        return False
    a = abs(a)
    b = abs(b)
    if a == 1 or b == 1:
        return True
    if a == 0 or b == 0:
        return False
    (a, eA) = _factor_out_odd(a)
    (b, eB) = _factor_out_odd(b)
    if a > b:
        a, b = b, a
    for p in _ps4detect:
        if a%p == 0 == b%p:
            return False
    return _gcd_odds_via_halve(a, b) == 1
_ps4detect = (3,5,7)


def _sign_abs5nonzero_(x, /):
    assert x
    return (+1, x) if x > 0 else (-1, -x)
def _check_result4gcdext(a, b, r, /):
    (d, ((u,a_d), (v,b_d))) = r
    assert d >= 0
    assert a == a_d*d
    assert b == b_d*d
    assert u*a_d+v*b_d == 1
    if a and b:
        assert 0 <= u < abs(b_d)
        assert abs(v) <= abs(a_d)
def gcdext(a, b, /, *, validate=True):
    r'''[[[
    a -> b -> (d, ((u,a_d), (v,b_d)))
    [d >= 0]
    [a == a_d*d][b == b_d*d]
    [u*a_d+v*b_d == 1]

    [A:=abs(a)]
    [Sa:=sign(a)]
    [B:=abs(b)]
    [Sb:=sign(b)]

    [a==0==b]:
        #old:-> (0, ((1,1), (0,0)))
        -> (0, ((0,0), (1,1)))
            !! gcdext_many([0,0,0])
    [a=!=0==b]:
        -> (A, ((Sa,Sa), (0,0)))
    [a==0=!=b]:
        -> (B, ((0,0), (Sb,Sb)))
    [a=!=0=!=b]:
        [d == gcd(a,b) > 0]
        [a_d:=a///d]
        [b_d:=b///d]
        [0 <= u < abs(b_d)]
        [abs(v) <= abs(a_d)]
        -> (d, ((u,a_d), (v,b_d)))

    name "gcdext" from PARI-GP
        gcdext(x,y): returns [u,v,d] such that d=gcd(x,y) and u*x+v*y=d.

    #]]]'''#'''
    #'a -> b -> (u, v, d) # [u*a+v*b == d][a%%d == 0][b%%d == 0][d > 0]'
    if validate:
        r = gcdext(a, b, validate=False)
        return r

    if a == 0:
        if b == 0:
            # [a==0==b]
            #return (0, ((1,1), (0,0)))
            # !! gcdext_many([0,0,0])
            return (0, ((0,0), (1,1)))
        (Sb, B) = _sign_abs5nonzero_(b)
        # [a==0=!=b]
        return (B, ((0,0), (Sb,Sb)))
    elif b == 0:
        # [a=!=0==b]
        (Sa, A) = _sign_abs5nonzero_(a)
        return (A, ((Sa,Sa), (0,0)))
    else:
        # [a=!=0=!=b]

        (a_d, d, b_d) = gcd_ex(a, b)
        # [d == gcd(a,b) > 0]
        # [d > 0]
        # [a == a_d*d][b == b_d*d]
        # [1==gcd(a_d,b_d)]
        # !! [b=!=0]
        # [b_d=!=0]
        u = pow(a_d, -1, abs(b_d))
            # [0 == pow(0,-1,1)]
            # [+3 == pow(2,-1,+5)]
            # [-2 == pow(2,-1,-5)]
        # [0 <= u < abs(b_d)]
        # [u*a_d %b_d == 1]
        ua_d = u*a_d
        v = (1-ua_d)//b_d
        vb_d = v*b_d
        assert ua_d+vb_d == 1
        # [u*a_d+v*b_d == 1]
        # !! [0 <= u < abs(b_d)]
        # !! [v == (1-u*a_d)///b_d]
        # [v{u:=0} == 1/b_d]
        # [v{u:=(-1+abs(b_d))} == (1-(-1+abs(b_d))*a_d)/b_d == (1/b_d +(-sign(b_d) +1/b_d)*a_d)]
        # [[b>0] -> [(-sign(b_d) +1/b_d) <= 0]
        # [[b<0] -> [(-sign(b_d) +1/b_d) >= 0]
        # [w:=(1/b_d +(-sign(b_d) +1/b_d)*a_d)]
        # [[a*b>0] -> [w <= v <= 1/b_d]
        # [[a*b<0] -> [1/b_d <= v <= w]

        # !! [0 <= u < abs(b_d)]
        # !! [v == (1-u*a_d)///b_d]
        # [abs(v) <= (1+abs(u*a_d))/abs(b_d) <= (1+(-1+abs(b_d))*abs(a_d))/abs(b_d) == abs(a_d) +(1-abs(a_d))/abs(b_d) <= abs(a_d)]
        # [abs(v) <= abs(a_d)]


        # [u*a_d+v*b_d == 1]
        # [0 <= u < abs(b_d)]
        # [a == a_d*d][b == b_d*d]
        # [d > 0]
        return (d, ((u,a_d), (v,b_d)))
    raise 000




def gcdext_many(iterable, /, *, validate=True, fancy=True):
    if validate or fancy:
        iterable = tuple(iterable)
    if fancy:
        ju_ls = sorted(enumerate(iterable), key=lambda j_u:abs(j_u[1]))
        iterable7saved = iterable
        iterable = tuple(u for j, u in ju_ls)


    rs = []
    d = 0
    for b in iterable:
        a = d
        r = gcdext(a, b)
        rs.append(r)
        d = r[0]
    gd = d
    ls = []
    ku = 1 # == II(us[j:])  # from:u
    kd = 1 # == d///gd      # from:a_d
    for (d, ((u,a_d), (v,b_d))) in reversed(rs):
        ls.append((ku*v,kd*b_d))
        ku *= u
        kd *= a_d
    d = gd
    pairs = tuple(reversed(ls))
    #########
    if fancy:
        _pairs = [None]*len(pairs)
        for (j, _), pair in zip(ju_ls, pairs):
            _pairs[j] = pair
        pairs = tuple(_pairs)
        iterable = iterable7saved
    #########
    if validate:
        assert len(pairs) == len(iterable)
        assert all(b == b_gd*gd for b, (gv, b_gd) in zip(iterable, pairs)), (iterable, gd, pairs)
        assert not pairs or 1 == sum(gv*b_gd for b, (gv, b_gd) in zip(iterable, pairs)), (iterable, gd, pairs)
    #########
    return (gd, pairs)



def noncoprime_part_of_to_(u7whole, u7mask, /):
    'u7whole/int{=!=0} -> u7mask/int -> noncoprime_part/int{>0} # [noncoprime_part == II[p**gde(p;u7whole) | [p::prime][u7whole%p==0][u7mask%p==0]]]'
    assert u7whole
    #assert u7mask
    a = abs(u7whole)
    b = abs(u7mask)
    L = a.bit_length()
    e = 1<<L.bit_length()
    assert e >= L
    noncoprime_part = gcd(a, pow(b, e, a))
    return noncoprime_part
def coprime_part_of_to_(u7whole, u7mask, /):
    'u7whole/int{=!=0} -> u7mask/int -> coprime_part/int{>0} # [coprime_part == II[p**gde(p;u7whole) | [p::prime][u7whole%p==0][u7mask%p=!=0]]]'
    a = abs(u7whole)
    noncoprime_part = noncoprime_part_of_to_(a, u7mask)
    coprime_part = a//noncoprime_part
    return coprime_part


from seed.math.gcd import gcd, gcd_many, are_coprime
from seed.math.gcd import gcd_ex # -> (lhs///gcd, gcd, rhs///gcd)
from seed.math.gcd import gcdext, gcdext_many # -> (gcd, [(coeff4int, int///gcd)])
from seed.math.gcd import noncoprime_part_of_to_, coprime_part_of_to_
from seed.math.gcd import *
