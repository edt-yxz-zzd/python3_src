
'''
dict/set are unordered
let us sorted it

see:
    ast.literal_eval
    seed.helper.safe_eval
        # for "set()"


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




'''

__all__ = '''
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
    '''.split()
    #check_echo

from seed.abc import abstractmethod, override, ABC, final
from seed.for_libs.for_operator.method_caller import method_caller
from seed.tiny import echo, fst
from itertools import repeat
from types import MappingProxyType
from fractions import Fraction
from collections import OrderedDict
from functools import cmp_to_key
import operator # __lt__, methodcaller

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

def stable_repr_print(ofile, obj, *
    , indent:str='    ', depth:int=-1, maybe_max_depth:[None, int]=None
    , has_head_eol_when_indent:bool=True
    ):
    iter_eol_indents = make_iter_eol_indents(
        indent=indent, depth=depth, maybe_max_depth=maybe_max_depth)
    stable_repr_print_ex(ofile, obj
        ,iter_eol_indents=iter_eol_indents
        ,has_head_eol_when_indent=has_head_eol_when_indent
        )
def stable_repr_print_ex(ofile, obj, *
    ,iter_eol_indents:IterEOLIndentsABC
    ,has_head_eol_when_indent:bool#default True
    ):
    mk = SortableIterReprable4builtins._make_sortable_iter_reprable_
    helper = mk(obj)
    it = helper.stable_iter_repr_data(
            iter_eol_indents=iter_eol_indents
            ,has_head_eol_when_indent=has_head_eol_when_indent
            )
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
    return iter_repr_on_ordered_iterable__is_empty(
            iter_repr_element, sized_iterable
            ,is_empty=not sized_iterable
            ,open=open, close=close
            ,sep=sep, iter_eol_indents=iter_eol_indents
            ,end4singleton=end4singleton
            ,whole4empty=whole4empty
            ,iter_repr_on_ordered_iterable=iter_repr_on_ordered_iterable
            ,has_head_eol_when_indent=has_head_eol_when_indent
            )


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


def iter_repr_on_mapping__by_ordered_items(iter_repr_element, pairs, *
    ,is_empty:bool
    ,open:str, close:str
    ,item_sep:str, sep:str
    ,iter_eol_indents:IterEOLIndentsABC, end4singleton:str
    ,whole4empty:[None,str]
    ,has_head_eol_when_indent:bool#default True
    ):
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
    return iter_repr_on_ordered_iterable__is_empty(
            iter_repr_element, pairs
            ,is_empty=is_empty
            ,open=open, close=close
            ,sep=sep, iter_eol_indents=iter_eol_indents
            ,end4singleton=end4singleton
            ,whole4empty=whole4empty
            ,iter_repr_on_ordered_iterable=iter_repr_on_ordered_iterable
            ,has_head_eol_when_indent=has_head_eol_when_indent
            )

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
    return iter_repr_on_ordered_iterable(iter_repr_pair, pairs
            ,sep=sep
            ,iter_eol_indents=iter_eol_indents
            ,end4singleton=end4singleton
            ,has_head_eol_when_indent=has_head_eol_when_indent
            )



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
            raise Exception('datatype {datatype!r} has been registered!')
        if name in n2t:
            raise Exception('datatype name {name!r} has been registered!')
        t2n.setdefault(datatype, name)
        n2t.setdefault(name, datatype)
        t2S.setdefault(datatype, SortableIterReprable)
        return
        ##
        if name in n2t:
            T = n2t[name]
            if datatype is T:
                if datatype not in t2n or t2n[datatype] != name:
                    raise logic-error
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

class SortableIterReprable__directly(SortableIterReprable4builtins):
    supported_types = {
        type(None) # NoneType
        , type(...) # Ellipsis ellipsis
        , type(NotImplemented) # NotImplementedType
        , bool, int, float, complex, Fraction
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
        cmp = SortableIterReprable4builtins.compare_wobject
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
        cmp = SortableIterReprable4builtins.compare_wobject
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
        return iter_repr_on_mapping__by_ordered_items(
                f, self.wobject_pairs
                ,is_empty=not self.wobject_pairs
                ,sep=None
                ,item_sep=None
                ,iter_eol_indents=iter_eol_indents
                ,has_head_eol_when_indent=has_head_eol_when_indent
                ,**kwargs
                )

    _cmp1 = SortableIterReprable4builtins.compare_wobject
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
            register(datatype, datatype.__name__, S__)
__register(); del __register










if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


















