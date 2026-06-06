
e ../../python3_src/seed/math/factor_pint/README.txt
find ../../python3_src/seed/math/ -name '*factor*.py'


[[
view ../../python3_src/seed/math/factor_pint/perfect_power/detect_perfect_power.py
from seed.math.factor_pint.perfect_power.detect_perfect_power import detect_perfect_power_, is_perfect_power_, factor_pint_as_perfect_power_

]]
[[
view ../../python3_src/seed/algo/rho_method.py
from seed.algo.rho_method import try_factor1_pint__via_rho_method_, sprp_factor_pint__via_rho_method_

def try_factor1_pint__via_rho_method_(n, f_=None, /, *, to_detect_SPRP=False, seeds=None, max_num_seeds=None, max_num_tries_per_seed=None, to_output_statistics=False, _verbose=False):
    'n/int{>=1}/[not is_prime(n)] -> may (n -> (*params) -> uint%n -> uint%n) -> (kw:seeds/may (Iter params_x0/(*params, x0))) -> imay proper_factor if not to_output_statistics else (imay_proper_factor, jseed, total_steps) # [SPRP == strong probable-prime]'

def sprp_factor_pint__via_rho_method_(n, f_=None, /, *, seeds=None, max_num_seeds=None, max_num_tries_per_seed=None, to_output_statistics=False):
    'n/int{>=1} -> may (n -> (*params) -> uint%n -> uint%n) -> (kw:seeds/may (Iter params_x0/(*params, x0))) -> (success_part, failure_part)/(sprp2exp, non_sprp2exp)/({sprp:exp}, {non_sprp:exp}) if not to_output_statistics else (sprp2exp, non_sprp2exp, total_steps) # [SPRP == strong probable-prime]'

]]
[[
find ../../python3_src/seed/math/ -name '*factor*.py'



view ../../python3_src/seed/math/factor_pint_by_trial_division_.py
view ../../python3_src/seed/math/factor_pint/factor_pint__naive_brute_force.py
view ../../python3_src/seed/math/factor_pint_into_strong_probable_primes_by_quadratic_sieve_.py
view ../../python3_src/seed/math/factor_pint/sprp_factor_pint_framework.py
  view ../../python3_src/seed/math/sprp_factor_pint__via_rho_method_.py
  view ../../python3_src/seed/math/factor_pint/sprp_factor_pint__via_Lehman_method__O_cube_root.py
    view ../../python3_src/seed/math/factor_pint/factor_pint__near_sqrtN.py

def try_factor_pint__near_sqrtNmulCmulZpow_(N, k=1, /, *, force6sprp=False, with_position6ok=False, verbose=False, ground_scale=1):
    'N/uint -> may (n0, n1) # via factor_pint__near_sqrtN_(N*c*2**ez) where [c:<-[1..]][ez:<-[0..=floor_log2(n)**2]]'
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__near_sqrtN   @try_factor_pint__near_sqrtNmulCmulZpow_ +with_position6ok   ='(-1+2**67)' =1  --ground_scale=3933



auxiliary:
  view ../../python3_src/seed/math/max_power_of_base_as_factor_of_.py
  view ../../python3_src/seed/math/semi_factor_pint_via_trial_division.py
  view ../../python3_src/seed/math/factor_pint/factor_pint5or_emay_prime_factors4target_pint_.py








deprecated:
  view ../../python3_src/seed/math/factor_pint_as_perfect_power_.py
  view ../../python3_src/seed/math/_data4factor_pint_as_perfect_power_.py
  view ../../python3_src/seed/math/factor_pint_as_perfect_power__7prepare.py










irrelevant:
  view ../../python3_src/seed/math/is_prime__via_complete_factorization_Nmm_.py
  view ../../python3_src/seed/math/is_complete_factorization_of__ft2e_.py
  view ../../python3_src/seed/math/is_kth_primitive_root_mod_N__via_complete_factorization_k_.py
  view ../../python3_src/seed/math/find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_.py
  view ../../python3_src/seed/math/all_factors_of_.py
  view ../../python3_src/seed/math/list_all_factors5factorization_.py
]]

