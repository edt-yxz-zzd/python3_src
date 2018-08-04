
__all__ = '''
    ITreeNodeOps
    '''.split()
from .abc import not_implemented
from .ITreeNodeRelated import ITreeNodeRelated
from .IParentInfoOps import IParentInfoOps
from ..TreeNodeOps.depth import verify_depth

from numbers import Integral


pos_inf = float('inf')

class ITreeNodeOps(ITreeNodeRelated):
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


-------------------------------------
methods:
    # type
        `is_leaf
        is_nonleaf
        is_math_tree_leaf
        is_root
        is_nonroot

    # parent_info
        `_get_parent_info_ops_
        `get_parent_info
        get_parent_info_ops
        get_innode_position
        is_ROOT_PARENT_INFO
        get_parent
        get_maybe_parent_innode_position

    # children
        `get_num_children
        `get_child_at
        `unstable_iter_children
        `unstable_iter_innode_position_child_pairs

        static_get_min_num_children_of_nonleaf
        static_get_max_num_children_of_nonleaf_or_inf
        calc_num_nodes_of_subtree
        bottomup_eval_unoriented_subtree
        new_innode_position2child_dict

    # data
        `get_bottomup_auto_data
        `get_impl_data
        `get_usr_data

        get_topdown_auto_data
        get_leaf_impl_data
        get_leaf_usr_data
        get_nonleaf_impl_data
        get_nonleaf_usr_data

'''
    __slots__ = ()

    def static_get_min_num_children_of_nonleaf(ops):
        # min_num_children of any possible nonleaf
        # -> UInt
        return 0
    def static_get_max_num_children_of_nonleaf_or_inf(ops):
        # max_num_children of any possible nonleaf
        # -> UInt | +inf
        return pos_inf
    def basic_eqHashableConstant(ops, lhs, rhs):
        # LEFT/RIGHT/BLACK/RED is hashable constant, must have __eq__
        # ROOT_PARENT_INFO may not be hashable, may not have __eq__
        #
        # return lhs in {rhs}
        if lhs is rhs: return True
        try:
            # hashable, hence __eq__ for same type
            return lhs == rhs
        except:
            # two types not support (==)
            return False
        pass

    @not_implemented
    def _get_parent_info_ops_(ops):
        ...

    def get_parent_info_ops(ops):
        parent_info_ops = ops._get_parent_info_ops_()
        assert isinstance(parent_info_ops, IParentInfoOps)
        return parent_info_ops


    def get_maybe_parent_innode_position(ops, self):
        # -> None | (parent, innode_position)
        return ops.get_parent_info_ops().get_maybe_parent_innode_position(
                    ops.get_parent_info(self))
    def get_topdown_auto_data(ops, self):
        return ops.get_parent_info_ops().get_topdown_auto_data(
                    ops.get_parent_info(self))
    @not_implemented
    def get_bottomup_auto_data(ops, self):
        ...
    @not_implemented
    def get_usr_data(ops, self):
        ...
    @not_implemented
    def get_impl_data(ops, self):
        ...

    # -- return self.parent_info == ROOT_PARENT_INFO
    def is_root(ops, self):
        return ops.is_ROOT_PARENT_INFO(ops.get_parent_info(self))
    def is_nonroot(ops, self):
        return not ops.is_root(self)

    # -- return self.maybe_chilren == nothing
    @not_implemented
    def is_leaf(ops, self):...
    def is_nonleaf(ops, self):
        return not ops.is_leaf(self)
    def is_math_tree_leaf(ops, self):
        # math tree and computer tree are different concepts
        return ops.is_leaf(self) or ops.num_children(self) == 0



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
    @not_implemented
    def get_parent_info(ops, self):
        ...


    #nonroot

    # precondition:
    #    not self.is_root()
    # -- return self.parent_info.parent
    # postcondition:
    #    allow "y.parent is not y.parent", e.g. this is a wrapper class
    def get_parent(ops, self):
        assert not ops.is_root(self)
        return ops.get_parent_info_ops().get_parent(ops.get_parent_info(self))
    # -- return self.parent_info.pos
    def get_innode_position(ops, self):
        assert not ops.is_root(self)
        return ops.get_parent_info_ops().get_innode_position(
                ops.get_parent_info(self))
    @property
    def is_ROOT_PARENT_INFO(ops):
        return ops.get_parent_info_ops().is_ROOT_PARENT_INFO



    # nonleaf

    # precondition:
    #    not self.is_leaf()
    #    no old2new broken below self
    # -- return iter(unjust(self.maybe_children))
    # postcondition:
    #    allow "set(map(id, self.unstable_iter_children())) != set(map(id, self.unstable_iter_children()))"
    #       e.g. this is a wrapper tree
    #           every node is created on-fly
    #   unstable: the order of children is arbitrary since not oriented
    @not_implemented
    def unstable_iter_children(ops, self):
        assert ops.is_nonleaf(self)
        ...
    # def iter_reversed_children??? No, since not oriented

    @not_implemented
    def unstable_iter_innode_position_child_pairs(ops, self):
        assert ops.is_nonleaf(self)
        ...
    def new_innode_position2child_dict(ops, self):
        assert ops.is_nonleaf(self)
        return dict(ops.unstable_iter_innode_position_child_pairs(self))

    # -- return len(unjust(self.maybe_children))
    # ?? nonleaf.num_children == 0 as filesystem.directory??
    @not_implemented
    def get_num_children(ops, self):
        assert ops.is_nonleaf(self)
        ...
    def bottomup_eval_unoriented_subtree(ops, self, on_leaf, on_nonleaf, combine):
        # ops -> node -> (leaf->a) -> (nonleaf->b) -> (b -> unordered[c] -> c) -> c
        unstable_iter_children = ops.unstable_iter_children
        def this(self):
            if ops.is_leaf(self):
                return on_leaf(self)
            return combine(on_nonleaf(self), map(this, unstable_iter_children(self)))
        return this(self)
    #def get_num_nodes_of_subtree(ops, self):
    def calc_num_nodes_of_subtree(ops, self):
        on_node = lambda _: 1
        combine = lambda a, bs: sum(bs, a)
        return ops.bottomup_eval_unoriented_subtree(
                    self, on_node, on_node, combine)
        if ops.is_leaf(self):
            return 1
        return sum(map(ops.calc_num_nodes_of_subtree
                        , ops.unstable_iter_children(self))
                , 1)

    # precondition:
    #    not self.is_leaf()
    #    no old2new broken at (self, pos)
    # -- return unjust(self.maybe_children)[pos]
    @not_implemented
    def get_child_at(ops, self, innode_pos):
        assert ops.is_nonleaf(self)
        ...
    def get_nonleaf_usr_data(ops, self):
        assert ops.is_nonleaf(self)
        return ops.get_usr_data(self)
    def get_nonleaf_impl_data(ops, self):
        assert ops.is_nonleaf(self)
        return ops.get_impl_data(self)




    # leaf
    def get_leaf_usr_data(ops, self):
        assert ops.is_leaf(self)
        return ops.get_usr_data(self)
    def get_leaf_impl_data(ops, self):
        assert ops.is_leaf(self)
        return ops.get_impl_data(self)

    def to_root_of_subtree(ops, self, depth):
        # -> root of subtree
        # see: ITreeNodeOps__imodify.fixed_the_only_broken_above_until_root
        assert verify_depth(depth)
        is_root = ops.is_root
        get_parent = ops.get_parent

        node = self
        while depth != 0 and not is_root(node):
            node = get_parent(node)
            depth -= 1
        return node, depth


    def to_root_of_tree(ops, self):
        # -> root of whole tree
        # == to_root_of_subtree(self, -inf)
        # see: ITreeNodeOps__imodify.fixed_the_only_broken_above_until_root
        is_root = ops.is_root
        get_parent = ops.get_parent

        node = self
        while not is_root(node):
            node = get_parent(node)
        root = node
        return root


    def why_not_static_min_or_max_num_children_ok(ops):
        min_num_children = ops.static_get_min_num_children_of_nonleaf()
        max_num_children = ops.static_get_max_num_children_of_nonleaf_or_inf()

        reasons = set()
        if not isinstance(min_num_children, Integral):
            reasons.add('min_num_children is not Integral')

        if min_num_children < 0:
            reasons.add('min_num_children < 0')

        if isinstance(max_num_children, Integral):
            pass
        elif isinstance(max_num_children, float) and max_num_children == pos_inf:
            pass
        else:
            reasons.add('max_num_children is not Integral or +inf')

        if max_num_children < min_num_children:
            reasons.add('max_num_children < min_num_children')
        return tuple(sorted(reasons))

    def unstable_iter_nodes_of_subtree(ops, self):
        is_leaf = ops.is_leaf
        unstable_iter_children = ops.unstable_iter_children

        iters = [iter([self])]; del self
        while iters:
            it = iters.pop()
            for node in it:
                yield node

                if is_leaf(node):
                    continue
                nonleaf = node; del node
                iters.append(unstable_iter_children(nonleaf))
        return

    def why_not_num_children_ok(ops, self):
        is_leaf = ops.is_leaf
        unstable_iter_children = ops.unstable_iter_children
        get_num_children = ops.get_num_children
        min_num_children = ops.static_get_min_num_children_of_nonleaf()
        max_num_children = ops.static_get_max_num_children_of_nonleaf_or_inf()

        reasons = set()
        stack = [self]; del self
        while stack:
            node = stack.pop()
            if is_leaf(node):
                continue

            nonleaf = node; del node
            num_children = get_num_children(nonleaf)
            if not isinstance(num_children, Integral):
                reasons.add('nonleaf.num_children is not Integral')
            if num_children < min_num_children:
                reasons.add(f'nonleaf.num_children < min_num_children = {min_num_children}')
            if num_children > max_num_children:
                reasons.add(f'nonleaf.num_children > max_num_children = {max_num_children}')


            [*children] = unstable_iter_children(nonleaf)
            if len(children) != num_children:
                reasons.add('len(children) != num_children')

            stack.extend(children)
        return tuple(sorted(reasons))



    def check_subtree(ops, self, **kwargs):
        reasons = ops.why_not_subtree_ok(self, **kwargs)
        if reasons: raise ValueError(reasons)
    def why_not_subtree_ok(ops, self, **kwargs):
        # kwargs readonly, should not remove key from it
        #   i.e. donot override: def is_subtree_ok(ops, self, *, as_root=..., **kwargs)
        #
        # -> reasons
        # -> () | tuple<str>
        return (ops.why_not_static_min_or_max_num_children_ok()
                + ops.why_not_num_children_ok(self)
                )
    def is_subtree_ok(ops, self, **kwargs):
        # kwargs readonly, should not remove key from it
        #   i.e. donot override: def is_subtree_ok(ops, self, *, as_root=..., **kwargs)
        return not ops.why_not_subtree_ok(self, **kwargs)


if __name__ == "__main__":
    XXX = ITreeNodeOps

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)


