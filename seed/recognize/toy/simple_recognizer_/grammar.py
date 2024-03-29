#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/toy/simple_recognizer_/grammar.py
%s/语法/句法/g
[[
view ../../python3_src/useful__cjk_naming.txt
    [:非汉字部件环境冫标识命名规范]:goto
    [:命名规范冫句法分析]:goto
    [:区别冖冖纟匕]:goto
######################
copy from:[:命名规范冫句法分析]
######################
冊cè同“册”。
訄qiú逼迫。
圁:yín古水名/古地名
#####
圁爻爻语言
  圁訄叕叕句法语言
  『圁』:指『语言』
  『訄』:指『句法语言/元语言』
#####
冊乂乂文本匕圁爻爻语言 :: 冊乂乂文本{圁爻爻语言}
#xxx冊圁爻爻语言句法文本匕圁訄叕叕句法语言 :: 冊圁爻爻语言句法文本{圁訄叕叕句法语言}
冊句法文本纟圁爻爻语言匕圁訄叕叕句法语言 :: 冊句法文本纟圁爻爻语言{圁訄叕叕句法语言}
解码器 :: 冊乂乂文本{圁爻爻语言} -> 解码结果
句法分析器 :: 冊句法文本纟圁爻爻语言{圁訄叕叕句法语言} -> 基符讠解码器/{基符:解码器纟基符} -> 冊乂乂文本{圁爻爻语言} -> 句法树{圁爻爻语言}
句法树 = 叶节点纟基符 | 叉节点纟展符
叶节点纟基符 = 乸叶节点 基符 解码结果纟基符
叉节点纟展符 = 乸叉节点 展符 (自由容器 句法树)
自由容器 a = a | [自由容器 a]
树解码器 :: 展符讠变换器/{展符:变换器} -> 基符讠变换器/{基符:变换器} -> 句法树{圁爻爻语言} -> 解码结果
句法解码器 =[def]= 句法分析器 >>> 树解码器
句法解码器 :: 冊句法文本纟圁爻爻语言{圁訄叕叕句法语言} -> 展符讠变换器/{展符:变换器} -> 基符讠变换器/{基符:变换器} -> 基符讠解码器/{基符:解码器纟基符} -> 冊乂乂文本{圁爻爻语言} -> 解码结果
解码器纟基符 :: 文本 -> 起讫讫 -> 讫错果 ##-->解码结果纟基符
变换器 :: 自由容器 解码结果 -> 解码结果
#####
######################
.. 文本in某语言
.. 某某某语言句法文本in某句法语言
######################
]]
[[
view ../../python3_src/useful__cjk_naming.txt
    [:区别冖冖纟匕]:goto
######################
copy from:[:区别冖冖纟匕]
######################
===
区别冖冖纟匕:4纟,6匕
[:命名规范冫句法分析]:goto
冊句法文本纟圁爻爻语言匕圁訄叕叕句法语言 :: 冊句法文本纟圁爻爻语言{圁訄叕叕句法语言}
冊句法纟乙匕甲
    冊句法纟乙:
        句法文本 的内容 描述 乙语言 的 句法
    冊句法匕甲:
        句法文本 的格式 符合 甲语言 的 句法
]]



seed.recognize.toy.simple_recognizer_.grammar
py -m seed.recognize.toy.simple_recognizer_.grammar
py -m nn_ns.app.debug_cmd   seed.recognize.toy.simple_recognizer_.grammar -x
py -m nn_ns.app.doctest_cmd seed.recognize.toy.simple_recognizer_.grammar:__doc__
py_adhoc_call   seed.recognize.toy.simple_recognizer_.grammar   @f
from seed.recognize.toy.simple_recognizer_.grammar import *
#]]]'''
__all__ = r'''
展符名讠变果扌冖冖圁訄甲版
解码器纟构造辅助表达式纟句法书冖冖圁訄甲版
宽解码冃辅助表达式巛冊句法文本匕圁訄甲版扌


















may_int5smay_
add_
con4str_
con_
the_one_
fst
snd
echo
空白字集式
空白
标识首字集式
标识体字集式
标识冖无尾随空白
标识
数字集式
基符首字集式
基符
展符名
展符
函数名
定义符
行首
变换乊左侧
变换序列乊左侧
原子表达式
允空数
数量范围
重复表达式
后缀表达式
串联表达式
锁定表达式
优选表达式
互斥表达式
表达式
定义行冖无首
定义行
句法书
call__
展符名讠变果扌冖冖圁訄甲版
解码器纟构造辅助表达式纟句法书冖冖圁訄甲版
宽解码冃辅助表达式巛冊句法文本匕圁訄甲版扌



may5tmay_
join_
mk_bool
mk_int
整数冖无尾随空白
整数
元素纟字符串常量冖无尾随空白
跳过纟双引号纟字符串常量冖无尾随空白
跳过纟单引号纟字符串常量冖无尾随空白
跳过纟字符串常量冖含原貌冖无尾随空白
文本纟字符串常量冖含原貌冖无尾随空白
字符串常量冖部分
字符串常量
基符名
变换冫变果式
拆包符
数目纟拆包符
常量表达式
空表达式
允空表达式
括号表达式
尾限
尾限暨变换乊右侧
前瞻符
反转符
忽略符
前缀符
前缀符序列
前缀表达式
'''.split()#'''
__all__
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
from seed.recognize.toy.simple_recognizer import 取冫变量值扌,注册冫变量名纟公用扌,注册冫变量名纟私用扌
from seed.recognize.toy.simple_recognizer import 乸私用空间,乸具名私用空间,乸私钥,乸具名私钥

# 构造 解码器 并 注册:
from seed.recognize.toy.simple_recognizer import 构造冫解码器巛名扌,注册冫解码器名纟公用扌,注册冫解码器名纟私用扌

# 构造 输入纟解码:
from seed.recognize.toy.simple_recognizer import 构造冫全文暨起讫讫扌, 乸具名全文, 构造冫具名全文暨起讫讫扌
# 最后:解码 并 检查: 解码器.宽解码扌
from seed.recognize.toy.simple_recognizer import 检查冫讫错果扌,检查冫讫错果冖扩展扌

######################
from ast import literal_eval
from seed.recognize.toy.simple_recognizer_.basic import the_one_
from seed.recognize.toy.simple_recognizer_.basic import 数字表,标识体字集,标识首字集,空白字集

__all__
变换器冫取原文片段
def may5tmay_(tmay, /):
    if tmay:
        [i] = tmay
        return i
    return None
def may_int5smay_(smay, /):
    if smay:
        s = smay
        return int(s)
    return None
def add_(x_y, /):
    x, y = x_y
    return x+y
con4str_ = add_
def con_(x_xs, /):
    try:
        x, xs = x_xs
        return (x, *xs)
    except ValueError as e:
        raise ValueError(len(x_xs), x_xs) from e
def join_(lsls, /):
    xs = []
    for ls in lsls:
        xs.extend(ls)
    return xs

fst = at[0]
snd = at[1]
def echo(x,/):
    return x
echo = 乸具名函数('echo', echo)
#xxx:mk_bool = 构造冫具名函数扌(..., bool)
mk_bool = 构造冫具名函数扌('bool', lambda x:bool(x))
    #<<==:
    #ValueError: no signature found for builtin type <class 'bool'>
mk_int = 构造冫具名函数扌('int', lambda x:int(x))
    #<<==:
    #ValueError: no signature found for builtin type <class 'int'>
#con_ = 构造冫具名函数扌(..., con_)


######################

__all__
#class Global:
class 匴解码器表达式包纟圁訄甲版右递归句法语言:
    '圁訄甲版右递归句法语言#具名展符外赋结果变换器#两段式解码冫先锁定再解码#不支持左递归'
    引用名纟表达式 = '解码器纟表达式'
    _get_nms = globals
    _get_nms = locals
    _名前 = 000
    _名前 = set(_get_nms())
    ######################
    #构造 魖辅助表达式
    ######################
    ###以下:统一 空白 结尾
    ### ==>> 任何 展式 都是 空白 结尾
    ###         例外:空白字集式
    ###         例外:*冖无尾随空白
    空白字集式 = 码集式(空白字集) >> '空白字集式'
    空白 = -(-空白字集式[1:] | -常量式('#') + 定长式(1)//常量式('\n'))[:] >> '空白'
    标识首字集式 = 码集式(标识首字集) >> '标识首字集式'
    标识体字集式 = 码集式(标识体字集) >> '标识体字集式'
    标识冖无尾随空白 = 标识首字集式 + 标识体字集式[:]%''.join >>con4str_
    标识 = 标识冖无尾随空白 + -空白 >>the_one_ >> '标识'

    数字集式 = 码集式(数字表) >> '数字集式'
    整数冖无尾随空白 = 数字集式[1:]%''.join >> '整数冖无尾随空白'
    整数 = 整数冖无尾随空白 + -空白 >>the_one_ >> mk_int >> '整数'

    元素纟字符串常量冖无尾随空白 = -(常量式("\\")[:1] + 定长式(1)) >> '元素纟字符串常量'
    跳过纟双引号纟字符串常量冖无尾随空白 = -常量式('"') + -(元素纟字符串常量冖无尾随空白) // 常量式('"') >>'跳过纟双引号纟字符串常量冖无尾随空白'
    跳过纟单引号纟字符串常量冖无尾随空白 = -常量式("'") + -(元素纟字符串常量冖无尾随空白) // 常量式("'") >>'跳过纟单引号纟字符串常量冖无尾随空白'
    跳过纟字符串常量冖含原貌冖无尾随空白 = -常量式('r')[:1] + (跳过纟单引号纟字符串常量冖无尾随空白 | 跳过纟双引号纟字符串常量冖无尾随空白) >>'跳过纟字符串常量冖含原貌冖无尾随空白'
    文本纟字符串常量冖含原貌冖无尾随空白 = 跳过纟字符串常量冖含原貌冖无尾随空白 >> 变换器冫取原文片段 >> '文本纟字符串常量冖含原貌冖无尾随空白'
    字符串常量冖部分 = 文本纟字符串常量冖含原貌冖无尾随空白 + -空白 >>the_one_ >>literal_eval >> '字符串常量冖部分'
    字符串常量 = 字符串常量冖部分[1:] >>''.join >> '字符串常量'

    if 0:
        #基符首字集式 = (码集式(小写字母表) | 码集式('`丶灬罒艹冖凵囿槑魅')) >> '基符首字集式'
        基符名 = -+基符首字集式 >> 标识 >>the_one_ >> '基符名'
    else:
        基符首字集式 = 码集式('`') >> '基符首字集式'
        基符名 = -基符首字集式 >> 标识 >>the_one_ >> '基符名'
    展符名 = +标识首字集式 + +~基符首字集式 >> 标识 >>snd >> '展符名'
    基符 = 基符名 >> '基符'
    展符 = 展符名 >> '展符'
    函数名 = 标识 >> '函数名'

    定义符 = -常量式('=') + -空白 >> '定义符'
    行首 = -常量式(';') + -空白 >> '行首'
    变换冫变果式 = -常量式('%') + -空白 + 函数名 >>the_one_ >> '变换冫变果式'
        #乸具名引用变量:...
    拆包符 = -常量式('!') + -空白 >> '拆包符'
    数目纟拆包符 = 拆包符[:]%len >> '数目纟拆包符'
    变换乊左侧 = 变换冫变果式 + 数目纟拆包符 >> '变换乊左侧'
    变换序列乊左侧 = 变换乊左侧[:] >> '变换序列乊左侧'
    #参数化模板? join
    '乸具名引用变量(彧鬽名, 鬽变量类型, 参数数目, 变量名)'
    常量表达式 = 字符串常量 >> '常量表达式'
    空表达式 = 空式 >> '空表达式'
    允空表达式 = (引用式(True, 引用名纟表达式) | 空表达式) >> '允空表达式'
    括号表达式 = -常量式('(') + -空白 + 允空表达式 + -常量式(')') + -空白 >>the_one_ >> '括号表达式'
    原子表达式 = (基符 | 展符 | 常量表达式 | 括号表达式) >> '原子表达式'
    允空数 = 整数[:1] >>may5tmay_ >> '允空数'
    数量范围 = -常量式('[') + -空白 + -+~常量式(']') + 允空数 + (-常量式(':') + -空白 + 允空数 >>the_one_)[:1] + -常量式(']') + -空白 >>con_ >> '数量范围'
    重复表达式 = 原子表达式 + 数目纟拆包符 + 数量范围[:] >> '重复表达式'
    尾限 = 常量式('/')[1:2]%len + -空白 + 重复表达式 >> '尾限'
    尾限暨变换乊右侧 = (变换乊左侧 | 尾限) >> '尾限暨变换乊右侧'
    后缀表达式 = 重复表达式 + 尾限暨变换乊右侧[:] >> '后缀表达式'
    前瞻符 = -常量式('+') + -空白 >>变换器冫取原文片段 >>fst >> '前瞻符'
    反转符 = -常量式('~') + -空白 >>变换器冫取原文片段 >>fst >> '反转符'
    忽略符 = -常量式('-') + -空白 >>变换器冫取原文片段 >>fst >> '忽略符'
    前缀符 = (前瞻符 | 反转符 | 忽略符) >> '前缀符'
    ###前缀符 = (前瞻符 | 反转符 | 忽略符)>>变换器冫取原文片段 >>fst >> '前缀符'
    前缀符序列 = 前缀符[:] >> '前缀符序列'
    #欤出现忽略符 = 忽略符[:1]%bool >> '欤出现忽略符'
        # 1-->None:
    #欤出现忽略符 = 忽略符[:]%bool >> '欤出现忽略符'
        #ValueError: no signature found for builtin type <class 'bool'>
    #欤出现忽略符 = 忽略符[:]%mk_bool >> '欤出现忽略符'
    #可忽略表达式 = 欤出现忽略符 + 后缀表达式 >> '可忽略表达式' #  >>echo
    前缀表达式 = 前缀符序列 + 后缀表达式 >> '前缀表达式' #  >>echo
        # 具名后 可省略echo:
        # 这里 echo:原因见下:
    串联表达式 = 前缀表达式 + (-常量式('+') + -空白 + 前缀表达式 >>the_one_)[:] >>con_ >> '串联表达式'
        #由于 (+) 平坦化/扁平化: 为避免 前缀表达式/可忽略表达式 被拆开，必须 不是 串联
    锁定表达式 = 串联表达式 + (-常量式('>>') + -空白 + 串联表达式 >>the_one_)[:1] >>con_ >> '锁定表达式'
    优选表达式 = 锁定表达式 + (-常量式('|') + -空白 + 锁定表达式 >>the_one_)[:] >>con_ >> '优选表达式'
    互斥表达式 = 优选表达式 + (-常量式('^') + -空白 + 优选表达式 >>the_one_)[:] >>con_ >> '互斥表达式'
    表达式 = 互斥表达式 >> '表达式'
    定义行冖无首 = 前缀符序列 + 展符名 + 数目纟拆包符 + 变换序列乊左侧 + -定义符 + 表达式 >>'定义行冖无首'
    定义行 = 定义行冖无首 + -行首[1:] >>the_one_ >>'定义行'
    句法书 = -空白 + -行首[1:] + 定义行//常量式('.') >>the_one_ >>'句法书'
    ######################
    _名后 = set(_get_nms())
    _名集 = _名后 -_名前
#end-class Global:
#end-class 匴解码器表达式包纟圁訄甲版右递归句法语言:
######################
if __name__ == '__main__':
    from seed.recognize.toy.simple_recognizer_.grammar import *

######################
def __():
    匴 = 匴解码器表达式包纟圁訄甲版右递归句法语言
    句法书,表达式,引用名纟表达式 = 匴.句法书,匴.表达式,匴.引用名纟表达式
    ######################
    from seed.recognize.toy.simple_recognizer_.context import 乸具名全文冖冖记录讫地址
    from seed.recognize.toy.simple_recognizer_.scene import 具名扌,注册冫变换结果函数纟具名解码器扌,取冫变换结果函数纟具名解码器扌

    场景 = 构造冫解码场景扌(鬽名='场景')
    #场景.注册冫变量名纟公用扌(场景.公钥纟欤自动注册冫具名解码器, True)
    #场景.注册冫变量名纟公用扌(场景.公钥纟欤自动变换结果冫具名解码器, True)
    场景.欤自动注册冫具名解码器 = True
    场景.欤自动变换结果冫具名解码器 = True
    场景.注册冫变换结果函数纟具名解码器扌('句法书', lambda x:(99999, x))
    ######################
    ######################

    场景.注册冫解码器名纟公用扌(引用名纟表达式, 表达式(场景))
    解码器纟句法书 = 句法书(场景)
    ######################
    ######################
    # [:命名规范冫句法分析]:goto
    def 甲版解码扌(名纟文本, 句法文本纟圁訄甲版, /):
        全文 = 乸具名全文冖冖记录讫地址(名纟文本, None, 句法文本纟圁訄甲版, 0)
        全文暨起讫讫 = 构造冫全文暨起讫讫扌(全文, 0, None, None)
        r = 解码器纟句法书.宽解码扌(全文暨起讫讫)
        ##讫地址 在 解码后
        讫地址纟已访问纟全文 = 全文.讫地址纟已访问
        return 讫地址纟已访问纟全文, r
    ######################
    ######################
    讫地址纟已访问纟全文, r = 甲版解码扌(名纟文本:='单行', 句法文本:='; a = b;.')
    if 0:
        assert r == (2, False, (3, False, 'a')), r
    if 0:
        #now:++行首@尾部:
        assert r == (2, True, (99999, [])), r
        assert 讫地址纟已访问纟全文 == 3
            #错在: 展符 首字母大写
    if 1:
        #now:++『`』作为 基符首字:
        assert r == (9, True, (99999, [[[], 'a', 0, [], (((([[], [['b', 0, []], []]],),),),)]])), r
        assert 讫地址纟已访问纟全文 == 9
    ######################
    ######################
    讫地址纟已访问纟全文, r = 甲版解码扌(名纟文本:='单行', 句法文本:='; a=;.')
    if 1:
        # [表达式 =!= 允空表达式]
        #   <<== 前瞻符 避免 (x+ +y)-->(x+()+y)
        assert r == (5, False, (';',)), r
        assert 讫地址纟已访问纟全文 == 5
    讫地址纟已访问纟全文, r = 甲版解码扌(名纟文本:='单行', 句法文本:=';a =( );.')
    if 1:
        # [表达式 =!= 允空表达式]
        #   <<== 前瞻符 避免 (x+ +y)-->(x+()+y)
        assert r == (9, True, (99999, [[[], 'a', 0, [], (((([[], [[None, 0, []], []]],),),),)]])), r
        assert 讫地址纟已访问纟全文 == 9
    ######################
    ######################
    #讫地址纟已访问纟全文, r = 甲版解码扌(名纟文本:='单行', 句法文本:='; A = b')
    讫地址纟已访问纟全文, r = 甲版解码扌(名纟文本:='单行', 句法文本:=r'; A = b0 + "\"." ;.')
    if 0:
        assert r == (7, True, (99999, [['A', 0, [], (((([0, [['b', []], []]],),),),)]])), r
        assert 讫地址纟已访问纟全文 == 7
    if 1:
        assert r == (19, True, (99999, [[[], 'A', 0, [], (((([[], [['b0', 0, []], []]], [[], [['".', 0, []], []]]),),),)]])), r
        assert 讫地址纟已访问纟全文 == 19
    ######################
    ######################
    讫地址纟已访问纟全文, r = 甲版解码扌(名纟文本:='两行', 句法文本:=' ; ; Aaaa%f%f = -b[2][3:]%g/h//h%g + (t^u)[:4] >> s | d ^ e ;B != c000 ; # xxx \n  \n ; . xxxxx,,,')
    if 0b000:
        print(句法文本[:69])
    assert r == (87, True, (99999, [[[], 'Aaaa', 0, [['f', 0], ['f', 0]], (((([['-'], [['b', 0, [(2,), (3, None)]], [['g', 0], [1, ['h', 0, []]], [2, ['h', 0, []]], ['g', 0]]]], [[], [[(((([[], [['t', 0, []], []]],),),), ((([[], [['u', 0, []], []]],),),)), 0, [(None, 4)]], []]]), ([[], [['s', 0, []], []]],)), (([[], [['d', 0, []], []]],),)), ((([[], [['e', 0, []], []]],),),))], [[], 'B', 1, [], (((([[], [['c000', 0, []], []]],),),),)]])), r
    assert 讫地址纟已访问纟全文 == 87
    assert 句法文本[87-1] == '.'
    assert len(句法文本) == 96
    ######################
    ######################
if __name__ == '__main__':
    __()
######################
######################
#_名集
def call__(n, f, /):
    def call_(args, /):
        args = (*args,)
        assert len(args) == n, (n, args)
        return f(*args)
    return call_
def __():
    匴 = 匴解码器表达式包纟圁訄甲版右递归句法语言
    _名集 = 匴._名集
    from seed.tiny_.dict__add_fmap_filter import dict_add__new, filter4dict_key
    from seed.recognize.toy.simple_recognizer_.expr import 具名式,串联式,首选式,锁隙式,独尊式,前瞻式,反转式,忽略式
    if 0:
        for 名 in sorted(_名集): print(名)
    def 拆包扌(表达式, 数目纟拆包符, /):
        for _ in range(数目纟拆包符):
            表达式 %= the_one_
        return 表达式
    def 构造冫变果式扌(表达式, f, 数目纟拆包符, /):
        return 拆包扌(表达式%f, 数目纟拆包符)
    def 构造冫尾限式扌(e, n, te, /):
        if n == 1:
            e /= te
        elif n == 2:
            e //= te
        else:
            raise 000
        return e
    nms = 000
    nms = set(locals())
    基符 = lambda 名:引用式(True, 名)
    展符 = lambda 名:引用式(True, 名)
    函数名 = lambda 名:乸具名引用变量(名, None, 1, 名)
    def 数量范围(xs, /):
        if len(xs) == 1:
            [i] = xs
            return i
        mi, mj = xs
        return slice(mi,mj,None)
    常量表达式 = 常量式
    空表达式 = lambda _:空式
    原子表达式 = lambda e:e%echo
        #阻止 表达式 越界 整理！
    def 重复表达式(xs, /):
        e,n,ks = 原子表达式,数目纟拆包符,列表纟数量范围 = xs
        e = 拆包扌(e, 数目纟拆包符)
        for k in ks:
            e = e[k]
        return e
    def 后缀表达式(xs, /):
        e, ts = 重复表达式, 列表纟变换暨尾限 = xs
        for t in ts:
            T = type(t)
            assert T is list
            x,y = t
            if type(x) is int:
                n, te = 尾限 = t
                e  = 构造冫尾限式扌(e, n, te)
            elif type(x) is 乸具名引用变量 and type(y) is int:
                f, 数目纟拆包符 = 变换乊左侧 = t
                e = 构造冫变果式扌(e, f, 数目纟拆包符)
            else:
                raise 000
        return e
    前瞻符 = lambda ch:前瞻式
    反转符 = lambda ch:反转式
    忽略符 = lambda ch:忽略式
    def 前缀表达式(xs, /):
        前缀符序列, e = xs
        #bug:for f in 前缀符序列:
        for f in reversed(前缀符序列):
            e = f(e)
        return e
    串联表达式 = lambda es, /: 串联式(*es) if len(es) >= 2 else (the_one_(es) if es else 空式)
    #bug:锁定表达式 = lambda es, /: 锁隙式(*es) if len(es) >= 2 else (the_one_(es) >> -空式 >>the_one_ if es else 空式)
    锁定表达式 = lambda es, /: 锁隙式(*es) if len(es) >= 2 else (the_one_(es) if es else 空式)
    优选表达式 = lambda es, /: 首选式(*es) if len(es) >= 2 else (the_one_(es) if es else 失败式(None))
    互斥表达式 = lambda es, /: 独尊式(*es) if len(es) >= 2 else (the_one_(es) if es else 失败式(None))
    表达式 = lambda e:e%echo
        #阻止 表达式 越界 整理！
    def 定义行冖无首(xs, /):
        前缀符序列, 展符名, 数目纟拆包符, 变换序列乊左侧, e = xs
        e = 拆包扌(e, 数目纟拆包符)
        for 变换乊左侧 in 变换序列乊左侧:
            f, 数目纟拆包符 = 变换乊左侧
            e = 构造冫变果式扌(e, f, 数目纟拆包符)
        for 式扌 in 前缀符序列:
            e = 式扌(e)
        return 具名式(None, 展符名, e)
    def 句法书(es, /):
        d = {}
        for 行冃具名式 in es:
            展符名 = 行冃具名式.鬽名纟解码器
            dict_add__new(d, 展符名, 行冃具名式)
        return d
    nms = set(locals()) -nms
    assert nms <= _名集
    nm2f = filter4dict_key(nms.__contains__, locals())
    assert nm2f.keys() == nms
    nm2fff = {nm:乸具名函数(f'变果扌纟{nm}', f) for nm,f in nm2f.items()}
    # [:命名规范冫句法分析]:goto
    #展符名讠变果扌冖冖句法书 = nm2fff
    展符名讠变果扌冖冖圁訄甲版 = nm2fff
    return 展符名讠变果扌冖冖圁訄甲版
if not __name__ == '__main__':
    展符名讠变果扌冖冖圁訄甲版 = __()
    #场景.注册冫解码器名纟公用扌(引用名纟表达式, 表达式(场景))
    #句法书,表达式,引用名纟表达式

def __():
    #print(展符名讠变果扌冖冖圁訄甲版)
    展符名讠变果扌冖冖圁訄甲版
    匴 = 匴解码器表达式包纟圁訄甲版右递归句法语言
    句法书,表达式,引用名纟表达式 = 匴.句法书,匴.表达式,匴.引用名纟表达式
    ######################
    from seed.recognize.toy.simple_recognizer_.scene import 具名扌,注册冫变换结果函数纟具名解码器扌,取冫变换结果函数纟具名解码器扌

    场景 = 构造冫解码场景扌(鬽名='场景')
    场景.欤自动注册冫具名解码器 = True
    场景.欤自动变换结果冫具名解码器 = True
    #####
    #注册:变果扌:以构造 魖辅助表达式
    for nm, f in 展符名讠变果扌冖冖圁訄甲版.items():
        场景.注册冫变换结果函数纟具名解码器扌(nm, f)
    ######################
    ######################
    场景.注册冫解码器名纟公用扌(引用名纟表达式, 表达式(场景))
    解码器纟构造辅助表达式纟句法书冖冖圁訄甲版 = 句法书(场景)
    return 解码器纟构造辅助表达式纟句法书冖冖圁訄甲版
if not __name__ == '__main__':
    解码器纟构造辅助表达式纟句法书冖冖圁訄甲版 = __()


def 宽解码冃辅助表达式巛冊句法文本匕圁訄甲版扌(冊句法文本匕圁訄甲版, /):
    return 宽解码冃辅助表达式巛冊句法文本扌(解码器纟构造辅助表达式纟句法书冖冖圁訄甲版, 冊句法文本匕圁訄甲版)
def 宽解码冃辅助表达式巛冊句法文本扌(解码器, 冊句法文本, /):
    from seed.recognize.toy.simple_recognizer_.context import 乸具名全文冖冖记录讫地址
    全文 = 乸具名全文冖冖记录讫地址('冊句法文本', None, 冊句法文本, 0)
    全文暨起讫讫 = 构造冫全文暨起讫讫扌(全文, 0, None, None)
    #bug:return 全文.讫地址纟已访问, 解码器.宽解码扌(全文暨起讫讫)
    #   !! 取 讫地址 时，尚未解码
    r = 解码器.宽解码扌(全文暨起讫讫)
    讫地址纟已访问纟全文 = 全文.讫地址纟已访问
    return 讫地址纟已访问纟全文, r
def __():
    讫地址纟已访问纟全文, r = 宽解码冃辅助表达式巛冊句法文本匕圁訄甲版扌(冊句法文本匕圁訄甲版:=' ; ; Aaaa%f%f = -b[2][3:]%g/h//h%g + (t^u)[:4] >> s | d ^ e ; B = c000 ; # xxx \n  \n ;.')
    assert 讫地址纟已访问纟全文 == 86, (讫地址纟已访问纟全文, r)
    assert r[:2] == (86, True), r
    d = r[2]
    s = '\n'.join(f'{nm!r}:{expr!s}' for nm, expr in sorted(d.items()))
    old_ss = '''\
'Aaaa':具名式(None, 'Aaaa', 变果式(f, 变果式(f, 变果式(echo, 独尊式(首选式(锁隙式(串联式(忽略式(变果式(g, 尾限式(True, 变果式(echo, 引用式(True, 'h')), 尾限式(False, 变果式(echo, 引用式(True, 'h')), 变果式(g, 重复式(3, None, 重复式(2, 2, 变果式(echo, 引用式(True, 'b'))))))))), 重复式(0, 4, 变果式(echo, 变果式(echo, 独尊式(变果式(the_one_, 锁隙式(变果式(echo, 引用式(True, 't')), 忽略式(空式))), 变果式(the_one_, 锁隙式(变果式(echo, 引用式(True, 'u')), 忽略式(空式)))))))), 变果式(echo, 引用式(True, 's'))), 变果式(the_one_, 锁隙式(变果式(echo, 引用式(True, 'd')), 忽略式(空式)))), 变果式(the_one_, 锁隙式(变果式(echo, 引用式(True, 'e')), 忽略式(空式))))))))
'B':具名式(None, 'B', 变果式(echo, 变果式(the_one_, 锁隙式(变果式(echo, 引用式(True, 'c000')), 忽略式(空式)))))'''#'''
    ss = '''\
'Aaaa':具名式(None, 'Aaaa', 变果式(f, 变果式(f, 变果式(echo, 独尊式(首选式(锁隙式(串联式(忽略式(变果式(g, 尾限式(True, 变果式(echo, 引用式(True, 'h')), 尾限式(False, 变果式(echo, 引用式(True, 'h')), 变果式(g, 重复式(3, None, 重复式(2, 2, 变果式(echo, 引用式(True, 'b'))))))))), 重复式(0, 4, 变果式(echo, 变果式(echo, 独尊式(变果式(echo, 引用式(True, 't')), 变果式(echo, 引用式(True, 'u'))))))), 变果式(echo, 引用式(True, 's'))), 变果式(echo, 引用式(True, 'd'))), 变果式(echo, 引用式(True, 'e')))))))
'B':具名式(None, 'B', 变果式(echo, 变果式(echo, 引用式(True, 'c000'))))\
'''#'''
    assert s == ss, (s, echo)
if __name__ == '__main__':
    __()























######################
######################
######################
######################
def __():
    'copy to: ./expr_generator__2nd.py'
    ######################
    ######################
    ######################
    # [:命名规范冫句法分析]:goto
    # 圁訄甲版右递归句法语言=>:
    # 圁訄乙版右递归句法语言
    #句法文本
    (冊句法纟乙匕甲 :=
    (冊句法文本纟乙版匕甲版 :=
    (冊句法文本纟圁訄乙版匕圁訄甲版 :=
    (冊句法文本纟圁訄乙版右递归句法语言匕圁訄甲版右递归句法语言 :=
    r'''
#『>>the_one_』-->『!』
#『>>f』-->左侧『%f』
#『常量式』-->已无需
# 行首 插入『;』
# 多个:兼顾表达式
#
# len,may5tmay_,con_#join_
#
#; 空白 = `丶空白
#; 函数名 = `丶函数名
#; 展符名 = `丶展符名
#; 基符名 = `丶基符名
#; 字符串常量 = `丶字符串常量
#; 整数 = `丶整数
######################
; 基符 = 基符名
; 展符 = 展符名
; -定义符 = -('=') + -空白
; -行首 = -(';') + -空白
; 变换冫变果式! = -('%') + -空白 + 函数名
; 拆包符! = '!' + -空白
; 数目纟拆包符%len%冃基符扌 = 拆包符[:]
; 变换乊左侧 = 变换冫变果式 + 数目纟拆包符
; 变换序列乊左侧 = 变换乊左侧[:]
; 常量表达式 = 字符串常量
#; 空表达式 = ()
#; 允空表达式 = 表达式 | 空表达式
#; 括号表达式! = -('(') + -空白 + 允空表达式 + -(')') + -空白
; 括号表达式! = -('(') + -空白 + 表达式[:1] + -(')') + -空白
; 原子表达式 = 基符 | 展符 | 常量表达式 | 括号表达式
#; 允空数 %may5tmay_ = 整数[:1]
; 允空数 = 整数[:1]
; 数量范围 %con_ = -('[') + -空白 + -+~(']') + 允空数 + (-(':') + -空白 + 允空数)![:1] + -(']') + -空白
; 重复表达式 = 原子表达式 + 数目纟拆包符 + 数量范围[:]
; 尾限符!%len%冃基符扌 = ('/')[1:2] + -空白
; 尾限 = 尾限符 + 重复表达式
; 尾限暨变换乊右侧 = 变换乊左侧 | 尾限
; 后缀表达式 = 重复表达式 + 尾限暨变换乊右侧[:]
; 前瞻符 = -('+') + -空白
; 反转符 = -('~') + -空白
; 忽略符 = -('-') + -空白
; 前缀符 = 前瞻符 | 反转符 | 忽略符
; 前缀符序列 = 前缀符[:]
; 前缀表达式 = 前缀符序列 + 后缀表达式
; 串联表达式 %con_ = 前缀表达式 + (-('+') + -空白 + 前缀表达式)![:]
; 锁定表达式 %con_ = 串联表达式 + (-('>>') + -空白 + 串联表达式)![:1]
; 兼顾表达式 %con_ = 锁定表达式 + (-('&') + -空白 + 锁定表达式)![:]
; 优选表达式 %con_ = 兼顾表达式 + (-('|') + -空白 + 兼顾表达式)![:]
; 互斥表达式 %con_ = 优选表达式 + (-('^') + -空白 + 优选表达式)![:]
; 表达式 = 互斥表达式
; 定义行冖无首 = 前缀符序列 + 展符名 + 数目纟拆包符 + 变换序列乊左侧 + -定义符 + 表达式
; 定义行! = 定义行冖无首 + -行首[1:]
; 句法书! = -空白 + -行首[1:] + 定义行//'.'
;.

'''#'''
    ))))
    讫地址纟已访问纟全文, r = 宽解码冃辅助表达式巛冊句法文本匕圁訄甲版扌(冊句法纟乙匕甲)
    assert 讫地址纟已访问纟全文 == r[0], (讫地址纟已访问纟全文, r, 冊句法纟乙匕甲[:讫地址纟已访问纟全文])
    assert r[1] is True, (讫地址纟已访问纟全文, r, 冊句法纟乙匕甲[:讫地址纟已访问纟全文])
    assert 冊句法纟乙匕甲[讫地址纟已访问纟全文-1] == '.'
    #return 冊句法文本纟圁訄乙版右递归句法语言匕圁訄甲版右递归句法语言
    ######################
    d = r[2]
    #表达式冫句法书 = d['句法书']
    nms = sorted(d)
        #1/2=>魖匴后处理纟圁訄乙版:goto
    assert nms == ['串联表达式', '互斥表达式', '优选表达式', '允空数', '兼顾表达式', '前瞻符', '前缀符', '前缀符序列', '前缀表达式', '原子表达式', '反转符', '变换乊左侧', '变换冫变果式', '变换序列乊左侧', '句法书', '后缀表达式', '基符', '定义符', '定义行', '定义行冖无首', '尾限', '尾限暨变换乊右侧', '尾限符', '展符', '常量表达式', '忽略符', '拆包符', '括号表达式', '数目纟拆包符', '数量范围', '行首', '表达式', '重复表达式', '锁定表达式'], nms
        # '允空表达式', '空表达式',
    ######################
    匴 = 匴解码器表达式包纟圁訄甲版右递归句法语言
    from seed.recognize.toy.simple_recognizer_.expr_generator__2nd import 匴后处理纟圁訄乙版冫解码为表达式
    from seed.recognize.toy.simple_recognizer_.expr import 具名式,串联式,首选式,锁隙式,独尊式,前瞻式,反转式,忽略式,兼顾式,变果式,重复式,尾限式
    ######################
    from seed.recognize.toy.simple_recognizer_.syntax_tree_base import 乸句法树纟基符,乸句法树纟展符
    from seed.tiny import curry1
    def 冃基符扌(果, /):
        return 基符名凵变换结果扌('冃基符', 果)
    冃基符扌 = 构造冫具名函数扌(..., 冃基符扌)
    def 基符名凵变换结果扌(基符名, 果, /):
        return 乸句法树纟基符(基符名, 果)
    def 展符名凵变换结果扌(展符名, 果, /):
        return 乸句法树纟展符(展符名, 果)
    def 名凵变换结果扌(名, 果, /):
        return (名, 果)
    def 预处理器纟构造冫具名解码器(场景, 名, 解码器名, /):
        return 场景.变换结果解码器扌(None, curry1(名凵变换结果扌,名), 解码器名)
    ######################
    #用于 基符:解码器 #具名 之下
    def 变换讫错果扌(场景, 解码器名, 全文暨起讫讫, 讫错果, /):
        '[变换讫错果扌 :: (场景 -> 解码器 -> 全文暨起讫讫 -> 讫错果 -> 讫错果)]'
        (讫地址乊严, 错误丷结果, 错误丨结果) = 讫错果
        #bug:return (讫地址乊严, 错误丷结果, (解码器名.鬽名, 错误丨结果))
    ######################
    场景 = 构造冫解码场景扌(鬽名='场景')

    ######################
    #手动注册:基符:解码器:
    #   避免自动注册:因为 名字碰撞
    #for nm in '空白,函数名,展符名,字符串常量,基符,展符,整数'.split(','):
    #    解码器名纟基符 = f'丶{nm}'
    #    表达式名纟基符 = nm
    #    具名表达式纟基符 = getattr(匴, 表达式名纟基符)
    #    #具名表达式纟基符 = 具名表达式纟基符.更名扌(None, 解码器名纟基符)
    #    场景.注册冫解码器名纟公用扌(解码器名纟基符, 具名表达式纟基符(场景))
    ######################
    ######################
    场景.欤自动注册冫具名解码器 = True
    场景.欤自动变换结果冫具名解码器 = True
    ######################
    #自动注册:
    #   !! 现在 基符名不是『丶空白』而是相同的『空白』，或者说 没有 基符，全都是 展符！
    #但避免自动预处理:因为 基符 之下 还有 一些更基本的变果操作，不适合 自动返回树节点
    名凵变换结果扌 = 基符名凵变换结果扌
    for nm in '空白,函数名,基符名,展符名,字符串常量,整数'.split(','):
        #1/2=>魖匴后处理纟圁訄乙版:goto
        表达式名纟基符 = nm
        具名表达式纟基符 = getattr(匴, 表达式名纟基符)
        #bug:具名式之下非具名式:场景.注册冫变换结果函数纟具名解码器扌(表达式名纟基符, 变换讫错果扌)
            #鬽变换结果扌丨变换讫错果扌丨两段式篡改器
        场景.注册冫变换结果函数纟具名解码器扌(表达式名纟基符, curry1(名凵变换结果扌,表达式名纟基符))
        具名表达式纟基符(场景)
        #场景.注册冫解码器名纟公用扌(解码器名纟基符, )
    ######################
    名凵变换结果扌 = 展符名凵变换结果扌
    场景.预处理器纟构造冫具名解码器 = 预处理器纟构造冫具名解码器
    ######################
    #注册:函数:
    #for nm4f in 'len,may5tmay_,con_'.split(','):
    for nm4f in 'len,con_,冃基符扌'.split(','):
        场景.注册冫变量名纟公用扌(nm4f, eval(nm4f))
    ######################
    #自动注册:展符:解码器:
    for 表达式 in d.values():
        表达式(场景)
    #xxx:已注册:解码器纟句法书 = 表达式冫句法书(场景)
    解码器纟句法书 = 场景.构造冫解码器巛名扌('句法书')
    #assert 0, (场景.罓注册处纟解码器, 场景.罓注册处纟变量)
    #assert 0, 场景.罓注册处纟解码器
    #assert 0, 场景.罓注册处纟变量
    a,r = 宽解码冃辅助表达式巛冊句法文本扌(解码器纟句法书, 冊句法文本:=';A=b;.')
    #assert 0, (a,r)
    assert ((a,r) ==
        (6, (6, True, ('句法书', [('定义行', ('定义行冖无首', [('前缀符序列', []), ('展符名', 'A'), ('数目纟拆包符', ('冃基符', 0)), ('变换序列乊左侧', []), ('表达式', ('互斥表达式', (('优选表达式', (('兼顾表达式', (('锁定表达式', (('串联表达式', (('前缀表达式', [('前缀符序列', []), ('后缀表达式', [('重复表达式', [('原子表达式', ('展符', ('展符名', 'b'))), ('数目纟拆包符', ('冃基符', 0)), []]), []])]),)),)),)),)),)))]))])))
    ), (a,r)
    ######################
    assert type(r[2]) is 乸句法树纟展符
    句法树 = r[2]
    展符讠表达式纟解码器纟子语言 = 句法树.解码扌(匞参数配置纟解码:=匴后处理纟圁訄乙版冫解码为表达式)
    assert (展符讠表达式纟解码器纟子语言==
        #old:{'A': 具名式(None, 'A', 变果式(the_one_, 锁隙式(引用式(True, 'b'), 空式)))}
        {'A': 具名式(None, 'A', 引用式(True, 'b'))}
        ), 展符讠表达式纟解码器纟子语言
    ######################
    ######################
    a,r = 宽解码冃辅助表达式巛冊句法文本扌(解码器纟句法书, 冊句法纟乙匕甲)
    assert r[1], (a, r)
    #assert 0, r[2]
    句法树 = r[2]
    nm2e = 展符讠表达式纟解码器纟圁訄乙版 = 句法树.解码扌(匞参数配置纟解码:=匴后处理纟圁訄乙版冫解码为表达式)
    from seed.mapping_tools.dict_op import mapping_symmetric_diff4patch__immutable__default
    def 构造冫展符讠表达式纟解码器纟圁訄乙版扌():
        冃基符扌 = 乸具名引用变量('冃基符扌', None, 1, '冃基符扌')
        len = 乸具名引用变量('len', None, 1, 'len')
        con_ = 乸具名引用变量('con_', None, 1, 'con_')
        return \
{'基符': 具名式(None, '基符', 引用式(True, '基符名'))
,'展符': 具名式(None, '展符', 引用式(True, '展符名'))
,'定义符': 具名式(None, '定义符', 忽略式(串联式(忽略式(常量式('=')), 忽略式(引用式(True, '空白')))))
,'行首': 具名式(None, '行首', 忽略式(串联式(忽略式(常量式(';')), 忽略式(引用式(True, '空白')))))
,'变换冫变果式': 具名式(None, '变换冫变果式', 变果式(the_one_, 串联式(忽略式(常量式('%')), 忽略式(引用式(True, '空白')), 引用式(True, '函数名'))))
,'拆包符': 具名式(None, '拆包符', 变果式(the_one_, 串联式(常量式('!'), 忽略式(引用式(True, '空白')))))
,'数目纟拆包符': 具名式(None, '数目纟拆包符', 变果式(冃基符扌, 变果式(len, 重复式(0, None, 引用式(True, '拆包符')))))
,'变换乊左侧': 具名式(None, '变换乊左侧', 串联式(引用式(True, '变换冫变果式'), 引用式(True, '数目纟拆包符')))
,'变换序列乊左侧': 具名式(None, '变换序列乊左侧', 重复式(0, None, 引用式(True, '变换乊左侧')))
,'常量表达式': 具名式(None, '常量表达式', 引用式(True, '字符串常量'))
,'括号表达式': 具名式(None, '括号表达式', 变果式(the_one_, 串联式(忽略式(常量式('(')), 忽略式(引用式(True, '空白')), 重复式(0, 1, 引用式(True, '表达式')), 忽略式(常量式(')')), 忽略式(引用式(True, '空白')))))
,'原子表达式': 具名式(None, '原子表达式', 首选式(引用式(True, '基符'), 引用式(True, '展符'), 引用式(True, '常量表达式'), 引用式(True, '括号表达式')))
,'允空数': 具名式(None, '允空数', 重复式(0, 1, 引用式(True, '整数')))
,'数量范围': 具名式(None, '数量范围', 变果式(con_, 串联式(忽略式(常量式('[')), 忽略式(引用式(True, '空白')), 忽略式(前瞻式(反转式(常量式(']')))), 引用式(True, '允空数'), 重复式(0, 1, 变果式(the_one_, 串联式(忽略式(常量式(':')), 忽略式(引用式(True, '空白')), 引用式(True, '允空数')))), 忽略式(常量式(']')), 忽略式(引用式(True, '空白')))))
,'重复表达式': 具名式(None, '重复表达式', 串联式(引用式(True, '原子表达式'), 引用式(True, '数目纟拆包符'), 重复式(0, None, 引用式(True, '数量范围'))))
,'尾限符': 具名式(None, '尾限符', 变果式(冃基符扌, 变果式(len, 变果式(the_one_, 串联式(重复式(1, 2, 常量式('/')), 忽略式(引用式(True, '空白')))))))
,'尾限': 具名式(None, '尾限', 串联式(引用式(True, '尾限符'), 引用式(True, '重复表达式')))
,'尾限暨变换乊右侧': 具名式(None, '尾限暨变换乊右侧', 首选式(引用式(True, '变换乊左侧'), 引用式(True, '尾限')))
,'后缀表达式': 具名式(None, '后缀表达式', 串联式(引用式(True, '重复表达式'), 重复式(0, None, 引用式(True, '尾限暨变换乊右侧'))))
,'前瞻符': 具名式(None, '前瞻符', 串联式(忽略式(常量式('+')), 忽略式(引用式(True, '空白'))))
,'反转符': 具名式(None, '反转符', 串联式(忽略式(常量式('~')), 忽略式(引用式(True, '空白'))))
,'忽略符': 具名式(None, '忽略符', 串联式(忽略式(常量式('-')), 忽略式(引用式(True, '空白'))))
,'前缀符': 具名式(None, '前缀符', 首选式(引用式(True, '前瞻符'), 引用式(True, '反转符'), 引用式(True, '忽略符')))
,'前缀符序列': 具名式(None, '前缀符序列', 重复式(0, None, 引用式(True, '前缀符')))
,'前缀表达式': 具名式(None, '前缀表达式', 串联式(引用式(True, '前缀符序列'), 引用式(True, '后缀表达式')))
,'串联表达式': 具名式(None, '串联表达式', 变果式(con_, 串联式(引用式(True, '前缀表达式'), 重复式(0, None, 变果式(the_one_, 串联式(忽略式(常量式('+')), 忽略式(引用式(True, '空白')), 引用式(True, '前缀表达式')))))))
,'锁定表达式': 具名式(None, '锁定表达式', 变果式(con_, 串联式(引用式(True, '串联表达式'), 重复式(0, 1, 变果式(the_one_, 串联式(忽略式(常量式('>>')), 忽略式(引用式(True, '空白')), 引用式(True, '串联表达式')))))))
,'兼顾表达式': 具名式(None, '兼顾表达式', 变果式(con_, 串联式(引用式(True, '锁定表达式'), 重复式(0, None, 变果式(the_one_, 串联式(忽略式(常量式('&')), 忽略式(引用式(True, '空白')), 引用式(True, '锁定表达式')))))))
,'优选表达式': 具名式(None, '优选表达式', 变果式(con_, 串联式(引用式(True, '兼顾表达式'), 重复式(0, None, 变果式(the_one_, 串联式(忽略式(常量式('|')), 忽略式(引用式(True, '空白')), 引用式(True, '兼顾表达式')))))))
,'互斥表达式': 具名式(None, '互斥表达式', 变果式(con_, 串联式(引用式(True, '优选表达式'), 重复式(0, None, 变果式(the_one_, 串联式(忽略式(常量式('^')), 忽略式(引用式(True, '空白')), 引用式(True, '优选表达式')))))))
,'表达式': 具名式(None, '表达式', 引用式(True, '互斥表达式'))
,'定义行冖无首': 具名式(None, '定义行冖无首', 串联式(引用式(True, '前缀符序列'), 引用式(True, '展符名'), 引用式(True, '数目纟拆包符'), 引用式(True, '变换序列乊左侧'), 忽略式(引用式(True, '定义符')), 引用式(True, '表达式')))
,'定义行': 具名式(None, '定义行', 变果式(the_one_, 串联式(引用式(True, '定义行冖无首'), 忽略式(重复式(1, None, 引用式(True, '行首'))))))
,'句法书': 具名式(None, '句法书', 变果式(the_one_, 串联式(忽略式(引用式(True, '空白')), 忽略式(重复式(1, None, 引用式(True, '行首'))), 尾限式(True, 常量式('.'), 引用式(True, '定义行')))))
}
    assert nm2e == (cop := 构造冫展符讠表达式纟解码器纟圁訄乙版扌()), mapping_symmetric_diff4patch__immutable__default(nm2e, cop)
    ######################
    ######################
    return 冊句法文本纟圁訄乙版右递归句法语言匕圁訄甲版右递归句法语言

if __name__ == '__main__':
    冊句法文本纟圁訄乙版右递归句法语言匕圁訄甲版右递归句法语言 = __()
def __():
    冊句法纟乙匕甲 = 冊句法文本纟圁訄乙版右递归句法语言匕圁訄甲版右递归句法语言
    讫地址纟已访问纟全文, r = 宽解码冃辅助表达式巛冊句法文本匕圁訄甲版扌(冊句法纟乙匕甲)
######################
__all__
######################
######################
######################
if __name__ == '__main__':
    __()
__all__
del __all__
from seed.recognize.toy.simple_recognizer_.grammar import *
