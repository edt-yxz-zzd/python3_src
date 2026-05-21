#__all__:goto
r'''[[[
e ../../python3_src/seed/debug/print_local_variables.py

seed.debug.print_local_variables
py -m nn_ns.app.debug_cmd   seed.debug.print_local_variables -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.debug.print_local_variables:__doc__ -ht # -ff -df
#######

[[
usage:
    print_eqs(locals(), 'd0 c0 d1 c1')
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.debug.print_local_variables   @f
]]]'''#'''
__all__ = r'''
print_eqs
print_eq
'''.split()#'''
__all__

def print_eq(*args, sep='=', **kwds):
    print(*args, sep='=', **kwds)

def print_eqs(nm2v, nms, /):
    if isinstance(nms, str):
        nms = nms.split()
    for nm in nms:
        print_eq(nm, nm2v[nm])

__all__
from seed.debug.print_local_variables import print_eqs, print_eq
from seed.debug.print_local_variables import *
