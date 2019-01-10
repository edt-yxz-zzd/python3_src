
r'''
>>> mk(one_vertex_edgeless_ugraph)
ImmutableNamespace(aedge2maybe_upper_hedge=(), depth2depth_idx2vertex=((0,),), depth2vertices1=((0,),), either_root=(False, 0), vertex2child_aedges=((),), vertex2depth=(0,), vertex2depth_idx=(0,), vertex2maybe_parent_aedge=(None,), vertex2maybe_parent_vertex=(None,))
>>> mk(two_vertices_one_nonloop_ugraph)
ImmutableNamespace(aedge2maybe_upper_hedge=(None,), depth2depth_idx2vertex=((0, 1),), depth2vertices1=((0, 1),), either_root=(True, 0), vertex2child_aedges=((), ()), vertex2depth=(0, 0), vertex2depth_idx=(0, 1), vertex2maybe_parent_aedge=(0, 0), vertex2maybe_parent_vertex=(None, None))
>>> mk(three_vertices_two_nonparallel_nonloops_ugraph)
ImmutableNamespace(aedge2maybe_upper_hedge=(1, 2), depth2depth_idx2vertex=((1,), (0, 2)), depth2vertices1=((1,), (0, 2)), either_root=(False, 1), vertex2child_aedges=((), (0, 1), ()), vertex2depth=(1, 0, 1), vertex2depth_idx=(0, 0, 1), vertex2maybe_parent_aedge=(0, None, 1), vertex2maybe_parent_vertex=(1, None, 1))

>>> mk(None)
Traceback (most recent call last):
    ...
TypeError
>>> mk(nothing_ugraph)
Traceback (most recent call last):
    ...
ValueError
>>> mk(three_vertices_three_nonparallel_nonloops_ugraph)
Traceback (most recent call last):
    ...
ValueError




>>> mk(one_vertex_edgeless_ugraph, (False, 0)) == mk(one_vertex_edgeless_ugraph)
True
>>> mk(two_vertices_one_nonloop_ugraph, (False, 0))
ImmutableNamespace(aedge2maybe_upper_hedge=(0,), depth2depth_idx2vertex=((0,), (1,)), depth2vertices1=((0,), (1,)), either_root=(False, 0), vertex2child_aedges=((0,), ()), vertex2depth=(0, 1), vertex2depth_idx=(0, 0), vertex2maybe_parent_aedge=(None, 0), vertex2maybe_parent_vertex=(None, 0))
>>> mk(three_vertices_two_nonparallel_nonloops_ugraph, (False, 0))
ImmutableNamespace(aedge2maybe_upper_hedge=(0, 2), depth2depth_idx2vertex=((0,), (1,), (2,)), depth2vertices1=((0,), (1,), (2,)), either_root=(False, 0), vertex2child_aedges=((0,), (1,), ()), vertex2depth=(0, 1, 2), vertex2depth_idx=(0, 0, 0), vertex2maybe_parent_aedge=(None, 0, 1), vertex2maybe_parent_vertex=(None, 0, 1))
>>> mk(three_vertices_two_nonparallel_nonloops_ugraph, (False, 1)) == mk(three_vertices_two_nonparallel_nonloops_ugraph)
True


>>> mk(two_vertices_one_nonloop_ugraph, (True, 0)) == mk(two_vertices_one_nonloop_ugraph)
True
>>> mk(three_vertices_two_nonparallel_nonloops_ugraph, (True, 0))
ImmutableNamespace(aedge2maybe_upper_hedge=(None, 2), depth2depth_idx2vertex=((0, 1), (2,)), depth2vertices1=((0, 1), (2,)), either_root=(True, 0), vertex2child_aedges=((), (1,), ()), vertex2depth=(0, 0, 1), vertex2depth_idx=(0, 1, 0), vertex2maybe_parent_aedge=(0, 0, 1), vertex2maybe_parent_vertex=(None, None, 1))



'''

from .Maker4UTree import Maker4UTree
from .example__UGraph import (
    one_vertex_edgeless_ugraph
    ,two_vertices_one_nonloop_ugraph
    ,three_vertices_two_nonparallel_nonloops_ugraph

    ,nothing_ugraph
    ,one_vertex_one_loop_ugraph
    ,one_vertex_two_loops_ugraph
    ,two_vertices_edgeless_ugraph
    ,two_vertices_two_parallel_nonloops_ugraph
    ,three_vertices_three_nonparallel_nonloops_ugraph
    )

def mk(utree, maybe_either_root=None):
    return Maker4UTree(utree).make_all_rooted_utree_attrs(maybe_either_root=maybe_either_root)
    ns.either_root


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


