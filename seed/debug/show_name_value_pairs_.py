#__all__:goto
r'''[[[
e ../../python3_src/seed/debug/show_name_value_pairs_.py

seed.debug.show_name_value_pairs_
py -m nn_ns.app.debug_cmd   seed.debug.show_name_value_pairs_ -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.debug.show_name_value_pairs_:__doc__ -ht # -ff -df
#######

[[
come_from:
view ../../python3_src/seed/helper/forest_tabulation5modular_func.py
]]


'#'; __doc__ = r'#'
>>> xnms = parse_xnms_('(a, [b, c], d, (e,))')
>>> xnms
('a', ['b', 'c'], 'd', ('e',))
>>> show_name_value_pairs_(xnms, (1, [2, 3], 999, (555,)))
a=1
b=2
c=3
d=999
e=555
>>> show_name_value_pairs_(xnms, (1, [2, 3], 999, (555,)), sep='==')
a==1
b==2
c==3
d==999
e==555


py_adhoc_call   seed.debug.show_name_value_pairs_   @f
]]]'''#'''
__all__ = r'''
errshow_name_value_pairs_
    show_name_value_pairs_

iter_name_value_pairs_
parse_xnms_

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.helper.stable_repr import stable_repr
import sys
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

def errshow_name_value_pairs_(xnms, xs, /, **kwds4print):
    show_name_value_pairs_(xnms, xs, file=sys.stderr)
def show_name_value_pairs_(xnms, xs, /, sep='=', **kwds4print):
    for nm, val in iter_name_value_pairs_(xnms, xs):
        print(nm, stable_repr(val), sep=sep, **kwds4print)
def iter_name_value_pairs_(xnms, xs, /):
    'xnms/[(str|xnms)] -> xs/tuple{(value|xs)}[#same tree struct as xnms#] -> Iter (str, value)'
    if not len(xnms) == len(xs):raise Exception(xnms, len(xnms), len(xs))
    for xnm, x in zip(xnms, xs):
        match xnm:
            case (tuple() | list()) as _xnms:
                _xs = x
                yield from iter_name_value_pairs_(_xnms, _xs)
            case str() as nm:
                val = x
                yield (nm, val)
            case _:
                raise TypeError(type(xnm))
class _D(dict):
    def __missing__(sf, k, /):
        sf[k] = k
        return k
def __():
    # => "sf[k] = k"
    d = _D()
    if not d[1] == 1: raise 000
    if not 1 in d: raise 000
    if not len(d) == 1: raise 000
if 0:__()

def parse_xnms_(s, /):
    '-> T/[(str|T)]'
    return eval(s, _D())
def _old__parse_nms_(s, /):
    '-> [str]'
    for c in '(,)':
        s = s.replace(c, ' ')
    nms = s.split()
    return tuple(nms)



__all__
from seed.debug.show_name_value_pairs_ import errshow_name_value_pairs_, show_name_value_pairs_, iter_name_value_pairs_, parse_xnms_
from seed.debug.show_name_value_pairs_ import *
