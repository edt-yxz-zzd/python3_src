

'''
vertex = std_vertex :: UInt[0..num_vertices]
u2vtc :: [[StdVertex<num_vertices>]]{len=num_vertices}

dgraph = u2vtc


dgraph_DFS:
color:
    white - not visited
    red - visiting descendants
    grey - visited, but some income edges have not been visited
    black - all income edges have been visited
color change of v when visiting edge (u,v):
    white -> red : enter v - ENTER
    red -> red : back edge or self loop - BACK or LOOP
    red -> grey : exit but not finished - HEXIT
    red -> black : exit - EXIT
    grey -> grey : forward or cross edge, not finished - HFORWARD HCROSS
    grey -> black : forward or cross edge, finished - FORWARD CROSS

'''

__all__ = '''
    dgraph_DFS

    ENTER
    BACK
    LOOP
    HEXIT
    EXIT
    HFORWARD
    HCROSS
    FORWARD
    CROSS

    WHITE
    RED
    GREY
    BLACK
    '''.split()


# H stands for half
ENTER = 'ENTER'
BACK = 'BACK'
LOOP = 'LOOP'
HEXIT = 'HEXIT'
EXIT = 'EXIT'
HFORWARD = 'HFORWARD'
HCROSS = 'HCROSS'
FORWARD = 'FORWARD'
CROSS = 'CROSS'

WHITE = 'WHITE'
RED = 'RED'
GREY = 'GREY'
BLACK = 'BLACK'

def dgraph_DFS(u2vtc, roots=None):
    n = len(u2vtc)

    _roots = roots
    roots = []
    roots_to_try = range(n) if _roots == None else _roots

##    u2hexit_order = [None]*n
##    hexit_order = 0

    u2enter_order = [None]*n
    enter_order = 0

    nRemainIncomeEdges = [0]*n
    nEdges = 0
    for vtc in u2vtc:
        nEdges += len(vtc)
        for v in vtc:
            nRemainIncomeEdges[v] += 1
    assert nEdges == sum(nRemainIncomeEdges)
    nEdgesEnter = 0
    nEdgesExit = 0
    nEdgesEnterExit = 0


    color = [WHITE] * n
    for u in roots_to_try:
        c = color[u]
        assert c != RED
        if c != WHITE:
            continue

        root = u
        roots.append(root)


        stack = [iter((root,))] # a virtual income edge here
        nRemainIncomeEdges[root] += 1
        nEdgesEnter -= 1
        nEdgesExit -= 1

        path = []
        stack_pop = False
        while stack:
            if stack_pop:
                stack_pop = False
                assert 0 < len(path) == len(stack)

                nEdgesExit += 1
                node = path[-1]
                assert nRemainIncomeEdges[node]
                if nRemainIncomeEdges[node] > 1:
                    case = HEXIT
                    color[node] = GREY
                else:
                    case = EXIT
                    color[node] = BLACK

                if len(path) == 1:
                    assert node == roots[-1]
                yield case, path, node
                nRemainIncomeEdges[node] -= 1
                path.pop()

            assert len(path) + 1 == len(stack)
            # node = next(stack[-1])
            for node in stack[-1]:
                break
            else:
                stack.pop()
                stack_pop = True
                continue

            path.append(node)
            if not nRemainIncomeEdges[node]:
                print('\t', node)
            assert nRemainIncomeEdges[node]
            c = color[node]
            assert c != BLACK
            if c == WHITE:
                nEdgesEnter += 1
                color[node] = RED
                case = ENTER
                if len(path) == 1:
                    assert node == roots[-1]
                yield case, path, node # if len(path) == 1, then node is a selected root
                assert u2enter_order[node] == None
                u2enter_order[node] = enter_order
                enter_order += 1
##                assert u2hexit_order[node] == None
##                u2hexit_order[node] = hexit_order
##                hexit_order += 1
                stack.append(iter(u2vtc[node]))
                continue


            if c == RED:
                #color[node] = RED
                assert len(path) > 1
                if path[-2] == path[-1]:
                    case = LOOP
                else:
                    case = BACK
                yield case, path, node
            else:
                assert c == GREY
                case = FORWARD
                p = path[-2]
                assert color[p] == RED != GREY == color[node]
                assert p != node
                node_idx = u2enter_order[node]
                p_idx = u2enter_order[p]
                if node_idx < p_idx:
                    case = CROSS
##                if len(roots) > 1:
##                    node_idx = u2hexit_order[node]
##                    pre_root_idx = u2hexit_order[roots[-2]]
##                    if node_idx <= pre_root_idx:
##                        case = CROSS
                if nRemainIncomeEdges[node] > 1:
                    case = 'H' + case
                else:
                    color[node] = BLACK

                yield case, path, node

            nEdgesEnterExit += 1
            nRemainIncomeEdges[node] -= 1
            path.pop()
        else:
            assert not path


    if _roots == None:
        #assert hexit_order == n
        assert enter_order == n
        assert not any(nRemainIncomeEdges)
        for c in color: assert c == BLACK
        assert nEdges == nEdgesEnterExit + nEdgesExit == nEdgesEnterExit + nEdgesEnter

def _test_dgraph_DFS():
    dg = [[1, 2], [2], [], [0,1,2,3,4], [2,3,4]]
    dgs = [[], dg]
    for dg in dgs:
        for a in dgraph_DFS(dg):
            print(a)
    return

if '__main__' == __name__:
    _test_dgraph_DFS()

