
__all__ = '''
    nothing_ugraph
    one_vertex_edgeless_ugraph
    one_vertex_one_loop_ugraph
    one_vertex_two_loops_ugraph
    two_vertices_edgeless_ugraph
    two_vertices_one_nonloop_ugraph
    two_vertices_two_parallel_nonloops_ugraph
    three_vertices_two_nonparallel_nonloops_ugraph
    three_vertices_three_nonparallel_nonloops_ugraph
    '''.split()

from .UGraph import UGraph


_mk = UGraph.make_UGraph__simplest
mk = lambda num_vertices, hedge2vertex, hedge2aedge: _mk(num_vertices=num_vertices, hedge2vertex=hedge2vertex, hedge2aedge=hedge2aedge)


nothing_ugraph = mk(0, [], [])
one_vertex_edgeless_ugraph = mk(1, [], [])
two_vertices_edgeless_ugraph = mk(2, [], [])
one_vertex_one_loop_ugraph = mk(1, [0,0], [0,0])
one_vertex_two_loops_ugraph = mk(1, [0,0,0,0], [0,0,1,1])
two_vertices_one_nonloop_ugraph = mk(2, [0,1], [0,0])
two_vertices_two_parallel_nonloops_ugraph = mk(2, [0,1,0,1], [0,0,1,1])
three_vertices_two_nonparallel_nonloops_ugraph = mk(3, [0,1,1,2], [0,0,1,1])
three_vertices_three_nonparallel_nonloops_ugraph = mk(3, [0,1,1,2,2,0], [0,0,1,1,2,2])


del _mk, mk, UGraph

