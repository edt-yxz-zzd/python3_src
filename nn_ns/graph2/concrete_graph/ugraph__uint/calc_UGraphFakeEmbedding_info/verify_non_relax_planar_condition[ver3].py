from seed.verify.common_verify import (
    is_UInt, is_Sequence, is_tuple
    #is_int, is_UInt, is_pair, is_tuple
    )

def new_path2old_path(hedges):
    '''[new_HXY] -> [old_hedge]
convert back to original hedges
    HPM/HNM -> old hedges
        HPM -> HPM//6
        HNM -> HNM//6
    remove other HXY
'''
    for hedge in hedges:
        q,r = divmod(hedge, 6)
        if r in (1,4):
            hedge = q
            yield hedge


def is_tuple_of_UInt(obj):
    return is_tuple(obj) and is_Sequence.of(obj, is_UInt)
def is_tuple_of_UInt_lt(obj, upper_bound):
    return is_tuple_of_UInt(obj) and max(obj, default=upper_bound-1) < upper_bound
def is_hedges1(num_hedges, obj):
    return is_tuple_of_UInt_lt(obj, num_hedges) and len(obj) >= 1
def _is_connected(ugraph_fake_embedding, hedge_before, hedge_after):
    fvertex0 = ugraph_fake_embedding.hedge2fvertex[ugraph_fake_embedding.hedge2another_hedge(hedge_before)]
    fvertex1 = ugraph_fake_embedding.hedge2fvertex[hedge_after]
    return fvertex1 == fvertex0
def is_path_hedges1(ugraph_fake_embedding, hedges):
    return (is_hedges1(ugraph_fake_embedding.num_hedges, hedges)
        and all(_is_connected(ugraph_fake_embedding, hedges[i-1], hedges[i]) for i in range(1, len(hedges)))
        )
def is_path_hedges1__without_crossing(ugraph_fake_embedding, hedges):
    if not is_path_hedges1(ugraph_fake_embedding, hedges):
        return False
    fvertices = set(ugraph_fake_embedding.hedge2fvertex[hedge] for hedge in hedges)
    if len(fvertices) != len(hedges):
        return False

    begin_fvertex = ugraph_fake_embedding.hedge2fvertex[hedges[0]]
    end_fvertex = ugraph_fake_embedding.hedge2fvertex[ugraph_fake_embedding.hedge2another_hedge(hedges[-1])]
    return end_fvertex == begin_fvertex or end_fvertex not in fvertices
def is_cycle_hedges1__without_crossing(ugraph_fake_embedding, hedges):
    if not is_path_hedges1__without_crossing(ugraph_fake_embedding, hedges):
        return False
    begin_fvertex = ugraph_fake_embedding.hedge2fvertex[hedges[0]]
    end_fvertex = ugraph_fake_embedding.hedge2fvertex[ugraph_fake_embedding.hedge2another_hedge(hedges[-1])]
    return begin_fvertex == end_fvertex

def hedges_are_in_clockwise_around_vertex(ugraph_fake_embedding, hedges):
    hedges = tuple(hedges)
    if len(hedges) <= 1: return True

    fvertices = tuple(ugraph_fake_embedding.hedge2fvertex[hedge] for hedge in hedges)
    if not all(fvertices[0] == fvertex for fvertex in fvertices):
        raise logic-error

    hedges__set = set(hedges)
    f = ugraph_fake_embedding.hedge2iter_fake_clockwise_hedges_around_vertex
    hedges__tuple = tuple(hedge for hedge in f(hedges[0]) if hedge in hedges__set)
    return hedges == hedges__tuple

def verify_non_relax_planar_condition(
    ugraph_fake_embedding, cycle_hedges1, path_hedges1
    ):
    '''verify result from is_ugraph_fake_embedding_relax_planar_ex
    verify non_relax_planar_condition
'''
    if not (is_cycle_hedges1__without_crossing(ugraph_fake_embedding, cycle_hedges1)
        and is_path_hedges1__without_crossing(ugraph_fake_embedding, path_hedges1)
        ):
        return False


    begin_fvertex = ugraph_fake_embedding.hedge2fvertex[path_hedges1[0]]
    end_fvertex = ugraph_fake_embedding.hedge2fvertex[ugraph_fake_embedding.hedge2another_hedge(path_hedges1[-1])]

    fvertices = tuple(ugraph_fake_embedding.hedge2fvertex[hedge] for hedge in cycle_hedges1)
    i = fvertices.index(begin_fvertex)
    j = fvertices.index(end_fvertex)

    hedge2another_hedge = ugraph_fake_embedding.hedge2another_hedge
    clockwise_hedgess = [(cycle_hedges1[i]
                        , path_hedges1[0]
                        , hedge2another_hedge(cycle_hedges1[i-1])
                        )#inner
                        ,(cycle_hedges1[j]
                        , hedge2another_hedge(cycle_hedges1[j-1])
                        , hedge2another_hedge(path_hedges1[-1])
                        )
                        ]
    return all(hedges_are_in_clockwise_around_vertex(ugraph_fake_embedding, clockwise_hedges)
                for clockwise_hedges in clockwise_hedgess)



