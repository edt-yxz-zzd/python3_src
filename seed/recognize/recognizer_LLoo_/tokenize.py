#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/recognizer_LLoo_/tokenize.py

seed.recognize.recognizer_LLoo_.tokenize
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_LLoo_.tokenize -x
py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LLoo_.tokenize:__doc__ -ht
py_adhoc_call   seed.recognize.recognizer_LLoo_.tokenize   @f
#]]]'''
__all__ = r'''
tokenize_
    iter4tokenize_


Signal__EOF4Tokenization
BaseTokenizationError
    TokenizationFail
ITokenizationFramework
    ITokenizer__stated
        Tokenizer__stated__subkeying




is_tkds
check_tkds
check__st2may_keyed_rgnrs4token
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.recognize.recognizer_LLoo_._common import (Cased
,check_non_ABC
,check_may_, check_not_
,check_type_is, check_type_le, check_int_ge
,ICallable, IHashable
,abstractmethod, override, ABC, ABC__no_slots
,repr_helper, _Base4repr #sf._args4repr = (...)
)


from seed.types.ForkableForwardInputStream import IForkableForwardInputStream, ForkableForwardInputStream__using_LazyListIter
    #def __init__(sf, global_runtime_info, prev_token_end_gap_position_info, lazylist_iter, /):
from seed.types.IToken import Token__keyed, PositionInfo4Span, PositionInfo4Gap__higher_level

from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import IRecognizerLLoo
from seed.recognize.recognizer_LLoo_.combinator_LLoo__wrapper import mk_LLoo__Cased#_6oresult_only_
from seed.recognize.recognizer_LLoo_.combinator_LLoo__parallel import mk_LLoo__the_first_one
from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import parse__via_IRecognizerLLoo

from seed.types.LazyList import to_LazyListIter
from seed.tiny_.verify import is_iterator, is_reiterable
from seed.tiny_.check import check_subscriptable, check_pair

___end_mark_of_excluded_global_names__0___ = ...
def __obsolete():
  def tokenize_(may__bad_reply2may_token_keyed_data8eof, is_tkey_ignored_, keyed_rgnrs4token, inputter, /, *, global_runtime_info=None):
    '(may (tgbegin -> reply4LLoo{not .ok} -> may tkd/Cased | ^Exception)|Exception) -> (tkey -> ignored/bool) -> [(tkey,rgnr{oresult as tdat})] -> IForkableForwardInputStream{low_level_token} -> IForkableForwardInputStream{high_level_token | ^TokenizationFail}'
    #global_runtime_info = inputter.global_runtime_info
    tgend4low_lvl = inputter.tell_gap_position_info()
    tgend = PositionInfo4Gap__higher_level(tgend4low_lvl, 0)
    it = iter4tokenize_(may__bad_reply2may_token_keyed_data8eof, is_tkey_ignored_, keyed_rgnrs4token, inputter)
    return ForkableForwardInputStream__using_LazyListIter(global_runtime_info, tgend, to_LazyListIter(it))
  def iter4tokenize_(may__bad_reply2may_token_keyed_data8eof, is_tkey_ignored_, keyed_rgnrs4token, inputter, /):
    '(may (tgbegin -> reply4LLoo{not .ok} -> may tkd/Cased | ^Exception)|Exception) -> (tkey -> ignored/bool) -> [(tkey,rgnr{oresult as tdat})] -> IForkableForwardInputStream{low_level_token} -> Iter (high_level_token/IToken | ^TokenizationFail)'
    #tkeys4ignore = frozenset(tkeys4ignore)
    _6oresult_only_ = True
    rgnr4token = mk_LLoo__the_first_one(mk_LLoo__Cased(tkey, rgnr, _6oresult_only_=_6oresult_only_) for tkey, rgnr in keyed_rgnrs4token)
    m = may__bad_reply2may_token_keyed_data8eof
    tgend4low_lvl = inputter.tell_gap_position_info()
    tgend = PositionInfo4Gap__higher_level(tgend4low_lvl, idx4gap:=0)
    while not inputter.eof:
        tgbegin = tgend
        reply4LLoo = parse__via_IRecognizerLLoo(rgnr4token, inputter)
        inputter = reply4LLoo.the_inputter4end
        tgend4low_lvl = inputter.tell_gap_position_info()
        idx4gap += 1
        tgend = PositionInfo4Gap__higher_level(tgend4low_lvl, idx4gap)
        tspan = PositionInfo4Span(tgbegin, tgend)
        ######################
        if not reply4LLoo.ok:
            msg = (reply4LLoo.errmsg, tgbegin, tgend)
            if m is None:
                pass
            elif isinstance(m, type) and issubclass(m, Exception):
                Err = m
                raise Err(msg)
            elif isinstance(m, Exception):
                exc = m
                raise exc
            else:
                f = m
                may_tkd = f(tgbegin, reply4LLoo)
                    # ^Exception
                if may_tkd is None:
                    pass
                else:
                    tkd = may_tkd
                    check_type_le(Cased, tkd)
                    token8eof = Token__keyed(tspan, tkd)
                    yield token8eof
            return
        ######################
        assert reply4LLoo.ok
        ######################
        oresult = reply4LLoo.oresult
        tkd = oresult
        check_type_is(Cased, tkd)
        token = Token__keyed(tspan, tkd)
        #if not token.token_key in tkeys4ignore:
        if not is_tkey_ignored_(token.token_key):
            yield token
        continue
        ######################
    return
#end-def __obsolete():


class Signal__EOF4Tokenization(BaseException):pass
class BaseTokenizationError(Exception):pass
class TokenizationFail(BaseTokenizationError):pass
class ITokenizationFramework(ABC):
    r'''[[[
    tokenize :: [low_level_token] -> [high_level_token]

    ##custom_1 :: high_level_tkd -> may high_level_tkd
    custom_1 :: high_level_tkd -> Iter (high_level_tkd | ^Signal__EOF4Tokenization | ^TokenizationFail)
        feature:
            * filter out noise high_level_token #eg:space, comment
            * rekeying,subkeying:refine tkey/token_key
            * tokenize prefix only

    ##custom_2 :: tgbegin{not eof} -> reply4LLoo{not ok} -> (may high_level_tkd | ^TokenizationFail) #for token8eof
    custom_2 :: tgbegin{not eof} -> reply4LLoo{not ok} -> Iter (high_level_tkd | ^Signal__EOF4Tokenization | ^TokenizationFail) #for tailing_tokens
        feature:
            * raise at fail
            * tokenize prefix only and save tail inputter@tgend#using mk_LLoo__try__rollback_if_fail_before_hdr_sgnl_else_lift

    custom_3 :: inputter{eof} -> Iter (high_level_tkd | ^Signal__EOF4Tokenization | ^TokenizationFail) #for tailing_tokens

    #]]]'''#'''
    __slots__ = ()
    ######################
    @abstractmethod
    def _mk_context4tokenization_(sf, inputter, /):
        'inputter.fork()/IForkableForwardInputStream{low_level_token} -> ctx #for:state<ctx> #["inputter" for global_runtime_info]'
    @abstractmethod
    def _may_rgnr5ctx4tokenization_(sf, ctx, /):
        'ctx -> may rgnr/IRecognizerLLoo #stated:rgnr<state<ctx> > #stop if None'
    @abstractmethod
    def _raise_or_iter_tailing_tkds6eof4tokenization_(sf, ctx, tspan4eof, inputter, /):
        'ctx -> tspan4eof/IPositionInfo4Span -> inputter{eof}[#without .fork()#] -> Iter (high_level_tkd | ^Signal__EOF4Tokenization | ^TokenizationFail) #for tailing_tokens #custom_3'
    @abstractmethod
    def _raise_or_iter_tailing_tkds6fail4tokenization_(sf, ctx, rgnr, tspan, reply4LLoo, /):
        'ctx -> rgnr/IRecognizerLLoo -> tspan{tgbegin not eof}/IPositionInfo4Span -> reply4LLoo<rgnr>{not ok} -> Iter (high_level_tkd | ^Signal__EOF4Tokenization | ^TokenizationFail) #for tailing_tokens #custom_2'
    @abstractmethod
    def _mk_auxiliary5oresult4tokenization_(sf, ctx, rgnr, oresult, /):
        'ctx -> rgnr/IRecognizerLLoo -> oresult<reply4LLoo<rgnr> > -> auxiliary'
    @abstractmethod
    def _iter_tkds5oresult4tokenization_(sf, ctx, rgnr, oresult, auxiliary, /):
        'ctx -> rgnr/IRecognizerLLoo -> oresult<reply4LLoo<rgnr> > -> auxiliary -> Iter (high_level_tkd/tkd/token_keyed_data/Cased | ^Signal__EOF4Tokenization | ^TokenizationFail) #custom_1'
    @abstractmethod
    def _update_ctx4tokenization_(sf, ctx, rgnr, oresult, auxiliary, inputter, /):
        'ctx -> rgnr/IRecognizerLLoo -> oresult<reply4LLoo<rgnr> > -> auxiliary -> inputter.fork()/IForkableForwardInputStream{low_level_token} -> ctx #["inputter" for global_runtime_info]'


    ######################

    def tokenize_(sf, inputter, /, *, global_runtime_info=None, begin_idx4gap=0, nonlazy=False):
        'IForkableForwardInputStream{low_level_token} -> IForkableForwardInputStream{high_level_token | ^TokenizationFail}'
        #global_runtime_info = inputter.global_runtime_info
        it = sf.iter4tokenize_(inputter, begin_idx4gap=begin_idx4gap, to_yield_leading_gap=True)
        if not is_iterator(it):raise TypeError(type(it))
        assert iter(it) is it
        for tgend in it:
            #head
            break
        else:
            raise 000
        inputter4high_lvl = ForkableForwardInputStream__using_LazyListIter(global_runtime_info, tgend, to_LazyListIter(it))
        if nonlazy:
            for _ in iter(inputter4high_lvl.get_curr_lazylist()):pass
        return inputter4high_lvl


    def iter4tokenize_(sf, inputter, /, *, begin_idx4gap=0, to_yield_leading_gap=False):
        'IForkableForwardInputStream{low_level_token} -> Iter (high_level_token/IToken | ^TokenizationFail)'
        check_int_ge(0, begin_idx4gap)
        check_type_is(bool, to_yield_leading_gap)

        ######################
        stopped = False
        def tokens5lazy_tkds_(_tspan, lazy__tkds, /):
            '-> Iter (IToken | ^TokenizationFail) #[#set:"stopped","idx4gap"#]'
            nonlocal stopped, idx4gap, tspan, tgbegin, tgend
                #SyntaxError: name 'tspan' is parameter and nonlocal
            _idx4gap = idx4gap
            try:
                tkds = lazy__tkds()
                    #^Signal__EOF4Tokenization | ^TokenizationFail
                #assert iter(tkds) is tkds
                i = -1
                for i, tkd in enumerate(tkds):
                    #^Signal__EOF4Tokenization | ^TokenizationFail
                    check_type_is(Cased, tkd)
                    if not i==0:
                        if i==1:
                            _tgbegin = _tspan.end_gap_position_info
                            tgend4low_lvl = _tgbegin.low_lvl_gap
                                #immutable
                        else:
                            _tgbegin = _tgend
                        _tgbegin
                        tgend4low_lvl
                        #idx4gap += 1
                        _idx4gap += 1
                        _tgend = PositionInfo4Gap__higher_level(tgend4low_lvl, _idx4gap)
                        _tspan = PositionInfo4Span(_tgbegin, _tgend)
                    #end-if not i==0:
                    _tspan
                    token = Token__keyed(_tspan, tkd)
                    yield token
            except Signal__EOF4Tokenization:
                stopped = True
            if i >= 1:
                (idx4gap, tspan, tgbegin, tgend) = (_idx4gap, _tspan, _tgbegin, _tgend)
        #end-def tokens5lazy_tkds_(_tspan, lazy__tkds, /):
        ######################

        ctx = sf._mk_context4tokenization_(inputter.fork())
        tgend4low_lvl = inputter.tell_gap_position_info()
        tgend = PositionInfo4Gap__higher_level(tgend4low_lvl, idx4gap:=begin_idx4gap)
        if to_yield_leading_gap:
            yield tgend
        while not inputter.eof:
            tgbegin = tgend
            may_rgnr = sf._may_rgnr5ctx4tokenization_(ctx)
            if may_rgnr is None:
                #stop
                return
            rgnr = may_rgnr
                #rgnr4token
            reply4LLoo = parse__via_IRecognizerLLoo(rgnr, inputter)
            inputter = reply4LLoo.the_inputter4end
            tgend4low_lvl = inputter.tell_gap_position_info()
            idx4gap += 1
            tgend = PositionInfo4Gap__higher_level(tgend4low_lvl, idx4gap)
            tspan = PositionInfo4Span(tgbegin, tgend)
            ######################
            if not reply4LLoo.ok:
                #fail
                lazy__tailing_tkds6fail = lambda:sf._raise_or_iter_tailing_tkds6fail4tokenization_(ctx, rgnr, tspan, reply4LLoo) #custom_2
                yield from tokens5lazy_tkds_(tspan4fail:=tspan, lazy__tailing_tkds6fail)
                    #^TokenizationFail
                #if stopped: return
                return
            ######################
            assert reply4LLoo.ok
            ######################
            oresult = reply4LLoo.oresult
            auxiliary = sf._mk_auxiliary5oresult4tokenization_(ctx, rgnr, oresult)
            lazy__tkds = lambda:sf._iter_tkds5oresult4tokenization_(ctx, rgnr, oresult, auxiliary) #custom_1
            yield from tokens5lazy_tkds_(tspan, lazy__tkds)
                #^TokenizationFail
            if stopped: return
            ######################
            ctx = sf._update_ctx4tokenization_(ctx, rgnr, oresult, auxiliary, inputter.fork())
            continue
            ######################
        else:#@while
            #eof
            tg4eof = tgend
            #xxx:_tg4eof = tgend
            tgend4low_lvl = inputter.tell_gap_position_info()
            idx4gap += 1
            _tg4eof = PositionInfo4Gap__higher_level(tgend4low_lvl, idx4gap)
            tspan4eof = PositionInfo4Span(tg4eof, _tg4eof)
            lazy__tailing_tkds = lambda:sf._raise_or_iter_tailing_tkds6eof4tokenization_(ctx, tspan4eof, inputter) #.fork() #custom_3
            yield from tokens5lazy_tkds_(tspan4eof, lazy__tailing_tkds)
                #^TokenizationFail
            #if stopped: return
            return
        raise 000
        return


#end-class ITokenizationFramework(ABC):



class ITokenizer__stated(ITokenizationFramework):
    __slots__ = ()
    ######################
    @property
    @abstractmethod
    def _state0_(sf, /):
        '-> st'
    @abstractmethod
    def _may_rgnr5state_(sf, st, /):
        'st -> may rgnr/IRecognizerLLoo #stop if None'
    @property
    @abstractmethod
    def _tailing_tkds6eof_(sf, /):
        '-> tailing_tkds6eof/[tkd]'
    @property
    @abstractmethod
    def _may_exc_mkr_or_tailing_tkds6fail_(sf, /):
        '-> (may exc_mkr/(msg -> TokenizationFail) | tailing_tkds6fail/[tkd])'

    @abstractmethod
    def _mk_auxiliary5stated_oresult_(sf, st, rgnr, oresult, /):
        'st -> rgnr/IRecognizerLLoo -> oresult<reply4LLoo<rgnr> > -> auxiliary'
    @abstractmethod
    def _iter_tkds5stated_oresult_(sf, st, rgnr, oresult, auxiliary, /):
        'st -> rgnr/IRecognizerLLoo -> oresult<reply4LLoo<rgnr> > -> auxiliary -> Iter (high_level_tkd/tkd/token_keyed_data/Cased | ^Signal__EOF4Tokenization | ^TokenizationFail) #custom_1'
    @abstractmethod
    def _update_state_(sf, st, rgnr, oresult, auxiliary, /):
        'st -> rgnr/IRecognizerLLoo -> oresult<reply4LLoo<rgnr> > -> auxiliary -> st'

    ######################
    def _mk_ctx5st_(sf, st, /):
        'st -> ctx'
        may_rgnr = sf._may_rgnr5state_(st)
        ctx = (st, may_rgnr)
        return ctx
    ######################
    @override
    def _mk_context4tokenization_(sf, inputter, /):
        'inputter.fork()/IForkableForwardInputStream{low_level_token} -> ctx #for:state<ctx> #["inputter" for global_runtime_info]'
        st = sf._state0_
        ctx = sf._mk_ctx5st_(st)
        return ctx
    @override
    def _may_rgnr5ctx4tokenization_(sf, ctx, /):
        'ctx -> may rgnr/IRecognizerLLoo #stated:rgnr<state<ctx> > #stop if None'
        (st, may_rgnr) = ctx
        return may_rgnr
    @override
    def _raise_or_iter_tailing_tkds6eof4tokenization_(sf, ctx, tspan4eof, inputter, /):
        'ctx -> tspan4eof/IPositionInfo4Span -> inputter{eof}[#without .fork()#] -> Iter (high_level_tkd | ^Signal__EOF4Tokenization | ^TokenizationFail) #for tailing_tokens #custom_3'
        yield from sf._tailing_tkds6eof_
        return
    @override
    def _raise_or_iter_tailing_tkds6fail4tokenization_(sf, ctx, rgnr, tspan, reply4LLoo, /):
        'ctx -> rgnr/IRecognizerLLoo -> tspan{tgbegin not eof}/IPositionInfo4Span -> reply4LLoo<rgnr>{not ok} -> Iter (high_level_tkd | ^Signal__EOF4Tokenization | ^TokenizationFail) #for tailing_tokens #custom_2'
        x = sf._may_exc_mkr_or_tailing_tkds6fail_
        if x is None:
            exc_mkr = TokenizationFail
        elif callable(x):
            exc_mkr = x
        else:
            tailing_tkds6fail = x
            yield from tailing_tkds6fail
            return
        (st, may_rgnr) = ctx
        msg = (st, reply4LLoo.errmsg, tspan)
        raise exc_mkr(msg)
    @override
    def _mk_auxiliary5oresult4tokenization_(sf, ctx, rgnr, oresult, /):
        'ctx -> rgnr/IRecognizerLLoo -> oresult<reply4LLoo<rgnr> > -> auxiliary'
        (st, may_rgnr) = ctx
        return sf._mk_auxiliary5stated_oresult_(st, rgnr, oresult)
    @override
    def _iter_tkds5oresult4tokenization_(sf, ctx, rgnr, oresult, auxiliary, /):
        'ctx -> rgnr/IRecognizerLLoo -> oresult<reply4LLoo<rgnr> > -> auxiliary -> Iter (high_level_tkd/tkd/token_keyed_data/Cased | ^Signal__EOF4Tokenization | ^TokenizationFail) #custom_1'
        (st, may_rgnr) = ctx
        it = sf._iter_tkds5stated_oresult_(st, rgnr, oresult, auxiliary)
        return it
    @override
    def _update_ctx4tokenization_(sf, ctx, rgnr, oresult, auxiliary, inputter, /):
        'ctx -> rgnr/IRecognizerLLoo -> oresult<reply4LLoo<rgnr> > -> auxiliary -> inputter.fork()/IForkableForwardInputStream{low_level_token} -> ctx #["inputter" for global_runtime_info]'
        (st, may_rgnr) = ctx
        _st = sf._update_state_(st, rgnr, oresult, auxiliary)
        _ctx = ctx if _st is st else sf._mk_ctx5st_(_st)
        return _ctx


    ######################
#end-class ITokenizer__stated(ITokenizationFramework):


def is_tkds(tkds, /):
    return (is_reiterable(tkds) and all(T is Cased for T in map(type, tkds)))
def check_tkds(tkds, /):
    if not is_reiterable(tkds):raise TypeError(type(tkds))
    for tkd in tkds:
        #check_type_is(Cased, tkd)
        check_type_le(Cased, tkd)

def check__st2may_keyed_rgnrs4token(st2may_keyed_rgnrs4token, /):
    check_subscriptable(st2may_keyed_rgnrs4token)
    items = iter(st2may_keyed_rgnrs4token.items() if hasattr(st2may_keyed_rgnrs4token, 'items') else enumerate(st2may_keyed_rgnrs4token))
    for st, m in items:
        if not st2may_keyed_rgnrs4token[st] is m:raise LookupError(st)
        if m is None:
            continue
        keyed_rgnrs4token = m
        if not is_reiterable(keyed_rgnrs4token):raise TypeError(type(keyed_rgnrs4token))
        len(keyed_rgnrs4token)
            # ^TypeError
        for x in keyed_rgnrs4token:
            check_pair(x)
        for tkey0, rgnr4tdat in keyed_rgnrs4token:
            check_type_is(str, tkey0)
            check_type_le(IRecognizerLLoo, rgnr4tdat)
class Tokenizer__stated__subkeying(ITokenizer__stated, _Base4repr):
    r'''[[[
    subkeying
    mk_LLoo__the_first_one
    [tkey/high_level_tkey :: str]

    [st2may_keyed_rgnrs4token :: {st:may keyed_rgnrs4token}]
    [st0 :: st]
    [tkey0 := tkey{before subkeying}]
    [tkey1 := tkey{after subkeying}]
    [tkey := tkey1]
    [keyed_rgnrs4token :: [(tkey0, rgnr4tdat/IRecognizerLLoo)]]
    [(tkey0,rgnr4tdat) :<- keyed_rgnrs4token]:
        [tkd0 := oresult<rgnr4tdat>]
        [tkd0 :: Cased<tkey0,tdat0>]
        [tdat0 :: (Cased<subkey/str,tdat1> if tkey2subkeying_(tkey0) else tdat1)]
        [tkey1 == (f"{tkey0}{sep4subkeying}{subkey}" if tkey2subkeying_(tkey0) else tkey0)]
        [tdat1 == (Cased<next_state/st,tdat2> if tkey2stated_(tkey1) else tdat2)]
        [tdat := tdat2]
        #xxx:[@tkey -> [not (tkey2subkeying_(tkey) and tkey2stated_(tkey))]]

    [tkey2subkeying_ :: tkey0 -> bool]
    [sep4subkeying :: str]
    [tkey2stated_ :: tkey1 -> bool]
    [tkey2ignored_ :: tkey1 -> bool]

    #]]]'''#'''
    ___no_slots_ok___ = True
    def __init__(sf, may_exc_mkr_or_tailing_tkds6fail, tailing_tkds6eof, tkey2ignored_, tkey2stated_, sep4subkeying, tkey2subkeying_, st0, st2may_keyed_rgnrs4token, /):
        '(may (msg->TokenizationFail)|[tkd]) -> [tkd] -> (tkey1->bool) -> (tkey1->bool) -> str -> (tkey0->bool) -> st -> {st:may [(tkey0, rgnr4tdat/IRecognizerLLoo)]} -> None #[tkd::Cased][tkey0 := tkey{before subkeying}][tkey1 := tkey{after subkeying}]'
        ######################
        num_args = len(locals()) -1
        ######################
        if not ((__:=may_exc_mkr_or_tailing_tkds6fail) is None or callable(__) or None is check_tkds(__)):raise TypeError(type(__))
        check_tkds(tailing_tkds6eof)

        check_type_le(ICallable, tkey2ignored_)
        check_type_le(ICallable, tkey2stated_)
        check_type_is(str, sep4subkeying)
        check_type_le(ICallable, tkey2subkeying_)
        check_type_le(IHashable, st0)
        check__st2may_keyed_rgnrs4token(st2may_keyed_rgnrs4token)
        st2may_keyed_rgnrs4token[st0]
            # ^LookupError

        ######################
        args = (may_exc_mkr_or_tailing_tkds6fail, tailing_tkds6eof, tkey2ignored_, tkey2stated_, sep4subkeying, tkey2subkeying_, st0, st2may_keyed_rgnrs4token)
        assert len(args) == num_args

        sf._args4repr = args

        sf._st2rgnr4tkd = {}
            #cache
        ######################
        L0 = len(vars(sf))
        ######################
        sf._may_exc_mkr_or_tailing_tkds6fail = may_exc_mkr_or_tailing_tkds6fail
        sf._tailing_tkds6eof = tailing_tkds6eof
        sf._tkey2ignored = tkey2ignored_
        sf._tkey2stated = tkey2stated_
        sf._sep4subkeying = sep4subkeying
        sf._tkey2subkeying = tkey2subkeying_
        sf._st0 = st0
        sf._st2may_keyed_rgnrs4token = st2may_keyed_rgnrs4token
        ######################
        L1 = len(vars(sf))
        assert L1 - L0 == num_args
        ######################
    ######################
    @property
    @override
    def _state0_(sf, /):
        '-> st'
        return sf._st0
    @override
    def _may_rgnr5state_(sf, st, /):
        'st -> may rgnr/IRecognizerLLoo #stop if None'
        m = sf._st2rgnr4tkd.get(st)
        if not m is None:
            rgnr4tkd = m
            return rgnr4tkd
        m = sf._st2may_keyed_rgnrs4token[st]
            # ^LookupError
        if m is None:
            #not cache since halt immediately
            return None
        keyed_rgnrs4token = m
        _6oresult_only_ = True
        rgnr4tkd = mk_LLoo__the_first_one(mk_LLoo__Cased(tkey, rgnr4tdat, _6oresult_only_=_6oresult_only_) for tkey, rgnr4tdat in keyed_rgnrs4token)
        sf._st2rgnr4tkd[st] = rgnr4tkd
        return sf._may_rgnr5state_(st) #recur
    @property
    @override
    def _tailing_tkds6eof_(sf, /):
        '-> tailing_tkds6eof/[tkd]'
        return sf._tailing_tkds6eof
    @property
    @override
    def _may_exc_mkr_or_tailing_tkds6fail_(sf, /):
        '-> may_exc_mkr_or_tailing_tkds6fail/(may exc_mkr/(msg -> TokenizationFail) | tailing_tkds6fail/[tkd])'
        return sf._may_exc_mkr_or_tailing_tkds6fail

    @override
    def _mk_auxiliary5stated_oresult_(sf, st, rgnr, oresult, /):
        'st -> rgnr/IRecognizerLLoo -> oresult<reply4LLoo<rgnr> > -> auxiliary'
        check_type_is(Cased, oresult)
        (tkey0, tdat0) = tkd0 = oresult
        #next_st = st
        #xxxif (subkeying:=sf._tkey2subkeying(tkey)) and (stated:=sf._tkey2stated(tkey)):raise 000
        #elif subkeying:
        if (subkeying:=sf._tkey2subkeying(tkey0)):
            check_type_is(Cased, tdat0)
            (subkey, tdat1) = tdat0
            check_type_is(str, subkey)
            sep = sf._sep4subkeying
            tkey1 = f'{tkey0}{sep}{subkey}'
            tkey1, tdat1
            tkd1 = Cased(tkey1, tdat1)
        else:
            (tkey1, tdat1) = tkd1 = tkd0
        tkd1, tkey1, tdat1
        #elif stated:
        if (stated:=sf._tkey2stated(tkey1)):
            check_type_is(Cased, tdat1)
            (next_st, tdat2) = tdat1
            tkd2 = Cased(tkey1, tdat2)
        else:
            next_st = st
            tdat2 = tdat1
            tkd2 = tkd1
        tkd2, tkey1, tdat2
        next_st

        (tkey, tdat) = tkd = tkd2
        auxiliary = (next_st, tkd)
            #after subkeying
        return auxiliary
    @override
    def _iter_tkds5stated_oresult_(sf, st, rgnr, oresult, auxiliary, /):
        'st -> rgnr/IRecognizerLLoo -> oresult<reply4LLoo<rgnr> > -> auxiliary -> Iter (high_level_tkd/tkd/token_keyed_data/Cased | ^Signal__EOF4Tokenization | ^TokenizationFail) #custom_1'
        (next_st, tkd) = auxiliary
            #after subkeying
        (tkey1, tdat2) = tkd2 = tkd
        if not sf._tkey2ignored(tkey1):
            yield tkd
        return
    @override
    def _update_state_(sf, st, rgnr, oresult, auxiliary, /):
        'st -> rgnr/IRecognizerLLoo -> oresult<reply4LLoo<rgnr> > -> auxiliary -> st'
        (next_st, tkd) = auxiliary
            #after subkeying
        return next_st

    ######################
#end-class Tokenizer__stated__subkeying(ITokenizer__stated):



def tokenize_(may_exc_mkr_or_tailing_tkds6fail, tailing_tkds6eof, tkey2ignored_, tkey2stated_, sep4subkeying, tkey2subkeying_, st0, st2may_keyed_rgnrs4token, inputter, /, *, global_runtime_info=None, begin_idx4gap=0, nonlazy=False):
    '(may (msg->TokenizationFail)|[tkd]) -> [tkd] -> (tkey1->bool) -> (tkey1->bool) -> str -> (tkey0->bool) -> st -> {st:may [(tkey0, rgnr4tdat/IRecognizerLLoo)]} -> IForkableForwardInputStream{low_level_token} -> IForkableForwardInputStream{high_level_token | ^TokenizationFail} #[tkd::Cased][tkey0 := tkey{before subkeying}][tkey1 := tkey{after subkeying}]'
    tokenizer = Tokenizer__stated__subkeying(may_exc_mkr_or_tailing_tkds6fail, tailing_tkds6eof, tkey2ignored_, tkey2stated_, sep4subkeying, tkey2subkeying_, st0, st2may_keyed_rgnrs4token)
    inputter4high_lvl = tokenizer.tokenize_(inputter, begin_idx4gap=begin_idx4gap, global_runtime_info=global_runtime_info, nonlazy=nonlazy)
    return inputter4high_lvl
def iter4tokenize_(may_exc_mkr_or_tailing_tkds6fail, tailing_tkds6eof, tkey2ignored_, tkey2stated_, sep4subkeying, tkey2subkeying_, st0, st2may_keyed_rgnrs4token, inputter, /, *, begin_idx4gap=0, to_yield_leading_gap=False):
    '(may (msg->TokenizationFail)|[tkd]) -> [tkd] -> (tkey1->bool) -> (tkey1->bool) -> str -> (tkey0->bool) -> st -> {st:may [(tkey0, rgnr4tdat/IRecognizerLLoo)]} -> IForkableForwardInputStream{low_level_token} -> Iter (high_level_token/IToken | ^TokenizationFail) #[tkd::Cased][tkey0 := tkey{before subkeying}][tkey1 := tkey{after subkeying}]'
    tokenizer = Tokenizer__stated__subkeying(may_exc_mkr_or_tailing_tkds6fail, tailing_tkds6eof, tkey2ignored_, tkey2stated_, sep4subkeying, tkey2subkeying_, st0, st2may_keyed_rgnrs4token)
    it = tokenizer.iter4tokenize_(inputter, begin_idx4gap=begin_idx4gap, to_yield_leading_gap=to_yield_leading_gap)
    return it

__all__
from seed.recognize.recognizer_LLoo_.tokenize import tokenize_, iter4tokenize_
from seed.recognize.recognizer_LLoo_.tokenize import (Signal__EOF4Tokenization
,BaseTokenizationError
,    TokenizationFail
,ITokenizationFramework
,    ITokenizer__stated
,        Tokenizer__stated__subkeying
)

from seed.recognize.recognizer_LLoo_.tokenize import *
