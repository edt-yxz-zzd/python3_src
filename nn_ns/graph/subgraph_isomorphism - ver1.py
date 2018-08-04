

'''
graph A, B
    A <= B ??
    if yes, find out a[i]->b[i]


v[G] - vertex of G
e[G] = (v[G], v[G])
color_accept(v[A], v[B])

weight_accept(e[A], e[B])
    exists a order of edges between the two vertices, s.t.
        # num (a1, a2) <= num (b1, b2)
        (a1, a2) -> (b1, b2)
        weight(a1, a2) accepted by weight(b1, b2)
        and same for (2, 1), {1,2}
        # (x,y) is directed-edge, {x,y} is undirected-edge

incremental_partial_isomorphism_accept(idx_A2idx_B)
    idx_A2idx_B - map v[A][i] -> v[B][idx_A2idx_B[i]]
    to check whether the last mapping pair (len(idx_A2idx_B)-1, idx_A2idx_B[-1])
        satisfies additional constraint

'''

__all__ = 'subgraph_isomorphism'.split()



from collections import deque
def default_incremental_partial_isomorphism_accept(A, B, idx_A2idx_B):
    return True
def subgraph_isomorphism(A, vertices_A,
                         B, vertices_B,
                         color_accept, weight_accept,
                         incremental_partial_isomorphism_accept = None):
    '''\
very slow
A, B :: graph
vertices_A, vertices_B :: [v]
color_accept :: (A, v_A, B, v_B) -> bool
weight_accept :: (A, (v_A, v_A), B, (v_B, v_B)) -> bool
incremental_partial_isomorphism_accept :: (A, B, idx_A2idx_B :: [int]) -> bool


if success:
    return [int] # list of index of B vertex
    subgraph isomorphism: vertices_A[i] -> vertices_B[result[i]]
else:
    return False
'''
    if len(vertices_A) > len(vertices_B):
        return False
    if incremental_partial_isomorphism_accept is None:
        incremental_partial_isomorphism_accept = default_incremental_partial_isomorphism_accept

    ls = [] # [(tring idx of vtx in vertices_B, num_untried_idc)]
    #unused_idc = set(range(len(vertices_B)))
    L = len(vertices_B)
    idc_deque = deque(range(L), L)
    occupied_idc = idx_A2idx_B = []
    num_untried_idc = len(vertices_B)

    while len(ls) < len(vertices_A):
        # tried_idc = idc_deque[num_untried_idc:]
        # unused_idc = idc_deque[:num_untried_idc]
        #     idc_deque = unused_idc + tried_idc
        # occupied_idc = [idx for idx, _ in ls]
        # all_idc = occupied_idc + tried_idc + unused_idc = occupied_idc + idc_deque
        #print(ls)

        if not num_untried_idc: # not unused_idc
            if not ls:
                # halt
                return False
            
            #unused_idc = tried_idc # tried_idc[curr]
            tring_idx, num_untried_idc = ls.pop() # tring = idx[prev], tried_idc[prev]
            occupied_idc.pop() # pop tring_idx
            idc_deque.append(tring_idx) # tried_idc.append
            continue
        
        tring_idx = idc_deque.popleft() # unused_idc.popleft
        idc_deque.append(tring_idx) # tried_idc.append
        num_untried_idc -= 1

        va = vertices_A[len(ls)]
        vb = vertices_B[tring_idx]
        if not color_accept(A, va, B, vb):
            continue

        for idx_A, (idx_B, _) in enumerate(ls):
            va_ = vertices_A[idx_A]
            vb_ = vertices_B[idx_B]
            if not weight_accept(A, (va, va_), B, (vb, vb_)):
                break
        else:
            # pass edge test
            if incremental_partial_isomorphism_accept(A, B, idx_A2idx_B):
                # success!
                idc_deque.pop() # tried_idc.pop tring_idx
                ls.append((tring_idx, num_untried_idc))
                occupied_idc.append(tring_idx)
                num_untried_idc = len(idc_deque)
                continue
            # fail
            
        # fail
        continue

    # success
    return [idx_B for idx_B, _ in ls]


def test_subgraph_isomorphism():
    a, b, c, d = 'abcd'
    colors_A = ['one', 'two']
    A = [[a, b],
         [c, c]],\
        colors_A
         
    colors_B = ['one', 'two', 'one', 'xxxx']
    B = [[a, 9, 9, b],
         [9, d, c, 9],
         [9, b, a, 9],
         [c, 9, 9, d]],\
        colors_B

    def color_accept(A, va, B, vb):
        get_color = lambda G, v: G[1][v]
        return get_color(A, va) == get_color(B, vb)

    def weight_accept(A, ea, B, eb):
        def get_weight(G, e):
            u, v = e
            g = G[0]
            return g[u][v], g[v][u]
        return get_weight(A, ea) == get_weight(B, eb)
        

    to_vertices = lambda G: list(range(len(G[0])))
    r = subgraph_isomorphism(A, to_vertices(A), B, to_vertices(B), color_accept, weight_accept)
    assert r == [2,1]


test_subgraph_isomorphism()


    








