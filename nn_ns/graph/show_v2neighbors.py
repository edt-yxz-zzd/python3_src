
import networkx as nx
import matplotlib.pyplot as plt

def v2neighbors_to_networkx_graph(v2neighbors):
    v2neighbors = dict(enumerate(v2neighbors))
    g = nx.Graph(v2neighbors)
    return g
def show_v2neighbors(v2neighbors):
    g = v2neighbors_to_networkx_graph(v2neighbors)
    nx.draw(g)
    plt.show()
