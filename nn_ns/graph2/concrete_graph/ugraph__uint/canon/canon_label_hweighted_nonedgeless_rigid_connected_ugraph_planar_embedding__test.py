
'''
>>> this(single_loop_graph)
(UGraphFakeEmbeddingLabelling(old_fvertex2new_fvertex = UIntBijection(forward_mapping = [0], backward_mapping = [0]), old_hedge2new_hedge = UIntBijection(forward_mapping = [0, 1], backward_mapping = [0, 1]), old_fface2new_fface = UIntBijection(forward_mapping = [0, 1], backward_mapping = [0, 1])), [(0, 1)])
>>> this(single_loop_graph, [1,0])
(UGraphFakeEmbeddingLabelling(old_fvertex2new_fvertex = UIntBijection(forward_mapping = [0], backward_mapping = [0]), old_hedge2new_hedge = UIntBijection(forward_mapping = [1, 0], backward_mapping = [1, 0]), old_fface2new_fface = UIntBijection(forward_mapping = [1, 0], backward_mapping = [1, 0])), [(1,), (0,)])

>>> this(single_nonloop_graph)
(UGraphFakeEmbeddingLabelling(old_fvertex2new_fvertex = UIntBijection(forward_mapping = [0, 1], backward_mapping = [0, 1]), old_hedge2new_hedge = UIntBijection(forward_mapping = [0, 1], backward_mapping = [0, 1]), old_fface2new_fface = UIntBijection(forward_mapping = [0], backward_mapping = [0])), [(0, 1)])
>>> this(single_nonloop_graph, [1,0])
(UGraphFakeEmbeddingLabelling(old_fvertex2new_fvertex = UIntBijection(forward_mapping = [1, 0], backward_mapping = [1, 0]), old_hedge2new_hedge = UIntBijection(forward_mapping = [1, 0], backward_mapping = [1, 0]), old_fface2new_fface = UIntBijection(forward_mapping = [0], backward_mapping = [0])), [(1,), (0,)])


>>> this(two_parallel_nonloops_graph)
(UGraphFakeEmbeddingLabelling(old_fvertex2new_fvertex = UIntBijection(forward_mapping = [0, 1], backward_mapping = [0, 1]), old_hedge2new_hedge = UIntBijection(forward_mapping = [0, 1, 3, 2], backward_mapping = [0, 1, 3, 2]), old_fface2new_fface = UIntBijection(forward_mapping = [0, 1], backward_mapping = [0, 1])), [(0, 1, 2, 3)])
>>> this(two_parallel_nonloops_graph, [0,1,0,0])
(UGraphFakeEmbeddingLabelling(old_fvertex2new_fvertex = UIntBijection(forward_mapping = [0, 1], backward_mapping = [0, 1]), old_hedge2new_hedge = UIntBijection(forward_mapping = [3, 2, 0, 1], backward_mapping = [2, 3, 1, 0]), old_fface2new_fface = UIntBijection(forward_mapping = [1, 0], backward_mapping = [1, 0])), [(2,), (3,), (0,), (1,)])
>>> this(two_parallel_nonloops_graph, [0,1,1,0])
(UGraphFakeEmbeddingLabelling(old_fvertex2new_fvertex = UIntBijection(forward_mapping = [0, 1], backward_mapping = [0, 1]), old_hedge2new_hedge = UIntBijection(forward_mapping = [0, 1, 3, 2], backward_mapping = [0, 1, 3, 2]), old_fface2new_fface = UIntBijection(forward_mapping = [0, 1], backward_mapping = [0, 1])), [(0, 3), (1, 2)])
>>> this(two_parallel_nonloops_graph, [0,1,0,1])
(UGraphFakeEmbeddingLabelling(old_fvertex2new_fvertex = UIntBijection(forward_mapping = [0, 1], backward_mapping = [0, 1]), old_hedge2new_hedge = UIntBijection(forward_mapping = [0, 1, 3, 2], backward_mapping = [0, 1, 3, 2]), old_fface2new_fface = UIntBijection(forward_mapping = [0, 1], backward_mapping = [0, 1])), [(0, 2), (1, 3)])
>>> this(two_parallel_nonloops_graph, [1,1,0,0])
(UGraphFakeEmbeddingLabelling(old_fvertex2new_fvertex = UIntBijection(forward_mapping = [0, 1], backward_mapping = [0, 1]), old_hedge2new_hedge = UIntBijection(forward_mapping = [3, 2, 0, 1], backward_mapping = [2, 3, 1, 0]), old_fface2new_fface = UIntBijection(forward_mapping = [1, 0], backward_mapping = [1, 0])), [(2, 3), (0, 1)])


>>> this(two_parallel_loops_graph)
(UGraphFakeEmbeddingLabelling(old_fvertex2new_fvertex = UIntBijection(forward_mapping = [0], backward_mapping = [0]), old_hedge2new_hedge = UIntBijection(forward_mapping = [2, 3, 0, 1], backward_mapping = [2, 3, 0, 1]), old_fface2new_fface = UIntBijection(forward_mapping = [1, 2, 0], backward_mapping = [2, 0, 1])), [(2, 1), (3, 0)])


>>> this(three_parallel_nonloops_graph)
(UGraphFakeEmbeddingLabelling(old_fvertex2new_fvertex = UIntBijection(forward_mapping = [0, 1], backward_mapping = [0, 1]), old_hedge2new_hedge = UIntBijection(forward_mapping = [3, 2, 5, 4, 0, 1], backward_mapping = [4, 5, 1, 0, 3, 2]), old_fface2new_fface = UIntBijection(forward_mapping = [2, 0, 1], backward_mapping = [1, 2, 0])), [(4, 3, 0, 5, 2, 1)])
>>> this(three_parallel_nonloops_graph, [1,1,1,0,0,0])
(UGraphFakeEmbeddingLabelling(old_fvertex2new_fvertex = UIntBijection(forward_mapping = [0, 1], backward_mapping = [0, 1]), old_hedge2new_hedge = UIntBijection(forward_mapping = [3, 2, 5, 4, 0, 1], backward_mapping = [4, 5, 1, 0, 3, 2]), old_fface2new_fface = UIntBijection(forward_mapping = [2, 0, 1], backward_mapping = [1, 2, 0])), [(4,), (5,), (3,), (2,), (0,), (1,)])
>>> this(three_parallel_nonloops_graph, [1,0,0,1,0,0])
(UGraphFakeEmbeddingLabelling(old_fvertex2new_fvertex = UIntBijection(forward_mapping = [0, 1], backward_mapping = [0, 1]), old_hedge2new_hedge = UIntBijection(forward_mapping = [3, 2, 5, 4, 0, 1], backward_mapping = [4, 5, 1, 0, 3, 2]), old_fface2new_fface = UIntBijection(forward_mapping = [2, 0, 1], backward_mapping = [1, 2, 0])), [(4, 5), (2, 1), (0, 3)])


>>> this(two_nonparallel_loops_graph)
Traceback (most recent call last):
    ...
ValueError
>>> this(three_nonparallel_nonloops_graph)
Traceback (most recent call last):
    ...
ValueError
>>> this(edgeless_graph)
Traceback (most recent call last):
    ...
ValueError
>>> this(one_loop_one_nonloop_disconnected_graph)
Traceback (most recent call last):
    ...
ValueError

'''

from ..example__UGraphFakeEmbedding import (
    edgeless_graph
    ,single_loop_graph
    ,single_nonloop_graph
    ,two_parallel_nonloops_graph
    ,two_parallel_loops_graph
    ,two_nonparallel_loops_graph
    ,three_parallel_nonloops_graph
    ,three_nonparallel_nonloops_graph
    ,one_loop_one_nonloop_disconnected_graph
    )

from ..UGraphFakeEmbedding import UGraphFakeEmbedding
from ..UGraphFakeEmbeddingLabelling import UGraphFakeEmbeddingLabelling
from .canon_label_hweighted_nonedgeless_rigid_connected_ugraph_planar_embedding import \
    canon_label_hweighted_nonedgeless_rigid_connected_ugraph_planar_embedding


_this = canon_label_hweighted_nonedgeless_rigid_connected_ugraph_planar_embedding.by_partition_distinguishable_hedges_ex__O_E_logE
def this(embedding, hedge2hweight=None):
    if hedge2hweight is None:
        hedge2hweight = [0]*embedding.num_hedges
    num_hweights = 1+max(hedge2hweight, default=-1)
    labelling, hedge_classes = _this(nonedgeless_rigid_connected_ugraph_planar_embedding=embedding, hedge2hweight=hedge2hweight, num_hweights=num_hweights)
    hedge_classes = list(hedge_classes)
    return labelling, hedge_classes



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


