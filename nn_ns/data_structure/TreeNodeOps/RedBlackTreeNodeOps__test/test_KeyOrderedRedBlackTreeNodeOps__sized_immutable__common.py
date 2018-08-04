
__all__ = '''
    KeyOrderedRedBlackTreeNodeOps__sized_immutable
    simple_KRBT_SI

    This
    ops
    is_leaf
    is_root
    is_RED
    is_red_node
    is_LEFT
    get_parent

    rbt_from_entities
    rbt_helper_to_plain
    rbt_helper_from_plain
    rbt_helper_to_direction_path
    iter_entities_of_subtree
    get_num_entities_of_subtree
    why_not_subtree_ok

    list_entities
    '''.split()

from ..RedBlackTreeNodeOps__concrete.KeyOrderedRedBlackTreeNodeOps__sized_immutable import \
    KeyOrderedRedBlackTreeNodeOps__sized_immutable, simple_KRBT_SI

This = KeyOrderedRedBlackTreeNodeOps__sized_immutable
ops = simple_KRBT_SI
is_leaf = ops.is_leaf
is_root = ops.is_root
is_RED = ops.is_RED
is_red_node = ops.is_red_node
is_LEFT = ops.is_LEFT
get_parent = ops.get_parent

rbt_from_entities = ops.rbt_from_entities
rbt_helper_to_plain = ops.rbt_helper_to_plain
rbt_helper_from_plain = ops.rbt_helper_from_plain
rbt_helper_to_direction_path = ops.rbt_helper_to_direction_path
iter_entities_of_subtree = ops.iter_entities_of_subtree
get_num_entities_of_subtree = ops.get_num_entities_of_subtree
why_not_subtree_ok = ops.why_not_subtree_ok

def list_entities(subtree, reverse=False):
    return [*iter_entities_of_subtree(subtree, reverse=reverse)]

