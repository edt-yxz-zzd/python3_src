
'''
Data Structures and Algorithms in C ++ (2ed)
    by Michael T. Goodrich

[red-black tree]
    a red-black tree is a binary search tree
        with nodes colored red and black in a way that
        satisfies the following properties:
    
    Root Property:
        The root is black.
    External Property:
        Every external node is black.
    Internal Property:
        The children of a red node are black.
    Depth Property:
        All the external nodes have the same black depth,
        defined as the number of black ancestors minus one.
        (Recall that a node is an ancestor of itself.)

    [red-black tree <-> (2,4) tree] # many to many relationship
        black->{?, ?} <<== 2-node
        black->{red, ?} <<== 3-node
        black->{red, red} <<== 4-node



we assume that entries are stored at the internal nodes of a red-black tree,
    with the external nodes being empty placeholders

we assume that the external nodes are actual nodes,
    but we note that, at the expense of slightly more complicated methods,
    external nodes could be null.


insert e:
    find a external node u
    replace u by red(null, e, null)

    me = u
    while me is not root and parent is red:
        # double-red == parent and me are both red
        ==>> parent is not root
        ==>> grandpa is black
        ==>> exists uncle
        
        if uncle is black
            ==>> children of (grandpa, parent, me) exclude these 3
                    are all black;
                 total 4 (my 2 children + sibling + uncle)

            -              grandpa:black
            - uncle:black,                       parent:red
            -                      sibling:black,            me:red
            -                                        lchild:black, rchild:black

            trinode restructuring (grandpa, parent, me) ->
                black -> {red, red}
                the above 2 reds -> the 4 black others

            -                              g_p_m_1:black
            -           g_p_m_0:red,                          g_p_m_2:red
            - u_s_l_r_0:black, u_s_l_r_1:black     u_s_l_r_2:black, u_s_l_r_3:black,
            - # g_p_m_i is one of (grandpa, parent, me)
            - # u_s_l_r_i is one of (uncle, sibling, lchild, rchild)
            
        else:
            # uncle is red
            -           grandpa:black
            - uncle:red,            parent:red
            -                     ....   me:red
            recolor (grandpa, parent, uncle)
            
            -           grandpa:red
            - uncle:black,          parent:black
            -                     ....   me:red

            
            me := grandpa
            continue
    if me is root:
        root = me
        recolor (root)
    return root

remove e:
    find v.e == e
    if v has no external children:
        let u = SUCC v # in inorder
        assert u has external child
        swap u.e, v.e
        v := u
    assert v has external child

    x = a external child of v
    me = another child of v
    
    remove v, x
    let me be child of parent[v]
    if v and me both black:
        color me double black

    while me has double black:
        # double black : me contain two black!! since v was removed
        if me is root:
            color me black
            return
        
        if sibling is red:
            ==>> parent and nephews are all black
            # if sibling is left child, same-direct-nephew is left child
            # if right, then right
            # other-nephew between same-direct-nephew and me
            adjustment (parent, sibling, same-direct-nephew) 
                sibling:black -> {parent:red, same-direct-nephew:black}
                my parent not changed
                new_parent = parent
                new_grandpa = sibling
                new_uncle = same-direct-nephew
                new_sibling = other-nephew
                # now, sibling is black!!
        
        assert sibling is black
        if both nephews are black:
            # extract black
            color sibling red
            color me black

            # assign black
            if parent is red:
                color parent black
            else:
                color parent double black
            me := parent
            continue

        assert exists a red_nephew
        - parent:grey -> {me:double_black, sibling:black->{.., red_nephew:red}}
        NOTE:
            # assume red = 0, black = 1, grey = 0 or 1
            # all outgoings:
            me:double_black <- grey = 2 + grey
            other_nephew:self <- black <- grey = self + 1 + grey
            children of red_nephew : self <- red <- black <- grey = self + 1 + grey
            
        
        trinode restructuring (parent, sibling, red_nephew)
        - s_n_A:grey -> {parent:black->{me:black, ..}, s_n_B:black->{..}}
        - s_n_X = sibling or red_nephew
        NOTE:
            # all outgoings not changed!!
            me:black <- black <- grey = 2 + grey
            other_nephew:self <- black <- grey = self + 1 + grey
            children of red_nephew : self <- black <- grey = self + 1 + grey

        return
            

            
        
            

restruct(me) = trinode restructuring (grandpa, parent, me)
adjust(me) = adjustment (parent, me, same-direct-child)
           = restruct(same-direct-child)

'''
