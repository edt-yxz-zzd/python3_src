
'''
see:
    "planar/algo - is fake_embedding relax_planar.txt"
'''

__all__ = '''
    is_relax_planar_embedding

    detect_ABAB_or_AAA
    iter_non_planar_aedge_pairs
    '''.split()

from ..iter_cycle_from import iter_cycle_from
from seed.abc.Ops__concrete.EqOps import python_eq_key_ops
from seed.types.OneTime import OneTimeSet, OneTimeMap

def is_relax_planar_embedding(ugraph_fake_embedding):
    '''
hedges of fface has no ABAB pattern
'''
    some_hedges = ugraph_fake_embedding.fface2arbitrary_hedge

    aedge_eq_ops = python_eq_key_ops
    def hedge2pseudo_aedge(hedge):
        return min(hedge, ugraph_fake_embedding.hedge2another_hedge(hedge))

    hedge2fake_clockwise_next_hedge_around_fface = \
        ugraph_fake_embedding.hedge2fake_clockwise_next_hedge_around_fface
    num_hedges = ugraph_fake_embedding.num_hedges
    hedge2aedge = tuple(map(hedge2pseudo_aedge, range(num_hedges)))

    buffer__aedge_set = OneTimeSet([None]*num_hedges)
    buffer__forbidden_aedge2aedge = OneTimeMap([None]*num_hedges)

    it = iter_non_planar_aedge_pairs(
        some_hedges
        ,buffer__aedge_set              = buffer__aedge_set
        ,buffer__forbidden_aedge2aedge  = buffer__forbidden_aedge2aedge
        ,aedge_eq_ops                   = aedge_eq_ops
        ,hedge2aedge                    = hedge2aedge
        ,hedge2fake_clockwise_next_hedge_around_fface
            = hedge2fake_clockwise_next_hedge_around_fface
        )

    for _ in it:
        return False
    return True








def detect_ABAB_or_AAA(
    obj_eq_ops, objs, buffer__obj_set, buffer__forbidden_obj2obj
    ):
    '''
input:
    obj_eq_ops
        # seed.abc.Ops__concrete.EqOps.python_eq_key_ops
    objs # Iter obj
        # aedges of a fface
    buffer__obj_set
        # e.g. seed.types.OneTime.OneTimeSet
    buffer__forbidden_obj2obj
        # e.g. seed.types.OneTime.OneTimeMap
output:
    ()|(obj,)|(obj,obj)
    #no ABAB or AAA
    #AAA
    #ABAB
'''
    buffer__forbidden_obj2obj.clear()
    buffer__obj_set.clear()
    obj_stack = []
    for obj in objs:
        assert len(obj_stack) == len(buffer__obj_set)
        #assert set(obj_stack) == set(buffer__obj_set)
        if obj in buffer__forbidden_obj2obj:
            A = buffer__forbidden_obj2obj[obj]
            if obj_eq_ops.eq(A, obj):
                return (A,) #AAA
            B = obj
            return (A, B) #ABAB
        elif obj in buffer__obj_set:
            while obj_stack:
                _obj = obj_stack.pop()
                buffer__obj_set.remove(_obj)
                buffer__forbidden_obj2obj[_obj] = obj
                if obj_eq_ops.eq(_obj, obj):
                    break
            else:
                raise logic-error
        else:
            buffer__obj_set.add(obj)
            obj_stack.append(obj)
    return ()

def iter_non_planar_aedge_pairs(some_hedges, *
    ,buffer__aedge_set
    ,buffer__forbidden_aedge2aedge
    ,aedge_eq_ops
    ,hedge2aedge
    ,hedge2fake_clockwise_next_hedge_around_fface
    ):
    '''
    # donot consider isolated vertex
    # diff connected components donot share same external ffaces
input:
    hedge2aedge # <<== ugraph
    hedge2fake_clockwise_next_hedge_around_fface # ugraph_fake_embedding
    some_hedges # Iter hedge
        # each hedge repr a fface
    buffer # seq of len num_hedges
output:
    Iter (aedge, aedge)
'''
    for hedge in some_hedges:
        #aedge_cycle = (ugraph.hedge2aedge[h] for h in ugraph_fake_embedding.hedge2iter_fake_clockwise_hedges_around_fface(hedge))
        hedge_cycle = iter_cycle_from(hedge2fake_clockwise_next_hedge_around_fface, hedge)
        aedge_cycle = (hedge2aedge[hedge] for hedge in hedge_cycle)
        r = detect_ABAB_or_AAA(
                aedge_eq_ops, aedge_cycle
                , buffer__aedge_set, buffer__forbidden_aedge2aedge
                )
        if r:
            assert len(r) == 2 # ABAB
            yield r



