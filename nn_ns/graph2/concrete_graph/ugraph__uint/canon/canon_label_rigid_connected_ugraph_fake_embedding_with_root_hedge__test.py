
'''
>>> this(single_loop_graph, 0)
UGraphFakeEmbeddingLabelling(old_fvertex2new_fvertex = UIntBijection(forward_mapping = [0], backward_mapping = [0]), old_hedge2new_hedge = UIntBijection(forward_mapping = [0, 1], backward_mapping = [0, 1]), old_fface2new_fface = UIntBijection(forward_mapping = [0, 1], backward_mapping = [0, 1]))
>>> this(single_loop_graph, 1)
UGraphFakeEmbeddingLabelling(old_fvertex2new_fvertex = UIntBijection(forward_mapping = [0], backward_mapping = [0]), old_hedge2new_hedge = UIntBijection(forward_mapping = [1, 0], backward_mapping = [1, 0]), old_fface2new_fface = UIntBijection(forward_mapping = [1, 0], backward_mapping = [1, 0]))

>>> this(single_nonloop_graph, 0)
UGraphFakeEmbeddingLabelling(old_fvertex2new_fvertex = UIntBijection(forward_mapping = [0, 1], backward_mapping = [0, 1]), old_hedge2new_hedge = UIntBijection(forward_mapping = [0, 1], backward_mapping = [0, 1]), old_fface2new_fface = UIntBijection(forward_mapping = [0], backward_mapping = [0]))
>>> this(single_nonloop_graph, 1)
UGraphFakeEmbeddingLabelling(old_fvertex2new_fvertex = UIntBijection(forward_mapping = [1, 0], backward_mapping = [1, 0]), old_hedge2new_hedge = UIntBijection(forward_mapping = [1, 0], backward_mapping = [1, 0]), old_fface2new_fface = UIntBijection(forward_mapping = [0], backward_mapping = [0]))


>>> this(two_parallel_nonloops_graph, 0)
UGraphFakeEmbeddingLabelling(old_fvertex2new_fvertex = UIntBijection(forward_mapping = [0, 1], backward_mapping = [0, 1]), old_hedge2new_hedge = UIntBijection(forward_mapping = [0, 1, 3, 2], backward_mapping = [0, 1, 3, 2]), old_fface2new_fface = UIntBijection(forward_mapping = [0, 1], backward_mapping = [0, 1]))
>>> this(two_parallel_nonloops_graph, 1)
UGraphFakeEmbeddingLabelling(old_fvertex2new_fvertex = UIntBijection(forward_mapping = [1, 0], backward_mapping = [1, 0]), old_hedge2new_hedge = UIntBijection(forward_mapping = [1, 0, 2, 3], backward_mapping = [1, 0, 2, 3]), old_fface2new_fface = UIntBijection(forward_mapping = [1, 0], backward_mapping = [1, 0]))
>>> this(two_parallel_nonloops_graph, 2)
UGraphFakeEmbeddingLabelling(old_fvertex2new_fvertex = UIntBijection(forward_mapping = [0, 1], backward_mapping = [0, 1]), old_hedge2new_hedge = UIntBijection(forward_mapping = [3, 2, 0, 1], backward_mapping = [2, 3, 1, 0]), old_fface2new_fface = UIntBijection(forward_mapping = [1, 0], backward_mapping = [1, 0]))
>>> this(two_parallel_nonloops_graph, 3)
UGraphFakeEmbeddingLabelling(old_fvertex2new_fvertex = UIntBijection(forward_mapping = [1, 0], backward_mapping = [1, 0]), old_hedge2new_hedge = UIntBijection(forward_mapping = [2, 3, 1, 0], backward_mapping = [3, 2, 0, 1]), old_fface2new_fface = UIntBijection(forward_mapping = [0, 1], backward_mapping = [0, 1]))


>>> this(two_parallel_loops_graph, 0)
UGraphFakeEmbeddingLabelling(old_fvertex2new_fvertex = UIntBijection(forward_mapping = [0], backward_mapping = [0]), old_hedge2new_hedge = UIntBijection(forward_mapping = [0, 1, 3, 2], backward_mapping = [0, 1, 3, 2]), old_fface2new_fface = UIntBijection(forward_mapping = [0, 1, 2], backward_mapping = [0, 1, 2]))
>>> this(two_nonparallel_loops_graph, 0)
UGraphFakeEmbeddingLabelling(old_fvertex2new_fvertex = UIntBijection(forward_mapping = [0], backward_mapping = [0]), old_hedge2new_hedge = UIntBijection(forward_mapping = [0, 1, 3, 2], backward_mapping = [0, 1, 3, 2]), old_fface2new_fface = UIntBijection(forward_mapping = [0], backward_mapping = [0]))
>>> this(two_nonparallel_loops_graph, 3)
UGraphFakeEmbeddingLabelling(old_fvertex2new_fvertex = UIntBijection(forward_mapping = [0], backward_mapping = [0]), old_hedge2new_hedge = UIntBijection(forward_mapping = [3, 2, 1, 0], backward_mapping = [3, 2, 1, 0]), old_fface2new_fface = UIntBijection(forward_mapping = [0], backward_mapping = [0]))

>>> this(three_parallel_nonloops_graph, 0)
UGraphFakeEmbeddingLabelling(old_fvertex2new_fvertex = UIntBijection(forward_mapping = [0, 1], backward_mapping = [0, 1]), old_hedge2new_hedge = UIntBijection(forward_mapping = [0, 1, 3, 2, 5, 4], backward_mapping = [0, 1, 3, 2, 5, 4]), old_fface2new_fface = UIntBijection(forward_mapping = [0, 1, 2], backward_mapping = [0, 1, 2]))
>>> this(three_parallel_nonloops_graph, 5)
UGraphFakeEmbeddingLabelling(old_fvertex2new_fvertex = UIntBijection(forward_mapping = [1, 0], backward_mapping = [1, 0]), old_hedge2new_hedge = UIntBijection(forward_mapping = [4, 5, 2, 3, 1, 0], backward_mapping = [5, 4, 2, 3, 0, 1]), old_fface2new_fface = UIntBijection(forward_mapping = [2, 1, 0], backward_mapping = [2, 1, 0]))

>>> this(three_nonparallel_nonloops_graph, 0)
UGraphFakeEmbeddingLabelling(old_fvertex2new_fvertex = UIntBijection(forward_mapping = [0, 1], backward_mapping = [0, 1]), old_hedge2new_hedge = UIntBijection(forward_mapping = [0, 1, 5, 4, 3, 2], backward_mapping = [0, 1, 5, 4, 3, 2]), old_fface2new_fface = UIntBijection(forward_mapping = [0], backward_mapping = [0]))
>>> this(three_nonparallel_nonloops_graph, 3)
UGraphFakeEmbeddingLabelling(old_fvertex2new_fvertex = UIntBijection(forward_mapping = [1, 0], backward_mapping = [1, 0]), old_hedge2new_hedge = UIntBijection(forward_mapping = [2, 3, 1, 0, 4, 5], backward_mapping = [3, 2, 0, 1, 4, 5]), old_fface2new_fface = UIntBijection(forward_mapping = [0], backward_mapping = [0]))


>>> this(edgeless_graph, 0)
Traceback (most recent call last):
    ...
ValueError
>>> this(one_loop_one_nonloop_disconnected_graph, 0)
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
from .canon_label_rigid_connected_ugraph_fake_embedding_with_root_hedge import \
    canon_label_rigid_connected_ugraph_fake_embedding_with_root_hedge


_this = canon_label_rigid_connected_ugraph_fake_embedding_with_root_hedge.by_dfs_preorder__O_E
this = lambda embedding, root_hedge: _this(rigid_connected_ugraph_fake_embedding=embedding, root_hedge=root_hedge)

def _t():
    r = this(single_loop_graph, 0)
    print(r)
    r = this(single_loop_graph, 1)
    print(r)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


