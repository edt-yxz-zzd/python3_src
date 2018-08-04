
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
MutableRedBlackTreeNodeABC
    RBT_Node_Const_ROOT_PARENT_INFO_ABC
    RBT_Node_Bool_Constants_ABC
    RBT_Node_Class_Constants_ABC

    RBT_Node_AllSelf_ABC
        RBT_Node_AllSelf

    RBT_NodeWrapper_ABC
        RBT_Node_ImmutablePlain_MutableParentedSelf_ABC
            RBT_Node_TuplePlain_MutableParentedSelf_ABC
                RBT_Node_TuplePlain_MutableParentedSelf


        RBT_Node_AllUnderlying_ABC
            RBT_Node_ImmutableBothPlainParented_ABC
                RBT_Node_XTupleBothPlainParented_ABC
                    RBT_Node_XTupleBothPlainParented_SizeDepthOrderno_ABC
                    RBT_Node_TupleBothPlainParented_ABC
                        RBT_Node_TupleBothPlainParented
'''.split()

#from seed.types.ABC import *
#from .importABC import *
from .importABC import ABC, not_implemented
from .TreeNodeABC import *
from seed.lang.class_property import class_property
#class_property = classmethod

class MutableRedBlackTreeNodeABC(MutableBinaryTreeNodeABC, EqOrientedTreeNodeABC):

    def nonleaf_node_eq(self, other):
        assert isinstance(other, __class__)
        assert not self.is_leaf()
        assert not other.is_leaf()
        assert self.num_children == other.num_children
        return bool(self.is_red()) == bool(other.is_red()) and\
               self.entity == other.entity

    def leaf_node_eq(self, other):
        assert isinstance(other, __class__)
        assert self.is_leaf()
        assert other.is_leaf()
        return True


  # constant

    @class_property
    @not_implemented
    def RED(cls):...
    @class_property
    @not_implemented
    def BLACK(cls):...

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

    @classmethod
    def from_entities(cls, entities, reverse=False):
        # O(n*log(n))
        #   insert_entity_at_leaf + get_last_leaf/get_first_leaf
        #       OrientedTreeNode_PositiveNumChildren_ABC.get_first_leaf
        #       OrientedTreeNode_PositiveNumChildren_ABC.get_last_leaf
        #       MutableRedBlackTreeNodeABC.insert_entity_at_leaf
        root = cls.make_leaf_root()
        if reverse:
            def get_leaf(root):
                return root.get_first_leaf()
        else:
            def get_leaf(root):
                return root.get_last_leaf()
        for entity in entities:
            leaf = get_leaf(root)
            root = leaf.insert_entity_at_leaf(entity)
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
            a, b, c, d = uncle, a, b, c

        # update bottom-up!!!
        A.children = a, b
        C.children = c, d
        B.children = A, C
        B.parent_info = grandpa_pos
        return B


    @classmethod
    def another_color_from(cls, color):
        return cls.BLACK if color == cls.RED else cls.RED




    # any node query
    @property
    def another_color(self):
        return self.another_color_from(self.color)
    def is_red(self):
        # bug: forgot "not self.is_leaf() and"
        return not self.is_leaf() and self.color == self.RED
    def is_black(self):
        return not self.is_red()

    # nonleaf modify

    def recolor(self):
        self.color = self.another_color


    # insert/remove
    def insert_entity_at_leaf(self, entity):
        # :: leaf_self -> entity -> new_root
        assert self.is_leaf()
        raise NotImplementedError
    def remove_leaf_and_its_parent(self):
        # :: leaf_self -> new_root
        assert self.is_leaf()
        raise NotImplementedError
    def remove_entity_at_nonleaf(self,
                                 child_leaf_first=True,
                                 prefer_succ_leaf=True):
        '''
:: nonleaf_self -> child_leaf_first -> prefer_succ_leaf -> new_root

1) if child_leaf_first ==>>
    if there is a child leaf, remove it and self
    else goto 2)
2) leaf = self.succ_leaf() if prefer_succ_leaf else self.prev_leaf()
    swap self.entity and leaf.parent.entity
    remove leaf and its parent
return new_root
'''
        assert self.is_nonleaf()
        raise NotImplementedError








class RBT_Node_Const_ROOT_PARENT_INFO_ABC(MutableRedBlackTreeNodeABC):
    ROOT_PARENT_INFO = None
    @class_property
    @not_implemented
    def ROOT_PARENT_INFO(cls):...
    @classmethod
    def new_ROOT_PARENT_INFO(cls):
        return cls.ROOT_PARENT_INFO
    @classmethod
    def is_ROOT_PARENT_INFO(cls, parent_info):
        return parent_info == cls.new_ROOT_PARENT_INFO()

class RBT_Node_Bool_Constants_ABC(MutableRedBlackTreeNodeABC):
    # since double-black color on single node
    #   let black be 1
    # children can be treated as a sequence
    #   let left be 0
    RED = LEFT = False
    BLACK = RIGHT = True

class RBT_Node_Class_Constants_ABC(MutableRedBlackTreeNodeABC):
    from seed.cases.CLASS import RED, BLACK, LEFT, RIGHT

##
##class RBT_Node_xxxx_ABC(MutableRedBlackTreeNodeABC):
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







class RBT_Node_AllSelf_ABC(MutableTreeNode_SimpleParentInfo_ParentedSelf_ABC):
    # parent_info = ROOT_PARENT_INFO | (direction, parent)
    # both nonleaf and leaf are of type __class__
    #   so, None is not a node
    def __init__(self, maybe_args, parent_info):
        if not maybe_args:
            # leaf
            self._left = None
        else:
            self.color, self.entity, self._left, self._right = maybe_args

            # to set parent_info of left/right
            self.left = self._left
            self.right = self._right
        self.parent_info = parent_info

    def copy(self):
        # as root
        cls = type(self)
        if self.is_leaf():
            maybe_args = None
        else:
            maybe_args = self.color, self.entity, self.left.copy(), self.right.copy()
        new = cls.from_maybe_node_args_and_parent_info(
                    maybe_args, self.new_ROOT_PARENT_INFO())
        return new



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
        if self.is_leaf(): raise TypeError # AttributeError
        self._left = x
        # bug: forgot update x.parent_info
        x.parent_info = self.make_child_parent_info(self.LEFT)

    @property
    def right(self):
        return self._right
    @right.setter
    def right(self, x):
        if self.is_leaf(): raise TypeError # AttributeError
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









MutableBinaryTreeNodeWrapper_NoOtherLeafAttrs_ABC.make_leaf_root
#print(MutableBinaryTreeNodeWrapper_NoOtherLeafAttrs_ABC.make_leaf_root.__self__)
#print(MutableRedBlackTreeNodeABC.make_leaf_root.__self__)
# MutableTreeNodeWrapperABC.make_leaf_root override MutableRedBlackTreeNodeABC.make_leaf_root
class RBT_NodeWrapper_ABC(
                          MutableBinaryTreeNodeWrapper_NoOtherLeafAttrs_ABC,
                          MutableTreeNodeWrapperABC,
                          MutableRedBlackTreeNodeABC):

    # assume underlying node {.underlying}
    # assume both self and underlying_node have {.parent, .direction}
    #    we update both
    #    for a concrete subclass, we simplely pass some update action


    @classmethod
    @not_implemented
    def get_underlying_left(cls, nonleaf_underlying):...
    @classmethod
    @not_implemented
    def get_underlying_right(cls, nonleaf_underlying):...


    @classmethod
    @not_implemented
    def get_underlying_color(cls, nonleaf_underlying):...
    @classmethod
    @not_implemented
    def get_underlying_entity(cls, nonleaf_underlying):...
    @classmethod
    def get_underlying_other_nonleaf_attr_dict(cls, nonleaf_underlying):
        return dict(color=cls.get_underlying_color(nonleaf_underlying),
                    entity=cls.get_underlying_entity(nonleaf_underlying))



    @classmethod
    def make_underlying_nonleaf(cls,
                                position2underlying_child_dict,
                                position_parent_underlying_dict,
                                **other_nonleaf_attr_dict):
        #print(other_nonleaf_attr_dict)
        assert len(position2underlying_child_dict) == 2
        assert len(other_nonleaf_attr_dict) == 2
        left_underlying = position2underlying_child_dict[cls.LEFT]
        right_underlying = position2underlying_child_dict[cls.RIGHT]
        return cls.make_underlying_nonleaf_rbt(
            left_underlying = left_underlying,
            right_underlying = right_underlying,
            position_parent_underlying_dict = position_parent_underlying_dict,
            **other_nonleaf_attr_dict)




    @classmethod
    @not_implemented
    def make_underlying_nonleaf_rbt(cls, color, entity,
                                left_underlying, right_underlying,
                                position_parent_underlying_dict):...
    @classmethod
    @not_implemented
    def make_underlying_leaf(cls,
                             position_parent_underlying_dict):...


    # get_underlying_position_parent_dict, make_underlying_leaf




    # constructor


    @classmethod
    def make_red_nonleaf_root(cls, entity):
        return cls.make_nonleaf_root_with_leaves((cls.LEFT, cls.RIGHT), color=cls.RED, entity=entity)



    def __setattr(self, **kwds):
        self.underlying = self.setattr_underlying_nonleaf_node(self.underlying, **kwds)


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


##    def get_underlying_child(self, underlying, direction):
##        f = self.get_underlying_left if direction == self.LEFT \
##            else self.get_underlying_right
##        return f(underlying)
##    def get_child(self, direction):
##        pos = self.make_child_parent_info(direction)
##        underlying_child = self.get_underlying_child(self.underlying, direction)
##        return self.from_underlying_node_and_parent_info(underlying_child, pos)
##    def set_child(self, direction, child):
##        # modification should be bottom-up
##        # first child
##        child.parent_info = self.make_child_parent_info(direction)
##
##        # second self
##        if direction == self.LEFT:
##            d = dict(left_underlying = child.underlying)
##        else:
##            d = dict(right_underlying = child.underlying)
##        self.__setattr(**d)
##

















class RBT_Node_ImmutablePlain_MutableParentedSelf_ABC(RBT_Node_Const_ROOT_PARENT_INFO_ABC,
                                                      RBT_NodeWrapper_ABC):
    # self is the node with {.direction, .parent}
    # self.underlying is plain node
    #       ??? without parent_info???

    PLAIN_LEAF = None
    @class_property
    @not_implemented
    def PLAIN_LEAF(cls):...

    @classmethod
    def get_underlying_position_parent_dict(cls, underlying):
        return {}

    @classmethod
    def make_underlying_leaf(cls,
                             position_parent_underlying_dict):
        assert not position_parent_underlying_dict
        return cls.PLAIN_LEAF


    def is_leaf(self):
        return self.is_PLAIN_LEAF(self.underlying)
    @classmethod
    def is_PLAIN_LEAF(cls, plain_node):
        return plain_node == cls.PLAIN_LEAF


    def copy(self):
        # as root
        cls = type(self)
        #if self.is_leaf(): return cls.make_leaf_root()
        return cls.from_underlying_node_and_parent_info(
                    self.underlying, cls.new_ROOT_PARENT_INFO())
        #self.parent_info
        return cls.make_nonleaf_root_with_leaves([left, right], color=self.color, entity=self.entity)







'''
make_nonleaf_root_with_leaves
from_underlying_node_and_parent_info
from_maybe_node_args_and_parent_info
from_underlying_node
from_root_plain_node
'''

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
    def make_underlying_nonleaf_rbt(cls, color, entity,
                                left_underlying, right_underlying,
                                position_parent_underlying_dict):
        assert not position_parent_underlying_dict
        return color, entity, left_underlying, right_underlying


    @classmethod
    def make_underlying_leaf(cls,
                             position_parent_underlying_dict):
        assert not position_parent_underlying_dict
        return cls.PLAIN_LEAF

class RBT_Node_TuplePlain_MutableParentedSelf(
    RBT_Node_TuplePlain_MutableParentedSelf_ABC,
    RBT_Node_Class_Constants_ABC,
    MutableTreeNode_SimpleParentInfo_ParentedSelf_ABC):

    from seed.cases.CLASS import PLAIN_LEAF, ROOT_PARENT_INFO























class RBT_Node_AllUnderlying_ABC(MutableTreeNodeWrapper_AllUnderlying_ABC,
                                 RBT_NodeWrapper_ABC):
    # TODO
    # xxxxxxxxxxxxxxxxxxxxxxxxxx
    pass


class RBT_Node_ImmutableBothPlainParented_ABC(MutableTreeNodeWrapper_SimpleParentInfo_ParentedUnderlying_ABC,
                                              RBT_Node_AllUnderlying_ABC,
                                              RBT_Node_Const_ROOT_PARENT_INFO_ABC,
                                              ):

    @class_property
    @not_implemented
    def PLAIN_LEAF(cls):...
    @classmethod
    def is_PLAIN_LEAF(cls, plain_node):
        return plain_node == cls.PLAIN_LEAF

class RBT_Node_XTupleBothPlainParented_ABC(
    RBT_Node_ImmutableBothPlainParented_ABC):
    # underlying node (i.e. parented node) = (plain, underlying_parent_info)
    # plain node = LEAF | (color, entity, left_plain, right_plain, other attrs...)
    # underlying_parent_info = ROOT_PARENT_INFO | (direction, parent_underlying, other attrs...)
    # parent_info = underlying_parent_info
    # plain node extra attrs: e.g. size
    # underlying_parent_info extra attrs: e.g. depth, order_number_in_whole_tree


    @classmethod
    def from_root_plain_node(cls, plain_node):
        info = cls.new_ROOT_PARENT_INFO()
        underlying = plain_node, info
        return cls.from_underlying_node(underlying)
    @property
    def plain(self):
        return self.get_underlying_plain(self.underlying)

    @classmethod
    def set_underlying_parent_info(cls, underlying, underlying_parent_info):
        plain = cls.get_underlying_plain(underlying)
        return plain, underlying_parent_info

    def copy(self):
        # as root
        return self.from_root_plain_node(self.plain)




##    @classmethod
##    def is_underlying_root(cls, underlying):
##        return cls.is_root_underlying_parent_info(cls.get_underlying_parent_info(underlying))

    @classmethod
    def is_underlying_leaf(cls, underlying):
        return cls.is_PLAIN_LEAF(cls.get_underlying_plain(underlying))

    @classmethod
    def get_underlying_position_from(cls, underlying_parent_info):
        return underlying_parent_info[0]
    @classmethod
    def get_underlying_parent_from(cls, underlying_parent_info):
        return underlying_parent_info[1]

    @classmethod
    def get_underlying_plain(cls, underlying):
        return underlying[0]

    @classmethod
    def get_underlying_parent_info(cls, underlying):
        return underlying[1]

    @classmethod
    def get_underlying_color(cls, underlying):
        try:
            return cls.get_underlying_plain(underlying)[0]
        except:
            from pprint import pprint
            pprint(underlying)
            pprint(cls.get_underlying_plain(underlying))
            raise
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
    def make_underlying_nonleaf_rbt(cls, color, entity,
                                left_underlying, right_underlying,
                                position_parent_underlying_dict):
        info = cls.make_parent_info_from_dict(position_parent_underlying_dict)
        plain = cls.make_plain(color, entity,
                               cls.get_underlying_plain(left_underlying),
                               cls.get_underlying_plain(right_underlying))
        return plain, info
    @classmethod
    def make_parent_info_from_dict(cls, position_parent_underlying_dict):
        if not position_parent_underlying_dict:
            info = cls.new_underlying_ROOT_PARENT_INFO()
        else:
            assert len(position_parent_underlying_dict) == 2
            direction = position_parent_underlying_dict['position']
            parent_underlying = position_parent_underlying_dict['parent_underlying']
            parent = cls.from_underlying_node(parent_underlying)
            info = parent.make_child_parent_info_at_pos(direction)
            if 0:
                assert len(position_parent_underlying_dict) == \
                       2 + len(cls.ordered_underlying_parent_info_extra_attr_names)
                it = chain(('position', 'parent_underlying'),
                           cls.ordered_underlying_parent_info_extra_attr_names)
                info = tuple(map(position_parent_underlying_dict.__getitem__, it))
        return info
    @classmethod
    def make_underlying_leaf(cls,
                             position_parent_underlying_dict):
        info = cls.make_parent_info_from_dict(position_parent_underlying_dict)
        plain = cls.PLAIN_LEAF
        return plain, info

    @class_property
    def num_underlying_parent_info_extra_attrs(cls):
        return len(cls.ordered_underlying_parent_info_extra_attr_names)
    @class_property
    def num_plain_node_extra_attrs(cls):
        return len(cls.ordered_plain_node_extra_attr_names)
    @classmethod
    def make_plain(cls, color, entity, left_plain, right_plain):
        r = cls._make_plain(color, entity, left_plain, right_plain)
        assert len(r) == 4 + cls.num_plain_node_extra_attrs
        return r
    @class_property
    @not_implemented
    def ordered_underlying_parent_info_extra_attr_names(cls):...
    @class_property
    @not_implemented
    def ordered_plain_node_extra_attr_names(cls):...
    #def _make_child_parent_info_at_pos(self, direction):
    @classmethod
    @not_implemented
    def _make_plain(cls, color, entity, left_plain, right_plain):...


class RBT_Node_XTupleBothPlainParented_SizeDepthOrderno_ABC(
    RBT_Node_XTupleBothPlainParented_ABC):
    # why sized?
    #    to support O(1) TreeIteratorComparableTreeNodeABC::is_same_position
    #    size + begin_leaf_orderno ==>> orderno ==>> is_same_position
    # size ::= num nonleaf nodes of subtree rooted by self
    # depth ::= 0 if self is root else self.parent.depth+1
    # orderno ::= num nodes(both nonleaf and leaf) before self in inorder
    # begin_leaf_orderno ::= self.get_first_leaf().orderno
    ordered_underlying_parent_info_extra_attr_names = ('depth', 'begin_leaf_orderno')
    ordered_plain_node_extra_attr_names = ('size',)
    ordered_underlying_parent_info_extra_attr_defaults = (0, 0)
    ordered_plain_node_extra_attr_defaults = (0,)



    @classmethod
    def _underlying_parent_info_extra_getitem(cls, info, extra_index):
        if cls.is_ROOT_PARENT_INFO(info):
            return cls.ordered_underlying_parent_info_extra_attr_defaults[extra_index]

        return info[2 + extra_index]
    @classmethod
    def _plain_extra_getitem(cls, plain, extra_index):
        if cls.is_PLAIN_LEAF(plain):
            return cls.ordered_plain_node_extra_attr_defaults[extra_index]
        return plain[4 + extra_index]
    @classmethod
    def get_underlying_depth(cls, underlying):
        info = cls.get_underlying_parent_info(underlying)
        return cls._underlying_parent_info_extra_getitem(info, 0)
    @classmethod
    def get_underlying_begin_leaf_orderno(cls, underlying):
        info = cls.get_underlying_parent_info(underlying)
        return cls._underlying_parent_info_extra_getitem(info, 1)
    @classmethod
    def get_underlying_size(cls, underlying):
        plain = cls.get_underlying_plain(underlying)
        return cls.get_plain_size(plain)
    @classmethod
    def get_plain_size(cls, plain):
        return cls._plain_extra_getitem(plain, 0)



    @property
    def depth(self):
        return self.get_underlying_depth(self.underlying)
    @property
    def begin_leaf_orderno(self):
        return self.get_underlying_begin_leaf_orderno(self.underlying)
    @property
    def orderno(self):
        if self.is_leaf():
            return self.begin_leaf_orderno
        left_underlying = self.get_underlying_left(self.underlying)
        left_size = self.get_underlying_size(left_underlying)
        num_left_nodes = 2*left_size + 1
        return self.begin_leaf_orderno + num_left_nodes
    @property
    def size(self):
        return self.get_underlying_size(self.underlying)

    def _make_child_parent_info_at_pos(self, direction):
        # direction, self.underlying
        child_depth = self.depth + 1

        # begin_leaf_orderno
        if direction == self.LEFT:
            begin_leaf_orderno = left_begin_leaf_orderno = \
                                 self.begin_leaf_orderno
        else:
            begin_leaf_orderno = right_begin_leaf_orderno = \
                                 self.orderno + 1
        return direction, self.underlying, child_depth, begin_leaf_orderno

    @classmethod
    def _make_plain(cls, color, entity, left_plain, right_plain):
        left_size = cls.get_plain_size(left_plain)
        right_size = cls.get_plain_size(right_plain)
        size = left_size + 1 + right_size
        return color, entity, left_plain, right_plain, size

class RBT_Node_TupleBothPlainParented_ABC(
    RBT_Node_XTupleBothPlainParented_ABC):
    # plain node and underlying_parent_info have no extra attrs
    ordered_underlying_parent_info_extra_attr_names = ()
    ordered_plain_node_extra_attr_names = ()
    @classmethod
    def _make_plain(cls, color, entity, left_plain, right_plain):
        return color, entity, left_plain, right_plain



class RBT_Node_TupleBothPlainParented(
    RBT_Node_Class_Constants_ABC,
    RBT_Node_TupleBothPlainParented_ABC):
    from seed.cases.CLASS import PLAIN_LEAF, ROOT_PARENT_INFO









# cyclic import
from ._insert import insert_entity_at_leaf
from ._remove import remove_leaf_and_its_parent, remove_entity_at_nonleaf
MutableRedBlackTreeNodeABC.insert_entity_at_leaf = insert_entity_at_leaf
MutableRedBlackTreeNodeABC.remove_leaf_and_its_parent = remove_leaf_and_its_parent
MutableRedBlackTreeNodeABC.remove_entity_at_nonleaf = remove_entity_at_nonleaf
del insert_entity_at_leaf
del remove_leaf_and_its_parent, remove_entity_at_nonleaf











def __test_wrapper(cls):
    node = cls.make_leaf_root()
    #print(node.underlying)
    node.underlying
    node = cls.make_red_nonleaf_root(2)
    #print(node)
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












