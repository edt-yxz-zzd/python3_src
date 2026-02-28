#__all__:goto
r'''[[[
e ../../python3_src/seed/math/all_factors_of_.py

seed.math.all_factors_of_
py -m nn_ns.app.debug_cmd   seed.math.all_factors_of_ -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.all_factors_of_:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>> sorted_all_factors5factorization_({})
[1]
>>> sorted_all_factors5factorization_({2:0})
[1]
>>> sorted_all_factors5factorization_({2:1})
[1, 2]
>>> sorted_all_factors5factorization_({2:2})
[1, 2, 4]
>>> sorted_all_factors5factorization_({2:2, 3:0})
[1, 2, 4]
>>> sorted_all_factors5factorization_({2:2, 3:1})
[1, 2, 3, 4, 6, 12]
>>> sorted_all_factors5factorization_({2:2, 3:2})
[1, 2, 3, 4, 6, 9, 12, 18, 36]
>>> sorted_all_factors5factorization_({2:2, 3:2, 5:0})
[1, 2, 3, 4, 6, 9, 12, 18, 36]
>>> sorted_all_factors5factorization_({2:2, 3:2, 5:1})
[1, 2, 3, 4, 5, 6, 9, 10, 12, 15, 18, 20, 30, 36, 45, 60, 90, 180]
>>> sorted_all_factors5factorization_({2:2, 3:2, 5:2})
[1, 2, 3, 4, 5, 6, 9, 10, 12, 15, 18, 20, 25, 30, 36, 45, 50, 60, 75, 90, 100, 150, 180, 225, 300, 450, 900]
>>> sorted_all_factors5factorization_({2:0, 3:0, 5:2})
[1, 5, 25]
>>> sorted_all_factors5factorization_({2:1, 3:0, 5:2})
[1, 2, 5, 10, 25, 50]
>>> sorted_all_factors5factorization_({2:1, 3:1, 5:2})
[1, 2, 3, 5, 6, 10, 15, 25, 30, 50, 75, 150]
>>> sorted_all_factors5factorization_({2:2, 3:1, 5:1})
[1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60]
>>> sorted_all_factors5factorization_({2:1, 3:1, 5:1})
[1, 2, 3, 5, 6, 10, 15, 30]





py_adhoc_call   seed.math.all_factors_of_   @f
]]]'''#'''
__all__ = r'''
sorted_all_factors5factorization_
    iter_unsorted_all_factors5factorization_

有序列表冫所有因数巛因数分解扌
    无序枚举冫所有因数巛因数分解扌

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.from itertools import islice
#.from seed.tiny_.check import check_type_is, check_int_ge
___end_mark_of_excluded_global_names__0___ = ...

#grep 'sorted_factors\|iter_factors\|all_factors\|factors_of' -r ../../python3_src/seed/math/ | grep '\[def\]\|@\[\|::\|<-' -v
#sorted_factors_of_
#all_factors_of_
#sorted_all_factors_of_
def sorted_all_factors5factorization_(p2e, /):
    'p2e/{prime:uint} -> sorted[factor/pint]'
    return sorted(iter_unsorted_all_factors5factorization_(p2e))
def iter_unsorted_all_factors5factorization_(p2e, /):
    #
    'p2e/{prime:uint} -> Iter factor/pint'
    pe_ls = sorted(p2e.items())
    #ps = sorted(p2e.keys())
    #es = [p2e[p] for p in ps]
    #product(*[range(1+e) for e in es])
    #assert all(max_e >= 0 for (p, max_e) in pe_ls)
    pe_ls = [(p,max_e) for (p, max_e) in pe_ls if not max_e == 0]
    assert all(max_e >= 1 for (p, max_e) in pe_ls)

    eu_ls = []
    b_next = False
    while 1:
        if b_next:
            if not eu_ls:break
            (e, u) = eu_ls.pop()
            (p, max_e) = pe_ls[len(eu_ls)]
            if not e < max_e:
                #if e == max_e:
                b_next = True
                continue
            # [e < max_e]
            e += 1
            # [e <= max_e]
            u *= p
            eu_ls.append((e,u))
            b_next = False
            continue
        else:
            last_u = eu_ls[-1][-1] if eu_ls else 1
            for (p, max_e) in pe_ls[len(eu_ls):]:
                # [max_e >= 0]
                e = 0
                eu_ls.append((e,last_u))
            assert len(eu_ls) == len(pe_ls)
            yield last_u
            b_next = True
            continue




def 无序枚举冫所有因数巛因数分解扌(因数分解, /):
    'p2e/{prime:uint} -> Iter factor/pint'
    return iter_unsorted_all_factors5factorization_(因数分解)
def 有序列表冫所有因数巛因数分解扌(因数分解, /):
    'p2e/{prime:uint} -> sorted[factor/pint]'
    return sorted_all_factors5factorization_(因数分解)



__all__
from seed.math.all_factors_of_ import sorted_all_factors5factorization_, iter_unsorted_all_factors5factorization_
from seed.math.all_factors_of_ import 有序列表冫所有因数巛因数分解扌, 无序枚举冫所有因数巛因数分解扌

from seed.math.all_factors_of_ import *
