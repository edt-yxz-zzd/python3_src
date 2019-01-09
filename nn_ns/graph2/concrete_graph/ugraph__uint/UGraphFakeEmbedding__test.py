
r'''

    >>> edgeless_graph
    UGraphFakeEmbedding(num_hedges = 0, num_ffaces = 0, num_fvertices = 0, hedge2fake_clockwise_next_hedge_around_vertex = [], hedge2fake_clockwise_prev_hedge_around_vertex = (), hedge2fake_clockwise_next_hedge_around_fface = (), hedge2fake_clockwise_prev_hedge_around_fface = (), fface2degree = (), hedge2fake_clockwise_fface = (), fface2arbitrary_hedge = (), fvertex2degree = (), hedge2fvertex = (), fvertex2arbitrary_hedge = ())
    >>> single_loop_graph
    UGraphFakeEmbedding(num_hedges = 2, num_ffaces = 2, num_fvertices = 1, hedge2fake_clockwise_next_hedge_around_vertex = [1, 0], hedge2fake_clockwise_prev_hedge_around_vertex = (1, 0), hedge2fake_clockwise_next_hedge_around_fface = (0, 1), hedge2fake_clockwise_prev_hedge_around_fface = (0, 1), fface2degree = (1, 1), hedge2fake_clockwise_fface = (0, 1), fface2arbitrary_hedge = (0, 1), fvertex2degree = (2,), hedge2fvertex = (0, 0), fvertex2arbitrary_hedge = (0,))
    >>> single_nonloop_graph
    UGraphFakeEmbedding(num_hedges = 2, num_ffaces = 1, num_fvertices = 2, hedge2fake_clockwise_next_hedge_around_vertex = [0, 1], hedge2fake_clockwise_prev_hedge_around_vertex = (0, 1), hedge2fake_clockwise_next_hedge_around_fface = (1, 0), hedge2fake_clockwise_prev_hedge_around_fface = (1, 0), fface2degree = (2,), hedge2fake_clockwise_fface = (0, 0), fface2arbitrary_hedge = (0,), fvertex2degree = (1, 1), hedge2fvertex = (0, 1), fvertex2arbitrary_hedge = (0, 1))
    >>> two_parallel_nonloops_graph
    UGraphFakeEmbedding(num_hedges = 4, num_ffaces = 2, num_fvertices = 2, hedge2fake_clockwise_next_hedge_around_vertex = [2, 3, 0, 1], hedge2fake_clockwise_prev_hedge_around_vertex = (2, 3, 0, 1), hedge2fake_clockwise_next_hedge_around_fface = (3, 2, 1, 0), hedge2fake_clockwise_prev_hedge_around_fface = (3, 2, 1, 0), fface2degree = (2, 2), hedge2fake_clockwise_fface = (0, 1, 1, 0), fface2arbitrary_hedge = (0, 1), fvertex2degree = (2, 2), hedge2fvertex = (0, 1, 0, 1), fvertex2arbitrary_hedge = (0, 1))
    >>> two_parallel_loops_graph
    UGraphFakeEmbedding(num_hedges = 4, num_ffaces = 3, num_fvertices = 1, hedge2fake_clockwise_next_hedge_around_vertex = [2, 0, 3, 1], hedge2fake_clockwise_prev_hedge_around_vertex = (1, 3, 0, 2), hedge2fake_clockwise_next_hedge_around_fface = (3, 1, 2, 0), hedge2fake_clockwise_prev_hedge_around_fface = (3, 1, 2, 0), fface2degree = (2, 1, 1), hedge2fake_clockwise_fface = (0, 1, 2, 0), fface2arbitrary_hedge = (0, 1, 2), fvertex2degree = (4,), hedge2fvertex = (0, 0, 0, 0), fvertex2arbitrary_hedge = (0,))
    >>> two_nonparallel_loops_graph
    UGraphFakeEmbedding(num_hedges = 4, num_ffaces = 1, num_fvertices = 1, hedge2fake_clockwise_next_hedge_around_vertex = [2, 3, 1, 0], hedge2fake_clockwise_prev_hedge_around_vertex = (3, 2, 0, 1), hedge2fake_clockwise_next_hedge_around_fface = (2, 3, 1, 0), hedge2fake_clockwise_prev_hedge_around_fface = (3, 2, 0, 1), fface2degree = (4,), hedge2fake_clockwise_fface = (0, 0, 0, 0), fface2arbitrary_hedge = (0,), fvertex2degree = (4,), hedge2fvertex = (0, 0, 0, 0), fvertex2arbitrary_hedge = (0,))
    >>> three_parallel_nonloops_graph
    UGraphFakeEmbedding(num_hedges = 6, num_ffaces = 3, num_fvertices = 2, hedge2fake_clockwise_next_hedge_around_vertex = [2, 5, 4, 1, 0, 3], hedge2fake_clockwise_prev_hedge_around_vertex = (4, 3, 0, 5, 2, 1), hedge2fake_clockwise_next_hedge_around_fface = (3, 4, 5, 0, 1, 2), hedge2fake_clockwise_prev_hedge_around_fface = (3, 4, 5, 0, 1, 2), fface2degree = (2, 2, 2), hedge2fake_clockwise_fface = (0, 1, 2, 0, 1, 2), fface2arbitrary_hedge = (0, 1, 2), fvertex2degree = (3, 3), hedge2fvertex = (0, 1, 0, 1, 0, 1), fvertex2arbitrary_hedge = (0, 1))
    >>> three_nonparallel_nonloops_graph
    UGraphFakeEmbedding(num_hedges = 6, num_ffaces = 1, num_fvertices = 2, hedge2fake_clockwise_next_hedge_around_vertex = [2, 3, 4, 5, 0, 1], hedge2fake_clockwise_prev_hedge_around_vertex = (4, 5, 0, 1, 2, 3), hedge2fake_clockwise_next_hedge_around_fface = (5, 4, 1, 0, 3, 2), hedge2fake_clockwise_prev_hedge_around_fface = (3, 2, 5, 4, 1, 0), fface2degree = (6,), hedge2fake_clockwise_fface = (0, 0, 0, 0, 0, 0), fface2arbitrary_hedge = (0,), fvertex2degree = (3, 3), hedge2fvertex = (0, 1, 0, 1, 0, 1), fvertex2arbitrary_hedge = (0, 1))
    >>> one_loop_one_nonloop_disconnected_graph
    UGraphFakeEmbedding(num_hedges = 4, num_ffaces = 3, num_fvertices = 3, hedge2fake_clockwise_next_hedge_around_vertex = [0, 1, 3, 2], hedge2fake_clockwise_prev_hedge_around_vertex = (0, 1, 3, 2), hedge2fake_clockwise_next_hedge_around_fface = (1, 0, 2, 3), hedge2fake_clockwise_prev_hedge_around_fface = (1, 0, 2, 3), fface2degree = (2, 1, 1), hedge2fake_clockwise_fface = (0, 0, 1, 2), fface2arbitrary_hedge = (0, 2, 3), fvertex2degree = (1, 1, 2), hedge2fvertex = (0, 1, 2, 2), fvertex2arbitrary_hedge = (0, 1, 2))





    .calc.XXX
        is_ugraph_fake_embedding_planar


    #is_ugraph_fake_embedding_planar
    >>> edgeless_graph.calc.is_ugraph_fake_embedding_planar
    True
    >>> single_loop_graph.calc.is_ugraph_fake_embedding_planar
    True
    >>> single_nonloop_graph.calc.is_ugraph_fake_embedding_planar
    True
    >>> two_parallel_nonloops_graph.calc.is_ugraph_fake_embedding_planar
    True
    >>> two_parallel_loops_graph.calc.is_ugraph_fake_embedding_planar
    True
    >>> two_nonparallel_loops_graph.calc.is_ugraph_fake_embedding_planar
    False
    >>> three_parallel_nonloops_graph.calc.is_ugraph_fake_embedding_planar
    True
    >>> three_nonparallel_nonloops_graph.calc.is_ugraph_fake_embedding_planar
    False
    >>> one_loop_one_nonloop_disconnected_graph.calc.is_ugraph_fake_embedding_planar
    True

'''

'''
    #XXX
    >>> edgeless_graph.calc.XXX
    >>> single_loop_graph.calc.XXX
    >>> single_nonloop_graph.calc.XXX
    >>> two_parallel_nonloops_graph.calc.XXX
    >>> two_parallel_loops_graph.calc.XXX
    >>> two_nonparallel_loops_graph.calc.XXX
    >>> three_parallel_nonloops_graph.calc.XXX
    >>> three_nonparallel_nonloops_graph.calc.XXX
    >>> one_loop_one_nonloop_disconnected_graph.calc.XXX
'''


from .UGraphFakeEmbedding import UGraphFakeEmbedding
from .example__UGraphFakeEmbedding import (
    edgeless_graph
    ,single_loop_graph
    ,single_nonloop_graph
    ,two_parallel_nonloops_graph
    ,two_parallel_loops_graph
    ,two_nonparallel_loops_graph
    ,three_parallel_nonloops_graph
    ,three_nonparallel_nonloops_graph
    ,one_loop_one_nonloop_disconnected_graph
    )

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


