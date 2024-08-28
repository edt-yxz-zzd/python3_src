#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/recognizer_LLoo_/combinator_LLoo__gi8flow.py

seed.recognize.recognizer_LLoo_.combinator_LLoo__gi8flow
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_LLoo_.combinator_LLoo__gi8flow -x
py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LLoo_.combinator_LLoo__gi8flow:__doc__ -ht
#]]]'''
__all__ = r'''
mk_LLoo__gi8flow__all_in_one

IRecognizerLLoo__gi8flow
    IRecognizerLLoo__gi8flow__all_in_one
        RecognizerLLoo__gi8flow__all_in_one

WhetherForwardHeaderSignal
    HForwardHeaderSignal
    HNoHeaderSignal
EitherTailWForwardOrEResult
    TailForwardHeaderSignal
    TailNoHeaderSignal
    FinalEResult
        FinalOResult
        FinalErrmsg
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.recognize.recognizer_LLoo_._common import (check_non_ABC
,BoxedFinalResult, BoxedHalfwayResult, BoxedTailRecur
,Cased, Either, mk_Left, mk_Right
,IGeneratorIterator
,mk_tuple
#,check_non_ABC
,check_type_is, check_type_le
,abstractmethod, override, ABC
,repr_helper, _Base4repr #sf._args4repr = (...)
)
from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import IRecognizerLLoo, Signal__HeaderCompleted, Reply4IRecognizerLLoo
from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import mk_gi4patch_header_signal_if_ok


from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import mk_gi4skip_header_signal, mk_gi4patch_header_signal_if_ok# mk_gi4validate_two_phases

from seed.tiny import check_callable

___end_mark_of_excluded_global_names__0___ = ...


class WhetherForwardHeaderSignal(Cased):
    def __new__(cls, fwd_hdr_sgnl, rgnr, /):
        check_type_is(bool, fwd_hdr_sgnl)
        check_type_le(IRecognizerLLoo, rgnr)
        return super(__class__, cls).__new__(cls, fwd_hdr_sgnl, rgnr)
    @property
    def fwd_hdr_sgnl(sf, /):
        '-> bool'
        return sf.case
    @property
    def rgnr(sf, /):
        '-> IRecognizerLLoo'
        return sf.payload

def HForwardHeaderSignal(rgnr, /):
    return WhetherForwardHeaderSignal(True, rgnr)
def HNoHeaderSignal(rgnr, /):
    return WhetherForwardHeaderSignal(False, rgnr)

class EitherTailWForwardOrEResult(Cased):
    def __new__(cls, is_eresult, whether_fwd_or_eresult, /):
        check_type_is(bool, is_eresult)
        if not is_eresult:
            whether_fwd = whether_fwd_or_eresult
            check_type_is(WhetherForwardHeaderSignal, whether_fwd)
        else:
            eresult = whether_fwd_or_eresult
            check_type_is(Either, eresult)
        return super(__class__, cls).__new__(cls, is_eresult, whether_fwd_or_eresult)
    @property
    def is_eresult(sf, /):
        '-> bool'
        return sf.case
    @property
    def whether_fwd(sf, /):
        '-> WhetherForwardHeaderSignal'
        if sf.is_eresult: raise AttributeError('whether_fwd')
        return sf.payload
    @property
    def eresult(sf, /):
        '-> Either'
        if not sf.is_eresult: raise AttributeError('eresult')
        return sf.payload

def TailForwardHeaderSignal(rgnr, /):
    return EitherTailWForwardOrEResult(False, HForwardHeaderSignal(rgnr))
def TailNoHeaderSignal(rgnr, /):
    return EitherTailWForwardOrEResult(False, HNoHeaderSignal(rgnr))
def FinalEResult(eresult, /):
    return EitherTailWForwardOrEResult(True, eresult)
def FinalOResult(oresult, /):
    return FinalEResult(mk_Right(oresult))
def FinalErrmsg(errmsg, /):
    return FinalEResult(mk_Left(errmsg))

class IRecognizerLLoo__gi8flow(IRecognizerLLoo):
    __slots__ = ()
    #@property
    #@override
    #___666_tribool_skip4serial4LLoo_999___ = False # False-append;True-skip;...-extend


    @abstractmethod
    def _mk_gi8flow4LLoo_(sf, /):
        r'''[[[
        -> gi8flow4LLoo/IGeneratorIterator(
            ;yield-WhetherForwardHeaderSignal
            ;send-Reply4IRecognizerLLoo.oresult
            ;return-EitherTailWForwardOrEResult#Either<tail/WhetherForwardHeaderSignal,Reply4IRecognizerLLoo.the_eresult>
            )
        #]]]'''#'''
        ######################
        #example:
        ######################
        rgnr = IRecognizerLLoo()
        oresult = yield HNoHeaderSignal(rgnr)
        oresult = yield HForwardHeaderSignal(rgnr)
        eresult = mk_Left('err')
        return FinalOResult(oresult)
        return FinalEResult(eresult)
        return FinalErrmsg('err')
        return TailForwardHeaderSignal(rgnr)
        return TailNoHeaderSignal(rgnr)
        ######################


    @override
    def _iter4two_phases_recognize_(sf, inputter4whole, /):
        gi8flow4LLoo = sf._mk_gi8flow4LLoo_()
        check_type_le(IGeneratorIterator, gi8flow4LLoo)
        inputter = inputter4whole
        777;    del inputter4whole
        hdr_sgnl_occured = False
        oresult = None#init
        try:
            while 1:
                #########
                oresult, inputter, hdr_sgnl_occured
                #########
                whether_fwd = gi8flow4LLoo.send(oresult)
                    # ^StopIteration
                777;    del oresult
                check_type_is(WhetherForwardHeaderSignal, whether_fwd)
                (fwd_hdr_sgnl, rgnr) = whether_fwd
                    #check_type_le(IRecognizerLLoo, rgnr)
                gi = rgnr.iter4two_phases_recognize(inputter)
                777;    del inputter, rgnr
                (fwd_hdr_sgnl, gi) = _fff(hdr_sgnl_occured, fwd_hdr_sgnl, gi)
                gi#validated
                x = yield gi
                if type(x) is Signal__HeaderCompleted:
                    assert fwd_hdr_sgnl
                    hdr_sgnl = x; del x
                    yield BoxedHalfwayResult(hdr_sgnl)
                    del hdr_sgnl
                    hdr_sgnl_occured = True
                    x = yield gi
                else:
                    assert not fwd_hdr_sgnl or not x.ok
                    x
                777;    gi.close(); del gi
                x
                check_type_is(Reply4IRecognizerLLoo, x)
                reply4LLoo = x; del x
                if not reply4LLoo.ok:
                    return BoxedFinalResult(reply4LLoo)
                #########
                #next round:
                oresult = reply4LLoo.oresult
                inputter = reply4LLoo.the_inputter4end
                777;    del reply4LLoo
                #########
                oresult, inputter, hdr_sgnl_occured
                #########
            #end-while
            raise 000
        except StopIteration as e:
            oresult, inputter, hdr_sgnl_occured
            777;    del oresult
            inputter, hdr_sgnl_occured
            #########
            ee = e.value
            check_type_is(EitherTailWForwardOrEResult, ee)
            #########
            ee, inputter, hdr_sgnl_occured
            #########
        else:
            raise 000
        #########
        ee, inputter, hdr_sgnl_occured
        #########
        if not ee.is_eresult:
            whether_fwd = ee.whether_fwd
            (fwd_hdr_sgnl, rgnr) = whether_fwd
                #check_type_le(IRecognizerLLoo, rgnr)
            gi = rgnr.iter4two_phases_recognize(inputter)
            777;    del inputter, rgnr
            (fwd_hdr_sgnl, gi) = _fff(hdr_sgnl_occured, fwd_hdr_sgnl, gi)
            gi#validated
            return BoxedTailRecur(gi)
        else:
            eresult = ee.eresult
        #########
        eresult, inputter
        #########
        reply4LLoo = Reply4IRecognizerLLoo(inputter, eresult)
        return BoxedFinalResult(reply4LLoo)
def _fff(hdr_sgnl_occured, fwd_hdr_sgnl, gi, /):
    fwd_hdr_sgnl = not hdr_sgnl_occured and fwd_hdr_sgnl
    if fwd_hdr_sgnl:
        gi = mk_gi4patch_header_signal_if_ok(gi)
    else:
        gi = mk_gi4skip_header_signal(gi)
            #mk_gi4validate_two_phases
    gi#validated
    return (fwd_hdr_sgnl, gi)
#end-class IRecognizerLLoo__gi8flow(IRecognizerLLoo):

class IRecognizerLLoo__gi8flow__all_in_one(IRecognizerLLoo__gi8flow):
    __slots__ = ()
    @abstractmethod
    def _all_in_one4gi8flow4LLoo_(sf, case, /):
        'case/uint%5 -> result4all_in_one4gi8flow4LLoo(([case==0]gi8flow4LLoo)|([case==1](Iter tribool_skip){len==1})|([case==2](Iter kinded_name))|([case==3](Iter IDependentTreeNode)))'
    @override
    def _mk_gi8flow4LLoo_(sf, /):
        '-> gi8flow4LLoo'
        return sf._all_in_one4gi8flow4LLoo_(0)

    @property
    @override
    def ___666_tribool_skip4serial4LLoo_999___(sf, /):
        '-> tribool # False-append;True-skip;...-extend'
        [tribool_skip] = sf._all_in_one4gi8flow4LLoo_(1)
        return tribool_skip

    @override
    def _iter_directly_used_kinded_names_(sf, /):
        '-> Iter (kinded_name)'
        return sf._all_in_one4gi8flow4LLoo_(2)
    @override
    def _iter_direct_child_dependent_tree_nodes_(sf, /):
        '-> Iter IDependentTreeNode'
        return sf._all_in_one4gi8flow4LLoo_(3)

class RecognizerLLoo__gi8flow__all_in_one(IRecognizerLLoo__gi8flow__all_in_one):
    'all_in_one_ex :: case/uint%5 -> (*args4all_in_one_ex) -> result4all_in_one4gi8flow4LLoo(([case==0]gi8flow4LLoo)|([case==1](Iter tribool_skip){len==1})|([case==2](Iter kinded_name))|([case==3](Iter IDependentTreeNode)))'
    ___no_slots_ok___ = True
    def __init__(sf, all_in_one_ex, args4all_in_one_ex, /):
        check_callable(all_in_one_ex)
        args4all_in_one_ex = mk_tuple(args4all_in_one_ex)
        sf._f_args = (all_in_one_ex, args4all_in_one_ex)
        sf._args4repr = (all_in_one_ex, *args4all_in_one_ex)

    @override
    def _all_in_one4gi8flow4LLoo_(sf, case, /):
        'case/uint%5 -> result4all_in_one4gi8flow4LLoo(([case==0]gi8flow4LLoo)|([case==1](Iter tribool_skip){len==1})|([case==2](Iter kinded_name))|([case==3](Iter IDependentTreeNode)))'
        (all_in_one_ex, args4all_in_one_ex) = sf._f_args
        return all_in_one_ex(case, *args4all_in_one_ex)

check_non_ABC(RecognizerLLoo__gi8flow__all_in_one)

def mk_LLoo__gi8flow__all_in_one(all_in_one_ex, args4all_in_one_ex, /):
    '(all_in_one_ex/(case/uint%5 -> (*args4all_in_one_ex) -> result4all_in_one4gi8flow4LLoo(([case==0]gi8flow4LLoo)|([case==1](Iter tribool_skip){len==1})|([case==2](Iter kinded_name))|([case==3](Iter IDependentTreeNode)))) -> args4all_in_one_ex/[arg] -> IRecognizerLLoo'
    return RecognizerLLoo__gi8flow__all_in_one(all_in_one_ex, *args4all_in_one_ex)

__all__
from seed.recognize.recognizer_LLoo_.combinator_LLoo__gi8flow import mk_LLoo__gi8flow__all_in_one
from seed.recognize.recognizer_LLoo_.combinator_LLoo__gi8flow import IRecognizerLLoo__gi8flow
from seed.recognize.recognizer_LLoo_.combinator_LLoo__gi8flow import \
(IRecognizerLLoo__gi8flow
,   IRecognizerLLoo__gi8flow__all_in_one
,       RecognizerLLoo__gi8flow__all_in_one
,mk_LLoo__gi8flow__all_in_one
#
,WhetherForwardHeaderSignal
,   HForwardHeaderSignal
,   HNoHeaderSignal
,EitherTailWForwardOrEResult
,   TailForwardHeaderSignal
,   TailNoHeaderSignal
,   FinalEResult
,       FinalOResult
,       FinalErrmsg
)
from seed.recognize.recognizer_LLoo_.combinator_LLoo__gi8flow import *
