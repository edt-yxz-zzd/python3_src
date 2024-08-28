#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/recognizer_LLoo_/combinator_LLoo__wrapper.py

seed.recognize.recognizer_LLoo_.combinator_LLoo__wrapper
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_LLoo_.combinator_LLoo__wrapper -x
py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LLoo_.combinator_LLoo__wrapper:__doc__ -ht
py_adhoc_call   seed.recognize.recognizer_LLoo_.combinator_LLoo__wrapper   @f
from seed.recognize.recognizer_LLoo_.combinator_LLoo__wrapper import *
#]]]'''
__all__ = r'''
RecognizerLLoo__tag
RecognizerLLoo__skip
RecognizerLLoo__invert_err_ok


IRecognizerLLoo__try
    RecognizerLLoo__try
    RecognizerLLoo__optional__tmay

RecognizerLLoo__look_ahead__no_err4hdr
    RecognizerLLoo__look_ahead__no_err4whole
RecognizerLLoo__look_ahead4hdr
    RecognizerLLoo__look_ahead4whole
RecognizerLLoo__not_followed_by4hdr
    RecognizerLLoo__not_followed_by4whole


'''.split()#'''
__all__



r'''[[[
#anchor
not_followed_by4whole
look_ahead4whole
not_followed_by4hdr
look_ahead4hdr
look_ahead__no_err4hdr
look_ahead__no_err4whole

#anchor@fail-before-hdr_sgnl,move_on@succ/fail-after-hdr_sgnl
try

#move_on
skip
invert_err_ok


????
constant
constant_overwrite6ok

wrapper4postprocess
wrapper4postprocess6ok
wrapper4serial_collector
trace6enter
trace6exit
trace6err
trace6exc
trace6ok


#]]]'''#'''

from seed.recognize.recognizer_LLoo_.interface_LLoo import IRecognizerLLoo, IRecognizerLLoo__wrapper, IPseudoMaker4RecognizerLLoo__wrapper__single_ref
from seed.recognize.recognizer_LLoo_.interface_LLoo import Reply4IRecognizerLLoo, unpacker__ignore
from seed.tiny_.check import check_type_is, check_int_ge, check_non_ABC


from seed.func_tools.recur5yield import mk_gi4return
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




class _IRecognizerLLoo__wrapper__single_ref(IRecognizerLLoo__wrapper, IPseudoMaker4RecognizerLLoo__wrapper__single_ref):
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        return repr_helper(sf, sf._rgnr)
    def __init__(sf, rgnr, /):
        check_type_le(IRecognizerLLoo, rgnr)
        sf._rgnr = rgnr
    @property
    @override
    def the_wrapped_obj(sf, /):
        '-> wrapped_obj'
        return sf._rgnr










class RecognizerLLoo__tag(_IRecognizerLLoo__wrapper__single_ref):
    'tag:cased...'
    def __init__(sf, tag, rgnr, /):
        sf._tg = tag
        super().__init__(rgnr)
    @property
    def tag(sf, /):
        return sf._tg

    #@override
    may_preprocess = None
    #@override
    may_header_signal_process = None
    @override
    def may_postprocess(sf, state, reply4LLoo, /):
        '-> may postprocess/YS_GI(state -> Reply4IRecognizerLLoo -> Reply4IRecognizerLLoo)'
        new_eresult = reply4LLoo.the_eresult.fmap4payload(lambda x:(sf.tag, x))
        reply4LLoo = reply4LLoo.ireplace__eresult(new_eresult)
        return reply4LLoo
check_non_ABC(RecognizerLLoo__tag)














class RecognizerLLoo__skip(_IRecognizerLLoo__wrapper__single_ref):
    'skip'
    #@override
    may_preprocess = None

    #@override
    may_header_signal_process = None

    @override
    def may_postprocess(sf, state, reply4LLoo, /):
        '-> may postprocess/YS_GI(state -> Reply4IRecognizerLLoo -> Reply4IRecognizerLLoo)'
        if reply4LLoo.ok:
            reply4LLoo = reply4LLoo.ireplace__result(unpacker__ignore)
        return BoxedFinalResult(reply4LLoo)
        777;   yield
check_non_ABC(RecognizerLLoo__skip)



class RecognizerLLoo__invert_err_ok(_IRecognizerLLoo__wrapper__single_ref):
    'invert_err_ok'
    #@override
    may_preprocess = None

    #@override
    may_header_signal_process = None

    @override
    def may_postprocess(sf, state, reply4LLoo, /):
        '-> may postprocess/YS_GI(state -> Reply4IRecognizerLLoo -> Reply4IRecognizerLLoo)'
        reply4LLoo = ~reply4LLoo
        return BoxedFinalResult(reply4LLoo)
        777;   yield
check_non_ABC(RecognizerLLoo__invert_err_ok)






















class IRecognizerLLoo__try(_IRecognizerLLoo__wrapper__single_ref):
    'try:[fail-before-hdr_sgnl<==>not ok]'
    @override
    def may_preprocess(sf, inputter4whole, /):
        '-> may preprocess/YS_GI(inputter4whole -> (state, inputter4whole))'
        state = inputter4whole.fork()
        return BoxedFinalResult((state, inputter4whole))
        777;   yield
    @override
    def may_header_signal_process(sf, state, hdr_sgnl, tail_gi_after_hdr_sgnl, /):
        '-> may header_signal_process/YS_GI(state -> hdr_sgnl/Signal__HeaderCompleted -> tail_gi_after_hdr_sgnl -> (state, may hdr_sgnl, tail_gi_after_hdr_sgnl))'
        state = None#del#free-memory
        may_hdr_sgnl = hdr_sgnl
        return BoxedFinalResult((state, may_hdr_sgnl, tail_gi_after_hdr_sgnl))
        777;   yield
    @override
    def may_postprocess(sf, state, reply4LLoo, /):
        '-> may postprocess/YS_GI(state -> Reply4IRecognizerLLoo -> Reply4IRecognizerLLoo)'
        if reply4LLoo.ok or state is None:
            #succ or fail-after-hdr_sgnl
            reply4LLoo = reply4LLoo.ilift()
            return BoxedFinalResult()
        else:
            #fail-before-hdr_sgnl
            inputter4whole = state
            reply4LLoo = ~reply4LLoo.ilift__(num_consumed:=0, inputter4end:=inputter4whole)
        reply4LLoo
        return BoxedFinalResult(reply4LLoo)
        777;   yield
    @abstractmethod
    def postpostprocess(sf, reply4LLoo, /):
        'Reply4IRecognizerLLoo -> Reply4IRecognizerLLoo'
class RecognizerLLoo__try(IRecognizerLLoo__try):
    'try:[fail-before-hdr_sgnl<==>not ok]'
    @override
    def postpostprocess(sf, reply4LLoo, /):
        'Reply4IRecognizerLLoo -> Reply4IRecognizerLLoo'
        return reply4LLoo
check_non_ABC(RecognizerLLoo__try)

class RecognizerLLoo__optional__tmay(IRecognizerLLoo__try):
    'optional__tmay:[fail-after-hdr_sgnl<==>not ok]'
    @override
    def postpostprocess(sf, reply4LLoo, /):
        'Reply4IRecognizerLLoo -> Reply4IRecognizerLLoo'
        if reply4LLoo.ok:
            #succ or fail-after-hdr_sgnl
            reply4LLoo = reply4LLoo.result
            check_type_is(Reply4IRecognizerLLoo, reply4LLoo)
            if reply4LLoo.ok:
                #succ
                result6ok = reply4LLoo.result
                tmay_result6ok = (result6ok,)
                reply4LLoo = reply4LLoo.ireplace__result(tmay_result6ok)
            else:
                #fail-after-hdr_sgnl
                # [not ok]
                reply4LLoo
                pass
            reply4LLoo
        else:
            #fail-before-hdr_sgnl
            tmay_result6ok = null_tuple
            reply4LLoo = reply4LLoo.ireplace__result(tmay_result6ok)
        reply4LLoo
        return reply4LLoo
check_non_ABC(RecognizerLLoo__optional__tmay)













class _IRecognizerLLoo__look_ahead(_IRecognizerLLoo__wrapper__single_ref):
    @property
    @abstractmethod
    def no_err(sf, /):
        '-> bool'
    @property
    @abstractmethod
    def to_inv_ok(sf, /):
        '-> bool # perform after no_err'
    @property
    @abstractmethod
    def hdr_vs_whole(sf, /):
        '-> bool'

    @override
    def may_preprocess(sf, inputter4whole, /):
        '-> may preprocess/YS_GI(inputter4whole -> (state, inputter4whole))'
        state = inputter4whole.fork()
        return BoxedFinalResult((state, inputter4whole))
        777;   yield
    @override
    def may_header_signal_process(sf, state, hdr_sgnl, tail_gi_after_hdr_sgnl, /):
        '-> may header_signal_process/YS_GI(state -> hdr_sgnl/Signal__HeaderCompleted -> tail_gi_after_hdr_sgnl -> (state, may hdr_sgnl, tail_gi_after_hdr_sgnl))'
        inputter4whole = state
        if sf.hdr_vs_whole:
            #look_ahead4whole
            may_hdr_sgnl = hdr_sgnl.ilift__(num_consumed:=0, inputter4body:=state)
            return BoxedFinalResult((state, may_hdr_sgnl, tail_gi_after_hdr_sgnl))
        #look_ahead4hdr
        reply4LLoo = Reply4IRecognizerLLoo(num_consumed:=0, inputter4end:=inputter4whole, Either.from_right(hdr_sgnl))
        if sf.to_inv_ok:
            reply4LLoo = ~reply4LLoo
        may_hdr_sgnl = None
        tail_gi_after_hdr_sgnl = mk_gi4return(BoxedFinalResult(reply4LLoo))
        return BoxedFinalResult((state, may_hdr_sgnl, tail_gi_after_hdr_sgnl))
        777;   yield
    @override
    def may_postprocess(sf, state, reply4LLoo, /):
        '-> may postprocess/YS_GI(state -> Reply4IRecognizerLLoo -> Reply4IRecognizerLLoo)'
        #succ/fail-before-hdr_sgnl
        inputter4whole = state
        ok = reply4LLoo.ok
        reply4LLoo = reply4LLoo.ilift__(num_consumed:=0, inputter4end:=inputter4whole)
        to_inv_ok = bool(sf.to_inv_ok) ^ (not (sf.no_err or ok))
        if to_inv_ok:
            reply4LLoo = ~reply4LLoo
        return BoxedFinalResult(reply4LLoo)
        777;   yield




class RecognizerLLoo__look_ahead__no_err4hdr(_IRecognizerLLoo__look_ahead):
    'look_ahead__no_err4hdr'
    no_err = True
    to_inv_ok = False
    hdr_vs_whole = False
check_non_ABC(RecognizerLLoo__look_ahead__no_err4hdr)


class RecognizerLLoo__look_ahead__no_err4whole(_IRecognizerLLoo__look_ahead):
    'look_ahead__no_err4whole'
    no_err = True
    to_inv_ok = False
    hdr_vs_whole = True
check_non_ABC(RecognizerLLoo__look_ahead__no_err4whole)


class RecognizerLLoo__look_ahead4hdr(_IRecognizerLLoo__look_ahead):
    'look_ahead4hdr'
    no_err = False
    to_inv_ok = False
    hdr_vs_whole = False
check_non_ABC(RecognizerLLoo__look_ahead4hdr)


class RecognizerLLoo__look_ahead4whole(_IRecognizerLLoo__look_ahead):
    'look_ahead4whole'
    no_err = False
    to_inv_ok = False
    hdr_vs_whole = True
check_non_ABC(RecognizerLLoo__look_ahead4whole)










#class RecognizerLLoo__not_followed_by__no_err4hdr(_IRecognizerLLoo__look_ahead):
#    'not_followed_by__no_err4hdr'
#    no_err = True
#    to_inv_ok = True
#    hdr_vs_whole = False
#check_non_ABC(RecognizerLLoo__not_followed_by__no_err4hdr)
#
#
#class RecognizerLLoo__not_followed_by__no_err4whole(_IRecognizerLLoo__look_ahead):
#    'not_followed_by__no_err4whole'
#    no_err = True
#    to_inv_ok = True
#    hdr_vs_whole = True
#check_non_ABC(RecognizerLLoo__not_followed_by__no_err4whole)


class RecognizerLLoo__not_followed_by4hdr(_IRecognizerLLoo__look_ahead):
    'not_followed_by4hdr'
    no_err = False
    to_inv_ok = True
    hdr_vs_whole = False
check_non_ABC(RecognizerLLoo__not_followed_by4hdr)


class RecognizerLLoo__not_followed_by4whole(_IRecognizerLLoo__look_ahead):
    'not_followed_by4whole'
    no_err = False
    to_inv_ok = True
    hdr_vs_whole = True
check_non_ABC(RecognizerLLoo__not_followed_by4whole)




















__all__
from seed.recognize.recognizer_LLoo_.combinator_LLoo__wrapper import *
