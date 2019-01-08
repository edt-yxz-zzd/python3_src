canon_label_rigid_connected_planar_ugraph
ICanonLabelRigidConnectedPlanarUGraph




TODO:
    vertex2color, ...

def utree2centers(utree):
    # -> (unicenter_vertex,) | (bicenter_vertex0, bicenter_vertex1)
    pass
def make_vertex2maybe_parent_aedge_with_root_vertex(utree, root_vertex):
    # -> [(None|aedge)]
    pass
def make_vertex2child_aedges_with_root_vertex(utree, root_vertex):
    # -> [[aedge]]
    pass
def make_aedge2parent_hedge_with_root_vertex(utree, root_vertex):
    # -> [hedge]
    pass
def make_vertex2depth_with_root_vertex(utree, root_vertex):
    # -> [depth]
    # vertex2depth
    # vertex2depth[root_vertex] == 0
    pass
def make_depth2vertices_with_root_vertex(utree, root_vertex):
    # -> [[vertex]]
    # depth2vertices
    vertex2depth = make_vertex2depth_with_root_vertex(utree, root_vertex)
    L = 1+max(vertex2depth, default=-1)
    depth2vertices = [[] for _ in range(L)]
    for vertex, depth in enumerate(vertex2depth):
        depth2vertices[depth].append(vertex)
    assert all(depth2vertices)
    return tuple(map(tuple, depth2vertices))

canon_label_flower_ugraph
canon_label_bond_ugraph
canon_label_rigid_biconnected_planar_ugraph
def canon_label_rigid_connected_planar_ugraph(ugraph):
    biconnected_components = decompose_rigid_connected_ugraph2biconnected_components__BC(ugraph)
    super_utree = biconnected_components.super_utree
    subgraphs = biconnected_components.super_vertex2ugraph
    #super_vertex2case = biconnected_components.super_vertex2case
    def canon_BC(super_vertex):
        subgraph = subgraphs[super_vertex]
        #case = super_vertex2case[super_vertex]
        num_vertices = subgraph.num_vertices
        if num_vertices == 1:
            # leaf or cut_vertex
            canon = canon_label_flower_ugraph
        elif num_vertices == 2:
            # bridge_bond
            canon = canon_label_bond_ugraph
        else:
            # biconnected_block
            canon = canon_label_rigid_biconnected_planar_ugraph
        labelling = canon(subgraph)
        return labelling

    new_subgraphs = tuple(map(canon_BC, range(super_utree.num_vertices)))




    [unicenter_super_vertex] = utree2centers(super_utree)
    depth2super_vertices = make_depth2vertices_with_root_vertex(super_utree, unicenter_super_vertex)
    super_vertex2maybe_parent_super_aedge = make_vertex2maybe_parent_aedge_with_root_vertex(super_utree, unicenter_super_vertex)
    super_vertex2child_super_aedges = make_vertex2child_aedges_with_root_vertex(super_utree, unicenter_super_vertex)
    super_aedge2parent_super_hedge = make_aedge2parent_hedge_with_root_vertex(super_utree, unicenter_super_vertex)

    #biconnected_components.super_vertex2maybe_parent_super_hedge
    #biconnected_components.super_aedge2parent_super_hedge
    super_vertex2unordered_child_super_vertices = [[] for _ in range(super_utree.num_vertices)]
    super_vertex2sorted_child_upper_colors = [None for _ in range(super_utree.num_vertices)]
    super_vertex2upper_color = [None]*super_utree.num_vertices
    is_super_leaf_or_cut_super_vertex = True
    prev_num_upper_colors = 0
    for super_vertices in reversed(depth2super_vertices):
        level
        if is_super_leaf_or_cut_super_vertex:
            child_upper_colorss = []
            for super_vertex in super_vertices:
                child_upper_colors = []
                for child_super_aedge in super_vertex2child_super_aedges[super_vertex]
                    child_upper_super_hedge = super_aedge2parent_super_hedge[child_super_aedge]
                    child_lower_super_hedge = utree.hedge2anohter_hedge[child_upper_super_hedge]
                    child_super_vertex = utree.hedge2vertex[child_lower_super_hedge]
                    child_upper_color = super_vertex2upper_color[child_super_vertex]
                    # assert 0 <= child_upper_color < prev_num_upper_colors
                    child_upper_colors.append(child_upper_color)
                super_vertex2sorted_child_upper_colors[super_vertex] = child_upper_colors
                child_upper_colorss.append(child_upper_colors)
            #sort child_upper_colors
            inplace_bucket_sort__lsls(prev_num_upper_colors, child_upper_colorss)
        sorted_super_vertices = bucket_sort4uint_seq(prev_num_upper_colors, super_vertices, key=lambda super_vertex: super_vertex2sorted_child_upper_colors[super_vertex])
        for super_vertex in super_vertices:
            sorted_child_colors = super_vertex2sorted_child_upper_colors[super_vertex]
        is_super_leaf_or_cut_super_vertex = not is_super_leaf_or_cut_super_vertex
        prev_num_upper_colors


from ..imports__bucket_sort import bucket_sort4uint_seq
inplace_bucket_sort__lsls
from .ICanonLabelSuperUTree import ICanonLabelSuperUTree



def make_aedge2maybe_upper_hedge_from_utree_with_root_vertex(utree, root_vertex):
def make_aedge2maybe_upper_hedge_from_utree_with_root_aedge(utree, root_aedge):
    # -> [(None|upper_hedge)]
    # aedge2maybe_upper_hedge
    pass
def make_vertex2maybe_parent_aedge_from_utree_with_root_vertex(utree, root_vertex):
def make_vertex2depth_from_utree_with_root_vertex(utree, root_vertex):
def make_vertex2depth_from_utree_with_root_aedge(utree, root_aedge):
    # -> [depth]
    # vertex2depth
    # vertex2depth[root_vertex] == 0 for root_vertex incident to root_aedge
    pass
def make_depth2vertices1_from_vertex2depth(vertex2depth):
def utree2either_center(utree)
    # -> (is_bicenter, unicenter_vertex_or_bicenter_aedge)
    # -> (False, unicenter_vertex)|(True, bicenter_aedge)
    pass
    :: num_global_colors -> row2column2global_color
    -> num_layers -> row2layer
    -> (layer2num_layer_local_colors, row2column2layer_local_color, layer2layer_local_color2global_color)


    (is_bicenter, unicenter_or_bicenter
    ) = utree2either_center(super_utree)

    if is_bicenter:
        bicenter_super_aedge = unicenter_or_bicenter
        labelling = canon_label_bicenter_super_utree(super_utree, bicenter_super_aedge, rooted_super_utree_attrs)
    else:
        unicenter_super_vertex = unicenter_or_bicenter
        labelling = canon_label_unicenter_super_utree(super_utree, unicenter_super_vertex, rooted_super_utree_attrs)
    return labelling

def canon_label_unicenter_super_utree(super_utree, unicenter_super_vertex, rooted_super_utree_attrs):
def canon_label_bicenter_super_utree(super_utree, bicenter_super_aedge, rooted_super_utree_attrs):

