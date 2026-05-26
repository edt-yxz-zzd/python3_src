#__all__:goto
r'''[[[
e ../../python3_src/seed/math/perfect_kth_root.py
view ../../python3_src/seed/math/factor_pint/perfect_power/detect_perfect_power.py
old:view ../../python3_src/seed/math/factor_pint_as_perfect_power_.py

seed.math.perfect_kth_root
py -m nn_ns.app.debug_cmd   seed.math.perfect_kth_root -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.perfect_kth_root:__doc__ -ht # -ff -df

[[
]]


'#'; __doc__ = r'#'
>>>


py_adhoc_call   seed.math.perfect_kth_root   @factor_pint_as_perfect_power_ =1000
    (10, 3)
py_adhoc_call   seed.math.perfect_kth_root   @factor_pint_as_perfect_power_ =1001
    (1001, 1)

]]]'''#'''
__all__ = r'''
factor_pint_as_perfect_power_
is_kth_power_
    is_square_
    is_cube_
may_perfect_kth_root_
    may_perfect_sqrt_
    may_perfect_cbrt_


'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
___end_mark_of_excluded_global_names__0___ = ...


from seed.math.factor_pint.perfect_power.detect_perfect_power import factor_pint_as_perfect_power_
from seed.math.factor_pint.perfect_power.detect_perfect_power import is_kth_power_, is_square_, is_cube_
from seed.math.factor_pint.perfect_power.detect_perfect_power import may_perfect_kth_root_, may_perfect_sqrt_, may_perfect_cbrt_






__all__
from seed.math.perfect_kth_root import factor_pint_as_perfect_power_
from seed.math.perfect_kth_root import is_kth_power_, is_square_, is_cube_
from seed.math.perfect_kth_root import may_perfect_kth_root_, may_perfect_sqrt_, may_perfect_cbrt_

from seed.math.perfect_kth_root import *
