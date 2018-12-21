
'''
no is_relax_planar_embedding
    using is_relax_planar_ugraph instead
    see: "algo - is fake_embedding relax_planar[ver2].txt"
        requires biconnected ugraph instead of just an embedding
    version1 is error:
        "algo - is fake_embedding relax_planar[ver1][error].txt"
'''
from ..UGraphFakeEmbedding import UGraphFakeEmbedding
#from .is_relax_planar_embedding import is_relax_planar_embedding
from .is_ugraph_fake_embedding_relax_planar_ex import is_ugraph_fake_embedding_relax_planar_ex
from .make_hedge2fake_aedge import make_hedge2fake_aedge
from .make_hedge2fake_counterclockwise_fface import make_hedge2fake_counterclockwise_fface

_get = object.__getattribute__
class Calc_UGraphFakeEmbedding_Info:
    all_attr_seq = '''
        is_ugraph_fake_embedding_relax_planar_ex
        is_ugraph_fake_embedding_relax_planar
        hedge2fake_counterclockwise_fface
        '''.split()
        #is_relax_planar_embedding
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

    '''
    def is_relax_planar_embedding(self):
        ugraph_fake_embedding = _get(self, 'ugraph_fake_embedding')
        return is_relax_planar_embedding(ugraph_fake_embedding)
    '''
    def is_ugraph_fake_embedding_relax_planar(self):
        return not self.is_ugraph_fake_embedding_relax_planar_ex
    def is_ugraph_fake_embedding_relax_planar_ex(self):
        ugraph_fake_embedding = _get(self, 'ugraph_fake_embedding')
        return is_ugraph_fake_embedding_relax_planar_ex(
            ugraph_fake_embedding
            )

        ### old version
        hedge2fake_aedge = make_hedge2fake_aedge(
            num_hedges=ugraph_fake_embedding.num_hedges
            ,hedge2another_hedge=ugraph_fake_embedding.hedge2another_hedge
            )
        return is_ugraph_fake_embedding_relax_planar_ex(
            ugraph_fake_embedding=ugraph_fake_embedding
            ,hedge2aedge=hedge2fake_aedge
            )

    def hedge2fake_counterclockwise_fface(self):
        ugraph_fake_embedding = _get(self, 'ugraph_fake_embedding')
        return make_hedge2fake_counterclockwise_fface(
                hedge2fake_clockwise_fface
                    = ugraph_fake_embedding.hedge2fake_clockwise_fface
                ,hedge2fake_clockwise_prev_hedge_around_vertex
                    = ugraph_fake_embedding.hedge2fake_clockwise_prev_hedge_around_vertex
                )



