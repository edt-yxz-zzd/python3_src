import networkx as nx
import planarity

c3 = [\
    'C~',\
    'E{Sw',\
    'Gs@ipo',\
    'GtPHOk',\
    'Is?HGtcU?',\
    'Is@?xOXX?',\
    'It?IQGiDO',\
    'It?IQKWHG',\
    'It?IQOeDO',\
    ]
c2 = [\
    'Gv?IXW',\
    'Is@@WoXX?',\
    'It?GYDKKO',\
    'It?IQScDG',\
    ]

h = nx.parse_graph6(c3[0])


#import functools

basic_sym = ['.', 'o'...]
def is_planar(G):
    G = planarity.planarity_networkx.pgraph_graph(G)
    return planarity.planarity_functions.is_planar(G)
def _get_d2(pt, to, G):
    assert G.has_edge(pt, to)
    old = pt
    ls = []
    while 2 == len(G[to]):
        if to == old: break
        ls.append(to)
        for n in G[to]:
            if n != pt: break
        pt = to
        to = n
    return (ls, to)
def _get_lr_d2(pt, G):
    assert len(G[pt]) == 2
    l, r = G[pt]
    assert l != r
    
    rs, rto = _get_d2(pt, r, G)
    if rto == pt:
        return rs + [pt], ()
    ls, lto = _get_d2(pt, l, G)
    return (ls.reverse()+[pt]+rs, (lto, rto))
def _count_multiedge(s, t, G):
    # G is cccc..H, counts 'c'
    assert G.has_edge(s, t)
    assert len(G[s]) == len(G[t]) == 2
    s_ = {t}
    t_ = {s}
    ls = []
    while G.has_edge(s, t):
        ls.append((s,t))
        sn = set(G[s]) - s_
        tn = set(G[t]) - t_
        if len(sn) == 0:
            assert len(tn) == 0
            # G is 1-1 or cccc...o
            assert len(s) == len(tn) < 3
            return ls, ()
        assert len(sn) == len(tn) == 1
        sn, = sn
        tn, = tn
        s_ = {s, tn}
        t_ = {t, sn}
        s,t = sn,tn

    return ls, (s,t)
        
    
def parsing(G):
    assert len(G) > 0
    assert len(G) % 2 == 0
    # G should be a planar cubic simple graph
    if not is_connected(G):
        raise "not a connected graph"
    if G.number_of_selfloops() > 0:
        raise 'has selfloops'
    for n in G:
        if len(G[n]) != 3:
            raise "not a cubic graph"
    if not is_planar(G):
        raise 'not a planar graph'
        
    c2 = [tuple(set(c)) for c in biconnected_components(G)]
    pt = {n:[None, None] for n in G}
    _c2 = {}
    for c in c2:
        if len(c) == 2:
            a, b = c
            for n,t in zip(c, (b,a)):
                pt[n][1] = t
        else:
            _c2[c] = {'io_pt':[]}
            for n in c:
                pt[n][0] = c
    c2 = _c2
    tri = []
    for n in G:
        if pt[n][0] == None:
            pt[n][0] = (n)
            tri.append(n)
    H = nx.Graph()
    for c in c2:
        for n in c:
            if pt[n][1] != None: # out-degree
                c2[c]['io_pt'].append(n)
                x = pt[n][1]
                if n < x:
                    to = pt[x][0]
                    H.add_edge(c, to, {c:n, to:x})
    for n in tri:
        for x in G[n]:
            if n < x:
                c = pt[n][0]
                to = pt[x][0]
                H.add_edge(c, to, {c:n, to:x})
    # H done!
    



    
    pt2sub = {n:0 for n in c2}
    pts = pt2sub.copy()
    for ns in c2:
        # c2 is 1-1, sun, circle with > 2 point....
        L = len(ns)
        assert L > 1
        #if L > 10: raise 'unknown symbol'
        if L == 1:
            raise 'unknown error'
            n, = ns
            pt2sub[n] = {'nodes': ns, 'char': '.'}
            continue

        # 1-1
        if L == 2:
            for n in ns:
                pts[n] += 1
            continue
        sub = subgraph(G, ns)
        d2 = set(n for n in sub if len(sub[n]) == 2)
        # circle
        if len(d2) == len(sub):
            node_info = {'nodes': ns, 'char': 'o', 'inum': 0, 'onum': 0}
            for n in d2:
                pt2sub[n] = node_info
            continue

        d3 = set(sub.nodes()) - d2
        assert len(d3) >= 2
        # co
        if len(d3) == 2:
            s, t = d3
            s_t = set(sub[s])
            assert t in s_t
            s_t.discard(t)
            sl, sr = s_t
            ls, to = _get_d2(s, sl, sub)
            assert to == t
            rs, to = _get_d2(s, sr, sub)
            assert to == t
            if len(ls) > 2 and len(rs) > 2:
                raise """unknow meaning of 'co'"""
            node_info = {'nodes': ns, 'char': 'co', 'inum': 0, 'LR':{set(ls), set(rs)}}
            for n in d2:
                pt2sub[n] = node_info
            continue

        # len(d3)>2
        ssub = subgraph(sub, d3)
        sd2 = set(n for n in ssub if len(ssub[n]) == 2)
        sL = len(sd2)
        if sL > 4:
            raise 'unknow usage of out_going_spaces '
        if len(ssub) == sL:
            # -o[-o-o...]
            assert sL == 4
            node_info = {'nodes': ns, 'char': 'co', 'inum': 1}
            for n in d2:
                pt2sub[n] = node_info
            continue

        # degree(x) > 2 for some x
        processed = {}
        counts = []
        for n in sd2:
            if n in processed: continue
            ls, lr = _get_lr_d2(n, ssub)
            assert lr != ()
            assert lr[0] != lr[1]
            assert len(ls)%2 == 0
            if len(ls) == 4:
                if ssub.has_edge(*lr):
                    raise """unknow meaning of the symbol"""
                io_edge = {(n for n in ls[:2]):1, (n for n in ls[2:]):1}
                pure = subgraph(ssub, d3-sd2)
                sym = sym_ord(pure)
                node_info = {'nodes': ns, 'char': sym, 'io_edge': io_edge}
                for n in d2:
                    pt2sub[n] = node_info
                continue
            
            assert not 
            
xxxxx


            
            processed |= set(ls) | set(lr)
            counts.append 
            
        if sL == 4:
            #ds = [len(set(G[n])) & sd2) for n in sd2]
            a = sum(ds)
            assert a in {4, 6}
            if a == 4:
                symbol
                _count_multiedge
            
        if sL == 0:
            which_symbol(ssub)
            
        
            
        
        
is_isomorphic
G=nx.Graph()
G.add_edges_from([(1,2),(1,3)])
G.add_node("spam")       # adds node "spam"

import matplotlib.pyplot as plt
nx.draw(h)

plt.show()
