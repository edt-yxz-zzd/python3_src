

r'''
# test get_num_entities_of_subtree/iter_entities_of_subtree
>>> root = ops.rbt_from_entities(4, '0123')
>>> get_num_entities_of_subtree(root)
4
>>> list_entities(root, reverse=False)
['0', '1', '2', '3']
>>> list_entities(root, reverse=True)
['3', '2', '1', '0']
>>> why_not_subtree_ok(root, as_root=True, strict=True)
()


# test rbt_helper_to_plain/rbt_helper_from_plain
>>> plain = rbt_helper_to_plain(root)
>>> plain
('BLACK', '1', ('BLACK', '0', (), ()), ('BLACK', '2', (), ('RED', '3', (), ())))
>>> root2 = rbt_helper_from_plain(plain)
>>> why_not_subtree_ok(root2, as_root=True, strict=True)
()
>>> plain2 = rbt_helper_to_plain(root2)
>>> plain2
('BLACK', '1', ('BLACK', '0', (), ()), ('BLACK', '2', (), ('RED', '3', (), ())))


# test get_left_child/get_right_child
>>> root_left = ops.get_left_child(root)
>>> root_left_right = ops.get_right_child(root_left)
>>> root_right = ops.get_right_child(root)
>>> root_right_right = ops.get_right_child(root_right)
>>> rbt_helper_to_plain(root_left)
('BLACK', '0', (), ())
>>> rbt_helper_to_plain(root_right)
('BLACK', '2', (), ('RED', '3', (), ()))
>>> (root_left, root_right) == tuple(ops.iter_children(root))
True


# test rbt_helper_to_direction_path
>>> rbt_helper_to_direction_path(root)
[]
>>> rbt_helper_to_direction_path(root_left)
['LEFT']
>>> rbt_helper_to_direction_path(root_left_right)
['LEFT', 'RIGHT']
>>> rbt_helper_to_direction_path(root_right)
['RIGHT']
>>> rbt_helper_to_direction_path(root_right_right)
['RIGHT', 'RIGHT']


# test is_leaf/is_nonleaf
>>> is_leaf(root)
False
>>> is_leaf(root_left)
False
>>> is_leaf(root_left_right)
True

>>> ops.is_nonleaf(root)
True
>>> ops.is_nonleaf(root_left)
True
>>> ops.is_nonleaf(root_left_right)
False


# test is_root/is_nonroot
>>> is_root(root)
True
>>> is_root(root_left)
False
>>> is_root(root_left_right)
False

>>> ops.is_nonroot(root)
False
>>> ops.is_nonroot(root_left)
True
>>> ops.is_nonroot(root_left_right)
True


# test is_RED/is_BLACK/get_the_color
>>> _B = ops.get_the_color(root)
>>> _B == ops.get_the_color(root_left_right)
True
>>> _R = ops.get_the_color(root_right_right)
>>> is_RED(_R)
True
>>> is_RED(_B)
False
>>> ops.is_BLACK(_R)
False
>>> ops.is_BLACK(_B)
True


# test is_red_node/is_black_node
>>> is_red_node(root)
False
>>> is_red_node(root_left_right)
False
>>> is_red_node(root_right)
False
>>> is_red_node(root_right_right)
True

>>> ops.is_black_node(root)
True
>>> ops.is_black_node(root_left_right)
True
>>> ops.is_black_node(root_right)
True
>>> ops.is_black_node(root_right_right)
False


# test is_LEFT/is_RIGHT
>>> L = ops.get_direction(root_left)
>>> R = ops.get_direction(root_right)
>>> is_LEFT(L)
True
>>> is_LEFT(R)
False

>>> ops.is_RIGHT(L)
False
>>> ops.is_RIGHT(R)
True


# test get_parent
>>> root3 = get_parent(root_left)
>>> rbt_helper_to_plain(root3) == rbt_helper_to_plain(root)
True

# test get_num_entities_of_subtree
>>> get_num_entities_of_subtree(root_left)
1
>>> get_num_entities_of_subtree(root_left_right)
0
>>> get_num_entities_of_subtree(root_right)
2
>>> get_num_entities_of_subtree(root_right_right)
1

# test get_num_entities_of_nonleaf/get_num_children
>>> ops.get_num_entities_of_nonleaf(root)
1
>>> ops.get_num_children(root)
2

'''

from .test_KeyOrderedRedBlackTreeNodeOps__sized_immutable__common import \
    (KeyOrderedRedBlackTreeNodeOps__sized_immutable
    ,simple_KRBT_SI

    ,This
    ,ops
    ,is_leaf
    ,is_root
    ,is_RED
    ,is_red_node
    ,is_LEFT
    ,get_parent

    ,rbt_from_entities
    ,rbt_helper_to_plain
    ,rbt_helper_from_plain
    ,rbt_helper_to_direction_path
    ,iter_entities_of_subtree
    ,get_num_entities_of_subtree
    ,why_not_subtree_ok

    ,list_entities
    )



plain = ('BLACK', '1', ('BLACK', '0', (), ()), ('BLACK', '2', (), ('RED', '3', (), ())))
root2 = rbt_helper_from_plain(plain)
#why_not_subtree_ok(root2, as_root=True, strict=True)
plain2 = rbt_helper_to_plain(root2)
assert plain2 == plain


if __name__ == "__main__":
    import doctest
    doctest.testmod()




