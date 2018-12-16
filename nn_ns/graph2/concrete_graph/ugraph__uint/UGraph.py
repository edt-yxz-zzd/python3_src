
'''
see:
    "decompose/README.txt"/UGraph
    nn_ns.CFG.CFG
        using class style like nn_ns.CFG.CFG

UGraph =
    # allow self_loop and multiedge
    #   # allow parallel_loop # multi_self_loop
    # every hedge is outgo hedge
    {num_vertices # for isolated vertices
    ,hedge2vertex
    ,hedge2aedge
    ######### generated dynamic on need or input ############
    ,hedge2fake_clockwise_next_hedge_around_vertex   # fake_embedding
    ,hedge2fake_clockwise_fface                      # named fface
    ######### generated dynamic on need ############
    #,hedge2is_outgo # always True
    ,num_hedges
    ,num_aedges # since no laedge
    ,num_ffaces

    ,hedge2another_hedge
    ,hedge2fake_clockwise_prev_hedge_around_vertex
    ,hedge2fake_clockwise_next_hedge_around_fface
        = hedge2fake_clockwise_prev_hedge_around_vertex . hedge2another_hedge
    ,hedge2fake_clockwise_prev_hedge_around_fface
        = hedge2another_hedge . hedge2fake_clockwise_next_hedge_around_vertex

    ,vertex2degree
    ,fface2degree
    #,aedge2degree # always 2

    ,vertex2unstable_maybe_arbitrary_hedge # vertex degree may be 0
    ,aedge2unstable_arbitrary_hedge # aedge degree == 2 # ugraph
    ,fface2unstable_arbitrary_hedge # fface degree >= 1
        # outgo hedges form fake_clockwise cycles1

    ,unstable_isolated_vertices
    ,unstable_self_loop_aedges
    }


'''

