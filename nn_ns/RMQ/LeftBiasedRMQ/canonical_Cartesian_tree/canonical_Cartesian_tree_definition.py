'''
Canonical Cartesian Tree of array A[0:L]
    # "Canonical" means "leftmost"  (min element) be root
    empty_tree if len(A) == 0
    root = min A.index(min(A)) # leftmost root_idx
        if no Canonical: root = arbitrary A.index(min(A))
    assert all(A[root] < x for x in A[:i])
    assert all(A[root] <= x for x in A[i+1:])

    left_child_tree = Canonical Cartesian Tree of A[0:i]
    right_child_tree = Canonical Cartesian Tree of A[i+1:L]

Free Canonical Cartesian Tree of array A[0:L]
    # "Canonical" means "leftmost"  (min element) be root
    # "Free" means donot hold the index, but the element directly

Canonical Cartesian Right Open Tree of array A[0:L]
    # "Canonical" means "leftmost"  (min element) be root
    # "Right Open" means may insert vertex between parent and its right_child
    #       and the right_child become left_child of new parent
    #       but all left_child_trees are closed
    #       i.e.
    #           new_parent.left_child := old_parent.right_child
    #           new_parent.left_child.parent := new_parent
    #           old_parent.right_child := new_parent
    #           old_parent.right_child.parent := old_parent
    #   assume there is a virtual root: vroot; which has -inf element
    #       if curr tree is empty: pass
    #       else:
    #           vroot.right_child is curr_global_root
    #       let p=vroot.right_child*
    #       let rc = p.right_child
    #       then in final tree, rc is p.right_child.left_child*
    #       tree edges other than vroot.right_child*->vroot.right_child*
    #           will not change in final tree!!


'''


__all__ = '''
    canonical_Cartesian_tree_definition
    '''.split()


def canonical_Cartesian_tree_definition(array):
    '''canonical_Cartesian_tree_definition
        :: Ord a => [a] -> (may_root, v2may_parent, v2may_left, v2may_right)
        # may_root :: None | uint
        # v2xxx :: [(None|uint)]
        # len(v2xxx) == len(input_array)

definition; very slow; O(n^2); used for testing
use canonical_Cartesian_tree instead

input:
    array :: Ord a => [a]
output:
    Cartesian_tree =[concept]= partial-oriented-rooted-binary-tree
        # 'partial' means PORBT_nonleaf_node have 1 or 2 children
        # allow empty tree!!!!!!
        # see: Catalan_number.py :: PORBT for detail
        #   num_PORBT(n) = Catalan_number(n) for n>=0

        let L = len(array)
        # all leaf vertices has same repr: None
        tree_nonleaf_vertex :: uint
        tree_nonleaf_vertex <- [0..L]
            root means the root vertex
                i.e. the array index of the root element
    Cartesian_tree =[repr]= (may_root, v2may_parent, v2may_left, v2may_right)
        root is a tree_nonleaf_vertex
        may_root = None | root
        v2may_parent :: [(None|nonleaf_vertex)]
            v2may_parent[v] is None <==> v == may_root is not None
        v2may_left = [(None|nonleaf_vertex)]
        v2may_right = [(None|nonleaf_vertex)]
        len(v2may_parent) == len(v2may_left) == len(v2may_right) == L
'''
    L = len(array)
    v2may_parent = [None] * L
    v2may_left = [None] * L
    v2may_right = [None] * L

    may_root = __canonical_Cartesian_tree_definition_impl(
            array, v2may_parent, v2may_left, v2may_right, begin=0, end=len(array))
    return may_root, v2may_parent, v2may_left, v2may_right

def __canonical_Cartesian_tree_definition_impl(
        array, v2may_parent, v2may_left, v2may_right, begin, end):
    # O(n^2)

    def set_parent_child(root, may_child_root):
        if may_child_root is None:
            return
        child_root = may_child_root
        v2child = v2may_left if child_root < root else v2may_right
        v2child[root] = child_root
        v2may_parent[child_root] = root

    def this_func(begin, end):
        # -> may_root

        L = end - begin
        assert L >= 0
        if not L:
            may_root = None
        else:
            root = array.index(min(array[begin:end]), begin, end) # O(n)

            may_left_child_root = this_func(begin, root)
            may_right_child_root = this_func(root+1, end)
            set_parent_child(root, may_left_child_root)
            set_parent_child(root, may_right_child_root)
            may_root = root
        return may_root

    may_root = this_func(begin, end)
    return may_root


