


r'''
>>> from ..OtherOps.TotalOrderingOps import python_total_key_ops
>>> from ..OtherOps.EqOps import python_eq_key_ops
>>> This = BlockDict

>>> from ..BlockDictOps__concrete.theUInt_as_BlockDictKeyOps import theUInt_as_BlockDictKeyOps
>>> UIntBlockDict = lambda *args, **kwargs: This(theUInt_as_BlockDictKeyOps, None, *args, **kwargs)
>>> block_dict_key_ops = theUInt_as_BlockDictKeyOps

>>> the0 = block_dict_key_ops.mkTheKey(0)
>>> the1 = block_dict_key_ops.mkTheKey(1)
>>> the2 = block_dict_key_ops.mkTheKey(2)
>>> the3 = block_dict_key_ops.mkTheKey(3)
>>> the4 = block_dict_key_ops.mkTheKey(4)
>>> the5 = block_dict_key_ops.mkTheKey(5)
>>> the6 = block_dict_key_ops.mkTheKey(6)
>>> the7 = block_dict_key_ops.mkTheKey(7)


>>> empty = UIntBlockDict()
>>> m = UIntBlockDict([(1, 'a'), (3, 'b'), (4, 'b'), (5, 'c'), (0, 'k')])

>>> m.block_dict_key_ops is m.get_block_dict_key_ops()
True
>>> m.block_key2block_items((the1, the3)) == [((the1, the1), 'a'), ((the3, the3), 'b')]
True
>>> m.block_key2block_items((the1, the3), reverse=True) == [((the3, the3), 'b'), ((the1, the1), 'a')]
True

>>> empty.block_key2block_items((the1, the5))
[]
>>> [*m.block_key2iter_block_items((the1, the5))] == [((the1, the1), 'a'), ((the3, the4), 'b'), ((the5, the5), 'c')]
True
>>> [*m.block_key2iter_block_items((the5, the1))]
[]

>>> t = m.copy()
>>> t == empty
False
>>> t == m
True
>>> t.clear()
>>> t.get_num_block_keys()
0
>>> t == empty
True
>>> m.get_num_block_keys()
4

>>> m == m.copy()
True
>>> m.dict_key2block_items(2)
[]
>>> m.dict_key2block_items(1) == [((the1, the1), 'a')]
True
>>> m.dict_value_eq('a', 'a')
True
>>> m.dict_value_eq('a', 'b')
False
>>> m.dict_value_eq is m.eq_dict_value_ops.eq
True

>>> t = m.copy()
>>> t.discard_block_items_of_block_key((the1, the4))
>>> t.get_num_block_keys()
2
>>> [*t.iter_block_items()] == [((the0, the0), 'k'), ((the5, the5), 'c')]
True


>>> m.eq_dict_value_ops is m.get_eq_dict_value_ops()
True
>>> m.get(4)
'b'
>>> m.get(6)
>>> m.get_block_dict_key_ops() is block_dict_key_ops
True
>>> m.get_eq_dict_value_ops() is python_eq_key_ops
True

>>> empty.get_num_block_keys()
0
>>> m.get_num_block_keys()
4

>>> m.get_total_dict_key_ops() is python_total_key_ops
True

>>> [*empty.iter_block_items()]
[]
>>> [*m.iter_block_items()] == [((the0, the0), 'k'), ((the1, the1), 'a'), ((the3, the4), 'b'), ((the5, the5), 'c')]
True
>>> [*m.iter_block_items()] == [*reversed([*m.iter_block_items(reverse=True)])]
True
>>> [*m.iter_block_keys()] == [(the0, the0), (the1, the1), (the3, the4), (the5, the5)]
True
>>> [*m.iter_dict_values()] == list('kabc')
True
>>> m.list_all_touch_or_overlap_block_items((the1, the3), False) == [((the0, the0), 'k'), ((the1, the1), 'a'), ((the3, the4), 'b')]
True

>>> t = This.make_empty_block_dict(block_dict_key_ops, python_total_key_ops)
>>> t.block_dict_key_ops is block_dict_key_ops
True
>>> t.eq_dict_value_ops is python_total_key_ops
True


>>> m.mkSingletonRange(1) == (the1, the1)
True
>>> m.pop(2)
Traceback (most recent call last):
    ...
KeyError: 2
>>> m.pop(2, None)
>>> m.pop(2, 'abc')
'abc'



>>> t = m.copy()
>>> t.pop(1)
'a'
>>> t.get_num_block_keys()
3
>>> t.pop(3)
'b'
>>> t.get_num_block_keys()
3
>>> t.pop(4)
'b'
>>> t.get_num_block_keys()
2
>>> [*t.iter_dict_values()]
['k', 'c']


>>> t = m.copy()
>>> t.pop_block_item() == ((the5, the5), 'c')
True
>>> t = m.copy()
>>> t.pop_block_item_of_dict_key(4) == ((the4, the4), 'b')
True
>>> 4 not in t
True
>>> 3 in t
True

>>> t = m.copy()
>>> t.pop_block_items_of_block_key((the3, the1))
[]
>>> t.pop_block_items_of_block_key((the1, the3), reverse=True) == [((the3, the3), 'b'), ((the1, the1), 'a')]
True
>>> t.pop_block_items_of_block_key((the1, the3))
[]

>>> t = m.copy()
>>> t.pop_block_items_of_dict_key(2)
[]
>>> t.pop_block_items_of_dict_key(1) == [((the1, the1), 'a')]
True
>>> t = m.copy()
>>> t.pop_left_or_right_block_item(False) == ((the0, the0), 'k')
True
>>> t.pop_left_or_right_block_item(True) == ((the5, the5), 'c')
True

>>> t = m.copy()
>>> t.pop_right_block_item() == m.copy().pop_left_or_right_block_item(True)
True
>>> t.pop_left_block_item() == m.copy().pop_left_or_right_block_item(False)
True

>>> t = m.copy()
>>> t.set_block_item((the2, the3), 'a')
>>> t.get_num_block_keys()
4
>>> t.block_key2block_items(((the0, block_dict_key_ops.getTheMaxKeyEx())), reverse=True) == [*t.iter_block_items(reverse=True)] == [((the5, the5), 'c'), ((the4, the4), 'b'), ((the1, the3), 'a'), ((the0, the0), 'k')]
True
>>> t.block_key2block_items(((the0, block_dict_key_ops.getTheMaxKeyEx()))) == [*t.iter_block_items()] == [((the0, the0), 'k'), ((the1, the3), 'a'), ((the4, the4), 'b'), ((the5, the5), 'c')]
True


>>> t = m.copy()
>>> t.set_fdefault(1, ...)
'a'
>>> t[1]
'a'
>>> t.set_fdefault(2, lambda: 'a')
'a'
>>> _ = t.pop_left_block_item()
>>> t.pop_left_block_item() == ((the1, the2), 'a')
True
>>> t.set_fdefault(2, lambda: 'x')
'x'

>>> t = m.copy()
>>> t.setdefault(1, 'y')
'a'
>>> t[1]
'a'
>>> t.setdefault(2, 'c')
'c'
>>> t.get_num_block_keys()
5
>>> t[2]
'c'
>>> t.setdefault(6, '.')
'.'
>>> t[6]
'.'


>>> m.total_dict_key_ops is m.get_total_dict_key_ops()
True

>>> t = m.copy()
>>> t.pop(3)
'b'
>>> t[1] = 'x'
>>> t.update(m)
>>> t == m
True
>>> t.update((k, 'c') for k in range(5))
>>> t.get_num_block_keys()
1
>>> [*t.iter_block_items()] == [((the0, the5), 'c')]
True

>>> t = m.copy()
>>> t.update_from_block_items([((the0, the3), 'c'), ((the2, the4), 'c')])
>>> t.get_num_block_keys()
1
>>> [*t.iter_block_items()] == [((the0, the5), 'c')]
True

>>> t = m.copy()
>>> t.update_from_items((k, 'c') for k in range(5))
>>> t.get_num_block_keys()
1
>>> [*t.iter_block_items()] == [((the0, the5), 'c')]
True

__bool__
>>> bool(empty)
False
>>> bool(m)
True

__contains__
>>> 2 in empty
False
>>> 2 in m
False
>>> 1 in m
True

__delitem__
>>> t = m.copy()
>>> del t[1]
>>> t.get_num_block_keys()
3
>>> del t[3]
>>> t.get_num_block_keys()
3
>>> del t[4]
>>> t.get_num_block_keys()
2
>>> del t[5]
>>> t.get_num_block_keys()
1
>>> del t[0]
>>> t.get_num_block_keys()
0
>>> t == empty
True


__eq__
>>> empty == m
False
>>> empty == empty
True
>>> m == m
True
>>> m == m.copy()
True

__getitem__
>>> m[1]
'a'

__ne__
>>> m != empty
True
>>> m != m
False
>>> m != m.copy()
False

__repr__
>>> empty # doctest: +ELLIPSIS
BlockDict(<...>, None)
>>> m # doctest: +ELLIPSIS
BlockDict(<...>, None, [(((<KeyExCase.TheKey: 2>, 0), (<KeyExCase.TheKey: 2>, 0)), 'k'), (((<KeyExCase.TheKey: 2>, 1), (<KeyExCase.TheKey: 2>, 1)), 'a'), (((<KeyExCase.TheKey: 2>, 3), (<KeyExCase.TheKey: 2>, 4)), 'b'), (((<KeyExCase.TheKey: 2>, 5), (<KeyExCase.TheKey: 2>, 5)), 'c')], is_block_items = True)

__setitem__
>>> t = m.copy()
>>> 2 in t
False
>>> t[2] = 'b'
>>> 2 in t
True
>>> t.get_num_block_keys()
4
>>> t[2]
'b'
>>> t[2] = 'x'
>>> t.get_num_block_keys()
5
>>> t[2]
'x'


swap
>>> t = m.copy()
>>> e = empty.copy()
>>> t.swap(e)
>>> t == empty != e == m
True

assign
>>> e = empty.copy()
>>> e.assign(m)
>>> e == m
True



self_make_empty_block_dict
self_make_block_dict_from_items
self_make_block_dict_from_block_items
>>> m.self_make_empty_block_dict() == empty
True
>>> m.self_make_block_dict_from_items([]) == empty
True
>>> m.self_make_block_dict_from_block_items([]) == empty
True
>>> m.self_make_block_dict_from_items([(1,'a'), (0, 'k'), (3, 'b'), (5, 'c'), (4, 'b')]) == m
True
>>> m.self_make_block_dict_from_block_items(m.iter_block_items()) == m
True

set_dict_key2default
>>> t = m.copy()
>>> t.set_dict_key2default(1, ...)
'a'
>>> t[1]
'a'
>>> t.set_dict_key2default(2, lambda k: 'A'+str(k))
'A2'
>>> t[2]
'A2'

>>> m.list_all_touch_or_overlap_block_items((the1, the4), False) == [*m.iter_block_items()]
True
>>> m.list_all_touch_or_overlap_block_items((the1, the3), False) == [*m.iter_block_items()][:-1]
True
>>> m.list_all_touch_or_overlap_block_items((the2, the4), False) == [*m.iter_block_items()][1:]
True

>>> m.list_all_touch_or_overlap_block_items((the1, the4), False, reverse=True) == [*m.iter_block_items()][::-1]
True
>>> m.list_all_touch_or_overlap_block_items((the1, the3), False, reverse=True) == [*m.iter_block_items()][-2::-1]
True
>>> m.list_all_touch_or_overlap_block_items((the2, the4), False, reverse=True) == [*m.iter_block_items()][:0:-1]
True


>>> m.list_all_touch_or_overlap_block_items((the1, the4), True) == [*m.iter_block_items()][1:-1]
True
>>> m.list_all_touch_or_overlap_block_items((the1, the3), True) == [*m.iter_block_items()][1:-1]
True
>>> m.list_all_touch_or_overlap_block_items((the2, the4), True) == [*m.iter_block_items()][2:-1]
True


>>> m.list_all_touch_or_overlap_block_items((the4, the1), False)
[]
>>> m.list_all_touch_or_overlap_block_items((the1, the4), True) == [*m.iter_all_touch_or_overlap_block_items((the1, the4), True)]
True
>>> m.list_all_touch_or_overlap_block_items((the1, the4), False) == [*m.iter_all_touch_or_overlap_block_items((the1, the4), False)]
True


>>> m.list_all_touch_or_overlap_block_items((the0, the0), True) == [((the0, the0), 'k')]
True
>>> m.block_dict_key_ops.eqRange((the0, the0), (the0, the0))
True


is_one_piece_block_key
is_exactly_block_key
>>> m == UIntBlockDict([(1, 'a'), (3, 'b'), (4, 'b'), (5, 'c'), (0, 'k')])
True
>>> m.is_exactly_block_key((the0, the1))
False
>>> m.is_exactly_block_key((the0, the0))
True
>>> m.is_exactly_block_key((the3, the3))
False
>>> m.is_exactly_block_key((the3, the4))
True
>>> m.is_exactly_block_key((the3, the5))
False
>>> m.is_exactly_block_key((the2, the4))
False
>>> m.is_exactly_block_key((the2, the2))
False
>>> m.is_exactly_block_key((the2, the1))
False

>>> m.is_one_piece_block_key((the0, the1))
False
>>> m.is_one_piece_block_key((the0, the0))
True
>>> m.is_one_piece_block_key((the3, the3))
True
>>> m.is_one_piece_block_key((the3, the4))
True
>>> m.is_one_piece_block_key((the3, the5))
False
>>> m.is_one_piece_block_key((the2, the4))
False
>>> m.is_one_piece_block_key((the2, the2))
False
>>> m.is_one_piece_block_key((the2, the1))
False



'''

__all__ = '''
    BlockDict
    '''.split()


from .abc import override
from ..BlockDictOps.IBlockDictKeyOps import IBlockDictKeyOps, KeyExCase
from ..BlockDictOps__concrete.BlockDictOps__for_KeyOrderedRedBlackTreeNodeOps__sized_immutable import \
    BlockDictOps__for_KeyOrderedRedBlackTreeNodeOps__sized_immutable
from ..BlockDict.IBlockDict import IBlockDict

from ..OtherOps.IEqOps import IEqOps
from ..OtherOps.ITotalOrderingOps import ITotalOrderingOps
from ..OtherOps.TotalOrderingOps import TotalOrderingOps, python_total_key_ops
from ..OtherOps.EqOps import EqOps, python_eq_key_ops

from ..RedBlackTreeNodeOps__concrete.KeyOrderedRedBlackTreeNodeOps__sized_immutable import \
    KeyOrderedRedBlackTreeNodeOps__sized_immutable
from ..KeyOrderedTreeNodeOps.IKeyOrderedRedBlackTreeNodeOps__imodify import \
    IKeyOrderedRedBlackTreeNodeOps__imodify

#from collections.abc import MutableMapping
import operator
from seed.helper.repr_input import repr_helper
from seed.tiny import fst, snd



# global_item2tree_key :: ((left_bound, right_bound), dict_value) -> left_bound
global_item2tree_key = lambda e: e[0][0]
#Node__global = KeyOrderedRedBlackTreeNodeOps__sized_immutable(None, None)
neg_inf = float('-inf')

class BlockDict(IBlockDict):
    '''
not (MutableMapping):
    since no __len__/__iter__
        # hence no keys/items/values/popitem

dict_key :: ITotalOrderingOps
    # to using KeyOrderedTree
dict_value :: IEqOps
    # to merge two touch/overlap blocks with same dict_value

dict_key = basic_key = key :: Key in IBlockDictKeyOps
    # BlockDict implement details:
    # tree_key = lkey_ex = left_key_ex = left_bound :: KeyEx in IBlockDictKeyOps

item = (dict_key, dict_value)

block_key = (lkey_ex, rkey_ex) = range :: Range
block_item = (block_key, dict_value) = entity




example:
    >>> This = BlockDict

    >>> from ..BlockDictOps__concrete.theUInt_as_BlockDictKeyOps import theUInt_as_BlockDictKeyOps
    >>> UIntBlockDict = lambda *args, **kwargs: This(theUInt_as_BlockDictKeyOps, None, *args, **kwargs)
    >>> block_dict_key_ops = theUInt_as_BlockDictKeyOps

    >>> m = UIntBlockDict()
    >>> m # doctest: +ELLIPSIS
    BlockDict(<...>, None)
    >>> bool(m)
    False

    >>> m[1] = 'a'
    >>> bool(m)
    True
    >>> m.get_num_block_keys()
    1
    >>> m # doctest: +ELLIPSIS
    BlockDict(<...>, None, [(((<KeyExCase.TheKey: ...>, 1), (<KeyExCase.TheKey: ...>, 1)), 'a')], is_block_items = True)



    # dict_key
    >>> m[3] = 'c'
    >>> m.get_num_block_keys()
    2
    >>> m[2] = 'b'
    >>> m.get_num_block_keys()
    3
    >>> list(m.iter_dict_values())
    ['a', 'b', 'c']
    >>> list(m.iter_dict_values(reverse=True))
    ['c', 'b', 'a']

    >>> m[3] = 'a'
    >>> m.get_num_block_keys()
    3
    >>> m[2] = 'a'
    >>> m.get_num_block_keys()
    1
    >>> m[2] = 'b'
    >>> m.get_num_block_keys()
    3
    >>> m[3] = 'b'
    >>> m.get_num_block_keys()
    2
    >>> m[1] = 'b'
    >>> m.get_num_block_keys()
    1
    >>> del m[2]
    >>> m.get_num_block_keys()
    2


    # m = {1:'b', 3:'b'}
    # set_block_item
    >>> the0 = block_dict_key_ops.mkTheKey(0)
    >>> the1 = block_dict_key_ops.mkTheKey(1)
    >>> the2 = block_dict_key_ops.mkTheKey(2)
    >>> the3 = block_dict_key_ops.mkTheKey(3)
    >>> the4 = block_dict_key_ops.mkTheKey(4)
    >>> the5 = block_dict_key_ops.mkTheKey(5)
    >>> the6 = block_dict_key_ops.mkTheKey(6)
    >>> the7 = block_dict_key_ops.mkTheKey(7)

    >>> rng = (the2, the7) # [2,7] # [2..7]
    >>> m.set_block_item(rng, 'c')
    >>> m.get_num_block_keys()
    2
    >>> m # doctest: +ELLIPSIS
    BlockDict(<...>, None, [(((<...TheKey...>, 1), (<...TheKey...>, 1)), 'b'), (((<...TheKey...>, 2), (<...TheKey...>, 7)), 'c')], is_block_items = True)


    >>> m.set_block_item((the2,the4), 'b')
    >>> m.get_num_block_keys()
    2
    >>> m # doctest: +ELLIPSIS
    BlockDict(<...>, None, [(((<...TheKey...>, 1), (<...TheKey...>, 4)), 'b'), (((<...TheKey...>, 5), (<...TheKey...>, 7)), 'c')], is_block_items = True)

    >>> m.set_block_item((the4,the5), 'a')
    >>> m.get_num_block_keys()
    3
    >>> m # doctest: +ELLIPSIS
    BlockDict(<...>, None, [(((<...TheKey...>, 1), (<...TheKey...>, 3)), 'b'), (((<...TheKey...>, 4), (<...TheKey...>, 5)), 'a'), (((<...TheKey...>, 6), (<...TheKey...>, 7)), 'c')], is_block_items = True)


    >>> m.set_block_item((the3,the5), 'c')
    >>> m.get_num_block_keys()
    2
    >>> m # doctest: +ELLIPSIS
    BlockDict(<...>, None, [(((<...TheKey...>, 1), (<...TheKey...>, 2)), 'b'), (((<...TheKey...>, 3), (<...TheKey...>, 7)), 'c')], is_block_items = True)


    # m = {(1,2):'b', (3,7):'c'}
    >>> m.set_block_item((the7,the7), 'c')
    >>> m.get_num_block_keys()
    2
    >>> m.set_block_item((the7,the7), 'b')
    >>> m.get_num_block_keys()
    3
    >>> m.set_block_item((the2,the6), 'b')
    >>> m.get_num_block_keys()
    1
    >>> m # doctest: +ELLIPSIS
    BlockDict(<...>, None, [(((<...TheKey...>, 1), (<...TheKey...>, 7)), 'b')], is_block_items = True)


    # m = {(1,7):'b'}
    >>> del m[2]
    >>> m.get_num_block_keys()
    2
    >>> del m[6]
    >>> m.get_num_block_keys()
    3
    >>> del m[4]
    >>> m.get_num_block_keys()
    4


    # m = {(1,1):'b', (3,3):'b', (5,5):'b', (7,7):'b'}
    >>> [*ls] = m.block_key2iter_block_items((the2, the5))
    >>> len(ls)
    2
    >>> ls # doctest: +ELLIPSIS
    [(((..., 3), (..., 3)), 'b'), (((..., 5), (..., 5)), 'b')]

    # block_key2iter_block_items
    >>> [*ls] = m.block_key2iter_block_items((the2, the5), reverse=True)
    >>> len(ls)
    2
    >>> ls # doctest: +ELLIPSIS
    [(((..., 5), (..., 5)), 'b'), (((..., 3), (..., 3)), 'b')]

    # pop_block_items_of_block_key
    >>> ls = m.pop_block_items_of_block_key((the2, the5), reverse=True)
    >>> ls # doctest: +ELLIPSIS
    [(((..., 5), (..., 5)), 'b'), (((..., 3), (..., 3)), 'b')]

    >>> m.get_num_block_keys()
    2
    >>> m # doctest: +ELLIPSIS
    BlockDict(<...>, None, [(((..., 1), (..., 1)), 'b'), (((..., 7), (..., 7)), 'b')], is_block_items = True)


'''
    __slots__ = '''
        _BlockDict__tree
        _BlockDict__ops
        '''.split()

    def __init__(self
            , block_dict_key_ops
            , eq_dict_value_ops # =None
            , iterable=None, *
            , is_block_items=False
            #, is_sorted=False
            #, reverse=False
            ):
        '''
input:
    block_dict_key_ops :: IBlockDictKeyOps<dict_key>
        # about dict_key instead of tree_key
    iterable :: None | IBlockDict | Iter item | Iter block_item
        if is_block_items:
            iterable :: None | IBlockDict | Iter block_item
        else:
            iterable :: None | IBlockDict | Iter item

    # no: dict_key2tree_key :: None | (dict_key -> tree_key)
    eq_dict_value_ops :: None | IEqOps<dict_value>
        default = python_eq_key_ops
    is_block_items :: bool = False
        affect how to treat the input iterable

    is_sorted :: bool = False
        if iterable is items:
            let (<=) = block_dict_key_ops.total_key_ops.le
            item_a before item_b ==>> dict_key_a <= dict_key_b
        elif iterable is block_items:
            let (<=) = block_dict_key_ops.leRange
            block_item_a before block_item_b ==>> block_key_a <= block_key_b
    reverse :: bool = False
        if is_sorted=True:
            iterable is reversed sorted
'''
        if not isinstance(block_dict_key_ops, IBlockDictKeyOps): raise TypeError
        if eq_dict_value_ops is None:
            eq_dict_value_ops = python_eq_key_ops
        elif not isinstance(eq_dict_value_ops, IEqOps): raise TypeError
        ops = BlockDictOps__for_KeyOrderedRedBlackTreeNodeOps__sized_immutable(block_dict_key_ops, eq_dict_value_ops)


        self.__ops = ops
        self.__tree = ops.make_empty_block_dict()

        if iterable is None:
            iterable = ()
        elif isinstance(iterable, IBlockDict):
            other = iterable
            if isinstance(other, __class__):
                self.__tree = ops.copy_block_dict(other.__tree)
                return

            if other.block_dict_key_ops != ops.block_dict_key_ops: raise TypeError
            if other.eq_dict_value_ops != ops.eq_dict_value_ops: raise TypeError

            iterable = other.iter_block_items()
            is_block_items = True
            is_sorted = True
            reverse = False


        #self.__tree = ???

        if False and is_sorted:
            '''
            if is_block_items:
            else:
            TODO

            self.__tree = tree
            '''
        else:
            if is_block_items:
                # unordered block_items
                self.update_from_block_items(iterable)
            else:
                # unordered items
                self.update_from_items(iterable)

        return

    @override
    def swap(self, other):
        if type(other) is not type(self): return TypeError
        if other.block_dict_key_ops != self.block_dict_key_ops: raise TypeError
        if other.eq_dict_value_ops != self.eq_dict_value_ops: raise TypeError
        other.__tree, self.__tree = self.__tree, other.__tree
    '''
    def assign(self, other):
        other = other.copy()
        self.swap(other)
    '''

    def __repr__(self):
        block_dict_key_ops = self.block_dict_key_ops
        eq_dict_value_ops = self.eq_dict_value_ops
        if eq_dict_value_ops == python_eq_key_ops:
            eq_dict_value_ops = None

        kwargs = {}
        if self:
            kwargs['is_block_items'] = True
            args = ([*self.iter_block_items()],)
        else:
            args = ()
        return repr_helper(self, block_dict_key_ops, eq_dict_value_ops
                        , *args, **kwargs)

    @override
    def self_make_empty_block_dict(self):
        return type(self).make_empty_block_dict(
                self.block_dict_key_ops
                , self.eq_dict_value_ops)
    @classmethod
    def make_empty_block_dict(cls, block_dict_key_ops, eq_dict_value_ops):
        # eq_dict_value_ops may be None
        return cls(block_dict_key_ops, eq_dict_value_ops)
    def copy(self):
        other = self.self_make_empty_block_dict()
        other.__tree = self.block_dict_ops.copy_block_dict(self.__tree)
        return other

    @property
    def block_dict_ops(self):
        return self.__ops


    @override
    def _get_block_dict_key_ops_(self):
        # -> IBlockDictKeyOps<dict_key, KeyEx<dict_key> >
        #
        # dict_key vs tree_key
        #   dict_key = basic_key = key in IBlockDictKeyOps
        #   tree_key = lkey_ex = left_key_ex = left_bound
        #       is key_ex in IBlockDictKeyOps
        return self.block_dict_ops.block_dict_key_ops
    @override
    def _get_eq_dict_value_ops_(self):
        # -> IEqOps<dict_value>
        return self.block_dict_ops.eq_dict_value_ops

    @override
    def get_num_block_keys(self):
        # no __len__
        return self.block_dict_ops.get_num_block_keys(self.__tree)
        return self.Node.get_num_entities_of_subtree(self.__tree)
    @override
    def iter_block_items(self, *, reverse=False):
        # no items
        return self.block_dict_ops.iter_block_items(self.__tree, reverse=reverse)
        return self.Node.iter_entities_of_subtree(self.__tree, reverse=reverse)
    @override
    def pop_left_or_right_block_item(self, right:bool):
        old_entity, new_tree = self.block_dict_ops.ipop_left_or_right_block_item(self.__tree, right)
        self.__tree = new_tree
        return old_entity

    @override
    def clear(self):
        self.__tree = self.block_dict_ops.iclear(self.__tree)
        return
        self.__tree = self.Node.make_root_leaf()


    @override
    def iter_all_touch_or_overlap_block_items(self, block_key
            , overlap_only:bool
                # False ==>> touch_or_overlap
                # True ==>> overlap_only
            , *, reverse=False):
        return self.block_dict_ops.iter_all_touch_or_overlap_block_items(
                self.__tree, block_key, overlap_only, reverse=reverse)

    @override
    def set_block_item(self, block_key, dict_value):
        # if block_key overlap or touch input_block_key
        #   and block_dict_value_eq(self[block_key], dict_value):
        #   then merge the two ranges/block_keys
        self.__tree = self.block_dict_ops.iset_block_item(self.__tree, block_key, dict_value)
    '''
    @override
    def block_key2iter_block_items(self, block_key, *, reverse=False):
        # -> Iter (block_key, dict_value)
        # all block_key result inside input_block_key
        return self.block_dict_ops.block_key2iter_block_items(
                    self.__tree, block_key, reverse=reverse)
    '''

    @override
    def discard_block_items_of_block_key(self, block_key):
        #self.pop_block_items_of_block_key(block_key)
        new_tree = self.block_dict_ops.idiscard_block_items_of_block_key(
                    self.__tree, block_key)
        self.__tree = new_tree
        return

    @override
    def pop_block_items_of_block_key(self, block_key, *, reverse=False):
        # -> [block_item]
        #   not Iter block_item
        block_items, new_tree = \
            self.block_dict_ops.ipop_block_items_of_block_key(
                    self.__tree, block_key, reverse=reverse)
        self.__tree = new_tree
        return block_items



if __name__ == "__main__":
    XXX = BlockDict

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
