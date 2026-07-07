#__all__:goto
#_debugging_:goto
#buggy!!!!!!!
#slow????????
r'''[[[
e ../../python3_src/seed/math/factor_pint/perfect_power/detect_perfect_power__7lift_precision.py

seed.math.factor_pint.perfect_power.detect_perfect_power__7lift_precision
py -m nn_ns.app.debug_cmd   seed.math.factor_pint.perfect_power.detect_perfect_power__7lift_precision -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.factor_pint.perfect_power.detect_perfect_power__7lift_precision:__doc__ -ht # -ff -df
#######

[[
see:
    '/sdcard/0my_files/book/math/factorint/snd/Detecting perfect powers in essentially linear time(1998)(Berstein).pdf'
]]



'#'; __doc__ = r'#'
>>> factor_pint_as_perfect_power_(244)
(244, 1)
>>> #   fail!!(3, 5) not (244, 1)  <<== bug@detect_perfect_kth_root_()
>>> factor_pint_as_perfect_power_(1)
Traceback (most recent call last):
    ...
TypeError: 1
>>> factor_pint_as_perfect_power_(2)
(2, 1)
>>> factor_pint_as_perfect_power_(4)
(2, 2)
>>> #   fail!!(4, 1) not (2, 2)  <<== bug@trunc4pf_()
>>> factor_pint_as_perfect_power_(8)
(2, 3)
>>> factor_pint_as_perfect_power_(2**4)
(2, 4)
>>> factor_pint_as_perfect_power_(2**5)
(2, 5)
>>> factor_pint_as_perfect_power_(2**6)
(2, 6)
>>> factor_pint_as_perfect_power_(9)
(3, 2)
>>> factor_pint_as_perfect_power_(3**3)
(3, 3)
>>> factor_pint_as_perfect_power_(3**4)
(3, 4)
>>> factor_pint_as_perfect_power_(3**5)
(3, 5)
>>> factor_pint_as_perfect_power_(3**6)
(3, 6)
>>> factor_pint_as_perfect_power_((-1+2**67)**2)
(147573952589676412927, 2)
>>> factor_pint_as_perfect_power_((-1+2**67)**3)
(147573952589676412927, 3)
>>> factor_pint_as_perfect_power_((-1+2**67)**4)
(147573952589676412927, 4)
>>> factor_pint_as_perfect_power_((-1+2**67)**5)
(147573952589676412927, 5)




>>> std4pf_(-3, 7)
(-3, 7)
>>> std4pf_(-3, 14)
(-2, 7)
>>> fraction5pf_((-2, 3))
Fraction(3, 4)
>>> fraction5pf_((0, 3))
Fraction(3, 1)
>>> fraction5pf_((2, 3))
Fraction(12, 1)


>>> pfs = [(ez,odd) for ez in [0, 4, -5] for odd in range(1,11,2)]


>>> for pf in pfs:
...     print(pf, ceil_log2__4pf_(pf), sep=':')
(0, 1):0
(0, 3):2
(0, 5):3
(0, 7):3
(0, 9):4
(4, 1):4
(4, 3):6
(4, 5):7
(4, 7):7
(4, 9):8
(-5, 1):-5
(-5, 3):-3
(-5, 5):-2
(-5, 7):-2
(-5, 9):-1



>>> for pf in pfs:
...     print(pf, num_bits4pf_(pf), sep=':')
(0, 1):1
(0, 3):2
(0, 5):3
(0, 7):3
(0, 9):4
(4, 1):1
(4, 3):2
(4, 5):3
(4, 7):3
(4, 9):4
(-5, 1):1
(-5, 3):2
(-5, 5):3
(-5, 7):3
(-5, 9):4



>>> bs = range(1,5)
>>> for b in bs:
...     for pf in pfs:
...         print(b, pf, trunc4pf_(b, pf), sep=':')
1:(0, 1):(0, 1)
1:(0, 3):(1, 1)
1:(0, 5):(2, 1)
1:(0, 7):(2, 1)
1:(0, 9):(3, 1)
1:(4, 1):(4, 1)
1:(4, 3):(5, 1)
1:(4, 5):(6, 1)
1:(4, 7):(6, 1)
1:(4, 9):(7, 1)
1:(-5, 1):(-5, 1)
1:(-5, 3):(-4, 1)
1:(-5, 5):(-3, 1)
1:(-5, 7):(-3, 1)
1:(-5, 9):(-2, 1)
2:(0, 1):(0, 1)
2:(0, 3):(0, 3)
2:(0, 5):(2, 1)
2:(0, 7):(1, 3)
2:(0, 9):(3, 1)
2:(4, 1):(4, 1)
2:(4, 3):(4, 3)
2:(4, 5):(6, 1)
2:(4, 7):(5, 3)
2:(4, 9):(7, 1)
2:(-5, 1):(-5, 1)
2:(-5, 3):(-5, 3)
2:(-5, 5):(-3, 1)
2:(-5, 7):(-4, 3)
2:(-5, 9):(-2, 1)
3:(0, 1):(0, 1)
3:(0, 3):(0, 3)
3:(0, 5):(0, 5)
3:(0, 7):(0, 7)
3:(0, 9):(3, 1)
3:(4, 1):(4, 1)
3:(4, 3):(4, 3)
3:(4, 5):(4, 5)
3:(4, 7):(4, 7)
3:(4, 9):(7, 1)
3:(-5, 1):(-5, 1)
3:(-5, 3):(-5, 3)
3:(-5, 5):(-5, 5)
3:(-5, 7):(-5, 7)
3:(-5, 9):(-2, 1)
4:(0, 1):(0, 1)
4:(0, 3):(0, 3)
4:(0, 5):(0, 5)
4:(0, 7):(0, 7)
4:(0, 9):(0, 9)
4:(4, 1):(4, 1)
4:(4, 3):(4, 3)
4:(4, 5):(4, 5)
4:(4, 7):(4, 7)
4:(4, 9):(4, 9)
4:(-5, 1):(-5, 1)
4:(-5, 3):(-5, 3)
4:(-5, 5):(-5, 5)
4:(-5, 7):(-5, 7)
4:(-5, 9):(-5, 9)




>>> from math import floor
>>> from seed.math.sign_of import sign_of

fraction5pf_
mul4pf_
add4pf_
unsafe_sub4pf_
lt4pf_
>>> for lhs in pfs:
...     for rhs in pfs:
...         r = mul4pf_(lhs, rhs)
...         assert fraction5pf_(r) == fraction5pf_(lhs)*fraction5pf_(rhs)


>>> for lhs in pfs:
...     for rhs in pfs:
...         r = add4pf_(lhs, rhs)
...         assert fraction5pf_(r) == fraction5pf_(lhs)+fraction5pf_(rhs)


>>> for lhs in pfs:
...     for rhs in pfs:
...         fr = fraction5pf_(lhs) -fraction5pf_(rhs)
...         if not fr > 0:continue
...         r = unsafe_sub4pf_(lhs, rhs)
...         assert fraction5pf_(r) == fr

>>> for lhs in pfs:
...     for rhs in pfs:
...         r = lt4pf_(lhs, rhs)
...         assert r is (fraction5pf_(lhs) < fraction5pf_(rhs))


step4pf_
rshift4pf_k_
lshift4pint_
>>> for b in bs:
...     for rhs in pfs:
...         r = step4pf_(b, rhs)
...         assert fraction5pf_(r) == (1+Fraction(2)**-b)*fraction5pf_(rhs)


>>> for k in range(-5,+6):
...     for lhs in pfs:
...         r = rshift4pf_k_(lhs, k)
...         assert fraction5pf_(r) == (Fraction(2)**-k)*fraction5pf_(lhs)


>>> for k in range(-5,+6):
...     for u in range(1, 20):
...         r = lshift4pint_(u, k)
...         assert r == floor(Fraction(2)**k *u)





div4pf_k_
pow4pf_k_
    cmp_pow4pint_

[1 <= (r/k) / div4pf_k_(b;r,k) < (1+2**(1-b))]
>>> for b in range(1,9):
...   for lhs in pfs:
...     for k in range(1,99):
...         r = div4pf_k_(b, lhs, k)
...         assert  1 <= fraction5pf_(lhs)/k / fraction5pf_(r) < (1+Fraction(2)**(1-b))


[1 <= (r**k) / pow4pf_k_(b;r,k) < (1+2**(1-b))**(-1+2*k)]
>>> for b in range(1,9):
...   for lhs in pfs:
...     for k in range(1,19):
...         r = pow4pf_k_(b, lhs, k)
...         assert  1 <= fraction5pf_(lhs)**k / fraction5pf_(r) < (1+Fraction(2)**(1-b))**(-1+2*k)



>>> for n in range(1,999):
...   for x in range(1, 33):
...     for k in range(1,19):
...         r = cmp_pow4pint_(n, x, k)
...         assert r == sign_of(n - x**k)
















[[
{ +to_show_total_timedelta }
{ +to_show_timedelta }
py_adhoc_call  { +to_show_timedelta } seed.math.factor_pint.perfect_power.detect_perfect_power__7lift_precision   ,_iter_run_lt__to_seperate_setup_time_  +validate --repeat=1 ='1+2**16'
    #bug-fixed:^Exception: (244, {2: 2, 61: 1}, 1, (3, 5))
    1:duration: 34.985080014 *(unit: 0:00:01)
        这是由于未曾优化:试除->成则锁定少量指数，败则降低指数上限

py_adhoc_call  { +to_show_timedelta } seed.math.factor_pint.perfect_power.detect_perfect_power__7lift_precision   ,_iter_run_lt__to_seperate_setup_time_  -validate --repeat=1 ='1+2**16'
]]

py_adhoc_call   seed.math.factor_pint.perfect_power.detect_perfect_power__7lift_precision   @f

]]]'''#'''
__all__ = r'''
std4pf_
fraction5pf_

ceil_log2__4pf_
num_bits4pf_
trunc4pf_

mul4pf_
add4pf_
unsafe_sub4pf_
lt4pf_

step4pf_
rshift4pf_k_
lshift4pint_

div4pf_k_
pow4pf_k_
    cmp_pow4pint_

nroot4pf_k_
detect_perfect_kth_root_
    find_arbitrary_uint_ex__nearby_le_5over8_
factor_pint_as_perfect_power_
    detect_perfect_power_
        is_perfect_power_

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.math.max_power_of_base_as_factor_of_ import factor_pint_out_power_of_base_
    from seed.math.prime_sieve.sieve_lt import list_primes__lt_
    from seed.math.floor_ceil_tools.fc_log import floor_log2, ceil_log2
    from seed.tiny_.check import check_type_is, check_int_ge
    from fractions import Fraction
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

r'''[[[
[[[[[[[[[
see:
    '/sdcard/0my_files/book/math/factorint/snd/Detecting perfect powers in essentially linear time(1998)(Berstein).pdf'

[[[
===
[TIME{factor_pint_as_perfect_power_(N)} == log2(N) * exp(O(sqrt(lnlnN*lnlnlnN)))]

[factor_pint_as_perfect_power_ :: perfect-power classification algorithm] # max exp
[factor_pint_as_perfect_power_{arbitrary_exp_ok:=True} :: perfect-power decomposition algorithm]
[is_perfect_power_ :: perfect-power dedetection algorithm]

[b-bit number == uint%2**b]
[time4mul__le_zpow_(b) := TIME{__mul__{uint%2**b}}]
[max_ratio4time4mul__le_zpow_(b) := max[time4mul__le_zpow_(_b)/_b | [b:<-[1..=b]]]]
[time4mul__le_zpow_(b)/b <= max_ratio4time4mul__le_zpow_(b)]
[time4mul__le_zpow_(b) <= b*max_ratio4time4mul__le_zpow_(b)]

fast.__mul__ => [time4mul__le_zpow_(B) == O(B*lnB*lnlnB)][max_ratio4time4mul__le_zpow_(B) == O(lnB*lnlnB)]
slow.__mul__ => [time4mul__le_zpow_(B) == O(B**2)][max_ratio4time4mul__le_zpow_(B) == O(B)]

[pf{ez,odd} :: positive floating-point number:2**ez*odd]
    (ez, odd)
    [ez::int][odd:uint{%2==1}]

[num_bits4pf_(pf{ez,odd}) := odd.bit_length()]
[num_bits4pf_(pf{ez,odd}) == 1+floor_log2(odd)]
[2**(-1+num_bits4pf_(pf)) <= pf.odd < 2**num_bits4pf_(pf)]
[2**(-1+pf.ez+num_bits4pf_(pf)) <= pf < 2**(pf.ez+num_bits4pf_(pf))]

[b :: uint{>0}]
truncation to b bits
[trunc4pf_(b;pf) := div4pf_k_(b;pf,1)]
[num_bits4pf_(trunc4pf_(b;pf)) == min(b,num_bits4pf_(pf))]
[2**(-1+pf.ez+num_bits4pf_(pf)) <= trunc4pf_(b;pf) <= pf < trunc4pf_(b;pf) +2**(-b+pf.ez+num_bits4pf_(pf))]
!! [2**(-1+pf.ez+num_bits4pf_(pf)) <= trunc4pf_(b;pf)]
[2**(-b+pf.ez+num_bits4pf_(pf)) <= 2**(1-b)*trunc4pf_(b;pf)]
[2**(-1+pf.ez+num_bits4pf_(pf)) <= trunc4pf_(b;pf) <= pf < trunc4pf_(b;pf) +2**(-b+pf.ez+num_bits4pf_(pf)) <= trunc4pf_(b;pf)*(1+2**(1-b))]
[trunc4pf_(b;pf) <= pf < trunc4pf_(b;pf)*(1+2**(1-b))]
[1 <= pf/trunc4pf_(b;pf) < (1+2**(1-b))]
[0 <= -1+pf/trunc4pf_(b;pf) < 2**(1-b)]
[0 <= 2**b*(-1+pf/trunc4pf_(b;pf)) < 2]


[k :: uint{>0}]
[div4pf_k_(b;r,k) ~= (r/k)]
    approximation
[div4pf_k_(b;r,k) := (r.ez-pad, (r.odd<<pad) //k)]
    where:
        [nb4r := num_bits4pf_(r)]
        [ce4k := ceil_log2(k)]
        [pad := (b+ce4k-nb4r)]
    NOTE:MAYBE[pad < 0]
    [(r.odd<<pad) >>pad <= r.odd]
    [(r.odd<<pad) <= r.odd*2**pad]
[1 <= (r/k) / div4pf_k_(b;r,k) < (1+2**(1-b))]
    [[proof:
    [div4pf_k_(b;r,k) == 2**(r.ez-pad) *((r.odd<<pad) //k)]

    [s := div4pf_k_(b;r,k)]
    [m := ((r.odd<<pad) //k)]
    [m <= ((r.odd<<pad) /k) < 1+m]
    [k*m <= (r.odd<<pad) <= (k-1)+k*m]
    !! [div4pf_k_(b;r,k) == 2**(r.ez-pad) *((r.odd<<pad) //k)]
    [s == div4pf_k_(b;r,k) == 2**(r.ez-pad) *((r.odd<<pad) //k) == m*2**(r.ez-pad)]
    [s == m*2**(r.ez-pad)]

    [m
    == ((r.odd<<pad) //k)
    !! [2**(-1+nb4r) <= r.odd < 2**nb4r]
    >= ((2**(-1+nb4r)<<pad) //k)
    == ((2**(-1+nb4r)*2**pad) //k)
        # 纯二幂位移:pad正负无关
    == (2**(-1+nb4r+pad) //k)
    !! [pad := (b+ce4k-nb4r)]
    == (2**(-1+b+ce4k) //k)
    == ((2**(-1+b)*2**ce4k) //k)
    >= 2**(-1+b)  *((2**ce4k) //k)
    !! [2**(-1+ce4k) < k <= 2**ce4k]
    >= 2**(-1+b)
    ]
    [m >= 2**(-1+b)]


    * [pad < 0]:
        [(r.odd<<pad) == (r.odd//2**-pad)]
        !! [(r.odd//2**-pad) <= (r.odd/2**-pad) < 1+(r.odd//2**-pad)]
        [-1+(r.odd/2**-pad) < (r.odd//2**-pad) <= (r.odd/2**-pad)]
        [-2**-pad+(r.odd) < 2**-pad*(r.odd//2**-pad) <= (r.odd)]
        [1-2**-pad+(r.odd) <= 2**-pad*(r.odd//2**-pad) <= (r.odd)]
        [(1-2**-pad+r.odd) <= 2**-pad*(r.odd<<pad) <= (r.odd)]

        !! [k*m <= (r.odd<<pad) <= (k-1)+k*m]
        [2**-pad*k*m <= 2**-pad*(r.odd<<pad) <= 2**-pad*((k-1)+k*m)]
        !! [(1-2**-pad+r.odd) <= 2**-pad*(r.odd<<pad) <= (r.odd)]
        [2**-pad*k*m <= 2**-pad*(r.odd<<pad) <= (r.odd)]  [(1-2**-pad+r.odd) <= 2**-pad*(r.odd<<pad) <= 2**-pad*((k-1)+k*m)]
        [2**-pad*k*m <= (r.odd)]  [(1-2**-pad+r.odd) <= 2**-pad*((k-1)+k*m)]
        [2**-pad*k*m <= (r.odd) <= -(1-2**-pad) +2**-pad*((k-1)+k*m)]
        [2**-pad*k*m <= (r.odd) <= -1 +2**-pad*k*(1+m)]
        [2**-pad*m <= (r.odd)/k < 2**-pad*(1+m)]
    * [pad >= 0]:
        [(r.odd<<pad) == (r.odd*2**pad)]
        !! [m <= ((r.odd<<pad) /k) < 1+m]
        [m <= ((r.odd*2**pad) /k) < 1+m]
        [2**-pad*m <= (r.odd)/k < 2**-pad*(1+m)]
    ==>>:
    [2**-pad*m <= (r.odd)/k < 2**-pad*(1+m)]
    # 『(2**r.ez*)』
    [2**r.ez*2**-pad*m <= (2**r.ez*r.odd)/k < 2**r.ez*2**-pad*(1+m)]
    [2**(r.ez-pad)*m <= r/k < 2**(r.ez-pad)*m*(1+1/m)]
    !! [s == m*2**(r.ez-pad)]
    [s <= r/k < s*(1+1/m)]
    !! [m >= 2**(-1+b)]
    [1/m <= 2**(1-b)]
    [s <= r/k < s*(1+1/m) <= s*(1+2**(1-b))]
    [s <= r/k < s*(1+2**(1-b))]
    [1 <= (r/k) / s < (1+2**(1-b))]
    !! [s := div4pf_k_(b;r,k)]
    [1 <= (r/k) / div4pf_k_(b;r,k) < (1+2**(1-b))]
    DONE
    ]]
[k:=1]:
    [1 <= (r/1) / div4pf_k_(b;r,1) < (1+2**(1-b))]
    [1 <= r/trunc4pf_(b;r) < (1+2**(1-b))]

[pow4pf_k_(b;r,k) ~= r**k]
    the b-bit approximate kth power of r
[TIME{pow4pf_k_(b;r,k)} <= 2*floor_log2(k)*time4mul__le_zpow_(b)]


[pow4pf_k_(b;r,1) := trunc4pf_(b;r)]
[pow4pf_k_(b;r,1+2*k) := trunc4pf_(b;mul4pf_(trunc4pf_(b;r), pow4pf_k_(b;r,2*k)))]
[pow4pf_k_(b;r,2*k) := trunc4pf_(b;mul4pf_(pow4pf_k_(b;r,k), pow4pf_k_(b;r,k)))]

[1 <= (r**k) / pow4pf_k_(b;r,k) < (1+2**(1-b))**(-1+2*k)]
    [[proof:
    [k > 0]
    * [k==1]:
        !! [1 <= r/trunc4pf_(b;r) < (1+2**(1-b))]
        ok
    * [k==i+j][1<=i<=j<k][1 <= (r**i) / pow4pf_k_(b;r,i) < (1+2**(1-b))**(-1+2*i)][1 <= (r**j) / pow4pf_k_(b;r,j) < (1+2**(1-b))**(-1+2*j)]:
        #任意拆分都行
        [1 <= (r**k) / (pow4pf_k_(b;r,i)*pow4pf_k_(b;r,j)) < (1+2**(1-b))**(-2+2*k)]
        !! [1 <= r/trunc4pf_(b;r) < (1+2**(1-b))]
        [1 <= (pow4pf_k_(b;r,i)*pow4pf_k_(b;r,j))/trunc4pf_(b;(pow4pf_k_(b;r,i)*pow4pf_k_(b;r,j))) < (1+2**(1-b))]
        [1 <= (r**k) / trunc4pf_(b;(2*j)) < (1+2**(1-b))**(-1+2*k)]
        ok
    DONE
    ]]

===
]]]
[[[
===
approximate roots
    root extraction: y**/k
    inversion:y**-1
统一形式:y**/-k
    因为其牛顿迭代的形式最简单，只用 加法+乘法+除法{固定整数分母}
    [h(z) := -1 + 1/(y*z**k)]
    [new_z := z -h(z)/Dh(z)]
    [new_z == z -(-1 + 1/(y*z**k))/(1/y * -k * z**-(1+k))]
    [new_z == z -(-y*z**(1+k) + z)/(-k)]
    [new_z == z +(z -y*z**(1+k))/k]
    [new_z == (z*(1+k) -y*z**(1+k))/k]
        # update6Newton_method:here
[k==a*b]:
    [y**/k == (y**/-a)**/-b]

[y**/k == (y**/-1)**/-k]
[y**/k == y*(y**/-k)**(k-1)]
    !! [y**/k == y**(1-(k-1)/k)]

[nroot_(b;r,k) ~= r**/-k]
    a binary search for small b
        # 实现:(z**k*r-1)粗略估计以选 左半、右半，但模糊 则 中间一半
        意图:至少得保证 牛顿迭代 不出现 负数{数据仅:正浮点数} 即 [0 < (z*(1+k) -y*z**(1+k))]
    , and then Newton’s method with increasing precision for all larger b.
[(1-2**-b) < (r**/-k) / nroot_(b;r,k) < (1+2**-b)]
[abs(1 - (r**/-k) / nroot_(b;r,k)) < (2**-b)]

[32/33 < 993/1024 < e**/-33]
[32/33 < float(993*2**-10) < e**/-33]
===
]]]
[[[
===

7.  Some overly specific inequalities 
Lemma__7_1
[@[exp,err::real] -> [exp>0] -> [0 < err < 1] -> [(1+err/4/exp)**(2*exp) < (1+err)]]
    #[@[exp,err::real] -> [exp>0] -> [0 < err < 1/2] -> [(1+err/exp)**exp < (1+2*err)]]
Lemma__7_2
[@[exp::real] -> [exp>=1] -> [7/8 <= (1-1/8/exp)**exp]]
Lemma__7_3
[@[t::real] -> [0 < t < 1/36] -> [(1+3*t)*(1+t)*(1+(32/3)*t) < (1+16*t)]]
Lemma__7_4
[@[t,exp::real] -> [exp>=1] -> [0 < t < 1/4/(1+exp)] -> [(1+t)**(3+2*exp) < 1+(16*t)*(-2+7*exp)/9]]

=======
Lemma__7_1
[@[x,c::real] -> [x>0] -> [0 < c < 1] -> [(1+c/(2*x))**x < (1+c)]]
    # 统一形式牜上界:goto
Lemma__7_2
[@[x,c::real] -> [x>=1] -> [0 < c < 1] -> [(1-c/x)**x >= (1-c)]]
    # 统一形式牜下界:here




=======
辅助公式牜一:here
[@[k,c::real][k >= 1][c > -1/k] -> [(1+c)**k >= 1+c*k]]
    [[proof:
    [(1+c)**k >= 1+c*k]:
        <==> [k*ln(1+c) >= ln(1+c*k)]
    [f(c) := k*ln(1+c) - ln(1+c*k)]
    [Df(c) == k/(1+c) - k/(1+c*k)]
    [Df(c) < 0]:
        <==> [k/(1+c) < k/(1+c*k)]
        !! [k >= 1]
        <==> [1/(1+c) < 1/(1+c*k)]
        !! [k >= 1][c > -1/k]
        => [1+c*k > 0][c > -1]
        <==> [(1+c) > (1+c*k)]
        <==> [0 > (-1+k)*c]
    [k==1]:
        [f(c) == 0]
        [f(c) >= 0]
    [k > 1]:
        [Df(c) < 0]:
            <==> [0 > (-1+k)*c]
            !! [k > 1]
            <==> [c < 0]
        [f(c) >= f(0) == 0]
        [f(c) >= 0]
    [f(c) >= 0]
    [(1+c)**k >= 1+c*k]
    DONE
    ]]


=======
Lemma__7_1
[@[exp,err::real] -> [exp>0] -> [0 < err < 1] -> [(1+err/4/exp)**(2*exp) < (1+err)]]
<==>:
# exp --> x
# err --> c
[@[x,c::real] -> [x>0] -> [0 < c < 1] -> [(1+c/4/x)**(2*x) < (1+c)]]
<==>:
[@[x,c::real] -> [x>0] -> [0 < c < 1] -> [(2*x)*ln(1+c/4/x) < ln(1+c)]]
<==>:
 x --> 1/x
[@[x,c::real] -> [1/x > 0] -> [0 < c < 1] -> [(2*1/x)*ln(1+(c/4)*x) < ln(1+c)]]
<==>:
[@[x,c::real] -> [x > 0] -> [0 < c < 1] -> [2*ln(1+(c/4)*x) < x*ln(1+c)]]
    [[proof:
    [f(x) := 2*ln(1+(c/4)*x) - x*ln(1+c)]
    [Df(x)
    == (c/4)*2/(1+(c/4)*x) - ln(1+c)
    == (2*c)/(4+c*x) - ln(1+c)
    ]
    [Df(x) < 0]:
        <==> [(2*c)/(4+c*x) < ln(1+c)]
        !! [x > 0]
        !! [0 < c < 1]
        => [c*x > 0][ln(1+c) > 0]
        <==> [(2*c)/ln(1+c) < (4+c*x)]
        <==> [x > (-4+2*c/ln(1+c))/c]
    [(-4+2*c/ln(1+c)) >= 0]:
        <==> [c >= 2*ln(1+c)]
        !! [0 < c < 1]
        ==>> [1 >= 2*ln(1+1)]
        ==>> [1 >= ln(4)]
        ==>> [e >= 4]
        ==>> _L
    [(-4+2*c/ln(1+c)) < 0]
    [Df(x) < 0]:
        <==> [x > (-4+2*c/ln(1+c))/c]
        !! [x > 0]
        !! [0 < c < 1]
        !! [(-4+2*c/ln(1+c)) < 0]
        <==> [x > 0]
    [Df(x) < 0]
    [f(x) > f(+oo) == -oo]
    [f(x) < f(0) == 2*ln(1+(c/4)*0) - 0*ln(1+c) == 0]
    [f(x) < 0]
    [2*ln(1+(c/4)*x) < x*ln(1+c)]
    DONE

    ]]
[@[x,c::real] -> [x>0] -> [0 < c < 1] -> [(1+c/4/x)**(2*x) < (1+c)]]
# c --> c/u
# x --> v*x
[@[x,c,u,v::real] -> [v*x,u,v>0] -> [0 < c/u < 1] -> [(1+c/u/4/v/x)**(2*v*x) < (1+c/u)]]
[@[x,c,u,v::real] -> [x,u,v>0] -> [0 < c < u] -> [(1+c/(4*u*v*x))**(2*v*x) < (1+c/u)]]
# x --> x/2
[@[x,c,u,v::real] -> [x,u,v>0] -> [0 < c < u] -> [(1+c/(2*u*v*x))**(v*x) < (1+c/u)]]
# v --> 1
[@[x,c,u::real] -> [x,u>0] -> [0 < c < u] -> [(1+c/(2*u*x))**x < (1+c/u)]]
# u --> 1
[@[x,c::real] -> [x>0] -> [0 < c < 1] -> [(1+c/(2*x))**x < (1+c)]]
    # 统一形式牜上界:here

=======
Lemma__7_2
[@[exp::real] -> [exp>=1] -> [7/8 <= (1-1/8/exp)**exp]]
    # [L:=7]
<<==:
[@[L > 0] -> [B:=(1+L)] -> @[exp::real] -> [exp>=1] -> [L/B <= (1-1/B/exp)**exp]]
<==>:
# exp --> c
[@[L > 0] -> [B:=(1+L)] -> @[c::real] -> [c>=1] -> [L/B <= (1-1/B/c)**c]]
<==>:
# ln()
[@[L > 0] -> [B:=(1+L)] -> @[c::real] -> [c>=1] -> [ln(L/B) <= c*ln(1-1/B/c)]]
<==>:
# (/c)
[@[L > 0] -> [B:=(1+L)] -> @[c::real] -> [c>=1] -> [ln(L/B)/c <= ln(1-1/B/c)]]
<==>:
# c --> 1/x
[@[L > 0] -> [B:=(1+L)] -> @[x::real] -> [1/x>=1] -> [ln(L/B)*x <= ln(1-1/B*x)]]
[@[L > 0] -> [B:=(1+L)] -> @[x::real] -> [0 < x <= 1] -> [x*ln(L/B) <= ln(1-x/B)]]
    [[proof:
    !! [@[x::real] -> [not [-1 <= L <= 0]] -> [B:=1+L] -> [1/B < ln(B/L) < 1/L]] # bounds4ln_BoverL:goto
    [1/B < ln(B/L) < 1/L]
    [-1/B > ln(L/B) > -1/L]

    [f(x) := x*ln(L/B) -ln(1-x/B)]
    [Df(x)
    == ln(L/B) -1/(1-x/B) * -1/B
    == ln(L/B) +1/B/(1-x/B)
    == ln(L/B) +1/(B-x)
        # > ln(L/B) +1/B
        # <= ln(L/B) +1/L
        # !! [-1/B > ln(L/B) > -1/L]
        # [ln(L/B) +1/B < 0 < ln(L/B) +1/L]
    ]
    [Df(x) < 0]:
        <==> [-ln(L/B) > 1/(B-x)]
        <==> [ln(B/L) > 1/(B-x)]
        !! [0 < x <= 1]
        !! [B > 1]
        => [0 < B-x]
        <==> [(B-x) > 1/ln(B/L)]
        <==> [x < B -1/ln(B/L)]
    [f(x) >= f(B -1/ln(B/L))]
    [f(x) <= max(f(0^{+}),f(1))]
    [f(1) == 1*ln(L/B) -ln(1-1/B) == 0]
    [f(0) == 0*ln(L/B) -ln(1-0/B) == 0]
    [f(x) <= max(f(0^{+}),f(1)) == 0]
    [f(x) <= 0]
    [x*ln(L/B) <= ln(1-x/B)]
    DONE
    ]]
[@[L > 0] -> [B:=(1+L)] -> @[x::real] -> [0 < x <= 1] -> [x*ln(L/B) <= ln(1-x/B)]]
    [c:=L/B]
    [c == L/(1+L)]
    !! [L > 0]
    [0 < c < 1]
    [c*(1+L) == L]
    [c == L*(1-c)]
    [L == c/(1-c)]
    [B == 1+L == 1/(1-c)]
    [L/B == c]
[@[c :: real] -> [0 < c < 1] -> @[x::real] -> [0 < x <= 1] -> [x*ln(c) <= ln(1-x*(1-c))]]
# c --> 1-c
[@[c :: real] -> [0 < c < 1] -> @[x::real] -> [0 < x <= 1] -> [x*ln(1-c) <= ln(1-x*c)]]
# x --> 1/x
[@[c :: real] -> [0 < c < 1] -> @[x::real] -> [0 < 1/x <= 1] -> [1/x*ln(1-c) <= ln(1-1/x*c)]]
[@[c :: real] -> [0 < c < 1] -> @[x::real] -> [x >= 1] -> [ln(1-c) <= x*ln(1-c/x)]]
[@[c :: real] -> [0 < c < 1] -> @[x::real] -> [x >= 1] -> [(1-c) <= (1-c/x)**x]]

统一形式:上下限:
[@[x,c::real] -> [x>=1] -> [0 < c < 1] -> [(1-c/x)**x >= (1-c)]]
    # 统一形式牜下界:here
[@[x,c::real] -> [x>0] -> [0 < c < 1] -> [(1+c/(2*x))**x < (1+c)]]
    # 统一形式牜上界:goto

=======
辅助:
[@[x::real] -> [x > -1] -> [x =!= 0] -> [ln(1 + x) < x]]
    # [ln(1+x) == x/1 -x**2/2 +x**3/3 ... + x**k *(-1)**(k-1)/k +...]
    [[proof:
    [g(x) := ln(1 + x) - x]
    [Dg(x) == 1/(1+x) -1 == -x/(1+x)]
    [x > 0]:
        [Dg(x) < 0]
    [-1 < x < 0]:
        [Dg(x) > 0]
    [x > -1][x =!= 0]:
        [g(x) < g(0) == 0]
        [g(x) < 0]
        [ln(1 + x) < x]
    [[x > -1] -> [x =!= 0] -> [ln(1 + x) < x]]
    DONE
    ]]
<==>:
# x --> 1/x
[@[x::real] -> [not [-1 <= x <= 0]] -> [ln(1 + 1/x) < 1/x]]
[@[x::real] -> [not [-1 <= x <= 0]] -> [ln((x+1)/x) < 1/x]]
# x --> x-1
[@[x::real] -> [not [-1 <= x-1 <= 0]] -> [ln(x/(x-1)) < 1/(x-1)]]
[@[x::real] -> [not [0 <= x <= 1]] -> [-ln(x/(x-1)) > -1/(x-1)]]
[@[x::real] -> [not [0 <= x <= 1]] -> [ln((x-1)/x) > 1/(1-x)]]
[@[x::real] -> [not [0 <= x <= 1]] -> [1/(1-x) < ln(1-1/x)]]
# x --> -x
[@[x::real] -> [not [0 <= -x <= 1]] -> [1/(1+x) < ln(1+1/x)]]
[@[x::real] -> [not [-1 <= x <= 0]] -> [1/(1+x) < ln(1 + 1/x)]]
!! [@[x::real] -> [not [-1 <= x <= 0]] -> [ln(1 + 1/x) < 1/x]]
[@[x::real] -> [not [-1 <= x <= 0]] -> [1/(1+x) < ln(1 + 1/x) < 1/x]]
[@[x::real] -> [not [-1 <= x <= 0]] -> [1/(1+x) < ln((1+x)/x) < 1/x]]
    对称型
[@[x::real] -> [not [-1 <= L <= 0]] -> [B:=1+L] -> [1/B < ln(B/L) < 1/L]]
    [:bounds4ln_BoverL]:here
# x --> 1/x
[@[x::real] -> [not [-1 <= 1/x <= 0]] -> [1/(1+1/x) < ln(1+x) < x]]
[@[x::real] -> [x > -1] -> [x =!= 0] -> [x/(1+x) < ln(1+x) < x]]
[@[x::real] -> [x > -1] -> [x =!= 0] -> [1-1/(1+x) < ln(1+x) < x]]
    增量型
# x --> 1/7
[1-1/(1+1/7) < ln(1+1/7) < 1/7]
[1-1/(8/7) < ln(8/7) < 1/7]
[1-7/8 < ln(8/7) < 1/7]
[1/8 < ln(8/7) < 1/7]
    [:bounds4ln_8over7]:here

=======
Lemma__7_3
[@[t::real] -> [0 < t < 1/36] -> [(1+3*t)*(1+t)*(1+(32/3)*t) < (1+16*t)]]
    复变函数，零点，上界？
    算了，记不起来，蛮力证明:
<==>:
# t --> 1/t
[@[t::real] -> [0 < 1/t < 1/36] -> [(1+3/t)*(1+1/t)*(1+(32/3)/t) < (1+16/t)]]
[@[t::real] -> [t > 36] -> [(t+3)*(t+1)*(t+(32/3)) < t**2*(t+16)]]
    [[proof:
    [(t**2+4*t+3)*(t+(32/3)) < t**3+16*t**2]
    [(t**3+4*t**2+3*t)+((32/3)*t**2+(32/3)*4*t+(32/3)*3) < t**3+16*t**2]
    [3*t+(32/3)*4*t+32 < 4/3*t**2]
    [137*t+96 < 4*t**2]
    [4*t**2 -137*t -96 > 0]
    [137**2 +4*4*96 == 20305]
    [sqrt(20305) ~= 142.5]
    [(137 -sqrt(20305)) /8 ~= -0.7 < 36]
    [(137 +sqrt(20305)) /8 ~= 35.0 < 36]
    DONE
    ]]


=======
Lemma__7_4
[@[t,exp::real] -> [exp>=1] -> [0 < t < 1/4/(1+exp)] -> [(1+t)**(3+2*exp) < 1+(16*t)*(-2+7*exp)/9]]
# exp --> c
[@[t,c::real] -> [c>=1] -> [0 < t < 1/4/(1+c)] -> [(1+t)**(3+2*c) < 1+(16*t)*(-2+7*c)/9]]
[@[t,c::real] -> [c>=1] -> [0 < t < 1/4/(1+c)] -> [(1+t)**(3+2*c) < 1+(16*t)*(-1+7*(1+c)/9)]]
# c --> (c-1)
[@[t,c::real] -> [c>=2] -> [0 < t < 1/4/c] -> [(1+t)**(1+2*c) < 1+(16*t)*(-1+7*c/9)]]
# c --> ((c-1)/2)
[@[t,c::real] -> [((c-1)/2)>=2] -> [0 < t < 1/4/((c-1)/2)] -> [(1+t)**(1+2*((c-1)/2)) < 1+(16*t)*(-1+7*((c-1)/2)/9)]]
[@[t,c::real] -> [c>=5] -> [0 < t < 1/2/(c-1)] -> [18*(1+t)**c < 18+(16*t)*(-25+7*c)]]



# exp --> x
[@[t,x::real] -> [x>=1] -> [0 < t < 1/4/(1+x)] -> [(1+t)**(3+2*x) < 1+(16*t)*(-2+7*x)/9]]
# t --> (c/4/(1+x))
[@[c,x::real] -> [x>=1] -> [0 < c < 1] -> [(1+(c/4/(1+x)))**(3+2*x) < 1+(16*(c/4/(1+x)))*(-2+7*x)/9]]
# x --> ((x-3)/2)
[@[c,x::real] -> [((x-3)/2)>=1] -> [0 < c < 1] -> [(1+(c/4/(1+((x-3)/2))))**(3+2*((x-3)/2)) < 1+(16*(c/4/(1+((x-3)/2))))*(-2+7*((x-3)/2))/9]]
[@[c,x::real] -> [x>=5] -> [0 < c < 1] -> [(1+c/2/(x-1))**x < 1+(4/9)*c*(7*x-25)/(x-1)]]
[@[c,x::real] -> [x>=5] -> [0 < c < 1] -> [(1+c/2/(x-1))**x < 1+(4/9)*c*(7-18/(x-1))]]
[@[c,x::real] -> [x>=5] -> [0 < c < 1] -> [(1+c/2/(x-1))**x < 1+(28/9)*c -8*c/(x-1)]]
[@[c,x::real] -> [x>=5] -> [0 < c < 1] -> [(1+c/2/(x-1))**(x-1) *((x-1)+c/2) < (1+(28/9)*c)*(x-1) -8*c]]
# x --> (x+1)
[@[c,x::real] -> [x>=4] -> [0 < c < 1] -> [(1+c/2/x)**x *(x+c/2) < (1+(28/9)*c)*x -8*c]]
[@[c,x::real] -> [x>=4] -> [0 < c < 1] -> [(1+c/2/x)**x *(x+c/2)*9 < (9+28*c)*x -72*c]]
# c --> c*x
[@[c,x::real] -> [x>=4] -> [0 < c*x < 1] -> [(1+c*x/2/x)**x *(x+c*x/2)*9 < (9+28*c*x)*x -72*c*x]]
[@[c,x::real] -> [x>=4] -> [0 < c < 1/x] -> [(1+c/2)**x *(1+c/2)*9 < (9+28*c*x) -72*c]]
[@[c,x::real] -> [x>=4] -> [0 < c < 1/x] -> [x*ln(1+c/2) +ln(1+c/2) +ln9 < ln(9+28*c*x -72*c)]]

#rollback:『c --> c*x』
[@[c,x::real] -> [x>=4] -> [0 < c < 1] -> [(1+c/2/x)**x *(x+c/2)*9 < (9+28*c)*x -72*c]]
[@[c,x::real] -> [x>=4] -> [0 < c < 1] -> [(1+c/2/x)**x < (9+28*c)/9*(x -72*c/(9+28*c))/(x+c/2)]]
[@[c,x::real] -> [x>=4] -> [0 < c < 1] -> [x*ln(1+c/2/x) < ln(9+28*c) -ln9 +ln(x -72*c/(9+28*c)) -ln(x+c/2)]]
    [[proof:
    [f(x) := x*ln(1+c/2/x) - (ln(9+28*c) -ln9 +ln(x -72*c/(9+28*c)) -ln(x+c/2))]
    [Df(x)
    == ln(1+c/2/x) +x/(1+c/2/x) *(c/2) *-1/x**2 -1/(x -72*c/(9+28*c)) +1/(x+c/2)
    == ln(1+c/2/x) +(1-c/2)/(x+c/2) -1/(x -72*c/(9+28*c))
    ]

    !! [x>=4]
    !! [0 < c < 1]
    [(9+28*c) > 9 > 0]
    [((9+28*c)*x -72*c) >= ((9+28*c)*4 -72*c) == (36+40*c) > 36 > 0]
    [((9+28*c)*x -72*c) > 0]
    [x > 72*c/(9+28*c)]

    [ln(1+c/2/x) < ln(1+1/2/4) == ln(9/8)]
    [ln(1+c/2/x) > ln(1+0/2/+oo) == 0]
    [0 < ln(1+c/2/x) < ln(9/8) ~= 0.118]

    [(1-c/2)/(x+c/2) < (1-0/2)/(4+0/2) == 1/4]
    [(1-c/2)/(x+c/2) > (1-1/2)/(+oo+1/2) == 0]
    [0 < (1-c/2)/(x+c/2) < 1/4 == 0.25]

    [(x -72*c/(9+28*c)) < +oo]
    [(x -72*c/(9+28*c))
    == (x -(18/7)*c/(c+9/28))
    == (x + (-(18/7)*(c+9/28) +(18/7)*(9/28))/(c+9/28))
    == (x -(18/7) +(81/98)/(c+9/28))
    > (4 -(18/7) +(81/98)/(1+9/28))
    == (4 -72*1/(9+28*1))
    == (4 -72/37)
    == (76/37)
    ~= 2.054
    ]
    [2.054 ~= (76/37) < (x -72*c/(9+28*c)) < +oo]
    [0 < 1/(x -72*c/(9+28*c)) < (37/76) ~= 0.487]

    [Df(x) < 0]:
        <==> [ln(1+c/2/x) +(1-c/2)/(x+c/2) < 1/(x -72*c/(9+28*c))]

    [DDf(x)
    == -(c/2)/x/(x+c/2) -(1-c/2)/(x+c/2)**2 +1/(x -72*c/(9+28*c))**2
    ]
    [DDf(x) < 0]:
        <==> [1/(x -72*c/(9+28*c))**2 < (c/2)/x/(x+c/2) +(1-c/2)/(x+c/2)**2]
        <==> [x*(x+c/2)**2 < ((c/2)*(x+c/2) +(1-c/2)*x)*(x -72*c/(9+28*c))**2]
        <==> [x*(x+c/2)**2 < (x +c**2/4)*(x -72*c/(9+28*c))**2]
        <==> [x*(x**2 +c*x +c**2/4) < (x +c**2/4)*(x**2 -2*x*(72*c/(9+28*c)) +(72*c/(9+28*c))**2)]
        <==> [(x**3 +c*x**2 +x*c**2/4) < (x**3 -2*x**2*(72*c/(9+28*c)) +x*(72*c/(9+28*c))**2) +(c**2/4)*(x**2 -2*x*(72*c/(9+28*c)) +(72*c/(9+28*c))**2)]
        <==> [(c +2*(72*c/(9+28*c)) -(c**2/4))*x**2 +x*(c**2/4 -(72*c/(9+28*c))**2 +2*(c**2/4)*(72*c/(9+28*c))) - (c**2/4)*((72*c/(9+28*c))**2) < 0]
        <==> [(1 +2*(72/(9+28*c)) -(c/4))*x**2 +x*(c/4 -c*(72/(9+28*c))**2 +2*(c/4)*(72*c/(9+28*c))) - (c/4)*((72*c/(9+28*c))**2) < 0]
        <==> [(1/c +2*(72/c/(9+28*c)) -(1/4))*x**2 +x*(1/4 -(72/(9+28*c))**2 +2*(1/4)*(72*c/(9+28*c))) - (1/4)*((72*c/(9+28*c))**2) < 0]
        <==> [(1/c +2*(72/c/(9+28*c)) -(1/4))*x**2 +x*(1/4/(72*c/(9+28*c)) -(72/c/(9+28*c)) +(1/2))*(72*c/(9+28*c)) - (1/4)*((72*c/(9+28*c))**2) < 0]
        <==> [(1/c +2*(72/c/(9+28*c)) -(1/4))/(72*c/(9+28*c))*x**2 +x*(1/4/(72*c/(9+28*c)) -(72/c/(9+28*c)) +(1/2)) - (1/4)*(72*c/(9+28*c)) < 0]
        ???还是改回去吧:
    break:见下面
    ]]

#rollback:『rollback:『c --> c*x』』
[@[c,x::real] -> [x>=4] -> [0 < c < 1/x] -> [x*ln(1+c/2) +ln(1+c/2) +ln9 < ln(9+28*c*x -72*c)]]
    [[proof:
    [4 <= x < 1/c]
    [f(x) := x*ln(1+c/2) +ln(1+c/2) +ln9 - ln(9+28*c*x -72*c)]
    [Df(x)
    == ln(1+c/2) - 28*c/(9+28*c*x -72*c)
    ]
    !! [x>=4]
    !! [0 < c < 1/x]
    [0 < c < 1/4]
    [(9+28*c*x -72*c) >= (9+28*c*4 -72*c) == (9+40*c) > 0]
    [(9+28*c*x -72*c) > 0]
    [ln(1+c/2) > 0]

    [Df(x) <= 0]:
        <==> [ln(1+c/2) <= 28*c/(9+28*c*x -72*c)]
        !! [(9+28*c*x -72*c) > 0]
        !! [ln(1+c/2) > 0]
        <==> [(9+28*c*x -72*c) <= 28*c/ln(1+c/2)]
        <==> [28*c*x <= (72*c-9) +28*c/ln(1+c/2)]
        <==> [x <= (72*c-9)/(28*c) +1/ln(1+c/2)]
        <==> [x <= 9*(2/7 -1/(28*c)) +1/ln(1+c/2)]
        !! rhs(c)单调递增
        => [rhs(c) > rhs(0^{+}) == 9*(2/7 -1/(28*0^{+})) +1/ln(1+0^{+}/2) == -oo]
        => [rhs(c) <= rhs(1/x) == 9*(2/7 -1/(28*1/x)) +1/ln(1+1/x/2) <= rhs(1/4) == 9*(2/7 -1/(28*1/4)) +1/ln(1+1/4/2) == 9*(2/7 -1/7) +1/ln(1+1/8) == 9/7 +ln(9/8)]
        !! [@[x::real] -> [not [-1 <= L <= 0]] -> [B:=1+L] -> [1/B < ln(B/L) < 1/L]] # bounds4ln_BoverL:goto
        => [rhs(c) <= 9/7 +ln(9/8) < 9/7 + 1/8 < 10/7 < 4]
        <==> [x <= rhs(c) < 4]
        !! [x >= 4]
        <==> _L
    [Df(x) > 0]
    !! [4 <= x < 1/c]
    [f(x)
    < f(1/c)
    == (1/c)*ln(1+c/2) +ln(1+c/2) +ln9 - ln(9+28*c*(1/c) -72*c)
    == (1+1/c)*ln(1+c/2) +ln9 -ln(37-72*c)
    ]
    # [g(c) := (1+1/c)*ln(1+c/2) +ln9 -ln(37-72*c)]
    [g(c) := (1+1/c)*ln(1+c/2)]
    [h(z) := g(2/z)]
    [h(z) == g(2/z) == (1+z/2)*ln(1+1/z)]
    !! [0 < c < 1/x]
    !! [c := 2/z]
    [0 < 2/z < 1/x]
    [z > 2*x]
    [Dh(z)
    == (1/2)*ln(1+1/z) + (1+z/2)/(1+1/z) * -1/z**2
    == (1/2)*ln(1+1/z) - (1+z/2)/(1+z) /z
    == (1/2)*ln(1+1/z) - (1+z -z/2)/(1+z) /z
    == (1/2)*ln(1+1/z) -1/z +1/2/(1+z)
    == -(1/2)*(1/z-ln(1+1/z) +1/z -1/(1+z))
    !! [ln(1+1/z) < 1/z]
    !! [1/(1+z) < 1/z]
    < 0
    ]
    [z > 2*x]
    [h(z)
    >= h(+oo)
    == limit[(1+z/2)*ln(1+1/z) | z--> +oo]
    == limit[(1+z/2)*(1/z) | z--> +oo]
    == 1/2
    ]
    [g(c) > g(0) == h(+oo) == 1/2]
    [g(c) > 1/2]
    [f(x)
    < (1+1/c)*ln(1+c/2) +ln9 -ln(37-72*c)
    == g(c) +ln9 -ln(37-72*c)
    !! [g(c) > 1/2]
    < 1/2 +ln9 -ln(37-72*c)
    !! [0 < c < 1/x]
    < 1/2 +ln9 -ln(37-72/x)
    !! [4 <= x < 1/c]
    <= 1/2 +ln9 -ln(37-72/4)
    == 1/2 +ln9 -ln(37-18)
    == 1/2 +ln9 -ln(19)
    == (1 +2*ln(9/19))/2
    == (1 -ln(361/81))/2
    !! [361/81 > 4 > e]
    < 0
    ]
    [f(x) < 0]
    [x*ln(1+c/2) +ln(1+c/2) +ln9 < ln(9+28*c*x -72*c)]
    DONE
    ]]

=======

===
]]]

]]]]]]]]]
#]]]'''#'''

__all__
_debugging_ = True
def std4pf_(ez, x, /):
    assert x > 0, (ez, x)
    (_ez, odd) = factor_pint_out_power_of_base_(2, x)
    ez = ez + _ez
    return (ez, odd)
def fraction5pf_(r, /):
    (ez, odd) = r
    assert odd&1
    return Fraction(2)**ez * odd


def ceil_log2__4pf_(r, /):
    'ceil_log2{positive_float}'
    (ez, odd) = r
    fe4odd = -1+odd.bit_length()
    ce4odd = fe4odd + (not odd == 1<<fe4odd)
    return ez + ce4odd
def num_bits4pf_(r, /):
    'num_bits4pf_{positive_float}'
    (ez, odd) = r
    return odd.bit_length()
def trunc4pf_(b, r, /):
    'trunc4pf_{positive_float}'
    # [trunc4pf_(b;pf) := div4pf_k_(b;pf,1)]
    if 0:
        # to found bug
        return div4pf_k_(b, r, 1)
    if not b > 0:raise ValueError('[b==0] => [result:=0] which is not positive_float')
    B = num_bits4pf_(r)
    if B > b:
        (ezO, oddO) = r
        d = (B-b)
        xT = oddO >> d
        (_ez, oddT) = factor_pint_out_power_of_base_(2, xT)
        #bug{4->(4,1)}:ezT = ezO + _ez
        ezT = ezO + _ez + d
        pfT = (ezT, oddT)
    else:
        pfT = r
    return pfT

def mul4pf_(lhs, rhs, /):
    'mul{positive_float}'
    (ezL, oddL) = lhs
    (ezR, oddR) = rhs
    return (ezL+ezR, oddL*oddR)
def add4pf_(lhs, rhs, /):
    'add{positive_float}'
    (ezL, oddL) = lhs
    (ezR, oddR) = rhs
    if ezL == ezR:
        even = oddL + oddR
        (_ez, odd) = factor_pint_out_power_of_base_(2, even)
        ez = ezL + _ez
    else:
        if ezL > ezR:
            lhs, rhs = rhs, lhs
            (ezL, oddL) = lhs
            (ezR, oddR) = rhs
        assert ezL < ezR

        evenR = oddR << (ezR -ezL)
        odd = oddL + evenR
        ez = ezL
    return (ez, odd)
def __():
    def neg4pf_(r, /):
        raise Exception('not positive')
        (ez, odd) = r
        return (ez, -odd)
    def sub4pf_(lhs, rhs, /):
        raise Exception('may be not positive')
def unsafe_sub4pf_(lhs, rhs, /):
    (ezL, oddL) = lhs
    (ezR, oddR) = rhs
    if ezL == ezR:
        even = oddL - oddR
        if even <= 0:raise Exception
        (_ez, odd) = factor_pint_out_power_of_base_(2, even)
        ez = ezL + _ez
    else:
        if ezL > ezR:
            lhs, rhs = rhs, lhs
            (ezL, oddL) = lhs
            (ezR, oddR) = rhs
            neg = True
        else:
            neg = False
        assert ezL < ezR

        evenR = oddR << (ezR -ezL)
        odd = oddL - evenR
        if neg:
            odd = -odd
        if odd <= 0:raise Exception
        ez = ezL
    return (ez, odd)
def lt4pf_(lhs, rhs, /):
    (ezL, oddL) = lhs
    (ezR, oddR) = rhs
    if ezL == ezR:
        return oddL < oddR
    # [ezL =!= ezR]
    nb4L = ezL + oddL.bit_length()
    nb4R = ezR + oddR.bit_length()
    if not nb4L == nb4R:
        return nb4L < nb4R
    # [nb4L == nb4R]
    # [ezL =!= ezR]
    if ezL > ezR:
        # [ezL > ezR]
        # [oddL.bit_length() < oddR.bit_length()]
        xR = oddR >> (ezL -ezR)
        # [xR < oddR/2**(ezL -ezR) < 1+xR]
        return oddL <= xR
    else:
        # [ezL <= ezR]
        # !! [ezL =!= ezR]
        # [ezL < ezR]
        # [oddL.bit_length() > oddR.bit_length()]
        #assert ezL < ezR
        xL = oddL >> (ezR -ezL)
        # [xL < oddL/2**(ezR -ezL) < 1+xL]
        return xL < oddR


def step4pf_(b, r, /):
    '-> r*(1+2**-b)'
    return add4pf_(r, rshift4pf_k_(r, b))
def rshift4pf_k_(r, k, /):
    '-> r/2**k'
    (ez, odd) = r
    return (ez-k, odd)
def lshift4pint_(n, pad, /):
    '-> (r*2**pad if pad >= 0 else r//2**-pad)'
    if pad < 0:
        return n >> -pad
    return n << pad
def div4pf_k_(b, r, k, /):
    assert k > 0
    assert b > 0
    r'''[[[
[div4pf_k_(b;r,k) := (r.ez-pad, (r.odd<<pad) //k)]
    where:
        [nb4r := num_bits4pf_(r)]
        [ce4k := ceil_log2(k)]
        [pad := (b+ce4k-nb4r)]
    NOTE:MAYBE[pad < 0]
    #]]]'''#'''
    nb4r = num_bits4pf_(r)
    ce4k = ceil_log2(k)
    pad = (b+ce4k-nb4r)
    (ez, odd) = r
    return std4pf_(ez-pad, lshift4pint_(odd, pad)//k)

def pow4pf_k_(b, r, k, /, *, avoid_trunc_first=False):
    assert k > 0
    assert b > 0
    if not avoid_trunc_first:
        r = trunc4pf_(b, r)
    elif _debugging_:
        assert r == trunc4pf_(b, r)
    # [r trunc4pf_]
    avoid_trunc_last = False
    if k == 1:
        pow_r_k = r
        # [pow_r_k trunc4pf_]
        avoid_trunc_last = True
    elif k&1:
        # odd
        pow_r_kmm = pow4pf_k_(b, r, k-1, avoid_trunc_first=True)
        pow_r_k = mul4pf_(r, pow_r_kmm)
        # [pow_r_k not trunc4pf_]
    else:
        h = k >>1
        pow_r_h = pow4pf_k_(b, r, h, avoid_trunc_first=True)
        pow_r_k = mul4pf_(pow_r_h, pow_r_h)
        # [pow_r_k not trunc4pf_]
    if not avoid_trunc_last:
        pow_r_k = trunc4pf_(b, pow_r_k)
    elif _debugging_:
        assert r == trunc4pf_(b, r)
    # [pow_r_k trunc4pf_]
    return pow_r_k

def cmp_pow4pint_(n, x, k, /):
    'n/uint{>0} -> x/uint{>0} -> k/uint{>0} -> sign_of(n-x**k)/{-1|0|+1}'
    assert n > 0
    assert x > 0
    assert k > 0
    nb4zn = n.bit_length()
    # [nb4zn == floor_log2(2*n)]
    ce4k = ceil_log2(k)
    #min_b4N = 4 + ce4k
    max1_b4B = 3 + ce4k
    # [max1_b4B == ceil_log2(8*k)]
    n7pf = std4pf_(0, n)
    x7pf = std4pf_(0, x)
    b = 1
    assert b <= nb4zn
    # [distance_(i,j) =[def]= if i==j then 0 else floor_log2(abs(i-j))]
    # [min_b7stop := max(1, nb4zn-distance_(n,x**k))]
    while 1:
        # [1 <= b <= nb4zn]
        low4pow_x_k = pow4pf_k_(b+max1_b4B, x7pf, k)
        # [low4pow_x_k <= x**k < low4pow_x_k*(1+2**-b)]
        if lt4pf_(n7pf, low4pow_x_k):
            # [n < pow4pf_k_(b;x7pf,k) <= x**k]
            return -1
        # [pow4pf_k_(b;x7pf,k) <= n]
        up4pow_x_k = step4pf_(b, low4pow_x_k)
        # [up4pow_x_k == low4pow_x_k*(1+2**-b)]
        if not lt4pf_(n7pf, up4pow_x_k):
            # [x**k < pow4pf_k_(b;x7pf,k)*(1+2**-b) <= n]
            return +1
        # !! [n < 2**nb4zn <= 2*n]
        # [pow4pf_k_(b;x7pf,k) <= {n,x**k} < pow4pf_k_(b;x7pf,k)*(1+2**-b) < pow4pf_k_(b;x7pf,k) +2**(nb4zn-b)]
        # [abs(n-x**k) < 2**(nb4zn-b)]

        # [1 <= b <= nb4zn]
        if b == nb4zn:
            return 0
        # [1 <= b < nb4zn]

        # !! [b < nb4zn]
        # [n==x**k] => [distance_(n,x**k) == 0 < nb4zn -b]
        # !! [abs(n-x**k) < 2**(nb4zn-b)]
        # [n=!=x**k] => [distance_(n,x**k) == floor_log2(abs(n-x**k)) <= log2(abs(n-x**k)) < log2(2**(nb4zn-b)) == nb4zn -b]
        # [distance_(n,x**k) < nb4zn -b]
        # [b < nb4zn -distance_(n,x**k)]
        # [b < max(1,nb4zn -distance_(n,x**k)) == min_b7stop]
        # [b < min_b7stop]
        # invariant: [b < min_b7stop]
        # [1 <= b < nb4zn]
        b = min(nb4zn, b<<1)
        # [1 < b <= nb4zn]
def _nroot4pf_k__7binary_search_(b, r, k, /):
    '-> near{r**/-k}'
    # [1 <= b <= 3+ceil_log2(k) == ceil_log2(8*k)]
    assert k > 0
    assert b > 0
    # [b >= 1]
    ce4r = ceil_log2__4pf_(r)
    # [2**(-1+ce4r) < r <= 2**(ce4r)]
    # [2**((-1+ce4r)/k) < r**/k <= 2**(ce4r/k)]
    # [2**((-1+ce4r)/-k) > r**/-k >= 2**(ce4r/-k)]
    # !! [ceil((-1+ce4r)/-k) == ceil((1-ce4r)/k) == ((1-ce4r+(k-1))//k) == ((k-ce4r)//k) == (1 + (-ce4r)//k)]
    # [2**(1 + ce4r//-k) > r**/-k >= 2**(ce4r//-k)]
    fe4z = ce4r // -k
    # [2**fe4z <= r**/-k < 2**(1+fe4z)]

    z = std4pf_(-1+fe4z, 3)
    # [z == nroot_(1;r,k)]
    if b == 1:
        return z
    # [b >= 2]
    _b = 1
    # [_b <= b]
    # [2**fe4z == z -2**(fe-_b) <= r**/-k < z +2**(fe-_b) == 2**(1+fe4z)]
    # [2**fe4z <= z -2**(fe-_b) <= r**/-k < z +2**(fe-_b) <= 2**(1+fe4z)]
    # [z == nroot_(_b;r,k)]
    B = ceil_log2(66*(1+2*k))
    # !! [1 <= b <= 3+ceil_log2(k) == ceil_log2(8*k)]
    # [B > b]
    r7B = trunc4pf_(B, r)
    for _b in range(1, b):
        # [_b < b]
        # [z == nroot_(_b;r,k)]
        # invariant:[2**fe4z <= z -2**(fe-_b) <= r**/-k < z +2**(fe-_b) <= 2**(1+fe4z)]
        # !! [_b < b < B]
        # [z == trunc4pf_(B, z)]
        # => avoid_trunc_first
        pow_z_k = pow4pf_k_(B, z, k, avoid_trunc_first=True)
        mul_r_pow_z_k = trunc4pf_(B, mul4pf_(r7B, pow_z_k))
            # ~= r*z**k ~= 1
        if not lt4pf_(_div_993_1024, mul_r_pow_z_k):
            # [r*z**k <= 993/1024]
            z = add4pf_(z, std4pf_(fe4z-_b-1, +1))
        elif not lt4pf_(_one, mul_r_pow_z_k):
            # [993/1024 < r*z**k <= 1]
            pass
        else:
            # [1 < r*z**k]
            #bug:z = add4pf_(z, std4pf_(fe4z-_b-1, -1))
            z = unsafe_sub4pf_(z, std4pf_(fe4z-_b-1, +1))
        z
        # [z == nroot_(1+_b;r,k)]
    # [z == nroot_(b;r,k)]
    return z
_div_993_1024 = std4pf_(-10, 993)
    # [32/33 < float(993*2**-10) < e**/-33]
_one = std4pf_(0, 1)

def nroot4pf_k_(b, r, k, /):
    '-> near{r**/-k}'
    assert k > 0
    assert b > 0
    ce4k = ceil_log2(k)
    #max1_b4B = 3 + ce4k
    min_b4N = 4 + ce4k
    if b >= min_b4N:
        kpp7pf = std4pf_(0, 1+k)
    stk = []
    while b >= min_b4N:
        #_nroot4pf_k__7Newton_method_
        # [b >= 4+ceil_log2(k) == ceil_log2(16*k)]
        bx = 1 +(b +ce4k)//2
        stk.append((b, bx))
        b = bx
    # [b <= 3+ceil_log2(k) == ceil_log2(8*k)]
    z = _nroot4pf_k__7binary_search_(b, r, k)
    for (b, bx) in reversed(stk):
        B = 2*bx +4 -ce4k
        r7B = trunc4pf_(B, r)
        z = _post4nroot4pf_k__7Newton_method_(b, r, k, kpp7pf, bx, B, r7B, z)
    # [(1-2**-b) < (r**/-k) / z < (1+2**-b)]
    # [(1-2**-b) < (r**/-k) / nroot_(b;r,k) < (1+2**-b)]
    return z

def _nroot4pf_k__7Newton_method_(b, r, k, /):
    '-> near{r**/-k}'
    # [b >= 4+ceil_log2(k) == ceil_log2(16*k)]
    assert k > 0
    assert b >= 4
    # [b >= 4]

    # update6Newton_method:[new_z == (z*(1+k) -r*z**(1+k))/k]
    kpp7pf = std4pf_(0, 1+k)
    ce4k = ceil_log2(k)
    # [b >= 4+ce4k]

    # [bx := ceil_log2(2*k) +ceil((b -ceil_log2(2*k)) / 2)]
    # [bx == ceil(ceil_log2(2*k) +(b -ceil_log2(2*k)) / 2)]
    # [bx == ceil((b +ceil_log2(2*k)) / 2)]
    # [bx == ceil((b +1+ceil_log2(k)) / 2)]
    # [bx == floor((1+b +1+ceil_log2(k)) / 2)]
    # [bx == 1 +((b +ceil_log2(k)) //2)]
    # [bx == 1 +(b +ce4k)//2]
    bx = 1 +(b +ce4k)//2
    # !! [b >= 4+ce4k]
    # [bx >= 1 +(4+ce4k +ce4k)//2 == 3+ce4k]
    # [bx >= 3+ce4k]
    # !! [b >= 4+ce4k]
    # [ce4k <= b-4]
    # [bx <= 1 +(b +(b-4))/2 == b-1 < b]
    # [bx < b] # ==>> recur stop
    # [3+ce4k <= bx < b]

    B = 2*bx +4 -ce4k
    r7B = trunc4pf_(B, r)
    # [B{b} := 2*bx +4 -ce4k]
    # !! [3+ce4k <= bx < b]
    # [6+2*ce4k <= 2*bx < 2*b]
    # [10+ce4k <= 2*bx +4 -ce4k < 2*b +4 -ce4k]
    # [10+ce4k <= B < 2*b +4 -ce4k]

    # !! [3+ce4k <= bx < b]
    # [B == 2*bx +4 -ce4k == bx +4 +(bx-ce4k) >= bx +4 +3 == 7+bx]
    # [B-bx >= 7]

    # !! [3+ce4k <= bx{b} < b]
    # !! [bx{b} == 1 +(b +ce4k)//2]
    # [bx{b} >= 4+ce4k] => [bx{bx{b}} <= bx{b}]
    # !! [B{b} := 2*bx +4 -ce4k]
    # [bx{b} >= 4+ce4k] => [B{bx{b}} <= B{b}]
    # [bx{b} == (3+ce4k)] => [B{bx{b}} == ceil_log2(66*(1+2*k)) <?> B{b} == 2*bx +4 -ce4k == 2*(3+ce4k) +4 -ce4k == 10+ce4k == ceil_log2(1024*k)]
    # !! [k >= 1]
    # [1024*k -(66*(1+2*k)) >= 1024*k -(66*(k+2*k)) == 1024*k -198*k > 0]
    # [bx{b} == (3+ce4k)] => [B{bx{b}} <= B{b}]
    # !! [bx{b} >= 4+ce4k] => [B{bx{b}} <= B{b}]
    # [bx{b} >= (3+ce4k)] => [B{bx{b}} <= B{b}]

    f = _nroot4pf_k__7binary_search_ if bx <= 3+ce4k else _nroot4pf_k__7Newton_method_
    z = f(bx, r, k) #recur
    return _post4nroot4pf_k__7Newton_method_(b, r, k, kpp7pf, bx, B, r7B, z)
def _post4nroot4pf_k__7Newton_method_(b, r, k, kpp7pf, bx, B, r7B, z, /):
    # [z*(1-2**-bx{b}) < r**/-k < z*(1+2**-bx{b})]
    # !! [3+ce4k <= bx{b} < b]
    # [z*(1-2**-(3+ce4k)) < r**/-k < z*(1+2**-(3+ce4k))]
    # [z**k*(1-2**-(3+ce4k))**k < 1/r < z**k*(1+2**-(3+ce4k))**k]
    # [(1+2**-(3+ce4k))**-k < r*z**k < (1-2**-(3+ce4k))**-k]

    r'''[[[
    ?c => [z*(1+c) == r**/-k]
    [z*(1-2**-(3+ce4k)) < z*(1+c) < z*(1+2**-(3+ce4k))]
    [-2**-(3+ce4k) < c < +2**-(3+ce4k)]

    !! [2**(-1+3+ce4k) < 8*k <= 2**(3+ce4k)]
    [2*2**-(3+ce4k) > 1/(8*k) >= 2**-(3+ce4k)]
    [1/(16*k) < 2**-(3+ce4k) <= 1/(8*k)]
    !! [-2**-(3+ce4k) < c < +2**-(3+ce4k)]
    [-1/(8*k) < c < 1/(8*k)]
    !! [@[k,c::real][k >= 1][c > -1/k] -> [(1+c)**k >= 1+c*k]] # 辅助公式牜一:goto
    [(1+c)**k >= 1+c*k > 1-1/8 == 7/8 > 1/2]
    [(1+c)**-k < 2]

    [(z*(1+k) -r*z**(1+k))
    !! [z*(1+c) == r**/-k]
    == z*(1+k -(1+c)**-k)
    !! [(1+c)**-k < 2]
    !! [z>0]
    > z*(1+k -2)
    == z*(k -1)
    !! [k>=1]
    !! [z>0]
    >= 0
    ]
    [(z*(1+k) -r*z**(1+k)) > 0]
    => ok:unsafe_sub4pf_

    #]]]'''#'''

    # [z7B := trunc4pf_(B, z)]
    # !! [B-bx >= 7]
    # bug:[z7B == z]
    # !! [3+ce4k <= bx{b} < b]
    # !! [bx{b} >= (3+ce4k)] => [B{bx{b}} <= B{b}]
    # [z7B == z]
    z7B = z

    # !! update6Newton_method:[new_z == (z*(1+k) -r*z**(1+k))/k]
    mul_z_kpp = mul4pf_(z7B, kpp7pf)
    pow_z_kpp = pow4pf_k_(B, z7B, 1+k, avoid_trunc_first=True)
    mul_r_pow_z_kpp = trunc4pf_(B, mul4pf_(r7B, pow_z_kpp))
        # ~= r*z**(1+k) ~= z
    new_z = div4pf_k_(B, unsafe_sub4pf_(mul_z_kpp, mul_r_pow_z_kpp), k)
        #sub4pf_ raise Exception('may be not positive')
    return new_z



def detect_perfect_kth_root_(k, n, nb4zn, inv4n7pf, /):
    'k/uint{>=2} -> n/uint{>=2} -> nb4zn/uint -> inv4n7pf/positive_float -> (0|rt) # [rt**k == n] # [nb4zn := floor_log2(2*n)][b==3+ceil(nb4zn/k)][(1-2**-b) < (1/n)/inv4n7pf < (1+2**-b)]  #eg:[inv4n7pf:=nroot_(b;n,1)]'
    assert k >= 2
    assert n >= 2
    assert nb4zn >= k
    b = 3-(nb4zn//-k)
    # [b==3+ceil(nb4zn/k)]
    assert b >= 4
    rt7pf = nroot4pf_k_(b, inv4n7pf, k)
    # [(1-2**-b) < (inv4n7pf**/-k) / rt7pf < (1+2**-b)]
    # [rt7pf ~ (1/n)**/-k == n**/k]
    # [abs(rt7pf - n**/k) < 1/4]
    r'''[[[
    Lemma__10_1__1
    [@[t::real] -> [0 <= t <= 1/10] -> [sqrt(1+t)/(1-t) <= (1+2*t)]]
    Lemma__10_1__2
    [@[t::real] -> [0 <= t <= 1/10] -> [sqrt(1-t)/(1+t) >= (1-2*t)]]

    Lemma__10_1
    [@[t::real] -> [f(t) := (1+2*t) -sqrt(1+t)/(1-t)] -> [0 <= t <= 1/10] -> [[f(+t) >= 0][f(-t) <= 0]]]
    <==>
    [@[t::real] -> [f(t) := (1+2*t) -sqrt(1+t)/(1-t)] -> [0 <= t <= 1/10] -> [[t*f(+t) >= 0][f(0) == 0]]]

    [[k,n>=2][nb4zn := floor_log2(2*n)][b==3+ceil(nb4zn/k)][(1-2**-b) < (1/n)/inv4n7pf < (1+2**-b)][(1-2**-b) < (inv4n7pf**/-k) / rt7pf < (1+2**-b)] -> [abs(rt7pf - n**/k) < 1/4]]
    [[proof:
    !! [nb4zn := floor_log2(2*n)]
    [n < 2**nb4zn <= 2*n]
    [n**/k < 2**(nb4zn/k) <= 2*n**/k]
    !! [n >= 2]
    [nb4zn >= 2]
    [b >= 4]
    [c := 2**-b]
    [0 < c <= 2**-4 == 1/16 < 1/10]
    [0 < c < 1/10]
    [0 < c < 1]
    [(1-c) < (inv4n7pf**/-k) / rt7pf < (1+c)]
    [(1-c) < (1/n)/inv4n7pf < (1+c)]

    [(1-c)**/k < (inv4n7pf**/-k)/(n**/k) < (1+c)**/k]
    [(1-c)**/k * (n**/k) < (inv4n7pf**/-k) < (1+c)**/k * (n**/k)]

    [(inv4n7pf**/-k)/(1+c) < rt7pf < (inv4n7pf**/-k)/(1-c)]
    [(1-c)**/k * (n**/k)/(1+c) < rt7pf < (1+c)**/k * (n**/k)/(1-c)]

    [(n**/k) * ((1-c)**/k/(1+c) -1) < rt7pf -(n**/k) < (n**/k) * ((1+c)**/k/(1-c) -1)]
    !! [k>=2]
    !! [0 < c < 1]
    [(1-c)**/k <= (1-c)**/2 < 1 < (1+c)**/2 <= (1+c)**/k]
    [(n**/k) * ((1-c)**/2/(1+c) -1) < rt7pf -(n**/k) < (n**/k) * ((1+c)**/2/(1-c) -1)]
    !! [0 < c < 1/10]
    !! [@[t::real] -> [f(t) := (1+2*t) -sqrt(1+t)/(1-t)] -> [0 <= t <= 1/10] -> [[f(+t) >= 0][f(-t) <= 0]]] #Lemma__10_1
    [(n**/k) * ((1-2*c) -1) < rt7pf -(n**/k) < (n**/k) * ((1+2*c) -1)]
    [(n**/k) * (-2*c) < rt7pf -(n**/k) < (n**/k) * (+2*c)]
    !! [n**/k < 2**(nb4zn/k)]
    !! [c > 0]
    [2**(nb4zn/k) * (-2*c) < rt7pf -(n**/k) < 2**(nb4zn/k) * (+2*c)]
    [abs(rt7pf -(n**/k)) < 2**(nb4zn/k) * (+2*c)]

    [abs(rt7pf -(n**/k))
    < 2**(nb4zn/k) * 2*c
    == 2**(nb4zn/k) * 2*2**-b
    !! [b==3+ceil(nb4zn/k)]
    == 2**(nb4zn/k) * 2*2**-(3+ceil(nb4zn/k))
    == 2**(nb4zn/k +1 -(3+ceil(nb4zn/k)))
    <= 1/4
    ]
    [abs(rt7pf -(n**/k)) < 1/4]
    DONE
    ]]

    #]]]'''#'''
    rt7pf
    # [abs(rt7pf -(n**/k)) < 1/4]
    # ?rt7uint => [abs(rt7uint - rt7pf) <= 5/8]
    (rt7uint, sign4diff, may_abs4diff) = find_arbitrary_uint_ex__nearby_le_5over8_(rt7pf)
    # [sign4diff == sign_of(rt7uint - rt7pf)]
    # [abs(rt7uint - rt7pf) <= 5/8]
    if sign4diff == 0:
        assert may_abs4diff is None
        # [abs(rt7uint - rt7pf) == 0]
        # [abs(rt7uint - rt7pf) < 1/4]
        # [rt7uint == rt7pf > 0]
        # [rt7uint > 0]
        assert not rt7uint == 0
        if 0:
            #bug{244->(3,5)}:
            #   !! rt7uint is int, but maybe not the root!!
            return rt7uint
        # [rt7uint > 0][abs(rt7uint - rt7pf) < 1/4]
        pass
    else:
        assert not may_abs4diff is None
        abs4diff = may_abs4diff
        if rt7uint == 0:
            # !! [rt7pf > 0]
            # [rt7uint == 0 < rt7pf]
            # !! [sign4diff == sign_of(rt7uint - rt7pf)]
            assert sign4diff == -1
            return 0
        # [rt7uint > 0]
        if not lt4pf_(abs4diff, _1over4):
            return 0
        # [abs(rt7uint - rt7pf) < 1/4]
        # [rt7uint > 0][abs(rt7uint - rt7pf) < 1/4]
    # [rt7uint > 0][abs(rt7uint - rt7pf) < 1/4]
    if 0 == cmp_pow4pint_(n, rt7uint, k):
        return rt7uint
    return 0
_1over4 = std4pf_(-2, 1)
def find_arbitrary_uint_ex__nearby_le_5over8_(r, /):
    '-> (u/uint, sign4diff/{-1|0|+1}, may abs4diff/pf) # [diff:=u-r][diff==sign4diff*abs4diff]'
    (ez, odd) = r
    if ez >= 0:
        u = odd << ez
        #bug:return (u, 0, 0)
        return (u, 0, None)
    # [ez < 0]
    ux = odd >> (-1-ez)
    u = ux >> 1
    mask = (-1+(1<<-ez))
    odd4abs4diff = (odd & mask)
    if ux&1:
        u += 1
        odd4abs4diff ^= mask
        odd4abs4diff += 1
        sign4diff = +1
    else:
        sign4diff = -1
    ez4abs4diff = ez
    assert odd4abs4diff&1
    abs4diff = (ez4abs4diff, odd4abs4diff)
    return (u, sign4diff, abs4diff)

def detect_perfect_power_(n, /):
    '-> ((n,1)|(rt,exp{arbitrary_exp}))'
    '-> ((n,1)|(rt/max_nontrival_root,p/min_prime))'
    # [factor_pint_as_perfect_power_{arbitrary_exp_ok:=True} :: perfect-power decomposition algorithm]
    return factor_pint_as_perfect_power_(n, arbitrary_exp_ok=True)
def _init4factor_pint_as_perfect_power_(n, /):
    nb4zn = n.bit_length()
    # [nb4zn == floor_log2(2*n)]
    # [n < 2**nb4zn <= 2*n]
    min_k = min_p = 2
    max_b = 3-(nb4zn//-min_k)
        # !! [b==3+ceil(nb4zn/k)]
    n7pf = std4pf_(0, n)
    inv4n7pf = nroot4pf_k_(max_b,n7pf,1)
    return (nb4zn, inv4n7pf)
def factor_pint_as_perfect_power_(n, /, *, arbitrary_exp_ok=False):
    '-> ((n,1)|(rt/min_nontrival_root,exp/max_exp))'
    # [factor_pint_as_perfect_power_ :: perfect-power classification algorithm] # max exp
    check_int_ge(2, n)
    (nb4zn, inv4n7pf) = _init4factor_pint_as_perfect_power_(n)
    ps = list_primes__lt_(nb4zn, _mk=list)
    #for k in ps:
        # !! skip:『j+=1』 to reuse k
        # for_loop --> while_loop
    j = 0
    exp = 1
    while j < len(ps):
        k = ps[j]
        rt = detect_perfect_kth_root_(k, n, nb4zn, inv4n7pf)
        if not rt == 0:
            n = rt
            exp *= k
            if arbitrary_exp_ok:
                break
            (nb4zn, inv4n7pf) = _init4factor_pint_as_perfect_power_(n)
            while ps and not ps[-1] < nb4zn:
                ps.pop()
            #skip:『j+=1』
            continue
        j += 1
    return (n, exp)
def is_perfect_power_(n, /):
    # [is_perfect_power_ :: perfect-power dedetection algorithm]
    assert n >= 2
    return not 1 == detect_perfect_power_(n)[1]



def _iter_run_lt__to_seperate_setup_time_(m, /, *, repeat, validate, **kwds):
    _run_lt_(30, validate=True, **kwds)
    yield 666
    for _ in range(repeat):
        _run_lt_(m, validate=validate, **kwds)
    yield 999
def _run_lt_(m, /, *, validate, **kwds):
    if validate:
        from math import gcd
        from seed.math.prime_sieve.sieve_lt import tabulate_may_prime_factorization4uint_lt_
        u2p2e = tabulate_may_prime_factorization4uint_lt_(m)
    for u in range(2, m):
        (rt, e) = factor_pint_as_perfect_power_(u)
        if validate:
            p2e = u2p2e[u]
            _e = gcd(*sorted(p2e.values()))
            if not e == _e:raise Exception((u, p2e, _e, (rt, e)))
            if not rt**e == u:raise Exception((u, p2e, _e, (rt, e)))




__all__
from seed.math.factor_pint.perfect_power.detect_perfect_power__7lift_precision import detect_perfect_kth_root_
from seed.math.factor_pint.perfect_power.detect_perfect_power__7lift_precision import *
