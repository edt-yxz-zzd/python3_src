


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


__all__ = '''
    SearchableMultiWayLikeTreeOpsABC
    SearchableMultiWayLikeTreeOpsWithParentABC
'''.split()


from abc import abstractmethod, ABCMeta
class SearchableOrderedTreeOpsABC(metaclass=ABCMeta):
    @abstractmethod
    def is_leaf(self, node):
        raise NotImplementedError
    @abstractmethod
    def key_lt(self, key1, key2):
        raise NotImplementedError
    @abstractmethod
    def to_key(self, entity): # no to_value
        raise NotImplementedError

    @abstractmethod
    def fixed_node_eq(self, fixed_node1, fixed_node2):
        '''__is__ operator for two nodes without broken points
should be an O(1) operation

used at search, to compare whether two paths are identital
    e.g. begin == end??
NOTE: a plain node may be shared in different trees/subtrees

undefined behavior if contains broken points


broken point: see RedBlackTreeOpsABC
'''
        raise NotImplementedError
    

class SearchableMultiWayLikeTreeOpsABC(SearchableOrderedTreeOpsABC):
    '''ordered tree

consider only to support 'find'
no other operation are required

red-black is like a multi-way tree when searching
    but it's donot have same depth for leaves

not require to_parent
    if multiway tree:
        to_parent_position(self, node)
'''
    @abstractmethod
    def find_innode_range(self, nonleaf_node, key):
        '''
d-node = (.e[0]=-oo, .c[1], .e[1], ..., .e[d-1], .c[d], .e[d]=+oo)

# begin and end can be any type...
begin, end = innode_range
.c[begin:end] contains all children that equal to key


all(to_key(e) < key for e in .e[:begin])
all(key == to_key(e) for e in .e[begin:end])
all(key < to_key(e) for e in .e[end:])
assume pos is int:
    1 <= begin <= end <= d
    .e[begin:end]
    unknown .c[begin:end+1]
    ==>> exists c[begin] and c[end]



tree entity iterator
    empty tree entity iterator = (leaf_root, None)
    otherwise:
    tree entity iterator = (node, innode_entity_pos of node)
    tree entity iterator end = (last, innode_entity_end of last node)
    tree entity iterator begin/rend = (first, innode_entity_begin of first)

    but how to represent:
        inorder_SUCC(node)
        inorder_PREV(node)
        maybe node??
    
'''
        raise NotImplementedError
    @abstractmethod
    def innode_pos2child(self, nonleaf_node, innode_pos):
        'allow innode_pos2child(pos) is not innode_pos2child(pos)'
        raise NotImplementedError
    @abstractmethod
    def innode_pos2entity(self, nonleaf_node, innode_pos):
        'not allow?? innode_pos2entity(pos) is not innode_pos2entity(pos); what if immutable??'
        raise NotImplementedError
    @abstractmethod
    def iter_innode_range(self, nonleaf_node, innode_begin, innode_end):
        'why need a node??'
        raise NotImplementedError
    @abstractmethod
    def iter_reversed_innode_range(self, nonleaf_node, innode_begin, innode_end):
        'why need a node??'
        raise NotImplementedError
    

##    
##    @abstractmethod
##    def get_innode_prebegin(self, node):
##        'e.g. 0; a special value'
##        raise NotImplementedError
    @abstractmethod
    def get_innode_begin(self, nonleaf_node):
        'e.g. 1; .begin == .e.begin == .c.begin'
        raise NotImplementedError
    @abstractmethod
    def get_innode_entity_end(self, nonleaf_node):
        'e.g. d; .e.end == .c.end-1'
        raise NotImplementedError
    @abstractmethod
    def get_innode_child_end(self, nonleaf_node):
        'e.g. d+1; .c.end == .e.end+1'
        raise NotImplementedError


    
    def get_innode_child_begin(self, nonleaf_node):
        'e.g. 1; .c.begin == .begin'
        return self.get_innode_begin(nonleaf_node)
    def get_innode_entity_begin(self, nonleaf_node):
        'e.g. 1; .e.begin == .c.begin'
        return self.get_innode_begin(nonleaf_node)
    
        
class SearchableMultiWayLikeTreeOpsWithParentABC(SearchableMultiWayLikeTreeOpsABC):
    @abstractmethod
    def is_root(self, node):
        raise NotImplementedError
    @abstractmethod
    def to_parent_innode_pos(self, nonroot_node):
        '''a parent innode_pos point to nonroot_node;
undefined behavior if nonroot_node is root
not allow:
    to_parent_innode_pos(node) to_parent_innode_pos(node)
'''
        raise NotImplementedError
    @abstractmethod
    def unsafe_to_parent(self, nonroot_node):
        '''return the stored parent

!NOT! allow:
    unsafe_to_parent(ops, node) is not unsafe_to_parent(ops, node)
    therefore we can check that whether there is a broken
    e.g. in trinode_restructuring

return old parent if there is a broken between parent and me;
see also : fix_broken_between_parent_me

undefined behavior if me is root
'''
        raise NotImplementedError
    
