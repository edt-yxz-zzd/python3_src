
__all__ = '''
    IKeyOrderedUnbalancedMultiWayTreeNodeOps
    '''.split()

from .abc import not_implemented, override, abstractmethod
from .IKeyOrderedTreeNodeOps import IKeyOrderedTreeNodeOps
from ..TreeNodeOps.IOrientedTreeNodeOps__inorder import \
    IOrientedTreeNodeOps__inorder
from ..TreeNodeOps.depth import verify_depth
from ..UnbalancedMultiWayTreeNodeOps.IUnbalancedMultiWayTreeNodeOps import\
    IUnbalancedMultiWayTreeNodeOps

from seed.iters.is_sorted import is_sorted



class IKeyOrderedUnbalancedMultiWayTreeNodeOps(
        IKeyOrderedTreeNodeOps
        , IUnbalancedMultiWayTreeNodeOps
        ):
        #IKeyOrderedTreeNodeOps, IOrientedTreeNodeOps__inorder):
    '''assume ordered by key_lt
    assume nonleaf.num_children > 0 since num_entities = num_children-1
    assume nonleaf.num_children >= 2 since inorder


entity_position == innode_position
    except:
        entity_position != innode_last == entity_end

IUnbalancedMultiWayTreeNodeOps's methods
    `get_entity_at
    `iter_entities_of_nonleaf
    `iter_reversed_entities_of_nonleaf

    get_num_entities_of_nonleaf
    calc_num_entities_of_subtree
    iter_innode_position_entity_pairs_of_nonleaf
    iter_reversed_innode_position_entity_pairs_of_nonleaf
    get_innode_entity_begin
    get_innode_entity_end

new methods:
    `find_innode_range_of_nonleaf
    `find_innode_begin_of_nonleaf
    `find_innode_end_of_nonleaf

    get_key_at

    # find
    subtree_contains

    find_begin_leaf_ex_of_subtree
    find_end_leaf_ex_of_subtree
    find_begin_leaf_of_subtree
    find_end_leaf_of_subtree

    find_maybe_first_nonleaf_ex_of_subtree
    find_maybe_last_nonleaf_ex_of_subtree
    find_first_entity_of_subtree
    find_last_entity_of_subtree


    find_begin_or_end_leaf_of_subtree
    find_begin_or_end_leaf_ex_of_subtree
    find_first_or_last_entity_of_subtree
    find_maybe_first_or_last_nonleaf_ex_of_subtree
'''
    __slots__ = ()

    @override
    def why_not_subtree_ok(ops, self, **kwargs):
        # kwargs readonly, should not remove key from it
        #   i.e. donot override: def is_subtree_ok(ops, self, *, as_root=..., **kwargs)
        return (ops.why_not_entities_key_ordered(
                    self, strict=kwargs['strict'])
                + super().why_not_subtree_ok(self, **kwargs)
                )
    def check_entities_are_key_ordered(ops, self, *, strict:bool):
        reasons = ops.why_not_entities_key_ordered(self, strict=strict)
        if reasons: raise ValueError(reasons)
    def why_not_entities_key_ordered(ops, self, *, strict:bool):
        # -> reasons
        if ops.are_entities_key_ordered(self, strict=strict):
            return ()
        return ('entities not sorted',)

    def are_entities_key_ordered(ops, self, *, strict:bool):
        before = ops.key_lt if strict else ops.key_le
        entities = ops.iter_entities_of_subtree(self)
        return is_sorted(entities, key=ops.entity2key, before=before)

  # nonleaf
    def get_key_at(ops, self, entity_position):
        # like get_child_at
        assert entity_position != ops.get_innode_entity_end(self)
        return ops.entity2key(ops.get_entity_at(self, entity_position))

    @abstractmethod
    def find_innode_range_of_nonleaf(ops, self, key):
        # useless
        # key -> [begin, end) of self_node not self_subtree
        # entities[begin:end] contains all entities which equal to key
        return (ops.find_innode_begin_of_nonleaf(self, key)
                , ops.find_innode_end_of_nonleaf(self, key)
                )

    @abstractmethod
    def find_innode_begin_of_nonleaf(ops, self, key):
        # to be overrided by using binary search
        # mainly used in find_begin_leaf_of_subtree
        # before_key < key <= curr_after_key
        entity2key = ops.entity2key
        key_le = ops.key_le
        for pos, e in ops.iter_innode_position_entity_pairs_of_nonleaf(self):
            k = entity2key(e)
            if key_le(key, k):
                # key <= k
                break
        else:
            pos = ops.get_innode_entity_end(self)
        return pos

    @abstractmethod
    def find_innode_end_of_nonleaf(ops, self, key):
        # to be overrided by using binary search
        # mainly used in find_end_leaf_of_subtree
        # before_key <= key < curr_after_key
        entity2key = ops.entity2key
        key_lt = ops.key_lt
        for pos, e in ops.iter_innode_position_entity_pairs_of_nonleaf(self):
            k = entity2key(e)
            if key_lt(key, k):
                # key < k
                break
        else:
            pos = ops.get_innode_entity_end(self)
        return pos



    def find_begin_leaf_of_subtree(ops, self, key):
        # -> leaf
        return ops.find_begin_or_end_leaf_of_subtree(self, key, False)
    def find_end_leaf_of_subtree(ops, self, key):
        # -> leaf
        return ops.find_begin_or_end_leaf_of_subtree(self, key, True)
    def find_begin_or_end_leaf_of_subtree(ops, self, key, end:bool):
        # -> leaf
        leaf, depth = ops.find_begin_or_end_leaf_ex_of_subtree(self, 0, key, end)
        return leaf



    def find_begin_leaf_ex_of_subtree(ops, self, depth, key):
        # -> (leaf, depth)
        return ops.find_begin_or_end_leaf_ex_of_subtree(self, depth, key, False)
    def find_end_leaf_ex_of_subtree(ops, self, depth, key):
        # -> (leaf, depth)
        return ops.find_begin_or_end_leaf_ex_of_subtree(self, depth, key, True)
    def find_begin_or_end_leaf_ex_of_subtree(ops, self, depth, key, end:bool):
        # -> (leaf, depth)
        # since nonleaf.num_children > 0
        assert verify_depth(depth)

        get_child_at = ops.get_child_at
        if not end:
            find = ops.find_innode_begin_of_nonleaf
        else:
            find = ops.find_innode_end_of_nonleaf

        node = self
        while not ops.is_leaf(node):
            pos = find(node, key)
            node = get_child_at(node, pos)
            depth += 1
        leaf = node
        return leaf, depth



    ######################
    def subtree_contains(ops, self, key):
        node = self
        while not ops.is_leaf(node):
            pos = ops.find_innode_begin_of_nonleaf(node, key)
            if pos != ops.get_innode_entity_end(node):
                k = ops.get_key_at(node, pos)
                if ops.key_eq(k, key):
                    return True
            node = ops.get_child_at(node, pos)
        return False
        ######
        node = ops.find_maybe_first_nonleaf_of_subtree(self, key)
        return ops.is_nonleaf(node)



    def find_maybe_first_nonleaf_ex_of_subtree(ops, self, depth, key):
        # return leaf if not found
        # -> triple
        return ops.find_maybe_first_or_last_nonleaf_ex_of_subtree(
                self, depth, key, False)
    def find_maybe_last_nonleaf_ex_of_subtree(ops, self, depth, key):
        # return leaf if not found
        # -> triple
        return ops.find_maybe_first_or_last_nonleaf_ex_of_subtree(
                self, depth, key, True)
    def find_maybe_first_or_last_nonleaf_ex_of_subtree(ops, self, depth, key, last:bool):
        # return leaf if not found
        # -> triple
        assert verify_depth(depth)
        if not last:
            find = ops.find_begin_leaf_ex_of_subtree
            step = ops.leaf_to_inorder_succ_nonleaf_entity_position_ex
        else:
            find = ops.find_end_leaf_ex_of_subtree
            step = ops.leaf_to_inorder_prev_nonleaf_entity_position_ex

        # bug: leaf, leaf_depth = find(self, key, depth)
        leaf, leaf_depth = find(self, depth, key)
        if 0:
            print('self', ops.rbt_helper_to_plain(new_root))
            print('key', key)
            print('depth', depth)
            print('leaf', ops.rbt_helper_to_direction_path_ex(leaf))

        del depth
        try:
            nonleaf, pos, nonleaf_depth = step(leaf, leaf_depth)
        except StopIteration:
            return leaf, None, leaf_depth

        k = ops.get_key_at(nonleaf, pos)
        if ops.key_eq(key, k):
            # key == k
            return nonleaf, pos, nonleaf_depth
        return leaf, None, leaf_depth




    def find_first_entity_of_subtree(ops, self, key
            , *, key2default=None, entity2result=None):
        # root -> key -> (entity | raise KeyError)
        return ops.find_first_or_last_entity_of_subtree(
                self, key, False
                , key2default=key2default, entity2result=entity2result)
    def find_last_entity_of_subtree(ops, self, key
            , *, key2default=None, entity2result=None):
        # root -> key -> (entity | raise KeyError)
        return ops.find_first_or_last_entity_of_subtree(
                self, key, True
                , key2default=key2default, entity2result=entity2result)
    def find_first_or_last_entity_of_subtree(ops, self, key, last:bool
            , *, key2default=None, entity2result=None):
        find = ops.find_maybe_first_or_last_nonleaf_ex_of_subtree

        node, may_pos, depth = find(self, 0, key, last)
        if ops.is_leaf(node):
            if key2default is None:
                raise KeyError(key)
            return key2default(key)

        pos = may_pos
        entity = ops.get_entity_at(node, pos)
        if entity2result is None:
            return entity
        else:
            return entity2result(entity)



if __name__ == '__main__':
    XXX = IKeyOrderedUnbalancedMultiWayTreeNodeOps

    from seed.helper.print_methods import print_methods
    print_methods(XXX)


