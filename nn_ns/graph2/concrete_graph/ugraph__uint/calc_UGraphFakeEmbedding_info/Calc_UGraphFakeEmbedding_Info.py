
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

_get = object.__getattribute__
class Calc_UGraphFakeEmbedding_Info:
    all_attr_seq = '''
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




