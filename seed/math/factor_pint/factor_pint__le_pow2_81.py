#__all__:goto
#rho_vs_ECM:goto
r'''[[[
e ../../python3_src/seed/math/factor_pint/factor_pint__le_pow2_81.py

seed.math.factor_pint.factor_pint__le_pow2_81
py -m nn_ns.app.debug_cmd   seed.math.factor_pint.factor_pint__le_pow2_81 -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.factor_pint.factor_pint__le_pow2_81:__doc__ -ht # -ff -df
#######

[[
DONE::
@20260905
view ../../python3_src/seed/algo/rho_method__7iter7batch.py
    gcd only once per batch when fail
]]


'#'; __doc__ = r'#'
>>> from seed.helper.stable_repr import stable_repr, stable_repr_print
>>> stable_print = lambda x, /:stable_repr_print(None, x)

factor_pint__le_pow2_81_
    factor_pint__le_pow2_81__7rho_
>>> factor_pint__le_pow2_81_(-1)
Traceback (most recent call last):
    ...
TypeError: -1
>>> factor_pint__le_pow2_81_(0)
Traceback (most recent call last):
    ...
TypeError: 0
>>> factor_pint__le_pow2_81_(1)
{}
>>> factor_pint__le_pow2_81_(2)
{2: 1}
>>> factor_pint__le_pow2_81_(1+2**81)
Traceback (most recent call last):
    ...
TypeError: 2417851639229258349412353
>>> factor_pint__le_pow2_81_(2**81)
{2: 81}
>>> stable_print(factor_pint__le_pow2_81_(-1+2**81))
{7: 1, 73: 1, 2593: 1, 71119: 1, 262657: 1, 97685839: 1}
>>> stable_print(factor_pint__le_pow2_81_(-1+2**81, with_idc=True))
({7: 1, 73: 1, 2593: 1, 71119: 1, 262657: 1, 97685839: 1}, (479, 545))
>>> stable_print(factor_pint__le_pow2_81_(-1+2**81, with_idc=True, max4prime7trial_division=2))
({7: 1, 73: 1, 2593: 1, 71119: 1, 262657: 1, 97685839: 1}, (4, 13, 59, 479, 545))
>>> stable_print(factor_pint__le_pow2_81_(-1+2**81, with_idc=True, max4prime7trial_division=2, partial_ok=True, max4num_steps=545))
(({7: 1, 73: 1, 2593: 1, 71119: 1, 262657: 1, 97685839: 1}, {}, {}), (4, 13, 59, 479, 545))
>>> stable_print(factor_pint__le_pow2_81_(-1+2**81, with_idc=True, max4prime7trial_division=2, partial_ok=True, max4num_steps=544))
(({7: 1, 73: 1, 2593: 1, 262657: 1}, {6947319183841: 1}, {}), (4, 13, 59, 479))
>>> stable_print(factor_pint__le_pow2_81_(-1+2**81, with_idc=True, max4prime7trial_division=2, partial_ok=True, max4num_steps=479))
(({7: 1, 73: 1, 2593: 1, 262657: 1}, {6947319183841: 1}, {}), (4, 13, 59, 479))
>>> stable_print(factor_pint__le_pow2_81_(-1+2**81, with_idc=True, max4prime7trial_division=2, partial_ok=True, max4num_steps=478))
(({7: 1, 73: 1, 2593: 1}, {1824762014870125537: 1}, {}), (4, 13, 59))
>>> stable_print(factor_pint__le_pow2_81_(-1+2**81, with_idc=True, max4prime7trial_division=2, partial_ok=True, max4num_steps=59))
(({7: 1, 73: 1, 2593: 1}, {1824762014870125537: 1}, {}), (4, 13, 59))
>>> stable_print(factor_pint__le_pow2_81_(-1+2**81, with_idc=True, max4prime7trial_division=2, partial_ok=True, max4num_steps=58))
(({7: 1, 73: 1}, {4731607904558235517441: 1}, {}), (4, 13))
>>> stable_print(factor_pint__le_pow2_81_(-1+2**81, with_idc=True, max4prime7trial_division=2, partial_ok=True, max4num_steps=13))
(({7: 1, 73: 1}, {4731607904558235517441: 1}, {}), (4, 13))
>>> stable_print(factor_pint__le_pow2_81_(-1+2**81, with_idc=True, max4prime7trial_division=2, partial_ok=True, max4num_steps=12))
(({7: 1}, {345407377032751192773193: 1}, {}), (4,))
>>> stable_print(factor_pint__le_pow2_81_(-1+2**81, with_idc=True, max4prime7trial_division=2, partial_ok=True, max4num_steps=4))
(({7: 1}, {345407377032751192773193: 1}, {}), (4,))
>>> stable_print(factor_pint__le_pow2_81_(-1+2**81, with_idc=True, max4prime7trial_division=2, partial_ok=True, max4num_steps=3))
(({}, {2417851639229258349412351: 1}, {}), ())

>>> #stable_print(factor_pint__le_pow2_81_(549755813911*1099511627791, known_factor4Pmm=2*47846459))
>>> stable_print(factor_pint__le_pow2_81_(549755813911*1099511627791, even_exp=2*47846459))
{549755813911: 1, 1099511627791: 1}
>>> stable_print(factor_pint__le_pow2_81_(549755813911*1099511627791, even_exp=2*47846459, with_idc=True))
({549755813911: 1, 1099511627791: 1}, (21,))
>>> factor_pint__le_pow2_81_(1, with_idc=True)
({}, ())
>>> factor_pint__le_pow2_81_(2, with_idc=True)
({2: 1}, ())



factor_pint__le_pow2_81_
    ++kw:using_ECM
    factor_pint__le_pow2_81__7ECM_
        ++kw:with_settingss,_n2settings4EPC
>>> stable_print(factor_pint__le_pow2_81_(n:=549755813911*1099511627791, using_ECM=True, inversionless=False)) #doctest: +SKIP
{549755813911: 1, 1099511627791: 1}

>>> stable_print(factor_pint__le_pow2_81_(n:=549755813911*1099511627791, using_ECM=True, inversionless=False, _n2settings4EPC={n:((604462909840849692000601, 113612373689681093668799, -35105676510727254637001), (-13323696834883514051457, 107231846234603392551700))}))
{549755813911: 1, 1099511627791: 1}


>>> stable_print(factor_pint__le_pow2_81_(n:=549755813911*1099511627791, using_ECM=True, inversionless=True, _n2settings4EPC={n:((604462909840849692000601, -202034900548755701729777, 1), (-139840703184852864221651, 1))}))
{549755813911: 1, 1099511627791: 1}
















#rho_vs_ECM:goto
[[
py_adhoc_call   seed.math.factor_pint.factor_pint__le_pow2_81   @factor_pint__le_pow2_81_ =456777897
    {3: 1, 401: 1, 379699: 1}

py_adhoc_call   seed.math.factor_pint.factor_pint__le_pow2_81   @factor_pint__le_pow2_81_ =-1+549755813911
    {2: 1, 3: 1, 5: 1, 383: 1, 47846459: 1}
]]


]]]'''#'''
__all__ = r'''
factor_pint__le_pow2_81_
    factor_pint__le_pow2_81__7rho_
    factor_pint__le_pow2_81__7ECM_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.abc.abc__ver1 import abstractmethod, override, ABC
from seed.math.factor_pint.sprp_factor_pint_framework import IFramework4sprp_factor_pint
#   def sprp_factor_pint_(sf, n, max4prime7trial_division, /, *args7init, **kwds7init):
#.#################################
from seed.helper.lazy_import__func import force_lazy_imported_func_
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.types.Rope import Rope, mk_Rope
    from itertools import repeat
    from math import isqrt
    #from random import Random
        # .seed(self, a=None, version=2)
        # .getstate(self) # [625 == len(st4Random[1])] #too huge
        # .setstate(self, state)
        # .randrange(self, start, stop=None, step=1)

    from seed.types.SinglyLinkedList import mk_rglnkls_, oo_push_, list7up_, top6_
    from seed.tiny_.check import check_type_is, check_int_ge, check_int_ge_le
    from seed.math.II import II__ft2e_
    from seed.math.hrem_ import mk_hrem_
    from seed.math.is_prime__le_pow2_81 import is_prime__le_pow2_81
    from seed.math.factor_pint_by_trial_division_ import factor_pint_by_trial_division_ex_
    #def factor_pint_by_trial_division_ex_(n, /, *, upperbound4probably_prime=default4upperbound4probably_prime, may_upperbound4prime_factor=None, next_prime_factor=2):
    #   -> (p2e/{prime:exp}, unfactored_part/pint, may next_prime_factor/prime)

    from seed.algo.rho_method import try_factor1_pint__via_rho_method_# sprp_factor_pint__via_rho_method_
    #def try_factor1_pint__via_rho_method_(n, f_=None, /, *, to_detect_SPRP=False, seeds=None, max_num_seeds=None, max_num_tries_per_seed=None, to_output_statistics=False, _verbose=False):
    #   'n/int{>=1}/[not is_prime(n)] -> may (n -> (*params) -> uint%n -> uint%n) -> (kw:seeds/may (Iter params_x0/(*params, x0))) -> imay proper_factor if not to_output_statistics else (imay_proper_factor, jseed, total_steps) # [SPRP == strong probable-prime]'
    #def sprp_factor_pint__via_rho_method_(n, f_=None, /, *, seeds=None, max_num_seeds=None, max_num_tries_per_seed=None, to_output_statistics=False):
    #   'n/int{>=1} -> may (n -> (*params) -> uint%n -> uint%n) -> (kw:seeds/may (Iter params_x0/(*params, x0))) -> (success_part, failure_part)/(sprp2exp, non_sprp2exp)/({sprp:exp}, {non_sprp:exp}) if not to_output_statistics else (sprp2exp, non_sprp2exp, total_steps) # [SPRP == strong probable-prime]'

    from seed.algo.rho_method__7iter7batch import Ops4RhoMethod7batch__7factor_pint__7even_exp_add_constant, try_factor_pint7rho_, try_factor_pint7rho__7resume_, reset4new_modulus7factor_pint7rho__7resume_
    #.Ops4RhoMethod7batch__7factor_pint__7even_exp_add_constant(modulus, even_exp, addend)
    #.def try_factor_pint7rho_(ops, imay_max4end6rho, u0_or_scale, may_empty_saver7immutable, /, *, u0_be_floor_sqrt_scale_modulus=False):
    #.def try_factor_pint7rho__7resume_(ops, imay_max4end6rho, record7old, /):
    #.  '-> (final, some_proper_factors, idc, record7old)'





    from seed.math.factor_pint.factor_pint__elliptic_curve_method import try_factor_pint__elliptic_curve_method_
    #def try_factor_pint__elliptic_curve_method_(n, Bs_or_kss=None, ks5n_and_B_or_ks_=None, /, *, random_uint_mod_=None, with_ctx=False, result6fail=None):
    #   'n/uint{>=1} -> Iter (B/uint{>=2}|ks/(Iter k/uint{>=2})) -> may (n -> (B|ks) -> ks) -> may non_trivial_factor{n} # [ks are multiplier => II(ks)*pt] # [B is smooth bound => ks:=chains(repeat(p,floor_log_(p,B)) for p in primes_lt(1+B))] # [[p::prime][n%p==0][1==gcd(n,[1..<p])] -> [best:B1:=exp((1/sqrt2+o(1))*sqrt(ln(p)*lnln(p)))]]'
    #
    from seed.math.factor_pint.factor_pint__elliptic_curve_method import ex1_try_factor_pint__elliptic_curve_method_
    #def ex1_try_factor_pint__elliptic_curve_method_(n, B1, /, *, random_uint_mod_=None, settings4EPC=None):
    #   'n/uint{>=1} -> B1/uint{>=2} -> may (ft/non_trivial_factor{n}, settings4EPC{n}, B1) # [B1 is smooth bound] # [settings4EPC == (args4EPC, xy6EPC) :: ((n,a,b),(x,y))]'


    from seed.math.factor_pint.factor_pint__elliptic_curve_method import try1_factor_pint__elliptic_curve_method_
    #def try1_factor_pint__elliptic_curve_method_(n_or_settings4EPC, B1_or_dup_exps4stage1, B2_or_delta_exps4stage2, /, *, random_uint_mod_=None, result6fail=None, dup_exps_from_B1_=None, delta_exps_from_B1_B2_=None):
    #   '-> (((result6fail|ft), may_exc_or_ctx) | (ft, settings4EPC, stage, ((j4exp, zmay_q1{==max_exp6stage1}) if stage==1 else (max_exp6stage1, j4delta, zmay_q2{==max_exp6stage2}))))'

    from seed.math.factor_pint.factor_pint__elliptic_curve_method import try1_factor_pint__elliptic_curve_method7inversionless_
    #def try1_factor_pint__elliptic_curve_method7inversionless_(n_or_settings4EPC, may_B1=None, may_B2=None, may_max4big_step=None, /, *, random_uint_mod_=None, result6fail=None, dup_exps_from_B1_=None, delta_exps_from_B1_B2_=None, default_B1=10000, default_scale4B2=100, default_max4big_step=1<<16):
    #   '-> (((result6fail|ft), may_exc_or_ctx) | (ft, settings4EPC, stage, ((j4exp, zmay_q1{==max_exp6stage1}) if stage==1 else (max_exp6stage1, j4delta, zmay_q2{==max_exp6stage2}))))'

#.#################################
___end_mark_of_excluded_global_names__0___ = ...


__all__
r'''[[[
@20260914
[[
rho_vs_ECM:here.2
===
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__le_pow2_81   @factor_pint__le_pow2_81_ ='549755813911*1099511627791' +using_ECM +inversionless
    # Random
    {549755813911: 1, 1099511627791: 1}
    total::duration: 0.7501875430000001 *(unit: 0:00:01)

py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__le_pow2_81   @factor_pint__le_pow2_81_ ='549755813911*1099511627791' +using_ECM +inversionless +with_settingss
    ({549755813911: 1, 1099511627791: 1}, (((604462909840849692000601, 14923775115358469412605, 1), (10541229878755366100832, 1)),))
    total::duration: 1.880881079 *(unit: 0:00:01)

    ({549755813911: 1, 1099511627791: 1}, (((604462909840849692000601, -202034900548755701729777, 1), (-139840703184852864221651, 1)),))
    total::duration: 0.35082293600000003 *(unit: 0:00:01)

    ({549755813911: 1, 1099511627791: 1}, (((604462909840849692000601, -289818814942228560223796, 1), (-102630186370812554545569, 1)),))
    total::duration: 1.635154302 *(unit: 0:00:01)

py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__le_pow2_81   @factor_pint__le_pow2_81_ ='549755813911*1099511627791' +using_ECM --_n2settings4EPC='{604462909840849692000601:((604462909840849692000601, -202034900548755701729777, 1), (-139840703184852864221651, 1))}'
    {549755813911: 1, 1099511627791: 1}
    total::duration: 0.723129167 *(unit: 0:00:01)

===
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__le_pow2_81   @factor_pint__le_pow2_81_ ='549755813911*1099511627791' +using_ECM -inversionless
    # Random
    total::duration: 5.77967163 *(unit: 0:00:01)

py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__le_pow2_81   @factor_pint__le_pow2_81_ ='549755813911*1099511627791' +using_ECM -inversionless +with_settingss
    ({549755813911: 1, 1099511627791: 1}, (((604462909840849692000601, -238844943539410519780725, -144177954435258709866479), (74364165618371020917331, 216514399612423748830434)),))
    total::duration: 1.8384451609999999 *(unit: 0:00:01)

    ({549755813911: 1, 1099511627791: 1}, (((604462909840849692000601, 113612373689681093668799, -35105676510727254637001), (-13323696834883514051457, 107231846234603392551700)),))
    total::duration: 0.8044147070000001 *(unit: 0:00:01)

    ({549755813911: 1, 1099511627791: 1}, (((604462909840849692000601, 18426764286133623819458, 201502428517262863668966), (105524329500195629724647, -176413129203945517834447)),))
    total::duration: 1.8505403080000002 *(unit: 0:00:01)

    ({549755813911: 1, 1099511627791: 1}, (((604462909840849692000601, -145285473388244114487881, 184802563999449591581844), (-66409063353429872777492, 242169134493245460633533)),))
    total::duration: 3.964906317 *(unit: 0:00:01)

    ({549755813911: 1, 1099511627791: 1}, (((604462909840849692000601, -52839341178021735480612, 277844712784484400075759), (-92650030823243892396760, -270500905887093727942890)),))
    total::duration: 1.7508722479999999 *(unit: 0:00:01)

    ({549755813911: 1, 1099511627791: 1}, (((604462909840849692000601, -76434491821837347931671, 49058017485055316816124), (114442361590495381402379, -297843683799628017356922)),))
    total::duration: 2.592038168 *(unit: 0:00:01)

    ({549755813911: 1, 1099511627791: 1}, (((604462909840849692000601, 165551835224444326975068, -40432400309918487748668), (293972846397678063079016, -55280335966848148551201)),))
    total::duration: 4.844703626 *(unit: 0:00:01)



===
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__le_pow2_81   @factor_pint__le_pow2_81_ ='549755813911*1099511627791'
    #no Random
    {549755813911: 1, 1099511627791: 1}
    total::duration: 12.830700333 *(unit: 0:00:01)

py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__le_pow2_81   @factor_pint__le_pow2_81_ ='549755813911*1099511627791' +with_idc
    ({549755813911: 1, 1099511627791: 1}, (887005,))
    total::duration: 12.574937949 *(unit: 0:00:01)
    # [2**19 < 887005 < 2**20]

===
+partial_ok
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__le_pow2_81   @factor_pint__le_pow2_81_ ='549755813911*1099511627791' +partial_ok
    ({549755813911: 1, 1099511627791: 1}, {}, {})
    total::duration: 12.480942045 *(unit: 0:00:01)

py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__le_pow2_81   @factor_pint__le_pow2_81_ ='549755813911*1099511627791' +partial_ok --max4num_steps='2**18'
    ({}, {604462909840849692000601: 1}, {})
    total::duration: 3.6437982339999997 *(unit: 0:00:01)

py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__le_pow2_81   @factor_pint__le_pow2_81_ ='549755813911*1099511627791' +partial_ok --max4num_steps='2**20' +u0_be_floor_sqrt_scale_modulus
    ({549755813911: 1, 1099511627791: 1}, {}, {})
    total::duration: 13.205335966 *(unit: 0:00:01)

py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__le_pow2_81   @factor_pint__le_pow2_81_ ='549755813911*1099511627791' +partial_ok --max4num_steps='2**20' +u0_be_floor_sqrt_scale_modulus --u0_or_scale=2
    ({549755813911: 1, 1099511627791: 1}, {}, {})
    total::duration: 12.641410258999999 *(unit: 0:00:01)

===
]]

#]]]'''#'''

r'''[[[
before:@20260914

? nextprime(2^40)
1099511627791
? nextprime(2^39)
549755813911

? factorint(549755813911*1099511627791)
time = 2 ms.
[549755813911,1;1099511627791,1]
? ##
  ***   last result computed in 2 ms.

? ??factorint
factorint(x,{flag = 0}):
   Factors the integer n into a product of pseudoprimes (see ispseudoprime),
        using a combination of
            the Shanks SQUFOF and
            Pollard Rho method (with modifications due to Brent),
            Lenstra's ECM (with modifications by Montgomery), and
            MPQS (the latter adapted from the LiDIA code with the kind permission of the LiDIA maintainers), as well as
            a search for pure powers.

why 2ms vs 4s ???
not caused by "near 2 power" <<==:
    nextprime(sqrtint(2^79*5))
        1738480528859
    nextprime(sqrtint(2^77*3))
        673310613653
    logint(673310613653*1738480528859, 2)
        79
    factorint(673310613653*1738480528859)
        [673310613653,1;1738480528859,1]
    ? ##
      ***   last result computed in 4 ms.



[[
rho_vs_ECM:here.1
===
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__le_pow2_81   @factor_pint__le_pow2_81_ ='549755813911*1099511627791' +using_ECM
    {549755813911: 1, 1099511627791: 1}
    total::duration: 0.997917318 *(unit: 0:00:01)
    total::duration: 13.91103833 *(unit: 0:00:01)
    total::duration: 9.320658043 *(unit: 0:00:01)
    total::duration: 0.998879152 *(unit: 0:00:01)
    total::duration: 2.0438173070000003 *(unit: 0:00:01)
        # Random

===
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__le_pow2_81   @factor_pint__le_pow2_81_ ='549755813911*1099511627791'
    {549755813911: 1, 1099511627791: 1}
        #no Random
    total::duration: 3.440160165 *(unit: 0:00:01)
        @[(_addend,_u0) += (+1, +1)] #before ++"num_repeat"
    total::duration: 8.762207085 *(unit: 0:00:01)
        @[(_addend,_u0) += (+3, +5)] #before ++"num_repeat"
    total::duration: 7.349229636 *(unit: 0:00:01)
        @[(_addend,_u0) += (+1, -1)][num_repeat:=5]
    total::duration: 6.963595950999999 *(unit: 0:00:01)
        @[(_addend,_u0) += (+1@num_repeat-reset, -1)][num_repeat:=5]
    total::duration: 9.466995399 *(unit: 0:00:01)
        @[(_addend,_u0) += (+1@num_repeat-reset, -1)][num_repeat:=3]
    total::duration: 2.166163706 *(unit: 0:00:01)
        @[(_addend,_u0) += (+1@num_repeat-reset, -1)][num_repeat:=3][max_num_tries_per_seed:=_zpow22]#初始即巅峰
    total::duration: 2.167334395 *(unit: 0:00:01)
        @[(_addend,_u0) += (+1@num_repeat-reset, -1)][num_repeat:=3][max_num_tries_per_seed:=_zpow23]#初始即更高峰
    total::duration: 2.1269970120000004 *(unit: 0:00:01)
        @[_addend += (+1@num_repeat-reset)][_u0 := isqrt(_u0*n4part)][num_repeat:=3][max_num_tries_per_seed:=_zpow23]#初始即更高峰

===
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__le_pow2_81   @factor_pint__le_pow2_81_ ='549755813911*1099511627791'  --known_factor4Pmm='2*47846459'
    {549755813911: 1, 1099511627791: 1}
    total::duration: 0.133934608 *(unit: 0:00:01)
        @[(_addend,_u0) += (+1, +1)] #before ++"num_repeat"
    total::duration: 0.35900999899999997 *(unit: 0:00:01)
        @[(_addend,_u0) += (+3, +5)] #before ++"num_repeat"
===
]]

#]]]'''#'''




__all__
_zpow81 = 1<<81
_zpow12 = 1<<12
_zpow16 = 1<<16
_zpow22 = 1<<22
_zpow23 = 1<<23
r'''[[[
before:@20260914

from seed.math.factor_pint.sprp_factor_pint_framework import IFramework4sprp_factor_pint, IFramework4sprp_factor_pint__7mixins7utilities
class _Framework4factor_pint__le_pow2_81(IFramework4sprp_factor_pint__7mixins7utilities):
    ___no_slots_ok___ = True
    #@override
    #_is_SPRP_ = staticmethod(is_prime__le_pow2_81)
    @property
    @override
    def _is_SPRP_(sf, /):
        '-> (pint -> bool)'
        return force_lazy_imported_func_(is_prime__le_pow2_81)
    if 000:
        def sprp_factor_pint_(sf, n4whole, /, *args4whole, **kwds4whole):
            'n4whole/uint{>=1} -> (*args4whole) -> (**kwds4whole) -> output4whole'
    @override
    def _prepare_initial_state4whole_(sf, n4whole, /, *, upperbound4prime_factor4trial_division=_zpow12, known_factor4Pmm=2, addend=1, u0=0, using_ECM=False):
        # xxx:seed4Random=None #st4Random too huge

        #def _prepare_initial_state4whole_(sf, n4whole, /, *args4whole, **kwds4whole):
        'n4whole/uint{>=1} -> (*args4whole) -> (**kwds4whole) -> st'
        check_int_ge(3, upperbound4prime_factor4trial_division)
        check_int_ge_le(1, _zpow81, n4whole)
        check_int_ge(1, known_factor4Pmm)
        check_type_is(int, addend)
        check_type_is(int, u0)
        check_type_is(bool, using_ECM)
        hrem4N_ = mk_hrem_(n4whole)
        _addend = hrem4N_(addend)
        _u0 = hrem4N_(u0)
        _known_factor4Pmm = known_factor4Pmm << (known_factor4Pmm&1)

        args6input = (upperbound4prime_factor4trial_division, known_factor4Pmm, addend, u0)
        args7using = (_known_factor4Pmm, _addend, _u0, using_ECM)
        st0 = (case:=0, args6input, args7using)
        return st0
    @override
    def _format_output4whole_(sf, n4whole, st, raw_output, /):
        'n4whole/uint{>=1} -> st -> raw_output -> output4whole'
        match raw_output:
            #fail:case ({**p2e} as sprp2exp, [] as non_sprp2exp, [] as non_sprp2exp4todo):
            #useless:case ({**p2e} as sprp2exp, {} as non_sprp2exp, {} as non_sprp2exp4todo):
            case ({**p2e} as sprp2exp, {} as non_sprp2exp, {} as non_sprp2exp4todo) if not (non_sprp2exp or non_sprp2exp4todo):
                if not n4whole == II__ft2e_(p2e):raise Exception(n4whole, p2e)

                return p2e
        raise Exception(raw_output)
        raise 000
    @override
    def _stop4whole_(sf, n4whole, st, /):
        'n4whole/uint{>=1} -> st -> whether_stop/bool'
        return False
    @override
    def _core_factor_algo_(sf, st, n4part, /):
        'st -> n4part/uint{>=2} -> (st, some_proper_factors/[factor{n4part}]{neednot_complete,neednot_coprime}) # eg. [some_proper_factors := tmay_proper_factor~imay_proper_factor@seed.algo.rho_method.try_factor1_pint__via_rho_method_]'
        match st:
            case (0, (upperbound4prime_factor4trial_division, known_factor4Pmm, addend, u0) as args6input, (_known_factor4Pmm, _addend, _u0, using_ECM) as args7using):
                (p2e, unfactored_part, may_next_prime_factor) = factor_pint_by_trial_division_ex_(n4part, may_upperbound4prime_factor=upperbound4prime_factor4trial_division)
                if p2e:
                    ps = tuple(sorted(p2e))
                    assert ps
                    st = (case:=1, args6input, args7using)
                    return (st, ps)
                assert may_next_prime_factor
                pass
            case (1, args6input, (_known_factor4Pmm, _addend, _u0, using_ECM) as args7using):
                pass
            case _:
                raise 000
        if using_ECM:
            while 1:
                match try_factor_pint__elliptic_curve_method_(n4part):
                    case None:
                        pass
                    case proper_factor:
                        new_st = (1, args6input, (_known_factor4Pmm, 1+_addend, 1+_u0, using_ECM))
                        return (new_st, (proper_factor,))
            raise 000
        assert not using_ECM
        #.max_num_tries_per_seed = _zpow16
        #.max_num_tries_per_seed = _zpow22
        max_num_tries_per_seed = _zpow23
        num_repeat = num_repeat0 = 3
            # reuse:max_num_tries_per_seed
            # reuse:_addend
        while 1:
            match try_factor1_pint__via_rho_method_(n4part, _step4rho_, seeds=[(_known_factor4Pmm, _addend, _u0)], max_num_tries_per_seed=max_num_tries_per_seed):
                #imay proper_factor
                case -1:
                    pass
                case proper_factor:
                    new_st = (1, args6input, (_known_factor4Pmm, 1+_addend, 1+_u0, using_ECM))
                    return (new_st, (proper_factor,))

            num_repeat -= 1
            if not num_repeat > 0:
                num_repeat = num_repeat0
                if max_num_tries_per_seed < _zpow22:
                    max_num_tries_per_seed <<= 2
                _addend += 1
            _u0 = isqrt(_u0*n4part)
            continue
            _u0 -= 1
            continue
            _addend += 1
            _u0 -= 1
            continue
            _addend += 1
            _u0 += 1
            continue
            _addend += 3
            _u0 += 5
            continue
        raise 000

def _step4rho_(n4part, _known_factor4Pmm, _addend, u, /):
    return (_addend +pow(u, _known_factor4Pmm, n4part))%n4part
_ops = _Framework4factor_pint__le_pow2_81()
def factor_pint__le_pow2_81_(n4whole, /, *, upperbound4prime_factor4trial_division=_zpow12, known_factor4Pmm=2, addend=1, u0=0, using_ECM=False):
    sf = _ops
    return sf.sprp_factor_pint_(n4whole, upperbound4prime_factor4trial_division=upperbound4prime_factor4trial_division, known_factor4Pmm=known_factor4Pmm, addend=addend, u0=u0, using_ECM=using_ECM)
#]]]'''#'''






































def factor_pint__le_pow2_81_(n, /, *, using_ECM=False, **kwds):
    if using_ECM:
        return factor_pint__le_pow2_81__7ECM_(n, **kwds)
    return factor_pint__le_pow2_81__7rho_(n, **kwds)


def factor_pint__le_pow2_81__7rho_(n, /, *, partial_ok=False, with_idc=False, max4prime7trial_division=_zpow12, max4num_steps=_zpow23, even_exp=2, addend=1, u0_or_scale=1, u0_be_floor_sqrt_scale_modulus=False, may_empty_saver7immutable=None):
    _ops7rho = _Framework4factor_pint__le_pow2_81__7rho(partial_ok=partial_ok, more=with_idc)
    return _ops7rho.sprp_factor_pint_(n, max4prime7trial_division, max4num_steps=max4num_steps, even_exp=even_exp, addend=addend, u0_or_scale=u0_or_scale, u0_be_floor_sqrt_scale_modulus=u0_be_floor_sqrt_scale_modulus, may_empty_saver7immutable=may_empty_saver7immutable)


def factor_pint__le_pow2_81__7ECM_(n, /, *, partial_ok=False, with_settingss=False, max4prime7trial_division=_zpow12, max4num_trials=_zpow12, max4num_trials4part=16, _n2settings4EPC={}, inversionless=True):
    _ops7ECM = _Framework4factor_pint__le_pow2_81__7ECM(partial_ok=partial_ok, more=with_settingss, n2settings4EPC=_n2settings4EPC, inversionless=inversionless)
    return _ops7ECM.sprp_factor_pint_(n, max4prime7trial_division, max4num_trials=max4num_trials, max4num_trials4part=max4num_trials4part)




class _IFramework4factor_pint__le_pow2_81__7common(IFramework4sprp_factor_pint):
    ___no_slots_ok___ = True
    def __init__(sf, /, *, partial_ok, more, n2settings4EPC={}, inversionless=True):
        sf.partial_ok = partial_ok
        sf.more = more
        sf.n2settings4EPC = n2settings4EPC
        sf.inversionless = inversionless

    @abstractmethod
    def _st2may_more_info_(sf, st, /):
        return None


    @override
    def _format_output_(sf, n, max4prime7trial_division, p2e7trial_division, n7unfactored_part, st, raw_output, /):
        check_int_ge_le(1, _zpow81, n)
        (sprp2exp, non_sprp2exp, non_sprp2exp4todo) = raw_output
        # !! [n <= 2**81]
        # !! _is_SPRP_:using:is_prime__le_pow2_81
        # [sprp indeed be prime]
        p2e = {**p2e7trial_division, **sprp2exp}
        if sf.partial_ok:
            out = (p2e, non_sprp2exp, non_sprp2exp4todo)
        else:
            if non_sprp2exp or non_sprp2exp4todo:raise Exception
            out = p2e
        out
        may_info = sf._st2may_more_info_(st)
        return out if not sf.more else (out, may_info)
    @property
    @override
    def _is_SPRP_(sf, /):
        '-> (pint -> bool)'
        return force_lazy_imported_func_(is_prime__le_pow2_81)
#end-class _IFramework4factor_pint__le_pow2_81__7common(IFramework4sprp_factor_pint):


class _Framework4factor_pint__le_pow2_81__7ECM(_IFramework4factor_pint__le_pow2_81__7common):

    @override
    def _st2may_more_info_(sf, st, /):
        (num_trials, max4num_trials, max4num_trials4part, rglnkls4settings4EPC) = st
        ls4settings4EPC = tuple(list7up_(rglnkls4settings4EPC))
        return ls4settings4EPC
    @override
    def _core_factor_algo_(sf, st, n7part, /):
        try1_ = try1_factor_pint__elliptic_curve_method_ if not sf.inversionless else try1_factor_pint__elliptic_curve_method7inversionless_
        (num_trials, max4num_trials, max4num_trials4part, rglnkls4settings4EPC) = st
        sz = 0
        szs = range(1, 1+min(max4num_trials4part, max4num_trials4part-num_trials)) if sf.partial_ok else repeat(0)
        for sz in szs:
            ##################
            n7part_or_settings4EPC = sf.n2settings4EPC.get(n7part, n7part)
            for sz7retry, B1 in ((16, 100), (4, 1000), (1, 10000)):
                B2 = 100*B1
                for _ in range(sz7retry):
                    match try1_(n7part_or_settings4EPC, B1, B2):
                        case (None, may_exc_or_ctx):
                            continue
                        case (proper_factor, may_exc_or_ctx):
                            some_proper_factors = (proper_factor,)
                            x_settings4EPC = may_exc_or_ctx
                            break
                        case (proper_factor, settings4EPC, stage, details):
                            some_proper_factors = (proper_factor,)
                            x_settings4EPC = settings4EPC
                            break
                    #match
                    raise 000
                else:
                    continue
                #end-for _ in range(sz7retry):
                some_proper_factors
                break
            else:
                continue
            #end-for sz7retry, B1 in ...:
            some_proper_factors
            break
            raise 000
            ##################
            match ex1_try_factor_pint__elliptic_curve_method_(n7part, B1:=1_00_00, settings4EPC=sf.n2settings4EPC.get(n7part, None)):
                case None:
                    continue
                case (proper_factor, (args4EPC, xy6EPC) as settings4EPC, B1):
                    some_proper_factors = (proper_factor,)
                    x_settings4EPC = settings4EPC
                    break
            raise 000
            ##################
            match try_factor_pint__elliptic_curve_method_(n7part):
                case None:
                    continue
                case proper_factor:
                    some_proper_factors = (proper_factor,)
                    break
            raise 000
            ##################
        else:
            some_proper_factors = ()
        some_proper_factors
        if some_proper_factors:
            rglnkls4settings4EPC = oo_push_(rglnkls4settings4EPC, x_settings4EPC)
            #print(rglnkls4settings4EPC)
        new_st = st if sz == 0 and not some_proper_factors else (num_trials+sz, max4num_trials, max4num_trials4part, rglnkls4settings4EPC)
        assert some_proper_factors or sf.partial_ok
        return (new_st, some_proper_factors)




    @override
    def _mk_state7root_(sf, n, ns, max4prime7trial_division, p2e7trial_division, n7unfactored_part, /, *, max4num_trials, max4num_trials4part):
        check_int_ge_le(1, _zpow81, n)
        args7common = ()
        kwds7common = {}
        check_int_ge(1, max4num_trials4part)
        check_int_ge(max4num_trials4part, max4num_trials)
        rglnkls4settings4EPC = mk_rglnkls_()
        st = (num_trials:=0, max4num_trials, max4num_trials4part, rglnkls4settings4EPC)
        return (st, args7common, kwds7common)
    @override
    def _mk_state7enter_(sf, ns, st7parent, /):
        st7child = st7parent
        return st7child

    @override
    def _mk_state7exit_(sf, ns, st7parent, st, /):
        st7parent7new = st
        #print(st7parent7new[-1])
        return st7parent7new

    @override
    def _stop_(sf, ns, st, /):
        if not sf.partial_ok:return False
        # => nonempty non_sprp2exp4todo
        (num_trials, max4num_trials, max4num_trials4part, rglnkls4settings4EPC) = st
        return num_trials >= max4num_trials
#end-class _Framework4factor_pint__le_pow2_81__7ECM(IFramework4sprp_factor_pint):

class _Framework4factor_pint__le_pow2_81__7rho(_IFramework4factor_pint__le_pow2_81__7common):

    @override
    def _st2may_more_info_(sf, st, /):
        if st is None:
            idc = ()
        else:
            (rope8idc, record7old, max4num_steps, even_exp, addend) = st
            idc = tuple(sorted(iter(rope8idc)))
        return idc
    @override
    def _core_factor_algo_(sf, st, n7part, /):
        (rope8idc, record7old, max4num_steps, even_exp, addend) = st
        ops = Ops4RhoMethod7batch__7factor_pint__7even_exp_add_constant(modulus:=n7part, even_exp, addend)
        imay_max4end6rho = 1+max4num_steps if sf.partial_ok else -1
        (final, some_proper_factors, idc, record7old) = ops.try_factor_pint7rho__7resume_(imay_max4end6rho, record7old)
        rope8idc = Rope(rope8idc, idc)
        #print(idc)
        st = (rope8idc, record7old, max4num_steps, even_exp, addend)
        if not (some_proper_factors or sf.partial_ok):raise Exception(n7part, st)
        return (st, some_proper_factors)



    @override
    def _mk_state7root_(sf, n, ns, max4prime7trial_division, p2e7trial_division, n7unfactored_part, /, *, max4num_steps, even_exp, addend, u0_or_scale, u0_be_floor_sqrt_scale_modulus, may_empty_saver7immutable):
        check_int_ge_le(1, _zpow81, n)
        args7common = ()
        kwds7common = {}
        check_int_ge(1, max4num_steps)
        check_int_ge(2, even_exp)
        check_type_is(int, addend)

        if n == 1:
            st = None
        else:
            ops = Ops4RhoMethod7batch__7factor_pint__7even_exp_add_constant(modulus:=n, even_exp, addend)
            pt_0 = ops.prepare4try_factor_pint7rho_(u0_or_scale, u0_be_floor_sqrt_scale_modulus=u0_be_floor_sqrt_scale_modulus)
            record7new_round = ops.prepare4iter7rho_(pt_0, may_empty_saver7immutable)
            rope8idc = Rope()
            st = (rope8idc, record7new_round, max4num_steps, even_exp, addend)
        return (st, args7common, kwds7common)

    @override
    def _mk_state7enter_(sf, ns, st7parent, /, *args7common, **kwds7common):
        n7part = top6_(ns)
        (rope8idc, record7old, max4num_steps, even_exp, addend) = st7parent
        ops = Ops4RhoMethod7batch__7factor_pint__7even_exp_add_constant(modulus:=n7part, even_exp, addend)
        record7new = ops.reset4new_modulus7factor_pint7rho__7resume_(record7old, modulus7new:=n7part)
        st = (rope8idc, record7new, max4num_steps, even_exp, addend)
        return st
        (jround, jbatch, end6i, i, pt_i, saver_i_jpp_kpp) = record7old
        (k, pt_k, st_i_jpp_kpp) = saver_i_jpp_kpp.last
        st_i_kpp_kpp = 1
        saver_i_kpp_kpp = saver_i_jpp_kpp.oo_clear().oo_append((k, pt_k, st_i_kpp_kpp), non_reproduceable_ok=True)
        record7old = (jround, jbatch, end6i, i, pt_i, saver_i_kpp_kpp)
        st = (rope8idc, record7old, max4num_steps, even_exp, addend)
        return st

    @override
    def _mk_state7exit_(sf, ns, st7parent, st, /, *args7common, **kwds7common):
        (_rope8idc, record7old, max4num_steps, even_exp, addend) = st7parent
        rope8idc = st[0]
        st7parent7new = (rope8idc, record7old, max4num_steps, even_exp, addend)
        return st7parent7new

    @override
    def _stop_(sf, ns, st, /):
        return st is None
        return False
        if not sf.partial_ok:return False


#end-class _Framework4factor_pint__le_pow2_81__7rho(IFramework4sprp_factor_pint):




__all__
from seed.math.factor_pint.factor_pint__le_pow2_81 import factor_pint__le_pow2_81_, factor_pint__le_pow2_81__7rho_, factor_pint__le_pow2_81__7ECM_
#def factor_pint__le_pow2_81_(n, /, *, using_ECM=False, **kwds):
#def factor_pint__le_pow2_81__7rho_(n, /, *, partial_ok=False, with_idc=False, max4prime7trial_division=_zpow12, max4num_steps=_zpow23, even_exp=2, addend=1, u0_or_scale=1, u0_be_floor_sqrt_scale_modulus=False, may_empty_saver7immutable=None):
#def factor_pint__le_pow2_81__7ECM_(n, /, *, partial_ok=False, with_settingss=False, max4prime7trial_division=_zpow12, max4num_trials=_zpow12, max4num_trials4part=16):
from seed.math.factor_pint.factor_pint__le_pow2_81 import *
