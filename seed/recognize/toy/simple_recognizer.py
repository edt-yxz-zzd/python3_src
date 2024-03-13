#__all__:goto
# [:本模块使用流程]:goto
# [:本模块引入指令]:goto
# [:本模块测试命令行]:goto
# [:本模块类方法显示命令行]:goto
r'''[[[
e ../../python3_src/seed/recognize/toy/simple_recognizer.py


# [:本模块测试命令行]:here
py -m nn_ns.app.doctest_cmd seed.recognize.toy.simple_recognizer_.test!

seed.recognize.toy.simple_recognizer
py -m nn_ns.app.debug_cmd   seed.recognize.toy.simple_recognizer -x





[[[
===
===
设计局限性:
    由于 假设 解码结果<解码器,全文暨起讫讫> 只有一个 或对或错
    因此 不能支持『左递归』语法
===
命名规范:见:
    view ../../python3_src/useful__cjk_naming.txt

===
交互关联:
    魖解码场景 --> 用户数据纟场景固化
    魖解码场景 --> 全文
    魖解码器 <--> 魖解码场景 <--> 魖辅助构造表达式
    #####
    魖解码场景 处于 核心地位，是 黏合剂
    #####
    魖辅助构造表达式
        通过 魖解码场景 界面 构造 解码器
    #####
    魖解码器
        通过 魖解码场景 界面 访问 全文
        通过 魖解码场景 界面 构造 解码器
    #####

===
TODO:fmap 魖辅助构造表达式
    DONE:罓整理扌
    TODO:_1,_2:参数化 魖辅助构造表达式

===
DONE:乸定域解码器:兼顾式:AND
===
DONE:用户数据:用户数据纟场景固化,用户数据纟全文随行
DONE:分离出:全文暨起讫讫,全文暨讫讫
    更新 乸前瞻零解码器
DONE:前瞻讫地址
    前瞻讫地址冃上限===讫地址纟全文
    解码讫地址冃上限===讫地址乊宽
    [0 <= 起地址纟全文 <= 起地址 <= 讫地址乊严 <= 解码讫地址冃上限===讫地址乊宽 <= 前瞻讫地址冃上限===讫地址纟全文 <= len(全文)]
    其中, 变化最快最多的是『起地址』
        其次是『讫地址乊宽』
            #『讫地址乊严』是 返回值 暨 下一个『起地址』
        再次是『讫地址纟全文』
===
DONE:分裂模块:
e ../../python3_src/seed/recognize/toy/simple_recognizer.py
seed.recognize.toy.simple_recognizer
-->
e ../../python3_src/seed/recognize/toy/simple_recognizer_/test.py
seed.recognize.toy.simple_recognizer_.test
    doctest
e ../../python3_src/seed/recognize/toy/simple_recognizer_/_common.py
seed.recognize.toy.simple_recognizer_._common
    琐碎
e ../../python3_src/seed/recognize/toy/simple_recognizer_/error.py
seed.recognize.toy.simple_recognizer_.error
    异常
e ../../python3_src/seed/recognize/toy/simple_recognizer_/context.py
seed.recognize.toy.simple_recognizer_.context
    乸全文暨讫讫
    乸全文暨起讫讫
e ../../python3_src/seed/recognize/toy/simple_recognizer_/decoder.py
seed.recognize.toy.simple_recognizer_.decoder
    魖解码器
    解码器
e ../../python3_src/seed/recognize/toy/simple_recognizer_/scene.py
seed.recognize.toy.simple_recognizer_.scene
    魖解码场景:依赖于 解码器
    乸解码场景
e ../../python3_src/seed/recognize/toy/simple_recognizer_/expr.py
seed.recognize.toy.simple_recognizer_.expr
    魖辅助构造表达式
===

py -m nn_ns.app.doctest_cmd seed.recognize.toy.simple_recognizer_.test:__doc__
===
grep check_int_ge_le -r ../../python3_src/seed/recognize/toy/simple_recognizer_
ls ../../python3_src/seed/recognize/toy/simple_recognizer_
===
===
py -m nn_ns.app.debug_cmd   seed.recognize.toy.simple_recognizer_.error -x
py -m nn_ns.app.debug_cmd   seed.recognize.toy.simple_recognizer_.context -x
py -m nn_ns.app.debug_cmd   seed.recognize.toy.simple_recognizer_.decoder -x
py -m nn_ns.app.debug_cmd   seed.recognize.toy.simple_recognizer_.scene -x
py -m nn_ns.app.debug_cmd   seed.recognize.toy.simple_recognizer_.expr -x
===
py -m nn_ns.app.doctest_cmd seed.recognize.toy.simple_recognizer_.context:__doc__
py -m nn_ns.app.doctest_cmd seed.recognize.toy.simple_recognizer_.test!
py -m nn_ns.app.doctest_cmd seed.recognize.toy.simple_recognizer_.test:test4context__no_op
py -m nn_ns.app.doctest_cmd seed.recognize.toy.simple_recognizer_.test:test4context__has_op
===
# [:本模块类方法显示命令行]:here
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.recognize.toy.simple_recognizer_.context:乸全文暨起讫讫@T    =T            +exclude_attrs5listed_in_cls_doc
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.recognize.toy.simple_recognizer_.scene:魖解码场景@T    =T      ++exclude_prefixes:_       +exclude_attrs5listed_in_cls_doc
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.recognize.toy.simple_recognizer_.scene:乸解码场景@T    =T      ++exclude_prefixes:_       +exclude_attrs5listed_in_cls_doc
===
]]]

[[
TODO
[[DONE:总结

总结:不可修改类型:类设计:见:_4repr
    唯一:保存:__new__对应__repr__
    其余:__init__:截留:保存.__3
        @property return __3[i]
            eg:_4repr+乸两段式篡改器#乸包装解码器

class _4repr:
    #__slots__ = ()
    def __eq__(sf, ot, /):
        return type(sf) is type(ot) and sf._args == ot._args
    def __repr__(sf, /):
        return repr_helper(sf, *sf._args)
    def __new__(cls, /, *_args):
        sf = super(__class__, cls).__new__(cls)
        sf._args = _args
        return sf
class C(_4repr):
    def __init__(sf, ..., a, b, ..., /):
        sf.__2 = a, b
    @property
    def a(sf, /):
        return sf.__2[0]


总结:构造界面 隔离 具现类型:见:魖解码场景<:魖工厂场景 +魖注册处
    匴场景包/场景 是 什么？
    匴一揽子构造函数包
        +匞参数配置
            ::固化变量
        +注册变量(公|私)
            ::只增变量
    [场景 作为 构造界面:起到 隔离 具现类型 的作用] ==>>这其实就是 工厂！！
class 魖工厂场景(ABC):#魖工厂#魖场景
    @abstractmethod
    def 构造冫某某某扌(sf, a, b, /):
        '使用:聚合式参数'
        return 乸某某某(a,b)
    def 构造冫某某某灬扌(sf, s4a, t4a, b, /):
        '使用:离散式参数'
        a = mk_a_(s4a, t4a)
        return sf.构造冫某某某扌(a,b)
]]

DONE:囗->冫
    grep 囗 ../../python3_src/seed/recognize/toy/simple_recognizer_/*.py -1
    %s/\(\<\(取\|注册\|罓\?检查\|欤已注册\|构造\)\)\@<=囗/冫/g

DONE:小类 移动至:basic.py register.py



DONE
设计 表达式 对应于:包装解码器、变换讫错果解码器
魖讫错果变换器
    乸讫错果变换器
    惑构造冫讫错果变换器扌
魖两段式篡改器
    乸两段式篡改器
DONE
新类型测试+更新流程
    乸具名引用变量
    变果式 >>
    * 魖讫错果变换器(:: non_callable)
    * 魖两段式篡改器(:: non_callable)
    * 乸具名引用变量(:: non_callable)
    乸讫错果变换器
    惑构造冫讫错果变换器扌
    乸两段式篡改器

取消TODO
??鬽名 彧名 与__name__
    算了，没必要

取消TODO
??尾限式 / // --> * **
    但是 *,** 优先级不同


TODO:grammar:半括号:
    a + b . * x * y . * z
    ((a + b ) * x * y ) * z
    a + b . * x + y . * z
    ((a + b ) * x + y ) * z
    禁止: a * . x . * z
        a * ( x ) * z
        另一半必须在端点
    ######################
    expr = expr op expr
    expr = id
    expr = expr m_rexpr
    m_rexpr = m_rexpr op expr
    m_rexpr = .
    expr = lexpr_m expr
    lexpr_m = expr op lexpr_m
    lexpr_m = .
    ######################
    left corner
        全文随行.{(优先并联解码器,分支号,起地址,讫地址乊宽):彧讫错果)}
            发现 重入 则 下一分支
            不太对，这样只有 两层，看来 还得 循环...
TODO
全文+最大访问地址
]]



seed.recognize.toy.simple_recognizer
py -m nn_ns.app.debug_cmd   seed.recognize.toy.simple_recognizer -x
py -m nn_ns.app.doctest_cmd seed.recognize.toy.simple_recognizer:__doc__
py -m nn_ns.app.doctest_cmd seed.recognize.toy.simple_recognizer:__doc__

py -m nn_ns.app.doctest_cmd seed.recognize.toy.simple_recognizer:__doc__  -ff -v --ndiff

py_adhoc_call   seed.recognize.toy.simple_recognizer   @f
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.recognize.toy.simple_recognizer:XXX@T    =T      ++exclude_prefixes:_       +exclude_attrs5listed_in_cls_doc








#]]]'''
__all__ = r'''
定长式
码集式
常量式
失败式
成功式
空式
引用式
at
构造冫具名函数扌
乸具名函数
乸具名码集
乸具名引用变量
乸两段式篡改器
惑构造冫讫错果变换器扌
变换器冫取原文片段
惑构造冫结果变换器扌


魖解码场景
乸解码场景
构造冫解码场景扌


取冫变量值扌
注册冫变量名纟公用扌
注册冫变量名纟私用扌
乸私用空间
乸具名私用空间
乸私钥
乸具名私钥


构造冫解码器巛名扌
注册冫解码器名纟公用扌
注册冫解码器名纟私用扌


构造冫全文暨起讫讫扌
乸具名全文
构造冫具名全文暨起讫讫扌
乸具名全文冖冖记录讫地址


检查冫讫错果扌
检查冫讫错果冖扩展扌
'''.split()#'''
__all__


# [:本模块使用流程]:here
######################
######################
######################
#别的并不特别需要:共计7步骤:
#   ######################
#   ######################
#   1. 构建 表达式(eg:常量式,引用式)/.整理扌 #at,构造冫具名函数扌,乸具名函数,乸具名码集
#   2. 构建 场景:构造冫解码场景扌(鬽名=...)
#   3. 注册 变量 以使用 乸具名引用变量:注册冫变量名纟公用扌,注册冫变量名纟私用扌#取冫变量值扌#乸私用空间,乸具名私用空间,乸私钥,乸具名私钥
#       注册冫变换结果函数纟具名解码器扌,取冫变换结果函数纟具名解码器扌#具名扌
#   4. 构建 解码器:表达式(场景),场景.引用扌/.具名扌/.包装扌
#       具名式/.具名扌:设定:场景.欤自动注册冫具名解码器/.欤自动变换结果冫具名解码器#公钥纟欤自动注册冫具名解码器,公钥纟欤自动变换结果冫具名解码器,注册冫变量名纟公用扌
#   5. 注册 解码器 以使用 引用式:注册冫解码器名纟公用扌,注册冫解码器名纟私用扌#构造冫解码器巛名扌(场景,解码器名)
#   6. 构建 全文暨起讫讫:构造冫全文暨起讫讫扌, 乸具名全文, 构造冫具名全文暨起讫讫扌,乸具名全文冖冖记录讫地址
#   7. 解码:解码器.宽解码扌(全文暨起讫讫)/.严解码乊容错扌/.严解码乊不容错扌
#   ######################
#   ######################
if 1:
    # copy from: ..._/.test.py
    ######################
    ######################
    ######################
    # 构造 表达式:
    from seed.recognize.toy.simple_recognizer_.expr import 定长式,码集式,常量式,失败式,成功式,空式,引用式
    from seed.recognize.toy.simple_recognizer_.basic import at,构造冫具名函数扌,乸具名函数,乸具名码集
    from seed.recognize.toy.simple_recognizer_.basic import 乸具名引用变量,乸两段式篡改器,惑构造冫讫错果变换器扌,变换器冫取原文片段#乸讫错果变换器
    from seed.recognize.toy.simple_recognizer_.basic import 惑构造冫结果变换器扌#乸错果变换器,乸结果变换器,

    # 构造 场景:
    from seed.recognize.toy.simple_recognizer_.scene import 魖解码场景, 乸解码场景, 构造冫解码场景扌

    # 注册 变量:
    #   特别是:乸具名引用变量.变量名
    #   命名规范:变量名『变量冫某某』;;连锁引用:变量名<乸具名引用变量>『引用冫某某』
    from seed.recognize.toy.simple_recognizer_.scene import 具名扌,注册冫变换结果函数纟具名解码器扌,取冫变换结果函数纟具名解码器扌
    from seed.recognize.toy.simple_recognizer_.scene import 取冫变量值扌,注册冫变量名纟公用扌,注册冫变量名纟私用扌
    from seed.recognize.toy.simple_recognizer_.scene import 乸私用空间,乸具名私用空间,乸私钥,乸具名私钥

    # 构造 解码器 并 注册:
    from seed.recognize.toy.simple_recognizer_.scene import 构造冫解码器巛名扌,注册冫解码器名纟公用扌,注册冫解码器名纟私用扌

    # 构造 输入纟解码:
    from seed.recognize.toy.simple_recognizer_.context import 构造冫全文暨起讫讫扌, 乸具名全文, 构造冫具名全文暨起讫讫扌,乸具名全文冖冖记录讫地址
    # 最后:解码 并 检查: 解码器.宽解码扌
    from seed.recognize.toy.simple_recognizer_.basic import 检查冫讫错果扌,检查冫讫错果冖扩展扌

######################
######################
######################






























def __():
    from seed.tiny import null_tuple
    from enum import Enum, auto
    class __:
        @property
        def 欤结束(sf, /):
            return sf._欤结束
        @property
        def 欤开始(sf, /):
            return sf._欤开始
        @property
        def 欤失败(sf, /):
            return sf._欤失败
        @property
        def 欤匹配(sf, /):
            return sf._欤匹配
        @property
        def 欤锁定(sf, /):
            return sf._欤锁定
        @property
        def 欤有前(sf, /):
            return sf._欤有前
        @property
        def 欤有后(sf, /):
            return sf._欤有后
        @property
        def 所有前驱(sf, /):
            return sf._所有前驱
        @property
        def 所有后继(sf, /):
            return sf._所有后继
        @property
        def 欤任意(sf, /):
            return sf._欤任意
        @property
        def 欤必须零(sf, /):
            return sf._欤必须零
        @property
        def 欤禁止零(sf, /):
            return sf._欤禁止零
        @property
        def 欤仍需继续检测乊串联(sf, /):
            return sf._欤仍需继续检测乊串联

    class 筐允零首锁定况型(Enum, __):
        #[:锁定况态]:goto
        匡锁定前失败 = auto()
        匡锁定暨匹配 = auto()
        匡允零首锁定 = auto()

        匡锁定后失败 = auto()
        匡锁定后匹配 = auto()


    class 筐首非零锁定况型(Enum, __):
        #[:锁定况态]:goto
        匡非零锁定前失败 = auto() #任意

        匡零锁定暨匹配 = auto() #必须零
            #欤仍需继续检测乊串联
        匡非零锁定暨匹配 = auto() #禁止零
        匡非零锁定暨返回起地址暨匹配 = auto() #必须零

        匡非零锁定 = auto() #禁止零
        匡非零锁定暨返回起地址 = auto() #必须零

        匡非零锁定后失败 = auto() #任意
        匡非零锁定后匹配 = auto() #任意#<<==乸前瞻零解码器
        #xxx匡首非零锁定后匹配暨返回起地址

    def _get(cls, s, /):
        return tuple(getattr(cls, nm) for nm in s.split())
    def _init(cls, 所有前驱, 所有后继, /):
        所有前驱 = _get(cls, 所有前驱)
        所有后继 = _get(cls, 所有后继)
        for x in cls:
            x._所有前驱 = null_tuple
            x._所有后继 = null_tuple
        for x in 所有后继:
            x._所有前驱 = 所有前驱
        for x in 所有前驱:
            x._所有后继 = 所有后继


        for x in cls:
            x._欤有后 = bool(所有后继)
            x._欤有前 = bool(所有前驱)
            x._欤结束 = not x.欤有后
            x._欤开始 = not x.欤有前
            assert x.欤结束 or x.欤开始

            x._欤失败 = '失败' in x.name
            x._欤匹配 = '匹配' in x.name
            x._欤锁定 = x.欤开始 and not x.欤失败
            assert x.欤结束 or x.欤锁定
            assert not (x.欤失败 and x.欤锁定)

    def _init1():
        cls = 筐允零首锁定况型
        for x in cls:
            x._欤任意 = True
            x._欤禁止零 = False
            x._欤必须零 = False
            x._欤仍需继续检测乊串联 = False
        for x in cls:
            assert sum([x.欤任意, x.欤必须零, x.欤禁止零]) == 1
    def _init2():
        cls = 筐首非零锁定况型
        for x in cls:
            x._欤任意 = not x.欤锁定
            x._欤禁止零 = x.欤锁定 and '非零' in x.name and not '返回' in x.name
            x._欤必须零 = x.欤锁定 and not x.欤禁止零
            x._欤仍需继续检测乊串联 = False
        cls.匡零锁定暨匹配._欤仍需继续检测乊串联 = True
        for x in cls:
            assert sum([x.欤任意, x.欤必须零, x.欤禁止零]) == 1
    _init(筐允零首锁定况型, '匡允零首锁定', '匡锁定后失败 匡锁定后匹配')
    _init(筐首非零锁定况型, '匡非零锁定 匡非零锁定暨返回起地址', '匡非零锁定后失败 匡非零锁定后匹配')
    _init1()
    _init2()
    def _况型扌(允零首锁定丷首非零锁定, /):
        if 允零首锁定丷首非零锁定:
            T = 筐首非零锁定况型
        else:
            T = 筐允零首锁定况型
        return T

if 1:
    from seed.recognize.toy.simple_recognizer_.expr_generator__2nd import 生成冫展符讠表达式纟解码器纟子语言纟圁訄乙版扌


__all__
# [:本模块引入指令]:here
######################
# 使用已有的句法解码器:
# 生成 句法树+表达式:
from seed.recognize.toy.simple_recognizer import 生成冫展符讠表达式纟解码器纟子语言纟圁訄乙版扌
# 操作 句法树: 句法树.解码扌/.树变换扌
#
######################
######################
# 从零开始，构建解码器:
######################
# 构造 表达式:
from seed.recognize.toy.simple_recognizer import 定长式,码集式,常量式,失败式,成功式,空式,引用式
from seed.recognize.toy.simple_recognizer import at,构造冫具名函数扌,乸具名函数,乸具名码集
from seed.recognize.toy.simple_recognizer import 乸具名引用变量,乸两段式篡改器,惑构造冫讫错果变换器扌,变换器冫取原文片段#乸讫错果变换器
from seed.recognize.toy.simple_recognizer import 惑构造冫结果变换器扌#乸错果变换器,乸结果变换器,

# 构造 场景:
from seed.recognize.toy.simple_recognizer import 魖解码场景, 乸解码场景, 构造冫解码场景扌

# 注册 变量:
#   特别是:乸具名引用变量.变量名
#   命名规范:变量名『变量冫某某』;;连锁引用:变量名<乸具名引用变量>『引用冫某某』
from seed.recognize.toy.simple_recognizer import 具名扌,注册冫变换结果函数纟具名解码器扌,取冫变换结果函数纟具名解码器扌
from seed.recognize.toy.simple_recognizer import 取冫变量值扌,注册冫变量名纟公用扌,注册冫变量名纟私用扌
from seed.recognize.toy.simple_recognizer import 乸私用空间,乸具名私用空间,乸私钥,乸具名私钥

# 构造 解码器 并 注册:
from seed.recognize.toy.simple_recognizer import 构造冫解码器巛名扌,注册冫解码器名纟公用扌,注册冫解码器名纟私用扌

# 构造 输入纟解码:
from seed.recognize.toy.simple_recognizer import 构造冫全文暨起讫讫扌, 乸具名全文, 构造冫具名全文暨起讫讫扌,乸具名全文冖冖记录讫地址
# 最后:解码 并 检查: 解码器.宽解码扌
from seed.recognize.toy.simple_recognizer import 检查冫讫错果扌,检查冫讫错果冖扩展扌

######################
from seed.recognize.toy.simple_recognizer import *
