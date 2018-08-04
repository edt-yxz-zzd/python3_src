
__all__ = '''
    ITreeNodeOps__constructor
    '''.split()
from .abc import not_implemented
from .ITreeNodeOps import ITreeNodeOps
from .IParentInfoOps__constructor import IParentInfoOps__constructor


class ITreeNodeOps__constructor(ITreeNodeOps):
    __slots__ = ()

    @not_implemented
    def copy_subtree_as_tree(ops, self):
        # copy self as a subtree root
        # result is a whole tree
        #   i.e. new self is root of new tree
        ...

    def get_parent_info_ops(ops):
        parent_info_ops = super().get_parent_info_ops()
        assert isinstance(parent_info_ops, IParentInfoOps__constructor)
        return parent_info_ops

    @property
    def make_ROOT_PARENT_INFO(ops):
        return ops.get_parent_info_ops().make_ROOT_PARENT_INFO
    def make_child_parent_info_at_position(
            ops, parent_node, innode_position):
        assert ops.is_nonleaf(parent_node)
        return ops.get_parent_info_ops().make_child_parent_info_at_position(
                ops, parent_node, innode_position)

