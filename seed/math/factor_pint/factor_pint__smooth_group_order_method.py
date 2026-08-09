#__all__:goto
#TODO:goto
r'''[[[
e ../../python3_src/seed/math/factor_pint/factor_pint__smooth_group_order_method.py
view ../../python3_src/seed/math/factor_pint/factor_pint__smooth_group_order_method__7py_adhoc_call.py
view ../../python3_src/seed/math/factor_pint/smooth_group_order_method.py
view ../../python3_src/seed/math/BinaryQuadraticForm.py


seed.math.factor_pint.factor_pint__smooth_group_order_method
py -m nn_ns.app.debug_cmd   seed.math.factor_pint.factor_pint__smooth_group_order_method -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.factor_pint.factor_pint__smooth_group_order_method:__doc__ -ht # -ff -df
#######

[[
come_from:
view script/整数分解牜允许快速求值的多根多项式.py
    ==>>: (P+1) method
        # vs:(P-1) method
更高维度 意义不大
DONE:factor_pint__smooth_group_order_method7Pmm_#(P-1) method
DONE:factor_pint__smooth_group_order_method7Qpp_#(P+1) method
]]
[[
[f(X):=X**2+B*X+1][p::prime]:
    [norm(%f(X);X) == 1]
    [D:=B**2-4]
    [Jacobi_symbol(p;D) == -1]:
        [(p+1) % order_(%{p;f(X)};X) == 0]
    [B:=+1]:
        [order_(%{p;f(X)};X) == 3]
    [B:=-1][p >= 3]:
        [order_(%{p;f(X)};X) == 6]
]]
[[
[n%2==0][n>0]:
    [D := [n%4==3]*-n + [n%4==1]*-4*n]
    [B**2-4*A*C == D]
    [-B**2+4*A*C == -D]
    [p::prime][p%2==1][A%p==0]:
        [D%p == (B**2-4*A*C)%p == B**2%p]
        [Jacobi_symbol(p;D)==+1]
        [B%p <- sqrts_mod_(p;D)]
        [B%2 == B**2%2 == (D+4*A*C)%2 == D%2]
        [B%2 == D%2]
    [p::prime][p%2==1][Jacobi_symbol(p;D)==+1][A:=p]:
        [xB6p := sqrts_mod_(p;D)[0]]
        [B := B6p if B6p%2 == D%2 else (p-B6p)]
        [C:=(B**2-D)///(4*A)]
    [n%4==3]:
        [-B**2+4*A*C == -D == n]
        [4*A*C == n+B**2]
        [B%2 == 1]
        [B:=1][A:=1][C:=(1+n)///4] => trivial_factorization#class_group{D}.one
        [B:=3][A:=1][C:=(9+n)///4] => ???
    [n%4==1]:
        [-B**2+4*A*C == -D == 4*n]
        [4*A*C == 4*n+B**2]
        [B%2 == 0]
        [A*C == n+(B///2)**2]
        [B:=0][A:=1][C:=n] => trivial_factorization#class_group{D}.one
        [B:=2][A:=2][C:=(n+1)///2] => trivial_factorization
        [B:=2][A:=1][C:=n+1] => ???

    factor n:
        [qfb :<- class_group{D}][h(D) == (1+2*k)*2**ez][gcd(e,h(D)) == (1+2*k)][g:=(qfb**e)][[g==class_group{D}.1]or[?[j:<-[0..<ez]] -> [is_ambiguous_form_(g**2**j)]]]
<<==:
binary quadratic form
[D<0][D%4 <= 1]:
  [h(D) =[def]= len(class_group{D})]
  [h(D) < sqrt(-D)*ln(-D)]

page248[259/604]
5.6.4 Ambiguous forms and factorization
[D<0][D%4 <= 1]:
  [class_group{D}.1 == [D%4==0](1,0,-D/4) + [D%4==1](1,1,(1-D)/4)]
  [is_ambiguous_form_(D;qfb) =[def]= [is_reduced_form_(D;qfb)][qfb**2 == 1]]
    #sqrt1
  [class_group{D}.ambiguous_form <- (a,0,c)|(a,a,c)|(a,b,a)]
#Lemma 5.6.8.Suppose D is a negative discriminant....
    # 注意下面:[u*v==-D///4] | [u*v==-D] 即 整数分解
    # [n%2==1] => [D == -n if n%4==3 else -4*n]
    #
    [[D<0][D%4 <= 1] -> [D%4==0] -> [class_group{D}.ambiguous_form_set == ({(u,0,v) | [[u,v::uint][0 < u <= v][u*v==-D///4][gcd(u,v)==1]]} \-/ {((u+v)///2,v-u,(u+v)///2) | [[u,v::uint][u < v <= 3*u][u*v==-D///4][gcd(u,v)<=2][(u+v)%4 == 2]]} \-/ {(2*u,2*u,(u+v)///2) | [[u,v::uint][0 < 3*u < v][u*v==-D///4][gcd(u,v)<=2][(u+v)%4 == 2]]})]]
        # [(u+v)%4 == 2]
        # [{u,v}%4 == {1}|{3}|{0,2}]
        # [(u*v)%4 == 1|0]
    [[D<0][D%4 <= 1] -> [D%4==1] -> [class_group{D}.ambiguous_form_set == ({((u+v)///4,(v-u)///2,(u+v)///4) | [[u,v::uint][u <= v <= 3*u][u*v==-D][gcd(u,v)==1]]} \-/ {(u,u,(u+v)///4) | [[u,v::uint][0 < 3*u <= v][u*v==-D][gcd(u,v)==1]]})]]
        # [(u+v)%4 == 0]
        # [(u*v)%4 == 3]
        # [{u,v}%4 == {1,3}]


view ../../python3_src/seed/math/BinaryQuadraticForm.py

TODO:
binary quadratic form
  [D == [n%4==3]*-n + [n%4==1]*-4*n]
  [h(D) < sqrt(-D)*ln(-D)]
  [bqf**odd then **2 to found ambiguous forms maybe yield nontrivial factorizations]
  [[bqf**2 == 1] <-> [bqf is ambiguous form]]


view ../../python3_src/seed/math/BinaryQuadraticForm.py
    Qfb__x__smooth_group_order_method:goto
]]
[[
view ../../python3_src/seed/math/factor_pint/factor_pint__elliptic_curve_method.py
TODO: Montgomery coordinates:(X,Z)
]]
[[
view ../../python3_src/seed/algo/rho_method__7iter.py
view ../../python3_src/seed/types/HistorySaver.py
view ../../python3_src/seed/abc/IReproduceable.py
view ../../python3_src/seed/types/Reproduceable.py
TODO: rho_method+Reproduceable+HistorySaver
]]
























'#'; __doc__ = r'#'
>>> factor_pint__smooth_group_order_method7Pmm_(17*31, 5,  2,2, bound4pow4stage1=16)
17
>>> factor_pint__smooth_group_order_method7Pmm_(17*31, 5,  2,2, bound4pow4stage1=8)
0

>>> factor_pint__smooth_group_order_method7Pmm_(7*5, 2,  2,3)
7
>>> factor_pint__smooth_group_order_method7Pmm_(7*5, 2,  2,2)
0


M67
>>> [-1+2**67 == 193707721*761838257287]
[True]
>>> [-1+193707721 == 2**3 * 3**3 *5 *67 *2677]
[True]
>>> factor_pint__smooth_group_order_method7Pmm_(-1+2**67, 5,  67,2677)
193707721
>>> factor_pint__smooth_group_order_method7Pmm_(-1+2**67, 5,  67,-1+2677)
0
>>> factor_pint__smooth_group_order_method7Pmm_(-1+2**67, 5,  -1+67,2677)
0

>>> factor_pint__smooth_group_order_method7Pmm_(13*37, 2,  4,4)
13
>>> factor_pint__smooth_group_order_method7Pmm_(13*37, 6,  4,4)
37
>>> factor_pint__smooth_group_order_method7Pmm_(13*37, 10,  4,4) # !! [2,2,3]
(3,)
>>> factor_pint__smooth_group_order_method7Pmm_(13*37, 10,  3,3) # !! [2,3]
(2,)
>>> factor_pint__smooth_group_order_method7Pmm_(13*37, 10,  2,3) # !! [2]++[3]
(1, 2)
>>> search_the_last_used_prime_6stage2_6smooth_group_order_method_(2,2,3,  1,2)
3
>>> raw_search_the_last_used_prime_6stage2_6smooth_group_order_method_(2,3,  2-1)
3







>>> factor_pint__smooth_group_order_method7Qpp_(2, 0,  2,2, more_info=True)
(-99002, None, '[n==2]')
>>> factor_pint__smooth_group_order_method7Qpp_(4, 0,  2,2, more_info=True)
(99002, 2, '[n>2][n%2==0]')
>>> factor_pint__smooth_group_order_method7Qpp_(6, 0,  2,2, more_info=True)
(99002, 2, '[n>2][n%2==0]')
>>> factor_pint__smooth_group_order_method7Qpp_(3, 0,  2,2, more_info=True)
(-99003, None, '[2 <= n < 9][n%2==1]')
>>> factor_pint__smooth_group_order_method7Qpp_(5, 0,  2,2, more_info=True)
(-99003, None, '[2 <= n < 9][n%2==1]')
>>> factor_pint__smooth_group_order_method7Qpp_(7, 0,  2,2, more_info=True)
(-99003, None, '[2 <= n < 9][n%2==1]')
>>> factor_pint__smooth_group_order_method7Qpp_(9, 0,  2,2)
0
>>> factor_pint__smooth_group_order_method7Qpp_(9, 1,  2,2)
3
>>> factor_pint__smooth_group_order_method7Qpp_(9, 2,  2,2)
-1
>>> factor_pint__smooth_group_order_method7Qpp_(9, 3,  2,2)
3
>>> factor_pint__smooth_group_order_method7Qpp_(9, 4,  2,2)
3
>>> factor_pint__smooth_group_order_method7Qpp_(9, 5,  2,2)
3
>>> factor_pint__smooth_group_order_method7Qpp_(9, 6,  2,2)
3
>>> factor_pint__smooth_group_order_method7Qpp_(9, 7,  2,2)
-1
>>> factor_pint__smooth_group_order_method7Qpp_(9, 8,  2,2)
3

>>> factor_pint__smooth_group_order_method7Qpp_(9, 1,  2,2, more_info=True)
(99001, 3, 'from:gcd(D,n) or gcd(B-2,n)')
>>> factor_pint__smooth_group_order_method7Qpp_(9, 2,  2,2, more_info=True)
(-99001, None, '[D%n == 0]')
>>> factor_pint__smooth_group_order_method7Qpp_(9, 3,  2,2, more_info=True) #doctest: +ELLIPSIS
(10, 3, (((1, (-1, -3)), ('stage1', (0, (0, 1)), (0, (0, Reproduceable7tmay_prev_oresult(((0, 1),), ...), -1), (1, Reproduceable7tmay_prev_oresult(((-1, -3),), ...), 0)))),))
>>> factor_pint__smooth_group_order_method7Qpp_(9, 4,  2,2, more_info=True)
(99001, 3, 'from:gcd(D,n) or gcd(B-2,n)')
>>> factor_pint__smooth_group_order_method7Qpp_(9, 5,  2,2, more_info=True)
(99001, 3, 'from:gcd(D,n) or gcd(B-2,n)')
>>> factor_pint__smooth_group_order_method7Qpp_(9, 6,  2,2, more_info=True) #doctest: +ELLIPSIS
(10, 3, (((1, (-1, 3)), ('stage1', (0, (0, 1)), (0, (0, Reproduceable7tmay_prev_oresult(((0, 1),), ...), -1), (1, Reproduceable7tmay_prev_oresult(((-1, 3),), ...), 0)))),))
>>> factor_pint__smooth_group_order_method7Qpp_(9, 7,  2,2, more_info=True)
(-99001, None, '[D%n == 0]')
>>> factor_pint__smooth_group_order_method7Qpp_(9, 8,  2,2, more_info=True)
(99001, 3, 'from:gcd(D,n) or gcd(B-2,n)')







>>> #factor_pint__smooth_group_order_method7Qpp_(7*31, 9,  2,2, bound4pow4stage1=16) #old:31
>>> #factor_pint__smooth_group_order_method7Qpp_(7*31, 9,  2,2, bound4pow4stage1=15) #old:0
>>> factor_pint__smooth_group_order_method7Qpp_(7*31, 9,  2,2, more_info=True)
(99001, 7, 'from:gcd(D,n) or gcd(B-2,n)')

>> #factor_pint__smooth_group_order_method7Qpp_(7*31, 20,  2,2, bound4pow4stage1=16)
31
>> #factor_pint__smooth_group_order_method7Qpp_(7*31, 20,  2,2, bound4pow4stage1=15)
0
>>> factor_pint__smooth_group_order_method7Qpp_(7*31, 3,  2,2, bound4pow4stage1=4)
7
>>> factor_pint__smooth_group_order_method7Qpp_(7*31, 3,  2,2, bound4pow4stage1=3)
0


>>> factor_pint__smooth_group_order_method7Qpp_(11*23, 2,  4,4)
-1
>>> factor_pint__smooth_group_order_method7Qpp_(11*23, -2,  4,4)
-1
>>> factor_pint__smooth_group_order_method7Qpp_(11*23, -2,  4,4, more_info=True)
(-99001, None, '[D%n == 0]')
>>> factor_pint__smooth_group_order_method7Qpp_(11*23, 3,  4,4)
23
>>> factor_pint__smooth_group_order_method7Qpp_(11*23, 6,  4,4)
11
>>> factor_pint__smooth_group_order_method7Qpp_(11*23, 45,  4,4) # !! [2,2,3]
(3,)
>>> factor_pint__smooth_group_order_method7Qpp_(11*23, 45,  3,3) # !! [2,3]
(2,)
>>> factor_pint__smooth_group_order_method7Qpp_(11*23, 45,  2,3) # !! [2]++[3]
(1, 2)


>>> factor_pint__smooth_group_order_method7Qpp_(11*23, 16,  4,4) # !! [2,2,3]
(3,)
>>> factor_pint__smooth_group_order_method7Qpp_(11*23, 16,  3,3) # !! [2,3] #old: (2,)  #why???  #bug_fixed_1:goto
0
>>> factor_pint__smooth_group_order_method7Qpp_(11*23, 16,  2,3) # !! [2]++[3] #old: (1, 2)  #why???  #bug_fixed_1:goto
0

>>> factor_pint__smooth_group_order_method7Qpp_(11*23, 16,  3,3, more_info=True, _debug7list_all=True) # !! [2,3] #doctest: +ELLIPSIS
as_dup_ps:[2, 3]
...
as_pts6stage1:[(-1, -16), (-1, 0)]
...
(-23, None, (((2, (-1, 0)), ('stage1', (0, (0, 1)), (4, (2, (-1, 0), -1), None))), ((2, (-2, 0)), ('stage2', (2, (-2, 0)), (4, (2, (-2, 0), -1), None)))))
>>> factor_pint__smooth_group_order_method7Qpp_(11*23, 16,  2,3, more_info=True) # !! [2]++[3]
(-23, None, (((1, (-1, -16)), ('stage1', (0, (0, 1)), (4, (1, (-1, -16), -1), None))), ((2, (-2, 0)), ('stage2', (1, (-2, -16)), (4, (2, (-2, 0), -1), None)))))
>>> 环幂冫二维剩余环扌(MAB:=(11*23,16,1), ab:=(0,1), 6) # == (-1, 0)
(252, 0)
>>> 环乘阶纟幺正点乊二维剩余环扌(MAx:=MAB, ab, 欤待定系数=False)
12
>>> 环幂冫二维剩余环扌(MAB, ab:=(0,1), 2) # == (-1, -16)
(252, 237)
>>> 环幂冫二维剩余环扌(MAB, ab:=(-1,-16), 3) # == (-1, 0)
(252, 0)
>>> 环幂冫二维剩余环扌(MAB:=(M:=11,(16)%M,1), ab:=(0,1), 6) # == (-1, 0)
(10, 0)
>>> 环乘阶纟幺正点乊二维剩余环扌(MAx:=MAB, ab, 欤待定系数=False)
12
>>> 环幂冫二维剩余环扌(MAB:=(M:=23,(16)%M,1), ab:=(0,1), 6) # == (-1, 0)
(22, 0)
>>> 环乘阶纟幺正点乊二维剩余环扌(MAx:=MAB, ab, 欤待定系数=False)
12




>>> [+1+18014398509482483 == 2**2 *3*29*229*521*10429*41603]
[True]
>>> [-1+18014398509482483 == 2*223*40391028048167]
[True]

>>> [+1+18014398509482839 == 2**3 *5*67*173*383*2153*47119]
[True]
>>> [-1+18014398509482839 == 2 *3**2 *17**3 *19*293*36591421]
[True]

>>> [+1+18446744073709552901 == 2*3*7*31*1567*5147*17713*99173]
[True]
>>> [-1+18446744073709552901 == 2**2 *5**2 *13*103*239*257*9181*244297]
[True]

>>> factor_pint__smooth_group_order_method7Qpp_(18014398509482483*18014398509482839, 3,  10429,47119)
18014398509482483
>>> factor_pint__smooth_group_order_method7Qpp_(18014398509482483*18014398509482839, 4,  10429,47119)
18014398509482839


>>> factor_pint__smooth_group_order_method7Qpp_(18014398509482483*18446744073709552901, 3,  17713,99173)
18014398509482483
>>> factor_pint__smooth_group_order_method7Qpp_(18014398509482483*18446744073709552901, 4,  17713,99173)
18446744073709552901








>>> one_trial4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_(77, 35, 1,    1,1)
(901001, 35, None, None, 7)


[n:=M67*35][群规模==61536569536][群规模.最大素因子==1993<11953]
>>> used_As7reduced = set()
>>> kwds = dict(used_As7reduced=used_As7reduced)

>>> from seed.types.Reproduceable import Reproduceable5seq
>>> reproduceable4exps6stage1 = Reproduceable5seq((2, 2, 2, 13, 17, 37, 59, 1993), 0)

>>> one_trial4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_((-1+2**67), 35, 3,    1993,1993, **kwds)  #doctest: +SKIP
>>> one_trial4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_((-1+2**67), 35, 3,    1993,1993, reproduceable4exps6stage1, **kwds)
(701110, 35, (3, 3), (2, 2, 13, 17, 37, 59, 1993))
>>> #used_As7reduced.add(_[1][1])
>>> one_trial4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_((-1+2**67), 35, 4,    1993,1993, reproduceable4exps6stage1, **kwds)
(701110, 35, (13, 13), (2, 2, 2, 13, 17, 37, 59, 1993))
>>> #used_As7reduced.add(_[1][1])
>>> one_trial4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_((-1+2**67), 35, 400,    1993,1993, reproduceable4exps6stage1, **kwds)
(701110, 35, (419, 419), (2, 2, 2, 13, 17, 37, 59, 1993))
>>> #used_As7reduced.add(_[1][1])
>>> sorted(used_As7reduced)
[3, 13, 419]


>>> one_trial4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_((-1+2**67), 35, 40099,    1993,1993, reproduceable4exps6stage1, **kwds)
(701110, 35, (40111, 40111), (2, 2, 2, 13, 37, 59, 1993))
>>> #used_As7reduced.add(_[1][1])


_iter_test4factor7bqf
>>> one_trial4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_((-1+2**67), 35, 83,    1993,1993, reproduceable4exps6stage1, **kwds)
(901111, 35, (83, 83), (2, 13, 17, 37, 59, 1993), 193707721)

























py_adhoc_call:
view ../../python3_src/seed/math/factor_pint/factor_pint__smooth_group_order_method__7py_adhoc_call.py

py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @f
]]]'''#'''
__all__ = r'''
factor_pint__smooth_group_order_method7Pmm_
factor_pint__smooth_group_order_method7Qpp_








iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_
    trials4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_
        iter_trials4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_
            one_trial4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_
                IOps6stage123_4smooth_group_order_method__7BinaryQuadraticForm
                    Ops6stage123_4smooth_group_order_method__7BinaryQuadraticForm


    mk__approximate_qfbclassno5D_
        default_approximate_qfbclassno5D_
        mk__approximate_qfbclassno5D__7pow_







待定系数冫幺正点乊二维剩余环扌
环范冫二维剩余环扌
环乘冫二维剩余环扌
环幂冫二维剩余环扌
环乘阶纟幺正点乊二维剩余环扌
Jacobi_symbol4discriminant5MAB_
discriminant5MAB_
考察冫环乘阶纟幺正点乊随机二维剩余环扌
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.abc.abc__ver1 import abstractmethod, override, ABC
from seed.math.factor_pint.smooth_group_order_method import IOps6stage123_4smooth_group_order_method__7default_mixin
from seed.math.factor_pint.smooth_group_order_method import default_prepare_exps4search6stage1_, default_prepare_exps4search6stage2_
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.dict__add_fmap_filter import fmap4dict_value
    from seed.mapping_tools.dict_op import inv__k2v_to_v2ks
    from seed.math.Jacobi_symbol import Jacobi_symbol

    from seed.tiny_.check import check_type_is, check_int_ge, check_callable, check_may_, check_ABC, check_uint_lt
    from math import gcd
    from decimal import Decimal, Context

    from seed.math.factor_pint.smooth_group_order_method import smooth_group_order_method_
    #def smooth_group_order_method_(bound4stage1, bound4pow4stage1, bound4stage2, diff_one_, detect_, mul_, may_square_, may_pow_, one, pt0, /, *, num_muls_per_detect, imay_detect_period=0, case4xprimes=None, max_size7dense=2049, max_size7physical=65537):
    from seed.math.factor_pint.smooth_group_order_method import search_the_last_used_prime_6stage2_6smooth_group_order_method_, raw_search_the_last_used_prime_6stage2_6smooth_group_order_method_
    #def search_the_last_used_prime_6stage2_6smooth_group_order_method_(bound4stage1, bound4pow4stage1, bound4stage2, offset1, offset2, /):
    #def raw_search_the_last_used_prime_6stage2_6smooth_group_order_method_(bound4stage1, bound4stage2, delta4offset, /):

    from seed.math.hrem_ import hrem_, mk_hrem_

    from seed.helper.repr_input import repr_helper
    from seed.types.CachedProperty import CachedProperty
    from seed.math.BinaryQuadraticForm import mk_one6Qfb_class_group5D_
    from seed.math.BinaryQuadraticForm import nk2D_, D2Qfb7A_ge_
    from seed.math.iter_unsorted_squarefree_uints import iter_unsorted_squarefree_uints_ # kw:to_view_primes => Iter (u, vw4rv_js, vw4rv_ps, imay_new_prime)
    from seed.math.iter_sorted_squarefree_uints import iter_sorted_squarefree_uints_
    #def iter_sorted_squarefree_uints_(may_primes=None, /, *, may_prime2ok_=None, more=False, to_seq6more=False, may_squarefree7resume=None, new_resume=False, neg_resume_ok=False):
    from seed.math.iter_sorted_squarefree_uints import iter_sorted_partial_squarefree_uints7mimic_oldAPI__7odd_only__7basis_eq_fst_16_odd_primes_, iter_sorted_squarefree_uints7mimic_oldAPI__7builtin_data6zpow64_, iter_sorted_squarefree_uints__7chunk_sieve__7mimic_oldAPI__7odd_only_

    from seed.math.II import II
    from seed.math.max_power_of_base_as_factor_of_ import factor_pint_out_power_of_base_
    from seed.tiny_.verify import is_iterable# is_iterator
    from seed.iters.generator_iterator_capturer import GeneratorIteratorCapturer
    from seed.tiny_.containers import mk_tuple
    from math import ceil
#.    from itertools import islice
import numbers
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

__all__
#'''[[[
######################
#copy_from:
#   view script/整数分解牜允许快速求值的多根多项式.py
######################
def 待定系数冫幺正点乊二维剩余环扌(MA, ab, /):
    # [1 == norm(a+b*X) == (a**2-A*a*b+B*b**2)]
    # [1+A*a*b-a**2 == B*b**2]
    # [1+(A*b-a)*a == B*b**2]
    # [(1+(A*b-a)*a)/b**2 == B]
    (M,A) = MA
    (a,b) = ab
    B = ((A*b-a)%M *a + 1) %M * pow(b, -2, M) %M
    return B
def 环范冫二维剩余环扌(MAB, ab, /):
    # [norm(a+b*X) == (a**2-A*a*b+B*b**2)]
    # [norm(a+b*X) == (a**2+b*(-A*a+B*b))]
    (M,A,B) = MAB
    (a,b) = ab
    aA_bB = (-A*a+B*b)%M
    return (a**2+b*aA_bB)%M

def 环乘冫二维剩余环扌(MAB, ab, cd, /):
    # ZZ[X]%(X**2+A*X+B)
    # [(a+b*X)*(c+d*X) == ((a*c-b*d*B)+(b*c+a*d-b*d*A)*X)]
    (M,A,B) = MAB
    (a,b) = ab
    (c,d) = cd
    bd = b*d%M
    ac_bdB = (a*c-bd*B)%M
    ad_bc_bdA = (a*d+b*c-bd*A)%M
    return (ac_bdB, ad_bc_bdA)
def 环幂冫二维剩余环扌(MAB, ab, e, /):
    def mul_(ab, cd, /, *, MAB=MAB):
        return 环乘冫二维剩余环扌(MAB, ab, cd)
    def sq_(ab, /):
        return mul_(ab, ab)
    pw = I = (1,0)
    for b in map(int, f'{e:b}'):
        pw = sq_(pw)
        if b:
            pw = mul_(ab, pw)
    return pw

def 环乘阶纟幺正点乊二维剩余环扌(MAx, ab, /, *, 欤待定系数):
    if 欤待定系数:
        MA = MAx
        B = 待定系数冫幺正点乊二维剩余环扌(MA, ab)
        MAB = (*MA,B)
    else:
        MAB = MAx
    MAB
    def mul_(ab, cd, /, *, MAB=MAB):
        return 环乘冫二维剩余环扌(MAB, ab, cd)
    I = (1,0)
    pw = I
    e = 0
    while 1:
        e += 1
        pw = mul_(ab, pw)
        if pw == I:break
    return e if not 欤待定系数 else (e, B)

def Jacobi_symbol4discriminant5MAB_(MAB, /):
    (M,A,B) = MAB
    D = discriminant5MAB_(MAB)
    return Jacobi_symbol(M, D)
def discriminant5MAB_(MAB, /):
    # ZZ[X]%(X**2+A*X+B)
    (M,A,B) = MAB
    D = (A**2-4*B)%M
    return D
    ##bug:
    assert M&1
    D = (A**2-4*B)%M
    if D&1:
        D += M
    assert D&1 == 0
    D //= 2
    return D
def 考察冫环乘阶纟幺正点乊随机二维剩余环扌(M, abA_ls, /, *, only_exps=False, to_show_Jacobi_symbol=False):
    es = {1}
    if to_show_Jacobi_symbol:
        #e2Js = {1:{0}}
        e2Js = {}
    for (a,b,A) in abA_ls:
        a %= M
        b %= M
        A %= M
        MA = (M,A)
        ab = (a,b)
        (e,B) = 环乘阶纟幺正点乊二维剩余环扌(MA, ab, 欤待定系数=True)
        MAB = (M,A,B)
        if not only_exps:
            yield (e, MAB, ab)
        es.add(e)
        if to_show_Jacobi_symbol:
            J = Jacobi_symbol4discriminant5MAB_(MAB)
            Js = e2Js.setdefault(e, set())
            Js.add(J)
    _es = sorted(es)
    ls = []
    while _es:
        _e = _es.pop()
        if not any(e%_e == 0 for e in ls):
            ls.append(_e)
    es = ls
    yield es
    if to_show_Jacobi_symbol:
        #yield e2Js
        e2Js = fmap4dict_value(frozenset, e2Js)
        js2es = inv__k2v_to_v2ks(e2Js)
        yield js2es
    return
######################
#end-copy_from:
######################
#]]]'''#'''























__all__
#################################
def factor_pint__smooth_group_order_method7Pmm_(n, u0, bound4stage1, bound4stage2=None, /, *, scale4bound4stage2=100, more_info=False, detect_once6stage1=False, bound4pow4stage1=1, case4xprimes=2, max_size7dense=2049, max_size7physical=65537, _debug7list_all=False, **kwds):
    '-> ((offset1, offset2)/{#found-factor-of-(P-1) at stage2#}|(offset1,)/{#found-factor-of-(P-1) at stage1#}|0/{#fail#}|nontrivial_factor/uint{>0}) # (P-1) method'
    ######################
    check_int_ge(2, n)
    check_type_is(int, u0)
    check_int_ge(1, bound4stage1)
    check_int_ge(1, bound4pow4stage1)
    check_int_ge(1, scale4bound4stage2)
    if bound4stage2 is None:
        bound4stage2 = scale4bound4stage2*bound4stage1
    check_int_ge(1, bound4stage2)

    ######################
    num_muls_per_detect = 10*n.bit_length()
    imay_detect_period = -1 if detect_once6stage1 else 0
    one = 1
    pt0 = u0%n
    ######################
    def diff_one_(u, /):
        return (u-1)%n
    def detect_(u, /):
        v = gcd(u, n)
        if v == 1:
            return (-1, None)
        if v == n:
            return (+1, None)
        if 1 < v < n:
            return (0, v)
        raise 000
    detect_
    def mul_(a, b, /):
        return a*b%n
    def square_(a, /):
        return pow(a, 2, n)
    def pow_(a, e, /):
        return pow(a, e, n)
    ######################
    r = smooth_group_order_method_(bound4stage1, bound4pow4stage1, bound4stage2, diff_one_, detect_, mul_, square_, pow_, one, pt0, num_muls_per_detect=num_muls_per_detect, imay_detect_period=imay_detect_period, case4xprimes=case4xprimes, max_size7dense=max_size7dense, max_size7physical=max_size7physical, _debug7list_all=_debug7list_all, **kwds)
    return _postprocess(n, r, more_info)
#end-def factor_pint__smooth_group_order_method7Pmm_(n, u0, bound4stage1, bound4stage2=None, /, *, more_info=False, detect_once6stage1=False, bound4pow4stage1=1, case4xprimes=2, max_size7dense=2049, max_size7physical=65537, _debug7list_all=False, **kwds):
#################################
def _postprocess(n, r, more_info, /):
    if more_info:
        return r

    match r:
        case ((10|20), int(nontrivial_factor), _):
            # +10|+20
            assert 0 < nontrivial_factor < n
            assert n%nontrivial_factor == 0
            return nontrivial_factor
        #case ((-11|-22|-23), None, _):
            #case (ocase, None, _) if ocase < 0:
        case (-23, None, _):
            return 0
        case (-11, None, [((offset1, _), _)]):
            return (offset1,)
        case (-22, None, [((offset1, _), _), ((offset2, _), _)]):
            return (offset1, offset2)
        case _:
            raise TypeError(r)
    raise 000
#################################







#################################
def _iter_search_exceptional4factor_pint__smooth_group_order_method7Pmm_(n, u0s, /, *args, **kwds):
    return _iter_search_exceptional(factor_pint__smooth_group_order_method7Pmm_, n, u0s, *args, **kwds)
def _iter_search_exceptional4factor_pint__smooth_group_order_method7Qpp_(n, u0s, /, *args, **kwds):
    return _iter_search_exceptional(factor_pint__smooth_group_order_method7Qpp_, n, u0s, *args, **kwds)
def _iter_search_exceptional(f, n, u0s, /, *args, **kwds):
    #十分稀罕，必须 mul_order4pt0{@p},mul_order4pt0{@q} 的 最大素因子 恰好相同
    for u0 in u0s:
        r = f(n, u0, *args, **kwds)
        match r:
            case int(u) if u >= 0:
                pass
            case _:
                yield (u0, r)
def _iter_search_mul_order4X_4factor_pint__smooth_group_order_method7Qpp_(n, u0s, /):
    from seed.math.factor_pint.factor_pint__naive_brute_force import factor_pint__naive_brute_force_, iter_factor_pint__naive_brute_force_
    hrem4N_ = mk_hrem_(n)
    one = (1, 0) # == 1+0*X == 1
    pt0 = (0, 1) # == 0+1*X == X
    # [norm(pt0) == 1]
    for u0 in u0s:
        B = hrem4N_(u0)
        #D = hrem4N_(B**2-4)
        mul_order4pt0 = mul_order4X = 环乘阶纟幺正点乊二维剩余环扌(MAx:=(n,B,1), pt0, 欤待定系数=False)
        p2e = factor_pint__naive_brute_force_(mul_order4pt0)
        yield (u0, mul_order4pt0, p2e)
    ######################

#################################


__all__
#################################
def factor_pint__smooth_group_order_method7Qpp_(n, u0, bound4stage1, bound4stage2=None, /, *, scale4bound4stage2=100, more_info=False, detect_once6stage1=False, bound4pow4stage1=1, case4xprimes=2, max_size7dense=2049, max_size7physical=65537, _debug7list_all=False, **kwds):
    '-> ((offset1, offset2)/{#found-factor-of-(P-1|P+1) at stage2#}|(offset1,)/{#found-factor-of-(P-1|P+1) at stage1#}|-1/{#[(u0**2-4)%n==0]#}||0/{#fail#}|nontrivial_factor/uint{>0}) # (P+1) method # NOTE:[MAYBE RETURN -1]'
    ######################
    r'''[[[
    证明:只需B，无需C:
    #see:待定系数冫幺正点乊二维剩余环扌
    [gcd(b,n)==1][norm((c+b*X)%{n,(X**2+B*X+C)}) == 1]:
        !! [gcd(b,n)==1]
        [b=!=0] # [c==0]:ok
        !! [norm((c+b*X)%{n,(X**2+B*X+C)}) == 1]
        [1 == norm(c+b*X) == (c**2-B*c*b+C*b**2)]

        [Y:=(c+b*X)]
        [X==(Y-c)/b]
        # --> Y%(((Y-c)/b)**2+B*(Y-c)/b+C)
        # pt0:(c+b*X) --> (0+1*Y)
        [(((Y-c)/b)**2+B*(Y-c)/b+C)
        == ((Y-c)**2+B*(Y-c)*b+C*b**2)/b**2
        == ((Y**2-2*c*Y+c**2)+(B*b*Y-B*c*b)+C*b**2)/b**2
        == ((Y**2+(B*b-2*c)*Y)+(c**2-B*c*b+C*b**2))/b**2
        == ((Y**2+(B*b-2*c)*Y)+1)/b**2
            # C --> 1
        ]
        ==>> fixed:[C{Y}:=1][pt0{Y}:=(0,1)]
        ==>> the only parameter:B{Y}
    #]]]'''#'''
    ######################
    check_int_ge(2, n)
    # [n >= 2]
    check_type_is(int, u0)
    check_int_ge(1, bound4stage1)
    check_int_ge(1, bound4pow4stage1)
    check_int_ge(1, scale4bound4stage2)
    if bound4stage2 is None:
        bound4stage2 = scale4bound4stage2*bound4stage1
    check_int_ge(1, bound4stage2)
    ######################
    # [n >= 2]
    if n&1 == 0:
        # [n%2==0]
        if n == 2:
            return 0 if not more_info else (-99002, None, '[n==2]')
        # [n > 2]
        return 2 if not more_info else (+99002, 2, '[n>2][n%2==0]')
    if n < 9:
        return 0 if not more_info else (-99003, None, '[2 <= n < 9][n%2==1]')
    check_int_ge(9, n)
    if not n&1 == 1:raise ValueError
    # [n >= 9][n%2==1] # n_is_odd_ge9
    ######################
    num_muls_per_detect = 10*n.bit_length()
    imay_detect_period = -1 if detect_once6stage1 else 0
    # [pt == (a,b) === (a+b*X)%{n,1+B*X+X**2}]
    hrem4N_ = mk_hrem_(n)
    one = (1, 0) # == 1+0*X == 1
    pt0 = (0, 1) # == 0+1*X == X
    # [norm(pt0) == 1]
    B = hrem4N_(u0)
    ######################
    D = hrem4N_(B**2-4)
    tm = _4D_01(n, u0, B, D, more_info)
    if tm:
        [result] = tm
        return result
    ######################



    ######################
    def diff_one_(ab, /):
        (a, b) = ab
        return (hrem4N_(a-1), b)
    def detect_(ab, /):
        return _detect4Qpp_(n, ab)
    def mul_(ab, cd, /):
        #环乘冫二维剩余环扌
        (a,b) = ab
        (c,d) = cd
        bd = hrem4N_(b*d)
        ac_bd1 = hrem4N_(a*c-bd*1)
        ad_bc_bdB = hrem4N_(a*d+b*c-bd*B)
        return (ac_bd1, ad_bc_bdB)
    def square_(ab, /):
        (a,b) = ab
        bd = hrem4N_(b**2)
        ac_bd1 = hrem4N_(a**2-bd*1)
        ad_bc_bdB = hrem4N_(a*b*2-bd*B)
        return (ac_bd1, ad_bc_bdB)
    ######################
    r = smooth_group_order_method_(bound4stage1, bound4pow4stage1, bound4stage2, diff_one_, detect_, mul_, square_, may_pow_:=None, one, pt0, num_muls_per_detect=num_muls_per_detect, imay_detect_period=imay_detect_period, case4xprimes=case4xprimes, max_size7dense=max_size7dense, max_size7physical=max_size7physical, _debug7list_all=_debug7list_all, **kwds)
    return _postprocess(n, r, more_info)
def _4D_01(n, u0, B, D, more_info, /):
    def _4D_0(D, /):
        if abs(B) == 2:
            return -1
        if D == 0:
            v = gcd(B-2, n)
            if 1 < v < n: return v
            return -1
        v = gcd(D, n)
        if v == 1:return 0
        if 1 < v < n: return v
        raise 000
    def _4D_1(D, /):
        v = _4D_0(D)
        if v == 0:return
        if v == -1:
            # [D%n == 0]
            assert D == 0, (n, u0, B, D)
            yield -1 if not more_info else (-99001, None, '[D%n == 0]')
            return
        if 1 < v < n:
            yield v if not more_info else (+99001, v, 'from:gcd(D,n) or gcd(B-2,n)')
            return
        raise 000

    tm = [*_4D_1(D)]
    return tm
def _detect4Qpp_(n, ab, /):
    # !! [norm(pt0) == 1]
    # !! [ab == (-one+pt0**exp)]
    # [norm(one+ab) == 1]
    # [(a, b) := ab]
    # [a1 := 1+a]
    # [1 == norm(a1+b*X) == (a1**2-B*a1*b+1*b**2)]
    # [[b==0] -> [abs(1+a) == 1]]
    # [[b==0] -> [(1+a) <- {-1,+1}]]
    # [[b==0] -> [a <- {-2,0}]]
    # [[a==0] -> [b <- {-1,+1}]]

    #(a, b) = ab
    us = tuple(filter(bool, ab))
    match us:
        case (a,b):
            #if all(a,b):
            v = gcd(a*b, n)
            if v == 1: return (-1, None)
            if 1 < v < n: return (0, v)
            assert v == n, (n, ab, v)
            v = gcd(a, n)
            if 1 < v < n: return (0, v)
            assert -n < a < n, (n, ab, v)
            assert -n < b < n, (n, ab, v)
            assert not 0 == a, (n, ab, v)
            assert not 0 == b, (n, ab, v)
            assert 1 < v < n, (n, ab, v)
            raise 000
        case ():
            #if not any(a,b):
            assert ab == (0,0), (n, ab)
            return (+1, None)
        case [u]:
            #[u] = filter(bool, ab)
            # !! [[b==0] -> [a <- {-2,0}]]
            # !! [[a==0] -> [b <- {-1,+1}]]
            # !! [n >= 9][n%2==1] # n_is_odd_ge9
            # [ab <- {(-2,0), (0,-1), (0,+1)}]
            v = gcd(u, n)
            if v == 1: return (-1, None)
            assert ab in [(-2,0), (0,-1), (0,+1)], (n, ab, u, v)
            raise 000
            if 1 < v < n: return (0, v)
            assert -n < u < n, (n, u)
            assert not 0 == u, (n, u)
            #if v == n:
            raise 000
        case _:
            raise 000
    raise 000
    r'''[[[
    factor_pint__smooth_group_order_method7Qpp_(11*23, 16,  3,3) # !! [2,3] #old: (2,)  #why???
    factor_pint__smooth_group_order_method7Qpp_(11*23, 16,  2,3) # !! [2]++[3] #old: (1, 2)  #why???
    #bug_fixed_1:here
    why?
        since:
            ... ...
            for x in ab:
                _v = gcd(x, n)
                ...
                if _v == 1:
                    v == 1 #bug!!!
            if v == n: return (+1, None)
    #]]]'''#'''
_detect4Qpp_
#end-def factor_pint__smooth_group_order_method7Qpp_
#################################





#################################
__all__
#################################
class _FoundNontrivialFactor(BaseException):pass
class _IsPrime(BaseException):pass
def _iter__k4D__min_A__pairs_(n, case4ks4D, emay_signed_prev_k4D__or__k4D__min_A__pairs, /):
    '#[case4ks4D == (0/unsorted-squarefree|1/sorted-squarefree|2/sorted-odd-partial_squarefree{only-resp.to:3,5,7..59}|3/builtin_data6zpow64|4/sorted-odd-chunk_sieve)]'
    #kw:to_sorted_ks4D --> case4ks4D
    if is_iterable(emay_signed_prev_k4D__or__k4D__min_A__pairs):
        k4D__min_A__pairs = emay_signed_prev_k4D__or__k4D__min_A__pairs
        if not 0 == case4ks4D:
            #if to_sorted_ks4D:
            pass;k4D__min_A__pairs
        return (yield from k4D__min_A__pairs)
    emay_signed_prev_k4D = emay_signed_prev_k4D__or__k4D__min_A__pairs
    if ... is emay_signed_prev_k4D:
        more_kwds = {}
    elif isinstance(emay_signed_prev_k4D, int):
        signed_prev_k4D = emay_signed_prev_k4D
        if signed_prev_k4D == 0:raise ValueError('signed_prev_k4D SHOULD NOT BE 0')
        more_kwds = dict(may_squarefree7resume=abs(signed_prev_k4D), new_resume=(signed_prev_k4D < 0))
    else:
        raise TypeError(emay_signed_prev_k4D__or__k4D__min_A__pairs)
    more_kwds
    prime2ok_ = lambda p:p>2
    min_A = 3
    match case4ks4D:
        #if to_sorted_ks4D:
        case 0:
            it = iter_unsorted_squarefree_uints_(to_view_primes=True, may_prime2ok_=prime2ok_, **more_kwds)
            #for (k4D, vw4rv_js, vw4rv_ps, imay_new_prime) in it:
        case 1:
            it = iter_sorted_squarefree_uints_(more=True, may_prime2ok_=prime2ok_, **more_kwds)
            #for (k4D, js4ps, ps, imay_new_prime) in it:
        case 2:
            it = iter_sorted_partial_squarefree_uints7mimic_oldAPI__7odd_only__7basis_eq_fst_16_odd_primes_(more=True, may_prime2ok_=prime2ok_, **more_kwds)
            #for (k4D, _None, _None, -1) in it:
        case 3:
            it = iter_sorted_squarefree_uints7mimic_oldAPI__7builtin_data6zpow64_(more=True, may_prime2ok_=prime2ok_, **more_kwds)
            #for (k4D, _None, _None, -1) in it:
        case 4:
            it = iter_sorted_squarefree_uints__7chunk_sieve__7mimic_oldAPI__7odd_only_(more=True, may_prime2ok_=prime2ok_, **more_kwds)
            #for (k4D, None, ps4u, imay_new_prime) in it:
        case _:
            raise ValueError(case4ks4D)
    it
    for (k4D, asif_js, asif_ps, imay_new_prime) in it:
        ##################
        match imay_new_prime:
            case -1:
                pass
            case new_prime:
                if n%new_prime == 0:
                    if n == new_prime:
                        raise _IsPrime(n)
                    raise _FoundNontrivialFactor(n, new_prime)
        ##################
        yield (k4D, min_A)

def iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_(n, emay_signed_prev_k4D__or__k4D__min_A__pairs, bound4stage1, bound4stage2=None, may_reproduceable4exps6stage1=None, may_reproduceable4exps6stage2=None, /, *, scale4bound4stage2=100, quiet_level=0, case4xprimes=None, stop_if_found_exps7key=False, try_resting_=None, case4ks4D=0, exp4pt0=1, imay_sz4giant_step=-1, info8qfbclassno4D=None):
    r'''[[[
    '#[case4ks4D == (0/unsorted-squarefree|1/sorted-squarefree|2/sorted-odd-partial_squarefree{only-resp.to:3,5,7..59})]'
    #]]]'''#'''
    try_resting_ = try_resting_ if not None is try_resting_ else lambda:None
    check_uint_lt(4, quiet_level)
    no_stage2 = not imay_sz4giant_step == -1
    t = _head4trial4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_(n, _k4D:=1, bound4stage1, bound4stage2, may_reproduceable4exps6stage1, may_reproduceable4exps6stage2, scale4bound4stage2, case4xprimes, no_stage2)
    match t:
        case (-101111, _k4D, _ops6stage12, _D, max4exp6stage1, max4exp6stage2, reproduceable4exps6stage1, reproduceable4exps6stage2):
            pass
        case _:
            raise Exception(t)

    if 1:
        (bound4stage1, bound4stage2, may_reproduceable4exps6stage1, may_reproduceable4exps6stage2) = (max4exp6stage1, max4exp6stage2, reproduceable4exps6stage1, reproduceable4exps6stage2)

    quiet7outside = bool(quiet_level)
    quiet7inside = quiet7outside and not stop_if_found_exps7key
    for (k4D, min_A) in _iter__k4D__min_A__pairs_(n, case4ks4D, emay_signed_prev_k4D__or__k4D__min_A__pairs):
        try_resting_()
        it = iter_trials4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_(n, k4D, min_A, bound4stage1, bound4stage2, may_reproduceable4exps6stage1, may_reproduceable4exps6stage2, scale4bound4stage2=scale4bound4stage2, used_As7reduced=None, quiet=quiet7inside, exp4pt0=exp4pt0, imay_sz4giant_step=imay_sz4giant_step, info8qfbclassno4D=info8qfbclassno4D)
        ######################
        if not stop_if_found_exps7key:
            # [[quiet7inside] <-> [quiet_level > 0]]
            result4trials = yield from it
        else:
            # ++kw:stop_if_found_exps7key
            # [not quiet7inside]
            assert not quiet7inside
            gnr = GeneratorIteratorCapturer(it)
            for tmp in gnr:
                if not quiet7outside:yield tmp
                match tmp:
                    case (result4one_trial, (group_order7guess, ez4group_order7guess, odd4group_order7guess, [])):
                        pass
                    case (result4one_trial, (group_order7guess, ez4group_order7guess, odd4group_order7guess, tmp__known_exps7key)):
                        known_exps7key = tuple(sorted(tmp__known_exps7key))
                        assert len(known_exps7key) > 0
                        # !! stop_if_found_exps7key
                        return (result4one_trial, (group_order7guess, ez4group_order7guess, odd4group_order7guess, known_exps7key))
                    case _:
                        raise Exception(tmp)
            gnr
            [result4trials] = gnr.get_tmay_result()
        result4trials
        ######################
        if quiet_level < 2:
            yield result4trials
        (result4one_trial, info4group_order) = result4trials
        (group_order7guess, ez4group_order7guess, odd4group_order7guess, known_exps7key) = info4group_order
        ######################
        if 2 == quiet_level < 3:
            match result4one_trial:
                case (201100|401100|601100, *_):
                    # fail or handled
                    pass
                case _:
                    yield result4trials
        ######################
        match result4one_trial:
            case (201100|401100|601100, *_):
                # fail or handled
                pass#continue
            case (901001|901111, *_):
                # ok
                return result4trials
            case (301110|501110|701110, *_):
                # found more_exps7key
                if stop_if_found_exps7key:
                    return result4trials
                pass#continue
            case _:
                raise Exception(result4one_trial)
        ######################

def trials4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_(n, k4D, min_A, bound4stage1, bound4stage2=None, may_reproduceable4exps6stage1=None, may_reproduceable4exps6stage2=None, /, *, scale4bound4stage2=100, used_As7reduced=None, exp4pt0=1, imay_sz4giant_step=-1, info8qfbclassno4D=None):
    it = iter_trials4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_(n, k4D, min_A, bound4stage1, bound4stage2, may_reproduceable4exps6stage1, may_reproduceable4exps6stage2, scale4bound4stage2=scale4bound4stage2, used_As7reduced=used_As7reduced, quiet=True, exp4pt0=exp4pt0, imay_sz4giant_step=imay_sz4giant_step, info8qfbclassno4D=info8qfbclassno4D)
    try:
        r = next(it)
    except StopIteration as exc:
        return exc.value
    else:
        # !! [quiet:=True]
        raise Exception(r)
def iter_trials4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_(n, k4D, min_A, bound4stage1, bound4stage2=None, may_reproduceable4exps6stage1=None, may_reproduceable4exps6stage2=None, /, *, scale4bound4stage2=100, used_As7reduced=None, quiet=False, try_resting_=None, case4xprimes=None, exp4pt0=1, imay_sz4giant_step=-1, info8qfbclassno4D=None):
    '-> (result4one_trial, info4group_order)/(result{one_trial4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_()}, (group_order7guess, ez4group_order7guess, odd4group_order7guess, known_exps7key))'
    try_resting_ = try_resting_ if not None is try_resting_ else lambda:None
    if used_As7reduced is None:
        used_As7reduced = set()
    ######################
    group_order7guess = 1
    777;ez4group_order7guess = 0
    777;odd4group_order7guess = 1
    777;known_exps7key = []
    ######################
    def f_(t, /):
        nonlocal known_exps7key
        known_exps7key.sort()
        known_exps7key = tuple(known_exps7key)
        return hf_(t)
    def hf_(t, /):
        return (t, (group_order7guess, ez4group_order7guess, odd4group_order7guess, known_exps7key))
    def g_(more_exps7key, /):
        nonlocal group_order7guess, ez4group_order7guess, odd4group_order7guess# known_exps7key
        more_group_order7guess = II(more_exps7key)
        (more_ez4group_order7guess, more_odd4group_order7guess) = factor_pint_out_power_of_base_(2, more_group_order7guess)
        group_order7guess *= more_group_order7guess
        777;ez4group_order7guess += more_ez4group_order7guess
        777;odd4group_order7guess *= more_odd4group_order7guess
        777;known_exps7key.extend(more_exps7key)
        pass
    ######################
    no_stage2 = not imay_sz4giant_step == -1
    t = _head4trial4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_(n, k4D, bound4stage1, bound4stage2, may_reproduceable4exps6stage1, may_reproduceable4exps6stage2, scale4bound4stage2, case4xprimes, no_stage2)
    match t:
        case (-101111, k4D, ops6stage123, D, max4exp6stage1, max4exp6stage2, reproduceable4exps6stage1, reproduceable4exps6stage2):
            pass
        case (901001, *_):
            return f_(t)
        case _:
            raise Exception(t)
    #########
    min_A
    #########
    while 1:
        try_resting_()
        ######################
        (A_A, pt0) = _neck4trial4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_(D, min_A, exp4pt0)
        (A7repr, A7reduced) = A_A
        assert A7repr >= min_A
        777;min_A = 1+A7repr
        if A7reduced in used_As7reduced:
            continue
        # [not A7reduced in used_As7reduced]
        ######################
        if pt0.eq_one_(): continue
        pt1 = pt0**odd4group_order7guess
        if pt1.eq_one_(): continue
        for _ in range(ez4group_order7guess):
            # [one =!= pt1]
            if pt1.is_ambiguous_form_():
                pt7ambiguous = pt1
                t = _tail4trial4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_(n, k4D, A_A, D, _exps7key:=(), _pt0:=pt7ambiguous, pt7ambiguous)
                t;break
            # [not pt1.is_ambiguous_form_()]
            # [one =!= pt1**2]
            pt1 **= 2
            # [one =!= pt1]
            if pt1.eq_one_(): raise 000
        else:
            # [one =!= pt1]
            if pt1.eq_one_(): raise 000
            # [one =!= pt1 == pt0**group_order7guess]
            # [not A7reduced in used_As7reduced]
            t = _body4trial4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_(n, k4D, A_A, ops6stage123, D, max4exp6stage1, max4exp6stage2, reproduceable4exps6stage1, reproduceable4exps6stage2, _pt0:=pt1, used_As7reduced, imay_sz4giant_step, info8qfbclassno4D)
            # [A7reduced in used_As7reduced]
            assert A7reduced in used_As7reduced
            t
        t # from "break" or "else@for_loop"
        if not quiet:
            yield hf_(t)
        match t:
            case (201100|601100, k4D, A_A):
                # fail
                return f_(t)
            case (401100, k4D, A_A):
                # handled
                # 401100 <==> before call has:[A7reduced in used_As7reduced]
                # _L
                raise 000
            case (901111, k4D, A_A, more_exps7key, nontrivial_factor4n):
                if more_exps7key:g_(more_exps7key)
                return f_(t)
            case (301110|501110|701110, k4D, A_A, more_exps7key):
                if more_exps7key:g_(more_exps7key)
                pass
            case _:
                raise Exception(t)
        ######################

def one_trial4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_(n, k4D, min_A, bound4stage1, bound4stage2=None, may_reproduceable4exps6stage1=None, may_reproduceable4exps6stage2=None, /, *, scale4bound4stage2=100, used_As7reduced=None, case4xprimes=None, exp4pt0=1, imay_sz4giant_step=-1, info8qfbclassno4D=None):
    #case : regex"[1-9]0[01]\{4}"
    'n/uint{>0}{%2==1} -> k4D/uint{>0}{%2==1} -> min_A -> bound4stage1 -> may bound4stage2 -> (case, k4D, may A_A, ?may exps7key?, ?may nontrivial_factor4n?)/((901001, k4D, None, None, nontrivial_factor4n)|(201100|401100|601100, k4D, A_A)|(301110|501110|701110, k4D, A_A, exps7key)|(901111, k4D, A_A, exps7key, nontrivial_factor4n)) # [A_A := (A7repr, A7reduced)]'

    ######################
    # factor (n*k4D)
    ######################
    # [n > 0][n%2==1]
    # [k4D > 0][k4D%2==1]
    # [1==gcd(k4D,n)]
    # !! [平方因子基本不影响 群规模耂最大素因子]
    # => 最好有:[is_squarefree_(k4D)] # see:iter_unsorted_squarefree_uints_()
    # [D := -k4D*n if k4D*n%4==3 else -4*k4D*n]
    # [min_A >= 3]
    # [A :: prime][A >= min_A >= 3][Jacobi_symbol(A;D) == +1]
    # !! [(1+8*_)型素数 开平方更难:需要 平方非剩余]
    # => 最好避免:[A%8 == 1] # ++kw:avoid_A_mod8_eq1
    # => 或者:[gde_(2;A-1) <= max_ez4Amm]
    #       # O((log2(p)+log2(p///odd4p)**(3/2))*log2(p)**2)
    # [B**2 =[%A]= D][B%2 == D%2]
    # !! [A%2 == 1]
    # => [%A范围内B只有一个解]
    # !! [B%2 == D%2]
    # => [%(2*A)范围内B只有一个解]
    # !! 调整冫二二型中部牜保持等价类
    # => [等效步长:(2*A)]
    # => [只有一个不等效B]
    # => [B{A}唯一]
    ######################
    no_stage2 = not imay_sz4giant_step == -1
    t = _head4trial4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_(n, k4D, bound4stage1, bound4stage2, may_reproduceable4exps6stage1, may_reproduceable4exps6stage2, scale4bound4stage2, case4xprimes, no_stage2)
    match t:
        case (-101111, k4D, ops6stage123, D, max4exp6stage1, max4exp6stage2, reproduceable4exps6stage1, reproduceable4exps6stage2):
            pass
        case (901001, *_):
            return t
        case _:
            raise Exception(t)
    (A_A, pt0) = _neck4trial4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_(D, min_A, exp4pt0)
    t = _body4trial4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_(n, k4D, A_A, ops6stage123, D, max4exp6stage1, max4exp6stage2, reproduceable4exps6stage1, reproduceable4exps6stage2, pt0, used_As7reduced, imay_sz4giant_step, info8qfbclassno4D)
    return t
def _head4trial4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_(n, k4D, bound4stage1, bound4stage2, may_reproduceable4exps6stage1, may_reproduceable4exps6stage2, scale4bound4stage2, case4xprimes, no_stage2, /):
    check_int_ge(1, bound4stage1)
    check_int_ge(1, scale4bound4stage2)
    if bound4stage2 is None:
        bound4stage2 = scale4bound4stage2*bound4stage1
    check_int_ge(1, bound4stage2)

    max4exp6stage1 = bound4stage1
    max4exp6stage2 = bound4stage2
    ######################
    try:
        ops6stage123 = Ops6stage123_4smooth_group_order_method__7BinaryQuadraticForm(n, k4D)
        D = ops6stage123.D
    except ValueError as exc:
        match exc.args:
            case (_n, _k4D, ft4n):
                assert _n == n
                assert _k4D == k4D
                if 1 < ft4n < n:
                    assert n%ft4n == 0
                    return (901001, k4D, None, None, ft4n)
                if 1 == ft4n:raise 000
                assert n == ft4n
                raise
        raise
    ops6stage123
    D
    assert k4D == ops6stage123.k4D
    ######################
    #.reproduceable4exps6stage1 = ops6stage123.prepare_exps4search6stage1_(max4exp6stage1, may_reproduceable4exps6stage1)
    #.reproduceable4exps6stage2 = ops6stage123.prepare_exps4search6stage2_(max4exp6stage1, max4exp6stage2, may_reproduceable4exps6stage2)
    reproduceable4exps6stage1 = default_prepare_exps4search6stage1_(ops6stage123, max4exp6stage1, case4xprimes=case4xprimes) if None is may_reproduceable4exps6stage1 else may_reproduceable4exps6stage1
    if no_stage2:
        reproduceable4exps6stage2 = 'no_stage2'
    else:
        reproduceable4exps6stage2 = default_prepare_exps4search6stage2_(ops6stage123, max4exp6stage1, max4exp6stage2, case4xprimes=case4xprimes) if None is may_reproduceable4exps6stage2 else may_reproduceable4exps6stage2
    return (-101111, k4D, ops6stage123, D, max4exp6stage1, max4exp6stage2, reproduceable4exps6stage1, reproduceable4exps6stage2)
def _neck4trial4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_(D, min_A, exp4pt0, /):
    ######################
    #bug:A7repr = bqf7reduced.binary_quadratic_form7repr.A
    (A7repr, bqf7reduced) = D2Qfb7A_ge_(D, min_A, avoid_A_mod8_eq1=True, with_A7repr=True)
    A7reduced = bqf7reduced.binary_quadratic_form7reduced.A
    A_A = (A7repr, A7reduced)
    A_A
    bqf7reduced
    ######################
    #输出A7repr，以便外部步进
    #输出A7reduced，以便考察重复性
    ######################
    pt0 = bqf7reduced**exp4pt0
    return (A_A, pt0)

def mk__approximate_qfbclassno5D_(info8qfbclassno4D, /):
    match info8qfbclassno4D:
        case None:
            approximate_qfbclassno5D_ = default_approximate_qfbclassno5D_
        case f if callable(f):
            approximate_qfbclassno5D_ = f
        case ('pow', numbers.Rational() as exp8D2qfbclassno) if 0 < exp8D2qfbclassno < 1:
            approximate_qfbclassno5D_ = mk__approximate_qfbclassno5D__7pow_(exp8D2qfbclassno)
        case _:
            raise Exception(info8qfbclassno4D)
    return approximate_qfbclassno5D_

def mk__approximate_qfbclassno5D__7pow_(exp8D2qfbclassno, /):
    assert 0 < exp8D2qfbclassno < 1
    ctx = Context()
    exp7float = Decimal(exp8D2qfbclassno, ctx)
    def approximate_qfbclassno5D_(D, /):
        #.L = D.bit_length()
        #.nb = max(128, L)
        #.ez = L -nb
        #.h = D >> ez
        #.h = float(h)
            #view ../../python3_src/seed/seq_tools/bisearch.py
            #   [min_u7OverflowError == (-1+2**54)*2**970]
        neg_D7float = -Decimal(D, ctx)
        try:
            cls_no7approx7float = (neg_D7float**exp7float)
        except ArithmeticError as exc:
            #decimal.InvalidOperation
            #fixed bug: D7float --> neg_D7float
            raise type(exc)((exc, neg_D7float, exp7float))
        cls_no7approx = max(1, ceil(cls_no7approx7float))
        check_int_ge(1, cls_no7approx)
        return cls_no7approx
    return approximate_qfbclassno5D_
#def default_approximate_qfbclassno5D_(D, /):
default_approximate_qfbclassno5D_ = mk__approximate_qfbclassno5D__7pow_(0.441)
r'''[[[
0.441
<<==:
[[

群规模估值:用于:群规模计算牜大小步碰撞.偏移量
放大后,D5m_(m),log(qfbclassno(D))/log(D)
{D5m_(m)=
  ;my(r=m%4)
  ;if(m >= 0
    ,error("[m >= 0]")
    ,if(r==0
      ,error("[m%4 == 0]")
      ,if(r==1
        ,return(m)
        ,return(4*m)
      )
    )
  )
}
{show_mean4log4qfbclassno4D5ms_(min4m,max4m,m0=1)=
  ;my(rs=List())
  ;forsquarefree(x=min4m,max4m
    ,my(m=x[1],pes4m=x[2],D=D5m_(m*m0))
    ;listput(~rs,2*log(qfbclassno(D))/log(-D))
  )
  ;rs=Vec(rs)
  ;my(mean=vecsum(rs)/#rs)
  ;my(min4err=vecmin(abs(rs-vector(#rs,X,mean))))
  ;return([mean,min4err,rs,vecsort(rs)])
}

nextprime(29000)
  29009
show_mean4log4qfbclassno4D5ms_(-100,-1,29009)[1..2]
  [0.86057613929243587453198509923605952986, 0.00048598564436822031709086749447615410408]
show_mean4log4qfbclassno4D5ms_(-1000,-1,29009)[1..2]
  [0.88132235105307186709414489010594722033, 1.0075223547532987208334929578146912105 E-5]
show_mean4log4qfbclassno4D5ms_(-1000,-500,29009)[1..2]
  [0.88678369407877883727920995464530258551, 3.7030643143200225322394714450761370057 E-5]
show_mean4log4qfbclassno4D5ms_(-1000,-800,29009)[1..2]
  [0.88735634419363160908152515022158746100, 0.00018460169130574102234133339968835027838]
show_mean4log4qfbclassno4D5ms_(-1000,-900,29009)[1..2]
  [0.88645103358968659311113601851182759324, 0.0010899122952507569927304651094482180382]

nextprime(1+29009)
  29017
show_mean4log4qfbclassno4D5ms_(-100,-1,29017)[1..2]
  [0.86547168673198083332761475166637102422, 0.0028426643805527096384356881750204851694]
show_mean4log4qfbclassno4D5ms_(-1000,-1,29017)[1..2]
  [0.88210856579607417616843267386737811775, 8.9958525945190972352785429741321448196 E-6]
show_mean4log4qfbclassno4D5ms_(-1000,-500,29017)[1..2]
  [0.88672681089441901055251810956622127197, 0.00031263236228346922681896176387514849489]
show_mean4log4qfbclassno4D5ms_(-1000,-800,29017)[1..2]
  [0.88963352678946504338299476944859876034, 0.00080886706885714751257312444407259261552]
show_mean4log4qfbclassno4D5ms_(-1000,-900,29017)[1..2]
  [0.89200732280371416441795426296295532700, 0.00014284098049500096411496212684712980606]
show_mean4log4qfbclassno4D5ms_(-1000-3000,-100-3000,29017)[1..2]
  [0.89607277654108153088233740317878042093, 0.00058272664684526994765476960572833814668]

[[m::squarefree{<0}] -> [0.882 ~= MEAN{2*log(qfbclassno(D))/log(-D) | [k::squarefree{>0}][1==gcd(m,k)][D:=D5m_(k*m)]}]]
[qfbclassno(D) ~= (-D)**0.441]
  以此为基点，使用 大小步碰撞 探测 给定bqf乘阶
  stage3:bqf:=pt0|pt1
baby_steps_giant_steps_method
]]
#]]]'''#'''

def _body4trial4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_(n, k4D, A_A, ops6stage123, D, max4exp6stage1, max4exp6stage2, reproduceable4exps6stage1, reproduceable4exps6stage2, pt0, used_As7reduced, imay_sz4giant_step, info8qfbclassno4D, /):
    #one_trial4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_
    #iter_trials4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_
    #   trials4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_
    #   iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_

    if not None is used_As7reduced:
        (A7repr, A7reduced) = A_A
        if A7reduced in used_As7reduced:
            return (401100, k4D, A_A)
        used_As7reduced.add(A7reduced)
    using_baby_steps_giant_steps_method_instead_stage2 = not imay_sz4giant_step == -1
    if using_baby_steps_giant_steps_method_instead_stage2:
        sz4giant_step = imay_sz4giant_step
        approximate_qfbclassno5D_ = mk__approximate_qfbclassno5D_(info8qfbclassno4D)
        offset4exp4pt7final6stage1 = approximate_qfbclassno5D_(D)
        r13 = ops6stage123.search6stage13_(offset4exp4pt7final6stage1, min_num_fwd_giant_steps:=-sz4giant_step, max_num_fwd_giant_steps:=sz4giant_step, sz4giant_step, detect_period:=1, max4exp6stage1, reproduceable4exps6stage1, pt0)
        match r13:
            case (304, -1, r1, (history_saver7oo, offset7first7oo, offset7last7oo)):
                return (601100, k4D, A_A)
            case ((107|307), 1, _pt7found, (exps7key, (1, pt7found) as patch0001) as exps7key_patch):
                # !! to_search_exps8factors4order6found
                assert pt7found.eq_one_()
                assert _pt7found.eq_one_()
                exps7key
                pass
            case _:
                raise Exception((n, k4D, A_A), r12)
        exps7key
    else:
        r12 = ops6stage123.search6stage12_(to_search_exps8factors4order6found:=True, detect_period:=1, max4exp6stage1, max4exp6stage2, reproduceable4exps6stage1, reproduceable4exps6stage2, pt0)
        match r12:
            case (202, -1, r1, r2):
                return (201100, k4D, A_A)
            case ((107|207), 1, _pt7found, (exps7key, (1, pt7found) as patch0001) as exps7key_patch):
                # !! to_search_exps8factors4order6found
                assert pt7found.eq_one_()
                assert _pt7found.eq_one_()
                exps7key
                pass
            case _:
                raise Exception((n, k4D, A_A), r12)
        exps7key
    exps7key
    ######################
    exps7key = _std_exps7key_(exps7key)
    ######################
    num_twos = exps7key.count(2)
    if 0 == num_twos:
        return (301110, k4D, A_A, exps7key)
    exps7key7odd = exps7key[num_twos:]
    exps7key7even = exps7key[:num_twos]
    if not 0 == exps7key7odd.count(2):raise Exception((n, k4D, A_A), exps7key)
    if not (2,)*num_twos == exps7key7even:raise Exception((n, k4D, A_A), exps7key)
    pt = pt0**II(exps7key7odd)
    for _ in range(-1+num_twos):
        pt **= 2
    pt7ambiguous = pt
    return _tail4trial4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_(n, k4D, A_A, D, exps7key, pt0, pt7ambiguous)
def _std_exps7key_(exps7key, /):
    exps7key = mk_tuple(exps7key)
    num_twos = exps7key.count(2)
    if not (exps7key[:num_twos] == (2,)*num_twos and all(e&1 == 1 for e in exps7key[num_twos:])):
        num_twos = 0
        odds = []
        for e in exps7key:
            (ez, odd) = factor_pint_out_power_of_base_(2, e)
            num_twos += ez
            if not odd == 1:
                odds.append(odd)
        odds.sort()
        exps7key = (*[2]*num_twos, *odds)
    return exps7key

def _tail4trial4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_(n, k4D, A_A, D, exps7key, pt0, pt7ambiguous, /):
    if not pt7ambiguous.is_ambiguous_form_():raise Exception((n, k4D, A_A), exps7key, pt0, pt7ambiguous)
    zmay_nontrivial_odd_factor4D = pt7ambiguous.try_factor_D6ambiguous_form_()
    match zmay_nontrivial_odd_factor4D:
        case 0:
            return (501110, k4D, A_A, exps7key)
        case nontrivial_odd_factor4D:
            pass
    ft6k = gcd(k4D, nontrivial_odd_factor4D)
    ft6n = nontrivial_odd_factor4D//ft6k
    if 1 == ft6n or n == ft6n:
        return (701110, k4D, A_A, exps7key)
    if 1 < ft6n < n:
        assert n%ft6n == 0, (n, k4D, A_A, exps7key, nontrivial_odd_factor4D, ft6k, ft6n)
        return (901111, k4D, A_A, exps7key, ft6n)
    raise Exception(n, k4D, A_A, exps7key, nontrivial_odd_factor4D, ft6k, ft6n)


    ######################
    ######################
    ######################


    #.######################
    #.check_int_ge(1, n)
    #.check_int_ge(1, k4D)
    #.if not n&1:raise ValueError(n)
    #.if not k4D&1:raise ValueError(k4D)
    #.if 1 < (g:=gcd(n,k4D)):
    #.    if g < n:
    #.        return g
    #.    if g == n:raise ValueError(k4D)
    #.    raise 000
    #.#nk = n*k4D
    #.#D = n2D_(nk)
    #.D = nk2D_(n, k4D)



    ######################
#################################

class IOps6stage123_4smooth_group_order_method__7BinaryQuadraticForm(IOps6stage123_4smooth_group_order_method__7default_mixin):
    '[pt :: EqvCls4BinaryQuadraticForm]'
    __slots__ = ()
    @property
    @abstractmethod
    def n(sf, /):
        '-> n/int{>=1}{%2==1}'
    @property
    @abstractmethod
    def k4D(sf, /):
        '-> k4D/int{>=1}{%2==1}{[gcd(n,k4D) == 1]}'
    @CachedProperty
    def D(sf, /):
        '-> D/int{<0}{%4<2}'
        n = sf.n
        k4D = sf.k4D
        return nk2D_(n, k4D)
    #@override
    may_key7hash_ = None
    @CachedProperty
    @override
    def one(sf, /):
        return mk_one6Qfb_class_group5D_(sf.D)
    @override
    def eq_one_(sf, pt, /):
        return pt.eq_one_()
    @override
    def pow_(sf, pt, exp, /):
        return (pt**exp)
    @override
    def square_(sf, pt, /):
        return (pt**2)
    @override
    def mul_(sf, pt8lhs, pt8rhs, /):
        return pt8lhs * pt8rhs
    @override
    def detect_partial_one_(sf, pt, /):
        return +1 if pt.eq_one_() else -1
    #search6stage12_
check_ABC(IOps6stage123_4smooth_group_order_method__7BinaryQuadraticForm, 'n k4D'.split())
class Ops6stage123_4smooth_group_order_method__7BinaryQuadraticForm(IOps6stage123_4smooth_group_order_method__7BinaryQuadraticForm):
    ___no_slots_ok___ = True
    def __init__(sf, n, k4D, /):
        check_int_ge(1, n)
        check_int_ge(1, k4D)
        sf._n = n
        sf._k4D = k4D
        777;sf.D # check
    @property
    @override
    def n(sf, /):
        return sf._n
    @property
    @override
    def k4D(sf, /):
        return sf._k4D
    def __repr__(sf, /):
        return repr_helper(sf, sf.n, sf.k4D)
#################################

def _iter_test4factor7bqf():
    from seed.types.Reproduceable import Reproduceable5seq
    reproduceable4exps6stage1 = Reproduceable5seq((2, 2, 2, 13, 17, 37, 59, 1993), 0)

    used_As7reduced = set()
    kwds = dict(used_As7reduced=used_As7reduced)
    min_A = 1
    while 1:
        yield (min_A)
        t = one_trial4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_((-1+2**67), 35, min_A,    1993,1993, reproduceable4exps6stage1, **kwds)
        match t:
            case (_, k4D, _, _, ft4n):
                yield (t)
                break
            case (_, k4D, A_A, exps7key):
                (A7repr, A7reduced) = A_A
                min_A = 1+A7repr
                continue
            case (401100, k4D, A_A):
                (A7repr, A7reduced) = A_A
                min_A = 1+A7repr
                continue

            case (201100|601100, k4D, A_A):
                raise Exception('reproduceable4exps6stage1 not catch all prime factor of order of class group', t)
            case _:
                raise Exception(t)
        raise 000





__all__


















__all__
from seed.math.factor_pint.factor_pint__smooth_group_order_method import factor_pint__smooth_group_order_method7Pmm_, factor_pint__smooth_group_order_method7Qpp_
from seed.math.factor_pint.factor_pint__smooth_group_order_method import *
