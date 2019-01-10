
__all__ = '''
    Calc_UGraph_Info
    '''.split()

from ..UGraph import UGraph
import weakref # ref

_get = object.__getattribute__
def _get_ugraph(self):
    return _get(self, '_ugraph_ref')()
def _get_cache(self):
    return _get(self, '_cache')
class Calc_UGraph_Info:
    all_attr_seq = '''
        sorted_self_loop_aedges
        degree2sorted_vertices
        sorted_nonempty_vertex_degrees
        is_ugraph_utree
        is_ugraph_rigid_connected
        '''.split()
        #is_ugraph_rigid_biconnected
        #is_ugraph_rigid_triconnected
        #either_ugraph_nonplanar_condition_or_ugraph_planar_embedding

    all_attr_set = frozenset(all_attr_seq)

    def __init__(self, ugraph):
        assert isinstance(ugraph, UGraph)
        self._ugraph_ref = weakref.ref(ugraph)
        self._cache = {}
    def __getattribute__(self, attr):
        if attr in UGraph.all_UGraph_attr_set:
            ugraph = _get_ugraph(self)
            return getattr(ugraph, attr)

        if attr not in __class__.all_attr_set:
            raise AttributeError(attr)

        cache = _get_cache(self)
        try:
            return cache[attr]
        except KeyError:
            r = _get(self, attr)()
            r = cache.setdefault(attr, r)
            return r


    def sorted_self_loop_aedges(self):
        ugraph = _get_ugraph(self)
        return tuple(filter(ugraph.is_aedge_self_loop, range(ugraph.num_aedges)))
    def degree2sorted_vertices(self):
        ugraph = _get_ugraph(self)
        vertex2degree = ugraph.vertex2degree
        #max_vertex_degree = max(vertex2degree, default=-1)
        num_vertex_degrees = 1+max(vertex2degree, default=-1)
        degree2sorted_vertices = [[] for _ in range(num_vertex_degrees)]
        for vertex, vertex_degree in enumerate(vertex2degree):
            degree2sorted_vertices[vertex_degree].append(vertex)
        return tuple(map(tuple, degree2sorted_vertices))
    def sorted_nonempty_vertex_degrees(self):
        sorted_nonempty_vertex_degrees = tuple(
            vertex_degree
            for vertex_degree, vertices
                in enumerate(self.degree2sorted_vertices)
                if vertices
            )
        return sorted_nonempty_vertex_degrees

    def is_ugraph_utree(self):
        ugraph = _get_ugraph(self)
        return (ugraph.num_aedges+1 == ugraph.num_vertices
            and self.is_ugraph_rigid_connected)
    def is_ugraph_rigid_connected(self):
        ugraph = _get_ugraph(self)
        ugraph_fake_embedding = ugraph.ugraph_fake_embedding
        if ugraph.num_aedges == 0:
            return ugraph.num_vertices == 1 # <<== rigid
        return (ugraph.num_vertices == ugraph_fake_embedding.num_fvertices
            and ugraph_fake_embedding.calc.is_ugraph_fake_embedding_nonedgeless_rigid_connected
            )

