#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/recognizer_LLoo_/combinator_LLoo__wrapper.py

seed.recognize.recognizer_LLoo_.combinator_LLoo__wrapper
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_LLoo_.combinator_LLoo__wrapper -x
py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LLoo_.combinator_LLoo__wrapper:__doc__ -ht
#]]]'''
__all__ = r'''
ICallable__using_IDependentTreeNode
    Callable__ref
_IDependentTreeNode__ref__init



IRecognizerLLoo__wrapper_base
    _IRecognizerLLoo__wrapper_base__single_ref
    IRecognizerLLoo__lazy_wrapper
        RecognizerLLoo__lazy_wrapper
IRecognizerLLoo__wrapper
    IRecognizerLLoo__wrapper4simple_postprocess
        RecognizerLLoo__wrapper4simple_postprocess
        IRecognizerLLoo__wrapper4simple_postprocess6ok
            RecognizerLLoo__wrapper4simple_postprocess6ok
        IRecognizerLLoo__wrapper4simple_postprocess6err
            RecognizerLLoo__wrapper4simple_postprocess6err


RecognizerLLoo__validate_two_phases
    RecognizerLLoo__skip_header_signal
    RecognizerLLoo__header_signal_at_beginning
    RecognizerLLoo__patch_header_signal_if_ok

RecognizerLLoo__tag
    RecognizerLLoo__Cased
RecognizerLLoo__invert_err_ok

RecognizerLLoo__tribool_skip
    RecognizerLLoo__tribool_skip__as
    RecognizerLLoo__skip
    RecognizerLLoo__pack
    RecognizerLLoo__unpack
    RecognizerLLoo__unbox


IRecognizerLLoo__try
    RecognizerLLoo__try__rollback_if_fail_before_hdr_sgnl_else_lift
    RecognizerLLoo__optional__either
    RecognizerLLoo__optional__tmay
    RecognizerLLoo__optional__default

RecognizerLLoo__look_ahead__no_err4hdr
    RecognizerLLoo__look_ahead__no_err4whole
RecognizerLLoo__look_ahead4hdr
    RecognizerLLoo__look_ahead4whole
RecognizerLLoo__not_followed_by4hdr
    RecognizerLLoo__not_followed_by4whole



IRecognizerLLoo__wrapper4simple_postprocess6ok
    IRecognizerLLoo__constant_overwrite6ok
        RecognizerLLoo__constant_overwrite6ok
IRecognizerLLoo__wrapper4simple_postprocess6err
    IRecognizerLLoo__constant_overwrite6err
        RecognizerLLoo__constant_overwrite6err
IRecognizerLLoo__wrapper4simple_postprocess
    IRecognizerLLoo__constant_overwrite
        RecognizerLLoo__constant_overwrite


IRecognizerLLoo__constant_eresult
    RecognizerLLoo__ignore
        recognizer_LLoo__ignore
    RecognizerLLoo__constant_eresult
        recognizer_LLoo__pass
        recognizer_LLoo__fail




RecognizerLLoo__named_wrapper
RecognizerLLoo__ref





mk_LLoo__with_tribool_skip
    mk_LLoo__with_tribool_skip_as
    mk_LLoo__skip
    mk_LLoo__pack
    mk_LLoo__unpack

mk_LLoo__simple_postprocess
mk_LLoo__simple_postprocess6ok
mk_LLoo__simple_postprocess6err
mk_LLoo__validate_two_phases
mk_LLoo__skip_header_signal
mk_LLoo__header_signal_at_beginning
mk_LLoo__patch_header_signal_if_ok
mk_LLoo__tag
mk_LLoo__Cased
mk_LLoo__invert_err_ok
mk_LLoo__unbox
mk_LLoo__try__rollback_if_fail_before_hdr_sgnl_else_lift
mk_LLoo__optional__either
mk_LLoo__optional__tmay
mk_LLoo__optional__default
mk_LLoo__look_ahead__no_err4hdr
mk_LLoo__look_ahead__no_err4whole
mk_LLoo__look_ahead4hdr
mk_LLoo__look_ahead4whole
mk_LLoo__not_followed_by4hdr
mk_LLoo__not_followed_by4whole
mk_LLoo__constant_overwrite6ok
mk_LLoo__constant_overwrite6err
mk_LLoo__constant_overwrite
mk_LLoo__constant_eresult
mk_LLoo__named_wrapper
mk_LLoo__ref
mk_LLoo__lazy

'''.split()#'''
    #RecognizerLLoo__skip#vs:RecognizerLLoo__constant_overwrite6ok__null_tuple
        #xxx:RecognizerLLoo__constant_overwrite6ok__null_tuple
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.recognize.recognizer_LLoo_._common import (IForkable__stamp
,mk_gi4either8xresult# detach_asif_new_gi_wrapper
,mk_gi4xresult_xexception__as_
,mk_gi4return
,BoxedFinalResult, BoxedHalfwayResult, BoxedTailRecur
,Cased, Either, mk_Left, mk_Right

,check_non_ABC
,check_type_is, check_type_le
,mk_tuple, null_tuple, null_iter
,abstractmethod, override, ABC
,repr_helper, _Base4repr # sf._args4repr = (...)
)
from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import IWrapper, IRecognizerLLoo, Signal__HeaderCompleted, Reply4IRecognizerLLoo, Error__not_Reply4IRecognizerLLoo_after_Signal__HeaderCompleted
from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import mk_gi4skip_header_signal, mk_gi4header_signal_at_beginning, mk_gi4patch_header_signal_if_ok, mk_gi4validate_two_phases
from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import INamed, IDependentTreeNode__ref, IScene
from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import IDependentTreeNode


from seed.tiny_.check import check_callable, check_pseudo_qual_name


from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots

from collections.abc import Callable as ICallable

from seed.recognize.recognizer_LLoo_.IScene import ILazyWrapper
___end_mark_of_excluded_global_names__0___ = ...

class IRecognizerLLoo__wrapper_base(IRecognizerLLoo, IDependentTreeNode, IWrapper):
    '[force:IDependentTreeNode above IWrapper]'
    __slots__ = ()
    @property
    @override
    def ___666_tribool_skip4serial4LLoo_999___(sf, /):
        '-> tribool'
        return sf.the_wrapped_obj.___666_tribool_skip4serial4LLoo_999___

    #@override
    _base_type4wrapped_obj_ = IRecognizerLLoo

    @override
    def _iter4two_phases_recognize_(sf, inputter4whole, /):
        raw_gi = sf.the_wrapped_obj._iter4two_phases_recognize_(inputter4whole)
        return raw_gi
class IRecognizerLLoo__wrapper(IRecognizerLLoo__wrapper_base):
    'YS_GI<I->O>:yield-send-version-IGeneratorIterator-for-recur5yield__list__echo__echo'
    __slots__ = ()
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

    @override
    def _iter4two_phases_recognize_(sf, inputter4whole, /):
        if not None is (preprocess := sf.may_preprocess):
            (state, inputter4whole) = yield preprocess(inputter4whole)
        else:
            state = None#init
            inputter4whole
        (state, inputter4whole)
        raw_gi = sf.the_wrapped_obj._iter4two_phases_recognize_(inputter4whole)
        del inputter4whole
        if None is sf.may_header_signal_process is sf.may_postprocess:
            return BoxedTailRecur(raw_gi)
        cased_gi = mk_gi4either8xresult(raw_gi, ___666_close_wrapped_gi_999___=False)
        x = yield cased_gi
        if x.is_left:
            hdr_sgnl, _2_cased_gi = x.left
            check_type_is(Signal__HeaderCompleted, hdr_sgnl)
            if not _2_cased_gi is cased_gi:
                cased_gi = _2_cased_gi
                raw_gi = mk_gi4xresult_xexception__as_(raw_gi, _2_cased_gi)
            cased_tail_gi_after_hdr_sgnl = cased_gi
            raw_tail_gi_after_hdr_sgnl = raw_gi
            del cased_gi, raw_gi, _2_cased_gi
            if not None is (header_signal_process := sf.may_header_signal_process):
                #detach_asif_new_gi_wrapper(raw_tail_gi_after_hdr_sgnl, cased_tail_gi_after_hdr_sgnl)
                del cased_tail_gi_after_hdr_sgnl
                (state, may_hdr_sgnl, raw_tail_gi_after_hdr_sgnl) = yield header_signal_process(state, hdr_sgnl, raw_tail_gi_after_hdr_sgnl)
                cased_tail_gi_after_hdr_sgnl = mk_gi4either8xresult(raw_tail_gi_after_hdr_sgnl, ___666_close_wrapped_gi_999___=False)
                if may_hdr_sgnl is None:
                    pass#drop:hdr_sgnl
                else:
                    hdr_sgnl = may_hdr_sgnl
                    check_type_is(Signal__HeaderCompleted, hdr_sgnl)
                    yield BoxedHalfwayResult(hdr_sgnl)
                    del hdr_sgnl
                (state, cased_tail_gi_after_hdr_sgnl)
            else:
                yield BoxedHalfwayResult(hdr_sgnl)
                del hdr_sgnl
                (state, cased_tail_gi_after_hdr_sgnl)
            (state, cased_tail_gi_after_hdr_sgnl)
            if None is sf.may_postprocess:
                #detach_asif_new_gi_wrapper(raw_tail_gi_after_hdr_sgnl, cased_tail_gi_after_hdr_sgnl)
                del cased_tail_gi_after_hdr_sgnl
                return BoxedTailRecur(raw_tail_gi_after_hdr_sgnl)
            y = yield cased_tail_gi_after_hdr_sgnl
            del cased_tail_gi_after_hdr_sgnl
            del raw_tail_gi_after_hdr_sgnl
            if not y.is_right:
                raise Error__not_Reply4IRecognizerLLoo_after_Signal__HeaderCompleted
            x = y
            del y
            state, x
        else:
            del cased_gi
            del raw_gi
            x
            state, x
        state, x
        assert x.is_right
        reply4LLoo = x.right
        check_type_is(Reply4IRecognizerLLoo, reply4LLoo)
        if not None is (postprocess := sf.may_postprocess):
            reply4LLoo = yield postprocess(state, reply4LLoo)
            check_type_is(Reply4IRecognizerLLoo, reply4LLoo)
        else:
            del state
            reply4LLoo
        reply4LLoo
        return BoxedFinalResult(reply4LLoo)
['_iter_direct_child_dependent_tree_nodes_', '_iter_directly_used_kinded_names_', 'scene', 'the_wrapped_obj']





















class IRecognizerLLoo__lazy_wrapper(IRecognizerLLoo__wrapper_base, ILazyWrapper):
    __slots__ = ()
    @abstractmethod
    def unlazy(sf, /):
        '-> the_underlying_wrapped_recognizer_LLoo/IRecognizerLLoo'























class IRecognizerLLoo__wrapper4simple_postprocess(IRecognizerLLoo__wrapper):
    __slots__ = ()
    @abstractmethod
    def _simple_postprocess_(sf, eresult, /):
        'eresult -> eresult/Either'
    def simple_postprocess(sf, eresult, /):
        'eresult -> eresult/Either'
        check_type_is(Either, eresult)
        eresult = sf._simple_postprocess_(eresult)
        check_type_is(Either, eresult)
        return eresult
    may_preprocess = None
    may_header_signal_process = None
    #bug:@property
    @override
    def may_postprocess(sf, state, reply4LLoo, /):
        'YS_GI(state -> Reply4IRecognizerLLoo -> Reply4IRecognizerLLoo)'
        #'-> may postprocess/YS_GI(state -> Reply4IRecognizerLLoo -> Reply4IRecognizerLLoo)'
        eresult = reply4LLoo.the_eresult
        eresult = sf.simple_postprocess(eresult)
        reply4LLoo = reply4LLoo.ireplace__eresult(eresult)
        reply4LLoo
        return BoxedFinalResult(reply4LLoo)
        777;    yield





class IRecognizerLLoo__wrapper4simple_postprocess6ok(IRecognizerLLoo__wrapper4simple_postprocess):
    'simple_postprocess6ok:[Reply4IRecognizerLLoo.ok is True]'
    __slots__ = ()
    @abstractmethod
    def simple_postprocess6ok(sf, oresult, /):
        'oresult -> oresult/result6ok4LLoo'
    @override
    def _simple_postprocess_(sf, eresult, /):
        'eresult -> eresult/Either'
        return eresult.fmap_if_right(sf.simple_postprocess6ok)







class IRecognizerLLoo__wrapper4simple_postprocess6err(IRecognizerLLoo__wrapper4simple_postprocess):
    'simple_postprocess6err:[Reply4IRecognizerLLoo.ok is False]'
    __slots__ = ()
    @abstractmethod
    def simple_postprocess6err(sf, errmsg, /):
        'errmsg -> errmsg/result6err4LLoo'
    @override
    def _simple_postprocess_(sf, eresult, /):
        'eresult -> eresult/Either'
        return eresult.fmap_if_left(sf.simple_postprocess6err)
























r'''[[[
#anchor
not_followed_by4whole
look_ahead4whole
not_followed_by4hdr
look_ahead4hdr
look_ahead__no_err4hdr
look_ahead__no_err4whole

#anchor@fail-before-hdr_sgnl,move_on@succ/fail-after-hdr_sgnl
    fail_before_hdr_sgnl
    fail_after_hdr_sgnl
try/try__rollback_if_fail_before_hdr_sgnl_else_lift

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


parserTrace:print_err(pos)@beginning
parserTraced:print_err(pos)@beginning +@err
#]]]'''#'''



class _IRecognizerLLoo__wrapper_base__single_ref(IRecognizerLLoo__wrapper_base, _Base4repr):
    ___no_slots_ok___ = True
    def __init__(sf, /, *args):
        #def __init__(sf, rgnr, /):
        if not args:raise TypeError
        rgnr = args[-1]
        check_type_le(IRecognizerLLoo, rgnr)
        sf._rgnr = rgnr
        #_Base4repr.__init__(sf, *args)
        sf._args4repr = args
    @property
    @override
    def the_wrapped_obj(sf, /):
        '-> wrapped_obj'
        return sf._rgnr

    @override
    def _iter_directly_used_kinded_names_(sf, /):
        '-> Iter knm/kinded_name'
        return null_iter
    @override
    def _iter_direct_child_dependent_tree_nodes_(sf, /):
        '-> Iter IDependentTreeNode'
        yield sf.the_wrapped_obj
        return

class _IRecognizerLLoo__wrapper__single_ref(_IRecognizerLLoo__wrapper_base__single_ref, IRecognizerLLoo__wrapper):
    pass












class RecognizerLLoo__lazy_wrapper(_IRecognizerLLoo__wrapper_base__single_ref, IRecognizerLLoo__lazy_wrapper):# _Base4repr
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        return repr_helper(sf, sf._x, non_lazy=sf._b)
    def __init__(sf, lazy_or_rgnr, /, *, non_lazy=False):
        sf._x = lazy_or_rgnr
        sf._b = non_lazy
        check_type_is(bool, non_lazy)
        if non_lazy:
            rgnr = lazy_or_rgnr
            check_type_le(IRecognizerLLoo, rgnr)
        else:
            lazy__rgnr = lazy_or_rgnr
            check_callable(lazy__rgnr)
    @override
    def unlazy(sf, /):
        '-> the_underlying_wrapped_recognizer_LLoo/IRecognizerLLoo'
        #if non_lazy:
        lazy_or_rgnr = sf._x
        non_lazy = sf._b
        if non_lazy:
            rgnr = lazy_or_rgnr
        else:
            lazy__rgnr = lazy_or_rgnr
            sf._x = rgnr = lazy__rgnr()
            sf._b = non_lazy = True
            return sf.unlazy()
        return rgnr
check_non_ABC(RecognizerLLoo__lazy_wrapper)






















class _IRecognizerLLoo__wrapper_base__single_ref__tribool_skip(_IRecognizerLLoo__wrapper_base__single_ref):
    def __init__(sf, tribool_skip, rgnr, /):
        if not tribool_skip is ...:
            check_type_is(bool, tribool_skip)
        sf._t = tribool_skip
        super().__init__(tribool_skip, rgnr)
    @property
    @override
    def ___666_tribool_skip4serial4LLoo_999___(sf, /):
        '-> tribool'
        return sf._t


class _IRecognizerLLoo__wrapper_base__single_ref__tribool_skip__as(_IRecognizerLLoo__wrapper_base__single_ref):
    def __init__(sf, rgnr8src, rgnr8dst, /):
        check_type_le(IRecognizerLLoo, rgnr8src)
        sf._t = None
        sf._src = rgnr8src
        super().__init__(tribool_skip, rgnr8dst)
        _args4repr = (rgnr8src, rgnr8dst)
    @property
    @override
    def ___666_tribool_skip4serial4LLoo_999___(sf, /):
        '-> tribool'
        if not None is (t := sf._t):
            return t
        sf._t = sf._src.___666_tribool_skip4serial4LLoo_999___
        return sf.___666_tribool_skip4serial4LLoo_999___







class ICallable__using_IDependentTreeNode(ICallable, IDependentTreeNode):
    'see:simple_postprocess/simple_postprocess6ok/simple_postprocess6err'
    __slots__ = ()
    @abstractmethod
    def __call__(sf, /, *args):
        '-> ?'

class _IDependentTreeNode__ref__init(IDependentTreeNode__ref, _Base4repr):
    ___no_slots_ok___ = True
    def __init__(sf, scene, kinded_name, /):
        check_type_le(IScene, scene)
        sf._sc = scene
        sf._knm = kinded_name
        #_Base4repr.__init__(sf, scene, kinded_name)
        sf._args4repr = (scene, kinded_name)

    @property
    @override
    def its_kinded_name(sf, /):
        '-> knm/kinded_name/(hashable&&immutable)'
        return sf._knm
    @property
    @override
    def scene(sf, /):
        '-> IScene'
        return sf._sc

class Callable__ref(ICallable__using_IDependentTreeNode, _IDependentTreeNode__ref__init):
    'see:simple_postprocess/simple_postprocess6ok/simple_postprocess6err'
    #@override
    _base_type4wrapped_obj_ = ICallable
    @override
    def __call__(sf, /, *args):
        '-> ?'
        return sf.the_wrapped_obj(*args)
check_non_ABC(Callable__ref)

class RecognizerLLoo__wrapper4simple_postprocess(_IRecognizerLLoo__wrapper_base__single_ref, IRecognizerLLoo__wrapper4simple_postprocess):
    'simple_postprocess'
    ___no_slots_ok___ = True
    def __init__(sf, eresult2eresult_, rgnr, /):
        check_callable(eresult2eresult_)
        sf._e2e = eresult2eresult_
        super().__init__(eresult2eresult_, rgnr)
    @property
    @override
    def _simple_postprocess_(sf, /):
        '-> (eresult -> eresult/Either)'
        return sf._e2e
    @override
    def _iter_direct_child_dependent_tree_nodes_(sf, /):
        '-> Iter IDependentTreeNode'
        yield sf.the_wrapped_obj
        f = sf._e2e
        if isinstance(f, IDependentTreeNode):
            yield f
        return
check_non_ABC(RecognizerLLoo__wrapper4simple_postprocess)



class RecognizerLLoo__wrapper4simple_postprocess6ok(_IRecognizerLLoo__wrapper_base__single_ref, IRecognizerLLoo__wrapper4simple_postprocess6ok):
    'simple_postprocess6ok'
    ___no_slots_ok___ = True
    def __init__(sf, oresult2oresult_, rgnr, /):
        check_callable(oresult2oresult_)
        sf._o2o = oresult2oresult_
        super().__init__(oresult2oresult_, rgnr)
    @property
    @override
    def simple_postprocess6ok(sf, /):
        '-> (oresult -> oresult/result6ok4LLoo)'
        return sf._o2o
    @override
    def _iter_direct_child_dependent_tree_nodes_(sf, /):
        '-> Iter IDependentTreeNode'
        yield sf.the_wrapped_obj
        f = sf._o2o
        if isinstance(f, IDependentTreeNode):
            yield f
        return

check_non_ABC(RecognizerLLoo__wrapper4simple_postprocess6ok)













class RecognizerLLoo__wrapper4simple_postprocess6err(_IRecognizerLLoo__wrapper_base__single_ref, IRecognizerLLoo__wrapper4simple_postprocess6err):
    'simple_postprocess6err'
    ___no_slots_ok___ = True
    def __init__(sf, errmsg2errmsg_, rgnr, /):
        check_callable(errmsg2errmsg_)
        sf._m2m = errmsg2errmsg_
        super().__init__(errmsg2errmsg_, rgnr)
    @property
    @override
    def simple_postprocess6err(sf, /):
        '-> (errmsg -> errmsg/result6err4LLoo)'
        return sf._m2m
    @override
    def _iter_direct_child_dependent_tree_nodes_(sf, /):
        '-> Iter IDependentTreeNode'
        yield sf.the_wrapped_obj
        f = sf._m2m
        if isinstance(f, IDependentTreeNode):
            yield f
        return

check_non_ABC(RecognizerLLoo__wrapper4simple_postprocess6err)
















class _IRecognizerLLoo__handle_gi4two_phases_recognize(_IRecognizerLLoo__wrapper_base__single_ref):
    @abstractmethod
    def _handle_gi4two_phases_recognize_(sf, inputter4whole, gi4two_phases_recognize, /):
        'gi4two_phases_recognize -> gi4two_phases_recognize'
    @override
    def _iter4two_phases_recognize_(sf, inputter4whole, /):
        gi4two_phases_recognize = super()._iter4two_phases_recognize_(inputter4whole)
        gi4two_phases_recognize = sf._handle_gi4two_phases_recognize_(inputter4whole, gi4two_phases_recognize)
        return gi4two_phases_recognize
class RecognizerLLoo__skip_header_signal(_IRecognizerLLoo__handle_gi4two_phases_recognize):
    'see:mk_gi4skip_header_signal#<==>mk_gi4header_signal_at_end#vs:mk_gi4header_signal_at_beginning'
    @override
    def _handle_gi4two_phases_recognize_(sf, inputter4whole, gi4two_phases_recognize, /):
        'gi4two_phases_recognize -> gi4two_phases_recognize'
        return mk_gi4skip_header_signal(gi4two_phases_recognize)
check_non_ABC(RecognizerLLoo__skip_header_signal)
class RecognizerLLoo__header_signal_at_beginning(_IRecognizerLLoo__handle_gi4two_phases_recognize):
    'see:mk_gi4header_signal_at_beginning#vs:mk_gi4skip_header_signal'
    @override
    def _handle_gi4two_phases_recognize_(sf, inputter4whole, gi4two_phases_recognize, /):
        'gi4two_phases_recognize -> gi4two_phases_recognize'
        return mk_gi4header_signal_at_beginning(inputter4whole, gi4two_phases_recognize)
check_non_ABC(RecognizerLLoo__header_signal_at_beginning)
class RecognizerLLoo__patch_header_signal_if_ok(_IRecognizerLLoo__handle_gi4two_phases_recognize):
    'see:mk_gi4patch_header_signal_if_ok'
    @override
    def _handle_gi4two_phases_recognize_(sf, inputter4whole, gi4two_phases_recognize, /):
        'gi4two_phases_recognize -> gi4two_phases_recognize'
        return mk_gi4patch_header_signal_if_ok(gi4two_phases_recognize)
check_non_ABC(RecognizerLLoo__patch_header_signal_if_ok)
class RecognizerLLoo__validate_two_phases(_IRecognizerLLoo__handle_gi4two_phases_recognize):
    'see:mk_gi4validate_two_phases'
    @override
    def _handle_gi4two_phases_recognize_(sf, inputter4whole, gi4two_phases_recognize, /):
        'gi4two_phases_recognize -> gi4two_phases_recognize'
        return mk_gi4validate_two_phases(gi4two_phases_recognize)
check_non_ABC(RecognizerLLoo__validate_two_phases)








class RecognizerLLoo__tag(_IRecognizerLLoo__wrapper__single_ref, IRecognizerLLoo__wrapper4simple_postprocess):
    'tag:cased...#vs:RecognizerLLoo__Cased #[eresult = Either<(errmsg if _6oresult_only_ else tagged errmsg), (tagged oresult)>]'
    #_6oresult_only_ = False
    #   '-> bool # [eresult = Either<(errmsg if _6oresult_only_ else tagged errmsg), (tagged oresult)>]'
    _type4eresult_ = tuple
    def _tagged_(sf, tag, payload, /):
        return (tag, payload)
    def __init__(sf, _6oresult_only_, tag, rgnr, /):
        #def __init__(sf, tag, rgnr, /, *, _6oresult_only_=False):
        check_type_is(bool, _6oresult_only_)
        sf._6oresult_only_ = _6oresult_only_
        sf._tg = tag
        super().__init__(tag, rgnr)
    @property
    def tag(sf, /):
        return sf._tg

    @override
    def _simple_postprocess_(sf, eresult, /):
        'eresult -> eresult/Either'
        if sf._6oresult_only_ and eresult.is_left:
            new_eresult = eresult
        else:
            new_eresult = eresult.fmap4payload(lambda x:sf._tagged_(sf.tag, x))
        return new_eresult
check_non_ABC(RecognizerLLoo__tag)




class RecognizerLLoo__Cased(RecognizerLLoo__tag):
    'tag:cased...#vs:RecognizerLLoo__tag #[eresult = Either<(errmsg if _6oresult_only_ else tagged errmsg), (tagged oresult)>]'
    #@override
    _type4eresult_ = Cased
    @override
    def _tagged_(sf, tag, payload, /):
        return Cased(tag, payload)
    @property
    def case(sf, /):
        return sf.tag

check_non_ABC(RecognizerLLoo__Cased)




class RecognizerLLoo__invert_err_ok(_IRecognizerLLoo__wrapper__single_ref, IRecognizerLLoo__wrapper4simple_postprocess):
    'invert_err_ok'
    @override
    def _simple_postprocess_(sf, eresult, /):
        'eresult -> eresult/Either'
        return ~eresult
check_non_ABC(RecognizerLLoo__invert_err_ok)







class RecognizerLLoo__tribool_skip(_IRecognizerLLoo__wrapper_base__single_ref__tribool_skip):
    pass
check_non_ABC(RecognizerLLoo__tribool_skip)

class RecognizerLLoo__tribool_skip__as(_IRecognizerLLoo__wrapper_base__single_ref__tribool_skip__as):
    'see:RecognizerLLoo__lazy_wrapper'
    pass
check_non_ABC(RecognizerLLoo__tribool_skip__as)


class RecognizerLLoo__skip(_IRecognizerLLoo__wrapper_base__single_ref):
    'skip # [[a] -> []] #combinator_LLoo__serial:skip'
    #see:RecognizerLLoo__constant_overwrite6ok__null_tuple
    #@property
    #@override
    ___666_tribool_skip4serial4LLoo_999___ = True # False-append;True-skip;...-extend
check_non_ABC(RecognizerLLoo__skip)








class RecognizerLLoo__pack(_IRecognizerLLoo__wrapper_base__single_ref):
    'pack # [a -> a] #combinator_LLoo__serial:pack'
    #@property
    #@override
    ___666_tribool_skip4serial4LLoo_999___ = False # False-append;True-skip;...-extend
check_non_ABC(RecognizerLLoo__pack)













class RecognizerLLoo__unpack(_IRecognizerLLoo__wrapper_base__single_ref):
    'unpack # [[a] -> [*a]] #combinator_LLoo__serial:extend'
    #@property
    #@override
    ___666_tribool_skip4serial4LLoo_999___ = ... # False-append;True-skip;...-extend
check_non_ABC(RecognizerLLoo__unpack)





class RecognizerLLoo__unbox(_IRecognizerLLoo__wrapper__single_ref, IRecognizerLLoo__wrapper4simple_postprocess6ok):
    'unbox # [[a]{len=1} -> a]'
    @override
    def simple_postprocess6ok(sf, oresult, /):
        'oresult -> oresult/result6ok4LLoo'
        [new_oresult] = oresult
        return new_oresult
check_non_ABC(RecognizerLLoo__unbox)


















class IRecognizerLLoo__try(_IRecognizerLLoo__wrapper__single_ref):
    'try/try__rollback_if_fail_before_hdr_sgnl_else_lift:[rollback:fail_before_hdr_sgnl<==>not ok][ok=>lifted][lift:oresult<sf> == reply4LLoo<the_wrapped_obj>@(succ|fail_after_hdr_sgnl)] #used in RecognizerLLoo__the_first_one'
    #'try/try__rollback_if_fail_before_hdr_sgnl_else_lift:[fail_before_hdr_sgnl<==>not ok][ok=>lifted]'
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
            #succ or fail_after_hdr_sgnl
            reply4LLoo = reply4LLoo.ilift()
            assert reply4LLoo.ok
        else:
            #fail_before_hdr_sgnl
            inputter4whole = state
            reply4LLoo = ~reply4LLoo.ilift_(inputter4end:=inputter4whole)
            assert not reply4LLoo.ok
        reply4LLoo
        # [#fail_before_hdr_sgnl<==>not ok#]
        reply4LLoo = sf._postpostprocess4try_(reply4LLoo)
        return BoxedFinalResult(reply4LLoo)
        777;   yield
    @abstractmethod
    def _postpostprocess4try_(sf, reply4LLoo, /):
        'Reply4IRecognizerLLoo[#fail_before_hdr_sgnl<==>not ok#] -> Reply4IRecognizerLLoo'



class RecognizerLLoo__try__rollback_if_fail_before_hdr_sgnl_else_lift(IRecognizerLLoo__try):
    #class RecognizerLLoo__try(IRecognizerLLoo__try):
    'try/try__rollback_if_fail_before_hdr_sgnl_else_lift:[rollback:fail_before_hdr_sgnl<==>not ok][ok=>lifted][lift:oresult<sf> == reply4LLoo<the_wrapped_obj>@(succ|fail_after_hdr_sgnl)] #used in RecognizerLLoo__the_first_one'
    @override
    def _postpostprocess4try_(sf, reply4LLoo, /):
        'Reply4IRecognizerLLoo[#fail_before_hdr_sgnl<==>not ok#] -> Reply4IRecognizerLLoo'
        return reply4LLoo
check_non_ABC(RecognizerLLoo__try__rollback_if_fail_before_hdr_sgnl_else_lift)


class RecognizerLLoo__optional__either(IRecognizerLLoo__try):
    'optional__tmay:[fail_after_hdr_sgnl<==>not ok]'
    @override
    def _postpostprocess4try_(sf, reply4LLoo, /):
        'Reply4IRecognizerLLoo[#fail_before_hdr_sgnl<==>not ok#] -> Reply4IRecognizerLLoo'
        if reply4LLoo.ok:
            #succ or fail_after_hdr_sgnl
            reply4LLoo = reply4LLoo.oresult
                #unlift
            check_type_is(Reply4IRecognizerLLoo, reply4LLoo)
            if reply4LLoo.ok:
                #succ
                either8oresult = reply4LLoo.the_eresult#mk_Right(reply4LLoo.oresult)
                eresult = mk_Right(either8oresult)
                    #[ok]
                reply4LLoo = reply4LLoo.ireplace__eresult(eresult)
            else:
                #fail_after_hdr_sgnl
                # [not ok]
                reply4LLoo
                    #[not ok]
                pass
            reply4LLoo
        else:
            #fail_before_hdr_sgnl
            either8oresult = reply4LLoo.the_eresult#mk_Left(reply4LLoo.errmsg)
            eresult = mk_Right(either8oresult)
                #[ok]
            reply4LLoo = reply4LLoo.ireplace__eresult(eresult)
        reply4LLoo
        return reply4LLoo
check_non_ABC(RecognizerLLoo__optional__either)


class RecognizerLLoo__optional__tmay(IRecognizerLLoo__try):
    'optional__tmay:[fail_after_hdr_sgnl<==>not ok]'
    @override
    def _postpostprocess4try_(sf, reply4LLoo, /):
        'Reply4IRecognizerLLoo[#fail_before_hdr_sgnl<==>not ok#] -> Reply4IRecognizerLLoo'
        reply4LLoo = RecognizerLLoo__optional__either._postpostprocess4try_(_sf_:=None, reply4LLoo)
        if reply4LLoo.ok:
            #succ or fail_before_hdr_sgnl
            either8oresult = reply4LLoo.oresult
            check_type_is(Either, either8oresult)
            tmay8oresult = either8oresult.to_tmay_right()
            reply4LLoo = reply4LLoo.ireplace__oresult(tmay8oresult)
        else:
            #fail_after_hdr_sgnl
            reply4LLoo
        reply4LLoo
        return reply4LLoo
check_non_ABC(RecognizerLLoo__optional__tmay)


class RecognizerLLoo__optional__default(IRecognizerLLoo__try):
    'optional__tmay:[fail_after_hdr_sgnl<==>not ok]'
    def __init__(sf, oresult8default, rgnr, /):
        sf._o = oresult8default
        super().__init__(oresult8default, rgnr)
    @override
    def _postpostprocess4try_(sf, reply4LLoo, /):
        'Reply4IRecognizerLLoo[#fail_before_hdr_sgnl<==>not ok#] -> Reply4IRecognizerLLoo'
        reply4LLoo = RecognizerLLoo__optional__either._postpostprocess4try_(_sf_:=None, reply4LLoo)
        if reply4LLoo.ok:
            #succ or fail_before_hdr_sgnl
            either8oresult = reply4LLoo.oresult
            check_type_is(Either, either8oresult)
            oresult8default = sf._o
            oresult = either8oresult.to_right__default_(oresult8default)
            reply4LLoo = reply4LLoo.ireplace__oresult(oresult)
        else:
            #fail_after_hdr_sgnl
            reply4LLoo
        reply4LLoo
        return reply4LLoo
check_non_ABC(RecognizerLLoo__optional__default)














class _IRecognizerLLoo__look_ahead(_IRecognizerLLoo__wrapper__single_ref):
    #@property
    #@override
    ___666_tribool_skip4serial4LLoo_999___ = True#skip
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
            may_hdr_sgnl = hdr_sgnl.ilift_(inputter4body:=state)
            return BoxedFinalResult((state, may_hdr_sgnl, tail_gi_after_hdr_sgnl))
        #look_ahead4hdr
        reply4LLoo = Reply4IRecognizerLLoo(num_consumed:=0, inputter4end:=inputter4whole, mk_Right(hdr_sgnl))
        if sf.to_inv_ok:
            reply4LLoo = ~reply4LLoo
        may_hdr_sgnl = None
        tail_gi_after_hdr_sgnl = mk_gi4return(BoxedFinalResult(reply4LLoo))
        return BoxedFinalResult((state, may_hdr_sgnl, tail_gi_after_hdr_sgnl))
        777;   yield
    @override
    def may_postprocess(sf, state, reply4LLoo, /):
        '-> may postprocess/YS_GI(state -> Reply4IRecognizerLLoo -> Reply4IRecognizerLLoo)'
        #succ/fail_before_hdr_sgnl
        inputter4whole = state
        ok = reply4LLoo.ok
        reply4LLoo = reply4LLoo.ilift_(inputter4end:=inputter4whole)
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








class IRecognizerLLoo__constant_overwrite6ok(_IRecognizerLLoo__wrapper__single_ref, IRecognizerLLoo__wrapper4simple_postprocess6ok):
    @property
    @abstractmethod
    def oresult(sf, /):
        '-> oresult/result6ok'
    @override
    def simple_postprocess6ok(sf, oresult, /):
        'oresult -> oresult/result6ok4LLoo'
        return sf.oresult

def __():
    class RecognizerLLoo__constant_overwrite6ok__null_tuple(IRecognizerLLoo__constant_overwrite6ok):
        'constant_overwrite6ok__null_tuple'
        #@override
        oresult = null_tuple
    check_non_ABC(RecognizerLLoo__constant_overwrite6ok__null_tuple)

class RecognizerLLoo__constant_overwrite6ok(IRecognizerLLoo__constant_overwrite6ok):
    'constant_overwrite6ok'
    def __init__(sf, oresult, rgnr, /):
        sf._o = oresult
        super().__init__(oresult, rgnr)
    @property
    @override
    def oresult(sf, /):
        '-> oresult/result6ok'
        return sf._o
check_non_ABC(RecognizerLLoo__constant_overwrite6ok)












class IRecognizerLLoo__constant_overwrite6err(_IRecognizerLLoo__wrapper__single_ref, IRecognizerLLoo__wrapper4simple_postprocess6err):
    @property
    @abstractmethod
    def errmsg(sf, /):
        '-> errmsg/result6err'
    @override
    def simple_postprocess6err(sf, errmsg, /):
        'errmsg -> errmsg/result6err4LLoo'
        return sf.errmsg


class RecognizerLLoo__constant_overwrite6err(IRecognizerLLoo__constant_overwrite6err):
    'constant_overwrite6err'
    def __init__(sf, errmsg, rgnr, /):
        sf._m = errmsg
        super().__init__(errmsg, rgnr)
    @property
    @override
    def errmsg(sf, /):
        '-> errmsg/result6err'
        return sf._m
check_non_ABC(RecognizerLLoo__constant_overwrite6err)










class IRecognizerLLoo__constant_overwrite(_IRecognizerLLoo__wrapper__single_ref, IRecognizerLLoo__wrapper4simple_postprocess):
    @property
    @abstractmethod
    def errmsg(sf, /):
        '-> errmsg/result6err'
    @property
    @abstractmethod
    def oresult(sf, /):
        '-> oresult/result6ok'
    @override
    def _simple_postprocess_(sf, eresult, /):
        'eresult -> eresult/Either'
        return eresult.ireplace__either(sf.errmsg, sf.oresult)


class RecognizerLLoo__constant_overwrite(IRecognizerLLoo__constant_overwrite):
    'constant_overwrite'
    def __init__(sf, errmsg, oresult, rgnr, /):
        sf._m = errmsg
        sf._o = oresult
        super().__init__(errmsg, oresult, rgnr)
    @property
    @override
    def errmsg(sf, /):
        '-> errmsg/result'
        return sf._m
    @property
    @override
    def oresult(sf, /):
        '-> oresult/result6ok'
        return sf._o
check_non_ABC(RecognizerLLoo__constant_overwrite)



























class IRecognizerLLoo__constant_eresult(IRecognizerLLoo):
    __slots__ = ()
    @property
    @abstractmethod
    def eresult(sf, /):
        '-> eresult/Either'
    @override
    def _iter4two_phases_recognize_(sf, inputter4whole, /):
        reply4LLoo = Reply4IRecognizerLLoo(inputter4end:=inputter4whole, sf.eresult)
        return BoxedFinalResult(reply4LLoo)
        777;    yield
    @override
    def _iter_directly_used_kinded_names_(sf, /):
        '-> Iter knm/kinded_name'
        return null_iter
    @override
    def _iter_direct_child_dependent_tree_nodes_(sf, /):
        '-> Iter IDependentTreeNode'
        return null_iter
class RecognizerLLoo__ignore(IRecognizerLLoo__constant_eresult):
    ___no_slots_ok___ = True
    #@override
    eresult = mk_Right(None)
    #@override
    ___666_tribool_skip4serial4LLoo_999___ = True
class RecognizerLLoo__constant_eresult(IRecognizerLLoo__constant_eresult):
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        if sf._t is False:
            return repr_helper(sf, sf._x)
        return repr_helper(sf, sf._x, tribool_skip=sf._t)
    def __init__(sf, eresult, /, *, tribool_skip=False):
        check_type_is(Either, eresult)
        if not tribool_skip is ...:
            check_type_is(bool, tribool_skip)
        sf._x = eresult
        sf._t = tribool_skip
    @property
    @override
    def eresult(sf, /):
        '-> eresult/Either'
        return sf._x
    @property
    @override
    def ___666_tribool_skip4serial4LLoo_999___(sf, /):
        '-> tribool'
        return sf._t
recognizer_LLoo__ignore = RecognizerLLoo__ignore()
recognizer_LLoo__pass = RecognizerLLoo__constant_eresult(RecognizerLLoo__ignore.eresult)
recognizer_LLoo__fail = RecognizerLLoo__constant_eresult(mk_Left('constant_fail'))





class RecognizerLLoo__named_wrapper(_IRecognizerLLoo__wrapper_base__single_ref):
    'named_wrapper'
    def __repr__(sf, /):
        return sf._nm
    def __init__(sf, name, rgnr, /):
        check_pseudo_qual_name(name)
        sf._nm = name
        super().__init__(name, rgnr)
    @property
    @override
    def my_name(sf, /):
        '-> nm/(hashable&&immutable)'
        return sf._nm
check_non_ABC(RecognizerLLoo__named_wrapper)








def __():
    assert 0, (IDependentTreeNode__ref.__mro__, IDependentTreeNode.__mro__, IWrapper.__mro__)

class RecognizerLLoo__ref(_IDependentTreeNode__ref__init, IRecognizerLLoo__wrapper_base, IDependentTreeNode__ref, IDependentTreeNode, IWrapper, _Base4repr):
    'ref'
    '[force:IDependentTreeNode above IWrapper]'

check_non_ABC(RecognizerLLoo__ref)















recognizer_LLoo__ignore
recognizer_LLoo__pass
recognizer_LLoo__fail

def mk_LLoo__skip(rgnr, /, *, to_wrap=False):
    'IRecognizerLLoo -> IRecognizerLLoo'
    return mk_LLoo__with_tribool_skip(True, rgnr, to_wrap=to_wrap)
def mk_LLoo__pack(rgnr, /, *, to_wrap=False):
    'IRecognizerLLoo -> IRecognizerLLoo'
    return mk_LLoo__with_tribool_skip(False, rgnr, to_wrap=to_wrap)
def mk_LLoo__unpack(rgnr, /, *, to_wrap=False):
    'IRecognizerLLoo -> IRecognizerLLoo'
    return mk_LLoo__with_tribool_skip(..., rgnr, to_wrap=to_wrap)
def mk_LLoo__with_tribool_skip(tribool_skip, rgnr, /, *, to_wrap=False):
    'tribool -> IRecognizerLLoo -> IRecognizerLLoo'
    #to_wrap:see:RecognizerLLoo__lazy_wrapper
    check_type_is(bool, to_wrap)
    if not tribool_skip is ...:
        check_type_is(bool, tribool_skip)
    check_type_le(IRecognizerLLoo, rgnr)
    if not to_wrap and tribool_skip is rgnr.___666_tribool_skip4serial4LLoo_999___:
        return rgnr
    #RecognizerLLoo__tribool_skip
    if tribool_skip is False:
        T = RecognizerLLoo__pack
    elif tribool_skip is True:
        T = RecognizerLLoo__skip
    elif tribool_skip is ...:
        T = RecognizerLLoo__unpack
    else:
        raise 000
    assert tribool_skip is T.___666_tribool_skip4serial4LLoo_999___
    return T(rgnr)
def mk_LLoo__with_tribool_skip_as(rgnr8src, rgnr8dst, /, *, to_wrap=False):
    'IRecognizerLLoo -> IRecognizerLLoo -> IRecognizerLLoo'
    #to_wrap:see:RecognizerLLoo__lazy_wrapper
    check_type_is(bool, to_wrap)
    check_type_le(IRecognizerLLoo, rgnr8src)
    check_type_le(IRecognizerLLoo, rgnr8dst)
    if to_wrap:
        #T = RecognizerLLoo__tribool_skip__as
        return RecognizerLLoo__tribool_skip__as(rgnr8src, rgnr8dst)
    tribool_skip = rgnr8src.___666_tribool_skip4serial4LLoo_999___
    return mk_LLoo__with_tribool_skip(tribool_skip, rgnr8dst, to_wrap=to_wrap)


mk_LLoo__with_tribool_skip
mk_LLoo__with_tribool_skip_as
mk_LLoo__skip
mk_LLoo__pack
mk_LLoo__unpack




#.+1,$s/^RecognizerLLoo__\(\w*\)\n    def __init__(sf, \(.*\), \/):$/def mk_LLoo__\1(\2, \/):\r    return RecognizerLLoo__\1(\2)
def mk_LLoo__simple_postprocess(eresult2eresult_, rgnr, /):
    '(Either -> Either) -> IRecognizerLLoo -> IRecognizerLLoo'
    return RecognizerLLoo__wrapper4simple_postprocess(eresult2eresult_, rgnr)
def mk_LLoo__simple_postprocess6ok(oresult2oresult_, rgnr, /):
    '(Reply4IRecognizerLLoo.oresult -> oresult) -> IRecognizerLLoo -> IRecognizerLLoo'
    return RecognizerLLoo__wrapper4simple_postprocess6ok(oresult2oresult_, rgnr)
def mk_LLoo__simple_postprocess6err(errmsg2errmsg_, rgnr, /):
    '(Reply4IRecognizerLLoo.errmsg -> errmsg) -> IRecognizerLLoo -> IRecognizerLLoo'
    return RecognizerLLoo__wrapper4simple_postprocess6err(errmsg2errmsg_, rgnr)


def mk_LLoo__validate_two_phases(rgnr, /):
    'IRecognizerLLoo -> IRecognizerLLoo'
    return RecognizerLLoo__validate_two_phases(rgnr)
def mk_LLoo__skip_header_signal(rgnr, /):
    'IRecognizerLLoo -> IRecognizerLLoo'
    return RecognizerLLoo__skip_header_signal(rgnr)
def mk_LLoo__header_signal_at_beginning(rgnr, /):
    'IRecognizerLLoo -> IRecognizerLLoo'
    return RecognizerLLoo__header_signal_at_beginning(rgnr)
def mk_LLoo__patch_header_signal_if_ok(rgnr, /):
    'IRecognizerLLoo -> IRecognizerLLoo'
    return RecognizerLLoo__patch_header_signal_if_ok(rgnr)

def mk_LLoo__tag(tag, rgnr, /, *, _6oresult_only_=False):
    'tag -> IRecognizerLLoo -> IRecognizerLLoo'
    return RecognizerLLoo__tag(_6oresult_only_, tag, rgnr)
def mk_LLoo__Cased(case, rgnr, /, *, _6oresult_only_=False):
    'case -> IRecognizerLLoo -> IRecognizerLLoo'
    return RecognizerLLoo__Cased(_6oresult_only_, case, rgnr)
def mk_LLoo__invert_err_ok(rgnr, /):
    'IRecognizerLLoo -> IRecognizerLLoo'
    return RecognizerLLoo__invert_err_ok(rgnr)

def mk_LLoo__unbox(rgnr, /):
    'IRecognizerLLoo -> IRecognizerLLoo'
    return RecognizerLLoo__unbox(rgnr)


def mk_LLoo__try__rollback_if_fail_before_hdr_sgnl_else_lift(rgnr, /):
    'IRecognizerLLoo -> IRecognizerLLoo'
    return RecognizerLLoo__try__rollback_if_fail_before_hdr_sgnl_else_lift(rgnr)
def mk_LLoo__optional__either(rgnr, /):
    'IRecognizerLLoo -> IRecognizerLLoo'
    return RecognizerLLoo__optional__either(rgnr)
def mk_LLoo__optional__tmay(rgnr, /):
    'IRecognizerLLoo -> IRecognizerLLoo'
    return RecognizerLLoo__optional__tmay(rgnr)
def mk_LLoo__optional__default(oresult8default, rgnr, /):
    'default/Reply4IRecognizerLLoo.oresult -> IRecognizerLLoo -> IRecognizerLLoo'
    return RecognizerLLoo__optional__default(oresult8default, rgnr)

def mk_LLoo__look_ahead__no_err4hdr(rgnr, /):
    'IRecognizerLLoo -> IRecognizerLLoo'
    return RecognizerLLoo__look_ahead__no_err4hdr(rgnr)
def mk_LLoo__look_ahead__no_err4whole(rgnr, /):
    'IRecognizerLLoo -> IRecognizerLLoo'
    return RecognizerLLoo__look_ahead__no_err4whole(rgnr)
def mk_LLoo__look_ahead4hdr(rgnr, /):
    'IRecognizerLLoo -> IRecognizerLLoo'
    return RecognizerLLoo__look_ahead4hdr(rgnr)
def mk_LLoo__look_ahead4whole(rgnr, /):
    'IRecognizerLLoo -> IRecognizerLLoo'
    return RecognizerLLoo__look_ahead4whole(rgnr)
def mk_LLoo__not_followed_by4hdr(rgnr, /):
    'IRecognizerLLoo -> IRecognizerLLoo'
    return RecognizerLLoo__not_followed_by4hdr(rgnr)
def mk_LLoo__not_followed_by4whole(rgnr, /):
    'IRecognizerLLoo -> IRecognizerLLoo'
    return RecognizerLLoo__not_followed_by4whole(rgnr)



def mk_LLoo__constant_overwrite6ok(oresult, rgnr, /):
    'Reply4IRecognizerLLoo.oresult -> IRecognizerLLoo -> IRecognizerLLoo'
    return RecognizerLLoo__constant_overwrite6ok(oresult, rgnr)
def mk_LLoo__constant_overwrite6err(errmsg, rgnr, /):
    'Reply4IRecognizerLLoo.errmsg -> IRecognizerLLoo -> IRecognizerLLoo'
    return RecognizerLLoo__constant_overwrite6err(errmsg, rgnr)
def mk_LLoo__constant_overwrite(errmsg, oresult, rgnr, /):
    'Reply4IRecognizerLLoo.the_eresult/Either -> IRecognizerLLoo -> IRecognizerLLoo'
    return RecognizerLLoo__constant_overwrite(errmsg, oresult, rgnr)


def mk_LLoo__constant_eresult(eresult, /, *, tribool_skip=False):
    'Reply4IRecognizerLLoo.the_eresult/Either -> IRecognizerLLoo'
    return RecognizerLLoo__constant_eresult(eresult, tribool_skip=tribool_skip)

def mk_LLoo__named_wrapper(name, rgnr, /):
    'name -> IRecognizerLLoo -> IRecognizerLLoo'
    return RecognizerLLoo__named_wrapper(name, rgnr)
def mk_LLoo__ref(scene, kinded_name, /):
    'IScene -> kinded_name/Hashable -> IRecognizerLLoo'
    return RecognizerLLoo__ref(scene, kinded_name)



def mk_LLoo__lazy(lazy_or_rgnr, /, *, non_lazy=False):
    r'lazy_or_rgnr/(IRecognizerLLoo if non_lazy else (()->IRecognizerLLoo)) -> (*,non_lazy/bool) -> IRecognizerLLoo'
    return RecognizerLLoo__lazy_wrapper(lazy_or_rgnr, non_lazy=non_lazy)













__all__
from seed.recognize.recognizer_LLoo_.combinator_LLoo__wrapper import mk_LLoo__skip, mk_LLoo__pack, mk_LLoo__unpack, mk_LLoo__with_tribool_skip, mk_LLoo__with_tribool_skip_as
from seed.recognize.recognizer_LLoo_.combinator_LLoo__wrapper import recognizer_LLoo__pass

from seed.recognize.recognizer_LLoo_.combinator_LLoo__wrapper import \
(recognizer_LLoo__ignore
,recognizer_LLoo__pass
,recognizer_LLoo__fail
,mk_LLoo__with_tribool_skip
,mk_LLoo__with_tribool_skip_as
,mk_LLoo__skip
,mk_LLoo__pack
,mk_LLoo__unpack
#
,mk_LLoo__simple_postprocess
,mk_LLoo__simple_postprocess6ok
,mk_LLoo__simple_postprocess6err
,mk_LLoo__validate_two_phases
,mk_LLoo__skip_header_signal
,mk_LLoo__header_signal_at_beginning
,mk_LLoo__patch_header_signal_if_ok
,mk_LLoo__tag
,mk_LLoo__Cased
,mk_LLoo__invert_err_ok
,mk_LLoo__unbox
,mk_LLoo__try__rollback_if_fail_before_hdr_sgnl_else_lift
,mk_LLoo__optional__either
,mk_LLoo__optional__tmay
,mk_LLoo__optional__default
,mk_LLoo__look_ahead__no_err4hdr
,mk_LLoo__look_ahead__no_err4whole
,mk_LLoo__look_ahead4hdr
,mk_LLoo__look_ahead4whole
,mk_LLoo__not_followed_by4hdr
,mk_LLoo__not_followed_by4whole
,mk_LLoo__constant_overwrite6ok
,mk_LLoo__constant_overwrite6err
,mk_LLoo__constant_overwrite
,mk_LLoo__constant_eresult
,mk_LLoo__named_wrapper
,mk_LLoo__ref
,mk_LLoo__lazy
)

from seed.recognize.recognizer_LLoo_.combinator_LLoo__wrapper import ICallable__using_IDependentTreeNode, Callable__ref, _IDependentTreeNode__ref__init
from seed.recognize.recognizer_LLoo_.combinator_LLoo__wrapper import *
