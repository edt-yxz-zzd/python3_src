r'''
e ../../python3_src/nn_ns/math_nn/mk_coprimes.py
from nn_ns.math_nn.mk_coprimes import deep_gcd_into_3_coprimess, split_hints_into_coprimess__by_gcd, split_pint_into_coprimess__by_gcd_hints

#'''


__all__ = '''
    deep_gcd_into_3_coprimess
    split_hints_into_coprimess__by_gcd
    split_pint_into_coprimess__by_gcd_hints
    '''.split()



from seed.math.gcd import gcd
from seed.func_tools.recur5yield import recur5yield__list__echo__echo #, recur5yield__list__echo__off, recur5yield__list__0func__echo, recur5yield__list__0func__off
from seed.tiny import null_tuple, mk_tuple
from seed.math.max_power_of_base_as_factor_of_ import max_power_of_base_as_factor_of_



def _():
  @recur5yield__list__echo__echo
  def deep_gcd_into_3_coprimess(lhs_coprimes, rhs_coprimes, /):
    r'lhs_coprimes/(Iter pint) -> rhs_coprimes/(Iter pint) -> (coprimesL{lhs%.==0;gcd(rhs,.)==1}, coprimesG{lhs%.==0;rhs%.==0;}, coprimesR{rhs%.==0;gcd(lhs,.)==1}){are_pairwise_coprime(coprimesL\-/coprimesR)}'
    lhs_coprimes = mk_tuple(lhs_coprimes)
    rhs_coprimes = mk_tuple(rhs_coprimes)
    if not all(lhs >= 1 for lhs in lhs_coprimes): raise TypeError
    if not all(rhs >= 1 for rhs in rhs_coprimes): raise TypeError
    return False, _deep_gcd__s_s(lhs_coprimes, rhs_coprimes)
    yield #bug:miss this line

  def _3_gcd__1_1(lhs, rhs, /):
    r'lhs/pint -> rhs/pint -> (lhs/gcd, gcd, rhs/gcd)'
    g = gcd(lhs, rhs)
    lhs_g = lhs//g
    rhs_g = rhs//g
    return (lhs_g, g, rhs_g)
  def _3_gcd_ex__1_1(lhs, rhs, /):
    g = gcd(lhs, rhs)
    lhs_g = _reduce_xhs(g, lhs)
    rhs_g = _reduce_xhs(g, rhs)
    return (lhs_g, g, rhs_g)
  def _reduce_xhs(g, xhs, /):
    if not g == 1:
        eR = max_power_of_base_as_factor_of_(g, xhs)
            #required: [base>=2]
            #==>> [g=!=1]
        xhs_g = xhs // g**eR
    else:
        xhs_g = xhs
    return xhs_g
  def _deep_gcd__s_s(lhs_coprimes, rhs_coprimes, /):
    r'lhs_coprimes/[pint] -> rhs_coprimes/[pint] -> (coprimesL{lhs%.==0;gcd(rhs,.)==1}, coprimesG{lhs%.==0;rhs%.==0;}, coprimesR{rhs%.==0;gcd(lhs,.)==1}){are_pairwise_coprime(coprimesL\-/coprimesR)}'
    def pushsL(lhss, /):
        either_stack.extend((False, lhs) for lhs in lhss)
    def pushsR(rhss, /):
        either_stack.extend((True, rhs) for rhs in rhss)
    lhs_stack = []
    either_stack = []
        # either = (is_right, (lhs|rhs))
        # 不变量:if lhs before@list/below@stack rhs, then gcd(lhs, rhs)==1
        #
    pushsR(rhs_coprimes)
    pushsL(lhs_coprimes)

    sR_ls = []
    sG_ls = []
    while either_stack:
        (is_right, xhs) = either = either_stack.pop()
        if not is_right:
            lhs = xhs
            lhs_stack.append(lhs)
            continue
        rhs = xhs

        if not lhs_stack:
            sR_ls.append(rhs)
            continue
        lhs = lhs_stack.pop()

        (sL1, sG1, sR1) = yield _deep_gcd__1_1(lhs, rhs)
        sG_ls.extend(sG1)
        pushsL(sL1)
        pushsR(sR1)
        continue

    sL = mk_tuple(lhs_stack)
    sG = mk_tuple(sG_ls)
    sR = mk_tuple(sR_ls)
    return True, (sL, sG, sR)

  def _deep_gcd__1_1(lhs, rhs, /):
    r'lhs/pint -> rhs/pint -> (coprimesL{lhs%.==0;gcd(rhs,.)==1}, coprimesG{lhs%.==0;rhs%.==0;}, coprimesR{rhs%.==0;gcd(lhs,.)==1}){are_pairwise_coprime(coprimesL\-/coprimesR)}'
    if lhs == 1 or rhs == 1:
        coprimesL = null_tuple if lhs == 1 else (lhs,)
        coprimesG = null_tuple
        coprimesR = null_tuple if rhs == 1 else (rhs,)
        return True, (coprimesL, coprimesG, coprimesR)

    (lhs_g, g, rhs_g) = _3_gcd_ex__1_1(lhs, rhs)
    # [coprime lhs_g rhs_g]
    sG, sGL, sL = yield _deep_gcd__1_1(g, lhs_g)
    sG, sGR, sR = yield _deep_gcd__s_s(sG, (rhs_g,))
    sG = (*sGL, *sG, *sGR)
    return True, (sL, sG, sR)
  if 1:
    return deep_gcd_into_3_coprimess
deep_gcd_into_3_coprimess = _()


def split_hints_into_coprimess__by_gcd(hints, /):
    r'Iter pint -> coprimes/[pint]'
    coprimes = ()
    for rhs in hints:
        (sL, sG, sR) = deep_gcd_into_3_coprimess(coprimes, (rhs,))
        coprimes = (*sL, *sG, *sR)
    return coprimes
def split_pint_into_coprimess__by_gcd_hints(n, hints, /):
    coprimes = split_hints_into_coprimess__by_gcd(hints)
    (sL, sG, sR) = deep_gcd_into_3_coprimess(coprimes, (n,))
    #coprimes = (*sL, *sG, *sR)
    coprimes = (*sG, *sR)
    return coprimes


