'''
[2001]A linear time implementation of SPQR-trees
[1973]Dividing a Graph into Triconnected Components

'''


'''
preprocess
g : biconnected-undirected-multi-graph-without-loops
DFS(g)->dfs_tree with back-edge, depth[v] (that is height in dfs-tree)
    lowpt1_depth[v] lowpt2_depth[v]
give each edge a direction as the first DFS: new_e2old_de[e] # new_e is old_normal_e
known whether an edge is a tree arc: is_tree_arc[e]
calc sort_key[e] by is_tree_arc[e], depth[v] lowpt1_depth[v] lowpt2_depth[v]
sort back-edges and subtree-arcs of a node by sort_key[e]
now we got a new tree, but needed to be relabel.

DFS(new-tree) by the ordering of sorted edges
label nodes by postfix order with reversed(range(n))
relabel(new-tree)->finial-tree
relabel edges


'''
import itertools
from .bucket_sort import bucket_sorts
from .multi_graph import connected_undirected_mgraph2directed_palm_tree, \
     inv_automap, item_map, mx_map, rows_map, \
     multi_graph, make_mgraph, dfs_ordering, find_lowpt_k, \
     make_mgraph_from_e2undirected_vtc_pairs, \
     palm_tree2tree_info, \
     enter_edge, back_edge, dead_edge, exit_edge, \
     enter_root, exit_root, loop_edge

def preprocess(g, DFS):
    n = g.nv()
    k = 2

    if DFS == None:
        DFS = g.DFS()
    # for palm_tree
    roots, palm_tree, new_e2old_de = \
           connected_undirected_mgraph2directed_palm_tree(g, DFS)
    assert len(roots) == 1
    root, = roots


    
    # for v2lows
    v2lows = find_lowpt_k(palm_tree, k, start_vtc_or_edges=[('v', root)])



    # for v2depth
    is_tree_arc, v2enter_edge, v2parent, v2depth, \
                 v2num_enter_edges, v2num_children, \
                 v2num_out_back_edges, v2num_in_back_edges = \
                 palm_tree2tree_info(roots, palm_tree)

    # for v2low_depths
    v2low_depths = [[v2depth[lowpt] for lowpt in lows]
                    for lows in v2lows]


    # to sort edges
    edge_keys = [None]*g.ne()
    for e in palm_tree.edges():
        parent, child = palm_tree.edge2ends(e)
        if is_tree_arc[e]:
            key = 3*v2low_depths[child][0] + 0
            if v2low_depths[child][1] >= v2depth[parent]:
                key += 2
        else:
            key = v2depth[child]
            key += 1
        edge_keys[e] = (parent, key, e)

    edge_keys = bucket_sorts(edge_keys, lambda i, e: e[i], [1,0], [n*3+2, n])

    # for child-edges-sorted palm-tree
    adj = [[] for _ in range(n)]
    # sorted outgoings
    for parent, _, e in edge_keys:
        adj[parent].append(e)
    # padding incoming edges
    for parent, _, e in edge_keys:
        child = palm_tree.edge2end(e)
        assert palm_tree.is_normal(e)
        adj[child].append(palm_tree.flip(e))
    # update palm tree adj order
    palm_tree = palm_tree.reposition_edges(adj)


    # relabel g/tree
    prefix_ordering, postfix_ordering = \
        dfs_ordering(palm_tree, palm_tree.\
                     DFS(start_vtc_or_edges=[('v', root)]))
    
    postfix_ordering.reverse()
    new_vtx2old_vtx = postfix_ordering
    del postfix_ordering
    old_vtx2new_vtx = inv_automap(new_vtx2old_vtx)
    assert old_vtx2new_vtx[root] == 0
    root = 0
    roots = [root]

    palm_tree, _new_edge2old_edge, _old_edge2new_edge = \
               palm_tree.relabel_vertices(old_vtx2new_vtx)
    # edge numbers are not changed, since palm tree is a digraph
    assert list(_old_edge2new_edge) == list(range(palm_tree.ne()))


    # recalc ...
    v2low_depths = rows_map(v2low_depths, old_vtx2new_vtx, new_vtx2old_vtx)
    v2depth = rows_map(v2depth, old_vtx2new_vtx, new_vtx2old_vtx)
    is_tree_arc, v2enter_edge, v2parent, _v2depth, \
                 v2num_enter_edges, v2num_children, \
                 v2num_out_back_edges, v2num_in_back_edges = \
                 palm_tree2tree_info(roots, palm_tree)
    assert _v2depth == v2depth
    new_edge2old_dedge = new_e2old_de

    # undirected-graph, needn't to count incomings
    g_v2degree = [g.num_outgoings(v) for v in g.vertices()] 

    tree_v2degree_fromgraph = rows_map(
        g_v2degree, old_vtx2new_vtx, new_vtx2old_vtx)
    tree_v2degree = [palm_tree.num_edges(v) for v in palm_tree.vertices()]
    tree_v2degree_fromsum = [sum(nums) for nums in zip(
        v2num_enter_edges, v2num_children, \
        v2num_out_back_edges, v2num_in_back_edges)]

    assert tree_v2degree == tree_v2degree_fromgraph
    assert tree_v2degree == tree_v2degree_fromsum
    v2degree = tree_v2degree

    
    v2back_edges_to_me = [[] for _ in palm_tree.vertices()]
    num_descendants = [1] * palm_tree.nv()
    for case, edges, v in palm_tree.DFS():
        if case == back_edge:
            v2back_edges_to_me[v].append(edges[-1])
        elif case == exit_edge:
            e = edges[-1]
            parent = palm_tree.edge2src(e)
            num_descendants[parent] += num_descendants[v]
    for es in v2back_edges_to_me:
        es.reverse()

        
    assert palm_tree.num_outgoings(root) == 1 # biconnected
    return palm_tree, new_edge2old_dedge, \
           old_vtx2new_vtx, new_vtx2old_vtx, \
           v2depth, v2low_depths, \
           is_tree_arc, v2enter_edge, v2parent, v2degree, \
           v2num_enter_edges, v2num_children, \
           v2num_out_back_edges, v2num_in_back_edges,\
           v2back_edges_to_me, num_descendants



def maxsplitted_SPQR_components2types(virtual_edge2vtx_pair,
                                       component2virtual_edges):
    '''identify component type, that is S, P, Q or R

maxsplitted_SPQR_component:
    each P is a 3-bone
    each S is a cycle of length 3
    Q if presented, should be the only one component
    Q contains one or two edges

'''

    edges, components = virtual_edge2vtx_pair, component2virtual_edges
    def edges2type(es, components):
        L = len(es)
        if L > 3:
            return 'R'
        
        s = set(x for e in es for x in edges[e])
        if L < 3:
            if len(components) == 1 and len(s) == 2:
                return 'Q'
            if L == 0:
                raise Exception('SPQR contains an empty component')
            if len(s) == 2:
                raise Exception('maxsplitted_SPQR: Q not the only one component')
            raise Exception('unknown type')
            raise logic-error
        
        L = len(s)
        if L == 2:
            return 'P'
        if L == 3:
            return 'S'

        raise logic-error
    
    component2type = [edges2type(es, components) for es in components]
    return component2type
    

def basic_SPQR(g, DFS):
    o = __SPQR(g, DFS)
    o.find_split_components()
    edges, components, tree, new_edge2old_dedge,\
           old_vtx2new_vtx, new_vtx2old_vtx = o.get_result()
    new_e2old_e = [g.normal(de) for de in new_edge2old_dedge]
    assert list(g.edges()) == new_e2old_e # edge nums keep the same
    if not list(g.edges()) == new_e2old_e:
        raise Exception('unknown, logic-error??')
    #print('components', components, 'edges', edges)
    #print('components', list(list(edges[e] for e in es) for es in components))

    # e2old_pair
    edges = [[new_vtx2old_vtx[x] for x in uv] for uv in edges]
    edges = map(sorted, edges)
    edges = tuple(map(tuple, edges))
    # classify component with only 3 edges to P or S
    component2type = maxsplitted_SPQR_components2types(edges, components)
    old_edge2virtual_edge = old_e2new_e = new_e2old_e
    virtual_edge2vtx_pair = edges
    component2virtual_edges = components
    return component2type, virtual_edge2vtx_pair, \
           component2virtual_edges, old_edge2virtual_edge

def basic2merged_SPQR(virtual_from, component2type, virtual_edge2vtx_pair, \
                      component2virtual_edges):
    r = component2type, edge2pair, components =\
        merge_oversplitted_SPQR_components(
            virtual_from,
            component2type, 
            virtual_edge2vtx_pair,
            component2virtual_edges)
    return r

def SPQR(g, DFS=None):
    '''decompose a biconnected undirected multi-graph to SPQR components
'''

    component2type, edges, components, old_e2new_e = basic_SPQR(g, DFS)
    # component as vertex, virtual edge as edge
    # make a super-tree
    # all connected P's (or S's) are merged together
    # form a maximum P (or S)
    # erase duplicated virtual edges in these new components
    virtual_from = g.ne()
    component2type, edge2pair, components =\
                    basic2merged_SPQR(virtual_from, component2type,
                                      edges, components)

    return component2type, edge2pair, components

def merge_oversplitted_SPQR_components(virtual_from,
                                       component2type,
                                       virtual_edge2vtx_pair,
                                       component2virtual_edges):
    '''merge connected S's or P's, relabel or drop some virtual edges

oversplitted_SPQR_component:
    may exist some connected S's or P's
'''
    edges, components = virtual_edge2vtx_pair, component2virtual_edges
    ne = virtual_from
    num_virtual_edges = len(edges) - ne
    # num_virtual_edges == num_components - 1
    assert num_virtual_edges == len(components) - 1
    assert sum(map(len, components)) == ne + 2*num_virtual_edges
    
    # super_edge = virtual_edge - virtual_from
    super_edge2component_idcs = [[] for _ in range(len(edges) - virtual_from)]
    for i, es in enumerate(components):
        for e in es:
            if e >= virtual_from:
                super_e = e - virtual_from
                super_edge2component_idcs[super_e].append(i)
    assert all(len(idcs) == 2 for idcs in super_edge2component_idcs)

    # super edge2pair->graph->tree to get tree info
    # only to check that super graph is really a tree
    super_edge2pairs = super_edge2component_idcs
    super_G = make_mgraph_from_e2undirected_vtc_pairs(
        len(components), super_edge2pairs)
    roots, super_tree, new_e2old_de = \
           connected_undirected_mgraph2directed_palm_tree(
               super_G, super_G.DFS())
    if not len(roots) == 1:
        raise Exception('SPQR components do not connected by virtual edges')
    
    is_tree_arc, v2enter_edge, v2parent, v2depth, \
           v2num_enter_edges, v2num_children, \
           v2num_out_back_edges, v2num_in_back_edges = \
           palm_tree2tree_info(roots, super_tree)

    if not sum(v2num_in_back_edges) == 0:
        raise Exception('SPQR not form a tree')


    # find out connected P's or S's
    component2merge_to_idx = list(super_tree.vertices())
    #merged_component2super_edges_discarded = [[] for _ in super_tree.nv()]
    super_edge2discarded = [False] * super_tree.ne()
    for case, es, v in super_tree.DFS():
        if case == enter_edge:
            e = es[-1]
            parent, child = super_tree.edge2ends(e)
            if component2type[parent] == component2type[child] != 'R':
                lowest_idx = component2merge_to_idx[parent]
                component2merge_to_idx[child] = lowest_idx
                #merged_component2super_edges_discarded[lowest_idx].append(e)
                super_edge2discarded[e] = True


    # after merging, some super-edges hence co-virtual-edges
    # will be discarded. now relabel and move them to the end.
    new_super_edge2old = [e for discared, e in \
                          zip(super_edge2discarded, super_tree.edges()) \
                          if not discared]
    discared_from = len(new_super_edge2old)
    new_super_edge2old.extend(e for discared, e in \
                          zip(super_edge2discarded, super_tree.edges()) \
                          if discared)
    old_super_edge2new = inv_automap(new_super_edge2old)

    old_edge2new = list(range(ne))
    old_edge2new.extend(new_super_e + virtual_from
                        for new_super_e in old_super_edge2new)
    discared_from += virtual_from

    
    # relabel ...
    edges, components
    components = [[old_edge2new[e] for e in es] for es in components]
    # reposition
    new_edge2old = inv_automap(old_edge2new)
    edges = rows_map(edges, old_edge2new, new_edge2old)
    
    # merges
    for to_idx, es in zip(component2merge_to_idx, components):
        to_component = components[to_idx]
        if to_component is es:
            continue
        to_component.extend(es)
        es.clear()

    # drop discared virtual edges
    component2type = [typ for typ, es in zip(component2type, components) if es]
    components = [[e for e in es if e < discared_from]
                  for es in components if es]
    assert len(component2type) == len(components)

    edge2pair = edges[:discared_from]

    num_virtual_edges = len(edge2pair) - ne
    assert len(components)-1 == num_virtual_edges
    assert sum(map(len, components)) == ne + 2*num_virtual_edges

    return component2type, edge2pair, components
    
    
        
                    

class __SPQR:
    def __init__(self, g, DFS):
        '''decompose a biconnected undirected multi-graph to SPQR components
'''
        n = g.nv()
        self.g = g
        palm_tree, new_edge2old_dedge, \
           old_vtx2new_vtx, new_vtx2old_vtx, \
           v2depth, v2low_depths, \
           is_tree_arc, v2enter_edge, v2parent, v2degree, \
           v2num_enter_edges, v2num_children, \
           v2num_out_back_edges, v2num_in_back_edges, \
           v2back_edges_to_me, num_descendants = preprocess(g, DFS)

        self.tree = self.palm_tree = tree = palm_tree
        self.new_edge2old_dedge = new_edge2old_dedge
        self.old_vtx2new_vtx = old_vtx2new_vtx
        self.new_vtx2old_vtx = new_vtx2old_vtx
        self.v2depth = v2depth
        self.v2low_depths = v2low_depths
        self.v2back_edges_to_me = v2back_edges_to_me # immutable!!!
        self.num_descendants = num_descendants








        
        self.components = []

        # contains already visited edges that are not yet assigned to a split component.
        self.E = [] 
        # contains triples (h; a; b) (or a special end-of-stack marker EOS), such
        # thatf (a, b) is a potential type-2 separation pair, and h is the highest
        # numbered vertex in the component that would be split off.
        self.T = []

        # when add/remove edge
        self.v2deg = v2degree # mutable
        # if tree_arc
        self.parent = v2parent # mutable
        self.num_children = v2num_children # mutable
        self.v2enter_edge = v2enter_edge # mutable
        self.num_enter_edges = v2num_enter_edges # mutable
        # not tree_arc
        self.num_out_back_edges = v2num_out_back_edges # mutable
        self.num_in_back_edges = v2num_in_back_edges # mutable

        # when add new virtaul edge:
        # to add new virtual edges
        self.edges = [tree.edge2ends(e) for e in tree.edges()]
        self.is_edge_in_G = [True] * tree.ne()
        self.is_tree_arc = is_tree_arc  # mutable


        # others:
        # let e = x~>me, largest x last
        # using at max_back_edge_from_to
        # need not be changed, in fact, only the max x used.
        self.back_edges_to_me = v2back_edges_to_me
        # using depth to find a1 when doing dfs
        self.dfs_edges = None
        self.is_only_childedge_tree_arc_flags = [False]*n

    def get_degs_of(self, v):
        v2deg_ls = (self.num_children, self.num_out_back_edges,\
                    self.num_in_back_edges, self.num_enter_edges)
        return [v2deg[v] for v2deg in v2deg_ls]
    def check_deg(self, v):
        #print(self.get_degs_of(v))
        assert sum(self.get_degs_of(v)) == self.v2deg[v]
        
    def max_descendants(self, v):
        return v + self.num_descendants[v] - 1
    def get_result(self):
        return self.edges, self.components, \
               self.tree, self.new_edge2old_dedge,\
               self.old_vtx2new_vtx, self.new_vtx2old_vtx
    
    def make_P_node(self, edge_remain, back_edge):
        # P node, tri-bond
        assert set(self.edges[edge_remain]) == set(self.edges[back_edge])
        v, w = self.edges[edge_remain]
        C = self.new_component([edge_remain, back_edge])
        return self.new_virtual_edge(C, v, w)
        
    def deg(self, v):
        return self.v2deg[v]
    

    def add_edge_to_G(self, v, w):
        assert len(self.is_tree_arc) == len(self.edges) == len(self.is_edge_in_G)
        e = len(self.edges)
        self.edges.append((v,w))
        self.is_edge_in_G.append(True)

        # assume back edge as if v ~> w
        self.is_tree_arc.append(False) # using make_tree_edge to inverse it

        self.v2deg[v] += 1
        self.v2deg[w] += 1
        self.num_out_back_edges[v] += 1
        self.num_in_back_edges[w] += 1
        
        return e
    def remove_edges_from_G(self, edges):
        for e in edges:
            if not 0 <= e < len(self.is_edge_in_G) or not self.is_edge_in_G[e]:
                print('self.is_edge_in_G', self.is_edge_in_G)
                print('e', e)
                print('edges', edges)
            assert self.is_edge_in_G[e] == True
            self.is_edge_in_G[e] = False
            v, w = self.edges[e]
            self.v2deg[v] -= 1
            self.v2deg[w] -= 1
            if self.is_tree_arc[e]:
                self.is_tree_arc[e] = False
                parent, child = v, w
                self.parent[child] = None
                self.num_enter_edges[child] -= 1
                self.v2enter_edge[child] = None
                self.num_children[parent] -= 1
            else:
                self.num_out_back_edges[v] -= 1
                self.num_in_back_edges[w] -= 1
                
                
            
            
    def new_component(self, edges):
        #print('new_component remove', edges)
        self.remove_edges_from_G(edges)
        C = list(edges)
        self.components.append(C)
        return C
    def add_edges(self, component, edges):
        component.extend(edges)
        self.remove_edges_from_G(edges)
        return
    def new_virtual_edge(self, component, v, w):
        #add(Gc, (v,w))
        e = self.add_edge_to_G(v, w)
        component.append(e)
        #print('new_virtual_edge', component, e, (v, w))
        return e
    def make_tree_edge(self, e):
        if not self.is_edge_in_G[e] or self.is_tree_arc[e]:
            raise logic-error

        # old edge was back edge
        # v~>w delete
        v, w = self.edges[e] 
        self.num_out_back_edges[v] -= 1
        self.num_in_back_edges[w] -= 1

        # changes to tree edge
        # v->w add
        parent, child = v, w
        self.is_tree_arc[e] = True
        assert self.parent[child] == None
        assert self.v2enter_edge[child] == None
        self.v2enter_edge[child] = e
        self.parent[child] = v
        self.num_enter_edges[child] += 1
        self.num_children[parent] += 1
        return
    
    def is_only_childedge_tree_arc(self, v):
        # called at most once
        flags = self.is_only_childedge_tree_arc_flags
        if flags[v]:
            raise logic-error
        flags[v] = True

        self.check_deg(v)
        assert self.deg(v) == 2
        assert v != 0
        assert self.num_children[v] + self.num_out_back_edges[v] == 1
        assert self.num_children[v] >= 0
        assert self.num_out_back_edges[v] >= 0
        return self.num_children[v] == 1



    
        
    def only_childedge_to(self, v):
        # called at most once
        # return the only child or the only back edge
        raise

    def max_back_edge_from_to(self, w):
        # if exists v~>w, return max v
        # else 0

        # need not be changed, in fact, only the max x used.
        es = self.back_edges_to_me[w]
        if not es:
            return 0 # it's ok, since root is small enough

        e = es[-1]
        # even e was removed!
        v, _w = self.edges[e]
        assert _w == w
        return v
    
    def high(self, w):
        #max(v for v ~> w) or -1 # or first visited 
        raise
    def path_search(self, v):
        stack = []
        begin_path = True # path is -*->~>; that is a ear
        wrong_cases = {loop_edge, dead_edge}
        not_used_cases = {exit_root} | wrong_cases
        
        for action, edges, v in self.palm_tree.DFS():
            self.dfs_edges = edges
            if edges:
                edge = edges[-1]
            else:
                edge = None
                del edge
                
            if action == enter_root:
                begin_path = True
            elif action == enter_edge:
                stack.append(begin_path)
                self.enter_tree_arc(begin_path, edge)
                begin_path = False
            elif action == back_edge:
                stack.append(begin_path)
                self.enter_back_arc(begin_path, edge)
                begin_path = False

                # exit back edge
                begin_path = stack.pop()
                self.exit_back_arc(begin_path, edge)
                begin_path = True
            elif action == exit_edge:
                begin_path = stack.pop()
                self.exit_tree_arc(begin_path, edge)
                begin_path = True
            elif action in not_used_cases:
                if action in wrong_cases:
                    raise ValueError('not a tree')
            else:
                raise


    def middle_backto_root_section(self, edge,
                                   back_edge_tail_depth,
                                   biggest_vtx_in_middle):
        v, w = self.edges[edge]
        tri = (biggest_vtx_in_middle, back_edge_tail_depth, v)
        T = self.T[-1]
        biggest_vtcs = []
        while T:
            biggest_vtx, max_a2_depth, possible_b2 = T[-1]
            if max_a2_depth > back_edge_tail_depth:
                # reduce max_a2 to back_edge_tail
                # all these subtrees are merged together
                # biggest_vtx be max one
                T.pop()
                biggest_vtcs.append(biggest_vtx)
                last_possible_b2 = possible_b2
            else:
                break
                
        if biggest_vtcs:
            biggest_vtcs.append(biggest_vtx_in_middle)
            biggest_vtx = max(biggest_vtcs)
            tri = (biggest_vtx, back_edge_tail_depth, last_possible_b2)
        return tri
    
    def enter_tree_arc_begin_path(self, edge):
        v, w = self.edges[edge]

        # assume this a (a2, b2)
        possible_b2 = v
        max_a2_depth_from_w = self.v2low_depths[w][0]
        biggest_vtx_in_tree_w = self.max_descendants(w)
        tri = (biggest_vtx_in_tree_w, max_a2_depth_from_w, possible_b2)


        # assume in middle section
        # if edge in middle section of some previous tri
        # previous possible (a2, b2) # v may be a2
        # possible_a2 -+-> v
        # middle section contains w
        depth_back_to_root_section = self.v2low_depths[w][0]
        biggest_vtx_in_middle = biggest_vtx_in_tree_w # if a2 == v
        tri = self.middle_backto_root_section(edge, 
                            depth_back_to_root_section,
                            biggest_vtx_in_middle)
        
        T = self.T[-1]
        T.append(tri)
        self.T.append([])
        
        
        
    def enter_tree_arc(self, begin_path, edge):
        if begin_path:
            self.enter_tree_arc_begin_path(edge)
        return
    
    def enter_back_arc_begin_path(self, edge):
        v, w = self.edges[edge]
        # if v in some middle of (a2:b2)
        depth_back_to_root = self.v2depth[w]
        biggest_vtx_in_middle = v
        tri = self.middle_backto_root_section(edge, 
                            depth_back_to_root,
                            biggest_vtx_in_middle)
        T = self.T[-1]
        T.append(tri)
        self.T.append([])
    
    def enter_back_arc(self, begin_path, edge):
        if begin_path:
            self.enter_back_arc_begin_path(edge)
    def exit_tree_arc(self, begin_path, edge):
        # exit_back_arc->multiedges_case->cause enter_edge be replaced
        # self.E.append(edge)
        t = self.tree.edge2end(edge)
        edge = self.v2enter_edge[t]
        self.E.append(edge)

        # edge = (v, w)
        # v, w = a2, r2 ?
        # v, w = b1, r1 ?
        self.middle_case()
        self.subtree_case()
        if begin_path:
            # since v is min possible a2 for current path it starts
            # each possible (a2,b2) pair yielded from tree v that
            # not yet generate type2 component will never have a chance.
            self.T.pop()

        # a right subtree generate a tri (h, max_a2, possible_b2)
        # a left subtree may have a back edge go to
        # middle (max_a2 : possible_b2) that is v.
        # this tri will be merged with tri of that left subtree
        # since left tri included right one, simply discard it.
        T = self.T[-1]
        v, w = self.edges[edge]
        while T:
            h, max_a2_depth, possible_b2 = T[-1]
            if max_a2_depth != self.v2depth[v] and possible_b2 != v and \
                self.max_back_edge_from_to(v) > h:
                T.pop()
            else:
                break
        
        
    def exit_back_arc(self, begin_path, edge):
        self.E.append(edge)
        self.multiedges_case()
        if begin_path:
            self.T.pop()

    def multiedges_case(self):
        # remove all same edges on self.E
        self.multi_back_edges2Pnodes()
        self.multi_tree_edge2Pnode()

    def multi_tree_edge2Pnode(self):
        # if self.E = [...v~>w] and w->v
        edge = self.E[-1]
        assert not self.is_tree_arc[edge] # back edge
        
        v, w = self.edges[edge]
        if w == self.parent[v]:
            # v~>w : curr edge
            # w->v : tree arc
            self.E.pop()
            wv_remain = self.v2enter_edge[v]
            assert self.is_tree_arc[wv_remain]
            new_wv = self.make_P_node(wv_remain, edge)
            self.make_tree_edge(new_wv)
            #print('multiedges_case', new_wv, self.edges[new_wv])

    def multi_back_edges2Pnodes(self):
        # if self.E = [...v~>w, v~>w]
        E = self.E
        back_edge = E.pop()
        assert not self.is_tree_arc[back_edge] # back edge
        vw = self.edges[back_edge]
        while E:
            same_edge = E[-1]
            if vw == self.edges[same_edge]:
                E.pop()
                back_edge = self.make_P_node(back_edge, same_edge)
            else:
                break
        E.append(back_edge)
            
        
        
    def middle_case(self):
        edge = self.E[-1]
        v, w = self.edges[edge]
        # v = a2 ?

        # 0-+-> a2 -> r2 -+[0]-> b2

        # a2 != 0
        if v == 0:
            return

        T = self.T[-1]
        E = self.E
        v2depth = self.v2depth
        parent = self.parent
        old_v = v
        while True:
            edge = self.E[-1]
            v, w = self.edges[edge]
            assert v == old_v
            
            while T:
                h, max_a2_depth, possible_b2 = T[-1]
                # a2 > r2 >= parent(b2)
                if max_a2_depth == v2depth[v] == v2depth[parent[possible_b2]]:
                    # since max_a2 == v and exiting v
                    # we can't reduce max_a2 now.
                    T.pop()
                else:
                    break

            # the T stack doesn't contain all possible split pairs
            # because it requites at least one subtree of b2
            # or a back-edge from b2 to determine the max possible a2
            # but any ancestors of b2, as far as there no back-edges
            # comein from tree b2, they all possible a2 except
            # parent and those whose non-first children' lowpt1
            # less than this ancestors range.
            # the right part of this range will move out
            # and left a straight line. that is nodes of degree 2.
            if self.deg(w) == 2 and self.is_only_childedge_tree_arc(w):
                edge_vw = E[-1]
                edge_wx = E[-2]
                assert (v, w) == self.edges[edge_vw]
                _w, x = self.edges[edge_wx]
                assert w == _w
                h, a2_depth, b2 = x, v2depth[v], x  # make a tri as bellow

            elif not T:
                break
            else:
                h, a2_depth, b2 = T[-1]
                if a2_depth != v2depth[v]: break
                T.pop()

            # now we have found out a (a2, b2) pair, where a2 == v
            #assert v == a2 < b2 <= h
            assert a2_depth == v2depth[v] < v2depth[b2]
            a2 = v
            assert v == a2 < b2 <= h
            
            num_ab = 0
            es = []
            b2a2_ls = []
            between_a2_h = lambda x: a2 <= x and x <= h
            is_b2a2 = lambda e: tuple(self.edges[e]) == (b2, a2)
            while E:
                e = E[-1]
                x, y = self.edges[e]
                if all(map(between_a2_h, (x,y))):
                    E.pop()
                    if is_b2a2(e):
                        # multi-edge may come from Type-1
                        # when we replace a subtree by a back-edge
                        # or this is a multi-graph
                        # note that if this edge is virtual due to Type-1
                        # then it has been pushed before go down from
                        # start edge of path.
                        # all these multiply edges are at last in the class with same lowpt1
                        b2a2 = e
                        b2a2_ls.append(b2a2)
                    else:
                        es.append(e)
                else:
                    break
            C = self.new_component(es)
            a2b2 = self.new_virtual_edge(C, a2, b2)
            for b2a2 in b2a2_ls:
                a2b2 = self.make_P_node(a2b2, b2a2)

            E.append(a2b2)
            self.make_tree_edge(a2b2) # mark is_tree_arc[e] = True
        return

    def subtree_case(self):
        edge = self.E[-1]
        v, w = self.edges[edge]
        # v = b1 ?
        # w = r1 ?

        # lowpt1(r1)=a1, lowpt2(r1)>=b1
        # exists s1, such that s1-+->a1 or a1-+->s1-+->b1
        #                     or a1->s1!=b1 or b1->s1!=r1
        # that is :
        # a1 != 0 or 0-+->s-+->b1 (these two eq: parent(b1)!=0)
        # or 0->b1 and 0->s1 (but this is impossible since biconnected)
        # or 0->b1->s1!=r1

        b1 = v
        r1 = w
        a1_depth = self.v2low_depths[r1][0]

        b1_depth = self.v2depth[b1]
        if not a1_depth < b1_depth or not self.v2low_depths[r1][1] >= b1_depth:
            return
        if self.parent[b1] != 0 or self.num_children[b1] != 1:
            biggest_vtx = self.max_descendants(r1)
            smallest_vtx = r1
            # except a1, b1
            a1_2_x = self.dfs_edges[a1_depth]
            a1 = self.tree.edge2src(a1_2_x)
            E = self.E
            #print('E', E)
            #print('smallest_vtx, biggest_vtx', (smallest_vtx, biggest_vtx))
            es = []
            while E:
                edge = E[-1]
                x, y = self.edges[edge]
                #print('edge = (x,y)', edge, (x,y))
                if smallest_vtx <= x <= biggest_vtx or \
                   smallest_vtx <= y <= biggest_vtx:
                    assert smallest_vtx <= x <= biggest_vtx or \
                           x == a1 or x == b1
                    if not (smallest_vtx <= y <= biggest_vtx or \
                           y == a1 or y == b1):
                        print('smallest_vtx, biggest_vtx', (smallest_vtx, biggest_vtx),
                              'x,y', x,y, '(a1,b1,r1)', (a1,b1,r1))
                        print(self.tree)
                        print(self.g)
                        print('self.v2low_depths', self.v2low_depths)
                        print('self.v2depth', self.v2depth)
                        print('self.v2low_depths[r1][1]', self.v2low_depths[r1][1])
                        print('b1_depth', b1_depth)
                    assert smallest_vtx <= y <= biggest_vtx or \
                           y == a1 or y == b1
                    assert {x,y} != {a1, b1}
                    es.append(edge)
                    E.pop()
                else:
                    break

            if not len(es) > 1:
                print('a1, b1', (a1, b1))
                print('es', es)
                print('E', E)
            assert len(es) > 1

            #print(self.tree)
            C = self.new_component(es)
            b1a1 = self.new_virtual_edge(C, b1, a1)
            E.append(b1a1)
            # will remove all duplicated b1~>a1
            # if a1->b1, then remove b1a1
            self.multiedges_case() 
        return
            
            

                
                
                
                
                
                
                    
            
    def find_split_components(self):
        self.T.append([])
        self.path_search(0)
        self.new_component(self.E)
        self.E = []



makeg = make_mgraph_from_e2undirected_vtc_pairs

def to_vtc_ls(c2type, edges, components):
    return [{x for e in es for x in edges[e]} for es in components]

def test():
    args_ls = [(2,[(0,1)]),
               (4, [(0,1), (0,2), (0,3), (1,2), (3,2)]),
               (4, [(0,1), (0,2), (0,3), (1,2), (3,2), (1,3)]),
               (4, [(0,1), (1,2), (0,3), (3,2)]),
               (4, [(0,1), (0,1), (0,1), (1,2), (0,3), (3,2)]*4),
               (5, [(0,1), (0,2), (1,2), (0,3), (3,1), (2,4), (3,4)]),
               (6, [(0,1), (0,2), (1,2), (0,3), (3,1), (2,4), (3,4), (2,5), (3,5)]),
               (6, [(0,1), (0,2), (1,2), (0,3), (3,1), (2,4), (3,4), (2,5), (3,5), (4,5)]),
               ]
    for i, (n, es) in enumerate(args_ls):
        #if i != 3: continue
        g = makeg(n, es)
        if i<0 and i == 3:
            assert all(set(uv) != {0, 2} for uv in g.e2vtc)
            roots, tree, e2e = connected_undirected_mgraph2directed_palm_tree(g, g.DFS())
            
            assert all(set(uv) != {0, 2} for uv in tree.e2vtc)
        r =  SPQR(g)
        print(r)
        print(to_vtc_ls(*r))

if __name__ == '__main__':
    test()



    
