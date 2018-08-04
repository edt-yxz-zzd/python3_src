
'''

# equivalence classes;
# partition of a set;
# connected components of a undirected graph
# support operations:
#     merge partitions ==>> .merge_elems


[Handbook of Mathematics::5. Algebra and Discrete Mathematics
    5.2 Set Theory::5.2.4 Equivalence and Order Relations
    2. Equivalence Classes, Partitions]
    [page295]
        An equivalence relation in a set A defines a partition of A into non-empty pairwise disjoint subsets, into equivalence classes.


'''


__all__ = '''
    SetPartition
    BoundedIntSetPartition
'''.split()


import itertools
import collections
from seed.types.Maybe import *
from abc import abstractmethod, ABCMeta
from seed.helper import repr_helper


def is_sorted(iterable):
    it = iter(iterable)
    for fst in it:
        break
    else:
        return True

    for snd in it:
        if fst > snd:
            return False
    return True



class SetPartitionMixin:
    @classmethod
    def from_partitions(cls, partitions, *, disjoint=True, new_elems_allowed=True):
        self = cls.factory_SetPartition()
        self.add_partitions(partitions, disjoint=disjoint, new_elems_allowed=new_elems_allowed)
        return self

    def add_partitions(self, partitions, *, disjoint=True, new_elems_allowed=True):
        for partition in partitions:
            self.add_partition(partition, disjoint=disjoint, new_elems_allowed=new_elems_allowed)

    def to_elem_set_view(self):
        return frozenset(self.iter_elems())
    def add_partition(self, partition, *, disjoint=True, new_elems_allowed=True):
        'return Maybe std_elem'
        existed_elems = self.to_elem_set_view()
        
        input_elems = frozenset(partition)
        new_elems = input_elems - existed_elems
        elems_to_be_merged = input_elems & existed_elems
        
        if not new_elems_allowed and new_elems:
            raise ValueError('new_elems_allowed==False but exist new_elems')
        if disjoint and elems_to_be_merged:
            raise ValueError('disjoint==True but actually not disjoint')
        
        self.add_disjoint_partition(new_elems)
        return self.merge_partitions_via_elems(input_elems)

    def add_disjoint_partition(self, partition):
        '<==> add([partition], disjoint = True, new_elems_allowed = True)'
        partition = frozenset(partition)
        if not partition:
            return nothing
        
        elem_set = self.to_elem_set_view()
        if not elem_set.isdisjoint(partition):
            raise ValueError('self and new_partition should be disjoint')

        
        
        std_elem = next(iter(partition))
        self._add_disjoint_partition(partition, std_elem)
        return just(std_elem)
        
    def are_in_same_partition(self, elems):
        return len(set(map(self.to_std_elem, elems))) < 2

        
    def merge_partitions_via_elems(self, elems):
        '''precondition: elems <= self; return Maybe std_elem'''
        return merge_partitions_via_elems(self, elems)
        
    def iter_partitions(self):
        'return Iterator (Iterable elem)'
        d = collections.defaultdict(list)
        for e in self.iter_elems():
            std = self.to_std_elem(e)
            d[std].append(e)
        return d.values()
        
    def output_partitions(self, outer_t, inner_t):
        return outer_t(map(inner_t, self.iter_partitions()))
    
        
    def __repr__(self):
        partitions = self.to_frozenset()
        return '{}({})'.format(type(self).__name__, partitions)

    def sorted_repr(self, key=None):
        key_for_elem = key
        clss = self.iter_partitions()
        clss = [sorted(cls, key=key_for_elem) for cls in clss]
        if key is None:
            key_for_cls = None
        else:
            def key_for_cls(cls):
                return tuple(map(key_for_elem, cls))

        clss = sorted(clss, key=key_for_cls)
        return '{}({})'.format(type(self).__name__, clss)

    def to_frozenset(self):
        'frozenset< frozenset<elem> >'
        return self.output_partitions(frozenset, frozenset)
    def to_elem2partition(self, items2dict=dict):
        def to_items(self):
            for iter_partition in self.iter_partitions():
                partition = frozenset(iter_partition)
                for elem in partition:
                    yield elem, partition

        return items2dict(to_items(self))

    def __eq__(self, other):
        if type(self) is not type(other):
            return NotImplemented
        return self.to_frozenset() == other.to_frozenset()
    def __ne__(self, other):
        if type(self) is not type(other):
            return NotImplemented
        return not self == other
    
class SetPartitionABC(SetPartitionMixin, metaclass=ABCMeta):
    '''

input:
    partition :: Iter elem
    partitions :: Iter (Iter elem)
    disjoint=True: means input contains no elems in self
    new_elems_allowed=True: means allowing input contain elems not in self
'''
    @classmethod
    def factory_SetPartition(cls):
        return cls()
    @abstractmethod
    def _add_disjoint_partition(self, partition, std_elem):
        '''precondition:
    std_elem in partition;
    self and partition are disjoint;
    partition is iterable
'''
        raise NotImplementedError
    
    @abstractmethod
    def _merge_to_left_partition(self, left_std_elem, right_std_elem):
        'precondition :: input are different std elems'
        raise NotImplementedError        

    @abstractmethod
    def iter_elems(self):
        raise NotImplementedError


    

    @abstractmethod
    def set_std_elem(self, elem):
        raise NotImplementedError
        
    @abstractmethod
    def to_std_elem(self, elem):
        raise NotImplementedError

    @abstractmethod
    def add_elem(self, elem):
        'elem in or not in self; return None'
        raise NotImplementedError

    def is_std_elem(self, elem):
        return elem == self.to_std_elem(elem)


def merge_partitions_via_elems(self, elems):
    '''precondition: elems <= self; return Maybe std_elem'''
    elems = iter(elems)
    for head in elems:
        break
    else:
        return nothing

    fst = self.to_std_elem(head)
    for elem in elems:
        snd = self.to_std_elem(elem)
        if fst != snd:
            self._merge_to_left_partition(fst, snd)
    return just(fst)

def to_std_elem(elem2parent, elem):
    ls = [] # non_std_elems
    parent = elem2parent[elem]
    while parent != elem:
        # elem is not a std_elem
        ls.append(elem)
        elem = parent
        parent = elem2parent[elem]

    std = elem

    if ls:
        ls.pop() # since ls[-1] -> std
        for non_std in ls:
            # set non_std -> std
            elem2parent[non_std] = std
    return std



class SetPartition(SetPartitionABC):
    def __init__(self, partitions=(), *, disjoint=True, new_elems_allowed=True):
        self.__elems = set()
        self.__elem2parent = {} # if elem2parent[x] == x then x is a root
        self.add_partitions(partitions, disjoint=disjoint, new_elems_allowed=new_elems_allowed)
            
    def _add_disjoint_partition(self, partition, std_elem):
        '''precondition:
    std_elem in partition;
    self and partition are disjoint;
    partition is iterable
'''
        for elem in partition:
            self.__elem2parent[elem] = std_elem
            self.__elems.add(elem)
    def _merge_to_left_partition(self, left_std_elem, right_std_elem):
        'precondition :: input are different std elems'
        assert self.is_std_elem(left_std_elem)
        assert self.is_std_elem(right_std_elem)
        assert left_std_elem != right_std_elem
        self.__elem2parent[right_std_elem] = left_std_elem
        
    def iter_elems(self):
        return iter(self.__elems)
    def set_std_elem(self, elem):
        old_std = self.to_std_elem(elem)
        new_std = elem
        self.__elem2parent[new_std] = new_std
        self.__elem2parent[old_std] = new_std
    def to_std_elem(self, elem):
        return to_std_elem(self.__elem2parent, elem)
            
    def add_elem(self, elem):
        'elem in or not in self; return None'
        if elem in self.__elems:
            return
        self.__elems.add(elem)
        self.__elem2parent[elem] = elem
        return

    def is_std_elem(self, elem):
        return elem == self.__elem2parent[elem]






















    

class BoundedIntSetPartition:
    # no set_std_elem(self, elem) using mini elem as std

    
    def __init__(self, n, partitions=None):
        'disjoint = False; new_elems_allowed = False'
        self.__elem2parent = list(range(n))
        if partitions is not None:
            for elems in partitions:
                self.merge_partitions_via_elems(elems)
    
    @property
    def __n(self):
        return len(self.__elem2parent)
    def _merge_to_left_partition(self, left_std_elem, right_std_elem):
        'precondition :: input are different std elems'
        assert self.is_std_elem(left_std_elem)
        assert self.is_std_elem(right_std_elem)
        assert left_std_elem != right_std_elem
        # not to left but to min one
        if left_std_elem > right_std_elem:
            left_std_elem, right_std_elem = right_std_elem, left_std_elem
        self.__elem2parent[right_std_elem] = left_std_elem
        
    def merge_partitions_via_elems(self, elems):
        '''precondition: elems <= self; return Maybe std_elem'''
        maybe_elem = merge_partitions_via_elems(self, elems)
        if maybe_elem != nothing:
            elem = unjust(maybe_elem)
            std = self.to_std_elem(elem)
            maybe_elem = just(std)
        return maybe_elem

    def iter_elems(self):
        return iter(range(self.__n))

        
    def to_std_elem(self, elem):
        return to_std_elem(self.__elem2parent, elem)


    def is_std_elem(self, elem):
        return elem == self.to_std_elem(elem)

    
    def are_in_same_partition(self, elems):
        return len(set(map(self.to_std_elem, elems))) < 2

    def __repr__(self):
        return repr_helper(self, self.__n, self.to_sorted_partitions())
    

    def to_sorted_partitions(self):
        ls = sorted(self.iter_elems(), key=self.to_std_elem)
        partitions = [tuple(ipartition) for std_elem, ipartition in itertools.groupby(ls, self.to_std_elem)]
        partitions.sort()
        assert all(map(is_sorted, partitions))
        return partitions
    def to_elem2min_elem(self):
        return tuple(map(self.to_std_elem, self.iter_elems()))
    
    def __eq__(self, other):
        if type(self) is not type(other):
            return NotImplemented
        return self.__n == other.__n and self.to_elem2min_elem() == other.to_elem2min_elem()
    def __ne__(self, other):
        if type(self) is not type(other):
            return NotImplemented
        return not self == other
    


bp = BoundedIntSetPartition(5, [(1,), (2,4), (3,)])
assert bp == BoundedIntSetPartition(5, [(0,), (1,), (2, 4), (3,)])
bp.merge_partitions_via_elems([0, 1, 4])
assert bp == BoundedIntSetPartition(5, [(0, 1, 2, 4), (3,)])
































        

class __deprecated__SetPartition: # deprecated
    # equivalence classes;
    # partition of a set;
    # connected components of a undirected graph
    # support operations:
    #     merge partitions ==>> .merge_elems
    class __Node:
        def __init__(self, elem, parent=None):
            self.elem = elem
            self.parent = self if parent is None else parent
        def is_root(self):
            return self.parent is self
        def __eq__(self, other):
            return self is other
        def __ne__(self, other):
            return not self == other
        
        def __hash__(self):
            return id(self)
    def __make_node(self, elem, parent=None):
        return __class__.__Node(elem, parent)


            
        
    def __init__(self, eq_clses, *, disjoint=True, new_elems_allowed=True):
        'eq_clses :: [[elem]]'
        elem2node = self.__elem2node = {}
        elem_set = self.__elem_set = set()
        self.update_eq_clses(eq_clses,
                        disjoint=disjoint,
                        new_elems_allowed=new_elems_allowed)
        
        
    def update_eq_clses(self, eq_clses, *, disjoint=True, new_elems_allowed=True):
        for eq_cls in eq_clses:
            self.update(eq_cls,
                        disjoint=disjoint,
                        new_elems_allowed=new_elems_allowed)

    def update(self, eq_cls, *, disjoint=True, new_elems_allowed=True):
        '''

input:
    eq_cls :: [[elem]] i.e. iterable< iterable <elem> >
    disjoint=True: means input contains no elems in self
    new_elems_allowed=True: means allowing input contain elems not in self


        
    if disjoint == True:
        add a new equivalence class
    else:
        add pairwise equal rules on input elems
        that is to merge the eq_clses of input elems
        

    if new_elems_allowed == True:
        each input elem will be added to self
    else:
        each input elem should be in self

    case disjoint, new_elems_allowed of
        (True, True) -> add a new equivalence class
        (True, False) -> input should be empty, non-interesting
        (False, True) -> add input elem to self, merge their eq_clses
        (False, False) -> merge input elems' eq_clses
'''
        elem2node = self.__elem2node
        elem_set = self.__elem_set
        
        input_elems = set(eq_cls)
        existed_elems = elem_set
        new_elems = input_elems - existed_elems
        elems_to_be_merged = input_elems & existed_elems
        
        if not new_elems_allowed and new_elems:
            raise ValueError('new_elems_allowed==False but exist new_elems')
        if disjoint and elems_to_be_merged:
            raise ValueError('disjoint==True but actually not disjoint')
        
        self.add_new_partition(new_elems)
        self.merge_elems(input_elems)

    def merge_elems(self, elems):
        # all elems should be in self
        elems = set(elems)
        if not elems:
            return
        roots = set(map(self.__elem2root, elems))
        
        std_root = roots.pop()
        for root in roots:
            # assert root is not std_root
            root.parent = std_root
        
    def add_new_partition(self, new_partition):
        # as if :: disjoint = True, new_elems_allowed = True
        # self and new_partition should be disjoint

        
        # new_partition should be a container intead of iterator
        # new_partition should be a set instance
        
##        if not isinstance(new_partition, (set, frozenset)):
##            raise TypeError
        new_partition = frozenset(new_partition)
        if len(new_partition) == 0:
            return
        
        elem2node = self.__elem2node
        elem_set = self.__elem_set

        old_size = len(elem_set)
        delta_size = len(new_partition) # set required  -------------------
        expeted_size = old_size + delta_size
        elem_set |= new_partition       # set required  -------------------
        if len(elem_set) != expeted_size:
            elem_set = set(self.__elem2node) # restore
            raise ValueError('self and new_partition should be disjoint')

        
        
        std_elem = next(iter(new_partition))
        node = self.__make_node(std_elem)

        for e in new_partition:
            elem2node[e] = node
        

            

    def __elem2root(self, elem):
        elem2node = self.__elem2node
        nonroots = []
        node = elem2node[elem]
        while not node.is_root():
            nonroots.append(node)
            node = node.parent

        root = node
        for node in nonroots:
            # bug:
            #    once this body only contains:
            #        elem2node[node.elem] = root
            #    heights of other leaves are not changed
            elem2node[node.elem] = root
            node.parent = root # maybe was root though # patch
            
        return root

    def are_of_same_eq_cls(self, elem, *elems):
        elem2root = self.__elem2root
        std_root = elem2root(elem)
        pred = lambda e: elem2root(e) is std_root
        return all(map(pred, elems))
    

    def set_std_elem(self, elem):
        root = self.__elem2root(elem)
        root.elem = elem
        
    def to_std_elem(self, elem):
        root = self.__elem2root(elem)
        return root.elem

##    def merge(self, std_elem, *elems):
##        std_root = self.__elem2root(std_elem)
##        for elem in elems:
##            root = self.__elem2root(elem)
##            if root is not std_root:
##                root.parent = std_root

    def add_elem(self, elem):
        elem2node = self.__elem2node
        elem_set = self.__elem_set
        if elem in elem2node:
            return
        elem2node[elem] = self.__make_node(elem)
        elem_set.add(elem)
        assert len(elem2node) == len(elem_set)
    
    def elems(self):
        return self.__elem2node.keys()
    def iter_partitions(self):
        d = collections.defaultdict(list)
        for e in self.elems():
            std = self.to_std_elem(e)
            d[std].append(e)
        return d.values()
    def output_partitions(self, type=list):
        return type(self.iter_partitions())
    
        
    def __repr__(self):
        clss = self.output_partitions()
        return '{}({})'.format(type(self).__name__, clss)

    def sorted_repr(self, key=None):
        key_for_elem = key
        clss = self.iter_partitions()
        clss = [sorted(cls, key=key_for_elem) for cls in clss]
        if key is None:
            key_for_cls = None
        else:
            def key_for_cls(cls):
                return tuple(map(key_for_elem, cls))

        clss = sorted(clss, key=key_for_cls)
        return '{}({})'.format(type(self).__name__, clss)

    def to_frozenset(self):
        'frozenset< frozenset<elem> >'
        clss = self.iter_partitions()
        return frozenset(map(frozenset, clss))

    def __eq__(self, other):
        return isinstance(other, type(self)) and\
               self.to_frozenset() == other.to_frozenset()
    def __ne__(self, other):
        return not self == other
    
    
        
            
s = SetPartition([(1,2), (3,), (4,5)])
#print(s.sorted_repr())
s.add_elem(6)
#print(s.sorted_repr())
assert s.sorted_repr() == \
       'SetPartition([[1, 2], [3], [4, 5], [6]])'
assert s.sorted_repr(key=lambda x:-x) == \
       'SetPartition([[6], [5, 4], [3], [2, 1]])'
assert s == SetPartition([[1, 2], [3], [4, 5], [6]])\
         == SetPartition([[6], [5, 4], [3], [2, 1]])

s.merge_partitions_via_elems([1,6,2,4])
assert s.sorted_repr() == \
       'SetPartition([[1, 2, 4, 5, 6], [3]])'
assert s.sorted_repr(key=lambda x:-x) == \
       'SetPartition([[6, 5, 4, 2, 1], [3]])'
assert s == SetPartition([[1, 2, 4, 5, 6], [3]])\
         == SetPartition([[6, 5, 4, 2, 1], [3]])









