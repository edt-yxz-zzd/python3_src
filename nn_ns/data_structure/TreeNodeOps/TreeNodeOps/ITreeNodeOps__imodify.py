

__all__ = '''
    ITreeNodeOps__imodify
    '''.split()
from .abc import not_implemented
from .ITreeNodeOps import ITreeNodeOps


class ITreeNodeOps__imodify(ITreeNodeOps):
    '''

new methods:
    `basic_iset_parent_info
    `basic_iset_child_at
    `iter_refresh_downs

    refresh_up
    fixed_the_only_broken_above_until_root
    fixed_the_only_broken_above_until_root__with_new_me
    fixed_the_only_broken_above_until_root__refresh_down
'''
    __slots__ = ()

    # get_parent_info in ITreeNodeOps


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
    @not_implemented
    def basic_iset_parent_info(ops, self, parent_info):...


    # precondition:
    #    not self.is_leaf()
    #    pos/innode_position exists in self
    #    allow new2old/dangling broken below self
    #    no old2new broken below self except at (self, pos)
    #    no new2old broken above self
    # NOTE: update should be performed bottom-up
    #       and then iter_refresh_downs to update topdown_auto_data(depth)
    # -- ????child.parent_info = self.make_child_parent_info(pos)????
    #       new verion donot update child.parent_info
    # -- unjust(self.maybe_children)[pos] = child
    # postcondition:
    #    old2new broken above self
    #    fix a possible dangling/new2old/old2new broken at (self, pos)
    #    new2old broken below child
    @not_implemented
    def basic_iset_child_at(ops, self, innode_position, child):
        # modify self only
        # donot modify child and self.children[innode_position]
        ...




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
            child = me.get_child_at(child.innode_position)


iter_refresh_downs is to handle new2old broken
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
    # -- self.parent.basic_iset_child_at(self.innode_pos, self)
    # -- return self.parent
    # postcondition:
    #   old2new broken above parent
    #   new2old broken below self
    #   # why?
    #   #   for mutable node: self is final, so OK
    #   #   for immutable node: self_subtree is final, so OK
    #   #       node = (new_parent_info, self_subtree) is on-fly, so OK
    #   #       BUT self = (old_parent_info, self_subtree) is BAD!!!!
    #   #       ...
    #   #   for wrapper node: since is mutable/immutable node
    def refresh_up(ops, self):
        assert not ops.is_root(self)
        parent = ops.get_parent(self)
        innode_position = ops.get_innode_position(self)
        parent = ops.basic_iset_child_at(parent, innode_position, self)
        return parent

    # "son, grandson, ... = self.refresh_down(son_pos, grandson_pos, ...)"
    #    fix new2old broken below self
    # precondition:
    #    no other kinds of brokens
    # usage:
    #    e.g. binary tree:
    #         left, = me.refresh_down(me.LEFT) <==> left = me.left
    @not_implemented
    def iter_refresh_downs(ops, self, *innode_positions):
        # impl for wrapper node
        node = self
        for pos in innode_positions:
            node = ops.get_child_at(node, pos)
            yield node



    # precondition:
    #    there are only one possible broken in the whole tree,
    #       which is a old2new broken above self
    # return root
    # postcondition:
    #    new2old broken between root and self
    def fixed_the_only_broken_above_until_root(ops, self):
        node = self
        while not ops.is_root(node):
            node = ops.refresh_up(node)
        root = node
        return root

    # return root, new_me
    def fixed_the_only_broken_above_until_root__with_new_me(ops, self):
        node = self
        innode_positions = []
        while not ops.is_root(node):
            innode_positions.append(ops.get_innode_position(node))
            node = ops.refresh_up(node)
        root = node
        innode_positions.reverse()
        *proper_descendants, = ops.iter_refresh_downs(root, *innode_positions)
        assert len(proper_descendants) == len(innode_positions)
        new_me = root if not proper_descendants else proper_descendants[-1]
        return root, new_me

    # return new_me
    def fixed_the_only_broken_above_until_root__refresh_down(ops, self):
        root, new_me = ops.fixed_the_only_broken_above_until_root__with_new_me(self)
        return new_me




if __name__ == '__main__':
    XXX = ITreeNodeOps__imodify

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)




