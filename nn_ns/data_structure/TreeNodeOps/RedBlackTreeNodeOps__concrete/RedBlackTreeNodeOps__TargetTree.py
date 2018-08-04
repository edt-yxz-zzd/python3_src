

'''
used as a std red_black_tree_node


TargetTree_PlainNode
    = ()
    | (is_black::bool
        , entity::object
        , left::TargetTree_PlainNode
        , right::TargetTree_PlainNode
        )

ParentInfo = TheRootParentInfo | (parent::TargetTree_PlainNode, direction)
TargetTreeNode = (ParentInfo, TargetTree_PlainNode)
'''



__all__ = '''
    RedBlackTreeNodeOps__TargetTree
    '''.split()



from .abc import override
from ..RedBlackTreeNodeOps.IRedBlackTreeNodeOps__parent_info_plain_node import \
    IRedBlackTreeNodeOps__parent_info_plain_node
from .ParentInfoOps__parent_innode_position import \
    the_ParentInfoOps__parent_innode_position



class LEFT:
    __slots__ = ()
class RIGHT:
    __slots__ = ()

the_plain_leaf = ()

class RedBlackTreeNodeOps__TargetTree(
        IRedBlackTreeNodeOps__parent_info_plain_node):
    '''

bottomup_auto_data = None
RED = False, BLACK = True


override:
    _get_parent_info_ops_
    basic_update_plain_nonleaf
    get_BLACK
    get_LEFT
    get_RED
    get_RIGHT
    get_bottomup_auto_data_of_plain_leaf
    get_bottomup_auto_data_of_plain_nonleaf
    get_left_plain_child_of_plain_nonleaf
    get_right_plain_child_of_plain_nonleaf
    get_the_color_of_plain_nonleaf
    get_the_entity_of_plain_nonleaf
    is_plain_leaf
    make_bottomup_auto_data_of_nonleaf
    make_plain_leaf
    basic_make_plain_nonleaf
    mkNode_from_parent_info_plain_node
    unNode_to_parent_info_plain_node


example:
    >>> This = RedBlackTreeNodeOps__TargetTree
    >>> ops = theRedBlackTreeNodeOps__TargetTree
    >>> root = ops.rbt_from_entities(3, [1, 2, 3])
    >>> ops.rbt_helper_to_plain(root)
    ('BLACK', 2, ('BLACK', 1, (), ()), ('BLACK', 3, (), ()))
    >>> first_leaf, first_depth = ops.get_first_or_last_leaf_ex(root, 0, False)
    >>> ops.rbt_helper_to_direction_path(first_leaf)
    ['LEFT', 'LEFT']
    >>> [*ls] = ops.leaf_to_iter_entities_of_subtree(first_leaf, first_depth, reverse=False)
    >>> ls
    [1, 2, 3]
    >>> [*ls] = ops.leaf_to_iter_entities_of_subtree(first_leaf, first_depth, reverse=True)
    >>> ls
    []

    >>> last_leaf, last_depth = ops.get_first_or_last_leaf_ex(root, 0, True)
    >>> ops.rbt_helper_to_direction_path(last_leaf)
    ['RIGHT', 'RIGHT']
    >>> [*ls] = ops.leaf_to_iter_entities_of_subtree(last_leaf, last_depth, reverse=False)
    >>> ls
    []
    >>> [*ls] = ops.leaf_to_iter_entities_of_subtree(last_leaf, last_depth, reverse=True)
    >>> ls
    [3, 2, 1]

    >>> [*ls] = ops.iter_entities_of_subtree(root, reverse=False)
    >>> ls
    [1, 2, 3]
    >>> [*ls] = ops.iter_entities_of_subtree(root, reverse=True)
    >>> ls
    [3, 2, 1]



    >>> root = ops.rbt_from_entities(4, '0123')
    >>> ops.rbt_helper_to_plain(root)
    ('BLACK', '1', ('BLACK', '0', (), ()), ('BLACK', '2', (), ('RED', '3', (), ())))
    >>> [*ls] = ops.iter_entities_of_subtree(root, reverse=False)
    >>> ls
    ['0', '1', '2', '3']
    >>> [*ls] = ops.iter_entities_of_subtree(root, reverse=True)
    >>> ls
    ['3', '2', '1', '0']
'''
    __slots__ = ()

    @override
    def _get_parent_info_ops_(ops):
        return the_ParentInfoOps__parent_innode_position
    @override
    def basic_update_plain_nonleaf(ops, plain_nonleaf, **kwargs):

        is_black, old_entity, old_left_plain_child, old_right_plain_child = plain_nonleaf
        Nothing = []

        def this(
            bottomup_auto_data=Nothing
            , color=Nothing
            , entity=Nothing
            , left_plain_child=Nothing
            , right_plain_child=Nothing):
            if bottomup_auto_data is not Nothing:
                if bottomup_auto_data is not None: raise TypeError
            if color is Nothing:
                color = is_black
            else:
                if type(color) is not bool: raise TypeError
            if entity is Nothing:
                entity = old_entity
            if left_plain_child is Nothing:
                left_plain_child = old_left_plain_child
            if right_plain_child is Nothing:
                right_plain_child = old_right_plain_child
            return color, entity, left_plain_child, right_plain_child
        return this(**kwargs)


    @override
    def get_BLACK(ops):
        # color = is_black
        return True
    @override
    def get_RED(ops):
        return False
    @override
    def get_LEFT(ops):
        return LEFT
    @override
    def get_RIGHT(ops):
        return RIGHT

    @override
    def get_bottomup_auto_data_of_plain_leaf(ops, plain_leaf):
        return None
    @override
    def get_bottomup_auto_data_of_plain_nonleaf(ops, plain_nonleaf):
        return None
    @override
    def get_left_plain_child_of_plain_nonleaf(ops, plain_nonleaf):
        return plain_nonleaf[2]
    @override
    def get_right_plain_child_of_plain_nonleaf(ops, plain_nonleaf):
        return plain_nonleaf[3]
    @override
    def get_the_color_of_plain_nonleaf(ops, plain_nonleaf):
        return plain_nonleaf[0]
    @override
    def get_the_entity_of_plain_nonleaf(ops, plain_nonleaf):
        return plain_nonleaf[1]


    @override
    def is_plain_leaf(ops, plain_node):
        return plain_node == the_plain_leaf
    @override
    def make_plain_leaf(ops):
        return the_plain_leaf
    @override
    def basic_make_plain_nonleaf(ops, bottomup_auto_data
            , color, entity, left_plain_child, right_plain_child):
        # donot verify bottomup_auto_data
        assert type(color) is bool
        return (color, entity, left_plain_child, right_plain_child)

    @override
    def make_bottomup_auto_data_of_nonleaf(ops, left_data, right_data):
        assert left_data is None
        assert right_data is None
        return None
    @override
    def mkNode_from_parent_info_plain_node(ops, parent_info, plain_node):
        node = parent_info, plain_node
        return node
    @override
    def unNode_to_parent_info_plain_node(ops, self):
        parent_info, plain_node = self
        return parent_info, plain_node

    @override
    def get_args_for_eq_hash(ops):
        return ()

theRedBlackTreeNodeOps__TargetTree = RedBlackTreeNodeOps__TargetTree()
empty_tree = theRedBlackTreeNodeOps__TargetTree.make_root_leaf()
theRedBlackTreeNodeOps__TargetTree.check_red_black_tree_properties(empty_tree, True)


if __name__ == '__main__':
    XXX = RedBlackTreeNodeOps__TargetTree

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

if __name__ == "__main__":
    import doctest
    doctest.testmod()


