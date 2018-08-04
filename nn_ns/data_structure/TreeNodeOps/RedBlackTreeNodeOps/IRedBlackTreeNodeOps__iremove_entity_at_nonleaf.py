
__all__ = '''
    red_black_tree__iremove_entity_at_nonleaf_ex
    red_black_tree__iremove_entity_at_nonleaf

    red_black_tree__iremove_entity_at_nonleaf_with_succ_leaf_ex
    red_black_tree__iremove_entity_at_nonleaf_with_prev_leaf_ex
'''.split()



from .IRedBlackTreeNodeOps__ihandle_double_black import \
    red_black_tree__ihandle_double_black
from .IRedBlackTreeNodeOps__iremove_leaf_and_its_parent import \
    red_black_tree__iremove_leaf_and_its_parent_ex

if False:
    is_leaf = ops.is_leaf
    is_root = ops.is_root
    is_red_node = ops.is_red_node
    is_black_node = ops.is_black_node

    get_left_child = ops.get_left_child
    get_right_child = ops.get_right_child
    iter_children = ops.iter_children
    nonleaf_to_inorder_succ_leaf = ops.nonleaf_to_inorder_succ_leaf
    nonleaf_to_inorder_prev_leaf = ops.nonleaf_to_inorder_prev_leaf

    irecolor = ops.irecolor
    get_parent = ops.get_parent
    make_ROOT_PARENT_INFO = ops.get_parent_info_ops().make_ROOT_PARENT_INFO
    get_the_entity = ops.get_the_entity
    get_parent_info = ops.get_parent_info
    iset_the_entity = ops.iset_the_entity
    basic_iset_parent_info = ops.basic_iset_parent_info



def red_black_tree__iremove_entity_at_nonleaf(
    ops, nonleaf, *, child_leaf_first=True, prefer_succ_leaf=True):
    '''
1) if child_leaf_first ==>>
    if there is a child leaf, remove it and self
    else goto 2)
2) leaf = self.succ_leaf() if prefer_succ_leaf else self.prev_leaf()
    swap self.entity and leaf.parent.entity
    remove leaf and its parent
return new_root
'''
    root, is_root_double_black = red_black_tree__iremove_entity_at_nonleaf_ex(
                ops, nonleaf
                , child_leaf_first=child_leaf_first
                , prefer_succ_leaf=prefer_succ_leaf
                )
    return root


def red_black_tree__iremove_entity_at_nonleaf_ex(
        ops, nonleaf, *, child_leaf_first=True, prefer_succ_leaf=True):
    'return root, is_root_double_black'
    is_leaf = ops.is_leaf
    iter_children = ops.iter_children

    assert not is_leaf(nonleaf)

    left, right = iter_children(nonleaf)
    children = left, right
    if child_leaf_first and any(map(is_leaf, children)):
        if all(map(is_leaf, children)):
            leaf = right if prefer_succ_leaf else left
        else:
            leaf = right if is_leaf(right) else left

        return red_black_tree__iremove_leaf_and_its_parent_ex(ops, leaf)
    else:
        return red_black_tree__iremove_entity_at_nonleaf_with_prev_or_succ_leaf_ex(
                ops, nonleaf, prefer_succ_leaf)

#def red_black_tree__iremove_entity_at_nonleaf_with_succ_leaf_ex(ops, nonleaf):
#def red_black_tree__iremove_entity_at_nonleaf_with_prev_leaf_ex(ops, nonleaf):
def red_black_tree__iremove_entity_at_nonleaf_with_prev_or_succ_leaf_ex(
        ops, nonleaf, prefer_succ_leaf:bool):
    is_leaf = ops.is_leaf
    if prefer_succ_leaf:
        get_left_or_right_child = ops.get_right_child
        nonleaf_to_prev_or_succ_leaf = ops.nonleaf_to_inorder_succ_leaf
    else:
        get_left_or_right_child = ops.get_left_child
        nonleaf_to_prev_or_succ_leaf = ops.nonleaf_to_inorder_prev_leaf

    assert not is_leaf(nonleaf)
    child = get_left_or_right_child(nonleaf)
    if is_leaf(child):
        leaf = child
        return red_black_tree__iremove_leaf_and_its_parent_ex(ops, leaf)

    return __remove_leaf_and_its_parent_ex__in_subtree(
            ops, nonleaf, nonleaf_to_prev_or_succ_leaf)


def __remove_leaf_and_its_parent_ex__in_subtree(
        ops, subtree_root, leaf_gettor):
    'postcondition: broken above result_subtree'
    # split out subtree

    is_leaf = ops.is_leaf
    is_root = ops.is_root
    is_red_node = ops.is_red_node
    is_black_node = ops.is_black_node
    irecolor = ops.irecolor
    get_parent = ops.get_parent
    get_the_entity = ops.get_the_entity
    get_parent_info = ops.get_parent_info
    make_ROOT_PARENT_INFO = ops.get_parent_info_ops().make_ROOT_PARENT_INFO
    basic_iset_parent_info = ops.basic_iset_parent_info
    iset_the_entity = ops.iset_the_entity

    assert not is_leaf(subtree_root)
    org_subtree_root_is_red = is_red_node(subtree_root)
    org_subtree_root_is_root = is_root(subtree_root)
    if org_subtree_root_is_red:
        assert not org_subtree_root_is_root
        black_count = 0
        subtree_root = irecolor(subtree_root)
        # old2new broken above subtree_root
    else:
        black_count = 1
    # old2new broken above subtree_root

    assert is_black_node(subtree_root) # make sure this is really a rb tree
    org_subtree_pos = get_parent_info(subtree_root) # save
    # bug: subtree_root.parent_info = subtree_root.make_ROOT_PARENT_INFO
    subtree_root = basic_iset_parent_info(subtree_root, make_ROOT_PARENT_INFO())

    # remove
    leaf = leaf_gettor(subtree_root)
        # why not leaf but leaf_gettor?
        #   subtree_root may not be the input subtree_root

    # root.entity = leaf.parent.entity
    nonleaf_to_remove = get_parent(leaf)
        # assert nonleaf_to_remove is not subtree_root
    entity_to_store = get_the_entity(nonleaf_to_remove)
    # bugs: subtree_root is not the old subtree_root after remove
    #   subtree_root, is_subtree_root_double_black = \
    #        red_black_tree__iremove_leaf_and_its_parent_ex(ops, leaf)
    #   assert is_black_node(subtree_root)
    #   subtree_root = iset_the_entity(subtree_root, entity_to_store) # override entity
    subtree_root = iset_the_entity(subtree_root, entity_to_store) # override entity
        # since subtree_root is root, no broken!!!
    leaf = leaf_gettor(subtree_root)
        # since subtree_root is not subtree_root
    subtree_root, is_subtree_root_double_black = \
            red_black_tree__iremove_leaf_and_its_parent_ex(ops, leaf)
    assert is_black_node(subtree_root)
    # old2new broken above subtree_root

    black_count += bool(is_subtree_root_double_black)
    assert black_count in (0, 1, 2)
    if black_count == 0:
        assert org_subtree_root_is_red
        assert not org_subtree_root_is_root # since its org color is red
        subtree_root = irecolor(subtree_root) # -> RED, hence not org tree root
    # old2new broken above subtree_root

    if black_count == 0:
        assert not is_subtree_root_double_black
        assert is_red_node(subtree_root)
        is_subtree_root_double_black = False
    elif black_count == 1:
        assert is_black_node(subtree_root)
        is_subtree_root_double_black = False
    else:
        assert is_subtree_root_double_black
        assert black_count == 2
        assert is_black_node(subtree_root)
        is_subtree_root_double_black = True
    # old2new broken above subtree_root


    # join back subtree
    subtree_root = basic_iset_parent_info(subtree_root, org_subtree_pos) # restore
    # old2new broken above subtree_root

    if org_subtree_root_is_root:
        root = subtree_root
        is_root_double_black = is_subtree_root_double_black
    elif is_subtree_root_double_black:
        root, is_root_double_black = \
            red_black_tree__ihandle_double_black(ops, subtree_root)
    else:
        assert not is_root(subtree_root)
        root = fixed_the_only_broken_above_until_root(subtree_root)
        is_root_double_black = False
    assert is_black_node(root)
    return root, is_root_double_black






