

'''
array
L = len(array)
SA
    len(SA) == L
    not include the empty isuffix (i.e. isuffix=L)
LCP
    len(LCP) == max(0, L-1)

SA vs SuffixTree
    SuffixTree contains the empty isuffix

SuffixTree = 
SuffixTreeNonRootNonLeaf = SuffixTreeNonRootNonLeaf
        { nonempty_common_prefix_range :: (begin_isuffix, end_isuffix_ex)
            # one of many such range
            # 0 <= begin_isuffix < end_isuffix_ex <= L
        , children :: [SuffixTreeNonRootNonLeaf|SuffixTreeLeaf]{2..}
        }

SuffixTreeLeaf = SuffixTreeNonEmptyLeaf | SuffixTreeEmptyLeaf
SuffixTreeNonEmptyLeaf = SuffixTreeNonEmptyLeaf {whole_isuffix :: UInt}
    # 0 <= whole_isuffix < L
    # whole_isuffix is begin from root, not the remain suffix
SuffixTreeEmptyLeaf = SuffixTreeEmptyLeaf
    # the empty leaf: suffix = array[L:]
SuffixTreeRootNonLeaf = SuffixTreeRootNonLeaf
        { children :: [SuffixTreeNonRootNonLeaf|SuffixTreeLeaf]{2..}
        }
SuffixTreeLeafRoot = SuffixTreeEmptyLeaf

'''

__all__ = '''
    SuffixTree
    '''.split()

from itertools import chain
from seed.helper.repr_input import repr_helper
from ..make_SA_LCP import make_SA_LCP as sa_lcp_from_array

old_print = print
def new_print(*args, **kwargs):pass

print = new_print
TESTING = False




class SuffixTreeNode:
    # begin_isuffix: choose the left most
    def __init__(self, begin_isuffix, size, children):
        #if not 0 <= begin_isuffix <= L: raise ValueError
        if not 0 <= begin_isuffix: raise ValueError
        if not 0 <= size: raise ValueError
        if size == 0:
            # self is root
            # begin_isuffix: choose the left most
            if not begin_isuffix == 0: raise ValueError

        # if begin_isuffix == end_isuffix_ex ==>> [self is root]
        children = tuple(children)
        if not all(isinstance(c, (SuffixTreeNode, SuffixTreeLeaf)) for c in children): raise TypeError

        self.begin_isuffix = begin_isuffix
        self.size = size
        self.children = children
    def is_root(self):
        return self.size == 0
    def __repr__(self):
        return repr_helper(self
                , self.begin_isuffix, self.size, list(self.children))
    def to_data(self):
        return (self.begin_isuffix, self.size
                , list(c.to_data() for c in self.children))



    # verify
    def iter_leaves(self):
        yield from chain.from_iterable(c.iter_leaves() for c in self.children)
    def verify(self, is_root, L):
        if bool(is_root) != self.is_root():
            return False
        if not 0 <= self.begin_isuffix <= self.begin_isuffix+self.size <= L: return False
        return all(c.verify(False, L) for c in self.children)

    def iter_LCP_ex(self, common_lcp):
        common_lcp += self.size
        it = iter(self.children)
        c = next(it)
        yield from c.iter_LCP_ex(common_lcp)

        for c in it:
            yield common_lcp
            yield from c.iter_LCP_ex(common_lcp)

    def iter_suffices_ex(self, array, prefix):
        L = len(array)
        begin_isuffix = self.begin_isuffix
        end_isuffix_ex = begin_isuffix + self.size
        #bug:prefix += array[begin_isuffix:end_isuffix_ex]
        prefix = prefix + array[begin_isuffix:end_isuffix_ex]

        yield from chain.from_iterable(c.iter_suffices_ex(array, prefix)
                                for c in self.children)

    def verify_with_array(self, array, common_lcp):
        L = len(array)
        common_lcp += self.size

        def get_may_first_char(c):
            if isinstance(c, SuffixTreeLeaf):
                begin_isuffix = c.whole_isuffix + common_lcp
            else:
                begin_isuffix = c.begin_isuffix
            if begin_isuffix == L:
                return ()
            return (array[begin_isuffix],)
        def all_mayhead_diff(cs):
            [*may_heads] = map(get_may_first_char, cs)
            return len(may_heads) == len(set(may_heads))


        return (all_mayhead_diff(self.children)
            and all(c.verify_with_array(array, common_lcp)
                    for c in self.children)
            )

class SuffixTreeLeaf:
    def __init__(self, whole_isuffix):
        if not whole_isuffix >= 0: raise ValueError
        self.whole_isuffix = whole_isuffix
    '''
    def is_root(self):
        return self.whole_isuffix == 0 == L
    '''

    def __repr__(self):
        return repr_helper(self, self.whole_isuffix)
    def to_data(self):
        return (self.whole_isuffix,)
    def iter_leaves(self):
        yield self
    def iter_LCP_ex(self, common_lcp):
        return
        yield common_lcp # the stmt should exist
    def verify(self, is_root, L):
        if is_root:
            return self.whole_isuffix == L == 0
        return 0 <= self.whole_isuffix <= L > 0

    def verify_with_array(self, array, common_lcp):
        return True
    def iter_suffices_ex(self, array, prefix):
        whole_suffix = array[self.whole_isuffix:]
        try:
            assert whole_suffix[:len(prefix)] == prefix
        except:
            old_print(whole_suffix[:len(prefix)], prefix)
            old_print(array, whole_suffix, self.whole_isuffix)
            raise
        yield whole_suffix
        return
        common_lcp = len(prefix)
        begin_isuffix = self.whole_isuffix + common_lcp
        yield array[begin_isuffix:]















def make_SuffixTreeRoot(SA, LCP):
    # -> (SuffixTreeLeaf | SuffixTreeNode)
    # -> root
    L = len(SA)
    if not len(LCP) == max(0, L-1): raise ValueError
    the_empty_leaf = SuffixTreeLeaf(L)
    if not SA:
        root = the_empty_leaf
        return root

    children_stack = [[the_empty_leaf]]
    children_min_LCP_stack = [0]
    ancestor_stack = []
        # right most open root
        # :: [(whole_isuffix, prev_LCP)]
        #   begin_isuffix == whole_isuffix+prev_LCP
    assert len(children_stack) == len(children_min_LCP_stack) == len(ancestor_stack) + 1

    def close():
        N = len(ancestor_stack)
        assert ancestor_stack
        assert len(children_stack) == N+1
        assert len(children_min_LCP_stack) == N+1
        show('close() :: begin')

        prev_isuffix, prev_prev_LCP = ancestor_stack.pop()
        prev_children_min_LCP = children_min_LCP_stack.pop()
        prev_children = children_stack.pop()
        assert prev_children
        if len(prev_children) == 1:
            # prev is leaf
            [prev_node] = prev_children
        else:
            prev_begin_isuffix0 = prev_isuffix + prev_prev_LCP
            prev_size0 = prev_children_min_LCP - prev_prev_LCP

            parent_children_min_LCP = children_min_LCP_stack[-1]
            prev_size1 = prev_children_min_LCP - parent_children_min_LCP
            prev_begin_isuffix1 = prev_isuffix + parent_children_min_LCP

            assert prev_begin_isuffix0 == prev_begin_isuffix1
            assert prev_size0 == prev_size1

            prev_node = SuffixTreeNode(prev_begin_isuffix0, prev_size0, prev_children)
        children_stack[-1].append(prev_node)

        show('close() :: end')
        return
    def put(isuffix, prev_LCP):
        # ancestor_stack may be empty
        N = len(ancestor_stack)
        #assert ancestor_stack
        assert len(children_stack) == N+1
        assert len(children_min_LCP_stack) == N+1
        show('put() :: begin')

        #bug:children_min_LCP_stack[-1] = min(children_min_LCP_stack[-1], prev_LCP)
        parent_child_min_LCP = children_min_LCP_stack[-1]
        if prev_LCP < parent_child_min_LCP:
            parent_isuffix, parent_prev_LCP = ancestor_stack[-1]
            ancestor_stack.append((parent_isuffix, prev_LCP))
            children_stack.insert(-1, [])
            children_min_LCP_stack.insert(-1, prev_LCP)
            close()
            parent_child_min_LCP = children_min_LCP_stack[-1]
        assert prev_LCP <= parent_child_min_LCP

        ancestor_stack.append((isuffix, prev_LCP))
        children_min_LCP_stack.append(L-isuffix)
        self_leaf = SuffixTreeLeaf(isuffix)
        children = [self_leaf]
        children_stack.append(children)

        show('put() :: end')
        return

    def show(s):
        if not TESTING: return
        print('\n')
        print(s)
        print(f'isuffix={isuffix}, prev_LCP={prev_LCP}')
        print(f'ancestor_stack={ancestor_stack}')
        print(f'children_min_LCP_stack={children_min_LCP_stack}')
        print(f'children_stack={children_stack}')

    isuffix, prev_LCP = SA[0], 0
    put(isuffix, prev_LCP)

    prev_prev_LCP = ancestor_stack[-1][-1]
    for isuffix, prev_LCP in zip(SA[1:], LCP):
        N = len(ancestor_stack)
        assert ancestor_stack
        assert len(children_stack) == N+1
        assert len(children_min_LCP_stack) == N+1
        assert prev_prev_LCP == ancestor_stack[-1][-1]

        while prev_prev_LCP > prev_LCP:
            # isuffix is uncle
            close()
            prev_prev_LCP = ancestor_stack[-1][-1]

        if prev_prev_LCP == prev_LCP:
            # prev_isuffix and isuffix is sibling
            close()
            put(isuffix, prev_LCP)
        else:
            # prev_prev_LCP < prev_LCP:
            # isuffix is child
            put(isuffix, prev_LCP)

        # next round
        prev_prev_LCP = prev_LCP

    while ancestor_stack:
        close()
    [root_children] = children_stack

    root = SuffixTreeNode(0, 0, root_children)
    return root


'''
    >>> this = make_SA_LCP
    >>> this(b'')
    ([], [])
    >>> this(b'231')
    ([2, 0, 1], [0, 0])
    >>> this([1,1,1,0])
    ([3, 2, 1, 0], [0, 1, 2])
    >>> this(b'112233112233')
    ([6, 0, 7, 1, 8, 2, 9, 3, 11, 5, 10, 4], [6, 1, 5, 0, 4, 1, 3, 0, 1, 1, 2])
    >>> this([1,1,1])
    ([2, 1, 0], [1, 2])

    >>> this(b'0120121')
    ([0, 3, 6, 1, 4, 2, 5], [3, 0, 1, 2, 0, 1])
    >>> this(b'100100100')
    ([8, 7, 4, 1, 5, 2, 6, 3, 0], [1, 2, 5, 1, 4, 0, 3, 6])
    >>> this(b'100100')
    ([5, 4, 1, 2, 3, 0], [1, 2, 1, 0, 3])


'''
class SuffixTree:
    r'''

example:
    >>> SuffixTree.from_uint_array(b'231', testing=True).to_data()
    (0, 0, [(3,), (2,), (0,), (1,)])
    >>> SuffixTree.from_uint_array(b'100', testing=True).to_data()
    (0, 0, [(3,), (2, 1, [(2,), (1,)]), (0,)])
    >>> SuffixTree.from_uint_array(b'\1\0\0', testing=True).to_data()
    (0, 0, [(3,), (2, 1, [(2,), (1,)]), (0,)])


    >>> this = lambda SA, LCP, array: SuffixTree(SA, LCP, testing=True, array=array).to_data()
    >>> this([], [], b'')
    (0,)
    >>> this([2, 0, 1], [0, 0], b'231')
    (0, 0, [(3,), (2,), (0,), (1,)])
    >>> this([3, 2, 1, 0], [0, 1, 2], b'1110')
    (0, 0, [(4,), (3,), (2, 1, [(2,), (2, 1, [(1,), (0,)])])])
    >>> this([6, 0, 7, 1, 8, 2, 9, 3, 11, 5, 10, 4], [6, 1, 5, 0, 4, 1, 3, 0, 1, 1, 2], b'112233112233')
    (0, 0, [(12,), (6, 1, [(7, 5, [(6,), (0,)]), (8, 4, [(7,), (1,)])]), (8, 1, [(9, 3, [(8,), (2,)]), (10, 2, [(9,), (3,)])]), (11, 1, [(11,), (5,), (11, 1, [(10,), (4,)])])])
    >>> this([2, 1, 0], [1, 2], b'111')
    (0, 0, [(3,), (2, 1, [(2,), (2, 1, [(1,), (0,)])])])
    >>> this([0, 3, 6, 1, 4, 2, 5], [3, 0, 1, 2, 0, 1], b'0120121')
    (0, 0, [(7,), (0, 3, [(0,), (3,)]), (6, 1, [(6,), (2, 1, [(1,), (4,)])]), (2, 1, [(2,), (5,)])])
    >>> this([8, 7, 4, 1, 5, 2, 6, 3, 0], [1, 2, 5, 1, 4, 0, 3, 6], b'100100100')
    (0, 0, [(9,), (8, 1, [(8,), (8, 1, [(7,), (6, 3, [(4,), (1,)])]), (6, 3, [(5,), (2,)])]), (6, 3, [(6,), (6, 3, [(3,), (0,)])])])
    >>> this([5, 4, 1, 2, 3, 0], [1, 2, 1, 0, 3], b'100100')
    (0, 0, [(6,), (5, 1, [(5,), (5, 1, [(4,), (1,)]), (2,)]), (3, 3, [(3,), (0,)])])

'''
    def __init__(self, SA, LCP, *, testing=False, array=None):
        root = make_SuffixTreeRoot(SA, LCP)
        self.root = root
        self.L = len(SA)
        #self.SA = tuple(SA)
        #self.LCP = tuple(LCP)
        if testing:
            assert self.test(SA, LCP, array)

    def test(self, SA, LCP, may_array):
        L = len(SA)
        [*SA_ex] = self.iter_SA_ex()
        [*LCP_ex] = self.iter_LCP_ex()
        assert len(SA_ex) == L+1
        assert len(LCP_ex) == L
        assert not L or LCP_ex[0] == 0

        if not SA_ex == [L, *SA]: return False
        print('here')

        print(LCP_ex, LCP)
        if L:
            print('here2')
            if not LCP_ex == [0, *LCP]: return False
        else:
            print('here3')
            if not LCP_ex == [*LCP]: return False

        print('here4')
        if may_array is not None:
            array = may_array
            if not self.verify_with_array(SA_ex, array):
                return False
        return True

    def iter_leaves(self):
        return self.root.iter_leaves()
    def verify_with_array(self, SA_ex, array):
        print('here5')
        if not self.root.verify_with_array(array, 0): return False
        print('here6')
        [*suffices_ex] = self.iter_suffices_ex(array)
        ans = [array[isuffix_ex:] for isuffix_ex in SA_ex]
        if not suffices_ex == ans:
            print(suffices_ex)
            print(ans)
            return False
        return True
    def verify(self):
        return self.root.verify(True, self.L)
    def iter_SA_ex(self):
        leaves = self.iter_leaves()
        return (leaf.whole_isuffix for leaf in leaves)
    def iter_LCP_ex(self):
        return self.root.iter_LCP_ex(0)
    def iter_suffices_ex(self, array):
        return self.root.iter_suffices_ex(array, array[0:0])

    @classmethod
    def from_SA_LCP(cls, SA, LCP, *, testing=False, array=None):
        return cls(SA, LCP, testing=testing, array=array)
    @classmethod
    def from_uint_array(cls, array, *, make_SA_LCP=None, testing=False):
        if make_SA_LCP is None:
            make_SA_LCP = sa_lcp_from_array
        SA, LCP = make_SA_LCP(array)
        return cls.from_SA_LCP(SA, LCP, testing=testing, array=array)

    def __str__(self):
        return '<{}({}, {})>'.format(type(self).__name__, self.L, self.root)
        return str(self.root)

    def to_data(self):
        '''data = (whole_isuffix,) | (begin_isuffix, size, [data])
'''
        return self.root.to_data()


def _t():
    this = lambda SA, LCP, array: SuffixTree(SA, LCP, testing=True, array=array).to_data()
    r = this([2,1,0], [1,0], b'100')
    assert r == (0, 0, [(3,), (2, 1, [(2,), (1,)]), (0,)])
    print(r)

    r = this([6, 0, 7, 1, 8, 2, 9, 3, 11, 5, 10, 4], [6, 1, 5, 0, 4, 1, 3, 0, 1, 1, 2], b'112233112233')
    assert r == (0, 0, [(12,), (6, 1, [(7, 5, [(6,), (0,)]), (8, 4, [(7,), (1,)])]), (8, 1, [(9, 3, [(8,), (2,)]), (10, 2, [(9,), (3,)])]), (11, 1, [(11,), (5,), (11, 1, [(10,)
, (4,)])])])
    r = this([3, 2, 1, 0], [0, 1, 2], b'1110')
    assert r == (0, 0, [(4,), (3,), (2, 1, [(2,), (2, 1, [(1,), (0,)])])])


assert sa_lcp_from_array(b'100') == sa_lcp_from_array([1,0,0]) == sa_lcp_from_array(b'\1\0\0')
#old_print(sa_lcp_from_array(b'100'))
r = SuffixTree.from_uint_array(b'\1\0\0', testing=True).to_data()
assert r == (0, 0, [(3,), (2, 1, [(2,), (1,)]), (0,)])

SuffixTree.from_uint_array([1,0,0], testing=True)

if __name__ == "__main__":
    print = old_print
    TESTING = True
    _t()
if __name__ == "__main__":
    print = new_print
    TESTING = False
    import doctest
    doctest.testmod()



