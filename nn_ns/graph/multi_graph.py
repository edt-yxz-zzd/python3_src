'''
how to represent an edge?

let end vertex: (vertex label, oriented place)

edge label: to distinguist from multi-edges
incident end vertices: ((u, i), (v, j)) s.t.
                            (u,i)<(v,j) if undirected else (u,i)->(v,j)
                            g[u][i] and g[v][j] point to this edge

directed: 0: undirected; +1: directed
io(u,i): +1: outgoing(same) if ends[0] == (u,i); -1: income(reversed) # even for undirected


////////////////////// like this:
edge_label in range(1, num_edges + 1)
edge_label2edge_ends = [None, ...list of incident end vertices...]
edge_label2directed = [None, ...list of boolean...]

dedge_label = io * edge_label
'''


import collections
import itertools
from sand import k_min_different_elements
from .automap import inv_automap, item_map, mx_map, rows_map


MultiGraphBase = collections.namedtuple(
    'MultiGraphBase',
    'e2info adj_ls e2is_directed e2vtc '\
    'v2outgoings v2incomings de2outgoing_loc de2incoming_loc '\
    'incoming_end2next_outgoing_end '\
    'outgoing_end2next_incoming_end '\
    'NOT_VTX NOT_EDGE'.split())


__all__ = ('inv_automap, item_map, mx_map, rows_map, '
           'multi_graph, make_mgraph, dfs_ordering, find_lowpt_k, '
           'connected_undirected_mgraph2directed_palm_tree, '
           'palm_tree2tree_info, '
           'BLACK, GREY, WHITE, '
           'enter_edge, back_edge, dead_edge, exit_edge, '
           'enter_root, exit_root, loop_edge'.split(', '))



class multi_graph(MultiGraphBase):
    __slots__ = ()
    #def __init__(self):pass
##    def __new__(cls, n, directed_N_vtx_loc_pair_ls):
##        edges, adj_ls, e2is_directed, e2vtc = \
##              make_mgraph_args(n, directed_N_vtx_loc_pair_ls)
##        self = super(multi_graph, cls).\
##               __new__(cls, edges, adj_ls, e2is_directed, e2vtc)
##        return self
    def nv(self):
        return len(self.adj_ls)
    __len__ = order = num_vertices = nv
    def ne(self):
        return len(self.e2info)
    num_edges = ne
    
    def vertices(self):
        return range(self.nv())
    def edges(self):
        return range(self.ne())
    
    
    def vtx2incident_edges(self, v):
        return self.adj_ls[v]
    def num_outgoings(self, v):
        return len(self.outgoings(v))
    def outgoings(self, v):
        return self.v2outgoings[v]
    def is_outgoing(self, e):
        return e >= 0 or not self.is_directed(e)
    def is_incoming(self, e):
        return e < 0 or not self.is_directed(e)
    def incomings(self, v):
        return self.v2incomings[v]
    def num_incomings(self, v):
        return len(self.incomings(v))
    
    def is_directed(self, e):
        return self.e2is_directed[self.normal(e)]
    def is_loop(self, e):
        s,t = self.edge2ends(e)
        return s == t

    def num_edges(self, v=None):
        if v == None:
            return self.ne()
        return self.num_edge_ends(v)
    def num_edge_ends(self, v):
        return len(self.adj_ls[v])
    
    @classmethod
    def normal(self, e):
        s, e = self.e2sign_normal(e)
        return e

    @classmethod
    def flip(self, e):
        return -e-1
    @classmethod
    def is_normal(self, e):
        return e >= 0
    @classmethod
    def e2sign_normal(self, e):
        s = 1
        if e < 0:
            e = self.flip(e)
            s = -1
        return s, e
    
    def next_edge(self, e):
        (v, vloc), (u, uloc) = self.edge2locs(e)
        uloc += 1
        uloc %= len(self.adj_ls[u])
        return adj_ls[u][uloc]
    
    def prev_edge(self, e):
        (v, vloc), (u, uloc) = self.edge2locs(e)
        vloc -= 1
        vloc %= len(self.adj_ls[v])
        return adj_ls[v][vloc]


    # dedge is a normal or not-normal edge
    # each dedge can be decoded to a (src->end) pair
    # if a normal edge is (src->end),
    # then the not-normal one is (src'->end')==(end->src)
    #
    # dedge with IO property : incoming/outgoing
    # IO means what direction dedge enter or leaving it's src
    # if dedge is directed
    # then normal dedge should come with outgoing
    #      and not-normal dedge with incoming
    # if undirected
    # then both are ok
    #
    # (nde, outgoing)->(nnde, incoming) real direction of de
    # (nue, outgoing)->(nnue, incoming) assumed direction of ue
    # (nue, incoming)<-(nnue, outgoing) reversed direction of ue
    #
    def incoming2next_outgoing(self, e):
        # if e is normal and directed: error
        # e is assigned with a direction
        # let e : u -> v
        # u is the current vertex
        # e is an incoming edge of u
        # may be None
        assert self.is_incoming(e)
        return self.incoming_end2next_outgoing_end[e]
    def outgoing2next_incoming(self, e):
        # may be None
        assert self.is_outgoing(e)
        return self.outgoing_end2next_incoming_end[e]
    def incoming2next_incoming(self, e):
        # may be None
        assert self.is_incoming(e)
        v, vloc = self.de2incoming_loc[e]
        next_vloc = (vloc+1) % self.num_incomings(v)
        if next_vloc == vloc:
            return None
        return self.v2incomings[v][next_vloc]
    def outgoing2next_outgoing(self, e):
        # may be None
        assert self.is_outgoing(e)
        v, vloc = self.de2outgoing_loc[e]
        next_vloc = (vloc+1) % self.num_outgoings(v)
        if next_vloc == vloc:
            return None
        return self.v2outgoings[v][next_vloc]
    
    def next_outgoing(self, e, from_src=False):
        f = self.outgoing2next_outgoing
        if not from_src:
            f = self.incoming2next_outgoing
            e = self.flip(e)
        return f(e)
    
    def outgoings_from(self, e, from_src=False):
        if not from_src:
            e = self.next_outgoing(e, from_src)
        if e == None:
            return iter(())

        v, vloc = self.de2outgoing_loc[e]
        outs = self.v2outgoings[v]
        return itertools.chain(outs[vloc:], outs[:vloc])
    
    
        
        
    def edge2end(self, e):
        s, t = self.edge2ends(e)
        return t
    def edge2src(self, e):
        s, t = self.edge2ends(e)
        return s
    def edge2ends(self, e):
        s, e = self.e2sign_normal(e)
        uv = self.e2vtc[e]
        return self.sorted_with_sign(s, uv)

    def sorted_with_sign(self, s, pair):
        if s == -1:
            return tuple(reversed(pair))
        return pair
    def edge2locs(self, e):
        s, e = self.e2sign_normal(e)
        d, locs = self.e2info[e]
        return self.sorted_with_sign(s, locs)

    def relabel_vertices(self, old_vtx2new_vtx, new_vtx2old_vtx=None):
        # edge number keep the same, but the undirected edges may be reversed.
        e2info = ((d, ((old_vtx2new_vtx[v], vloc) for v, vloc in pair))
                  for d, pair in self.e2info)
        n = self.nv()
        g = make_mgraph(n, e2info, **self.get_keyword_args())
        new_edge2old_edge = tuple((self.flip(new_e)
                                       if not self.is_directed(new_e) and \
                                          g.edge2ends(new_e) != \
                                          tuple(old_vtx2new_vtx[v]
                                                for old_v in self.edge2ends(new_e))
                                       else new_e)
                                  for new_e in g.edges())
        old_edge2new_edge = new_edge2old_edge
        return g, new_edge2old_edge, old_edge2new_edge

    def get_keyword_args(self):
        return dict(NOT_VTX=self.NOT_VTX, NOT_EDGE=self.NOT_EDGE)
    def reposition_edges(self, v2incident_dedges):
        edge2is_directed = self.e2is_directed
        g = make_mgraph_from_v2incident_dedges_N_is_directed(
            v2incident_dedges, edge2is_directed, **self.get_keyword_args())
        return g

    def vertex_map(self, value=None, *, value_factory=None):
        # return buf[vtx] = value_factory(vtx) or value
        if value_factory == None:
            value_factory=lambda vtx: value
        return [value_factory(vtx) for vtx in self.vertices()]
    def edge_map(self, value=None, *, value_factory=None):
        # return buf[normal_edge] = value_factory(normal_edge) or value
        if value_factory == None:
            value_factory=lambda normal_edge: value
        return [value_factory(edge) for edge in self.edges()]
    def DFS(self, *,
            start_vtc_or_edges=None,
            vertex_iter=None,
            edge_iter=None,
            edge2ends=None,
            colormap=None
            ):

        def f_edge_iter(G, v, *, start_edge=None, comein_edge=None):
            if start_edge != None:
                assert v == G.edge2end(G.flip(start_edge))
                return G.outgoings_from(start_edge, from_src=True)
            elif comein_edge != None:
                assert v == G.edge2end(comein_edge)
                return G.outgoings_from(comein_edge, from_src=False)
            else:
                return G.outgoings(v)
        if colormap == None:
            colormap = self.vertex_map(value=BLACK)
        if vertex_iter == None:
            vertex_iter = multi_graph.vertices
        if edge_iter == None:
            edge_iter = f_edge_iter
        if edge2ends == None:
            edge2ends = multi_graph.edge2ends
        return mgraph_DFS(self, start_vtc_or_edges,
                          vertex_iter, edge_iter,
                          edge2ends, colormap)
    
        
        
            
    
def _check_vtx(n, v):
    if not 0 <= v < n:
        raise ValueError('vertex should be in range(n)')
def _check_vtc(n, vtc):
    _check = lambda v: _check_vtx(n, v)
    list(map(_check, vtc))
    
        
def make_mgraph(n, directed_N_vtx_loc_pair_ls, *, NOT_VTX=None, NOT_EDGE=None):
    args = make_mgraph_args(n, directed_N_vtx_loc_pair_ls)
    g = multi_graph(*args, NOT_VTX=NOT_VTX, NOT_EDGE=NOT_EDGE)
    return g


def make_mgraph_from_e2undirected_vtc_pairs(n, e2undirected_vtc_pairs, **kw):
    n, es = make_mgraph_args_from_e2undirected_vtc_pairs(
        n, e2undirected_vtc_pairs)
    return make_mgraph(n, es, **kw)

def make_mgraph_from_v2neighbors(v2neighbors, **kw):
    n, es = make_mgraph_args_from_multi_directed_v2neighbors(v2neighbors)
    return make_mgraph(n, es, **kw)

def make_mgraph_from_v2incident_dedges_N_is_directed(
    v2incident_dedges, edge2is_directed, **kw):
    n, es = make_mgraph_args_from_v2incident_dedges_N_is_directed(
        v2incident_dedges, edge2is_directed)
    return make_mgraph(n, es, **kw)

def make_mgraph_from_simple_graph(simple_graph, **kw):
    sg = simple_graph
    n, es = make_mgraph_args_from_simple_graph(simple_graph)
    mg = make_mgraph(n, es, **kw)
    assert all(mg.edge2ends(uedge) == sg.dedge2edge(uedge)
               for uedge in sg.uedges())
    return mg


    
def make_mgraph_args_from_multi_directed_v2neighbors(v2neighbors):
    # multi-directed graph

    v2income_idx = [len(ns) for ns in v2neighbors]
    es = []
    d = True
    n = len(v2neighbors)
    for v, ns in enumerate(v2neighbors):
        for loc, u in enumerate(ns):
            if not 0 <= u < n:
                raise ValueError('u not in range(order(G))')
            es.append((d, ((v, loc), (u, v2income_idx[u]))))
            v2income_idx[u] += 1
    return n, es

def make_mgraph_args_from_directed_v2incident_outgoings(v2incident_outgoings):
    raise error
    n = len(v2incident_dedges)
    ne = sum(len(es) for es in v2incident_outgoings)
    g = multi_graph
    if any(not g.is_normal(e) for es in v2incident_outgoings for e in es):
        raise ValueError('not outgoing edge which should be normal edge if directed')

    v2outs = [[] for _ in range(n)]
    for es in v2incident_outgoings:
        for e in es:
            
            v2outs[xxxx]

def make_mgraph_args_from_v2incident_dedges_N_is_directed(v2incident_dedges, edge2is_directed):
    n = len(v2incident_dedges)
    ne = len(edge2is_directed)
    g = multi_graph
    e2locs = [[None, None] for _ in range(ne)]
    for v, dedges in enumerate(v2incident_dedges):
        for vloc, de in enumerate(dedges):
            ne = g.normal(de)
            locs = e2locs[ne]
            idx = 1 - g.is_normal(de)
            if locs[idx] != None:
                raise ValueError('incident_dedges at same position')
            locs[idx] = (v, vloc)

    if any(loc == None for locs in e2locs for loc in locs):
        raise ValueError('some ends of incident_dedges do not present')

    e2info = zip(edge2is_directed, e2locs)
    return n, e2info


def make_mgraph_args_from_e2undirected_vtc_pairs(
    n, e2undirected_vtc_pairs):
    v2last_loc = [0]*n

    def require_loc(u):
        uloc = v2last_loc[u]
        v2last_loc[u] += 1
        return u, uloc
        
    def uv2locs(uv):
        u, v = uv
        _check_vtc(n, uv)
        return tuple(map(require_loc, uv))

    directed = False
    e2info = tuple((directed, uv2locs(uv)) for uv in e2undirected_vtc_pairs)
    return n, e2info



def make_mgraph_args_from_simple_graph(simple_graph):
    sg = simple_graph
    n = sg.nv()
    is_directed = False
    e2info = tuple((is_directed,
                    tuple((v, loc) for v, loc in
                          zip(sg.dedge2edge(uedge),
                              sg.where_dedge(uedge))
                          )
                    )
                   for uedge in sg.uedges()
                   )
    return n, e2info

def make_mgraph_args(n, directed_N_vtx_loc_pair_ls):
    flip = lambda e: -e-1
    is_normal = lambda e: e >= 0
    normal = lambda e: e if is_normal(e) else flip(e)

    
    edges = tuple((bool(d), tuple((v, loc) for v, loc in
                                  (pair if d else sorted(pair))))
                   for d, pair in directed_N_vtx_loc_pair_ls)
                  
    if not all(0 <= x < n for d, ((v, vl), (u, ul)) in edges for x in [v, u]):
        raise ValueError('vetex not in range(n)')
    v2num_neighbors = [0]*n
    for d, ((v, vl), (u, ul)) in edges:
        v2num_neighbors[v] += 1
        v2num_neighbors[u] += 1

    
    adj_ls = [[None]*m for m in v2num_neighbors]
    for e, (d, pair) in enumerate(edges):
        for i, (x, loc) in enumerate(pair):
            if not 0 <= loc < len(adj_ls[x]):
                raise ValueError('vertex location should in range(m) for some m')
            if not adj_ls[x][loc] == None:
                raise ValueError('vertex location duplicated!')

            adj_ls[x][loc] = e if i == 0 else flip(e)
    if any(e == None for es in adj_ls for e in es):
        raise logic - error - Exception('logic error')

    adj_ls = tuple(tuple(es) for es in adj_ls)
    e2is_directed = tuple(d for d,_ in edges)
    e2vtc = tuple(tuple(v for v,_ in pair) for _, pair in edges)
    #return edges, adj_ls, e2is_directed, e2vtc


    is_undirected_edge = lambda e: not e2is_directed[normal(e)]
    is_outgoing = lambda e: is_normal(e) or is_undirected_edge(e)
    is_incoming = lambda e: not is_normal(e) or is_undirected_edge(e)
    v2outgoings = tuple(tuple(e for e in es if is_outgoing(e))
                        for es in adj_ls)
    v2incomings = tuple(tuple(e for e in es if is_incoming(e))
                        for es in adj_ls)
    #return edges, adj_ls, e2is_directed, e2vtc, v2outgoings, v2incomings

    ne = len(edges)
    de2outgoing_loc = [None]*(2*ne)
    for v, dedges in enumerate(v2outgoings):
        for vloc, de in enumerate(dedges):
            de2outgoing_loc[de] = (v, vloc)
    de2incoming_loc = [None]*(2*ne)
    for v, dedges in enumerate(v2incomings):
        for vloc, de in enumerate(dedges):
            de2incoming_loc[de] = (v, vloc)
    de2outgoing_loc = tuple(de2outgoing_loc)
    de2incoming_loc = tuple(de2incoming_loc)
##    return edges, adj_ls, e2is_directed, e2vtc, \
##           v2outgoings, v2incomings, de2outgoing_loc, de2incoming_loc

    incoming_end2next_outgoing_end = [None]*(2*ne)
    outgoing_end2next_incoming_end = [None]*(2*ne)
    for ends in adj_ls:
        next_incoming = next_outgoing = None
        L = len(ends)
        for i in range(L-1, -1-L, -1):
            end = ends[i]
            if is_incoming(end) and next_outgoing != end:
                incoming_end2next_outgoing_end[end] = next_outgoing
            # not elif !
            if is_outgoing(end) and next_incoming != end:
                outgoing_end2next_incoming_end[end] = next_incoming

            if is_incoming(end):
                next_incoming = end
            # not elif !
            if is_outgoing(end):
                next_outgoing = end

    incoming_end2next_outgoing_end = tuple(incoming_end2next_outgoing_end)
    outgoing_end2next_incoming_end = tuple(outgoing_end2next_incoming_end)
    return edges, adj_ls, e2is_directed, e2vtc, \
           v2outgoings, v2incomings, de2outgoing_loc, de2incoming_loc,\
           incoming_end2next_outgoing_end,\
           outgoing_end2next_incoming_end

            
    

BLACK = 0
GREY = 1
WHITE = 2

'''
dead_edge:
    revisit at back edge for undirected graph
    forword-edge or cross-edge in directed graph
'''

enter_edge = 1
back_edge = 1<<1
dead_edge = 1<<2
exit_edge = 1<<3
enter_root = 1<<4
exit_root = 1<<5
loop_edge = 1<<6

enter_edge = 'enter_edge'
back_edge = 'back_edge'
dead_edge = 'dead_edge'
exit_edge = 'exit_edge'
enter_root = 'enter_root'
exit_root = 'exit_root'
loop_edge = 'loop_edge'

def mgraph_DFS(G, start_vtc_or_edges, vertex_iter, edge_iter, edge2ends, colormap):
    '''dfs for multi-graph

start_vtc_or_edges = [('v', vtx)|('e', edge)] if None using all vertices
vertex_iter(G): yield all vertices
edge_iter(G, v, *, start_edge=None, comein_edge=None): yield all edges of v
edge2ends(G, e): yield the source and target end of edge, begin->end (take care of the order)
colormap[v]=color: can use to store color; list or dict or somewhat
                if alway return BLACK, then treat G as a DAG
                if exists cycle, dead loop...

'''

    edge2end = lambda G,e: edge2ends(G,e)[-1]
    edge2src = lambda G,e: edge2ends(G,e)[0]
    
    edge_stack = []
    edge_iters = []
    if start_vtc_or_edges == None:
        start_vtc_or_edges = zip(itertools.repeat('v'), vertex_iter(G))

    for case, v_e in start_vtc_or_edges:
        assert len(edge_stack) == len(edge_iters) == 0
        
        if case == 'e':
            start_edge = v_e
            root = edge2src(G, start_edge)
        elif case == 'v':
            start_edge = None
            root = v_e
        else:
            raise ValueError('start_vtc_or_edges case should be "v" or "e"')
        if colormap[root] != BLACK:
            continue
        yield enter_root, edge_stack, root
        colormap[root] = GREY
        edge_iters.append(iter(edge_iter(G, root, start_edge=start_edge)))

        def pre_v():
            if not edge_stack:
                raise logic-error - Exception
            elif len(edge_stack) == 1:
                return root
            else:
                e = edge_stack[-2]
                return edge2end(G, e)
            
        while edge_iters:
            assert len(edge_stack) + 1 == len(edge_iters)
            #print(len(edge_stack), len(edge_iters))
            
            for edge in edge_iters[-1]:
                break
            else:
                if not edge_stack:
                    yield exit_root, edge_stack, root
                    colormap[root] = WHITE
                    edge_iters.pop()
                    break
                v = edge2end(G, edge_stack[-1])
                yield exit_edge, edge_stack, v
                colormap[v] = WHITE
                edge_stack.pop()
                edge_iters.pop()
                continue

            edge_stack.append(edge)
            v = edge2end(G, edge)

            assert len(edge_stack) == len(edge_iters)
            if colormap[v] == BLACK:
                case = enter_edge
                yield case, edge_stack, v
                colormap[v] = GREY
                edge_iters.append(edge_iter(G, v, comein_edge=edge))
                
            elif colormap[v] == GREY:
                case = back_edge
                if pre_v() == v:
                    case == loop_edge
                yield case, edge_stack, v
                edge_stack.pop()
            elif colormap[v] == WHITE:
                case = dead_edge
                yield case, edge_stack, v
                edge_stack.pop()
            else:
                raise ValueError('color should be one of BLACK GREY or WHITE')

            
def dfs_ordering(G, DFS):
    n = G.nv()
    prefix_ordering = []
    postfix_ordering = []
    useless_cases = {back_edge, loop_edge, dead_edge}
    for case, edges, v in DFS:
        if case in useless_cases:
            continue
        elif case == enter_edge or case == enter_root:
            prefix_ordering.append(v)
        elif case == exit_edge or case == exit_root:
            postfix_ordering.append(v)
        else:
            raise
    
    assert n == len(prefix_ordering) == len(postfix_ordering)
    return prefix_ordering, postfix_ordering

    
def find_lowpt_k(G, k, *args, **kw_args):
    n = G.nv()
    v2lows = [None]*n
    ordering = []
    old_v2new_label = [G.NOT_VTX]*n
    
    if k < 0:
        k = 0
    for case, edges, v in G.DFS(*args, **kw_args):
        if case == enter_edge or case == enter_root:
            old_v2new_label[v] = len(ordering)
            ordering.append(v)
            v2lows[v] = []
            
        elif case == back_edge or case == loop_edge:
            e = edges[-1]
            u = G.edge2src(e)
            if k:
                v2lows[u].append(old_v2new_label[v])
        elif case == exit_edge or case == exit_root:
            lows = v2lows[v]
            
            if k:
                lows = k_min_different_elements(k, lows) # (degree*k)log(k)
                assert len(lows) <= k
                v2lows[v] = lows
            if edges:
                e = edges[-1]
                parent = G.edge2src(e)
                v2lows[parent].extend(lows)
        elif case == dead_edge:
            raise
        else:
            raise
                
    assert all(len(s) <= k for s in v2lows)

    new_label2old_v = ordering
    for v in range(n):
        lows = sorted(v2lows[v]) # k log k
        new = old_v2new_label[v]
        lows = [min(u, new) for u in lows]
        
        for i in range(len(lows)):
            lows[i] = new_label2old_v[lows[i]]
        while len(lows) < k:
            lows.append(v)
        v2lows[v] = lows
    return v2lows
            
            
        
def connected_undirected_mgraph2directed_palm_tree(G, DFS):
    roots = [] # G may be a empty graph
    es = []           # visited dedges; old_dedges
    normal_es = set() # visited edges; normal_old_edges
    #v2enter_edge = [G.NOT_EDGE] * G.nv()
    #is_tree_arc = [False] * G.ne()
    
    new_edge_cases = frozenset([enter_edge, back_edge, loop_edge, dead_edge])
    for case, edges, v in DFS:
        #print(case, edges, v)
        if case in new_edge_cases:
            e = edges[-1]
            #print(e, G.edge2ends(e))
            ne = G.normal(e)
            if ne in normal_es:
                continue
            es.append(e)
            normal_es.add(ne)
##            if case == enter_edge:
##                # here, ne is the real edge number in palmtree
##                is_tree_arc[ne] = True
##                v2enter_edge[v] = ne
        elif case == enter_root:
            roots.append(v)

    if not len(es) == len(normal_es) == G.ne():
        print(G)
        print(es)
    assert len(es) == len(normal_es) == G.ne()
    new_e2info = [None]*G.ne()
    new_e2old_de = [None]*G.ne()
    for old_de in es:
        info = (True, G.edge2locs(old_de))
        old_ne = G.normal(old_de)
        new_e = old_ne
        new_e2info[new_e] = info
        new_e2old_de[new_e] = old_de

    assert all(info != None for info in new_e2info)
    n = G.nv()
    palm_tree = make_mgraph(n, new_e2info)
    return roots, palm_tree, new_e2old_de

def palm_tree2tree_info(roots, palm_tree):
    G = palm_tree
    v2enter_edge = [G.NOT_EDGE] * G.nv()
    is_tree_arc = [False] * G.ne()
    v2parent = [G.NOT_VTX] * G.nv()
    v2depth = [None]*G.nv()
    v2num_children = [None]*G.nv()
    v2num_out_back_edges = [None]*G.nv()
    v2num_in_back_edges = [None]*G.nv()
    v2num_enter_edges = [None]*G.nv()

    start_vtc = [('v', v) for v in roots]
    for case, edges, v in G.DFS(start_vtc_or_edges=start_vtc):
        if case == enter_edge or case == enter_root:
            v2depth[v] = len(edges)
            v2num_children[v] = 0
            v2num_out_back_edges[v] = 0
            v2num_in_back_edges[v] = 0
            v2num_enter_edges[v] = int(case == enter_edge)
            if case == enter_edge:
                e = edges[-1]
                parent = G.edge2src(e)
                v2num_children[parent] += 1
        elif case == back_edge or case == loop_edge:
            e = edges[-1]
            backfrom, backto = G.edge2ends(e)
            v2num_out_back_edges[backfrom] += 1
            v2num_in_back_edges[backto] += 1
            

        
        if edges:
            e = edges[-1]
            if not G.is_normal(e):
                raise ValueError('not a palm tree or with wrong roots')
            if case == enter_edge:
                is_tree_arc[e] = True
                v2enter_edge[v] = e
                v2parent[v] = G.edge2src(e)
            
    return is_tree_arc, v2enter_edge, v2parent, v2depth, \
           v2num_enter_edges, v2num_children, \
           v2num_out_back_edges, v2num_in_back_edges

def test():
    e = [(0, ((1,0), (0,1))), (1, ((1,1), (0, 0)))]
    print(make_mgraph_args(2, e))



    g = make_mgraph(2, e)
    print(type(g), g)
    for case, es, v in g.DFS():
        print(case, es, v)


    g2 = make_mgraph_from_v2neighbors([[1,3,4], [], [3,4,2,2], [0], [4,4]])
    print(g2)



