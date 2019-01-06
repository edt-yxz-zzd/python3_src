
r'''
partition_distinguishable_hedges_of_ugraph_planar_embedding__O_E_logE
'''

__all__ = '''
    partition_distinguishable_hedges_of_ugraph_planar_embedding__O_E_logE
    '''.split()


from ..UGraphFakeEmbedding import UGraphFakeEmbedding
from .refine_hedge_partition_of_ugraph_planar_embedding import refine_hedge_partition_of_ugraph_planar_embedding
from ..verify_associate_data import verify_associate_data_ex

from ..inverse_uint_bijection import inverse_uint_bijection
from .make_compact_uint2group_idx import make_compact_uint2group_idx
from seed.algo.bucket_sort.radix_sort_with_table import radix_sort_with_table
from itertools import accumulate, chain


def partition_distinguishable_hedges_of_ugraph_planar_embedding__O_E_logE(*
    ,ugraph_planar_embedding

    ,maybe_fvertex2color
    ,maybe_num_colors

    ,maybe_hedge2aedge
    ,maybe_aedge2weight
    ,maybe_num_weights

    ,maybe_hedge2hweight
    ,maybe_num_hweights

    ,maybe_fface2area
    ,maybe_num_areas
    ):
    '''

input:
    ugraph_planar_embedding
    maybe_hedge2aedge :: None | [AEdge]
        if maybe_num_weights is not None and > 0:
            maybe_hedge2aedge is not None

    maybe_XXX2YYY :: None | [YYY]
    maybe_num_YYYs :: None | UInt
        XXX = fvertex | aedge | hedge | fface
        YYY = color | weight | hweight | area

        (maybe_num_YYYs is None) is (maybe_XXX2YYY is None)
            #both be None or not be None
output:
    hedge_classes :: [[HEdge]]
        # partition in immutable grouped form


#################################################
partition_distinguishable_hedges_of_ugraph_planar_embedding__O_E_logE

partition distinguishable_hedges; O(E*log(E))
ref:
    "[planar_graph][triconnected][isomorphism][1973]A V log V algorithm for isomorphism of triconnected planar graphs[good].pdf"
        # but in this_func, neednot triconnected
        #   requires: planar
        #   #neednot triconnected/connected/rigid_connected


'''

    '''
    fvertex2color, num_colors = make_std_associate_data(
        maybe_input2output=maybe_fvertex2color, maybe_num_outputs=maybe_num_colors)
    aedge2weight, num_weights = make_std_associate_data(
        maybe_input2output=maybe_aedge2weight, maybe_num_outputs=maybe_num_weights)
    hedge2hweight, num_hweights = make_std_associate_data(
        maybe_input2output=maybe_hedge2hweight, maybe_num_outputs=maybe_num_hweights)
    fface2area, num_areas = make_std_associate_data(
        maybe_input2output=maybe_fface2area, maybe_num_outputs=maybe_num_areas)
    '''

    assert isinstance(ugraph_planar_embedding, UGraphFakeEmbedding)
    assert ugraph_planar_embedding.calc.is_ugraph_fake_embedding_planar
    assert ugraph_planar_embedding.num_hedges%2 == 0
    num_aedges = ugraph_planar_embedding.num_hedges//2

    assert verify_associate_data_ex(
        expected_input_size=ugraph_planar_embedding.num_fvertices
        ,maybe_input2output=maybe_fvertex2color
        ,maybe_num_outputs=maybe_num_colors
        )
    assert verify_associate_data_ex(
        expected_input_size=num_aedges
        ,maybe_input2output=maybe_aedge2weight
        ,maybe_num_outputs=maybe_num_weights
        )
    assert verify_associate_data_ex(
        expected_input_size=ugraph_planar_embedding.num_hedges
        ,maybe_input2output=maybe_hedge2hweight
        ,maybe_num_outputs=maybe_num_hweights
        )
    assert verify_associate_data_ex(
        expected_input_size=ugraph_planar_embedding.num_ffaces
        ,maybe_input2output=maybe_fface2area
        ,maybe_num_outputs=maybe_num_areas
        )

    assert maybe_hedge2aedge is None or (
        maybe_aedge2weight is not None
        and verify_associate_data(
            expected_input_size=ugraph_planar_embedding.num_hedges
            ,maybe_input2output=maybe_hedge2aedge
            ,maybe_num_outputs=num_aedges
            )
        and all(maybe_hedge2aedge[hedge] == maybe_hedge2aedge[ugraph_planar_embedding.hedge2another_hedge(hedge)] for hedge in range(ugraph_planar_embedding.num_hedges))
        )

    (hedge2class_idx, class_idx2size, sorted_hedges
    ) = make_hedge2class_idx__via_radix_sort(
        ugraph_planar_embedding=ugraph_planar_embedding
        ,maybe_fvertex2color=maybe_fvertex2color
        ,maybe_num_colors=maybe_num_colors
        ,maybe_hedge2aedge=maybe_hedge2aedge
        ,maybe_aedge2weight=maybe_aedge2weight
        ,maybe_num_weights=maybe_num_weights
        ,maybe_hedge2hweight=maybe_hedge2hweight
        ,maybe_num_hweights=maybe_num_hweights
        ,maybe_fface2area=maybe_fface2area
        ,maybe_num_areas=maybe_num_areas
        )



    #partition hedges by hedge2class_idx
    position2hedge = list(sorted_hedges)
    hedge2position = list(inverse_uint_bijection(position2hedge))
    hedge2class_idx = list(hedge2class_idx)
    class_idx2end = list(accumulate(class_idx2size))
    class_idx2begin = [0] if class_idx2end else []
    class_idx2begin.extend(class_idx2end[:-1])
    hedge_classes = refine_hedge_partition_of_ugraph_planar_embedding(
            ugraph_planar_embedding=ugraph_planar_embedding
            ,position2hedge=position2hedge
            ,hedge2position=hedge2position
            ,hedge2class_idx=hedge2class_idx
            ,class_idx2begin=class_idx2begin
            ,class_idx2end=class_idx2end
            )
    return hedge_classes

def make_hedge2class_idx__via_radix_sort(*
    ,ugraph_planar_embedding

    ,maybe_fvertex2color
    ,maybe_num_colors

    ,maybe_hedge2aedge
    ,maybe_aedge2weight
    ,maybe_num_weights

    ,maybe_hedge2hweight
    ,maybe_num_hweights

    ,maybe_fface2area
    ,maybe_num_areas
    ):
    # -> (hedge2class_idx, class_idx2size, sorted_hedges)
    def maybe_num_XXXs2num_XXXs(maybe_num_XXXs):
        if maybe_num_XXXs is None:
            return 0
        num_XXXs = maybe_num_XXXs
        return num_XXXs
    num_colors = maybe_num_XXXs2num_XXXs(maybe_num_colors)
    num_weights = maybe_num_XXXs2num_XXXs(maybe_num_weights)
    num_hweights = maybe_num_XXXs2num_XXXs(maybe_num_hweights)
    num_areas = maybe_num_XXXs2num_XXXs(maybe_num_areas)
    if num_colors > 0:
        fvertex2color = maybe_fvertex2color
    if num_weights > 0:
        aedge2weight = maybe_aedge2weight
        hedge2aedge = maybe_hedge2aedge
    if num_hweights > 0:
        hedge2hweight = maybe_hedge2hweight
    if num_areas > 0:
        fface2area = maybe_fface2area

    def hedge2class_data__func(this_hedge):
        that_hedge = ugraph_planar_embedding.hedge2another_hedge(this_hedge)
        class_data__left = hedge2class_data__half__func(this_hedge)
        class_data__right = hedge2class_data__half__func(that_hedge)
        class_data = merge_two_half(class_data__left, class_data__right)
        return class_data
    def hedge2class_data__half__func(hedge):
        fvertex = ugraph_planar_embedding.hedge2fvertex[hedge]
        fface = ugraph_planar_embedding.hedge2fake_clockwise_fface[hedge]
        if num_weights > 0:
            aedge = hedge2aedge[hedge]

        class_data__half = [
            ugraph_planar_embedding.fvertex2degree[fvertex]
            ,ugraph_planar_embedding.fface2degree[fface]
            ]
        if num_colors > 0:
            class_data__half.append(fvertex2color[fvertex])
        if num_weights > 0:
            class_data__half.append(aedge2weight[aedge])
        if num_hweights > 0:
            class_data__half.append(hedge2hweight[hedge])
        if num_areas > 0:
            class_data__half.append(fface2area[fface])
        return tuple(class_data__half)


    def make_alphabet_sizes():
        alphabet_sizes__half = make_alphabet_sizes__half()
        return merge_two_half(alphabet_sizes__half, alphabet_sizes__half)
    def make_alphabet_sizes__half():
        alphabet_sizes__half = [fvertex_degree_UB, fface_degree_UB]
        if num_colors > 0:
            alphabet_sizes__half.append(num_colors)
        if num_weights > 0:
            alphabet_sizes__half.append(num_weights)
        if num_hweights > 0:
            alphabet_sizes__half.append(num_hweights)
        if num_areas > 0:
            alphabet_sizes__half.append(num_areas)
        return tuple(alphabet_sizes__half)

    def merge_two_half(left_seq, right_seq):
        assert len(left_seq) == len(right_seq) == half_size
        return tuple(chain.from_iterable(zip(left_seq, right_seq)))
        return left_seq + right_seq
    half_size = 2 + sum([num_colors > 0, num_weights > 0, num_hweights > 0, num_areas > 0])

    hedge2class_data = tuple(map(hedge2class_data__func
                            , range(ugraph_planar_embedding.num_hedges)))

    fvertex_degree_UB = 1+max(ugraph_planar_embedding.fvertex2degree, default=-1)
    fface_degree_UB = 1+max(ugraph_planar_embedding.fface2degree, default=-1)

    alphabet_sizes = make_alphabet_sizes()
    table = tuple([] for _ in range(max(alphabet_sizes)))
    num_hedges = ugraph_planar_embedding.num_hedges
    key = hedge2class_data.__getitem__

    sorted_hedges = radix_sort_with_table(alphabet_sizes, range(num_hedges), table, key=key)

    (hedge2group_idx, group_idx2key, group_idx2size
    ) = make_compact_uint2group_idx(num_hedges, sorted_hedges, key=key)

    hedge2class_idx = hedge2group_idx
    class_idx2size = group_idx2size
    return hedge2class_idx, class_idx2size, sorted_hedges






