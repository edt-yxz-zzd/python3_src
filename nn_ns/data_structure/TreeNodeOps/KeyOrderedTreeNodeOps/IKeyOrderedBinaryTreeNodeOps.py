__all__ = '''
    IKeyOrderedBinaryTreeNodeOps
    '''.split()

from .abc import not_implemented, override, abstractmethod
from .IKeyOrderedUnbalancedMultiWayTreeNodeOps import \
    IKeyOrderedUnbalancedMultiWayTreeNodeOps
from ..UnbalancedMultiWayTreeNodeOps.IBinaryTreeNodeOps import\
    IBinaryTreeNodeOps

class IKeyOrderedBinaryTreeNodeOps(
        IKeyOrderedUnbalancedMultiWayTreeNodeOps
        , IBinaryTreeNodeOps
        ):
    '''

abstract_methods:
    `_get_parent_info_ops_
    `get_parent_info

    `get_LEFT
    `get_RIGHT
    `is_leaf
    `get_left_child
    `get_right_child

    `_get_key_ops_
    `entity2key
    `get_the_entity

    `get_impl_data
    `get_usr_data
    `get_bottomup_auto_data

new_concrete_methods:
    get_the_key
    find_maybe_first_nonleaf_of_subtree
    find_maybe_last_nonleaf_of_subtree


    # override
    find_innode_range_of_nonleaf
    find_innode_begin_of_nonleaf
    find_innode_end_of_nonleaf
'''
    __slots__ = ()

    def get_the_key(ops, self):
        return ops.entity2key(ops.get_the_entity(self))

    @property
    @override
    def find_innode_range_of_nonleaf(ops):
        # useless
        return super().find_innode_range_of_nonleaf

    @override
    def find_innode_begin_of_nonleaf(ops, self, key):
        self_key = ops.get_the_key(self)
        if ops.key_lt(self_key, key):
            # self_key < key
            return ops.get_RIGHT()
        # key <= self_key
        return ops.get_LEFT()
    @override
    def find_innode_end_of_nonleaf(ops, self, key):
        self_key = ops.get_the_key(self)
        if ops.key_lt(key, self_key):
            # key < self_key
            return ops.get_LEFT()
        # self_key <= key
        return ops.get_RIGHT()


    #############
    def find_maybe_first_nonleaf_of_subtree(ops, self, depth, key):
        # return leaf if not found
        # -> (node, depth)
        node, may_pos, depth = ops.find_maybe_first_nonleaf_ex_of_subtree(self, depth, key)
        return node, depth

    def find_maybe_last_nonleaf_of_subtree(ops, self, depth, key):
        # return leaf if not found
        # -> (node, depth)
        # if return leaf, then not found
        leaf = ops.find_end_leaf_of_subtree(self, key)
        node, may_pos, depth = ops.find_maybe_last_nonleaf_ex_of_subtree(self, depth, key)
        return node, depth


if __name__ == '__main__':
    XXX = IKeyOrderedBinaryTreeNodeOps

    from seed.helper.print_methods import print_methods
    print_methods(XXX)

