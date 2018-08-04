
'''
why ordered set?
    tree structure allows incremental modify.
    like leftward_list, we can hold all the middle sets at same time
        using only O(N log N) space

TODO:
    implement .__or__ not using ._from_iterable
        i.e. avoid create new tree from empty tree;
             create new tree from old tree + insert
    implement .update_add by replace instead of discard+insert
'''

__all__ = '''
    OrderedSet
    FrozenOrderedSet
'''.split()


from collections.abc import Set, MutableSet, Hashable
from seed.types.RedBlackTree.RedBlackTreeNodeABC import \
     RBT_Node_TupleBothPlainParented_ABC,\
     RBT_Node_Bool_Constants_ABC
from seed.types.RedBlackTree.OrderedMutableRedBlackTreeNodeABC import \
     OrderedMutableRedBlackTreeNodeABC
from seed.helper.repr_input import repr_helper


class _Node(
    RBT_Node_Bool_Constants_ABC,
    RBT_Node_TupleBothPlainParented_ABC,
    OrderedMutableRedBlackTreeNodeABC):
    PLAIN_LEAF = ()
    ROOT_PARENT_INFO = None


class _OrderedSet(Set):
    from seed.cases.ECHO import PLAIN_NODE_AND_SIZE
    __RBT_Node__ = _Node
##    __constructor_cases = frozenset({})
    @classmethod
    def _check_plain_node(cls, plain):
        assert type(plain) is tuple
        assert len(plain) in (0, 4)

    def copy(self):
        return cls(self)
    def __init__(self, iterable = (), *, constructor_case = None):
        Node = type(self).__RBT_Node__
        if constructor_case is None:
            # iterable
            if isinstance(iterable, __class__):
                other = iterable
                if type(other).__RBT_Node__ is Node:
                    # copy
                    states = other.get_states()
                    self.__set_states(states)
                    return
            plain = Node.PLAIN_LEAF
            size = 0
        elif constructor_case == __class__.PLAIN_NODE_AND_SIZE:
            # plain_node
            plain, size = iterable
            self._check_plain_node(plain)
            assert size >= 0
            iterable = ()
        else:
            raise ValueError('unknown constructor_case: {}'
                             .format(constructor_case))

        root = Node.from_root_plain_node(plain)
        root, size = self.__update(root, size, iterable)
        states = root.plain, size
        self.__set_states(states)
    @classmethod
    def from_iterable(cls, iterable):
        return cls(iterable)
    @classmethod
    def from_states(cls, states):
        plain_node, size = states
        return cls((plain_node, size),
                   constructor_case = __class__.PLAIN_NODE_AND_SIZE)
        
    def __set_states(self, states):
        # see get_states
        Node = type(self).__RBT_Node__
        plain, size = states
        root = Node.from_root_plain_node(plain)
        self.__root, self.__size = root, size
    def get_states(self):
        # return hashable states
        return self.__root.plain, self.__size

    @staticmethod
    def __update(root, size, iterable):
        for e in iterable:
            if not root.subtree_contains(root.entity2key(e)):
                root = root.insert_entity_as_last(e) # NOTE: "root ="
                size += 1
        return root, size

    def get_entity(self, key):
        root = self.__root
        return root.subtree_get_last_entity(key)
    
        
    def __contains__(self, key): # entity?? why not key??
        root = self.__root
        return root.subtree_contains(key)

    @staticmethod
    def __iter_nonleaf_nodes2iter_entities(it):
        return (nonleaf.entity for nonleaf in it)
    def __iter__(self):
        it = self.__root.get_first_leaf().leaf_inorder_iter_nonleaf_nodes()
        return self.__iter_nonleaf_nodes2iter_entities(it)
    def __reversed__(self):
        it = self.__root.get_last_leaf().leaf_inorder_iter_reversed_nonleaf_nodes()
        return self.__iter_nonleaf_nodes2iter_entities(it)
    def __len__(self):
        return self.__size
    def __repr__(self):
        return repr_helper(self,
                           self.get_states(),
                           constructor_case = __class__.PLAIN_NODE_AND_SIZE)
    def __str__(self):
        return repr_helper(self, list(self))


class FrozenOrderedSet(_OrderedSet, Hashable):
    def __init__(self, iterable = (), *, constructor_case = None):
        self.__root = None
        self.__size = None
        _OrderedSet.__init__(self, iterable, constructor_case = constructor_case)
        
    @property
    def _OrderedSet__root(self):
        return self.__root
    @_OrderedSet__root.setter
    def _OrderedSet__root(self, root):
        if self.__root is not None:
            raise AttributeError('not writable')
        # initial
        self.__root = root
    @property
    def _OrderedSet__size(self):
        return self.__size
    @_OrderedSet__size.setter
    def _OrderedSet__size(self, size):
        if self.__size is not None:
            raise AttributeError('not writable')
        # initial
        self.__size = size
    
    def __hash__(self):
        return self._hash()




class OrderedSet(_OrderedSet, MutableSet):
    def set_states(self, states):
        # see get_states
        plain, size = states
        return self._OrderedSet__set_states(states)

    def __force_add(self, e):
        root = self._OrderedSet__root
        root = root.insert_entity_as_last(e) # NOTE: "root ="
        self._OrderedSet__root = root
        self._OrderedSet__size += 1
    def update_add(self, e):
        root = self._OrderedSet__root
        key = root.entity2key(e)
        self.discard(key)
        self.__force_add(e)
        
    def add(self, e):
        root = self._OrderedSet__root
        key = root.entity2key(e)
        if key in self:
            return
        self.__force_add(e)
    def discard(self, key): # entity?? why not key??
        if key not in self:
            return
        root = self._OrderedSet__root
        root = root.subtree_remove_last_entity(key) # NOTE: "root ="
        self._OrderedSet__root = root
        self._OrderedSet__size -= 1




if __name__ == '__main__':
    s = OrderedSet(range(100))
    assert list(s) == list(range(100))

    assert 99 in s
    assert 100 not in s
    s.discard(100)
    s.remove(99)
    assert len(s) == 99
    assert list(s) == list(range(99))













        
        
