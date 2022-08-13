
r'''[[[
e ../../python3_src/seed/math/lcm_parts_of.py
!mv ../../python3_src/seed/math/lcm_parts.py ../../python3_src/seed/math/lcm_parts_of.py
py -m seed.math.lcm_parts_of
from seed.math.lcm_parts_of import lcm_parts_of


(s,t) -> (m,n)
[m*n == lcm(s,t)][gcd(m,n)==1][s%m==0][t%n==0]
[is_prime q][es:=max_power_of_base_as_factor_of_(q,s)][et:=max_power_of_base_as_factor_of_(q,t)]:
    * [es < et]:
        [max_power_of_base_as_factor_of_(q,m) == 0]
        [max_power_of_base_as_factor_of_(q,n) == et]
    * [es > et]:
        [max_power_of_base_as_factor_of_(q,m) == es]
        [max_power_of_base_as_factor_of_(q,n) == 0]
    * [es == et > 0]:
        [{max_power_of_base_as_factor_of_(q,m), max_power_of_base_as_factor_of_(q,n)} == {0, es}]
    * [es == et == 0]:
        [{max_power_of_base_as_factor_of_(q,m), max_power_of_base_as_factor_of_(q,n)} == {0}]

lcm_parts_of(s,t) -> (m_, g, n_)
    m_ 包含 q<[es>et]>**es
    n_ 包含 q<[es<et]>**et
    g  包含 q<[es==et>0]>**es
    [lcm(s,t)==m_*g*n_]
    ===可行(m,n):
    (m,n) := (m_*g1, g2*n_)
        where [g1*g2==g][gcd(g1,g2)==1]
        eg: [(g1,g2):=(g,1)]

源自:高斯 求 本原根%p 的 算法中
    素数p
    s = order<%p>(a)
    任选b <- {1..<p} \-\ {a**i %p | [i<-[1..=s]]}
    t = order<%p>(b)
    [s%t =!= 0]
    [lcm(s,t) =!= s]
    [lcm(s,t) > s]
    [lcm(s,t) >= t]
    ?m,n. [m*n == lcm(s,t)][gcd(m,n)==1][s%m==0][t%n==0]
    c = a**(s///m) * b**(t///n) %p
    [order<%p>(c) == m*n == lcm(s,t) > s]
    即 由a找到c，order增加
    ###
    https://libgen.lc/edition.php?id=135789101
    wget 'http://62.182.86.140/main/11000/d46c0428209914a6acfaede707854241/Paulo%20Ribenboim%20-%20The%20new%20book%20of%20prime%20number%20records-Springer%20%281996%29.djvu' -O 'The new book of prime number records(3ed)(1996)(Ribenboim).djvu'



#]]]'''
__all__ = '''
    lcm_parts_of
    '''.split()
from seed.math.gcd import gcd

def lcm_parts_of(s, t, /):
    's -> t -> (m_, g, n_)'
    if not type(s) is int: raise TypeError
    if not type(t) is int: raise TypeError
    if not s >= 1: raise ValueError
    if not t >= 1: raise ValueError
    #raise NotImplementedError
    g0 = gcd(s,t)
    def f(g, u, /):
        c = c0 = u // g
        assert c*g == u
        acc = 1
        c = gcd(g, c)
        while not c == 1:
            g //= c
            acc *= c
            c = gcd(g, c)
        v = c0*acc
        assert gcd(g,v) == 1
        return acc, v
    (acc_s, m_) = f(g0,s)
    (acc_t, n_) = f(g0,t)
    g = g0 //(acc_s*acc_t)
    assert m_*g*n_ == s*t//g0 #==lcm(s,t)
    assert gcd(m_,n_) == 1
    assert gcd(m_,g) == 1
    assert gcd(g,n_) == 1
    assert s%(m_*g) == 0
    assert t%(n_*g) == 0
    return (m_, g, n_)

assert lcm_parts_of(2**2 * 3**3 * 5**2 * 7**3 * 11**2 * 13**0, 2**0 * 3**2 * 5**2 * 7**3 * 11**3 * 13**2) == (2**2 * 3**3, 5**2 * 7**3, 11**3 * 13**2)

