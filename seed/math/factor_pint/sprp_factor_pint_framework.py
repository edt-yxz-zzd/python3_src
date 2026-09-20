#__all__:goto
r'''[[[
e ../../python3_src/seed/math/factor_pint/sprp_factor_pint_framework.py

seed.math.factor_pint.sprp_factor_pint_framework
py -m nn_ns.app.debug_cmd   seed.math.factor_pint.sprp_factor_pint_framework -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.factor_pint.sprp_factor_pint_framework:__doc__ -ht # -ff -df
#######

[[
come_from:
view ../../python3_src/seed/algo/rho_method.py
    #view ../../python3_src/seed/math/sprp_factor_pint__via_rho_method_.py
]]


'#'; __doc__ = r'#'
>>> from seed.helper.stable_repr import stable_repr, stable_repr_print
>>> stable_print = lambda x, /:stable_repr_print(None, x)

>>> n7unfactored_part = 65 * 77 * 19*23
>>> n = 2**3 * 3**2 * n7unfactored_part
>>> n2factor_tree = {n7unfactored_part:{65:{5:{}}, 77:{11:{}}}}

>>> stable_print(_Framework4sprp_factor_pint__7testing(4, n2factor_tree, verbose=False).sprp_factor_pint_(n, 3))
({2: 3, 3: 2}, {5: 1, 7: 1, 11: 1, 13: 1}, {437: 1}, {})
>>> stable_print(_Framework4sprp_factor_pint__7testing(3, n2factor_tree, verbose=False).sprp_factor_pint_(n, 3))
({2: 3, 3: 2}, {7: 1, 11: 1}, {437: 1}, {65: 1})
>>> stable_print(_Framework4sprp_factor_pint__7testing(2, n2factor_tree, verbose=False).sprp_factor_pint_(n, 3))
({2: 3, 3: 2}, {}, {437: 1}, {65: 1, 77: 1})
>>> stable_print(_Framework4sprp_factor_pint__7testing(1, n2factor_tree, verbose=False).sprp_factor_pint_(n, 3))
({2: 3, 3: 2}, {}, {}, {65: 1, 77: 1, 437: 1})
>>> stable_print(_Framework4sprp_factor_pint__7testing(0, n2factor_tree, verbose=False).sprp_factor_pint_(n, 3))
({2: 3, 3: 2}, {}, {}, {2187185: 1})













py_adhoc_call   seed.math.factor_pint.sprp_factor_pint_framework   @f
]]]'''#'''
__all__ = r'''
IFramework4sprp_factor_pint
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.check import check_type_is, check_int_ge
    from seed.types.SinglyLinkedList import mk_rglnkls_, oo_push_, oo_pop_, top6_, list7up_

    from seed.math.semi_factor_pint_via_trial_division import semi_factor_pint_via_trial_division#as _semi_factor_pint_via_trial_division_
    from seed.math.merge_coprimess_into_smaller_coprimes import merge_coprimess_into_smaller_coprimes#as _merge_coprimess_into_smaller_coprimes_
    from seed.math.factor_pint.perfect_power.detect_perfect_power import factor_pint_as_perfect_power_#as _factor_pint_as_perfect_power_
    from seed.math.primality_test.strong_probable_prime import detect_strong_probable_prime__not_waste_too_much_time_#as _is_SPRP_
    from seed.math.factor_pint_by_trial_division_ import factor_pint_by_trial_division_ex_ # _preprocess7trial_division_



#.#################################
___end_mark_of_excluded_global_names__0___ = ...


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
    #
    st - (state/statistics&inner_args&inner_kwds) for whole factorazation
    #
    raw_output - (success_part, failure_part, todo_part)/(sprp2exp, non_sprp2exp, non_sprp2exp4todo)/({int:int},{int:int},{int:int})
    #
    some_proper_factors - [factor{n7part}]{neednot_complete,neednot_coprime}
        # eg. [some_proper_factors := tmay_proper_factor~imay_proper_factor@seed.algo.rho_method.try_factor1_pint__via_rho_method_]
    #

print_methods7py    seed.math.factor_pint.sprp_factor_pint_framework   IFramework4sprp_factor_pint

new_abstract_methods:
    `_core_factor_algo_
    `_format_output_
    `_mk_state7root_
    `_mk_state7enter_
    `_mk_state7exit_
    `_stop_

new_concrete_methods:
    _is_SPRP_
    _factor_pint_as_perfect_power_
    _merge_coprimess_into_smaller_coprimes_
    _semi_factor_pint_via_trial_division_
    _preprocess7trial_division_
    sprp_factor_pint_

    #]]]'''#'''
    __slots__ = ()

    @abstractmethod
    def _core_factor_algo_(sf, st, n7part, /):
        'st -> n7part/uint{>=2} -> (st, some_proper_factors/[factor{n7part}]{neednot_complete,neednot_coprime}) # eg. [some_proper_factors := tmay_proper_factor~imay_proper_factor@seed.algo.rho_method.try_factor1_pint__via_rho_method_]'



    @abstractmethod
    def _format_output_(sf, n, max4prime7trial_division, p2e7trial_division, n7unfactored_part, st, raw_output, /):
        'n/uint{>=1} -> max4prime7trial_division -> p2e7trial_division/{p:e} -> n7unfactored_part -> st -> raw_output/(sprp2exp, non_sprp2exp, non_sprp2exp4todo) -> output'

    @abstractmethod
    def _mk_state7root_(sf, n, ns, max4prime7trial_division, p2e7trial_division, n7unfactored_part, /, *args7init, **kwds7init):
        'n -> ns/rglnkls{==[n]} -> max4prime7trial_division -> p2e7trial_division -> n7unfactored_part-> (*args7init) -> (**kwds7init) -> (st, args7common, kwds7common)'
    @abstractmethod
    def _mk_state7enter_(sf, ns, st7parent, /, *args7common, **kwds7common):
        'ns/rglnkls{non_sprp/uint{>=3}{%2==1}}{descend}{len>2}{last==n7part} -> st7parent/st{ns[:-1]} -> (*args7common) -> (**kwds7common) -> st{ns}'
    @abstractmethod
    def _mk_state7exit_(sf, ns, st7parent, st, /, *args7common, **kwds7common):
        'ns/rglnkls{non_sprp/uint{>=3}{%2==1}}{descend}{len>2}{last==n7part} -> st7parent/st{ns[:-1]} -> st{ns} -> (*args7common) -> (**kwds7common) -> st7parent/st{ns[:-1]}'

    @abstractmethod
    def _stop_(sf, ns, st, /):
        'ns -> st -> whether_stop/bool # eg:limited by max4num_steps'


    #@abstractmethod
    def _is_SPRP_(sf, pint, /):
        '(pint -> bool)'
        return detect_strong_probable_prime__not_waste_too_much_time_(pint)
    #@abstractmethod
    def _factor_pint_as_perfect_power_(sf, pint, /):
        '(pint -> (base/pint, exp/pint))'
        return factor_pint_as_perfect_power_(pint)
    #@abstractmethod
    def _merge_coprimess_into_smaller_coprimes_(sf, coprimess, /):
        '([coprimes/[pint]]{intra:maybe noncoprime} -> coprimes/[pint])'
        return merge_coprimess_into_smaller_coprimes(coprimess)
    #@abstractmethod
    def _semi_factor_pint_via_trial_division_(sf, candidate_factors, pint, /):
        '([factor7candidate/pint] -> target/pint -> ({factor/pint:exp/pint}, unfactored_part/pint))'
        return semi_factor_pint_via_trial_division(candidate_factors, pint)

    def _preprocess7trial_division_(sf, n, max4prime7trial_division, /):
        'n/uint{>=1} -> max4prime7trial_division/uint{>=2} -> (p2e7trial_division, n7unfactored_part)'
        (p2e7trial_division, n7unfactored_part, may_next_prime_factor) = factor_pint_by_trial_division_ex_(n, may_upperbound4prime_factor=1+max4prime7trial_division)
        return (p2e7trial_division, n7unfactored_part)


    def sprp_factor_pint_(sf, n, max4prime7trial_division, /, *args7init, **kwds7init):
        'n/uint{>=1} -> max4prime7trial_division/uint{>=2} -> (*args7init) -> (**kwds7init) -> output'
        check_int_ge(1, n)
        check_int_ge(2, max4prime7trial_division)
        # [n >= 1]
        # [max4prime7trial_division >= 1]
        (p2e7trial_division, n7unfactored_part) = sf._preprocess7trial_division_(n, max4prime7trial_division)
        assert n7unfactored_part >= 1
        ns = mk_rglnkls_([n])
        (st, args7common, kwds7common) = sf._mk_state7root_(n, ns, max4prime7trial_division, p2e7trial_division, n7unfactored_part, *args7init, **kwds7init)
        if n7unfactored_part == 1:
            raw_output = ({}, {}, {})
            st
        else:
            # [n7unfactored_part >= 2]
            assert n7unfactored_part >= 2
            (st, raw_output) = _raw_sprp_factor_pint_(sf, n, ns, n7unfactored_part, st, args7common, kwds7common)
        st, raw_output
        assert len(raw_output) == 3
            # (sprp2exp, non_sprp2exp, non_sprp2exp4todo)
        output = sf._format_output_(n, max4prime7trial_division, p2e7trial_division, n7unfactored_part, st, raw_output)
        return output
    #end-def sprp_factor_pint_(sf, n, max4prime7trial_division, /, *args7init, **kwds7init):

#end-class IFramework4sprp_factor_pint(ABC):




def _raw_sprp_factor_pint_(sf, n, ns, n7unfactored_part, st, args7common, kwds7common, /):
    '-> (st, raw_output)'
    #n7unfactored_part = top6_(ns)
    assert n7unfactored_part >= 2
    # [n7unfactored_part >= 2]

    _is_SPRP_ = sf._is_SPRP_
    _factor_pint_as_perfect_power_ = sf._factor_pint_as_perfect_power_
    _merge_coprimess_into_smaller_coprimes_ = sf._merge_coprimess_into_smaller_coprimes_
    _semi_factor_pint_via_trial_division_ = sf._semi_factor_pint_via_trial_division_
    _stop_ = sf._stop_
    _core_factor_algo_ = sf._core_factor_algo_
    _mk_state7exit_ = sf._mk_state7exit_
    _mk_state7enter_ = sf._mk_state7enter_



    ls4sprp4succ = []
        # [sprp-factor]{pairwise-coprime}
    ls4non_sprp4todo = []
        # [(non-sprp)-(non-perfect_power)-factor]{pairwise-coprime}
        # a todo_list
    ls4non_sprp4fail = []
    def put_exit_mark_():
        ls4non_sprp4todo.append(0x000000)
    def put(factor):
        # [factor >= 2]
        assert 1 < factor <= n
        if _is_SPRP_(factor):
            ls4sprp4succ.append(factor)
            return
        (factor, exp) = _factor_pint_as_perfect_power_(factor)
        if exp > 1 and _is_SPRP_(factor):
            ls4sprp4succ.append(factor)
            return
        ls4non_sprp4todo.append(factor)
        return
    #end-put

    # [n7unfactored_part >= 2]
    put(n7unfactored_part)
    ns, st # [n7unfactored_part is top6_(ns)]
    assert list7up_(ns) == [n]
    _ls4non_sprp4todo = []
    stk7st7parent = []
    b_stop = False
    while ls4non_sprp4todo:
        match ls4non_sprp4todo.pop():
            # zmay n7part
            case 0x000000:
                # exit_mark # <<== put_exit_mark_()
                # exit
                st7parent = stk7st7parent.pop()
                st = _mk_state7exit_(ns, st7parent, st, *args7common, **kwds7common)
                ns = oo_pop_(ns)
                continue
                ...
            case n7part:
                # [n7part >= 2]
                # [top6_(ns)%n7part == 0]
                assert n7part >= 2
                assert top6_(ns)%n7part == 0
                pass
        #end-match ls4non_sprp4todo.pop():
        n7part
        # [n7part >= 2]
        # [top6_(ns)%n7part == 0]
        if b_stop or (b_stop:=_stop_(ns, st)):
            _ls4non_sprp4todo.append(n7part)
            continue

        n7part
        # [n7part >= 2]
        # [top6_(ns)%n7part == 0]

        # enter
        ns = oo_push_(ns, n7part)
        777;st7parent = st
        777;st = _mk_state7enter_(ns, st7parent, *args7common, **kwds7common)
        777;stk7st7parent.append(st7parent)
        777;put_exit_mark_()
        (st, some_proper_factors) = _core_factor_algo_(st7old:=st, n7part)
        777;some_proper_factors = tuple(some_proper_factors)
        777;ctx = (ns, n7part, stk7st7parent, st7old, st, some_proper_factors)
        for ft in some_proper_factors:
            if not 1 < ft < n7part:raise Exception(n7part, ft, some_proper_factors, ctx)
            if not 0 == n7part %ft:raise Exception(n7part, ft, some_proper_factors, ctx)
        some_proper_factors
        ft_lsls = [[ft] for ft in some_proper_factors]
        if not ft_lsls:
            ls4non_sprp4fail.append(n7part)
            continue
        ft_lsls.append([n7part//ft_lsls[0][0]])
        factors = _merge_coprimess_into_smaller_coprimes_(ft_lsls)
        factors = sorted(factors)
        for _ in map(put, factors):pass
    assert not ls4non_sprp4todo
    assert not _ls4non_sprp4todo or b_stop
    ls4non_sprp4todo = _ls4non_sprp4todo
    assert not ls4non_sprp4todo or b_stop
    assert list7up_(ns) == [n]
    assert not stk7st7parent
    777; st
    777; ls4non_sprp4todo # <<== b_stop
    777; ls4non_sprp4fail # <<== _core_factor_algo_
    777; ls4sprp4succ
    unfactored_part = n7unfactored_part
    (sprp2exp, unfactored_part) = _semi_factor_pint_via_trial_division_(ls4sprp4succ, unfactored_part)
        #success_part
    (non_sprp2exp, unfactored_part) = _semi_factor_pint_via_trial_division_(ls4non_sprp4fail, unfactored_part)
        #failure_part
    (non_sprp2exp4todo, unfactored_part) = _semi_factor_pint_via_trial_division_(ls4non_sprp4todo, unfactored_part)
        #todo_part
    if not 1==unfactored_part:raise Exception(n, n7unfactored_part, sprp2exp, non_sprp2exp, non_sprp2exp4todo, unfactored_part, st)
    raw_output = (sprp2exp, non_sprp2exp, non_sprp2exp4todo)
    return (st, raw_output)
#end-def _raw_sprp_factor_pint_(sf, n, ns, st, args7common, kwds7common, /):


class _Framework4sprp_factor_pint__7testing(IFramework4sprp_factor_pint):
    ___no_slots_ok___ = True
    def __init__(sf, max4num_steps, n2factor_tree, /, *, verbose):
        sf.max4num_steps = max4num_steps
        sf.n2factor_tree = n2factor_tree
        sf.verbose = verbose

    @override
    def _core_factor_algo_(sf, st, n7part, /):
        (cnt, ns, n2factor_tree) = st
        some_proper_factors = tuple(sorted(n2factor_tree))
        st = (1+cnt, ns, n2factor_tree)
        if sf.verbose:print('_core_factor_algo_:', st)
        return (st, some_proper_factors)



    @override
    def _mk_state7root_(sf, n, ns, max4prime7trial_division, p2e7trial_division, n7unfactored_part, /, *args7init, **kwds7init):
        args7common = args7init
        kwds7common = kwds7init
        #n7unfactored_part = top6_(ns)
        #st = (cnt:=0, ns, sf.n2factor_tree.get(n7unfactored_part, {}))
        st = (cnt:=0, ns, sf.n2factor_tree)
        if sf.verbose:print('_mk_state7root_:', st)
        return (st, args7common, kwds7common)
    @override
    def _mk_state7enter_(sf, ns, st7parent, /, *args7common, **kwds7common):
        (cnt, ns7parent, n2factor_tree) = st7parent
        assert oo_pop_(ns) is ns7parent
        n7part = top6_(ns)
        st = (cnt, ns, n2factor_tree.get(n7part, {}))
        if sf.verbose:print('_mk_state7enter_:', (st7parent, st))
        return st

    @override
    def _mk_state7exit_(sf, ns, st7parent, st, /, *args7common, **kwds7common):
        (cnt7parent, ns7parent, n2factor_tree7parent) = st7parent
        (cnt7child, ns7same, n2factor_tree) = st
        assert ns7same is ns
        assert oo_pop_(ns) is ns7parent
        st7parent7new = (cnt7child, ns7parent, n2factor_tree7parent)
        if sf.verbose:print('_mk_state7exit_:', (st7parent, st, st7parent7new))
        return st7parent7new

    @override
    def _stop_(sf, ns, st, /):
        return st[0] >= sf.max4num_steps

    @override
    def _format_output_(sf, n, max4prime7trial_division, p2e7trial_division, n7unfactored_part, st, raw_output, /):
        (sprp2exp, non_sprp2exp, non_sprp2exp4todo) = raw_output
        return (p2e7trial_division, sprp2exp, non_sprp2exp, non_sprp2exp4todo)

#end-class _Framework4sprp_factor_pint__7testing(IFramework4sprp_factor_pint):











__all__
from seed.math.factor_pint.sprp_factor_pint_framework import IFramework4sprp_factor_pint
#   def sprp_factor_pint_(sf, n, max4prime7trial_division, /, *args7init, **kwds7init):
from seed.math.factor_pint.sprp_factor_pint_framework import *
