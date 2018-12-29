

__all__ = '''
    relabel_ugraph_fake_embedding__prime
    '''.split()

from .relabel_XXX2YYY import relabel_XXX2YYY


def relabel_ugraph_fake_embedding__prime(*
    ,hedge2fake_clockwise_next_hedge_around_vertex
    ,hedge2another_hedge
    ,hedge2fvertex
    ,hedge2fake_clockwise_fface
    #,fvertex2arbitrary_hedge
    #,fface2arbitrary_hedge

    ,new_hedge2old_hedge
    ,old_hedge2new_hedge
    ,old_fvertex2new_fvertex
    ,old_fface2new_fface
    #,new_fvertex2old_fvertex
    #,new_fface2old_fface
    ):
    '''
-> (hedge2fake_clockwise_next_hedge_around_vertex__new
    ,hedge2another_hedge__new
    ,hedge2fvertex__new
    ,hedge2fake_clockwise_fface__new
    ,fvertex2min_hedge__new
    ,fface2min_hedge__new
    )

    #,fvertex2arbitrary_hedge__new   #=fvertex2min_hedge__new
    #,fface2arbitrary_hedge__new     #=fface2min_hedge__new
'''
    #num_fvertices = len(fvertex2arbitrary_hedge)
    num_hedges = len(hedge2another_hedge)
    #num_ffaces = len(fface2arbitrary_hedge)
    num_ffaces = 1+max(hedge2fake_clockwise_fface, default=-1)
    num_fvertices = 1+max(hedge2fvertex, default=-1)

    assert num_hedges == len(hedge2fake_clockwise_next_hedge_around_vertex)
    assert num_hedges == len(hedge2another_hedge)
    assert num_hedges == len(new_hedge2old_hedge)
    assert num_hedges == len(old_hedge2new_hedge)
    #assert num_ffaces == len(fface2arbitrary_hedge)
    #assert num_ffaces == len(new_fface2old_fface)
    assert num_ffaces == len(old_fface2new_fface)
    #assert num_fvertices == len(fvertex2arbitrary_hedge)
    #assert num_fvertices == len(new_fvertex2old_fvertex)
    assert num_fvertices == len(old_fvertex2new_fvertex)

    hedge2fake_clockwise_next_hedge_around_vertex__new = relabel_XXX2YYY(
        old_XXX2old_YYY=hedge2fake_clockwise_next_hedge_around_vertex
        ,new_XXX2old_XXX=new_hedge2old_hedge
        ,old_YYY2new_YYY=old_hedge2new_hedge
        )
    hedge2another_hedge__new = relabel_XXX2YYY(
        old_XXX2old_YYY=hedge2another_hedge
        ,new_XXX2old_XXX=new_hedge2old_hedge
        ,old_YYY2new_YYY=old_hedge2new_hedge
        )

    hedge2fvertex__new = relabel_XXX2YYY(
        old_XXX2old_YYY=hedge2fvertex
        ,new_XXX2old_XXX=new_hedge2old_hedge
        ,old_YYY2new_YYY=old_fvertex2new_fvertex
        )
    hedge2fake_clockwise_fface__new = relabel_XXX2YYY(
        old_XXX2old_YYY=hedge2fake_clockwise_fface
        ,new_XXX2old_XXX=new_hedge2old_hedge
        ,old_YYY2new_YYY=old_fface2new_fface
        )

    def make_XXX2min_hedge(num_XXXs, hedge2XXX):
        XXX2min_hedge = [None]*num_XXXs
        for hedge, XXX in zip(reversed(range(num_hedges)), reversed(hedge2XXX)):
            XXX2min_hedge[XXX] = hedge
        return XXX2min_hedge

    fvertex2min_hedge__new = make_XXX2min_hedge(num_fvertices, hedge2fvertex__new)
    fface2min_hedge__new = make_XXX2min_hedge(num_ffaces, hedge2fake_clockwise_fface__new)

    return (hedge2fake_clockwise_next_hedge_around_vertex__new
            ,hedge2another_hedge__new
            ,hedge2fvertex__new
            ,hedge2fake_clockwise_fface__new
            ,tuple(fvertex2min_hedge__new)
            ,tuple(fface2min_hedge__new)
            )

    '''
    fface2arbitrary_hedge__new = relabel_XXX2YYY(
        old_XXX2old_YYY=fface2arbitrary_hedge
        ,new_XXX2old_XXX=new_fface2old_fface
        ,old_YYY2new_YYY=old_hedge2new_hedge
        )
    fvertex2arbitrary_hedge__new = relabel_XXX2YYY(
        old_XXX2old_YYY=fvertex2arbitrary_hedge
        ,new_XXX2old_XXX=new_fvertex2old_fvertex
        ,old_YYY2new_YYY=old_hedge2new_hedge
        )
    fface2min_hedge__new
    fvertex2min_hedge__new

    fface2arbitrary_hedge__new = fface2min_hedge__new
    fvertex2arbitrary_hedge__new = fvertex2min_hedge__new
    '''

