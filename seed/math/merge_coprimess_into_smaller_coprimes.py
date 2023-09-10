#__all__:goto
r'''[[[
e ../../python3_src/seed/math/merge_coprimess_into_smaller_coprimes.py
    <==>
    view ../../python3_src/nn_ns/math_nn/mk_coprimes.py
    from nn_ns.math_nn.mk_coprimes import deep_gcd_into_3_coprimess, split_hints_into_coprimess__by_gcd, split_pint_into_coprimess__by_gcd_hints
view ../../python3_src/seed/math/lcm_parts_of.py






seed.math.merge_coprimess_into_smaller_coprimes
py -m nn_ns.app.debug_cmd   seed.math.merge_coprimess_into_smaller_coprimes -x
py -m nn_ns.app.doctest_cmd seed.math.merge_coprimess_into_smaller_coprimes:__doc__ -ff -v
py_adhoc_call   seed.math.merge_coprimess_into_smaller_coprimes   @f



>>> merge = merge_coprimess_into_smaller_coprimes
>>> merge([[-2**7 * 5**5, 11**4 * 13], [2**3 * 3**6, -5**2 * 13**3]], validate=True)
(2, 5, 13, 14641, 729)
>>> (2, 5, 13, 14641, 729) == (2, 5, 13, 11**4, 3**6)
True

>>> semi_factor_coprimess_via_gcd([[2**7 * 5**5, 11**4 * 13], [2**3 * 3**6, 5**2 * 13**3]])
((2, 5, 13, 14641, 729), (((7, 5, 0, 0, 0), (0, 0, 1, 1, 0)), ((3, 0, 0, 0, 1), (0, 2, 3, 0, 0))))


#]]]'''
__all__ = r'''

merge_coprimess_into_smaller_coprimes
    verify4merge_coprimess_into_smaller_coprimes
    semi_factor_coprimess_via_gcd

'''.split()#'''
__all__

from seed.math.gcd import gcd # gcd_many, are_coprime
from seed.tiny_.check import check_uint_lt, check_int_ge_lt, check_int_ge, check_int_ge_le
from seed.tiny import check_type_is
from seed.math.gcd import gcd
from seed.func_tools.recur5yield import recur5yield__list__echo__echo #, recur5yield__list__echo__off, recur5yield__list__0func__echo, recur5yield__list__0func__off
from seed.tiny import null_tuple, mk_tuple
#from seed.math.max_power_of_base_as_factor_of_ import max_power_of_base_as_factor_of_
from seed.math.semi_factor_pint_via_trial_division import semi_factor_pint_via_trial_division
from seed.math.are_pairwise_coprime import are_pairwise_coprime



def _remove_gcd_pow(n, g, /):
    'n -> g -> m # [n==m*g**k][m%g=!=0]'
    # [m =[def]= n//g**max_power_of_base_as_factor_of_(g, n)]
    assert n > 0
    assert g > 1
    m = n
    pows = [g]
        # [pows[i] == g**(2**i)]
    while 1:
        gg = pows[-1]
        q, r = divmod(m, gg)
        if r:
            pows.pop()
            k = (1<<len(pows)) -1
            break
        m = q
        pows.append(gg**2)
    k, m
    # [n == m*g**k]
    while pows:
        gg = pows.pop()
        q, r = divmod(m, gg)
        if r==0:
            m = q
            k += 1<<len(pows)
    assert not m%g == 0
    assert n == m*g**k
    return m


def __():
  def on_1_1(lhs, rhs, /):
    'lhs/ge1 -> rhs/ge1 -> (lonly_factor/ge1, common_factors/[ge2], ronly_factor/ge1){[are_pairwise_coprime([lonly_factor,*common_factors,ronly_factor])][?ks. lhs == lonly_factor * II ft**k {(ft,k)<-zip common_factors ks}][?ks. rhs == ronly_factor * II ft**k {(ft,k)<-zip common_factors ks}]}'
    assert lhs > 0
    assert rhs > 0
    if not lhs < rhs:
        if lhs == rhs:
            g = lhs
            return (1, (g,), 1)
        # [lhs > rhs]
        (ronly_factor, common_factors, lonly_factor) = on_1_1(rhs, lhs)
        return (lonly_factor, common_factors, ronly_factor)

    # [lhs < rhs]
    g = gcd(lhs, rhs)
    if g == 1:
        return (lhs, (), rhs)
    if 0:
        #bug:
        if g == lhs:
            return (1, (g,), rhs//g)
    lhs_g = _remove_gcd_pow(lhs, g)
    rhs_g = _remove_gcd_pow(rhs, g)
    # [gcd(lhs_g, rhs_g)==1]
    # [are_pairwise_coprime([lhs_g, rhs_g])]
    (lonly_factor, lcommon_factors, g_lhs) = on_1_1(lhs_g, g)
    # [are_pairwise_coprime([lonly_factor, *lcommon_factors, g_lhs])]

    # !! [are_pairwise_coprime([lhs_g, rhs_g])]
    # [are_pairwise_coprime([lonly_factor, *lcommon_factors, rhs_g])]

    rhs_g_lhs = _remove_gcd_pow(rhs_g, g_lhs)
    (g_lhs_rhs, rcommon_factors, ronly_factor) = on_1_1(g_lhs, rhs_g_lhs)
    # [are_pairwise_coprime([g_lhs_rhs, *rcommon_factors, ronly_factor])]
    # !! [are_pairwise_coprime([lonly_factor, *lcommon_factors, g_lhs])]
    # [are_pairwise_coprime([lonly_factor, *lcommon_factors, g_lhs_rhs])]

    # !! [are_pairwise_coprime([lonly_factor, *lcommon_factors, rhs_g])]
    # [are_pairwise_coprime([lonly_factor, *lcommon_factors, *rcommon_factors, ronly_factor])]

    # !! [are_pairwise_coprime([lonly_factor, *lcommon_factors, g_lhs_rhs])]
    # !! [are_pairwise_coprime([g_lhs_rhs, *rcommon_factors, ronly_factor])]
    # !! [are_pairwise_coprime([lonly_factor, *lcommon_factors, *rcommon_factors, ronly_factor])]
    # [are_pairwise_coprime([lonly_factor, *lcommon_factors, g_lhs_rhs, *rcommon_factors, ronly_factor])]
    lonly_factor, ronly_factor
    if g_lhs_rhs == 1:
        common_factors = (*lcommon_factors, *rcommon_factors)
    else:
        common_factors = (*lcommon_factors, g_lhs_rhs, *rcommon_factors)
    return (lonly_factor, common_factors, ronly_factor)
  def on_s_s(lcoprimes, rcoprimes, /):
    'lcoprimes/[ge1] -> rcoprimes[ge1] -> (lonly_factors/[ge1]{len=len lcoprimes}, common_factors/[ge2], ronly_factors/[ge1]{len=len rcoprimes})'

@recur5yield__list__echo__echo
def on_1_1_(common_factors4out, lhs, rhs, /):
    'common_factors4out/[ge2] -> lhs/ge1 -> rhs/ge1 -> (lonly_factor/ge1, ronly_factor/ge1){[are_pairwise_coprime([lonly_factor,*common_factors,ronly_factor])][?ks. lhs == lonly_factor * II ft**k {(ft,k)<-zip common_factors ks}][?ks. rhs == ronly_factor * II ft**k {(ft,k)<-zip common_factors ks}]}'
    assert lhs > 0
    assert rhs > 0
    (lonly_factor, ronly_factor) = yield _on_1_1_(common_factors4out, lhs, rhs)
    return True, (lonly_factor, ronly_factor)
def _on_1_1_(common_factors4out, lhs, rhs, /):
    if not lhs < rhs:
        if lhs == rhs:
            g = lhs
            if not g == 1:
                common_factors4out.append(g)
            return True, (1, 1)
        # [lhs > rhs]
        (ronly_factor, lonly_factor) = yield _on_1_1_(common_factors4out, rhs, lhs)
        return True, (lonly_factor, ronly_factor)

    # [lhs < rhs]
    g = gcd(lhs, rhs)
    if g == 1:
        return True, (lhs, rhs)
    if 0:
        #bug:
        if g == lhs:
            common_factors4out.append(g)
            return True, (1, rhs//g)
    lhs_g = _remove_gcd_pow(lhs, g)
    rhs_g = _remove_gcd_pow(rhs, g)
    # [gcd(lhs_g, rhs_g)==1]
    # [are_pairwise_coprime([lhs_g, rhs_g])]
    (lonly_factor, g_lhs) = yield _on_1_1_(common_factors4out, lhs_g, g)
        #output: lcommon_factors
    # [are_pairwise_coprime([lonly_factor, *lcommon_factors, g_lhs])]

    # !! [are_pairwise_coprime([lhs_g, rhs_g])]
    # [are_pairwise_coprime([lonly_factor, *lcommon_factors, rhs_g])]

    if g_lhs == 1:
        rhs_g_lhs = rhs_g
        (g_lhs_rhs, ronly_factor) = (g_lhs, rhs_g_lhs)
            #output: rcommon_factors:=[]
    else:
        rhs_g_lhs = _remove_gcd_pow(rhs_g, g_lhs)
        (g_lhs_rhs, ronly_factor) = yield _on_1_1_(common_factors4out, g_lhs, rhs_g_lhs)
            #output: rcommon_factors
    # [are_pairwise_coprime([g_lhs_rhs, *rcommon_factors, ronly_factor])]
    # !! [are_pairwise_coprime([lonly_factor, *lcommon_factors, g_lhs])]
    # [are_pairwise_coprime([lonly_factor, *lcommon_factors, g_lhs_rhs])]

    # !! [are_pairwise_coprime([lonly_factor, *lcommon_factors, rhs_g])]
    # [are_pairwise_coprime([lonly_factor, *lcommon_factors, *rcommon_factors, ronly_factor])]

    # !! [are_pairwise_coprime([lonly_factor, *lcommon_factors, g_lhs_rhs])]
    # !! [are_pairwise_coprime([g_lhs_rhs, *rcommon_factors, ronly_factor])]
    # !! [are_pairwise_coprime([lonly_factor, *lcommon_factors, *rcommon_factors, ronly_factor])]
    # [are_pairwise_coprime([lonly_factor, *lcommon_factors, g_lhs_rhs, *rcommon_factors, ronly_factor])]
    lonly_factor, ronly_factor
    if not g_lhs_rhs == 1:
        # had output: lcommon_factors
        # had output: rcommon_factors
        common_factors4out.append(g_lhs_rhs)
    return True, (lonly_factor, ronly_factor)


def __():
  def on_s_s_(common_factors4out, lcoprimes, rcoprimes, /):
    'common_factors4out/[ge2] -> lcoprimes/[ge1] -> rcoprimes[ge1] -> (lonly_factors/[ge1]{len=len lcoprimes}, ronly_factors/[ge1]{len=len rcoprimes})'
    #rcoprimes = mk_tuple(rcoprimes)
    ronly_factors = []
    lonly_factors = []
    for lhs in lcoprimes:
        lonly_factor = lhs
        for rhs in rcoprimes:
            (lonly_factor, ronly_factor) = on_1_1_(common_factors4out, lonly_factor, rhs)
            ronly_factors.append(ronly_factor)
        rcoprimes = ronly_factors
        ronly_factors = []
        lonly_factors.append(lonly_factor)
    ronly_factors = mk_tuple(rcoprimes)
    lonly_factors = mk_tuple(lonly_factors)
    return lonly_factors, ronly_factors

def on_s_s__filterout1_(common_factors4out, lcoprimes, rcoprimes, /):
    'common_factors4out/[ge2] -> lcoprimes/[ge1] -> rcoprimes[ge1] -> (lonly_factors/[ge2]{len<=len lcoprimes}, ronly_factors/[ge2]{len<=len rcoprimes})'
    #rcoprimes = mk_tuple(rcoprimes)
    ronly_factors = []
    lonly_factors = []
    for lhs in lcoprimes:
        if lhs == 1:continue
        lonly_factor = lhs
        for rhs in rcoprimes:
            if rhs == 1:continue
            (lonly_factor, ronly_factor) = on_1_1_(common_factors4out, lonly_factor, rhs)
            if ronly_factor == 1:continue
            ronly_factors.append(ronly_factor)
        rcoprimes = ronly_factors
        ronly_factors = []
        if lonly_factor == 1:continue
        lonly_factors.append(lonly_factor)
    ronly_factors = mk_tuple(u for u in rcoprimes if not u==1)
    lonly_factors = mk_tuple(lonly_factors)
    return lonly_factors, ronly_factors





def merge_coprimess_into_smaller_coprimes(coprimess, /, *, validate=False):
    'coprimess/(Iter (Iter int{=!=0}){pairwise_coprime}) -> coprimes/(tuple<int{>=2}>){pairwise_coprime}'
    coprimess8in = [*map(list, coprimess)]
    1;  del coprimess
    #check
    for us in coprimess8in:
        for u in us:
            check_type_is(int, u)
            if u == 0: raise ValueError
    #abs
    for i, us in enumerate(coprimess8in):
        for j in range(len(us)):
            u = us[j]
            if u < 0:
                us[j] = abs(u)
    #

    #it = iter(coprimess8in)
    lcoprimes = null_tuple
    for rcoprimes in coprimess8in:
        common_factors4out = []
        (lonly_factors, ronly_factors) = on_s_s__filterout1_(common_factors4out, lcoprimes, rcoprimes)
        common_factors4out.extend(lonly_factors)
        common_factors4out.extend(ronly_factors)
        lcoprimes = common_factors4out
    coprimes8out = mk_tuple(lcoprimes)
    assert all(u >= 2 for u in coprimes8out)
    if validate:
        verify4merge_coprimess_into_smaller_coprimes(coprimess8in, coprimes8out)
    return coprimes8out

def verify4merge_coprimess_into_smaller_coprimes(coprimess8in, coprimes8out, /):
    check_type_is(tuple, coprimes8out)
    if not all(u >= 2 for u in coprimes8out):raise TypeError
    if not are_pairwise_coprime(coprimes8out):raise TypeError

    factors = set()
    for js in coprimess8in:
        for j in js:
            (factor2exp, unfactored_part) = semi_factor_pint_via_trial_division(coprimes8out, abs(j))
            if not unfactored_part == 1:raise TypeError
            assert all(e >= 1 for e in factor2exp.values())
            factors.update(factor2exp.keys())
    if not factors == {*coprimes8out}:raise TypeError

def semi_factor_coprimess_via_gcd(coprimess, /):
    'coprimess/(Iter (Iter int{>0}){pairwise_coprime}) -> (coprimes/(tuple<int{>=2}>){pairwise_coprime}, idx2exp__lsls/[[idx2exp/[uint]]])'
    coprimess8in = [*map(list, coprimess)]
    1;  del coprimess
    coprimes8out = merge_coprimess_into_smaller_coprimes(coprimess8in)
    factor2idx = {ft:idx for idx, ft in enumerate(coprimes8out)}
    L = len(coprimes8out)

    idx2exp__lsls = []
    for js in coprimess8in:
        idx2exp__ls = []
        for j in js:
            if not j > 0: raise NotImplementedError
            (factor2exp, unfactored_part) = semi_factor_pint_via_trial_division(coprimes8out, j)
            if not unfactored_part == 1:raise logic-err
            idx2exp = [0]*L
            for ft, e in factor2exp.items():
                idx = factor2idx[ft]
                idx2exp[idx] = e
            idx2exp
            idx2exp = mk_tuple(idx2exp)
            idx2exp__ls.append(idx2exp)
        idx2exp__ls = mk_tuple(idx2exp__ls)
        idx2exp__lsls.append(idx2exp__ls)
    idx2exp__lsls = mk_tuple(idx2exp__lsls)
    return (coprimes8out, idx2exp__lsls)



__all__


from seed.math.merge_coprimess_into_smaller_coprimes import merge_coprimess_into_smaller_coprimes, semi_factor_coprimess_via_gcd
from seed.math.merge_coprimess_into_smaller_coprimes import *
