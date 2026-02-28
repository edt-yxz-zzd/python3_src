#__all__:goto
r'''[[[
e ../../python3_src/seed/math/power/addition_chain/common/indices.py

seed.math.power.addition_chain.common.indices
py -m nn_ns.app.debug_cmd   seed.math.power.addition_chain.common.indices -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.power.addition_chain.common.indices:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.math.power.addition_chain.common.indices   @f
]]]'''#'''
__all__ = r'''
松序加链讠址引减一讠最大最小加数址引扌
    非末址引讠出点址引复列巛址引减一讠最大最小加数址引扌

严序加链讠址引讠列表纟双加数址引扌
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.tiny_.check import check_type_is, check_int_ge
from seed.math.power.addition_chain.common.check import 检查冫松序加链扌
___end_mark_of_excluded_global_names__0___ = ...

def 松序加链讠址引减一讠最大最小加数址引扌(松序加链, /):
    'us/乸松序加链 -> kmm2ji/[(j/uint,i/uint)]{len==len(us)-1} # [[k:<-[1..=len(kmm2ji)]] -> [(j,i):=kmm2ji[k-1]] -> [[k>j>=i>=0][us[k] == us[j]+us[i]][ts:={t | [t:<-[0..<k]][us[k]-us[t] <- us[:k]]}][j==max(ts)][i==min(ts)]]]'
    检查冫松序加链扌(松序加链)
    us = 松序加链
    显链长 = len(us)-1
    u2min_k = {u:显链长-k for k, u in enumerate(reversed(us))}
    ls = []
    for k, u in enumerate(us):
        if k == 0:
            continue
        for j in reversed(range(k)):
            if not None is (i:=u2min_k.get(us[k] -us[j])):
                break
        else:
            raise 000
        ls.append((j,i))

    kmm2ji = tuple(ls)
    return kmm2ji

def 非末址引讠出点址引复列巛址引减一讠最大最小加数址引扌(kmm2ji, /):
    'kmm2ji/[(j/uint,i/uint)] -> j2ks/[[k/uint]]'
    显链长 = len(kmm2ji)
    j2ks = [[] for j in range(显链长)]
    for kmm in range(显链长):
        k = kmm+1
        for j in kmm2ji[kmm]:
            j2ks[j].append(k)
    j2ks = tuple(map(tuple, j2ks))

    return j2ks



def 严序加链讠址引讠列表纟双加数址引扌(严序加链, /, *, 欤带逆映射=False):
    '严序加链 -> [[(大加数址引, 小加数址引)]]'
    assert 严序加链[0] == 1
    k2u = 严序加链
    k2jis = []
    u2k = {}
    _uk = 1
    for k, uk in enumerate(k2u):
        check_int_ge(_uk, uk)
        777;_uk = 1+uk
        if not k == u2k.setdefault(uk, k):raise TypeError(严序加链, k, uk)
        k2jis.append(jis:=[])
        for j in reversed(range(k)):
            uj = k2u[j]
            ui = uk -uj
            if not ui <= uj:
                break
            if not None is (i:=u2k.get(ui)):
                jis.append((j, i))
        if bool(jis) is (k == 0 and uk == 1):raise TypeError(严序加链, k, uk, jis)
    k2jis
    assert not k2jis[0]
    #.kmm2jis = tuple(map(tuple, k2jis[1:]))
    k2jis = tuple(map(tuple, k2jis))
    return k2jis if not 欤带逆映射 else (k2jis, u2k)




__all__
from seed.math.power.addition_chain.common.indices import 松序加链讠址引减一讠最大最小加数址引扌, 非末址引讠出点址引复列巛址引减一讠最大最小加数址引扌
from seed.math.power.addition_chain.common.indices import 严序加链讠址引讠列表纟双加数址引扌
from seed.math.power.addition_chain.common.indices import *
