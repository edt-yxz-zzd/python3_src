
#e ../../python3_src/seed/tiny_/iter_stop_with_.py
__all__ = r'''
    iter_stop_with_
    GetStopIterationValue
    '''.split()#'''

def iter_stop_with_(r, it, /):
    it = iter(it)
    return _iter_stop_with_(r, it)
def _iter_stop_with_(r, it, /):
    yield from it
    return r
class GetStopIterationValue:
    def __init__(sf, it, /):
        sf._it = iter(it)
        sf._tmay = ()
    def __iter__(sf, /):
        if sf._tmay:
            return
        try:
            #bug:yield from sf._it
            while 1:
                yield next(sf._it)
        except StopIteration as e:
            if sf._tmay:
                # reenter
                return
            sf._tmay = (e.value,)
            return
        raise 000
    def get_iterator(sf, /):
        return sf._it
    def get_tmay_value5StopIteration(sf, /):
        return sf._tmay

assert not list(_:=GetStopIterationValue(iter_stop_with_(..., []))) and _.get_tmay_value5StopIteration() == (...,)
assert all((_:=GetStopIterationValue(iter_stop_with_(..., [1,2,3])), _it1:=iter(_), _it2:=iter(_), [next(_it1) == 1, next(_it2) == 2, next(_it1) == 3, _.get_tmay_value5StopIteration() == (), next(_it1, 666) == 666, _.get_tmay_value5StopIteration() == (...,), next(_it2, 999) == 999, _.get_tmay_value5StopIteration() == (...,)])[-1])
from seed.tiny_.iter_stop_with_ import iter_stop_with_, GetStopIterationValue
from seed.tiny_.iter_stop_with_ import *

