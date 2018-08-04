

__all__ = '''
    IBinaryTreeNodeOps
    '''.split()
from .abc import not_implemented, override, abstractmethod
from ..TreeNodeOps.IOrientedTreeNodeOps__constant_num_children import \
    IOrientedTreeNodeOps__positive_constant_num_children
from ..TreeNodeOps.IOrientedTreeNodeOps__inorder import \
    IOrientedTreeNodeOps__inorder
from .IUnbalancedMultiWayTreeNodeOps import \
    IUnbalancedMultiWayTreeNodeOps
from ..TreeNodeOps.depth import verify_depth, neg_inf




class IBinaryTreeNodeOps(
        IUnbalancedMultiWayTreeNodeOps
        #IOrientedTreeNodeOps__inorder
        , IOrientedTreeNodeOps__positive_constant_num_children):
    '''

nonleaf.num_children == 2
nonleaf.iter_innode_positions == [LEFT, RIGHT]
direction =[def]= innode_position
    alias
    require: direction.__eq__


LEFT/RIGHT will be used as key in dict ==>> hashable and __eq__

new methods:
    `get_LEFT
    `get_RIGHT
    `get_left_child
    `get_right_child
    `get_the_entity

    get_entity_at

    is_LEFT
    is_RIGHT
    static_iter_innode_positions
    static_iter_reversed_innode_positions
    get_direction
    get_maybe_parent_direction
    another_direction_of
    get_another_direction
    get_sibling
    is_left_child
    is_right_child

    __iter_triples2iter_pairs
    nonleaf_to_inorder_succ_leaf_ex
    nonleaf_to_inorder_prev_leaf_ex
    leaf_to_inorder_succ_nonleaf_ex
    leaf_to_inorder_prev_nonleaf_ex
    nonleaf_to_inorder_succ_leaf
    nonleaf_to_inorder_prev_leaf
    leaf_to_inorder_succ_nonleaf
    leaf_to_inorder_prev_nonleaf

    leaf_to_inorder_iter_node_pairs
    leaf_to_inorder_iter_reversed_node_pairs
    leaf_to_inorder_iter_nonleaf_node_pairs
    leaf_to_inorder_iter_reversed_nonleaf_node_pairs


    iter_nodes_of_subtree
    iter_reversed_nodes_of_subtree
    __nonleaf_join_leaves_to_leaves
    __nonleaf_join_leaves_to_nonleaves
    iter_leaf_nodes_of_subtree
    iter_reversed_leaf_nodes_of_subtree
    iter_nonleaf_nodes_of_subtree
    iter_reversed_nonleaf_nodes_of_subtree

override:
    static_get_num_children_of_nonleaf
    _iter_children_
    _iter_reversed_children_
    _iter_innode_positions_
    _iter_reversed_innode_positions_
    get_first_child
    get_last_child
    get_child_at

    prev_innode_position_of
    succ_innode_position_of

    _iter_entities_of_nonleaf_
    _iter_reversed_entities_of_nonleaf_

'''
    __slots__ = ()

    @abstractmethod
    def get_the_entity(ops, self):
        return ops.get_usr_data(self)
    def get_entity_at(ops, self, entity_position):
        # like get_child_at
        assert entity_position != ops.get_innode_entity_end(self)
        assert entity_position == ops.get_LEFT()
        return ops.get_the_entity(self)


    @override
    def _iter_entities_of_nonleaf_(ops, self):
        assert not ops.is_leaf(self)
        yield ops.get_the_entity(self)
    @override
    def _iter_reversed_entities_of_nonleaf_(ops, self):
        assert not ops.is_leaf(self)
        yield ops.get_the_entity(self)





    def get_maybe_parent_direction(ops, self):
        # -> None | (parent, direction)
        return ops.get_maybe_parent_innode_position(self)

    @override
    def static_get_num_children_of_nonleaf(ops):
        return 2

    def static_iter_innode_positions(ops):
        yield ops.get_LEFT()
        yield ops.get_RIGHT()
    def static_iter_reversed_innode_positions(ops):
        yield ops.get_RIGHT()
        yield ops.get_LEFT()
    def another_direction_of(ops, direction):
        return ops.get_RIGHT() if direction == ops.get_LEFT() else ops.get_LEFT()



    # constant

    # the only two innode_pos values
    @not_implemented
    def get_LEFT(ops):...
    @not_implemented
    def get_RIGHT(ops):...

    def is_LEFT(ops, direction):
        # return direction == ops.get_LEFT()
        LEFT = ops.get_LEFT()
        eq = ops.basic_eqHashableConstant

        if eq(direction, LEFT): return True

        RIGHT = ops.get_RIGHT()
        if eq(direction, RIGHT): return False
        raise TypeError

    def is_RIGHT(ops, direction):
        return not ops.is_LEFT(direction)






    # nonleaf

    @not_implemented
    def get_left_child(ops, self):
        assert not ops.is_leaf(self)
        ...
    @not_implemented
    def get_right_child(ops, self):
        assert not ops.is_leaf(self)
        ...








    ## override

    @override
    def _iter_children_(ops, self):
        assert not ops.is_leaf(self)
        yield ops.get_left_child(self)
        yield ops.get_right_child(self)
    @override
    def _iter_reversed_children_(ops, self):
        assert not ops.is_leaf(self)
        yield ops.get_right_child(self)
        yield ops.get_left_child(self)

    @override
    def _iter_innode_positions_(ops, self):
        assert not ops.is_leaf(self)
        return ops.static_iter_innode_positions()
    @override
    def _iter_reversed_innode_positions_(ops, self):
        assert not ops.is_leaf(self)
        return ops.static_iter_reversed_innode_positions()

    @override
    def get_first_child(ops, self):
        assert not ops.is_leaf(self)
        return ops.get_left_child(self)
    @override
    def get_last_child(ops, self):
        assert not ops.is_leaf(self)
        return ops.get_right_child(self)


    @override
    def get_child_at(ops, self, direction):
        assert not ops.is_leaf(self)
        return ops.get_left_child(self) if direction == ops.get_LEFT() else ops.get_right_child(self)









    # nonroot query

    # the same as self.innode_position
    # return LEFT/RIGHT
    def get_direction(ops, self):
        assert not ops.is_root(self)
        return ops.get_innode_position(self)

    def get_another_direction(ops, self):
        assert not ops.is_root(self)
        return ops.another_direction_of(ops.get_direction(self))

    def get_sibling(ops, self):
        assert not ops.is_root(self)
        parent = ops.get_parent(self)
        another_direction = ops.get_another_direction(self)
        return ops.get_child_at(parent, another_direction)
    def is_left_child(ops, self):
        assert not ops.is_root(self)
        return ops.get_direction(self) == ops.get_LEFT()
    def is_right_child(ops, self):
        assert not ops.is_root(self)
        return not ops.is_left(self)

    @override
    def is_first_child(ops, self):
        return ops.is_left_child(self)
    @override
    def is_last_child(ops, self):
        return ops.is_right_child(self)






    # iter/travel
    @staticmethod
    def __iter_triples2iter_pairs(it):
        # triple = (nonleaf, innode_position, depth) | (leaf, None, depth)
        it = iter(it)
        for node, may_pos, depth in it:
            yield node, depth

    def leaf_to_inorder_succ_nonleaf(ops, self):
        # may raise StopIteration
        nonleaf, _ = ops.leaf_to_inorder_succ_nonleaf_ex(self, neg_inf)
        return nonleaf
    def leaf_to_inorder_succ_nonleaf_ex(ops, self, depth):
        # may raise StopIteration
        # depth may < 0
        assert verify_depth(depth)
        nonleaf, _LEFT, depth = ops.leaf_to_inorder_succ_nonleaf_entity_position_ex(self, depth)
        return nonleaf, depth

    def leaf_to_inorder_prev_nonleaf(ops, self):
        # may raise StopIteration
        nonleaf, _ = ops.leaf_to_inorder_prev_nonleaf_ex(self, neg_inf)
        return nonleaf
    def leaf_to_inorder_prev_nonleaf_ex(ops, self, depth):
        # may raise StopIteration
        # depth may < 0
        assert verify_depth(depth)
        nonleaf, _LEFT, depth = ops.leaf_to_inorder_prev_nonleaf_entity_position_ex(self, depth)
        return nonleaf, depth

    def nonleaf_to_inorder_succ_leaf(ops, self):
        leaf, _ = ops.nonleaf_to_inorder_succ_leaf_ex(self, 0)
        return leaf
    def nonleaf_to_inorder_succ_leaf_ex(ops, self, depth):
        # depth may < 0
        assert ops.is_nonleaf(self)
        assert verify_depth(depth)
        right_child = ops.get_right_child(self)
        leaf, depth = ops.get_first_leaf_ex(right_child, depth+1)
        return leaf, depth
    def nonleaf_to_inorder_prev_leaf(ops, self):
        leaf, _ = ops.nonleaf_to_inorder_prev_leaf_ex(self, 0)
        return leaf
    def nonleaf_to_inorder_prev_leaf_ex(ops, self, depth):
        assert ops.is_nonleaf(self)
        assert verify_depth(depth)
        left_child = ops.get_left_child(self)
        leaf, depth = ops.get_last_leaf_ex(left_child, depth+1)
        return leaf, depth



    def leaf_to_inorder_iter_node_pairs(ops, self, depth):
        it = ops.leaf_to_inorder_iter_node_entity_position_triples(self, depth)
        return __class__.__iter_triples2iter_pairs(it)
    def leaf_to_inorder_iter_reversed_node_pairs(ops, self, depth):
        it = ops.leaf_to_inorder_iter_reversed_node_entity_position_triples(self, depth)
        return __class__.__iter_triples2iter_pairs(it)
    def leaf_to_inorder_iter_nonleaf_node_pairs(ops, self, depth):
        it = ops.leaf_to_inorder_iter_nonleaf_entity_position_triples(self, depth)
        return __class__.__iter_triples2iter_pairs(it)
    def leaf_to_inorder_iter_reversed_nonleaf_node_pairs(ops, self, depth):
        it = ops.leaf_to_inorder_iter_reversed_nonleaf_entity_position_triples(self, depth)
        return __class__.__iter_triples2iter_pairs(it)




    #############

    def iter_nodes_of_subtree(ops, self):
        leaf, depth = ops.get_first_leaf_ex(self, 0)
        for node, depth in ops.leaf_to_inorder_iter_node_pairs(leaf, depth):
            yield node
    def iter_reversed_nodes_of_subtree(ops, self):
        leaf, depth = ops.get_last_leaf_ex(self, 0)
        for node, depth in ops.leaf_to_inorder_iter_reversed_node_pairs(leaf, depth):
            yield node

    @staticmethod
    def __nonleaf_join_leaves_to_leaves(it):
        it = iter(it)
        while True:
            leaf = next(it) # may StopIteration
            yield leaf
            nonleaf = next(it)

    @staticmethod
    def __nonleaf_join_leaves_to_nonleaves(it):
        it = iter(it)
        while True:
            leaf = next(it) # may StopIteration
            nonleaf = next(it)
            yield nonleaf

    def iter_leaf_nodes_of_subtree(ops, self):
        it = ops.iter_nodes_of_subtree(self)
        return __class__.__nonleaf_join_leaves_to_leaves(it)
    def iter_reversed_leaf_nodes_of_subtree(ops, self):
        it = ops.iter_reversed_nodes_of_subtree(self)
        return __class__.__nonleaf_join_leaves_to_leaves(it)

    def iter_nonleaf_nodes_of_subtree(ops, self):
        it = ops.iter_nodes_of_subtree(self)
        return __class__.__nonleaf_join_leaves_to_nonleaves(it)
    def iter_reversed_nonleaf_nodes_of_subtree(ops, self):
        it = ops.iter_reversed_nodes_of_subtree(self)
        return __class__.__nonleaf_join_leaves_to_nonleaves(it)




    @override
    def succ_innode_position_of(ops, self, innode_position):
        # innode_position -> (succ_innode_position | raise StopIteration)
        if ops.is_RIGHT(innode_position):
            raise StopIteration
        return ops.get_RIGHT()
    @override
    def prev_innode_position_of(ops, self, innode_position):
        # innode_position -> (prev_innode_position | raise StopIteration)
        if ops.is_LEFT(innode_position):
            raise StopIteration
        return ops.get_LEFT()




    ##########

if __name__ == '__main__':
    XXX = IBinaryTreeNodeOps

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)



