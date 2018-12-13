[Planar_Graph_Isomorphism_1974]Linear time algorithm for isomorphism of planar graphs[good].pdf
    only bucket classify/partition not bucket sort!! [[linear|cycle]]
        the coloring/hweighting are unstable!!!
        we can not encode the ugraph!
        we can only classify/partition planar ugraphs instead of encoding each and then classifying!!
    only handle triconnected planar simple ugraph!
        although loops and bonds will occur while processing.
            loops of same vertex
                should not be one inside another.
                be neighbours or seperatered by non-loop edges
        ?can occur isolated vertex with loops beside other components?
            no, alway only one connected component.
            isolated vertex with loops is the only component.
        ?treat 2-cycle as bond or cycle?
            if treat 2-cycle as cycle then generate 2 loops. one inside another. forbidden.
            so must treat 2-cycle as bond


algo name: O(n) encoding hweighted_planar_ugraph by reduction 1974
    for each connected component:
        BC tree
        SPQR tree
        if root of BC tree is neither vertex nor bond
            and root of SPQR tree of root of BC tree is R:
            encode R/triconnected_planar_ugraph by using:
                algo name: O(n) encoding hweighted_planar_ugraph by reduction 1974
                planar_embedding algo # 2 possible planar_embeddings
        tree-encoding algo


algo name: O(n) encoding hweighted_planar_ugraph_embedding by reduction 1974
input:
    undirected_graph
        # no haedge, no laedge
        # may not connected
        # with loops, multiedges/bonds/parallel_edges
        # repr by hedges
    planar_embedding
    hedge2hweight
output:
    encoding_data
        == sorted[([(reduction_name, new_hweight2old_hweight_tuple)], final_graph_encoding) for each connected component]

        final_graph_encoding come from:
            algo name: O(n^2) encoding hweighted_planar_ugraph_embedding by naive DFS for all start hedge
            input:
                # 6 possibles:
                single vertex or one of the 5 regular solid polyhedron polyhedra
                planar_embedding
                hedge2hweight
            since input has constant size, so final_graph_encoding is O(1)
outline:
    loop:
        remove loops, bonds, vertices of degree 1
        if not regular graph:
            for d in [2..5]:
                for v in vertices of degree d incident with non-degree-d vertices:
                    if vertex of degree d incident with no degree d vertices:
                        d-star to d-gon
                    else:
                        if not (4,x,4,y):
                            find out the repr aedge
                            collapse the aedge
                                # non-degree-d vertex as center:
                                #   multi degree-d vertices collapse to the center
                        else:
                            #(4,x,4,y)
                            "+" ==>> "N"
                            #  x          x
                            # 4+4  ==>> 4 N 4
                            #  y          y
        else:
            # regular graph
            Ls = numbers of edges of faces
            if len(Ls) == 1:
                break # stop
            for L in [3,4,5]:
                for v in vertices incident exactly one face of size L:
                    choose one aedge from two and assign direction
                we now have directed [lines|cycles] # the paper say directed [trees|cycles]
                for directed cycles:
                    collapse the face to a new vertex
                for directed lines:
                    for v in bottomup line: # dfs
                        collapse the aedge

            #no vertices incident exactly one face of size L
            # face size 3 or x # x repr ">3"
            for v in vertices incident faces of size 3,x:
                if not (3,x,3,x):
                    # deg 4 or 5
                    # cycle (3,3,x,x)    ==>> 33
                    #       #both 33 and xx choose arbitrary one
                    # cycle (3,3,3,x,x)  ==>> xx
                    # cycle (3,3,x,x,x)  ==>> 33
                    # cycle (3,x,3,x,x)  ==>> xx
                    #
                    # "33" or "xx"
                    let e be the aedge between 33 or xx
                    assign a direction to e
                    e may have two directions!!!
                    ...collapse e depends on directions...
                else:
                    #(3,x,3,x)
                    # deg 4
                    3-gon/triangle face ==>> 3-star
                        # two new vertices, E be same
                        #   V'=V+2, E'=E
                        # the original v is now of degree 2, can be removed
                        #   hence V'--, E'--
                        #   V''=V'-1, E''=E'-1
                        # V''+E''=V'+E'-2=V+E


classify:
    1) max, [[UInt]]
        use bucket sort
    2) max, [cycle[UInt]]
        use nn_ns.RMQ.make_SA_LCP
        #instead of use nn_ns.RMQ.min_period
        # chain double cycle
        make_SA_LCP(chain.from_iterable(chain(cycle, cycle) for cycle in cycles))
        #LCP < len
        #   find out min index i: (cycle+cycle)[i:len(cycle)+i] is the min period



