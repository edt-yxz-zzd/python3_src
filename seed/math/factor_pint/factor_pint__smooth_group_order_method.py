#__all__:goto
r'''[[[
e ../../python3_src/seed/math/factor_pint/factor_pint__smooth_group_order_method.py
view ../../python3_src/seed/math/factor_pint/smooth_group_order_method.py


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



]]
[[
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







>>> factor_pint__smooth_group_order_method7Qpp_(7*31, 9,  2,2, bound4pow4stage1=16)
31
>>> factor_pint__smooth_group_order_method7Qpp_(7*31, 9,  2,2, bound4pow4stage1=15)
0
>>> factor_pint__smooth_group_order_method7Qpp_(7*31, 3,  2,2, bound4pow4stage1=4)
7
>>> factor_pint__smooth_group_order_method7Qpp_(7*31, 3,  2,2, bound4pow4stage1=3)
0


>>> factor_pint__smooth_group_order_method7Qpp_(11*23, 3,  4,4)
23
>>> factor_pint__smooth_group_order_method7Qpp_(11*23, 6,  4,4)
11
>>> factor_pint__smooth_group_order_method7Qpp_(11*23, 16,  4,4) # !! [2,2,3]
(3,)
>>> factor_pint__smooth_group_order_method7Qpp_(11*23, 16,  3,3) # !! [2,3]
(2,)
>>> factor_pint__smooth_group_order_method7Qpp_(11*23, 16,  2,3) # !! [2]++[3]
(1, 2)


>>> factor_pint__smooth_group_order_method7Qpp_(18014398509482483*18014398509482839, 3,  10429,47119)
18014398509482483
>>> factor_pint__smooth_group_order_method7Qpp_(18014398509482483*18014398509482839, 4,  10429,47119)
18014398509482839



















[[
def factor_pint__smooth_group_order_method7Pmm_(n, u0, bound4stage1, bound4stage2=None, /, *, more_info=False, detect_once6stage1=False, bound4pow4stage1=1, case4xprimes=2, max_size7dense=2049, max_size7physical=65537):
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Pmm_   ='17*31' =5  =2 =2 --bound4pow4stage1=16
    17
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Pmm_   ='17*31' =5  =2 =2 --bound4pow4stage1=8
    0


py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Pmm_   ='7*5' =2  =2 =3 --bound4pow4stage1=2 # +more_info +_debug7list_all
    7
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Pmm_   ='7*5' =2  =2 =2 --bound4pow4stage1=2
    0



[M67 == -1+2**67 == 193707721*761838257287]
[193707721 == 1+2**3 * 3**3 *5 *67 *2677]
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Pmm_   ='-1+2**67' =5  =67 =2677 --bound4pow4stage1=1
    193707721
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Pmm_   ='-1+2**67' =5  =67 =-1+2677 --bound4pow4stage1=1
    0
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Pmm_   ='-1+2**67' =5  =-1+67 =2677 --bound4pow4stage1=1
    0

py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Pmm_   ='13*37' =2  =4 =4
    13
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Pmm_   ='13*37' =6  =4 =4
    37
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Pmm_   ='13*37' =10  =4 =4
    (3,) # <<== [2,2,3]
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Pmm_   ='13*37' =10  =2 =4
    (1, 2) # <<== [2]++[3]


]]
[[
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =3   =2 =2 --bound4pow4stage1=4
    7
    # [D==B**2-4==5]
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =3   =2 =2 --bound4pow4stage1=2
    0
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =5   =2 =2 --bound4pow4stage1=8
    31
    # [D==B**2-4==21]
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =5   =2 =2 --bound4pow4stage1=4
    0

py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =6   =2 =2 --bound4pow4stage1=32
    0
    # [D==B**2-4==32]
    # [Jacobi_symbol(7;32) == Jacobi_symbol(7;4) == +1]
    # [Jacobi_symbol(31;32) == Jacobi_symbol(31;1) == +1]
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =6   =2 =2 --bound4pow4stage1=2
    0
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =6   =2 =3 --bound4pow4stage1=2
    7
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =6   =5 =5
    7
    #???31???

py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =8   =2 =2 --bound4pow4stage1=4
    31
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =8   =2 =2 --bound4pow4stage1=2
    0

py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =9   =2 =2 --bound4pow4stage1=16
    31
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =9   =2 =2 --bound4pow4stage1=8
    0

py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =12   =2 =2 --bound4pow4stage1=32
    0
    # [D==B**2-4==140]
    # [Jacobi_symbol(7;140) == 0]
    # [Jacobi_symbol(31;140) == Jacobi_symbol(31;16) == +1]

py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =20   =2 =2 --bound4pow4stage1=16
    31
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =20   =2 =2 --bound4pow4stage1=8
    0
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =22   =2 =2 --bound4pow4stage1=16
    31
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =22   =2 =2 --bound4pow4stage1=8
    0






py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='11*23' =3   =4 =4
    23
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='11*23' =6   =4 =4
    11
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='11*23' =16   =4 =4
    (3,) # <<== [2,2,3]
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='11*23' =16   =3 =3
    (2,) # <<== [2,3]
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='11*23' =16   =2 =3
    (1, 2) # <<== [2]++[3]





[M67 == -1+2**67 == 193707721*761838257287]
[193707721 == -1+2*13*7450297]
    #7450297:23bit
[761838257287 == -1+2**3 *67927 *1401943]
    #1401943:21bit

? default('output,0)
? factorint(-1+2^53)~
[6361,69431,20394401;1,1,1]

? factorint(-1+20394401)~
[2,5,13,37,53;5,2,1,1,1]
? factorint(1+20394401)~
[2,3,7,277,1753;1,1,1,1,1]

? factorint(-1+69431)~
[2,5,53,131;1,1,1,1]
? factorint(1+69431)~
[2,3,11,263;3,1,1,1]

? factorint(-1+6361)~
[2,3,5,53;3,1,1,1]
? factorint(1+6361)~
[2,3181;1,1]


? factorint(1+2^54)~
[5,13,37,109,246241,279073;1,1,1,1,1,1]

? factorint(1+246241)~
[2,123121;1,1]
? factorint(-1+246241)~
[2,3,5,19;5,4,1,1]

? factorint(1+279073)~
[2,139537;1,1]
? factorint(-1+279073)~
[2,3,17,19;5,3,1,1]

? nextprime(2^54)
18014398509482143
iter_next_probable_primes ='2**54' | more

? factorint(1+18014398509482143)~
[2,7,11,179,3517,11613247;5,1,1,1,1,1]
? factorint(1+18014398509482147)~
[2,3,173,1721,5042101063;2,1,1,1,1]
? factorint(1+18014398509482171)~
[2,3,7,59,2683,2551369;2,3,1,2,1,1]
? factorint(1+18014398509482329)~
[2,5,1801439850948233;1,1,1]
? factorint(1+18014398509482357)~
[2,3,419,2161,3847,861941;1,1,1,1,1,1]
? factorint(1+18014398509482387)~
[2,3,13,103,13841173861;2,5,1,1,1]
? factorint(1+18014398509482399)~
[2,3,5,2663,3541,795997;5,1,2,1,1,1]
? factorint(1+18014398509482461)~
[2,40751,221030140481;1,1,1]
? factorint(1+18014398509482471)~
[2,3,1063033,706092791;3,1,1,1]
? factorint(1+18014398509482483)~
[2,3,29,229,521,10429,41603;2,1,1,1,1,1,1]
? factorint(1+18014398509482537)~
[2,3,131,22919082073133;1,1,1,1]
? factorint(1+18014398509482579)~
[2,3,5,269,1116133736647;2,1,1,1,1]
? factorint(1+18014398509482603)~
[2,3,166799986198913;2,3,1]
? factorint(1+18014398509482677)~
[2,283,1873,129281,131441;1,1,1,1,1]
? factorint(1+18014398509482693)~
[2,3,11,90981810653953;1,2,1,1]
? factorint(1+18014398509482723)~
[2,3,19,8011951,9861583;2,1,1,1,1]
? factorint(1+18014398509482839)~
[2,5,67,173,383,2153,47119;3,1,1,1,1,1,1]
? factorint(1+18014398509482863)~
[2,1125899906842679;4,1]


/,\d\{,5};
? factorint(1+18014398509482483)~
[2,3,29,229,521,10429,41603;2,1,1,1,1,1,1]
? factorint(1+18014398509482839)~
[2,5,67,173,383,2153,47119;3,1,1,1,1,1,1]

? factorint(-1+18014398509482483)~
[2,223,40391028048167;1,1,1]
? factorint(-1+18014398509482839)~
[2,3,17,19,293,36591421;1,2,3,1,1,1]

324518553658451118278737859609237
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='18014398509482483*18014398509482839' =3  =10429 =47119
    18014398509482483
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='18014398509482483*18014398509482839' =4  =10429 =47119
    18014398509482839

]]



py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @f
]]]'''#'''
__all__ = r'''
factor_pint__smooth_group_order_method7Pmm_
factor_pint__smooth_group_order_method7Qpp_




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
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.dict__add_fmap_filter import fmap4dict_value
    from seed.mapping_tools.dict_op import inv__k2v_to_v2ks
    from seed.math.Jacobi_symbol import Jacobi_symbol

    from seed.tiny_.check import check_type_is, check_int_ge, check_callable, check_may_
    from math import gcd

    from seed.math.factor_pint.smooth_group_order_method import smooth_group_order_method_
    #def smooth_group_order_method_(bound4stage1, bound4pow4stage1, bound4stage2, diff_one_, detect_, mul_, may_square_, may_pow_, one, pt0, /, *, num_muls_per_detect, imay_detect_period=0, case4xprimes=None, max_size7dense=2049, max_size7physical=65537):

    from seed.math.hrem_ import hrem_, mk_hrem_
#.    from itertools import islice
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

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























#################################
def factor_pint__smooth_group_order_method7Pmm_(n, u0, bound4stage1, bound4stage2=None, /, *, more_info=False, detect_once6stage1=False, bound4pow4stage1=1, case4xprimes=2, max_size7dense=2049, max_size7physical=65537, _debug7list_all=False, **kwds):
    '-> ((offset1, offset2)/{#found-factor-of-(P-1) at stage2#}|(offset1,)/{#found-factor-of-(P-1) at stage1#}|0/{#fail#}|nontrivial_factor/uint{>0}) # (P-1) method'
    check_int_ge(2, n)
    check_type_is(int, u0)
    check_int_ge(1, bound4stage1)
    check_int_ge(1, bound4pow4stage1)
    if bound4stage2 is None:
        bound4stage2 = 100*bound4stage1
    check_int_ge(1, bound4stage2)

    num_muls_per_detect = 10*n.bit_length()
    imay_detect_period = -1 if detect_once6stage1 else 0
    one = 1
    pt0 = u0%n
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
    r = smooth_group_order_method_(bound4stage1, bound4pow4stage1, bound4stage2, diff_one_, detect_, mul_, square_, pow_, one, pt0, num_muls_per_detect=num_muls_per_detect, imay_detect_period=imay_detect_period, case4xprimes=case4xprimes, max_size7dense=max_size7dense, max_size7physical=max_size7physical, _debug7list_all=_debug7list_all, **kwds)
    return _postprocess(n, r, more_info)
#end-def factor_pint__smooth_group_order_method7Pmm_(n, u0, bound4stage1, bound4stage2=None, /, *, more_info=False, detect_once6stage1=False, bound4pow4stage1=1, case4xprimes=2, max_size7dense=2049, max_size7physical=65537, _debug7list_all=False, **kwds):
#################################
def _postprocess(n, r, more_info, /):
    if more_info:
        return r

    match r:
        case ((10|20), int(nontrivial_factor), _):
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
def factor_pint__smooth_group_order_method7Qpp_(n, u0, bound4stage1, bound4stage2=None, /, *, more_info=False, detect_once6stage1=False, bound4pow4stage1=1, case4xprimes=2, max_size7dense=2049, max_size7physical=65537, _debug7list_all=False, **kwds):
    '-> ((offset1, offset2)/{#found-factor-of-(P-1|P+1) at stage2#}|(offset1,)/{#found-factor-of-(P-1|P+1) at stage1#}|0/{#fail#}|nontrivial_factor/uint{>0}) # (P+1) method'
    check_int_ge(2, n)
    if not n&1 == 1:raise ValueError
    check_type_is(int, u0)
    check_int_ge(1, bound4stage1)
    check_int_ge(1, bound4pow4stage1)
    if bound4stage2 is None:
        bound4stage2 = 100*bound4stage1
    check_int_ge(1, bound4stage2)

    num_muls_per_detect = 10*n.bit_length()
    imay_detect_period = -1 if detect_once6stage1 else 0
    # [pt == (a,b) === (a+b*X)%{n,1+B*X+X**2}]
    hrem4N_ = mk_hrem_(n)
    one = (1, 0)
    pt0 = (0, 1)
    B = hrem4N_(u0)

    def diff_one_(ab, /):
        (a, b) = ab
        return (hrem4N_(a-1), b)
    def detect_(ab, /):
        (a, b) = ab
        v = gcd(a*b, n)
        if v == 1:
            return (-1, None)
        if 1 < v < n:
            return (0, v)
        assert v == n
        if a == 0 == b:
            return (+1, None)
        for x in ab:
            if x:
                _v = gcd(x, n)
                if 1 < _v < n:
                    return (0, _v)
                if _v == 1:
                    v == 1
        if v == 1:
            return (-1, None)
        if v == n:
            return (+1, None)
        raise 000
    detect_
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
    r = smooth_group_order_method_(bound4stage1, bound4pow4stage1, bound4stage2, diff_one_, detect_, mul_, square_, may_pow_:=None, one, pt0, num_muls_per_detect=num_muls_per_detect, imay_detect_period=imay_detect_period, case4xprimes=case4xprimes, max_size7dense=max_size7dense, max_size7physical=max_size7physical, _debug7list_all=_debug7list_all, **kwds)
    return _postprocess(n, r, more_info)
#end-def factor_pint__smooth_group_order_method7Qpp_
#################################








__all__
from seed.math.factor_pint.factor_pint__smooth_group_order_method import factor_pint__smooth_group_order_method7Pmm_, factor_pint__smooth_group_order_method7Qpp_
from seed.math.factor_pint.factor_pint__smooth_group_order_method import *
