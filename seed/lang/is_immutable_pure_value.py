#__all__:goto
r'''[[[
e ../../python3_src/seed/lang/is_immutable_pure_value.py
seed.lang.is_immutable_pure_value

py -m nn_ns.app.debug_cmd   seed.lang.is_immutable_pure_value
py -m seed.lang.is_immutable_pure_value

from seed.lang.is_immutable_pure_value import is_immutable_pure_value


view ../../python3_src/seed/func_tools/recur5yield.py
view ../../python3_src/seed/func_tools/fmapT/TypeBasedDispatcher.py
view ../../python3_src/seed/func_tools/fmapT/TypeBasedFMapT__literal_rebuild.py

from seed.func_tools.recur5yield import recur5yield__list__echo__echo
from seed.func_tools.fmapT.TypeBasedDispatcher import TypeBasedDispatcher, on_type4dispatcherT, on_basetype4dispatcherT, on_type, on_basetype
from seed.func_tools.fmapT.TypeBasedFMapT__literal_rebuild import TypeBasedFMapT__literal_rebuild, literal_rebuild


>>> def mk(T, /):
...     class C(T):
...         __slots__ = 'x'
...     C()
>>> mk(range)
Traceback (most recent call last):
    ...
TypeError: type 'range' is not an acceptable base type
>>> mk(slice)
Traceback (most recent call last):
    ...
TypeError: type 'slice' is not an acceptable base type
>>> mk(type(...))
Traceback (most recent call last):
    ...
TypeError: type 'ellipsis' is not an acceptable base type
>>> mk(type(NotImplemented))
Traceback (most recent call last):
    ...
TypeError: type 'NotImplementedType' is not an acceptable base type
>>> mk(type(None))
Traceback (most recent call last):
    ...
TypeError: type 'NoneType' is not an acceptable base type
>>> mk(bool)
Traceback (most recent call last):
    ...
TypeError: type 'bool' is not an acceptable base type
>>> mk(int)
Traceback (most recent call last):
    ...
TypeError: nonempty __slots__ not supported for subtype of 'int'
>>> mk(float)
>>> mk(complex)
>>> mk(str)
>>> mk(bytes)
Traceback (most recent call last):
    ...
TypeError: nonempty __slots__ not supported for subtype of 'bytes'
>>> mk(tuple)
Traceback (most recent call last):
    ...
TypeError: nonempty __slots__ not supported for subtype of 'tuple'
>>> mk(frozenset)



>>> from collections import namedtuple
>>> B = namedtuple('B', 'xxx yyy')
>>> issubclass(B, tuple)
True
>>> from enum import IntEnum, IntFlag
>>> E = IntEnum('Em', 'iii jjj')
>>> F = IntFlag('Fg', 'aaa bbb')
>>> issubclass(E, int)
True
>>> issubclass(F, int)
True
>>> class Int(int):pass
>>> class Bytes(bytes):pass
>>> class Tuple(tuple):pass
>>> from seed.lang.is_immutable_pure_value import is_immutable_pure_value
>>> is_immutable_pure_value((0, '', (None, False, .5, 1j, b'', frozenset([2]))))
True
>>> is_immutable_pure_value(frozenset([2, B(1,2), E.iii, F.aaa, Int(0), Bytes(), Tuple()]))
True

>>> is_immutable_pure_value((0, '', (None, [])))
False




#]]]'''
__all__ = r'''
    is_immutable_pure_value
'''.split()#'''
__all__




immutable_solid_types = (
    type(None)
    ,type(...)#Ellipsis
    ,type(NotImplemented)
    ,bool
    ,int
    ,str
    ,bytes
    ,float
    ,complex
    ,range
        # arg must be int
    ,)
immutable_container_types = (
    tuple
    ,frozenset
    ,)
immutable_solid_basetypes = (
    int
    ,bytes
    ,)
immutable_container_basetypes = (
    tuple
    ,)


_f = lambda x:(x.start, x.stop, x.step)
assert _f(range(2,3,4)) == (2,3,4)
assert _f(slice(2,3,4)) == (2,3,4)
_xxx_immutable_complex_types = {
    slice:_f
        #TypeError: unhashable type: 'slice'
        #arg can be any thing
    }

r'''[[[
namedtuple <: tuple
not real immutable:
    datetime
    Fraction
    decimal

>>> x._denominator=3
>>> x
Fraction(1, 3)

#]]]'''


def is_immutable_pure_value(obj, /):
    # immutable ==>> DAG
    # no circle
    # tree
    # but subtree may repeat
    s = {*[]}
    ls = []
    def put(x, /):
        if not id(x) in s:
            s.add(id(x))
            ls.append(x)
    put(obj)
    while ls:
        x = ls.pop()
        T = type(x)
        if T in immutable_solid_types or isinstance(x, immutable_solid_basetypes):
            continue
        if T in immutable_container_types or isinstance(x, immutable_container_basetypes):
            for _ in map(put, x):pass
            continue
        return False
    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
