#__all__:goto
r'''[[[
e ../../python3_src/seed/math/all_factors_of_.py
see:
    view ../../python3_src/seed/math/all_factors_of_.py
        flatten recur
        fancy
        fast
    view ../../python3_src/seed/math/list_all_factors5factorization_.py
        using:II__ft_e_pairs_
        native
        slow

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


>>> sorted_all_factors5factorization_({}, with_factorization=True)
[(1, {})]
>>> sorted_all_factors5factorization_({2:1}, with_factorization=True)
[(1, {}), (2, {2: 1})]
>>> sorted_all_factors5factorization_({2:1, 3:1, 5:1}, with_factorization=True)
[(1, {}), (2, {2: 1}), (3, {3: 1}), (5, {5: 1}), (6, {2: 1, 3: 1}), (10, {2: 1, 5: 1}), (15, {3: 1, 5: 1}), (30, {2: 1, 3: 1, 5: 1})]
>>> sorted_all_factors5factorization_({2:3, 3:2, 5:1}, with_factorization=True)
[(1, {}), (2, {2: 1}), (3, {3: 1}), (4, {2: 2}), (5, {5: 1}), (6, {2: 1, 3: 1}), (8, {2: 3}), (9, {3: 2}), (10, {2: 1, 5: 1}), (12, {2: 2, 3: 1}), (15, {3: 1, 5: 1}), (18, {2: 1, 3: 2}), (20, {2: 2, 5: 1}), (24, {2: 3, 3: 1}), (30, {2: 1, 3: 1, 5: 1}), (36, {2: 2, 3: 2}), (40, {2: 3, 5: 1}), (45, {3: 2, 5: 1}), (60, {2: 2, 3: 1, 5: 1}), (72, {2: 3, 3: 2}), (90, {2: 1, 3: 2, 5: 1}), (120, {2: 3, 3: 1, 5: 1}), (180, {2: 2, 3: 2, 5: 1}), (360, {2: 3, 3: 2, 5: 1})]





iter_unsorted_all_factors5factorization__7pairs7exp_ge1_
>>> [*iter_unsorted_all_factors5factorization__7pairs7exp_ge1_([])]
[1]
>>> [*iter_unsorted_all_factors5factorization__7pairs7exp_ge1_([(2,3)])]
[1, 2, 4, 8]
>>> [*iter_unsorted_all_factors5factorization__7pairs7exp_ge1_([(2,3),(3,2)])]
[1, 3, 9, 2, 6, 18, 4, 12, 36, 8, 24, 72]
>>> [*iter_unsorted_all_factors5factorization__7pairs7exp_ge1_([(2,3),(3,2),(5,1)])]
[1, 5, 3, 15, 9, 45, 2, 10, 6, 30, 18, 90, 4, 20, 12, 60, 36, 180, 8, 40, 24, 120, 72, 360]
>>> [*iter_unsorted_all_factors5factorization__7pairs7exp_ge1_([(2,3),(3,2),(5,1),(7,0)])]
Traceback (most recent call last):
    ...
AssertionError: not all [exp>=1]



>>> [*iter_unsorted_all_factors5factorization__7pairs7exp_ge1_([], with_factorization=True)]
[(1, {})]
>>> [*iter_unsorted_all_factors5factorization__7pairs7exp_ge1_([(2,3)], with_factorization=True)]
[(1, {}), (2, {2: 1}), (4, {2: 2}), (8, {2: 3})]
>>> [*iter_unsorted_all_factors5factorization__7pairs7exp_ge1_([(2,3),(3,2)], with_factorization=True)]
[(1, {}), (3, {3: 1}), (9, {3: 2}), (2, {2: 1}), (6, {2: 1, 3: 1}), (18, {2: 1, 3: 2}), (4, {2: 2}), (12, {2: 2, 3: 1}), (36, {2: 2, 3: 2}), (8, {2: 3}), (24, {2: 3, 3: 1}), (72, {2: 3, 3: 2})]
>>> [*iter_unsorted_all_factors5factorization__7pairs7exp_ge1_([(2,3),(3,2),(5,1)], with_factorization=True)]
[(1, {}), (5, {5: 1}), (3, {3: 1}), (15, {3: 1, 5: 1}), (9, {3: 2}), (45, {3: 2, 5: 1}), (2, {2: 1}), (10, {2: 1, 5: 1}), (6, {2: 1, 3: 1}), (30, {2: 1, 3: 1, 5: 1}), (18, {2: 1, 3: 2}), (90, {2: 1, 3: 2, 5: 1}), (4, {2: 2}), (20, {2: 2, 5: 1}), (12, {2: 2, 3: 1}), (60, {2: 2, 3: 1, 5: 1}), (36, {2: 2, 3: 2}), (180, {2: 2, 3: 2, 5: 1}), (8, {2: 3}), (40, {2: 3, 5: 1}), (24, {2: 3, 3: 1}), (120, {2: 3, 3: 1, 5: 1}), (72, {2: 3, 3: 2}), (360, {2: 3, 3: 2, 5: 1})]



>>> [*iter_unsorted_all_factors5factorization__7pairs7exp_ge1_([], with_factorization=True, imay_max4factor=15)]
[(1, {})]
>>> [*iter_unsorted_all_factors5factorization__7pairs7exp_ge1_([(2,3)], with_factorization=True, imay_max4factor=15)]
[(1, {}), (2, {2: 1}), (4, {2: 2}), (8, {2: 3})]
>>> [*iter_unsorted_all_factors5factorization__7pairs7exp_ge1_([(2,3),(3,2)], with_factorization=True, imay_max4factor=15)]
[(1, {}), (3, {3: 1}), (9, {3: 2}), (2, {2: 1}), (6, {2: 1, 3: 1}), (4, {2: 2}), (12, {2: 2, 3: 1}), (8, {2: 3})]
>>> [*iter_unsorted_all_factors5factorization__7pairs7exp_ge1_([(2,3),(3,2),(5,1)], with_factorization=True, imay_max4factor=15)]
[(1, {}), (5, {5: 1}), (3, {3: 1}), (15, {3: 1, 5: 1}), (9, {3: 2}), (2, {2: 1}), (10, {2: 1, 5: 1}), (6, {2: 1, 3: 1}), (4, {2: 2}), (12, {2: 2, 3: 1}), (8, {2: 3})]



>>> [*iter_unsorted_all_factors5factorization__7pairs7exp_ge1_([], imay_max4factor=15)]
[1]
>>> [*iter_unsorted_all_factors5factorization__7pairs7exp_ge1_([(2,3)], imay_max4factor=15)]
[1, 2, 4, 8]
>>> [*iter_unsorted_all_factors5factorization__7pairs7exp_ge1_([(2,3),(3,2)], imay_max4factor=15)]
[1, 3, 9, 2, 6, 4, 12, 8]
>>> [*iter_unsorted_all_factors5factorization__7pairs7exp_ge1_([(2,3),(3,2),(5,1)], imay_max4factor=15)]
[1, 5, 3, 15, 9, 2, 10, 6, 4, 12, 8]





















py_adhoc_call   seed.math.all_factors_of_   @f
]]]'''#'''
__all__ = r'''
sorted_all_factors5factorization_
    iter_unsorted_all_factors5factorization_
        iter_unsorted_all_factors5factorization__7pairs7exp_ge1_

有序列表冫所有因数巛因数分解扌
    无序枚举冫所有因数巛因数分解扌

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.from itertools import islice
#.from seed.tiny_.check import check_type_is, check_int_ge
___end_mark_of_excluded_global_names__0___ = ...

#grep 'sorted_factors\|iter_factors\|all_factors\|factors_of' -r ../../python3_src/seed/math/ | grep '\[def\]\|@\[\|::\|<-' -v
#list alter names for search:
#   sorted_factors_of_
#   all_factors_of_
#   sorted_all_factors_of_

#   sorted_divisors_of_
#   all_divisors_of_
#   sorted_all_divisors_of_

def sorted_all_factors5factorization_(p2e, /, *, with_factorization=False):
    'p2e/{prime:uint} -> sorted[factor/pint]'
    return sorted(iter_unsorted_all_factors5factorization_(p2e, with_factorization=with_factorization))
def iter_unsorted_all_factors5factorization_(p2e, /, *, with_factorization=False, imay_max4factor=-1):
    #
    'p2e/{prime:uint} -> Iter factor/pint'
    pe_ls = sorted(p2e.items())
    #ps = sorted(p2e.keys())
    #es = [p2e[p] for p in ps]
    #product(*[range(1+e) for e in es])
    assert all(max_e >= 0 for (p, max_e) in pe_ls)
    if not all(max_e > 0 for (p, max_e) in pe_ls):
        pe_ls = [(p,max_e) for (p, max_e) in pe_ls if not max_e == 0]
    return iter_unsorted_all_factors5factorization__7pairs7exp_ge1_(pe_ls, with_factorization=with_factorization, imay_max4factor=imay_max4factor)
def iter_unsorted_all_factors5factorization__7pairs7exp_ge1_(pe_ls, /, *, with_factorization=False, imay_max4factor=-1):
    '[(prime{>=2},uint{>=1})]{no duplicate prime} -> Iter divisor/factor/pint'
    # {strict-sorted} --> {no duplicate prime}
    assert imay_max4factor >= -1
    b_p2e4ft = bool(with_factorization)
    len(pe_ls)
    assert all(max_e >= 1 for (p, max_e) in pe_ls), 'not all [exp>=1]'
    assert all(p >= 2 for (p, max_e) in pe_ls)

    # [imay_max4factor >= -1]
    b_limit = not imay_max4factor == -1
    if b_limit:
        max4factor = imay_max4factor
        match max4factor:
            case 0:
                return;yield
            case 1:
                yield 1 if not b_p2e4ft else (1, {})
                return
        assert max4factor >= 2
    # b_limit => [2 <= max4factor]

    if b_p2e4ft:
        p2e4ft = {}
    eu_ls = []
        # [(e, u)]{len<=len(pe_ls)}
        # [e == gde_(p;u)]
        # [0 <= e <= max_e == pe_ls[j][1]]
    b_next = False
    while 1:
        if b_next:
            if not eu_ls:break
            (e, u) = eu_ls.pop()
            (p, max_e) = pe_ls[len(eu_ls)]
            if not e < max_e:
                # [e == max_e]
                b_next = True
                b_del = True
            else:
                # [0 <= e < max_e]
                e += 1
                # [1 <= e <= max_e]
                u *= p
                # [e == gde_(p;u)]
                if b_limit and not u <= max4factor:
                    b_next = True
                    b_del = not e == 1
                else:
                    # b_limit => [u <= max4factor]
                    # [1 <= e <= max_e]
                    eu_ls.append((e,u))
                        # => [0 <= e <= max_e]
                    if b_p2e4ft:
                        # [1 <= e <= max_e]
                        p2e4ft[p] = e
                    b_next = False
                b_next
            b_next
            if b_next:
                if b_p2e4ft:
                    e = p2e4ft.pop(p, None)
                    assert b_del is (not e is None)
            continue
        else:
            last_u = eu_ls[-1][-1] if eu_ls else 1
            # !! b_limit => [u <= max4factor]
            # !! b_limit => [2 <= max4factor]
            # b_limit => [last_u <= max4factor]
            for (p, max_e) in pe_ls[len(eu_ls):]:
                # [max_e >= 0]
                e = 0
                eu_ls.append((e,last_u))
                    # => [0 <= e <= max_e]
            assert len(eu_ls) == len(pe_ls)
            yield last_u if not b_p2e4ft else (last_u, dict(p2e4ft))
            b_next = True
            continue




def 无序枚举冫所有因数巛因数分解扌(因数分解, /):
    'p2e/{prime:uint} -> Iter factor/pint'
    return iter_unsorted_all_factors5factorization_(因数分解)
def 有序列表冫所有因数巛因数分解扌(因数分解, /):
    'p2e/{prime:uint} -> sorted[factor/pint]'
    return sorted_all_factors5factorization_(因数分解)



__all__
from seed.math.all_factors_of_ import sorted_all_factors5factorization_, iter_unsorted_all_factors5factorization_, iter_unsorted_all_factors5factorization__7pairs7exp_ge1_
#def iter_unsorted_all_factors5factorization__7pairs7exp_ge1_(pe_ls, /, *, with_factorization=False, imay_max4factor=-1):
from seed.math.all_factors_of_ import 有序列表冫所有因数巛因数分解扌, 无序枚举冫所有因数巛因数分解扌

from seed.math.all_factors_of_ import *
