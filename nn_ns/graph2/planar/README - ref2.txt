
connected undirected graph
    num_vertices >= 1
connected undirected planar graph
    # self_loops, multiedges
    V=num_vertices
    E=num_aedges
    H=num_hedges=2E
    F=num_faces

    V + F = E + 2
    V >= 1
    F >= 1
    E >= 0

    D=mean_vertex_degree :: float >= 0
    O=mean_face_degree :: float >= 0
    D*V = H
    O*F = H

    ==>>
        V=H/D
        F=H/O
        E=H/2

    [D > 0]
        1/D + 1/O = 1/2 + 2/H = 1/2 + 1/E
        1/D + 1/O = 1/2 + 1/E

connected regular undirected planar graph
    # may not simple
    D :: UInt
    O :: float >= 0

    [D == 0]
        E = H = 0
        V + F = 2
        V = F = 1
        O = 0
    [D == 1]
        H > 0
        E >= 1
        1/1 + 1/O = 1/2 + 1/E
        1/2 + 1/O = 1/E
        1/O = 1/E - 1/2 > 0
        E < 2

        E = 1
        H = 2
        V = 2
        F = 1
        O = 2

    [D == 2]
        E >= 1
        1/2 + 1/O = 1/2 + 1/E
        1/O = 1/E

        E = n
        O = n
        V = n
        F = 2

    # D >= 3
    [D == 3]
        1/3 + 1/O = 1/2 + 1/E
        1/O = 1/6 + 1/E
        O = 6*E/(6+E) :: float
    ...

connected regular undirected planar graph with regular faces
    D :: UInt
    O :: UInt

    # for 0 <= D <= 2 see above
    [D > 0]
        E > 0
        1/D + 1/O = 1/2 + 1/E > 1/2
        1/O > 1/2 - 1/D
        [1/2 - 1/D > 0] <==> [D > 2]
        [D > 2]
            O < 1/(1/2-1/D) = 2*D/(D-2)
    [D >= 3]
        O < 2*D/(D-2) = 2 + 4/(D-2) <= 2+4/(3-2) = 6
        O < 6

    switch D&O
        [D == 0] ==>> [O == 0]
        [D == 1] ==>> [O == 2]
        [D == 2] ==>> [O == E]
        [D >= 3] ==>> [O < 6]
    [O == 0] ==>> [D = 0]
    [O == 1] ==>> [D = 2]
        # single self_loop
        # 1-cycle
    [O == 2] ==>> [D = E]
        # multiedges
        # n-bond
    [O >= 3] ==>> [D < 6]


    [x,y [3..5]][1/x + 1/y = 1/2 + 1/E][E > 0]
        [x=3]
            1/y = 1/6 + 1/E
            [y=3][E=6]
            [y=4][E=12]
            [y=5][E=30]
        [x=4]
            1/y = 1/4 + 1/E
            [y=3][E=12]
        [x=5]
            1/y = 3/10 + 1/E
            [y=3][E=30]
        {x,y} <- {{3,3}, {3,4}, {3,5}}
        ({x,y}, E) <- {({3,3},6), ({3,4},12), ({3,5},30)}

    # 5 solutions:
    [D == 3][O == 3]
        E = 6
        V = 4
        F = 4
    [D == 3][O == 4]
        E = 12
        V = 8
        F = 6
    [D == 4][O == 3]
        E = 12
        V = 6
        F = 8
    [D == 3][O == 5]
        E = 30
        V = 20
        F = 12
    [D == 5][O == 3]
        E = 30
        V = 12
        F = 20


    # 6 special cases:
    [D == 0][O == 0] # isolated vertex
        E = 0
        V = 1
        F = 1
    [D == 1][O == 2] # aedge
        E = 1
        V = 2
        F = 1
    [D == 2][O == 1] # self_loop
        E = 1
        V = 1
        F = 2
    [D == 2][O == 2] # Q
        E = 2
        V = 2
        F = 2
    [D == 2][O == n >= 3] # S # n-cycle
        E = n
        V = n
        F = 2
    [D == n >= 3][O == 2] # P # n-bond
        E = n
        V = 2
        F = n

define degree_1_face:
    facee f is called degree_1_face iff face2degree[f] == 1
define min_loop:
    aedge e is called min_loop iff
        exist h <- aedge2hedges[e]. embedding.hedge2clockwise_next_hedge[h] == hedge2another_hedge[h]
        i.e. exist f <- embedding.aedge2face[e]. f is degree_1_face
    # self_loop may incident to 0/1/2 degree_1_faces.
define parallel_loop:
    aedge e0 is parallel_loop of e1 iff
        exist h <- aedge2hedges[e0].
            e1 == hedge2aedge[embedding.hedge2clockwise_next_hedge[h]]
               == hedge2aedge[embedding.hedge2clockwise_prev_hedge[hedge2another_hedge[h]]]
    # hence e1 is parallel_loop of e0

connected undirected planar graph with num_aedges >= 2 and simple embedding
    simple embedding <==> [no multiedge][no parallel_loop][no min_loop]
        # the graph itself may have multiedge
        #   it is the embedding has not
        # the graph itself may have self_loop
        #   it is the embedding has not min_loop and parallel_loop

    D,O :: float >= 0

    [has degree_0_face] ==>> [E == 0] error
    [has degree_1_face] ==>> [has min_loop] ==>> [not simple embedding] error
    [has degree_2_face] ==>> [E == 1]or[has bond] ==>> [not E==2]or[not simple embedding] error
    ==>> [face degree >= 3]
    ==>> [O >= 3]
    ==>> [D < 6]

    # "weir" means self_loop(but not min_loop) occurs
    #   except the regular_Veq1_regular_Feq2
    there exists "weir" regular vertex_degree embedding
        e.g. O-O : both vertices have degree 3; 2 self_loops
    ??does there exist "weir" regular vertex_degree regular face_degree embedding??
        NO!!
        assume exist one
        each self_loop split the whole plane/sphere into 2 part
        let us choose a self_loop and the half sphere which donot contain other self_loops
            let us name the subgraph in the half sphere we choose as G (not contain the outer self_loop
            then G is nearly regular except:
                one vertex has less degree: DD-2-k
                    other vertices has degree DD
                    k is the remain degree of the vertex on another half sphere
                        k >= 1 # since no min_loop
                    V >= 1
                    DD > 2+k
                        ==>> DD >= 3+k >= 4
                        # except the regular_Veq1_regular_Feq2
                        # which DD = 2
                one face has degree: OO-1
                    other faces has degree OO
                    OO >= 1
                    E >= 0
            [no self_loop]
                [no min_loop]
                [OO != 1]
            [no self_loop]
                [no parallel_loop]
                    [no degree_2_face between parallel_loops]
            [no multiedge]
                [no degree_2_face between multiedge]
            [DD >= 3]
                [no degree_2_face bound by single aedge]
            ==>> [no degree_2_faces]
            ==>> [OO != 2]
            ==>> [OO >= 3]

            (V-1)*DD + (DD-2-k) = 2*E = H = (F-1)*OO + (OO-1)
            V*DD - (2+k) = 2*E = F*OO - 1
            V = (2*E + (2+k)) / DD
            F = (2*E + 1) / OO
            V + F = E + 2
            (2*E + (2+k)) / DD + (2*E + 1) / OO = E + 2
            2*E/DD + (2+k)/DD + 2*E/OO + 1/OO = E + 2
            2*E(1/DD+1/OO) + (2+k)/DD + 1/OO = E + 2
            2*(1/DD+1/OO-1/2)*E = 2 - (2+k)/DD - 1/OO
                > 0 # since D > 2+k ; OO > 0
            ==>> [1/DD+1/OO > 1/2][E>0]
            [OO >= 3]
            [1/OO <= 1/3]
            [1/DD > 1/6]
            [DD < 6]
            [4 <= DD <= 5]
            [OO == 3]
            [DD=5][OO=3]
                E = 25-3*(k+2)
                k<-[1..2] # since DD >= 3+k; k >= 1
                [k=1][E=16]
                [k=2][E=13]
            [DD=4][OO=3]
                E = 10-3/2*(k+2)
                k<-[1..1]
                [k=1] ==>> E not UInt error

            [DD=5][OO=3][k=1][E=16][V=7][F=11]
                vertex_degree[start v] = DD-2-k = 2
                external_face_degree = OO-1 = 2
                can not construct G
            [DD=5][OO=3][k=2][E=13][V=6][F=9]
                vertex_degree[start v] = DD-2-k = 1
                external_face_degree = OO-1 = 2
                can not construct G
        conclusion:
            no "weir" regular vertex_degree regular face_degree embedding

algo = algo_1 >> algo_2 >> algo_3
algo input:
    planar embedding of connected undirected planar graph
        num_vertices >= 1
        num_aedges >= 1
            # why?
            #   no color only hweight
            #   so we need aedge to avoid isolated vertex without loops
algo_1:
    reduct
    # algo_1 need not sort or classify/partition
algo_2:
    flatten hweight
    bucket sort
    relabel hweight
    if cycle hweights then min_period else O(n^2) relabel result graph...
algo_3:
    regenerate and relabel graph


algo_1:
################ duplicated since not O(1) ################
(1) remove self_loops by cut one loop into two new aedges
    one loop -> two new degree_1_vertices and two new aedges
    cut loop:
        h0, h1 are the two hedges of loop
        hweights of new e0 = (hweight[h0], n0)
        hweights of new e1 = (hweight[h1], n1)
        n0 is the number of hedges between h0,h1 in clockwise
        n1 is the number of hedges between h1,h0 in clockwise
            how to count n0 in O(1)?
################ duplicated since not O(1) ################
(1) remove parallel_loops and min_loops
    (1_1) remove parallel_loops
        many to one
        how?
            for each end: group hweights in clockwise
            e1//e2//e3//e4//..//e[n]
            h[2i-1]-e[i]-h[2i]
            h[2i-1] -clockwise-> h[2(i+1)-1]
            h[2i] -clockwise-> h[2(i-1)]

            new aedge: h1' - e1' - h2'
            h1' = [h1,h3,...,h[2n-1]]
            h2' = [h[2n],...,h4,h2]
    (1_2) remove min_loops
        clockwise_next_aedge[min_loop] may be
            * min_loop
            * aedge not min_loop
                # may be self_loop
                # at later round may be come min_loop
        min_loop_line = max neighbor min_loops
        save hweights into clockwise_next_hedge of the whole min_loop_line
            # why not save to aedge?
            #   since the another hedge may save other min_loop_line hweights
        goto (1_2)

(2) remove bonds
    (2_1) is regular_Veq2_regular_Fge2? stop
        # include 2-bond/2-cycle
    (2_2) bond with non_bond_aedge -> one new aedge
(3) remove degree_1_vertices
    (3_1) is regular_Veq2_regular_Feq1? stop
    (3_2) is star? stop
    (3_3) remove degree_1_vertices
        save degree_1_vertices to clockwise_next_hedge
            # like min_loop_line
    if has parallel_loops or min_loops goto (1)
    if has bonds goto (2)
# now no self_loops, no bonds, no degree_1_vertices
# vertex degree >= 2
(4) remove degree_2_vertices
    (4_1) is regular_Vge2_regular_Feq2? stop
        # n-circle
        # assert n >= 3
    (4_2) remove degree_2_vertices_line
        ...v[deg>2]-(hw0,hw1)-v[deg=2]-(hw2,hw3)-...-v[deg=2]-(hw2n,hw2n1)-v[deg>2]...
        ...v[deg>2]-([hw0,hw2,...hw2n], [hw2n1,...hw3,hw1])-v[deg>2]...
    if has parallel_loops or min_loops goto (1)
    if has bonds goto (2)
# now no self_loops, no bonds, no degree_1_vertices, no degree_2_vertices
# vertex degree >= 3
#   ==>> num_aedges >= 2
#   ==>> connected undirected planar graph with num_aedges >= 2 and simple embedding
#   ==>> O >= 3
#   ==>> D < 6
#
# vertex degree >= 3
#   ==>> D >= 3
#   ==>> O < 6
#
#   ==>> 3 <= D < 6
#   ==>> 3 <= O < 6
#   ==>> min_vertex_degree < 6
#   ==>> min_face_degree < 6
(5) remove degree_d_vertices_with_all_diff_degree_neighbors
    d-star ==>> d-gon
    (5_1) remove degree_3_vertices_with_all_diff_degree_neighbors
    (5_2) remove degree_4_vertices_with_all_diff_degree_neighbors
    (5_3) remove degree_5_vertices_with_all_diff_degree_neighbors
    save hweights to the new clockwise_next_hedge
    if has bonds goto (2)
(6) remove degree_d_vertices_with_both_same_and_diff_degree_neighbors
    select a aedge to collapse
        selected aedge = (degree_d_vertex, not_degree_d_vertex)
            # d into not_d
            # d <= 5 ==>> O(1)
        d == vertex2degree[hedge2vertex[hedge2another_hedge[hedge2clockwise_next_hedge[hedge on the degree_d_vertex side]]]]
        save hweights of selected aedge into the clockwise_next_hedge
    (6_1) remove degree_3_vertices_with_both_same_and_diff_degree_neighbors
        example:
            n-wheel -[(6_1)]-> n-flower
            define n-wheel:
                1-2-3-...-n
                0-1,0-2,...,0-n
            define n-flower:
                # n-flower is embedding instead of just graph
                # n-wheel and n-band are triconnected simple planar graph
                #   embedding and graph are nearly the same
                vertices = {0}
                v0-h1-e1-h2-v0
                v0-h3-e2-h4-v0
                ...
                v0-h[2n-1]-e[n]-h[2n]-v0

                hedge2clockwise_next_hedge[h1] == h2
                hedge2clockwise_next_hedge[h3] == h4
                ...
                hedge2clockwise_next_hedge[h[2n-1]] == h[2n]

                hedge2clockwise_next_hedge[h2] == h3
                ...
                hedge2clockwise_next_hedge[h[2n-2]] == h[2n-1]
                hedge2clockwise_next_hedge[h[2n]] == h[1]

        goto (1)
    (6_2) remove degree_4_vertices_with_both_same_and_diff_degree_neighbors
        (6_2_1) (4,ge5,4,ge5)
            degree_4_vertice form a circle, may be 1-circle/self_loop
        goto (1)
    (6_3) remove degree_5_vertices_with_both_same_and_diff_degree_neighbors
        goto (1)
# now no self_loops, no bonds, no degree_1_vertices, no degree_2_vertices, regular vertex degree
# vertex degree >= 3
#   # see above
#   ==>> min_face_degree < 6
# regular vertex degree < 6 ==>> collapse aedge in O(1)
(7) remove vertices_with_unique_face_degree_d
    # face_degree: 3,4,5,ge6
    #
    # v may has self_loop which is not min_loop
    #   so face contain self_loop must incident to v at least twice
    #   hence no unique
    #   i.e. self_loop will not be selected edge to be collapsed
    by collapse the selected edges
        if selected edges form arcs: ...
        if selected edges form circles: ...
    (7_1) remove vertices_with_unique_face_degree_3
    (7_2) remove vertices_with_unique_face_degree_4
    (7_3) remove vertices_with_unique_face_degree_5
    (7_4) remove vertices_with_unique_face_degree_ge6
        example:
            n-band -[(7_4)][(1_2)]-> n-bond
            define n-band:
                1-3-...-(2n-1) -1
                2-4-...-  2n   -2
                1-2,3-4,...,(2n-1)-2n

(8) is regular face_degree? stop
    # regular_Vge3_regular_Fge3
    # the 5 solutions
# now no self_loops, no bonds, no degree_1_vertices, no degree_2_vertices, regular vertex degree, not regular face degree, no vertices with unique face_degree
# [not regular face_degree]
#   ==>> exist vertex v has more than one face_degrees
#   [no vertices with unique face_degrees]
#       ==>> vertex_degree[v] >= 2*num_diff_face_degrees >= 2*2 = 4
#       ==>> regular vertex_degree <- [4..5]
#   [D >= 4]
#       O < 2*D/(D-2) = 2 + 4/(D-2) <= 2+4/(4-2) = 4
#       min_face_degree <= O < 4
#   ==>> min_face_degree = 3
#
(9) remove vertices_with_diff_face_degrees_without_unique_face_degree
    # face_degree: 3,ge4
    # regular vertex_degree <- [4..5]
    # * v has only 1 face_degrees
    # * v has 2 face_degrees, must exist!

    must have degree_3_faces
    let f3_vtc = vertices that incident to at least one degree_3_faces
    [len f3_vtc > 0]
    [no v <- f3_vtc has another face_degrees]
        ==>> f3_vtc form a connected component
        ==>> f3_vtc == all vertices
        ==>> regular face_degree 3
        ==>> error
    ==>> [exist v <- f3_vtc has another face_degrees]
    # face_degree: 3,ge4

    if regular vertex_degree == 5:
        (9_1) remove vertices_with_face_degrees 3 and ge4
            one and only one neighbor (3,3) or (ge4,ge4)
            selected the middle edge to collapse
            mark as a directed edge
            one aedge may have 2 directions
            one vertex can not have diff outgo and income aedge at same time
    if regular vertex_degree == 4:
        (9_2) remove vertices_with_face_degrees 3 and ge4
            (9_2_1) (3,3) # both (3,3) and (ge4,ge4)
                like above
                one aedge may have 2 directions
            (9_2_2) (3,ge4,3,ge4)
                3-gon ==>> 3-star
                # at least one degree_2_vertices to be remove
                #   with at least one aedges
                # 2 new vertices v.s. degree_2_vertices and aedges
                #   size not increase
                # and since not regular vertex_degree later
                #   will perform more reductions




