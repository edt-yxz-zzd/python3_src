#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/recognizer_LLoo_/combinator_LLoo__parallel.py

seed.recognize.recognizer_LLoo_.combinator_LLoo__parallel
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_LLoo_.combinator_LLoo__parallel -x
py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LLoo_.combinator_LLoo__parallel:__doc__ -ht
py_adhoc_call   seed.recognize.recognizer_LLoo_.combinator_LLoo__parallel   @f
#]]]'''
__all__ = r'''
RecognizerLLoo__the_first_one
RecognizerLLoo__the_only_one

RecognizerLLoo__the_first_one__tagged
RecognizerLLoo__the_only_one__tagged

RecognizerLLoo__the_first_one__cased
RecognizerLLoo__the_only_one__cased

mk_LLoo__the_first_one
    mk_LLoo__choice
mk_LLoo__the_only_one
    mk_LLoo__parallel
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...

#from seed.recognize.recognizer_LLoo_.combinator_LLoo__wrapper import RecognizerLLoo__try__rollback_if_fail_before_hdr_sgnl_else_lift, RecognizerLLoo__tag
from seed.recognize.recognizer_LLoo_.combinator_LLoo__wrapper import RecognizerLLoo__tag, RecognizerLLoo__Cased
from seed.recognize.recognizer_LLoo_._common import (IForkable__stamp
,mk_gi4either8xresult, detach_asif_new_gi_wrapper
,mk_gi4xresult_xexception__as_
,BoxedFinalResult, BoxedHalfwayResult, BoxedTailRecur
,Cased, Either, mk_Left, mk_Right
,check_non_ABC
,check_type_is, check_type_le
,mk_tuple, null_iter
,abstractmethod, override, ABC
,repr_helper
)
from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import IRecognizerLLoo, Signal__HeaderCompleted, Reply4IRecognizerLLoo, Error__not_only_one_match



from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import IRecognizerLLoo, mk_gi4patch_header_signal_if_ok
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots


___end_mark_of_excluded_global_names__0___ = ...

def _check_rgnrs(rgnrs, /):
    for rgnr in rgnrs:
        check_type_le(IRecognizerLLoo, rgnr)


class _IRecognizerLLoo__parallel(IRecognizerLLoo):
    'parallel/choice:the_only_one/the_first_one'
    ___no_slots_ok___ = True
    #@property
    #@override
    ___666_tribool_skip4serial4LLoo_999___ = False # False-append;True-skip;...-extend
    #@property
    #@abstractmethod
    #def first_one__vs__only_one(sf, /):
    #    '-> bool'
    #@property
    #@abstractmethod
    #def to_tag_branch_idx(sf, /):
    #    '-> bool'
    @property
    @abstractmethod
    def _6oresult_only_(sf, /):
        '-> bool # [eresult = Either<(errmsg if _6oresult_only_ else tagged errmsg), (tagged oresult)>]'
    @property
    @abstractmethod
    def _bare_vs_cased_vs_tagged_(sf, /):
        '-> tribool/(False-bare|...-cased|True-tagged)'
    def __repr__(sf, /):
        return repr_helper(sf, sf._rgnrs)
    def __init__(sf, rgnrs, /):
        rgnrs = mk_tuple(rgnrs)
        _check_rgnrs(rgnrs)
        sf._rgnrs = rgnrs
    @override
    def _iter_directly_used_kinded_names_(sf, /):
        '-> Iter knm/kinded_name'
        return null_iter
    @override
    def _iter_direct_child_dependent_tree_nodes_(sf, /):
        '-> Iter IDependentTreeNode'
        return iter(sf._rgnrs)
    @property
    def num_branches(sf, /):
        '-> uint'
        return len(sf._rgnrs)
    def iter_child_recognizers4LLoo(sf, /):
        '-> Iter IRecognizerLLoo'
        it = iter(sf._rgnrs)
        case = sf._bare_vs_cased_vs_tagged_
        if case is False:
            #bare
            return it
        elif case is True:
            T = RecognizerLLoo__tag
        elif case is ...:
            T = RecognizerLLoo__Cased
        else:
            raise TypeError(type(case))
        _6oresult_only_ = sf._6oresult_only_
        return (T(_6oresult_only_, branch_idx, rgnr) for branch_idx, rgnr in enumerate(it))


def _show_gi(gi, /):
    #print(dir(gi))
    for nm in dir(gi):
        if nm.startswith('gi_'):
            print(nm, getattr(gi, nm))
class _IRecognizerLLoo__the_first_one(_IRecognizerLLoo__parallel):
    'the_first_one'
    @override
    def _iter4two_phases_recognize_(sf, inputter4whole, /):
        L = sf.num_branches
        rgnrs = sf.iter_child_recognizers4LLoo()
        for sz, rgnr in enumerate(rgnrs, 1):
            if sz == L:
                #last_branch
                rgnr
                gi = rgnr.iter4two_phases_recognize(inputter4whole)
                    # no:.fork()
                if 0b0000:
                    print(_IRecognizerLLoo__parallel)
                    _show_gi(gi)
                    raise 000
                return BoxedTailRecur(gi)
            #nonlast_branch
            #xxx:rgnr = RecognizerLLoo__try__rollback_if_fail_before_hdr_sgnl_else_lift(rgnr)
            #   #<<==skip hdr_sgnl is incorrect
            rgnr
            gi = rgnr.iter4two_phases_recognize(inputter4whole.fork())
                # has:.fork()
            _gi = mk_gi4either8xresult(gi, ___666_close_wrapped_gi_999___=False)
            x = yield _gi
            if x.is_left:
                hdr_sgnl, _2_gi = x.left
                check_type_is(Signal__HeaderCompleted, hdr_sgnl)
                #now:[default:___666_close_wrapped_gi_999___=False]:detach_asif_new_gi_wrapper(gi, _gi)
                    ##bug:_gi.close() => gi.close()!!!!==>>StopIteration(None)
                #bug:_gi.close();del _gi
                if not _2_gi is _gi:
                    gi = mk_gi4xresult_xexception__as_(gi, _2_gi)
                del _2_gi
                del _gi
                del inputter4whole
                if 0b0000:
                    print(_IRecognizerLLoo__parallel)
                    _show_gi(gi)
                    raise 000
                yield BoxedHalfwayResult(hdr_sgnl)
                return BoxedTailRecur(gi)
            reply4LLoo = x.right
            check_type_is(Reply4IRecognizerLLoo, reply4LLoo)
            _gi.close();del _gi
            gi.close();del gi
            if not reply4LLoo.ok:
                # !! fail_before_hdr_sgnl
                del reply4LLoo
                inputter4whole
                continue
            del inputter4whole
            return BoxedFinalResult(reply4LLoo)
        assert L == 0
        reply4LLoo = Reply4IRecognizerLLoo(inputter4end:=inputter4whole, _no_branches)
        return BoxedFinalResult(reply4LLoo)
_no_branches = mk_Left('no_branches')
class _IRecognizerLLoo__the_only_one(_IRecognizerLLoo__parallel):
    'the_only_one'
    @override
    def _iter4two_phases_recognize_(sf, inputter4whole, /):
        L = sf.num_branches
        rgnrs = sf.iter_child_recognizers4LLoo()
        imay_sz = -1
        may_hdr_sgnl_gi0 = None
        for sz, rgnr in enumerate(rgnrs, 1):
            if sz == L:
                #last_branch
                inputter4branch = inputter4whole#xxx:.fork()
                del inputter4whole
                if may_hdr_sgnl_gi0 is None:
                    gi = rgnr.iter4two_phases_recognize(inputter4branch)
                    return BoxedTailRecur(gi)
            else:
                #nonlast_branch
                inputter4branch = inputter4whole.fork()
            gs = []
            gi0 = rgnr.iter4two_phases_recognize(inputter4branch)
            gs.append(gi0)
            gi1 = mk_gi4patch_header_signal_if_ok(gi0)
            gs.append(gi1)
            gi2 = mk_gi4either8xresult(gi1, ___666_close_wrapped_gi_999___=False)
            gs.append(gi2)
            x = yield gi2
            if x.is_right:
                #=>not hdr_sgnl
                #=>reply4LLoo
                #=>not reply4LLoo.ok
                #=>curr-branch-fail
                reply4LLoo = x.right
                check_type_is(Reply4IRecognizerLLoo, reply4LLoo)
                if not reply4LLoo.ok:raise 000
                #not match
                for gi in gs:
                    gi.close()
                del gi, gs
                continue
            #match
            hdr_sgnl, _2_gi = x.left
            check_type_is(Signal__HeaderCompleted, hdr_sgnl)
            if may_hdr_sgnl_gi0 is None:
                if not _2_gi is gi2:
                    gi0 = mk_gi4xresult_xexception__as_(gi0, _2_gi)
                may_hdr_sgnl_gi0 = hdr_sgnl, gi0
                del _2_gi, gi0, gi1, gi2
                imay_sz = sz
                continue
            prev_sz = imay_sz
            sz
            js = [prev_sz-1,sz-1]
            rgnrs = sf._rgnrs
            ms = [rgnrs[j] for j in js]
            raise Error__not_only_one_match((js, ms, sf))
        if not may_hdr_sgnl_gi0 is None:
            hdr_sgnl, gi0 = may_hdr_sgnl_gi0
            yield BoxedHalfwayResult(hdr_sgnl)
            #xxx:detach_asif_new_gi_wrapper(gi, g1)
            return BoxedTailRecur(gi0)
        if not L == 0:raise 000
        reply4LLoo = Reply4IRecognizerLLoo(inputter4end:=inputter4whole, _no_branches)
        return BoxedFinalResult(reply4LLoo)
######################
class RecognizerLLoo__the_first_one(_IRecognizerLLoo__the_first_one):
    #@override
    _bare_vs_cased_vs_tagged_ = False
    #@override
    _6oresult_only_ = False
class RecognizerLLoo__the_only_one(_IRecognizerLLoo__the_only_one):
    #@override
    _bare_vs_cased_vs_tagged_ = False
    #@override
    _6oresult_only_ = False
######################
class RecognizerLLoo__the_first_one__tagged(_IRecognizerLLoo__the_first_one):
    #@override
    _bare_vs_cased_vs_tagged_ = True
    #@override
    _6oresult_only_ = False
class RecognizerLLoo__the_only_one__tagged(_IRecognizerLLoo__the_only_one):
    #@override
    _bare_vs_cased_vs_tagged_ = True
    #@override
    _6oresult_only_ = False
######################
class RecognizerLLoo__the_first_one__cased(_IRecognizerLLoo__the_first_one):
    #@override
    _bare_vs_cased_vs_tagged_ = ...
    #@override
    _6oresult_only_ = False
class RecognizerLLoo__the_only_one__cased(_IRecognizerLLoo__the_only_one):
    #@override
    _bare_vs_cased_vs_tagged_ = ...
    #@override
    _6oresult_only_ = False
######################
######################
class RecognizerLLoo__the_first_one__tagged__6oresult_only(_IRecognizerLLoo__the_first_one):
    #@override
    _bare_vs_cased_vs_tagged_ = True
    #@override
    _6oresult_only_ = True
class RecognizerLLoo__the_only_one__tagged__6oresult_only(_IRecognizerLLoo__the_only_one):
    #@override
    _bare_vs_cased_vs_tagged_ = True
    #@override
    _6oresult_only_ = True
######################
class RecognizerLLoo__the_first_one__cased__6oresult_only(_IRecognizerLLoo__the_first_one):
    #@override
    _bare_vs_cased_vs_tagged_ = ...
    #@override
    _6oresult_only_ = True
class RecognizerLLoo__the_only_one__cased__6oresult_only(_IRecognizerLLoo__the_only_one):
    #@override
    _bare_vs_cased_vs_tagged_ = ...
    #@override
    _6oresult_only_ = True
######################
check_non_ABC(RecognizerLLoo__the_first_one)
check_non_ABC(RecognizerLLoo__the_only_one)
######################
check_non_ABC(RecognizerLLoo__the_first_one__tagged)
check_non_ABC(RecognizerLLoo__the_only_one__tagged)
check_non_ABC(RecognizerLLoo__the_first_one__cased)
check_non_ABC(RecognizerLLoo__the_only_one__cased)
######################
check_non_ABC(RecognizerLLoo__the_first_one__tagged__6oresult_only)
check_non_ABC(RecognizerLLoo__the_only_one__tagged__6oresult_only)
check_non_ABC(RecognizerLLoo__the_first_one__cased__6oresult_only)
check_non_ABC(RecognizerLLoo__the_only_one__cased__6oresult_only)
######################



_Ts4the_first_one = \
(RecognizerLLoo__the_first_one
,RecognizerLLoo__the_first_one__tagged
,RecognizerLLoo__the_first_one__cased
,RecognizerLLoo__the_first_one__tagged__6oresult_only
,RecognizerLLoo__the_first_one__cased__6oresult_only
)
_Ts4the_only_one = \
(RecognizerLLoo__the_only_one
,RecognizerLLoo__the_only_one__tagged
,RecognizerLLoo__the_only_one__cased
,RecognizerLLoo__the_only_one__tagged__6oresult_only
,RecognizerLLoo__the_only_one__cased__6oresult_only
)

def _mk_LLoo__the_xxx_one(Ts, rgnrs, /, *, tagged=False, cased=False, _6oresult_only_=False):
    if tagged and cased:raise TypeError
    if not (tagged or cased) and _6oresult_only_:raise TypeError
    if not tagged:
        if not cased:
            assert not _6oresult_only_
            i = 0
        else:
            i = 2 if not _6oresult_only_ else 4
        i
    else:
        assert not cased
        if not cased:
            i = 1 if not _6oresult_only_ else 3
        else:
            raise 000
        i
    i
    T = Ts[i]
    return T(rgnrs)
def mk_LLoo__the_first_one(rgnrs, /, *, tagged=False, cased=False, _6oresult_only_=False):
    '[IRecognizerLLoo] -> IRecognizerLLoo #the_first_one/choice'
    return _mk_LLoo__the_xxx_one(_Ts4the_first_one, rgnrs, tagged=tagged, cased=cased, _6oresult_only_=_6oresult_only_)
def mk_LLoo__the_only_one(rgnrs, /, *, tagged=False, cased=False, _6oresult_only_=False):
    '[IRecognizerLLoo] -> IRecognizerLLoo #the_only_one/parallel'
    return _mk_LLoo__the_xxx_one(_Ts4the_only_one, rgnrs, tagged=tagged, cased=cased, _6oresult_only_=_6oresult_only_)
mk_LLoo__choice = mk_LLoo__the_first_one
mk_LLoo__parallel = mk_LLoo__the_only_one

__all__
from seed.recognize.recognizer_LLoo_.combinator_LLoo__parallel import \
(RecognizerLLoo__the_first_one
,RecognizerLLoo__the_only_one
,RecognizerLLoo__the_first_one__tagged
,RecognizerLLoo__the_only_one__tagged
,RecognizerLLoo__the_first_one__cased
,RecognizerLLoo__the_only_one__cased
)

from seed.recognize.recognizer_LLoo_.combinator_LLoo__parallel import \
(mk_LLoo__the_first_one
    ,mk_LLoo__choice
,mk_LLoo__the_only_one
    ,mk_LLoo__parallel
)

from seed.recognize.recognizer_LLoo_.combinator_LLoo__parallel import *
