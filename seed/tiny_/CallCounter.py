
r'''
from seed.tiny_.CallCounter import CallCounter

used in:
    seed.algo.merge_sort
        to count how many cmp() called by merge_sort

#'''

class CallCounter:
    def __init__(sf, f, /):
        assert callable(f)
        sf.func = f
        sf.count = 0
    def __call__(sf, /, *args, **kwds):
        sf.count += 1
        return sf.func(*args, **kwds)
from seed.tiny_.CallCounter import CallCounter

