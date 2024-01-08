__all__ = '''
    DigraphABC
'''.split()
    #mk_vertex_mapping__default_


#from seed.types.ABC import *
from seed.abc.abc__ver1 import ABC, not_implemented


class DigraphABC(ABC):
    'directed; multi-edges; loops; may or may not oriented'
    __slots__ = ()

    @not_implemented
    def make_vertex_set(self):
        # O(N) time/space
        # just suitable for for fixed self.vertices
        ...
    @not_implemented
    def make_vertex_mapping(self):
        # O(N) time/space
        # just suitable for for fixed self.vertices
        # e.g. return [None]*self.num_vertices()
        ...
    def make_vertex_mapping__default_(self, default):
        'e.g. make_vertex_mapping__default_ :: g --> ({vtx:default}|[default]*g.nv) # vs: make_vertex_mapping :: g --> ({}|[None]*g.nv)'
        return mk_vertex_mapping__default_(default, self)
    def make_vertex_mapping__fdefault_(self, fdefault):
        return mk_vertex_mapping__fdefault_(fdefault, self)
    def make_vertex_mapping__vtx2default_(self, vtx2default_):
        return mk_vertex_mapping__vtx2default_(vtx2default_, self)


    @not_implemented
    def num_vertices(self):...
    @not_implemented
    def num_dedges(self):...
    @not_implemented
    def iter_vertices(self):...
    @not_implemented
    def iter_adjacent_dedges(self, v):...
    @not_implemented
    def dedge2ends(self, e):...
    def iter_neighbors(self, v):
        for e in self.iter_adjacent_dedges(v):
            _v, u = self.dedge2ends(e)
            yield u
    def iter_dedges(self):
        for v in self.iter_vertices():
            for e in self.iter_adjacent_dedges(v):
                yield e
    def iter_dedges__ends_(self):
        '-> Iter (u,v)'
        for e in self.iter_dedges():
            yield self.dedge2ends(e)

    @classmethod
    @not_implemented
    def from_vertex_pairs(cls, pairs, missing_vtc):
        # pairs :: [(u,v)] where u->v is a directed edges
        #     order of pairs is important for oriened digraph
        #        if u->v1 before u->v2, then neighbors[u] = (..., v1,..., v2, ...)
        #     count of same pair is important for multi-edged digraph
        # isolated_vtc <= missing_vtc <= all_vtc
        ...


def mk_vertex_mapping__default_(default, g):
    vtx2default = g.make_vertex_mapping()
    for v in g.iter_vertices():
        vtx2default[v] = default
    return vtx2default

def mk_vertex_mapping__fdefault_(fdefault, g):
    vtx2default = g.make_vertex_mapping()
    for v in g.iter_vertices():
        vtx2default[v] = fdefault()
    return vtx2default

def mk_vertex_mapping__vtx2default_(vtx2default_, g):
    vtx2default = g.make_vertex_mapping()
    for v in g.iter_vertices():
        vtx2default[v] = vtx2default_(vtx)
    return vtx2default







from seed.graph.DigraphABC import DigraphABC
#from seed.graph.DigraphABC import mk_vertex_mapping__default_
#from seed.graph.DigraphABC import mk_vertex_mapping__fdefault_
#from seed.graph.DigraphABC import mk_vertex_mapping__vtx2default_
from seed.graph.DigraphABC import *
