
__all__ = '''
    make_hedge2hweight
    '''.split()

from ..is_uint_sequence import is_uint_sequence
from .make_compact_uint2group_idx import make_compact_uint2group_idx
from ..imports__bucket_sort import radix_sort

class make_hedge2hweight:
    @classmethod
    def from_color_hweight_area(cls, *
        ,ugraph_fake_embedding
        ,fvertex2color
        ,hedge2hweight
        ,fface2area
        ,num_colors
        ,num_hweights
        ,num_areas
        ):
        '''
        -> (hedge2new_hweight, new_hweight2old_color_hweight_area_triple)
'''
        assert isinstance(ugraph_fake_embedding, UGraphFakeEmbedding)

        assert is_uint_sequence(fvertex2color)
        assert is_uint_sequence(hedge2hweight)
        assert is_uint_sequence(fface2area)
        assert len(fvertex2color) == ugraph_fake_embedding.num_fvertices
        assert len(hedge2hweight) == ugraph_fake_embedding.num_hedges
        assert len(fface2area) == ugraph_fake_embedding.num_ffaces
        assert num_colors <= ugraph_fake_embedding.num_fvertices
        assert num_hweights <= ugraph_fake_embedding.num_hedges
        assert num_areas <= ugraph_fake_embedding.num_ffaces
        assert max(fvertex2color, default=-1) < num_colors
        assert max(hedge2hweight, default=-1) < num_hweights
        assert max(fface2area, default=-1) < num_areas
        assert min(fvertex2color, default=0) >= 0
        assert min(hedge2hweight, default=0) >= 0
        assert min(fface2area, default=0) >= 0

        def hedge2triple__func(hedge):
            fvertex = ugraph_fake_embedding.hedge2fvertex[hedge]
            fface = ugraph_fake_embedding.hedge2fake_clockwise_fface[hedge]
            color = fvertex2color[fvertex]
            hweight = hedge2hweight[hedge]
            area = fface2area[fface]
            return (color, hweight, area)

        #hedge2triple = tuple(map(hedge2triple__func, range(ugraph_fake_embedding.num_hedges)))

        alphabet_sizes = (num_colors, num_hweights, num_areas)
        #table = tuple([] for _ in max(alphabet_sizes))
        num_hedges = ugraph_fake_embedding.num_hedges
        key = hedge2triple__func
        sorted_hedges = radix_sort(alphabet_sizes, range(num_hedges), key=key)


        (hedge2new_hweight
        ,new_hweight2old_color_hweight_area_triple
        ,new_hweight2size
        ) = make_compact_uint2group_idx(num_hedges, sorted_hedges, key=key)
        return tuple(hedge2new_hweight), tuple(new_hweight2old_color_hweight_area_triple)

