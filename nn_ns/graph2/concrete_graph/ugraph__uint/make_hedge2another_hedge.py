

__all__ = '''
    make_hedge2another_hedge
    '''.split()
    # from_hedge2aedge
    # from_hedge2fake_clockwise_next_hedge_around_vertex_and_fface

from .makes_for_UGraphFakeEmbedding import (
    make_hedge2another_hedge
        as _from_hedge2fake_clockwise_next_hedge_around_vertex_and_fface
    )

class make_hedge2another_hedge:
    '''
methods:
    from_hedge2aedge
    from_hedge2fake_clockwise_next_hedge_around_vertex_and_fface
'''
    @classmethod
    def from_hedge2fake_clockwise_next_hedge_around_vertex_and_fface(cls, *
        ,hedge2fake_clockwise_next_hedge_around_vertex
        ,hedge2fake_clockwise_next_hedge_around_fface
        ):
        return _from_hedge2fake_clockwise_next_hedge_around_vertex_and_fface(
            hedge2fake_clockwise_next_hedge_around_vertex
                = hedge2fake_clockwise_next_hedge_around_vertex
            ,hedge2fake_clockwise_next_hedge_around_fface
                = hedge2fake_clockwise_next_hedge_around_fface
            )

    @classmethod
    def from_hedge2aedge(cls, *, hedge2aedge):
        num_hedges = len(hedge2aedge)
        num_aedges = num_hedges // 2
        if num_hedges != num_aedges*2: raise ValueError
        if not all(0 <= u < num_aedges for u in hedge2aedge): raise ValueError

        aedge2hedges = [[] for _ in range(num_aedges)]
        for hedge, aedge in enumerate(hedge2aedge):
            aedge2hedges[aedge].append(hedge)
        if not all(len(hedges) == 2 for hedges in aedge2hedges): raise ValueError

        hedge2another_hedge = [None]*num_hedges
        for hedges in aedge2hedges:
            hedge, other = hedges
            hedge2another_hedge[hedge] = other
            hedge2another_hedge[other] = hedge
        assert all(h is not None for h in hedge2another_hedge)

        return tuple(hedge2another_hedge)

