#__all__:goto
r'''[[[
e ../../python3_src/seed/func_tools/func_access.py

seed.func_tools.func_access
py -m nn_ns.app.debug_cmd   seed.func_tools.func_access -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.func_tools.func_access:__doc__ -ht # -ff -df

[[
to be used as named function as postprocess@rgnr
]]

py_adhoc_call   seed.func_tools.func_access   @f
]]]'''#'''
__all__ = r'''
FuncAccess
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.pkg_tools.import_object import import4qobject
#def import4qobject(may_qname4module, may_qname4obj, /):

#.from seed.tiny_.check import check_type_is, check_int_ge
#.
from seed.helper.repr_input import repr_helper
___end_mark_of_excluded_global_names__0___ = ...


class FuncAccess:
    def __init__(sf, may_qname4module, may_qname4obj, /):
        sf._args = (may_qname4module, may_qname4obj)
        #sf._f = None
    def __repr__(sf, /):
        return repr_helper(sf, *sf._args)
    @property
    def func(sf, /):
        try:
            return sf._f
        except AttributeError:
            pass
        f = import4qobject(*sf._args)
        assert callable(f)
        sf._f = f
        return sf.func
    def __call__(sf, /, *args, **kwds):
        return sf.func(*args, **kwds)
#func_access = FuncAccess

__all__
from seed.func_tools.func_access import FuncAccess
from seed.func_tools.func_access import *
