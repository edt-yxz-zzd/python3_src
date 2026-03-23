#__all__:goto
r'''[[[
e ../../python3_src/seed/math/power/addition_chain/shortest/may_optimal_addition_chain5target_uint7generally_solved_small_step_cases.py
[[num_small_steps <= 3]or[num_small_steps == 4][阳爻数纟靶值==5]]

seed.math.power.addition_chain.shortest.may_optimal_addition_chain5target_uint7generally_solved_small_step_cases
py -m nn_ns.app.debug_cmd   seed.math.power.addition_chain.shortest.may_optimal_addition_chain5target_uint7generally_solved_small_step_cases -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.power.addition_chain.shortest.may_optimal_addition_chain5target_uint7generally_solved_small_step_cases:__doc__ -ht # -ff -df
#######
view ../../python3_src/seed/math/power/addition_chain/shortest/may_optimal_addition_chain5target_uint7generally_solved_small_step_cases.py.bit_ptn_dat.txt
view ../../python3_src/seed/math/power/addition_chain/shortest/may_optimal_addition_chain5target_uint7generally_solved_small_step_cases.py.chain_ptn_dat.txt
view ../../python3_src/seed/math/power/addition_chain/shortest/may_optimal_addition_chain5target_uint7generally_solved_small_step_cases__7data.py
view ../../python3_src/seed/math/power/addition_chain/shortest/may_optimal_addition_chain5target_uint7generally_solved_small_step_cases__7data7prepare.py
view ../../python3_src/seed/math/power/addition_chain/shortest/may_optimal_addition_chain5target_uint7generally_solved_small_step_cases__7data7prepare__py_adhoc_call.py
#######

[[
http://wwwhomes.uni-bielefeld.de/achim/addition_chain.html
Generally Solved Small Step Cases
view others/数学/最短加链/最短加链-小步分类/all_1_step_numbers.txt
view others/数学/最短加链/最短加链-小步分类/all_2_step_numbers.txt
view others/数学/最短加链/最短加链-小步分类/all_3_step_numbers.txt

===
[列表纟已知阳爻模板 :: [(允负序号, 总小步数, 阳爻数纟靶值, 欤最短加链含加星链, 变量数, 列表纟表达式纟阳爻位, 列表纟表达式冃不等式)]]
[列表纟表达式纟阳爻位,列表纟表达式冃不等式 :: [表达式纟非负整数]]
[表达式纟非负整数 :: [单项式纟非负整数]]
[单项式纟非负整数 :: (毝变量号, 系数)]
    [变量值==阳爻位]
    [列表纟表达式纟阳爻位:表达式:严格递降]
===
格式示例:
 25 5* 3  @(p)+@(q)+@(-p+2q-2)+@(r)+@(-p+q+r-1)
 42 6* 2  @(p)+@(p-7)+@(q)+@(q-3)+@(q-4)+@(q-5) ,q>=6
===
e ../../python3_src/seed/math/power/addition_chain/shortest/may_optimal_addition_chain5target_uint7generally_solved_small_step_cases.py.bit_ptn_dat.txt
===
]]
[[
DONE:构造冫最短加链:_趃解读冫加链模板灬扌()
view others/数学/最短加链/最短加链-小步分类/minimal_1_step_chains.txt
view others/数学/最短加链/最短加链-小步分类/minimal_2_step_chains.txt
view others/数学/最短加链/最短加链-小步分类/minimal_3_step_chains.txt

===
格式示例:
#Shortest Addition Chains with 3 Small Steps

  8 5* @(p)+@(p-7)+@(q)+@(q-1)+@(q-3) ,q>=4
    A=p-6,  C=q-4
    0                 1
    1( 0, *:A)        @(A)
    2( 1, 1:A-1)      @(A)+@(A-1)
    3( 2, 1:C)        @(A)+@(A-1)+@(C)
    4( 3, 2  )        @(A+1)+@(A)+@(C)
    5( 4, 3  )        @(A+2)+@(A-1)+@(C+1)
    6( 5, 4  )        @(A+2)+@(A+1)+@(A)+@(A-1)+@(C+1)+@(C)
    7( 6, *:3)        @(A+5)+@(A+4)+@(A+3)+@(A+2)+@(C+4)+@(C+3)
    8( 7, 5  )        @(A+6)+@(A-1)+@(C+4)+@(C+3)+@(C+1)


===
e ../../python3_src/seed/math/power/addition_chain/shortest/may_optimal_addition_chain5target_uint7generally_solved_small_step_cases.py.chain_ptn_dat.txt
===
 19 5* @(p)+@(q)+@(q-2)+@(q-3)+@(q-4) ,p>=6
    A=p-4, G=-p+q+1   ==>  G=0  ==>  q=p-1
    #<==> 19 5* @(p)+@(p-1)+@(p-3)+@(p-4)+@(p-5) ,p>=6
===
见下面:独占失败列表纟允负序号:[19,21,22,90,91,93,95]
===
Update:
In March 2020 Neill Clift proved that 7 algebraic expressions of the above list are fully covered by the remaining ones. These redundant ones are:
 19 covered by 20 and 26,
 21 covered by 24 and 28 and 30,
 22 covered by 28 and 30,
 90 covered by 69 and 76,
 91 covered by 105 and 106,
 93 covered by 56 and 69,
 95 covered by 86 and 99 and 110,
Moreover he showed that non of the remaining 189 algebraic expressions can be covered by others totally.

2nd Update:
In May 2020, during Achim checked for every listed addition chain whether its number of independent variables equals the dimension of its feasable set, he discovered for the chain 19 the missing condition -p+q+1>=0 implied from the strict monotony of the exponents which forces q=p-1.
Furthermore the chains with no 19[G=0],21[E=0,1],22[E=0,1],89[C=3,4],90[E=0,1,2],91[D-E=1,2],93[E=1,2],95[F=0,1,2] and 186[E=2,3] has a one dimension smaller feasible set than their number of independent variables. In the preceeding sentence is indicated for each case in brackets which variable has which finite range.
Moreover in case no 89 only C=4 is needed and in case no 186 only E=4 is needed to cover all numbers together with the remaining listed addition chains. Thus we may eliminate in case 89 q=p-6 and in case 186 q=p-4 and simplify both corresponding addition chains.

Thus the list of needed 3-small-step addition chains can be shorten to
  1 chain  with 4 bits set
 31 chains with 5 bits set
 82 chains with 6 bits set
 43 chains with 7 bits set
 32 chains with 8 bits set
A total of 189 chains.
===
    [[
    证明:第40模板几乎被涵盖
      搜索定位:『@40:卡壳:』
        => 并集:{40,42}
        view ../../python3_src/seed/math/power/addition_chain/shortest/may_optimal_addition_chain5target_uint7generally_solved_small_step_cases__7data7prepare__py_adhoc_call.py
      view others/数学/最短加链/最短加链-小步分类/minimal_3_step_chains.txt
     40 6* @(p)+@(p-7)+@(p-8)+@(p-11)+@(p-12)+@(p-13)
        [p>=13]
            !! [8295 == 0b10000001100111 == 2**13+2**6+2**5+2**2+2**1+2**0]
            [p==13] => 8295
     42 6* @(p)+@(p-7)+@(q)+@(q-3)+@(q-4)+@(q-5) ,q>=6
        [q:=p-8] => No.40 [p>=14]
            [p:=q+8]
            [p>=14]
    ]]
===
]]
#######



'#'; __doc__ = r'#'
>>>






e ../../python3_src/seed/math/power/addition_chain/shortest/may_optimal_addition_chain5target_uint7generally_solved_small_step_cases__7data7prepare__py_adhoc_call.py
[[
py_adhoc_call   seed.math.power.addition_chain.shortest.may_optimal_addition_chain5target_uint7generally_solved_small_step_cases   ,枚举冫允负序号纟已知阳爻模板辻最小靶值牜匹配扌 +欤独占 --集合纟允负序号牜跳过='[19,21,22,90,91,93,95]'
    <==> ++独占失败列表纟允负序号:之后:
py_adhoc_call   seed.math.power.addition_chain.shortest.may_optimal_addition_chain5target_uint7generally_solved_small_step_cases   ,枚举冫允负序号纟已知阳爻模板辻最小靶值牜匹配扌 +欤独占
    列表纟允负序号纟已知阳爻模板辻空位丨最小靶值牜匹配牜独占:goto
    _列表纟允负序号辻空位丨最小靶值牜独占
    (-2, 1)
    (-1, 3)
    (0, 7)
    ... ...
    (39, 1039)
    ... ...
    (90, 'pass')
    (91, 'pass')
    ... ...
    (200, 9141)
    (201, 465)
===
DONE:+欤独占:独占失败列表纟允负序号:[19,21,22,90,91,93,95]
    尝试:看看这些阳爻模板是否必然被其余模板涵盖？
    发现:原来已知这些被涵盖
===
]]
[[
py_adhoc_call   seed.math.power.addition_chain.shortest.may_optimal_addition_chain5target_uint7generally_solved_small_step_cases   ,_趃解读冫阳爻模板灬扌  =...
    (-2, 0, 1, True, 1, (((0, 1),),), ())
    ... ...
    (39, 3, 5, False, 4, (((0, 1),), ((1, 1),), ((2, 1),), ((3, 1),), ((1, -1), (2, 1), (3, 1))), ())
    ... ...

=>第39模板:唯一一个非加星链型模板
]]
[[
第39模板:唯一一个非加星链型模板
第39模板所独占的靶值里，虽然1039有最短加链是加星链，但是16537没有最短加链是加星链

!! [第39模板耂靶值耂阳爻数==5]
=> [12509不匹配第39模板]
>>> x=12509
>>> bin(x)
'0b11000011011101'
>>> x.bit_count()
8
>>> x=16537
>>> bin(x)
'0b100000010011001'
>>> x.bit_count()
5
>>> x=1039
>>> bin(x)
'0b10000001111'
>>> x.bit_count()
5
>>> from seed.math.power.addition_chain.data.get_target_uint2may_optimal_addition_chain7arbitrary_recur_shortest_stem_ import 取冫靶值讠婪溟链牜递归最短牜任意扌, 靶值讠婪溟链牜递归最短牜任意扌
>>> 靶值讠婪溟链牜递归最短牜任意扌(1039)
(1, 2, 4, 8, 16, 32, 64, 128, 256, 260, 261, 522, 783, 1039)
>>> from seed.math.power.addition_chain.shortest.rewrite3 import 严序加链讠最短缩写文本纟递归婪溟链扌, 严序加链巛缩写文本纟递归婪溟链扌#严序加链巛最短缩写文本纟递归婪溟链扌
>>> 严序加链讠最短缩写文本纟递归婪溟链扌(靶值讠婪溟链牜递归最短牜任意扌(1039), fmt_case='dnzw_str')
'[---^6-3-^1-3^6]'

head -n 1039 /sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-1.ver2.out.txt | tail -n 1
    ==>>:s_1039
>>> s_1039 = '[#Id+B-BL-I-W-g-Y-G-.-E-q-R-CC-U-q],[-^1-1^1----4-1-^1--3-1]:[-^1-1^1----4-1--^1-3-1],[-^5-1^5-^1-3^4--2-1]:[-^6-^1--3^5-2-1],[-^1---3-1----4-1-1-1]:[---^1-3-1----4-1-1-1],[-^6-^1--3^6-2-2]:[-^6-^1-^1-3^6-2^1],[-^5-1^5-^1-1^1-4^5-1-1]:[-^6-^2-2^5-1-1],[-^1-1^1----4-1---3-1-2]:[-^1-1^1----4-1----4-2],[-^5-1^5-^1-1^1-4^5--2]:[-^6-^2--3^6-2],[--^6-2-1-3^6--2]:[---^6-3--3^6-2],[-^8-1^2-^1-3^8]:[---^6-3-^1-3^6],[-^1---3-1----4-1--2]:[---^1-3-1----4-1--2],[-^5-1^5-^1-3^4---3]:[-^6-^1---4^6-3],[-^6-^1-^1-1^1-4^6]:[-^6-^1-^2-3^6],[-^1-1^1----4-1-^1---4]:[-^1-1^1----4-1---^1-4]'
>>> 次大数讠首尾加链纟一零三九 = (
... {541: ((1, 2, 3, 5, 10, 20, 40, 43, 83, 166, 249, 498, 541, 1039), (1, 2, 3, 5, 10, 20, 40, 43, 83, 166, 332, 498, 541, 1039))
... , 617: ((1, 2, 4, 8, 16, 32, 33, 65, 130, 195, 211, 422, 617, 1039), (1, 2, 4, 8, 16, 32, 64, 65, 130, 195, 390, 422, 617, 1039))
... , 626: ((1, 2, 3, 6, 12, 13, 25, 50, 100, 200, 213, 413, 626, 1039), (1, 2, 4, 8, 12, 13, 25, 50, 100, 200, 213, 413, 626, 1039))
... , 649: ((1, 2, 4, 8, 16, 32, 64, 65, 130, 195, 390, 454, 649, 1039), (1, 2, 4, 8, 16, 32, 64, 65, 130, 195, 390, 585, 649, 1039))
... , 682: ((1, 2, 4, 8, 16, 32, 33, 65, 130, 195, 325, 357, 682, 1039), (1, 2, 4, 8, 16, 32, 64, 65, 130, 260, 325, 357, 682, 1039))
... , 707: ((1, 2, 3, 5, 10, 20, 40, 43, 83, 166, 332, 375, 707, 1039), (1, 2, 3, 5, 10, 20, 40, 43, 83, 166, 332, 664, 707, 1039))
... , 714: ((1, 2, 4, 8, 16, 32, 33, 65, 130, 195, 325, 357, 714, 1039), (1, 2, 4, 8, 16, 32, 64, 65, 130, 260, 325, 650, 714, 1039))
... , 778: ((1, 2, 4, 8, 16, 32, 64, 128, 130, 131, 261, 389, 778, 1039), (1, 2, 4, 8, 16, 32, 64, 128, 256, 260, 261, 522, 778, 1039))
... , 783: ((1, 2, 4, 8, 16, 32, 64, 128, 256, 257, 261, 522, 783, 1039), (1, 2, 4, 8, 16, 32, 64, 128, 256, 260, 261, 522, 783, 1039))
... , 826: ((1, 2, 3, 6, 12, 13, 25, 50, 100, 200, 213, 413, 826, 1039), (1, 2, 4, 8, 12, 13, 25, 50, 100, 200, 213, 413, 826, 1039))
... , 844: ((1, 2, 4, 8, 16, 32, 33, 65, 130, 195, 211, 422, 844, 1039), (1, 2, 4, 8, 16, 32, 64, 65, 130, 195, 390, 780, 844, 1039))
... , 975: ((1, 2, 4, 8, 16, 32, 64, 65, 130, 195, 390, 585, 975, 1039), (1, 2, 4, 8, 16, 32, 64, 65, 130, 195, 390, 780, 975, 1039))
... , 996: ((1, 2, 3, 5, 10, 20, 40, 43, 83, 166, 249, 498, 996, 1039), (1, 2, 3, 5, 10, 20, 40, 43, 83, 166, 332, 664, 996, 1039))
... })
>>> from seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest import 解读冫文本冃次大数讠首尾加链扌
>>> r = 解读冫文本冃次大数讠首尾加链扌(s_1039, ver=2)
>>> r == (1039, 次大数讠首尾加链纟一零三九)
True
>>> 最大次大数纟一零三九 = max(次大数讠首尾加链纟一零三九)
>>> 加星链牜递归最短牜右侧最大纟一零三九 = 次大数讠首尾加链纟一零三九[最大次大数纟一零三九][-1]
>>> 加星链牜递归最短牜右侧最大纟一零三九
(1, 2, 3, 5, 10, 20, 40, 43, 83, 166, 332, 664, 996, 1039)
>>> 严序加链讠最短缩写文本纟递归婪溟链扌(加星链牜递归最短牜右侧最大纟一零三九, fmt_case='dnzw_str')
'[-^1-1^1----4-1---^1-4]'



(1, 2, 3, 5, 10, 20, 40, 43, 83, 166, 332, 664, 996, 1039)
'[-^1-1^1----4-1---^1-4]'

(1, 2, 4, 8, 16, 32, 64, 128, 256, 260, 261, 522, 783, 1039)
'[---^6-3-^1-3^6]'
'0b10000001111'
>>> for u in (1, 2, 4, 8, 16, 32, 64, 128, 256, 260, 261, 522, 783, 1039):print(f'{u}:{u:b}')
1:1
2:10
4:100
8:1000
16:10000
32:100000
64:1000000
128:10000000
256:100000000
260:100000100
261:100000101
522:1000001010
783:1100001111
1039:10000001111

(39, 3, 5, False, 4, (((0, 1),), ((1, 1),), ((2, 1),), ((3, 1),), ((1, -1), (2, 1), (3, 1))), ())
 39 5  @(p)+@(q)+@(r)+@(s)+@(-q+r+s)
    A=s,  B=-q+r+s,  C=p-q-1,  D=q-s-1
    0                 1
    1( 0, *:A)        @(A)
    2( 1, 1:B)        @(A)+@(B)
    3( 1, *:C+1)      @(A+C+1)
    4( 3, 2  )        @(A+C+1)+@(A)+@(B)
    5( 4, *:D+1)      @(A+C+D+2)+@(A+D+1)+@(B+D+1)
    6( 5, 2  )        @(A+C+D+2)+@(A+D+1)+@(B+D+1)+@(A)+@(B)
py_adhoc_call   seed.math.power.addition_chain.shortest.may_optimal_addition_chain5target_uint7generally_solved_small_step_cases   ,枚举冫独占靶值巛阳爻模板牜匹配扌 +欤最小总小步数 =39 | more
py_adhoc_call   seed.math.power.addition_chain.shortest.may_optimal_addition_chain5target_uint7generally_solved_small_step_cases   ,140:枚举冫独占靶值巛阳爻模板牜匹配扌 +欤最小总小步数 =39
\<\(1039\|1051\|2063\|2075\|2078\|2099\|2102\|2243\|2633\|4111\|4123\|4126\|4141\|4147\|4150\|4156\|4198\|4204\|4483\|4486\|5257\|5266\|8207\|8219\|8222\|8237\|8243\|8246\|8252\|8277\|8291\|8294\|8300\|8312\|8396\|8408\|8579\|8837\|8963\|8966\|8972\|10385\|10505\|10514\|10532\|16399\|16411\|16414\|16429\|16435\|16438\|16444\|16469\|16474\|16483\|16486\|16492\|16504\|16537\|16549\|16554\|16582\|16588\|16600\|16624\|16792\|16816\|16969\|17155\|17158\|17669\|17674\|17923\|17926\|17932\|17944\|20753\|20770\|21001\|21010\|21028\|21064\|32783\|32795\|32798\|32813\|32819\|32822\|32828\|32853\|32858\|32867\|32870\|32876\|32888\|32921\|32933\|32938\|32948\|32963\|32966\|32972\|32984\|33008\|33065\|33074\|33098\|33108\|33164\|33176\|33200\|33248\|33539\|33584\|33632\|33938\|34053\|34307\|34310\|34316\|34913\|35333\|35338\|35348\|35843\|35846\|35852\|35864\|35888\|37137\|41249\|41489\|41506\|41540\|41993\|42002\|42020\|42056\|42128\|65551\)\>
==>>:
    {16537,20753,32921,33065,33074,41489,41506}
        #交集#7个
        => 测试用靶值列表牜小
<<==:
view others/数学/oeis整数序列/摘要.txt
view others/数学/oeis整数序列/A349044.txt
    [序列纟靶值牜最短加星链不是最短加链:前43个]
    12509, 13207, 13705, 15473, 16537, 20753, 22955, 23219, 23447, 24797, 25018, 26027, 26253, 26391, 26414, 26801, 27401, 27410, 30897, 30946, 31001, 32921, 33065, 33074, 41489, 41506, 43755, 43927, 45867, 46355, 46419, 46797, 46871, 46894, 47761, 49373, 49577, 49593, 49594, 49611, 50036, 50829, 51667
view ../../python3_src/seed/math/power/addition_chain/shortest/search_star_chain7recursive_shortest.py
    [:序列纟靶值牜不存在加星链牜递归最短:前74个:le74174]

]]



]]]'''#'''
__all__ = r'''
构造冫鬽最短加链巛靶值纟已知阳爻模板扌
试搜索冫阳爻模板巛靶值扌
    趃搜索冫阳爻模板巛靶值扌
枚举冫靶值巛阳爻模板牜匹配扌
    阳爻模板巛丨允负序号扌
    枚举冫独占靶值巛阳爻模板牜匹配扌
        独占失败列表纟允负序号

试匹配冫阳爻模板乊靶值扌

枚举冫允负序号纟已知阳爻模板辻最小靶值牜匹配扌
    列表纟允负序号纟已知阳爻模板辻空位丨最小靶值牜匹配牜独占
        测试用靶值列表牜小
    测试用靶值列表牜大

构造冫鬽最短加链巛靶值纟已知阳爻模板扌
    加链模板巛允负序号扌
    趃测试冫构造冫鬽最短加链巛靶值纟已知阳爻模板扌
        测试用靶值列表牜小
        测试用靶值列表牜大


枚举冫最小靶值辻允负序号纟已知阳爻模板牜匹配扌
    枚举冫允负序号纟已知阳爻模板辻最小靶值牜匹配扌
'''.split()#'''
    #_版本比较冫趃解读冫阳爻模板灬扌
    #   _趃解读冫阳爻模板灬扌
    #       _ver1解读冫阳爻模板扌
    #       _ver2解读冫阳爻模板扌
    #
    #_趃解读冫加链模板灬扌
    #
    #_列表纟已知阳爻模板
    #_列表纟已知加链模板
    #
    #_列表纟允负序号辻空位丨最小靶值牜独占==列表纟允负序号纟已知阳爻模板辻空位丨最小靶值牜匹配牜独占
    #   独占失败列表纟允负序号
    #
    #测试用靶值列表牜小
    #测试用靶值列表牜大
    #   _大列表纟测试用靶值
    #
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
#.def mk_context4lazy_import_registered_names_(qnm4mdl7inject, qnm4pseudo_mdl7import, name7importZqnm4mdl, name7importZalias7inject={}, may_bifix4lazy_name7import=None, lazy_name7importZoriginal_name7import={}):
from seed.helper.lazy_import__func7context7register import mk_context4lazy_import_registered_names_, name7importZqnm4mdl_7tiny
with mk_context4lazy_import_registered_names_(__name__, 'seed._lazy_', name7importZqnm4mdl_7tiny):
    from seed._lazy_ import print_err, at# fst, echo, ifNone
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from itertools import chain, islice
    from seed.tiny_.check import check_type_is, check_int_ge
    from seed.math.power.addition_chain.common.properties import 显链长纟, 阳爻数纟, 首爻位纟, 小步数纟
    from seed.seq_tools.bisearch import bisearch
    #def bisearch(x, array, /, begin=None, end=None, *, key=None, __lt__=None, result_case=2):
    from seed.tiny_.count_ import count_
    from seed.math.power.addition_chain.common.check import 检查冫严序加链乊靶值扌# 检查冫严序加链扌, 检查冫严序加链内容扌
    from nn_ns.math_nn.numbers.shortest_addition_chain_length__ver3 import 取冫靶值讠最小显链长扌, 靶值讠最小显链长扌


#.    from seed.helper.ifNone import ifNone as _ifNone, ifNonef as _ifNonef


with mk_ctx4lazy_import4funcs_(__name__):
    from seed.math.power.addition_chain.shortest.may_optimal_addition_chain5target_uint7generally_solved_small_step_cases__7data7prepare import \
(_版本比较冫趃解读冫阳爻模板灬扌
,   _趃解读冫阳爻模板灬扌
,       _ver1解读冫阳爻模板扌
,       _ver2解读冫阳爻模板扌
#
,_趃解读冫加链模板灬扌
)
#.#################################
___end_mark_of_excluded_global_names__0___ = ...
__all__
from seed.math.power.addition_chain.shortest.may_optimal_addition_chain5target_uint7generally_solved_small_step_cases__7data import _列表纟已知阳爻模板, _列表纟已知加链模板, _列表纟允负序号辻空位丨最小靶值牜独占, _阳爻模板牜后手乊阳爻数五, 独占失败列表纟允负序号, 阳爻模板巛丨允负序号扌, _大列表纟测试用靶值
#################################
#独占失败列表纟允负序号 = (19,21,22,90,91,93,95)
独占失败列表纟允负序号
#################################
from seed.math.power.addition_chain.shortest.may_optimal_addition_chain5target_uint7generally_solved_small_step_cases__7data import _列表纟已知阳爻模板
_列表纟已知阳爻模板
    #_趃解读冫阳爻模板灬扌(_文本冃阳爻模板数据)
    #'emay str -> Iter 阳爻模板/(允负序号, 总小步数, 阳爻数纟靶值, 欤最短加链含加星链, 变量数, 列表纟表达式纟阳爻位, 列表纟表达式冃不等式)'
_最大总小步数 = max(map(at(1), _列表纟已知阳爻模板))
_最大阳爻数纟靶值 = max(map(at(2), _列表纟已知阳爻模板))
assert _最大总小步数 == 3
assert _最大阳爻数纟靶值 == 8
assert _列表纟已知阳爻模板 == tuple(sorted(_列表纟已知阳爻模板, key=at(2)))
        # !! 要求:阳爻数牜升列
        #   @趃搜索冫阳爻模板巛靶值扌()
assert _列表纟已知阳爻模板 == tuple(sorted(_列表纟已知阳爻模板, key=at(1)))
        # !! 要求:总小步数牜升列
        #   @趃搜索冫阳爻模板巛靶值扌()
#_阳爻模板牜后手乊阳爻数五 = (201, 4, 5, True, 5, (((0, 1),), ((1, 1),), ((2, 1),), ((3, 1),), ((4, 1),)), ())
_阳爻模板牜后手乊阳爻数五

def 试搜索冫阳爻模板巛靶值扌(靶值, /, *, 欤排除冫独占失败列表纟允负序号=True):
    for 阳爻模板 in 趃搜索冫阳爻模板巛靶值扌(靶值, 欤排除冫独占失败列表纟允负序号=欤排除冫独占失败列表纟允负序号):
        return 阳爻模板
    return None
def 趃搜索冫阳爻模板巛靶值扌(靶值, /, *, 欤排除冫独占失败列表纟允负序号:bool):
    check_int_ge(1, 靶值)
    _独占失败列表纟允负序号 = 独占失败列表纟允负序号 if 欤排除冫独占失败列表纟允负序号 else ()
    total = 0
    阳爻数纟靶值 = 阳爻数纟(靶值)
    if not 阳爻数纟靶值 <= _最大阳爻数纟靶值:
        return total
    (i, j) = bisearch(阳爻数纟靶值, _列表纟已知阳爻模板, key=at(2))
        # !! 要求:阳爻数牜升列
    assert i < j, (阳爻数纟靶值, (i, j))
    #if 0b00001:print_err((靶值, i, j, [_列表纟已知阳爻模板[k][0] for k in range(i, j)]))
    for k in range(i, j):
        阳爻模板 = _列表纟已知阳爻模板[k]
        if 阳爻模板[0] in _独占失败列表纟允负序号:
            continue
        if not total == 0:
            # !! 要求:总小步数牜升列
            #   要求:阳爻模板牜第一.总小步数牜第一 是 最小
            if 总小步数牜第一 < 阳爻模板[1]:
                break
            assert 总小步数牜第一 == 阳爻模板[1], (靶值, 总小步数牜第一, 阳爻模板牜第一, 阳爻模板)
        if not None is (变量号讠变量值 := 试匹配冫阳爻模板乊靶值扌(靶值, 阳爻模板, 欤最小总小步数=False)):
            if total == 0:
                总小步数牜第一 = 阳爻模板[1]
                阳爻模板牜第一 = 阳爻模板
            else:
                assert 总小步数牜第一 == 阳爻模板[1], (靶值, 总小步数牜第一, 阳爻模板牜第一, 阳爻模板)
            total += 1
            yield 阳爻模板
            continue
    if total == 0:
        if 阳爻数纟靶值 == 5:
            # !! [阳爻数纟靶值 == 5]
            # => [总小步数纟{靶值} <= 4]
            # !! [_最大总小步数 == 3][total == 0]
            # => [总小步数纟{靶值} > 3]
            # => [总小步数纟{靶值} == 4]
            total += 1
            yield _阳爻模板牜后手乊阳爻数五
    return total
def 试匹配冫阳爻模板乊靶值扌(靶值, 阳爻模板, /, *, 欤最小总小步数:bool):
    '-> 鬽变量号讠变量值/may [uint]'
    欤排除冫独占失败列表纟允负序号 = False
    (允负序号, 总小步数, 阳爻数纟靶值, 欤最短加链含加星链, 变量数, 列表纟表达式纟阳爻位, 列表纟表达式冃不等式) = 阳爻模板
    if not 阳爻数纟靶值 == 阳爻数纟(靶值):
        return None
    s = f'{靶值:b}'
    assert s.count('1') == 阳爻数纟靶值
    assert s[0] == '1'
    t = s[::-1]
    列表纟阳爻位 = [j for j, c in enumerate(t) if c == '1']
    777;列表纟阳爻位.reverse()
    assert len(列表纟阳爻位) == 阳爻数纟靶值, (靶值, 阳爻数纟靶值, 列表纟阳爻位)
    assert len(列表纟表达式纟阳爻位) == 阳爻数纟靶值
    变量号讠变量值 = []
    for ls8expr, 阳爻位 in zip(列表纟表达式纟阳爻位, 列表纟阳爻位):
        match ls8expr:
            case ((变量号, 1),) if 变量号 >= 0:
                if not 变量号 == len(变量号讠变量值): raise Exception(阳爻模板)
                变量号讠变量值.append(变量值:=阳爻位)
                assert 阳爻位 == _eval(变量号讠变量值, ls8expr)
                continue
        if not 阳爻位 == _eval(变量号讠变量值, ls8expr):
            return None
    for ls8expr in 列表纟表达式冃不等式:
        if not 0 <= _eval(变量号讠变量值, ls8expr):
            return None
    if not len(变量号讠变量值) == 变量数: raise Exception(阳爻模板)
    assert 靶值 == _靶值巛变量配置扌(列表纟表达式纟阳爻位, 变量号讠变量值)
    if 欤最小总小步数:
        for 阳爻模板牜第一 in 趃搜索冫阳爻模板巛靶值扌(靶值, 欤排除冫独占失败列表纟允负序号=欤排除冫独占失败列表纟允负序号):
            最小总小步数 = 阳爻模板牜第一[1]
            if not 总小步数 == 最小总小步数:
                if not 总小步数 > 最小总小步数: raise Exception(阳爻模板, 靶值, 阳爻模板牜第一)
                return None
    变量号讠变量值 = tuple(变量号讠变量值)
    return 变量号讠变量值
def _靶值巛变量配置扌(列表纟表达式纟阳爻位, 变量号讠变量值, /):
    列表纟阳爻位 = [_eval(变量号讠变量值, ls8expr) for ls8expr in 列表纟表达式纟阳爻位]
    靶值 = sum(1<<阳爻位 for 阳爻位 in 列表纟阳爻位)
    return 靶值
def _eval(变量号讠变量值, ls8expr, /):
    return sum(系数 if 毝变量号 == -1 else 变量号讠变量值[毝变量号]*系数 for (毝变量号, 系数) in ls8expr)

#def 阳爻模板巛丨允负序号扌(阳爻模板丨允负序号, /):
def 枚举冫独占靶值巛阳爻模板牜匹配扌(阳爻模板丨允负序号, /, *, 欤最小总小步数:bool):
    欤排除冫独占失败列表纟允负序号 = False
    阳爻模板 = 阳爻模板巛丨允负序号扌(阳爻模板丨允负序号)
    允负序号 = 阳爻模板[0]
    if 允负序号 in 独占失败列表纟允负序号:
        return
    交集合纟允负序号 = None
    并集合纟允负序号 = set()
    靶值 = 0
    try:
        for 靶值 in 枚举冫靶值巛阳爻模板牜匹配扌(阳爻模板, 欤最小总小步数=欤最小总小步数):
            列表纟允负序号 = [阳爻模板[0] for 阳爻模板 in 趃搜索冫阳爻模板巛靶值扌(靶值, 欤排除冫独占失败列表纟允负序号=欤排除冫独占失败列表纟允负序号)]
            if not 允负序号 in 列表纟允负序号: raise Exception(阳爻模板, 允负序号, 靶值, 列表纟允负序号)
                #^Exception: ((5, 3, 4, True, 4, (((0, 1),), ((1, 1),), ((2, 1),), ((3, 1),)), ()), 5, 15, [3])
            if 列表纟允负序号 == [允负序号]:
                #独占
                yield 靶值
            集合纟允负序号 = set(列表纟允负序号)
            if 交集合纟允负序号 is None:
                交集合纟允负序号 = 集合纟允负序号
            else:
                交集合纟允负序号 &= 集合纟允负序号
            并集合纟允负序号 |= 集合纟允负序号
            if not 允负序号 in 交集合纟允负序号: raise Exception(阳爻模板, 允负序号, 靶值, 交集合纟允负序号)
    except KeyboardInterrupt:

        print_err((阳爻模板, 允负序号, 靶值, 交集合纟允负序号, 并集合纟允负序号))
            # ^C((19, 3, 5, True, 2, (((0, 1),), ((1, 1),), ((1, 1), (-1, -2)), ((1, 1), (-1, -3)), ((1, 1), (-1, -4))), (((0, 1), (-1, -6)),)), 19, 196159429230833773869868536099094796500303545336195973120, {19}, {12, 15, 16, 17, 19, 20, 26, 27, 28, 30, 33, 34, 35, 36})
        raise
def 枚举冫靶值巛阳爻模板牜匹配扌(阳爻模板丨允负序号, /, *, 欤最小总小步数:bool, 欤独占=False):
    '-> Iter 靶值{阳爻模板}'
    if 欤独占:
        yield from 枚举冫独占靶值巛阳爻模板牜匹配扌(阳爻模板丨允负序号, 欤最小总小步数=欤最小总小步数)
        return
    阳爻模板 = 阳爻模板巛丨允负序号扌(阳爻模板丨允负序号)
    (允负序号, 总小步数, 阳爻数纟靶值, 欤最短加链含加星链, 变量数, 列表纟表达式纟阳爻位, 列表纟表达式冃不等式) = 阳爻模板
    assert len(列表纟表达式纟阳爻位) == 阳爻数纟靶值
    变量号讠变量值 = []
    列表纟阳爻位 = []
    def f(j, /):
        assert j == len(列表纟阳爻位)
        if j == 阳爻数纟靶值:
            if not len(变量号讠变量值) == 变量数: raise Exception(阳爻模板)
            for ls8expr in 列表纟表达式冃不等式:
                if not 0 <= _eval(变量号讠变量值, ls8expr):
                    return
            靶值 = _靶值巛变量配置扌(列表纟表达式纟阳爻位, 变量号讠变量值)
            if None is 试匹配冫阳爻模板乊靶值扌(靶值, 阳爻模板, 欤最小总小步数=False): raise Exception(阳爻模板, 变量号讠变量值, 列表纟阳爻位, 靶值, bin(靶值))
            if 欤最小总小步数:
                if None is 试匹配冫阳爻模板乊靶值扌(靶值, 阳爻模板, 欤最小总小步数=欤最小总小步数):
                    return
            yield 靶值
            return
        ls8expr = 列表纟表达式纟阳爻位[j]
        match ls8expr:
            case ((变量号, 1),) if 变量号 >= 0:
                if not 变量号 == len(变量号讠变量值): raise Exception(阳爻模板)
                for 阳爻位 in count_(0, None if j==0 else 列表纟阳爻位[j-1]):
                    变量号讠变量值.append(变量值:=阳爻位)
                    assert 阳爻位 == _eval(变量号讠变量值, ls8expr)
                    列表纟阳爻位.append(变量值:=阳爻位)
                    yield from f(j+1)
                    列表纟阳爻位.pop()
                    变量号讠变量值.pop()
                return
        阳爻位 = _eval(变量号讠变量值, ls8expr)
        if not 阳爻位 >= 0:
            return
        if not (j == 0 or 阳爻位 < 列表纟阳爻位[j-1]):
            return
        列表纟阳爻位.append(变量值:=阳爻位)
        yield from f(j+1)
        列表纟阳爻位.pop()

    yield from f(0)
    return

def 枚举冫允负序号纟已知阳爻模板辻最小靶值牜匹配扌(*, 欤独占=False, 集合纟允负序号牜跳过=(), 毝前几个每模板=-1, 允负序号牜起始=-2):
    '-> Iter (允负序号{阳爻模板}, 最小靶值{阳爻模板})'
    #@20260323:++kw:毝前几个每模板,允负序号牜起始
    check_int_ge(-1, 毝前几个每模板)
    check_int_ge(-2, 允负序号牜起始)
    欤最小总小步数 = True
    集合纟允负序号牜跳过 = set(集合纟允负序号牜跳过)
    for 阳爻模板 in chain(_列表纟已知阳爻模板, [_阳爻模板牜后手乊阳爻数五]):
        允负序号 = 阳爻模板[0]
        if not 允负序号 >= 允负序号牜起始:
            continue
        if 允负序号 in 集合纟允负序号牜跳过:
            yield (允负序号, 'pass')
            continue
        if 欤独占 and 允负序号 in 独占失败列表纟允负序号:
            yield (允负序号, 'pass')
            continue
        it = 枚举冫靶值巛阳爻模板牜匹配扌(阳爻模板, 欤独占=欤独占, 欤最小总小步数=欤最小总小步数)
        if not -1 == 毝前几个每模板:
            靶值列表 = tuple(islice(it, 0, 毝前几个每模板))
            if not 靶值列表 and 毝前几个每模板:
                raise Exception(阳爻模板)
            yield (允负序号, 靶值列表)
            continue
        for 最小靶值 in it:
            break
        else:
            raise Exception(阳爻模板)
        yield (允负序号, 最小靶值)
def 枚举冫最小靶值辻允负序号纟已知阳爻模板牜匹配扌(前置跳跃点集=(), /, *, 欤排除冫独占失败列表纟允负序号=False):
    '[#废置#]: -> Iter (最小靶值{阳爻模板}, 允负序号{阳爻模板})'
    允负序号讠最小靶值 = {}
    sz = 1+len(_列表纟已知阳爻模板)
    def loop_(靶值, /):
        #if not None is (阳爻模板:=试搜索冫阳爻模板巛靶值扌(靶值)):
        for 阳爻模板 in 趃搜索冫阳爻模板巛靶值扌(靶值, 欤排除冫独占失败列表纟允负序号=欤排除冫独占失败列表纟允负序号):
            允负序号 = 阳爻模板[0]
            if 靶值 == 允负序号讠最小靶值.setdefault(允负序号, 靶值):
                最小靶值 = 靶值
                yield (最小靶值, 允负序号)
                if sz == len(允负序号讠最小靶值):
                    return True
        return False
    靶值 = 0
    for 靶值 in 前置跳跃点集:
        b_stop = yield from loop_(靶值)
        if b_stop:
            return
    b_stop = sz == len(允负序号讠最小靶值)
    while not b_stop:
        靶值 += 1
        b_stop = yield from loop_(靶值)




from seed.math.power.addition_chain.shortest.may_optimal_addition_chain5target_uint7generally_solved_small_step_cases__7data import _列表纟允负序号辻空位丨最小靶值牜独占
_列表纟允负序号辻空位丨最小靶值牜独占
    # tuple(枚举冫允负序号纟已知阳爻模板辻最小靶值牜匹配扌(欤独占=True))
    # :: [(允负序号, ('pass'|最小靶值))]
    # 空位:see:独占失败列表纟允负序号
列表纟允负序号纟已知阳爻模板辻空位丨最小靶值牜匹配牜独占 = _列表纟允负序号辻空位丨最小靶值牜独占

测试用靶值列表牜小 = (12509, 16537, *(x for _, x in _列表纟允负序号辻空位丨最小靶值牜独占 if not type(x) is str))
_大列表纟测试用靶值
测试用靶值列表牜大 = (12509, *(16537,20753,32921,33065,33074,41489,41506), *(y for _, x in _大列表纟测试用靶值 if not type(x) is str for y in x))
##################################
##################################
##################################
__all__
#DONE:构造冫最短加链:_趃解读冫加链模板灬扌()
#   see:_ver2解读冫阳爻模板扌, _prepare_1_2, _gmk_txt_rgnrs_1_2
#

from seed.math.power.addition_chain.shortest.may_optimal_addition_chain5target_uint7generally_solved_small_step_cases__7data import _列表纟已知加链模板
_列表纟已知加链模板
    #_趃解读冫加链模板灬扌(_文本冃加链模板数据)
    #'emay str -> Iter (允负序号, jnvar2old_ls8expr, k2j_ls8ez_pairs)'

def 加链模板巛允负序号扌(允负序号, /):
    check_int_ge(-2, 允负序号)
    加链模板 = (_允负序号, jnvar2old_ls8expr, k2j_ls8ez_pairs) = _列表纟已知加链模板[2+允负序号]
    if not _允负序号 == 允负序号:raise 000
    return 加链模板
def 构造冫鬽最短加链巛靶值纟已知阳爻模板扌(靶值, /):
    '靶值 -> 鬽 最短加链'
    while 1:
        if not None is (阳爻模板:=试搜索冫阳爻模板巛靶值扌(靶值, 欤排除冫独占失败列表纟允负序号=True)):
            if not None is (变量号讠变量值 := 试匹配冫阳爻模板乊靶值扌(靶值, 阳爻模板, 欤最小总小步数=True)):
                break
            else:
                raise 000
        else:
            return None
        raise 000
    允负序号 = 阳爻模板[0]
    (_允负序号, jnvar2old_ls8expr, k2j_ls8ez_pairs) = 加链模板巛允负序号扌(允负序号)
    新变量号讠变量值 = jnvar2value = tuple(_eval(变量号讠变量值, old_ls8expr) for old_ls8expr in jnvar2old_ls8expr)
    k2u = []
    us = []
    for k, j_ls8ez_pairs in enumerate(k2j_ls8ez_pairs):
        assert k == len(k2u)
        match j_ls8ez_pairs:
            case ():
                assert k == 0
                us.append(1)
                k2u.append(1)
            case ((j, ls8max_ez),):
                assert k > 0
                max_ez = _eval(新变量号讠变量值, ls8max_ez)
                uj = k2u[j]
                us.extend(uj<<ez for ez in range(1, 1+max_ez))
                #k2u.append(None)
                k2u.append(us[-1])
            case ((j, ()), (i, ls8ez)):
                assert k > 0
                ez = _eval(新变量号讠变量值, ls8ez)
                uj = k2u[j]
                ui = k2u[i]
                uk = uj + (ui<<ez)
                us.append(uk)
                k2u.append(uk)
            case _:
                raise Exception(靶值, 允负序号, k, j_ls8ez_pairs)
            #case
        #match
    #for ... in
    最短加链 = tuple(us)
    ##################
    检查冫严序加链乊靶值扌(靶值, 最短加链)
    ##################
    try:
        最小显链长 = 靶值讠最小显链长扌(靶值)
    except IndexError:
        pass
    else:
        if not 最小显链长 == 显链长纟(最短加链):raise Exception(靶值, 允负序号, (最小显链长, 显链长纟(最短加链)))
    ##################
    return 最短加链
    ##################
def 趃测试冫构造冫鬽最短加链巛靶值纟已知阳爻模板扌(彧趃靶值, /):
    趃靶值 = iter(测试用靶值列表牜大 if 彧趃靶值 is True else (测试用靶值列表牜小 if 彧趃靶值 is ... else 彧趃靶值))
    for 靶值 in 趃靶值:
        鬽最短加链 = 构造冫鬽最短加链巛靶值纟已知阳爻模板扌(靶值)
        yield (靶值, 鬽最短加链)

##################################
##################################
##################################
__all__
from seed.math.power.addition_chain.shortest.may_optimal_addition_chain5target_uint7generally_solved_small_step_cases import 试搜索冫阳爻模板巛靶值扌, 试匹配冫阳爻模板乊靶值扌, 构造冫鬽最短加链巛靶值纟已知阳爻模板扌
    # -> 鬽 阳爻模板
    # -> 鬽 变量号讠变量值
    # -> 鬽 最短加链
from seed.math.power.addition_chain.shortest.may_optimal_addition_chain5target_uint7generally_solved_small_step_cases import *
