r'''[[[
e ../../python3_src/seed/graph/strong_connected_components.py



seed.graph.strong_connected_components
py -m nn_ns.app.debug_cmd   seed.graph.strong_connected_components -x
py -m nn_ns.app.doctest_cmd seed.graph.strong_connected_components:__doc__ -ht



>>> from seed.graph.U2Vtc_To_DigraphABC import IntU2Vtc_To_Digraph
>>> def f(pairs, missing_vtc=(), /):
...     g = IntU2Vtc_To_Digraph.from_vertex_pairs(pairs, missing_vtc)
...     return decompose_to_strong_connected_components_in_reversed_topological_ordering(g)

#>>> f([(0,1),(1,2),(2,3)])
#>>> f([(0,1),(1,2),(2,2)])
#>>> f([(0,1),(1,2),(2,1)])
#>>> f([(0,1),(1,2),(2,0)])
#>>> f([(0,1),(1,0)])
#>>> f([(0,1),(1,0),(2,0),(3,2),(3,4),(3,5),(4,3),(5,6),(6,3)])

>>> f([(0,1),(1,2),(2,3)])
[[3], [2], [1], [0]]
>>> f([(0,1),(1,2),(2,2)])
[[2], [1], [0]]
>>> f([(0,1),(1,2),(2,1)])
[[2, 1], [0]]
>>> f([(0,1),(1,2),(2,0)])
[[2, 1, 0]]
>>> f([(0,1),(1,0)])
[[1, 0]]
>>> f([(0,1),(1,0),(2,0),(3,2),(3,4),(3,5),(4,3),(5,6),(6,3)])
[[1, 0], [2], [4, 6, 5, 3]]







#]]]'''#'''

__all__ = r'''
decompose_to_strong_connected_components_in_reversed_topological_ordering
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.graph.dfs import dfs, ENTER, EXIT, BACK, CROSS_OR_FORWARD
if 0:
    from seed.graph.DigraphABC import (DigraphABC, DigraphABC__mk
,num_vertices
,num_dedges
,iter_vertices
,iter_dedges
,    iter_dedges__ends_
#
,dedge2ends
,vertex2iter_adjacent_dedges
,    vertex2iter_neighbors
#
,make_vertex_set
,make_vertex_mapping
,    make_vertex_mapping__default_
,    make_vertex_mapping__fdefault_
,    make_vertex_mapping__vtx2default_
#
,from_vertex_pairs
)
___end_mark_of_excluded_global_names__0___ = ...


#def decompose_to_connected_components(g, roots=None):
#    raise should-be-undirected-graph
#    topological_ordering = reversed(list(iter_reversed_topological_ordering(g, roots)))
#    root2connected_components
#    for case, path in dfs(g, topological_ordering):raise
#

def decompose_to_strong_connected_components_in_reversed_topological_ordering(g, roots=None, /):
    'DigraphABC -> [strong_connected_component]/[[vertex]]{reversed_topological_ordering}'
    #xxx:assert all(type(v) is int for v in g.iter_vertices())

    # [vst_num == preorder_num == ipreorder] #visit dfs_tree in preorder
    # [low_num<vst_num> == min vst_num of vtc<subtree<dfs_tree;vtx<vst_num>>>]
    #   [#subtree include dedge:BACK/ENTER(EXIT), not inclde:CROSS_OR_FORWARD#]
    #
    stack = vst_num2vtx_low_num_pair = []
        # :: [(vtx, low_num)]
        #vst_num2vtx = []
        #vtx2low_num = g.make_vertex_mapping()
    vtx2vst_num = g.make_vertex_mapping()
        # :: {vtx:vst_num}
    components = []
        # :: [[vtx]]
        # in reversed_topological_ordering
    new_components = []
        # :: [vtx]

    def _exit(xxx_num4me, /):
        assert _path # cannot be root
        # EXIT | BACK
        (parent, low_num4parent) = stack[-1]
        (vtx4update, _tail_path) = _path
        assert parent == vtx4update
        _low_num4parent = min(low_num4parent, xxx_num4me)
        if _low_num4parent < low_num4parent:
            stack[-1] = (parent, _low_num4parent)
        return

    for case, (me, _path) in dfs(g, roots):
        if case == ENTER:
            vst_num = len(stack)
            low_num = vst_num
            stack.append((me,low_num))
            vtx2vst_num[me] = vst_num
        elif case == EXIT:
            (_me,low_num4me) = stack.pop()
            assert _me == me
            new_components.append(me)

            if low_num4me == vtx2vst_num[me]:
                # a new complete scc
                components.append(new_components)
                new_components = []
                continue

            assert _path # cannot be root
            _exit(low_num4me)
        elif case == BACK:
            assert _path # cannot be root
            vst_num4me = vtx2vst_num[me]
            _exit(vst_num4me)
        elif case == CROSS_OR_FORWARD:
            pass
        else:
            raise 000



    assert not stack
    assert not new_components
    assert sum(map(len, components)) == g.num_vertices() or not roots is None
    assert all(components)
    return components
















from seed.graph.strong_connected_components import decompose_to_strong_connected_components_in_reversed_topological_ordering
from seed.graph.strong_connected_components import *

