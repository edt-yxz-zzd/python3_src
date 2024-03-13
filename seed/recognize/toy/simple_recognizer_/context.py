#__all__:goto
r'''[[[

seed.recognize.toy.simple_recognizer_.context
py -m nn_ns.app.debug_cmd   seed.recognize.toy.simple_recognizer_.context -x
py -m nn_ns.app.doctest_cmd seed.recognize.toy.simple_recognizer_.context:__doc__



>>> 构造冫具名全文暨起讫讫扌(None, 'data', 'txt', 0, 1, 2)
乸全文暨起讫讫(乸全文暨讫讫(乸具名全文(None, 'data', 'txt'), 1, 2), 0)
>>> 构造冫具名全文暨起讫讫扌('x', 'data', 'txt', 0, 1, 2)
乸全文暨起讫讫(乸全文暨讫讫(x, 1, 2), 0)
>>> 构造冫具名全文暨起讫讫扌('x', 'data', 'txt', 0, 1, 2).全文
x
>>> 构造冫具名全文暨起讫讫扌(None, 'data', 'txt', 0, 1, 2).全文
乸具名全文(None, 'data', 'txt')
>>> 构造冫具名全文暨起讫讫扌('x', 'data', 'txt', 0, 1, 2).全文[:]
'txt'
>>> len(构造冫具名全文暨起讫讫扌('x', 'data', 'txt', 0, 1, 2).全文)
3
>>> 构造冫具名全文暨起讫讫扌('x', 'data', 'txt', 0, 1, 2).全文.用户数据纟全文随行
'data'

>>> 构造冫全文暨起讫讫扌('txt', 0, 1, 2)
乸全文暨起讫讫(乸全文暨讫讫('txt', 1, 2), 0)
>>> str(构造冫全文暨起讫讫扌('txt', 0, 1, 2))
"构造冫全文暨起讫讫扌('txt', 0, 1, 2)"
>>> 构造冫全文暨起讫讫扌('txt', 0, 1, 2) == 构造冫全文暨起讫讫扌('txt', 0, 1, 2)
True
>>> sf = 构造冫全文暨起讫讫扌('txt', 0, 2, 4)
Traceback (most recent call last):
    ...
seed.recognize.toy.simple_recognizer_.error.地址异常冖冖讫地址太大乊宽前瞻: (4, 3)
>>> sf = 构造冫全文暨起讫讫扌('text_', 0, 2, 4)
>>> str(sf)
"构造冫全文暨起讫讫扌('text_', 0, 2, 4)"
>>> str(sf << 2)
"构造冫全文暨起讫讫扌('text_', 2, 2, 4)"
>>> str(sf << 1)
"构造冫全文暨起讫讫扌('text_', 1, 2, 4)"
>>> str(sf << 0)
"构造冫全文暨起讫讫扌('text_', 0, 2, 4)"
>>> sf << -1
Traceback (most recent call last):
    ...
seed.recognize.toy.simple_recognizer_.error.地址异常冖冖起地址太小: (0, -1)
>>> sf << 3
Traceback (most recent call last):
    ...
seed.recognize.toy.simple_recognizer_.error.地址异常冖冖起讫范围不正常乊宽步进: (3, 2)
>>> str(sf)
"构造冫全文暨起讫讫扌('text_', 0, 2, 4)"
>>> (sf << 0) is sf
True

    全文
    讫地址乊宽
    起地址
    全文暨讫讫
    平铺直叙参数
>>> sf.全文
'text_'
>>> sf.起地址
0
>>> sf.讫地址乊宽
2
>>> sf.全文暨讫讫
乸全文暨讫讫('text_', 2, 4)
>>> sf.全文暨讫讫.平铺直叙参数()
('text_', 2, 4)
>>> sf.平铺直叙参数()
('text_', 0, 2, 4)

    更新冫起地址扌
>>> str(sf.更新冫起地址扌(2))
"构造冫全文暨起讫讫扌('text_', 2, 2, 4)"
>>> str(sf.更新冫起地址扌(1))
"构造冫全文暨起讫讫扌('text_', 1, 2, 4)"
>>> str(sf.更新冫起地址扌(0))
"构造冫全文暨起讫讫扌('text_', 0, 2, 4)"
>>> sf.更新冫起地址扌(-1)
Traceback (most recent call last):
    ...
seed.recognize.toy.simple_recognizer_.error.地址异常冖冖起地址太小: (0, -1)
>>> sf.更新冫起地址扌(3)
Traceback (most recent call last):
    ...
seed.recognize.toy.simple_recognizer_.error.地址异常冖冖起讫范围不正常乊宽步进: (3, 2)
>>> sf.更新冫起地址扌(0) is sf
True

    更新冫全文暨讫讫扌
>>> sf.更新冫全文暨讫讫扌(sf.全文暨讫讫) is sf
True

    限制步进扌
    限制前瞻扌
>>> sf.限制步进扌(2) is sf
True
>>> sf.限制步进扌(3) is sf
True
>>> sf.限制步进扌(1) is sf
False
>>> str(sf.限制步进扌(1))
"构造冫全文暨起讫讫扌('text_', 0, 1, 4)"
>>> str((sf<<1).限制步进扌(0))
Traceback (most recent call last):
    ...
seed.recognize.toy.simple_recognizer_.error.地址异常冖冖起讫范围不正常乊宽步进: (1, 0)
>>> sf.限制前瞻扌(4) is sf
True
>>> sf.限制前瞻扌(5) is sf
True
>>> sf.限制前瞻扌(3) is sf
False
>>> str(sf.限制前瞻扌(3))
"构造冫全文暨起讫讫扌('text_', 0, 2, 3)"
>>> str(sf.限制前瞻扌(2))
"构造冫全文暨起讫讫扌('text_', 0, 2, 2)"
>>> str(sf.限制前瞻扌(1))
"构造冫全文暨起讫讫扌('text_', 0, 1, 1)"
>>> str((sf<<1).限制前瞻扌(0))
Traceback (most recent call last):
    ...
seed.recognize.toy.simple_recognizer_.error.地址异常冖冖起讫范围不正常乊宽步进: (1, 0)


    乊乸前瞻零解码器冖冖临时扩张扌
>>> str(sf.乊乸前瞻零解码器冖冖临时扩张扌())
"构造冫全文暨起讫讫扌('text_', 0, 4, 4)"
>>> ot = 构造冫全文暨起讫讫扌('text_', 0, 1, 1)
>>> ot.乊乸前瞻零解码器冖冖临时扩张扌() is ot
True

    __new__
    __str__
    __lshift__

    __getitem__
>>> sf[:] is sf
True
>>> sf[None]
Traceback (most recent call last):
    ...
TypeError: <class 'NoneType'>

>>> str(sf[1])
"构造冫全文暨起讫讫扌('text_', 1, 2, 4)"
>>> str(sf[1:])
"构造冫全文暨起讫讫扌('text_', 1, 2, 4)"
>>> str(sf[:1])
"构造冫全文暨起讫讫扌('text_', 0, 1, 4)"
>>> str(sf[::3])
"构造冫全文暨起讫讫扌('text_', 0, 2, 3)"
>>> str(sf[::1])
"构造冫全文暨起讫讫扌('text_', 0, 1, 1)"
>>> sf[::4] is sf
True
>>> sf[0:2:4] is sf
True
>>> sf[:3:5] is sf
True
>>> sf[:8:5] is sf
True




>>> 乸具名全文冖冖记录讫地址(None, None, range(100, 200), 4)
乸具名全文冖冖记录讫地址(None, None, range(100, 200), 4)

>>> 全文 = 乸具名全文冖冖记录讫地址(None, None, range(100, 200), 4)
>>> 全文.全文
range(100, 200)
>>> len(全文)
100
>>> 全文.讫地址纟已访问
4
>>> 全文[3]
103
>>> 全文.讫地址纟已访问
4
>>> 全文[4]
104
>>> 全文.讫地址纟已访问
5
>>> 全文[4:6]
range(104, 106)
>>> 全文.讫地址纟已访问
6
>>> 全文[8:6:-1]
range(108, 106, -1)
>>> 全文.讫地址纟已访问
9



#]]]'''
__all__ = r'''
构造冫全文暨起讫讫扌
    乸全文暨起讫讫
        乸全文暨讫讫
乸具名全文
构造冫具名全文暨起讫讫扌

乸具名全文冖冖记录讫地址
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.recognize.toy.simple_recognizer_._common import abstractmethod, override, ABC
from seed.recognize.toy.simple_recognizer_._common import _4repr, _4repr_named, _巛彧
from seed.recognize.toy.simple_recognizer_._common import check_type_is, ifNone
from seed.helper.repr_input import repr_helper
___end_mark_of_excluded_global_names__0___ = ...
__all__




class 乸具名全文(_4repr_named):
    def __init__(sf, 鬽名, 用户数据纟全文随行, 全文, /):
        sf.__2 = 用户数据纟全文随行, 全文
    @property
    def 用户数据纟全文随行(sf, /):
        return sf.__2[0]
    @property
    def 全文(sf, /):
        return sf.__2[1]
    def __len__(sf, /):
        return len(sf.全文)
    def __getitem__(sf, k, /):
        return sf.全文[k]
class 乸具名全文冖冖记录讫地址(乸具名全文):
    def __init__(sf, 鬽名, 用户数据纟全文随行, 全文, 讫地址纟已访问, /):
        sf.__1 = 讫地址纟已访问
        super().__init__(鬽名, 用户数据纟全文随行, 全文)
    @property
    def 讫地址纟已访问(sf, /):
        return sf.__1
    def __getitem__(sf, k, /):
        if type(k) is int:
            y = k
        elif type(k) is slice:
            r = range(*k.indices(len(sf)))
            if not r:
                y = -2
            else:
                y = max(r[0], r[-1])
        else:
            raise TypeError(type(k))
        y += 1
        x = sf.讫地址纟已访问
        if x < y:
            sf.__1 = y
        return sf.全文[k]







__all__

def _检查起地址扌(起地址纟全文, 讫地址纟宽步进,     起地址, /):
    #  起地址 不允许 负数
    check_type_is(int, 起地址)
    if not 起地址纟全文 <= 起地址:
        raise 地址异常冖冖起地址太小(起地址纟全文, 起地址)
    if not 起地址 <= 讫地址纟宽步进:
        raise 地址异常冖冖起讫范围不正常乊宽步进(起地址, 讫地址纟宽步进)
    return
def _地址规范化扌(全文总长, 起地址纟全文,     鬽讫地址纟宽步进, 鬽讫地址纟宽前瞻, /):
    '-> (讫地址纟宽步进, 讫地址纟宽前瞻)'
    #免检:全文总长, 起地址纟全文

    if 鬽讫地址纟宽前瞻 is None:
        讫地址纟宽前瞻 = 全文总长
    else:
        讫地址纟宽前瞻 = 鬽讫地址纟宽前瞻
        check_type_is(int, 讫地址纟宽前瞻)
        if not 讫地址纟宽前瞻 <= 全文总长:
            raise 地址异常冖冖讫地址太大乊宽前瞻(讫地址纟宽前瞻, 全文总长)
    #  鬽讫地址纟宽前瞻 不允许 负数
    #  鬽讫地址纟宽步进 不允许 负数

    if 鬽讫地址纟宽步进 is None:
        讫地址纟宽步进 = 讫地址纟宽前瞻
    else:
        讫地址纟宽步进 = 鬽讫地址纟宽步进
        check_type_is(int, 讫地址纟宽步进)
        if not 讫地址纟宽步进 <= 讫地址纟宽前瞻:
            raise 地址异常冖冖讫地址太大乊宽步进(讫地址纟宽步进, 讫地址纟宽前瞻)
    if not 起地址纟全文 <= 讫地址纟宽步进:
        raise 地址异常冖冖讫地址太小乊宽步进(起地址纟全文, 讫地址纟宽步进)
    return (讫地址纟宽步进, 讫地址纟宽前瞻)




#class _乸散列暨显示(_4repr):
#    def __hash__(sf, /):
#        return hash((type(sf), sf._args))
#class 乸全文暨讫讫(_乸散列暨显示):
class 乸全文暨讫讫(_4repr):
    '极少变更'
    #全文暨讫讫==全文+讫地址纟宽步进+讫地址纟宽前瞻
    def 平铺直叙参数(sf, /):
        return (sf.全文, sf.讫地址纟宽步进, sf.讫地址纟宽前瞻)
    @property
    def 全文(sf, /):
        return sf._args[0]
        return sf._全文
    @property
    def 讫地址纟宽步进(sf, /):
        return sf._args[1]
        return sf._讫地址纟宽步进
    @property
    def 讫地址纟宽前瞻(sf, /):
        return sf._args[2]
        return sf._讫地址纟宽前瞻
    ######################
    def 限制步进扌(sf, 讫地址纟宽步进, /):
        if not 讫地址纟宽步进 < sf.讫地址纟宽步进:
            return sf
        return type(sf)(sf.全文, 讫地址纟宽步进, sf.讫地址纟宽前瞻)
    def 限制前瞻扌(sf, 讫地址纟宽前瞻, /):
        if not 讫地址纟宽前瞻 < sf.讫地址纟宽前瞻:
            return sf
        讫地址纟宽步进 = min(sf.讫地址纟宽步进, 讫地址纟宽前瞻)
        return type(sf)(sf.全文, 讫地址纟宽步进, 讫地址纟宽前瞻)
    ######################

    def __new__(cls, 全文, 鬽讫地址纟宽步进, 鬽讫地址纟宽前瞻, /, *, _欤免检=False):
        if _欤免检:
            (讫地址纟宽步进, 讫地址纟宽前瞻) = (鬽讫地址纟宽步进, 鬽讫地址纟宽前瞻)
        else:
            (讫地址纟宽步进, 讫地址纟宽前瞻) = _地址规范化扌(全文总长:=len(全文), 起地址纟全文:=0,     鬽讫地址纟宽步进, 鬽讫地址纟宽前瞻)
        sf = super(__class__, cls).__new__(cls, 全文, 讫地址纟宽步进, 讫地址纟宽前瞻)
        return sf
        sf._全文 = 全文
        sf._讫地址纟宽步进 = 讫地址纟宽步进
        sf._讫地址纟宽前瞻 = 讫地址纟宽前瞻
    ######################
    def 乊乸前瞻零解码器冖冖临时扩张扌(sf, /):
        讫地址纟宽步进 = sf.讫地址纟宽前瞻
        if 讫地址纟宽步进 == sf.讫地址纟宽步进:
            return sf
        return type(sf)(sf.全文, 讫地址纟宽步进, sf.讫地址纟宽前瞻, _欤免检=True)
    ######################
    def __getitem__(sf, 鬽讫地址丶鬽讫地址, /):
        (鬽讫地址纟宽步进, 鬽讫地址纟宽前瞻) = 鬽讫地址丶鬽讫地址
        ######################
        if not 鬽讫地址纟宽前瞻 is None:
            讫地址纟宽前瞻 = 鬽讫地址纟宽前瞻
            sf = sf.限制前瞻扌(讫地址纟宽前瞻)
        ######################
        #先:前瞻，再:步进
        #   <<== 最小化修改
        ######################
        if not 鬽讫地址纟宽步进 is None:
            讫地址纟宽步进 = 鬽讫地址纟宽步进
            sf = sf.限制步进扌(讫地址纟宽步进)
        ######################
        return sf
    #end-def __getitem__
#end-class 乸全文暨讫讫(_4repr):


class 构造冫具名全文暨起讫讫扌(_4repr):
    def __new__(cls, 鬽名, 用户数据纟全文随行, 全文, 起地址, 鬽讫地址纟宽步进, 鬽讫地址纟宽前瞻, /):
        cls = None
        具名全文 = 乸具名全文(鬽名, 用户数据纟全文随行, 全文)
        全文暨起讫讫 = 构造冫全文暨起讫讫扌(具名全文, 起地址, 鬽讫地址纟宽步进, 鬽讫地址纟宽前瞻)
        return 全文暨起讫讫
class 构造冫全文暨起讫讫扌(_4repr):
    #全文暨起讫讫==全文暨讫讫+起地址
    #全文暨讫讫==全文+讫地址纟宽步进+讫地址纟宽前瞻
    #
    def __new__(cls, 全文, 起地址, 鬽讫地址纟宽步进, 鬽讫地址纟宽前瞻, /):
        cls = None
        全文暨讫讫 = 乸全文暨讫讫(全文, 鬽讫地址纟宽步进, 鬽讫地址纟宽前瞻)
        全文暨起讫讫 = 乸全文暨起讫讫(全文暨讫讫, 起地址)
        return 全文暨起讫讫
_obj4nm4repr = object.__new__(构造冫全文暨起讫讫扌)
class 乸全文暨起讫讫(_4repr):
    r'''[[[
    前瞻讫地址
    前瞻讫地址冃上限===讫地址纟全文
    解码讫地址冃上限===讫地址乊宽
    [0 <= 起地址纟全文 <= 起地址 <= 讫地址乊严 <= 解码讫地址冃上限===讫地址乊宽 <= 前瞻讫地址冃上限===讫地址纟全文 <= len(全文)]
    其中, 变化最快最多的是『起地址』
        其次是『讫地址乊宽』
            #『讫地址乊严』是 返回值 暨 下一个『起地址』
        再次是『讫地址纟全文』
===
===
===
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.recognize.toy.simple_recognizer_.context:乸全文暨起讫讫@T    =T      ++exclude_prefixes:_       +exclude_attrs5listed_in_cls_doc
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.recognize.toy.simple_recognizer_.context:乸全文暨起讫讫@T    =T            +exclude_attrs5listed_in_cls_doc
===:
new_concrete_methods:
    平铺直叙参数
    全文
    讫地址乊宽
    起地址
    全文暨讫讫
    更新冫起地址扌
    更新冫全文暨讫讫扌
    乊乸前瞻零解码器冖冖临时扩张扌
    限制步进扌
    限制前瞻扌
    __str__
    __getitem__
    __new__
    __lshift__
===
===
===
    #]]]'''#'''
    #全文暨起讫讫==全文暨讫讫+起地址
    def 平铺直叙参数(sf, /):
        (全文, 讫地址纟宽步进, 讫地址纟宽前瞻) = sf.全文暨讫讫.平铺直叙参数()
        return (全文, sf.起地址, 讫地址纟宽步进, 讫地址纟宽前瞻)
    def __str__(sf, /):
        return repr_helper(_obj4nm4repr, *sf.平铺直叙参数())
    #def __repr__(sf, /):
    #    return repr_helper(sf, *sf._args)
    def __getitem__(sf, 起地址丨丮鬽起地址丶鬽讫地址丶鬽讫地址厈, /):
        k = 起地址丨丮鬽起地址丶鬽讫地址丶鬽讫地址厈
        if type(k) is int:
            起地址 = k
            return sf << 起地址
        if not type(k) is slice:
            raise TypeError(type(k))
        sl = k
        #if not sl.step is None: raise TypeError(sl)
        鬽起地址 = sl.start
        #鬽讫地址乊宽 = sl.stop
        鬽讫地址纟宽步进 = sl.stop
        鬽讫地址纟宽前瞻 = sl.step
        ######################
        if not 鬽起地址 is None:
            起地址 = 鬽起地址
            sf <<= 起地址
        if not (鬽讫地址纟宽步进 is None is 鬽讫地址纟宽前瞻):
            鬽讫地址丶鬽讫地址 = (鬽讫地址纟宽步进, 鬽讫地址纟宽前瞻)
            x = sf.全文暨讫讫[鬽讫地址丶鬽讫地址]
            sf = sf.更新冫全文暨讫讫扌(x)
        return sf
    #end-def __getitem__

    def __new__(cls, 全文暨讫讫, 起地址, /, *, __lshift__=False):
        if __lshift__:
            sf4old = 全文暨讫讫
            check_type_is(cls, sf4old)
            #讫地址乊严 = 起地址
            #起地址 = 讫地址乊严
            起地址纟全文 = sf4old.起地址
            全文暨讫讫 = sf4old.全文暨讫讫
        else:
            check_type_is(乸全文暨讫讫, 全文暨讫讫)
            起地址纟全文 = 0
            全文暨讫讫

        起地址
        _检查起地址扌(起地址纟全文, 全文暨讫讫.讫地址纟宽步进,     起地址)
        sf = super(__class__, cls).__new__(cls, 全文暨讫讫, 起地址)
        return sf
        sf._全文暨讫讫 = 全文暨讫讫
        sf._起地址 = 起地址
        pass
    #def __init__(sf, 全文, 起地址, 鬽讫地址纟宽步进, 鬽讫地址纟宽前瞻, /):
        #构造冫全文暨起讫讫扌

    @property
    def 全文(sf, /):
        return sf.全文暨讫讫.全文
    @property
    def 讫地址乊宽(sf, /):
        #这里没有:讫地址纟宽前瞻
        #   <<== 它只用于 乸前瞻解码器:通过 乊乸前瞻零解码器冖冖临时扩张扌 提现，并不需要输出接口
        return sf.全文暨讫讫.讫地址纟宽步进
    @property
    def 起地址(sf, /):
        return sf._args[1]
        return sf._起地址
    @property
    def 全文暨讫讫(sf, /):
        return sf._args[0]
        return sf._全文暨讫讫

    ######################
    def __lshift__(sf, 讫地址乊严, /):
        if 讫地址乊严 == sf.起地址:
            return sf
        return type(sf)(sf, 起地址:=讫地址乊严, __lshift__=True)
    def 更新冫起地址扌(sf, 起地址, /):
        return sf << 起地址
    ######################
    def 更新冫全文暨讫讫扌(sf, 全文暨讫讫, /):
        if 全文暨讫讫 is sf.全文暨讫讫:
            return sf
        return type(sf)(全文暨讫讫, sf.起地址)
    ######################
    ######################
    def 限制步进扌(sf, 讫地址纟宽步进, /):
        x = sf.全文暨讫讫.限制步进扌(讫地址纟宽步进)
        return sf.更新冫全文暨讫讫扌(x)
    def 限制前瞻扌(sf, 讫地址纟宽前瞻, /):
        x = sf.全文暨讫讫.限制前瞻扌(讫地址纟宽前瞻)
        return sf.更新冫全文暨讫讫扌(x)
    ######################
    def 乊乸前瞻零解码器冖冖临时扩张扌(sf, /):
        全文暨讫讫 = sf.全文暨讫讫.乊乸前瞻零解码器冖冖临时扩张扌()
        return sf.更新冫全文暨讫讫扌(全文暨讫讫)
    ######################
#end-class 乸全文暨起讫讫(_4repr):



__all__
___begin_mark_of_excluded_global_names__999___ = ...
from seed.recognize.toy.simple_recognizer_.error import \
(地址异常
,地址异常冖冖起地址太小
,地址异常冖冖讫地址太大乊宽步进
,地址异常冖冖讫地址太大乊宽前瞻
,地址异常冖冖讫地址太小乊宽步进
,地址异常冖冖起讫范围不正常乊宽步进
)
___end_mark_of_excluded_global_names__999___ = ...
from seed.recognize.toy.simple_recognizer_.context import 乸具名全文冖冖记录讫地址
from seed.recognize.toy.simple_recognizer_.context import 构造冫全文暨起讫讫扌, 乸具名全文, 构造冫具名全文暨起讫讫扌
from seed.recognize.toy.simple_recognizer_.context import 乸全文暨起讫讫

from seed.recognize.toy.simple_recognizer_.context import 构造冫全文暨起讫讫扌,乸全文暨起讫讫,乸全文暨讫讫
from seed.recognize.toy.simple_recognizer_.context import *
