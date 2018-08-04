
import networkx as nx
import matplotlib.pyplot as plt
from math import *


def sqare_modN_circle_rooted_forest(N):
    return [(i**2) % N for i in range(N)]


def to_nxgraph(N):
    ls = sqare_modN_circle_rooted_forest(N)

    g = nx.DiGraph(enumerate(ls))
    return g

def list_ntrees(*rng, **kw):
    d = {}
    for N in range(*rng, **kw):
        g = to_nxgraph(N)
        d[N] = nx.number_weakly_connected_components(g)
    return d


def max_ntrees(*rng, **kw):
    return max(nx.number_weakly_connected_components(to_nxgraph(N)) for N in range(*rng, **kw))


def show_one(N):
    g = to_nxgraph(N)
    gs = nx.weakly_connected_component_subgraphs(g)
    L = len(gs)
    COL = ceil(sqrt(L))
    ROW = (L+COL-1)//COL
    assert (ROW-1)*COL < L <= ROW*COL
    assert ROW <= COL
    for i, tree in enumerate(gs, 1):
        plt.subplot(ROW, COL, i)
        nx.draw_spring(tree, hold=True)
    
    plt.suptitle('N={}'.format(N))
    plt.show()
    return

    ts = 'draw_shell draw_spring draw_spectral draw_circular draw_random'.split()
    for title in ts:
        getattr(nx, title)(g)
        plt.suptitle(title)
        plt.show()

    return

def show(*range_args, **range_kwargs):
    for N in range(*range_args, **range_kwargs):
        show_one(N)



print(max_ntrees(1, 300))

    




















