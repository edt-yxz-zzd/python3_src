
__all__ = '''
    IUnbalancedMultiWayTreeNodeOps__num_entities_of_subtree
    '''.split()

from .abc import not_implemented, override, abstractmethod
from .IUnbalancedMultiWayTreeNodeOps import IUnbalancedMultiWayTreeNodeOps
from ..TreeNodeOps.depth import verify_depth

from numbers import Integral



class IUnbalancedMultiWayTreeNodeOps__num_entities_of_subtree(
        IUnbalancedMultiWayTreeNodeOps):
    '''
new_methods:
    `get_num_entities_of_subtree
    `index_nonleaf_entity_position_ex_at

    index_entity_at
    is_num_entities_of_subtree_ok
    why_not_num_entities_of_subtree_ok
    check_num_entities_of_subtree_ok
'''
    __slots__ = ()

    @not_implemented
    def get_num_entities_of_subtree(ops, self):
        ...

    @abstractmethod
    def index_nonleaf_entity_position_ex_at(ops, self, depth, idx):
        # to be overrided by binary search??
        # -> (nonleaf, entity_position, depth) | IndexError
        #assert type(idx) is int and 0 <= idx < num_entities_of_subtree
        is_leaf = ops.is_leaf
        get_num_entities_of_subtree = ops.get_num_entities_of_subtree
        iter_innode_position_child_pairs = ops.iter_innode_position_child_pairs
        is_last_innode_position = ops.is_last_innode_position

        assert verify_depth(depth)
        assert not is_leaf(self)

        num_entities_of_subtree = get_num_entities_of_subtree(self)
        if not (0 <= idx < num_entities_of_subtree): raise IndexError

        nonleaf = self; del self

        while True:
            for innode_position, child in iter_innode_position_child_pairs(nonleaf):
                num_entities_of_child_subtree = get_num_entities_of_subtree(child)
                assert 0 <= num_entities_of_child_subtree < num_entities_of_subtree
                if idx < num_entities_of_child_subtree:
                    break
                elif idx == num_entities_of_child_subtree:
                    assert not is_last_innode_position(nonleaf, innode_position)
                    entity_position = innode_position # not last
                    return nonleaf, entity_position, depth
                else:
                    idx -= num_entities_of_child_subtree
                    idx -= 1
            else:
                raise logic-error

            assert num_entities_of_child_subtree > idx >= 0
            assert not is_leaf(child)

            nonleaf = child
            depth += 1


    def index_entity_at(ops, self, idx):
        # -> entity
        # index_entity_at of subtree
        # get_entity_at of nonleaf
        nonleaf, entity_position, depth = ops.index_nonleaf_entity_position_ex_at(self, 0, idx)
        return ops.get_entity_at(nonleaf, entity_position)

    def is_num_entities_of_subtree_ok(ops, self):
        return not ops.why_not_num_entities_of_subtree_ok(self)
    def check_num_entities_of_subtree_ok(ops, self):
        reasons = ops.why_not_num_entities_of_subtree_ok(self)
        if reasons: raise ValueError(reasons)

    @override
    def why_not_subtree_ok(ops, self, **kwargs):
        # kwargs readonly, should not remove key from it
        #   i.e. donot override: def is_subtree_ok(ops, self, *, as_root=..., **kwargs)
        return (ops.why_not_num_entities_of_subtree_ok(self)
                + super().why_not_subtree_ok(self, **kwargs)
                )
    def why_not_num_entities_of_subtree_ok(ops, self):
        get_num_entities_of_subtree = ops.get_num_entities_of_subtree
        get_num_entities_of_nonleaf = ops.get_num_entities_of_nonleaf
        is_leaf = ops.is_leaf
        iter_children = ops.iter_children

        reasons = set()
        stack = [self]; del self
        while stack:
            node = stack.pop()
            num_entities_of_subtree = get_num_entities_of_subtree(node)
            if not isinstance(num_entities_of_subtree, Integral):
                reasons.add('node.num_entities_of_subtree is not Integral')
            if num_entities_of_subtree < 0:
                reasons.add('node.num_entities_of_subtree < 0')

            if is_leaf(node):
                leaf = node; del node
                if num_entities_of_subtree != 0:
                    reasons.add('leaf.num_entities_of_subtree != 0')
                continue

            nonleaf = node; del node
            if num_entities_of_subtree <= 0:
                reasons.add('nonleaf.num_entities_of_subtree <= 0')

            [*children] = iter_children(nonleaf)
            num_entities_of_nonleaf = get_num_entities_of_nonleaf(nonleaf)
            #if len(children) != 1+num_entities_of_nonleaf:
            #    reasons.add('len(children) != 1 + nonleaf.num_entities_of_nonleaf')

            if num_entities_of_subtree != num_entities_of_nonleaf \
                + sum(map(get_num_entities_of_subtree, children)):
                reasons.add('num_entities_of_nonleaf !='
                            'num_entities_of_nonleaf + '
                            'sum(map(get_num_entities_of_subtree, children))')

            stack.extend(children)
        return tuple(sorted(reasons))



if __name__ == '__main__':
    XXX = IUnbalancedMultiWayTreeNodeOps__num_entities_of_subtree

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)




