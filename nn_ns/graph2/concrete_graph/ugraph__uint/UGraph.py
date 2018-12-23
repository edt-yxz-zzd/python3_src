
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


class UGraph:
    '''

methods:
    vertex2degree
        <<== vertex2maybe_fvertex + ugraph_fake_embedding.fvertex2degree
    vertex2maybe_arbitrary_hedge
        <<== vertex2maybe_fvertex + ugraph_fake_embedding.fvertex2arbitrary_hedge

    degree2unstable_iter_vertices

calc attrs:
    """
    neednot:
    .calc.sorted_vertex_degrees
        .calc.num_vertex_degrees
        .calc.degree2maybe_sorted_vertex_degrees_idx
        .calc.sorted_vertex_degrees_idx2nonempty_sorted_vertices
        <<== .calc.sorted_isolated_vertices + ugraph_fake_embedding.calc fvertex version
    """
    .calc.sorted_isolated_vertices

ugraph_fake_embedding.calc attrs:

'''
    attr_seq = '''
        '''.split()
    attr_set = frozenset(attr_seq)


    @classmethod
    def make_UGraph__simplest(cls, *
        ,num_vertices
        ,hedge2vertex
        ,hedge2aedge
        ):

    @classmethod
    def make_UGraph__simpler(cls, *
        ,num_vertices
        ,hedge2vertex
        ,hedge2aedge
        ,ugraph_fake_embedding
        ):


    def __init__(self, *
        ,num_vertices
        ,num_aedges
            # <<== ugraph_fake_embedding.num_hedges

        ,hedge2vertex
        ,hedge2aedge

        ,aedge2arbitrary_hedge
        ,hedge2another_hedge
            # <<== ugraph_fake_embedding.hedge2another_hedge()

        ,vertex2maybe_fvertex
        ,fvertex2vertex
            # <<== hedge2vertex + ugraph_fake_embedding.fvertex2arbitrary_hedge
        ,ugraph_fake_embedding
        ):

