
# for UGraphFakeEmbedding

__all__ = '''
    make_hedge2another_hedge
    make_hedge2fake_clockwise_prev_hedge_around_fface

    make_hedge2fake_clockwise_fface_ex
    make_hedge2fake_clockwise_fface
    make_fface2degree

    make_hedge2fvertex_ex
    make_hedge2fvertex
    make_fvertex2degree

    make_XXX2degree
    make_hedge2XXX
    make_hedge2XXX_ex
    '''.split()

from .iter_cycle_from import iter_cycle_from

def make_hedge2another_hedge(*
    ,hedge2fake_clockwise_next_hedge_around_vertex
    ,hedge2fake_clockwise_next_hedge_around_fface
    ):
    hedge2another_hedge = tuple(
        hedge2fake_clockwise_next_hedge_around_vertex[hedge]
        for hedge in hedge2fake_clockwise_next_hedge_around_fface
        )
    return hedge2another_hedge


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









def make_hedge2XXX_ex(*, hedge2next_hedge_around_XXX):
    # -> (hedge2XXX, XXX2arbitrary_hedge)
    L = len(hedge2next_hedge_around_XXX)
    hedge2XXX = [None]*L
    XXX2arbitrary_hedge = []

    for hedge in range(L):
        if hedge2XXX[hedge] is not None: continue
        XXX = len(XXX2arbitrary_hedge)

        XXX2arbitrary_hedge.append(hedge)
        for hedge in iter_cycle_from(hedge2next_hedge_around_XXX, hedge):
            assert hedge2XXX[hedge] is None
            hedge2XXX[hedge] = XXX
    return (tuple(hedge2XXX)
           ,tuple(XXX2arbitrary_hedge)
           )
def make_hedge2XXX(*
    ,hedge2next_hedge_around_XXX
    ,XXX2arbitrary_hedge
    ):
    # -> hedge2XXX
    L = len(hedge2next_hedge_around_XXX)
    hedge2XXX = [None]*L
    for XXX, hedge in enumerate(XXX2arbitrary_hedge):
        for hedge in iter_cycle_from(hedge2next_hedge_around_XXX, hedge):
            #assert hedge2XXX[hedge] is None
            hedge2XXX[hedge] = XXX
    # assert all(XXX is not None for XXX in hedge2XXX)
    return tuple(hedge2XXX)

def make_XXX2degree(*
    ,hedge2next_hedge_around_XXX
    ,XXX2arbitrary_hedge
    ):
    XXX2degree = []
    for hedge in XXX2arbitrary_hedge:
        XXX_degree = 0
        for hedge in iter_cycle_from(hedge2next_hedge_around_XXX, hedge):
            XXX_degree += 1
        XXX2degree.append(XXX_degree)
    return tuple(XXX2degree)









def make_hedge2fake_clockwise_fface_ex(*
    ,hedge2fake_clockwise_next_hedge_around_fface
    ):
    # -> (hedge2fake_clockwise_fface, fface2arbitrary_hedge)
    (hedge2fake_clockwise_fface, fface2arbitrary_hedge
    ) = make_hedge2XXX_ex(
        hedge2next_hedge_around_XXX=hedge2fake_clockwise_next_hedge_around_fface)
    return (hedge2fake_clockwise_fface, fface2arbitrary_hedge)


def make_hedge2fake_clockwise_fface(*
    ,hedge2fake_clockwise_next_hedge_around_fface
    ,fface2arbitrary_hedge
    ):
    # -> hedge2fake_clockwise_fface
    hedge2fake_clockwise_fface = make_hedge2XXX(
        hedge2next_hedge_around_XXX=hedge2fake_clockwise_next_hedge_around_fface
        ,XXX2arbitrary_hedge=fface2arbitrary_hedge
        )
    return hedge2fake_clockwise_fface


def make_fface2degree(*
    ,hedge2fake_clockwise_next_hedge_around_fface
    ,fface2arbitrary_hedge
    ):
    # -> fface2degree
    fface2degree = make_XXX2degree(
        hedge2next_hedge_around_XXX=hedge2fake_clockwise_next_hedge_around_fface
        ,XXX2arbitrary_hedge=fface2arbitrary_hedge
        )
    return fface2degree









def make_hedge2fvertex_ex(*
    ,hedge2fake_clockwise_next_hedge_around_vertex
    ):
    # -> (hedge2fvertex, fvertex2arbitrary_hedge)
    (hedge2fvertex, fvertex2arbitrary_hedge
    ) = make_hedge2XXX_ex(
        hedge2next_hedge_around_XXX=hedge2fake_clockwise_next_hedge_around_vertex)
    return (hedge2fvertex, fvertex2arbitrary_hedge)


def make_hedge2fvertex(*
    ,hedge2fake_clockwise_next_hedge_around_vertex
    ,fvertex2arbitrary_hedge
    ):
    # -> hedge2fvertex
    hedge2fvertex = make_hedge2XXX(
        hedge2next_hedge_around_XXX=hedge2fake_clockwise_next_hedge_around_vertex
        ,XXX2arbitrary_hedge=fvertex2arbitrary_hedge
        )
    return hedge2fvertex


def make_fvertex2degree(*
    ,hedge2fake_clockwise_next_hedge_around_vertex
    ,fvertex2arbitrary_hedge
    ):
    # -> fvertex2degree
    fvertex2degree = make_XXX2degree(
        hedge2next_hedge_around_XXX=hedge2fake_clockwise_next_hedge_around_vertex
        ,XXX2arbitrary_hedge=fvertex2arbitrary_hedge
        )
    return fvertex2degree

