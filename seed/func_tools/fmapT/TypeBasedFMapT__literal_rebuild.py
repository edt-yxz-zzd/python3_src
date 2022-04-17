#__all__:goto
#main_body_src_code:goto
#HHHHH
#[[[__doc__:begin
r'''
seed.func_tools.fmapT.TypeBasedFMapT__literal_rebuild
py -m    seed.func_tools.fmapT.TypeBasedFMapT__literal_rebuild
py -m nn_ns.app.debug_cmd   seed.func_tools.fmapT.TypeBasedFMapT__literal_rebuild

from seed.func_tools.fmapT.TypeBasedFMapT__literal_rebuild import TypeBasedFMapT__literal_rebuild, literal_rebuild

#[[[doc_sections:begin
#doctest_examples:goto
#wwwzzz:goto

#[[[doctest_examples:begin
>>>
...
#]]]doctest_examples:end

#[[[wwwzzz:begin
#]]]wwwzzz:end
#]]]doc_sections:end


#'''
#]]]__doc__:end

#################################
#HHHHH
__all__ = '''
    TypeBasedFMapT__literal_rebuild
    literal_rebuild

    '''.split()

#################################
#HHHHH
___begin_mark_of_excluded_global_names__2___ = ...
#from collections.abc import Set, Sequence, Mapping, ByteString, String
#   no-String!!!
from collections.abc import Set, MutableSet, Mapping, MutableMapping, Sequence, MutableSequence, ByteString


from seed.func_tools.fmapT.fmapT__tiny import fmapT__dict, fmapT__list, fmapT__tuple
from seed.tiny import expectError
import ast
from seed.helper.stable_repr import stable_repr
from seed.func_tools.fmapT.TypeBasedDispatcher import TypeBasedDispatcher, on_type, on_basetype
if 0:
    #for literal_eval-supported builtin type only
    r'''
        py_eval -i 'Ellipsis'
        py_literal_eval -i 'Ellipsis'
    from seed.helper.repr_input import repr_helper
    from seed.types.view.RecurView import default_cfg4RecurView

    from fractions import Fraction
    from decimal import Decimal
    from numbers import Number
    from array import array as WordArray
    import datetime
    import time
    from pathlib import PurePath
    from types import MappingProxyType
    #'''
from types import MappingProxyType
___end_mark_of_excluded_global_names__2___ = ...


#HHHHH
#[[[main_body_src_code:begin
#zzzwww:goto

#[[[zzzwww:begin
class TypeBasedFMapT__literal_rebuild(TypeBasedDispatcher):
    r'''
    #'''

    r'''
    @on_basetype([x], [])
    def on_x(sf, obj, /):
        f = sf.type_based_dispatcherT
        return fmapT__y(f)(obj)
    @on_type(x)
    def on_x(sf, obj, /):
        return obj
        f = sf.type_based_dispatcherT
        return fmapT__y(f)(obj)
    #'''

    @on_basetype([Mapping], [])
    def on_Mapping(sf, obj, /):
        f = sf.type_based_dispatcherT
        return fmapT__dict(f)(obj)

    #@on_basetype([Sequence], [String, ByteString])
    @on_basetype([Sequence], [MutableSequence, ByteString])
    @on_type(tuple)
    def on_Sequence(sf, obj, /):
        f = sf.type_based_dispatcherT
        return tuple(map(f, obj))
        return fmapT__tuple(f)(obj)#bug! length-tuple, _check_len_same
    @on_basetype([MutableSequence], [ByteString])
    @on_type(list)
    def on_MutableSequence(sf, obj, /):
        f = sf.type_based_dispatcherT
        return fmapT__list(f)(obj)
    @on_basetype([Set], [])
    @on_type(set)
    @on_type(frozenset)
    def on_Set(sf, obj, /):
        f = sf.type_based_dispatcherT
        return set(obj)#mimic fmapT__dict, key-not-changed!!!
        return set(map(f, obj))
    r'''
    @on_basetype([String], [])
    def on_String(sf, obj, /):
        return str(obj)
    #'''
    @on_basetype([ByteString], [])
    @on_type(bytearray)
    def on_ByteString(sf, obj, /):
        return bytes(obj)


    @on_type(bool)
    @on_type(int)
    @on_type(float)
    @on_type(complex)
    @on_type(str)
    @on_type(bytes)
    @on_type(type(None))
    #for literal_eval-supported builtin type only
        #@on_type(type(...))
        #@on_type(type(Ellipsis))
        #@on_type(type(NotImplemented))
    def on_solid_immutable__echo(sf, obj, /):
        return obj
    assert expectError(ValueError, lambda:ast.literal_eval('Ellipsis'))
    assert expectError(ValueError, lambda:ast.literal_eval('NotImplemented'))
        #ValueError: malformed node or string: <_ast.Name object at 0xb6447028>
    assert ast.literal_eval('...') is Ellipsis
    #help(ast.literal_eval)
    r'''
literal_eval(node_or_string)
    Safely evaluate an expression node or a string containing a Python expression.

    The string or node provided may only consist of the following Python literal structures:
        strings, bytes, numbers, tuples, lists, dicts, sets, booleans, and None.
    #'''
literal_rebuild = TypeBasedFMapT__literal_rebuild().type_based_dispatcherT


assert stable_repr(literal_rebuild([MappingProxyType({3:(4, None, True), 5:'cd', 7:bytearray(b'abc'), 8:frozenset()})])) == "[{3: (4, None, True), 5: 'cd', 7: b'abc', 8: set()}]"


#]]]zzzwww:end
#]]]main_body_src_code:end


#HHHHH
if __name__ == "__main__":
    from seed.func_tools.fmapT.TypeBasedFMapT__literal_rebuild import *
    from seed.func_tools.fmapT.TypeBasedFMapT__literal_rebuild import TypeBasedFMapT__literal_rebuild, literal_rebuild
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #<BLANKLINE>
    #Traceback (most recent call last):


