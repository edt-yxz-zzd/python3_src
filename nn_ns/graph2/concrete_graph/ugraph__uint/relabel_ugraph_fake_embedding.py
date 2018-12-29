
__all__ = '''
    relabel_ugraph_fake_embedding
    '''.split()

from .UGraphFakeEmbedding import UGraphFakeEmbedding
from .UGraphFakeEmbeddingLabelling import UGraphFakeEmbeddingLabelling
from .relabel_ugraph_fake_embedding__prime import relabel_ugraph_fake_embedding__prime

def relabel_ugraph_fake_embedding(*
    ,ugraph_fake_embedding__old
    ,ugraph_fake_embedding_labelling__old2new
    ):
    '''UGraphFakeEmbedding -> UGraphFakeEmbeddingLabelling -> UGraphFakeEmbedding
ugraph_fake_embedding__old -> ugraph_fake_embedding_labelling__old2new -> ugraph_fake_embedding__new
'''
    assert isinstance(ugraph_fake_embedding__old, UGraphFakeEmbedding)
    assert isinstance(ugraph_fake_embedding_labelling__old2new, UGraphFakeEmbeddingLabelling)
    if ugraph_fake_embedding__old.num_fvertices != ugraph_fake_embedding_labelling__old2new.num_fvertices: raise ValueError
    if ugraph_fake_embedding__old.num_ffaces != ugraph_fake_embedding_labelling__old2new.num_ffaces: raise ValueError
    if ugraph_fake_embedding__old.num_hedges != ugraph_fake_embedding_labelling__old2new.num_hedges: raise ValueError

    (hedge2fake_clockwise_next_hedge_around_vertex__new
    ,hedge2another_hedge__new
    ,hedge2fvertex__new
    ,hedge2fake_clockwise_fface__new
    ,fvertex2min_hedge__new
    ,fface2min_hedge__new
    ) = relabel_ugraph_fake_embedding__prime(
        ,hedge2fake_clockwise_next_hedge_around_vertex
            = ugraph_fake_embedding__old
                .hedge2fake_clockwise_next_hedge_around_vertex
        ,hedge2another_hedge
            = ugraph_fake_embedding__old.hedge2another_hedge
        ,hedge2fvertex
            = ugraph_fake_embedding__old.hedge2fvertex
        ,hedge2fake_clockwise_fface
            = ugraph_fake_embedding__old.hedge2fake_clockwise_fface



        ,new_hedge2old_hedge
            = ugraph_fake_embedding_labelling__old2new
                .old_hedge2new_hedge.backward_mapping
        ,old_hedge2new_hedge
            = ugraph_fake_embedding_labelling__old2new
                .old_hedge2new_hedge.forward_mapping
        ,old_fvertex2new_fvertex
            = ugraph_fake_embedding_labelling__old2new
                .old_fvertex2new_fvertex.forward_mapping
        ,old_fface2new_fface
            = ugraph_fake_embedding_labelling__old2new
                .old_fface2new_fface.forward_mapping
        )

    fvertex2arbitrary_hedge__new = fvertex2min_hedge__new
    fface2arbitrary_hedge__new = fface2min_hedge__new

    ugraph_fake_embedding__new = UGraphFakeEmbedding.make_UGraphFakeEmbedding__simplest(
        ,hedge2fake_clockwise_next_hedge_around_vertex
            = hedge2fake_clockwise_next_hedge_around_vertex__new
        ,hedge2another_hedge
            = hedge2another_hedge__new
        ,fface2arbitrary_hedge
            = fface2arbitrary_hedge__new
        ,fvertex2arbitrary_hedge
            = fvertex2arbitrary_hedge__new
        )
    return ugraph_fake_embedding__new

