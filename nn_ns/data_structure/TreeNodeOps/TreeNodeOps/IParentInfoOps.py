
__all__ = '''
    IParentInfoOps
    '''.split()

from .abc import not_implemented
from .ITreeNodeRelated import ITreeNodeRelated

class IParentInfoOps(ITreeNodeRelated):
    '''

methods:
    `get_innode_position
    `get_parent
    `get_topdown_auto_data
    `is_ROOT_PARENT_INFO
'''
    __slots__ = ()


    @not_implemented
    def is_ROOT_PARENT_INFO(ops, parent_info):
        # -- return parent_info == ROOT_PARENT_INFO
        # NOTE: can not be replaced by "parent_info == ops.make_ROOT_PARENT_INFO()"
        #       since parent_info may not support .__eq__
        ...


    @not_implemented
    def get_parent(ops, parent_info):
        # precondition:
        #    -- parent_info != ROOT_PARENT_INFO
        assert not ops.is_ROOT_PARENT_INFO(parent_info)
        ...
    @not_implemented
    def get_innode_position(ops, parent_info):
        assert not ops.is_ROOT_PARENT_INFO(parent_info)
        ...
    def get_maybe_parent_innode_position(ops, parent_info):
        # -> None | (parent, innode_position)
        if ops.is_ROOT_PARENT_INFO(parent_info):
            return None
        parent = ops.get_parent(parent_info)
        innode_position = ops.get_innode_position(parent_info)
        return (parent, innode_position)

    @not_implemented
    def get_topdown_auto_data(ops, parent_info):
        ...


if __name__ == '__main__':
    XXX = IParentInfoOps

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)


