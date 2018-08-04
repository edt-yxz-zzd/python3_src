
__all__ = '''
    KeyOrderedMap
    '''.split()


from .KeyOrderedSet import KeyOrderedSet, Node__global
from ..KeyOrderedTreeNodeOps.TotalOrderingOps import \
    TotalOrderingOps, python_total_key_ops
from ..RedBlackTreeNodeOps__concrete.KeyOrderedRedBlackTreeNodeOps__sized_immutable import \
    KeyOrderedRedBlackTreeNodeOps__sized_immutable
from ..KeyOrderedTreeNodeOps.IKeyOrderedRedBlackTreeNodeOps__imodify import \
    IKeyOrderedRedBlackTreeNodeOps__imodify

from collections.abc import MutableMapping
import operator
from seed.helper.repr_input import repr_helper
from seed.tiny import echo





def make_pop():
    Nothing = object()
    def pop(self, dict_key, default=Nothing):
        def fdefault():
            if default is Nothing:
                raise KeyError(dict_key)
            return default
        return self.pop_dict_value_of_dict_key(dict_key, fdefault=fdefault)



def eprint(*args):
    import sys
    print(*args, file=sys.stderr)


def override(f):
    return f
def to_pair(iterable):
    a, b = iterable
    return a, b

class KeyOrderedMap(MutableMapping):
    '''mapping base on comparason (red-black-tree)

## !!!!!!! if the key is mutable, this dict will fail!!!!!!!!!

entity = item = (dict_key, dict_val)
tree_key = set_key = fst2key dict_key

fst2key :: dict_key -> tree_key
entity2key = fst2key . fst :: item -> tree_key


see:
    KeyOrderedSet
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
    >>> This = KeyOrderedMap
    >>> m = This()
    >>> m
    KeyOrderedMap([])
    >>> len(m)
    0

    >>> m[1] = 4
    >>> m[2] = 3
    >>> m[0] = 1
    >>> m
    KeyOrderedMap([(0, 1), (1, 4), (2, 3)])
    >>> len(m)
    3

    # reverse
    >>> key_ops = TotalOrderingOps(operator.__ge__, operator.__eq__)
    >>> fst2key = len
    >>> entity2key = lambda item: fst2key(item[0])
    >>> Node = KeyOrderedRedBlackTreeNodeOps__sized_immutable(key_ops, entity2key)
    >>> That = lambda *args, **kwargs: KeyOrderedMap(*args, RBT_Node=Node, fst2key=fst2key, **kwargs)

    ## but if the key is mutable, this dict will fail!!!!!!!!!
    >>> m = That([([], 4), ({1,2}, 2), ((1,), 5), ['3535', 3]])
    >>> m # doctest: +ELLIPSIS
    KeyOrderedMap([('3535', 3), ({1, 2}, 2), ((1,), 5), ([], 4)], ...)

    #KeyOrderedMap([('3535', 3), ({1, 2}, 2), ((1,), 5), ([], 4)], RBT_Node = ..., fst2key = ...)

    >>> m.setdefault([0], '') # do nothing
    >>> m # doctest: +ELLIPSIS
    KeyOrderedMap([('3535', 3), ({1, 2}, 2), ((1,), 5), ([], 4)], ...)

    >>> del m[[0]]
    >>> m # doctest: +ELLIPSIS
    KeyOrderedMap([('3535', 3), ({1, 2}, 2), ([], 4)], ...)
    >>> m.setdefault([0], '')
    >>> m # doctest: +ELLIPSIS
    KeyOrderedMap([('3535', 3), ({1, 2}, 2), ([0], ''), ([], 4)], ...)


'''
    __slots__ = '_KeyOrderedMap__set _KeyOrderedMap__fst2key'.split()

    def __init__(self, iterable=None
            , *, RBT_Node=None, fst2key=None
            , is_sorted=False, reverse=False, strict=False
            ):
        '''

iterable :: None | Iter Entity
RBT_Node :: None | IKeyOrderedRedBlackTreeNodeOps__imodify
    see:
        KeyOrderedRedBlackTreeNodeOps__sized_immutable
        TotalOrderingOps
            python_total_key_ops

fst2key :: None | dict_key -> tree_key
    if fst2key is None: fst2key = echo
    if RBT_Node is None: RBT_Node = Node__global
    assert (fst2key . fst) == RBT_Node.entity2key
        # !!!!!!!precondition!!!!!!!!!!
        i.e. RBT_Node.key_eq(fst2key(entity[0]), RBT_Node.entity2key(entity))

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
        if fst2key is None:
            fst2key = echo
        else:
            assert callable(fst2key)
        #precondition: assert (fst2key . fst) == RBT_Node.entity2key

        if iterable is not None:
            iterable = map(to_pair, iterable)

        self.__set = KeyOrderedSet(iterable, RBT_Node=RBT_Node
                        , is_sorted=is_sorted, reverse=reverse, strict=strict)
        self.__fst2key = fst2key

    @property
    def Node(self):
        return self.__set.Node



    @classmethod
    def make_empty_map(cls, RBT_Node):
        return cls(RBT_Node=RBT_Node)
    def assign(self, other):
        tmp = other.copy()
        self.swap(tmp)
    def copy(self):
        cls = type(self)
        RBT_Node = self.Node

        new = cls.make_empty_map(RBT_Node)
        new.__set = self.__set.copy()
        new.__fst2key = self.__fst2key
        return new


    def __repr__(self):
        entities = list(self.items())
        if self.Node is Node__global and self.fst2key is echo:
            return repr_helper(self, entities)
        return repr_helper(self, entities
                , RBT_Node=self.Node, fst2key=self.fst2key)

    def swap(self, other):
        if type(self) is not type(other): raise TypeError
        self.__test(other)

        a = self.__get_properties()
        b = other.__get_properties()
        self.__set_properties(b)
        try:
            other.__set_properties(a)
        except:
            self.__set_properties(a)
            raise

    def __get_properties(self):
        return self.__set, self.__fst2key
    def __set_properties(self, properties):
        if not len(properties) == 2: raise TypeError
        self.__set, self.__fst2key = properties


    @classmethod
    def from_sorted_entities(cls, RBT_Node, fst2key, entities
                            , reverse=False, strict=False):
        return cls(entities, RBT_Node=RBT_Node, fst2key=fst2key
            , is_sorted=True, reverse=reverse, strict=strict
            )



    def get_item_from_dict_key(self, dict_key
            , *, dict_key2result=None, item2result=None):
        # item is entity
        tree_key = self.fst2key(dict_key)

        if dict_key2result is None:
            tree_key2result = None
        else:
            def tree_key2result(tree_key):
                return dict_key2result(dict_key)

        return self.get_entity_from_tree_key(tree_key
                , tree_key2result=tree_key2result
                , entity2result=item2result)



    def may_get_item_from_dict_key(self, dict_key):
        # -> () | (item,)
        # item is entity
        tree_key = self.fst2key(dict_key)
        return self.may_get_entity_from_tree_key(tree_key)
    def may_get_entity_from_tree_key(self, tree_key):
        # -> () | (entity,)
        def tree_key2result(tree_key): return ()
        def entity2result(entity): return (entity,)
        return self.get_entity_from_tree_key(tree_key
                , tree_key2result=tree_key2result
                , entity2result=entity2result)

    def get_entity_from_tree_key(self, tree_key
            , *, tree_key2result=None, entity2result=None):
        return self.__set.get_entity(tree_key
                    , key2result=tree_key2result
                    , entity2result=entity2result)



    @property
    def fst2key(self):
        # dict_key -> tree_key
        return self.__fst2key
    @property
    def entity2key(self):
        return self.Node.entity2key
    @property
    def tree_key_lt(self):
        return self.Node.key_lt
    @property
    def tree_key_le(self):
        return self.Node.key_le
    @property
    def tree_key_eq(self):
        return self.Node.key_eq

    def __dict_key_cmp(self, tree_cmp, dict_key_lhs, dict_key_rhs):
        tree_key_lhs, tree_key_rhs = map(self.fst2key, [dict_key_lhs, dict_key_rhs])
        return tree_cmp(tree_key_lhs, tree_key_rhs)
    def dict_key_le(self, dict_key_lhs, dict_key_rhs):
        return self.__dict_key_cmp(self.tree_key_le, dict_key_lhs, dict_key_rhs)
    def dict_key_lt(self, dict_key_lhs, dict_key_rhs):
        return self.__dict_key_cmp(self.tree_key_lt, dict_key_lhs, dict_key_rhs)
    def dict_key_eq(self, dict_key_lhs, dict_key_rhs):
        return self.__dict_key_cmp(self.tree_key_eq, dict_key_lhs, dict_key_rhs)

    def item_eq(self, item_lhs, item_rhs):
        dict_key_lhs, value_lhs = item_lhs
        dict_key_rhs, value_rhs = item_rhs
        return (self.dict_key_eq(dict_key_lhs, dict_key_rhs)
            and value_lhs == value_rhs)



    def set_key2default(self, dict_key, dict_key2default):
        # default is a dict_value
        self.set_key2default_ex(dict_key, dict_key2default)
    def set_key2default_ex(self, dict_key, dict_key2default):
        # -> does_iinsert
        # default is a dict_value
        def tree_key2entity(tree_key):
            dict_value = dict_key2default(dict_key)
            entity = item = dict_key, dict_value
            return entity
        tree_key = self.fst2key(dict_key)
        does_iinsert = self.__set.add_key2entity_if_not_any_ex(
                            tree_key, tree_key2entity)
        return does_iinsert

    def set_fdefault(self, dict_key, fdefault):
        # default is a dict_value
        self.set_fdefault_ex(dict_key, fdefault)
    def set_fdefault_ex(self, dict_key, fdefault):
        # default is a dict_value
        # -> does_iinsert
        def dict_key2default(key):
            return fdefault()
        return self.set_key2default_ex(dict_key, dict_key2default)

    def pop_left_or_right_item(self, right:bool):
        return self.__set.pop_left_or_right(right)
    def pop_left_or_right_key(self, right:bool):
        dict_key, dict_value = self.pop_left_or_right_item(right)
        return dict_key
    def pop_left_or_right_value(self, right:bool):
        dict_key, dict_value = self.pop_left_or_right_item(right)
        return dict_value

    def popleft_item(self):
        return self.pop_left_or_right_item(False)
    def popright_item(self):
        return self.pop_left_or_right_item(True)
    def popleft_key(self):
        return self.pop_left_or_right_key(False)
    def popright_key(self):
        return self.pop_left_or_right_key(True)
    def popleft_value(self):
        return self.pop_left_or_right_value(False)
    def popright_value(self):
        return self.pop_left_or_right_value(True)


    def popitem_of_tree_key(self, tree_key, *, fdefault=None):
        entity = self.__set.pop_key(tree_key, fdefault=fdefault)
        # dict_key, dict_value = entity
        return entity

    def pop_dict_value_of_tree_key(self, tree_key, *, fdefault=None):
        def fdefault_ex():
            return None, fdefault()
        _, dict_value = self.popitem_of_tree_key(tree_key, fdefault=fdefault_ex)
        return dict_value

    def popitem_of_dict_key(self, dict_key, *, fdefault=None):
        tree_key = self.fst2key(dict_key)
        return self.popitem_of_tree_key(tree_key, fdefault=fdefault)
    def pop_dict_value_of_dict_key(self, dict_key, *, fdefault=None):
        tree_key = self.fst2key(dict_key)
        return self.pop_dict_value_of_tree_key(tree_key, fdefault=fdefault)


    # dict ops
    @override
    def __len__(self):
        return len(self.__set)
    @override
    def __getitem__(self, dict_key):
        #tree_key = self.fst2key(dict_key)
        item = self.get_item_from_dict_key(dict_key)
        dict_key, dict_value = item
        return dict_value
    @override
    def __setitem__(self, dict_key, value):
        #tree_key = self.fst2key(dict_key)
        entity = dict_key, value
        self.__set.add(entity)
    @override
    def __delitem__(self, dict_key):
        tree_key = self.fst2key(dict_key)
        self.__set.remove_key(tree_key)
    @override
    def get(self, dict_key, default=None):
        def dict_key2result(dict_key):
            return default
        return self.get_item_from_dict_key(dict_key
            , dict_key2result=dict_key2result)

    @override
    def items(self):
        return iter(self.__set)
    @override
    def keys(self):
        for dict_key, value in self.items():
            yield dict_key
    @override
    def values(self):
        for dict_key, value in self.items():
            yield value
    @override
    def __iter__(self):
        return self.keys()

    @override
    def __contains__(self, dict_key):
        tree_key = self.fst2key(dict_key)
        return self.__set.contains_key(tree_key)

    def __test(self, other):
        # assert isinstance(other, __class__)
        if self.Node != other.Node: raise TypeError
        if self.fst2key != other.fst2key: raise TypeError

    @override
    def __eq__(self, other):
        if not isinstance(other, __class__): return NotImplemented
        self.__test(other)

        if len(self) != len(other): return False
        return all(map(self.item_eq, self.items(), other.items()))

    @override
    def __ne__(self, other):
        return not (self == other)
    @override
    def popitem(self):
        return self.popright_item()

    @override
    def clear(self):
        self.__set.clear()
    @override
    def setdefault(self, dict_key, default=None):
        self.set_fdefault(dict_key, lambda: default)

    pop = override(make_pop())
        #   how pop? what is its API??

    def update(self, other_or_items):
        if isinstance(other_or_items, __class__):
            other = other_or_items
            self.__test(other)
            self.__set.update(other.__set)
        else:
            items = other_or_items
            self.__set.update(map(to_pair, items))
        pass


#MutableMapping.register(KeyOrderedMap)
assert issubclass(KeyOrderedMap, MutableMapping)



if __name__ == '__main__':
    XXX = KeyOrderedMap

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

