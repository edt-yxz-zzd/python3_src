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
sz be (-1+2**ez):
    since [1+num_roots == degree]
    FFT{degree:=2**ez} => [sz==num_roots==-1+2**ez]
vs:
    *  9 seconds@[sz:=-1+2**12]
    * 20 seconds@[sz:=2**12]

[sz:=-1+2**12]:
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479//48544121//212885833' ='666699996666' ='-1+2**12'  --offset=6_6666_6666_9999_9999_9999_9999
    total::duration: 8.919303248 *(unit: 0:00:01)


[sz:=-1+2**13]:
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @factor_pint__7batch_gcd_IIdiffs_  ='(-1+2**1207)//131071//228479//48544121//212885833' ='6666999966669' ='-1+2**13'  --offset=66_6666_6666_9999_9999_9999_9999
    total::duration: 21.164170992 *(unit: 0:00:01)
]]




py_adhoc_call   seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs   @f
from seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs import *
]]]'''#'''
__all__ = r'''
factor_pint__7batch_gcd_IIdiffs_




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
    from seed.math.polynomial.eval_polynomial.mk_polynomial_coeffs5roots_ import mul7polynomial_, mk_polynomial_coeffs5roots_, mk_polynomial_coeffs5roots_on_geometric_progression_
    #def mk_polynomial_coeffs5roots_on_geometric_progression_(opsX, may_B, T, invT, sz, /):
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
def factor_pint__7batch_gcd_IIdiffs_(N, x0, sz, /, offset=1, *, to_show_soon=False, fancy_vs_native=False):
    r'''[[[
    :: N/uint -> x0 -> sz -> offset -> (nontrivial_factors, ks4zero)

    [best_sz == -1+2**ez]

    # to factor N require [sz == O(min_prime_factor{N}**/2)]
    kw:fancy_vs_native:
        fancy => O(sz*ln(sz))
        native => O(sz**2)

    precondition:
        [gcd(N,x0) == 1]
    postcondition:
        [@[n:<-nontrivial_factors] -> [[1 < n < N][N%n == 0]]]
        [@[k:<-ks4zero] -> [0 == II[((x0**t -1) %N) | [t:<-[1+sz*(k-1)..<=sz*k]]] %N]]


    [f(X) := II[(X -x0**(j-offset*sz) %N) | [j:<-[0..<sz]]] %N]
    [diffs := [f(X:=(x0**sz)**i) | [i:<-[0..<sz]]]]
    [diffs == [II[((x0**t -1) %N) | [t:<-[1+sz*(k-1)..<=sz*k]]] * x0**(-offset*sz**2 +sz*(sz-1)/2) %N | [k:<-[offset..<offset+sz]]]]

    #]]]'''#'''
    # [gcd(N,x0) == 1]
    check_int_ge(3, N)
    check_int_ge(1, offset)
    ev = Eval_polynomial_on_geometric_progression__7modulus(N, hrem_vs_mod=True)
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


    x0 %= N
    assert 1 < x0 < N
    def _4fancy():
        inv_x0 = pow(x0, -1, N)
        inv_x1 = pow(inv_x0, sz, N)
        #B = pow(x0, -offset*sz, N)
        #B = pow(inv_x0, +offset*sz, N)
        B = pow(inv_x1, +offset, N)
            # bias
        # [B == x0**(-offset*sz) %N]
        cs0_off = mk_polynomial_coeffs5roots_on_geometric_progression_(opsN, B, x0, inv_x0, sz)
            #优化:几何级数:II[(x-x0**(i*K+j)) | i,j...] == x0**??? * II[(x/x0**(i*Kj) -x0**j0) | i,j...]
            # O(sz*ln(sz))
        # [cs0_off == poly{roots:=[x0**(j-offset*sz) %N | [j:<-[0..<sz]]]}.coeffs]
        assert -1+len(cs0_off) == sz

        #x1 = pow(x0, sz, N)
        x1 = pow(inv_x1, -1, N)
        T, invT = x1, inv_x1
        # [T == x0**sz %N]
        # !! [gcd(N,x0) == 1]
        # [gcd(N,x1) == 1]

        # [polynomial{cs0_off;X} == II[(X -x0**(j-offset*sz) %N) | [j:<-[0..<sz]]] %N]
        diffs = ev.evals_(coeffs8poly:=cs0_off, T, invT)
            # O(sz*ln(sz))
        assert -1+len(diffs) == sz
        diffs.pop()
        assert len(diffs) == sz
        # [diffs == [II[((x0**t -1) %N) | [t:<-[1+sz*(k-1)..<=sz*k]]] * x0**(-offset*sz**2 +sz*(sz-1)/2) %N | [k:<-[offset..<offset+sz]]]]
        return diffs
    def _4native():
        # diff from _4fancy():by drop: 『x0**???』
        x = x0
        diffs = []
        y = pow(x0, (offset-1)*sz, N)
        for _ in range(sz):
            IIdiffs = 1
            for _ in range(sz):
                y = y*x%N
                IIdiffs = IIdiffs*(y-1)%N
            diffs.append(IIdiffs)
        assert len(diffs) == sz
        # drop: 『x0**???』
        # [diffs == [II[((x0**t -1) %N) | [t:<-[1+sz*(k-1)..<=sz*k]]] %N | [k:<-[offset..<offset+sz]]]]
        return diffs

    diffs = _4fancy() if not fancy_vs_native else _4native()
    assert len(diffs) == sz
    # [diffs == [polynomial{cs0_off;X}(X:=T**i) | [i:<-[0..<sz]]]]

    # [diffs == [II[(T**i -x0**(j-offset*sz) %N) | [j:<-[0..<sz]]] %N | [i:<-[0..<sz]]]]
    # !! [T == x1 == x0**sz]
    # [diffs == [II[((x0**sz)**i -x0**(j-offset*sz) %N) | [j:<-[0..<sz]]] %N | [i:<-[0..<sz]]]]
    # [diffs == [II[((x0**(sz*(offset+i)-j) -1)*x0**(j-offset*sz) %N) | [j:<-[0..<sz]]] %N | [i:<-[0..<sz]]]]
    # [diffs == [II[((x0**(sz*k-j) -1)*x0**(j-offset*sz) %N) | [j:<-[0..<sz]]] %N | [k:<-[offset..<offset+sz]]]]
    # [diffs == [II[((x0**(sz*k-j) -1) %N) | [j:<-[0..<sz]]] * II[(x0**(j-offset*sz) %N) | [j:<-[0..<sz]]] %N | [k:<-[offset..<offset+sz]]]]
    # [diffs == [II[((x0**(sz*k-j) -1) %N) | [j:<-[0..<sz]]] * II[(x0**(j-offset*sz) %N) | [j:<-[0..<sz]]] %N | [k:<-[offset..<offset+sz]]]]
    # [diffs == [II[((x0**t -1) %N) | [t:<-[1+sz*(k-1)..<=sz*k]]] * x0**sum[(j-offset*sz) | [j:<-[0..<sz]]] %N | [k:<-[offset..<offset+sz]]]]

    # [diffs == [II[((x0**t -1) %N) | [t:<-[1+sz*(k-1)..<=sz*k]]] * x0**(-offset*sz**2 +sz*(sz-1)/2) %N | [k:<-[offset..<offset+sz]]]]
    #idc4zero = find_indices_(diffs, 0)
    idc4zero = [*iter_find(diffs, 0)]
        #优化:定位所有0点，[x0**e%N==1][phi_(N)%e == 0]
        # O(sz)
    # [@[i:<-idc4zero] -> [diffs[i] == 0]]
    # !! [gcd(N,x0) == 1]
    # [@[i:<-idc4zero] -> [k:=(i+offset)] -> [II[((x0**t -1) %N) | [t:<-[1+sz*(k-1)..<=sz*k]]] %N == 0]]
    ks4zero = [i+offset for i in idc4zero]
    if to_show_soon and ks4zero: show_(('ks4zero', ks4zero))
    # [@[k:<-ks4zero] -> [0 == II[((x0**t -1) %N) | [t:<-[1+sz*(k-1)..<=sz*k]]] %N]]
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
    # [@[k:<-ks4zero] -> [0 == II[((x0**t -1) %N) | [t:<-[1+sz*(k-1)..<=sz*k]]] %N]]
    return (nontrivial_factors, ks4zero)


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
from seed.math.factor_pint.factor_pint__7batch_gcd_IIdiffs import *
