#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/toy/simple_recognizer_/basic.py
grep '包装灬扌\|乸两段式篡改器'  ../../python3_src/seed/recognize/toy/simple_recognizer_/*.py -l -a
    ++乊起始扌


seed.recognize.toy.simple_recognizer_.basic
py -m nn_ns.app.debug_cmd   seed.recognize.toy.simple_recognizer_.basic -x
py -m nn_ns.app.doctest_cmd seed.recognize.toy.simple_recognizer_.basic:__doc__
py_adhoc_call   seed.recognize.toy.simple_recognizer_.basic   @f
#]]]'''
__all__ = r'''
at
乸具名引用变量

乸具名码集
构造冫具名函数扌
    乸具名函数
    None8echo

检查冫讫错果扌
检查冫讫错果冖扩展扌

魖两段式篡改器
    乸两段式篡改器
魖讫错果变换器
    乸讫错果变换器
    惑构造冫讫错果变换器扌
    变换器冫取原文片段

魖错果变换器
    乸错果变换器
    乸结果变换器
    惑构造冫结果变换器扌


the_one_

大写字母表
小写字母表
英文字母表
字母数字表
数字表
标识体字集
标识首字集
空白字集

'''.split()#'''
__all__



from seed.recognize.toy.simple_recognizer_._common import abstractmethod, override, ABC
from seed.recognize.toy.simple_recognizer_._common import _4repr, _4repr_named, _巛彧
from seed.recognize.toy.simple_recognizer_._common import check_type_le, check_type_is, ifNone, echo
from seed.recognize.toy.simple_recognizer_._common import check_int_ge_le, check_int_ge
from seed.tiny_.check import check_may_, check_not_
from seed.tiny_.check import check_callable
from seed.recognize.toy.simple_recognizer_.error import \
(解码失败冖冖宽严讫地址不同
,解码失败冖冖不匹配
,解引用异常冖冖循环引用
)
from seed.for_libs.for_inspect import check_num_args_ok_, is_num_args_ok_



from functools import update_wrapper

from seed.lang.slice_show import show_slice_ as _show_slice_
def _show_slice_ex_(k, /):
    f = _show_slice_ if type(k) is slice else repr
    return f(k)
#from seed.tiny_.at import at
class _At:
    def __new__(cls, /):
        try:
            return at
        except NameError:
            return super().__new__(cls)
    def __getitem__(sf, k, /):
        return _AT(k)
    def __repr__(sf, /):
        return f'at'
at = _At()
assert at is _At()
class _AT:
    def __init__(sf, k_or_ks, /):
        if type(k_or_ks) in (int,slice):
            iks = k = k_or_ks
        else:
            iks = ks = tuple(k_or_ks)
        sf._iks = iks
    def __call__(sf, ls, /):
        iks = sf._iks
        if type(iks) in (int,slice):
            k = iks
            return ls[k]
        ks = iks
        return tuple(x for k in ks for x in ls[k])
    def __repr__(sf, /):
        iks = sf._iks
        if type(iks) in (int,slice):
            k = iks
            s = _show_slice_ex_(k)
        else:
            ks = iks
            ss = [*map(_show_slice_ex_, ks)]
            s = ', '.join(ss)
            if len(ss) == 1:
                s += ','
        return f'at[{s!s}]'
assert at[1]('ab') == 'b'
assert {at}
assert {at[0]}
assert at[1,]('ab') == ('b',)
assert at[1,1]('ab') == ('b', 'b')
assert at[()]('ab') == ()
assert at[1,:]('ab') == ('b', 'a', 'b')


at
class 乸具名引用变量(_4repr_named):
    r'''
    变果式:callable (果->果) vs: non_callable乸具名引用变量.call::(场景->果->果) #用于 查询用户自定义变量

    [彧鬽名 :: ... | None | 名]
    [[彧鬽名 is ...] -> [变量名 :: 名]]
    [参数数目 :: int{>=-1}]
        -1 表示 变量值 不是 函数
    [变量名 :: hashable]

    '''#'''
    def __new__(cls, 彧鬽名, 鬽变量类型, 参数数目, 变量名, /):
        '乸具名引用变量(彧鬽名, 鬽变量类型, 参数数目, 变量名)'
        鬽名 = _巛彧(彧鬽名, 变量名)
        sf = super(__class__, cls).__new__(cls, 鬽名, 鬽变量类型, 参数数目, 变量名)
        check_int_ge(-1, 参数数目)
        check_may_([check_type_le, type], 鬽变量类型)
        hash(变量名)
        return sf
    @property
    def 鬽变量类型(sf, /):
        return sf._args[1]
    @property
    def 参数数目(sf, /):
        return sf._args[2]
    @property
    def 变量名(sf, /):
        return sf._args[3]
    #def __call__(sf, /, *args, **kwds):
    #def call(sf, 场景, 结果, /):
    def 取冫变量值巛场景扌(sf, 场景, /, *, 递归丷单步=False):
        x = 场景.取冫变量值扌(sf.变量名, None)
        if 递归丷单步:
            return x
        ids = set()
        ks = set()
        xks = []
        while type(x) is 乸具名引用变量:
            #if x.参数数目 in (1,4) or issubclass(x.鬽变量类型, 魖讫错果变换器):
            k = x.变量名
            xks.append((x, k))
            i = id(x)
            if i in ids or k in ks:
                raise 解引用异常冖冖循环引用(xks)
            ids.add(i)
            ks.add(k)
            x = 场景.取冫变量值扌(k, None)
        assert not isinstance(x, 乸具名引用变量)
        return x
#end-class 乸具名引用变量(_4repr_named):


class 乸具名码集(_4repr_named):
    '用于 码集式: 稳定显示'
    def __init__(sf, 鬽名, 包含扌丨码集, /):
        pass
    def __contains__(sf, k, /):
        m, f_or_ks = sf._args
        if callable(f_or_ks):
            f = f_or_ks
            return f(k)
        ks = f_or_ks
        return k in ks

def _巛彧鬽名(彧鬽名, 函数, /):
    鬽名 = _巛彧(彧鬽名, getattr(函数, '__name__', None))
    return 鬽名
def 构造冫具名函数扌(彧名, 函数, /):
    名 = _巛彧鬽名(彧名, 函数)
    return 乸具名函数(名, 函数)
class 乸具名函数(_4repr_named):
    '用于 变果式: 稳定显示'
    #def __new__(cls, 彧名, 函数, /, *args):
    #    if 彧名 is ...:
    #        名 = 函数.__name__
    def __init__(sf, 名, 函数, /):
        if not callable(函数): raise TypeError(type(函数))
        #check_pseudo_identifier(名)
            #_4repr_named
        check_type_is(str, 名)
        #sf.__f = 函数
        update_wrapper(sf, 函数)
    def __call__(sf, /, *args, **kwds):
        #f = sf.__f
        f = sf.__wrapped__
        return f(*args, **kwds)
    #inspect.signature(callable, *, follow_wrapped=True) -> Signature
    #.__wrapped__=f
    #@property
    #def __wrapped__(sf, /):
    #    return sf.__f
None8echo = 乸具名函数('None', echo)

def 检查冫讫错果扌(全文暨起讫讫, r, /):
    check_type_is(tuple, r)
    (讫地址, 错误丷结果, 错误丨结果) = r
    check_type_is(bool, 错误丷结果)
    check_int_ge_le(全文暨起讫讫.起地址, 全文暨起讫讫.讫地址乊宽,    讫地址)
def 检查冫讫错果冖扩展扌(sf, 宽丷严, 欤不容错, 全文暨起讫讫, r, /):
    检查冫讫错果扌(全文暨起讫讫, r)

    if 宽丷严 or 欤不容错:
        (讫地址, 错误丷结果, 错误丨结果) = r

    if 宽丷严 and 错误丷结果:
        讫地址乊严 = 讫地址#匹配=>乊严
        讫地址乊宽 = 全文暨起讫讫.讫地址乊宽
        if not 讫地址乊严 == 讫地址乊宽: raise 解码失败冖冖宽严讫地址不同(讫地址乊宽, 讫地址乊严)
    if 欤不容错 and not 错误丷结果:
        讫地址乊错 = 讫地址#匹配=>乊错
        错误 = 错误丨结果
        raise 解码失败冖冖不匹配(sf, 全文暨起讫讫.起地址, 讫地址乊错, 错误)

检查冫讫错果扌
检查冫讫错果冖扩展扌


class 魖两段式篡改器(ABC):
    r'''
!!必须non_callable!!
见:乸两段式篡改器<:魖两段式篡改器
见:乸包装解码器<:乸魖包装解码器
提供完整信息:
乊起始扌 :: 包装解码器 -> 全文暨起讫讫 -> None
乊锁定扌,乊失败扌,乊匹配扌,乊结束扌 :: 包装解码器 -> 全文暨起讫讫 -> 讫错果 -> 讫错果
包装解码器:
    .场景
    .解码器名
    .两段式篡改器
        .乊起始扌
        .乊锁定扌
        .乊失败扌
        .乊匹配扌
        .乊结束扌

    '''#'''
    __slots__ = ()
    @abstractmethod
    def 乊起始扌(sf, 包装解码器, 全文暨起讫讫, /):
        '包装解码器 -> 全文暨起讫讫 -> None'
        #用于:调试
    @abstractmethod
    def 乊锁定扌(sf, 包装解码器, 全文暨起讫讫, 讫错果, /):
        '包装解码器 -> 全文暨起讫讫 -> 讫错果 -> 讫错果'
    @abstractmethod
    def 乊失败扌(sf, 包装解码器, 全文暨起讫讫, 讫错果, /):
        '包装解码器 -> 全文暨起讫讫 -> 讫错果 -> 讫错果'
    @abstractmethod
    def 乊匹配扌(sf, 包装解码器, 全文暨起讫讫, 讫错果, /):
        '包装解码器 -> 全文暨起讫讫 -> 讫错果 -> 讫错果'
    @abstractmethod
    def 乊结束扌(sf, 包装解码器, 全文暨起讫讫, 讫错果, /):
        '包装解码器 -> 全文暨起讫讫 -> 讫错果 -> 讫错果'


def _echo_4(场景, 解码器名, 全文暨起讫讫, 讫错果, /):
    '[变换讫错果扌 :: (场景 -> 解码器 -> 全文暨起讫讫 -> 讫错果 -> 讫错果)]'
    return 讫错果
def _do_nothing(包装解码器, 全文暨起讫讫, /):
    '乊起始扌 :: 包装解码器 -> 全文暨起讫讫 -> None'
    return None
def _echo_3(包装解码器, 全文暨起讫讫, 讫错果, /):
    '乊锁定扌,... :: 包装解码器 -> 全文暨起讫讫 -> 讫错果 -> 讫错果'
    return 讫错果
_echo_3 = 乸具名函数('None', _echo_3)
_do_nothing = 乸具名函数('None', _do_nothing)
class 乸两段式篡改器(_4repr_named, 魖两段式篡改器):
    ___no_slots_ok___ = True
    __doc__ = 魖两段式篡改器.__doc__
    def __init__(sf, 鬽名, 乊起始扌,乊锁定扌, 乊失败扌, 乊匹配扌, 乊结束扌, /):
        '[乊锁定扌, 乊失败扌, 乊匹配扌, 乊结束扌:: 包装解码器 -> 全文暨起讫讫 -> 讫错果 -> 讫错果]'
        '乸两段式篡改器(鬽名, 乊锁定扌, 乊失败扌, 乊匹配扌, 乊结束扌)'
        乊起始扌 = ifNone(乊起始扌,_do_nothing)
        f = sf.__1 = 乊起始扌
        check_num_args_ok_(2, f)

        fs = sf.__4 = [_echo_3 if m is None else m for m in [乊锁定扌, 乊失败扌, 乊匹配扌, 乊结束扌]]
        for f in fs:
            check_num_args_ok_(3, f)
    @property
    @override
    def 乊起始扌(sf, /):
        '-> (包装解码器 -> 全文暨起讫讫 -> None)'
        #用于:调试
        return sf.__1
    @property
    @override
    def 乊锁定扌(sf, /):
        '-> (包装解码器 -> 全文暨起讫讫 -> 讫错果 -> 讫错果)'
        return sf.__4[0]
    @property
    @override
    def 乊失败扌(sf, /):
        '-> (包装解码器 -> 全文暨起讫讫 -> 讫错果 -> 讫错果)'
        return sf.__4[1]
    @property
    @override
    def 乊匹配扌(sf, /):
        '-> (包装解码器 -> 全文暨起讫讫 -> 讫错果 -> 讫错果)'
        return sf.__4[2]
    @property
    @override
    def 乊结束扌(sf, /):
        '-> (包装解码器 -> 全文暨起讫讫 -> 讫错果 -> 讫错果)'
        return sf.__4[3]


class 魖讫错果变换器(魖两段式篡改器):
    r'''
    !!必须non_callable!!
    配合 乸变换讫错果解码器
    now:[魖讫错果变换器 <: 魖两段式篡改器]
    '''#'''
    __slots__ = ()
    @abstractmethod
    def 罓变换讫错果扌(sf, 场景, 解码器名, 全文暨起讫讫, 讫错果, /):
        '-> 讫错果/(讫地址乊严, 错误丷结果, 错误丨结果)'
    def 变换讫错果扌(sf, 场景, 解码器名, 全文暨起讫讫, 讫错果, /):
        '-> 讫错果/(讫地址乊严, 错误丷结果, 错误丨结果)'
        r = sf.罓变换讫错果扌(场景, 解码器名, 全文暨起讫讫, 讫错果)
        检查冫讫错果扌(全文暨起讫讫, r)
        return r
    乊起始扌 = _do_nothing
    乊锁定扌 = _echo_3
    乊失败扌 = _echo_3
    乊匹配扌 = _echo_3
    @override
    def 乊结束扌(sf, 包装解码器, 全文暨起讫讫, 讫错果, /):
        '包装解码器 -> 全文暨起讫讫 -> 讫错果 -> 讫错果'
        return sf.变换讫错果扌(包装解码器.场景, 包装解码器.解码器名, 全文暨起讫讫, 讫错果)


class 乸讫错果变换器(_4repr_named, 魖讫错果变换器):
    '[变换讫错果扌 :: (场景 -> 解码器 -> 全文暨起讫讫 -> 讫错果 -> 讫错果)]'
    ___no_slots_ok___ = True
    def __init__(sf, 鬽名, 鬽变换讫错果扌, /):
        变换讫错果扌 = ifNone(鬽变换讫错果扌, _echo_4)
        #check_callable(变换讫错果扌)
        check_num_args_ok_(4, 变换讫错果扌)
        check_not_([check_type_le, 魖讫错果变换器], 变换讫错果扌)
        sf._f = 变换讫错果扌
    @override
    def 罓变换讫错果扌(sf, 场景, 解码器名, 全文暨起讫讫, 讫错果, /):
        '-> 讫错果/(讫地址乊严, 错误丷结果, 错误丨结果)'
        变换讫错果扌 = sf._f
        return 变换讫错果扌(场景, 解码器名, 全文暨起讫讫, 讫错果)

def 惑构造冫讫错果变换器扌(彧鬽名, 鬽变换讫错果扌丨两段式篡改器, /):
    '-> 两段式篡改器/魖两段式篡改器'
    if (鬽变换讫错果扌丨两段式篡改器 is None) or callable(鬽变换讫错果扌丨两段式篡改器):
        鬽变换讫错果扌 = 鬽变换讫错果扌丨两段式篡改器
        鬽名 = _巛彧鬽名(彧鬽名, 鬽变换讫错果扌)
        两段式篡改器 = 讫错果变换器 = 乸讫错果变换器(鬽名, 鬽变换讫错果扌)
    else:
        两段式篡改器 = 鬽变换讫错果扌丨两段式篡改器
        check_type_le(魖两段式篡改器, 两段式篡改器)
    return 两段式篡改器


def 变换器冫取原文片段(场景, 解码器, 全文暨起讫讫, 讫错果, /):
    '[变换讫错果扌 :: (场景 -> 解码器 -> 全文暨起讫讫 -> 讫错果 -> 讫错果)]'
    (讫地址乊严, 错误丷结果, 错误丨结果) = 讫错果
    if 错误丷结果:
        原文片段 = 全文暨起讫讫.全文[全文暨起讫讫.起地址:(讫地址乊果:=讫地址乊严)]
        讫错果 = (讫地址乊严, 错误丷结果, 错误丨结果:=原文片段)
    return 讫错果
变换器冫取原文片段 = 惑构造冫讫错果变换器扌(..., 变换器冫取原文片段)


class 魖错果变换器(魖讫错果变换器):
    r'''
    !!必须non_callable!!
    配合 乸变换结果解码器/乸变换讫错果解码器
    用于 更新代码:
        乸变换结果解码器-->乸变换讫错果解码器
    '''#'''
    __slots__ = ()
    @abstractmethod
    def 变换错误扌(sf, 错误, /):
        '-> 错误'
    @abstractmethod
    def 变换结果扌(sf, 结果, /):
        '-> 结果'
    @override
    def 罓变换讫错果扌(sf, 场景, 解码器名, 全文暨起讫讫, 讫错果, /):
        '-> 讫错果/(讫地址乊严, 错误丷结果, 错误丨结果)'
        (讫地址乊严, 错误丷结果, 错误丨结果) = 讫错果
        变换错果扌 = sf.变换错误扌 if not 错误丷结果 else sf.变换结果扌

        return (讫地址乊严, 错误丷结果, 变换错果扌(错误丨结果))
class 乸错果变换器(_4repr_named, 魖错果变换器):
    ___no_slots_ok___ = True
    def __init__(sf, 鬽名, 鬽变换错误扌, 鬽变换结果扌, /):
        变换错误扌 = ifNone(鬽变换错误扌, None8echo)
        变换结果扌 = ifNone(鬽变换结果扌, None8echo)
        check_callable(变换错误扌)
        check_callable(变换结果扌)
        sf.__2 = 变换错误扌,变换结果扌

        check_num_args_ok_(1, 变换错误扌, ok_if_no_signature=True)
        check_num_args_ok_(1, 变换结果扌, ok_if_no_signature=True)
    @property
    @override
    def 变换错误扌(sf, /):
        return sf.__2[0]
    @property
    @override
    def 变换结果扌(sf, /):
        return sf.__2[1]
class 乸结果变换器(_4repr_named, 魖错果变换器):
    ___no_slots_ok___ = True
    def __init__(sf, 鬽名, 鬽变换结果扌, /):
        变换结果扌 = ifNone(鬽变换结果扌, None8echo)
        check_callable(变换结果扌)
        sf.__1 = 变换结果扌

        check_num_args_ok_(1, 变换结果扌, ok_if_no_signature=True)
    变换错误扌 = None8echo
    @property
    @override
    def 变换结果扌(sf, /):
        return sf.__1

assert is_num_args_ok_(1, bool, ok_if_no_signature=True)
def 惑构造冫结果变换器扌(彧鬽名, 鬽变换错误扌, 鬽变换结果扌丨变换讫错果扌丨两段式篡改器, /):
    '-> 两段式篡改器/魖两段式篡改器#不能 合并到 惑构造冫讫错果变换器扌<<==当函数同时支持1/4个参数时，无法区分'
    if not 鬽变换错误扌 is None:
        变换错误扌 = 鬽变换错误扌
        鬽变换结果扌 = 鬽变换结果扌丨变换讫错果扌丨两段式篡改器
        鬽名 = _巛彧鬽名(彧鬽名, 鬽变换结果扌)
        两段式篡改器 = 讫错果变换器 = 错果变换器 = 乸错果变换器(鬽名, 变换错误扌, 鬽变换结果扌)
    elif is_num_args_ok_(1, 鬽变换结果扌丨变换讫错果扌丨两段式篡改器, ok_if_no_signature=True):
        变换结果扌 = 鬽变换结果扌丨变换讫错果扌丨两段式篡改器
        鬽名 = _巛彧鬽名(彧鬽名, 变换结果扌)
        两段式篡改器 = 讫错果变换器 = 结果变换器 = 乸结果变换器(鬽名, 变换结果扌)
    else:
        鬽变换讫错果扌丨两段式篡改器 = 鬽变换结果扌丨变换讫错果扌丨两段式篡改器
        两段式篡改器 = 惑构造冫讫错果变换器扌(彧鬽名, 鬽变换讫错果扌丨两段式篡改器)
    return 两段式篡改器



def the_one_(ls, /):
    [x] = ls
    return x
the_one_ = 乸具名函数('the_one_', the_one_)
######################
大写字母表 = 乸具名码集('英文字母表', str.isupper)
小写字母表 = 乸具名码集('英文字母表', str.islower)

英文字母表 = 乸具名码集('英文字母表', str.isalpha)
字母数字表 = 乸具名码集('字母数字表', str.isalnum)
数字表 = 乸具名码集('数字表', str.isdigit)
标识体字集 = 乸具名码集('标识体字集', lambda ch:str.isdigit(ch) or ch.isidentifier())
标识首字集 = 乸具名码集('标识首字集', str.isidentifier)
空白字集 = 乸具名码集('空白字集', str.isspace)
######################


__all__
from seed.recognize.toy.simple_recognizer_.basic import 大写字母表,小写字母表,英文字母表,字母数字表,数字表,标识体字集,标识首字集,空白字集
from seed.recognize.toy.simple_recognizer_.basic import the_one_
from seed.recognize.toy.simple_recognizer_.basic import 魖错果变换器,乸错果变换器,乸结果变换器,惑构造冫结果变换器扌
from seed.recognize.toy.simple_recognizer_.basic import 魖讫错果变换器,乸讫错果变换器,惑构造冫讫错果变换器扌,变换器冫取原文片段
from seed.recognize.toy.simple_recognizer_.basic import 魖两段式篡改器,乸两段式篡改器
from seed.recognize.toy.simple_recognizer_.basic import at, 乸具名引用变量
    # [at :: callable]
from seed.recognize.toy.simple_recognizer_.basic import 乸具名码集, 构造冫具名函数扌, 乸具名函数, None8echo
from seed.recognize.toy.simple_recognizer_.basic import 检查冫讫错果扌,检查冫讫错果冖扩展扌
from seed.recognize.toy.simple_recognizer_.basic import *
