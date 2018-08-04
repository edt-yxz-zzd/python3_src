
__all__ = '''
    copy_from_another_ops_subtree_as_tree__def
    '''.split()


def copy_from_another_ops_subtree_as_tree__def(ops, another_ops, another_node):
    '''
may return a tree with red root
which is not a red_black_tree

requires:
    another_ops / from_ops
        .is_leaf
        .iter_children
        .get_the_color
        .get_the_entity
        .is_RED
    ops / to_ops
        .make_root_leaf
        .make_root_nonleaf
        .get_RED
        .get_BLACK
'''
    #is_root = another_ops.is_root
    is_leaf = another_ops.is_leaf
    iter_children = another_ops.iter_children
    get_the_color = another_ops.get_the_color
    get_the_entity = another_ops.get_the_entity
    is_RED = another_ops.is_RED

    #assert is_root(another_node)
    CASE_recur = 0
    CASE_merge = 1
    another_stack = [(CASE_recur, another_node)]
    # another_stack = [(CASE_recur, another_node)|(CASE_merge, another_node)]
    subtree_stack = []


    make_root_leaf = ops.make_root_leaf
    make_root_nonleaf = ops.make_root_nonleaf
    RED = ops.get_RED()
    BLACK = ops.get_BLACK()

    while another_stack:
        case, another_node = another_stack.pop()
        if case is CASE_recur:
            if is_leaf(another_node):
                # basic case of recur
                node = make_root_leaf()
                subtree_stack.append(node)
            else:
                another_stack.append((CASE_merge, another_node))
                another_left, another_right = iter_children(another_node)

                another_stack.append((CASE_recur, another_left))
                another_stack.append((CASE_recur, another_right))
                # another_stack append: another_left, then another_right
                # ==>> another_stack = [..., another_left, another_right]
                # ... flip ...
                # ==>> will subtree_stack = [..., right, left]
        else:
            assert case is CASE_merge
            assert not is_leaf(another_node)
            assert len(subtree_stack) >= 2

            # subtree_stack = [..., right, left]
            left_child = subtree_stack.pop()
            right_child = subtree_stack.pop()
            entity = get_the_entity(another_node)

            another_color = get_the_color(another_node)
            color = RED if is_RED(another_color) else BLACK
            # bug: color = get_the_color(another_node)

            node = make_root_nonleaf(
                    color=color, entity=entity
                    , left_child=left_child, right_child=right_child
                    )

            subtree_stack.append(node)

    assert len(subtree_stack) == 1
    root, = subtree_stack
    may_red_root = root
    return may_red_root

