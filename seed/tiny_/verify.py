
#from seed.tiny_.verify import is_iterable, is_iterator, is_reiterable

__all__ = '''
    is_iterable
    is_iterator
    is_reiterable
    '''.split()

from collections.abc import Iterable, Iterator

def is_iterable(x, /):
    if not isinstance(x, Iterable): return False
    return iter(x) is not None
def is_iterator(x, /):
    if not isinstance(x, Iterator): return False
    return iter(x) is x
def is_reiterable(x, /):
    return is_iterable(x) and not is_iterator(x)


