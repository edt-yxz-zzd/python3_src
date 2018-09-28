


'''
see: "def - 2.1. infinite implicit graph.txt"
    implicit graph
        * finite sourced DAG_as_compact_forest
            # need not vertex_eq to avoid parent since DAG

DAG_as_tree_dfs/DAG_as_forest_dfs
    treat DAG as a tree
        so we will not color vertices
    output vertex may be duplicated
        since it or its ancestors may have multiparents
    used at:
        implicit graph dfs
            game state graph dfs    [duplicated states]
            filesystem dfs          [duplicated dirs/files]

    when dfs, we have to hold ancestor_stack or iterator_stack
    * for unparented tree
    * DAG with multiparents # e.g. non-tree
'''


__all__ = '''
IDAG_as_tree_ops__hedge
IDAG_as_tree_ops__vertex_only
DAG_as_tree_ops__vertex_only_mapping
ChildHEdgeEnter
ChildHEdgeExit
DAG_as_tree_dfs__with_leftbias_ancestor_stack
DAG_as_tree_dfs__with_ancestor_seq_view
DAG_as_tree_dfs__with_ancestor_seq
DAG_as_tree_dfs
    '''.split()
from itertools import chain
from abc import ABC, ABCMeta, abstractmethod

from seed.tiny import echo
from ..stack.IMutableStackOps import IMutableOutputViewStackOps
from ..stack.NonExistStackOps import theNonExistStackOps, theSizedNonExistStackOps
from ..stack.SeqAsStackOps import basic_seq_as_stack_ops
from ..stack.convert_PseudoImmutable2MutableStackOps import \
    convert_PseudoImmutable2MutableStackOps, Wrapper
from seed.types.View import SeqView
from ..stack.LeftBiasListAsStackOps import the_left_bias_list_as_stack_ops

wrapped_leftbias_ops = convert_PseudoImmutable2MutableStackOps(
    the_left_bias_list_as_stack_ops
    ,IMutableOutputViewStackOps
    )

'''
class DAG_as_tree_ops__vertex:
    def outgo_vtx2unstable_iter_vertices(self, g, v):pass
NonRootExit
NonRootEnter
too ugly
'''





class IDAG_as_tree_ops__hedge:
    # v->hedge->aedge...u
    # the hedge is child hedge of v
    @abstractmethod
    def outgo_vtx2unstable_iter_hedges(self, g, v):pass
    @abstractmethod
    def hedge2another_vtx(self, g, hedge):pass

class IDAG_as_tree_ops__vertex_only(IDAG_as_tree_ops__hedge):
    # use vtx as hedge
    @abstractmethod
    def outgo_vtx2unstable_iter_vertices(self, g, v):pass
    def outgo_vtx2unstable_iter_hedges(self, g, v):
        return self.outgo_vtx2unstable_iter_vertices(v)
    def hedge2another_vtx(self, g, hedge):
        return hedge
class DAG_as_tree_ops__vertex_only_mapping(DAG_as_tree_ops__vertex_only):
    # g is a mapping {vtx:children}
    def outgo_vtx2unstable_iter_vertices(self, g, v):
        return g[v]



ChildHEdgeEnter = 0
ChildHEdgeExit = 1
def DAG_as_tree_dfs__with_leftbias_ancestor_stack(
        aDAG_as_tree_ops, DAG, root
        , ancestor_hedge_stack_required=True
        , ancestor_vertex_stack_required=True):
    # yield (ChildHEdgeEnter, (hedge, stackH, stackV))
    #     | (ChildHEdgeExit, (None, stackH, stackV))
    #   stackH = stack<ancestor_hedge>
    #   stackV = stack<ancestor_vertex>
    #   stack a = () | (stack a, a)
    # see: DAG_as_tree_dfs
    def f(required):
        if required:
            stack = Wrapper(())
            ops = wrapped_leftbias_ops
            unbox = Wrapper.get_wrapped_obj
        else:
            stack = None
            ops = theNonExistStackOps
            unbox = echo
        return stack, ops
    stackH, opsH, unboxH = f(ancestor_hedge_stack_required)
    stackV, opsV, unboxV = f(ancestor_vertex_stack_required)
    dfs_iter = DAG_as_tree_dfs(
            aDAG_as_tree_ops, DAG, root
            , stackH, opsH
            , stackV, opsV
            )
    for case, may_hedge in dfs_iter:
        yield case, (may_hedge, unboxH(stackH), unboxV(stackV))
def DAG_as_tree_dfs__with_ancestor_seq_view(
        aDAG_as_tree_ops, DAG, root
        , ancestor_hedge_seq_view_required=True
        , ancestor_vertex_seq_view_required=True):
    # output: (dfs_iter, viewH, viewV)
    #   dfs_iter - see: DAG_as_tree_dfs
    #   viewH - ancestor_hedge_seq_view
    #   viewV - ancestor_vertex_seq_view
    # yield (ChildHEdgeEnter, hedge) | (ChildHEdgeExit, None)
    # see: DAG_as_tree_dfs

    def f(required):
        if required:
            seq = []
            ops = basic_seq_as_stack_ops
            view = SeqView(seq)
        else:
            seq = None
            ops = theNonExistStackOps
            view = None
        return seq, ops, view
    seqH, opsH, viewH = f(ancestor_hedge_seq_view_required)
    seqV, opsV, viewV = f(ancestor_vertex_seq_view_required)
    dfs_iter = DAG_as_tree_dfs(
            aDAG_as_tree_ops, DAG, root
            , seqH, opsH
            , seqV, opsV
            )
    return dfs_iter, viewH, viewV



def DAG_as_tree_dfs__with_ancestor_seq(
        aDAG_as_tree_ops, DAG, root
        , ancestor_hedge_seq=None
        , ancestor_vertex_seq=None):
    # yield (ChildHEdgeEnter, hedge) | (ChildHEdgeExit, None)
    # see: DAG_as_tree_dfs
    def f(may_seq):
        return theNonExistStackOps if may_seq is None else basic_seq_as_stack_ops
    ancestor_vertex_stack_ops = f(ancestor_vertex_seq)
    ancestor_hedge_stack_ops = f(ancestor_hedge_seq)

    return DAG_as_tree_dfs(
        aDAG_as_tree_ops, DAG, root
        , ancestor_hedge_stack_ops
            , ancestor_hedge_stack
        , ancestor_vertex_stack_ops
            , ancestor_vertex_stack
        )


def DAG_as_tree_dfs(
    aDAG_as_tree_ops:IDAG_as_tree_ops__hedge
        , DAG, root
    , ancestor_hedge_stack_ops:IMutableOutputViewStackOps
        , ancestor_hedge_stack
    , ancestor_vertex_stack_ops:IMutableOutputViewStackOps
        , ancestor_vertex_stack
    ):
    # yield (ChildHEdgeEnter, hedge) | (ChildHEdgeExit, None)
    # ancestor_vertex_stack can be used as output, too
    #   len(ancestor_vertex_stack)-1 == len(ancestor_hedge_stack)
    #       ancestor_vertex_stack[i]->ancestor_hedge_stack[i]->aedge...
    #       ancestor_hedge_stack[i]->aedge...ancestor_vertex_stack[i+1]
    #
    # push before yield
    # pop after yield
    #
    # stack push order
    #   [hedge->...v->iter_child_hedges]
    #       ->[child_hedge->...target_vtx->target_vtx_iter_child_hedges]
    # stack pop in reverse order

    get_target_vtx = aDAG_as_tree_ops.hedge2another_vtx
    f = aDAG_as_tree_ops.outgo_vtx2unstable_iter_hedges
    def iter_children(v):
        return f(DAG, v)
    def push(hedge):
        ancestor_hedge_stack_ops.push(ancestor_hedge_stack, hedge)
        v = get_target_vtx(hedge)
        ancestor_vertex_stack_ops.push(ancestor_vertex_stack, v)
        iterator_stack.append(iter_children(v))
    def pop():
        iterator_stack.pop()
        ancestor_vertex_stack_ops.pop_None(ancestor_vertex_stack)
        ancestor_hedge_stack_ops.pop_None(ancestor_hedge_stack)

    #ancestor_hedge_stack = []
    #ancestor_hedges_view = SeqView(ancestor_hedge_stack)
    #ancestor_hedges_stack = ()
    iterator_stack = [] # except root's children

    ancestor_vertex_stack_ops.push(root)
    for hedge in iter_children(root):
        # -1+len(ancestor_vertex_stack)
        #   == len(ancestor_hedge_stack)
        #   == len(iterator_stack)
        #
        # push before yield
        # pop after yield
        #
        # stack push order [...v->iter_child_hedges]->[child_hedge->...target_vtx->target_vtx_iter_child_hedges]
        #   stack pop in reverse order
        push(hedge)
        yield ChildHEdgeEnter, hedge
        while iterator_stack:
            for hedge in iterator_stack[-1]:
                # enter hedge
                push(hedge)
                yield ChildHEdgeEnter, hedge
                break
            else:
                # exit hedge
                yield ChildHEdgeExit, None
                pop()
        yield ChildHEdgeExit, None
        pop()
    ancestor_vertex_stack_ops.pop_None()
    return


if __name__ == "__main__":
    import doctest
    doctest.testmod()


