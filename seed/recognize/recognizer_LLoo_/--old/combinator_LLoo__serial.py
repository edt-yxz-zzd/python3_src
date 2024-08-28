#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/recognizer_LLoo_/combinator_LLoo__serial.py

seed.recognize.recognizer_LLoo_.combinator_LLoo__serial
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_LLoo_.combinator_LLoo__serial -x
py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LLoo_.combinator_LLoo__serial:__doc__ -ht
py_adhoc_call   seed.recognize.recognizer_LLoo_.combinator_LLoo__serial   @f
from seed.recognize.recognizer_LLoo_.combinator_LLoo__serial import *
#]]]'''
__all__ = r'''
IRecognizerLLoo__serial_framework
    RecognizerLLoo__serial

IChildItem4Serial4LLoo
    ChildItem4Serial4LLoo__plain
        TriboolTriple8cases4hdr_sgnl
'''.split()#'''
__all__

from seed.recognize.recognizer_LLoo_.combinator_LLoo__wrapper import RecognizerLLoo__try, RecognizerLLoo__optional__tmay
from seed.recognize.recognizer_LLoo_.combinator_LLoo__parallel import RecognizerLLoo__the_first_one__tagged





from seed.recognize.recognizer_LLoo_.interface_LLoo import Signal__HeaderCompleted, Reply4IRecognizerLLoo
from seed.recognize.recognizer_LLoo_.interface_LLoo import IPseudoMaker4RecognizerLLoo, IMaker4RecognizerLLoo, IRecognizerLLoo

from seed.recognize.recognizer_LLoo_.interface_LLoo import IScene4LLoo, IAsBiCollectorOps, IAsBiUnpacker
from seed.recognize.recognizer_LLoo_.interface_LLoo import Error__not_Reply4IRecognizerLLoo_after_Signal__HeaderCompleted

r'''[[[


ICollectorOps
    CollectorOps__rglnkls
        collector_ops__rglnkls
    CollectorOps__list
        collector_ops__list
IUnpacker
    Unpacker__ignore
        unpacker__ignore
    Unpacker__one
    Unpacker__many

IBiUnpacker
    BiUnpacker



#]]]'''#'''

from seed.func_tools.recur5yield import bind_gi_with_the_following_first_value4send, mk_gi4either8xresult, mk_gi4xresult_xexception
from seed.func_tools.recur5yield import BoxedHalfwayResult, BoxedException__halfway, BoxedException__final, BoxedException__through, Escaped, BoxedTailRecur, BoxedFinalResult
from seed.func_tools.recur5yield import EFlowControl, EFinal, EHalfway, mk_boxed_EFinal, mk_boxed_EHalfway
from seed.func_tools.recur5yield import recur5yield__list__echo__echo
from seed.types.Either import Either

from seed.types.StackStyleSet import StackStyleSet# MultiSetStyleStack
from seed.tiny_.check import check_type_is, check_type_le, check_int_ge, check_pseudo_qual_name, check_callable, check_pair, check_non_ABC
from seed.tiny import chains, snd, null_iter, null_tuple, mk_tuple
from seed.tiny_.dict_op__add import dict_add# set_add, dict_update, set_update
#from seed.tiny_.verify import is_iterable, is_iterator, is_reiterable
from seed.tiny_.check import check_tribool

from seed.types.ForkableForwardInputStream import IForkable, IForkableForwardInputStream# ForkableForwardInputStream__using_LazyListIter
from collections.abc import Generator as IGeneratorIterator



from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.helper.repr_input import repr_helper


class IChildItem4Serial4LLoo(ABC):
    __slots__ = ()
    @abstractmethod
    def _mk_ex__child_recognizer_LLoo_(sf, scene, acc4args4mkr, /):
        'IScene4LLoo -> acc4args4mkr -> (acc4args4mkr, IRecognizerLLoo)'
    @abstractmethod
    def _update_accumulators_ex_(sf, acc4args4mkr, acc4result6ok, result6ok4child_LLoo, /):
        'acc4args4mkr -> acc4result6ok -> result6ok4child_LLoo -> (acc4args4mkr, acc4result6ok, stopped/bool)'
    @abstractmethod
    def _mk_may_header_signal_at_beginning_(sf, acc4result6ok, num_consumed, inputter4child_begin, /):
        'acc4result6ok -> num_consumed/uint -> inputter4child_begin/IForkableForwardInputStream -> may Signal__HeaderCompleted'
    @abstractmethod
    def _mk_may_header_signal5header_signal_(sf, acc4result6ok, num_consumed, hdr_sgnl, /):
        'acc4result6ok -> num_consumed/uint -> hdr_sgnl/Signal__HeaderCompleted -> may Signal__HeaderCompleted'
    @abstractmethod
    def _mk_may_header_signal5ok_reply_(sf, reply4LLoo, acc4result6ok, num_consumed, /):
        'reply4LLoo/Reply4IRecognizerLLoo -> acc4result6ok -> num_consumed/uint -> may Signal__HeaderCompleted'



    def mk_ex__child_recognizer_LLoo(sf, scene, acc4args4mkr, /):
        'IScene4LLoo -> acc4args4mkr -> (acc4args4mkr, IRecognizerLLoo)'
        (acc4args4mkr, child_rgnr) = sf._mk_ex__child_recognizer_LLoo_(scene, acc4args4mkr)
        return (acc4args4mkr, child_rgnr)
    def update_accumulators_ex(sf, acc4args4mkr, acc4result6ok, result6ok4child_LLoo, /):
        'acc4args4mkr -> acc4result6ok -> result6ok4child_LLoo -> (acc4args4mkr, acc4result6ok, stopped/bool)'
        (acc4args4mkr, acc4result6ok, stopped) = sf._update_accumulators_ex_(acc4args4mkr, acc4result6ok, result6ok4child_LLoo)
        return (acc4args4mkr, acc4result6ok, stopped)
    def mk_may_header_signal_at_beginning(sf, acc4result6ok, num_consumed, inputter4child_begin, /):
        'acc4result6ok -> num_consumed/uint -> inputter4child_begin/IForkableForwardInputStream -> may Signal__HeaderCompleted'
        may_hdr_sgnl = sf._mk_may_header_signal_at_beginning_(acc4result6ok, num_consumed, inputter4child_begin)
        return may_hdr_sgnl
    def mk_may_header_signal5header_signal(sf, acc4result6ok, num_consumed, hdr_sgnl, /):
        'acc4result6ok -> num_consumed/uint -> hdr_sgnl/Signal__HeaderCompleted -> may Signal__HeaderCompleted'
        may_hdr_sgnl = sf._mk_may_header_signal5header_signal_(acc4result6ok, num_consumed, hdr_sgnl)
        return may_hdr_sgnl
    def mk_may_header_signal5ok_reply(sf, reply4LLoo, acc4result6ok, num_consumed, /):
        'reply4LLoo/Reply4IRecognizerLLoo -> acc4result6ok -> num_consumed/uint -> may Signal__HeaderCompleted'
        may_hdr_sgnl = sf._mk_may_header_signal5ok_reply_(reply4LLoo, acc4result6ok, num_consumed)
        return may_hdr_sgnl

class IRecognizerLLoo__serial_framework(IRecognizerLLoo):
    __slots__ = ()
    @abstractmethod
    def _finalize4serial_(sf, acc4result6ok, /):
        'acc4result6ok -> result6ok4whole_LLoo'
    @abstractmethod
    def _initialize4accumulators_ex_(sf, /):
        '-> (acc4args4mkr, acc4result6ok, stopped/bool)'
    @abstractmethod
    def _iter_child_items4serial_(sf, /):
        '-> Iter IChildItem4Serial4LLoo'
    @override
    def _iter4two_phases_recognize_(sf, inputter4whole, /):
        (acc4args4mkr, acc4result6ok, stopped) = sf._initialize4accumulators_ex_()
        child_items = sf._iter_child_items4serial_()
        if not child_items is iter(child_items):raise TypeError
        hdr_sgnl_occured = False
        inputter = inputter4whole
        num_consumed = 0
        def f(lazy_may_hdr_sgnl, /):
            nonlocal hdr_sgnl_occured
            ######################
            if not hdr_sgnl_occured:
                may_hdr_sgnl = lazy_may_hdr_sgnl()
                if not None is may_hdr_sgnl:
                    hdr_sgnl = may_hdr_sgnl
                    yield BoxedHalfwayResult(hdr_sgnl)
                    hdr_sgnl_occured = True
            ######################
        #end-def f(lazy_may_hdr_sgnl, /):
        #try:#StopIteration
        while not stopped:
            #child_item = next(child_items)
                # ^StopIteration
            for child_item in child_items:
                break
            else:
                break
            ######################
            if not hdr_sgnl_occured:
                yield from f(lambda:child_item.mk_may_header_signal_at_beginning(acc4result6ok, num_consumed, inputter4child_begin:=inputter))
            ######################
            (acc4args4mkr, child_rgnr) = child_item.mk_ex__child_recognizer_LLoo(sf.scene, acc4args4mkr)
            gi = child_rgnr.iter4two_phases_recognize(inputter)
            gi = mk_gi4either8xresult(gi)
            x = yield gi
            if x.is_left:
                hdr_sgnl = x.left
                check_type_is(Signal__HeaderCompleted, hdr_sgnl)
                ######################
                if not hdr_sgnl_occured:
                    yield from f(lambda:child_item.mk_may_header_signal5header_signal(acc4result6ok, num_consumed, hdr_sgnl))
                ######################
                y = yield gi
                if not y.is_right:
                    raise Error__not_Reply4IRecognizerLLoo_after_Signal__HeaderCompleted
                x = y
            assert x.is_right
            reply4LLoo = x.right
            check_type_is(Reply4IRecognizerLLoo, reply4LLoo)
            if not reply4LLoo.ok:
                return BoxedFinalResult(reply4LLoo)
            result6ok4child_LLoo = reply4LLoo.result
            (acc4args4mkr, acc4result6ok, stopped) = child_item.update_accumulators_ex(acc4args4mkr, acc4result6ok, result6ok4child_LLoo)
            num_consumed += reply4LLoo.num_consumed
            ######################
            if not hdr_sgnl_occured:
                yield from f(lambda:child_item.mk_may_header_signal5ok_reply(reply4LLoo, acc4result6ok, num_consumed))
            ######################
            inputter = reply4LLoo.the_inputter4end
            ######################

        #except StopIteration:
        #   pass
        result6ok4whole_LLoo = sf._finalize4serial_(acc4result6ok)
        return BoxedFinalResult(result6ok4whole_LLoo)



class TriboolTriple8cases4hdr_sgnl(tuple):
    def __new__(cls, tribool__hdr_sgnl_at_beginning, tribool__hdr_sgnl5hdr_sgnl, tribool__hdr_sgnl5ok_reply, /):
        sf = tuple.__new__(cls, [tribool__hdr_sgnl_at_beginning, tribool__hdr_sgnl5hdr_sgnl, tribool__hdr_sgnl5ok_reply])
        for t in sf:
            check_tribool(t)
        return sf
    @property
    def tribool__hdr_sgnl_at_beginning(sf, /):
        return sf[0]
    @property
    def tribool__hdr_sgnl5hdr_sgnl(sf, /):
        return sf[1]
    @property
    def tribool__hdr_sgnl5ok_reply(sf, /):
        return sf[2]
class ChildItem4Serial4LLoo__plain(IChildItem4Serial4LLoo):
    ___no_slots_ok___ = True
    #def __init__(sf, xcollector_ops, recognizer_LLoo, tribool_triple8cases4hdr_sgnl, /):
    def __init__(sf, scene, xcollector_ops, psmkr, tribool_triple8cases4hdr_sgnl, /):
        check_type_is(TriboolTriple8cases4hdr_sgnl, tribool_triple8cases4hdr_sgnl)
        check_type_le(IScene4LLoo, scene)
        check_type_le(IAsBiCollectorOps, xcollector_ops)
        #check_type_le(IRecognizerLLoo, recognizer_LLoo)
        _check_plain_psmkr_(psmkr)
        sf._scn = scene
        sf._xops = xcollector_ops
        #sf._rgnr = recognizer_LLoo
        sf._psmkr = psmkr
        sf._t3 = tribool_triple8cases4hdr_sgnl
    def __repr__(sf, /):
        return repr_helper(sf, sf._scn, sf._xops, sf._psmkr, sf._t3)
    @override
    def _mk_ex__child_recognizer_LLoo_(sf, scene, acc4args4mkr, /):
        'IScene4LLoo -> acc4args4mkr -> (acc4args4mkr, IRecognizerLLoo)'
        psmkr = sf._psmkr
        scene = sf._scn
        im = psmkr.imay_num_params_required
        if im == -1:
            rgnr = psmkr
        elif im == 0:
            rgnr = psmkr.mk_pseudo_mkr4recognizer_LLoo(scene)
        elif im == 1:
            rgnr = psmkr.mk_pseudo_mkr4recognizer_LLoo(scene, acc4args4mkr)
        else:
            raise 000
        return (acc4args4mkr, rgnr)
        return (acc4args4mkr, sf._rgnr)
    @override
    def _update_accumulators_ex_(sf, acc4args4mkr, acc4result6ok, result6ok4child_LLoo, /):
        'acc4args4mkr -> acc4result6ok -> result6ok4child_LLoo -> (acc4args4mkr, acc4result6ok, stopped/bool)'
        #check_type_le(IUnpacker, result6ok4child_LLoo)
        check_type_le(IAsBiUnpacker, result6ok4child_LLoo)
        xunpacker = result6ok4child_LLoo
        bi_unpacker = xunpacker.as_IBiUnpacker()
        bi_collector_ops = sf._xops.as_IBiCollectorOps()
        acc4args4mkr = bi_collector_ops.collector_ops4args4mkr.puts(acc4args4mkr, bi_unpacker.unpacker4args4mkr)
        acc4result6ok = bi_collector_ops.collector_ops4result.puts(acc4result6ok, bi_unpacker.unpacker4result)
        stopped = False
        return (acc4args4mkr, acc4result6ok, stopped)
    @override
    def _mk_may_header_signal_at_beginning_(sf, acc4result6ok, num_consumed, inputter4child_begin, /):
        'acc4result6ok -> num_consumed/uint -> inputter4child_begin/IForkableForwardInputStream -> may Signal__HeaderCompleted'
        t = sf._t3.tribool__hdr_sgnl_at_beginning
        if t is False:
            return None
        elif t is ...:
            #at_beginning ==>> [child num_consumed<child-until-now> == 0]
            return None
        elif t is True:
            return Signal__HeaderCompleted(num_consumed, inputter4child_begin, acc4result6ok)
        raise 000
    @override
    def _mk_may_header_signal5header_signal_(sf, acc4result6ok, num_consumed, hdr_sgnl, /):
        'acc4result6ok -> num_consumed/uint -> hdr_sgnl/Signal__HeaderCompleted -> may Signal__HeaderCompleted'
        t = sf._t3.tribool__hdr_sgnl5hdr_sgnl
        if t is False:
            return None
        elif t is ...:
            if hdr_sgnl.num_consumed == 0:
                return None
            else:
                pass
        elif t is True:
            pass
        else:
            raise 000
        return Signal__HeaderCompleted(num_consumed+hdr_sgnl.num_consumed, hdr_sgnl.the_inputter4body, (acc4result6ok, hdr_sgnl.the_result4header))
    @override
    def _mk_may_header_signal5ok_reply_(sf, reply4LLoo, acc4result6ok, num_consumed, /):
        'reply4LLoo/Reply4IRecognizerLLoo -> acc4result6ok -> num_consumed/uint -> may Signal__HeaderCompleted'
        t = sf._t3.tribool__hdr_sgnl5ok_reply
        if t is False:
            return None
        elif t is ...:
            if reply4LLoo.num_consumed == 0:
                return None
            else:
                pass
        elif t is True:
            pass
        else:
            raise 000
        return Signal__HeaderCompleted(num_consumed, reply4LLoo.the_inputter4end, acc4result6ok)
check_non_ABC(ChildItem4Serial4LLoo__plain)


def _check_plain_psmkr_(psmkr, /):
    check_type_le(IPseudoMaker4RecognizerLLoo, psmkr)
    if not -1 <= psmkr.imay_num_params_required < 2: raise TypeError
def _check_plain_psmkrs_(psmkrs, /):
    for psmkr in psmkrs:
        _check_plain_psmkr_(psmkr)
def _check_may_plain_psmkr_(may_psmkr, /):
    if not None is may_psmkr:
        _check_plain_psmkr_(may_psmkr)

_cases__forehead = TriboolTriple8cases4hdr_sgnl(False, False, False)
_cases__chin = TriboolTriple8cases4hdr_sgnl(False, ..., ...)
_cases__neck__last = TriboolTriple8cases4hdr_sgnl(False, True, True)
_cases__neck__nonlast = _cases__forehead
_cases__body__first = TriboolTriple8cases4hdr_sgnl(True, False, False)
_cases__body__nonfirst = _cases__forehead
class RecognizerLLoo__serial(IRecognizerLLoo__serial_framework):
    r'''[[[
    #serial/tuple
    [scene :: IScene4LLoo]
    [xcollector_ops :: IAsBiCollectorOps]
    [rgnr :: IRecognizerLLoo]
    [psmkr :: IPseudoMaker4RecognizerLLoo/(IMaker4RecognizerLLoo|IRecognizerLLoo)]
    [hdr_sgnl :: Signal__HeaderCompleted]]
    [forehead - ignore hdr_sgnl]
    [chin - (forward first hdr_sgnl|wrap first reply4LLoo) which consume input]
    [neck - forward last hdr_sgnl if chin consume nothing]
    [body - yield hdr_sgnl at beginning if chin&neck donot]
    [result6ok4LLoo===Reply4IRecognizerLLoo.result :: IAsBiUnpacker]
    #]]]'''#'''
    #xxx:[result6ok4LLoo===Reply4IRecognizerLLoo.result :: (IUnpacker|IBiUnpacker)]
    ___no_slots_ok___ = True
    #def __init__(sf, scene, xcollector_ops, rgnrs8forehead, rgnrs8chin, rgnrs8neck, rgnrs8body, /):
    def __init__(sf, scene, xcollector_ops, xunpacker, psmkrs8forehead, psmkrs8chin, psmkrs8neck, psmkrs8body, /):
        check_type_le(IScene4LLoo, scene)
        check_type_le(IAsBiCollectorOps, xcollector_ops)
        check_type_le(IAsBiUnpacker, xunpacker)
        psmkrs8forehead = mk_tuple(psmkrs8forehead)
        psmkrs8chin = mk_tuple(psmkrs8chin)
        psmkrs8neck = mk_tuple(psmkrs8neck)
        psmkrs8body = mk_tuple(psmkrs8body)

        _check_plain_psmkrs_(psmkrs8forehead)
        _check_plain_psmkrs_(psmkrs8chin)
        _check_plain_psmkrs_(psmkrs8neck)
        _check_plain_psmkrs_(psmkrs8body)

        sf._args = (scene, xcollector_ops, xunpacker, psmkrs8forehead, psmkrs8chin, psmkrs8neck, psmkrs8body)
    def __repr__(sf, /):
        return repr_helper(sf, *sf._args)
    @property
    def xunpacker(sf, /):
        '-> IAsBiUnpacker'
        return sf._args[2]
    @property
    def xcollector_ops(sf, /):
        '-> IAsBiCollectorOps'
        return sf._args[1]
    @property
    @override
    def scene(sf, /):
        '-> IScene4LLoo'
        return sf._args[0]
    @override
    def _finalize4serial_(sf, acc4result6ok, /):
        'acc4result6ok -> result6ok4whole_LLoo'
        bi_collector_ops = sf.xcollector_ops.as_IBiCollectorOps()
        return bi_collector_ops.collector_ops4result.finalize_collect(acc4result6ok)
    @override
    def _initialize4accumulators_ex_(sf, /):
        '-> (acc4args4mkr, acc4result6ok, stopped/bool)'
        #acc4args4mkr = None
        bi_collector_ops = sf.xcollector_ops.as_IBiCollectorOps()
        acc4args4mkr = bi_collector_ops.collector_ops4args4mkr.mk_empty_inner_container()
        acc4result6ok = bi_collector_ops.collector_ops4result.mk_empty_inner_container()
        stopped = False
        bi_unpacker = sf.xunpacker.as_IBiUnpacker()
        acc4args4mkr = bi_collector_ops.collector_ops4args4mkr.puts(acc4args4mkr, bi_unpacker.unpacker4args4mkr)
        acc4result6ok = bi_collector_ops.collector_ops4result.puts(acc4result6ok, bi_unpacker.unpacker4result)
        return (acc4args4mkr, acc4result6ok, stopped)
    @override
    def _iter_child_items4serial_(sf, /):
        '-> Iter IChildItem4Serial4LLoo'
        (scene, xcollector_ops, xunpacker, psmkrs8forehead, psmkrs8chin, psmkrs8neck, psmkrs8body) = sf._args
        for psmkr in psmkrs8forehead:
            yield ChildItem4Serial4LLoo__plain(scene, xcollector_ops, psmkr, _cases__forehead)
        for psmkr in psmkrs8chin:
            yield ChildItem4Serial4LLoo__plain(scene, xcollector_ops, psmkr, _cases__chin)

        L = len(psmkrs8neck)
        for sz, psmkr in enumerate(psmkrs8neck, 1):
            yield ChildItem4Serial4LLoo__plain(scene, xcollector_ops, psmkr, _cases__neck__nonlast if not sz == L else _cases__neck__last)

        L = len(psmkrs8body)
        for i, psmkr in enumerate(psmkrs8body):
            yield ChildItem4Serial4LLoo__plain(scene, xcollector_ops, psmkr, _cases__body__first if i == 0 else _cases__body__nonfirst)

    @override
    def _iter_directly_used_kinded_names_(sf, /):
        '-> Iter (kind, name)'
        return null_iter
    @override
    def _iter_directly_used_IRequiredSceneAsClosure_(sf, /):
        '-> Iter IRequiredSceneAsClosure'
        (scene, xcollector_ops, xunpacker, psmkrs8forehead, psmkrs8chin, psmkrs8neck, psmkrs8body) = sf._args
        yield from psmkrs8forehead
        yield from psmkrs8chin
        yield from psmkrs8neck
        yield from psmkrs8body
check_non_ABC(RecognizerLLoo__serial)




r'''[[[
######################
end_by
between
many0
many1
skip_many1
optional__tmay
    #skip_optional
sep_by
sep_end_by


######################
dependent_pair #do_if
loop_while #sep_by1
loop_until #end_by1
while_loop #many0(sep+body)
until_loop #end_by0
do_if
do_unless
    #do_ifnot
if_then_else
    #flip => ifnot_then_else #unless_then_else
#]]]'''#'''

RecognizerLLoo__optional__tmay
class RecognizerLLoo__end_by(IRecognizerLLoo__serial_framework):
    '#end_by0/array'
    ___no_slots_ok___ = True
RecognizerLLoo__the_first_one__tagged
    def __init__(sf, scene, xcollector_ops, xunpacker, may_psmkr8end_mark7pre_body, psmkr8loop_body, may_psmkr8end_mark7post_body, /):
        check_type_le(IScene4LLoo, scene)
        check_type_le(IAsBiCollectorOps, xcollector_ops)
        check_type_le(IAsBiUnpacker, xunpacker)

        _check_may_plain_psmkr_(may_psmkr8end_mark7pre_body)
        _check_plain_psmkr_(psmkr8loop_body)
        _check_may_plain_psmkr_(may_psmkr8end_mark7post_body)
        sf._args = (scene, xcollector_ops, xunpacker, may_psmkr8end_mark7pre_body, psmkr8loop_body, may_psmkr8end_mark7post_body)
        . .
        if may_psmkr8end_mark7pre_body is None:
        RecognizerLLoo__the_first_one__tagged()
    def __repr__(sf, /):
        return repr_helper(sf, *sf._args)
    . .
        . .
        . .
        . .
    @property
    def xunpacker(sf, /):
        '-> IAsBiUnpacker'
        return sf._args[2]
    @property
    def xcollector_ops(sf, /):
        '-> IAsBiCollectorOps'
        return sf._args[1]
    @property
    @override
    def scene(sf, /):
        '-> IScene4LLoo'
        return sf._args[0]
    @override
    def _finalize4serial_(sf, acc4result6ok, /):
        'acc4result6ok -> result6ok4whole_LLoo'
        bi_collector_ops = sf.xcollector_ops.as_IBiCollectorOps()
        return bi_collector_ops.collector_ops4result.finalize_collect(acc4result6ok)
    @override
    def _initialize4accumulators_ex_(sf, /):
        '-> (acc4args4mkr, acc4result6ok, stopped/bool)'
        #acc4args4mkr = None
        bi_collector_ops = sf.xcollector_ops.as_IBiCollectorOps()
        acc4args4mkr = bi_collector_ops.collector_ops4args4mkr.mk_empty_inner_container()
        acc4result6ok = bi_collector_ops.collector_ops4result.mk_empty_inner_container()
        stopped = False
        bi_unpacker = sf.xunpacker.as_IBiUnpacker()
        acc4args4mkr = bi_collector_ops.collector_ops4args4mkr.puts(acc4args4mkr, bi_unpacker.unpacker4args4mkr)
        acc4result6ok = bi_collector_ops.collector_ops4result.puts(acc4result6ok, bi_unpacker.unpacker4result)
        return (acc4args4mkr, acc4result6ok, stopped)
    @override
    def _iter_child_items4serial_(sf, /):
        '-> Iter IChildItem4Serial4LLoo'
        (scene, xcollector_ops, xunpacker, psmkrs8forehead, psmkrs8chin, psmkrs8neck, psmkrs8body) = sf._args
        for psmkr in psmkrs8forehead:
            yield ChildItem4Serial4LLoo__plain(scene, xcollector_ops, psmkr, _cases__forehead)
        for psmkr in psmkrs8chin:
            yield ChildItem4Serial4LLoo__plain(scene, xcollector_ops, psmkr, _cases__chin)

        L = len(psmkrs8neck)
        for sz, psmkr in enumerate(psmkrs8neck, 1):
            yield ChildItem4Serial4LLoo__plain(scene, xcollector_ops, psmkr, _cases__neck__nonlast if not sz == L else _cases__neck__last)

        L = len(psmkrs8body)
        for i, psmkr in enumerate(psmkrs8body):
            yield ChildItem4Serial4LLoo__plain(scene, xcollector_ops, psmkr, _cases__body__first if i == 0 else _cases__body__nonfirst)

    @override
    def _iter_directly_used_kinded_names_(sf, /):
        '-> Iter (kind, name)'
        return null_iter
    @override
    def _iter_directly_used_IRequiredSceneAsClosure_(sf, /):
        '-> Iter IRequiredSceneAsClosure'
        (scene, xcollector_ops, xunpacker, psmkrs8forehead, psmkrs8chin, psmkrs8neck, psmkrs8body) = sf._args
        yield from psmkrs8forehead
        yield from psmkrs8chin
        yield from psmkrs8neck
        yield from psmkrs8body
check_non_ABC(RecognizerLLoo__end_by)

class RecognizerLLoo__many(IRecognizerLLoo__serial_framework):
    '#many0/array'

__all__
from seed.recognize.recognizer_LLoo_.combinator_LLoo__serial import *
