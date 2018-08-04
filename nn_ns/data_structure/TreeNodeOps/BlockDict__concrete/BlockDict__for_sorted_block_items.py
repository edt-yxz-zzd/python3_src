
r'''
example:
>>> This = BlockDict__for_sorted_block_items

mkBlockDict :: block_dict_key_ops -> (Iter a = None) -> (is_block_items=False) -> BlockDict
>>> mkBlockDict = lambda block_dict_key_ops, iterable=None, *args, is_block_items=False, **kwargs: This(block_dict_key_ops, None, None, iterable, *args, is_block_items=is_block_items, **kwargs)

>>> from ..OtherOps.TotalOrderingOps import python_total_key_ops
>>> from ..OtherOps.EqOps import python_eq_key_ops
>>> from ..BlockDictOps__concrete.theUInt_as_BlockDictKeyOps import theUInt_as_BlockDictKeyOps
>>> block_dict_key_ops = theUInt_as_BlockDictKeyOps
>>> UIntBlockDict = lambda *args, **kwargs: mkBlockDict(theUInt_as_BlockDictKeyOps, *args, **kwargs)

>>> def _block_items2seq(block_items): return list(block_items)
>>> t = This.make_empty_block_dict(block_dict_key_ops, python_total_key_ops, _block_items2seq)
>>> t.block_dict_key_ops is block_dict_key_ops
True
>>> t.eq_dict_value_ops is python_total_key_ops
True
>>> t.block_items2seq is _block_items2seq
True

__repr__

>>> m = UIntBlockDict([(1, 'a')])
>>> m # doctest: +ELLIPSIS
BlockDict__for_sorted_block_items(<...>, None, None, [(((<KeyExCase.TheKey: ...>, 1), (<KeyExCase.TheKey: ...>, 1)), 'a')], is_block_items = True)

>>> m = UIntBlockDict([(1, 'b'), (3, 'b')])
>>> m # doctest: +ELLIPSIS
BlockDict__for_sorted_block_items(<...>, None, None, [(((<...TheKey...>, 1), (<...TheKey...>, 1)), 'b'), (((<...TheKey...>, 3), (<...TheKey...>, 3)), 'b')], is_block_items = True)

>>> empty = UIntBlockDict()
>>> empty # doctest: +ELLIPSIS
BlockDict__for_sorted_block_items(<...>, None, None)

>>> m = UIntBlockDict([(1, 'a'), (3, 'b'), (4, 'b'), (5, 'c'), (0, 'k')])
>>> m # doctest: +ELLIPSIS
BlockDict__for_sorted_block_items(<...>, None, None, [(((<KeyExCase.TheKey: 2>, 0), (<KeyExCase.TheKey: 2>, 0)), 'k'), (((<KeyExCase.TheKey: 2>, 1), (<KeyExCase.TheKey: 2>, 1)), 'a'), (((<KeyExCase.TheKey: 2>, 3), (<KeyExCase.TheKey: 2>, 4)), 'b'), (((<KeyExCase.TheKey: 2>, 5), (<KeyExCase.TheKey: 2>, 5)), 'c')], is_block_items = True)
'''
from .example_BlockDict import example_BlockDict
__doc__ += example_BlockDict



__all__ = '''
    BlockDict__for_sorted_block_items
    '''.split()


from .abc import override
from ..BlockDictOps.IBlockDictKeyOps import IBlockDictKeyOps, KeyExCase
from ..BlockDictOps__concrete.BlockDictOps__for_sorted_block_items import \
    BlockDictOps__for_sorted_block_items
from ..BlockDict.IBlockDict import IBlockDict
from ..BlockDict.IBlockDict_by_BlockDictOps import IBlockDict_by_BlockDictOps

from ..OtherOps.IEqOps import IEqOps
from ..OtherOps.ITotalOrderingOps import ITotalOrderingOps
from ..OtherOps.TotalOrderingOps import TotalOrderingOps, python_total_key_ops
from ..OtherOps.EqOps import EqOps, python_eq_key_ops


#from collections.abc import MutableMapping
import operator
from seed.helper.repr_input import repr_helper
from seed.tiny import fst, snd



class BlockDict__for_sorted_block_items(IBlockDict_by_BlockDictOps):
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


all_methods:
        __bool__
        __contains__
        __eq__
        __getitem__
        __hash__
        __ne__
        __repr__

        block_dict_key_ops
        block_dict_ops
        block_items2seq
        block_key2block_items
        block_key2iter_block_items
        copy
        dict_key2block_items
        dict_value_eq
        eq_dict_value_ops
        get
        get_block_dict_key_ops
        get_block_dict_ops
        get_eq_dict_value_ops
        get_num_block_keys
        get_total_dict_key_ops
        is_exactly_block_key
        is_one_piece_block_key
        iter_all_touch_or_overlap_block_items
        iter_block_items
        iter_block_keys
        iter_dict_values
        list_all_touch_or_overlap_block_items
        make_empty_block_dict
        mkSingletonRange
        self_make_block_dict_from_block_items
        self_make_block_dict_from_items
        self_make_block_dict_from_iterable
        self_make_empty_block_dict
        total_dict_key_ops
'''
    __slots__ = '''
        _seq
        _ops
        '''.split()

    def __init__(self
            , block_dict_key_ops
            , eq_dict_value_ops # =None
            , block_items2seq # =tuple
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
    block_items2seq :: None | (Iter block_item -> Seq block_item)
        default = tuple
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
        ops = BlockDictOps__for_sorted_block_items(
                block_dict_key_ops, eq_dict_value_ops, block_items2seq)


        self._ops = ops
        #self._seq = ops.make_empty_block_dict()

        if iterable is None:
            iterable = ()
        elif isinstance(iterable, IBlockDict):
            other = iterable
            if isinstance(other, __class__):
                self._seq = ops.copy_block_dict(other._seq)
                return

            if other.block_dict_key_ops != ops.block_dict_key_ops: raise TypeError
            if other.eq_dict_value_ops != ops.eq_dict_value_ops: raise TypeError

            iterable = other.iter_block_items()
            is_block_items = True
            is_sorted = True
            reverse = False


        self._seq = ops.make_block_dict_from_iterable(iterable, is_block_items)
        return


    @override
    def _get_block_dict_ops_(self):
        return self._ops
    @override
    def _get_data_for_block_dict_ops_(self):
        return self._seq
    @override
    def _set_data_for_block_dict_ops_(self, data):
        self._seq = data


    @property
    def block_items2seq(self):
        return self.block_dict_ops.block_items2seq

    def __repr__(self):
        block_dict_key_ops = self.block_dict_key_ops
        eq_dict_value_ops = self.eq_dict_value_ops
        block_items2seq = self.block_items2seq
        if eq_dict_value_ops == python_eq_key_ops:
            eq_dict_value_ops = None
        if block_items2seq is tuple:
            block_items2seq = None

        kwargs = {}
        if self:
            kwargs['is_block_items'] = True
            args = ([*self.iter_block_items()],)
        else:
            args = ()
        return repr_helper(self
                        , block_dict_key_ops
                        , eq_dict_value_ops
                        , block_items2seq
                        , *args, **kwargs)
    @classmethod
    def make_empty_block_dict(cls
            , block_dict_key_ops, eq_dict_value_ops, block_items2seq):
        # eq_dict_value_ops may be None
        return cls(block_dict_key_ops, eq_dict_value_ops, block_items2seq)

    @override
    def self_make_empty_block_dict(self):
        return type(self).make_empty_block_dict(
                self.block_dict_key_ops
                , self.eq_dict_value_ops
                , self.block_items2seq)


    def copy(self):
        other = self.self_make_empty_block_dict()
        other._seq = self.block_dict_ops.copy_block_dict(self._seq)
        return other

    def self_make_block_dict_from_block_items(self, block_items):
        other = self.self_make_empty_block_dict()
        other._seq = self.block_dict_ops.make_block_dict_from_block_items(block_items)
        return other
    def self_make_block_dict_from_items(self, items):
        other = self.self_make_empty_block_dict()
        other._seq = self.block_dict_ops.make_block_dict_from_items(items)
        return other


def _t():
    This = BlockDict__for_sorted_block_items
    from ..BlockDictOps__concrete.theUInt_as_BlockDictKeyOps import theUInt_as_BlockDictKeyOps
    UIntBlockDict = lambda *args, **kwargs: This(theUInt_as_BlockDictKeyOps, None, None, *args, **kwargs)
    block_dict_key_ops = theUInt_as_BlockDictKeyOps


    the2 = block_dict_key_ops.mkTheKey(2)
    the3 = block_dict_key_ops.mkTheKey(3)
    t = UIntBlockDict([(1, 'a'), (3, 'b'), (4, 'b'), (5, 'c'), (0, 'k'), (2, 'a'), (3, 'a')])
if __name__ == "__main__":
    _t()

if __name__ == "__main__":
    XXX = BlockDict__for_sorted_block_items

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

