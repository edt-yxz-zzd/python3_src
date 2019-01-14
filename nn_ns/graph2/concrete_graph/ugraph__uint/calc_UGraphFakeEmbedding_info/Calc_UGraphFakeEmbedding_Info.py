
__all__ = '''
    Calc_UGraphFakeEmbedding_Info
    '''.split()

from ..UGraphFakeEmbedding import UGraphFakeEmbedding
#from .is_relax_planar_embedding import is_relax_planar_embedding
#from .is_ugraph_fake_embedding_relax_planar_ex import is_ugraph_fake_embedding_relax_planar_ex
from .ugraph_fake_embedding2maybe_nonplanar_condition import ugraph_fake_embedding2maybe_nonplanar_condition
from .make_hedge2fake_aedge import make_hedge2fake_aedge
from .make_hedge2fake_counterclockwise_fface import make_hedge2fake_counterclockwise_fface
from .ugraph_fake_embedding2num_nonedgeless_connected_components import ugraph_fake_embedding2num_nonedgeless_connected_components

import weakref # ref

_get = object.__getattribute__
def _get_ugraph_fake_embedding(self):
    return _get(self, '_ugraph_fake_embedding_ref')()
def _get_cache(self):
    return _get(self, '_cache')
class Calc_UGraphFakeEmbedding_Info:
    all_attr_seq = '''
        maybe_ugraph_fake_embedding_nonplanar_condition
        is_ugraph_fake_embedding_planar
        hedge2fake_counterclockwise_fface
        is_ugraph_fake_embedding_nonedgeless_rigid_connected
        num_nonedgeless_connected_components
        '''.split()
        #is_relax_planar_embedding
        #is_ugraph_fake_embedding_relax_planar
        #is_ugraph_fake_embedding_relax_planar_ex
    all_attr_set = frozenset(all_attr_seq)
    def __init__(self, ugraph_fake_embedding):
        assert isinstance(ugraph_fake_embedding, UGraphFakeEmbedding)
        """
        global UGraphFakeEmbedding
        try:
            UGraphFakeEmbedding
        except NameError:
            from ..UGraphFakeEmbedding import UGraphFakeEmbedding
            UGraphFakeEmbedding
        """

        self._ugraph_fake_embedding_ref = weakref.ref(ugraph_fake_embedding)
        self._cache = {}
    def __getattribute__(self, attr):
        if attr in UGraphFakeEmbedding.all_UGraphFakeEmbedding_attr_set:
            ugraph_fake_embedding = _get_ugraph_fake_embedding(self)
            return getattr(ugraph_fake_embedding, attr)

        if attr not in __class__.all_attr_set:
            raise AttributeError(attr)

        cache = _get_cache(self)
        try:
            return cache[attr]
        except KeyError:
            r = _get(self, attr)()
            r = cache.setdefault(attr, r)
            return r

    def is_ugraph_fake_embedding_planar(self):
        return not self.maybe_ugraph_fake_embedding_nonplanar_condition
    def maybe_ugraph_fake_embedding_nonplanar_condition(self):
        ugraph_fake_embedding = _get_ugraph_fake_embedding(self)
        return ugraph_fake_embedding2maybe_nonplanar_condition(
            ugraph_fake_embedding
            )


    def hedge2fake_counterclockwise_fface(self):
        ugraph_fake_embedding = _get_ugraph_fake_embedding(self)
        return make_hedge2fake_counterclockwise_fface(
                hedge2fake_clockwise_fface
                    = ugraph_fake_embedding.hedge2fake_clockwise_fface
                ,hedge2fake_clockwise_prev_hedge_around_vertex
                    = ugraph_fake_embedding.hedge2fake_clockwise_prev_hedge_around_vertex
                )
    def is_ugraph_fake_embedding_nonedgeless_rigid_connected(self):
        return 1 == self.num_nonedgeless_connected_components
    def num_nonedgeless_connected_components(self):
        ugraph_fake_embedding = _get_ugraph_fake_embedding(self)
        return ugraph_fake_embedding2num_nonedgeless_connected_components(
            ugraph_fake_embedding
            )





