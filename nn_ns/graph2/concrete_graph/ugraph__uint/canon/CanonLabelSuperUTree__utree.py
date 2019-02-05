
__all__ = '''
    CanonLabelSuperUTree__utree
    '''.split()

from .CanonLabelSuperUTreeABC import CanonLabelSuperUTreeABC
from .abc import override
from ..Coloring import (RowColoring, TableColoring, Serialization)
#from ..IMaker4UTree import IMaker4UTree
from ..Maker4UTree import Maker4UTree
from ..reindex_complex_colors import (
    reindex_complex_colors__old_color_sequence
    ,reindex_complex_colors__old_color_tuple
    )
#from ..imports__bucket_sort import (bucket_sort_per_row, bucket_sort4uint_seq)
#from seed.iters.group_by_eq import group_by_eq

ordered_name_seq = tuple('''
    vertex
    aedge
    hedge
    '''.split()
    )
class CanonLabelSuperUTree__utree(CanonLabelSuperUTreeABC):
    def __init__(self, *
        ,utree
        ,vertex_rowcoloring : RowColoring
        ,aedge_rowcoloring
        ,hedge_rowcoloring
        ):
        assert isinstance(utree, UGraph)
        assert utree.calc.is_ugraph_utree

        assert isinstance(vertex_rowcoloring, RowColoring)
        assert isinstance(aedge_rowcoloring, RowColoring)
        assert isinstance(hedge_rowcoloring, RowColoring)
        assert len(vertex_rowcoloring.column2color) == utree.num_vertices
        assert len(aedge_rowcoloring.column2color) == utree.num_aedges
        assert len(hedge_rowcoloring.column2color) == utree.num_hedges

        name2named_global_rowcoloring = dict(
            vertex = vertex_rowcoloring
            ,aedge = aedge_rowcoloring
            ,hedge = hedge_rowcoloring
            )
        super().__init__(
            super_utree=utree
            ,name2named_global_rowcoloring=name2named_global_rowcoloring
            ,ordered_name_seq=ordered_name_seq
            )
        #self.super_vertex2XXX = 


    @override
    def make_IMaker4UTree(self, utree):
        # -> IMaker4UTree
        return Maker4UTree(utree)

    _static_name2case2num_named_local_indices = dict(
        # case == 2: one of bicenter_vertex
        # case == 1: unicenter_vertex
        # case == 0: otherwise
        vertex = (2, 1, 2)
        ,aedge = (1, 0, 1)
        ,hedge = (2, 0, 2)
        )
    @override
    def super_vertex2num_named_local_indices(self, name, super_vertex):
        # -> UInt
        # -> num_named_local_indices
        #
        # vertex -> subgraph
        # * root_vertex:
        #   subgraph:
        #       no aedge
        #       single vertex - the root_vertex
        # * 2 root_vertices incident to root_aedge
        #   subgraph per vertex:
        #       single aedge - the root_aedge
        #       two vertices - 2 root_vertices
        # * otherwise
        #   subgraph:
        #       single aedge - the parent_aedge
        #       two vertices - the vertex and parent_vertex
        #

        rooted_super_utree_attrs = self.rooted_super_utree_attrs
        depth2vertices1 = rooted_super_utree_attrs.depth2vertices1
        root_vertices = depth2vertices1[0]

        # case == 2: one of bicenter_vertex
        # case == 1: unicenter_vertex
        # case == 0: otherwise
        if super_vertex in root_vertices:
            case = len(root_vertices)
            assert 1 <= case <= 2
        else:
            case = 0
        return self._static_name2case2num_named_local_indices[name][case]

        ##############
        (is_root_aedge, root_vertex_or_root_aedge
        ) = rooted_super_utree_attrs.either_root

        if is_root_aedge:
            root_aedge = root_vertex_or_root_aedge
        else:
            root_vertex = root_vertex_or_root_aedge

        if name == 'vertex':
            return 2
        self.name2named_global_rowcoloring

    @override
    def named_local_idx2maybe_named_global_idx(self, name, super_vertex, named_local_idx):
        # -> (None|UInt)
        # -> (None|named_global_idx)
        # named_local_idx may be virtual one
        # color virtual_named_local_idx with a special color
        #
        # use: locally_reindex_global_colors

        assert 0 <= named_local_idx <= 1
        if name == 'vertex':
            if named_local_idx != 0:
                assert named_local_idx == 1
                # parent_vertex is virtual
                return None
            return super_vertex

        rooted_super_utree_attrs = self.rooted_super_utree_attrs
        maybe_parent_aedge = rooted_super_utree_attrs.vertex2maybe_parent_aedge[super_vertex]
        if maybe_parent_aedge is None:
            # super_vertex is unicenter_vertex
            #   subgraph has no aedges
            raise IndexError(f'named_local_idx {named_local_idx} out of range')
        parent_aedge = maybe_parent_aedge

        if name == 'aedge':
            assert named_local_idx == 0
            return parent_aedge

        assert name == 'hedge'
        if named_local_idx != 0:
            # return Maybe upper_hedge
            maybe_upper_hedge = rooted_super_utree_attrs.aedge2maybe_upper_hedge[parent_aedge]
            return maybe_upper_hedge
            if maybe_upper_hedge is None:
                #upper_hedge of one bicenter_vertex is virtual
                return None
            else:
                upper_hedge = maybe_upper_hedge
                # upper_hedge of non-bicenter_vertex is non-virtual
                return upper_hedge

        # return lower_hedge
        utree = self.super_utree
        lower_hedge = utree.aedge2arbitrary_hedge[parent_aedge]
        if utree.hedge2vertex[lower_hedge] != super_vertex:
            lower_hedge = utree.hedge2another_hedge[lower_hedge]
            assert utree.hedge2vertex[lower_hedge] == super_vertex
        return lower_hedge



# xxx upper_interface_info :: [parent_lower_hedge]
# upper_interface_info is None
# lower_foot_coloring = parent_depth_idx2unsorted_colors
#   :: (num_colors, [[color]])
    @override
    def make_name2named_merged_layer_tablecoloring_at_depth(self, *
        ,depth
        ,upper_interface_info
        ,name2named_layer_tablecoloring_at_depth
        ,lower_foot_coloring
        ):
        # -> name2named_merged_layer_tablecoloring_at_depth
        #
        #named_merged_layer_tablecoloring_at_depth = (num_named_depth_merged_layer_colors, depth_idx2named_local_idx2named_depth_merged_layer_color)
        #

        assert upper_interface_info is None

        (num_lower_layer_exported_colors
        ,curr_layer_depth_idx2unsorted_lower_layer_exported_colors
        ) = lower_foot_coloring

        (num_new_colors
        ,curr_layer_depth_idx2new_color
        ,new_color2sorted_lower_layer_exported_colors
        ) = reindex_complex_colors__old_color_sequence(
            num_lower_layer_exported_colors
            ,curr_layer_depth_idx2unsorted_lower_layer_exported_colors
            ,ordered=False)
        depth_idx2subtree_color = curr_layer_depth_idx2new_color
        num_subtree_colors = num_new_colors


        #name2named_layer_tablecoloring_at_depth
        vertex_tablecoloring = name2named_layer_tablecoloring_at_depth['vertex']
        aedge_tablecoloring = name2named_layer_tablecoloring_at_depth['aedge']
        hedge_tablecoloring = name2named_layer_tablecoloring_at_depth['hedge']

        merged_aedge_tablecoloring = aedge_tablecoloring
        merged_hedge_tablecoloring = hedge_tablecoloring
        # only merged_vertex_tablecoloring need to be calc

        rooted_super_utree_attrs = self.rooted_super_utree_attrs
        depth2vertices1 = rooted_super_utree_attrs.depth2vertices1
        depth_idx2vertex = depth2vertices1[depth]
        num_depth_indices = len(depth_idx2vertex)

        depth_idx2big_color = []
        for depth_idx in range(num_depth_indices):
            vertex2color = vertex_tablecoloring.row2column2color[depth_idx]
            assert 1 <= len(vertex2color) <= 2
            vertex_color = vertex2color[0]
            # parent_vertex_color = 0 if any since virtual

            subtree_color = depth_idx2subtree_color[depth_idx]
            big_color = (vertex_color, subtree_color)
            depth_idx2big_color.append(big_color)

        # sizes for big_color
        sizes = (vertex_tablecoloring.num_colors
                ,num_subtree_colors
                )

        (num_merged_colors
        ,depth_idx2merged_color
        ,merged_color2big_color
        ) = reindex_complex_colors__old_color_tuple(
            sizes, depth_idx2big_color
            )

        depth_idx2vertex2merged_color_ex = []
        for depth_idx in range(num_depth_indices):
            vertex2color = vertex_tablecoloring.row2column2color[depth_idx]
            L = len(vertex2color)
            merged_color_ex = 1+depth_idx2merged_color[depth_idx]
            if L == 1:
                vertex2merged_color_ex = (merged_color_ex,)
            elif L == 2:
                vertex2merged_color_ex = (merged_color_ex, 0)
            else:
                raise logic-error
            depth_idx2vertex2merged_color_ex.append(vertex2merged_color_ex)
        (merged_vertex_tablecoloring
        ) = TableColoring(
            num_colors=1+num_merged_colors
            ,row2column2color=depth_idx2vertex2merged_color_ex
            )

        (name2named_merged_layer_tablecoloring_at_depth
        ) = dict(
            vertex = merged_vertex_tablecoloring
            ,aedge = merged_aedge_tablecoloring
            ,hedge = merged_hedge_tablecoloring
            )
        return name2named_merged_layer_tablecoloring_at_depth










xxxxxxxxxxxxxxxxxxxx
        depth_idx2big_color = []
        for depth_idx, super_vertex in enumerate(depth_idx2vertex):
            vertex2color = vertex_tablecoloring.row2column2color[depth_idx]
            vertex_color = vertex2color[0]
            # parent_vertex_color = virtual if any

            aedge2weight = aedge_tablecoloring.row2column2color[depth_idx]
            hedge2hweight = hedge_tablecoloring.row2column2color[depth_idx]
            assert len(aedge2weight) <= 1
            #assert len(hedge2hweight) in (0, 2)

            if aedge2weight:
                # but same level cannot have both cases
                #   hence we need not (1+) indeed
                parent_aedge_weight = 1+aedge2weight[0]
                lower_hweight = 1+hedge2hweight[0]
                upper_hweight = 1+hedge2hweight[1]
            else:
                parent_aedge_weight = 0
                lower_hweight = 0
                upper_hweight = 0

            subtree_color = depth_idx2subtree_color[depth_idx]
            big_color = (parent_aedge_weight
                        , upper_hweight, lower_hweight
                        , vertex_color, subtree_color
                        )
            depth_idx2big_color.append(big_color)

        # sizes for big_color
        sizes = (1+aedge_tablecoloring.num_colors
                ,1+hedge_tablecoloring.num_colors
                ,1+hedge_tablecoloring.num_colors
                ,vertex_tablecoloring.num_colors
                ,num_subtree_colors
                )
        (depth_idx2merged_color
        ) = reindex_complex_colors__old_color_tuple(
            sizes, depth_idx2big_color
            )
        ...




        name2merged_tablecoloring = {}
        for name, named_layer_tablecoloring_at_depth in name2named_layer_tablecoloring_at_depth.items():
            # upper_interface_info->tablecoloring->lower_foot_coloring -> merged_tablecoloring
            tablecoloring = named_layer_tablecoloring_at_depth
            if name == 'hedge':
            elif name == 'aedge':
                # since at most one aedge
            elif name == 'vertex':
            else:
        TODO xxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxx




    @override
    def make_init_lower_foot_coloring(self):
        # -> lower_foot_coloring
        #
        # lower_foot_coloring = parent_depth_idx2unsorted_colors
        #   :: (num_colors, [[color]])
        rooted_super_utree_attrs = self.rooted_super_utree_attrs
        depth2vertices1 = rooted_super_utree_attrs.depth2vertices1
        depth2depth_idx2vertex = depth2vertices1
        last_layer_depth_idx2vertex = depth2depth_idx2vertex[-1]
        num_parent_depth_indices = len(last_layer_depth_idx2vertex)
        parent_depth_idx2unsorted_colors = [()]*num_parent_depth_indices
            # since vertex in last layer has no children
        return parent_depth_idx2unsorted_colors

    @override
    def make_depth2upper_interface_info(self):
        # -> depth2upper_interface_info
        # -> [upper_interface_info]
        #
        # upper_interface_info is None
        rooted_super_utree_attrs = self.rooted_super_utree_attrs
        depth2vertices1 = rooted_super_utree_attrs.depth2vertices1
        num_depths = len(depth2vertices1)
        return [None]*num_depths


    @override
    def canon_label_and_serialize_subgraphs_at_depth(self, *
        ,depth
        ,name2depth_idx2named_merged_local_rowcoloring_at_depth
        ):
        # -> depth_idx2upper_interface_subgraph_labelling_pairs
        # -> [(upper_interface, subgraph_serialization)]
        #
        # upper_interface_subgraph_labelling_pairs :: [(UpperInterface, UGraphLabelling)]
        # upper_interface :: UpperInterface # user_defined_data
        # subgraph_serialization :: Serialization

        (depth_idx2merged_local_vertex_rowcoloring
        ) = name2depth_idx2named_merged_local_rowcoloring_at_depth['vertex']
        (depth_idx2merged_local_aedge_rowcoloring
        ) = name2depth_idx2named_merged_local_rowcoloring_at_depth['aedge']
        (depth_idx2merged_local_hedge_rowcoloring
        ) = name2depth_idx2named_merged_local_rowcoloring_at_depth['hedge']

        #
        # upper_interface is super_vertex
        rooted_super_utree_attrs = self.rooted_super_utree_attrs
        depth2vertices1 = rooted_super_utree_attrs.depth2vertices1
        depth_idx2vertex = depth2vertices1[depth]
        num_depth_indices = len(depth_idx2vertex)
        for depth_idx, super_vertex in enumerate(depth_idx2vertex):
            merged_local_vertex_rowcoloring = depth_idx2merged_local_vertex_rowcoloring[depth_idx]
            merged_local_aedge_rowcoloring = depth_idx2merged_local_aedge_rowcoloring[depth_idx]
            merged_local_hedge_rowcoloring = depth_idx2merged_local_hedge_rowcoloring[depth_idx]

            num_aedges = len(merged_local_aedge_rowcoloring.column2color)
            upper_interface = super_vertex
            #subgraph_serialization = 
            if num_aedges == 0:
                # only single vertex, no edges
                subgraph_serialization = Serialization(
                    upper_bound = merged_local_vertex_rowcoloring.num_colors
                    ,serialization = merged_local_vertex_rowcoloring.column2color
                    )
            elif num_aedges == 1:
                (this_vertex_color, parent_vertex_color
                ) = merged_local_vertex_rowcoloring.column2color
                [parent_aedge_weight
                ] = merged_local_aedge_rowcoloring.column2color
                (lower_hedge_hweight, upper_hedge_hweight
                ) = merged_local_hedge_rowcoloring.column2color
                serialization = (parent_vertex_color
                                , upper_hedge_hweight
                                , aedge2weight
                                , lower_hedge_hweight
                                , this_vertex_color
                                )

                num_vertex_colors = merged_vertex_tablecoloring.num_colors
                num_aedge_weights = merged_aedge_tablecoloring.num_colors
                num_hedge_hweights = merged_hedge_tablecoloring.num_colors
                upper_bound = max(num_vertex_colors, num_aedge_weights, num_hedge_hweights)

                subgraph_serialization = Serialization(
                    upper_bound = upper_bound
                    ,serialization = serialization
                    )
            else:
                raise logic-error
    @abstractmethod
    def colored_subgraph_labelling2local_upper_color_at_depth(self, *
        ,depth
        ,depth_idx2upper_interface_subgraph_labelling_pairs
        ,ordered_name_seq
        ,name2depth_idx2named_depth_merged_local_compactrecoloring
        ):
        # -> depth_idx2upper_interface_local_upper_color_pairs
        #
        # upper_interface_local_upper_color_pairs :: [(UpperInterface, local_upper_color)]
        raise NotImplementedError
    @abstractmethod
    def make_lower_foot_coloring_of_upper_layer(self, *
        ,depth
        ,depth_idx2upper_interface_local_upper_color_pairs
        ):
        # -> lower_foot_coloring
        raise NotImplementedError



    @abstractmethod
    def make_UGraphLabelling_of_original_entire_graph(self, depth2triple):
        #depth2triple :: [triple]
        #triple =
        #   (name2depth_idx2named_depth_merged_local_compactrecoloring
        #   ,depth_idx2upper_interface_subgraph_labelling_pairs
        #   ,depth_idx2upper_interface_local_upper_color_pairs
        #   )
        raise NotImplementedError



