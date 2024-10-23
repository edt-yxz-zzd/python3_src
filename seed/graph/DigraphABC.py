r'''[[[
e ../../python3_src/seed/graph/DigraphABC.py


py -m nn_ns.app.debug_cmd   seed.graph.DigraphABC -x


iter_adjacent_dedges --> vertex2iter_adjacent_dedges
iter_neighbors --> vertex2iter_neighbors
.+1,$s/\<\(iter_adjacent_dedges\|iter_neighbors\)\>/vertex2\0/g


#]]]'''#'''
__all__ = '''
DigraphABC
    DigraphABC__mk

    num_vertices
    num_dedges
    iter_vertices
    iter_dedges
        iter_dedges__ends_

    dedge2ends
    vertex2iter_adjacent_dedges
        vertex2iter_neighbors

    make_vertex_set
    make_vertex_mapping
        make_vertex_mapping__default_
        make_vertex_mapping__fdefault_
        make_vertex_mapping__vtx2default_

    from_vertex_pairs

'''.split()
#_mk_vertex_mapping__default_
#    _mk_vertex_mapping__fdefault_
#    _mk_vertex_mapping__vtx2default_
__all__


#from seed.types.ABC import *
from seed.abc.abc__ver1 import ABC, not_implemented


class DigraphABC(ABC):
    'directed; multi-edges; loops; may or may not oriented'
    __slots__ = ()

    @not_implemented
    def make_vertex_set(self):
        '-> {vtx}'
        # O(N) time/space
        # just suitable for for fixed self.vertices
    @not_implemented
    def make_vertex_mapping(self):
        '-> {vtx:???}'
        # O(N) time/space
        # just suitable for for fixed self.vertices
        # e.g. return [None]*self.num_vertices()
    def make_vertex_mapping__default_(self, default):
        '-> {vtx:default}'
        'e.g. make_vertex_mapping__default_ :: g --> ({vtx:default}|[default]*g.nv) # vs: make_vertex_mapping :: g --> ({}|[None]*g.nv)'
        return _mk_vertex_mapping__default_(default, self)
    def make_vertex_mapping__fdefault_(self, fdefault):
        '-> {vtx:fdefault()}'
        return _mk_vertex_mapping__fdefault_(fdefault, self)
    def make_vertex_mapping__vtx2default_(self, vtx2default_):
        '-> {vtx:vtx2default_(vtx)}'
        return _mk_vertex_mapping__vtx2default_(vtx2default_, self)


    @not_implemented
    def num_vertices(self):
        '-> uint'
    @not_implemented
    def num_dedges(self):
        '-> uint'
    @not_implemented
    def iter_vertices(self):
        '-> Iter<vtx>'
    @not_implemented
    def vertex2iter_adjacent_dedges(self, v):
        'src/vtx -> Iter<dedge{.src==src}>'
    @not_implemented
    def dedge2ends(self, e):
        'dedge -> (src/vtx, dst/vtx) # [dedge{src-->dst}]'
    def vertex2iter_neighbors(self, v):
        'src/vtx -> Iter<dst/vtx>'
        for e in self.vertex2iter_adjacent_dedges(v):
            _v, u = self.dedge2ends(e)
            yield u
    def iter_dedges(self):
        '-> Iter<dedge>'
        for v in self.iter_vertices():
            for e in self.vertex2iter_adjacent_dedges(v):
                yield e
    def iter_dedges__ends_(self):
        '-> Iter (u,v)'
        for e in self.iter_dedges():
            yield self.dedge2ends(e)

class DigraphABC__mk(DigraphABC):
    r'''[[[
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.graph.DigraphABC:DigraphABC__mk@T    =T   +exclude_attrs5listed_in_cls_doc
==>>:
abstract_methods:
    `dedge2ends
    `from_vertex_pairs
    `vertex2iter_adjacent_dedges
    `iter_vertices
    `make_vertex_mapping
    `make_vertex_set
    `num_dedges
    `num_vertices
concrete_methods:
    iter_dedges
    iter_dedges__ends_
    vertex2iter_neighbors
    make_vertex_mapping__default_
    make_vertex_mapping__fdefault_
    make_vertex_mapping__vtx2default_
new_abstract_methods:
    `from_vertex_pairs
    #]]]'''#'''
    __slots__ = ()
    @classmethod
    @not_implemented
    def from_vertex_pairs(cls, pairs, missing_vtc):
        r'''[[[
        :: [(u,v)] -> [v] -> dgraph

        # pairs :: [(u,v)] where u->v is a directed edges
        #     order of pairs is important for oriened digraph
        #        if u->v1 before u->v2, then neighbors[u] = (..., v1,..., v2, ...)
        #     count of same pair is important for multi-edged digraph
        # isolated_vtc <= missing_vtc <= all_vtc
        #]]]'''#'''


######################
######################
######################
#NOTE:mk vs make: flip args
def _mk_vertex_mapping__default_(default, g):
    vtx2default = g.make_vertex_mapping()
    for v in g.iter_vertices():
        vtx2default[v] = default
    return vtx2default

def _mk_vertex_mapping__fdefault_(fdefault, g):
    vtx2default = g.make_vertex_mapping()
    for v in g.iter_vertices():
        vtx2default[v] = fdefault()
    return vtx2default

def _mk_vertex_mapping__vtx2default_(vtx2default_, g):
    vtx2default = g.make_vertex_mapping()
    for v in g.iter_vertices():
        vtx2default[v] = vtx2default_(v)
    return vtx2default



######################
######################
######################
#below just for "export"/"import"
######################
######################
######################
def iter_vertices(g, /):
    return g.iter_vertices()

def make_vertex_mapping(g, /):
    return g.make_vertex_mapping()

def make_vertex_set(g, /):
    return g.make_vertex_set()

def num_dedges(g, /):
    return g.num_dedges()

def num_vertices(g, /):
    return g.num_vertices()

def iter_dedges(g, /):
    return g.iter_dedges()

def iter_dedges__ends_(g, /):
    return g.iter_dedges__ends_()


######################
######################
######################
def from_vertex_pairs(cls, pairs, missing_vtc, /):
    return cls.from_vertex_pairs(pairs, missing_vtc)

def dedge2ends(g, dedge, /):
    return g.dedge2ends(dedge)

def vertex2iter_adjacent_dedges(g, vtx, /):
    return g.vertex2iter_adjacent_dedges(vtx)

def vertex2iter_neighbors(g, vtx, /):
    return g.vertex2iter_neighbors(vtx)

#NOTE:mk vs make: flip args
def make_vertex_mapping__default_(g, default, /):
    return g.make_vertex_mapping__default_(default)

def make_vertex_mapping__fdefault_(g, fdefault, /):
    return g.make_vertex_mapping__fdefault_(fdefault)

def make_vertex_mapping__vtx2default_(g, vtx2default_, /):
    return g.make_vertex_mapping__vtx2default_(vtx2default_)
######################
######################
######################


__all__
from seed.graph.DigraphABC import DigraphABC, DigraphABC__mk
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

from seed.graph.DigraphABC import *
