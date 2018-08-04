


__all__ = '''
    KeyOrderedRedBlackTreeNodeOps__sized_immutable
    '''.split()



from .abc import override
from seed.tiny import echo
from ..KeyOrderedTreeNodeOps.TotalOrderingOps import \
    TotalOrderingOps, python_total_key_ops

from ..KeyOrderedTreeNodeOps.IKeyOrderedTreeNodeOps__num_entities_of_subtree import \
    IKeyOrderedTreeNodeOps__num_entities_of_subtree
from ..KeyOrderedTreeNodeOps.ITotalOrderingOps import ITotalOrderingOps
from .RedBlackTreeNodeOps__sized_immutable import \
    RedBlackTreeNodeOps__sized_immutable
from ..KeyOrderedTreeNodeOps.IKeyOrderedBinaryTreeNodeOps import\
    IKeyOrderedBinaryTreeNodeOps
from ..KeyOrderedTreeNodeOps.IKeyOrderedRedBlackTreeNodeOps__imodify import \
    IKeyOrderedRedBlackTreeNodeOps__imodify


class KeyOrderedRedBlackTreeNodeOps__sized_immutable(
        RedBlackTreeNodeOps__sized_immutable
        , IKeyOrderedRedBlackTreeNodeOps__imodify
        , IKeyOrderedTreeNodeOps__num_entities_of_subtree
        , IKeyOrderedBinaryTreeNodeOps
        ):
    '''
see:
    KeyOrderedTreeNodeOps.ITotalOrderingOps
    KeyOrderedTreeNodeOps.TotalOrderingOps
    KeyOrderedTreeNodeOps.TotalOrderingOps.python_total_key_ops

input:
    key_ops :: None | ITotalOrderingOps = python_total_key_ops
    entity2key :: None | (entity -> key) = echo

override:
    _get_key_ops_
    entity2key




example:
    >>> This = KeyOrderedRedBlackTreeNodeOps__sized_immutable
    >>> ops = simple_KRBT_SI
    >>> root = ops.rbt_from_entities(3, [1, 2, 3])
    >>> ops.rbt_helper_to_plain(root)
    ('BLACK', 2, ('BLACK', 1, (), ()), ('BLACK', 3, (), ()))
    >>> first_leaf, first_depth = ops.get_first_or_last_leaf_ex(root, 0, False)
    >>> ops.rbt_helper_to_direction_path(first_leaf)
    ['LEFT', 'LEFT']
    >>> [*ls] = ops.leaf_to_iter_entities_of_subtree(first_leaf, first_depth, reverse=False)
    >>> ls
    [1, 2, 3]
    >>> [*ls] = ops.leaf_to_iter_entities_of_subtree(first_leaf, first_depth, reverse=True)
    >>> ls
    []

    >>> last_leaf, last_depth = ops.get_first_or_last_leaf_ex(root, 0, True)
    >>> ops.rbt_helper_to_direction_path(last_leaf)
    ['RIGHT', 'RIGHT']
    >>> [*ls] = ops.leaf_to_iter_entities_of_subtree(last_leaf, last_depth, reverse=False)
    >>> ls
    []
    >>> [*ls] = ops.leaf_to_iter_entities_of_subtree(last_leaf, last_depth, reverse=True)
    >>> ls
    [3, 2, 1]

    >>> [*ls] = ops.iter_entities_of_subtree(root, reverse=False)
    >>> ls
    [1, 2, 3]
    >>> [*ls] = ops.iter_entities_of_subtree(root, reverse=True)
    >>> ls
    [3, 2, 1]



    >>> root = ops.rbt_from_entities(3, [0, 1, 2])
    >>> ops.rbt_helper_to_plain(root)
    ('BLACK', 1, ('BLACK', 0, (), ()), ('BLACK', 2, (), ()))
    >>> [*ls] = ops.iter_entities_of_subtree(root, reverse=False)
    >>> ls
    [0, 1, 2]


    >>> root = ops.rbt_from_entities(4, '0123')
    >>> ops.rbt_helper_to_plain(root)
    ('BLACK', '1', ('BLACK', '0', (), ()), ('BLACK', '2', (), ('RED', '3', (), ())))
    >>> [*ls] = ops.iter_entities_of_subtree(root, reverse=False)
    >>> ls
    ['0', '1', '2', '3']
    >>> [*ls] = ops.iter_entities_of_subtree(root, reverse=True)
    >>> ls
    ['3', '2', '1', '0']

'''
    __slots__ = '''
        _key_ops
        _entity2key
        '''.split()


    # user-defined
    @property
    @override
    def entity2key(ops):
        return ops._entity2key
    @override
    def _get_key_ops_(ops):
        return ops._key_ops

    def __init__(self, key_ops, entity2key):
        #assert entity2key is None or callable(entity2key)
        #assert isinstance(key_ops, ITotalOrderingOps) or is_pair(key_ops)

        if key_ops is None:
            key_ops = python_total_key_ops
        elif not isinstance(key_ops, ITotalOrderingOps): raise TypeError

        if entity2key is None:
            entity2key = echo
        elif not callable(entity2key): raise TypeError

        self._key_ops = key_ops
        self._entity2key = entity2key
    def get_args_for_eq_hash(ops):
        return (ops._key_ops, ops._entity2key)

simple_KRBT_SI = KeyOrderedRedBlackTreeNodeOps__sized_immutable(
        None, None)

if __name__ == '__main__':
    XXX = KeyOrderedRedBlackTreeNodeOps__sized_immutable

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)

    from seed.helper.find_bases_without_slots import print_bases_without_slots
    print_bases_without_slots(XXX)

if __name__ == "__main__":
    import doctest
    doctest.testmod()


