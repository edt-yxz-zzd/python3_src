

class RedBlackTreeOpsABC:
    ## need not "key"; searching should be another class

    # plain - color, entity, left_plain, right_plain
    # node - plain, direction, parent_node
    @property
    def RED(self):
        pass
    def is_root(self, node):
        pass
    def is_leaf(self, node):
        pass
    def get_color(self, node):
        pass
    def set_color(self, node, color):
        pass
    def get_entity(self, node):
        pass
    def set_entity(self, node, entity):
        '''\
for remove

    mutable ... easy
    immutable:
        let_be_root
        swap_or_move
        since root ==>> no broken at all
            ... now remove ...
                fixed only broken above until root
        joint to old tree
        if red
            remove again
        fixed only broken above until root
        '''
    def make_leaf_root(self):
        # for make empty tree
        return black_leaf_root
    def make_red_nonleaf(self, entity, parent_info):
        # for insert entity
        return node

    def get_left_child(self, nonleaf):
        # me.left
    def get_right_child(self, nonleaf):
        # me.right
    def set_children(self, nonleaf, left, right):
        # me.left = left; ...
        # but without: left.parent = me; ...
        return nonleaf
    
    def get_root_parent_info(self):
        return self.get_parent_info(self.make_leaf_root())
    def get_parent_info(self, node):
        # include {parent_node, direction_info, is_root_info}
        # allow root
    def set_parent_info(self, node, parent_info):
        # without me.parent.child = me
        # now, we can make a node be root: let_be_root
        # that is cut it out of old tree
    def get_parent(self, nonroot):
        # me.parent
        # maybe : me.parent.child is not me
    def get_direction(self, nonroot):
        # me.direction # left or right
    def refresh_up(self, nonroot):
        '''
        mutable:
            me.parent.child = me
        immutable:
            parent, me, sibliing ...
            parent' = set_left(parent, me)
            me' = parent'.to_child()
            return parent', me'
            # refresh down required:
            #    sibling' = parent'.get_child() # !!!
            # new2old broken between parent' and sibling
    '''
        return parent, me

    def fixed_the_only_broken_above_until_root(self, node):
        'there is only one broken above node or none; fix it'
        return root


class WrappedRedBlackTreeNode:
    def __init__(self, ops, node):
        self.ops = ops
        self.node = node
    @property
    def RED(self):
        return self.ops.RED
    @property
    def BLACK(self):
        return self.ops.BLACK
    @property
    def LEFT(self):
        return self.ops.LEFT
    @property
    def RIGHT(self):
        return self.ops.RIGHT


    def is_root(self):
        return self.node.is_root()
    def is_leaf(self):
        return self.node.is_leaf()
    @property
    def color(self):
        return self.ops.get_color(self.node)
    @color.setter
    def color(self, c):
        self.node = self.ops.set_color(self.node, c)
    @property
    def entity(self):
        return self.ops.get_entity(self.node)
    @entity.setter
    def entity(self, e):
        self.node = self.ops.set_entity(self.node, e)

    

    @property
    def left(self):
        return self.__node2this(self.ops.get_left_child(self.node))
    @left.setter
    def left(self, x):
        self.children = x, self.right

    @property
    def right(self):
        return self.__node2this(self.ops.get_right_child(self.node))
    @right.setter
    def right(self, x):
        self.children = self.left, x 

    @property
    def children(self):
        return self.left, self.right
    @children.setter
    def children(self, x):
        left, right = x
        self.node = self.ops.set_children(self.node, left.node, right.node)

    @property
    def parent(self):
        return self.__node2this(self.ops.get_parent(self.node))
    @property
    def direction(self):
        return self.ops.get_direction(self.node)
        
    @property
    def parent_info(self):
        return self.ops.get_parent_info(self.node)
    @parent_info.setter
    def parent_info(self, x):
        self.node = self.ops.set_parent_info(self.node, x)

    def refresh_up(self):
        parent, me = self.ops.refresh_up(self.node)
        self.node = me
        return self.__node2this(parent)

    def __node2this(self, node):
        return type(self)(self.ops, node)
    def make_leaf_root(self):
        return self.__node2this(self.ops.make_leaf_root())
    def make_red_nonleaf(self, entity, parent_info):
        return self.__node2this(self.ops.make_red_nonleaf(entity, parent_info))
    def make_leaf_root(self):
        return self.__node2this(self.ops.make_leaf_root())
    def get_root_parent_info(self):
        return self.ops.get_root_parent_info()
    def fixed_the_only_broken_above_until_root(self):
        self.node = self.ops.fixed_the_only_broken_above_until_root(self.node)
        return None
    


class WrappedRedBlackTreeNodeEx(WrappedRedBlackTreeNode):
    def is_black(self):
        return self.color == self.BLACK
    def is_red(self):
        return not self.is_black()
    def is_left(self):
        return self.direction == self.LEFT
    def is_right(self):
        return not self.is_left()

    def color_to_other_color(self, color):
        return self.RED if color == self.BLACK else self.BLACK
    def recolor(self):
        self.color = self.color_to_other_color(self.color)
        return None

    def get_child(self, direction):
        return self.left if direction == self.LEFT else self.right
            
        
    def get_descendants(self, directions):
        for d in directions:
            self = self.get_child(d)
            yield self
    
    def get_descendants__olds(self, olds):
        'olds should be [child of self, child of prev, child of prev...]'
        return self.get_descendants(old.direction for old in olds)

    















    
