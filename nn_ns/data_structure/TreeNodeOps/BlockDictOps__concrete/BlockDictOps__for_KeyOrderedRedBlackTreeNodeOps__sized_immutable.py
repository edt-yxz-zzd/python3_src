
__all__ = '''
    BlockDictOps__for_KeyOrderedRedBlackTreeNodeOps__sized_immutable
    uint_block_dict_ops
    int_block_dict_ops
    fraction_block_dict_ops
    '''.split()

from .abc import override
from ..OtherOps.IEqOps import IEqOps
from ..OtherOps.ITotalOrderingOps import ITotalOrderingOps
from ..BlockDictOps.IBlockDictKeyOps import IBlockDictKeyOps, KeyExCase
from ..OtherOps.EqOps import EqOps, python_eq_key_ops

from ..RedBlackTreeNodeOps__concrete.KeyOrderedRedBlackTreeNodeOps__sized_immutable import \
    KeyOrderedRedBlackTreeNodeOps__sized_immutable

from ..BlockDictOps.IBlockDictOps__blind_iupdate import IBlockDictOps__blind_iupdate
from ..BlockDictOps.IBlockDictOps__position import IBlockDictOps__position
from ..RedBlackTreeNodeOps__concrete.KeyOrderedRedBlackTreeNodeOps__sized_immutable import \
    KeyOrderedRedBlackTreeNodeOps__sized_immutable
from .theUInt_as_BlockDictKeyOps import theUInt_as_BlockDictKeyOps
from .theInt_as_BlockDictKeyOps import theInt_as_BlockDictKeyOps
from .theFraction_as_BlockDictKeyOps import theFraction_as_BlockDictKeyOps



#from collections.abc import MutableMapping
import operator
from seed.helper.repr_input import repr_helper
from seed.tiny import fst, snd



# global_item2tree_key :: ((left_bound, right_bound), dict_value) -> left_bound
global_item2tree_key = lambda e: e[0][0]
#Node__global = KeyOrderedRedBlackTreeNodeOps__sized_immutable(None, None)
neg_inf = float('-inf')


class BlockDictOps__for_KeyOrderedRedBlackTreeNodeOps__sized_immutable(
        IBlockDictOps__blind_iupdate
        , IBlockDictOps__position
        ):
    '''

self                    :: KeyOrderedRedBlackTreeNodeOps__sized_immutable
left_bound              as tree_key
leaf                    as position
(block_key, dict_value) as tree_entity

testing:
    see: BlockDict2
'''
    __slots__ = '''
        _block_dict_key_ops
        _eq_dict_value_ops
        _RBT_Node
        '''.split()

    def __init__(ops, block_dict_key_ops, eq_dict_value_ops):
        '''
input:
    block_dict_key_ops :: IBlockDictKeyOps<dict_key>
        # about dict_key instead of tree_key

    # no: dict_key2tree_key :: None | (dict_key -> tree_key)
    eq_dict_value_ops :: None | IEqOps<dict_value>
        default = python_eq_key_ops

'''
        if not isinstance(block_dict_key_ops, IBlockDictKeyOps): raise TypeError
        if eq_dict_value_ops is None:
            eq_dict_value_ops = python_eq_key_ops
        elif not isinstance(eq_dict_value_ops, IEqOps): raise TypeError

        total_left_bound_ops = block_dict_key_ops.make_total_left_bound_ops()
        assert isinstance(total_left_bound_ops, ITotalOrderingOps)

        # left_bound = tree_key
        RBT_Node = KeyOrderedRedBlackTreeNodeOps__sized_immutable(
                    total_left_bound_ops, global_item2tree_key)

        ops._block_dict_key_ops = block_dict_key_ops
        ops._eq_dict_value_ops = eq_dict_value_ops
        ops._RBT_Node = RBT_Node
        return


    def __repr__(ops):
        block_dict_key_ops = ops.block_dict_key_ops
        eq_dict_value_ops = ops.eq_dict_value_ops

        if eq_dict_value_ops == python_eq_key_ops:
            eq_dict_value_ops = None

        return repr_helper(ops, block_dict_key_ops, eq_dict_value_ops)

    @property
    def Node(ops):
        return ops._RBT_Node

    @override
    def make_empty_block_dict(ops):
        return ops.Node.make_root_leaf()
    @override
    def copy_block_dict(ops, self):
        return self
    @override
    def iassign(ops, self, other):
        return other






    @override
    def get_args_for_eq_hash(ops):
        return (ops.block_dict_key_ops, ops.eq_dict_value_ops)



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
        return ops.Node.get_num_entities_of_subtree(self)
    @override
    def iter_block_items(ops, self, *, reverse=False):
        # no items
        return ops.Node.iter_entities_of_subtree(self, reverse=reverse)
    @override
    def ipop_left_or_right_block_item(ops, self, right:bool):
        last = bool(right)
        old_entity, new_self = ops.Node.rbt_ipop_the_first_or_last_entity_of_subtree(self, last)
        return old_entity, new_self

    @override
    def iclear(ops, self):
        return ops.Node.make_root_leaf()

    @override
    def _index_block_item_at_(ops, self, i:'UInt'):
        # -> block_item
        assert 0 <= i < ops.get_num_block_keys(self)
        return ops.Node.index_entity_at(self, i)







    @override
    def _blind_iupdate_exactly_(
            ops, self, block_keys_to_del, block_items_to_insert):
        # -> new_self
        #
        # assume self is a dict<block_key, dict_value>
        #   update directly
        #   donot care whether block_key is empty, insert/remove it directly
        #   treat all block_keys as exaclty block_keys
        #   see: is_exactly_block_key
        Node = ops.Node
        iremove = Node.find_and_iremove_first_or_last_entity_of_subtree
        iinsert_ex = Node.find_and_iinsert_entity_of_tree_if_not_any_ex

        tree = self

        last = True
        block_key2tree_key = fst # left_bound = tree_key
        for block_key in block_keys_to_del:
            tree_key = block_key2tree_key(block_key)
            tree = iremove(tree, tree_key, last)

        for entity in block_items_to_insert:
            does_iinsert, tree = iinsert_ex(tree, entity)
            assert does_iinsert
        new_self = tree
        return new_self


    @override
    def get_the_begin_or_end_position(ops, self, end:bool):
        last = bool(end)
        return ops.Node.get_first_or_last_leaf(self, last)
    @override
    def _left_bound2begin_(ops, self, left_bound):
        # -> position
        # if begin not the begin position of whole:
        #   then left_bound may be inside the range at prev(begin)
        #
        # leaf as position
        tree = self
        tree_key = left_bound
        leaf = ops.Node.find_begin_leaf_of_subtree(tree, tree_key)
        begin = leaf
        return begin
    @override
    def prev_or_succ_position_of(ops, self, position, succ:bool):
        # -> (position | raise StopIteration)
        # StopIteration if not succ and position is the begin position of whole
        # StopIteration if succ and position is the end position of whole
        leaf = position
        leaf, depth = ops.Node.leaf_to_inorder_iter_prev_or_succ_leaf_ex(leaf, neg_inf, succ)
        return leaf

    @override
    def iter_block_items_from_position(ops, self, position, *, reverse=False):
        # assume: +1 for succ, -1 for prev
        # if reverse:   self[position-1], self[position-2], ...
        #   else:       self[position], self[position+1]...
        leaf = position
        return ops.Node.leaf_to_iter_entities_of_subtree(leaf, neg_inf, reverse=reverse)


uint_block_dict_ops = BlockDictOps__for_KeyOrderedRedBlackTreeNodeOps__sized_immutable(theUInt_as_BlockDictKeyOps, None)
int_block_dict_ops = BlockDictOps__for_KeyOrderedRedBlackTreeNodeOps__sized_immutable(theInt_as_BlockDictKeyOps, None)
fraction_block_dict_ops = BlockDictOps__for_KeyOrderedRedBlackTreeNodeOps__sized_immutable(theFraction_as_BlockDictKeyOps, None)

if __name__ == '__main__':
    XXX = BlockDictOps__for_KeyOrderedRedBlackTreeNodeOps__sized_immutable

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)


