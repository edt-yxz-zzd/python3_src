
r'''
example:
>>> This = BlockDict

mkBlockDict :: block_dict_key_ops -> (Iter a = None) -> (is_block_items=False) -> BlockDict
>>> mkBlockDict = lambda block_dict_key_ops, iterable=None, *args, is_block_items=False, **kwargs: This(block_dict_key_ops, None, iterable, *args, is_block_items=is_block_items, **kwargs)

>>> from ..OtherOps.TotalOrderingOps import python_total_key_ops
>>> from ..OtherOps.EqOps import python_eq_key_ops
>>> from ..BlockDictOps__concrete.theUInt_as_BlockDictKeyOps import theUInt_as_BlockDictKeyOps
>>> block_dict_key_ops = theUInt_as_BlockDictKeyOps
>>> UIntBlockDict = lambda *args, **kwargs: mkBlockDict(theUInt_as_BlockDictKeyOps, *args, **kwargs)

>>> t = This.make_empty_block_dict(block_dict_key_ops, python_total_key_ops)
>>> t.block_dict_key_ops is block_dict_key_ops
True
>>> t.eq_dict_value_ops is python_total_key_ops
True


__repr__

>>> m = UIntBlockDict([(1, 'a')])
>>> m # doctest: +ELLIPSIS
BlockDict(<...>, None, [(((<KeyExCase.TheKey: ...>, 1), (<KeyExCase.TheKey: ...>, 1)), 'a')], is_block_items = True)

>>> m = UIntBlockDict([(1, 'b'), (3, 'b')])
>>> m # doctest: +ELLIPSIS
BlockDict(<...>, None, [(((<...TheKey...>, 1), (<...TheKey...>, 1)), 'b'), (((<...TheKey...>, 3), (<...TheKey...>, 3)), 'b')], is_block_items = True)

>>> empty = UIntBlockDict()
>>> empty # doctest: +ELLIPSIS
BlockDict(<...>, None)

>>> m = UIntBlockDict([(1, 'a'), (3, 'b'), (4, 'b'), (5, 'c'), (0, 'k')])
>>> m # doctest: +ELLIPSIS
BlockDict(<...>, None, [(((<KeyExCase.TheKey: 2>, 0), (<KeyExCase.TheKey: 2>, 0)), 'k'), (((<KeyExCase.TheKey: 2>, 1), (<KeyExCase.TheKey: 2>, 1)), 'a'), (((<KeyExCase.TheKey: 2>, 3), (<KeyExCase.TheKey: 2>, 4)), 'b'), (((<KeyExCase.TheKey: 2>, 5), (<KeyExCase.TheKey: 2>, 5)), 'c')], is_block_items = True)
'''
from .example_BlockDict__mutable import example_BlockDict
__doc__ += example_BlockDict



__all__ = '''
    BlockDict
    '''.split()


from .abc import override
from ..BlockDictOps.IBlockDictKeyOps import IBlockDictKeyOps, KeyExCase
from ..BlockDictOps__concrete.BlockDictOps__for_KeyOrderedRedBlackTreeNodeOps__sized_immutable import \
    BlockDictOps__for_KeyOrderedRedBlackTreeNodeOps__sized_immutable
from ..BlockDict.IBlockDict import IBlockDict
from ..BlockDict.IBlockDict_by_BlockDictOps__imodify import \
    IBlockDict_by_BlockDictOps__imodify

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

class BlockDict(IBlockDict_by_BlockDictOps__imodify):
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
    # no: dict_key2tree_key :: None | (dict_key -> tree_key)
    eq_dict_value_ops :: None | IEqOps<dict_value>
        default = python_eq_key_ops

    iterable :: None | IBlockDict | Iter item | Iter block_item
        if is_block_items:
            iterable :: None | IBlockDict | Iter block_item
        else:
            iterable :: None | IBlockDict | Iter item
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
    def _get_block_dict_ops_(self):
        return self.__ops
    @override
    def _get_data_for_block_dict_ops_(self):
        return self.__tree
    @override
    def _set_data_for_block_dict_ops_(self, data):
        self.__tree = data



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
    @classmethod
    def make_empty_block_dict(cls, block_dict_key_ops, eq_dict_value_ops):
        # eq_dict_value_ops may be None
        return cls(block_dict_key_ops, eq_dict_value_ops)

    @override
    def self_make_empty_block_dict(self):
        return type(self).make_empty_block_dict(
                self.block_dict_key_ops
                , self.eq_dict_value_ops)

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
