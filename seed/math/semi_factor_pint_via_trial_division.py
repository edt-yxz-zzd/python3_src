r'''[[[
e ../../python3_src/seed/math/semi_factor_pint_via_trial_division.py
seed.math.semi_factor_pint_via_trial_division
py -m seed.math.semi_factor_pint_via_trial_division

py -m seed.math.semi_factor_pint_via_trial_division _test1__iter_unsorted_products_of_coprime_factors__ge_le +show
py -m seed.math.semi_factor_pint_via_trial_division _test1__iter_unsorted_products_of_coprime_factors__ge_le



from seed.math.semi_factor_pint_via_trial_division import semi_factor_pint_via_trial_division, calc_num_products_of_coprime_factors__ge1_le, calc_num_products_of_coprime_factors__ge_le, iter_unsorted_products_of_coprime_factors__ge_le

#]]]'''
__all__ = '''
    semi_factor_pint_via_trial_division
    calc_num_products_of_coprime_factors__ge1_le
        calc_num_products_of_coprime_factors__ge_le
    iter_unsorted_products_of_coprime_factors__ge_le
    '''.split()
from seed.math.max_power_of_base_as_factor_of_ import max_power_of_base_as_factor_of_, count_num_low_0bits_of_pint, count_num_low_1bits_of_uint, factor_pint_out_2_powers, factor_nonzero_int_out_sign_and_2_powers
from seed.func_tools.recur5yield import recur5yield__list__echo__echo
from seed.math.are_pairwise_coprime import are_pairwise_coprime
from seed.func_tools.fmapT.checkT__tiny import (dot, checkT__pattern_list, checkT__AND, check_int, checkT__ge)
from seed.math.iter_sorted_products_of_uints import iter_sorted_products_of_uints, iter_sorted_products_of_strict_sorted_pairwise_coprime_uints, iter_sorted_products_of_strict_sorted_pairwise_coprime_uints__with_ifactor_exp_pairs
from itertools import takewhile
from seed.math.floor_ceil import floor_div, ceil_div
from seed.math.floor_ceil import floor_log_, ceil_log_
from seed.tiny import mk_tuple


def semi_factor_pint_via_trial_division(candidate_factors, pint, /):
    'Iter factor{>=2} -> pint -> (factor2exp/{factor:exp{>=1}}, unfactored_part{>=1})'
    assert pint >= 1
    ft2e = {}
    it = iter(candidate_factors)
    while pint > 1:
        for ft in it:
            break
        else:
            break
        assert ft >= 2
        if ft == 2:
            (exp, odd) = factor_pint_out_2_powers(pint)
            if exp > 0:
                ft2e[2] = exp
                pint = odd
        else:
            exp = max_power_of_base_as_factor_of_(ft, pint)
            if exp > 0:
                ft2e[ft] = exp
                pint //= ft**exp
    factor2exp = ft2e
    unfactored_part = pint
    return (factor2exp, unfactored_part)

check_iterable_of_int_ge2 = checkT__pattern_list(checkT__AND(check_int, checkT__ge(2)))
def _():
    @recur5yield__list__echo__echo
    def calc_num_products_of_coprime_factors__ge1_le(coprime_factors, upperbound, /, *, turnoff__verify_factors_are_pairwise_coprime=False, calc_directly_via_def=False, calc_directly_via_enumerate=False):
        'coprime_factors/[int{>=2}] -> upperbound/int -> count/uint # [count == len{u <- [1..=upperbound] | [(_,unfactored_part) := semi_factor_pint_via_trial_division(coprime_factors, u)][unfactored_part == 1]}] # O(count*log2(upperbound)**2) # [count <= II{floor_log(ft;upperbound) | [ft :<- coprime_factors]} <= floor_log2(upperbound)**len(coprime_factors)]'
        if calc_directly_via_enumerate and calc_directly_via_def: raise TypeError

        check_int(upperbound)
        #coprime_factors = [*coprime_factors]
        coprime_factors = mk_tuple(coprime_factors)
        check_iterable_of_int_ge2(coprime_factors)
        if not turnoff__verify_factors_are_pairwise_coprime:
            if not are_pairwise_coprime(coprime_factors): raise ValueError
        if calc_directly_via_enumerate:
            #it = iter_sorted_products_of_uints(coprime_factors)
            it = iter_sorted_products_of_strict_sorted_pairwise_coprime_uints(sorted(coprime_factors), finite_seq_vs_infinite_seq=False, turnoff__verify_factors_are_pairwise_coprime=True)
            if 0b00:
                #it = [*it] #infinite length
                #print(it)
                for u in it:
                    if type(u) is not int:
                        print(type(u))
                        print(repr(u))
                        #<class 'tuple'>
                        #(1, ())
                        #bug:iter_sorted_products_of_strict_sorted_pairwise_coprime_uints__with_ifactor_exp_pairs --> iter_sorted_products_of_strict_sorted_pairwise_coprime_uints
                        break
                raise ...

            it = map(upperbound.__ge__, it)
            it = takewhile(bool, it)
            # O(log2(len(coprime_factors)*count)*len(coprime_factors)*count*log2(upperbound)**2)
            #   其中『len(coprime_factors)*』源自同一个新ft2e由len(ft2e)个旧ft2e导出(e+=1 for each ft)，这些新ft2e同时存在于 堆(heap)中
            #   乘法:由ft2e到product，共计算L*count次
            #   其中『log2(...)』部分，是因为 极值锋面 接近O(count)
            return True, sum(it)

        if calc_directly_via_def:
            # O(upperbound*log2(upperbound)**2)
            return True, sum(unfactored_part == 1 for u in range(1, upperbound+1) for (_, unfactored_part) in [semi_factor_pint_via_trial_division(coprime_factors, u)])
        if upperbound <= 0:
            return True, 0
        begin4factors = 0
        # O(count*log2(upperbound)**2)
        return False, recur(coprime_factors, begin4factors, upperbound);yield


    def recur(coprime_factors, begin4factors, upperbound, /):
        #if upperbound == 0: return True, 0
            # [1..=0]
        assert upperbound >= 1

        if begin4factors == len(coprime_factors): return True, 1
            # [1..=upperbound>=1]
            # [II__p2e({}) == 1]
        ft = coprime_factors[begin4factors]
        begin4factors += 1
        acc = 0
        while upperbound:
            acc += yield recur(coprime_factors, begin4factors, upperbound)
            upperbound //= ft
        return True, acc
    return calc_num_products_of_coprime_factors__ge1_le
calc_num_products_of_coprime_factors__ge1_le = _()

def _test1__calc_num_products_of_coprime_factors__ge1_le():
    coprime_factors = [2,3,5,7]
    upperbound_ans_pairs = (
        [(10, 10)
        ,(100, 46)
        ,(1000, 141)
        ])
    kwargss = [{}
        ,dict(calc_directly_via_enumerate=True)
        ,dict(calc_directly_via_def=True)
        ]
    for kwargs in kwargss:
        for upperbound, ans in upperbound_ans_pairs:
            assert (calc_num_products_of_coprime_factors__ge1_le(coprime_factors, upperbound, **kwargs) == ans)
_test1__calc_num_products_of_coprime_factors__ge1_le()

#if __name__ == '__main__' and 0:
def _test2__calc_num_products_of_coprime_factors__ge1_le(*, show=False):
    if show:
        for i in range(11):
            print(calc_num_products_of_coprime_factors__ge1_le([2,3,5,7], 10**i))
    else:
        assert ([calc_num_products_of_coprime_factors__ge1_le([2,3,5,7], 10**i) for i in range(11)] == [1, 10, 46, 141, 338, 694, 1273, 2155, 3427, 5194, 7575])
        assert ([calc_num_products_of_coprime_factors__ge1_le([2,3,5,7], 10**i, calc_directly_via_enumerate=True) for i in range(11)] == [1, 10, 46, 141, 338, 694, 1273, 2155, 3427, 5194, 7575])


def calc_num_products_of_coprime_factors__ge_le(coprime_factors, lowerbound, upperbound, /, *, turnoff__verify_factors_are_pairwise_coprime=False):
    coprime_factors = mk_tuple(coprime_factors)
    return (
        +calc_num_products_of_coprime_factors__ge1_le(coprime_factors, upperbound, turnoff__verify_factors_are_pairwise_coprime=turnoff__verify_factors_are_pairwise_coprime)
        -calc_num_products_of_coprime_factors__ge1_le(coprime_factors, lowerbound-1, turnoff__verify_factors_are_pairwise_coprime=True)
        )

def _():
    r'''
    由于『可重启』(见下面:参数:prev_product4resume)，故不采用递归算法实现
    #'''
    def iter_unsorted_products_of_coprime_factors__ge_le(coprime_factors, lowerbound, upperbound, /, *, turnoff__verify_factors_are_pairwise_coprime=False, prev_product4resume=-1):
        'NOTE when using "prev_product4resume": output order depends on (lowerbound, upperbound) and the order of coprime_factors'
        check_int(upperbound)
        check_int(lowerbound)
        if not 1 <= lowerbound <= upperbound: raise ValueError
        check_int(prev_product4resume)
        coprime_factors = mk_tuple(coprime_factors)
        check_iterable_of_int_ge2(coprime_factors)
        if not turnoff__verify_factors_are_pairwise_coprime:
            if not are_pairwise_coprime(coprime_factors): raise ValueError
        if prev_product4resume >= 1:
            if not lowerbound <= prev_product4resume <= upperbound: raise ValueError('prev_product4resume is not in range[lowerbound..=upperbound]')
            (ft2e, _1) = semi_factor_pint_via_trial_division(coprime_factors, prev_product4resume)
            if not _1 == 1: raise ValueError('prev_product4resume is not product of coprime_factors')

        L = len(coprime_factors)
        #if L == 0 and 1 == lowerbound <= upperbound:
        if 1 == lowerbound <= upperbound:
            if not prev_product4resume >= 1:
                yield 1

        debound = (lowerbound, upperbound)
        if 0:
            debounds = [debound]*L
            ifactor_exp_pairs = []
                # [(ifactor, exp)]
            ifactor_exp_debound_triples = [(L, 0, debound)]
                # [(ifactor, exp, debound)]
                # [(ifactor, exp, (lowerbound, upperbound))]
        #####
        stack = ifactor_exp_debound_product_quadruple = [(L, 0, debound, 1)]
            # [(ifactor_ex, exp_ex, (lowerbound, upperbound), product)]
            # [0 <= ifactor_ex <= L]
            # [exp_ex >= 0]
            # except stack bottom:
            # [(ifactor, exp, (lowerbound, upperbound), product)]
            # [0 <= ifactor < L]
            # [exp >= 1]
            # [1 <= lowerbound <= upperbound]
        #####
        if prev_product4resume >= 1:
            restore_stack(coprime_factors, lowerbound, upperbound, stack, ft2e)

        while try_inc(coprime_factors, stack, 0):
            (ifactor, exp, (lowerbound, upperbound), product) = stack[-1]
            if lowerbound == 1:
                yield product

    def restore_stack(coprime_factors, lowerbound, upperbound, stack, ft2e, /):
        product = 1
        for ifactor in reversed(range(len(coprime_factors))):
            factor = coprime_factors[ifactor]
            if factor in ft2e:
                exp = ft2e[factor]
                fe = factor**exp
                lowerbound = ceil_div(lowerbound, fe)
                upperbound = floor_div(upperbound, fe)
                product *= fe
                stack.append((ifactor, exp, (lowerbound, upperbound), product))
        assert lowerbound == 1 # hence prev_product4resume be output
        return
    def try_inc(coprime_factors, stack, ifactor_ex, /):
        L = len(coprime_factors)
        #if ifactor_ex == L: return False
        while not ifactor_ex == L:
            ifactor = ifactor_ex
            (_ifactor_ex, _exp_ex, (lowerbound, upperbound), product) = stack[-1]
            assert ifactor <= _ifactor_ex
            if ifactor == _ifactor_ex:
                stack.pop()
            elif ifactor < _ifactor_ex:
                (_ifactor_ex, _exp_ex, (lowerbound, upperbound), product) = (ifactor, 0, (lowerbound, upperbound), product)
            else:
                raise logic-err
            assert _ifactor_ex == ifactor
            factor = coprime_factors[ifactor]
            if ifactor == 0 == _exp_ex:
                delta_exp = max(1, ceil_log_(factor, lowerbound))
            else:
                delta_exp = 1
            assert delta_exp >= 1 # 'inc' exp
            fe = factor**delta_exp
            lowerbound = ceil_div(lowerbound, fe)
            upperbound = floor_div(upperbound, fe)
            if not (lowerbound <= upperbound):
                ifactor_ex += 1
                continue
                #return False
            exp = _exp_ex + delta_exp
            product *= fe
            stack.append((ifactor, exp, (lowerbound, upperbound), product))
            return True
        assert ifactor_ex == L
        assert len(stack) == 1
        return False
    return iter_unsorted_products_of_coprime_factors__ge_le
iter_unsorted_products_of_coprime_factors__ge_le = _()


def _test1__iter_unsorted_products_of_coprime_factors__ge_le(*, show=False):
    inputs = (
    [([], 2,9)
    ,([], 1,9)
    ,([2], 1,9)
    ,([2], 9,39)
    ,([2,3], 9,39)
    ,([2,3,5], 9,39)
    ,([2,3,5,13], 9,39)
    ,([2,3,5,13], 1,39)
    ])
    outputs = (
    [[]
    ,[1]
    ,[1, 2, 4, 8]
    ,[16, 32]
    ,[16, 32, 12, 24, 9, 18, 36, 27]
    ,[16, 32, 12, 24, 9, 18, 36, 27, 10, 20, 15, 30, 25]
    ,[16, 32, 12, 24, 9, 18, 36, 27, 10, 20, 15, 30, 25, 13, 26, 39]
    ,[1, 2, 4, 8, 16, 32, 3, 6, 12, 24, 9, 18, 36, 27, 5, 10, 20, 15, 30, 25, 13, 26, 39]
    ,
    ])

    if show:
        for (coprime_factors, lowerbound, upperbound) in inputs:
            print([*iter_unsorted_products_of_coprime_factors__ge_le(coprime_factors, lowerbound, upperbound)])
    else:
        for (coprime_factors, lowerbound, upperbound), ans in zip(inputs, outputs):
            result = [*iter_unsorted_products_of_coprime_factors__ge_le(coprime_factors, lowerbound, upperbound)]
            assert (result == ans)
            assert len(result) == calc_num_products_of_coprime_factors__ge_le(coprime_factors, lowerbound, upperbound)
        for (coprime_factors, lowerbound, upperbound), ans in zip(inputs, outputs):
            for i, x in enumerate(ans):
                result = [*iter_unsorted_products_of_coprime_factors__ge_le(coprime_factors, lowerbound, upperbound, prev_product4resume=x)]
                #print(result)
                assert (result == ans[i+1:])
#def _test1__iter_unsorted_products_of_coprime_factors__ge_le(*, show=False):




def _NOP_():pass #nop:no-op:无操作:用于 adhoc_argparser__main
if __name__ == "__main__":
    from seed.recognize.cmdline.adhoc_argparser import adhoc_argparser__main, adhoc_argparse, AdhocArgParserError
    adhoc_argparser__main(globals(), None)
        #main()


