#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/toy/simple_recognizer_/syntax_tree_base.py

seed.recognize.toy.simple_recognizer_.syntax_tree_base
py -m nn_ns.app.debug_cmd   seed.recognize.toy.simple_recognizer_.syntax_tree_base -x
py -m nn_ns.app.doctest_cmd seed.recognize.toy.simple_recognizer_.syntax_tree_base:__doc__
py_adhoc_call   seed.recognize.toy.simple_recognizer_.syntax_tree_base   @f
#]]]'''
__all__ = r'''
魖泛变换纟句法树
    魖泛变换纟句法树冖冖匞参数配置
        乸解码纟句法树
        乸树变换纟句法树

魖句法树
    魖句法树纟基符
    魖句法树纟展符
    魖句法树冖冖委托后处理
        乸句法树纟基符
        乸句法树纟展符
'''.split()#'''
__all__

from seed.recognize.toy.simple_recognizer_._common import abstractmethod, override, ABC
from seed.recognize.toy.simple_recognizer_._common import _4repr, _4repr_named, _巛彧
from seed.recognize.toy.simple_recognizer_._common import check_type_le, check_type_is, ifNone# echo

class 魖句法树(ABC):
    r'''[[[
    魖句法树.句法树容器 = 句法树容器纟展符 | 句法树容器纟基符
    句法树容器纟基符 = sf/魖句法树纟基符/魖句法树
    句法树容器纟展符 = 魖句法树 | [句法树容器纟展符]
    #]]]'''#'''
    __slots__ = ()
    @abstractmethod
    def 罓后处理纟解码扌(sf, 匞参数配置纟解码, 解码结果纟句法树容器, /):
        '-> 解码结果纟句法树/object'
        #罓后处理纟解码扌=>解码扌
        return 解码结果纟句法树容器
    @abstractmethod
    def 罓后处理纟树变换扌(sf, 匞参数配置纟树变换, 树变换结果纟句法树容器, /):
        '-> 树变换结果纟句法树/魖句法树'
        #罓后处理纟树变换扌=>树变换扌
        return type(sf)(sf.符号纟句法树, 树变换结果纟句法树容器)
    @property
    @abstractmethod
    def 符号纟句法树(sf, /):
        '-> 符号纟句法树/(基符|展符)'
    @property
    @abstractmethod
    def 句法树容器(sf, /):
        '-> 句法树容器'
    @property
    def 欤是句法树纟基符(sf, /):
        '-> bool'
        return sf.句法树容器 is sf
    @property
    def 欤是句法树纟展符(sf, /):
        '-> bool'
        return not sf.欤是句法树纟基符
    #def 解码扌(sf, 基符讠变换器, 展符讠变换器, /):
    def 解码扌(sf, 匞参数配置纟解码, /):
        '-> 解码结果纟句法树/object'
        #罓后处理纟解码扌=>解码扌
        匴解码纟句法树 = 乸解码纟句法树(匞参数配置纟解码)
        return 匴解码纟句法树.泛变换冫句法树扌(sf)
    def 树变换扌(sf, 匞参数配置纟树变换, /):
        '-> 树变换结果纟句法树/魖句法树'
        #罓后处理纟树变换扌=>树变换扌
        匴树变换纟句法树 = 乸树变换纟句法树(匞参数配置纟树变换)
        return 匴树变换纟句法树.泛变换冫句法树扌(sf)

class 魖泛变换纟句法树(ABC):
    __slots__ = ()
    #可能需要:
    #匞参数配置
    #匞参数配置纟解码
    #匞参数配置纟树变换
    @abstractmethod
    def 预处理纟泛变换纟基符(sf, 句法树纟基符, /):
        '-> 泛变换结果纟句法树容器'
    @abstractmethod
    def 后处理纟泛变换扌(sf, 句法树, 泛变换结果纟句法树容器, /):
        '-> 泛变换结果纟句法树'

    def 泛变换冫句法树容器扌(sf, 句法树容器, /):
        '-> 泛变换结果纟句法树容器'
        if isinstance(句法树容器, 魖句法树):
            句法树 = 句法树容器
            泛变换结果纟句法树 = sf.泛变换冫句法树扌(句法树)
            泛变换结果纟句法树容器 = 泛变换结果纟句法树
        else:
            句法树容器冃父 = 句法树容器
            泛变换结果纟句法树容器 = [*map(sf.泛变换冫句法树容器扌, 句法树容器冃父)]
        return 泛变换结果纟句法树容器

    def 泛变换冫句法树扌(sf, 句法树, /):
        '-> 泛变换结果纟句法树'
        if 句法树.欤是句法树纟基符:
            句法树纟基符 = 句法树
            # !! [句法树纟基符.句法树容器 is 句法树纟基符]
            泛变换结果纟句法树容器 = sf.预处理纟泛变换纟基符(句法树纟基符)
        else:
            句法树容器 = 句法树.句法树容器纟展符
            泛变换结果纟句法树容器 = sf.泛变换冫句法树容器扌(句法树容器)
        泛变换结果纟句法树容器
        泛变换结果纟句法树 = sf.后处理纟泛变换扌(句法树, 泛变换结果纟句法树容器)
        return 泛变换结果纟句法树

class 魖泛变换纟句法树冖冖匞参数配置(_4repr, 魖泛变换纟句法树):
    '含:匞参数配置'
    ___no_slots_ok___ = True
    def __init__(sf, 匞参数配置, /):
        sf.__1 = 匞参数配置
    @property
    def 匞参数配置(sf, /):
        '-> 匞参数配置'
        return sf.__1
class 乸解码纟句法树(魖泛变换纟句法树冖冖匞参数配置):
    '匴解码纟句法树'
    #含:匞参数配置纟解码
    __slots__ = ()
    @override
    def 预处理纟泛变换纟基符(sf, 句法树纟基符, /):
        '-> 解码结果纟句法树容器/object'
        # !! [句法树纟基符.句法树容器 is 句法树纟基符]
        解码结果纟句法树容器 = 句法树纟基符.解码结果纟基符 # = 句法树纟基符.句法树容器.解码结果纟基符
        return 解码结果纟句法树容器
    @override
    def 后处理纟泛变换扌(sf, 句法树, 解码结果纟句法树容器, /):
        '-> 解码结果纟句法树/object'
        解码结果纟句法树 = 句法树.罓后处理纟解码扌(sf.匞参数配置, 解码结果纟句法树容器)
        return 解码结果纟句法树



class 乸树变换纟句法树(魖泛变换纟句法树冖冖匞参数配置):
    '匴树变换纟句法树'
    #含:匞参数配置纟树变换
    __slots__ = ()
    @override
    def 预处理纟泛变换纟基符(sf, 句法树纟基符, /):
        '-> 树变换结果纟句法树容器/句法树容器'
        # !! [句法树纟基符.句法树容器 is 句法树纟基符]
        树变换结果纟句法树容器 = 句法树纟基符 # = 句法树纟基符.句法树容器
        return 树变换结果纟句法树容器
    @override
    def 后处理纟泛变换扌(sf, 句法树, 树变换结果纟句法树容器, /):
        '-> 树变换结果纟句法树/魖句法树'
        树变换结果纟句法树 = 句法树.罓后处理纟树变换扌(sf.匞参数配置, 树变换结果纟句法树容器)
        check_type_le(魖句法树, 树变换结果纟句法树)
        return 树变换结果纟句法树


class 魖句法树纟基符(魖句法树):
    __slots__ = ()
    @property
    @abstractmethod
    def 基符(sf, /):
        '-> 基符'
    @property
    @abstractmethod
    def 解码结果纟基符(sf, /):
        '-> 解码结果纟基符'
    @property
    @override
    def 句法树容器(sf, /):
        '-> 句法树容器'
        return sf
    @property
    @override
    def 符号纟句法树(sf, /):
        '-> 符号纟句法树/(基符|展符)'
        return sf.基符
    @property
    @override
    def 欤是句法树纟基符(sf, /):
        '-> bool'
        return True
        return sf.句法树容器 is sf

class 魖句法树纟展符(魖句法树):
    __slots__ = ()
    @property
    @abstractmethod
    def 展符(sf, /):
        '-> 展符'
    @property
    @abstractmethod
    def 句法树容器纟展符(sf, /):
        '-> 句法树容器纟展符'
    @property
    @override
    def 句法树容器(sf, /):
        '-> 句法树容器'
        return sf.句法树容器纟展符
    @property
    @override
    def 符号纟句法树(sf, /):
        '-> 符号纟句法树/(基符|展符)'
        return sf.展符
    @property
    @override
    def 欤是句法树纟基符(sf, /):
        '-> bool'
        return False

class 魖句法树冖冖委托后处理(魖句法树):
    __slots__ = ()
    罓格式纟后处理名纟匞参数配置纟解码 = '{}'
        #匞参数配置纟树变换.fff
    罓格式纟后处理名纟匞参数配置纟树变换 = '{}'
        #匞参数配置纟树变换.ggg
    @override
    def 罓后处理纟解码扌(sf, 匞参数配置纟解码, 解码结果纟句法树容器, /):
        '-> 解码结果纟句法树/object'
        #罓后处理纟解码扌=>解码扌
        后处理名纟解码 = sf.罓格式纟后处理名纟匞参数配置纟解码.format(sf.符号纟句法树)
        鬽后处理纟解码扌 = getattr(匞参数配置纟解码, 后处理名纟解码, None)
        if not 鬽后处理纟解码扌 is None:
            后处理纟解码扌 = 鬽后处理纟解码扌
            return 后处理纟解码扌(sf, 解码结果纟句法树容器)
        return 解码结果纟句法树容器
    @override
    def 罓后处理纟树变换扌(sf, 匞参数配置纟树变换, 树变换结果纟句法树容器, /):
        '-> 树变换结果纟句法树/魖句法树'
        #罓后处理纟树变换扌=>树变换扌
        后处理名纟树变换 = sf.罓格式纟后处理名纟匞参数配置纟树变换.format(sf.符号纟句法树)
        鬽后处理纟树变换扌 = getattr(匞参数配置纟树变换, 后处理名纟树变换, None)
        if not 鬽后处理纟树变换扌 is None:
            后处理纟树变换扌 = 鬽后处理纟树变换扌
            return 后处理纟树变换扌(sf, 树变换结果纟句法树容器)
        return type(sf)(sf.符号纟句法树, 树变换结果纟句法树容器)


class 乸句法树纟基符(tuple, 魖句法树冖冖委托后处理, 魖句法树纟基符):
    #___no_slots_ok___ = True
    __slots__ = ()
    def __new__(cls, 基符, 解码结果纟基符, /):
        return super(__class__, cls).__new__(cls, [基符, 解码结果纟基符])
    @property
    @override
    def 基符(sf, /):
        '-> 基符'
        return sf[0]
    @property
    @override
    def 解码结果纟基符(sf, /):
        '-> 解码结果纟基符'
        return sf[1]
乸句法树纟基符('aa', 999)
class 乸句法树纟展符(tuple, 魖句法树冖冖委托后处理, 魖句法树纟展符):
    #___no_slots_ok___ = True
    __slots__ = ()
    def __new__(cls, 展符, 句法树容器纟展符, /):
        return super(__class__, cls).__new__(cls, [展符, 句法树容器纟展符])
    @property
    @override
    def 展符(sf, /):
        '-> 展符'
        return sf[0]
    @property
    @override
    def 句法树容器纟展符(sf, /):
        '-> 句法树容器纟展符'
        return sf[1]
乸句法树纟展符('AA', 999)




__all__
from seed.recognize.toy.simple_recognizer_.syntax_tree_base import 魖句法树,魖句法树纟基符,魖句法树纟展符,魖句法树冖冖委托后处理,乸句法树纟基符,乸句法树纟展符
from seed.recognize.toy.simple_recognizer_.syntax_tree_base import 魖泛变换纟句法树,魖泛变换纟句法树冖冖匞参数配置,乸解码纟句法树,乸树变换纟句法树
from seed.recognize.toy.simple_recognizer_.syntax_tree_base import *
