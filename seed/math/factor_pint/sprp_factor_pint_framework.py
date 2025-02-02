#__all__:goto
r'''[[[
e ../../python3_src/seed/math/factor_pint/sprp_factor_pint_framework.py

seed.math.factor_pint.sprp_factor_pint_framework
py -m nn_ns.app.debug_cmd   seed.math.factor_pint.sprp_factor_pint_framework -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.factor_pint.sprp_factor_pint_framework:__doc__ -ht # -ff -df

[[
源起:
view ../../python3_src/seed/algo/rho_method.py
    #view ../../python3_src/seed/math/sprp_factor_pint__via_rho_method_.py
]]

py_adhoc_call   seed.math.factor_pint.sprp_factor_pint_framework   @f
from seed.math.factor_pint.sprp_factor_pint_framework import *
]]]'''#'''
__all__ = r'''
IFramework4sprp_factor_pint
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#from itertools import islice
from seed.tiny_.check import check_type_is, check_int_ge
from seed.helper.ifNone import ifNonef

from seed.abc.abc__ver1 import abstractmethod, override, ABC
#from seed.helper.repr_input import repr_helper
___end_mark_of_excluded_global_names__0___ = ...

#.class __(ABC):
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError

def _lazy_imports():
    'lazy_import'
    global _lazy_imports
    from seed.math.semi_factor_pint_via_trial_division import semi_factor_pint_via_trial_division
    from seed.math.merge_coprimess_into_smaller_coprimes import merge_coprimess_into_smaller_coprimes
    from seed.math.factor_pint_as_pefect_power_ import factor_pint_as_pefect_power_
    from seed.math.prime_gens import detect_strong_pseudoprime__not_waste_too_much_time_ as _is_SPRP_
    _4lazy_imports = (_is_SPRP_, factor_pint_as_pefect_power_, merge_coprimess_into_smaller_coprimes, semi_factor_pint_via_trial_division)
        #utilities
    def f():
        return _4lazy_imports
    if f is _lazy_imports:raise 000
    _lazy_imports = f
    if not f is _lazy_imports:raise 000
    return _lazy_imports()
#.def _x_is_SPRP_(n, /):
#.    'used in doctest'
#.    return _is_SPRP_(n)
#.def _is_SPRP_(n, /):
#.    "lazy_import"
#.    global _is_SPRP_
#.    from seed.math.prime_gens import detect_strong_pseudoprime__not_waste_too_much_time_ as f
#.    if f is _is_SPRP_:raise 000
#.    _is_SPRP_ = f
#.    if not f is _is_SPRP_:raise 000
#.    return _is_SPRP_(n)

class IFramework4sprp_factor_pint(ABC):
    r'''[[[
    IFramework4sprp_factor_pint - interface of framework for sprp_factor_pint_
    #
    sprp_factor_pint_ - factor positive integer down into strong probable-primes
    #
    [SPRP == strong probable-prime]
    #
    pint - positive integer
    #
    utilities - (_is_SPRP_, factor_pint_as_pefect_power_, merge_coprimess_into_smaller_coprimes, semi_factor_pint_via_trial_division)
    #
    st - (state/statistics&inner_args&inner_kwds) for whole factorazation
    #
    raw_output - (success_part, failure_part, todo_part)/(sprp2exp, non_sprp2exp, non_sprp2exp4todo)/({int:int},{int:int},{int:int})
    #
    some_proper_factors - [factor{n4part}]{neednot_complete,neednot_coprime})
        # eg. [some_proper_factors := tmay_proper_factor~imay_proper_factor@seed.algo.rho_method.try_factor1_pint__via_rho_method_]
    #

    #]]]'''#'''
    __slots__ = ()

    @abstractmethod
    def _core_factor_algo_(sf, st, n4part, /):
        'st -> n4part/uint{>=2} -> (st, some_proper_factors/[factor{n4part}]{neednot_complete,neednot_coprime}) # eg. [some_proper_factors := tmay_proper_factor~imay_proper_factor@seed.algo.rho_method.try_factor1_pint__via_rho_method_]'
    @abstractmethod
    def _prepare4whole_(sf, n4whole, /, *args4whole, **kwds4whole):
        'n4whole/uint{>=1} -> (*args4whole) -> (**kwds4whole) -> (st, may utilities)'
    @abstractmethod
    def _stop4whole_(sf, n4whole, st, /):
        'n4whole/uint{>=1} -> st -> whether_stop/bool'
    @abstractmethod
    def _format_output4whole_(sf, n4whole, st, raw_output, /):
        'n4whole/uint{>=1} -> st -> raw_output -> output4whole'
    def sprp_factor_pint_(sf, n4whole, /, *args4whole, **kwds4whole):
        'n4whole/uint{>=1} -> (*args4whole) -> (**kwds4whole) -> output4whole'
        check_int_ge(1, n4whole)
        # [n4whole >= 1]
        (st, may_utilities) = sf._prepare4whole_(n4whole, *args4whole, **kwds4whole)
        if n4whole == 1:
            raw_output = ({}, {}, {})
            st
        else:
            # [n4whole >= 2]
            utilities = ifNonef(may_utilities, _lazy_imports)
            assert len(utilities) == 4
                # (_is_SPRP_, factor_pint_as_pefect_power_, merge_coprimess_into_smaller_coprimes, semi_factor_pint_via_trial_division)
            (st, raw_output) = _raw_sprp_factor_pint_(sf, n4whole, st, utilities, *args4whole, **kwds4whole)
        st, raw_output
        assert len(raw_output) == 3
            # (sprp2exp, non_sprp2exp, non_sprp2exp4todo)
        output4whole = sf._format_output4whole_(n4whole, st, raw_output)
        return output4whole
    #end-def sprp_factor_pint_(sf, n4whole, /, *args4whole, **kwds4whole):

    ######################
    #deprecate:
    ######################
    #.@abstractmethod
    #.def _core_factor_algo_(sf, st, n4part, /, *args4core, **kwds4core):
    #.    'st -> n4part/uint{>=2} -> (*args4core) -> (**kwds4core) -> (st, some_proper_factors/[factor{n4part}]) # eg. [some_proper_factors := tmay_proper_factor]@seed.algo.rho_method.try_factor1_pint__via_rho_method_'
    #.@abstractmethod
    #.def _prepare4whole_(sf, n4whole, /, *args4whole, **kwds4whole):
    #.    'n4whole/uint{>=1} -> (*args4whole) -> (**kwds4whole) -> (st, (args4stop, kwds4stop), (args4fmt, kwds4fmt), (args4core, kwds4core))'
    #.@abstractmethod
    #.def _stop4whole_(sf, n4whole, /, *args4stop, **kwds4stop):
    #.    'n4whole/uint{>=1} -> st -> (*args4stop) -> (**kwds4stop) -> bool'
    #.@abstractmethod
    #.def _format_output4whole_(sf, n4whole, st, /, *args4fmt, **kwds4fmt):
    #.    'n4whole/uint{>=1} -> st -> (*args4fmt) -> (**kwds4fmt) -> raw_output -> output4whole'
    ######################
#end-class IFramework4sprp_factor_pint(ABC):





def _raw_sprp_factor_pint_(sf, n4whole, st, utilities, /, *args4whole, **kwds4whole):
    'n4whole/uint{>=2} -> st -> utilities -> (*args4whole) -> (**kwds4whole) -> (st, raw_output)'
    # [n4whole >= 2]
    (_is_SPRP_, factor_pint_as_pefect_power_, merge_coprimess_into_smaller_coprimes, semi_factor_pint_via_trial_division) = utilities

    ls4sprp4succ = []
        # [sprp-factor]{pairwise-coprime}
    ls4non_sprp4todo = []
        # [(non-sprp)-(non-pefect_power)-factor]{pairwise-coprime}
        # a todo_list
    ls4non_sprp4fail = []
    def put(factor):
        # [factor >= 2]
        if _is_SPRP_(factor):
            ls4sprp4succ.append(factor)
            return
        (factor, exp) = factor_pint_as_pefect_power_(factor)
        if exp > 1 and _is_SPRP_(factor):
            ls4sprp4succ.append(factor)
            return
        ls4non_sprp4todo.append(factor)
        return
    #end-put

    # [n4whole >= 2]
    put(n4whole)
    b_stop = False
    while ls4non_sprp4todo and not (b_stop:=sf._stop4whole_(n4whole, st)):
        n4part = ls4non_sprp4todo.pop()
        # [n4part >= 2]
        (st, some_proper_factors) = sf._core_factor_algo_(st, n4part)
        ft_lsls = [[ft] for ft in some_proper_factors]
        if not ft_lsls:
            ls4non_sprp4fail.append(n4part)
            continue
        ft_lsls.append([n4part//ft_lsls[0][0]])
        factors = merge_coprimess_into_smaller_coprimes(ft_lsls)
        for _ in map(put, factors):pass
    assert not ls4non_sprp4todo or b_stop
    777; st
    777; ls4non_sprp4todo
    777; ls4non_sprp4fail
    777; ls4sprp4succ
    unfactored_part = n4whole
    (sprp2exp, unfactored_part) = semi_factor_pint_via_trial_division(ls4sprp4succ, unfactored_part)
        #success_part
    (non_sprp2exp, unfactored_part) = semi_factor_pint_via_trial_division(ls4non_sprp4fail, unfactored_part)
        #failure_part
    (non_sprp2exp4todo, unfactored_part) = semi_factor_pint_via_trial_division(ls4non_sprp4todo, unfactored_part)
        #todo_part
    if not unfactored_part==1:raise Exception(n4whole, sprp2exp, non_sprp2exp, unfactored_part, st, utilities)
    raw_output = (sprp2exp, non_sprp2exp, non_sprp2exp4todo)
    return (st, raw_output)
#end-def _raw_sprp_factor_pint_(sf, n4whole, st, utilities, /, *args4whole, **kwds4whole):



__all__
from seed.math.factor_pint.sprp_factor_pint_framework import *
