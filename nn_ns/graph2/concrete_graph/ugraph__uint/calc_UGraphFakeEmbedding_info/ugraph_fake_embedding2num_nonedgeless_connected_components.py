
__all__ = '''
    ugraph_fake_embedding2num_nonedgeless_connected_components
    '''.split()

from .dfs__ugraph_fake_embedding import (
    dfs__ugraph_fake_embedding
    ,DFS_Case
    )

def ugraph_fake_embedding2num_nonedgeless_connected_components(ugraph_fake_embedding):
    it = dfs__ugraph_fake_embedding(
        ugraph_fake_embedding=ugraph_fake_embedding
        ,is_clockwise_around_fvertex=False
        ).more_dfs()

    num_connected_components = 0
    for case, payload in it:
        '''
        (DFS_EnterRootVertex, Vertex)
        (DFS_ExitRootVertex, Vertex)
        (DFS_EnterTreeHEdge, (HEdge, Vertex))
        (DFS_ExitTreeHEdge, None)
        (DFS_EnterExitBackOrRBackHEdge, (HEdge, Vertex))
        '''
        if case == DFS_Case.DFS_EnterRootVertex:
            num_connected_components += 1
    return num_connected_components

