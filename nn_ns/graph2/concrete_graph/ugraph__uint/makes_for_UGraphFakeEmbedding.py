
# for UGraphFakeEmbedding

__all__ = '''
    make_hedge2fake_clockwise_prev_hedge_around_fface
    make_hedge2fake_clockwise_fface_ex
    make_hedge2fake_clockwise_fface
    make_fface2degree
    make_hedge2another_hedge
    '''.split()

from .iter_cycle_from import iter_cycle_from

def make_hedge2fake_clockwise_prev_hedge_around_fface(*
    ,hedge2fake_clockwise_next_hedge_around_vertex
    ,hedge2another_hedge
    ):
    # hedge2fake_clockwise_prev_hedge_around_fface[hedge] = hedge2another_hedge[hedge2fake_clockwise_next_hedge_around_vertex[hedge]]
    L = len(hedge2another_hedge)
    hedge2fake_clockwise_prev_hedge_around_fface = tuple(
        hedge2another_hedge[hedge2fake_clockwise_next_hedge_around_vertex[hedge]]
        for hedge in range(L)
        )
    return hedge2fake_clockwise_prev_hedge_around_fface


def make_hedge2fake_clockwise_fface_ex(*
    ,hedge2fake_clockwise_next_hedge_around_fface
    ):
    # -> (hedge2fake_clockwise_fface, fface2arbitrary_hedge)
    L = len(hedge2fake_clockwise_next_hedge_around_fface)
    hedge2fake_clockwise_fface = [None]*L
    fface2arbitrary_hedge = []

    for hedge in range(L):
        if hedge2fake_clockwise_fface[hedge] is not None: continue
        fface = len(fface2arbitrary_hedge)

        fface2arbitrary_hedge.append(hedge)
        for hedge in iter_cycle_from(hedge2fake_clockwise_next_hedge_around_fface, hedge):
            assert hedge2fake_clockwise_fface[hedge] is None
            hedge2fake_clockwise_fface[hedge] = fface
    return (tuple(hedge2fake_clockwise_fface)
           ,tuple(fface2arbitrary_hedge)
           )

def make_hedge2fake_clockwise_fface(*
    ,hedge2fake_clockwise_next_hedge_around_fface
    ,fface2arbitrary_hedge
    ):
    L = len(hedge2fake_clockwise_next_hedge_around_fface)
    hedge2fake_clockwise_fface = [None]*L
    for fface, hedge in enumerate(fface2arbitrary_hedge):
        for hedge in iter_cycle_from(hedge2fake_clockwise_next_hedge_around_fface, hedge):
            #assert hedge2fake_clockwise_fface[hedge] is None
            hedge2fake_clockwise_fface[hedge] = fface
    # assert all(fface is not None for fface in hedge2fake_clockwise_fface)
    return tuple(hedge2fake_clockwise_fface)
def make_fface2degree(*
    ,hedge2fake_clockwise_next_hedge_around_fface
    ,fface2arbitrary_hedge
    ):
    fface2degree = []
    for hedge in fface2arbitrary_hedge:
        fface_degree = 0
        for hedge in iter_cycle_from(hedge2fake_clockwise_next_hedge_around_fface, hedge):
            fface_degree += 1
        fface2degree.append(fface_degree)
    return tuple(fface2degree)

def make_hedge2another_hedge(*
    ,hedge2fake_clockwise_next_hedge_around_vertex
    ,hedge2fake_clockwise_next_hedge_around_fface
    ):
    hedge2another_hedge = tuple(
        hedge2fake_clockwise_next_hedge_around_vertex[hedge]
        for hedge in hedge2fake_clockwise_next_hedge_around_fface
        )
    return hedge2another_hedge


