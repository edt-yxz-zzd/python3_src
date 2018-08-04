
__all__ = '''
    rbt_helper_to_plain__def
    rbt_helper_from_plain__def
    '''.split()


from .copy_from_another_ops_subtree_as_tree__def import \
    copy_from_another_ops_subtree_as_tree__def


RED = 'RED'
BLACK = 'BLACK'
def is_plain_node__fast(plain):
    return type(plain) is tuple and len(plain) in (4, 0)
def is_color(color):
    return color == BLACK or color == RED
def is_plain_node__complete(plain):
    def this(plain):
        if not is_plain_node__fast(plain): return False
        if not plain: return True
        color, entity, left_plain, right_plain = plain
        return is_color(color) and this(left_plain) and this(right_plain)
    return this(plain)

class PlainOps:
    '''
why is plain node?
    plain = () | (color, entity, left_plain, right_plain)
    color = 'RED' | 'BLACK'

why such API?
    see: requires of copy_from_another_ops_subtree_as_tree__def
'''
    __slots__ = ()

    # as input ops
    def is_leaf(ops, plain):
        try:
            assert type(plain) is tuple
            assert len(plain) in (0, 4)
        except AssertionError:
            print(plain)
            raise
        return plain == ()
    def iter_children(ops, plain):
        # precondition: plain is nonleaf
        (color, entity, left_plain, right_plain) = plain
        yield left_plain
        yield right_plain

    def get_the_color(ops, plain):
        # precondition: plain is nonleaf
        return plain[0]
    def get_the_entity(ops, plain):
        # precondition: plain is nonleaf
        return plain[1]
    def is_RED(ops, color):
        if RED == color: return True
        if BLACK == color: return False
        raise TypeError
    '''
    #bug: def is_RED(ops, plain):
    def is_red_node(ops, plain):
        # black leaf
        # black root # but plain node donot know what is root
        if ops.is_leaf(plain): return False
        color = ops.get_the_color(plain)
        return ops.is_RED(color)
    '''



    # as constructor ops
    def make_root_leaf(ops):
        return ()
    def make_root_nonleaf(ops, color, entity, left_child, right_child):
        plain = (color, entity, left_child, right_child)
        return plain
    def get_RED(ops):
        return RED
    def get_BLACK(ops):
        return BLACK

thePlainOps = PlainOps()

def rbt_helper_from_plain__def(to_ops, from_plain):
    # plain = () | (color, entity, left_plain, right_plain)
    # color = 'RED' | 'BLACK'
    #
    # may return a tree with red root
    # which is not a red_black_tree
    #
    # requires:
    #   # see: IRedBlackTreeNodeOps__constructor
    #   to_ops.make_root_leaf
    #   to_ops.make_root_nonleaf
    #   to_ops.get_RED
    #   to_ops.get_BLACK
    #
    assert is_plain_node__complete(from_plain)
    f = copy_from_another_ops_subtree_as_tree__def
    may_red_root = f(to_ops, thePlainOps, from_plain)
    return may_red_root
def rbt_helper_to_plain__def(from_ops, from_node):
    # plain = () | (color, entity, left_plain, right_plain)
    # color = 'RED' | 'BLACK'
    #
    # may return a tree with red root
    # which is not a red_black_tree
    #
    # requires:
    #   # see: IRedBlackTreeNodeOps
    #   from_ops.is_leaf
    #   from_ops.iter_children
    #   from_ops.get_the_color
    #   from_ops.get_the_entity
    #   from_ops.is_RED
    #
    f = copy_from_another_ops_subtree_as_tree__def
    may_red_root_plain = f(thePlainOps, from_ops, from_node)
    assert is_plain_node__complete(may_red_root_plain)
    return may_red_root_plain



