

__all__ = '''
    edgeless_graph
    single_loop_graph
    single_nonloop_graph
    two_parallel_nonloops_graph
    two_parallel_loops_graph
    two_nonparallel_loops_graph
    three_parallel_nonloops_graph
    three_nonparallel_nonloops_graph
    one_loop_one_nonloop_disconnected_graph
    '''.split()

from .UGraphFakeEmbedding import UGraphFakeEmbedding

_mk = UGraphFakeEmbedding.make_UGraphFakeEmbedding__simplest
mk = lambda hedge2fake_clockwise_next_hedge_around_vertex, hedge2another_hedge: _mk(hedge2fake_clockwise_next_hedge_around_vertex=hedge2fake_clockwise_next_hedge_around_vertex, hedge2another_hedge=hedge2another_hedge)

# edgeless
edgeless_graph = mk([], [])

# a loop edge
single_loop_graph = mk([1,0], [1,0])

# a non-loop edge
single_nonloop_graph = mk([0,1], [1,0])

# 2 parallel non-loop edges
two_parallel_nonloops_graph = mk([2,3,0,1], [1,0,3,2])

# 2 parallel loop edges
two_parallel_loops_graph = mk([2,0,3,1], [1,0,3,2])

# 2 non-parallel loop edges # non-planar
two_nonparallel_loops_graph = mk([2,3,1,0], [1,0,3,2])

# 3 parallel non-loop edges
three_parallel_nonloops_graph = mk([2,5,4,1,0,3], [1,0,3,2,5,4])

# 3 non_parallel non-loop edges
three_nonparallel_nonloops_graph = mk([2,3,4,5,0,1], [1,0,3,2,5,4])

# a loop and a nonloop disconnected
one_loop_one_nonloop_disconnected_graph = mk([0,1,3,2], [1,0,3,2])


del mk, _mk, UGraphFakeEmbedding

