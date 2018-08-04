
'''
see: canonical_Cartesian_tree_definition
'''

__all__ = '''
    canonical_Cartesian_tree
    '''.split()

from .canonical_Cartesian_tree_definition import canonical_Cartesian_tree_definition


def canonical_Cartesian_tree(array):
    ''':: Ord a => [a] -> (may_root, v2may_parent, v2may_left, v2may_right)

what?
    see: canonical_Cartesian_tree_definition
input and output:
    see: canonical_Cartesian_tree_definition

let L = len(array)
time and space
    time O(L)*(a.'<' + uint[..L].'+-')
    space O(L*log2(L))*bit
        # array<uint[0..L-1], L>
        for both space(output) and working space

'''
    L = len(array)
    # time O(L)*ops
    # space O(L*log2(L))*bit # list<uint[0..L-1]>
    v2may_parent = [None] * L
    v2may_left = [None] * L
    v2may_right = [None] * L
    right_open_tree_roots = []

    # time O(1)*ops
    def set_child(parent, child, v2lr):
        v2lr[parent] = child
        v2may_parent[child] = parent
    def set_left_child(parent, child):
        set_child(parent, child, v2may_left)
    def set_right_child(parent, child):
        set_child(parent, child, v2may_right)

    # time O(len(right_open_tree_roots)-result)*(a.'<' + uint[..L].'+-')
    def find_left_child_begin(x):
        L = len(right_open_tree_roots)
        i = 0
        for i in reversed(range(L)):
            root_idx = right_open_tree_roots[i]
            if not x < array[root_idx]:
                i += 1
                break

        assert i == L or x < array[right_open_tree_roots[i]]
        assert i == 0 or not x < array[right_open_tree_roots[i-1]]
        return i

    # time O(len(sink_roots))*ops
    def merge_right_open_trees(sink_roots):
        # sink means will modify roots
        # [root] -> may_root
        roots = sink_roots
        if not roots:
            root = None
            return root

        root = roots.pop()
        while roots:
            right = root
            root = roots.pop()
            set_right_child(root, right) # right cannot be None
        return root

    # total time O(L)*(a.'<' + uint[..L].'+-')
    for v, x in enumerate(array):
        # time O(len(right_open_tree_roots)-begin)*(a.'<' + uint[..L].'+-')
        begin = find_left_child_begin(x)

        # time O(len(right_open_tree_roots)-begin)*ops
        roots = right_open_tree_roots[begin:]
        del right_open_tree_roots[begin:]
        may_root = merge_right_open_trees(roots); del roots

        # time O(1)*ops
        if may_root is not None:
            left = may_root
            set_left_child(v, left)
        right_open_tree_roots.append(v)

    may_root = merge_right_open_trees(right_open_tree_roots); del right_open_tree_roots
    assert len(array) == 0 or v2may_parent.count(None) == 1
    assert may_root is None or may_root == v2may_parent.index(None)

    return may_root, v2may_parent, v2may_left, v2may_right
canonical_Cartesian_tree.__doc__ += canonical_Cartesian_tree_definition.__doc__

def test_canonical_Cartesian_tree():
    from itertools import chain, product
    import random
    data = [
        [],
        ]\
        + [[random.randint(0, 10) for _ in range(9)] for _ in range(100)]

    data.extend(chain.from_iterable(product(range(3), repeat=r)
                                    for r in range(4)))

    for array in data:
        array = list(array)
        #print(array)
        assert canonical_Cartesian_tree(array) == canonical_Cartesian_tree_definition(array)

test_canonical_Cartesian_tree()


