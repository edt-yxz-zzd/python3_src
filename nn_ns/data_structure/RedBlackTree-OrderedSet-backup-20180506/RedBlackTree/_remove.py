

__all__ = '''
    remove_leaf_and_its_parent_ex
    remove_leaf_and_its_parent

    remove_entity_at_nonleaf_ex
    remove_entity_at_nonleaf
'''.split()




def remove_leaf_and_its_parent(leaf):
    root, is_root_double_black = remove_leaf_and_its_parent_ex(leaf)
    return root

def remove_entity_at_nonleaf(nonleaf,
                             child_leaf_first=True,
                             prefer_succ_leaf=True):
    '''
1) if child_leaf_first ==>>
    if there is a child leaf, remove it and self
    else goto 2)
2) leaf = self.succ_leaf() if prefer_succ_leaf else self.prev_leaf()
    swap self.entity and leaf.parent.entity
    remove leaf and its parent
return new_root
'''
    root, is_root_double_black = remove_entity_at_nonleaf_ex(
        nonleaf, child_leaf_first, prefer_succ_leaf)
    return root


def remove_entity_at_nonleaf_ex(nonleaf,
                                child_leaf_first=True,
                                prefer_succ_leaf=True):
    'return root, is_root_double_black'
    assert isinstance(nonleaf, MutableRedBlackTreeNodeABC)
    assert not nonleaf.is_leaf()

    if child_leaf_first and any(child.is_leaf() for child in nonleaf.children):
        if all(child.is_leaf() for child in nonleaf.children):
            leaf = nonleaf.right if prefer_succ_leaf else nonleaf.left
        else:
            leaf = nonleaf.right if nonleaf.right.is_leaf() else nonleaf.left

        return remove_leaf_and_its_parent_ex(leaf)
    elif prefer_succ_leaf:
        return remove_entity_at_nonleaf_with_succ_leaf_ex(nonleaf)
    else:
        return remove_entity_at_nonleaf_with_prev_leaf_ex(nonleaf)

def remove_entity_at_nonleaf_with_succ_leaf_ex(nonleaf):
    assert isinstance(nonleaf, MutableRedBlackTreeNodeABC)
    assert not nonleaf.is_leaf()
    right = nonleaf.right
    if right.is_leaf():
        leaf = right
        return remove_leaf_and_its_parent_ex(leaf)

    succ_leaf = nonleaf.nonleaf_inorder_succ_leaf()
    nonleaf.entity = succ_leaf.parent.entity
    # broken above nonleaf; new2old broken below nonleaf
    succ_leaf_gettor = type(nonleaf).nonleaf_inorder_succ_leaf
    return __remove_leaf_and_its_parent_ex__in_subtree(nonleaf, succ_leaf_gettor)

def remove_entity_at_nonleaf_with_prev_leaf_ex(nonleaf):
    assert isinstance(nonleaf, MutableRedBlackTreeNodeABC)
    assert not nonleaf.is_leaf()
    left = nonleaf.left
    if right.is_leaf():
        leaf = left
        return remove_leaf_and_its_parent_ex(leaf)

    prev_leaf = nonleaf.nonleaf_inorder_prev_leaf()
    nonleaf.entity = prev_leaf.parent.entity
    # broken above nonleaf; new2old broken below nonleaf
    prev_leaf_gettor = type(nonleaf).nonleaf_inorder_prev_leaf
    return __remove_leaf_and_its_parent_ex__in_subtree(nonleaf, prev_leaf_gettor)

def __remove_leaf_and_its_parent_ex__in_subtree(subtree_root, leaf_gettor):
    'postcondition: broken above result_subtree'
    # split out subtree
    if subtree_root.is_red():
        assert subtree_root.is_nonroot()
        black_count = 0
        subtree_root.recolor()
    else:
        black_count = 1

    assert subtree_root.is_black() # make sure this is really a rb tree
    org_subtree_pos = subtree_root.parent_info # save
    # bug: subtree_root.parent_info = subtree_root.new_ROOT_PARENT_INFO
    subtree_root.parent_info = subtree_root.new_ROOT_PARENT_INFO()

    # remove
    leaf = leaf_gettor(subtree_root)
    subtree_root, is_subtree_root_double_black = remove_leaf_and_its_parent_ex(leaf)
    assert subtree_root.is_black()

    black_count += bool(is_subtree_root_double_black)
    assert black_count in (0, 1, 2)
    if black_count == 0:
        assert subtree_root.is_nonroot() # since its org color is red
        subtree_root.recolor() # -> RED, hence not org tree root
        assert subtree_root.is_red()

    if black_count == 0:
        assert not is_subtree_root_double_black
        is_subtree_root_double_black = False
    elif black_count == 1:
        is_subtree_root_double_black = False
    else:
        assert is_subtree_root_double_black
        assert black_count == 2
        is_subtree_root_double_black = True

    # broken above subtree_root
    # return subtree_root, is_subtree_root_double_black

    # join back subtree
    subtree_root.parent_info = org_subtree_pos # restore
    if is_subtree_root_double_black:
        root, is_root_double_black = handle_double_black(subtree_root)
    else:
        assert subtree_root.is_nonroot() or subtree_root.is_black()
        # subtree_root may be root; that is fine
        root = subtree_root.fixed_the_only_broken_above_until_root()
        is_root_double_black = False
    assert root.is_black()
    return root, is_root_double_black










def remove_leaf_and_its_parent_ex(leaf):
    '''
precondition:
    root.is_black()
return root, is_root_double_black
postcondition:
    root may be black or double_black

'''
    assert leaf.is_leaf()
    assert not leaf.is_root()
    me, is_me_double_black = __remove__raw__node_with_zombie_entity_and_an_leaf_child(
                                leaf)
    assert me.is_black()

    # broken above me
    if is_me_double_black:
        # double black : me contain two black!! since nonleaf was removed
        assert me.is_black() # indeed double black

        # broken above me
        root, is_root_double_black = handle_double_black(me)
    else:
        is_root_double_black = False
        assert me.is_black() # me may be root; that is fine
        root = me.fixed_the_only_broken_above_until_root()
    assert root.is_black()
    return root, is_root_double_black


def __find_if(pred, iterable):
    for x in iterable:
        if pred(x):
            return x
    return ValueError('not found')
def handle_double_black(me):
    '''
precondition:
    root.is_black()
    allow broken above (maybe parent), me
return root, is_root_double_black
postcondition:
    root may be black or double_black

'''
    is_root_double_black = False
    is_me_double_black = True
    while is_me_double_black:
        assert me.is_black() # indeed double black


        # broken above (maybe parent), me
        #   maybe parent from maybe grandpa when "me:=parent" see below

        if me.is_root():
            is_root_double_black = is_me_double_black # for output

            # color me black ; ...
            is_me_double_black = False
            continue


        parent = me.refresh_up()
        # broken above parent
        sibling = me.sibling
        # me double black ==>> me maybe a leaf
        #                 ==>> sibling should not be a leaf
        assert not sibling.is_leaf()

        if sibling.is_red():
            assert not sibling.is_leaf()
            # ==>> parent and nephews are all black

            # broken above parent
            parent, sibling, me = __remove__red_sibling(parent, sibling, me)
            # broken above grandpa
            assert sibling.is_black()


        # broken above (parent or grandpa)
        #   source:
        #      <- broken above parent
        #      <- broken above grandpa
        assert sibling.is_black()

        nephews = sibling.children
        # if both nephews are black:
        if all(nephew.is_black() for nephew in nephews):
            # broken above (parent or grandpa)
            parent, is_parent_double_black = __remove__black_sibling_and_no_red_nephews(parent, me, sibling)
            del me, sibling
            # broken above (maybe grandpa), parent
            # [BLACK me]

        else:
            # broken above (parent or grandpa)
            # assert exists a red_nephew
            red_nephew = __find_if(type(me).is_red, nephews)
            parent, is_parent_double_black = __remove__black_sibling_and_a_red_nephew(parent, me, sibling, red_nephew)
            del me, sibling, red_nephew
            # broken above (maybe grandpa), parent
            # [BLACK me]


        # broken above (maybe grandpa), parent
        me = parent ; del parent
        # broken above (maybe parent), me
        is_me_double_black = is_parent_double_black
        continue

    # broken above (maybe parent), me
    if me.is_root():
        # no parent
        pass
        # broken above me
    else:
        parent = me.refresh_up()
        # broken above parent
        me = parent ; del parent
        # broken above me


    # broken above me
    root = me.fixed_the_only_broken_above_until_root()
    # broken above root
    # ignore broken above root
    assert root.is_black()
    return root, is_root_double_black


def __remove__raw__node_with_zombie_entity_and_an_leaf_child(
    leaf_child):
    if not leaf_child.is_leaf():
        raise ValueError('not a leaf')
    if leaf_child.is_root():
        raise ValueError('a root has no parent')
    nonleaf = leaf_child.parent

    me = leaf_child.sibling # me may be a leaf !!
    is_double_black = nonleaf.is_black() and me.is_black()

    # bug: forgot color me black
    assert nonleaf.is_black() or me.is_black()
    # -> BLACK
    if me.is_red():
        me.recolor()

    # remove nonleaf, leaf_child
    # replace nonleaf by me ==>> me.parent = nonleaf.parent
    #
    me.parent_info = nonleaf.parent_info
    # broken above me
    del leaf_child, nonleaf

    is_me_double_black = is_double_black # since nonleaf removed, me bears more
    del is_double_black


    # broken above me
    assert me.is_black()
    return me, is_me_double_black



def __remove__red_sibling(parent, sibling, me):
        '''
precondition:
    [broken above parent]
    [RED sibling] ==>> parent and nephews are all black
    [DOUBLE_BLACK me]

return:
    parent, sibling, me

postconditon:
    [broken above grandpa]
    [DOUBLE_BLACK me]
    [BLACK sibling]
    [OLD grandpa, uncle, parent, sibling, me]

'''
        # broken above parent
        is_me_double_black = True
        assert not sibling.is_leaf()
        # [RED sibling] ==>> parent and nephews are all black
        # if sibling is left child, same-direct-nephew is left child
        # if right, then right
        # other-nephew between same-direct-nephew and me

        del me
        sibling_direction = sibling.direction
        sibling.recolor()# -> BLACK
        # broken above parent, sibling
        parent = sibling.refresh_up()
        # broken above parent
        del sibling
        parent.recolor() # -> RED
        sibling, same_direction_nephew = parent.refresh_downs(
            sibling_direction, sibling_direction)

        node = same_direction_nephew.trinode_restructure()
        del sibling, same_direction_nephew
        # the result node take place of old parent, be child of old grandpa
        # but result node is now parent of old parent
        #     and old parent is still my parent
        grandpa = node ; del node
        # broken above grandpa

        uncle = grandpa.get_child(sibling_direction)
        parent = uncle.sibling
        sibling = parent.get_child(sibling_direction)
        me = sibling.sibling


        #      sibling:black -> {parent:red, same-direct-nephew:black}
        assert grandpa.is_black() # <- old sibling:RED
        assert uncle.is_black()   # <- old same_direction_nephew
        assert parent.is_red()    # <- old parent:BLACK # my parent not changed
        assert sibling.is_black() # <- old other_nephew
        assert is_me_double_black # <- old me


        # now, sibling is black!!
        # but broken above grandpa
        return parent, sibling, me

def __remove__black_sibling_and_no_red_nephews(parent, me, sibling):
        '''
precondition:
    [broken above (parent or grandpa)]
    [BLACK sibling]
    [ALL . BLACK nephews]
    [DOUBLE_BLACK me]

return:
    parent, is_parent_double_black

postconditon:
    [broken above (maybe grandpa), parent]
    [BLACK me]
    [OLD parent, me, sibling]

'''
    # broken above (parent or grandpa)
      # extract black
        # color me black <- double black
        # color sibling red <- black
        is_me_double_black = False
        sibling.recolor()
        # broken above (parent or grandpa), sibling
        parent = sibling.refresh_up()
        # broken above (parent or grandpa), parent; new2old broken above me
        # broken above (maybe grandpa), parent; new2old broken above me
        del me, sibling
        # broken above (maybe grandpa), parent

      # assign black
        if parent.is_red():
            # color parent black <- red
            is_parent_double_black = False
            parent.recolor()
            # broken above (maybe grandpa), parent
        else:
            # color parent double black <- black
            is_parent_double_black = True
        # broken above (maybe grandpa), parent

        return parent, is_parent_double_black
        #continue

def __remove__black_sibling_and_a_red_nephew(parent, me, sibling, red_nephew):
        '''
precondition:
    [broken above (parent or grandpa)]
    [BLACK sibling]
    [RED red_nephew]
    [DOUBLE_BLACK me]

return:
    parent, is_parent_double_black

postconditon:
    [broken above (maybe grandpa), parent]
    [BLACK me]
    [OLD parent, me, sibling, red_nephew]

'''
        # broken above (parent or grandpa)
        # assert exists a red_nephew


##        - parent:grey -> {me:double_black, sibling:black->{.., red_nephew:red}}
##        NOTE:
##            # assume red = 0, black = 1, grey = 0 or 1
##            # all outgoings:
##            me:double_black <- grey = 2 + grey
##            other_nephew:self <- black <- grey = self + 1 + grey
##            children of red_nephew : self <- red <- black <- grey = self + 1 + grey
##

        # broken above (parent or grandpa)
        # color parent, me, sibling, red_nephew -> all black
        is_me_double_black = False
        assert me.is_black()
        assert sibling.is_black()
        grey = parent.color # save color
        red_nephew.recolor() # -> BLACK
        recolored_red_nephew = red_nephew; del red_nephew
        # broken above (parent or grandpa), recolored_red_nephew
        sibling = recolored_red_nephew.refresh_up()
        # broken above (parent or grandpa), sibling; new2old: recolored_red_nephew
        parent = sibling.refresh_up()
        # broken above (maybe grandpa), parent; new2old: sibling, recolored_red_nephew
        parent.color = parent.BLACK
        # broken above (maybe grandpa), parent; new2old: sibling, recolored_red_nephew
        sibling, recolored_red_nephew = parent.refresh_downs(
            sibling.direction, recolored_red_nephew.direction)
        # broken above (maybe grandpa), parent



        parent = recolored_red_nephew.trinode_restructure()
        del sibling, recolored_red_nephew, me # they are all invalid, since the struct changes
        # broken above (maybe grandpa), parent
        parent.color = grey # restore color
        is_parent_double_black = False
        # broken above (maybe grandpa), parent


##        - s_n_A:grey -> {parent:black->{me:black, ..}, s_n_B:black->{..}}
##        - s_n_X = sibling or red_nephew
##        NOTE:
##            # all outgoings not changed!!
##            me:black <- black <- grey = 2 + grey
##            other_nephew:self <- black <- grey = self + 1 + grey
##            children of red_nephew : self <- black <- grey = self + 1 + grey


        return parent, is_parent_double_black
        #continue





















# cyclic import
from .RedBlackTreeNodeABC import MutableRedBlackTreeNodeABC





########################### old code

if 0:
    from .TreeNodeABC import BinaryTreeNodeABC, MutableBinaryTreeNodeABC
    from .RedBlackTreeNodeABC import MutableRedBlackTreeNodeABC
    def to_inorder_succ_descendant_nonleaf(self):
        '''
    descendant means me is nonleaf
    descendant_nonleaf means me with some nonleaf children
    succ_descendant_nonleaf means me with nonleaf right child
    '''
    ##    assert isinstance(self, SearchableMultiWayLikeTreeOpsABC)
    ##    assert not self.is_leaf(me)
    ##    nonleaf_entity_pos_to_inorder_succ_leaf
        # TODO: BinaryTreeNodeABC? maybe we can use super() instead...
        assert isinstance(self, BinaryTreeNodeABC)
        assert not self.is_leaf()
        if self.right.is_leaf():
            raise ValueError('me.right_child is a leaf')


        succ_leaf_descendant = nonleaf_to_inorder_succ_leaf(self)
        # succ_nonleaf_descendant, = leaf_to_maybe_inorder_succ_nonleaf(succ_leaf_descendant)

        assert succ_leaf_descendant.is_left()
        succ_nonleaf_descendant = succ_leaf_descendant.parent
        return succ_nonleaf_descendant



    def move_inorder_succ_descendant_entity_to_me(self):
        '''
    descendant means me is nonleaf
    descendant_entity means me with some nonleaf children
    inorder_succ_descendant_entity means me with nonleaf right child

    move means succ_nonleaf_descendant will contain a zombie entity after move
        zombie entity means the only entity method allowed is destructor
        we can copy succ_nonleaf_descendant.entity to me.entity or
            swap succ_nonleaf_descendant.entity and me.entity
        like C++ std::move:
            me.entity = std::move(succ_nonleaf_descendant.entity)
        and succ_nonleaf_descendant will be destroyed soon

    return None
    postcondition:
        broken above self

    '''
        assert isinstance(self, MutableBinaryTreeNodeABC)
        assert not self.is_leaf()

        succ_descendant_nonleaf = to_inorder_succ_descendant_nonleaf(self)
        self.entity = succ_nonleaf_descendant.entity
        # broken above self; and new2old below self
        del succ_descendant_nonleaf
        # broken above self
        return



    def remove_nonleaf(self):
        assert isinstance(self, MutableRedBlackTreeNodeABC)
        assert not self.is_leaf()

        is_org_subtree_root_black = True
        if not any(map(type(self).is_leaf, self.children)):
            # has no external children
            move_inorder_succ_descendant_entity_to_me(self)
            # broken above self

            # cut subtree above self; i.e. let self be root
            org_subtree_parent_info = self.parent_info
            self.parent_info = self.new_ROOT_PARENT_INFO()
            if self.is_red():
                self.recolor()
                is_org_subtree_root_black = False
            # new_root = self
            # broken above new_root
            succ_descendant_nonleaf_with_zombie_entity = to_inorder_succ_descendant_nonleaf(self)

            me_with_zombie_entity = succ_descendant_nonleaf_with_zombie_entity
        else:
            # cut subtree above root
            # new_root = old_root
            org_subtree_parent_info = self.new_ROOT_PARENT_INFO()
            me_with_zombie_entity = self

        # broken above new_root
        org_subtree_parent_info
        self = me_with_zombie_entity # nonleaf to be removed


        assert any(map(type(self).is_leaf, self.children))
        for child in self.children:
            if self.is_leaf(child):
                break
        else:
            raise logic-error

        subtree_root, is_double_black = remove_node_with_zombie_entity_and_an_leaf_child(
            me_with_zombie_entity, child.direction)
        assert subtree_root.is_black()
        subtree_root.parent_info = org_subtree_parent_info
        # broken above subtree_root
        curr_color = is_org_subtree_root_black + bool(is_double_black)
        if curr_color == 0:
            # no black
            assert subtree_root.is_nonroot() # since its org color is red
            subtree_root.recolor() # -> RED
        else:pass

        if curr_color == 2:
            # double black
            root, is_double_black = handle_double_black(subtree_root)
            # broken above root
            del is_double_black
        else:
            assert subtree_root.is_nonroot() or subtree_root.is_black()
            # subtree_root may be root; that is fine
            root = subtree_root.fixed_the_only_broken_above_until_root()
        # broken above root
        # ignore
        return root







    def remove_node_with_zombie_entity_and_an_leaf_child(
        nonleaf, direction_to_leaf_child):
        '''
    precondition:
        root.is_black()
    return root, is_root_double_black
    postcondition:
        root may be black or double_black

    '''
        assert isinstance(nonleaf, MutableRedBlackTreeNodeABC)
        assert not nonleaf.is_leaf()
        leaf_child = nonleaf.get_child(direction_to_leaf_child)
        return remove_leaf_and_its_parent_ex(leaf_child)










