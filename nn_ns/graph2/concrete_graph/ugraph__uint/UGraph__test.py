
r'''
    >>> nothing_ugraph
    UGraph(ugraph_basic = UGraphBasic(num_vertices = 0, num_aedges = 0, num_hedges = 0, hedge2vertex = [], hedge2aedge = [], hedge2another_hedge = (), vertex2degree = ()), ugraph_fake_embedding = UGraphFakeEmbedding(num_hedges = 0, num_ffaces = 0, num_fvertices = 0, hedge2fake_clockwise_next_hedge_around_vertex = (), hedge2fake_clockwise_prev_hedge_around_vertex = (), hedge2fake_clockwise_next_hedge_around_fface = (), hedge2fake_clockwise_prev_hedge_around_fface = (), fface2degree = (), hedge2fake_clockwise_fface = (), fface2arbitrary_hedge = (), fvertex2degree = (), hedge2fvertex = (), fvertex2arbitrary_hedge = ()), aedge2arbitrary_hedge = (), fvertex2vertex = (), vertex2maybe_fvertex = ())
    >>> one_vertex_edgeless_ugraph
    UGraph(ugraph_basic = UGraphBasic(num_vertices = 1, num_aedges = 0, num_hedges = 0, hedge2vertex = [], hedge2aedge = [], hedge2another_hedge = (), vertex2degree = (0,)), ugraph_fake_embedding = UGraphFakeEmbedding(num_hedges = 0, num_ffaces = 0, num_fvertices = 0, hedge2fake_clockwise_next_hedge_around_vertex = (), hedge2fake_clockwise_prev_hedge_around_vertex = (), hedge2fake_clockwise_next_hedge_around_fface = (), hedge2fake_clockwise_prev_hedge_around_fface = (), fface2degree = (), hedge2fake_clockwise_fface = (), fface2arbitrary_hedge = (), fvertex2degree = (), hedge2fvertex = (), fvertex2arbitrary_hedge = ()), aedge2arbitrary_hedge = (), fvertex2vertex = (), vertex2maybe_fvertex = (None,))
    >>> one_vertex_one_loop_ugraph
    UGraph(ugraph_basic = UGraphBasic(num_vertices = 1, num_aedges = 1, num_hedges = 2, hedge2vertex = [0, 0], hedge2aedge = [0, 0], hedge2another_hedge = (1, 0), vertex2degree = (2,)), ugraph_fake_embedding = UGraphFakeEmbedding(num_hedges = 2, num_ffaces = 2, num_fvertices = 1, hedge2fake_clockwise_next_hedge_around_vertex = (1, 0), hedge2fake_clockwise_prev_hedge_around_vertex = (1, 0), hedge2fake_clockwise_next_hedge_around_fface = (0, 1), hedge2fake_clockwise_prev_hedge_around_fface = (0, 1), fface2degree = (1, 1), hedge2fake_clockwise_fface = (0, 1), fface2arbitrary_hedge = (0, 1), fvertex2degree = (2,), hedge2fvertex = (0, 0), fvertex2arbitrary_hedge = (0,)), aedge2arbitrary_hedge = (0,), fvertex2vertex = (0,), vertex2maybe_fvertex = (0,))
    >>> one_vertex_two_loops_ugraph
    UGraph(ugraph_basic = UGraphBasic(num_vertices = 1, num_aedges = 2, num_hedges = 4, hedge2vertex = [0, 0, 0, 0], hedge2aedge = [0, 0, 1, 1], hedge2another_hedge = (1, 0, 3, 2), vertex2degree = (4,)), ugraph_fake_embedding = UGraphFakeEmbedding(num_hedges = 4, num_ffaces = 3, num_fvertices = 1, hedge2fake_clockwise_next_hedge_around_vertex = (1, 2, 3, 0), hedge2fake_clockwise_prev_hedge_around_vertex = (3, 0, 1, 2), hedge2fake_clockwise_next_hedge_around_fface = (0, 3, 2, 1), hedge2fake_clockwise_prev_hedge_around_fface = (0, 3, 2, 1), fface2degree = (1, 2, 1), hedge2fake_clockwise_fface = (0, 1, 2, 1), fface2arbitrary_hedge = (0, 1, 2), fvertex2degree = (4,), hedge2fvertex = (0, 0, 0, 0), fvertex2arbitrary_hedge = (0,)), aedge2arbitrary_hedge = (0, 2), fvertex2vertex = (0,), vertex2maybe_fvertex = (0,))
    >>> two_vertices_edgeless_ugraph
    UGraph(ugraph_basic = UGraphBasic(num_vertices = 2, num_aedges = 0, num_hedges = 0, hedge2vertex = [], hedge2aedge = [], hedge2another_hedge = (), vertex2degree = (0, 0)), ugraph_fake_embedding = UGraphFakeEmbedding(num_hedges = 0, num_ffaces = 0, num_fvertices = 0, hedge2fake_clockwise_next_hedge_around_vertex = (), hedge2fake_clockwise_prev_hedge_around_vertex = (), hedge2fake_clockwise_next_hedge_around_fface = (), hedge2fake_clockwise_prev_hedge_around_fface = (), fface2degree = (), hedge2fake_clockwise_fface = (), fface2arbitrary_hedge = (), fvertex2degree = (), hedge2fvertex = (), fvertex2arbitrary_hedge = ()), aedge2arbitrary_hedge = (), fvertex2vertex = (), vertex2maybe_fvertex = (None, None))
    >>> two_vertices_one_nonloop_ugraph
    UGraph(ugraph_basic = UGraphBasic(num_vertices = 2, num_aedges = 1, num_hedges = 2, hedge2vertex = [0, 1], hedge2aedge = [0, 0], hedge2another_hedge = (1, 0), vertex2degree = (1, 1)), ugraph_fake_embedding = UGraphFakeEmbedding(num_hedges = 2, num_ffaces = 1, num_fvertices = 2, hedge2fake_clockwise_next_hedge_around_vertex = (0, 1), hedge2fake_clockwise_prev_hedge_around_vertex = (0, 1), hedge2fake_clockwise_next_hedge_around_fface = (1, 0), hedge2fake_clockwise_prev_hedge_around_fface = (1, 0), fface2degree = (2,), hedge2fake_clockwise_fface = (0, 0), fface2arbitrary_hedge = (0,), fvertex2degree = (1, 1), hedge2fvertex = (0, 1), fvertex2arbitrary_hedge = (0, 1)), aedge2arbitrary_hedge = (0,), fvertex2vertex = (0, 1), vertex2maybe_fvertex = (0, 1))
    >>> two_vertices_two_parallel_nonloops_ugraph
    UGraph(ugraph_basic = UGraphBasic(num_vertices = 2, num_aedges = 2, num_hedges = 4, hedge2vertex = [0, 1, 0, 1], hedge2aedge = [0, 0, 1, 1], hedge2another_hedge = (1, 0, 3, 2), vertex2degree = (2, 2)), ugraph_fake_embedding = UGraphFakeEmbedding(num_hedges = 4, num_ffaces = 2, num_fvertices = 2, hedge2fake_clockwise_next_hedge_around_vertex = (2, 3, 0, 1), hedge2fake_clockwise_prev_hedge_around_vertex = (2, 3, 0, 1), hedge2fake_clockwise_next_hedge_around_fface = (3, 2, 1, 0), hedge2fake_clockwise_prev_hedge_around_fface = (3, 2, 1, 0), fface2degree = (2, 2), hedge2fake_clockwise_fface = (0, 1, 1, 0), fface2arbitrary_hedge = (0, 1), fvertex2degree = (2, 2), hedge2fvertex = (0, 1, 0, 1), fvertex2arbitrary_hedge = (0, 1)), aedge2arbitrary_hedge = (0, 2), fvertex2vertex = (0, 1), vertex2maybe_fvertex = (0, 1))
    >>> three_vertices_two_nonparallel_nonloops_ugraph
    UGraph(ugraph_basic = UGraphBasic(num_vertices = 3, num_aedges = 2, num_hedges = 4, hedge2vertex = [0, 1, 1, 2], hedge2aedge = [0, 0, 1, 1], hedge2another_hedge = (1, 0, 3, 2), vertex2degree = (1, 2, 1)), ugraph_fake_embedding = UGraphFakeEmbedding(num_hedges = 4, num_ffaces = 1, num_fvertices = 3, hedge2fake_clockwise_next_hedge_around_vertex = (0, 2, 1, 3), hedge2fake_clockwise_prev_hedge_around_vertex = (0, 2, 1, 3), hedge2fake_clockwise_next_hedge_around_fface = (2, 0, 3, 1), hedge2fake_clockwise_prev_hedge_around_fface = (1, 3, 0, 2), fface2degree = (4,), hedge2fake_clockwise_fface = (0, 0, 0, 0), fface2arbitrary_hedge = (0,), fvertex2degree = (1, 2, 1), hedge2fvertex = (0, 1, 1, 2), fvertex2arbitrary_hedge = (0, 1, 3)), aedge2arbitrary_hedge = (0, 2), fvertex2vertex = (0, 1, 2), vertex2maybe_fvertex = (0, 1, 2))
    >>> three_vertices_three_nonparallel_nonloops_ugraph
    UGraph(ugraph_basic = UGraphBasic(num_vertices = 3, num_aedges = 3, num_hedges = 6, hedge2vertex = [0, 1, 1, 2, 2, 0], hedge2aedge = [0, 0, 1, 1, 2, 2], hedge2another_hedge = (1, 0, 3, 2, 5, 4), vertex2degree = (2, 2, 2)), ugraph_fake_embedding = UGraphFakeEmbedding(num_hedges = 6, num_ffaces = 2, num_fvertices = 3, hedge2fake_clockwise_next_hedge_around_vertex = (5, 2, 1, 4, 3, 0), hedge2fake_clockwise_prev_hedge_around_vertex = (5, 2, 1, 4, 3, 0), hedge2fake_clockwise_next_hedge_around_fface = (2, 5, 4, 1, 0, 3), hedge2fake_clockwise_prev_hedge_around_fface = (4, 3, 0, 5, 2, 1), fface2degree = (3, 3), hedge2fake_clockwise_fface = (0, 1, 0, 1, 0, 1), fface2arbitrary_hedge = (0, 1), fvertex2degree = (2, 2, 2), hedge2fvertex = (0, 1, 1, 2, 2, 0), fvertex2arbitrary_hedge = (0, 1, 3)), aedge2arbitrary_hedge = (0, 2, 4), fvertex2vertex = (0, 1, 2), vertex2maybe_fvertex = (0, 1, 2))
















    ########################################
    .calc.XXX
        sorted_self_loop_aedges
        degree2sorted_vertices
        sorted_nonempty_vertex_degrees

    # sorted_self_loop_aedges
    >>> nothing_ugraph.calc.sorted_self_loop_aedges
    ()
    >>> one_vertex_edgeless_ugraph.calc.sorted_self_loop_aedges
    ()
    >>> one_vertex_one_loop_ugraph.calc.sorted_self_loop_aedges
    (0,)
    >>> one_vertex_two_loops_ugraph.calc.sorted_self_loop_aedges
    (0, 1)
    >>> two_vertices_edgeless_ugraph.calc.sorted_self_loop_aedges
    ()
    >>> two_vertices_one_nonloop_ugraph.calc.sorted_self_loop_aedges
    ()
    >>> two_vertices_two_parallel_nonloops_ugraph.calc.sorted_self_loop_aedges
    ()
    >>> three_vertices_two_nonparallel_nonloops_ugraph.calc.sorted_self_loop_aedges
    ()
    >>> three_vertices_three_nonparallel_nonloops_ugraph.calc.sorted_self_loop_aedges
    ()

    # degree2sorted_vertices
    >>> nothing_ugraph.calc.degree2sorted_vertices
    ()
    >>> one_vertex_edgeless_ugraph.calc.degree2sorted_vertices
    ((0,),)
    >>> one_vertex_one_loop_ugraph.calc.degree2sorted_vertices
    ((), (), (0,))
    >>> one_vertex_two_loops_ugraph.calc.degree2sorted_vertices
    ((), (), (), (), (0,))
    >>> two_vertices_edgeless_ugraph.calc.degree2sorted_vertices
    ((0, 1),)
    >>> two_vertices_one_nonloop_ugraph.calc.degree2sorted_vertices
    ((), (0, 1))
    >>> two_vertices_two_parallel_nonloops_ugraph.calc.degree2sorted_vertices
    ((), (), (0, 1))
    >>> three_vertices_two_nonparallel_nonloops_ugraph.calc.degree2sorted_vertices
    ((), (0, 2), (1,))
    >>> three_vertices_three_nonparallel_nonloops_ugraph.calc.degree2sorted_vertices
    ((), (), (0, 1, 2))

    # sorted_nonempty_vertex_degrees
    >>> nothing_ugraph.calc.sorted_nonempty_vertex_degrees
    ()
    >>> one_vertex_edgeless_ugraph.calc.sorted_nonempty_vertex_degrees
    (0,)
    >>> one_vertex_one_loop_ugraph.calc.sorted_nonempty_vertex_degrees
    (2,)
    >>> one_vertex_two_loops_ugraph.calc.sorted_nonempty_vertex_degrees
    (4,)
    >>> two_vertices_edgeless_ugraph.calc.sorted_nonempty_vertex_degrees
    (0,)
    >>> two_vertices_one_nonloop_ugraph.calc.sorted_nonempty_vertex_degrees
    (1,)
    >>> two_vertices_two_parallel_nonloops_ugraph.calc.sorted_nonempty_vertex_degrees
    (2,)
    >>> three_vertices_two_nonparallel_nonloops_ugraph.calc.sorted_nonempty_vertex_degrees
    (1, 2)
    >>> three_vertices_three_nonparallel_nonloops_ugraph.calc.sorted_nonempty_vertex_degrees
    (2,)


'''

'''
    # XXX
    >>> nothing_ugraph.calc.XXX
    >>> one_vertex_edgeless_ugraph.calc.XXX
    >>> one_vertex_one_loop_ugraph.calc.XXX
    >>> one_vertex_two_loops_ugraph.calc.XXX
    >>> two_vertices_edgeless_ugraph.calc.XXX
    >>> two_vertices_one_nonloop_ugraph.calc.XXX
    >>> two_vertices_two_parallel_nonloops_ugraph.calc.XXX
    >>> three_vertices_two_nonparallel_nonloops_ugraph.calc.XXX
    >>> three_vertices_three_nonparallel_nonloops_ugraph.calc.XXX

'''

from .UGraph import UGraph
from .example__UGraph import (
    nothing_ugraph
    ,one_vertex_edgeless_ugraph
    ,one_vertex_one_loop_ugraph
    ,one_vertex_two_loops_ugraph
    ,two_vertices_edgeless_ugraph
    ,two_vertices_one_nonloop_ugraph
    ,two_vertices_two_parallel_nonloops_ugraph
    ,three_vertices_two_nonparallel_nonloops_ugraph
    ,three_vertices_three_nonparallel_nonloops_ugraph
    )

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


