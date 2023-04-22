

__all__ = '''
    is_iterable
    is_iterator
    is_reiterable

    type_is
    is_str
    is_char

    is_callable
    is_subscriptable
    is_container
    is_sized
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


r'''
subscriptable/callable/container/iterable/iterator/reiterable/sized/hashable
  is_subscriptable
  check_subscriptable
xxx is_hashable
    see:
        from seed.tiny_.Hashable import check_Hashable__shallow, is_Hashable__shallow, check_Hashable__deep, is_Hashable__deep
py -m nn_ns.app.debug_cmd   seed.tiny_.verify -x

'''#'''

is_callable = callable
def is_subscriptable(x, /):
    cls = type(x)
    return hasattr(cls, '__getitem__')
def is_container(x, /):
    cls = type(x)
    return hasattr(cls, '__contains__')
def is_sized(x, /):
    cls = type(x)
    return hasattr(cls, '__len__')
#xxx is_hashable


from seed.tiny_.verify import is_iterable, is_iterator, is_reiterable
from seed.tiny_.verify import type_is, is_str, is_char
from seed.tiny_.verify import is_callable, is_subscriptable, is_container, is_sized
from seed.tiny_.verify import *
