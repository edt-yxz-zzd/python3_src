
from seed.types.ABC import *


class DigraphABC(ABC):
    'directed; multi-edges; loops; may or may not oriented'
    __slots__ = ()

    @not_implemented
    def make_vertex_mapping(self):
        # O(N) time/space
        # just suitable for for fixed self.vertices
        # e.g. return [None]*self.num_vertices()
        ... 
    @not_implemented
    def make_vertex_set(self):
        # O(N) time/space
        # just suitable for for fixed self.vertices
        ...
    
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
            
    @classmethod
    @not_implemented
    def from_vertex_pairs(cls, pairs, missing_vtc):
        # pairs :: [(u,v)] where u->v is a directed edges
        #     order of pairs is important for oriened digraph
        #        if u->v1 before u->v2, then neighbors[u] = (..., v1,..., v2, ...)
        #     count of same pair is important for multi-edged digraph
        # isolated_vtc <= missing_vtc <= all_vtc
        ...
        




    
    

