

__all__ = '''
    IRedBlackTreeNodeOps
    '''.split()

from .abc import not_implemented, override, abstractmethod
#from ..KeyOrderedTreeNodeOps.IKeyOrderedBinaryTreeNodeOps import \
#    IKeyOrderedBinaryTreeNodeOps
from ..UnbalancedMultiWayTreeNodeOps.IBinaryTreeNodeOps import\
    IBinaryTreeNodeOps
from itertools import chain

from .rbt_helper_to_or_from_plain__def import rbt_helper_to_plain__def



#class IRedBlackTreeNodeOps(IKeyOrderedBinaryTreeNodeOps):
class IRedBlackTreeNodeOps(IBinaryTreeNodeOps):
    '''

entity == nonleaf_usr_data
None == leaf_usr_data
color == impl_data

RED/BLACK(like LEFT/RIGHT) will be used as key in dict ==>> hashable and __eq__

RedBlackTree_Property:
    Root Property:
        The root is black.
    External Property:
        Every external node is black.
    Internal Property:
        The children of a red node are black.
    Depth Property:
        All the external nodes have the same black height,
        defined as the number of black ancestors minus one.
        (Recall that a node is an ancestor of itself.)



##############
new_abstract_methods:
    `get_RED
    `get_BLACK
    `get_the_color_of_nonleaf
    `get_the_entity
new_concrete_methods:
    # color
    is_RED
    is_BLACK

    # any node query
    another_color_of
    get_the_color
    get_another_color
    is_red_node
    is_black_node

    # data
    get_impl_data
    get_usr_data


    # property
    check_red_black_tree_properties
    holds_red_black_tree_properties
    holds_red_black_tree__RootProperty
    holds_red_black_tree__ExternalProperty
    holds_red_black_tree__InternalProperty
    holds_red_black_tree__DepthProperty
    get_all_black_heights_of_subtree
    get_arbitrary_one_black_height

    rbt_helper_to_direction_path
    rbt_helper_to_direction_path_ex
    rbt_helper_to_plain
'''
    __slots__ = ()

    @not_implemented
    def get_RED(ops):...
    @not_implemented
    def get_BLACK(ops):...

    def is_RED(ops, color):
        # return color == ops.get_RED()
        RED = ops.get_RED()
        eq = ops.basic_eqHashableConstant

        if eq(color, RED): return True

        BLACK = ops.get_BLACK()
        if eq(color, BLACK): return False
        raise TypeError
    def is_BLACK(ops, color):
        return not ops.is_RED(color)


    @not_implemented
    def get_the_color_of_nonleaf(ops, self):
        assert not ops.is_leaf(self)
        ...

    def another_color_of(ops, color):
        return ops.get_BLACK() if ops.is_RED(color) else ops.get_RED()

    @not_implemented
    def get_the_entity(ops, self):
        assert not ops.is_leaf(self)
        ...


    def rbt_helper_to_direction_path(ops, self):
        # -> [direction]
        # direction = 'LEFT' | 'RIGHT'
        path_ex = ops.rbt_helper_to_direction_path_ex(self)
        path = [direction for _, _, direction in path_ex]
        return path
    def rbt_helper_to_direction_path_ex(ops, self):
        # -> [(color, entity, child_direction)]
        # direction = 'LEFT' | 'RIGHT'
        # color = 'RED' | 'BLACK'
        is_root = ops.is_root
        get_parent = ops.get_parent
        get_direction = ops.get_direction
        is_LEFT = ops.is_LEFT
        is_red_node = ops.is_red_node
        get_the_entity = ops.get_the_entity

        path_ex = [] # (parent.color, parent.entity, direction)
        node = self
        while not is_root(node):
            parent = get_parent(node)
            direction = get_direction(node)
            direction = 'LEFT' if is_LEFT(direction) else 'RIGHT'

            color = 'RED' if is_red_node(parent) else 'BLACK'
            entity = get_the_entity(parent)
            path_ex.append((color, entity, direction))

            node = parent

        path_ex.reverse()
        return path_ex


    def rbt_helper_to_plain(ops, self):
        # plain = () | (color, entity, left_plain, right_plain)
        # color = 'RED' | 'BLACK'
        #
        # may return red plain node
        return rbt_helper_to_plain__def(ops, self)

        # old version
        is_leaf = ops.is_leaf
        is_red_node = ops.is_red_node
        get_the_entity = ops.get_the_entity
        get_left_child = ops.get_left_child
        get_right_child = ops.get_right_child

        def this(self):
            if ops.is_leaf(self):
                return ()
            left_plain = this(get_left_child(self))
            right_plain = this(get_right_child(self))
            color = 'RED' if is_red_node(self) else 'BLACK'
            entity = get_the_entity(self)
            return color, entity, left_plain, right_plain
        return this(self)

    # any node query
    def get_the_color(ops, self):
        if ops.is_leaf(self):
            return ops.get_BLACK()
        return ops.get_the_color_of_nonleaf(self)
    def get_another_color(ops, self):
        return ops.another_color_of(ops.get_the_color(self))
    def is_red_node(ops, self):
        return ops.is_RED(ops.get_the_color(self))
    def is_black_node(ops, self):
        return not ops.is_red_node(self)


    # data
    # get_bottomup_auto_data
    # get_parent_info
    def get_impl_data(ops, self):
        return ops.get_the_color(self)
    def get_usr_data(ops, self):
        if ops.is_leaf(self):
            return None
        return ops.get_the_entity(self)



    # property
    def check_red_black_tree_properties(ops, self, as_root:bool):
        'see: RedBlackTree_Property'
        reasons = ops.why_not_holds_red_black_tree_properties(self, as_root)
        if reasons: raise ValueError(reasons)
        return None

    @override
    def why_not_subtree_ok(ops, self, **kwargs):
        # kwargs readonly, should not remove key from it
        #   i.e. donot override: def is_subtree_ok(ops, self, *, as_root=..., **kwargs)
        return (ops.why_not_holds_red_black_tree_properties(
                    self, kwargs['as_root'])
                + super().why_not_subtree_ok(self, **kwargs)
                )

    def why_not_holds_red_black_tree_properties(ops, self, as_root):
        # -> reasons
        reasons0 = ops.why_not_holds_red_black_tree__RootProperty(self, as_root)
        reasons1 = ops.why_not_holds_red_black_tree__ExternalProperty(self)
        reasons2 = ops.why_not_holds_red_black_tree__InternalProperty(self)
        reasons3 = ops.why_not_holds_red_black_tree__DepthProperty(self)
        return tuple(chain(reasons0, reasons1, reasons2, reasons3))

    def holds_red_black_tree_properties(ops, self, as_root):
        fs = (ops.holds_red_black_tree__ExternalProperty
             ,ops.holds_red_black_tree__InternalProperty
             ,ops.holds_red_black_tree__DepthProperty
             )
        return (ops.holds_red_black_tree__RootProperty(self, as_root)
            and all(f(self) for f in fs)
            )


    def holds_red_black_tree__RootProperty(ops, self, as_root):
        if as_root:
            # self will be root
            return ops.is_black_node(self)
        return True # pass since self will be not root

    def why_not_holds_red_black_tree__RootProperty(ops, self, as_root):
        # -> reasons
        # -> args
        if not ops.holds_red_black_tree__RootProperty(self, as_root):
            return ('red root',)
        return ()

    def holds_red_black_tree__ExternalProperty(ops, self):
        # to be overrided: return True
        #       since leaf node contains no color
        leaf_nodes = ops.iter_leaf_nodes_of_subtree(self)
        return all(map(ops.is_black_node, leaf_nodes))
    def why_not_holds_red_black_tree__ExternalProperty(ops, self):
        # -> reasons
        if not ops.holds_red_black_tree__ExternalProperty(self):
            return ('red leaf',)
        return ()

    def holds_red_black_tree__InternalProperty(ops, self):
        def one_layer(nonleaf):
            return (ops.is_black_node(nonleaf)
                or all(map(ops.is_black_node, ops.iter_children(nonleaf)))
                )

        nodes = [self]; del self
        while nodes:
            node = nodes.pop()
            if ops.is_leaf(node):
                continue
            if not one_layer(node): return False

            nodes.extend(ops.iter_children(node))
        # bugs: forgot "return True"
        return True

    def why_not_holds_red_black_tree__InternalProperty(ops, self):
        # -> reasons
        if not ops.holds_red_black_tree__InternalProperty(self):
            return ('double red',)
        return ()
    def why_not_holds_red_black_tree__DepthProperty(ops, self):
        # -> reasons
        if not ops.holds_red_black_tree__DepthProperty(self):
            return ('black height not all the same',)
        return ()


    def holds_red_black_tree__DepthProperty(ops, self):
        return len(ops.get_all_black_heights_of_subtree(self)) == 1

    def get_all_black_heights_of_subtree(ops, self, *, pseudo_parent_black_height=0):
        # black_height is not height!!
        def is_black_node(node):
            return node2self_black_count(ops, node)
        iter_children = ops.iter_children
        is_leaf = ops.is_leaf

        black_heights = set()
        black_height = is_black_node(self) # + pseudo_parent_black_height
        node_black_height_pairs = [(self, black_height)]
        while node_black_height_pairs:
            node, black_height = node_black_height_pairs.pop()
            if is_leaf(node):
                black_heights.add(black_height)
                continue

            for child in iter_children(node):
                child_black_height = black_height + is_black_node(child)
                node_black_height_pairs.append((child, child_black_height))

        if pseudo_parent_black_height:
            black_heights = {pseudo_parent_black_height+d for d in black_heights}
        assert ops.get_arbitrary_one_black_height(
                    self, pseudo_parent_black_height=pseudo_parent_black_height
                ) in black_heights
        return black_heights



    def get_arbitrary_one_black_height(ops, self, *, pseudo_parent_black_height=0):
        def is_black_node(node):
            return node2self_black_count(ops, node)
        is_leaf = ops.is_leaf
        get_child = ops.get_left_child

        node = self
        black_height = is_black_node(node)
        while not is_leaf(node):
            node = get_child(node)
            black_height += is_black_node(node)
        black_height += pseudo_parent_black_height
        return black_height




def node2self_black_count(ops, node):
    return int(bool(ops.is_black_node(node)))

if __name__ == '__main__':
    XXX = IRedBlackTreeNodeOps

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)




