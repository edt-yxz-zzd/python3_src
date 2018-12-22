
'''
see:
    "def - 3.5. non_planar_condition.txt"
        for non_planar_condition
'''


__all__ = '''
    verify_non_planar_condition

    check_non_planar_condition
    CheckNonPlanarConditionError
    CheckNonPlanarConditionTypeError
    CheckNonPlanarConditionValueError
    '''.split()

from ..NonEmptyPathOps import (
    Path
    ,NonEmptyPathOps
    ,are_distinguish_elements
    )
from .is_in_clockwise_around_vertex import is_in_clockwise_around_vertex
from itertools import chain
from seed.types.OneTime import OneTimeSet


class CheckNonPlanarConditionError(Exception):pass
class CheckNonPlanarConditionTypeError(CheckNonPlanarConditionError):pass
class CheckNonPlanarConditionValueError(CheckNonPlanarConditionError):pass
def verify_non_planar_condition(ugraph_fake_embedding, non_planar_condition):
    try:
        check_non_planar_condition(ugraph_fake_embedding, non_planar_condition)
    except CheckNonPlanarConditionError:
        return False
    return True

def check_non_planar_condition(ugraph_fake_embedding, non_planar_condition):
    path_ops = NonEmptyPathOps(ugraph_fake_embedding)

    buffer__fvertex2XXX = [None]*ugraph_fake_embedding.num_fvertices
    buffer__fvertex_set = OneTimeSet(buffer__fvertex2XXX)
    _check_type(path_ops, non_planar_condition, buffer__fvertex_set)

    (simple_nonempty_path0, simple_path1, simple_nonempty_path2
    ) = non_planar_condition
    path, end_fvertex = simple_path1
    simple_path1 = Path(ugraph_fake_embedding, path, end_fvertex)
    args = (path_ops
        , simple_nonempty_path0, simple_path1, simple_nonempty_path2)

    _check_same_end_fvertices(*args)
    _check_distinguish_middle_fvertices(*args, buffer__fvertex_set)
    _check_end_hedges_embedding_in_same_direction(*args)







def _check_type(path_ops, non_planar_condition, buffer__fvertex_set):
    if type(non_planar_condition) is not tuple: raise CheckNonPlanarConditionTypeError
    if len(non_planar_condition) != 3: raise CheckNonPlanarConditionTypeError


    def is_simple_maybe_empty_path(path):
        return path_ops.is_simple_maybe_empty_path(path, buffer__fvertex_set)
    def is_simple_nonempty_path(path):
        return path_ops.is_simple_nonempty_path(path, buffer__fvertex_set)

    (simple_nonempty_path0, simple_path1, simple_nonempty_path2
    ) = non_planar_condition
    if not is_simple_maybe_empty_path(simple_path1): raise CheckNonPlanarConditionTypeError
    if not is_simple_nonempty_path(simple_nonempty_path0): raise CheckNonPlanarConditionTypeError
    if not is_simple_nonempty_path(simple_nonempty_path2): raise CheckNonPlanarConditionTypeError
    return





def _check_same_end_fvertices(path_ops, simple_nonempty_path0, simple_path1, simple_nonempty_path2):

    end_fvertices_1 = simple_path1.end_fvertices
    end_fvertices_0 = path_ops.end_fvertices_of__basic(simple_nonempty_path0)
    end_fvertices_2 = path_ops.end_fvertices_of__basic(simple_nonempty_path2)
    if not end_fvertices_0 == end_fvertices_1 == end_fvertices_2: raise CheckNonPlanarConditionValueError('not same end_fvertices')








def _check_distinguish_middle_fvertices(path_ops, simple_nonempty_path0, simple_path1, simple_nonempty_path2, buffer__fvertex_set):
    middle_fvertices_1 = simple_path1.iter_middle_fvertices()
    middle_fvertices_0 = path_ops.iter_middle_fvertices_of__basic(simple_nonempty_path0)
    middle_fvertices_2 = path_ops.iter_middle_fvertices_of__basic(simple_nonempty_path2)

    all_middle_fvertices = chain(middle_fvertices_0, middle_fvertices_1, middle_fvertices_2)
    if not are_distinguish_elements(all_middle_fvertices, buffer__fvertex_set): raise CheckNonPlanarConditionValueError('cross: shared some middle_fvertices')


def _check_end_hedges_embedding_in_same_direction(path_ops, simple_nonempty_path0, simple_path1, simple_nonempty_path2):
    def get_end_hedges(nonempty_path):
        first_hedge = path_ops.first_hedge_of__basic(nonempty_path)
        reversed_last_hedge = path_ops.reversed_last_hedge_of__basic(nonempty_path)
        return first_hedge, reversed_last_hedge

    def is_in_clockwise(hedges1):
        b = is_in_clockwise_around_vertex(hedges1
            , hedge2fake_clockwise_next_hedge_around_vertex
                =path_ops.ugraph_fake_embedding.hedge2fake_clockwise_next_hedge_around_vertex
            )
        return bool(b)

    (first_hedge_0, reversed_last_hedge_0) = get_end_hedges(simple_nonempty_path0)
    (first_hedge_2, reversed_last_hedge_2) = get_end_hedges(simple_nonempty_path2)

    if simple_path1.path:
        (first_hedge_1, reversed_last_hedge_1) = get_end_hedges(simple_path1.path)
        _3_first_hedges = (first_hedge_0, first_hedge_0, first_hedge_2)
        _3_reversed_last_hedges = (reversed_last_hedge_0, reversed_last_hedge_0, reversed_last_hedge_2)

        if not is_in_clockwise(_3_first_hedges) == is_in_clockwise(_3_reversed_last_hedges): raise CheckNonPlanarConditionValueError('3 first_hedges and 3 reversed_last_hedges are not in same clockwise_direction')

    else:
        _4_hedges = (first_hedge_0, first_hedge_2, reversed_last_hedge_0, reversed_last_hedge_2)
        if not (is_in_clockwise(_4_hedges) or is_in_clockwise(reversed(_4_hedges))): raise CheckNonPlanarConditionValueError('simple_path is empty but the 4 first/reversed_last_hedges are not seperate each other')



