
# connected component
# vertex aedge hedge
# clockwise next prev around

connected graph
    ??num_vertices >= 1??
connected component
    num_vertices >= 1

biconnected graph
biconnected component
    [num_vertices >= 2][num_aedges >= 2]
    #exclude the_single_nonloop_edge_graph
  why?
    [biconnected] <==> [connected][has no cut vertices][has no a cut edges]
    [connected] ==>> [num_vertices >= 1]
    [has no cut vertices] ==>> [num_vertices != 1]
    ==>> [num_vertices >= 2]
    [num_vertices >= 2][connected]
        ==>> [num_aedges >= 1]
        [has no a cut edges] ==>> [num_aedges != 1]
        ==>> [num_aedges >= 2]


triconnected graph
triconnected component
    num_vertices >= 3

dgraph2strongly_connected_components


UGraph =
    # allow self_loop and multiedge
    #   # allow parallel_loop # multi_self_loop
    # every hedge is outgo hedge
    {num_vertices # for isolated vertices
    ,hedge2vertex
    ,hedge2aedge
    ######### generated dynamic on need or input ############
    ,hedge2clockwise_next_hedge_around_vertex   # fake_embedding
    ,hedge2clockwise_fface                      # named fface
    ######### generated dynamic on need ############
    #,hedge2is_outgo # always True
    ,num_hedges
    ,num_aedges # since no laedge
    ,num_ffaces

    ,hedge2another_hedge
    ,hedge2clockwise_prev_hedge_around_vertex
    ,hedge2clockwise_next_hedge_around_fface
        = hedge2clockwise_next_hedge_around_vertex . hedge2another_hedge
    ,hedge2clockwise_prev_hedge_around_fface
        = hedge2another_hedge . hedge2clockwise_prev_hedge_around_vertex

    ,vertex2degree
    ,fface2degree
    #,aedge2degree # always 2

    ,vertex2unstable_maybe_arbitrary_hedge # vertex degree may be 0
    ,aedge2unstable_arbitrary_hedge # aedge degree == 2 # ugraph
    ,fface2unstable_arbitrary_hedge # fface degree >= 1
        # outgo hedges form clockwise cycles1

    ,unstable_isolated_vertices
    ,unstable_self_loop_aedges
    }

ugraph2connected_components
  function:
    # neednot UGraph constructor
    UGraph -> ([isolated_vertex], [nonempty[aedge]])
  method:
    # need UGraph constructor
    UGraph ->
        {component_idx2ugraph :: [UGraph]

        ,old_vertex2component_idx :: [UInt]
        ,old_vertex2new_vertex :: [UInt]
        ,component_idx2new_vertex2old_vertex :: [[UInt]]

        #,old_hedge2component_idx :: [UInt]
        ,old_hedge2new_hedge :: [UInt]
        ,component_idx2new_hedge2old_hedge :: [[UInt]]

        #,old_aedge2component_idx :: [UInt]
        #,old_aedge2new_aedge :: [UInt]
        #,component_idx2new_aedge2old_aedge :: [[UInt]]
        }

ugraph2biconnected_components
    # input: ugraph # need not connected ugraph
    # output:
    #   super forest
    #       4 node types:
    #           L: leaf-node, from old non-cut vertex
    #           C: cut_vertex-node from old cut vertex
    #           B: biconnected_component-node
    #           E: cut_edge-node
    #       a bipartite graph
    #           L/C-node vs B/E-node
    #           leaves are super_vertex from old_vertex_with_loops0
    #       super vertex <-> (old_vertex_with_loops0 | cut_edge | biconnected_component<new virtual vertex, old hedge/aedge of nonloop>)
  function:
    UGraph -> ([isolated_vertex], [non_isolated_cut_vertex], [nonempty[nonempty[aedge]]])
  method:
    UGraph ->
        # super_vertex <-> (old_vertex_with_loops0 | loop_free_biconnected_component)
        {super_vertex2ugraph :: [UGraph]
        ,super_forest :: UGraph
        ,super_vertex2node_type # L/C/B/E-node
            # num_vertices == 1 and leaf <==> L-node
            # num_vertices == 1 and non-leaf <==> C-node
            # num_vertices == 2 and num_aedges == 1 <==> E
            # num_vertices >= 2 and num_aedges >= 2 <==> B
        ,super_hedge2new_vertex

        ,old_aedge2super_vertex
        ,old_hedge2new_hedge
        ,super_vertex2new_hedge2old_hedge

        ,old_vertex2super_vertex # L/C-node # not B/E-node
            # into but maynot onto
            # injection maynot surjection
            # surjection <==> all old_vertex are isolated
        ,super_vertex2maybe_old_vertex
            # only L/C-node map to old_vertex
        ,super_vertex2new_vertex2old_vertex
            # <<== super_vertex2new_hedge2old_hedge & super_vertex2maybe_old_vertex
        }
loop_free_biconnected_ugraph2triconnected_components
    # input:
    #   biconnected_ugraph without loops
    #       num_vertices >= 2
    #       num_aedges >= 2
    #       exclude the_single_nonloop_edge_graph
    #           why?
    #               see below: super_vertex2new_aedge2super_hedge
    #               ensure no isolated super node
    #               i.e. the super_tree is not a bare root
    # output:
    #   # OPSR-tree # like SPQR-tree
    #   super_tree
    #       4 node types:
    #           S(n-circle n>=3; with virtual aedges)
    #           R(triconnected-component; with virtual aedges)
    #           P: ParallelEdges2 (with virtual aedges; num aedges >= 2)
    #               seperating pair or old aedge end-vertices
    #           O: OldEdge (one old aedge)
    #       super leaf <==> O node
    #       a bipartite graph
    #           S/R/O node vs P node
    #           super_tree has unicenter O/P/S/R node
    #
  function:
    # error: UGraph -> [[aedge]]
    #   should insert virtual aedges
  method:
    UGraph ->
        {super_vertex2ugraph :: [UGraph]
        ,super_tree :: UGraph # OPSR-tree
        ,super_vertex2node_type # O/P/S/R
            # super leaf <==> O
            # num_vertices==2 and not super leaf <==> P
            #
            # num_vertices==2 and num_aedges==1 <==> O
            # num_vertices==2 and num_aedges>=2 <==> P
            # num_vertices>=3 and any/all vertex degrees are 2 <==> S
            # num_vertices>=3 and any/all vertex degrees >= 3 <==> R
        ,super_hedge2new_aedge
            # for orientation: check equal of old-vertex from end-vertex
        ,super_vertex2new_aedge2super_hedge
            # ==>> exclude the_single_nonloop_edge_graph

        ,old_vertex2unicenter_super_vertex
        ,old_vertex2unicenter_new_vertex
            # each old_vertex has at least 1 nonloop aedge
            # each incident aedge contained by a O-node
            # all nodes contain old_vertex form a sub-super-tree
            #   this subtree's leaves are O-nodes, too
            #   ==>> a bipartite graph too
            #   ==>> has a unicenter too
        ,super_vertex2new_vertex2old_vertex

        ,old_aedge2leaf_super_vertex
            # to O-node, i.e. super leaf
        ,old_hedge2new_hedge
        ,super_vertex2maybe_new_hedge2old_hedge
            # only O-node/leaf map to array
        }



