#__all__:goto
r'''[[[

seed.recognize.toy.simple_recognizer_.decoder
py -m nn_ns.app.debug_cmd   seed.recognize.toy.simple_recognizer_.decoder -x
py -m nn_ns.app.doctest_cmd seed.recognize.toy.simple_recognizer_.decoder:__doc__
py_adhoc_call   seed.recognize.toy.simple_recognizer_.decoder   @f
from seed.recognize.toy.simple_recognizer_.decoder import *
#]]]'''
__all__ = r'''
筐简化锁定况型
魖解码器
    魖解码器冫侧重两段式
    魖解码器冫侧重单段式冫实心锁定

    乸优先并联解码器
    乸互斥并联解码器
    乸码元集合匹配解码器
    乸码元串常量匹配解码器
    乸间隙锁定串联解码器
    乸元素锁定串联解码器
    乸串联解码器
    乸首非零锁定串联解码器
    乸首锁定串联解码器
    乸尾锁定串联解码器
    乸实心锁定串联解码器
    乸序列解码器
    乸失败零解码器
    乸恒果零解码器
    乸收集时忽略结果解码器
    乸前瞻零解码器
    乸逆转成败解码器
    乸变换结果解码器
    乸结尾限长序列解码器
    乸直达终点解码器
    乸码元串定长读取解码器
    乸定域解码器

    乸零解码器
    乸具名零解码器
    乸具名解码器
    乸引用解码器

    乸变换讫错果解码器
    乸包装解码器
魖讫错果变换器
    乸讫错果变换器
    惑构造冫讫错果变换器扌
    魖错果变换器
        乸错果变换器
        乸结果变换器
        惑构造冫结果变换器扌
    乸变换结果解码器
    乸变换讫错果解码器
魖两段式篡改器
    乸两段式篡改器
检查冫讫错果扌
    检查冫讫错果冖扩展扌

乸魖包装解码器
    乸包装解码器
    乸收集时忽略结果解码器
    乸前瞻零解码器
    乸逆转成败解码器
    乸变换讫错果解码器
    乸变换结果解码器
    乸结尾限长序列解码器
    乸直达终点解码器

'''.split()#'''
#xxx惑构造冫变换结果解码器扌
#不够泛化:只支持字符串:乸正则表达式文本识别器
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.recognize.toy.simple_recognizer_._common import abstractmethod, override, ABC
from seed.recognize.toy.simple_recognizer_._common import _4repr, _4repr_named# _巛彧
from seed.recognize.toy.simple_recognizer_._common import check_type_le, check_type_is, ifNone# echo-->None8echo
from seed.recognize.toy.simple_recognizer_._common import check_pseudo_qual_name
from seed.tiny_.check import check_may_, check_not_
from seed.tiny_.check import check_callable
from itertools import count
from enum import Enum, auto
from seed.recognize.toy.simple_recognizer_.basic import None8echo# 乸具名函数
import re
___end_mark_of_excluded_global_names__0___ = ...



from seed.recognize.toy.simple_recognizer_.basic import 检查冫讫错果扌,检查冫讫错果冖扩展扌
from seed.recognize.toy.simple_recognizer_.basic import 魖讫错果变换器,乸讫错果变换器,惑构造冫讫错果变换器扌
from seed.recognize.toy.simple_recognizer_.basic import 魖错果变换器,乸错果变换器,乸结果变换器,惑构造冫结果变换器扌
from seed.recognize.toy.simple_recognizer_.basic import 魖两段式篡改器,乸两段式篡改器

class 筐简化锁定况型(Enum):
    #[:锁定况态]:goto
    匡重复 = auto()
    匡待续 = auto()
    匡后续 = auto()
    ######################
    #非必要:但人性化
    匡失败 = auto()
    匡结束 = auto()
    匡待续或失败 = auto()
    ######################

def _失败耶(r, /):
    #(讫地址, 错误丷结果, 错误丨结果) = r
    return not r[1]


检查冫讫错果扌
检查冫讫错果冖扩展扌

__all__
#class 乸解码器:
class 魖解码器(ABC):
    r'''[[[
    ######################
    两段式宽解码扌
    宽解码扌
        严解码乊容错扌
        严解码乊不容错扌
    ######################
    #严: 指『讫地址乊严』与『讫地址乊宽』相符/严丝合缝
    #   #re.fullmatch
    #   #注意:讫地址乊错 不相干
    #不容错: 指 出错时 抛出异常
    ######################
    #
    ######################
    #两段式:指『先锁定再其余』用于 并联解码器.分支
    ######################
    #
    #]]]'''#'''
    __slots__ = ()
    @property
    @abstractmethod
    def 场景(sf, /):
        '-> 场景/解码场景/魖解码场景/乸解码场景'
    @property
    @abstractmethod
    def 欤上级收集子结果时忽略我的结果(sf, /):
    #def 串联时忽略结果解码吗扌(sf, /):
        '-> bool#配合:乸串联解码器/乸定域解码器#乸收集时忽略结果解码器-特化'
        #返回值:
        _乸解码器:False
        乸收集时忽略结果解码器:True
        #相关上级:
        乸串联解码器
        乸定域解码器
        return False
    @abstractmethod
    def 罓宽解码扌(sf, 全文暨起讫讫, /):
        '-> 讫错果/(讫地址乊严, 错误丷结果, 错误丨结果)'
        魖解码器冫侧重两段式
            #依赖于:罓两段式宽解码扌
    def 宽解码扌(sf, 全文暨起讫讫, /, *, 宽丷严=False, 欤不容错=False):
        '-> 讫错果/(讫地址/(乊错|乊严), 错误丷结果, 错误丨结果) | ^解码失败冖冖宽严讫地址不同 if 宽丷严 | ^解码失败冖冖不匹配 if 欤不容错'
        '-> (讫地址, 错误丷结果, 错误丨结果)'
        r = sf.罓宽解码扌(全文暨起讫讫)
        检查冫讫错果冖扩展扌(sf, 宽丷严, 欤不容错, 全文暨起讫讫, r)
        return r
    ######################
    #严: 指『讫地址乊严』与『讫地址乊宽』相符/严丝合缝
    #   #re.fullmatch
    #   #注意:讫地址乊错 不相干
    #不容错: 指 出错时 抛出异常
    ######################
    #
    def 严解码乊容错扌(sf, 全文暨起讫讫, /):
        '-> (错误丷结果, 讫地址暨错误丨结果) | ^解码失败冖冖宽严讫地址不同'    \
        ' # 讫地址暨错误丨结果/((讫地址乊错,错误)|结果)'
        r = sf.宽解码扌(全文暨起讫讫, 宽丷严=True)
            # ^解码失败冖冖宽严讫地址不同
        (讫地址, 错误丷结果, 错误丨结果) = r
        if 错误丷结果:
            讫地址乊严 = 讫地址#匹配=>乊严
            结果 = 错误丨结果
            讫地址暨错误丨结果 = 结果
        else:
            讫地址乊错 = 讫地址#匹配=>乊错
            错误 = 错误丨结果
            讫地址暨错误丨结果 = 讫地址乊错,错误
        return (错误丷结果, 讫地址暨错误丨结果)
    def 严解码乊不容错扌(sf, 全文暨起讫讫, /):
        '-> 结果 | ^解码失败冖冖宽严讫地址不同 | ^解码失败冖冖不匹配'
        r = sf.宽解码扌(全文暨起讫讫, 宽丷严=True, 欤不容错=True)
            # ^解码失败冖冖宽严讫地址不同
            # ^解码失败冖冖不匹配
        (讫地址, 错误丷结果, 错误丨结果) = r
        assert 错误丷结果
        结果 = 错误丨结果
        return 结果


    @abstractmethod
    def 罓两段式宽解码扌(sf, 全文暨起讫讫, /):
        '-> Iter<(筐简化锁定况型,(讫地址, 错误丷结果, 错误丨结果))>{1<=len<=2} #配合:乸并联解码器#乸串联解码器-特化|单项式-包装器-可能需要特化'
        魖解码器冫侧重单段式冫实心锁定
            #依赖于:罓宽解码扌
    ######################
    #两段式:指『先锁定再其余』用于 并联解码器.分支
    ######################
    #
    def 两段式宽解码扌(sf, 全文暨起讫讫, /, *, 宽丷严=False, 欤不容错=False):
        '-> Iter<(讫地址, 错误丷结果, 错误丨结果)>{len==2} #本函数的用途是 重复一次 返回值 iff 匡锁定前失败/匡锁定暨匹配'
        #[:锁定况态]:goto
        it = sf.罓两段式宽解码扌(全文暨起讫讫)
        assert iter(it) is it
        T = 筐简化锁定况型
        for j, (case, r) in enumerate(it):
            check_type_is(T, case)
            检查冫讫错果扌(全文暨起讫讫, r)

            ######################
            if case is T.匡待续或失败:
                if not j == 0:raise 000
                #case = T.匡重复 if _失败耶(r) else T.匡待续
                if _失败耶(r):
                    [(case, r2)] = it
                    if not _失败耶(r2): raise 000
                    yield r
                    r = r2
                    j = 1
                else:
                    case = T.匡待续
            ######################
            if case is T.匡待续:
                if not j == 0:raise 000
                if _失败耶(r):raise 000
                yield r
                continue
            ######################
            if case is T.匡后续:
                if not j == 1:raise 000
            elif case is T.匡重复:
                if not j == 0:raise 000
            elif case is T.匡失败:
                if not _失败耶(r):raise 000
            elif not case is T.匡结束:
                raise 000#未知case
            ######################
            # case as-if T.匡结束:
            if not j <= 1:raise 000
            [] = it
            检查冫讫错果冖扩展扌(sf, 宽丷严, 欤不容错, 全文暨起讫讫, r)
            if j == 0:
                yield r
            yield r
            return
        raise 000#[] or [匡待续]
    ######################
    ######################
    ######################
    ######################
    #def 罓两段式宽解码扌(sf, 全文暨起讫讫, /):
    #    '-> Iter<(筐允零首锁定况型,(讫地址, 错误丷结果, 错误丨结果))>{1<=len<=2} #配合:乸并联解码器#乸串联解码器-特化|单项式-包装器-可能需要特化'
    #取消:太复杂:def 罓两段式宽解码扌(sf, 全文暨起讫讫, /, *, 允零首锁定丷首非零锁定):
    #   '-> Iter<((筐允零首锁定况型|筐首非零锁定况型),(讫地址, 错误丷结果, 错误丨结果))>{1<=len<=2} #配合:乸并联解码器#乸串联解码器-特化|单项式-包装器-可能需要特化'
        #[:锁定况态]:goto
    #def 两段式宽解码扌(sf, 全文暨起讫讫, /, *, 允零首锁定丷首非零锁定):
    #    '-> Iter<(筐允零首锁定况型,(讫地址, 错误丷结果, 错误丨结果))>{1<=len<=2} #配合:乸并联解码器#乸串联解码器-特化|单项式-包装器-可能需要特化'
    #    '-> Iter<((筐允零首锁定况型|筐首非零锁定况型),(讫地址, 错误丷结果, 错误丨结果))>{1<=len<=2} #配合:乸并联解码器#乸串联解码器-特化|单项式-包装器-可能需要特化'
    ######################
    ######################
    ######################

#end-class 魖解码器(ABC):


class 魖解码器冫侧重两段式(魖解码器):
    __slots__ = ()
    @override
    def 罓宽解码扌(sf, 全文暨起讫讫, /):
        '-> (讫地址乊严, 错误丷结果, 错误丨结果)'
        for r in sf.两段式宽解码扌(全文暨起讫讫):pass
        return r

class 魖解码器冫侧重单段式冫实心锁定(魖解码器):
    __slots__ = ()
    @override
    def 罓两段式宽解码扌(sf, 全文暨起讫讫, /):
        '-> Iter<筐简化锁定况型,(讫地址, 错误丷结果, 错误丨结果))>{1<=len<=2} #配合:乸并联解码器#乸串联解码器-特化|单项式-包装器-可能需要特化'
        r = sf.宽解码扌(全文暨起讫讫)
        yield 筐简化锁定况型.匡结束, r
        return





class _乸解码器(_4repr, 魖解码器):
    ___no_slots_ok___ = True
    def __init__(sf, 场景, /):
        sf._场景 = 场景
    @property
    @override
    def 场景(sf, /):
        '-> 场景/解码场景/乸解码场景'
        return sf._场景
    @property
    @override
    def 欤上级收集子结果时忽略我的结果(sf, /):
        '-> bool#见:乸串联解码器,乸收集时忽略结果解码器'
        return False
    欤上级收集子结果时忽略我的结果 = False


__all__
class _乸并联解码器(_乸解码器, 魖解码器冫侧重两段式):
    r'''[[[
    彧鬽错误乊多锁定:
        [彧鬽错误乊多锁定 is ...]:继续解码
        [not$ 彧鬽错误乊多锁定 is ...]:中止解码
            ^解码异常冖冖互斥并联冖冖多锁定

    列表纟丮锁定丶动态厈
        #xxx :: [(解码器名冃锁定,部分构造参数冃后续)]
        :: [((解码器名冃锁定,部分构造参数冃后续)|解码器名)]
            #now:两段式宽解码扌
            #[部分构造参数冃后续==None] => 实心锁定
            #两段式宽解码扌 => 『[(x,y)] --> [((x,y)|z)]』

    解码器名冃锁定
        :: 解码器名
        见:魖解码场景.构造冫解码器巛名扌
    部分构造参数冃后续
        :: callable | non_callable
        ===
        * non_callable部分构造参数冃后续
            见:魖解码场景.构造冫解码器纟并联扌
        * callable部分构造参数冃后续
            :: sf/_乸并联解码器 -> 索引号冃分支 -> 结果冃锁定 -> 魖解码器

    #]]]'''#'''
    def __init__(sf, 场景, 鬽错误乊无锁定, 彧鬽错误乊多锁定, 列表纟丮锁定丶动态厈, /, *, 互斥丷优先):
        super().__init__(场景)
        sf._场景 = 场景
        sf._鬽错误乊无锁定 = 鬽错误乊无锁定
        sf._彧鬽错误乊多锁定 = 彧鬽错误乊多锁定
        sf._ls = 列表纟丮锁定丶动态厈
        列表纟丮锁定丶动态厈[:0]
        sf._互斥丷优先 = 互斥丷优先
    @override
    def 罓两段式宽解码扌(sf, 全文暨起讫讫, /):
        '-> Iter<筐简化锁定况型,(讫地址, 错误丷结果, 错误丨结果))>{1<=len<=2} #配合:乸并联解码器#乸串联解码器-特化|单项式-包装器-可能需要特化'
        T = 筐简化锁定况型
        ls = sf._ls
        场景 = sf.场景
        互斥丷优先 = sf._互斥丷优先
        rs = []
        js = []
        ys = []
        for j in range(len(ls)):
            x = ls[j]
            if not type(x) is tuple:
                解码器名 = x
                解码器 = 场景.构造冫解码器巛名扌(解码器名)
                it = 解码器.两段式宽解码扌(全文暨起讫讫)
                r = next(it)
                y = False, it
            else:
                (解码器名冃锁定,部分构造参数冃后续) = x
                解码器冃锁定 = 场景.构造冫解码器巛名扌(解码器名冃锁定)
                r = 解码器冃锁定.宽解码扌(全文暨起讫讫)
                y = True, 部分构造参数冃后续
            r
            y
            (讫地址乊左, 错误丷结果, 错误丨结果) = r
            rs.append((讫地址乊左, 错误丷结果, 错误丨结果))
            ys.append(y)
            if 错误丷结果:
                js.append(j)
                if 互斥丷优先:
                    break

        rs, ys, js
        ok = len(js) == 1
            # 唯一锁定
            # 下面js被修改
        if ok:
            pass
        elif not js:
            鬽错误 = sf._鬽错误乊无锁定
            if not rs:
                #空:无分支
                错误 = ifNone(鬽错误,[])
                yield T.匡失败, (全文暨起讫讫.起地址,False, 错误)
                return
            js = range(len(rs))
                #全错,无锁定
            #len(js) 可能为 1
            #   ==>> 使用 『ok』
            鬽错误
                #全错
        else:
            彧鬽错误 = sf._彧鬽错误乊多锁定
            js
                #全对,多锁定
            if 彧鬽错误 is ...:
                #继续解码
                错误 = js
                pass
            else:
                #中止解码
                鬽错误 = 彧鬽错误
                错误 = ifNone(鬽错误,js)
                raise 解码异常冖冖互斥并联冖冖多锁定(错误)
            鬽错误 = 错误
                #全对
        if ok:
            pass
        else:
            鬽错误
            js
                #全错|全对
            assert js
            j = max(js, key=lambda j:rs[j][0])
            (讫地址乊左乊最大, 错误丷结果, 错误丨结果) = rs[j]
            if not 错误丷结果:
                #全错
                错误 = ifNone(鬽错误,错误丨结果)
            else:
                #全对
                assert 鬽错误 is js
                assert 鬽错误 is 错误
                错误
            错误
            yield T.匡失败, (讫地址乊左乊最大,False, 错误)
            return
            return (讫地址乊左乊最大,False, 错误)
        [j] = js
        (it_vs_arg, it_or_arg) = y = ys[j]
        (讫地址乊左, 错误丷结果, 错误丨结果) = r = rs[j]
        assert 错误丷结果
        结果冃锁定 = 错误丨结果
        起地址乊右 = 讫地址乊左

        yield T.匡待续, r

        if not it_vs_arg:
            it = it_or_arg
            [r] = it
        else:
            arg = it_or_arg
            部分构造参数冃后续 = arg
            解码器冃后续 = 场景.构造冫解码器纟并联扌(sf, j, 结果冃锁定, 部分构造参数冃后续)
            r = 解码器冃后续.宽解码扌(全文暨起讫讫 << 起地址乊右)
        r
        yield T.匡后续, r
        return
#end-class _乸并联解码器(_乸解码器):

class 乸优先并联解码器(_乸并联解码器):
    def __init__(sf, 场景, 鬽错误乊无锁定, 鬽解码器名乊无锁定, 列表纟丮锁定丶动态厈, /):
        if not None is 鬽解码器名乊无锁定:
            #无锁定
            #『if-then-else』之『else』
            解码器名乊无锁定 = 鬽解码器名乊无锁定
            列表纟丮锁定丶动态厈 = [*列表纟丮锁定丶动态厈, 解码器名乊无锁定]
                #允许 非 有序对 <<==两段式宽解码扌
        super().__init__(场景, 鬽错误乊无锁定, 彧鬽错误乊多锁定:=None, 列表纟丮锁定丶动态厈, 互斥丷优先=True)
class 乸互斥并联解码器(_乸并联解码器):
    def __init__(sf, 场景, 鬽错误乊无锁定, 彧鬽错误乊多锁定, 列表纟丮锁定丶动态厈, /):
        super().__init__(场景, 鬽错误乊无锁定, 彧鬽错误乊多锁定, 列表纟丮锁定丶动态厈, 互斥丷优先=False)



class 乸码元集合匹配解码器(_乸解码器, 魖解码器冫侧重单段式冫实心锁定):
    def __init__(sf, 场景, 码元集, /):
        super().__init__(场景)
        sf._ls = 码元集

    @override
    def 罓宽解码扌(sf, 全文暨起讫讫, /):
        '-> (讫地址乊严, 错误丷结果, 错误丨结果)'
        ls = sf._ls
        场景 = sf.场景
        全文 = 全文暨起讫讫.全文
        起地址 = 全文暨起讫讫.起地址


        全文
        eof = 起地址 == 全文暨起讫讫.讫地址乊宽
        if eof:
            魊码元 = ()
        else:
            码元 = 全文[起地址]
            if 码元 in ls:
                return (讫地址乊严:=起地址+1, True, 结果:=码元)
            魊码元 = (码元,)
        魊码元
        return (讫地址乊错:=起地址+len(魊码元), False, 错误:=魊码元)
#end-class 乸码元集合匹配解码器(_乸解码器):



class 乸码元串常量匹配解码器(_乸解码器, 魖解码器冫侧重单段式冫实心锁定):
    'vs:乸码元串定长读取解码器'
    def __init__(sf, 场景, 码元串, /):
        super().__init__(场景)
        #sf._鬽错误 = 鬽错误
        sf._ls = 码元串
        码元串[:0]
        #check_type_is(tuple, 码元串)
            #str/bytes

    @override
    def 罓宽解码扌(sf, 全文暨起讫讫, /):
        '-> (讫地址乊严, 错误丷结果, 错误丨结果)'
        ls = sf._ls
        场景 = sf.场景
        全文 = 全文暨起讫讫.全文
        起地址 = 全文暨起讫讫.起地址

        #if not 起地址 + len(ls) <= 讫地址乊宽:
        #    return (?讫地址乊错?, 错误丷结果, 错误丨结果)

        全文
        讫地址冃上限 = 全文暨起讫讫.讫地址乊宽
        #鬽错误 = sf._鬽错误
        地址 = 起地址-1
        for 地址,码元 in enumerate(ls, 起地址):
            #bug:if 讫地址冃上限 < 地址:
            if 讫地址冃上限 == 地址 or not 码元 == 全文[地址]:
                讫地址乊错 = 地址 + (not 讫地址冃上限 == 地址)
                return (讫地址乊错, False, 错误:=None)
                return (地址, False, 错误:=地址-起地址)
        讫地址乊严 = 地址+1
        return (讫地址乊严, True, 结果:=None)
        #return (地址+1, True, 码元串)
#end-class 乸码元串常量匹配解码器(_乸解码器):

__all__
def _规范化范围扌(L, begin, may_end, /):
    begin = _规范化索引号扌(L, begin)
        # None 有歧义
    end = _规范化鬽索引号扌(L, may_end)
    if not begin <= end: raise 索引号异常(L, begin, end)
    return begin, end

def _规范化鬽索引号扌(L, may_j, /):
    if may_j is None: return L
    j = may_j
    j = _规范化索引号扌(L, j)
    return j
def _规范化索引号扌(L, j, /):
    check_type_is(int, j)
    j0 = j
    if j < 0:
        j += L
    if not 0 <= j <= L:raise 索引号异常(L,j0)
    return j

def _put_(rs_, 解码器, r, /):
    (讫地址, 错误丷结果, 错误丨结果) = r
    assert 错误丷结果
    结果 = 错误丨结果
    if not 解码器.欤上级收集子结果时忽略我的结果:
        rs_.append(结果)

__all__
class _乸串联解码器(_乸解码器, 魖解码器冫侧重两段式):
    r'''[[[
    [:锁定况态]:here
    原计划过于复杂，已取消
        now:筐简化锁定况型
    ===
    保底索引号=>解禁
    封顶索引号=>裁剪
    [0<=保底索引号<=封顶索引号<=总长]
    * [保底索引号==封顶索引号]:
        前缀实心锁定
        [保底索引号==封顶索引号==总长]:
            实心锁定
    * [保底索引号==封顶索引号-1]:
        期间:唯一锁定信号:
            元素锁定
    * [保底索引号<封顶索引号-1]:
        期间:锁定信号序列:
            元素锁定,元素匹配;循环:下一个元素
    *保底居后:首锁定
    *保底居后:首非零锁定
    ==>>两段式宽解码扌:kw:允零首锁定丷首非零锁定
    #注意:乸前瞻零解码器:讫地址乊锁定 极可能 大于 讫地址乊结束(===起地址)
    *首锁定:返回序列:
        筐允零首锁定况型
        * [失败]
        * [锁定暨匹配]
        * [锁定,失败]
        * [锁定,匹配]
    *首非零锁定:返回序列:
        不同上
        筐首非零锁定况型
        * [失败]
        * [零锁定暨匹配]
            [要求:[起地址==讫地址]]
        * [非零锁定暨匹配]
            [要求:[起地址<讫地址]]
        * [非零锁定暨返回起地址暨匹配]
            [允许:[起地址==讫地址]]<<==乸前瞻零解码器
        * [非零锁定,失败]
        * [非零锁定,匹配]
    ===
    ===
    ===
    '鬽索引锁定丨首非零锁定:may int/鬽索引锁定|.../首非零锁定'
    #]]]'''#'''
    def __init__(sf, 场景, 保底后冫允零首锁定丷首非零锁定, 保底索引号, 鬽封顶索引号, 列表纟解码器名, /):
        super().__init__(场景)
        #sf._鬽错误 = 鬽错误
        sf._ls = 列表纟解码器名
        列表纟解码器名[:0]
        L = len(列表纟解码器名)
        (保底索引号, 封顶索引号) = _规范化范围扌(L, 保底索引号, 鬽封顶索引号)
        sf._封顶索引号 = 封顶索引号
        sf._保底索引号 = 保底索引号
        sf._保底后冫允零首锁定丷首非零锁定 = 保底后冫允零首锁定丷首非零锁定
        check_type_is(bool, 保底后冫允零首锁定丷首非零锁定)
        return
    #@override
    #def 罓宽解码扌(sf, 全文暨起讫讫, /):
    #    '-> (讫地址乊严, 错误丷结果, 错误丨结果)'
    #    ls = sf._ls
    #    return sf._宽解码扌(全文暨起讫讫, ls)
    def _宽解码扌(sf, 全文暨起讫讫, ls, /):
        '-> (讫地址, 错误丷结果, 错误丨结果)'
        场景 = sf.场景
        rs_ = []
        for 解码器名 in ls:
            解码器 = 场景.构造冫解码器巛名扌(解码器名)
            r = 解码器.宽解码扌(全文暨起讫讫)
            if _失败耶(r):
                return r
            _put_(rs_, 解码器, r)
            (讫地址, 错误丷结果, 错误丨结果) = r
            全文暨起讫讫 <<= 讫地址
        return (讫地址:=全文暨起讫讫.起地址, True, rs_)
    @override
    def 罓两段式宽解码扌(sf, 全文暨起讫讫, /):
        '-> Iter<筐简化锁定况型,(讫地址, 错误丷结果, 错误丨结果))>{1<=len<=2} #配合:乸并联解码器#乸串联解码器-特化|单项式-包装器-可能需要特化'
        #注意:忽略/跳过！！==>>_put_
        ls = sf._ls
        L = len(ls)
        场景 = sf.场景
        封顶索引号 = sf._封顶索引号
        保底索引号 = sf._保底索引号
        保底后冫允零首锁定丷首非零锁定 = sf._保底后冫允零首锁定丷首非零锁定
        if 保底后冫允零首锁定丷首非零锁定:
            #首非零锁定
            def ok_(r, /):
                #起地址乊保底
                (讫地址, 错误丷结果, 错误丨结果) = r
                return 起地址乊保底 < 讫地址
        else:
            #允零首锁定
            def ok_(r, /):
                return True
        ok_
        _put_
        #T = _况型扌(允零首锁定丷首非零锁定)
        T = 筐简化锁定况型
        ls_ = ls[:保底索引号]
        r = sf._宽解码扌(全文暨起讫讫, ls_)
        if _失败耶(r):
            yield T.匡失败, r
            return
        (讫地址, 错误丷结果, 错误丨结果) = r
        起地址乊保底 = 讫地址
        全文暨起讫讫 <<= 讫地址
        rs_ = 错误丨结果

        已锁定 = False
        for j in range(保底索引号,封顶索引号):
            解码器名 = ls[j]
            解码器 = 场景.构造冫解码器巛名扌(解码器名)
            it = 解码器.两段式宽解码扌(全文暨起讫讫)
            for r in it:
                if _失败耶(r):
                    yield T.匡失败, r
                    return
                if ok_(r):
                    yield T.匡待续, r
                    已锁定 = True
                    break
            if 已锁定:
                for r in it:pass
                if _失败耶(r):
                    yield T.匡失败, r
                    return
            _put_(rs_, 解码器, r)
            (讫地址, 错误丷结果, 错误丨结果) = r
            全文暨起讫讫 <<= 讫地址
            if 已锁定:
                j += 1
                break
        else:
            #封顶
            if 0:
                #bug: 后面还有...
                yield T.匡重复, (讫地址, True, rs_)
                return
            #封顶
            j = 封顶索引号
            yield T.匡待续, (讫地址, True, rs_)
            已锁定 = True
        assert 已锁定
        j
        _ls = ls[j:]
        r = sf._宽解码扌(全文暨起讫讫, _ls)
        if _失败耶(r):
            yield T.匡失败, r
            return
        (讫地址, 错误丷结果, 错误丨结果) = r
        全文暨起讫讫 <<= 讫地址
        _rs = 错误丨结果
        rs_ += _rs
            #_put_()
        yield T.匡后续, (讫地址, True, rs_)
        return
    #end-def 罓两段式宽解码扌(sf, 全文暨起讫讫, /):
#end-class _乸串联解码器(_乸解码器):
_乸自定义锁定串联解码器 = _乸串联解码器
    #def __init__(sf, 场景, 保底后冫允零首锁定丷首非零锁定, 保底索引号, 封顶索引号, 列表纟解码器名, /):
class 乸间隙锁定串联解码器(_乸自定义锁定串联解码器):
    def __init__(sf, 场景, 鬽索引号纟间隙, 列表纟解码器名, /):
        索引号纟间隙 = _规范化鬽索引号扌(len(列表纟解码器名), 鬽索引号纟间隙)
            #<<== 起 必须非 鬽
        super().__init__(场景, False, 索引号纟间隙, 索引号纟间隙, 列表纟解码器名)
class 乸元素锁定串联解码器(_乸自定义锁定串联解码器):
    def __init__(sf, 场景, 鬽索引号纟元素, 列表纟解码器名, /):
        索引号纟元素 = _规范化鬽索引号扌(len(列表纟解码器名), 鬽索引号纟元素)
            #<<== 起 必须非 鬽
        super().__init__(场景, False, 索引号纟元素, None, 列表纟解码器名)
    pass
class 乸串联解码器(_乸自定义锁定串联解码器):
    '首非零锁定:锁定于第一个讫非起的子解码器'
    def __init__(sf, 场景, 列表纟解码器名, /):
        super().__init__(场景, True, 0, None, 列表纟解码器名)
乸首非零锁定串联解码器 = 乸串联解码器
class 乸首锁定串联解码器(乸元素锁定串联解码器):
    '首锁定/允零'
    def __init__(sf, 场景, 列表纟解码器名, /):
        assert len(列表纟解码器名)
        super().__init__(场景, 0, 列表纟解码器名)
class 乸尾锁定串联解码器(乸元素锁定串联解码器):
    '尾锁定/允零'
    def __init__(sf, 场景, 列表纟解码器名, /):
        assert len(列表纟解码器名)
        super().__init__(场景, -1, 列表纟解码器名)
class 乸实心锁定串联解码器(乸间隙锁定串联解码器):
    '实心锁定'
    def __init__(sf, 场景, 列表纟解码器名, /):
        super().__init__(场景, None, 列表纟解码器名)
def 宽解码冖冖欤锁定后失败(解码器, 全文暨起讫讫, /):
    '-> (欤锁定后失败, 讫错果/(讫地址, 错误丷结果, 错误丨结果)) #[[欤锁定后失败 is True] -> [错误丷结果 is False]]'
    it = 解码器.两段式宽解码扌(全文暨起讫讫)
    r = next(it)
    if _失败耶(r):
        [r] = it
        return False, r
    r = next(it)
    [] = it
    if _失败耶(r):
        return True, r
    return False, r
class 乸序列解码器(_乸解码器, 魖解码器冫侧重两段式):
    'regex(x{m,n}) # greedy'
    def __init__(sf, 场景, 最小数目, 鬽最大数目, 解码器名, /):
        super().__init__(场景)
        sf._最小数目 = 最小数目
        sf._鬽最大数目 = 鬽最大数目
        sf._解码器名 = 解码器名
        check_type_is(int, 最小数目)
        if not 鬽最大数目 is None:
            最大数目 = 鬽最大数目
            check_type_is(int, 最大数目)
            if not 0 <= 最小数目 <= 最大数目: raise 数目范围异常(最小数目, 最大数目)
    @override
    def 罓两段式宽解码扌(sf, 全文暨起讫讫, /):
        '-> Iter<筐简化锁定况型,(讫地址, 错误丷结果, 错误丨结果))>{1<=len<=2} #配合:乸并联解码器#乸串联解码器-特化|单项式-包装器-可能需要特化'
        T = 筐简化锁定况型
        场景 = sf.场景
        最小数目 = sf._最小数目
        鬽最大数目 = sf._鬽最大数目
        解码器名 = sf._解码器名
        解码器 = 场景.构造冫解码器巛名扌(解码器名)
        rs = []
        for i in count(0):
            if i == 最小数目:
                yield T.匡待续, (讫地址:=全文暨起讫讫.起地址, True, rs)
            if i == 鬽最大数目:
                break
            #bug:(讫地址, 错误丷结果, 错误丨结果) = 解码器.宽解码扌(全文暨起讫讫)
            if i < 最小数目:
                r = 解码器.宽解码扌(全文暨起讫讫)
            else:
                (欤锁定后失败, r) = 宽解码冖冖欤锁定后失败(解码器, 全文暨起讫讫)
                if 欤锁定后失败:
                    yield T.匡失败, r
                    return
            r
            (讫地址, 错误丷结果, 错误丨结果) = r
            if not 错误丷结果:
                错误 = 错误丨结果
                if len(rs) >= 最小数目:
                    讫地址 = 全文暨起讫讫.起地址
                        #后退#回到上一正确位置#避免错误
                    break
                yield T.匡失败, (讫地址, False, 错误)
                return
            结果 = 错误丨结果
            rs.append(结果)
            if 全文暨起讫讫.起地址 == 讫地址:
                #匹配 空串
                if 鬽最大数目 is None:
                    raise 解码异常冖冖匹配空串导致无限长序列
                assert i == 0
                最大数目 = 鬽最大数目
                assert len(rs) == 1
                rs *= 最大数目
                break
            全文暨起讫讫 <<= 讫地址
        yield T.匡后续, (讫地址:=全文暨起讫讫.起地址, True, rs)
        return
        return (讫地址, True, rs)
#end-class 乸序列解码器(_乸解码器):



#class 乸断言零解码器(_乸解码器):

class 乸失败零解码器(_乸解码器, 魖解码器冫侧重单段式冫实心锁定):
    'error msg :: m a'
    def __init__(sf, 场景, 错误, /):
        super().__init__(场景)
        sf._错误 = 错误
    @override
    def 罓宽解码扌(sf, 全文暨起讫讫, /):
        '-> (讫地址乊严, 错误丷结果, 错误丨结果)'
        错误 = sf._错误
        讫地址 = 全文暨起讫讫.起地址
        return (讫地址, False, 错误)
class 乸恒果零解码器(_乸解码器, 魖解码器冫侧重单段式冫实心锁定):
    'return a :: m a'
    def __init__(sf, 场景, 结果, /):
        super().__init__(场景)
        sf._结果 = 结果
    @override
    def 罓宽解码扌(sf, 全文暨起讫讫, /):
        '-> (讫地址乊严, 错误丷结果, 错误丨结果)'
        结果 = sf._结果
        讫地址 = 全文暨起讫讫.起地址
        return (讫地址, True, 结果)
class 乸零解码器(乸恒果零解码器):
    def __init__(sf, 场景, /):
        super().__init__(场景, None)
class 乸具名零解码器(乸恒果零解码器):
    '用于测试:显示短名'
    def __init__(sf, 场景, 名, /):
        super().__init__(场景, None)
        sf._名 = 名
        check_pseudo_qual_name(名)
    def __repr__(sf, /):
        return sf._名

class _冖乸引用解码器(_乸解码器):
    def __init__(sf, 场景, 解码器名, /):
        super().__init__(场景)
        sf._解码器名 = 解码器名
    @override
    def 罓宽解码扌(sf, 全文暨起讫讫, /):
        '-> (讫地址乊严, 错误丷结果, 错误丨结果)'
        场景 = sf.场景
        解码器名 = sf._解码器名
        解码器 = 场景.构造冫解码器巛名扌(解码器名)
        return 解码器.宽解码扌(全文暨起讫讫)
    @override
    def 罓两段式宽解码扌(sf, 全文暨起讫讫, /):
        '-> Iter<筐简化锁定况型,(讫地址, 错误丷结果, 错误丨结果))>{1<=len<=2} #配合:乸并联解码器#乸串联解码器-特化|单项式-包装器-可能需要特化'
        T = 筐简化锁定况型
        场景 = sf.场景
        解码器名 = sf._解码器名
        解码器 = 场景.构造冫解码器巛名扌(解码器名)
        it = 解码器.两段式宽解码扌(全文暨起讫讫)
        r = next(it)
        yield T.匡待续或失败, r
        [r] = it
        yield T.匡结束, r
        return
class 乸引用解码器(_冖乸引用解码器):
    '参见:引用式:虽然 解码器名 基本上可当作 解码器 使用，但 有时就是要求 对象 必须是 解码器,比如 构造函数 返回值'
class 乸具名解码器(_冖乸引用解码器):
    #using _4repr.__eq__
    '用于测试:显示短名 # vs:解码器名: 去掉 引号 直接显示变量名 #参见:引用式,具名式'
    def __init__(sf, 场景, 鬽名, 解码器名, /):
        super().__init__(场景, 解码器名)
        名 = ifNone(鬽名, 解码器名)
        check_pseudo_qual_name(名)
        sf._名 = 名
    def __repr__(sf, /):
        return sf._名


def _罓乊失败扌(sf, 全文暨起讫讫, r, /):
    '-> r/讫错果'
    r = sf.罓乊失败扌(全文暨起讫讫, r)
    r = sf.罓乊结束扌(全文暨起讫讫, r)
    return r
def _罓乊匹配扌(sf, 全文暨起讫讫, r, /):
    '-> r/讫错果'
    r = sf.罓乊匹配扌(全文暨起讫讫, r)
    r = sf.罓乊结束扌(全文暨起讫讫, r)
    return r
class 乸魖包装解码器(_乸解码器, 魖解码器冫侧重两段式):
    def 罓乊起始扌(sf, 全文暨起讫讫, /):
        '-> None'
        #用于:调试
        return
    def 罓乊锁定扌(sf, 全文暨起讫讫, r, /):
        '-> r/讫错果'
        return r
    def 罓乊失败扌(sf, 全文暨起讫讫, r, /):
        '-> r/讫错果'
        return r
    def 罓乊匹配扌(sf, 全文暨起讫讫, r, /):
        '-> r/讫错果'
        return r
    def 罓乊结束扌(sf, 全文暨起讫讫, r, /):
        '-> r/讫错果'
        return r
    @property
    def 解码器名(sf, ):
        return sf._解码器名
    def __init__(sf, 场景, 解码器名, /):
        super().__init__(场景)
        sf._解码器名 = 解码器名
    @override
    def 罓两段式宽解码扌(sf, 全文暨起讫讫, /):
        '-> Iter<筐简化锁定况型,(讫地址, 错误丷结果, 错误丨结果))>{1<=len<=2} #配合:乸并联解码器#乸串联解码器-特化|单项式-包装器-可能需要特化'
        sf.罓乊起始扌(全文暨起讫讫)
        T = 筐简化锁定况型
        场景 = sf.场景
        解码器名 = sf._解码器名
        解码器 = 场景.构造冫解码器巛名扌(解码器名)
        it = 解码器.两段式宽解码扌(全文暨起讫讫)
        for j, r in enumerate(it):
            if _失败耶(r):
                r = _罓乊失败扌(sf, 全文暨起讫讫, r)
                yield T.匡结束, r#允许:匹配
                #yield T.匡失败, r
                return
            if j == 1:
                break
            r = sf.罓乊锁定扌(全文暨起讫讫, r)
            if _失败耶(r):
                r = _罓乊失败扌(sf, 全文暨起讫讫, r)
                yield T.匡结束, r#允许:匹配
                return
            yield T.匡待续, r
        [] = it
        r = _罓乊匹配扌(sf, 全文暨起讫讫, r)
        yield T.匡结束, r#允许:失败
        return
None8echo


魖两段式篡改器,乸两段式篡改器
class 乸包装解码器(乸魖包装解码器):
    __doc__ = 乸两段式篡改器.__doc__

    def __init__(sf, 场景, 两段式篡改器, 解码器名, /):
        super().__init__(场景, 解码器名)
        sf.__1 = 两段式篡改器
        #check_type_is(乸两段式篡改器, 两段式篡改器)
        check_type_le(魖两段式篡改器, 两段式篡改器)
    @property
    def 两段式篡改器(sf, /):
        return sf.__1

    ######################
    @override
    def 罓乊起始扌(sf, 全文暨起讫讫, /):
        '-> None'
        #用于:调试
        sf.两段式篡改器.乊起始扌(sf, 全文暨起讫讫)
        return
    @override
    def 罓乊锁定扌(sf, 全文暨起讫讫, r, /):
        '-> r/讫错果'
        return sf.两段式篡改器.乊锁定扌(sf, 全文暨起讫讫, r)
    @override
    def 罓乊失败扌(sf, 全文暨起讫讫, r, /):
        '-> r/讫错果'
        return sf.两段式篡改器.乊失败扌(sf, 全文暨起讫讫, r)
    @override
    def 罓乊匹配扌(sf, 全文暨起讫讫, r, /):
        '-> r/讫错果'
        return sf.两段式篡改器.乊匹配扌(sf, 全文暨起讫讫, r)
    @override
    def 罓乊结束扌(sf, 全文暨起讫讫, r, /):
        '-> r/讫错果'
        return sf.两段式篡改器.乊结束扌(sf, 全文暨起讫讫, r)

class 乸收集时忽略结果解码器(乸魖包装解码器):
    'skip/ignore/drop/discard # vs 乸恒果零解码器: 地址更改，不是 零解码器 #相当于: 乸变换结果解码器(None, lambda _:None, 解码器名) # 主要是 配合 乸串联解码器'
    @property
    @override
    def 欤上级收集子结果时忽略我的结果(sf, /):
        '-> bool#见:乸串联解码器,乸收集时忽略结果解码器'
        return True
    欤上级收集子结果时忽略我的结果 = True
    @override
    def 罓乊匹配扌(sf, 全文暨起讫讫, r, /):
        '-> r/讫错果'
        (讫地址, 错误丷结果, 错误丨结果) = r
        return (讫地址, True, None)



class 乸前瞻零解码器(乸魖包装解码器):
    '上帝视角:压缩扩展结果为解码结果:增强编程能力 # Either msg a -> Either msg (Either msg a)'
    #@override
    #def 罓乊匹配扌(sf, 全文暨起讫讫, r, /):
    #    '-> r/讫错果'
    #    结果 = r
    #    讫地址 = 全文暨起讫讫.起地址
    #    return (讫地址, True, 结果)
    @override
    def 罓乊结束扌(sf, 全文暨起讫讫, r, /):
        '-> r/讫错果'
        (讫地址, 错误丷结果, 错误丨结果) = r
        讫地址 = 全文暨起讫讫.起地址
        错误丨结果 = r
        return (讫地址, 错误丷结果, 错误丨结果)
        return (讫地址, True, 错误丨结果)

    @override
    def 罓两段式宽解码扌(sf, 全文暨起讫讫, /):
        '-> Iter<筐简化锁定况型,(讫地址, 错误丷结果, 错误丨结果))>{1<=len<=2} #配合:乸并联解码器#乸串联解码器-特化|单项式-包装器-可能需要特化'
        return super().罓两段式宽解码扌(全文暨起讫讫.乊乸前瞻零解码器冖冖临时扩张扌())



class 乸逆转成败解码器(乸魖包装解码器):
    '交换角色: 结果<->错误 # Either msg a -> Either a msg'
    @override
    def 罓乊结束扌(sf, 全文暨起讫讫, r, /):
        '-> r/讫错果'
        (讫地址, 错误丷结果, 错误丨结果) = r
        return (讫地址, not 错误丷结果, 错误丨结果)


魖讫错果变换器,乸讫错果变换器,惑构造冫讫错果变换器扌
魖错果变换器,乸错果变换器,乸结果变换器,惑构造冫结果变换器扌
def __():
    pass
    #def 惑构造冫变换结果解码器扌(场景, 鬽变换错误扌, 鬽变换结果扌丨变换讫错果扌丨讫错果变换器, 解码器名, /):
    #    '-> 乸变换结果解码器|乸变换讫错果解码器'
#class 乸变换讫错果解码器(乸魖包装解码器):
class 乸变换讫错果解码器(乸包装解码器):
    r'''
    泛化版 乸变换结果解码器
    乸变换讫错果解码器+乸讫错果变换器
    魖讫错果变换器.变换讫错果扌 :: 场景 -> 解码器名 -> 全文暨起讫讫 -> 讫错果 -> 讫错果
        now:[魖讫错果变换器 <: 魖两段式篡改器]
        now:[乸变换讫错果解码器 <: 乸包装解码器]
    '''#'''
    def __init__(sf, 场景, 鬽变换讫错果扌丨两段式篡改器, 解码器名, /):
        两段式篡改器 = 惑构造冫讫错果变换器扌(鬽名:=None, 鬽变换讫错果扌丨两段式篡改器)
        super().__init__(场景, 两段式篡改器, 解码器名)
#class 乸变换结果解码器(乸魖包装解码器):
class 乸变换结果解码器(乸变换讫错果解码器):
    r'''
    fmap@结果 # fmap :: (a->b) -> m a -> m b
        now:[乸变换结果解码器 <: 乸变换讫错果解码器 <: 乸包装解码器]
    '''#'''
    def __init__(sf, 场景, 鬽变换错误扌, 鬽变换结果扌丨变换讫错果扌丨两段式篡改器, 解码器名, /):
        '惑构造冫结果变换器扌:不能 合并到 惑构造冫讫错果变换器扌<<==当函数同时支持1/4个参数时，无法区分'
        两段式篡改器 = 惑构造冫结果变换器扌(彧鬽名:=None, 鬽变换错误扌, 鬽变换结果扌丨变换讫错果扌丨两段式篡改器)
        super().__init__(场景, 两段式篡改器, 解码器名)
    #def __init__(sf, 场景, 变换错误扌, 变换结果扌, 解码器名, /):
    #    super().__init__(场景, 解码器名)
    #    变换错误扌 = ifNone(变换错误扌, None8echo)
    #    变换结果扌 = ifNone(变换结果扌, None8echo)
    #    check_callable(变换错误扌)
    #    check_callable(变换结果扌)
    #    sf._变换错误扌 = 变换错误扌
    #    sf._变换结果扌 = 变换结果扌
    #@override
    #def 罓乊失败扌(sf, 全文暨起讫讫, r, /):
    #    '-> r/讫错果'
    #    (讫地址, 错误丷结果, 错误丨结果) = r
    #    变换错误扌 = sf._变换错误扌
    #    错误 = 错误丨结果
    #    错误 = 变换错误扌(错误)
    #    return (讫地址, False, 错误)
    #@override
    #def 罓乊匹配扌(sf, 全文暨起讫讫, r, /):
    #    '-> r/讫错果'
    #    (讫地址, 错误丷结果, 错误丨结果) = r
    #    变换结果扌 = sf._变换结果扌
    #    结果 = 错误丨结果
    #    结果 = 变换结果扌(结果)
    #    return (讫地址, True, 结果)




def _f4尾递归(并联解码器, 索引号冃分支, 结果冃锁定, /):
    场景 = 并联解码器.场景
    解码器冃后续 = 场景.串联扌([场景.恒果零解码器扌(结果冃锁定), 并联解码器])
    return 解码器冃后续
class 乸结尾限长序列解码器(乸魖包装解码器):
    'regex(x*? y) #nongreedy'
    def __init__(sf, 场景, 鬽错误乊无锁定, 欤去除结果冃结尾, 解码器名冃结尾, 解码器名冃元素, /):
        check_type_is(bool, 欤去除结果冃结尾)
        sf._欤去除结果冃结尾 = 欤去除结果冃结尾
        列表纟丮锁定丶动态厈 = (
            [(解码器名冃结尾, 场景.恒果零解码器扌(''))
                    #发现:结果冃结尾 被 忽略 ==>> 构造冫解码器纟并联扌::串联扌
            #,(解码器名冃元素, _f4尾递归)
            ,(解码器名冃元素, ...)
            ])
        解码器 = 场景.优先并联扌(鬽错误乊无锁定, 鬽解码器名乊无锁定:=None, 列表纟丮锁定丶动态厈)
            #?乸变换结果解码器
        super().__init__(场景, 解码器)
    @override
    def 罓乊匹配扌(sf, 全文暨起讫讫, r, /):
        '-> r/讫错果'
        (讫地址, 错误丷结果, 错误丨结果) = r
        lnkls = 结果 = 错误丨结果
        rs = []
        while lnkls:
            x, lnkls = lnkls
            rs.append(x)
        assert rs
        assert lnkls == ''
        if sf._欤去除结果冃结尾:
            rs.pop()
        return (讫地址, True, rs)
class 乸直达终点解码器(乸魖包装解码器):
    'regex(x .*)'
    @override
    def 罓乊匹配扌(sf, 全文暨起讫讫, r, /):
        '-> r/讫错果'
        (讫地址, 错误丷结果, 错误丨结果) = r
        讫地址 = 全文暨起讫讫.讫地址乊宽
        return (讫地址, 错误丷结果, 错误丨结果)
class 乸码元串定长读取解码器(_乸解码器, 魖解码器冫侧重两段式):
    'vs:乸码元串常量匹配解码器'
    def __init__(sf, 场景, 鬽长度, /):
        super().__init__(场景)
        sf._鬽长度 = 鬽长度
        if not 鬽长度 is None:
            长度 = 鬽长度
            check_type_is(int, 长度)
            if not 长度 >= 0: raise TypeError(长度)

    @override
    def 罓两段式宽解码扌(sf, 全文暨起讫讫, /):
        '-> Iter<筐简化锁定况型,(讫地址, 错误丷结果, 错误丨结果))>{1<=len<=2} #配合:乸并联解码器#乸串联解码器-特化|单项式-包装器-可能需要特化'
        T = 筐简化锁定况型
        鬽长度 = sf._鬽长度
        全文暨起讫讫.起地址

        全文 = 全文暨起讫讫.全文
        起地址 = 全文暨起讫讫.起地址
        讫地址冃上限 = 全文暨起讫讫.讫地址乊宽
        if not 鬽长度 is None:
            长度 = 鬽长度
            讫地址乊严 = 起地址 + 长度
        else:
            讫地址乊严 = 讫地址冃上限
        讫地址乊严

        if not 讫地址乊严 <= 讫地址冃上限:
            yield T.匡失败, (讫地址冃上限, False, None)
            return
        yield T.匡待续, (讫地址乊严, True, None)
        yield T.匡后续, (讫地址乊严, True, 全文[起地址:讫地址乊严])
        return
#end-class 乸码元串定长读取解码器(_乸解码器):


class 乸定域解码器(_乸解码器, 魖解码器冫侧重两段式):
    '乸定域解码器-as-AND vs 乸并联解码器-as-OR'
    def __init__(sf, 场景, 限制冫步进丷前瞻, 保底索引号, 列表纟解码器名, /):
        super().__init__(场景)
        sf._ls = 列表纟解码器名
        列表纟解码器名[:0]
        if not 列表纟解码器名:raise TypeError('乸定域解码器 不允许 空 列表纟解码器名')
        L = len(列表纟解码器名)
        (保底索引号, _) = _规范化范围扌(L, 保底索引号, 保底索引号)
        sf._保底索引号 = 保底索引号
        sf._限制冫步进丷前瞻 = 限制冫步进丷前瞻
        check_type_is(bool, 限制冫步进丷前瞻)
    @override
    def 罓两段式宽解码扌(sf, 全文暨起讫讫, /):
        '-> Iter<筐简化锁定况型,(讫地址, 错误丷结果, 错误丨结果))>{1<=len<=2} #配合:乸并联解码器#乸串联解码器-特化|单项式-包装器-可能需要特化'
        T = 筐简化锁定况型
        场景 = sf.场景
        保底索引号 = sf._保底索引号
        限制冫步进丷前瞻 = sf._限制冫步进丷前瞻
        ls = sf._ls

        #注意:忽略/跳过！！==>>_put_
        _put_
        rs_ = []
        def h(全文暨起讫讫, r, /):
            (讫地址乊严, 错误丷结果, 错误丨结果) = r
            #xxx全文暨起讫讫 <<= 讫地址
            if 限制冫步进丷前瞻:
                return 全文暨起讫讫.限制前瞻扌(讫地址乊严)
            else:
                return 全文暨起讫讫.限制步进扌(讫地址乊严)

        for j, 解码器名 in enumerate(ls):
            宽丷严 = (not j==0)
            解码器 = 场景.构造冫解码器巛名扌(解码器名)
            if j == 保底索引号:
                it = 解码器.两段式宽解码扌(全文暨起讫讫, 宽丷严=宽丷严)
                r = next(it)
                if _失败耶(r):
                    yield T.匡失败, r
                    return
                yield T.匡待续, r
                [r] = it
            else:
                r = 解码器.宽解码扌(全文暨起讫讫, 宽丷严=宽丷严)
            r
            if _失败耶(r):
                yield T.匡失败, r
                return
            _put_(rs_, 解码器, r)
            if j == 0:
                全文暨起讫讫 = h(全文暨起讫讫, r)

        讫地址乊严 = 全文暨起讫讫.讫地址乊宽
            # !! 列表纟解码器名 非空
            # !! h()

        yield T.匡结束, (讫地址乊严, True, rs_)
            # if 保底索引号==len(列表纟解码器名):前无 匡待续
        return
#end-class 乸定域解码器(_乸解码器, 魖解码器冫侧重两段式):




class 乸正则表达式文本识别器(_乸解码器, 魖解码器冫侧重单段式冫实心锁定):
    '码元串===str'
    def __init__(sf, 场景, 跳过丷读取, 正则表达式, /):
        super().__init__(场景)
        check_type_is(bool, 跳过丷读取)
        sf.__2 = 跳过丷读取, re.compile(正则表达式)

    @override
    def 罓宽解码扌(sf, 全文暨起讫讫, /):
        '-> (讫地址乊严, 错误丷结果, 错误丨结果)'
        跳过丷读取, 正则表达式 = sf.__2
        场景 = sf.场景
        全文 = 全文暨起讫讫.全文
        check_type_is(str, 全文)
        起地址 = 全文暨起讫讫.起地址
        讫地址 = 全文暨起讫讫.讫地址乊宽
        m = 正则表达式.match(全文, 起地址, 讫地址)
        if m is None:
            #讫地址乊错 = ???
            #错误 = ???
            return (讫地址乊错:=起地址, False, 错误:=None)
        讫地址乊严 = m.end(0)
        if 跳过丷读取:
            结果 = 全文[起地址:讫地址乊严]
        else:
            结果 = None
        return (讫地址乊严, True, 结果)
#end-class 乸正则表达式文本识别器(_乸解码器):




__all__
___begin_mark_of_excluded_global_names__999___ = ...
from seed.recognize.toy.simple_recognizer_.error import \
(解码失败冖冖宽严讫地址不同
,解码失败冖冖不匹配
,解码异常冖冖互斥并联冖冖多锁定
,解码异常冖冖匹配空串导致无限长序列
,数目范围异常
,索引号异常
)
___end_mark_of_excluded_global_names__999___ = ...
from seed.recognize.toy.simple_recognizer_.decoder import *
