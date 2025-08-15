#__all__:goto
r'''[[[
e ../../python3_src/seed/for_libs/for_importlib__reload.py

seed.for_libs.for_importlib__reload
py -m nn_ns.app.debug_cmd   seed.for_libs.for_importlib__reload -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.for_libs.for_importlib__reload:__doc__ -ht # -ff -df

[[
源起:
view ../../python3_src/seed/pkg_tools/ModuleReloader.py
]]
[[
usage:
from seed.for_libs.for_importlib__reload import clear_later_variables_if_reload_
clear_later_variables_if_reload_(globals(), '')
]]



>>> d = {111:222, 333:444}
>>> clear_later_variables_if_reload_(d, [555,777])
>>> d.update({111:-222, 555:-666, -999:-999})
>>> clear_later_variables_if_reload_(d, [555,777])
>>> d == {111: -222, 333: 444, clear_later_variables_if_reload_: frozenset({clear_later_variables_if_reload_, 777, 555, 333, 111}), 555: -666}
True

]]]'''#'''
__all__ = r'''
clear_later_variables_if_reload_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.tiny_.containers import mk_tuple__split_first_if_str
___end_mark_of_excluded_global_names__0___ = ...

def clear_later_variables_if_reload_(_globals, extra_nms8ok='', /):
    key4nms8snapshot = clear_later_variables_if_reload_
    b_reload = key4nms8snapshot in _globals
    if b_reload:
        nms8snapshot = _globals[key4nms8snapshot]
        nms8del = _globals.keys() -nms8snapshot
        for nm in nms8del:
            del _globals[nm]
    #else:
    if 1:
        extra_nms8ok = mk_tuple__split_first_if_str(extra_nms8ok)
        nms8snapshot = frozenset({*_globals.keys(), *extra_nms8ok, key4nms8snapshot})
        _globals[key4nms8snapshot] = nms8snapshot

__all__
from seed.for_libs.for_importlib__reload import clear_later_variables_if_reload_
clear_later_variables_if_reload_(globals(), '')
from seed.for_libs.for_importlib__reload import *
