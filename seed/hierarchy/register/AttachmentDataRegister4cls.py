#__all__:goto
#main_body_src_code:goto
#HHHHH
#[[[__doc__:begin
r'''
seed.hierarchy.register.AttachmentDataRegister4cls
py -m    seed.hierarchy.register.AttachmentDataRegister4cls
py -m nn_ns.app.debug_cmd   seed.hierarchy.register.AttachmentDataRegister4cls

ls ../../python3_src/seed/
mkdir -p ../../python3_src/seed/hierarchy/register/
py -m nn_ns.app.mk_py_template -o ../../python3_src/seed/hierarchy/register/AttachmentDataRegister4cls.py
e ../../python3_src/seed/hierarchy/register/AttachmentDataRegister4cls.py


from seed.hierarchy.register.AttachmentDataRegister4cls import attachment_data_register4cls, mk_private_attr, mk_private_attr__using_permanent_objs_as_path, IHandler4AttachmentDataRegister4cls, default_handler4AttachmentDataRegister4cls, FunctionalHandler4AttachmentDataRegister4cls, mk_FunctionalHandler4AttachmentDataRegister4cls__human

from seed.hierarchy.register.AttachmentDataRegister4cls import AttachmentMutableDictRegister4cls, attachment_mutable_dict_register4cls, AttachmentDataRegister4cls, attachment_data_register4cls, mk_private_attr, mk_private_attr__using_permanent_objs_as_path, IHandler4AttachmentDataRegister4cls, DefaultHandler4AttachmentDataRegister4cls, default_handler4AttachmentDataRegister4cls, FunctionalHandler4AttachmentDataRegister4cls, mk_FunctionalHandler4AttachmentDataRegister4cls__human, default_FunctionalHandler4AttachmentDataRegister4cls



#[[[doc_sections:begin
#doctest_examples:goto
#wwwzzz:goto

#[[[doctest_examples:begin

# NOTE: ???where attachment_mutable_dict_register4cls???
    __main__ vs seed.hierarchy.register.AttachmentDataRegister4cls
>>> from seed.hierarchy.register.AttachmentDataRegister4cls import attachment_mutable_dict_register4cls
>>> from seed.hierarchy.register.AttachmentDataRegister4cls import attachment_data_register4cls, IHandler4AttachmentDataRegister4cls, default_handler4AttachmentDataRegister4cls, FunctionalHandler4AttachmentDataRegister4cls
>>> from seed.hierarchy.symbol.PrivateSymbol import PrivateSymbol

>>> handler = default_handler4AttachmentDataRegister4cls
>>> data = object()
>>> args = (111, 999)
>>> kwargs = dict(a=111, b=999)
>>> register4cls = attachment_data_register4cls






>>> cls = object
>>> symbol = []
>>> symbol2 = []

doctest_examples__snippet
{doctest_examples__snippet4object}

>>> class X:pass
>>> cls = X
>>> symbol = PrivateSymbol('tmp')
>>> symbol2 = PrivateSymbol('tmp')

doctest_examples__snippet
{doctest_examples__snippet4X}


#################################
#################################
#################################
#################################


>>> dict_register4cls = attachment_mutable_dict_register4cls

>>> dict_register4cls.detect_attachment_mutable_dict4cls(str)
False
>>> dict_register4cls.register_attachment_mutable_dict4cls(str)
>>> dict_register4cls.detect_attachment_mutable_dict4cls(str)
True
>>> dict_register4cls.register_attachment_mutable_dict4cls(str)
Traceback (most recent call last):
    ...
LookupError: cls registered: cls=<class 'str'>

>>> dict_register4cls.detect_attachment_mutable_dict4cls(PrivateSymbol)
False
>>> dict_register4cls.register_attachment_mutable_dict4cls(PrivateSymbol)
Traceback (most recent call last):
    ...
TypeError: cls.__setattr__ allowed: cls=<class 'seed.hierarchy.symbol.PrivateSymbol.PrivateSymbol'>

>>> dict_register4cls.register_attachment_mutable_dict4cls(1)
Traceback (most recent call last):
    ...
TypeError: cannot create weak reference to 'int' object
>>> dict_register4cls.register_attachment_mutable_dict4cls(set())
Traceback (most recent call last):
    ...
TypeError: descriptor '__getattribute__' requires a 'type' object but received a 'set'





>>> dict_register4cls.detect_attachment_mutable_dict4cls(object)
True
>>> dict_register4cls.register_attachment_mutable_dict4cls(object)
Traceback (most recent call last):
    ...
LookupError: cls registered: cls=<class 'object'>




#]]]doctest_examples:end

#[[[wwwzzz:begin
#]]]wwwzzz:end
#]]]doc_sections:end


#'''

_doctest_examples__snippet = r'''

#[[[doctest_examples__snippet:begin

>>> register4cls.detect_handler4symbol(symbol)
False
>>> register4cls.detect_handler4symbol(symbol2)
False
>>> register4cls.register_handler4symbol(symbol, handler)
>>> register4cls.register_handler4symbol(symbol, handler)
Traceback (most recent call last):
    ...
LookupError: handler registered for symbol={symbol!s}
>>> register4cls.detect_handler4symbol(symbol)
True
>>> register4cls.detect_handler4symbol(symbol2)
False
>>> register4cls.get_handler4symbol(symbol) is handler
True
>>> register4cls.get_handler4symbol(symbol2)
Traceback (most recent call last):
    ...
LookupError: no registered handler: symbol={symbol!s}



>>> register4cls.detect_data4cls(cls, symbol)
False
>>> register4cls.detect_data4cls(cls, symbol2)
Traceback (most recent call last):
    ...
LookupError: no registered handler: symbol={symbol!s}
>>> register4cls.get_data4cls(cls, symbol)
Traceback (most recent call last):
    ...
LookupError: no registered data: cls={cls!s}; symbol={symbol!s}


>>> attachment_mutable_dict_register4cls.detect_attachment_mutable_dict4cls(cls)
False
>>> register4cls.register_data4cls(cls, symbol, data)
>>> attachment_mutable_dict_register4cls.detect_attachment_mutable_dict4cls(cls)
{is_external_d4cls!r}
>>> register4cls.register_data4cls(cls, symbol, data)
Traceback (most recent call last):
    ...
LookupError: data registered for cls={cls!s}; symbol={symbol!s}

>>> register4cls.detect_data4cls(cls, symbol)
True
>>> register4cls.detect_data4cls(cls, symbol2)
Traceback (most recent call last):
    ...
LookupError: no registered handler: symbol={symbol!s}

>>> register4cls.get_data4cls(cls, symbol) is data
True
>>> register4cls.get_data4cls(cls, symbol2)
Traceback (most recent call last):
    ...
LookupError: no registered handler: symbol={symbol!s}


>>> register4cls.get_data_ex4cls(cls, symbol) == (handler, data)
True
>>> register4cls.get_and_explain_data4cls(cls, symbol, *args, **kwargs) == (handler, register4cls, cls, symbol, data, args, kwargs)
True









#]]]doctest_examples__snippet:end


#'''
__doc__ = __doc__.format(
    doctest_examples__snippet4X=_doctest_examples__snippet.format(
        cls=f"<class '{__name__!s}.X'>", symbol="PrivateSymbol('tmp')", is_external_d4cls=False)
    ,doctest_examples__snippet4object=_doctest_examples__snippet.format(
        cls="<class 'object'>", symbol="[]", is_external_d4cls=True)
    )
#]]]__doc__:end

#################################
#HHHHH
__all__ = '''
    attachment_data_register4cls
        mk_private_attr
            mk_private_attr__using_permanent_objs_as_path
    IHandler4AttachmentDataRegister4cls
        default_handler4AttachmentDataRegister4cls
        FunctionalHandler4AttachmentDataRegister4cls
            mk_FunctionalHandler4AttachmentDataRegister4cls__human






    AttachmentMutableDictRegister4cls
        attachment_mutable_dict_register4cls

    AttachmentDataRegister4cls
        attachment_data_register4cls
        mk_private_attr
            mk_private_attr__using_permanent_objs_as_path

    IHandler4AttachmentDataRegister4cls
        DefaultHandler4AttachmentDataRegister4cls
            default_handler4AttachmentDataRegister4cls
        FunctionalHandler4AttachmentDataRegister4cls
            mk_FunctionalHandler4AttachmentDataRegister4cls__human
            default_FunctionalHandler4AttachmentDataRegister4cls
    '''.split()

#################################
#HHHHH
___begin_mark_of_excluded_global_names__0___ = ...
from seed.types.mapping.Mapping__permanent__weakref import PermanentKeyRefDict, WeakKeyRefDict#, PermanentKeyRefSet, WeakKeyRefSet
from seed.tiny import expectError #echo, print_err, mk_fprint, mk_assert_eq_f
from types import MappingProxyType
import weakref
from seed.abc.abc__ver1 import ABCMeta, abstractmethod, override, ABC, ABC__no_slots
#from collections.abc import Mapping, Set
import operator

r"""
import ...
#"""
___end_mark_of_excluded_global_names__0___ = ...

#HHHHH
#[[[main_body_src_code:begin
#AttachmentMutableDictRegister4cls:goto
#IHandler4AttachmentDataRegister4cls:goto
#AttachmentDataRegister4cls:goto
#zzzwww:goto

#[[[AttachmentMutableDictRegister4cls:begin
def mk_private_attr__using_permanent_objs_as_path(permanent_private_obj, /, *permanent_objs):
    r'''
    :: permanent_private_obj -> (*permanent_objs) -> attr:str
    see: mk_private_attr
    #'''
    middle_part4attr = '_'.join(map('{:X}'.format, map(id, permanent_objs)))
    return mk_private_attr(permanent_private_obj, middle_part4attr)
def mk_private_attr(permanent_private_obj, middle_part4attr, /):
    r'''
    :: permanent_private_obj -> middle_part4attr:str -> attr:str
    format:
        f'___{id(permanent_private_obj):X}_{middle_part4attr!s}__h'
    intent:
        .startswith('__') to avoid x.__??? in cls.method
        not .endswith('__') to avoid x.__???__
        why permanent_private_obj?
            to alloc exclusive header
            then format of middle_part4attr is user_defined
            eg. using id seq of permanent_objs to make up middle_part4attr
                see: mk_private_attr__using_permanent_objs_as_path
    #'''
    if not type(middle_part4attr) is str: raise TypeError
    if not middle_part4attr.isidentifier(): raise TypeError
    return f'___{id(permanent_private_obj):X}_{middle_part4attr!s}__h'
class AttachmentMutableDictRegister4cls:
    r'''
>>> type.__setattr__(object, 'a', '')
Traceback (most recent call last):
    ...
TypeError: can't set attributes of built-in/extension type 'object'
>>> type.__getattribute__('', '__dict__')
Traceback (most recent call last):
    ...
TypeError: descriptor '__getattribute__' requires a 'type' object but received a 'str'

>>> class Meta(type):
...     __slots__ = () #donot affect __weakref__, __dict__
>>> class C(Meta):
...     __slots__ = ()
>>> weakref.ref(C) is not None
True
>>> type.__getattribute__(C, '__dict__') is not None
True
>>> 'a' in type.__getattribute__(C, '__dict__')
False
>>> type.__setattr__(C, 'a', '')
>>> C.a
''
>>> 'a' in type.__getattribute__(C, '__dict__')
True


>>> weakref.ref(object) is not None
True
>>> weakref.ref(type) is not None
True
>>> weakref.ref(tuple) is not None
True
>>> weakref.ref(str) is not None
True

    #'''
    ___DictType4cls2dict___ = WeakKeyRefDict
    ___DictType4cls_external_dict___ = dict

    def __init__(sf, d, /):
        OuterDict = type(sf).___DictType4cls2dict___
        if not type(d) is OuterDict: raise TypeError
        sf._d = d
    def _snapshot(sf, /):
        View = MappingProxyType
        OuterDict = type(sf).___DictType4cls2dict___
        InnerDict = type(sf).___DictType4cls_external_dict___
        d = OuterDict((cls, View(InnerDict(d4cls)))
            for (cls, d4cls) in sf._d.items())
        return View(d)
        ##deprecated:
        View = MappingProxyType
        OuterDict = type(sf).___DictType4cls2dict___
        InnerDict = type(sf).___DictType4cls_external_dict___
        d = OuterDict((i, (cls, View(InnerDict(d4cls))))
            for i, (cls, d4cls) in sf._d.items())
        return View(d)
    def _restore(sf, d, /):
        _d = sf._d
        _d.clear()
        _d.update(d)
        return
        ##deprecated:
        def f(i, cls, /):
            if not i == id(cls): raise ValueError
            type.__getattribute__(cls, '__dict__')
                #check cls is type #TypeError
            return True
        InnerDict = type(sf).___DictType4cls_external_dict___
        d = {i:(cls, InnerDict(d4cls))
            for i, (cls, d4cls) in d.items() if f(i, cls)}
        _d = sf._d
        _d.clear()
        _d.update(d)
    def view_attachment_mutable_dict4cls(sf, cls, /):
        d4cls = sf._get_attachment_mutable_dict4cls(cls)
        return MappingProxyType(d4cls)
    def _get_attachment_mutable_dict4cls(sf, cls, /):
        d = sf._d
        if not cls in d: raise LookupError(f'cls not registered: cls={cls!r}')
        d4cls = d[cls]
        return d4cls
        ##deprecated:
        d = sf._d
        i = id(cls)
        if not i in d: raise LookupError(f'cls not registered: cls={cls!r}')
        _cls, d4cls = d[i]
        return d4cls
    def detect_attachment_mutable_dict4cls(sf, cls, /):
        d = sf._d
        return cls in d
        ##deprecated:
        d = sf._d
        i = id(cls)
        return i in d
    def detect_key4attachment_mutable_dict4cls(sf, cls, key, /):
        d4cls = sf.view_attachment_mutable_dict4cls(cls)
        return key in d4cls
    def getitem4attachment_mutable_dict4cls(sf, cls, key, /):
        d4cls = sf.view_attachment_mutable_dict4cls(cls)
        return d4cls[key] #KeyError
    def set_new_item4attachment_mutable_dict4cls(sf, cls, key, value, /):
        d4cls = sf._get_attachment_mutable_dict4cls(cls)
        if key in d4cls: raise KeyError(key)
        d4cls[key] = value
    def register_attachment_mutable_dict4cls(sf, cls, /):
        d = sf._d
        if 1:
            if cls in d: raise LookupError(f'cls registered: cls={cls!r}')
        else:
            ##deprecated:
            i = id(cls)
            if i in d: raise LookupError(f'cls registered: cls={cls!r}')
        sf._test_setattr4cls(cls)
        if 1:
            InnerDict = type(sf).___DictType4cls_external_dict___
            d[cls] = InnerDict()
            assert cls in d
        else:
            ##deprecated:
            d[i] = (cls, {})
    def _test_setattr4cls(sf, cls, /):
        #attr = f'___{id(sf._d):X}'
        attr = mk_private_attr(sf._d, '_')
        d4cls = type.__getattribute__(cls, '__dict__')
            #check cls is type to avoid TypeError ...
        if attr in d4cls: raise logic-err
        try:
            type.__setattr__(cls, attr, 'try-expect-failure')
        except TypeError:
            #TypeError: can't set attributes of built-in/extension type 'object'
            pass #ok
        else:
            ok = not attr in d4cls
            type.__delattr__(cls, attr)#restore
            if not ok:
                raise TypeError(f'cls.__setattr__ allowed: cls={cls!r}')
        return
attachment_mutable_dict_register4cls = AttachmentMutableDictRegister4cls(AttachmentMutableDictRegister4cls.___DictType4cls2dict___())


#]]]AttachmentMutableDictRegister4cls:end

#[[[IHandler4AttachmentDataRegister4cls:begin
class IHandler4AttachmentDataRegister4cls(ABC):
    r'''
    register4cls :: AttachmentDataRegister4cls
    #'''
    __slots__ = ()

    @abstractmethod
    def check_symbol(handler, register4cls, symbol, /):
        '-> None'
    @abstractmethod
    def check_cls(handler, register4cls, cls, symbol, /):
        '-> None'
        #eg. requires IBaeXXX.__xxx__, register only for cls that not subclass of IBaeXXX
    @abstractmethod
    def mk_data(handler, register4cls, cls, symbol, /, *args, **kwargs):
        '-> data'
    @abstractmethod
    def check_data(handler, register4cls, cls, symbol, data, /):
        '-> None'
        #eg. mimic py-getattr()-protocol, using descriptor as data
    @abstractmethod
    def explain_data(handler, register4cls, cls, symbol, data, /, *args, **kwargs):
        '-> ???'
class DefaultHandler4AttachmentDataRegister4cls(IHandler4AttachmentDataRegister4cls):
    #__slots__ = ('__weakref__',)
    __slots__ = ('__weakref__', '__dict__')

    @override
    def check_symbol(handler, register4cls, symbol, /):
        '-> None'
        return
    @override
    def check_cls(handler, register4cls, cls, symbol, /):
        '-> None'
        return
    @override
    #def mk_data(handler, register4cls, cls, symbol, /, *args, **kwargs):
    def mk_data(handler, register4cls, cls, symbol, data, /):
        '-> data'
        return data
    @override
    def check_data(handler, register4cls, cls, symbol, data, /):
        '-> None'
        return
    @override
    def explain_data(handler, register4cls, cls, symbol, data, /, *args, **kwargs):
        '-> ???'
        return (handler, register4cls, cls, symbol, data, args, kwargs)

    r'''
    def explain_data(handler, register4cls, cls, symbol, data, /):
        '-> ???'
        return data
    #'''

default_handler4AttachmentDataRegister4cls = DefaultHandler4AttachmentDataRegister4cls()

class FunctionalHandler4AttachmentDataRegister4cls(IHandler4AttachmentDataRegister4cls):
    __slots__ = ('__weakref__', '__dict__')
    def __init__(sf, /, *, check_symbol, check_cls, mk_data, check_data, explain_data, ):
        d = {**locals()}
        del d['sf']
        def g(sf, d, /):
            for attr, may_f in d.items():
                if may_f is None:
                    f = getattr(DefaultHandler4AttachmentDataRegister4cls, attr)
                else:
                    f = may_f
                if not callable(f): raise TypeError(f'not callable: {attr!s}={f!r}')
                setattr(sf, f'_{attr!s}', f)
            #end-for
            return
        g(sf, d)

        if 0:
            sf._mk_data = mk_data
            sf._check_data = check_data
            sf._explain_data = explain_data
        #print(sf.__dict__)
        sf._check_symbol
        sf._check_cls
        sf._mk_data
        sf._check_data
        sf._explain_data

    @override
    def check_symbol(handler, register4cls, symbol, /):
        '-> None'
        handler._check_symbol(handler, register4cls, symbol)
        return
    @override
    def check_cls(handler, register4cls, cls, symbol, /):
        '-> None'
        handler._check_cls(handler, register4cls, cls, symbol)
        return
    @override
    def mk_data(handler, register4cls, cls, symbol, /, *args, **kwargs):
        '-> data'
        return handler._mk_data(handler, register4cls, cls, symbol, *args, **kwargs)
    @override
    def check_data(handler, register4cls, cls, symbol, data, /):
        '-> None'
        handler._check_data(handler, register4cls, cls, symbol, data)
        return
    @override
    def explain_data(handler, register4cls, cls, symbol, data, /, *args, **kwargs):
        '-> ???'
        return handler._explain_data(handler, register4cls, cls, symbol, data, *args, **kwargs)
def mk_FunctionalHandler4AttachmentDataRegister4cls__human(*, check_symbol=None, check_cls=None, mk_data=None, check_data=None, explain_data=None):
    return FunctionalHandler4AttachmentDataRegister4cls(**locals())
default_FunctionalHandler4AttachmentDataRegister4cls = mk_FunctionalHandler4AttachmentDataRegister4cls__human()

#]]]IHandler4AttachmentDataRegister4cls:end

#[[[AttachmentDataRegister4cls:begin
class AttachmentDataRegister4cls:
    r'''
    see:
        handler :: IHandler4AttachmentDataRegister4cls
        AttachmentMutableDictRegister4cls
    DONE:
        #TypeError: can't set attributes of built-in/extension type 'object'
        see:AttachmentMutableDictRegister4cls
    #'''
    ___BaseClass4handler___ = IHandler4AttachmentDataRegister4cls
    if 1:
        ___DictType4symbol2handler___ = PermanentKeyRefDict
    else:
        ___DictType4symbol2handler___ = WeakKeyRefDict
    def __init__(sf, d, /):
        Dict = type(sf).___DictType4symbol2handler___
        if not type(d) is Dict: raise TypeError
        sf._d = d
        sf._ed = attachment_mutable_dict_register4cls

    def _snapshot(sf, /):
        Dict = type(sf).___DictType4symbol2handler___
        return MappingProxyType(Dict(sf._d)), sf._ed._snapshot()
        def mk(_d, /):
            d = Dict()
            d.update(_d)
        return MappingProxyType(mk(sf._d)), sf._ed._snapshot()
        ##deprecated:
        return MappingProxyType({**sf._d}), sf._ed._snapshot()
    def _restore(sf, dd, /):
        d, ed = dd
        sf._ed._restore(ed)
        Dict = type(sf).___DictType4symbol2handler___
        d = Dict(d)
        _d = sf._d
        _d.clear()
        _d.update(d)
    def mk_attr(sf, symbol, /):
        return mk_private_attr__using_permanent_objs_as_path(sf._d, symbol)
        j = id(sf._d)
        i = id(symbol)
        attr = f'___{j:X}_{i:X}'
        return attr
    def check_symbol(sf, symbol, /):
        pass
    def check_handler(sf, handler, /):
        if not isinstance(handler, type(sf).___BaseClass4handler___):raise TypeError
    def _mk_data_using_handler_(sf, handler, cls, symbol, /, *args, **kwargs):
        '-> data'
        data = handler.mk_data(sf, cls, symbol, *args, **kwargs)
        return data
        ##deprecated:
        def f(data, /):
            return data
        data = f(*args, **kwargs)
        return data
    def check_data_using_handler(sf, handler, cls, symbol, data, /):
        '-> None'
        handler.check_data(sf, cls, symbol, data)
        return
    def check_cls_using_handler(sf, handler, cls, symbol, /):
        handler.check_cls(sf, cls, symbol)
        return
    def check_symbol_using_handler(sf, handler, symbol, /):
        handler.check_symbol(sf, symbol)
        return
    def mk_and_check_data_using_handler(sf, handler, cls, symbol, /, *args, **kwargs):
        sf.check_cls_using_handler(handler, cls, symbol)
        data = sf._mk_data_using_handler_(handler, cls, symbol, *args, **kwargs)
        sf.check_data_using_handler(handler, cls, symbol, data)
        return data
    def register_handler4symbol(sf, symbol, handler, /):
        if symbol in sf._d: raise LookupError(f'handler registered for symbol={symbol!r}')
        sf.check_symbol(symbol)
        sf.check_handler(handler)
        sf.check_symbol_using_handler(handler, symbol)
        attr = sf.mk_attr(symbol)
        #sf._d[symbol] = (symbol, attr, handler)
        sf._d[symbol] = (attr, handler)
        return
        ##deprecated:
        i = id(symbol)
        if i in sf._d: raise LookupError(f'handler registered for symbol={symbol!r}')
        sf.check_symbol(symbol)
        sf.check_handler(handler)
        attr = sf.mk_attr(symbol)
        sf._d[i] = (symbol, attr, handler)
    def detect_handler4symbol(sf, symbol, /):
        '-> handler_exists:bool'
        return symbol in sf._d
        ##deprecated:
        i = id(symbol)
        return i in sf._d
    def get_handler4symbol(sf, symbol, /):
        '-> handler|raise LookupError'
        (attr, handler) = sf._1_preprocess_data4cls(symbol)
        return handler
    def _1_preprocess_data4cls(sf, symbol, /):
        if 1:
            if not symbol in sf._d: raise LookupError(f'no registered handler: symbol={symbol!r}')
            (attr, handler) = sf._d[symbol]
        else:
            ##deprecated:
            i = id(symbol)
            if not i in sf._d: raise LookupError(f'no registered handler: symbol={symbol!r}')
            (symbol, attr, handler) = sf._d[i]
        return attr, handler

    def _0_preprocess_data4cls(sf, cls, /):
        d4cls = type.__getattribute__(cls, '__dict__')
            #check cls is type?
        is_external_d4cls = sf._ed.detect_attachment_mutable_dict4cls(cls)
        if is_external_d4cls:
            d4cls = sf._ed.view_attachment_mutable_dict4cls(cls)
        return d4cls, is_external_d4cls
    def _2_preprocess_data4cls(sf, cls, symbol, /):
        (attr, handler) = sf._1_preprocess_data4cls(symbol)
        (d4cls, is_external_d4cls) = sf._0_preprocess_data4cls(cls)
        return attr, handler, d4cls, is_external_d4cls
    def get_tmay_data_ex4cls(sf, cls, symbol, /):
        '-> tmay (handler, data)'
        attr, handler, d4cls, is_external_d4cls = sf._2_preprocess_data4cls(cls, symbol)
        if not attr in d4cls:
            return ()
        data = d4cls[attr]
        data_ex = (handler, data)
        return (data_ex,)
    def get_data_ex4cls(sf, cls, symbol, /):
        '-> (handler, data) | raise LookupError'
        tmay_data_ex = sf.get_tmay_data_ex4cls(cls, symbol)
        if not tmay_data_ex: raise LookupError(f'no registered data: cls={cls!r}; symbol={symbol!r}')
        [(handler, data)] = tmay_data_ex
        return (handler, data)
    def detect_data4cls(sf, cls, symbol, /):
        attr, handler, d4cls, is_external_d4cls = sf._2_preprocess_data4cls(cls, symbol)
        return attr in d4cls
    def get_tmay_data4cls(sf, cls, symbol, /):
        '-> tmay data'
        tmay_data_ex = sf.get_tmay_data_ex4cls(cls, symbol)
        if not tmay_data_ex:
            return ()
        [(handler, data)] = tmay_data_ex
        return (data,)
    def get_data4cls(sf, cls, symbol, /):
        '-> data | raise LookupError'
        handler, data = sf.get_data_ex4cls(cls, symbol)
        return data
    def _explain_data_using_handler_(sf, handler, cls, symbol, data, /, *args, **kwargs):
        '-> ???'
        r = handler.explain_data(sf, cls, symbol, data, *args, **kwargs)
        return r
        ##deprecated:
        def f(data, /):
            return data
        data = f(data, *args, **kwargs)
        return data
    def get_tmay_and_explain_data4cls(sf, cls, symbol, /, *args, **kwargs):
        '-> tmay result4explain'
        tmay_data_ex = sf.get_tmay_data_ex4cls(cls, symbol)
        if not tmay_data_ex:
            return ()
        [(handler, data)] = tmay_data_ex
        result = sf._explain_data_using_handler_(handler, cls, symbol, data, *args, **kwargs)
        return (result,)
    def get_and_explain_data4cls(sf, cls, symbol, /, *args, **kwargs):
        '-> result4explain | raise LookupError'
        handler, data = sf.get_data_ex4cls(cls, symbol)
        return sf._explain_data_using_handler_(handler, cls, symbol, data, *args, **kwargs)

    def register_data4cls(sf, cls, symbol, /, *args, **kwargs):
        attr, handler, d4cls, is_external_d4cls = sf._2_preprocess_data4cls(cls, symbol)
        if attr in d4cls: raise LookupError(f'data registered for cls={cls!r}; symbol={symbol!r}')

        ed = sf._ed
        data = sf.mk_and_check_data_using_handler(handler, cls, symbol, *args, **kwargs)
        if not is_external_d4cls:
            try:
                type.__setattr__(cls, attr, data)
            except TypeError:#AttributeError?
                #TypeError: can't set attributes of built-in/extension type 'object'
                ok = False
            else:
                ok = attr in d4cls
                if not ok:
                    type.__delattr__(cls, attr, data) #restore
                    #raise LookupError(f'fail to register: {cls!r} {symbol!r}')
            ########################
            if not ok:
                if ed.detect_attachment_mutable_dict4cls(cls):raise logic-err
                ed.register_attachment_mutable_dict4cls(cls)
                if not ed.detect_attachment_mutable_dict4cls(cls):raise logic-err
                #################################
                _attr, _handler, d4cls, is_external_d4cls = sf._2_preprocess_data4cls(cls, symbol)
                if not _attr == attr:raise logic-err
                if not _handler is handler:raise logic-err
                if d4cls:raise logic-err
                if not is_external_d4cls:raise logic-err
        #################################
        if is_external_d4cls:
            if ed.detect_key4attachment_mutable_dict4cls(cls, attr): raise logic-err
            ed.set_new_item4attachment_mutable_dict4cls(cls, attr, data)
            if not ed.detect_key4attachment_mutable_dict4cls(cls, attr): raise logic-err

        if not sf.get_data4cls(cls, symbol) is data: raise logic-err
        return
        if cls is object:
            if not ed.detect_attachment_mutable_dict4cls(cls):raise logic-err
            #if ed.detect_attachment_mutable_dict4cls(cls):raise logic-err
        return
    #end-def register_data4cls(sf, cls, symbol, /, *args, **kwargs):
attachment_data_register4cls = AttachmentDataRegister4cls(AttachmentDataRegister4cls.___DictType4symbol2handler___())

def _t_attachment_data_register4cls(register4cls, f, /):
    dd = register4cls._snapshot()
    try:
        f(register4cls)
    finally:
        register4cls._restore(dd)
def __t_attachment_data_register4cls(register4cls, /):
    symbol = []; symbol2 = []
    handler = default_FunctionalHandler4AttachmentDataRegister4cls #default_handler4AttachmentDataRegister4cls
    data = set()
    register4cls.register_handler4symbol(symbol, handler)
    assert register4cls.detect_handler4symbol(symbol)
    assert not register4cls.detect_handler4symbol(symbol2)
    assert handler is register4cls.get_handler4symbol(symbol)

    class X:pass
    register4cls.register_data4cls(X, symbol, data)
    assert register4cls.get_data4cls(X, symbol) is data
    (_handler, _register4cls, _cls, _symbol, _data, args, kwargs) = register4cls.get_and_explain_data4cls(X, symbol)
    assert (args, kwargs) == ((), {})
    assert all(map(operator.is_, (handler, register4cls, X, symbol, data), (_handler, _register4cls, _cls, _symbol, _data)))

    #deprecated:assert expectError(TypeError, lambda:register4cls.register_data4cls(object, symbol, data))
        #TypeError: can't set attributes of built-in/extension type 'object'
    register4cls.register_data4cls(object, symbol, data)
    dd = register4cls._snapshot()
    register4cls._restore(({}, {}))
    assert not dd == register4cls._snapshot()
    register4cls._restore(dd)
    assert dd == register4cls._snapshot()
_t_attachment_data_register4cls(attachment_data_register4cls, __t_attachment_data_register4cls)


#]]]AttachmentDataRegister4cls:end

#[[[stable_repr4export_long_term_storage:begin
#]]]stable_repr4export_long_term_storage:end

#[[[zzzwww:begin
#]]]zzzwww:end
#]]]main_body_src_code:end


#HHHHH
if __name__ == "__main__":
    from seed.hierarchy.register.AttachmentDataRegister4cls import *
    from seed.hierarchy.register.AttachmentDataRegister4cls import attachment_data_register4cls, mk_private_attr, mk_private_attr__using_permanent_objs_as_path, IHandler4AttachmentDataRegister4cls, default_handler4AttachmentDataRegister4cls, FunctionalHandler4AttachmentDataRegister4cls, mk_FunctionalHandler4AttachmentDataRegister4cls__human

    from seed.hierarchy.register.AttachmentDataRegister4cls import AttachmentMutableDictRegister4cls, attachment_mutable_dict_register4cls, AttachmentDataRegister4cls, attachment_data_register4cls, mk_private_attr, mk_private_attr__using_permanent_objs_as_path, IHandler4AttachmentDataRegister4cls, DefaultHandler4AttachmentDataRegister4cls, default_handler4AttachmentDataRegister4cls, FunctionalHandler4AttachmentDataRegister4cls, mk_FunctionalHandler4AttachmentDataRegister4cls__human, default_FunctionalHandler4AttachmentDataRegister4cls
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #<BLANKLINE>
    #Traceback (most recent call last):


