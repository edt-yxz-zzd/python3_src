from .TreeNodeABC import TreeNodeABC
from seed.types import not_implemented

class TreeIteratorComparableTreeNodeABC(TreeNodeABC):
    # is in same position in same tree?
    # precondition:
    #     self, other are in same tree
    #     e.g. if we know node is i-th node of a tree
    #          then we simply compare node order number
    #          but that will cause bug if not in same tree
    def is_same_position__BigO_depth(self, other):
        while self.is_nonroot() and other.is_nonroot():
            if bool(self.is_left()) != bool(other.is_left()):
                return False
            self = self.parent
            other = other.parent
        return self.is_root() and other.is_root()
    def is_same_position__fastest(self, other):
        return self.is_same_position__BigO_depth(other)

class TreeIteratorComparableFastTreeNodeABC(TreeIteratorComparableTreeNodeABC):
    @not_implemented
    def is_same_position__BigO_1(self, other):...
    def is_same_position__fastest(self, other):
        return self.is_same_position__BigO_1(other)
