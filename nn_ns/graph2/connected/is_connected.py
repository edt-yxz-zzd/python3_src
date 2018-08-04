


def is_ugraph_connected(dfs, is_new_round)
    '''test whether a ugraph is connected

input:
    dfs :: Iter (case, payload)
    is_new_round :: (case, payload) -> bool
        True for each connected component
output:
    null_graph is connected
    K[1] is connected
    graph with (num_connected_components < 2) is connected
'''
    dfs = iter(dfs)
    def round():
        for case_payload in dfs:
            if is_new_round(case_payload):
                return 1
        return 0
    return round() + round() < 2
def is_dgraph_weakly_connected(dfs, discover, 
def is_bgraph_weakly_connected(dfs, NewPhase, *, case_eq):
    '''test whether a bgraph is weakly connected

input:
    dfs :: Iter (case, payload)
    NewPhase is a case at the begin per round
    # why not RootEnter? loose_edge
    # why not NewComponent? weak, sink at beginning
output:

problem:
    null_graph
    loose_edge
    isolated_vtx
'''


