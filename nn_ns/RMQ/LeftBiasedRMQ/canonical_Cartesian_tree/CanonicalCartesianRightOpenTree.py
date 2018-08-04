'''
see: canonical_Cartesian_tree_definition
'''

__all__ = '''
    CanonicalCartesianRightOpenTree
    canonical_Cartesian_tree__via_CanonicalCartesianRightOpenTree
    '''.split()

from .canonical_Cartesian_tree_definition import canonical_Cartesian_tree_definition



class CanonicalCartesianRightOpenTree:
    '''CanonicalCartesianRightOpenTree

current global root may become a left_child_root
left_child_trees are closed/final
right_child_trees are open
    right_child_root may become a left_child_root
    i.e. may change parent
    when a new element x comes:
        we find parent p of x
        and then insert x into p and p.right_child
            x.left_child := p.right_child
            x.left_child.parent := x
            p.right_child := x
            p.right_child.parent := p

# if the offset is 0, then is CanonicalCartesianRightOpenTree
OffsetCanonicalCartesianRightOpenTree
    = EmptyOCCROTree
    | NonEmptyOCCROTree
            {root :: uint
            # root < left_child_node
            # root <= right_child_node
            ,left_child_tree :: OffsetCanonicalCartesianTree
            ,right_child_tree :: OffsetCanonicalCartesianRightOpenTree
            }

OffsetCanonicalCartesianTree
    = EmptyOCCTree
    | NonEmptyOCCTree
            {root :: uint
            # root < left_child_node
            # root <= right_child_node
            ,left_child_tree :: OffsetCanonicalCartesianTree
            ,right_child_tree :: OffsetCanonicalCartesianTree
            }



'''
    def __init__(self, iterable=()):
        self.v2may_parent = []
        self.v2may_left = []
        self.v2may_right = []
        self.may_root = None
        #self.right_roots = [] # == [root, root.right, root.right.right, ...]
        #self.may_right_most = None == len(array)-1
        self.array = []

        self.feeds(iterable)

    def to_concept_canonical_Cartesian_tree(self):
        return self.may_root, self.v2may_parent, self.v2may_left, self.v2may_right
    @property
    def may_right_most(self):
        may_right_most = len(self.array)-1
        if may_right_most == -1:
            return None
        return may_right_most

    def __find_may_parent_of_x(self, x):
        # :: element -> Maybe UInt

        array = self.array
        v2may_parent = self.v2may_parent
        may_parent = self.may_right_most
        while may_parent is not None:
            parent = may_parent
            parent_element = array[parent]
            if parent_element <= x: break
            may_parent = v2may_parent[parent]
        return may_parent


    def feed(self, x):
        array = self.array
        v = idx_of_x = len(array)

        # right_most := v
        # v.right := None
        # v.parent := parent
        # v.left := parent.right or root
        # may: parent.right.parent := v
        # may: parent.right := v
        # may: root := v
        # array[v] := x

        may_parent = self.__find_may_parent_of_x(x)
        #self.may_right_most = v
        self.v2may_right.append(None)
        self.v2may_parent.append(may_parent) # v -> may_parent

        if may_parent is None:
            # v/x be new global root
            may_left_child_of_x = self.may_root
            self.may_root = v
        else:
            parent = may_parent
            may_right_child_of_parent = self.v2may_right[parent]

            may_left_child_of_x = may_right_child_of_parent
            self.v2may_right[parent] = v

        self.v2may_left.append(may_left_child_of_x)
        if may_left_child_of_x is not None:
            left_child_of_x = may_left_child_of_x
            self.v2may_parent[left_child_of_x] = v

        array.append(x)
    def feeds(self, iterable):
        for x in iterable:
            self.feed(x)

def canonical_Cartesian_tree__via_CanonicalCartesianRightOpenTree(iterable):
    '''see: canonical_Cartesian_tree_definition, but O(n)'''
    t = CanonicalCartesianRightOpenTree(iterable)
    return t.to_concept_canonical_Cartesian_tree()


