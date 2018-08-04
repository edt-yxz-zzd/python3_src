

__all__ = '''
    KeyOrderedSet
    '''.split()

from ..KeyOrderedTreeNodeOps.TotalOrderingOps import \
    TotalOrderingOps, python_total_key_ops

from ..RedBlackTreeNodeOps__concrete.KeyOrderedRedBlackTreeNodeOps__sized_immutable import \
    KeyOrderedRedBlackTreeNodeOps__sized_immutable
from ..KeyOrderedTreeNodeOps.IKeyOrderedRedBlackTreeNodeOps__imodify import \
    IKeyOrderedRedBlackTreeNodeOps__imodify


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
from seed.tiny import echo


if 1 and __debug__:
    from sys import stderr
    def eprint(*args):
        print(*args, file=stderr)




Node__global = simple_KRBT_SI = KeyOrderedRedBlackTreeNodeOps__sized_immutable(
        None, None)

neg_inf = float('-inf')

class KeyOrderedSet:
    ''' set base on comparason (red-black-tree)

## !!!!!!! if the key is mutable, this set will fail!!!!!!!!!


see:
    KeyOrderedTreeNodeOps.ITotalOrderingOps
    KeyOrderedTreeNodeOps.TotalOrderingOps
    KeyOrderedTreeNodeOps.TotalOrderingOps.python_total_key_ops
    IKeyOrderedRedBlackTreeNodeOps__imodify
    KeyOrderedRedBlackTreeNodeOps__sized_immutable

input:
    RBT_Node :: None | IKeyOrderedRedBlackTreeNodeOps__imodify
    #key_ops :: None | ITotalOrderingOps = python_total_key_ops
    #entity2key :: None | (entity -> key) = echo




example:
    >>> This = KeyOrderedSet
    >>> This()
    KeyOrderedSet([])
    >>> This([])
    KeyOrderedSet([])
    >>> issubclass(This, MutableSet)
    True

    >>> This(range(3), is_sorted=True)
    KeyOrderedSet([0, 1, 2])

    >>> s = This(range(3))
    >>> s
    KeyOrderedSet([0, 1, 2])
    >>> len(s)
    3
    >>> 1 in s
    True
    >>> 3 in s
    False

    >>> s.add(6)
    >>> s
    KeyOrderedSet([0, 1, 2, 6])
    >>> s.add(6)
    >>> s
    KeyOrderedSet([0, 1, 2, 6])
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


    >>> t = KeyOrderedSet([5,2,4,4])
    >>> t
    KeyOrderedSet([2, 4, 5])
    >>> t.swap(s)
    >>> s
    KeyOrderedSet([2, 4, 5])
    >>> t
    KeyOrderedSet([1, 2])

    >>> s | t
    KeyOrderedSet([1, 2, 4, 5])
    >>> s & t
    KeyOrderedSet([2])
    >>> s - t
    KeyOrderedSet([4, 5])
    >>> s ^ t
    KeyOrderedSet([1, 4, 5])

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
    KeyOrderedSet([2, 4, 5])
    >>> t
    KeyOrderedSet([1, 2])
    >>> t.discard(3)
    >>> len(t)
    2
    >>> t.remove(3) # doctest: +IGNORE_EXCEPTION_DETAIL 
    Traceback (most recent call last):
        ...
    KeyError
    >>> t.remove(2)
    >>> t
    KeyOrderedSet([1])
    >>> t.discard(1)
    >>> t
    KeyOrderedSet([])
    >>> t <= s
    True
    >>> not t
    True

    >>> t &= s
    >>> t
    KeyOrderedSet([])
    >>> t |= s
    >>> t
    KeyOrderedSet([2, 4, 5])

    >>> t.pop()
    5
    >>> t
    KeyOrderedSet([2, 4])
    >>> t.clear()
    >>> t
    KeyOrderedSet([])
    >>> s
    KeyOrderedSet([2, 4, 5])


    >>> t ^= s
    >>> t
    KeyOrderedSet([2, 4, 5])
    >>> t |= s
    >>> t
    KeyOrderedSet([2, 4, 5])
    >>> t &= s
    >>> t
    KeyOrderedSet([2, 4, 5])

    >>> t ^= s
    >>> t
    KeyOrderedSet([])

    >>> t ^= s
    >>> t
    KeyOrderedSet([2, 4, 5])
    >>> len(t)
    3
    >>> t -= s
    >>> t
    KeyOrderedSet([])
    >>> t -= s
    >>> t
    KeyOrderedSet([])
    >>> bool(t)
    False



    # reverse order
    >>> key_ops = TotalOrderingOps(operator.__ge__, operator.__eq__)
    >>> entity2key = len
    >>> RBT_Node__tmp = KeyOrderedRedBlackTreeNodeOps__sized_immutable(key_ops, len)
    >>> That = lambda iterable, **kwargs: KeyOrderedSet(iterable, RBT_Node=RBT_Node__tmp, **kwargs)
    >>> s = That([[], {}, (), [1], [2], (1,2)])
    >>> s # doctest: +ELLIPSIS
    KeyOrderedSet([(1, 2), [2], ()], RBT_Node = ...)
    >>> s.get_entity(2)
    (1, 2)
    >>> s.may_get_entity(2)
    ((1, 2),)
    >>> s.may_get_entity(3)
    ()

    >>> s.remove_key(0)
    >>> s # doctest: +ELLIPSIS
    KeyOrderedSet([(1, 2), [2]], RBT_Node = ...)
    >>> s.remove([..., None])
    >>> s # doctest: +ELLIPSIS
    KeyOrderedSet([[2]], RBT_Node = ...)
    >>> s.pop()
    [2]


    >>> len(s)
    0
    >>> s.add_if_not_any([6])
    >>> len(s)
    1
    >>> s.add_if_not_any([""]) # has no effect
    >>> s # doctest: +ELLIPSIS
    KeyOrderedSet([[6]], RBT_Node = ...)
    >>> len(s)
    1

    >>> s.add([0]) # update
    >>> len(s)
    1
    >>> s # doctest: +ELLIPSIS
    KeyOrderedSet([[0]], RBT_Node = ...)
    >>> s.add(["", ""])
    >>> s # doctest: +ELLIPSIS
    KeyOrderedSet([['', ''], [0]], RBT_Node = ...)
    >>> len(s)
    2

    >>> s.add_key2entity_if_not_any(1, lambda _:[1])
    >>> s # doctest: +ELLIPSIS
    KeyOrderedSet([['', ''], [0]], RBT_Node = ...)
    >>> len(s)
    2
    >>> s.add_key2entity_if_not_any(0, lambda _:[])
    >>> s # doctest: +ELLIPSIS
    KeyOrderedSet([['', ''], [0], []], RBT_Node = ...)
    >>> len(s)
    3





    >>> key_ops = TotalOrderingOps(operator.__ge__, operator.__eq__)
    >>> fst2key = len
    >>> entity2key = lambda item: fst2key(item[0])
    >>> Node = KeyOrderedRedBlackTreeNodeOps__sized_immutable(key_ops, entity2key)
    >>> That2 = lambda *args, **kwargs: KeyOrderedSet(*args, RBT_Node=Node, **kwargs)
    >>> s = That2([('3535', 3), ({1, 2}, 2), ((1,), 5), ([], 4)], is_sorted=True)
    >>> s # doctest: +ELLIPSIS
    KeyOrderedSet([('3535', 3), ({1, 2}, 2), ((1,), 5), ([], 4)], RBT_Node = ...)
    >>> s.remove_key(1)
    >>> s # doctest: +ELLIPSIS
    KeyOrderedSet([('3535', 3), ({1, 2}, 2), ([], 4)], RBT_Node = ...)

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
            pop_left_or_right
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
    __slots__ = '_KeyOrderedSet__ops _KeyOrderedSet__tree _KeyOrderedSet__size'.split()


    @property
    def Node(self):
        return self.__ops
        return type(self.__tree)

    def __repr__(self):
        entities = list(self)
        if self.Node is Node__global:
            return repr_helper(self, entities)
        return repr_helper(self, entities, RBT_Node=self.Node)

    def swap(self, other):
        if type(self) is not type(other): raise TypeError
        a = self.__get_properties()
        b = other.__get_properties()
        self.__set_properties(b)
        other.__set_properties(a)

    def __get_properties(self):
        return self.__ops, self.__tree, self.__size
    def __set_properties(self, properties):
        if not len(properties) == 3: raise TypeError
        self.__ops, self.__tree, self.__size = properties

    @classmethod
    def make_empty_set(cls, RBT_Node):
        return cls(RBT_Node=RBT_Node)

    @classmethod
    def from_sorted_entities(cls, RBT_Node, entities
                            , reverse=False, strict=False):
        return cls(entities, RBT_Node=RBT_Node
            , is_sorted=True, reverse=reverse, strict=strict
            )


    def __init__(self, iterable=None
            , *, RBT_Node=None, is_sorted=False, reverse=False, strict=False
            ):
        '''

iterable :: None | Iter Entity
RBT_Node :: None | IKeyOrderedRedBlackTreeNodeOps__imodify
    see:
        KeyOrderedRedBlackTreeNodeOps__sized_immutable
        TotalOrderingOps
            python_total_key_ops

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
            assert isinstance(RBT_Node, IKeyOrderedRedBlackTreeNodeOps__imodify)



        self.__ops = RBT_Node
        if iterable is not None and is_sorted:
            # iterable is_sorted
            entities = iterable; del iterable

            if not strict:
                key = RBT_Node.entity2key
                eq = RBT_Node.key_eq
                entities = neighbor_unique(entities, key=key, __eq__=eq)

            try:
                num_entities = len(entities)
            except:
                entities = tuple(entities)
                num_entities = len(entities)

            strict = True
            tree = RBT_Node.from_sorted_entities(num_entities, entities
                        , reverse=reverse, strict=strict)


            self.__tree = tree
            self.__size = __class__.__count_size(RBT_Node, tree)
            if self.__size != num_entities:
                ops = RBT_Node
                tree
                eprint(ops)
                eprint(ops.rbt_helper_to_plain(tree))
                [*ls] = __class__.__iter(ops, tree, reverse=False)
                eprint('entities from __iter', ls)
                [*ls] = ops.iter_entities_of_subtree(tree, reverse=False)
                eprint('entities from iter_entities_of_subtree', ls)

                first_leaf, first_depth = ops.get_first_or_last_leaf_ex(tree, 0, False)
                path = ops.rbt_helper_to_direction_path(first_leaf)
                eprint(path)
                [*ls] = ops.leaf_to_iter_entities_of_subtree(first_leaf, first_depth, reverse=False)
                eprint('entities from leaf_to_iter_entities_of_subtree', ls)
                [*ls] = ops.leaf_to_iter_entities_of_subtree(first_leaf, first_depth, reverse=True)
                eprint('reversed entities from leaf_to_iter_entities_of_subtree', ls)

                eprint('size', self.__size)
                eprint('num_entities', num_entities)
            assert self.__size == num_entities
        else:
            self.__tree = RBT_Node.make_root_leaf()
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
        RBT_Node = self.Node

        new = cls.make_empty_set(RBT_Node)
        new.__tree = RBT_Node.copy_subtree_as_tree(self.__tree)
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
        return self.Node.subtree_contains(self.__tree, key)


    def get_entity(self, key, *, key2default=None, entity2result=None):
        result = self.Node.find_first_entity_of_subtree(self.__tree, key
                , key2default=key2default, entity2result=entity2result)
        return result

    def may_get_entity(self, key):
        # -> () | (entity,)
        def key2default(key): return ()
        def entity2result(entity): return (entity,)
        result = self.Node.find_first_entity_of_subtree(self.__tree, key
                , key2default=key2default, entity2result=entity2result)
        return result


    def pop_key(self, key, *, fdefault=None):
        f = self.Node.find_and_ipop_first_or_last_entity_of_subtree
        entity, root = f(self.__tree, key, True, fdefault=fdefault)
        self.__size -= 1
        self.__tree = root
        return entity
        # old version
        def pop_key(self, key):
            entity = self.get_entity(key)
            self.remove_key(key)
            return entity

    def discard_key(self, key):
        self.discard_key_ex(key)
        return
        # old version
        if self.contain_key(key):
            self.remove_key(key)
    def discard_key_ex(self, key):
        # -> does_iremove
        idiscard_ex = self.Node.find_and_idiscard_first_or_last_entity_of_subtree_ex
        does_iremove, payload = idiscard_ex(self.__tree, key, True)
        does_iremove = bool(does_iremove)

        if does_iremove:
            old_entity, new_root = payload
            self.__size -= 1
            self.__tree = new_root
        return does_iremove

    def remove_key(self, key):
        # may raise KeyError
        f = self.Node.find_and_iremove_first_or_last_entity_of_subtree
        self.__tree = f(self.__tree, key, True)
        self.__size -= 1


    def __contains__(self, x):
        key = self.Node.entity2key(x)
        return self.contain_key(key)


    def update(self, iterable):
        return self.update_right_biased(iterable)
    def update_left_biased(self, iterable):
        for x in iterable:
            self.add_if_not_any(x)
    def update_right_biased(self, iterable):
        for x in iterable:
            self.add(x)
    def remove(self, x):
        key = self.Node.entity2key(x)
        self.remove_key(key)
    def discard(self, x):
        key = self.Node.entity2key(x)
        self.discard_key(key)

    def add_key2entity_if_not_any(self, key, key2entity):
        # precondition: key_eq(key, entity2key(key2entity(key)))
        self.add_key2entity_if_not_any_ex(key, key2entity)
    def add_key2entity_if_not_any_ex(self, key, key2entity):
        # -> does_iinsert
        # precondition: key_eq(key, entity2key(key2entity(key)))
        f = self.Node.find_and_iinsert_key2entity_of_tree_if_not_any_ex
        does_iinsert, root = f(self.__tree, key, key2entity)
        does_iinsert = bool(does_iinsert)

        self.__size += does_iinsert
        self.__tree = root
        return does_iinsert

    def add_if_not_any(self, x):
        self.add_if_not_any_ex(x)
    def add_if_not_any_ex(self, x):
        # -> does_iinsert
        key = self.entity2key(x)
        def key2entity(key): return x
        return self.add_key2entity_if_not_any_ex(key, key2entity)



    def add(self, x):
        self.add_ex(x)
    def add_ex(self, x):
        # -> does_iinsert
        f = self.Node.find_and_ireplace_first_or_last_entity_or_iinsert_entity_of_tree_ex
        does_iinsert, (may_old_entity, new_root) = f(self.__tree, x, True)
        does_iinsert = bool(does_iinsert)

        self.__size += does_iinsert
        self.__tree = new_root
        return does_iinsert

    def pop(self):
        return self.popright()
    def popleft(self):
        return self.pop_left_or_right(False)
    def popright(self):
        return self.pop_left_or_right(True)
    def pop_left_or_right(self, right:bool):
        if not self:
            raise KeyError('pop empty set')
        RBT_Node = self.Node

        f = RBT_Node.rbt_ipop_the_first_or_last_entity_of_subtree
        last = bool(right)
        entity, root = f(self.__tree, last)

        self.__tree = root
        self.__size -= 1
        return entity


    def clear(self):
        if self:
            self.__tree = self.Node.make_root_leaf()
            self.__size = 0

    #############
    @staticmethod
    def __iter(RBT_Node, tree, *, reverse):
        f = RBT_Node.iter_entities_of_subtree
        return f(tree, reverse=reverse)
        # bug: always empty iterator
        # def __iter(RBT_Node, tree, *, reverse):
        #   f = ...
        #   return f(...)
        #   # old version
        #   ...
        #   yield ...
        #

        # old version
        @staticmethod
        def __iter(RBT_Node, tree, *, reverse):
            if reverse:
                leaf = RBT_Node.get_last_leaf(tree)
                #eprint('tree', RBT_Node.rbt_helper_to_plain(tree))
                #eprint('leaf', RBT_Node.rbt_helper_to_direction_path_ex(leaf))

                it = RBT_Node.leaf_to_inorder_iter_reversed_nonleaf_node_pairs(leaf, neg_inf)
            else:
                leaf = RBT_Node.get_first_leaf(tree)
                it = RBT_Node.leaf_to_inorder_iter_nonleaf_node_pairs(leaf, neg_inf)
            get_the_entity = RBT_Node.get_the_entity
            for nonleaf, depth in it:
                yield get_the_entity(nonleaf)
    @staticmethod
    def __count_size(RBT_Node, tree):
        # O(n)
        return len_of_iterator(__class__.__iter(RBT_Node, tree, reverse=False))

    def __iter__(self):
        return self.__iter(self.Node, self.__tree, reverse=False)
    def __reversed__(self):
        return self.__iter(self.Node, self.__tree, reverse=True)

    def issuperset(self, other):
        return self >= other

    def issubset(self, other):
        if not isinstance(other, __class__): raise TypeError
        if self.Node != other.Node: raise TypeError
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
        output = cls.from_sorted_entities(Node, it)
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
        output = cls.from_sorted_entities(Node, it)
        return output

MutableSet.register(KeyOrderedSet)
assert issubclass(KeyOrderedSet, MutableSet)



def g():
    This = KeyOrderedSet
    key_ops = TotalOrderingOps(operator.__ge__, operator.__eq__)
    entity2key = len
    RBT_Node__tmp = KeyOrderedRedBlackTreeNodeOps__sized_immutable(key_ops, len)
    That = lambda iterable: KeyOrderedSet(iterable, RBT_Node=RBT_Node__tmp)
def f():
    This = KeyOrderedSet
    s = This()
    #s = This(range(2))
    ops = s.Node
    assert not ops.key_le(1, 0)
    assert not ops.key_lt(1, 0)
    assert ops.key_lt(0, 1)
    assert ops.key_le(0, 1)
    assert not ops.key_eq(0, 1)
    assert not ops.key_eq(1, 0)

    s.add('0')
    root = s._KeyOrderedSet__tree
    entity = '1'
    begin = ops.find_begin_or_end_leaf_of_subtree(root, entity, False)
    end = ops.find_begin_or_end_leaf_of_subtree(root, entity, True)
    print('begin', ops.rbt_helper_to_direction_path_ex(begin))
    print('end', ops.rbt_helper_to_direction_path_ex(end))
    try:
        ops.leaf_to_inorder_succ_nonleaf_entity_position_ex(begin, neg_inf)
    except StopIteration:
        pass
    else:
        raise logic-error
    prev, _, _ = ops.leaf_to_inorder_prev_nonleaf_entity_position_ex(end, neg_inf)
    assert '0' == ops.get_the_entity(prev)


    find = ops.find_maybe_first_or_last_nonleaf_ex_of_subtree
    node_, may_pos, depth = find(root, 0, entity, False)
    print('node is leaf' if ops.is_leaf(node_) else 'node is not leaf')
    print('node_', ops.rbt_helper_to_direction_path_ex(node_))

    s.add('1')
    assert len(s) == 2
    root = s._KeyOrderedSet__tree

    print('root', ops.rbt_helper_to_plain(root))
    print()

    entity = '2'
    begin = ops.find_begin_or_end_leaf_of_subtree(root, entity, False)
    end = ops.find_begin_or_end_leaf_of_subtree(root, entity, True)
    print('begin', ops.rbt_helper_to_direction_path_ex(begin))
    print('end', ops.rbt_helper_to_direction_path_ex(end))

    new_root = ops.rbt_iinsert_entity_at_leaf(begin, entity)
    print('new_root', ops.rbt_helper_to_plain(new_root))

    parent_info, plain_node = s._KeyOrderedSet__tree
    print(parent_info)
    print()
    print(plain_node)

    r = s.pop() # 1?
    try:
        assert r == '1'
    except:
        print(r)
        raise

    s = This(range(3))
    try:
        assert list(s) == [0,1,2]
    except:
        print(s)
        raise
if 0 and __name__ == "__main__":
    f()

if __name__ == "__main__":
    XXX = KeyOrderedSet

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest.testmod(raise_on_error=True)

