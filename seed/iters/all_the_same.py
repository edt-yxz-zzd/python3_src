
__all__ = '''
    all_the_same
    all_equal
    all_the_same_ex
    '''.split()
import operator

def all_equal(start, iterable, *, key=None, __eq__=None):
    if key is not None:
        start = key(start)
        iterable = map(key, iterable)
    if __eq__ is None:
        __eq__ = operator.eq
    return all(__eq__(start, x) for x in iterable)
def all_the_same_ex(iterable, *, default=None, key=None, __eq__=None):
    it = iter(iterable)
    for x in it:break
    else: return (default,)
    return (x,) if all_equal(x, it, key=key, __eq__=__eq__) else ()
def all_the_same(iterable, *, key=None, __eq__=None):
    return bool(all_the_same_ex(iterable, key=key, __eq__=__eq__))

assert all_the_same([]) == True
assert all_the_same([object()]) == True
assert all_the_same([1,object()]) == False
assert all_the_same([1,1]) == True


