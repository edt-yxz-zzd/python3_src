
__all__ = '''
    dfs__ugraph_fake_embedding
    DFS_Case
    '''.split()

import operator

if False:
    from ..dfs.dfs__finite_explicit_ugraph import (
        dfs__finite_explicit_ugraph
        ,DFS_Case
        ,DFS_CaseParts
        ,Vertex2TwoColor__seq
        ,make_hedge2unstable_iter_other_hedges_around_another_vertex
        )
else:
    from .imports import dfs__finite_explicit_ugraph as _x
    dfs__finite_explicit_ugraph = _x.dfs__finite_explicit_ugraph
    DFS_Case = _x.DFS_Case
    DFS_CaseParts = _x.DFS_CaseParts
    Vertex2TwoColor__seq = _x.Vertex2TwoColor__seq
    make_hedge2unstable_iter_other_hedges_around_another_vertex = _x.make_hedge2unstable_iter_other_hedges_around_another_vertex
    del _x


def dfs__ugraph_fake_embedding(*
    ,ugraph_fake_embedding
    ,is_clockwise_around_fvertex:bool
    ,maybe_ancestor_hedge_stack = None
    ,maybe_ancestor_vertex_stack = None
    ):
    all_fvertices = range(ugraph_fake_embedding.num_fvertices)
    vertex2color = Vertex2TwoColor__seq([False]*ugraph_fake_embedding.num_fvertices, True)

    is_clockwise_around_fvertex = bool(is_clockwise_around_fvertex)
    _vertex2iter_hedges = ugraph_fake_embedding.fvertex2iter_fake_clockwise_hedges
    def vertex2iter_hedges(vertex):
        return _vertex2iter_hedges(vertex, reverse=not is_clockwise_around_fvertex)
    def hedge2another_vertex(hedge):
        return ugraph_fake_embedding.hedge2fvertex[ugraph_fake_embedding.hedge2another_hedge(hedge)]

    if is_clockwise_around_fvertex:
        hedge2next = ugraph_fake_embedding.hedge2fake_clockwise_next_hedge_around_vertex
    else:
        hedge2next = ugraph_fake_embedding.hedge2fake_clockwise_prev_hedge_around_vertex
    hedge2others_around_another_fvertex = (
        make_hedge2unstable_iter_other_hedges_around_another_vertex
        .from_hedge2next_hedge_in_cycle_around_vertex
        (hedge_eq=operator.__eq__
        ,hedge2another_hedge=ugraph_fake_embedding.hedge2another_hedge
        ,hedge2next_hedge_in_cycle_around_vertex=hedge2next.__getitem__
        )
        )

    return dfs__finite_explicit_ugraph(
            source_vertices=all_fvertices
            ,vertex2color=vertex2color
            ,vertex2unstable_iter_hedges=vertex2iter_hedges
            ,hedge2another_vertex=hedge2another_vertex
            ,hedge2unstable_iter_other_hedges_around_another_vertex
                =hedge2others_around_another_fvertex

            ,maybe_ancestor_hedge_stack = maybe_ancestor_hedge_stack
            ,maybe_ancestor_vertex_stack = maybe_ancestor_vertex_stack
            )


