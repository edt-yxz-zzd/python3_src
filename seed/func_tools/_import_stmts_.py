
#.flatten_recur = lazy_import4func_('seed.iters.flatten_recur', 'flatten_recur', __name__)
from seed.iters.flatten_recur import flatten_recur
# def flatten_recur(g:Generator, /, *, value:object=None, is_exc=False, boxed=False):
#
# [flatten_recur :: recur_GI -> final_result]
#   [recur_GI == GI{yield{recur_GI}; return{final_result if not boxed else (Either recur_GI final_result)}}]












from seed.func_tools.recur5yield__strict import BoxedTailRecur, BoxedFinalResult
from seed.func_tools.recur5yield__strict import IDecorator4recur5yield, Decorator4recur5yield
from seed.func_tools.recur5yield__strict import IExecutor4recur5yield, IExecutor4recur5yield__dispatch_by_dict, Executor4recur5yield__dispatch_by_dict

######################
# Decorator4recur5yield(executor4recur5yield)(wrapped) :: (*args) -> (**kwds) -> final_result
#
# Decorator4recur5yield(executor4recur5yield) :: wrapped -> wrapper
#   [wrapped/main_prepare_func :: (*args) -> (**kwds) -> (st, exprlist5yield)]
#   [wrapper/expected_main_recur_func :: (*args) -> (**kwds) -> final_result<_main_generator_func_>]

######################
# IExecutor4recur5yield <==> (emplace_stack_ops, child_gi_protocol, tail_recur_gi_protocol){==params{IDecorator4recur5yield}}
#
# Executor4recur5yield__dispatch_by_dict(may_emplace_stack_ops, using_tail_recur_gi_protocol, _allow__gi2gi_, may_type2attr_or_child_gi_protocol)
#   [using_tail_recur_gi_protocol :: bool]
#   [_allow__gi2gi_ :: bool]
#   [may_emplace_stack_ops :: may IEmplaceStackOps]
#   [may_type2attr_or_child_gi_protocol :: may {type:(attr|child_gi_protocol)}]
#       [child_gi_protocol :: exprlist5yield -> GI]
######################
if 0:
    r'''
    (emplace_stack_ops, child_gi_protocol, tail_recur_gi_protocol) -> decorator

    decorator :: main_prepare_func -> expected_main_recur_func
    expected_main_recur_func :: (*args4main, **kwds4main) -> main_result
    main_result = result5recur<main_generator_iterator>

    main_prepare_func(*args4main, **kwds4main) -> (st, main-exprlist5yield)
        child_gi_protocol := _st_and_type2child_gi_protocol_(st, type(exprlist5yield))
    main_generator_iterator := child_gi_protocol(main-exprlist5yield)
    main_generator_iterator :: GI
    GI == GeneratorIterator<iter-exprlist5yield, return-result5return>

    emplace_stack_ops :: IEmplaceStackOps
    child_gi_protocol(exprlist5yield) -> GI
    tail_recur_gi_protocol(result5return) -> either_tailrecur_result
    either_tailrecur_result === (is_result5recur, payload) :: ((False, exprlist5yield)|(True, result5recur))
    #'''
######################
if 0:
    r'''
#both: +_allow__gi2gi_

-using_tail_recur_gi_protocol
>>> dr1 = Decorator4recur5yield(Executor4recur5yield__dispatch_by_dict(None, False, True, None))

+using_tail_recur_gi_protocol
>>> dr2 = Decorator4recur5yield(Executor4recur5yield__dispatch_by_dict(None, True, True, None))


>>> st = None
>>> @dr1
... def main1(m, n, /):
...     return (st, _main1(m, n))
>>> def _main1(m, n, /):
...     if n == 0:
...         return (m)
...     _m = yield _inc(m)
...     r = yield _main1(_m, n-1)
...     return r
...     return (yield _main1((yield _inc(m)), n-1))
...     777;    yield
>>> def _inc(m, /):
...     return (m+1)
...     777;    yield
>>> main1(0, 999)
999


>>> st = None
>>> @dr2
... def main2(m, n, /):
...     #bug:return (st, BoxedTailRecur(_main2(m, n)))
...     return (st, _main2(m, n))
>>> def _main2(m, n, /):
...     if n == 0:
...         return BoxedFinalResult(m)
...     return BoxedTailRecur(_main2((yield _inc(m)), n-1))
...     777;    yield
>>> def _inc(m, /):
...     return BoxedFinalResult(m+1)
...     777;    yield
>>> main2(0, 10000)
10000


    #'''
######################

