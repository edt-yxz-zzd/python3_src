

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

__all__ = 'iter_subgraph_isomorphisms'.split()



from collections import deque
def default_incremental_partial_isomorphism_accept(A, B, idx_A2idx_B):
    return True

def subgraph_isomorphism(
        A, vertices_A, B, vertices_B,
        vertex_accept, vertex_pair_accept,
        incremental_partial_isomorphism_accept = None):
    '''see iter_subgraph_isomorphisms;
return None or [idx_B]'''
    it = iter_subgraph_isomorphisms(
        A, vertices_A, B, vertices_B,
        vertex_accept, vertex_pair_accept,
        incremental_partial_isomorphism_accept)
    return next(it, None)

def subgraph_isomorphisms(
        A, vertices_A, B, vertices_B,
        vertex_accept, vertex_pair_accept,
        incremental_partial_isomorphism_accept = None):
    '''see iter_subgraph_isomorphisms;
return [[idx_B]]'''
    it = iter_subgraph_isomorphisms(
        A, vertices_A, B, vertices_B,
        vertex_accept, vertex_pair_accept,
        incremental_partial_isomorphism_accept)
    return list(it)

    

def iter_subgraph_isomorphisms(
        A, vertices_A, B, vertices_B,
        vertex_accept, vertex_pair_accept,
        incremental_partial_isomorphism_accept = None):
    '''\
very slow
A, B :: graph
vertices_A, vertices_B :: [v]
vertex_accept :: (A, v_A, B, v_B) -> bool
vertex_pair_accept :: (A, (v_A, v_A), B, (v_B, v_B)) -> bool
incremental_partial_isomorphism_accept :: (A, B, idx_A2idx_B :: [int]) -> bool


yield [int] # list of index of B vertex
    subgraph isomorphism: vertices_A[i] -> vertices_B[result[i]]

'''
    if len(vertices_A) > len(vertices_B):
        return
    if incremental_partial_isomorphism_accept is None:
        incremental_partial_isomorphism_accept = default_incremental_partial_isomorphism_accept



    
    
    #unused_idc = set(range(len(vertices_B)))
    L = len(vertices_B)
    ls = [L] # [num_untried_idc]
    idc_deque = deque(range(L), L)
    occupied_idc = idx_A2idx_B = [] # [tring idx of vtx in vertices_B]
    num_untried_idc = len(vertices_B)

    while True:
        # tried_idc = idc_deque[num_untried_idc:]
        # unused_idc = idc_deque[:num_untried_idc]
        #     idc_deque = unused_idc ++ tried_idc
        # all_idc = occupied_idc + tried_idc + unused_idc = occupied_idc + idc_deque

        #print(ls, occupied_idc)
        assert len(occupied_idc) <= len(vertices_A)
        assert len(occupied_idc) + 1 == len(ls)
        
        if len(occupied_idc) == len(vertices_A):
            # success
            yield occupied_idc.copy() # [idx_B for idx_B, _ in ls]
            num_untried_idc = ls[-1] = 0 # mark as fail

        if not num_untried_idc: # not unused_idc
            ls.pop()
            if not ls:
                # halt
                return
            

            # restore parent num_untried_idc
            # move tring_idx from occupied to tried
            num_untried_idc = ls[-1] # tried_idc[prev]
            tring_idx = occupied_idc.pop() # pop tring = idx[prev]
            idc_deque.append(tring_idx) # tried_idc.append
            continue

        assert len(occupied_idc) < len(vertices_A)
        assert len(ls) <= len(vertices_A)
        
        # move tring_idx from unused to tried
        tring_idx = idc_deque.popleft() # unused_idc.popleft
        idc_deque.append(tring_idx) # tried_idc.append
        num_untried_idc -= 1; ls[-1] -= 1

        va = vertices_A[len(occupied_idc)]
        vb = vertices_B[tring_idx]
        if not vertex_accept(A, va, B, vb):
            continue

        occupied_idc.append(tring_idx)
        for idx_A, idx_B in enumerate(occupied_idc):
            va_ = vertices_A[idx_A]
            vb_ = vertices_B[idx_B]
            if not vertex_pair_accept(A, (va, va_), B, (vb, vb_)):
                break
        else:
            # edge test success
            
            if incremental_partial_isomorphism_accept(A, B, idx_A2idx_B):
                # additional test success!
                #print('occupied_idc grow')

                # move tring_idx from tried_idc to occupied_idc
                idc_deque.pop() # tried_idc.pop tring_idx
                # has add tring_idx to occupied_idc
                ls[-1] = num_untried_idc # update
                num_untried_idc = len(idc_deque); ls.append(num_untried_idc)
                continue
            # fail
            
        # fail
        occupied_idc.pop() # pop tring_idx
        continue

    raise ...


def test_subgraph_isomorphism():
    a, b, c, d = 'abcd'
    colors_A = ['one', 'two']
    A = [[a, b],
         [c, d]],\
        colors_A
         
    colors_B = ['one', 'two', 'one', 'xxxx']
    B = [[a, 9, 9, b],
         [9, d, c, 9],
         [9, b, a, b],
         [c, 9, c, d]],\
        colors_B
    colors_C = ['two', 'two', 'one', 'two']
    C = [[d, 9, c, b],
         [9, d, c, 9],
         [b, b, a, b],
         [c, 9, c, d]],\
        colors_C

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
    rs = subgraph_isomorphisms(A, to_vertices(A), B, to_vertices(B), color_accept, weight_accept)
    rsAC = subgraph_isomorphisms(A, to_vertices(A), C, to_vertices(C), color_accept, weight_accept)
    try:
        assert r == [2,1]
        assert rs == [[2,1]]
        assert rsAC == [[2, 3], [2, 0], [2, 1]]
    except:
        print(r)
        print(rs)
        print(rsAC)
        raise


test_subgraph_isomorphism()


    








