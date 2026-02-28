#__all__:goto
r'''[[[
e ../../python3_src/seed/math/power/addition_chain/short/binary.py

seed.math.power.addition_chain.short.binary
py -m nn_ns.app.debug_cmd   seed.math.power.addition_chain.short.binary -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.power.addition_chain.short.binary:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>> for 靶值 in range(1, 20):
...     加链 = 构造冫加链巛靶值牜二进制拆分扌(靶值)
...     print(f'{靶值}:{加链}')
1:(1,)
2:(1, 2)
3:(1, 2, 3)
4:(1, 2, 4)
5:(1, 2, 4, 5)
6:(1, 2, 3, 6)
7:(1, 2, 3, 6, 7)
8:(1, 2, 4, 8)
9:(1, 2, 4, 8, 9)
10:(1, 2, 4, 5, 10)
11:(1, 2, 4, 5, 10, 11)
12:(1, 2, 3, 6, 12)
13:(1, 2, 3, 6, 12, 13)
14:(1, 2, 3, 6, 7, 14)
15:(1, 2, 3, 6, 7, 14, 15)
16:(1, 2, 4, 8, 16)
17:(1, 2, 4, 8, 16, 17)
18:(1, 2, 4, 8, 9, 18)
19:(1, 2, 4, 8, 9, 18, 19)




py_adhoc_call   seed.math.power.addition_chain.short.binary   @f
]]]'''#'''
__all__ = r'''
构造冫加链巛靶值牜二进制拆分扌
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.tiny_.check import check_type_is, check_int_ge
from seed.math.power.addition_chain.common.check import 检查冫严序加链乊靶值扌
___end_mark_of_excluded_global_names__0___ = ...
def 构造冫加链巛靶值牜二进制拆分扌(靶值, /):
    check_int_ge(1, 靶值)
    u = 靶值
    ls = []
    while u:
        ls.append(u)
        if u&1:
            ls.append(u^1)
        u >>= 1
    ls.pop()
    ls.reverse()
    加链 = tuple(ls)
    检查冫严序加链乊靶值扌(靶值, 加链)
    return 加链


__all__
from seed.math.power.addition_chain.short.binary import 构造冫加链巛靶值牜二进制拆分扌
from seed.math.power.addition_chain.short.binary import *
