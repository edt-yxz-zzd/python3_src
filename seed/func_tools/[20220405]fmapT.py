r'''
py -m nn_ns.app.debug_cmd   seed.func_tools.fmapT
py -m nn_ns.app.debug_cmd   collections.abc

from seed.func_tools.fmapT import fmapT__dict, fmapT__list, fmapT__iter, fmapT__tuple, fmapT__tpls, fmapT__pairs, fmap_rngs2hex_repr
from seed.func_tools.fmapT import literal_rebuild

e ../../python3_src/seed/func_tools/fmapT.py
    简化版 of 设想中的 parameterized_transform.py
see:
    view ../../python3_src/seed/func_tools/parameterized_transform.py
#'''

__all__ = '''
    fmapT__dict
    fmapT__list
    fmapT__iter
    fmapT__tuple
    fmapT__tpls
    fmapT__pairs

    fmap_rngs2hex_repr












    TypeBasedFMapT
    on_type4fmapT
    on_basetype4fmapT
    on_type
    on_basetype
    TypeBasedFMapT__literal_rebuild
    literal_rebuild



    '''.split()

___begin_mark_of_excluded_global_names__0___ = ...
from seed.tiny import fmap4dict_value as _fmapT__dict
from seed.tiny import HexReprInt
from seed.func_tools.dot2 import dot
___end_mark_of_excluded_global_names__0___ = ...

def fmapT__dict(f, /):
    return lambda d, /: _fmapT__dict(f, d)
def fmapT__list(f, /):
    return lambda ls, /: [*map(f, ls)]
def fmapT__iter(f, /):
    return lambda it, /: map(f, it)
def fmapT__tuple(*funcs):
    return lambda tpl, /: _check_len_same(funcs, tpl) or tuple(f(x) for f, x in zip(funcs, tpl))
def _check_len_same(lhs, rhs, /):
    if not len(lhs) == len(rhs):raise TypeError
    return

#fmapT__pairs(f, g, /)
fmapT__tpls = dot[fmapT__list, fmapT__tuple]
fmapT__pairs = fmapT__tpls
fmap_rngs2hex_repr = fmapT__pairs(HexReprInt, HexReprInt)































___begin_mark_of_excluded_global_names__1___ = ...
from seed.abc.abc__ver0 import ABC, abstractmethod, override
from seed.types.attr.IValueAppendDecorator import IValueAppendDecorator, IValueAppendDecorator__fix2, group_by_case_then_attr__IValueAppendDecorator
___end_mark_of_excluded_global_names__1___ = ...


#class Meta4TypeBasedFMapT(type):
class TypeBasedFMapT:
    def __init_subclass__(cls, /, *args, **kwargs):
        case2attr2argss = group_by_case_then_attr__IValueAppendDecorator(IValueAppendDecorator, __class__, cls)
        attr2argss__on_type = case2attr2argss.get('on_type', {})
        attr2argss__on_basetype = case2attr2argss.get('on_basetype', {})
        type2attr = {}
        for attr, argss in attr2argss__on_type.items():
            for [typ] in argss:
                dict_add__eq(type2attr, typ, attr)
        cls.___type2attr4fmapT_handler___ = type2attr

        triple_set = set()
        for attr, argss in attr2argss__on_basetype.items():
            for required_bases, excluded_bases in argss:
                triple_set.add((required_bases, excluded_bases, attr))
        cls.___required_bases_excluded_bases_attr_triple_set4fmapT_handler___ = triple_set
        super(__class__, cls).__init_subclass__(*args, **kwargs)




    def type_based_fmapT(sf, obj, /):
        typ = type(obj)
        cls = type(sf)
        type2attr = cls.___type2attr4fmapT_handler___
        if typ in type2attr:
            attr = type2attr[typ]
            f = getattr(sf, attr)
            return f(obj)

        triple_set = cls.___required_bases_excluded_bases_attr_triple_set4fmapT_handler___
        attrs = {attr
            for required_bases, excluded_bases, attr in triple_set
            if all(issubclass(typ, basecls) for basecls in required_bases)
            and all(not issubclass(typ, basecls) for basecls in excluded_bases)
            }

        if not attrs:
            return sf.fallback_fmapT(obj)
        if len(attrs) > 1:
            raise TypeError(f'more than 1 attr-name matched: {attrs!r}')
        [attr] = attrs
        f = getattr(sf, attr)
        return f(obj)

    def fallback_fmapT(sf, obj, /):
        typ = type(obj)
        cls = type(sf)
        raise NotImplementedError(f'{cls.__name__}.fallback_fmapT: {obj!r}')

class on_type4fmapT(IValueAppendDecorator__fix2):
    # @override
    ___symbol8lord___ = TypeBasedFMapT
    # @override
    ___case4option___ = 'on_type'
    @override
    def check_args4case(sf, typ, /):
        if not isinstance(typ, type): raise TypeError
class on_basetype4fmapT(IValueAppendDecorator__fix2):
    # @override
    ___symbol8lord___ = TypeBasedFMapT
    # @override
    ___case4option___ = 'on_basetype'
    @override
    def standardize_args4case(sf, required_bases, excluded_bases, /):
        return frozenset(required_bases), frozenset(excluded_bases)
    @override
    def check_args4case(sf, required_bases, excluded_bases, /):
        if not all(isinstance(typ, type) for typ in required_bases): raise TypeError
        if not all(isinstance(typ, type) for typ in excluded_bases): raise TypeError
on_type = on_type4fmapT
on_basetype = on_basetype4fmapT









r'''[[
___type4fmapT_handler___ = '___type4fmapT_handler___'
___basetype4fmapT_handler___ = '___basetype4fmapT_handler___'
def _on_xxx(attr, val, /):
    def _(f, /):
        setattr(f, attr, val)
    return _
def on_type(types, /):
    types = [*types]
    assert isinstance(cls, type)
    return _on_xxx(___type4fmapT_handler___, cls)
def on_basetype(required_bases, excluded_bases, /):
    assert isinstance(basecls, type)
    return _on_xxx(___basetype4fmapT_handler___, basecls)
def collect_fmapT_handler(attr, cls, /):
    type2name = {getattr(f, attr): nm for nm, f in cls.__dict__.items() if hasattr(f, attr) and type(nm) is str and nm.isidentifier()}
        #??OrderDict??metaclass.__prepare__??
        #   [(type, attr)]???
    return (type2name)
    #return MapView(type2name)
class TypeBasedFMapT:
    def __init_subclass__(cls, /, *args, **kwargs):
        cls.___type2attr4fmapT_handler___ = collect_fmapT_handler(___type4fmapT_handler___, cls)
        cls.___basetype2attr4fmapT_handler___ = collect_fmapT_handler(___basetype4fmapT_handler___, cls)
        super(__class__, cls).__init_subclass__(*args, **kwargs)


#]]'''











___begin_mark_of_excluded_global_names__2___ = ...
#from collections.abc import Set, Sequence, Mapping, ByteString, String
#   no-String!!!
from collections.abc import Set, MutableSet, Mapping, MutableMapping, Sequence, MutableSequence, ByteString


from seed.tiny import expectError, dict_add__eq
import ast
from seed.helper.stable_repr import stable_repr
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

class TypeBasedFMapT__literal_rebuild(TypeBasedFMapT):
    r'''
    #'''

    r'''
    @on_basetype([x], [])
    def on_x(sf, obj, /):
        f = sf.type_based_fmapT
        return fmapT__y(f)(obj)
    @on_type(x)
    def on_x(sf, obj, /):
        return obj
        f = sf.type_based_fmapT
        return fmapT__y(f)(obj)
    #'''

    @on_basetype([Mapping], [])
    def on_Mapping(sf, obj, /):
        f = sf.type_based_fmapT
        return fmapT__dict(f)(obj)

    #@on_basetype([Sequence], [String, ByteString])
    @on_basetype([Sequence], [MutableSequence, ByteString])
    @on_type(tuple)
    def on_Sequence(sf, obj, /):
        f = sf.type_based_fmapT
        return tuple(map(f, obj))
        return fmapT__tuple(f)(obj)#bug! length-tuple, _check_len_same
    @on_basetype([MutableSequence], [ByteString])
    @on_type(list)
    def on_MutableSequence(sf, obj, /):
        f = sf.type_based_fmapT
        return fmapT__list(f)(obj)
    @on_basetype([Set], [])
    @on_type(set)
    @on_type(frozenset)
    def on_Set(sf, obj, /):
        f = sf.type_based_fmapT
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
literal_rebuild = TypeBasedFMapT__literal_rebuild().type_based_fmapT


assert stable_repr(literal_rebuild([MappingProxyType({3:(4, None, True), 5:'cd', 7:bytearray(b'abc'), 8:frozenset()})])) == "[{3: (4, None, True), 5: 'cd', 7: b'abc', 8: set()}]"


