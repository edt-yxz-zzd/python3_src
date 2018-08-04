
'''
LeftistTreeForPriorityQueue - 1971 by Clark A. Crane
met at: AOCP vol3 2ed 5.2.3 page150

2016/1/7
'''

__all__ = ['LeftistTreeForPriorityQueue']


import collections
from operator import lt as eye_less_than
eye_key = lambda x:x

class _Leaf:
    # key = +inf
    __slots__ = ()
_leaf = None
def _Leaf():
    # key = +inf
    return _leaf

def _is_leaf(node):
    return node is None
def _min_leaf_height(node):
    if _is_leaf(node):
        return 0
    return node.min_leaf_height
def _node_less_than(key_less_than, lnode, rnode):
    if _is_leaf(lnode):
        # leaf leaf +inf
        return False
    if _is_leaf(rnode):
        # right leaf +inf
        return True

    # compare key instead of value!!
    return key_less_than(lnode.key, rnode.key)


_NodeAttr = ('key', 'value', 'left', 'right', 'min_leaf_height')
_NodeBase = collections.namedtuple('_NodeBase', _NodeAttr)

class _Node(_NodeBase):
    __slots__ = () # _NodeAttr
    
    def __new__(cls, key, value, left=None, right=None):

        left = _Leaf() if left is None else left
        right = _Leaf() if right is None else right
        assert _min_leaf_height(right) <= _min_leaf_height(left)
        
        min_leaf_height = 1 + _min_leaf_height(right)
        self = super(_Node, cls).__new__(cls,
                key=key, value=value,
                left=left, right=right,
                min_leaf_height=min_leaf_height)
        return self
        
        
    @staticmethod
    def from_root(root, left, right):
        return _Node(root.key, root.value, left, right)
    
    @staticmethod
    def from_root_N_2children(root, node1, node2):
        # may swap node1, node2
        if _min_leaf_height(node2) > _min_leaf_height(node1):
            node1, node2 = node2, node1
        return _Node.from_root(root, node1, node2)

    def iset_childrens(self, child1, child2):
        # 'i' for 'immutable'
        return self.from_root_N_2children(self, child1, child2)
    def iset_left_right(self, left, right):
        # 'i' for 'immutable'
        return self.from_root(self, left, right)
    def icut(self):
        return self.iset_left_right(_Leaf(), _Leaf()), self.left, self.right

    def __iter__(self):
        raise NotImplementedError('not iterable')
    
    '''
    def __init__(self, key, value, left=None, right=None):
        self.value = value
        self.key = key
        self.left = _Leaf() if left is None else left
        self.right = _Leaf() if right is None else right
        assert _min_leaf_height(self.right) <= _min_leaf_height(self.left)
        
        self.min_leaf_height = 1 + _min_leaf_height(self.right)
    '''

_Node(0,0)






def _merge_2nodes(key_less_than, node1, node2):
    '''merge 2 nodes into one node

the same as:
def _merge_2nodes(key_less_than, node1, node2):
    if _node_less_than(key_less_than, node2, node1):
        node1, node2 = node2, node1
    # what if a < b and b < a??
    assert not _node_less_than(key_less_than, node2, node1)
    root = node1
    if _is_leaf(root):
        assert _is_leaf(node2)
        return root
    
    child1 = root.left
    child2 = _merge_2nodes(key_less_than, root.right, node2)
    tree = _Node.from_root_N_2children(root, child1, child2)
    assert _min_leaf_height(tree) <= _min_leaf_height(node1) + _min_leaf_height(node2)
    return tree
'''
    stack = []
    
    while True:
        max_tree_min_leaf_height = _min_leaf_height(node1) + _min_leaf_height(node2)
        
        if _node_less_than(key_less_than, node2, node1):
            node1, node2 = node2, node1
        assert not _node_less_than(key_less_than, node2, node1)
        root = node1
        if _is_leaf(node2):
            tree = root
            break
        
        assert not _is_leaf(root)
        
        child1 = root.left
        stack.append((root, child1, max_tree_min_leaf_height))

        # calc child2 in next round
        node1, node2 = root.right, node2

    L = len(stack)
    while True:
        assert _min_leaf_height(tree) <= max_tree_min_leaf_height
        if not stack:
            break

        (root, child1, max_tree_min_leaf_height) = stack.pop()
        child2 = tree
        tree = _Node.from_root_N_2children(root, child1, child2)

    if not L <= max_tree_min_leaf_height:
        raise Exception('not L <= max_tree_min_leaf_height', L, max_tree_min_leaf_height)
    assert L <= max_tree_min_leaf_height # '<' if one node is a leaf
    return tree

def _pop_root(less_than, tree):
    # return cut_root, new_tree_removed_old_root
    if _is_leaf(tree):
        #raise ValueError('pop_root(leaf)')
        return _Leaf(), _Leaf()
    root, left, right = tree.icut()
    return root, _merge_2nodes(less_than, left, right)

def _init_tree_only_one_node(key, value):
    return _Node(key, value)

def _init_tree(key_f, key_less_than_f, iterable):
    merge_stack = []
    _____count = 0
    for value in iterable:
        _____count += 1
        
        tree = _init_tree_only_one_node(key_f(value), value)
        small = tree
        small_size = 1
        while merge_stack:
            to, to_size = merge_stack[-1]
            if to_size == small_size:
                merge_stack.pop()
                small = _merge_2nodes(key_less_than_f, to, small)
                small_size += to_size
            elif to_size > small_size:
                break
            else:
                raise Exception('bug: not len(to) >= len(small)')

        merge_stack.append((small, small_size))

    small = _Leaf()
    small_size = 0
    while merge_stack:
        to, to_size = merge_stack.pop()
        assert to_size > small_size
        small = _merge_2nodes(key_less_than_f, to, small)
        small_size += to_size

    
    tree, size = small, small_size
    assert _____count == size
    assert _min_leaf_height(tree) <= size.bit_length()
    return tree, size
    
    
    





class LeftistTreeForPriorityQueue:
    '''Leftist Tree For Priority Queue


performence:
1) treated as stack, insertion/deletion O(1)?? - I don't know
2) merge 2 disjoint trees, O(log(N1+N2)) - fast than balanced tree
3) initialize O(n) - I guess

constraint:
1) key(parent) <= key(child)
2) min_leaf_height(parent.left) >= min_leaf_height(parent.right)
3) min_leaf_height(parent) == min_leaf_height(parent.right) + 1
4) +inf = key(leaf) > key(nonleaf)
5) min_leaf_height(leaf) == 0


example:
    >>> Tree = LeftistTreeForPriorityQueue
    >>> Tree()
    LeftistTreeForPriorityQueue()
    >>> _.iadd(3) # immutable add; note this will return a new tree
    LeftistTreeForPriorityQueue([3])
    >>> tree = _.iupdate([4,5,1,8,4])
    >>> tree.check()
    >>> tree.nonstable_sorted_repr()
    'LeftistTreeForPriorityQueue([1, 3, 4, 4, 5, 8])'
    >>> tname = type(tree).__name__
    >>> repr(tree) == '{!s}({!r})'.format(tname, list(tree.values())) # unorder
    True
    >>> list(tree | Tree([9, -1]))
    [-1, 1, 3, 4, 4, 5, 8, 9]
    >>> tree.ipop() # doctest: +ELLIPSIS
    (LeftistTreeForPriorityQueue([...]), 1)
    >>> import operator
    >>> Tree([4,5,1,8,4], less_than=operator.gt) # doctest: +ELLIPSIS
    LeftistTreeForPriorityQueue([...], less_than=<...>)
    >>> list(_)
    [8, 5, 4, 4, 1]
    >>> Tree([4,5,1,8,4], key=lambda x:-x, less_than=operator.gt) # doctest: +ELLIPSIS
    LeftistTreeForPriorityQueue([...], key=<...>, less_than=<...>)
    >>> tree |= _
    Traceback (most recent call last):
        ...
    ValueError: self.key is not other.key
'''
    __slots__ = ('key', 'less_than', 'size', 'root')
     
    def __init__(self, iterable=None, *,
                 key=None,
                 less_than=None,
                 __from_node_N_size=None):
        self.less_than = eye_less_than if less_than is None else less_than
        self.key = eye_key if key is None else key
        #self.root = _Leaf()
        if __from_node_N_size is None:
            self.root = None
            self.size = None

            iterable = () if iterable is None else iterable
            self.__init(iterable)
        else:
            assert iterable is None
            self.root, self.size = __from_node_N_size
    def __len__(self):
        return self.size

    def __iter__(self):
        # NOTE: each iter log(N)
        #       total = log(N)*N
        # smallest-first
        while self:
            self, value = self.ipop()
            yield value
    def values(self):
        # O(N), but values are unordered.
        for node in self.__iter_tree():
            yield node.value

    def __repr__(self):
        return self.__repr(self.values())
    def __repr(self, iterable):
        #tpl = '{type!s}({iterable!r}{key!s}{lt!s})'
        tpl = '{type!s}({args!s})'
        typ = type(self).__name__
        itr = list(iterable)

        args = []
        if itr:
            args.append(repr(itr))
        if self.key is not eye_key:
            key = 'key=' + repr(self.key)
            args.append(key)

        if self.less_than is not eye_less_than:
            lt = 'less_than=' + repr(self.less_than)
            args.append(lt)
        
        return tpl.format(type=typ, args=', '.join(args))

    def nonstable_sorted_repr(self):
        return self.__repr(self)
        
            
    def __init(self, iterable):
        assert self.root == None
        assert self.size == None
        
        self.root, self.size = _init_tree(self.key, self.less_than, iterable)
        return

    def make_tree(self, iterable):
        # not class/static method!
        return LeftistTreeForPriorityQueue(
            iterable, key=self.key, less_than=self.less_than)
    def __from_node_N_size(self, node, size):
        assert size >= 0
        assert (size == 0) == _is_leaf(node)
        return LeftistTreeForPriorityQueue(
            key=self.key, less_than=self.less_than,
            _LeftistTreeForPriorityQueue__from_node_N_size=(node, size))
    
    def __from_2nodes(self, size, node1, node2):
        assert size >= 0
        assert (size == 0) == all(map(_is_leaf, [node1, node2]))
        root = _merge_2nodes(self.less_than, node1, node2)
        return LeftistTreeForPriorityQueue(
            key=self.key, less_than=self.less_than,
            _LeftistTreeForPriorityQueue__from_node_N_size=(root, size))
    
##    def update(self, iterable):
##        self <<= self.make_tree(iterable)
    def __ior__(self, other):
        # may not return self, since this is a immutable object
        return self | other
    
    def __or__(self, other):
        if not isinstance(other, LeftistTreeForPriorityQueue):
            raise NotImplemented
        if self.key is not other.key:
            raise ValueError('self.key is not other.key')
        if self.less_than is not other.less_than:
            raise ValueError('self.less_than is not other.less_than')

        size = len(self) + len(other)
        return self.__from_2nodes(size, self.root, other.root)

    def iupdate(self, iterable):
        return self | self.make_tree(iterable)
    def iadd(self, value):
        # 'i' stands for immutable
        return self.iupdate([value])
    
    
    def ipop(self):
        if not self:
            raise IndexError('pop empty tree')
        _root, tree = _pop_root(self.less_than, self.root)
        assert not _is_leaf(_root)

        itree = self.__from_node_N_size(tree, len(self)-1)
        return itree, self.top()
    def top(self):
        if not self:
            raise IndexError('top of empty tree')
        return self.root.value

    def __iter_tree(self):
        ls = [self.root]
        while ls:
            node = ls.pop()
            if _is_leaf(node):
                continue
            
            yield node
            cs = node.left, node.right
            ls.extend(cs)
            
    def check(self):
        assert len(self).bit_length() >= _min_leaf_height(self.root)
        count = 0
        for parent in self.__iter_tree():
            count += 1
            
            cs = [parent.left, parent.right]
            assert all(not _node_less_than(self.less_than, child, parent)
                       for child in cs)
            assert _min_leaf_height(parent.left) >= _min_leaf_height(parent.right)
            assert _min_leaf_height(parent) == _min_leaf_height(parent.right) + 1
        assert len(self) == count
        return
        
##    def merge_with(self, other):
##        self <<= other
##    def clear(self):
##        self.size = 0
##        self.root = _Leaf()
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
















