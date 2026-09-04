#__all__:goto
#rho_vs_ECM:goto
r'''[[[
e ../../python3_src/seed/math/factor_pint/factor_pint__le_pow2_81.py

seed.math.factor_pint.factor_pint__le_pow2_81
py -m nn_ns.app.debug_cmd   seed.math.factor_pint.factor_pint__le_pow2_81 -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.factor_pint.factor_pint__le_pow2_81:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
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
>>> factor_pint__le_pow2_81_(-1+2**81)
{73: 1, 2593: 1, 7: 1, 262657: 1, 71119: 1, 97685839: 1}
>>> factor_pint__le_pow2_81_(549755813911*1099511627791, known_factor4Pmm=2*47846459)
{549755813911: 1, 1099511627791: 1}



++kw:using_ECM
>>> factor_pint__le_pow2_81_(549755813911*1099511627791, using_ECM=True) == {549755813911: 1, 1099511627791: 1}
True








#rho_vs_ECM:goto
[[
py_adhoc_call   seed.math.factor_pint.factor_pint__le_pow2_81   @factor_pint__le_pow2_81_ =456777897
    {401: 1, 379699: 1, 3: 1}

py_adhoc_call   seed.math.factor_pint.factor_pint__le_pow2_81   @factor_pint__le_pow2_81_ =-1+549755813911
    {3: 1, 5: 1, 383: 1, 47846459: 1, 2: 1}
]]


]]]'''#'''
__all__ = r'''
factor_pint__le_pow2_81_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.abc.abc__ver1 import abstractmethod, override, ABC
from seed.math.factor_pint.sprp_factor_pint_framework import IFramework4sprp_factor_pint, IFramework4sprp_factor_pint__7mixins7utilities
#.#################################
from seed.helper.lazy_import__func import force_lazy_imported_func_
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    #from random import Random
        # .seed(self, a=None, version=2)
        # .getstate(self) # [625 == len(st4Random[1])] #too huge
        # .setstate(self, state)
        # .randrange(self, start, stop=None, step=1)

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

    from seed.math.factor_pint.factor_pint__elliptic_curve_method import try_factor_pint__elliptic_curve_method_
    #def try_factor_pint__elliptic_curve_method_(n, Bs_or_kss=None, ks5n_and_B_or_ks_=None, /, *, random_uint_mod_=None, with_ctx=False, result6fail=None):
    #   'n/uint{>=1} -> Iter (B/uint{>=2}|ks/(Iter k/uint{>=2})) -> may (n -> (B|ks) -> ks) -> may non_trivial_factor{n} # [ks are multiplier => II(ks)*pt] # [B is smooth bound => ks:=chains(repeat(p,floor_log_(p,B)) for p in primes_lt(1+B))] # [[p::prime][n%p==0][1==gcd(n,[1..<p])] -> [best:B1:=exp((1/sqrt2+o(1))*sqrt(ln(p)*lnln(p)))]]'

#.#################################
___end_mark_of_excluded_global_names__0___ = ...

r'''[[[

[[
rho_vs_ECM:here
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

__all__
from seed.math.factor_pint.factor_pint__le_pow2_81 import factor_pint__le_pow2_81_
from seed.math.factor_pint.factor_pint__le_pow2_81 import *
