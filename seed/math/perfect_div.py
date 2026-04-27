#__all__:goto
r'''[[[
e ../../python3_src/seed/math/perfect_div.py

seed.math.perfect_div
py -m nn_ns.app.debug_cmd   seed.math.perfect_div -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.perfect_div:__doc__ -ht # -ff -df

[[
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.math.perfect_div   @f
]]]'''#'''
__all__ = r'''
may_perfect_div
    tmay_perfect_div
perfect_div

perfect_kth_root_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
#.from seed.tiny_.check import check_type_is, check_int_ge

#.#################################
___end_mark_of_excluded_global_names__0___ = ...

from seed.math.floor_ceil import perfect_div, perfect_kth_root_

__all__




def may_perfect_div(n, d, /):
    'n/int -> d/int{=!=0} -> may q/int{[q*d == n]}'
    (q, r) = divmod(n, d)
    return q if r == 0 else None
def tmay_perfect_div(n, d, /):
    'n/int -> d/int{=!=0} -> tmay q/int{[q*d == n]}'
    if not None is (q:=may_perfect_div(n, d)):
        return (q,)
    return ()
















__all__
from seed.math.perfect_div import perfect_div, perfect_kth_root_
from seed.math.perfect_div import may_perfect_div, tmay_perfect_div
from seed.math.perfect_div import *
