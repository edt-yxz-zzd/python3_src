
__all__ = r'''
next__tmay
next_
    StopIterationError
'''.split()#'''
__all__

def next__tmay(iterator, /):
    try:
        return (next(iterator),)
    except StopIteration:
        return ()
    Nothing = []
    m = next(iterator, Nothing)
    if m is Nothing:
        tmay = ()
    else:
        value = m
        tmay = (value,)
    return tmay
head__tmay = next__tmay
safe_head = head__tmay

assert () == next__tmay(iter([]))
assert (9,) == next__tmay(iter([9,5]))

class StopIterationError(BaseException):pass
def next_(iterator, /):
    try:
        return next(iterator)
    except StopIteration as exc:
        raise StopIterationError(exc)
        raise StopIterationError(exc.value)
def __():
    def __():
        return 999;yield
    try:
        next_(__())
    except StopIterationError as e:
        [exc] = e.args
        assert 999 == exc.value
    else:
        raise 000
__()





from seed.for_libs.next__tmay import next__tmay, next_, StopIterationError
from seed.for_libs.next__tmay import *
