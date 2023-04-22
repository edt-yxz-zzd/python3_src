#__all__:goto
r'''[[[
e ../../python3_src/seed/tiny_/CompactData.py
come from:
    view ../../python3_src/seed/graph/DGraph4GrowingOnly.py
        class _Data

seed.tiny_.CompactData
py -m nn_ns.app.debug_cmd seed.tiny_.CompactData
py -m seed.tiny_.CompactData


from seed.tiny_.CompactData import Base4CompactData, mk_CompactDataType, mk_CompactDataType_then_write_to_module




>>> from seed.tiny_.CompactData import Base4CompactData, mk_CompactDataType, mk_CompactDataType_then_write_to_module


>>> class C:
...   class D:pass
...
>>> C.D.__qualname__
'C.D'
>>> C.D.__module__
'__main__'

>>> T = mk_CompactDataType(__slots__='x y z', __module__='ppp.kkk', __qualname__='a.b')
>>> T
<class 'ppp.kkk.a.b'>
>>> T.__module__
'ppp.kkk'
>>> T.__qualname__
'a.b'
>>> T.__name__
'b'
>>> T()
a.b()
>>> T(x=1,y=2)
a.b(x=1, y=2)
>>> T(z=1)
a.b(z=1)
>>> T(a=1)
Traceback (most recent call last):
    ...
AttributeError: 'b' object has no attribute 'a'



>>> mk_CompactDataType_then_write_to_module('a.b', 'kkk', 'x y z')
Traceback (most recent call last):
    ...
ModuleNotFoundError: No module named 'kkk'
>>> mk_CompactDataType_then_write_to_module('a.b', '__main__', 'x y z')
Traceback (most recent call last):
    ...
AttributeError: module '__main__' has no attribute 'a'

>>> mk_CompactDataType_then_write_to_module('a', '__main__', 'x y z')
>>> mk_CompactDataType_then_write_to_module('a', '__main__', 'x y z')
Traceback (most recent call last):
    ...
AttributeError: __main__::a existed
>>> mk_CompactDataType_then_write_to_module('a.b', '__main__', 'x y z')
>>> mk_CompactDataType_then_write_to_module('a.b', globals(), 'x y z')
Traceback (most recent call last):
    ...
AttributeError: __main__::a.b existed

#]]]'''
__all__ = r'''
    Base4CompactData
    mk_CompactDataType
    mk_CompactDataType_then_write_to_module
'''.split()#'''
__all__

import importlib
#importlib.import_module(name, package=None)


class Base4CompactData:
    __slots__ = ()
    def __init__(sf, /, **kw):
        for nm, v in sorted(kw.items()):
            #sorted() to shared keys
            setattr(sf, nm, v)
    def __repr__(sf, /):
        cls = type(sf)
        nms = [nm for nm in cls.__0_slots_0__ if hasattr(sf, nm)]
        s = ', '.join(f'{nm!s}={getattr(sf,nm)!r}' for nm in nms)
        tynm = cls.__qualname__
        return f'{tynm!s}({s!s})'



def mk_CompactDataType_then_write_to_module(__qualname__, module_name_or_globals, __slots__, /):
    if type(module_name_or_globals) is str:
        __module__ = module_name_or_globals
    else:
        globals = module_name_or_globals
        __module__ = globals['__name__']
    module_obj = importlib.import_module(__module__)

    [*nms,name4cls] = __qualname__.split('.')
    obj = module_obj
    for nm in nms:
        obj = getattr(obj, nm)
    if hasattr(obj, name4cls): raise AttributeError(f'{__module__!s}::{__qualname__!s} existed')

    cls = mk_CompactDataType(__slots__=__slots__, __module__=__module__, __qualname__=__qualname__)

    setattr(obj, name4cls, cls)
    return None
    return cls

def mk_CompactDataType(*, __slots__, __module__, __qualname__):
    if type(__slots__) is not str: raise TypeError
    if type(__module__) is not str: raise TypeError
    if type(__qualname__) is not str: raise TypeError
    __slots__ = tuple(__slots__.split())
    #return type(__qualname__, (Base4CompactData,), dict(__slots__=__slots__, __module__=__module__, __0_slots_0__=__slots__))
    #   ==>> __name__ will contain '.' !!!
    #
    _,_,name4cls = __qualname__.rpartition('.')
    return type(name4cls, (Base4CompactData,), dict(__slots__=__slots__, __module__=__module__, __qualname__=__qualname__, __0_slots_0__=__slots__))

from seed.tiny_.CompactData import Base4CompactData, mk_CompactDataType, mk_CompactDataType_then_write_to_module
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +IGNORE_EXCEPTION_DETAIL

