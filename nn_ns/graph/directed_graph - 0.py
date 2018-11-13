'''
dgraph = u2vtc # allows loop; multiedge

u2vtc = [[v]]
u2sorted_vtc = [sorted([v])]
dedge = (u,v)



dedges <-> u2vtc

reverse_dedge/reverse_u2vtc


u2vtc_to_strong_connected_components_ex



'''

from .dgraph_DFS import dgraph_DFS, ENTER, EXIT, HEXIT, BACK, LOOP
from .bucket_sort import bucket_sort, is_sorted
from .rooted_tree import parent2components
from collections.abc import Mapping
# from sand.big import SetPartition
# to avoid cyclic import : from .directed_acyclic_graph import reversed_topological_ordering

def rindex(seq, value):
    L = len(seq)
    for i, x in enumerate(reversed(seq)):
        if x == value:
            return L - i - 1
    else:
        raise ValueError('not found')

def up2downs_to_u2vtc_ex(up2downs):
    'Up2Downs container a = Map a (container a); u2vtc :: Map int [int]'

    #print(up2downs)
    assert isinstance(up2downs, Mapping)
    vtx2up = tuple(up2downs)

    up2vtx = dict((up, v) for v, up in enumerate(vtx2up))
    for up, downs in up2downs.items():
        for down in downs:
            try:
                assert down in up2vtx
            except:
                print(up, downs)
                print(down, set(up2vtx))
                raise

    n = len(vtx2up)
    u2vtc = [None] * n # [] for _ in range(n)]
    
    for up, downs in up2downs.items():
        v = up2vtx[up]
        u2vtc[v] = [up2vtx[down] for down in downs]
    return u2vtc, vtx2up, up2vtx



def is_u2vtc(u2vtc, n = None):
    if n == None:
        n = len(u2vtc)

    if not n == len(u2vtc) or n < 0:
        return False
        
    return all((isinstance(v, int) and 0 <= v < n) for vtc in u2vtc for v in vtc)

def is_u2sorted_vtc(u2vtc, n = None):
    if not is_u2vtc(u2vtc, n):
        return False
    
    return all(is_sorted(vtc) for vtc in u2vtc)



def dedges2u2vtc(n, dedges):
    dedges = bucket_sort(dedges, lambda e:e[1], n)
    ls = [[] for _ in range(n)]
    for u, v in dedges:
        ls[u].append(v)

    for u, vtc in enumerate(ls):
        assert is_sorted(vtc)
        if vtc:
            assert vtc[-1] < n
            assert vtc[0] >= 0
##        s = set(vtc)
##        assert len(s) == len(vtc)
##        assert u not in s

    return ls

def u2vtc2dedges(u2vtc):
    n = len(u2vtc)
    dedges = []
    for u, vtc in enumerate(u2vtc):
        dedges.extend((u, v) for v in vtc)

    dedges = bucket_sort(dedges, lambda e:e[1], n)
    dedges = bucket_sort(dedges, lambda e:e[0], n)
    assert is_sorted(dedges)
    return dedges


def reverse_dedges(dedges):
    return [(v, u) for u, v in dedges]

def reverse_u2vtc(u2vtc):
    n = len(u2vtc)
    ls = [[] for _ in range(n)]
    for u, vtc in enumerate(u2vtc):
        for v in vtc:
            ls[v].append(u)
            
    return ls


def u2vtc_to_strong_connected_components(u2vtc):
    n = len(u2vtc)
    components = []
    ungrouped_vtx_stack = []
    v2grouped = [False] * n
    v2preorder_num = [None] * n
    v2low_preorder_num = [None] * n
    curr_preorder_num = 0
    for case, path, v in dgraph_DFS(u2vtc):
        #print(case, path, v)
        if case == ENTER:
            assert v2preorder_num[v] is None
            v2preorder_num[v] = curr_preorder_num
            curr_preorder_num += 1
            
            ungrouped_vtx_stack.append(v)
            v2low_preorder_num[v] = v2preorder_num[v]
            continue

        to_group_v = not v2grouped[v]
        if to_group_v and len(path) > 1:
            u = path[-2]
            assert v == path[-1]
            v2low_preorder_num[u] = min(v2low_preorder_num[u], v2low_preorder_num[v])
            if v2preorder_num[u] >= v2preorder_num[v]:
                # [h]cross/back/loop to v ==>> not [h]exit from/[h]forward to v
                to_group_v = False # bug : once without this line

        #print(v2preorder_num[v], v2low_preorder_num[v])
        if to_group_v and v2preorder_num[v] == v2low_preorder_num[v]:
            # found a new component
            i = rindex(ungrouped_vtx_stack, v)
            new_component = ungrouped_vtx_stack[i:]
            del ungrouped_vtx_stack[i:]
##            new_component = []
##            while ungrouped_vtx_stack:
##                x = ungrouped_vtx_stack[-1]
##                if v2low_preorder_num[x] >= v2low_preorder_num[v]:
##                    new_component.append(ungrouped_vtx_stack.pop())
##                else:
##                    break
##            assert v in new_component
##            assert v == new_component[-1]
            components.append(new_component)
            for x in new_component:
                v2grouped[x] = True

    assert sum(map(len, components)) == n
    
    return sorted_components(components)

def components_to_v2std_stds(vtc_ls, vtc2std=lambda vtc:vtc[0]):
    n = sum(map(len, vtc_ls))
    v2std = [None] * n
    stds = []
    for vtc in vtc_ls:
        assert vtc
        std = vtc2std(vtc)
        assert 0 <= std < n
        
        stds.append(std)
        for v in vtc:
            assert v2std[v] is None
            v2std[v] = std

    assert all(std is not None for std in v2std)
    return v2std, stds


def sorted_components(vtc_ls):
    v2std, stds = components_to_v2std_stds(vtc_ls, min)
    n = len(v2std)
    std2vtc = [None] * n
    for std in stds:
        assert std2vtc[std] is None
        std2vtc[std] = []

    for v, std in enumerate(v2std):
        std2vtc[std].append(v)
    ls = [vtc for vtc in std2vtc if vtc is not None]
    return ls

        
def u2vtc_to_strong_connected_components_ex(u2vtc):
    vtc_ls = u2vtc_to_strong_connected_components(u2vtc)
    v2std, stds = components_to_v2std_stds(vtc_ls)
    
    inter_edges = []
    intra_edges = []
    for e in u2vtc2dedges(u2vtc):
        u, v = e
        if v2std[u] == v2std[v]:
            inter_edges.append(e)
        else:
            intra_edges.append(e)
    return vtc_ls, inter_edges, intra_edges

u2vtc = [[], [], [7, 3], [6, 11], [], [6, 2, 12], [1, 9, 4], [], [], [8, 10], [0, 5], [], []]
#print(u2vtc_to_strong_connected_components(u2vtc))
assert u2vtc_to_strong_connected_components(u2vtc) == [[0], [1], [2, 3, 5, 6, 9, 10], [4], [7], [8], [11], [12]]


def __old__u2vtc_to_strong_connected_components_ex(u2vtc):
    '''

bug:
    A->B->C->B
    A->D->C # now D->C is CROSS/HCROSS
'''  
    
    n = len(u2vtc)
    ls = []
    depth = [None] * n
    lowest_p2edges = [[] for _ in range(n)]
    v2lowest_p = [None] * n

    discarded_edges = []
    for case, path, node in dgraph_DFS(u2vtc):
        # print(case, path, node)
        if len(path) > 1:
            edge = tuple(path[-2:])
            assert len(edge) == 2
        else:
            edge = None
        if case == ENTER:
            depth[node] = len(path) - 1
        elif case == EXIT or case == HEXIT:
            if depth[node] < len(path) - 1:
                assert edge
                idx = depth[node]
                low_p = path[idx]
                v2lowest_p[node] = low_p

                p = path[-2]
                lowest_p2edges[low_p].append(edge)

                if depth[p] > idx:
                    depth[p] = idx
            elif edge:
                discarded_edges.append(edge)
                
            depth[node] = None
        elif case == BACK or case == LOOP:
            assert depth[node] != None
            assert edge
            idx = depth[node]
            low_p = path[idx]
            assert depth[low_p] <= idx
            
            p = path[-2]
            lowest_p2edges[low_p].append(edge)
            if depth[p] > idx:
                depth[p] = idx
##        elif case == LOOP:
##            raise 'test'
        else:
            assert edge
            discarded_edges.append(edge)

    vtc_ls = parent2components(v2lowest_p)
    assert is_sorted(vtc_ls)
    assert all(is_sorted(vtc) for vtc in vtc_ls)
    
    edges_ls = [[] for _ in vtc_ls]
    for edges, vtc in zip(edges_ls, vtc_ls):
        for v in vtc:
            edges.extend(lowest_p2edges[v])

    double_layer_sum = lambda ls_ls: sum(len(ls) for ls in ls_ls)
    assert double_layer_sum(u2vtc) == \
           double_layer_sum(edges_ls) + len(discarded_edges)

    return vtc_ls, edges_ls, discarded_edges
strong_connected_components = u2vtc_to_strong_connected_components_ex


##u2vtc = [[], [4, 6, 2], [], [7, 9], [8, 3, 10], [], [11, 12], [1, 5], [], [], [], [4, 0], []]
###print(u2vtc_to_strong_connected_components_ex(u2vtc)[0])
##assert u2vtc_to_strong_connected_components_ex(u2vtc)[0] == [[0], [1, 3, 4, 7], [2], [5], [6], [8], [9], [10], [11], [12]]
##assert u2vtc2dedges(u2vtc) == [(1, 2), (1, 4), (1, 6), (3, 7), (3, 9), (4, 3), (4, 8), (4, 10), (6, 11), (6, 12), (7, 1), (7, 5), (11, 0), (11, 4)]
### 1->6->11->4->3->7->1 but [1, 3, 4, 7] do not include 6, 11


def to_reversed_topological_ordered_strong_connected_components(u2vtc):
    from .directed_acyclic_graph import reversed_topological_ordering

    vtc_ls, edges_ls, discarded_edges = u2vtc_to_strong_connected_components_ex(u2vtc)
    n = len(u2vtc)
    super_n = len(vtc_ls)
    
    v2super_v = [None] * n
    super_v2component = [None] * super_n
    for super_v, vtc in enumerate(vtc_ls):
        assert vtc
        component = frozenset(vtc)
        for v in vtc:
            v2super_v[v] = super_v
        super_v2component[super_v] = component

    def to_super_vtx(vtx):
        return v2super_v[vtx]
    def to_super_dedge(e):
        u, v = e
        return to_super_vtx(u), to_super_vtx(v)
    super_dedges = set(map(tuple, map(to_super_dedge, discarded_edges)))
    super_g = dedges2u2vtc(super_n, super_dedges)
    try:
        super_vtc = reversed_topological_ordering(super_g)
    except:
        print(super_g)
        print(super_dedges)
        print(discarded_edges)
        print(vtc_ls)
        print(u2vtc)
        raise
    return list(map(super_v2component.__getitem__, super_vtc))

to_reversed_topological_ordered_strong_connected_components(u2vtc)

    
