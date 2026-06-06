r'''[[[
e ../../python3_src/seed/algo/rho_method__7iter___py_adhoc_call.py
view ../../python3_src/seed/algo/rho_method__7iter.py

[[[[[[[[[
=========


[[
py_adhoc_call   seed.algo.rho_method__7iter   ,300:iter_rho_method4factor_pint7gcd7quadratic_attract_  ='-1+2**67'  =1 =999
1..=9
py_adhoc_call   seed.algo.rho_method__7iter   ,300:iter_rho_method4factor_pint7gcd7quadratic_attract_  ='-1+2**67'  =9 =999
py_adhoc_call   seed.algo.rho_method__7iter   ,3000:iter_rho_method4factor_pint7gcd7quadratic_attract_  ='-1+2**67'  =10 =999
10..=20
py_adhoc_call   seed.algo.rho_method__7iter   ,3000:iter_rho_method4factor_pint7gcd7quadratic_attract_  ='-1+2**67'  =20 =999
全部失败
]]
[[
py_adhoc_call   seed.algo.rho_method__7iter   ,300:iter_rho_method4factor_pint7gcd7quadratic_attract_  ='1019*1021'  =1 =999
    ...
    (True, 1021, (7, 227050, 227050), (15, 964212, 964212))

py_adhoc_call   seed.algo.rho_method__7iter   ,300:iter_rho_method4factor_pint7gcd7quadratic_attract_  ='4079*65519'  =1 =999
1..=10:失败
py_adhoc_call   seed.algo.rho_method__7iter   ,300:iter_rho_method4factor_pint7gcd7quadratic_attract_  ='4079*65519'  =11 =999
    (True, 4079, (7, 194123193, 194123193), (15, 131102643, 131102643))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info  ='4079*65519'  =999 =300 ='range(1,12)'
    (4079, (267252001, 999, 11, 11, 15))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info  ='4079*65519'  =999 =300 ='range(1,21)' +neg_Jacobi_symbol_only
    (65519, (267252001, 999, 1, 19, 27))
]]

[[
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info  ='-1+2**67'  =999 =1000 ='range(1,200)'
    fail!
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info  ='-1+2**67'  =999 =3000 ='range(1,200)'
    fail!
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info  ='-1+2**67'  =999 =3000 ='range(2000,2100)'
    fail!
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info  ='-1+2**67'  =999 =30000 ='range(2000,2050)'
    fail!
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info  ='-1+2**67'  =999 =10000 ='range(4000,4050)'
    fail!
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info  ='-1+2**67'  =999 =5000 ='range(6000,6050)' +neg_Jacobi_symbol_only
    (None, 18)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info  ='-1+2**67'  =999 =5000 ='range(7000,7050)' +neg_Jacobi_symbol_only
    (None, 17)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info +neg_Jacobi_symbol_only  ='-1+2**67'  =999 =1000 ='range(1,200)'
    (None, 89)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info +neg_Jacobi_symbol_only  ='-1+2**67'  =999 =1000 ='range(200,1000)'
    (None, 395)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info +neg_Jacobi_symbol_only  ='-1+2**67'  =999 =1000 ='range(1000,2000)'
    (None, 488)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info +neg_Jacobi_symbol_only  ='-1+2**67'  =999 =1000 ='range(2000,3000)'
    (None, 517)
败于M67

]]
[[
==>>:
@20260604
try_factor_pint7iter_rho_method7gcd7quadratic_attract_()败于M67,M1207部分因子,M71部分因子
    但下面 调整比率 后，已完全分解:M67,M71
<<==:
view ../../python3_src/nn_ns/math_nn/factor_Mersenne_number_into_prime2exp.py.cached.txt
>34
: {3: 1, 43691: 1, 131071: 1}
>38
: {3: 1, 174763: 1, 524287: 1}
>62
: {3: 1, 715827883: 1, 2147483647: 1}


>41
: {13367: 1, 164511353: 1}
>59
: {179951: 1, 3203431780337: 1}
>67
: {193707721: 1, 761838257287: 1}

-1+2**1207 首缺未知

py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info +neg_Jacobi_symbol_only  ='-1+2**41'  =999 =1000 ='range(1,20)'
    (None, 6)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info +neg_Jacobi_symbol_only  ='-1+2**41'  =999 =1000 ='range(20,100)'
    (None, 39)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info +neg_Jacobi_symbol_only  ='-1+2**41'  =999 =1000 ='range(100,200)'
    (13367, (2199023255551, 999, 31, 172, 417))


py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info +neg_Jacobi_symbol_only  ='-1+2**59'  =999 =1000 ='range(1,20)'
    (None, 8)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info +neg_Jacobi_symbol_only  ='-1+2**59'  =999 =1000 ='range(20,60)'
    (179951, (576460752303423487, 999, 2, 21, 417))



py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info +neg_Jacobi_symbol_only  ='-1+2**34'  =999 =100 ='range(1,20)'
    (3, (17179869183, 999, 1, 5, 1))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info +neg_Jacobi_symbol_only  ='(-1+2**34)//3'  =999 =100 ='range(1,20)'
    (131071, (5726623061, 999, 1, 2, 31))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info +neg_Jacobi_symbol_only  ='(-1+2**38)//3'  =999 =100 ='range(1,20)'
    (524287, (91625968981, 999, 1, 2, 49))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info +neg_Jacobi_symbol_only  ='(-1+2**62)//3'  =999 =100 ='range(1,20)'
    (2147483647, (1537228672809129301, 999, 1, 2, 61))




py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info +neg_Jacobi_symbol_only  ='1207'  =999 =100 ='range(1,20)'
    (17, (1207, 999, 1, 3, 3))
1207==17*71
>17
: {131071: 1}
>71
: {228479: 1, 48544121: 1, 212885833: 1}
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info +neg_Jacobi_symbol_only  ='(-1+2**1207)'  =999 =100 ='range(1,20)'
    (131071, (..., 999, 2, 5, 31))

py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info +neg_Jacobi_symbol_only  ='(-1+2**1207)//131071'  =999 =100 ='range(1,20)'
    (None, 6)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info +neg_Jacobi_symbol_only  ='(-1+2**1207)//131071'  =999 =100 ='range(20,200)'
    (228479, (16815049632774420574441519062910463351147319906138141236290669274662547844137478460398394921578487309783670511677572332834409371205106641524051285677146552785256970988029135604010338112584530947807125788661406683077204322194343469256099743208282989546475601187864955247731886223773266220155845449238496142878030222028692345753104211261688863652500777640001537, 999, 10, 41, 55))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info +neg_Jacobi_symbol_only  ='(-1+2**1207)//131071//228479'  =999 =100 ='range(1,200)'
    (None, 107)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info +neg_Jacobi_symbol_only  ='(-1+2**1207)//131071//228479'  =999 =100 ='range(200,1000)'
    (None, 381)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info +neg_Jacobi_symbol_only  ='(-1+2**1207)//131071//228479'  =999 =100 ='range(1000,2000)'
    (None, 504)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info +neg_Jacobi_symbol_only  ='(-1+2**1207)//131071//228479'  =999 =1000 ='range(2000,2100)'
    (None, 53)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info +neg_Jacobi_symbol_only  ='(-1+2**1207)//131071//228479'  =999 =1000 ='range(2100,2200)'
    (None, 49)
is_prime ='(-1+2**1207)//131071//228479'
    False
(-1+2**1207)//131071//228479 * 228479*131071 == (-1+2**1207)
x=(-1+2**1207)//131071//228479
0 < x%131071
0 < x%228479
0 == x%48544121
0 == x%212885833
y=x//48544121//212885833
y*48544121*212885833 == x

0 < y%48544121
0 < y%212885833

y==7121450524338129034228935888406290342440924878292924475154549706165967683018106989365212535726088820424187252154592086367126609115652316059905387197810171357101484623269226530219357641629634637632902818929376633641165995708421341209033069328278856607776384578328080846029713646218471064646270016968312691054210973840071649700163924918271
is_prime ='(-1+2**1207)//131071//228479//48544121//212885833'
    False

py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info +neg_Jacobi_symbol_only  ='(-1+2**1207)//131071//228479//48544121//212885833'  =999 =1000 ='range(1,200)'
    (None, 100)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info +neg_Jacobi_symbol_only  ='(-1+2**1207)//131071//228479//48544121//212885833'  =666 =1000 ='range(77200,77300)'
    (None, 43)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info +neg_Jacobi_symbol_only  ='(-1+2**1207)//131071//228479//48544121//212885833'  =666 ='10**4' ='range(76200,76300)'
    (None, 40)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info +neg_Jacobi_symbol_only  ='(-1+2**1207)//131071//228479//48544121//212885833'  =666 =1000 ='range(765200,765300)'
    (None, 59)
败于M1207部分因子


py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info +neg_Jacobi_symbol_only  ='(-1+2**71)'  =999 =100 ='range(1,200)'
    (228479, (2361183241434822606847, 999, 5, 11, 55))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info +neg_Jacobi_symbol_only  ='(-1+2**71)//228479'  =999 =100 ='range(1,200)'
    (None, 95)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info -neg_Jacobi_symbol_only  ='(-1+2**71)//228479'  =999 =100 ='range(1,200)'
    (None, 199)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info -neg_Jacobi_symbol_only  ='(-1+2**71)//228479'  =999 =100 ='range(200,1000)'
    (None, 800)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info -neg_Jacobi_symbol_only  ='(-1+2**71)//228479'  =999 =100 ='range(1000,5000)'
    (None, 4000)
败于M71部分因子

]]
[[
@20260605
++kw:ratio
再战！

结果:
    已完全分解M71
    已完全分解M67
    再败于M1207部分因子
<<==:

py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info -neg_Jacobi_symbol_only  ='(-1+2**71)//228479'  =999 =100 ='range(1,500)' --ratio=-1
    (None, 499)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info -neg_Jacobi_symbol_only  ='(-1+2**71)//228479'  =999 =100 ='range(1,500)' --ratio=-2
    (None, 499)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info -neg_Jacobi_symbol_only  ='(-1+2**71)//228479'  =999 =100 ='range(1,500)' --ratio=+2
    (None, 499)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info -neg_Jacobi_symbol_only  ='(-1+2**71)//228479'  =999 =100 ='range(1,500)' --ratio=-3
    (None, 499)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info -neg_Jacobi_symbol_only  ='(-1+2**71)//228479'  =999 =100 ='range(1,500)' --ratio=+3
    (None, 499)

1000!
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info -neg_Jacobi_symbol_only  ='(-1+2**71)//228479'  =999 =1000 ='range(1,500)' --ratio=-1
    (48544121, (10334355636337793, 999, 37, 37, 774))
>>> x=48544121
>>> x.bit_length()
26


def try_factor_pint7iter_rho_method7gcd7quadratic_attract__ratios_(ratios, M, u0, max_num_steps_per_D, Ds, /, *, exp=2, more_info=False, neg_Jacobi_symbol_only=False, neg_ratio_too=False):
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract__ratios_ +more_info -neg_Jacobi_symbol_only  +neg_ratio_too ='range(4)' ='(-1+2**71)//228479'  =999 =1000 ='range(1,60)'
    (48544121, [[(-1, (10334355636337793, 999, 37, 37, 774))]])
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract__ratios_ +more_info -neg_Jacobi_symbol_only  +neg_ratio_too ='chain([None],range(4))' ='(-1+2**71)//228479'  =999 =1000 ='range(1,60)'
    (48544121, [[(None, (10334355636337793, 999, 52, 52, 981))]])
已完全分解M71




py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract_ +more_info -neg_Jacobi_symbol_only  ='(-1+2**67)'  =999 =100 ='range(1,500)' --ratio=-1
    (None, 499)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract__ratios_ +more_info -neg_Jacobi_symbol_only  +neg_ratio_too ='range(4)' ='(-1+2**67)'  =999 =100 ='range(1,500)'
    (None, [[(-1, 499)], [(2, 499)], [(-2, 499)], [(3, 499)], [(-3, 499)]])
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract__ratios_ +more_info -neg_Jacobi_symbol_only  +neg_ratio_too ='range(4)' ='(-1+2**67)'  =999 =1000 ='range(1,500)'
    (193707721, [[(-1, (147573952589676412927, 999, 18, 18, 119))]])
>>> x=193707721
>>> x.bit_length()
28

已完全分解M67




py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract__ratios_ +more_info -neg_Jacobi_symbol_only  +neg_ratio_too ='chain([None], range(4))' ='(-1+2**1207)'  =999 =100 ='range(1,500)'
    (131071, [[(None, (..., 999, 1, 1, 31))]])
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract__ratios_ +more_info -neg_Jacobi_symbol_only  +neg_ratio_too ='chain([None], range(4))' ='(-1+2**1207)//131071'  =999 =100 ='range(1,500)'
    (228479, [[(None, (16815049632774420574441519062910463351147319906138141236290669274662547844137478460398394921578487309783670511677572332834409371205106641524051285677146552785256970988029135604010338112584530947807125788661406683077204322194343469256099743208282989546475601187864955247731886223773266220155845449238496142878030222028692345753104211261688863652500777640001537, 999, 11, 11, 55))]])
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract__ratios_ +more_info -neg_Jacobi_symbol_only  +neg_ratio_too ='chain([None], range(4))' ='(-1+2**1207)//131071//228479'  =999 =100 ='range(1,500)'
    (None, [[(None, 499)], [(-1, 499)], [(2, 499)], [(-2, 499)], [(3, 499)], [(-3, 499)]])

1000:
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract__ratios_ +more_info -neg_Jacobi_symbol_only  +neg_ratio_too ='chain([None], range(4))' ='(-1+2**1207)//131071//228479'  =999 =1000 ='range(1,500)'
    (48544121, [[(None, (73595602365094475091546790133493508598809168046683245446148964564194292885286956177147111645177400591667814160940709355496169762670121286963140094613275411680097387453679049733281124797397270417881406118993022041750901930568426285374584724234100243551817021204858894024097996856486881595927176892574355380048189207886468103209066090370182220915273515903, 999, 52, 52, 981))]])
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract__ratios_ +more_info -neg_Jacobi_symbol_only  +neg_ratio_too ='chain([None], range(4))' ='(-1+2**1207)//131071//228479//48544121'  =999 =1000 ='range(1,200)'
    (212885833, [[(None, 199)], [(-1, 199)], [(2, 199)], [(-2, 199)], [(3, (1516055927042009373113312529306968161990391546005812844899364117937047266450389660514135411890090678367990516522911381081473691998051036642792236254793354105229290019561360473151447624263240247318133664815828512823435446087661702338262232088497394845234029908685727238198380332326686512583618042905223381839547351323684861926103597392775578754743, 999, 150, 150, 969))]])
>>> x=212885833
>>> x.bit_length()
28

py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract__ratios_ +more_info -neg_Jacobi_symbol_only  +neg_ratio_too ='chain([], range(3,4))' ='(-1+2**1207)//131071//228479//48544121//212885833'  =999 =1000 ='range(1,200)'
    (None, [[(None, 199)], [(3, 199)], [(-3, 199)]])

10000:
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract__ratios_ +more_info -neg_Jacobi_symbol_only  +neg_ratio_too ='chain([None], range(3))' ='(-1+2**1207)//131071//228479//48544121//212885833'  =999 =10000 ='range(1,30)'
    (None, [[(None, 29)], [(-1, 29)], [(2, 29)], [(-2, 29)]])
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract__ratios_ +more_info -neg_Jacobi_symbol_only  +neg_ratio_too ='chain([], range(3,7))' ='(-1+2**1207)//131071//228479//48544121//212885833'  =999 =10000 ='range(1,10)'
    (None, [[(3, 9)], [(-3, 9)], [(4, 9)], [(-4, 9)], [(5, 9)], [(-5, 9)], [(6, 9)], [(-6, 9)]])

100000:
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd7quadratic_attract__ratios_ +more_info +neg_Jacobi_symbol_only  +neg_ratio_too ='chain([None], range(3))' ='(-1+2**1207)//131071//228479//48544121//212885833'  =999 =100000 ='range(1,13)'
    (None, [[(None, 5)], [(-1, 5)], [(2, 5)], [(-2, 5)]])
再败于M1207部分因子

py_adhoc_call  { +to_show_total_timedelta }  seed.math.factor_pint.perfect_power.detect_perfect_power   @factor_pint_as_perfect_power_ ='(-1+2**1207)//131071//228479//48544121//212885833'
    (..., 1)
    total::duration: 0.22078354499999997 *(unit: 0:00:01)

py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__near_sqrtN   @try_factor_pint__near_sqrtNmulCmulZpow_ +with_position6ok   ='(-1+2**1207)//131071//228479//48544121//212885833'  =21 # --ground_scale=3933
    ^C
    KeyboardInterrupt
    try_factor_pint__near_sqrtNmulCmulZpow_(...):[last_c =0][log2(N) ~= 1120][ground_scale == 1]
    total::duration: 322.358306317 *(unit: 0:00:01)


]]
[[
@20260605
++kw:exp
]]
[[
@20260606
++mk_u2next_u__5name_
    ++.pow_u_u_
++try_factor_pint7iter_rho_method7gcd_
def try_factor_pint7iter_rho_method7gcd_(u2next_u_, M, max_num_steps_per_u0, u0s, /, *, more_info=False, extra_args=()):

py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :pow_u_u_  ='-1+2**34'  =999 ='range(9)'
    (3, (17179869183, 3, 2, 2))

py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :pow_u_u_  ='(-1+2**34)//3'  =999 ='range(9)'
    (None, 9)

py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :pow_u_u_  ='(-1+2**34)//3'  =9 ='range(999)'
    (43691, (5726623061, 28, 27, 6))

py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :pow_u_u_  ='(-1+2**67)'  =9 ='range(999)'
    (193707721, (147573952589676412927, 711, 710, 4))

py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :pow_u_u_  ='(-1+2**71)'  =9 ='range(999)'
    (228479, (2361183241434822606847, 150, 149, 8))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :pow_u_u_  ='(-1+2**71)//228479'  =9 ='range(999)'
    (None, 999)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :pow_u_u_  ='(-1+2**71)//228479'  =9 ='range(9999)'
    (212885833, (10334355636337793, 4420, 4419, 9))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :pow_u_u_  ='(-1+2**71)//228479'  =99 ='range(9999)'
    (48544121, (10334355636337793, 13, 12, 64))

py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :pow_u_u_  ='(-1+2**1207)'  =9 ='range(999)'
    (131071, (..., 3, 2, 7))
        分解出(-1+2**17)是素数
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :pow_u_u_  ='(-1+2**1207)//131071'  =9 ='range(999)'
    (2361183241434822606847, (..., 17, 16, 5))
        分解出(-1+2**71)非素数
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :pow_u_u_  ='(-1+2**1207)//131071//2361183241434822606847'  =9 ='range(999)'
    ^KeyboardInterrupt
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :pow_u_u_  ='(-1+2**1207)//131071//2361183241434822606847'  =99 ='range(9)'
    (None, 9)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :pow_u_u_  ='(-1+2**1207)//131071//2361183241434822606847'  =99 ='range(9,99)'
    (None, 90)
    10000次，好久...
py_adhoc_call  { +to_show_total_timedelta } seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :pow_u_u_  ='(-1+2**1207)//131071//2361183241434822606847'  =999 ='[666, 999]'
    (None, 2)
    total::duration: 16.57306881 *(unit: 0:00:01)
    2000次
    125次/秒

py_adhoc_call  { +to_show_total_timedelta } seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :pow_u_u_  ='(-1+2**1207)//131071//2361183241434822606847'  =1050 ='[666777888999, 579852, 67899]'
    (None, 3)
    total::duration: 26.052310298 *(unit: 0:00:01)

py_adhoc_call  { +to_show_total_timedelta } seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :pow_u_u_  ='(-1+2**1207)//131071//2361183241434822606847'  =1050 ='range(1,50)'
    (None, 49)
    total::duration: 423.683837063 *(unit: 0:00:01)









===
#def iter_rho_method4factor_pint7gcd_(M, u0, u2next_u_, /, *, extra_args=()):
py_adhoc_call   seed.algo.rho_method__7iter   ,iter_rho_method4factor_pint7gcd_ ='(-1+2**34)//3' =999 :pow_u_u_
    ...
    (True, 5726623061, (15, 1, 1), (16, 1, 1))
    #fail:[gcd==M]
py_adhoc_call   seed.algo.rho_method__7iter   ,iter_rho_method4factor_pint7gcd_ ='(-1+2**34)//3' =24 :pow_u_u_
    ...
    (True, 5726623061, (31, 5387970854, 5387970854), (55, 5387970854, 5387970854))
    #fail:[gcd==M]
py_adhoc_call   seed.algo.rho_method__7iter   ,iter_rho_method4factor_pint7gcd_ ='(-1+2**34)//3' =2 :pow_u_u_
    ...
    (True, 5726623061, (3, 256, 256), (4, 256, 256))
    #fail:[gcd==M]
py_adhoc_call   seed.algo.rho_method__7iter   ,iter_rho_method4factor_pint7gcd_ ='(-1+2**34)//3' =3 :pow_u_u_
    (True, 5726623061, (31, 1394477694, 1394477694), (55, 1394477694, 1394477694))
    #fail:[gcd==M]
py_adhoc_call   seed.algo.rho_method__7iter   ,iter_rho_method4factor_pint7gcd_ ='(-1+2**34)//3' =4 :pow_u_u_
    (True, 5726623061, (1, 256, 256), (2, 256, 256))
    #fail:[gcd==M]
py_adhoc_call   seed.algo.rho_method__7iter   ,iter_rho_method4factor_pint7gcd_ ='(-1+2**34)//3' =5 :pow_u_u_
    (True, 5726623061, (15, 2171643601, 2171643601), (23, 2171643601, 2171643601))
py_adhoc_call   seed.algo.rho_method__7iter   ,iter_rho_method4factor_pint7gcd_ ='(-1+2**34)//3' =6 :pow_u_u_
    (True, 5726623061, (63, 2814162323, 2814162323), (87, 2814162323, 2814162323))
py_adhoc_call   seed.algo.rho_method__7iter   ,iter_rho_method4factor_pint7gcd_ ='(-1+2**34)//3' =7 :pow_u_u_
    (True, 5726623061, (31, 1, 1), (32, 1, 1))
py_adhoc_call   seed.algo.rho_method__7iter   ,iter_rho_method4factor_pint7gcd_ ='(-1+2**34)//3' =8 :pow_u_u_
    (True, 5726623061, (1, 16777216, 16777216), (2, 16777216, 16777216))
py_adhoc_call   seed.algo.rho_method__7iter   ,iter_rho_method4factor_pint7gcd_ ='(-1+2**34)//3' =9 :pow_u_u_
    (True, 5726623061, (31, 1651830758, 1651830758), (55, 1651830758, 1651830758))
py_adhoc_call   seed.algo.rho_method__7iter   ,iter_rho_method4factor_pint7gcd_ ='(-1+2**34)//3' =27 :pow_u_u_
    (True, 43691, (3, 1242896403, 1242896403), (6, 2055505312, 2055505312))





===
py_adhoc_call  { +lineno }  seed.algo.rho_method__7iter   ,iter_rho_method4factor_pint7gcd_ ='(-1+2**1207)//131071//2361183241434822606847' =7777 :pow_u_u_ | more
    3646:(False, 1, (2047, 1237762608873391170283358747717139495284446254962292850413455511049915225053982648965
    839095178654670661306720510218031707850048792202586778920659756764999577781968679267971681955992232259805543
    694329074989231771733407907058532412012199853137448054734576424801108961187420251911710118694017427240334840
    719511071289980192484401821580907257, 1237762608873391170283358747717139495284446254962292850413455511049915
    225053982648965839095178654670661306720510218031707850
    048792202586778920659756764999577781968679267971681955
    992232259805543694329074989231771733407907058532412012199853137448054734576424801108961187420251911710118694017427240334840719511071289980192484401821580907257), (3646, 69454102406461834031689553186741509629868453321
    336188606748411646636523872764341386234543883561023370277351872004707787187819350744751037024048415886909485901360829646762953527317484393373329391114541814047316793167681283512912452344296568759016273943140222173090
    144947369415080471881329246098259091234906275058904378
    7374686814964624395, 694541024064618340316895531867415
    096298684533213361886067484116466365238727643413862345
    438835610233702773518720047077871878193507447510370240484158869094859013608296467629535273174843933733293911145418140473167931676812835129124523442965687590162739
    431402221730901449473694150804718813292460982590912349
    062750589043787374686814964624395))
    q #quit

]]
[[
pow_u_rru_
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :pow_u_rru_  ='(-1+2**34)'  =999 ='range(9)'
    (3, (17179869183, 4, 3, 1))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :pow_u_rru_  ='(-1+2**34)//3'  =999 ='range(9)'
    (None, 9)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :pow_u_rru_  ='(-1+2**34)//3'  =9 ='range(999)'
    (131071, (5726623061, 49, 48, 8))


py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :pow_u_rru_  ='(-1+2**67)'  =9 ='range(999)'
    (193707721, (147573952589676412927, 406, 405, 9))


py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :pow_u_rru_  ='(-1+2**71)'  =9 ='range(999)'
    (228479, (2361183241434822606847, 380, 379, 4))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :pow_u_rru_  ='(-1+2**71)//228479'  =9 ='range(999)'
    (None, 999)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :pow_u_rru_  ='(-1+2**71)//228479'  =99 ='range(99)'
    (48544121, (10334355636337793, 32, 31, 64))


py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :pow_u_rru_  ='(-1+2**1207)'  =9 ='range(99)'
    (131071, (..., 91, 90, 2))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :pow_u_rru_  ='(-1+2**1207)//131071'  =9 ='range(99)'
    (None, 99)
py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :pow_u_rru_  ='(-1+2**1207)//131071'  =99 ='range(99)'
    (228479, (..., 57, 56, 56))
    total::duration: 28.479676537 *(unit: 0:00:01)
py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :pow_u_rru_  ='(-1+2**1207)//131071//228479'  =99 ='range(99)'
    (None, 99)
    total::duration: 68.986338382 *(unit: 0:00:01)
py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :pow_u_rru_  ='(-1+2**1207)//131071//228479'  =20 ='range(99,999)'
    (None, 900)
    total::duration: 158.247528669 *(unit: 0:00:01)
py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :pow_u_rru_  ='(-1+2**1207)//131071//228479'  =999 ='range(20)'
    (212885833, (..., 16, 15, 256))
    total::duration: 31.830279334000004 *(unit: 0:00:01)
py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :pow_u_rru_  ='(-1+2**1207)//131071//228479//212885833'  =9 ='range(999)'
    (48544121, (345704555948983580751222605468037455544583692643761999165763954636635181286520630882690590525004078555419017295250028946248244535229929024742290364682347893389868678831620748259378653897543621035042788023348749758049432676755086306633587610473357536909546353912892334287448788837380651797187353902381824440371235073620272811714371291067462534791, 33, 32, 4))
    total::duration: 0.9205307730000001 *(unit: 0:00:01)
py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :pow_u_rru_  ='(-1+2**1207)//131071//228479//212885833//48544121'  =9 ='range(999)'
    (None, 999)
    total::duration: 55.781627965 *(unit: 0:00:01)
py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :pow_u_rru_  ='(-1+2**1207)//131071//228479//212885833//48544121'  =99 ='range(99)'
    (None, 99)
    total::duration: 50.432513651 *(unit: 0:00:01)
py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :pow_u_rru_  ='(-1+2**1207)//131071//228479//212885833//48544121'  =20 ='range(99,999)'
    (None, 900)
    total::duration: 127.79933114699999 *(unit: 0:00:01)
py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :pow_u_rru_  ='(-1+2**1207)//131071//228479//212885833//48544121'  =999 ='range(20)'
    (None, 20)
    total::duration: 49.32840859 *(unit: 0:00:01)
py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :pow_u_rru_  ='(-1+2**1207)//131071//228479//212885833//48544121'  =999 ='range(20,50)'
    (None, 30)
    total::duration: 164.267597916 *(unit: 0:00:01)



++kw:gcd_with_more
py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ --gcd_with_more=2  +more_info  :pow_u_rru_  ='(-1+2**1207)//131071//228479//212885833//48544121'  =9999 ='range(50,61)'
    (None, 11)
    total::duration: 663.55538255 *(unit: 0:00:01)
py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ --gcd_with_more=2  +more_info  :pow_u_rru_  ='(-1+2**1207)//131071//228479//212885833//48544121'  =9999 ='range(61,62)'
    (None, 1)
    total::duration: 85.750497514 *(unit: 0:00:01)

py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ --gcd_with_more=2  +more_info  :pow_u_rru_  ='(-1+2**1207)//131071//228479//212885833//48544121'  =999 ='range(66661,66672)'
    (None, 11)
    total::duration: 90.661727451 *(unit: 0:00:01)

]]
[[
random_walk_1_
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :random_walk_1_  ='(-1+2**34)'  =999 ='range(9)'
    (3, (17179869183, 1, 0, 3))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :random_walk_1_  ='(-1+2**34)//3'  =999 ='range(9)'
    (None, 9)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :random_walk_1_  ='(-1+2**34)//3'  =999 ='range(999)'
    (43691, (5726623061, 209, 208, 68))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :random_walk_1_  ='(-1+2**67)'  =999 ='range(999)'
    (None, 999)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :random_walk_1_  ='(-1+2**67)'  =9999 ='range(9999)'
    (None, 9999)

]]
[[
add_1_pow_u_2_
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_1_pow_u_2_  ='(-1+2**34)'  =99 ='range(99)'
    (3, (17179869183, 1, 0, 4))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_1_pow_u_2_  ='(-1+2**34)//3'  =99 ='range(99)'
    (None, 99)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_1_pow_u_2_  ='(-1+2**34)//3'  =999 ='range(20)'
    (131071, (5726623061, 1, 0, 509))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_1_pow_u_2_  ='(-1+2**67)'  =999 ='range(20)'
    (None, 20)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_1_pow_u_2_  ='(-1+2**67)'  =999 ='range(20,100)'
    (None, 80)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_1_pow_u_2_  ='(-1+2**67)'  =9999 ='range(20)'
    (None, 20)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_1_pow_u_2_  ='(-1+2**67)'  =9999 ='range(20,100)'
    (None, 80)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_1_pow_u_2_  ='(-1+2**67)'  =999 ='range(100,1000)'
    (None, 900)
    ???感觉不太行，实则 步数上限 设置不对，真得非常大:O(p**/2)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_1_pow_u_2_  ='(-1+2**67)'  =99999 ='range(2,4)'
    (193707721, (147573952589676412927, 1, 2, 13719))

>>> 13719**2/193707721
0.9716234336369071

]]
[[
add_B_pow_u_2_
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**34)//3'  =999 ='range(20)'  --extra_args='(1,)'
    (131071, (5726623061, 1, 0, 509))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**34)//3'  =999 ='range(20)'  --extra_args='(666,)'
    (43691, (5726623061, 1, 0, 623))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =999 ='range(20)'  --extra_args='(666,)'
    (None, 20)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =999 ='range(20)'  --extra_args='(67,)'
    (None, 20)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =999 ='range(20)'  --extra_args='(678,)'
    (None, 20)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =9999 ='range(2,4)'  --extra_args='(6789,)'
    (None, 2)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =9999 ='range(2,4)'  --extra_args='(67890,)'
    (193707721, (147573952589676412927, 2, 3, 8188))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =9999 ='range(2,4)'  --extra_args='(678901,)'
    (193707721, (147573952589676412927, 1, 2, 7088))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =9999 ='range(2,4)'  --extra_args='(6789012,)'
    (None, 2)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =9999 ='range(2,4)'  --extra_args='(67890123,)'
    (None, 2)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =9999 ='range(2,4)'  --extra_args='(123,)'
    (None, 2)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =9999 ='range(2,4)'  --extra_args='(1234,)'
    (None, 2)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =9999 ='range(2,4)'  --extra_args='(12345,)'
    (None, 2)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =9999 ='range(2,4)'  --extra_args='(123456,)'
    (None, 2)

193707721
>>> from math import isqrt
>>> isqrt(193707721)
13917
>>> 9999**2 < 193707721 < 99999**2
True
>>> 65465**2/193707721
22.124395470018463
>>> 26055**2/193707721
3.504573909059619
>>> 13719**2/193707721  # 『1+x**2』表现最佳！
0.9716234336369071


(+1+x**2)@[x==2]:13719
(-4+x**2)@[x==2]:8739
(-3+x**2)@[x==3]:6439
<<==:
99999:
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =99999 ='range(2,4)'  --extra_args='(1234567,)'
    (193707721, (147573952589676412927, 1, 2, 65465))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =99999 ='range(2,4)'  --extra_args='(123456,)'
    (193707721, (147573952589676412927, 1, 2, 26055))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =99999 ='range(2,4)'  --extra_args='(12345,)'
    (193707721, (147573952589676412927, 1, 2, 27555))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =99999 ='range(2,4)'  --extra_args='(1234,)'
    (193707721, (147573952589676412927, 1, 2, 18245))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =99999 ='range(2,4)'  --extra_args='(123,)'
    (193707721, (147573952589676412927, 1, 2, 37081))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =99999 ='range(2,4)'  --extra_args='(12,)'
    (193707721, (147573952589676412927, 1, 2, 30605))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =99999 ='range(2,4)'  --extra_args='(1,)'
    (193707721, (147573952589676412927, 1, 2, 13719))
    『1+x**2』表现最佳！

py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =99999 ='range(2,4)'  --extra_args='(-1,)'
    (193707721, (147573952589676412927, 1, 2, 51637))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =99999 ='range(2,4)'  --extra_args='(-2,)'
    (193707721, (147573952589676412927, 2, 3, 62203))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =99999 ='range(2,4)'  --extra_args='(+2,)'
    (193707721, (147573952589676412927, 1, 2, 25386))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =99999 ='range(2,4)'  --extra_args='(+3,)'
    (193707721, (147573952589676412927, 1, 2, 20520))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =99999 ='range(2,4)'  --extra_args='(-3,)'
    (193707721, (147573952589676412927, 2, 3, 6439))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =99999 ='range(2,4)'  --extra_args='(-4,)'
    (193707721, (147573952589676412927, 1, 2, 8739))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =99999 ='range(2,4)'  --extra_args='(+4,)'
    (193707721, (147573952589676412927, 1, 2, 16058))




尝试类似:(-3+x**2)@[x==3]:6439
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =99999 ='[5]'  --extra_args='(+5,)'
    (193707721, (147573952589676412927, 1, 5, 18345))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =99999 ='[5]'  --extra_args='(-5,)'
    (193707721, (147573952589676412927, 1, 5, 54387))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =99999 ='[7]'  --extra_args='(-7,)'
    (193707721, (147573952589676412927, 1, 7, 33312))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =99999 ='[7]'  --extra_args='(+7,)'
    (193707721, (147573952589676412927, 1, 7, 32705))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =99999 ='[11]'  --extra_args='(+11,)'
    (193707721, (147573952589676412927, 1, 11, 20851))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =99999 ='[11]'  --extra_args='(-11,)'
    (193707721, (147573952589676412927, 1, 11, 12572))





尝试类似:(-4+x**2)@[x==2]:8739
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =99999 ='[3]'  --extra_args='(-3**3,)'
    (193707721, (147573952589676412927, 1, 3, 29694))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =99999 ='[3]'  --extra_args='(-3**2,)'
    (193707721, (147573952589676412927, 1, 3, 15396))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =99999 ='[3]'  --extra_args='(-3*2,)'
    (None, 1)
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =99999 ='[5]'  --extra_args='(-5**5,)'
    (193707721, (147573952589676412927, 1, 5, 34766))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =99999 ='[5]'  --extra_args='(-5**2,)'
    (193707721, (147573952589676412927, 1, 5, 64706))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =99999 ='[5]'  --extra_args='(-5*2,)'
    (193707721, (147573952589676412927, 1, 5, 16223))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =99999 ='[7]'  --extra_args='(-7**7,)'
    (193707721, (147573952589676412927, 1, 7, 52767))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =99999 ='[7]'  --extra_args='(-7**2,)'
    (193707721, (147573952589676412927, 1, 7, 22994))
py_adhoc_call   seed.algo.rho_method__7iter   @try_factor_pint7iter_rho_method7gcd_ +more_info  :add_B_pow_u_2_  ='(-1+2**67)'  =99999 ='[7]'  --extra_args='(-7*2,)'
    (193707721, (147573952589676412927, 1, 7, 30328))



]]




=========
]]]]]]]]]

#]]]'''#'''
