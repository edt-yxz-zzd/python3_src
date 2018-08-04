
'''
store form:
    PNode = ImmutableRedBlackTreeNode
    PNode a = Leaf | (color, a, (PNode a), (PNode a), size)
    why size?
        to support O(1) fixed_node_eq
        size ==>> pos_in_tree
extract form:
    ENode a = (Node a, pos_in_tree, Direction, ENode a) | (Node a, pos_in_tree)


size[node]:
    how many nonleaf node in subtree rooted by node
    size[leaf] = 0
    size[nonleaf] = 1 + size[nonleaf.left] + size[nonleaf.right]
    size_include_leaves[node] = size[node]*2 + 1
pos_in_tree[node]:
    how many nodes (include both leaf/nonleaf) before node in inorder?

    pos_in_tree[leaf_root] = 0
    pos_in_tree[nonleaf_root] = size_include_leaves[me.left]
                              = size[me.left]*2 + 1
    pos_in_tree[nonroot_left_leaf] = pos_in_tree[me.parent]-1
    pos_in_tree[nonroot_right_leaf] = pos_in_tree[me.parent]+1
    pos_in_tree[nonroot_left_nonleaf] = pos_in_tree[me.parent]
                                        - size_include_leaves[me]
                                        + size_include_leaves[me.left]
    pos_in_tree[nonroot_right_nonleaf] = pos_in_tree[me.parent] + 1
                                        + size_include_leaves[me.left]
    pos_in_tree[me] = [nonroot me] * pos_in_tree[me.parent]
                    - [left    me] * size_include_leaves[me]
                    + [right   me]
                    + [nonleaf me] * size_include_leaves[me.left]

to_depth(root) = 0



'''

from .RedBlackTreeOpsABC import RedBlackTreeOps



class Leaf: pass
class Left: pass
class Right:pass
class Red: pass
class Black: pass

leaf_root = Leaf, 0

def is_leaf(node):
    return plain_is_leaf(to_plain(node))
def is_root(node):
    return len(node) == 2
def is_left(nonroot_node):
    return to_direction(nonroot_node) is Left

def to_plain(node):
    return node[0]
def to_pos(node):
    return nonroot[1]
def to_direction(nonroot):
    return nonroot[2]
def to_parent(nonroot):
    return nonroot[3]


def plain_is_leaf(plain_node):
    return plain_node is Leaf
def plain_to_color(plain_nonleaf):
    return plain_nonleaf[0]
def plain_to_entity(plain_nonleaf):
    return plain_nonleaf[1]
def plain_to_left(plain_nonleaf):
    return plain_nonleaf[2]
def plain_to_right(plain_nonleaf):
    return plain_nonleaf[3]
def plain_to_size(plain_nonleaf):
    return plain_nonleaf[4]
def plain_to_size_include_leaves(plain_node):
    return plain_to_size(plain_nonleaf)*2+1 if not plain_is_leaf(plain_node) else 1


def make_plain_node(color, entity, plain_left, plain_right):
    size = plain_to_size(plain_left) + 1 + plain_to_size(plain_right)
    return color, entity, plain_left, plain_right, size

def to_left(nonleaf):
    me = nonleaf
    plain_me = to_plain(me)
    plain_left = plain_to_left(plain_me)
    pos = to_pos(me)
    left_begin_pos = pos - plain_to_size_include_leaves(plain_left)
    if not plain_is_leaf(plain_left):
        left_pos = left_begin_pos + plain_to_size_include_leaves(plain_to_left(plain_left))
    else:
        left_pos = left_begin_pos
    return plain_left, left_pos, Left, me
def to_right(nonleaf):
    me = nonleaf
    plain_me = to_plain(me)
    plain_right = plain_to_right(plain_me)
    pos = to_pos(me)
    right_begin_pos = pos + 1
    if not plain_is_leaf(plain_right):
        right_pos = right_begin_pos + plain_to_size_include_leaves(plain_to_left(plain_right))
    else:
        right_pos = right_begin_pos
    return plain_left, right_pos, Right, me







def to_size(node):
    return 0 if is_leaf(node) else plain_to_size(to_plain(node))
def to_size_include_leaves(node):
    return 2*to_size(node) + 1
def calc_nonleaf_size(left, right):
    return to_size(left) + to_size(right) + 1
    
    


class ImmutableRedBlackTreeOps(RedBlackTree):
    @abstractmethod
    def key_lt(self, key1, key2):
        raise NotImplementedError
    @abstractmethod
    def to_key(self, entity): # no to_value
        raise NotImplementedError



    def fixed_node_eq(self, fixed_node1, fixed_node2):
        'NOTE: a plain node may be shared in different trees/subtrees'
        # O(1)
        pos1, pos2 = map(to_pos, [fixed_node1, fixed_node2])
        if pos1 is None or pos2 is None:
            raise ValueError('not fixed node')
        return pos1 == pos2
    
        while True:
            if fixed_node1 is fixed_node2:
                return True
            b1 = self.is_root(fixed_node1)
            b2 = self.is_root(fixed_node2)
            if b1 or b2:
                break

            if to_direction(fixed_node1) != to_direction(fixed_node2):
                return False
            fixed_node1, fixed_node2 = map(to_parent, [fixed_node1, fixed_node2])
        if b1 and b2:
            raise ValueError('two different trees!!')
        return False
    
    def is_leaf(self, node):
        return is_leaf(node)



    # property
    LEFT = Left
    RIGHT = Right
    RED = Red
    BLACK = Black
    
    def to_color(self, nonleaf_node):
        return to_color(nonleaf_node)
    def to_entity(self, nonleaf_node):
        'undefined behavior if me is leaf'
        return to_entity(nonleaf_node)
    def to_left(self, nonleaf_node):
        return to_left(nonleaf_node)
    def to_right(self, nonleaf_node):
        return to_right(nonleaf_node)
        

    
    def is_root(self, node):
        return is_root(node)
    
    def is_left(self, nonroot_node):
        return is_left(nonroot_node)
    def unsafe_to_parent(self, nonroot_node):
        return to_parent(nonroot_node)
    
    def unsafe_replace_to_broken_node(self, node:'destroy',
                                      color, entity,
                                      left:'destroy', right:'destroy'):
        'when modifying, donot access .pos_in_tree'
        
        plain_left = to_plain(left)
        plain_right = to_plain(right)
        plain_node = make_plain_node(color, entity, plain_left, plain_right)
        return plain_node, None, to_direction(node), to_parent(node)
    
    def make_new_leaf_root(self):
        return leaf_root



class DirectImmutableRedBlackTreeOps(ImmutableRedBlackTreeOps):
    def key_lt(self, key1, key2):
        return key1 < key2
    def to_key(self, entity):
        return entity



def test_DirectImmutableRedBlackTreeOps():
    ops = DirectImmutableRedBlackTreeOps()

    
