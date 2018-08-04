
'''
support both mutable and immutable nodes

direction:
    for nonroot node, direction means the node is a left child or right one
broken point:
    see "refresh_proper_descendants"
        structure changed
        old2new
        new2old
    
fixed node:
    no broken point above it's ancestors (include itself)
node type:
    plain_node - store form
        assume plain-node do not know its parent # not required
    node - extract form
        should know parent and direction
        assume extract a new obj each time call .to_left/right() # not required
        so allow to_left(parent) is not to_left(parent) 
        


'''




'''
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

from .SearchableMultiWayLikeTreeOpsABC import SearchableMultiWayLikeTreeOpsWithParentABC
        
class RedBlackTreeOpsMixin_defaultOps:
    # below 4-tuple are innode_positions
    # not part of public interface
    # maybe override, but iter_innode_range too
    _INNODE_POS = tuple(range(4))


    def find_innode_range(self, nonleaf_node, key):
        '2-node : (.e[0]=-oo, .c[1], .e[1], .c[2], .e[2]=+oo)'
        e = self.to_entity(nonleaf_node)
        k = self.to_key(e)
        lt = self.key_lt
        _1, _2 = self._INNODE_POS[1:-1]
        if lt(k, key):
            begin = end = _2
        elif lt(key, k):
            begin = end = _1
        else:
            # k == key
            begin = _1
            end = _2
        return begin, end
    
    def innode_pos2child(self, node, innode_pos):
        if innode_pos == self._INNODE_POS[1]:
            return self.to_left(node)
        elif innode_pos == self._INNODE_POS[2]:
            return self.to_right(node)
        raise ValueError('innode_pos out of child range')
        
    def innode_pos2entity(self, node, innode_pos):
        if innode_pos == self._INNODE_POS[1]:
            return self.to_entity(node)
        raise ValueError('innode_pos out of entity range')

    def iter_innode_range(self, node, innode_begin, innode_end):
        ls = self._INNODE_POS
        i = ls.index(innode_begin)
        j = ls.index(innode_end, i)
        return iter(ls[i:j]) # not j+1, end is not in output
        

    def get_innode_begin(self, node):
        'e.g. 1; .begin == .e.begin == .c.begin'
        return self._INNODE_POS[1]
    def get_innode_entity_end(self, node):
        'e.g. d; .e.end == .c.end-1'
        return self._INNODE_POS[2]
    def get_innode_child_end(self, node):
        'e.g. d+1; .c.end == .e.end+1'
        return self._INNODE_POS[3]


    
    def to_parent_innode_pos(self, nonroot_node):
        return self._INNODE_POS[1 if self.is_left(nonroot_node) else 2]
    
    
class RedBlackTreeOpsABC(RedBlackTreeOpsMixin_defaultOps,
                         SearchableMultiWayLikeTreeOpsWithParentABC):
    '''

Node - concrete object - plain node
node - abstract object - argued node

node should contain parent and left/right info

if exists Node.parent:
    # mutable tree
    node = Node
else:
    node = {proper_ancestors::[(Node, Direction)], this::Node}

store form and extract form:
    e.g.
        use None as leaf, but we require .to_parent
        None is store form
        (Leaf parent) is extract form as result of to_children

store form : IsMutable? HasParent? IsNullLeaf?
    if not IsNullLeaf:
        ==>> HasParent ==>> IsMutable
        StoreNode e = StoreLeaf (StoreNode e) | StoreNode (StoreNode e) e (StoreNode e) (StoreNode e)
        ExtractNode e = ExtractNode (StoreNode e)
    if IsNullLeaf and HasParent:
        ==>> IsMutable
        StoreNode e = StoreLeaf | StoreNode (StoreNode e) e (StoreNode e) (StoreNode e)
        ExtractNode e = ExtractLeaf {parent::StoreNode e} | ExtractNode (StoreNode e)

    if not HasParent:
        ==>> IsNullLeaf
        StoreNode e = StoreLeaf | StoreNode e (StoreNode e) (StoreNode e)
        ExtractNode e = NoParent {root::StoreNode e} | ExtractNode {broken_parent::ExtractNode e, this::StoreNode e}
        no matter whether StoreNode e is mutable, we can modify ExtractNode e
        so, we assume (ExtractNode e) is a broken tree,
            # plain - i.e. donot know parent
            it contains a plain subtree (StoreNode e) and a broken_parent (ExtractNode e)
            since the subtree may not be a child of the "parent"

        how to implement .is_left?
            we should contains Direction information!!
            ExtractNode e = {proper_ancestors::[(StoreNode e, Direction)],
                             this::(StoreNode e)}

    if not IsMutable:
        ==>> not HasParent ==>> IsNullLeaf


let's call (StoreNode e) plain_node and (ExtractNode e) broken_node

(ExtractNode e) carry parent information is indeed a Monad


'''
    # inherit methods
    
    @abstractmethod
    def is_leaf(self, node):
        raise NotImplementedError
    @abstractmethod
    def key_lt(self, key1, key2):
        raise NotImplementedError
    @abstractmethod
    def to_key(self, entity): # no to_value
        raise NotImplementedError



    # property

    @property
    @abstractmethod
    def LEFT(self):
        raise NotImplementedError
    @property
    @abstractmethod
    def RIGHT(self):
        raise NotImplementedError
    @property
    @abstractmethod
    def RED(self):
        raise NotImplementedError
    @property
    @abstractmethod
    def BLACK(self):
        raise NotImplementedError

    
    @abstractmethod
    def to_color(self, nonleaf_node):
        '''
though leaf/root should be BLACK,
    this function should return the color store in nonleaf_node
    therefore we may find (is_root(n) and to_color(n)==RED) error,
        if exists implement defect

undefined behavior if me is leaf
'''
        raise NotImplementedError
    
    @abstractmethod
    def to_entity(self, nonleaf_node):
        'undefined behavior if me is leaf'
        raise NotImplementedError
    @abstractmethod
    def to_left(self, nonleaf_node):
        '''return stored left child in a extract form node instead of store form node

allow:
    to_left(ops, node) is not to_left(ops, node)

undefined behavior if me is leaf
undefined behavior if there is a broken between me and left child;
'''
        raise NotImplementedError
    @abstractmethod
    def to_right(self, nonleaf_node):
        '''return stored right child in a extract form node instead of store form node
allow:
    to_right(ops, node) is not to_right(ops, node)
undefined behavior if me is leaf
undefined behavior if there is a broken between me and right child;
'''
        raise NotImplementedError


    @abstractmethod
    def is_root(self, node):
        raise NotImplementedError
    @abstractmethod
    def is_left(self, nonroot_node):
        'is a left child; undefined behavior if nonroot_node is root'
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
    
    @abstractmethod
    def unsafe_replace_to_broken_node(self, node:'destroy',
                                      color, entity,
                                      left:'destroy', right:'destroy'):
        '''node is required; others are optional;
return a new node; and as-if destroy the old node

NOTE: node may be a leaf

undefined behavior if access the input "node"/"left"/"right" after return of this function


why broken?
    donot update me.parent
        i.e. me.parent refer to an old parent which may not have me as a child
    unless no proper_ancestors, i.e. node is a root
        if node is root ==>> new node is not broken
    

if node is leaf:
    node = Node(...)
    return node
if mutable:
    # node.parent.left/right = ?? without such update

    # update other property
    node.color = color
    node.entity = entity
    node.left = left
    node.right = right

    # update child property
    left.parent  = node if has .parent
    right.parent = node if -----------
    return node

if immutable:
    plain_left = to_plain(left)
    plain_right = to_plain(right)
    this = Node(entity, plain_left, plain_right)
    return (proper_ancestors node), this

'''
        raise NotImplementedError
    
    @abstractmethod
    def make_new_leaf_root(self):
        'return a leaf root'
        raise NotImplementedError

    def make_new_nonleaf_root(self, color, entity):
        'return a nonleaf root'
        new = self.make_new_leaf_root
        return self.unsafe_replace_to_broken_node(new(), color, entity, new(), new())

    

        



class SizedRedBlackTreeOpsABC(RedBlackTreeOpsABC):
    @abstractmethod
    def plain_root2root(self, plain_root):
    def nonleaf2plain_node(self, nonleaf):
        
    
    @abstractmethod
    def to_size(self, plain_nonleaf):
        '''return number of nonleaf nodes in the subtree rooted by nonleaf_node
should be O(1) operation

undefined behavior if nonleft_node is leaf

'''
        raise NotImplementedError
    
    








    










































            
        
            






        
        
        










