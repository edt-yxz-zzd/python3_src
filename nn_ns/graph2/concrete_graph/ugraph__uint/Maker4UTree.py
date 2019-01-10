
__all__ = '''
    Maker4UTree
    '''.split()


from .IMaker4UTree import IMaker4UTree
from .abc import override
from .UGraph import UGraph

class Maker4UTree(IMaker4UTree):
    '''

usage:
    # see: IMaker4UTree
    ns = Maker4UTree(utree).make_all_rooted_utree_attrs(maybe_either_root=None)
    ns.either_root
'''
    utree_type = UGraph
    def __init__(self, utree):
        assert isinstance(utree, UGraph)
        assert utree.calc.is_ugraph_utree
        super().__init__(utree)
    @override
    def vertex2unstable_iter_hedges(self, vertex):
        return self.utree.vertex2unstable_iter_hedges(vertex)
    @override
    def hedge2unstable_iter_other_hedges_around_another_vertex(self, hedge):
        return self.utree.hedge2unstable_iter_other_hedges_around_another_vertex(hedge)



