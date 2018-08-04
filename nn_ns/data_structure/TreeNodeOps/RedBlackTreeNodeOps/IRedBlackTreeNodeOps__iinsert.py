
__all__ = '''
    red_black_tree__iinsert_entity_at_leaf
    '''.split()

from .IRedBlackTreeNodeOps__itrinode_restructure import \
    red_black_tree__itrinode_restructure__for_double_red_when_uncle_is_black

def xprint(*args):pass
def red_black_tree__iinsert_entity_at_leaf(ops, leaf, entity):
    # -> root
    # if this is an ordered tree,
    # then leaf should be between find_range(root, key);
    # otherwise this call will disrupt order

    self = leaf
    is_leaf = ops.is_leaf
    make_bare_red_nonleaf = ops.make_bare_red_nonleaf
    get_maybe_parent_direction = ops.get_maybe_parent_direction
    fixed_the_only_broken_above_until_root = ops.fixed_the_only_broken_above_until_root

    is_red_node = ops.is_red_node
    is_black_node = ops.is_black_node
    is_root = ops.is_root
    refresh_up = ops.refresh_up
    iter_refresh_downs = ops.iter_refresh_downs
    get_sibling = ops.get_sibling
    irecolor = ops.irecolor
    iter_children = ops.iter_children
    iset_children = ops.iset_children
    get_direction = ops.get_direction
    get_parent = ops.get_parent

    assert is_leaf(self)
    leaf = self

    # replace u by red(null, e, null)
    maybe_parent_direction = get_maybe_parent_direction(self)
    me = make_bare_red_nonleaf(maybe_parent_direction, entity)
    xprint('self', self)
    xprint('me', me)
    del leaf, maybe_parent_direction
    # old2new broken above me
    # red root | double red | parent black OK


    while True:
        # old2new broken above me
        assert is_red_node(me)
        if is_root(me):
            me = irecolor(me)
            xprint('irecolor me', me)
            break
        parent = refresh_up(me)
        # old2new broken above parent
        # !AND! new2old broken above me
        #   # me.parent may be old parent
        #   #   when node.parent is immutable


        if is_black_node(parent):
            me = parent
            xprint('is_black_node me', me)
            # old2new broken above me
            #   # discard old me
            break

        # double-red ::= parent and me are both red
        assert not is_root(parent)

        me, = iter_refresh_downs(parent, get_direction(me))
        xprint('iter_refresh_downs me', me)
        # old2new broken above grandpa
        # !AND! new2old broken above parent

        assert is_black_node(get_parent(parent))
        uncle = get_sibling(parent)


        if is_black_node(uncle):
##            ==>> children of (grandpa, parent, me) exclude these 3
##                    are all black;
##                 total 4 (my 2 children + sibling + uncle)
##
##            -              grandpa:black
##            - uncle:black,                       parent:red
##            -                      sibling:black,            me:red
##            -                                        lchild:black, rchild:black

            grandpa = red_black_tree__itrinode_restructure__for_double_red_when_uncle_is_black(ops, me)
            del parent, uncle, me # they are all invalid, since the struct changes
            # old2new broken above grandpa

            me = grandpa; del grandpa
            xprint('grandpa me', me)
            # old2new broken above me

            break
##                black -> {red, red}
##                the above 2 reds -> the 4 black others
##
##            -                              g_p_m_1:black
##            -           g_p_m_0:red,                          g_p_m_2:red
##            - u_s_l_r_0:black, u_s_l_r_1:black     u_s_l_r_2:black, u_s_l_r_3:black,
##            - # g_p_m_i is one of (grandpa, parent, me)
##            - # u_s_l_r_i is one of (uncle, sibling, lchild, rchild)

        else:
            # uncle is red
##            -           grandpa:black
##            - uncle:red,            parent:red
##            -                     ....   me:red
            # irecolor(self, grandpa, parent, uncle)

            grandpa = refresh_up(parent)
            # old2new broken above grandpa
            # !AND! new2old broken above parent
            # !AND! new2old broken above me
            del parent, uncle
            # old2new broken above grandpa

            left, right = iter_children(grandpa)
            left = irecolor(left)
            right = irecolor(right)
            # old2new broken above grandpa, left, right
            grandpa = iset_children(grandpa, [left, right])
            del left, right # to ignore the new2old broken points above them
            # old2new broken above grandpa
            grandpa = irecolor(grandpa) # -> red
            # old2new brken above grandpa
            assert is_red_node(grandpa)

##
##            -           grandpa:red
##            - uncle:black,          parent:black
##            -                     ....   me:red


            me = grandpa
            xprint('me=grandpa continue', me)
            # old2new broken above me
            continue

    # old2new broken above me

    assert is_black_node(me)

    root = fixed_the_only_broken_above_until_root(me); del me

    # old2new broken above root
    # ignore old2new broken above root
    return root


