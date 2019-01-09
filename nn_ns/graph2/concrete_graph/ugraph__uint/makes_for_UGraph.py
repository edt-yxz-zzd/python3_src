
__all__ = '''
    makes_for_UGraph
    '''.split()

from .UGraphFakeEmbedding import UGraphFakeEmbedding

class makes_for_UGraph:
    class aedge2arbitrary_hedge:
        def from_hedge2aedge(*, hedge2aedge):
            num_hedges = len(hedge2aedge)
            num_aedges = num_hedges//2
            aedge2arbitrary_hedge = [None]*num_aedges
            for hedge in reversed(range(num_hedges)):
                aedge = hedge2aedge[hedge]
                aedge2arbitrary_hedge[aedge] = hedge
            return tuple(aedge2arbitrary_hedge)
    class fvertex2vertex:
        def from_vertex2degree(*, vertex2degree):
            fvertex2vertex = tuple(vertex for vertex, degree in enumerate(vertex2degree) if degree)
            return fvertex2vertex

        def from_fvertex2arbitrary_hedge(*, hedge2vertex, fvertex2arbitrary_hedge):
            fvertex2vertex = tuple(hedge2vertex[hedge] for hedge in fvertex2arbitrary_hedge)
            return fvertex2vertex
    class vertex2maybe_fvertex:
        def from_fvertex2vertex(*, num_vertices, fvertex2vertex):
            vertex2maybe_fvertex = [None]*num_vertices
            for fvertex, vertex in enumerate(fvertex2vertex):
                vertex2maybe_fvertex[vertex] = fvertex
            return tuple(vertex2maybe_fvertex)
    #class hedge2fvertex:
    #   def from_hedge2vertex(*, num_fvertices, hedge2vertex, vertex2maybe_fvertex):
    class hedge2fake_clockwise_next_hedge_around_vertex:
        def from_hedge2vertex(*, num_fvertices, hedge2vertex, vertex2maybe_fvertex):
            fvertex2hedges = [[] for _ in range(num_fvertices)]
            for hedge, vertex in enumerate(hedge2vertex):
                maybe_fvertex = vertex2maybe_fvertex[vertex]
                if maybe_fvertex is not None:
                    fvertex = maybe_fvertex
                    fvertex2hedges[fvertex].append(hedge)
            assert all(fvertex2hedges)

            num_hedges = len(hedge2vertex)
            hedge2fake_clockwise_next_hedge_around_vertex = [None]*num_hedges
            for hedges1 in fvertex2hedges:
                prev_hedge = hedges1[-1]
                for hedge in hedges1:
                    hedge2fake_clockwise_next_hedge_around_vertex[prev_hedge] = hedge
                    prev_hedge = hedge
            assert all(h is not None for h in hedge2fake_clockwise_next_hedge_around_vertex)
            return tuple(hedge2fake_clockwise_next_hedge_around_vertex)

    class ugraph_fake_embedding:
        def from_hedge2fake_clockwise_next_hedge_around_vertex(*
            ,hedge2fake_clockwise_next_hedge_around_vertex
            ,hedge2another_hedge
            ):
            return UGraphFakeEmbedding.make_UGraphFakeEmbedding__simplest(
                hedge2fake_clockwise_next_hedge_around_vertex
                    = hedge2fake_clockwise_next_hedge_around_vertex
                ,hedge2another_hedge = hedge2another_hedge
                )
        def from_hedge2vertex(*
            ,num_fvertices
            ,hedge2vertex
            ,vertex2maybe_fvertex
            ,hedge2another_hedge
            ):
            hedge2fake_clockwise_next_hedge_around_vertex = (
                makes_for_UGraph
                .hedge2fake_clockwise_next_hedge_around_vertex
                .from_hedge2vertex(
                    num_fvertices=num_fvertices
                    ,hedge2vertex=hedge2vertex
                    ,vertex2maybe_fvertex=vertex2maybe_fvertex
                    )
                )
            return (makes_for_UGraph.ugraph_fake_embedding
                .from_hedge2fake_clockwise_next_hedge_around_vertex(
                    hedge2fake_clockwise_next_hedge_around_vertex
                        =hedge2fake_clockwise_next_hedge_around_vertex
                    ,hedge2another_hedge=hedge2another_hedge
                    )
                )

