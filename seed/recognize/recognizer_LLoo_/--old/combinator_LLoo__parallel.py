#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/recognizer_LLoo_/combinator_LLoo__parallel.py

seed.recognize.recognizer_LLoo_.combinator_LLoo__parallel
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_LLoo_.combinator_LLoo__parallel -x
py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LLoo_.combinator_LLoo__parallel:__doc__ -ht
py_adhoc_call   seed.recognize.recognizer_LLoo_.combinator_LLoo__parallel   @f
from seed.recognize.recognizer_LLoo_.combinator_LLoo__parallel import *
#]]]'''
__all__ = r'''
RecognizerLLoo__the_first_one
RecognizerLLoo__the_only_one
RecognizerLLoo__the_first_one__tagged
RecognizerLLoo__the_only_one__tagged
'''.split()#'''
__all__

from seed.recognize.recognizer_LLoo_.combinator_LLoo__wrapper import RecognizerLLoo__try, RecognizerLLoo__tag

from seed.recognize.recognizer_LLoo_.interface_LLoo import mk_gi4skip_header_signal, mk_gi4patch_header_signal_unless_fail
from seed.recognize.recognizer_LLoo_.interface_LLoo import IPseudoMaker4RecognizerLLoo, IRecognizerLLoo, IScene4LLoo
from seed.recognize.recognizer_LLoo_.interface_LLoo import Error__not_only_one_match
from seed.recognize.recognizer_LLoo_.interface_LLoo import Signal__HeaderCompleted, Reply4IRecognizerLLoo







from seed.func_tools.recur5yield import bind_gi_with_the_following_first_value4send, mk_gi4either8xresult, mk_gi4xresult_xexception
from seed.func_tools.recur5yield import BoxedHalfwayResult, BoxedException__halfway, BoxedException__final, BoxedException__through, Escaped, BoxedTailRecur, BoxedFinalResult
from seed.func_tools.recur5yield import EFlowControl, EFinal, EHalfway, mk_boxed_EFinal, mk_boxed_EHalfway
from seed.func_tools.recur5yield import recur5yield__list__echo__echo
from seed.types.Either import Either

from seed.types.StackStyleSet import StackStyleSet# MultiSetStyleStack
from seed.tiny_.check import check_type_is, check_type_le, check_int_ge, check_pseudo_qual_name, check_callable, check_pair, check_non_ABC
from seed.tiny import chains, snd, null_iter, null_tuple, mk_tuple
from seed.tiny_.dict_op__add import dict_add# set_add, dict_update, set_update

from seed.types.ForkableForwardInputStream import IForkable, IForkableForwardInputStream# ForkableForwardInputStream__using_LazyListIter
from collections.abc import Generator as IGeneratorIterator

from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.helper.repr_input import repr_helper

def _check_psmkr_(m, M, psmkr, /):
    check_type_le(IPseudoMaker4RecognizerLLoo, psmkr)
    if not m <= psmkr.imay_num_params_required < M:raise TypeError
def _check_psmkrs_(m, M, psmkrs, /):
    for psmkr in psmkrs:
        _check_psmkr_(m, M, psmkr)

#class _RecognizerLLoo__tag_branch_idx(RecognizerLLoo__tag):
#    'see:_IRecognizerLLoo__parallel.to_tag_branch_idx'
#    def __init__(sf, branch_idx, rgnr, /):
#        check_int_ge(0, branch_idx)
#        #check_type_le(IRecognizerLLoo, rgnr)
#        super().__init__(branch_idx, rgnr)

class _IRecognizerLLoo__parallel(IRecognizerLLoo):
    'parallel/choice:the_only_one/the_first_one'
    ___no_slots_ok___ = True
    #@property
    #@abstractmethod
    #def first_one__vs__only_one(sf, /):
    #    '-> bool'
    @property
    @abstractmethod
    def to_tag_branch_idx(sf, /):
        '-> bool'
    def __repr__(sf, /):
        return repr_helper(sf, sf._scn, sf._psmkrs)
    def __init__(sf, scene, psmkrs, /):
        check_type_le(IScene4LLoo, scene)
        psmkrs = mk_tuple(psmkrs)
        _check_psmkrs_(-1, 1, psmkrs)
        sf._scn = scene
        sf._psmkrs = psmkrs
    @override
    def _iter_directly_used_kinded_names_(sf, /):
        '-> Iter (kind, name)'
        return null_iter
    @override
    def _iter_directly_used_IRequiredSceneAsClosure_(sf, /):
        '-> Iter IRequiredSceneAsClosure'
        return iter(sf._psmkrs)
    @property
    def num_branches(sf, /):
        '-> uint'
        return len(sf._psmkrs)
    @property
    @override
    def scene(sf, /):
        '-> IScene4LLoo'
        return sf._scn
    def iter_recognizers4LLoo(sf, /):
        '-> Iter IRecognizerLLoo'
        for branch_idx, psmkr in enumerate(sf._psmkrs):
            im = psmkr.imay_num_params_required
            if im == -1:
                rgnr = psmkr
            elif im == 0:
                rgnr = psmkr.mk_pseudo_mkr4recognizer_LLoo(sf.scene)
            else:
                raise TypeError(psmkr)
            check_type_le(IRecognizerLLoo, rgnr)
            if to_tag_branch_idx:
                rgnr = RecognizerLLoo__tag(branch_idx, rgnr)
            yield rgnr



class _IRecognizerLLoo__the_first_one(_IRecognizerLLoo__parallel):
    'the_first_one'
    @override
    def _iter4two_phases_recognize_(sf, inputter4whole, /):
        L = sf.num_branches
        rgnrs = sf.iter_recognizers4LLoo()
        for sz, rgnr in enumerate(rgnrs, 1):
            if sz == L:
                #last_branch
                rgnr
                gi = rgnr.iter4two_phases_recognize(inputter4whole)
                return BoxedTailRecur(gi)
            #nonlast_branch
            rgnr = RecognizerLLoo__try(rgnr)
            gi = rgnr.iter4two_phases_recognize(inputter4whole)
            reply4LLoo = yield mk_gi4skip_header_signal(gi)
            if not reply4LLoo.ok:
                inputter4whole = reply4LLoo.the_inputter4end
                continue
            reply4LLoo = reply4LLoo.result
            check_type_is(Reply4IRecognizerLLoo, reply4LLoo)
            return BoxedFinalResult(reply4LLoo)
        assert L == 0
        reply4LLoo = Reply4IRecognizerLLoo(num_consumed:=0, inputter4end:=inputter4whole, Either.from_left('no branches'))
        return BoxedFinalResult(reply4LLoo)
class _IRecognizerLLoo__the_only_one(_IRecognizerLLoo__parallel):
    'the_only_one'
    @override
    def _iter4two_phases_recognize_(sf, inputter4whole, /):
        L = sf.num_branches
        rgnrs = sf.iter_recognizers4LLoo()
        imay_sz = -1
        may_gi = None
        for sz, rgnr in enumerate(rgnrs, 1):
            if sz == L:
                #last_branch
                inputter4branch = inputter4whole
                if may_gi is None:
                    gi = rgnr.iter4two_phases_recognize(inputter4branch)
                    return BoxedTailRecur(gi)
            else:
                #nonlast_branch
                inputter4branch = inputter4whole.fork()
            gi = rgnr.iter4two_phases_recognize(inputter4branch)
            gi = mk_gi4patch_header_signal_unless_fail(gi)
            gi = mk_gi4either8xresult(gi)
            x = yield gi
            if x.is_right:
                #curr-branch-fail
                reply4LLoo = x.right
                check_type_is(Reply4IRecognizerLLoo, reply4LLoo)
                if not reply4LLoo.ok:raise 000
                #not match
                continue
            #match
            hdr_sgnl = x.left
            check_type_is(Signal__HeaderCompleted, hdr_sgnl)
            if may_gi is None:
                may_gi = gi
                imay_sz = sz
                continue
            prev_sz = imay_sz
            sz
            js = [prev_sz-1,sz-1]
            psmkrs = sf._psmkrs
            ms = [psmkrs[j] for j in js]
            raise Error__not_only_one_match((js, ms, sf))
        if may_gi is None:
            assert L == 0
            reply4LLoo = Reply4IRecognizerLLoo(num_consumed:=0, inputter4end:=inputter4whole, Either.from_left('no branches'))
        else:
            gi = may_gi
            x = yield gi
            assert x.is_right
            reply4LLoo = x.right
        check_type_is(Reply4IRecognizerLLoo, reply4LLoo)
        return BoxedFinalResult(reply4LLoo)
class RecognizerLLoo__the_first_one(_IRecognizerLLoo__the_first_one):
    #@override
    to_tag_branch_idx = False
class RecognizerLLoo__the_only_one(_IRecognizerLLoo__the_only_one):
    #@override
    to_tag_branch_idx = False
class RecognizerLLoo__the_first_one__tagged(_IRecognizerLLoo__the_first_one):
    #@override
    to_tag_branch_idx = True
class RecognizerLLoo__the_only_one__tagged(_IRecognizerLLoo__the_only_one):
    #@override
    to_tag_branch_idx = True
check_non_ABC(RecognizerLLoo__the_first_one)
check_non_ABC(RecognizerLLoo__the_only_one)
check_non_ABC(RecognizerLLoo__the_first_one__tagged)
check_non_ABC(RecognizerLLoo__the_only_one__tagged)

__all__
from seed.recognize.recognizer_LLoo_.combinator_LLoo__parallel import *
