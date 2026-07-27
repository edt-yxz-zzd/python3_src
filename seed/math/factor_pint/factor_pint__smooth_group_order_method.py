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
>>> [+1+18014398509482839 == 2**3 *5*67*173*383*2153*47119]
[True]
>>> [-1+18014398509482483 == 2*223*40391028048167]
[True]
>>> [-1+18014398509482839 == 2 *3**2 *17**3 *19*293*36591421]
[True]
>>> factor_pint__smooth_group_order_method7Qpp_(18014398509482483*18014398509482839, 3,  10429,47119)
18014398509482483
>>> factor_pint__smooth_group_order_method7Qpp_(18014398509482483*18014398509482839, 4,  10429,47119)
18014398509482839





















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
r'''[[[

[[[
===

[[
def factor_pint__smooth_group_order_method7Pmm_(n, u0, bound4stage1, bound4stage2=None, /, *, more_info=False, detect_once6stage1=False, bound4pow4stage1=1, case4xprimes=2, max_size7dense=2049, max_size7physical=65537):
===
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Pmm_   ='17*31' =5  =2 =2 --bound4pow4stage1=16
    17
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Pmm_   ='17*31' =5  =2 =2 --bound4pow4stage1=8
    0


===
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Pmm_   ='7*5' =2  =2 =3 --bound4pow4stage1=2 # +more_info +_debug7list_all
    7
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Pmm_   ='7*5' =2  =2 =2 --bound4pow4stage1=2
    0



===
[M67 == -1+2**67 == 193707721*761838257287]
[193707721 == 1+2**3 * 3**3 *5 *67 *2677]
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Pmm_   ='-1+2**67' =5  =67 =2677 --bound4pow4stage1=1
    193707721
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Pmm_   ='-1+2**67' =5  =67 =-1+2677 --bound4pow4stage1=1
    0
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Pmm_   ='-1+2**67' =5  =-1+67 =2677 --bound4pow4stage1=1
    0



===
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Pmm_   ='13*37' =2  =4 =4
    13
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Pmm_   ='13*37' =6  =4 =4
    37
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Pmm_   ='13*37' =10  =4 =4
    (3,) # <<== [2,2,3]
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Pmm_   ='13*37' =10  =2 =4
    (1, 2) # <<== [2]++[3]

===
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   ,_iter_search_exceptional4factor_pint__smooth_group_order_method7Pmm_  ='13*37' ='range(13*37)'   =4 =4
    (1, (0,))
    (10, (3,))
    (11, (3,))
    (23, (3,))
    (29, (3,))
    (31, (2,))
    (45, (3,))
    (48, (3,))
    (63, (3,))
    (82, (3,))
    (84, (3,))
    (85, (3,))
    (88, (3,))
    (97, (3,))
    (100, (3,))
    (101, (3,))
    (119, (3,))
    (121, (3,))
    (134, (3,))
    (137, (3,))
    (140, (3,))
    (158, (3,))
    (159, (3,))
    (162, (3,))
    (171, (3,))
    (175, (3,))
    (193, (3,))
    (199, (3,))
    (211, (3,))
    (212, (3,))
    (214, (3,))
    (216, (2,))
    (230, (3,))
    (232, (3,))
    (236, (3,))
    (245, (3,))
    (249, (3,))
    (251, (3,))
    (265, (2,))
    (267, (3,))
    (269, (3,))
    (270, (3,))
    (282, (3,))
    (288, (3,))
    (306, (3,))
    (310, (3,))
    (319, (3,))
    (322, (3,))
    (323, (3,))
    (341, (3,))
    (344, (3,))
    (347, (3,))
    (360, (3,))
    (362, (3,))
    (380, (3,))
    (381, (3,))
    (384, (3,))
    (393, (3,))
    (396, (3,))
    (397, (3,))
    (399, (3,))
    (418, (3,))
    (433, (3,))
    (436, (3,))
    (450, (2,))
    (452, (3,))
    (458, (3,))
    (470, (3,))
    (471, (3,))
    (480, (1,))

===
]]
[[
===
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =3   =2 =2 --bound4pow4stage1=4
    7
    # [D==B**2-4==5]
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =3   =2 =2 --bound4pow4stage1=2
    0
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =5   =2 =2 +more_info
    (99001, 7, 'from:gcd(D,n) or gcd(B-2,n)')
    # [D==B**2-4==21]

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

py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =9   =2 =2 +more_info
    (99001, 7, 'from:gcd(D,n) or gcd(B-2,n)')

py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =12   =2 =2 +more_info
    (99001, 7, 'from:gcd(D,n) or gcd(B-2,n)')
    # [D==B**2-4==140]

py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =20   =2 =2 --bound4pow4stage1=16
    31
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =20   =2 =2 --bound4pow4stage1=8
    0
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =22   =2 =2 --bound4pow4stage1=16
    31
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =22   =2 =2 --bound4pow4stage1=8
    0






===
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='11*23' =3   =4 =4
    23
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='11*23' =6   =4 =4
    11
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='11*23' =16   =4 =4
    (3,) # <<== [2,2,3]
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='11*23' =16   =3 =3
    0
    #???old:(2,) # <<== [2,3]
    #bug_fixed_1:goto
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='11*23' =16   =2 =3
    0
    #???old:(1, 2) # <<== [2]++[3]
    #bug_fixed_1:goto

===
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   ,_iter_search_exceptional4factor_pint__smooth_group_order_method7Qpp_  ='11*23' ='range(11*23)'   =4 =4
    (0, (2,))
    (1, (3,))
    (2, -1)
    (16, (3,))
    (39, (3,))
    (45, (3,))
    (76, (3,))
    (93, (3,))
    (116, (3,))
    (122, (3,))
    (131, (3,))
    (137, (3,))
    (160, (3,))
    (177, (3,))
    (208, (3,))
    (214, (3,))
    (237, (3,))
    (251, -1)
    (252, (3,))

===
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='11*23' =45   =4 =4
    (3,) # <<== [2,2,3]
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='11*23' =45   =3 =3
    (2,) # <<== [2,3]
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='11*23' =45   =2 =3
    (1, 2) # <<== [2]++[3]





===
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

===
324518553658451118278737859609237
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='18014398509482483*18014398509482839' =3  =10429 =47119
    18014398509482483
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='18014398509482483*18014398509482839' =4  =10429 =47119
    18014398509482839

===
]]
[[
===
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   ,stable_repr._iter_search_mul_order4X_4factor_pint__smooth_group_order_method7Qpp_  ='11*23' ='range(11*23)'
    (0, 4, {2: 2})
    (1, 3, {3: 1})
    (2, 506, {2: 1, 11: 1, 23: 1})
    (3, 120, {2: 3, 3: 1, 5: 1})
    (4, 110, {2: 1, 5: 1, 11: 1})
    (5, 24, {2: 3, 3: 1})
    (6, 132, {2: 2, 3: 1, 11: 1})
    (7, 60, {2: 2, 3: 1, 5: 1})
    (8, 120, {2: 3, 3: 1, 5: 1})
    (9, 11, {11: 1})
    (10, 66, {2: 1, 3: 1, 11: 1})
    (11, 44, {2: 2, 11: 1})
    (12, 33, {3: 1, 11: 1})
    (13, 22, {2: 1, 11: 1})
    (14, 110, {2: 1, 5: 1, 11: 1})
    (15, 120, {2: 3, 3: 1, 5: 1})
    (16, 12, {2: 2, 3: 1})
    (17, 132, {2: 2, 3: 1, 11: 1})
    (18, 40, {2: 3, 5: 1})
    (19, 55, {5: 1, 11: 1})
    (20, 264, {2: 3, 3: 1, 11: 1})
    (21, 138, {2: 1, 3: 1, 23: 1})
    (22, 12, {2: 2, 3: 1})
    (23, 12, {2: 2, 3: 1})
    (24, 66, {2: 1, 3: 1, 11: 1})
    (25, 230, {2: 1, 5: 1, 23: 1})
    (26, 120, {2: 3, 3: 1, 5: 1})
    (27, 132, {2: 2, 3: 1, 11: 1})
    (28, 24, {2: 3, 3: 1})
    (29, 110, {2: 1, 5: 1, 11: 1})
    (30, 60, {2: 2, 3: 1, 5: 1})
    (31, 264, {2: 3, 3: 1, 11: 1})
    (32, 66, {2: 1, 3: 1, 11: 1})
    (33, 44, {2: 2, 11: 1})
    (34, 66, {2: 1, 3: 1, 11: 1})
    (35, 22, {2: 1, 11: 1})
    (36, 110, {2: 1, 5: 1, 11: 1})
    (37, 110, {2: 1, 5: 1, 11: 1})
    (38, 24, {2: 3, 3: 1})
    (39, 12, {2: 2, 3: 1})
    (40, 110, {2: 1, 5: 1, 11: 1})
    (41, 40, {2: 3, 5: 1})
    (42, 11, {11: 1})
    (43, 24, {2: 3, 3: 1})
    (44, 92, {2: 2, 23: 1})
    (45, 6, {2: 1, 3: 1})
    (46, 44, {2: 2, 11: 1})
    (47, 30, {2: 1, 3: 1, 5: 1})
    (48, 230, {2: 1, 5: 1, 23: 1})
    (49, 24, {2: 3, 3: 1})
    (50, 132, {2: 2, 3: 1, 11: 1})
    (51, 40, {2: 3, 5: 1})
    (52, 110, {2: 1, 5: 1, 11: 1})
    (53, 132, {2: 2, 3: 1, 11: 1})
    (54, 24, {2: 3, 3: 1})
    (55, 44, {2: 2, 11: 1})
    (56, 66, {2: 1, 3: 1, 11: 1})
    (57, 22, {2: 1, 11: 1})
    (58, 110, {2: 1, 5: 1, 11: 1})
    (59, 55, {5: 1, 11: 1})
    (60, 132, {2: 2, 3: 1, 11: 1})
    (61, 24, {2: 3, 3: 1})
    (62, 60, {2: 2, 3: 1, 5: 1})
    (63, 55, {5: 1, 11: 1})
    (64, 88, {2: 3, 11: 1})
    (65, 66, {2: 1, 3: 1, 11: 1})
    (66, 24, {2: 3, 3: 1})
    (67, 69, {3: 1, 23: 1})
    (68, 66, {2: 1, 3: 1, 11: 1})
    (69, 20, {2: 2, 5: 1})
    (70, 15, {3: 1, 5: 1})
    (71, 276, {2: 2, 3: 1, 23: 1})
    (72, 24, {2: 3, 3: 1})
    (73, 110, {2: 1, 5: 1, 11: 1})
    (74, 40, {2: 3, 5: 1})
    (75, 22, {2: 1, 11: 1})
    (76, 12, {2: 2, 3: 1})
    (77, 24, {2: 3, 3: 1})
    (78, 33, {3: 1, 11: 1})
    (79, 22, {2: 1, 11: 1})
    (80, 110, {2: 1, 5: 1, 11: 1})
    (81, 55, {5: 1, 11: 1})
    (82, 132, {2: 2, 3: 1, 11: 1})
    (83, 132, {2: 2, 3: 1, 11: 1})
    (84, 120, {2: 3, 3: 1, 5: 1})
    (85, 60, {2: 2, 3: 1, 5: 1})
    (86, 11, {11: 1})
    (87, 24, {2: 3, 3: 1})
    (88, 44, {2: 2, 11: 1})
    (89, 24, {2: 3, 3: 1})
    (90, 506, {2: 1, 11: 1, 23: 1})
    (91, 30, {2: 1, 3: 1, 5: 1})
    (92, 20, {2: 2, 5: 1})
    (93, 12, {2: 2, 3: 1})
    (94, 276, {2: 2, 3: 1, 23: 1})
    (95, 120, {2: 3, 3: 1, 5: 1})
    (96, 110, {2: 1, 5: 1, 11: 1})
    (97, 88, {2: 3, 11: 1})
    (98, 66, {2: 1, 3: 1, 11: 1})
    (99, 12, {2: 2, 3: 1})
    (100, 24, {2: 3, 3: 1})
    (101, 22, {2: 1, 11: 1})
    (102, 110, {2: 1, 5: 1, 11: 1})
    (103, 110, {2: 1, 5: 1, 11: 1})
    (104, 132, {2: 2, 3: 1, 11: 1})
    (105, 132, {2: 2, 3: 1, 11: 1})
    (106, 110, {2: 1, 5: 1, 11: 1})
    (107, 120, {2: 3, 3: 1, 5: 1})
    (108, 132, {2: 2, 3: 1, 11: 1})
    (109, 66, {2: 1, 3: 1, 11: 1})
    (110, 8, {2: 3})
    (111, 33, {3: 1, 11: 1})
    (112, 264, {2: 3, 3: 1, 11: 1})
    (113, 230, {2: 1, 5: 1, 23: 1})
    (114, 30, {2: 1, 3: 1, 5: 1})
    (115, 12, {2: 2, 3: 1})
    (116, 12, {2: 2, 3: 1})
    (117, 230, {2: 1, 5: 1, 23: 1})
    (118, 120, {2: 3, 3: 1, 5: 1})
    (119, 22, {2: 1, 11: 1})
    (120, 24, {2: 3, 3: 1})
    (121, 44, {2: 2, 11: 1})
    (122, 12, {2: 2, 3: 1})
    (123, 264, {2: 3, 3: 1, 11: 1})
    (124, 110, {2: 1, 5: 1, 11: 1})
    (125, 110, {2: 1, 5: 1, 11: 1})
    (126, 132, {2: 2, 3: 1, 11: 1})
    (127, 132, {2: 2, 3: 1, 11: 1})
    (128, 110, {2: 1, 5: 1, 11: 1})
    (129, 110, {2: 1, 5: 1, 11: 1})
    (130, 264, {2: 3, 3: 1, 11: 1})
    (131, 12, {2: 2, 3: 1})
    (132, 44, {2: 2, 11: 1})
    (133, 24, {2: 3, 3: 1})
    (134, 22, {2: 1, 11: 1})
    (135, 120, {2: 3, 3: 1, 5: 1})
    (136, 115, {5: 1, 23: 1})
    (137, 12, {2: 2, 3: 1})
    (138, 12, {2: 2, 3: 1})
    (139, 30, {2: 1, 3: 1, 5: 1})
    (140, 230, {2: 1, 5: 1, 23: 1})
    (141, 264, {2: 3, 3: 1, 11: 1})
    (142, 66, {2: 1, 3: 1, 11: 1})
    (143, 8, {2: 3})
    (144, 66, {2: 1, 3: 1, 11: 1})
    (145, 132, {2: 2, 3: 1, 11: 1})
    (146, 120, {2: 3, 3: 1, 5: 1})
    (147, 55, {5: 1, 11: 1})
    (148, 132, {2: 2, 3: 1, 11: 1})
    (149, 132, {2: 2, 3: 1, 11: 1})
    (150, 110, {2: 1, 5: 1, 11: 1})
    (151, 55, {5: 1, 11: 1})
    (152, 22, {2: 1, 11: 1})
    (153, 24, {2: 3, 3: 1})
    (154, 12, {2: 2, 3: 1})
    (155, 33, {3: 1, 11: 1})
    (156, 88, {2: 3, 11: 1})
    (157, 110, {2: 1, 5: 1, 11: 1})
    (158, 120, {2: 3, 3: 1, 5: 1})
    (159, 276, {2: 2, 3: 1, 23: 1})
    (160, 12, {2: 2, 3: 1})
    (161, 20, {2: 2, 5: 1})
    (162, 15, {3: 1, 5: 1})
    (163, 506, {2: 1, 11: 1, 23: 1})
    (164, 24, {2: 3, 3: 1})
    (165, 44, {2: 2, 11: 1})
    (166, 24, {2: 3, 3: 1})
    (167, 22, {2: 1, 11: 1})
    (168, 60, {2: 2, 3: 1, 5: 1})
    (169, 120, {2: 3, 3: 1, 5: 1})
    (170, 132, {2: 2, 3: 1, 11: 1})
    (171, 132, {2: 2, 3: 1, 11: 1})
    (172, 110, {2: 1, 5: 1, 11: 1})
    (173, 55, {5: 1, 11: 1})
    (174, 11, {11: 1})
    (175, 66, {2: 1, 3: 1, 11: 1})
    (176, 24, {2: 3, 3: 1})
    (177, 12, {2: 2, 3: 1})
    (178, 22, {2: 1, 11: 1})
    (179, 40, {2: 3, 5: 1})
    (180, 55, {5: 1, 11: 1})
    (181, 24, {2: 3, 3: 1})
    (182, 276, {2: 2, 3: 1, 23: 1})
    (183, 30, {2: 1, 3: 1, 5: 1})
    (184, 20, {2: 2, 5: 1})
    (185, 33, {3: 1, 11: 1})
    (186, 138, {2: 1, 3: 1, 23: 1})
    (187, 24, {2: 3, 3: 1})
    (188, 66, {2: 1, 3: 1, 11: 1})
    (189, 88, {2: 3, 11: 1})
    (190, 110, {2: 1, 5: 1, 11: 1})
    (191, 60, {2: 2, 3: 1, 5: 1})
    (192, 24, {2: 3, 3: 1})
    (193, 132, {2: 2, 3: 1, 11: 1})
    (194, 110, {2: 1, 5: 1, 11: 1})
    (195, 110, {2: 1, 5: 1, 11: 1})
    (196, 11, {11: 1})
    (197, 66, {2: 1, 3: 1, 11: 1})
    (198, 44, {2: 2, 11: 1})
    (199, 24, {2: 3, 3: 1})
    (200, 132, {2: 2, 3: 1, 11: 1})
    (201, 110, {2: 1, 5: 1, 11: 1})
    (202, 40, {2: 3, 5: 1})
    (203, 132, {2: 2, 3: 1, 11: 1})
    (204, 24, {2: 3, 3: 1})
    (205, 230, {2: 1, 5: 1, 23: 1})
    (206, 30, {2: 1, 3: 1, 5: 1})
    (207, 44, {2: 2, 11: 1})
    (208, 6, {2: 1, 3: 1})
    (209, 92, {2: 2, 23: 1})
    (210, 24, {2: 3, 3: 1})
    (211, 22, {2: 1, 11: 1})
    (212, 40, {2: 3, 5: 1})
    (213, 110, {2: 1, 5: 1, 11: 1})
    (214, 12, {2: 2, 3: 1})
    (215, 24, {2: 3, 3: 1})
    (216, 110, {2: 1, 5: 1, 11: 1})
    (217, 110, {2: 1, 5: 1, 11: 1})
    (218, 22, {2: 1, 11: 1})
    (219, 66, {2: 1, 3: 1, 11: 1})
    (220, 44, {2: 2, 11: 1})
    (221, 66, {2: 1, 3: 1, 11: 1})
    (222, 264, {2: 3, 3: 1, 11: 1})
    (223, 60, {2: 2, 3: 1, 5: 1})
    (224, 55, {5: 1, 11: 1})
    (225, 24, {2: 3, 3: 1})
    (226, 132, {2: 2, 3: 1, 11: 1})
    (227, 120, {2: 3, 3: 1, 5: 1})
    (228, 115, {5: 1, 23: 1})
    (229, 66, {2: 1, 3: 1, 11: 1})
    (230, 12, {2: 2, 3: 1})
    (231, 12, {2: 2, 3: 1})
    (232, 138, {2: 1, 3: 1, 23: 1})
    (233, 264, {2: 3, 3: 1, 11: 1})
    (234, 110, {2: 1, 5: 1, 11: 1})
    (235, 40, {2: 3, 5: 1})
    (236, 132, {2: 2, 3: 1, 11: 1})
    (237, 12, {2: 2, 3: 1})
    (238, 120, {2: 3, 3: 1, 5: 1})
    (239, 55, {5: 1, 11: 1})
    (240, 22, {2: 1, 11: 1})
    (241, 66, {2: 1, 3: 1, 11: 1})
    (242, 44, {2: 2, 11: 1})
    (243, 33, {3: 1, 11: 1})
    (244, 22, {2: 1, 11: 1})
    (245, 120, {2: 3, 3: 1, 5: 1})
    (246, 60, {2: 2, 3: 1, 5: 1})
    (247, 132, {2: 2, 3: 1, 11: 1})
    (248, 24, {2: 3, 3: 1})
    (249, 110, {2: 1, 5: 1, 11: 1})
    (250, 120, {2: 3, 3: 1, 5: 1})
    (251, 253, {11: 1, 23: 1})
    (252, 6, {2: 1, 3: 1})

===
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   ,stable_repr._iter_search_mul_order4X_4factor_pint__smooth_group_order_method7Qpp_  ='11*23' ='range(11*23)' | grep '[0-9][0-9]:' -v | lineno1
    1:(0, 4, {2: 2})
    2:(1, 3, {3: 1})
    3:(3, 120, {2: 3, 3: 1, 5: 1})
    4:(5, 24, {2: 3, 3: 1})
    5:(7, 60, {2: 2, 3: 1, 5: 1})
    6:(8, 120, {2: 3, 3: 1, 5: 1})
    7:(15, 120, {2: 3, 3: 1, 5: 1})
    8:(16, 12, {2: 2, 3: 1})
    9:(18, 40, {2: 3, 5: 1})
    10:(22, 12, {2: 2, 3: 1})
    11:(23, 12, {2: 2, 3: 1})
    12:(26, 120, {2: 3, 3: 1, 5: 1})
    13:(28, 24, {2: 3, 3: 1})
    14:(30, 60, {2: 2, 3: 1, 5: 1})
    15:(38, 24, {2: 3, 3: 1})
    16:(39, 12, {2: 2, 3: 1})
    17:(41, 40, {2: 3, 5: 1})
    18:(43, 24, {2: 3, 3: 1})
    19:(45, 6, {2: 1, 3: 1})
    20:(47, 30, {2: 1, 3: 1, 5: 1})
    21:(49, 24, {2: 3, 3: 1})
    22:(51, 40, {2: 3, 5: 1})
    23:(54, 24, {2: 3, 3: 1})
    24:(61, 24, {2: 3, 3: 1})
    25:(62, 60, {2: 2, 3: 1, 5: 1})
    26:(66, 24, {2: 3, 3: 1})
    27:(69, 20, {2: 2, 5: 1})
    28:(70, 15, {3: 1, 5: 1})
    29:(72, 24, {2: 3, 3: 1})
    30:(74, 40, {2: 3, 5: 1})
    31:(76, 12, {2: 2, 3: 1})
    32:(77, 24, {2: 3, 3: 1})
    33:(84, 120, {2: 3, 3: 1, 5: 1})
    34:(85, 60, {2: 2, 3: 1, 5: 1})
    35:(87, 24, {2: 3, 3: 1})
    36:(89, 24, {2: 3, 3: 1})
    37:(91, 30, {2: 1, 3: 1, 5: 1})
    38:(92, 20, {2: 2, 5: 1})
    39:(93, 12, {2: 2, 3: 1})
    40:(95, 120, {2: 3, 3: 1, 5: 1})
    41:(99, 12, {2: 2, 3: 1})
    42:(100, 24, {2: 3, 3: 1})
    43:(107, 120, {2: 3, 3: 1, 5: 1})
    44:(110, 8, {2: 3})
    45:(114, 30, {2: 1, 3: 1, 5: 1})
    46:(115, 12, {2: 2, 3: 1})
    47:(116, 12, {2: 2, 3: 1})
    48:(118, 120, {2: 3, 3: 1, 5: 1})
    49:(120, 24, {2: 3, 3: 1})
    50:(122, 12, {2: 2, 3: 1})
    51:(131, 12, {2: 2, 3: 1})
    52:(133, 24, {2: 3, 3: 1})
    53:(135, 120, {2: 3, 3: 1, 5: 1})
    54:(137, 12, {2: 2, 3: 1})
    55:(138, 12, {2: 2, 3: 1})
    56:(139, 30, {2: 1, 3: 1, 5: 1})
    57:(143, 8, {2: 3})
    58:(146, 120, {2: 3, 3: 1, 5: 1})
    59:(153, 24, {2: 3, 3: 1})
    60:(154, 12, {2: 2, 3: 1})
    61:(158, 120, {2: 3, 3: 1, 5: 1})
    62:(160, 12, {2: 2, 3: 1})
    63:(161, 20, {2: 2, 5: 1})
    64:(162, 15, {3: 1, 5: 1})
    65:(164, 24, {2: 3, 3: 1})
    66:(166, 24, {2: 3, 3: 1})
    67:(168, 60, {2: 2, 3: 1, 5: 1})
    68:(169, 120, {2: 3, 3: 1, 5: 1})
    69:(176, 24, {2: 3, 3: 1})
    70:(177, 12, {2: 2, 3: 1})
    71:(179, 40, {2: 3, 5: 1})
    72:(181, 24, {2: 3, 3: 1})
    73:(183, 30, {2: 1, 3: 1, 5: 1})
    74:(184, 20, {2: 2, 5: 1})
    75:(187, 24, {2: 3, 3: 1})
    76:(191, 60, {2: 2, 3: 1, 5: 1})
    77:(192, 24, {2: 3, 3: 1})
    78:(199, 24, {2: 3, 3: 1})
    79:(202, 40, {2: 3, 5: 1})
    80:(204, 24, {2: 3, 3: 1})
    81:(206, 30, {2: 1, 3: 1, 5: 1})
    82:(208, 6, {2: 1, 3: 1})
    83:(210, 24, {2: 3, 3: 1})
    84:(212, 40, {2: 3, 5: 1})
    85:(214, 12, {2: 2, 3: 1})
    86:(215, 24, {2: 3, 3: 1})
    87:(223, 60, {2: 2, 3: 1, 5: 1})
    88:(225, 24, {2: 3, 3: 1})
    89:(227, 120, {2: 3, 3: 1, 5: 1})
    90:(230, 12, {2: 2, 3: 1})
    91:(231, 12, {2: 2, 3: 1})
    92:(235, 40, {2: 3, 5: 1})
    93:(237, 12, {2: 2, 3: 1})
    94:(238, 120, {2: 3, 3: 1, 5: 1})
    95:(245, 120, {2: 3, 3: 1, 5: 1})
    96:(246, 60, {2: 2, 3: 1, 5: 1})
    97:(248, 24, {2: 3, 3: 1})
    98:(250, 120, {2: 3, 3: 1, 5: 1})
    99:(252, 6, {2: 1, 3: 1})

===
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   ,stable_repr._iter_search_mul_order4X_4factor_pint__smooth_group_order_method7Qpp_  ='11*23' ='range(11*23)' | grep '[0-9][0-9]:\|[4-9]:' -v | lineno1
    # [55 == 253/4.6]
    1:(0, 4, {2: 2})
    2:(1, 3, {3: 1})
    3:(5, 24, {2: 3, 3: 1})
    4:(16, 12, {2: 2, 3: 1})
    5:(22, 12, {2: 2, 3: 1})
    6:(23, 12, {2: 2, 3: 1})
    7:(28, 24, {2: 3, 3: 1})
    8:(38, 24, {2: 3, 3: 1})
    9:(39, 12, {2: 2, 3: 1})
    10:(43, 24, {2: 3, 3: 1})
    11:(45, 6, {2: 1, 3: 1})
    12:(49, 24, {2: 3, 3: 1})
    13:(54, 24, {2: 3, 3: 1})
    14:(61, 24, {2: 3, 3: 1})
    15:(66, 24, {2: 3, 3: 1})
    16:(72, 24, {2: 3, 3: 1})
    17:(76, 12, {2: 2, 3: 1})
    18:(77, 24, {2: 3, 3: 1})
    19:(87, 24, {2: 3, 3: 1})
    20:(89, 24, {2: 3, 3: 1})
    21:(93, 12, {2: 2, 3: 1})
    22:(99, 12, {2: 2, 3: 1})
    23:(100, 24, {2: 3, 3: 1})
    24:(110, 8, {2: 3})
    25:(115, 12, {2: 2, 3: 1})
    26:(116, 12, {2: 2, 3: 1})
    27:(120, 24, {2: 3, 3: 1})
    28:(122, 12, {2: 2, 3: 1})
    29:(131, 12, {2: 2, 3: 1})
    30:(133, 24, {2: 3, 3: 1})
    31:(137, 12, {2: 2, 3: 1})
    32:(138, 12, {2: 2, 3: 1})
    33:(143, 8, {2: 3})
    34:(153, 24, {2: 3, 3: 1})
    35:(154, 12, {2: 2, 3: 1})
    36:(160, 12, {2: 2, 3: 1})
    37:(164, 24, {2: 3, 3: 1})
    38:(166, 24, {2: 3, 3: 1})
    39:(176, 24, {2: 3, 3: 1})
    40:(177, 12, {2: 2, 3: 1})
    41:(181, 24, {2: 3, 3: 1})
    42:(187, 24, {2: 3, 3: 1})
    43:(192, 24, {2: 3, 3: 1})
    44:(199, 24, {2: 3, 3: 1})
    45:(204, 24, {2: 3, 3: 1})
    46:(208, 6, {2: 1, 3: 1})
    47:(210, 24, {2: 3, 3: 1})
    48:(214, 12, {2: 2, 3: 1})
    49:(215, 24, {2: 3, 3: 1})
    50:(225, 24, {2: 3, 3: 1})
    51:(230, 12, {2: 2, 3: 1})
    52:(231, 12, {2: 2, 3: 1})
    53:(237, 12, {2: 2, 3: 1})
    54:(248, 24, {2: 3, 3: 1})
    55:(252, 6, {2: 1, 3: 1})

===
]]

===
]]]

#]]]'''#'''
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








__all__
from seed.math.factor_pint.factor_pint__smooth_group_order_method import factor_pint__smooth_group_order_method7Pmm_, factor_pint__smooth_group_order_method7Qpp_
from seed.math.factor_pint.factor_pint__smooth_group_order_method import *
