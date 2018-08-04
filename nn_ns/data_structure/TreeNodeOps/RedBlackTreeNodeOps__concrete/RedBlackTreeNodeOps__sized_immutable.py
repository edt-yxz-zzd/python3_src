
__all__ = '''
    RedBlackTreeNodeOps__sized_immutable
    theRedBlackTreeNodeOps__sized_immutable
    '''.split()



from .abc import override
#from ..KeyOrderedTreeNodeOps.IKeyOrderedTreeNodeOps__num_entities_of_subtree import \
#    IKeyOrderedTreeNodeOps__num_entities_of_subtree
#from ..KeyOrderedTreeNodeOps.ITotalOrderingOps import ITotalOrderingOps
from ..UnbalancedMultiWayTreeNodeOps.IUnbalancedMultiWayTreeNodeOps__num_entities_of_subtree import \
    IUnbalancedMultiWayTreeNodeOps__num_entities_of_subtree
from ..RedBlackTreeNodeOps.IRedBlackTreeNodeOps__parent_info_plain_node import \
    IRedBlackTreeNodeOps__parent_info_plain_node
from .ParentInfoOps__parent_innode_position import \
    the_ParentInfoOps__parent_innode_position

from collections import namedtuple


# node = (parent_info, plain_node)
PlainNonLeaf = namedtuple('PlainNonLeaf', '''
    num_entities
    color
    entity
    left_plain_child
    right_plain_child
    '''.split())
    # both child are plain!!
class ThePlainLEAF:
    __slots__ = ()
"""
but how?
    immutable and hash
    _replace

class PlainNonLeaf:
    __slots__ = '''
        num_entities
        color
        entity
        left_plain_child
        right_plain_child
        '''.split()
    def __init__(self
                , num_entities:'UInt'
                , color:'RED|BLACK'
                , entity
                , left_plain_child:'ThePlainLEAF|PlainNonLeaf'
                , right_plain_child:'ThePlainLEAF|PlainNonLeaf'
                ):
        self.num_entities = num_entities
        self.color = color
        self.entity = entity
        self.left_plain_child = left_plain_child
        self.right_plain_child = right_plain_child
"""

class LEFT:
    __slots__ = ()
class RIGHT:
    __slots__ = ()

class RED:
    __slots__ = ()
class BLACK:
    __slots__ = ()



class RedBlackTreeNodeOps__sized_immutable(
        IRedBlackTreeNodeOps__parent_info_plain_node
        , IUnbalancedMultiWayTreeNodeOps__num_entities_of_subtree):
    '''

bottomup_auto_data == num_entities


override:
    get_num_entities_of_subtree
    index_nonleaf_entity_position_ex_at

    _get_parent_info_ops_
    basic_update_plain_nonleaf
    get_BLACK
    get_RED
    get_LEFT
    get_RIGHT
    get_bottomup_auto_data_of_plain_leaf
    get_bottomup_auto_data_of_plain_nonleaf
    make_bottomup_auto_data_of_nonleaf
    get_left_plain_child_of_plain_nonleaf
    get_right_plain_child_of_plain_nonleaf
    get_the_color_of_plain_nonleaf
    get_the_entity_of_plain_nonleaf
    is_plain_leaf
    make_plain_leaf
    basic_make_plain_nonleaf
    unNode_to_parent_info_plain_node
    mkNode_from_parent_info_plain_node
'''
    __slots__ = ()

    def _get_parent_info_ops_(ops):
        return the_ParentInfoOps__parent_innode_position
    def basic_update_plain_nonleaf(ops, plain_nonleaf, **kwargs):
        if 'num_entities' in kwargs: raise TypeError
        if 'bottomup_auto_data' in kwargs:
            kwargs['num_entities'] = kwargs.pop('bottomup_auto_data')
        return plain_nonleaf._replace(**kwargs)

    def get_BLACK(ops):
        return BLACK
    def get_RED(ops):
        return RED
    def get_LEFT(ops):
        return LEFT
    def get_RIGHT(ops):
        return RIGHT



    def get_num_entities_of_subtree(ops, self):
        return ops.get_bottomup_auto_data(self)
    def get_bottomup_auto_data_of_plain_leaf(ops, plain_leaf):
        # bottomup_auto_data = num_entities
        assert ops.is_plain_leaf(plain_leaf)
        return 0
    def get_bottomup_auto_data_of_plain_nonleaf(ops, plain_nonleaf):
        # bottomup_auto_data = num_entities
        return plain_nonleaf.num_entities
    def make_bottomup_auto_data_of_nonleaf(ops, left_data, right_data):
        # bottomup_auto_data = num_entities
        left_num_entities = left_data
        right_num_entities = right_data
        self_num_entities_innode = 1
        return left_num_entities + self_num_entities_innode + right_num_entities


    def get_left_plain_child_of_plain_nonleaf(ops, plain_nonleaf):
        return plain_nonleaf.left_plain_child
    def get_right_plain_child_of_plain_nonleaf(ops, plain_nonleaf):
        return plain_nonleaf.right_plain_child
    def get_the_color_of_plain_nonleaf(ops, plain_nonleaf):
        return plain_nonleaf.color
    def get_the_entity_of_plain_nonleaf(ops, plain_nonleaf):
        return plain_nonleaf.entity

    def index_nonleaf_entity_position_ex_at(ops, self, depth, idx):
        return super().index_nonleaf_entity_position_ex_at(self, depth, idx)

    def is_plain_leaf(ops, plain_node):
        return plain_node is ThePlainLEAF

    def make_plain_leaf(ops):
        return ThePlainLEAF
    def basic_make_plain_nonleaf(ops, bottomup_auto_data
            , color, entity, left_plain_child, right_plain_child):
        # donot verify bottomup_auto_data
        num_entities = bottomup_auto_data
        #assert num_entities >= 0
        return PlainNonLeaf(
                num_entities= num_entities
                , color=color
                , entity=entity
                , left_plain_child=left_plain_child
                , right_plain_child=right_plain_child
                )
    def unNode_to_parent_info_plain_node(ops, self):
        parent_info, plain_node = self
        return parent_info, plain_node
    def mkNode_from_parent_info_plain_node(ops, parent_info, plain_node):
        node = parent_info, plain_node
        return node
    @override
    def get_args_for_eq_hash(ops):
        return ()



theRedBlackTreeNodeOps__sized_immutable = RedBlackTreeNodeOps__sized_immutable()

if __name__ == '__main__':
    XXX = RedBlackTreeNodeOps__sized_immutable

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)


