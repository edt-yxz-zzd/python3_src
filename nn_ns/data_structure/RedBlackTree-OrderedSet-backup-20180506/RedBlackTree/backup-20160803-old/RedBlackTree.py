
'''
entity_pointer = (last_leaf,) | (leaf, nonleaf, leaf)


'''

from .RedBlackTreeOpsABC import RedBlackTreeOps, insert_at_end

class RedBlackTree:
    '''
using nonleaf as position, so we can dereference faster
    and last_leaf[root] as end postion
'''
    def __init__(self, aRedBlackTreeOps, iterable=()):
        assert isinstance(aRedBlackTreeOps, RedBlackTreeOps):
        self.__ops = aRedBlackTreeOps
        self.__tree = self.__ops.new_leaf_root()
        self.__size = 0
        self.update_at_end(iterable)
    def __len__(self):
        return self.__size

    def __iter__(self):
        'inorder'
        return self.__iter(iter_subtree_and_succs)
    def __reversed__(self):
        'revesed inorder'
        return self.__iter(iter_reversed_subtree_and_prevs)
        
    def __iter(self, f):
        return map(self.__ops.to_entity, iter_subtree_and_succs(self.__ops, self.__tree))


    def begin(self)
    def end(self)
    def iter_ptrs(self, begin, end)
    def iter_reversed_ptrs(self, begin, end)
    def ptr2entity(self, ptr)
    def find_begin
    def find_end
    def find_first_ptr # differ find_begin, if range empty raise
    def find_last_ptr
    def insert_at(self, ptr, iterable)
    def remove_between(self, begin, end)
    def clear
    



    ########
    def iter(self, begin, end) # -> entity
    def iter_reversed(self, begin, end)
    def update/insert/remove/discard_at_end/begin
    
    

    
    def iter(self, begin, end)
        
    def get_begin(self):
        return to_first_leaf(self.__ops, self.__tree)
    def get_end(self):
        return to_last_leaf(self.__ops, self.__tree)
    def prev_entity_pos(self, leaf):
        # StopIteration
        nonleaf, prev_leaf = leaf_to_prev_nonleaf_leaf_or_raise(self.__ops, leaf)
        return self.__ops.to_entity(nonleaf)
    def succ_entity_pos(self, leaf):
        # StopIteration
        nonleaf, prev_leaf = leaf_to_succ_nonleaf_leaf_or_raise(self.__ops, leaf)
        return self.__ops.to_entity(nonleaf)
    def pos2entity(self, leaf):
    def find_begin(self, key):
        return find_begin(self.__ops, self.__tree, key)
    def find_end(self, key):
        return find_end(self.__ops, self.__tree, key)
    def pos_equal(self, begin, end):
    def iter(self, begin, end):
        return iter_nonleaves(self.__ops, begin, end)
    def iter_reversed(self, begin, end):
        return iter_reversed_nonleaves(self.__ops, begin, end)
        
        
        
    def update_at_end(self, iterable):
        for _ in map(self.insert_at_end, iterable):pass
    def update_at_begin(self, iterable):
        for _ in map(self.insert_at_begin, iterable):pass

    def __insert(self, f, entity):
        self.__tree = f(self.__ops, self.__tree, entity)
        self.__size += 1
    def insert_at_end(self, entity):
        'insert at end if equal range is (begin, end)'
        self.__insert(insert_at_end, entity)
    def insert_at_begin(self, entity):
        'insert at begin if equal range is (begin, end)'
        self.__insert(insert_at_begin, entity)

    def __discard(self, f, key):
        # return whether perform discard
        is_new, root = f(self.__ops, self.__tree, key)
        if is_new:
            self.__tree = root
            self.__size -= 1
        return is_new
        
    def discard_first(self, key):
        # return whether perform discard
        return self.__discard(discard_first, key)
    def discard_last(self, key):
        # return whether perform discard
        return self.__discard(discard_last, key)

    def __remove(self, f, key):
        if not f(key):
            raise KeyError('remove but not found: {}'.format(key))
    def remove_first(self, key):
        self.__remove(self.discard_first, key)
        
    def remove_last(self, key):
        self.__remove(self.discared_last, key)
    





        
    






