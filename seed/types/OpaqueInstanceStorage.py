#__all__:goto
#main_body_src_code:goto
#HHHHH
#[[[__doc__:begin
r'''

view ../../python3_src/script/try_python/try_attrs/try_slots.py
    见B_a
        隐藏 attr 的方法有了！
          定义__slots__，取出descriptor，删除cls.__dict__中的descriptor

view ../../python3_src/seed/mapping_tools/fdefault.py
e ../../python3_src/seed/abc/storage/MemberGetter.py


seed.types.OpaqueInstanceStorage
py -m    seed.types.OpaqueInstanceStorage
py -m nn_ns.app.debug_cmd   seed.types.OpaqueInstanceStorage

e ../../python3_src/seed/types/OpaqueInstanceStorage.py


from seed.types.OpaqueInstanceStorage import OpaqueStorage, get_opaque_storage4instance, IGetOpaqueStorage, WithOpaqueStorage

from seed.types.OpaqueInstanceStorage import register_external_opaque_storage4permanent_obj, register_opaque_storage_getter4cls_besides_subclasses, register_opaque_storage_getter4base_cls, register_opaque_storage_to_instance_dict, register_external_opaque_storage4weakable_obj


from seed.types.OpaqueInstanceStorage import IProtocol4OpaqueStorage, IProtocol4OpaqueStorage__default_auto_mk_payload, Protocol4OpaqueStorage__mimic_readonly_attribute, Protocol4OpaqueStorage__mimic_readonly_attribute__instance2result, Protocol4OpaqueStorage__mimic_readonly_attribute__lazy_value, Protocol4OpaqueStorage__mimic_writable_attribute, Protocol4OpaqueStorage__using_ops_method_as_action_case, Protocol4OpaqueStorage__using_ops_method_as_action_case__default_auto_mk_payload, Protocol4OpaqueStorage__using_permission_access

from seed.types.OpaqueInstanceStorage import OpaqueStorage_Throwable_with_payload, OpaqueStorageError, OpaqueStorage_PermissionError, OpaqueStorage_ProtocolError, OpaqueStorage_ProtocolExistsError, OpaqueStorage_ProtocolNotFoundError, OpaqueStorage_KeyPathError, OpaqueStorage_KeyPathExistsError, OpaqueStorage_KeyPathNotFoundError



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
    OpaqueStorage
    get_opaque_storage4instance
        IGetOpaqueStorage
        WithOpaqueStorage
        WithOpaqueStorage_GetOpaqueStorage

        register_external_opaque_storage4permanent_obj
        register_opaque_storage_getter4cls_besides_subclasses
        register_opaque_storage_getter4base_cls
        register_opaque_storage_to_instance_dict
        register_external_opaque_storage4weakable_obj


    IProtocol4OpaqueStorage
        IProtocol4OpaqueStorage__default_auto_mk_payload
            Protocol4OpaqueStorage__mimic_readonly_attribute
            Protocol4OpaqueStorage__mimic_readonly_attribute__instance2result
            Protocol4OpaqueStorage__mimic_readonly_attribute__lazy_value
            Protocol4OpaqueStorage__mimic_writable_attribute

        Protocol4OpaqueStorage__using_ops_method_as_action_case
            Protocol4OpaqueStorage__using_ops_method_as_action_case__default_auto_mk_payload

        Protocol4OpaqueStorage__using_permission_access

    OpaqueStorage_Throwable_with_payload

    OpaqueStorageError
        OpaqueStorage_PermissionError
        OpaqueStorage_ProtocolError
            OpaqueStorage_ProtocolExistsError
            OpaqueStorage_ProtocolNotFoundError
        OpaqueStorage_KeyPathError
            OpaqueStorage_KeyPathExistsError
            OpaqueStorage_KeyPathNotFoundError

    '''.split()

#################################
#HHHHH
___begin_mark_of_excluded_global_names__0___ = ...
import random
import itertools
from seed.abc.abc import ABC, abstractmethod, override#, not_implemented, ABCMeta
from seed.helper.check.checkers import check_type_is, check_callable, check_instance, check_is_None #, check_pair
from seed.tiny import expectError
from seed.helper.check.checkers import check_tmay, check_bool, check_int, check_tuple
  #from seed.helper.check.checkers import checks, checkers, check_funcs
  #view ../../python3_src/seed/helper/check/checkers.py

from seed.tiny import check_Weakable, is_Weakable, check_Hashable__deep
import weakref
from weakref import WeakKeyDictionary
from seed.abc.eq_by_id.BaseAddrAsHash import BaseAddrAsHash, le_AddrAsHash
from seed.abc.eq_by_id.AddrAsHash import AddrAsHash
from seed.tiny import catched_call__either
#from seed.types.mapping.OpaquePseudoMapping import IMutableOpaquePseudoMapping__init_new_key_only
#from collections.abc import Mapping
from seed.types.mapping.OpaquePseudoMapping__weakref import PermanentKeyRefDict, WeakKeyRefDict, PermanentKeyRefSet

from seed.types.mapping.OpaquePseudoMapping__weakref import WeakKeyDictionary4AddrAsHash, MutableOpaquePseudoMapping__init_new_key_only__WeakKeyDictionary4AddrAsHash

from seed.types.mapping.OpaquePseudoMapping__weakref import IMutableOpaquePseudoMapping__init_new_key_only__WeakKeyPathDictionary, IMutableOpaquePseudoMapping__init_new_key_only__WeakKeyPathDictionary__init, MutableOpaquePseudoMapping__init_new_key_only__WeakRefDictionary, MutableOpaquePseudoMapping__init_new_key_only__Value_Ref_Weak_KeysTripleDictionary


from seed.tiny import check_pseudo_identifier

r'''
from seed.mapping_tools.fdefault import mapping_get__tmay_, mapping_get_fdefault__cased_, mapping_set_fdefault__cxxxvalue_, option2mapping_get__tmay
from seed.mapping_tools.fdefault import mapping_reversable_update__tmay
from seed.mapping_tools.fdefault import mapping_contain_, mapping_set__overwrite_or_raise__pair_, mapping_set__new_or_raise__return_, mapping_set__new_or_overwrite__pair__uniform_, mapping_set__new_or_overwrite__pair__onthen_, mapping_set__new_or_pass__cased_, mapping_set__overwrite_or_pass__may_pair_

from seed.mapping_tools.fdefault import mapping_on_key, get_fdefault, set_fdefault, getitem_fdefault, setitem_fdefault, add_new_item




from seed.tiny_.mk_fdefault import mk_fdefaultP, mk_fdefault, mk_fdefaultP_from_default, mk_fdefault_from_default, Mk_fdefaultP, Mk_fdefault, Mk_fdefault1__caller_args_at_last, Mk_fdefault1__caller_args_at_first, Mk_fdefaultP_from_default, Mk_fdefault_from_default, mk_default2value__default_at_last, mk_default2value__default_at_first, mk_tmay_from_default2value, mk_fvalue, mk_tmay_from_is_safe_fvalue, mk_tmay_from_try_fvalue, mk_tmay_from_try_fvalue_KeyError, mk_default

from seed.helper.get4may import nmay2tmay__Nothing, nmay2tmay, get4nmay__Nothing, get4nmay, fget4nmay__Nothing, fget4nmay, fgetP4nmay__Nothing_, fgetP4nmay_, fget4nmay__human, fget4nmay__Nothing__human, xget4nmay_, xget4nmay__human
#'''


r"""
import ...
from seed.tiny import str2__all__
__all__ = str2__all__(r'''#)
    #(''')
from seed.helper.repr_input import repr_helper
from seed.tiny import echo, print_err, mk_fprint, mk_assert_eq_f, expectError
if 0b00:#[01_to_turn_off]
    #0b01
    print(fr'x={x}')
    from seed.tiny import print_err
    print_err(fr'x={x}')
    from pprint import pprint
    pprint(x)
#"""
___end_mark_of_excluded_global_names__0___ = ...

#HHHHH
#[[[main_body_src_code:begin
#OpaqueInstanceStorage:goto
#zzzwww:goto

#[[[OpaqueInstanceStorage:begin

class IGetOpaqueStorage(ABC):
    __slots__ = ()
    @abstractmethod
    def ___get_opaque_storage4instance___(sf, /):
        '-> OpaqueStorage'
def _mk_attr():
    i = hash(random.randint(0, id(object())))
    #attr = f'__{i:X}'
    attr = f'_{i:X}'
    return attr
class WithOpaqueStorage:
    __slots__ = (_mk_attr(),)
    if 0:
      def __new__(cls, /, *_0, **_2):
        sf = super().__new__(cls, *_0, **_2)
        if 0:
          if type(sf) is cls and __class__ in cls.__mro__:
            try:
                #_descriptor.__get__(sf)
                #_get_opaque_storage4WithOpaqueStorage(sf)
                opaque_storage = _get_opaque_storage4WithOpaqueStorage(sf)
                    #__new__ return non-fresh sf, neednot init
            except AttributeError:
                #fresh instance
                opaque_storage = OpaqueStorage()
                _descriptor.__set__(sf, opaque_storage)
                #opaque_storage = _descriptor.__get__(sf)
                opaque_storage = _get_opaque_storage4WithOpaqueStorage(sf)
            check_type_is(OpaqueStorage, opaque_storage)
        return sf


_descriptor = getattr(WithOpaqueStorage, *WithOpaqueStorage.__slots__)
delattr(WithOpaqueStorage, *WithOpaqueStorage.__slots__)
WithOpaqueStorage.__slots__ = ()

check_Weakable
is_Weakable
class WithOpaqueStorage_GetOpaqueStorage(WithOpaqueStorage, IGetOpaqueStorage):
    __slots__ = ()
    @override
    def ___get_opaque_storage4instance___(sf, /):
        '-> OpaqueStorage'
        opaque_storage = _get_opaque_storage4WithOpaqueStorage(sf)
        check_type_is(OpaqueStorage, opaque_storage)
        return opaque_storage





class IPseudoMutableMapping:
    get
    setdefault
    __contains__
    __setitem__?
    __bool__?
    __len__?
    __iter__?
    __getitem__?
e ../../python3_src/seed/abc/storage/MemberGetter.py
e ../../python3_src/seed/types/mapping/PseudoMapping.py
e ../../python3_src/seed/types/mapping/OpaquePseudoMapping.py
e ../../python3_src/seed/lang/hasattr__as_cls.py
py -m nn_ns.app.mk_py_template -o  ../../python3_src/seed/lang/hasattr__as_cls.py
py -m nn_ns.app.mk_py_template -o   ../../python3_src/seed/abc/storage/IStorage4Attachment.py
py -m nn_ns.app.mk_py_template -o   ../../python3_src/seed/abc/storage/MemberGetter.py
e ../../python3_src/seed/abc/storage/IStorage4Attachment.py
from seed.types.mapping.PseudoMapping import IPseudoMapping___get, IPseudoMapping___get__setdefault

from seed.tiny_.mk_fdefault import mk_tmay_from_try_fvalue_KeyError, mk_tmay_from_default2value, mk_tmay_from_is_safe_fvalue, mk_default
        default = mk_default(imay_xdefault_rank, xdefault, mapping, key)



def get_opaque_storage4instance(obj, /):
    #return _get_opaque_storage4WithOpaqueStorage(obj)
    def f():
        yield _get_may_external_opaque_storage4permanent_obj(obj)
        yield _get_may_opaque_storage4WithOpaqueStorage(obj)
        cls = type(obj)
        #IGetOpaqueStorage.___get_opaque_storage4instance___
        #if isinstance(obj, IGetOpaqueStorage:
        #see: base_cls2opaque_storage_getter

        #cls2opaque_storage_getter
        yield _get_may_opaque_storage__unsing_opaque_storage_getter4cls_besides_subclasses(obj)
        #base_cls2opaque_storage_getter
        #   using IGetOpaqueStorage API
        yield _get_may_opaque_storage__unsing_opaque_storage_getter4base_cls(obj)

        #instance.__dict__[OpaqueStorage]
        #opaque_storage_from_instance_dict
        yield _get_may_opaque_storage_from_instance_dict(obj)
        #external_opaque_storage4weakable_obj
        yield _get_may_external_opaque_storage4weakable_obj(obj)
        return
    for may_opaque_storage in f():
        if may_opaque_storage is not None:
            opaque_storage = may_opaque_storage
            check_type_is(OpaqueStorage, opaque_storage)
            return opaque_storage
    raise LookupError
    return None


if 1:
    #opaque_storage4WithOpaqueStorage
    def _get_may_opaque_storage4WithOpaqueStorage(obj, /):
        try:
            return _get_opaque_storage4WithOpaqueStorage(obj)
        except TypeError:
            return None
    #opaque_storage4WithOpaqueStorage
    def _get_opaque_storage4WithOpaqueStorage(obj, /):
        try:
            opaque_storage = _descriptor.__get__(obj)
                #AttributeError if not init
                #TypeError if not <: WithOpaqueStorage
        except AttributeError:
            #fresh instance, init here
            opaque_storage = OpaqueStorage()
            _descriptor.__set__(obj, opaque_storage)
            opaque_storage = _get_opaque_storage4WithOpaqueStorage(obj)
        check_type_is(OpaqueStorage, opaque_storage)
        return opaque_storage

        opaque_storage = _descriptor.__get__(obj)
        check_type_is(OpaqueStorage, opaque_storage)
        return opaque_storage
    #opaque_storage4WithOpaqueStorage
    #_get_opaque_storage4WithOpaqueStorage(WeakableDict())
    assert expectError(TypeError, lambda:_get_opaque_storage4WithOpaqueStorage(set()))
    #opaque_storage4WithOpaqueStorage


if 1:
    #external_opaque_storage4permanent_obj
    _external_opaque_storage4permanent_obj = PermanentKeyRefDict()
    #external_opaque_storage4permanent_obj
    def register_external_opaque_storage4permanent_obj(permanent_obj, /,*, registered_ok):
        d = _external_opaque_storage4permanent_obj
        k = permanent_obj
        if k in d:
            if not registered_ok: raise LookupError('registered')
        else:
            opaque_storage = OpaqueStorage()
            d[k] = opaque_storage

    #external_opaque_storage4permanent_obj
    def _get_may_external_opaque_storage4permanent_obj(permanent_obj, /):
        d = _external_opaque_storage4permanent_obj
        k = permanent_obj
        may_opaque_storage = d.get(k)
        if may_opaque_storage is not None:
            opaque_storage = may_opaque_storage
            check_type_is(OpaqueStorage, opaque_storage)
        return may_opaque_storage
    #external_opaque_storage4permanent_obj

if 1:
    #cls2opaque_storage_getter
    #   vs _base_cls2opaque_storage_getter
    #_cls2opaque_storage_getter = WeakKeyRefDict()
    _cls2opaque_storage_getter = WeakKeyDictionary4AddrAsHash()
    #cls2opaque_storage_getter
    def register_opaque_storage_getter4cls_besides_subclasses(cls, opaque_storage_getter, /,*, registered_ok):
        check_instance(type, cls)
        check_instance(AddrAsHash, cls) # isinstance not issubclass
        check_Weakable(cls)
        check_callable(opaque_storage_getter)

        d = _cls2opaque_storage_getter
        k = cls
        if k in d:
            if not registered_ok: raise LookupError('registered')
        else:
            d[k] = opaque_storage_getter
    #cls2opaque_storage_getter
    def _get_may_opaque_storage__unsing_opaque_storage_getter4cls_besides_subclasses(obj, /):
        cls = type(obj)
        if not is_Weakable(cls): return None
        d = _cls2opaque_storage_getter
        k = cls
        m = d.get(k)
        if m is not None:
            opaque_storage_getter = m
            opaque_storage = opaque_storage_getter(obj)
            check_type_is(OpaqueStorage, opaque_storage)
            return opaque_storage
        return None
    #cls2opaque_storage_getter

if 1:
    #base_cls2opaque_storage_getter
    def register_opaque_storage_getter4base_cls(base_cls, opaque_storage_getter, /,*, registered_ok):
        check_instance(type, base_cls)
        check_callable(opaque_storage_getter)

        if hasattr(base_cls, '___get_opaque_storage4instance___'):
            if not registered_ok: raise LookupError('registered')
        else:
            setattr(base_cls, '___get_opaque_storage4instance___', opaque_storage_getter)

    #base_cls2opaque_storage_getter
    def _get_may_opaque_storage__unsing_opaque_storage_getter4base_cls(obj, /):
        cls = type(obj)
        m = getattr(cls, '___get_opaque_storage4instance___', None)
        if m is not None:
            ___get_opaque_storage4instance___ = m
            opaque_storage = ___get_opaque_storage4instance___(obj)
            check_type_is(OpaqueStorage, opaque_storage)
            return opaque_storage
        return None
    #base_cls2opaque_storage_getter
if 1:
    #opaque_storage_from_instance_dict
    def _get_may_opaque_storage_from_instance_dict(obj, /):
        k = OpaqueStorage
        m = getattr(obj, '__dict__', {}).get(OpaqueStorage)
        if m is not None:
            opaque_storage = m
            check_type_is(OpaqueStorage, opaque_storage)
            return opaque_storage
        return None
    #opaque_storage_from_instance_dict
    def register_opaque_storage_to_instance_dict(obj, /,*, registered_ok):
        d = obj.__dict__
        k = OpaqueStorage
        if k in d:
            if not registered_ok: raise LookupError('registered')
        else:
            opaque_storage = OpaqueStorage()
            d[k] = opaque_storage
    #opaque_storage_from_instance_dict

if 1:
    #external_opaque_storage4weakable_obj
    #_external_opaque_storage4weakable_obj = WeakKeyDictionary4AddrAsHash()
    _external_opaque_storage4weakable_obj = WeakKeyRefDict()
    #external_opaque_storage4weakable_obj
    def _get_may_external_opaque_storage4weakable_obj(weakable_obj, /):
        d = _external_opaque_storage4weakable_obj
        k = weakable_obj
        may_opaque_storage = d.get(k)
        if may_opaque_storage is not None:
            opaque_storage = may_opaque_storage
            check_type_is(OpaqueStorage, opaque_storage)
        return may_opaque_storage

    #external_opaque_storage4weakable_obj
    def register_external_opaque_storage4weakable_obj(weakable_obj, /,*, registered_ok):
        d = _external_opaque_storage4weakable_obj
        k = weakable_obj
        if k in d:
            if not registered_ok: raise LookupError('registered')
        else:
            opaque_storage = OpaqueStorage()
            d[k] = opaque_storage

    #external_opaque_storage4weakable_obj





















class IProtocol4OpaqueStorage(AddrAsHash):
    r'''
    may try:
        args[0] = key_path
        see:
            IMutableOpaquePseudoMapping__init_new_key_only__WeakKeyPathDictionary__init
                MutableOpaquePseudoMapping__init_new_key_only__WeakRefDictionary
                MutableOpaquePseudoMapping__init_new_key_only__Value_Ref_Weak_KeysTripleDictionary
    #'''
    __slots__ = '__weakref__'
    @abstractmethod
    def mk_new_payload(protocol, /, *args, **kwargs):
        '... -> payload | raise OpaqueStorage_Throwable_with_payload<exc, tmay_payload>'
    @abstractmethod
    def call_with_payload(protocol, payload, /, *args, **kwargs):
        'payload -> ... -> (tmay_payload, is_result, exception_vs_result) | raise OpaqueStorage_Throwable_with_payload<exc, tmay_payload>'


class IProtocol4OpaqueStorage__default_auto_mk_payload(IProtocol4OpaqueStorage):
    __slots__ = ()
    def mk_new_default_payload(protocol, /):
        '() -> payload | raise OpaqueStorage_Throwable_with_payload<exc, tmay_payload>'
        return protocol.mk_new_payload()













class Protocol4OpaqueStorage__mimic_readonly_attribute(IProtocol4OpaqueStorage):
    __slots__ = ()
    @override
    def mk_new_payload(protocol, payload, /):
        '... -> payload | raise OpaqueStorage_Throwable_with_payload<exc, tmay_payload>'
        return payload
    @override
    def call_with_payload(protocol, payload, /):
        'payload -> ... -> (tmay_payload, is_result, exception_vs_result) | raise OpaqueStorage_Throwable_with_payload<exc, tmay_payload>'
        return ((), True, payload)

class Protocol4OpaqueStorage__mimic_readonly_attribute__instance2result(IProtocol4OpaqueStorage):
    r'''
    instance2result
    payload
        = (tribool_case, exception_vs_instance2result_vs_result)
        = (False, exception)
        | (..., instance2result)
        | (True, result)
    #'''
    __slots__ = ()
    @classmethod
    def __check_unpacked_payload(cls, tribool_case, exception_vs_instance2result_vs_result, /):
        if tribool_case is False:
            exception = exception_vs_instance2result_vs_result
            if not isinstance(exception, Exception): raise TypeError
        elif tribool_case is ...: #Ellipsis
            instance2result = exception_vs_instance2result_vs_result
            check_callable(instance2result)
        elif tribool_case is True:
            result = exception_vs_instance2result_vs_result
            #pass
        else:
            raise TypeError(f'not tribool: type(tribool_case) is {type(tribool_case)!r}')
    @override
    def mk_new_payload(protocol, tribool_case, exception_vs_instance2result_vs_result, /):
        '... -> payload | raise OpaqueStorage_Throwable_with_payload<exc, tmay_payload>'
        __class__.__check_unpacked_payload(tribool_case, exception_vs_instance2result_vs_result)
        payload = (tribool_case, exception_vs_instance2result_vs_result)
        return payload
    @override
    def call_with_payload(protocol, payload, instance, /):
        'payload -> ... -> (tmay_payload, is_result, exception_vs_result) | raise OpaqueStorage_Throwable_with_payload<exc, tmay_payload>'
        (tribool_case, exception_vs_instance2result_vs_result) = payload
        if tribool_case is ...:
            instance2result = exception_vs_instance2result_vs_result
            calc_result = lambda:instance2result(instance)
            either = catched_call__either(Exception, calc_result)
            payload = (is_result, exception_vs_result) = either
            tmay_payload = (payload,)
        else:
            tmay_payload = ()
            (is_result, exception_vs_result) = payload
        if not type(is_result) is bool: raise logic-err
        return (tmay_payload, is_result, exception_vs_result)


class Protocol4OpaqueStorage__mimic_readonly_attribute__lazy_value(IProtocol4OpaqueStorage__default_auto_mk_payload):
    r'''
    lazy_value :: () -> value|raise Exception
    result = tmay value
    payload = may_either
        = may (is_value, exception_vs_value)
        = None
        | (False, exception)
        | (True, value)
    #'''
    __slots__ = ()
    @override
    def mk_new_payload(protocol, /):
        '... -> payload | raise OpaqueStorage_Throwable_with_payload<exc, tmay_payload>'
        payload = None
        return payload
    @override
    def call_with_payload(protocol, payload, may_lazy_value, /):
        'payload -> ... -> (tmay_payload, is_result, exception_vs_result) | raise OpaqueStorage_Throwable_with_payload<exc, tmay_payload>'
        if payload is None:
            if may_lazy_value is None:
                tmay_payload = ()
                result = tmay_value = ()
                return (tmay_payload, True, result)
            lazy_value = may_lazy_value
            check_callable(lazy_value)

            either = catched_call__either(Exception, lazy_value)
            payload = (is_value, exception_vs_value) = either
            tmay_payload = (payload,)
        else:
            tmay_payload = ()
        tmay_payload
        (is_value, exception_vs_value) = payload
        if not type(is_value) is bool: raise logic-err
        if is_value:
            value = exception_vs_value
            result = tmay_value = (value,)
            exception_vs_result = result
        else:
            exception = exception_vs_value
            exception_vs_result = exception
        is_result = is_value
        return (tmay_payload, is_result, exception_vs_result)


class Protocol4OpaqueStorage__mimic_writable_attribute(IProtocol4OpaqueStorage__default_auto_mk_payload):
    __slots__ = ()
    @override
    def mk_new_payload(protocol, tmay_value=(), /):
        '... -> payload | raise OpaqueStorage_Throwable_with_payload<exc, tmay_payload>'
        check_tmay(tmay_value)
        payload = tmay_value
        return payload

    def call_with_payload__uniform(protocol, payload, tmay_old_value2pair___tmay_tmay_new_value__result, /, *args, **kwargs):
        r'''
        payload -> tmay_old_value2pair___tmay_tmay_new_value__result ... -> (tmay_payload, is_result, exception_vs_result) | raise OpaqueStorage_Throwable_with_payload<exc, tmay_payload>
        see:
            cls.set_attr
            cls.set_attr__new
                # raise OpaqueStorage_KeyPathExistsError#AttributeError
            cls.set_attr__overwrite
                # raise OpaqueStorage_KeyPathNotFoundError#AttributeError
            cls.get_attr
                # raise OpaqueStorage_KeyPathNotFoundError#AttributeError
            cls.pop_attr
                # raise OpaqueStorage_KeyPathNotFoundError#AttributeError

            cls.set_attr__fdefault
            cls.get_attr__fdefault
            cls.pop_attr__fdefault

            cls.set_attr__tmay
            cls.get_attr__tmay
            cls.pop_attr__tmay
        #'''
        tmay_old_value = payload
        check_tmay(tmay_old_value)

        (tmay_tmay_new_value, result) = tmay_old_value2pair___tmay_tmay_new_value__result(tmay_old_value, *args, **kwargs)
        check_tmay(tmay_tmay_new_value)
        if tmay_tmay_new_value:
            [tmay_new_value] = tmay_tmay_new_value
            check_tmay(tmay_new_value)
        tmay_new_payload = tmay_tmay_new_value
        is_result = True
        return (tmay_new_payload, True, result)

    #tmay_old_value2pair___tmay_tmay_new_value__result: below classmethod
    @classmethod
    def set_attr(cls, tmay_old_value, new_value, /):
        'result = None'
        result = None
        tmay_tmay_new_value = ((new_value,),)
        return tmay_tmay_new_value, result
    @classmethod
    def set_attr__new(cls, tmay_old_value, new_value, /):
        'result = None'
        if tmay_old_value: raise OpaqueStorage_KeyPathExistsError
        return cls.set_attr(tmay_old_value, new_value)
    @classmethod
    def set_attr__overwrite(cls, tmay_old_value, new_value, /):
        'result = None'
        if not tmay_old_value: raise OpaqueStorage_KeyPathNotFoundError
        return cls.set_attr(tmay_old_value, new_value)
    @classmethod
    def get_attr(cls, tmay_old_value, /):
        'result = old_value'
        if not tmay_old_value: raise OpaqueStorage_KeyPathNotFoundError
        #if not tmay_old_value: raise AttributeError
        [old_value] = tmay_old_value
        result = old_value
        tmay_tmay_new_value = ()
        return tmay_tmay_new_value, result
    @classmethod
    def pop_attr(cls, tmay_old_value, /):
        'result = old_value'
        (_tmay_tmay_new_value, result) = cls.get_attr(tmay_old_value)
        tmay_tmay_new_value = ((),)
        return tmay_tmay_new_value, result

    @classmethod
    def set_attr__fdefault(cls, tmay_old_value, calc_new_value, /):
        'result = (is_new_value, old_value|new_value)'
        is_new_value = not tmay_old_value
        if is_new_value:
            new_value = calc_new_value()
            old_value__vs__new_value = new_value
            tmay_tmay_new_value = ((new_value,),)
        else:
            [old_value] = tmay_old_value
            old_value__vs__new_value = old_value
            tmay_tmay_new_value = ()
        result = is_new_value, old_value__vs__new_value
        return tmay_tmay_new_value, result
    @classmethod
    def get_attr__fdefault(cls, tmay_old_value, calc_default, /):
        'result = (is_default_value, old_value|default_value)'
        (_tmay_tmay_new_value, result) = cls.set_attr__fdefault(tmay_old_value, calc_default)
        tmay_tmay_new_value = ()
        return tmay_tmay_new_value, result
    @classmethod
    def pop_attr__fdefault(cls, tmay_old_value, calc_default, /):
        'result = (is_default_value, old_value|default_value)'
        (_tmay_tmay_new_value, result) = cls.set_attr__fdefault(tmay_old_value, calc_default)
        tmay_tmay_new_value = ((),) if tmay_old_value else ()
        return tmay_tmay_new_value, result
    @classmethod
    def get_attr__tmay(cls, tmay_old_value, /):
        'result = tmay_old_value'
        result = tmay_old_value
        tmay_tmay_new_value = ()
        return tmay_tmay_new_value, result
    @classmethod
    def pop_attr__tmay(cls, tmay_old_value, /):
        'result = tmay_old_value'
        result = tmay_old_value
        tmay_tmay_new_value = ((),) if tmay_old_value else ()
        return tmay_tmay_new_value, result
    @classmethod
    def set_attr__tmay(cls, tmay_old_value, tmay_new_value, /):
        'result = tmay_old_value'
        check_tmay(tmay_new_value)
        result = tmay_old_value
        tmay_tmay_new_value = (tmay_new_value,)
        return tmay_tmay_new_value, result


    #@override
    call_with_payload = call_with_payload__uniform

Protocol4OpaqueStorage__mimic_readonly_attribute()
Protocol4OpaqueStorage__mimic_readonly_attribute__instance2result()
Protocol4OpaqueStorage__mimic_readonly_attribute__lazy_value()
Protocol4OpaqueStorage__mimic_writable_attribute()
class Protocol4OpaqueStorage__using_ops_method_as_action_case(IProtocol4OpaqueStorage):
    r'''
    protocol=sf<ops>
    payload=obj4ops=ops(...)
    action_case=type(ops).method=args[0]
            #method: here meaning unbounded-instance-method got from cls<ops>
    #'''
    __slots__ = '_ops'
    def __init__(protocol, ops, /):
        check_callable(ops)
        protocol._ops = ops
    @override
    def mk_new_payload(protocol, /, *args, **kwargs):
        '... -> payload | raise OpaqueStorage_Throwable_with_payload<exc, tmay_payload>'
        payload = obj4ops = protocol._ops(*args, **kwargs)
        return payload
    @override
    def call_with_payload(protocol, payload, action_case, /, *args, **kwargs):
        'payload -> ... -> (tmay_payload, is_result, exception_vs_result) | raise OpaqueStorage_Throwable_with_payload<exc, tmay_payload>'
        check_callable(action_case)
        ops = protocol._ops
        method_from_ops_cls = getattr(type(ops), action_case.__name__, None)
        if not action_case is method_from_ops_cls: raise TypeError
        (tmay_payload, is_result, exception_vs_result) = method_from_ops_cls(ops, payload, *args, **kwargs)
        return (tmay_payload, is_result, exception_vs_result)

class Protocol4OpaqueStorage__using_ops_method_as_action_case__default_auto_mk_payload(Protocol4OpaqueStorage__using_ops_method_as_action_case, IProtocol4OpaqueStorage__default_auto_mk_payload):
    __slots__ = ()
Protocol4OpaqueStorage__using_ops_method_as_action_case(id)
Protocol4OpaqueStorage__using_ops_method_as_action_case__default_auto_mk_payload(id)



class Protocol4OpaqueStorage__using_permission_access(IProtocol4OpaqueStorage__default_auto_mk_payload):
    r'''
    args[0] = permission :: int
        detect = 0b01
        get__tmay = 0b11
        set__new_or_overwrite = 0b11_1_00
        detect_set__new_or_pass = 0b01_1_01
        detect_set__overwrite_or_pass = 0b10_1_01
        drop__delete_or_pass = 0b100_1_00
        burn__final = 0b1_000_0_00
        pass
    args[1] = config4key_path = [weak_vs_ref_vs_value]
    args[2] = key_path = [key]{len=len(config4key_path)}
        ++value:permission
        ++value:config4key_path
    #args[3] = descriptor4opaque
    ...
    ###default_value=(is_final, descriptor4opaque, cmay (is_result, exception_vs_result))
    default_value=(False, ())=(is_final, tmay_value)
    default_value=((), None, False, ())=(tmay_descriptor4opaque, payload4descriptor4opaque, is_final, tmay_value)
        descriptor4opaque:
            callback on pre-/post-action
            using tmay extra_args_kwargs...
            check input
            check ouput
            check tmay_old_value tmay_new_value
            transform input
            transform ouput
            send msg??? modify payload4descriptor4opaque
    ===
    MutableOpaquePseudoMapping__init_new_key_only__Value_Ref_Weak_KeysTripleDictionary
    #'''
    __slots__ = ()
    @override
    def mk_new_payload(protocol, /):
        #def mk_new_payload(protocol, /, *tmay_value, is_final=False):
        '... -> payload | raise OpaqueStorage_Throwable_with_payload<exc, tmay_payload>'
        payload = d = MutableOpaquePseudoMapping__init_new_key_only__Value_Ref_Weak_KeysTripleDictionary()
        return payload
    @override
    def call_with_payload(protocol, payload, permission, config4key_path, key_path, action_case, /, *args, **kwargs):
        'payload -> ... -> (tmay_payload, is_result, exception_vs_result) | raise OpaqueStorage_Throwable_with_payload<exc, tmay_payload>'
        check_int(permission)
        check_tuple(config4key_path)
        check_tuple(key_path)
        if len(config4key_path) != len(key_path): raise TypeError
        if not all(config4key is None or type(config4key) is bool for config4key in config4key_path): raise TypeError

        ops = sf = protocol
        method_from_ops_cls = getattr(type(ops), action_case.__name__, None)
        if not action_case is method_from_ops_cls: raise TypeError
        permission_requirements = action_case.___permission_requirements___
        if not permission_requirements==(permission_requirements & permission): raise OpaqueStorage_PermissionError

        d = payload#payload4protocol
        del payload
        def f():
            #bug:keys4value = []
            keys4value = [permission, config4key_path]
            keys4ref = []
            keys4weak = []
            for config4key, key in zip(config4key_path, key_path):
                if config4key is True:
                    keys4value.append(key)
                elif config4key is None:
                    keys4ref.append(key)
                elif config4key is False:
                    keys4weak.append(key)
                else:
                    raise logic-err
            return (tuple(keys4value), tuple(keys4ref), tuple(keys4weak))
        k = f()
        m = d.get(k)
        if m is None:
            payload4key_path = (False, ())
        else:
            payload4key_path = m
        (is_final, tmay_old_value) = payload4key_path
        check_tmay(tmay_old_value)
        check_bool(is_final)
        if is_final and (permission_requirements & __class__.PrimePermissionRequirements.__.modify): raise OpaqueStorage_PermissionError

        (tmay_is_final, tmay_tmay_new_value, result4protocol) = method_from_ops_cls(ops, permission, is_final, tmay_old_value)
        check_tmay(tmay_tmay_new_value)
        if tmay_tmay_new_value: check_tmay(*tmay_tmay_new_value)
        check_tmay(tmay_is_final)
        if tmay_is_final: check_bool(*tmay_is_final)

        [_is_final] = tmay_is_final or [is_final]
        if is_final and not _is_final: raise logic-err
        if is_final and tmay_tmay_new_value: raise logic-err
        if tmay_tmay_new_value:
            base_modify = __class__.PrimePermissionRequirements.__.base_modify
            if tmay_tmay_new_value and not (permission & base_modify): raise logic-err
            if tmay_tmay_new_value and not (permission_requirements & base_modify): raise logic-err
            if tmay_tmay_new_value and is_final: raise logic-err

        if tmay_tmay_new_value or _is_final is not is_final:
            #update payload4key_path
            [_tmay_value] = tmay_tmay_new_value or [tmay_old_value]
            _payload4key_path = (_is_final, _tmay_value)
            d[k] = _payload4key_path
        return ((), True, result4protocol)


    def __check_permission(protocol, is_final, permission, prime_names_str, /):
        s = __class__.PrimePermissionRequirements
        permission_requirements = 0
        for prime_name in prime_names_str.split():
            permission_requirements |= getattr(s, prime_name)
        if not permission_requirements == (permission_requirements & permission): raise OpaqueStorage_PermissionError
        if is_final and (permission_requirements & s.__.modify): raise OpaqueStorage_PermissionError

    #[[[action_case-begin
    def detect(protocol, permission, is_final, tmay_old_value, /):
        r'extra~() -> result4protocol~old_value_exists'
        __class__.__check_permission(permission, is_final, 'detect')
        tmay_is_final = ()
        tmay_tmay_new_value = ()
        result4protocol = old_value_exists = bool(tmay_old_value)
        return (tmay_is_final, tmay_tmay_new_value, result4protocol)
    def get__tmay(protocol, permission, is_final, tmay_old_value, /):
        r'extra~() -> result4protocol~tmay_old_value'
        __class__.__check_permission(permission, is_final, 'get__tmay detect')
        tmay_is_final = ()
        tmay_tmay_new_value = ()
        result4protocol = tmay_old_value
        return (tmay_is_final, tmay_tmay_new_value, result4protocol)


    def set__new_or_overwrite(protocol, permission, is_final, tmay_old_value, lazy_new_value, /):
        r'extra~(lazy_new_value,) -> result4protocol~new_value'
        #why lazy_new_value not new_value? to check permission before eval
        __class__.__check_permission(permission, is_final, 'set__new_or_overwrite')
        check_callable(lazy_new_value)
        tmay_is_final = ()
        new_value = lazy_new_value()
        tmay_new_value = (new_value,)
        tmay_tmay_new_value = (tmay_new_value,)
        result4protocol = new_value
        return (tmay_is_final, tmay_tmay_new_value, result4protocol)
    def detect_set__new_or_pass(protocol, permission, is_final, tmay_old_value, lazy_new_value, /):
        r'extra~(lazy_new_value,) -> result4protocol~tmay_new_value'
        __class__.__check_permission(permission, is_final, 'detect_set__new_or_pass detect')
        check_callable(lazy_new_value)
        tmay_is_final = ()
        tmay_new_value = (lazy_new_value(),) if not tmay_old_value else ()
        tmay_tmay_new_value = (tmay_new_value,) if tmay_new_value else ()
        result4protocol = tmay_new_value
        return (tmay_is_final, tmay_tmay_new_value, result4protocol)
    def detect_set__overwrite_or_pass(protocol, permission, is_final, tmay_old_value, lazy_new_value, /):
        r'extra~(lazy_new_value,) -> result4protocol~tmay_new_value'
        __class__.__check_permission(permission, is_final, 'detect_set__overwrite_or_pass detect')
        check_callable(lazy_new_value)
        tmay_is_final = ()
        tmay_new_value = (lazy_new_value(),) if tmay_old_value else ()
        tmay_tmay_new_value = (tmay_new_value,) if tmay_new_value else ()
        result4protocol = tmay_new_value
        return (tmay_is_final, tmay_tmay_new_value, result4protocol)
    def drop__delete_or_pass(protocol, permission, is_final, tmay_old_value, /):
        r'extra~() -> result4protocol~None'
        __class__.__check_permission(permission, is_final, 'drop__delete_or_pass')
        tmay_is_final = ()
        tmay_tmay_new_value = ((),) if tmay_old_value else ()
        result4protocol = None
        return (tmay_is_final, tmay_tmay_new_value, result4protocol)
    def burn__final(protocol, permission, is_final, tmay_old_value, /):
        r'extra~() -> result4protocol~None'
        __class__.__check_permission(permission, is_final, 'burn__final')
        tmay_is_final = (True,) if not is_final else ()
        tmay_tmay_new_value = ()
        result4protocol = None
        return (tmay_is_final, tmay_tmay_new_value, result4protocol)
    class PrimePermissionRequirements:
        r'''
        detect, get, modify, set__new, set__overwrite, drop, burn
        #'''
        detect = 0b01
        get__tmay = 0b11
        set__new_or_overwrite = 0b11_1_00
        detect_set__new_or_pass = 0b01_1_01
        detect_set__overwrite_or_pass = 0b10_1_01
        drop__delete_or_pass = 0b100_1_00
        burn__final = 0b1_000_0_00
        class __:
            modify = 0b0_111_1_00
            base_modify = 0b0_000_1_00
        pass
    detect.___permission_requirements___ = (
        PrimePermissionRequirements.detect
        )
    get__tmay.___permission_requirements___ = (
        PrimePermissionRequirements.get__tmay
        )

    set__new_or_overwrite.___permission_requirements___ = (
        PrimePermissionRequirements.set__new_or_overwrite
        )
    detect_set__new_or_pass.___permission_requirements___ = (
        PrimePermissionRequirements.detect_set__new_or_pass
        )
    detect_set__overwrite_or_pass.___permission_requirements___ = (
        PrimePermissionRequirements.detect_set__overwrite_or_pass
        )
    drop__delete_or_pass.___permission_requirements___ = (
        PrimePermissionRequirements.drop__delete_or_pass
        )
    burn__final.___permission_requirements___ = (
        PrimePermissionRequirements.burn__final
        )


    r'''
    get__raise
        get__tmay
    detect_set__new_or_raise
        detect_set__new_or_pass
    detect_set__overwrite_or_raise
        detect_set__overwrite_or_pass
    detect_set__new_or_overwrite
        detect_set__new_or_pass
        detect_set__overwrite_or_raise
    get_set__overwrite
        get__raise
        detect_set__overwrite_or_raise
    get_set__new_or_overwrite
        get__tmay
        detect_set__new_or_raise
        detect_set__overwrite_or_raise
    detect_drop__delete_or_pass
        detect
        drop__delete_or_pass
    detect_drop__delete_or_raise
        detect_drop__delete_or_pass
    get_drop__delete_or_pass
        get__tmay
        drop__delete_or_pass
    get_drop__delete_or_raise
        get__raise
        drop__delete_or_pass
    alter__drop_or_set
        set__new_or_overwrite
        drop__delete_or_pass
    detect_alter__drop_or_set
        detect_drop__delete_or_pass # ()
        detect_set__new_or_overwrite # (exist2new_value,)
    get_alter__drop_or_set
        get_drop__delete_or_pass # ()
        get_set__new_or_overwrite # (tmay_old_value2new_value,)
    #'''

    def get__raise(protocol, permission, is_final, tmay_old_value, /):
        r'extra~() -> result4protocol~old_value'
        __class__.__check_permission(permission, is_final, 'get__tmay detect')
        (tmay_is_final, tmay_tmay_new_value, result4protocol) = protocol.get__tmay(permission, is_final, tmay_old_value)
        if not tmay_old_value is result4protocol: raise logic-err
        if not tmay_old_value: raise OpaqueStorage_KeyPathNotFoundError
        [old_value] = tmay_old_value
        result4protocol = old_value
        return (tmay_is_final, tmay_tmay_new_value, result4protocol)


    def detect_set__new_or_raise(protocol, permission, is_final, tmay_old_value, lazy_new_value, /):
        r'extra~(lazy_new_value,) -> result4protocol~new_value'
        __class__.__check_permission(permission, is_final, 'detect_set__new_or_pass detect')
        check_callable(lazy_new_value)
        (tmay_is_final, tmay_tmay_new_value, result4protocol) = protocol.detect_set__new_or_pass(permission, is_final, tmay_old_value, lazy_new_value)
        tmay_new_value = result4protocol
        if not tmay_new_value: raise OpaqueStorage_KeyPathExistsError
        [new_value] = tmay_new_value
        result4protocol = new_value
        return (tmay_is_final, tmay_tmay_new_value, result4protocol)


    def detect_set__overwrite_or_raise(protocol, permission, is_final, tmay_old_value, lazy_new_value, /):
        r'extra~(lazy_new_value,) -> result4protocol~new_value'
        __class__.__check_permission(permission, is_final, 'detect_set__overwrite_or_pass detect')
        check_callable(lazy_new_value)
        (tmay_is_final, tmay_tmay_new_value, result4protocol) = protocol.detect_set__overwrite_or_pass(permission, is_final, tmay_old_value, lazy_new_value)
        tmay_new_value = result4protocol
        if not tmay_new_value: raise OpaqueStorage_KeyPathNotFoundError
        [new_value] = tmay_new_value
        result4protocol = new_value
        return (tmay_is_final, tmay_tmay_new_value, result4protocol)

    def detect_set__new_or_overwrite(protocol, permission, is_final, tmay_old_value, exist2new_value, /):
        r'extra~(exist2new_value,) -> result4protocol~(old_value_exists, new_value)'
        __class__.__check_permission(permission, is_final, 'detect_set__overwrite_or_pass detect_set__new_or_pass detect')
        check_callable(exist2new_value)
        old_value_exists = False
        lazy_new_value = lambda:exist2new_value(old_value_exists)
        (tmay_is_final, tmay_tmay_new_value, result4protocol) = protocol.detect_set__new_or_pass(permission, is_final, tmay_old_value, lazy_new_value)
        tmay_new_value = result4protocol
        if not tmay_new_value:
            old_value_exists = True
            (tmay_is_final, tmay_tmay_new_value, _result4protocol) = protocol.detect_set__overwrite_or_raise(permission, is_final, tmay_old_value, lazy_new_value)
            new_value = _result4protocol
        else:
            [new_value] = tmay_new_value
        result4protocol = (old_value_exists, new_value)
        return (tmay_is_final, tmay_tmay_new_value, result4protocol)


    def get_set__overwrite(protocol, permission, is_final, tmay_old_value, old_value2new_value, /):
        r'extra~(old_value2new_value,) -> result4protocol~(old_value, new_value)'
        __class__.__check_permission(permission, is_final, 'detect_set__overwrite_or_pass get__tmay detect')
        check_callable(old_value2new_value)
        (tmay_is_final, tmay_tmay_new_value, result4protocol) = protocol.get__raise(permission, is_final, tmay_old_value)
        old_value = result4protocol
        lazy_new_value = lambda:old_value2new_value(old_value)
        (tmay_is_final, tmay_tmay_new_value, _result4protocol) = protocol.detect_set__overwrite_or_raise(permission, is_final, tmay_old_value, lazy_new_value)
        new_value = _result4protocol
        result4protocol = (old_value, new_value)
        return (tmay_is_final, tmay_tmay_new_value, result4protocol)
    def get_set__new_or_overwrite(protocol, permission, is_final, tmay_old_value, tmay_old_value2new_value, /):
        r'extra~(tmay_old_value2new_value,) -> result4protocol~(tmay_old_value, new_value)'
        __class__.__check_permission(permission, is_final, 'detect_set__overwrite_or_pass detect_set__new_or_pass get__tmay detect')
        check_callable(tmay_old_value2new_value)
        (tmay_is_final, tmay_tmay_new_value, result4protocol) = protocol.get__tmay(permission, is_final, tmay_old_value)
        #tmay_old_value = result4protocol
        if not tmay_old_value is result4protocol: raise logic-err
        lazy_new_value = lambda:tmay_old_value2new_value(tmay_old_value)
        if tmay_old_value:
            f = protocol.detect_set__overwrite_or_raise
        else:
            f = protocol.detect_set__new_or_raise
        (tmay_is_final, tmay_tmay_new_value, _result4protocol) = f(permission, is_final, tmay_old_value, lazy_new_value)
        new_value = _result4protocol
        result4protocol = (tmay_old_value, new_value)
        return (tmay_is_final, tmay_tmay_new_value, result4protocol)


    def detect_drop__delete_or_pass(protocol, permission, is_final, tmay_old_value, /):
        r'extra~() -> result4protocol~old_value_exists'
        __class__.__check_permission(permission, is_final, 'drop__delete_or_pass detect')
        (tmay_is_final, tmay_tmay_new_value, result4protocol) = protocol.detect(permission, is_final, tmay_old_value)
        old_value_exists = result4protocol
        (tmay_is_final, tmay_tmay_new_value, _result4protocol) = protocol.drop__delete_or_pass(permission, is_final, tmay_old_value)
        if not old_value_exists is result4protocol: raise logic-err
        return (tmay_is_final, tmay_tmay_new_value, result4protocol)

    def detect_drop__delete_or_raise(protocol, permission, is_final, tmay_old_value, /):
        r'extra~() -> result4protocol~None'
        __class__.__check_permission(permission, is_final, 'drop__delete_or_pass detect')
        (tmay_is_final, tmay_tmay_new_value, result4protocol) = protocol.detect_drop__delete_or_pass(permission, is_final, tmay_old_value)
        old_value_exists = result4protocol
        if not old_value_exists: raise OpaqueStorage_KeyPathNotFoundError
        result4protocol = None
        return (tmay_is_final, tmay_tmay_new_value, result4protocol)

    def get_drop__delete_or_pass(protocol, permission, is_final, tmay_old_value, /):
        r'extra~() -> result4protocol~tmay_old_value'
        __class__.__check_permission(permission, is_final, 'drop__delete_or_pass get__tmay detect')
        (tmay_is_final, tmay_tmay_new_value, result4protocol) = protocol.get__tmay(permission, is_final, tmay_old_value)
        if not tmay_old_value is result4protocol: raise logic-err
        (tmay_is_final, tmay_tmay_new_value, _result4protocol) = protocol.drop__delete_or_pass(permission, is_final, tmay_old_value)
        if not tmay_old_value is result4protocol: raise logic-err
        return (tmay_is_final, tmay_tmay_new_value, result4protocol)

    def get_drop__delete_or_raise(protocol, permission, is_final, tmay_old_value, /):
        r'extra~() -> result4protocol~old_value'
        __class__.__check_permission(permission, is_final, 'drop__delete_or_pass get__tmay detect')
        (tmay_is_final, tmay_tmay_new_value, result4protocol) = protocol.get__raise(permission, is_final, tmay_old_value)
        old_value = result4protocol
        if not old_value is tmay_old_value[0]: raise logic-err
        (tmay_is_final, tmay_tmay_new_value, _result4protocol) = protocol.drop__delete_or_pass(permission, is_final, tmay_old_value)
        if not old_value is result4protocol: raise logic-err
        return (tmay_is_final, tmay_tmay_new_value, result4protocol)


    def alter__drop_or_set(protocol, permission, is_final, tmay_old_value, lazy_tmay_lazy_new_value, /):
        r'extra~(lazy_tmay_lazy_new_value,) -> result4protocol~tmay_new_value'
        #why lazy_tmay_lazy_new_value not tmay_new_value? to check permission before eval
        __class__.__check_permission(permission, is_final, 'drop__delete_or_pass set__new_or_overwrite')
        check_callable(lazy_tmay_lazy_new_value)
        tmay_lazy_new_value = lazy_tmay_lazy_new_value()
        check_tmay(tmay_lazy_new_value)
        if tmay_lazy_new_value:
            [lazy_new_value] = tmay_lazy_new_value
            check_callable(lazy_new_value)
            (tmay_is_final, tmay_tmay_new_value, result4protocol) = protocol.set__new_or_overwrite(permission, is_final, tmay_old_value, lazy_new_value)
            new_value = result4protocol
            tmay_new_value = (new_value,)
        else:
            (tmay_is_final, tmay_tmay_new_value, result4protocol) = protocol.drop__delete_or_pass(permission, is_final, tmay_old_value)
            check_is_None(result4protocol)
            tmay_new_value = ()
        result4protocol = tmay_new_value
        return (tmay_is_final, tmay_tmay_new_value, result4protocol)

    def detect_alter__drop_or_set(protocol, permission, is_final, tmay_old_value, lazy_tmay__exist2new_value, /):
        r'extra~(lazy_tmay__exist2new_value,) -> result4protocol~(old_value_exists, tmay_new_value)'
        'lazy_tmay__exist2new_value -> (old_value_exists, tmay_new_value)'
            #detect_drop__delete_or_pass # ()
            #detect_set__new_or_overwrite # (exist2new_value,)
        __class__.__check_permission(permission, is_final, 'detect_drop__delete_or_pass detect_set__new_or_overwrite drop__delete_or_pass set__new_or_overwrite detect')
        check_callable(lazy_tmay__exist2new_value)
        if 0:
            (tmay_is_final, tmay_tmay_new_value, result4protocol) = protocol.detect(permission, is_final, tmay_old_value)
            old_value_exists = result4protocol
            if not old_value_exists is bool(tmay_old_value): raise logic-err
            ###
            (tmay_is_final, tmay_tmay_new_value, result4protocol) = protocol.alter__drop_or_set(permission, is_final, tmay_old_value, lazy_tmay__exist2new_value)
            tmay_new_value = result4protocol
            result4protocol = (old_value_exists, tmay_new_value)
            return (tmay_is_final, tmay_tmay_new_value, result4protocol)
        #######################
        #######################
        tmay__exist2new_value = lazy_tmay__exist2new_value()
        if tmay__exist2new_value:
            #set
            [exist2new_value] = tmay__exist2new_value
            (tmay_is_final, tmay_tmay_new_value, result4protocol) = protocol.detect_set__new_or_overwrite(permission, is_final, tmay_old_value, tmay_old_value2new_value)
            (old_value_exists, new_value) = result4protocol
            tmay_new_value = (new_value,)
        else:
            #del
            (tmay_is_final, tmay_tmay_new_value, result4protocol) = protocol.detect_drop__delete_or_pass(permission, is_final, tmay_old_value)
            old_value_exists = result4protocol
            tmay_new_value = ()
        result4protocol = (old_value_exists, tmay_new_value)
        return (tmay_is_final, tmay_tmay_new_value, result4protocol)



    def get_alter__drop_or_set(protocol, permission, is_final, tmay_old_value, lazy_tmay__tmay_old_value2new_value, /):
        r'extra~(lazy_tmay__tmay_old_value2new_value,) -> result4protocol~(tmay_old_value, tmay_new_value)'
        'lazy_tmay__tmay_old_value2new_value -> (tmay_old_value, tmay_new_value)'
            #get_drop__delete_or_pass # ()
            #get_set__new_or_overwrite # (tmay_old_value2new_value,)

        __class__.__check_permission(permission, is_final, 'get_drop__delete_or_pass get_set__new_or_overwrite drop__delete_or_pass set__new_or_overwrite get__tmay detect')
        check_callable(lazy_tmay__tmay_old_value2new_value)

        if 0:
            (tmay_is_final, tmay_tmay_new_value, result4protocol) = protocol.get__tmay(permission, is_final, tmay_old_value)
            if not tmay_old_value is result4protocol: raise logic-err
            ###
            (tmay_is_final, tmay_tmay_new_value, result4protocol) = protocol.alter__drop_or_set(permission, is_final, tmay_old_value, lazy_tmay__tmay_old_value2new_value)
            tmay_new_value = result4protocol
            result4protocol = (tmay_old_value, tmay_new_value)
            return (tmay_is_final, tmay_tmay_new_value, result4protocol)
        #######################
        #######################
        tmay__tmay_old_value2new_value = lazy_tmay__tmay_old_value2new_value()
        if tmay__tmay_old_value2new_value:
            #set
            [tmay_old_value2new_value] = tmay__tmay_old_value2new_value
            (tmay_is_final, tmay_tmay_new_value, result4protocol) = protocol.get_set__new_or_overwrite(permission, is_final, tmay_old_value, tmay_old_value2new_value)
            (_tmay_old_value, new_value) = result4protocol
            tmay_new_value = (new_value,)
        else:
            #del
            (tmay_is_final, tmay_tmay_new_value, result4protocol) = protocol.get_drop__delete_or_pass(permission, is_final, tmay_old_value)
            _tmay_old_value = result4protocol
            tmay_new_value = ()
        result4protocol = (tmay_old_value, tmay_new_value)
        return (tmay_is_final, tmay_tmay_new_value, result4protocol)


    #]]]action_case-end


    get__raise.___permission_requirements___ = (
        get__tmay.___permission_requirements___
        )
    detect_set__new_or_raise.___permission_requirements___ = (
        detect_set__new_or_pass.___permission_requirements___
        )
    detect_set__overwrite_or_raise.___permission_requirements___ = (
        detect_set__overwrite_or_pass.___permission_requirements___
        )
    detect_set__new_or_overwrite.___permission_requirements___ = (
        detect_set__new_or_pass.___permission_requirements___
        | detect_set__overwrite_or_raise.___permission_requirements___
        )

    get_set__overwrite.___permission_requirements___ = (
        get__raise.___permission_requirements___
        | detect_set__overwrite_or_raise.___permission_requirements___
        )
    get_set__new_or_overwrite.___permission_requirements___ = (
        get__tmay.___permission_requirements___
        | detect_set__new_or_raise.___permission_requirements___
        | detect_set__overwrite_or_raise.___permission_requirements___
        )
    detect_drop__delete_or_pass.___permission_requirements___ = (
        detect.___permission_requirements___
        | drop__delete_or_pass.___permission_requirements___
        )
    detect_drop__delete_or_raise.___permission_requirements___ = (
        detect_drop__delete_or_pass.___permission_requirements___
        )
    get_drop__delete_or_pass.___permission_requirements___ = (
        get__tmay.___permission_requirements___
        | drop__delete_or_pass.___permission_requirements___
        )
    get_drop__delete_or_raise.___permission_requirements___ = (
        get__raise.___permission_requirements___
        | drop__delete_or_pass.___permission_requirements___
        )
    alter__drop_or_set.___permission_requirements___ = (
        set__new_or_overwrite.___permission_requirements___
        | drop__delete_or_pass.___permission_requirements___
        )
    detect_alter__drop_or_set.___permission_requirements___ = (
        detect_drop__delete_or_pass.___permission_requirements___
        | detect_set__new_or_overwrite.___permission_requirements___
        )
    get_alter__drop_or_set.___permission_requirements___ = (
        get_drop__delete_or_pass.___permission_requirements___
        | get_set__new_or_overwrite.___permission_requirements___
        )


Protocol4OpaqueStorage__using_permission_access()

















class OpaqueStorage_Throwable_with_payload(BaseException):
    def __init__(sf, exception, tmay_payload, /):
        check_instance(BaseException, exception)
        check_tmay(tmay_payload)
        sf.exception = exception
        sf.tmay_payload = tmay_payload
            #why not payload?
            #   exception may be OpaqueStorage_Throwable_with_payload
            #       cannot throw exception directly
class OpaqueStorageError(Exception):pass
class OpaqueStorage_PermissionError(OpaqueStorageError, PermissionError):pass
    #权限拒绝
class OpaqueStorage_ProtocolError(OpaqueStorageError, LookupError):pass
class OpaqueStorage_ProtocolExistsError(OpaqueStorage_ProtocolError):pass
class OpaqueStorage_ProtocolNotFoundError(OpaqueStorage_ProtocolError):pass
FileExistsError
FileNotFoundError
LookupError
KeyError
AttributeError
PermissionError
class OpaqueStorage_KeyPathError(OpaqueStorageError, LookupError):pass
class OpaqueStorage_KeyPathExistsError(OpaqueStorage_KeyPathError):pass
class OpaqueStorage_KeyPathNotFoundError(OpaqueStorage_KeyPathError):pass





class OpaqueStorage:
    r'''
    protocol=ops=key=key_path_fmt=protocol_impl_ver :: IProtocol4OpaqueStorage <: AddrAsHash&Weakable
    usage:
        eg: key_path = protocol, symbol

    .init_new_payload4protocol(protocol, *args, **kwargs)
        payload = protocol.mk_new_payload(*args, **kwargs)
    .call_protocol(protocol, *args, **kwargs)
        if default:
            payload = protocol.mk_new_default_payload()
        (tmay_payload, is_result, exception_vs_result) = protocol.call_with_payload(payload, *args, **kwargs)
    #'''
    __slots__ = '__d'
    @classmethod
    def check_protocol(cls, protocol, /):
        check_Weakable(protocol)
        if not le_AddrAsHash(type(protocol)):raise TypeError
            #to avoid err introduced by skip check@BaseAddrAsHash
        check_instance(IProtocol4OpaqueStorage, protocol)
    def __contains__(sf, protocol, /):
        sf.check_protocol(protocol)
        return protocol in sf.__d
    def __init__(sf, /):
        sf.__d = WeakKeyDictionary()
        #sf.__d = WeakKeyDictionary4AddrAsHash()
    def __catched_call(sf, protocol, f, /):
        try:
            return f()
        except OpaqueStorage_Throwable_with_payload as e:
            exception = e.exception
            tmay_payload = e.tmay_payload
            del e
            check_tmay(tmay_payload)
            if tmay_payload:
                [payload] = tmay_payload
                sf.__d[protocol] = payload
                    #init@protocol
                    #auto-init-on-default@protocol
                    #update@protocol
            raise exception

    def init_new_payload4protocol(sf, protocol, /, *args, **kwargs):
        if protocol in sf: raise OpaqueStorage_ProtocolExistsError#KeyError#existed
            #sf.check_protocol(protocol)
            #   using __contains__ ==>> .check_protocol(protocol) called
        if 1:
            payload = sf.__catched_call(protocol, lambda:protocol.mk_new_payload(*args, **kwargs))
        sf.__d[protocol] = payload
            #init@protocol
    def call_protocol(sf, protocol, /, *args, **kwargs):
        #sf.check_protocol(protocol)
        if protocol not in sf:
            #sf.check_protocol(protocol)
            #   using __contains__ ==>> .check_protocol(protocol) called
            if isinstance(protocol, IProtocol4OpaqueStorage__default_auto_mk_payload):
                if 1:
                    default_payload = sf.__catched_call(protocol, protocol.mk_new_default_payload)
                sf.__d[protocol] = default_payload
                    #auto-init-on-default@protocol
                del default_payload
            else:
                raise OpaqueStorage_ProtocolNotFoundError#KeyError#not exists

        payload = sf.__d[protocol]
        if 1:
            (tmay_payload, is_result, exception_vs_result) = sf.__catched_call(protocol, lambda:protocol.call_with_payload(payload, *args, **kwargs))
        del payload

        check_tmay(tmay_payload)
        check_type_is(bool, is_result)
        if tmay_payload:
            [new_payload] = tmay_payload
            sf.__d[protocol] = new_payload
                #update@protocol

        if is_result:
            result = exception_vs_result
            return result
        else:
            exc = exception_vs_result
            raise exc
        pass



r"""
description4action
    #access control via key visible instead of description4action
    required:
        init_key
    optional:
        get__tmay # allmost be required
            get
        set__new
        set__overwrite
        pop__tmay
            pop
            remove
            discard

class OpaqueStorageError(Exception):pass
class Permission4OpaqueStorageError(OpaqueStorageError, PermissionError):pass
    #权限拒绝
class IDescriptor4OpaqueStorage(ABC):
    'descriptor4opaque.op -> raise OpaqueStorageError'
    @abstractmethod
    def on_init_key(sf, payload, setting4path, setting4key, env4descriptor4opaque, instance, path, id4description4action, key, /):
        '-> (is_ok, exc_vs_None, tmay payload)'
    @abstractmethod
    def on_send_msg(sf, payload, setting4path, setting4key, env4descriptor4opaque, instance, path, id4description4action, key, group4action, action_path_on_key, msg, /):
        '-> (is_ok, exc_vs_response, tmay payload)'
    @abstractmethod
    def on_get__tmay(sf, payload, setting4path, setting4key, env4descriptor4opaque, instance, path, id4description4action, key, /):
        '-> (is_ok, exc_vs_tmay old_value, tmay payload)'
    @abstractmethod
    def on_set__new(sf, payload, setting4path, setting4key, env4descriptor4opaque, instance, path, id4description4action, key, new_value, /):
        '-> (is_ok, exc_vs_None, tmay payload)'
    @abstractmethod
    def on_set__overwrite(sf, payload, setting4path, setting4key, env4descriptor4opaque, instance, path, id4description4action, key, new_value, /):
        '-> (is_ok, exc_vs_old_value, tmay payload)'
    @abstractmethod
    def on_pop__tmay(sf, payload, setting4path, setting4key, env4descriptor4opaque, instance, path, id4description4action, key, /):
        '-> (is_ok, exc_vs_old_value, tmay payload)'


class OpaqueStorage:
    r'''
    ver3:
        ops <: (EqById&Weakable)
            le_AddrAsHash + weakref.ref/check_Weakable
        mapping:
            ops -> payload
                detect(ops) -> bool
                init(ops, *args, **kwargs) -> payload
                    ops.mk_new(*args, **kwargs) -> payload
                call(ops, *args, **kwargs) -> result
                    ops.call(payload, *args, **kwargs) -> (result, tmay payload)
                no-del !!!
                    deleteable-key/path should be upper/deeper-level
                    payload-for-ops is likely to be dict, user cannot access it
                    ops is a-new-version impl of opaque-mapping

    #################################
    path+key[ver1] --> [ver2]who{<:(EqById&Weakable) :.symbol4user_name, .usage<user_defined_namespace-key>, }+user_defined_namespace+key
        mapping:
            who -> (key[i] ->)* -> (descriptor4opaque, payload)
            who -> usage<path>
                via register extension
                    eg. who == None/'cache_dict': path=instance of CachedLazyProperty
                via type(who)
                via object.__getattribute__(who, '___the_dict4extension___')
        usage<path>:
            check(path)
            to_keys(path) -> [key]{len(keys)==len(fmts)}
                + to_keys_in_use(path) -> [key]{len(keys)==len(fmts)}
                + to_keys_for_descriptor4opaque(path) -> [key]{len(keys)==len(fmts)}
            get_fmts() -> [fmt]
                fmt = (either<dict, WeakKeyDictionary>, .mk_working_key(key))
                    mk_working_key : eg. -> AddrAsHashWrapper<key>
            to_??? for descriptor4opaque

        description4action & descriptor4opaque shouldnot be changed
            so description4action<user_defined_namespace> should be buildin immutable, or deepcopy into internal and use its id
            descriptor4opaque saved with payload

    #################################
    ###path <: Weakable&EqById
    description4action <: EqById
        using id(path), id(description4action), id(key) as key
            通过env4opaque_storage.setting4path+.setting4key 配置path 与 key 的使用方式
    opaque-Map<id(path), (path, Map<description4action, Map<key, (state{setted, popped}, case{value|exc|descriptor4opaque}, payload)> >)>
    ###WeakKeyMap<path, ...>


    #XMap<setting, k, v> = Map<setting, YMap<setting, k, v> >
    #YMap<setting, k, v> =
    DEFINE XMap<setting, k, v> =
        case setting of
        (dict, id, echo) # special case of (dict, f, g)
            -> dict<id(k), (k, v)> # check k' is k
        (dict, f, g)
            -> dict<f(k), (g(k), v)> # check g(k') is g(k)
        (WeakKeyDictionary, echo, None)
            -> WeakKeyDictionary<k, v>
        (dict, echo, None)
            -> dict<k, v>

    #opaque_storage = opaque-Map<id(path), (path, Map<id4description4action, Map<id(key), (key, descriptor4opaque, payload)> >)>
    DEFINE opaque_storage = opaque-Map<(setting4path, setting4key), XMap<setting4path, path, (Map<id4description4action, XMap<key, (key, descriptor4opaque, payload)> >,)> >

    env4opaque_storage
        .setting4path
        .setting4key
    env4descriptor4opaque
        depends on descriptor4opaque
    description4action:
        DEFINE description4action = (may {require:(is_ok, {require}}, may default_requires_ok, may {action_on_key:{require}}, may default_actions_ok, may {group4action:description4action}, may default_groups_ok)
            default ok ==>> listed are forbidden
            default not ok ==>> listed are ok
            None ==>> raise on default but listed actions are ok-or-not?

        DEFINE action_path_on_key = (action_on_key,) | (group4action, action_path_on_key)
        ###
        if tmay_group4action == ():
            #no init_key
            {init_key} <= description4action.set4permitted_operation4key <= {init_key, get__tmay, set__new, set__overwrite, pop__tmay}
            action_on_key <- {init_key, get__tmay, set__new, set__overwrite, pop__tmay}
    #'''
    @classmethod
    def register_description4action(cls, description4action, /):
        '-> id(deepcopy<FrozenDict+unique>(description4action)) #too heavy??'
    @classmethod
    def __get_description4action(cls, id4description4action, /):
        '-> description4action'
    @classmethod
    def does_description_accept_the_operation(cls, description4action, tmay_group4action, action_path_on_key, /):
        '-> bool # [tmay_group4action=()]:action_on_key <- {init_key, get__tmay, set__new, set__overwrite, pop__tmay}'
    def __get_storage(sf, setting4path, path, id4description4action, /):
        '-> storage::dict'
    def __get_descriptor4opaque_ex(sf, storage, setting4key, key, /):
        '-> (descriptor4opaque, payload)'

    def init_key_with_descriptor4opaque(sf, env4opaque_storage, env4descriptor4opaque, instance, path, id4description4action, key, descriptor4opaque, payload, /):
        '-> None'
        #init_key
        #init_key_with_descriptor4opaque
    def send_msg_to_descriptor4opaque(sf, env4opaque_storage, env4descriptor4opaque, instance, path, id4description4action, key, tmay_group4action, action_path_on_key, msg, /):
        '-> response'
        check_type_is(int, id4description4action)
        check_tmay(tmay_group4action)
        check__action_path_on_key__shallow(action_path_on_key)

        description4action = sf.__get_description4action(id4description4action)
        if not sf.does_description_accept_the_operation(description4action, tmay_group4action, action_path_on_key): raise Permission4OpaqueStorageError
        del description4action

        setting4path, setting4key = env4opaque_storage.setting4path, env4opaque_storage.setting4key
        storage = sf.__get_storage(setting4path, setting4key, path, id4description4action)
        (descriptor4opaque, payload) = sf.__get_descriptor4opaque_ex(storage, setting4key, key)

        if tmay_group4action == ():
            #the default group4action
            #   ie. get/set/pop
            check_tmay(msg)
            tmay_new_value = msg
            if not len(action_path_on_key)==1: raise TypeError
            [action_on_key] = action_path_on_key
            if action_on_key is the_action__init_key: raise TypeError#call init_key_with_descriptor4opaque directly once
            elif action_on_key is the_action__get__tmay:
                f = descriptor4opaque.on_get__tmay
            elif action_on_key is the_action__set__new:
                f = descriptor4opaque.on_set__new
            elif action_on_key is the_action__set__overwrite:
                f = descriptor4opaque.on_set__overwrite
            elif action_on_key is the_action__pop__tmay:
                f = descriptor4opaque.on_pop__tmay
            elif action_on_key is the_action__x:
                f = descriptor4opaque.on_x
            (is_ok, exc_vs_result, tmay_payload) = f(payload, setting4path, setting4key, env4descriptor4opaque, instance, path, id4description4action, key, *tmay_new_value)
        else:
            [group4action] = tmay_group4action
            descriptor4opaque.on_send_msg...



def check__action_path_on_key__shallow(action_path_on_key, /):
    check_type_is(tuple, action_path_on_key)
    if not 1 <= len(action_path_on_key) <= 2: raise TypeError
#the_action__init_key
the_action__get__tmay
the_action__set__new
the_action__set__overwrite
the_action__pop__tmay

prime,func_prime,permission_prime
    detect
    get__tmay
    set__new_or_overwrite
    detect_set__new_or_pass
    detect_set__overwrite_or_pass
    drop__delete_or_pass
    6
    burn__final
compose
    get__raise
        get__tmay
    detect_set__new_or_raise
        detect_set__new_or_pass
    detect_set__overwrite_or_raise
        detect_set__overwrite_or_pass
    detect_set__new_or_overwrite
        detect_set__new_or_pass
        detect_set__overwrite_or_raise
    get_set__overwrite
        get__raise
        detect_set__overwrite_or_raise
    get_set__new_or_overwrite
        get__tmay
        detect_set__new_or_raise
        detect_set__overwrite_or_raise
    detect_drop__delete_or_pass
        detect
        drop__delete_or_pass
    detect_drop__delete_or_raise
        detect_drop__delete_or_pass
    get_drop__delete_or_pass
        get__tmay
        drop__delete_or_pass
    get_drop__delete_or_raise
        get__raise
        drop__delete_or_pass
    alter__drop_or_set
        set__new_or_overwrite
        drop__delete_or_pass
    detect_alter__drop_or_set
        detect_drop__delete_or_pass # ()
        detect_set__new_or_overwrite # (exist2new_value,)
    get_alter__drop_or_set
        get_drop__delete_or_pass # ()
        get_set__new_or_overwrite # (tmay_old_value2new_value,)
    13
6+13=19

    def detect(sf, env4opaque_storage, env4descriptor4opaque, instance, path, id4description4action, key, /):
        '-> bool #prime; +detect'
    def get__tmay(sf, env4opaque_storage, env4descriptor4opaque, instance, path, id4description4action, key, /):
        '-> tmay old_value #prime; +get +detect'
    def get__raise(sf, env4opaque_storage, env4descriptor4opaque, instance, path, id4description4action, key, /):
        '-> old_value #compose; +get +detect'
        get__tmay

    def set__new_or_overwrite(sf, env4opaque_storage, env4descriptor4opaque, instance, path, id4description4action, key, lazy_new_value, /):
        '-> new_value #func_prime&permission_compose; +set__new +set__overwrite'
        #why lazy_new_value not new_value? to check permission before eval
    def detect_set__new_or_pass(sf, env4opaque_storage, env4descriptor4opaque, instance, path, id4description4action, key, lazy_new_value, /):
        '-> tmay new_value #func_compose&permission_prime; +set__new +detect'
    def detect_set__overwrite_or_pass(sf, env4opaque_storage, env4descriptor4opaque, instance, path, id4description4action, key, lazy_new_value, /):
        '-> tmay new_value #func_compose&permission_prime; +set__overwrite +detect'


    def detect_set__new_or_raise(sf, env4opaque_storage, env4descriptor4opaque, instance, path, id4description4action, key, lazy_new_value, /):
        '-> new_value #compose; +set__new +detect'
        detect_set__new_or_pass
    def detect_set__overwrite_or_raise(sf, env4opaque_storage, env4descriptor4opaque, instance, path, id4description4action, key, lazy_new_value, /):
        '-> new_value #compose; +set__overwrite +detect'
        detect_set__overwrite_or_pass

    def detect_set__new_or_overwrite(sf, env4opaque_storage, env4descriptor4opaque, instance, path, id4description4action, key, exist2new_value, /):
        '-> (exist, new_value) #compose; +set__new +set__overwrite +detect'
        detect_set__new_or_pass
        detect_set__overwrite_or_raise
    def get_set__overwrite(sf, env4opaque_storage, env4descriptor4opaque, instance, path, id4description4action, key, old_value2new_value, /):
        '-> (old_value, new_value) #compose;  +set__overwrite +get +detect'
        get__raise
        detect_set__overwrite_or_raise
    def get_set__new_or_overwrite(sf, env4opaque_storage, env4descriptor4opaque, instance, path, id4description4action, key, tmay_old_value2new_value, /):
        '-> (tmay old_value, new_value) #compose; +set__new +set__overwrite +get +detect'
        get__tmay
        detect_set__new_or_raise
        detect_set__overwrite_or_raise



    def drop__delete_or_pass(sf, env4opaque_storage, env4descriptor4opaque, instance, path, id4description4action, key, /):
        '-> None #func_compose&permission_prime; +delete    #==discard'
    def detect_drop__delete_or_pass(sf, env4opaque_storage, env4descriptor4opaque, instance, path, id4description4action, key, /):
        '-> exist #compose; +delete +detect'
        detect
        drop__delete_or_pass

    def detect_drop__delete_or_raise(sf, env4opaque_storage, env4descriptor4opaque, instance, path, id4description4action, key, /):
        '-> None #compose; +delete +detect    #==remove'
        detect_drop__delete_or_pass
    def get_drop__delete_or_pass(sf, env4opaque_storage, env4descriptor4opaque, instance, path, id4description4action, key, /):
        '-> tmay old_value #compose; +delete +get +detect    #==pop__tmay'
        get__tmay
        drop__delete_or_pass
    def get_drop__delete_or_raise(sf, env4opaque_storage, env4descriptor4opaque, instance, path, id4description4action, key, /):
        '-> old_value #compose; +delete +get +detect    #==pop'
        get__raise
        drop__delete_or_pass


    def alter__drop_or_set(sf, env4opaque_storage, env4descriptor4opaque, instance, path, id4description4action, key, lazy_tmay_lazy_new_value, /):
        '-> tmay_new_value #compose; +delete +set__new +set__overwrite'
        #why lazy_tmay_lazy_new_value not tmay_new_value? to check permission before eval
        set__new_or_overwrite
        drop__delete_or_pass
    def detect_alter__drop_or_set(sf, env4opaque_storage, env4descriptor4opaque, instance, path, id4description4action, key, lazy_tmay__exist2new_value, /):
        '-> (exist, tmay_new_value) #compose; +delete +set__new +set__overwrite +detect'
        'lazy_tmay__exist2new_value -> (old_value_exists, tmay_new_value)'
            detect_drop__delete_or_pass # ()
            detect_set__new_or_overwrite # (exist2new_value,)
    def get_alter__drop_or_set(sf, env4opaque_storage, env4descriptor4opaque, instance, path, id4description4action, key, lazy_tmay__tmay_old_value2new_value, /):
        '-> (tmay old_value, tmay_new_value) #compose; +delete +set__new +set__overwrite +detect'
        'lazy_tmay__tmay_old_value2new_value -> (tmay_old_value, tmay_new_value)'
            get_drop__delete_or_pass # ()
            get_set__new_or_overwrite # (tmay_old_value2new_value,)



mapping_get__tmay_, mapping_get_fdefault__cased_, mapping_set_fdefault__cxxxvalue_, option2mapping_get__tmay
mapping_reversable_update__tmay
mapping_contain_, mapping_set__overwrite_or_raise__pair_, mapping_set__new_or_raise__return_, mapping_set__new_or_overwrite__pair__uniform_, mapping_set__new_or_overwrite__pair__onthen_, mapping_set__new_or_pass__cased_, mapping_set__overwrite_or_pass__may_pair_
#"""
#]]]OpaqueInstanceStorage:end

#[[[zzzwww:begin
#]]]zzzwww:end
#]]]main_body_src_code:end


#HHHHH
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #<BLANKLINE>
    #Traceback (most recent call last):



