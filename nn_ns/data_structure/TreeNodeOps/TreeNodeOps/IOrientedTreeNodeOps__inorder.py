


__all__ = '''
    IOrientedTreeNodeOps__inorder
    '''.split()

from .abc import not_implemented, override, abstractmethod
from .IOrientedTreeNodeOps__positive_num_children import \
    IOrientedTreeNodeOps__positive_num_children
from .depth import verify_depth




class IOrientedTreeNodeOps__inorder(IOrientedTreeNodeOps__positive_num_children):
    '''
inorder ==>> nonleaf.num_children >= 2


num_innode_positions == num_children
num_middle_position == num_children - 1
middle_position == entity_position == innode_position
    except:
        middle_position == entity_position != last_innode_position == entity_end


new methods:
    leaf_to_inorder_succ_nonleaf_entity_position_ex
    leaf_to_inorder_prev_nonleaf_entity_position_ex

    nonleaf_entity_position_to_inorder_succ_leaf_ex
    nonleaf_entity_position_to_inorder_prev_leaf_ex

    leaf_to_inorder_iter_node_entity_position_triples
    leaf_to_inorder_iter_reversed_node_entity_position_triples

    __inorder__iter_node_triples2iter_nonleaf_triples
    leaf_to_inorder_iter_nonleaf_entity_position_triples
    leaf_to_inorder_iter_reversed_nonleaf_entity_position_triples
'''
    __slots__ = ()

    @override
    def static_get_min_num_children_of_nonleaf(ops):
        # inorder ==>> nonleaf.num_children >= 2
        return max(2, super().static_get_min_num_children_of_nonleaf())
        return 2


    ############## inorder
    ############## inorder ==>> require all nonleaf.num_children >= 2


    def leaf_to_inorder_prev_or_succ_nonleaf_entity_position_ex(ops, self, depth, succ:bool):
        # leaf -> ((nonleaf, innode_position, depth) | raise StopIteration)
        if succ:
            f = ops.leaf_to_inorder_succ_nonleaf_entity_position_ex
        else:
            f = ops.leaf_to_inorder_prev_nonleaf_entity_position_ex
        return f(self, depth)

    def leaf_to_inorder_succ_nonleaf_entity_position_ex(ops, self, depth):
        # leaf -> ((nonleaf, innode_position, depth) | raise StopIteration)
        # depth == 0: treat self as root of subtree, donot escape this subtree
        # depth == -inf: iter whole tree
        ####### inorder ==>> require all nonleaf.num_children >= 2
        assert ops.is_leaf(self)
        assert verify_depth(depth)

        node = self
        is_root = ops.is_root
        get_parent = ops.get_parent
        get_innode_position = ops.get_innode_position
        is_last_innode_position = ops.is_last_innode_position
        while not (depth == 0 or is_root(node)):
            depth -= 1
            parent = get_parent(node)
            pos = get_innode_position(node)
            if not is_last_innode_position(parent, pos):
                #bug: succ_pos = ops.succ_innode_position_of(parent, pos)
                #   succ(pos) may be entity_end!!
                succ_pos = pos
                return parent, succ_pos, depth
            node = parent
        else:
            if is_root(node):
                raise StopIteration('self is last leaf of whole tree')
            assert depth == 0
            raise StopIteration('self is last leaf of subtree')


    def leaf_to_inorder_prev_nonleaf_entity_position_ex(ops, self, depth):
        # leaf -> ((nonleaf, innode_position, depth) | raise StopIteration)
        # depth == 0: treat self as root of subtree, donot escape this subtree
        # depth == -inf: iter whole tree
        ####### inorder ==>> require all nonleaf.num_children >= 2
        assert ops.is_leaf(self)
        assert verify_depth(depth)
        node = self
        is_root = ops.is_root
        get_parent = ops.get_parent
        get_innode_position = ops.get_innode_position
        is_first_innode_position = ops.is_first_innode_position

        while not (depth == 0 or is_root(node)):
            depth -= 1
            parent = get_parent(node)
            pos = get_innode_position(node)
            if not is_first_innode_position(parent, pos):
                prev_pos = ops.prev_innode_position_of(parent, pos)
                return parent, prev_pos, depth
            node = parent
        else:
            if is_root(node):
                raise StopIteration('self is first leaf of whole tree')
            assert depth == 0
            raise StopIteration('self is first leaf of subtree')




    def nonleaf_entity_position_to_inorder_prev_or_succ_leaf_ex(ops, self, innode_position, depth, succ:bool):
        # nonleaf -> innode_position in nonleaf -> depth of nonleaf -> (leaf, depth of leaf)
        # depth == 0: treat self as root of subtree, donot escape this subtree
        # depth == -inf: iter whole tree
        ####### inorder ==>> require all nonleaf.num_children >= 2
        assert ops.is_nonleaf(self)
        assert verify_depth(depth)
        node = self
        pos = innode_position
        assert not ops.is_last_innode_position(node, pos)

        succ = bool(succ)
        if succ:
            pos = ops.succ_innode_position_of(node, pos)
        else:
            pos = pos

        child = ops.get_child_at(node, pos)

        last = last_leaf_of_child = not succ
        leaf, depth = ops.get_first_or_last_leaf_ex(child, depth+1, last)
        return leaf, depth
    def nonleaf_entity_position_to_inorder_succ_leaf_ex(ops, self, innode_position, depth):
        f = ops.nonleaf_entity_position_to_inorder_prev_or_succ_leaf_ex
        return f(self, innode_position, depth, True)
        #####
        right_child = ops.get_right_child(self)
        return ops.get_first_leaf_ex(right_child)

    def nonleaf_entity_position_to_inorder_prev_leaf_ex(ops, self, innode_position, depth):
        f = ops.nonleaf_entity_position_to_inorder_prev_or_succ_leaf_ex
        return f(self, innode_position, depth, False)
        #####
        left_child = ops.get_left_child(self)
        return ops.get_last_leaf(left_child)




    def leaf_to_inorder_iter_reversed_node_entity_position_triples(ops, self, depth, *, reverse=False):
        # -> Iter (node, may_entity_position, depth)
        # -> Iter ((nonleaf, entity_position, depth)|(leaf, None, depth))
        f = ops.leaf_to_inorder_iter_node_entity_position_triples
        return f(self, depth, reverse=not reverse)
    def leaf_to_inorder_iter_node_entity_position_triples(ops, self, depth, *, reverse=False):
        '''iter nodes after self in inorder till last leaf of subtree; include self
        # -> Iter (node, may_entity_position, depth)
        # -> Iter ((nonleaf, entity_position, depth)|(leaf, None, depth))

depth == -inf: whole tree
depth == 0: self is root of subtree
node_entity_position_triple = (nonleaf, entity_position, depth) | (leaf, None, depth)
'''
        assert ops.is_leaf(self)
        assert verify_depth(depth)

        leaf = self; del self
        if not reverse:
            # succ
            leaf2nonleaf = ops.leaf_to_inorder_succ_nonleaf_entity_position_ex
            nonleaf2leaf = ops.nonleaf_entity_position_to_inorder_succ_leaf_ex
        else:
            # prev
            leaf2nonleaf = ops.leaf_to_inorder_prev_nonleaf_entity_position_ex
            nonleaf2leaf = ops.nonleaf_entity_position_to_inorder_prev_leaf_ex
        while True:
            yield leaf, None, depth
            nonleaf, pos, depth = leaf2nonleaf(leaf, depth) # may StopIteration
            yield nonleaf, pos, depth
            leaf, depth = nonleaf2leaf(nonleaf, pos, depth)


    @staticmethod
    def __iter_node_triples2iter_leaf_pairs(it):
        # leaf_pair = (leaf, depth)
        it = iter(it)
        while True:
            leaf, _None, depth = leaf_triple = next(it)
            yield leaf, depth
            nonleaf_triple = next(it) # may StopIteration
    @staticmethod
    def __iter_node_triples2iter_nonleaf_triples(it):
        # nonleaf_triple = (nonleaf, entity_position, depth)
        it = iter(it)
        while True:
            leaf_triple = next(it)
            nonleaf_triple = next(it) # may StopIteration
            yield nonleaf_triple

    def leaf_to_inorder_iter_reversed_nonleaf_entity_position_triples(ops, self, depth, *, reverse=False):
        # -> Iter (nonleaf, entity_position, depth)
        f = ops.leaf_to_inorder_iter_nonleaf_entity_position_triples
        return f(self, depth, reverse=not reverse)
    def leaf_to_inorder_iter_nonleaf_entity_position_triples(ops, self, depth, *, reverse=False):
        # -> Iter (nonleaf, entity_position, depth)
        assert ops.is_leaf(self)
        leaf = self
        it = ops.leaf_to_inorder_iter_node_entity_position_triples(leaf, depth, reverse=reverse)
        return __class__.__iter_node_triples2iter_nonleaf_triples(it)

    def leaf_to_inorder_iter_leaf_depth_pairs(ops, self, depth, *, reverse=False):
        # -> Iter (leaf, depth)
        assert ops.is_leaf(self)
        leaf = self
        it = ops.leaf_to_inorder_iter_node_entity_position_triples(leaf, depth, reverse=reverse)
        return __class__.__iter_node_triples2iter_leaf_pairs(it)
    def leaf_to_inorder_iter_prev_or_succ_leaf_ex(ops, self, depth, succ:bool):
        # -> (leaf, depth) | raise StopIteration
        assert ops.is_leaf(self)
        leaf = self
        f = ops.leaf_to_inorder_iter_leaf_depth_pairs
        it = f(self, depth, reverse=not succ)
        the_self, depth = next(it)
        leaf, depth = next(it)
        return leaf, depth



if __name__ == '__main__':
    XXX = IOrientedTreeNodeOps__inorder

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)





