#__all__:goto
r'''[[[
e ../../python3_src/seed/math/inv_mod__py_.py

seed.math.inv_mod__py_
py -m nn_ns.app.debug_cmd   seed.math.inv_mod__py_ -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.inv_mod__py_:__doc__ -ht # -ff -df

[[
@20250204
found: pow(x,-1,M) is ok in py
    when reading about "power ladders" @'Prime numbers-A Computational Perspective(2ed)(2005)(Pomerance).pdf'
]]


>>> inv_mod__py_(7, 3)
5
>>> inv_mod__py_(7, 3)*3%7
1
>>> for i in range(1, 7):
...     assert 1 == inv_mod__py_(7, i)*i%7

py_adhoc_call   seed.math.inv_mod__py_   @inv_mod__py_

]]]'''#'''
__all__ = r'''
inv_mod__py_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
___end_mark_of_excluded_global_names__0___ = ...

def inv_mod__py_(M, x, /):
    'M/int -> x/int -> x**-1%M'
    return pow(x, -1, M)


__all__
from seed.math.inv_mod__py_ import inv_mod__py_
from seed.math.inv_mod__py_ import *
