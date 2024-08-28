#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/recognizer_LLoo_/grammar.py


py -m seed.recognize.recognizer_LLoo_.grammar
py -m seed.recognize.recognizer_LLoo_.grammar 2>/sdcard/0my_files/tmp/0tmp
view /sdcard/0my_files/tmp/0tmp
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_LLoo_.grammar -x
py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LLoo_.grammar:__doc__ -ht


view ../../python3_src/seed/recognize/recognizer_LLoo_/syntax.txt
[[
simplified_grammar:
simplified:
grammar = end_by[<'..',line>]
line = ';;' skip_case nm postprocess '=' rgnr_expr
rgnr_expr = skip_case atom_rgnr_expr postprocess
atom_rgnr_expr
  = nm
  | str
  | {:| sep_by[<':|',rgnr_expr>] :|}
  | {+:| sep_by[<'+:|',rgnr_expr>] +:|}
  | {*:| sep_by[<'*:|',rgnr_expr>] *:|}
  | {>| sep_by[<'>|',rgnr_expr>] >|}
  | {+>| sep_by[<'+>|',rgnr_expr>] +>|}
  | {*>| sep_by[<'*>|',rgnr_expr>] *>|}
  | (, sep_by[<',',yield_rgnr_expr>] ,)
yield_rgnr_expr = '-^-'? rgnr_expr?
skip_case
  = -
  | .
  | ...
postprocess
  = [min:max1:uhidx4hdr]
  | [min:max1:uhidx4hdr:%rgnr8sep]
  | [min:max1:uhidx4hdr:/rgnr8end]
  | [min:max1:uhidx4hdr:://rgnr8end]

  | .!
  | ~!
  | ^$
  | ^^

  | !^
  | !$
  | ?$
  | ?^
  | ?/
  | ?%
 #selected:
  | $%f4eresult #nm
  | $&f4oresult #nm
  | $|f4errmsg  #nm
  | :*label     #str
 #cancelled:
  | ?=oresult   #py_expr
  | $=eresult   #py_expr
  | $>oresult   #py_expr
  | $<errmsg    #py_expr
  | $+tag       #py_expr
  | $*tag       #py_expr
]]

>>> s=bytes(range(0x80)).decode('ascii')
>>> s[32:127]
' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'




[[
why so slow?
######################
_to_show4build_ = True
######################
==>>:
build:_1_token_LLoo__grammar@seed.recognize.recognizer_LLoo_.grammar...: ... ...
build:_1_token_LLoo__grammar@seed.recognize.recognizer_LLoo_.grammar...:duration: 0.010581614999999989 *(unit: 0:00:01)
build:_2_token_LLoo__grammar@seed.recognize.recognizer_LLoo_.grammar...: ... ...
build:_2_token_LLoo__grammar@seed.recognize.recognizer_LLoo_.grammar...:duration: 2.803250773 *(unit: 0:00:01)
build:_3_token_LLoo__grammar@seed.recognize.recognizer_LLoo_.grammar...: ... ...
build:_3_token_LLoo__grammar@seed.recognize.recognizer_LLoo_.grammar...:duration: 2.765551469 *(unit: 0:00:01)
build:_4_token_LLoo__grammar@seed.recognize.recognizer_LLoo_.grammar...: ... ...
build:_4_token_LLoo__grammar@seed.recognize.recognizer_LLoo_.grammar...:duration: 2.7909477019999995 *(unit: 0:00:01)
build:_5_token_LLoo__grammar@seed.recognize.recognizer_LLoo_.grammar...: ... ...
build:_5_token_LLoo__grammar@seed.recognize.recognizer_LLoo_.grammar...:duration: 2.803178313 *(unit: 0:00:01)
]]
[[
py -m seed.recognize.recognizer_LLoo_.grammar
==>>:
import@seed.recognize.recognizer_LLoo_.grammar...: ... ...
import@seed.recognize.recognizer_LLoo_.grammar...:duration: 0.30158615000000005 *(unit: 0:00:01)
]]
[[
_to_show4build_ = True
=>nonlazy=True
==>>:
build:_1_token_LLoo__grammar@seed.recognize.recognizer_LLoo_.grammar...: ... ...
build:_1_token_LLoo__grammar@seed.recognize.recognizer_LLoo_.grammar...:duration: 0.009678076999999896 *(unit: 0:00:01)
build:_2_token_LLoo__grammar@seed.recognize.recognizer_LLoo_.grammar...: ... ...
build-nonlazy:inputter4char+inputter4token@seed.recognize.recognizer_LLoo_.grammar...: ... ...
build-nonlazy:inputter4char+inputter4token@seed.recognize.recognizer_LLoo_.grammar...:duration: 0.001654999999999962 *(unit: 0:00:01)
build:_2_token_LLoo__grammar@seed.recognize.recognizer_LLoo_.grammar...:duration: 2.6484976159999998 *(unit: 0:00:01)
build:_3_token_LLoo__grammar@seed.recognize.recognizer_LLoo_.grammar...: ... ...
build-nonlazy:inputter4char+inputter4token@seed.recognize.recognizer_LLoo_.grammar...: ... ...
build-nonlazy:inputter4char+inputter4token@seed.recognize.recognizer_LLoo_.grammar...:duration: 0.00038084600000010127 *(unit: 0:00:01)
build:_3_token_LLoo__grammar@seed.recognize.recognizer_LLoo_.grammar...:duration: 2.618429541 *(unit: 0:00:01)
build:_4_token_LLoo__grammar@seed.recognize.recognizer_LLoo_.grammar...: ... ...
build-nonlazy:inputter4char+inputter4token@seed.recognize.recognizer_LLoo_.grammar...: ... ...
build-nonlazy:inputter4char+inputter4token@seed.recognize.recognizer_LLoo_.grammar...:duration: 0.00042469300000025356 *(unit: 0:00:01)
build:_4_token_LLoo__grammar@seed.recognize.recognizer_LLoo_.grammar...:duration: 2.6324948500000005 *(unit: 0:00:01)
build:_5_token_LLoo__grammar@seed.recognize.recognizer_LLoo_.grammar...: ... ...
build-nonlazy:inputter4char+inputter4token@seed.recognize.recognizer_LLoo_.grammar...: ... ...
build-nonlazy:inputter4char+inputter4token@seed.recognize.recognizer_LLoo_.grammar...:duration: 0.0003873070000004475 *(unit: 0:00:01)
build:_5_token_LLoo__grammar@seed.recognize.recognizer_LLoo_.grammar...:duration: 2.6475217790000016 *(unit: 0:00:01)
]]




py_adhoc_call   seed.recognize.recognizer_LLoo_.grammar   @f
#]]]'''
__all__ = r'''
mk_recognizer_LLoo5grammar__
    IBundle4referred_funcs4grammar








simplified_grammar4LLoo
IBundle4referred_funcs4grammar
    bundle4referred_funcs4simplified_grammar4LLoo
token_LLoo__grammar4simplified_grammar4LLoo
mk_recognizer_LLoo5grammar__
    RecognizationFail

tokenize4simplified_grammar4LLoo_
    keyed_char_LLoos4tokenize4simplified_grammar4LLoo
    ignored_tkeys4tokenize4simplified_grammar4LLoo
    subkeying_tkeys4tokenize4simplified_grammar4LLoo
    subkeying_sep4tokenize4simplified_grammar4LLoo
'''.split()#'''
#(_3_fs, _3_keyed_rgnrs4token, _3_token_LLoo__grammar)
#(_2_fs, _2_keyed_rgnrs4token, _2_token_LLoo__grammar)
#(_1_fs, _1_keyed_rgnrs4token, _1_token_LLoo__grammar)
#
#keyed_rgnrs4token
#   token_LLoo__grammar
#
#recognizer_LLoo__grammar
#    recognizer_LLoo__rgnr_expr
#        view4scene
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.for_libs.for_time import (
Timer__print_err
    ,timer__print_err__thread_wide
    ,timer__print_err__process_wide
    ,timer__print_err__system_wide__highest_resolution
    ,timer__print_err__system_wide__monotonic
)

timer = timer__print_err__thread_wide
_to_show_ = __name__ == "__main__"
_to_show4build_ = False
#_to_show4build_ = True

with timer(prefix='import@seed.recognize.recognizer_LLoo_.grammar...', _to_show_=_to_show_, _show_hint_on_enter_=True):
    from seed.recognize.recognizer_LLoo_.stream.char_stream import CharTokenKeySetQuery__using_regex, recognizer_LLoo__isdigit, recognizer_LLoo__regex__w
    from seed.recognize.recognizer_LLoo_.stream.char_stream import char_set_query__regex__w

    from seed.recognize.recognizer_LLoo_.combinator_LLoo__wrapper import mk_LLoo__not_followed_by4whole, mk_LLoo__unbox, mk_LLoo__simple_postprocess6ok
    from seed.recognize.recognizer_LLoo_.stream.token_stream import mk_LLoo__tkey_set, mk_LLoo__match_constant_tkey, recognizer_LLoo__any_tkey, mk_LLoo__raw_string


    from seed.recognize.recognizer_LLoo_.combinator_LLoo__loop import mk_LLoo__many, mk_LLoo__end_by__pre, mk_LLoo__sep_by, mk_LLoo__between
    from seed.recognize.recognizer_LLoo_.combinator_LLoo__serial import mk_LLoo__tuple

    from seed.recognize.recognizer_LLoo_.stream.token_stream import mk_LLoo__match_constant_tkeys
    from seed.recognize.recognizer_LLoo_.stream.char_stream import recognizer_LLoo__isspace
    from seed.recognize.recognizer_LLoo_.combinator_LLoo__wrapper import mk_LLoo__skip, mk_LLoo__unpack, mk_LLoo__pack, mk_LLoo__ref, mk_LLoo__optional__tmay
    from seed.recognize.recognizer_LLoo_.combinator_LLoo__parallel import mk_LLoo__the_first_one, mk_LLoo__the_only_one


    from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import IRecognizerLLoo, parse__via_IRecognizerLLoo, mk_gi4skip_header_signal, Signal__HeaderCompleted, Reply4IRecognizerLLoo
    from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import Error4IRecognizerLLoo


    from seed.recognize.recognizer_LLoo_.Scene import mk_Scene_ex



    from seed.recognize.recognizer_LLoo_._common import KindedName, Cased

    from seed.recognize.recognizer_LLoo_.combinator_LLoo__wrapper import mk_LLoo__lazy

    from seed.recognize.recognizer_LLoo_.tokenize import tokenize_# iter4tokenize_
    #obsolete#def tokenize_(may__bad_reply2may_token_keyed_data8eof, is_tkey_ignored_, keyed_rgnrs4token, inputter, /, *, global_runtime_info=None):
#def tokenize_(may_exc_mkr_or_tailing_tkds6fail, tailing_tkds6eof, tkey2ignored_, tkey2stated_, sep4subkeying, tkey2subkeying_, st0, st2may_keyed_rgnrs4token, inputter, /, *, global_runtime_info=None, begin_idx4gap=0, nonlazy=False):
    '(may (msg->TokenizationFail)|[tkd]) -> [tkd] -> (tkey1->bool) -> (tkey1->bool) -> str -> (tkey0->bool) -> st -> {st:may [(tkey0, rgnr4tdat/IRecognizerLLoo)]} -> IForkableForwardInputStream{low_level_token} -> IForkableForwardInputStream{high_level_token | ^TokenizationFail} #[tkd::Cased][tkey0 := tkey{before subkeying}][tkey1 := tkey{after subkeying}]'
#def iter4tokenize_(may_exc_mkr_or_tailing_tkds6fail, tailing_tkds6eof, tkey2ignored_, tkey2stated_, sep4subkeying, tkey2subkeying_, st0, st2may_keyed_rgnrs4token, inputter, /, *, begin_idx4gap=0, to_yield_leading_gap=False):
    '(may (msg->TokenizationFail)|[tkd]) -> [tkd] -> (tkey1->bool) -> (tkey1->bool) -> str -> (tkey0->bool) -> st -> {st:may [(tkey0, rgnr4tdat/IRecognizerLLoo)]} -> IForkableForwardInputStream{low_level_token} -> Iter (high_level_token/IToken | ^TokenizationFail) #[tkd::Cased][tkey0 := tkey{before subkeying}][tkey1 := tkey{after subkeying}]'

    from seed.recognize.recognizer_LLoo_.stream.token_stream import mk_LLoo__traced, mk_LLoo__traced__simple
    #def mk_LLoo__traced(rgnr, /, *, may_label6enter=None, may_label6hdr_sgnl=None, may_label6err=None, may_label6ok=None, may_label6exit=None):
    #def mk_LLoo__traced__simple(label, rgnr, /):
    from seed.tiny_.check import check_type_is, check_type_le, check_tmay, check_pair, check_may_# check_int_ge
    from seed.tiny import dict_add__new, set_add, dict_add, echo, expectError
    from seed.tiny_.mk_fdefault import eliminate_tmay__mix
    #def eliminate_tmay__mix(tmay_value, imay_xdefault_rank, xdefault, /, *args4xdefault):

    from ast import literal_eval
    from collections.abc import Callable as ICallable

    from seed.recognize.recognizer_LLoo_.combinator_LLoo__wrapper import Callable__ref
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
    from seed.recognize.recognizer_LLoo_.combinator_LLoo__loop import \
(mk_LLoo__base_loop
,mk_LLoo__many
,mk_LLoo__skip_many1
,mk_LLoo__end_by__pre
,mk_LLoo__end_by__post
,mk_LLoo__sep_by
,mk_LLoo__between
)
    from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
    #from seed.helper.repr_input import repr_helper
___end_mark_of_excluded_global_names__0___ = ...
__all__

class RecognizationFail(Error4IRecognizerLLoo):pass


class IBundle4referred_funcs4grammar(ABC):
    __slots__ = ()
    @abstractmethod
    def reset(sf, /):
        '-> None # eg:reset:sf.*mutable_args #init/reassign fresh obj instead of clear()'
    @abstractmethod
    def detach(sf, /):
        '-> (*sf.*mutable_args) #delete/reassign dummy obj'

class _Bundle4referred_funcs4simplified_grammar4LLoo(IBundle4referred_funcs4grammar):
    #bundle4referred_funcs4simplified_grammar4LLoo
    #class _fs8postprocess:
    r'''[[[
grep '\$& *_' ../../python3_src/seed/recognize/recognizer_LLoo_/grammar.py
.,.+24s/^\(;;\|    {\?>| \).*\$& *\(\w\+\)/\2
_mk_name_rgnr_pair
_mk_rgnr__wrapper
_mk_rgnr__parallel
_mk_rgnr__parallel__tag
_mk_rgnr__parallel__cased
_mk_rgnr__choice
_mk_rgnr__choice__tag
_mk_rgnr__choice__cased
_mk_rgnr__tuple
_mk_rgnr__raw_str
_mk4py_expr5raw_str
_mk_char_set_query
_mk_knm8f
_mk_rgnr__ref
_mk_rgnr__tkd
_get_payload
    #]]]'''#'''
    ___no_slots_ok___ = True

    #def __init__(sf, /, *, no_op:bool):
    #    check_type_is(bool, no_op)
    #    sf.no_op = no_op
    #def __getattribute__(sf, nm, /):
    #    if nm.startswith('_mk') and sf.no_op:
    #        return echo
    #    return super().__getattribute__(nm)
    def __init__(sf, /, *, _debug_:bool):
        check_type_is(bool, _debug_)
        sf._debug_ = _debug_
        sf.reset()
    if 0:
        #useless
        def copy_and_reset(sf, /):
            return type(sf)(_debug_=sf._debug_)
    @override
    def reset(sf, /):
        '-> None # eg:reset:(knm_set, nm2rgnr, register4scene, view4scene, ...)'
        sf.knm_set = set()
        sf.nm2rgnr = {}
        (sf.register4scene, sf.view4scene) = mk_Scene_ex()
    @override
    def detach(sf, /):
        '-> (knm_set, nm2rgnr, register4scene, view4scene)'
        r = (sf.knm_set, sf.nm2rgnr, sf.register4scene, sf.view4scene)
        (sf.knm_set, sf.nm2rgnr, sf.register4scene, sf.view4scene) = [None]*len(r)
        return r

    def _add_knm(sf, knm, /):
        check_type_is(KindedName, knm)
        #if not set_add(sf.knm_set, knm):raise KeyError(knm)
        sf.knm_set.add(knm)
    def _get_payload(sf, oresult, /):
        check_type_le(Cased, oresult)
        return oresult.payload
    def _mk_rgnr__tkd(sf, oresult, /):
        check_type_is(str, oresult)
        return mk_LLoo__match_constant_tkey(tkey:=oresult, nm_or_case4token_extraction='tkd')
    def _mk_rgnr__ref(sf, oresult, /):
        check_type_is(str, oresult)
        sf._add_knm(_knm4rgnr:=KindedName(IRecognizerLLoo, nm:=oresult))
        rgnr = mk_LLoo__ref(sf.view4scene, _knm4rgnr)
        rgnr = mk_LLoo__pack(rgnr, to_wrap=True)
            # <<== strict: .unlazy()
        return rgnr
    def _mk_knm8f(sf, oresult, /):
        check_type_is(str, oresult)
        sf._add_knm(_knm4f:=KindedName(ICallable, nm:=oresult))
        return Callable__ref(sf.view4scene, _knm4f)
    def _mk_char_set_query(sf, oresult, /):
        check_type_is(str, oresult)
        return CharTokenKeySetQuery__using_regex(False, regex:=oresult)
    def _mk4py_expr5raw_str(sf, oresult, /):
        #xxx:check_type_is(Cased, oresult)
        return _mk4py_expr5raw_str(oresult)
    def _mk_rgnr__raw_str(sf, oresult, /):
        check_type_is(tuple, oresult)
        assert len(oresult) == 5
        return mk_LLoo__raw_string(*oresult[1:-1])
    def _mk_rgnr__tuple(sf, oresult, /):
        check_type_is(tuple, oresult)
        assert len(oresult) == 3
        ls = oresult[1]
            # :: [(Cased(0,tmay rgnr)|Cased(1,rgnr))]
        check_type_is(tuple, ls)
        for i, x in enumerate(ls):
            if x.case == 0:
                check_tmay(tm:=x.payload)
                uhidx4hdr = bool(tm)+2*i
                break#ignore succeed '-^-'
            assert x.case == 1, x
        else:
            uhidx4hdr = 1 if ls else 0
        uhidx4hdr
        rs = []
        for x in ls:
            if x.case:
                rgnr = x.payload
                rs.append(rgnr)
            else:
                tm = x.payload
                rs.extend(tm)
        rs
        return mk_LLoo__tuple(uhidx4hdr, rs)
    def _mk_rgnr__choice_(sf, oresult, /, **kwds):
        check_type_is(tuple, oresult)
        check_type_is(tuple, rs:=oresult[1])
        return mk_LLoo__the_first_one(rs, **kwds)
    def _mk_rgnr__parallel_(sf, oresult, /, **kwds):
        check_type_is(tuple, oresult)
        check_type_is(tuple, rs:=oresult[1])
        return mk_LLoo__the_only_one(rs, **kwds)
    def _mk_rgnr__choice__cased(sf, oresult, /):
        return sf._mk_rgnr__choice_(oresult, cased=True)
    def _mk_rgnr__choice__tag(sf, oresult, /):
        return sf._mk_rgnr__choice_(oresult, tagged=True)
    def _mk_rgnr__choice(sf, oresult, /):
        return sf._mk_rgnr__choice_(oresult)
    def _mk_rgnr__parallel__cased(sf, oresult, /):
        return sf._mk_rgnr__parallel_(oresult, cased=True)
    def _mk_rgnr__parallel__tag(sf, oresult, /):
        return sf._mk_rgnr__parallel_(oresult, tagged=True)
    def _mk_rgnr__parallel(sf, oresult, /):
        return sf._mk_rgnr__parallel_(oresult)
    def _mk_rgnr__wrapper(sf, oresult, /):
        check_type_is(tuple, oresult)
        (tmay_skip_case, rgnr, ls4postprocess) = oresult
        check_tmay(tmay_skip_case)
        check_type_is(tuple, ls4postprocess)
        for postprocess in ls4postprocess:
            rgnr = _apply_postprocess(postprocess, rgnr)
        for skip_case in tmay_skip_case:
            rgnr = _apply_skip_case(skip_case, rgnr)
        return rgnr
    def _mk_name_rgnr_pair(sf, oresult, /):
        check_type_is(tuple, oresult)
        (tmay_skip_case, nm, ls4postprocess, rgnr) = oresult
        _rgnr = sf._mk_rgnr__wrapper((tmay_skip_case, rgnr, ls4postprocess))
        if sf._debug_:
            _rgnr = mk_LLoo__traced__simple(nm, _rgnr)
        #dict_add__new(sf.nm2rgnr, nm, _rgnr)
        if not dict_add(sf.nm2rgnr, nm, _rgnr):raise KeyError(nm)
        sf.register4scene.register(KindedName(IRecognizerLLoo, nm), _rgnr)
        return (nm, _rgnr)
def _apply_skip_case(skip_case, rgnr, /):
    check_type_is(Cased, skip_case)
    skip_case = skip_case.case
    check_type_is(str, skip_case)
    if skip_case == '-':
        T = mk_LLoo__skip
    elif skip_case == '...':
        T = mk_LLoo__unpack
    elif skip_case == '.':
        T = mk_LLoo__pack
    else:
        raise Error4IRecognizerLLoo(fr'unknown skip_case:{skip_case!r}')
    return T(rgnr, to_wrap=True)
_op2mkr = (
{".!" : mk_LLoo__unbox
,"~!" : mk_LLoo__invert_err_ok
,"^$" : mk_LLoo__skip_header_signal
,"^^" : mk_LLoo__header_signal_at_beginning
,"!^" : mk_LLoo__not_followed_by4hdr
,"!$" : mk_LLoo__not_followed_by4whole
,"?$" : mk_LLoo__look_ahead4whole
,"?^" : mk_LLoo__look_ahead4hdr
,"?/" : mk_LLoo__optional__tmay
,"?%" : mk_LLoo__optional__either
})
_op2mkr_1arg = (
{"$%" : mk_LLoo__simple_postprocess
,"$&" : mk_LLoo__simple_postprocess6ok
,"$|" : mk_LLoo__simple_postprocess6err
,":*" : mk_LLoo__traced__simple
,"?=" : mk_LLoo__optional__default
,"$=" : mk_LLoo__constant_overwrite
,"$>" : mk_LLoo__constant_overwrite6ok
,"$<" : mk_LLoo__constant_overwrite6err
,"$+" : mk_LLoo__tag
,"$*" : mk_LLoo__Cased
})
_op2loop_mkr = (
{":%" : mk_LLoo__sep_by
,":/" : mk_LLoo__end_by__pre
,":://" : mk_LLoo__end_by__post
})
def _apply_postprocess(postprocess, rgnr, /):
    #if type(postprocess) is str:
    if type(postprocess) is Cased:
        cased = postprocess
        op = tkey = cased.case
        f = _op2mkr[op]
        return f(rgnr)
    check_type_is(tuple, postprocess)
    ls = postprocess
    begin = ls[0]
    #if 0b0000:print(begin)
    begin = tkey = begin.case
    check_type_is(str, begin)
    if begin == '[':
        # (, "[" , -^- , uint ?/ , ":" , uint ?/ , ":" , uint ?/ , sep_end_by ?/ , "]" ,)
        # loop:many/sep_by/end_by
        (_, tmay_min, _, tmay_max, _, tmay_uhidx4hdr, tmay__sep_end_by, _) = ls
        min_loops = eliminate_tmay__mix(tmay_min, -1, 0)
        imay_max_loops = eliminate_tmay__mix(tmay_max, -1, -1)
        may_uhidx4hdr = eliminate_tmay__mix(tmay_uhidx4hdr, -1, None)
        kwds = dict(min_loops=min_loops, imay_max_loops=imay_max_loops, may_uhidx4hdr=may_uhidx4hdr)
        if not tmay__sep_end_by:
            f = mk_LLoo__many
            return f(rgnr, **kwds)
        [(op, _rgnr)] = tmay__sep_end_by
        op = tkey = op.case
        f = _op2loop_mkr[op]
        return f(_rgnr, rgnr, **kwds)
    check_pair(ls)
    op, arg = ls
    op = tkey = op.case
    check_type_is(str, op)
    f = _op2mkr_1arg[op]
    return f(arg, rgnr)
def _mk_uint(digits, /):
    return int(''.join(digits))
def _mk_str_and_eval(chars, /):
    s = _mk_str(chars)
    return literal_eval(s)
def _mk_str(chars, /):
    try:
        s = ''.join(chars)
    except TypeError:
        raise TypeError(chars)
    return s
def _mk4raw_str(pair, /):
    nm, chars = pair
    s = _mk_str(chars)
    check_type_is(str, nm)
    check_type_is(str, s)
    return Cased(nm, s)
def __():
  def _mk4py_expr5raw_str(cased, /):
    #old-API:tokenize_()
    check_type_is(Cased, cased)
    (nm, s) = cased
    if not nm == 'py_expr':
        raise Error4IRecognizerLLoo(fr'unknown raw_str case:{nm!r} ;expecting: "py_expr"')
    x = eval(s, {}, {})
    return x
def _mk4py_expr5raw_str(s, /):
    #new-API:tokenize_()
    check_type_is(str, s)
    x = eval(s, {}, {})
    return x

def _mk4avoid(rgnr_, _rgnr, /):
    return mk_LLoo__unbox(mk_LLoo__tuple(3, [mk_LLoo__not_followed_by4whole(rgnr_), _rgnr]))

def _traced(label, rgnr, /):
    return mk_LLoo__traced__simple(label, rgnr)
    def _traced(label6err, rgnr, /):
        return mk_LLoo__traced(rgnr, may_label6err=label6err)

def __():
    #:h [:
    #    #vim:]
    #*[:punct:]*	  [:punct:]   ispunct	ASCII punctuation characters
    pass

def _1_main(*, _debug_, no_op):
    ######################
    ######################
    ######################
    fs = _Bundle4referred_funcs4simplified_grammar4LLoo(_debug_=_debug_) #(no_op=no_op)
    if no_op:
        def g(f6ok, rgnr, /):
            return rgnr
    else:
        def g(f6ok, rgnr, /):
            return mk_LLoo__simple_postprocess6ok(f6ok, rgnr)
    if _debug_:
        f = _traced
    else:
        def f(label, rgnr, /):
            return rgnr
    f
    ######################
    ######################
    ######################
    ops4skip_case = \
      ('-'
      ,'.'
      ,'...'
      )
    ops4simple_postprocess = \
      ('$%' #f4eresult
      ,'$&' #f4oresult
      ,'$|' #f4errmsg
      )
    ops4postprocess = \
      ('.!'
      ,'~!'
      ,'^$'
      ,'^^'
      ,'!^'
      ,'!$'
      ,'?$'
      ,'?^'
      ,'?/'
      ,'?%'
      )
    ops4simple_postprocess__using_py_expr = \
      ('?=' #oresult
      ,'$=' #eresult
      ,'$>' #oresult
      ,'$<' #errmsg
      ,'$+' #tag
      ,'$*' #tag
      )
    ops = r'''
    ;; = ..
    [ ] : ::// :/ :%
    (, ,) , -^-
    {>| >|} >|
    {+>| +>|} +>|
    {*>| *>|} *>|
    {:| :|} :|
    {+:| +:|} +:|
    {*:| *:|} *:|
    - . ...
    $% $& $|
    .!
    ~!
    ^$
    ^^
    !^
    !$
    ?$
    ?^
    ?/
    ?%
    :*


    ?=
    $=
    $>
    $<
    $+
    $*

    '''#'''
    ops = ops.split()
    ops.sort(key=len, reverse=True)
    ######################
    ######################
    ######################
    char_LLoo__spaces1 = mk_LLoo__skip(mk_LLoo__many(recognizer_LLoo__isspace, min_loops=1))
    char_LLoo__line_tail_comment = mk_LLoo__skip(mk_LLoo__tuple(1, [mk_LLoo__match_constant_tkey('#'), mk_LLoo__end_by__pre(mk_LLoo__match_constant_tkey('\n'), recognizer_LLoo__any_tkey, min_loops=0)]))
        # \n # ???eof???
    char_LLoo__uint = mk_LLoo__simple_postprocess6ok(_mk_uint, mk_LLoo__many(recognizer_LLoo__isdigit, min_loops=1))
    char_LLoo__name = mk_LLoo__simple_postprocess6ok(_mk_str, _mk4avoid(recognizer_LLoo__isdigit, mk_LLoo__many(recognizer_LLoo__regex__w, min_loops=1)))
    char_LLoo__str = mk_LLoo__simple_postprocess6ok(_mk_str_and_eval, mk_LLoo__tuple(1, [__:=mk_LLoo__match_constant_tkey('"'), mk_LLoo__unpack(mk_LLoo__many(mk_LLoo__tkey_set(CharTokenKeySetQuery__using_regex(False, r'[^"]')))), __]))

    char_LLoo__raw_str = mk_LLoo__simple_postprocess6ok(_mk4raw_str, mk_LLoo__tuple(1,
        # py_expr ::= &'py_expr:xxx(...)xxx'
        # --> Cased("py_expr", raw_str)
        [mk_LLoo__skip(mk_LLoo__match_constant_tkeys("&'"))
        ,char_LLoo__name#eg:"py_expr"
        ,mk_LLoo__skip(mk_LLoo__match_constant_tkey(":"))
        ,mk_LLoo__raw_string
            (CharTokenKeySetQuery__using_regex(False, '[(]')
            ,CharTokenKeySetQuery__using_regex(False, '[)]')
            ,char_set_query__regex__w
            )
        ,mk_LLoo__skip(mk_LLoo__match_constant_tkey("'"))
        ]))
    tkeys4ignore = ('spaces1', 'line_tail_comment')
    sep4subkeying = '-'
    tkeys4subkeying = ('raw_str',)
    keyed_rgnrs4token = (
    [('spaces1', char_LLoo__spaces1)
    ,('line_tail_comment', char_LLoo__line_tail_comment)
    ,('uint', char_LLoo__uint)
    ,('name', char_LLoo__name)
    ,('str', char_LLoo__str)
    ,('raw_str', char_LLoo__raw_str)
        # py_expr ::= &'py_expr:xxx(...)xxx'
        # --> Cased("py_expr", raw_str)#char_LLoo__raw_str
        # --> Cased("raw_str", Cased("py_expr", raw_str))#mk_LLoo__the_first_one
        # --> Cased("raw_str-py_expr", raw_str)#new-API:tokenize_():tkey2subkeying_:
    ,*((op, mk_LLoo__match_constant_tkeys(op)) for op in ops)
    ])

    ######################
    ######################
    ######################
    def mk_LLoo__match_constant_tkd(tkey, /):
        return mk_LLoo__match_constant_tkey(tkey, nm_or_case4token_extraction='tkd')
    if no_op:
        _mk_LLoo__match_constant_tkey = mk_LLoo__match_constant_tkey
    else:
        _mk_LLoo__match_constant_tkey = mk_LLoo__match_constant_tkd
    def _mk4ops(ops, /):
        return mk_LLoo__the_first_one(map(_mk_LLoo__match_constant_tkey, ops))
    def _mk4branch4atom_rgnr_expr(open, close, sep, rgnr_expr, /):
      # {:| sep_by[<':|',rgnr_expr>] :|}
      return mk_LLoo__tuple(1,
        [_mk_LLoo__match_constant_tkey(open)
        ,mk_LLoo__sep_by(_mk_LLoo__match_constant_tkey(sep), mk_LLoo__pack(rgnr_expr, to_wrap=True))
            #NOTE:『rgnr_expr-ref-lazy』==>>『to_wrap=True』
        ,_mk_LLoo__match_constant_tkey(close)
        ])
    (register4scene, view4scene) = mk_Scene_ex()
    ######################
    ######################
    ######################
    #always:_mk4py_expr5raw_str
    #not_used:_mk_rgnr__raw_str
    #not_used:_mk_char_set_query



    #token_LLoo__raw_str = g(fs._get_payload, mk_LLoo__match_constant_tkd('raw_str'))
    token_LLoo__raw_str8py_expr = g(fs._get_payload, mk_LLoo__match_constant_tkd('raw_str-py_expr'))
        # <-- Cased("raw_str-py_expr", raw_str)#new-API:tokenize_():tkey2subkeying_:
    token_LLoo__str = g(fs._get_payload, mk_LLoo__match_constant_tkd('str'))
    token_LLoo__name = g(fs._get_payload, mk_LLoo__match_constant_tkd('name'))
    token_LLoo__uint = g(fs._get_payload, mk_LLoo__match_constant_tkd('uint'))

    #token_LLoo__raw_str = f('raw_str', token_LLoo__raw_str)
    token_LLoo__raw_str8py_expr = f('raw_str8py_expr', token_LLoo__raw_str8py_expr)
    token_LLoo__str = f('str', token_LLoo__str)
    token_LLoo__name = f('name', token_LLoo__name)
    token_LLoo__uint = f('uint', token_LLoo__uint)


    token_LLoo__nm4knm8f = g(fs._mk_knm8f, token_LLoo__name)
    token_LLoo__nm8ref = g(fs._mk_rgnr__ref, token_LLoo__name)
    token_LLoo__str8tkd = g(fs._mk_rgnr__tkd, token_LLoo__str)

    token_LLoo__nm4knm8f = f('nm4knm8f', token_LLoo__nm4knm8f)
    token_LLoo__nm8ref = f('nm8ref', token_LLoo__nm8ref)
    token_LLoo__str8tkd = f('str8tkd', token_LLoo__str8tkd)



    token_LLoo__py_expr = mk_LLoo__the_first_one(
        [token_LLoo__uint
        ,token_LLoo__str
        ,g(fs._mk4py_expr5raw_str, token_LLoo__raw_str8py_expr)
            #new-API:tokenize_()
        #,mk_LLoo__simple_postprocess6ok(_mk4py_expr5raw_str, token_LLoo__raw_str)
            #old-API:tokenize_()

            # ~= ,g(fs._mk4py_expr5raw_str, token_LLoo__raw_str)
        #??? ,mk_LLoo__simple_postprocess6ok(_mk4py_expr5name, token_LLoo__name)
        #   ??? knm:=(object,nm)
        #   ref:leaf???
        ])

    token_LLoo__rgnr_expr = mk_LLoo__ref(view4scene, _knm4rgnr_expr:=KindedName(IRecognizerLLoo, 'rgnr_expr'))
        #ref to:_token_LLoo__rgnr_expr

    token_LLoo__op4postprocess = _mk4ops(ops4postprocess)
    token_LLoo__skip_case = _mk4ops(ops4skip_case)

    token_LLoo__py_expr = f('py_expr', token_LLoo__py_expr)
    token_LLoo__rgnr_expr = f('rgnr_expr', token_LLoo__rgnr_expr)
    token_LLoo__op4postprocess = f('op4postprocess', token_LLoo__op4postprocess)
    token_LLoo__skip_case = f('skip_case', token_LLoo__skip_case)


    token_LLoo__simple_postprocess__using_py_expr = mk_LLoo__tuple(1, [_mk4ops(ops4simple_postprocess__using_py_expr), token_LLoo__py_expr])
    token_LLoo__simple_postprocess = mk_LLoo__tuple(1, [_mk4ops(ops4simple_postprocess), token_LLoo__nm4knm8f])#token_LLoo__name
    token_LLoo__traced = mk_LLoo__tuple(1, [_mk_LLoo__match_constant_tkey(':*'), token_LLoo__str])
        # :*label
        #===token_LLoo__simple_postprocess__using_str

    token_LLoo__loop4postprocess = mk_LLoo__tuple(1,
        # [min:max:uhidx4hdr:%rgnr8sep]
        [mk_LLoo__skip(_mk_LLoo__match_constant_tkey('['))
        ,mk_LLoo__optional__tmay(token_LLoo__uint)
        ,mk_LLoo__optional__tmay(mk_LLoo__unbox(mk_LLoo__tuple(1, [mk_LLoo__skip(_mk_LLoo__match_constant_tkey(':')),mk_LLoo__optional__tmay(token_LLoo__uint)])))
        ,mk_LLoo__optional__tmay(mk_LLoo__unbox(mk_LLoo__tuple(1, [mk_LLoo__skip(_mk_LLoo__match_constant_tkey(':')),mk_LLoo__optional__tmay(token_LLoo__uint)])))
        ,mk_LLoo__optional__tmay(mk_LLoo__tuple(1, [_mk4ops([':%',':/',':://']),token_LLoo__rgnr_expr]))
        ,mk_LLoo__skip(_mk_LLoo__match_constant_tkey(']'))
        ])
    token_LLoo__loop4postprocess = mk_LLoo__tuple(1,
        # [min?:max?:uhidx4hdr?:%rgnr8sep]
        [_mk_LLoo__match_constant_tkey('[')
        ,mk_LLoo__optional__tmay(token_LLoo__uint)#min
        ,_mk_LLoo__match_constant_tkey(':')
        ,mk_LLoo__optional__tmay(token_LLoo__uint)#max
        ,_mk_LLoo__match_constant_tkey(':')
        ,mk_LLoo__optional__tmay(token_LLoo__uint)#uhidx4hdr
        ,mk_LLoo__optional__tmay(mk_LLoo__tuple(1, [_mk4ops([':%',':/',':://']),token_LLoo__rgnr_expr]))
        ,_mk_LLoo__match_constant_tkey(']')
        ])

    token_LLoo__simple_postprocess__using_py_expr = f('simple_postprocess__using_py_expr', token_LLoo__simple_postprocess__using_py_expr)
    token_LLoo__simple_postprocess = f('simple_postprocess', token_LLoo__simple_postprocess)
    token_LLoo__traced = f('traced', token_LLoo__traced)
    token_LLoo__loop4postprocess = f('loop4postprocess', token_LLoo__loop4postprocess)

    token_LLoo__postprocess = mk_LLoo__the_first_one(
        [token_LLoo__loop4postprocess
        ,token_LLoo__op4postprocess
        ,token_LLoo__traced
        ,token_LLoo__simple_postprocess
        ,token_LLoo__simple_postprocess__using_py_expr
        ])

    token_LLoo__postprocess = f('postprocess', token_LLoo__postprocess)


    token_LLoo__line4grammar = mk_LLoo__tuple(1,
        [mk_LLoo__skip(_mk_LLoo__match_constant_tkey(';;'))
        ,mk_LLoo__optional__tmay(token_LLoo__skip_case)
        ,token_LLoo__name
        ,mk_LLoo__many(token_LLoo__postprocess)
        ,mk_LLoo__skip(_mk_LLoo__match_constant_tkey('='))
        ,token_LLoo__rgnr_expr
        ])

    token_LLoo__line4grammar = g(fs._mk_name_rgnr_pair, token_LLoo__line4grammar)
    token_LLoo__line4grammar = f('line4grammar', token_LLoo__line4grammar)

    token_LLoo__grammar = mk_LLoo__end_by__pre(mk_LLoo__skip(_mk_LLoo__match_constant_tkey('..')), token_LLoo__line4grammar)
    token_LLoo__grammar = f('grammar', token_LLoo__grammar)

    #yield_rgnr_expr = '-^-'? rgnr_expr?
    if 0: token_LLoo__yield_rgnr_expr = mk_LLoo__tuple(1,
        [mk_LLoo__optional__tmay(_mk_LLoo__match_constant_tkey('-^-'))
        ,mk_LLoo__optional__tmay(token_LLoo__rgnr_expr)
        ])
    _1_token_LLoo__yield_rgnr_expr = mk_LLoo__unbox(mk_LLoo__tuple(1,
        [mk_LLoo__skip(_mk_LLoo__match_constant_tkey('-^-'))
        ,mk_LLoo__optional__tmay(token_LLoo__rgnr_expr)
        ]))
    token_LLoo__yield_rgnr_expr = mk_LLoo__the_first_one(
        [_1_token_LLoo__yield_rgnr_expr
        ,token_LLoo__rgnr_expr
        ]
        , cased=True
        )
    token_LLoo__yield_rgnr_expr = f('yield_rgnr_expr', token_LLoo__yield_rgnr_expr)

    token_LLoo__atom_rgnr_expr = mk_LLoo__the_first_one(
        [token_LLoo__nm8ref#token_LLoo__name
        ,token_LLoo__str8tkd#token_LLoo__str
        ,g(fs._mk_rgnr__parallel, _mk4branch4atom_rgnr_expr('{:|', ':|}', ':|', token_LLoo__rgnr_expr))
        ,g(fs._mk_rgnr__parallel__tag, _mk4branch4atom_rgnr_expr('{+:|', '+:|}', '+:|', token_LLoo__rgnr_expr))
        ,g(fs._mk_rgnr__parallel__cased, _mk4branch4atom_rgnr_expr('{*:|', '*:|}', '*:|', token_LLoo__rgnr_expr))
        ,g(fs._mk_rgnr__choice, _mk4branch4atom_rgnr_expr('{>|', '>|}', '>|', token_LLoo__rgnr_expr))
        ,g(fs._mk_rgnr__choice__tag, _mk4branch4atom_rgnr_expr('{+>|', '+>|}', '+>|', token_LLoo__rgnr_expr))
        ,g(fs._mk_rgnr__choice__cased, _mk4branch4atom_rgnr_expr('{*>|', '*>|}', '*>|', token_LLoo__rgnr_expr))
        ,g(fs._mk_rgnr__tuple, _mk4branch4atom_rgnr_expr('(,', ',)', ',', token_LLoo__yield_rgnr_expr))
        #no: 『>| (, "[<" , regex8char_set_query , -"," , regex8char_set_query , -"," , regex8char_set_query , ">]" ,) $& _mk_rgnr__raw_str』
        ]
        #,cased=True
        )
    token_LLoo__atom_rgnr_expr = f('atom_rgnr_expr', token_LLoo__atom_rgnr_expr)

    token_LLoo__rgnr_expr
        #rgnr_expr = skip_case?/ atom_rgnr_expr postprocess[0::1]
    _token_LLoo__rgnr_expr = mk_LLoo__tuple(3,
        [mk_LLoo__optional__tmay(token_LLoo__skip_case)
        ,token_LLoo__atom_rgnr_expr
        ,mk_LLoo__many(token_LLoo__postprocess)
        ])

    _token_LLoo__rgnr_expr = g(fs._mk_rgnr__wrapper, _token_LLoo__rgnr_expr)
    _token_LLoo__rgnr_expr = f('_rgnr_expr', _token_LLoo__rgnr_expr)

    register4scene.register(_knm4rgnr_expr, _token_LLoo__rgnr_expr)
    ##register4scene.register(KindedName(ICallable, '_mk4py_expr5raw_str'), _mk4py_expr5raw_str)

    view4scene.detect_circle_ref()
    assert not (__:=[*view4scene.findout_all_missing_kinded_names()]), __
    #return (keyed_rgnrs4token, token_LLoo__grammar, token_LLoo__atom_rgnr_expr)
    return (fs, tkeys4ignore, sep4subkeying, tkeys4subkeying, keyed_rgnrs4token, token_LLoo__grammar)
if __name__ == "__main__":
    from seed.recognize.recognizer_LLoo_.grammar import (_1_fs, _1_tkeys4ignore, _1_sep4subkeying, _1_tkeys4subkeying, _1_keyed_rgnrs4token, _1_token_LLoo__grammar)
else:
    #(_keyed_rgnrs4token, _token_LLoo__grammar, _token_LLoo__atom_rgnr_expr) = _1_main(_debug_=False, no_op=False)
    with timer(prefix='build:_1_token_LLoo__grammar@seed.recognize.recognizer_LLoo_.grammar...', _to_show_=_to_show4build_, _show_hint_on_enter_=True):
        (_1_fs, _1_tkeys4ignore, _1_sep4subkeying, _1_tkeys4subkeying, _1_keyed_rgnrs4token, _1_token_LLoo__grammar) = _1_main(_debug_=False, no_op=False)


#grammar = ???
    #py_expr = "&'py_expr:"  [< char'(' , char')' , regex'\w' >]  "'"
      # &'py_expr:(\w*)\(.*?\)\1'
      # eval
    #py_stmts = "&'py_stmts:"  [< char'(' , char')' , regex'\w' >]  "'"
      # exec
simplified_grammar4LLoo = (r'''
#simplified_grammar
#globals: (knm_set/{knm}, nm2rgnr/{nm:rgnr})
#;; grammar = line[0::1 :/ -".."]
;; grammar = line[0::1 ::// -".."]
    #bug-fixed:why? ok@『:/』but bug@『:://』{only output "grammar"}
    #   swap args:API_changed:mk_LLoo__end_by__post
;; line = (, -";;" , skip_case ?/ , -^- nm , postprocess[0::1] , -"=" , rgnr_expr ,) $& _mk_name_rgnr_pair
;; rgnr_expr = (, skip_case ?/ , -^- atom_rgnr_expr , postprocess[0::1] ,) $& _mk_rgnr__wrapper
;; atom_rgnr_expr =
    {>| nm8ref # $& _mk_rgnr__ref
    >| str8tkd # $& _mk_rgnr__tkd
    >| (, "{:|" , -^- , rgnr_expr[0::1 :% -":|"] , ":|}" ,) $& _mk_rgnr__parallel
    >| (, "{+:|" , -^- , rgnr_expr[0::1 :% -"+:|"] , "+:|}" ,) $& _mk_rgnr__parallel__tag
    >| (, "{*:|" , -^- , rgnr_expr[0::1 :% -"*:|"] , "*:|}" ,) $& _mk_rgnr__parallel__cased
    >| (, "{>|" , -^- , rgnr_expr[0::1 :% -">|"] , ">|}" ,) $& _mk_rgnr__choice
    >| (, "{+>|" , -^- , rgnr_expr[0::1 :% -"+>|"] , "+>|}" ,) $& _mk_rgnr__choice__tag
    >| (, "{*>|" , -^- , rgnr_expr[0::1 :% -"*>|"] , "*>|}" ,) $& _mk_rgnr__choice__cased
    >| (, "(," , -^- , yield_rgnr_expr[0::1 :% -","] , ",)" ,) $& _mk_rgnr__tuple
    >| (, "[<" , regex8char_set_query , -"," , regex8char_set_query , -"," , regex8char_set_query , ">]" ,) $& _mk_rgnr__raw_str
    >|}

;; yield_rgnr_expr =
    # ;; yield_rgnr_expr = (, "-^-" ?/ , -^- , rgnr_expr ?/ ,)
    {*>| (, -^- -"-^-"  , rgnr_expr ?/ ,) .!
    *>| rgnr_expr
    *>|}
;; skip_case =
    {>| "-"
    >| "..."
    >| "."
    >|}
;; sep_end_by =
    {>| (, ":%" , -^- , rgnr_expr ,)
    >| (, ":/" , -^- , rgnr_expr ,)
    >| (, ":://" , -^- , rgnr_expr ,)
    >|}
;; postprocess =
    {>| (, "[" , -^- , uint ?/ , ":" , uint ?/ , ":" , uint ?/ , sep_end_by ?/ , "]" ,)
    >| ".!"
    >| "~!"
    >| "^$"
    >| "^^"
    >| "!^"
    >| "!$"
    >| "?$"
    >| "?^"
    >| "?/"
    >| "?%"
    >| (, "$%" , -^- , nm4knm8f ,)
    >| (, "$&" , -^- , nm4knm8f ,)
    >| (, "$|" , -^- , nm4knm8f ,)
    >| (, ":*" , -^- , str ,)
    >| (, "?=" , -^- , py_expr ,)
    >| (, "$=" , -^- , py_expr ,)
    >| (, "$>" , -^- , py_expr ,)
    >| (, "$<" , -^- , py_expr ,)
    >| (, "$+" , -^- , py_expr ,)
    >| (, "$*" , -^- , py_expr ,)
    >|}

;; py_expr =
    {>| uint
    >| str
    # >| raw_str $& _mk4py_expr5raw_str
        #old-API:tokenize_()
    >| raw_str8py_expr $& _mk4py_expr5raw_str
        #new-API:tokenize_()
    >|}


;; regex8char_set_query = str $& _mk_char_set_query
;; nm4knm8f = nm $& _mk_knm8f
;; nm8ref = nm $& _mk_rgnr__ref
;; str8tkd = str $& _mk_rgnr__tkd

;; nm = "name" $& _get_payload
;; uint = "uint" $& _get_payload
;; str = "str" $& _get_payload
# ;; raw_str = "raw_str" $& _get_payload
    #old-API:tokenize_()
;; raw_str8py_expr = "raw_str-py_expr" $& _get_payload
    #new-API:tokenize_()

..

'''#'''
)#end-simplified_grammar
simplified_grammar4LLoo
class _data4simplified_grammar4LLoo:
    sgLLoo = simplified_grammar4LLoo
    keyed_rgnrs4token = _1_keyed_rgnrs4token
    tkeys4ignore = _1_tkeys4ignore
    sep4subkeying = _1_sep4subkeying
    tkeys4subkeying = _1_tkeys4subkeying
def tokenize4simplified_grammar4LLoo_(inputter4char, /, *, nonlazy=False
    ,keyed_rgnrs4token=_data4simplified_grammar4LLoo.keyed_rgnrs4token
    ,tkeys4ignore=_data4simplified_grammar4LLoo.tkeys4ignore
    ,sep4subkeying=_data4simplified_grammar4LLoo.sep4subkeying
    ,tkeys4subkeying=_data4simplified_grammar4LLoo.tkeys4subkeying
    ):
    'inputter4char -> inputter4token'
    #inputter4token = tokenize_(None, tkeys4ignore.__contains__, keyed_rgnrs4token, inputter4char)
    #new-API:tokenize_():
    #def tokenize_(may_exc_mkr_or_tailing_tkds6fail, tailing_tkds6eof, tkey2ignored_, tkey2stated_, sep4subkeying, tkey2subkeying_, st0, st2may_keyed_rgnrs4token, inputter, /, *, global_runtime_info=None, begin_idx4gap=0, nonlazy=False):
    inputter4token = tokenize_(may_exc_mkr_or_tailing_tkds6fail:=(), tailing_tkds6eof:=(), tkeys4ignore.__contains__, tkey2stated_:=lambda tkey1:False, sep4subkeying, tkeys4subkeying.__contains__, st0:=0, [keyed_rgnrs4token], inputter4char)
    return inputter4token

#def _2_main(keyed_rgnrs4token, token_LLoo__grammar, /):
####def _2_main(keyed_rgnrs4token, token_LLoo__grammar, /, *, token_LLoo__atom_rgnr_expr=_token_LLoo__atom_rgnr_expr):
####    from seed.recognize.recognizer_LLoo_.stream._common import mk_forkable_char_stream5txt# mk_forkable_char_stream5ipath, mk_forkable_char_stream5ifile, iter_char_tokens5ifile
####    if 0b0000:
####        simplified_grammar = r'(, ,)'
####        token_LLoo__grammar = token_LLoo__atom_rgnr_expr
####        if 0b0001:
####            token_LLoo__1 = mk_LLoo__tuple(1,
####            [mk_LLoo__match_constant_tkey('(,')
####            #,mk_LLoo__sep_by(mk_LLoo__match_constant_tkey(','), mk_LLoo__pack(mk_LLoo__match_constant_tkey('!!!!!!'), to_wrap=True))
####                #NOTE:『rgnr_expr-ref-lazy』==>>『to_wrap=True』
####            ,mk_LLoo__match_constant_tkey(',)')
####            ])
####        if 0b0001:
####            token_LLoo__grammar = token_LLoo__1
####                #ok
####            token_LLoo__grammar = mk_LLoo__the_first_one([mk_LLoo__match_constant_tkey('#'), token_LLoo__1, mk_LLoo__match_constant_tkey('#')])
####                #ok
####            token_LLoo__grammar = mk_LLoo__the_first_one([mk_LLoo__match_constant_tkey('#'), token_LLoo__1])
####                #not ok
####            token_LLoo__grammar = mk_LLoo__the_first_one([token_LLoo__1])
####                #not ok
    ##if 0b0000:
    ##    x = _test4parallel(token_LLoo__1, inputter4token)
    ##    if 0b0001:print(x)
    ##else:
    ##    reply4LLoo = parse__via_IRecognizerLLoo(token_LLoo__grammar, inputter4token)
    ##    if 0b0001:print(reply4LLoo)

#def _2_main(keyed_rgnrs4token, token_LLoo__grammar, /):
#def _2_main(*, _debug_, no_op):
#    (fs, keyed_rgnrs4token, token_LLoo__grammar) = _1_main(_debug_=False, no_op=False)
#def _2_main(fs, tkeys4ignore, keyed_rgnrs4token, token_LLoo__grammar, /, *, general_vs_specific):
def _2_main(fs, token_LLoo__grammar, /, *, general_vs_specific):
    from seed.recognize.recognizer_LLoo_.stream._common import mk_forkable_char_stream5txt
    ######################
    fs
    #tkeys4ignore
    #keyed_rgnrs4token
    token_LLoo__grammar
    fname = f'{__file__}::simplified_grammar4LLoo'
    grammar4xxx = simplified_grammar4LLoo
    ######################
    fs.reset()
    #bug:fs = fs.copy_and_reset()
        #since token_LLoo__grammar bind to fs
    with timer(prefix='build-nonlazy:inputter4char+inputter4token@seed.recognize.recognizer_LLoo_.grammar...', _to_show_=_to_show4build_, _show_hint_on_enter_=True):
        inputter4char = mk_forkable_char_stream5txt(..., fname, grammar4xxx)
        inputter4token = tokenize4simplified_grammar4LLoo_(inputter4char, nonlazy=_to_show4build_)
        #obsolete#def tokenize_(may__bad_reply2may_token_keyed_data8eof, is_tkey_ignored_, keyed_rgnrs4token, inputter, /, *, global_runtime_info=None):
        #inputter4token = tokenize_(None, tkeys4ignore.__contains__, keyed_rgnrs4token, inputter4char)
    reply4LLoo = parse__via_IRecognizerLLoo(token_LLoo__grammar, inputter4token)
    if not reply4LLoo.ok:
        raise RecognizationFail(reply4LLoo)
    oresult = reply4LLoo.oresult
    end_gap_position_info = reply4LLoo.the_inputter4end.tell_gap_position_info()
    (knm_set, nm2rgnr, register4scene, view4scene) = fs.detach()
    del fs
    if general_vs_specific is False:
        return (end_gap_position_info, oresult, knm_set, nm2rgnr, register4scene, view4scene)
    #######above:general but miss nm4knm8f
    #######below:specific{simplified_grammar4LLoo}, fill nm4knm8f
    _fs = _Bundle4referred_funcs4simplified_grammar4LLoo(_debug_=False)
    for knm in knm_set:
        if knm.kind is ICallable:
            #nm4knm8f
            _f = getattr(_fs, knm.name)
            register4scene.register(knm, _f)
    view4scene.detect_circle_ref()
        # ^LookupError__circle_ref
    missing_knms = view4scene.findout_all_missing_kinded_names()
    if missing_knms:
        for knm in missing_knms:
            assert expectError(LookupError, lambda:view4scene.dereference(knm))
        raise Error4IRecognizerLLoo(missing_knms, {*view4scene.iter_all_registered_kinded_names()}, {*nm2rgnr}, end_gap_position_info)
        raise Error4IRecognizerLLoo(missing_knms)
    _token_LLoo__grammar = nm2rgnr['grammar']

    return (_fs, _token_LLoo__grammar)
if __name__ == "__main__":
    from seed.recognize.recognizer_LLoo_.grammar import (_4_fs, _4_token_LLoo__grammar)
    pass
elif 0:
    (_oresult, _knm_set, _nm2rgnr, _register4scene, _view4scene) = _2_main(_1_fs, _1_keyed_rgnrs4token, _1_token_LLoo__grammar, general_vs_specific=False)
else:
    (_1_fs, _1_tkeys4ignore, _1_keyed_rgnrs4token, _1_token_LLoo__grammar)
    (_1_fs, _1_token_LLoo__grammar)
        #manually#handicraft

    with timer(prefix='build:_2_token_LLoo__grammar@seed.recognize.recognizer_LLoo_.grammar...', _to_show_=_to_show4build_, _show_hint_on_enter_=True):
        (_2_fs, _2_token_LLoo__grammar) = _2_main(_1_fs, _1_token_LLoo__grammar, general_vs_specific=True)
            #generated <-- handicraft

    with timer(prefix='build:_3_token_LLoo__grammar@seed.recognize.recognizer_LLoo_.grammar...', _to_show_=_to_show4build_, _show_hint_on_enter_=True):
        (_3_fs, _3_token_LLoo__grammar) = _2_main(_2_fs, _2_token_LLoo__grammar, general_vs_specific=True)
            #generated <-- generated <-- handicraft

    with timer(prefix='build:_4_token_LLoo__grammar@seed.recognize.recognizer_LLoo_.grammar...', _to_show_=_to_show4build_, _show_hint_on_enter_=True):
        (_4_fs, _4_token_LLoo__grammar) = _2_main(_3_fs, _3_token_LLoo__grammar, general_vs_specific=True)
            #generated <-- generated <-- generated <-- handicraft
            #final

    with timer(prefix='build:_5_token_LLoo__grammar@seed.recognize.recognizer_LLoo_.grammar...', _to_show_=_to_show4build_, _show_hint_on_enter_=True):
        (_5_fs, _5_token_LLoo__grammar) = _2_main(_4_fs, _4_token_LLoo__grammar, general_vs_specific=True)
            # _5_:testing:_4_token_LLoo__grammar

if not __name__ == "__main__":
    (_1_fs, _1_token_LLoo__grammar)
        #manually#handicraft
    (_2_fs, _2_token_LLoo__grammar)
        #generated <-- handicraft
    (_3_fs, _3_token_LLoo__grammar)
        #generated <-- generated <-- handicraft
    (_4_fs, _4_token_LLoo__grammar)
        #generated <-- generated <-- generated <-- handicraft
        #final
    if 1:
        (_5_fs, _5_token_LLoo__grammar)
            # _5_:testing:_4_token_LLoo__grammar

from seed.recognize.recognizer_LLoo_.grammar import \
(_4_fs as bundle4referred_funcs4simplified_grammar4LLoo
,_1_tkeys4ignore as ignored_tkeys4tokenize4simplified_grammar4LLoo
,_1_tkeys4subkeying as subkeying_tkeys4tokenize4simplified_grammar4LLoo
,_1_sep4subkeying as subkeying_sep4tokenize4simplified_grammar4LLoo
,_1_keyed_rgnrs4token as keyed_char_LLoos4tokenize4simplified_grammar4LLoo
,_4_token_LLoo__grammar as token_LLoo__grammar4simplified_grammar4LLoo
)
from seed.recognize.recognizer_LLoo_.grammar import bundle4referred_funcs4simplified_grammar4LLoo, keyed_char_LLoos4tokenize4simplified_grammar4LLoo, token_LLoo__grammar4simplified_grammar4LLoo
from seed.recognize.recognizer_LLoo_.grammar import ignored_tkeys4tokenize4simplified_grammar4LLoo, subkeying_sep4tokenize4simplified_grammar4LLoo, subkeying_tkeys4tokenize4simplified_grammar4LLoo


def mk_recognizer_LLoo5grammar__(may_bundle4referred_funcs4grammar4xxx, fname, grammar4xxx, /, *, bundle_incomplete=False):
    'may IBundle4referred_funcs4grammar -> fname/str -> grammar4xxx/str -> (end_gap_position_info/IPositionInfo4Gap, register4scene/IScene__register, view4scene/IScene, knm_set/{KindedName}, nm2rgnr/{nm:token_LLoo<nm>}) #see:seed.recognize.recognizer_LLoo_.tokenize.tokenize_()'
    'grammar4xxx is short to be loaded in text-form'
    check_may_([check_type_le, IBundle4referred_funcs4grammar], may_bundle4referred_funcs4grammar4xxx)
    check_type_is(str, fname)
    check_type_is(str, grammar4xxx)
    check_type_is(bool, bundle_incomplete)
    ######################
    from seed.recognize.recognizer_LLoo_.stream._common import mk_forkable_char_stream5txt
    ######################
    fs = bundle4referred_funcs4simplified_grammar4LLoo
    tkeys4ignore = ignored_tkeys4tokenize4simplified_grammar4LLoo
    tkeys4subkeying = subkeying_tkeys4tokenize4simplified_grammar4LLoo
    sep4subkeying = subkeying_sep4tokenize4simplified_grammar4LLoo
    keyed_rgnrs4token = keyed_char_LLoos4tokenize4simplified_grammar4LLoo
    token_LLoo__grammar = token_LLoo__grammar4simplified_grammar4LLoo
    fname
    grammar4xxx
    tokenize4simplified_grammar4LLoo_
    ######################
    tokenize4simplified_grammar4LLoo_
    ######################
    fs.reset()
    #bug:fs = fs.copy_and_reset()
        #since token_LLoo__grammar bind to fs
    inputter4char = mk_forkable_char_stream5txt(..., fname, grammar4xxx)
    inputter4token = tokenize4simplified_grammar4LLoo_(inputter4char)
        #obsolete#def tokenize_(may__bad_reply2may_token_keyed_data8eof, is_tkey_ignored_, keyed_rgnrs4token, inputter, /, *, global_runtime_info=None):
        #inputter4token = tokenize_(None, tkeys4ignore.__contains__, keyed_rgnrs4token, inputter4char)
    reply4LLoo = parse__via_IRecognizerLLoo(token_LLoo__grammar, inputter4token)
    if not reply4LLoo.ok:
        raise RecognizationFail(reply4LLoo)
    oresult = reply4LLoo.oresult
    end_gap_position_info = reply4LLoo.the_inputter4end.tell_gap_position_info()
    (knm_set, nm2rgnr, register4scene, view4scene) = fs.detach()
    del fs
    #######fill nm4knm8f
    if not None is (_fs := may_bundle4referred_funcs4grammar4xxx):
        _fs
        for knm in knm_set:
            if knm.kind is ICallable:
                #nm4knm8f
                _f = getattr(_fs, knm.name)
                check_type_le(ICallable, _f)
                register4scene.register(knm, _f)
    if not None is _fs and not bundle_incomplete:
        view4scene.detect_circle_ref()
            # ^LookupError__circle_ref
        missing_knms = view4scene.findout_all_missing_kinded_names()
        if missing_knms:
            for knm in missing_knms:
                assert expectError(LookupError, lambda:view4scene.dereference(knm))
            raise Error4IRecognizerLLoo(missing_knms, {*view4scene.iter_all_registered_kinded_names()}, {*nm2rgnr}, end_gap_position_info)
            raise Error4IRecognizerLLoo(missing_knms)
    return (end_gap_position_info, register4scene, view4scene, knm_set, nm2rgnr)
if not __name__ == "__main__":
    (_end_gap_position_info, _register4scene, _view4scene, _knm_set, _nm2rgnr) = mk_recognizer_LLoo5grammar__(bundle4referred_funcs4simplified_grammar4LLoo, f'{__file__}::simplified_grammar4LLoo', simplified_grammar4LLoo)


__all__
from seed.recognize.recognizer_LLoo_.grammar import mk_recognizer_LLoo5grammar__, IBundle4referred_funcs4grammar
from seed.recognize.recognizer_LLoo_.grammar import *
