nothing here


'''
graph operators like that in simple_undirected_graph.py
'''

from .DFS import white, black, gray, DFS
from .bucket_sort import group, group_to_list, bucket_sorts, bucket_sort
##group = bucket_sort.group
##group_to_list = bucket_sort.group_to_list
##bucket_sorts = bucket_sort.bucket_sorts
##bucket_sort = bucket_sort.bucket_sort
##white = DFS.black
##black = DFS.black
##gray = DFS.gray
##DFS = DFS.DFS


def dfs1_enter_tree_edge(G, v, w, parent_edge, lowpt, lowpt2, height):
    edge_idx = G.edge_index((v, w))
    tree_edge_direction = v < w
    
    lowpt[edge_idx] = height[v]
    lowpt2[edge_idx] = height[v]

    height[w] = height[v] + 1
    parent_edge[w] = (tree_edge_direction, edge_idx)

def dfs1_visit_back_edge(G, v, w, parent_edge, lowpt, lowpt2, height, nesting_depth):
    edge_idx = G.edge_index((v, w))
    lowpt[edge_idx] = height[w]
    dfs1_eixt_tree_edge(G, v, w, parent_edge, lowpt, lowpt2, height, nesting_depth)


def dfs1_exit_tree_edge(G, v, w, parent_edge, lowpt, lowpt2, height, nesting_depth):
    edge_idx = parent_edge[w][1]
    nesting_depth[edge_idx] = 2*lowpt[edge_idx]
    if lowpt2[edge_idx] < height[v]:#chordal
        nesting_depth[edge_idx] += 1
    e = parent_edge[v]
    if e == None: return
    e = e[1]

    if lowpt[edge_idx] < lowpt[e]:
        lowpt2[e] = min(lowpt[e], lowpt2[edge_idx])
        lowpt[e] = lowpt[edge_idx]
    elif lowpt[edge_idx] > lowpt[e]:
        lowpt2[e] = min(lowpt2[e], lowpt[edge_idx])
    else:
        lowpt2[e] = min(lowpt2[e], lowpt2[edge_idx])



def dfs2_dir_root(G, r, ls):
    return ls[r]
def dfs2_dir_node(G, p, v, ls):
    ls = ls[v]
    loc = ls.index(p)
    return ls[:loc] + ls[loc+1:]
    
def dfs2_what_color(G, p, v, parent_edge, height):
    x = parent_edge[v]
    if p == x: return white
    if height[p] < height[v]:
        return black
    return gray # back edge
def dfs2_what_color_mayroot(G, r):
    return white














def dfs2_enter_tree_edge(G, v, w, parent_edge, lowpt, lowpt2, height):
    edge_idx = G.edge_index((v, w))
    if len(conflict_pairs): stack_bottom[edge_idx] = conflict_pairs[-1]
    

def dfs2_visit_back_edge(G, v, w, parent_edge, lowpt, lowpt2, height, nesting_depth):
    edge_idx = G.edge_index((v, w))
    if len(conflict_pairs): stack_bottom[edge_idx] = conflict_pairs[-1]
    lowpt_edge[edge_idx] = edge_idx
    conflict_pairs.append(((), (edge_idx, edge_idx)))


def dfs2_exit_tree_edge(G, v, w, parent_edge, lowpt, lowpt2, height, nesting_depth):
    edge_idx = G.edge_index((v, w))
    e = parent_edge[v]
    if lowpt[edge_idx] < height[v]:# then /* ei has return edge */
if ei = e1 then
lowpt edge[e] = lowpt edge[e1]
else
I add constraints of e
i
(Algorithm 4)









def planarity_test(G):
    n = G.order()
    ne = G.num_edges()
    if n > 2 and ne > 3*n-6: raise 'not planar'

    #Phase 1 - DFS orientation and nesting order
    height = [None]*n         #tree-path distance from root
    lowpt = [None]*ne         #height of lowest return point
    lowpt2 = [None]*ne        #height of next-to-lowest return point (tree edges only)
    nesting_depth = [None]*ne #proxy for nesting order < given
    #                         #by twice lowpt (plus 1 if chordal)
    parent_edge = [None]*n    #[(u<v?, edge_idx)]

    en_tree_e = lambda G, v, w: dfs1_enter_tree_edge(\
        G, v, w, parent_edge, lowpt, lowpt2, height)
    ex_tree_e = lambda G, v, w: dfs1_eixt_tree_edge(\
        G, v, w, parent_edge, lowpt, lowpt2, height, nesting_depth)
    vi_back_e = lambda G, v, w: dfs1_visit_back_edge(\
        G, v, w, parent_edge, lowpt, lowpt2, height, nesting_depth)
    roots = DFS(G, visit_back_edge = vi_back_e, \
                enter_tree_edge = en_tree_e, exit_tree_edge = ex_tree_e)

    
    #phase 2 - Testing for LR partition
    #sort adjacency lists according to non-decreasing nesting depth
    ls = list(u, v, nesting_depth[idx] for (u, v), idx in enumerate(G.edges()))
    ls = bucket_sorts(ls, key_with_round = lambda i, e: e[i], [2, 0], N=2*n+1)
    adjacency_list = tuple(group_to_list(\
        n, ls, key = lambda e: e[0], get_data = lambda e:e[1]))

    ref = [[] for i in range(ne)] #edge relative to which side is defined
    side = [1]*ne            #side of edge, or modifier for side of reference edge
    #I = (low, high)         interval of return edges represented by its two edges
    #                        with extremal lowpoints
    #P = (L, R)              intervals with con
icting edges, i.e., a con
ict pair
    conflict_pairs = []      #S - con
ict pairs consisting of current return edges
    stack_bottom = [None]*ne #top of stack S when traversing the edge (tree edges only)
    lowpt_edge = [None]*ne   #next back edge in traversal (i.e. with lowest return point)
    DFS(G, \
        dir_root = lambda G, r: dfs2_dir_root(G,r,adjacency_list), \
        dir_node = lambda G, p, v: dfs2_dir_node(G,p,v,adjacency_list),\
        roots = roots, \
        what_color = lambda G, p, v: dfs2_what_color(G, p, v, parent_edge, height), \
        what_color_mayroot = dfs2_what_color_mayroot,..)














    
