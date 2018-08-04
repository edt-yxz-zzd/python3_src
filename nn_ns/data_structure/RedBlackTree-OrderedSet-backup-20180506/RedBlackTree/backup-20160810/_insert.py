

def insert_entity_at_leaf(leaf, entity):
    # if this is an ordered tree,
    # then leaf should be between find_range(root, key);
    # otherwise this call will disrupt order
    assert isinstance(leaf, MutableRedBlackTreeNodeABC)
    assert leaf.is_leaf()
    
    # replace u by red(null, e, null)
    me = leaf.make_red_nonleaf_node(entity, leaf.parent_info)
    del leaf
    # broken above me

    while True:
        # broken above me
        assert me.is_red()
        if me.is_root():
            me.recolor()
            break
        parent = me.refresh_up()
        # broken above parent
        
    
        if parent.is_black():
            me = parent
            # broken above me
            break
        
        # double-red ::= parent and me are both red
        assert not parent.is_root()
        grandpa = parent.refresh_up()
        # old2new broken above grandpa
        # !AND! new2old broken above me
        me, = parent.refresh_downs(me.direction)
        # broken above grandpa
        
        assert grandpa.is_black()
        uncle = parent.sibling
        
        
        if uncle.is_black():
##            ==>> children of (grandpa, parent, me) exclude these 3
##                    are all black;
##                 total 4 (my 2 children + sibling + uncle)
##
##            -              grandpa:black
##            - uncle:black,                       parent:red
##            -                      sibling:black,            me:red
##            -                                        lchild:black, rchild:black

            grandpa = me.trinode_restructure()
            del parent, uncle, me # they are all invalid, since the struct changes
            # broken above grandpa
            
            me = grandpa
            # broken above me
            assert me.is_red()
            me.recolor() # -> black
            left, right = me.children
            left.color = me.RED
            right.color = me.RED
            # broken above me, left, right
            me.children = left, right
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
            left, right = grandpa.children
            left.recolor()
            right.recolor()
            # broken above grandpa, left, right
            grandpa.children = left, right
            del left, right # to ignore the new2old broken points above them
            # broken above grandpa
            grandpa.recolor()
            # brken above grandpa
            assert grandpa.is_red()
            
##            
##            -           grandpa:red
##            - uncle:black,          parent:black
##            -                     ....   me:red

            
            me = grandpa
            # broken above me
            continue    
    
    # broken above me

    assert me.is_black()
    root = me.fixed_the_only_broken_above_until_root(); del me
    # broken above root
    return root # ignore broken above root


# cyclic import
from .RedBlackTreeNodeABC import MutableRedBlackTreeNodeABC
insert_at_leaf = insert_entity_at_leaf



def _test1():
    from .RedBlackTreeNodeABC import RBT_Node_TupleBothPlainParented as Node
    LEAF = Node.PLAIN_LEAF
    BLACK = Node.BLACK
    RED = Node.RED
    ROOT_PARENT_INFO = Node.ROOT_PARENT_INFO
    root = Node.make_leaf_root()
    assert root.underlying == (LEAF, ROOT_PARENT_INFO)
    n0 = insert_at_leaf(root, 0)
    assert n0.underlying == ((BLACK, 0, LEAF, LEAF), ROOT_PARENT_INFO)
    n1 = insert_at_leaf(n0.right, 1)
    assert n1.underlying == ((BLACK, 0, LEAF, (RED, 1, LEAF, LEAF)), ROOT_PARENT_INFO)
    n2 = insert_at_leaf(n1.right.right, 2)
    assert n2.underlying == ((BLACK, 1, (RED, 0, LEAF, LEAF), (RED, 2, LEAF, LEAF)), ROOT_PARENT_INFO)
    n3 = insert_at_leaf(n2.right.right, 3)
    assert n3.underlying == ((BLACK, 1, (BLACK, 0, LEAF, LEAF), (BLACK, 2, LEAF, (RED, 3, LEAF, LEAF))), ROOT_PARENT_INFO)
    n4 = insert_at_leaf(n3.right.right.right, 4)
    assert n4.underlying == ((BLACK, 1, (BLACK, 0, LEAF, LEAF), (BLACK, 3, (RED, 2, LEAF, LEAF), (RED, 4, LEAF, LEAF))), ROOT_PARENT_INFO)
    n5 = insert_at_leaf(n4.right.right.right, 5)
    assert n5.underlying == ((BLACK, 1, (BLACK, 0, LEAF, LEAF), (RED, 3, (BLACK, 2, LEAF, LEAF), (BLACK, 4, LEAF, (RED, 5, LEAF, LEAF)))), ROOT_PARENT_INFO)
    n6 = insert_at_leaf(n5.right.right.right.right, 6)
    assert n6.underlying == ((BLACK, 1, (BLACK, 0, LEAF, LEAF), (RED, 3, (BLACK, 2, LEAF, LEAF), (BLACK, 5, (RED, 4, LEAF, LEAF), (RED, 6, LEAF, LEAF)))), ROOT_PARENT_INFO)
    n7 = insert_at_leaf(n6.right.right.right.right, 7)
    assert n7.underlying == ((BLACK, 3, (RED, 1, (BLACK, 0, LEAF, LEAF), (BLACK, 2, LEAF, LEAF)), (RED, 5, (BLACK, 4, LEAF, LEAF), (BLACK, 6, LEAF, (RED, 7, LEAF, LEAF)))), ROOT_PARENT_INFO)






def _test2():
    from .RedBlackTreeNodeABC import RBT_Node_TupleBothPlainParented as Node
    LEAF = Node.PLAIN_LEAF
    BLACK = Node.BLACK
    RED = Node.RED
    ROOT_PARENT_INFO = Node.ROOT_PARENT_INFO
    root = Node.make_leaf_root()
    assert root.underlying == (LEAF, ROOT_PARENT_INFO)
    n0 = insert_at_leaf(root, 0)
    assert n0.underlying == ((BLACK, 0, LEAF, LEAF), ROOT_PARENT_INFO)
    n1 = insert_at_leaf(n0.right, 1)
    assert n1.underlying == ((BLACK, 0, LEAF, (RED, 1, LEAF, LEAF)), ROOT_PARENT_INFO)
    n2 = insert_at_leaf(n1.right.left, 2)
    assert n2.underlying == ((BLACK, 2, (RED, 0, LEAF, LEAF), (RED, 1, LEAF, LEAF)), ROOT_PARENT_INFO)
    n3 = insert_at_leaf(n2.right.left, 3)
    assert n3.underlying == ((BLACK, 2, (BLACK, 0, LEAF, LEAF), (BLACK, 1, (RED, 3, LEAF, LEAF), LEAF)), ROOT_PARENT_INFO)
    n4 = insert_at_leaf(n3.right.left.right, 4)
    # print(n4.underlying)
    assert n4.underlying == ((BLACK, 2, (BLACK, 0, LEAF, LEAF), (BLACK, 4, (RED, 3, LEAF, LEAF), (RED, 1, LEAF, LEAF))), ROOT_PARENT_INFO)






def _test3():
    from operator import attrgetter
    from .RedBlackTreeNodeABC import \
         RBT_Node_TupleBothPlainParented,\
         RBT_Node_AllSelf, \
         RBT_Node_TuplePlain_MutableParentedSelf
         
    Node = RBT_Node_TupleBothPlainParented
    LEAF = Node.PLAIN_LEAF
    BLACK = Node.BLACK
    RED = Node.RED
    ROOT_PARENT_INFO = Node.ROOT_PARENT_INFO
    
    Nodes = [Node, RBT_Node_AllSelf, RBT_Node_TuplePlain_MutableParentedSelf]
    attrsls = [
        '''
right
right.right
right.right
right.right.right
right.right.right
right.right.right.right
right.right.right.right'''.split(),
        '''
right
right.left
right.left
right.left.right
'''.split()
        ]
    datalsls = [
        [   (LEAF, ROOT_PARENT_INFO),
            ((BLACK, 0, LEAF, LEAF), ROOT_PARENT_INFO),
            ((BLACK, 0, LEAF, (RED, 1, LEAF, LEAF)), ROOT_PARENT_INFO),
            ((BLACK, 1, (RED, 0, LEAF, LEAF), (RED, 2, LEAF, LEAF)), ROOT_PARENT_INFO),
            ((BLACK, 1, (BLACK, 0, LEAF, LEAF), (BLACK, 2, LEAF, (RED, 3, LEAF, LEAF))), ROOT_PARENT_INFO),
            ((BLACK, 1, (BLACK, 0, LEAF, LEAF), (BLACK, 3, (RED, 2, LEAF, LEAF), (RED, 4, LEAF, LEAF))), ROOT_PARENT_INFO),
            ((BLACK, 1, (BLACK, 0, LEAF, LEAF), (RED, 3, (BLACK, 2, LEAF, LEAF), (BLACK, 4, LEAF, (RED, 5, LEAF, LEAF)))), ROOT_PARENT_INFO),
            ((BLACK, 1, (BLACK, 0, LEAF, LEAF), (RED, 3, (BLACK, 2, LEAF, LEAF), (BLACK, 5, (RED, 4, LEAF, LEAF), (RED, 6, LEAF, LEAF)))), ROOT_PARENT_INFO),
            ((BLACK, 3, (RED, 1, (BLACK, 0, LEAF, LEAF), (BLACK, 2, LEAF, LEAF)), (RED, 5, (BLACK, 4, LEAF, LEAF), (BLACK, 6, LEAF, (RED, 7, LEAF, LEAF)))), ROOT_PARENT_INFO),
        ],
        [   (LEAF, ROOT_PARENT_INFO),
            ((BLACK, 0, LEAF, LEAF), ROOT_PARENT_INFO),
            ((BLACK, 0, LEAF, (RED, 1, LEAF, LEAF)), ROOT_PARENT_INFO),
            ((BLACK, 2, (RED, 0, LEAF, LEAF), (RED, 1, LEAF, LEAF)), ROOT_PARENT_INFO),
            ((BLACK, 2, (BLACK, 0, LEAF, LEAF), (BLACK, 1, (RED, 3, LEAF, LEAF), LEAF)), ROOT_PARENT_INFO),
            ((BLACK, 2, (BLACK, 0, LEAF, LEAF), (BLACK, 4, (RED, 3, LEAF, LEAF), (RED, 1, LEAF, LEAF))), ROOT_PARENT_INFO),
        ],
    ]

    assert len(attrsls) == len(datalsls)
    assert all(len(attrs) + 2 == len(datals) for attrs, datals in zip(attrsls, datalsls))
    assert Nodes[0] is Node

    def assert_eq(subtrees):
        s = subtrees[0]
        for t in subtrees:
            try:
                assert t.oriented_subtree_eq(s)
            except:
                print(s, t)
                print(s.underlying)
                print(j, i)
                raise
            
    for j, (attrs, datals) in enumerate(zip(attrsls, datalsls)):
        roots = [Node.make_leaf_root() for Node in Nodes]
        assert roots[0].underlying == datals[0]
        assert_eq(roots)
        n0s = [insert_at_leaf(root, 0) for root in roots]
        assert n0s[0].underlying == datals[1]
        assert_eq(n0s)

        roots = n0s
        for i, (attr, data) in enumerate(zip(attrs, datals[2:]), 1):
            get = attrgetter(attr)
            roots = [insert_at_leaf(get(root), i) for root in roots]
            assert roots[0].underlying == datals[i+1]
            assert_eq(roots)




if 1 or __name__ == '__main__':
    _test1()
    _test2()
    _test3()






