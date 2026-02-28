#__all__:goto
r'''[[[
e ../../python3_src/seed/math/power/addition_chain/common/check.py

seed.math.power.addition_chain.common.check
py -m nn_ns.app.debug_cmd   seed.math.power.addition_chain.common.check -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.power.addition_chain.common.check:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.math.power.addition_chain.common.check   @f
]]]'''#'''
__all__ = r'''
检查冫严序加链乊靶值扌
    检查冫严序加链扌
    检查冫严序加链内容扌

检查冫松序加链乊靶值扌
    检查冫松序加链扌
    检查冫松序加链内容扌

检查冫散漫加链乊靶值扌
    检查冫散漫加链扌
    检查冫散漫加链内容扌

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from itertools import pairwise
from seed.tiny_.check import check_type_is, check_int_ge, check_int_ge_le
___end_mark_of_excluded_global_names__0___ = ...


def 检查冫严序加链乊靶值扌(靶值, 加链, /, *, 严序丷松序=False, 欤偏序=False):
    check_int_ge(1, 靶值)
    检查冫严序加链扌(加链, 严序丷松序=严序丷松序, 欤偏序=欤偏序)
    if not 加链[-1] == 靶值:raise TypeError
def 检查冫严序加链扌(加链, /, *, 严序丷松序=False, 欤偏序=False):
    check_type_is(tuple, 加链)
    检查冫严序加链内容扌(加链, 严序丷松序=严序丷松序, 欤偏序=欤偏序)
def 检查冫严序加链内容扌(加链, /, *, 严序丷松序=False, 欤偏序=False):
    check_type_is(bool, 严序丷松序)
    check_type_is(bool, 欤偏序)
    if not len(加链) > 0:raise TypeError
    check_int_ge_le(1, 1, 加链[0])
    if 欤偏序:
        for v in 加链:
            check_int_ge(1, v)
    else:
        b = not 严序丷松序
        for u, v in pairwise(加链):
            check_int_ge(b+u, v)
        del b

    v2j = {1:0}
    j2kk = [None]
    it = enumerate(加链)
    777; next(it)
    for j, v in it:
        v2j[v] = j
        for ka in range(j)[::-1]:
            a = 加链[ka]
            b = v -a
            if a < b and not 欤偏序: raise Exception(f'非加链')#ValueError
            if not None is (kb:=v2j.get(b)):
                assert ka >= kb >= 0
                j2kk.append((ka, kb))
                break
        else:
            if 欤偏序: raise Exception(f'非加链')#ValueError
            raise 000
    return (j2kk, v2j)



def 检查冫松序加链乊靶值扌(靶值, 加链, /):
    检查冫严序加链乊靶值扌(靶值, 加链, 严序丷松序=True)
def 检查冫松序加链扌(加链, /):
    检查冫严序加链扌(加链, 严序丷松序=True)
def 检查冫松序加链内容扌(加链, /):
    检查冫严序加链内容扌(加链, 严序丷松序=True)


def 检查冫散漫加链乊靶值扌(靶值, 加链, /):
    检查冫严序加链乊靶值扌(靶值, 加链, 欤偏序=True)
def 检查冫散漫加链扌(加链, /):
    检查冫严序加链扌(加链, 欤偏序=True)
def 检查冫散漫加链内容扌(加链, /):
    检查冫严序加链内容扌(加链, 欤偏序=True)



#def 欤严序加链扌(x, /):
#def 欤松序加链扌(x, /):

__all__
from seed.math.power.addition_chain.common.check import 检查冫严序加链乊靶值扌, 检查冫严序加链扌, 检查冫严序加链内容扌
from seed.math.power.addition_chain.common.check import 检查冫松序加链乊靶值扌, 检查冫松序加链扌, 检查冫松序加链内容扌
from seed.math.power.addition_chain.common.check import 检查冫散漫加链乊靶值扌, 检查冫散漫加链扌, 检查冫散漫加链内容扌
from seed.math.power.addition_chain.common.check import *
