


from .simple_undirected_graph import graph
from .graph_format_ascii_embedding import str2embedding
from .show_v2neighbors import v2neighbors_to_networkx_graph

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math

graph_format_ascii_embedding_strs = [\
        '4 bcd,adc,abd,acb',\
        '6 bcd,aef,afd,ace,bdf,bec',\
        '8 bcd,aef,afg,agh,bhf,bec,chd,dge',\
        '8 bcd,aef,afg,age,bdh,bhc,chd,egf',\
        '10 bcd,aef,afg,ahi,bjf,bec,cjh,dgi,dhj,eig',\
        '10 bcd,aef,afd,acg,bhi,bic,djh,egj,ejf,gih',\
        '10 bcd,aef,agd,ach,bif,beg,cfj,dji,ehj,gih',\
        '10 bcd,aef,afg,agh,bhi,bic,cjd,dje,ejf,gih',\
        '10 bcd,aef,agh,ahe,bdi,bjg,cfj,cid,ehj,fig',\
        '12 bcd,aef,afd,acg,bhi,bjc,djk,ekl,elj,fig,glh,hki',\
        '12 bcd,aef,agh,aij,bkl,blg,cfl,cki,dhj,dik,ejh,egf',\
        '12 bcd,aef,afg,ahi,bjf,bec,ckl,dli,dhj,eik,gjl,gkh',\
        '12 bcd,aef,afg,agh,bij,bjc,chd,dgk,ekl,elf,hli,ikj',\
        '12 bcd,aef,afg,agh,bij,bjc,ckd,dki,ehl,elf,glh,ikj',\
        '12 bcd,aef,agd,ach,bif,bej,cjk,dli,ehl,fkg,gjl,hki',\
        '12 bcd,aef,agd,ach,bij,bjg,cfk,dki,ehl,elf,glh,ikj',\
        '12 bcd,aef,agh,ahe,bdi,bjk,ckl,cid,ehj,fil,flg,gkj',\
        '12 bcd,aef,agh,ahe,bdi,bjg,cfj,ckd,ekl,flg,hli,ikj',\
        '12 bcd,aef,agh,aie,bdj,bkg,cfk,cli,dhl,elk,fjg,hji',\
        '12 bcd,aef,agh,aij,bjk,blg,cfl,cki,dhj,die,ehl,fkg',\
        '12 bcd,aef,agh,aie,bdj,bjg,cfk,cki,dhl,elf,glh,ikj',\
        '14 bcd,aef,agd,ach,bij,bjk,ckh,dgl,emn,enf,flg,hkm,iln,imj',\
        '14 bcd,aef,agd,ach,bij,bjg,cfh,dgk,ekl,emf,hni,inm,jln,kml',\
        '14 bcd,aef,agd,ach,bij,bjg,cfh,dgk,elm,enf,hnl,ikm,iln,jmk',\
        '14 bcd,aef,agd,ach,bij,bkg,cfh,dgl,emn,enk,fjl,hkm,iln,imj',\
        '14 bcd,aef,agd,ach,bif,bej,cjk,dlm,enj,fig,gnl,hkm,hln,imk',\
        '14 bcd,aef,agh,aij,bkl,bmn,cnl,cki,dhj,dik,ejh,egm,fln,fmg',\
        '14 bcd,aef,agd,ach,bif,bej,cjk,dkl,emn,fng,glh,hkm,iln,imj',\
        '14 bcd,aef,agd,ach,bij,bjg,cfk,dkl,emj,eif,gnh,hnm,iln,kml',\
        '14 bcd,aef,afg,ahi,bjf,bec,ckl,dli,dhj,eim,gmn,gnh,jnk,kml',\
        '14 bcd,aef,agh,aij,bkf,beg,cfh,cgl,dmj,dik,ejn,hnm,iln,kml',\
        '14 bcd,aef,afg,ahi,bjk,bkc,clm,dmi,dhn,enk,ejf,gnm,glh,ilj',\
        '14 bcd,aec,abf,afg,bhi,cjd,dkl,eli,ehm,fmn,gnl,gkh,inj,jmk',\
        '14 bcd,aef,afg,agh,bij,bjc,ckd,dkl,emn,enf,glh,hkm,iln,imj',\
        '14 bcd,aef,afg,agh,bij,bjc,ckd,dkl,elm,emf,gnh,hni,inj,kml',\
        '14 bcd,aef,agd,ach,bij,bjg,cfk,dkl,elm,emf,gnh,hni,inj,kml',\
        '14 bcd,aef,afg,ahi,bjk,bgc,cfl,dlm,dmj,ein,enl,gkh,hni,jmk',\
        '14 bcd,aec,abf,agh,bij,cjk,dkh,dgl,elm,emf,fng,hni,inj,kml',\
        '14 bcd,aef,agh,aij,bkf,beg,cfl,cmi,dhj,din,enl,gkm,hln,jmk',\
        '14 bcd,aef,afg,agh,bij,bkc,cld,dmi,ehj,eik,fjn,gnm,hln,kml',\
        '14 bcd,aef,afg,agh,bij,bkc,cld,dli,ehj,eim,fmn,gnh,jnk,kml',\
        '14 bcd,aef,agh,aij,bkl,bmg,cfh,cgi,dhn,dnk,ejl,ekm,fln,imj',\
        '14 bcd,aef,afg,agh,bij,bkc,cld,dmi,ehn,enk,fjl,gkm,hln,imj',\
        '14 bcd,aef,agh,ahe,bdi,bjk,clm,cid,ehj,fin,fnl,gkm,gln,jmk',\
        '14 bcd,aef,agh,aie,bdj,bkl,cmh,cgi,dhj,eik,fjn,fnm,gln,kml',\
        '14 bcd,aef,agh,ahe,bdi,bjk,clm,cid,ehn,fnk,fjl,gkm,gln,imj',\
        '14 bcd,aef,agh,ahe,bdi,bjk,ckl,cid,ehm,fmn,fng,gnm,ilj,jlk',\
        '14 bcd,aef,agh,ahe,bdi,bjg,cfk,cld,elm,fmk,gjn,hni,inj,kml',\
        '14 bcd,aef,agh,aie,bdj,bkg,cfk,clm,dmn,elk,fjg,hjn,hni,iml',\
        '14 bcd,aef,agh,aie,bdj,bkl,clh,cgm,dmn,enk,fjl,fkg,hni,imj',\
        '14 bcd,aef,agh,aij,bjk,blg,cfl,cmi,dhm,dke,ejn,fng,hni,kml',\
        '14 bcd,aef,agh,aij,bkl,bmg,cfh,cgi,dhm,dnk,ejl,ekn,fni,jml',\
        '14 bcd,aef,agh,aij,bjf,bek,ckl,cmi,dhm,dne,flg,gkn,hni,jml',\
        '14 bcd,aef,agh,aie,bdj,bjg,cfk,cli,dhm,emf,gnl,hkn,inj,kml',\
        '14 bcd,aef,agh,aie,bdj,bkg,cfl,cmi,dhn,enk,fjl,gkm,hln,imj',\
        '20 bcd,aef,agh,aij,bjk,blg,cfm,cni,dho,dpe,eql,fkr,grn,hms,isp,joq,kpt,ltm,nto,qsr',
        ]

def get_planar_embeddings():
    for string in graph_format_ascii_embedding_strs:
        embedding = str2embedding(string)
        yield embedding



def graph_format_ascii_embedding_str2networkx_graph(graph_format_ascii_embedding_str):

    string = graph_format_ascii_embedding_str
    embedding = str2embedding(string)
##    g = graph(embedding)
##    n = g.order()
##    edges = g.edges()
    g = v2neighbors_to_networkx_graph(embedding)
    return g


def show_graph_format_ascii_embedding_by_networkx(graph_format_ascii_embedding_str):

    g = graph_format_ascii_embedding_str2networkx_graph(graph_format_ascii_embedding_str)
    nx.draw(g)
    plt.show()





def show_triconnected_cubic_graph_in_3D(graph_format_ascii_embedding_str):
    gx = graph_format_ascii_embedding_str2networkx_graph(graph_format_ascii_embedding_str)
    n = gx.order()
    assert n >= 4

    source = 0
    target2distance = single_source_shortest_distances(gx, source)
    target2parent = one_single_source_shortest_path_target2parent(gx, source)
    
    max_distance = max(target2distance.values())
    distance2targets = [[] for _ in range(max_distance+1)]
    for target, distance in target2distance.items():
        distance2targets[distance].append(target)
    assert all(len(vs) >= 3 for vs in distance2targets[1:-1])
    pos = nx.drawing.spring_layout(gx, dim=3)
##    nx.draw(gx, pos=pos)
##    plt.show()
##    return
    def draw_edges(v2xyz, edges):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        for u,v in edges:
            x,y,z = (np.linspace(ux, vx, 100) for ux, vx in zip(v2xyz[u], v2xyz[v]))
            ax.plot(x, y, z)
        
        plt.show()
    
    v2xyz = [tuple(pos[i]) for i in range(len(pos))]
    draw_edges(v2xyz, gx.edges())
    return

    x = [x for x,y,z in xyz]
    y = [y for x,y in xyz]
    m = max(max(x)-min(x), max(y)-min(y))
    
    

    string = graph_format_ascii_embedding_str
    embedding = str2embedding(string)
    g = graph(embedding) # to preserve orienation
    v2angle = [None] * n
    v2angle[source] = 0
    first_layer_angle = 0
    
    for v in g.neighbors(source):
        v2angle[v] = first_layer_angle
        first_layer_angle += 120

    parent2children = [[c for c in g.neighbors(p)
                        if target2distance[p] < target2distance[c]
                        ]
                       for p in g.vertices()]

    parents_who_have_2_children = [p for p in g.vertices() if len(parent2children[p]) == 2]
    for p in parents_who_have_2_children:
        pp = target2parent[p]
        pp_loc = g.neighbors(p).index(pp)
        if pp_loc == 1:
            children = parent2children[p]
            children.reverse()

    def middle(angle1, angle2):
        assert 0 <= angle1 < 360
        assert 0 <= angle2 < 360
        d = angle2 - angle1
        if abs(d) == 180:
            print(angle1, angle2)
            print(parent2children)
        assert abs(d) != 180
        if abs(d) > 180:
            d += 360
        return (angle1 + d/2)%360

    v2left_bound = [None] * n
    v2right_bound = [None] * n
    def fill_bound(level):
        vs = distance2targets[level]
        L = len(vs)
        print(vs)
        for loc, v in enumerate(vs):
            left = loc - 1
            right = loc - (L-1)
            left = vs[left]
            right = vs[right]
            print(v2angle[left], v2angle[v], v2angle[right])
            v2left_bound[v] = middle(v2angle[left], v2angle[v])
            v2right_bound[v] = middle(v2angle[v], v2angle[right])
            print(v2left_bound[v], v2angle[v], v2right_bound[v])
        
        return

    def adjust(level):
        # no detal(angle) > 120
        vs = distance2targets[level]
        L = len(vs)
        if not L >= 3:
            print(distance2targets)
            print(L)
            print(vs)
        assert L >= 3
        if L == 3:
            a, b, c = vs
            angle_a = v2angle[a]
            for i, v in enumerate(vs):
                v2angle[v] = (angle_a + i*120) % 360
        else:
            for u, v in zip(vs, vs[1:]+[vs[0]]):
                d = (v2angle[v] - v2angle[u]) % 360
                assert d < 180
                if d > 120:
                    dd = (d-90)/2
                    v2angle[u] += dd
                    v2angle[v] -= dd
                    v2angle[u] %= 360
                    v2angle[v] %= 360
            for u, v in zip(vs, vs[1:]+[vs[0]]):
                d = (v2angle[v] - v2angle[u]) % 360
                assert d <= 120

            
        
    for level in range(1, len(distance2targets)-1):
        adjust(level)
        fill_bound(level)
        for parent in distance2targets[level]:
            children = parent2children[parent]
            for i, child in enumerate(children):
                parents = [v for v in g.neighbors(child)
                           if level == target2distance[v]]
                assert 1 <= len(parents) <= 3
                
                if len(parents) == 2:
                    p1, p2 = parents
                    v2angle[child] = middle(v2angle[p1], v2angle[p2])
                elif len(parents) == 3:
                    v2angle[child] = 0
                elif len(children) == 2:
                    left_bound = v2left_bound[parent]
                    right_bound = v2right_bound[parent]
                    bound = [left_bound, right_bound][i]
                    v2angle[child] = middle(bound, v2angle[parent])
                else:
                    v2angle[child] = v2angle[parent]
                
                    
    num_layers = len(distance2targets)
    if len(distance2targets[-1]) > 1:
        num_layers += 1

    z = np.linspace(-1, 1, num_layers)
    r = (1 - z**2)**.5
    v2xyz = [None]*n
    for Z, R, vs in zip(z, r, distance2targets):
        for v in vs:
            angle = v2angle[v]*np.pi*2/360
            X = R * math.cos(angle)
            Y = R * math.sin(angle)
            v2xyz[v] = X,Y,Z


    draw_edges(v2xyz, g.edges())
    assert 3*n//2 == len(g.edges())
            



def one_single_source_shortest_path_target2parent(G, source, weight=None):
    target2path = nx.shortest_path(G, source, weight=weight)
    target2parent = {target:path[-2]
                     for target, path in target2path.items()
                     if target != source}
    return target2parent
def one_single_source_shortest_path_tree(G, source, weight=None):
    target2parent = one_single_source_shortest_path_target2parent(G, source, weight)
    edges = target2parent.items()
    g = nx.Graph()
    g.add_nodes_from(g.nodes())
    g.add_edges_from(edges)
    return g
def single_source_shortest_distances(G, source, weight=None):
    target2path = nx.shortest_path(G, source, weight=weight)
    assert len(target2path) == G.order()
    target2len_path = {target:len(path) for target, path in target2path.items()}
    target_len_ls = [(target, len(path)) for target, path in target2path.items()]
    target_len_ls.sort(key=lambda e: e[1])

    def get_weight(u, v):
        if weight == None:
            if not G.has_edge(u,v):
                raise ValueError('not has edge')
            return 1
        w = weight.get((u,v))
        if w == None:
            return weight.get((v,u))

    def path2distance(path):
        return sum(get_weight(u,v) for u,v in zip(path, path[1:]))
                   
    target2distance = {}
    for target, _ in target_len_ls:
        target2distance[target] = path2distance(target2path[target])
        
    
    assert len(target2distance) == G.order()
    return target2distance


def _test(begin=None, end=None, step=None):
    for embedding_str in graph_format_ascii_embedding_strs[begin:end:step]:
        show_triconnected_cubic_graph_in_3D(embedding_str)


def main(args=None):
    import argparse

    parser = argparse.ArgumentParser(description='show graphs')
    parser.add_argument('begin', type=int, nargs='?', default=None,
                       help='show graphs[begin:end:step]')
    parser.add_argument('end', type=int, nargs='?', default=None,
                       help='show graphs[begin:end:step]')
    parser.add_argument('step', type=int, nargs='?', default=None,
                       help='show graphs[begin:end:step]')


    args = parser.parse_args()
    _test(args.begin, args.end, args.step)

if __name__ == '__main__':
    main()
























