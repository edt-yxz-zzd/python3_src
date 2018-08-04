




'''
def __leaf_to_next_nonleaf_leaf(
    self, leaf, leaf_to_next_nonleaf_or_raise, nonleaf_to_next_leaf):
    nonleaf = leaf_to_next_nonleaf_or_raise(self, leaf)
    return nonleaf, nonleaf_to_next_leaf(nonleaf)
def leaf_to_prev_nonleaf_leaf_or_raise(self, leaf):
    # raise StopIteration
    return __leaf_to_next_nonleaf_leaf(
        self, leaf, leaf_to_prev_nonleaf_or_raise, nonleaf_to_inorder_prev_leaf)
def leaf_to_succ_nonleaf_leaf_or_raise(self, leaf):
    # raise StopIteration
    return __leaf_to_next_nonleaf_leaf(
        self, leaf, leaf_to_succ_nonleaf_or_raise, nonleaf_to_inorder_succ_leaf)


    

    

def unjust_or_raise(maybe):
    if not maybe:
        raise StopIteration
    x, = maybe
    return x
def leaf_to_prev_nonleaf_or_raise(self, leaf):
    # raise StopIteration
    maybe = leaf_to_maybe_inorder_prev_nonleaf(self, leaf)
    return unjust_or_raise(maybe)

def leaf_to_succ_nonleaf_or_raise(self, leaf):
    # raise StopIteration
    maybe = leaf_to_maybe_inorder_succ_nonleaf(self, leaf)
    return unjust_or_raise(maybe)

def find_maybe_last(self, node, key):
    end = find_end(self, node, key)
    maybe_last = leaf_to_maybe_inorder_prev_nonleaf(self, end)
    if maybe_last:
        last, = maybe_last
        last_key = self.to_key(self.to_entity(last))
        if self.key_lt(last_key, key):
            # last < key
            # hence begin == end
            maybe_last = ()
    return maybe_last
def find_maybe_first(self, node, key):
    begin = find_begin(self, node, key)
    maybe_first = leaf_to_maybe_inorder_succ_nonleaf(self, begin)
    if maybe_first:
        first, = maybe_first
        first_key = self.to_key(self.to_entity(first))
        if self.key_lt(key, first_key):
            # key < first
            # hence begin == end
            maybe_first = ()
    return maybe_first


def iter_rdirections(self, node):
    'me <- ... <- root'
    while not self.is_root(node):
        yield to_direction(node)
        node = self.unsafe_to_parent(node)

def to_rdirections(self, node):
    'me <- ... <- root'
    ls = list(iter_rdirections(self, node))
    assert len(ls) == self.to_depth(node)
    return ls
    
'''

'''

# without using fixed_node_eq
def __iter_nonleaves_from_leaf(self, leaf,
                             leaf2maybe_next_nonleaf,
                             nonleaf2next_leaf):
    assert self.is_leaf(leaf)
        
    while True:
        maybe_nonleaf = leaf2maybe_next_nonleaf(leaf)
        if not maybe_nonleaf:
            break

        nonleaf, = maybe_nonleaf
        yield self.to_entity(nonleaf)
        leaf = nonleaf2next_leaf(self, nonleaf)
    return
    
def iter_subtree_and_succs(self, node):
    'inorder nonleaves; e.g. iter_subtree_and_succs(root) == iter(tree)'
    return __iter_nonleaves_from_leaf(
                        self,
                        to_first_leaf(node),
                        leaf_to_maybe_inorder_succ_nonleaf,
                        nonleaf_to_inorder_succ_leaf)
def iter_reversed_subtree_and_prevs(self, node):
    'inorder nonleaves; e.g. iter_reversed_subtree_and_prevs(root) == iter_reversed(tree)'
    return __iter_nonleaves_from_leaf(
                        self,
                        to_last_leaf(node),
                        leaf_to_maybe_inorder_prev_nonleaf,
                        nonleaf_to_inorder_prev_leaf)
    



# using fixed_node_eq
def iter_subtree(self, node):
    begin, end = to_range(self, node)
    return iter_nonleaves(self, begin, end)
def iter_reversed_subtree(self, node):
    begin, end = to_range(self, node)
    return iter_reversed_nonleaves(self, begin, end)


def iter_nonleaves(self, begin, end):
    assert self.is_leaf(begin)
    assert self.is_leaf(end)

    while not self.fixed_node_eq(begin, end):
        maybe_nonleaf = leaf_to_maybe_inorder_succ_nonleaf(self, begin)
        if not maybe_nonleaf:
            raise ValueError('not begin <= end')
        nonleaf, = maybe_nonleaf
        yield nonleaf
        begin = nonleaf_to_inorder_succ_leaf(nonleaf)

def iter_reversed_nonleaves(self, begin, end):
    assert self.is_leaf(begin)
    assert self.is_leaf(end)
    
    while not self.fixed_node_eq(begin, end):
        maybe_nonleaf = leaf_to_maybe_inorder_prev_nonleaf(self, end)
        if not maybe_nonleaf:
            raise ValueError('not begin <= end')
        nonleaf, = maybe_nonleaf
        yield nonleaf
        end = nonleaf_to_inorder_prev_leaf(nonleaf)
    
'''
