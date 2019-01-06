
__all__ = '''
    canon_label_hweighted_nonedgeless_rigid_connected_ugraph_planar_embedding
    '''.split()

from ..UGraphFakeEmbedding import UGraphFakeEmbedding
from ..UGraphFakeEmbeddingLabelling import UGraphFakeEmbeddingLabelling
from .canon_label_rigid_connected_ugraph_fake_embedding_with_root_hedge import \
    canon_label_rigid_connected_ugraph_fake_embedding_with_root_hedge
from .partition_distinguishable_hedges_of_ugraph_planar_embedding__O_E_logE import partition_distinguishable_hedges_of_ugraph_planar_embedding__O_E_logE

class canon_label_hweighted_nonedgeless_rigid_connected_ugraph_planar_embedding:
    '''
input:
    #hweighted rigid_connected nonedgeless ugraph_planar_embedding
    #   fvertex-color and fface-area can merge into hedge-hweight
    nonedgeless_rigid_connected_ugraph_planar_embedding :: UGraphFakeEmbedding
    hedge2hweight
output:
    ugraph_fake_embedding_labelling :: UGraphFakeEmbeddingLabelling
'''

    @classmethod
    def by_partition_distinguishable_hedges__O_E_logE(cls, *
        ,nonedgeless_rigid_connected_ugraph_planar_embedding
        ,hedge2hweight
        ,num_hweights
        ):
        '''
nonedgeless_rigid_connected_ugraph_planar_embedding -> hedge2hweight -> num_hweights -> ugraph_fake_embedding_labelling
ugraph_fake_embedding_labelling :: UGraphFakeEmbeddingLabelling


by partition distinguishable_hedges; O(E*log(E))


ref:
    "[planar_graph][triconnected][isomorphism][1973]A V log V algorithm for isomorphism of triconnected planar graphs[good].pdf"
        # but in this_func, neednot triconnected
        #   requires: planar & rigid_connected
see:
    .make_hedge2hweight.from_color_hweight_area
    by_partition_distinguishable_hedges_ex__O_E_logE
'''
        (ugraph_fake_embedding_labelling, hedge_classes
        ) = cls.by_partition_distinguishable_hedges_ex__O_E_logE(
                nonedgeless_rigid_connected_ugraph_planar_embedding
                    = nonedgeless_rigid_connected_ugraph_planar_embedding
                ,hedge2hweight = hedge2hweight
                ,num_hweights = num_hweights
                )
        return ugraph_fake_embedding_labelling

    @classmethod
    def by_partition_distinguishable_hedges_ex__O_E_logE(cls, *
        ,nonedgeless_rigid_connected_ugraph_planar_embedding
        ,hedge2hweight
        ,num_hweights
        ):
        '''
nonedgeless_rigid_connected_ugraph_planar_embedding -> hedge2hweight -> num_hweights -> (ugraph_fake_embedding_labelling, hedge_classes)

ugraph_fake_embedding_labelling :: UGraphFakeEmbeddingLabelling
hedge_classes :: [[HEdge]]

see:
    by_partition_distinguishable_hedges__O_E_logE
        diff only output
'''
        assert isinstance(nonedgeless_rigid_connected_ugraph_planar_embedding, UGraphFakeEmbedding)

        if not nonedgeless_rigid_connected_ugraph_planar_embedding.calc.is_ugraph_fake_embedding_nonedgeless_rigid_connected: raise ValueError
        if not nonedgeless_rigid_connected_ugraph_planar_embedding.calc.is_ugraph_fake_embedding_planar: raise ValueError

        ugraph_planar_embedding = nonedgeless_rigid_connected_ugraph_planar_embedding
        del nonedgeless_rigid_connected_ugraph_planar_embedding

        assert ugraph_planar_embedding.num_fvertices > 0
        assert ugraph_planar_embedding.num_hedges > 0
        assert ugraph_planar_embedding.num_ffaces > 0

        hedge_classes = partition_distinguishable_hedges_of_ugraph_planar_embedding__O_E_logE(
            ugraph_planar_embedding=ugraph_planar_embedding
            ,maybe_fvertex2color=None
            ,maybe_num_colors=None
            ,maybe_hedge2aedge=None
            ,maybe_aedge2weight=None
            ,maybe_num_weights=None
            ,maybe_hedge2hweight=hedge2hweight
            ,maybe_num_hweights=num_hweights
            ,maybe_fface2area=None
            ,maybe_num_areas=None
            )

        #choose root_hedge
        root_hedge = hedge_classes[0][0]

        ugraph_fake_embedding_labelling = canon_label_rigid_connected_ugraph_fake_embedding_with_root_hedge.by_dfs_preorder__O_E(
            rigid_connected_ugraph_fake_embedding=ugraph_planar_embedding
            ,root_hedge=root_hedge
            )
        return ugraph_fake_embedding_labelling, hedge_classes

