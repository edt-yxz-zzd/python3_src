#__all__:goto
#TODO:goto
r'''[[[
e ../../python3_src/seed/algo/rho_method__7iter7batch.py




seed.algo.rho_method__7iter7batch
py -m nn_ns.app.debug_cmd   seed.algo.rho_method__7iter7batch -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.algo.rho_method__7iter7batch:__doc__ -ht # -ff -df
#######

[[
come_from:
view ../../python3_src/seed/math/factor_pint/factor_pint__le_pow2_81.py
]]
[[
#halfDONE:TODO:++HistorySaver
view ../../python3_src/seed/types/HistorySaver.py
view ../../python3_src/seed/types/Reproduceable.py
SparseHistorySaver7immutable(max_size7physical, imay_max_size7apparent)
SparseHistorySaver7immutable(settings, data)
    [settings == (max_size7physical, imay_max_size7apparent)]
    [data == (may_head, history_lnkls, size7physical, size7apparent, curr_size4step, remain_size4last_step)]

st{batch} contains SparseHistorySaver7immutable


rp_j6i = (merge_st_pt_, is_bad_st_, st2eresult_, pt2next_pt_, i, xi, j, xj, st_i_j, )
history2rank_:
    #st2eresult_->eresult
        Left => -1
        Right => 0
    #is_bad_st_
        bad_state => +1
    @SparseHistorySaver7immutable.forward_search_key_points_()
mstep7stated_:
    jpp = 1+j
    x_jpp := pt2next_pt_(xj)
    st_i_jpp := merge_st_pt_(st_i_j, x_jpp)
    @IStatedStepOps__7endless__7oresult6both_states
        @IStatedStepOps__7endless__7prev_oresult6curr_state
            @IStatedStepOps__7endless__7prev_oresult_is_curr_state
                @StatedStepOps__7bare_iterate7exclude_initial_state

@20260909:
    xxx:raw_iter_rho_method7batch__5xxx__7resume_
    ++raw_iter_rho_method7batch__5reproduceable__7resume_
    ++kw:mode@raw_iter_rho_method7batch__7next__7resume_

]]


'#'; __doc__ = r'#'
>>> Ops4RhoMethod__7factor_pint__7next(3, 1, 2)
Ops4RhoMethod__7factor_pint__7next(3, 1, 2)


? nextprime(2^20)
1048583
? nextprime(2^21)
2097169
? factorint(1048583*2097169)
[1048583,1;2097169,1]

so many bad_state => required:[st{batch} contains SparseHistorySaver7immutable] to finer search inner batch
    bad_state comes from both rho{%p}, rho{%q} hit loop in current batch

>>> _internal_kwds4xxx = dict(_turnoff_HistorySaver=True)
>>> kwds = dict(mode='iterable', may_args6mode=None)
>>> try_factor1_pint__7rho_method7batch__5seed_(1048583*2097169, 11, 1, more=True, **kwds)
(10, True, Either(False, 'bad_state'), (1120516837464, 0), (1023, 1120516837464), (1120, 973647898056))
>>> try_factor1_pint__7rho_method7batch__5seed_(1048583*2097169, 11, 2, more=True, **kwds)
(10, True, Either(False, 'bad_state'), (1987185451198, 0), (1023, 1987185451198), (1120, 1530424140167))
>>> try_factor1_pint__7rho_method7batch__5seed_(1048583*2097169, 11, 4, more=True, **kwds)
(10, True, Either(False, 'bad_state'), (1203515666247, 0), (1023, 1203515666247), (1162, 1509203825322))
>>> try_factor1_pint__7rho_method7batch__5seed_(1048583*2097169, 11, 5, **kwds)
-1
>>> try_factor1_pint__7rho_method7batch__7resume_(1048583*2097169, 11, 10, 1203515666247, 1162, 1509203825322, (1203515666247, 0), more=True, **kwds)
(10, True, Either(False, 'bad_state'), (1203515666247, 0), (1023, 1203515666247), (1162, 1509203825322))



>>> try_factor1_pint__7rho_method7batch__5seed_(1048583*2097169, 9, 3, more=True, **kwds)
(8, True, Either(True, 1048583), (1320160886868, 1611055504196), (255, 1320160886868), (511, 1211621383699))

>>> try_factor1_pint__7rho_method7batch__5seed_(1048583*2097169, 8, 3, more=True, **kwds)
(7, False, Either(False, 1), (1194865290398, 165238984380), (127, 1194865290398), (255, 1320160886868))
>>> try_factor1_pint__7rho_method7batch__7resume_(1048583*2097169, 9, 7, 1194865290398, 255, 1320160886868, (1194865290398, 165238984380), more=True, **kwds)
(8, True, Either(True, 1048583), (1320160886868, 1611055504196), (255, 1320160886868), (511, 1211621383699))

>>> try_factor1_pint__7rho_method7batch__5seed_(1048583*2097169, 9, 3, more=True, may_max_num_steps=500, **kwds)
(8, True, Either(True, 1048583), (1320160886868, 2171419307979), (255, 1320160886868), (499, 1412690831784))
>>> try_factor1_pint__7rho_method7batch__7resume_(1048583*2097169, 9, 8, 1320160886868, 499, 1412690831784, (1320160886868, 2171419307979), more=True, **kwds)
(8, True, Either(True, 1048583), (1320160886868, 1611055504196), (255, 1320160886868), (511, 1211621383699))
>>> try_factor1_pint__7rho_method7batch__7resume_(1048583*2097169, 9, 8, 1320160886868, 499, 1412690831784, (1320160886868, 2171419307979), more=True, may_max_num_steps=500, **kwds)
(8, True, Either(True, 1048583), (1320160886868, 2171419307979), (255, 1320160886868), (499, 1412690831784))
>>> try_factor1_pint__7rho_method7batch__7resume_(1048583*2097169, 9, 8, 1320160886868, 499, 1412690831784, (1320160886868, 2171419307979), more=True, may_max_num_steps=501, **kwds)
(8, True, Either(True, 1048583), (1320160886868, 1167295178596), (255, 1320160886868), (500, 1916251590320))
>>> try_factor1_pint__7rho_method7batch__7resume_(1048583*2097169, 9, 8, 1320160886868, 499, 1412690831784, (1320160886868, 2171419307979), more=True, may_max_num_steps=499, **kwds)
Traceback (most recent call last):
    ...
TypeError: 499


>>> try_factor1_pint__7rho_method7batch__5seed_(1048583*2097169, 10, 3, **kwds)
1048583
>>> try_factor1_pint__7rho_method7batch__5seed_(1048583*2097169, 10, None, **kwds)
2097169





@20260909:
    TODO:test:raw_iter_rho_method7batch__5reproduceable__7resume_
    TODO:test:kw:mode@raw_iter_rho_method7batch__7next__7resume_
    TODO:++kw:mode@all-top-level-method{has:pt2next_pt_}
    TODO:test:raw_iter_rho_method7batch__5reproduceable_
    TODO:test:kw:mode@raw_iter_rho_method7batch__7next_

TODO:5iterable:++kw:imay_cache_size4batch{otherwise loss info inside batch interval}
    DenseHistorySaver
DONE:HistorySaver:++search/fill:kw:non_reproduceable_ok,may_iter_subsequents_

#
#def mk_history_saver_(max_size7dense, max_size7physical, cost_per_detect, imay_detect_period, /):
#
#DenseHistorySaver(max_size7apparent, mark8no_check='!', may_history_array=None, /, *, no_copy=False)
#   [mark8no_check === '!']
#
#SparseHistorySaver(max_size7dense, max_size7physical, imay_max_size7apparent, mark8no_check='!', payload=None, /, *, no_copy=False)
#   recommend:[1 == max_size7physical%2]
#   [payload :: may (history_array, size7apparent, curr_max_size7physical, curr_step, last_step)]
#   [mark8no_check === '!']
#
#SparseHistorySaver7immutable(max_size7physical, imay_max_size7apparent, mark8no_check='!', data=None)
#   [data == (may_head, history_lnkls, size7physical, size7apparent, curr_size4step, remain_size4last_step)]
#   [mark8no_check === '!']
#






















py_adhoc_call   seed.algo.rho_method__7iter7batch   @f
]]]'''#'''
__all__ = r'''
raw_iter_rho_method7batch__7next_
    raw_iter_rho_method7batch__7next__7resume_

    raw_iter_rho_method7batch__5iterable_
        raw_iter_rho_method7batch__5iterable__7resume_

    raw_iter_rho_method7batch__5reproduceable_
        raw_iter_rho_method7batch__5reproduceable__7resume_


try_factor1_pint__7rho_method7batch__5seed_
    try_factor1_pint__7rho_method7batch__7resume_


IOps4RhoMethod
    IOps4RhoMethod__7next
        iter_rho_method7batch__5seed_
        iter_rho_method7batch__7resume_

    iter_rho_method7batch__7next_
    iter_rho_method7batch__7next__7resume_

    iter_rho_method7batch__5iterable_
    iter_rho_method7batch__5iterable__7resume_

    iter_rho_method7batch__5reproduceable_
    iter_rho_method7batch__5reproduceable__7resume_

IOps4RhoMethod
    IOps4RhoMethod__7next
    IOps4RhoMethod__7factor_pint
        IOps4RhoMethod__7factor_pint__7next
            Ops4RhoMethod__7factor_pint__7next
                try_factor1_pint__7rho_method7batch__5seed_
                try_factor1_pint__7rho_method7batch__7resume_




default_args4history_saver7immutable
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.#################################
from seed.helper.lazy_import__func import force_lazy_imported_func_
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.excepts.repack_exception_ import repack_exception_, repack_exception7new_subclass_
    from seed.types.Either import Cased, Either
    from seed.types.Either import mk_Left, mk_Right
    from seed.iters.iterate import iterate
    from seed.tiny_.check import check_type_is, check_type_le, check_int_ge, check_int_ge_lt, check_callable
    from seed.types.attr.class2method_decorator import mk_instance_method_decorator_# mk_class_method_decorator_, mk_static_method_decorator_, MethodDecoratorBase
    #def mk_instance_method_decorator_(klass, /, *, name=''):

    from seed.helper.repr_input import repr_helper

    from itertools import islice
    from math import gcd, isqrt

    from seed.types.Reproduceable import iter_snds4reproduceable_
    from seed.types.Reproduceable import Reproduceable7step_via_ops, StatedStepOps__7bare_iterate7include_initial_state
    from seed.types.HistorySaver import SparseHistorySaver7immutable
    from seed.types.HistorySaver import IHistorySaver7immutable

#.#################################
___end_mark_of_excluded_global_names__0___ = ...

default_args4history_saver7immutable = (2049, -1) #(max_size7physical, imay_max_size7apparent)


class IOps4RhoMethod(ABC):
    #pt2st_, merge_st_pt_, is_bad_st_, st2eresult_
    __slots__ = ()
    @abstractmethod
    def pt2st_(sf, x, /):
        '(x[i] -> st[i,i])'
    @abstractmethod
    def merge_st_pt_(sf, st_i_jmm, xj, /):
        '(st[i,-1+j] -> x[j] -> st[i,j])'
    @abstractmethod
    def is_bad_st_(sf, st, /):
        '(st -> whether_bad_state/bool)'
    @abstractmethod
    def st2eresult_(sf, st, /):
        '(st -> eresult/(Either errmsg oresult))'
    @property
    def basic_ops7iterable(sf, /):
        return (sf.pt2st_, sf.merge_st_pt_, sf.is_bad_st_, sf.st2eresult_)

class IOps4RhoMethod__7next(IOps4RhoMethod):
    #pt2next_pt_#?rho_step_?
    __slots__ = ()
    @abstractmethod
    def pt2next_pt_(sf, x, /):
        '(x[j] -> x[1+j])'

###########################
# [:reason_of_order_of_the_two_decorators{_method_,_method__7next_}]:goto
###########################
_method__7next_ = mk_instance_method_decorator_(IOps4RhoMethod__7next)

@_method__7next_
def iter_rho_method7batch__5seed_(sf, x0, /, *, mode, may_args6mode, pt2next_pt_=None, may_max_num_steps=None):
    'x[0] -> Iter (log2_ipp, whether_stop[i,j]/bool{==is_bad_st_(st[i,j]) or eresult[i,j].is_right}, eresult[i,j], st[i,j], (i, x[i]), (j, x[j])){[i+1==2**log2_ipp][i <= j < 2*(1+i)]}  # stop iff found result or detect bad seed/state'
    if pt2next_pt_ is None:
        pt2next_pt_ = sf.pt2next_pt_
    return sf.iter_rho_method7batch__7next_(pt2next_pt_, x0, mode=mode, may_args6mode=may_args6mode, may_max_num_steps=may_max_num_steps)

@_method__7next_
def iter_rho_method7batch__7resume_(sf, log2_ipp, xi, j, xj, st_i_j, /, *, mode, may_args6mode, pt2next_pt_=None, may_max_num_steps=None):
    'log2_ipp/uint{[i+1==2**log2_ipp]} -> x[i] -> j/uint{>=i==-1+2**log2_ipp}{<2*(1+i)==2**(1+log2_ipp)} -> x[j] -> st[i,j] -> Iter (log2_ipp, whether_stop[i,j]/bool{==is_bad_st_(st[i,j]) or eresult[i,j].is_right}, eresult[i,j], st[i,j], (i, x[i]), (j, x[j])){[i+1==2**log2_ipp][i <= j < 2*(1+i)]}  # stop iff found result or detect bad seed/state'
    if pt2next_pt_ is None:
        pt2next_pt_ = sf.pt2next_pt_
    return sf.iter_rho_method7batch__7next__7resume_(pt2next_pt_, log2_ipp, xi, j, xj, st_i_j, mode=mode, may_args6mode=may_args6mode, may_max_num_steps=may_max_num_steps)
@_method__7next_
@override
def iter_rho_method7batch__5reproduceable_(sf, x0, history_saver7immutable__or__args=default_args4history_saver7immutable, /, *, pt2next_pt_=None, may_max_num_steps=None):
    # override:API changed --> {default&&ok:[pt2next_pt_:=None]}
    return iter_rho_method7batch__5reproduceable_(sf, x0, history_saver7immutable__or__args, pt2next_pt_=pt2next_pt_, may_max_num_steps=may_max_num_steps)
    # !! super():required:__class__
    #.return super(sf).iter_rho_method7batch__5reproduceable_(x0, history_saver7immutable__or__args, pt2next_pt_=pt2next_pt_, may_max_num_steps=may_max_num_steps)
    return raw_iter_rho_method7batch__5reproduceable_(*_mk_basic_ops7reproduceable_(sf, pt2next_pt_), x0, history_saver7immutable__or__args, may_max_num_steps=may_max_num_steps)
@_method__7next_
@override
def iter_rho_method7batch__5reproduceable__7resume_(sf, log2_ipp, j, k, history_saver_i_j_k, /, *, pt2next_pt_=None, may_max_num_steps=None):
    # override:API changed --> {default&&ok:[pt2next_pt_:=None]}
    return iter_rho_method7batch__5reproduceable__7resume_(sf, log2_ipp, j, k, history_saver_i_j_k, pt2next_pt_=pt2next_pt_, may_max_num_steps=may_max_num_steps)
    # !! super():required:__class__
    #.return super(sf).iter_rho_method7batch__5reproduceable__7resume_(log2_ipp, j, k, history_saver_i_j_k, pt2next_pt_=pt2next_pt_, may_max_num_steps=may_max_num_steps)
    return raw_iter_rho_method7batch__5reproduceable__7resume_(*_mk_basic_ops7reproduceable_(sf, pt2next_pt_), log2_ipp, j, k, history_saver_i_j_k, may_max_num_steps=may_max_num_steps)






###########################
###########################
###########################
###########################
# [:reason_of_order_of_the_two_decorators{_method_,_method__7next_}]:here
# _method_ after _method__7next_
#   !! iter_rho_method7batch__5reproduceable_{7next} call global iter_rho_method7batch__5reproduceable_() as super() method
###########################
###########################
###########################
###########################
_method_ = mk_instance_method_decorator_(IOps4RhoMethod)

@_method_
def iter_rho_method7batch__7next_(sf, pt2next_pt_, x0, /, *, mode, may_args6mode, may_max_num_steps=None):
    'pt2next_pt_/(x[j] -> x[1+j]) -> x[0] -> Iter (log2_ipp, whether_stop[i,j]/bool{==is_bad_st_(st[i,j]) or eresult[i,j].is_right}, eresult[i,j], st[i,j], (i, x[i]), (j, x[j])){[i+1==2**log2_ipp][i <= j < 2*(1+i)]}  # stop iff found result or detect bad seed/state'
    return raw_iter_rho_method7batch__7next_(*sf.basic_ops7iterable, pt2next_pt_, x0, mode=mode, may_args6mode=may_args6mode, may_max_num_steps=may_max_num_steps)

@_method_
def iter_rho_method7batch__7next__7resume_(sf, pt2next_pt_, log2_ipp, xi, j, xj, st_i_j, /, *, mode, may_args6mode, may_max_num_steps=None):
    'pt2next_pt_/(x[j] -> x[1+j]) -> log2_ipp/uint{[i+1==2**log2_ipp]} -> x[i] -> j/uint{>=i==-1+2**log2_ipp}{<2*(1+i)==2**(1+log2_ipp)} -> x[j] -> st[i,j] -> Iter (log2_ipp, whether_stop[i,j]/bool{==is_bad_st_(st[i,j]) or eresult[i,j].is_right}, eresult[i,j], st[i,j], (i, x[i]), (j, x[j])){[i+1==2**log2_ipp][i <= j < 2*(1+i)]}  # stop iff found result or detect bad seed/state'
    return raw_iter_rho_method7batch__7next__7resume_(*sf.basic_ops7iterable, pt2next_pt_, log2_ipp, xi, j, xj, st_i_j, mode=mode, may_args6mode=may_args6mode, may_max_num_steps=may_max_num_steps)

@_method_
def iter_rho_method7batch__5iterable_(sf, xs, /, *, may_max_num_steps=None):
    'Iter x[k]{k>=0} -> Iter (log2_ipp, whether_stop[i,j]/bool{==is_bad_st_(st[i,j]) or eresult[i,j].is_right}, eresult[i,j], st[i,j], (i, x[i]), (j, x[j])){[i+1==2**log2_ipp][i <= j < 2*(1+i)]}  # stop iff found result or detect bad seed/state'
    return raw_iter_rho_method7batch__5iterable_(*sf.basic_ops7iterable, xs, may_max_num_steps=may_max_num_steps)

@_method_
def iter_rho_method7batch__5iterable__7resume_(sf, log2_ipp, xi, j, xj, st_i_j, xs6jpp, /, *, may_max_num_steps=None):
    'log2_ipp/uint{[i+1==2**log2_ipp]} -> x[i] -> j/uint{>=i==-1+2**log2_ipp}{<2*(1+i)==2**(1+log2_ipp)} -> x[j] -> st[i,j] -> Iter x[k]{k>=1+j} -> Iter (log2_ipp, whether_stop[i,j]/bool{==is_bad_st_(st[i,j]) or eresult[i,j].is_right}, eresult[i,j], st[i,j], (i, x[i]), (j, x[j])){[i+1==2**log2_ipp][i <= j < 2*(1+i)]}  # stop iff found result or detect bad seed/state'
    return raw_iter_rho_method7batch__5iterable__7resume_(*sf.basic_ops7iterable, log2_ipp, xi, j, xj, st_i_j, xs6jpp, may_max_num_steps=may_max_num_steps)


@_method_
def iter_rho_method7batch__5reproduceable_(sf, x0, history_saver7immutable__or__args=default_args4history_saver7immutable, /, *, pt2next_pt_, may_max_num_steps=None):
    return raw_iter_rho_method7batch__5reproduceable_(*_mk_basic_ops7reproduceable_(sf, pt2next_pt_), x0, history_saver7immutable__or__args, may_max_num_steps=may_max_num_steps)
@_method_
def iter_rho_method7batch__5reproduceable__7resume_(sf, log2_ipp, j, k, history_saver_i_j_k, /, *, pt2next_pt_, may_max_num_steps=None):
    return raw_iter_rho_method7batch__5reproduceable__7resume_(*_mk_basic_ops7reproduceable_(sf, pt2next_pt_), log2_ipp, j, k, history_saver_i_j_k, may_max_num_steps=may_max_num_steps)
def _mk_basic_ops7reproduceable_(sf, pt2next_pt_, /):
    #vs: .basic_ops7iterable
    #see:_prepare0001__6reproduceable_
    if pt2next_pt_ is None:
        #expected:IOps4RhoMethod__7next
        try:
            pt2next_pt_ = sf.pt2next_pt_
        except AttributeError:
            check_type_le(IOps4RhoMethod__7next, sf)
            raise
    else:
        #ok:IOps4RhoMethod
        check_callable(pt2next_pt_)
    pt2next_pt_

    (pt2rp_, rp2xx_st_, rp5payload_) = _prepare0001__6reproduceable_(sf.pt2st_, sf.merge_st_pt_, pt2next_pt_)
    return (pt2rp_, rp2xx_st_, sf.is_bad_st_, sf.st2eresult_)




class IOps4RhoMethod__7factor_pint(IOps4RhoMethod):
    __slots__ = ()
    @property
    @abstractmethod
    def modulus(sf, /):
        '-> int{>0}'

    @override
    def pt2st_(sf, x, /):
        '(x[i] -> st[i,i])'
        xi = x%sf.modulus
        IIdiffs_i_i = 1
        st_i_i = (xi, IIdiffs_i_i)
        return st_i_i
    @override
    def merge_st_pt_(sf, st_i_jmm, xj, /):
        '(st[i,-1+j] -> x[j] -> st[i,j])'
        (xi, IIdiffs_i_jmm) = st_i_jmm
        IIdiffs_i_j = IIdiffs_i_jmm * (xj-xi) %sf.modulus
        st_i_j = (xi, IIdiffs_i_j)
        return st_i_j
    @override
    def is_bad_st_(sf, st, /):
        '(st -> whether_bad_state/bool)'
        (xi, IIdiffs_i_j) = st_i_j = st
        return 0 == IIdiffs_i_j #%sf.modulus
    @override
    def st2eresult_(sf, st, /):
        '(st -> eresult/(Either errmsg oresult))'
        (xi, IIdiffs_i_j) = st_i_j = st
        m = sf.modulus
        assert m > 0
        zmay_ft = gcd(m, IIdiffs_i_j) %m
        whether_proper_factor = 1 < zmay_ft < m
        eresult = eresult_i_j = Either(whether_proper_factor, zmay_ft)
        return eresult


class IOps4RhoMethod__7factor_pint__7next(IOps4RhoMethod__7factor_pint, IOps4RhoMethod__7next):
    __slots__ = ()
    @property
    @abstractmethod
    def addend(sf, /):
        '-> int{[addend%modulus=!=0]}'
    @property
    @abstractmethod
    def assumed_factor4phi4modulus(sf, /):
        '-> int{>0}{%2==0} # assume [1 < gcd(phi_(modulus), assumed_factor4phi4modulus)]'
    @override
    def pt2next_pt_(sf, x, /):
        '(x[j] -> x[1+j])'
        m = sf.modulus
        return (sf.addend + pow(x, sf.assumed_factor4phi4modulus, m)) %m


class Ops4RhoMethod__7factor_pint__7next(IOps4RhoMethod__7factor_pint__7next):
    ___no_slots_ok___ = True
    def __init__(sf, modulus, addend, assumed_factor4phi4modulus, /):
        # !! [0 == assumed_factor4phi4modulus %2]
        check_int_ge(3, modulus)

        check_int_ge(2, assumed_factor4phi4modulus)
        if not 0 == assumed_factor4phi4modulus&1:raise ValueError(assumed_factor4phi4modulus)

        check_type_is(int, addend)
        addend %= modulus
        if 0 == addend:raise ValueError(assumed_factor4phi4modulus)
        if addend > (modulus>>1):
            addend -= modulus

        sf._args4repr = (modulus, addend, assumed_factor4phi4modulus)
        sf._m = modulus
        sf._e = assumed_factor4phi4modulus
        sf._d = addend

    def __repr__(sf, /):
        return repr_helper(sf, *sf._args4repr)
    @property
    @override
    def modulus(sf, /):
        '-> int{>0}'
        return sf._m

    @property
    @override
    def addend(sf, /):
        '-> int{[addend%modulus=!=0]}'
        return sf._d
    @property
    @override
    def assumed_factor4phi4modulus(sf, /):
        '-> int{>0}{%2==0} # assume [1 < gcd(phi_(modulus), assumed_factor4phi4modulus)]'
        return sf._e

#Ops4RhoMethod__7factor_pint__7next(3, 1, 2)
def try_factor1_pint__7rho_method7batch__7resume_(modulus, log2_max_num_steps, log2_ipp, xi, j, xj, st_i_j, /, *, mode, may_args6mode, more=False, addend=1, assumed_factor4phi4modulus=2, may_max_num_steps=None):
    'modulus/int{>3} -> log2_max_num_steps/int{>log2_ipp} -> log2_ipp/uint{[i+1==2**log2_ipp]} -> x[i] -> j/uint{>=i==-1+2**log2_ipp}{<2*(1+i)==2**(1+log2_ipp)} -> x[j] -> st[i,j] -> Iter x[k]{k>=1+j} -> Iter (log2_ipp, whether_stop[i,j]/bool{==is_bad_st_(st[i,j]) or eresult[i,j].is_right}, eresult[i,j], st[i,j], (i, x[i]), (j, x[j])){[i+1==2**log2_ipp][i <= j < 2*(1+i)]}  # stop iff found result or detect bad seed/state'
    check_int_ge(3, modulus)
    check_int_ge(0, log2_ipp)
    check_int_ge(1+log2_ipp, log2_max_num_steps)
    # [log2_max_num_steps > log2_ipp]
    i = -1 + (1<<log2_ipp)
    end6i = 1 << (1+log2_ipp)
    check_int_ge_lt(i, end6i, j)
    assert st_i_j[0] == xi, (xi, st_i_j)
    ops = Ops4RhoMethod__7factor_pint__7next(modulus, addend, assumed_factor4phi4modulus)
    it = ops.iter_rho_method7batch__7resume_(log2_ipp, xi, j, xj, st_i_j, mode=mode, may_args6mode=may_args6mode, may_max_num_steps=may_max_num_steps)
    it = islice(it, 0, log2_max_num_steps-log2_ipp)
    # !! [log2_max_num_steps > log2_ipp]
    # [len(it) > 0]
    # => record occurs
    for record in it:pass
    if more:
        return record
    (log2_ipp, whether_stop, eresult_i_j, st_i_j, (i, xi), (j, xj)) = record
    imay_proper_factor = eresult_i_j.to_right__fdefault_(lambda:-1)
    return imay_proper_factor



def try_factor1_pint__7rho_method7batch__5seed_(modulus, log2_max_num_steps, may_x0, /, *, mode, may_args6mode, more=False, addend=1, assumed_factor4phi4modulus=2, may_max_num_steps=None):
    'modulus/int{>3} -> log2_max_num_steps/int{>0} -> may x0/int -> (imay proper_factor/int{[1 < proper_factor < modulus][0==modulus%proper_factor]} if not more else (log2_ipp, whether_stop[i,j]/bool{==is_bad_st_(st[i,j]) or eresult[i,j].is_right}, eresult[i,j], st[i,j], (i, x[i]), (j, x[j])){[i+1==2**log2_ipp][i <= j < 2*(1+i)]})  # stop iff found result or detect bad seed/state'
    check_int_ge(3, modulus)
    check_int_ge(1, log2_max_num_steps)
    # [log2_max_num_steps > 0]
    if may_x0 is None:
        x0 = isqrt(modulus)
    else:
        x0 = may_x0
    x0
    check_type_is(int, x0)
    ops = Ops4RhoMethod__7factor_pint__7next(modulus, addend, assumed_factor4phi4modulus)
    ###########################
    max_num_steps = 1 << log2_max_num_steps
    if not may_max_num_steps is None:
        max_num_steps = min(max_num_steps, may_max_num_steps)
    max_num_steps
    _may_max_num_steps = max_num_steps
    ###########################
    it = ops.iter_rho_method7batch__5seed_(x0, mode=mode, may_args6mode=may_args6mode, may_max_num_steps=_may_max_num_steps)
    it = islice(it, 0, log2_max_num_steps)
    # !! [log2_max_num_steps > 0]
    # [len(it) > 0]
    # => record occurs
    for record in it:pass
    if more:
        return record
    (log2_ipp, whether_stop, eresult_i_j, st_i_j, (i, xi), (j, xj)) = record
    imay_proper_factor = eresult_i_j.to_right__fdefault_(lambda:-1)
    return imay_proper_factor








def raw_iter_rho_method7batch__7next_(pt2st_, merge_st_pt_, is_bad_st_, st2eresult_, pt2next_pt_, x0, /, *, mode, may_args6mode, may_max_num_steps=None):
    'pt2st_/(x[i] -> st[i,i]) -> merge_st_pt_/(st[i,-1+j] -> x[j] -> st[i,j]) -> is_bad_st_/(st -> whether_bad_state/bool) -> st2eresult_/(st -> eresult/(Either errmsg oresult)) -> pt2next_pt_/(x[j] -> x[1+j]) -> x[0] -> Iter (log2_ipp, whether_stop[i,j]/bool{==is_bad_st_(st[i,j]) or eresult[i,j].is_right}, eresult[i,j], st[i,j], (i, x[i]), (j, x[j])){[i+1==2**log2_ipp][i <= j < 2*(1+i)]}  # stop iff found result or detect bad seed/state'
    _check_mode_(mode)
    match (mode, may_args6mode):
        case ('iterable', None):
            pass
        case ('reproduceable', None):
            (max_size7physical, imay_max_size7apparent) = default_args4history_saver7immutable #(2049, -1)
        case ('reproduceable', (max_size7physical, imay_max_size7apparent)):
            pass
        case _:
            raise TypeError((mode, may_args6mode))

    match mode:
        #case None:
        case 'iterable':
            xs = iterate(pt2next_pt_, x0)
            return raw_iter_rho_method7batch__5iterable_(pt2st_, merge_st_pt_, is_bad_st_, st2eresult_, xs, may_max_num_steps=may_max_num_steps)
        case 'reproduceable':
            args4history_saver7immutable = (max_size7physical, imay_max_size7apparent)
            (pt2rp_, rp2xx_st_, rp5payload_) = _prepare0001__6reproduceable_(pt2st_, merge_st_pt_, pt2next_pt_)
            return raw_iter_rho_method7batch__5reproduceable_(pt2rp_, rp2xx_st_, is_bad_st_, st2eresult_, x0, args4history_saver7immutable, may_max_num_steps=may_max_num_steps)
        case _:
            raise 000
    raise 000


def _check_mode_(mode, /):
    # mode:'iterable,reproduceable'
    match mode:
        case str('iterable'|'reproduceable'):
            pass
        case _:
            raise TypeError('expected ("iterable"|"reproduceable"):', mode)
def raw_iter_rho_method7batch__7next__7resume_(pt2st_, merge_st_pt_, is_bad_st_, st2eresult_, pt2next_pt_, log2_ipp, xi, j, xj, st_i_j, /, *, mode, may_args6mode, may_max_num_steps=None):
    'pt2st_/(x[i] -> st[i,i]) -> merge_st_pt_/(st[i,-1+j] -> x[j] -> st[i,j]) -> is_bad_st_/(st -> whether_bad_state/bool) -> st2eresult_/(st -> eresult/(Either errmsg oresult)) -> pt2next_pt_/(x[j] -> x[1+j]) -> log2_ipp/uint{[i+1==2**log2_ipp]} -> x[i] -> j/uint{>=i==-1+2**log2_ipp}{<2*(1+i)==2**(1+log2_ipp)} -> x[j] -> st[i,j] -> Iter (log2_ipp, whether_stop[i,j]/bool{==is_bad_st_(st[i,j]) or eresult[i,j].is_right}, eresult[i,j], st[i,j], (i, x[i]), (j, x[j])){[i+1==2**log2_ipp][i <= j < 2*(1+i)]}  # stop iff found result or detect bad seed/state'
    _check_mode_(mode)
    match (mode, may_args6mode):
        case ('iterable', None):
            pass
        case ('reproduceable', None):
            (max_size7physical, imay_max_size7apparent) = default_args4history_saver7immutable #(2049, -1)
        case ('reproduceable', (max_size7physical, imay_max_size7apparent)):
            pass
        case _:
            raise TypeError((mode, may_args6mode))

    match mode:
        #case None:
        case 'iterable':
            xs6jpp = iterate(pt2next_pt_, xj) # indeed:xs6i
            777; next(xs6jpp) # -> xj
            return raw_iter_rho_method7batch__5iterable__7resume_(pt2st_, merge_st_pt_, is_bad_st_, st2eresult_, log2_ipp, xi, j, xj, st_i_j, xs6jpp, may_max_num_steps=may_max_num_steps)
        case 'reproduceable':
            (pt2rp_, rp2xx_st_, k, history_saver_i_j_k) = _prepare0003__6reproduceable_(pt2st_, merge_st_pt_, pt2next_pt_, xi, xj, st_i_j, j, max_size7physical, imay_max_size7apparent)
            return raw_iter_rho_method7batch__5reproduceable__7resume_(pt2rp_, rp2xx_st_, is_bad_st_, st2eresult_, log2_ipp, j, k, history_saver_i_j_k, may_max_num_steps=may_max_num_steps)
        case _:
            raise 000
    raise 000

def _prepare0003__6reproduceable_(pt2st_, merge_st_pt_, pt2next_pt_, xi, xj, st_i_j, j, max_size7physical, imay_max_size7apparent, /):
    (pt2rp_, rp2xx_st_, rp_i_j) = _prepare0002__6reproduceable_(pt2st_, merge_st_pt_, pt2next_pt_, xi, xj, st_i_j)
    history_saver_i_j_j = SparseHistorySaver7immutable(max_size7physical, imay_max_size7apparent).oo_append(rp_i_j)
    k = j
    777;history_saver_i_j_k = history_saver_i_j_j
    return (pt2rp_, rp2xx_st_, k, history_saver_i_j_k)
def _prepare0002__6reproduceable_(pt2st_, merge_st_pt_, pt2next_pt_, xi, xj, st_i_j, /):
    (pt2rp_, rp2xx_st_, rp5payload_) = _prepare0001__6reproduceable_(pt2st_, merge_st_pt_, pt2next_pt_)
    payload4rp_i_j = (xi, xj, st_i_j)
    rp_i_j = rp5payload_(payload4rp_i_j)
    return (pt2rp_, rp2xx_st_, rp_i_j)
def _prepare0001__6reproduceable_(pt2st_, merge_st_pt_, pt2next_pt_, /):
    def next7payload4rp_(payload4rp_i_j, /):
        (xi, xj, st_i_j) = payload4rp_i_j
        x_jpp = pt2next_pt_(xj)
        st_i_jpp = merge_st_pt_(st_i_j, x_jpp)
        payload4rp_i_jpp = (xi, x_jpp, st_i_jpp)
        return payload4rp_i_jpp
    ops4step7stated = StatedStepOps__7bare_iterate7include_initial_state(mstep7stated_:=next7payload4rp_)
    def rp5payload_(payload4rp_i_j, /):
        rp_i_j = Reproduceable7step_via_ops(ops4step7stated, initial_state:=payload4rp_i_j)
        return rp_i_j
    def rp2payload_(rp_i_j, /):
        payload4rp_i_j = rp_i_j.initial_state
        return payload4rp_i_j
    rp5payload_#pt2next_pt_, merge_st_pt_
    rp2payload_
    def pt2rp_(xi, /):
        st_i_i = pt2st_(xi)
        payload4rp_i_i = (xi, xi, st_i_i)
        rp_i_i = rp5payload_(payload4rp_i_i)
        return rp_i_i
    if 0:
      def rp2xx_st_(rp_i_j, /):
        payload4rp_i_j = rp2payload_(rp_i_j)
        return payload4rp_i_j
        (xi, xj, st_i_j) = payload4rp_i_j
        return (xi, xj, st_i_j)
    rp2xx_st_ = rp2payload_
    pt2rp_#pt2st_,pt2next_pt_, merge_st_pt_
    rp2xx_st_
    return (pt2rp_, rp2xx_st_, rp5payload_)

r'''[[[
def raw_iter_rho_method7batch__5xxx__7resume_(pt2st_, merge_st_pt_, is_bad_st_, st2eresult_, log2_ipp, xi, j, xj, st_i_j, xs6jpp, /, *, may_max_num_steps=None, mode:'iterable,reproduceable'):
    raw_iter_rho_method7batch__5iterable__7resume_(pt2st_, merge_st_pt_, is_bad_st_, st2eresult_, log2_ipp, xi, j, xj, st_i_j, xs6jpp, /, *, may_max_num_steps=None)
    raw_iter_rho_method7batch__5reproduceable__7resume_(pt2rp_, rp2xx_st_, is_bad_st_, st2eresult_, log2_ipp, j, k, history_saver_i_j_k, /, *, may_max_num_steps=None)
    TODO
#]]]'''#'''

default_cache_size4batch = 2049
def raw_iter_rho_method7batch__5iterable__7resume_(pt2st_, merge_st_pt_, is_bad_st_, st2eresult_, log2_ipp, xi, j, xj, st_i_j, xs6jpp, /, *, imay_cache_size4batch, may_max_num_steps=None):
    #vs:raw_iter_rho_method7batch__5reproduceable__7resume_
    r'''[[[
    :: pt2st_ -> merge_st_pt_ -> is_bad_st_ -> st2eresult_ -> log2_ipp/uint -> x[i] -> j/uint -> x[j] -> st[i,j] -> Iter x[k]{k>=1+j} -> Iter (log2_ipp, whether_stop[i,j]/bool, eresult[i,j], st[i,j], (i, x[i]), (j, x[j]))
    [pt2st_ :: (x[i] -> st[i,i])]
    [merge_st_pt_ :: (st[i,-1+j] -> x[j] -> st[i,j])]
    [is_bad_st_ :: (st -> whether_bad_state/bool)]
    [st2eresult_ :: (st -> eresult/(Either errmsg oresult))]
    [0 <= -1+2**log2_ipp == i <= j < 2*(1+i) == 2**(1+log2_ipp)]
    [whether_stop[i,j] == [[is_bad_st_(st[i,j])]or[eresult[i,j].is_right]]]
        # stop iff found result or detect bad seed/state

    * [imay_cache_size4batch:=-1]:
        # detect_batch_end_only: dont call st2eresult_() upon internal of bacth
        # batch end j be (-1+2*i)
        # ???batch size be (1+i){==2**log2_ipp}
        [whether_stop[i,j] == [[is_bad_st_(st[i,j])]or[[eresult[i,j].is_right][j==-1+min(max_num_steps,2**(1+log2_ipp))]]]]

    * [imay_cache_size4batch:=0]:
        # auto_batch_mode
        # auto select cache_size4batch
        [cache_size4batch := default_cache_size4batch]

    * [imay_cache_size4batch:=1]:
        # non_batch_mode
        # st2eresult_() detect per step
        [cache_size4batch := 1]

    * [imay_cache_size4batch>=2]:
        [cache_size4batch := imay_cache_size4batch]

    #]]]'''#'''
    # @20260909:++kw:imay_cache_size4batch{otherwise loss info inside batch interval}

    # may_max_num_steps vs log2_max_num_steps
    check_int_ge(0, log2_ipp)
    i = -1 + (1<<log2_ipp)
    end6i = 1 << (1+log2_ipp)
    check_int_ge_lt(i, end6i, j)
    if not None is may_max_num_steps:
        max_num_steps = may_max_num_steps
        check_int_ge(1+j, max_num_steps)

    check_int_ge(-1, imay_cache_size4batch)
    mode7batch7no_cache = False
    mode7batch7cache = False
    mode7non_batch = False
    match imay_cache_size4batch:
        case -1:
            mode7batch7no_cache = True
        case 0:
            mode7batch7cache = True
            cache_size4batch = default_cache_size4batch
        case 1:
            mode7non_batch = True
        case cache_size4batch:
            mode7batch7cache = True
    mode7batch7no_cache
    mode7batch7cache #optional:cache_size4batch
    mode7non_batch


    if is_bad_st_(st_i_j):
        eresult_i_j = mk_Left('bad_state')
        whether_stop = True
        yield (log2_ipp, whether_stop, eresult_i_j, st_i_j, (i, xi), (j, xj))
        return
    # [not$is_bad_st_(st_i_j)]

    777;snapshot = (log2_ipp, xi, j, xj, st_i_j)
    if mode7batch7cache:
        cache_size4batch
        kwds = dict(non_reproduceable_ok=True)
        j0 = j
        777;history_saver_i_j0_j = DenseHistorySaver(cache_size4batch)
        777;history_saver_i_j0_j.append(snapshot, **kwds)
        assert not history_saver_i_j0_j.full
    # mode7batch7cache => [not history_saver_i_j0_j.full]
        TODO

    xs6jpp = iter(xs6jpp)
    it = enumerate(xs6jpp, 1+j)
    if not None is may_max_num_steps:
        it = islice(it, 0, max_num_steps-(1+j))
    it
    #whether_stop = False
    j, xj, st_i_j
    777;snapshot
    #while not whether_stop:
    try:
     while 1:
        # mode7batch7cache => [not history_saver_i_j0_j.full]
        j, xj, st_i_j
        777;snapshot
        for j, xj in islice(it, 0, end6i-(1+j)):
            # mode7batch7cache => [not history_saver_i_j0_j.full]
            ##################
            777;st_i_jmm = st_i_j
            # [not$is_bad_st_(st_i_jmm)]
            st_i_j = merge_st_pt_(st_i_jmm, xj)
            777;snapshot = (log2_ipp, xi, j, xj, st_i_j)
            ##################
            #j, xj, st_i_j
            ##################
            if is_bad_st_(st_i_j):
                j, xj, st_i_j
                eresult_i_j = mk_Left('bad_state')
                whether_stop = True
                break
            # [not$is_bad_st_(st_i_j)]
            if mode7batch7cache:
                777;history_saver_i_j0_j.append(snapshot, **kwds)
                if history_saver_i_j0_j.full:
                    ... = history_saver_i_j0_j.search_key_points_(TODO, ..., backward_vs_forward=backward_vs_forward)
                    if ...:return ...
                    TODO
                    j0 = j
                    777;history_saver_i_j0_j.clear_but_last_()
                    assert not history_saver_i_j0_j.full
            # mode7batch7cache => [not history_saver_i_j0_j.full]
            ##################
            #j, xj, st_i_j
            ##################
        else:
            j, xj, st_i_j
            eresult_i_j = st2eresult_(st_i_j)
            whether_stop = eresult_i_j.is_right
        j, xj, st_i_j, eresult_i_j, whether_stop
        yield (log2_ipp, whether_stop, eresult_i_j, st_i_j, (i, xi), (j, xj))#record
        if whether_stop:break
        if not 1+j == end6i:
            #assert not None is may_max_num_steps
            #assert 1+j == max_num_steps < end6i == 1 << (1+log2_ipp), (log2_ipp, i, j, max_num_steps, end6i, 1 << (1+log2_ipp))
            assert 1+j < end6i == 1 << (1+log2_ipp), (log2_ipp, i, j, end6i, 1 << (1+log2_ipp))
                # !! [xs6jpp is finite&&short] or [max_num_steps occurs]
            return
        assert 1+j == end6i == 1 << (1+log2_ipp), (log2_ipp, i, j, end6i, 1 << (1+log2_ipp))
        log2_ipp += 1
        777;i = j
        777;xi = xj
        777;st_i_j = pt2st_(xi)
        777;end6i = 1 << (1+log2_ipp)
        777;snapshot = (log2_ipp, xi, j, xj, st_i_j)
    except BaseException as exc:
        #KeyboardInterrupt
        raise repack_exception_(exc, snapshot)















def raw_iter_rho_method7batch__5iterable_(pt2st_, merge_st_pt_, is_bad_st_, st2eresult_, xs, /, *, may_max_num_steps=None):
    'pt2st_/(x[i] -> st[i,i]) -> merge_st_pt_/(st[i,-1+j] -> x[j] -> st[i,j]) -> is_bad_st_/(st -> whether_bad_state/bool) -> st2eresult_/(st -> eresult/(Either errmsg oresult)) -> Iter x[k]{k>=0} -> Iter (log2_ipp, whether_stop[i,j]/bool{==is_bad_st_(st[i,j]) or eresult[i,j].is_right}, eresult[i,j], st[i,j], (i, x[i]), (j, x[j])){[i+1==2**log2_ipp][i <= j < 2*(1+i)]}  # stop iff found result or detect bad seed/state'
    xs = iter(xs)
    x0 = next(xs)
    log2_ipp = 0
    #i = -1 + (1<<log2_ipp)
    i = 0
    xi = x0
    j = i
    xj = xi
    st_i_j = pt2st_(x0)
    xs6jpp = xs
    return raw_iter_rho_method7batch__5iterable__7resume_(pt2st_, merge_st_pt_, is_bad_st_, st2eresult_, log2_ipp, xi, j, xj, st_i_j, xs6jpp, may_max_num_steps=may_max_num_steps)



def raw_iter_rho_method7batch__5reproduceable_(pt2rp_, rp2xx_st_, is_bad_st_, st2eresult_, x0, history_saver7immutable__or__args=default_args4history_saver7immutable, /, *, may_max_num_steps=None):
    #vs:raw_iter_rho_method7batch__5iterable_
    log2_ipp = 0
    777;i = 0
    777;xi = x0
    rp_i_i = pt2rp_(xi)
    j = i
    777;rp_i_j = rp_i_i

    force_lazy_imported_func_(IHistorySaver7immutable)
    match history_saver7immutable__or__args:
        case IHistorySaver7immutable() as history_saver7immutable:
            history_saver_i_j_j = history_saver7immutable.oo_clear_().oo_append(rp_i_j)
        case (max_size7physical, imay_max_size7apparent):
            history_saver_i_j_j = SparseHistorySaver7immutable(max_size7physical, imay_max_size7apparent).oo_append(rp_i_j)
        case _:
            raise TypeError(history_saver7immutable__or__args)
    history_saver_i_j_j
    assert len(history_saver_i_j_j) == 1
    k = j
    777;history_saver_i_j_k = history_saver_i_j_j
    return raw_iter_rho_method7batch__5reproduceable__7resume_(pt2rp_, rp2xx_st_, is_bad_st_, st2eresult_, log2_ipp, j, k, history_saver_i_j_k, may_max_num_steps=may_max_num_steps)

def raw_iter_rho_method7batch__5reproduceable__7resume_(pt2rp_, rp2xx_st_, is_bad_st_, st2eresult_, log2_ipp, j, k, history_saver_i_j_k, /, *, may_max_num_steps=None):
    #vs:raw_iter_rho_method7batch__5iterable__7resume_
    r'''[[[
    :: pt2rp_ -> rp2xx_st_ -> is_bad_st_ -> st2eresult_ -> log2_ipp/uint -> j/uint -> k/uint -> history_saver{i,j,k} -> Iter (log2_ipp, whether_stop[i,k]/bool, eresult[i,k], (i,j,k), history_saver{i,j,k}, (st[i,j], st[i,k]), (x[i], x[j], x[k]))
    #   # stop iff found result or detect bad seed/state
    #   # [whether_stop[i,k] == [[is_bad_st_(st[i,k])]or[[eresult[i,k].is_right][[rp[i,k] stopped]or[k==-1+min(2*(1+i),max_num_steps)]or[k==j-1+history_saver_i_j_k.imay_max_size7apparent>=j+1][#<==>[history_saver_i_j_k.full]<==>[1+k-j==history_saver_i_j_k.imay_max_size7apparent>=2=!=-1]#]]]]]
    #
    [-1+2**log2_ipp == i <= j <= k < min(2*(1+i), max_num_steps)]
    [pt2rp_ :: x[i] -> rp[i,i]]
    [rp2xx_st_ :: rp[i,j] -> (x[i],x[j],st[i,j])]
    [is_bad_st_ :: (st -> whether_bad_state/bool)]
    [st2eresult_ :: (st -> eresult/(Either errmsg oresult))]
    #
    [rp[i,j] :: IReproduceable{offset==j-i}{xnext4reproduceable_ :: rp[i,j] -> ResultTypes4xnext{rp[i,1+j]}}]
    [history_saver[i,j,k] :: IHistorySaver7immutable{rp}{len>=1}{len==1+k-j}{.head is rp[i,j]}{.last is rp[i,k]}]
    #   #   [x[i] == rp2xx_st_(history_saver[i,j,k].head)[0]]
    #
    #]]]'''#'''
    # (j,k) come from:
    #       * eg: [0==M%N][xj%M --> xj%N]
    #       * eg: resume@j stop by max_num_steps/imay_max_size7apparent/KeyboardInterrupt @k
    #
    # xxx:rp{[oresult::(x[j],st[i,j])]}{hasattr: .tmay_oresult[#eg:Reproduceable7cached_oresult#]}
    #   --> rp2xx_st_
    #
    ##############################
    ##############################
    ##############################
    # code base upon raw_iter_rho_method7batch__5iterable__7resume_()
    ##############################
    ##############################
    ##############################

    # may_max_num_steps vs log2_max_num_steps
    check_int_ge(0, log2_ipp)
    i = -1 + (1<<log2_ipp)
    end6i = 1 << (1+log2_ipp) # double_ipp
    check_int_ge_lt(i, end6i, j)
    check_int_ge_lt(j, end6i, k)
    # [0 <= i <= j <= k < end6i]
    if not None is may_max_num_steps:
        max_num_steps = may_max_num_steps
        check_int_ge(1+k, max_num_steps)
        # [0 <= i <= j <= k < min(end6i, max_num_steps)]
    if not 1+k-j == len(history_saver_i_j_k) > 0: raise ValueError('not satisfied precondition:[1+k-j == len(history_saver_i_j_k) > 0]')
    # [len(history_saver_i_j_k) > 0]


    #yield-(log2_ipp, whether_stop, eresult_i_k, (i,j,k), history_saver_i_j_k, (st_i_j, st_i_k), (xi, xj, xk))
    (_, (st_i_j, st_i_k), (xi, xj, xk)) = _extract4output(rp2xx_st_, history_saver_i_j_k)

    777;snapshot = (log2_ipp, (i,j,k), history_saver_i_j_k, (st_i_j, st_i_k), (xi, xj, xk))
    if is_bad_st_(st_i_k):
        eresult_i_k = mk_Left('bad_state')
        whether_stop = True
        yield (log2_ipp, whether_stop, eresult_i_k, (i,j,k), history_saver_i_j_k, (st_i_j, st_i_k), (xi, xj, xk))
        #.yield (log2_ipp, whether_stop, eresult_i_k, (i,j,k), *_extract4output(rp2xx_st_, history_saver_i_j_k))
        return

    # [not$is_bad_st_(st_i_k)]
    _ver = 1
    # !! [len(history_saver_i_j_k) > 0]
    (_max4num_remain_ks, expected_k7final, idx_rps6kpp6i) = _mk_ex__idx_rps6kpp6i(end6i, may_max_num_steps, i,j,k,history_saver_i_j_k, ver=_ver)
    assert _max4num_remain_ks >= 0
    b_init = True
    try:
     while 1:
        # snapshot, end6i, log2_ipp, (i,j,k), (history_saver_i_j_k, (st_i_j, st_i_k), (xi, xj, xk))
        # [not$is_bad_st_(st_i_k)]
        # [len(history_saver_i_j_k) > 0]
        # iterator:idx_rps6kpp6i{_max4num_remain_ks}
        if b_init:
            b_init = False
            assert _max4num_remain_ks >= 0
            skip6init = history_saver_i_j_k.full
        else:
            assert _max4num_remain_ks > 0
            skip6init = False

        if skip6init:
            assert history_saver_i_j_k.full
            skip6init = False
            # [history_saver_i_j_k.full]
        else:
            # [not$is_bad_st_(st_i_k)]
            # [not history_saver_i_j_k.full]
            assert not history_saver_i_j_k.full
            for kpp, rp_kpp6i in idx_rps6kpp6i:
                777;_max4num_remain_ks -= 1
                # [not$is_bad_st_(st_i_k)]
                # [not history_saver_i_j_k.full]
                if _ver==2:
                    # !! _mk_ex__idx_rps6kpp6i(...,_ver=2)
                    # [not$[[history_saver_i_j_k.full]or[1+k == end6i]or[1+k == max_num_steps]]]
                    pass
                else:
                    # [not$[[1+k == end6i]or[1+k == max_num_steps]]]
                    pass
                # [not$[[history_saver_i_j_k.full]or[1+k == end6i]or[1+k == max_num_steps]]]
                # [not history_saver_i_j_k.full]
                assert not history_saver_i_j_k.full
                history_saver_i_j_kpp = history_saver_i_j_k.oo_append(rp_kpp6i)
                    # not ^FullError
                # [MAYBE:[history_saver_i_j_kpp.full]]
                (_xi, x_kpp, st_i_kpp) = rp2xx_st_(rp_kpp6i)
                ##################
                # update k:
                ##################
                (k, xk, st_i_k, history_saver_i_j_k) = (kpp, x_kpp, st_i_kpp, history_saver_i_j_kpp)
                777;snapshot = (log2_ipp, (i,j,k), history_saver_i_j_k, (st_i_j, st_i_k), (xi, xj, xk))
                ##################
                # [MAYBE:[history_saver_i_j_k.full]]
                ##################
                if is_bad_st_(st_i_k):
                    eresult_i_k = mk_Left('bad_state')
                    whether_stop = True
                    yield (log2_ipp, whether_stop, eresult_i_k, (i,j,k), history_saver_i_j_k, (st_i_j, st_i_k), (xi, xj, xk))
                    return
                # [not$is_bad_st_(st_i_k)]
                ##################
                # [MAYBE:[history_saver_i_j_k.full]]
                if not _ver==2:
                    if history_saver_i_j_k.full:
                        break # [history_saver_i_j_k.full]
                    # [not history_saver_i_j_k.full]
                else:
                    # [_ver==2] => idx_rps6kpp6i cutoff@[history_saver_i_j_k.full]
                    pass
                # [not$is_bad_st_(st_i_k)]
            #end-for kpp, rp_kpp6i in idx_rps6kpp6i:
            # [MAYBE:[history_saver_i_j_k.full]]
            # [not$is_bad_st_(st_i_k)]
            # [[history_saver_i_j_k.full]or[1+k == end6i]or[1+k == max_num_steps]or[rp_k6i stopped]]
        ###########################
        # [MAYBE:[history_saver_i_j_k.full]]
        # [not$is_bad_st_(st_i_k)]
        # [[history_saver_i_j_k.full]or[1+k == end6i]or[1+k == max_num_steps]or[rp_k6i stopped]]

        ###########################
        ###########################
        ###########################
        ###########################
        #below never update k
        ###########################
        ###########################
        ###########################


        ###########################
        assert k <= expected_k7final
        assert _max4num_remain_ks >= 0
        assert k+_max4num_remain_ks == expected_k7final
        ###########################
        # ??? [known:[rp_k6i stopped]]
        if _ver==2:
            known__rp_k6i__stopped = k < expected_k7final
            assert known__rp_k6i__stopped is (_max4num_remain_ks > 0)
        else:
            known__rp_k6i__stopped = not history_saver_i_j_k.full and k < expected_k7final
        known__rp_k6i__stopped
        ###########################

        if 1:
            eresult_i_k = st2eresult_(st_i_k)
            whether_stop = known__rp_k6i__stopped or eresult_i_k.is_right or 1+k == may_max_num_steps
            yield (log2_ipp, whether_stop, eresult_i_k, (i,j,k), history_saver_i_j_k, (st_i_j, st_i_k), (xi, xj, xk))
            if whether_stop:return
            # [not-known:[rp_k6i not stopped]]
            assert not _ver==2 or _max4num_remain_ks == 0
            # [1+k =!= max_num_steps]
            history_saver_i_k_k = history_saver_i_j_k.oo_clear_but_last_()
            # [1 == len(history_saver_i_k_k)]
            ##################
            # update j:
            ##################
            (j, xj, st_i_j, history_saver_i_j_k) = (k, xk, st_i_k, history_saver_i_k_k)
            777;snapshot = (log2_ipp, (i,j,k), history_saver_i_j_k, (st_i_j, st_i_k), (xi, xj, xk))
            ##################
            # [1 == len(history_saver_i_j_k)]
            # [not history_saver_i_j_k.full]
            # [1+k =!= max_num_steps]
            # [not-known:[rp_k6i not stopped]]
        # [not-known:[rp_k6i not stopped]]
        # [not$is_bad_st_(st_i_k)]
        # [1+k =!= max_num_steps]
        # [not history_saver_i_j_k.full]
        assert not history_saver_i_j_k.full
        assert not _ver==2 or _max4num_remain_ks == 0
        if 1+k == end6i:
            # [1+k == end6i]
            assert _max4num_remain_ks == 0
            rp_k6k = pt2rp_(xk)
            # !! [not history_saver_i_j_k.full]
            history_saver_k_k_k = history_saver_i_j_k.oo_clear_().oo_append(rp_k6k)
            # [len(history_saver_k_k_k) == 1]
            (_1_xk, _2_xk, st_k_k) = rp2xx_st_(rp_k6k)
            ##################
            # update i,j:
            ##################
            (end6i, log2_ipp, (i,j), (history_saver_i_j_k, (st_i_j, st_i_k), (xi, xj))) = (end6i<<1, 1+log2_ipp, (k,k), (history_saver_k_k_k, (st_k_k, st_k_k), (xk, xk)))
            777;snapshot = (log2_ipp, (i,j,k), history_saver_i_j_k, (st_i_j, st_i_k), (xi, xj, xk))
            # [1+k < end6i]
            assert 1+k < end6i
            # !! [len(history_saver_k_k_k) == 1]
            # [len(history_saver_i_j_k) == 1 > 0]
            ##################
            if is_bad_st_(st_i_k):
                eresult_i_k = mk_Left('bad_state')
                whether_stop = True
                yield (log2_ipp, whether_stop, eresult_i_k, (i,j,k), history_saver_i_j_k, (st_i_j, st_i_k), (xi, xj, xk))
                return
            # [not$is_bad_st_(st_i_k)]
            ##################
            ##################
            # snapshot, end6i, log2_ipp, (i,j,k), (history_saver_i_j_k, (st_i_j, st_i_k), (xi, xj, xk))
            # [not$is_bad_st_(st_i_k)]
            # [len(history_saver_i_j_k) > 0]
            # yet...:iterator:idx_rps6kpp6i{_max4num_remain_ks}
            ##################
            # [1+k < end6i]

            # !! [len(history_saver_i_j_k) == 1 > 0]
            # [not history_saver_i_j_k.full]
        # [len(history_saver_i_j_k) > 0]
        # [not-known:[rp_k6i not stopped]]
        # [1+k < end6i]
        # [1+k =!= max_num_steps]
        # [not history_saver_i_j_k.full]
        # [not$is_bad_st_(st_i_k)]
        assert not _ver==2 or _max4num_remain_ks == 0
        if _max4num_remain_ks == 0:
            # [_max4num_remain_ks == 0]
            # !! [len(history_saver_i_j_k) > 0]
            (_max4num_remain_ks, expected_k7final, idx_rps6kpp6i) = _mk_ex__idx_rps6kpp6i(end6i, may_max_num_steps, i,j,k,history_saver_i_j_k, ver=_ver)
            # !! [1+k < end6i]
            # !! [1+k =!= max_num_steps]
            # !! [not history_saver_i_j_k.full]
            assert _max4num_remain_ks > 0 # !!!
            # iterator:idx_rps6kpp6i{_max4num_remain_ks>0}
        # iterator:idx_rps6kpp6i{_max4num_remain_ks>0}

        ###########################
        # [not-known:[rp_k6i not stopped]]
        # [1+k < end6i]
        # [1+k =!= max_num_steps]
        # [not history_saver_i_j_k.full]
        # [not$is_bad_st_(st_i_k)]
        # iterator:idx_rps6kpp6i{_max4num_remain_ks>0}
        # => next round process at least one rp_kpp6i if [rp_k6i actually not stopped]
        assert _max4num_remain_ks > 0 # !!!
        assert 1+k < end6i
        assert may_max_num_steps is None or 1+k < max_num_steps
        assert not history_saver_i_j_k.full
        ###########################
    except BaseException as exc:
        #KeyboardInterrupt
        raise repack_exception_(exc, snapshot)




def _extract4output(rp2xx_st_, history_saver_i_j_k, /):
    rp_j6i = history_saver_i_j_k.head
    rp_k6i = history_saver_i_j_k.last
    (xi, xj, st_i_j) = rp2xx_st_(rp_j6i)
    (_xi, xk, st_i_k) = rp2xx_st_(rp_k6i)
    return (history_saver_i_j_k, (st_i_j, st_i_k), (xi, xj, xk))


def _mk_ex__idx_rps6kpp6i(end6i, may_max_num_steps, i,j,k,history_saver_i_j_k, /, *, ver):
    '-> (_max4num_remain_ks, Iter [(1+k,rp[i,1+k])...])'
    # precondition:[len(history_saver_i_j_k) > 0]
    rp_k6i = history_saver_i_j_k.last
        # not ^EmptyError
    match ver:
        case 1:
            max4kpp = _calc_max4kpp__ver1_(end6i, may_max_num_steps)
        case 2:
            max4kpp = _calc_max4kpp__ver2_(end6i, may_max_num_steps, i,j,k,history_saver_i_j_k)
        case _:
            raise 000
    rps6kpp6i = iter_snds4reproduceable_(rp_k6i)
    777;rps6kpp6i = islice(rps6kpp6i, 0, _max4num_remain_ks:=max4kpp -(1+k))
    idx_rps6kpp6i = enumerate(rps6kpp6i, 1+k)
    expected_k7final = k+_max4num_remain_ks
    return (_max4num_remain_ks, expected_k7final, idx_rps6kpp6i)



def _calc_max4kpp__ver1_(end6i, may_max_num_steps, /):
    #max4kpp = min(end6i, max_num_steps)
    max4kpp = end6i
    match may_max_num_steps:
        case None:
            pass
        case max_num_steps:
            max4kpp = min(max4kpp, max_num_steps)
    max4kpp
    return max4kpp

def _calc_max4kpp__ver2_(end6i, may_max_num_steps, i,j,k,history_saver_i_j_k, /):
    max4kpp = _calc_max4kpp__ver1_(end6i, may_max_num_steps)
    match history_saver_i_j_k.imay_max_size7apparent:
        case -1:
            pass
        case max_size7apparent:
            size7apparent = history_saver_i_j_k.size7apparent
            assert 0 < 1+k-j == size7apparent <= max_size7apparent
            max4kpp = min(max4kpp, 1+k+max_size7apparent -size7apparent)
    max4kpp

    return max4kpp














__all__
from seed.algo.rho_method__7iter7batch import raw_iter_rho_method7batch__7next_, raw_iter_rho_method7batch__5iterable_, raw_iter_rho_method7batch__5iterable__7resume_, raw_iter_rho_method7batch__7next__7resume_
#.  all: -> Iter (log2_ipp, whether_stop, eresult_i_j, st_i_j, (i, xi), (j, xj))
#.  raw_iter_rho_method7batch__7next_(pt2st_, merge_st_pt_, is_bad_st_, st2eresult_, pt2next_pt_, x0, /, *, mode, may_args6mode, pt2next_pt_=None, may_max_num_steps=None)
#.  raw_iter_rho_method7batch__5iterable_(pt2st_, merge_st_pt_, is_bad_st_, st2eresult_, xs, /, *, pt2next_pt_=None, may_max_num_steps=None)
#.  raw_iter_rho_method7batch__5iterable__7resume_(pt2st_, merge_st_pt_, is_bad_st_, st2eresult_, log2_ipp, xi, j, xj, st_i_j, xs6jpp, /, *, may_max_num_steps=None)
#.  raw_iter_rho_method7batch__7next__7resume_(pt2st_, merge_st_pt_, is_bad_st_, st2eresult_, pt2next_pt_, log2_ipp, xi, j, xj, st_i_j, /, *, mode, may_args6mode, may_max_num_steps=None)


from seed.algo.rho_method__7iter7batch import IOps4RhoMethod, IOps4RhoMethod__7next
from seed.algo.rho_method__7iter7batch import IOps4RhoMethod__7factor_pint, IOps4RhoMethod__7factor_pint__7next, Ops4RhoMethod__7factor_pint__7next

from seed.algo.rho_method__7iter7batch import IOps4RhoMethod, iter_rho_method7batch__7next_, iter_rho_method7batch__5iterable_, iter_rho_method7batch__5iterable__7resume_, iter_rho_method7batch__7next__7resume_
from seed.algo.rho_method__7iter7batch import IOps4RhoMethod__7next, iter_rho_method7batch__5seed_, iter_rho_method7batch__7resume_
#.  all: -> Iter (log2_ipp, whether_stop, eresult_i_j, st_i_j, (i, xi), (j, xj))
#.  iter_rho_method7batch__7next_(sf, pt2next_pt_, x0, /, *, mode, may_args6mode, may_max_num_steps=None)
#.  iter_rho_method7batch__7next__7resume_(sf, pt2next_pt_, log2_ipp, xi, j, xj, st_i_j, /, *, mode, may_args6mode, may_max_num_steps=None)
#.  iter_rho_method7batch__5iterable_(sf, xs, /, *, may_max_num_steps=None)
#.  iter_rho_method7batch__5iterable__7resume_(sf, log2_ipp, xi, j, xj, st_i_j, xs6jpp, /, *, may_max_num_steps=None)
#.  iter_rho_method7batch__5seed_(sf, x0, /, *, mode, may_args6mode, pt2next_pt_=None, may_max_num_steps=None)
#.  iter_rho_method7batch__7resume_(sf, log2_ipp, xi, j, xj, st_i_j, /, *, mode, may_args6mode, pt2next_pt_=None, may_max_num_steps=None)

from seed.algo.rho_method__7iter7batch import try_factor1_pint__7rho_method7batch__5seed_, try_factor1_pint__7rho_method7batch__7resume_
#.  try_factor1_pint__7rho_method7batch__5seed_(modulus, log2_max_num_steps, may_x0, /, *, mode, may_args6mode, more=False, addend=1, assumed_factor4phi4modulus=2, may_max_num_steps=None)
#.  try_factor1_pint__7rho_method7batch__7resume_(modulus, log2_max_num_steps, log2_ipp, xi, j, xj, st_i_j, /, *, mode, may_args6mode, more=False, addend=1, assumed_factor4phi4modulus=2, may_max_num_steps=None)
from seed.algo.rho_method__7iter7batch import *
