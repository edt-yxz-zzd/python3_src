#__all__:goto
# [:曾经主要作业命令行]:goto
# [:主要简并记录输出文件]:goto
# [:主要简并记录输出文件牜未打包:2份]:goto
# [:主要尾六表另档文件:2份]:goto
# [:主要左侧最大另档文件]:goto
# [:主要任意婪溟链牜递归最短另档文件]:goto
# [:主要数据备份命令]:goto
# [:主要数据备份命令牜最后一跃:2路]:goto
# [:当前主要作业命令行]:goto
# [:额外生成数据]:goto
# [:主要数据备份牜逐个文件打包]:goto
r'''[[[
e ../../python3_src/seed/math/power/addition_chain/shortest/mixed_recursive_greedy_zpow_addition_chain.py
    简并态{递归婪溟链}
doc:e ../../python3_src/seed/math/power/addition_chain/shortest/mixed_recursive_greedy_zpow_addition_chain__doc__py_adhoc_call.py
old:view script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py
view ../../python3_src/seed/recognize/text_recognizer/ITextRecognizer.py

%s/script[.]min_add_ver5__mixed_recursive_greedy_zpow_addition_chain/seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain

seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain
py -m nn_ns.app.debug_cmd   seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain:__doc__ -ht # -ff -df

[[
DONE:移动到seed, 原位重命名附日期
DONE:分离出doc
cp -iv script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py ../../python3_src/seed/math/power/addition_chain/shortest/mixed_recursive_greedy_zpow_addition_chain.py
mv -iv script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain-20260216.py
e ../../python3_src/seed/math/power/addition_chain/shortest/mixed_recursive_greedy_zpow_addition_chain.py
e ../../python3_src/seed/math/power/addition_chain/shortest/mixed_recursive_greedy_zpow_addition_chain__doc__py_adhoc_call.py
]]

===old:
e script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py
    简并态{递归婪溟链}
    # [:约束牜定义冫递归婪溟链]:goto
view ../../python3_src/seed/recognize/text_recognizer/ITextRecognizer.py


script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain
py -m nn_ns.app.debug_cmd   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain -x # -off_defs
py -m nn_ns.app.doctest_cmd script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain:__doc__ -ht # -ff -df
#######

[[
溟隘链-->简并态算法牜加溟链
猜想出处:view ../../python3_src/seed/math/power/addition_chain/shortest/rewrite.py
  view ../../python3_src/bash_script/app/szmm4shortest_addition_chain
view script/min_add_ver4__pseudo_addition_chain.py
  view script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.无缺精深.out.txt
  枚举冫相关信息纟最短短程加链牜简并态算法扌
      [相关信息 :: (自然数, 长度纟最短短程加链, 规模纟次大点集纟所有最短短程加链, 规模纟点集纟所有最短短程加链, 次大点集纟所有最短短程加链, 简并态/点集纟所有最短短程加链, 最短短程加链牜水平反转后词典序最小,最短短程加链牜水平反转后词典序最大)]
        (6, 4, 2, 5, [3, 4], RT({1: 4, 6: 1}), [1, 2, 3, 6], [1, 2, 4, 6])
        (n, sz4chain, num_submaxs, num_nodes, submaxs4n, nodes4n, ls0, ls1) = n2info[n]
        (靶值, 最小显链长, 数目{次大数}, 数目{简并态点集}, 次大数点集, RT(简并态点集), 最短加链牜右侧最小, 最短加链牜右侧最大)
          RT:"NonTouchRanges"
          [RT({1: 4, 6: 1}) == [1..<1+4]++[6..<6+1]]


view ../../python3_src/seed/math/power/addition_chain/shortest/rewrite2.py
    溟隘链、溟母链
        未必:递归最短
        糅合:介点/出度为一
]]
[[
递归婪溟链
    强调:递归最短{在不考虑 溟化值 的前提下 递归最短}{溟化值集 构成 跳线，不是 主线}
    『婪』-贪婪型:类比于:加星链
    『溟』-二幂环

# [:约束牜定义冫递归婪溟链]:here
[靶值 == 次大数 + (内点<<溟次)]
[内点 in 简并集纟次大数]
[最小显链长纟靶值 == 最小显链长纟次大数 +1 +溟次]
[溟化值集 := {内点<<ez | [n:<-[1..=溟次]]}]
]]



'#'; __doc__ = r'#'
>>>



[[
xxx:py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌  --ver=1  --休眠期:auto   :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver1.out.txt
view script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver1.out.txt
[靶值==1270] =>: resting...: 14.999647877999998 seconds
... ....
1270:resting...: 14.999647877999998 seconds
8406: resting...: 108.16011947200002 seconds
12999:resting...: 135.65701834099855 seconds
14836:resting...: 130.62248388499995 seconds
15148:resting...: 158.15175883699976 seconds
15270:resting...: 138.40876877500068
17010:resting...: 309.90105902899995 seconds
18030:resting...: 101.91477030200258 seconds
18146:resting...: 199.71460082900012 seconds
18180:resting...: 357.4434666979978 seconds
18252:resting...: 249.11337842399735 seconds
24042:consumed: 455.2927567769998 seconds
24241:consumed: 331.8897022779993 seconds
24254:consumed: 254.6687823809998 seconds
25270:consumed: 488.849069959997 seconds
25934:consumed: 520.0703521059986 seconds
25942:consumed: 453.9847385569992 seconds
25946:consumed: 501.7201072550015 seconds
27002:consumed: 414.01798976400096 seconds
27306:consumed: 252.93409234700084 seconds
27378:consumed: 522.2650140949991 seconds
34020:consumed: 1090.8120074530016 seconds
36312:consumed: 931.6696436359998 seconds
36319:consumed: 841.9737413150033 seconds
38901:consumed: 1342.9543523759985 seconds
]]
[[
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   @转换冫文件格式纟简并记录纟递归婪溟链扌  --verI=1  --verO=2    :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver1.out.txt   :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.out.txt
du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver1.out.txt
    4.0M @[靶值<=2858]
du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.out.txt
    2.1M @[靶值<=2858]
view script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.out.txt

]]
[[
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌  --ver=2  --休眠期:auto   :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.out.txt
    #见下面:分裂文件
view script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.out.txt
]]
[[
测试:分裂文件:
    文件路径冃靶值讠简并记录-->列表纟文件路径冃靶值讠简并记录
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌  --ver=2  --休眠期:auto   :/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part1.test-out.txt
file_startswith_    /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part1.test-out.txt    script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.out.txt
    =>same
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌  --ver=2  --休眠期:auto  :/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part1.test-out.txt    :/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part2.test-out.txt
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌  --ver=2  --休眠期:auto  :/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part1.test-out.txt    :/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part2.test-out.txt    :/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part3.test-out.txt
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌  --ver=2  --休眠期:auto  :/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part1.test-out.txt    :/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part2.test-out.txt    :/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part3.test-out.txt    :/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part4.test-out.txt

view /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part1.test-out.txt
    [1..=86]
view /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part2.test-out.txt
    [87..=126]
view /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part3.test-out.txt
    [127..=158]
view /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part3.test-out.txt
    [159..=190]

cat script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.out.txt  | head -n 126  | tail -n +87  |  diff  -s  -   /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part2.test-out.txt
    => ... are identical
cat script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.out.txt  | head -n 158  | tail -n +127  |  diff  -s  -   /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part3.test-out.txt
    => ... are identical
cat script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0001.1-6017.out.txt  | head -n 190  | tail -n +159  |  diff  -s  -   /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part4.test-out.txt
    => ... are identical

]]
[[
分裂文件:
mv -iv   script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.out.txt   script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0001.1-6017.out.txt
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌  --ver=2  --休眠期:auto   :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0001.1-6017.out.txt    :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0002.6018-_.out.txt
view script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0002.6018-_.out.txt

]]
[[
DONE:由 自顶向下搜索 改为 自底向上注册
===
自顶向下搜索:
def _求冫丮最小显链长辻次大数讠溟次厈乊后续简并记录纟递归婪溟链牜靶值大于一牜自顶向下搜索扌(靶值讠简并记录, 靶值, /):
    for 次大数 in reversed(range(1, 靶值)):
        溟化值 = 靶值 -次大数
        ... ...
        assert 靶值 == 次大数 + (内点<<溟次)
        assert 内点 in 简并集纟次大数
        ... ...
        显链长纟靶值 = 最小显链长纟次大数 +1 +溟次
    ... ...
    return (最小显链长纟靶值, 次大数讠溟次)
===
自底向上注册:
[靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈 :: {靶值:{显链长纟靶值:[(次大数,内点,溟次)]}}{靶值>=当前靶值}]
def _求冫丮最小显链长辻次大数讠溟次厈乊后续简并记录纟递归婪溟链牜靶值大于一牜自底向上注册扌(靶值讠简并记录, 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈, /):
    靶值 = len(靶值讠简并记录)
    assert 靶值 >= 2
    最小显链长纟靶值 = min(d:=靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈[靶值])
    ls = d[最小显链长纟靶值]
    次大数讠溟次 = {次大数:溟次 for (次大数,内点,溟次) in ls}
    return (最小显链长纟靶值, 次大数讠溟次)
def 后续更新冫靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈乊已有后续简并记录纟递归婪溟链牜靶值大于一扌(靶值讠简并记录, 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈, 简并记录纟当前靶值, /):
    当前靶值 = len(靶值讠简并记录)
    assert 当前靶值 >= 2
    assert 当前靶值 == 简并记录纟当前靶值.靶值
    ... ...
def 初始化构造冫靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈乊后续简并记录纟递归婪溟链牜靶值大于一扌(靶值讠简并记录, /):
    当前靶值 = len(靶值讠简并记录)
    assert 当前靶值 >= 2
    ... ...
    assert min(靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈) == 当前靶值
    return 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈

===
]]
[[
++kw:自顶向下搜索丷自底向上注册
测试:自底向上注册
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌 +自顶向下搜索丷自底向上注册  --ver=2  --休眠期:auto   :/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part1.bottomup.test-out.txt

暂停使用冫自顶向下搜索
file_startswith_    /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part1.bottomup.test-out.txt    script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0001.1-6017.out.txt
    =>same
view /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part1.bottomup.test-out.txt
    [1..=445]
cat script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0001.1-6017.out.txt  | head -n 445  | tail -n +1  |  diff  -s  -   /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part1.bottomup.test-out.txt
    => ... are identical

]]
[[
自底向上注册:
mv -iv script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0002.6018-_.out.txt    script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0002.6018-9192.out.txt
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌  +自顶向下搜索丷自底向上注册   --ver=2  --休眠期:auto   :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0001.1-6017.out.txt    :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0002.6018-9192.out.txt  :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0003.9193-_.bottomup.out.txt

@20260208
mv -iv   script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0003.9193-_.bottomup.out.txt   script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0003.9193-13013.bottomup.out.txt
view script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0003.9193-13013.bottomup.out.txt
(12509, 17, 6, 41, FD('{:[#Bh1+B-B-gh-BAy-D];B:[#BBV+B];}'), RT('[#B+E-B-B-D+C-C+C-G-H-P-P-f-f-.-.-B.-M-By-Q-Du-M-Dy-Q-II-IH-QQ+C-QP-Q-gQ-B-M-B-gQ-Q-BAy-D-M]'), [1, 2, 3, 6, 12, 13, 24, 48, 96, 192, 384, 397, 781, 1562, 3123, 4181, 6261, 12509], [1, 2, 4, 8, 16, 17, 32, 64, 128, 256, 512, 1024, 1041, 2082, 4164, 8328, 12496, 12509], [1, 2, 3, 6, 12, 13, 24, 48, 96, 192, 384, 397, 781, 1562, 3124, 6248, 6261, 12509], [1, 2, 4, 8, 16, 17, 32, 64, 128, 256, 512, 1024, 1041, 2082, 4164, 8328, 12492, 12509], [1, 2, 3, 6, 12, 13, 24, 48, 96, 192, 384, 397, 781, 1562, 3124, 6248, 6261, 12509], [1, 2, 4, 8, 12, 13, 24, 48, 96, 192, 384, 768, 781, 1562, 3124, 6248, 12496, 12509])

du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0001.1-6017.out.txt
    5.5M
du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0002.6018-9192.out.txt
    4.1M
du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0003.9193-13013.bottomup.out.txt
    5.1M

]]
[[
@20260208
++kw:鬽最大靶值
++乸异常牜最大靶值
测试:kw:鬽最大靶值
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌 --鬽最大靶值=500 +自顶向下搜索丷自底向上注册  --ver=2  --休眠期:auto   :/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part1.bottomup.test-out.txt   :/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part2.446-500.bottomup.test-out.txt
    再次执行:^script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.乸异常牜最大靶值: 500
cat script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0001.1-6017.out.txt  | head -n 500  | tail -n +446  |  diff  -s  -   /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part2.446-500.bottomup.test-out.txt
    => ... are identical

]]
[[
@20260208
++kw:彣匹配模板纟前置文件路径冃靶值讠简并记录#smay_shell_pattern4pre_ipaths
测试:kw:彣匹配模板纟前置文件路径冃靶值讠简并记录
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌 --鬽最大靶值=500 +自顶向下搜索丷自底向上注册  --ver=2  --休眠期:auto   --彣匹配模板纟前置文件路径冃靶值讠简并记录:'/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part?.bottomup.test-out.txt'   :/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part2.446-500.bottomup.test-out.txt
]]
[[
分离出来:规范冫列表纟文件路径冃靶值讠简并记录扌
分离出来:mk_rest_func_
测试:规范冫列表纟文件路径冃靶值讠简并记录扌
测试:mk_rest_func_
prefix=/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌  --鬽最大靶值=530  +自顶向下搜索丷自底向上注册   --ver=2  --休眠期:auto      --彣匹配模板纟前置文件路径冃靶值讠简并记录:${prefix}'枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part*.bottomup.test-out.txt'   :${prefix}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part3.501-530.bottomup.test-out.txt
cat script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0001.1-6017.out.txt  | head -n 530  | tail -n +501  |  diff  -s  -   ${prefix}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part3.501-530.bottomup.test-out.txt
    => ... are identical
rm -iv ${prefix}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part3.501-530.bottomup.test-out.txt
]]
[[
@20260208
自底向上注册x鬽最大靶值x彣匹配模板纟前置文件路径冃靶值讠简并记录:
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌  --鬽最大靶值=16016  +自顶向下搜索丷自底向上注册   --ver=2  --休眠期:auto      --彣匹配模板纟前置文件路径冃靶值讠简并记录:'script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt'     :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0004.13014-16016.bottomup.out.txt
    完成@20260209晚八点
    # [:曾经主要作业命令行]:goto

du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt
    5.5M #1-6017.out.txt
    4.1M #6018-9192.out.txt
    5.1M #9193-13013.bottomup.out.txt
    4.6M #13014-16016.bottomup.out.txt
    ~=20M
]]
[[
@20260208
失败:加强猜测约束牜极简次大数集:
  [靶值 == 次大数 + (内点<<溟次)]
  [内点 in {次大数, *靶值讠简并记录[次大数].次大数讠溟次, 2, 1}]
极简次大数集-->极简次大数讠溟次
另档冫极简次大数集纟简并记录纟递归婪溟链扌
def 另档冫极简次大数集纟简并记录纟递归婪溟链扌(输出文件路径冃靶值讠极简次大数集, /, *列表纟输入文件路径冃靶值讠简并记录, ver, 彣匹配模板纟前置文件路径冃靶值讠简并记录=''):
测试:另档冫极简次大数集纟简并记录纟递归婪溟链扌
prefix=/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   @另档冫极简次大数集纟简并记录纟递归婪溟链扌  --ver=2   :${prefix}另档冫极简次大数集纟简并记录纟递归婪溟链扌.ver2.part-1-2.1-500.bottomup.test-out.txt    --彣匹配模板纟前置文件路径冃靶值讠简并记录:${prefix}'枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part?.bottomup.test-out.txt'   :${prefix}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part2.446-500.bottomup.test-out.txt
    ^Exception: 59
    失败！
view /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫极简次大数集纟简并记录纟递归婪溟链扌.ver2.part-1-2.1-500.bottomup.test-out.txt

rm -iv /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫极简次大数集纟简并记录纟递归婪溟链扌.ver2.part-1-2.1-500.bottomup.test-out.txt
]]
[[
@20260208
失败:加强猜测约束牜幸存次大数必由集:
  [靶值 == 次大数 + (内点<<溟次)]
  [内点 in {次大数, 2, 1, *靶值讠幸存次大数必由集[次大数].幸存次大数讠溟次.keys(), *chains(靶值讠幸存次大数必由集[次大数].幸存次大数讠必由集.values())}]
幸存次大数必由集-->(幸存次大数讠溟次, 幸存次大数讠必由集)
另档冫幸存次大数必由集纟简并记录纟递归婪溟链扌
def 另档冫幸存次大数必由集纟简并记录纟递归婪溟链扌(输出文件路径冃靶值讠幸存次大数必由集, /, *列表纟输入文件路径冃靶值讠简并记录, ver, 彣匹配模板纟前置文件路径冃靶值讠简并记录=''):
测试:另档冫幸存次大数必由集纟简并记录纟递归婪溟链扌
prefix=/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   @另档冫幸存次大数必由集纟简并记录纟递归婪溟链扌  --ver=2   :${prefix}另档冫幸存次大数必由集纟简并记录纟递归婪溟链扌.ver2.part-1-2.1-500.bottomup.test-out.txt    --彣匹配模板纟前置文件路径冃靶值讠简并记录:${prefix}'枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part?.bottomup.test-out.txt'   :${prefix}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part2.446-500.bottomup.test-out.txt
    ^Exception: 77
    失败！
view /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫幸存次大数必由集纟简并记录纟递归婪溟链扌.ver2.part-1-2.1-500.bottomup.test-out.txt



]]
[[
@20260208
失败:双定点最短加靶链简并态
(靶值讠定点讠简并态, 靶值讠次大数讠溟次)
    [1<=定点<=靶值]
* [1 <= 定点 < 靶值]:
    #########
    #xxx:[靶值讠定点讠简并态[靶值][定点] := {u | [[(次大数,溟次):<-靶值讠次大数讠溟次[靶值].items()][内点 := (靶值-次大数)>>溟次][次偏简并态:=靶值讠定点讠简并态[次大数][内点]][定点 <- 次偏简并态][u:<-???如何筛选:次偏简并态]]}]
        不行！除非:[定点<-{次大数,内点}]，否则:需要:仨定点简并态！
    #########
* [定点 == 靶值]:
    #########
    ... ...
    #########

]]
[[
@20260208
失败{@靶值=2077}:易来简并态
    易来:容易得到的，计算量小的
双定点最短加靶链易来简并态
双点易来简并态
(靶值讠定点讠易来简并态, 靶值讠易来次大数讠溟次)
    [1<=定点<=靶值]
* [3 <= 定点 < 靶值]:
    #########
    [靶值讠定点讠易来简并态[靶值][定点] := {u | [[(次大数,溟次):<-靶值讠易来次大数讠溟次[靶值].items()][内点 := (靶值-次大数)>>溟次][内点溟化值集 := {内点<<ez | [ez:<-[0..=溟次]]}][内有效集 := if [定点 <- {次大数,min(次大数,2),1}\-/内点溟化值集] then 靶值讠定点讠易来简并态[次大数][内点] elif [定点>次大数] then {} elif [内点 <- {次大数,min(次大数,2),1}] then 靶值讠定点讠易来简并态[次大数][定点] elif [定点<-靶值讠定点讠易来简并态[次大数][内点]] then {定点} else {}][有效集 := if 内有效集 then {靶值,次大数,2,1}\-/内点溟化值集\-/内有效集 else {}][u:<-有效集]]}]
    #########
* [定点 == 靶值]or[定点<=min(靶值,2)]:
    #########
    [靶值讠定点讠易来简并态[靶值][定点] := {靶值,定点}\-/{u | [[(次大数,溟次):<-靶值讠易来次大数讠溟次[靶值].items()][内点 := (靶值-次大数)>>溟次][内点溟化值集 := {内点<<ez | [ez:<-[0..=溟次]]}][内有效集 := 靶值讠定点讠易来简并态[次大数][内点]][有效集 := 内点溟化值集\-/内有效集][u:<-有效集]]}]
    #########

另档冫双点易来简并态纟简并记录纟递归婪溟链扌
def 另档冫双点易来简并态纟简并记录纟递归婪溟链扌(输出文件路径冃靶值讠双点易来简并态, /, *列表纟输入文件路径冃靶值讠简并记录, ver, 彣匹配模板纟前置文件路径冃靶值讠简并记录=''):
测试:另档冫双点易来简并态纟简并记录纟递归婪溟链扌
prefix=/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   @另档冫双点易来简并态纟简并记录纟递归婪溟链扌  --ver=2   :${prefix}另档冫双点易来简并态纟简并记录纟递归婪溟链扌.ver2.part-1-2.1-500.bottomup.test-out.txt    --彣匹配模板纟前置文件路径冃靶值讠简并记录:${prefix}'枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part?.bottomup.test-out.txt'   :${prefix}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part2.446-500.bottomup.test-out.txt
view /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫双点易来简并态纟简并记录纟递归婪溟链扌.ver2.part-1-2.1-500.bottomup.test-out.txt
du -h /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫双点易来简并态纟简并记录纟递归婪溟链扌.ver2.part-1-2.1-500.bottomup.test-out.txt
    3.4M

小数据成功，但是 存储空间开销大
    =>考虑使用:NonTouchRanges+intern()
    但 更重要更难避免的毛病 是 计算时间开销大


===
欤按需计算:=True
    有用性？
    只保留:靶值讠易来简并态
        因为 后面 此靶值 将作为 更大靶值 的 潜在次大数 出现，需要 查询 内点 是否 在内
    靶值讠定点讠易来简并态-->靶值讠定点讠易来简并态扌

    靶值讠定点讠易来简并态扌(靶值讠易来简并态, 缓存冃靶值讠定点讠易来简并态, 靶值, 定点) -> 易来简并态

按需计算
另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌
def 另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌(输出文件路径冃靶值讠双点易来简并态, /, *列表纟输入文件路径冃靶值讠简并记录, ver, 彣匹配模板纟前置文件路径冃靶值讠简并记录=''):
测试:另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌
prefix=/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   @另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌  --ver=2   :${prefix}另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌.ver2.part-1-2.1-500.bottomup.test-out.txt    --彣匹配模板纟前置文件路径冃靶值讠简并记录:${prefix}'枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part?.bottomup.test-out.txt'   :${prefix}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part2.446-500.bottomup.test-out.txt
view /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌.ver2.part-1-2.1-500.bottomup.test-out.txt
小数据成功
    但见下面:^Exception: 2077
du -h /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌.ver2.part-1-2.1-500.bottomup.test-out.txt
    216K#py.dict+py.set
    120K#py.dict+ranges2delta_txt_
    84K#_表述冫次大数讠溟次讠文本表达扌+ranges2delta_txt_


]]
[[
回到上面:见上面:按需计算
#.@20260208
#.易来偏次简并态
#.    易来简并态:容易得到的，计算量小的
#.    偏次简并态:[双定点==(靶值,靶值or次大数)]
#.(靶值讠定点讠易来偏次简并态, 靶值讠易来偏次次大数讠溟次)
#.    [定点 <- {靶值}\-/易来偏次次大数讠溟次.keys()]
#.        #[1<=定点<=靶值]
#.
#.
#.[靶值讠定点讠易来偏次简并态[靶值][靶值] := 缓存...]
#.    因为 后面 此靶值 将作为 更大靶值 的 潜在次大数 出现，需要 查询 内点 是否 在内
#.
#.按需计算:[靶值讠定点讠易来偏次简并态[靶值][次大数] := ...]
#.
#.[按需计算:靶值讠定点讠易来偏次简并态[靶值][1] := 靶值讠定点讠易来偏次简并态[靶值][靶值]]
#.[按需计算:靶值讠定点讠易来偏次简并态[靶值][2] := 靶值讠定点讠易来偏次简并态[靶值][靶值]]
#.
#.[按需计算:靶值讠定点讠易来偏次简并态[靶值][定点] := {u | [[(次大数,溟次):<-靶值讠易来次大数讠溟次[靶值].items()][内点 := (靶值-次大数)>>溟次][内点溟化值集 := {内点<<ez | [ez:<-[0..=溟次]]}][内有效集 := if [定点 <- {次大数,min(次大数,2),1}\-/内点溟化值集] then 靶值讠定点讠易来偏次简并态[次大数][内点] elif [定点>次大数] then {} elif [内点 <- {次大数,min(次大数,2),1}] then 靶值讠定点讠易来偏次简并态[次大数][定点] elif [定点<-靶值讠定点讠易来偏次简并态[次大数][内点]] then {定点} else {}][有效集 := if 内有效集 then {靶值,次大数,2,1}\-/内点溟化值集\-/内有效集 else {}][u:<-有效集]]}]
#.

]]
[[
按需计算
另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌
prefix0=script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   @另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌  --ver=2  +verbose  :${prefix0}另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌.ver2.part-1-2-3-4.1-14781.bottomup.test-out.txt    --彣匹配模板纟前置文件路径冃靶值讠简并记录:${prefix0}'枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt'     :${prefix0}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0004.13014-16016.bottomup.out.txt
    ^Exception: 2077
view script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌.ver2.part-1-2-3-4.1-14781.bottomup.test-out.txt
du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌.ver2.part-1-2-3-4.1-14781.bottomup.test-out.txt
    636K
rm -iv script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌.ver2.part-1-2-3-4.1-14781.bottomup.test-out.txt


###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   @另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌  --ver=2  +verbose  :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌.ver2.part1.1-2076.test-out.txt    :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0001.1-6017.out.txt
    ^Exception: 2077
view script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌.ver2.part1.1-2076.test-out.txt
du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌.ver2.part1.1-2076.test-out.txt
rm -iv script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌.ver2.part1.1-2076.test-out.txt

]]
[[
测试:另档冫尾六表纟简并记录纟递归婪溟链扌
def 另档冫尾六表纟简并记录纟递归婪溟链扌(输出文件路径冃靶值讠尾六表, /, *列表纟输入文件路径冃靶值讠尾六表, ver, 彣匹配模板纟前置文件路径冃靶值讠尾六表='', verbose=False):
prefix=/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   @另档冫尾六表纟简并记录纟递归婪溟链扌  +verbose  --ver=2   :${prefix}另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2.1-500.bottomup.test-out.txt    --彣匹配模板纟前置文件路径冃靶值讠尾六表:${prefix}'枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part?.bottomup.test-out.txt'   :${prefix}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part2.446-500.bottomup.test-out.txt
view /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2.1-500.bottomup.test-out.txt
rm -iv /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2.1-500.bottomup.test-out.txt




提取数据:提取冫尾六表:
prefix0=script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   @另档冫尾六表纟简并记录纟递归婪溟链扌  --ver=2  +verbose  :${prefix0}另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2-3-4.1-15062.extract-out.txt    --彣匹配模板纟前置文件路径冃靶值讠尾六表:${prefix0}'枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt'     :${prefix0}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0004.13014-16016.bottomup.out.txt

15062
view script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2-3-4.1-15062.extract-out.txt
du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2-3-4.1-15062.extract-out.txt
    6.8M
    =>ver3
rm -iv script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2-3-4.1-15062.extract-out.txt


]]
[[
++ver3
++MAX_VERSION
下上界辻左右大小四色最短加链-->(自然数集,6址引列表)$ranges2delta_txt_

测试:转换冫文件格式纟简并记录纟递归婪溟链灬扌
prefix=/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   @转换冫文件格式纟简并记录纟递归婪溟链灬扌  +verbose  --verI=2 --verO=3   :${prefix}转换冫文件格式纟简并记录纟递归婪溟链灬扌.ver3.part-1-2.1-500.bottomup.test-out.txt    --彣匹配模板纟前置文件路径冃靶值讠简并记录:${prefix}'枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part?.bottomup.test-out.txt'   :${prefix}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part2.446-500.bottomup.test-out.txt
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   @转换冫文件格式纟简并记录纟递归婪溟链灬扌  +verbose  --verI=3 --verO=1   :${prefix}转换冫文件格式纟简并记录纟递归婪溟链灬扌.ver1.part-1-2.1-500.bottomup.test-out.txt   :${prefix}转换冫文件格式纟简并记录纟递归婪溟链灬扌.ver3.part-1-2.1-500.bottomup.test-out.txt
view /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫文件格式纟简并记录纟递归婪溟链灬扌.ver1.part-1-2.1-500.bottomup.test-out.txt
view /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫文件格式纟简并记录纟递归婪溟链灬扌.ver3.part-1-2.1-500.bottomup.test-out.txt

du -h /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫文件格式纟简并记录纟递归婪溟链灬扌.ver1.part-1-2.1-500.bottomup.test-out.txt
    324K
du -h /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫文件格式纟简并记录纟递归婪溟链灬扌.ver3.part-1-2.1-500.bottomup.test-out.txt
    176K

rm -iv /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫文件格式纟简并记录纟递归婪溟链灬扌.ver1.part-1-2.1-500.bottomup.test-out.txt
rm -iv /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫文件格式纟简并记录纟递归婪溟链灬扌.ver3.part-1-2.1-500.bottomup.test-out.txt


]]
[[
测试:转换冫尾六表纟简并记录纟递归婪溟链扌
prefix=/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   @转换冫尾六表纟简并记录纟递归婪溟链扌  +verbose  --verI=2 --verO=3   :${prefix}转换冫尾六表纟简并记录纟递归婪溟链扌.ver3.part-1-2.1-500.bottomup.test-out.txt    --彣匹配模板纟前置文件路径冃靶值讠尾六表:${prefix}'枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part?.bottomup.test-out.txt'   :${prefix}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part2.446-500.bottomup.test-out.txt
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   @转换冫尾六表纟简并记录纟递归婪溟链扌  +verbose  --verI=3 --verO=2   :${prefix}转换冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2.1-500.bottomup.test-out.txt   :${prefix}转换冫尾六表纟简并记录纟递归婪溟链扌.ver3.part-1-2.1-500.bottomup.test-out.txt
view /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2.1-500.bottomup.test-out.txt
view /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫尾六表纟简并记录纟递归婪溟链扌.ver3.part-1-2.1-500.bottomup.test-out.txt

du -h /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2.1-500.bottomup.test-out.txt
    212K
du -h /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫尾六表纟简并记录纟递归婪溟链扌.ver3.part-1-2.1-500.bottomup.test-out.txt
    176K

rm -iv /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2.1-500.bottomup.test-out.txt
rm -iv /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫尾六表纟简并记录纟递归婪溟链扌.ver3.part-1-2.1-500.bottomup.test-out.txt


]]
[[
++kw:欤删除中段数据
++kw:欤允许输入输出是同版本
测试:转换冫尾六表纟简并记录纟递归婪溟链扌
prefix=/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   @转换冫尾六表纟简并记录纟递归婪溟链扌  +欤删除中段数据  +verbose  --verI=2 --verO=3   :${prefix}转换冫尾六表纟简并记录纟递归婪溟链扌.ver3.part-1-2.1-500.bottomup.欤删除中段数据.test-out.txt    --彣匹配模板纟前置文件路径冃靶值讠尾六表:${prefix}'枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part?.bottomup.test-out.txt'   :${prefix}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part2.446-500.bottomup.test-out.txt
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   @转换冫尾六表纟简并记录纟递归婪溟链扌  +欤允许输入输出是同版本   +欤删除中段数据  +verbose  --verI=2 --verO=2   :${prefix}转换冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2.1-500.bottomup.欤删除中段数据.test-out.txt    --彣匹配模板纟前置文件路径冃靶值讠尾六表:${prefix}'枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part?.bottomup.test-out.txt'   :${prefix}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part2.446-500.bottomup.test-out.txt

view /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2.1-500.bottomup.欤删除中段数据.test-out.txt
view /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫尾六表纟简并记录纟递归婪溟链扌.ver3.part-1-2.1-500.bottomup.欤删除中段数据.test-out.txt

du -h /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2.1-500.bottomup.欤删除中段数据.test-out.txt
    128K
du -h /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫尾六表纟简并记录纟递归婪溟链扌.ver3.part-1-2.1-500.bottomup.欤删除中段数据.test-out.txt
    92K

rm -iv /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2.1-500.bottomup.欤删除中段数据.test-out.txt
rm -iv /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫尾六表纟简并记录纟递归婪溟链扌.ver3.part-1-2.1-500.bottomup.欤删除中段数据.test-out.txt



提取数据:提取冫尾六表:
prefix0=script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   @另档冫尾六表纟简并记录纟递归婪溟链扌  --ver=2  +verbose  :${prefix0}另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2-3-4.1-16016.extract-out.txt    --彣匹配模板纟前置文件路径冃靶值讠尾六表:${prefix0}'枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt'     :${prefix0}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0004.13014-16016.bottomup.out.txt

16016-ver2
head script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2-3-4.1-16016.extract-out.txt
du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2-3-4.1-16016.extract-out.txt
    ver2:       7.3M
    vs:ver3:    4.9M
rm -iv script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2-3-4.1-16016.extract-out.txt

===
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   @另档冫尾六表纟简并记录纟递归婪溟链扌  --ver=-1 --verI=2  --verO=3  +verbose  :${prefix0}另档冫尾六表纟简并记录纟递归婪溟链扌.ver3.part-1-2-3-4.1-16016.extract-out.txt    --彣匹配模板纟前置文件路径冃靶值讠尾六表:${prefix0}'枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt'     :${prefix0}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0004.13014-16016.bottomup.out.txt

16016-ver3
view script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫尾六表纟简并记录纟递归婪溟链扌.ver3.part-1-2-3-4.1-16016.extract-out.txt
du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫尾六表纟简并记录纟递归婪溟链扌.ver3.part-1-2-3-4.1-16016.extract-out.txt
    ver3:       4.9M
    vs:ver2:    7.3M
    但是，转换格式费时显著！
rm -iv script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫尾六表纟简并记录纟递归婪溟链扌.ver3.part-1-2-3-4.1-16016.extract-out.txt


===
tar -cvf script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2-3-4.1-16016.extract-out.txt.tar.lzma --lzma -C script/  min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2-3-4.1-16016.extract-out.txt
tar -cvf script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫尾六表纟简并记录纟递归婪溟链扌.ver3.part-1-2-3-4.1-16016.extract-out.txt.tar.lzma --lzma -C script/  min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫尾六表纟简并记录纟递归婪溟链扌.ver3.part-1-2-3-4.1-16016.extract-out.txt

du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫尾六表纟简并记录纟递归婪溟链扌.ver?.part-1-2-3-4.1-16016.extract-out.txt.tar.lzma
    600K#ver2#看来还是原版更好压缩
    1.1M#ver3

rm -iv script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫尾六表纟简并记录纟递归婪溟链扌.ver3.part-1-2-3-4.1-16016.extract-out.txt.tar.lzma


tar -xvf script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2-3-4.1-16016.extract-out.txt.tar.lzma -O | more
    # 旧版:[:主要尾六表另档文件]:goto
===
]]
[[
1-16016完成@20260209晚八点
tar -cvf script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part-1-2-3-4.1-16016.out.txt.tar.lzma --lzma   script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt
du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part-1-2-3-4.1-16016.out.txt.tar.lzma
    4.3M # vs ~20M
tar -xf script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part-1-2-3-4.1-16016.out.txt.tar.lzma -O | head -n 6019 | tail -n +6016 | more
    # [:主要简并记录输出文件]:goto
from seed.for_libs.for_tarfile import iter_chain_read_multi_tarfile_

===
尝试:压缩ver1:结果不如ver2
prefix0=script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   @转换冫文件格式纟简并记录纟递归婪溟链灬扌  +verbose  --verI=2 --verO=1   :${prefix0}转换冫文件格式纟简并记录纟递归婪溟链灬扌.ver1.part-1-2-3-4.1-16016.out.txt    --彣匹配模板纟前置文件路径冃靶值讠简并记录:${prefix0}'枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt'     :${prefix0}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0004.13014-16016.bottomup.out.txt
head script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫文件格式纟简并记录纟递归婪溟链灬扌.ver1.part-1-2-3-4.1-16016.out.txt
du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫文件格式纟简并记录纟递归婪溟链灬扌.ver1.part-1-2-3-4.1-16016.out.txt
    46M
tar -cvf script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver1.part-1-2-3-4.1-16016.out.txt.tar.lzma --lzma   script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫文件格式纟简并记录纟递归婪溟链灬扌.ver1.part-1-2-3-4.1-16016.out.txt
du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver1.part-1-2-3-4.1-16016.out.txt.tar.lzma
    ver1:       6.1M # vs 46M
    vs:ver2:    4.3M # vs ~20M

rm -iv script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫文件格式纟简并记录纟递归婪溟链灬扌.ver1.part-1-2-3-4.1-16016.out.txt
]]
[[
DONE:最短加链牜左侧最大:头部二幂多长？
    看来，总有 最短加链牜左侧最大:[1,2,3,...]
head script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2-3-4.1-16016.extract-out.txt
求最小比率: 长度纟头部二幂/最小显链长
def 求冫丮最小比率辻靶值列表厈牜长度纟头部二幂纟左侧最大最短加链之于最小显链长纟靶值扌(*列表纟输入文件路径冃靶值讠尾六表, ver, verbose=False):

echo script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt  |  sed 's/script/:\0/g'
printf ' :%s' script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   @求冫丮最小比率辻靶值列表厈牜长度纟头部二幂纟左侧最大最短加链之于最小显链长纟靶值扌  +verbose  --ver=2      $(printf ' :%s' script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt)
    =>: (Fraction(1, 17), [14759, 15449])
        # 注意:局限于[靶值<-[1..=16016]]
===
tail -n 1258 script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0004.13014-16016.bottomup.out.txt | head -n 1
(14759, 17, 4, 32, FD('{:[#CKa+B-B9-oF-D7];}'), RT('[#B+D-B-E-C-G-C-Q-F-h-L-BD-X-CH-v-EP-C-Bc-Ii-C8-RF-F5-M-D7-oF-B9-uM-B9-oF-D7-uM]'), [1, 2, 3, 5, 10, 13, 23, 46, 92, 184, 368, 643, 1283, 2566, 2957, 5775, 8858, 14759], [1, 2, 3, 5, 10, 20, 40, 80, 160, 320, 640, 736, 1472, 2944, 3209, 5901, 11802, 14759], [1, 2, 3, 5, 10, 13, 23, 46, 92, 184, 368, 736, 1472, 2944, 2957, 5901, 8858, 14759], [1, 2, 3, 5, 10, 20, 40, 80, 160, 320, 640, 643, 1283, 2566, 3209, 5775, 11550, 14759], [1, 2, 3, 5, 10, 13, 23, 46, 92, 184, 368, 736, 1472, 2944, 2957, 5901, 8858, 14759], [1, 2, 3, 5, 10, 13, 23, 46, 92, 184, 368, 736, 1472, 2944, 2957, 5901, 11802, 14759])
===
tail -n 568 script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0004.13014-16016.bottomup.out.txt | head -n 1
(15449, 17, 6, 41, FD('{:[#CQ2+B-P3-n-fv-vC];B:[#BRT+B];}'), RT('[#B+D-B+C-D-B-H-D-P-H-f-P+C-_-f+D-B9-.-B-D9-CD-H7-EH-P3-C-IM-C-fs-C-n-n-PP-wS-PP-n-n-fv-vC-BP]'), [1, 2, 3, 5, 10, 20, 40, 80, 97, 193, 386, 772, 1544, 2563, 3091, 5163, 9270, 15449], [1, 2, 3, 6, 12, 24, 48, 96, 192, 384, 640, 1280, 2560, 5120, 5123, 10246, 15369, 15449], [1, 2, 3, 5, 10, 20, 40, 80, 160, 320, 640, 1280, 2560, 2563, 5123, 5163, 10286, 15449], [1, 2, 3, 6, 12, 24, 48, 96, 192, 384, 386, 772, 1544, 3088, 3091, 6179, 12358, 15449], [1, 2, 3, 6, 12, 24, 48, 96, 97, 193, 386, 772, 1544, 3088, 3091, 6179, 9270, 15449], [1, 2, 3, 5, 10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120, 5123, 10246, 15369, 15449])
===


]]
[[
@20260210
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌  --鬽最大靶值=20020  +自顶向下搜索丷自底向上注册   --ver=2  --休眠期:auto      --彣匹配模板纟前置文件路径冃靶值讠简并记录:'script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt'     :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0005.16017-20020.bottomup.out.txt
    # [:曾经主要作业命令行]:goto
    @20260210清晨:启动:16017..
    @20260211清晨:..=17500
    @20260212清晨:完成

du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0005.16017-20020.bottomup.out.txt
    6.7M

]]
[[
@20260212
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌  --鬽最大靶值=23023  +自顶向下搜索丷自底向上注册   --ver=2  --休眠期:auto      --彣匹配模板纟前置文件路径冃靶值讠简并记录:'script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt'     :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0006.20021-23023.bottomup.out.txt
    # [:曾经主要作业命令行]:goto
    @20260212傍晚:启动:20021..
    @20260213深夜:完成
du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0006.20021-23023.bottomup.out.txt
    4.6M

]]
[[
@20260213
DONE:丢弃越界:鬽最大靶值x自底向上
测试:丢弃越界:
prefix=/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌 --鬽最大靶值=500 +自顶向下搜索丷自底向上注册  --ver=2  --休眠期:auto   --彣匹配模板纟前置文件路径冃靶值讠简并记录:${prefix}'枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part?.bottomup.test-out.txt'   :${prefix}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part2.446-500.bottomup.test-out.txt


###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌 --鬽最大靶值=253 +自顶向下搜索丷自底向上注册  --ver=2  --休眠期:auto    :${prefix}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part1-2.1-500.bottomup.test-out2.txt
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌 --鬽最大靶值=323 +自顶向下搜索丷自底向上注册  --ver=2  --休眠期:auto    :${prefix}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part1-2.1-500.bottomup.test-out2.txt
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌 --鬽最大靶值=500 +自顶向下搜索丷自底向上注册  --ver=2  --休眠期:auto    :${prefix}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part1-2.1-500.bottomup.test-out2.txt
file_startswith_    /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part1-2.1-500.bottomup.test-out2.txt   script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0001.1-6017.out.txt
    =>same
]]
[[
DONE{内点址距 不可控}:递归婪溟链:最大纟最小主线距离纟次大数辻内点乊靶值==max{min{址引纟次大数-址引纟内点 | [us:<-最短加链/-\递归婪溟链][主线:=递归婪溟链主线纟(us)][次大数:=主线[-2]][内点:=max{n | [ez:<-[0..]][n:=(靶值-次大数)/2**ez][n<-us]}][址引纟次大数:=主线.index(次大数)][址引纟内点:=主线.index(内点)]} | [靶值:<-[2..]]}
from seed.math.power.addition_chain.shortest.rewrite3 import 枚举冫递归婪溟链巛严序加链扌
  .次大数址引讠内点址距
最大化乊已有简并记录冫最小化乊尾四链冫最大内点址距乊加链扌
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,最大化乊已有简并记录冫最小化乊尾四链冫最大内点址距乊加链扌  +欤趃输出 +欤记录首峰值位 +verbose  --ver=2      $(printf ' :%s' /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part?.bottomup.test-out.txt)
    # 注意:局限于[靶值<-[1..=455]]
... ...
靶值: 445
8
(1, 3, 5, 10, 13, 23, 46, 92, 184, 185, 369)
(1, 2, 4, 8, 16, 80, 144, 288, 368, 369)
(1, 3, 5, 10, 13, 26, 52, 104, 208, 209, 417)
(1, 3, 6, 7, 13, 26, 52, 104, 208, 209, 417)
(1, [(1, 3, 7), (1, 3, 4, 7)])
(2, [(1, 3, 5, 10, 13), (1, 3, 6, 7, 13)])
(3, [(1, 3, 9, 18, 19, 37), (1, 5, 9, 18, 19, 37), (1, 2, 4, 36, 37)])
(4, [(1, 3, 5, 10, 20, 21, 41), (1, 2, 4, 8, 40, 41)])(5, [(1, 3, 5, 10, 20, 40, 41, 81), (1, 2, 4, 8, 16, 80, 81)])
(6, [(1, 3, 5, 7, 14, 19, 38, 76, 152, 157), (1, 3, 9, 18, 21, 39, 78, 79, 157)])
(7, [(1, 3, 5, 10, 13, 23, 46, 92, 93, 185), (1, 2, 4, 8, 40, 72, 144, 184, 185)])
(8, [(1, 3, 5, 10, 13, 23, 46, 92, 184, 185, 369), (1, 2, 4, 8, 16, 80, 144, 288, 368, 369)])


(369, 11, 20, 94, ..., [1, 2, 3, 5, 10, 13, 23, 46, 92, 184, 185, 369], [1, 2, 4, 8, 16, 32, 64, 80, 144, 288, 368, 369], [1, 2, 3, 5, 10, 13, 23, 46, 92, 184, 185, 369], [1, 2, 4, 8, 16, 32, 48, 80, 160, 320, 368, 369])
    尾四链 只要 3条
(417, 11, 16, 77, ..., [1, 2, 3, 5, 10, 13, 26, 52, 104, 208, 209, 417], [1, 2, 4, 8, 16, 32, 64, 128, 256, 384, 416, 417], [1, 2, 3, 6, 7, 13, 26, 52, 104, 208, 209, 417], [1, 2, 4, 8, 16, 32, 64, 128, 256, 384, 416, 417])
    尾四链 只要 3条

>>> uss = ([1, 2, 3, 5, 10, 13, 23, 46, 92, 184, 185, 369], [1, 2, 4, 8, 16, 32, 64, 80, 144, 288, 368, 369], [1, 2, 4, 8, 16, 32, 48, 80, 160, 320, 368, 369])
>>> [[(str(递归婪溟链), max(递归婪溟链.次大数址引讠内点址距)) for 递归婪溟链 in 枚举冫递归婪溟链巛严序加链扌(us)] for us in uss]
[[('[1~3~5~10~13~23~46~92~184~185~369]', 8)], [('[1~2~4~8~16~80~144~288~368~369]', 8)], [('[1~2~4~8~16~48~80~160~320~368~369]', 9)]]





###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,最大化乊已有简并记录冫最小化乊尾四链冫最大内点址距乊加链扌  +欤趃输出 +欤记录首峰值位 +verbose  --ver=2      $(printf ' :%s' script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt)
    # 注意:局限于[靶值<-[1..=22463]]
... ...
靶值: 22463
14
(1, 3, 5, 10, 13, 23, 46, 92, 184, 185, 369, 738, 1476, 2952, 5904, 5905, 11809)
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 2560, 4608, 9216, 11776, 11808, 11809)
(1, 3, 5, 10, 13, 23, 46, 92, 184, 368, 371, 739, 1478, 2956, 5912, 5913, 11825)
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 2560, 2576, 4624, 9248, 11824, 11825)
(1, 3, 5, 10, 13, 23, 46, 92, 93, 185, 370, 740, 1480, 2960, 5920, 5921, 11841)
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 2560, 4608, 9216, 11776, 11840, 11841)
(1, 3, 5, 10, 13, 23, 46, 92, 184, 187, 371, 742, 1484, 2968, 5936, 5937, 11873)
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 2560, 2592, 4640, 9280, 11872, 11873)
(1, 3, 5, 10, 13, 26, 52, 104, 105, 209, 418, 836, 1672, 3344, 6688, 6689, 13377)
(1, 3, 6, 7, 13, 26, 52, 104, 105, 209, 418, 836, 1672, 3344, 6688, 6689, 13377)
(1, 3, 7, 14, 28, 31, 59, 118, 236, 267, 503, 1006, 2012, 4024, 8048, 8049, 16097)
(1, 3, 6, 12, 13, 25, 75, 125, 250, 253, 503, 1006, 2012, 4024, 8048, 8049, 16097)
(1, 3, 5, 10, 13, 23, 46, 59, 151, 302, 604, 1208, 2416, 4832, 9664, 9665, 19329)
(1, 3, 9, 18, 36, 72, 73, 79, 151, 302, 604, 1208, 2416, 4832, 9664, 9665, 19329)
(1, 5, 9, 18, 36, 41, 77, 154, 155, 309, 618, 1236, 2472, 4944, 9888, 9889, 19777)
(1, 2, 4, 8, 16, 32, 64, 128, 256, 2304, 4352, 8704, 17408, 19712, 19776, 19777)
(1, 3, 5, 10, 13, 39, 78, 156, 312, 624, 627, 1251, 2502, 5004, 10008, 10009, 20017)
(1, 3, 9, 18, 21, 39, 78, 156, 312, 624, 627, 1251, 2502, 5004, 10008, 10009, 20017)
(1, 3, 5, 10, 13, 39, 78, 156, 312, 624, 637, 1261, 2522, 5044, 10088, 10089, 20177)
(1, 3, 6, 7, 13, 39, 78, 156, 312, 624, 637, 1261, 2522, 5044, 10088, 10089, 20177)
(1, 3, 5, 10, 20, 40, 80, 160, 320, 640, 641, 1281, 2562, 5124, 10248, 10249, 20497)
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 20480, 20496, 20497)
(1, 3, 5, 10, 20, 40, 80, 160, 320, 321, 641, 1282, 2564, 5128, 10256, 10257, 20513)
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 20480, 20512, 20513)
(1, 3, 5, 10, 20, 40, 80, 160, 161, 321, 642, 1284, 2568, 5136, 10272, 10273, 20545)
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 20480, 20544, 20545)
(1, 3, 5, 10, 20, 40, 80, 81, 161, 322, 644, 1288, 2576, 5152, 10304, 10305, 20609)
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 20480, 20608, 20609)
(1, 3, 5, 10, 20, 40, 41, 81, 162, 324, 648, 1296, 2592, 5184, 10368, 10369, 20737)
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 20480, 20736, 20737)
(1, 3, 5, 10, 20, 21, 41, 82, 164, 328, 656, 1312, 2624, 5248, 10496, 10497, 20993)
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 20480, 20992, 20993)
(1, 2, 6, 10, 20, 40, 46, 86, 172, 344, 688, 1376, 2752, 5504, 11008, 11009, 11015, 22023)
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 4608, 4610, 8706, 17412, 22022, 22023)
(1, 3, 5, 10, 20, 23, 43, 86, 172, 344, 688, 1376, 1377, 2753, 5506, 11012, 22024, 22029)
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 4608, 4612, 8708, 17416, 22028, 22029)
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 4608, 4616, 8712, 17424, 22040, 22041)
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 4608, 4624, 8720, 17440, 22064, 22065)
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 4608, 4640, 8736, 17472, 22112, 22113)
(1, [(1, 3, 7), (1, 3, 4, 7)])
(2, [(1, 3, 5, 10, 13), (1, 3, 6, 7, 13)])
(3, [(1, 3, 9, 18, 19, 37), (1, 5, 9, 18, 19, 37), (1, 2, 4, 36, 37)])
(4, [(1, 3, 5, 10, 20, 21, 41), (1, 2, 4, 8, 40, 41)])(5, [(1, 3, 5, 10, 20, 40, 41, 81), (1, 2, 4, 8, 16, 80, 81)])
(6, [(1, 3, 5, 7, 14, 19, 38, 76, 152, 157), (1, 3, 9, 18, 21, 39, 78, 79, 157)])
(7, [(1, 3, 5, 10, 13, 23, 46, 92, 93, 185), (1, 2, 4, 8, 40, 72, 144, 184, 185)])
(8, [(1, 3, 5, 10, 13, 23, 46, 92, 184, 185, 369), (1, 2, 4, 8, 16, 80, 144, 288, 368, 369)])
(9, [(1, 3, 5, 10, 20, 21, 41, 82, 164, 328, 329, 657), (1, 2, 4, 8, 16, 32, 64, 128, 640, 656, 657)])
(10, [(1, 3, 5, 10, 20, 40, 41, 81, 162, 324, 648, 649, 1297), (1, 2, 4, 8, 16, 32, 64, 128, 256, 1280, 1296, 1297)])
(11, [(1, 3, 5, 10, 20, 40, 80, 81, 161, 322, 644, 1288, 1289, 2577), (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 2560, 2576, 2577)])
(12, [(1, 3, 5, 10, 20, 40, 80, 160, 161, 321, 642, 1284, 2568, 2569, 5137), (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 5120, 5136, 5137)])
(13, [(1, 3, 5, 10, 13, 23, 46, 92, 93, 185, 370, 740, 1480, 2960, 2961, 5921), (1, 2, 4, 8, 16, 32, 64, 128, 256, 1280, 2304, 4608, 5888, 5920, 5921)])
(14, [(1, 3, 5, 10, 13, 23, 46, 92, 184, 185, 369, 738, 1476, 2952, 5904, 5905, 11809), (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 2560, 4608, 9216, 11776, 11808, 11809)])

]]
[[
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌  --鬽最大靶值=26026  +自顶向下搜索丷自底向上注册   --ver=2  --休眠期:auto      --彣匹配模板纟前置文件路径冃靶值讠简并记录:'script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt'     :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0007.23024-26026.bottomup.out.txt
    # [:曾经主要作业命令行]:goto
    @20260213深夜:启动
    @20260215下午:完成
du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0007.23024-26026.bottomup.out.txt
    5.0M
]]
[[
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌  --鬽最大靶值=29029  +自顶向下搜索丷自底向上注册   --ver=2  --休眠期:auto      --彣匹配模板纟前置文件路径冃靶值讠简并记录:'script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt'     :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0008.26027-29029.bottomup.out.txt
    # [:曾经主要作业命令行]:goto
    @20260215下午:启动
    @20260216傍晚:完成
du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0008.26027-29029.bottomup.out.txt
    5.4M
]]
[[
上面文件改名前
下面文件改名后:
py_adhoc_call   seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌  --鬽最大靶值=32032  +自顶向下搜索丷自底向上注册   --ver=2  --休眠期:auto      --彣匹配模板纟前置文件路径冃靶值讠简并记录:'script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt'     :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0009.29030-32032.bottomup.out.txt
    # [:曾经主要作业命令行]:goto
    @20260216傍晚:启动
    @20260218下午:完成
du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0009.29030-32032.bottomup.out.txt
    6.4M
===

mkdir /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链
mkdir /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/txt
mkdir /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/tar
mkdir /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/extract
cp -iv -u -t /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/txt/  script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt
    # [:主要数据备份命令]:here

tree /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链
head -n 1 /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/txt/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*
tail -n 1 /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/txt/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*
du -bh /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/txt
    47M#@[1..=32032]
    53M#@[1..=35035]


]]
[[
py_adhoc_call   seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌  --鬽最大靶值=35035  +自顶向下搜索丷自底向上注册   --ver=2  --休眠期:auto      --彣匹配模板纟前置文件路径冃靶值讠简并记录:'script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt'     :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0010.32033-35035.bottomup.out.txt
    # [:曾经主要作业命令行]:goto
    @20260218下午:启动
    @20260220午后:完成

===
head -n 1 script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0010.32033-35035.bottomup.out.txt
tail -n 1 script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0010.32033-35035.bottomup.out.txt
===
ls /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/txt
du -bh /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/txt
    53M#@[1..=35035]
cd /sdcard/0my_files/zip/addition_chain/
tar -cvf 靶值讠简并记录纟递归婪溟链/tar/mixed_recursive_greedy_zpow_addition_chain..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part-01-10.1-35035.out.txt.tar.lzma --lzma  靶值讠简并记录纟递归婪溟链/txt
tar -tf 靶值讠简并记录纟递归婪溟链/tar/mixed_recursive_greedy_zpow_addition_chain..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part-01-10.1-35035.out.txt.tar.lzma
tar -xf 靶值讠简并记录纟递归婪溟链/tar/mixed_recursive_greedy_zpow_addition_chain..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part-01-10.1-35035.out.txt.tar.lzma -O | more
py_adhoc_call  { -end4print }  seed.for_libs.for_tarfile   ,str.iter_chain_read_multi_tarfile_   --xencoding4data:ascii  :靶值讠简并记录纟递归婪溟链/tar/mixed_recursive_greedy_zpow_addition_chain..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part-01-10.1-35035.out.txt.tar.lzma | head -n 6019 | tail -n +6016 | more
du -bh 靶值讠简并记录纟递归婪溟链/tar/mixed_recursive_greedy_zpow_addition_chain..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part-01-10.1-35035.out.txt.tar.lzma
    14M
    # [:主要简并记录输出文件]:here
===
另档:尾六表
prefixZ=/sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/
infixI=min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..
infixO=mixed_recursive_greedy_zpow_addition_chain..
py_adhoc_call   seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain   @另档冫尾六表纟简并记录纟递归婪溟链扌  --ver=2  -verbose  :${prefixZ}extract/${infixO}另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-01-10.1-35035.extract-out.txt    --彣匹配模板纟前置文件路径冃靶值讠尾六表:${prefixZ}txt/${infixI}'枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt'     :${prefixZ}txt/${infixI}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0010.32033-35035.bottomup.out.txt
du -bh /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/extract/mixed_recursive_greedy_zpow_addition_chain..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-01-10.1-35035.extract-out.txt
    18M
tar -cvf 靶值讠简并记录纟递归婪溟链/tar/mixed_recursive_greedy_zpow_addition_chain..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-01-10.1-35035.extract-out.txt.tar.lzma --lzma  -C /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/extract/    mixed_recursive_greedy_zpow_addition_chain..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-01-10.1-35035.extract-out.txt
tar -tf 靶值讠简并记录纟递归婪溟链/tar/mixed_recursive_greedy_zpow_addition_chain..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-01-10.1-35035.extract-out.txt.tar.lzma
tar -xf 靶值讠简并记录纟递归婪溟链/tar/mixed_recursive_greedy_zpow_addition_chain..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-01-10.1-35035.extract-out.txt.tar.lzma -O | more
du -bh /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/tar/mixed_recursive_greedy_zpow_addition_chain..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-01-10.1-35035.extract-out.txt.tar.lzma
    1.5M
    # [:主要尾六表另档文件]:here

cp -iv /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/tar/mixed_recursive_greedy_zpow_addition_chain..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-01-10.1-35035.extract-out.txt.tar.lzma  ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain__six_lists.py..尾六表纟简并记录纟递归婪溟链.ver2.le35035.txt.tar.lzma
e ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain__six_lists.py
from nn_ns.math_nn.numbers.shortest_addition_chain__six_lists import 枚举冫尾六表灬巛靶值灬扌
from nn_ns.math_nn.numbers.shortest_addition_chain__six_lists import 靶值讠尾六表扌, 取冫靶值讠尾六表扌

]]
[[
@20260222
def 另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌(输出文件路径冃靶值讠址距溟次形式, /, *列表纟输入文件路径冃靶值讠尾六表, ver, 彣匹配模板纟前置文件路径冃靶值讠尾六表='', verbose=False):
/sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/extract/mixed_recursive_greedy_zpow_addition_chain..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-01-10.1-35035.extract-out.txt

py_adhoc_call   seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain   @另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌  --ver=2  -verbose  :/sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/extract/mixed_recursive_greedy_zpow_addition_chain..另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌.1-35035.extract-out.txt  :/sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/extract/mixed_recursive_greedy_zpow_addition_chain..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-01-10.1-35035.extract-out.txt

more /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/extract/mixed_recursive_greedy_zpow_addition_chain..另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌.1-35035.extract-out.txt
du -bh /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/extract/mixed_recursive_greedy_zpow_addition_chain..另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌.1-35035.extract-out.txt
    754K

tar -cvf /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/tar/mixed_recursive_greedy_zpow_addition_chain..另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌.1-35035.extract-out.txt.tar.lzma --lzma -C  /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/extract/  mixed_recursive_greedy_zpow_addition_chain..另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌.1-35035.extract-out.txt
tar -xf /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/tar/mixed_recursive_greedy_zpow_addition_chain..另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌.1-35035.extract-out.txt.tar.lzma -O | more

du -bh /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/tar/mixed_recursive_greedy_zpow_addition_chain..另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌.1-35035.extract-out.txt.tar.lzma
    101K

#cp -iv /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/tar/mixed_recursive_greedy_zpow_addition_chain..另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌.1-35035.extract-out.txt.tar.lzma   ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain__max_recur_shortest_stem.py..址距溟次形式纟左侧最大纟递归婪溟链.le35035.txt.tar.lzma
    # 旧版[:主要左侧最大另档文件]:goto
    #   !! 已有[1..=39363]
rm -iv ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain__max_recur_shortest_stem.py..址距溟次形式纟左侧最大纟递归婪溟链.le35035.txt.tar.lzma
e ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain__max_recur_shortest_stem.py
from nn_ns.math_nn.numbers.shortest_addition_chain__max_recur_shortest_stem import 取冫靶值讠婪溟链牜递归最短牜左侧最大扌, 靶值讠婪溟链牜递归最短牜左侧最大扌, 枚举冫婪溟链牜递归最短牜左侧最大灬巛靶值灬扌

e ../../python3_src/seed/math/power/addition_chain/data/get_target_uint2may_optimal_addition_chain7max_recur_shortest_stem_.py
    <=:e ../../python3_src/seed/math/power/addition_chain/data/get_target_uint2may_len_optimal_addition_chain_.py
from seed.math.power.addition_chain.data.get_target_uint2may_optimal_addition_chain7max_recur_shortest_stem_ import 取冫靶值讠婪溟链牜递归最短牜左侧最大扌, 靶值讠婪溟链牜递归最短牜左侧最大扌

]]
[[
@20260223
求冫丮最大比率辻靶值列表厈牜次大数纟右侧最小最短加链之于靶值扌
py_adhoc_call   seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain   @求冫丮最大比率辻靶值列表厈牜次大数纟右侧最小最短加链之于靶值扌  +verbose  --ver=2      $(printf ' :%s' script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt)
    =>: (Fraction(166, 191), [382])
        # 注意:局限于[靶值<-[1..=35035]]
===
head -n 382 script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0001.1-6017.out.txt | tail -n 1
(382, 11, 2, 20, FD('{:[#FM+B-j];}'), RT('[#B+C-B+C-C+C-E-B+C-F-J-M-D-g-I-BJ-R-CT-j-N]'), [1, 2, 4, 5, 9, 14, 23, 46, 83, 166, 332, 382], [1, 2, 4, 8, 16, 17, 33, 50, 92, 184, 368, 382], [1, 2, 4, 5, 9, 14, 23, 46, 92, 184, 368, 382], [1, 2, 4, 8, 16, 17, 33, 50, 83, 166, 332, 382], [1, 2, 4, 8, 16, 17, 33, 50, 83, 166, 332, 382], [1, 2, 4, 5, 9, 14, 23, 46, 92, 184, 368, 382])
===
]]
[[
@20260223
求冫丮最大差值辻靶值列表厈牜两倍次大数纟右侧最小最短加链之于靶值扌
py_adhoc_call   seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain   @求冫丮最大差值辻靶值列表厈牜两倍次大数纟右侧最小最短加链之于靶值扌  +verbose  --ver=2      $(printf ' :%s' script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt)
    =>: (13845, [25127])
        # 注意:局限于[靶值<-[1..=35035]]
===
tail -n 900 script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0007.23024-26026.bottomup.out.txt | head -n 1
(25127, 18, 1, 19, FD('{:[#Ewe+B];}'), RT('[#B+C-B-D-H-P-f-.-B.-D.+C-IA-IA-H.-gC-YC-BAF-CYO-BYI]'), [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 513, 1026, 1539, 2051, 4102, 5641, 9743, 19486, 25127], [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 513, 1026, 1539, 2051, 4102, 5641, 9743, 19486, 25127], [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 513, 1026, 1539, 2051, 4102, 5641, 9743, 19486, 25127], [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 513, 1026, 1539, 2051, 4102, 5641, 9743, 19486, 25127], [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 513, 1026, 1539, 2051, 4102, 5641, 9743, 19486, 25127], [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 513, 1026, 1539, 2051, 4102, 5641, 9743, 19486, 25127])
>>> bin(25127)
'0b110001000100111'

=>:枚举生成冫文件后续简并记录纟递归婪溟链扌():kw:欤最后一跃牜轻算随缘而止
===
]]
[[
@20260223
++kw:欤最后一跃牜轻算随缘而止
测试:kw:欤最后一跃牜轻算随缘而止
prefix=/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..
py_adhoc_call   seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌   -欤只保留首条最短加链乊各次大数  +verbose +欤最后一跃牜轻算随缘而止 --鬽最大靶值=None  +自顶向下搜索丷自底向上注册   --ver=2  --休眠期:auto      --彣匹配模板纟前置文件路径冃靶值讠简并记录:${prefix}'枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part*.bottomup.test-out.txt'   :${prefix}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part4.531-_.bottomup-last_leap.test-out.txt
    [1..=530] ==>> bottomup.last_leap[531..<1097]
    ^AssertionError: (乸简并记录纟递归婪溟链(1097, 13, 6, 14, {41: 5, 73: 4, 553: 1, 1033: 0, 1089: 0, 1096: 0}, NonTouchRanges(((1, 3), (4, 5), (8, 9), (16, 18), (33, 34), (41, 42), (66, 67), (132, 133), (264, 265), (528, 529), (1056, 1057), (1097, 1098))), (1, 2, 4, 8, 16, 17, 33, 41, 66, 132, 264, 528, 1056, 1097), (1, 2, 4, 8, 16, 17, 33, 41, 66, 132, 264, 528, 1056, 1097), (1, 2, 4, 8, 16, 17, 33, 41, 66, 132, 264, 528, 1056, 1097), (1, 2, 4, 8, 16, 17, 33, 41, 66, 132, 264, 528, 1056, 1097), (1, 2, 4, 8, 16, 17, 33, 41, 66, 132, 264, 528, 1056, 1097), (1, 2, 4, 8, 16, 17, 33, 41, 66, 132, 264, 528, 1056, 1097)), 12)
view /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part4.531-_.bottomup-last_leap.test-out.txt
rm -iv /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part4.531-_.bottomup-last_leap.test-out.txt


===
py_adhoc_call   seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌  -欤只保留首条最短加链乊各次大数  +verbose +欤最后一跃牜轻算随缘而止 --鬽最大靶值=None  -自顶向下搜索丷自底向上注册   --ver=2  --休眠期:auto      --彣匹配模板纟前置文件路径冃靶值讠简并记录:${prefix}'枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part*.bottomup.test-out.txt'   :${prefix}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part4.531-_.topdown-last_leap.test-out.txt
    [1..=530] ==>> topdown.last_leap[531..<1103]
    ^AssertionError: (乸简并记录纟递归婪溟链(1103, 14, 32, 15, {1102: 0, 1101: 0, 1099: 0, 1078: 0, 1039: 0, 983: 0, 713: 1, 519: 1, 503: 1, 501: 1, 499: 1, 497: 1, 469: 1, 431: 1, 427: 1, 407: 1, 383: 1, 379: 1, 327: 2, 319: 2, 303: 2, 275: 2, 263: 2, 247: 2, 239: 2, 235: 2, 223: 2, 215: 3, 167: 3, 159: 3, 143: 3, 127: 3}, NonTouchRanges(((1, 3), (4, 5), (8, 9), (16, 17), (32, 34), (65, 66), (97, 98), (162, 163), (259, 260), (518, 519), (551, 552), (1102, 1104))), (1, 2, 4, 8, 16, 32, 33, 65, 97, 162, 259, 518, 551, 1102, 1103), (1, 2, 4, 8, 16, 32, 33, 65, 97, 162, 259, 518, 551, 1102, 1103), (1, 2, 4, 8, 16, 32, 33, 65, 97, 162, 259, 518, 551, 1102, 1103), (1, 2, 4, 8, 16, 32, 33, 65, 97, 162, 259, 518, 551, 1102, 1103), (1, 2, 4, 8, 16, 32, 33, 65, 97, 162, 259, 518, 551, 1102, 1103), (1, 2, 4, 8, 16, 32, 33, 65, 97, 162, 259, 518, 551, 1102, 1103)), 13)
view /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part4.531-_.topdown-last_leap.test-out.txt
rm -iv /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part4.531-_.topdown-last_leap.test-out.txt
===
发现计算结果不同{只保留首条最短加链}:why?? 1097 vs 1103
    可能是:topdown:bypass:部分计算直接使用 次大数讠溟次, 而 内点集 只含 一条 最短加链 不能 涵盖所有 次大数讠溟次
    [1..=530] ==>> bottomup.last_leap[531..<1097]
    [1..=530] ==>> topdown.last_leap[531..<1103]
=>:++kw:欤只保留首条最短加链乊各次大数
    now:计算结果不同{只保留首条最短加链乊各次大数}:1335
    [1..=530] ==>> bottomup.last_leap.multi[531..<1335]
    [1..=530] ==>> topdown.last_leap.multi[531..<1335]
===
py_adhoc_call   seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌   +欤只保留首条最短加链乊各次大数  +verbose +欤最后一跃牜轻算随缘而止 --鬽最大靶值=None  +自顶向下搜索丷自底向上注册   --ver=2  --休眠期:auto      --彣匹配模板纟前置文件路径冃靶值讠简并记录:${prefix}'枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part*.bottomup.test-out.txt'   :${prefix}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part4.531-_.bottomup-last_leap-multi.test-out.txt
    [1..=530] ==>> bottomup.last_leap.multi[531..<1335]
    ^AssertionError: (乸简并记录纟递归婪溟链(1335, 14, 80, 321, ..., ..., (1, 2, 3, 5, 8, 15, 19, 37, 55, 80, 139, 223, 445, 670, 1335), (1, 2, 4, 8, 16, 32, 64, 128, 256, 320, 640, 664, 1200, 1334, 1335), (1, 2, 3, 5, 10, 15, 30, 60, 120, 240, 245, 365, 605, 730, 1335), (1, 2, 4, 8, 16, 32, 64, 128, 256, 257, 273, 529, 802, 1331, 1335), (1, 2, 3, 5, 10, 20, 40, 80, 85, 165, 330, 335, 665, 670, 1335), (1, 2, 3, 5, 10, 20, 40, 43, 83, 166, 332, 335, 667, 1334, 1335)), 13)
rm -iv /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part4.531-_.bottomup-last_leap-multi.test-out.txt

===
py_adhoc_call   seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌  +欤只保留首条最短加链乊各次大数  +verbose +欤最后一跃牜轻算随缘而止 --鬽最大靶值=None  -自顶向下搜索丷自底向上注册   --ver=2  --休眠期:auto      --彣匹配模板纟前置文件路径冃靶值讠简并记录:${prefix}'枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part*.bottomup.test-out.txt'   :${prefix}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part4.531-_.topdown-last_leap-multi.test-out.txt
    [1..=530] ==>> topdown.last_leap.multi[531..<1335]
    ^AssertionError: (乸简并记录纟递归婪溟链(1335, 14, 81, 320, ..., ..., (1, 2, 3, 5, 8, 15, 19, 37, 55, 80, 139, 223, 445, 670, 1335), (1, 2, 4, 8, 16, 32, 64, 128, 256, 320, 640, 1040, 1320, 1334, 1335), (1, 2, 3, 5, 10, 15, 30, 60, 120, 240, 245, 365, 605, 730, 1335), (1, 2, 4, 8, 16, 32, 64, 128, 256, 258, 274, 530, 804, 1334, 1335), (1, 2, 3, 5, 10, 20, 40, 80, 85, 165, 330, 335, 665, 670, 1335), (1, 2, 4, 8, 16, 32, 64, 128, 256, 258, 274, 530, 804, 1334, 1335)), 13)
===
===

===
实战:
    ===
    注意:自底向上注册.鬽最大靶值=None:内存不足
        鬽最大靶值=70000:翻倍=>基本等同于None
        加载后内存还剩740M，毛病应当出自:
            初始化构造冫靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈乊后续简并记录纟递归婪溟链牜靶值大于一扌()
            =>更改方案:自底向上注册-->自顶向下搜索
    ===
    自顶向下搜索:最后一跃:
    [1..=35035] ==>> topdown.last_leap.multi[35036..<37726]
        效果很差，本来以为能翻倍...，也许 递归婪溟链 本来就止步于此？
            => 重启计算
    ===
###自底向上注册:最后一跃:内存不足:py_adhoc_call   seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌 +欤只保留首条最短加链乊各次大数  +verbose +欤最后一跃牜轻算随缘而止 --鬽最大靶值=70000  +自顶向下搜索丷自底向上注册   --ver=2  --休眠期:auto      --彣匹配模板纟前置文件路径冃靶值讠简并记录:'script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt'     :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part0011.35036-_.bottomup-last_leap.out.txt
rm -iv script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part0011.35036-_.bottomup-last_leap.out.txt

自顶向下搜索:最后一跃:
py_adhoc_call   seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌 +欤只保留首条最短加链乊各次大数  +verbose +欤最后一跃牜轻算随缘而止 --鬽最大靶值=None  -自顶向下搜索丷自底向上注册   --ver=2  --休眠期:auto      --彣匹配模板纟前置文件路径冃靶值讠简并记录:'script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt'     :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part0011.35036-_.topdown-last_leap-multi.out.txt
    [1..=35035] ==>> topdown.last_leap.multi[35036..<37726]
    ^AssertionError: (乸简并记录纟递归婪溟链(37726, 20, 289, 1831, ..., ..., (1, 2, 3, 4, 7, 11, 19, 28, 53, 101, 127, 235, 465, 871, 1491, 2398, 4222, 7547, 11231, 18863, 37726), (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 4352, 7168, 10752, 18816, 37632, 37707, 37725, 37726), (1, 2, 3, 4, 8, 11, 19, 38, 76, 152, 304, 608, 1216, 1824, 1827, 3043, 6086, 7910, 15820, 31640, 37726), (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 4098, 4102, 4166, 8262, 16524, 33048, 37214, 37726), (1, 2, 3, 5, 7, 14, 28, 56, 112, 224, 225, 449, 898, 1796, 3592, 3816, 7632, 7639, 11231, 18863, 37726), (1, 2, 3, 6, 9, 18, 36, 72, 75, 147, 294, 588, 1176, 2352, 4704, 9408, 18816, 37632, 37707, 37725, 37726)), 19)
tail script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part0011.35036-_.topdown-last_leap-multi.out.txt
欤只保留首条最短加链乊各次大数:(37725, 19, 26, 147, FD('{:[#EnU+B-I-b-j-HX-U9-DH-It-RB-HN-gE-EA-8I-Ob-iD-Rb-GP-p7-GJ-Jt-BJ-C-1];B:[#DEf+B-IB];C:[#B15+B];}'), RT('[#B+G-B+D-B-B-B-B-B-D+C-C-D-D-D-E-C+C-G-H+C-E-B-C-E-E-K-B-N-Q-K-D-C-B-P-a+C-C-b-I-u-M+C-b-H-1-H-BA-5-s-Z-B-BH-Br-C-M-CB-Bz-BZ-s-G-D-CP-Da-c-ED-Dn-Dg-Y-h-H+C-Ee-BU-Fg-C-2-C-IE-DA-n-Dm-CA-FA-B1-I-G-KU-MZ-Bz-Y-Tc-Ig-EW-Bj-Ke-Dr-R-N-I-tU-EA-IB-YC-HN-RB-It-DH-U9-HX-j-b-H+C-I-BB-I-b-j-HX-U9-DH-It-RB-HN-YC-IB-EA-8I-Ob-iD-Rb-GP-p7-GJ-Il-BH-3-R-C-1-R]'), [1, 2, 3, 5, 9, 14, 25, 45, 70, 140, 233, 457, 914, 1165, 2285, 3889, 6300, 12575, 18900, 37725], [1, 2, 4, 8, 16, 32, 64, 96, 192, 384, 768, 784, 1568, 3136, 4704, 9408, 18816, 37632, 37707, 37725], [1, 2, 3, 5, 10, 20, 25, 45, 70, 140, 280, 560, 1120, 1165, 2285, 4570, 9140, 18280, 19445, 37725], [1, 2, 4, 8, 16, 32, 64, 65, 129, 193, 322, 515, 1030, 2060, 4120, 4249, 8369, 16738, 33476, 37725], [1, 2, 3, 6, 9, 18, 36, 72, 75, 147, 294, 588, 1176, 2352, 4704, 9408, 9417, 18825, 18900, 37725], [1, 2, 3, 6, 9, 18, 36, 72, 75, 147, 294, 588, 1176, 2352, 4704, 9408, 18816, 37632, 37707, 37725])
#rm -iv script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part0011.35036-_.topdown-last_leap-multi.out.txt

]]
[[
factor 37726
    37726: 2 13 1451
>>> bin(37726)
'0b1001001101011110'

@20260223
动因{重启计算}:
    ===
    自顶向下搜索:
    [1..=35035] ==>> topdown.last_leap.multi[35036..<37726]
        效果很差，本来以为能翻倍...，也许 递归婪溟链 本来就止步于此？
    ===
==>>:
期待失败于:37726:因为可能救场的只有两千多个点[35036..<37726]，这不太合理:见上面:求冫丮最大差值辻靶值列表厈牜两倍次大数纟右侧最小最短加链之于靶值扌
    结果未失败:侥幸通关:唯一次大数:36956@37726
    :echo 37726-36956
        770
==>>:
py_adhoc_call   seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌  --鬽最大靶值=38038  +自顶向下搜索丷自底向上注册   --ver=2  --休眠期:auto      --彣匹配模板纟前置文件路径冃靶值讠简并记录:'script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt'     :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0011.35036-38038.bottomup.out.txt
    # [:曾经主要作业命令行]:goto
    @20260223中午:启动
    @20260223八点半:..35950
    @20260224四点:..36312
    @20260224十点半:完成

du -bh script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0011.35036-38038.bottomup.out.txt
    5.4M
    # [:主要简并记录输出文件牜未打包]:goto
tail -n 313 script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0011.35036-38038.bottomup.out.txt | head -n 1
(37726, 19, 1, 21, FD('{:[#JBc+B];}'), RT('[#B+C-B-D-H-P-f-.-B.+C-D.-EA-MB-IA-YD-gE-YD-gE-CQW-Egt-MB]'), [1, 2, 4, 8, 16, 32, 64, 128, 256, 257, 513, 770, 1540, 2053, 3593, 5646, 9239, 18478, 36956, 37726], [1, 2, 4, 8, 16, 32, 64, 128, 256, 257, 513, 770, 1540, 2053, 3593, 7186, 9239, 18478, 36956, 37726], [1, 2, 4, 8, 16, 32, 64, 128, 256, 257, 513, 770, 1540, 2053, 3593, 5646, 9239, 18478, 36956, 37726], [1, 2, 4, 8, 16, 32, 64, 128, 256, 257, 513, 770, 1540, 2053, 3593, 7186, 9239, 18478, 36956, 37726], [1, 2, 4, 8, 16, 32, 64, 128, 256, 257, 513, 770, 1540, 2053, 3593, 5646, 9239, 18478, 36956, 37726], [1, 2, 4, 8, 16, 32, 64, 128, 256, 257, 513, 770, 1540, 2053, 3593, 7186, 9239, 18478, 36956, 37726])
===

===
]]
[[
[#结果未失败#:]期待失败于:37726:因为可能救场的只有两千多个点[35036..<37726]，这不太合理:见上面:求冫丮最大差值辻靶值列表厈牜两倍次大数纟右侧最小最短加链之于靶值扌
    若是出现 首败点，也许可以考虑进一步泛化:[支线由 (内点*2**ez)-->(内点*靶值牜最小显链长可自二进制拆分)]
        虽然 靶值牜二幂或三 的 最短加链唯一，但 作为 支线 删除其他可能，也并非不可接受，只是 简并态 更大 能走得更远
        重点在于 重复使用的兼容性，不同靶值 共享 同一套 溟化值集，但是 出现许多 介点，如何 兼容？或者同样强行指定一个 介点集，还是 有点麻烦，感觉不太行
    加星链牜递归最短--泛化->婪溟链牜递归最短--泛化->婪泝链牜递归最短
    ,泝:6751:氵:8:44133124:iryy:su:sù:泝sù/同“溯”。
    ,溟:7191:氵:13:4414525114134:ipju:ming:míng:溟míng/〔溟溟〕ａ．形容潮湿、潮润；ｂ．形容昏暗。/海：东溟。“北溟有鱼，其名为鲲”。

靶值牜最小显链长可自二进制拆分 有哪些？

]]
[[
@20260224
再来一次:le35035-->le38038
自顶向下搜索:最后一跃:
py_adhoc_call   seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌 +欤只保留首条最短加链乊各次大数  +verbose +欤最后一跃牜轻算随缘而止 --鬽最大靶值=None  -自顶向下搜索丷自底向上注册   --ver=2  --休眠期:auto      --彣匹配模板纟前置文件路径冃靶值讠简并记录:'script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt'     :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part0012.38039-_.topdown-last_leap-multi.out.txt
    [1..=38038] ==>> topdown.last_leap.multi[38039..<50215]
    ^AssertionError: (乸简并记录纟递归婪溟链(50215, 20, 146, 769, ..., ..., (1, 2, 3, 5, 7, 13, 23, 39, 55, 95, 190, 295, 390, 780, 1557, 3015, 5023, 10043, 16741, 25112, 50215), (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 8320, 16640, 33280, 50176, 50210, 50214, 50215), (1, 2, 3, 5, 7, 14, 28, 56, 112, 224, 448, 896, 1792, 1795, 3587, 7174, 14348, 16140, 19727, 34075, 50215), (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 8193, 16385, 16897, 16901, 33286, 33318, 50215), (1, 2, 3, 6, 12, 24, 25, 49, 98, 196, 392, 784, 1568, 3136, 6272, 12544, 12556, 12559, 25103, 25112, 50215), (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 1026, 2050, 3074, 6148, 12296, 24592, 25618, 50210, 50214, 50215)), 19)
tail script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part0012.38039-_.topdown-last_leap-multi.out.txt
欤只保留首条最短加链乊各次大数:(50214, 19, 36, 188, FD('{:[#GIT+B-B+C-M+C-B-BP-v-CP-Bf-B8-C-M-Bf0-X7-E-K-e-CA-EB-BN-F-J-v3-DAJ-M8-Bf-C-.-Z-B];B:[#EFi+B-ID-Cn-BgD];I:[#Em+B];}'), RT('[#B+E-B-B-D-D+C-G+C-G+D-N+C-O+D-d-B+C-c+D-9-C+C-B-5-B-B+C-g-BZ-C-C-B-B3+C-B+C-E-8-C5-F-C-C-C+D-C3-2+D-D-L-Hu-E-C-F-I-C-E+C-He-B-J-X-Hd-H.-J-F-L-R-F-J-B-O9+C-B-U-v-g-Oa-P.-T-L-X-j-L-T+C-C-GA-X7-E-C-m-CA-BP-cG-f.-n-X-v-BH-X-n+C-G-C-F-L4-v3-H-B-F-BN-Ch-Bf-CA-e-K-E-FT-Cn-P.-BQD-Pw-M-C+C-O-8-v-Bf-CP-v-v-f-B+D-L+C-B-B+C-M+C-B-BP-v-CP-v-v-B7+C-C-M-Pw-BQD-Pr-P-D-Cn-FD-P-E-K-e-CA-EB-BN-F-J-v3-C.p-f-LZ-Bi-Bf-C-.-Z-B-D]'), [1, 2, 3, 6, 12, 17, 25, 49, 98, 195, 261, 390, 777, 1545, 3090, 4201, 8369, 12555, 25107, 50214], [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 4097, 8193, 16386, 32772, 49920, 50210, 50214], [1, 2, 3, 6, 12, 24, 25, 49, 98, 196, 392, 784, 785, 1569, 3138, 6276, 12552, 12555, 25107, 50214], [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 4097, 8193, 16386, 32772, 49158, 50182, 50214], [1, 2, 3, 6, 12, 24, 25, 49, 98, 196, 392, 784, 785, 1569, 3138, 6276, 12552, 12555, 25107, 50214], [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 1026, 2050, 3074, 6148, 12296, 24592, 25618, 50210, 50214])

mv -iv script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part0012.38039-_.topdown-last_leap-multi.out.txt script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part0012.38039-_lt50215首败点.topdown-last_leap-multi.out.txt
du -bh script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part0012.38039-_lt50215首败点.topdown-last_leap-multi.out.txt
    17M
]]
[[
@20260225:
++kw:欤允许缺失乊最后一跃#乸异常牜最小显链长,乸失败记录
###py_adhoc_call   seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain   @_test乸异常牜最小显链长
###py_adhoc_call   seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain   @_test乸失败记录
===
prefixT=/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2
===
测试:kw:欤允许缺失乊最后一跃
py_adhoc_call   seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌  +欤允许追附乊最后一跃 +欤允许缺失乊最后一跃 +欤只保留首条最短加链乊各次大数  +verbose +欤最后一跃牜轻算随缘而止 --鬽最大靶值=2002  -自顶向下搜索丷自底向上注册   --ver=2  --休眠期:auto      --彣匹配模板纟前置文件路径冃靶值讠简并记录:${prefixT}'.part*.bottomup.test-out.txt:|:'${prefixT}.asis-part4.531-_.topdown-last_leap-multi.test-out.txt   :${prefixT}.asis-part5-as-part4-2.1335-2002.topdown-last_leap-multi-miss_ok.test-out.txt
rm -iv /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part5-as-part4-2.1335-2002.topdown-last_leap-multi-miss_ok.test-out.txt
head -n 1 /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part5-as-part4-2.1335-2002.topdown-last_leap-multi-miss_ok.test-out.txt
grep "^('fail:', "  /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part5-as-part4-2.1335-2002.topdown-last_leap-multi-miss_ok.test-out.txt | lineno
    失败记录:共:13
===
xxx:测试:kw:欤只保留后半段数据乊最后一跃乊自顶向下
    发现无法实现
xxx:fmts4prepaths_le2002=${prefixT}'.part*.bottomup.test-out.txt:|:'"${prefixT}.asis-part4.531-_.topdown-last_leap-multi.test-out.txt:|:${prefixT}.asis-part5-as-part4-2.1335-2002.topdown-last_leap-multi-miss_ok.test-out.txt"
xxx:py_adhoc_call   seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌 +欤只保留后半段数据乊最后一跃乊自顶向下 +欤允许追附乊最后一跃 +欤允许缺失乊最后一跃 +欤只保留首条最短加链乊各次大数  +verbose +欤最后一跃牜轻算随缘而止 --鬽最大靶值=2022  -自顶向下搜索丷自底向上注册   --ver=2  --休眠期:auto      --彣匹配模板纟前置文件路径冃靶值讠简并记录:"${fmts4prepaths_le2002}"  :${prefixT}.asis-part6-as-part4-3.2003-2022.topdown-last_leap-multi-miss_ok-drop_half.test-out.txt
===
测试:kw:鬽最大靶值纟留空数据段纟最后一跃乊自顶向下
fmts4prepaths_lt1335=${prefixT}'.part*.bottomup.test-out.txt:|:'"${prefixT}.asis-part4.531-_.topdown-last_leap-multi.test-out.txt"
py_adhoc_call   seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌 --鬽最大靶值纟留空数据段纟最后一跃乊自顶向下=2002 +欤允许追附乊最后一跃 +欤允许缺失乊最后一跃 +欤只保留首条最短加链乊各次大数  +verbose +欤最后一跃牜轻算随缘而止 --鬽最大靶值=2022  -自顶向下搜索丷自底向上注册   --ver=2  --休眠期:auto      --彣匹配模板纟前置文件路径冃靶值讠简并记录:"${fmts4prepaths_lt1335}"  :${prefixT}.asis-part6-as-part4-3.2003-2022.topdown-last_leap-multi-miss_ok-skip_holes.test-out.txt
    ^Exception: ('次大数讠溟次 empty @靶值=', 2003)
py_adhoc_call   seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌  --鬽最大靶值纟留空数据段纟最后一跃乊自顶向下=1366 +欤允许追附乊最后一跃 +欤允许缺失乊最后一跃 +欤只保留首条最短加链乊各次大数  +verbose +欤最后一跃牜轻算随缘而止 --鬽最大靶值=1400  -自顶向下搜索丷自底向上注册   --ver=2  --休眠期:auto      --彣匹配模板纟前置文件路径冃靶值讠简并记录:${prefixT}'.part*.bottomup.test-out.txt:|:'${prefixT}.asis-part4.531-_.topdown-last_leap-multi.test-out.txt   :${prefixT}.asis-part5-as-part4-z.1367-1400.topdown-last_leap-multi-miss_ok-skip_holes.test-out.txt
view /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part5-as-part4-z.1367-1400.topdown-last_leap-multi-miss_ok-skip_holes.test-out.txt
===
再再来一次:le38038++le50214
自顶向下搜索:最后一跃:+欤允许缺失乊最后一跃
prefixL=script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2
py_adhoc_call   seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌 +欤只保留后半段数据乊最后一跃乊自顶向下 +欤允许追附乊最后一跃 +欤允许缺失乊最后一跃 +欤只保留首条最短加链乊各次大数  +verbose +欤最后一跃牜轻算随缘而止 --鬽最大靶值=70070  -自顶向下搜索丷自底向上注册   --ver=2  --休眠期:auto      --彣匹配模板纟前置文件路径冃靶值讠简并记录:"${prefixL}"'.part00*.out.txt:|:'"${prefixL}".asis-part0012.38039-_lt50215首败点.topdown-last_leap-multi.out.txt    :"${prefixL}".asis-part0013-as-12-2.50215-70070.topdown-last_leap-multi-miss_ok.out.txt
    崩溃两次:似乎因为 内存不足
    => ++kw:欤只保留后半段数据乊最后一跃乊自顶向下
###rm -iv script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part0013-as-12-2.50215-70070.topdown-last_leap-multi-miss_ok.out.txt
mv -iv script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part0013-as-12-2.50215-70070.topdown-last_leap-multi-miss_ok.out.txt script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part0013-as-12-2.50215-62001.topdown-last_leap-multi-miss_ok.out.txt
tail -n 1 script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part0013-as-12-2.50215-62001.topdown-last_leap-multi-miss_ok.out.txt
    (62001, 19, 4, 43, FD('{:[#Hkx+B-Dn-CgH];B:[#FIR+B];}'), RT('[#B+E-B-B-D-D-H-H-P+C-O-I-v-G-Bx-N-Dj-b+C-D.-DG-E4-KO-Jx-UA-c-Tj-oB-5-nH-BQD-Bz-BOP-IA-CYG-Dn-w-Dn-CYG-IA-FAP]'), [1, 2, 3, 6, 12, 24, 48, 49, 73, 121, 242, 484, 968, 1936, 3843, 7686, 15372, 21009, 31025, 62001], [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 513, 769, 1281, 2562, 5124, 10248, 20496, 30976, 41505, 62001], [1, 2, 3, 6, 12, 24, 48, 49, 73, 121, 242, 484, 968, 1936, 3872, 7744, 15488, 30976, 31025, 62001], [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 513, 769, 1281, 2562, 5124, 10248, 20496, 21009, 41505, 62001], [1, 2, 3, 6, 12, 24, 48, 49, 73, 121, 242, 484, 968, 1936, 3872, 7744, 15488, 30976, 31025, 62001], [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 513, 769, 1281, 2562, 5124, 10248, 20496, 21009, 41505, 62001])
grep "^('fail:', "  script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part0013-as-12-2.50215-62001.topdown-last_leap-multi-miss_ok.out.txt > /sdcard/0my_files/tmp/-0tmp
view /sdcard/0my_files/tmp/-0tmp
    失败记录:共:1:[50215]@[50215..=62001]

===
再再再来一次:le38038++le50214
自顶向下搜索:最后一跃:+欤允许缺失乊最后一跃,--鬽最大靶值纟留空数据段纟最后一跃乊自顶向下
prefixL=script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2
py_adhoc_call   seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌  --鬽最大靶值纟留空数据段纟最后一跃乊自顶向下=62001  +欤允许追附乊最后一跃 +欤允许缺失乊最后一跃 +欤只保留首条最短加链乊各次大数  +verbose +欤最后一跃牜轻算随缘而止 --鬽最大靶值=70070  -自顶向下搜索丷自底向上注册   --ver=2  --休眠期:auto      --彣匹配模板纟前置文件路径冃靶值讠简并记录:"${prefixL}"'.part00*.out.txt:|:'"${prefixL}".asis-part0012.38039-_lt50215首败点.topdown-last_leap-multi.out.txt    :"${prefixL}".asis-part0014-as-12-3.62002-70070.topdown-last_leap-multi-miss_ok-skip_holes.out.txt
grep "^('fail:', "  script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part0014-as-12-3.62002-70070.topdown-last_leap-multi-miss_ok-skip_holes.out.txt
    失败记录:共:0:[]@[62002..=70070]
===
也就是说:最后一跃 一共只遭遇 两痛点:[37726,50215]@[35035..=70070]
    但是 37726次大数36956 已被涵盖:le38038
也就是说:还剩:单痛点:[50215]@[50215..=70070]
    取消:TODO:网页版计算最短加链，再尝试转换为 婪溟链#rewrite3
        !! 已得:加星链牜递归最短
            #50215次大数38942:差一点点就被涵盖le38038
        <<==:
py_adhoc_call   seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest   ,枚举冫加星链牜递归最短巛靶值扌 =50215  +欤次大数降序
    (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 1025, 2050, 3075, 4099, 8198, 11273, 19471, 38942, 50215)
        唯一！
py_adhoc_call   seed.math.power.addition_chain.shortest.rewrite3   @严序加链讠最短缩写文本纟递归婪溟链扌 --fmt_case:dnzw_str  ='(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 1025, 2050, 3075, 4099, 8198, 11273, 19471, 38942, 50215)'
    '[-^10-^1-2^10--2-1--2]'
===
du -bh script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part0012.38039-_lt50215首败点.topdown-last_leap-multi.out.txt
    17M#止步原由:首败点#=>+miss_ok
du -bh script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part0013-as-12-2.50215-62001.topdown-last_leap-multi-miss_ok.out.txt
    18M#止步原由:内存不足#=>+skip_holes
du -bh script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part0014-as-12-3.62002-70070.topdown-last_leap-multi-miss_ok-skip_holes.out.txt
    11M#止步原由:手动设定上限{避免miss_ok导致无限多缺失}

mkdir /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/txt-asis/
ls script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part00*.out.txt
    排除asis-part0011:因为已有part0011{35036-38038}
ls script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part001{2,3-as-12-2,4-as-12-3}.*.out.txt
cp -iv -u -t /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/txt-asis/  script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part001{2,3-as-12-2,4-as-12-3}.*.out.txt
    # [:主要数据备份命令牜最后一跃]:here
===
最后一跃=>实非左侧最大
py_adhoc_call   seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain   @另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌 +欤允许缺失乊最后一跃 --ver=2  -verbose  :/sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/extract/mixed_recursive_greedy_zpow_addition_chain..另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌.38039-70070.miss-50215.实非左侧最大.extract-out.txt  $(printf ' :%s' script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part001{2,3-as-12-2,4-as-12-3}.*.out.txt)
tail -n 1 /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/extract/mixed_recursive_greedy_zpow_addition_chain..另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌.38039-70070.miss-50215.实非左侧最大.extract-out.txt

[-^12-1^12--^1-4^10-5^5]
    (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 4097, 8193, 16386, 32772, 49158, 50182, 50214)

50215
###{代码出错后修补用命令行:}:py_adhoc_call   seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain   @另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌 +欤追附 +欤允许缺失乊最后一跃 --ver=2  -verbose  :/sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/extract/mixed_recursive_greedy_zpow_addition_chain..另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌.38039-70070.miss-50215.实非左侧最大.extract-out.txt  $(printf ' :%s' script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part001{3-as-12-2,4-as-12-3}.*.out.txt)
:echo 70070-38038
    32032行
wc -l /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/extract/mixed_recursive_greedy_zpow_addition_chain..另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌.38039-70070.miss-50215.实非左侧最大.extract-out.txt
    32032
du -bh /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/extract/mixed_recursive_greedy_zpow_addition_chain..另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌.38039-70070.miss-50215.实非左侧最大.extract-out.txt
    839K
head -n 12177 /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/extract/mixed_recursive_greedy_zpow_addition_chain..另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌.38039-70070.miss-50215.实非左侧最大.extract-out.txt | tail -n 2
    [-^12-1^12--^1-4^10-5^5]   #50214
    -50215
tar -cvf /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/tar/mixed_recursive_greedy_zpow_addition_chain..另档冫婪溟链牜递归最短牜任意讠址距溟次形式扌.38039-70070.miss-50215.extract-out.txt.tar.lzma --lzma -C  /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/extract/  mixed_recursive_greedy_zpow_addition_chain..另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌.38039-70070.miss-50215.实非左侧最大.extract-out.txt
tar -tf /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/tar/mixed_recursive_greedy_zpow_addition_chain..另档冫婪溟链牜递归最短牜任意讠址距溟次形式扌.38039-70070.miss-50215.extract-out.txt.tar.lzma
tar -xf /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/tar/mixed_recursive_greedy_zpow_addition_chain..另档冫婪溟链牜递归最短牜任意讠址距溟次形式扌.38039-70070.miss-50215.extract-out.txt.tar.lzma -O | more
du -bh /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/tar/mixed_recursive_greedy_zpow_addition_chain..另档冫婪溟链牜递归最短牜任意讠址距溟次形式扌.38039-70070.miss-50215.extract-out.txt.tar.lzma
    128K
    # 废弃:[:主要任意婪溟链牜递归最短牜有缺失另档文件]:here
    #   格式纟缺失行:『-靶值』
    #   缺失:『-50215』:补全:[-^10-^1-2^10--2-1--2]
    # TODO:已有一路无缺失:[1..=39363][39364..=63795][63796..=65564]

echo $'aaa\nbbb\nccc' | sed -e 's/bbb/ddd/'
echo $'aaa\n-50215\nccc' | sed -e 's/^-50215$/[-^10-^1-2^10--2-1--2]/'
#sed -e 's/^-50215$/[-^10-^1-2^10--2-1--2]/' < /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/extract/mixed_recursive_greedy_zpow_addition_chain..另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌.38039-70070.miss-50215.实非左侧最大.extract-out.txt >> /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/extract/mixed_recursive_greedy_zpow_addition_chain..另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌.38039-70070.patch-50215.实非左侧最大.extract-out.txt
du -bh /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/extract/mixed_recursive_greedy_zpow_addition_chain..另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌.38039-70070.patch-50215.实非左侧最大.extract-out.txt
    839K
head -n 12177 /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/extract/mixed_recursive_greedy_zpow_addition_chain..另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌.38039-70070.patch-50215.实非左侧最大.extract-out.txt | tail -n 2
    [-^12-1^12--^1-4^10-5^5]
    [-^10-^1-2^10--2-1--2]

tar -cvf /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/tar/mixed_recursive_greedy_zpow_addition_chain..另档冫婪溟链牜递归最短牜任意讠址距溟次形式扌.38039-70070.patch-50215.extract-out.txt.tar.lzma --lzma -C  /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/extract/  mixed_recursive_greedy_zpow_addition_chain..另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌.38039-70070.patch-50215.实非左侧最大.extract-out.txt
tar -tf /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/tar/mixed_recursive_greedy_zpow_addition_chain..另档冫婪溟链牜递归最短牜任意讠址距溟次形式扌.38039-70070.patch-50215.extract-out.txt.tar.lzma
tar -xf /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/tar/mixed_recursive_greedy_zpow_addition_chain..另档冫婪溟链牜递归最短牜任意讠址距溟次形式扌.38039-70070.patch-50215.extract-out.txt.tar.lzma -O | more
tar -xf /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/tar/mixed_recursive_greedy_zpow_addition_chain..另档冫婪溟链牜递归最短牜任意讠址距溟次形式扌.38039-70070.patch-50215.extract-out.txt.tar.lzma -O | head -n 12178 | tail -n 3
    [-^12-1^12--^1-4^10-5^5]
    [-^10-^1-2^10--2-1--2]
    [----------^5-7-6-3^5-3]
du -bh /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/tar/mixed_recursive_greedy_zpow_addition_chain..另档冫婪溟链牜递归最短牜任意讠址距溟次形式扌.38039-70070.patch-50215.extract-out.txt.tar.lzma
    128K
cp -iv /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/tar/mixed_recursive_greedy_zpow_addition_chain..另档冫婪溟链牜递归最短牜任意讠址距溟次形式扌.38039-70070.patch-50215.extract-out.txt.tar.lzma ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain__arbitrary_recur_shortest_stem.py..址距溟次形式纟任意纟递归婪溟链.ge38039.le70070.txt.tar.lzma
    # [:主要任意婪溟链牜递归最短另档文件]:here
    #old:vs: ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain__max_recur_shortest_stem.py..址距溟次形式纟左侧最大纟递归婪溟链.le35035.txt.tar.lzma
    #vs: ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain__max_recur_shortest_stem.py..址距溟次形式纟左侧最大纟递归婪溟链.le39363.txt.tar.lzma




DONE:
e ../../python3_src/seed/math/power/addition_chain/data/get_target_uint2may_optimal_addition_chain7arbitrary_recur_shortest_stem_.py
    e ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain__arbitrary_recur_shortest_stem.py
from seed.math.power.addition_chain.data.get_target_uint2may_optimal_addition_chain7arbitrary_recur_shortest_stem_ import 取冫靶值讠婪溟链牜递归最短牜任意扌, 靶值讠婪溟链牜递归最短牜任意扌
    参考:
        view ../../python3_src/seed/math/power/addition_chain/data/get_target_uint2may_optimal_addition_chain7max_recur_shortest_stem_.py
            view ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain__max_recur_shortest_stem.py
        # 前半段:
        from nn_ns.math_nn.numbers.shortest_addition_chain__max_recur_shortest_stem import 取冫靶值讠婪溟链牜递归最短牜左侧最大扌
===
]]
[[
改回:自顶向下搜索:以降低内存开销
py_adhoc_call   seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌  --鬽最大靶值=39363  -自顶向下搜索丷自底向上注册 +verbose  --ver=2  --休眠期:auto      --彣匹配模板纟前置文件路径冃靶值讠简并记录:'script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt'     :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0012.38039-39363.topdown.out.txt
    # [:曾经主要作业命令行]:goto
    @20260225黄昏:启动
    @20260226下午:完成
!! 50215次大数38942
=>part0012.38039-41041-->part0012.38039-39363
mv -iv script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0012.38039-41041.topdown.out.txt  script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0012.38039-39363.topdown.out.txt
tail -n 1 script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0012.38039-39363.topdown.out.txt
du -bh script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0012.38039-39363.topdown.out.txt
    2.4M
    # [:主要简并记录输出文件牜未打包]:here
===
#py_adhoc_call   seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌 +欤只保留首条最短加链乊各次大数  +verbose +欤最后一跃牜轻算随缘而止 --鬽最大靶值=None  -自顶向下搜索丷自底向上注册   --ver=2  --休眠期:auto      --彣匹配模板纟前置文件路径冃靶值讠简并记录:'script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt'     :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part0013.39364-_.topdown-last_leap-multi.out.txt
    # [:曾经主要作业命令行]:goto
    启动，运行直至内存不足崩溃:[..=63795]
tail -n 1 script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part0013.39364-_.topdown-last_leap-multi.out.txt
mv -iv script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part0013.39364-_.topdown-last_leap-multi.out.txt script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part0013.39364-63795.topdown-last_leap-multi.out.txt
du -bh script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part0013.39364-63795.topdown-last_leap-multi.out.txt
    35M#止步原由:内存不足#=>+skip_holes

===
prefixL=script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2
#py_adhoc_call   seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌   --鬽最大靶值纟留空数据段纟最后一跃乊自顶向下=63795  +欤允许追附乊最后一跃 +欤只保留首条最短加链乊各次大数  +verbose +欤最后一跃牜轻算随缘而止 --鬽最大靶值=None  -自顶向下搜索丷自底向上注册   --ver=2  --休眠期:auto      --彣匹配模板纟前置文件路径冃靶值讠简并记录:"${prefixL}".part00*.out.txt    :"${prefixL}".asis-part0014-as-13-2.63796-_.topdown-last_leap-multi-skip_holes.out.txt
    #空洞:不含: ':|:'"${prefixL}".asis-part0013.39364-63795.topdown-last_leap-multi.out.txt
    ^乸异常牜最小显链长: 乸失败记录(乸简并记录纟递归婪溟链(65565, 20, 48, 334, ..., ..., (1, 2, 3, 5, 7, 14, 21, 29, 32, 64, 128, 256, 510, 1020, 2016, 3645, 6558, 10930, 21855, 32784, 65565), (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 65552, 65560, 65564, 65565), (1, 2, 3, 5, 7, 14, 28, 56, 112, 224, 231, 455, 910, 1820, 3640, 3645, 7285, 14570, 29140, 36425, 65565), (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 65552, 65560, 65564, 65565), (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 16392, 16393, 16397, 32781, 32784, 65565), (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 65552, 65560, 65564, 65565)), 19)
    # [:曾经主要作业命令行]:goto
tail -n 1 script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part0014-as-13-2.63796-_.topdown-last_leap-multi-skip_holes.out.txt
    65564
mv -iv script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part0014-as-13-2.63796-_.topdown-last_leap-multi-skip_holes.out.txt script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part0014-as-13-2.63796-65564.topdown-last_leap-multi-skip_holes.out.txt
du -bh script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part0014-as-13-2.63796-65564.topdown-last_leap-multi-skip_holes.out.txt
    2.5M#止步原由:空洞过大，要是填上 整个四万段 应该能走得更远#vs:此前另一条路:设定上限而止步于70070
>>> bin(65564)
'0b10000000000011100'
>>> 65564-2**16
28


mkdir /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/txt-asis-2/
ls script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part001{3,4-as-13-2}.*.out.txt
cp -iv -u -t /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/txt-asis-2/  script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.asis-part001{3,4-as-13-2}.*.out.txt
    # [:主要数据备份命令牜最后一跃]:goto

]]
[[
===
另档:尾六表
prefixZ=/sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/
infixI=min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..
infixO=mixed_recursive_greedy_zpow_addition_chain..
printf ' :%s\n' ${prefixZ}txt/${infixI}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt
printf ' :%s\n' ${prefixZ}txt/${infixI}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00{11,12}.*.out.txt
#py_adhoc_call   seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain   @另档冫尾六表纟简并记录纟递归婪溟链扌  --ver=2  -verbose  :${prefixZ}extract/${infixO}另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-01-12.1-39363.extract-out.txt    $(printf ' :%s\n' ${prefixZ}txt/${infixI}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt)
py_adhoc_call   seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain   @另档冫尾六表纟简并记录纟递归婪溟链扌  --ver=2  -verbose  :${prefixZ}extract/${infixO}另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-11-12.35036-39363.extract-out.txt    $(printf ' :%s\n' ${prefixZ}txt/${infixI}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00{11,12}.*.out.txt)
du -bh /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/extract/mixed_recursive_greedy_zpow_addition_chain..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-11-12.35036-39363.extract-out.txt
    2.6M
wc -l /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/extract/mixed_recursive_greedy_zpow_addition_chain..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-11-12.35036-39363.extract-out.txt
    4328行
tar -cvf /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/tar/mixed_recursive_greedy_zpow_addition_chain..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-11-12.35036-39363.extract-out.txt.tar.lzma --lzma  -C /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/extract/    mixed_recursive_greedy_zpow_addition_chain..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-11-12.35036-39363.extract-out.txt
tar -tf /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/tar/mixed_recursive_greedy_zpow_addition_chain..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-11-12.35036-39363.extract-out.txt.tar.lzma
tar -xf /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/tar/mixed_recursive_greedy_zpow_addition_chain..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-11-12.35036-39363.extract-out.txt.tar.lzma -O | more
du -bh /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/tar/mixed_recursive_greedy_zpow_addition_chain..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-11-12.35036-39363.extract-out.txt.tar.lzma
    236K
    # [:主要尾六表另档文件]:here
cp -iv /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/tar/mixed_recursive_greedy_zpow_addition_chain..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-11-12.35036-39363.extract-out.txt.tar.lzma  ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain__six_lists.py..尾六表纟简并记录纟递归婪溟链.ver2.ge35036.le39363.txt.tar.lzma
e ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain__six_lists.py

===
#py_adhoc_call   seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain   @另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌  --ver=2  -verbose  :/sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/extract/mixed_recursive_greedy_zpow_addition_chain..另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌.1-39363.extract-out.txt    $(printf ' :%s' script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt)
py_adhoc_call   seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain   @另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌  --ver=2  -verbose  :/sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/extract/mixed_recursive_greedy_zpow_addition_chain..另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌.35036-39363.extract-out.txt    :/sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/extract/mixed_recursive_greedy_zpow_addition_chain..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-11-12.35036-39363.extract-out.txt
#rm -iv /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/extract/mixed_recursive_greedy_zpow_addition_chain..另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌.35036-39363.extract-out.txt
du -bh /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/extract/mixed_recursive_greedy_zpow_addition_chain..另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌.35036-39363.extract-out.txt
    104K
wc -l /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/extract/mixed_recursive_greedy_zpow_addition_chain..另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌.35036-39363.extract-out.txt
    4328行

ls /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/extract/mixed_recursive_greedy_zpow_addition_chain..另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌.*
#cat  /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/extract/mixed_recursive_greedy_zpow_addition_chain..另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌.1-35035.extract-out.txt  /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/extract/mixed_recursive_greedy_zpow_addition_chain..另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌.35036-39363.extract-out.txt  >  /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/extract/mixed_recursive_greedy_zpow_addition_chain..另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌.1-39363.extract-out.txt
du -bh /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/extract/mixed_recursive_greedy_zpow_addition_chain..另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌.1-39363.extract-out.txt
    858K
wc -l /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/extract/mixed_recursive_greedy_zpow_addition_chain..另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌.1-39363.extract-out.txt
    39363行

tar -cvf /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/tar/mixed_recursive_greedy_zpow_addition_chain..另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌.1-39363.extract-out.txt.tar.lzma --lzma -C  /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/extract/  mixed_recursive_greedy_zpow_addition_chain..另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌.1-39363.extract-out.txt
tar -xf /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/tar/mixed_recursive_greedy_zpow_addition_chain..另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌.1-39363.extract-out.txt.tar.lzma -O | more

du -bh /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/tar/mixed_recursive_greedy_zpow_addition_chain..另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌.1-39363.extract-out.txt.tar.lzma
    114K
cp -iv /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/tar/mixed_recursive_greedy_zpow_addition_chain..另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌.1-39363.extract-out.txt.tar.lzma   ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain__max_recur_shortest_stem.py..址距溟次形式纟左侧最大纟递归婪溟链.le39363.txt.tar.lzma
    # [:主要左侧最大另档文件]:here
e ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain__max_recur_shortest_stem.py
===


]]
[[
#过气{加星链牜递归最短:单点搜索}:py_adhoc_call   seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest   ,枚举生成冫文件冃靶值讠鬽首尾加星链牜递归最短扌   --休眠期:auto :/sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠鬽首尾加星链牜递归最短扌.out.txt
    @20260225晚九点半:启动
view /sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠鬽首尾加星链牜递归最短扌.out.txt

#最新版:{加星链牜递归最短:次大数}:
prefixAB=/sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌
py_adhoc_call   seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest   ,枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌 +欤询问中止乊靶值牜无加星链牜递归最短  --ver=2 --鬽最大靶值=None  --休眠期:auto :"${prefixAB}".-0.out.txt :"${prefixAB}".-1.ver2.out.txt
    # [:当前主要作业命令行]:here
    # [:额外生成数据]:here
    命令结束:见:
view ../../python3_src/seed/math/power/addition_chain/shortest/search_star_chain7recursive_shortest.py
ls /sdcard/0my_files/zip/addition_chain/靶值讠允空升列纟次大数纟加星链牜递归最短
    靶值讠允空升列纟次大数纟加星链牜递归最短.le74174.txt.txz
    靶值讠允空次大数讠首尾加星链牜递归最短.le74174.txt.txz
    @20260311:通过万维网得到末尾三个空缺靶值的最短加链，已然可以拼凑出来le74174的所有靶值的某条婪溟链牜递归最短


泛化版{婪溟链牜递归最短:次大数}:编辑中...:
发现病蛊:e ../../python3_src/seed/math/power/addition_chain/shortest/search_greedy_zpow_chain7recursive_shortest.py
    停滞:[内点:<-简并态{次大数}]但未必是 主干值
]]
[[
@20260309
tree /sdcard/0my_files/zip/addition_chain/
ls /sdcard/0my_files/zip/addition_chain/
    偏移值文本冃靶值讠最小显链长.le131157856.txt.txz
    偏移值文本冃靶值讠最小显链长.le7320000.txt.txz
    靶值讠允空升列纟次大数纟加星链牜递归最短
    靶值讠简并记录纟递归婪溟链
ls /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链
    extract
    tar
    txt
    txt-asis
    txt-asis-2
ls /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/tar
ls /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/txt


:r !ls /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/txt
:.+1,.+12s/^min_.*\([.]ver2[.].*[.]\)out[.]txt/\1
    min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌{.???.}out.txt
.ver2.part0001.1-6017.
.ver2.part0002.6018-9192.
.ver2.part0003.9193-13013.bottomup.
.ver2.part0004.13014-16016.bottomup.
.ver2.part0005.16017-20020.bottomup.
.ver2.part0006.20021-23023.bottomup.
.ver2.part0007.23024-26026.bottomup.
.ver2.part0008.26027-29029.bottomup.
.ver2.part0009.29030-32032.bottomup.
.ver2.part0010.32033-35035.bottomup.
.ver2.part0011.35036-38038.bottomup.
.ver2.part0012.38039-39363.topdown.
-->:
    靶值讠简并记录纟递归婪溟链{.???.}txt.txz
.v2p01.1-6017.
.v2p02.6018-9192.
.v2p03.9193-13013.
.v2p04.13014-16016.
.v2p05.16017-20020.
.v2p06.20021-23023.
.v2p07.23024-26026.
.v2p08.26027-29029.
.v2p09.29030-32032.
.v2p10.32033-35035.
.v2p11.35036-38038.
.v2p12.38039-39363.


==>>:
mkdir /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/tar-12parts/
rt_dir=/sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/
f(){ txz $rt_dir/tar-12parts/靶值讠简并记录纟递归婪溟链${1}txt.txz   $rt_dir/txt/  -ipaths  $rt_dir/txt/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌${2}out.txt ; }
f  .v2p01.1-6017.         .ver2.part0001.1-6017.
f  .v2p02.6018-9192.      .ver2.part0002.6018-9192.
f  .v2p03.9193-13013.     .ver2.part0003.9193-13013.bottomup.
f  .v2p04.13014-16016.    .ver2.part0004.13014-16016.bottomup.
f  .v2p05.16017-20020.    .ver2.part0005.16017-20020.bottomup.
f  .v2p06.20021-23023.    .ver2.part0006.20021-23023.bottomup.
f  .v2p07.23024-26026.    .ver2.part0007.23024-26026.bottomup.
f  .v2p08.26027-29029.    .ver2.part0008.26027-29029.bottomup.
f  .v2p09.29030-32032.    .ver2.part0009.29030-32032.bottomup.
f  .v2p10.32033-35035.    .ver2.part0010.32033-35035.bottomup.
f  .v2p11.35036-38038.    .ver2.part0011.35036-38038.bottomup.
f  .v2p12.38039-39363.    .ver2.part0012.38039-39363.topdown.

==>>:
ls /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/tar-12parts/
:r !du -ch /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/tar-12parts/*
    1.0M
    0.9M
    1.2M
    1.1M
    1.8M
    1.1M
    1.2M
    1.4M
    1.8M
    1.6M
    1.4M
    676K
    ==>>:
    16M
    # [:主要数据备份牜逐个文件打包]:here

]]




















from seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain import *
]]]'''#'''

