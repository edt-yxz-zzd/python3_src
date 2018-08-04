

__all__ = '''
    red_black_tree__iremove_leaf_and_its_parent_ex
    red_black_tree__iremove_leaf_and_its_parent
'''.split()


from .IRedBlackTreeNodeOps__ihandle_double_black import \
    red_black_tree__ihandle_double_black


if False:
    is_black_node = ops.is_black_node
    is_leaf = ops.is_leaf
    is_root = ops.is_root
    fixed_the_only_broken_above_until_root = ops.fixed_the_only_broken_above_until_root

    get_parent = ops.get_parent
    get_sibling = ops.get_sibling
    get_parent_info = ops.get_parent_info
    basic_iset_parent_info = ops.basic_iset_parent_info
    irecolor = ops.irecolor


def red_black_tree__iremove_leaf_and_its_parent(ops, leaf):
    root, is_root_double_black = \
        red_black_tree__iremove_leaf_and_its_parent_ex(ops, leaf)
    return root


def red_black_tree__iremove_leaf_and_its_parent_ex(ops, leaf):
    '''
precondition:
    root.is_black()
    self.is_leaf()
    self.is_nonroot()
return root, is_root_double_black
postcondition:
    root may be black or double_black
'''
    self = leaf
    is_black_node = ops.is_black_node
    is_leaf = ops.is_leaf
    is_root = ops.is_root
    fixed_the_only_broken_above_until_root = ops.fixed_the_only_broken_above_until_root

    assert is_leaf(self)
    assert not is_root(self)

    leaf = self; del self
    me, is_me_double_black = \
        __remove__raw__node_with_zombie_entity_and_an_leaf_child(ops, leaf)
    del leaf
    assert is_black_node(me)

    # broken above me
    if is_me_double_black:
        # double black : me contain two black!! since nonleaf was removed
        #assert is_black_node(me) # indeed double black

        xprint(">>>>>>>>>>>>>>>")
        # old2new broken above me
        root, is_root_double_black = red_black_tree__ihandle_double_black(ops, me)
    else:
        is_root_double_black = False
        #assert is_black_node(me) # me may be root; that is fine
        root = fixed_the_only_broken_above_until_root(me)
    assert is_black_node(root)
    return root, is_root_double_black


def __remove__raw__node_with_zombie_entity_and_an_leaf_child(ops, leaf_child):
    is_leaf = ops.is_leaf
    is_root = ops.is_root
    get_parent = ops.get_parent
    get_sibling = ops.get_sibling
    get_parent_info = ops.get_parent_info
    basic_iset_parent_info = ops.basic_iset_parent_info
    is_black_node = ops.is_black_node
    is_red_node = ops.is_red_node
    irecolor = ops.irecolor



    if not is_leaf(leaf_child): raise ValueError('not a leaf')
    if is_root(leaf_child): raise ValueError('a root has no parent')

    nonleaf = get_parent(leaf_child)

    xprint('leaf_child', leaf_child)
    me = get_sibling(leaf_child) # me may be a leaf !!
    is_double_black = is_black_node(nonleaf) and is_black_node(me)

    assert is_black_node(nonleaf) or is_black_node(me)

    # bug: forgot color me black
    # -> BLACK
    if is_red_node(me):
        # not leaf
        me = irecolor(me) # red->black
        # old2new broken above me
    assert is_black_node(me)

    # remove nonleaf, leaf_child
    # replace nonleaf by me ==>> me.parent = nonleaf.parent
    #
    parent_info = get_parent_info(nonleaf)
    me = basic_iset_parent_info(me, parent_info)
    # old2new broken above me
    del leaf_child, nonleaf

    is_me_double_black = is_double_black # since nonleaf removed, me bears more
    del is_double_black


    assert is_black_node(me)
    xprint('me', me)
    xprint('is_me_double_black', is_me_double_black)
    # old2new broken above me
    return me, is_me_double_black

def xprint(*args):
    return
    print(*args)

