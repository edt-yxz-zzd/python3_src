
from ..UGraphFakeEmbedding import UGraphFakeEmbedding
from .is_relax_biconnected_ugraph_fake_embedding_relax_planar_ex \
    import is_relax_biconnected_ugraph_fake_embedding_relax_planar_ex

relax_biconnected_ugraph_fake_embedding=UGraphFakeEmbedding(
    num_hedges = 24
    , num_ffaces = 4
    , num_fvertices = 8
    , hedge2fake_clockwise_next_hedge_around_vertex = [1, 2, 0, 4, 5, 3, 7, 8, 6, 10, 11, 9, 13, 14, 12, 16, 17, 15, 19, 20, 18, 22, 23, 21]
    , hedge2fake_clockwise_prev_hedge_around_vertex = (2, 0, 1, 5, 3, 4, 8, 6, 7, 11, 9, 10, 14, 12, 13, 17, 15, 16, 20, 18, 19, 23, 21, 22)
    , hedge2fake_clockwise_next_hedge_around_fface = (22, 9, 5, 1, 6, 14, 16, 3, 11, 7, 0, 20, 4, 21, 17, 13, 18, 8, 10, 15, 23, 19, 12, 2)
    , hedge2fake_clockwise_prev_hedge_around_fface = (10, 3, 23, 7, 12, 2, 4, 9, 17, 1, 18, 8, 22, 15, 5, 19, 6, 14, 16, 21, 11, 13, 0, 20)
    , fface2degree = (8, 4, 4, 8)
    , hedge2fake_clockwise_fface = (0, 1, 3, 1, 0, 3, 0, 1, 3, 1, 0, 3, 0, 2, 3, 2, 0, 3, 0, 2, 3, 2, 0, 3)
    , fface2arbitrary_hedge = [4, 7, 19, 2]
    , fvertex2degree = (3, 3, 3, 3, 3, 3, 3, 3)
    , hedge2fvertex = (0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7)
    , fvertex2arbitrary_hedge = [1, 4, 7, 10, 13, 16, 19, 22]
    )
hedge2fake_counterclockwise_fface=(3, 0, 1, 3, 1, 0, 3, 0, 1, 3, 1, 0, 3, 0, 2, 3, 2, 0, 3, 0, 2, 3, 2, 0)



r = is_relax_biconnected_ugraph_fake_embedding_relax_planar_ex(
    relax_biconnected_ugraph_fake_embedding
        = relax_biconnected_ugraph_fake_embedding
    ,hedge2fake_counterclockwise_fface
        = hedge2fake_counterclockwise_fface
    )

cycle_hedges1=(3, 0, 21, 18, 9, 6, 16, 18, 10, 0, 22, 12)
path_hedges1=(4, 8)
assert r == (2, (cycle_hedges1, path_hedges1))
'''
arc1 (4,)
arc2 ()
arc3 (6, 16, 18)
arc4 (10, 0, 22, 12)
arc5 (3, 0, 21, 18, 9)
arc6 (8,)
'''

e = relax_biconnected_ugraph_fake_embedding
# verify path_hedges1 from inside to outside of cycle_hedges1

assert e.hedge2fake_clockwise_next_hedge_around_vertex[4] == 5
assert e.hedge2fake_clockwise_next_hedge_around_vertex[5] == 3
assert e.hedge2fake_clockwise_next_hedge_around_vertex[3] == 4
assert e.hedge2another_hedge(5) == 12

assert e.hedge2fake_clockwise_next_hedge_around_vertex[8] == 6
assert e.hedge2fake_clockwise_next_hedge_around_vertex[6] == 7
assert e.hedge2fake_clockwise_next_hedge_around_vertex[7] == 8
assert e.hedge2another_hedge(8) == 9

print(r)
