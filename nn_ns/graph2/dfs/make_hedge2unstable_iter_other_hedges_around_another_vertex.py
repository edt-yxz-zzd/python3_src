
'''
for dfs__finite_explicit_ugraph

make_hedge2unstable_iter_other_hedges_around_another_vertex
    from_vertex2unstable_iter_hedges
    from_hedge2next_hedge_in_cycle_around_vertex
'''
class make_hedge2unstable_iter_other_hedges_around_another_vertex:
    @classmethod
    def from_vertex2unstable_iter_hedges(cls, *
        ,hedge_eq
        ,hedge2another_vertex
        ,hedge2another_hedge
        ,vertex2unstable_iter_hedges
        ):
        def hedge2unstable_iter_other_hedges_around_another_vertex(hedge):
            hedge0 = hedge2another_hedge(hedge)
            vertex = hedge2another_vertex(hedge)
            for hedge in vertex2unstable_iter_hedges(vertex):
                if not hedge_eq(hedge, hedge0):
                    yield hedge
        return hedge2unstable_iter_other_hedges_around_another_vertex

    @classmethod
    def from_hedge2next_hedge_in_cycle_around_vertex(cls, *
        ,hedge_eq
        ,hedge2another_hedge
        ,hedge2next_hedge_in_cycle_around_vertex
        ):
        def hedge2unstable_iter_other_hedges_around_another_vertex(hedge):
            hedge = hedge0 = hedge2another_hedge(hedge)
            while True:
                hedge = hedge2next_hedge_in_cycle_around_vertex(hedge)
                if hedge_eq(hedge, hedge0): break
                yield hedge
        return hedge2unstable_iter_other_hedges_around_another_vertex


