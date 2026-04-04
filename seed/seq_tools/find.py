#__all__:goto
r'''[[[
e ../../python3_src/seed/seq_tools/find.py

seed.seq_tools.find
py -m nn_ns.app.debug_cmd   seed.seq_tools.find -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.seq_tools.find:__doc__ -ht # -ff -df
#######

[[
list.index
has no:list.find
]]


'#'; __doc__ = r'#'
>>> find7seq_([3, 5, 6, 7], 6)
2
>>> find7seq_([3, 5, 6, 7], 6, 2)
2
>>> find7seq_([3, 5, 6, 7], 6, 2, -1)
2
>>> find7seq_([3, 5, 6, 7], 6, 3)
-1
>>> find7seq_([3, 5, 6, 7], 6, 0, -2)
-1

>>> find7iter_(iter([3, 5, 6, 7]), 6)
2
>>> find7iter_(iter([3, 5, 6, 7]), 6, offset=1000)
1002
>>> find7iter_(iter([3, 5, 6, 7]), 999)
-1


py_adhoc_call   seed.seq_tools.find   @f
]]]'''#'''
__all__ = r'''
find7seq_
find7iter_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
#.from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.#################################
#.from seed.helper.lazy_import__func7dict import lazy_import__funcs7dict_
#.(check_type_is, check_int_ge, _ifNone) = lazy_import__funcs7dict_(__name__ or globals() or locals(), 'seed.tiny_.check',  'check_type_is, check_int_ge      ifNone:_ifNone')
#.#################################
#.def mk_context4lazy_import_registered_names_(qnm4mdl7inject, qnm4pseudo_mdl7import, name7importZqnm4mdl, name7importZalias7inject={}, may_bifix4lazy_name7import=None, lazy_name7importZoriginal_name7import={}):
#.from seed.helper.lazy_import__func7context7register import mk_context4lazy_import_registered_names_, name7importZqnm4mdl_7tiny
#.with mk_context4lazy_import_registered_names_(__name__, 'seed._lazy_', name7importZqnm4mdl_7tiny):
#.    from seed._lazy_ import print_err, fst, echo, ifNone
#.#################################
#.from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
#.with mk_ctx4lazy_import4funcs_(__name__):
#.    from itertools import islice
#.    from functools import cached_property
#.    from seed.for_libs.for_functools.cached_property import cached_property
#.    from seed.types.CachedProperty import CachedProperty, mk_cached_propertyT_
#.    from seed.func_tools.dot2 import dot
#.    from seed.tiny_.check import check_type_is, check_int_ge
#.with mk_ctx4lazy_import4funcs_(__name__, arbitrary_ok=True):
#.    from seed.data_funcs.lnkls import rglnkls_ops# empty_rglnkls, mk_empty_rglnkls, rglnkls_ipush_right, rglnkls_ipop_right, rglnkls2reversed_iterable, rglnkls5iterable
#.with mk_ctx4lazy_import4funcs_(__name__, 'ifNone:_ifNone, ifNonef:_ifNonef'):
#.    from seed.helper.ifNone import ifNone as _ifNone, ifNonef as _ifNonef
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

def find7iter_(iterable, x, /, *, offset=0):
    'Iter x -> x -> imay_idx'
    xs = [x]
    for j, y in enumerate(iterable, offset):
        if y in xs:
            return j
    return -1

def find7seq_(seq, x, begin=None, end=None, /):
    '[x] -> x -> imay_idx'
    try:
        return seq.index(x, begin, end)
            # None => ^TypeError: slice indices must be integers or have an __index__ method
    except ValueError:
        return -1
def find7seq_(seq, x, /, *args):
    try:
        return seq.index(x, *args)
    except ValueError:
        return -1

__all__
from seed.seq_tools.find import find7seq_, find7iter_
from seed.seq_tools.find import *
