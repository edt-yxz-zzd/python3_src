
__all__ = '''
    dfs__ugraph_fake_embedding
    dfs__ugraph_fake_embedding__two_color
    DFS_SourceType
    DFS_Case
    DFS_CaseParts
    '''.split()

from seed.tiny import echo
import enum
import operator

if False:
    from ..dfs.dfs__finite_explicit_ugraph__two_color import (
        dfs__finite_explicit_ugraph__two_color
        ,DFS_Case
        ,DFS_CaseParts
        ,Vertex2TwoColor__seq
        ,make_hedge2unstable_iter_other_hedges_around_another_vertex
        )
else:
    from .imports import Vertex2TwoColor__seq
    from .imports import dfs__finite_explicit_ugraph__two_color as _x
    dfs__finite_explicit_ugraph__two_color = _x.dfs__finite_explicit_ugraph__two_color
    DFS_Case = _x.DFS_Case
    DFS_CaseParts = _x.DFS_CaseParts
    make_hedge2unstable_iter_other_hedges_around_another_vertex = _x.make_hedge2unstable_iter_other_hedges_around_another_vertex
    del _x


DFS_SourceType = enum.Enum('DFS_SourceType', 'VERTEX HEDGE EITHER'.split())

class dfs__ugraph_fake_embedding:
    def __init__(self, *
        ,ugraph_fake_embedding
        ,is_clockwise_around_fvertex:bool
        ,maybe_ancestor_hedge_stack = None
        ,maybe_ancestor_vertex_stack = None
        ,maybe_vertex2color = None
        ):
        'maybe_vertex2color :: None|IVertex2TwoColor'
        self.ugraph_fake_embedding = ugraph_fake_embedding
        self.is_clockwise_around_fvertex = bool(is_clockwise_around_fvertex)
        self.maybe_ancestor_hedge_stack = maybe_ancestor_hedge_stack
        self.maybe_ancestor_vertex_stack = maybe_ancestor_vertex_stack
        self.vertex2color = _make_vertex2color_from_maybe(maybe_vertex2color, ugraph_fake_embedding.num_fvertices)

    def more_dfs(self, *, source_vertices=None):
        if source_vertices is None:
            all_fvertices = range(self.ugraph_fake_embedding.num_fvertices)
            source_vertices = all_fvertices
        return self.more_dfs_via(sources=source_vertices, source_type=DFS_SourceType.VERTEX)
    def more_dfs_via(self, *, sources, source_type):
        '''source_type :: DFS_SourceType; sources - see: dfs__ugraph_fake_embedding__two_color'''
        return dfs__ugraph_fake_embedding__two_color(
                ugraph_fake_embedding
                    = self.ugraph_fake_embedding
                ,is_clockwise_around_fvertex
                    = self.is_clockwise_around_fvertex
                ,maybe_ancestor_hedge_stack
                    = self.maybe_ancestor_hedge_stack
                ,maybe_ancestor_vertex_stack
                    = self.maybe_ancestor_vertex_stack
                ,maybe_vertex2color
                    =  self.vertex2color

                ,sources = sources
                ,source_type = source_type
                )


def _make_vertex2color(num_fvertices):
    return Vertex2TwoColor__seq([False]*num_fvertices, True)
def _make_vertex2color_from_maybe(maybe_vertex2color, num_fvertices):
    if maybe_vertex2color is None:
        vertex2color = _make_vertex2color(num_fvertices)
    else:
        vertex2color = maybe_vertex2color
    return vertex2color



def dfs__ugraph_fake_embedding__two_color(*
    ,ugraph_fake_embedding
    ,is_clockwise_around_fvertex:bool
    ,maybe_ancestor_hedge_stack
    ,maybe_ancestor_vertex_stack
    ,sources
    ,maybe_vertex2color
    ,source_type : DFS_SourceType
    ):
    '''

maybe_vertex2color :: None | IVertex2TwoColor
source_type = DFS_SourceType
Source = Vertex | HEdge | ((False, HEdge)|(True, Vertex))
sources :: Iter Source
    depends on source_type
'''
    vertex2color = _make_vertex2color_from_maybe(maybe_vertex2color, ugraph_fake_embedding.num_fvertices)

    is_clockwise_around_fvertex = bool(is_clockwise_around_fvertex)
    _vertex2iter_hedges = ugraph_fake_embedding.fvertex2iter_fake_clockwise_hedges
    _hedge2iter_hedges = ugraph_fake_embedding.hedge2iter_fake_clockwise_hedges_around_vertex
    def fvertex2iter_hedges(vertex):
        return _vertex2iter_hedges(vertex, reverse=not is_clockwise_around_fvertex)
    def hedge2iter_hedges(vertex):
        return _hedge2iter_hedges(vertex, reverse=not is_clockwise_around_fvertex)
    hedge2another_hedge = ugraph_fake_embedding.hedge2another_hedge
    def hedge2another_vertex(hedge):
        return ugraph_fake_embedding.hedge2fvertex[hedge2another_hedge(hedge)]

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

    def hedge2fvertex(hedge):
        return ugraph_fake_embedding.hedge2fvertex[hedge]

    if source_type == DFS_SourceType.VERTEX:
        source2vertex = echo
        source2unstable_iter_hedges = fvertex2iter_hedges
    elif source_type == DFS_SourceType.HEDGE:
        source2vertex = hedge2fvertex
        source2unstable_iter_hedges = hedge2iter_hedges
    elif source_type == DFS_SourceType.EITHER:
        (either2fvertex, either2iter_hedges
        ) = (dfs__finite_explicit_ugraph__two_color
            .make_kwargs4via_opaque_sources
            .from_kwargs__source_either__less
            )(
                hedge2vertex=hedge2fvertex
                ,vertex2unstable_iter_hedges=fvertex2iter_hedges
                ,hedge2unstable_iter_hedges=hedge2iter_hedges
                )
        source2vertex = either2fvertex
        source2unstable_iter_hedges = either2iter_hedges
    elif type(source_type) is not DFS_SourceType: raise TypeError
    else:
        raise Exception(f'unknown source_type: {source_type!r}')

    return dfs__finite_explicit_ugraph__two_color.via_opaque_sources(
            sources=sources
            ,source2vertex=source2vertex
            ,source2unstable_iter_hedges=source2unstable_iter_hedges
            ,hedge2another_vertex=hedge2another_vertex

            ,vertex2color=vertex2color
            ,hedge2unstable_iter_other_hedges_around_another_vertex
                =hedge2others_around_another_fvertex
            ,maybe_ancestor_hedge_stack = maybe_ancestor_hedge_stack
            ,maybe_ancestor_vertex_stack = maybe_ancestor_vertex_stack
            )

dfs__ugraph_fake_embedding__two_color.DFS_SourceType = DFS_SourceType

