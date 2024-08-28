#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/recognizer_LLoo_/combinator_LLoo__loop.py

seed.recognize.recognizer_LLoo_.combinator_LLoo__loop
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_LLoo_.combinator_LLoo__loop -x
py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LLoo_.combinator_LLoo__loop:__doc__ -ht
#]]]'''
__all__ = r'''
RecognizerLLoo__base_loop
RecognizerLLoo__many
RecognizerLLoo__skip_many1
RecognizerLLoo__end_by__pre
RecognizerLLoo__end_by__post
RecognizerLLoo__sep_by
RecognizerLLoo__between


mk_LLoo__base_loop
mk_LLoo__many
mk_LLoo__skip_many1
mk_LLoo__end_by__pre
mk_LLoo__end_by__post
mk_LLoo__sep_by
mk_LLoo__between




uhidx4hdr5may__
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...

from seed.recognize.recognizer_LLoo_._common import (IForkable__stamp
#mk#gi4either8xresult
,BoxedFinalResult, BoxedHalfwayResult
#,Cased, Either, mk_Left, mk_Right
,check_non_ABC
,check_type_is, check_type_le, check_int_ge
,mk_tuple, null_iter, null_tuple
,abstractmethod, override, ABC
,repr_helper, _Base4repr #sf._args4repr = (...)
)
from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import IRecognizerLLoo, Signal__HeaderCompleted, Reply4IRecognizerLLoo, IDependentTreeNode

from seed.tiny_.check import check_int_ge_lt, check_may_
from seed.tiny import echo

from seed.recognize.recognizer_LLoo_.combinator_LLoo__serial import IRecognizerLLoo__serial_framework, RecognizerLLoo__tuple
from seed.recognize.recognizer_LLoo_.combinator_LLoo__wrapper import RecognizerLLoo__tag, recognizer_LLoo__ignore, RecognizerLLoo__unbox
from seed.recognize.recognizer_LLoo_.combinator_LLoo__wrapper import _IRecognizerLLoo__wrapper_base__single_ref# IRecognizerLLoo__wrapper_base

from seed.recognize.recognizer_LLoo_.combinator_LLoo__wrapper import mk_LLoo__skip, mk_LLoo__pack, mk_LLoo__unpack, mk_LLoo__with_tribool_skip_as#, mk_LLoo__with_tribool_skip, RecognizerLLoo__skip, RecognizerLLoo__unpack, RecognizerLLoo__pack
from seed.recognize.recognizer_LLoo_.combinator_LLoo__wrapper import mk_LLoo__optional__default, mk_LLoo__optional__tmay

from seed.recognize.recognizer_LLoo_.combinator_LLoo__parallel import RecognizerLLoo__the_first_one
from seed.types.view.View import SeqView

from itertools import count as count_
___end_mark_of_excluded_global_names__0___ = ...




class _IRecognizerLLoo__base_loop(IRecognizerLLoo__serial_framework, _Base4repr):
    r'''[[[
    [rgnrs :: [IRecognizerLLoo]]
    [uhidx4hdr :: uint]
        #unsigned half index for header Signal__HeaderCompleted
        [0 <= uhidx4hdr < (1+2*(1+max_loops))]
    [_update_context4serial4LLoo_():using:rgnr.iter4unpack_oresult4serial4LLoo()#___666_tribool_skip4serial4LLoo_999___/(False-append|True-skip|...-extend)]

    #]]]'''#'''
    ___no_slots_ok___ = True
    #@property
    #@override
    ___666_tribool_skip4serial4LLoo_999___ = False # False-append;True-skip;...-extend
    def __init__(sf, to_output_num_loops, min_loops, imay_max_loops, uhidx4hdr, may_rgnr4end7pre, rgnr4body4loop, may_rgnr4end7post, /):
        check_type_is(bool, to_output_num_loops)
        check_int_ge(0, min_loops)
        check_int_ge(-1, imay_max_loops)
        check_int_ge(0, uhidx4hdr)
        if not imay_max_loops == -1:
            max_loops = imay_max_loops
            check_int_ge(min_loops, max_loops)
            check_int_ge_lt(0, 3+2*max_loops, uhidx4hdr)

        check_type_le(IRecognizerLLoo, rgnr4body4loop)
        check_may_([check_type_le, IRecognizerLLoo], may_rgnr4end7pre)
        check_may_([check_type_le, IRecognizerLLoo], may_rgnr4end7post)

        may_raw_rgnrs = (may_rgnr4end7pre, rgnr4body4loop, may_rgnr4end7post)
        ms = [*may_raw_rgnrs]
        if ms[-1] is None:
            ms[-1] = recognizer_LLoo__ignore
        assert len(ms) == 3
        _rgnrs = [RecognizerLLoo__tag(_6oresult_only_:=True, ibranch, may_rgnr) for ibranch, may_rgnr in enumerate(ms) if not None is may_rgnr]
            #may remove may_rgnr4end7pre
        rgnrs = mk_tuple(_rgnrs)
        assert 2 <= len(rgnrs) <= 3
        rgnr4round = RecognizerLLoo__the_first_one(rgnrs)

        #xxx:assert _rgnrs[-2] is rgnr4body4loop
        assert _rgnrs[-2].tag == 1
        del _rgnrs[-2]
            # del rgnr4body4loop
        _rgnrs = mk_tuple(_rgnrs)
        assert 1 <= len(_rgnrs) <= 2
        assert not any(rgnr.tag == 1 for rgnr in _rgnrs)
        rgnr4end6max = RecognizerLLoo__the_first_one(_rgnrs) if len(_rgnrs) == 2 else echo(*_rgnrs)


        args = (to_output_num_loops, min_loops, imay_max_loops, uhidx4hdr, may_rgnr4end7pre, rgnr4body4loop, may_rgnr4end7post)
        sf._ms = may_raw_rgnrs
        sf._rs = rgnrs
        sf._r4r = rgnr4round
        sf._r4e = rgnr4end6max
        sf._ich = ichild_ex = uhidx4hdr>>1
        sf._bm = begin_vs_middle = bool(uhidx4hdr&1)
        sf._args4bloop = args
        sf._args4repr = args
    @property
    def to_output_num_loops(sf, /):
        return sf._args4bloop[0]
    @property
    def min_loops(sf, /):
        return sf._args4bloop[1]
    @property
    def imay_max_loops(sf, /):
        return sf._args4bloop[2]
    @property
    def uhidx4hdr(sf, /):
        return sf._args4bloop[3]
    @property
    def may_rgnr4end7pre(sf, /):
        return sf._args4bloop[4]
    @property
    def rgnr4body4loop(sf, /):
        return sf._args4bloop[5]
    @property
    def may_rgnr4end7post(sf, /):
        return sf._args4bloop[6]


    def _view_ctx_(sf, ctx, /):
        'ctx -> ctx_view'
        (num_rounds, stopped, ls) = ctx
        ctx_view = (num_rounds, stopped, SeqView(ls))
        return ctx_view
    @property
    def _may_raw_rgnrs_(sf, /):
        '-> [may IRecognizerLLoo]'
        may_raw_rgnrs = sf._ms
        return may_raw_rgnrs
    @property
    def _rgnrs_(sf, /):
        '-> [RecognizerLLoo__tag]/[IRecognizerLLoo]'
        rgnrs = sf._rs
        return rgnrs
    @property
    def _rgnr4round_(sf, /):
        '-> IRecognizerLLoo'
        rgnr4round = sf._r4r
        return rgnr4round
    @property
    def _rgnr4end6max_(sf, /):
        '-> IRecognizerLLoo'
        rgnr4end6max = sf._r4e
        return rgnr4end6max
    @property
    def _tagged_rgnr4body4loop_(sf, /):
        rgnr = sf._rgnrs_[-2]
        assert rgnr.tag == 1
        return rgnr

    @override
    def _iter_child_items4serial4LLoo_(sf, /):
        '-> Iter child_item'
        # (body_vs_round_vs_end, ichild, child_rgnr) = child_item
        ######################
        #rgnr4body4loop = sf.rgnr4body4loop
        tagged_rgnr4body4loop = sf._tagged_rgnr4body4loop_
        min_loops = sf.min_loops
        for ichild in range(min_loops):
            yield (False, ichild, tagged_rgnr4body4loop)
        ######################
        rgnr4round = sf._rgnr4round_
        if sf.imay_max_loops == -1:
            js = count_(min_loops)
        else:
            max_loops = sf.imay_max_loops
            js = range(min_loops, 1+max_loops)
        js
        for ichild in js:
            yield (..., ichild, rgnr4round)
        ######################
        rgnr4end6max = sf._rgnr4end6max_
        if 1:
            yield (True, ichild:=1+max_loops, rgnr4end6max)
        return
    @override
    def _initialize_context4serial4LLoo_(sf, inputter4whole, /):
        'inputter4whole.fork() -> ctx' ' #assume[inputter contains global runtime info...]'
        return (0, False, [])
            # (num_rounds, stopped, ls)
    @override
    def _is_stopped4serial4LLoo_(sf, ctx, inputter, /):
        'ctx -> inputter.fork() -> stopped/bool' ' #assume[inputter contains global runtime info...]'
        (num_rounds, stopped, ls) = ctx
        return stopped
    #def _mk_child_recognizer_ex4serial4LLoo_(sf, ctx, child_item, inputter, /):

    @override
    def _update_context4serial4LLoo_(sf, child_item, child_rgnr, ctx, result6ok4child, inputter, /):
        'child_item -> child_rgnr -> ctx -> result6ok4child -> inputter.fork() -> ctx' ' #assume[inputter contains global runtime info...]'
        (body_vs_round_vs_end, ichild, _child_rgnr) = child_item
        (num_rounds, stopped, ls) = ctx
        assert not stopped
        assert ichild == num_rounds
        #if body_vs_round_vs_end is ...:
        #    #round
        #    #_rgnr = sf._rgnr4round_
        #    (ibranch, raw_oresult) = result6ok4child
        #elif body_vs_round_vs_end is False:
        #    #body
        #    #xxx:_rgnr = sf.rgnr4body4loop
        #    #(ibranch, raw_oresult) = (1, result6ok4child)
        #    #_rgnr = sf._tagged_rgnr4body4loop_
        #    (ibranch, raw_oresult) = result6ok4child
        #elif body_vs_round_vs_end is True:
        #    #end
        #    #_rgnr = sf._rgnr4end6max_
        #    (ibranch, raw_oresult) = result6ok4child
        #    assert not ibranch == 1
        #else:
        #    raise 000
        (ibranch, raw_oresult) = result6ok4child
        stopped = not ibranch == 1
        may_rgnr = sf._may_raw_rgnrs_[ibranch]
        if may_rgnr is None:
            assert ibranch == 2
            #recognizer_LLoo__ignore
            ls; pass
        else:
            rgnr = may_rgnr
            #assert not rgnr is None, (sf._may_raw_rgnrs_, ibranch)
            it = rgnr.iter4unpack_oresult4serial4LLoo(raw_oresult)
            ls.extend(it)
        ctx = (1+num_rounds, stopped, ls)
        return ctx
    @override
    def _finalize_oresult4serial4LLoo_(sf, ctx, inputter, /):
        'ctx -> inputter.fork() -> result6ok4whole_LLoo' ' #assume[inputter contains global runtime info...]'
        (num_rounds, stopped, ls) = ctx
        if not stopped: raise 000
        num_loops = num_rounds-1
        if (max_loops:=sf.imay_max_loops) == -1:
            max_loops = num_loops
        min_loops = sf.min_loops
        if not 1 <= 1+min_loops <= num_rounds <= 1+max_loops: raise Exception(min_loops, num_rounds, max_loops)#000
            #『1+』for『_rgnr4end6max_』
        if not 0 <= min_loops <= num_loops <= max_loops: raise Exception(min_loops, num_loops, max_loops)#000
        ls = tuple(ls)
        if sf.to_output_num_loops:
            return (num_loops, ls)
        return ls
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
            (body_vs_round_vs_end, ichild, _child_rgnr) = child_item
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


class RecognizerLLoo__base_loop(_IRecognizerLLoo__base_loop):
    ___no_slots_ok___ = True
    @override
    def _mk_child_recognizer_ex4serial4LLoo_(sf, ctx, child_item, inputter, /):
        'ctx -> child_item -> inputter.fork() -> (child_rgnr/IRecognizerLLoo, ctx)' ' #assume[inputter contains global runtime info...]'
        (body_vs_round_vs_end, ichild, child_rgnr) = child_item
        return (child_rgnr, ctx)
check_non_ABC(RecognizerLLoo__base_loop)










class RecognizerLLoo__many(_IRecognizerLLoo__wrapper_base__single_ref):
    ___no_slots_ok___ = True
    def __init__(sf, min_loops, imay_max_loops, uhidx4hdr, rgnr4body4loop, /):
        the_wrapped_obj = RecognizerLLoo__base_loop(to_output_num_loops:=False, min_loops, imay_max_loops, uhidx4hdr, may_rgnr4end7pre:=None, rgnr4body4loop, may_rgnr4end7post:=None)
        super().__init__(the_wrapped_obj)
        sf._args4repr = (min_loops, imay_max_loops, uhidx4hdr, rgnr4body4loop)
check_non_ABC(RecognizerLLoo__many)














class RecognizerLLoo__skip_many1(_IRecognizerLLoo__wrapper_base__single_ref):
    ___no_slots_ok___ = True
    #@override
    ___666_tribool_skip4serial4LLoo_999___ = True
    def __init__(sf, rgnr4body4loop, /):
        the_wrapped_obj = mk_LLoo__skip(RecognizerLLoo__many(min_loops:=1, imay_max_loops:=-1, uhidx4hdr:=1, mk_LLoo__skip(rgnr4body4loop)))
        super().__init__(the_wrapped_obj)
        sf._args4repr = (rgnr4body4loop,)
        assert sf.___666_tribool_skip4serial4LLoo_999___ is True
check_non_ABC(RecognizerLLoo__skip_many1)

















class RecognizerLLoo__end_by__pre(_IRecognizerLLoo__wrapper_base__single_ref):
    ___no_slots_ok___ = True
    def __init__(sf, min_loops, imay_max_loops, uhidx4hdr, rgnr4end7pre, rgnr4body4loop, /):
        if None is rgnr4end7pre:raise TypeError
        the_wrapped_obj = RecognizerLLoo__base_loop(to_output_num_loops:=False, min_loops, imay_max_loops, uhidx4hdr, may_rgnr4end7pre:=rgnr4end7pre, rgnr4body4loop, may_rgnr4end7post:=None)
        super().__init__(the_wrapped_obj)
        sf._args4repr = (min_loops, imay_max_loops, uhidx4hdr, rgnr4end7pre, rgnr4body4loop)
check_non_ABC(RecognizerLLoo__end_by__pre)







class RecognizerLLoo__end_by__post(_IRecognizerLLoo__wrapper_base__single_ref):
    ___no_slots_ok___ = True
    #API_changed:def __init__(sf, min_loops, imay_max_loops, uhidx4hdr, rgnr4body4loop, rgnr4end7post, /):
    def __init__(sf, min_loops, imay_max_loops, uhidx4hdr, rgnr4end7post, rgnr4body4loop, /):
        if None is rgnr4end7post:raise TypeError
        the_wrapped_obj = RecognizerLLoo__base_loop(to_output_num_loops:=False, min_loops, imay_max_loops, uhidx4hdr, may_rgnr4end7pre:=None, rgnr4body4loop, may_rgnr4end7post:=rgnr4end7post)
        super().__init__(the_wrapped_obj)
        sf._args4repr = (min_loops, imay_max_loops, uhidx4hdr, rgnr4end7post, rgnr4body4loop)
check_non_ABC(RecognizerLLoo__end_by__post)









class RecognizerLLoo__sep_by(_IRecognizerLLoo__wrapper_base__single_ref):
    ___no_slots_ok___ = True
    def __init__(sf, min_loops, imay_max_loops, uhidx4hdr, rgnr4sep, rgnr4item, /):
        check_int_ge(0, min_loops)
        check_int_ge(-1, imay_max_loops)
        check_int_ge(0, uhidx4hdr)
        if 0 <= imay_max_loops < 2:
            the_wrapped_obj = RecognizerLLoo__many(min_loops, imay_max_loops, uhidx4hdr, rgnr4body4loop:=rgnr4item)
        else:
            rgnr4body4loop = mk_LLoo__with_tribool_skip_as(rgnr4item, RecognizerLLoo__unbox(RecognizerLLoo__tuple(1, [mk_LLoo__skip(rgnr4sep), mk_LLoo__pack(rgnr4item)])))
            rgnr4tail = RecognizerLLoo__many(max(0,min_loops-1), imay_max_loops if imay_max_loops == -1 else max(0,imay_max_loops-1), max(0,uhidx4hdr-2), rgnr4body4loop)
            _s1 = RecognizerLLoo__tuple(min(3, uhidx4hdr), [rgnr4item, mk_LLoo__unpack(rgnr4tail)])
            if min_loops >= 1:
                the_wrapped_obj = _s1
            else:
                assert min_loops == 0
                the_wrapped_obj = mk_LLoo__optional__default(null_tuple, _s1)
            the_wrapped_obj
        the_wrapped_obj
        super().__init__(the_wrapped_obj)
        sf._args4repr = (min_loops, imay_max_loops, uhidx4hdr, rgnr4sep, rgnr4item)
check_non_ABC(RecognizerLLoo__sep_by)









class RecognizerLLoo__between(_IRecognizerLLoo__wrapper_base__single_ref):
    ___no_slots_ok___ = True
    def __init__(sf, rgnr4begin, rgnr4body, rgnr4end, /):
        the_wrapped_obj = mk_LLoo__with_tribool_skip_as(rgnr4body, RecognizerLLoo__unbox(RecognizerLLoo__tuple(1, [mk_LLoo__skip(rgnr4begin), mk_LLoo__pack(rgnr4body), mk_LLoo__skip(rgnr4end)])))
        super().__init__(the_wrapped_obj)
        sf._args4repr = (rgnr4begin, rgnr4body, rgnr4end)
check_non_ABC(RecognizerLLoo__between)




















def uhidx4hdr5may__(default, imay_max_loops, may_uhidx4hdr, /):
    if may_uhidx4hdr is None:
        uhidx4hdr = default
        if not imay_max_loops == -1:
            max_loops = imay_max_loops
            uhidx4hdr = min(uhidx4hdr, 2*max_loops)
    else:
        uhidx4hdr = may_uhidx4hdr
    return uhidx4hdr
def mk_LLoo__base_loop(rgnr4body4loop, /, *, to_output_num_loops=False, min_loops=0, imay_max_loops=-1, may_uhidx4hdr:1=None, may_rgnr4end7pre=None, may_rgnr4end7post=None):
    'IRecognizerLLoo -> IRecognizerLLoo'
    uhidx4hdr = uhidx4hdr5may__(default:=1, imay_max_loops, may_uhidx4hdr)
    return RecognizerLLoo__base_loop(to_output_num_loops, min_loops, imay_max_loops, uhidx4hdr, may_rgnr4end7pre, rgnr4body4loop, may_rgnr4end7post)
def mk_LLoo__many(rgnr4body4loop, /, *, min_loops=0, imay_max_loops=-1, may_uhidx4hdr:1=None):
    'IRecognizerLLoo -> IRecognizerLLoo'
    uhidx4hdr = uhidx4hdr5may__(default:=1, imay_max_loops, may_uhidx4hdr)
    return RecognizerLLoo__many(min_loops, imay_max_loops, uhidx4hdr, rgnr4body4loop)
def mk_LLoo__skip_many1(rgnr4body4loop, /):
    'IRecognizerLLoo -> IRecognizerLLoo'
    return RecognizerLLoo__skip_many1(rgnr4body4loop)
def mk_LLoo__end_by__pre(rgnr4end7pre, rgnr4body4loop, /, *, min_loops=0, imay_max_loops=-1, may_uhidx4hdr:1=None):
    'IRecognizerLLoo -> IRecognizerLLoo -> IRecognizerLLoo'
    uhidx4hdr = uhidx4hdr5may__(default:=1, imay_max_loops, may_uhidx4hdr)
    return RecognizerLLoo__end_by__pre(min_loops, imay_max_loops, uhidx4hdr, rgnr4end7pre, rgnr4body4loop)
#bug:def mk_LLoo__end_by__post(rgnr4body4loop, rgnr4end7post, /, *, min_loops=0, imay_max_loops=-1, may_uhidx4hdr:1=None):
def mk_LLoo__end_by__post(rgnr4end7post, rgnr4body4loop, /, *, min_loops=0, imay_max_loops=-1, may_uhidx4hdr:1=None):
    'IRecognizerLLoo -> IRecognizerLLoo -> IRecognizerLLoo'
    uhidx4hdr = uhidx4hdr5may__(default:=1, imay_max_loops, may_uhidx4hdr)
    #API_changed:return RecognizerLLoo__end_by__post(min_loops, imay_max_loops, uhidx4hdr, rgnr4body4loop, rgnr4end7post)
    return RecognizerLLoo__end_by__post(min_loops, imay_max_loops, uhidx4hdr, rgnr4end7post, rgnr4body4loop)
def mk_LLoo__sep_by(rgnr4sep, rgnr4item, /, *, min_loops=0, imay_max_loops=-1, may_uhidx4hdr:1=None):
    'IRecognizerLLoo -> IRecognizerLLoo -> IRecognizerLLoo'
    uhidx4hdr = uhidx4hdr5may__(default:=1, imay_max_loops, may_uhidx4hdr)
    return RecognizerLLoo__sep_by(min_loops, imay_max_loops, uhidx4hdr, rgnr4sep, rgnr4item)
def mk_LLoo__between(rgnr4begin, rgnr4body, rgnr4end, /):
    'IRecognizerLLoo -> IRecognizerLLoo -> IRecognizerLLoo -> IRecognizerLLoo'
    return RecognizerLLoo__between(rgnr4begin, rgnr4body, rgnr4end)




















__all__
from seed.recognize.recognizer_LLoo_.combinator_LLoo__loop import \
(mk_LLoo__base_loop
,mk_LLoo__many
,mk_LLoo__skip_many1
,mk_LLoo__end_by__pre
,mk_LLoo__end_by__post
,mk_LLoo__sep_by
,mk_LLoo__between
)
from seed.recognize.recognizer_LLoo_.combinator_LLoo__loop import *
