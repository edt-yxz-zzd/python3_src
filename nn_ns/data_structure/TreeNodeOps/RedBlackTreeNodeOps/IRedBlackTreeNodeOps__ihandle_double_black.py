

__all__ = '''
    red_black_tree__ihandle_double_black
'''.split()


from .IRedBlackTreeNodeOps__itrinode_restructure import \
    red_black_tree__itrinode_restructure


'''
    __find_if
    __remove__red_sibling
    __remove__black_sibling_and_no_red_nephews
    __remove__black_sibling_and_a_red_nephew
'''

def __find_if(pred, iterable):
    for x in iterable:
        if pred(x):
            return x
    raise ValueError('not found')


if False:
    is_black_node = ops.is_black_node
    is_red_node = ops.is_red_node
    is_root = ops.is_root
    refresh_up = ops.refresh_up
    get_sibling = ops.get_sibling
    is_leaf = ops.is_leaf
    irecolor = ops.irecolor
    iter_children = ops.iter_children
    fixed_the_only_broken_above_until_root = ops.fixed_the_only_broken_above_until_root
    if __remove__red_sibling:
        is_red_node = ops.is_red_node
        get_direction = ops.get_direction
        irecolor = ops.irecolor
        refresh_up = ops.refresh_up
        iter_refresh_downs = ops.iter_refresh_downs
        get_child_at = ops.get_child_at
    elif __remove__black_sibling_and_no_red_nephews:
        irecolor = ops.irecolor
        is_red_node = ops.is_red_node
        refresh_up = ops.refresh_up
    elif __remove__black_sibling_and_a_red_nephew:
        is_black_node = ops.is_black_node
        get_the_color = ops.get_the_color
        refresh_up = ops.refresh_up
        iset_the_color = ops.iset_the_color
        BLACK = ops.get_BLACK()


def red_black_tree__ihandle_double_black(ops, me):
    '''
precondition:
    root.is_black()
    allow old2new broken above (maybe parent), me
return root, is_root_double_black
postcondition:
    root may be black or double_black

'''
    is_black_node = ops.is_black_node
    is_red_node = ops.is_red_node
    is_root = ops.is_root
    refresh_up = ops.refresh_up
    iter_refresh_downs = ops.iter_refresh_downs
    get_direction = ops.get_direction
    get_sibling = ops.get_sibling
    is_leaf = ops.is_leaf
    irecolor = ops.irecolor
    iter_children = ops.iter_children
    fixed_the_only_broken_above_until_root = ops.fixed_the_only_broken_above_until_root



    is_root_double_black = False
    is_me_double_black = True

    while is_me_double_black:
        assert is_black_node(me) # indeed double black


        # old2new broken above (maybe parent), me
        #   maybe parent from maybe grandpa when "me:=parent" see below

        if is_root(me):
            is_root_double_black = is_me_double_black # for output

            # color me black ; ...
            is_me_double_black = False
            #break
            continue


        parent = refresh_up(me)
        # old2new broken above parent
        me, = iter_refresh_downs(parent, get_direction(me))

        sibling = get_sibling(me)
        # me double black ==>> me maybe a leaf
        #                 ==>> sibling should not be a leaf
        assert not is_leaf(sibling)

        if is_red_node(sibling):
            #assert not is_leaf(sibling)
            # ==>> parent and nephews are all black

            # old2new broken above parent
            parent, sibling, me = __remove__red_sibling(ops, parent, sibling, me)
            # old2new broken above grandpa
            assert is_black_node(sibling)


        # old2new broken above (parent or grandpa)
        #   source:
        #      <- old2new broken above parent
        #      <- old2new broken above grandpa
        assert is_black_node(sibling)

        nephews = tuple(iter_children(sibling))
        # if both nephews are black:
        if all(map(is_black_node, nephews)):
            # old2new broken above (parent or grandpa)
            parent, is_parent_double_black = __remove__black_sibling_and_no_red_nephews(ops, parent, me, sibling)
            del me, sibling
            # old2new broken above (maybe grandpa), parent
            # [BLACK me]

        else:
            # old2new broken above (parent or grandpa)
            # assert exists a red_nephew
            red_nephew = __find_if(is_red_node, nephews)
            parent, is_parent_double_black = __remove__black_sibling_and_a_red_nephew(ops, parent, me, sibling, red_nephew)
            del me, sibling, red_nephew
            # old2new broken above (maybe grandpa), parent
            # [BLACK me]


        # old2new broken above (maybe grandpa), parent
        me = parent ; del parent
        # old2new broken above (maybe parent), me
        is_me_double_black = is_parent_double_black
        continue

    # old2new broken above (maybe parent), me
    if is_root(me):
        # no parent
        pass
        # old2new broken above me
    else:
        parent = refresh_up(me)
        # old2new broken above parent
        me = parent ; del parent
        # old2new broken above me


    # old2new broken above me
    root = fixed_the_only_broken_above_until_root(me)
    # old2new broken above root
    # ignore old2new broken above root
    assert is_black_node(root)
    return root, is_root_double_black




def __remove__red_sibling(ops, parent, sibling, me):
        '''
precondition:
    [old2new broken above parent]
    [RED sibling] ==>> parent and nephews are all black
    [DOUBLE_BLACK me]

return:
    parent, sibling, me

postconditon:
    [old2new broken above grandpa]
    [DOUBLE_BLACK me]
    [BLACK sibling]
    [OLD grandpa, uncle, parent, sibling, me]

'''
        is_red_node = ops.is_red_node
        is_black_node = ops.is_black_node
        get_direction = ops.get_direction
        irecolor = ops.irecolor
        refresh_up = ops.refresh_up
        iter_refresh_downs = ops.iter_refresh_downs
        get_child_at = ops.get_child_at
        get_sibling = ops.get_sibling



        # old2new broken above parent
        is_me_double_black = True

        assert is_red_node(sibling)
        #assert not is_leaf(sibling)
        #assert not is_root(sibling)
        # [RED sibling] ==>> parent and nephews are all black
        # if sibling is left child, same-direct-nephew is left child
        # if right, then right
        # other-nephew between same-direct-nephew and me

        del me
        sibling_direction = get_direction(sibling)
        sibling = irecolor(sibling)# -> BLACK
        # old2new broken above parent, sibling
        parent = refresh_up(sibling)
        # old2new broken above parent
        del sibling
        parent = irecolor(parent) # -> RED
        sibling, same_direction_nephew = iter_refresh_downs(
            parent, sibling_direction, sibling_direction)

        node = red_black_tree__itrinode_restructure(ops, same_direction_nephew)
        del sibling, same_direction_nephew
        # the result node take place of old parent, be child of old grandpa
        # but result node is now parent of old parent
        #     and old parent is still my parent
        grandpa = node ; del node
        # old2new broken above grandpa

        uncle = get_child_at(grandpa, sibling_direction)
        parent = get_sibling(uncle)
        sibling = get_child_at(parent, sibling_direction)
        me = get_sibling(sibling)


        #      sibling:black -> {parent:red, same-direct-nephew:black}
        assert is_black_node(grandpa) # <- old sibling:RED
        assert is_black_node(uncle)   # <- old same_direction_nephew
        assert is_red_node(parent)    # <- old parent:BLACK # my parent not changed
        assert is_black_node(sibling) # <- old other_nephew
        assert is_me_double_black # <- old me


        # now, sibling is black!!
        # but old2new broken above grandpa
        return parent, sibling, me

def __remove__black_sibling_and_no_red_nephews(ops, parent, me, sibling):
        '''
precondition:
    [old2new broken above (parent or grandpa)]
    [BLACK sibling]
    [ALL . BLACK nephews]
    [DOUBLE_BLACK me]

return:
    parent, is_parent_double_black

postconditon:
    [old2new broken above (maybe grandpa), parent]
    [BLACK me]
    [OLD parent, me, sibling]

'''
        irecolor = ops.irecolor
        is_red_node = ops.is_red_node
        refresh_up = ops.refresh_up



    # old2new broken above (parent or grandpa)
      # extract black
        # color me black <- double black
        # color sibling red <- black
        is_me_double_black = False
        sibling = irecolor(sibling)
        # old2new broken above (parent or grandpa), sibling
        parent = refresh_up(sibling)
        # old2new broken above (parent or grandpa), parent; new2old broken above me
        # old2new broken above (maybe grandpa), parent; new2old broken above me
        del me, sibling
        # old2new broken above (maybe grandpa), parent

      # assign black
        if is_red_node(parent):
            # color parent black <- red
            is_parent_double_black = False
            parent = irecolor(parent)
            # old2new broken above (maybe grandpa), parent
        else:
            # color parent double black <- black
            is_parent_double_black = True
        # old2new broken above (maybe grandpa), parent

        return parent, is_parent_double_black
        #continue

def __remove__black_sibling_and_a_red_nephew(ops, parent, me, sibling, red_nephew):
        '''
precondition:
    [old2new broken above (parent or grandpa)]
    [BLACK sibling]
    [RED red_nephew]
    [DOUBLE_BLACK me]

return:
    parent, is_parent_double_black

postconditon:
    [old2new broken above (maybe grandpa), parent]
    [BLACK me]
    [OLD parent, me, sibling, red_nephew]

'''
        # old2new broken above (parent or grandpa)
        # assert exists a red_nephew


##        - parent:grey -> {me:double_black, sibling:black->{.., red_nephew:red}}
##        NOTE:
##            # assume red = 0, black = 1, grey = 0 or 1
##            # all outgoings:
##            me:double_black <- grey = 2 + grey
##            other_nephew:self <- black <- grey = self + 1 + grey
##            children of red_nephew : self <- red <- black <- grey = self + 1 + grey
##

        is_black_node = ops.is_black_node
        get_the_color = ops.get_the_color
        refresh_up = ops.refresh_up
        iter_refresh_downs = ops.iter_refresh_downs
        get_direction = ops.get_direction
        iset_the_color = ops.iset_the_color
        irecolor = ops.irecolor
        BLACK = ops.get_BLACK()



        # old2new broken above (parent or grandpa)
        # color parent, me, sibling, red_nephew -> all black
        is_me_double_black = False
        assert is_black_node(me)
        assert is_black_node(sibling)
        grey = get_the_color(parent) # save color
        red_nephew = irecolor(red_nephew) # -> BLACK
        recolored_red_nephew = red_nephew; del red_nephew
        # old2new broken above (parent or grandpa), recolored_red_nephew
        sibling = refresh_up(recolored_red_nephew)
        # old2new broken above (parent or grandpa), sibling; new2old: recolored_red_nephew
        parent = refresh_up(sibling)
        # old2new broken above (maybe grandpa), parent; new2old: sibling, recolored_red_nephew
        parent = iset_the_color(parent, BLACK)
        # old2new broken above (maybe grandpa), parent; new2old: sibling, recolored_red_nephew
        sibling, recolored_red_nephew = iter_refresh_downs(parent
            , get_direction(sibling), get_direction(recolored_red_nephew))
        # old2new broken above (maybe grandpa), parent



        parent = red_black_tree__itrinode_restructure(ops, recolored_red_nephew)
        del sibling, recolored_red_nephew, me # they are all invalid, since the struct changes
        # old2new broken above (maybe grandpa), parent
        parent = iset_the_color(parent, grey) # restore color
        is_parent_double_black = False
        # old2new broken above (maybe grandpa), parent


##        - s_n_A:grey -> {parent:black->{me:black, ..}, s_n_B:black->{..}}
##        - s_n_X = sibling or red_nephew
##        NOTE:
##            # all outgoings not changed!!
##            me:black <- black <- grey = 2 + grey
##            other_nephew:self <- black <- grey = self + 1 + grey
##            children of red_nephew : self <- black <- grey = self + 1 + grey


        return parent, is_parent_double_black
        #continue




