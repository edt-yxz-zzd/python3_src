
__all__ = '''
    BlockDictOps__for_sorted_block_items
    uint_block_dict_ops__for_sorted_block_items
    int_block_dict_ops__for_sorted_block_items
    fraction_block_dict_ops__for_sorted_block_items
    '''.split()

from .abc import override
from ..OtherOps.IEqOps import IEqOps
from ..OtherOps.ITotalOrderingOps import ITotalOrderingOps
from ..BlockDictOps.IBlockDictKeyOps import IBlockDictKeyOps, KeyExCase
from ..OtherOps.EqOps import EqOps, python_eq_key_ops


from ..BlockDictOps.IBlockDictOps__position import IBlockDictOps__position
from ..BlockDictOps.IBlockDictOps__constructor import IBlockDictOps__constructor
from .theUInt_as_BlockDictKeyOps import theUInt_as_BlockDictKeyOps
from .theInt_as_BlockDictKeyOps import theInt_as_BlockDictKeyOps
from .theFraction_as_BlockDictKeyOps import theFraction_as_BlockDictKeyOps
from .merge_and_iter_sorted_block_items import merge_and_iter_sorted_block_items



#from collections.abc import MutableMapping
import operator
from seed.helper.repr_input import repr_helper
#from seed.tiny import fst, snd
from seed.seq_tools.bisearch import bisearch


# global_item2tree_key :: ((left_bound, right_bound), dict_value) -> left_bound
global_item2tree_key = lambda e: e[0][0]


class BlockDictOps__for_sorted_block_items(
        IBlockDictOps__constructor
        , IBlockDictOps__position):
    '''

self                    :: sorted (Seq (range, dict_value))
                                with key = global_item2tree_key
left_bound              as key_for_sort
index                   as position
(block_key, dict_value) as seq_entity

testing:
    see: BlockDict__for_sorted_block_items
'''
    __slots__ = '''
        _block_dict_key_ops
        _eq_dict_value_ops
        _block_items2seq
        '''.split()

    def __init__(ops, block_dict_key_ops, eq_dict_value_ops, block_items2seq):
        '''
input:
    block_dict_key_ops :: IBlockDictKeyOps<dict_key>
        # about dict_key instead of tree_key

    # no: dict_key2tree_key :: None | (dict_key -> tree_key)
    eq_dict_value_ops :: None | IEqOps<dict_value>
        default = python_eq_key_ops
    block_items2seq :: None | (Iter block_item -> Seq block_item)
        default = tuple
        must be hashable
'''
        if not isinstance(block_dict_key_ops, IBlockDictKeyOps): raise TypeError
        if eq_dict_value_ops is None:
            eq_dict_value_ops = python_eq_key_ops
        elif not isinstance(eq_dict_value_ops, IEqOps): raise TypeError

        if block_items2seq is None:
            block_items2seq = tuple
        elif not callable(block_items2seq): raise TypeError
        hash(block_items2seq) # test hashable


        total_left_bound_ops = block_dict_key_ops.make_total_left_bound_ops()
        assert isinstance(total_left_bound_ops, ITotalOrderingOps)

        # left_bound = tree_key

        ops._block_dict_key_ops = block_dict_key_ops
        ops._eq_dict_value_ops = eq_dict_value_ops
        ops._block_items2seq = block_items2seq
        return


    def __repr__(ops):
        block_dict_key_ops = ops.block_dict_key_ops
        eq_dict_value_ops = ops.eq_dict_value_ops
        block_items2seq = ops.block_items2seq

        if eq_dict_value_ops == python_eq_key_ops:
            eq_dict_value_ops = None
        if block_items2seq == tuple:
            block_items2seq = None

        return repr_helper(ops, block_dict_key_ops, eq_dict_value_ops, block_items2seq)

    @override
    def copy_block_dict(ops, self):
        #bug:tuple has no copy:
        #   return self.copy()
        return self[:] # tuple[:] do not really copy the underlying data



    def merge_and_iter_sorted_block_items(ops, iterable, is_block_items:bool):
        return merge_and_iter_sorted_block_items(
                    ops.block_dict_key_ops
                    , ops.eq_dict_value_ops
                    , iterable
                    , is_block_items)

    @property
    def block_items2seq(ops):
        return ops._block_items2seq

    @override
    def make_empty_block_dict(ops):
        return ops.block_items2seq(())
    @override
    def make_block_dict_from_block_items(ops, block_items):
        it = ops.merge_and_iter_sorted_block_items(block_items, True)
        return ops.block_items2seq(it)
    @override
    def make_block_dict_from_items(ops, items):
        it = ops.merge_and_iter_sorted_block_items(items, False)
        return ops.block_items2seq(it)








    @override
    def get_args_for_eq_hash(ops):
        return (ops.block_dict_key_ops, ops.eq_dict_value_ops, ops.block_items2seq)



    @override
    def _get_block_dict_key_ops_(ops):
        # -> IBlockDictKeyOps<dict_key, KeyEx<dict_key> >
        #
        # dict_key vs tree_key
        #   dict_key = basic_key = key in IBlockDictKeyOps
        #   tree_key = lkey_ex = left_key_ex = left_bound
        #       is key_ex in IBlockDictKeyOps
        return ops._block_dict_key_ops
    @override
    def _get_eq_dict_value_ops_(ops):
        # -> IEqOps<dict_value>
        return ops._eq_dict_value_ops

    @override
    def get_num_block_keys(ops, self):
        # no __len__
        return len(self)
    @override
    def iter_block_items(ops, self, *, reverse=False):
        # no items
        return iter(self) if not reverse else reversed(self)

    @override
    def _index_block_item_at_(ops, self, i:'UInt'):
        return self[i]





    @override
    def get_the_begin_or_end_position(ops, self, end:bool):
        return 0 if not end else len(self)
    @override
    def _left_bound2begin_(ops, self, left_bound):
        # -> position
        # if begin not the begin position of whole:
        #   then left_bound may be inside the range at prev(begin)
        #
        # index as position
        #
        #bisect_left
        begin = bisearch(left_bound, self
                , key=global_item2tree_key
                #, __lt__=ops.total_left_bound_ops.lt
                , __lt__=ops.block_dict_key_ops.ltKeyEx
                , result_case=0)
        return begin
    @override
    def prev_or_succ_position_of(ops, self, position, succ:bool):
        # -> (position | raise StopIteration)
        # StopIteration if not succ and position is the begin position of whole
        # StopIteration if succ and position is the end position of whole
        succ = bool(succ)

        L = len(self)
        if not (0 <= position <= L): raise ValueError
        if succ:
            if position == L:
                raise StopIteration
            return position + 1
        else:
            if position == 0:
                raise StopIteration
            return position - 1
        pass

    @override
    def iter_block_items_from_position(ops, self, position, *, reverse=False):
        # assume: +1 for succ, -1 for prev
        # if reverse:   self[position-1], self[position-2], ...
        #   else:       self[position], self[position+1]...
        L = len(self)
        if not (0 <= position <= L): raise ValueError
        if not reverse:
            idc = range(position, L)
        else:
            idc = range(position-1, -1, -1)
        for idx in idc:
            yield self[idx]
        return


uint_block_dict_ops__for_sorted_block_items = \
    BlockDictOps__for_sorted_block_items(theUInt_as_BlockDictKeyOps, None, tuple)
int_block_dict_ops__for_sorted_block_items = \
    BlockDictOps__for_sorted_block_items(theInt_as_BlockDictKeyOps, None, tuple)
fraction_block_dict_ops__for_sorted_block_items = \
    BlockDictOps__for_sorted_block_items(theFraction_as_BlockDictKeyOps, None, tuple)

if __name__ == '__main__':
    XXX = BlockDictOps__for_sorted_block_items

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)


