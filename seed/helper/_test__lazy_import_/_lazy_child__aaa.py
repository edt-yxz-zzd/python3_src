#__all__:goto
r'''[[[
e ../../python3_src/seed/helper/_test__lazy_import_/_lazy_child__aaa.py

seed.helper._test__lazy_import_._lazy_child__aaa
py -m nn_ns.app.debug_cmd   seed.helper._test__lazy_import_._lazy_child__aaa -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.helper._test__lazy_import_._lazy_child__aaa:__doc__ -ht # -ff -df
py_adhoc_call   seed.helper._test__lazy_import_._lazy_child__aaa   @f
from seed.helper._test__lazy_import_._lazy_child__aaa import *
]]]'''#'''
__all__ = r'''
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#from seed.helper.lazy_import import name4on_missing4lazy_attr_mdl
    #def _may_on_missing_(Dict4lazy_attr_mdl, k, /) -> 'v':
from seed.helper.lazy_import import Dict4lazy_attr_mdl
from seed.types.attr.BatchCachedProperty import CachedProperty, BatchCachedProperty, mk_batch_cached_properties_, mk_decorator8injector4batch_cached_property_
#hasattr = __builtins__.hasattr
#hasattr = __builtins__['hasattr']
___end_mark_of_excluded_global_names__0___ = ...

def _may_on_missing_(dict4lazy_attr_mdl, nm, /):
    #if hasattr(__builtins__, nm):
        #return getattr(__builtins__, nm)
    if nm in __builtins__:
        'eg:globals,hasattr,KeyError,...'
        raise {}[nm]
        raise KeyError(nm)
        return __builtins__[nm]

    assert globals() is dict4lazy_attr_mdl
    assert type(dict4lazy_attr_mdl) is Dict4lazy_attr_mdl
    return getattr(_t, nm)

def _mk_a_b(sf, /) -> '(a, b)':
    #or:def _mk_a_b(sf, /) -> ('a', 'b'):
    #or:def _mk_a_b(sf, /) -> '(A, B)#(a, b)':
    print('calling:_mk_a_b()')
    assert isinstance(sf, _T)
    assert not 'a' in vars(sf)
    assert not 'b' in vars(sf)
    a = 666
    b = 999
    return (a, b)
class _T:
    #@cached_property
    @CachedProperty
    def c(sf, /):
        print('calling:c()')
        return 777
    a, b = mk_batch_cached_properties_(_mk_a_b)
_t = _T()


__all__
from seed.helper._test__lazy_import_._lazy_child__aaa import *
