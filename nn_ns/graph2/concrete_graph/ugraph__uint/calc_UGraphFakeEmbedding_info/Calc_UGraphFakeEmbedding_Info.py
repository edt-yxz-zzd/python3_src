
__all__ = '''
    Calc_UGraphFakeEmbedding_Info
    '''.split()

from ..UGraphFakeEmbedding import UGraphFakeEmbedding
#from .is_relax_planar_embedding import is_relax_planar_embedding
#from .is_ugraph_fake_embedding_relax_planar_ex import is_ugraph_fake_embedding_relax_planar_ex
from .ugraph_fake_embedding2maybe_non_planar_condition import ugraph_fake_embedding2maybe_non_planar_condition
from .make_hedge2fake_aedge import make_hedge2fake_aedge
from .make_hedge2fake_counterclockwise_fface import make_hedge2fake_counterclockwise_fface

_get = object.__getattribute__
class Calc_UGraphFakeEmbedding_Info:
    all_attr_seq = '''
        maybe_ugraph_fake_embedding_non_planar_condition
        is_ugraph_fake_embedding_planar
        hedge2fake_counterclockwise_fface
        '''.split()
        #is_relax_planar_embedding
        #is_ugraph_fake_embedding_relax_planar
        #is_ugraph_fake_embedding_relax_planar_ex
    all_attr_set = frozenset(all_attr_seq)
    def __init__(self, ugraph_fake_embedding):
        assert isinstance(ugraph_fake_embedding, UGraphFakeEmbedding)
        self.ugraph_fake_embedding = ugraph_fake_embedding
        self.cache = {}
    def __getattribute__(self, attr):
        if attr in UGraphFakeEmbedding.all_UGraphFakeEmbedding_attr_set:
            ugraph_fake_embedding = _get(self, 'ugraph_fake_embedding')
            return getattr(ugraph_fake_embedding, attr)

        if attr not in __class__.all_attr_set:
            raise AttributeError(attr)

        cache = _get(self, 'cache')
        try:
            return cache[attr]
        except KeyError:
            r = _get(self, attr)()
            r = cache.setdefault(attr, r)
            return r

    def is_ugraph_fake_embedding_planar(self):
        return not self.maybe_ugraph_fake_embedding_non_planar_condition
    def maybe_ugraph_fake_embedding_non_planar_condition(self):
        ugraph_fake_embedding = _get(self, 'ugraph_fake_embedding')
        return ugraph_fake_embedding2maybe_non_planar_condition(
            ugraph_fake_embedding
            )


    def hedge2fake_counterclockwise_fface(self):
        ugraph_fake_embedding = _get(self, 'ugraph_fake_embedding')
        return make_hedge2fake_counterclockwise_fface(
                hedge2fake_clockwise_fface
                    = ugraph_fake_embedding.hedge2fake_clockwise_fface
                ,hedge2fake_clockwise_prev_hedge_around_vertex
                    = ugraph_fake_embedding.hedge2fake_clockwise_prev_hedge_around_vertex
                )



