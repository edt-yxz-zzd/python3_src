#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/recognizer_LLoo_/interface_LLoo.py

seed.recognize.recognizer_LLoo_.interface_LLoo/g
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_LLoo_.interface_LLoo -x
py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LLoo_.interface_LLoo:__doc__ -ht
py_adhoc_call   seed.recognize.recognizer_LLoo_.interface_LLoo   @f


[[
LLoo ~= LL(+oo;)
    vivi LL1
using IForkableForwardInputStream
    # has no 『.seek()』
two phases:
    1. recognize header, declare to stick into current branch/choice/alternate
    2. continue to recognize whole

view ../../python3_src/seed/types/ForkableForwardInputStream.py
    view ../../python3_src/seed/types/LazyList.py

from seed.types.ForkableForwardInputStream import IForkable, IForkableForwardInputStream, ForkableForwardInputStream__using_LazyListIter
]]
[[
refactor:iter4two_phases_recognize() using halfway_result#BoxedHalfwayResult
view ../../python3_src/seed/func_tools/recur5yield.py
    #[:define____std_flattenable]:goto
###########
[[
std <<==:
    std_flattenable using tail_recur_gi_protocol__echo
    std_flattenable using child_gi_protocol__echo
    as-if:std_flattenable using child_gi_exc_protocol__echo[#TODO#]

std_flattenable(raw_halfway_exception,raw_final_exception;raw_halfway_result,raw_final_result;)
[std_flattenable(rhe,rfe;rhr,rfr;) =[def]= IGeneratorIterator
        <return-Either(std_flattenable(rhe,rfe;rhr,rfr;), rfr;)
            # | (False, tail_gi/tail_recur)
            # | (True, raw_final_result)
            #support: BoxedTailRecur|BoxedFinalResult
            #support: Either
            #support: tuple<bool,gi_or_rfr>
        ,yield-std_flattenable(?rhe,?rfe;?rhr,?rfr;)
            =>return5yield-(?rhr|?rfr)[#distinguished<<==mk_gi4either8xresult()#]
            =>raise5yield-(?rhe|?rfe|Escaped)[#except:BoxedException will be Escaped#]
        ,yield-BoxedHalfwayResult(rhr)
            =>return5yield-?userdefined
            =>raise5yield-?userdefined
            [#vivi:normal coroutine:feedback is userdefined#]
        ,yield-BoxedException__halfway(rhe)
            =>return5yield-?userdefined
            =>raise5yield-?userdefined
        ,raise-BoxedException__final(rfe)
        >
]

]]
###########
]]
[[
view ../../python3_src/seed/func_tools/recur5yield.py
    #[:___main_exports___]:goto
######################
from seed.func_tools.recur5yield import bind_gi_with_the_following_first_value4send, mk_gi4either8xresult, mk_gi4xresult_xexception
from seed.func_tools.recur5yield import BoxedHalfwayResult, BoxedException__halfway, BoxedException__final, BoxedException__through, Escaped, BoxedTailRecur, BoxedFinalResult
from seed.func_tools.recur5yield import EFlowControl, EFinal, EHalfway, mk_boxed_EFinal, mk_boxed_EHalfway
from seed.func_tools.recur5yield import recur5yield__list__echo__echo
### from seed.types.Either import Either
######################

]]
[[
ref to maker instead of recognizer since factory ~= maker
    ref to maker
        ref to recognizer
    ref to callable
        ref to postprocess6ok
        ref to postprocess
    ref to obj
        ref to constant/param
        ref to state/global_output_collector


]]
[[
]]
[[
++collector_ops:for:
    mk__serial
    mk__many___
    mk__skip_many1
    mk__end_by___
    mk__sep_by___
    mk__sep_end_by___
mk__wrapper4postprocess6ok
    IUnpacker
ICollectorOps:
    mk_empty
    puts :: Reply4IRecognizerLLoo<errmsg,IUnpacker> -> None
    finalize_collect
]]
[[
++accumulator serial
    empty_pass_recognizer_LLoo which required prev partial results and mk args for next recognizer_LLoo
dependent_pair
]]
[[
]]
[[
]]
[[
]]
[[
]]
[[
]]







from seed.recognize.recognizer_LLoo_.interface_LLoo import *
#]]]'''
__all__ = r'''
parse__via_IRecognizerLLoo
    mk_gi4skip_header_signal
    mk_gi4patch_header_signal_unless_fail


Signal__HeaderCompleted
Reply4IRecognizerLLoo

IAsBiCollectorOps
    ICollectorOps
        CollectorOps__rglnkls
            collector_ops__rglnkls
        CollectorOps__list
            collector_ops__list
    IBiCollectorOps
        BiCollectorOps


IAsBiUnpacker
    IUnpacker
        Unpacker__ignore
            unpacker__ignore
        Unpacker__one
        Unpacker__many

    IBiUnpacker
        BiUnpacker


INamed
IWrapper
    ILazyWrapper


IScene
    IScene4LLoo


IRequiredSceneAsClosure
    IPseudoMaker4RecognizerLLoo
        IMaker4RecognizerLLoo
            Maker4RecognizerLLoo__constant_eresult
                mkr4LLoo__constant_eresult
        IRecognizerLLoo
            RecognizerLLoo__constant_eresult
    IRequiredSceneAsClosure__ref


IRequiredSceneAsClosure__ref
    IPseudoMaker4RecognizerLLoo__ref
        PseudoMaker4RecognizerLLoo__ref
        IMaker4RecognizerLLoo__ref
            Maker4RecognizerLLoo__ref
        IRecognizerLLoo__ref
            RecognizerLLoo__ref

NamedWrapper
    PseudoMaker4RecognizerLLoo__named
        Maker4RecognizerLLoo__named
        RecognizerLLoo__named

IMaker4RecognizerLLoo__as_RecognizerLLoo
RecognizerLLoo__wrapper4mkr

ILazyWrapper
    PseudoMaker4RecognizerLLoo__wrapper4lazy
        Maker4RecognizerLLoo__wrapper4lazy
        RecognizerLLoo__wrapper4lazy



IWrapper
    IPseudoMaker4RecognizerLLoo__wrapper
        IPseudoMaker4RecognizerLLoo__wrapper__single_ref
        IMaker4RecognizerLLoo__wrapper
        IRecognizerLLoo__wrapper
            IRecognizerLLoo__named_wrapper
            IRecognizerLLoo__wrapper4postprocess6ok



Error4IRecognizerLLoo
    ParallelError4IRecognizerLLoo
        Error__not_only_one_match
    LogicError4IRecognizerLLoo
        Error__not_Reply4IRecognizerLLoo_after_Signal__HeaderCompleted
    TypeError4IRecognizerLLoo
        Error__too_few_args
        Error__too_many_args
KindError
LookupError__circle_ref


'''.split()#'''
__all__

from enum import Enum, auto
from itertools import count as count_ #islice

#from seed.data_funcs.lnkls import rglnkls_ops, empty_rglnkls, rglnkls_ipush_right, rglnkls_ipop_right, rglnkls2reversed_iterable, rglnkls5iterable
from seed.data_funcs.lnkls import rglnkls2list



from seed.func_tools.recur5yield import bind_gi_with_the_following_first_value4send, mk_gi4either8xresult, mk_gi4xresult_xexception
from seed.func_tools.recur5yield import BoxedHalfwayResult, BoxedException__halfway, BoxedException__final, BoxedException__through, Escaped, BoxedTailRecur, BoxedFinalResult
from seed.func_tools.recur5yield import EFlowControl, EFinal, EHalfway, mk_boxed_EFinal, mk_boxed_EHalfway
from seed.func_tools.recur5yield import recur5yield__list__echo__echo
from seed.types.Either import Either

from seed.types.StackStyleSet import StackStyleSet# MultiSetStyleStack
from seed.tiny_.check import check_type_is, check_type_le, check_int_ge, check_pseudo_qual_name, check_callable, check_pair
from seed.tiny import chains, snd, null_iter, null_tuple, mk_tuple
from seed.tiny_.dict_op__add import dict_add# set_add, dict_update, set_update

from seed.types.ForkableForwardInputStream import IForkable, IForkableForwardInputStream# ForkableForwardInputStream__using_LazyListIter
from collections.abc import Generator as IGeneratorIterator

from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.helper.repr_input import repr_helper

class Signal__HeaderCompleted:
    def __init__(sf, num_consumed, inputter4body:IForkable, result4header, /):
        'num_consumed/uint -> inputter4body/IForkable -> result4header -> None'
        check_int_ge(0, num_consumed)
        check_type_le(IForkable, inputter4body)
        sf._st = inputter4body
        sf._r4hdr = result4header
    def __repr__(sf, /):
        return repr_helper(sf, sf._n, sf._st, sf._r4hdr)
    @property
    def num_consumed(sf, /):
        '-> num_consumed/uint'
        return sf._n
    @property
    def the_inputter4body(sf, /):
        '-> end_of_header/begin_of_body/IForkable'
        return sf._st
    @property
    def the_result4header(sf, /):
        '-> result4header'
        return sf._r4hdr
    def ireplace_ex__inputter4body(sf, num_consumed, inputter4body, /):
        'num_consumed/uint -> inputter4body/IForkable -> Signal__HeaderCompleted'
        #used by:???
        return type(sf)(num_consumed, inputter4body, sf.the_result4header)
    def ireplace__result4header(sf, result4header, /):
        'result4header -> Signal__HeaderCompleted'
        #used with:wrapper.header_signal_process
        return type(sf)(sf.num_consumed, sf.the_inputter4body, result4header)
    def ilift(sf, /):
        '-> Signal__HeaderCompleted'
        return sf.ireplace__result4header(sf)
    def ilift__(sf, num_consumed, inputter4body, /):
        '-> Signal__HeaderCompleted'
        #used by:look_ahead
        #used by:look_ahead__no_err
        return sf.ilift().ireplace_ex__inputter4body(num_consumed, inputter4body)
    def __pos__(sf, /):
        '-> Signal__HeaderCompleted #+sf'
        return sf.ilift()






class Reply4IRecognizerLLoo:
    'reply4LLoo/Reply[;inputter,errmsg,rfr/raw_final_result;]'
    #class Result4IRecognizerLLoo:
    #class RecognizeResult:
    #def __init__(sf, forkable8inputter4end, err_vs_ok:bool, errmsg_or_result, /):
    def __init__(sf, num_consumed, inputter4end:IForkable, either_errmsg_or_result:Either, /):
        'num_consumed/uint -> inputter4end/IForkable -> either_errmsg_or_result/Either[;errmsg,raw_final_result;] -> None'
        check_int_ge(0, num_consumed)
        check_type_le(IForkable, inputter4end)
        check_type_is(Either, either_errmsg_or_result)
        sf._n = num_consumed
        sf._st = inputter4end
        sf._either = either_errmsg_or_result
    def __repr__(sf, /):
        return repr_helper(sf, sf._n, sf._st, sf._either)
    @property
    def num_consumed(sf, /):
        '-> num_consumed/uint'
        return sf._n
    @property
    def the_inputter4end(sf, /):
        '-> IForkable/(end_of_whole/end_of_body if sf.ok else begin_of_err)'
        return sf._st
    @property
    def the_eresult(sf, /):
        '-> Either(;errmsg, result;)'
        return sf._either
    @property
    def ok(sf, /):
        '-> err_vs_ok/bool'
        return sf._either.case
    @property
    def errmsg_or_result(sf, /):
        '-> errmsg_or_result/(errmsg if not sf.ok else result)'
        return sf._either.payload
    @property
    def errmsg(sf, /):
        '-> (errmsg if not sf.ok else ^AttributeError)'
        return sf._either.left
    @property
    def result(sf, /):
        '-> (result6ok if sf.ok else ^AttributeError)'
        return sf._either.right
    def ireplace_ex__inputter4end(sf, num_consumed, inputter4end, /):
        'num_consumed/uint -> inputter4end/IForkable -> Reply4IRecognizerLLoo'
        #used by:look_ahead
        return type(sf)(num_consumed, inputter4end, sf.the_eresult)
    def ireplace__eresult(sf, either_errmsg_or_result, /):
        'either_errmsg_or_result/Either -> Reply4IRecognizerLLoo'
        #used with:wrapper.postprocess
        check_type_is(Either, either_errmsg_or_result)
        return type(sf)(sf.num_consumed, sf.the_inputter4end, either_errmsg_or_result)
    def iflip__ok(sf, /):
        '-> Reply4IRecognizerLLoo'
        #used by:invert_err_ok
        return type(sf)(sf.num_consumed, sf.the_inputter4end, ~sf.the_eresult)

    def ireplace__result(sf, result6ok4LLoo, /):
        '-> Reply4IRecognizerLLoo'
        #used with:wrapper.postprocess6ok
        if not sf.ok:raise AttributeError
        return sf.ireplace__eresult(Either.from_right(result6ok4LLoo))
    def ilift(sf, /):
        '-> Reply4IRecognizerLLoo'
        return sf.ireplace__eresult(Either.from_right(sf))
    def ilift__(sf, num_consumed, inputter4end, /):
        '-> Reply4IRecognizerLLoo'
        #used by:look_ahead__no_err
        #used by:try
        return sf.ilift().ireplace_ex__inputter4end(num_consumed, inputter4end)
    def __invert__(sf, /):
        '-> Reply4IRecognizerLLoo #~sf'
        return sf.iflip__ok()
    def __pos__(sf, /):
        '-> Reply4IRecognizerLLoo #+sf'
        return sf.ilift()


class Error4IRecognizerLLoo(Exception):pass
class ParallelError4IRecognizerLLoo(Error4IRecognizerLLoo):pass
class Error__not_only_one_match(ParallelError4IRecognizerLLoo):pass
class LogicError4IRecognizerLLoo(Error4IRecognizerLLoo):pass
class Error__not_Reply4IRecognizerLLoo_after_Signal__HeaderCompleted(LogicError4IRecognizerLLoo):
    "LogicError4IRecognizerLLoo('not Reply4IRecognizerLLoo after Signal__HeaderCompleted')"
    pass
class TypeError4IRecognizerLLoo(Error4IRecognizerLLoo):pass
class Error__too_few_args(TypeError4IRecognizerLLoo):pass
class Error__too_many_args(TypeError4IRecognizerLLoo):pass
class KindError(Exception):pass
class LookupError__circle_ref(LookupError):pass





class INamed(ABC):
    __slots__ = ()
    @property
    @abstractmethod
    def my_name(sf, /):
        '-> nm/(hashable&&immutable)'
class IWrapper(ABC):
    __slots__ = ()
    @property
    @abstractmethod
    def the_wrapped_obj(sf, /):
        '-> wrapped_obj'
    _base_type4wrapped_obj_ = object
    def _check_wrapped_obj_(sf, wrapped_obj, /):
        check_type_le(type(sf)._base_type4wrapped_obj_, wrapped_obj)
class ILazyWrapper(IWrapper):
    'to break local recur/unamed recur'
    __slots__ = ()
    @abstractmethod
    def unlazy(sf, /):
        '-> the_wrapped_obj # get or (make and cache)'
    @property
    @override
    def the_wrapped_obj(sf, /):
        '-> wrapped_obj'
        return sf.unlazy()


class IAsBiCollectorOps(ABC):
    __slots__ = ()
    @abstractmethod
    def as_IBiCollectorOps(sf, /):
        '-> IBiCollectorOps'
class IBiCollectorOps(IAsBiCollectorOps):
    __slots__ = ()
    @property
    @abstractmethod
    def collector_ops4result(sf, /):
        '-> ICollectorOps'
    @property
    @abstractmethod
    def collector_ops4args4mkr(sf, /):
        '-> ICollectorOps'
    @override
    def as_IBiCollectorOps(sf, /):
        '-> IBiCollectorOps'
        return sf
class BiCollectorOps(IBiCollectorOps):
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        return repr_helper(sf, sf._c4r, sf._c4a)
    def __init__(sf, collector_ops4result, collector_ops4args4mkr, /):
        check_type_le(ICollectorOps, collector_ops4result)
        check_type_le(ICollectorOps, collector_ops4args4mkr)
        sf._c4r = collector_ops4result
        sf._c4a = collector_ops4args4mkr
    @property
    @override
    def collector_ops4result(sf, /):
        return sf._c4r
    @property
    @override
    def collector_ops4args4mkr(sf, /):
        return sf._c4a

class ICollectorOps(IAsBiCollectorOps):
    'used by:IRecognizerLLoo-serial'
    __slots__ = ()
    @abstractmethod
    def _check_outer_container_(sf, outer_container, /):
        '-> None | ^TypeError'
    @abstractmethod
    def _check_inner_container_(sf, inner_container, /):
        '-> None | ^TypeError'
    @abstractmethod
    def _mk_empty_inner_container_(sf, /):
        '-> inner_container<x>{len==0}'
    @abstractmethod
    def _puts_(sf, inner_container, iterable, /):
        'inner_container<x> -> Iterable<x> -> inner_container<x>'
    @abstractmethod
    def _finalize_collect_(sf, inner_container, /):
        'inner_container<x> -> outer_container<x>'


    @override
    def as_IBiCollectorOps(sf, /):
        '-> IBiCollectorOps'
        return BiCollectorOps(sf, sf)

    def mk_empty_inner_container(sf, /):
        '-> inner_container<x>{len==0}'
        inner_container = sf._mk_empty_inner_container_()
        sf._check_inner_container_(inner_container)
        return inner_container
    def puts(sf, inner_container, unpacker, /):
        'inner_container<x> -> IUnpacker<x> -> inner_container<x>'
        check_type_le(IUnpacker, unpacker)
        it = iter(unpacker.unpack())
        sf._check_inner_container_(inner_container)
        inner_container = sf._puts_(inner_container, it)
        sf._check_inner_container_(inner_container)
        return inner_container
    def finalize_collect(sf, inner_container, /):
        'inner_container<x> -> outer_container<x>'
        sf._check_inner_container_(inner_container)
        outer_container = sf._finalize_collect_(inner_container)
        sf._check_outer_container_(outer_container)
        return outer_container
class IAsBiUnpacker(ABC):
    __slots__ = ()
    @abstractmethod
    def as_IBiUnpacker(sf, /):
        '-> IBiUnpacker'
class IUnpacker(IAsBiUnpacker):
    'used by:ICollectorOps,IRecognizerLLoo-serial # Reply4IRecognizerLLoo<errmsg,IUnpacker>'
    __slots__ = ()
    @abstractmethod
    def _unpack_(sf, /):
        'IUnpacker<x> -> Iterable<x>'
    def unpack(sf, /):
        'IUnpacker<x> -> Iterator<x>'
        return iter(sf._unpack_())
    @override
    def as_IBiUnpacker(sf, /):
        '-> IBiUnpacker'
        return BiUnpacker(sf, sf)
class IBiUnpacker(IAsBiUnpacker):
    __slots__ = ()
    @property
    @abstractmethod
    def unpacker4result(sf, /):
        '-> IUnpacker<x> #to makeup:Reply4IRecognizerLLoo #ICollectorOps'
    @property
    @abstractmethod
    def unpacker4args4mkr(sf, /):
        '-> IUnpacker<x> #to makeup:args of IMaker4RecognizerLLoo.mk_pseudo_mkr4recognizer_LLoo/partial-num_params_required #dependent_pair...'
    @override
    def as_IBiUnpacker(sf, /):
        '-> IBiUnpacker'
        return sf


class BiUnpacker(IBiUnpacker):
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        return repr_helper(sf, sf._u4r, sf._u4a)
    def __init__(sf, unpacker4result, unpacker4args4mkr, /):
        check_type_le(IUnpacker, unpacker4result)
        check_type_le(IUnpacker, unpacker4args4mkr)
        sf._u4r = unpacker4result
        sf._u4a = unpacker4args4mkr
    @property
    @override
    def unpacker4result(sf, /):
        '-> IUnpacker<x> #to makeup:Reply4IRecognizerLLoo #ICollectorOps'
        return sf._u4r
    @property
    @override
    def unpacker4args4mkr(sf, /):
        '-> IUnpacker<x> #to makeup:args of IMaker4RecognizerLLoo.mk_pseudo_mkr4recognizer_LLoo/partial-num_params_required #dependent_pair...'
        return sf._u4a



class Unpacker__ignore(IUnpacker):
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        return repr_helper(sf)
    @override
    def _unpack_(sf, /):
        'IUnpacker<x> -> Iterable<x>'
        return null_iter
unpacker__ignore = Unpacker__ignore()
class Unpacker__one(IUnpacker):
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        return repr_helper(sf, sf._r)
    def __init__(sf, r, /):
        sf._r = r
    @override
    def _unpack_(sf, /):
        'IUnpacker<x> -> Iterable<x>'
        yield sf._r
        return
class Unpacker__many(IUnpacker):
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        return repr_helper(sf, sf._xs)
    def __init__(sf, xs, /):
        sf._xs = mk_tuple(xs)
    @override
    def _unpack_(sf, /):
        'IUnpacker<x> -> Iterable<x>'
        return sf._xs
class CollectorOps__rglnkls(ICollectorOps):
    ___no_slots_ok___ = True
    @override
    def _check_outer_container_(sf, outer_container, /):
        '-> None | ^TypeError'
        check_type_is(tuple, outer_container)
    @override
    def _check_inner_container_(sf, inner_container, /):
        '-> None | ^TypeError'
        check_type_is(tuple, inner_container)
    @override
    def _mk_empty_inner_container_(sf, /):
        '-> inner_container<x>{len==0}'
        return null_tuple#empty_rglnkls
    @override
    def _puts_(sf, inner_container, iterable, /):
        'inner_container<x> -> Iterable<x> -> inner_container<x>'
        iterable = iter(iterable)
        for x in iterable:
            #inner_container, _ = rglnkls_ipush_right(inner_container, x)
            inner_container = (inner_container, x)
        return inner_container
    @override
    def _finalize_collect_(sf, inner_container, /):
        'inner_container<x> -> outer_container<x>'
        return tuple(rglnkls2list(inner_container))

class CollectorOps__list(ICollectorOps):
    ___no_slots_ok___ = True
    @override
    def _check_outer_container_(sf, outer_container, /):
        '-> None | ^TypeError'
        check_type_is(tuple, outer_container)
    @override
    def _check_inner_container_(sf, inner_container, /):
        '-> None | ^TypeError'
        check_type_is(list, inner_container)
    @override
    def _mk_empty_inner_container_(sf, /):
        '-> inner_container<x>{len==0}'
        return []
    @override
    def _puts_(sf, inner_container, iterable, /):
        'inner_container<x> -> Iterable<x> -> inner_container<x>'
        inner_container.extend(iterable)
        return inner_container
    @override
    def _finalize_collect_(sf, inner_container, /):
        'inner_container<x> -> outer_container<x>'
        return tuple(inner_container)

collector_ops__list = CollectorOps__list()
collector_ops__rglnkls = CollectorOps__rglnkls()

class IRequiredSceneAsClosure(ABC):
    '[kinded_name == (kind, name)]'
    # eg:[kind :: Kind4Scene4LLoo]
    __slots__ = ()
    @abstractmethod
    def _iter_directly_used_kinded_names_(sf, /):
        '-> Iter (kind, name)'
    @abstractmethod
    def _iter_directly_used_IRequiredSceneAsClosure_(sf, /):
        '-> Iter IRequiredSceneAsClosure'


    def iter_directly_used_kinded_names(sf, /):
        '-> Iter (kind, name)'
        for knm in sf._iter_directly_used_kinded_names_():
            check_pair(knm)
            hash(knm)
            yield knm

    def iter_directly_used_IRequiredSceneAsClosure(sf, /):
        '-> Iter IRequiredSceneAsClosure'
        for x in sf._iter_directly_used_IRequiredSceneAsClosure_():
            check_type_le(IRequiredSceneAsClosure, x)
            yield x

class IRequiredSceneAsClosure__ref(IRequiredSceneAsClosure):
    __slots__ = ()
    @property
    @abstractmethod
    def its_kind(sf, /):
        '-> kind/(hashable&&immutable)'
    @property
    @abstractmethod
    def its_name(sf, /):
        '-> name/(hashable&&immutable)'
    @property
    def its_kinded_name(sf, /):
        '-> (kind, name)/(hashable&&immutable)'
        return (sf.kind, sf.name)
    @override
    def _iter_directly_used_kinded_names_(sf, /):
        '-> Iter (kind, name)'
        yield sf.its_kinded_name
        return
    @override
    def _iter_directly_used_IRequiredSceneAsClosure_(sf, /):
        '-> Iter IRequiredSceneAsClosure'
        return null_iter
class IScene(ABC):
    r'''[[[
    'factory4combinators&&closure4ref&&register4ref'

    global_recur_break vs local_recur_break
    named_recur_break vs unamed_recur_break
        * global_recur_break:using:
            IRequiredSceneAsClosure__ref
            IScene.dereference()
            +++
            IScene.register()
            #xxx:IScene.register__named()
        * local_recur_break:using:
            ILazyWrapper
                .unlazy()
            ######
            xxx = mk_Xxx(..., lazy_wrapper4xxx:=XxxLazyWrapper(lazy_xxx:=lambda:xxx), ...)
            yyy = lazy_wrapper4xxx.unlazy()
            assert xxx is yyy
            ######
            ??weakref??
            ######



IScene4LLoo = IScene<IRecognizerLLoo>
#class IFactory4CommonCombinators4IRecognizerLLoo(ABC):
    'factory4combinators&&closure4recognizer_ref&&register4named_recognizer'
ref:LLoo:
    IRequiredSceneAsClosure__ref
        ICallable__ref
            IPostprocess6Reply
            IPostprocess6ok_result
        IPseudoMaker4RecognizerLLoo__ref
            IRecognizerLLoo__ref
            IMaker4RecognizerLLoo__ref
named:LLoo:
    IPseudoMaker4RecognizerLLoo__named
        IRecognizerLLoo__named
        IMaker4RecognizerLLoo__named
lazy_wrapper:LLoo:
    IPseudoMaker4RecognizerLLoo__lazy_wrapper
        .unlazy()
        IRecognizerLLoo__lazy_wrapper
        IMaker4RecognizerLLoo__lazy_wrapper

    #]]]'''#'''
    __slots__ = ()
    @abstractmethod
    def check_kind(sf, kind, /):
        '-> None | ^KindError'
    @abstractmethod
    def check_kind_of_obj(sf, kind, obj, /):
        '-> None | ^KindError'
    @abstractmethod
    def _register_(sf, kind, name, obj, /):
        '-> None | ^KeyError'
    @abstractmethod
    def _lookup_(sf, kind, name, /):
        '-> obj | ^KeyError'
    @abstractmethod
    def _iter_registered_kinds_(sf, kind, /):
        '-> Iter kind'
    @abstractmethod
    def _iter_registered_names6kind_(sf, kind, /):
        '-> Iter name'
    @abstractmethod
    def _iter_registered_named_objs6kind_(sf, kind, /):
        '-> Iter (name, obj)'
    ######################
    ######################
    def register(sf, kind, name, obj, /):
        '-> None | ^KeyError | ^KindError'
        sf.check_kind_of_obj(kind, obj)
            # ^KindError
        sf._register_(kind, name, obj)
            # ^KeyError
    ######################
    def dereference(sf, kind, name, /):
        '-> obj | ^KeyError | ^LookupError__circle_ref # until not ref/IRequiredSceneAsClosure__ref'
        knm = kinded_name = (kind, name)
        s = StackStyleSet()
        for sz in count_(1):
            s.add(knm)
            if not len(s) == sz:
                ls = [*s]
                j = ls.index(knm)
                ls.append(knm)
                leadings = ls[:j]
                circle = ls[j:]
                raise LookupError__circle_ref(leadings, circle)
            obj = sf._lookup_(knm)
                # ^KeyError
            if not isinstance(obj, IRequiredSceneAsClosure__ref):
                break
            ref = obj
            knm = ref.its_kinded_name
        return obj
    ######################
    def iter_all_registered_objs(sf, /):
        '-> Iter obj # [maybe not unique]'
        kinds = sf._iter_registered_kinds_()
        nmobjs = chains(map(sf._iter_registered_named_objs6kind_, kinds))
        objs = map(snd, nmobjs)
        return objs
    ######################
    def iter_all_registered_kinded_names(sf, /):
        '-> Iter (kind, name) # [unique]'
        kinds = sf._iter_registered_kinds_()
        k2nms = sf._iter_registered_names6kind_
        return ((k,nm) for k in kinds for nm in k2nms(k))
    ######################
    def detect_circle_ref(scene, /):
        '-> None | ^LookupError__circle_ref'
        known_knms = {*scene.iter_all_registered_kinded_names()}
        for kind, name in known_knms:
            scene.dereference(kind, name)
                # ^LookupError__circle_ref
        return
    ######################
    def findout_all_missing_kinded_names(scene, /):
        'IScene -> Iter (kind, name) #but not detect circle_ref, see:.detect_circle_ref()'
        objs = scene.iter_all_registered_objs()
        addr2node = {id(obj):obj for obj in objs if isinstance(obj, IRequiredSceneAsClosure)}
            # unique&&filter
        ls = [*addr2node.values()]
        def put(node, /):
            if dict_add(addr2node, id(node), node):
                ls.append(node)
        while ls:
            node = ls.pop()
            for child_node in node.iter_directly_used_IRequiredSceneAsClosure():
                put(child_node)
        ######################
        nodes = addr2node.values()
        used_knms = {knm for node in nodes for knm in node.iter_directly_used_kinded_names()}
        known_knms = {*scene.iter_all_registered_kinded_names()}
        missing_knms = used_knms -known_knms
        return missing_knms

    ######################
    ######################
#end-class IScene(ABC):
r'''[[[
class Kind4Scene4LLoo(Enum):
    IRequiredSceneAsClosure = auto()
    if 1:
        IPseudoMaker4RecognizerLLoo = auto()

    ICallable = auto()
    if 1:
        IPostprocess6Reply = auto()
        IPostprocess6ok_result = auto()
    Others = auto()
    if 1:
        ConstantParameter = auto()
        MutableGlobalState = auto()
class Name4Scene4LLoo(Enum):
    head = auto()
        # [recognizer_LLoo a] -> recognizer_LLoo [a]
        # hdr_sgnl@head_end
    neck = auto()
        # [recognizer_LLoo a] -> recognizer_LLoo [a]
        # hdr_sgnl@neck.fst_nonempty_consumed otherwise neck_end
    body = auto()
        # [recognizer_LLoo a] -> recognizer_LLoo [a]
        # hdr_sgnl@body_begin
    head_body = auto()
        # recognizer_LLoo a -> recognizer_LLoo b -> recognizer_LLoo (a,b)
        # hdr_sgnl@head_end/body_begin
    head_neck_body = auto()
        # [recognizer_LLoo a] -> [recognizer_LLoo a] -> [recognizer_LLoo a] -> recognizer_LLoo [a]
        # hdr_sgnl@neck.fst_nonempty_consumed otherwise neck_end
    serial = head_neck_body

    skip = auto()
        # recognizer_LLoo a -> recognizer_LLoo None
        # hdr_sgnl@skip_end
    skip_body
        # recognizer_LLoo a -> recognizer_LLoo b -> recognizer_LLoo b
        # hdr_sgnl@skip_end/body_begin
    #accumulator
    dependent_pair
        # recognizer_LLoo a -> mkr4recognizer_LLoo<a> b -> recognizer_LLoo (a,b)

    the_only_one
    the_first_one
    parallel = the_only_one
    choice = the_first_one

    any_token
    eof
    not_followed_by
    look_ahead
    wrapper4postprocess
    wrapper4postprocess6ok
    wrapper4serial_collector
    invert_err_ok
    constant
    constant_overwrite6ok
    trace6enter
    trace6exit
    trace6err
    trace6exc
    trace6ok

    end_by
    between
    many
    skip_many1
    optional__tmay
    sep_by
    sep_end_by
#]]]'''#'''

class IScene4LLoo(IScene):
    'IPseudoMaker4RecognizerLLoo,'
    __slots__ = ()
    @override
    def check_kind(sf, kind, /):
        '-> None | ^KindError'
        #if type(kind) is not Kind4Scene4LLoo:raise KindError(kind)



class IPseudoMaker4RecognizerLLoo(IRequiredSceneAsClosure):
    'IPseudoMaker4RecognizerLLoo==(IMaker4RecognizerLLoo|IRecognizerLLoo)'
    __slots__ = ()
    @property
    @abstractmethod
    def imay_num_params_required(sf, /):
        '-> (imay num_params_required)/int{>=-1}'
class IMaker4RecognizerLLoo(IPseudoMaker4RecognizerLLoo):
    __slots__ = ()
    @property
    @abstractmethod
    def num_params_required(sf, /):
        '-> num_params_required/uint'
    @abstractmethod
    def mk_pseudo_mkr4recognizer_LLoo(sf, scene, /, *args):
        'scene -> *args{len=num_params_required} -> (IMaker4RecognizerLLoo|IRecognizerLLoo)/IPseudoMaker4RecognizerLLoo'


    @property
    @override
    def imay_num_params_required(sf, /):
        '-> (imay num_params_required)/int{>=-1}'
        return sf.num_params_required
    def mk_pseudo_mkr4recognizer_LLoo__slack(sf, scene, /, *args):
        'scene -> *args -> (pseudo_mkr/IPseudoMaker4RecognizerLLoo, args4remain{[[len<pseudo_mkr.num_params_required] or [[len==0][pseudo_mkr :: IRecognizerLLoo]]]}) | ^Error__too_many_args'
        L = len(args)
        i = 0
        while 0 <= (xsz := sf.imay_num_params_required) and (j := i + xsz) <= L:
            sf = sf.mk_pseudo_mkr4recognizer_LLoo(scene, *args[i:j])
            i = j
        args4remain = args[i:]
        if xsz < 0:
            assert xsz == -1
            if args4remain:raise Error__too_many_args
        else:
            assert len(args4remain) < sf.num_params_required
        return (sf, args4remain)
    def mk_recognizer_LLoo(sf, scene, /, *args):
        'scene -> *args{len=num_params_required} -> IRecognizerLLoo | ^Error__too_many_args | ^Error__too_few_args'
        (sf, args4remain) = sf.mk_pseudo_mkr4recognizer_LLoo__slack(scene, *args)
            # ^Error__too_many_args
        if not sf.imay_num_params_required == -1:
            assert sf.num_params_required > len(args4remain)
            raise Error__too_few_args
        assert isinstance(sf, IRecognizerLLoo)
        return sf
#end-class IMaker4RecognizerLLoo(IPseudoMaker4RecognizerLLoo):
class IRecognizerLLoo(IPseudoMaker4RecognizerLLoo):
    __slots__ = ()
    #@override
    imay_num_params_required = -1
    def iter4two_phases_recognize(sf, inputter4whole, /):
        check_type_le(IForkable, inputter4whole)
        gi = sf._iter4two_phases_recognize_(inputter4whole)
        check_type_le(IGeneratorIterator, gi)
        return gi
    @property
    @abstractmethod
    def scene(sf, /):
        '-> IScene4LLoo'
    @abstractmethod
    def _iter4two_phases_recognize_(sf, inputter4whole, /):
        r'''[[[
        :: inputter4whole/begin_of_whole/begin_of_header/IForkable
        -> gi4two_phases_recognize/IGeneratorIterator/std_flattenable(rhe:=<none>,rfe:=Error4IRecognizerLLoo;rhr:=Signal__HeaderCompleted[#at_most_one#],rfr:=?userdefined;)
        #]]]'''#'''
        ######################
        ######################
        ######################
        ###example:
        ######################
        saved_snapshot = inputter4whole.fork()
        ot = ...
        gi = ot.iter4two_phases_recognize(...)
        try:
            hdr_sgnl_or_reply = yield gi
        except Error4IRecognizerLLoo:
            raise BoxedException__final(Error4IRecognizerLLoo(...))
        if type(hdr_sgnl_or_reply) is Signal__HeaderCompleted:
            ...
            hdr_sgnl = hdr_sgnl_or_reply
            ...
            reply4LLoo = yield gi
        else:
            reply4LLoo = hdr_sgnl_or_reply
        if not reply4LLoo.ok:
            raise BoxedException__final(Error4IRecognizerLLoo(...))
        inputter4continue = reply4LLoo.the_inputter4end
        partial_result = reply4LLoo.the_result4header
        yield BoxedHalfwayResult(Signal__HeaderCompleted(...))
        ...
        return BoxedTailRecur((...).iter4two_phases_recognize(...)) if 0 else BoxedFinalResult(...)
        ######################
        ######################
        ######################
    iter4two_phases_recognize.__doc__ = _iter4two_phases_recognize_.__doc__
#end-class IRecognizerLLoo(IPseudoMaker4RecognizerLLoo):
@recur5yield__list__echo__echo
def parse__via_IRecognizerLLoo(recognizer_LLoo, inputter4whole, /):
    'YS_GI(IRecognizerLLoo -> IForkable -> Reply4IRecognizerLLoo)'
    'IRecognizerLLoo -> IForkable -> Reply4IRecognizerLLoo'
    check_type_le(IRecognizerLLoo, recognizer_LLoo)
    check_type_le(IForkable, inputter4whole)
    gi = recognizer_LLoo.iter4two_phases_recognize(inputter4whole)
    return mk_gi4skip_header_signal(gi)
    #return BoxedTailRecur(mk_gi4skip_header_signal(gi))
    #777;    yield
def mk_gi4skip_header_signal(gi4two_phases_recognize, /):
    'gi4two_phases_recognize -> gi4one_phase_recognize'
    'YS_GI(gi4two_phases_recognize -> Reply4IRecognizerLLoo)'
    #xxx:'YS_GI(IRecognizerLLoo -> IForkable -> Reply4IRecognizerLLoo)'
    gi = mk_gi4either8xresult(gi4two_phases_recognize)
    gi4two_phases_recognize = None
    x = yield gi
    if x.is_left:
        hdr_sgnl = x.left
        check_type_is(Signal__HeaderCompleted, hdr_sgnl)
        y = yield gi
        if not y.is_right:
            raise Error__not_Reply4IRecognizerLLoo_after_Signal__HeaderCompleted
        x = y
    assert x.is_right
    reply4LLoo = x.right
    check_type_is(Reply4IRecognizerLLoo, reply4LLoo)
    return BoxedFinalResult(reply4LLoo)
def mk_gi4patch_header_signal_unless_fail(gi4two_phases_recognize, /):
    'gi4two_phases_recognize -> gi4two_phases_recognize{with hdr_sgnl or fail}'
    gi = mk_gi4either8xresult(gi4two_phases_recognize)
    gi4two_phases_recognize = None
    hdr_sgnl_occured = False
    x = yield gi
    if x.is_left:
        hdr_sgnl = x.left
        check_type_is(Signal__HeaderCompleted, hdr_sgnl)
        yield BoxedHalfwayResult(hdr_sgnl)
        hdr_sgnl_occured = True
        y = yield gi
        if not y.is_right:
            raise Error__not_Reply4IRecognizerLLoo_after_Signal__HeaderCompleted
        x = y
    assert x.is_right
    reply4LLoo = x.right
    check_type_is(Reply4IRecognizerLLoo, reply4LLoo)
    if not hdr_sgnl_occured and reply4LLoo.ok:
        hdr_sgnl = Signal__HeaderCompleted(reply4LLoo.num_consumed, reply4LLoo.the_inputter4end, reply4LLoo.result)
        yield BoxedHalfwayResult(hdr_sgnl)
        hdr_sgnl_occured = True
    assert hdr_sgnl_occured or not reply4LLoo.ok
    return BoxedFinalResult(reply4LLoo)



class NamedWrapper(INamed, IWrapper):
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        if sf._b:
            return sf._nm
        return str(sf)
    def __str__(sf, /):
        return repr_helper(sf, sf._nm, sf._w, repr_by_name=sf._b)
    def __init__(sf, nm, wrapped_obj, /, *, repr_by_name:bool):
        check_type_is(bool, repr_by_name)
        hash(nm) # hashable
        if repr_by_name:
            #check_type_is(str, nm)
            check_pseudo_qual_name(nm)
        sf._check_wrapped_obj_(wrapped_obj)

        sf._nm = nm
        sf._w = wrapped_obj
        sf._b = repr_by_name
    @property
    @override
    def my_name(sf, /):
        '-> nm/(hashable&&immutable)'
        return sf._nm
    @property
    @override
    def the_wrapped_obj(sf, /):
        '-> wrapped_obj'
        return sf._w
class PseudoMaker4RecognizerLLoo__named(NamedWrapper, IPseudoMaker4RecognizerLLoo):
    ___no_slots_ok___ = True
    _base_type4wrapped_obj_ = IPseudoMaker4RecognizerLLoo
    @property
    @override
    def imay_num_params_required(sf, /):
        '-> (imay num_params_required)/int{>=-1}'
        return sf.the_wrapped_obj.imay_num_params_required
    @override
    def _iter_directly_used_kinded_names_(sf, /):
        '-> Iter (kind, name)'
        return null_iter
    @override
    def _iter_directly_used_IRequiredSceneAsClosure_(sf, /):
        '-> Iter IRequiredSceneAsClosure'
        yield sf.the_wrapped_obj
        return

class Maker4RecognizerLLoo__named(PseudoMaker4RecognizerLLoo__named, IMaker4RecognizerLLoo):
    ___no_slots_ok___ = True
    _base_type4wrapped_obj_ = IMaker4RecognizerLLoo

    @property
    @override
    def num_params_required(sf, /):
        '-> num_params_required/uint'
        return sf.the_wrapped_obj.num_params_required
    @override
    def mk_pseudo_mkr4recognizer_LLoo(sf, scene, /, *args):
        'scene -> *args{len=num_params_required} -> (IMaker4RecognizerLLoo|IRecognizerLLoo)/IPseudoMaker4RecognizerLLoo'
        return sf.the_wrapped_obj.mk_pseudo_mkr4recognizer_LLoo(scene, *args)
class RecognizerLLoo__named(PseudoMaker4RecognizerLLoo__named, IRecognizerLLoo):
    ___no_slots_ok___ = True
    _base_type4wrapped_obj_ = IRecognizerLLoo
    @property
    @override
    def scene(sf, /):
        '-> IScene4LLoo'
        return sf.the_wrapped_obj.scene
    @override
    def _iter4two_phases_recognize_(sf, inputter4whole, /):
        return sf.the_wrapped_obj._iter4two_phases_recognize_(inputter4whole)













class IPseudoMaker4RecognizerLLoo__ref(IPseudoMaker4RecognizerLLoo, IRequiredSceneAsClosure__ref):
    __slots__ = ()
class PseudoMaker4RecognizerLLoo__ref(IPseudoMaker4RecognizerLLoo__ref):
    #++scene??
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        return repr_helper(sf, sf._kd, sf._nm, sf._im)
    def __init__(sf, its_kind, its_name, imay_num_params_required, /):
        hash(its_kind)
        hash(its_name)
        check_int_ge(-1, imay_num_params_required)
        sf._kd = its_kind
        sf._nm = its_name
        sf._im = imay_num_params_required
    @property
    @override
    def imay_num_params_required(sf, /):
        '-> (imay num_params_required)/int{>=-1}'
        return sf._im
    @property
    @override
    def its_kind(sf, /):
        '-> kind/(hashable&&immutable)'
        return sf._kd
    @property
    @override
    def its_name(sf, /):
        '-> name/(hashable&&immutable)'
        return sf._nm
class IMaker4RecognizerLLoo__ref(IPseudoMaker4RecognizerLLoo__ref, IMaker4RecognizerLLoo, IRequiredSceneAsClosure__ref):
    __slots__ = ()
class IRecognizerLLoo__ref(IPseudoMaker4RecognizerLLoo__ref, IRecognizerLLoo, IRequiredSceneAsClosure__ref):
    __slots__ = ()
class Maker4RecognizerLLoo__ref(PseudoMaker4RecognizerLLoo__ref, IMaker4RecognizerLLoo__ref):
    ___no_slots_ok___ = True
    def __init__(sf, its_kind, its_name, num_params_required, /):
        check_int_ge(0, num_params_required)
        super().__init__(its_kind, its_name, num_params_required)
    @override
    def num_params_required(sf, /):
        '-> num_params_required/uint'
        return super().imay_num_params_required
    @override
    def mk_pseudo_mkr4recognizer_LLoo(sf, scene, /, *args):
        'scene -> *args{len=num_params_required} -> (IMaker4RecognizerLLoo|IRecognizerLLoo)/IPseudoMaker4RecognizerLLoo'
        mkr = scene.dereference(*sf.its_kinded_name)
        return mkr.mk_pseudo_mkr4recognizer_LLoo(scene, *args)
class RecognizerLLoo__ref(PseudoMaker4RecognizerLLoo__ref, IRecognizerLLoo__ref):
    ___no_slots_ok___ = True
    def __init__(sf, its_kind, its_name, /):
        super().__init__(its_kind, its_name, imay_num_params_required:=-1)
    @property
    @override
    def scene(sf, /):
        '-> IScene4LLoo'
        return sf._scn
    @override
    def _iter4two_phases_recognize_(sf, inputter4whole, /):
        ot = sf.scene.dereference(*sf.its_kinded_name)
        return ot._iter4two_phases_recognize_with_inner_args_(inputter4whole)

class IMaker4RecognizerLLoo__as_RecognizerLLoo(IMaker4RecognizerLLoo):
    'use:RecognizerLLoo__wrapper4mkr'
    __slots__ = ()
    @abstractmethod
    def _inner_args5outer_args_(sf, scene, /, *outer_args):
        'scene -> *outer_args{len=num_params_required} -> inner_args/tuple'
    @abstractmethod
    def _iter4two_phases_recognize_with_inner_args_(sf, inputter4whole, /, *inner_args):
        'see:IRecognizerLLoo._iter4two_phases_recognize_'
    @abstractmethod
    def _iter_directly_used_kinded_names_with_inner_args_(sf, /, *inner_args):
        'see:IRequiredSceneAsClosure._iter_directly_used_kinded_names_'
    @abstractmethod
    def _iter_directly_used_IRequiredSceneAsClosure_with_inner_args_(sf, /, *inner_args):
        'see:IRequiredSceneAsClosure._iter_directly_used_IRequiredSceneAsClosure_'

    @override
    def mk_pseudo_mkr4recognizer_LLoo(sf, scene, /, *outer_args):
        'scene -> *args{len=num_params_required} -> (IMaker4RecognizerLLoo|IRecognizerLLoo)/IPseudoMaker4RecognizerLLoo'
        if not len(outer_args) == sf.num_params_required:raise TypeError((len(outer_args), sf.num_params_required))
        inner_args = sf._inner_args5outer_args_(scene, *outer_args)
        return RecognizerLLoo__wrapper4mkr(mkr8rgnr:=sf, scene, inner_args)

class RecognizerLLoo__wrapper4mkr(IRecognizerLLoo):
    'used by:IMaker4RecognizerLLoo__as_RecognizerLLoo'
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        return repr_helper(sf, sf._mkr, sf._xs)
    def __init__(sf, mkr8rgnr, scene, inner_args, /):
        check_type_is(tuple, inner_args)
        check_type_le(IMaker4RecognizerLLoo__as_RecognizerLLoo, mkr8rgnr)
        check_type_le(IScene4LLoo, scene)
        sf._mkr = mkr8rgnr
        sf._scn = scene
        sf._xs = inner_args

    @property
    @override
    def scene(sf, /):
        '-> IScene4LLoo'
        return sf._scn
    @override
    def _iter4two_phases_recognize_(sf, inputter4whole, /):
        return sf._mkr._iter4two_phases_recognize_with_inner_args_(inputter4whole, *sf._xs)
    @override
    def _iter_directly_used_kinded_names_(sf, /):
        '-> Iter (kind, name)'
        return sf._mkr._iter_directly_used_kinded_names_with_inner_args_(*sf._xs)
    @override
    def _iter_directly_used_IRequiredSceneAsClosure_(sf, /):
        '-> Iter IRequiredSceneAsClosure'
        return sf._mkr._iter_directly_used_IRequiredSceneAsClosure_with_inner_args_(*sf._xs)

class PseudoMaker4RecognizerLLoo__wrapper4lazy(IPseudoMaker4RecognizerLLoo, ILazyWrapper):
    ___no_slots_ok___ = True
    _base_type4wrapped_obj_ = IPseudoMaker4RecognizerLLoo
    def __repr__(sf, /):
        return repr_helper(sf, sf._x, non_lazy=sf._b)
    def __init__(sf, lazy_or_wrapped_obj, /, *, non_lazy=False):
        sf._x = lazy_or_wrapped_obj
        sf._b = non_lazy
        check_type_is(bool, non_lazy)
        if non_lazy:
            wrapped_obj = lazy_or_wrapped_obj
            check_type_le(sf._base_type4wrapped_obj_, wrapped_obj)
        else:
            lazy__wrapped_obj = lazy_or_wrapped_obj
            check_callable(lazy__wrapped_obj)
    @override
    def unlazy(sf, /):
        '-> the_wrapped_obj/IPseudoMaker4RecognizerLLoo'
        #if non_lazy:
        if sf._b:
            return sf._x
        lazy__wrapped_obj = sf._x
        wrapped_obj = lazy__wrapped_obj()
        check_type_le(sf._base_type4wrapped_obj_, wrapped_obj)
        sf._x = wrapped_obj
        sf._b = True
        return sf.unlazy()
    @property
    @override
    def imay_num_params_required(sf, /):
        '-> (imay num_params_required)/int{>=-1}'
        return sf.unlazy().imay_num_params_required
    @override
    def _iter_directly_used_kinded_names_(sf, /):
        '-> Iter (kind, name)'
        return null_iter
    @override
    def _iter_directly_used_IRequiredSceneAsClosure_(sf, /):
        '-> Iter IRequiredSceneAsClosure'
        yield sf.unlazy()
        return



PseudoMaker4RecognizerLLoo__wrapper4lazy
class Maker4RecognizerLLoo__wrapper4lazy(PseudoMaker4RecognizerLLoo__wrapper4lazy, IMaker4RecognizerLLoo, ILazyWrapper):
    ___no_slots_ok___ = True
    _base_type4wrapped_obj_ = IMaker4RecognizerLLoo
    @property
    @override
    def num_params_required(sf, /):
        '-> num_params_required/uint'
        return sf.unlazy().num_params_required
    @override
    def mk_pseudo_mkr4recognizer_LLoo(sf, scene, /, *args):
        'scene -> *args{len=num_params_required} -> (IMaker4RecognizerLLoo|IRecognizerLLoo)/IPseudoMaker4RecognizerLLoo'
        return sf.unlazy().mk_pseudo_mkr4recognizer_LLoo(scene, *args)
class RecognizerLLoo__wrapper4lazy(PseudoMaker4RecognizerLLoo__wrapper4lazy, IRecognizerLLoo, ILazyWrapper):
    ___no_slots_ok___ = True
    _base_type4wrapped_obj_ = IRecognizerLLoo
    @property
    @override
    def scene(sf, /):
        '-> IScene4LLoo'
        return sf.unlazy().scene
    @override
    def _iter4two_phases_recognize_(sf, inputter4whole, /):
        return sf.unlazy()._iter4two_phases_recognize_(inputter4whole)


class IPseudoMaker4RecognizerLLoo__wrapper(IPseudoMaker4RecognizerLLoo, IWrapper):
    __slots__ = ()
    _base_type4wrapped_obj_ = IPseudoMaker4RecognizerLLoo
    @property
    @override
    def imay_num_params_required(sf, /):
        '-> (imay num_params_required)/int{>=-1}'
        return sf.the_wrapped_obj.imay_num_params_required
class IPseudoMaker4RecognizerLLoo__wrapper__single_ref(IPseudoMaker4RecognizerLLoo__wrapper):
    __slots__ = ()
    @override
    def _iter_directly_used_kinded_names_(sf, /):
        '-> Iter (kind, name)'
        return null_iter
    @override
    def _iter_directly_used_IRequiredSceneAsClosure_(sf, /):
        '-> Iter IRequiredSceneAsClosure'
        yield sf.the_wrapped_obj
        return
class IMaker4RecognizerLLoo__wrapper(IPseudoMaker4RecognizerLLoo__wrapper, IMaker4RecognizerLLoo, IWrapper):
    __slots__ = ()
    _base_type4wrapped_obj_ = IMaker4RecognizerLLoo
    @abstractmethod
    def _wrap_pseudo_mkr4recognizer_LLoo_(sf, scene, pseudo_mkr4recognizer_LLoo, /):
        'IPseudoMaker4RecognizerLLoo -> wrapper-IPseudoMaker4RecognizerLLoo'
    def _wrapped_args5wrapper_args_(sf, scene, /, *wrapper_args):
        'scene -> *wrapper_args{len=sf.num_params_required} -> wrapped_args/tuple{len=the_wrapped_obj.num_params_required}'
        wrapped_args = wrapper_args
        return wrapped_args
    @property
    @override
    def num_params_required(sf, /):
        '-> num_params_required/uint'
        return sf.the_wrapped_obj.num_params_required
    @override
    def mk_pseudo_mkr4recognizer_LLoo(sf, scene, /, *wrapper_args):
        'scene -> *args{len=num_params_required} -> (IMaker4RecognizerLLoo|IRecognizerLLoo)/IPseudoMaker4RecognizerLLoo'
        wrapped_args = sf._wrapped_args5wrapper_args_(scene, *wrapper_args)
        pseudo_mkr = sf.the_wrapped_obj.mk_pseudo_mkr4recognizer_LLoo(scene, *wrapped_args)
        wrapper4pseudo_mkr = sf._wrap_pseudo_mkr4recognizer_LLoo_(scene, pseudo_mkr)
        return wrapper4pseudo_mkr
class IRecognizerLLoo__wrapper(IPseudoMaker4RecognizerLLoo__wrapper, IRecognizerLLoo, IWrapper):
    'YS_GI<I->O>:yield-send-version-IGeneratorIterator-for-recur5yield__list__echo__echo'
    __slots__ = ()
    _base_type4wrapped_obj_ = IRecognizerLLoo
    @property
    @abstractmethod
    def may_preprocess(sf, /):
        '-> may preprocess/YS_GI(inputter4whole -> (state, inputter4whole))'
    @property
    @abstractmethod
    def may_header_signal_process(sf, /):
        '-> may header_signal_process/YS_GI(state -> hdr_sgnl/Signal__HeaderCompleted -> tail_gi_after_hdr_sgnl -> (state, may hdr_sgnl, tail_gi_after_hdr_sgnl))'
    @property
    @abstractmethod
    def may_postprocess(sf, /):
        '-> may postprocess/YS_GI(state -> Reply4IRecognizerLLoo -> Reply4IRecognizerLLoo)'
    @property
    @override
    def scene(sf, /):
        '-> IScene4LLoo'
        return sf.the_wrapped_obj.scene
    @override
    def _iter4two_phases_recognize_(sf, inputter4whole, /):
        if not None is (preprocess := sf.may_preprocess):
            (state, inputter4whole) = yield preprocess(inputter4whole)
        else:
            state = None#init
            inputter4whole
        (state, inputter4whole)
        gi = sf.the_wrapped_obj._iter4two_phases_recognize_(inputter4whole)
        inputter4whole = None#del
        if None is sf.may_header_signal_process is sf.may_postprocess:
            return BoxedTailRecur(gi)
        gi, old_gi = mk_gi4either8xresult(gi), gi
        x = yield gi
        if x.is_left:
            hdr_sgnl = x.left
            check_type_is(Signal__HeaderCompleted, hdr_sgnl)
            tail_gi_after_hdr_sgnl = gi
            gi = None#del
            if not None is (header_signal_process := sf.may_header_signal_process):
                (state, may_hdr_sgnl, tail_gi_after_hdr_sgnl) = yield header_signal_process(state, hdr_sgnl, tail_gi_after_hdr_sgnl)
                tail_gi_after_hdr_sgnl, old_gi = mk_gi4either8xresult(tail_gi_after_hdr_sgnl), tail_gi_after_hdr_sgnl
                if may_hdr_sgnl is None:
                    pass#drop:hdr_sgnl
                else:
                    hdr_sgnl = may_hdr_sgnl
                    check_type_is(Signal__HeaderCompleted, hdr_sgnl)
                    yield BoxedHalfwayResult(hdr_sgnl)
                    hdr_sgnl = None#del
                (state, tail_gi_after_hdr_sgnl)
            else:
                yield BoxedHalfwayResult(hdr_sgnl)
                hdr_sgnl = None#del
                (state, tail_gi_after_hdr_sgnl)
            (state, tail_gi_after_hdr_sgnl)
            if None is sf.may_postprocess:
                return BoxedTailRecur(old_gi)
            y = yield tail_gi_after_hdr_sgnl
            tail_gi_after_hdr_sgnl = None#del
            if not y.is_right:
                raise Error__not_Reply4IRecognizerLLoo_after_Signal__HeaderCompleted
            x = y
            state
        state, x
        assert x.is_right
        reply4LLoo = x.right
        check_type_is(Reply4IRecognizerLLoo, reply4LLoo)
        if not None is (postprocess := sf.may_postprocess):
            reply4LLoo = yield postprocess(state, reply4LLoo)
            check_type_is(Reply4IRecognizerLLoo, reply4LLoo)
        else:
            state = None#del
            reply4LLoo
        reply4LLoo
        return BoxedFinalResult(reply4LLoo)
['_iter_directly_used_IRequiredSceneAsClosure_', '_iter_directly_used_kinded_names_', 'scene', 'the_wrapped_obj']
class IRecognizerLLoo__named_wrapper(NamedWrapper, IRecognizerLLoo__wrapper):
    __slots__ = ()

class IRecognizerLLoo__wrapper4postprocess6ok(IRecognizerLLoo__wrapper):
    'postprocess6ok:[Reply4IRecognizerLLoo.ok is True]'
    __slots__ = ()
    @property
    @abstractmethod
    def postprocess6ok(sf, result6ok4LLoo, /):
        'result6ok4LLoo -> result6ok4LLoo'
    may_preprocess = None
    may_header_signal_process = None
    @property
    @override
    def may_postprocess(sf, state, reply4LLoo, /):
        'YS_GI(state -> Reply4IRecognizerLLoo -> Reply4IRecognizerLLoo)'
        #'-> may postprocess/YS_GI(state -> Reply4IRecognizerLLoo -> Reply4IRecognizerLLoo)'
        if reply4LLoo.ok:
            result6ok4LLoo = reply4LLoo.result
            result6ok4LLoo = sf.postprocess(result6ok4LLoo)
            reply4LLoo = reply4LLoo.ireplace__result(result6ok4LLoo)
        reply4LLoo
        return BoxedFinalResult(reply4LLoo)
        yield



class Maker4RecognizerLLoo__constant_eresult(IMaker4RecognizerLLoo):
, eresult
    def mk_pseudo_mkr4recognizer_LLoo(sf, scene, /):
class Maker4RecognizerLLoo__constant_eresult(IMaker4RecognizerLLoo):
    ___no_slots_ok___ = True
    @property
    @override
    def num_params_required(sf, /):
        '-> num_params_required/uint'
        return 1
    @override
    def mk_pseudo_mkr4recognizer_LLoo(sf, scene, eresult, /):
        'scene -> Either -> RecognizerLLoo__constant_eresult'
        return RecognizerLLoo__constant_eresult(scene, eresult)
    @override
    def _iter_directly_used_kinded_names_(sf, /):
        '-> Iter (kind, name)'
        return null_iter
    @override
    def _iter_directly_used_IRequiredSceneAsClosure_(sf, /):
        '-> Iter IRequiredSceneAsClosure'
        return null_iter
mkr4LLoo__constant_eresult = Maker4RecognizerLLoo__constant_eresult()
class RecognizerLLoo__constant_eresult(IRecognizerLLoo):
    ___no_slots_ok___ = True
    def __init__(sf, scene, eresult, /):
        check_type_le(IScene4LLoo, scene)
        check_type_is(Either, eresult)
        sf._scn = scene
        sf._x = eresult
    @property
    @override
    def scene(sf, /):
        '-> IScene4LLoo'
        return sf._scn
    @override
    def _iter4two_phases_recognize_(sf, inputter4whole, /):
        reply4LLoo = Reply4IRecognizerLLoo(num_consumed:=0, inputter4end:=inputter4whole, eresult:=sf._x)
        return BoxedFinalResult(reply4LLoo)
        777;    yield
    @override
    def _iter_directly_used_kinded_names_(sf, /):
        '-> Iter (kind, name)'
        return null_iter
    @override
    def _iter_directly_used_IRequiredSceneAsClosure_(sf, /):
        '-> Iter IRequiredSceneAsClosure'
        return null_iter
#xxx:recognizer_LLoo__pass = RecognizerLLoo__constant_eresult(Either.from_right(unpacker__ignore))
#xxx:recognizer_LLoo__fail = RecognizerLLoo__constant_eresult(Either.from_left('constant_fail'))
######################
######################
######################

def __():
    import inspect
    from seed.tiny import print_err
    n = 0
    for nm, x in sorted(globals().items()):
        if not isinstance(x, type):continue
        typ = x
        if not typ.__module__ == __name__:continue
        if not (typ.__name__[0] == 'I') is (inspect.isabstract(typ)):
            if not n:print_err('!'*22)
            print_err(__name__, typ.__name__, getattr(typ, '__abstractmethods__', None))
            n += 1
    if n:print_err('!'*22)
__()

######################
######################
######################


__all__
from seed.recognize.recognizer_LLoo_.interface_LLoo import *
