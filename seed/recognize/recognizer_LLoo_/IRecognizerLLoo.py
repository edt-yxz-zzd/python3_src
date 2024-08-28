#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/recognizer_LLoo_/IRecognizerLLoo.py

seed.recognize.recognizer_LLoo_.IRecognizerLLoo
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_LLoo_.IRecognizerLLoo -x
py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LLoo_.IRecognizerLLoo:__doc__ -ht


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

from seed.types.ForkableForwardInputStream import IForkable, IForkable__stamp, IForkableForwardInputStream, ForkableForwardInputStream__using_LazyListIter
]]
[[
refactor:iter4two_phases_recognize() using halfway_result#BoxedHalfwayResult
view ../../python3_src/seed/func_tools/recur5yield__halfway.py
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
view ../../python3_src/seed/func_tools/recur5yield__halfway.py
    #[:___main_exports___]:goto
######################
from seed.func_tools.recur5yield__halfway import bind_gi_with_the_following_first_value4send, mk_gi4either8xresult, mk_gi4xresult_xexception
from seed.func_tools.recur5yield__halfway import BoxedHalfwayResult, BoxedException__halfway, BoxedException__final, BoxedException__through, Escaped, BoxedTailRecur, BoxedFinalResult
from seed.func_tools.recur5yield__halfway import EFlowControl, EFinal, EHalfway, mk_boxed_EFinal, mk_boxed_EHalfway
from seed.func_tools.recur5yield__halfway import recur5yield__list__echo__echo
### from seed.types.Either import Either
######################

]]


#]]]'''
__all__ = r'''
Error4IRecognizerLLoo
    ParallelError4IRecognizerLLoo
        Error__not_only_one_match
    LogicError4IRecognizerLLoo
        Error__not_Reply4IRecognizerLLoo_after_Signal__HeaderCompleted
        Error__inputter_changed
    TypeError4IRecognizerLLoo
        Error__too_few_args
        Error__too_many_args
KindError
LookupError__circle_ref

IScene
    IScene__register

IDependentTreeNode
    IDependentTreeNode__no_ref
        IDependentTreeNode__leaf
    IDependentTreeNode__no_children
        IDependentTreeNode__leaf
        IDependentTreeNode__ref
    IDependentTreeNode__wrapper

IWithScene
INamed
IWrapper
    ILazyWrapper
        IDependentTreeNode__ref

TmpSnapshot4Inputter
BaseReply
    Signal__HeaderCompleted
    Reply4IRecognizerLLoo

IRecognizerLLoo
    IRecognizerLLoo__no_ref
        IRecognizerLLoo__leaf
    IRecognizerLLoo__no_children
        IRecognizerLLoo__leaf

BaseHandler4gi4two_phases_recognize
    parse__via_IRecognizerLLoo
    mk_gi4skip_header_signal
    mk_gi4header_signal_at_beginning
    mk_gi4patch_header_signal_if_ok
    mk_gi4validate_two_phases

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...

from seed.recognize.recognizer_LLoo_._common import (IGeneratorIterator

,mk_gi4either8xresult, detach_asif_new_gi_wrapper
,BoxedHalfwayResult, BoxedException__halfway, BoxedException__final, BoxedException__through, Escaped, BoxedTailRecur, BoxedFinalResult
,EFlowControl, EFinal, EHalfway, mk_boxed_EFinal, mk_boxed_EHalfway
,recur5yield__list__echo__echo
,Cased, Either, mk_Left, mk_Right

,check_type_is, check_type_le, check_int_ge
,null_iter, null_tuple, mk_tuple

,IForkable, IForkable__stamp
,IGeneratorIterator

,abstractmethod, override, ABC, ABC__no_slots
,repr_helper# _Base4repr
)


___end_mark_of_excluded_global_names__0___ = ...
from seed.recognize.recognizer_LLoo_.IScene import \
(KindError
,LookupError__circle_ref
,IWithScene
,IScene
,    IScene__register
,INamed
,IWrapper
,    ILazyWrapper
,IDependentTreeNode
,    IDependentTreeNode__no_ref
,    IDependentTreeNode__no_children
,        IDependentTreeNode__leaf
,    IDependentTreeNode__wrapper
,    IDependentTreeNode__ref
)







class Error4IRecognizerLLoo(Exception):pass
class ParallelError4IRecognizerLLoo(Error4IRecognizerLLoo):pass
class Error__not_only_one_match(ParallelError4IRecognizerLLoo):pass
class LogicError4IRecognizerLLoo(Error4IRecognizerLLoo):pass
class Error__not_Reply4IRecognizerLLoo_after_Signal__HeaderCompleted(LogicError4IRecognizerLLoo):
    "LogicError4IRecognizerLLoo('not Reply4IRecognizerLLoo after Signal__HeaderCompleted')"
    pass
class Error__inputter_changed(LogicError4IRecognizerLLoo):pass

class TypeError4IRecognizerLLoo(Error4IRecognizerLLoo):pass
class Error__too_few_args(TypeError4IRecognizerLLoo):pass
class Error__too_many_args(TypeError4IRecognizerLLoo):pass





















class TmpSnapshot4Inputter:
    def __repr__(sf, /):
        return repr_helper(sf, sf._i, _may_stamp=sf._s)
    def __init__(sf, inputter:IForkable__stamp, /, *, _may_stamp=None):
        check_type_le(IForkable__stamp, inputter)
        stamp = _may_stamp if not _may_stamp is None else inputter.get_stamp()
        sf._i = inputter
        sf._s = stamp
        #if _may_stamp is None: assert sf.the_inputter is inputter
    @property
    def inputter_changed(sf, /):
        '-> bool'
        inputter = sf._i
        stamp = sf._s
        return inputter.has_changed_since_stamp_(stamp)
    @property
    def the_inputter(sf, /):
        '-> IForkable__stamp|^Error__inputter_changed'
        if sf.inputter_changed:raise Error__inputter_changed
        return sf._i
    def unsafe_get_the_inputter(sf, /):
        '-> IForkable__stamp'
        return sf._i

class BaseReply:
    '[xinputter :: (IForkable__stamp|TmpSnapshot4Inputter)]'
    def __init__(sf, xinputter:[IForkable__stamp,TmpSnapshot4Inputter], payload, /):
        'xinputter/(IForkable__stamp|TmpSnapshot4Inputter) -> payload -> None'
        if not type(xinputter) is TmpSnapshot4Inputter:
            xinputter = TmpSnapshot4Inputter(xinputter)
        check_type_is(TmpSnapshot4Inputter, xinputter)
        sf._tmp = xinputter
        sf._pd = payload
    def __repr__(sf, /):
        return repr_helper(sf, sf._tmp, sf._pd)
    @property
    def _tmp_snapshot4inputter_(sf, /):
        '-> TmpSnapshot4Inputter'
        return sf._tmp
    @property
    def _inputter_(sf, /):
        '-> IForkable__stamp | ^Error__inputter_changed'
        return sf._tmp.the_inputter
    @property
    def _payload_(sf, /):
        '-> payload'
        return sf._pd
    def ireplace__xinputter(sf, xinputter, /):
        'xinputter/(IForkable__stamp|TmpSnapshot4Inputter) -> ot/BaseReply'
        if xinputter is (tmp:=sf._tmp_snapshot4inputter_) or (xinputter is tmp.unsafe_get_the_inputter() and not tmp.inputter_changed()):
            return sf
        return type(sf)(xinputter, sf._payload_)
    def ireplace__payload(sf, payload, /):
        'payload -> ot/BaseReply'
        if payload is sf._payload_:
            return sf
        return type(sf)(sf._tmp_snapshot4inputter_, payload)
    def ilift(sf, /):
        '-> ot/BaseReply'
        raise 000
        return sf.ireplace__payload(sf)
    def ilift_(sf, xinputter, /):
        '-> ot/BaseReply'
        #used by:look_ahead
        return sf.ilift().ireplace__xinputter(xinputter)
    def __pos__(sf, /):
        '-> ot/BaseReply #+sf'
        return sf.ilift()




class Signal__HeaderCompleted(BaseReply):
    def __init__(sf, xinputter4body:[IForkable__stamp,TmpSnapshot4Inputter], hresult, /):
        'xinputter4body/(IForkable__stamp|TmpSnapshot4Inputter) -> hresult -> None'
        super().__init__(xinputter4body, hresult)
    @property
    def the_inputter4body(sf, /):
        '-> end_of_header/begin_of_body/IForkable__stamp | ^Error__inputter_changed'
        return sf._inputter_
    @property
    def the_hresult(sf, /):
        '-> hresult/result4header'
        return sf._payload_
    def ireplace__xinputter4body(sf, xinputter4body, /):
        'xinputter4body -> Signal__HeaderCompleted'
        return sf.ireplace__xinputter(xinputter4body)
    def ireplace__hresult(sf, hresult, /):
        'hresult -> Signal__HeaderCompleted'
        return sf.ireplace__payload(hresult)
    @override
    def ilift(sf, /):
        '-> ot/BaseReply'
        return sf.ireplace__payload(sf)


class Reply4IRecognizerLLoo(BaseReply):
    'reply4LLoo/Reply[;inputter,errmsg,oresult/rfr/raw_final_result;]'
    #class Result4IRecognizerLLoo:
    #class RecognizeResult:
    #def __init__(sf, forkable8inputter4end, err_vs_ok:bool, errmsg_or_oresult, /):
    def __init__(sf, xinputter4end:[IForkable__stamp,TmpSnapshot4Inputter], eresult:Either, /):
        'xinputter4end/(IForkable__stamp|TmpSnapshot4Inputter) -> eresult/either_errmsg_or_oresult/Either[;errmsg,oresult/raw_final_result;] -> None'
        check_type_is(Either, eresult)
        super().__init__(xinputter4end, eresult)
    def to_Signal__HeaderCompleted(sf, /):
        '-> Signal__HeaderCompleted'
        return Signal__HeaderCompleted(sf._tmp_snapshot4inputter_, sf._payload_)
    @property
    def the_inputter4end(sf, /):
        '-> IForkable__stamp/(end_of_whole/end_of_body if sf.ok else end_of_err) | ^Error__inputter_changed'
        return sf._inputter_
    @property
    def the_eresult(sf, /):
        '-> eresult/either_errmsg_or_oresult/Either(;errmsg, oresult;)'
        return sf._payload_
    @property
    def ok(sf, /):
        '-> err_vs_ok/bool'
        return sf.the_eresult.case
    @property
    def errmsg_or_oresult(sf, /):
        '-> errmsg_or_oresult/(errmsg if not sf.ok else oresult)'
        return sf.the_eresult.payload
    @property
    def errmsg(sf, /):
        '-> (errmsg if not sf.ok else ^AttributeError)'
        return sf.the_eresult.left
    @property
    def oresult(sf, /):
        '-> (oresult/result6ok if sf.ok else ^AttributeError)'
        return sf.the_eresult.right
    def ireplace__xinputter4end(sf, xinputter4end, /):
        'xinputter4end -> Reply4IRecognizerLLoo'
        return sf.ireplace__xinputter(xinputter4end)
    def ireplace__eresult(sf, eresult, /):
        'eresult/Either -> Reply4IRecognizerLLoo'
        return sf.ireplace__payload(eresult)
    def iflip__ok(sf, /):
        '-> Reply4IRecognizerLLoo'
        return sf.ireplace__eresult(~sf.the_eresult)
    def ireplace__oresult(sf, oresult, /):
        'oresult/result6ok4LLoo -> Reply4IRecognizerLLoo | ^AttributeError'
        #if not sf.ok:raise AttributeError
        if oresult is sf.oresult:
            #^ AttributeError
            return sf
        return sf.ireplace__eresult(mk_Right(oresult))
    def __invert__(sf, /):
        '-> Reply4IRecognizerLLoo #~sf'
        return sf.iflip__ok()
    @override
    def ilift(sf, /):
        '-> ot/BaseReply'
        return sf.ireplace__payload(mk_Right(sf))





class IRecognizerLLoo(IDependentTreeNode):
    __slots__ = ()
    #@property
    #___666_tribool_skip4serial4LLoo_999___ = False # False-append;True-skip;...-extend
    @property
    @abstractmethod
    def ___666_tribool_skip4serial4LLoo_999___(sf, /):
        '-> tribool # False-append;True-skip;...-extend'


    @abstractmethod
    def _iter4two_phases_recognize_(sf, inputter4whole, /):
        r'''[[[
        :: inputter4whole/begin_of_whole/begin_of_header/IForkable__stamp
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
    def iter4two_phases_recognize(sf, inputter4whole, /):
        check_type_le(IForkable__stamp, inputter4whole)
        gi = sf._iter4two_phases_recognize_(inputter4whole)
        check_type_le(IGeneratorIterator, gi)
        return gi
    iter4two_phases_recognize.__doc__ = _iter4two_phases_recognize_.__doc__
    def iter4one_phase_recognize(sf, inputter4whole, /):
        '-> gi4one_phase_recognize #skip_header_signal'
        gi4two_phases_recognize = sf.iter4two_phases_recognize(inputter4whole)
        gi4one_phase_recognize = mk_gi4skip_header_signal(gi4two_phases_recognize)
        return gi4one_phase_recognize
    def iter4unpack_oresult4serial4LLoo(sf, oresult, /):
        'oresult -> Iter item4serial # [sf is child of serial4LLoo]'
        c = sf.___666_tribool_skip4serial4LLoo_999___
        if c is False:
            #append
            yield oresult
        elif c is True:
            #skip
            pass
        elif c is ...:
            #extend
            yield from oresult
        else:
            raise TypeError((type(c), type(sf), sf))
        return
#end-class IRecognizerLLoo(IPseudoMaker4RecognizerLLoo):

class IRecognizerLLoo__no_ref(IRecognizerLLoo, IDependentTreeNode__no_ref):
    __slots__ = ()
class IRecognizerLLoo__no_children(IRecognizerLLoo, IDependentTreeNode__no_children):
    __slots__ = ()
class IRecognizerLLoo__leaf(IRecognizerLLoo__no_children, IRecognizerLLoo__no_ref, IDependentTreeNode__leaf):
    __slots__ = ()

class BaseHandler4gi4two_phases_recognize:
    def __init__(sf, gi4two_phases_recognize, /):
        #check_type_le(IGeneratorIterator, gi4two_phases_recognize)
        sf._gi = mk_gi4either8xresult(gi4two_phases_recognize, ___666_close_wrapped_gi_999___=False)
            #bug:[see:detach_asif_new_gi_wrapper]
        sf._gi0 = gi4two_phases_recognize

    def __del__(sf, /):
        if sf._gi is None:
            return
        detach_asif_new_gi_wrapper(sf._gi0, sf._gi)
        sf._gi0 = null_iter
        sf._gi = None
    def __iter__(sf, /):
        if sf._gi is None: raise 000#__del__
        gi = sf._gi
        hdr_sgnl_occured = False
        x = yield gi
        if x.is_left:
            hdr_sgnl, gi = x.left
            del x
            check_type_is(Signal__HeaderCompleted, hdr_sgnl)
            may_hdr_sgnl = sf._mk_may_hdr_sgnl_(hdr_sgnl)
            del hdr_sgnl
            if not None is may_hdr_sgnl:
                hdr_sgnl = may_hdr_sgnl
                check_type_is(Signal__HeaderCompleted, hdr_sgnl)
                yield BoxedHalfwayResult(hdr_sgnl)
                del hdr_sgnl
                hdr_sgnl_occured = True
            ######################
            y = yield gi
            if not y.is_right:
                raise Error__not_Reply4IRecognizerLLoo_after_Signal__HeaderCompleted
            x = y
            del y
        assert x.is_right
        reply4LLoo = x.right
        check_type_is(Reply4IRecognizerLLoo, reply4LLoo)
        (may_hdr_sgnl, reply4LLoo) = sf._mk_reply4LLoo_ex_(hdr_sgnl_occured, reply4LLoo)
        check_type_is(Reply4IRecognizerLLoo, reply4LLoo)
        if not None is may_hdr_sgnl:
            if hdr_sgnl_occured:raise LogicError4IRecognizerLLoo
            hdr_sgnl = may_hdr_sgnl
            check_type_is(Signal__HeaderCompleted, hdr_sgnl)
            yield BoxedHalfwayResult(hdr_sgnl)
            del hdr_sgnl
            hdr_sgnl_occured = True
            ######################
        return BoxedFinalResult(reply4LLoo)


    def _mk_may_hdr_sgnl_(sf, hdr_sgnl, /):
        'Signal__HeaderCompleted -> may Signal__HeaderCompleted'
        return hdr_sgnl
    def _mk_reply4LLoo_ex_(sf, hdr_sgnl_occured, reply4LLoo, /):
        'bool -> Reply4IRecognizerLLoo -> (may Signal__HeaderCompleted, Reply4IRecognizerLLoo)'
        return (may_hdr_sgnl:=None, reply4LLoo)
class _Handler4mk_gi4skip_header_signal(BaseHandler4gi4two_phases_recognize):
    'see:mk_gi4skip_header_signal()'
    def _mk_may_hdr_sgnl_(sf, hdr_sgnl, /):
        'Signal__HeaderCompleted -> may Signal__HeaderCompleted'
        return None
class _Handler4mk_gi4patch_header_signal_if_ok(BaseHandler4gi4two_phases_recognize):
    'see:mk_gi4patch_header_signal_if_ok()'
    def _mk_reply4LLoo_ex_(sf, hdr_sgnl_occured, reply4LLoo, /):
        'bool -> Reply4IRecognizerLLoo -> (may Signal__HeaderCompleted, Reply4IRecognizerLLoo)'
        if not hdr_sgnl_occured and reply4LLoo.ok:
            hdr_sgnl = Signal__HeaderCompleted(reply4LLoo._tmp_snapshot4inputter_, reply4LLoo.oresult)
            may_hdr_sgnl = hdr_sgnl
        else:
            may_hdr_sgnl = None
        may_hdr_sgnl
        return (may_hdr_sgnl, reply4LLoo)



@recur5yield__list__echo__echo
def parse__via_IRecognizerLLoo(recognizer_LLoo, inputter4whole, /):
    'YS_GI(IRecognizerLLoo -> IForkable__stamp -> Reply4IRecognizerLLoo)'
    'IRecognizerLLoo -> IForkable__stamp -> Reply4IRecognizerLLoo'
    check_type_le(IRecognizerLLoo, recognizer_LLoo)
    check_type_le(IForkable__stamp, inputter4whole)
    gi = recognizer_LLoo.iter4two_phases_recognize(inputter4whole)
    gi = mk_gi4skip_header_signal(gi)
    return gi
    #return BoxedTailRecur(gi);yield
def mk_gi4skip_header_signal(gi4two_phases_recognize, /):
    'gi4two_phases_recognize -> gi4one_phase_recognize #[mk_gi4header_signal_at_end<==>mk_gi4skip_header_signal] #see:mk_gi4header_signal_at_beginning'
    'YS_GI(gi4two_phases_recognize -> Reply4IRecognizerLLoo)'
    #xxx:'YS_GI(IRecognizerLLoo -> IForkable__stamp -> Reply4IRecognizerLLoo)'
    return iter(_Handler4mk_gi4skip_header_signal(gi4two_phases_recognize))
def mk_gi4header_signal_at_beginning(xinputter4begin, gi4two_phases_recognize, /):
    'xinputter4begin -> gi4two_phases_recognize -> gi4two_phases_recognize{hdr_sgnl at beginning} #[mk_gi4header_signal_at_end<==>mk_gi4skip_header_signal]'
    yield BoxedHalfwayResult(Signal__HeaderCompleted(xinputter4begin, None))
    return BoxedTailRecur(mk_gi4skip_header_signal(gi4two_phases_recognize))

def mk_gi4patch_header_signal_if_ok(gi4two_phases_recognize, /):
    #def mk_gi4patch_header_signal_ unless_fail(gi4two_phases_recognize, /):
    'gi4two_phases_recognize -> gi4two_phases_recognize{yield hdr_sgnl or fail}'
    return iter(_Handler4mk_gi4patch_header_signal_if_ok(gi4two_phases_recognize))
def mk_gi4validate_two_phases(gi4two_phases_recognize, /):
    'gi4two_phases_recognize -> gi4two_phases_recognize{validate two phases:(fail|hdr_sgnl-fail|hdr_sgnl-succ)}'
    return iter(BaseHandler4gi4two_phases_recognize(gi4two_phases_recognize))










__all__
from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import parse__via_IRecognizerLLoo, mk_gi4skip_header_signal, mk_gi4header_signal_at_beginning, mk_gi4patch_header_signal_if_ok, mk_gi4validate_two_phases

from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import IRecognizerLLoo, Signal__HeaderCompleted, Reply4IRecognizerLLoo


from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import IRecognizerLLoo, IRecognizerLLoo__no_ref, IRecognizerLLoo__no_children, IRecognizerLLoo__leaf

from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import IDependentTreeNode, IDependentTreeNode__no_ref, IDependentTreeNode__no_children, IDependentTreeNode__leaf, IDependentTreeNode__ref

from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import IScene, IScene__register, IWithScene, INamed, IWrapper, ILazyWrapper, IDependentTreeNode__ref

from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import TmpSnapshot4Inputter, BaseReply, BaseHandler4gi4two_phases_recognize


from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import *
