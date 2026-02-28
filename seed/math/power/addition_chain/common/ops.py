#__all__:goto
r'''[[[
e ../../python3_src/seed/math/power/addition_chain/common/ops.py

seed.math.power.addition_chain.common.ops
py -m nn_ns.app.debug_cmd   seed.math.power.addition_chain.common.ops -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.power.addition_chain.common.ops:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.math.power.addition_chain.common.ops   @f
]]]'''#'''
__all__ = r'''
串接冫加链序列扌
    就地串接冫加链扌
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.from itertools import islice
#.from seed.tiny_.check import check_type_is, check_int_ge
___end_mark_of_excluded_global_names__0___ = ...

def 串接冫加链序列扌(列表纟加链):
    #.it = map(乸加辗链础链式, 列表纟加链)
    #.x = 加辗链构造式牜幺
    #.for y in  it:
    #.    x = 乸加辗链串接式(x, y)
    #.return x.冃加链
    us = [1]
    for vs in 列表纟加链:
        就地串接冫加链扌(us, vs)
    return tuple(us)


def 就地串接冫加链扌(us, vs, /):
    assert vs[0] == 1
    u = us.pop()
    us.extend(u*v for v in vs)



__all__
from seed.math.power.addition_chain.common.ops import 串接冫加链序列扌, 就地串接冫加链扌
from seed.math.power.addition_chain.common.ops import *
