
__all__ = '''
    IRedBlackTreeNodeOps__parent_info_plain_node
    '''.split()



from .abc import not_implemented, abstractmethod, override
from ..RedBlackTreeNodeOps.IRedBlackTreeNodeOps__imodify import \
    IRedBlackTreeNodeOps__imodify



# node = (parent_info, plain_node)
# plain_node = plain_nonleaf | plain_leaf
# plain_nonleaf = (bottomup_auto_data, color, entity, left_plain_child, right_plain_child)




class IRedBlackTreeNodeOps__parent_info_plain_node(
        IRedBlackTreeNodeOps__imodify):
    '''
abstract_methods:
    `_get_parent_info_ops_
    `get_BLACK
    `get_LEFT
    `get_RED
    `get_RIGHT


    `get_the_color_of_plain_nonleaf
    `get_the_entity_of_plain_nonleaf
    `basic_update_plain_nonleaf
    `get_bottomup_auto_data_of_plain_leaf
    `get_bottomup_auto_data_of_plain_nonleaf
    `get_left_plain_child_of_plain_nonleaf
    `get_right_plain_child_of_plain_nonleaf
    `is_plain_leaf
    `make_bottomup_auto_data_of_nonleaf
    `make_plain_leaf
    `make_plain_nonleaf
    `mkNode_from_parent_info_plain_node
    `unNode_to_parent_info_plain_node

new_abstract_methods:
    `unNode_to_parent_info_plain_node
    `mkNode_from_parent_info_plain_node
    `basic_update_plain_nonleaf
    `get_the_color_of_plain_nonleaf
    `get_the_entity_of_plain_nonleaf
    `get_bottomup_auto_data_of_plain_nonleaf
    `get_bottomup_auto_data_of_plain_leaf
    `make_bottomup_auto_data_of_nonleaf
    `get_left_plain_child_of_plain_nonleaf
    `get_right_plain_child_of_plain_nonleaf
    `is_plain_leaf
    `make_plain_leaf
    `basic_make_plain_nonleaf

new_concrete_methods:
    get_bottomup_auto_data_of_plain_node
    update_plain_node_of_nonleaf
    get_plain_node

    make_leaf__from_parent_info
    make_nonleaf__from_parent_info
    make_plain_nonleaf

    # override
    get_the_color_of_nonleaf
    get_the_entity
    get_bottomup_auto_data
    get_parent_info
    basic_iset_parent_info
    copy_subtree_as_tree
    get_left_child
    get_right_child
    is_leaf
    basic_iset_left_child
    basic_iset_right_child
    basic_iset_children
    iset_the_color
    iset_the_entity
    make_child_leaf
    make_root_leaf
    make_child_nonleaf
    make_root_nonleaf

    iter_refresh_downs
    plain_node_to_root
'''
    __slots__ = ()

    @override
    def iter_refresh_downs(ops, self, *directions):
        return super().iter_refresh_downs(self, *directions)

    def plain_node_to_root(ops, plain_node):
        parent_info = ops.make_ROOT_PARENT_INFO()
        node = ops.mkNode_from_parent_info_plain_node(parent_info, plain_node)
        return node

    @abstractmethod
    def unNode_to_parent_info_plain_node(ops, self):
        parent_info, plain_node = self
        return parent_info, plain_node
    @abstractmethod
    def mkNode_from_parent_info_plain_node(ops, parent_info, plain_node):
        node = parent_info, plain_node
        return node

    @not_implemented
    def basic_update_plain_nonleaf(ops, plain_nonleaf, **kwargs):
        # donot eval bottomup_auto_data
        assert not ops.is_plain_leaf(plain_nonleaf)
        assert set(kwargs) <= set('''
            bottomup_auto_data
            color
            entity
            left_plain_child
            right_plain_child
            '''.split())
        raise...
        plain_node = plain_node._replace(**kwargs)
        return plain_node

    @not_implemented
    def get_the_color_of_plain_nonleaf(ops, plain_nonleaf):
        ...
    @not_implemented
    def get_the_entity_of_plain_nonleaf(ops, plain_nonleaf):
        ...

    @override
    def get_the_color_of_nonleaf(ops, self):
        assert not ops.is_leaf(self)
        plain_node = ops.get_plain_node(self)
        return ops.get_the_color_of_plain_nonleaf(plain_node)
    @override
    def get_the_entity(ops, self):
        assert not ops.is_leaf(self)
        plain_node = ops.get_plain_node(self)
        return ops.get_the_entity_of_plain_nonleaf(plain_node)

    @not_implemented
    def get_bottomup_auto_data_of_plain_nonleaf(ops, plain_nonleaf):
        ...
    @not_implemented
    def get_bottomup_auto_data_of_plain_leaf(ops, plain_leaf):
        ...

    @override
    def get_bottomup_auto_data(ops, self):
        plain_node = ops.get_plain_node(self)
        return ops.get_bottomup_auto_data_of_plain_node(plain_node)
    def get_bottomup_auto_data_of_plain_node(ops, plain_node):
        if ops.is_plain_leaf(plain_node):
            return ops.get_bottomup_auto_data_of_plain_leaf(plain_node)
        return ops.get_bottomup_auto_data_of_plain_nonleaf(plain_node)
    def update_plain_node_of_nonleaf(ops, self, **kwargs):
        assert not ops.is_leaf(self)
        nonleaf = self

        assert 'bottomup_auto_data' not in kwargs
        d = {}
        if 'left_plain_child' in kwargs:
            d['left_plain_child'] = kwargs['left_plain_child']
        if 'right_plain_child' in kwargs:
            d['right_plain_child'] = kwargs['right_plain_child']

        parent_info, plain_nonleaf = \
                        ops.unNode_to_parent_info_plain_node(nonleaf)
        if len(d) == 1:
            if 'left_plain_child' not in d:
                left_plain_child = \
                    ops.get_left_plain_child_of_plain_nonleaf(plain_nonleaf)
                d['left_plain_child'] = left_plain_child
            else:
                right_plain_child = \
                    ops.get_right_plain_child_of_plain_nonleaf(plain_nonleaf)
                d['right_plain_child'] = right_plain_child

            assert len(d) == 2

        if d:
            left_data = ops.get_bottomup_auto_data_of_plain_node(
                        d['left_plain_child'])
            right_data = ops.get_bottomup_auto_data_of_plain_node(
                        d['right_plain_child'])
            bottomup_auto_data = ops.make_bottomup_auto_data_of_nonleaf(
                                    left_data, right_data)
            kwargs['bottomup_auto_data'] = bottomup_auto_data

        plain_nonleaf = ops.basic_update_plain_nonleaf(
                                plain_nonleaf, **kwargs)
        node = ops.mkNode_from_parent_info_plain_node(
                                parent_info, plain_nonleaf)
        return node

    @not_implemented
    def make_bottomup_auto_data_of_nonleaf(ops, left_data, right_data):
        # if bottomup_auto_data is num_entities
        left_num_entities = left_data
        right_num_entities = right_data
        self_num_entities_innode = 1
        return left_num_entities + self_num_entities_innode + right_num_entities

    def get_plain_node(ops, self):
        parent_info, plain_node = ops.unNode_to_parent_info_plain_node(self)
        return plain_node

    @override
    def get_parent_info(ops, self):
        parent_info, plain_node = ops.unNode_to_parent_info_plain_node(self)
        return parent_info

    @override
    def basic_iset_parent_info(ops, self, parent_info):
        plain_node = ops.get_plain_node(self)
        node = ops.mkNode_from_parent_info_plain_node(parent_info, plain_node)
        return node





    # self

    @override
    def copy_subtree_as_tree(ops, self):
        # may return a tree with red root
        #   which is not a red_black_tree
        if ops.is_root(self):
            return self
        return ops.basic_iset_parent_info(self, ops.make_ROOT_PARENT_INFO())


    @not_implemented
    def get_left_plain_child_of_plain_nonleaf(ops, nonleaf_plain_node):
        ...
    @not_implemented
    def get_right_plain_child_of_plain_nonleaf(ops, nonleaf_plain_node):
        ...

    @override
    def get_left_child(ops, self):
        # on-fly
        parent_info = ops.make_child_parent_info_at_position(self, ops.get_LEFT())
        self_plain_node = ops.get_plain_node(self)
        left_plain_child = ops.get_left_plain_child_of_plain_nonleaf(self_plain_node)
        left_child = ops.mkNode_from_parent_info_plain_node(parent_info, left_plain_child)
        return left_child

    @override
    def get_right_child(ops, self):
        # on-fly
        parent_info = ops.make_child_parent_info_at_position(self, ops.get_RIGHT())
        self_plain_node = ops.get_plain_node(self)
        right_plain_child = ops.get_right_plain_child_of_plain_nonleaf(self_plain_node)
        right_child = ops.mkNode_from_parent_info_plain_node(parent_info, right_plain_child)
        return right_child



    @not_implemented
    def is_plain_leaf(self, plain_node):
        ...

    @override
    def is_leaf(ops, self):
        plain_node = ops.get_plain_node(self)
        return ops.is_plain_leaf(plain_node)



    @override
    def basic_iset_left_child(ops, self, left_child):
        left_plain_child = ops.get_plain_node(left_child)
        return ops.update_plain_node_of_nonleaf(
                    self, left_plain_child=left_plain_child)
    @override
    def basic_iset_right_child(ops, self, right_child):
        right_plain_child = ops.get_plain_node(right_child)
        return ops.update_plain_node_of_nonleaf(
                    self, right_plain_child=right_plain_child)
    @override
    def basic_iset_children(ops, self, children):
        # basic
        #   i.e. not set parent's child at this direction
        # -> new_self
        left_child, right_child = children

        left_plain_child = ops.get_plain_node(left_child)
        right_plain_child = ops.get_plain_node(right_child)

        return ops.update_plain_node_of_nonleaf(
                    self
                    , left_plain_child=left_plain_child
                    , right_plain_child=right_plain_child
                    )


    @override
    def iset_the_color(ops, self, color):
        return ops.update_plain_node_of_nonleaf(self, color=color)
    @override
    def iset_the_entity(ops, self, entity):
        return ops.update_plain_node_of_nonleaf(self, entity=entity)




    #############

    @override
    def make_child_leaf(ops, parent, direction):
        # postcondition:
        #   old2new broken above:
        #       result
        #           parent -[old2new broken]-> result_leaf
        parent_info = ops.make_child_parent_info_at_position(parent, direction)
        return ops.make_leaf__from_parent_info(parent_info)

    @override
    def make_root_leaf(ops):
        parent_info = ops.make_ROOT_PARENT_INFO()
        return ops.make_leaf__from_parent_info(parent_info)
    def make_leaf__from_parent_info(ops, parent_info):
        plain_node = ops.make_plain_leaf()
        return ops.mkNode_from_parent_info_plain_node(parent_info, plain_node)
    @not_implemented
    def make_plain_leaf(ops):
        ...
    def make_plain_nonleaf(
            ops, color, entity, left_plain_child, right_plain_child):
        left_data = ops.get_bottomup_auto_data_of_plain_node(left_plain_child)
        right_data = ops.get_bottomup_auto_data_of_plain_node(right_plain_child)
        self_data = ops.make_bottomup_auto_data_of_nonleaf(left_data, right_data)
        return ops.basic_make_plain_nonleaf(self_data
                    , color, entity, left_plain_child, right_plain_child)

    @not_implemented
    def basic_make_plain_nonleaf(ops, bottomup_auto_data
            , color, entity, left_plain_child, right_plain_child):
        # donot verify bottomup_auto_data
        ...


    def make_nonleaf__from_parent_info(
            ops, parent_info, color, entity, left_child, right_child):
        left_plain_child = ops.get_plain_node(left_child)
        right_plain_child = ops.get_plain_node(right_child)
        self_plain_node = ops.make_plain_nonleaf(
            color=color
            , entity=entity
            , left_plain_child=left_plain_child
            , right_plain_child=right_plain_child
            )
        return ops.mkNode_from_parent_info_plain_node(parent_info, self_plain_node)

    @override
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
        parent_info = ops.make_child_parent_info_at_position(parent, direction)
        return ops.make_nonleaf__from_parent_info(
                parent_info, color, entity, left_child, right_child)
    @override
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
        parent_info = ops.make_ROOT_PARENT_INFO()
        return ops.make_nonleaf__from_parent_info(
                parent_info, color, entity, left_child, right_child)


if __name__ == '__main__':
    XXX = IRedBlackTreeNodeOps__parent_info_plain_node

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)



