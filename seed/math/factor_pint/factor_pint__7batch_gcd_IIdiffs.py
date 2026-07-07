#__all__:goto
r'''[[[
e ../../python3_src/seed/math/factor_pint/factor_pint__7batch_gcd_IIdiffs.py

seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs
py -m nn_ns.app.debug_cmd   seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs:__doc__ -ht # -ff -df
#######

[[
view ../../python3_src/seed/math/polynomial/eval_polynomial/eval_polynomial_on_geometric_progression.py
===
@20260611
批量差积:计算冫积纟整个集合的任意俩不同元素的差:(*-*)
  [f(xs) := II[(a-b) | [a,b:<-xs][a=!=b]] %M]
  [ff(xs,ys) := II[(a-b) | [a:<-xs][b:<-ys][a=!=b]] %M]
  可以通过 多项式求值 实现快速算法！
    f(xs):分治:f(xsL),f(xsR)，再结合:ff(xsL,xsR)
    ff(xs,ys): 多项式 II[(X-b) | [b:<-ys]] 在 xs 上 求值
  * 随机生成集合
    生日悖论=>O(p**/2)
  * {B**j}
    不同层次的j
    [xs := {c**i | [i:<-[0..<K0]]}]
    [ys := {c**Kb*(c**Ke)**j | [j:<-[0..<K1]]}]
    [(ys *-* xs) %M
    == II[(c**Kb*(c**Ke)**j -c**i) | [i:<-[0..<K0]][j:<-[0..<K1]]] %M
    == II[(c**(Kb+Ke*j-i) -1)*c**i | [i:<-[0..<K0]][j:<-[0..<K1]]] %M
    ]
    [K == Ke == K0 == K1][Kb==0]:
        [M%p==0][order_mod_(p;c) < K**2] => [gcd(M,(ys *-* xs) %M) %p == 0]
          但若[p==1+2*q]则要求[K==O(p**/2)]
    [K == Ke == K0 == K1][Kb==Ku*K**2]:
        [M%p==0][Ku*K**2 <= order_mod_(p;c) < (1+Ku)*K**2] => [gcd(M,(ys *-* xs) %M) %p == 0]
          #增量搜索...内存限制
          #随机搜索...内存限制
  * {A**i} - {B**j}
    [(A**i-B**j) %p == 0]概率多大？
  * {h(b,c;i)} - {B**j}
    [h(b,c,0) := c]
    [h(b,c,1+i) := (b+h(b,c;i)**2)]
===
@20260612
完成:太慢了，只能独立单用
    本想作为一个插件:TODO: e ../../python3_src/seed/algo/rho_method__7iter.py
]]


'#'; __doc__ = r'#'
>>> factor_pint__7batch_gcd_IIdiffs_(257*(1+2**16), 3, 16) # <<== [16**2 >= phi_(257)]
([257], [])
>>> factor_pint__7batch_gcd_IIdiffs_(257*(1+2**16), 3, 15) # <<== [15**2 < phi_(257)]
([], [])

>>> from itertools import islice
>>> [*islice(iter_factor_pint__7batch_gcd_IIdiffs_(N:=17*37, x0:=3, sz:=-1+2**2, fancy_vs_native=False), 0, 9)]
[(0, [], []), (1, [], [5]), (2, [], []), (3, [17, 37], []), (4, [], []), (5, [17, 37], []), (6, [], []), (7, [17, 37], []), (8, [17], [])]
>>> [*islice(iter_factor_pint__7batch_gcd_IIdiffs_(N:=17*37, x0:=3, sz:=-1+2**2, fancy_vs_native=True), 0, 9)]
[(0, [], []), (1, [], [5]), (2, [], []), (3, [17, 37], []), (4, [], []), (5, [17, 37], []), (6, [], []), (7, [17, 37], []), (8, [17], [])]


postcondition:
    [@[k:<-ks4zero] -> [0 == II[((-1+x0**t) %N) | [t:<-[1+sz*k..=sz*(1+k)]]] %N]]
>>> k=5
>>> II_mod(N, (-1+pow(x0,t,N) for t in range(1+sz*k, 1+sz*(1+k))))
0

postcondition:
    offset => [@[n:<-nontrivial_factors] -> [0 == II[(x0**j -1) %n | [j:<-[(1+offset*szsz)..=(1+offset)*szsz]]] %n]]
>>> offset=3
>>> nontrivial_factors=[17, 37]
>>> for n in nontrivial_factors:
...     assert 0 == II_mod(N, (-1+pow(x0,j,N) for j in range(1+offset*sz**2, 1+(1+offset)*sz**2))), (n)



>>> factor_pint__7batch_gcd_IIdiffs_(257*(1+2**16), 3, 16, optimized6zpow=True)
([257], [])
>>> factor_pint__7batch_gcd_IIdiffs_(257*(1+2**16), 3, 15, optimized6zpow=True)
([], [])
>>> factor_pint__7batch_gcd_IIdiffs_(257*(1+2**16), 3, 16, optimized6zpow=False)
([257], [])
>>> factor_pint__7batch_gcd_IIdiffs_(257*(1+2**16), 3, 15, optimized6zpow=False)
([], [])



















[[
py_adhoc_call   seed.math.find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_   @find_the_min_primitive_root_mod_prime__using_factorization_of_pmm_ '={2: 8}'  =257
    3
py_adhoc_call   seed.math.find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_   @find_the_min_primitive_root_mod_prime__using_factorization_of_pmm_ '={2: 16}'  ='1+2**16'
    3
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='257*(1+2**16)' =3 ='16'
    ([257], [])
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='257*(1+2**16)' =3 ='15'
    ([], [])

]]
[[
py_adhoc_call   seed.math.find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_   @find_the_min_primitive_root_mod_prime__using_factorization_of_pmm_ '={2: 13, 29: 1, 101: 1, 179: 1}'  =4294991873
    3
py_adhoc_call   seed.math.find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_   @find_the_min_primitive_root_mod_prime__using_factorization_of_pmm_ '={2: 1, 3:1}'  =7
    3
py_adhoc_call   seed.math.find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_   @find_the_min_primitive_root_mod_prime__using_factorization_of_pmm_ '={2: 1, 5:1}'  =11
    2
py_adhoc_call   seed.math.Chinese_Remainder_Theorem__ver2   @apply_CRT -extended  ='[7,11]'  ='[3,2]'
    24

py_adhoc_call   seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='7*11' =24 =2
    ([], [])
py_adhoc_call   seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='7*11' =24 =3
    ([7], [])
py_adhoc_call   seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='7*11' =24 =2  --offset=2
    ([7], [])



]]
[[
M67:[x0:=2]最糟糕的情况
===
>67
: {193707721: 1, 761838257287: 1}

>>> 193707721 .bit_length()
28
>>> 88308 .bit_length()
17

py_adhoc_call   seed.math.factor_pint.factor_pint__naive_brute_force   ,iter_factor_pint__naive_brute_force_ =193707721-1  --max1_num_bits=29
193707721*761838257287==-1+2**67==147573952589676412927
193707721==1+2**3*3**3*5*67*2677
py_adhoc_call   seed.math.max_order_mod_   @order_mod_ ='(193707721-1)>>3' =2 ='[3,5,67,2677]'
    88308
py_adhoc_call   math   @isqrt =88308
    297
py_adhoc_call   seed.math.max_order_mod_   @order_mod_ ='(193707721)' =2 ='193707721-1' ='[2,3,5,67,2677]'
py_adhoc_call   seed.math.max_order_mod_   @order_mod_ ='(193707721)' =2 ='193707721-1' ='[2,3,5,67,2677]'
    67

===
???why fail???
    !! [order_mod_(-1+2**67;2) == 67] too small
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='-1+2**67' =2 ='9'
    ([], [8])
    total::duration: 0.47551814000000003 *(unit: 0:00:01)
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='-1+2**67' =2 ='8'
    ([], [])
    total::duration: 0.4490136880000001 *(unit: 0:00:01)



py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='-1+2**67' =2 ='2**9'
    新版:
    ([], [1, 2, 3, 4, 5, ..., 510, 511, 512])
    total::duration: 3.661708713 *(unit: 0:00:01)
    旧版:
    []
    total::duration: 5.772766154 *(unit: 0:00:01)
保留下列旧版输出:证明:O(sz*ln(sz)*lnln(sz)):

#旧版:且[sz:=2**10]实际上是[lbM==11]
假设:O(sz*ln(sz)*lnln(sz)):
    13.25 x2 --> 30.0
    13.25 x4 --> 67.0
    13.25 x8 --> 148.5
    :echo 13.25*(12.0/11)*2*log(12)/log(11)
    :echo 13.25*(13.0/11)*4*log(13)/log(11)
    :echo 13.25*(13.0/11)*8*log(13)/log(11)
假设:O(sz*ln(sz)):
    13.25 x2 --> 29
    13.25 x4 --> 62.6
    13.25 x8 --> 135.0
    :echo 13.25*(12.0/11)*2
    :echo 13.25*(13.0/11)*4
    :echo 13.25*(14.0/11)*8
假设:O(sz*ln(sz)**2):
    13.25 x2 --> 31.5
    13.25 x4 --> 74.0
    13.25 x8 --> 171.7
    :echo 13.25*pow(12.0/11.0,2)*2
    :echo 13.25*pow(13.0/11.0,2)*4
    :echo 13.25*pow(14.0/11.0,2)*8
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='-1+2**67' ='(False, (2**10, 2))'
    []
    total::duration: 13.250274873 *(unit: 0:00:01)
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='-1+2**67' ='(False, (2**11, 2))'
    []
    total::duration: 29.063826905000003 *(unit: 0:00:01)
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='-1+2**67' ='(False, (2**12, 2))'
    []
    total::duration: 65.765770542 *(unit: 0:00:01)



]]
[[
M67:[x0:=3]
_default4min_ez4M4recur=2
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='-1+2**67' =3 ='2**8'
    ([], [])
    total::duration: 1.7228267769999999 *(unit: 0:00:01)
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='-1+2**67' =3 ='2**9'
    ([], [])
    total::duration: 3.714471842 *(unit: 0:00:01)
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='-1+2**67' =3 ='2**12'
    ([], [])
    total::duration: 28.894737618 *(unit: 0:00:01)
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='-1+2**67' =3 ='2**13'
    ([], [])
    total::duration: 58.956489125 *(unit: 0:00:01)

???why fail???
    !! [193707721 .bit_length() == 28]
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='-1+2**67' =3 ='2**14'
    ([193707721], [])
    total::duration: 117.586852547 *(unit: 0:00:01)
    _default4min_ez4M4recur = 2
    _default4min_len4recur = 3

py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='-1+2**67' =999 ='2**9'
    ([], [])
    total::duration: 3.6981264059999996 *(unit: 0:00:01)


=========
_default4min_ez4M4recur=4
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='-1+2**67' =3 ='2**10'
    total::duration: 2.164931444 *(unit: 0:00:01)
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='-1+2**67' =3 ='2**11'
    total::duration: 3.937559703 *(unit: 0:00:01)
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='-1+2**67' =3 ='2**12'
    total::duration: 9.842352038 *(unit: 0:00:01)
=========
fix:sz=2**12
fix:_default4min_len4recur = 3
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='-1+2**67' =3 ='2**12'
_default4min_ez4M4recur=4
    total::duration: 9.842352038 *(unit: 0:00:01)
_default4min_ez4M4recur=5
    total::duration: 7.281013268000001 *(unit: 0:00:01)
_default4min_ez4M4recur=6
    total::duration: 7.281175234 *(unit: 0:00:01)
_default4min_ez4M4recur=9
    total::duration: 12.730962077 *(unit: 0:00:01)
_default4min_ez4M4recur=8
    total::duration: 12.393002973 *(unit: 0:00:01)
_default4min_ez4M4recur=7
    total::duration: 8.267685101 *(unit: 0:00:01)

=========
fix:sz=2**12
fix:_default4min_ez4M4recur = 5
    _default4min_len4recur:should match _default4min_ez4M4recur
_default4min_len4recur = 16
    total::duration: 7.306811389 *(unit: 0:00:01)
_default4min_len4recur = 32
    total::duration: 7.197319943 *(unit: 0:00:01)
_default4min_len4recur = 64
    total::duration: 7.362201423 *(unit: 0:00:01)
_default4min_len4recur = 24
    total::duration: 7.27977017 *(unit: 0:00:01)
_default4min_len4recur = 40
    total::duration: 7.692338782 *(unit: 0:00:01)
=========
fix:sz=2**14
fix:_default4min_ez4M4recur = 5
fix:_default4min_len4recur = 32
    total::duration: 30.656554515 *(unit: 0:00:01)

]]
[[
M1207:(-1+2**1207)
fix:_default4min_ez4M4recur = 5
fix:_default4min_len4recur = 32
cmp:kw:fancy_vs_native:
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='-1+2**1207' =3 ='2**7'
    total::duration: 0.7746513159999999 *(unit: 0:00:01)
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='-1+2**1207' =3 ='2**7' +fancy_vs_native
    total::duration: 0.313707778 *(unit: 0:00:01)
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='-1+2**1207' =3 ='2**8'
    total::duration: 1.276031086 *(unit: 0:00:01)
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='-1+2**1207' =3 ='2**8' +fancy_vs_native
    total::duration: 0.7553711500000001 *(unit: 0:00:01)
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='-1+2**1207' =3 ='2**9'
    ([131071, 228479], [])
    total::duration: 2.5418582360000004 *(unit: 0:00:01)
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='-1+2**1207' =3 ='2**9' +fancy_vs_native
    ([131071, 228479], [])
    total::duration: 2.5023634599999998 *(unit: 0:00:01)
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479' =3 ='2**10'
    total::duration: 4.494771076 *(unit: 0:00:01)
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479' =3 ='2**10' +fancy_vs_native
    total::duration: 9.178510253 *(unit: 0:00:01)
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479' =3 ='2**11'
    total::duration: 8.745499635 *(unit: 0:00:01)
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479' =3 ='2**11' +fancy_vs_native
    total::duration: 36.138675844 *(unit: 0:00:01)
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479' =3 ='2**12'
    total::duration: 21.566013433000002 *(unit: 0:00:01)
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479' =3 ='2**12' +fancy_vs_native
    total::duration: 144.248593731 *(unit: 0:00:01)

3-->5
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479' =5 ='2**12'
    ([48544121], [])
    total::duration: 21.689972340999997 *(unit: 0:00:01)
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479//48544121' =7 ='2**12'
    total::duration: 21.338051258 *(unit: 0:00:01)
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479//48544121' =11 ='2**12'  --offset=6
    total::duration: 21.366172194 *(unit: 0:00:01)
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479//48544121' =13 ='2**12'  --offset=7
    ([212885833], [])
    total::duration: 21.547251733 *(unit: 0:00:01)
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479//48544121//212885833' =17 ='2**12'  --offset=8
    total::duration: 20.076290508 *(unit: 0:00:01)
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479//48544121//212885833' =19 ='2**12'  --offset=80000
    total::duration: 20.393226055 *(unit: 0:00:01)
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479//48544121//212885833' =23 ='2**12'  --offset=9999
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479//48544121//212885833' =25 ='2**12'  --offset=99999
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479//48544121//212885833' ='29**30' ='2**12'  --offset=999999
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479//48544121//212885833' ='31' ='2**12'  --offset=9999999
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479//48544121//212885833' ='37' ='2**12'  --offset=9999_9999
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479//48544121//212885833' ='42' ='2**12'  --offset=9_9999_9999
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479//48544121//212885833' ='48' ='2**12'  --offset=99_9999_9999
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479//48544121//212885833' ='56' ='2**12'  --offset=999_9999_9999
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479//48544121//212885833' ='60' ='2**12'  --offset=9999_9999_9999
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479//48544121//212885833' ='61' ='2**12'  --offset=9_9999_9999_9999
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479//48544121//212885833' ='63' ='2**12'  --offset=99_9999_9999_9999
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479//48544121//212885833' ='66' ='2**12'  --offset=999_9999_9999_9999
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479//48544121//212885833' ='666' ='2**12'  --offset=9999_9999_9999_9999
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479//48544121//212885833' ='6666' ='2**12'  --offset=6_9999_9999_9999_9999
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479//48544121//212885833' ='66669' ='2**12'  --offset=66_9999_9999_9999_9999
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479//48544121//212885833' ='666699' ='2**12'  --offset=666_9999_9999_9999_9999
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479//48544121//212885833' ='6666999' ='2**12'  --offset=6666_9999_9999_9999_9999
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479//48544121//212885833' ='66669999' ='2**12'  --offset=6_6666_9999_9999_9999_9999
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479//48544121//212885833' ='666699996' ='2**12'  --offset=66_6666_9999_9999_9999_9999
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479//48544121//212885833' ='6666999966' ='2**12'  --offset=666_6666_9999_9999_9999_9999
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479//48544121//212885833' ='66669999666' ='2**12'  --offset=6666_6666_9999_9999_9999_9999
fail....

]]
[[
[best_sz == -1+2**ez]
    since [1+num_roots == 1+degree == num_coeffs]
    FFT{num_coeffs:=2**ez} => [sz==num_roots==-1+2**ez]
vs:
    *  9 seconds@[sz:=-1+2**12]
    * 20 seconds@[sz:=2**12]

[sz:=-1+2**12]:
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479//48544121//212885833' ='666699996666' ='-1+2**12'  --offset=6_6666_6666_9999_9999_9999_9999
    total::duration: 8.919303248 *(unit: 0:00:01)


[sz:=-1+2**13]:
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479//48544121//212885833' ='6666999966669' ='-1+2**13'  --offset=66_6666_6666_9999_9999_9999_9999
    total::duration: 21.164170992 *(unit: 0:00:01)
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479//48544121//212885833' ='66669999666699' ='-1+2**13'  --offset=666_6666_6666_9999_9999_9999_9999
    total::duration: 21.535224565 *(unit: 0:00:01)
py_adhoc_call { +to_show_timedelta +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   ,iter_factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479//48544121//212885833' ='17' ='-1+2**13'  --offset='2**607' +stop6ok
    0:duration: 21.015465134 *(unit: 0:00:01)
    1:duration: 10.618644633999999 *(unit: 0:00:01)
    2:duration: 10.489319719000001 *(unit: 0:00:01)
    3:duration: 10.475810175 *(unit: 0:00:01)
    4:duration: 10.625674492000002 *(unit: 0:00:01)
    ...
    ...
    (531137992816767098689588206552468627329593117727031923199444138200403559860852242739162502265229285668889329486246501015346579337652707239409519978766587351943831270835393219031728175, [], [])
    47:duration: 12.456458363000024 *(unit: 0:00:01)
    ^KeyboardInterrupt
    total::duration: 524.346967415 *(unit: 0:00:01)
    TODO

]]
[[
testing:
++kw:optimized6zpow
#see above:py_adhoc_call { +to_show_timedelta +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   ,iter_factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479//48544121//212885833' ='17' ='-1+2**13'  --offset='2**607' +stop6ok -optimized6zpow
py_adhoc_call { +to_show_timedelta +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   ,iter_factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479//48544121//212885833' ='17' ='2**13'  --offset='2**404' +stop6ok +optimized6zpow
    0: ... ...
    (41315998049390537434494706752048189989275292685267576205290549704650361952269459114074325652482205302974450751563959894016, [], [])
    #pre:0:duration: 33.419425473000004 *(unit: 0:00:01)
    0:duration: 21.634655211 *(unit: 0:00:01)
        ##after:++kw:optimized6zpow@mk_polynomial_coeffs5roots_on_geometric_progression_
    1: ... ...
    (41315998049390537434494706752048189989275292685267576205290549704650361952269459114074325652482205302974450751563959894017, [], [])
    1:duration: 11.160727951000005 *(unit: 0:00:01)
    2: ... ...
    (41315998049390537434494706752048189989275292685267576205290549704650361952269459114074325652482205302974450751563959894018, [], [])
    2:duration: 11.129016419000003 *(unit: 0:00:01)

]]
[[
[@[k:<-ks4zero] -> [0 == II[((-1+x0**t) %N) | [t:<-[1+sz*k..=sz*(1+k)]]] %N]]

py_adhoc_call { +to_show_timedelta +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   ,9:iter_factor_pint__7batch_gcd_IIdiffs_  ='17*37' =3 ='-1+2**2' +fancy_vs_native
    [N:=17*37][x0:=3][sz:=3][k:=5]:
        [II[((-1+x0**t) %N) | [t:<-[1+sz*k..=sz*(1+k)]]] %N
        == II[((-1+3**t) %N) | [t:<-[16..=18]]] %N
        == (-1+3**16)*(-1+3**17)*(-1+3**18) %(17*37)
        == 0 #ok
        ]
    <<==:
    0: ... ...
    (0, [], [])
    0:duration: 0.04941115699999998 *(unit: 0:00:01)
    1: ... ...
    (1, [], [5])
    1:duration: 0.0008639999999999759 *(unit: 0:00:01)
    2: ... ...
    (2, [], [])
    2:duration: 0.000546692999999987 *(unit: 0:00:01)
    3: ... ...
    (3, [17, 37], [])
    3:duration: 0.0008149239999999947 *(unit: 0:00:01)
    4: ... ...
    (4, [], [])
    4:duration: 0.0007153069999999984 *(unit: 0:00:01)
    5: ... ...
    (5, [17, 37], [])
    5:duration: 0.00048638400000000637 *(unit: 0:00:01)
    6: ... ...
    (6, [], [])
    6:duration: 0.0003861540000000274 *(unit: 0:00:01)
    7: ... ...
    (7, [17, 37], [])
    7:duration: 0.000737537999999982 *(unit: 0:00:01)
    8: ... ...
    (8, [17], [])
    8:duration: 0.001306230999999991 *(unit: 0:00:01)
    9: ... ...
    9:duration: 0.0007379229999999737 *(unit: 0:00:01)
    total::duration: 0.19958684799999998 *(unit: 0:00:01)
py_adhoc_call { +to_show_timedelta +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   ,9:iter_factor_pint__7batch_gcd_IIdiffs_  ='17*37' =3 ='-1+2**2' -fancy_vs_native -_debug
    同上
py_adhoc_call { +to_show_timedelta +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   ,9:iter_factor_pint__7batch_gcd_IIdiffs_  ='17*37' =3 ='-1+2**2' --offset=4 -fancy_vs_native -_debug

py_adhoc_call { +to_show_timedelta +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   ,9:iter_factor_pint__7batch_gcd_IIdiffs_  ='-1+2**1207' =3 ='-1+2**8' -fancy_vs_native
    0: ... ...
    (0, [], [])
    0:duration: 1.003686858 *(unit: 0:00:01)
    1: ... ...
    (1, [228479], [])
    1:duration: 0.2087683090000001 *(unit: 0:00:01)
    2: ... ...
    (2, [131071], [])
    2:duration: 0.19771276800000015 *(unit: 0:00:01)
    3: ... ...
    (3, [228479], [])
    3:duration: 0.19724830799999982 *(unit: 0:00:01)
    4: ... ...
    (4, [131071], [])
    4:duration: 0.19724830800000026 *(unit: 0:00:01)
    5: ... ...
    (5, [228479], [])
    5:duration: 0.1969952300000002 *(unit: 0:00:01)
    6: ... ...
    (6, [131071], [])
    6:duration: 0.19703592300000006 *(unit: 0:00:01)
    7: ... ...
    (7, [228479], [])
    7:duration: 0.19708477000000002 *(unit: 0:00:01)
    8: ... ...
    (8, [131071, 228479], [])
    8:duration: 0.19774584800000028 *(unit: 0:00:01)
    9: ... ...
    9:duration: 0.00022246199999997884 *(unit: 0:00:01)
    total::duration: 2.7438774009999998 *(unit: 0:00:01)
py_adhoc_call { +to_show_timedelta +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   ,9:iter_factor_pint__7batch_gcd_IIdiffs_  ='-1+2**1207' =3 ='-1+2**8' +fancy_vs_native
    同上

py_adhoc_call { +to_show_timedelta +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   ,9:iter_factor_pint__7batch_gcd_IIdiffs_  ='-1+2**1207' =3 ='-1+2**7' -fancy_vs_native
    [sz:=127][x0:=3][offset:=7]:
        [?[t:<-[1+offset*sz*sz..=(1+offset)*sz*sz]] -> [(-1+x0**t)%228479 == 0]]
        [127*127*7+1 == 112904]
        [127*127*8 == 129032]
        [?[t:<-[112904..=129032]] -> [(-1+3**t)%228479 == 0]]
        [t==114239]
    <<==:
    0: ... ...
    (0, [], [])
    0:duration: 0.739905388 *(unit: 0:00:01)
    1: ... ...
    (1, [], [])
    1:duration: 0.11583223099999995 *(unit: 0:00:01)
    2: ... ...
    (2, [], [])
    2:duration: 0.0869560009999999 *(unit: 0:00:01)
    3: ... ...
    (3, [], [])
    3:duration: 0.08675100099999988 *(unit: 0:00:01)
    4: ... ...
    (4, [], [])
    4:duration: 0.08679177000000005 *(unit: 0:00:01)
    5: ... ...
    (5, [], [])
    5:duration: 0.08651861500000013 *(unit: 0:00:01)
    6: ... ...
    (6, [], [])
    6:duration: 0.08649684600000018 *(unit: 0:00:01)
    7: ... ...
    (7, [228479], [])
    7:duration: 0.08673576999999999 *(unit: 0:00:01)
    8: ... ...
    (8, [131071], [])
    8:duration: 0.08675861499999993 *(unit: 0:00:01)
    9: ... ...
    9:duration: 0.0001803080000000179 *(unit: 0:00:01)
    total::duration: 1.5185997740000001 *(unit: 0:00:01)

]]





py_adhoc_call   seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @f
]]]'''#'''
__all__ = r'''
factor_pint__7batch_gcd_IIdiffs_
iter_factor_pint__7batch_gcd_IIdiffs_



mk_pows_mod_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.check import check_type_is, check_int_ge
    from math import gcd
    from seed.math.II import II_mod
    from seed.math.polynomial.eval_polynomial.eval_polynomial_on_geometric_progression import Eval_polynomial_on_geometric_progression__7modulus
        # Eval_polynomial_on_geometric_progression__7modulus(modulus, hrem_vs_mod=hrem_vs_mod).evals_(coeffs8poly, T, invT)
    from seed.math.polynomial.eval_polynomial.mk_polynomial_coeffs5roots_ import mk_polynomial_coeffs5roots_on_geometric_progression_
    #def mk_polynomial_coeffs5roots_on_geometric_progression_(opsX, may_B, T, sz, /):
    from seed.data_funcs.heap.heap_shape import heap_shape5num_leafs_, mk_rvheap__fill_, mk_rvheap__Nothing_
    #def mk_rvheap__fill_(parent5children_, leafs, /, *, inplace=False, with_fwd_idx=False, with_bwd_idc=False):
    from seed.types.view.SeqSliceView import SeqSliceView
    from seed.iters.find import iter_find

#.#################################
___end_mark_of_excluded_global_names__0___ = ...

def mk_pows_mod_(N, sz, x0, e0, /):
    check_int_ge(1, N)
    check_int_ge(1, sz)
    check_type_is(int, x0)
    x0 %= N
    xs = [pow(x0, e0, N)]
    for j in range(sz-1):
        xs.append(x0*xs[-1]%N)
    assert len(xs) == sz
    return xs
def factor_pint__7batch_gcd_IIdiffs_(N, x0, sz, /, offset=0, *, to_show_soon=False, fancy_vs_native=False, optimized6zpow=False):
    r'''[[[
    :: N/uint -> x0/int -> sz/uint -> offset/uint -> (nontrivial_factors, ks4zero)

    [best_sz == -1+2**ez]
        since [1+num_roots == 1+degree == num_coeffs]
        FFT{num_coeffs:=2**ez} => [sz==num_roots==-1+2**ez]
        ++kw:optimized6zpow:@20260617
            turn on optimization for [sz == 2**ez]

    # to factor N require [sz == O(min_prime_factor{N}**/2)]
    kw:fancy_vs_native:
        fancy => O(sz*ln(sz)*lnln(sz))
        native => O(sz**2)

    precondition:
        [gcd(N,x0) == 1]
    postcondition:
            offset => [@[n:<-nontrivial_factors] -> [0 == II[(x0**j -1) %n | [j:<-[(1+offset*szsz)..=(1+offset)*szsz]]] %n]]
        [@[n:<-nontrivial_factors] -> [[1 < n < N][N%n == 0]]]
        [@[k:<-ks4zero] -> [0 == II[((-1+x0**t) %N) | [t:<-[1+sz*k..=sz*(1+k)]]] %N]]


    [f(X) := II[(X -x0**(j-offset*sz) %N) | [j:<-[0..<sz]]] %N]
    [diffs := [f(X:=(x0**sz)**i) | [i:<-[0..<sz]]]]
    [diffs == [II[((x0**t -1) %N) | [t:<-[1+sz*(k-1)..<=sz*k]]] * x0**(-offset*sz**2 +sz*(sz-1)/2) %N | [k:<-[offset..<offset+sz]]]]

    #]]]'''#'''
    it = iter_factor_pint__7batch_gcd_IIdiffs_(N, x0, sz, offset, to_show_soon=to_show_soon, fancy_vs_native=fancy_vs_native, optimized6zpow=optimized6zpow)
    (offset, nontrivial_factors, ks4zero) = next(it)
    return (nontrivial_factors, ks4zero)
def iter_factor_pint__7batch_gcd_IIdiffs_(N, x0, sz, /, offset=0, *, to_show_soon=False, fancy_vs_native=False, stop6ok=False, _debug=False, optimized6zpow=False):
    'N/uint -> x0/int -> sz/uint -> offset/uint -> Iter (offset, nontrivial_factors, ks4zero) #see:factor_pint__7batch_gcd_IIdiffs_'
    # [gcd(N,x0) == 1]
    check_int_ge(4, N)
        # !! [1 < x0 < N-1]
    check_int_ge(0, offset)
    check_int_ge(1, sz)
    check_type_is(int, x0)
    x0 %= N
    if not 1 < x0 < N-1:raise ValueError(x0, N)
    ev = Eval_polynomial_on_geometric_progression__7modulus(N, hrem_vs_mod=True, optimized6zpowpp=optimized6zpow)
    opsN = ev.opsN
    if to_show_soon:
        if callable(to_show_soon):
            show_ = to_show_soon
        else:
            show_ = print
        show_
    else:
        def show_(*args, **kwds):
            pass
        show_
    show_
    to_show_soon = bool(to_show_soon)

    r'''[[[
    版本二:jx连续，可与_4native类比
        xs6offset__ver2
        xs6offset_snd_form__ver2
        ys__ver2
        diffs6offset__ver2
        diffs6offset_snd_form__ver2
        IIdiffs6offset__ver2
        data4update4csX_6offset__ver2
        update4csX_6offset__ver2
        update4invB_6offset__ver2

    [szsz := sz**2]
    [T := x0**sz %N]
    # useless:[B{offset} := T**(1+offset*sz) %N]
    [invT := x0**-sz %N]
    [invT_9sz := invT**sz %N]
    [invT_9sz == x0**-szsz %N]
    [invB{offset} := invT**(1+offset*sz) %N]

    [xs{offset} := [invB{offset}*x0**jx %N | [jx:<-[0..<sz]]]]
    [ys := [(x0**sz)**jy %N | [jy:<-[0..<sz]]]]

    [ys == T **. [0..<sz] %N] # ys__ver2:here
    [xs{offset} == invB{offset} *. x0 **. [0..<sz] %N] # xs6offset__ver2:here

    [xs{offset}
    == [invT**(1+offset*sz)*x0**jx %N | [jx:<-[0..<sz]]]
    == [(x0**-sz)**(1+offset*sz)*x0**jx %N | [jx:<-[0..<sz]]]
    == [x0**(jx-sz*(1+offset*sz)) %N | [jx:<-[0..<sz]]]
    == [x0**(jx-sz-offset*szsz)) %N | [jx:<-[0..<sz]]]
    == [x0**-(sz-jx+offset*szsz)) %N | [jx:<-[0..<sz]]]
    ]
    [xs{offset} == [x0**-(sz-jx+offset*szsz)) %N | [jx:<-[0..<sz]]]] # xs6offset_snd_form__ver2:here


    [csX{offset}(X) := polynomial{X;roots:=xs{offset}}.coeffs]
    [evals_(csX{offset}; ys) == [eval_(csX{offset}; ys[jy]) | [jy:<-[0..<sz]]]]
    [evals_(csX{offset}; ys) == [II[(ys[jy] -xs{offset}[jx]) | [jx:<-[0..<sz]]] %N | [jy:<-[0..<sz]]]]

    [diffs{offset} := evals_(csX{offset}; ys)]

    [diffs{offset}
    == evals_(csX{offset}; ys)
    == [II[(ys[jy] -xs{offset}[jx]) | [jx:<-[0..<sz]]] %N | [jy:<-[0..<sz]]]
    == [II[(T**jy -invB{offset} * x0**jx) | [jx:<-[0..<sz]]] %N | [jy:<-[0..<sz]]]
    == [II[(T**jy -invT**(1+offset*sz) * x0**jx) | [jx:<-[0..<sz]]] %N | [jy:<-[0..<sz]]]
    == [II[invT**(1+offset*sz) * (T**(jy+1+offset*sz) -x0**jx) | [jx:<-[0..<sz]]] %N | [jy:<-[0..<sz]]]
    == [II[invT**(1+offset*sz) * x0**jx * (x0**-jx * T**(jy+1+offset*sz) -1) | [jx:<-[0..<sz]]] %N | [jy:<-[0..<sz]]]
    == [invT**(sz*(1+offset*sz)) * II[x0**jx * (x0**-jx * (x0**sz)**(jy+1+offset*sz) -1) | [jx:<-[0..<sz]]] %N | [jy:<-[0..<sz]]]
    == [invT**(sz*(1+offset*sz)) * II[x0**jx * (x0**((sz-jx)+jy*sz+offset*szsz) -1) | [jx:<-[0..<sz]]] %N | [jy:<-[0..<sz]]]
    # [jx:=(sz-1-rjx)]
    == [invT**(sz*(1+offset*sz)) * II[x0**jx | [jx:<-[0..<sz]]] * II[(x0**(1+rjx+jy*sz+offset*szsz) -1) | [rjx:<-[0..<sz]]] %N | [jy:<-[0..<sz]]]
    == [invT**(sz*(1+offset*sz)) * x0**sum[jx | [jx:<-[0..<sz]]] * II[(x0**sjx -1) | [sjx:<-[base+0..<base+sz]]] %N | [jy:<-[0..<sz]][base:=(1+jy*sz+offset*szsz)]]
    == [(x0**-sz)**(sz*(1+offset*sz)) * x0**(sz*(sz-1)///2) * II[(x0**sjx -1) | [sjx:<-[base+0..<base+sz]]] %N | [jy:<-[0..<sz]][base:=(1+jy*sz+offset*szsz)]]
    == [x0**(-szsz-offset*szszsz +(szsz-sz)/2) * II[(x0**sjx -1) | [sjx:<-[base+0..<base+sz]]] %N | [jy:<-[0..<sz]][base:=(1+jy*sz+offset*szsz)]]
    == [x0**(-(2*offset*szsz +sz+1)*sz/2) * II[(x0**sjx -1) | [sjx:<-[base+0..<base+sz]]] %N | [jy:<-[0..<sz]][base:=(1+jy*sz+offset*szsz)]]
    ]

    [diffs{offset} == [x0**(-(2*offset*szsz +sz+1)*sz/2) * II[(x0**sjx -1) | [sjx:<-[base+0..<base+sz]]] %N | [jy:<-[0..<sz]][base:=(1+jy*sz+offset*szsz)]]] # diffs6offset__ver2:here
        # 内层sjx连续
    # [jy:=k-offset*sz]
    [diffs{offset} == [x0**(-(2*offset*szsz +sz+1)*sz/2) * II[(x0**sjx -1) | [sjx:<-[base+0..<base+sz]]] %N | [k:<-[offset*sz..<(1+offset)*sz]][base:=(1+sz*k)]]]
    [diffs{offset} == [x0**(-(2*offset*szsz +sz+1)*sz/2) * II[(x0**sjx -1) | [sjx:<-[(1+sz*k)..=sz*(1+k)]]] %N | [k:<-[offset*sz..<(1+offset)*sz]]]]
    # [sjx:=t]
    [diffs{offset} == [x0**(-(2*offset*szsz +sz+1)*sz/2) * II[(x0**t -1) | [t:<-[(1+sz*k)..=sz*(1+k)]]] %N | [k:<-[offset*sz..<(1+offset)*sz]]]] # diffs6offset_snd_form__ver2:here

    [II(diffs{offset}) %N
    == II[x0**(-(2*offset*szsz +sz+1)*sz/2) * II[(x0**sjx -1) | [sjx:<-[base+0..<base+sz]]] %N | [jy:<-[0..<sz]][base:=(1+jy*sz+offset*szsz)]] %N
    == II[x0**(-(2*offset*szsz +sz+1)*sz/2) %N | [jy:<-[0..<sz]]] * II[(x0**sjx -1) %N | [jy:<-[0..<sz]][base:=(1+jy*sz+offset*szsz)][sjx:<-[base+0..<base+sz]]] %N
    == x0**(-(2*offset*szsz +sz+1)*szsz/2) * II[(x0**sjx -1) %N | [jy:<-[0..<sz]][jx:<-[0..<sz]][sjx:=(1+jx+jy*sz+offset*szsz)]] %N
    == x0**(-(2*offset*szsz +sz+1)*szsz/2) * II[(x0**sjx -1) %N | [jj:<-[0..<szsz]][sjx:=(1+jj+offset*szsz)]] %N
    == x0**(-(2*offset*szsz +sz+1)*szsz/2) * II[(x0**j -1) %N | [j:<-[(1+offset*szsz)..<(1+(1+offset)*szsz)]]] %N
    == x0**(-(2*offset*szsz +sz+1)*szsz/2) * II[(x0**j -1) %N | [j:<-[(1+offset*szsz)..=(1+offset)*szsz]]] %N
    ]

    [II(diffs{offset}) %N == x0**(-(2*offset*szsz +sz+1)*szsz/2) * II[(x0**j -1) %N | [j:<-[(1+offset*szsz)..=(1+offset)*szsz]]] %N] # IIdiffs6offset__ver2:here



    # transform:csX{offset} --> csX{1+offset}
    !! [invB{offset} := invT**(1+offset*sz) %N]
    [invB{1+offset} == invT**(1+(1+offset)*sz) %N]
    [invB{1+offset} == invT**sz * invT**(1+offset*sz) %N]
    [invB{1+offset} == (invT_9sz * invB{offset}) %N] # update4invB_6offset__ver2:here

    !! [xs{offset} == invB{offset} *. x0 **. [0..<sz] %N] # xs6offset__ver2:goto
    [xs{1+offset} == invB{1+offset} *. x0 **. [0..<sz] %N]
    [xs{1+offset} == (invT**sz * invB{offset}) *. x0 **. [0..<sz] %N]
    [xs{1+offset} == invT**sz *. (invB{offset} *. x0 **. [0..<sz]) %N]
    [xs{1+offset} == invT**sz *. xs{offset} %N]


    !! [csX{offset}(X) := polynomial{X;roots:=xs{offset}}.coeffs]
    [csX{1+offset}(X) == polynomial{X;roots:=xs{1+offset}}.coeffs]
    [sum[csX{1+offset}[jc] * X**jc | [jc:<-[0..=sz]]]
    == polynomial{X;roots:=xs{1+offset}}
    == II[(X -xs{1+offset}[jx]) | [jx:<-[0..<sz]]] %N
    !! [xs{1+offset} == invT**sz *. xs{offset} %N]
    == II[(X -invT**sz * xs{offset}[jx] %N) | [jx:<-[0..<sz]]] %N
    == II[invT**sz * ((T**sz * X) -xs{offset}[jx]) | [jx:<-[0..<sz]]] %N
    == invT**szsz * II[((T**sz * X) -xs{offset}[jx]) | [jx:<-[0..<sz]]] %N
    == invT**szsz * polynomial{(T**sz * X);roots:=xs{offset}} %N
    !! [csX{offset}(X) := polynomial{X;roots:=xs{offset}}.coeffs]
    == invT**szsz * sum[csX{offset}[jc]*(T**sz * X)**jc %N | [jc:<-[0..=sz]]] %N
    == sum[(invT**szsz * csX{offset}[jc]*(T**sz)**jc %N) * X**jc | [jc:<-[0..=sz]]] %N
    == sum[(invT**(szsz-sz*jc) * csX{offset}[jc] %N) * X**jc | [jc:<-[0..=sz]]] %N
    == sum[((invT**sz)**(sz-jc) * csX{offset}[jc] %N) * X**jc | [jc:<-[0..=sz]]] %N
    ]

    [sum[csX{1+offset}[jc] * X**jc | [jc:<-[0..=sz]]] %N == sum[((invT**sz)**(sz-jc) * csX{offset}[jc]) * X**jc | [jc:<-[0..=sz]]] %N]
    [csX{1+offset} == [((invT**sz)**(sz-jc) * csX{offset}[jc] %N) | [jc:<-[0..=sz]]]]
    [csX{1+offset} == csX{offset} .*. [(invT**sz)**(sz-jc) %N | [jc:<-[0..=sz]]]]
    [csX{1+offset} == csX{offset} .*. reverse [(invT**sz)**jc %N | [jc:<-[0..=sz]]] %N]
    [csX{1+offset} == csX{offset} .*. (reverse ((invT**sz) **. [0..=sz])) %N]
    [csX{1+offset} == csX{offset} .*. (reverse (invT_9sz **. [0..=sz])) %N]
    [ts := (reverse (invT_9sz **. [0..=sz])) %N] # data4update4csX_6offset__ver2:here
    [csX{1+offset} == csX{offset} .*. ts %N] # update4csX_6offset__ver2:here



    #]]]'''#'''
    r'''[[[
    版本一:jx不连续，无法与_4native类比
    [szsz := sz**2]
    [T := x0**sz %N]
    [B{offset} := T**(1+offset*sz) %N]
    [xs := [x0**j %N | [j:<-[0..<sz]]]]
    [ys{offset} := [(x0**sz)*(x0**sz)**(j+offset*sz) %N | [j:<-[0..<sz]]]]
    [ys{offset} == [T**(j+1+offset*sz) %N | [j:<-[0..<sz]]]]
    [ys{offset} == T**(1+offset*sz) * [T**j %N | [j:<-[0..<sz]]]]

    [ys{offset} == B{offset} * T **. [0..<sz] %N]
    [xs == x0 **. [0..<sz] %N]
    [csY{offset}(X) := polynomial{X;roots:=ys{offset}}.coeffs]
    [evals_(csY{offset}; xs) == [eval_(csY{offset}; xs[jx]) | [jx:<-[0..<sz]]]]
    [evals_(csY{offset}; xs) == [II[(xs[jx] -ys{offset}[jy]) | [jy:<-[0..<sz]]] %N | [jx:<-[0..<sz]]]]
    [diffs{offset} := evals_(csY{offset}; xs)]

    [diffs{offset}
    == evals_(csY{offset}; xs)
    == [II[(xs[jx] -ys{offset}[jy]) | [jy:<-[0..<sz]]] %N | [jx:<-[0..<sz]]]
    == [II[(x0**jx -B{offset} * T**jy) %N | [jy:<-[0..<sz]]] %N | [jx:<-[0..<sz]]]
    == [II[(x0**jx -T**(1+offset*sz) * T**jy) %N | [jy:<-[0..<sz]]] %N | [jx:<-[0..<sz]]]
    == [II[x0**jx * (1 -x0**-jx * T**(jy+1+offset*sz)) %N | [jy:<-[0..<sz]]] %N | [jx:<-[0..<sz]]]
    == [II[x0**jx %N | [jy:<-[0..<sz]]] * II[(1 -x0**-jx * T**(jy+1+offset*sz)) %N | [jy:<-[0..<sz]]] %N | [jx:<-[0..<sz]]]
    == [((x0**jx)**sz %N) * II[(1 -x0**-jx * (x0**sz)**(jy+1+offset*sz)) %N | [jy:<-[0..<sz]]] %N | [jx:<-[0..<sz]]]
    == [((x0**sz)**jx %N) * (-1)**sz *II[(-1+x0**((sz-jx)+jy*sz+offset*szsz)) %N | [jy:<-[0..<sz]]] %N | [jx:<-[0..<sz]]]
    == [(-1)**sz * ((x0**sz)**(sz-1-rjx) %N) * II[(-1+x0**(1+rjx+jy*sz+offset*szsz)) %N | [jy:<-[0..<sz]]] %N | [jx:<-[0..<sz]][rjx:=(sz-1-jx)]]
    ]

    [diffs{offset} == [(-1)**sz * ((x0**sz)**(sz-1-rjx) %N) * II[(-1+x0**(1+rjx+jy*sz+offset*szsz)) %N | [jy:<-[0..<sz]]] %N | [jx:<-[0..<sz]][rjx:=(sz-1-jx)]]]
        # jx在外层，即内部jx不连续
        #   diffs{offset}[jx]

    [II(diffs{offset})
    == II[(-1)**sz * ((x0**sz)**(sz-1-rjx) %N) * II[(-1+x0**(1+rjx+jy*sz+offset*szsz)) %N | [jy:<-[0..<sz]]] %N | [jx:<-[0..<sz]][rjx:=(sz-1-jx)]]
    == (-1)**szsz * II[((x0**sz)**(sz-1-rjx) %N) %N | [jx:<-[0..<sz]][rjx:=(sz-1-jx)]] * II[II[(-1+x0**(1+rjx+jy*sz+offset*szsz)) %N | [jy:<-[0..<sz]]] %N | [jx:<-[0..<sz]][rjx:=(sz-1-jx)]]
    == (-1)**szsz * ((x0**sz)**sum[jx | [jx:<-[0..<sz]]] %N) * II[(-1+x0**(1+rjx+jy*sz+offset*szsz)) %N | [jy:<-[0..<sz]][rjx:<-[0..<sz]]]
    == (-1)**(sz%2) * ((x0**sz)**(sz*(sz-1)///2) %N) * II[(-1+x0**(1+j+offset*szsz)) %N | [j:<-[0..<szsz]]]
    == (-1)**(sz%2) * (x0**(szsz*(sz-1)///2) %N) * II[(-1+x0**j) %N | [base:=(1+offset*szsz)][j:<-[base+0..<base+szsz]]]
    ]

    #]]]'''#'''

    def _4fancy(offset, /, *, N=N, sz=sz, x0=x0, debug=_debug):

        # !! [gcd(N,x0) == 1]
        inv_x0 = pow(x0, -1, N)
        # [inv_x0 == x0**-1%N]
        invT = pow(inv_x0, sz, N)
        # [invT == x0**-sz%N]
        invT_9sz = pow(invT, sz, N)
        # [invT_9sz == x0**-szsz %N]
        #invB_6offset = pow(invT, 1+offset*sz, N) # bias
        invB_6offset = invT*pow(invT_9sz, offset, N) %N # bias
        # [invB{offset} == invT**(1+offset*sz) %N]
        ###########################
        # !! [xs{offset} == invB{offset} *. x0 **. [0..<sz] %N] # xs6offset__ver2:goto
        csX_6offset = mk_polynomial_coeffs5roots_on_geometric_progression_(opsN, invB_6offset, x0, sz, optimized6zpow=optimized6zpow)
            #优化:几何级数:II[(x-x0**(i*K+j)) | i,j...] == x0**??? * II[(x/x0**(i*Kj) -x0**j0) | i,j...]
            # O(sz*ln(sz)*lnln(sz))
        if not debug:
            invB_6offset = None

        T = pow(invT, -1, N)
        # !! [invT == x0**-sz%N]
        # [T == x0**sz%N]

        # !! [gcd(N,x0) == 1]
        # [gcd(N,T) == 1]

        to_init = True
        while 1:
            assert -1+len(csX_6offset) == sz
            assert csX_6offset[-1] == 1
            # [xs{offset} == invB{offset} *. x0 **. [0..<sz] %N]
            # [xs{offset} == [x0**-(sz-jx+offset*szsz)) %N | [jx:<-[0..<sz]]]] # xs6offset_snd_form__ver2:goto
            # [polynomial{csX_6offset;X} == II[(X -x0**-(sz-jx+offset*szsz) %N) | [jx:<-[0..<sz]]] %N]

            ########################
            # !! [ys == T **. [0..<sz] %N] # ys__ver2:goto
            diffs_ = ev.evals_(coeffs8poly:=csX_6offset, T, invT)
                # O(sz*ln(sz)*lnln(sz))
            assert -1+len(diffs_) == sz
            777;diffs_.pop()
            777;diffs6offset, diffs_ = diffs_, None
            assert len(diffs6offset) == sz
            # diffs6offset__ver2:goto
            # diffs6offset_snd_form__ver2:goto
            # IIdiffs6offset__ver2:goto
            yield (offset, diffs6offset)
            #########
            if to_init:
                to_init = False
                # !! [ts := (reverse (invT_9sz **. [0..=sz])) %N] # data4update4csX_6offset__ver2:goto
                ts = mk_pows_mod_(N, 1+sz, invT_9sz, 0)
                777;ts.reverse()
            ts
            # !! [csX{1+offset} == csX{offset} .*. ts %N] # update4csX_6offset__ver2:goto
            csX_6offsetpp = [*map(opsN.mul_, csX_6offset, ts)]
            if debug:
                # !! [invB{1+offset} == (invT_9sz * invB{offset}) %N] # update4invB_6offset__ver2:goto
                invB_6offsetpp = invB_6offset * invT_9sz %N

            #########
            if debug:
                print('offset=', offset)
                print('csX_6offset=', csX_6offset)
                print('ts=', ts)
                print('csX_6offsetpp=', csX_6offsetpp)
                print('diffs6offset=', diffs6offset)
            #########
            #next round:
            offset += 1
            csX_6offset = csX_6offsetpp
            if debug:
                invB_6offset = invB_6offsetpp
            #########
            if debug:
                _csX_6offset = mk_polynomial_coeffs5roots_on_geometric_progression_(opsN, invB_6offset, x0, sz)
                print('_csX_6offset=', _csX_6offset)
                if not csX_6offset == _csX_6offset: raise Exception(csX_6offset, _csX_6offset)
            #########
        #########
    def _4native(offset, /, *, N=N, sz=sz, x0=x0):
        # diff from _4fancy():by drop: 『x0**???』
        # [xs{offset} == [x0**-(sz-jx+offset*szsz)) %N | [jx:<-[0..<sz]]]] # xs6offset_snd_form__ver2:goto
        # [polynomial{csX_6offset;X} == II[(X -x0**-(sz-jx+offset*szsz) %N) | [jx:<-[0..<sz]]] %N]
        szsz = sz**2
        z = pow(x0, offset*szsz, N)
        # [z == x0**(offset*szsz) %N]
        while 1:
            # [z == x0**(offset*szsz) %N]
            jy = 0
            diffs = []
            # [diffs == [II[(-1+x0**(1+_jx +_jy*sz +offset*szsz)) %N | [_jx:<-[0..<sz]]] %N] | [_jy:<-[0..<jy]]]
            for jy in range(sz):
                # [z == x0**(jy*sz +offset*szsz) %N]
                # [diffs == [II[(-1+x0**(1+_jx +_jy*sz +offset*szsz)) %N | [_jx:<-[0..<sz]]] %N] | [_jy:<-[0..<jy]]]
                jx = 0
                IIdiffs = 1
                # [IIdiffs = II[(-1+x0**(1+_jx +jy*sz +offset*szsz)) %N | [_jx:<-[0..<jx]]] %N]
                for jx in range(sz):
                    # [z == x0**(jx +jy*sz +offset*szsz) %N]
                    # [IIdiffs = II[(-1+x0**(1+_jx +jy*sz +offset*szsz)) %N | [_jx:<-[0..<jx]]] %N]
                    z = z*x0%N
                    # [z == x0**(1 +jx +jy*sz +offset*szsz) %N]
                    IIdiffs = IIdiffs*(z-1)%N
                    # [IIdiffs = II[(-1+x0**(1+_jx +jy*sz +offset*szsz)) %N | [_jx:<-[0..=jx]]] %N]
                    # [z == x0**((1+jx) +jy*sz +offset*szsz) %N]
                # [z == x0**((1+jy)*sz +offset*szsz) %N]
                # [IIdiffs = II[(-1+x0**(1+_jx +jy*sz +offset*szsz)) %N | [_jx:<-[0..<sz]]] %N]
                # [diffs == [II[(-1+x0**(1+_jx +_jy*sz +offset*szsz)) %N | [_jx:<-[0..<sz]]] %N] | [_jy:<-[0..<jy]]]
                diffs.append(IIdiffs)
                # [diffs == [II[(-1+x0**(1+_jx +_jy*sz +offset*szsz)) %N | [_jx:<-[0..<sz]]] %N] | [_jy:<-[0..=jy]]]
            # [diffs == [II[(-1+x0**(1+_jx +_jy*sz +offset*szsz)) %N | [_jx:<-[0..<sz]]] %N] | [_jy:<-[0..<sz]]]
            # [diffs == [II[(-1+x0**(1+jx +jy*sz +offset*szsz)) %N | [jx:<-[0..<sz]]] %N] | [jy:<-[0..<sz]]]
            assert len(diffs) == sz
            # drop: 『x0**???』
            # [diffs == [II[(-1+x0**(1+jx +sz*(jy +offset*sz))) %N | [jx:<-[0..<sz]]] %N] | [jy:<-[0..<sz]]]
            # [jy:=k-offset*sz]
            # [diffs == [II[(-1+x0**(1+jx +sz*k)) %N | [jx:<-[0..<sz]]] %N] | [k:<-[offset*sz..<(1+offset)*sz]]]
            # [jx:=t-1-sz*k]
            # [diffs{offset} == [II[((-1+x0**t) %N) | [t:<-[1+sz*k..=sz*(1+k)]]] %N | [k:<-[offset*sz..<(1+offset)*sz]]]]
            yield (offset, diffs)
            #########
            #next round:
            offset += 1
            #########
        #########

    def main(*, offset0=offset):
        iter_ = (_4fancy if not fancy_vs_native else _4native)
        it = iter_(offset0)
        for j, (_offset, diffs) in enumerate(it, offset0):
            assert _offset == j
            assert len(diffs) == sz
            # [diffs == [polynomial{cs0_off;X}(X:=T**i) | [i:<-[0..<sz]]]]
            yield (rss := _postprocess(show_, N, sz, _offset, diffs))
            if stop6ok:
                (offset, nontrivial_factors, ks4zero) = rss
                if nontrivial_factors or ks4zero:
                    break

    del offset
    return main()
def _postprocess(show_, N, sz, offset, diffs, /):
    assert len(diffs) == sz
    # _4native => [diffs{offset} == [II[((-1+x0**t) %N) | [t:<-[1+sz*k..=sz*(1+k)]]] %N | [k:<-[offset*sz..<(1+offset)*sz]]]]
    # _4fancy => [diffs{offset} == [x0**(-(2*offset*szsz +sz+1)*sz/2) * II[(x0**t -1) | [t:<-[(1+sz*k)..=sz*(1+k)]]] %N | [k:<-[offset*sz..<(1+offset)*sz]]]] # diffs6offset_snd_form__ver2:goto

    #idc4zero = find_indices_(diffs, 0)
    idc4zero = [*iter_find(diffs, 0)]
        #优化:定位所有0点，[x0**e%N==1][phi_(N)%e == 0]
        # O(sz)
    # [@[i:<-idc4zero] -> [diffs[i] == 0]]
    # !! _4fancy => [diffs{offset} == [x0**(-(2*offset*szsz +sz+1)*sz/2) * II[(x0**t -1) | [t:<-[(1+sz*k)..=sz*(1+k)]]] %N | [k:<-[offset*sz..<(1+offset)*sz]]]] # diffs6offset_snd_form__ver2:goto
    # !! [gcd(N,x0) == 1]
    # [@[i:<-idc4zero] -> [k:=(i+offset*sz)] -> [II[((-1+x0**t) %N) | [t:<-[1+sz*k..=sz*(1+k)]]] %N == 0]]
    off_sz = offset*sz
    ks4zero = [i+off_sz for i in idc4zero]
    if ks4zero: show_(('ks4zero', ks4zero))
    # [@[k:<-ks4zero] -> [0 == II[((-1+x0**t) %N) | [t:<-[1+sz*k..=sz*(1+k)]]] %N]]
    sz4diffs = len(diffs)
    (IIdiffs, rvheap) = _II_mod_ex_(N, diffs)
        #优化:二叉树
        # O(sz)
    rvheap = diffs
    777; diffs = SeqSliceView(rvheap, range(sz4diffs))
    assert len(rvheap) == -1+2*sz4diffs
    #IIdiffs = II_mod(N, filter(bool, diffs))
    #m = gcd(N, IIdiffs)
    nontrivial_gcds = _iter_nontrivial_gcds_(N, rvheap, show_)
        #优化:二叉树
        # O(sz)
    nontrivial_factors = sorted(set(nontrivial_gcds))
    # [@[n:<-nontrivial_factors] -> [[1 < n < N][N%n == 0]]]
    # !! _4fancy => [II(diffs{offset}) %N == x0**(-(2*offset*szsz +sz+1)*szsz/2) * II[(x0**j -1) %N | [j:<-[(1+offset*szsz)..=(1+offset)*szsz]]] %N] # IIdiffs6offset__ver2:goto
    # offset => [@[n:<-nontrivial_factors] -> [0 == II[(x0**j -1) %n | [j:<-[(1+offset*szsz)..=(1+offset)*szsz]]] %n]]



    ######################
    # postcondition:
    # offset => [@[n:<-nontrivial_factors] -> [0 == II[(x0**j -1) %n | [j:<-[(1+offset*szsz)..=(1+offset)*szsz]]] %n]]
    # [@[n:<-nontrivial_factors] -> [[1 < n < N][N%n == 0]]]
    # [@[k:<-ks4zero] -> [0 == II[((-1+x0**t) %N) | [t:<-[1+sz*k..=sz*(1+k)]]] %N]]
    return (offset, nontrivial_factors, ks4zero)


    r'''[[[

    match either_sz_x0_or_xs0:
        case (False, (sz, x0)):
            assert 1 < x0 < N
            x0 %= N
            xs0 = mk_pows_mod_(N, sz, x0, 0)
        case (True, xs0):
            assert len(xs0) == sz
            assert xs0[0] == 1
            x0 = xs0[1]
            assert 1 < x0 < N
        case _:
            raise Exception(either_sz_x0_or_xs0)
    x0 %= N
    xs0
    # [xs0 == [x0**j %N | [j:<-[0..<sz]]]]

    #xs1 = mk_pows_mod_(N, sz, x1)
    T = x1 = x0*xs0[-1]%N #pow(x0, sz, N)
    # [T == x0**sz %N]
    # !! [gcd(N,x0) == 1]
    # [gcd(N,x1) == 1]
    if offset:
        bias = pow(x1, -offset, N)
        # [bias == x0**(-offset*sz) %N]
        xs0_off = [bias*u%N for u in xs0]
        # [xs0_off == [x0**(j-offset*sz) %N | [j:<-[0..<sz]]]]
    else:
        # [offset == 0]
        xs0_off = xs0
    xs0_off
    # [xs0_off == [x0**(j-offset*sz) %N | [j:<-[0..<sz]]]]
    cs0_off = mk_polynomial_coeffs5roots_(opsN, xs0_off)

    #]]]'''#'''
def _II_mod_ex_(N, diffs, /):
    def parent5children_(k, node6vj, node6vi, /):
        # [k%2 == 0][sz >= sz-k == vj == 1+vi > vi == 2*vparent > vparent >= 1]
        # [node6k is node6vj is rvheap8vj2node[-vj] is rvheap8vj2node[k]]
        if node6vj == 0:
            node6vj = 1
        if node6vi == 0:
            node6vi = 1
        return node6vj*node6vi%N

    rvheap = mk_rvheap__fill_(parent5children_, diffs, inplace=True, with_fwd_idx=True, with_bwd_idc=False)
    assert rvheap is diffs
    IIdiffs = rvheap[-1]
    return (IIdiffs, rvheap)
def _iter_nontrivial_gcds_(N, rvheap, show_, /):
    sz = len(rvheap)
    bs = [False]*sz
    bs[-1] = True
    for vj in range(1, 1+sz):
        if not bs[-vj]:continue
        u = gcd(N, rvheap[-vj])
        if u == 1:continue
        # [1 < u <= N]
        vchild = 2*vj
        if vchild > sz:
            # vj is leaf
            if u < N:
                # [1 < u < N]
                show_(('factor', u))
                yield u
            continue
        # [1 < u <= N]
        try:
            for vchild in [1+vchild, vchild]:
                # turnoff:step_into
                #bug:bs[vchild] = True
                bs[-vchild] = True
        except IndexError:
            raise IndexError(sz, vj, 2*vj, vchild)




__all__
from seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs import factor_pint__7batch_gcd_IIdiffs_, iter_factor_pint__7batch_gcd_IIdiffs_
from seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs import *
