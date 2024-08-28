#__all__:goto
r'''[[[[[
dict/set are unordered
let us sorted it

see:
    ast.literal_eval
    seed.helper.safe_eval
        # for "set()"

e ../../python3_src/seed/helper/stable_repr.py
    view ../../python3_src/seed/helper/repr_input.py
    view ../../python3_src/seed/types/NamedTupleBase.py
    view ../../python3_src/seed/helper/stable_repr.py

[[
w_
wobject - wrapped obj; match with iter_repr_element()
    iter_repr_element :: wobject -> iter_eol_indents -> Iter str
        eg. if [transform obj into wobject/SortableIterReprable4builtins]: then [iter_repr_element := method_caller('stable_iter_repr_data', has_head_eol_when_indent=has_head_eol_when_indent)]
]]
[[
iter_eol_indents/IterEOLIndentsABC
    --> eof, indents, eof, indents, ...
has_head_eol_when_indent/bool
    if has_head_eol_when_indent:
        [
            xxx
            ,yyy
        ]
    else:
        [xxx
            ,yyy
        ]
]]
[[
TODO:
    ': ' --> (':', any_spaces)

TODO:
    (iter_repr_element :: wobject -> iter_eol_indents -> Iter str)
        --> (iter_repr_element :: wobject -> iter_eol_indents -> has_head_eol_when_indent -> Iter str)
            # <<== def stable_iter_repr_data(self, *, iter_eol_indents, has_head_eol_when_indent):
        or: using env/namedtuple
]]





py -m nn_ns.app.debug_cmd   seed.helper.stable_repr -x
py -m seed.helper.stable_repr
py -m nn_ns.app.doctest_cmd seed.helper.stable_repr:__doc__ -ff -v

from seed.helper.stable_repr import stable_repr, stable_repr_ex, stable_repr_print, stable_repr_print_ex
from seed.helper.stable_repr import stable_repr__expand_top_layer, stable_repr_print__expand_top_layer
from seed.helper.stable_repr import stable_repr__expand_all_layer, stable_repr_print__expand_all_layer
from seed.helper.stable_repr import stable_repr__expand_all_layer__noindent, stable_repr_print__expand_all_layer__noindent


SortableIterReprable4builtins.register_datatype_and_name_and_SortableIterReprable
    后来注册了个seed.tiny.HexReprInt

from seed.helper.stable_repr import IGetFuncNameArgsOrderedKwds4stable_repr, register4get__funcname__args__ordered_kwdxxxs, get4get__funcname__args__ordered_kwdxxxs
    [seed.types.NamedTupleBase <: seed.helper.stable_repr.IGetFuncNameArgsOrderedKwds4stable_repr]





#################################
#################################
#################################

>>> from seed.helper.stable_repr import stable_repr, stable_repr_ex, stable_repr_print, stable_repr_print_ex
>>> from seed.helper.stable_repr import stable_repr__expand_top_layer, stable_repr_print__expand_top_layer
>>> from seed.helper.stable_repr import stable_repr__expand_all_layer, stable_repr_print__expand_all_layer
>>> from seed.helper.stable_repr import stable_repr__expand_all_layer__noindent, stable_repr_print__expand_all_layer__noindent

>>> from seed.helper.stable_repr import IGetFuncNameArgsOrderedKwds4stable_repr, register4get__funcname__args__ordered_kwdxxxs, get4get__funcname__args__ordered_kwdxxxs



>>> stable_repr(None)
'None'
>>> stable_repr(...)
'Ellipsis'
>>> stable_repr(NotImplemented)
'NotImplemented'
>>> stable_repr(False)
'False'

>>> stable_repr(0)
'0'
>>> stable_repr(0.0)
'0.0'
>>> stable_repr(0j)
'0j'
>>> stable_repr(Fraction(3,4))
'Fraction(3, 4)'
>>> stable_repr(b'')
"b''"

>>> stable_repr(())
'()'
>>> stable_repr([])
'[]'
>>> stable_repr(set())
'set()'
>>> stable_repr(frozenset())
'frozenset()'
>>> stable_repr({})
'{}'
>>> stable_repr(OrderedDict())
'OrderedDict()'

>>> stable_repr((1,))
'(1,)'
>>> stable_repr([1])
'[1]'
>>> stable_repr({1})
'{1}'
>>> stable_repr(frozenset({1}))
'frozenset({1})'
>>> stable_repr({1:2})
'{1: 2}'
>>> stable_repr(OrderedDict([(1, 2)]))
'OrderedDict([(1, 2)])'

>>> stable_repr((1, 2))
'(1, 2)'
>>> stable_repr([1, 2])
'[1, 2]'
>>> stable_repr({1, 2})
'{1, 2}'
>>> stable_repr(frozenset({1, 2}))
'frozenset({1, 2})'
>>> stable_repr({1:2,3:4})
'{1: 2, 3: 4}'
>>> stable_repr(OrderedDict([(1, 2), (3, 4)]))
'OrderedDict([(1, 2), (3, 4)])'


#############stable_repr_ex
>>> iter_eol_indents = IterEOLIndents(indent='    ', depth=0, maybe_max_depth=None)
>>> _stable_repr_ex = lambda obj: stable_repr_ex(obj, iter_eol_indents=iter_eol_indents, has_head_eol_when_indent=True)
>>> _stable_repr_ex(Fraction(3,4))
'Fraction(3, 4)'
>>> _stable_repr_ex(b'')
"b''"

>>> _stable_repr_ex(())
'()'
>>> _stable_repr_ex([])
'[]'
>>> _stable_repr_ex(set())
'set()'
>>> _stable_repr_ex(frozenset())
'frozenset()'
>>> _stable_repr_ex({})
'{}'
>>> _stable_repr_ex(OrderedDict())
'OrderedDict()'


>>> print_stable_repr_ex = lambda obj: print(_stable_repr_ex(obj))
>>> print_stable_repr_ex((1,))
(
    1,
)
>>> print_stable_repr_ex([1])
[
    1
]
>>> print_stable_repr_ex({1})
{
    1
}
>>> print_stable_repr_ex(frozenset({1}))
frozenset({
    1
})
>>> print_stable_repr_ex({1:2})
{
    1
    : 2
}
>>> print_stable_repr_ex(OrderedDict([(1, 2)]))
OrderedDict([
    (
        1
        ,2
    )
])

>>> print_stable_repr_ex((1, 2))
(
    1
    ,2
)
>>> print_stable_repr_ex([1, 2])
[
    1
    ,2
]
>>> print_stable_repr_ex({1, 2})
{
    1
    ,2
}
>>> print_stable_repr_ex(frozenset({1, 2}))
frozenset({
    1
    ,2
})
>>> print_stable_repr_ex({1:2,3:4})
{
    1
    : 2
    ,3
    : 4
}
>>> print_stable_repr_ex(OrderedDict([(1, 2), (3, 4)]))
OrderedDict([
    (
        1
        ,2
    )
    ,(
        3
        ,4
    )
])


>>> print(stable_repr(OrderedDict([(1, 2), (3, 4)]), depth=0))
OrderedDict([
    (
        1
        ,2
    )
    ,(
        3
        ,4
    )
])
>>> print(stable_repr(OrderedDict([(1, 2), (3, 4)]), depth=1))
OrderedDict([
        (
            1
            ,2
        )
        ,(
            3
            ,4
        )
    ])

>>> import io
>>> fout = io.StringIO()
>>> stable_repr_print(fout, OrderedDict([(1, 2), (3, 4)]), depth=1)
>>> print(fout.getvalue())
OrderedDict([
        (
            1
            ,2
        )
        ,(
            3
            ,4
        )
    ])


### has_no_more_intents
>>> print(stable_repr(OrderedDict([(1, 2), (3, 4)]), depth=0, maybe_max_depth=0))
OrderedDict([(1, 2), (3, 4)])

>>> print(stable_repr(OrderedDict([(1, 2), (3, 4)]), depth=0, maybe_max_depth=1))
OrderedDict([
    (1, 2)
    ,(3, 4)
])

>>> print(stable_repr(OrderedDict([(1, 2), (3, [4,5])]), depth=0, maybe_max_depth=2))
OrderedDict([
    (
        1
        ,2
    )
    ,(
        3
        ,[4, 5]
    )
])

>>> print(stable_repr({1: 2, 3: [4,5]}, indent='', depth=0, maybe_max_depth=1))
{
1
: 2
,3
: [4, 5]
}

############ has_head_eol_when_indent
>>> print(stable_repr({1: 2, 3: [4,5]}, indent='', depth=0, maybe_max_depth=1, has_head_eol_when_indent=False))
{1
: 2
,3
: [4, 5]
}
>>> print(stable_repr__expand_top_layer({1: 2, 3: [4,5]}))
{1
: 2
,3
: [4, 5]
}
>>> import sys
>>> stable_repr_print__expand_top_layer(sys.stdout, {1: 2, 3: [4,5]})
{1
: 2
,3
: [4, 5]
}
>>> stable_repr__expand_top_layer({1: 2, 3: [4,5]})
'{1\n: 2\n,3\n: [4, 5]\n}'
>>> from seed.tiny_.pprint4container__depth1 import show5pprint
>>> show5pprint(0, stable_repr_print__expand_top_layer, {1: 2, 3: [4,5]}) #2 diffs cmp pprint4container__depth1: no tailing EOL, item_sep=': ' has space
'{1\n: 2\n,3\n: [4, 5]\n}'


############## sort....
>>> sorted_mapping = lambda d, key=None, reverse=False: sorted_mapping_by_SortableIterReprable(d, key=key, reverse=reverse, SortableIterReprable=None)
>>> sorted_mapping({2:1, 5:4})
[(2, 1), (5, 4)]
>>> sorted_mapping({2:1, 5:4}, reverse=True)
[(5, 4), (2, 1)]

>>> class W:
...     def __init__(self, obj): self.obj = obj
...     def get_obj(self): return self.obj
...     def __repr__(self): return f'{type(self).__name__}({self.obj!r})'
>>> class M(W):
...     def items(self): return iter(self.obj)
>>> d = M([(W(2), 1), (W(5), 4)])
>>> sorted_mapping(d, key=W.get_obj)
[(W(2), 1), (W(5), 4)]
>>> sorted_mapping(d, key=W.get_obj, reverse=True)
[(W(5), 4), (W(2), 1)]






>>> from seed.helper.stable_repr import IGetFuncNameArgsOrderedKwds4stable_repr, register4get__funcname__args__ordered_kwdxxxs, get4get__funcname__args__ordered_kwdxxxs

>>> class X(IGetFuncNameArgsOrderedKwds4stable_repr):
...     def ___get__funcname__args__ordered_kwdxxxs___(sf):
...         return (None, [0, 1, [2]], [('a', 111), ('b', 222), ('c', [333])])
>>> stable_repr(X())
'X(0, 1, [2], a= 111, b= 222, c= [333])'
>>> stable_repr_print__expand_top_layer(None, X())
X(0
,1
,[2]
,a
= 111
,b
= 222
,c
= [333]
)
>>> stable_repr_print(None, X(), depth=0)
X(
    0
    ,1
    ,[
        2
    ]
    ,a
    = 111
    ,b
    = 222
    ,c
    = [
        333
    ]
)

>>> dict(**{'def':1})
{'def': 1}
>>> dict(def=1)
Traceback (most recent call last):
    dict(def=1)
         ^^^
SyntaxError: invalid syntax


[[
from keyword import iskeyword
not is_valid_python_id(nm)
iskeyword(nm)
==>>:
,open4py_kw:str, close4py_kw:str, item_sep4py_kw:str
]]

>>> class XX(IGetFuncNameArgsOrderedKwds4stable_repr):
...     def ___get__funcname__args__ordered_kwdxxxs___(sf):
...         return (None, [0, 1, [2]], [('a', 111), ('def', [222, [444]]), ('c', [333])])

>>> stable_repr(XX())
"XX(0, 1, [2], a= 111, **{'def': [222, [444]]}, c= [333])"

>>> stable_repr_print__expand_top_layer(None, XX())
XX(0
,1
,[2]
,a
= 111
,**{'def': [222, [444]]}
,c
= [333]
)

>>> stable_repr_print(None, XX(), depth=0)
XX(
    0
    ,1
    ,[
        2
    ]
    ,a
    = 111
    ,**{
        'def'
        : [
            222
            ,[
                444
            ]
        ]
    }
    ,c
    = [
        333
    ]
)




>>> stable_repr_print__expand_all_layer(None, [(0, 1, [2, [3, {4:{5:{6}}}]]), []])
[
  (
    0
    ,1
    ,[
      2
      ,[
        3
        ,{
          4
          : {
            5
            : {
              6
            }
          }
        }
      ]
    ]
  )
  ,[]
]


>>> stable_repr_print__expand_all_layer__noindent(None, [(0, 1, [2, [3, {4:{5:{6}}}]]), []])
[
(
0
,1
,[
2
,[
3
,{
4
: {
5
: {
6
}
}
}
]
]
)
,[]
]



#]]]]]'''

__all__ = r'''
    stable_repr__expand_top_layer
    stable_repr_print__expand_top_layer

    stable_repr__expand_all_layer
    stable_repr_print__expand_all_layer

    stable_repr__expand_all_layer__noindent
    stable_repr_print__expand_all_layer__noindent

    stable_repr
    stable_repr_ex
    stable_repr_print
    stable_repr_print_ex

    sorted_by_SortableIterReprable
    sorted_by_SortableIterReprable_with_first_as_key
    sorted_mapping_by_SortableIterReprable

    make_iter_eol_indents
    IterEOLIndentsABC
        NoIterEOLIndents
            the_no_iter_indents
        IterEOLIndentsABC__irelpace
            FiniteIterEOLIndents
            IterEOLIndents

    SortableIterReprableABC
        SortableIterReprable4builtins
            SortableIterReprable__funcname_args_kwds
            SortableIterReprable__directly
            SortableIterReprable__iterable
                SortableIterReprable__tuple_list
                SortableIterReprable__set_frozenset
                SortableIterReprable__OrderedDict
            SortableIterReprable__dict

    directly_compare
    compare_on_sized_ordered_iterable
    sort_iterable

    iter_repr_on_ordered_iterable
        iter_repr_on_ordered_mapping_items
            iter_repr_on_mapping__by_ordered_items
        iter_repr_on_ordered_iterable__is_empty
            iter_repr_on_ordered_sized_iterable
            iter_repr_on_mapping__by_ordered_items

    iter_eithers5input4call
        iter_repr_on_input4call
        iter_repr_on_call__by_args_kwds

IGetFuncNameArgsOrderedKwds4stable_repr
    register4get__funcname__args__ordered_kwdxxxs
    get4get__funcname__args__ordered_kwdxxxs
    apply4get__funcname__args__ordered_kwdxxxs
    get__funcname__args__ordered_kwdxxxs____ex

    '''.split()#'''
    #check_echo
__all__

from seed.abc.abc__ver0 import abstractmethod, override, ABC, final
from seed.for_libs.for_operator.method_caller import method_caller
from seed.tiny import echo, fst
from seed.tiny import HexReprInt
from itertools import repeat
from types import MappingProxyType
from fractions import Fraction
from collections import OrderedDict
from functools import cmp_to_key, partial
import operator # __lt__, methodcaller


from seed.tiny_.check import check_pseudo_qual_name, check_pseudo_identifier, check_smay_pseudo_qual_name
from seed.tiny_.check import check_str, check_type_le, check_callable
from seed.tiny import ifNone, mk_tuple
from seed.lang.is_valid_python_id import is_valid_python_id
from keyword import iskeyword

#grep 'is.*abstrac' -i -r ../../python3_src/seed/ -l -a
import inspect #.isabstract
inspect.isabstract
import sys
sys.stdout

__all__

def check_echo(type_, obj):
    try:
        if type(obj) is not type_: raise TypeError
    except TypeError:
        from seed.tiny import print_err
        print_err(type, repr(obj))
    return obj
class IterEOLIndentsABC(ABC):
    'should be immutable value'
    @final
    def has_no_more_intents(self):
        '-> bool'
        return (self.has_no_intents()
                or check_echo(bool
                    , type(self).__has_no_more_intents__(self))
                )
    @final
    def has_no_intents(self):
        '-> bool'
        b = type(self).__has_no_intents__(self)
        return check_echo(bool, b)
    @final
    def iter_eol_indents(self):
        '-> Iter str'
        if self.has_no_intents():
            it = iter('')
        else:
            it = type(self).__iter_eol_indents__(self)
        if iter(it) is not it: raise TypeError
        return it
    @final
    def deeper(self):
        '-> IterEOLIndentsABC'
        #return type(self).__deeper__(self)
        #####################
        if self.has_no_more_intents():
            'should be immutable value'
            return the_no_iter_indents
        return type(self).__deeper__(self)
    @abstractmethod
    def __has_no_more_intents__(self):
        '-> bool'
        raise NotImplementedError
    @abstractmethod
    def __has_no_intents__(self):
        '-> bool'
        raise NotImplementedError
    @abstractmethod
    def __iter_eol_indents__(self):
        '-> Iter str'
        raise NotImplementedError
    @abstractmethod
    def __deeper__(self):
        '-> IterEOLIndentsABC'
        raise NotImplementedError

class NoIterEOLIndents(IterEOLIndentsABC):
    'immutable'
    def __new__(cls):
        try:
            return the_no_iter_indents
        except NameError:
            return super().__new__(cls)

    @override
    def __has_no_more_intents__(self):
        return True
    @override
    def __has_no_intents__(self):
        return True
    @override
    def __iter_eol_indents__(self):
        return; yield
    @override
    def __deeper__(self):
        return self
the_no_iter_indents = NoIterEOLIndents()

class IterEOLIndentsABC__irelpace(IterEOLIndentsABC):
    'immutable'
    @abstractmethod
    def get_kwargs(self):
        raise NotImplementedError
    def ireplace(self, **kwargs):
        d = self.get_kwargs()
        d.update(kwargs)
        return type(self)(**d)
    def copy(self):
        return self
        return self.ireplace()
class FiniteIterEOLIndents(IterEOLIndentsABC__irelpace):
    'immutable'
    def __init__(self, *, indents:tuple, length:int):
        if type(indents) is not tuple: raise TypeError
        if not all(type(indent) is str for indent in indents):raise TypeError
        if type(length) is not int: raise TypeError
        if not -1 <= length <= len(indents): raise TypeError
        self.__indents = indents
        self.__length = length
    @property
    def indents(self):
        return self.__indents
    @property
    def length(self):
        return self.__length
    ############################
    @override
    def get_kwargs(self):
        return dict(indents=self.indents, length=self.length)
    @override
    def __has_no_more_intents__(self):
        return self.length >= len(self.indents)
    @override
    def __has_no_intents__(self):
        return not 0 <= self.length <= len(self.indents)
    @override
    def __iter_eol_indents__(self):
        L = self.length
        if L < 0: return
        for i in range(L):
            yield self.indents[i]
    @override
    def __deeper__(self):
        return self.ireplace(length=self.length+1)
        L = self.length
        assert 0 <= L < len(self.indents)
        if not 0 <= L < len(self.indents):
            L = -1
        else:
            L += 1
        return self.ireplace(length=L)
class IterEOLIndents(IterEOLIndentsABC__irelpace):
    '''immutable
    maybe_max_depth is None ==>> inf; < 0 or < depth ==>> no indent
    '''
    def __init__(self, *, indent:str, depth:int, maybe_max_depth:[None,int]):
        assert type(indent) is str
        assert type(depth) is int
        assert maybe_max_depth is None or type(maybe_max_depth) is int
        if not depth >= -1: raise ValueError
        if maybe_max_depth is None and depth < 0: raise ValueError
        #if depth < 0: depth = -1
        self.__indent = indent
        self.__depth = depth
        self.__maybe_max_depth = maybe_max_depth
    @property
    def indent(self):
        return self.__indent
    @property
    def depth(self):
        return self.__depth
    @property
    def maybe_max_depth(self):
        return self.__maybe_max_depth
    ######################
    @override
    def __has_no_more_intents__(self):
        m = self.maybe_max_depth
        depth = self.depth
        return depth < 0 or (m is not None and m <= depth)
    @override
    def __has_no_intents__(self):
        m = self.maybe_max_depth
        depth = self.depth
        return depth < 0 or (m is not None and m < depth)
    @override
    def __iter_eol_indents__(self):
        if self.has_no_intents():
            return
        yield '\n'
        yield from repeat(self.indent, self.depth)
    @override
    def get_kwargs(self):
        return dict(
                indent=self.indent
                ,depth=self.depth
                ,maybe_max_depth=self.maybe_max_depth
                )
    @override
    def __deeper__(self):
        #bug: return type(self)(self.indent, self.depth+1)
        return self.ireplace(depth=self.depth+1)



def make_iter_eol_indents(*
    , indent:str, depth:int, maybe_max_depth:[None, int]
    ):
    if depth < 0 or (maybe_max_depth is not None and maybe_max_depth < 0):
        iter_eol_indents = the_no_iter_indents
    else:
        iter_eol_indents = IterEOLIndents(
            indent=indent
            ,depth=depth
            ,maybe_max_depth=maybe_max_depth
            )
    return iter_eol_indents


def sorted_by_SortableIterReprable(iterable, *
    , key, reverse:bool
    , SortableIterReprable:'subclass_of_SortableIterReprableABC'
    ):
    if type(reverse) is not bool: raise TypeError
    if key is None:
        key = echo
    if SortableIterReprable is None:
        cls = SortableIterReprable4builtins
    else:
        cls = SortableIterReprable
    mk = data2wobj = cls._make_sortable_iter_reprable_
    cmp = wobj_cmp = cls.compare_wobject
    wobj2key = cmp_to_key(cmp)
    obj2data = key
    def obj2key(obj):
        return wobj2key(data2wobj(obj2data(obj)))
    return sorted(iterable, key=obj2key, reverse=reverse)
def sorted_by_SortableIterReprable_with_first_as_key(iterable, *
    , key, reverse, SortableIterReprable
    ):
    'key = key . fst'
    if key is None:
        obj2data = fst
    else:
        def obj2data(obj):
            return key(fst(obj))
    return sorted_by_SortableIterReprable(iterable
            ,key=obj2data
            ,reverse=reverse
            ,SortableIterReprable=SortableIterReprable
            )
def sorted_mapping_by_SortableIterReprable(mapping, *
    , key, reverse, SortableIterReprable
    ):
    'key = key(key)'
    pairs = mapping.items()
    return sorted_by_SortableIterReprable_with_first_as_key(pairs
            ,key=key
            ,reverse=reverse
            ,SortableIterReprable=SortableIterReprable
            )

##################################
_kwargs4expand_top_layer = dict(indent='', depth=0, maybe_max_depth=1, has_head_eol_when_indent=False)
def stable_repr__expand_top_layer(obj, /):
    return stable_repr(obj, **_kwargs4expand_top_layer)
def stable_repr_print__expand_top_layer(may_ofile, obj, /):
    return stable_repr_print(may_ofile, obj, **_kwargs4expand_top_layer)
##################################
_kwargs4expand_all_layer = dict(indent='  ', depth=0, maybe_max_depth=None, has_head_eol_when_indent=True)
def stable_repr__expand_all_layer(obj, /):
    return stable_repr(obj, **_kwargs4expand_all_layer)
def stable_repr_print__expand_all_layer(may_ofile, obj, /):
    return stable_repr_print(may_ofile, obj, **_kwargs4expand_all_layer)
##################################
_kwargs4expand_all_layer__noindent = {**_kwargs4expand_all_layer, 'indent':''}
def stable_repr__expand_all_layer__noindent(obj, /):
    return stable_repr(obj, **_kwargs4expand_all_layer__noindent)
def stable_repr_print__expand_all_layer__noindent(may_ofile, obj, /):
    return stable_repr_print(may_ofile, obj, **_kwargs4expand_all_layer__noindent)
##################################
##################################
##################################

def stable_repr(obj, *
    , indent:str='    ', depth:int=-1, maybe_max_depth:[None, int]=None
    ,has_head_eol_when_indent:bool=True
    ):
    iter_eol_indents = make_iter_eol_indents(
        indent=indent, depth=depth, maybe_max_depth=maybe_max_depth)
    return stable_repr_ex(obj
                ,iter_eol_indents=iter_eol_indents
                ,has_head_eol_when_indent=has_head_eol_when_indent
                )
def stable_repr_ex(obj, *
    ,iter_eol_indents:IterEOLIndentsABC
    ,has_head_eol_when_indent:bool#default True
    ):
    mk = SortableIterReprable4builtins._make_sortable_iter_reprable_
    helper = mk(obj)
    return helper.stable_repr_data(
            iter_eol_indents=iter_eol_indents
            ,has_head_eol_when_indent=has_head_eol_when_indent
            )

def stable_repr_print(may_ofile, obj, *
    , indent:str='    ', depth:int=-1, maybe_max_depth:[None, int]=None
    , has_head_eol_when_indent:bool=True
    ):
    iter_eol_indents = make_iter_eol_indents(
        indent=indent, depth=depth, maybe_max_depth=maybe_max_depth)
    stable_repr_print_ex(may_ofile, obj
        ,iter_eol_indents=iter_eol_indents
        ,has_head_eol_when_indent=has_head_eol_when_indent
        )
def stable_repr_print_ex(may_ofile, obj, *
    ,iter_eol_indents:IterEOLIndentsABC
    ,has_head_eol_when_indent:bool#default True
    ):
    mk = SortableIterReprable4builtins._make_sortable_iter_reprable_
    helper = mk(obj)
    it = helper.stable_iter_repr_data(
            iter_eol_indents=iter_eol_indents
            ,has_head_eol_when_indent=has_head_eol_when_indent
            )

    ofile = ifNone(may_ofile, sys.stdout)
    for _ in map(ofile.write, it):pass




################################
def directly_compare(lhs_object, rhs_object, *, __lt__=operator.__lt__):
    if __lt__ is None:
        __lt__ = operator.__lt__

    if __lt__(lhs_object, rhs_object):
        return -1 # LT
    elif __lt__(rhs_object, lhs_object):
        #lhs_object > rhs_object:
        return +1 # GT
    else:
        return 0 # EQ

def compare_on_sized_ordered_iterable(cmp, lhs_wobjects, rhs_wobjects):
    r = directly_compare(len(lhs_wobjects), len(rhs_wobjects))
    if r: return r
    for r in map(cmp, lhs_wobjects, rhs_wobjects):
        if r: return r
    return 0
def sort_iterable(cmp, iterable):
    key = cmp_to_key(cmp)
    return sorted(iterable, key=key)





def iter_repr_on_ordered_sized_iterable(
    iter_repr_element, sized_iterable, *
    , sep, iter_eol_indents:IterEOLIndentsABC
    , iter_repr_on_ordered_iterable:[None, 'callable']
    , open:str, close:str
    , end4singleton
    , whole4empty:[None,str]
    ,has_head_eol_when_indent:bool#default True
    ):
    return (iter_repr_on_ordered_iterable__is_empty
    (iter_repr_element, sized_iterable
    ,is_empty=not sized_iterable
    ,open=open, close=close
    ,sep=sep, iter_eol_indents=iter_eol_indents
    ,end4singleton=end4singleton
    ,whole4empty=whole4empty
    ,iter_repr_on_ordered_iterable=iter_repr_on_ordered_iterable
    ,has_head_eol_when_indent=has_head_eol_when_indent
    ))


#[def____iter_repr_on_ordered_iterable__is_empty]:here
def iter_repr_on_ordered_iterable__is_empty(
    iter_repr_element, iterable, *
    ,is_empty:bool
    ,open:str, close:str
    ,sep, iter_eol_indents:IterEOLIndentsABC
    ,end4singleton
    ,whole4empty:[None,str]
    ,iter_repr_on_ordered_iterable:[None, 'callable']
    ,has_head_eol_when_indent:bool#default True
    ):
    'if whole4empty is not None, then use it instead of open+close'
    if is_empty:
        if whole4empty is not None:
            assert type(whole4empty) is str
            yield whole4empty
        else:
            yield open
            yield close
        return
    if iter_repr_on_ordered_iterable is None:
        iter_repr_on_ordered_iterable = globals()['iter_repr_on_ordered_iterable']

    yield open
    yield from iter_repr_on_ordered_iterable(
                iter_repr_element
                ,iterable
                ,sep=sep
                ,iter_eol_indents=iter_eol_indents.deeper()
                ,end4singleton=end4singleton
                ,has_head_eol_when_indent=has_head_eol_when_indent
                )
    if not iter_eol_indents.has_no_more_intents():
        yield from iter_eol_indents.iter_eol_indents()
    yield close

#[def____iter_repr_on_ordered_iterable]:here
def iter_repr_on_ordered_iterable(
    iter_repr_element, iterable, *
    , sep:str, iter_eol_indents:IterEOLIndentsABC
    , end4singleton:str
    , has_head_eol_when_indent:bool#default True
    ):
    'iter_repr_element :: element -> iter_eol_indents -> Iter str'
    assert type(has_head_eol_when_indent) is bool
    if end4singleton is None:
        end4singleton = ''
    if iter_eol_indents is None:
        iter_eol_indents = the_no_iter_indents
    if sep is None:
        sep = ', ' if iter_eol_indents.has_no_intents() else ','


    it = iter(iterable)
    for head in it:
        if has_head_eol_when_indent:
            yield from iter_eol_indents.iter_eol_indents()
        yield from iter_repr_element(head, iter_eol_indents=iter_eol_indents)
        break
    else:
        #empty
        return

    x = y = []
    for x in it:
        yield from iter_eol_indents.iter_eol_indents()
        yield sep
        yield from iter_repr_element(x, iter_eol_indents=iter_eol_indents)
    if x is y:
        # singleton
        # (x,)
        yield end4singleton


#[def____iter_repr_on_mapping__by_ordered_items]:here
def iter_repr_on_mapping__by_ordered_items(iter_repr_element, pairs, *
    ,is_empty:bool
    ,open:str, close:str
    ,item_sep:str, sep:str
    ,iter_eol_indents:IterEOLIndentsABC, end4singleton:str
    ,whole4empty:[None,str]
    ,has_head_eol_when_indent:bool#default True
    ):
    if 0:
      def iter_repr_on_ordered_iterable(
        iter_repr_element, pairs, *
        , sep:str, iter_eol_indents:IterEOLIndentsABC
        , end4singleton:str, has_head_eol_when_indent:bool#default True
        ):
        return iter_repr_on_ordered_mapping_items(
            iter_repr_element, pairs
            ,item_sep=item_sep
            ,sep=sep
            ,iter_eol_indents=iter_eol_indents
            ,end4singleton=end4singleton
            ,has_head_eol_when_indent=has_head_eol_when_indent
            )
    iter_repr_on_ordered_iterable = partial(iter_repr_on_ordered_mapping_items, item_sep=item_sep)

    return (iter_repr_on_ordered_iterable__is_empty
    (iter_repr_element, pairs
    ,is_empty=is_empty
    ,open=open, close=close
    ,sep=sep, iter_eol_indents=iter_eol_indents
    ,end4singleton=end4singleton
    ,whole4empty=whole4empty
    ,iter_repr_on_ordered_iterable=iter_repr_on_ordered_iterable
    ,has_head_eol_when_indent=has_head_eol_when_indent
    ))

#[def____iter_repr_on_ordered_mapping_items]:here
def iter_repr_on_ordered_mapping_items(iter_repr_element, pairs, *
    ,item_sep:str, sep:str
    ,iter_eol_indents:IterEOLIndentsABC, end4singleton:str
    ,has_head_eol_when_indent:bool#default True
    ):
    'iter_repr_element::element->Iter str'
    if item_sep is None:
        item_sep = ': ' # always
        # if iter_eol_indents.has_no_intents() else
    def iter_repr_pair(item):
        k,v = item
        yield from iter_repr_element(k)
        yield item_sep
        yield from iter_repr_element(v)
    def iter_repr_pair(item, *, iter_eol_indents):
        return iter_repr_on_ordered_iterable(iter_repr_element, item
                ,sep=item_sep
                ,iter_eol_indents=iter_eol_indents
                ,end4singleton=''
                ,has_head_eol_when_indent=False
                )
    return (iter_repr_on_ordered_iterable
    (iter_repr_pair, pairs
    ,sep=sep
    ,iter_eol_indents=iter_eol_indents
    ,end4singleton=end4singleton
    ,has_head_eol_when_indent=has_head_eol_when_indent
    ))


#[def____iter_repr_on_ordered_iterable]:goto
def iter_eithers5input4call(args, ordered_kwd_pairs):
    for x in args:
        yield False, x
    for nm, v in ordered_kwd_pairs:
        yield True, (nm, v)
def iter_repr_on_input4call(iter_repr_element, args, ordered_kwd_pairs, *
    ,item_sep:str, sep:str
    ,iter_eol_indents:IterEOLIndentsABC, end4singleton:str
    ,has_head_eol_when_indent:bool#default True
    ,open4py_kw:str, close4py_kw:str, item_sep4py_kw:str
    ):
    'iter_repr_element::element->Iter str'
    eithers = iter_eithers5input4call(args, ordered_kwd_pairs)
    return (_iter_repr_on_eithers5input4call
    (iter_repr_element, eithers
    ,item_sep=item_sep
    ,sep=sep
    ,iter_eol_indents=iter_eol_indents
    ,end4singleton=end4singleton
    ,has_head_eol_when_indent=has_head_eol_when_indent
    ,open4py_kw=open4py_kw, close4py_kw=close4py_kw, item_sep4py_kw=item_sep4py_kw
    ))
def _iter_repr_on_eithers5input4call(iter_repr_element, eithers, *
    ,item_sep:str, sep:str
    ,iter_eol_indents:IterEOLIndentsABC, end4singleton:str
    ,has_head_eol_when_indent:bool#default True
    ,open4py_kw:str, close4py_kw:str, item_sep4py_kw:str
    ):
    'iter_repr_element::element->Iter str'
    open4py_kw = ifNone(open4py_kw, '**{')
    close4py_kw = ifNone(close4py_kw, '}')
    item_sep4py_kw = ifNone(item_sep4py_kw, ': ')

    if item_sep is None:
        item_sep = '= ' # always
        # if iter_eol_indents.has_no_intents() else

    #[def____iter_repr_on_ordered_mapping_items]:goto
    #def iter_repr_pair(item, *, iter_eol_indents):
    def iter_repr_either(either_arg_or_kwd_pair, *, iter_eol_indents):
        #end4singleton=''
        #has_head_eol_when_indent=False
        is_kwd_pair, x = either_arg_or_kwd_pair
        if is_kwd_pair:
            #ordered_kwd_pairs
            nm, v = x
            if is_valid_python_id(nm):
                yield nm
                yield from iter_eol_indents.iter_eol_indents()
                yield item_sep
                yield from iter_repr_element(v, iter_eol_indents=iter_eol_indents)
            else:
                #[def____iter_repr_on_ordered_iterable__is_empty]:goto
                yield open4py_kw # '**{'
                if 1:
                    _iter_eol_indents = iter_eol_indents.deeper()
                    if has_head_eol_when_indent:
                        yield from _iter_eol_indents.iter_eol_indents()
                    yield repr(nm)
                    yield from _iter_eol_indents.iter_eol_indents()
                    yield item_sep4py_kw # ': '
                    yield from iter_repr_element(v, iter_eol_indents=_iter_eol_indents)
                if not iter_eol_indents.has_no_more_intents():
                    yield from iter_eol_indents.iter_eol_indents()
                yield close4py_kw # '}'
        else:
            #args
            v = x
            yield from iter_repr_element(v, iter_eol_indents=iter_eol_indents)
    return (iter_repr_on_ordered_iterable
    (iter_repr_either, eithers
    ,sep=sep
    ,iter_eol_indents=iter_eol_indents
    ,end4singleton=end4singleton
    ,has_head_eol_when_indent=has_head_eol_when_indent
    ))

#[def____iter_repr_on_mapping__by_ordered_items]:goto
def iter_repr_on_call__by_args_kwds(iter_repr_element, func_name, args, ordered_kwd_pairs, *
    ,is_empty:bool
    #,open:str, close:str
    ,item_sep:str, sep:str
    ,iter_eol_indents:IterEOLIndentsABC
    #,end4singleton:str
    #,whole4empty:[None,str]
    ,has_head_eol_when_indent:bool#default True
    #,open4py_kw:[None,str], close4py_kw:[None,str], item_sep4py_kw:[None,str]
    ):
    return (_iter_repr_on_call__by_args_kwds_
    (iter_repr_element, args, ordered_kwd_pairs
    ,open4py_kw=None, close4py_kw=None, item_sep4py_kw=None
    ,open=func_name+'(', close=')'
    ,end4singleton='' #(1,) vs f(1)
    ,whole4empty=None
    ,is_empty=is_empty
    ,item_sep=item_sep
    ,sep=sep
    ,iter_eol_indents=iter_eol_indents
    ,has_head_eol_when_indent=has_head_eol_when_indent
    #,open4py_kw=open4py_kw, close4py_kw=close4py_kw, item_sep4py_kw=item_sep4py_kw
    ))

def _iter_repr_on_call__by_args_kwds_(iter_repr_element, args, ordered_kwd_pairs, *
    ,is_empty:bool
    ,open:str, close:str
    ,item_sep:str, sep:str
    ,iter_eol_indents:IterEOLIndentsABC, end4singleton:str
    ,whole4empty:[None,str]
    ,has_head_eol_when_indent:bool#default True
    ,open4py_kw:str, close4py_kw:str, item_sep4py_kw:str
    ):
    eithers = iter_eithers5input4call(args, ordered_kwd_pairs)

    iter_repr_on_ordered_iterable = partial(_iter_repr_on_eithers5input4call, item_sep=item_sep, open4py_kw=open4py_kw, close4py_kw=close4py_kw, item_sep4py_kw=item_sep4py_kw)

    return (iter_repr_on_ordered_iterable__is_empty
    (iter_repr_element, eithers
    ,is_empty=is_empty
    ,open=open, close=close
    ,sep=sep, iter_eol_indents=iter_eol_indents
    ,end4singleton=end4singleton
    ,whole4empty=whole4empty
    ,iter_repr_on_ordered_iterable=iter_repr_on_ordered_iterable
    ,has_head_eol_when_indent=has_head_eol_when_indent
    ))




class SortableIterReprableABC(ABC):
    '''
    def _get_datatype2SortableIterReprable_(cls):
    def _from_data_(cls, data):
    def _get_datatype2name_(cls):
    def _get_name2datatype_(cls):
    def get_datatype(self):
    def stable_iter_repr_data(self, *
        ,iter_eol_indents:IterEOLIndentsABC
        ,has_head_eol_when_indent:bool#default True
        ):
    def compare_wobject_of_same_datatype(self, other):
    '''
    @classmethod
    @abstractmethod
    def _get_datatype2SortableIterReprable_(cls):
        '-> Map datatype subclass-of-SortableIterReprable'
        raise NotImplementedError
    @classmethod
    @abstractmethod
    def _from_data_(cls, data):
        raise NotImplementedError
    @classmethod
    @abstractmethod
    def _get_datatype2name_(cls):
        raise NotImplementedError
    @classmethod
    @abstractmethod
    def _get_name2datatype_(cls):
        raise NotImplementedError
    ##############
    @abstractmethod
    def get_datatype(self):
        raise NotImplementedError
    @abstractmethod
    def stable_iter_repr_data(self, *
        ,iter_eol_indents:IterEOLIndentsABC
        ,has_head_eol_when_indent:bool#default True
        ):
        raise NotImplementedError
    @abstractmethod
    def compare_wobject_of_same_datatype(self, other):
        raise NotImplementedError

    #################################################
    #################################################
    @final
    def stable_repr_data(self, *
        , iter_eol_indents, has_head_eol_when_indent:bool
        ):
        mk_it = lambda: self.stable_iter_repr_data(
                    iter_eol_indents=iter_eol_indents
                    ,has_head_eol_when_indent=has_head_eol_when_indent
                    )
        try:
            return ''.join(mk_it())
        except Exception:
            from seed.tiny import print_err
            print_err(list(mk_it()))
            raise
    @classmethod
    @final
    def _make_sortable_iter_reprable_(cls, data):
        datatype = type(data)
        d = cls._get_datatype2SortableIterReprable_()
        SortableIterReprable = d[datatype]
        return SortableIterReprable._from_data_(data)
    @final
    def compare_wobject(self, other):
        S = type(self)
        O = type(other)
        t2n = S._get_datatype2name_()
        if t2n is not O._get_datatype2name_():
            raise Exception(f'{S!r} and {O!r} are not in same domain')

        SD = self.get_datatype()
        OD = other.get_datatype()
        if SD is OD:
            return self.compare_wobject_of_same_datatype(other)

        SN = t2n[SD]
        ON = t2n[OD]
        return directly_compare(SN, ON)

    @classmethod
    def register_datatype_and_name_and_SortableIterReprable(cls
        , datatype, name, SortableIterReprable
        ):
        assert isinstance(datatype, type)
        assert type(name) is str
        t2n = cls._get_datatype2name_()
        n2t = cls._get_name2datatype_()
        t2S = cls._get_datatype2SortableIterReprable_()
        assert len(t2n) == len(n2t) == len(t2S)
        if datatype in t2n:
            raise Exception(f'datatype {datatype!r} has been registered!')
        if name in n2t:
            raise Exception(f'datatype name {name!r} has been registered!')
        t2n.setdefault(datatype, name)
        n2t.setdefault(name, datatype)
        t2S.setdefault(datatype, SortableIterReprable)
        return
        ##
        if name in n2t:
            T = n2t[name]
            if datatype is T:
                if datatype not in t2n or t2n[datatype] != name:
                    raise logic-err
                else:
                    pass
            else:
                #datatype is not T
                raise Exception(f'name {name!r} is mapping to anoter datatype {T!r} other than datatype {datatype!r}')
        elif datatype in t2n:
            N = t2n[datatype]
            if N != name:
                raise Exception(f'datatype {datatype!r} has been registered with another name {N!r} other than name {name!r}')
            else:
                pass
        else:
            assert datatype not in t2n
            assert name not in n2t
            t2n.setdefault(datatype, name)
            n2t.setdefault(name, datatype)
            assert n2t[name] is datatype
            assert t2n[datatype] == name

class _IGetFuncNameArgsOrderedKwds4stable_repr(ABC):
    __slots__ = ()
    _ty2nm = {}
    _nm2ty = {}
    _ty2f = {}
class IGetFuncNameArgsOrderedKwds4stable_repr(ABC):
    r'''[[[
    'see:SortableIterReprable__funcname_args_kwds'
    'see:IGetFuncNameArgsOrderedKwds4stable_repr'
    'see:register4get__funcname__args__ordered_kwdxxxs'
    'see:get4get__funcname__args__ordered_kwdxxxs'
    #]]]'''#'''
    __slots__ = ()
    @abstractmethod
    def ___get__funcname__args__ordered_kwdxxxs___(sf):
        '-> (may func_name, args, (ordered_kwd_pairs/[(nm,v)]|ordered_field_names__str/str|ordered_either_Ellipsis_field_name_pair_or_kwd_pair__seq)/[((nm,v)|(Ellipsis,nm))])'
    @classmethod
    def __init_subclass__(cls, /, **kwargs):
        if not inspect.isabstract(cls):
            get4get__funcname__args__ordered_kwdxxxs(cls)
                #==>> register4get__funcname__args__ordered_kwdxxxs(cls, None, None)
        super().__init_subclass__(**kwargs)
    #end-def __init_subclass__(cls, /, *, ...):

def register4get__funcname__args__ordered_kwdxxxs(datatype, may_xname, ___get__funcname__args__ordered_kwdxxxs___):
    check_type_le(type, datatype)

    xname = ifNone(may_xname, f'{datatype.__module__}:{datatype.__qualname__}')
    check_str(xname) #neednot check_pseudo_qual_name

    if ___get__funcname__args__ordered_kwdxxxs___ is None:
        m = getattr(datatype, '___get__funcname__args__ordered_kwdxxxs___', None)
        if m is None:
            raise LookupError(datatype)
            raise TypeError(datatype)
        ___get__funcname__args__ordered_kwdxxxs___ = m
    check_callable(___get__funcname__args__ordered_kwdxxxs___)

    T = _IGetFuncNameArgsOrderedKwds4stable_repr
    t2n = T._ty2nm
    n2t = T._nm2ty
    t2f = T._ty2f
    if datatype in t2n: raise KeyError(datatype)
    if xname in n2t: raise KeyError(xname)

    if 1:
        SortableIterReprable4builtins.register_datatype_and_name_and_SortableIterReprable(datatype, xname, SortableIterReprable__funcname_args_kwds)

    t2n[datatype] = xname
    n2t[xname] = datatype
    t2f[datatype] = ___get__funcname__args__ordered_kwdxxxs___
def get4get__funcname__args__ordered_kwdxxxs(datatype):
    'datatype -> (xname, ___get__funcname__args__ordered_kwdxxxs___)'
    check_type_le(type, datatype)
    T = _IGetFuncNameArgsOrderedKwds4stable_repr
    t2n = T._ty2nm
    n2t = T._nm2ty
    t2f = T._ty2f

    m = t2f.get(datatype)
    while m is None:
        ___get__funcname__args__ordered_kwdxxxs___ = None
        may_xname = None
        register4get__funcname__args__ordered_kwdxxxs(datatype, may_xname, ___get__funcname__args__ordered_kwdxxxs___)
        m = t2f.get(datatype)
    else:
        ___get__funcname__args__ordered_kwdxxxs___ = m
        xname = t2n[datatype]
    return (xname, ___get__funcname__args__ordered_kwdxxxs___)



def apply4get__funcname__args__ordered_kwdxxxs(___get__funcname__args__ordered_kwdxxxs___, sf):
    '-> (func_name, args, ordered_kwd_pairs)'
    (may_func_name, args, ordered_kwdxxxs) = ___get__funcname__args__ordered_kwdxxxs___(sf)
    if type(ordered_kwdxxxs) is str:
        ordered_field_names__str = ordered_kwdxxxs
        ordered_field_names__str.replace(',', ' ')
        ordered_field_names = ordered_field_names__str.split()
        ordered_either_pairs = [(..., nm) for nm in ordered_field_names]
    else:
        ordered_either_pairs = ordered_kwdxxxs
    ordered_either_pairs

    ordered_kwd_pairs = []
    for a, b in ordered_either_pairs:
        if a is ...:
            nm = b
            v = getattr(sf, nm)
        else:
            nm = a
            v = b
        #if not str.isidentifier(nm):raise ValueError(nm)
        check_pseudo_identifier(nm)
        #check_pseudo_qual_name
        ordered_kwd_pairs.append((nm, v))
    ordered_kwd_pairs


    ordered_kwd_pairs = mk_tuple(ordered_kwd_pairs)
    args = mk_tuple(args)
    func_name = ifNone(may_func_name, type(sf).__qualname__)
    check_str(func_name)
    return (func_name, args, ordered_kwd_pairs)


def get__funcname__args__ordered_kwdxxxs____ex(data):
    'data -> (xname, func_name, args, ordered_kwd_pairs)'
    datatype = type(data)
    (xname, ___get__funcname__args__ordered_kwdxxxs___) = get4get__funcname__args__ordered_kwdxxxs(datatype)
    (func_name, args, ordered_kwd_pairs) = apply4get__funcname__args__ordered_kwdxxxs(___get__funcname__args__ordered_kwdxxxs___, data)
    return (xname, func_name, args, ordered_kwd_pairs)

class SortableIterReprable4builtins(SortableIterReprableABC):
    '''
    def _from_data_(cls, data):
    def get_datatype(self):
    def stable_iter_repr_data(self, *
        ,iter_eol_indents:IterEOLIndentsABC
        ,has_head_eol_when_indent:bool#default True
        ):
    def compare_wobject_of_same_datatype(self, other):
    '''
    datatype2SortableIterReprable = {}
    datatype2name = {}
    name2datatype = {}
    @classmethod
    @override
    def _get_datatype2SortableIterReprable_(cls):
        return cls.datatype2SortableIterReprable
    @classmethod
    @override
    def _get_datatype2name_(cls):
        return cls.datatype2name
    @classmethod
    @override
    def _get_name2datatype_(cls):
        return cls.name2datatype
SortableIterReprable4builtins

#class SortableIterReprable__funcname_args_kwds(SortableIterReprableABC):
class SortableIterReprable__funcname_args_kwds(SortableIterReprable4builtins):
    r'''[[[
    'see:IGetFuncNameArgsOrderedKwds4stable_repr'
    'see:SortableIterReprable__funcname_args_kwds'
    'see:iter_repr_on_call__by_args_kwds'
    #]]]'''#'''
    def __init__(sf, data, /):
        #sf.data = data
        datatype = type(data)
        (xname, ___get__funcname__args__ordered_kwdxxxs___) = get4get__funcname__args__ordered_kwdxxxs(datatype)
        sf.datatype = datatype
        sf._xname = xname
        sf._3 = sf._explain_data(___get__funcname__args__ordered_kwdxxxs___, data)
    def _explain_data(sf, ___get__funcname__args__ordered_kwdxxxs___, data, /):
        (func_name, args, ordered_kwd_pairs) = apply4get__funcname__args__ordered_kwdxxxs(___get__funcname__args__ordered_kwdxxxs___, data)
        mk = SortableIterReprable4builtins._make_sortable_iter_reprable_
        #wrapped:args,ordered_kwd_pairs
        wargs = tuple(map(mk, args))
        wordered_kwd_pairs = tuple((nm, mk(v)) for nm, v in ordered_kwd_pairs)
        return (func_name, wargs, wordered_kwd_pairs)

    @classmethod
    @override
    def _from_data_(cls, data):
        return cls(data)

    if 0:
        #since now [__class__ <: SortableIterReprable4builtins]
        #bug:
        @classmethod
        @override
        def _get_datatype2SortableIterReprable_(cls):
            '-> Map datatype subclass-of-SortableIterReprable'
            raise logic-err
            return __class__
    if 0:
        #since now [__class__ <: SortableIterReprable4builtins]
        @classmethod
        @override
        def _get_datatype2name_(cls):
            T = _IGetFuncNameArgsOrderedKwds4stable_repr
            t2n = T._ty2nm
            return t2n
        @classmethod
        @override
        def _get_name2datatype_(cls):
            T = _IGetFuncNameArgsOrderedKwds4stable_repr
            n2t = T._nm2ty
            return n2t
    ##############
    @override
    def get_datatype(self):
        return self.datatype
    @override
    def stable_iter_repr_data(self, *
        ,iter_eol_indents:IterEOLIndentsABC
        ,has_head_eol_when_indent:bool#default True
        ):
        #(func_name, args, ordered_kwd_pairs) = self._explain_data()
        (func_name, wargs, wordered_kwd_pairs) = self._3

        datatype = self.datatype
        f = method_caller('stable_iter_repr_data', has_head_eol_when_indent=has_head_eol_when_indent)
        return (iter_repr_on_call__by_args_kwds
        (f, func_name, wargs, wordered_kwd_pairs
        ,is_empty= 0 == (len(wargs) + len(wordered_kwd_pairs))
        ,sep=None
        ,item_sep=None
        ,iter_eol_indents=iter_eol_indents
        ,has_head_eol_when_indent=has_head_eol_when_indent
        ))


    @override
    def compare_wobject_of_same_datatype(self, other):
        (func_nameL, wargsL, wordered_kwd_pairsL) = self._3
        (func_nameR, wargsR, wordered_kwd_pairsR) = other._3
        cmp = SortableIterReprableABC.compare_wobject
        cmp_ls = directly_compare, cmp, cmp
        for _cmp, _x, _y in zip(self._3, other._3):
            r = _cmp(_x, _y)
            if r:
                break
        else:
            r = 0
        return r
        #return compare_on_sized_ordered_iterable(cmp, self._explain_data(), other._explain_data())
SortableIterReprable__funcname_args_kwds
r'''[[[
#]]]'''#'''



class SortableIterReprable__directly(SortableIterReprable4builtins):
    supported_types = {
        type(None) # NoneType
        , type(...) # Ellipsis ellipsis
        , type(NotImplemented) # NotImplementedType
        , bool, int, float, complex, Fraction
            , HexReprInt
        , bytes, bytearray, str
        }

    @classmethod
    @override
    def _from_data_(cls, data):
        return cls(data)
    def __init__(self, data):
        datatype = type(data)
        if datatype not in type(self).supported_types:
            raise TypeError(datatype)
        self.data = data

    @override
    def get_datatype(self):
        return type(self.data)
    @override
    def stable_iter_repr_data(self, *
        ,iter_eol_indents:IterEOLIndentsABC
        ,has_head_eol_when_indent:bool#default True
        ):
        yield repr(self.data)
    @override
    def compare_wobject_of_same_datatype(self, other):
        return directly_compare(self.data, other.data)

class SortableIterReprable__iterable(SortableIterReprable4builtins):
    '''
    supported_types = ...
    def _data2wobjects_(cls, data):
    def get_kwargs_for_repr_iterable(self):
    '''
    #supported_types = ...

    @classmethod
    @abstractmethod
    def _data2wobjects_(cls, data):
        raise NotImplementedError
    @abstractmethod
    def get_kwargs_for_repr_iterable(self):
        '-> {open=str, close=str, end4singleton=str, whole4empty=(None|str)}'
        raise NotImplementedError

    @classmethod
    @override
    def _from_data_(cls, data):
        return cls(data)
    def __init__(self, data):
        cls = type(self)
        datatype = type(data)
        if datatype not in cls.supported_types:
            raise TypeError(datatype)

        wobjects = cls._data2wobjects_(data)
        if type(wobjects) is not tuple:
            raise TypeError

        #self.data = data
        self.datatype = datatype
        self.wobjects = wobjects

    @override
    def get_datatype(self):
        return self.datatype



    @override
    def stable_iter_repr_data(self, *
        ,iter_eol_indents:IterEOLIndentsABC
        ,has_head_eol_when_indent:bool#default True
        ):
        f = method_caller('stable_iter_repr_data', has_head_eol_when_indent=has_head_eol_when_indent)
        kwargs = self.get_kwargs_for_repr_iterable()
        return iter_repr_on_ordered_sized_iterable(f, self.wobjects
            ,iter_eol_indents=iter_eol_indents
            ,sep=None
            ,iter_repr_on_ordered_iterable=None
            ,has_head_eol_when_indent=has_head_eol_when_indent
            ,**kwargs
            )


    @override
    def compare_wobject_of_same_datatype(self, other):
        cmp = SortableIterReprableABC.compare_wobject
        return compare_on_sized_ordered_iterable(cmp, self.wobjects, other.wobjects)


class SortableIterReprable__tuple_list(SortableIterReprable__iterable):
    supported_types = {tuple, list}

    @classmethod
    @override
    def _data2wobjects_(cls, data):
        mk = SortableIterReprable4builtins._make_sortable_iter_reprable_
        wobjects = tuple(map(mk, data))
        return wobjects
    @override
    def get_kwargs_for_repr_iterable(self):
        datatype = self.datatype
        open, close = '()' if datatype is tuple else '[]'
        end4singleton = ',' if datatype is tuple else ''
        kwargs = dict(
            open=open, close=close, end4singleton=end4singleton
            ,whole4empty=None
            )
        return kwargs
    '''
    @override
    def stable_iter_repr_data(self, *, iter_eol_indents:IterEOLIndentsABC):
        if len(self.wobjects) == 1:
            datatype = self.datatype
            if datatype is tuple:
                [wobject] = self.wobjects
                def _iter():
                    yield '('
                    yield from wobject.stable_iter_repr_data(iter_eol_indents=iter_eol_indents)
                    yield ',)'
                return _iter()
        return super().stable_iter_repr_data(iter_eol_indents=iter_eol_indents)
    '''


class SortableIterReprable__set_frozenset(SortableIterReprable__iterable):
    supported_types = {set, frozenset}

    @classmethod
    @override
    def _data2wobjects_(cls, data):
        mk = SortableIterReprable4builtins._make_sortable_iter_reprable_
        cmp = SortableIterReprableABC.compare_wobject
        wobjects = tuple(sort_iterable(cmp, map(mk, data)))
        return wobjects
    @override
    def get_kwargs_for_repr_iterable(self):
        datatype = self.datatype
        open, close = '{}' if datatype is set else ('frozenset({', '})')
        whole4empty='set()' if datatype is set else 'frozenset()'
        kwargs = dict(
            open=open, close=close, end4singleton=''
            ,whole4empty=whole4empty
            )
        return kwargs


class SortableIterReprable__OrderedDict(SortableIterReprable__iterable):
    supported_types = {OrderedDict}

    @classmethod
    @override
    def _data2wobjects_(cls, data):
        it = data.items()
        mk = SortableIterReprable4builtins._make_sortable_iter_reprable_
        wobjects = tuple(map(mk, it))
        return wobjects
    @override
    def get_kwargs_for_repr_iterable(self):
        datatype = self.datatype
        open, close = ('OrderedDict([', '])')
        kwargs = dict(
            open=open, close=close, end4singleton=''
            ,whole4empty='OrderedDict()'
            )
        return kwargs

class SortableIterReprable__dict(SortableIterReprable4builtins):
    supported_types = {dict}
    @classmethod
    def _data2wobject_pairs_(cls, data):
        mk = SortableIterReprable4builtins._make_sortable_iter_reprable_
        it_pairs = ((mk(k), mk(v)) for k, v in data.items())
        pairs = sort_iterable(cls._cmp_pair, it_pairs)
        return tuple(pairs)

    def get_kwargs_for_repr_mapping(self):
        open, close = '{}'
        kwargs = dict(
            open=open, close=close, end4singleton=''
            ,whole4empty=None
            )
        return kwargs

    @classmethod
    @override
    def _from_data_(cls, data):
        return cls(data)
    def __init__(self, data):
        cls = type(self)
        datatype = type(data)
        if datatype not in cls.supported_types:
            raise TypeError(datatype)

        wobject_pairs = cls._data2wobject_pairs_(data)
        if type(wobject_pairs) is not tuple:
            raise TypeError
        if not all(type(pair) is tuple and len(pair)==2 for pair in wobject_pairs):
            raise TypeError

        #self.data = data
        self.datatype = datatype
        self.wobject_pairs = wobject_pairs

    @override
    def get_datatype(self):
        return self.datatype



    @override
    def stable_iter_repr_data(self, *
        ,iter_eol_indents:IterEOLIndentsABC
        ,has_head_eol_when_indent:bool#default True
        ):
        datatype = self.datatype
        kwargs = self.get_kwargs_for_repr_mapping()
        f = method_caller('stable_iter_repr_data', has_head_eol_when_indent=has_head_eol_when_indent)
        return (iter_repr_on_mapping__by_ordered_items
        (f, self.wobject_pairs
        ,is_empty=not self.wobject_pairs
        ,sep=None
        ,item_sep=None
        ,iter_eol_indents=iter_eol_indents
        ,has_head_eol_when_indent=has_head_eol_when_indent
        ,**kwargs
        ))

    _cmp1 = SortableIterReprableABC.compare_wobject
    @classmethod
    def _cmp_pair(cls, lhs_pair, rhs_pair):
        return compare_on_sized_ordered_iterable(cls._cmp1, lhs_pair, rhs_pair)
    @override
    def compare_wobject_of_same_datatype(self, other):
        return compare_on_sized_ordered_iterable(type(self)._cmp_pair, self.wobject_pairs, other.wobject_pairs)



def __register():
    S = SortableIterReprable4builtins
    register = S.register_datatype_and_name_and_SortableIterReprable

    Sdy = SortableIterReprable__directly
    Stl = SortableIterReprable__tuple_list
    Ssf = SortableIterReprable__set_frozenset
    SO = SortableIterReprable__OrderedDict
    Sdc = SortableIterReprable__dict
    for S__ in [Sdy, Stl, Ssf, SO, Sdc]:
        for datatype in S__.supported_types:
            if 0b00:
                register(datatype, datatype.__name__, S__)
            else:
                register(datatype, datatype.__qualname__, S__)
__register(); del __register




















from seed.helper.stable_repr import stable_repr, stable_repr_ex, stable_repr_print, stable_repr_print_ex
from seed.helper.stable_repr import stable_repr__expand_top_layer, stable_repr_print__expand_top_layer
from seed.helper.stable_repr import stable_repr__expand_all_layer, stable_repr_print__expand_all_layer
from seed.helper.stable_repr import stable_repr__expand_all_layer__noindent, stable_repr_print__expand_all_layer__noindent


from seed.helper.stable_repr import IGetFuncNameArgsOrderedKwds4stable_repr, register4get__funcname__args__ordered_kwdxxxs, get4get__funcname__args__ordered_kwdxxxs

from seed.helper.stable_repr import *

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):







