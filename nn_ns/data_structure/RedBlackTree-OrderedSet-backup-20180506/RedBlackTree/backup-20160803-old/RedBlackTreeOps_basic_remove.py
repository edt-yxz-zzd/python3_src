
from .RedBlackTreeOpsABC import RedBlackTreeOpsABC

def to_inorder_succ_descendant_nonleaf(self, me):
    '''
descendant means me is nonleaf
descendant_nonleaf means me with some nonleaf children
succ_descendant_nonleaf means me with nonleaf right child
'''
##    assert isinstance(self, SearchableMultiWayLikeTreeOpsABC)
##    assert not self.is_leaf(me)
##    nonleaf_entity_pos_to_inorder_succ_leaf
    # TODO: RedBlackTreeOpsABC? maybe we can use super() instead...
    assert isinstance(self, RedBlackTreeOpsABC)
    assert not self.is_leaf(me)
    if self.is_leaf(self.to_right(me)):
        raise ValueError('me.right_child is a leaf')

    
    succ_leaf_descendant = nonleaf_to_inorder_succ_leaf(self, me)
    # succ_nonleaf_descendant, = leaf_to_maybe_inorder_succ_nonleaf(succ_leaf_descendant)
    
    assert self.is_left(succ_leaf_descendant)
    succ_nonleaf_descendant = self.to_parent(succ_leaf_descendant)
    return succ_nonleaf_descendant
    


def move_inorder_succ_descendant_entity_to_me(self, me):
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

return new_me, new_succ_nonleaf_descendant_with_zombie_entity

'''
    assert isinstance(self, RedBlackTreeOpsABC)
    assert not self.is_leaf(me)

    succ_descendant_nonleaf = to_inorder_succ_descendant_nonleaf(self, me)
    entity = self.to_entity(succ_nonleaf_descendant)
    me = replace(self, me, entity=entity)
    me = fix_broken_above_me(me)
    succ_descendant_nonleaf_with_zombie_entity = to_inorder_succ_descendant_nonleaf(self, me)
    return me, succ_descendant_nonleaf_with_zombie_entity
    


def remove_nonleaf(self, nonleaf):
    assert isinstance(self, RedBlackTreeOpsABC)
    assert not self.is_leaf(nonleaf)
    
    children = to_children(self, nonleaf)
    if not any(map(self.is_leaf, children)):
        # has no external children
        nonleaf, succ_nonleaf_with_zombie_entity = move_inorder_succ_descendant_entity_to_me(nonleaf)

        me_with_zombie_entity = succ_nonleaf_with_zombie_entity
    else:
        me_with_zombie_entity = nonleaf
    
    children = to_children(self, me_with_zombie_entity)
    assert any(map(self.is_leaf, children))
    for child in children:
        if self.is_leaf(child):
            break
    else:
        raise logic-error

    return remove_node_with_zombie_entity_and_an_leaf_child(
        self, me_with_zombie_entity, to_direction(self, child))


def __find_if(pred, iterable):
    for x in iterable:
        if pred(x):
            return x
    return ValueError('not found')



def remove_node_with_zombie_entity_and_an_leaf_child(
    self, nonleaf, direction_to_leaf):
    assert isinstance(self, RedBlackTreeOpsABC)
    assert not self.is_leaf(nonleaf)
    me, is_me_double_black = __remove__raw__node_with_zombie_entity_and_an_leaf_child(
                                self, nonleaf, direction_to_leaf)
    # broken above me

    
    while is_me_double_black:
        # double black : me contain two black!! since v was removed
        assert is_black(self, me) # indeed double black


        # broken above (maybe parent), me
        #   maybe parent from maybe grandpa when "me:=parent" see below
        
        if self.is_root(me):
            # color me black ; ...
            is_me_double_black = False
            continue


        parent, me = fix_broken_between_parent_me(self, me)
        # broken above parent
        sibling = to_sibling(self, me)
        
        if is_red(self, sibling):
            assert not self.is_leaf(sibling)
            # ==>> parent and nephews are all black
            
            # broken above parent
            parent, sibling, me = __remove__red_sibling(self, parent, me, sibling)
            # broken above grandpa
            assert is_black(self, sibling)


        # broken above (parent or grandpa)
        #   source:
        #      <- broken above parent
        #      <- broken above grandpa
        assert is_black(self, sibling)
    
        nephews = to_children(self, sibling)
        # if both nephews are black:
        if all(is_black(self, nephew) for nephew in nephews):
            # broken above (parent or grandpa)
            parent, is_parent_double_black = __remove__black_sibling_and_no_red_nephews(self, parent, me, sibling)
            del me, sibling
            # broken above (maybe grandpa), parent
            # [BLACK me]

        else:
            # broken above (parent or grandpa)
            # assert exists a red_nephew
            red_nephew = __find_if(lambda node: is_red(self, node), nephews)
            parent, is_parent_double_black = __remove__black_sibling_and_a_red_nephew(self, parent, me, sibling, red_nephew)
            del me, sibling, red_nephew
            # broken above (maybe grandpa), parent
            # [BLACK me]


        # broken above (maybe grandpa), parent
        me = parent ; del parent
        # broken above (maybe parent), me
        is_me_double_black = is_parent_double_black
        continue

    # broken above (maybe parent), me
    if self.is_root(me):
        # no parent
        pass
        # broken above me
    else:
        parent, me = fix_broken_between_parent_me(self, me)
        # broken above parent
        me = parent ; del parent
        # broken above me

    
    # broken above me
    root = fix_broken_node_until_root(self, me)
    # broken above root
    return root # ignore broken above root


def __remove__raw__node_with_zombie_entity_and_an_leaf_child(
    self, nonleaf, direction_to_leaf):
    
    leaf_child = to_child(self, direction_to_leaf)
    if not self.is_leaf(leaf_child):
        raise ValueError('not direction to a leaf')
    
    me = to_sibling(self, leaf_child) # me may be a leaf !!
    is_double_black = is_black(self, nonleaf) and is_black(self, me)
    
    # remove nonleaf, leaf_child
    # replace nonleaf by me ==>> me.parent = nonleaf.parent
    # 
    me = replace_using_other_parent(self, me, nonleaf)
    # broken above me
    del leaf_child, nonleaf

    is_me_double_black = is_double_black # since nonleaf removed, me bears more
    
    # broken above me
    return me, is_me_double_black



def __remove__red_sibling(self, parent, me, sibling):
        '''
precondition:
    [broken above parent]
    [RED sibling] ==>> parent and nephews are all black
    [DOUBLE_BLACK me]
    
return:
    parent, sibling, me

postconditon:
    [broken above grandpa]
    [BLACK me]
    [BLACK sibling]
    [OLD grandpa, uncle, parent, sibling, me]
    
'''
        # broken above parent
        assert not self.is_leaf(sibling)
        # [RED sibling] ==>> parent and nephews are all black
        # if sibling is left child, same-direct-nephew is left child
        # if right, then right
        # other-nephew between same-direct-nephew and me

        del me
        sibling_direction = to_direction(self, sibling)
        sibling = recolor(self, sibling)# -> BLACK
        # broken above parent, sibling
        parent, sibling = fix_broken_between_parent_me(self, sibling)
        # broken above parent
        del sibling
        parent = recolor(self, parent) # -> RED
        sibling, same_direction_nephew = refresh_proper_descendants(
                            self, parent, [sibling_direction, sibling_direction])

            
        grandpa, uncle, parent, sibling, me = adjustment(self, parent, sibling, same_direction_nephew)
        # broken above grandpa
        
        #      sibling:black -> {parent:red, same-direct-nephew:black}
        assert is_black(self, grandpa) # <- old sibling:RED
        assert is_black(self, uncle)   # <- old same_direction_nephew
        assert is_red(self, parent)    # <- old parent:BLACK # my parent not changed
        assert is_black(self, sibling) # <- old other_nephew
        # assert is_double_black(me) # <- old me

        
        # now, sibling is black!!
        # but broken above grandpa
        return parent, sibling, me
    
def __remove__black_sibling_and_no_red_nephews(self, parent, me, sibling):
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
        sibling = recolor(self, sibling)
        # broken above (parent or grandpa), sibling
        parent, sibling = fix_broken_between_parent_me(self, sibling)
        # broken above (parent or grandpa), parent; new2old broken above me
        # broken above (maybe grandpa), parent; new2old broken above me
        del me, sibling
        # broken above (maybe grandpa), parent

      # assign black
        if is_red(self, parent):
            # color parent black <- red
            parent = recolor(self, parent)
            # broken above (maybe grandpa), parent
        else:
            # color parent double black <- black
            is_parent_double_black = True
        # broken above (maybe grandpa), parent

        return parent, is_parent_double_black
        #continue

def __remove__black_sibling_and_a_red_nephew(self, parent, me, sibling, red_nephew):
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
        assert is_black(self, me)
        assert is_black(self, sibling)
        grey = self.to_color(parent) # save color
        recolored_red_nephew = recolor(self, red_nephew) ; del red_nephew
        # broken above (parent or grandpa), recolored_red_nephew
        sibling = fix_broken_above(self, recolored_red_nephew)
        # broken above (parent or grandpa), sibling; new2old: recolored_red_nephew
        parent = fix_broken_above(self, sibling)
        # broken above (maybe grandpa), parent; new2old: sibling, recolored_red_nephew
        parent = replace(self, parent, self.BLACK)
        # broken above (maybe grandpa), parent; new2old: sibling, recolored_red_nephew
        to_di = lambda nonroot: to_direction(self, nonroot)
        sibling, recolored_red_nephew = refresh_proper_descendants(
            self, parent, map(to_di, [sibling, recolored_red_nephew]))
        # broken above (maybe grandpa), parent
        

        
        parent = trinode_restructuring(self, parent, sibling, recolored_red_nephew)
        del sibling, recolored_red_nephew, me # they are all invalid, since the struct changes
        # broken above (maybe grandpa), parent
        parent = replace(self, parent, grey) # restore color
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
        
