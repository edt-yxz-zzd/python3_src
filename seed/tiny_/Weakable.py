
__all__ = '''
    check_Weakable
    is_Weakable
    WeakableDict
    '''.split()

#from seed.tiny_.Weakable import check_Weakable, is_Weakable, WeakableDict
import weakref

r'''
class Weakable:
    __slots__ = '__weakref__'
#'''

def check_Weakable(obj, /):
    weakref.ref(obj)#TypeError

def is_Weakable(obj, /):
    try:
        weakref.ref(obj)#TypeError
    except TypeError:
        return False
    return True

class WeakableDict(dict):
    __slots__ = '__weakref__'

assert is_Weakable(frozenset())
assert is_Weakable(set())
assert not is_Weakable(())
assert not is_Weakable([])
assert not is_Weakable({})
assert not is_Weakable(dict())
assert is_Weakable(WeakableDict())

