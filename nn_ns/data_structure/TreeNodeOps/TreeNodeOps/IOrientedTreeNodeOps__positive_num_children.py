
__all__ = '''
    IOrientedTreeNodeOps__positive_num_children
    '''.split()
from .abc import not_implemented, override
from .IOrientedTreeNodeOps import IOrientedTreeNodeOps
from .depth import verify_depth


class IOrientedTreeNodeOps__positive_num_children(IOrientedTreeNodeOps):
    'nonleaf.num_children > 0; i.e. nonleaf is also math nonleaf'
    __slots__ = ()

    @not_implemented
    def _get_num_children_(ops, self):
        assert ops.is_nonleaf(self)
        ...

    def static_get_min_num_children_of_nonleaf(ops):
        return max(1, super().static_get_min_num_children_of_nonleaf())
        return 1

    @override
    def get_num_children(ops, self):
        assert ops.is_nonleaf(self)
        n = ops._get_num_children_(self)
        assert n >= ops.static_get_min_num_children()
        return n

    @override
    def is_math_tree_leaf(ops, self):
        # math tree and computer tree are different concepts
        #assert ops.is_leaf(self) or ops.num_children(self) > 0
        return ops.is_leaf(self)
        return ops.is_leaf(self) or ops.num_children(self) == 0


    def get_first_leaf(ops, self):
        return ops.get_first_or_last_leaf(self, False)
    def get_last_leaf(ops, self):
        return ops.get_first_or_last_leaf(self, True)
    def get_first_or_last_leaf(ops, self, last:bool):
        leaf, depth = ops.get_first_or_last_leaf_ex(self, 0, last)
        return leaf



    def get_first_leaf_ex(ops, self, depth):
        return ops.get_first_or_last_leaf_ex(self, depth, False)
    def get_last_leaf_ex(ops, self, depth):
        return ops.get_first_or_last_leaf_ex(self, depth, True)
    def get_first_or_last_leaf_ex(ops, self, depth, last:bool):
        assert verify_depth(depth)
        is_leaf = ops.is_leaf
        if not last:
            get_child = ops.get_first_child
        else:
            get_child = ops.get_last_child

        node = self
        while not is_leaf(node):
            node = get_child(node)
            depth += 1
        leaf = node
        return leaf, depth



    @override
    def get_innode_first_or_last_position_or_StopIteration(ops, self, last:bool):
        return ops.get_innode_first_or_last_position(self, last)
    def get_innode_first_or_last_position(ops, self, last:bool):
        assert ops.is_nonleaf(self)
        #assert self.num_children
        for c in ops.iter_innode_positions(self, reverse=last):
            return c
        raise logic-error

    @override
    def get_innode_first_position_or_StopIteration(ops, self):
        return ops.get_innode_first_position(self)
    def get_innode_first_position(ops, self):
        return ops.get_innode_first_or_last_position(self, False)
    @override
    def get_innode_last_position_or_StopIteration(ops, self):
        return ops.get_innode_last_position(self)
    def get_innode_last_position(ops, self):
        return ops.get_innode_first_or_last_position(self, True)




    @override
    def get_first_or_last_child_or_StopIteration(ops, self, last:bool):
        return ops.get_first_or_last_child(self, last)
    def get_first_or_last_child(ops, self, last:bool):
        assert ops.is_nonleaf(self)
        #assert self.num_children
        for c in ops.iter_children(self, reverse=last):
            return c
        raise logic-error
    @override
    def get_first_child_or_StopIteration(ops, self):
        return ops.get_first_child(self)
    def get_first_child(ops, self):
        return ops.get_first_or_last_child(self, False)
    @override
    def get_last_child_or_StopIteration(ops, self):
        return ops.get_last_child(self)
    def get_last_child(ops, self):
        return ops.get_first_or_last_child(self, True)

