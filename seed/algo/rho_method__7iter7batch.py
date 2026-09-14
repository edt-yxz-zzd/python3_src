#__all__:goto
r'''[[[
e ../../python3_src/seed/algo/rho_method__7iter7batch.py

seed.algo.rho_method__7iter7batch
py -m nn_ns.app.debug_cmd   seed.algo.rho_method__7iter7batch -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.algo.rho_method__7iter7batch:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'

def try_factor_pint7rho_(ops, imay_max4end6rho, u0_or_scale, may_empty_saver7immutable, /, *, u0_be_floor_sqrt_scale_modulus=False):
def try_factor_pint7rho__7resume_(ops, imay_max4end6rho, record7old, /):
#.  '-> (final, some_proper_factors, idc, record7old)'
#.  (jround, jbatch, end6i, i, pt_i, saver_i_jpp_kpp) = record7old

>>> ops = Ops4RhoMethod7batch__7factor_pint__7even_exp_add_constant(97*79, 2, 1)
>>> ops
Ops4RhoMethod7batch__7factor_pint__7even_exp_add_constant(7663, 2, 1)
>>> output = ops.try_factor_pint7rho_(-1, 1, None, u0_be_floor_sqrt_scale_modulus=True); output
(True, (79, 97), (10, 11), (3, 0, 16, 7, 6109, SparseHistorySaver7immutable(2049, -1, '!', ((7, 6109, 1), mk_rglnkls_([(8, 1072, 2626), (9, 7398, 5531), (10, 1259, 2813), (11, 6504, 0)]), 5, 5, 1, 0))))
>>> ops.beyond7rho_(output[-1][-1].last[-1])
True
>>> ops.try_factor_pint7rho_(11, 1, None, u0_be_floor_sqrt_scale_modulus=True)
(True, (97,), (10,), (3, 0, 16, 7, 6109, SparseHistorySaver7immutable(2049, -1, '!', ((7, 6109, 1), mk_rglnkls_([(8, 1072, 2626), (9, 7398, 5531), (10, 1259, 2813)]), 4, 4, 1, 0))))

>>> output = ops.try_factor_pint7rho_(10, 1, None, u0_be_floor_sqrt_scale_modulus=True); output
(False, (), (), (3, 1, 16, 7, 6109, SparseHistorySaver7immutable(2049, -1, '!', ((9, 7398, 5531), mk_rglnkls_(), 1, 1, 1, 0))))

>>> ops.try_factor_pint7rho__7resume_(11, output[-1])
(True, (97,), (10,), (3, 1, 16, 7, 6109, SparseHistorySaver7immutable(2049, -1, '!', ((9, 7398, 5531), mk_rglnkls_([(10, 1259, 2813)]), 2, 2, 1, 0))))
>>> ops.try_factor_pint7rho__7resume_(12, output[-1])
(True, (79, 97), (10, 11), (3, 1, 16, 7, 6109, SparseHistorySaver7immutable(2049, -1, '!', ((9, 7398, 5531), mk_rglnkls_([(10, 1259, 2813), (11, 6504, 0)]), 3, 3, 1, 0))))



















py_adhoc_call   seed.algo.rho_method__7iter7batch   @f
]]]'''#'''
__all__ = r'''
IOps4RhoMethod7batch
    mnext7rho7branched_
    setup7rho7new_round_
    iter7rho_
        prepare4iter7rho_
    iter7rho__7offseted_jround_
        prepare4iter7rho__7offseted_jround_
    iter7rho__7resume_

    gmk_default_empty_saver7immutable_
        default_args4history_saver7immutable
    iter_subsequents7rho7unlimit_
    try_search_oresult7rho__7resume_
    try_search_oresult7rho_

    IOps4RhoMethod7batch__7factor_pint
        try_factor_pint7rho_
            prepare4try_factor_pint7rho_
        try_factor_pint7rho__7resume_
        postprocess7factor_pint7rho_

IOps4RhoMethod7batch
    IOps4RhoMethod7batch__7factor_pint
        IOps4RhoMethod7batch__7factor_pint__7even_exp_add_constant
            Ops4RhoMethod7batch__7factor_pint__7even_exp_add_constant

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
    from seed.math.gcd import noncoprime_part_of_to_, coprime_part_of_to_

    from seed.types.Reproduceable import iter_snds4reproduceable_
    from seed.types.Reproduceable import Reproduceable7step_via_ops, StatedStepOps__7bare_iterate7include_initial_state
    from seed.types.HistorySaver import SparseHistorySaver7immutable
    from seed.types.HistorySaver import IHistorySaver7immutable
    from seed.types.SinglyLinkedList import mk_rglnkls_, oo_push_, list7up_

#.#################################

#.from seed.helper.lazy_import__func7dict import lazy_import__funcs7dict_
#.(check_type_is, check_int_ge, _ifNone) = lazy_import__funcs7dict_(__name__ or globals() or locals(), 'seed.tiny_.check',  'check_type_is, check_int_ge      ifNone:_ifNone')
#.#################################
#.def mk_context4lazy_import_registered_names_(qnm4mdl7inject, qnm4pseudo_mdl7import, name7importZqnm4mdl, name7importZalias7inject={}, may_bifix4lazy_name7import=None, lazy_name7importZoriginal_name7import={}):
#.from seed.helper.lazy_import__func7context7register import mk_context4lazy_import_registered_names_, name7importZqnm4mdl_7tiny
#.with mk_context4lazy_import_registered_names_(__name__, 'seed._lazy_', name7importZqnm4mdl_7tiny):
#.    from seed._lazy_ import print_err, fst, echo, ifNone
#.#################################
#.from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
#.with mk_ctx4lazy_import4funcs_(__name__):
#.    from itertools import islice
#.    from functools import cached_property
#.    from seed.for_libs.for_functools.cached_property import cached_property
#.    from seed.types.CachedProperty import CachedProperty, mk_cached_propertyT_
#.    from seed.func_tools.dot2 import dot
#.    from seed.tiny_.check import check_type_is, check_int_ge
#.with mk_ctx4lazy_import4funcs_(__name__, arbitrary_ok=True):
#.    from seed.data_funcs.lnkls import rglnkls_ops# empty_rglnkls, mk_empty_rglnkls, rglnkls_ipush_right, rglnkls_ipop_right, rglnkls2reversed_iterable, rglnkls5iterable
#.with mk_ctx4lazy_import4funcs_(__name__, 'ifNone:_ifNone, ifNonef:_ifNonef'):
#.    from seed.helper.ifNone import ifNone as _ifNone, ifNonef as _ifNonef
#.#################################
___end_mark_of_excluded_global_names__0___ = ...


#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.    raise NotImplementedError(Exception, StopIteration)

class IOps4RhoMethod7batch(ABC):
    __slots__ = ()
    @abstractmethod
    def step7rho_(sf, pt_k, /):
        'pt[k] -> pt[1+k]'
    @abstractmethod
    def rdiff7rho_(sf, pt_i, pt_kpp, /):
        '[i<kpp] => pt[i] -> pt[kpp] -> df[i,kpp]'
    @abstractmethod
    def setup7rho_(sf, pt_i, /):
        'pt[i] -> ([i<jpp] => st[i,jpp,jpp]) # [@[i,jpp::uint][i<jpp] -> [not beyond7rho_(st[i,jpp,jpp])][detect7rho_(st[i,jpp,jpp]).is_left]] # [rank==-1]'
    @abstractmethod
    def merge7rho_(sf, st_i_jpp_kpp, df_i_kpp, /):
        '[i<jpp<=kpp] => st[i,jpp,kpp] -> df[i,kpp] -> st[i,jpp,1+kpp]'
    @abstractmethod
    def beyond7rho_(sf, st_i_jpp_kpp, /):
        '[i<jpp<=kpp] => st[i,jpp,kpp] -> bad/bool # [rank==+1]'
    @abstractmethod
    def detect7rho_(sf, st_i_jpp_kpp, /):
        '[i<jpp<=kpp][not beyond7rho_(st[i,jpp,kpp])] => st[i,jpp,kpp] -> eresult[i,jpp,kpp] # [rank==(-1|0)]'
    @abstractmethod
    def size4next_round_(sf, jround, size4curr_round, /):
        'jround -> size4curr_round/size4round{jround} -> size4next_round/size4round{1+jround} # [size4curr_round == end6i-(1+i)] # [1 == size4round{jround:=0}]'

IOps4RhoMethod7batch.__doc__ = r'''
step7rho_ :: pt[k] -> pt[1+k]
rdiff7rho_ :: [i<kpp] => pt[i] -> pt[kpp] -> df[i,kpp]
setup7rho_ :: pt[i] -> ([i<jpp] => st[i,jpp,jpp])
merge7rho_ :: [i<jpp<=kpp] => st[i,jpp,kpp] -> df[i,kpp] -> st[i,jpp,1+kpp]
beyond7rho_ :: [i<jpp<=kpp] => st[i,jpp,kpp] -> bad/bool
    [rank==+1]
detect7rho_ :: [i<jpp<=kpp][not beyond7rho_(st[i,jpp,kpp])] => st[i,jpp,kpp] -> eresult[i,jpp,kpp]
    [rank==(-1|0)]
[@[i,jpp::uint][i<jpp] -> [not beyond7rho_(st[i,jpp,jpp])][detect7rho_(st[i,jpp,jpp]).is_left]]
    [rank==-1]

size4next_round_ :: jround -> size4curr_round/size4round{jround} -> size4next_round/size4round{1+jround}
[1 == size4round{jround:=0}]

###num_batchs4round_ :: jround -> size4curr_round/size4round{jround} -> num_batchs4curr_round/num_batchs4round{jround}

[i<=j<=k]:
    [sts_i_jpp_kpp :: [st[i,1+j,1+z] | [z:<-[j..<k]]]]
      # [j==k] => null/empty
    [saver_i_jpp_kpp :: IHistorySaver7immutable [(t, pt[t], st[i,1+j,1+t]) | [t:<-[j..=k]]]]
        # nonempty
        # len == 1+k-j
        # first:(j, pt_j, st_i_jpp_jpp)
        # last:(k, pt_k, st_i_jpp_kpp)
        #saver_i_jpp_kpp{max_size7physical:=max4size4cache6batch, imay_max_size7apparent:=max4size4batch}

yield [i<=j<=k][0<=i<=j<=k<min(end6i,max4end)] => (imay_max4end6rho, jround, end6i, i, pt_i, saver_i_jpp_kpp)
    #saver_i_jpp_kpp{max4size4cache6batch, max4size4batch;head{j,pt_j}, last{k,pt_k}}
    #pt_i:required by rdiff7rho_
    #pt_j:pt[j]{j>=i}:to regenerate sts_i_jpp_kpp
    #pt_k:pt[k]{k>=j}:step7rho_
    #imay_max4end6rho:imay_max4num_steps6rho



'''#'''
#SparseHistorySaver7immutable(max_size7physical, imay_max_size7apparent, mark8no_check='!', data=None)
#   [data == (may_head, history_lnkls, size7physical, size7apparent, curr_size4step, remain_size4last_step)]
#   [mark8no_check === '!']
#




_method6IOps4RhoMethod7batch_ = mk_instance_method_decorator_(IOps4RhoMethod7batch)





@_method6IOps4RhoMethod7batch_
def iter_subsequents7rho7unlimit_(ops, i, pt_i, k, pt_k, st_i_jpp_kpp, /):
    while 1:
        kpp = 1+k
        pt_kpp = ops.step7rho_(pt_k)
        df_kpp = ops.rdiff7rho_(pt_i, pt_kpp)
        st_i_jpp_kpppp = ops.merge7rho_(st_i_jpp_kpp, df_kpp)
        yield (kpp, pt_kpp, st_i_jpp_kpppp)

        #next:
        k = kpp
        pt_k = pt_kpp
        st_i_jpp_kpp = st_i_jpp_kpppp
        #yield (k, pt_k, st_i_jpp_kpp)

@_method6IOps4RhoMethod7batch_
def mnext7rho7branched_(ops, imay_max4end6rho, record7old, /):
    'ops -> imay_max4end6rho -> record7old -> may ((False, record7next)|(True, record7old, record7old7reset))'
    (jround, jbatch, end6i, i, pt_i, saver_i_jpp_kpp) = record7old
    assert len(saver_i_jpp_kpp) >= 1
    # saver_i_jpp_kpp{max4size4cache6batch, max4size4batch;head{j,pt_j}, last{k,pt_k}}
    # imay_max4end6rho
    (k, pt_k, st_i_jpp_kpp) = saver_i_jpp_kpp.last
    if -1 != imay_max4end6rho <= k:raise Exception
    if ops.beyond7rho_(st_i_jpp_kpp):
        # [beyond7rho_(st_i_jpp_kpp{old})]
        return None
    # [not beyond7rho_(st_i_jpp_kpp{old})]

    kpp = 1+k
    b_detect7old = False
    if kpp == end6i:
        # or kpp == imay_max4end6rho:
        sz7next_round = ops.size4next_round_(jround, end6i-(1+i))
        if not sz7next_round > 0:raise Exception
        r'''[[[
        if 0b0000:
            end6k = kpp + sz7next_round
            # [end6k > kpp]
            st_k_kpp_kpp = ops.setup7rho_(pt_k)
            saver_k_kpp_kpp = saver_i_jpp_kpp.oo_clear().oo_append((k, pt_k, st_k_kpp_kpp), non_reproduceable_ok=True)
            if saver_k_kpp_kpp.full:raise Exception
            # [not saver_k_kpp_kpp.full]
            # [i:=k][j:=k]
            (jround, jbatch, end6i, i, pt_i, saver_i_jpp_kpp) = (1+jround, 0, end6k, k, pt_k, saver_k_kpp_kpp)
            # [end6i > kpp]
            # [not saver_i_jpp_kpp.full]
        else:
        #]]]'''#'''
        if 0x1111:
            # [i:=k][j:=k]
            (jround, jbatch, end6i, i, pt_i, saver_i_jpp_kpp) = ops.setup7rho7new_round_(1+jround, sz7next_round, k, pt_k, saver_i_jpp_kpp.oo_clear())
            # [end6i > kpp]
            # [not saver_i_jpp_kpp.full]
        # updated: (jround, jbatch, end6i, i, pt_i, saver_i_jpp_kpp)
        # [end6i > kpp]
        # [not saver_i_jpp_kpp.full]
        b_detect7old = True
    elif saver_i_jpp_kpp.full or kpp == imay_max4end6rho:
        # [end6i > kpp]
        # [saver_i_jpp_kpp.full]or[kpp == imay_max4end6rho]
        bnew_batch = saver_i_jpp_kpp.full
        saver_i_kpp_kpp = saver_i_jpp_kpp.oo_clear_but_last_()
        if saver_i_kpp_kpp.full:raise Exception
        # [not saver_i_kpp_kpp.full]
        # [j:=k]
        saver_i_jpp_kpp = saver_i_kpp_kpp
        # [not saver_i_jpp_kpp.full]
        # [end6i > kpp]
        jbatch += 1
        #jbatch += bnew_batch
        b_detect7old = True
    if not kpp < end6i:raise Exception
    if saver_i_jpp_kpp.full:raise Exception
    # [end6i > kpp]
    # [not saver_i_jpp_kpp.full]

    assert b_detect7old is (not (jround, jbatch) == record7old[:2] or kpp == imay_max4end6rho)
    if b_detect7old:
        record7old7reset = (jround, jbatch, end6i, i, pt_i, saver_i_jpp_kpp)
        # [b_detect7old is True]
        # [not beyond7rho_(st_i_jpp_kpp{old})]
        # [end6i > kpp]
        # [not saver_i_jpp_kpp.full]
        return (b_detect7old, record7old, record7old7reset)

    # [b_detect7old is False]
    # [end6i > kpp]
    # [not saver_i_jpp_kpp.full]
    pt_kpp = ops.step7rho_(pt_k)
    df_kpp = ops.rdiff7rho_(pt_i, pt_kpp)
    st_i_jpp_kpppp = ops.merge7rho_(st_i_jpp_kpp, df_kpp)
    saver_i_jpp_kpppp = saver_i_jpp_kpp.oo_append((kpp, pt_kpp, st_i_jpp_kpppp), non_reproduceable_ok=True)
    # [MAYBE:saver_i_jpp_kpppp.full]
    # [k:=1+k]
    k = kpp
    saver_i_jpp_kpp = saver_i_jpp_kpppp
    # [end6i > k]
    # [MAYBE:saver_i_jpp_kpp.full]
    assert len(saver_i_jpp_kpp) >= 2
    record7next = (jround, jbatch, end6i, i, pt_i, saver_i_jpp_kpp)
    # [b_detect7old is False]
    # [end6i > k]
    # [MAYBE:saver_i_jpp_kpp.full]
    return (b_detect7old, record7next)




@_method6IOps4RhoMethod7batch_
def setup7rho7new_round_(ops, jround7new, sz7new_round, k, pt_k, empty_saver7immutable, /):
    'ops -> jround7new/uint{>=0} -> sz7new_round{jround7new}/uint{>0} -> k/uint -> pt[k] -> IHistorySaver7immutable{len==0} -> record7new_round{jround7new}'
    sz7new_round
    if not sz7new_round > 0:raise Exception
    if not 0 == len(empty_saver7immutable):raise Exception
    kpp = 1+k
    end6k = kpp + sz7new_round
    # [end6k > kpp]
    st_k_kpp_kpp = ops.setup7rho_(pt_k)
    saver_k_kpp_kpp = empty_saver7immutable.oo_append((k, pt_k, st_k_kpp_kpp), non_reproduceable_ok=True)
    if saver_k_kpp_kpp.full:raise Exception
    # [not saver_k_kpp_kpp.full]
    # [i:=k][j:=k]
    record7new_round = (jround7new, 0, end6k, k, pt_k, saver_k_kpp_kpp)
        #  (jround7new, jbatch, end6i, i, pt_i, saver_i_jpp_kpp)
    # [end6i > kpp]
    # [not saver_i_jpp_kpp.full]
    return record7new_round


default_args4history_saver7immutable = (2049, 2049) #(max_size7physical, imay_max_size7apparent)
default_args4history_saver7immutable = (2049, -1) #(max_size7physical, imay_max_size7apparent)
@_method6IOps4RhoMethod7batch_
def gmk_default_empty_saver7immutable_(sf, may_empty_saver7immutable=None, /):
    '-> empty_saver7immutable/IHistorySaver7immutable{len==0}'
    if not None is may_empty_saver7immutable:
        empty_saver7immutable = may_empty_saver7immutable
        return empty_saver7immutable
    default_empty_saver7immutable = SparseHistorySaver7immutable(*default_args4history_saver7immutable)
    return default_empty_saver7immutable


@_method6IOps4RhoMethod7batch_
def iter7rho_(ops, imay_max4end6rho, pt_0, may_empty_saver7immutable, /):
    'ops -> imay_max4end6rho -> pt[0] -> may IHistorySaver7immutable{len==0} -> Iter ((10001, record7next)|(10002, record7old, oresult)|(10003, record7old, errmsg, record7old7reset)|(10009, record7old)) # [case{10002|10009} must be last if occurs]'
    record7new_round = ops.prepare4iter7rho_(pt_0, may_empty_saver7immutable)
    return ops.iter7rho__7resume_(imay_max4end6rho, record7new_round)
    return ops.iter7rho__7offseted_jround_(imay_max4end6rho, jround7new:=0, sz7new_round:=1, 0, pt_0, may_empty_saver7immutable)
    record7new_round = ops.prepare4iter7rho__7offseted_jround_(jround7new:=0, sz7new_round:=1, 0, pt_0, may_empty_saver7immutable)
    return ops.iter7rho__7resume_(imay_max4end6rho, record7new_round)
@_method6IOps4RhoMethod7batch_
def prepare4iter7rho_(ops, pt_0, may_empty_saver7immutable, /):
    'ops -> pt[0] -> may IHistorySaver7immutable{len==0} -> record7new_round'
    record7new_round = ops.prepare4iter7rho__7offseted_jround_(jround7new:=0, sz7new_round:=1, 0, pt_0, may_empty_saver7immutable)
    return record7new_round




@_method6IOps4RhoMethod7batch_
def iter7rho__7offseted_jround_(ops, imay_max4end6rho, jround7new, sz7new_round, k, pt_k, may_empty_saver7immutable, /):
    'ops -> imay_max4end6rho -> jround7new/uint{>=0} -> sz7new_round{jround7new}/uint{>0} -> k/uint -> pt[k] -> may IHistorySaver7immutable{len==0} -> Iter ((10001, record7next)|(10002, record7old, oresult)|(10003, record7old, errmsg, record7old7reset)|(10009, record7old)) # [case{10002|10009} must be last if occurs]'
    record7new_round = ops.prepare4iter7rho__7offseted_jround_(jround7new, sz7new_round, k, pt_k, may_empty_saver7immutable)
    return ops.iter7rho__7resume_(imay_max4end6rho, record7new_round)
@_method6IOps4RhoMethod7batch_
def prepare4iter7rho__7offseted_jround_(ops, jround7new, sz7new_round, k, pt_k, may_empty_saver7immutable, /):
    'ops -> jround7new/uint{>=0} -> sz7new_round{jround7new}/uint{>0} -> k/uint -> pt[k] -> may IHistorySaver7immutable{len==0} -> record7new_round'
    #empty_saver7immutable = ops.gmk_default_empty_saver7immutable_() if None is may_empty_saver7immutable else may_empty_saver7immutable
    empty_saver7immutable = ops.gmk_default_empty_saver7immutable_(may_empty_saver7immutable)
    record7new_round = ops.setup7rho7new_round_(jround7new, sz7new_round, k, pt_k, empty_saver7immutable)
    return record7new_round




@_method6IOps4RhoMethod7batch_
def iter7rho__7resume_(ops, imay_max4end6rho, record7old, /):
    'ops -> imay_max4end6rho -> record7old -> Iter ((10001, record7next)|(10002, record7old, oresult)|(10003, record7old, errmsg, record7old7reset)|(10009, record7old)) # [case{10002|10009} must be last if occurs]'
    if not -1 == imay_max4end6rho:
        max4end6rho = imay_max4end6rho
        (jround, jbatch, end6i, i, pt_i, saver_i_jpp_kpp) = record7old
        if max4end6rho <= record7old[3]:
            assert max4end6rho <= i
            if not i < max4end6rho:raise Exception
            raise 000

        r'''[[[
        CANCEL_1:
        ===
        if max4end6rho < record7old[2]:
            assert max4end6rho < end6i
            end6i = max4end6rho
            record7old = (jround, jbatch, end6i, i, pt_i, saver_i_jpp_kpp)
        if not i < end6i <= max4end6rho:raise Exception
        #]]]'''#'''

    # !! {hard to resume with large max4end6rho}:
    # CANCEL_1:record7old # maybe updated end6i
    # CANCEL_1:[[-1 =!= imay_max4end6rho] -> [end6i{record7old} <= max4end6rho]]

    strict = False
    while 1:
        # CANCEL_1:[[-1 =!= imay_max4end6rho] -> [end6i{record7old} <= max4end6rho]]
        match ops.mnext7rho7branched_(imay_max4end6rho, record7old):
            case None:
                # [beyond7rho_(st_i_jpp_kpp{old})]
                yield (10009, record7old)
                # stop{beyond/bad:no oresult after}
                return None
            case (False, record7next):
                # [b_detect7old is False]
                yield (10001, record7next)
                record7old = record7next
                777;strict = False
                continue
            case (True, record7old, record7old7reset):
                if strict:raise 000#dead_loop
                # [b_detect7old is True]
                # [not beyond7rho_(st_i_jpp_kpp{old})]
                # [end6i > kpp]
                # [not saver_i_jpp_kpp.full]
                pass
            case _:
                raise 000
        #end-match ops.mnext7rho7branched_(record7old):
        record7old, record7old7reset

        # [b_detect7old is True]
        # [not beyond7rho_(st_i_jpp_kpp{old})]
        # [end6i > kpp]
        # [not saver_i_jpp_kpp.full]
        (jround, jbatch, end6i, i, pt_i, saver_i_jpp_kpp) = record7old
        (k, pt_k, st_i_jpp_kpp) = saver_i_jpp_kpp.last
        # !! [not beyond7rho_(st_i_jpp_kpp{old})]
        eresult = ops.detect7rho_(st_i_jpp_kpp)
        match eresult:
            case (True, oresult):
                yield (10002, record7old, oresult)
                # stop{found:oresult}
                return None
            case (False, errmsg):
                pass
            case _:
                raise 000
        errmsg
        yield (10003, record7old, errmsg, record7old7reset)


        ###########################
        record7old7reset
        if -1 != imay_max4end6rho <= 1+(k:=record7old7reset[-1].last[0]):
            # [max4end6rho <= 1+k]
            assert max4end6rho == 1+k
            # [max4end6rho == 1+k]
            # stop{hit:max4end6rho}
            return None
        r'''[[[
        CANCEL_1:
        ===
        # to update:end6i{record7old7reset}
        if 1+record7old[0] == record7old7reset[0] and not -1 == imay_max4end6rho and max4end6rho < record7old7reset[2]:
            # new round
            (jround, jbatch, end6i, i, pt_i, saver_i_jpp_kpp) = record7old7reset
            # !! new round
            assert i == k
            # [i == k]
            # !! [end6i > kpp]
            # [end6i > 1+k==1+i]
            assert max4end6rho < end6i
            if not i < max4end6rho:raise Exception
            if 1+i == max4end6rho:
                # stop{hit:max4end6rho}
                return None
            # [1+i < max4end6rho]

            end6i = max4end6rho
            # [1+i < end6i{new} <= max4end6rho]
            # !! [i == k]
            # [end6i{new} > kpp] # postcondition
            # [end6i{new} <= max4end6rho] # postcondition
            record7old7reset = (jround, jbatch, end6i, i, pt_i, saver_i_jpp_kpp) # update end6i
        record7old7reset # maybe updated end6i{record7old7reset}
        # CANCEL_1:[[-1 =!= imay_max4end6rho] -> [end6i{record7old7reset} <= max4end6rho]]
        #]]]'''#'''
        # [end6i > kpp]
        # [not saver_i_jpp_kpp.full]
        ###########################
        record7old = record7old7reset
        777;strict = True#avoid:dead_loop
        # CANCEL_1:[[-1 =!= imay_max4end6rho] -> [end6i{record7old} <= max4end6rho]]
        continue
    #end-while 1:
    raise 000






@_method6IOps4RhoMethod7batch_
def try_search_oresult7rho__7resume_(ops, imay_max4end6rho, record7old, /):
    '-> (final/bool, tmay_oresult, record7old)'
    (jround, jbatch, end6i, i, pt_i, saver_i_jpp_kpp) = record7old
    assert len(saver_i_jpp_kpp) >= 1
    (k, pt_k, st_i_jpp_kpp) = saver_i_jpp_kpp.last
    if ops.beyond7rho_(st_i_jpp_kpp):
        rank = +1
        m = (10009, record7old)
    elif (x:=ops.detect7rho_(st_i_jpp_kpp)).is_right:
        oresult = x.right
        rank = 0
        m = (10002, record7old, oresult)
    else:
        rank = -1
        m = (10001, record7old)
    rank, m

    if not -1 == rank:
        m
        #if 0b0001:print(m)
        return _finalize4try_search_oresult7rho_(ops, imay_max4end6rho, m)

    m
    try:
        it = ops.iter7rho__7resume_(imay_max4end6rho, record7old)
        for m in it:
            #if 0b0001:print(m)
            pass
        m
        return _finalize4try_search_oresult7rho_(ops, imay_max4end6rho, m)
    except KeyboardInterrupt as exc:
        raise _on_error7try_search_oresult7rho_(ops, imay_max4end6rho, m, exc)

@_method6IOps4RhoMethod7batch_
def try_search_oresult7rho_(ops, imay_max4end6rho, pt_0, may_empty_saver7immutable, /):
    '-> (final/bool, tmay_oresult, record7old)'
    m = None
    try:
        it = ops.iter7rho_(imay_max4end6rho, pt_0, may_empty_saver7immutable)
        for m in it:
            #if 0b0001:print(m)
            pass
        m
        return _finalize4try_search_oresult7rho_(ops, imay_max4end6rho, m)
    except KeyboardInterrupt as exc:
        raise _on_error7try_search_oresult7rho_(ops, imay_max4end6rho, m, exc)

def _finalize4try_search_oresult7rho_(ops, imay_max4end6rho, m, /):
    '-> (final/bool, tmay_oresult, record7old)'
    #print(m)
    match m:
        case None:
            raise Exception(imay_max4end6rho)
        case (10001, record7next):
            record7export = record7next
            tmay_oresult = ()
            ok = False
        case (10003, record7old, errmsg, record7old7reset):
            record7export = record7old7reset
            tmay_oresult = ()
            ok = False
        case (10002, record7old, oresult):
            record7export = record7old
            tmay_oresult = (oresult,)
            ok = True
        case (10009, record7old):
            record7export = record7old
            tmay_oresult = ()
            ok = True
        case _:
            raise Exception(m)
    ok
    record7export

    final = ok
    return (final, tmay_oresult, record7export)
    k = record7export[-1].last[0]
    return (final, tmay_oresult, k, record7export)



def _on_error7try_search_oresult7rho_(ops, imay_max4end6rho, m, exc, /):
    #repack_exception_
    raise KeyboardInterrupt(exc, m)









class IOps4RhoMethod7batch__7factor_pint(IOps4RhoMethod7batch):
    __slots__ = ()
    @property
    @abstractmethod
    def modulus(sf, /):
        '-> modulus/int{>=2}'
        # !! [[modulus:=0] -> [beyond7rho_(st_i_jpp_jpp)]]

    @abstractmethod
    def step7rho_(sf, pt_k, /):
        'pt[k] -> pt[1+k]'


    @override
    def rdiff7rho_(sf, pt_i, pt_kpp, /):
        df_i_kpp = (pt_kpp - pt_i) %sf.modulus
        return df_i_kpp
    @override
    def setup7rho_(sf, pt_i, /):
        st_i_jpp_jpp = 1
        return st_i_jpp_jpp
    @override
    def merge7rho_(sf, st_i_jpp_kpp, df_i_kpp, /):
        st_i_jpp_kpppp = (st_i_jpp_kpp * df_i_kpp) %sf.modulus
        return st_i_jpp_kpppp
    @override
    def beyond7rho_(sf, st_i_jpp_kpp, /):
        return st_i_jpp_kpp == 0
    @override
    def detect7rho_(sf, st_i_jpp_kpp, /):
        ft = gcd(sf.modulus, st_i_jpp_kpp)
        if 1 < ft:
            if not ft < sf.modulus: raise 000
            return mk_Right(ft)
        if not 1 == ft: raise 000

        return mk_Left('coprime')
    @override
    def size4next_round_(sf, jround, size4curr_round, /):
        return 2*size4curr_round


class IOps4RhoMethod7batch__7factor_pint__7even_exp_add_constant(IOps4RhoMethod7batch__7factor_pint):
    __slots__ = ()
    @property
    @abstractmethod
    def addend(sf, /):
        '-> int{[addend%modulus=!=0]}'
    @property
    @abstractmethod
    def even_exp(sf, /):
        '-> assumed_factor4phi4modulus/int{>0}{%2==0} # assume [1 < gcd(phi_(modulus), assumed_factor4phi4modulus)]'

    @override
    def step7rho_(sf, pt_k, /):
        M = sf.modulus
        even_exp = sf.even_exp # assumed_factor4phi4modulus
        pt_kpp = (sf.addend +pow(pt_k, even_exp, M)) %M
        return pt_kpp

class Ops4RhoMethod7batch__7factor_pint__7even_exp_add_constant(IOps4RhoMethod7batch__7factor_pint__7even_exp_add_constant):
    ___no_slots_ok___ = True
    def __init__(sf, modulus, even_exp, addend, /):
        check_int_ge(2, modulus)
        check_int_ge(2, even_exp)
        check_type_is(int, addend)
        if not even_exp&1 == 0:raise ValueError(even_exp)
        if not abs(addend) < modulus:
            addend = addend%modulus
            if 2*addend > modulus:
                addend -= modulus
        sf._m = modulus
        sf._e = even_exp
        sf._a = addend
        sf._args = (modulus, even_exp, addend)
    def __repr__(sf, /):
        (modulus, even_exp, addend) = sf._args
        return repr_helper(sf, modulus, even_exp, addend)


    @property
    @override
    def modulus(sf, /):
        return sf._m

    @property
    @override
    def even_exp(sf, /):
        return sf._e

    @property
    @override
    def addend(sf, /):
        return sf._a












IOps4RhoMethod7batch__7factor_pint
_method6IOps4RhoMethod7batch__7factor_pint_ = mk_instance_method_decorator_(IOps4RhoMethod7batch__7factor_pint)

@_method6IOps4RhoMethod7batch__7factor_pint_
def try_factor_pint7rho__7resume_(ops, imay_max4end6rho, record7old, /):
    'ops -> imay_max4end6rho -> record7old -> (final, some_proper_factors, idc, record7old)'
    (final, tmay_oresult, record7old) = ops.try_search_oresult7rho__7resume_(imay_max4end6rho, record7old)
    return _2_finalize4try_factor_pint7rho_(ops, final, tmay_oresult, record7old)
@_method6IOps4RhoMethod7batch__7factor_pint_
def try_factor_pint7rho_(ops, imay_max4end6rho, u0_or_scale, may_empty_saver7immutable, /, *, u0_be_floor_sqrt_scale_modulus=False):
    'ops -> imay_max4end6rho -> (u0/int|scale/uint{>0}) -> may IHistorySaver7immutable{len==0} -> (final, some_proper_factors, idc, record7old)'
    pt_0 = ops.prepare4try_factor_pint7rho_(u0_or_scale, u0_be_floor_sqrt_scale_modulus=u0_be_floor_sqrt_scale_modulus)
    (final, tmay_oresult, record7old) = ops.try_search_oresult7rho_(imay_max4end6rho, pt_0, may_empty_saver7immutable)
    return _2_finalize4try_factor_pint7rho_(ops, final, tmay_oresult, record7old)
@_method6IOps4RhoMethod7batch__7factor_pint_
def prepare4try_factor_pint7rho_(ops, u0_or_scale, /, *, u0_be_floor_sqrt_scale_modulus=False):
    'ops -> (u0/int|scale/uint{>0}) -> pt[0]/uint%modulus'
    if u0_be_floor_sqrt_scale_modulus:
        scale = u0_or_scale
        check_int_ge(1, scale)
        u0 = isqrt(scale*ops.modulus)
    else:
        u0 = u0_or_scale
    u0
    pt_0 = u0 %ops.modulus
    return pt_0
def _finalize4try_factor_pint7rho_(ops, imay_max4end6rho, m, /):
    #def _finalize4try_factor_pint7rho_(ops, imay_max4end6rho, u0, may_empty_saver7immutable, pt_0, m, /):
    '-> (final, some_proper_factors, idc, record7old)'
    (final, tmay_oresult, record7old) = _finalize4try_search_oresult7rho_(ops, imay_max4end6rho, m)
    return _2_finalize4try_factor_pint7rho_(ops, final, tmay_oresult, record7old)
def _2_finalize4try_factor_pint7rho_(ops, final, tmay_oresult, record7old, /):
    '-> (final, some_proper_factors, idc, record7old)'
    if not final:
        record7old
        assert not tmay_oresult
        some_proper_factors = ()
        js = ()
    else:
        record7old
        tmay_oresult
        (js, some_proper_factors) = ops.postprocess7factor_pint7rho_(record7old, tmay_oresult)
        assert some_proper_factors or tmay_oresult is None
    return (final, some_proper_factors, js, record7old)
    return (final, some_proper_factors, record7old)



@_method6IOps4RhoMethod7batch__7factor_pint_
def postprocess7factor_pint7rho_(ops, record7old, tmay_oresult, /):
    '[case<-{10002,10009}] => ... -> ([idx], [proper_factor{modulus}])'
    def iter_subsequents_(history, /):
        (k, pt_k, st_i_jpp_kpp) = history
        return ops.iter_subsequents7rho7unlimit_(i, pt_i, k, pt_k, st_i_jpp_kpp)
    iter_subsequents_

    (jround, jbatch, end6i, i, pt_i, saver_i_jpp_kpp) = record7old
    #(k, pt_k, st_i_jpp_kpp) = saver_i_jpp_kpp.last
    (j, pt_j, st_i_jpp_jpp) = saver_i_jpp_kpp.head
    777;offset = j

    st7fold7fwd = (N:=ops.modulus, div_M_N:=1, fts:=mk_rglnkls_())
    _ops7fwd = _Ops4postprocess7factor_pint_(ops.modulus, i, pt_i)
    (st7fold7fwd, ls4left_transition) = saver_i_jpp_kpp.forward_search_key_points_(_ops7fwd.stZhistory2rank7fwd_, _ops7fwd.op4fold7fwd_, st7fold7fwd, offset=offset, may_iter_subsequents_=iter_subsequents_)
    js = []
    for ((jmm, history6jmm, rank6jmm), (j, history6j, rank6j)) in ls4left_transition:
        assert rank6jmm == -1
        assert 0 <= rank6j <= +1
        (_j, pt_j, _st) = history6j
        if not _j == j:raise Exception
        js.append(j)
    js = tuple(js)
    (N, div_M_N, fts) = st7fold7fwd
    assert N*div_M_N == ops.modulus
    fts = tuple(sorted(set(list7up_(fts))))
    #xxx:assert fts[0] == oresult
    assert fts or not tmay_oresult
    return (js, fts)
    return fts
class _Ops4postprocess7factor_pint_:
    r'''[[[
    # !! IHistorySaver::forward_search_key_points_(sf, stZhistory2rank7fwd_, op4fold7fwd_, st7fold7fwd, /, *, offset=0, _max_size7dense_6SparseHistorySaver=2049, _max_size7physical_6SparseHistorySaver=65537, may_iter_subsequents_=None):
        '[sf.size7apparent > 0][stZhistory2rank_(st7fold)(sf.head) == -1] => ... -> (st7fold, [((-1+offset4key_point, history{-1+offset4key_point}, -1), (offset4key_point, history{offset4key_point}, (0|+1)))]) | ^EmptyError@{not$[sf.size7apparent > 0]} | ^ValueError@{not$[stZhistory2rank_(st7fold)(sf.head) == -1]} # typing{args}:see above:IHistorySaverBase.__doc__ # [op4fold7fwd_::op4fold_{forward_search}]'

    [stZhistory2rank_ :: st7fold{k} -> history2rank_{k}]
        # stZhistory2rank7fwd_
    [history2rank_{k} :: history -> (-1|0|+1)]
    [forward_search => [history2rank_{k}(history{j}) >= history2rank_{1+k}(history{j})]]
        # history2rank7fwd_
    [op4fold_{forward_search} :: [[history2rank_{k}(history{-1+j}) == -1][history2rank_{k}(history{j}) >= 0]] => prev_history6key_point/history{-1+j} -> j/uint%(offset+size7apparent) -> history6key_point/history{j} -> st7fold{k} -> st7fold{1+k}{forward_search => [history2rank_{1+k}(history{j}) == -1]}]
        # op4fold7fwd_

    #]]]'''#'''
    def __init__(sf, modulus, i, pt_i, /):
        sf.modulus = modulus
        sf.i = i
        sf.pt_i = pt_i
    def stZhistory2rank7fwd_(sf, st7fold7fwd):
        (N, div_M_N, fts) = st7fold7fwd
        def history2rank7fwd_(history, /):
            (k, pt_k, st_i_jpp_kpp) = history
            if N == 1:
                return -1
            st_i_jpp_kpp %= N
            if 0 == st_i_jpp_kpp:
                return +1
            ft = gcd(N, st_i_jpp_kpp)
            return -1 if 1==ft else 0
        return history2rank7fwd_
    def op4fold7fwd_(sf, prev_history6key_point, jh, history6key_point, st7fold7fwd):
        # [history2rank_{jr,st7fold7fwd}(prev_history6key_point) == -1]
        # [history2rank_{jr,st7fold7fwd}(history6key_point) >= 0]
        (N, div_M_N, fts) = st7fold7fwd
        (k, pt_k, st_i_jpp_kpp) = history6key_point
        assert k == jh
        #st_i_jpp_kpp %= N
        #ft = gcd(N, st_i_jpp_kpp)
        i = sf.i
        pt_i = sf.pt_i
        assert k > i
        df_i_k = pt_k -pt_i
        ft = gcd(N, df_i_k)
        assert 1 < ft <= N, (ft, N)
        #bug:assert 1 < ft < N, (ft, N)
        d = N if ft == N else ft*noncoprime_part_of_to_(N//ft, ft)
        _st7fold7fwd = (N//d, d*div_M_N, oo_push_(fts, ft))
        # [history2rank_{1+jr,_st7fold7fwd}(history6key_point) == -1]
        return _st7fold7fwd






__all__

from seed.algo.rho_method__7iter7batch import \
(IOps4RhoMethod7batch
,   mnext7rho7branched_
,   setup7rho7new_round_
,   iter7rho_
,       prepare4iter7rho_
,   iter7rho__7offseted_jround_
,       prepare4iter7rho__7offseted_jround_
,   iter7rho__7resume_
#
,   gmk_default_empty_saver7immutable_
,       default_args4history_saver7immutable
,   iter_subsequents7rho7unlimit_
,   try_search_oresult7rho__7resume_
,   try_search_oresult7rho_
#
,   IOps4RhoMethod7batch__7factor_pint
,       try_factor_pint7rho_
,           prepare4try_factor_pint7rho_
,       try_factor_pint7rho__7resume_
,       postprocess7factor_pint7rho_
)

from seed.algo.rho_method__7iter7batch import \
(IOps4RhoMethod7batch
,   IOps4RhoMethod7batch__7factor_pint
,       IOps4RhoMethod7batch__7factor_pint__7even_exp_add_constant
,           Ops4RhoMethod7batch__7factor_pint__7even_exp_add_constant
)

from seed.algo.rho_method__7iter7batch import Ops4RhoMethod7batch__7factor_pint__7even_exp_add_constant, try_factor_pint7rho_, try_factor_pint7rho__7resume_
#.Ops4RhoMethod7batch__7factor_pint__7even_exp_add_constant(modulus, even_exp, addend)
#.def try_factor_pint7rho_(ops, imay_max4end6rho, u0_or_scale, may_empty_saver7immutable, /, *, u0_be_floor_sqrt_scale_modulus=False):
#.  '-> (final, some_proper_factors, idc, record7old)'
#.def try_factor_pint7rho__7resume_(ops, imay_max4end6rho, record7old, /):
#.  '-> (final, some_proper_factors, idc, record7old)'
#.  (jround, jbatch, end6i, i, pt_i, saver_i_jpp_kpp) = record7old
#.  (k, pt_k, st_i_jpp_kpp) = saver_i_jpp_kpp.last

from seed.algo.rho_method__7iter7batch import *
