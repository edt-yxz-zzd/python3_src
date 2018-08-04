
from .TreeNodeABC import TreeNodeABC, OrientedTreeNodeABC, BinaryTreeNodeABC
from seed.types.ABC import not_implemented
from abc import abstractmethod

    
class OrderedTreeNodeABC(OrientedTreeNodeABC):
    
    @classmethod
    def key_lt(cls, key0, key1):
        try:
            return key0 < key1
        except TypeError:
            # sorted([1,'a'])
            # TypeError: unorderable types: str() < int()
            print(key0, key1)
            raise
            # bug: what if orderable(A,B)(B,C) but not (A,C)??
            #      a>b>c but A<C??
            if type(key0) is not type(key1):
                return type(key0) < type(key1)
            return id(key0) < id(key1)

    @classmethod
    def key_eq(cls, key0, key1):
        return not cls.key_lt(key0, key1) and\
               not cls.key_lt(key1, key0)
    @classmethod
    def entity2key(cls, entity):
        return entity
    
        
class OrderedUnbalancedMultiWayTreeNodeABC(OrderedTreeNodeABC):
    # assume ordered by key_lt

    @property
    def num_entities(self):
        assert self.is_nonleaf()
        return self.num_children - 1
    @not_implemented
    def iter_entities(self):...
    @not_implemented
    def iter_reversed_entities(self):...

    def iter_innode_position_entity_pairs(self):
        # NOTE: not output innode_last (== child_last == entity_end)
        return zip(self.iter_innode_positions(), self.iter_entities())

    def iter_reversed_innode_position_entity_pairs(self):
        # NOTE: not output innode_last (== child_last == entity_end)
        return zip(self.iter_reversed_innode_positions(),
                   self.iter_reversed_entities())

  # nonleaf
  
    # entity_begin == child_begin
    # entity_end == child_last
    def get_innode_begin(self):
        return self.innode_first_position
            
    def get_innode_entity_end(self):
        return self.innode_last_position

    
    # entities[begin:end] contains all entities which equal to key
    def find_innode_range(self, key):
        return self.find_innode_begin(key), self.find_innode_end(key)
    @abstractmethod
    def find_innode_begin(self, key):
        for pos, e in self.iter_innode_position_entity_pairs():
            k = self.entity2key(e)
            if not self.key_lt(k, key):
                # not k < key ==>> k >= key ==>> key <= k
                break
        else:
            pos = self.get_innode_entity_end()
        return pos
    @abstractmethod
    def find_innode_end(self, key):
        for pos, e in self.iter_innode_position_entity_pairs():
            k = self.entity2key(e)
            if self.key_lt(key, k):
                # key < k
                break
        else:
            pos = self.get_innode_entity_end()
        return pos



    def subtree_find_begin_leaf(self, key):
        while not self.is_leaf():
            pos = self.find_innode_begin(key)
            self = self.get_child_at_pos(pos)
        return self
    def subtree_find_end_leaf(self, key):
        while not self.is_leaf():
            pos = self.find_innode_end(key)
            self = self.get_child_at_pos(pos)
        return self
    


        
class OrderedBinaryTreeNodeABC(BinaryTreeNodeABC,
                               OrderedUnbalancedMultiWayTreeNodeABC):
    def find_innode_begin(self, key):
        return super().find_innode_begin(key)
    def find_innode_end(self, key):
        return super().find_innode_end(key)


    


