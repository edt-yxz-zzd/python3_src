#__all__:goto
r'''[[[
e ../../python3_src/seed/types/MakeDict.py
[[
see:
    seed.tiny_.bmk_pairs
        bracket-make-pairs
        using __getitem__, not __call__

    seed.types.MakeDict
        baseclass
        using "class"

    seed.for_libs.for_inspect
        @decorator
        using api-signature #inspect.getfullargspec

    seed.helper.mk_pairs
        asm above
]]

[[usage:

######################
from seed.types.MakeDict import MakeDict, MakeOrderedDict, MakeOrderedDict__replace_then_move_to_end, ListSortedItems, ListOrderedItems, ListOrderedItems__replace_then_move_to_end
class d(MakeDict):
class d(MakeOrderedDict):
class d(MakeOrderedDict__replace_then_move_to_end):
class ps(ListSortedItems):
class ps(ListOrderedItems):
class ps(ListOrderedItems__replace_then_move_to_end):

######################
from seed.types.MakeDict import MakeDict, OrderedDict, OrderedDict__replace_then_move_to_end
class d(MakeDict):
class d(MakeDict, dict8ns=OrderedDict()):
class d(MakeDict, dict8ns=OrderedDict__replace_then_move_to_end()):
class d(MakeDict, dict8ns='ordered_dict'):
class d(MakeDict, dict8ns='ordered_dict__replace_then_move_to_end'):
class ps(MakeDict, dict8ns='sorted_items'):
class ps(MakeDict, dict8ns='ordered_items'):
class ps(MakeDict, dict8ns='ordered_items__replace_then_move_to_end'):


######################
>>> from seed.types.MakeDict import MakeDict, MakeOrderedDict, MakeOrderedDict__replace_then_move_to_end, ListSortedItems, ListOrderedItems, ListOrderedItems__replace_then_move_to_end
>>> class d(MakeDict):
...     a = 1
>>> d
{'a': 1}
>>> class d(MakeOrderedDict):
...     a = 1
...     b = 2
...     c = 3
...     a = 4
...     del b; b = 5
>>> d
OrderedDict([('a', 4), ('c', 3), ('b', 5)])
>>> class d(MakeOrderedDict__replace_then_move_to_end):
...     a = 1
...     b = 2
...     c = 3
...     a = 4
...     del b; b = 5
>>> d
OrderedDict__replace_then_move_to_end([('c', 3), ('a', 4), ('b', 5)])
>>> class ps(ListSortedItems):
...     a = 1
...     b = 2
...     c = 3
...     a = 4
...     del b; b = 5
>>> ps
[('a', 4), ('b', 5), ('c', 3)]
>>> class ps(ListOrderedItems):
...     a = 1
...     b = 2
...     c = 3
...     a = 4
...     del b; b = 5
>>> ps
[('a', 4), ('c', 3), ('b', 5)]
>>> class ps(ListOrderedItems__replace_then_move_to_end):
...     a = 1
...     b = 2
...     c = 3
...     a = 4
...     del b; b = 5
>>> ps
[('c', 3), ('a', 4), ('b', 5)]



######################
>>> from seed.types.MakeDict import show_registerrd_names4dict_mkr_ex, register_dict_mkr_ex, lookup_dict_mkr_ex
>>> sorted(show_registerrd_names4dict_mkr_ex())
['ordered_dict', 'ordered_dict__replace_then_move_to_end', 'ordered_items', 'ordered_items__replace_then_move_to_end', 'py_dict', 'sorted_items']

######################
>>> from seed.types.MakeDict import MakeDict, OrderedDict, OrderedDict__replace_then_move_to_end
>>> class d(MakeDict, dict8ns=OrderedDict()):
...     a = 1
...     b = 2
...     c = 3
...     a = 4
...     del b; b = 5
>>> d
OrderedDict([('a', 4), ('c', 3), ('b', 5)])
>>> class d(MakeDict, dict8ns=OrderedDict__replace_then_move_to_end()):
...     a = 1
...     b = 2
...     c = 3
...     a = 4
...     del b; b = 5
>>> d
OrderedDict__replace_then_move_to_end([('c', 3), ('a', 4), ('b', 5)])
>>> class d(MakeDict, dict8ns='ordered_dict'):
...     a = 1
...     b = 2
...     c = 3
...     a = 4
...     del b; b = 5
>>> d
OrderedDict([('a', 4), ('c', 3), ('b', 5)])
>>> class d(MakeDict, dict8ns='ordered_dict__replace_then_move_to_end'):
...     a = 1
...     b = 2
...     c = 3
...     a = 4
...     del b; b = 5
>>> d
OrderedDict__replace_then_move_to_end([('c', 3), ('a', 4), ('b', 5)])
>>> class ps(MakeDict, dict8ns='ordered_items'):
...     a = 1
...     b = 2
...     c = 3
...     a = 4
...     del b; b = 5
>>> ps
[('a', 4), ('c', 3), ('b', 5)]
>>> class ps(MakeDict, dict8ns='ordered_items__replace_then_move_to_end'):
...     a = 1
...     b = 2
...     c = 3
...     a = 4
...     del b; b = 5
>>> ps
[('c', 3), ('a', 4), ('b', 5)]

>>> class d(MakeDict, dict8ns='py_dict'):
...     a = 1
>>> d
{'a': 1}
>>> class ps(MakeDict, dict8ns='sorted_items'):
...     a = 1
...     b = 2
...     c = 3
...     a = 4
...     del b; b = 5
>>> ps
[('a', 4), ('b', 5), ('c', 3)]

]]


py -m nn_ns.app.debug_cmd   seed.types.MakeDict
py -m nn_ns.app.adhoc_argparser__main__call8module   seed.types.MakeDict   @f
py -m nn_ns.app.doctest_cmd seed.types.MakeDict:__doc__ -v
py -m nn_ns.app.doctest_cmd seed.types.MakeDict:_D
py -m nn_ns.app.doctest_cmd seed.types.MakeDict:MakeDict_Meta

from seed.types.MakeDict import MakeDict, OrderedDict, OrderedDict__replace_then_move_to_end
from seed.types.MakeDict import show_registerrd_names4dict_mkr_ex, register_dict_mkr_ex, lookup_dict_mkr_ex
from seed.types.MakeDict import MakeDict, MakeOrderedDict, MakeOrderedDict__replace_then_move_to_end, ListSortedItems, ListOrderedItems, ListOrderedItems__replace_then_move_to_end











#离散关联囗要求第一囗赋值非预置属性囗简洁
>>> class d(MakeDict):
...     a = 1
...     b = 1
...     a = 2

#离散关联囗要求第二囗读取预置属性囗简洁
>>> class d(MakeDict):
...     a = __module__
...     b = __qualname__



#离散关联囗要求第三囗禁止赋值分隔符囗于读取分隔符之前
>>> class d(MakeDict):
...     __ = 1 #反常模式:指示符/分隔符，未曾被读取前，则不得被赋值
Traceback (most recent call last):
    ...
KeyError: "should read sep_key first before write it!: '__'"

#离散关联囗要求第三囗赋值预置属性囗于读取分隔符之后
>>> class d(MakeDict):
...     __ #反常模式:指示符/分隔符，未被赋值前，却已可被读取
...     __module__ = ... #再次赋值
...     __module__ = ... #第三次赋值

#离散关联囗要求第三囗于读取分隔符之后囗正常对待分隔符囗囗禁止再次读取分隔符囗于赋值分隔符之前
>>> class d(MakeDict):
...     __ #反常模式:指示符/分隔符，未被赋值前，却已可被读取
...     __ #正常化:未被赋值，禁止读取分隔符
Traceback (most recent call last):
    ...
NameError: name '__' is not defined

#离散关联囗要求第三囗于读取分隔符之后囗正常对待分隔符囗囗赋值分隔符
>>> class d(MakeDict):
...     __ #反常模式:指示符/分隔符，未被赋值前，却已可被读取
...     __ = ... #正常化:赋值分隔符
...     __ = ... #正常化:再次赋值分隔符

#离散关联囗要求第三囗于读取分隔符之后囗正常对待分隔符囗囗再次读取分隔符囗于赋值分隔符之后
>>> class d(MakeDict):
...     __ #反常模式:指示符/分隔符，未被赋值前，却已可被读取
...     __ = ... #正常化:赋值分隔符
...     __ #正常化:读取分隔符





#离散关联囗要求第一囗禁止赋值预置属性囗于用户代码区囗于读取分隔符之前囗囗已赋值某非预置属性
#   注意:[正常化==>>已进入用户代码区][not [已进入用户代码区==>>正常化]]
#MakeDict_Meta:def __prepare__(metacls, name, bases, /, *, dict8ns=None, _is_in_phase4using_MakeDict=True, **kwargs):
>>> _d = MakeDict_Meta.__prepare__('d', ())
>>> len(_d)
0
>>> _d['a'] = 1
>>> _d['__module__'] = ...
Traceback (most recent call last):
    ...
KeyError: "set once-key after non-once-key: '__module__'"


#离散关联囗要求第一囗禁止赋值预置属性囗于用户代码区囗于读取分隔符之前囗囗第二次赋值预置属性
>>> class d(MakeDict):
...     __module__ = ...
Traceback (most recent call last):
    ...
KeyError: "set more than once: '__module__'"




#>>> dir(OrderedDict([])) #.move_to_end



#dict__vs__OrderedDict:
>>> class d(MakeDict):
...     a = 1
>>> d
{'a': 1}
>>> type(d) is dict
True
>>> class d(MakeDict, dict8ns=OrderedDict()):
...     a = 1
>>> d
OrderedDict([('a', 1)])
>>> type(d) is OrderedDict
True

#OrderedDict多次赋值情况下的次序，是『首次赋值次序』，而非『最后赋值次序』
#OrderedDict____vs____OrderedDict__replace_then_move_to_end:
>>> class d(MakeDict, dict8ns=OrderedDict()):
...     a = 1
...     b = 2
...     a = 3
>>> d
OrderedDict([('a', 3), ('b', 2)])
>>> class d(MakeDict, dict8ns=OrderedDict__replace_then_move_to_end()):
...     a = 1
...     b = 2
...     a = 3
>>> d
OrderedDict__replace_then_move_to_end([('b', 2), ('a', 3)])
>>> d.setdefault('b', 4)
2
>>> d
OrderedDict__replace_then_move_to_end([('b', 2), ('a', 3)])
>>> d.setdefault('c', 5)
5
>>> d
OrderedDict__replace_then_move_to_end([('b', 2), ('a', 3), ('c', 5)])


#重命名:__a -> _d__a
>>> class d(MakeDict):
...     __a = 1
>>> d
{'_d__a': 1}
>>> class d(MakeDict, dict8ns=OrderedDict()):
...     __ # 避免『禁止赋值分隔符』
...     _ = 1
...     __ = 2 #赋值分隔符
...     ___ = 3
...     ____ = 4
>>> d
OrderedDict([('_', 1), ('__', 2), ('___', 3), ('____', 4)])

# x=regex'\w'
# a=regex'\w' except '_'
#重命名:__xxxa -> _d__xxxa
#重命名:__xxxa_ -> _d__xxxa_
#不重命名:axxx, _axxx, __xxx__
#多次赋值情况下的次序，是『首次赋值次序』，而非『最后赋值次序』
>>> class d(MakeDict, dict8ns=OrderedDict()):
...     a = 1 #被5替代，是『首次赋值次序』，而非『最后赋值次序』
...     _a = 2
...     __a = 3 #
...     ___a = 4 #被17替代，是『首次赋值次序』，而非『最后赋值次序』
...     a = 5
...     a_ = 6
...     a__ = 7
...     a___ = 8
...     _a_ = 9
...     __a__ = 10
...     ___a___ = 11
...     __a___ = 12
...     _a___ = 13
...     a___ = 14
...     ___a__ = 15
...     ___a_ = 16 #
...     ___a = 17 #
>>> d
OrderedDict([('a', 5), ('_a', 2), ('_d__a', 3), ('_d___a', 17), ('a_', 6), ('a__', 7), ('a___', 14), ('_a_', 9), ('__a__', 10), ('___a___', 11), ('__a___', 12), ('_a___', 13), ('___a__', 15), ('_d___a_', 16)])






##old tests:
>>> class d(MakeDict):
...     __ # for arbitrary keys:
...     a = 1
...     b = 1
>>> d == {'a': 1, 'b':1}
True

>>> class d(MakeDict):
...     __ # for arbitrary keys:
...     a = 1
...     a = 2
>>> d
{'a': 2}

>>> class d(MakeDict):
...     a = 1
...     a = 2
>>> d
{'a': 2}

>>> class d(MakeDict):
...     a = 1
...     a = 2
...     __ # for arbitrary keys:
>>> d
{'a': 2}



#debug only:
>>> _set_at_most_once_keys_MakeDict ##@py3_10_5
('__module__', '__qualname__')


]]]'''#'''
__all__ = '''
    MakeDict
        OrderedDict
        OrderedDict__replace_then_move_to_end

    show_registerrd_names4dict_mkr_ex
        lookup_dict_mkr_ex
        register_dict_mkr_ex
            list_items_
            sorted_items_


    MakeDict_Meta
        MakeDict
        MakeOrderedDict
        MakeOrderedDict__replace_then_move_to_end
        ListSortedItems
        ListOrderedItems
        ListOrderedItems__replace_then_move_to_end
    '''.split()#'''



from seed.tiny import check_type_is, check_callable, check_pair
from seed.tiny import echo
from collections import UserDict #, defaultdict


py_dict = dict
__all__
######################
######################
##export:'OrderedDict'
from collections import OrderedDict
class OrderedDict__replace_then_move_to_end(OrderedDict):
    'replace_then_move_to_end:『最后赋值次序』，而非『首次赋值次序』'
    def __setitem__(sf, k, v, /):
        super().__setitem__(k,v)
        sf.move_to_end(k)

class _D(UserDict, dict):# <<== __prepare__() is reqired to return obj of subclass of py.dict
    #[[[
    r'''used in MakeDict_Meta

[[
class _D(UserDict, dict):# <<== __prepare__() is reqired to return obj of subclass of py.dict
    def __init__(self, data, set_at_most_once_keys, sep_key='__', /):
        ... ...
    def moveout_dict_without_set_at_most_once_keys_before_first_read_sep_key(self, /):
        ... ...
        return data

class MakeDict_Meta(type):
    def __new__(metacls, name, bases, namespace, /, *, dict8ns=None, **kwargs):
        ... ...
        d = namespace.moveout_dict_without_set_at_most_once_keys_before_first_read_sep_key()
        return postprocessor(d)
    @classmethod
    def __prepare__(metacls, name, bases, /, *, dict8ns=None, _is_in_phase4using_MakeDict=True, **kwargs):
        ... ...
        return _D(dict8ns, _set_at_most_once_keys_MakeDict)
if 1:
    ... ...
    class d(MakeDict):pass
    _set_at_most_once_keys_MakeDict = tuple(sorted(d.keys()))
]]==>>也就是说：MakeDict_Meta/MakeDict 使用 _D 时，固定配置为:_D(locals.data, globals._set_at_most_once_keys_MakeDict, '__')
[[sep/sep_key用意义何在？
以前未做详细注释，现在考古...

三种操作:
    读:__getitem__
    写:__setitem__
    终结时破坏性提取:moveout_dict_without_set_at_most_once_keys_before_first_read_sep_key

三种键值:
    sep_key
    non_set_at_most_once_keys
        相对于 set_at_most_once_keys
    set_at_most_once_keys
        见globals._set_at_most_once_keys_MakeDict
        其定义为，python自动给cls.__dict__提前添加的属性(不可能追加属性，因为用户会覆盖删除某些预置属性)
            例如:__qualname__, __module__ #@py3_10_5
        因为 这里使用『class』语句块用于构建『名值映射表』，所以 这些预置属性显然是不需要的
        这些预置属性理应删除，可惜无法提前清空，只能于『终结时破坏性提取』进行删除，但有条件，即用户未曾给这些预置属性赋值
        ???这里似是假设了或者检测py内建只给这些预置属性赋值最多一次。但从逻辑上讲，当然可以多次

三种键值-中文名:
    分隔符:sep_key
    非类型预置的属性名集:non_set_at_most_once_keys
    类型预置的属性名集:set_at_most_once_keys

分情况:
    要求第一，若用户构建『名值映射表』实例时并未涉及『类型预置的属性名集』，则不应当要求多余设置，尽量简洁
        class d(MakeDict):
            a = 1
            b = 1
            a = 2
        d == dict(b=1,a=2)
        #离散关联囗要求第一囗赋值非预置属性囗简洁
    要求第二，若用户构建『名值映射表』实例时使用/读取『类型预置的属性名集』，则不应当有多余设置，尽量简洁
        class d(MakeDict):
            a = __module__
            b = __qualname__
        #离散关联囗要求第二囗读取预置属性囗简洁
    要求第三，若用户构建『名值映射表』实例时使用/赋值给『类型预置的属性名集』，则应当有显式指示符，最好是反常模式的语句
        class d(MakeDict):
        __ #反常模式:指示符/分隔符，未被赋值前，却已可被读取
            __module__ = ... #再次赋值
            __module__ = ... #第三次赋值
        #离散关联囗要求第三囗赋值预置属性囗于读取分隔符之后

[要求第一] ==>>:
    py预置后，这些预置属性值不得再被赋值(分隔符之前)，防止用户误用
        ==>> 若有『非类型预置的属性名集』被赋值，则 说明已进入『用户代码区』，禁止这些预置属性值再被赋值(分隔符之前)
        #离散关联囗要求第一囗禁止赋值预置属性囗于用户代码区囗于读取分隔符之前囗囗已赋值某非预置属性
        #   注意:[正常化==>>已进入用户代码区][not [已进入用户代码区==>>正常化]]
        但 在任何『非类型预置的属性名集』被赋值前，究竟何时进入『用户代码区』，这里假设『类型预置的属性名集最多只被预置一次』，据此假设，第二次赋值就是用户误用(分隔符之前)
        #离散关联囗要求第一囗禁止赋值预置属性囗于用户代码区囗于读取分隔符之前囗囗第二次赋值预置属性
[要求第三] ==>>:
    因为使用『指示符/分隔符，未被赋值前，却已可被读取』这种反常模式，所以『指示符/分隔符，未曾被读取前，则不得被赋值』
        #离散关联囗要求第三囗禁止赋值分隔符囗于读取分隔符之前
    分隔符被首次读取后，被当作普通属性，正常对待
        #离散关联囗要求第三囗于读取分隔符之后囗正常对待分隔符囗囗禁止再次读取分隔符囗于赋值分隔符之前
        #离散关联囗要求第三囗于读取分隔符之后囗正常对待分隔符囗囗赋值分隔符
        #离散关联囗要求第三囗于读取分隔符之后囗正常对待分隔符囗囗再次读取分隔符囗于赋值分隔符之后


]]


扩展:除了OrderedDict，还可有
    * HistoryGrowOnlyDict(类似HistoryGrowOnlyStack)，保存整个赋值历史(删除？要么不许删除，要么后处理不考虑该属性删除动作之前的赋值历史)，这样一来就相当于ordered_multi_dict，不是{k:v}而是[(k,v)]，『名』不再有『唯一性』。
        view ../../python3_src/seed/types/HistoryGrowOnlyStack.py
    * OrderedDict, 多次赋值情况下的次序，是『首次赋值次序』，而非『最后赋值次序』，所以可改用『最后赋值次序』
    * OrderedDict__replace_then_move_to_end(pop_before_replace/replace_then_move_to_end)(OrderedDict.move_to_end), 不同OrderedDict之处，在于改用『最后赋值次序』
    * py_dict
        若只是使用py.dict，那还不如：
            def _():
                ...
                return {**locals()}
            d = _()

>>> sep = '____'
>>> THIS = lambda ks: _D({}, ks, sep)

>>> set_at_most_once_keys = o1, o2 = '12'
>>> k1, k2 = 'ab'
>>> d = THIS(set_at_most_once_keys)
>>> d[o1] = 1
>>> d[o1] = 2 #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
KeyError

>>> d = THIS(set_at_most_once_keys)
>>> d[o1] = 1
>>> d[o2] = 1
>>> d[o1] = 2 #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
KeyError
>>> d = THIS(set_at_most_once_keys)
>>> d[k1] = 1
>>> d[o1] = 1 #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
KeyError
>>> d = THIS(set_at_most_once_keys)
>>> d[sep] = 1 #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
KeyError
>>> d = THIS(set_at_most_once_keys)
>>> d[k1] = 1
>>> d[k1] = 2
>>> d = THIS(set_at_most_once_keys)
>>> d[sep]
>>> d[o1] = 1
>>> d[o1] = 2
>>> d = THIS(set_at_most_once_keys)
>>> d[o1] = 1
>>> d[k1] = 1
>>> d[k2] = 1
>>> d[sep]
>>> d[o1] = 2
>>> d[o1] = 3
>>> d[o2] = 1
>>> d[k2] = 2
>>> d.moveout_dict_without_set_at_most_once_keys_before_first_read_sep_key() == {o1:3, o2:1, k1:1, k2:2}
True

'''#'''#]]]
    #def __new__(cls, data, set_at_most_once_keys, sep_key='__'):
    #   # fail!!!!
    #   return object.__new__(cls) # donot init type<'dict'>
    def __init__(self, data, set_at_most_once_keys, sep_key='__', /):
        set_at_most_once_keys = set(set_at_most_once_keys)
        if sep_key in set_at_most_once_keys:
            raise ValueError(f'sep_key in set_at_most_once_keys: {sep_key}')
        #super().__init__() donot init type<'dict'>
        super().__init__()
        self.data = data
        self.sep_key = sep_key
        self.set_at_most_once_keys = set_at_most_once_keys
        self.sep_key_occured = False
        self.non_set_at_most_once_keys_written = False
        self.set_at_most_once_key2count = {k:0 for k in set_at_most_once_keys}
            #defaultdict(int)
            #bug: after sep_key first read: all += 1
            #bug: after sep_key first read: all := 1
        if 999:#new
            self.once_keys4stand = {*[]}
    def __getitem__(self, key, /):
        if not self.sep_key_occured and key == self.sep_key:
            # first read sep_key
            self.sep_key_occured = True
            if not all(v < 2 for v in self.set_at_most_once_key2count.values()): raise logic-err
            self.set_at_most_once_key2count = {k:1 for k in self.set_at_most_once_keys}
                #不是/xxx: frozen? no set any more??
                #正常化:sep_key_occured之后，正常对待所有属性
                #see:moveout_dict_without_set_at_most_once_keys_before_first_read_sep_key
            return None
        return self.data[key]
    def __setitem__(self, key, obj, /):
        if not self.sep_key_occured:
            # before first read sep_key
            #于读取分隔符之前

            if key in self.set_at_most_once_keys:
                #预置属性赋值，只有首次允许
                if key in self:
                    #禁止再次赋值预置属性
                    #离散关联囗要求第一囗禁止赋值预置属性囗于用户代码区囗于读取分隔符之前囗囗第二次赋值预置属性
                    raise KeyError(f'set more than once: {key!r}')
                elif self.non_set_at_most_once_keys_written:
                    #于用户代码区，禁止赋值预置属性
                    #   注意:[正常化==>>已进入用户代码区][not [已进入用户代码区==>>正常化]]
                    #离散关联囗要求第一囗禁止赋值预置属性囗于用户代码区囗于读取分隔符之前囗囗已赋值某非预置属性
                    raise KeyError(f'set once-key after non-once-key: {key!r}')
                else:
                    #py预置，至多一次
                    pass
            elif key == self.sep_key:
                # write sep_key before first read sep_key
                #于读取分隔符之前，禁止赋值分隔符
                #离散关联囗要求第三囗禁止赋值分隔符囗于读取分隔符之前
                raise KeyError(f'should read sep_key first before write it!: {key!r}')
            else:
                # write non_set_at_most_once_keys
                #非预置属性赋值，必然允许
                self.non_set_at_most_once_keys_written = True
        else:
            #于读取分隔符之后，正常化
            pass
        if key in self.set_at_most_once_keys:
            self.set_at_most_once_key2count[key] += 1
        else:
            pass
        if 999:#new
            if self.sep_key_occured and key in self.set_at_most_once_keys:
                self.once_keys4stand.add(key)
            else:
                pass
        else:
            pass
        self.data[key] = obj
    def moveout_dict_without_set_at_most_once_keys_before_first_read_sep_key(self, /):
        if not all(v > 0 for v in self.set_at_most_once_key2count.values()): raise logic-err # must set at least once or sep_key_occured!!! #see:__getitem__(k) 正常化 on [k==sep_key][not sep_key_occured]


        if 999:#new
            keys_to_del = [k for k, v in self.set_at_most_once_key2count.items() if k not in self.once_keys4stand]
        else:#old
            keys_to_del = [k for k, v in self.set_at_most_once_key2count.items() if v < 2]

        data, self.data = self.data, None # donot use me from now on
        for k in keys_to_del:
            del data[k]
        return data

        return {k:v for k, v in self.items()
                if k not in self.set_at_most_once_key2count
                    or self.set_at_most_once_key2count[k] > 1
                }
#end-class _D(UserDict, dict):# <<== __prepare__() is reqired to return obj of subclass of py.dict

def check_dict_mkr_ex(dict_mkr_ex, /):
    check_pair(dict_mkr_ex)
    (dict_mkr,may_postprocessor) = dict_mkr_ex
    check_callable(dict_mkr)
    if not may_postprocessor is None:
        postprocessor = may_postprocessor
        check_callable(postprocessor)
_nm2dict_mkr_ex = {}
def show_registerrd_names4dict_mkr_ex():
    return _nm2dict_mkr_ex.keys()
def register_dict_mkr_ex(nm4dict_mkr_ex, dict_mkr, may_postprocessor, /):
    r''':: nm4dict_mkr_ex/str -> dict_mkr -> may postprocessor -> None

    dict_mkr_ex = (dict_mkr,may postprocessor)
    dict_mkr :: () -> mapping
    postprocessor :: mapping -> obj

    #'''
    check_type_is(str, nm4dict_mkr_ex)
    dict_mkr_ex =(dict_mkr, may_postprocessor)
    check_dict_mkr_ex(dict_mkr_ex)
    if nm4dict_mkr_ex in _nm2dict_mkr_ex:raise LookupError(nm4dict_mkr_ex)#existed
    _nm2dict_mkr_ex[nm4dict_mkr_ex] = dict_mkr_ex
def lookup_dict_mkr_ex(nm4dict_mkr_ex, /):
    'nm4dict_mkr_ex -> dict_mkr_ex/(dict_mkr,may_postprocessor)'
    check_type_is(str, nm4dict_mkr_ex)
    dict_mkr_ex = (dict_mkr,may_postprocessor) = _nm2dict_mkr_ex[nm4dict_mkr_ex]
    return dict_mkr_ex

def sorted_items_(mapping, /):
    'postprocessor for register_dict_mkr_ex/lookup_dict_mkr_ex'
    return sorted(mapping.items())
def list_items_(mapping, /):
    'postprocessor for register_dict_mkr_ex/lookup_dict_mkr_ex'
    return [*mapping.items()]
register_dict_mkr_ex('py_dict', dict, None)
register_dict_mkr_ex('sorted_items', dict, sorted_items_)

register_dict_mkr_ex('ordered_dict', OrderedDict, None)
register_dict_mkr_ex('ordered_items', OrderedDict, list_items_)
register_dict_mkr_ex('ordered_dict__replace_then_move_to_end', OrderedDict__replace_then_move_to_end, None)
register_dict_mkr_ex('ordered_items__replace_then_move_to_end', OrderedDict__replace_then_move_to_end, list_items_)



def _is_first_def_MakeDict(name, /):
    try:
        MakeDict
    except NameError:
        if name == 'MakeDict':
            return True
    return False
class MakeDict_Meta(type):
    #[[[
    r'''

the_kwarg_named_dict8ns for kwarg "dict8ns=":
    the_kwarg_named_dict8ns :: ( None | nm4dict_mkr_ex/str | py_dict_obj/(?<:py.dict) | dict_mkr/Callable | xdict_mkr_ex/((py_dict_obj|dict_mkr),may postprocessor) )
        None => .default4the_kwarg_named_dict8ns...
        nm4dict_mkr_ex => lookup_dict_mkr_ex(nm4dict_mkr_ex)...

???postprocessor may be used like:
    @postprocessor
    class ...


>>> class d(metaclass=MakeDict_Meta):
...     __module__
...     __qualname__
...     a = 1
...     __
...     __module__ = 2
>>> d == {'a': 1, '__module__':2}
True
>>> class d(MakeDict): #doctest: +IGNORE_EXCEPTION_DETAIL
...     __module__ = 2
Traceback (most recent call last):
    ...
KeyError
>>> class d(MakeDict): #doctest: +IGNORE_EXCEPTION_DETAIL
...     __qualname__
...     a = 1
...     __
...     __module__ = 2
>>> d == {'a': 1, '__module__':2}
True
>>> class d(MakeDict):
...     a = 1
...     b = 1
>>> d == {'a': 1, 'b':1}
True
>>> type(d) is dict
True
>>> class d(MakeDict, dict8ns=OrderedDict()):
...     a = 1
...     b = 1
>>> d == {'a': 1, 'b':1}
True
>>> type(d) is OrderedDict
True
'''#'''#]]]
    _is_in_phase4using_MakeDict = False
    def __new__(metacls, name, bases, namespace, /, *, dict8ns=None, _is_in_phase4using_MakeDict=True, **kwargs):
        '-> ((mapping|[(nm,v)]) if _is_in_phase4using_MakeDict else a_klass_obj/MakeDict_Meta) #see:the_kwarg_named_dict8ns for kwarg "dict8ns="'
        if 0x777:#new2
            if not _is_in_phase4using_MakeDict:
                return super().__new__(metacls, name, bases, namespace, **kwargs)
        elif 777:#new
            if not metacls._is_in_phase4using_MakeDict:
                return super().__new__(metacls, name, bases, namespace, **kwargs)
        else:#old
            if _is_first_def_MakeDict(name):
                return super().__new__(metacls, name, bases, namespace, **kwargs)

        dict_mkr_ex = (dict_mkr,may_postprocessor) = metacls._dict_mkr_ex5the_kwarg_named_dict8ns(bases, dict8ns=dict8ns, _is_in_phase4using_MakeDict=_is_in_phase4using_MakeDict)

        del dict8ns, dict_mkr, dict_mkr_ex
        may_postprocessor
        if not may_postprocessor is None:
            postprocessor = may_postprocessor
        else:
            postprocessor = echo
        postprocessor
        del may_postprocessor

        d = namespace.moveout_dict_without_set_at_most_once_keys_before_first_read_sep_key()
        return postprocessor(d)
    #def __init__(self, name, bases, namespace, **kwargs):

    @classmethod
    def _dict_mkr_ex5the_kwarg_named_dict8ns(metacls, bases, /, *, dict8ns, _is_in_phase4using_MakeDict):
        '-> dict_mkr_ex #see:the_kwarg_named_dict8ns for kwarg "dict8ns="'
        assert _is_in_phase4using_MakeDict
        if dict8ns is None:
            if 777:#new
                assert len(bases) < 2, '??do you means to set "_is_in_phase4using_MakeDict=False"??'
                [basecls] = bases if bases else [MakeDict]
                dict8ns = basecls.default4the_kwarg_named_dict8ns
                if 0b00:print(basecls, dict8ns)
            else:#old
                dict8ns = {}
        assert dict8ns is not None
        ###
        if type(dict8ns) is str:
            nm4dict_mkr_ex = dict8ns
            del dict8ns
            # register_dict_mkr_ex+lookup_dict_mkr_ex
            dict_mkr_ex = (dict_mkr,may_postprocessor) = lookup_dict_mkr_ex(nm4dict_mkr_ex)
        elif type(dict8ns) is tuple:
            xdict_mkr_ex = dict8ns
            del dict8ns
            check_pair(xdict_mkr_ex)
            (xdict_mkr,may_postprocessor) = xdict_mkr_ex
            if isinstance(xdict_mkr, py_dict): #must be py.dict, not collections.abc.Mapping
                d = xdict_mkr
                lazy_d = lambda:d
                dict_mkr = lazy_d
            else:
                dict_mkr = xdict_mkr
                check_callable(dict_mkr)
            dict_mkr_ex = (dict_mkr,may_postprocessor)
            check_dict_mkr_ex(dict_mkr_ex)
        elif isinstance(dict8ns, py_dict): #must be py.dict, not collections.abc.Mapping
            d = dict8ns
            del dict8ns
            lazy_d = lambda:d
            dict_mkr = lazy_d
            may_postprocessor = None
            dict_mkr_ex = (dict_mkr,may_postprocessor)
        elif callable(dict8ns):
            dict_mkr = dict8ns
            del dict8ns
            may_postprocessor = None
            dict_mkr_ex = (dict_mkr,may_postprocessor)
        else:
            raise TypeError(type(dict8ns))
        check_dict_mkr_ex(dict_mkr_ex)
        return dict_mkr_ex
    #end-def _dict_mkr_ex5the_kwarg_named_dict8ns(metacls, bases, /, *, dict8ns, _is_in_phase4using_MakeDict):
    @classmethod
    def __prepare__(metacls, name, bases, /, *, dict8ns=None, _is_in_phase4using_MakeDict=True, **kwargs):
        '-> namespace/(subclass<py_dict>) #see:the_kwarg_named_dict8ns for kwarg "dict8ns="'
        # fail!!!! must return subclass of py.dict #fixed by:class _D(..., dict)!!!!
        ######################
        assert not _is_in_phase4using_MakeDict or len(bases) < 2
        ######################
        if 0x777:#new2
            if not _is_in_phase4using_MakeDict:
                return super().__prepare__(name, bases, **kwargs)
        elif 777:#new
            if not metacls._is_in_phase4using_MakeDict:
                return super(__class__,metacls).__prepare__(name, bases, **kwargs)
        else:#old
            pass
        dict_mkr_ex = (dict_mkr,may_postprocessor) = metacls._dict_mkr_ex5the_kwarg_named_dict8ns(bases, dict8ns=dict8ns, _is_in_phase4using_MakeDict=_is_in_phase4using_MakeDict)
        dict8ns = dict_mkr()

        return _D(dict8ns, _set_at_most_once_keys_MakeDict)
if 1:
    # initial _set_at_most_once_keys_MakeDict
    _set_at_most_once_keys_MakeDict = ()
        # this dumb setting is required to mk the class 'MakeDict'
        # this dumb setting is required to find out all the names set by py.class-api/protocol
    class MakeDict(metaclass=MakeDict_Meta, _is_in_phase4using_MakeDict=False):
        default4the_kwarg_named_dict8ns = 'py_dict'
    class __d(MakeDict):pass
        #call __prepare__() ==>> using _set_at_most_once_keys_MakeDict
    _set_at_most_once_keys_MakeDict = tuple(sorted(__d.keys()))
    del __d
#end-class MakeDict_Meta(type):
if 1:
    ######################
    class MakeOrderedDict(metaclass=MakeDict_Meta, _is_in_phase4using_MakeDict=False):
        default4the_kwarg_named_dict8ns = 'ordered_dict'
    class MakeOrderedDict__replace_then_move_to_end(metaclass=MakeDict_Meta, _is_in_phase4using_MakeDict=False):
        default4the_kwarg_named_dict8ns = 'ordered_dict__replace_then_move_to_end'
    ######################
    class ListSortedItems(metaclass=MakeDict_Meta, _is_in_phase4using_MakeDict=False):
        default4the_kwarg_named_dict8ns = 'sorted_items'
    class ListOrderedItems(metaclass=MakeDict_Meta, _is_in_phase4using_MakeDict=False):
        default4the_kwarg_named_dict8ns = 'ordered_items'
    class ListOrderedItems__replace_then_move_to_end(metaclass=MakeDict_Meta, _is_in_phase4using_MakeDict=False):
        default4the_kwarg_named_dict8ns = 'ordered_items__replace_then_move_to_end'
    ######################
    ######################
    MakeDict_Meta._is_in_phase4using_MakeDict = True
    ######################
    ######################


r'''
class MakeDict_Type:
    def __call__(*args, **kwargs):
        print(args)
        print(kwargs)
MakeDict_Meta = MakeDict_Type()
class MakeDict(metaclass=MakeDict_Meta): pass
'''#'''

def _t0():
    class k(metaclass=MakeDict_Meta):
        __module__
        __qualname__
        pass
    class d(MakeDict):
        a = 1
    class x(MakeDict, dict8ns=OrderedDict()):
        a = 1
    #print(k)
    #print(d)
    assert k == {}
    assert d == {'a':1}
    assert x == {'a':1}
    assert type(d) is dict
    assert type(x) is OrderedDict
_t0()


from seed.types.MakeDict import MakeDict, OrderedDict, OrderedDict__replace_then_move_to_end
from seed.types.MakeDict import show_registerrd_names4dict_mkr_ex, register_dict_mkr_ex, lookup_dict_mkr_ex
from seed.types.MakeDict import MakeDict, MakeOrderedDict, MakeOrderedDict__replace_then_move_to_end, ListSortedItems, ListOrderedItems, ListOrderedItems__replace_then_move_to_end
if 1:
    from seed.types.MakeDict import _nm2dict_mkr_ex

if __name__ == "__main__":
    #_t0()
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


