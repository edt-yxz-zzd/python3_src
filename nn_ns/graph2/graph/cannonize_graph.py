
'''
using the tree canonization algorithm
assume some basic canonization are known
connected_component

allow loops, multi-edge

canonize_ex :: ugraph -> (canon, old_vtx2new_vtx)
canonize :: ugraph -> canon
    # new_vtx2color :: [color]
    # new_vtx2sorted_multi_weighted_neighbors :: [sorted[(vtx, weight)]]
    # canon = sized_flatten([new_vtx2color]) + sized_flatten(new_vtx2sorted_multi_weighted_neighbors, 2)
    # i.e. canon =
            [V, color_of[new_vtx=0], ..., color_of[new_vtx=V-1]
            ## sorted by (neighbor, weight)
            ,num_edges_of(new_vtx=0)
            ,neighbor_of[new_vtx=0 at aedge A], weight_of[A]
            ,neighbor_of[new_vtx=0 at aedge B], weight_of[B]
            ,...
            ,num_edges_of(new_vtx=V-1)
            ...
            ,neighbor_of[new_vtx=V-1 at aedge X], weight_of[X]
            ]
'''


__all__ = '''
    ugraph_canon_ex
    canon_map2canon
    reverse_map


IColoredWeightedUGraphOps
    canon_map2canon
    IColoredWeightedUGraphOps__to_connected_subgraphs
        ugraph2canon_map
        IConnected2ColoredWeightedUGraphCanonization

IColoredWeightedUGraphCanonization
    IConnected2ColoredWeightedUGraphCanonization
    IConnectedColoredWeightedUGraphCanonization
        ugraph2canon_map

reverse_map
fixed_flatten
    sized_flatten
        canon_map2canon

canon_map2canon
    ugraph_canon_ex
    IColoredWeightedUGraphCanonization
ugraph2canon_map
    ugraph_canon_ex
    IConnected2ColoredWeightedUGraphCanonization

    '''.split()

from itertools import chain
#from ..bucket_sort.super_sort import make_super_sort
from ..bucket_sort.inplace_bucket_sort import (
    inplace_bucket_sort, calc_upper_bound_of_seqs_ex)
from ..bucket_sort.UIntSeqSort import UIntSeqSort
from ..bucket_sort.echo import fst, snd
from abc import ABC, abstractmethod

'''
class IColoredUGraphOps:
    # vertices = [0..V-1]
    # color in [0..V-1]
    def num_vertices(self, g):pass
    def color_of(self, g, vtx):pass
    def vtx2multi_neighbors(self, g, vtx):pass
'''

class IColoredWeightedUGraphOps(ABC):
    # vertices = [0..V-1]
    # color in [0..V-1]
    # aedges = [0..E-1]
    # weight in [0..E-1]
    @abstractmethod
    def num_vertices(self, g):pass
    @abstractmethod
    def num_edges(self, g):pass
    @abstractmethod
    def color_of(self, g, vtx):pass
    @abstractmethod
    def weight_of(self, g, aedge):pass
    @abstractmethod
    def vtx2hedges(self, g, vtx):pass
    @abstractmethod
    def hedge2aedge(self, g, hedge):pass
    @abstractmethod
    def hedge2another_vertex(self, g, hedge):pass


class IColoredWeightedUGraphOps__to_connected_subgraphs(IColoredWeightedUGraphOps):
    #def to_connected_components(self, g):pass
    @abstractmethod
    def to_connected_subgraphs(self, g):
        # g -> [(subgraph::IColoredWeightedUGraphOps, sub_vtx2org_vtx, sub_aedge2org_aedge)]
        pass
class IColoredWeightedUGraphCanonization(IColoredWeightedUGraphOps):
    # color are ordered, i.e. the ordering of color affect the canon result
    # vertices = [0..V-1]
    # color in [0..V-1]
    # aedges = [0..E-1]
    # weight in [0..E-1]
    def canonize_ex(self, g):
        canon_map = old_vtx2new_vtx = self.make_canon_map(g)
        ops = self
        canon = canon_map2canon(ops, g, canon_map)
        return canon, old_vtx2new_vtx

    def canonize(self, g):
        canon, old_vtx2new_vtx = self.canonize_ex(g)
        return canon

    @abstractmethod
    def make_canon_map(self, g):
        # colored_ugraph -> old_vtx2new_vtx
        pass

class IConnectedColoredWeightedUGraphCanonization(IColoredWeightedUGraphCanonization):
    pass


class IConnected2ColoredWeightedUGraphCanonization(
    IColoredWeightedUGraphOps__to_connected_subgraphs):
    def __init__(self, connected_ugraph_canon):
        assert isinstance(connected_ugraph_canon, IConnectedColoredWeightedUGraphCanonization)
        self.__canonizer = connected_ugraph_canon
    def make_canon_map(self, g):
        return ugraph2canon_map(self, g, self.__canonizer)


def reverse_map(old_vtx2new_vtx):
    # old_vtx2new_vtx -> new_vtx2old_vtx
    V = len(old_vtx2new_vtx)
    new_vtx2old_vtx = [None]*V
    for old_vtx, new_vtx in enumerate(old_vtx2new_vtx):
        assert 0 <= new_vtx < V
        new_vtx2old_vtx[new_vtx] = old_vtx
    assert None not in new_vtx2old_vtx
    return new_vtx2old_vtx
def canon_map2canon(ops, g, old_vtx2new_vtx):
    # canon_map -> canon
    #
    # canon_map = old_vtx2new_vtx
    ####canon = (new_vtx2color, new_vtx2sorted_multi_weighted_neighbors)
    # canon = sized_flatten([new_vtx2color]) + sized_flatten(new_vtx2sorted_multi_weighted_neighbors, 2)
    # upper_bound of canon = max(V+1, E)
    assert isinstance(ops, IColoredWeightedUGraphOps)
    V = len(old_vtx2new_vtx)
    assert V == ops.num_vertices(g)
    E = ops.num_edges(g)

    # new_vtx2color
    new_vtx2old_vtx = reverse_map(old_vtx2new_vtx)
    new_vtx2color = [ops.color_of(new_vtx2old_vtx[new_vtx])
                    for new_vtx in range(V)]

    # new_vtx2sorted_multi_weighted_neighbors
    def new_vtx2iter_multi_weighted_neighbors(new_vtx):
        old_vtx = new_vtx2old_vtx[new_vtx]
        for old_hedge in ops.vtx2hedges(old_vtx):
            old_neighbor = ops.hedge2another_vertex(old_hedge)
            new_neighbor = old_vtx2new_vtx[old_neighbor]

            old_aedge = ops.hedge2aedge(old_hedge)
            weight = ops.weight_of(old_aedge)
            yield (new_neighbor, weight)

    # new_vtx2multi_weighted_neighbors :: [[(vtx, weight)]]
    new_vtx2multi_weighted_neighbors = \
        [[*new_vtx2iter_multi_weighted_neighbors(new_vtx)]
         for new_vtx in range(V)
        ]
    #inplace_bucket_sort(new_vtx2multi_neighbors, V)
    #sort = make_super_sort([(inplace_bucket_sort), (inplace_bucket_sort)])
    inplace_bucket_sort(new_vtx2multi_weighted_neighbors, E, key=snd)
    inplace_bucket_sort(new_vtx2multi_weighted_neighbors, V, key=fst)
    new_vtx2sorted_multi_weighted_neighbors = new_vtx2multi_weighted_neighbors
    del new_vtx2multi_weighted_neighbors

    # canon
    it = chain(sized_flatten([new_vtx2color])
            , sized_flatten(new_vtx2sorted_multi_weighted_neighbors, 2)
            )
    canon = list(it)
    assert 0 <= min(canon) <= max(canon) < max(V+1,E)
    return canon

def fixed_flatten(x, *lens):
    '''
example:
    >>> [*fixed_flatten(0)]
    [0]
    >>> [*fixed_flatten([0])]
    [[0]]
    >>> [*fixed_flatten([0], 1)]
    [0]
    >>> [*fixed_flatten([0,1], 2)]
    [0, 1]
    >>> [*fixed_flatten([[0,1],[3,4], 2)]
    [[0, 1], [3, 4]]
    >>> [*fixed_flatten([[0,1],[3,4]], 2, 2)]
    [[0, 1, 3, 4]]
    >>> [*fixed_flatten([[0,1],[3,4],[5,6]], 3, 2)]
    [[0, 1, 3, 4, 5, 6]]
    >>> [*fixed_flatten([[0,1,-1],[3,4,-5]], 2, 3)]
    [[0, 1, -1, 3, 4, -5]]
'''
    L = len(lens)
    def this_func(x, idx):
        if idx == L:
            yield x
            return
        assert idx < L
        ls = x
        assert len(ls) == lens[idx]
        idx += 1
        for x in ls:
            yield from this_func(x, idx)
    yield from this_func(x, 0)

def sized_flatten(iter_lsls, *lens):
    '''
example:
    >>> [*sized_flatten([])]
    []
    >>> [*sized_flatten([[]])]
    [0]
    >>> [*sized_flatten([[], []])]
    [0, 0]
    >>> [*sized_flatten([[], [-1]])]
    [0, 1, -1]
    >>> [*sized_flatten(['ab', 'cde'])]
    [2, 'a', 'b', 3, 'c', 'd', 'e']
    >>> [*sized_flatten(['ab', 'cde'], 1, 1, 1)]
    [2, 'a', 'b', 3, 'c', 'd', 'e']
    >>> [*sized_flatten([[(1,2),(3,4)], [(5,6),(7,8),(9,0)]], 2)]
    [2, 1, 2, 3, 4, 3, 5, 6, 7, 8, 9, 0]

    # 2,----------; 3,-----------------
    #       2*2         3*2
'''
    for ls in iter_lsls:
        yield len(ls)
        #yield from ls
        for x in ls:
            yield from fixed_flatten(x, *lens)



def ugraph_canon_ex(ops, g, connected_ugraph_canon):
    # ... -> (canon, old_vtx2new_vtx)
    assert isinstance(ops, IColoredWeightedUGraphOps__to_connected_subgraphs)
    assert isinstance(connected_ugraph_canon, IConnectedColoredWeightedUGraphCanonization)
    canon_map = ugraph2canon_map(ops, g, connected_ugraph_canon)
    canon = canon_map2canon(ops, g, canon_map)
    return canon, canon_map

def ugraph2canon_map(ops, g, connected_ugraph_canon):
    # ... -> old_vtx2new_vtx
    assert isinstance(ops, IColoredWeightedUGraphOps__to_connected_subgraphs)
    assert isinstance(connected_ugraph_canon, IConnectedColoredWeightedUGraphCanonization)

    # subgraphs_ex :: [(subgraph, sub_vtx2org_vtx, sub_aedge2org_aedge)]
    subgraphs_ex = ops.to_connected_subgraphs(g)
    subgraphs = [*map(fst, subgraphs_ex)]
    subgraph_idx2old_sub_vtx2org_vtx = [*map(snd, subgraphs_ex)]

    # sub_canons_ex :: [(sub_canon, old_sub_vtx2new_sub_vtx)]
    sub_canons_ex = [*map(connected_ugraph_canon.canonize_ex, subgraphs)]
    sub_canons = [*map(fst, sub_canons_ex)]
    upper_bound = calc_upper_bound_of_seqs_ex(sub_canons)
    # sorted by subcanon
    sort = UIntSeqSort(upper_bound, key=snd)
    sorted_subgraph_idx_subcanon_pairs = sort(enumerate(sub_canons))
    sorted_subgraph_idc = [*map(fst, sorted_subgraph_idx_subcanon_pairs)]


    def make_new_sub_vtx2org_vtx(old_sub_vtx2org_vtx, old_sub_vtx2new_sub_vtx):
        assert len(old_sub_vtx2org_vtx) == len(old_sub_vtx2new_sub_vtx)
        new_sub_vtx2old_sub_vtx = reverse_map(old_sub_vtx2new_sub_vtx)
        new_sub_vtx2org_vtx = [old_sub_vtx2org_vtx[old_sub_vtx]
                                for old_sub_vtx in new_sub_vtx2old_sub_vtx]
        return new_sub_vtx2org_vtx

    subgraph_idx2new_sub_vtx2org_vtx = \
        [*map(make_new_sub_vtx2org_vtx
            , subgraph_idx2old_sub_vtx2org_vtx
            , map(snd, sub_canons_ex))]

    # sorted by subcanon
    sorted_new_sub_vtx2org_vtx_ls =\
        [subgraph_idx2new_sub_vtx2org_vtx[subgraph_idx]
            for subgraph_idx in sorted_subgraph_idc]

    new_vtx2old_vtx = \
        [*chain.from_iterable(sorted_new_sub_vtx2org_vtx_ls)]
    V = ops.num_vertices(g)
    assert len(new_vtx2old_vtx) == V
    old_vtx2new_vtx = reverse_map(new_vtx2old_vtx)
    canon_map = old_vtx2new_vtx
    return canon_map




