
'''
TODO:
    document
'''

'''
    1) Plain + Parented
        [immutable Plain] ==>> subtree sharable
        Plain a = Leaf | Nonleaf color a (Plain a) (Plain a)
        Parented a = (Plain a, Maybe (direction, Parented a))
        1-1) both immutable
        1-2) immutable + mutable
        ??1-3) mutable + immutable
    2) Leaf + Nonleaf
        [mutable Nonleaf]
        Nonleaf a = Nonleaf (Maybe (Nonleaf a)) color a (Node a) (Node a)
        Node a = Leaf a | Nonleaf a
        2-1) immutable + mutable
            Leaf a = Leaf
        2-2) mutable + mutable
            Leaf a = Leaf (Maybe (Nonleaf a))


suppose we are to wrap a plain node as RBT_Node
    there are lots of cases
    leaf:
        1) only one instance
        2) each leaf is distinguishable
        2-1) contain nothing
        2-2) contain .parent
        2-3) contain .parent, .direction
        2-4) contain .direction

    nonleaf:
        must: .color, .entity, .left, .right
        1) which properties??
            .parent? .direction?
        2) which properties are mutable??
            this determines whether a modification is preformed inplace

    3 cases = no_property, immutable_property, mutable_property
    leaf: 1 + 3*3 = 10
        singleton + parent? * direction?
    nonleaf: 2**3 * 3*3 = 72
        mutable?{color*entity*child} * parent? * direction?
    total = 10 * 72


assume underlying node use same RED/BLACK/LEFT/RIGHT
'''

__all__ = '''
RedBlackTreeNodeABC
    RBT_Node_Const_ROOT_PARENT_INFO_ABC
    RBT_Node_Bool_Constants_ABC
    RBT_Node_Class_Constants_ABC

    RBT_Node_AllSelf_ABC
        RBT_Node_AllSelf

    RBT_NodeWrapper_ABC
        RBT_Node_ImmutablePlain_MutableParentedSelf_ABC
            RBT_Node_TuplePlain_MutableParentedSelf_ABC
                RBT_Node_TuplePlain_MutableParentedSelf


        RBT_Node_SimpleParentInfo_ParentedUnderlying_ABC
            RBT_Node_ImmutableBothPlainParented_ABC
                RBT_Node_TupleBothPlainParented_ABC
                    RBT_Node_TupleBothPlainParented
'''.split()

from seed.types.ABC import *

class RedBlackTreeNodeABC(ABC):

  # constant
    
    @property
    @not_implemented
    def RED(self):...
    @property
    @not_implemented
    def BLACK(self):...
    @property
    @not_implemented
    def LEFT(self):...
    @property
    @not_implemented
    def RIGHT(self):...

  # property: read-write

    # nonleaf property
    #   if self is leaf ==>> undefined behavior

    # return RED/BLACK
    @property
    @not_implemented
    def color(self):...
    @color.setter
    @not_implemented
    def color(self, c):...
    @property
    @not_implemented
    def entity(self):...
    @entity.setter
    @not_implemented
    def entity(self, e):...

    
    # allow "self.left is not self.left"; so as ".right"
    #    but in logical self.left is self.left,
    #        i.e. they should refer to same subtree in concept
    # "other.left/right = self.left" where other is not self
    #    cripple self, cause a dangling broken below self
    #    i.e. getattr "self.left" causes undefined behavior
    #       # but setattr "self.left = ... " is fine
    #
    # if __class__ is a wrapper, and underlying node is immutable:
    #   "parent.left = me" ; parent' = parent{left=me}
    #   "me.left = x"      ; me' = me{left=x}
    #   parent's left child will be old me; parent'.left WAS me NOT me'
    #   parent always refer to old child
    #   hence we should update bottom-up
    #      or call refresh_up to update parent
    @property
    @not_implemented
    def left(self):...
    # x.left = y;
    #    let y.parent be x in concept
    #       allow "y.parent is not x" if __class__ is a wrapper
    #    cause a old2new broken above x (not y)
    #    cause a dangling above original x.left
    #    cripple original y.parent
    @left.setter
    @not_implemented
    def left(self, x):...

    @property
    @not_implemented
    def right(self):...
    @right.setter
    @not_implemented
    def right(self, x):...

    @property
    def children(self):
        return self.left, self.right
    @children.setter
    def children(self, x):
        self.left, self.right = x

    # any node property
    
    # parent_info : contain parent and direction from parent to me at least
    # the two operations we can perform on parent_info are:
    #    1) save:
    #       info = x.parent_info
    #    2) restore to any node:
    #       y.parent_info = info
    # precondition:
    #    no dangling above self
    #    # but old2new broken above self is allowed
    #    e.g. __class__ is a wrapper,
    #        and the underlying node has .parent/.direction
    #        we may def is_left(self): return self.underlying is self.underlying.parent.left
    #        hence after "self.parent.left = other"
    #            we cannot collect correct parent info
    @property
    @not_implemented
    def parent_info(self):...

    # if parent_info does not come from a root node
    #    let (parent1, diretion1) be the info contained in parent_info
    #    "y.parent_info = parent_info" <==>
    #       parent1.set_child(direction1, y)
    #          i.e. parent1.left/right = y
    #              cripple the original y.parent (if not parent1)
    #              old2new broken above parent1 (not y!!)
    #    hence we must call "parent = y.parent.refresh_up()" to update parent
    # if parent_info comes from a root node
    #    "y.parent_info = parent_info" <==>
    #       let y be root
    #       cripple the original y.parent (if y was not root)
    #    NOTE : this method may be called in __init__
    #           so, getattr "self.parent_info" is not available
    @parent_info.setter
    @not_implemented
    def parent_info(self, x):...


  # property : read only
    # nonroot property
    #   if self is root ==>> undefined behavior
    

    # allow "self.parent is not self.parent"
    #   e.g. __class__ is a wrapper,
    #        and the underlying node has .parent/.direction
    @property
    @not_implemented
    def parent(self):...

    # return LEFT/RIGHT
    @property
    @not_implemented
    def direction(self):...


    # precondition : allow dangling broken below parent
    # return (direction, parent) | None
    # postcondition :
    #    dangling broken above original parent's child
    #    dangling broken below parent
    @classmethod
    def _extract_parent_info(cls, parent_info):
        child = cls.make_leaf_root()
        _info = child.parent_info
        child.parent_info = parent_info
        if child.is_root():
            return None
        direction = child.direction
        parent = child.parent
        child.parent_info = _info
        return direction, parent

    @classmethod
    @not_implemented
    def is_ROOT_PARENT_INFO(cls, parent_info):...



    # any node query

    def is_root(self):
        return self.is_ROOT_PARENT_INFO(self.parent_info)
    @not_implemented
    def is_leaf(self):...




  # constructor

    # assume leaf with black color or none
    #    since we NEVER query color about leaf
    @classmethod
    @not_implemented
    def make_leaf_root(cls):...

    # with two black leaves
    @classmethod
    @not_implemented
    def make_red_nonleaf_root(cls, entity):...
    # with two black leaves
    # result_node.parent_info = parent_info
    @classmethod
    def make_red_nonleaf_node(cls, entity, parent_info):
        node = cls.make_red_nonleaf_root(entity)
        node.parent_info = parent_info
        return node
    
    # self is nonleaf; result {.parent=self, .direction=direction}
    # allow dangling broken below self
    @not_implemented
    def make_child_parent_info(self, direction):...

    # why not implement it?
    #   since it is likely to be a building block of make_leaf_root
    @classmethod
    @not_implemented
    def new_ROOT_PARENT_INFO(cls):
        return cls.make_leaf_root().parent_info

  # fixer
  
    # fix old2new broken above me
    #    i.e. me.parent.left/right = me; return parent
    # precondition:
    #     not self.is_root()
    # return parent
    # postcondition:
    #     old2new broken above parent
    #     new2old broken below me
    #        e.g. __class__ is a wrapper,
    #             underlying_node is immutable and has all properties:
    #                {.pos{.parent, .direction}, .plain {.left, .right}, ...}
    #             me.parent.left/right = me
    #                -- parent = This(me.underlying.parent)
    #@abstractmethod
    def refresh_up(self):
        if self.is_left():
            self.parent.left = self
        else:
            self.parent.right = self
        return self.parent

    # fix new2old broken below me
    # precondition:
    #    no other kinds of brokens
    # usage:
    #    left, = me.refresh_down(me.LEFT) <==> left = me.left
    def refresh_down(self, *directions):
        for direction in directions:
            self = self.get_child(direction)
            yield self
            
        

    # return root
    #@abstractmethod
    def fixed_the_only_broken_above_until_root(self):
        node = self
        while not node.is_root():
            node = node.refresh_up()
        root = node
        return root
    

  # structure modify

    # allow old2new broken above me and above parent and so on...
    #   not allow dangling
    # precondition: exists self.parent.parent
    # return node who occupies grandpa's position
    # postcondition:
    #    if return node is not root:
    #       old2new broken above return_node's parent
    def trinode_restructure(self):
        parent = self.parent
        grandpa = parent.parent
        grandpa_pos = grandpa.parent_info
        sibling = self.sibling
        uncle = parent.sibling

        if self.is_left():
            A, B = self, parent
            a, b, c = self.left, self.right, sibling
        else:
            A, B = parent, self
            a, b, c = sibling, self.left, self.right
        if parent.is_left():
            A, B, C = A, B, grandpa
            a, b, c, d = a, b, c, uncle
        else:
            A, B, C = grandpa, A, B
            a, b, c, d = uncle, a, b, c, d

        # update bottom-up!!!
        A.children = a, b
        C.children = c, d
        B.children = A, C
        B.parent_info = grandpa_pos
        return B
    


    def another_color_from(self, color):
        return self.BLACK if color == self.RED else self.RED
    def another_direction_from(self, direction):
        return self.RIGHT if color == self.LEFT else self.LEFT




    # nonleaf query
    @property
    def another_color(self):
        return self.another_color_from(self.color)
    def is_red(self):
        return self.color == self.RED
    def is_black(self):
        return not self.is_red()
    
    def get_child(self, direction):
        return self.left if direction == self.LEFT else self.right

    # nonleaf modify
    # postcondition: old2new broken above self
    def set_child(self, direction, node):
        if direction == self.LEFT:
            self.left = node
        else:
            self.right = node
    def recolor(self):
        self.color = self.another_color



    
    
    # nonroot query
    def sibling(self):
        return self.parent.get_child(self.another_direction)
    @property
    def another_direction(self):
        return self.another_direction_from(self.direction)
        
    def is_left(self):
        return self.direction == self.LEFT
    def is_right(self):
        return not self.is_left()





class RBT_Node_Const_ROOT_PARENT_INFO_ABC(RedBlackTreeNodeABC):
    ROOT_PARENT_INFO = None
    @property
    @classmethod
    @not_implemented
    def ROOT_PARENT_INFO(cls):...
    @classmethod
    def new_ROOT_PARENT_INFO(cls):
        return cls.ROOT_PARENT_INFO
    @classmethod
    def is_ROOT_PARENT_INFO(cls, parent_info):
        return parent_info == cls.new_ROOT_PARENT_INFO()
    
class RBT_Node_Bool_Constants_ABC(RedBlackTreeNodeABC):
    # since double-black color on single node
    #   let black be 1
    # children can be treated as a sequence
    #   let left be 0
    RED = LEFT = False
    BLACK = RIGHT = True
    
class RBT_Node_Class_Constants_ABC(RedBlackTreeNodeABC):
    from seed.cases.CLASS import RED, BLACK, LEFT, RIGHT


class RBT_Node_SimpleParentInfo_ParentedSelf_ABC(RedBlackTreeNodeABC):
    # assume ._parent_info
    # parent_info = (direction, parent)
    

    
    @property
    def parent_info(self):
        return self._parent_info
    @parent_info.setter
    def parent_info(self, info):
        # cripple_parent
        if not self.is_ROOT_PARENT_INFO(info):
            assert len(info) == 2
        self._parent_info = info
        # xxxx parent.set_child(direction, self)
        
    def make_child_parent_info(self, direction):
        return direction, self
    
    @property
    def direction(self):
        return self.parent_info[0]
    @property
    def parent(self):
        return self.parent_info[1]



##
##class RBT_Node_xxxx_ABC(RedBlackTreeNodeABC):
##    PLAIN_LEAF = None
##    @property
##    def color(self):...
##    @color.setter
##    def color(self, c):...
##    @property
##    def entity(self):...
##    @entity.setter
##    def entity(self, e):...
##
##
##    @property
##    def left(self):...
##    @left.setter
##    def left(self, x):...
##
##    @property
##    def right(self):...
##    @right.setter
##    def right(self, x):...
##    @property
##    def parent(self):...
##
##    @property
##    def direction(self):...
##
##
##    @classmethod
##    def is_ROOT_PARENT_INFO(cls, parent_info):...
##    def is_leaf(self):...
##
##
##    @not_implemented
##    def make_child_parent_info(self, direction):...
##    @classmethod
##    @not_implemented
##    def new_ROOT_PARENT_INFO(cls):...
##
##
##
##    @classmethod
##    def make_leaf_root(cls):...
##
##    @classmethod
##    def make_red_nonleaf_root(cls, entity):...







class RBT_Node_AllSelf_ABC(RBT_Node_SimpleParentInfo_ParentedSelf_ABC):
    # parent_info = ROOT_PARENT_INFO | (direction, parent)
    def __init__(self, maybe_args, parent_info):
        if not maybe_args:
            # leaf
            self.left = None
        else:
            self.color, self.entity, self.left, self.right = maybe_args
        self.parent_info = parent_info

    @classmethod
    def from_maybe_node_args_and_parent_info(cls, maybe_args, parent_info):
        return cls(maybe_args, parent_info)
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, c):
        self._color = c
    @property
    def entity(self):
        return self._entity
    @entity.setter
    def entity(self, e):
        self._entity = e


    @property
    def left(self):
        return self._left
    @left.setter
    def left(self, x):
        self._left = x
        if x is None:
            # this is a leaf
            return
        # bug: forgot update x.parent_info
        x.parent_info = self.make_child_parent_info(self.LEFT)

    @property
    def right(self):
        return self._right
    @right.setter
    def right(self, x):
        self._right = x
        x.parent_info = self.make_child_parent_info(self.RIGHT)


    def is_leaf(self):
        return self._left is None




    @classmethod
    def make_leaf_root(cls):
        args = None
        return cls.from_maybe_node_args_and_parent_info(args, cls.new_ROOT_PARENT_INFO())

    @classmethod
    def make_red_nonleaf_root(cls, entity):
        args = cls.RED, entity, cls.make_leaf_root(), cls.make_leaf_root()
        return cls.from_maybe_node_args_and_parent_info(args, cls.new_ROOT_PARENT_INFO())


    
class RBT_Node_AllSelf(RBT_Node_AllSelf_ABC,
                       RBT_Node_Const_ROOT_PARENT_INFO_ABC,
                       RBT_Node_Class_Constants_ABC):
    from seed.cases.CLASS import ROOT_PARENT_INFO











class RBT_NodeWrapper_ABC(RedBlackTreeNodeABC):
    # assume underlying node {.underlying}
    # assume both self and underlying_node have {.parent, .direction}
    #    we update both
    #    for a concrete subclass, we simplely pass some update action


    # class NO_INPUT: pass # used a default value to indicate "no input"

    def __init__(self, underlying_node, parent_info):
        self.underlying = underlying_node
        self.parent_info = parent_info
        
    @classmethod
    @not_implemented
    def get_underlying_color(cls, underlying):...
    @classmethod
    @not_implemented
    def get_underlying_entity(cls, underlying):...
    @classmethod
    @not_implemented
    def get_underlying_left(cls, underlying):...
    @classmethod
    @not_implemented
    def get_underlying_right(cls, underlying):...

    # since not all underlying node types own .parent/.direction
    #    we can return a dict with two possible keys:
    #        direction, parent_underlying
    #    which keys miss means they are "Not Available"
    # underlying is root ==>> return {}
    # but return {} ==xx==>> underlying is root
    @classmethod
    @not_implemented
    def get_underlying_direction_parent_dict(cls, underlying):...




    


    # parent_underlying : self.parent.underlying or new_parent.underlying
    #   not self.get_underlying_parent(self.underlying);
    #   since latter may fail if underlying has no {.parent}
    # left_underlying =
    #      new_left.underlying
    #           not self.left.underlying
    #           since self.left may be a leaf or dangling
    #      or self.left.underlying / self.get_underlying_left(self.underlying)
    #           using old value while not dangling
    # known keywords are:
    #   color, entity, left_underlying, right_underlying, maybe_direction_parent_underlying
    # where direction_parent_underlying_dict is None or
    #      a dict with two possible keys:
    #         direction, parent_underlying
    #      if make a root nonleaf,
    #         direction_parent_underlying_dict should be empty
    #      but empty not means make a root
    #         it may means nonleaf does not have {.direction, .parent}
    @classmethod
    @not_implemented
    def make_underlying_nonleaf(cls, color, entity,
                                left_underlying, right_underlying,
                                direction_parent_underlying_dict):...
    @classmethod
    @not_implemented
    def make_underlying_leaf_root(cls):...
    @classmethod
    def __test_known_keywords__setattr_underlying_node(
        cls, *,
        color=0, entity=0, left_underlying=0, right_underlying=0, direction_parent_underlying_dict=0):
        assert set(direction_parent_underlying_dict) <= \
               frozenset(['direction', 'parent_underlying'])
    
    # modify old node or create a new node
    # return the modified node or new node
    @classmethod
    def setattr_underlying_node(cls, target_underlying_node, **kwds):
        cls.__test_known_keywords__setattr_underlying_node(**kwds)
        d = self.extract_underlying_data_as_dict(self.underlying)
        d.update(kwds)
        return cls.make_underlying_nonleaf(**d)

    # return color, entity, left_underlying, right_underlying,
    #        direction, parent_underlying
    @classmethod
    def extract_underlying_data(cls, underlying):
        return tuple(f(underlying) for f in [
            cls.get_underlying_color,
            cls.get_underlying_entity,
            cls.get_underlying_left,
            cls.get_underlying_right,
            cls.get_underlying_direction_parent_dict,])
    @classmethod
    def extract_underlying_data_as_dict(cls, underlying):
        color, entity, left_underlying, right_underlying, \
               direction_parent_underlying_dict = \
               self.extract_underlying_data(self.underlying)
        return dict(color=color, entity=entity,
                    left_underlying=left_underlying,
                    right_underlying=right_underlying,
                    direction_parent_underlying_dict = direction_parent_underlying_dict)





    # constructor
    
    @classmethod
    def from_underlying_node_and_parent_info(cls, underlying, parent_info):
        return cls(underlying, parent_info)
        

    @classmethod
    def make_leaf_root(cls):
        underlying = cls.make_underlying_leaf_root()
        return cls.from_underlying_node_and_parent_info(underlying, cls.new_ROOT_PARENT_INFO())

    @classmethod
    def make_red_nonleaf_root(cls, entity):
        left = cls.make_leaf_root()
        right = cls.make_leaf_root()
        color = cls.RED
        underlying = cls.make_underlying_nonleaf(
            color = color,
            entity = entity,
            left_underlying = left.underlying,
            right_underlying = right.underlying,
            direction_parent_underlying_dict = {})
        return cls.from_underlying_node_and_parent_info(underlying,
                                                        cls.new_ROOT_PARENT_INFO())
    
    
        


    

    def __setattr(self, **kwds):
        self.underlying = self.setattr_underlying_node(self.underlying, **kwds)
    
        
    @property
    def color(self):
        return self.get_underlying_color(self.underlying)
    @color.setter
    def color(self, color):
        self.__setattr(color = color)
    @property
    def entity(self):
        return self.get_underlying_entity(self.underlying)
    @entity.setter
    def entity(self, entity):
        self.__setattr(entity = entity)

    @property
    def left(self):
        return self.get_child(self.LEFT)
    @left.setter
    def left(self, x):
        self.set_child(self.LEFT, x)
    @property
    def right(self):
        return self.get_child(self.RIGHT)
    @left.setter
    def right(self, x):
        self.set_child(self.RIGHT, x)
        
    def get_underlying_child(self, underlying, direction):
        f = self.get_underlying_left if direction == self.LEFT \
            else self.get_underlying_right
        return f(underlying)
    def get_child(self, direction):
        pos = self.make_child_parent_info(direction)
        underlying_child = self.get_underlying_child(self.underlying, direction)
        return self.from_underlying_node_and_parent_info(underlying_child, pos)
    def set_child(self, direction, child):
        # modification should be bottom-up
        # first child
        child.parent_info = self.make_child_parent_info(direction)

        # second self
        color, entity, left_underlying, right_underlying = self.extract_underlying_data(self.underlying)
        if direction == self.LEFT:
            d = dict(left_underlying = child.underlying)
        else:
            d = dict(right_underlying = child.underlying)
        self.__setattr(**d)
        






    
        







class RBT_Node_ImmutablePlain_MutableParentedSelf_ABC(RBT_Node_Const_ROOT_PARENT_INFO_ABC,
                                                      RBT_NodeWrapper_ABC):
    # self is the node with {.direction, .parent}
    # self.underlying is plain node
    
    PLAIN_LEAF = None
    @property
    @classmethod
    @not_implemented
    def PLAIN_LEAF(cls):...
    

    def is_leaf(self):
        return self.underlying == self.PLAIN_LEAF



        

    


    
class RBT_Node_TuplePlain_MutableParentedSelf_ABC(
    RBT_Node_ImmutablePlain_MutableParentedSelf_ABC):
    # underlying node (i.e. plain node) = (color, entity, left, right)
    
    @classmethod
    def get_underlying_color(cls, underlying):
        return underlying[0]
    @classmethod
    def get_underlying_entity(cls, underlying):
        return underlying[1]
    @classmethod
    def get_underlying_left(cls, underlying):
        return underlying[2]
    @classmethod
    def get_underlying_right(cls, underlying):
        return underlying[3]
    @classmethod
    def get_underlying_direction_parent_dict(cls, underlying):
        return {}
    @classmethod
    def make_underlying_nonleaf(cls, color, entity,
                                left_underlying, right_underlying,
                                direction_parent_underlying_dict):
        assert not direction_parent_underlying_dict
        return color, entity, left_underlying, right_underlying
    @classmethod
    def make_underlying_leaf_root(cls):
        return cls.PLAIN_LEAF



class RBT_Node_TuplePlain_MutableParentedSelf(
    RBT_Node_TuplePlain_MutableParentedSelf_ABC,
    RBT_Node_Class_Constants_ABC,
    RBT_Node_SimpleParentInfo_ParentedSelf_ABC):
    
    from seed.cases.CLASS import PLAIN_LEAF, ROOT_PARENT_INFO























class RBT_Node_AllUnderlying_ABC(RBT_NodeWrapper_ABC):

class RBT_Node_SimpleParentInfo_ParentedUnderlying_ABC(RBT_NodeWrapper_ABC):
    # self.parent_info = underlying_parent_info = direction, parent_underlying

    @classmethod
    @not_implemented
    def is_root_underlying_parent_info(cls, underlying_parent_info):...
    @classmethod
    @not_implemented
    def get_underlying_parent_info(cls, underlying):...

    # return the modified underlying node or new one
    @classmethod
    @not_implemented
    def set_underlying_parent_info(cls, underlying, underlying_parent_info):...

    

    
    @property
    def parent_info(self):
        return self.get_underlying_parent_info(self.underlying)
    @parent_info.setter
    def parent_info(self, parent_info):
        # cripple_parent
        underlying_parent_info = parent_info
        if not self.is_root_underlying_parent_info(underlying_parent_info):
            assert len(underlying_parent_info) == 2
        self.underlying = self.set_underlying_parent_info(self.underlying, underlying_parent_info)

        
    def make_child_parent_info(self, direction):
        return direction, self.underlying
    
    @property
    def direction(self):
        return self.parent_info[0]
    @property
    def parent(self):
        parent_underlying = self.parent_info[1]
        parent_info_of_parent = underlying_parent_info_of_parent\
                              = self.get_underlying_parent_info(parent_underlying)
        return type(self).from_underlying_node_and_parent_info(parent_underlying, parent_info_of_parent)



class RBT_Node_ImmutableBothPlainParented_ABC(RBT_Node_Const_ROOT_PARENT_INFO_ABC,
                                              RBT_Node_SimpleParentInfo_ParentedUnderlying_ABC,
                                              RBT_NodeWrapper_ABC):
    # self is the node with no {.direction, .parent}
    # self.underlying is parented node (i.e. with {.direction, .parent})
    # assume parent_info == underlying_parent_info

    def from_underlying_node(cls, underlying):
        del
    
    @classmethod
    @not_implemented
    def get_underlying_parent_info(cls, underlying):...
    @classmethod
    def is_root_underlying_parent_info(cls, underlying_parent_info):
        parent_info = underlying_parent_info
        return cls.is_ROOT_PARENT_INFO(parent_info)
    @classmethod
    @not_implemented
    def is_underlying_leaf(cls, underlying):...


    def is_leaf(self):
        return self.is_underlying_leaf(self.underlying)    
    @classmethod
    def new_underlying_ROOT_PARENT_INFO(cls):
        return cls.new_ROOT_PARENT_INFO()



    
class RBT_Node_TupleBothPlainParented_ABC(
    RBT_Node_ImmutableBothPlainParented_ABC):
    # underlying node (i.e. parented node) = (plain, underlying_parent_info)
    # plain node = (color, entity, left_plain, right_plain)
    # underlying_parent_info = ROOT_PARENT_INFO | (direction, parent_underlying)
    # parent_info = underlying_parent_info

    @property
    @classmethod
    @not_implemented
    def PLAIN_LEAF(cls):...
    @classmethod
    def set_underlying_parent_info(cls, underlying, underlying_parent_info):
        plain = cls.get_underlying_plain(underlying)
        return plain, underlying_parent_info
    

    
    

##    @classmethod
##    def is_underlying_root(cls, underlying):
##        return cls.is_root_underlying_parent_info(cls.get_underlying_parent_info(underlying))
    
    @classmethod
    def is_underlying_leaf(cls, underlying):
        return cls.get_underlying_plain(underlying) == cls.PLAIN_LEAF

    
    @classmethod
    def get_underlying_plain(cls, underlying):
        return underlying[0]

    @classmethod
    def get_underlying_parent_info(cls, underlying):
        return underlying[1]
    
    @classmethod
    def get_underlying_color(cls, underlying):
        return cls.get_underlying_plain(underlying)[0]
    @classmethod
    def get_underlying_entity(cls, underlying):
        return cls.get_underlying_plain(underlying)[1]
    @classmethod
    def get_underlying_left(cls, underlying):
        # bug: return cls.get_underlying_plain(underlying)[2]
        left_plain = cls.get_underlying_plain(underlying)[2]
        left_pos = cls.LEFT, underlying
        return left_plain, left_pos
    @classmethod
    def get_underlying_right(cls, underlying):
        right_plain = cls.get_underlying_plain(underlying)[3]
        right_pos = cls.RIGHT, underlying
        return right_plain, right_pos
    @classmethod
    def get_underlying_direction_parent_dict(cls, underlying):
        info = cls.get_underlying_parent_info(underlying)
        if cls.is_root_underlying_parent_info(info):
            return {}
        direction, parent_underlying = info
        return dict(direction = direction, parent_underlying = parent_underlying)


    @classmethod
    def make_underlying_nonleaf(cls, color, entity,
                                left_underlying, right_underlying,
                                direction_parent_underlying_dict):
        if not direction_parent_underlying_dict:
            info = cls.new_underlying_ROOT_PARENT_INFO()
        else:
            assert len(direction_parent_underlying_dict) == 2
            info = direction_parent_underlying_dict['direction'], \
                   direction_parent_underlying_dict['parent_underlying']
        plain = (color, entity,
                 cls.get_underlying_plain(left_underlying),
                 cls.get_underlying_plain(right_underlying))
        return plain, info
    @classmethod
    def make_underlying_leaf_root(cls):
        return (cls.PLAIN_LEAF, cls.new_underlying_ROOT_PARENT_INFO())



class RBT_Node_TupleBothPlainParented(
    RBT_Node_Class_Constants_ABC,
    RBT_Node_TupleBothPlainParented_ABC):
    from seed.cases.CLASS import PLAIN_LEAF, ROOT_PARENT_INFO

    



def __test_wrapper(cls):
    node = cls.make_leaf_root()
    #print(node.underlying)
    node.underlying
    node = cls.make_red_nonleaf_root(2)
    node.underlying, node.parent_info
    #print(node.underlying, node.parent_info)
    __test(cls)

def __test(cls):
    try:
        node = cls.make_leaf_root()
        assert node.is_root()
        assert node.is_leaf()
        
        node = cls.make_red_nonleaf_root(2)
        assert node.is_root()
        assert not node.is_leaf()
        
        assert node.entity == 2
        assert node.color == node.RED
        assert node.left
        assert node.left.is_leaf()
        assert not node.left.is_root()
        assert node.left.direction == node.LEFT
        assert node.left.parent.entity == 2
    except:
        print(node)
        print(node.underlying)
        print(node.parent_info)
        print(node.left.parent_info)
        raise


__test(RBT_Node_AllSelf)
__test_wrapper(RBT_Node_TuplePlain_MutableParentedSelf)
__test_wrapper(RBT_Node_TupleBothPlainParented)











    
