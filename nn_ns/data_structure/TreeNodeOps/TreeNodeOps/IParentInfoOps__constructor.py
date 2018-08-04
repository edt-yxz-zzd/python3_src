


__all__ = '''
    IParentInfoOps__constructor
    '''.split()
from .abc import not_implemented
from .ITreeNodeRelated import ITreeNodeRelated
from .IParentInfoOps import IParentInfoOps


class IParentInfoOps__constructor(IParentInfoOps):
    __slots__ = ()

    @not_implemented
    def make_child_parent_info_at_position(
        # precondition:
        #    -- not self.is_leaf()
        #    allow old2new/new2old/dangling broken below self
            ops, node_ops, parent_node, innode_position):
        assert node_ops.is_nonleaf(parent_node)
        ...


    @not_implemented
    def make_ROOT_PARENT_INFO(ops):
        # -- return ROOT_PARENT_INFO
        # postcondition:
        #    ops.make_ROOT_PARENT_INFO() may or may not return same object
        ...

