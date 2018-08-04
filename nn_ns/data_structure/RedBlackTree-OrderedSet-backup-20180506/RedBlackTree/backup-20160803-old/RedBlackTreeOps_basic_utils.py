

from .RedBlackTreeOpsABC import RedBlackTreeOpsABC

################  query  ##################

def is_black(self, node):
    return self.is_leaf(node) or self.to_color(node) == self.BLACK
def is_red(self, node):
    return not is_black(self, node)

def extract_nonleaf_args(self, node):
    assert not self.is_leaf(node)
    
    color = self.to_color(node)
    entity = self.to_entity(node)
    left, right = to_children(self, node)
    return color, entity, left, right


def color_to_other_color(self, color):
    return self.BLACK if color == self.RED else self.RED
def to_other_color(self, nonleaf):
    return color_to_other_color(self, self.to_color(nonleaf))


def to_direction(self, nonroot):
    assert not self.is_root(nonroot)
    return self.LEFT if self.is_left(nonroot) else self.RIGHT
def to_child(self, nonleaf, direction):
    assert not self.is_leaf(nonleaf)
    f = self.to_left if direction == self.LEFT else self.to_right
    return f(nonleaf)

def to_children(self, node):
    assert not self.is_leaf(node)
    left = self.to_left(node)
    right = self.to_right(node)
    return left, right


def to_sibling(self, nonroot):
    assert not self.is_root(nonroot)
    parent = self.to_parent(nonroot)
    f = self.to_right if self.is_left(nonroot) else self.to_left
    return f(parent)





################ modify ##################

def leaf2new_nonleaf(self, leaf, color, entity):
    assert self.is_leaf(leaf)
    left = self.new_leaf_root()
    right = self.new_leaf_root()
    return self.replace_to_broken_node(leaf, color, entity, left=left, right=right)


def recolor(self, nonleaf):
    assert not self.is_leaf(nonleaf)
    color = to_other_color(self, nonleaf)
    return replace(self, nonleaf, color=color)


def make_new_nonleaf_root(self, color, entity):
    root = self.make_new_leaf_root()
    return leaf2new_nonleaf(root, color, entity)

def replace_using_other_parent(self, this_node:'destroy', other_node:'destroy'):
    'this_node.parent := other_node.parent; destroy both nodes'

    this_node_args = extract_nonleaf_args(self, this_node)
    return self.replace_to_broken_node(other_node, *this_node_args)



# to define replace
if 1: 
    def __not_exist_f():
        __NUL = [] # donot use this variable except replace
        def replace(self, nonleaf:'destroy', color=__NUL, entity=__NUL,
                    left:'destroy'=__NUL, right:'destroy'=__NUL):
            # for leaf, see:leaf2new_nonleaf
            assert not self.is_leaf(nonleaf)
            
            # color, entity, left, right = extract_nonleaf_args(self, node)
            input_args = color, entity, left, right
            node_args = extract_nonleaf_args(self, nonleaf)
            # 'is' not '=='
            input_args = tuple(old if new is __NUL else new for new, old in zip(input_args, node_args))

            if all(new is old for new, old in zip(input_args, node_args)):
                return nonleaf
            return self.replace_to_broken_node(nonleaf, *input_args)
        return replace
    replace = __not_exist_f(); del __not_exist_f

