

__all__ = '''
    IOrientedTreeNodeOps
    '''.split()
from .abc import not_implemented, override
from .ITreeNodeOps import ITreeNodeOps



class IOrientedTreeNodeOps(ITreeNodeOps):
    '''# iter_children holds order

innode_position
    Eq innode_position
    entity_position =[def]= any innode_position except last_innode_position
    num_innode_positions == num_children


new methods:
    `_iter_children_
    `_iter_reversed_children_
    `_iter_innode_positions_
    `_iter_reversed_innode_positions_
    `succ_innode_position_of
    `prev_innode_position_of

    iter_children
    iter_reversed_children
    iter_innode_positions
    iter_reversed_innode_positions
    iter_innode_position_child_pairs
    iter_reversed_innode_position_child_pairs
    unstable_iter_children
    unstable_iter_innode_position_child_pairs
    get_innode_first_position_or_StopIteration
    get_innode_last_position_or_StopIteration
    get_first_child_or_StopIteration
    get_last_child_or_StopIteration

    is_first_child
    is_last_child
    is_first_innode_position
    is_last_innode_position

    get_first_math_leaf_of_subtree
    get_last_math_leaf_of_subtree
'''
    __slots__ = ()


    # nonroot
    def is_first_child(ops, self):
        assert not ops.is_root(self)
        parent = ops.get_parent(self)
        pos = ops.get_innode_position(self)
        return ops.is_first_innode_position(parent, pos)
    def is_last_child(ops, self):
        assert not ops.is_root(self)
        parent = ops.get_parent(self)
        pos = ops.get_innode_position(self)
        return ops.is_last_innode_position(parent, pos)



    # nonleaf

    @not_implemented
    def _iter_children_(ops, self):
        assert ops.is_nonleaf(self)
        ...
    @not_implemented
    def _iter_reversed_children_(ops, self):
        assert ops.is_nonleaf(self)
        ...

    @not_implemented
    def _iter_innode_positions_(ops, self):
        # -> Iter innode_position
        #   not (Iter entity_position)
        # include the end/last innode_position
        assert ops.is_nonleaf(self)
        ...
    @not_implemented
    def _iter_reversed_innode_positions_(ops, self):
        # -> Iter innode_position
        #   not (Iter entity_position)
        # include the end/last innode_position
        assert ops.is_nonleaf(self)
        ...

    @not_implemented
    def succ_innode_position_of(ops, self, innode_position):
        # innode_position -> (succ_innode_position | raise StopIteration)
        #
        # * entity_position -> innode_position
        #   entity_position -> (entity_position | end innode_position)
        # * end innode_position -> raise StopIteration
        assert not ops.is_leaf(self)
        ...
    @not_implemented
    def prev_innode_position_of(ops, self, innode_position):
        # innode_position -> (prev_innode_position | raise StopIteration)
        # * (innode_position != begin innode_position) -> entity_position
        # * begin innode_position -> raise StopIteration
        assert not ops.is_leaf(self)
        ...



    def prev_or_succ_innode_position_of(ops, self, innode_position, succ:bool):
        # -> (prev_innode_position | raise StopIteration)
        assert not ops.is_leaf(self)
        if succ:
            f = ops.succ_innode_position_of
        else:
            f = ops.prev_innode_position_of
        return f(self, innode_position)




    def iter_children(ops, self, *, reverse=False):
        if not reverse:
            f = ops._iter_children_
        else:
            f = ops._iter_reversed_children_
        return f(self)
    def iter_innode_positions(ops, self, *, reverse=False):
        if not reverse:
            f = ops._iter_innode_positions_
        else:
            f = ops._iter_reversed_innode_positions_
        return f(self)

    def iter_reversed_children(ops, self, *, reverse=False):
        return ops.iter_children(self, reverse=not reverse)
    def iter_reversed_innode_positions(ops, self, *, reverse=False):
        return ops.iter_innode_positions(self, reverse=not reverse)

    def iter_innode_position_child_pairs(ops, self, *, reverse=False):
        reverse = bool(reverse)
        return zip(ops.iter_innode_positions(self, reverse=reverse)
                    , ops.iter_children(self, reverse=reverse))
    def iter_reversed_innode_position_child_pairs(ops, self, *, reverse=False):
        return ops.iter_innode_position_child_pairs(self, reverse=not reverse)

    @override
    def unstable_iter_children(ops, self):
        return ops.iter_children(self)
    @override
    def unstable_iter_innode_position_child_pairs(ops, self):
        return ops.iter_innode_position_child_pairs(self)








    def is_first_or_last_innode_position(ops, self, innode_position, last:bool):
        assert not ops.is_leaf(self)

        if ops.is_math_tree_leaf(self): return False
        first_or_last_pos = ops.get_innode_first_or_last_position_or_StopIteration(self, last)
        return innode_position == first_or_last_pos
    def is_first_innode_position(ops, self, innode_position):
        return ops.is_first_or_last_innode_position(self, innode_position, False)
    def is_last_innode_position(ops, self, innode_position):
        return ops.is_first_or_last_innode_position(self, innode_position, True)





    def get_innode_first_or_last_position_or_StopIteration(ops, self, last:bool):
        assert ops.is_nonleaf(self)
        #may not self.num_children
        for c in ops.iter_innode_positions(self, reverse=last):
            return c
        assert ops.get_num_children(self) == 0
        raise StopIteration('has no children')

    def get_innode_first_position_or_StopIteration(ops, self):
        f = ops.get_innode_first_or_last_position_or_StopIteration
        return f(self, False)
    def get_innode_last_position_or_StopIteration(ops, self):
        f = ops.get_innode_first_or_last_position_or_StopIteration
        return f(self, True)



    def get_first_or_last_child_or_StopIteration(ops, self, last:bool):
        # -> child | raise StopIteration
        assert ops.is_nonleaf(self)
        #may not self.num_children
        for c in ops.iter_children(self, reverse=last):
            return c
        raise StopIteration('has no children')
    def get_first_child_or_StopIteration(ops, self):
        f = ops.get_first_or_last_child_or_StopIteration
        return f(self, False)
    def get_last_child_or_StopIteration(ops, self):
        f = ops.get_first_or_last_child_or_StopIteration
        return f(self, True)


    def get_first_or_last_math_leaf_of_subtree(ops, self, last):
        is_math_tree_leaf = ops.is_math_tree_leaf
        get_child = ops.get_first_or_last_child_or_StopIteration

        last = bool(last)
        node = self
        while not is_math_tree_leaf(node):
            node = get_child(node, last)
        return node

    def get_first_math_leaf_of_subtree(ops, self):
        return ops.get_first_or_last_math_leaf_of_subtree(self, False)
    def get_last_math_leaf_of_subtree(ops, self):
        return ops.get_first_or_last_math_leaf_of_subtree(self, True)



if __name__ == '__main__':
    XXX = IOrientedTreeNodeOps

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)




