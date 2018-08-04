
'''
Canonical Cartesian Tree of array A[0:L]

empty_tree if len(A) == 0
root = min A.index(min(A))
assert all(A[root] < x for x in A[:i])
assert all(A[root] <= x for x in A[i+1:])

left_child_tree = Canonical Cartesian Tree of A[0:i]
right_child_tree = Canonical Cartesian Tree of A[i+1:L]
'''

'''
Number of Binary Tree of order n
N(n) = 1 for n = 0, 1
N(n+1) = sum(N(i)*N(n-i) for i in [0,n])
error: N(n) =?= n! (imagine [1..n] -> Cartesian Tree; and any binary tree can be labelled like this, too)
tree: [2 1 3] and [3 1 2] one tree count twice

N(n) =?= C(2n, n)/(n+1) # Catalan Number

'''

import itertools
import random

debug = 1

def canonical_Cartesian_tree_definition(array):
    L = len(array)
    v2parent = [None] * L
    v2left = [None] * L
    v2right = [None] * L
    
    canonical_Cartesian_tree_definition_impl(array, 
                                           v2parent, v2left, v2right,
                                           begin=0, end=len(array))
    roots = [v for v, parent in enumerate(v2parent) if parent is None]
    assert len(roots) < 2
    return roots, v2parent, v2left, v2right

def canonical_Cartesian_tree_definition_impl(array, 
                                           v2parent, v2left, v2right,
                                           begin, end,
                                           super_root=None, v2child=None):
    L = end - begin
    assert L >= 0
    
    if not L:
        return
    
    root = array.index(min(array[begin:end]), begin, end)
    if super_root != None:
        v2child[super_root] = root
        v2parent[root] = super_root
        

    canonical_Cartesian_tree_definition_impl(array,
                                           v2parent, v2left, v2right,
                                           begin, root,
                                           root, v2left)

    canonical_Cartesian_tree_definition_impl(array,
                                           v2parent, v2left, v2right,
                                           root+1, end,
                                           root, v2right)
    
    
                       
def canonical_Cartesian_tree(array):
    L = len(array)
    v2parent = [None] * L
    v2left = [None] * L
    v2right = [None] * L
    right_open_tree_roots = []

    def set_child(parent, child, v2lr):
        v2lr[parent] = child
        v2parent[child] = parent
    def set_left_child(parent, child):
        set_child(parent, child, v2left)
    def set_right_child(parent, child):
        set_child(parent, child, v2right)

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
                
    def merge_right_open_trees(roots):
        while len(roots) > 1:
            root = roots.pop()
            set_right_child(roots[-1], root)
        return roots
    
    for v, x in enumerate(array):
        begin = find_left_child_begin(x)
        roots = right_open_tree_roots[begin:]
        del right_open_tree_roots[begin:]
        roots = merge_right_open_trees(roots)
        if roots:
            left, = roots
            set_left_child(v, left)
        right_open_tree_roots.append(v)

    roots = merge_right_open_trees(right_open_tree_roots)
    assert 0 <= len(roots) <= 1
    assert len(array) == 0 or v2parent.count(None) == 1
    assert not roots or roots[0] == v2parent.index(None)
##    if debug and roots:
##        root, = roots
##        counts = [0] * L
##        for v in itertools.chain(v2left, v2right):
##            if v is not None:
##                counts[v] += 1
##        assert all(c == 1 or (c == 0 and v == root) for v, c in enumerate(counts))
        
    return roots, v2parent, v2left, v2right


def test_canonical_Cartesian_tree():
    from itertools import chain, product
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


















        
        
