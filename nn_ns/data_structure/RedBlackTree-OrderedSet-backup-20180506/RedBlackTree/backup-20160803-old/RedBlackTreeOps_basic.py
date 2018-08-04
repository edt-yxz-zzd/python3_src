
from .RedBlackTreeOpsABC import RedBlackTreeOpsABC

def refresh_proper_descendants(self, node, descendant_directions):
    '''
each time we make a modification:
    recolor
    replace
    ...

    node = modify(node, ...)
we introduct a broken point between node and its parent if node is not root
    but the direction from parent -> node is not changed

    # take care : replace(node, ..., left) defines a new direction between node->left
    
we should maintain no more than one broken point
    otherwise too complicate

let us call the node below the only broken point topmost_node
before we use descendants of topmost_node after its birth
    # we can not use other nodes!
    # if needed, we fix the current broken point,
    #    then the parent of old topmost become new topmost

    we should refresh them
    e.g.
        grandpa = ... # replace by new value in same place
        # parent/me/... now may still refer to old grandpa
        # since direction holds, we use them to construct new references to grandpa
        parent, me, my_left_child = refresh_proper_descendants(self, grandpa, parent_d, mine_d, LEFT)

3 broken types:
    1) tree struct changed
    2) tree struct keeping
        e.g. parent -> me -> child
        me = tree_struct_keeping update
        2-1) old2new broken
            between parent and me
            parent = fix_broken_above(me)
            # but now yield a new2old broken between parent and me
            # see below
        2-2) new2old broken
            between me and child
            child = me.to_child(to_direction(child))


refresh_proper_descendants is to handle new2old broken
NOTE:
    we may have a old2new broken tree:
        above x -> above y -> above z
                           -> ...
                -> above w ...
        where x is an proper ancestor of y, and so on
              y and w should not be comparable by topological ordering
              

'''
    for d in descendant_directions:
        node = to_child(node, d)
        yield node




def fix_broken_between_parent_me(self, me):
    '''
broken_point between parent and me means:
    old_parent = to_parent(me)
    to_child(old_parent, to_direction(me)) may not be me !!

1) update parent.children
    new_parent = replace(old_parent, left/right=me)
2) update me.parent
    new_me = to_child(new_parent, to_direction(me))

NOTE:
    if there is 'sibling':
        parent, me, sibling ...
        parent, me = fix_broken_between_parent_me(me)
        then ==>> new2old broken above sibling
'''
    assert not self.is_root(me)
    parent = self.unsafe_to_parent(me)
    is_left = self.is_left(me)
    
    if is_left:
        parent = replace(self, parent, left = me)
        me = self.to_left(parent)
    else:
        parent = replace(self, parent, right = me)
        me = self.to_right(parent)

    return parent, me








def adjustment(self, parent, sibling, same_direction_nephew):
    '''
grandpa, uncle, parent, sibling, me =
'''
    sibling_d = to_direction(self, sibling)
    nephew_d = sibling_d
    me_d = to_direction(self, me)
    
    grandpa = trinode_restructuring(self, grandpa, parent, me)
    # why grandpa?? because me!

    # grandpa merge old parent direction and old sibling data(color, entity)
    uncle_d = nephew_d # uncle <- nephew
    parent_d = direction_to_other_direction(self, uncle_d) # parent <- parent
    me_d = me_d # me <- me
    uncle = to_child(self, grandpa, uncle_d)
    parent, me = refresh_proper_descendants(
                    self, grandpa, [parent_d, me_d])
    sibling = to_sibling(me)
    return grandpa, uncle, parent, sibling, me










def trinode_restructuring(self, grandpa, parent, me):
    # let {a,b,c} = {grandpa, parent, me}
    # assume a < b < c in inorder
    # then return b; where b->a, b->c
    assert not self.is_leaf(me)
    assert self.unsafe_to_parent(me) is parent
    assert self.unsafe_to_parent(parent) is grandpa
    # grandpa's parent information is most important
    # to avoid destroy grandpa, we use a shadow obj: grandpa_data_node
    grandpa_data_node = self.make_new_leaf_root(self.to_color(grandpa), self.to_entity(grandpa))
    

    sibling = to_sibling(self, me)
    left, right = to_children(self, me)
    if self.is_left(me):
        a, b, c = left, right, sibling
        A, B = me, parent
    else:
        a, b, c = sibling, left, right
        A, B = parent, me
    # (a,b,c) (A,B) keeping inorder
    
    uncle = to_sibling(self, parent)
    if self.is_left(parent):
        a, b, c, d = a, b, c, uncle
        A, B, C = A, B, grandpa_data_node
    else:
        a, b, c, d = uncle, a, b, c
        A, B, C = grandpa_data_node, A, B
    # (a,b,c,d) (A,B,C) is keeping inorder

    A = replace(A, left=a, right=b)
    C = replace(C, left=c, right=d)
    grandpa = replace(grandpa, left=A, right=C)
    # broken above grandpa
    return grandpa










