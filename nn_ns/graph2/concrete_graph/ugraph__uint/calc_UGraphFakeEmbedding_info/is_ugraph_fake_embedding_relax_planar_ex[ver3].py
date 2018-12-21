
from .ugraph_fake_embedding2relax_biconnected_ugraph_fake_embedding_ex \
    import ugraph_fake_embedding2relax_biconnected_ugraph_fake_embedding_ex
from .is_relax_biconnected_ugraph_fake_embedding_relax_planar_ex \
    import is_relax_biconnected_ugraph_fake_embedding_relax_planar_ex
from .make_hedge2fake_counterclockwise_fface \
    import make_hedge2fake_counterclockwise_fface

from .verify_non_relax_planar_condition import (
    verify_non_relax_planar_condition
    ,new_path2old_path
    ,is_path_hedges1
    )


def is_ugraph_fake_embedding_relax_planar_ex(*
    ,ugraph_fake_embedding
    ,hedge2aedge
    #bug: ,hedge2fake_counterclockwise_fface
    ):
    '''
input:
    ugraph_fake_embedding :: UGraphFakeEmbedding
    hedge2aedge
        if no ugraph on hand:
            see: .make_hedge2fake_aedge
output:
    () | (cycle_hedges1, path_hedges1)
        ()
            relax_planar
        (cycle_hedges1, path_hedges1)
            non-relax_planar
            when treat cycle_hedges1 as clockwise cycle:
                path_hedges1 begin inside&on cycle_hedges1
                path_hedges1 end outside&on cycle_hedges1
'''
    #assert isinstance(ugraph_fake_embedding, UGraphFakeEmbedding)
    (ugraph_fake_embedding__new, hedge2aedge__new
    ) = ugraph_fake_embedding2relax_biconnected_ugraph_fake_embedding_ex(
        ugraph_fake_embedding=ugraph_fake_embedding
        , hedge2aedge=hedge2aedge
        )
    (hedge2fake_counterclockwise_fface__new
    ) = make_hedge2fake_counterclockwise_fface(
            hedge2fake_clockwise_fface
                = ugraph_fake_embedding__new.hedge2fake_clockwise_fface
            ,hedge2fake_clockwise_prev_hedge_around_vertex
                = ugraph_fake_embedding__new.hedge2fake_clockwise_prev_hedge_around_vertex
            )



    (case, result
    ) = is_relax_biconnected_ugraph_fake_embedding_relax_planar_ex(
            relax_biconnected_ugraph_fake_embedding
                = ugraph_fake_embedding__new
            ,hedge2fake_counterclockwise_fface
                #bug: = hedge2fake_counterclockwise_fface
                = hedge2fake_counterclockwise_fface__new
            )
    if case == 0:
        return ()
    elif case == 2:
        (cycle_hedges1, path_hedges1) = result
        try:
            assert verify_non_relax_planar_condition(
                ugraph_fake_embedding__new, cycle_hedges1, path_hedges1)
        except:
            from seed.tiny import print_err
            print_err(f'ugraph_fake_embedding__new={ugraph_fake_embedding__new}')
            print_err(f'hedge2fake_counterclockwise_fface__new={hedge2fake_counterclockwise_fface__new}')
            print_err(f'cycle_hedges1={cycle_hedges1}')
            print_err(f'path_hedges1={path_hedges1}')
            print_err(f'is_path_hedges1(ugraph_fake_embedding__new, cycle_hedges1)={is_path_hedges1(ugraph_fake_embedding__new, cycle_hedges1)}')
            print_err(f'is_path_hedges1(ugraph_fake_embedding__new, path_hedges1)={is_path_hedges1(ugraph_fake_embedding__new, path_hedges1)}')
            #print_err(f'XXX={XXX}')
            raise

        # convert back to original hedges
        #   HPM/HNM -> old hedges
        #   remove other HXY
        cycle_hedges1 = new_path2old_path(cycle_hedges1)
        path_hedges1 = new_path2old_path(path_hedges1)

        '''
        assert verify_non_relax_planar_condition(
            ugraph_fake_embedding, cycle_hedges1, path_hedges1)
        '''
        return (cycle_hedges1, path_hedges1)
    elif case == 1:
        # ugraph_fake_embedding2relax_biconnected_ugraph_fake_embedding_ex
        #   should no fface contain duplicated fvertex
        raise logic-error
    else:
        raise logic-error-unknown-case

