
'''
oriented multi-edged digraph by defalt
oriented means neighbors are ordered
u2vtc is a mapping if obj_graph or sequence if int_graph
    why?
       d[v]
       unpredictable - mapping may be hash/ordered map
       O(1) - sequence
vtc is a Sequence if oriented or MultiSet/Set if not oriented
dedges = [(a,b)] # a->b

'''

__all__ = '''
    U2Vtc_To_DigraphABC
    ObjU2Vtc_To_Digraph
    IntU2Vtc_To_Digraph
'''.split()


from collections import defaultdict
from seed.graph.DigraphABC import DigraphABC
from seed.types.DefaultDict import DefaultDict
from seed.types.OneTime import OneTimeMap, OneTimeSet
from seed.types.to_container import to_container

def make_int_graph_map(N):
    buffer = [None]*N
    return OneTimeMap(buffer)
def make_int_graph_set(N):
    buffer = [None]*N
    return OneTimeSet(buffer)
    
def int_graph_dedges2u2vtc(dedges, missing_vtc):
    dedges, missing_vtc = map(to_container, [dedges, missing_vtc])
    iter_vtc = lambda:chain(missing_vtc, chain.from_iterable(dedges))
    N_1 = max(iter_vtc())
    _0 = min(iter_vtc())
    if not 0 == _0:
        raise ValueError('not 0 == min')
    N = N_1 + 1
    s = make_int_graph_set(N)
    s.update(iter_vtc())
    if len(s) != N:
        assert len(s) < N
        raise ValueError('miss some vertices')
    
    d = make_int_graph_map(N)
    dd = DefaultDict(d, list)
    _dedges2u2vtc(dedges, missing_vtc, dd, list.append)
    assert dd.mapping is d
    # return d.buffer # bug : buffer is [(pos, [vtx])]
    u2vtc = [None] * N
    for u, vtc in d.items():
        u2vtc[u] = vtc
    if any(vtc is None for vtc in u2vtc):
        raise ValueError('miss some vertices: {}'
                         .format(list(u for u, vtc in enumerate(u2vtc) if vtc is None)))
    return u2vtc


    




def obj_graph_dedges2u2vtc(dedges, missing_vtc):
    d = defaultdict(list)
    _dedges2u2vtc(dedges, missing_vtc, d, list.append)
    return dict(d)
    
def _dedges2u2vtc(dedges, missing_vtc, outputDefaultDict, neighbors_add):
    'isolated_vertices <= missing_vtc <= all_vertices'
    add = neighbors_add
    d = aDefaultDict
    for a, b in dedges:
        add(d[a], b)
        d[b]
    for v in missing_vtc:
        d[v]

class U2Vtc_To_DigraphABC(DigraphABC):
    __slots__ = ('u2vtc', 'ne')
    def __init__(self, u2vtc):
        self.u2vtc = u2vtc
        # self.ne = sum(map(len, u2vtc))
##    def make_vertex_mapping(self):
##        return dict
##    def make_vertex_set(self):
##        return set
    
    def num_vertices(self):
        return len(self.u2vtc)
    def num_dedges(self):
        try:
            return self.ne
        except AttributeError:
            self.ne = sum(map(len, u2vtc))
            return self.ne
    def iter_vertices(self):
        return iter(self.u2vtc)
    def iter_adjacent_dedges(self, v):
        return ((v, u) for u in self.u2vtc[v])
    def dedge2ends(self, e):
        return e
    def iter_neighbors(self, v):
        return iter(self.u2vtc[v])
            
    


class ObjU2Vtc_To_Digraph(U2Vtc_To_DigraphABC):
    __slots__ = ()
    def make_vertex_mapping(self):
        return {}
    def make_vertex_set(self):
        return set()
    @classmethod
    def from_vertex_pairs(cls, pairs, missing_vtc):
        u2vtc = obj_graph_dedges2u2vtc(pairs, missing_vtc)
        return cls(u2vtc)
class IntU2Vtc_To_Digraph(U2Vtc_To_DigraphABC):
    __slots__ = ()
    def make_vertex_mapping(self):
        return make_int_graph_map(self.num_vertices())
    def make_vertex_set(self):
        return make_int_graph_set(self.num_vertices())
    @classmethod
    def from_vertex_pairs(cls, pairs, missing_vtc):
        u2vtc = int_graph_dedges2u2vtc(pairs, missing_vtc)
        return cls(u2vtc)
        
    
