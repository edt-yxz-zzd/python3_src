
#from seed.tiny_.verify import is_iterable, is_iterator, is_reiterable
#from seed.tiny_.verify import type_is, is_str, is_char






__all__ = '''
    is_iterable
    is_iterator
    is_reiterable

    type_is
    is_str
    is_char
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

def type_is(T, x, /):
    return type(x) is T
def is_str(s, /):
    return type_is(str, s)
def is_char(ch, /):
    return is_str(ch) and len(ch)==1


from seed.tiny_.verify import is_iterable, is_iterator, is_reiterable
from seed.tiny_.verify import type_is, is_str, is_char
