
__all__ = '''
    IRedBlackTreeNodeOps__constructor
    '''.split()

from .abc import not_implemented, override, abstractmethod
from .IRedBlackTreeNodeOps import IRedBlackTreeNodeOps
from ..TreeNodeOps.ITreeNodeOps__constructor import \
    ITreeNodeOps__constructor
from ..TreeNodeOps.depth import verify_depth
from .IRedBlackTreeNodeOps__from_entities import \
    red_black_tree__from_entities

import operator


from .copy_from_another_ops_subtree_as_tree__def import \
    copy_from_another_ops_subtree_as_tree__def
from .rbt_helper_to_or_from_plain__def import rbt_helper_from_plain__def

class IRedBlackTreeNodeOps__constructor(
    IRedBlackTreeNodeOps, ITreeNodeOps__constructor):
    '''

new_abstract_methods:
    `make_child_leaf
    `make_root_leaf
    `make_child_nonleaf
    `make_root_nonleaf

    copy_from_another_ops_subtree_as_tree
    verify_result_of_copy_from_another_red_black_tree

    rbt_from_entities
    rbt_from_reversed_entities
    rbt_helper_from_plain
'''
    __slots__ = ()

    @not_implemented
    def make_child_leaf(ops, parent, direction):
        # postcondition:
        #   old2new broken above:
        #       result
        #           parent -[old2new broken]-> result_leaf
        ...
    @not_implemented
    def make_root_leaf(ops):
        ...

    @not_implemented
    def make_child_nonleaf(ops, parent, direction, color, entity, left_child, right_child):
        # result.parent := parent
        # result.direction := direction
        # result.topdown_auto_data := ...
        # result.bottomup_auto_data := ...
        # result.color := color
        # result.entity := entity
        #
        # left_child.parent := result
        # left_child.direction := LEFT
        # right_child.parent := result
        # right_child.direction := RIGHT
        #
        # postcondition:
        #   old2new broken above:
        #       result
        #           parent.get_child_at(direction) may not be result
        #           e.g. may have two nodes whose parent and direction are the same
        #   dangling broken below:
        #       left_child.old_parent if any
        #       right_child.old_parent if any
        ...
    @not_implemented
    def make_root_nonleaf(ops, color, entity, left_child, right_child):
        # although root should be BLACK
        # the result root will be inserted as nonroot (root of subtree) or recolored
        #
        #
        # result.bottomup_auto_data := ...
        # result.color := color
        # result.entity := entity
        #
        # left_child.parent := result
        # left_child.direction := LEFT
        # right_child.parent := result
        # right_child.direction := RIGHT
        #
        # postcondition:
        #   dangling broken below:
        #       left_child.old_parent if any
        #       right_child.old_parent if any
        ...



    def make_empty_tree(ops):
        return ops.make_root_leaf()

    # get_maybe_parent_direction
    def make_leaf_from_maybe_parent_direction(ops, maybe_parent_direction):
        if maybe_parent_direction is None:
            return ops.make_root_leaf()

        parent, direction = maybe_parent_direction
        return ops.make_child_leaf(parent, direction)
    def make_nonleaf__from_maybe_parent_direction(ops, maybe_parent_direction, color, entity, left_child, right_child):
        if maybe_parent_direction is None:
            # color may be not BLACK
            return ops.make_root_nonleaf(color, entity, left_child, right_child)

        parent, direction = maybe_parent_direction
        return ops.make_child_nonleaf(parent, direction, color, entity, left_child, right_child)



    def make_bare_red_nonleaf(ops, maybe_parent_direction, entity):
        # bare - children are all leaves
        #
        # when maybe_parent_direction is None:
        #   although root should be BLACK
        #   the result root will be inserted as nonroot (root of subtree) or recolored
        left_child = ops.make_empty_tree()
        right_child = ops.make_empty_tree()
        RED = ops.get_RED()
        return ops.make_nonleaf__from_maybe_parent_direction(
            maybe_parent_direction, RED, entity, left_child, right_child)


    def verify_result_of_copy_from_another_red_black_tree(
            ops, node, another_ops, another_node, *, entity_eq=None):

        if entity_eq is None:
            entity_eq = operator.is_
        o_is_leaf = ops.is_leaf
        o_iter_children = ops.iter_children
        o_is_red_node = ops.is_red_node
        o_get_the_entity = ops.get_the_entity

        a_is_leaf = another_ops.is_leaf
        a_iter_children = another_ops.iter_children
        a_is_red_node = another_ops.is_red_node
        a_get_the_entity = another_ops.get_the_entity

        def bool_eq(lhs, rhs):
            return bool(lhs) == bool(rhs)

        stack = [(node, another_node)]
        while stack:
            node, another_node = stack.pop()
            if not bool_eq(o_is_leaf(node), a_is_leaf(another_node)):
                return False
            if o_is_leaf(node):
                continue

            if not bool_eq(o_is_red_node(node), a_is_red_node(another_node)):
                return False
            if not entity_eq(o_get_the_entity(node)
                            , a_get_the_entity(another_node)):
                return False
            o_children = o_iter_children(node)
            a_children = a_iter_children(another_node)
            stack.extend(zip(o_children, a_children))
        return True

    def copy_from_another_ops_subtree_as_tree(ops, another_ops, another_node):
        # may return a tree with red root
        #   which is not a red_black_tree
        try:
            b_eq = ops == another_ops
        except:
            pass
        else:
            return another_ops.copy_subtree_as_tree(another_node)
        return copy_from_another_ops_subtree_as_tree__def(
                ops, another_ops, another_node)
    def rbt_helper_from_plain(ops, plain):
        # plain = () | (color, entity, left_plain, right_plain)
        # color = 'RED' | 'BLACK'
        return rbt_helper_from_plain__def(ops, plain)

    def rbt_from_reversed_entities(ops, num_entities, entities, *
            , pseudo_parent_is_black=False
            , black_height_of_subtree=None # >= 1
            , more_than_num_entities=False
            , reverse=False
            ):
        # -> subtree | raise ValueError
        #   result subtree may with RED root if pseudo_parent_is_black=True
        return ops.rbt_from_entities(
            num_entities, entities
            , black_height_of_subtree=black_height_of_subtree
            , pseudo_parent_is_black = bool(pseudo_parent_is_black)
            , more_than_num_entities=bool(more_than_num_entities)
            , reverse=not bool(reverse)
            )

    def rbt_from_entities(ops, num_entities, entities, *
            , pseudo_parent_is_black=False
            , black_height_of_subtree=None # >= 1
            , more_than_num_entities=False
            , reverse=False
            ):
        # -> subtree | raise ValueError
        #   result subtree may with RED root if pseudo_parent_is_black=True

        assert num_entities >= 0
        black_height_of_subtree, subtree = red_black_tree__from_entities(
            ops, num_entities, entities
            , black_height_of_subtree=black_height_of_subtree
            , pseudo_parent_is_black = bool(pseudo_parent_is_black)
            , more_than_num_entities=bool(more_than_num_entities)
            , reverse=bool(reverse)
            )
        return subtree




if __name__ == '__main__':
    XXX = IRedBlackTreeNodeOps__constructor

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)




