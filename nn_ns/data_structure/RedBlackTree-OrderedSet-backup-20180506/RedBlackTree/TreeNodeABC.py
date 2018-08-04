

'''
bugs:

    @left.setter
    def right(self, x):

TODO:
    max/min_height, size
    OrientedTreeNode : iter_reversed_children??
    BinaryTreeNode : tree_iterator
    RedBlackTreeNode : black_height; check_red_black_tree_properties
'''



__all__ = '''
TreeNodeABC
    MutableTreeNodeABC
    TreeNode_SimpleParentInfo_ParentedSelf_ABC
        MutableTreeNode_SimpleParentInfo_ParentedSelf_ABC
    MutableTreeNodeWrapperABC
        MutableTreeNodeWrapper_NoOtherLeafAttrs_ABC

    OrientedTreeNodeABC
        EqOrientedTreeNodeABC

        OrientedTreeNode_PositiveNumChildren_ABC
            BinaryTreeNodeABC
                MutableBinaryTreeNodeABC
                    MutableBinaryTreeNodeWrapperABC
                        MutableBinaryTreeNodeWrapper_NoOtherLeafAttrs_ABC
                        MutableTreeNodeWrapper_AllUnderlying_ABC
                            MutableTreeNodeWrapper_SimpleParentInfo_ParentedUnderlying_ABC

'''.split()


#from seed.types.ABC import *
from .importABC import ABC, not_implemented
from seed.lang.class_property import class_property
#class_property = classmethod


class TreeNodeABC(ABC):
    '''
in concept:
    ParentInfo a = ROOT_PARENT_INFO
                 | NonrootParentInfo {parent :: TreeNode a,
                                      pos :: TreeNodePos a}
    TreeNodePos a = ??
    TreeNode a = TreeNode{
        parent_info :: ParentInfo a
        maybe_chilren :: Maybe [TreeNode a]
        }

    to illustrate the side effect,
        I use "y.parent_info = parent_info" to represent a python statement
        and "-- y.parent_info = parent_info" to side effect in concept
'''
    @not_implemented
    def copy(self):
        # copy self as a root
        ...

    # -- return self.parent_info == ROOT_PARENT_INFO
    def is_root(self):
        return self.is_ROOT_PARENT_INFO(self.parent_info)
    def is_nonroot(self):
        return not self.is_root()
    # -- return self.maybe_chilren == nothing
    @not_implemented
    def is_leaf(self):...
    def is_nonleaf(self):
        return not self.is_leaf()
    def is_math_tree_leaf(self):
        # math tree and computer tree are different concepts
        return self.is_leaf() or self.num_children == 0

    # any node property

    # the two operations we can perform on parent_info are:
    #    1) save:
    #       info = x.parent_info
    #    2) restore to any node:
    #       y.parent_info = info

    # "... = self.parent_info;"
    # precondition:
    #    no dangling above self
    #    # because we may collect position from self.parent
    #    # but allow old2new broken above self
    # -- return self.parent_info
    @property
    @not_implemented
    def parent_info(self):...


    #nonroot

    # precondition:
    #    not self.is_root()
    # -- return self.parent_info.parent
    # postcondition:
    #    allow "y.parent is not y.parent", e.g. this is a wrapper class
    @property
    def parent(self):
        return self.get_parent_from(self.parent_info)
    # -- return self.parent_info.pos
    @property
    def innode_position(self):
        return self.get_innode_position_from(self.parent_info)


    # nonleaf

    # precondition:
    #    not self.is_leaf()
    #    no old2new broken below self
    # -- return iter(unjust(self.maybe_children))
    # postcondition:
    #    allow "set(map(id, self.iter_children())) != set(map(id, self.iter_children()))"
    @not_implemented
    def iter_children(self):...
    # def iter_reversed_children??? No, since not oriented
    @not_implemented
    def iter_innode_position_child_pairs(self):...
    def new_innode_position2child_dict(self):
        return dict(self.iter_innode_position_child_pairs())
    # -- return len(unjust(self.maybe_children))
    # ?? nonleaf.num_children == 0 as filesystem.directory??
    @property
    @not_implemented
    def num_children(self):...
    # precondition:
    #    not self.is_leaf()
    #    no old2new broken at (self, pos)
    # -- return unjust(self.maybe_children)[pos]
    @not_implemented
    def get_child(self, innode_pos):...




    # -- return parent_info == ROOT_PARENT_INFO
    # NOTE: can not be replaced by "parent_info == cls.new_ROOT_PARENT_INFO()"
    #       since parent_info may not support .__eq__
    @classmethod
    @not_implemented
    def is_ROOT_PARENT_INFO(cls, parent_info):...
    # precondition:
    #    -- parent_info != ROOT_PARENT_INFO
    @classmethod
    @not_implemented
    def get_parent_from(cls, parent_info):...
    @classmethod
    @not_implemented
    def get_innode_position_from(cls, parent_info):...
    # precondition:
    #    -- not self.is_leaf()
    #    allow old2new/new2old/dangling broken below self
    @not_implemented
    def make_child_parent_info_at_pos(self, innode_pos):...
    # -- return ROOT_PARENT_INFO
    # postcondition:
    #    cls.new_ROOT_PARENT_INFO() may or may not return same object
    @classmethod
    @not_implemented
    def new_ROOT_PARENT_INFO(cls):...





class MutableTreeNodeABC(TreeNodeABC):
    @property
    @not_implemented
    def parent_info(self):...
    # "y.parent_info = parent_info"
    # precondition:
    #     allow dangling/old2new broken above y
    #     no new2old broken above y
    #     NOTE : this method may be called in __init__
    #            so, getattr "self.parent_info" is not available
    # -- y.parent_info = parent_info
    # postcondition:
    #    assume y.parent_info and parent_info are both not ROOT_PARENT_INFO
    #    assume y is not leaf
    #    do not update y's new_parent
    #       old2new broken above self
    #    do not update y's old_parent
    #       dangling broken below y's old_parent
    #    do not update y's children
    #       new2old broken below self
    @parent_info.setter
    @not_implemented
    def parent_info(self, x):...


    # precondition:
    #    not self.is_leaf()
    #    pos exists in self
    #    allow new2old/dangling broken below self
    #    no old2new broken below self except at (self, pos)
    #    no new2old broken above self
    # NOTE: update should be performed bottom-up
    # -- child.parent_info = self.make_child_parent_info(pos)
    # -- unjust(self.maybe_children)[pos] = child
    # postcondition:
    #    old2new broken above self
    #    fix a possible dangling/new2old/old2new broken at (self, pos)
    #    new2old broken below child
    @not_implemented
    def set_child(self, innode_pos, child):...




  # fixer
    '''
3 broken types:
    1) tree struct changed
    2) tree struct keeping
        e.g. parent -> me -> child
        me = tree_struct_keeping update
        2-1) old2new broken
            between parent and me
            parent = fix_broken_above(me)
            # but now yield a new2old broken between parent and me
            # see below
        2-2) new2old broken
            between me and child
            child = me.get_child(child.innode_position)


refresh_downs is to handle new2old broken
NOTE:
    we may have a old2new broken tree:
        above x -> above y -> above z
                           -> ...
                -> above w ...
        where x is an proper ancestor of y, and so on
              y is not an ancestor of w and vice versa.


'''

    # "parent = self.refresh_up()"
    #   fix old2new broken above self
    # precondition:
    #     not self.is_root()
    #     allow old2new broken above self
    #     not allow other broken above self
    # -- self.parent.set_child(self.innode_pos, self)
    # -- return self.parent
    # postcondition:
    #     old2new broken above parent
    #     new2old broken below self
    #@abstractmethod
    def refresh_up(self):
        parent = self.parent
        parent.set_child(self.innode_position, self)
        return parent

    # "son, grandson, ... = self.refresh_down(son_pos, grandson_pos, ...)"
    #    fix new2old broken below self
    # precondition:
    #    no other kinds of brokens
    # usage:
    #    e.g. binary tree:
    #         left, = me.refresh_down(me.LEFT) <==> left = me.left
    def refresh_downs(self, *innode_poss):
        for pos in innode_poss:
            self = self.get_child(pos)
            yield self



    # precondition:
    #    there are only one possible broken in the whole tree,
    #       which is a old2new broken above self
    # return root
    # postcondition:
    #    new2old broken between root and self
    def fixed_the_only_broken_above_until_root(self):
        node = self
        while not node.is_root():
            node = node.refresh_up()
        root = node
        return root
    # return root, new_me
    def fixed_the_only_broken_above_until_root__with_new_me(self):
        node = self
        pos_ls = []
        while not node.is_root():
            pos_ls.append(node.innode_position)
            node = node.refresh_up()
        root = node
        pos_ls.reverse()
        *proper_descendants, = root.refresh_downs(*pos_ls)
        assert len(proper_descendants) == len(pos_ls)
        new_me = root if not proper_descendants else proper_descendants[-1]
        return root, new_me
    # return new_me
    def fixed_the_only_broken_above_until_root__refresh_down(self):
        root, new_me = self.fixed_the_only_broken_above_until_root__with_new_me()
        return new_me













class TreeNode_SimpleParentInfo_ParentedSelf_ABC(TreeNodeABC):
    # require ._parent_info
    # parent_info = (direction, parent)
    @property
    def parent_info(self):
        return self._parent_info
    def make_child_parent_info_at_pos(self, pos):
        return pos, self

    @classmethod
    def get_innode_position_from(cls, parent_info):
        return parent_info[0]
    @classmethod
    def get_parent_from(cls, parent_info):
        return parent_info[1]
class MutableTreeNode_SimpleParentInfo_ParentedSelf_ABC(TreeNode_SimpleParentInfo_ParentedSelf_ABC,
                                                        MutableTreeNodeABC):
    # require ._parent_info
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



























class MutableTreeNodeWrapperABC(MutableTreeNodeABC):
    # require underlying node {.underlying}
    # assume both self and underlying_node have {.parent, .direction}
    #    we update both
    #    for a concrete subclass, we simplely skip some update actions



    def __init__(self, underlying_node, parent_info):
        self.underlying = underlying_node
        self.parent_info = parent_info # NOTE: setter called in __init__


    @classmethod
    @not_implemented
    def get_underlying_child_at_pos(cls, nonleaf_underlying, pos):...
    @classmethod
    @not_implemented
    def iter_underlying_children(cls, nonleaf_underlying):...
    @classmethod
    @not_implemented
    def iter_underlying_position_child_pairs(cls, nonleaf_underlying):...
    @classmethod
    def new_innode_position2underlying_child_dict(cls, nonleaf_underlying):
        return dict(cls.iter_underlying_position_child_pairs(nonleaf_underlying))


    @classmethod
    @not_implemented
    def get_underlying_other_nonleaf_attr_dict(cls, nonleaf_underlying):...
    @classmethod
    @not_implemented
    def get_underlying_other_leaf_attr_dict(cls, leaf_underlying):...

    # since not all underlying node types own .parent/.direction
    #    we can return a dict with two possible keys:
    #        position, parent_underlying
    #    which keys miss means they are "Not Available"
    # underlying is root ==>> return {}
    # but return {} ==xx==>> underlying is root
    @classmethod
    @not_implemented
    def get_underlying_position_parent_dict(cls, underlying):...







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
    #   left_underlying,
    #   right_underlying,
    #   position_parent_underlying_dict,
    #   other_nonleaf_attr_dict
    # where position_parent_underlying_dict is
    #      a dict with two possible keys:
    #         position, parent_underlying
    #      if make a root nonleaf,
    #         position_parent_underlying_dict should be empty
    #      but empty not means make a root
    #         it may means nonleaf does not have {.position, .parent}
    @classmethod
    @not_implemented
    def make_underlying_nonleaf(cls,
                                position2underlying_child_dict,
                                position_parent_underlying_dict,
                                **other_nonleaf_attr_dict):...
    @classmethod
    @not_implemented
    def make_underlying_leaf(cls,
                             position_parent_underlying_dict,
                             **other_nonleaf_attr_dict):...
    @classmethod
    def __test_known_keywords__setattr_underlying_nonleaf_node(
        cls, *,
        position_parent_underlying_dict={},
        **other_nonleaf_attr_dict):
        assert set(position_parent_underlying_dict) <= \
               frozenset(['position', 'parent_underlying'])
    @classmethod
    def __test_known_keywords__setattr_underlying_leaf_node(
        cls, *,
        position_parent_underlying_dict={},
        **other_leaf_attr_dict):
        assert set(position_parent_underlying_dict) <= \
               frozenset(['position', 'parent_underlying'])

    # modify old node or create a new node
    # return the modified node or new node
    @classmethod
    def setattr_underlying_nonleaf_node(cls, target_underlying_node,
                                        position2underlying_child_dict={},
                                        **kwds):
        cls.__test_known_keywords__setattr_underlying_nonleaf_node(**kwds)
        d = cls.extract_underlying_nonleaf_data_as_dict(target_underlying_node)
        d['position2underlying_child_dict'].update(position2underlying_child_dict)
        d.update(kwds)
        return cls.make_underlying_nonleaf(**d)
    @classmethod
    def setattr_underlying_leaf_node(cls, target_underlying_node, **kwds):
        cls.__test_known_keywords__setattr_underlying_leaf_node(**kwds)
        d = self.extract_underlying_leaf_data_as_dict(self.underlying)
        others = self.get_underlying_other_leaf_attr_dict(self.underlying)
        others = dict(d['other_leaf_attr_dict'])
        others.update(kwds.get('other_leaf_attr_dict', ()))
        kwds['other_leaf_attr_dict'] = others
        d.update(kwds)
        return cls.make_underlying_leaf(**d)

    # return position2underlying_child_dict,
    #        position_parent_dict, other_nonleaf_attr_dict
    @classmethod
    def extract_underlying_nonleaf_data(cls, underlying):
        return tuple(f(underlying) for f in [
            cls.new_innode_position2underlying_child_dict,
            cls.get_underlying_position_parent_dict,
            cls.get_underlying_other_nonleaf_attr_dict,])
    @classmethod
    def extract_underlying_nonleaf_data_as_dict(cls, underlying):
        position2underlying_child_dict, \
               position_parent_underlying_dict, other_nonleaf_attr_dict = \
               cls.extract_underlying_nonleaf_data(underlying)
        return dict(position2underlying_child_dict = position2underlying_child_dict,
                    position_parent_underlying_dict = position_parent_underlying_dict,
                    **other_nonleaf_attr_dict)
    @classmethod
    def extract_underlying_leaf_data_as_dict(cls, underlying):
        position_parent_underlying_dict = cls.get_underlying_position_parent_dict(underlying)
        other_leaf_attr_dict = cls.get_underlying_other_leaf_attr_dict(underlying)
        return dict(position_parent_underlying_dict=position_parent_underlying_dict,
                    **other_leaf_attr_dict)





    # constructor

    @classmethod
    def from_underlying_node_and_parent_info(cls, underlying, parent_info):
        return cls(underlying, parent_info)


    @classmethod
    def make_underlying_leaf_root(cls, **other_leaf_attr_dict):
        return cls.make_underlying_leaf({}, **other_leaf_attr_dict)

    @classmethod
    def make_leaf_root(cls, **other_leaf_attr_dict):
        underlying = cls.make_underlying_leaf_root(**other_leaf_attr_dict)
        return cls.from_underlying_node_and_parent_info(underlying, cls.new_ROOT_PARENT_INFO())

    @classmethod
    def make_nonleaf_root(cls, pos2child, **other_nonleaf_attr_dict):
        underlying = cls.make_underlying_nonleaf(
            {pos: child.underlying for pos, child in pos2child.items()},
            position_parent_underlying_dict = {}, # root
            **other_nonleaf_attr_dict)
        self = cls.from_underlying_node_and_parent_info(underlying,
                                                        cls.new_ROOT_PARENT_INFO())

        for pos, child in pos2child.items():
            self.set_child(pos, child)
        return self








    def __setattr(self, **kwds):
        self.underlying = self.setattr_underlying_nonleaf_node(self.underlying, **kwds)


    def get_child_at_pos(self, pos):
        info = self.make_child_parent_info_at_pos(pos)
        underlying_child = self.get_underlying_child_at_pos(self.underlying, pos)
        return self.from_underlying_node_and_parent_info(underlying_child, info)
    def set_child_at_pos(self, pos, child):
        # modification should be bottom-up
        # but update .parent top-down

        # first self.children
        self.__setattr(position2underlying_child_dict = {pos: child.underlying})

        # second child.parent
        child.parent_info = self.make_child_parent_info(pos)












































class OrientedTreeNodeABC(TreeNodeABC):
    # iter_children holds order

    @not_implemented
    def iter_reversed_children(self):
        return iter(reversed(self.iter_children))
    @not_implemented
    def iter_innode_positions(self):...
    @not_implemented
    def iter_reversed_innode_positions(self):...
    def iter_innode_position_child_pairs(self):
        return zip(self.iter_children(), self.iter_innode_positions())
    def iter_reversed_innode_position_child_pairs(self):
        return zip(self.iter_reversed_children(),
                   self.iter_reversed_innode_positions())

    @property
    def innode_first_position(self):
        assert not self.is_leaf()
        #assert self.num_children
        for c in self.iter_innode_positions():
            return c
        raise StopIteration('has no children')
    @property
    def innode_last_position(self):
        assert not self.is_leaf()
        #assert self.num_children
        for c in self.iter_reversed_innode_positions():
            return c
        raise StopIteration('has no children')

    @property
    def first_child(self):
        assert not self.is_leaf()
        #assert self.num_children
        for c in self.iter_children():
            return c
        raise StopIteration('has no children')
    @property
    def last_child(self):
        assert not self.is_leaf()
        #assert self.num_children
        for c in self.iter_reversed_children():
            return c
        raise StopIteration('has no children')

##    def nonleaf_nonlast_inorder_succ_leaf(self, nonlast):
##        assert self.is_nonleaf()
##        # since pos exists ==>> num_children > 0
##        #       nonlast exists ==>> first != last ==>> num_children > 1
##        assert self.num_children > 1
##        assert nonlast != self.innode_last_position
class OrientedTreeNode_PositiveNumChildren_ABC(OrientedTreeNodeABC):
    'nonleaf.num_children > 0'
    def get_first_leaf(self):
        while self.is_nonleaf():
            self = self.first_child
        return self
    def get_last_leaf(self):
        while self.is_nonleaf():
            self = self.last_child
        return self
    #def nonleaf_pos_inorder_succ_leaf




class EqOrientedTreeNodeABC(OrientedTreeNodeABC):

    @not_implemented
    def nonleaf_node_eq(self, other):
        assert isinstance(other, __class__)
        assert not self.is_leaf()
        assert not other.is_leaf()
        assert self.num_children == other.num_children
    @not_implemented
    def leaf_node_eq(self, other):
        assert isinstance(other, __class__)
        assert self.is_leaf()
        assert other.is_leaf()

    def oriented_subtree_eq(self, other):
        if self.is_leaf():
            if not other.is_leaf():
                return False
            return self.leaf_node_eq(other)

        if other.is_leaf():
            return False
        if self.num_children != other.num_children or \
           not self.nonleaf_node_eq(other):
            return False

        return all(lchild.oriented_subtree_eq(rchild)
                   for lchild, rchild in
                   zip(self.iter_children(), other.iter_children()))


    pass



class BinaryTreeNodeABC(OrientedTreeNode_PositiveNumChildren_ABC):
  # constant
    # the only two innode_pos values
    @class_property
    @not_implemented
    def LEFT(cls):...
    @class_property
    @not_implemented
    def RIGHT(cls):...


    @property
    @not_implemented
    def left(self):...
    @property
    @not_implemented
    def right(self):...

    # the same as .innode_pos
    # return LEFT/RIGHT
    @property
    def direction(self):
        return self.innode_position
##        return self.get_direction_from(self.parent_info)
##    @classmethod
##    @not_implemented
##    def get_direction_from(cls, parent_info):...
##    @classmethod
##    def get_innode_position_from(cls, parent_info):
##        return cls.direction2innode_position(
##            cls.get_innode_position_from(parent_info))
##    @classmethod
##    def innode_position2direction(cls, pos):
##        # assume 0,1
##        return cls.LEFT if not pos else cls.RIGHT
##
##    @classmethod
##    def direction2innode_position(cls, direction):
##        return 0 if direction == cls.LEFT else 1



    def make_child_parent_info(self, direction):
        return self.make_child_parent_info_at_pos(direction)




    @property
    def children(self):
        return tuple(self.iter_children())


    def iter_children(self):
        yield self.left
        yield self.right
    def iter_reversed_children(self):
        yield self.right
        yield self.left

    def iter_innode_positions(self):
        yield self.LEFT
        yield self.RIGHT
    def iter_reversed_innode_positions(self):
        yield self.RIGHT
        yield self.LEFT

    @property
    def num_children(self):
        assert not self.is_leaf()
        return 2


    def get_child(self, direction):
        return self.left if direction == self.LEFT else self.right


    # nonroot query
    @property
    def sibling(self):
        return self.parent.get_child(self.another_direction)
    @property
    def another_direction(self):
        return self.another_direction_from(self.direction)

    def is_left(self):
        return self.direction == self.LEFT
    def is_right(self):
        return not self.is_left()
    @classmethod
    def another_direction_from(cls, direction):
        return cls.RIGHT if direction == cls.LEFT else cls.LEFT

    @property
    def first_child(self):
        return self.left

    @property
    def last_child(self):
        return self.right


    def nonleaf_inorder_succ_leaf(self):
        assert self.is_nonleaf()
        return self.right.get_first_leaf()
    def nonleaf_inorder_prev_leaf(self):
        assert self.is_nonleaf()
        return self.left.get_last_leaf()

    def leaf_inorder_succ_nonleaf(self):
        assert self.is_leaf()
        while self.is_nonroot():
            if self.is_left():
                return self.parent
            self = self.parent
        else:
            raise StopIteration('self is last leaf of whole tree')

    def leaf_inorder_prev_nonleaf(self):
        assert self.is_leaf()
        while self.is_nonroot():
            if self.is_right():
                return self.parent
            self = self.parent
        else:
            raise StopIteration('self is first leaf of whole tree')
    def leaf_inorder_iter_nodes(self):
        'iter nodes begin at self in inorder till last leaf of whole tree'
        assert self.is_leaf()
        leaf = self
        while True:
            yield leaf
            nonleaf = leaf.leaf_inorder_succ_nonleaf() # may StopIteration
            yield nonleaf
            leaf = nonleaf.nonleaf_inorder_succ_leaf()

    def leaf_inorder_iter_reversed_nodes(self):
        'iter nodes begin at self in inorder till last leaf of whole tree'
        assert self.is_leaf()
        leaf = self
        while True:
            yield leaf
            nonleaf = leaf.leaf_inorder_prev_nonleaf() # may StopIteration
            yield nonleaf
            leaf = nonleaf.nonleaf_inorder_prev_leaf()
    @staticmethod
    def __iter_nodes2iter_nonleaf_nodes(it):
        it = iter(it)
        while True:
            leaf = next(it)
            nonleaf = next(it) # may stop here
            yield nonleaf

    def leaf_inorder_iter_nonleaf_nodes(self):
        # leaf = self.get_first_leaf()
        leaf = self
        it = leaf.leaf_inorder_iter_nodes()
        return self.__iter_nodes2iter_nonleaf_nodes(it)
    def leaf_inorder_iter_reversed_nonleaf_nodes(self):
        #leaf = self.get_last_leaf()
        leaf = self
        it = leaf.leaf_inorder_iter_reversed_nodes()
        return self.__iter_nodes2iter_nonleaf_nodes(it)

class MutableBinaryTreeNodeABC(BinaryTreeNodeABC, MutableTreeNodeABC):
    # the same as get/set_child
    @property
    @not_implemented
    def left(self):...
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

    def set_child(self, direction, node):
        if direction == self.LEFT:
            self.left = node
        else:
            self.right = node






class MutableTreeNodeWrapper_NoOtherLeafAttrs_ABC(MutableTreeNodeWrapperABC):
    @classmethod
    def get_underlying_other_leaf_attr_dict(self, underlying):
        return {}

    @classmethod
    def make_nonleaf_root_with_leaves(cls, positions, **other_nonleaf_attr_dict):
        pos2child = {pos : cls.make_leaf_root() for pos in positions}
        return cls.make_nonleaf_root(pos2child, **other_nonleaf_attr_dict)


class MutableBinaryTreeNodeWrapperABC(MutableTreeNodeWrapperABC,
                                      MutableBinaryTreeNodeABC
                                      ):

    @classmethod
    @not_implemented
    def get_underlying_left(cls, underlying):...
    @classmethod
    @not_implemented
    def get_underlying_right(cls, underlying):...
    @classmethod
    def get_underlying_child_at_pos(cls, underlying, pos):
        f = cls.get_underlying_left if pos == cls.LEFT else cls.get_underlying_right
        return f(underlying)
    @classmethod
    def iter_underlying_children(cls, underlying):
        yield cls.get_underlying_left(underlying)
        yield cls.get_underlying_right(underlying)

    @classmethod
    def iter_underlying_position_child_pairs(cls, underlying):
        return zip((cls.LEFT, cls.RIGHT), cls.iter_underlying_children(underlying))


    @property
    def left(self):
        return self.get_child(self.LEFT)
    @left.setter
    def left(self, x):
        self.set_child(self.LEFT, x)
    @property
    def right(self):
        return self.get_child(self.RIGHT)
    @right.setter
    def right(self, x):
        self.set_child(self.RIGHT, x)

    get_underlying_child = get_underlying_child_at_pos
    def get_child(self, direction):
        return self.get_child_at_pos(direction)
    def set_child(self, direction, child):
        return self.set_child_at_pos(direction, child)

class MutableBinaryTreeNodeWrapper_NoOtherLeafAttrs_ABC(MutableTreeNodeWrapper_NoOtherLeafAttrs_ABC,
                                                        MutableBinaryTreeNodeWrapperABC):
    pass

#MutableBinaryTreeNodeWrapper_NoOtherLeafAttrs_ABC()



class MutableTreeNodeWrapper_AllUnderlying_ABC(MutableTreeNodeWrapperABC):
    # self is the node with no {.direction, .parent}
    # self.underlying is parented node (i.e. with {.direction, .parent})
    # assume parent_info == underlying_parent_info


    @classmethod
    def from_underlying_node(cls, underlying):
        underlying_parent_info = cls.get_underlying_parent_info(underlying)
        parent_info = underlying_parent_info
        return cls.from_underlying_node_and_parent_info(underlying, parent_info)



    @classmethod
    def get_underlying_position_parent_dict(cls, underlying):
        underlying_parent_info = cls.get_underlying_parent_info(underlying)
        if cls.is_root_underlying_parent_info(underlying_parent_info):
            return {}
        parent_underlying = cls.get_underlying_parent_from(underlying_parent_info)
        position = cls.get_underlying_position_from(underlying_parent_info)
        return dict(parent_underlying=parent_underlying, position=position)

    @classmethod
    @not_implemented
    def get_underlying_parent_from(cls, underlying_parent_info):...
    @classmethod
    @not_implemented
    def get_underlying_position_from(cls, underlying_parent_info):...

    @classmethod
    @not_implemented
    def get_underlying_parent_info(cls, underlying):...

    # return the modified underlying node or new one
    @classmethod
    @not_implemented
    def set_underlying_parent_info(cls, underlying, underlying_parent_info):...
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




class MutableTreeNodeWrapper_SimpleParentInfo_ParentedUnderlying_ABC(
    MutableTreeNodeWrapper_AllUnderlying_ABC):
    # self.parent_info = underlying_parent_info = direction, parent_underlying, extra attrs...
    # is_root_underlying_parent_info
    # get_underlying_parent_info
    # set_underlying_parent_info



    @property
    def parent_info(self):
        return self.get_underlying_parent_info(self.underlying)
    @parent_info.setter
    def parent_info(self, parent_info):
        # cripple_parent
        underlying_parent_info = parent_info
        if not self.is_root_underlying_parent_info(underlying_parent_info):
            assert len(underlying_parent_info) >= 2
        self.underlying = self.set_underlying_parent_info(self.underlying, underlying_parent_info)

    # override me to pack extra attrs. e.g. depth, order_number_in_whole_tree
    num_underlying_parent_info_extra_attrs = 0
    def _make_child_parent_info_at_pos(self, direction):
        return direction, self.underlying
    def make_child_parent_info_at_pos(self, direction):
        r = self._make_child_parent_info_at_pos(direction)
        assert len(r) == 2 + self.num_underlying_parent_info_extra_attrs
        return r

    @classmethod
    def get_innode_position_from(cls, parent_info):
        return parent_info[0]
    @classmethod
    def get_parent_from(cls, parent_info):
        parent_underlying = parent_info[1]
        parent_info_of_parent = underlying_parent_info_of_parent\
                              = cls.get_underlying_parent_info(parent_underlying)
        return cls.from_underlying_node_and_parent_info(parent_underlying, parent_info_of_parent)



