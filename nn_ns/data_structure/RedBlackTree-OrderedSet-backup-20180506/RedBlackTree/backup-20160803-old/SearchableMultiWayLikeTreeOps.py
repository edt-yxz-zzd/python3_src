
'''
inorder:
    R -> {A, B, C}
    ==>> inorder(R) = inorder(A) + [(R,1)] + inorder(B) + [(R,2)] + inorder(C)
    inorder(leaf) = [leaf]

nonleaf_entity_pos = (nonleaf, entity_pos)
entity_ptr: # entity_pointer
    (prev_leaf, (curr_nonleaf, curr_innode_entity_pos), succ_leaf)
    (last_tree_leaf,) 
'''

from .SearchableMultiWayLikeTreeOpsABC import \
     SearchableMultiWayLikeTreeOpsABC, \
     SearchableMultiWayLikeTreeOpsWithParentABC


##def is_empty_innode_range(self, nonleaf_node, innode_begin, innode_end):
##    'why need a node?? ; equal test; NOTE the order, cannot be (end, begin)'
##    assert isinstance(self, SearchableMultiWayLikeTreeOpsABC)
##    for _ in self.iter_innode_range(nonleaf_node, innode_begin, innode_end):
##        return False
##    return True
def is_empty_innode_range(self, nonleaf_node, innode_begin, innode_end):
    a = []
    return a is next(self.iter_innode_range(nonleaf_node, innode_begin, innode_end), a)

def succ_innode_pos_or_raise(self, nonleaf_node, innode_begin, innode_end):
    return next(self.iter_innode_range(nonleaf_node, innode_begin, innode_end))

def prev_innode_pos_or_raise(self, nonleaf_node, innode_begin, innode_end):
    return next(self.iter_reversed_innode_range(nonleaf_node, innode_begin, innode_end))

def raise_if_empty_range(self, nonleaf_node, innode_begin, innode_end):
    succ_innode_pos_or_raise(self, nonleaf_node, innode_begin, innode_end)


    
    
def find_begin(self, node, key):
    assert isinstance(self, SearchableMultiWayLikeTreeOpsABC)

    while not self.is_leaf(node):
        begin, _ = self.find_innode_range(node, key)
        node = self.get_child(node, begin)
    return node

def find_end(self, node, key):
    assert isinstance(self, SearchableMultiWayLikeTreeOpsABC)

    while not self.is_leaf(node):
        _, end = self.find_innode_range(node, key)
        node = self.get_child(node, end)
    return node # since node knowns parents, node is a tree position

def find_range(self, node, key):
    assert isinstance(self, SearchableMultiWayLikeTreeOpsABC)

    while not self.is_leaf(node):
        begin, end = self.find_innode_range(node, key)
        if begin != end:
            break
        node = self.get_child(node, begin)
    else:
        return node
    left = self.get_child(node, begin)
    right = self.get_child(node, end)
    return find_begin(self, left, key), find_end(self, right, key)


def horizontal_succ(self, node):
    'ERROR: since rb tree no same depth'
    assert isinstance(self, SearchableMultiWayLikeTreeOpsABC)
    self.to_parent_position(node)
    raise NotImplementedError



def to_first_child(self, nonleaf):
    assert isinstance(self, SearchableMultiWayLikeTreeOpsABC)
    assert not self.is_leaf(nonleaf)
    
    first_pos = self.get_innode_begin(nonleaf)
    first = self.innode_pos2child(nonleaf, first_pos)
    return first
def to_last_child(self, nonleaf):
    assert isinstance(self, SearchableMultiWayLikeTreeOpsABC)
    assert not self.is_leaf(nonleaf)
    
    last_pos = self.get_innode_entity_end(nonleaf) # e.end is c.last
    last = self.innode_pos2child(nonleaf, last_pos)
    return last

    

def to_first_leaf(self, node):
    assert isinstance(self, SearchableMultiWayLikeTreeOpsABC)
    while not self.is_leaf(node):
        node = self.to_first_child(node)
    return node
def to_last_leaf(self, node):
    assert isinstance(self, SearchableMultiWayLikeTreeOpsABC)
    while not self.is_leaf(node):
        node = self.to_last_child(node)
    return node

def to_range(self, node):
    assert isinstance(self, SearchableMultiWayLikeTreeOpsABC)
    begin = to_first_leaf(node)
    end = to_last_leaf(node)
    return begin, end


def nonleaf_entity_pos_to_inorder_prev_child(self, nonleaf_entity_pos):
    nonleaf, entity_pos = nonleaf_entity_pos
    assert isinstance(self, SearchableMultiWayLikeTreeOpsABC)
    assert not self.is_leaf(nonleaf)
    prev_child_pos = entity_pos
    prev_child = self.innode_pos2child(nonleaf, prev_child_pos)
    return prev_child
def nonleaf_entity_pos_to_inorder_succ_child(self, nonleaf_entity_pos):
    nonleaf, entity_pos = nonleaf_entity_pos
    assert isinstance(self, SearchableMultiWayLikeTreeOpsABC)
    assert not self.is_leaf(nonleaf)
    prev_child_pos = entity_pos
    child_end = self.get_innode_child_end(nonleaf)
    succ_child_pos = succ_innode_pos_or_raise(self, nonleaf, prev_child_pos, child_end)
    succ_child = self.innode_pos2child(nonleaf, succ_child_pos)
    return succ_child
def nonleaf_entity_pos_to_inorder_prev_leaf(self, nonleaf_entity_pos):
    prev_child = nonleaf_entity_pos_to_inorder_prev_child(self, nonleaf_entity_pos)
    return to_last_leaf(self, prev_child)
def nonleaf_entity_pos_to_inorder_succ_leaf(self, nonleaf_entity_pos):
    succ_child = nonleaf_entity_pos_to_inorder_succ_child(self, nonleaf_entity_pos)
    return to_first_leaf(self, succ_child)











########################################################################
########################################################################
################# SearchableMultiWayLikeTreeOpsWithParentABC ###########
########################################################################
########################################################################





def is_first_child(self, nonroot):
    assert isinstance(self, SearchableMultiWayLikeTreeOpsWithParentABC)
    assert not self.is_root(nonroot)

    parent = self.unsafe_to_parent(nonroot)
    my_pos = self.to_parent_innode_pos(nonroot)
    first_pos = self.get_innode_begin(nonroot)
    return self.is_empty_innode_range(parent, first_pos, my_pos)
def is_last_child(self, nonroot):
    assert isinstance(self, SearchableMultiWayLikeTreeOpsWithParentABC)
    assert not self.is_root(nonroot)

    parent = self.unsafe_to_parent(nonroot)
    my_pos = self.to_parent_innode_pos(nonroot)
    last_pos = self.get_innode_entity_end(nonroot)
    return self.is_empty_innode_range(parent, my_pos, last_pos)







def leaf_to_inorder_succ_nonleaf_entity_pos_or_raise(self, leaf):
    'StopIteration'
    assert isinstance(self, SearchableMultiWayLikeTreeOpsWithParentABC)
    assert self.is_leaf(leaf)

    node = leaf
    while not self.is_root(node):
        if not is_last_child(self, node):
            break
        node = self.unsafe_to_parent(node)
    else:
        # root --[right]*-->> leaf
        # end of inorder
        raise StopIteration
    assert not self.is_root(node)
    assert not is_last_child(self, node)
    parent = self.unsafe_to_parent(node)
    curr = self.to_parent_innode_pos(node)
    end = self.get_innode_entity_end(parent)
    succ_pos = succ_innode_pos_or_raise(self, parent, curr, end)
    return (parent, succ_pos)


    
def leaf_to_inorder_prev_nonleaf_entity_pos_or_raise(self, leaf):
    'StopIteration'
    assert isinstance(self, SearchableMultiWayLikeTreeOpsWithParentABC)
    assert self.is_leaf(leaf)

    node = leaf
    while not self.is_root(node):
        if not is_first_child(self, node):
            break
        node = self.unsafe_to_parent(node)
    else:
        # root --[left]*-->> leaf
        # begin of inorder
        raise StopIteration
    assert not self.is_root(node)
    assert not is_first_child(self, node)
    parent = self.unsafe_to_parent(node)
    curr = self.to_parent_innode_pos(node)
    begin = self.get_innode_entity_begin(parent)
    prev_pos = prev_innode_pos_or_raise(self, parent, begin, curr)
    return (parent, prev_pos)




def find_last_nonleaf_entity_pos_or_raise(self, node, key):
    end = find_end(self, node, key)
    last, pos = leaf_to_inorder_prev_nonleaf_entity_pos_or_raise(self, end)
    last_key = self.to_key(self.innode_pos2entity(last, pos))
    if self.key_lt(last_key, key):
        # last.key != key
        raise StopIteration
    return last, pos
def find_first_nonleaf_entity_pos_or_raise(self, node, key):
    begin = find_begin(self, node, key)
    first, pos = leaf_to_inorder_succ_nonleaf_entity_pos_or_raise(self, begin)
    first_key = self.to_key(self.innode_pos2entity(first, pos))
    if self.key_lt(first_key, key):
        # first.key != key
        raise StopIteration
    return first, pos
    








############  entity_pointer ############
# using fixed_node_eq

'''
entity_ptr: # entity_pointer
    (prev_leaf, (curr_nonleaf, curr_innode_entity_pos), succ_leaf)
    (last_tree_leaf,)
'''

def __last_tree_leaf_to_prev_ptr(self, last_tree_leaf):
    # if prev_ptr is None ==>> empty tree
    try:
        last_tree_nonleaf_entity_pos = leaf_to_inorder_prev_nonleaf_entity_pos_or_raise(self, last_tree_leaf)
    except StopIteration:
        # empty tree
        the_only_leaf = last_tree_leaf
        prev_ptr = None
    else:
        prev_leaf = nonleaf_entity_pos_to_inorder_prev_leaf(self, last_tree_nonleaf_entity_pos)
        prev_ptr = prev_leaf, last_tree_nonleaf_entity_pos, last_tree_leaf
    return prev_ptr

def leaf2entity_ptr(self, leaf):
    try:
        nonleaf_entity_pos = leaf_to_inorder_succ_nonleaf_entity_pos_or_raise(self, leaf)
    except StopIteration:
        last_tree_leaf = leaf
        ptr = last_tree_leaf,
    else:
        succ_leaf = nonleaf_entity_pos_to_inorder_succ_leaf(self, nonleaf_entity_pos)
        ptr = leaf, nonleaf_entity_pos, succ_leaf
    return ptr
def leaf2nonend_entity_ptr_or_raise(self, leaf):
    # may raise here
    nonleaf_entity_pos = leaf_to_inorder_succ_nonleaf_entity_pos_or_raise(self, leaf)

    succ_leaf = nonleaf_entity_pos_to_inorder_succ_leaf(self, nonleaf_entity_pos)
    ptr = leaf, nonleaf_entity_pos, succ_leaf
    return ptr

def leaf2prev_entity_ptr_or_raise(self, leaf):
    # prev ==>> nonend
    # may raise here
    nonleaf_entity_pos = leaf_to_inorder_prev_nonleaf_entity_pos_or_raise(self, leaf)

    prev_leaf = nonleaf_entity_pos_to_inorder_prev_leaf(self, nonleaf_entity_pos)
    ptr = prev_leaf, nonleaf_entity_pos, leaf
    return ptr


def to_entity_ptr_begin(self, node):
    first_leaf = to_first_leaf(self, node)
    return leaf2entity_ptr(self, first_leaf)
def to_entity_ptr_end(self, node):
    last_leaf = to_last_leaf(self, node)
    return leaf2entity_ptr(self, last_leaf)

def is_end_tree_ptr(entity_ptr):
    return len(entity_ptr) == 1
def entity_ptr2prev_leaf(entity_ptr):
    return entity_ptr[0]
def nonend_entity_ptr2nonleaf_entity_pos(nonend_entity_ptr):
    return __nonend_ptr2member(nonend_entity_ptr, 1)
def nonend_entity_ptr2succ_leaf(nonend_entity_ptr):
    return __nonend_ptr2member(nonend_entity_ptr, 2)

def __nonend_ptr2member(nonend_entity_ptr, idx):
    try:
        return nonend_entity_ptr[idx]
    except:
        if is_end_tree_ptr(nonend_entity_ptr):
            raise ValueError('is_end_tree_ptr')
        raise

def nonend_entity_ptr2entity(self, nonend_ptr):
    (nonleaf, pos) = nonend_entity_ptr2nonleaf_entity_pos(nonend_ptr)
    return self.innode_pos2entity(nonleaf, pos)

##def entity_ptr2nonleaf_entity_pos_or_raise(entity_ptr):
##    if is_end_tree_ptr(entity_ptr):
##        raise StopIteration
##    return entity_ptr[1]
##def entity_ptr2entity_or_raise(self, entity_ptr):
##    (nonleaf, pos) = entity_ptr2nonleaf_entity_pos_or_raise(entity_ptr)
##    return self.innode_pos2entity(nonleaf, pos)








def is_empty_entity_ptr_range(self, begin_ptr, end_ptr):
    a = entity_ptr2prev_leaf(begin_ptr)
    b = entity_ptr2prev_leaf(end_ptr)
    return self.fixed_node_eq(a, b)

def iter_entity_ptrs(self, begin_ptr, end_ptr):
    'iter nonend_tree_ptrs'
    begin_leaf = entity_ptr2prev_leaf(begin_ptr)
    end_leaf = entity_ptr2prev_leaf(end_ptr)
    while self.fixed_node_eq(begin_leaf, end_leaf):
        try:
            first_ptr = leaf2nonend_entity_ptr_or_raise(self, begin_leaf)
        except StopIteration:
            end_tree_leaf = begin_leaf
            raise ValueError('not begin_ptr <= end_ptr')
        yield first_ptr
        begin_leaf = entity_ptr2succ_leaf(first_ptr)



def iter_reversed_entity_ptrs(self, begin_ptr, end_ptr):
    'iter nonend_tree_ptrs'
    begin_leaf = entity_ptr2prev_leaf(begin_ptr)
    end_leaf = entity_ptr2prev_leaf(end_ptr)
    while self.fixed_node_eq(begin_leaf, end_leaf):
        try:
            last_ptr = leaf2prev_entity_ptr_or_raise(self, end_leaf)
        except StopIteration:
            begin_tree_leaf = end_leaf
            raise ValueError('not begin_ptr <= end_ptr')
        yield last_ptr
        end_leaf = entity_ptr2prev_leaf(last_ptr)


def nonend_entity_ptrs2iter_entities(self, nonend_ptrs):
    for nonend_ptr in nonend_ptrs:
        yield nonend_entity_ptr2entity(self, nonend_ptr)
    

def iter_entities(self, begin_ptr, end_ptr):
    return nonend_entity_ptrs2iter_entities(iter_entity_ptrs(self, begin_ptr, end_ptr))

def iter_reversed_entities(self, begin_ptr, end_ptr):
    return nonend_entity_ptrs2iter_entities(iter_reversed_entity_ptrs(self, begin_ptr, end_ptr))




























