
'''
sympy.__version__ == '0.7.2'
'''

r'''
sympy bugs from Archimedean_solid__L_div_R_using_sympy
bug1 from calc_L_div_R:
    # calc g3434
    [3,4,3,4]:
        L/R should be 1
        but yields 0.999999999999999076021
        it seems sympy only have 15 precision
        even I set sympy.mpmath.mp.dps = 100 gets this wrong result
        it is far from real ans
    that is:
    var('g', positive=True)
    f = -48*asin(sqrt(2)/sqrt(-g**2 + 4)) - 48*asin(1/sqrt(-g**2 + 4)) + 24*pi
    assert 0 == nsimplify(f.subs(g,1))
    sympy.mpmath.mp.dps = 100
    x = nsolve(f, g, 1)
    assert str(x)[6:][:21] == '0.9999999999999990760'
    assert '0.9999999999999990760' in str(x)
    

bug2 from sorted_Cs2solids:
    assert hash(2) != hash(Integer(2))
    assert hash(Fraction(1,2)) != hash(Rational(1,2))
    fixed by:
        import nn_ns.sympy_util.bug_fix__rational_hash
bug3 from calc_g33335:
    var('GG', positive=True)
    u = (209*GG**6 - 2696*GG**5 + 13872*GG**4 - 35776*GG**3 + 47104*GG**2 - 27648*GG + 4096)
    h = (209*GG**3 + GG**2*(-1348 + 40*sqrt(5)) + GG*(-256*sqrt(5) + 2608) - 1312 + 416*sqrt(5))
    assert 0 == expand(gcd(u,h,extension=True)*209 - h)
    gg, = solve(h)
    assert 0 == nsimplify(u.subs(GG, gg))
    assert all(0 != nsimplify(gg - _gg) for _gg in solve(u))
    
'''

'''
sympy bugs from fraction_division.py
bug:
    from sympy import Integer
    from numbers import Integral
    assert not issubclass(Integer, Integral)
    
    fixed by:
        import nn_ns.sympy_util.bug_fix__resister_number_types

'''

'''
sympy bugs from from nn_ns.sympy_util.geometry.py
bug1 from vec_sub:
    sympy bug: Tuple.__new__ not like tuple's!!!
    so type(Tuple_obj)(x for x in ls) fail

'''


r'''
sympy bugs from nth_pow_continued_fraction.py
bug1 from continued_fraction_dc:
    # expand(2**(1/3)) to 102 continued_fraction digits
    cf, xs = nth_pow_continued_fraction(2,3,102) 
    assert 0 in cf

    that is:
    from sympy import sympify, floor
    one = sympify(1)
    N = (-18946643396438422418200496503661148314139229271682874349*2**(one/3)
         + 23871274840024462774930909433822752859720888716067576820
         )
    D = (-133450479581198331510402510274281177418327310779117149571
         + 105919715836427477757469402582631193698068222179903783354*2**(one/3)
         )
    # assert xs[101] == N/D
    assert floor(N/D) == 0 # should be 1
    assert N > D
    assert D > N
    assert N-D > 0
    assert not (D-N < 0)
    assert str((N-D).evalf(10)) == '1.690148127e-57'

bug2 from root-finding/intervals:
    var('W')
    A, B = 1,2
    x = A+B*W
    A, B = map(Wild, 'A, B'.split(', '))
    X = A+B*W
    m = X.matches(x)
    assert m == {A: 2*W, B: 1/W}

bug3 or not: from __to_std_args_for_NthPow:
    cannot simplify: '-18**(1/3)/3 + 2**(1/3)*3**(2/3)/3' to 0
    
'''

from fractions import Fraction
from sympy import var, asin, sqrt, pi, nsimplify, nsolve, \
     Rational, Integer, expand, gcd, solve, sympify, floor, \
     Wild
import sympy.mpmath
import sympy
import numbers

# bug_...(): return True while the bug exists
def bug_not_high_precision():
    var('g', positive=True)
    f = -48*asin(sqrt(2)/sqrt(-g**2 + 4)) - 48*asin(1/sqrt(-g**2 + 4)) + 24*pi
    assert 0 == nsimplify(f.subs(g,1))
    sympy.mpmath.mp.dps = 100
    x = nsolve(f, g, 1)
    '''str(x)='0.99...' or "mpf('0.99...')" '''
    return '0.9999999999999990760' in str(x)
    assert str(x)[6:][:21] == '0.9999999999999990760'
    assert '0.9999999999999990760' in str(x)

def bug_not_using_std_hash_of_rational():
    return hash(2) != hash(Integer(2)) or hash(Fraction(1,2)) != hash(Rational(1,2))

def bug_calc_other_root():
    var('GG', positive=True)
    u = (209*GG**6 - 2696*GG**5 + 13872*GG**4 - 35776*GG**3 + 47104*GG**2 - 27648*GG + 4096)
    h = (209*GG**3 + GG**2*(-1348 + 40*sqrt(5)) + GG*(-256*sqrt(5) + 2608) - 1312 + 416*sqrt(5))
    assert 0 == expand(gcd(u,h,extension=True)*209 - h)
    gg, = solve(h)
    assert 0 == nsimplify(u.subs(GG, gg))
    return all(0 != nsimplify(gg - _gg) for _gg in solve(u))


__number_type_pairs = (
    (numbers.Number, sympy.Number),
    (numbers.Real, sympy.Float),
    (numbers.Rational, sympy.Rational),
    (numbers.Integral, sympy.Integer),
    )

def bug_not_using_std_number_hierarchy():
    return not all(issubclass(sympy_type, std_type)
                   for std_type, sympy_type in __number_type_pairs)

def bug_Tuple_not_using_iterable_to_init():
    return len(sympy.Tuple(range(3))) == 1

def bug_floor_and_cmp_fail():
    one = sympify(1)
    N = (-18946643396438422418200496503661148314139229271682874349*2**(one/3)
         + 23871274840024462774930909433822752859720888716067576820
         )
    D = (-133450479581198331510402510274281177418327310779117149571
         + 105919715836427477757469402582631193698068222179903783354*2**(one/3)
         )
    # assert xs[101] == N/D
    #assert floor(N/D) == 0 # should be 1
    return floor(N/D) == 0 or (N > D and D > N)
    assert N > D
    assert D > N
    assert N-D > 0
    assert not (D-N < 0)
    assert str((N-D).evalf(10)) == '1.690148127e-57'


def bug_weird_Wild_matches():
    var('W')
    A, B = 1,2
    x = A+B*W
    A, B = map(Wild, 'A, B'.split(', '))
    X = A+B*W
    m = X.matches(x)
    return m == {A: 2*W, B: 1/W}

__all__ = tuple(bug_func_name for bug_func_name in globals().keys()
                if bug_func_name.startswith('bug_'))

def test_all():    
    for bug_func_name in __all__:
        bug_func = globals()[bug_func_name]
        print('{}: {}'.format(bug_func.__name__, bug_func()))

if __name__ == '__main__':
    test_all()

    import nn_ns.sympy_util.bug_fix__resister_number_types
    import nn_ns.sympy_util.bug_fix__rational_hash
    print('''
after:
    import nn_ns.sympy_util.bug_fix__resister_number_types
    import nn_ns.sympy_util.bug_fix__rational_hash''')
    test_all()

    if False: #fail
        from nn_ns.math_nn.fraction_division import scoped_factiondiv_env
        print('\nusing "with fraction_division.scoped_factiondiv_env():"')
        with scoped_factiondiv_env():
            test_all()

        



