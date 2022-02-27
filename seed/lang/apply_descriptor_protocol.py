#__all__:goto
#main_body_src_code:goto
#HHHHH
#[[[__doc__:begin
r'''

seed.lang.apply_descriptor_protocol
py -m    seed.lang.apply_descriptor_protocol
py -m nn_ns.app.debug_cmd   seed.lang.apply_descriptor_protocol


seed.lang.basic_descriptors
seed.lang.apply_descriptor_protocol
seed.abc.IDescriptor
e ../../python3_src/seed/lang/basic_descriptors.py
e ../../python3_src/seed/lang/apply_descriptor_protocol.py
e ../../python3_src/seed/abc/IDescriptor.py





view /storage/emulated/0/0my_files/git_repos/python3_src/seed/abc/IDescriptor.py
    #see: seed.abc.IDescriptor for py_doc::descriptor_protocol
    #see: seed.abc.IDescriptor for test_super_in_classmethod/NonDataDescriptor4Echo

from seed.lang.apply_descriptor_protocol import is_descriptor, is_data_descriptor, is_non_data_descriptor

from seed.lang.apply_descriptor_protocol import extended_protocol_api_to_descriptor_protocol_api, extended_protocol__apply_descriptor_protocol_in_mapping_get_tmay___in_super_search, extended_protocol__apply_pseudo_descriptor_get___in_super_search

from seed.lang.apply_descriptor_protocol import apply_descriptor_protocol_in_mapping_get_tmay, apply_pseudo_descriptor_get, apply_descriptor_protocol_in_mapping_get_tmay___tmay_cased_result, apply_pseudo_descriptor_get___cased_result

#[[[doc_sections:begin
#doctest_examples:goto
#wwwzzz:goto

#[[[doctest_examples:begin

test_super_in_classmethod/NonDataDescriptor4Echo
    ... ... xxxxxxx

>>> from seed.abc.IDescriptor import NonDataDescriptor4Echo

>>> class A:
...     @classmethod
...     def f(cls, /):return cls
>>> class B(A):
...     @classmethod
...     def f(cls, /):return super(__class__, cls).f()
>>> class C(B):pass
>>> C.f() is C
True
>>> super(B, C).f() is C
True
>>> super(B, C()).f() is C
True
>>> del A, B, C

>>> class A:
...     @NonDataDescriptor4Echo
...     def f(cls, /):return cls
>>> class B(A):
...     @NonDataDescriptor4Echo
...     def f(sf_or_cls, /):return super(__class__, sf_or_cls).f()
>>> class C(B):pass
>>> c = C()
>>> A_f = A.__dict__['f']
>>> B_f = B.__dict__['f']
>>> type(A_f) is NonDataDescriptor4Echo
True
>>> type(B_f) is NonDataDescriptor4Echo
True
>>> C.f == (B_f, None, C)
True
>>> c.f == (B_f, c, C)
True
>>> super(B,C).f == (A_f, None, C)
True
>>> super(B,c).f == (A_f, c, C)
True
>>> del A, B, C



>>> def g():pass
>>> is_descriptor(g)
True
>>> is_descriptor(classmethod(g))
True
>>> is_descriptor(staticmethod(g))
True
>>> is_descriptor(property(g))
True
>>> is_descriptor(B_f)
True

>>> is_non_data_descriptor(g)
True
>>> is_non_data_descriptor(classmethod(g))
True
>>> is_non_data_descriptor(staticmethod(g))
True
>>> is_non_data_descriptor(property(g))
False
>>> is_non_data_descriptor(B_f)
True

>>> is_data_descriptor(g)
False
>>> is_data_descriptor(classmethod(g))
False
>>> is_data_descriptor(staticmethod(g))
False
>>> is_data_descriptor(property(g))
True
>>> is_data_descriptor(B_f)
False

>>> apply_pseudo_descriptor_get(1, 2, int)
1
>>> apply_pseudo_descriptor_get(1, None, int)
1
>>> apply_pseudo_descriptor_get(B_f, None, int) == (B_f, None, int)
True
>>> apply_pseudo_descriptor_get(B_f, 2, int) == (B_f, 2, int)
True

>>> d = {9:B_f, 6:1}
>>> apply_descriptor_protocol_in_mapping_get_tmay(d, 3, 2, int) == ()
True
>>> apply_descriptor_protocol_in_mapping_get_tmay(d, 6, 2, int) == (1,)
True
>>> apply_descriptor_protocol_in_mapping_get_tmay(d, 9, 2, int) == ((B_f, 2, int),)
True

>>> (key, (obj,), type_of_obj, lead_cls, start_cls, looking_cls) = ('key', ('obj',), 'type_of_obj', 'lead_cls', 'start_cls', 'looking_cls')

>>> extended_protocol_api_to_descriptor_protocol_api(key, (), type_of_obj, lead_cls, start_cls, looking_cls) == (None, type_of_obj)
True
>>> extended_protocol_api_to_descriptor_protocol_api(key, (obj,), type_of_obj, lead_cls, start_cls, looking_cls) == (obj, type_of_obj)
True

>>> extended_protocol__apply_descriptor_protocol_in_mapping_get_tmay___in_super_search(d, 9, (2,), type_of_obj, lead_cls, start_cls, looking_cls) == ((B_f, 2, type_of_obj),)
True
>>> extended_protocol__apply_descriptor_protocol_in_mapping_get_tmay___in_super_search(d, 9, (), type_of_obj, lead_cls, start_cls, looking_cls) == ((B_f, None, type_of_obj),)
True

>>> extended_protocol__apply_descriptor_protocol_in_mapping_get_tmay___in_super_search(d, 6, (2,), type_of_obj, lead_cls, start_cls, looking_cls) == (1,)
True
>>> extended_protocol__apply_descriptor_protocol_in_mapping_get_tmay___in_super_search(d, 6, (), type_of_obj, lead_cls, start_cls, looking_cls) == (1,)
True

>>> extended_protocol__apply_descriptor_protocol_in_mapping_get_tmay___in_super_search(d, 3, (2,), type_of_obj, lead_cls, start_cls, looking_cls) == ()
True
>>> extended_protocol__apply_descriptor_protocol_in_mapping_get_tmay___in_super_search(d, 3, (), type_of_obj, lead_cls, start_cls, looking_cls) == ()
True

#]]]doctest_examples:end

#[[[wwwzzz:begin
#]]]wwwzzz:end
#]]]doc_sections:end


#'''
#]]]__doc__:end

#################################
#HHHHH
__all__ = '''
    is_descriptor
        is_data_descriptor
        is_non_data_descriptor

    extended_protocol_api_to_descriptor_protocol_api
        extended_protocol__apply_descriptor_protocol_in_mapping_get_tmay___in_super_search
        extended_protocol__apply_pseudo_descriptor_get___in_super_search

    apply_descriptor_protocol_in_mapping_get_tmay
    apply_pseudo_descriptor_get
        apply_descriptor_protocol_in_mapping_get_tmay___tmay_cased_result
        apply_pseudo_descriptor_get___cased_result
    '''.split()

#################################
from types import MethodType

#HHHHH
#[[[main_body_src_code:begin
#zzzwww:goto

#[[[zzzwww:begin
def is_descriptor(x, /):
    'has any one of __get__, __set__, __delete__ ==>> descriptor'
    cls = type(x)
    return hasattr(cls, '__get__') or hasattr(cls, '__set__') or hasattr(cls, '__delete__')
def is_data_descriptor(x, /):
    'has any one of __set__, __delete__ ==>> data_descriptor'
    cls = type(x)
    return hasattr(cls, '__set__') or hasattr(cls, '__delete__')
def is_non_data_descriptor(x, /):
    'has __get__ and not any one of __set__, __delete__ ==>> non_data_descriptor'
    cls = type(x)
    return hasattr(cls, '__get__') and not is_data_descriptor(x)


def extended_protocol__apply_descriptor_protocol_in_mapping_get_tmay___in_super_search(pseudo_mapping, key, tmay_instance, type_of_instance, mro0_cls4instance, super0_cls4start_search, curr_cls4storage4descriptor, /):
    (may_instance, owner) = extended_protocol_api_to_descriptor_protocol_api(key, tmay_instance, type_of_instance, mro0_cls4instance, super0_cls4start_search, curr_cls4storage4descriptor)
    return apply_descriptor_protocol_in_mapping_get_tmay(pseudo_mapping, key, may_instance, owner)
def extended_protocol__apply_pseudo_descriptor_get___in_super_search(pseudo_descriptor, key, tmay_instance, type_of_instance, mro0_cls4instance, super0_cls4start_search, curr_cls4storage4descriptor, /):
    (may_instance, owner) = extended_protocol_api_to_descriptor_protocol_api(key, tmay_instance, type_of_instance, mro0_cls4instance, super0_cls4start_search, curr_cls4storage4descriptor)
    return apply_pseudo_descriptor_get(pseudo_descriptor, may_instance, owner)
def extended_protocol_api_to_descriptor_protocol_api(key, tmay_instance, type_of_instance, mro0_cls4instance, super0_cls4start_search, curr_cls4storage4descriptor, /):
    r'''
    super(super0_cls4start_search, mro0_cls4instance).xxx
    super(super0_cls4start_search, instance).xxx
        MethodType(super(super0_cls4start_search, mro0_cls4instance).xxx, instance)
    mro0_cls4instance.__mro__ = [mro0_cls4instance, ..., super0_cls4start_search, ..., curr_cls4storage4descriptor, ..., object]
    {curr_cls4storage4descriptor,super0_cls4start_search} <: mro0_cls4instance <: type_of_instance = type(instance)

    #see: seed.abc.IDescriptor for test_super_in_classmethod/NonDataDescriptor4Echo
    #'''
    [may_instance] = [None] if not tmay_instance else tmay_instance

    if 0:
        #by py_doc
        #see: seed.abc.IDescriptor for py_doc::descriptor_protocol
        #... ... xxxxxxx
        owner = super0_cls4start_search
    else:
        #by py_impl
        #see: seed.abc.IDescriptor for test_super_in_classmethod/NonDataDescriptor4Echo
        owner = type_of_instance
    return (may_instance, owner)
def apply_descriptor_protocol_in_mapping_get_tmay(pseudo_mapping, key, may_instance, owner, /):
    def mk_result_from___get__(get, /):
        return get(may_instance, owner)
    tmay_cased_result = apply_descriptor_protocol_in_mapping_get_tmay___tmay_cased_result(pseudo_mapping, key, mk_result_from___get__)
    if not tmay_cased_result:
        return ()
    [(is_from_mk, result)] = tmay_cased_result
    return (result,)
def apply_pseudo_descriptor_get(pseudo_descriptor, may_instance, owner, /):
    assert owner is not None
    assert may_instance is None or isinstance(may_instance, owner)
    def mk_result_from___get__(get, /):
        return get(may_instance, owner)
    (is_from_mk, result) = apply_pseudo_descriptor_get___cased_result(pseudo_descriptor, mk_result_from___get__)
    return result

def apply_descriptor_protocol_in_mapping_get_tmay___tmay_cased_result(pseudo_mapping, key, mk_result_from___get__, /):
    Nothing = object()
    may_pseudo_descriptor = pseudo_mapping.get(key, Nothing)
    if may_pseudo_descriptor is Nothing:
        return ()
    pseudo_descriptor = may_pseudo_descriptor
    (is_from_mk, result) = apply_pseudo_descriptor_get___cased_result(pseudo_descriptor, mk_result_from___get__)
    return ((is_from_mk, result),)
def apply_pseudo_descriptor_get___cased_result(pseudo_descriptor, mk_result_from___get__, /):
    Nothing = object()
    may_get = getattr(type(pseudo_descriptor), '__get__', Nothing)
    if may_get is Nothing:
        # not_a_descriptor or data_descriptor_without_get
        return (False, pseudo_descriptor)
    #bug:get = may_get
    get_ = may_get
    get = MethodType(get_, pseudo_descriptor)
    return (True, mk_result_from___get__(get))


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



