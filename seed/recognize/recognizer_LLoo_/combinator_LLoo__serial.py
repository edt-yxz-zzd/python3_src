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
mk_LLoo__xtuple
    mk_LLoo__tuple
    mk_LLoo__dependent_tuple



IRecognizerLLoo__flow_framework
    IRecognizerLLoo__serial_framework
        RecognizerLLoo__tuple
        RecognizerLLoo__dependent_tuple
            IMaker4RecognizerLLoo__5ctx

IMaker4RecognizerLLoo__5ctx
    Maker4RecognizerLLoo__5ctx__constant
        rgnr_or2mkr4rgnr7ctx

uhidx4hdr2ichild_ex_ex
uhidx4hdr5shidx4hdr
'''.split()#'''
__all__

___begin_mark_of_excluded_global_names__0___ = ...

from seed.recognize.recognizer_LLoo_._common import (IForkable__stamp
,mk_gi4either8xresult#detach_asif_new_gi_wrapper
,BoxedFinalResult, BoxedHalfwayResult
,Cased, Either, mk_Left, mk_Right
,check_non_ABC
,check_type_is, check_type_le, check_int_ge
,mk_tuple, null_iter
,abstractmethod, override, ABC
,repr_helper, _Base4repr #sf._args4repr = (...)
)
from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import IRecognizerLLoo, Signal__HeaderCompleted, Reply4IRecognizerLLoo, IDependentTreeNode, Error__not_Reply4IRecognizerLLoo_after_Signal__HeaderCompleted
from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import mk_gi4patch_header_signal_if_ok

from seed.tiny_.check import check_int_ge_lt, check_callable, check_subscriptable
from seed.types.view.View import SeqView

from seed.recognize.recognizer_LLoo_.IMaker4RecognizerLLoo import IMaker4RecognizerLLoo__5args_ex, IMaker4RecognizerLLoo__5args

___end_mark_of_excluded_global_names__0___ = ...


class IRecognizerLLoo__flow_framework(IRecognizerLLoo):
    'flow_framework#assume[inputter contains global runtime info...]'
    __slots__ = ()
    @abstractmethod
    def _initialize_state_context4flow4LLoo_(sf, inputter4whole, /):
        'inputter4whole.fork() -> (state4flow, ctx)' ' #assume[inputter contains global runtime info...]'
    @abstractmethod
    def _next_child_item_ex4flow4LLoo_(sf, state4flow, ctx, /):
        'state4flow -> ctx -> (child_item, ctx) | ^StopIteration'
    @abstractmethod
    def _is_stopped4flow4LLoo_(sf, state4flow, ctx, inputter, /):
        'state4flow -> ctx -> inputter.fork() -> stopped/bool' ' #assume[inputter contains global runtime info...]'
    @abstractmethod
    def _mk_child_recognizer_ex4flow4LLoo_(sf, state4flow, ctx, child_item, inputter, /):
        'state4flow -> ctx -> child_item -> inputter.fork() -> (child_rgnr/IRecognizerLLoo, ctx)' ' #assume[inputter contains global runtime info...]'
    @abstractmethod
    def _update_state_context4flow4LLoo_(sf, state4flow, child_item, child_rgnr, ctx, result6ok4child, inputter, /):
        'state4flow -> child_item -> child_rgnr -> ctx -> result6ok4child -> inputter.fork() -> (state4flow, ctx)' ' #assume[inputter contains global runtime info...]'
    @abstractmethod
    def _finalize_oresult4flow4LLoo_(sf, state4flow, ctx, inputter, /):
        'state4flow -> ctx -> inputter.fork() -> result6ok4whole_LLoo' ' #assume[inputter contains global runtime info...]'

    ######################
    #see:mv-from:IRecognizerLLoo__serial_framework
    ######################
    @abstractmethod
    def _mk_may_header_signal_at_child_beginning_(sf, child_item, child_rgnr, ctx, consumed0, inputter, /):
        '-> may Signal__HeaderCompleted'
    @abstractmethod
    def _mk_may_header_signal5header_signal_(sf, child_item, child_rgnr, ctx, consumed0, consumed, hdr_sgnl, /):
        '-> may Signal__HeaderCompleted'
    @abstractmethod
    def _mk_may_header_signal5ok_reply_(sf, child_item, child_rgnr, reply4LLoo, consumed0, consumed, ctx, /):
        '-> may Signal__HeaderCompleted'

    @override
    def _iter4two_phases_recognize_(sf, inputter4whole, /):
        ######################
        if 0:
            #child_items = sf._iter_child_items4serial4LLoo_()
            #if not child_items is iter(child_items):raise TypeError
            #ctx = sf._initialize_context4serial4LLoo_(inputter4whole.fork())
            pass
        else:
            (state4flow, ctx) = sf._initialize_state_context4flow4LLoo_(inputter4whole.fork())
        ctx
        ######################
        hdr_sgnl_occured = False
        inputter = inputter4whole
        del inputter4whole
        stamp0 = inputter.get_stamp()
        #consumed = False
        def f(may_hdr_sgnl, /):
            nonlocal f, hdr_sgnl_occured
            ######################
            assert not hdr_sgnl_occured
            if not None is may_hdr_sgnl:
                hdr_sgnl = may_hdr_sgnl
                yield BoxedHalfwayResult(hdr_sgnl)
                hdr_sgnl_occured = True
                f = None
            ######################
        #end-def f(may_hdr_sgnl, /):

        ######################
        ######################
        ######################
        #while not sf._is_stopped4serial4LLoo_(ctx, inputter.fork()):
        while not sf._is_stopped4flow4LLoo_(state4flow, ctx, inputter.fork()):
            #assert not inputter is None
            ######################
            if 0:
                #for child_item in child_items:
                #    #head
                #    break
                #else:
                #    break
                pass
            else:
                try:
                    (child_item, ctx) = sf._next_child_item_ex4flow4LLoo_(state4flow, ctx)
                except StopIteration:
                    break
            child_item
            ######################
            consumed0 = inputter.has_changed_since_stamp_(stamp0)
                #changed
            stamp = inputter.get_stamp()
            ######################
            #(child_rgnr, ctx) = sf._mk_child_recognizer_ex4serial4LLoo_(ctx, child_item, inputter.fork())
            (child_rgnr, ctx) = sf._mk_child_recognizer_ex4flow4LLoo_(state4flow, ctx, child_item, inputter.fork())
            check_type_le(IRecognizerLLoo, child_rgnr)
            ######################
            if not hdr_sgnl_occured:
                may_hdr_sgnl = sf._mk_may_header_signal_at_child_beginning_(child_item, child_rgnr, ctx, consumed0, inputter.fork())
                yield from f(may_hdr_sgnl)
                del may_hdr_sgnl
            ######################
            gi = child_rgnr.iter4two_phases_recognize(inputter)
            del inputter
            if not hdr_sgnl_occured:
                gi = mk_gi4patch_header_signal_if_ok(gi)
            gi = mk_gi4either8xresult(gi)
                #neednot:detach_asif_new_gi_wrapper
            x = yield gi
            if x.is_left:
                hdr_sgnl, gi = x.left
                del x
                check_type_is(Signal__HeaderCompleted, hdr_sgnl)
                ######################
                if not hdr_sgnl_occured:
                    ######################
                    inputter = hdr_sgnl.the_inputter4body
                    consumed0 = inputter.has_changed_since_stamp_(stamp0)
                    consumed = inputter.has_changed_since_stamp_(stamp)
                    stamp#unchanged
                    del inputter
                    ######################
                    may_hdr_sgnl = sf._mk_may_header_signal5header_signal_(child_item, child_rgnr, ctx, consumed0, consumed, hdr_sgnl)
                    del hdr_sgnl
                    yield from f(may_hdr_sgnl)
                    del may_hdr_sgnl
                ######################
                else:
                    del hdr_sgnl
                y = yield gi
                if not y.is_right:
                    raise Error__not_Reply4IRecognizerLLoo_after_Signal__HeaderCompleted
                x = y
                del y
            assert x.is_right
            reply4LLoo = x.right
            check_type_is(Reply4IRecognizerLLoo, reply4LLoo)
            if not reply4LLoo.ok:
                return BoxedFinalResult(reply4LLoo)
            inputter = reply4LLoo.the_inputter4end
            result6ok4child = reply4LLoo.oresult
            ######################
            #ctx = sf._update_context4serial4LLoo_(child_item, child_rgnr, ctx, result6ok4child, inputter.fork())
            (_state4flow, ctx) = sf._update_state_context4flow4LLoo_(state4flow, child_item, child_rgnr, ctx, result6ok4child, inputter.fork())
            ######################
            if not hdr_sgnl_occured:
                ######################
                consumed0 = inputter.has_changed_since_stamp_(stamp0)
                consumed = inputter.has_changed_since_stamp_(stamp)
                stamp#unchanged
                ######################
                may_hdr_sgnl = sf._mk_may_header_signal5ok_reply_(child_item, child_rgnr, reply4LLoo, consumed0, consumed, ctx)
                del reply4LLoo
                yield from f(may_hdr_sgnl)
                del may_hdr_sgnl
            ######################
            #next round:
            inputter
            state4flow = _state4flow
            del _state4flow
            ######################
        #end-while
        ######################
        ######################
        ######################

        #result6ok4whole_LLoo = sf._finalize_oresult4serial4LLoo_(ctx, inputter.fork())
        result6ok4whole_LLoo = sf._finalize_oresult4flow4LLoo_(state4flow, ctx, inputter.fork())
        reply4whole_LLoo = Reply4IRecognizerLLoo(inputter, mk_Right(result6ok4whole_LLoo))
        return BoxedFinalResult(reply4whole_LLoo)
IRecognizerLLoo__flow_framework
#end-class IRecognizerLLoo__flow_framework


class IRecognizerLLoo__serial_framework(IRecognizerLLoo__flow_framework):
    'serial_framework#assume[inputter contains global runtime info...]'
    __slots__ = ()
    @abstractmethod
    def _iter_child_items4serial4LLoo_(sf, /):
        '-> Iter child_item'
    @abstractmethod
    def _initialize_context4serial4LLoo_(sf, inputter4whole, /):
        'inputter4whole.fork() -> ctx' ' #assume[inputter contains global runtime info...]'
    @abstractmethod
    def _is_stopped4serial4LLoo_(sf, ctx, inputter, /):
        'ctx -> inputter.fork() -> stopped/bool' ' #assume[inputter contains global runtime info...]'
    @abstractmethod
    def _mk_child_recognizer_ex4serial4LLoo_(sf, ctx, child_item, inputter, /):
        'ctx -> child_item -> inputter.fork() -> (child_rgnr/IRecognizerLLoo, ctx)' ' #assume[inputter contains global runtime info...]'
    @abstractmethod
    def _update_context4serial4LLoo_(sf, child_item, child_rgnr, ctx, result6ok4child, inputter, /):
        'child_item -> child_rgnr -> ctx -> result6ok4child -> inputter.fork() -> ctx' ' #assume[inputter contains global runtime info...]'
    @abstractmethod
    def _finalize_oresult4serial4LLoo_(sf, ctx, inputter, /):
        'ctx -> inputter.fork() -> result6ok4whole_LLoo' ' #assume[inputter contains global runtime info...]'

    ######################
    #see:override:IRecognizerLLoo__flow_framework
    ######################
    @override
    def _initialize_state_context4flow4LLoo_(sf, inputter4whole, /):
        'inputter4whole.fork() -> (state4flow, ctx)' ' #assume[inputter contains global runtime info...]'
        child_items = sf._iter_child_items4serial4LLoo_()
        if not child_items is iter(child_items):raise TypeError
        state4flow = child_items
        ctx = sf._initialize_context4serial4LLoo_(inputter4whole)   #.fork()
        return (state4flow, ctx)
    @override
    def _next_child_item_ex4flow4LLoo_(sf, state4flow, ctx, /):
        'state4flow -> ctx -> (child_item, ctx) | ^StopIteration'
        child_items = state4flow
        child_item = next(child_items)
            # ^StopIteration
        return (child_item, ctx)
    @override
    def _is_stopped4flow4LLoo_(sf, state4flow, ctx, inputter, /):
        'state4flow -> ctx -> inputter.fork() -> stopped/bool' ' #assume[inputter contains global runtime info...]'
        return sf._is_stopped4serial4LLoo_(ctx, inputter)  #.fork()
    @override
    def _mk_child_recognizer_ex4flow4LLoo_(sf, state4flow, ctx, child_item, inputter, /):
        'state4flow -> ctx -> child_item -> inputter.fork() -> (child_rgnr/IRecognizerLLoo, ctx)' ' #assume[inputter contains global runtime info...]'
        (child_rgnr, ctx) = sf._mk_child_recognizer_ex4serial4LLoo_(ctx, child_item, inputter)  #.fork()
        return (child_rgnr, ctx)
    @override
    def _update_state_context4flow4LLoo_(sf, state4flow, child_item, child_rgnr, ctx, result6ok4child, inputter, /):
        'state4flow -> child_item -> child_rgnr -> ctx -> result6ok4child -> inputter.fork() -> (state4flow, ctx)' ' #assume[inputter contains global runtime info...]'
        ctx = sf._update_context4serial4LLoo_(child_item, child_rgnr, ctx, result6ok4child, inputter)  #.fork()
        return (state4flow, ctx)
    @override
    def _finalize_oresult4flow4LLoo_(sf, state4flow, ctx, inputter, /):
        'state4flow -> ctx -> inputter.fork() -> result6ok4whole_LLoo' ' #assume[inputter contains global runtime info...]'
        result6ok4whole_LLoo = sf._finalize_oresult4serial4LLoo_(ctx, inputter)   #.fork()
        return result6ok4whole_LLoo
IRecognizerLLoo__serial_framework
#end-class IRecognizerLLoo__serial_framework
























def uhidx4hdr2ichild_ex_ex(L, uhidx4hdr, /):
    'L/num_children -> uhidx4hdr -> (ichild_ex/uint%(num_children+1), begin_vs_middle/bool)'
    M = 2*L+1
    check_int_ge_lt(0, M, uhidx4hdr)
    ichild_ex = uhidx4hdr >> 1
    begin_vs_middle = bool(uhidx4hdr&1)
    return (ichild_ex, begin_vs_middle)

def uhidx4hdr5shidx4hdr(L, shidx4hdr, /):
    'L/num_children -> shidx4hdr -> uhidx4hdr'
    M = 2*L+1
    check_int_ge_lt(-M, M, shidx4hdr)
    uhidx4hdr = shidx4hdr + M if shidx4hdr < 0 else shidx4hdr
    return uhidx4hdr


class _IRecognizerLLoo__base_tuple(IRecognizerLLoo__serial_framework, _Base4repr):
    r'''[[[
    [rgnrs :: [IRecognizerLLoo]]
    [L := len(rgnrs)]
    [uhidx4hdr :: uint]
        #unsigned half index for header Signal__HeaderCompleted
        [0 <= uhidx4hdr < (2*L+1)]
    [shidx4hdr :: int]
        #signed half index for header Signal__HeaderCompleted
        [-(2*L+1) <= shidx4hdr < (2*L+1)]
    [_update_context4serial4LLoo_():using:rgnr.iter4unpack_oresult4serial4LLoo()#___666_tribool_skip4serial4LLoo_999___/(False-append|True-skip|...-extend)]

    #]]]'''#'''
    ___no_slots_ok___ = True
    @classmethod
    @abstractmethod
    def _basetype4child_arg_(cls, /):pass
    @classmethod
    def from_two_groups(cls, rgnrs4hdr, rgnrs4body, /):
        '[shidx4hdr = max(0, 2*len(rgnrs4hdr) -1)]'
        rgnrs4hdr = mk_tuple(rgnrs4hdr)
        rgnrs4body = mk_tuple(rgnrs4body)
        shidx4hdr = max(0, 2*len(rgnrs4hdr) -1)
        rgnrs = rgnrs4hdr + rgnrs4body
        return cls(shidx4hdr, rgnrs)
    def __init__(sf, shidx4hdr, rgnrs, /):
        rgnrs = mk_tuple(rgnrs)
        T = type(sf)._basetype4child_arg_
        for rgnr in rgnrs:
            check_type_le(T, rgnr)

        L = len(rgnrs)
        uhidx4hdr = uhidx4hdr5shidx4hdr(L, shidx4hdr)
            #^TypeError
        (ichild_ex, begin_vs_middle) = uhidx4hdr2ichild_ex_ex(L, uhidx4hdr)
        sf._ich = ichild_ex
        sf._bm = begin_vs_middle
        sf._rs = rgnrs
        #_Base4repr.__init__(sf, shidx4hdr, rgnrs)
        sf._args4repr = (shidx4hdr, rgnrs)

    def _view_ctx_(sf, ctx, /):
        'ctx -> ctx_view'
        return SeqView(ctx)
    @property
    def _rgnrs_(sf, /):
        '-> [IRecognizerLLoo|IMaker4RecognizerLLoo__5ctx]'
        rgnrs = sf._rs
        return rgnrs

    #@property
    #@override
    ___666_tribool_skip4serial4LLoo_999___ = False # False-append;True-skip;...-extend

    @override
    def _iter_child_items4serial4LLoo_(sf, /):
        '-> Iter child_item'
        rgnrs = sf._rgnrs_
        return iter(enumerate(rgnrs))
    @override
    def _initialize_context4serial4LLoo_(sf, inputter4whole, /):
        'inputter4whole.fork() -> ctx' ' #assume[inputter contains global runtime info...]'
        return []
    @override
    def _is_stopped4serial4LLoo_(sf, ctx, inputter, /):
        'ctx -> inputter.fork() -> stopped/bool' ' #assume[inputter contains global runtime info...]'
        return False
    #def _mk_child_recognizer_ex4serial4LLoo_(sf, ctx, child_item, inputter, /):

    @override
    def _update_context4serial4LLoo_(sf, child_item, child_rgnr, ctx, result6ok4child, inputter, /):
        'child_item -> child_rgnr -> ctx -> result6ok4child -> inputter.fork() -> ctx' ' #assume[inputter contains global runtime info...]'
        #[using:rgnr.iter4unpack_oresult4serial4LLoo()#___666_tribool_skip4serial4LLoo_999___/(False-append|True-skip|...-extend)]
        it = child_rgnr.iter4unpack_oresult4serial4LLoo(result6ok4child)
        ls = ctx
        ls.extend(it)
        return ctx
    @override
    def _finalize_oresult4serial4LLoo_(sf, ctx, inputter, /):
        'ctx -> inputter.fork() -> result6ok4whole_LLoo' ' #assume[inputter contains global runtime info...]'
        return tuple(ctx)
    @override
    def _mk_may_header_signal_at_child_beginning_(sf, child_item, child_rgnr, ctx, consumed0, inputter, /):
        '-> may Signal__HeaderCompleted'
        return sf.__mk_may_hdr_sgnl(not sf._bm, child_item, ctx, inputter)
    @override
    def _mk_may_header_signal5header_signal_(sf, child_item, child_rgnr, ctx, consumed0, consumed, hdr_sgnl, /):
        '-> may Signal__HeaderCompleted'
        return sf.__mk_may_hdr_sgnl(sf._bm, child_item, ctx, hdr_sgnl.the_inputter4body)
    @override
    def _mk_may_header_signal5ok_reply_(sf, child_item, child_rgnr, reply4LLoo, consumed0, consumed, ctx, /):
        '-> may Signal__HeaderCompleted'
        return None
    def __mk_may_hdr_sgnl(sf, b, child_item, ctx, inputter, /):
        may_hdr_sgnl = None
        if b:
            ichild, _ = child_item
            if ichild == sf._ich:
                hdr_sgnl = Signal__HeaderCompleted(inputter, sf._view_ctx_(ctx))
                may_hdr_sgnl = hdr_sgnl
        return may_hdr_sgnl

    @override
    def _iter_directly_used_kinded_names_(sf, /):
        '-> Iter knm/kinded_name'
        return null_iter
    @override
    def _iter_direct_child_dependent_tree_nodes_(sf, /):
        '-> Iter IDependentTreeNode'
        rgnrs = sf._rgnrs_
        return iter(rgnrs)

class RecognizerLLoo__tuple(_IRecognizerLLoo__base_tuple):
    r'''[[[
    [rgnrs :: [IRecognizerLLoo]]
    [L := len(rgnrs)]
    [uhidx4hdr :: uint]
        #unsigned half index for header Signal__HeaderCompleted
        [0 <= uhidx4hdr < (2*L+1)]
    [shidx4hdr :: int]
        #signed half index for header Signal__HeaderCompleted
        [-(2*L+1) <= shidx4hdr < (2*L+1)]
    [_update_context4serial4LLoo_():using:rgnr.iter4unpack_oresult4serial4LLoo()#___666_tribool_skip4serial4LLoo_999___/(False-append|True-skip|...-extend)]

    #]]]'''#'''
    ___no_slots_ok___ = True
    def __init__(sf, shidx4hdr, rgnrs, /):
        super().__init__(shidx4hdr, rgnrs)
    #@override
    _basetype4child_arg_ = IRecognizerLLoo
    @classmethod
    @override
    def from_two_groups(cls, rgnrs4hdr, rgnrs4body, /):
        '[shidx4hdr = max(0, 2*len(rgnrs4hdr) -1)]'
        return super().from_two_groups(rgnrs4hdr, rgnrs4body)
    @override
    def _mk_child_recognizer_ex4serial4LLoo_(sf, ctx, child_item, inputter, /):
        'ctx -> child_item -> inputter.fork() -> (child_rgnr/IRecognizerLLoo, ctx)' ' #assume[inputter contains global runtime info...]'
        (ichild, child_rgnr) = child_item
        return (child_rgnr, ctx)
check_non_ABC(RecognizerLLoo__tuple)




class IMaker4RecognizerLLoo__5ctx(IMaker4RecognizerLLoo__5args_ex):
    #class IMaker4RecognizerLLoo__5ctx(IDependentTreeNode):
    'context:ctx_view/[#see:serial_framework#]'
    __slots__ = ()
    @abstractmethod
    def _mk_recognizer_LLoo5ctx_(sf, ctx_view, inputter, /):
        'ctx_view/[#see:serial_framework#] -> inputter.fork() -> IRecognizerLLoo'
    def mk_recognizer_LLoo5ctx(sf, ctx_view, inputter, /):
        'ctx_view/[#see:serial_framework#] -> inputter.fork() -> IRecognizerLLoo'
        check_type_le(IForkable__stamp, inputter)
        rgnr = sf._mk_recognizer_LLoo5ctx_(ctx_view, inputter.fork())
        check_type_le(IRecognizerLLoo, rgnr)
        return rgnr


    #@override
    num_args4mkr4LLoo = 1

    @override
    def _mk_recognizer_LLoo5args_ex_(sf, inputter, /, *args):
        'inputter.fork() -> (*args){len=.num_args4mkr4LLoo} -> IRecognizerLLoo' ' #assume[inputter contains global runtime info...]'
        rgnr = sf._mk_recognizer_LLoo5ctx_(*args, inputter) #.fork()
        return rgnr
IMaker4RecognizerLLoo__5ctx

class RecognizerLLoo__dependent_tuple(_IRecognizerLLoo__base_tuple):
    r'''[[[
    [mkrs :: [IMaker4RecognizerLLoo__5ctx]]
    [L := len(mkrs)]
    [uhidx4hdr :: uint]
        #unsigned half index for header Signal__HeaderCompleted
        [0 <= uhidx4hdr < (2*L+1)]
    [shidx4hdr :: int]
        #signed half index for header Signal__HeaderCompleted
        [-(2*L+1) <= shidx4hdr < (2*L+1)]
    [_update_context4serial4LLoo_():using:rgnr.iter4unpack_oresult4serial4LLoo()#___666_tribool_skip4serial4LLoo_999___/(False-append|True-skip|...-extend)]

    #]]]'''#'''
    ___no_slots_ok___ = True
    #def __init__(sf, shidx4hdr, mkrs, /):
    #    super().__init__(shidx4hdr, mkrs)
    def __init__(sf, shidx4hdr, ls4rgnrXmkr, /):
        ls4rgnrXmkr = mk_tuple(ls4rgnrXmkr)
        mkrs = mk_tuple(map(rgnr_or2mkr4rgnr7ctx, ls4rgnrXmkr))
        super().__init__(shidx4hdr, mkrs)
        #_Base4repr
        sf._args4repr = (shidx4hdr, ls4rgnrXmkr)
    #@override
    _basetype4child_arg_ = IMaker4RecognizerLLoo__5ctx
    @classmethod
    @override
    #def from_two_groups(cls, mkrs4hdr, mkrs4body, /):
    def from_two_groups(cls, ls4rgnrXmkr4hdr, ls4rgnrXmkr4body, /):
        '[shidx4hdr = max(0, 2*len(mkrs4hdr) -1)]'
        return super().from_two_groups(ls4rgnrXmkr4hdr, ls4rgnrXmkr4body)
        mkrs4hdr = mk_tuple(map(rgnr_or2mkr4rgnr7ctx, ls4rgnrXmkr4hdr))
        mkrs4body = mk_tuple(map(rgnr_or2mkr4rgnr7ctx, ls4rgnrXmkr4body))
        return super().from_two_groups(mkrs4hdr, mkrs4body)
    @override
    def _mk_child_recognizer_ex4serial4LLoo_(sf, ctx, child_item, inputter, /):
        'ctx -> child_item -> inputter.fork() -> (child_rgnr/IRecognizerLLoo, ctx)' ' #assume[inputter contains global runtime info...]'
        (ichild, child_mkr) = child_item
        ctx_view = sf._view_ctx_(ctx)
        child_rgnr = child_mkr.mk_recognizer_LLoo5ctx(ctx_view, inputter.fork())
        return (child_rgnr, ctx)

check_non_ABC(RecognizerLLoo__dependent_tuple)








def mk_LLoo__xtuple(shidx4hdr__or__xs4hdr, xs4whole__or__xs4body, /, *, dependent):
    '(int{-(1+2*L)<=.<(1+2*L)}|[x]) -> [x]{len==L} -> IRecognizerLLoo # [x :: ((IRecognizerLLoo|IMaker4RecognizerLLoo__5ctx) if dependent else IRecognizerLLoo)]'#(RecognizerLLoo__dependent_tuple|RecognizerLLoo__tuple)
    T = RecognizerLLoo__dependent_tuple if dependent else RecognizerLLoo__tuple
    if type(shidx4hdr__or__xs4hdr) is int:
        shidx4hdr = shidx4hdr__or__xs4hdr
        xs4whole = xs4whole__or__xs4body
        sf = T(shidx4hdr, xs4whole)
    else:
        xs4hdr = shidx4hdr__or__xs4hdr
        xs4body = xs4whole__or__xs4body
        sf = T.from_two_groups(xs4hdr, xs4body)
    sf
    return sf


def mk_LLoo__tuple(shidx4hdr__or__rgnrs4hdr, rgnrs4whole__or__rgnrs4body, /):
    '(int{-(1+2*L)<=.<(1+2*L)}|[IRecognizerLLoo]) -> [IRecognizerLLoo]{len==L} -> IRecognizerLLoo'#RecognizerLLoo__tuple
    '-> IRecognizerLLoo/RecognizerLLoo__tuple'
    return mk_LLoo__xtuple(shidx4hdr__or__rgnrs4hdr, rgnrs4whole__or__rgnrs4body, dependent=False)
def mk_LLoo__dependent_tuple(shidx4hdr__or__mkrs4hdr, mkrs4whole__or__mkrs4body, /):
    '(int{-(1+2*L)<=.<(1+2*L)}|[(IRecognizerLLoo|IMaker4RecognizerLLoo__5ctx)]) -> [(IRecognizerLLoo|IMaker4RecognizerLLoo__5ctx)]{len==L} -> IRecognizerLLoo'#RecognizerLLoo__dependent_tuple
    '-> IRecognizerLLoo/RecognizerLLoo__dependent_tuple'
    return mk_LLoo__xtuple(shidx4hdr__or__mkrs4hdr, mkrs4whole__or__mkrs4body, dependent=True)






class Maker4RecognizerLLoo__5ctx__constant(IMaker4RecognizerLLoo__5ctx, _Base4repr):
    ___no_slots_ok___ = True
    def __init__(sf, rgnr, /):
        check_type_le(IRecognizerLLoo, rgnr)
        sf._r = rgnr
        #_Base4repr.__init__(sf, rgnr)
        sf._args4repr = (rgnr,)
    @override
    def _mk_recognizer_LLoo5ctx_(sf, ctx_view, inputter, /):
        'ctx_view/[#see:serial_framework#] -> inputter.fork() -> IRecognizerLLoo'
        return sf._r
    @override
    def _iter_directly_used_kinded_names_(sf, /):
        '-> Iter knm/kinded_name'
        return null_iter
    @override
    def _iter_direct_child_dependent_tree_nodes_(sf, /):
        '-> Iter IDependentTreeNode'
        rgnr = sf._r
        yield rgnr
        return

check_non_ABC(Maker4RecognizerLLoo__5ctx__constant)

def rgnr_or2mkr4rgnr7ctx(rgnr_or_mkr4rgnr7ctx, /):
    '(IRecognizerLLoo|IMaker4RecognizerLLoo__5ctx) -> IMaker4RecognizerLLoo__5ctx'
    if isinstance(IRecognizerLLoo, rgnr_or_mkr4rgnr7ctx):
        rgnr = rgnr_or_mkr4rgnr7ctx
        mkr4rgnr7ctx = Maker4RecognizerLLoo__5ctx__constant(rgnr)
    else:
        mkr4rgnr7ctx = rgnr_or_mkr4rgnr7ctx
    mkr4rgnr7ctx
    check_type_le(IMaker4RecognizerLLoo__5ctx, mkr4rgnr7ctx)
    return mkr4rgnr7ctx


__all__
from seed.recognize.recognizer_LLoo_.combinator_LLoo__serial import IMaker4RecognizerLLoo__5ctx, rgnr_or2mkr4rgnr7ctx, Maker4RecognizerLLoo__5ctx__constant

from seed.recognize.recognizer_LLoo_.combinator_LLoo__serial import mk_LLoo__xtuple, mk_LLoo__tuple, mk_LLoo__dependent_tuple

from seed.recognize.recognizer_LLoo_.combinator_LLoo__serial import *
