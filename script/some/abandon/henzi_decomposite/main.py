

img = scale(img, (2,2))
img = skeleton(img)
vex2xy, edges = pick_up_graph(img)
n = len(vex2xy)
vex_old2new = reorder_vtc_by_xy(vex2xy)
new_vex2xy = relabel_vex2xy(vex_old2new, vex2xy)
new_edges = relabel_edges(vex_old2new, edges)

g = graph(n, new_edges)
vtc_ls = connected_component(g)
subgraphs = []


