#__all__:goto
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
>>>



py_adhoc_call   seed.math.factor_pint.perfect_power.detect_perfect_power__7lift_precision   @f
from seed.math.factor_pint.perfect_power.detect_perfect_power__7lift_precision import *
]]]'''#'''
__all__ = r'''
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
#.from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.#################################
#.from seed.helper.lazy_import__func7dict import lazy_import__funcs7dict_
#.(check_type_is, check_int_ge, _ifNone) = lazy_import__funcs7dict_(__name__ or globals() or locals(), 'seed.tiny_.check',  'check_type_is, check_int_ge      ifNone:_ifNone')
#.#################################
#.def mk_context4lazy_import_registered_names_(qnm4mdl7inject, qnm4pseudo_mdl7import, name7importZqnm4mdl, name7importZalias7inject={}, may_bifix4lazy_name7import=None, lazy_name7importZoriginal_name7import={}):
#.from seed.helper.lazy_import__func7context7register import mk_context4lazy_import_registered_names_, name7importZqnm4mdl_7tiny
#.with mk_context4lazy_import_registered_names_(__name__, 'seed._lazy_', name7importZqnm4mdl_7tiny):
#.    from seed._lazy_ import print_err, fst, echo, ifNone
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.math.max_power_of_base_as_factor_of_ import factor_pint_out_power_of_base_
#.    from itertools import islice
#.    from functools import cached_property
#.    from seed.for_libs.for_functools.cached_property import cached_property
#.    from seed.types.CachedProperty import CachedProperty, mk_cached_propertyT_
#.    from seed.func_tools.dot2 import dot
#.    from seed.tiny_.check import check_type_is, check_int_ge
#.with mk_ctx4lazy_import4funcs_(__name__, arbitrary_ok=True):
#.    from seed.data_funcs.lnkls import rglnkls_ops# empty_rglnkls, mk_empty_rglnkls, rglnkls_ipush_right, rglnkls_ipop_right, rglnkls2reversed_iterable, rglnkls5iterable
#.with mk_ctx4lazy_import4funcs_(__name__, 'ifNone:_ifNone, ifNonef:_ifNonef'):
#.    from seed.helper.ifNone import ifNone as _ifNone, ifNonef as _ifNonef
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

[num_bits_of(pf{ez,odd}) := odd.bit_length()]
[num_bits_of(pf{ez,odd}) == 1+floor_log2(odd)]
[2**(-1+num_bits_of(pf)) <= pf.odd < 2**num_bits_of(pf)]
[2**(-1+pf.ez+num_bits_of(pf)) <= pf < 2**(pf.ez+num_bits_of(pf))]

[b :: uint{>0}]
truncation to b bits
[trunc(b;pf) := div(b;pf,1)]
[num_bits_of(trunc(b;pf)) == min(b,num_bits_of(pf))]
[2**(-1+pf.ez+num_bits_of(pf)) <= trunc(b;pf) <= pf < trunc(b;pf) +2**(-b+pf.ez+num_bits_of(pf))]
!! [2**(-1+pf.ez+num_bits_of(pf)) <= trunc(b;pf)]
[2**(-b+pf.ez+num_bits_of(pf)) <= 2**(1-b)*trunc(b;pf)]
[2**(-1+pf.ez+num_bits_of(pf)) <= trunc(b;pf) <= pf < trunc(b;pf) +2**(-b+pf.ez+num_bits_of(pf)) <= trunc(b;pf)*(1+2**(1-b))]
[trunc(b;pf) <= pf < trunc(b;pf)*(1+2**(1-b))]
[1 <= pf/trunc(b;pf) < (1+2**(1-b))]
[0 <= -1+pf/trunc(b;pf) < 2**(1-b)]
[0 <= 2**b*(-1+pf/trunc(b;pf)) < 2]


[k :: uint{>0}]
[div(b;r,k) ~= (r/k)]
    approximation
[div(b;r,k) := (r.ez-pad, (r.odd<<pad) //k)]
    where:
        [nb4r := num_bits_of(r)]
        [ce4k := ceil_log2(k)]
        [pad := (b+ce4k-nb4r)]
    NOTE:MAYBE[pad < 0]
    [(r.odd<<pad) >>pad <= r.odd]
    [(r.odd<<pad) <= r.odd*2**pad]
[1 <= (r/k) / div(b;r,k) < (1+2**(1-b))]
    [[proof:
    [div(b;r,k) == 2**(r.ez-pad) *((r.odd<<pad) //k)]

    [s := div(b;r,k)]
    [m := ((r.odd<<pad) //k)]
    [m <= ((r.odd<<pad) /k) < 1+m]
    [k*m <= (r.odd<<pad) <= (k-1)+k*m]
    !! [div(b;r,k) == 2**(r.ez-pad) *((r.odd<<pad) //k)]
    [s == div(b;r,k) == 2**(r.ez-pad) *((r.odd<<pad) //k) == m*2**(r.ez-pad)]
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
    !! [s := div(b;r,k)]
    [1 <= (r/k) / div(b;r,k) < (1+2**(1-b))]
    DONE
    ]]
[k:=1]:
    [1 <= (r/1) / div(b;r,1) < (1+2**(1-b))]
    [1 <= r/trunc(b;r) < (1+2**(1-b))]

[pow_(b;r,k) ~= r**k]
    the b-bit approximate kth power of r
[TIME{pow_(b;r,k)} <= 2*floor_log2(k)*time4mul__le_zpow_(b)]


[pow_(b;r,1) := trunc(b;r)]
[pow_(b;r,1+2*k) := trunc(b;mul4pf_(trunc(b;r), pow_(b;r,2*k)))]
[pow_(b;r,2*k) := trunc(b;mul4pf_(pow_(b;r,k), pow_(b;r,k)))]

[1 <= (r**k) / pow_(b;r,k) < (1+2**(1-b))**(-1+2*k)]
    [[proof:
    [k > 0]
    * [k==1]:
        !! [1 <= r/trunc(b;r) < (1+2**(1-b))]
        ok
    * [k==i+j][1<=i<=j<k][1 <= (r**i) / pow_(b;r,i) < (1+2**(1-b))**(-1+2*i)][1 <= (r**j) / pow_(b;r,j) < (1+2**(1-b))**(-1+2*j)]:
        #任意拆分都行
        [1 <= (r**k) / (pow_(b;r,i)*pow_(b;r,j)) < (1+2**(1-b))**(-2+2*k)]
        !! [1 <= r/trunc(b;r) < (1+2**(1-b))]
        [1 <= (pow_(b;r,i)*pow_(b;r,j))/trunc(b;(pow_(b;r,i)*pow_(b;r,j))) < (1+2**(1-b))]
        [1 <= (r**k) / trunc(b;(2*j)) < (1+2**(1-b))**(-1+2*k)]
        ok
    DONE
    ]]

===
]]]
[[[
===

7.  Some overly specific inequalities 
Lemma 7.1.
[@[exp,err::real] -> [exp>0] -> [0 < err < 1] -> [(1+err/4/exp)**(2*exp) < (1+err)]]
    #[@[exp,err::real] -> [exp>0] -> [0 < err < 1/2] -> [(1+err/exp)**exp < (1+2*err)]]
Lemma 7.2.
[@[exp::real] -> [exp>=1] -> [7/8 <= (1-1/8/exp)**exp]]
Lemma 7.3.
[@[t::real] -> [0 < t < 1/36] -> [(1+3*t)*(1+t)*(1+(32/3)*t) < (1+16*t)]]
Lemma 7.4.
[@[t,exp::real] -> [exp>=1] -> [0 < t < 1/4/(1+exp)] -> [(1+t)**(3+2*exp) < 1+(16*t)*(-2+7*exp)/9]]

Lemma 7.1.
[@[x,c::real] -> [x>=1] -> [0 < c < 1] -> [(1-c/x)**x >= (1-c)]]
    # 统一形式牜下界:here
Lemma 7.2.
[@[x,c::real] -> [x>0] -> [0 < c < 1] -> [(1+c/(2*x))**x < (1+c)]]
    # 统一形式牜上界:goto





=======
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
def num_bits_of(pf, /):
    'num_bits_of{positive_float}'
    (ez, odd) = pf
    return odd.bit_length()
def trunc(b, pf, /):
    'trunc{positive_float}'
    if not b > 0:raise ValueError('[b==0] => [result:=0] which is not positive_float')
    # [trunc(b;pf) := div(b;pf,1)]
    B = num_bits_of(pf)
    if B > b:
        (ezO, oddO) = pf
        xT = oddO >> (B-b)
        (_ez, oddT) = factor_pint_out_power_of_base_(2, xT)
        ezT = ezO + _ez
        pfT = (ezT, oddT)
    else:
        pfT = pf
    return pfT
    return div4pf_k_(b, r, d)

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

def lshift4pint_(n, pad, /):
    if pad < 0:
        return n >> -pad
    return n << pad
def div4pf_k_(b, r, k, /):
    assert k > 0
    assert b > 0
    r'''[[[
[div(b;r,k) := (r.ez-pad, (r.odd<<pad) //k)]
    where:
        [nb4r := num_bits_of(r)]
        [ce4k := ceil_log2(k)]
        [pad := (b+ce4k-nb4r)]
    NOTE:MAYBE[pad < 0]
    #]]]'''#'''
    nb4r = num_bits_of(r)
    ce4k = ceil_log2(k)
    pad = (b+ce4k-nb4r)
    (ez, odd) = r
    return std4pf_(ez-pad, lshift4pint_(odd, pad)//k)
def std4pf_(ez, x, /):
    assert x > 0
    (_ez, odd) = factor_pint_out_power_of_base_(2, x)
    ez = ez + _ez
    return (ez, odd)

def pow4pf_k_(b, r, k, /, *, avoid_trunc_first=False):
    assert k > 0
    assert b > 0
    if not avoid_trunc_first:
        r = trunc(b, r)
    # [r trunc]
    avoid_trunc_last = False
    if k == 1:
        pow_r_k = r
        # [pow_r_k trunc]
        avoid_trunc_last = True
    elif k&1:
        # odd
        pow_r_kmm = pow4pf_k_(b, r, k-1, avoid_trunc_first=True)
        pow_r_k = mul4pf_(r, pow_r_kmm)
        # [pow_r_k not trunc]
    else:
        h = k >>1
        pow_r_h = pow4pf_k_(b, r, h, avoid_trunc_first=True)
        pow_r_k = mul4pf_(pow_r_h, pow_r_h)
        # [pow_r_k not trunc]
    if not avoid_trunc_last:
        pow_r_k = trunc(b, pow_r_k)
    # [pow_r_k trunc]
    return pow_r_k



__all__
from seed.math.factor_pint.perfect_power.detect_perfect_power__7lift_precision import *
