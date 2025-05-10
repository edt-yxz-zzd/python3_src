#__all__:goto
r'''[[[
e ../../python3_src/seed/func_tools/recur5yield__strict.py
    ++check_type_is

seed.func_tools.recur5yield__strict
py -m nn_ns.app.debug_cmd   seed.func_tools.recur5yield__strict -x
py -m nn_ns.app.doctest_cmd seed.func_tools.recur5yield__strict:__doc__ -ht



[[

see also:
    seed.iters.flatten_recur
        view ../../python3_src/seed/iters/flatten_recur.py
    seed.func_tools.recur5yield
        view ../../python3_src/seed/func_tools/recur5yield.py
]]




#def Executor4recur5yield__dispatch_by_dict.__init__(sf, may_emplace_stack_ops, using_tail_recur_gi_protocol, _allow__gi2gi_, may_type2attr_or_child_gi_protocol, /):
>>> dr1 = Decorator4recur5yield(Executor4recur5yield__dispatch_by_dict(None, False, True, None))
>>> dr2 = Decorator4recur5yield(Executor4recur5yield__dispatch_by_dict(None, True, True, None))


>>> st = None
>>> @dr1
... def main1(m, n, /):
...     return (st, _main1(m, n))
>>> def _main1(m, n, /):
...     if n == 0:
...         return (m)
...     _m = yield _inc(m)
...     r = yield from _main1(_m, n-1) #counterexample
...     return r
...     return (yield from _main1((yield _inc(m)), n-1)) #counterexample
...     777;    yield
>>> def _inc(m, /):
...     return (m+1)
...     777;    yield
>>> main1(0, 999) #counterexample
Traceback (most recent call last):
    ...
RecursionError: maximum recursion depth exceeded




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





#]]]'''
__all__ = r'''
BoxedTailRecur
BoxedFinalResult

IExecutor4recur5yield
    IExecutor4recur5yield__dispatch_by_dict
        Executor4recur5yield__dispatch_by_dict

IPrepare4recur5yield
    IDecorator4recur5yield
        Decorator4recur5yield

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
if 1:
    from seed.types.ops.IEmplaceStackOps import IEmplaceStackOps
    from seed.types.ops.IEmplaceStackOps import the_emplace_stack_ops4list, the_emplace_stack_ops4HugeStack
from seed.func_tools.recur5yield import recur5yield__decoratorT__all_gi_protocols# child_gi_protocol__echo, child_gi_protocol__0func, child_gi_protocolT__0func5ref, tail_recur_gi_protocol__echo, tail_recur_gi_protocol__off

from functools import update_wrapper, wraps
from types import GeneratorType

from seed.types.Either import Either
from seed.tiny_.check import check_type_is, check_type_le, check_non_ABC, check_subscriptable, check_callable
from seed.tiny import echo, ifNone, null_mapping_view, print_err
from seed.helper.repr_input import repr_helper
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
___end_mark_of_excluded_global_names__0___ = ...

class _BoxedXxx:
    def __init__(sf, xxx, /):
        sf._x = xxx
    def unbox(sf, /):
        '-> xxx'
        return sf._x
    def __repr__(sf, /):
        return repr_helper(sf, sf.unbox())

class _IBoxed8Either(_BoxedXxx):
    def __iter__(sf, /):
        yield sf.case
        yield sf.unbox()
class BoxedTailRecur(_IBoxed8Either):
    'boxed_tail_recur:[xxx:=raw_tail_recur]'
    case = False
class BoxedFinalResult(_IBoxed8Either):
    'boxed_final_result:[xxx:=raw_final_result]'
    case = True



class IExecutor4recur5yield(ABC):
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
    #see:def recur5yield__decoratorT__all_gi_protocols(emplace_stack_ops, child_gi_protocol, tail_recur_gi_protocol, /):
    #see:def recur5yield__eval__main_generator_iterator(emplace_stack_ops, main_generator_iterator, child_gi_protocol, tail_recur_gi_protocol, /):
    __slots__ = ()

    @property
    @abstractmethod
    def _emplace_stack_ops_(sf, /):
        '-> emplace_stack_ops/IEmplaceStackOps'

    @property
    @abstractmethod
    def _using_tail_recur_gi_protocol_(sf, /):
        '-> bool # [True=>[result5return::(BoxedTailRecur exprlist5yield | BoxedFinalResult result5recur)]]'

    @abstractmethod
    def _st_and_type2child_gi_protocol_(sf, st, typ, /):
        'st -> type(exprlist5yield) -> child_gi_protocol/(exprlist5yield->GI)'

    def run_(sf, st, exprlist5yield, /):
        'st -> exprlist5yield -> result5recur'
        result5recur = _run(sf._emplace_stack_ops_, sf._using_tail_recur_gi_protocol_, sf._st_and_type2child_gi_protocol_, st, exprlist5yield)
        return result5recur

_Ts = (BoxedTailRecur, BoxedFinalResult)
#def _run(ops, _using_tail_recur_gi_protocol_, _st_and_type2child_gi_protocol_, main_gi, /):
def _run(ops, _using_tail_recur_gi_protocol_, _st_and_type2child_gi_protocol_, st, _0exprlist5yield, /):
    check_type_le(IEmplaceStackOps, ops)

    ######################
    if _using_tail_recur_gi_protocol_:
        def tail_recur_gi_protocol(result5return, /):
            '-> ((False, exprlist5yield)|(True, result5recur))'
            T = type(result5return)
            if T in _Ts:
                return result5return
            raise TypeError('not (BoxedTailRecur|BoxedFinalResult):', T)
            ## ###########
            ## if T is BoxedTailRecur:
            ##     #exprlist5yield = result5return.unbox()
            ##     return result5return
            ## if T is BoxedFinalResult:
            ##     #result5recur = result5return.unbox()
            ##     return result5return
            ## raise TypeError('not (BoxedTailRecur|BoxedFinalResult):', T)
    else:
        def tail_recur_gi_protocol(result5return, /):
            '-> (True, result5recur)'
            result5recur = result5return
            return (True, result5recur)
    ######################
    def child_gi_protocol(exprlist5yield, /):
        child_gi_protocol = _st_and_type2child_gi_protocol_(st, type(exprlist5yield))
        return child_gi_protocol(exprlist5yield)
    ######################
    init_value4send = None #const
    def push_ex(stack, exprlist5yield, /):
        gi = child_gi_protocol(exprlist5yield)
        push_gi(stack, gi)
    def push_gi(stack, gi, /):
        #if not isinstance(gi, GeneratorIterator): raise TypeError
        gi.send
        ops.push(stack, gi)
        ops.push(stack, init_value4send)
    ######################

    def main():
        stack = ops.mk_empty_stack()
            # :: [gi..., value4send]
        #push_gi(stack, main_gi)
        push_ex(stack, _0exprlist5yield)
        while 1:
            value4send = ops.pop(stack)
            if ops.is_empty(stack):
                main_result = value4send
                break
            gi = ops.get_top(stack)
            try:
                exprlist5yield = gi.send(value4send)
                    #raise StopIteration(result5return)
            except StopIteration as e:
                result5return = e.value
                ops.pop(stack)
                (is_result5recur, payload) = tail_recur_gi_protocol(result5return)
                if is_result5recur:
                    result5recur = payload
                    ops.push(stack, result5recur)
                    #if 0b0001:print_err('result5recur', result5recur)
                else:
                    exprlist5yield = payload
                    push_ex(stack, exprlist5yield)
            else:
                push_ex(stack, exprlist5yield)
            #end-try
        else:#while
            main_result
        #end-while:

        return main_result
    ######################
    return main()
#end-def _run(ops, _using_tail_recur_gi_protocol_, _st_and_type2child_gi_protocol_, st, _0exprlist5yield, /):
#end-class IExecutor4recur5yield(ABC):


class IPrepare4recur5yield(ABC):
    __slots__ = ()
    @abstractmethod
    def _prepare4recur5yield_(sf, /, *args, **kwds):
        '... -> (st, exprlist5yield)'
    def _call_on_(sf, executor4recur5yield, /, *args, **kwds):
        (st, exprlist5yield) = sf._prepare4recur5yield_(*args, **kwds)
        result5recur = executor4recur5yield.run_(st, exprlist5yield)
        return result5recur
class IDecorator4recur5yield(IPrepare4recur5yield):
#class IDecorator4recur5yield(ABC):
    __slots__ = ()
    @property
    @abstractmethod
    def _executor4recur5yield_(sf, /):
        '-> executor4recur5yield/IExecutor4recur5yield'
    @override
    def _prepare4recur5yield_(sf, wrapped, /, *_args, **kwds):
        '... -> (st, exprlist5yield)'
        (st, exprlist5yield) = wrapped(*_args, **kwds)
        return (st, exprlist5yield)
    def __call__(sf, wrapped, /):
        'wrapped/main_prepare_func/(... -> (st, exprlist5yield)) -> final_result<_main_generator_func_>'
        wrapped : 'main_prepare_func'
        wrapper : 'expected_main_recur_func'
        @wraps(wrapped)#update_wrapper(wrapper, wrapped)
        def wrapper(*_args, **kwds):
            return sf._call_on_(sf._executor4recur5yield_, wrapped, *_args, **kwds)
        return wrapper
#end-class IDecorator4recur5yield(ABC):



class IExecutor4recur5yield__dispatch_by_dict(IExecutor4recur5yield):
    __slots__ = ()
    @property
    @abstractmethod
    def _allow__gi2gi_(sf, /):
        '-> bool # default treatment when missing child_gi_protocol'

    @property
    @abstractmethod
    def _type2attr_or_child_gi_protocol_(sf, /):
        '-> {type(exprlist5yield): (attr/method_name4st/str|child_gi_protocol/(exprlist5yield->GI))}'

    @override
    def _st_and_type2child_gi_protocol_(sf, st, typ, /):
        'st -> type(exprlist5yield) -> child_gi_protocol/(exprlist5yield->GI)'
        Nothing = object()
        nm_or_f = sf._type2attr_or_child_gi_protocol_.get(typ, Nothing)
        if nm_or_f is Nothing:
            if not sf._allow__gi2gi_:raise TypeError(typ)
            if not hasattr(typ, 'send'):raise TypeError(typ)
            return echo #GI->GI
        elif type(nm_or_f) is str:
            nm = nm_or_f
            f = getattr(st, nm)
        else:
            f = nm_or_f
        f
        return (child_gi_protocol:=f)

#end-class IExecutor4recur5yield__dispatch_by_dict(IExecutor4recur5yield):

class Executor4recur5yield__dispatch_by_dict(IExecutor4recur5yield__dispatch_by_dict):
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        return repr_helper(sf, sf._emplace_stack_ops_, sf._using_tail_recur_gi_protocol_, sf._ty2nm_or_f)
    def __init__(sf, may_emplace_stack_ops, using_tail_recur_gi_protocol, _allow__gi2gi_, may_type2attr_or_child_gi_protocol, /):
        check_type_is(bool, using_tail_recur_gi_protocol)
        check_type_is(bool, _allow__gi2gi_)
        emplace_stack_ops = ifNone(may_emplace_stack_ops, the_emplace_stack_ops4list)
        check_type_le(IEmplaceStackOps, emplace_stack_ops)
        type2attr_or_child_gi_protocol = ifNone(may_type2attr_or_child_gi_protocol, null_mapping_view)
        check_subscriptable(type2attr_or_child_gi_protocol)

        sf._ops = emplace_stack_ops
        sf._b_tr = using_tail_recur_gi_protocol
        sf._b_g2g = _allow__gi2gi_
        sf._ty2nm_or_f = type2attr_or_child_gi_protocol
    @property
    @override
    def _emplace_stack_ops_(sf, /):
        '-> emplace_stack_ops/IEmplaceStackOps'
        return sf._ops

    @property
    @override
    def _using_tail_recur_gi_protocol_(sf, /):
        '-> bool # [True=>[result5return::(BoxedTailRecur exprlist5yield | BoxedFinalResult result5recur)]]'
        return sf._b_tr

    @property
    @override
    def _allow__gi2gi_(sf, /):
        '-> bool # default treatment when missing child_gi_protocol'
        return sf._b_g2g

    @property
    @override
    def _type2attr_or_child_gi_protocol_(sf, /):
        '-> {type(exprlist5yield): (attr/method_name4st/str|child_gi_protocol/(exprlist5yield->GI))}'
        return sf._ty2nm_or_f
#end-class Executor4recur5yield__dispatch_by_dict(IExecutor4recur5yield__dispatch_by_dict):
check_non_ABC(Executor4recur5yield__dispatch_by_dict)




class Decorator4recur5yield(IDecorator4recur5yield):
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        return repr_helper(sf, sf._emplace_stack_ops_, sf._using_tail_recur_gi_protocol_, sf._ty2nm_or_f)
    def __init__(sf, executor4recur5yield, /):
        check_type_le(IExecutor4recur5yield, executor4recur5yield)
        sf._exe = executor4recur5yield
    @property
    @override
    def _executor4recur5yield_(sf, /):
        '-> executor4recur5yield/IExecutor4recur5yield'
        return sf._exe
#end-class Decorator4recur5yield(IDecorator4recur5yield):
check_non_ABC(Decorator4recur5yield)







__all__
from seed.func_tools.recur5yield__strict import BoxedTailRecur, BoxedFinalResult

from seed.func_tools.recur5yield__strict import IDecorator4recur5yield, Decorator4recur5yield

from seed.func_tools.recur5yield__strict import IExecutor4recur5yield, IExecutor4recur5yield__dispatch_by_dict, Executor4recur5yield__dispatch_by_dict

from seed.func_tools.recur5yield__strict import *
