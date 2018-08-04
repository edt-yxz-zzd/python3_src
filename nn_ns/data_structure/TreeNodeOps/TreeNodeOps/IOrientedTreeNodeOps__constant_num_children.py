
__all__ = '''
    IOrientedTreeNodeOps__constant_num_children
    IOrientedTreeNodeOps__positive_constant_num_children
    '''.split()
from .abc import not_implemented, override, abstractmethod
from .IOrientedTreeNodeOps import IOrientedTreeNodeOps
from .IOrientedTreeNodeOps__positive_num_children import \
    IOrientedTreeNodeOps__positive_num_children

class IOrientedTreeNodeOps__constant_num_children(IOrientedTreeNodeOps):
    'nonleaf.num_children == C'
    __slots__ = ()

    @not_implemented
    def static_get_num_children_of_nonleaf(ops):
        ...
        raise ...
        m = ops.static_get_min_num_children_of_nonleaf()
        M = ops.static_get_max_num_children_of_nonleaf_or_inf()
        if m != M: raise TypeError
        return m
    @override
    def static_get_min_num_children_of_nonleaf(ops):
        return ops.static_get_num_children_of_nonleaf()
    @override
    def static_get_max_num_children_of_nonleaf_or_inf(ops):
        return ops.static_get_num_children_of_nonleaf()

    @override
    def get_num_children(ops, self):
        assert not ops.is_leaf(self)
        return ops.static_get_num_children_of_nonleaf()

class IOrientedTreeNodeOps__positive_constant_num_children(
        IOrientedTreeNodeOps__constant_num_children
        , IOrientedTreeNodeOps__positive_num_children):
    __slots__ = ()

    @override
    def _get_num_children_(ops, self):
        assert not ops.is_leaf(self)
        return ops.static_get_num_children_of_nonleaf()
    @override
    def get_num_children(ops, self):
        assert ops.is_nonleaf(self)
        n = ops._get_num_children_(self)
        assert n > 0
        return n
    @override
    def static_get_min_num_children_of_nonleaf(ops):
        return ops.static_get_num_children_of_nonleaf()
    @override
    def static_get_max_num_children_of_nonleaf_or_inf(ops):
        return ops.static_get_num_children_of_nonleaf()

