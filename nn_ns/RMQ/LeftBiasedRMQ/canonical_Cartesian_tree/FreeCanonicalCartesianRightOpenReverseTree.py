
'''
see: canonical_Cartesian_tree_definition
'''

__all__ = '''
    canonical_Cartesian_tree__via_FreeCanonicalCartesianRightOpenReverseTree
    FreeCanonicalCartesianRightOpenReverseTree



    FreeCanonicalCartesianTree
    to_concept_canonical_Cartesian_tree

    emptyFreeCanonicalCartesianRightOpenReverseTree
    emptyFreeCanonicalCartesianTree
    '''.split()

from .canonical_Cartesian_tree_definition import canonical_Cartesian_tree_definition








from collections import namedtuple

FreeCanonicalCartesianTreeBase = namedtuple(
        'FreeCanonicalCartesianTreeBase'
        , 'root_element left_child_tree right_child_tree'.split())
FreeCanonicalCartesianRightOpenReverseTreeBase = namedtuple(
        'FreeCanonicalCartesianRightOpenReverseTreeBase'
        , 'root_element parent_tree left_child_tree'.split())

def isFreeCanonicalCartesianTree(obj):
    return isinstance(obj, FreeCanonicalCartesianTree)
def isFreeCanonicalCartesianRightOpenReverseTree(obj):
    return isinstance(obj, FreeCanonicalCartesianRightOpenReverseTree)
class FreeCanonicalCartesianTree(FreeCanonicalCartesianTreeBase):
    '''FreeCanonicalCartesianTree

immutable
# Free means donot consider abs position in array
# Canonical means "leftmost"  (min element) be root

Ord a => FreeCanonicalCartesianTree a
    = EmptyFCCTree
    | NonEmptyFCCTree
        {root_element :: a
        # root_element < left_child_node
        # root_element <= right_child_node
        ,left_child_tree :: FreeCanonicalCartesianTree a
        ,right_child_tree :: FreeCanonicalCartesianTree a
        }
see: FreeCanonicalCartesianRightOpenReverseTree


EmptyFCCTree = FreeCanonicalCartesianTree(None, None, None)
'''
    __slots__ = ()
    def __new__(cls, root_element, left_child_tree, right_child_tree):
        if root_element is left_child_tree is right_child_tree is None:
            pass
        elif not isFreeCanonicalCartesianTree(left_child_tree): raise TypeError
        elif not isFreeCanonicalCartesianTree(right_child_tree): raise TypeError
        elif not (left_child_tree.is_empty() or root_element < left_child_tree.root_element): raise ValueError
        elif not (right_child_tree.is_empty() or root_element <= right_child_tree.root_element): raise ValueError

        self = super(__class__, cls).__new__(
                cls, root_element, left_child_tree, right_child_tree)
        return self
    def is_empty(self):
        return self.left_child_tree is None
    def get_empty_tree(self):
        return emptyFreeCanonicalCartesianTree
emptyFreeCanonicalCartesianTree = \
    FreeCanonicalCartesianTree(None, None, None)

class FreeCanonicalCartesianRightOpenReverseTree(
        FreeCanonicalCartesianRightOpenReverseTreeBase):
    '''FreeCanonicalCartesianRightOpenReverseTree

immutable
# Free means donot consider abs position in array
# Canonical means "leftmost"  (min element) be root

Ord a => FreeCanonicalCartesianRightOpenReverseTree a
    = EmptyFCCRORTree
    | NonEmptyFCCRORTree
            {root_element :: a
            # assume root_element is array[i]
            # then this tree repr Cartesian_tree of array[:i+1]
            #   i.e. root_element is the last element

            # parent_tree.root_element <= root_element
            , parent_tree :: FreeCanonicalCartesianRightOpenReverseTree a
            # root_element < left_child_node
            ,left_child_tree :: FreeCanonicalCartesianTree a
            }
see: FreeCanonicalCartesianTree

EmptyFCCRORTree = FreeCanonicalCartesianRightOpenReverseTree(None, None, None)
'''
    __slots__ = ()
    def __new__(cls, root_element, parent_tree, left_child_tree):
        if root_element is left_child_tree is parent_tree is None:
            pass
        elif not isFreeCanonicalCartesianRightOpenReverseTree(parent_tree): raise TypeError
        elif not isFreeCanonicalCartesianTree(left_child_tree): raise TypeError
        elif not (parent_tree.is_empty() or parent_tree.root_element <= root_element): raise ValueError
        elif not (left_child_tree.is_empty() or root_element < left_child_tree.root_element): raise ValueError

        self = super(__class__, cls).__new__(
                cls, root_element, parent_tree, left_child_tree)
        return self
    def is_empty(self):
        return self.left_child_tree is None

    def ifeeds(self, iterable):
        for x in iterable:
            self = self.ifeed(x)
        return self
    def ifeed(self, x):
        '''
        if self.is_empty():
            return __class__(
                x, emptyFreeCanonicalCartesianRightOpenReverseTree
                , emptyFreeCanonicalCartesianTree)
        '''

        right_most = self
        left_child_of_x = emptyFreeCanonicalCartesianTree
        while not right_most.is_empty() and x < right_most.root_element:
            # right_most become left_child_of_x

            right_child_of_left_child_of_x = left_child_of_x
            # left_child_of_x = right_most
            left_child_of_x = FreeCanonicalCartesianTree(
                right_most.root_element
                , right_most.left_child_tree
                , right_child_of_left_child_of_x)
            right_most = right_most.parent_tree
        # right_most.is_empty() or right_most.root_element <= x
        return __class__(x, right_most, left_child_of_x)

    def to_concept_canonical_Cartesian_tree(self):
        t = self.to_FreeCanonicalCartesianTree()
        return to_concept_canonical_Cartesian_tree(t)
    def to_FreeCanonicalCartesianTree(self):
        right_most = self
        result_tree = emptyFreeCanonicalCartesianTree
        while not right_most.is_empty():
            result_tree = FreeCanonicalCartesianTree(
                right_most.root_element
                , right_most.left_child_tree
                , result_tree
                )
            right_most = right_most.parent_tree
        return result_tree

    def get_empty_tree(self):
        return emptyFreeCanonicalCartesianRightOpenReverseTree
emptyFreeCanonicalCartesianRightOpenReverseTree = \
    FreeCanonicalCartesianRightOpenReverseTree(None, None, None)


def to_concept_canonical_Cartesian_tree(self):
    assert isFreeCanonicalCartesianTree(self)
    v2may_parent = []
    v2may_left = []
    v2may_right = []
    def handle_left_child(tree, offset_begin):
        # -> (offset_end, may_local_root)
        # parent == offset_end # maybe beyond the allow range
        # precondition:
        #   len(v2may_parent) == len(v2may_left) == len(v2may_right) == offset_begin
        #   v2may_parent contains many None
        # postcondition:
        #   len(v2may_parent) == len(v2may_left) == len(v2may_right) == offset_end
        #   v2may_parent[left_child_root] == parent # may change to None
        #   v2may_parent contains many None
        if tree.is_empty():
            offset_end = offset_begin
            may_local_root = None
        else:
            local_root, may_left_child_root = handle_left_child(tree.left_child_tree, offset_begin)
            v2may_parent.append(None)
            v2may_left.append(may_left_child_root)
            v2may_right.append(None) # to be modified
            offset_end = handle_right_child(tree.right_child_tree, local_root+1)
            parent = offset_end
            v2may_parent[local_root] = parent # may beyond
            may_local_root = local_root
        return offset_end, may_local_root
    def handle_right_child(tree, offset_begin):
        # -> offset_end
        # offset_end = offset_begin + size(tree)
        # parent == offset_begin-1 >= 0
        # precondition:
        #   len(v2may_parent) == len(v2may_left) == len(v2may_right) == offset_begin
        #   v2may_parent contains many None
        #   v2may_right[parent] is None
        # postcondition:
        #   len(v2may_parent) == len(v2may_left) == len(v2may_right) == offset_end
        #   v2may_parent contains many None
        #   update v2may_right[parent]
        parent = offset_begin-1
        assert parent >= 0
        #v2may_right.append(None)
        if tree.is_empty():
            offset_end = offset_begin
            #v2may_right[parent] = None
        else:
            (local_root, may_left_child_root) = handle_left_child(tree.left_child_tree, offset_begin)
            v2may_right[parent] = local_root
            v2may_parent.append(parent)
            v2may_left.append(may_left_child_root)
            v2may_right.append(None) # to be modified
            offset_end = handle_right_child(tree.right_child_tree, local_root+1)
        return offset_end

    size, may_root = handle_left_child(self, 0)
    if may_root is not None:
        root = may_root
        v2may_parent[root] = None
    return may_root, v2may_parent, v2may_left, v2may_right
def canonical_Cartesian_tree__via_FreeCanonicalCartesianRightOpenReverseTree(iterable):
    '''see: canonical_Cartesian_tree_definition, but O(n)'''

    t = emptyFreeCanonicalCartesianRightOpenReverseTree.ifeeds(iterable)
    return t.to_concept_canonical_Cartesian_tree()
















