__all__ = '''
    IUnbalancedMultiWayTreeNodeOps
    '''.split()

from .abc import not_implemented, override
from ..TreeNodeOps.IOrientedTreeNodeOps__inorder import \
    IOrientedTreeNodeOps__inorder


class IUnbalancedMultiWayTreeNodeOps(IOrientedTreeNodeOps__inorder):
    '''
    assume nonleaf.num_children > 0 since num_entities = num_children-1
    assume nonleaf.num_children >= 2 since inorder


entity_position == innode_position
    except:
        entity_position != innode_last == entity_end



new methods:
    `get_entity_at
    `_iter_entities_of_nonleaf_
    `_iter_reversed_entities_of_nonleaf_

    iter_entities_of_nonleaf
    iter_reversed_entities_of_nonleaf
    get_num_entities_of_nonleaf
    calc_num_entities_of_subtree
    iter_innode_position_entity_pairs_of_nonleaf
    iter_reversed_innode_position_entity_pairs_of_nonleaf
    get_innode_entity_begin
    get_innode_entity_end
    get_innode_entity_begin_or_end


    iter_entities_of_subtree
    iter_reversed_entities_of_subtree
    leaf_to_iter_entities_of_subtree
    leaf_to_iter_reversed_entities_of_subtree
'''
    __slots__ = ()

    @override
    def why_not_subtree_ok(ops, self, **kwargs):
        # kwargs readonly, should not remove key from it
        #   i.e. donot override: def is_subtree_ok(ops, self, *, as_root=..., **kwargs)
        return (ops.why_not_num_entities_of_nonleaf_ok(self)
                + super().why_not_subtree_ok(self, **kwargs)
                )
    def why_not_num_entities_of_nonleaf_ok(ops, self):
        # num_entities_of_nonleaf = num_children-1
        #
        is_leaf = ops.is_leaf
        unstable_iter_nodes_of_subtree = ops.unstable_iter_nodes_of_subtree
        get_num_children = ops.get_num_children
        get_num_entities_of_nonleaf = ops.get_num_entities_of_nonleaf

        #if ops.is_leaf(self): return ()
        for node in unstable_iter_nodes_of_subtree(self):
            if is_leaf(node): continue
            nonleaf = node; del node

            num_children = get_num_children(nonleaf)
            num_entities_of_nonleaf = get_num_entities_of_nonleaf(nonleaf)
            if num_children != 1+num_entities_of_nonleaf:
                return ('num_children != 1+num_entities_of_nonleaf',)
        return ()

    def get_num_entities_of_nonleaf(ops, self):
        assert not ops.is_leaf(self)
        return ops.get_num_children(self) - 1
        ########## require num_children > 0 ################
    #def get_num_entities_of_subtree(ops, self):
    def calc_num_entities_of_subtree(ops, self):
        on_leaf = lambda _: 0
        on_nonleaf = ops.get_num_entities_of_nonleaf
        combine = lambda a, bs: sum(bs, a)
        return ops.bottomup_eval_unoriented_subtree(
                    self, on_leaf, on_nonleaf, combine)
        if ops.is_leaf(self):
            return 0
        return sum(map(ops.calc_num_entities_of_subtree
                        , ops.unstable_iter_children(self))
                  , ops.get_num_entities_of_nonleaf(self))

  # nonleaf

    @not_implemented
    def _iter_entities_of_nonleaf_(ops, self):
        # self as node, not as subtree
        assert not ops.is_leaf(self)
        ...
    @not_implemented
    def _iter_reversed_entities_of_nonleaf_(ops, self):
        # self as node, not as subtree
        assert not ops.is_leaf(self)
        ...


    def iter_entities_of_nonleaf(ops, self, *, reverse=False):
        if not reverse:
            f = ops._iter_entities_of_nonleaf_
        else:
            f = ops._iter_reversed_entities_of_nonleaf_
        return f(self)
    def iter_reversed_entities_of_nonleaf(ops, self, *, reverse=False):
        return ops.iter_entities_of_nonleaf(self, reverse=not reverse)


    def iter_innode_position_entity_pairs_of_nonleaf(ops, self, *, reverse=False):
        # NOTE: not output innode_last (== child_last == entity_end)
        return zip(ops.iter_innode_positions(self, reverse=reverse)
                , ops.iter_entities_of_nonleaf(self, reverse=reverse))

    def iter_reversed_innode_position_entity_pairs_of_nonleaf(ops, self, *, reverse=False):
        # NOTE: not output innode_last (== child_last == entity_end)
        return ops.iter_innode_position_entity_pairs_of_nonleaf(self, reverse=not reverse)


    # entity_begin == child_begin
    # entity_end == child_last
    def get_innode_entity_begin_or_end(ops, self, end:bool):
        return ops.get_innode_first_or_last_position(self)
    def get_innode_entity_begin(ops, self):
        return ops.get_innode_first_position(self)
    def get_innode_entity_end(ops, self):
        return ops.get_innode_last_position(self)

    @not_implemented
    def get_entity_at(ops, self, entity_position):
        # like get_child_at
        assert entity_position != ops.get_innode_entity_end(self)
        ...


    def iter_reversed_entities_of_subtree(ops, self, *, reverse=False):
        return ops.iter_entities_of_subtree(self, reverse=not reverse)
    def iter_entities_of_subtree(ops, self, *, reverse=False):
        # reverse ==>> last leaf
        last = reverse = bool(reverse)
        leaf, depth = ops.get_first_or_last_leaf_ex(self, 0, last)
        return ops.leaf_to_iter_entities_of_subtree(leaf, depth, reverse=reverse)

    @staticmethod
    def __nonleaf_triples2entities(get_entity_at, triples):
        # triple = (nonleaf, entity_position, depth)
        # get_entity_at = ops.get_entity_at
        for nonleaf, entity_position, depth in triples:
            yield get_entity_at(nonleaf, entity_position)

    def leaf_to_iter_reversed_entities_of_subtree(ops, self, depth, *, reverse=False):
        f = ops.leaf_to_iter_entities_of_subtree
        return f(self, depth, reverse=not reverse)
    def leaf_to_iter_entities_of_subtree(ops, self, depth, *, reverse=False):
        assert ops.is_leaf(self)
        f = ops.leaf_to_inorder_iter_nonleaf_entity_position_triples
        it = f(self, depth, reverse=reverse)
        return __class__.__nonleaf_triples2entities(ops.get_entity_at, it)




if __name__ == '__main__':
    XXX = IUnbalancedMultiWayTreeNodeOps

    from seed.helper.print_methods import print_methods
    print_methods(XXX)
