#__all__:goto
#main_body_src_code:goto
#HHHHH
#[[[__doc__:begin
r'''
seed.func_tools.fmapT.TypeBasedDispatcher
py -m    seed.func_tools.fmapT.TypeBasedDispatcher
py -m nn_ns.app.debug_cmd   seed.func_tools.fmapT.TypeBasedDispatcher

from seed.func_tools.fmapT.TypeBasedDispatcher import TypeBasedDispatcher, on_type4dispatcherT, on_basetype4dispatcherT, on_type, on_basetype

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
    TypeBasedDispatcher
    on_type4dispatcherT
    on_basetype4dispatcherT
    on_type
    on_basetype

    '''.split()

#################################
#HHHHH
___begin_mark_of_excluded_global_names__1___ = ...
from seed.abc.abc__ver0 import ABC, abstractmethod, override
from seed.types.attr.IValueAppendDecorator import IValueAppendDecorator, IValueAppendDecorator__fix2, group_by_case_then_attr__IValueAppendDecorator
from seed.tiny import dict_add__eq

___end_mark_of_excluded_global_names__1___ = ...

#HHHHH
#[[[main_body_src_code:begin
#zzzwww:goto

#[[[zzzwww:begin


#class Meta4TypeBasedDispatcher(type):
class TypeBasedDispatcher:
    def __init_subclass__(cls, /, *args, **kwargs):
        case2attr2argss = group_by_case_then_attr__IValueAppendDecorator(IValueAppendDecorator, __class__, cls)
        attr2argss__on_type = case2attr2argss.get('on_type', {})
        attr2argss__on_basetype = case2attr2argss.get('on_basetype', {})
        type2attr = {}
        for attr, argss in attr2argss__on_type.items():
            for [typ] in argss:
                dict_add__eq(type2attr, typ, attr)
        cls.___type2attr4dispatcherT_handler___ = type2attr

        triple_set = set()
        for attr, argss in attr2argss__on_basetype.items():
            for required_bases, excluded_bases in argss:
                triple_set.add((required_bases, excluded_bases, attr))
        cls.___required_bases_excluded_bases_attr_triple_set4dispatcherT_handler___ = triple_set
        super(__class__, cls).__init_subclass__(*args, **kwargs)




    def type_based_dispatcherT(sf, obj, /):
        typ = type(obj)
        cls = type(sf)
        type2attr = cls.___type2attr4dispatcherT_handler___
        if typ in type2attr:
            attr = type2attr[typ]
            f = getattr(sf, attr)
            return f(obj)

        triple_set = cls.___required_bases_excluded_bases_attr_triple_set4dispatcherT_handler___
        attrs = {attr
            for required_bases, excluded_bases, attr in triple_set
            if all(issubclass(typ, basecls) for basecls in required_bases)
            and all(not issubclass(typ, basecls) for basecls in excluded_bases)
            }

        if not attrs:
            return sf.fallback_dispatcherT(obj)
        if len(attrs) > 1:
            raise TypeError(f'more than 1 attr-name matched: {attrs!r}')
        [attr] = attrs
        f = getattr(sf, attr)
        return f(obj)

    def fallback_dispatcherT(sf, obj, /):
        typ = type(obj)
        cls = type(sf)
        raise NotImplementedError(f'{cls.__name__}.fallback_dispatcherT: {obj!r}')

class on_type4dispatcherT(IValueAppendDecorator__fix2):
    # @override
    ___symbol8lord___ = TypeBasedDispatcher
    # @override
    ___case4option___ = 'on_type'
    @override
    def check_args4case(sf, typ, /):
        if not isinstance(typ, type): raise TypeError
class on_basetype4dispatcherT(IValueAppendDecorator__fix2):
    # @override
    ___symbol8lord___ = TypeBasedDispatcher
    # @override
    ___case4option___ = 'on_basetype'
    @override
    def standardize_args4case(sf, required_bases, excluded_bases, /):
        return frozenset(required_bases), frozenset(excluded_bases)
    @override
    def check_args4case(sf, required_bases, excluded_bases, /):
        if not all(isinstance(typ, type) for typ in required_bases): raise TypeError
        if not all(isinstance(typ, type) for typ in excluded_bases): raise TypeError
on_type = on_type4dispatcherT
on_basetype = on_basetype4dispatcherT


#]]]zzzwww:end






#[[[old_version:begin

r'''[[
___type4dispatcherT_handler___ = '___type4dispatcherT_handler___'
___basetype4dispatcherT_handler___ = '___basetype4dispatcherT_handler___'
def _on_xxx(attr, val, /):
    def _(f, /):
        setattr(f, attr, val)
    return _
def on_type(types, /):
    types = [*types]
    assert isinstance(cls, type)
    return _on_xxx(___type4dispatcherT_handler___, cls)
def on_basetype(required_bases, excluded_bases, /):
    assert isinstance(basecls, type)
    return _on_xxx(___basetype4dispatcherT_handler___, basecls)
def collect_dispatcherT_handler(attr, cls, /):
    type2name = {getattr(f, attr): nm for nm, f in cls.__dict__.items() if hasattr(f, attr) and type(nm) is str and nm.isidentifier()}
        #??OrderDict??metaclass.__prepare__??
        #   [(type, attr)]???
    return (type2name)
    #return MapView(type2name)
class TypeBasedDispatcher:
    def __init_subclass__(cls, /, *args, **kwargs):
        cls.___type2attr4dispatcherT_handler___ = collect_dispatcherT_handler(___type4dispatcherT_handler___, cls)
        cls.___basetype2attr4dispatcherT_handler___ = collect_dispatcherT_handler(___basetype4dispatcherT_handler___, cls)
        super(__class__, cls).__init_subclass__(*args, **kwargs)


#]]'''
#]]]old_version:end



#]]]main_body_src_code:end


#HHHHH
if __name__ == "__main__":
    from seed.func_tools.fmapT.TypeBasedDispatcher import *
    from seed.func_tools.fmapT.TypeBasedDispatcher import TypeBasedDispatcher, on_type4dispatcherT, on_basetype4dispatcherT, on_type, on_basetype
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #<BLANKLINE>
    #Traceback (most recent call last):


