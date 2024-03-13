#__all__:goto
r'''[[[

seed.recognize.toy.simple_recognizer_.register
py -m nn_ns.app.debug_cmd   seed.recognize.toy.simple_recognizer_.register -x
py -m nn_ns.app.doctest_cmd seed.recognize.toy.simple_recognizer_.register:__doc__
py_adhoc_call   seed.recognize.toy.simple_recognizer_.register   @f

py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.recognize.toy.simple_recognizer_.register:魖工厂场景@T    =T      ++exclude_prefixes:_       +exclude_attrs5listed_in_cls_doc

#]]]'''
__all__ = r'''
乸私用空间
    乸具名私用空间
乸私钥
    乸具名私钥
魖注册处
    乸具名注册处
    乸具名注册处暨用户数据
构造冫具名对象乊缺省扌
    构造冫具名注册处乊缺省扌
    构造冫具名注册处扌

魖工厂场景
    注册冫变量名纟公用扌
    注册冫变量名纟私用扌
    取冫变量值扌

乸可变真值
'''.split()#'''
__all__
from seed.recognize.toy.simple_recognizer_._common import abstractmethod, override, ABC
from seed.recognize.toy.simple_recognizer_._common import _4repr, _4repr_named, _巛彧
from seed.recognize.toy.simple_recognizer_._common import check_type_le, check_type_is, ifNone, ifNonef
from seed.recognize.toy.simple_recognizer_._common import check_pseudo_qual_name
from seed.tiny_.check import check_subscriptable
from seed.abc.eq_by_id.AddrAsHash import le_AddrAsHash #BaseAddrAsHash, le_AddrAsHash, AddrAsHash as EqById
from seed.recognize.toy.simple_recognizer_.error import 注册异常冖冖已注册
from weakref import WeakValueDictionary

__all__

class _魖具名:
    __slots__ = ()
    def __init__(sf, 名, /):
        check_pseudo_qual_name(名)
        sf._名 = 名
    def __repr__(sf, /):
        return sf._名
    #def __format__(sf, /, *args, **kwds):
    #    raise Exception(*args, **kwds)


class 乸私用空间(dict):
    '私用空间/weakable'
    __slots__ = '__weakref__'
#bug:class 乸具名私用空间(dict, _魖具名):
class 乸具名私用空间(_魖具名, dict):
    '具名:私用空间/weakable'
    __slots__ = ('__weakref__', '_名')
    def __init__(sf, 名, /, *args, **kwds):
        _魖具名.__init__(sf, 名)
        dict.__init__(sf, *args, **kwds)
assert 乸私用空间({1:2})[1] == 2
assert 乸具名私用空间('d', {1:2})[1] == 2
assert 1 not in 乸具名私用空间('d')
assert repr(乸具名私用空间('d')) == 'd'
assert repr(乸具名私用空间('d', {})) == 'd'
assert str(乸具名私用空间('d')) == 'd'

class 乸私钥:#不能用_4repr_named#
    '私钥/le_AddrAsHash#eq===is'
    __slots__ = ()
class 乸具名私钥(_魖具名):#不能用_4repr_named#
    '具名:私钥/le_AddrAsHash#eq===is'
    __slots__ = '_名'
assert le_AddrAsHash(乸私钥)
assert le_AddrAsHash(乸具名私钥)
assert not le_AddrAsHash(_4repr_named)
assert not le_AddrAsHash(_4repr)
assert repr(乸具名私钥('k')) == 'k'
assert str(乸具名私钥('k')) == 'k'



def _取冫私用区扌(sf, /):
    私用区 = sf.罓私用区
    check_type_is(WeakValueDictionary, 私用区)
    return 私用区

def _欤已注册扌丨取冫目标值扌(sf, 钥, 鬽槑目标值, /, *, 仅测试):
    '-> 欤已注册/bool if 仅测试 else (目标值 | ^LookupError if miss 钥 and 鬽槑目标值 is None)'
    #_欤已注册扌丨取冫目标值扌==>>欤已注册扌,取冫目标值扌
    Nothing = []
    if not Nothing is (x := sf.罓公用区.get(钥, Nothing)):
        if 仅测试: return True
        目标值 = x
    elif le_AddrAsHash(type(钥)) and not Nothing is (d := _取冫私用区扌(sf).get(钥, Nothing)):
        if 仅测试: return True
        私用空间 = d
        目标值 = 私用空间[钥]
    else:
        if 仅测试: return False
        if 鬽槑目标值 is None:
            raise LookupError(钥)
            return None
        槑目标值 = 鬽槑目标值
        目标值 = 槑目标值()
    if 仅测试: raise 000
    return 目标值

class 魖注册处(ABC):
    '乸具名注册处,乸具名注册处暨用户数据'
    __slots__ = ()
    @property
    @abstractmethod
    def 罓公用区(sf, /):
        '-> 公用区/{公钥:目标值}'
    @property
    @abstractmethod
    def 罓私用区(sf, /):
        '-> 私用区/WeakValueDictionary<私钥/AddrAsHash, 私用空间/weakable_mapping<私钥,目标值> >'
    def 罓检查冫目标值扌(sf, 目标值, /):
        '-> None | ^Exception'


    #_欤已注册扌丨取冫目标值扌==>>欤已注册扌,取冫目标值扌
    def 取冫目标值扌(sf, 钥, 鬽槑目标值, /, *, 仅测试=False):
        '-> 目标值 | (^LookupError if miss 钥 and 鬽槑目标值 is None)'
        '-> (目标值 | (^LookupError if miss 钥 and 鬽槑目标值 is None)) if not 仅测试 else 欤已注册/bool'
        目标值 = _欤已注册扌丨取冫目标值扌(sf, 钥, 鬽槑目标值, 仅测试=仅测试)
            # ^LookupError
        return 目标值
    def 欤已注册扌(sf, 钥, /):
        '-> 欤已注册/bool'
        欤已注册 = _欤已注册扌丨取冫目标值扌(sf, 钥, 鬽槑目标值:=None, 仅测试=True)
        return 欤已注册

    def 注册纟公用扌(sf, 公钥, 目标值, /):
        '公钥/hashable -> 目标值 -> None'
        if sf.欤已注册扌(公钥):
            raise 注册异常冖冖已注册(公钥)
        sf.罓检查冫目标值扌(目标值)
        公用区 = sf.罓公用区
        if not 目标值 is 公用区.setdefault(公钥, 目标值):
            raise 000
        assert sf.欤已注册扌(公钥)
        return
    def 注册纟私用扌(sf, 私钥, 私用空间, /):
        '私钥{eq==is} -> 私用空间/weakable_mapping<私钥,目标值> -> None #参见:乸私用空间,乸具名私用空间,乸私钥,乸具名私钥'
        if not le_AddrAsHash(type(私钥)): raise TypeError(f'not le_AddrAsHash({type(私钥)})')
        if sf.欤已注册扌(私钥):
            raise 注册异常冖冖已注册(私钥)

        if 1:
            目标值 = 私用空间[私钥]
            sf.罓检查冫目标值扌(目标值)
        私用区 = _取冫私用区扌(sf)
        if not 私用空间 is 私用区.setdefault(私钥, 私用空间):
            raise 000
        assert sf.欤已注册扌(私钥)
        return


def _分离扌(鬽名丨对象, /):
    if type(鬽名丨对象) is str:
        名纟对象 = 鬽名丨对象
        鬽名 = 名纟对象
        鬽对象 = None
    else:
        鬽对象 = 鬽名丨对象
        鬽名 = None
    return 鬽名, 鬽对象
def 构造冫具名对象乊缺省扌(构造冫具名对象巛鬽名扌, 鬽名丨对象, /):
    '(鬽 名 -> 具名对象) -> (鬽 名 | 对象) -> (对象|具名对象)'
    #返回值:对象 不一定 是 具名对象
    #   只是 缺省时 才 构造 具名对象
    (鬽名, 鬽对象) = _分离扌(鬽名丨对象)
    对象 = ifNonef(鬽对象, lambda:构造冫具名对象巛鬽名扌(鬽名))
    return 对象

def 构造冫具名注册处乊缺省扌(鬽乸具名注册处, 鬽名丨注册处, /):
    注册处 = 构造冫具名对象乊缺省扌(lambda 鬽名:构造冫具名注册处扌(鬽乸具名注册处,鬽名=鬽名), 鬽名丨注册处)
    return 注册处
def 构造冫具名注册处扌(cls=None, /, *, 鬽名=None, 鬽公用区=None, 鬽私用区=None):
    公用区 = ifNonef(鬽公用区, dict)
    私用区 = ifNonef(鬽私用区, WeakValueDictionary)
    cls = ifNone(cls, 乸具名注册处)
    return cls(鬽名, 公用区, 私用区)
class 乸具名注册处(_4repr_named, 魖注册处):
    ___no_slots_ok___ = True
    def __init__(sf, 鬽名, 公用区, 私用区, /):
        sf._鬽名 = 鬽名
        sf._公用区 = 公用区
        sf._私用区 = 私用区
        check_type_is(WeakValueDictionary, 私用区)
        check_subscriptable(公用区)

    @property
    @override
    def 罓公用区(sf, /):
        '-> 公用区/{公钥:目标值}'
        return sf._公用区
    @property
    @override
    def 罓私用区(sf, /):
        '-> 私用区/WeakValueDictionary<私钥/AddrAsHash, 私用空间/weakable_mapping<私钥,目标值> >'
        return sf._私用区



class 乸具名注册处暨用户数据(乸具名注册处):
    def __init__(sf, 鬽名, 公用区, 私用区, 用户数据纟注册随行, /):
        super().__init__(鬽名, 公用区, 私用区)
        sf._用户数据纟注册随行 = 用户数据纟注册随行
    @property
    @override
    def 用户数据纟注册随行(sf, /):
        '-> 用户数据纟注册随行'
        return sf._用户数据纟注册随行
    def 更新冫用户数据纟注册随行(sf, 用户数据纟注册随行, /):
        if 用户数据纟注册随行 is sf.用户数据纟注册随行:
            return sf
        鬽名, 公用区, 私用区, _ = sf._args
        return type(sf)(鬽名, 公用区, 私用区, 用户数据纟注册随行)

























__all__
######################
######################
######################
def _取冫变量值扌(sf, 变量名, 鬽槑变量值, /, *, 仅测试):
    '-> (变量值 | (^LookupError if miss 钥 and 鬽槑变量值 is None)) if not 仅测试 else 欤已注册/bool'
    return sf.罓注册处纟变量.取冫目标值扌(变量名, 鬽槑变量值, 仅测试=仅测试)
        # ^LookupError

def 注册冫变量名纟公用扌(场景, 变量名纟公用, 变量值, /):
    ':: 场景/魖工厂场景 -> 变量名纟公用/hashable -> 变量值 -> None'
    场景.注册冫变量名纟公用扌(变量名纟公用, 变量值)
def 注册冫变量名纟私用扌(场景, 变量名纟私用, 私用空间, /):
    ':: 场景/魖工厂场景 -> 变量名纟私用{eq==is} -> 私用空间/weakable_mapping<变量名纟私用,变量值> -> None #参见:乸私用空间,乸具名私用空间,乸私钥,乸具名私钥'
    场景.注册冫变量名纟私用扌(变量名纟私用, 私用空间)
def 取冫变量值扌(场景, 变量名, 鬽槑变量值, /):
    ':: 场景/魖工厂场景 -> 变量名 -> 鬽槑变量值/(None|(()->变量值)) -> -> 变量值 | (^LookupError if miss 钥 and 鬽槑变量值 is None)'
    变量值 = 场景.取冫变量值扌(变量名, 鬽槑变量值)
    return 变量值
class 魖工厂场景(ABC):
    r'''
[[
总结:构造界面 隔离 具现类型:
    见:魖解码场景<:魖工厂场景 +魖注册处
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


new_abstract_methods:
    `罓注册处纟变量
new_concrete_methods:
    罓检查冫变量值扌
    匞参数配置包
    欤已注册冫变量名扌
    注册冫变量名纟公用扌
    注册冫变量名纟私用扌
    取冫变量值扌
    '''#'''
    __slots__ = ()

    def 罓检查冫变量值扌(sf, 变量名, 变量值, /):
        pass
    @property
    def 匞参数配置包(sf, /):
        r'''
        :: -> 匞参数配置包
        #固化参数
        #用户数据纟场景固化
        '''#'''
        return None

    @property
    @abstractmethod
    def 罓注册处纟变量(sf, /):
        r'''
        :: -> 注册处纟变量/变量区/魖注册处<变量名,变量值>
        #只增参数
        '''#'''


    ######################

    def 欤已注册冫变量名扌(sf, 变量名, /):
        '-> 欤已注册/bool'
        欤已注册 = _取冫变量值扌(sf, 变量名, 鬽槑变量值:=None, 仅测试=True)
        return 欤已注册

    def 注册冫变量名纟公用扌(sf, 变量名纟公用, 变量值, /):
        '变量名纟公用/hashable -> 变量值 -> None'
        if 1:
            sf.罓检查冫变量值扌(变量名纟公用, 变量值)
        sf.罓注册处纟变量.注册纟公用扌(变量名纟公用, 变量值)
        return
    def 注册冫变量名纟私用扌(sf, 变量名纟私用, 私用空间, /):
        '变量名纟私用{eq==is} -> 私用空间/weakable_mapping<变量名纟私用,变量值> -> None #参见:乸私用空间,乸具名私用空间,乸私钥,乸具名私钥'
        if 1:
            变量值 = 私用空间[变量名纟私用]
            sf.罓检查冫变量值扌(变量名纟私用, 变量值)
        sf.罓注册处纟变量.注册纟私用扌(变量名纟私用, 变量值)
        return


    def 取冫变量值扌(sf, 变量名, 鬽槑变量值, /):
        '-> 变量值 | (^LookupError if miss 钥 and 鬽槑变量值 is None)'
        变量值 = _取冫变量值扌(sf, 变量名, 鬽槑变量值, 仅测试=False)
            # ^LookupError
        return 变量值

    ######################
#end-class 魖工厂场景(ABC):


class 乸可变真值(_4repr):
    def __init__(sf, b=False, /):
        sf._args
        if not sf._args:
            sf._args = (b,)
        assert sf._args[0] is b
        sf <<= b
    def __ilshift__(sf, b, /):
        check_type_is(bool, b)
        if not sf._args[0] is b:
            sf._args = (b, *sf._args[1:])
        return sf
    def __bool__(sf, /):
        return sf._args[0]

def __():
    assert not 乸可变真值()
    assert not 乸可变真值(False)
    b = 乸可变真值(False)
    assert not b
    assert repr(b) == '乸可变真值(False)'
    b <<= True
    assert b
    assert repr(b) == '乸可变真值(True)'
__()

__all__

from seed.recognize.toy.simple_recognizer_.register import 乸可变真值
from seed.recognize.toy.simple_recognizer_.register import 乸私用空间,乸具名私用空间,乸私钥,乸具名私钥
from seed.recognize.toy.simple_recognizer_.register import 魖注册处,乸具名注册处,乸具名注册处暨用户数据
from seed.recognize.toy.simple_recognizer_.register import 构造冫具名对象乊缺省扌,构造冫具名注册处乊缺省扌,构造冫具名注册处扌
from seed.recognize.toy.simple_recognizer_.register import 魖工厂场景,注册冫变量名纟公用扌,注册冫变量名纟私用扌,取冫变量值扌
from seed.recognize.toy.simple_recognizer_.register import *
