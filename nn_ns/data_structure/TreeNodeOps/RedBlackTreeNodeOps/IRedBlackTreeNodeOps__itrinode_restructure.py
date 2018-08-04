
__all__ = '''
    red_black_tree__itrinode_restructure
    red_black_tree__itrinode_restructure__for_double_red_when_uncle_is_black
    '''.split()

if False:
    # red_black_tree__itrinode_restructure
    get_parent = ops.get_parent
    get_sibling = ops.get_sibling
    get_parent_info = ops.get_parent_info
    is_left_child = ops.is_left_child
    iter_children = ops.iter_children

    iset_children = ops.iset_children
    basic_iset_parent_info = ops.basic_iset_parent_info

    # red_black_tree__itrinode_restructure__for_double_red_when_uncle_is_black
    is_red_node = ops.is_red_node
    is_black_node = ops.is_black_node
    irecolor = ops.irecolor


def red_black_tree__itrinode_restructure(ops, self):
    # allow old2new broken above me and above parent and so on...
    #   not allow dangling
    # precondition: exists self.parent.parent
    # return node who occupies grandpa's position
    # postcondition:
    #    if return node is not root:
    #       old2new broken above return_node's parent
    grandpa_pos, A, B, C, a, b, c, d = red_black_tree__itrinode_restructure__half0(ops, self)
    B = red_black_tree__itrinode_restructure__half1(ops, grandpa_pos, A, B, C, a, b, c, d)
    new_grandpa = B
    return new_grandpa

def red_black_tree__itrinode_restructure__for_double_red_when_uncle_is_black(ops, self):
    # see: red_black_tree__itrinode_restructure.__doc__
    #
    # self, parent are both red
    is_red_node = ops.is_red_node
    is_black_node = ops.is_black_node
    get_parent = ops.get_parent
    get_sibling = ops.get_sibling
    irecolor = ops.irecolor

    if __debug__:
        # preconditions:
        # * has grandpa
        parent = get_parent(self)
        uncle = get_sibling(parent)
        # * color
        assert is_red_node(self)
        assert is_red_node(parent)
        assert is_black_node(uncle)

        # other
        grandpa = get_parent(parent)
        assert is_black_node(grandpa)
        del parent, uncle, grandpa

##            ==>> children of (grandpa, parent, me) exclude these 3
##                    are all black;
##                 total 4 (my 2 children + sibling + uncle)
##
##            -              grandpa:black
##            - uncle:black,                       parent:red
##            -                      sibling:black,            me:red
##            -                                        lchild:black, rchild:black
    grandpa_pos, A, B, C, a, b, c, d = red_black_tree__itrinode_restructure__half0(ops, self)
    # a,b,c,d are all black
    #
    # one and only one of [A,C] is black, which is grandpa
    #   {A,B,C} == {grandpa, parent, self}
    if is_black_node(A):
        assert is_red_node(C)
        A = irecolor(A) # black->red
    else:
        #assert is_red_node(A)
        assert not is_red_node(C)
        C = irecolor(C) # black->red

    assert is_red_node(B)
    B = irecolor(B) # red->black


    B = red_black_tree__itrinode_restructure__half1(ops, grandpa_pos, A, B, C, a, b, c, d)
    new_grandpa = B
    return new_grandpa


def red_black_tree__itrinode_restructure__half0(ops, self):
    get_parent = ops.get_parent
    get_sibling = ops.get_sibling
    get_parent_info = ops.get_parent_info
    is_left_child = ops.is_left_child
    iter_children = ops.iter_children

    parent = get_parent(self)
    grandpa = get_parent(parent)
    grandpa_pos = get_parent_info(grandpa)
    sibling = get_sibling(self)
    uncle = get_sibling(parent)

    if is_left_child(self):
        A, B = self, parent
        (a, b), c = iter_children(self), sibling
    else:
        A, B = parent, self
        a, (b, c) = sibling, iter_children(self)
    # A < B
    # a < b < c

    if is_left_child(parent):
        A, B, C = A, B, grandpa
        a, b, c, d = a, b, c, uncle
    else:
        A, B, C = grandpa, A, B
        a, b, c, d = uncle, a, b, c
    # A < B < C
    # a < b < c < d

    # bug: return grandpa, A, B, C, a, b, c, d
    return grandpa_pos, A, B, C, a, b, c, d
    '''
        B
    A       C
  a   b   c   d
    '''


def red_black_tree__itrinode_restructure__half1(ops, grandpa_pos, A, B, C, a, b, c, d):
    iset_children = ops.iset_children
    basic_iset_parent_info = ops.basic_iset_parent_info

    # update bottom-up!!!
    A = iset_children(A, [a, b])
    C = iset_children(C, [c, d])
    B = iset_children(B, [A, C])

    B = basic_iset_parent_info(B, grandpa_pos)
    new_grandpa = B
    # old2new broken above B
    return B





