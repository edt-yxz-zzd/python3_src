
from .RedBlackTreeOpsABC import RedBlackTreeOpsABC


def insert_at_leaf(self, leaf, entity):
    'leaf should be between find_range(root, key); otherwise disrupt order'
    assert isinstance(self, RedBlackTreeOpsABC)
    assert self.is_leaf(leaf)
    
    # replace u by red(null, e, null)
    color = self.RED
    me = leaf2new_nonleaf(self, leaf, color, entity)

    while True:
        # broken above me
        assert is_red(self, me)
        if self.is_root(me):
            me = recolor(self, me)
            break
        parent, me = fix_broken_between_parent_me(self, me)
        # broken above parent
        
    
        if is_black(self, parent):
            me = parent
            # broken above me
            break
        
        # double-red == parent and me are both red
        assert not self.is_root(parent)
        grandpa, parent = fix_broken_between_parent_me(self, parent)
        # broken above grandpa
        # !AND! broken above me
        me, = refresh_proper_descendants(self, parent, [to_direction(me)])
        # broken above grandpa
        
        assert is_black(self, grandpa)
        uncle = to_sibling(self, parent)
        
        
        if is_black(self, uncle):
##            ==>> children of (grandpa, parent, me) exclude these 3
##                    are all black;
##                 total 4 (my 2 children + sibling + uncle)
##
##            -              grandpa:black
##            - uncle:black,                       parent:red
##            -                      sibling:black,            me:red
##            -                                        lchild:black, rchild:black

            grandpa = trinode_restructuring(self, grandpa, parent, me)
            del parent, uncle, me # they are all invalid, since the struct changes
            # broken above grandpa
            
            me = grandpa
            # broken above me
            assert is_red(self, me)
            recolor(self, me) # -> black
            left, right = to_children(self, me)
            left = replace(self, left, color=self.RED)
            right = replace(self, right, color=self.RED)
            # broken above me, left, right
            me = replace(self, me, left=left, right=right)
            del left, right
            # broken above me
            
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
            # recolor(self, grandpa, parent, uncle)
            

            # broken above grandpa
            left, right = to_children(self, grandpa)
            left = recolor(self, left)
            right = recolor(self, right)
            # broken above grandpa, left, right
            grandpa = replace(self, grandpa, left=left, right=right)
            del left, right # to ignore the new2old broken points above them
            # broken above grandpa
            grandpa = recolor(self, grandpa)
            # brken above grandpa
            
##            
##            -           grandpa:red
##            - uncle:black,          parent:black
##            -                     ....   me:red

            
            me = grandpa
            # broken above me
            continue    
    
    # broken above me

    assert is_black(self, me)
    root = fix_broken_node_until_root(self, me)
    # broken above root
    return root # ignore broken above root




