
__all__ = '''
    IKeyOrderedRedBlackTreeNodeOps
    '''.split()



from .abc import override

from .IKeyOrderedBinaryTreeNodeOps import IKeyOrderedBinaryTreeNodeOps
from ..RedBlackTreeNodeOps.IRedBlackTreeNodeOps import IRedBlackTreeNodeOps

class IKeyOrderedRedBlackTreeNodeOps(
        IKeyOrderedBinaryTreeNodeOps
        , IRedBlackTreeNodeOps):
    __slots__ = ()

    def check_KeyOrderedRedBlackTreeNode(ops, self, as_root, *, strict:bool):
        reasons = ops.why_bad_KeyOrderedRedBlackTreeNode(self, as_root, strict=strict)
        if reasons: raise ValueError(reasons)

    @override
    def why_not_subtree_ok(ops, self, **kwargs):
        # kwargs readonly, should not remove key from it
        #   i.e. donot override: def is_subtree_ok(ops, self, *, as_root=..., **kwargs)
        return (ops.why_bad_KeyOrderedRedBlackTreeNode(
                    self, kwargs['as_root'], strict=kwargs['strict'])
                + super().why_not_subtree_ok(self, **kwargs)
                )
    def why_bad_KeyOrderedRedBlackTreeNode(ops, self, as_root, *, strict:bool):
        # -> reasons
        reasons1 = ops.why_not_entities_key_ordered(self, strict=strict)
        reasons2 = ops.why_not_holds_red_black_tree_properties(self, as_root)
        return reasons1+reasons2
    def is_good_KeyOrderedRedBlackTreeNode(ops, self, as_root, *, strict:bool):
        return (ops.are_entities_key_ordered(self, strict=strict)
            and ops.holds_red_black_tree_properties(self, as_root)
            )
    pass





