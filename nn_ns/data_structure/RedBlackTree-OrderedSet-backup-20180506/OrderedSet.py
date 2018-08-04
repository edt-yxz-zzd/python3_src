

__all__ = '''
    OrderedSet
    '''.split()

from .Ordered_RBT_Node_TupleBothPlainParented import \
    Ordered_RBT_Node_TupleBothPlainParented as Node__global
from .RedBlackTree.OrderedMutableRedBlackTreeNodeABC import \
    OrderedMutableRedBlackTreeNodeABC

from collections.abc import MutableSet
import operator
from seed.iters.len_of_iterator import len_of_iterator
from seed.iters.neighbor_unique import neighbor_unique
from seed.iters.intersect_two_sorted_iterables import \
                intersect_two_sorted_iterables
from seed.iters.merge_two_sorted_iterables import merge_two_sorted_iterables

from seed.iters.are_two_sorted_iterables_disjoint import \
                are_two_sorted_iterables_disjoint
from seed.iters.is_subset_of_sorted_iterable import \
                is_subset_of_sorted_iterable
from seed.iters.difference_of_two_sorted_iterables import \
                difference_of_two_sorted_iterables
from seed.iters.symmetric_difference_of_two_sorted_iterables import \
                symmetric_difference_of_two_sorted_iterables
from seed.helper.repr_input import repr_helper

if 0 and useful:
    # constructor
        copy
        from_sorted_entities

        make_leaf_root
        insert_entity_as_first
        insert_entity_as_last
        subtree_remove_first_entity
        subtree_remove_last_entity

        remove_entity_at_nonleaf
        remove_leaf_and_its_parent

    # find
        subtree_contains
        subtree_find_begin_leaf
        subtree_find_end_leaf
        subtree_find_maybe_first_nonleaf
        subtree_find_maybe_last_nonleaf
        subtree_get_first_entity
        subtree_get_last_entity

        find_innode_begin
        find_innode_end
        find_innode_range

    # iter
        # not:
        #   iter_entities
        #   iter_reversed_entities
        get_first_leaf
        get_last_leaf

        leaf_inorder_iter_nodes
        leaf_inorder_iter_nonleaf_nodes
        leaf_inorder_iter_reversed_nodes
        leaf_inorder_iter_reversed_nonleaf_nodes

        leaf_inorder_prev_nonleaf
        leaf_inorder_succ_nonleaf

        nonleaf_inorder_prev_leaf
        nonleaf_inorder_succ_leaf


    # key
        key_eq
        key_lt
        entity2key




class OrderedSet:
    ''' set base on comparason (red-black-tree)


example:
    >>> This = OrderedSet
    >>> This()
    OrderedSet([])
    >>> This([])
    OrderedSet([])
    >>> issubclass(This, MutableSet)
    True

    >>> s = This(range(3))
    >>> s
    OrderedSet([0, 1, 2])
    >>> len(s)
    3
    >>> 1 in s
    True
    >>> 3 in s
    False

    >>> s.add(6)
    >>> s
    OrderedSet([0, 1, 2, 6])
    >>> s.add(6)
    >>> s
    OrderedSet([0, 1, 2, 6])
    >>> s.pop()
    6
    >>> s.popleft()
    0
    >>> [*iter(s)]
    [1, 2]
    >>> [*reversed(s)]
    [2, 1]
    >>> len(s)
    2


    >>> t = OrderedSet([5,2,4,4])
    >>> t
    OrderedSet([2, 4, 5])
    >>> t.swap(s)
    >>> s
    OrderedSet([2, 4, 5])
    >>> t
    OrderedSet([1, 2])

    >>> s | t
    OrderedSet([1, 2, 4, 5])
    >>> s & t
    OrderedSet([2])
    >>> s - t
    OrderedSet([4, 5])
    >>> s ^ t
    OrderedSet([1, 4, 5])

    >>> s <= t
    False
    >>> t <= s
    False

    >>> t == t
    True
    >>> t <= t
    True
    >>> t < t
    False

    >>> (s | t) >= t >= (s & t)
    True
    >>> (s ^ t) >= (s - t)
    True
    >>> (s ^ t).isdisjoint(s & t)
    True
    >>> s.isdisjoint(t)
    False

    >>> s
    OrderedSet([2, 4, 5])
    >>> t
    OrderedSet([1, 2])
    >>> t.discard(3)
    >>> len(t)
    2
    >>> t.remove(3) # doctest: +IGNORE_EXCEPTION_DETAIL 
    Traceback (most recent call last):
        ...
    KeyError
    >>> t.remove(2)
    >>> t
    OrderedSet([1])
    >>> t.discard(1)
    >>> t
    OrderedSet([])
    >>> t <= s
    True
    >>> not t
    True

    >>> t &= s
    >>> t
    OrderedSet([])
    >>> t |= s
    >>> t
    OrderedSet([2, 4, 5])

    >>> t.pop()
    5
    >>> t
    OrderedSet([2, 4])
    >>> t.clear()
    >>> t
    OrderedSet([])
    >>> s
    OrderedSet([2, 4, 5])


    >>> t ^= s
    >>> t
    OrderedSet([2, 4, 5])
    >>> t |= s
    >>> t
    OrderedSet([2, 4, 5])
    >>> t &= s
    >>> t
    OrderedSet([2, 4, 5])

    >>> t ^= s
    >>> t
    OrderedSet([])

    >>> t ^= s
    >>> t
    OrderedSet([2, 4, 5])
    >>> len(t)
    3
    >>> t -= s
    >>> t
    OrderedSet([])
    >>> t -= s
    >>> t
    OrderedSet([])
    >>> bool(t)
    False


    >>> class RBT_Node__tmp(Node__global):
    ...     @classmethod
    ...     def key_lt(cls, lhs, rhs):
    ...         return rhs < lhs # reverse
    ...     @classmethod
    ...     def key_eq(cls, lhs, rhs):
    ...         return rhs == lhs
    ...     @classmethod
    ...     def entity2key(cls, entity):
    ...         return len(entity)

    >>> That = lambda iterable: OrderedSet(iterable, RBT_Node=RBT_Node__tmp)
    >>> s = That([[], {}, (), [1], [2], (1,2)])
    >>> s # doctest: +ELLIPSIS
    OrderedSet([(1, 2), [1], []], RBT_Node = ...)
    >>> s.get_entity(2)
    (1, 2)
    >>> s.may_get_entity(2)
    ((1, 2),)
    >>> s.may_get_entity(3)
    ()

    >>> s.remove_key(0)
    >>> s # doctest: +ELLIPSIS
    OrderedSet([(1, 2), [1]], RBT_Node = ...)
    >>> s.remove([..., None])
    >>> s # doctest: +ELLIPSIS
    OrderedSet([[1]], RBT_Node = ...)
    >>> s.pop()
    [1]


methods:
    #private:
        #private properties:
            Node
            __size
            __tree
        #private methods:
            __get_properties
            __iter
            __set_properties
            __count_size


    #query
        get_entity
        may_get_entity
    #key ops:
        entity2key
        key_eq
        key_lt
        key_le
    #container ops:
        __repr__
        __len__
        __contains__
        __iter__
        __reversed__

        #container key ops:
            contain_key
            discard_key
            pop_key
            remove_key

        # container constructor
            copy
            from_sorted_entities
            make_empty_set
        # constructor modify
            assign
            swap

            add
            update
            clear
            discard
            pop
            popleft
            remove


    #set ops:
        # subset
            isdisjoint
            issubset
            issuperset

            __eq__
            __ne__
            __ge__
            __gt__
            __le__
            __lt__

        # set constructor
            __and__
            __or__
            __sub__
            __xor__

        # modify
            __iand__
            __ior__
            __isub__
            __ixor__

'''
    __slots__ = '_OrderedSet__tree _OrderedSet__size'.split()

    @property
    def Node(self):
        return type(self.__tree)

    def __repr__(self):
        entities = list(self)
        if self.Node is Node__global:
            return repr_helper(self, entities)
        else:
            return repr_helper(self, entities, RBT_Node=self.Node)

    def swap(self, other):
        if type(self) is not type(other): raise TypeError
        a = self.__get_properties()
        b = other.__get_properties()
        self.__set_properties(b)
        other.__set_properties(a)

    def __get_properties(self):
        return self.__tree, self.__size
    def __set_properties(self, properties):
        if not len(properties) == 2: raise TypeError
        self.__tree, self.__size = properties
    @classmethod
    def make_empty_set(cls, RBT_Node):
        return cls(RBT_Node=RBT_Node)
    @classmethod
    def from_sorted_entities(cls, RBT_Node, entities
                            , reverse=False, strict=False):
        return cls(entities, RBT_Node=RBT_Node
            , is_sorted=True, reverse=reverse, strict=strict)


    def __init__(self, iterable=None
            , *, RBT_Node=None, is_sorted=False, reverse=False, strict=False):
        '''

iterable :: [Entity]
RBT_Node <: OrderedMutableRedBlackTreeNodeABC
is_sorted :: bool
    whether iterable is sorted?
reverse :: bool
    whether iterable sorted in reverse order?
strict :: bool
    whether iterable is strict sorted?
'''

        if RBT_Node is None:
            RBT_Node = Node__global
        else:
            assert issubclass(RBT_Node, OrderedMutableRedBlackTreeNodeABC)

        #self.Node = RBT_Node


        if iterable is not None and is_sorted:
            # iterable is_sorted
            entities = iterable
            if not strict:
                key = RBT_Node.entity2key
                eq = RBT_Node.key_eq
                entities = neighbor_unique(entities, key=key, __eq__=eq)

            strict = True
            tree = RBT_Node.from_sorted_entities(
                        entities, reverse=reverse, strict=strict)
            self.__tree = tree
            self.__size = __class__.__count_size(tree)
        else:
            self.__tree = RBT_Node.make_leaf_root()
            self.__size = 0
            if iterable is not None:
                self.update(iterable)


    @classmethod
    def make_empty_set(cls, RBT_Node):
        return cls(RBT_Node=RBT_Node)
    def assign(self, other):
        tmp = other.copy()
        self.swap(tmp)
    def copy(self):
        cls = type(self)
        new = cls.make_empty_set(self.Node)
        new.__tree = self.__tree.copy()
        new.__size = self.__size
        return new

    @property
    def entity2key(self):
        return self.Node.entity2key
    @property
    def key_lt(self):
        return self.Node.key_lt
    @property
    def key_le(self):
        return self.Node.key_le
    @property
    def key_eq(self):
        return self.Node.key_eq

    def __len__(self):
        return self.__size
    def contain_key(self, key):
        return self.__tree.subtree_contains(key)
        return self.Node.subtree_contains(self.__tree, key)


    def get_entity(self, key, *, fdefault=None, fresult=None):
        if self.contain_key(key):
            entity = self.__tree.subtree_get_first_entity(key)
            if fresult is None:
                return entity
            return fresult(entity)
        if fdefault is None:
            raise KeyError
        return fdefault()

    def may_get_entity(self, key):
        # -> () | (entity,)
        if self.contain_key(key):
            entity = self.__tree.subtree_get_first_entity(key)
            return (entity,)
        return ()

    def pop_key(self, key):
        entity = self.get_entity(key)
        self.remove_key(key)
        return entity
    def discard_key(self, key):
        if self.contain_key(key):
            self.remove_key(key)
    def remove_key(self, key):
        # may raise KeyError
        self.__tree = self.__tree.subtree_remove_first_entity(key)
        self.__size -= 1


    def __contains__(self, x):
        key = self.Node.entity2key(x)
        return self.contain_key(key)


    def update(self, iterable):
        for x in iterable:
            self.add(x)
    def remove(self, x):
        key = self.Node.entity2key(x)
        self.remove_key(key)
    def discard(self, x):
        key = self.Node.entity2key(x)
        self.discard_key(key)

    def add(self, x):
        if x in self:
            return
        #self.discard(x)
        self.__tree = self.__tree.insert_entity_as_last(x)
        self.__size += 1

    def popleft(self):
        if not self:
            raise KeyError('pop empty set')
        leaf = self.__tree.get_first_leaf()
        assert not leaf.is_root()
        entity = leaf.parent.entity
        self.__tree = leaf.remove_leaf_and_its_parent()
        self.__size -= 1
        return entity


    def pop(self):
        if not self:
            raise KeyError('pop empty set')
        leaf = self.__tree.get_last_leaf()
        assert not leaf.is_root()
        entity = leaf.parent.entity
        self.__tree = leaf.remove_leaf_and_its_parent()
        self.__size -= 1
        return entity

        try:
            nonleaf = self.__tree.leaf_inorder_prev_nonleaf(leaf)
        except StopIteration:
            raise KeyError('pop empty set')
        entity = nonleaf.entity


    def clear(self):
        if self:
            self.__tree = self.Node.make_leaf_root()
            self.__size = 0


    #############
    @staticmethod
    def __iter(tree):
        it = tree.get_first_leaf().leaf_inorder_iter_nonleaf_nodes()
        for nonleaf in it:
            yield nonleaf.entity
    @staticmethod
    def __count_size(tree):
        # O(n)
        return len_of_iterator(__class__.__iter(tree))

    def __iter__(self):
        return self.__iter(self.__tree)
    def __reversed__(self):
        it = self.__tree.get_last_leaf().leaf_inorder_iter_reversed_nonleaf_nodes()
        for nonleaf in it:
            yield nonleaf.entity
    def issuperset(self, other):
        return self >= other

    def issubset(self, other):
        if not isinstance(other, __class__): raise TypeError
        if not self.Node is other.Node: raise TypeError
        if not len(self) <= len(other):
            return False
        Node = self.Node
        lhs = map(Node.entity2key, self)
        rhs = map(Node.entity2key, other)
        return is_subset_of_sorted_iterable(lhs, rhs, __lt__ = Node.key_lt)
    def isdisjoint(self, other):
        if not isinstance(other, __class__): raise TypeError
        if not self.Node is other.Node: raise TypeError

        Node = self.Node
        lhs = map(Node.entity2key, self)
        rhs = map(Node.entity2key, other)
        return are_two_sorted_iterables_disjoint(lhs, rhs, __lt__ = Node.key_lt)


    def __le__(self, other):
        return self.issubset(other)
    def __lt__(self, other):
        return len(self) < len(other) and self.issubset(other)
    def __eq__(self, other):
        if not isinstance(other, __class__): raise TypeError
        if not self.Node is other.Node: raise TypeError

        if len(self) != len(other): return False
        Node = self.Node
        lhs = map(Node.entity2key, self)
        rhs = map(Node.entity2key, other)
        return all(map(Node.key_eq, lhs, rhs))
    def __ne__(self, other):
        return not (self == other)
    def __gt__(self, other):
        if not isinstance(other, __class__): raise TypeError
        if not self.Node is other.Node: raise TypeError
        return other < self
    def __ge__(self, other):
        if not isinstance(other, __class__): raise TypeError
        if not self.Node is other.Node: raise TypeError
        return other <= self



    ##################
    def __iand__(self, other):
        # intersection
        if not isinstance(other, __class__): raise TypeError
        if not self.Node is other.Node: raise TypeError
        Node = self.Node

        if not self:
            return self
        if not other:
            self.clear()
            return self


        N = len(self)
        M = len(other)
        assert N > 0 and M > 0

        # M*log2_N v.s. N*log2(M) v.s. N+M
        log2_M = M.bit_length()
        log2_N = N.bit_length()
        log2_MN = log2_M + log2_N

        M_N = M+N
        M_log2_MN = M*log2_MN
        N_log2_MN = N*log2_MN
        m = min(M_N, M_log2_MN, N_log2_MN)
        if N_log2_MN == m:
            for x in self:
                if x not in other:
                    self.remove(x)
        else:
            self.swap(self & other)
        return self

    def __and__(self, other):
        # intersection
        if not isinstance(other, __class__): raise TypeError
        if not self.Node is other.Node: raise TypeError
        Node = self.Node

        cls = type(self)
        if not self or not other:
            return cls.make_empty_set(Node)

        if len(self) > len(other):
            self, other = other, self

        N = len(self)
        M = len(other)
        assert 0 < N <= M
        # N*log2(M) v.s. N+M
        log2_M = M.bit_length()
        if N * log2_M < N + M:
            it = (x for x in self if x in other)
        else:
            key = Node.entity2key
            it = intersect_two_sorted_iterables(
                    self, other
                    , left_key=key, right_key=key, __lt__=Node.key_lt)
        return cls.from_sorted_entities(Node, it)




    ###############
    def __ior__(self, other):
        # union
        if not isinstance(other, __class__): raise TypeError
        if not self.Node is other.Node: raise TypeError
        Node = self.Node

        if not other:
            return self
        if not self:
            self.assign(other)
            return self

        N = len(self)
        M = len(other)
        assert N > 0 and M > 0
        # M*log2(M+N) v.s. N*log2(M+N) v.s. v.s. N+M
        M_N = M+N
        log2_M_N = M_N.bit_length()
        M_log2_M_N = M * log2_M_N
        N_log2_M_N = N * log2_M_N

        m = min(M_log2_M_N, N_log2_M_N, M_N)
        if M_log2_M_N == m:
            self.update(other)
        else:
            self.swap(self | other)
        return self

    def __or__(self, other):
        # union
        if not isinstance(other, __class__): raise TypeError
        if not self.Node is other.Node: raise TypeError
        Node = self.Node

        if not self:
            return other.copy()
        if not other:
            return self.copy()

        if len(self) > len(other):
            self, other = other, self

        N = len(self)
        M = len(other)
        assert 0 < N <= M
        # N*log2(M+N) v.s. N+M
        M_N = M+N
        log2_M_N = M_N.bit_length()
        if N * log2_M_N < N + M:
            output = other.copy()
            output.update(self)
        else:
            key = Node.entity2key
            it = merge_two_sorted_iterables(
                    self, other
                    , left_key=key, right_key=key, before=Node.key_le)
            #bug: output = Node.from_sorted_entities(it)
            cls = type(self)
            output = cls.from_sorted_entities(Node, it)
        return output



    ###############
    def __isub__(self, other):
        # difference
        if not isinstance(other, __class__): raise TypeError
        if not self.Node is other.Node: raise TypeError
        Node = self.Node

        if not self:
            return self
        if not other:
            return self

        N = len(self)
        M = len(other)
        # may N > M
        assert N > 0 and M > 0

        # N*log2(M*N) v.s. M*log2(N*N) v.s. N+M
        # N decrease
        M_N = M+N
        log2_M = M.bit_length()
        log2_N = N.bit_length()
        log2_MN = log2_M + log2_N
        log2_NN = log2_N + log2_N
        N_log2_MN = N*log2_MN
        M_log2_NN = M*log2_NN

        m = min(N_log2_MN, M_log2_NN, M_N)
        if M_log2_NN == m:
            for y in other:
                self.discard(y)
        else:
            self.swap(self - other)
        return self


    def __sub__(self, other):
        # difference
        if not isinstance(other, __class__): raise TypeError
        if not self.Node is other.Node: raise TypeError
        Node = self.Node

        if not self:
            return cls.make_empty_set(RBT_Node=Node)
        if not other:
            return self.copy()

        N = len(self)
        M = len(other)
        # may N > M
        assert N > 0 and M > 0

        # N*log2(M) v.s. M*log2(N) v.s. N+M
        # N decrease
        M_N = M+N
        log2_M = M.bit_length()
        log2_N = N.bit_length()
        N_log2_M = N*log2_M
        M_log2_N = M*log2_N

        m = min(N_log2_M, M_log2_N, M_N)
        if M_log2_N == m:
            output = self.copy()
            for y in other:
                output.discard(y)
            return output
        elif N_log2_M == m:
            it = (x for x in self if x not in other)
        else:
            key = Node.entity2key
            it = difference_of_two_sorted_iterables(
                    self, other
                    , left_key=key, right_key=key, __lt__=Node.key_lt
                    )
        cls = type(self)
        output = cls.from_sorted_entities(it)
        return output


    #################
    def __ixor__(self, other):
        # symmetric_difference
        if not isinstance(other, __class__): raise TypeError
        if not self.Node is other.Node: raise TypeError

        if not other:
            return self
        if not self:
            self.assign(other)
            return self

        self.swap(self ^ other)
        return self

    def __xor__(self, other):
        # symmetric_difference
        if not isinstance(other, __class__): raise TypeError
        if not self.Node is other.Node: raise TypeError
        Node = self.Node

        if len(self) > len(other):
            self, other = other, self
        N = len(self)
        M = len(other)
        assert 0 < N <= M

        if not self:
            return other.copy()
        common = self & other
        union = self | other
        if not common:
            # assert self.isdisjoint(other)
            return union
        return union - common

        diff = other - self
        if len(diff) == M - N:
            # assert self <= other
            return diff



        # N*log2(M) v.s. N+M
        M_N = M+N
        log2_N = N.bit_length()
        N_log2_M = N*log2_M

        if N_log2_M <= M_N:
            it1 = (x for x in self if x not in other)
            it2 = (x for x in self if x not in other)
        else:
            key = Node.entity2key
            it = symmetric_difference_of_two_sorted_iterables(
                    self, other
                    , left_key=key, right_key=key, __lt__=Node.key_lt
                    )
        cls = type(self)
        output = cls.from_sorted_entities(it)
        return output

MutableSet.register(OrderedSet)



if __name__ == "__main__":
    print('\n'.join(dir(OrderedSet)))
    print()

    import doctest
    doctest.testmod()

