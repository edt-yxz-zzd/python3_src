'''

[Graph_Isomorphism_1981]PRACTICAL_GRAPH_ISOMORPHISM


ordered_partition = vertices::[int], end_of_cell::[bool]
example: 1234, FFTT => '123' '4'
requirement: elements in a cell should be sorted. '321' is error.

G = [[int]] # directed graph in adjection list form.
G[v] should be a sorted list

alpha = [(begin::int, end::int)] # some cells of ordered_partition
ordered_partition.vertices[begin:end]

'''
import collections # deque
import itertools # groupby
from sand import find, lens2rngs, intersect_sorted_list, is_main

##if is_main(__name__) and '__path__' not in globals():
##    __path__ = ['graph']
    
from .bucket_sort import is_sorted
from .directed_graph import is_u2sorted_vtc



def degree_v2cell(G, v, cell):
    vtc = G[v]
    r = intersect_sorted_list(vtc, cell)
    return len(r)


def refine_cell(G, cell, alpha_cell):
    assert cell
    assert alpha_cell
    
    degree_v_ls = [(degree_v2cell(G, v, alpha_cell), v) for v in cell]
    degree_v_ls.sort()

    vcells = []
    bcells = [False] * len(cell)
    for k, g in itertools.groupby(degree_v_ls, lambda deg_v:deg_v[0]):
        vcells.extend(v for deg, v in g)
        bcells[len(vcells)-1] = True

    assert len(vcells) == len(bcells) == len(cell)
    assert bcells[-1] == True
    return vcells, bcells
    
def end_of_cell2lens(end_of_cell):
    begin = 0
    N = len(end_of_cell)
    assert N

    ls = []
    while begin < N:
        end = 1 + end_of_cell.index(True, begin)
        L = end - begin
        assert L
        ls.append(L)
        
        begin = end
    assert end == N

    assert ls
    assert sum(ls) == N
    return ls

def rngs2end_of_cell(rngs, offset=0):
    ls = []
    for begin, end in rngs:
        assert begin == offset
        offset = end
        L = end - begin
        assert L > 0
        ls.extend([False] * L)
        ls[-1] = True
    return ls

def end_of_cell2rngs(end_of_cell, offset = 0):
    lens = end_of_cell2lens(end_of_cell)
    return lens2rngs(lens, offset)

def nontrival_cell_rngs(end_of_cell, *, end=0):
    N = len(end_of_cell)
    while True:
        # move to next nontrival cell
        begin = find(end_of_cell, False, end)
        if begin == -1:
            # this round ends
            # start next round
            break
        
        assert not end_of_cell[begin]
        end = 1 + end_of_cell.index(True, begin)
        assert 0 <= begin < end <= N
        yield begin, end
    return

def alpha_cells(alpha_queue, vertices):
    while alpha_queue:
        rng = alpha_queue.popleft()
        _begin, _end = rng
        alpha_cell = vertices[_begin : _end]
        yield alpha_cell
    return


def refine_ordered_partition_to_coarsest_equitable(u2sorted_vtc, ordered_partition, alpha):
    vertices, end_of_cell = ordered_partition
    G = u2sorted_vtc
    assert len(G) == len(end_of_cell) == len(vertices)

    
    N = len(vertices)
    assert N
    assert end_of_cell[-1]

    assert is_u2sorted_vtc(G)
    assert set(range(N)) == set(vertices)
    _rngs = end_of_cell2rngs(end_of_cell)
    assert all(is_sorted(vertices[begin:end]) for begin, end in _rngs)
    assert set(alpha) <= set(_rngs)
    
    

    
    alpha_queue = collections.deque(alpha, N)
    vertices, end_of_cell = partition = (list(vertices), list(end_of_cell))
    del alpha
    for alpha_cell in alpha_cells(alpha_queue, vertices):
        for begin, end in nontrival_cell_rngs(end_of_cell):
            partition_cell = vertices[begin : end]

            vcells, bcells = refine_cell(G, partition_cell, alpha_cell)
            n = bcells.count(True)
            assert n
            if n == 1:
                # no thing happens
                pass
            else:
                vertices[begin : end] = vcells
                end_of_cell[begin : end] = bcells
                
                lens = end_of_cell2lens(bcells)
                t = lens.index(max(lens))
                rngs = lens2rngs(lens, begin)
                assert len(rngs) > 1
                assert rngs[0][0] == begin
                assert rngs[-1][-1] == end

                # handle rngs[t]
                for i, beg_end in enumerate(alpha_queue):
                    if beg_end == (begin, end):
                        alpha_queue[i] = rngs[t]
                        break

                # skip rngs[t]
                alpha_queue.extend(rngs[:t])
                alpha_queue.extend(rngs[t+1:])


    assert len(vertices) == len(end_of_cell) == N
    return partition



def test_refine_ordered_partition_to_coarsest_equitable():
    t, f = True, False 
    G_ordp_result = [
        ([[1], [2], []], ([0, 1, 2], [f, f, t]), ([2, 0, 1], [t, t, t])),
        ([[]], ([0], [t]), ([0], [t])),
        ([[1], []], ([0, 1], [t, t]), ([0, 1], [t, t])),
        ([[1], []], ([0, 1], [f, t]), ([1, 0], [t, t])),
        ([[1], [2], [0]], ([0, 1, 2], [f, f, t]), ([0, 1, 2], [f, f, t])),
        ([[2], [2], []], ([0, 1, 2], [f, f, t]), ([2, 0, 1], [t, f, t])),
        ]
    
    for G, ordp, result in G_ordp_result:
        end_of_cell = ordp[-1]
        rngs = end_of_cell2rngs(end_of_cell)
        
        
        r1 = refine_ordered_partition_to_coarsest_equitable(G, ordp, rngs)

        m = len(G[0])
        if all(m == len(vtc) for vtc in G):
            # regular graph
            r2 = refine_ordered_partition_to_coarsest_equitable(G, ordp, rngs[:-1])
            assert r1 == r2
        
        if not r1 == result:
            print(r1)
            print(result)
        assert r1 == result
        assert r1 == result
    return

if __name__ == '__main__':
    test_refine_ordered_partition_to_coarsest_equitable()








