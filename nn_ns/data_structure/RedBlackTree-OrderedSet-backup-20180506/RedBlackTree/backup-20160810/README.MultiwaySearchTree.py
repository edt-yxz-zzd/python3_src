
'''
Data Structures and Algorithms in C ++ (2ed)
    by Michael T. Goodrich


[Multi-way Search Tree]

Entity = (Key, Value) # in concept

[d-node]
    internal node v is a d-node if v has d children (d>=2)
        v stores (d-1) entities
        v.e[1] ... v.e[d-1];
        assume virtual entities: v.e[0], v.e[d]
        v.e[i] <= v.e[i+1]

        v.e[i]; 0 <= i <= d ; virtual entity
        v.c[i]; 1 <= i <= d ; child
        v.E[i]; 1 <= i <= d-1; actual entity

[(2, 4) Tree]
    Size Property:
        Every internal node has at most four children
            and at least 2 children
    Depth Property:
        All the external nodes have the same depth

    find, insert, erase: O(log n)

d-node = (.e[0]=-oo, .c[1], .e[1], ..., .e[d-1], .c[d], .e[d]=+oo)

insert e
    find external node u
    if u is root:
        ...
        return
    v = parent[u]
    insert e into v
    # violate Size Property
    while overflow:
        # 4 entities: v.e[1], v.e[2], v.e[3], v.e[4]
        split 5-node v ->
            3-node v1, # 2 entities: e[1], e[2]
            v.e[3],
            2-node v2  # 1 entity: e[4]

        if v is root:
            set_root new_node(v1, v.e[3], v2)
            return
        v is children[p][i]
        p = (... p.e[i-1], p.c[i]=v, p.e[i], ...)
        new_p = (... p.e[i-1], v1, v.e[3], v2, p.e[i], ...)
        v = new_p
        
remove e
    find
    -> fail return
    -> v.e[i] == e

    if children of v are internal nodes:
        swap v.e[i] with SUCC/PREV entity u.e[j] # in inorder
        assert children of u are external
        v, i = u, j
    assert children of v are external

    remove v.e[i] and v.c[i]

    while underflow:
        # 1-node; no entity
        if v is root:
            root = v.children # external at above case and internal at below case
            return
        if u is a 3- or 4-node horizontal sibling of v:
            u.e[?] -> parent.e[?] -> v.e[1]
        else u is a 2-node horizontal sibling of v:
            fusion u.e[1], u.e[2], parent.e[?] v.e[nothing]
            parent now become (d-1)-node from d-node
            v = parent
    
        
'''
