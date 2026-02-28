#__all__:goto
#TODO:乸匴前缀无效判定器纟最短加链牜提前排除乘环殿后牜强制乘环次序牜强制可交换步次序
#    仔细想想，还是很慢，因为 失败的话 乘环的所有中间态 都得遍历一遍，考虑一开始就用 倍数 替代 乘环，也就是 直接 搜索 虚匏链(类似 骨架，只是 保留值 而非 倍数)。
#    move_to:e ../../python3_src/seed/math/power/addition_chain/shortest/search7contracted_chain.py
r'''[[[
e ../../python3_src/seed/math/power/addition_chain/shortest/search.py

seed.math.power.addition_chain.shortest.search
py -m nn_ns.app.debug_cmd   seed.math.power.addition_chain.shortest.search -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.power.addition_chain.shortest.search:__doc__ -ht # -ff -df
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.math.power.addition_chain.shortest.search:cls@T    =T   +exclude_attrs5listed_in_cls_doc
#######
from seed.pkg_tools.ModuleReloader import mk_doctestXmodule_reloader_
doctestXmodule_reloader = mk_doctestXmodule_reloader_('', 'seed.math.power.addition_chain.shortest.search:__doc__', '-ht')
doctestXmodule_reloader(reload_first=False)
doctestXmodule_reloader()
#######

[[
dfs/depth_first_search
    brute_force
    backtracking
    iterative_deepening
]]
[[
come_from:
    e script/蛮力搜索冫最短加链牜修剪搜索树.py
        deprecate...
]]
[[
病蛊记录:
fixed:bug:@蛮力搜索冫最短加链扌()&&@_4search(): len()==假想最小显链长  # 『+1』
fixed:bug:@_4search():return found not 鬽最短加链
fixed:bug:@蛮力搜索冫最短加链扌():没有 提前消除:二幂 三 [爻元数<=3]
    阳爻数==1 <=> 必 +0 => 唯一
    阳爻数==2 <=> 必 +1
    阳爻数==3 => 必 +2
    阳爻数>=4 => 必 >= +2
    已知最短加链
    ++:加辗链-上界
]]


'#'; __doc__ = r'#'
>>>



    def 蛮力搜索冫最短加链扌(sf, 匴前缀无效判定器纟最短加链, 靶值, 鬽前缀纟最短加链, /, *, 彧下界纟最小显链长, 彧上界纟最小显链长, 欤显示冗杂调试信息=False, **额外参数):
        '-> 鬽 最短加链{靶值}'
py_adhoc_call   seed.math.power.addition_chain.shortest.search   @_使用牜极简低效 =1 =None --彧下界纟最小显链长=0 --彧上界纟最小显链长=1
(1,)
py_adhoc_call   seed.math.power.addition_chain.shortest.search   @_使用牜极简低效 =8 =None --彧下界纟最小显链长=0 --彧上界纟最小显链长=1
    <None>
py_adhoc_call   seed.math.power.addition_chain.shortest.search   @_使用牜极简低效 =8 =None --彧下界纟最小显链长=0 --彧上界纟最小显链长=3
(1, 2, 4, 8)
py_adhoc_call   seed.math.power.addition_chain.shortest.search   @_使用牜极简低效 =14 =None --彧下界纟最小显链长=0 --彧上界纟最小显链长=8
(1, 2, 3, 6, 7, 14)
py_adhoc_call   seed.math.power.addition_chain.shortest.search   @_使用牜极简低效 =15 =None --彧下界纟最小显链长=0 --彧上界纟最小显链长=8 +欤显示冗杂调试信息
py_adhoc_call   seed.math.power.addition_chain.shortest.search   @_使用牜极简低效 =15 =None --彧下界纟最小显链长=0 --彧上界纟最小显链长=8
(1, 2, 4, 5, 10, 15)



++补丁牜下界纟非星步
py_adhoc_call   seed.math.power.addition_chain.shortest.search   @_使用牜极简低效 =29 =None --彧下界纟最小显链长=0 --彧上界纟最小显链长=8 +_欤添加显链长
(7, (1, 2, 4, 8, 16, 24, 28, 29))

szmm4shortest_addition_chain 29
[ℓ(29) == 7]



[[
===
debug: 各阶段抛出异常... 测试
===
===
py_adhoc_call   seed.math.power.addition_chain.shortest.search   @_使用牜极简低效 =15 =None --彧下界纟最小显链长=0 --彧上界纟最小显链长=8    --_毝靶值=-1   --_imay_case4starting=-1   --_毝假想显链长=-1
(1, 2, 4, 5, 10, 15)

===
py_adhoc_call   seed.math.power.addition_chain.shortest.search   @_使用牜极简低效 =15 =None --彧下界纟最小显链长=0 --彧上界纟最小显链长=8    --_毝靶值=15   --_imay_case4starting=-1   --_毝假想显链长=-1
^BaseException: ('debugging', 15, -1, -1)

===
py_adhoc_call   seed.math.power.addition_chain.shortest.search   @_使用牜极简低效 =15 =None --彧下界纟最小显链长=0 --彧上界纟最小显链长=8    --_毝靶值=15   --_imay_case4starting=0o00_00   --_毝假想显链长=-1
^BaseException: ('debugging', 15, 0, -1)

===
py_adhoc_call   seed.math.power.addition_chain.shortest.search   @_使用牜极简低效 =15 =None --彧下界纟最小显链长=0 --彧上界纟最小显链长=8    --_毝靶值=15   --_imay_case4starting=0o00_04   --_毝假想显链长=-1
{'参数牜本次运行': {'靶值': 15, '前缀纟最短加链': (1,), '下界纟最小显链长': 5, '上界纟最小显链长': 8}}
{'鬽最短加链牜待检查': (1, 2, 4, 5, 10, 15)}
^seed.math.power.addition_chain.shortest.search._4raise.<locals>.ERR: ('蛮力搜索冫最短加链扌', (BaseException('debugging', 15, 4, -1), {'参数牜本次运行': {'靶值': 15, '前缀纟最短加链': (1,), '下界纟最小显链长': 5, '上界纟最小显链长': 8}, '鬽最短加链牜待检查': (1, 2, 4, 5, 10, 15)}))

===
py_adhoc_call   seed.math.power.addition_chain.shortest.search   @_使用牜极简低效 =15 =None --彧下界纟最小显链长=0 --彧上界纟最小显链长=8    --_毝靶值=15   --_imay_case4starting=0o00_01   --_毝假想显链长=3
(1, 2, 4, 5, 10, 15)

===
py_adhoc_call   seed.math.power.addition_chain.shortest.search   @_使用牜极简低效 =15 =None --彧下界纟最小显链长=0 --彧上界纟最小显链长=8    --_毝靶值=15   --_imay_case4starting=0o00_01   --_毝假想显链长=5
{'参数牜本次运行': {'靶值': 15, '前缀纟最短加链': (1,), '下界纟最小显链长': 5, '上界纟最小显链长': 8}}
{'中断现场': {'鬽深入链乊回溯前': None, '鬽链': None, '假想最小显链长': 5, '新前缀牜假想显链长': (1,), '参数牜本次运行': {'靶值': 15, '前缀纟最短加链': (1,), '下界纟 显链长': 5, '上界纟最小显链长': 8}}}
{'参数牜下一次运行': {'靶值': 15, '前缀纟最短加链': (1,), '下界纟最小显链长': 5, '上界纟最小显链长': 8}}
^seed.math.power.addition_chain.shortest.search._4raise.<locals>.ERR: ('蛮力搜索冫最短加链扌', (BaseException('debugging', 15, 1, 5), {'参数牜本次运行': {'靶值': 15, '前缀纟最短加链': (1,), '下界纟最小显链长': 5, '上界纟 显链长': 8}, '中断现场': {'鬽深入链乊回溯前': None, ' 鬽链': None, '假想最小显链长': 5, '新前缀牜假想显链长': (1,), '参数牜本次运行': {'靶值': 15, '前缀纟最短加链': (1,), '下界纟最小显链长': 5, '上界纟最小显链长': 8}}}))

===
py_adhoc_call   seed.math.power.addition_chain.shortest.search   @_使用牜极简低效 =15 =None --彧下界纟最小显链长=0 --彧上界纟最小显链长=8    --_毝靶值=15   --_imay_case4starting=0o00_02   --_毝假想显链长=5
{'参数牜本次运行': {'靶值': 15, '前缀纟最短加链': (1,), '下界纟最小显链长': 5, '上界纟最小显链长': 8}}
{'中断现场': {'鬽深入链乊回溯前': [1], '鬽链': [1], ' 假想最小显链长': 5, '新前缀牜假想显链长': [1], '参数牜本次运行': {'靶值': 15, '前缀纟最短加链': (1,), '下界纟显 链长': 5, '上界纟最小显链长': 8}}}
{'参数牜下一次运行': {'靶值': 15, '前缀纟最短加链': [1], '下界纟最小显链长': 5, '上界纟最小显链长': 8}}
^seed.math.power.addition_chain.shortest.search._4raise.<locals>.ERR: ('蛮力搜索冫最短加链扌', (BaseException('debugging', 15, 2, 5), {'参数牜本次运行': {'靶值': 15, '前缀纟最短加链': (1,), '下界纟最小显链长': 5, '上界纟 显链长': 8}, '中断现场': {'鬽深入链乊回溯前': [1], '鬽链': [1], '假想最小显链长': 5, '新前缀牜假想显链长': [1], '参数牜本次运行': {'靶值': 15, '前缀纟最短加链': (1,), '下界纟最小显链长': 5, '上界纟最小显链长': 8}}}))

===
py_adhoc_call   seed.math.power.addition_chain.shortest.search   @_使用牜极简低效 =15 =None --彧下界纟最小显链长=0 --彧上界纟最小显链长=8    --_毝靶值=15   --_imay_case4starting=0o00_03   --_毝假想显链长=5
(1, 2, 4, 5, 10, 15)

===
py_adhoc_call   seed.math.power.addition_chain.shortest.search   @_使用牜极简低效 =29 =None --彧下界纟最小显链长=0 --彧上界纟最小显链长=8    --_毝靶值=29   --_imay_case4starting=0o00_03   --_毝假想显链长=7
{'参数牜本次运行': {'靶值': 29, '前缀纟最短加链': (1,), '下界纟最小显链长': 6, '上界纟最小显链长': 8}}
{'中断现场': {'鬽深入链乊回溯前': None, '鬽链': None, '假想最小显链长': 7, '新前缀牜假想显链长': (1,), '参数牜本次运行': {'靶值': 29, '前缀纟最短加链': (1,), '下界纟 显链长': 6, '上界纟最小显链长': 8}}}
{'参数牜下一次运行': {'靶值': 29, '前缀纟最短加链': (1,), '下界纟最小显链长': 7, '上界纟最小显链长': 8}}
^seed.math.power.addition_chain.shortest.search._4raise.<locals>.ERR: ('蛮力搜索冫最短加链扌', (BaseException('debugging', 29, 3, 7), {'参数牜本次运行': {'靶值': 29, '前缀纟最短加链': (1,), '下界纟最小显链长': 6, '上界纟 显链长': 8}, '中断现场': {'鬽深入链乊回溯前': None, ' 鬽链': None, '假想最小显链长': 7, '新前缀牜假想显链长': (1,), '参数牜本次运行': {'靶值': 29, '前缀纟最短加链': (1,), '下界纟最小显链长': 6, '上界纟最小显链长': 8}}}))

===
_4search
    209
    206
===
py_adhoc_call   seed.math.power.addition_chain.shortest.search   @_使用牜极简低效 =29 =None --彧下界纟最小显链长=0 --彧上界纟最小显链长=8    --_毝靶值=29   --_imay_case4starting=209   --_毝假想显链长=6
{'参数牜本次运行': {'靶值': 29, '前缀纟最短加链': (1,), '下界纟最小显链长': 6, '上界纟最小显链长': 8}}
{'中断现场': {'鬽深入链乊回溯前': [1, 2, 4, 8, 16, 17], '鬽链': [1, 2, 4, 8, 16], '假想最小显链长': 6, '新前缀牜假想显链长': [1, 2, 4, 8, 16, 17], '参数牜本次运行': {'靶值': 29, '前缀纟最短加链': (1,), '下界纟最小显链长': 6, '上界纟最小显链长': 8}}}
{'参数牜下一次运行': {'靶值': 29, '前缀纟最短加链': [1, 2, 4, 8, 16, 17], '下界纟最小显链长': 6, '上界纟最小显链长': 8}}
^seed.math.power.addition_chain.shortest.search._4raise.<locals>.ERR: ('蛮力搜索冫最短加链扌', (BaseException('debugging', 29, 209, 6), {'参数牜本次运行': {'靶值': 29, '前缀纟最短加链': (1,), '下界纟最小显链长': 6, '上界 纟显链长': 8}, '中断现场': {'鬽深入链乊回溯前': [1, 2, 4, 8, 16, 17], '鬽链': [1, 2, 4, 8, 16], '假想最小显链长': 6, '新前缀牜假想显链长': [1, 2, 4, 8, 16, 17], '参数牜本次运行': {'靶值': 29, '前缀纟最短加链': (1,), '下 界纟最小显链长': 6, '上界纟最小显链长': 8}}}))

===
py_adhoc_call   seed.math.power.addition_chain.shortest.search   @_使用牜极简低效 =29 =None --彧下界纟最小显链长=0 --彧上界纟最小显链长=8    --_毝靶值=29   --_imay_case4starting=206   --_毝假想显链长=6
{'参数牜本次运行': {'靶值': 29, '前缀纟最短加链': (1,), '下界纟最小显链长': 6, '上界纟最小显链长': 8}}
{'中断现场': {'鬽深入链乊回溯前': [1, 2], '鬽链': [1, 2], '假想最小显链长': 6, '新前缀牜假想显链长': [1, 2], '参数牜本次运行': {'靶值': 29, '前缀纟最短加链': (1,), ' 下界纟最小显链长': 6, '上界纟最小显链长': 8}}}
{'参数牜下一次运行': {'靶值': 29, '前缀纟最短加链': [1, 2], '下界纟最小显链长': 6, '上界纟最小显链长': 8}}
^seed.math.power.addition_chain.shortest.search._4raise.<locals>.ERR: ('蛮力搜索冫最短加链扌', (BaseException('debugging', 29, 206, 6), {'参数牜本次运行': {'靶值': 29, '前缀纟最短加链': (1,), '下界纟最小显链长': 6, '上界 纟显链长': 8}, '中断现场': {'鬽深入链乊回溯前': [1, 2], '鬽链': [1, 2], '假想最小显链长': 6, '新前缀牜假想显链长': [1, 2], '参数牜本次运行': {'靶值': 29, '前缀纟最短 加链': (1,), '下界纟最小显链长': 6, '上界纟最小显链长': 8}}}))

===
]]
[[
12509:首靶值牜最短加链非加星链
py_adhoc_call   seed.math.power.addition_chain.shortest.search   @_使用牜极简低效 =12509 =None --彧下界纟最小显链长=??? --彧上界纟最小显链长=???
szmm4shortest_addition_chain 12509
[ℓ(12509) == 17]

py_adhoc_call   seed.math.power.addition_chain.shortest.search   @_使用牜极简低效 =12509 =None --彧下界纟最小显链长=... --彧上界纟最小显链长=...
^C #KeyboardInterrupt
{'参数牜本次运行': {'靶值': 12509, '前缀纟最短加链': (1,), '下界纟最小显链长': 16, '上界纟最小显链长': 17}}
{'中断现场': {'鬽深入链乊回溯前': [1, 2, 4, 8, 16, 32, 64, 96, 192, 384, 768, 1536, 3072, 6144, 6240, 6272], '鬽链': [1, 2, 4, 8, 16, 32, 64, 96, 192, 384, 768, 1536, 3072, 6144, 6240, 6256], '假想最小显链长': 16, '新前 缀牜假想显链长': [1, 2, 4, 8, 16, 32, 64, 96, 192, 384, 768, 1536, 3072, 6144, 6240, 6256], '参数牜本次运行': {'靶值': 12509, '前缀纟最短加链': (1,), '下界纟最小 显链长': 16, '上界纟最小显链长': 17}}}
{'参数牜下一次运行': {'靶值': 12509, '前缀纟最短加链': [1, 2, 4, 8, 16, 32, 64, 96, 192, 384, 768, 1536, 3072, 6144, 6240, 6256], '下界纟最小显链长': 16, '上界纟 最小显链长': 17}}


##############
{'参数牜下一次运行': {'靶值': 12509, '前缀纟最短加链': [1, 2, 4, 8, 16, 32, 64, 96, 192, 384, 768, 1536, 3072, 6144, 6240, 6256], '下界纟最小显链长': 16, '上界纟 最小显链长': 17}}
##############
py_adhoc_call   seed.math.power.addition_chain.shortest.search   @_使用牜极简低效 =12509 ='[1, 2, 4, 8, 16, 32, 64, 96, 192, 384, 768, 1536, 3072, 6144, 6240, 6256]' --彧下界纟最小显链长=16 --彧上界纟最小显链长=17
^C#KeyboardInterrupt
{'参数牜本次运行': {'靶值': 12509, '前缀纟最短加链': (1, 2, 4, 8, 16, 32, 64, 96, 192, 384, 768, 1536, 3072, 6144, 6240, 6256), '下界纟最小显链长': 16, '上界纟 最小显链长': 17}}
{'中断现场': {'鬽深入链乊回溯前': [1, 2, 4, 8, 16, 32, 48, 56, 96, 192, 384, 768, 1536, 3072, 4608, 9216], '鬽链': [1, 2, 4, 8, 16, 32, 48, 56, 96, 192, 384, 768, 1536, 3072, 4608, 7680], '假想最小显链长': 16, '新前缀牜 假想最小显链长': [1, 2, 4, 8, 16, 32, 48, 56, 96, 192, 384, 768, 1536, 3072, 4608, 7680], '参数牜本次运行': {'靶值': 12509, '前缀纟最短加链': (1, 2, 4, 8, 16, 32, 64, 96, 192, 384, 768, 1536, 3072, 6144, 6240, 6256), '下界纟最小显链长': 16, '上界纟最小显链长': 17}}}
{'参数牜下一次运行': {'靶值': 12509, '前缀纟最短加链': [1, 2, 4, 8, 16, 32, 48, 56, 96, 192, 384, 768, 1536, 3072, 4608, 7680], '下界纟最小显链长': 16, '上界纟最 小显链长': 17}}





===
{'参数牜下一次运行': {'靶值': 12509, '前缀纟最短加链': [1, 2, 4, 8, 16, 32, 48, 56, 96, 192, 384, 768, 1536, 3072, 4608, 7680], '下界纟最小显链长': 16, '上界纟最 小显链长': 17}}

++补丁牜下界纟非星步
py_adhoc_call   seed.math.power.addition_chain.shortest.search   @_使用牜极简低效 =12509 ='[1, 2, 4, 8, 16, 32, 48, 56, 96, 192, 384, 768, 1536, 3072, 4608, 7680]' --彧下界纟最小显链长=16 --彧上界纟最小显链长=17 +_欤添加显链长
... ...
{'参数牜下一次运行': {'靶值': 12509, '前缀纟最短加链': [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 1152, 1536, 1600, 3072, 6144, 6656], '下界纟最小显链长': 17, '上界纟最小显链长': 17}}
... ...

！！！下界已提升！！！
py_adhoc_call   seed.math.power.addition_chain.shortest.search   @_使用牜极简低效 =12509 ='[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 1152, 1536, 1600, 3072, 6144, 6656]' --彧下界纟最小显链长=17 --彧上界纟最小显链长=17 +_欤添加显链长
... ...
{'参数牜下一次运行': {'靶值': 12509, '前缀纟最短加链': [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 768, 1536, 1537, 1793, 3330, 3458, 6788], '下界纟最小显链长': 17, '上界纟最小显链长': 17}}
... ...


]]

[[
TODO:
    乸匴前缀无效判定器纟最短加链牜提前排除乘环殿后牜强制乘环次序
分解整数
    检查短链串接=>最小串接显链长

* [最小串接显链长 < 假想最小显链长]:
    异常x完成...
* [最小串接显链长 == 假想最小显链长]:
    完成...
* [最小串接显链长 > 假想最小显链长]:
    #排除乘环殿后
    乘环次序...
    乘环义务出度...
        +环长不是倍数的最小显链长/即使是，搜过后排除此倍数
        +非星步/出度0
        +倍数降序
        +自由乘环#特别是最后一个乘环

每个节点 向外被一圈圈的乘环包裹
    b2ca_ls : 匏间讠匏脐匏口列表
    树: 父节点-(大乘环|大交错区)，子节点-(小乘环|小交错区)
j+i ~>k 破坏 所有 jk 之间的圈
a~>[c] : 匏口讠匏脐列
c~>[a] : 匏脐讠匏口列



]]






from seed.math.power.addition_chain.shortest.search import *
]]]'''#'''
__all__ = r'''
魖匴前缀无效判定器纟最短加链
    乸匴前缀无效判定器纟最短加链牜极简低效
        匴前缀无效判定器纟最短加链牜极简低效
魖匴蛮力搜索器纟最短加链
    乸匴蛮力搜索器纟最短加链
        匴蛮力搜索器纟最短加链


'''.split()#'''
#.蛮力搜索冫最短加链扌

__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
null_iter = iter('')
#.from functools import cached_property
from seed.tiny_.check import check_type_is, check_int_ge
#see:dot_#from seed.func_tools.dot2 import dot
#.
#.from abc import update_abstractmethods
from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.#################################
#.from seed.for_libs.for_importlib__reload import clear_later_variables_if_reload_
#.clear_later_variables_if_reload_(globals(), '')
#.    # <<== seed.pkg_tools.ModuleReloader
#.
#.#################################
#.from seed.helper.lazy_import__func7context import mk_ctx4lazy_import8lazy_objs__ver2_
#.with mk_ctx4lazy_import8lazy_objs__ver2_(nonexistent_prefix4qnm4mdl8src='__.', prefix4attr='lazy_', suffix4attr=''):
#.    from __.seed.tiny_.containers import lazy_null_tuple,lazy_null_iter,lazy_null_frozenset as _lazy_null_frozenset_ #null_tuple,null_iter,null_frozenset
#.#################################
#.from seed.helper.lazy_import__func import force_lazy_imported_func_ # lazy_import4func_, lazy_import4funcs_
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
#.with mk_ctx4lazy_import4funcs_(__name__, 'ifNone:_ifNone, ifNonef:_ifNonef'):
#.    from seed.helper.ifNone import ifNone as _ifNone, ifNonef as _ifNonef
with mk_ctx4lazy_import4funcs_(__name__):
    from collections import namedtuple
    from seed.math.power.addition_chain.common.check import 检查冫严序加链乊靶值扌, 检查冫严序加链扌, 检查冫严序加链内容扌
    from seed.math.power.addition_chain.common.check import 检查冫松序加链乊靶值扌, 检查冫松序加链扌, 检查冫松序加链内容扌
    from seed.math.power.addition_chain.short.binary import 构造冫加链巛靶值牜二进制拆分扌
    from seed.math.power.addition_chain.common.properties import 显链长纟, 阳爻数纟, 首爻位纟
    from seed.helper.ifNone import ifNone,ifNonef
    from seed.tiny_.funcs import echo,fst,snd
    from itertools import groupby
    from seed.iters.PeekableIterator import echo_or_mk_IPeekableIterator
        #is_empty#not hp
        #head#hp[0]
        #read1()#_heappop
    from seed.for_libs.for_heapq import merge_ex
        #def merge_ex(*sorted_iterable_exs, key4stable:[False,callable]=False, key4le=None, __le__=None, reverse=False, unique:[bool,callable]=False, obj2value_:[None,callable]=None):
    from seed.debug.print_err import print_err
    from seed.types.Either import mk_Left,mk_Right #Either,Cased

    from seed.data_funcs.lnkls import mk_empty_rglnkls, rglnkls_ipush_right, rglnkls_ipop_right, rglnkls2reversed_iterable, rglnkls5iterable #rglnkls_ops, empty_rglnkls

    from seed.data_funcs.lnkls import rglnkls2list



    from seed.math.power.addition_chain.shortest.upper_bound4len_optimal_addition_chain import 实证估计冫上界纟最小显链长巛靶值牜次优牜精研综合扌, 估计冫上界纟最小显链长巛靶值牜速算牜精研综合扌
    #def 实证估计冫上界纟最小显链长巛靶值牜次优牜精研综合扌(靶值, /, *, 欤排除窗式拆分牜定窗式=False, 欤排除窗式拆分牜滑窗式=False):
    #    '靶值 -> (上界纟最小显链长{靶值}, 加链{靶值}{显链长==上界纟最小显链长{靶值}})'

    from seed.math.power.addition_chain.shortest.lower_bound4len_optimal_addition_chain import 估计冫下界纟最小显链长巛靶值牜精研综合扌
    #def 估计冫下界纟最小显链长巛靶值牜精研综合扌(靶值, /, *, 鬽上界纟最小显链长, 鬽上界纟总小步数=None, 欤排除数据验证部分=False):

#.    from seed.helper.repr_input import repr_helper
#.    from seed.tiny_.map_ import map_, cmap_, call_, prepare4call_, dots_
#.    from seed.tiny_.types5py import mk_MapView,curry1,kwargs2Attrs #,MapView
#.    from seed.tiny_.containers import mk_tuple,mk_immutable_seq,mk_immutable_seq5iterT_,mk_immutable_seq5iter__,mk_bytes5iter_,mk_tuple__split_first_if_str,mk_tuple__split_first_if_str__sep_ #xxx:null_tuple
#.    from seed.debug.expectError import expectError
#.    from seed.iters.flatten_recur import flatten_recur
#.    # def flatten_recur(g:Generator, /, *, value:object=None, is_exc=False, boxed=False):
#.    from seed.func_tools.dot_ import dot_
#.    from seed.iters.PeekableIterator import echo_or_mk_PeekableIterator
#.    from seed.for_libs.for_collections.namedtuple__nontuple4cached_property import mk_named_pseudo_tuple_
#.    #def mk_named_pseudo_tuple_(__module__,typename, field_names, /):
#.    #    def _check6make_(sf, /):
#.    from seed.for_libs.for_collections.namedtuple__nontuple4cached_property import collect_tuple_subclasses_with_cached_property
#.    #assert not (__:=collect_tuple_subclasses_with_cached_property(globals(), to_print_err=True)), __
#.#################################
#.:s/\v^from +([_[:alnum:].]+) +import +([^# ]( *[^# ])*).*/lazy_import4funcs_('\1', '\2', __name__)\rif 0:\0



#.#################################
#.from seed.types.LazyList import ToConcatLazyList, decorator4protocol4ToConcatLazyList_
#.from seed.types.LazyList import LazyList, LazyListError
#.from seed.types.LazyList import to_LazyList, to_LazyListIter
#.
#.from seed.tiny_._Base4repr import _Base4repr
        #sf._reset4repr(may_args4repr, may_kwds4repr)
        #sf._init4repr(*args4repr, **kwds4repr)
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError(Exception, StopIteration)

__all__



class 魖匴前缀无效判定器纟最短加链(ABC):
    '匴前缀无效判定器{最短加链}'
    #额外参数:, 鬽素数分解纟靶值, 更小靶值讠最短加链, 更小靶值讠最小显链长
    __slots__ = ()
    @abstractmethod
    def 乊搜索起始纟批量处理扌(sf, 靶值, /, *, 欤显示冗杂调试信息, **额外参数):
        '靶值{>=15}{log2(靶值)%1=!=1}{阳爻数{靶值}>=4} -> 状态纟批次 | ^Exception # 做些针对 靶值 的冗长计算，比如:因数分解，异常出现时 分解结果 通过 保存冫状态纟批次讠部分具名参数扌 /保存冫状态纟无效判定讠额外具名参数扌 输出到 标准错误输出文件'
    @abstractmethod
    def 欤强制降序乊可交换步扌(sf, 状态纟批次, /):
        '状态纟批次{靶值} -> bool'
    @abstractmethod
    def 保存冫状态纟批次讠部分具名参数扌(sf, 状态纟批次, /):
        '状态纟批次{靶值} -> 部分具名参数{可读性数据}/kwds{.乊搜索起始纟批量处理扌.额外参数}'
    #下面 难以使用:异常出现时，b_goback多次...
    #.@abstractmethod
    #.def 保存冫状态纟无效判定讠额外具名参数扌(sf, 状态纟无效判定, /):
    #.    '状态纟无效判定{靶值,假想最小显链长} -> 额外具名参数{可读性数据}/kwds{.乊搜索起始纟批量处理扌.额外参数}'
    @abstractmethod
    def 乊搜索起始乊假想显链长扌(sf, 状态纟批次, 假想最小显链长, /):
        '状态纟批次{靶值} -> 假想最小显链长 -> Either 最短加链{靶值} 状态纟无效判定 | ^Exception # 起始:[前缀纟最短加链 == [1]]'
    #.@abstractmethod
    #.def 乊搜索起始扌(sf, 靶值, 假想最小显链长, /, *, 欤显示冗杂调试信息, **额外参数):
    #.    '靶值{>=15}{log2(靶值)%1=!=1}{阳爻数{靶值}>=4} -> 假想最小显链长 -> Either 最短加链{靶值} 状态纟无效判定 | ^Exception # 起始:[前缀纟最短加链 == [1]]'
    @abstractmethod
    def 欤加链前缀无效扌(sf, 状态纟无效判定, /):
        '状态纟无效判定 -> 欤加链前缀无效/bool'
    #@abstractmethod
    def 求取冫鬽下上界纟后一位扌(sf, 状态纟无效判定, /):
        '[0 <= 当前显链长 < 假想最小显链长][not 欤加链前缀无效] => 状态纟无效判定 -> 后几位/uint{>=1} -> 鬽 (下界纟后一位, 上界纟后一位)'
        return sf.求取冫鬽下上界纟后几位扌(状态纟无效判定, 1)
    @abstractmethod
    def 求取冫鬽下上界纟后几位扌(sf, 状态纟无效判定, 后几位, /):
        '[0 <= 当前显链长 < 假想最小显链长][not 欤加链前缀无效] => 状态纟无效判定 -> 后几位/uint{>=1} -> 鬽 (下界纟后几位, 上界纟后几位)'
    @abstractmethod
    def 乊加链前缀增位扌(sf, 状态纟无效判定, 值纟后一位, 列表纟大小址引纟加数纟后一位, /):
        '[0 <= 当前显链长 < 假想最小显链长][not 欤加链前缀无效][下界纟后一位<=值纟后一位<=上界纟后一位] => 状态纟无效判定 -> 值{后一位} -> 列表纟大小址引纟加数{后一位}/[(j,i)] -> 状态纟无效判定'
    @abstractmethod
    def 乊加链前缀减位扌(sf, 状态纟无效判定, /):
        '[0 < 当前显链长 <= 假想最小显链长] => 状态纟无效判定 -> 状态纟无效判定'


___begin_mark_of_excluded_global_names__99___ = ...
def 蛮力搜索冫最短加链扌(sf, 匴前缀无效判定器纟最短加链, 靶值, 鬽前缀纟最短加链, /, *, 彧下界纟最小显链长, 彧上界纟最小显链长, 欤显示冗杂调试信息=False, **额外参数):
    '-> 鬽 最短加链{靶值}'
    if 1:
        ######################
        #规范输入阶段:
        ######################
        check_int_ge(1, 靶值)
        check_type_is(bool, 欤显示冗杂调试信息)
        ######################
        if 彧上界纟最小显链长 is ...:
            (上界纟最小显链长, 加链冃证据) = 实证估计冫上界纟最小显链长巛靶值牜次优牜精研综合扌(靶值)
        else:
            上界纟最小显链长 = 彧上界纟最小显链长
        上界纟最小显链长
        check_int_ge(0, 上界纟最小显链长)
        ######################
        if 彧下界纟最小显链长 is ...:
            下界纟最小显链长 = 估计冫下界纟最小显链长巛靶值牜精研综合扌(靶值, 鬽上界纟最小显链长=上界纟最小显链长)
        else:
            下界纟最小显链长 = 彧下界纟最小显链长
        下界纟最小显链长
        check_int_ge(0, 下界纟最小显链长)
        ######################
        ######################
        verbose = 欤显示冗杂调试信息
        ######################
        sf.罓乊测试扌(靶值=靶值, case4starting=-1, 假想最小显链长=-1)
        if not 下界纟最小显链长 <= 上界纟最小显链长:
            return None
        # [下界纟最小显链长 <= 上界纟最小显链长]
        前缀纟最短加链 = [1] if None is 鬽前缀纟最短加链 else [*鬽前缀纟最短加链]
        if not 前缀纟最短加链:
            前缀纟最短加链.append(1)
        # [1 <= len(前缀纟最短加链)]
        # [0 <= 显链长纟(前缀纟最短加链)]
        if not 显链长纟(前缀纟最短加链) <= 上界纟最小显链长:raise Exception
        # [0 <= 显链长纟(前缀纟最短加链) <= 上界纟最小显链长]
        if not 显链长纟(前缀纟最短加链) <= 下界纟最小显链长: raise Exception('输入应当是: [前缀纟最短加链 := 前缀纟最短加链{乊前次搜索异常退出}][下界纟最小显链长 := 假想最小显链长{乊前次搜索异常退出}]')
        # [显链长纟(前缀纟最短加链) <= 下界纟最小显链长]
        # !! [下界纟最小显链长 <= 上界纟最小显链长]
        # 下界纟最小显链长 = max(下界纟最小显链长, 显链长纟(前缀纟最短加链))
        # [0 <= 显链长纟(前缀纟最短加链) <= 下界纟最小显链长 <= 上界纟最小显链长]
        检查冫严序加链内容扌(前缀纟最短加链)
        # [前缀纟最短加链 <- 乸严序加链]
        if 前缀纟最短加链[-1] > 靶值: raise Exception
        if 前缀纟最短加链[-1] == 靶值:
            # !! [0 <= 显链长纟(前缀纟最短加链) <= 下界纟最小显链长 <= 上界纟最小显链长]
            # !! [前缀纟最短加链 <- 乸严序加链]
            return tuple(前缀纟最短加链)
            raise Exception
        # [前缀纟最短加链[-1] < 靶值]
        阳爻数纟靶值 = 阳爻数纟(靶值)
        if not 阳爻数纟靶值 >= 4:
            最短加链 = 构造冫加链巛靶值牜二进制拆分扌(靶值)
            return 最短加链 if 下界纟最小显链长 <= 显链长纟(最短加链) <= 上界纟最小显链长 else None
        # [阳爻数{靶值} >= 4]
        # [靶值 >= 15]
        assert 靶值 >= 15
        首爻位纟靶值 = 首爻位纟(靶值)
        下界纟最小显链长 = max(下界纟最小显链长, 首爻位纟靶值+2)
        if not 下界纟最小显链长 <= 上界纟最小显链长:
            return None
        # [下界纟最小显链长 <= 上界纟最小显链长]
        ######################





        ######################
        #主工作循环:
        ######################

        ######################
        # [阳爻数{靶值} >= 4]
        # [前缀纟最短加链 <- 乸严序加链]
        # [前缀纟最短加链[-1] < 靶值]
        # [0 <= 显链长纟(前缀纟最短加链) <= 下界纟最小显链长 <= 上界纟最小显链长]
        ######################
        匴 = 匴前缀无效判定器纟最短加链
        备份纟前缀纟最短加链 = 前缀纟最短加链 = tuple(前缀纟最短加链)
        # [0 <= 显链长纟(前缀纟最短加链) <= 下界纟最小显链长 <= 上界纟最小显链长]
        # [前缀纟最短加链[-1] < 靶值]
        状态纟批次 = 匴.乊搜索起始纟批量处理扌(靶值, 欤显示冗杂调试信息=verbose, **额外参数)
        case4starting = 0o00_00
        sf.罓乊测试扌(靶值=靶值, case4starting=case4starting, 假想最小显链长=-1)
    try:
        for 假想最小显链长 in range(下界纟最小显链长, 1+上界纟最小显链长):
            sf.罓乊测试扌(靶值=靶值, case4starting=case4starting, 假想最小显链长=假想最小显链长)
            assert case4starting in (0, 3)
            # [下界纟最小显链长 <= 假想最小显链长 <= 上界纟最小显链长]
            # [0 <= 显链长纟(前缀纟最短加链) <= 下界纟最小显链长]

            if not 假想最小显链长 == 下界纟最小显链长:
                # [0 <= 显链长纟(前缀纟最短加链) <= 下界纟最小显链长]
                前缀纟最短加链 = (1,)
                # [0 <= 显链长纟(前缀纟最短加链) <= 下界纟最小显链长]
            # [0 <= 显链长纟(前缀纟最短加链) <= 下界纟最小显链长]
            # !! [下界纟最小显链长 <= 假想最小显链长 <= 上界纟最小显链长]
            # [0 <= 显链长纟(前缀纟最短加链) <= 假想最小显链长]
            case4starting = 0o00_01
            sf.罓乊测试扌(靶值=靶值, case4starting=case4starting, 假想最小显链长=假想最小显链长)
            #xxx取消:
                #.[前缀纟最短加链{1<=len<1+假想最小显链长}{严序加链}{前缀纟最短加链[-1]<靶值}]
                #.前缀纟最短加链 = [1]
                #.st = 匴.乊搜索起始扌(靶值, 假想最小显链长, 前缀纟最短加链, **额外参数)
            # [阳爻数{靶值} >= 4]
            # [靶值 >= 15]
            链 = [1]
            777;either_us_st = 匴.乊搜索起始乊假想显链长扌(状态纟批次, 假想最小显链长)
            if either_us_st.is_left:
                最短加链 = either_us_st.left
                鬽最短加链 = 最短加链
                break
            st = either_us_st.right
            # [st <~~ 链[-1]]
            # [len(链) == 1 <= len(前缀纟最短加链) <= 1+假想最小显链长]
            # [链 == 前缀纟最短加链[:len(链)]]
            欤强制降序乊可交换步 = 匴.欤强制降序乊可交换步扌(状态纟批次)
            kwds4hp = dict(假想最小显链长=假想最小显链长, 欤强制降序乊可交换步=欤强制降序乊可交换步, verbose=verbose)
            stk = []
                # :: [heap{-u:[(j,i)]}]
                #   heap_item.u
            # [len(链) == 1+len(stk)]
            # [len(链) == 1 <= len(前缀纟最短加链)]
            # [链 == 前缀纟最短加链[:len(链)]]
            # [st <~~ 链[-1]]
            for u in 前缀纟最短加链[1:]:
                # [len(链) == 1+len(stk)]
                # [len(链) < len(前缀纟最短加链)]
                # [链 == 前缀纟最短加链[:len(链)]]
                # [st <~~ 链[-1]]
                hp = _4mk_heap4next(sf, 匴, 靶值, 链, st, 上界=u, **kwds4hp)
                if not (hp and hp.head.u == u):
                    # [hp !<- stk]
                    # [not hp]or[hp[0] !<- 链]
                    break # (链, stk, st, hp{next})
                # [hp[0].u == u]
                stk.append(hp)
                链.append(u)
                # [len(链) <= len(前缀纟最短加链)]
                # [链 == 前缀纟最短加链[:len(链)]]
                777;st = 匴.乊加链前缀增位扌(st, u, hp.head.ji_ls)
                # [st <~~ 链[-1]]
                # [stk[-1][0].u == 链[-1]]
                # [len(链) == 1+len(stk)]
                # [stk[j-1][0].u == 链[j]]
            else:
                hp = _4mk_heap4next(sf, 匴, 靶值, 链, st, 上界=None, **kwds4hp)
                # [hp !<- stk]
                # [hp[0] !<- 链]
            ########
            # (链, stk, st, hp{next})
            ########
            # [st <~~ 链[-1]]
            ########
            # [hp !<- stk]
            # [not hp]or[hp[0] !<- 链]
            ########
            # [1 <= len(链) <= len(前缀纟最短加链) <= 1+假想最小显链长]
            # [链 == 前缀纟最短加链[:len(链)]]
            # !! [前缀纟最短加链[-1] < 靶值]
            # [链[-1] < 靶值]
            # [1 <= len(链) <= 1+假想最小显链长]
            # [len(链) == 1+len(stk)]
            # [[j:<-[1..<len(链)]] -> [链[j] == stk[j-1].u]]
            ########
            assert len(链) == 1+len(stk)
            # _深入链乊回溯前 = [*链]
            #_深入链乊回溯前 = [len(链), rglnkls5iterable(链)]
            _深入链乊回溯前 = []
                #用于 异常时输出环境
            case4starting = 0o00_02
            sf.罓乊测试扌(靶值=靶值, case4starting=case4starting, 假想最小显链长=假想最小显链长)
            if verbose:print_err(f'into: 靶值={靶值}, 假想最小显链长={假想最小显链长}, 链={链}')
            if _4search(sf, 匴, 靶值, 假想最小显链长, 链, stk, st, hp, _深入链乊回溯前, verbose=verbose, kwds4hp=kwds4hp):
                # found
                最短加链 = tuple(链)
                鬽最短加链 = 最短加链
                break
            assert 链 == [1]
            assert not stk
            case4starting = 0o00_03
        else:
            鬽最短加链 = None
        ######################
        #收尾阶段:
        ######################
        case4starting = 0o00_04
        sf.罓乊测试扌(靶值=靶值, case4starting=case4starting, 假想最小显链长=-1)
        if not 鬽最短加链 is None:
            检查冫严序加链乊靶值扌(靶值, 最短加链)
            assert 下界纟最小显链长 <= 显链长纟(最短加链) <= 上界纟最小显链长
        return 鬽最短加链
    except BaseException as e:
        ######################
        #输出中断现场:
        ######################
        if 0:0
        参数牜本次运行= dict(靶值=靶值, 前缀纟最短加链=备份纟前缀纟最短加链, 彧下界纟最小显链长=下界纟最小显链长, 彧上界纟最小显链长=上界纟最小显链长, **额外参数)
        _4print_err(参数牜本次运行=参数牜本次运行)
        if case4starting == 0o00_00:
            raise _4raise(e, 参数牜本次运行=参数牜本次运行)
        if case4starting == 0o00_04:
            _4print_err(鬽最短加链牜待检查=鬽最短加链)
            raise _4raise(e, 参数牜本次运行=参数牜本次运行, 鬽最短加链牜待检查=鬽最短加链)
        if case4starting == 0o00_03:
            if not 假想最小显链长 == 下界纟最小显链长:
                前缀纟最短加链 = (1,)
            case4starting = 0o00_01
        ######
        assert case4starting in (1, 2)
        ######
        if not case4starting == 0o00_02:
            #尚无:链、_深入链乊回溯前
            链 = None
            深入链乊回溯前 = None
        else:
            链
            深入链乊回溯前 = rglnkls2list(_深入链乊回溯前[1])
        ######
        if case4starting == 0o00_01:
            #尚无:链、_深入链乊回溯前
            新前缀 = 前缀纟最短加链
        elif case4starting == 0o00_02:
            #已有:链、_深入链乊回溯前
            if 深入链乊回溯前[:len(链)] == 链:
                # [b_goback]
                # [b_goback ing...]
                新前缀 = 深入链乊回溯前
            else:
                # [not b_goback]
                新前缀 = 链
            新前缀
        else:
            raise 000
        新前缀
        中断现场 = dict(鬽深入链乊回溯前=深入链乊回溯前, 鬽链=链, 假想最小显链长=假想最小显链长, 新前缀牜假想显链长=新前缀,     参数牜本次运行=参数牜本次运行)
        _4print_err(中断现场=中断现场)
        部分具名参数 = 匴.保存冫状态纟批次讠部分具名参数扌(状态纟批次)
        参数牜下一次运行 = dict(参数牜本次运行)
        777;参数牜下一次运行.update(前缀纟最短加链=新前缀, 彧下界纟最小显链长=假想最小显链长, **部分具名参数)
        _4print_err(参数牜下一次运行=参数牜下一次运行)
        raise _4raise(e, 参数牜本次运行=参数牜本次运行, 中断现场=中断现场)
    if 1:
        raise 000
#end-def 蛮力搜索冫最短加链扌(sf, 匴前缀无效判定器纟最短加链, 靶值, 鬽前缀纟最短加链, /, *, 下界纟最小显链长, 上界纟最小显链长, **额外参数):
def _4print_err(**kwds):
    print_err(kwds)
def _4raise(exc, /, **kwds):
    #bug:class ERR(type(exc), BaseException):
    #   class ERR(BaseException, BaseException):
    #       ^TypeError: duplicate base class BaseException
    bases = [type(exc), BaseException]
    if bases[0] is bases[1]:
        bases.pop()
    class ERR(*bases):
        def __init__(sf, /, *args):
            BaseException.__init__(sf, *args)

    raise ERR('蛮力搜索冫最短加链扌', (exc, kwds)) from exc
___end_mark_of_excluded_global_names__99___ = ...

class 魖匴蛮力搜索器纟最短加链(ABC):
    '匴蛮力搜索器{最短加链}'
    __slots__ = ()
    #.@property
    #.@abstractmethod
    #.def 匴前缀无效判定器纟最短加链(sf, /):
    #.    '-> 魖匴前缀无效判定器纟最短加链'
    #
    def 罓乊测试扌(sf, /, *, 靶值, case4starting, 假想最小显链长):
        return

    ######################
    蛮力搜索冫最短加链扌 = 蛮力搜索冫最短加链扌
    ######################
def _4pop(_链, /):
    (_链[1], u) = rglnkls_ipop_right(_链[1])
    _链[0] -= 1
    #if 0b0001:print_err('_4pop:', u, '#', _链[0])
def _4push(_链, u, /):
    #if 0b0001:print_err('_4push:', u, '#', _链[0])
    (_链[1], _None) = rglnkls_ipush_right(_链[1], u)
    _链[0] += 1
def _4search(sf, 匴, 靶值, 假想最小显链长, 链, stk, st, hp, _深入链乊回溯前, /, *, verbose, kwds4hp):
    '-> b_found'
    ########
    # (链, stk, st, hp{next})
    ########
    # [st <~~ 链[-1]]
    ########
    # [hp !<- stk]
    # [not hp]or[hp[0] !<- 链]
    ########
    # [链[-1] < 靶值]
    # [1 <= len(链) <= 1+假想最小显链长]
    # [len(链) == 1+len(stk)]
    # [[j:<-[1..<len(链)]] -> [链[j] == stk[j-1].u]]
    ########
    链长上界 = 1+假想最小显链长
    assert 1 <= len(链) <= 链长上界
    assert len(链) == 1+len(stk)
    ########
    b_goback = False
    stk.append(hp); del hp
    # [len(链) == len(stk) >= 1]
    # [[j:<-[1..<len(链)]] -> [链[j] == stk[j-1].u]]
    # [not stk[-1]]or[not stk[-1] !<- 链]
    # [st <~~ 链[-1]]
    # [not b_goback]
    # [1 <= len(链) <= 链长上界]
    # [链[-1] < 靶值]
    ########
    _链 = [len(链), rglnkls5iterable(链)]
    _深入链乊回溯前[:] = _链
    while 1:
        if verbose:print_err(f'loop: b_goback={b_goback}, 链={链}')
        assert stk
        # [1 <= len(链) <= 链长上界]
        # [链[-1] < 靶值]
        # [len(链) == len(stk) >= 1]
        # [[j:<-[1..<len(链)]] -> [链[j] == stk[j-1].u]]
        # [not stk[-1]]or[not stk[-1] !<- 链]
        # [st <~~ 链[-1]]
        assert 链[-1] < 靶值
        hp = stk[-1]
        if b_goback:
            #回溯
            # [not stk[-1] !<- 链]
            assert hp
            _heappop(hp)
            # [not stk[-1]]or[not stk[-1] !<- 链]
            b_goback = False
            # [len(链) == len(stk) >= 1]
            # [[j:<-[1..<len(链)]] -> [链[j] == stk[j-1].u]]
            # [st <~~ 链[-1]]
            continue
        #深入
        assert not b_goback
        # [链[-1] < 靶值]
        # [1 <= len(链) <= 链长上界]
        if len(链) == 链长上界 or hp.is_empty():
            if _深入链乊回溯前[0] > len(链):
                if verbose:print_err('_深入链乊回溯前: 回溯中...', 链, (靶值, 假想最小显链长))
                sf.罓乊测试扌(靶值=靶值, case4starting=209, 假想最小显链长=假想最小显链长)
                    #0o00_0209:『SyntaxError: invalid digit '9' in octal literal』
            else:
                if verbose:print_err('_深入链乊回溯前: 回溯起始', 链)
                _深入链乊回溯前[:] = _链
            stk.pop()
            # [len(链) -1 == len(stk) >= 0]
            if not stk:
                return (b_found:=False)
                break
            # [len(链) -1 == len(stk) >= 1]
            st = 匴.乊加链前缀减位扌(st)
            777;链.pop();_4pop(_链)
            # [st <~~ 链[-1]]
            # [len(链) == len(stk) >= 1]
            # [not stk[-1] !<- 链]
            # [[j:<-[1..<len(链)]] -> [链[j] == stk[j-1].u]]
            b_goback = True
            continue
        # [1 <= len(链) < 链长上界]
        # [len(hp) > 0]
        # [not stk[-1] !<- 链]
        u = hp.head.u
        if not u > 链[-1]:raise 000-_4mk_heap4next-_4next_bounds
            # !! [下界纟后一位 = max(下界纟后一位, 1+链[-1])]
            # => [hp[0].u >= 1+链[-1]]
            # => [链:严序]
        if not u <= 靶值:raise 000-_4mk_heap4next-_4next_bounds
            # !! [上界纟后一位 := min(上界纟后一位, 靶值)]
            # => [hp[0].u <= 靶值]
        # [u <= 靶值]
        # [1 <= len(链) < 链长上界]
        链.append(u);_4push(_链, u)
        # [1 <= len(链) <= 链长上界]
        777;st = 匴.乊加链前缀增位扌(st, u, hp.head.ji_ls)
        # [st <~~ 链[-1]]
        if u == 靶值:
            return (b_found:=True)
        # [u < 靶值]
        # [链[-1] < 靶值]
        hp = _4mk_heap4next(sf, 匴, 靶值, 链, st, 上界=None, **kwds4hp)
        stk.append(hp)
        # [not stk[-1]]or[not stk[-1] !<- 链]
        # [len(链) == len(stk) >= 1]
        # [[j:<-[1..<len(链)]] -> [链[j] == stk[j-1].u]]
        # [链[-1] < 靶值]
        # [1 <= len(链) <= 链长上界]
        _深入链乊回溯前[:] = _链
        sf.罓乊测试扌(靶值=靶值, case4starting=206, 假想最小显链长=假想最小显链长)
    raise 000

_U_JIs_Pair = namedtuple('_U_JIs_Pair', 'u  ji_ls')
def _4mk_heap4next(sf, 匴, 靶值, 假想最小显链长, 链, st, /, *, 上界:None, verbose, **_kwds4hp):
    #kwds4hp
    args_ = [sf, 匴, 靶值, 链, st]
    (下界纟后一位, 上界纟后一位) = _4next_bounds(*args_, 1)
    上界 = min(上界纟后一位, ifNone(上界, 上界纟后一位))
    下界 = 下界纟后一位
    if not 下界 <= 上界:
        if verbose: print_err(f'mk-empty-hp: hp=[], 下界={下界}, 上界={上界}')
        return echo_or_mk_IPeekableIterator(null_iter) #_4mk_empty_heap_()
    def u_objs2u_ji_ls_(u_objs, /):
        u, [*objs] = u_objs
        #objs.sort(reverse=True)
        assert objs[0][0] == u
        assert objs[-1][0] == u
        assert objs[0] >= objs[-1]
        ji_ls = tuple((j, i) for _u, (j, i) in objs)
        assert ji_ls[0] >= ji_ls[-1]
            #ji_ls降序
        return _U_JIs_Pair(u, ji_ls)

    it = echo_or_mk_IPeekableIterator(map(u_objs2u_ji_ls_, groupby(merge_ex(_4iter_next(链, 下界, args_, **_kwds4hp), reverse=True), key=fst)))
        # :: PeekableIterator{(u, ji_ls)}
    while (not it.is_empty()) and it.head.u > 上界:
        #it.read1()
        next(it)
    hp = it
    if verbose:
        hp = list(hp)
        print_err(f'mk: hp={hp}, 下界={下界}, 上界={上界}')
        hp = echo_or_mk_IPeekableIterator(iter(hp))
    return hp
def _heappop(hp, /):
    #it.read1()
    next(hp)
def _4iter_next(链, 下界, args_, /, *, 假想最小显链长, 欤强制降序乊可交换步):
    #_kwds4hp

    #########
    # [:补丁牜下界纟非星步]:here
    #########
    剩余长度 = 假想最小显链长 -len(链)
    if 剩余长度 >= 3:
        (下界纟后三位, 上界纟后三位) = _4next_bounds(*args_, 3)
            #@后一位非星步
        #[[[前缀纟最短加链[k] == 前缀纟最短加链[j]+前缀纟最短加链[i]]] -> [0 <= i <= j < k < 假想最小显链长] -> [前缀纟最短加链[k]*2+前缀纟最短加链[k-1] >= 下界乊[k+2]]]
        #   #前缀纟最短加链[k-1] 义务出度为1
        #   #前缀纟最短加链[k] 后续极大化=>等效义务出度为2 #因为 加法降序
        #     # 由于 加法降序 所以 [[前缀纟最短加链[k+1] == 前缀纟最短加链[k]+前缀纟最短加链[k-1]] -> [前缀纟最短加链[k]义务出度>=2]]
        #     #     => 还不如 [前缀纟最短加链[k+1]==2*前缀纟最短加链[k]][前缀纟最短加链[k+2]==2*前缀纟最短加链[k]+前缀纟最短加链[k-1]]
        #
        欤可行冫非星步 = 下界纟后三位 <= 上界纟后三位
        下界纟后一位牜非星步 = (下界纟后三位 -链[-1]   +1) //2
            #ceil(.../2)
            # !! [uk*2+链[-1] >= 下界纟后三位]
            #   where uk 是 值纟后一位
    else:
        欤可行冫非星步 = False
    欤可行冫非星步
    #########
    def _is_ok(欤星步, uk, /):
        if not uk >= 下界:
            return
        #if 欤强制降序乊可交换步 and not 欤星步 and not uk*2+链[-1] >= 下界纟后三位:
        if 欤强制降序乊可交换步 and not 欤星步 and not uk >= 下界纟后一位牜非星步:
            #补丁牜下界纟非星步
            return
    #########
    def _iter(欤星步, j, /):
        if j < 0:
            return
        if 欤强制降序乊可交换步 and not 欤星步 and not 欤可行冫非星步:
            #补丁牜下界纟非星步
            return
        uj = 链[j]
        uk = uj*2
        if not _is_ok(欤星步, uk):
            return
        obj = (uk, (j, j))
        yield (obj, [_iter(False, j-1)])
        for i in reversed(range(j)):
            ui = 链[i]
            uk = uj +ui
            if not _is_ok(欤星步, uk):
                return
            obj = (uk, (j, i))
            yield (obj, None)
    def main():
        k = len(链)
        return _iter(True, k-1)
    return main()


def _4next_bounds(sf, 匴, 靶值, 链, st, 后几位, /):
    ok = False
    while 1:
        if 匴.欤加链前缀无效扌(st):
            break
        鬽 = 匴.求取冫鬽下上界纟后几位扌(st, 后几位)
        if None is 鬽:
            break
        (下界纟后一位, 上界纟后一位) = 鬽
        下界纟后一位 = max(下界纟后一位, 后几位+链[-1])
            # => [hp[0].u >= 1+链[-1]]
            # => [链:严序]
        上界纟后一位 = min(上界纟后一位, 靶值)
            # => [hp[0].u <= 靶值]
            # => [链[-1] <= 靶值]
        if not 下界纟后一位 <= 上界纟后一位:
            break
        ok = True
        break
    if not ok:
        return (靶值, 0)
        return (靶值+1, 0)
    return (下界纟后一位, 上界纟后一位)





class 乸匴蛮力搜索器纟最短加链(魖匴蛮力搜索器纟最短加链):
    ___no_slots_ok___ = True
    def __init__(sf, /, *, _毝靶值=-1, _imay_case4starting=-1, _毝假想显链长=-1):
        sf._毝靶值 = _毝靶值
        sf._imay_case4starting = _imay_case4starting
        sf._毝假想显链长 = _毝假想显链长
    @override
    def 罓乊测试扌(sf, /, *, 靶值, case4starting, 假想最小显链长):
        if sf._毝靶值 == 靶值 and sf._imay_case4starting == case4starting and sf._毝假想显链长 == 假想最小显链长:
            raise BaseException('debugging', 靶值, case4starting, 假想最小显链长)
匴蛮力搜索器纟最短加链 = 乸匴蛮力搜索器纟最短加链()










class 乸匴前缀无效判定器纟最短加链牜极简低效(魖匴前缀无效判定器纟最短加链):
    ___no_slots_ok___ = True
    @override
    def 乊搜索起始纟批量处理扌(sf, 靶值, /, *, 欤显示冗杂调试信息, **额外参数):
        '靶值{>=15}{log2(靶值)%1=!=1}{阳爻数{靶值}>=4} -> 状态纟批次 | ^Exception'
        verbose = 欤显示冗杂调试信息
        状态纟批次 = (靶值, verbose)
        return 状态纟批次
    @override
    def 欤强制降序乊可交换步扌(sf, 状态纟批次, /):
        '状态纟批次{靶值} -> bool'
        return True
    @override
    def 保存冫状态纟批次讠部分具名参数扌(sf, 状态纟批次, /):
        '状态纟批次{靶值} -> 部分具名参数{可读性数据}/kwds{.乊搜索起始纟批量处理扌.额外参数}'
        return {}
    @override
    def 乊搜索起始乊假想显链长扌(sf, 状态纟批次, 假想最小显链长, /):
        '状态纟批次{靶值} -> 假想最小显链长 -> Either 最短加链{靶值} 状态纟无效判定 | ^Exception # 起始:[前缀纟最短加链 == [1]]'
        (靶值, verbose) = 状态纟批次
        ls = [靶值]
        while len(ls) <= 假想最小显链长:
            lb = ls[-1]
            ls.append((lb+1)//2)
        assert -1+len(ls) == 假想最小显链长
        ls.reverse()
        址引讠下界 = tuple(ls)
        加链前缀 = (None, 1)
        777;址引纟后一位 = 1 # == len(前缀纟最短加链)
        st = (靶值, 址引讠下界, 加链前缀, 址引纟后一位, verbose)
        if verbose:print_err(f'start: st={st}')
        return mk_Right(st)
    @override
    def 欤加链前缀无效扌(sf, st, /):
        '状态纟无效判定 -> 欤加链前缀无效/bool'
        (靶值, 址引讠下界, 加链前缀, 址引纟后一位, verbose) = st
        #bug:return 靶值 >= 加链前缀[-1] >= 址引讠下界[址引纟后一位-1]
        return not 靶值 >= 加链前缀[-1] >= 址引讠下界[址引纟后一位-1]
    @override
    def 求取冫鬽下上界纟后几位扌(sf, st, 后几位, /):
        '[0 <= 当前显链长 < 假想最小显链长][not 欤加链前缀无效] => 状态纟无效判定 -> 后几位/uint{>=1} -> 鬽 (下界纟后几位, 上界纟后几位)'
        check_int_ge(1, 后几位)
        (靶值, 址引讠下界, 加链前缀, 址引纟后一位, verbose) = st
        return (址引讠下界[址引纟后一位+(后几位-1)], 靶值)
    @override
    def 乊加链前缀增位扌(sf, st, 值纟后一位, 列表纟大小址引纟加数纟后一位, /):
        '[0 <= 当前显链长 < 假想最小显链长][not 欤加链前缀无效][下界纟后一位<=值纟后一位<=上界纟后一位] => 状态纟无效判定 -> 值{后一位} -> 列表纟大小址引纟加数{后一位}/降序[(j,i)] -> 状态纟无效判定'
        (靶值, 址引讠下界, 加链前缀, 址引纟后一位, verbose) = st
        加链前缀 = (加链前缀, 值纟后一位)
        777;址引纟后一位 += 1
        st = (靶值, 址引讠下界, 加链前缀, 址引纟后一位, verbose)
        return st
    @override
    def 乊加链前缀减位扌(sf, st, /):
        '[0 < 当前显链长 <= 假想最小显链长] => 状态纟无效判定 -> 状态纟无效判定'
        (靶值, 址引讠下界, 加链前缀, 址引纟后一位, verbose) = st
        (加链前缀, 值纟后一位) = 加链前缀
        777;址引纟后一位 -= 1
        st = (靶值, 址引讠下界, 加链前缀, 址引纟后一位, verbose)
        return st
匴前缀无效判定器纟最短加链牜极简低效 = 乸匴前缀无效判定器纟最短加链牜极简低效()

def _使用牜极简低效(*args, _毝靶值=-1, _imay_case4starting=-1, _毝假想显链长=-1, _欤添加显链长=False, **kwds):
    _匴蛮力搜索器纟最短加链 = 匴蛮力搜索器纟最短加链 if -1 == _毝靶值 == _imay_case4starting == _毝假想显链长 else 乸匴蛮力搜索器纟最短加链(_毝靶值=_毝靶值, _imay_case4starting=_imay_case4starting, _毝假想显链长=_毝假想显链长)
    鬽最短加链 = _匴蛮力搜索器纟最短加链.蛮力搜索冫最短加链扌(匴前缀无效判定器纟最短加链牜极简低效, *args, **kwds)
    if _欤添加显链长:
        szmm = 0 if 鬽最短加链 is None else 显链长纟(鬽最短加链)
        return (szmm, 鬽最短加链)
    return 鬽最短加链





__all__
from seed.math.power.addition_chain.shortest.search import *
