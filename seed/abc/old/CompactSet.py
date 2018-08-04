
'''
e.g.
    element::Int
    block::(begin::Int, end::Int)
    CompactOrdSet::[block::(Int, Int)]
    
'''

from seed.types.ABC import *

class CompactSet(ABC):
    @not_implemented
    def __contains__(self, element):...
    @not_implemented
    def iter_blocks(self):...
    @not_implemented
    def __or__(self, other):...
    @not_implemented
    def __and__(self, other):...
    @not_implemented
    def __sub__(self, other):...


from seed.types.RedBlackTree.RedBlackTreeNodeABC import \
     RBT_Node_TupleBothPlainParented_ABC,\
     RBT_Node_Bool_Constants_ABC
from seed.types.RedBlackTree.OrderedMutableRedBlackTreeNodeABC import \
     OrderedMutableRedBlackTreeNodeABC
from seed.helper.repr_input import repr_helper


class _Node(
    RBT_Node_Bool_Constants_ABC,
    RBT_Node_TupleBothPlainParented_ABC,
    OrderedMutableRedBlackTreeNodeABC):
    PLAIN_LEAF = ()
    ROOT_PARENT_INFO = None
    @property
    def key(self):
        return type(self).entity2key(self.entity)
    
class CompactOrdSet(CompactSet):
    # RBT<Range>; range = [begin, end)
    __RBT_Node__ = _Node

    def __init__(self, iterable):
        Node = type(self).__RBT_Node__
        self.__root = Node
        self.__update(iterable)
        
    def __contains__(self, element):
        key = rng = (element, element)
        leaf = self.__root.subtree_find_end_leaf(key)
        try:
            nonleaf = leaf.leaf_inorder_succ_nonleaf()
        except StopIteration:
            return False
        e0, e1 = nonleaf.key
        assert nonleaf.key_lt(e0, e1)
        return nonleaf.key_eq(e0, element)
        
    def iter_blocks(self):
        return map(type(self).entity2key, self.iter_entities())
    @not_implemented
    def __or__(self, other):...
    @not_implemented
    def __and__(self, other):...
    @not_implemented
    def __sub__(self, other):...
        




