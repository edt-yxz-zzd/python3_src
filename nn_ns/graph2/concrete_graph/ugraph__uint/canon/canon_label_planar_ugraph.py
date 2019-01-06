
'''

see: "def - 5. connectivity.txt"
    rigid_triconnected
    rigid_biconnected
    rigid_connected
    triconnected_components
    biconnected_components
    connected_components

methods:
    # ugraph -> labelling
    canon_label_rigid_triconnected_planar_ugraph
    canon_label_rigid_biconnected_planar_ugraph
    canon_label_rigid_connected_planar_ugraph
    canon_label_planar_ugraph

    decompose_rigid_biconnected_ugraph2triconnected_components__SPQR
    decompose_rigid_connected_ugraph2biconnected_components__BC
    decompose_ugraph2connected_components
        # ugraph -> connected_components

    serialize_ugraph :: ugraph -> (upper_bound, [UInt])
    relabel_ugraph :: ugraph -> labelling -> ugraph

ugraph :: ???
labelling :: UGraphLabelling

connected_components:
    super_idx2ugraph
    super_idx2vertex_offset
    super_idx2aedge_offset
    super_idx2hedge_offset
    offseted_new_vertex2old_vertex
    offseted_new_aedge2old_aedge
    offseted_new_hedge2old_hedge
'''

__all__ = '''
    ICanonLabelPlanarUGraph
    '''.split()

from nn_ns.graph2.bucket_sort.UIntSeqSort import UIntSeqSort
from ..UGraphLabelling import UGraphLabelling
from .abc import ABC, abstractmethod

class ICanonLabelPlanarUGraph(ABC):
    '''

connected_components:
    super_idx2ugraph
    super_idx2vertex_offset
    super_idx2aedge_offset
    super_idx2hedge_offset
    offseted_new_vertex2old_vertex
    offseted_new_aedge2old_aedge
    offseted_new_hedge2old_hedge

'''
    __slots__ = ()

    @abstractmethod
    def serialize_ugraph(self, ugraph):
        # -> (upper_bound, [UInt])
        pass
    @abstractmethod
    def relabel_ugraph(self, ugraph, labelling):
        # -> ugraph
        pass

    @abstractmethod
    def decompose_ugraph2connected_components(self, ugraph):
        # -> connected_components
        pass
    @abstractmethod
    def canon_label_rigid_connected_planar_ugraph(self, ugraph):
        # -> labelling
        pass

    def canon_label_planar_ugraph(self, ugraph):
        connected_components = self.decompose_ugraph2connected_components(ugraph)
        subgraphs = connected_components.super_idx2ugraph
        labellings = tuple(map(self.canon_label_rigid_connected_planar_ugraph, subgraphs))
        new_subgraphs = tuple(map(self.relabel_ugraph, subgraphs, labellings))

        ub_uints_pairs = tuple(map(self.serialize_ugraph, new_subgraphs))
        num_subgraphs = len(subgraphs)
        upper_bound = max(ub for ub, _ in ub_uints_pairs, default=0)
        ordered_subgraph_idc = UIntSeqSort(upper_bound, key=lambda i:ub_uints_pairs[i][1]).sort__uintss(range(num_subgraphs))



        def to_entire_vertex(super_idx, sub_vertex):
            vertex_offset = connected_components.super_idx2vertex_offset[super_idx]
            entire_vertex = connected_components.offseted_new_vertex2old_vertex[vertex_offset+sub_vertex]
            return entire_vertex

        def to_entire_aedge(super_idx, sub_aedge):
            aedge_offset = connected_components.super_idx2aedge_offset[super_idx]
            entire_aedge = connected_components.offseted_new_aedge2old_aedge[aedge_offset+sub_aedge]
            return entire_aedge
        def to_entire_hedge(super_idx, sub_hedge):
            hedge_offset = connected_components.super_idx2hedge_offset[super_idx]
            entire_hedge = connected_components.offseted_new_hedge2old_hedge[hedge_offset+sub_hedge]
            return entire_hedge





        entire_vertex_new2old = []
        entire_aedge_new2old = []
        entire_hedge_new2old = []
        for super_idx in ordered_subgraph_idc:
            #subgraph = subgraphs[super_idx]
            labelling = labellings[super_idx]
            new_subgraph = new_subgraphs[super_idx]

            # old_entire_vertex - entire ugraph
            # new_entire_vertex - new entire ugraph
            # old_sub_vertex - subgraph
            # new_sub_vertex - new_subgraph
            # new_entire_vertex = len(entire_vertex_new2old)

            ###### vertex
            new_sub_vertex2old_sub_vertex = labelling.old_vertex2new_vertex.backward_mapping
            for new_sub_vertex in range(new_subgraph.num_vertices):
                old_sub_vertex = new_sub_vertex2old_sub_vertex[new_sub_vertex]
                old_entire_vertex = to_entire_vertex(super_idx, old_sub_vertex)
                entire_vertex_new2old.append(old_entire_vertex)

            ###### aedge
            new_sub_aedge2old_sub_aedge = labelling.old_aedge2new_aedge.backward_mapping
            for new_sub_aedge in range(new_subgraph.num_aedges):
                old_sub_aedge = new_sub_aedge2old_sub_aedge[new_sub_aedge]
                old_entire_aedge = to_entire_aedge(super_idx, old_sub_aedge)
                entire_aedge_new2old.append(old_entire_aedge)

            ###### hedge
            new_sub_hedge2old_sub_hedge = labelling.old_hedge2new_hedge.backward_mapping
            for new_sub_hedge in range(new_subgraph.num_hedges):
                old_sub_hedge = new_sub_hedge2old_sub_hedge[new_sub_hedge]
                old_entire_hedge = to_entire_hedge(super_idx, old_sub_hedge)
                entire_hedge_new2old.append(old_entire_hedge)

        assert len(entire_vertex_new2old) == ugraph.num_vertices
        assert len(entire_aedge_new2old) == ugraph.num_aedges
        assert len(entire_hedge_new2old) == ugraph.num_hedges

        labelling = UGraphLabelling.make_UGraphLabelling__from_new2old_mappings(
            new_vertex2old_vertex=entire_vertex_new2old
            ,new_adge2old_adge=entire_adge_new2old
            ,new_hdge2old_hdge=entire_hdge_new2old
            )
        return labelling




