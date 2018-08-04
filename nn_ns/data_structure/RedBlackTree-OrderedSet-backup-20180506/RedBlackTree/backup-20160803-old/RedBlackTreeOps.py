
'''

TODO:
    to support insert_at(node, iterable) and remove_between(begin, end)
    return root, depth
    depth = None | depth where restructure happened
    if we want to refresh other nodes after one modification
        we save the directions first
        modify
        use "depth" to refresh ...


    but it seems too tedious
        and since SizedRBTree is more stable (can index by integer)
        I will not add this feature
    
'''

def insert_at_begin(self, node, entity):
    key = self.to_key(entity)
    leaf = find_begin(self, root, key)
    return insert_at_leaf(self, leaf, entity)
def insert_at_end(self, node, entity):
    'usually node should be root, but not required'
    key = self.to_key(entity)
    leaf = find_end(self, root, key)
    return insert_at_leaf(self, leaf, entity)

def discard_first(self, node, key):
    # return (is_new, node)
    maybe_first = find_maybe_first(self, node, key)
    return _discard_maybe_nonleaf(self, node, maybe_first)
    
def discard_last(self, node, key):
    # return (is_new, node)
    maybe_last = find_maybe_last(self, node, key)
    return _discard_maybe_nonleaf(self, node, maybe_last)

def _discard_maybe_nonleaf(self, node, maybe_nonleaf):
    if not maybe_nonleaf:
        return False, node
    nonleaf, = maybe_nonleaf
    return True, remove_nonleaf(self, nonleaf)


