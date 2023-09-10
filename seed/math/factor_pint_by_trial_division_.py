#__all__:goto
r'''[[[
e ../../python3_src/seed/math/factor_pint_by_trial_division_.py


seed.math.factor_pint_by_trial_division_
py -m nn_ns.app.debug_cmd   seed.math.factor_pint_by_trial_division_ -x
py -m nn_ns.app.doctest_cmd seed.math.factor_pint_by_trial_division_:__doc__ -ff -v
py_adhoc_call   seed.math.factor_pint_by_trial_division_   @f
from seed.math.factor_pint_by_trial_division_ import *


from seed.math.prime_gens import min_prime_factor_gen, tabulate_may_min_prime_factor4uint_lt_, tabulate_may_factorization4uint_lt_

from seed.math.factor_pint_by_trial_division_ import factor_pint_by_trial_division_, factor_pint_by_trial_division_ex_

py_adhoc_call   seed.math.factor_pint_by_trial_division_   @test4factor_pint_by_trial_division__between_ =1 =30000


factor_pint_by_trial_division_, factor_pint_by_trial_division_ex_
>>> stable_list_islice_(200, map(factor_pint_by_trial_division_, range(1, 999)))
[{}
,{2: 1}
,{3: 1}
,{2: 2}
,{5: 1}
,{2: 1, 3: 1}
,{7: 1}
,{2: 3}
,{3: 2}
,{2: 1, 5: 1}
,{11: 1}
,{2: 2, 3: 1}
,{13: 1}
,{2: 1, 7: 1}
,{3: 1, 5: 1}
,{2: 4}
,{17: 1}
,{2: 1, 3: 2}
,{19: 1}
,{2: 2, 5: 1}
,{3: 1, 7: 1}
,{2: 1, 11: 1}
,{23: 1}
,{2: 3, 3: 1}
,{5: 2}
,{2: 1, 13: 1}
,{3: 3}
,{2: 2, 7: 1}
,{29: 1}
,{2: 1, 3: 1, 5: 1}
,{31: 1}
,{2: 5}
,{3: 1, 11: 1}
,{2: 1, 17: 1}
,{5: 1, 7: 1}
,{2: 2, 3: 2}
,{37: 1}
,{2: 1, 19: 1}
,{3: 1, 13: 1}
,{2: 3, 5: 1}
,{41: 1}
,{2: 1, 3: 1, 7: 1}
,{43: 1}
,{2: 2, 11: 1}
,{3: 2, 5: 1}
,{2: 1, 23: 1}
,{47: 1}
,{2: 4, 3: 1}
,{7: 2}
,{2: 1, 5: 2}
,{3: 1, 17: 1}
,{2: 2, 13: 1}
,{53: 1}
,{2: 1, 3: 3}
,{5: 1, 11: 1}
,{2: 3, 7: 1}
,{3: 1, 19: 1}
,{2: 1, 29: 1}
,{59: 1}
,{2: 2, 3: 1, 5: 1}
,{61: 1}
,{2: 1, 31: 1}
,{3: 2, 7: 1}
,{2: 6}
,{5: 1, 13: 1}
,{2: 1, 3: 1, 11: 1}
,{67: 1}
,{2: 2, 17: 1}
,{3: 1, 23: 1}
,{2: 1, 5: 1, 7: 1}
,{71: 1}
,{2: 3, 3: 2}
,{73: 1}
,{2: 1, 37: 1}
,{3: 1, 5: 2}
,{2: 2, 19: 1}
,{7: 1, 11: 1}
,{2: 1, 3: 1, 13: 1}
,{79: 1}
,{2: 4, 5: 1}
,{3: 4}
,{2: 1, 41: 1}
,{83: 1}
,{2: 2, 3: 1, 7: 1}
,{5: 1, 17: 1}
,{2: 1, 43: 1}
,{3: 1, 29: 1}
,{2: 3, 11: 1}
,{89: 1}
,{2: 1, 3: 2, 5: 1}
,{7: 1, 13: 1}
,{2: 2, 23: 1}
,{3: 1, 31: 1}
,{2: 1, 47: 1}
,{5: 1, 19: 1}
,{2: 5, 3: 1}
,{97: 1}
,{2: 1, 7: 2}
,{3: 2, 11: 1}
,{2: 2, 5: 2}
,{101: 1}
,{2: 1, 3: 1, 17: 1}
,{103: 1}
,{2: 3, 13: 1}
,{3: 1, 5: 1, 7: 1}
,{2: 1, 53: 1}
,{107: 1}
,{2: 2, 3: 3}
,{109: 1}
,{2: 1, 5: 1, 11: 1}
,{3: 1, 37: 1}
,{2: 4, 7: 1}
,{113: 1}
,{2: 1, 3: 1, 19: 1}
,{5: 1, 23: 1}
,{2: 2, 29: 1}
,{3: 2, 13: 1}
,{2: 1, 59: 1}
,{7: 1, 17: 1}
,{2: 3, 3: 1, 5: 1}
,{11: 2}
,{2: 1, 61: 1}
,{3: 1, 41: 1}
,{2: 2, 31: 1}
,{5: 3}
,{2: 1, 3: 2, 7: 1}
,{127: 1}
,{2: 7}
,{3: 1, 43: 1}
,{2: 1, 5: 1, 13: 1}
,{131: 1}
,{2: 2, 3: 1, 11: 1}
,{7: 1, 19: 1}
,{2: 1, 67: 1}
,{3: 3, 5: 1}
,{2: 3, 17: 1}
,{137: 1}
,{2: 1, 3: 1, 23: 1}
,{139: 1}
,{2: 2, 5: 1, 7: 1}
,{3: 1, 47: 1}
,{2: 1, 71: 1}
,{11: 1, 13: 1}
,{2: 4, 3: 2}
,{5: 1, 29: 1}
,{2: 1, 73: 1}
,{3: 1, 7: 2}
,{2: 2, 37: 1}
,{149: 1}
,{2: 1, 3: 1, 5: 2}
,{151: 1}
,{2: 3, 19: 1}
,{3: 2, 17: 1}
,{2: 1, 7: 1, 11: 1}
,{5: 1, 31: 1}
,{2: 2, 3: 1, 13: 1}
,{157: 1}
,{2: 1, 79: 1}
,{3: 1, 53: 1}
,{2: 5, 5: 1}
,{7: 1, 23: 1}
,{2: 1, 3: 4}
,{163: 1}
,{2: 2, 41: 1}
,{3: 1, 5: 1, 11: 1}
,{2: 1, 83: 1}
,{167: 1}
,{2: 3, 3: 1, 7: 1}
,{13: 2}
,{2: 1, 5: 1, 17: 1}
,{3: 2, 19: 1}
,{2: 2, 43: 1}
,{173: 1}
,{2: 1, 3: 1, 29: 1}
,{5: 2, 7: 1}
,{2: 4, 11: 1}
,{3: 1, 59: 1}
,{2: 1, 89: 1}
,{179: 1}
,{2: 2, 3: 2, 5: 1}
,{181: 1}
,{2: 1, 7: 1, 13: 1}
,{3: 1, 61: 1}
,{2: 3, 23: 1}
,{5: 1, 37: 1}
,{2: 1, 3: 1, 31: 1}
,{11: 1, 17: 1}
,{2: 2, 47: 1}
,{3: 3, 7: 1}
,{2: 1, 5: 1, 19: 1}
,{191: 1}
,{2: 6, 3: 1}
,{193: 1}
,{2: 1, 97: 1}
,{3: 1, 5: 1, 13: 1}
,{2: 2, 7: 2}
,{197: 1}
,{2: 1, 3: 2, 11: 1}
,{199: 1}
,{2: 3, 5: 2}
]
>>> p13 = 2**13 -1
>>> p61 = 2**61 -1
>>> p127 = 2**127 -1
>>> p521 = 2**521 -1
>>> p13_p127 = p13*p127
>>> p13_p61 = p13*p61
>>> from seed.helper.stable_repr import stable_repr, stable_repr_ex, stable_repr_print, stable_repr_print_ex
>>> stable_repr(factor_pint_by_trial_division_(p13_p61))
'{8191: 1, 2305843009213693951: 1}'
>>> stable_repr(factor_pint_by_trial_division_(p13_p127))
Traceback (most recent call last):
    ...
seed.math.factor_pint_by_trial_division_.OverflowError__too_big_to_apply_trial_division__probably_prime: ({8191: 1}, 170141183460469231731687303715884105727, 8209)
>>> stable_repr(factor_pint_by_trial_division_ex_(p13_p127))
'({8191: 1}, 170141183460469231731687303715884105727, 8209)'


kw:
def factor_pint_by_trial_division_(n, /, *, upperbound4probably_prime=default4upperbound4probably_prime, may_upperbound4prime_factor=None, next_prime_factor=2):
seed.math.factor_pint_by_trial_division_.ValidateFail__factor_pint: (210, {5: 1, 42: 1}, 1, None, None, 3317044064679887385961981)
>>> stable_repr(factor_pint_by_trial_division_(2, next_prime_factor=-1))
'{2: 1}'
>>> stable_repr(factor_pint_by_trial_division_(8, next_prime_factor=3)) # violate precondition && detected
Traceback (most recent call last):
    ...
ValueError: violate precondition: next_prime_factor=3

>>> stable_repr(factor_pint_by_trial_division_(16, next_prime_factor=3)) # violate precondition && not detected
Traceback (most recent call last):
    ...
seed.math.factor_pint_by_trial_division_.ValidateFail__factor_pint: (16, {16: 1}, 1, None, None, 3317044064679887385961981)
>>> stable_repr(factor_pint_by_trial_division_(2*3*5*7, next_prime_factor=5)) # violate precondition && not-detected
Traceback (most recent call last):
    ...
seed.math.factor_pint_by_trial_division_.ValidateFail__factor_pint: (210, {5: 1, 42: 1}, 1, None, None, 3317044064679887385961981)
>>> stable_repr(factor_pint_by_trial_division_(2*3*5*7*7, next_prime_factor=5)) # violate precondition && not-detected
Traceback (most recent call last):
    ...
seed.math.factor_pint_by_trial_division_.ValidateFail__factor_pint: (1470, {5: 1, 7: 2, 6: 1}, 1, None, None, 3317044064679887385961981)
>>> stable_repr(factor_pint_by_trial_division_(2*3*5*7*7))
'{2: 1, 3: 1, 5: 1, 7: 2}'
>>> stable_repr(factor_pint_by_trial_division_(2*3*5*7))
'{2: 1, 3: 1, 5: 1, 7: 1}'
>>> stable_repr(factor_pint_by_trial_division_(2*3*5*7, may_upperbound4prime_factor=8))
'{2: 1, 3: 1, 5: 1, 7: 1}'
>>> stable_repr(factor_pint_by_trial_division_(2*3*5*7, may_upperbound4prime_factor=7))
Traceback (most recent call last):
    ...
seed.math.factor_pint_by_trial_division_.OverflowError__too_big_to_apply_trial_division__exceed_prime_factor_limit: ({2: 1, 3: 1, 5: 1}, 7, 7)
>>> stable_repr(factor_pint_by_trial_division_(2*3*5*7, may_upperbound4prime_factor=5))
Traceback (most recent call last):
    ...
seed.math.factor_pint_by_trial_division_.OverflowError__too_big_to_apply_trial_division__exceed_prime_factor_limit: ({2: 1, 3: 1}, 35, 5)
>>> stable_repr(factor_pint_by_trial_division_(2*3*5*7, may_upperbound4prime_factor=3))
Traceback (most recent call last):
    ...
seed.math.factor_pint_by_trial_division_.OverflowError__too_big_to_apply_trial_division__exceed_prime_factor_limit: ({2: 1}, 105, 3)
>>> stable_repr(factor_pint_by_trial_division_(2*3*5*7, may_upperbound4prime_factor=2))
Traceback (most recent call last):
    ...
seed.math.factor_pint_by_trial_division_.OverflowError__too_big_to_apply_trial_division__exceed_prime_factor_limit: ({}, 210, 2)
>>> stable_repr(factor_pint_by_trial_division_(2*3*5*7, may_upperbound4prime_factor=1))
Traceback (most recent call last):
    ...
seed.math.factor_pint_by_trial_division_.OverflowError__too_big_to_apply_trial_division__exceed_prime_factor_limit: ({}, 210, 2)
>>> stable_repr(factor_pint_by_trial_division_(2, may_upperbound4prime_factor=1))
Traceback (most recent call last):
    ...
seed.math.factor_pint_by_trial_division_.OverflowError__too_big_to_apply_trial_division__exceed_prime_factor_limit: ({}, 2, 2)
>>> stable_repr(factor_pint_by_trial_division_(1, may_upperbound4prime_factor=1))
'{}'
>>> stable_repr(factor_pint_by_trial_division_(1, may_upperbound4prime_factor=0))
'{}'

>>> prime_basis4A014233[-1]
41
>>> next(prime_gen.iter__ge_(1+prime_basis4A014233[-1]))
43
>>> stable_repr(factor_pint_by_trial_division_(p127, upperbound4probably_prime=100))
Traceback (most recent call last):
    ...
seed.math.factor_pint_by_trial_division_.OverflowError__too_big_to_apply_trial_division__probably_prime: ({}, 170141183460469231731687303715884105727, 43)
>>> stable_repr(factor_pint_by_trial_division_(p127, may_upperbound4prime_factor=3))
Traceback (most recent call last):
    ...
seed.math.factor_pint_by_trial_division_.OverflowError__too_big_to_apply_trial_division__exceed_prime_factor_limit: ({}, 170141183460469231731687303715884105727, 3)
>>> stable_repr(factor_pint_by_trial_division_(p127, may_upperbound4prime_factor=3, upperbound4probably_prime=7))
Traceback (most recent call last):
    ...
seed.math.factor_pint_by_trial_division_.OverflowError__too_big_to_apply_trial_division__exceed_prime_factor_limit: ({}, 170141183460469231731687303715884105727, 3)
>>> stable_repr(factor_pint_by_trial_division_(p127, may_upperbound4prime_factor=41, upperbound4probably_prime=7))
Traceback (most recent call last):
    ...
seed.math.factor_pint_by_trial_division_.OverflowError__too_big_to_apply_trial_division__exceed_prime_factor_limit: ({}, 170141183460469231731687303715884105727, 41)
>>> stable_repr(factor_pint_by_trial_division_(p127, may_upperbound4prime_factor=42, upperbound4probably_prime=7))
Traceback (most recent call last):
    ...
seed.math.factor_pint_by_trial_division_.OverflowError__too_big_to_apply_trial_division__exceed_prime_factor_limit: ({}, 170141183460469231731687303715884105727, 43)
>>> stable_repr(factor_pint_by_trial_division_(p127, may_upperbound4prime_factor=43, upperbound4probably_prime=7))
Traceback (most recent call last):
    ...
seed.math.factor_pint_by_trial_division_.OverflowError__too_big_to_apply_trial_division__exceed_prime_factor_limit: ({}, 170141183460469231731687303715884105727, 43)
>>> stable_repr(factor_pint_by_trial_division_(p127, may_upperbound4prime_factor=44, upperbound4probably_prime=7))
Traceback (most recent call last):
    ...
seed.math.factor_pint_by_trial_division_.OverflowError__too_big_to_apply_trial_division__probably_prime: ({}, 170141183460469231731687303715884105727, 43)
>>> stable_repr(factor_pint_by_trial_division_ex_(p127, may_upperbound4prime_factor=44, upperbound4probably_prime=7))
'({}, 170141183460469231731687303715884105727, 43)'
>>> stable_repr(factor_pint_by_trial_division_ex_(p127, may_upperbound4prime_factor=42, upperbound4probably_prime=7))
'({}, 170141183460469231731687303715884105727, 43)'

ValidateFail__factor_pint(n, p2e, unfactored_part, may_next_prime_factor, may_upperbound4prime_factor, upperbound4probably_prime)

check_result5factor_pint_






#]]]'''
__all__ = r'''
factor_pint_by_trial_division_

Error
    OverflowError__too_big_to_apply_trial_division__probably_prime
    OverflowError__too_big_to_apply_trial_division__exceed_prime_factor_limit
    ValidateFail__factor_pint

factor_pint_by_trial_division_
    factor_pint_by_trial_division_ex_
    default4upperbound4probably_prime
    check_result5factor_pint_

    test4factor_pint_by_trial_division__between_
    test4factor_pint_by_trial_division__Ns_



'''.split()#'''
#min_prime_factor_gen
    #tabulate_may_min_prime_factor4uint_lt_
    #tabulate_may_factorization4uint_lt_
__all__
from seed.tiny import check_type_is
from seed.iters.apply_may_args4islice_ import list_islice_, show_islice_, stable_show_islice_, stable_list_islice_

from seed.math.II import II
from seed.math.max_power_of_base_as_factor_of_ import factor_pint_out_power_of_base_


from seed.math.prime_gens import min_prime_factor_gen, tabulate_may_min_prime_factor4uint_lt_, tabulate_may_factorization4uint_lt_

from seed.math.prime_gens import A014233, prime_basis4A014233, prime_gen
from seed.math.prime_gens import is_prime__tribool_, Case4is_prime__tribool_
from seed.math.prime_gens import Error


class OverflowError__too_big_to_apply_trial_division__probably_prime(Error):pass
class OverflowError__too_big_to_apply_trial_division__exceed_prime_factor_limit(Error):pass

class ValidateFail__factor_pint(Error):pass
def check_result5factor_pint_(n, p2e, unfactored_part, may_next_prime_factor, may_upperbound4prime_factor, upperbound4probably_prime, /):
    if not n == unfactored_part * II(p**e for p,e in p2e.items()): raise ValidateFail__factor_pint(n, p2e, unfactored_part, may_next_prime_factor, may_upperbound4prime_factor, upperbound4probably_prime)

    if not all(_is_prime__tribool4factor_pint_(False, p) is not False for p in p2e): raise ValidateFail__factor_pint(n, p2e, unfactored_part, may_next_prime_factor, may_upperbound4prime_factor, upperbound4probably_prime)

    if not all(e > 0 for e in p2e.values()): raise ValidateFail__factor_pint(n, p2e, unfactored_part, may_next_prime_factor, may_upperbound4prime_factor, upperbound4probably_prime)

    if not (may_next_prime_factor is None) is (unfactored_part == 1): raise ValidateFail__factor_pint(n, p2e, unfactored_part, may_next_prime_factor, may_upperbound4prime_factor, upperbound4probably_prime)

    if not may_next_prime_factor is None:
        next_prime_factor = may_next_prime_factor

    if not may_upperbound4prime_factor is None:
        upperbound4prime_factor = may_upperbound4prime_factor

    if not (unfactored_part == 1 or (may_upperbound4prime_factor is not None and next_prime_factor >= upperbound4prime_factor) or _is_prime__tribool4factor_pint_(False, unfactored_part) is ...): raise ValidateFail__factor_pint(n, p2e, unfactored_part, may_next_prime_factor, may_upperbound4prime_factor, upperbound4probably_prime)

default4upperbound4probably_prime = 2**40
    #meaningless, since pseudoprime > 2**81
default4upperbound4probably_prime = A014233[-1] # < is_prime__using_A014233_.upperbound
def factor_pint_by_trial_division_ex_(n, /, *, upperbound4probably_prime=default4upperbound4probably_prime, may_upperbound4prime_factor=None, next_prime_factor=2):
    r'''[[[
-> (p2e/{prime:exp}, unfactored_part/pint, may next_prime_factor/prime)
postcondition:
    [[unfactored_part==1] <-> [may_next_prime_factor is None]]
    [[unfactored_part==1] or [next_prime_factor >=upperbound4prime_factor] or [unfactored_part is pseudoprime >=upperbound4probably_prime]]

precondition: [[n > 0][@[k :<- [2..<next_prime_factor]] -> [n%k =!= 0]]]

    #]]]'''#'''
    try:
        p2e = _factor_pint_by_trial_division_(upperbound4probably_prime, may_upperbound4prime_factor, next_prime_factor, n)
    except OverflowError__too_big_to_apply_trial_division__probably_prime as exc:
        [(p2e, pseudoprime, next_prime_factor)] = exc.args
        unfactored_part = pseudoprime
        assert unfactored_part > A014233[-1]
        may_next_prime_factor = next_prime_factor
    except OverflowError__too_big_to_apply_trial_division__exceed_prime_factor_limit as exc:
        [(p2e, unfactored_part, next_prime_factor)] = exc.args
        may_next_prime_factor = next_prime_factor
    else:
        unfactored_part = 1
        may_next_prime_factor = None

    check_result5factor_pint_(n, p2e, unfactored_part, may_next_prime_factor, may_upperbound4prime_factor, upperbound4probably_prime)
    return (p2e, unfactored_part, may_next_prime_factor)
def factor_pint_by_trial_division_(n, /, *, upperbound4probably_prime=default4upperbound4probably_prime, may_upperbound4prime_factor=None, next_prime_factor=2):
    r'''[[[
-> p2e/{prime:exp}
| ^OverflowError__too_big_to_apply_trial_division__probably_prime((p2e, unfactored_part/pseudoprime, next_prime_factor))
    when [pseudoprime >= upperbound4probably_prime]
| ^OverflowError__too_big_to_apply_trial_division__exceed_prime_factor_limit((p2e, unfactored_part, next_prime_factor))
    when [next_prime_factor >= upperbound4prime_factor]

precondition: [[n > 0][@[k :<- [2..<next_prime_factor]] -> [n%k =!= 0]]]

    #]]]'''#'''
    p2e = _factor_pint_by_trial_division_(upperbound4probably_prime, may_upperbound4prime_factor, next_prime_factor, n)
    unfactored_part = 1
    may_next_prime_factor = None
    check_result5factor_pint_(n, p2e, unfactored_part, may_next_prime_factor, may_upperbound4prime_factor, upperbound4probably_prime)
    return p2e
_sqare4next_prime4prime_basis4A014233 = prime_gen[len(prime_basis4A014233)]**2
assert _sqare4next_prime4prime_basis4A014233 == 43**2

def _is_prime__tribool4factor_pint_(skip_check, n, /):
    return is_prime__tribool_(n, case=Case4is_prime__tribool_.II_prime_basis_gtN, skip_check=skip_check)

def _factor_pint_by_trial_division_(upperbound4probably_prime, may_upperbound4prime_factor, next_prime_factor, n, /):
    #trial_division
    ######################
    #precondition: [[n > 0][@[k :<- [2..<next_prime_factor]] -> [n%k =!= 0]]]
        #   setup_loop_invariant4next_round:2
    ######################
    check_type_is(int, upperbound4probably_prime)
    if not may_upperbound4prime_factor is None:
        upperbound4prime_factor = may_upperbound4prime_factor
        check_type_is(int, upperbound4prime_factor)
    check_type_is(int, next_prime_factor)

    check_type_is(int, n)
    if not n > 0:raise ValueError(n)
    #n0 = n
    # [n >= 1]

    skip_check = False
    if not next_prime_factor <= 2:
        #bug:if not (n == next_prime_factor or n >= next_prime_factor**2): raise ValueError(f'violate precondition: next_prime_factor={next_prime_factor}')
        if not (n >= next_prime_factor): raise ValueError(f'violate precondition: next_prime_factor={next_prime_factor}')
        if not (n >= next_prime_factor**2):
            if _is_prime__tribool4factor_pint_(skip_check, n) is False: raise ValueError(f'violate precondition: next_prime_factor={next_prime_factor}')
            skip_check = True

    ps = prime_gen.iter__ge_(next_prime_factor)
    p2e = {}
    if n == 1:
        return p2e
    # [n >= 2]

    # !! [@[k :<- [2..<next_prime_factor]] -> [n%k =!= 0]]]
    # [[next_prime_factor > 2] -> [n >= next_prime_factor]]
    # !! [n >= 2]
    # [[next_prime_factor <= 2] -> [n >= 2 >= next_prime_factor]]
    # ==>>:
    # [n >= next_prime_factor]
        #   setup_loop_invariant4next_round:1

    n_changed = True
    n_init = True
    # [n >= 2]
    # [@[k :<- [2..<next_prime_factor]] -> [n%k =!= 0]]]
    #==>>:
    # [n >= next_prime_factor]
    while 1:
        ######################
        # loop-invariants:
        # [n >= 2]
        # [@[k :<- [2..<next_prime_factor]] -> [n%k =!= 0]]]
        #==>>:
        # [n >= next_prime_factor]
        ######################
        #
        p = next(ps)
            # [p := next_prime_factor] then [next_prime_factor := ???]

        # [n >= p >= 2]
        # [@[k :<- [2..<p]] -> [n%k =!= 0]]]





        ######################
        # detect limit about prime_factor:
        ######################
        if may_upperbound4prime_factor is not None and not p < upperbound4prime_factor:
            unfactored_part = n
            next_prime_factor = p
                #not used in trial_division yet
            raise OverflowError__too_big_to_apply_trial_division__exceed_prime_factor_limit((p2e, unfactored_part, next_prime_factor))





        ######################
        # detect prime since trial_division:
        ######################
        # !! [@[k :<- [2..<p]] -> [n%k =!= 0]]]
        # [[n is composite] -> [n >= p**2]]
        # [[n < p**2] -> [n is not composite]]
        # [[n < p**2] -> [n=!=1] -> [n is prime]]
        # !! [n >= p >= 2]
        # [[n < p**2] -> [n is prime]]
        if n < p**2:
            # [n is prime]
            n, p = 1, n
            p2e[p] = 1
            break




        ######################
        # detect limit about pseudoprime:
        ######################
        # [n >= p**2 > p >= 2]
        if (n_changed or n_init) and p > prime_basis4A014233[-1]:
            # n changed
            #
            # new-n < old-n
            # now n maybe prime
            #
            # [n > p > prime_basis4A014233[-1] >= 2]
            # [n > 3]
            # [p > 2]
            # !! [@[k :<- [2..<p]] -> [n%k =!= 0]]]
            # [n%2 =!= 0]
            #
            #satisfy precondition:
                # [n is odd][n >= 3]
                # [@[b :<- prime_basis4A014233] -> [b%n =!= 0]]
                #
            next_prime_factor = p
                #not used in trial_division yet
            if _4factor_(upperbound4probably_prime, next_prime_factor, p2e, n, skip_check=skip_check):
                n = 1
                #return p2e
                break
            skip_check = True
            n_init = False


        ######################
        # do trial_division
        ######################
        # [n >= p**2 > p >= 2]
        #   see below: [not n_changed]
        (e, n) = factor_pint_out_power_of_base_(p, n)
        # [new_n%p =!= 0]
        # [n%new_n == 0]
        #
        # !! [n%new_n == 0]
        # !! [@[k :<- [2..<p]] -> [n%k =!= 0]]]
        # [@[k :<- [2..<p]] -> [new_n%k =!= 0]]]
        # !! [new_n%p =!= 0]
        # [@[k :<- [2..<=p]] -> [new_n%k =!= 0]]]
        #==>>:
        # [n := new_n]
        # [@[k :<- [2..<=p]] -> [n%k =!= 0]]]
        # [@[k :<- [2..<next_prime_factor]] -> [n%k =!= 0]]]
        #   setup_loop_invariant4next_round:2
        #
        n_changed = e > 0
        # [[not n_changed] -> [n >= p**2 > p >= 2]]
        #==>>:
        # [[n < p] -> [n_changed]]
        #

        # !! [@[k :<- [2..<=p]] -> [n%k =!= 0]]]
        # [[n==1]or[n > p]]

        if n_changed:
            p2e[p] = e
            if n == 1:break
            # [n =!= 1]
            # !! [[n==1]or[n > p]]
            # [n > p]
        else:
            # [not n_changed]
            # !! [[not n_changed] -> [n >= p**2 > p >= 2]]
            # [n > p]
            pass
        # [n > p]
        # [n > p >= 2]
        # [n >= 2]
        #   setup_loop_invariant4next_round:1

        ##next round:
        # [n >= 2]
        # [@[k :<- [2..<next_prime_factor]] -> [n%k =!= 0]]]
        #==>>:
        # [n >= next_prime_factor]
        #
    assert n == 1
    return p2e
def _4factor_(upperbound4probably_prime, next_prime_factor, p2e, n, /, *, skip_check):
    r = _is_prime__tribool4factor_pint_(skip_check, n)
    if r is ...:
        #probably_prime
        pseudoprime = n
        if not pseudoprime < upperbound4probably_prime:
            raise OverflowError__too_big_to_apply_trial_division__probably_prime((p2e, pseudoprime, next_prime_factor))
        pass
    else:
        if r:
            #prime
            n, p = 1, n
            p2e[p] = 1
            return True
        #composite
        pass
    return False

def test4factor_pint_by_trial_division__between_(begin, end, /):
    test4factor_pint_by_trial_division__Ns_(range(begin, end))
def test4factor_pint_by_trial_division__Ns_(Ns, /):
    for n in Ns:
        factor_pint_by_trial_division_(n)



if __name__ == "__main__":
    pass
__all__


from seed.math.factor_pint_by_trial_division_ import factor_pint_by_trial_division_, factor_pint_by_trial_division_ex_
from seed.math.factor_pint_by_trial_division_ import *


