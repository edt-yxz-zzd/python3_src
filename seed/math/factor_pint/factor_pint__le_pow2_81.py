#__all__:goto
#rho_vs_ECM:goto
#iter_random_tests_:goto
#iter_random_tests__7ECM_7rho_first_:goto
#   bug__ft_eq_n7part:goto
#   [:性能统计{factor_pint__le_pow2_81__7ECM_7rho_first_}]:goto
#
#DONE: insert rho between trial_division and ECM @factor_pint__le_pow2_81_&factor_pint__le_pow2_81__7ECM_
#
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
>>> factor_pint__le_pow2_81_(-1, using_rho=True)
Traceback (most recent call last):
    ...
TypeError: -1
>>> factor_pint__le_pow2_81_(0, using_rho=True)
Traceback (most recent call last):
    ...
TypeError: 0
>>> factor_pint__le_pow2_81_(1, using_rho=True)
{}
>>> factor_pint__le_pow2_81_(2, using_rho=True)
{2: 1}
>>> factor_pint__le_pow2_81_(1+2**81, using_rho=True)
Traceback (most recent call last):
    ...
TypeError: 2417851639229258349412353
>>> factor_pint__le_pow2_81_(2**81, using_rho=True)
{2: 81}
>>> stable_print(factor_pint__le_pow2_81_(-1+2**81, using_rho=True))
{7: 1, 73: 1, 2593: 1, 71119: 1, 262657: 1, 97685839: 1}
>>> stable_print(factor_pint__le_pow2_81_(-1+2**81, using_rho=True, with_idc=True))
({7: 1, 73: 1, 2593: 1, 71119: 1, 262657: 1, 97685839: 1}, (479, 545))
>>> stable_print(factor_pint__le_pow2_81_(-1+2**81, using_rho=True, with_idc=True, max4prime7trial_division=2))
({7: 1, 73: 1, 2593: 1, 71119: 1, 262657: 1, 97685839: 1}, (4, 13, 59, 479, 545))
>>> stable_print(factor_pint__le_pow2_81_(-1+2**81, using_rho=True, with_idc=True, max4prime7trial_division=2, partial_ok=True, max4num_steps7rho=545))
(({7: 1, 73: 1, 2593: 1, 71119: 1, 262657: 1, 97685839: 1}, {}, {}), (4, 13, 59, 479, 545))
>>> stable_print(factor_pint__le_pow2_81_(-1+2**81, using_rho=True, with_idc=True, max4prime7trial_division=2, partial_ok=True, max4num_steps7rho=544))
(({7: 1, 73: 1, 2593: 1, 262657: 1}, {6947319183841: 1}, {}), (4, 13, 59, 479))
>>> stable_print(factor_pint__le_pow2_81_(-1+2**81, using_rho=True, with_idc=True, max4prime7trial_division=2, partial_ok=True, max4num_steps7rho=479))
(({7: 1, 73: 1, 2593: 1, 262657: 1}, {6947319183841: 1}, {}), (4, 13, 59, 479))
>>> stable_print(factor_pint__le_pow2_81_(-1+2**81, using_rho=True, with_idc=True, max4prime7trial_division=2, partial_ok=True, max4num_steps7rho=478))
(({7: 1, 73: 1, 2593: 1}, {1824762014870125537: 1}, {}), (4, 13, 59))
>>> stable_print(factor_pint__le_pow2_81_(-1+2**81, using_rho=True, with_idc=True, max4prime7trial_division=2, partial_ok=True, max4num_steps7rho=59))
(({7: 1, 73: 1, 2593: 1}, {1824762014870125537: 1}, {}), (4, 13, 59))
>>> stable_print(factor_pint__le_pow2_81_(-1+2**81, using_rho=True, with_idc=True, max4prime7trial_division=2, partial_ok=True, max4num_steps7rho=58))
(({7: 1, 73: 1}, {4731607904558235517441: 1}, {}), (4, 13))
>>> stable_print(factor_pint__le_pow2_81_(-1+2**81, using_rho=True, with_idc=True, max4prime7trial_division=2, partial_ok=True, max4num_steps7rho=13))
(({7: 1, 73: 1}, {4731607904558235517441: 1}, {}), (4, 13))
>>> stable_print(factor_pint__le_pow2_81_(-1+2**81, using_rho=True, with_idc=True, max4prime7trial_division=2, partial_ok=True, max4num_steps7rho=12))
(({7: 1}, {345407377032751192773193: 1}, {}), (4,))
>>> stable_print(factor_pint__le_pow2_81_(-1+2**81, using_rho=True, with_idc=True, max4prime7trial_division=2, partial_ok=True, max4num_steps7rho=4))
(({7: 1}, {345407377032751192773193: 1}, {}), (4,))
>>> stable_print(factor_pint__le_pow2_81_(-1+2**81, using_rho=True, with_idc=True, max4prime7trial_division=2, partial_ok=True, max4num_steps7rho=3))
(({}, {2417851639229258349412351: 1}, {}), ())

>>> #stable_print(factor_pint__le_pow2_81_(549755813911*1099511627791, using_rho=True, known_factor4Pmm=2*47846459))
>>> stable_print(factor_pint__le_pow2_81_(549755813911*1099511627791, using_rho=True, even_exp=2*47846459))
{549755813911: 1, 1099511627791: 1}
>>> stable_print(factor_pint__le_pow2_81_(549755813911*1099511627791, using_rho=True, even_exp=2*47846459, with_idc=True))
({549755813911: 1, 1099511627791: 1}, (21,))
>>> factor_pint__le_pow2_81_(1, using_rho=True, with_idc=True)
({}, ())
>>> factor_pint__le_pow2_81_(2, using_rho=True, with_idc=True)
({2: 1}, ())



factor_pint__le_pow2_81_
    ++kw:using_ECM
    factor_pint__le_pow2_81__7ECM_
        ++kw:with_settingss,_n2settings4EPC
    factor_pint__le_pow2_81__7ECM_7rho_first_
>>> stable_print(factor_pint__le_pow2_81_(n:=549755813911*1099511627791, using_ECM=True, inversionless=False)) #doctest: +SKIP
{549755813911: 1, 1099511627791: 1}

>>> stable_print(factor_pint__le_pow2_81_(n:=549755813911*1099511627791, using_ECM=True, inversionless=False, _n2settings4EPC={n:((604462909840849692000601, 113612373689681093668799, -35105676510727254637001), (-13323696834883514051457, 107231846234603392551700))})) #doctest: +SKIP
{549755813911: 1, 1099511627791: 1}


>>> stable_print(factor_pint__le_pow2_81_(n:=549755813911*1099511627791, using_ECM=True, inversionless=True, _n2settings4EPC={n:((604462909840849692000601, -202034900548755701729777, 1), (-139840703184852864221651, 1))})) #doctest: +SKIP
{549755813911: 1, 1099511627791: 1}





>>> stable_print(factor_pint__le_pow2_81_(n:=549755813911*1099511627791, using_ECM=True, inversionless=False, _n2settings4EPC={n:((604462909840849692000601, 73644595543270219858538, 6138896876984739143010), (-67935367150762130457386, -193852553264515344442992))}))
{549755813911: 1, 1099511627791: 1}
>>> stable_print(factor_pint__le_pow2_81_(n:=549755813911*1099511627791, using_ECM=True, inversionless=True, _n2settings4EPC={n:((604462909840849692000601, 15683270651875612453329, 1), (236180207207973089586995, 1))}))
{549755813911: 1, 1099511627791: 1}




>>> stable_print(factor_pint__le_pow2_81__7ECM_7rho_first_(12289*14341*15361, with_settingss=True, with_idc=True))
({12289: 1, 14341: 1, 15361: 1}, ((94, 246), []))
>>> stable_print(factor_pint__le_pow2_81__7ECM_7rho_first_(12289*14341*15361, with_settingss=True))
({12289: 1, 14341: 1, 15361: 1}, [])
>>> stable_print(factor_pint__le_pow2_81__7ECM_7rho_first_(12289*14341*15361, with_idc=True))
({12289: 1, 14341: 1, 15361: 1}, (94, 246))
>>> stable_print(factor_pint__le_pow2_81__7ECM_7rho_first_(12289*14341*15361))
{12289: 1, 14341: 1, 15361: 1}








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
    factor_pint__le_pow2_81__7ECM_7rho_first_

iter_random_tests_
iter_random_tests__7ECM_7rho_first_

default__using_rho_first
default__max4prime7trial_division
default__max4num_steps7rho
default__max4num_trials7ECM
default__max4num_trials7ECM7part

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
    from seed.debug.print_err import print_err
    from seed.types.Rope import Rope, mk_Rope
    from itertools import repeat, count
    from math import isqrt
    from random import randrange
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
    #.  '-> (final, some_factors, idc, record7old)'





    from seed.math.factor_pint.factor_pint__elliptic_curve_method import try_factor_pint__elliptic_curve_method_
    #def try_factor_pint__elliptic_curve_method_(n, Bs_or_kss=None, ks5n_and_B_or_ks_=None, /, *, random_uint_mod_=None, with_ctx=False, result6fail=None):
    #   'n/uint{>=1} -> Iter (B/uint{>=2}|ks/(Iter k/uint{>=2})) -> may (n -> (B|ks) -> ks) -> may non_trivial_factor{n} # [ks are multiplier => II(ks)*pt] # [B is smooth bound => ks:=chains(repeat(p,floor_log_(p,B)) for p in primes_lt(1+B))] # [[p::prime][n%p==0][1==gcd(n,[1..<p])] -> [best:B1:=exp((1/sqrt2+o(1))*sqrt(ln(p)*lnln(p)))]]'
    #
    from seed.math.factor_pint.factor_pint__elliptic_curve_method import ex1_try_factor_pint__elliptic_curve_method_
    #def ex1_try_factor_pint__elliptic_curve_method_(n, B1, /, *, random_uint_mod_=None, settings4EPC=None):
    #   'n/uint{>=1} -> B1/uint{>=2} -> may (ft/non_trivial_factor{n}, settings4EPC{n}, B1) # [B1 is smooth bound] # [settings4EPC == (args4EPC, xy6EPC) :: ((n,a,b),(x,y))]'



    ####################################
    #new_version:both B1,B2
    ####################################
    from seed.math.factor_pint.factor_pint__elliptic_curve_method import try1_factor_pint__elliptic_curve_method_
    #def try1_factor_pint__elliptic_curve_method_(n_or_settings4EPC, may_B1_or_dup_exps4stage1=None, may_B2_or_asc_exps4stage2=None, /, *, random_uint_mod_=None, result6fail=None, detect_square_at_first=False, dup_exps_from_B1_may_B1pw_=None, asc_exps_from_B1_B2_=None, may_B1_at_stage2=None, may_B1pw_at_stage1=None, B1_from_n_=None, default_scale4B2=100):
    #   '-> (((-9|-2|-1|+1), (result6fail|ft), n_or_settings4EPC, may_exc_or_msg_or_ctx) | (-3, result6fail, settings4EPC, ((ops4EPC, pt6EPC), (B1, B2, pt1, pt2))) | (+2, ft, settings4EPC, stage, ((j4exp, zmay_q1{==max_exp6stage1}) if stage==1 else (max_exp6stage1, j4delta, zmay_q2{==max_exp6stage2}))))



    from seed.math.factor_pint.factor_pint__elliptic_curve_method import try1_factor_pint__elliptic_curve_method7inversionless_
    #def try1_factor_pint__elliptic_curve_method7inversionless_(n_or_settings4EPC, may_B1=None, may_B2=None, may_max4big_step=None, /, *, random_uint_mod_=None, result6fail=None, detect_square_at_first=True, dup_exps_from_B1_may_B1pw_=None, asc_exps_from_B1_B2_=None, default_scale4B2=100, default_max4big_step=1<<16, imay_period4detect=0, may_B1_at_stage2=None, may_B1pw_at_stage1=None, B1_from_n_=None, strict=False):
    #   '-> (((-9|-2|-1|+1), (result6fail|ft), n_or_settings4EPC, may_exc_or_msg_or_ctx) | (-3, result6fail, settings4EPC, ((ops4EPC, pt6EPC), (B1, B2, pt1, pt2))) | (+2, ft, settings4EPC, stage, ((j4exp, zmay_q1{==max_exp6stage1}) if stage==1 else (max_exp6stage1, j4delta, zmay_q2{==max_exp6stage2}))))
    #   [settings4EPC == (args4EPC, XZ6EPC) :: ((n,N4C,D4C),(X,Z))]

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
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__le_pow2_81   @factor_pint__le_pow2_81_ ='549755813911*1099511627791' +using_ECM --_n2settings4EPC='{604462909840849692000601:((604462909840849692000601, -202034900548755701729777, 1), (-139840703184852864221651, 1))}'
    {549755813911: 1, 1099511627791: 1}
    total::duration: 0.723129167 *(unit: 0:00:01)


py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__le_pow2_81   @factor_pint__le_pow2_81_ ='549755813911*1099511627791' +using_ECM +inversionless +with_settingss
    ({549755813911: 1, 1099511627791: 1}, (((604462909840849692000601, -289818814942228560223796, 1), (-102630186370812554545569, 1)),))
    total::duration: 1.635154302 *(unit: 0:00:01)

    ####after{减少占比{[B1:=10000]}}
    ({549755813911: 1, 1099511627791: 1}, (((604462909840849692000601, -20364909009155365515380, 1), (118484407149852971221277, 1)),))
    total::duration: 0.40510562799999994 *(unit: 0:00:01)

    ({549755813911: 1, 1099511627791: 1}, (((604462909840849692000601, 20131030825862550320953, 1), (31678502696936596719446, 1)),))
    total::duration: 1.602889846 *(unit: 0:00:01)
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__le_pow2_81   @factor_pint__le_pow2_81_ ='549755813911*1099511627791' +using_ECM +inversionless +with_settingss +_verbose
    ####after{减少占比{[B1:=10000]}}
    ((604462909840849692000601, 59115648778082293158384, 1), (-76113690075940026331671, 1)) :B1= 200 :B2= 20000 :stage= 2 :details= (199, 640, 5153)
    ({549755813911: 1, 1099511627791: 1}, (((604462909840849692000601, 59115648778082293158384, 1), (-76113690075940026331671, 1)),))
    total::duration: 0.8691863799999999 *(unit: 0:00:01)

    ((604462909840849692000601, 168945804587651519881980, 1), (-95636410015988658685686, 1)) :B1= 300 :B2= 30000 :stage= 2 :details= (293, 640, 5303)
    total::duration: 1.395414527 *(unit: 0:00:01)

    ((604462909840849692000601, 15683270651875612453329, 1), (236180207207973089586995, 1)) :B1= 300 :B2= 30000 :stage= 1 :details= (78, 293)
    total::duration: 1.320948306 *(unit: 0:00:01)

    ((604462909840849692000601, -55754116084215197023007, 1), (-24495813232660716974342, 1)) :B1= 300 :B2= 30000 :stage= 2 :details= (293, 2560, 23581)
    total::duration: 1.434689921 *(unit: 0:00:01)

    ((604462909840849692000601, -20081519723206691902334, 1), (160627151869183643372871, 1)) :B1= 200 :B2= 20000 :stage= 2 :details= (199, 640, 5153)
    total::duration: 1.0531767079999999 *(unit: 0:00:01)

    ((604462909840849692000601, -7577513468616644692987, 1), (79567480232854775951558, 1)) :B1= 300 :B2= 30000 :stage= 2 :details= (293, 320, 2647)
    total::duration: 3.1835336990000003 *(unit: 0:00:01)

    ((604462909840849692000601, -263387916863968589748399, 1), (115347125251065563024224, 1)) :B1= 100 :B2= 10000 :stage= 2 :details= (97, 320, 2339)
    total::duration: 0.696998463 *(unit: 0:00:01)

    [< (js4round=(0, 3, 14), x_settings4EPC=((604462909840849692000601, 197097742550640764932434, 1), (195552093599058745647493, 1)), B1=300, B2=30000, stage=2, details=(293, 3182, 29989)) >]
    total::duration: 1.1046086860000002 *(unit: 0:00:01)

    [< (js4round=(0, 5, 1), x_settings4EPC=((604462909840849692000601, 92454234126377069514722, 1), (133864637128032526501896, 1)), B1=700, B2=70000, stage=2, details=(691, 4160, 40933)) >]
    total::duration: 1.8880445460000002 *(unit: 0:00:01)

    [< (js4round=(0, 3, 10), x_settings4EPC=((604462909840849692000601, -128692737290142111877748, 1), (-50079923289705892056223, 1)), B1=300, B2=30000, stage=2, details=(293, 320, 2647)) >]
    total::duration: 1.0313364710000001 *(unit: 0:00:01)

    [< (js4round=(0, 3, 8), proper_factor=1099511627791, x_settings4EPC=((604462909840849692000601, -284234283382121199913585, 1), (-165896858867726468756590, 1)), B1=300, B2=30000, stage=2, details=(293, 960, 8147)) >]
    total::duration: 0.9559972280000001 *(unit: 0:00:01)

    [< (js4round=(0, 3, 6), proper_factor=549755813911, x_settings4EPC=((604462909840849692000601, -39828808042386927468310, 1), (57529426462881938925329, 1)), B1=300, B2=30000, stage=2, details=(293, 960, 8147)) >]
    total::duration: 0.8486718580000001 *(unit: 0:00:01)





++:_pairs7sz7retry_B1
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__le_pow2_81   @factor_pint__le_pow2_81_ ='549755813911*1099511627791' +using_ECM +inversionless +with_settingss +_verbose
    ####after{去掉{[B1:=10000]}}
    [< (js4round=(0, 3, 23), proper_factor=549755813911, x_settings4EPC=((604462909840849692000601, -236656846118970149437495, 1), (118824335564190815329145, 1)), B1=300, B2=30000, stage=2, details=(293, 320, 2647)) >]
    total::duration: 1.50778223 *(unit: 0:00:01)

    [< (js4round=(0, 3, 1), proper_factor=1099511627791, x_settings4EPC=((604462909840849692000601, -35459297773888161797402, 1), (-181827569230866509496537, 1)), B1=300, B2=30000, stage=2, details=(293, 640, 5303)) >]
    total::duration: 1.085968455 *(unit: 0:00:01)

    [< (js4round=(0, 3, 2), proper_factor=1099511627791, x_settings4EPC=((604462909840849692000601, -136699063107805335575343, 1), (-45338748049220106669975, 1)), B1=300, B2=30000, stage=2, details=(293, 960, 8147)) >]
    total::duration: 1.101507777 *(unit: 0:00:01)



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


py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__le_pow2_81   @factor_pint__le_pow2_81_ ='549755813911*1099511627791' +using_ECM -inversionless +with_settingss +_verbose
    ####after{减少占比{[B1:=10000]}}
    ((604462909840849692000601, -145927939101466966415185, -207331627340976357209259), (225734422857491182087429, 175365583910717056631860)) :B1= 500 :B2= 50000 :stage= 2 :details= (499, 313, 2803)
    total::duration: 3.902407942 *(unit: 0:00:01)

    ((604462909840849692000601, -178651056718642821719303, 16493299631234729111811), (-279159455949762114510237, 160665169464467290947774)) :B1= 700 :B2= 70000 :stage= 2 :details= (691, 4441, 43889)
    total::duration: 5.407358632 *(unit: 0:00:01)

    ((604462909840849692000601, -155578207209523011352606, 206858468046227805922953), (-138510145011335141860410, -10194678741154736673608)) :B1= 700 :B2= 70000 :stage= 2 :details= (691, 2201, 20641)
    total::duration: 5.623004166 *(unit: 0:00:01)

    ((604462909840849692000601, -163640507962505728281236, 11663539682889584853683), (-224454576385950871979597, -190621435137217082701479)) :B1= 500 :B2= 50000 :stage= 2 :details= (499, 275, 2539)
    total::duration: 3.8105307799999997 *(unit: 0:00:01)

    ((604462909840849692000601, -129567861906399790556302, 148641073760833883650740), (-206411590607534455173966, 204270963997790393586442)) :B1= 500 :B2= 50000 :stage= 2 :details= (499, 2370, 22013)
    total::duration: 4.158184626 *(unit: 0:00:01)

    ((604462909840849692000601, 73644595543270219858538, 6138896876984739143010), (-67935367150762130457386, -193852553264515344442992)) :B1= 300 :B2= 30000 :stage= 1 :details= (71, 257)
    total::duration: 8.886406702999999 *(unit: 0:00:01)

    ((604462909840849692000601, 69853860208966862541890, 38820166569943002826376), (-22126137906579189868646, 121700105574596399723787)) :B1= 200 :B2= 20000 :stage= 2 :details= (199, 1681, 14753)
    total::duration: 7.694208688999999 *(unit: 0:00:01)

    [< :js4round= (0, 6, 0) :x_settings4EPC= ((604462909840849692000601, -233516287980666902930443, 278380035818721938499413), (-54177317125889783500966, -167356467310629287574757)) :B1= 1000 :B2= 100000 :stage= 2 :details= (997, 2235, 21407) >]
    total::duration: 5.771197783 *(unit: 0:00:01)

    [< , :js4round=, (0, 5, 6), :x_settings4EPC=, ((604462909840849692000601, 52579247858561495718961, -24847718755492241288022), (30913156755396657520540, 283588168323666183493171)), :B1=, 700, :B2=, 70000, :stage=, 2, :details=, (691, 4737, 47137),  >]
    total::duration: 5.668010083 *(unit: 0:00:01)

    [< (js4round=(0, 3, 0), x_settings4EPC=((604462909840849692000601, 259382781613772196677709, 127863603143205158860610), (48327143848491558959090, 278839066431823856955534)), B1=300, B2=30000, stage=2, details=(293, 1419, 12413)) >]
    total::duration: 2.271613088 *(unit: 0:00:01)

    [< (js4round=(0, 3, 13), x_settings4EPC=((604462909840849692000601, -20000002574251473318708, -247302947425328233462747), (72540310452760530824520, -248142857885576353317823)), B1=300, B2=30000, stage=2, details=(293, 346, 2803)) >]
    total::duration: 2.958946166 *(unit: 0:00:01)

    [< (js4round=(0, 11, 6), proper_factor=549755813911, x_settings4EPC=((604462909840849692000601, -231783102773132076289179, -50816269902896888436873), (-114386999512805666035365, -192685935760697701124326)), B1=500, B2=50000, stage=2, details=(499, 2402, 22291)) >]
    total::duration: 10.493244111000001 *(unit: 0:00:01)

    [< (js4round=(0, 3, 19), proper_factor=1099511627791, x_settings4EPC=((604462909840849692000601, -140860555816628965197650, -133975171045394889477152), (-87429062194307661116785, -265845716270506455712819)), B1=300, B2=30000, stage=2, details=(293, 3068, 28751)) >]
    total::duration: 3.361340317 *(unit: 0:00:01)





++:_pairs7sz7retry_B1
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__le_pow2_81   @factor_pint__le_pow2_81_ ='549755813911*1099511627791' +using_ECM -inversionless +with_settingss +_verbose
    ####after{去掉{[B1:=10000]}}
    [< (js4round=(0, 6, 16), proper_factor=549755813911, x_settings4EPC=((604462909840849692000601, 199497893217263432046615, -234282013521670395048734), (174651933880537788027836, 196266779186704587631785)), B1=1000, B2=100000, stage=2, details=(997, 1030, 9721)) >]
    total::duration: 8.816556395000001 *(unit: 0:00:01)

    [< (js4round=(0, 3, 18), proper_factor=1099511627791, x_settings4EPC=((604462909840849692000601, -37432636559557454984402, 146693379296717331064741), (224889907703519895902083, -239375454775474002908443)), B1=300, B2=30000, stage=2, details=(293, 1258, 10861)) >]
    total::duration: 2.930203627 *(unit: 0:00:01)

    [< (js4round=(0, 6, 0), proper_factor=1099511627791, x_settings4EPC=((604462909840849692000601, 41177667898464554779483, 220215993152488879163575), (-19372942735351051468754, 52164000650760958126900)), B1=1000, B2=100000, stage=2, details=(997, 2430, 23311)) >]
    total::duration: 5.7344598520000005 *(unit: 0:00:01)

    [< (js4round=(0, 3, 29), proper_factor=549755813911, x_settings4EPC=((604462909840849692000601, 230447764063546719731013, -257863118751497798726272), (234083891724461989954696, -762092553840436887608)), B1=300, B2=30000, stage=2, details=(293, 888, 7507)) >]
    total::duration: 3.652740161 *(unit: 0:00:01)

    [< (js4round=(0, 3, 86), proper_factor=549755813911, x_settings4EPC=((604462909840849692000601, 108103344455643462438760, 251922567403262716779841), (256561916156149126377098, 231024218729831085947048)), B1=300, B2=30000, stage=2, details=(293, 688, 5701)) >]
    total::duration: 7.889984164 *(unit: 0:00:01)



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

py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__le_pow2_81   @factor_pint__le_pow2_81_ ='549755813911*1099511627791' +partial_ok --max4num_steps7rho='2**18'
    ({}, {604462909840849692000601: 1}, {})
    total::duration: 3.6437982339999997 *(unit: 0:00:01)

py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__le_pow2_81   @factor_pint__le_pow2_81_ ='549755813911*1099511627791' +partial_ok --max4num_steps7rho='2**20' +u0_be_floor_sqrt_scale_modulus
    ({549755813911: 1, 1099511627791: 1}, {}, {})
    total::duration: 13.205335966 *(unit: 0:00:01)

py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__le_pow2_81   @factor_pint__le_pow2_81_ ='549755813911*1099511627791' +partial_ok --max4num_steps7rho='2**20' +u0_be_floor_sqrt_scale_modulus --u0_or_scale=2
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
[[
#iter_random_tests_:here
===
py_adhoc_call { +lineno +to_show_timedelta  +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__le_pow2_81   ,iter_random_tests_  +using_ECM +inversionless +_verbose +with_settingss  +with_idc +using_rho_first =100
    #只用到rho:47/100
    #只用到ECM:27/100
0: ... ...
1:(434164431139986732877854, ({2: 1, 3: 3, 144983: 1, 55455343441285547: 1}, ((1001,), [])))
0:duration: 0.389807995 *(unit: 0:00:01)
1: ... ...
[< (js4round=(0, 3, 1), proper_factor=30907770343, x_settings4EPC=((84731024404394463653933, 5435028229477934865169, 1), (28485634618421038757882, 1)), B1=300, B2=30000, stage=2, details=(293, 616, 5081)) >]
2:(932041268448339100193263, ({11: 1, 30907770343: 1, 2741414973131: 1}, ((), [((84731024404394463653933, 5435028229477934865169, 1), (28485634618421038757882, 1))])))
1:duration: 0.7445624609999999 *(unit: 0:00:01)
2: ... ...
[< (js4round=(0, 3, 5), proper_factor=1776613374593, x_settings4EPC=((19810461171998277169643, -8432383388071010950398, 1), (-7967049697151364658630, 1)), B1=300, B2=30000, stage=2, details=(293, 3000, 28081)) >]
3:(614124296331946592258933, ({31: 1, 11150687851: 1, 1776613374593: 1}, ((), [((19810461171998277169643, -8432383388071010950398, 1), (-7967049697151364658630, 1))])))
2:duration: 0.6987299260000002 *(unit: 0:00:01)
3: ... ...
4:(1082063601546334863951418, ({2: 1, 7: 1, 11: 1, 131: 1, 53636542160520217307: 1}, ((), [])))
3:duration: 0.0012240000000001139 *(unit: 0:00:01)
4: ... ...
5:(1498059672620128722337749, ({3: 1, 233: 1, 853: 1, 937: 1, 677107: 1, 3960098713: 1}, ((1617,), [])))
4:duration: 0.024788692 *(unit: 0:00:01)
5: ... ...
[< (js4round=(0, 1, 6), proper_factor=68318897, x_settings4EPC=((64847921073509809, 19788634280928515, 1), (12655002328387106, 1)), B1=50, B2=5000, stage=2, details=(47, 448, 3301)) >]
6:(1246286904422566350345490, ({2: 1, 5: 1, 97: 1, 19813: 1, 68318897: 1, 949194497: 1}, ((143,), [((64847921073509809, 19788634280928515, 1), (12655002328387106, 1))])))
5:duration: 0.09942984700000013 *(unit: 0:00:01)
6: ... ...
7:(1074092305765831484892779, ({1249: 1, 859961814063916320971: 1}, ((), [])))
6:duration: 0.0018430770000001928 *(unit: 0:00:01)
7: ... ...
8:(192360556765243053547773, ({3: 1, 7: 1, 101: 1, 6628379: 1, 1244279: 1, 10996393: 1}, ((1249, 3413), [])))
7:duration: 0.0463800769999998 *(unit: 0:00:01)
8: ... ...
9:(390494735228864530789693, ({7: 1, 613: 1, 550661: 1, 165261750766643: 1}, ((2061,), [])))
8:duration: 0.031024846000000217 *(unit: 0:00:01)
9: ... ...
10:(444984864047784130558109, ({444984864047784130558109: 1}, ((), [])))
9:duration: 0.0011756929999999777 *(unit: 0:00:01)
10: ... ...
11:(1095818982418480509388350, ({2: 1, 3: 2, 5: 2, 19: 1, 937: 1, 611459: 1, 223699890719: 1}, ((726,), [])))
10:duration: 0.012893845999999876 *(unit: 0:00:01)
11: ... ...
[< (js4round=(0, 1, 6), proper_factor=136893437, x_settings4EPC=((82439052463714090631, 6141008661209655817, 1), (28929903055484684711, 1)), B1=50, B2=5000, stage=2, details=(47, 268, 1861)) >]
12:(459350400327814912995932, ({2: 2, 7: 1, 199: 1, 136893437: 1, 602213329363: 1}, ((), [((82439052463714090631, 6141008661209655817, 1), (28929903055484684711, 1))])))
11:duration: 0.09509200000000018 *(unit: 0:00:01)
12: ... ...
[< (js4round=(0, 1, 26), proper_factor=110656477, x_settings4EPC=((16241363198013523032767, 6456186153133786284393, 1), (3862093639493003971909, 1)), B1=50, B2=5000, stage=2, details=(47, 592, 4481)) >]
13:(990723155078824904998787, ({61: 1, 110656477: 1, 146772820157771: 1}, ((), [((16241363198013523032767, 6456186153133786284393, 1), (3862093639493003971909, 1))])))
12:duration: 0.18353453799999997 *(unit: 0:00:01)
13: ... ...
14:(2276944607472259461854434, ({2: 1, 397: 1, 2867688422509142899061: 1}, ((), [])))
13:duration: 0.0013486160000000247 *(unit: 0:00:01)
14: ... ...
[< (js4round=(0, 2, 10), proper_factor=5333694397, x_settings4EPC=((118623332306565569359, 32989603891208674418, 1), (1609314400618121849, 1)), B1=100, B2=10000, stage=2, details=(97, 804, 6367)) >]
15:(1647203592408969496119074, ({2: 1, 53: 1, 131: 1, 5333694397: 1, 22240369147: 1}, ((), [((118623332306565569359, 32989603891208674418, 1), (1609314400618121849, 1))])))
14:duration: 0.28294746299999973 *(unit: 0:00:01)
15: ... ...
16:(1753140820282554221567378, ({2: 1, 11: 1, 17: 1, 241: 1, 19450382988467772667: 1}, ((), [])))
15:duration: 0.0012101540000002409 *(unit: 0:00:01)
16: ... ...
17:(1836100995953130480813265, ({5: 1, 13: 1, 27353857: 1, 1032677316038033: 1}, ((1478,), [])))
16:duration: 0.022186768999999718 *(unit: 0:00:01)
17: ... ...
18:(605402140688365371441342, ({2: 1, 3: 1, 7: 1, 17903: 1, 805135266885791117: 1}, ((259,), [])))
17:duration: 0.010272231000000076 *(unit: 0:00:01)
18: ... ...
19:(503435457052289903943855, ({3: 2, 5: 1, 234629: 1, 47681465637930511: 1}, ((620,), [])))
18:duration: 0.01311723099999984 *(unit: 0:00:01)
19: ... ...
20:(1101218879025846116464686, ({2: 1, 3: 1, 183536479837641019410781: 1}, ((), [])))
19:duration: 0.0011359230000000942 *(unit: 0:00:01)
20: ... ...
21:(1403124082469245893131805, ({3: 1, 5: 1, 17: 1, 103: 1, 53421819244974144037: 1}, ((), [])))
20:duration: 0.001046769000000225 *(unit: 0:00:01)
21: ... ...
[< (js4round=(0, 1, 12), proper_factor=286159987, x_settings4EPC=((1297870967117327711, -318524565452502924, 1), (-21770708120506318, 1)), B1=50, B2=5000, stage=2, details=(47, 488, 3607)) >]
22:(2083403476352188956099617, ({7: 1, 229321: 1, 286159987: 1, 4535473253: 1}, ((107,), [((1297870967117327711, -318524565452502924, 1), (-21770708120506318, 1))])))
21:duration: 0.12219761600000023 *(unit: 0:00:01)
22: ... ...
[< (js4round=(0, 1, 6), proper_factor=1460211979, x_settings4EPC=((282486086483676932681411, 113143649831392773627139, 1), (103987619256499406416547, 1)), B1=50, B2=5000, stage=2, details=(47, 624, 4751)) >]
23:(1129944345934707730725644, ({2: 2, 1460211979: 1, 193455532858409: 1}, ((), [((282486086483676932681411, 113143649831392773627139, 1), (103987619256499406416547, 1))])))
22:duration: 0.09688646200000006 *(unit: 0:00:01)
23: ... ...
24:(2303223056991611115657259, ({2411: 1, 955297825380178811969: 1}, ((), [])))
23:duration: 0.00245930800000016 *(unit: 0:00:01)
24: ... ...
[< (js4round=(0, 2, 10), proper_factor=946406443, x_settings4EPC=((7219134731538562601323, 1769625381514401811390, 1), (366659529579239410896, 1)), B1=100, B2=10000, stage=2, details=(97, 292, 2111)) >]
25:(996240592952321638982574, ({2: 1, 3: 1, 23: 1, 946406443: 1, 7627943348161: 1}, ((), [((7219134731538562601323, 1769625381514401811390, 1), (366659529579239410896, 1))])))
24:duration: 0.27890238599999995 *(unit: 0:00:01)
25: ... ...
26:(2035178086509767128540044, ({2: 2, 3: 1, 7: 1, 8440063: 1, 2870631481505257: 1}, ((3176,), [])))
25:duration: 0.04267861499999981 *(unit: 0:00:01)
26: ... ...
27:(754345048696281103716831, ({3: 1, 11: 1, 37: 1, 53549: 1, 11537268906823039: 1}, ((468,), [])))
26:duration: 0.010008923000000003 *(unit: 0:00:01)
27: ... ...
28:(2301952808743373524332794, ({2: 1, 67: 1, 149: 1, 5297: 1, 21765837195493747: 1}, ((143,), [])))
27:duration: 0.007015462000000028 *(unit: 0:00:01)
28: ... ...
29:(1779176340721759481872359, ({3: 1, 11: 1, 43: 1, 28201: 1, 44460269483538061: 1}, ((440,), [])))
28:duration: 0.01009161599999997 *(unit: 0:00:01)
29: ... ...
30:(792200601162172826848926, ({2: 1, 3: 2, 13: 1, 53: 1, 1926893: 1, 5183221: 1, 6395671: 1}, ((2243, 3298), [])))
29:duration: 0.046572999999999976 *(unit: 0:00:01)
30: ... ...
31:(1638765461212456560058197, ({3: 3, 60695017081942835557711: 1}, ((), [])))
30:duration: 0.001075691999999684 *(unit: 0:00:01)
31: ... ...
32:(116578000999452650440838, ({2: 1, 11: 1, 227: 1, 1907: 1, 12241013390106161: 1}, ((), [])))
31:duration: 0.0018653080000001765 *(unit: 0:00:01)
32: ... ...
[< (js4round=(0, 2, 7), proper_factor=1564837069, x_settings4EPC=((257335815739101584887163, -38954261700362076961607, 1), (69999994636419795544284, 1)), B1=100, B2=10000, stage=2, details=(97, 312, 2273)) >]
33:(2058686525912812679097304, ({2: 3, 1564837069: 1, 164448951802727: 1}, ((), [((257335815739101584887163, -38954261700362076961607, 1), (69999994636419795544284, 1))])))
32:duration: 0.2583874609999999 *(unit: 0:00:01)
33: ... ...
34:(2161351537743258255034969, ({7: 1, 23: 1, 71: 1, 189078080460437254399: 1}, ((), [])))
33:duration: 0.0010617689999996571 *(unit: 0:00:01)
34: ... ...
35:(561392947651398752818217, ({19: 1, 37: 1, 1637: 1, 26251: 1, 18583054312897: 1}, ((125,), [])))
34:duration: 0.005216921999999791 *(unit: 0:00:01)
35: ... ...
36:(1225121438593253779910452, ({2: 2, 21191: 1, 28356437: 1, 509701646239: 1}, ((199, 3926), [])))
35:duration: 0.05251323099999983 *(unit: 0:00:01)
36: ... ...
37:(390661392670439697987889, ({22193: 1, 17602910497473964673: 1}, ((329,), [])))
36:duration: 0.010147922999999892 *(unit: 0:00:01)
37: ... ...
38:(1635366573568942852257777, ({3: 1, 373: 1, 14867: 1, 14497669: 1, 6780527921: 1}, ((204, 2572), [])))
37:duration: 0.03808038500000066 *(unit: 0:00:01)
38: ... ...
[< (js4round=(0, 2, 25), proper_factor=229434779659, x_settings4EPC=((541339108855647560332243, -219461093841709425604383, 1), (-226064412531982060227977, 1)), B1=100, B2=10000, stage=2, details=(97, 316, 2297)) >]
39:(2165356435422590241328972, ({2: 2, 229434779659: 1, 2359446591577: 1}, ((), [((541339108855647560332243, -219461093841709425604383, 1), (-226064412531982060227977, 1))])))
38:duration: 0.39380046199999974 *(unit: 0:00:01)
39: ... ...
40:(1385298479781575637114511, ({975823: 1, 1419620648192936257: 1}, ((2533,), [])))
39:duration: 0.03377953900000019 *(unit: 0:00:01)
40: ... ...
[< (js4round=(0, 3, 3), proper_factor=164663689507, x_settings4EPC=((15521497178244760606469, 5753096542292742020660, 1), (720652601220808587315, 1)), B1=300, B2=30000, stage=2, details=(293, 1480, 12959)) >]
41:(496687909703832339407008, ({2: 5, 94261808567: 1, 164663689507: 1}, ((), [((15521497178244760606469, 5753096542292742020660, 1), (720652601220808587315, 1))])))
40:duration: 0.6471451559999997 *(unit: 0:00:01)
41: ... ...
42:(2184717547521766887932653, ({13: 1, 109: 1, 1541790788653328784709: 1}, ((), [])))
41:duration: 0.001151692000000537 *(unit: 0:00:01)
42: ... ...
43:(194158970644321298338915, ({5: 1, 67: 1, 579579016848720293549: 1}, ((), [])))
42:duration: 0.0010116929999997026 *(unit: 0:00:01)
43: ... ...
44:(462646202675271523416250, ({2: 1, 5: 4, 163: 1, 761: 1, 4943: 1, 41659: 1, 14489963: 1}, ((34, 480), [])))
43:duration: 0.010326153999999477 *(unit: 0:00:01)
44: ... ...
[< (js4round=(0, 1, 0), proper_factor=11132003, x_settings4EPC=((251154897192557, -37689564244242, 1), (-77754669304348, 1)), B1=50, B2=5000, stage=2, details=(47, 192, 1283)) >]
45:(1185336812145917529768844, ({2: 2, 23: 1, 113: 1, 453977: 1, 11132003: 1, 22561519: 1}, ((1145,), [((251154897192557, -37689564244242, 1), (-77754669304348, 1))])))
44:duration: 0.06903700000000068 *(unit: 0:00:01)
45: ... ...
[< (js4round=(0, 2, 0), proper_factor=596659781, x_settings4EPC=((5650313269766394641, 458618344448577678, 1), (1917621399037927780, 1)), B1=100, B2=10000, stage=2, details=(97, 504, 3821)) >]
46:(2161521691035864503519909, ({382549: 1, 596659781: 1, 9469908061: 1}, ((815,), [((5650313269766394641, 458618344448577678, 1), (1917621399037927780, 1))])))
45:duration: 0.20671046100000012 *(unit: 0:00:01)
46: ... ...
47:(1135930089190027162468458, ({2: 1, 3: 1, 7: 1, 24151: 1, 150203: 1, 1036747: 1, 7191439: 1}, ((283, 448, 1869), [])))
46:duration: 0.028696384999999935 *(unit: 0:00:01)
47: ... ...
[< (js4round=(0, 1, 3), proper_factor=141323129, x_settings4EPC=((45445211746689983, -19901127486022115, 1), (10253975695173299, 1)), B1=50, B2=5000, stage=2, details=(47, 448, 3301)) >]
48:(1551171823610090638152587, ({281: 1, 121469: 1, 141323129: 1, 321569527: 1}, ((563,), [((45445211746689983, -19901127486022115, 1), (10253975695173299, 1))])))
47:duration: 0.08263023099999955 *(unit: 0:00:01)
48: ... ...
49:(1037727345405398122427743, ({7: 1, 109: 1, 1360062051645344852461: 1}, ((), [])))
48:duration: 0.0010879230000000462 *(unit: 0:00:01)
49: ... ...
50:(508653468575060810262428, ({2: 2, 17: 1, 43: 1, 173958094587914093797: 1}, ((), [])))
49:duration: 0.0009500769999997161 *(unit: 0:00:01)
50: ... ...
[< (js4round=(0, 3, 0), proper_factor=7849515137, x_settings4EPC=((123828872863625208193, -53536264824630084671, 1), (-29298704889667080405, 1)), B1=300, B2=30000, stage=2, details=(293, 268, 2221)) >]
51:(1024807751819362223005268, ({2: 2, 2069: 1, 7849515137: 1, 15775353089: 1}, ((), [((123828872863625208193, -53536264824630084671, 1), (-29298704889667080405, 1))])))
50:duration: 0.5841336940000001 *(unit: 0:00:01)
51: ... ...
52:(2336740074819291528930269, ({17: 2, 103: 1, 78501027138082155707: 1}, ((), [])))
51:duration: 0.0011332300000006512 *(unit: 0:00:01)
52: ... ...
[< (js4round=(0, 2, 21), proper_factor=1874910259, x_settings4EPC=((13898383553550741655009, 6325548466544314618919, 1), (-6929688976047788253993, 1)), B1=100, B2=10000, stage=2, details=(97, 296, 2137)) >]
53:(639325643463334116130414, ({2: 1, 23: 1, 1874910259: 1, 7412826020251: 1}, ((), [((13898383553550741655009, 6325548466544314618919, 1), (-6929688976047788253993, 1))])))
52:duration: 0.36295807800000013 *(unit: 0:00:01)
53: ... ...
54:(295493253346080736777504, ({2: 5, 203789: 1, 45312377837199373: 1}, ((1033,), [])))
53:duration: 0.01915346100000015 *(unit: 0:00:01)
54: ... ...
55:(1596273244416667880926781, ({9439: 1, 354677: 1, 476813147403127: 1}, ((67, 3347), [])))
54:duration: 0.04687969300000017 *(unit: 0:00:01)
55: ... ...
56:(927081038235916586988776, ({2: 3, 115885129779489573373597: 1}, ((), [])))
55:duration: 0.001110999999999862 *(unit: 0:00:01)
56: ... ...
57:(418606385827937819083953, ({3: 1, 1223: 1, 114092773460871577837: 1}, ((), [])))
56:duration: 0.0017366160000005237 *(unit: 0:00:01)
57: ... ...
[< (js4round=(0, 3, 4), proper_factor=16148431847, x_settings4EPC=((17818851646418614165457, -4672338068380640746823, 1), (-667669962558592360397, 1)), B1=300, B2=30000, stage=2, details=(293, 296, 2417)) >]
58:(2173899900863070928185754, ({2: 1, 61: 1, 16148431847: 1, 1103441610631: 1}, ((), [((17818851646418614165457, -4672338068380640746823, 1), (-667669962558592360397, 1))])))
57:duration: 0.668588465 *(unit: 0:00:01)
58: ... ...
59:(1448919168228656139150210, ({2: 1, 3: 1, 5: 1, 53: 1, 70507: 1, 12924531140524217: 1}, ((473,), [])))
58:duration: 0.010151153999999885 *(unit: 0:00:01)
59: ... ...
[< (js4round=(0, 1, 16), proper_factor=170379133, x_settings4EPC=((18281790732374682127, 4607777676629312344, 1), (-9053982156764202216, 1)), B1=50, B2=5000, stage=2, details=(47, 512, 3797)) >]
60:(1828764090540904202528064, ({2: 6, 3: 1, 521: 1, 170379133: 1, 107300644219: 1}, ((), [((18281790732374682127, 4607777676629312344, 1), (-9053982156764202216, 1))])))
59:duration: 0.14161477000000033 *(unit: 0:00:01)
60: ... ...
[< (js4round=(0, 1, 3), proper_factor=71489783, x_settings4EPC=((311473954234533023309, 81954125296725962243, 1), (-70077934301118311301, 1)), B1=50, B2=5000, stage=2, details=(47, 276, 1907)) >]
61:(1883483001256221191949523, ({6047: 1, 71489783: 1, 4356901660123: 1}, ((108,), [((311473954234533023309, 81954125296725962243, 1), (-70077934301118311301, 1))])))
60:duration: 0.08332123099999933 *(unit: 0:00:01)
61: ... ...
62:(410876875687073294494383, ({3: 1, 4289: 1, 7589: 1, 875629: 1, 4805401829: 1}, ((116, 150, 1154), [])))
61:duration: 0.020542691999999363 *(unit: 0:00:01)
62: ... ...
63:(2059706904063735602887390, ({2: 1, 5: 1, 19: 1, 29: 1, 31: 1, 40169: 1, 300193380768451: 1}, ((507,), [])))
62:duration: 0.010132999999999726 *(unit: 0:00:01)
63: ... ...
64:(314135644382546107284114, ({2: 1, 3: 1, 7: 1, 1747: 1, 8568583: 1, 499650141217: 1}, ((1537,), [])))
63:duration: 0.025043691999999673 *(unit: 0:00:01)
64: ... ...
65:(519210789997923922013136, ({2: 4, 3: 4, 7: 2, 15107: 1, 541208237789887: 1}, ((147,), [])))
64:duration: 0.006922768999999995 *(unit: 0:00:01)
65: ... ...
[< (js4round=(0, 1, 20), proper_factor=12552996581, x_settings4EPC=((36289138806710787047, 7357125743321567852, 1), (-7024239564994849634, 1)), B1=50, B2=5000, stage=2, details=(47, 260, 1783)) >]
66:(841690285482849994768118, ({2: 1, 11597: 1, 2890874587: 1, 12552996581: 1}, ((141,), [((36289138806710787047, 7357125743321567852, 1), (-7024239564994849634, 1))])))
65:duration: 0.15866038599999932 *(unit: 0:00:01)
66: ... ...
67:(1787980699653870175231531, ({13: 1, 397: 1, 547373: 1, 632915302453727: 1}, ((3205,), [])))
66:duration: 0.042694769000000576 *(unit: 0:00:01)
67: ... ...
68:(374206939303332582503816, ({2: 3, 29: 1, 953: 1, 56237: 1, 2705629: 1, 11123477: 1}, ((769, 1210), [])))
67:duration: 0.019792922999999796 *(unit: 0:00:01)
68: ... ...
69:(760877823163192914091444, ({2: 2, 7: 1, 359: 1, 827: 1, 91528624690087111: 1}, ((), [])))
68:duration: 0.001425538000000337 *(unit: 0:00:01)
69: ... ...
70:(2374277568666450894797988, ({2: 2, 3: 1, 11: 1, 17986951277776143142409: 1}, ((), [])))
69:duration: 0.0010652310000001108 *(unit: 0:00:01)
70: ... ...
71:(1309795205040377523486350, ({2: 1, 5: 2, 109: 1, 1187: 1, 202467898416388169: 1}, ((), [])))
70:duration: 0.001615383999999942 *(unit: 0:00:01)
71: ... ...
72:(2162286218521752690123073, ({2162286218521752690123073: 1}, ((), [])))
71:duration: 0.0010532310000002099 *(unit: 0:00:01)
72: ... ...
73:(318719585941776778723373, ({101: 1, 139: 1, 547: 1, 613: 1, 49459: 1, 1368924343: 1}, ((475,), [])))
72:duration: 0.009846076999999731 *(unit: 0:00:01)
73: ... ...
74:(592501926435894821377587, ({3: 1, 29: 1, 211: 1, 5309: 1, 56269: 1, 108045363871: 1}, ((183, 281), [])))
73:duration: 0.010899000000000214 *(unit: 0:00:01)
74: ... ...
75:(1634957320644182520651554, ({2: 1, 7: 1, 116782665760298751475111: 1}, ((), [])))
74:duration: 0.001121538000000477 *(unit: 0:00:01)
75: ... ...
76:(171320453299148662277756, ({2: 2, 13: 1, 3294624101906705043803: 1}, ((), [])))
75:duration: 0.0009585389999999805 *(unit: 0:00:01)
76: ... ...
77:(471070215251662318699805, ({5: 1, 79: 1, 120383: 1, 4029563: 1, 2458472971: 1}, ((401, 2795), [])))
76:duration: 0.04096761499999957 *(unit: 0:00:01)
77: ... ...
78:(827271937793007026220072, ({2: 3, 3: 1, 181: 1, 193: 1, 8731: 1, 236527: 1, 477811343: 1}, ((112, 1624), [])))
77:duration: 0.025289616000000237 *(unit: 0:00:01)
78: ... ...
79:(695310567133213714393991, ({7: 1, 29: 1, 3425175207552776918197: 1}, ((), [])))
78:duration: 0.0011065380000001568 *(unit: 0:00:01)
79: ... ...
[< (js4round=(0, 1, 16), proper_factor=593617007, x_settings4EPC=((672814732825067689, -90271443354457244, 1), (-203521856777571535, 1)), B1=50, B2=5000, stage=2, details=(47, 480, 3541)) >]
80:(1129602784049395469483569, ({1678921: 1, 593617007: 1, 1133415527: 1}, ((1254,), [((672814732825067689, -90271443354457244, 1), (-203521856777571535, 1))])))
79:duration: 0.13921492299999993 *(unit: 0:00:01)
80: ... ...
81:(904833988004545201710872, ({2: 3, 113104248500568150213859: 1}, ((), [])))
80:duration: 0.0010523849999994894 *(unit: 0:00:01)
81: ... ...
82:(526107975266889033866576, ({2: 4, 15937: 1, 744451: 1, 2771482957703: 1}, ((273, 431), [])))
81:duration: 0.009974154000000013 *(unit: 0:00:01)
82: ... ...
[< (js4round=(0, 1, 29), proper_factor=213517357, x_settings4EPC=((6986918803883754135277, -2412824618741984621932, 1), (2213566703657792203482, 1)), B1=50, B2=5000, stage=2, details=(47, 292, 2029)) >]
83:(1271619222306843252620414, ({2: 1, 7: 1, 13: 1, 213517357: 1, 32722954714561: 1}, ((), [((6986918803883754135277, -2412824618741984621932, 1), (2213566703657792203482, 1))])))
82:duration: 0.195837770999999 *(unit: 0:00:01)
83: ... ...
84:(1897906522105061796551152, ({2: 4, 41: 1, 2893150186135764933767: 1}, ((), [])))
83:duration: 0.00101684599999885 *(unit: 0:00:01)
84: ... ...
[< (js4round=(0, 1, 2), proper_factor=91874821, x_settings4EPC=((6652243693162293719693, 2903545626535726456470, 1), (2828832260559587925541, 1)), B1=50, B2=5000, stage=2, details=(47, 292, 2029)) >]
85:(1789453553460657010597417, ({269: 1, 91874821: 1, 72405514598633: 1}, ((), [((6652243693162293719693, 2903545626535726456470, 1), (2828832260559587925541, 1))])))
84:duration: 0.07792869200000041 *(unit: 0:00:01)
85: ... ...
[< (js4round=(0, 2, 22), proper_factor=514992707, x_settings4EPC=((45607252395136093026847, -16719126888402975177013, 1), (20233354305322340305002, 1)), B1=100, B2=10000, stage=2, details=(97, 304, 2213)) >]
86:(1413824824249218883832257, ({31: 1, 514992707: 1, 88559025740021: 1}, ((), [((45607252395136093026847, -16719126888402975177013, 1), (20233354305322340305002, 1))])))
85:duration: 0.3714730810000013 *(unit: 0:00:01)
86: ... ...
87:(2286178344359961764577637, ({2286178344359961764577637: 1}, ((), [])))
86:duration: 0.0011683839999996337 *(unit: 0:00:01)
87: ... ...
88:(1644584512892888440621195, ({5: 1, 7: 1, 1451: 1, 32383272873740050027: 1}, ((), [])))
87:duration: 0.0018390769999996337 *(unit: 0:00:01)
88: ... ...
89:(2185794304658723836768049, ({398213: 1, 122027: 1, 44981913055799: 1}, ((484, 936), [])))
88:duration: 0.017317230000001516 *(unit: 0:00:01)
89: ... ...
90:(1851583585921005923232370, ({2: 1, 5: 1, 359: 1, 1741: 1, 20641: 1, 562043: 1, 25535821: 1}, ((126, 1768), [])))
89:duration: 0.029157307999998494 *(unit: 0:00:01)
90: ... ...
91:(2177628152543722780807191, ({3: 1, 11: 1, 13: 1, 131: 1, 2029: 1, 19097349123344021: 1}, ((), [])))
90:duration: 0.0021086930000002724 *(unit: 0:00:01)
91: ... ...
[< (js4round=(0, 2, 6), proper_factor=2210821747, x_settings4EPC=((857849721174151353019, 31734703376451685274, 1), (-334027000649812588435, 1)), B1=100, B2=10000, stage=2, details=(97, 280, 2017)) >]
92:(150981550926650638131344, ({2: 4, 11: 1, 2210821747: 1, 388023015577: 1}, ((), [((857849721174151353019, 31734703376451685274, 1), (-334027000649812588435, 1))])))
91:duration: 0.24780323199999899 *(unit: 0:00:01)
92: ... ...
93:(105157016546123545162179, ({3: 1, 491: 1, 79379: 1, 899352374761937: 1}, ((289,), [])))
92:duration: 0.009756077000000474 *(unit: 0:00:01)
93: ... ...
[< (js4round=(0, 1, 27), proper_factor=395415301, x_settings4EPC=((160274501498003489657, 72960301553130613728, 1), (38587757178897093557, 1)), B1=50, B2=5000, stage=2, details=(47, 544, 4057)) >]
94:(2065136951801774964230445, ({3: 1, 5: 1, 859: 1, 395415301: 1, 405332067557: 1}, ((), [((160274501498003489657, 72960301553130613728, 1), (38587757178897093557, 1))])))
93:duration: 0.19023230900000065 *(unit: 0:00:01)
94: ... ...
95:(692945915333750766441035, ({5: 1, 53: 1, 25806971: 1, 101324957762089: 1}, ((3555,), [])))
94:duration: 0.04885046200000076 *(unit: 0:00:01)
95: ... ...
96:(506530610157264383805669, ({3: 2, 56281178906362709311741: 1}, ((), [])))
95:duration: 0.0011502310000004456 *(unit: 0:00:01)
96: ... ...
97:(1437628596988045839202125, ({3: 3, 5: 3, 29: 1, 31: 1, 473819831743268929: 1}, ((), [])))
96:duration: 0.0007575390000003068 *(unit: 0:00:01)
97: ... ...
98:(63188631169752616916507, ({7: 1, 347: 1, 26014257377419768183: 1}, ((), [])))
97:duration: 0.001114152999999618 *(unit: 0:00:01)
98: ... ...
99:(2226624725380788820812317, ({2226624725380788820812317: 1}, ((), [])))
98:duration: 0.0010062309999998575 *(unit: 0:00:01)
99: ... ...
100:(764993187751151813938492, ({2: 2, 61: 1, 16729: 1, 187412157486202867: 1}, ((281,), [])))
99:duration: 0.009904000000000579 *(unit: 0:00:01)
100: ... ...
100:duration: 0.00014746100000095907 *(unit: 0:00:01)
total::duration: 8.889295402 *(unit: 0:00:01)


===
]]
[[
#iter_random_tests__7ECM_7rho_first_:here
    #old: -> (sz, sz7rho, sz7ECM)
    -> (sz, sz7rho, sz7ECM, sz7both, sz7trial_division_only)
===
py_adhoc_call { +lineno +to_show_timedelta  +to_show_total_timedelta +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__le_pow2_81   ,iter_random_tests__7ECM_7rho_first_   +inversionless +_verbose  =10
    11:(10, 3, 3)
    total::duration: 0.7881896180000001 *(unit: 0:00:01)

py_adhoc_call { +lineno +to_show_timedelta  +to_show_total_timedelta +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__le_pow2_81   ,iter_random_tests__7ECM_7rho_first_   +inversionless +_verbose  =100
    101:(100, 50, 24)
    total::duration: 7.662638938000001 *(unit: 0:00:01)

py_adhoc_call { +lineno +to_show_timedelta  +to_show_total_timedelta +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__le_pow2_81   ,iter_random_tests__7ECM_7rho_first_   +inversionless +_verbose  =1000
    1001:(1000, 486, 282)
    total::duration: 69.776057143 *(unit: 0:00:01)

py_adhoc_call { +lineno +to_show_timedelta  +to_show_total_timedelta +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__le_pow2_81   ,iter_random_tests__7ECM_7rho_first_   +inversionless +_verbose  =10000
    5018:((5018, 2351, 1458), (2386480851408344309006279, ({2386480851408344309006279: 1}, ((), []))))
    total::duration: 370.887233172 *(unit: 0:00:01)
    ^Exception: (173840879, 173840879, (173840879,))
        #line 276, in _raw_sprp_factor_pint_
        if not 1 < ft < n7part:raise Exception(n7part, ft, some_proper_factors)
            ###how??? see:bug__ft_eq_n7part  && [u0_or_scale=7][u0_be_floor_sqrt_scale_modulus=True]

py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__le_pow2_81   @factor_pint__le_pow2_81_ ='173840879' +using_ECM +inversionless +with_settingss +_verbose +using_rho_first +with_idc
    _core_factor_algo_:173840879:(39,):(5431,)
    ({5431: 1, 32009: 1}, ((39,), []))
    #   试除法 [max4prime7trial_division == _zpow12 == 4096 < 5431]
    #   !! bug__ft_eq_n7part.2

py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__le_pow2_81   @factor_pint__le_pow2_81_ ='173840879' +using_ECM +inversionless +with_settingss +_verbose -using_rho_first
    before{bug__kwds_pop_using_rho_first}:
        ({5431: 1, 32009: 1}, [])
        误导:以为: #   试除法 [max4prime7trial_division >= 5431]
    after{bug__kwds_pop_using_rho_first}:
        [< (js4round=(0, 0, 0), proper_factor=32009, x_settings4EPC=((173840879, 45772886, 1), (-64316261, 1)), B1=10, B2=1000, stage=2, details=(7, 112, 643)) >]




again:
py_adhoc_call { +lineno +to_show_timedelta  +to_show_total_timedelta +to_show_StopIteration_value  --may_args4PeriodicToilLeisureTime='(1,4)' --may_prompt_string6resting:$'\n\n    resting...\n\n' }  seed.math.factor_pint.factor_pint__le_pow2_81   ,iter_random_tests__7ECM_7rho_first_   +inversionless +_verbose  =10000
    10001:(10000, 4604, 2811)
    total::duration: 666.9295390699999 *(unit: 0:00:01)

    10001:(10000, 4711, 2738)
    total::duration: 647.418383681 *(unit: 0:00:01)

    10001:(10000, 4703, 2756)
    total::duration: 664.391561322 *(unit: 0:00:01)


    ##################
    # ++sz7both,sz7trial_division_only
    ##################
    10001:(10000, 4662, 2688, 610, 3260)
    total::duration: 669.9099197549999 *(unit: 0:00:01)

    ##################
    # above:after{fix:bug__ft_eq_n7part.1}&&before{fix:bug__ft_eq_n7part.2}
    ##################
    below:after{fix:bug__ft_eq_n7part.1,bug__ft_eq_n7part.2}
    ##################

    10001:(10000, 4691, 2775, 689, 3223)
    total::duration: 670.7234671360001 *(unit: 0:00:01)
        # [10000 == 4691+2775-689+3223]

    10001:(10000, 4700, 2841, 705, 3164)
    total::duration: 676.437974017 *(unit: 0:00:01)
        # [10000 == 4700+2841-705+3164]

==>>:
    ##################
    # [:性能统计{factor_pint__le_pow2_81__7ECM_7rho_first_}]:here
    ##################
    耗时:0.07秒/数
    尸方法起作用的概率是47%
    椭圆曲线法起作用的概率是28%
    尸方法椭圆曲线法共同起作用的概率是7%
    仅试除法起作用的概率是32%
    仅试除法尸方法共同起作用的概率是40%
    仅试除法椭圆曲线法共同起作用的概率是21%
    where:
        partial_ok = False
        default__max4prime7trial_division = _zpow12
            && max4num_steps7rho = max4num_steps7rho if not None is max4num_steps7rho else max(default__max4prime7trial_division, max4prime7trial_division)
        using:_pairs7sz7retry_B1__20260920
    ##################
===
]]


#]]]'''#'''




__all__

_zpow81 = 1<<81
_zpow12 = 1<<12
_zpow23 = 1<<23

default__max4num_steps7rho = _zpow23
    #max4num_steps7rho
default__max4prime7trial_division = _zpow12
    #max4prime7trial_division
#old:default__max4num_trials7ECM = _zpow12# ~=1000 ~= max_B1{sqrt(2**81)} ~= default__max4prime7trial_division
# !! _pairs7sz7retry_B1 => inner loop: (30,1000)
default__max4num_trials7ECM = 32 # [32*30 ~= 1000 ~= max_B1{sqrt(2**81)} ~= _zpow12 ~= default__max4prime7trial_division]
    #max4num_trials7ECM
default__max4num_trials7ECM7part = 16
    #max4num_trials7ECM7part

r'''[[[
before:@20260914

_zpow16 = 1<<16
_zpow22 = 1<<22
default__upperbound4prime_factor4trial_division = _zpow12
    #upperbound4prime_factor4trial_division
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
    def _prepare_initial_state4whole_(sf, n4whole, /, *, upperbound4prime_factor4trial_division=default__upperbound4prime_factor4trial_division, known_factor4Pmm=2, addend=1, u0=0, using_ECM=False):
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
def factor_pint__le_pow2_81_(n4whole, /, *, upperbound4prime_factor4trial_division=default__upperbound4prime_factor4trial_division, known_factor4Pmm=2, addend=1, u0=0, using_ECM=False):
    sf = _ops
    return sf.sprp_factor_pint_(n4whole, upperbound4prime_factor4trial_division=upperbound4prime_factor4trial_division, known_factor4Pmm=known_factor4Pmm, addend=addend, u0=u0, using_ECM=using_ECM)
#]]]'''#'''






































#def factor_pint__le_pow2_81_(n, /, *, using_ECM=False, **kwds):
def factor_pint__le_pow2_81_(n, /, *, using_rho:bool=None, using_ECM:bool=None, **kwds):
    if not None is using_ECM:
        check_type_is(bool, using_ECM)
    if not None is using_rho:
        check_type_is(bool, using_rho)
    match sum(map(bool, [using_rho, using_ECM])):
        case 0:
            if not False is using_ECM:
                using_ECM = True
            elif not False is using_rho:
                using_rho = True
            else:
                raise TypeError('[using_ECM:=False][using_rho:=False]')
        case 1:
            pass
        case 2:
            raise TypeError('[using_ECM:=True][using_rho:=True]')
        case _:
            raise 000

    assert bool(using_rho) ^ bool(using_ECM)

    if using_ECM:
        #bug:if kwds.pop('using_rho_first', default__using_rho_first):
        #   bug__kwds_pop_using_rho_first:here
        if kwds.get('using_rho_first', default__using_rho_first):
            kwds.pop('using_rho_first', default__using_rho_first)
            return factor_pint__le_pow2_81__7ECM_7rho_first_(n, **kwds)
        assert (not kwds['using_rho_first']) if default__using_rho_first else (not kwds.get('using_rho_first', False))
        return factor_pint__le_pow2_81__7ECM_(n, **kwds)
    if using_rho:
        return factor_pint__le_pow2_81__7rho_(n, **kwds)

default__using_rho_first = True

def factor_pint__le_pow2_81__7rho_(n, /, *, partial_ok=False, with_idc=False, max4prime7trial_division=default__max4prime7trial_division, max4num_steps7rho=default__max4num_steps7rho, even_exp=2, addend=1, u0_or_scale=1, u0_be_floor_sqrt_scale_modulus=False, may_empty_saver7immutable=None, _verbose=False):
    _ops7rho = _Framework4factor_pint__le_pow2_81__7rho(partial_ok=partial_ok, more=with_idc, verbose=_verbose)
    return _ops7rho.sprp_factor_pint_(n, max4prime7trial_division, max4num_steps7rho=max4num_steps7rho, even_exp=even_exp, addend=addend, u0_or_scale=u0_or_scale, u0_be_floor_sqrt_scale_modulus=u0_be_floor_sqrt_scale_modulus, may_empty_saver7immutable=may_empty_saver7immutable)










def _valitate_out_(n, out, /, *, partial_ok, more):
    if more:
        (out, _) = out
    if not partial_ok:
        p2e = out
        assert n == II__ft2e_(p2e)
    else:
        (p2e, non_sprp2exp, non_sprp2exp4todo) = out
        assert not (p2e.keys() & non_sprp2exp.keys())
        assert not (p2e.keys() & non_sprp2exp4todo.keys())
        assert not (non_sprp2exp.keys() & non_sprp2exp4todo.keys())
        assert n == II__ft2e_(p2e)*II__ft2e_(non_sprp2exp)*II__ft2e_(non_sprp2exp4todo)

def _pow_ft2e_(ft2e, k, /):
    return {ft:e*k for ft, e in ft2e.items()}

def factor_pint__le_pow2_81__7ECM_(n, /, *, partial_ok=False, with_settingss=False, max4prime7trial_division=default__max4prime7trial_division, max4num_trials7ECM=default__max4num_trials7ECM, max4num_trials7ECM7part=default__max4num_trials7ECM7part, _n2settings4EPC={}, inversionless=True, _verbose=False, using_rho_first=default__using_rho_first):
    if using_rho_first:
        kwds = dict(locals())
        777;del kwds['n']
        777;del kwds['using_rho_first']
        return factor_pint__le_pow2_81__7ECM_7rho_first_(n, **kwds)
    else:
        _ops7ECM = _Framework4factor_pint__le_pow2_81__7ECM(partial_ok=partial_ok, more=with_settingss, n2settings4EPC=_n2settings4EPC, inversionless=inversionless, verbose=_verbose)
        return _ops7ECM.sprp_factor_pint_(n, max4prime7trial_division, max4num_trials7ECM=max4num_trials7ECM, max4num_trials7ECM7part=max4num_trials7ECM7part)

def factor_pint__le_pow2_81__7ECM_7rho_first_(n, /, *, partial_ok=False, with_settingss=False, max4prime7trial_division=default__max4prime7trial_division, max4num_trials7ECM=default__max4num_trials7ECM, max4num_trials7ECM7part=default__max4num_trials7ECM7part, _n2settings4EPC={}, inversionless=True, _verbose=False, with_idc=False, max4num_steps7rho=None):
    with_settingss = bool(with_settingss)
    with_idc = bool(with_idc)
    max4num_steps7rho = max4num_steps7rho if not None is max4num_steps7rho else max(default__max4prime7trial_division, max4prime7trial_division)
    r = factor_pint__le_pow2_81__7rho_(n, partial_ok=True, with_idc=True, max4prime7trial_division=max4prime7trial_division, max4num_steps7rho=max4num_steps7rho, even_exp=2, addend=1, u0_or_scale=7, u0_be_floor_sqrt_scale_modulus=True, may_empty_saver7immutable=None, _verbose=_verbose)
    777;max4prime7trial_division = 2
    777;using_rho_first = False
    kwds = dict(locals())
    777;del kwds['n']
    777;del kwds['r']
    777;del kwds['with_idc']
    777;del kwds['max4num_steps7rho']
    ((pre__p2e, pre__non_sprp2exp, pre__non_sprp2exp4todo), pre__idc) = r

    g__xsettingss = []
    (g__p2e, g__non_sprp2exp, g__non_sprp2exp4todo) = ({}, {}, {})
    777;g__p2e.update(pre__p2e)
    for n7part, e in sorted([*pre__non_sprp2exp.items(), *pre__non_sprp2exp4todo.items()]):
        r = factor_pint__le_pow2_81__7ECM_(n7part, **kwds)
        if with_settingss:
            (r, _xsettingss) = r
            g__xsettingss.extend(_xsettingss)
        r
        if partial_ok:
            (_p2e, _non_sprp2exp, _non_sprp2exp4todo) = r
            777;g__non_sprp2exp.update(_pow_ft2e_(_non_sprp2exp, e))
            777;g__non_sprp2exp4todo.update(_pow_ft2e_(_non_sprp2exp4todo, e))
        else:
            _p2e = r
        _p2e
        777;g__p2e.update(_pow_ft2e_(_p2e, e))
    g__xsettingss
    out = (g__p2e, g__non_sprp2exp, g__non_sprp2exp4todo) if partial_ok else g__p2e
    _valitate_out_(n, out, partial_ok=partial_ok, more=False)
    match (with_idc, with_settingss):
        case (False, False):
            may_info = None
        case (False, True):
            may_info = g__xsettingss
        case (True, False):
            may_info = pre__idc
        case (True, True):
            may_info = (pre__idc, g__xsettingss)
        case _:
            raise 000
    may_info
    return out if None is may_info else (out, may_info)













class _IFramework4factor_pint__le_pow2_81__7common(IFramework4sprp_factor_pint):
    ___no_slots_ok___ = True
    def __init__(sf, /, *, partial_ok, more, n2settings4EPC={}, inversionless=True, verbose=False):
        sf.partial_ok = partial_ok
        sf.more = more
        sf.n2settings4EPC = n2settings4EPC
        sf.inversionless = inversionless
        sf.verbose = verbose

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


_pairs7sz7retry_B1__20260920 = ((10, 10), (30, 50), (50, 100), (100, 300), (30, 500), (20, 700), (30, 1000))
_pairs7sz7retry_B1__20260921 = ((10, 10), (20, 30), (20, 100), (100, 300), (20, 600), (30, 1000))
    # (30, 1000) => default__max4num_trials7ECM
_pairs7sz7retry_B1 = _pairs7sz7retry_B1__20260920
_pairs7sz7retry_B1 = _pairs7sz7retry_B1__20260921

def _mk_pairs7sz7retry_B1__7n_le_zpow81_():
    # !! [B1{sqrt(2**81)} ~= 1000][num_trials ~= B1]
    # => 去掉{[B1:=10000]}
    return _pairs7sz7retry_B1
    if 0:
        ##################
        #old:
        ##################
        # ls = ((16, 100), (4, 1000), (1, 10000))
        # !! [B1{sqrt(2**81)} ~= 1000][num_trials ~= B1]
        # => 减少占比{[B1:=10000]}
        ls1 = [(50, 10), (30, 100), (20, 200), (20, 300), (10, 500), (7, 700), (5, 1000)]
        #ls2 = [(20, 10), (20, 100), (10, 200), (10, 300), (5, 500), (5, 700), (30, 1000)]
        #ls = (*ls1*4, *ls2*10, (1, 10000))
        #ls = (*ls1*4, (100, 1000), (1, 10000))
        ls2 = [(10, 200), (30, 300), (5, 500), (5, 700), (5, 1000)]
        ls = (*ls1*4, *ls2*4, (50, 300), (100, 1000), (1, 10000))
class _Framework4factor_pint__le_pow2_81__7ECM(_IFramework4factor_pint__le_pow2_81__7common):

    @override
    def _st2may_more_info_(sf, st, /):
        (num_trials, max4num_trials7ECM, max4num_trials7ECM7part, rglnkls4settings4EPC) = st
        ls4settings4EPC = tuple(list7up_(rglnkls4settings4EPC))
        return ls4settings4EPC
    @override
    def _core_factor_algo_(sf, st, n7part, /):
        try1_ = try1_factor_pint__elliptic_curve_method_ if not sf.inversionless else try1_factor_pint__elliptic_curve_method7inversionless_
        (num_trials, max4num_trials7ECM, max4num_trials7ECM7part, rglnkls4settings4EPC) = st
        sz = 0
        szs = range(1, 1+min(max4num_trials7ECM7part, max4num_trials7ECM7part-num_trials)) if sf.partial_ok else repeat(0)
        ls = _mk_pairs7sz7retry_B1__7n_le_zpow81_()
        for j4round7outer, sz in enumerate(szs):
            ##################
            n7part_or_settings4EPC = sf.n2settings4EPC.get(n7part, n7part)
            for j4round7intermediate, (sz7retry, B1) in enumerate(ls):
                B2 = 100*B1
                for j4round7inner in range(sz7retry):
                    match try1_(n7part_or_settings4EPC, B1, B2):
                        case (_, None, _n7part_or_settings4EPC, may_exc_or_msg_or_ctx):
                            continue
                        case (_, proper_factor, _n7part_or_settings4EPC, may_exc_or_msg_or_ctx):
                            some_proper_factors = (proper_factor,)
                            x_settings4EPC = _n7part_or_settings4EPC
                            if sf.verbose:print_err('[< (', 'js4round=', (j4round7outer, j4round7intermediate, j4round7inner), ', proper_factor=', proper_factor, ', x_settings4EPC=', x_settings4EPC, ', B1=', B1, ', B2=', B2, ', may_exc_or_msg_or_ctx=', may_exc_or_msg_or_ctx, ') >]', sep='')
                            break
                        case (_, proper_factor, _settings4EPC, stage, details):
                            some_proper_factors = (proper_factor,)
                            x_settings4EPC = _settings4EPC
                            if sf.verbose:print_err('[< (', 'js4round=', (j4round7outer, j4round7intermediate, j4round7inner), ', proper_factor=', proper_factor, ', x_settings4EPC=', x_settings4EPC, ', B1=', B1, ', B2=', B2, ', stage=', stage, ', details=', details, ') >]', sep='')
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
        new_st = st if sz == 0 and not some_proper_factors else (num_trials+sz, max4num_trials7ECM, max4num_trials7ECM7part, rglnkls4settings4EPC)
        assert some_proper_factors or sf.partial_ok
        return (new_st, some_proper_factors)




    @override
    def _mk_state7root_(sf, n, ns, max4prime7trial_division, p2e7trial_division, n7unfactored_part, /, *, max4num_trials7ECM, max4num_trials7ECM7part):
        check_int_ge_le(1, _zpow81, n)
        args7common = ()
        kwds7common = {}
        check_int_ge(1, max4num_trials7ECM7part)
        check_int_ge(max4num_trials7ECM7part, max4num_trials7ECM)
        rglnkls4settings4EPC = mk_rglnkls_()
        st = (num_trials:=0, max4num_trials7ECM, max4num_trials7ECM7part, rglnkls4settings4EPC)
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
        (num_trials, max4num_trials7ECM, max4num_trials7ECM7part, rglnkls4settings4EPC) = st
        return num_trials >= max4num_trials7ECM
#end-class _Framework4factor_pint__le_pow2_81__7ECM(IFramework4sprp_factor_pint):

class _Framework4factor_pint__le_pow2_81__7rho(_IFramework4factor_pint__le_pow2_81__7common):

    @override
    def _st2may_more_info_(sf, st, /):
        if st is None:
            idc = ()
        else:
            (rope8idc, record7old, max4num_steps7rho, even_exp, addend) = st
            idc = tuple(sorted(iter(rope8idc)))
        return idc
    @override
    def _core_factor_algo_(sf, st, n7part, /):
        (rope8idc, record7old, max4num_steps7rho, even_exp, addend) = st7old = st
        ops = Ops4RhoMethod7batch__7factor_pint__7even_exp_add_constant(modulus:=n7part, even_exp, addend)
        imay_max4end6rho = 1+max4num_steps7rho if sf.partial_ok else -1
        #bug:(final, some_proper_factors, idc, record7old) = ops.try_factor_pint7rho__7resume_(imay_max4end6rho, record7old)
        #   bug__ft_eq_n7part:here.1
        if 1:
            (final, some_factors, idc, record7old) = ops.try_factor_pint7rho__7resume_(imay_max4end6rho, record7old)
            777;some_proper_factors = some_factors[:-1] if some_factors and some_factors[-1] == n7part else some_factors
            assert len(idc) == len(some_factors)
            assert 0 <= len(idc) -len(some_proper_factors) <= 1
        some_proper_factors
        idc
        rope8idc = Rope(rope8idc, idc)
        #print(idc)
        st = (rope8idc, record7old, max4num_steps7rho, even_exp, addend)
        if not (some_proper_factors or sf.partial_ok):raise Exception(n7part, st)
        #if sf.verbose:print_err('rho:_core_factor_algo_', st7old, n7part, st, idc, some_proper_factors, sep=':')
        if sf.verbose:print_err('rho:_core_factor_algo_', n7part, idc, some_proper_factors, sep=':')
        return (st, some_proper_factors)



    @override
    def _mk_state7root_(sf, n, ns, max4prime7trial_division, p2e7trial_division, n7unfactored_part, /, *, max4num_steps7rho, even_exp, addend, u0_or_scale, u0_be_floor_sqrt_scale_modulus, may_empty_saver7immutable):
        check_int_ge_le(1, _zpow81, n)
        args7common = ()
        kwds7common = {}
        check_int_ge(1, max4num_steps7rho)
        check_int_ge(2, even_exp)
        check_type_is(int, addend)

        r'''[[[
        #   bug__ft_eq_n7part:here.2
        if n == 1:
            st = None
        else:
            ops = Ops4RhoMethod7batch__7factor_pint__7even_exp_add_constant(modulus:=n, even_exp, addend)
            ... ...
        #]]]'''#'''
        if n7unfactored_part == 1:
            st = None
        else:
            ops = Ops4RhoMethod7batch__7factor_pint__7even_exp_add_constant(modulus:=n7unfactored_part, even_exp, addend)
            pt_0 = ops.prepare4try_factor_pint7rho_(u0_or_scale, u0_be_floor_sqrt_scale_modulus=u0_be_floor_sqrt_scale_modulus)
            record7new_round = ops.prepare4iter7rho_(pt_0, may_empty_saver7immutable)
            rope8idc = Rope()
            st = (rope8idc, record7new_round, max4num_steps7rho, even_exp, addend)
        #if sf.verbose:print_err('rho:_mk_state7root_', st, sep=':')
        return (st, args7common, kwds7common)

    @override
    def _mk_state7enter_(sf, ns, st7parent, /, *args7common, **kwds7common):
        n7part = top6_(ns)
        (rope8idc, record7old, max4num_steps7rho, even_exp, addend) = st7parent
        ops = Ops4RhoMethod7batch__7factor_pint__7even_exp_add_constant(modulus:=n7part, even_exp, addend)
        record7new = ops.reset4new_modulus7factor_pint7rho__7resume_(record7old, modulus7new:=n7part)
        st = (rope8idc, record7new, max4num_steps7rho, even_exp, addend)
        #if sf.verbose:print_err('rho:_mk_state7enter_', st7parent, st, sep=':')
        return st
        (jround, jbatch, end6i, i, pt_i, saver_i_jpp_kpp) = record7old
        (k, pt_k, st_i_jpp_kpp) = saver_i_jpp_kpp.last
        st_i_kpp_kpp = 1
        saver_i_kpp_kpp = saver_i_jpp_kpp.oo_clear().oo_append((k, pt_k, st_i_kpp_kpp), non_reproduceable_ok=True)
        record7old = (jround, jbatch, end6i, i, pt_i, saver_i_kpp_kpp)
        st = (rope8idc, record7old, max4num_steps7rho, even_exp, addend)
        return st

    @override
    def _mk_state7exit_(sf, ns, st7parent, st, /, *args7common, **kwds7common):
        (_rope8idc, record7old, max4num_steps7rho, even_exp, addend) = st7parent
        rope8idc = st[0]
        st7parent7new = (rope8idc, record7old, max4num_steps7rho, even_exp, addend)
        #if sf.verbose:print_err('rho:_mk_state7exit_', st7parent, st, st7parent7new, sep=':')
        return st7parent7new

    @override
    def _stop_(sf, ns, st, /):
        return st is None
        return False
        if not sf.partial_ok:return False


#end-class _Framework4factor_pint__le_pow2_81__7rho(IFramework4sprp_factor_pint):



def iter_random_tests_(may_max_sz, /, *args, **kwds):
    it = count() if None is may_max_sz else range(may_max_sz)
    for j in it:
        n = randrange(1, _zpow81)
        yield (n, factor_pint__le_pow2_81_(n, *args, **kwds))

def iter_random_tests__7ECM_7rho_first_(may_max_sz, /, *args, **kwds):
    it = iter_random_tests_(may_max_sz, *args, using_ECM=True, using_rho_first=True, with_settingss=True, with_idc=True, **kwds)
    sz = sz7rho = sz7ECM = sz7both = sz7trial_division_only = 0
    try:
        for sz, r in enumerate(it, 1):
            (n, (out, (idc7rho, x_settingss))) = r
            b_rho = bool(idc7rho)
            b_ECM = bool(x_settingss)
            sz7rho += b_rho
            sz7ECM += b_ECM
            sz7both += b_rho and b_ECM
            sz7trial_division_only += not (b_rho or b_ECM)
            yield ((sz, sz7rho, sz7ECM, sz7both, sz7trial_division_only), r)
            check_type_is(int, n)
            check_type_is(tuple, idc7rho)
            check_type_is(list, x_settingss)
    except KeyboardInterrupt as exc:
        raise KeyboardInterrupt((sz, sz7rho, sz7ECM, sz7both, sz7trial_division_only), exc)
    return (sz, sz7rho, sz7ECM, sz7both, sz7trial_division_only)

__all__
from seed.math.factor_pint.factor_pint__le_pow2_81 import factor_pint__le_pow2_81_, factor_pint__le_pow2_81__7rho_, factor_pint__le_pow2_81__7ECM_, factor_pint__le_pow2_81__7ECM_7rho_first_
#def factor_pint__le_pow2_81_(n, /, *, using_ECM:bool, **kwds):
#def factor_pint__le_pow2_81__7rho_(n, /, *, partial_ok=False, with_idc=False, max4prime7trial_division=default__max4prime7trial_division, max4num_steps7rho=default__max4num_steps7rho, even_exp=2, addend=1, u0_or_scale=1, u0_be_floor_sqrt_scale_modulus=False, may_empty_saver7immutable=None):
#def factor_pint__le_pow2_81__7ECM_(n, /, *, partial_ok=False, with_settingss=False, max4prime7trial_division=default__max4prime7trial_division, max4num_trials7ECM=default__max4num_trials7ECM, max4num_trials7ECM7part=default__max4num_trials7ECM7part, _n2settings4EPC={}, inversionless=True, _verbose=False, using_rho_first=default__using_rho_first):
#def factor_pint__le_pow2_81__7ECM_7rho_first_(n, /, *, partial_ok=False, with_settingss=False, max4prime7trial_division=default__max4prime7trial_division, max4num_trials7ECM=default__max4num_trials7ECM, max4num_trials7ECM7part=default__max4num_trials7ECM7part, _n2settings4EPC={}, inversionless=True, _verbose=False, with_idc=False, max4num_steps7rho=None):
from seed.math.factor_pint.factor_pint__le_pow2_81 import *
