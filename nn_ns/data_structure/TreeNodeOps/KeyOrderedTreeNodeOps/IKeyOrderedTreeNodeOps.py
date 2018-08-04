__all__ = '''
    IKeyOrderedTreeNodeOps
    '''.split()

from .abc import not_implemented, override
from .ITotalOrderingOps import ITotalOrderingOps
from ..TreeNodeOps.IOrientedTreeNodeOps import IOrientedTreeNodeOps


class IKeyOrderedTreeNodeOps(IOrientedTreeNodeOps):
    '''total_ordering key


abstract_methods:
    `_get_key_ops_
    `entity2key

    `_get_parent_info_ops_
    `get_parent_info

    `is_leaf
    `get_num_children
    `get_child_at
    `iter_children
    `iter_reversed_children

    `iter_innode_positions
    `iter_reversed_innode_positions
    `prev_innode_position_of
    `succ_innode_position_of

    `get_bottomup_auto_data
    `get_impl_data
    `get_usr_data


concrete_methods:
    # subtree
    bottomup_eval_unoriented_subtree
    calc_num_nodes_of_subtree
    get_first_math_leaf_of_subtree
    get_last_math_leaf_of_subtree


    # key
    get_key_ops
    key_eq
    key_ge
    key_gt
    key_le
    key_lt
    key_ne

    # data
    get_leaf_impl_data
    get_leaf_usr_data
    get_nonleaf_impl_data
    get_nonleaf_usr_data

    # nonroot
    is_root
    is_nonroot
    is_first_child
    is_last_child
    get_parent
    get_innode_position
    get_parent_info_ops
    get_topdown_auto_data

    # nonleaf
    is_math_tree_leaf
    is_nonleaf
    iter_innode_position_child_pairs
    iter_reversed_innode_position_child_pairs
    new_innode_position2child_dict
    unstable_iter_children
    unstable_iter_innode_position_child_pairs

    get_first_child_or_StopIteration
    get_last_child_or_StopIteration

    get_innode_first_position_or_StopIteration
    get_innode_last_position_or_StopIteration
    is_first_innode_position
    is_last_innode_position

'''
    __slots__ = ()

    @not_implemented
    def entity2key(ops, entity):
        return entity

    @not_implemented
    def _get_key_ops_(ops):
        ...
    def get_key_ops(ops):
        # bug: key_ops = ops.get_key_ops()
        key_ops = ops._get_key_ops_()
        assert isinstance(key_ops, ITotalOrderingOps)
        return key_ops




    @property
    def key_le(ops):
        return ops.get_key_ops().le
    @property
    def key_lt(ops):
        return ops.get_key_ops().lt
    @property
    def key_eq(ops):
        return ops.get_key_ops().eq
    @property
    def key_ne(ops):
        return ops.get_key_ops().ne
    @property
    def key_gt(ops):
        return ops.get_key_ops().gt
    @property
    def key_ge(ops):
        return ops.get_key_ops().ge


if __name__ == '__main__':
    XXX = IKeyOrderedTreeNodeOps

    from seed.helper.print_methods import print_methods
    print_methods(XXX)






