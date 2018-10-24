#################################u2vtc
directed_graph.py
    # u2vtc
    is_u2vtc
    is_u2sorted_vtc
    dedges2u2vtc
    u2vtc2dedges
    reverse_dedges
    reverse_u2vtc

    u2vtc_to_strong_connected_components
    components_to_v2std_stds
    sorted_components
    u2vtc_to_strong_connected_components_ex
    to_reversed_topological_ordered_strong_connected_components
        +directed_acyclic_graph.reversed_topological_ordering

dgraph_DFS.py
    # u2vtc
    dgraph_DFS
dgraph_ordered_partition.py
    # u2vtc
    refine_ordered_partition_to_coarsest_equitable
        +directed_graph.is_u2sorted_vtc
directed_acyclic_graph.py
    # u2vtc
    reversed_topological_ordering
    isDAG
    find_a_circle # bug?: result is not a circle!!!
    to_super_DAG
        +dedges2super_dedges
    u2vtc_to_heights
        +DAG_to_heights

#################################simple_undirected_graph
fake_face.py
    # simple_undirected_graph--
    fake_face
DFS.py
    # simple_undirected_graph
    DFS
        partial_DFS
            +fake_face.fake_face
                # not bug
                # but do not support multiedge and...
    is_connected
    is_biconnected
    DFS_lowpt

decompose.py
    # multi_directed_with_loops_graph
    weak_connect1_basic

    # multi_undirected_with_loops_graph
    connect1_basic
    connect2_basic
    connect3_basic
        +SPQR.basic_SPQR

    is_connect3
    connect2_extend
        connect2_extend__get_loops
        connect2_extend__calc_component2vtcs
        connect2_extend__find_out_cut_vtcs
        connect2_extend__find_out_bridge_components
        -connect2_extend__merge_bridges_to_L

BC_tree.py
    # simple_undirected_graph
    connected_components
        +make_connected_components
    bc_tree
        +BC_tree
    spqr_tree
        # O(V^2)
        +SPQR_tree
        ?????????? see below: SPQR.basic_SPQR
        ?????????????????? O(V)????????????

Boyer_Myrvold_planarity_test.py
    # simple_undirected_graph
    is_planar
    Boyer_Myrvold_planarity_test
    is_planar_embedding
    planar_embedding_by_Boyer_Myrvold
planar_embedding.py
    is_planar
    is_planar_embedding
    planar_embedding
    reverse_embedding

    polyhedra_faces2embedding
    polyhedra_embedding2faces
planar_ordering.py
    left_most_canonical_ordering
    drawing_planar_graphs_on_a_grid
    make_connected
rooted_tree.py
    is_vaild_parent_list
    search_parent
    parent2components
    DFS_tree
    rooted_tree

triconnected_planar_graph_isomorphism.py
    canonize_triconnected_planar_simple_graph
        # O(VlogV)

biconnected_planar_d2d3.py
    # simple_undirected_graph
    SPQR_tree_for_c2d2d3_planar
        +is_c2d2d3_planar
            +is_c2d2d3_graph
                +is_biconnected
            +Boyer_Myrvold_planarity_test.is_planar

    # not implemented
    -rs_tree
        -RS_tree_for_c2d2d3_planar

    orthogonal_drawing_of_c1d1d2d3_planar
        orthogonal_drawing_of_c1d1d2d3_tree
            orthogonal_drawing_of_sub_bc_tree
                -calc_xy
        -orthogonal_drawing_of_bc_tree

        ?orthogonal_drawing_of_block_node
        ?orthogonal_drawing_of_sub_rs_tree
        ?orthogonal_drawing_of_sub_rs_tree_rooted_by_R
        ?orthogonal_drawing_of_sub_rs_tree_rooted_by_RS

#################################
subgraph_isomorphism.py
    # not implemented
#################################plantri.embedding <: u2vtc
graph_format_ascii_embedding.py
    str2embedding
    embedding2str
    read_file
    write_file

#################################nauty.GRAPH6&SPARSE6
graph_format_g6_s6.py
    # not implemented

#################################multi_graph
multi_graph.py
    inv_automap
    item_map
    mx_map
    rows_map

    multi_graph
    make_mgraph
    dfs_ordering
    find_lowpt_k
    connected_undirected_mgraph2directed_palm_tree
    palm_tree2tree_info

nauty/cnauty.py
    #graph -> cgraph
        graph2cpacked_graph
        digraph2cpacked_graph
        multi_graph2csparse_graph
        multi_digraph2csparse_graph
    #cgraph -> graph
        cpacked_graph2graph
        cpacked_graph2digraph
        csparse_graph2multi_graph
        csparse_graph2multi_digraph

    #call nauty using py-graph
        nauty_packed
        nauty_sparse
    #call nauty using c-graph
        cnauty_packed
        cnauty_sparse

SPQR.py
    basic_SPQR
    SPQR

#################################
#################################
