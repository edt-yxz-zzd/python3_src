
'''
error:
    next aedge is visited? skip
    next aedge is visiting? parent edge; skip
    next aedge is unvisited? forward
    if no next aedge, then backward

    when enter unvisited aedge:
        if it is hhedge:
            visit it beside EnterExit!
        if it is not hhedge:
            the target_vtx is visited? impossble
            the target_vtx is visiting?
                this aedge is a back edge
            the target_vtx is unvisited?
                if target_vtx has no outgoing edge, we should visit the sink

'''

__all__ = '''
    DFS_Case
    DFS_OpsRootCase
    Graph_DFS_Ops
    dfs
    '''.split()

from enum import Enum
DFS_Case = Enum('DFS_Case', '''
    IsolatedVtxEnterExit
    LooseAEdgeEnterExit
    RootEnter
    RootExit
    AEdgeEnter
    AEdgeExit
    ''')

DFS_OpsRootCase = Enum('DFS_OpsRootCase', '''
    IsolatedVtx
    LooseAEdge
    RootHEdge
    ''')


class Graph_DFS_Ops(ABC):
    __slots__ = ()
    @abstractmethod
    def dfs_init(self, g):
        # return dataG
        pass
    @abstractmethod
    def iter_unvisited_roots(self, g, dataG):
        # not visited when yielding it
        # yield (IsolatedVtx, vtx)
        #       | (LooseAEdge, ledge)
        #       | (RootHEdge, (is_root_hedge, vtx, hedge, aedge, dataH))
        pass
    @abstractmethod
    def pseudo_face_walk(self, g, vtx, hedge, aedge, dataH):
        # return (vtx, hedge, aedge, aedge_visited, dataH)
        pass


def dfs(ops:Graph_DFS_Ops, g):
    # assume implicit oriented
    # assume pseudo-face
    # if not aedge_visited then forward phase else backward phase
    #
    # yield (IsolatedVtxEnterExit, vtx)
    #     | (LooseAEdgeEnterExit, ledge)
    #     | (RootEnter, vtx)
    #     | (RootExit, vtx)
    #     | (AEdgeEnter, (vtx, hedge, aedge))
    #     | (AEdgeExit, (vtx, hedge, aedge))
    assert isinstance(ops, Graph_DFS_Ops)

    def handle_isolated_vtx(vtx):
        yield IsolatedVtxEnterExit, vtx
    def handle_loose_aedge(aedge):
        yield LooseAEdgeEnterExit, aedge
    def handle_non_isolated_root(is_root_hedge
        , vtx, hedge, aedge, dataH):
        # vtx -> hedge -> aedge

        #assert not aedge_visited
        yield RootEnter, vtx
        yield AEdgeEnter, (vtx, hedge, aedge)
        vtx, hedge, aedge, aedge_visited, dataH =\
            ops.pseudo_face_walk(g, vtx, hedge, aedge, dataH)

        while not is_root_hedge(hedge):
            if aedge_visited:
                #backward phase
                yield AEdgeExit, (vtx, hedge, aedge)
            else:
                #forward phase
                yield AEdgeEnter, (vtx, hedge, aedge)

            vtx, hedge, aedge, aedge_visited, dataH =\
                ops.pseudo_face_walk(g, vtx, hedge, aedge, dataH)
        assert aedge_visited
        #backward phase
        yield AEdgeExit, (vtx, hedge, aedge)
        yield RootExit, vtx
        return
    pass

    dataG = ops.dfs_init(g)
    for case, data in ops.iter_unvisited_roots(g, dataG):
        if case == RootHEdge:
            is_root_hedge, vtx, hedge, aedge, dataH = data
            it = handle_non_isolated_root(
                    is_root_hedge, vtx, hedge, aedge, dataH)
        elif case == IsolatedVtx:
            isolated_vtx = data
            it = handle_isolated_vtx(isolated_vtx)
        elif case == LooseAEdge:
            loose_aedge = data
            it = handle_loose_aedge(loose_aedge)
        else:
            raise logic-error
        yield from it
    return

