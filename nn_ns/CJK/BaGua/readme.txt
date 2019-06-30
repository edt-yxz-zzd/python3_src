
hanzi_set
hanzi -> (left_part, right_part)


left_part -> left_repr_element
right_part -> right_repr_element
==>>
    left_part -> left_std
    right_part -> right_std
left_std_set /\ right_std_set == {}

left_right_bipartite_graph_edges = {
    (left_std<hanzi>, right_std<hanzi>) for hanzi in hanzi_set
    }
G = left_right_bipartite_graph \/ complete_graph(left_std_set) \/ complete_graph(right_std_set)

min_num = 8
for vertices in find_cliques(G):
    s = set(vertices)
    left_vtc = s /\ left_std_set
    right_vtc = s /\ right_std_set
    if len(left_vtc) >= min_num <= len(right_vtc):
        print(left_vtc, right_vtc)

