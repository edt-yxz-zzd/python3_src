
'''
CanonLabelSuperUTreeABC
    do most boring boilerplate code
'''

__all__ = '''
    CanonLabelSuperUTreeABC
    '''.split()

from ..IMaker4UTree import IMaker4UTree # make_all_rooted_utree_attrs
from ..UGraphLabelling import UGraphLabelling
from ..Coloring import (
    Serialization
    ,CompactRecoloring
    ,RowColoring
    ,TableColoring

    ,make_rowcoloring_from_color2columns
    ,make_column2color_from_color2columns
    )

from ..locally_reindex_global_colors import (
    locally_reindex_global_colors
    ,locally_reindex_global_colors__depth
    #,locally_reindex_global_colors__virtual_row_layer
    )
from seed.verify.common_verify import is_Sequence
    #is_uint_sequence
    #is_UInt
from .abc import ABC, abstractmethod
#from itertools import chain












class CanonLabelSuperUTreeABC(ABC):
    '''

# super_XXX - obj of super_utree
#   to distinguish the original_entire_graph and subgraphs
super_utree
super_vertex
super_aedge
super_hedge


# named_XXX - depends on "name"
# global_XXX - obj of the original_entire_graph
# local_XXX - obj of subgraphs; depends on "super_vertex"
name
    i.e. "vertex"/"aedge"/"hedge"
named_global_idx/named_local_idx
    i.e. vertex/aedge/hedge
named_global_color/named_local_color
    i.e. color/weight/hweight
num_named_global_colors/num_named_local_colors
    i.e. num_colors/num_weights/num_hweights
named_global_color_ex
    = 0 | 1+named_global_color
num_named_global_colors_ex
    = 1+named_global_color_ex


# depth_XXX - depends on "depth"
# named_depth_XXX - depends on "name&depth"
# named_depth_local_XXX - depends on "name&super_vertex"
#   super_vertex <==> (depth, depth_idx)
# named_depth_layer_XXX - depends on "name&depth"
#
depth
    using center as root
    i.e. unicenter_vertex as root_vertex
         bicenter_aedge as root_aedge
depth_idx
    (depth, depth_idx) <==> super_vertex
    by: depth2depth_idx2vertex <==> (vertex2depth, vertex2depth_idx)
depth_layer_color
depth_local_color


named_global_rowcoloring :: RowColoring
    # (num_named_global_colors, named_global_idx2named_global_color)
    # :: (UInt, [UInt])
    # :: (UInt, [UInt[0..num_named_global_colors-1]])
    # num_named_global_colors <= num_named_global_indices = len(named_global_idx2named_global_color)

named_depth_layer_tablecoloring :: TableColoring
    # (num_named_depth_layer_colors, depth_idx2named_local_idx2named_depth_layer_color)



##########################################################
##########################################################
##########################################################
abstract_methods:
    `canon_label_and_serialize_subgraphs_at_depth
    `colored_subgraph_labelling2local_upper_color_at_depth
    `make_IMaker4UTree
    `make_UGraphLabelling_of_original_entire_graph
    `make_depth2upper_interface_info
    `make_init_lower_foot_coloring
    `make_lower_foot_coloring_of_upper_layer
    `make_name2named_merged_layer_tablecoloring_at_depth
    `named_local_idx2maybe_named_global_idx
    `super_vertex2num_named_local_indices

'''
    #__slots__ = ()

    def __init__(self, *
        , super_utree, name2named_global_rowcoloring, ordered_name_seq
        ):
        # name2named_global_rowcoloring :: Map Name RowColoring
        self.super_utree = super_utree
        self.name2named_global_rowcoloring = name2named_global_rowcoloring
        self.rooted_super_utree_attrs = self.make_all_rooted_utree_attrs(super_utree)
        self.ordered_name_seq = ordered_name_seq

        assert all(isinstance(named_global_rowcoloring, RowColoring)
            for named_global_rowcoloring in name2named_global_rowcoloring.values()
            )
        assert is_Sequence(ordered_name_seq)
        assert len(ordered_name_seq) == len(name2named_global_rowcoloring)
        assert frozenset(ordered_name_seq) == frozenset(name2named_global_rowcoloring)

    @abstractmethod
    def super_vertex2num_named_local_indices(self, name, super_vertex):
        # -> UInt
        # -> num_named_local_indices
        raise NotImplementedError
    @abstractmethod
    def named_local_idx2maybe_named_global_idx(self, name, super_vertex, named_local_idx):
        # -> (None|UInt)
        # -> (None|named_global_idx)
        # named_local_idx may be virtual one
        # color virtual_named_local_idx with a special color
        #
        # use: locally_reindex_global_colors
        raise NotImplementedError






    @abstractmethod
    def make_IMaker4UTree(self, utree):
        # -> IMaker4UTree
        raise NotImplementedError
    def make_all_rooted_utree_attrs(self, utree):
        # -> namespace of rooted_utree_attrs...
        maker = self.make_IMaker4UTree(utree)
        ns = maker.make_all_rooted_utree_attrs(maybe_either_root=None)
        return ns
        '''
            aedge2maybe_upper_hedge
            vertex2maybe_parent_aedge
            either_center
            vertex2child_aedges
            vertex2maybe_parent_vertex
            vertex2depth
            depth2vertices1
            depth2depth_idx2vertex
            vertex2depth_idx
        '''


    def make_name2depth2named_depth_layer_tablecoloring(self, *
        ,name2named_global_rowcoloring
        ,depth2depth_idx2super_vertex
        ):
        # -> name2depth2named_depth_layer_tablecoloring
        #
        # coloring per depth # depth as layer
        #
        name2depth2named_depth_layer_tablecoloring = {
            name : self.make_depth2named_depth_layer_tablecoloring(
                name=name
                ,named_global_rowcoloring=named_global_rowcoloring
                ,depth2depth_idx2super_vertex=depth2depth_idx2super_vertex
                )
            for name, named_global_rowcoloring in name2named_global_rowcoloring.items()
            }
        return name2depth2named_depth_layer_tablecoloring
    def make_depth2named_depth_layer_tablecoloring(self, *
        , name, named_global_rowcoloring, depth2depth_idx2super_vertex
        ):
        # -> depth2named_depth_layer_tablecoloring
        # -> [(num_named_depth_layer_colors, depth_idx2named_local_idx2named_depth_layer_color)]
        num_named_global_colors = named_global_rowcoloring.num_colors
        named_global_idx2named_global_color = named_global_rowcoloring.column2color
        '''
        locally_reindex_global_colors__depth
            :: num_global_colors -> depth2row2column2global_color
            -> (depth2num_depth_local_colors, depth2row2column2depth_local_color, depth2depth_local_color2global_color)
        '''

        #super_vertex2num_named_local_indices
        #named_local_idx2maybe_named_global_idx
        def make_named_global_color_ex(name, super_vertex, named_local_idx):
            may_named_global_idx = self.named_local_idx2maybe_named_global_idx(name, super_vertex, named_local_idx)
            if may_named_global_idx is None:
                named_global_color_ex = 0
            else:
                named_global_idx = may_named_global_idx
                named_global_color = named_global_idx2named_global_color[named_global_idx]
                named_global_color_ex = 1+named_global_color
            return named_global_color_ex

        num_named_global_colors_ex = 1+num_named_global_colors
        depth2depth_idx2named_local_idx2named_global_color_ex = [
            [[make_named_global_color_ex(name, super_vertex, named_local_idx)
                    for named_local_idx in range(self.super_vertex2num_named_local_indices(name, super_vertex))
                ] for depth_idx, super_vertex in enumerate(depth_idx2super_vertex)
            ] for depth, depth_idx2super_vertex in enumerate(depth2depth_idx2super_vertex)
            ]

        (depth2num_named_depth_layer_colors
        ,depth2depth_idx2named_local_idx2named_depth_layer_color
        ,depth2named_depth_layer_color2named_global_color_ex
        ) = locally_reindex_global_colors__depth(
            num_global_colors
                =num_named_global_colors_ex
            ,depth2row2column2global_color
                =depth2depth_idx2named_local_idx2named_global_color_ex
            )

        # (depth2num_named_depth_layer_colors, depth2depth_idx2named_local_idx2named_depth_layer_color)
        depth2named_depth_layer_tablecoloring = tuple(
            TableColoring(
                num_colors
                    =num_named_depth_layer_colors
                ,row2column2color
                    =depth_idx2named_local_idx2named_depth_layer_color)
            for (num_named_depth_layer_colors
                ,depth_idx2named_local_idx2named_depth_layer_color
                ) in zip(
                depth2num_named_depth_layer_colors
                ,depth2depth_idx2named_local_idx2named_depth_layer_color)
            )
        return depth2named_depth_layer_tablecoloring

    def canon_label_super_utree(self):
        # -> UGraphLabelling
        ordered_name_seq = self.ordered_name_seq
        super_utree = self.super_utree
        rooted_super_utree_attrs = self.rooted_super_utree_attrs
        depth2depth_idx2super_vertex = rooted_super_utree_attrs.depth2depth_idx2vertex
        name2named_global_rowcoloring = self.name2named_global_rowcoloring

        (name2depth2named_depth_layer_tablecoloring
        ) = self.make_name2depth2named_depth_layer_tablecoloring(
            name2named_global_rowcoloring=name2named_global_rowcoloring
            ,depth2depth_idx2super_vertex=depth2depth_idx2super_vertex
            )

        depth2upper_interface_info = self.make_depth2upper_interface_info()
        lower_foot_coloring = self.make_init_lower_foot_coloring()
        saved_triples = []
        num_depths = len(depth2depth_idx2super_vertex)
        for depth in reversed(range(num_depths)):
            (name2named_layer_tablecoloring_at_depth
            ) = self.make_name2named_layer_tablecoloring_at_depth(
                depth = depth
                ,name2depth2named_depth_layer_tablecoloring
                    = name2depth2named_depth_layer_tablecoloring
                )
                #named_layer_tablecoloring_at_depth = (num_named_depth_layer_colors, depth_idx2named_local_idx2named_depth_layer_color)
            upper_interface_info = depth2upper_interface_info[depth]



            (name2named_merged_layer_tablecoloring_at_depth
            ) = self.make_name2named_merged_layer_tablecoloring_at_depth(
                depth = depth
                ,upper_interface_info
                    = upper_interface_info
                ,name2named_layer_tablecoloring_at_depth
                    = name2named_layer_tablecoloring_at_depth
                ,lower_foot_coloring
                    = lower_foot_coloring
                )
                #named_merged_layer_tablecoloring_at_depth = (num_named_depth_merged_layer_colors, depth_idx2named_local_idx2named_depth_merged_layer_color)

            (name2depth_idx2named_merged_local_rowcoloring_at_depth
            ,name2depth_idx2named_depth_merged_local_compactrecoloring
            ) = self.make_name2depth_idx2named_merged_local_rowcoloring_at_depth_ex(
                depth=depth
                ,name2named_merged_layer_tablecoloring_at_depth
                    = name2named_merged_layer_tablecoloring_at_depth
                )
                #named_merged_local_rowcoloring_at_depth :: RowColoring
                #   # (num_named_depth_merged_local_colors, named_local_idx2named_depth_merged_local_color)
                #named_depth_merged_local_compactrecoloring :: CompactRecoloring
                #   # (num_named_depth_merged_layer_colors, named_depth_merged_local_color2named_depth_merged_layer_color)



            (depth_idx2upper_interface_subgraph_labelling_pairs
            ) = self.canon_label_and_serialize_subgraphs_at_depth(
                depth = depth
                ,name2depth_idx2named_merged_local_rowcoloring_at_depth
                    = name2depth_idx2named_merged_local_rowcoloring_at_depth
                )
                # upper_interface_subgraph_labelling_pairs :: [(UpperInterface, Serialization)]
                # upper_interface - user_defined_data
                #   e.g. hedge(used to connect to upper layer)
                # subgraph_serialization :: Serialization
                #   subgraph_serialization is dependent on upper_interface
                # i.e. upper_interface_subgraph_labelling_pair is a dependent sum type
                #   e.g. (('vertex', upper_layer_depth_idx, upper_layer_local_vertex), subgraph_merged_layer_coloring_serialization)
                #   e.g. (('hedge', upper_layer_depth_idx, upper_layer_local_hedge), planar_subgraph_merged_layer_coloring_imaged_embedding_serialization)
                #
                # old:
                # upper_interface_subgraph_labelling_pairs :: [(UpperInterface, UGraphLabelling)]
                # subgraph_labelling :: UGraphLabelling
                #

            #upper_interface <<== subgraph + subgraph_labelling
            #std_subgraph <<== subgraph + subgraph_labelling
            #std_subgraph_structure_serialization <<== std_subgraph
            #std_subgraph_named_merged_local_coloring_serialization <<== std_subgraph + named_merged_local_rowcoloring_at_depth
            #std_subgraph_named_merged_layer_coloring_serialization <<== std_subgraph_named_merged_local_coloring_serialization + named_depth_merged_local_compactrecoloring
            #xxx std_subgraph_complete_serialization <<== std_subgraph_structure_serialization + [std_subgraph_named_merged_layer_coloring_serialization]
            # TODO
                # subgraph_serialization :: Serialization
                #   subgraph_serialization donot contain color info
                # subgraph_structure_serialization :: Serialization
                # subgraph_merged_local_coloring_serialization :: Serialization
                # subgraph_merged_layer_coloring_serialization :: Serialization
                #

            (depth_idx2upper_interface_local_upper_color_pairs
            #std - applied subgraph_labelling
            #,local_upper_color2std_subgraph_serialization
            #,local_upper_color2name2std_named_depth_merged_local_compactrecoloring
            ) = self.colored_subgraph_labelling2local_upper_color_at_depth(
                depth = depth
                ,depth_idx2upper_interface_subgraph_labelling_pairs
                    = depth_idx2upper_interface_subgraph_labelling_pairs
                ,ordered_name_seq
                    = ordered_name_seq
                ,name2depth_idx2named_depth_merged_local_compactrecoloring
                    = name2depth_idx2named_depth_merged_local_compactrecoloring
                )
                # upper_interface_local_upper_color_pairs :: [(UpperInterface, local_upper_color)]


            (lower_foot_coloring
            ) = self.make_lower_foot_coloring_of_upper_layer(
                depth = depth
                ,depth_idx2upper_interface_local_upper_color_pairs
                    = depth_idx2upper_interface_local_upper_color_pairs
                )

            # save
            #   to serialize the original_entire_graph
            saved_triples.append((
                name2depth_idx2named_depth_merged_local_compactrecoloring
                ,depth_idx2upper_interface_subgraph_labelling_pairs
                ,depth_idx2upper_interface_local_upper_color_pairs
                ))

        depth2triple = tuple(reversed(saved_triples)); del saved_triples

        (ugraph_labelling
        )= self.make_UGraphLabelling_of_original_entire_graph(
            depth2triple
            )
        assert isinstance(ugraph_labelling, UGraphLabelling)
        return ugraph_labelling
    #end of canon_label_super_utree


    @abstractmethod
    def make_UGraphLabelling_of_original_entire_graph(self, depth2triple):
        #depth2triple :: [triple]
        #triple =
        #   (name2depth_idx2named_depth_merged_local_compactrecoloring
        #   ,depth_idx2upper_interface_subgraph_labelling_pairs
        #   ,depth_idx2upper_interface_local_upper_color_pairs
        #   )
        raise NotImplementedError



    @abstractmethod
    def make_init_lower_foot_coloring(self):
        # -> lower_foot_coloring
        raise NotImplementedError
    @abstractmethod
    def make_depth2upper_interface_info(self):
        # -> depth2upper_interface_info
        # -> [upper_interface_info]
        raise NotImplementedError
    def make_name2named_layer_tablecoloring_at_depth(self, *
        ,depth
        ,name2depth2named_depth_layer_tablecoloring
        ):
        # -> name2named_layer_tablecoloring_at_depth
        #
        #named_layer_tablecoloring_at_depth = (num_named_depth_layer_colors, depth_idx2named_local_idx2named_depth_layer_color)
        #ordered_name_seq = self.ordered_name_seq
        name2named_layer_tablecoloring_at_depth = {
            name : depth2named_depth_layer_tablecoloring[depth]
            for name, depth2named_depth_layer_tablecoloring
                in name2depth2named_depth_layer_tablecoloring.items()
            }
        return name2named_layer_tablecoloring_at_depth
    @abstractmethod
    def make_name2named_merged_layer_tablecoloring_at_depth(self, *
        ,depth
        ,upper_interface_info
        ,name2named_layer_tablecoloring_at_depth
        ,lower_foot_coloring
        ):
        # -> name2named_merged_layer_tablecoloring_at_depth
        #
        #named_merged_layer_tablecoloring_at_depth = (num_named_depth_merged_layer_colors, depth_idx2named_local_idx2named_depth_merged_layer_color)
        raise NotImplementedError
    def make_name2depth_idx2named_merged_local_rowcoloring_at_depth_ex(self, *
        ,depth
        ,name2named_merged_layer_tablecoloring_at_depth
        ):
        # -> (name2depth_idx2named_merged_local_rowcoloring_at_depth
        #    ,name2depth_idx2named_depth_merged_local_compactrecoloring)
        #
        #named_merged_layer_tablecoloring_at_depth = (num_named_depth_merged_layer_colors, depth_idx2named_local_idx2named_depth_merged_layer_color)
        #
        #named_merged_local_rowcoloring_at_depth :: RowColoring
        #   # (num_named_depth_merged_local_colors, named_local_idx2named_depth_merged_local_color)
        #named_depth_merged_local_compactrecoloring :: CompactRecoloring
        #   # (num_named_depth_merged_layer_colors, named_depth_merged_local_color2named_depth_merged_layer_color)
        #
        #NOTE: super_vertex <==> (depth, depth_idx) <==> subgraph
        #
        #NOTE: named_depth_merged_layer_color ==>> named_depth_merged_local_color
        #       input color is merged but whole layer at depth
        #           tablecoloring
        #       output color is merged and local to each subgraph
        #           depth_idx2rowcoloring # not tablecoloring
        #
        '''
        locally_reindex_global_colors
        :: num_global_colors -> row2column2global_color
        -> (row2num_local_colors, row2column2local_color, row2local_color2global_color)
        '''
        name2depth_idx2named_merged_local_rowcoloring_at_depth = {}
        name2depth_idx2named_depth_merged_local_compactrecoloring = {}
        for name, named_merged_layer_tablecoloring_at_depth in name2named_merged_layer_tablecoloring_at_depth.items():
            # tablecoloring -> depth_idx2rowcoloring
            # tablecoloring -> depth_idx2compactrecoloring
            tablecoloring = named_merged_layer_tablecoloring_at_depth

            (row2num_local_colors
            ,row2column2local_color
            ,row2local_color2global_color
            ) = locally_reindex_global_colors(
                num_global_colors=tablecoloring.num_colors
                ,row2column2global_color=tablecoloring.row2column2color
                )
            depth_idx2rowcoloring = tuple(
                RowColoring(
                    num_colors=num_local_colors
                    ,column2color=column2local_color
                    )
                for num_local_colors, column2local_color
                    in zip(row2num_local_colors, row2column2local_color)
                )
            depth_idx2compactrecoloring = tuple(
                CompactRecoloring(
                    num_old_colors=tablecoloring.num_colors
                    ,compact_new_color2old_color=local_color2global_color
                    )
                for local_color2global_color in row2local_color2global_color
                )
            name2depth_idx2named_merged_local_rowcoloring_at_depth[name
                ] = depth_idx2rowcoloring
            name2depth_idx2named_depth_merged_local_compactrecoloring[name
                ] = depth_idx2compactrecoloring
        return (name2depth_idx2named_merged_local_rowcoloring_at_depth
                ,name2depth_idx2named_depth_merged_local_compactrecoloring
                )
    @abstractmethod
    def canon_label_and_serialize_subgraphs_at_depth(self, *
        ,depth
        ,name2depth_idx2named_merged_local_rowcoloring_at_depth
        ):
        # -> depth_idx2upper_interface_subgraph_labelling_pairs
        # -> [(upper_interface, subgraph_labelling, subgraph_serialization)]
        #
        # upper_interface_subgraph_labelling_pairs :: [(UpperInterface, UGraphLabelling)]
        # upper_interface :: UpperInterface # user_defined_data
        # subgraph_labelling :: UGraphLabelling
        # subgraph_serialization :: Serialization
        #   subgraph_serialization donot contain color info
        #
        raise NotImplementedError
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









###############################################


r'''
locally_reindex_global_colors
    :: num_global_colors -> row2column2global_color
    -> (row2num_local_colors, row2column2local_color, row2local_color2global_color)

locally_reindex_global_colors__depth
    :: num_global_colors -> depth2row2column2global_color
    -> (depth2num_depth_local_colors, depth2row2column2depth_local_color, depth2depth_local_color2global_color)

locally_reindex_global_colors__virtual_row_layer
    :: num_global_colors -> row2column2global_color
    -> num_layers -> row2layer
    -> (layer2num_layer_local_colors, row2column2layer_local_color, layer2layer_local_color2global_color)


'''

if __name__ == '__main__':
    classes = [CanonLabelSuperUTreeABC]
    excludes = '''
        logic
        error
        '''.split()

    from seed.helper.ongo import main
    main(modules=[__name__], classes=classes, excludes=excludes)


