
__all__ = '''
    ParentInfoOps__parent_innode_position
    the_ParentInfoOps__parent_innode_position
    '''.split()

from .abc import override
from ..TreeNodeOps.IParentInfoOps__constructor import \
    IParentInfoOps__constructor

# parent_info = (parent_node, direction) | TheRootParentInfo
#   topdown_auto_data = None

class TheRootParentInfo:
    __slots__ = ()
class ParentInfoOps__parent_innode_position(IParentInfoOps__constructor):
    __slots__ = ()

    @override
    def make_child_parent_info_at_position(
            ops, node_ops, parent_node, innode_position):
        assert not node_ops.is_leaf(parent_node)
        return (parent_node, innode_position)

    @override
    def make_ROOT_PARENT_INFO(ops):
        return TheRootParentInfo

    ###########
    @override
    def is_ROOT_PARENT_INFO(ops, parent_info):
        return parent_info is TheRootParentInfo

    # precondition:
    #    -- parent_info != ROOT_PARENT_INFO
    @override
    def get_parent(ops, parent_info):
        assert not ops.is_ROOT_PARENT_INFO(parent_info)
        parent_node, innode_position = parent_info
        return parent_node
    @override
    def get_innode_position(ops, parent_info):
        assert not ops.is_ROOT_PARENT_INFO(parent_info)
        parent_node, innode_position = parent_info
        return innode_position
    @override
    def get_topdown_auto_data(ops, parent_info):
        return None

    @override
    def get_args_for_eq_hash(ops):
        return ()

the_ParentInfoOps__parent_innode_position = \
    ParentInfoOps__parent_innode_position()

