
__all__ = '''
    IKeyOrderedRedBlackTreeNodeOps__imodify
    '''.split()



from .abc import override
from seed.iters.ensure_sorted import ensure_sorted, ensure_strict_sorted

from .IKeyOrderedRedBlackTreeNodeOps import IKeyOrderedRedBlackTreeNodeOps
from ..RedBlackTreeNodeOps.IRedBlackTreeNodeOps__imodify import \
    IRedBlackTreeNodeOps__imodify
from ..TreeNodeOps.depth import verify_depth



class IKeyOrderedRedBlackTreeNodeOps__imodify(
        IKeyOrderedRedBlackTreeNodeOps
        , IRedBlackTreeNodeOps__imodify):
    '''
since entities are key-ordered, should not call
    method of IRedBlackTreeNodeOps__imodify directly

should avoid call rbt_iinsert_entity_at_leaf directly since "ordered"
    using iinsert_entity_as_first_of_tree/iinsert_entity_as_last_of_tree
    should avoid call rbt_from_entities directly since "ordered"




new_methods:
    from_sorted_entities

    find_and_iinsert_entity_as_first_or_last_of_tree

    find_and_iinsert_entity_of_tree_if_not_any_ex
    find_and_iinsert_key2entity_of_tree_if_not_any_ex
    find_and_iinsert_key2entity_of_tree_if_not_any_ex_ex


    find_and_iremove_first_or_last_entity_of_subtree
    find_and_ipop_first_or_last_entity_of_subtree
    find_and_idiscard_first_or_last_entity_of_subtree_ex

    find_and_ireplace_first_or_last_entity_of_subtree_ex_ex
    find_and_ireplace_first_or_last_entity_of_subtree_ex
    find_and_ireplace_first_or_last_entity_or_iinsert_entity_of_tree_ex
'''
    __slots__ = ()




    '''
    old version
            iremove_first_entity_of_subtree
            iremove_last_entity_of_subtree
            find_and_ireplace_first_entity_of_subtree
            find_and_ireplace_last_entity_of_subtree
            find_and_ireplace_first_entity_or_iinsert_entity_of_tree
            find_and_ireplace_last_entity_or_iinsert_entity_of_tree
            idiscard_first_entity_of_subtree
            idiscard_last_entity_of_subtree

            iinsert_entity_as_first_or_last_of_tree
            find_and_ireplace_first_or_last_entity_of_subtree
            find_and_ireplace_first_or_last_entity_or_iinsert_entity_of_tree
            idiscard_first_or_last_entity_of_subtree
            idiscard_first_or_last_entity_of_subtree_ex
            '''

    def from_sorted_entities(ops, num_entities, entities, *, reverse=False, strict=False):
        # O(n); use divide-and-conquer
        before = ops.key_lt if strict else ops.key_le
        entities = ensure_sorted(entities, reverse=reverse
                                , key=ops.entity2key, before=before)

        root = ops.rbt_from_entities(num_entities, entities, reverse=reverse)
        ops.check_KeyOrderedRedBlackTreeNode(root, True, strict=strict)
        return root




    def find_and_iinsert_entity_as_first_or_last_of_tree(ops, self, entity, last:bool):
        # -> new_root
        if not ops.is_root(self): raise TypeError # whole tree root

        root = self
        key = ops.entity2key(entity)

        find = ops.find_begin_or_end_leaf_of_subtree
        leaf = find(root, key, last)
        new_root = ops.rbt_iinsert_entity_at_leaf(leaf, entity)
        return new_root

    def find_and_iinsert_entity_of_tree_if_not_any_ex(ops, self, entity):
        # -> (does_iinsert:bool, root)
        # precondition:
        #   is_root(self)
        if not ops.is_root(self): raise TypeError # whole tree root

        key = ops.entity2key(entity)
        def key2entity(key):
            return entity
        return ops.find_and_iinsert_key2entity_of_tree_if_not_any_ex(self, key, key2entity)

    def find_and_iinsert_key2entity_of_tree_if_not_any_ex(ops, self, key, key2entity):
        # -> (does_iinsert:bool, root)
        # precondition:
        #   key_eq(key, entity2key(key2entity(key))) if key not exist
        #   is_root(self)
        if not ops.is_root(self): raise TypeError # whole tree root

        f = ops.find_and_iinsert_key2entity_of_tree_if_not_any_ex_ex
        does_iinsert, payload = f(self, key, key2entity, False)

        does_iinsert = bool(does_iinsert)
        may_triple, root = payload
        return does_iinsert, root

    def find_and_iinsert_key2entity_of_tree_if_not_any_ex_ex(ops, self, key, key2entity, last:bool):
        # -> (does_iinsert:bool, payload)
        # -> (does_iinsert:bool, (may_triple, root))
        # -> (True, (None, new_root)) | (False, ((nonleaf, entity_position, nonleaf_depth), old_root=self))
        # precondition:
        #   key_eq(key, entity2key(key2entity(key))) if key not exist
        #   is_root(self)
        if not ops.is_root(self): raise TypeError # whole tree root

        find = ops.find_maybe_first_or_last_nonleaf_ex_of_subtree
        node, may_pos, depth = find(self, 0, key, last) # self is root

        if ops.is_leaf(node):
            # not found
            # insert
            leaf = node
            entity = key2entity(key)
            key_ = ops.entity2key(entity)
            if not ops.key_eq(key, key_): raise ValueError('not key_eq(key, entity2key(key2entity(key)))')

            new_root = ops.rbt_iinsert_entity_at_leaf(leaf, entity)
            may_triple = None

            does_iinsert = True
            payload = (may_triple, new_root)
        else:
            # found
            # do nothing
            nonleaf = node
            entity_position = may_pos
            nonleaf_depth = depth
            old_root = self

            triple = (nonleaf, entity_position, nonleaf_depth)
            may_triple = triple

            does_iinsert = False
            payload = (may_triple, old_root)
        return does_iinsert, payload











    def find_and_iremove_first_or_last_entity_of_subtree(ops, self, key, last:bool):
        # -> new_root | raise KeyError
        old_entity, new_root = ops.find_and_ipop_first_or_last_entity_of_subtree(self, key, last)
        return new_root
    def find_and_ipop_first_or_last_entity_of_subtree(ops, self, key, last:bool, *, fdefault=None):
        # -> (old_entity, new_root) | raise KeyError | (fdefault(), old_root)
        idiscard_ex = ops.find_and_idiscard_first_or_last_entity_of_subtree_ex
        does_iremove, payload = idiscard_ex(self, key, last)
        if does_iremove:
            old_entity, new_root = payload
            return old_entity, new_root
        elif fdefault is None:
            raise KeyError(key)
        else:
            # if fdefault raise
            #   to_root_of_tree neednot  be called
            return fdefault(), ops.to_root_of_tree(self)
        raise logic-error


    def find_and_idiscard_first_or_last_entity_of_subtree_ex(ops, self, key, last:bool):
        # -> (does_iremove, (may_old_entity, root))
        # -> (True, (old_entity, new_root)) | (False, (None, old_root))
        #
        # self may not be root, but result must be root of whole tree
        #   whether iremove
        idiscard_ex = ops.__find_and_idiscard_first_or_last_entity_of_subtree_ex
        does_iremove, payload = idiscard_ex(self, 0, key, last)
        does_iremove = bool(does_iremove)

        if does_iremove:
            old_entity, new_root = payload

            may_old_entity = old_entity
            root = new_root
        else:
            leaf, leaf_depth = payload
            del leaf_depth
            old_root = ops.to_root_of_tree(leaf)

            may_old_entity = None
            root = old_root
        return does_iremove, (may_old_entity, root)

    def __find_and_idiscard_first_or_last_entity_of_subtree_ex(ops, self, depth, key, last:bool):
        # -> (does_iremove, payload)
        # -> (True, (old_entity, new_root)) | (False, (leaf, leaf_depth))
        assert verify_depth(depth)
        find = ops.find_maybe_first_or_last_nonleaf_ex_of_subtree
        node, may_pos, depth = find(self, depth, key, last)

        if ops.is_leaf(node):
            # not found
            leaf = node
            leaf_depth = depth

            does_iremove = False
            payload = (leaf, leaf_depth)
        else:
            nonleaf = node
            old_entity = ops.get_the_entity(nonleaf)
            new_root = ops.rbt_iremove_entity_at_nonleaf(nonleaf)

            does_iremove = True
            payload = old_entity, new_root
        return does_iremove, payload



    def find_and_ireplace_first_or_last_entity_of_subtree_ex(ops, self, entity, last:bool):
        # -> (old_entity, new_root) | raise KeyError
        f = ops.find_and_ireplace_first_or_last_entity_of_subtree_ex_ex
        does_ireplace, payload = f(self, 0, entity, last)
        if not does_ireplace:
            raise KeyError(ops.entity2key(entity)) # not found

        old_entity, new_root = payload
        return old_entity, new_root

    def find_and_ireplace_first_or_last_entity_of_subtree_ex_ex(ops, self, depth, entity, last:bool):
        # (does_ireplace, payload)
        # -> (True, (old_entity, new_root)) | (False, (leaf, leaf_depth))
        assert verify_depth(depth)
        key = ops.entity2key(entity)

        find = ops.find_maybe_first_or_last_nonleaf_ex_of_subtree
        node, may_pos, depth = find(self, depth, key, last)

        if ops.is_leaf(node):
            # not found
            leaf = node
            leaf_depth = depth

            does_ireplace = False
            payload = leaf, leaf_depth
        else:
            nonleaf = node

            old_entity = ops.get_the_entity(nonleaf)
            new_root = ops.rbt_irepalce_entity_at_nonleaf(nonleaf, entity)
            does_ireplace = True
            payload = (old_entity, new_root)
        return does_ireplace, payload




    def find_and_ireplace_first_or_last_entity_or_iinsert_entity_of_tree_ex(ops, self, entity, last:bool):
        # -> (does_iinsert:bool, (may_old_entity, new_root))
        # -> (True, (None, new_root)) | (False, (old_entity, new_root))
        if not ops.is_root(self): raise TypeError # whole tree root

        f = ops.find_and_ireplace_first_or_last_entity_of_subtree_ex_ex
        does_ireplace, payload = f(self, 0, entity, last)

        if not does_ireplace:
            # not found
            leaf, leaf_depth = payload

            does_iinsert = True
            may_old_entity = None
            new_root = ops.rbt_iinsert_entity_at_leaf(leaf, entity)
        else:
            old_entity, new_root = payload

            does_iinsert = False
            may_old_entity = old_entity
        return does_iinsert, (may_old_entity, new_root)


if __name__ == '__main__':
    XXX = IKeyOrderedRedBlackTreeNodeOps__imodify

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)




