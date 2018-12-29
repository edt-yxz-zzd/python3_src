
__all__ = '''
    canon_label_rigid_connected_ugraph_fake_embedding_with_root_hedge
    canon_label_ugraph_fake_embedding_with_ordered_source_hedges
    '''.split()

from .dfs__ugraph_fake_embedding import (
    dfs__ugraph_fake_embedding
    ,DFS_Case
    ,DFS_SourceType
    )
from .imports import Vertex2TwoColor__seq
from ..UIntBijectionBuilder import UIntBijectionBuilder
from ..UGraphFakeEmbedding import UGraphFakeEmbedding
from ..UGraphFakeEmbeddingLabelling import UGraphFakeEmbeddingLabelling

class canon_label_rigid_connected_ugraph_fake_embedding_with_root_hedge:
    '''
methods:
    by_dfs_preorder__O_E
'''
    @classmethod
    def by_dfs_preorder__O_E(cls, *, rigid_connected_ugraph_fake_embedding, root_hedge):
        '''UGraphFakeEmbedding -> root_hedge -> UGraphFakeEmbeddingLabelling
by dfs preorder; O(E)
'''
        assert isinstance(rigid_connected_ugraph_fake_embedding, UGraphFakeEmbedding)
        assert isinstance(root_hedge, int)
        if not 0 <= root_hedge < rigid_connected_ugraph_fake_embedding.num_hedges: raise ValueError
        if not rigid_connected_ugraph_fake_embedding.calc.is_ugraph_fake_embedding_nonedgeless_rigid_connected: raise ValueError

        return canon_label_ugraph_fake_embedding_with_ordered_source_hedges.by_dfs_preorder__O_E(
            ugraph_fake_embedding
                = rigid_connected_ugraph_fake_embedding
            ,ordered_source_hedges = [root_hedge]
            )

class canon_label_ugraph_fake_embedding_with_ordered_source_hedges:
    '''
methods:
    by_dfs_preorder__O_E
'''
    @classmethod
    def by_dfs_preorder__O_E(cls, *, ugraph_fake_embedding, ordered_source_hedges):
        '''UGraphFakeEmbedding -> Iter source_hedge -> UGraphFakeEmbeddingLabelling
by dfs preorder; O(E)

len(ordered_source_hedges) >= num_nonedgeless_connected_components
    # result dfs tree should cover all fvertices
'''
        assert isinstance(ugraph_fake_embedding, UGraphFakeEmbedding)


        it = dfs__ugraph_fake_embedding(
            ugraph_fake_embedding=ugraph_fake_embedding
            ,is_clockwise_around_fvertex = False
            ,maybe_ancestor_hedge_stack = None
            ,maybe_ancestor_vertex_stack = None
            ).more_dfs_via(sources=ordered_source_hedges
                        , source_type=DFS_SourceType.HEDGE
                        )

        old_fvertex2new_fvertex__builder = UIntBijectionBuilder(ugraph_fake_embedding.num_fvertices)
        #old_aedge2new_aedge__builder = UIntBijectionBuilder(ugraph_fake_embedding.num_aedges)
        old_fface2new_fface__builder = UIntBijectionBuilder(ugraph_fake_embedding.num_ffaces)
        old_hedge2new_hedge__builder = UIntBijectionBuilder(ugraph_fake_embedding.num_hedges)

        def is_hedge_visited(hedge):
            return old_hedge2new_hedge__builder.is_old_uint_visited(hedge)
        def may_visit_fface_via_hedge(hedge):
            fface = ugraph_fake_embedding.hedge2fake_clockwise_fface[hedge]
            old_fface2new_fface__builder.may_visit_next_old_uint(fface)
        def visit_hedge(hedge):
            other = ugraph_fake_embedding.hedge2another_hedge(hedge)
            old_hedge2new_hedge__builder.visit_next_old_uint(hedge)
            old_hedge2new_hedge__builder.visit_next_old_uint(other)
            may_visit_fface_via_hedge(hedge)
            may_visit_fface_via_hedge(other)
        def visit_fvertex(fvertex):
            old_fvertex2new_fvertex__builder.visit_next_old_uint(fvertex)

        #num_visited_fvertices = 0
        for case, payload in it:
            '''
            (DFS_EnterRootVertex, Vertex)
            (DFS_ExitRootVertex, Vertex)
            (DFS_EnterTreeHEdge, (HEdge, Vertex))
            (DFS_ExitTreeHEdge, None)
            (DFS_EnterExitBackOrRBackHEdge, (HEdge, Vertex))
            '''
            if case == DFS_Case.DFS_EnterTreeHEdge:
                hedge, fvertex = payload
                visit_hedge(hedge)
                visit_fvertex(fvertex)
            elif case == DFS_Case.DFS_EnterExitBackOrRBackHEdge:
                hedge, fvertex = payload
                if not is_hedge_visited(hedge):
                    visit_hedge(hedge)
            elif case == DFS_Case.DFS_EnterRootVertex:
                fvertex = payload
                visit_fvertex(fvertex)
        # end for

        old_fvertex2new_fvertex = old_fvertex2new_fvertex__builder.to_uint_bijection__old2new()
        old_hedge2new_hedge = old_hedge2new_hedge__builder.to_uint_bijection__old2new()
        old_fface2new_fface = old_fface2new_fface__builder.to_uint_bijection__old2new()

        return UGraphFakeEmbeddingLabelling(
                    old_fvertex2new_fvertex=old_fvertex2new_fvertex
                    ,old_hedge2new_hedge=old_hedge2new_hedge
                    ,old_fface2new_fface=old_fface2new_fface
                    )


