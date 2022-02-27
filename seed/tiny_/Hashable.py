
__all__ = '''
    check_Hashable__shallow
    is_Hashable__shallow
    check_Hashable__deep
    is_Hashable__deep
    '''.split()

#from seed.tiny_.Hashable import check_Hashable__shallow, is_Hashable__shallow, check_Hashable__deep, is_Hashable__deep
from collections.abc import Hashable


def check_Hashable__shallow(obj, /):
    if not is_Hashable__shallow(obj): raise TypeError
def is_Hashable__shallow(obj, /):
    return isinstance(obj, Hashable)

def check_Hashable__deep(obj, /):
    hash(obj)#TypeError
def is_Hashable__deep(obj, /):
    try:
        check_Hashable__deep(obj)#TypeError
    except TypeError:
        return False
    return True

assert not is_Hashable__deep((1, []))
assert is_Hashable__shallow((1, []))


assert is_Hashable__deep(frozenset())
assert is_Hashable__deep(())
assert is_Hashable__deep((1, False))
assert not is_Hashable__deep([])
assert not is_Hashable__deep({})

assert is_Hashable__shallow(frozenset())
assert is_Hashable__shallow(())
assert is_Hashable__shallow((1, False))
assert not is_Hashable__shallow([])
assert not is_Hashable__shallow({})
