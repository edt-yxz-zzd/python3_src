
__all__ = '''
    is_in_clockwise_around_vertex
    '''.split()

from ..iter_cycle_from import iter_cycle_from
def is_in_clockwise_around_vertex(hedges1, *
    ,hedge2fake_clockwise_next_hedge_around_vertex
    ):
    #hedges1 = tuple(hedges1)
    #if not hedges1: raise ValueError

    it = iter(hedges1)
    for hedge_to_find in it:
        break
    else:
        raise ValueError('hedges1 is empty')

    for hedge in iter_cycle_from(hedge2fake_clockwise_next_hedge_around_vertex, hedge_to_find):
        if hedge == hedge_to_find:
            for hedge_to_find in it:
                break
            else:
                break
    else:
        return False
    return True


