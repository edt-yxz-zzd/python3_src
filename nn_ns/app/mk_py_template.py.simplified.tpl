#__all__:goto
r'''[[[
e zz
#view ../../python3_src/nn_ns/app/mk_py_template.py.tpl

z
py -m nn_ns.app.debug_cmd   z -x # -off_defs
py -m nn_ns.app.doctest_cmd z:__doc__ -ht # -ff -df
#######
from seed.pkg_tools.ModuleReloader import mk_doctestXmodule_reloader_
doctestXmodule_reloader = mk_doctestXmodule_reloader_('', 'z:__doc__', '-ht')
doctestXmodule_reloader(reload_first=False)
doctestXmodule_reloader()
#######

[[
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   z   @f
from z import *
]]]'''#'''
__all__ = r'''
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.from itertools import islice
#.from seed.tiny_.check import check_type_is, check_int_ge
#.
#.from seed.for_libs.for_importlib__reload import clear_later_variables_if_reload_
#.clear_later_variables_if_reload_(globals(), '')
#.    # <<== seed.pkg_tools.ModuleReloader
#.
#.#################################
#.from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
#.with mk_ctx4lazy_import4funcs_(__name__, 'ifNone:_ifNone, ifNonef:_ifNonef'):
#.    from seed.helper.ifNone import ifNone as _ifNone, ifNonef as _ifNonef
#.with mk_ctx4lazy_import4funcs_(__name__):
#.    from seed.debug.print_err import print_err
#.    from seed.iters.flatten_recur import flatten_recur
#.    # def flatten_recur(g:Generator, /, *, value:object=None, is_exc=False, boxed=False):
#.    from seed.func_tools.dot_ import dot_


#.#################################
#.:s/\v^from +([_[:alnum:].]+) +import +([^# ]( *[^# ])*).*/lazy_import4funcs_('\1', '\2', __name__)\rif 0:\0
#.from seed.helper.lazy_import__func import lazy_import4func_, lazy_import4funcs_, force_lazy_imported_func_
#.lazy_import4funcs_('seed.debug.print_err', 'print_err', __name__)
#.if 0:from seed.debug.print_err import print_err
#.
___end_mark_of_excluded_global_names__0___ = ...

#.if __name__ == "__main__":
#.    raise NotImplementedError(Exception, StopIteration)


__all__
#lazy_import4funcs_('z', '', __name__)
from z import *
