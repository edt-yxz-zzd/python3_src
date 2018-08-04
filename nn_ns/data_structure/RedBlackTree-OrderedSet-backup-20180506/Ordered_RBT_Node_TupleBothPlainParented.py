
__all__ = '''
    Ordered_RBT_Node_TupleBothPlainParented
    '''.split()


if 0 and useful:
    # constructor
        copy
        from_sorted_entities

        make_leaf_root
        insert_entity_as_first
        insert_entity_as_last
        subtree_remove_first_entity
        subtree_remove_last_entity

        remove_entity_at_nonleaf
        remove_leaf_and_its_parent

    # find
        subtree_contains
        subtree_find_begin_leaf
        subtree_find_end_leaf
        subtree_find_maybe_first_nonleaf
        subtree_find_maybe_last_nonleaf
        subtree_get_first_entity
        subtree_get_last_entity

        find_innode_begin
        find_innode_end
        find_innode_range

    # iter
        # not:
        #   iter_entities
        #   iter_reversed_entities
        get_first_leaf
        get_last_leaf

        leaf_inorder_iter_nodes
        leaf_inorder_iter_nonleaf_nodes
        leaf_inorder_iter_reversed_nodes
        leaf_inorder_iter_reversed_nonleaf_nodes

        leaf_inorder_prev_nonleaf
        leaf_inorder_succ_nonleaf

        nonleaf_inorder_prev_leaf
        nonleaf_inorder_succ_leaf

    # key
        key_eq
        key_lt
        entity2key




from .RedBlackTree.RedBlackTreeNodeABC import \
     RBT_Node_TupleBothPlainParented
from .RedBlackTree.OrderedMutableRedBlackTreeNodeABC import\
    OrderedMutableRedBlackTreeNodeABC


class Ordered_RBT_Node_TupleBothPlainParented(
        RBT_Node_TupleBothPlainParented, OrderedMutableRedBlackTreeNodeABC):
    pass

if __name__ == '__main__':
    Node = Ordered_RBT_Node_TupleBothPlainParented
    print(Node)
    print('\n'.join(dir(Node)))
    '''
<class '__main__.Ordered_RBT_Node_TupleBothPlainParented'>
BLACK
LEFT
PLAIN_LEAF
RED
RIGHT
ROOT_PARENT_INFO
_BinaryTreeNodeABC__iter_nodes2iter_nonleaf_nodes
_MutableTreeNodeWrapperABC__setattr
_MutableTreeNodeWrapperABC__test_known_keywords__setattr_underlying_leaf_node
_MutableTreeNodeWrapperABC__test_known_keywords__setattr_underlying_nonleaf_node
_RBT_NodeWrapper_ABC__setattr
__abstractmethods__
__eq__
__ge__
__gt__
__hash__
__le__
__lt__
__ne__
__repr__
__str__
_make_child_parent_info_at_pos
_make_plain
another_color
another_color_from
another_direction
another_direction_from
children
color
direction
entity
entity2key
extract_underlying_leaf_data_as_dict
extract_underlying_nonleaf_data
extract_underlying_nonleaf_data_as_dict
find_innode_begin
find_innode_end
find_innode_range
first_child
fixed_the_only_broken_above_until_root
fixed_the_only_broken_above_until_root__refresh_down
fixed_the_only_broken_above_until_root__with_new_me
from_root_plain_node
from_underlying_node
from_underlying_node_and_parent_info
get_child
get_child_at_pos
get_first_leaf
get_innode_begin
get_innode_entity_end
get_innode_position_from
get_last_leaf
get_parent_from
get_underlying_child
get_underlying_child_at_pos
get_underlying_color
get_underlying_entity
get_underlying_left
get_underlying_other_leaf_attr_dict
get_underlying_other_nonleaf_attr_dict
get_underlying_parent_from
get_underlying_parent_info
get_underlying_plain
get_underlying_position_from
get_underlying_position_parent_dict
get_underlying_right
innode_first_position
innode_last_position
innode_position
insert_entity_as_first
insert_entity_as_last
insert_entity_at_leaf
is_PLAIN_LEAF
is_ROOT_PARENT_INFO
is_black
is_leaf
is_left
is_math_tree_leaf
is_nonleaf
is_nonroot
is_red
is_right
is_root
is_root_underlying_parent_info
is_underlying_leaf
iter_children
iter_entities
iter_innode_position_child_pairs
iter_innode_position_entity_pairs
iter_innode_positions
iter_reversed_children
iter_reversed_entities
iter_reversed_innode_position_child_pairs
iter_reversed_innode_position_entity_pairs
iter_reversed_innode_positions
iter_underlying_children
iter_underlying_position_child_pairs
key_eq
key_lt
last_child
leaf_inorder_iter_nodes
leaf_inorder_iter_nonleaf_nodes
leaf_inorder_iter_reversed_nodes
leaf_inorder_iter_reversed_nonleaf_nodes
leaf_inorder_prev_nonleaf
leaf_inorder_succ_nonleaf
leaf_node_eq
left
make_child_parent_info
make_child_parent_info_at_pos
make_leaf_root
make_nonleaf_root
make_nonleaf_root_with_leaves
make_parent_info_from_dict
make_plain
make_red_nonleaf_node
make_red_nonleaf_root
make_underlying_leaf
make_underlying_leaf_root
make_underlying_nonleaf
make_underlying_nonleaf_rbt
new_ROOT_PARENT_INFO
new_innode_position2child_dict
new_innode_position2underlying_child_dict
new_underlying_ROOT_PARENT_INFO
nonleaf_inorder_prev_leaf
nonleaf_inorder_succ_leaf
nonleaf_node_eq
num_children
num_entities
num_plain_node_extra_attrs
num_underlying_parent_info_extra_attrs
ordered_plain_node_extra_attr_names
ordered_underlying_parent_info_extra_attr_names
oriented_subtree_eq
parent
parent_info
plain
recolor
refresh_downs
refresh_up
remove_entity_at_nonleaf
remove_leaf_and_its_parent
right
set_child
set_child_at_pos
set_underlying_parent_info
setattr_underlying_leaf_node
setattr_underlying_nonleaf_node
sibling
subtree_contains
subtree_find_begin_leaf
subtree_find_end_leaf
subtree_find_maybe_first_nonleaf
subtree_find_maybe_last_nonleaf
subtree_get_first_entity
subtree_get_last_entity
subtree_remove_first_entity
subtree_remove_last_entity
trinode_restructure
'''

