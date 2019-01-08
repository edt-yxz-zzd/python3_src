
'''

see: "def - 5. connectivity.txt"
    rigid_triconnected
    rigid_biconnected
    rigid_connected
    triconnected_components
    biconnected_components
    connected_components

methods:
    # ugraph -> **extra_data -> labelling
    canon_label_rigid_triconnected_planar_ugraph
    canon_label_rigid_biconnected_planar_ugraph
    canon_label_rigid_connected_planar_ugraph
    canon_label_planar_ugraph

    # what about canon_label_colored_simple_planar_ugraph??
    #   1 aedge and 2 hedges can be 3 new colored vertices
    #   new ugraph will have no self_loop and no multiedge
    #   fine, but...

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

from ..imports__bucket_sort import bucket_sort4uint_seq
from ..locally_reindex_global_colors import locally_reindex_global_colors
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
    def canon_label_rigid_connected_planar_ugraph(self, ugraph
        ,vertex2color
        ,num_colors
        ,aedge2weight
        ,num_weights
        ,hedge2hweight
        ,num_hweights
        ):
        # -> labelling
        pass

    def relabel_ugraph_ex(self, ugraph, labelling
        ,vertex2color
        ,aedge2weight
        ,hedge2hweight
        ):
        # -> (ugraph, vertex2color, aedge2weight, hedge2hweight)
        ugraph__new = self.relabel_ugraph(ugraph, labelling)
        #ugraph_serialization__new = self.serialize_ugraph(ugraph__new)

        vertex2color__new = tuple(vertex2color[labelling.old_vertex2new_vertex.backward_mapping[new_vertex]] for new_vertex in range(ugraph.num_vertices))
        aedge2weight__new = tuple(aedge2weight[labelling.old_aedge2new_aedge.backward_mapping[new_aedge]] for new_aedge in range(ugraph.num_aedges))
        hedge2hweight__new = tuple(hedge2hweight[labelling.old_hedge2new_hedge.backward_mapping[new_hedge]] for new_hedge in range(ugraph.num_hedges))
        return (ugraph__new, vertex2color__new, aedge2weight__new, hedge2hweight__new)

    def canon_label_planar_ugraph(self, ugraph, *
        ,vertex2color
        ,num_colors
        ,aedge2weight
        ,num_weights
        ,hedge2hweight
        ,num_hweights
        ):
        # -> labelling

        connected_components = self.decompose_ugraph2connected_components(ugraph)



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




        subgraphs = connected_components.super_idx2ugraph
        num_subgraphs = len(subgraphs)

        super_idx2vertex2global_color = []
        super_idx2aedge2global_weight = []
        super_idx2hedge2global_hweight = []
        for super_idx, subgraph in enumerate(subgraphs):
            sub_vertex2global_color = []
            for sub_vertex in range(subgraph.num_vertices):
                entire_vertex = to_entire_vertex(super_idx, sub_vertex)
                global_color = vertex2color[entire_vertex]
                sub_vertex2global_color.append(global_color)
            super_idx2vertex2global_color.append(sub_vertex2global_color)

            sub_aedge2global_weight = []
            for sub_aedge in range(subgraph.num_aedges):
                entire_aedge = to_entire_aedge(super_idx, sub_aedge)
                global_weight = aedge2weight[entire_aedge]
                sub_aedge2global_weight.append(global_weight)
            super_idx2aedge2global_weight.append(sub_aedge2global_weight)

            sub_hedge2global_hweight = []
            for sub_hedge in range(subgraph.num_hedges):
                entire_hedge = to_entire_hedge(super_idx, sub_hedge)
                global_hweight = hedge2hweight[entire_hedge]
                sub_hedge2global_hweight.append(global_hweight)
            super_idx2hedge2global_hweight.append(sub_hedge2global_hweight)


        (super_idx2num_local_colors, super_idx2vertex2local_color, _
        ) = locally_reindex_global_colors(num_colors, super_idx2vertex2global_color)
        (super_idx2num_local_weights, super_idx2aedge2local_weight, _
        ) = locally_reindex_global_weights(num_weights, super_idx2aedge2global_weight)
        (super_idx2num_local_hweights, super_idx2hedge2local_hweight, _
        ) = locally_reindex_global_hweights(num_hweights, super_idx2hedge2global_hweight)

        def canon(super_idx):
            return self.canon_label_rigid_connected_planar_ugraph(
                subgraphs[super_idx]
                ,vertex2color   =super_idx2vertex2local_color[super_idx]
                ,num_colors     =super_idx2num_local_colors[super_idx]
                ,aedge2weight   =super_idx2aedge2local_weight[super_idx]
                ,num_weights    =super_idx2num_local_weights[super_idx]
                ,hedge2hweight  =super_idx2hedge2local_hweight[super_idx]
                ,num_hweights   =super_idx2num_local_hweights[super_idx]
                )
        labellings = tuple(map(canon, range(num_subgraphs)))
        new_subgraph_extra_ls = tuple(map(self.relabel_ugraph_ex, subgraphs, labellings, super_idx2vertex2local_color, super_idx2aedge2local_weight, super_idx2hedge2local_hweight))
        new_subgraphs = tuple(map(fst, new_subgraph_extra_ls))

        ordered_subgraph_idc = range(new_subgraphs)
        # hedge
        upper_bound = max(super_idx2num_local_hweights, default=0)
        ordered_subgraph_idc = bucket_sort4uint_seq(upper_bound, ordered_subgraph_idc, key=lambda i:new_subgraph_extra_ls[i][-1])
        # aedge
        upper_bound = max(super_idx2num_local_weights, default=0)
        ordered_subgraph_idc = bucket_sort4uint_seq(upper_bound, ordered_subgraph_idc, key=lambda i:new_subgraph_extra_ls[i][-2])
        # vertex
        upper_bound = max(super_idx2num_local_colors, default=0)
        ordered_subgraph_idc = bucket_sort4uint_seq(upper_bound, ordered_subgraph_idc, key=lambda i:new_subgraph_extra_ls[i][-3])
        # ugraph_serialization
        ub_uints_pairs = tuple(map(self.serialize_ugraph, new_subgraphs))
        upper_bound = max(ub for ub, _ in ub_uints_pairs, default=0)
        ordered_subgraph_idc = bucket_sort4uint_seq(upper_bound, ordered_subgraph_idc, key=lambda i:ub_uints_pairs[i][1])



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
            ,new_aedge2old_aedge=entire_aedge_new2old
            ,new_hedge2old_hedge=entire_hedge_new2old
            )
        return labelling




