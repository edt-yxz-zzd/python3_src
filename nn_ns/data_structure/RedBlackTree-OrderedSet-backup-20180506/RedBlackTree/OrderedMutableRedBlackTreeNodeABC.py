
from .RedBlackTreeNodeABC import MutableRedBlackTreeNodeABC
from .OrderedUnbalancedMultiWayTreeNodeABC import OrderedBinaryTreeNodeABC
from seed.iters.ensure_sorted import ensure_sorted, ensure_strict_sorted

class OrderedMutableRedBlackTreeNodeABC(MutableRedBlackTreeNodeABC,
                                        OrderedBinaryTreeNodeABC):
    # should avoid call insert_entity_at_leaf directly since "ordered"
    #   using insert_entity_as_first/insert_entity_as_last
    # should avoid call from_entities directly since "ordered"

    @classmethod
    def from_sorted_entities(cls, entities, reverse=False, strict=False):
        # TODO: O(n); maybe use divide-and-conquer
        # curr impl: O(n*log(n))
        before = cls.key_lt if strict else cls.key_le
        entities = ensure_sorted(entities, reverse=reverse
                                , key=cls.entity2key, before=before)
        return cls.from_entities(entities)


    def iter_entities(self):
        yield self.entity
    def iter_reversed_entities(self):
        yield self.entity

    # root -> root
    #   should follow methods be tree methods instead of node methods?
    def insert_entity_as_first(self, entity):
        assert self.is_root()
        key = self.entity2key(entity)
        leaf = self.subtree_find_begin_leaf(key)
        return leaf.insert_entity_at_leaf(entity)
    def insert_entity_as_last(self, entity):
        assert self.is_root()
        key = self.entity2key(entity)
        leaf = self.subtree_find_end_leaf(key)
        return leaf.insert_entity_at_leaf(entity)


    def subtree_contains(self, key):
        node = self.subtree_find_maybe_first_nonleaf(key)
        return node.is_nonleaf()
    def subtree_get_first_entity(self, key):
        node = self.subtree_find_maybe_first_nonleaf(key)
        if node.is_leaf():
            raise KeyError(key)
        return node.entity
    def subtree_get_last_entity(self, key):
        node = self.subtree_find_maybe_last_nonleaf(key)
        if node.is_leaf():
            raise KeyError(key)
        return node.entity
    def subtree_find_maybe_first_nonleaf(self, key):
        # if return leaf, then not found
        leaf = self.subtree_find_begin_leaf(key)
        try:
            nonleaf = leaf.leaf_inorder_succ_nonleaf()
        except StopIteration:
            return leaf
        k = self.entity2key(nonleaf.entity)
        if self.key_lt(key, k):
            # key < k
            return leaf
        return nonleaf
    def subtree_find_maybe_last_nonleaf(self, key):
        # if return leaf, then not found
        leaf = self.subtree_find_end_leaf(key)
        try:
            nonleaf = leaf.leaf_inorder_prev_nonleaf()
        except StopIteration:
            return leaf
        k = self.entity2key(nonleaf.entity)
        if self.key_lt(k, key):
            # k < key
            return leaf
        return nonleaf


    def subtree_remove_first_entity(self, key):
        node = self.subtree_find_maybe_first_nonleaf(key)
        if node.is_leaf():
            raise KeyError(key)
        return node.remove_entity_at_nonleaf()

    def subtree_remove_last_entity(self, key):
        node = self.subtree_find_maybe_last_nonleaf(key)
        if node.is_leaf():
            raise KeyError(key)
        return node.remove_entity_at_nonleaf()




