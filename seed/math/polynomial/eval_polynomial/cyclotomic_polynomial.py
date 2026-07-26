#__all__:goto
r'''[[[
e ../../python3_src/seed/math/polynomial/eval_polynomial/cyclotomic_polynomial.py
see:
    pari-gp: polcyclo

seed.math.polynomial.eval_polynomial.cyclotomic_polynomial
py -m nn_ns.app.debug_cmd   seed.math.polynomial.eval_polynomial.cyclotomic_polynomial -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.polynomial.eval_polynomial.cyclotomic_polynomial:__doc__ -ht # -ff -df
#######

[[
come_from:
view others/数学/polynomial/polynomial_evaluation.txt
view ../../python3_src/seed/algo/FFT/convolution__7CRT.py
]]
[[
[p::prime][k::uint{>0}][x :<- FF(p**k)]:
    [x**(p**k) == x]
    [x*(-1+x**(-1+p**k)) == 0]
]]
[[
@20260620
[n>=1]:
  cyclotomic polynomial
  [PHI(n;x) =[def]= the polynomial of smallest degree having as roots all the primitive n-th roots of 1]
  a primitive nth root of 1
  [r(n) =[def]= cos(2*pi/n) +1j*sin(2*pi/n)]
  [PHI(n;x) == II[(x-r(n)**e) | [[e:<-[1..=n]][gcd(e,n)==1]]]]
  [(x**n - 1) == II[PHI(m;x) | [[m:<-[1..=n]][n%m==0]]]]
  [PHI(n;x) == (x**n - 1)/gcd((x**n - 1), II[(x**m - 1) | [[m:<-[1..<n]][n%m==0]]])]
[is_prime_(p)]:
  [PHI(p;x) == (x**p - 1)/(x-1)]
  [m>=1][m%p==0]:
    [PHI(p*m;x) == PHI(m;x**p)]
    也就是说，重点在于squarefree部分
  [m>=1][m%p=!=0]:
    [PHI(p*m;x) == PHI(m;x**p)/PHI(m;x)]
      计算squarefree部分
    =>:
    [e>=1]:
      [PHI(m*p**e;x) == PHI(m;x**p**e)/PHI(m;x**p**(e-1))]
[n::int][y::real][n>=2][y>1]:
  [{p | [[p:<-[1..]][is_prime_(p)][(y**n-1)%p==0][@[m:<-[1..<n]] -> [(y**m-1)%p=!=0]]]}
  # <=
  == {p | [[p:<-[1..]][is_prime_(p)][p%n==1][PHI(n;y)%p==0]]}
  # <=
  == {p | [[p:<-[1..]][is_prime_(p)][p%n=!=0][PHI(n;y)%p==0]]}
  ]
monic polynomial with integer coefficients.

]]
[[
DONE:iter_cyclotomic_polynomials__sorted_by_order_ sorted by num_coprimes{order}
iter_cyclotomic_polynomials__sorted_by_degree_
    view ../../python3_src/seed/math/valence_of_Euler_function.py
    from seed.math.prepare_p2e4N import num_coprimes_lt_, phi_
]]



'#'; __doc__ = r'#'
>>> cache = {}

>>> order = 2**3 *3**2 * 5
>>> order
360
>>> cs = cyclotomic_polynomial5order_(cache, order, None)
>>> cs
(1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
>>> _mul_order4var77polynomial7native_(cs, expected=order)
360

>>> [*iter_cyclotomic_polynomials__sorted_by_order_(cache, end=5)]
[(-1, 1), (1, 1), (1, 1, 1), (1, 0, 1)]
>>> [*iter_cyclotomic_polynomials__sorted_by_order_(cache, with_order=True, end=5)]
[(1, (-1, 1)), (2, (1, 1)), (3, (1, 1, 1)), (4, (1, 0, 1))]
>>> [*iter_cyclotomic_polynomials__sorted_by_order_(cache, with_degree=True, with_order=True, with_factorization4order=True, end=5)]
[(1, 1, {}, (-1, 1)), (1, 2, {2: 1}, (1, 1)), (2, 3, {3: 1}, (1, 1, 1)), (2, 4, {2: 2}, (1, 0, 1))]

>>> [*iter_cyclotomic_polynomials__sorted_by_degree_(cache, end=5)]
[(-1, 1), (1, 1), (1, 1, 1), (1, 0, 1), (1, -1, 1), (1, 1, 1, 1, 1), (1, 0, 0, 0, 1), (1, -1, 1, -1, 1), (1, 0, -1, 0, 1)]
>>> [*iter_cyclotomic_polynomials__sorted_by_degree_(cache, with_degree=True, end=5)]
[(1, (-1, 1)), (1, (1, 1)), (2, (1, 1, 1)), (2, (1, 0, 1)), (2, (1, -1, 1)), (4, (1, 1, 1, 1, 1)), (4, (1, 0, 0, 0, 1)), (4, (1, -1, 1, -1, 1)), (4, (1, 0, -1, 0, 1))]
>>> [*iter_cyclotomic_polynomials__sorted_by_degree_(cache, with_degree=True, with_order=True, with_factorization4order=True, end=5)]
[(1, 1, {}, (-1, 1)), (1, 2, {2: 1}, (1, 1)), (2, 3, {3: 1}, (1, 1, 1)), (2, 4, {2: 2}, (1, 0, 1)), (2, 6, {3: 1, 2: 1}, (1, -1, 1)), (4, 5, {5: 1}, (1, 1, 1, 1, 1)), (4, 8, {2: 3}, (1, 0, 0, 0, 1)), (4, 10, {5: 1, 2: 1}, (1, -1, 1, -1, 1)), (4, 12, {3: 1, 2: 2}, (1, 0, -1, 0, 1))]

>>> [*iter_cyclotomic_polynomials__sorted_by_(cache, degree_vs_order=False, with_degree=True, with_order=True, with_factorization4order=True, end=5)]
[(1, 1, {}, (-1, 1)), (1, 2, {2: 1}, (1, 1)), (2, 3, {3: 1}, (1, 1, 1)), (2, 4, {2: 2}, (1, 0, 1)), (2, 6, {3: 1, 2: 1}, (1, -1, 1)), (4, 5, {5: 1}, (1, 1, 1, 1, 1)), (4, 8, {2: 3}, (1, 0, 0, 0, 1)), (4, 10, {5: 1, 2: 1}, (1, -1, 1, -1, 1)), (4, 12, {3: 1, 2: 2}, (1, 0, -1, 0, 1))]
>>> [*iter_cyclotomic_polynomials__sorted_by_(cache, degree_vs_order=True, with_degree=True, with_order=True, with_factorization4order=True, end=5)]
[(1, 1, {}, (-1, 1)), (1, 2, {2: 1}, (1, 1)), (2, 3, {3: 1}, (1, 1, 1)), (2, 4, {2: 2}, (1, 0, 1))]
>>> [*iter_cyclotomic_polynomials__sorted_by_(cache, degree_vs_order=False, with_degree=True, with_order=True, with_factorization4order=True, end=5, squarefree_order_only=True)]
[(1, 1, {}, (-1, 1)), (1, 2, {2: 1}, (1, 1)), (2, 3, {3: 1}, (1, 1, 1)), (2, 6, {3: 1, 2: 1}, (1, -1, 1)), (4, 5, {5: 1}, (1, 1, 1, 1, 1)), (4, 10, {5: 1, 2: 1}, (1, -1, 1, -1, 1))]
>>> [*iter_cyclotomic_polynomials__sorted_by_(cache, degree_vs_order=True, with_degree=True, with_order=True, with_factorization4order=True, end=5, squarefree_order_only=True)]
[(1, 1, {}, (-1, 1)), (1, 2, {2: 1}, (1, 1)), (2, 3, {3: 1}, (1, 1, 1))]


>>> [*iter_exceptional_cyclotomic_polynomials__sorted_by_(cache, degree_vs_order=True, with_degree=True, with_order=True, with_factorization4order=True, begin=105, end=120)]
[(48, 105, {3: 1, 5: 1, 7: 1}, (1, 1, 1, 0, 0, -1, -1, -2, -1, -1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, -1, -1, -2, -1, -1, 0, 0, 1, 1, 1))]
>>> [*iter_exceptional_cyclotomic_polynomials__sorted_by_(cache, degree_vs_order=False, with_degree=True, with_order=True, with_factorization4order=True, begin=48, end=56)]
[(48, 105, {7: 1, 5: 1, 3: 1}, (1, 1, 1, 0, 0, -1, -1, -2, -1, -1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, -1, -1, -2, -1, -1, 0, 0, 1, 1, 1)), (48, 210, {7: 1, 5: 1, 3: 1, 2: 1}, (1, -1, 1, 0, 0, 1, -1, 2, -1, 1, 0, 0, 1, -1, 1, -1, 1, -1, 0, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 0, -1, 1, -1, 1, -1, 1, 0, 0, 1, -1, 2, -1, 1, 0, 0, 1, -1, 1))]




view ../../python3_src/seed/math/factor_pint/factor_pint__7batch_gcd_IIdiffs.py
>>> from math import gcd
>>> from seed.math.polynomial.eval_polynomial.eval_polynomial7native import poly_eval_
>>> #def poly_eval_(add_, mul_, zero, coeffs8poly, x, /):

factor 1207
    1207: 17 71
>>> M1207 = -1+2**1207
>>> cs = cyclotomic_polynomial5order_(cache, 1207, [17, 71])
>>> args = (int.__add__, int.__mul__, 0)
>>> u = poly_eval_(*args, cs, 2)
>>> M1207%u == 0
True
>>> u * 131071 * 228479 * 48544121 * 212885833 == M1207
True


[[
>>> repr_polynomial6ZZ_8PARI_GP_([])
'0'
>>> repr_polynomial6ZZ_8PARI_GP_([1])
'1'
>>> repr_polynomial6ZZ_8PARI_GP_([2])
'2'
>>> repr_polynomial6ZZ_8PARI_GP_([-1])
'-1'
>>> repr_polynomial6ZZ_8PARI_GP_([-2])
'-2'

>>> repr_polynomial6ZZ_8PARI_GP_([1,1])
'x + 1'
>>> repr_polynomial6ZZ_8PARI_GP_([1,2])
'2*x + 1'
>>> repr_polynomial6ZZ_8PARI_GP_([1,-1])
'-x + 1'
>>> repr_polynomial6ZZ_8PARI_GP_([1,-2])
'-2*x + 1'

>>> repr_polynomial6ZZ_8PARI_GP_([0,1])
'x'
>>> repr_polynomial6ZZ_8PARI_GP_([1,1])
'x + 1'
>>> repr_polynomial6ZZ_8PARI_GP_([2,1])
'x + 2'
>>> repr_polynomial6ZZ_8PARI_GP_([-1,1])
'x - 1'
>>> repr_polynomial6ZZ_8PARI_GP_([-2,1])
'x - 2'

>>> repr_polynomial6ZZ_8PARI_GP_([1,0,1])
'x^2 + 1'
>>> repr_polynomial6ZZ_8PARI_GP_([1,1,1])
'x^2 + x + 1'
>>> repr_polynomial6ZZ_8PARI_GP_([1,2,1])
'x^2 + 2*x + 1'
>>> repr_polynomial6ZZ_8PARI_GP_([1,-1,1])
'x^2 - x + 1'
>>> repr_polynomial6ZZ_8PARI_GP_([1,-2,1])
'x^2 - 2*x + 1'





]]

[[
view others/app/termux/help/gp-example.txt
分圆多项式:
pari-gp:
? ?polcyclo
polcyclo(n,{a = 'x}): n-th cyclotomic polynomial evaluated at a.

? polcyclo(2^4*3^3*5^2*7)
%1 = x^17280 - x^16920 + x^16560 + x^15480 - x^15120 + 2*x^14760 - x^14400 + x^14040 + x^12960 - x^12600 + x^12240 - x^11880 + x^11520 - x^11160 - x^10080 - x^9360 - x^8640 - x^7920 - x^7200 - x^6120 + x^5760 - x^5400 + x^5040 - x^4680 + x^4320 + x^3240 - x^2880 + 2*x^2520 - x^2160 + x^1800 + x^720 - x^360 + 1
>>> from seed.math.polynomial.eval_polynomial.repr_polynomial8dict import exp2coeff_to_exp2nonzero_coeff_
>>> cs = cyclotomic_polynomial5order_({}, 2**4 *3**3 *5**2 *7, [2,3,5,7])
>>> exp2coeff_to_exp2nonzero_coeff_(None, cs)
{0: 1, 360: -1, 720: 1, 1800: 1, 2160: -1, 2520: 2, 2880: -1, 3240: 1, 4320: 1, 4680: -1, 5040: 1, 5400: -1, 5760: 1, 6120: -1, 7200: -1, 7920: -1, 8640: -1, 9360: -1, 10080: -1, 11160: -1, 11520: 1, 11880: -1, 12240: 1, 12600: -1, 12960: 1, 14040: 1, 14400: -1, 14760: 2, 15120: -1, 15480: 1, 16560: 1, 16920: -1, 17280: 1}
>>> repr_polynomial6ZZ_8PARI_GP_(cs)
'x^17280 - x^16920 + x^16560 + x^15480 - x^15120 + 2*x^14760 - x^14400 + x^14040 + x^12960 - x^12600 + x^12240 - x^11880 + x^11520 - x^11160 - x^10080 - x^9360 - x^8640 - x^7920 - x^7200 - x^6120 + x^5760 - x^5400 + x^5040 - x^4680 + x^4320 + x^3240 - x^2880 + 2*x^2520 - x^2160 + x^1800 + x^720 - x^360 + 1'


view ../../python3_src/seed/math/factor_pint/database4factors4cyclotomic_numbers.py.default.db
2:3:[7]
2:21:[7, 337]
2:147:[7, 2741672362528725535068727]
2:1029:[7, 6896727944023, 2714819157586383751, 3274162442129276091367, 5878920553871871291270984955318098156844648537, 401566612311195594802501193435220042560698926924429408065263999053481174119481]

? polcyclo(21)
%1 = x^12 - x^11 + x^9 - x^8 + x^6 - x^4 + x^3 - x + 1
? polcyclo(21*7)
%2 = x^84 - x^77 + x^63 - x^56 + x^42 - x^28 + x^21 - x^7 + 1
? polcyclo(21*7*7)
%3 = x^588 - x^539 + x^441 - x^392 + x^294 - x^196 + x^147 - x^49 + 1
? polcyclo(3)
%4 = x^2 + x + 1
? divrem(polcyclo(21), polcyclo(3))
%6 = [x^10 - 2*x^9 + x^8 + 2*x^7 - 4*x^6 + 2*x^5 + 3*x^4 - 5*x^3 + x^2 + 5*x - 6, 7]~
    # => [gcd==7]仅限于[x==2]
    #   3:3:[13]
    #   3:21:[368089]

>>> exp2coeff_to_exp2nonzero_coeff_(None, cs:=cyclotomic_polynomial5order_({}, 21, [3,7]))
{0: 1, 1: -1, 3: 1, 4: -1, 6: 1, 8: -1, 9: 1, 11: -1, 12: 1}
>>> repr_polynomial6ZZ_8PARI_GP_(cs)
'x^12 - x^11 + x^9 - x^8 + x^6 - x^4 + x^3 - x + 1'
>>> exp2coeff_to_exp2nonzero_coeff_(None, cs:=cyclotomic_polynomial5order_({}, 147, [3,7]))
{0: 1, 7: -1, 21: 1, 28: -1, 42: 1, 56: -1, 63: 1, 77: -1, 84: 1}
>>> repr_polynomial6ZZ_8PARI_GP_(cs)
'x^84 - x^77 + x^63 - x^56 + x^42 - x^28 + x^21 - x^7 + 1'
>>> exp2coeff_to_exp2nonzero_coeff_(None, cs:=cyclotomic_polynomial5order_({}, 1029, [3,7]))
{0: 1, 49: -1, 147: 1, 196: -1, 294: 1, 392: -1, 441: 1, 539: -1, 588: 1}
>>> repr_polynomial6ZZ_8PARI_GP_(cs)
'x^588 - x^539 + x^441 - x^392 + x^294 - x^196 + x^147 - x^49 + 1'


]]































[[
===
py_adhoc_call { +lineno }  seed.math.polynomial.eval_polynomial.cyclotomic_polynomial   ,stable_repr.20:iter_cyclotomic_polynomials__sorted_by_order_ ='{}'
1:(-1, 1)
2:(1, 1)
3:(1, 1, 1)
4:(1, 0, 1)
5:(1, 1, 1, 1, 1)
6:(1, -1, 1)
7:(1, 1, 1, 1, 1, 1, 1)
8:(1, 0, 0, 0, 1)
9:(1, 0, 0, 1, 0, 0, 1)
10:(1, -1, 1, -1, 1)
11:(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
12:(1, 0, -1, 0, 1)
13:(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
14:(1, -1, 1, -1, 1, -1, 1)
15:(1, -1, 0, 1, -1, 1, 0, -1, 1)
16:(1, 0, 0, 0, 0, 0, 0, 0, 1)
17:(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
18:(1, 0, 0, -1, 0, 0, 1)
19:(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
20:(1, 0, -1, 0, 1, 0, -1, 0, 1)
===
]]
[[
===
py_adhoc_call { +lineno }  seed.math.polynomial.eval_polynomial.cyclotomic_polynomial   ,stable_repr.20:iter_cyclotomic_polynomials__sorted_by_degree_ ='{}' +with_degree +with_order +with_factorization4order
1:(1, 1, {}, (-1, 1))
2:(1, 2, {2: 1}, (1, 1))
3:(2, 3, {3: 1}, (1, 1, 1))
4:(2, 4, {2: 2}, (1, 0, 1))
5:(2, 6, {2: 1, 3: 1}, (1, -1, 1))
6:(4, 5, {5: 1}, (1, 1, 1, 1, 1))
7:(4, 8, {2: 3}, (1, 0, 0, 0, 1))
8:(4, 10, {2: 1, 5: 1}, (1, -1, 1, -1, 1))
9:(4, 12, {2: 2, 3: 1}, (1, 0, -1, 0, 1))
10:(6, 7, {7: 1}, (1, 1, 1, 1, 1, 1, 1))
11:(6, 9, {3: 2}, (1, 0, 0, 1, 0, 0, 1))
12:(6, 14, {2: 1, 7: 1}, (1, -1, 1, -1, 1, -1, 1))
13:(6, 18, {2: 1, 3: 2}, (1, 0, 0, -1, 0, 0, 1))
14:(8, 15, {3: 1, 5: 1}, (1, -1, 0, 1, -1, 1, 0, -1, 1))
15:(8, 16, {2: 4}, (1, 0, 0, 0, 0, 0, 0, 0, 1))
16:(8, 20, {2: 2, 5: 1}, (1, 0, -1, 0, 1, 0, -1, 0, 1))
17:(8, 24, {2: 3, 3: 1}, (1, 0, 0, 0, -1, 0, 0, 0, 1))
18:(8, 30, {2: 1, 3: 1, 5: 1}, (1, 1, 0, -1, -1, -1, 0, 1, 1))
19:(10, 11, {11: 1}, (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1))
20:(10, 22, {2: 1, 11: 1}, (1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1))
===
]]
[[
===
py_adhoc_call { +lineno }  seed.math.polynomial.eval_polynomial.cyclotomic_polynomial   ,stable_repr.20:iter_exceptional_cyclotomic_polynomials__sorted_by_ ='{}' -degree_vs_order +with_degree +with_order +with_factorization4order
1:(48, 105, {3: 1, 5: 1, 7: 1}, (1, 1, 1, 0, 0, -1, -1, -2, -1, -1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, -1, -1, -2, -1, -1, 0, 0, 1, 1, 1))
2:(48, 210, {2: 1, 3: 1, 5: 1, 7: 1}, (1, -1, 1, 0, 0, 1, -1, 2, -1, 1, 0, 0, 1, -1, 1, -1, 1, -1, 0, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 0, -1, 1, -1, 1, -1, 1, 0, 0, 1, -1, 2, -1, 1, 0, 0, 1, -1, 1))
3:(80, 165, {3: 1, 5: 1, 11: 1}, (1, 1, 1, 0, 0, -1, -1, -1, 0, 0, 0, -1, -1, -1, 0, 1, 2, 2, 1, 0, -1, -1, -1, 0, 0, 0, -1, -1, -1, 0, 1, 2, 2, 2, 1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 1, 2, 2, 2, 1, 0, -1, -1, -1, 0, 0, 0, -1, -1, -1, 0, 1, 2, 2, 1, 0, -1, -1, -1, 0, 0, 0, -1, -1, -1, 0, 0, 1, 1, 1))
4:(80, 330, {2: 1, 3: 1, 5: 1, 11: 1}, (1, -1, 1, 0, 0, 1, -1, 1, 0, 0, 0, 1, -1, 1, 0, -1, 2, -2, 1, 0, -1, 1, -1, 0, 0, 0, -1, 1, -1, 0, 1, -2, 2, -2, 1, 0, -1, 1, -1, 1, -1, 1, -1, 1, -1, 0, 1, -2, 2, -2, 1, 0, -1, 1, -1, 0, 0, 0, -1, 1, -1, 0, 1, -2, 2, -1, 0, 1, -1, 1, 0, 0, 0, 1, -1, 1, 0, 0, 1, -1, 1))
5:(96, 195, {3: 1, 5: 1, 13: 1}, (1, 1, 1, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, -1, -1, 0, 1, 1, 1, 1, 0, -1, -1, 0, 0, 0, 0, 0, -1, -1, 0, 1, 1, 1, 1, 0, -1, -1, 0, 1, 1, 1, 0, -1, -2, -1, 0, 1, 1, 1, 0, -1, -2, -1, 0, 1, 1, 1, 0, -1, -1, 0, 1, 1, 1, 1, 0, -1, -1, 0, 0, 0, 0, 0, -1, -1, 0, 1, 1, 1, 1, 0, -1, -1, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 1, 1, 1))
6:(96, 390, {2: 1, 3: 1, 5: 1, 13: 1}, (1, -1, 1, 0, 0, 1, -1, 1, 0, 0, 0, 0, 0, 1, -1, 0, 1, -1, 1, -1, 0, 1, -1, 0, 0, 0, 0, 0, -1, 1, 0, -1, 1, -1, 1, 0, -1, 1, 0, -1, 1, -1, 0, 1, -2, 1, 0, -1, 1, -1, 0, 1, -2, 1, 0, -1, 1, -1, 0, 1, -1, 0, 1, -1, 1, -1, 0, 1, -1, 0, 0, 0, 0, 0, -1, 1, 0, -1, 1, -1, 1, 0, -1, 1, 0, 0, 0, 0, 0, 1, -1, 1, 0, 0, 1, -1, 1))
7:(96, 420, {2: 2, 3: 1, 5: 1, 7: 1}, (1, 0, -1, 0, 1, 0, 0, 0, 0, 0, 1, 0, -1, 0, 2, 0, -1, 0, 1, 0, 0, 0, 0, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, 0, 0, 0, 0, 1, 0, -1, 0, 2, 0, -1, 0, 1, 0, 0, 0, 0, 0, 1, 0, -1, 0, 1))
8:(128, 255, {3: 1, 5: 1, 17: 1}, (1, 1, 1, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, -1, -1, -1, -1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, -1, -1, -1, -1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, -1, -1, -1, 0, 1, 2, 1, 0, -1, -1, -1, 0, 1, 1, 0, -1, -1, -1, 0, 1, 1, 0, -1, -1, -1, 0, 1, 2, 1, 0, -1, -1, -1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, -1, -1, -1, -1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, -1, -1, -1, -1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 1, 1, 1))
9:(128, 510, {2: 1, 3: 1, 5: 1, 17: 1}, (1, -1, 1, 0, 0, 1, -1, 1, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, -1, 1, -1, 1, 0, -1, 1, 0, 0, 0, 0, 0, 1, -1, 0, 1, -1, 1, -1, 0, 1, -1, 0, 0, 0, 0, 0, -1, 1, 0, -1, 1, -1, 0, 1, -2, 1, 0, -1, 1, -1, 0, 1, -1, 0, 1, -1, 1, 0, -1, 1, 0, -1, 1, -1, 0, 1, -2, 1, 0, -1, 1, -1, 0, 1, -1, 0, 0, 0, 0, 0, -1, 1, 0, -1, 1, -1, 1, 0, -1, 1, 0, 0, 0, 0, 0, 1, -1, 0, 1, -1, 1, -1, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 1, -1, 1, 0, 0, 1, -1, 1))
10:(144, 273, {3: 1, 7: 1, 13: 1}, (1, 1, 1, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 1, 2, 2, 1, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, -1, -1, -1, 0, 0, 1, 1, 2, 2, 2, 1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 1, 2, 2, 2, 2, 2, 1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 1, 2, 2, 2, 2, 2, 1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 1, 2, 2, 2, 1, 1, 0, 0, -1, -1, -1, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 1, 2, 2, 1, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 1, 1, 1))
11:(144, 285, {3: 1, 5: 1, 19: 1}, (1, 1, 1, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, -1, -2, -2, -1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, -1, -2, -2, -1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, -1, -2, -2, -1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, -1, -2, -2, -2, -1, 0, 1, 1, 1, 1, 1, 1, 1, 0, -1, -2, -2, -2, -1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, -1, -2, -2, -1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, -1, -2, -2, -1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, -1, -2, -2, -1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 1, 1, 1))
12:(144, 315, {3: 2, 5: 1, 7: 1}, (1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, -1, 0, 0, -2, 0, 0, -1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, -1, 0, 0, -2, 0, 0, -1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1))
13:(144, 546, {2: 1, 3: 1, 7: 1, 13: 1}, (1, -1, 1, 0, 0, 0, 0, 1, -1, 1, 0, 0, 0, 1, -1, 1, 0, 0, 0, 0, 1, -2, 2, -1, 0, 0, 0, 0, -1, 1, -1, 0, 0, 0, -1, 1, -1, 0, 0, -1, 1, -2, 2, -2, 1, 0, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 0, -1, 2, -2, 2, -2, 2, -1, 0, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 0, -1, 2, -2, 2, -2, 2, -1, 0, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 0, 1, -2, 2, -2, 1, -1, 0, 0, -1, 1, -1, 0, 0, 0, -1, 1, -1, 0, 0, 0, 0, -1, 2, -2, 1, 0, 0, 0, 0, 1, -1, 1, 0, 0, 0, 1, -1, 1, 0, 0, 0, 0, 1, -1, 1))
14:(144, 570, {2: 1, 3: 1, 5: 1, 19: 1}, (1, -1, 1, 0, 0, 1, -1, 1, 0, 0, 0, 0, 0, 0, 0, -1, 1, -1, 0, 1, -2, 2, -1, 0, 1, -1, 1, 0, 0, 0, 1, -1, 1, 0, -1, 2, -2, 1, 0, -1, 1, -1, 0, 0, 0, -1, 1, -1, 0, 1, -2, 2, -1, 0, 1, -1, 1, -1, 1, -1, 1, -1, 0, 1, -2, 2, -2, 1, 0, -1, 1, -1, 1, -1, 1, -1, 0, 1, -2, 2, -2, 1, 0, -1, 1, -1, 1, -1, 1, -1, 1, 0, -1, 2, -2, 1, 0, -1, 1, -1, 0, 0, 0, -1, 1, -1, 0, 1, -2, 2, -1, 0, 1, -1, 1, 0, 0, 0, 1, -1, 1, 0, -1, 2, -2, 1, 0, -1, 1, -1, 0, 0, 0, 0, 0, 0, 0, 1, -1, 1, 0, 0, 1, -1, 1))
15:(144, 630, {2: 1, 3: 2, 5: 1, 7: 1}, (1, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, 0, 2, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, 0, 1, 0, 0, -1, 0, 0, 1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, -1, 0, 0, 1, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, 0, 2, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, 0, 1))
16:(160, 660, {2: 2, 3: 1, 5: 1, 11: 1}, (1, 0, -1, 0, 1, 0, 0, 0, 0, 0, 1, 0, -1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, -1, 0, 1, 0, 0, 0, -1, 0, 2, 0, -2, 0, 1, 0, 0, 0, -1, 0, 1, 0, -1, 0, 0, 0, 0, 0, 0, 0, -1, 0, 1, 0, -1, 0, 0, 0, 1, 0, -2, 0, 2, 0, -2, 0, 1, 0, 0, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 0, 0, 1, 0, -2, 0, 2, 0, -2, 0, 1, 0, 0, 0, -1, 0, 1, 0, -1, 0, 0, 0, 0, 0, 0, 0, -1, 0, 1, 0, -1, 0, 0, 0, 1, 0, -2, 0, 2, 0, -1, 0, 0, 0, 1, 0, -1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, -1, 0, 1, 0, 0, 0, 0, 0, 1, 0, -1, 0, 1))
17:(176, 345, {3: 1, 5: 1, 23: 1}, (1, 1, 1, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, -1, -1, -1, -1, -1, -1, 0, 0, 1, 1, 2, 1, 1, 0, 0, -1, -1, -1, -1, -1, -1, 0, 0, 1, 1, 2, 1, 1, 0, 0, -1, -1, -1, -1, -1, -1, 0, 0, 1, 1, 2, 1, 1, 0, 0, -1, -1, -1, -1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, -1, -1, -1, -1, 0, 0, 1, 0, 1, 0, 1, 0, 0, -1, -1, -1, -1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, -1, -1, -1, -1, 0, 0, 1, 1, 2, 1, 1, 0, 0, -1, -1, -1, -1, -1, -1, 0, 0, 1, 1, 2, 1, 1, 0, 0, -1, -1, -1, -1, -1, -1, 0, 0, 1, 1, 2, 1, 1, 0, 0, -1, -1, -1, -1, -1, -1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 1, 1, 1))
18:(176, 690, {2: 1, 3: 1, 5: 1, 23: 1}, (1, -1, 1, 0, 0, 1, -1, 1, 0, 0, 0, 0, 0, 0, 0, -1, 1, -1, 0, 0, -1, 1, -1, 1, -1, 1, 0, 0, 1, -1, 2, -1, 1, 0, 0, 1, -1, 1, -1, 1, -1, 0, 0, -1, 1, -2, 1, -1, 0, 0, -1, 1, -1, 1, -1, 1, 0, 0, 1, -1, 2, -1, 1, 0, 0, 1, -1, 1, -1, 0, 0, -1, 0, -1, 0, -1, 0, -1, 0, 0, -1, 1, -1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, -1, 1, -1, 0, 0, -1, 0, -1, 0, -1, 0, -1, 0, 0, -1, 1, -1, 1, 0, 0, 1, -1, 2, -1, 1, 0, 0, 1, -1, 1, -1, 1, -1, 0, 0, -1, 1, -2, 1, -1, 0, 0, -1, 1, -1, 1, -1, 1, 0, 0, 1, -1, 2, -1, 1, 0, 0, 1, -1, 1, -1, 1, -1, 0, 0, -1, 1, -1, 0, 0, 0, 0, 0, 0, 0, 1, -1, 1, 0, 0, 1, -1, 1))
19:(192, 357, {3: 1, 7: 1, 17: 1}, (1, 1, 1, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, 0, 1, 1, 1, 1, 1, 1, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, 0, 1, 1, 1, 1, 1, 1, 0, -1, -1, 0, 1, 1, 0, 0, 0, 0, -1, -2, -2, -1, 0, 1, 1, 1, 1, 1, 0, -1, -2, -1, 0, 1, 1, 1, 1, 1, 0, -1, -2, -2, -1, 0, 1, 1, 1, 1, 1, 0, -1, -2, -1, 0, 1, 1, 1, 1, 1, 0, -1, -2, -1, 0, 1, 1, 1, 1, 1, 0, -1, -2, -2, -1, 0, 1, 1, 1, 1, 1, 0, -1, -2, -1, 0, 1, 1, 1, 1, 1, 0, -1, -2, -2, -1, 0, 0, 0, 0, 1, 1, 0, -1, -1, 0, 1, 1, 1, 1, 1, 1, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, 0, 1, 1, 1, 1, 1, 1, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 1, 1, 1))
20:(192, 714, {2: 1, 3: 1, 7: 1, 17: 1}, (1, -1, 1, 0, 0, 0, 0, 1, -1, 1, 0, 0, 0, 0, 0, 0, 0, 1, -1, 1, 0, -1, 1, -1, 1, -1, 1, 0, -1, 1, -1, 0, 0, 0, 0, 0, 0, 0, -1, 1, -1, 0, 1, -1, 1, -1, 1, -1, 0, 1, -1, 0, 1, -1, 0, 0, 0, 0, -1, 2, -2, 1, 0, -1, 1, -1, 1, -1, 0, 1, -2, 1, 0, -1, 1, -1, 1, -1, 0, 1, -2, 2, -1, 0, 1, -1, 1, -1, 1, 0, -1, 2, -1, 0, 1, -1, 1, -1, 1, 0, -1, 2, -1, 0, 1, -1, 1, -1, 1, 0, -1, 2, -2, 1, 0, -1, 1, -1, 1, -1, 0, 1, -2, 1, 0, -1, 1, -1, 1, -1, 0, 1, -2, 2, -1, 0, 0, 0, 0, -1, 1, 0, -1, 1, 0, -1, 1, -1, 1, -1, 1, 0, -1, 1, -1, 0, 0, 0, 0, 0, 0, 0, -1, 1, -1, 0, 1, -1, 1, -1, 1, -1, 0, 1, -1, 1, 0, 0, 0, 0, 0, 0, 0, 1, -1, 1, 0, 0, 0, 0, 1, -1, 1))
===
]]
[[
===
py_adhoc_call { +lineno }  seed.math.polynomial.eval_polynomial.cyclotomic_polynomial   ,stable_repr.20:iter_cyclotomic_polynomials__sorted_by_ ='{}' -degree_vs_order +with_degree +with_order +with_factorization4order +squarefree_order_only
1:(1, 1, {}, (-1, 1))
2:(1, 2, {2: 1}, (1, 1))
3:(2, 3, {3: 1}, (1, 1, 1))
4:(2, 6, {2: 1, 3: 1}, (1, -1, 1))
5:(4, 5, {5: 1}, (1, 1, 1, 1, 1))
6:(4, 10, {2: 1, 5: 1}, (1, -1, 1, -1, 1))
7:(6, 7, {7: 1}, (1, 1, 1, 1, 1, 1, 1))
8:(6, 14, {2: 1, 7: 1}, (1, -1, 1, -1, 1, -1, 1))
9:(8, 15, {3: 1, 5: 1}, (1, -1, 0, 1, -1, 1, 0, -1, 1))
10:(8, 30, {2: 1, 3: 1, 5: 1}, (1, 1, 0, -1, -1, -1, 0, 1, 1))
11:(10, 11, {11: 1}, (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1))
12:(10, 22, {2: 1, 11: 1}, (1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1))
13:(12, 13, {13: 1}, (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1))
14:(12, 21, {3: 1, 7: 1}, (1, -1, 0, 1, -1, 0, 1, 0, -1, 1, 0, -1, 1))
15:(12, 26, {2: 1, 13: 1}, (1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1))
16:(12, 42, {2: 1, 3: 1, 7: 1}, (1, 1, 0, -1, -1, 0, 1, 0, -1, -1, 0, 1, 1))
17:(16, 17, {17: 1}, (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1))
18:(16, 34, {2: 1, 17: 1}, (1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1))
19:(18, 19, {19: 1}, (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1))
20:(18, 38, {2: 1, 19: 1}, (1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1))
===
py_adhoc_call { +lineno }  seed.math.polynomial.eval_polynomial.cyclotomic_polynomial   ,stable_repr.20:iter_cyclotomic_polynomials__sorted_by_ ='{}' -degree_vs_order +with_degree +with_order +with_factorization4order -squarefree_order_only
1:(1, 1, {}, (-1, 1))
2:(1, 2, {2: 1}, (1, 1))
3:(2, 3, {3: 1}, (1, 1, 1))
4:(2, 4, {2: 2}, (1, 0, 1))
5:(2, 6, {2: 1, 3: 1}, (1, -1, 1))
6:(4, 5, {5: 1}, (1, 1, 1, 1, 1))
7:(4, 8, {2: 3}, (1, 0, 0, 0, 1))
8:(4, 10, {2: 1, 5: 1}, (1, -1, 1, -1, 1))
9:(4, 12, {2: 2, 3: 1}, (1, 0, -1, 0, 1))
10:(6, 7, {7: 1}, (1, 1, 1, 1, 1, 1, 1))
11:(6, 9, {3: 2}, (1, 0, 0, 1, 0, 0, 1))
12:(6, 14, {2: 1, 7: 1}, (1, -1, 1, -1, 1, -1, 1))
13:(6, 18, {2: 1, 3: 2}, (1, 0, 0, -1, 0, 0, 1))
14:(8, 15, {3: 1, 5: 1}, (1, -1, 0, 1, -1, 1, 0, -1, 1))
15:(8, 16, {2: 4}, (1, 0, 0, 0, 0, 0, 0, 0, 1))
16:(8, 20, {2: 2, 5: 1}, (1, 0, -1, 0, 1, 0, -1, 0, 1))
17:(8, 24, {2: 3, 3: 1}, (1, 0, 0, 0, -1, 0, 0, 0, 1))
18:(8, 30, {2: 1, 3: 1, 5: 1}, (1, 1, 0, -1, -1, -1, 0, 1, 1))
19:(10, 11, {11: 1}, (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1))
20:(10, 22, {2: 1, 11: 1}, (1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1))
===
PARI-GP:
? polcyclo(4,'p)
p^2 + 1
? polcyclo(3,'p)
p^2 + p + 1
? polcyclo(6,'p)
p^2 - p + 1
? polcyclo(5,'p)
p^4 + p^3 + p^2 + p + 1
? polcyclo(12,'p)
p^4 - p^2 + 1
? polcyclo(9,'p)
p^6 + p^3 + 1
? polcyclo(8,'p)
p^4 + 1
? polcyclo(10,'p)
p^4 - p^3 + p^2 - p + 1
===

]]
[[
===
py_adhoc_call { +lineno }  seed.math.polynomial.eval_polynomial.cyclotomic_polynomial   ,stable_repr.4:iter_exceptional_cyclotomic_polynomials__sorted_by_ ='{}' -degree_vs_order +with_degree +with_order +with_factorization4order +squarefree_order_only --begin=96
1:(96, 195, {3: 1, 5: 1, 13: 1}, (1, 1, 1, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, -1, -1, 0, 1, 1, 1, 1, 0, -1, -1, 0, 0, 0, 0, 0, -1, -1, 0, 1, 1, 1, 1, 0, -1, -1, 0, 1, 1, 1, 0, -1, -2, -1, 0, 1, 1, 1, 0, -1, -2, -1, 0, 1, 1, 1, 0, -1, -1, 0, 1, 1, 1, 1, 0, -1, -1, 0, 0, 0, 0, 0, -1, -1, 0, 1, 1, 1, 1, 0, -1, -1, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 1, 1, 1))
2:(96, 390, {2: 1, 3: 1, 5: 1, 13: 1}, (1, -1, 1, 0, 0, 1, -1, 1, 0, 0, 0, 0, 0, 1, -1, 0, 1, -1, 1, -1, 0, 1, -1, 0, 0, 0, 0, 0, -1, 1, 0, -1, 1, -1, 1, 0, -1, 1, 0, -1, 1, -1, 0, 1, -2, 1, 0, -1, 1, -1, 0, 1, -2, 1, 0, -1, 1, -1, 0, 1, -1, 0, 1, -1, 1, -1, 0, 1, -1, 0, 0, 0, 0, 0, -1, 1, 0, -1, 1, -1, 1, 0, -1, 1, 0, 0, 0, 0, 0, 1, -1, 1, 0, 0, 1, -1, 1))
3:(128, 255, {3: 1, 5: 1, 17: 1}, (1, 1, 1, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, -1, -1, -1, -1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, -1, -1, -1, -1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, -1, -1, -1, 0, 1, 2, 1, 0, -1, -1, -1, 0, 1, 1, 0, -1, -1, -1, 0, 1, 1, 0, -1, -1, -1, 0, 1, 2, 1, 0, -1, -1, -1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, -1, -1, -1, -1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, -1, -1, -1, -1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 1, 1, 1))
4:(128, 510, {2: 1, 3: 1, 5: 1, 17: 1}, (1, -1, 1, 0, 0, 1, -1, 1, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, -1, 1, -1, 1, 0, -1, 1, 0, 0, 0, 0, 0, 1, -1, 0, 1, -1, 1, -1, 0, 1, -1, 0, 0, 0, 0, 0, -1, 1, 0, -1, 1, -1, 0, 1, -2, 1, 0, -1, 1, -1, 0, 1, -1, 0, 1, -1, 1, 0, -1, 1, 0, -1, 1, -1, 0, 1, -2, 1, 0, -1, 1, -1, 0, 1, -1, 0, 0, 0, 0, 0, -1, 1, 0, -1, 1, -1, 1, 0, -1, 1, 0, 0, 0, 0, 0, 1, -1, 0, 1, -1, 1, -1, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 1, -1, 1, 0, 0, 1, -1, 1))

===
]]

py_adhoc_call   seed.math.polynomial.eval_polynomial.cyclotomic_polynomial   @cyclotomic_polynomial5order_
]]]'''#'''
__all__ = r'''
cyclotomic_polynomial5order_
iter_exceptional_cyclotomic_polynomials__sorted_by_
    iter_cyclotomic_polynomials__sorted_by_
        iter_cyclotomic_polynomials__sorted_by_degree_
        iter_cyclotomic_polynomials__sorted_by_order_


repr_polynomial6ZZ_8PARI_GP_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.check import check_type_is, check_int_ge
    from seed.algo.FFT.convolution import mk_ops4convolution7symbolic_FFT__5modulus_
    from seed.math.prepare_p2e4N import prepare_p2e4N_
    #def prepare_p2e4N_(N, may_p2e4N_or_ps4N_or_factor_pint_func, /):
    #from seed.math.II import II__ft2e_
    from seed.iters.flatten_recur import flatten_recur
    # def flatten_recur(g:Generator, /, *, value:object=None, is_exc=False, boxed=False):
    #
    from seed.iters.find import find_if
    from seed.math.polynomial.eval_polynomial.divmod7polynomial import perfect_div7polynomial_, add7polynomial_
    from seed.math.prime_sieve.sieve_ge_le import iter_sieve4prime_factorizations_ge_lt_
    from seed.math.valence_of_Euler_function import list_inv_phi_
    from seed.debug.print_err import print_err
    from seed.math.polynomial.eval_polynomial.repr_polynomial8dict import exp2coeff_to_exp2nonzero_coeff_

#.#################################
___end_mark_of_excluded_global_names__0___ = ...

def repr_polynomial6ZZ_8PARI_GP_(cs, /, *, str8op4pow='^', nm8var='x'):
    eq_zero_ = None
    def __():
        j2c = exp2coeff_to_exp2nonzero_coeff_(eq_zero_, cs)
        if not j2c:
            yield '0'
            return
        j_c_pairs = sorted(j2c.items(), reverse=True)
        b_fst = True
        for j, c in j_c_pairs:
            sign = '-+'[c > 0]
            u = abs(c)
            if u == 1:
                s4u = ''
            else:
                s4u = str(u)
            s4u
            if j == 0:
                s4xs = ''
            elif j == 1:
                s4xs = nm8var
            else:
                s4xs = f'{nm8var}{str8op4pow}{j}'
            s4xs
            match (s4u, s4xs):
                case ('', ''):
                    s4uxs = '1'
                case ('', _):
                    s4uxs = s4xs
                case (_, ''):
                    s4uxs = s4u
                case _:
                    s4uxs = f'{s4u}*{s4xs}'
            s4uxs
            if not b_fst:
                yield sign
                yield s4uxs
            else:
                b_fst = False
                if sign == '-':
                    yield sign+s4uxs
                else:
                    yield s4uxs
    return ' '.join(__())


if 0:
    _0_opsN = ...
def _gmk_opsX():
    global _0_opsN
    try:
        return _0_opsN
    except NameError:
        pass
    _0_opsN = mk_ops4convolution7symbolic_FFT__5modulus_(modulus:=0)
    return _gmk_opsX()
def iter_exceptional_cyclotomic_polynomials__sorted_by_(cache, /, *, degree_vs_order, with_degree=False, with_order=False, with_factorization4order=False, **kwds):
    _mk_output_ = _mk__mk_output_(with_degree, with_order, with_factorization4order)
    it = iter_cyclotomic_polynomials__sorted_by_(cache, degree_vs_order=degree_vs_order, with_degree=True, with_order=True, with_factorization4order=True, **kwds)
    for (degree, N, p2e4N, cs) in it:
        if max(map(abs, cs)) > 1:
            yield _mk_output_(N, p2e4N, cs)
def iter_cyclotomic_polynomials__sorted_by_(cache, /, *, degree_vs_order, **kwds):
    f = iter_cyclotomic_polynomials__sorted_by_degree_ if not degree_vs_order else iter_cyclotomic_polynomials__sorted_by_order_
    return f(cache, **kwds)
def _is_squarefree(N, p2e4N, /):
    return max(p2e4N.values(), default=1) == 1
def _is_ok7True(N, p2e4N, /):
    return True
def _mk__is_ok(squarefree_order_only, /):
    _is_ok_ = _is_squarefree if squarefree_order_only else _is_ok7True
    return _is_ok_
def iter_cyclotomic_polynomials__sorted_by_degree_(cache, /, *, with_degree=False, with_order=False, with_factorization4order=False, squarefree_order_only=False, begin=1, end=None):
    check_int_ge(1, begin)
    _mk_output_ = _mk__mk_output_(with_degree, with_order, with_factorization4order)
    _is_ok_ = _mk__is_ok(squarefree_order_only)

    it = iter_sieve4prime_factorizations_ge_lt_(begin, end, with_uint=True)
    for (output4phi, p2e4output4phi) in it:
        # [N == order == input4phi]
        # [degree == output4phi]
        inputs4phi = list_inv_phi_(p2e4output4phi, output4phi, to_sort=True, with_factorization=True)
        #for (input4phi, p2e4input4phi) in inputs4phi:
        for (N, p2e4N) in inputs4phi:
            if not _is_ok_(N, p2e4N):continue
            cs = cyclotomic_polynomial5order_(cache, N, p2e4N)
            #yield cs if not with_order else (N, cs)
            yield _mk_output_(N, p2e4N, cs)
def _mk__mk_output_(with_degree, with_order, with_factorization4order):
    if not any([with_order, with_degree, with_factorization4order]):
        def _mk_output_(N, p2e4N, cs):
            return cs
    else:
        def _mk_output_(N, p2e4N, cs):
            rs = []
            if with_degree:
                rs.append(-1+len(cs))
            if with_order:
                rs.append(N)
            if with_factorization4order:
                rs.append(p2e4N)
            rs.append(cs)
            rs = tuple(rs)
            return rs
    return _mk_output_

def iter_cyclotomic_polynomials__sorted_by_order_(cache, /, *, with_degree=False, with_order=False, with_factorization4order=False, squarefree_order_only=False, begin=1, end=None):
    check_int_ge(1, begin)
    _mk_output_ = _mk__mk_output_(with_degree, with_order, with_factorization4order)
    _is_ok_ = _mk__is_ok(squarefree_order_only)
    it = iter_sieve4prime_factorizations_ge_lt_(begin, end, with_uint=True)
    for (N, p2e4N) in it:
        if not _is_ok_(N, p2e4N):continue
        cs = cyclotomic_polynomial5order_(cache, N, p2e4N)
        #yield cs if not with_order else (N, cs)
        yield _mk_output_(N, p2e4N, cs)
def cyclotomic_polynomial5order_(cache, N, may_p2e4N_or_ps4N_or_factor_pint_func, /):
    '-> coeffs{cyclotomic_polynomial{order:=N}}/[int] # [(1-X**N)%poly{coeffs;X} == 0] #order:mul_order_of(independent_variable{X})'
    try:
        return cache[N]
    except KeyError:
        pass
    check_int_ge(1, N)
    p2e4N = prepare_p2e4N_(N, may_p2e4N_or_ps4N_or_factor_pint_func)

    pe_pairs4N = sorted(p2e4N.items(), key=lambda t:t[::-1])
    imay_j = find_if(pe_pairs4N, lambda t:t[1] > 1)
    j = len(pe_pairs4N) if imay_j < 0 else imay_j
    _0_opsN = _gmk_opsX()
    return flatten_recur(_0_cyclotomic_polynomial5order_(_0_opsN, cache, N, pe_pairs4N, j))
def _0_cyclotomic_polynomial5order_(_0_opsN, cache, N, pe_pairs4N, j, /):
    try:
        return cache[N]
    except KeyError:
        pass
    cs = yield _1_cyclotomic_polynomial5order_(_0_opsN, cache, N, pe_pairs4N, j)
    cs = tuple(cs)
    cache[N] = cs
    return cyclotomic_polynomial5order_(cache, N, None)
def _1_cyclotomic_polynomial5order_(_0_opsN, cache, N, pe_pairs4N, j, /):
    for j in range(len(pe_pairs4N)):
        (p, ep) = pe_pairs4N[j]
        if ep > 1:
            break
    else:
        #squarefree
        pe_pairs4N.sort()
        cs = yield _2_cyclotomic_polynomial5order_(_0_opsN, cache, N, pe_pairs4N)
        return cs
    pw = p**(ep-1)
    777;pe_pairs4N[j] = (p, 1)
    777;N //= pw
    777;j += 1
    _cs = yield _0_cyclotomic_polynomial5order_(_0_opsN, cache, N, pe_pairs4N, j)
    cs = _substitute7pow_(pw, _cs)
    return cs
def _substitute7pow_(pw, _cs, /):
    # [PHI(p*m;x) == PHI(m;x**p)]
    deg = (len(_cs)-1)*pw
    cs = [0]*(1+deg)
    for j, c in enumerate(_cs):
        cs[j*pw] = c
    return cs

def _2_cyclotomic_polynomial5order_(_0_opsN, cache, N, pe_pairs4N, /):
    #squarefree
    match pe_pairs4N:
        case []:
            # [N==1] => (X-1)
            return [-1, 1]
        case [(p, 1)]:
            # [PHI(p;x) == (x**p - 1)/(x-1)]
            return [1]*p
    (p, _1) = pe_pairs4N.pop()
    777; N //= p
    assert _1 == 1
    _cs = yield _0_cyclotomic_polynomial5order_(_0_opsN, cache, N, pe_pairs4N, len(pe_pairs4N))
    # [PHI(p*m;x) == PHI(m;x**p)/PHI(m;x)]
    cs8N = _substitute7pow_(p, _cs)
    cs8D = _cs
    return perfect_div7polynomial_(_0_opsN, cs8N, cs8D)


def _mul_order4var77polynomial7native_(cs, /, *, expected=0):
    assert len(cs) >= 2
    assert cs[-1] == 1
    cs8back = [-c for c in cs[:-1]]
    # [len(cs8back) >= 1]
    _0_opsN = _gmk_opsX()
    cs8pow = [1] # updated inplace
    cs8one = [1]
    def mul_var_(cs8pow, /):
        cs8pow.insert(0, 0)
        cs8pow = std_(cs8pow)
        return cs8pow
    def std_(cs8pow, /):
        # [len(cs8pow) <= len(cs)]
        if not len(cs8pow) < len(cs):
            # [len(cs8pow) == len(cs)]
            LC = cs8pow.pop()
            cs8pow = add7polynomial_(_0_opsN, cs8pow, [LC*c for c in cs8back])
            assert cs8pow[-1]
            # [len(cs8pow) < len(cs)]
        # [len(cs8pow) < len(cs)]
        assert len(cs8pow) < len(cs)
        #while cs8pow and 0 == cs8pow[-1]: cs8pow.pop()
        assert cs8pow[-1]
        return cs8pow
    order = 0
    while 1:
        #print_err(order, cs8pow)
        cs8pow = mul_var_(cs8pow)
        777;order += 1
        if cs8pow == cs8one:
            break
        if order == expected:
            raise Exception('fail:', order, cs8pow)
    return order




__all__
from seed.math.polynomial.eval_polynomial.cyclotomic_polynomial import cyclotomic_polynomial5order_
#def cyclotomic_polynomial5order_(cache, N, may_p2e4N_or_ps4N_or_factor_pint_func, /):

from seed.math.polynomial.eval_polynomial.cyclotomic_polynomial import iter_exceptional_cyclotomic_polynomials__sorted_by_

from seed.math.polynomial.eval_polynomial.cyclotomic_polynomial import iter_cyclotomic_polynomials__sorted_by_, iter_cyclotomic_polynomials__sorted_by_degree_, iter_cyclotomic_polynomials__sorted_by_order_

from seed.math.polynomial.eval_polynomial.cyclotomic_polynomial import *
