
from .RedBlackTreeOps2ABC import WrappedRedBlackTreeNodeEx


def insert_at_leaf(leaf, entity):
    'leaf should be between find_range(root, key); otherwise disrupt order'
    assert isinstance(self, WrappedRedBlackTreeNodeEx)
    assert leaf.is_leaf(leaf)
    
    # replace u by red(null, e, null)
    me = leaf.make_red_nonleaf(entity, leaf.parent_info)

    while True:
        # broken above me
        assert me.is_red
        if me.is_root():
            me.recolor()
            break
        parent = me.refresh_up()
        # broken above parent
        
    
        if parent.is_black():
            me = parent
            # broken above me
            break
        
        # double-red == parent and me are both red
        assert not parent.is_root()
        grandpa = parent.refresh_up()
        # broken above grandpa
        # !AND! new2old broken above me
        me, = parent.get_descendants__olds([me])
        # broken above grandpa
        
        assert grandpa.is_black()xxxxxxxxxxxxxxxxxxxxx
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




