
__all__ = '''
    IRedBlackTreeNodeOps__imodify
    '''.split()

from .abc import not_implemented, override, abstractmethod
from .IRedBlackTreeNodeOps__constructor import IRedBlackTreeNodeOps__constructor
from ..TreeNodeOps.depth import verify_depth
from ..TreeNodeOps.ITreeNodeOps__imodify import ITreeNodeOps__imodify
from .IRedBlackTreeNodeOps__iinsert import \
    red_black_tree__iinsert_entity_at_leaf
from .IRedBlackTreeNodeOps__iremove_entity_at_nonleaf import \
    red_black_tree__iremove_entity_at_nonleaf
from .IRedBlackTreeNodeOps__iremove_leaf_and_its_parent import \
    red_black_tree__iremove_leaf_and_its_parent


class IRedBlackTreeNodeOps__imodify(
        IRedBlackTreeNodeOps__constructor, ITreeNodeOps__imodify):
    '''


require methods:
    # make_ROOT_PARENT_INFO from ITreeNodeOps__constructor
    # make_bare_red_nonleaf from IRedBlackTreeNodeOps__constructor
    `iset_children
    `basic_iset_parent_info
    `iset_the_entity
    `iset_the_color
    irecolor


red_black_tree__itrinode_restructure
    iset_children
    basic_iset_parent_info

red_black_tree__itrinode_restructure__for_double_red_when_uncle_is_black
    +red_black_tree__itrinode_restructure
    irecolor

red_black_tree__iinsert_entity_at_leaf
    +red_black_tree__itrinode_restructure__for_double_red_when_uncle_is_black
    make_bare_red_nonleaf


red_black_tree__ihandle_double_black
    +red_black_tree__itrinode_restructure
    irecolor
    iset_the_color

red_black_tree__iremove_leaf_and_its_parent
    +red_black_tree__ihandle_double_black
    basic_iset_parent_info
    irecolor

red_black_tree__iremove_entity_at_nonleaf
    +red_black_tree__ihandle_double_black
    +red_black_tree__iremove_leaf_and_its_parent
    irecolor
    make_ROOT_PARENT_INFO
    iset_the_entity
    basic_iset_parent_info

'''
    __slots__ = ()

    @not_implemented
    def basic_iset_parent_info(ops, self, parent_info):
        # basic
        #   i.e. not set parent's child at this direction
        # -> new_self
        ...
    @not_implemented
    def iset_the_entity(ops, self, entity):
        # -> new_self
        assert not ops.is_leaf(self)
        ...
    @not_implemented
    def iset_the_color(ops, self, color):
        # -> new_self
        assert not ops.is_leaf(self)
        ...

    def irecolor(ops, self):
        # -> new_self
        assert not ops.is_leaf(self)
        color = ops.get_another_color(self)
        return ops.iset_the_color(self, color)

    @not_implemented
    def basic_iset_left_child(ops, self, left_child):
        # basic
        #   i.e. not set parent's child at this direction
        # -> new_self
        assert not ops.is_leaf(self)
        ...
    @not_implemented
    def basic_iset_right_child(ops, self, right_child):
        # basic
        #   i.e. not set parent's child at this direction
        # -> new_self
        assert not ops.is_leaf(self)
        ...
    def basic_iset_child_at(ops, self, direction, child):
        # basic
        #   i.e. not set parent's child at this direction
        # -> new_self
        assert not ops.is_leaf(self)
        if ops.is_LEFT(direction):
            f = ops.basic_iset_left_child
        else:
            f = ops.basic_iset_right_child
        return f(self, child)

    def basic_iset_parent(ops, self, direction, parent):
        assert not ops.is_leaf(parent)
        parent_info = ops.make_child_parent_info_at_position(parent, direction)
        return ops.basic_iset_parent_info(self, parent_info)

    @abstractmethod
    def basic_iset_children(ops, self, children):
        # basic
        #   i.e. not set parent's child at this direction
        # -> new_self
        assert not ops.is_leaf(self)
        left, right = children
        self = ops.basic_iset_left_child(self, left)
        self = ops.basic_iset_right_child(self, right)
        return self

    def iset_children(ops, self, children):
        # advance
        #   i.e. set children's parent
        assert not ops.is_leaf(self)

        # bottom-up!
        left, right = children
        left = ops.basic_iset_parent(left, ops.get_LEFT(), self)
        right = ops.basic_iset_parent(right, ops.get_RIGHT(), self)

        self = ops.basic_iset_children(self, [left, right])
        return self


    def rbt_iinsert_entity_at_leaf(ops, leaf, entity):
        # -> root
        assert ops.is_leaf(leaf)
        root = red_black_tree__iinsert_entity_at_leaf(ops, leaf, entity)
        return root
    def rbt_iremove_entity_at_nonleaf(
            ops, nonleaf, *, child_leaf_first=True, prefer_succ_leaf=True):
        # -> root
        assert not ops.is_leaf(nonleaf)
        root = red_black_tree__iremove_entity_at_nonleaf(
                ops, nonleaf
                , child_leaf_first=child_leaf_first
                , prefer_succ_leaf=prefer_succ_leaf
                )
        return root
    def rbt_iremove_leaf_and_its_parent(ops, leaf):
        # -> root
        assert ops.is_leaf(leaf)
        root = red_black_tree__iremove_leaf_and_its_parent(ops, leaf)
        return root

    def rbt_irepalce_entity_at_nonleaf(ops, nonleaf, entity):
        # -> root
        assert not ops.is_leaf(nonleaf)
        nonleaf = ops.iset_the_entity(nonleaf, entity)
        root = ops.fixed_the_only_broken_above_until_root(nonleaf)
        return root


    '''
    rbt_iinsert_entity_as_the_first_of_subtree
    rbt_iinsert_entity_as_the_last_of_subtree
    rbt_iinsert_entity_as_the_first_or_last_of_tree
    rbt_iremove_the_first_entity_of_subtree
    rbt_iremove_the_last_entity_of_subtree
    rbt_iremove_the_first_or_last_entity_of_subtree
    '''

    def rbt_iinsert_entity_as_the_first_of_subtree(ops, self, entity):
        # -> root
        return ops.rbt_iinsert_entity_as_the_first_or_last_of_tree(self, entity, False)
    def rbt_iinsert_entity_as_the_last_of_subtree(ops, self, entity):
        # -> root
        return ops.rbt_iinsert_entity_as_the_first_or_last_of_tree(self, entity, True)
    def rbt_iinsert_entity_as_the_first_or_last_of_tree(ops, self, entity, last:bool):
        # -> root
        leaf = ops.get_first_or_last_leaf(self, last)
        return ops.rbt_iinsert_entity_at_leaf(leaf, entity)

    def rbt_iremove_the_first_entity_of_subtree(ops, self):
        # -> root
        return ops.rbt_iremove_the_first_or_last_entity_of_subtree(self, False)
    def rbt_iremove_the_last_entity_of_subtree(ops, self):
        # -> root
        return ops.rbt_iremove_the_first_or_last_entity_of_subtree(self, True)
    def rbt_iremove_the_first_or_last_entity_of_subtree(ops, self, last:bool):
        # -> root
        assert not ops.is_leaf(self)
        leaf = ops.get_first_or_last_leaf(self, last)
        return ops.rbt_iremove_leaf_and_its_parent(leaf)


    def rbt_ipop_the_first_entity_of_subtree(ops, self, last:bool):
        # -> (entity, root) | raise KeyError
        return ops.rbt_ipop_the_first_or_last_entity_of_subtree(self, False)
    def rbt_ipop_the_last_entity_of_subtree(ops, self, last:bool):
        # -> (entity, root) | raise KeyError
        return ops.rbt_ipop_the_first_or_last_entity_of_subtree(self, True)
    def rbt_ipop_the_first_or_last_entity_of_subtree(ops, self, last:bool):
        # -> (entity, root) | raise KeyError
        f = ops.rbt_ipop_the_first_or_last_entity_of_subtree_ex
        does_iremove, payload = f(self, 0, last)
        if does_iremove:
            entity, root = payload
            return entity, root
        raise KeyError('pop empty subtree')

    def rbt_ipop_the_first_or_last_entity_of_subtree_ex(ops, self, depth, last:bool):
        # -> (does_iremove:bool, payload)
        # -> (True, (entity, root)) | (False, (leaf, leaf_depth))
        # self may not be root
        assert verify_depth(depth)
        last = bool(last)

        is_leaf = ops.is_leaf
        get_first_or_last_leaf = ops.get_first_or_last_leaf
        is_root = ops.is_root
        get_parent = ops.get_parent
        get_the_entity = ops.get_the_entity
        rbt_iremove_leaf_and_its_parent = ops.rbt_iremove_leaf_and_its_parent

        if is_leaf(self):
            does_iremove = False
            leaf = self
            leaf_depth = depth
            return does_iremove, (leaf, leaf_depth)

        does_iremove = True
        leaf = get_first_or_last_leaf(self, last)
        assert not is_root(leaf)

        entity = get_the_entity(get_parent(leaf))
        root = rbt_iremove_leaf_and_its_parent(leaf)
        return does_iremove, (entity, root)


if __name__ == '__main__':
    XXX = IRedBlackTreeNodeOps__imodify

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)



