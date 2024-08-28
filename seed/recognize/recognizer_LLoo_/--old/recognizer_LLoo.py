#__all__:goto
e ../../python3_src/seed/recognize/interface_LLoo.py


r'''[[[
mkdir ../../python3_src/seed/recognize/recognizer_LLoo_
py_tpl ../../python3_src/seed/recognize/recognizer_LLoo_/interface_LLoo.py
mv -iv ../../python3_src/seed/recognize/interface_LLoo.py ../../python3_src/seed/recognize/recognizer_LLoo_/interface_LLoo.py
e ../../python3_src/seed/recognize/recognizer_LLoo_/interface_LLoo.py

#]]]'''#'''
ref to maker instead of recognizer since factory ~= maker
    ref to maker
        ref to recognizer
    ref to callable
        ref to postprocess6ok
        ref to postprocess
    ref to obj
        ref to constant/param
        ref to state/global_output_collector

refactor:iter4two_phases_recognize() using halfway_result#BoxedHalfwayResult
r'''[[[
e ../../python3_src/seed/recognize/recognizer_LLoo.py
view ../../python3_src/seed/func_tools/recur5yield.py
    generator_iterator :: IGeneratorIterator<iter-exprlist5yield, return-return_value5child>
    generator_func(*args4gi_mkr, **kwds4gi_mkr) -> generator_iterator
        main_generator_func(*args4main, **kwds4main) -> generator_iterator
        child_gi_protocol(exprlist5yield) -> generator_iterator


[[
LLoo ~= LL(+oo;)
    vivi LL1
using IForkableForwardInputStream
    # has no 『.seek()』
two phases:
    1. recognize header, declare to stick into current branch/choice/alternate
    2. continue to recognize whole

]]
[[
++collector_ops:for:
    mk__serial
    mk__many___
    mk__skip_many1
    mk__end_by___
    mk__sep_by___
    mk__sep_end_by___
mk__wrapper4postprocess6ok
    IUnpackIter4OkResult4LLoo
ICollectorOps:
    mk_empty
    puts :: Result4IRecognizerLLoo<errmsg,IUnpackIter4OkResult4LLoo> -> None
    finalize_collect
]]


######################
from seed.func_tools.recur5yield import bind_gi_with_the_following_first_value4send, mk_gi4either8xresult, mk_gi4xresult_xexception
from seed.func_tools.recur5yield import BoxedHalfwayResult, BoxedException__halfway, BoxedException__final, Escaped, BoxedTailRecur, BoxedFinalResult
from seed.func_tools.recur5yield import EFlowControl, EFinal, EHalfway, mk_boxed_EFinal, mk_boxed_EHalfway
from seed.func_tools.recur5yield import recur5yield__list__echo__echo
### from seed.types.Either import Either
######################






seed.recognize.recognizer_LLoo
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_LLoo -x
py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LLoo:__doc__ -ht
py_adhoc_call   seed.recognize.recognizer_LLoo   @f
from seed.recognize.recognizer_LLoo import *
#]]]'''
__all__ = r'''
'''.split()#'''
__all__

from itertools import count as count_ #islice

>>> from seed.types.Either import Either
>>> from seed.func_tools.recur5yield import BoxedHalfwayResult, mk_gi4either8xresult, bind_gi_with_the_following_first_value4send
>>> from seed.func_tools.recur5yield import recur5yield__list__echo__echo

from seed.types.ForkableForwardInputStream import IForkable, IForkableForwardInputStream, ForkableForwardInputStream__using_LazyListIter
from seed.func_tools.recur5yield import recur5yield__list__echo__echo
from seed.types.StackStyleSet import StackStyleSet# MultiSetStyleStack

from collections.abc import Generator as IGeneratorIterator #, Callable
from seed.tiny_.check import check_type_le, check_callable, check_either, check_pair, check_may_ # #check_getitemable, check_type_is,  #no check_tuple
from seed.tiny_.check import check_pseudo_qual_name, check_smay_pseudo_qual_name #check_pseudo_identifier, check_smay_pseudo_identifier
from seed.tiny_.check import check_type_is, check_int_ge
from seed.tiny import at, curry1, ifNone, echo, print_err, const

from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.helper.repr_input import repr_helper


def __():
    from seed.types.Symbol import PublicSymbol, mk_public_symbol, public_symbol5cls, P, getP
    @public_symbol5cls
    class Signal__HeaderCompleted:
        'IRecognizerLLoo found/recognized a complete header of current branch'
        pass

class Signal__HeaderCompleted:
    def __init__(sf, forkable8inputer4body, result4header, /):
        'forkable8inputer4body/IForkable'
        sf._st = forkable8inputer4body
        sf._r4hdr = result4header
    def __repr__(sf, /):
        return repr_helper(sf, sf._st, sf._r4hdr)
    @property
    def the_inputer4body(sf, /):
        '-> end_of_header/begin_of_body/IForkable'
        return sf._st
    @property
    def the_result4header(sf, /):
        '-> result4header'
        return sf._r4hdr

class Result4IRecognizerLLoo:
    #class RecognizeResult:
    def __init__(sf, forkable8inputer4end, err_vs_ok:bool, errmsg_or_result, /):
        'forkable8inputer4end/IForkable'
        sf._st = forkable8inputer4end
        check_type_is(bool, err_vs_ok)
        sf._ok = err_vs_ok
        sf._either = errmsg_or_result
    def __repr__(sf, /):
        return repr_helper(sf, sf._st, sf._ok, sf._either)

    @property
    def the_inputer4end(sf, /):
        '-> IForkable/(end_of_whole/end_of_body if sf.ok else begin_of_err)'
        return sf._st
    @property
    def ok(sf, /):
        '-> err_vs_ok/bool'
        return sf._ok
    @property
    def errmsg_or_result(sf, /):
        '-> errmsg_or_result/(errmsg if not sf.ok else result)'
        return sf._either
    @property
    def errmsg(sf, /):
        '-> (errmsg if not sf.ok else ^AttributeError)'
        if sf.ok:
            raise AttributeError('errmsg@ok')
        return sf._either
    @property
    def result(sf, /):
        '-> (result if sf.ok else ^AttributeError)'
        if not sf.ok:
            raise AttributeError('result@not_ok')
        return sf._either


class Error4IRecognizerLLoo(Exception):pass
class LookupError__circle_ref(LookupError):pass

default_implemented_abstractmethod = abstractmethod
class IFactory4CommonCombinators4IRecognizerLLoo(ABC):
    r'''[[[
    'factory4combinators&&closure4recognizer_ref&&register4named_recognizer'
    global_recur_break vs local_recur_break
        * global_recur_break:using:
            IRecognizerLLoo__ref
            .dereference()
            +++
            .register()
            IRecognizerLLoo__named
            .register__named()
        * local_recur_break:using:
            IRecognizerLLoo__lazy_wrapper
                IRecognizerLLoo__lazy_wrapper.unlazy()
    #]]]'''#'''
    __slots__ = ()
    @abstractmethod
    def tracing(sf, forkable8inputer, msg, /):
        '-> None #logging...'
        print_err(msg)
    @abstractmethod
    def register(sf, nm, recognizer_LLoo, /):
        'nm/(hashable&&immutable) -> IRecognizerLLoo -> None | ^KeyError'
        check_type_le(IRecognizerLLoo, recognizer_LLoo)
    @abstractmethod
    def _lookup_(sf, nm, /):
        r'nm/(hashable&&immutable) -> IRecognizerLLoo | ^KeyError'
    def dereference(sf, nm, /):
        r'nm/(hashable&&immutable) -> until:IRecognizerLLoo\-\IRecognizerLLoo__ref | ^KeyError | ^LookupError__circle_ref'
        s = StackStyleSet()
        for sz in count_(1):
            s.add(nm)
            if not len(s) == sz:
                ls = [*s]
                j = ls.index(nm)
                ls.applied(nm)
                leadings = ls[:j]
                circle = ls[j:]
                circle.append(nm)
                raise LookupError__circle_ref(leadings, circle)
            recognizer_LLoo = sf._lookup_(nm)
                # ^KeyError
            if isinstance(recognizer_LLoo, IRecognizerLLoo__ref):
                ref = recognizer_LLoo
                nm = ref.its_name
                continue
            else:
                check_type_le(IRecognizerLLoo, recognizer_LLoo)
                break
            raise 000
        return recognizer_LLoo


    def register__named(sf, named_recognizer_LLoo, /):
        'nm/(hashable&&immutable) -> IRecognizerLLoo__named -> None | ^KeyError'
        check_type_le(IRecognizerLLoo__named, named_recognizer_LLoo)
        nm = named_recognizer_LLoo.my_name
        sf.register(nm, named_recognizer_LLoo)
    def mk_and_register__named(sf, nm, recognizer_LLoo, /):
        r'-> IRecognizerLLoo__named | ^KeyError'
        named_recognizer_LLoo = sf.mk__named(nm, recognizer_LLoo)
        sf.register__named(named_recognizer_LLoo)
        return named_recognizer_LLoo



    ######################
    ######################
    # /#@abstractmethod\(\n    @default_implemented_abstractmethod\n\)\@!
    # /[^#]@abstractmethod\(\n    @default_implemented_abstractmethod\n\)\@=
    ######################
    #@abstractmethod
    @default_implemented_abstractmethod
    def mk__ref(sf, nm, /):
        r'-> IRecognizerLLoo__ref'
        return RecognizerLLoo__ref(nm)
    #@abstractmethod
    @default_implemented_abstractmethod
    def mk__named(sf, nm, recognizer_LLoo, /):
        r'-> IRecognizerLLoo__named'
        return RecognizerLLoo__named_wrapper(nm, recognizer_LLoo, repr_by_name=True)

    #@abstractmethod
    @default_implemented_abstractmethod
    def mk__lazy_wrapper(sf, lazy__recognizer_LLoo, /):
        r'(() -> IRecognizerLLoo) -> IRecognizerLLoo__lazy_wrapper' \
        r'''
        ===
        usage:
            def _lazy():
                return local__recognizer_LLoo
            _local = factory4combinators.mk__lazy_wrapper(_lazy)
            _branch4recur = factory4combinators.mk__serial([header], [], [_local])
            local__recognizer_LLoo = factory4combinators.mk__choice__the_first_one([_branch4basic, _branch4recur])
            _local.unlazy()
            del _lazy, _local, _branch4recur
        ===
        '''#'''
        return RecognizerLLoo__lazy_wrapper(lazy__recognizer_LLoo)

    ######################
    ######################
    ######################
    @abstractmethod
    def mk__serial(sf, recognizers4header, recognizers4sgnl_if_consumed, recognizers4body, /):
        r'-> IRecognizerLLoo # [header==recognizers4header++recognizers4sgnl_if_consumed[:j4sgnl_at_consumed]] # [body==recognizers4sgnl_if_consumed[j4sgnl_at_consumed:]++recognizers4body]'
        #return RecognizerLLoo__serial
    @abstractmethod
    def mk__parallel__the_only_one(sf, recognizers, /):
        r'-> IRecognizerLLoo'
        #return RecognizerLLoo__parallel__the_only_one
    @abstractmethod
    def mk__choice__the_first_one(sf, recognizers, /):
        r'-> IRecognizerLLoo'
        #return RecognizerLLoo__choice__the_first_one
    @abstractmethod
    def mk__any_token(sf, /):
        r'-> IRecognizerLLoo'
        #return RecognizerLLoo__any_token
    #@abstractmethod
    @default_implemented_abstractmethod
    def mk__eof(sf, /):
        r'-> IRecognizerLLoo'
        return sf.mk__not_followed_by(sf.mk__any_token())
    #@abstractmethod
    @default_implemented_abstractmethod
    def mk__not_followed_by(sf, recognizer_LLoo, /):
        r'-> IRecognizerLLoo'
        return sf.mk__look_ahead(sf.mk__invert_err_ok(recognizer_LLoo))
    @abstractmethod
    def mk__invert_err_ok(sf, recognizer_LLoo, /):
        r'-> IRecognizerLLoo'
        return RecognizerLLoo__invert_err_ok(recognizer_LLoo)
        reformer4LLoo = the_reformer4LLoo__invert_err_ok
        return RecognizerLLoo__reform_wrapper(reformer4LLoo, recognizer_LLoo)
    @abstractmethod
    def mk__look_ahead(sf, recognizer_LLoo, /):
        r'-> IRecognizerLLoo'
        #return RecognizerLLoo__look_ahead
    #@abstractmethod
    @default_implemented_abstractmethod
    def mk__skip(sf, recognizer_LLoo, /):
        r'-> IRecognizerLLoo'
        return sf.mk__constant_overwrite6ok(None, recognizer_LLoo)
        #return RecognizerLLoo__skip
    @abstractmethod
    def mk__end_by___(sf, j4sgnl, min0, may_max1, recognizer4end, recognizer4continue, /):
        r'-> IRecognizerLLoo'
        #return RecognizerLLoo__end_by
    #@abstractmethod
    @default_implemented_abstractmethod
    def mk__end_by0(sf, recognizer4end, recognizer4continue, /):
        r'-> IRecognizerLLoo'
        return sf.mk__end_by___(0, 0, None, recognizer4end, recognizer4continue)
    #@abstractmethod
    @default_implemented_abstractmethod
    def mk__end_by1(sf, recognizer4end, recognizer4continue, /):
        r'-> IRecognizerLLoo'
        return sf.mk__end_by___(0, 1, None, recognizer4end, recognizer4continue)
    #@abstractmethod
    @default_implemented_abstractmethod
    def mk__between__(sf, recognizer4open, recognizer4close, recognizer4content, /):
        r'-> IRecognizerLLoo'
        return sf.mk__wrapper4postprocess6ok(_at1, sf.mk__serial([], [recognizer4open, recognizer4content, recognizer4close], []))
    #@abstractmethod
    @default_implemented_abstractmethod
    def mk__wrapper4postprocess6ok(sf, postprocess6ok, recognizer_LLoo, /):
        r'-> IRecognizerLLoo # [postprocess6ok :: Result4IRecognizerLLoo.result -> Result4IRecognizerLLoo.result]'
        transformer4result4LLoo = Transformer4Result4IRecognizerLLoo__component('', None, postprocess6ok, False)
        reformer4LLoo = Reformer4RecognizerLLoo('', None, None, transformer4result4LLoo)
        return RecognizerLLoo__reform_wrapper(reformer4LLoo, recognizer_LLoo)
        #return RecognizerLLoo__wrapper4postprocess6ok
        def postprocess(rr, /):
            if rr.ok:
                r6ok = rr.result
                r6ok = postprocess6ok(r6ok)
                rr = Result4IRecognizerLLoo(rr.the_inputer4end, rr.ok, r6ok)
            return rr
        return sf.mk__wrapper4postprocess(postprocess, recognizer_LLoo)
    @abstractmethod
    def mk__wrapper4postprocess(sf, postprocess, recognizer_LLoo, /):
        r'-> IRecognizerLLoo # [postprocess :: Result4IRecognizerLLoo -> Result4IRecognizerLLoo]'
        transformer4result4LLoo = Transformer4Result4IRecognizerLLoo__whole('', postprocess)
        reformer4LLoo = Reformer4RecognizerLLoo('', None, None, transformer4result4LLoo)
        return RecognizerLLoo__reform_wrapper(reformer4LLoo, recognizer_LLoo)
        #return RecognizerLLoo__wrapper4postprocess
    @abstractmethod
    def mk__many___(sf, j4sgnl, min0, may_max1, recognizer4continue, /):
        r'-> IRecognizerLLoo'
        #return RecognizerLLoo__many
    #@abstractmethod
    @default_implemented_abstractmethod
    def mk__many0(sf, recognizer4continue, /):
        r'-> IRecognizerLLoo'
        return sf.mk__many___(0, 0, None, recognizer4continue)
    #@abstractmethod
    @default_implemented_abstractmethod
    def mk__many1(sf, recognizer4continue, /):
        r'-> IRecognizerLLoo'
        return sf.mk__many___(0, 1, None, recognizer4continue)
    #@abstractmethod
    @default_implemented_abstractmethod
    def mk__skip_many1(sf, recognizer4continue, /):
        r'-> IRecognizerLLoo'
        return sf.mk__skip(sf.mk__many1(recognizer4continue))
            #waste memory!
        #return RecognizerLLoo__skip_many1
    #@abstractmethod
    @default_implemented_abstractmethod
    def mk__optional__tmay(sf, recognizer4continue, /):
        r'-> IRecognizerLLoo'
        return sf.mk__many___(0, 0, 1, recognizer4continue)
    #sepBy
    @abstractmethod
    def mk__sep_by___(sf, j4sgnl, min0, may_max1, recognizer4sep, recognizer4continue, /):
        r'-> IRecognizerLLoo'
        #return RecognizerLLoo__sep_by
    #@abstractmethod
    @default_implemented_abstractmethod
    def mk__sep_by0(sf, recognizer4sep, recognizer4continue, /):
        r'-> IRecognizerLLoo'
        return sf.mk__sep_by___(0, 0, None, recognizer4sep, recognizer4continue)
    #@abstractmethod
    @default_implemented_abstractmethod
    def mk__sep_by1(sf, recognizer4sep, recognizer4continue, /):
        r'-> IRecognizerLLoo'
        return sf.mk__sep_by___(0, 1, None, recognizer4sep, recognizer4continue)
    #sepEndBy
    @abstractmethod
    def mk__sep_end_by___(sf, j4sgnl, min0, may_max1, recognizer4sep_end, recognizer4continue, /):
        r'-> IRecognizerLLoo'
        #return RecognizerLLoo__sep_end_by
    #@abstractmethod
    @default_implemented_abstractmethod
    def mk__sep_end_by0(sf, recognizer4sep_end, recognizer4continue, /):
        r'-> IRecognizerLLoo'
        return sf.mk__sep_end_by___(0, 0, None, recognizer4sep_end, recognizer4continue)
    #@abstractmethod
    @default_implemented_abstractmethod
    def mk__sep_end_by1(sf, recognizer4sep_end, recognizer4continue, /):
        r'-> IRecognizerLLoo'
        return sf.mk__sep_end_by___(0, 1, None, recognizer4sep_end, recognizer4continue)
    @abstractmethod
    def mk__trace(sf, msg, may_recognizer_LLoo, /):
        r'-> IRecognizerLLoo'
        #return RecognizerLLoo__trace
    @abstractmethod
    def mk__constant(sf, err_vs_ok:bool, errmsg_or_result, /):
        r'-> IRecognizerLLoo'
        #return RecognizerLLoo__constant(smay_qname:='', err_vs_ok, errmsg_or_result)
    @abstractmethod
    def mk__constant_overwrite6ok(sf, result6ok, recognizer_LLoo, /):
        r'-> IRecognizerLLoo'
        #return RecognizerLLoo__constant_overwrite6ok(result6ok, recognizer_LLoo)

    ######################
    ######################
    r'''[[[
[[
######################
:browse Text.Parsec.Combinator
===
ghci> :browse Text.Parsec.Combinator
anyToken :: (Stream s m t, Show t) => ParsecT s u m t
between ::
  Stream s m t =>
  ParsecT s u m open
  -> ParsecT s u m close -> ParsecT s u m a -> ParsecT s u m a
chainl ::
  Stream s m t =>
  ParsecT s u m a
  -> ParsecT s u m (a -> a -> a) -> a -> ParsecT s u m a
chainl1 ::
  Stream s m t =>
  ParsecT s u m a -> ParsecT s u m (a -> a -> a) -> ParsecT s u m a
chainr ::
  Stream s m t =>
  ParsecT s u m a
  -> ParsecT s u m (a -> a -> a) -> a -> ParsecT s u m a
chainr1 ::
  Stream s m t =>
  ParsecT s u m a -> ParsecT s u m (a -> a -> a) -> ParsecT s u m a
choice :: Stream s m t => [ParsecT s u m a] -> ParsecT s u m a
count ::
  Stream s m t => Int -> ParsecT s u m a -> ParsecT s u m [a]
endBy ::
  Stream s m t =>
  ParsecT s u m a -> ParsecT s u m sep -> ParsecT s u m [a]
endBy1 ::
  Stream s m t =>
  ParsecT s u m a -> ParsecT s u m sep -> ParsecT s u m [a]
eof :: (Stream s m t, Show t) => ParsecT s u m ()
many1 :: Stream s m t => ParsecT s u m a -> ParsecT s u m [a]
manyTill ::
  Stream s m t =>
  ParsecT s u m a -> ParsecT s u m end -> ParsecT s u m [a]
notFollowedBy ::
  (Stream s m t, Show a) => ParsecT s u m a -> ParsecT s u m ()
option :: Stream s m t => a -> ParsecT s u m a -> ParsecT s u m a
optionMaybe ::
  Stream s m t => ParsecT s u m a -> ParsecT s u m (Maybe a)
optional :: Stream s m t => ParsecT s u m a -> ParsecT s u m ()
parserTrace :: (Show t, Stream s m t) => String -> ParsecT s u m ()
parserTraced ::
  (Stream s m t, Show t) =>
  String -> ParsecT s u m b -> ParsecT s u m b
sepBy ::
  Stream s m t =>
  ParsecT s u m a -> ParsecT s u m sep -> ParsecT s u m [a]
sepBy1 ::
  Stream s m t =>
  ParsecT s u m a -> ParsecT s u m sep -> ParsecT s u m [a]
sepEndBy ::
  Stream s m t =>
  ParsecT s u m a -> ParsecT s u m sep -> ParsecT s u m [a]
sepEndBy1 ::
  Stream s m t =>
  ParsecT s u m a -> ParsecT s u m sep -> ParsecT s u m [a]
skipMany1 :: Stream s m t => ParsecT s u m a -> ParsecT s u m ()
lookAhead :: Stream s m t => ParsecT s u m a -> ParsecT s u m a
]]
######################
view ../../python3_src/haskell_src/try_Parsec.hs
:browse Control.Arrow
:info Control.Arrow.Arrow
sepEndBy a sep ~= (sepBy a sep &&& optional sep) >>= fst
######################

    #]]]'''#'''


    ######################
    ######################
    ######################

_at1 = at[1]
#end-class IFactory4CommonCombinators4IRecognizerLLoo(ABC):



class IRecognizerLLoo(ABC):
    __slots__ = ()
    @abstractmethod
    def iter4two_phases_recognize(sf, factory4combinators, forkable8inputer4whole, /):
        r'''[[[
        :: factory4combinators/IFactory4CommonCombinators4IRecognizerLLoo
        -> forkable8inputer4whole/begin_of_whole/begin_of_header/IForkable
        -> gi4two_phases_recognize/IGeneratorIterator
            <iter-exprlist5yield/(child_gi4two_phases_recognize|Signal__HeaderCompleted{occur_at_most_1})
            ,return-return_value5child/either_tail_gi_or_result/(False,tail-gi4two_phases_recognize)/(True,Result4IRecognizerLLoo)
            ,raise-Error4IRecognizerLLoo
            >
        #]]]'''#'''
#end-class IRecognizerLLoo(ABC):
class IRecognizerLLoo__named(IRecognizerLLoo):
    __slots__ = ()
    @property
    @abstractmethod
    def my_name(sf, /):
        '-> nm/(hashable&&immutable)'
class IRecognizerLLoo__ref(IRecognizerLLoo):
    __slots__ = ()
    @property
    @abstractmethod
    def its_name(sf, /):
        '-> nm/(hashable&&immutable)'

class IRecognizerLLoo__lazy_wrapper(IRecognizerLLoo):
    __slots__ = ()
    @abstractmethod
    def unlazy(sf, /):
        '-> the_underlying_wrapped_recognizer_LLoo/IRecognizerLLoo'

class ITransformer4Result4IRecognizerLLoo(ABC):
    __slots__ = ()
    #@abstractmethod
    @default_implemented_abstractmethod
    def may_transform_result4LLoo(sf, reformer4LLoo, wrapper, recognizer_LLoo, factory4combinators, result4LLoo, /):
        #to impl:IReformer4RecognizerLLoo.may_postprocess
        'may ([applied by recur5yield__list__echo__echo] => ... -> IGeneratorIterator.return(result4LLoo))'
        return True, result4LLoo
        777;    yield
class IReformer4RecognizerLLoo(ABC):
    __slots__ = ()
    #@abstractmethod
    @default_implemented_abstractmethod
    def may_preprocess(sf, wrapper, recognizer_LLoo, factory4combinators, forkable8inputer4whole, /):
        'may ([applied by recur5yield__list__echo__echo] => ... -> IGeneratorIterator.return(reformer4LLoo, wrapper, recognizer_LLoo, factory4combinators, forkable8inputer4whole))' \
        '  #return new-reformer4LLoo to init/hold/update local state'
        #for trace... #IRecognizerLLoo__wrapper__traced
        return True, (sf, wrapper, recognizer_LLoo, factory4combinators, forkable8inputer4whole)
        777;    yield
    #@abstractmethod
    @default_implemented_abstractmethod
    def may_header_signal_process(sf, wrapper, recognizer_LLoo, factory4combinators, sgnl, tail_gi_after_sgnl, /):
        'may ([applied by recur5yield__list__echo__echo] => ... -> IGeneratorIterator.return((may sgnl, tail_gi_after_sgnl)|result4LLoo))'
        return True, (sgnl, tail_gi_after_sgnl)
        777;    yield
    #@abstractmethod
    @default_implemented_abstractmethod
    def may_postprocess(sf, wrapper, recognizer_LLoo, factory4combinators, result4LLoo, /):
        'may ([applied by recur5yield__list__echo__echo] => ... -> IGeneratorIterator.return(result4LLoo))'
        return True, result4LLoo
        777;    yield
#end-class IReformer4RecognizerLLoo(ABC):
class IRecognizerLLoo__reform_wrapper(IRecognizerLLoo):
    #class IRecognizerLLoo__wrapper(IRecognizerLLoo):
    __slots__ = ()
    @abstractmethod
    def _get_the_wrapped_recognizer_LLoo_(sf, /):
        '-> wrapped_recognizer_LLoo/IRecognizerLLoo'
        #def get_the_underlying_wrapped_recognizer_LLoo(sf, /):
    @abstractmethod
    def _get_the_may_reformer4LLoo_(sf, /):
        '-> may reformer4LLoo/IReformer4RecognizerLLoo'
    @override
    def iter4two_phases_recognize(sf, factory4combinators, forkable8inputer4whole, /):
        recognizer_LLoo = sf._get_the_wrapped_recognizer_LLoo_()
        check_type_le(IRecognizerLLoo, recognizer_LLoo)

        may_reformer4LLoo = sf._get_the_may_reformer4LLoo_()
        if may_reformer4LLoo is None:
            gi4two_phases_recognize = recognizer_LLoo.iter4two_phases_recognize(factory4combinators, forkable8inputer4whole)
            return False, gi4two_phases_recognize
        ###############
        reformer4LLoo = may_reformer4LLoo
        check_type_le(IReformer4RecognizerLLoo, reformer4LLoo)


        wrapper = sf
        sf = None#del

        if not None is reformer4LLoo.may_preprocess:
            (reformer4LLoo, wrapper, recognizer_LLoo, factory4combinators, forkable8inputer4whole) = yield reformer4LLoo.may_preprocess(wrapper, recognizer_LLoo, factory4combinators, forkable8inputer4whole)

        gi4two_phases_recognize = recognizer_LLoo.iter4two_phases_recognize(factory4combinators, forkable8inputer4whole)
        after_sgnl = False
        if None is reformer4LLoo.may_header_signal_process is reformer4LLoo.may_postprocess:
            return False, gi4two_phases_recognize

        (sgnl_gi_vs_result, sgnl_gi_or_result) = yield reform_half__gi4two_phases_recognize(gi4two_phases_recognize)
        after_sgnl = True
        gi4two_phases_recognize = None#del
        if sgnl_gi_vs_result:
            result = sgnl_gi_or_result
            gi = _mk_gi5val((True, result))
        else:
            (sgnl, tail_gi_after_sgnl) = sgnl_gi_or_result

            if not None is reformer4LLoo.may_header_signal_process:
                may_sgnl_gi_or_result = yield reformer4LLoo.may_header_signal_process(wrapper, recognizer_LLoo, factory4combinators, sgnl, tail_gi_after_sgnl)
            else:
                may_sgnl_gi_or_result = (sgnl, tail_gi_after_sgnl)
            may_sgnl_gi_or_result
            sgnl = None#del
            tail_gi_after_sgnl = None#del
            ############
            may_sgnl_gi_or_result
            if type(may_sgnl_gi_or_result) is Result4IRecognizerLLoo:
                result = may_sgnl_gi_or_result
                gi = _mk_gi5val((True, result))
            elif type(may_sgnl_gi_or_result) is tuple:
                may_sgnl_gi = may_sgnl_gi_or_result
                check_pair(may_sgnl_gi)
                (may_sgnl, tail_gi_after_sgnl) = may_sgnl_gi
                if not None is may_sgnl:
                    sgnl = may_sgnl
                    check_type_is(Signal__HeaderCompleted, sgnl)
                    yield sgnl
                    sgnl = None#del
                else:
                    #xxx:yield sgnl
                    pass#cancel sgnl
                tail_gi_after_sgnl
                gi = tail_gi_after_sgnl
                #result = yield tail_gi_after_sgnl
                    # !! [gi :: tail_gi<gi4two_phases_recognize> after sgnl]
                    # !! [applied by recur5yield__list__echo__echo]
                    # => [return_value5child :: Result4IRecognizerLLoo]
            else:
                raise TypeError(type(may_sgnl_gi_or_result))
            gi#result
        gi#result
        assert after_sgnl
        if not None is reformer4LLoo.may_postprocess:
            assert after_sgnl
            result = yield gi
            check_type_is(Result4IRecognizerLLoo, result)
            gi = reformer4LLoo.may_postprocess(wrapper, recognizer_LLoo, factory4combinators, result)
        return False, gi
        result = yield gi
        check_type_is(Result4IRecognizerLLoo, result)
        return True, result
def _mk_gi5val(x, /):
    return x; yield
#end-class IRecognizerLLoo__reform_wrapper(IRecognizerLLoo):






######################
######################
######################

class RecognizerLLoo__named_wrapper(IRecognizerLLoo__named):
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        if sf._b:
            return sf._nm
        return str(sf)
    def __str__(sf, /):
        return repr_helper(sf, sf._nm, sf._x, repr_by_name=sf._b)
    def __init__(sf, nm, recognizer_LLoo, /, *, repr_by_name:bool):
        check_type_is(bool, repr_by_name)
        check_type_le(IRecognizerLLoo, recognizer_LLoo)
        hash(nm) # hashable
        if repr_by_name:
            #check_type_is(str, nm)
            check_pseudo_qual_name(nm)
        sf._nm = nm
        sf._x = recognizer_LLoo
        sf._b = repr_by_name
    @property
    @override
    def my_name(sf, /):
        '-> nm/(hashable&&immutable)'
        return sf._nm
    @override
    def iter4two_phases_recognize(sf, factory4combinators, forkable8inputer4whole, /):
        sf = sf._x
        return sf.iter4two_phases_recognize(factory4combinators, forkable8inputer4whole)

class RecognizerLLoo__ref(IRecognizerLLoo__ref):
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        return repr_helper(sf, sf._nm)
    def __init__(sf, nm, /):
        hash(nm) # hashable
        sf._nm = nm
    @property
    @override
    def its_name(sf, /):
        '-> nm/(hashable&&immutable)'
        return sf._nm
    @override
    def iter4two_phases_recognize(sf, factory4combinators, forkable8inputer4whole, /):
        sf = factory4combinators.dereference(sf._nm)
        return sf.iter4two_phases_recognize(factory4combinators, forkable8inputer4whole)

class RecognizerLLoo__lazy_wrapper(IRecognizerLLoo__lazy_wrapper):
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        return repr_helper(sf, sf._x, non_lazy=sf._b)
    def __init__(sf, lazy_or_recognizer_LLoo, /, *, non_lazy=False):
        sf._x = lazy_or_recognizer_LLoo
        sf._b = non_lazy
        check_type_is(bool, non_lazy)
        if non_lazy:
            recognizer_LLoo = lazy_or_recognizer_LLoo
            check_type_le(IRecognizerLLoo, recognizer_LLoo)
        else:
            lazy__recognizer_LLoo = lazy_or_recognizer_LLoo
            check_callable(lazy__recognizer_LLoo)
    @override
    def unlazy(sf, /):
        '-> the_underlying_wrapped_recognizer_LLoo/IRecognizerLLoo'
        #if non_lazy:
        if sf._b:
            return sf._x
        lazy__recognizer_LLoo = sf._x
        sf._x = lazy__recognizer_LLoo()
        sf._b = True
        return sf.unlazy()
    @override
    def iter4two_phases_recognize(sf, factory4combinators, forkable8inputer4whole, /):
        sf = sf.unlazy()
        return sf.iter4two_phases_recognize(factory4combinators, forkable8inputer4whole)
class RecognizerLLoo__reform_wrapper(IRecognizerLLoo__reform_wrapper):
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        return repr_helper(sf, sf._f, sf._x)
    def __init__(sf, may_reformer4LLoo, recognizer_LLoo, /):
        sf._f = may_reformer4LLoo
        sf._x = recognizer_LLoo
        check_may_([check_type_le, IReformer4RecognizerLLoo], may_reformer4LLoo)
        check_type_le(IRecognizerLLoo, recognizer_LLoo)
    @override
    def _get_the_wrapped_recognizer_LLoo_(sf, /):
        '-> wrapped_recognizer_LLoo/IRecognizerLLoo'
        return sf._x
    @override
    def _get_the_may_reformer4LLoo_(sf, /):
        '-> may reformer4LLoo/IReformer4RecognizerLLoo'
        return sf._f
class _With_smay_qname:
    'required: sf._smay_qnm, sf._args'
    __slots__ = ()
    def __repr__(sf, /):
        s = sf._smay_qnm
        if s:
            return s
        return str(sf)
    def __str__(sf, /):
        return repr_helper(sf, *sf._args)
class Reformer4RecognizerLLoo(_With_smay_qname, IReformer4RecognizerLLoo):
    ___no_slots_ok___ = True
    def __init__(sf, smay_qname, may_preprocess, may_header_signal_process, may_postprocess, /):
        sf._args = (smay_qname, may_preprocess, may_header_signal_process, may_postprocess)
        #########
        if isinstance(may_postprocess, ITransformer4Result4IRecognizerLLoo):
            transformer4result4LLoo = may_postprocess
            may_postprocess = transformer4result4LLoo.may_transform_result4LLoo
        may_postprocess
        #########
        check_smay_pseudo_qual_name(smay_qname)
        check_may_(check_callable, may_preprocess)
        check_may_(check_callable, may_header_signal_process)
        check_may_(check_callable, may_postprocess)
        #########
        sf._smay_qnm = smay_qname
        sf._f0 = may_preprocess
        sf._f1 = may_header_signal_process
        sf._f2 = may_postprocess

    def _4may_xxx(sf, f, /):
        if f is None:
            return None
        return curry1(f, sf)
    @property
    @override
    def may_preprocess(sf, /):
        #def may_preprocess(sf, wrapper, recognizer_LLoo, factory4combinators, forkable8inputer4whole, /):
        'may ([applied by recur5yield__list__echo__echo] => ... -> IGeneratorIterator.return(reformer4LLoo, wrapper, recognizer_LLoo, factory4combinators, forkable8inputer4whole))' \
        '  #return new-reformer4LLoo to init/hold/update local state'

        return sf._4may_xxx(sf._f0)
    @property
    @override
    def may_header_signal_process(sf, /):
        #def may_header_signal_process(sf, wrapper, recognizer_LLoo, factory4combinators, sgnl, tail_gi_after_sgnl, /):
        'may ([applied by recur5yield__list__echo__echo] => ... -> IGeneratorIterator.return((may sgnl, tail_gi_after_sgnl)|result4LLoo))'
        return sf._4may_xxx(sf._f1)
    @property
    @override
    def may_postprocess(sf, /):
        #def may_postprocess(sf, wrapper, recognizer_LLoo, factory4combinators, result4LLoo, /):
        'may ([applied by recur5yield__list__echo__echo] => ... -> IGeneratorIterator.return(result4LLoo))'
        return sf._4may_xxx(sf._f2)
#end-class Reformer4RecognizerLLoo(IReformer4RecognizerLLoo):
#class Reformer4RecognizerLLoo__transformer4result4LLoo(IReformer4RecognizerLLoo):
class Transformer4Result4IRecognizerLLoo__whole(_With_smay_qname, ITransformer4Result4IRecognizerLLoo):
    ___no_slots_ok___ = True
    def __init__(sf, smay_qname, may_transformer4result4LLoo, /):
        sf._args = (smay_qname, may_transformer4result4LLoo)
        ######
        check_smay_pseudo_qual_name(smay_qname)
        check_may_(check_callable, may_transformer4result4LLoo)
        ######
        ######
        sf._smay_qnm = smay_qname
        sf._f = may_transformer4result4LLoo
    @property
    @override
    def may_transform_result4LLoo(sf, /):
        #def may_transform_result4LLoo(sf, reformer4LLoo, wrapper, recognizer_LLoo, factory4combinators, result4LLoo, /):
        #to impl:IReformer4RecognizerLLoo.may_postprocess
        'may ([applied by recur5yield__list__echo__echo] => ... -> IGeneratorIterator.return(result4LLoo))'
        f4w = ifNone(sf._f, echo)
        if f4w is echo:
            return None
        def transform_result4LLoo(reformer4LLoo, wrapper, recognizer_LLoo, factory4combinators, result4LLoo, /):
            result4LLoo = f4w(result4LLoo)
            check_type_is(Result4IRecognizerLLoo, result4LLoo)
            return True, result4LLoo
            777;    yield
        return transform_result4LLoo
#end-class Transformer4Result4IRecognizerLLoo__whole(_With_smay_qname, ITransformer4Result4IRecognizerLLoo):


class Transformer4Result4IRecognizerLLoo__component(_With_smay_qname, ITransformer4Result4IRecognizerLLoo):
    ___no_slots_ok___ = True
    def __init__(sf, smay_qname, may_transformer4errmsg, may_transformer4result, to_invert_ok:bool, /):
        sf._args = (smay_qname, may_transformer4errmsg, may_transformer4result, to_invert_ok)
        ######
        check_smay_pseudo_qual_name(smay_qname)
        check_may_(check_callable, may_transformer4errmsg)
        check_may_(check_callable, may_transformer4result)
        check_type_is(bool, to_invert_ok)
        ######
        ######
        sf._smay_qnm = smay_qname
        sf._f0 = may_transformer4errmsg
        sf._f1 = may_transformer4result
        sf._b2 = to_invert_ok
    @property
    @override
    def may_transform_result4LLoo(sf, /):
        #def may_transform_result4LLoo(sf, reformer4LLoo, wrapper, recognizer_LLoo, factory4combinators, result4LLoo, /):
        #to impl:IReformer4RecognizerLLoo.may_postprocess
        'may ([applied by recur5yield__list__echo__echo] => ... -> IGeneratorIterator.return(result4LLoo))'
        f4err = ifNone(sf._f0, echo)
        f4ok = ifNone(sf._f1, echo)
        to_invert_ok = sf._b2
        if not to_invert_ok and f4err is echo is f4ok:
            return None
        def transform_result4LLoo(reformer4LLoo, wrapper, recognizer_LLoo, factory4combinators, result4LLoo, /):
            #result4LLoo.the_inputer4end
            #result4LLoo.ok
            #result4LLoo.errmsg_or_result
            if result4LLoo.ok:
                errmsg_or_result = f4ok(result4LLoo.result)
            else:
                errmsg_or_result = f4err(result4LLoo.errmsg)
            ok = to_invert_ok ^ result4LLoo.ok
            result4LLoo = Result4IRecognizerLLoo(result4LLoo.the_inputer4end, ok, errmsg_or_result)
            return True, result4LLoo
            777;    yield
        return transform_result4LLoo
#end-class Transformer4Result4IRecognizerLLoo__component(_With_smay_qname, ITransformer4Result4IRecognizerLLoo):



######################
######################
######################
######################
######################
######main_funcs:
######################
######################
######################
######################
def reform_half__gi4two_phases_recognize(gi4two_phases_recognize, /):
    r'''[[[
    :: [applied by recur5yield__list__echo__echo]
    => gi4two_phases_recognize
    -> IGeneratorIterator
        <yield-child_gi4two_phases_recognize
        ,return-either_sgnl_gi_or_result/(sgnl_gi_vs_result/bool, sgnl_gi_or_result/((sgnl/Signal__HeaderCompleted,gi/IGeneratorIterator)|result/Result4IRecognizerLLoo))
            #impl actually return either__tail_gi__or__either_sgnl_gi_or_result
        ,raise-Error4IRecognizerLLoo
        >
    #]]]'''#'''
    check_type_le(IGeneratorIterator, gi4two_phases_recognize)
    gi = gi4two_phases_recognize
    gi4two_phases_recognize = None#del
    #for child_gi__or__hdr_signal in gi:
    #for subgiXsgnl in gi:
    value4send = None
    while 1:
      # come from:outer_while_continue6tail_gi
      try:
        while 1:
            subgiXsgnl = exprlist5yield = gi.send(value4send)
                # ^StopIteration
            if type(subgiXsgnl) is Signal__HeaderCompleted:
                sgnl = subgiXsgnl
                break#inner_while_break6sgnl
            else:
                subgi = subgiXsgnl
                #check_type_le(IGeneratorIterator, subgi)
                value4send = yield subgi
      except StopIteration as e:
        either_tail_gi_or_result = return_value5child = e.value
        check_either(either_tail_gi_or_result)
        (is_result, tail_gi_or_result) = either_tail_gi_or_result
        if is_result:
            result = tail_gi_or_result
            break#outer_while_break6result
        else:
            tail_gi = tail_gi_or_result
            check_type_le(IGeneratorIterator, tail_gi)
            #####next-round@outer_while:
            gi = tail_gi
            value4send = None
            continue#outer_while_continue6tail_gi
        raise 000
        #######old:
        result = return_value5child = e.value
        check_type_is(Result4IRecognizerLLoo, result)
        return True, (sgnl_gi_vs_result:=True, result)
      else:
        # come from:inner_while_break6sgnl
        sgnl
        return True, (sgnl_gi_vs_result:=False, (sgnl, gi))
    # come from:outer_while_break6result
    check_type_is(Result4IRecognizerLLoo, result)
    return True, (sgnl_gi_vs_result:=True, result)

def reform_exhausted__gi4two_phases_recognize(gi4two_phases_recognize, /):
    r'''[[[
    :: [applied by recur5yield__list__echo__echo]
    => gi4two_phases_recognize
    -> IGeneratorIterator
        <yield-child_gi4two_phases_recognize
        ,return-Result4IRecognizerLLoo
            #impl actually return either__tail_gi__or__result
        ,raise-Error4IRecognizerLLoo
        >
    #]]]'''#'''
    (sgnl_gi_vs_result, sgnl_gi_or_result) = yield reform_half__gi4two_phases_recognize(gi4two_phases_recognize)
    if sgnl_gi_vs_result:
        result = sgnl_gi_or_result
    else:
        #(sgnl, tail_gi_after_sgnl) = sgnl_gi
        (sgnl,gi) = sgnl_gi_or_result
        #xxx:yield sgnl
        return False, gi
        result = yield gi
            # !! [gi :: tail_gi<gi4two_phases_recognize> after sgnl]
            # !! [applied by recur5yield__list__echo__echo]
            # => [return_value5child :: Result4IRecognizerLLoo]
    check_type_is(Result4IRecognizerLLoo, result)
    return True, result

@recur5yield__list__echo__echo
def recognize__LLoo(recognizer_LLoo, factory4combinators, forkable8inputer4whole, /):
    r'''[[[
    :: [applied by recur5yield__list__echo__echo]
    => recognizer_LLoo/IRecognizerLLoo
    -> factory4combinators/IFactory4CommonCombinators4IRecognizerLLoo
    -> forkable8inputer4whole/begin_of_whole/begin_of_header/IForkable
    -> (Result4IRecognizerLLoo | ^Error4IRecognizerLLoo)
    #]]]'''#'''
    gi4two_phases_recognize = recognizer_LLoo.iter4two_phases_recognize(factory4combinators, forkable8inputer4whole)
    return False, reform_exhausted__gi4two_phases_recognize(gi4two_phases_recognize)


######################
######################
######################
######################
######################
# more concrete IRecognizerLLoo:
######################
######################
######################
######################
    #RecognizerLLoo__constant
    #RecognizerLLoo__constant_overwrite6ok
    #RecognizerLLoo__trace
    #RecognizerLLoo__any_token
    #RecognizerLLoo__invert_err_ok
    #RecognizerLLoo__look_ahead
    #RecognizerLLoo__skip
    #RecognizerLLoo__skip_many1
    #RecognizerLLoo__wrapper4postprocess6ok
    #RecognizerLLoo__wrapper4postprocess

    #RecognizerLLoo__serial
    #RecognizerLLoo__parallel__the_only_one
    #RecognizerLLoo__choice__the_first_one
    #RecognizerLLoo__many
    #RecognizerLLoo__end_by
    #RecognizerLLoo__sep_by
    #RecognizerLLoo__sep_end_by

class RecognizerLLoo__constant(_With_smay_qname, IRecognizerLLoo):
    ___no_slots_ok___ = True
    def __init__(sf, smay_qname, err_vs_ok:bool, errmsg_or_result, /):
        sf._args = (smay_qname, err_vs_ok, errmsg_or_result)
        ######
        check_smay_pseudo_qual_name(smay_qname)
        check_type_is(bool, err_vs_ok)
        ######
        sf._smay_qnm = smay_qname
        sf._ok = err_vs_ok
        sf._x = errmsg_or_result
    @override
    def iter4two_phases_recognize(sf, factory4combinators, forkable8inputer4whole, /):
        result4LLoo = Result4IRecognizerLLoo(forkable8inputer4end:=forkable8inputer4whole, sf._ok, sf._x)
        return True, result4LLoo
        777;    yield
the_pass_LLoo = RecognizerLLoo__constant('the_pass_LLoo', True, None, None)
class RecognizerLLoo__constant_overwrite6ok(IRecognizerLLoo__reform_wrapper):
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        return repr_helper(sf, sf._r6ok, sf._w)
    def __init__(sf, result6ok, recognizer_LLoo, /):
        check_type_le(IRecognizerLLoo, recognizer_LLoo)
        ######
        transformer8postprocess = Transformer4Result4IRecognizerLLoo__component('', None, const(result6ok), False)
        sf._r6ok = result6ok
        sf._w = recognizer_LLoo
        sf._f = Reformer4RecognizerLLoo('', None, None, transformer8postprocess)
    @override
    def _get_the_wrapped_recognizer_LLoo_(sf, /):
        '-> wrapped_recognizer_LLoo/IRecognizerLLoo'
        return sf._w
    @override
    def _get_the_may_reformer4LLoo_(sf, /):
        '-> may reformer4LLoo/IReformer4RecognizerLLoo'
        return sf._f


class RecognizerLLoo__trace(_With_smay_qname, IRecognizerLLoo):
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        return repr_helper(sf, sf._msg, sf._x)
    def __init__(sf, msg, may_recognizer_LLoo, /):
        check_may_([check_type_le, IRecognizerLLoo], may_recognizer_LLoo)
        sf._msg = msg
        sf._x = may_recognizer_LLoo
    @override
    def iter4two_phases_recognize(sf, factory4combinators, forkable8inputer4whole, /):
        factory4combinators.tracing(forkable8inputer4whole.fork(), sf._msg)
        recognizer_LLoo = ifNone(sf._x, the_pass_LLoo)

        gi4two_phases_recognize = recognizer_LLoo.iter4two_phases_recognize(factory4combinators, forkable8inputer4whole)
        return gi4two_phases_recognize
class RecognizerLLoo__any_token(_With_smay_qname, IRecognizerLLoo):
    r'''[[[
    required:
        [inputer/forkable8inputer4whole :: IForkableForwardInputStream]
    token may be (position_info, code/word/char)
    #]]]'''#'''
    ___no_slots_ok___ = True
    _smay_qnm = 'the_any_token_LLoo'
    _args = ()
    def __new__(cls, /):
        try:
            sf = the_any_token_LLoo
        except NameError:
            sf = super(__class__, cls).__new__(cls)
        return sf
    @override
    def iter4two_phases_recognize(sf, factory4combinators, forkable8inputer4whole, /):
        try:
            token = forkable8inputer4whole.read1()
        except EOFError:
            result4LLoo = Result4IRecognizerLLoo(forkable8inputer4whole, False, 'eof')
        else:
            result4LLoo = Result4IRecognizerLLoo(forkable8inputer4whole, True, token)
        return True, result
        777;    yield
the_any_token_LLoo = RecognizerLLoo__any_token()

the_transformer4result4LLoo__invert_err_ok = Transformer4Result4IRecognizerLLoo__component('', None, None, True)
the_reformer4LLoo__invert_err_ok = Reformer4RecognizerLLoo('', None, None, the_transformer4result4LLoo__invert_err_ok)
class _IWrap(IRecognizerLLoo__reform_wrapper):
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        return repr_helper(sf, sf._w)
    def __init__(sf, recognizer_LLoo, /):
        check_type_le(IRecognizerLLoo, recognizer_LLoo)
        sf._w = recognizer_LLoo
        #RecognizerLLoo__reform_wrapper(the_reformer4LLoo__invert_err_ok, recognizer_LLoo)
    @override
    def _get_the_wrapped_recognizer_LLoo_(sf, /):
        '-> wrapped_recognizer_LLoo/IRecognizerLLoo'
        return sf._w
class RecognizerLLoo__invert_err_ok(_IWrap):
    @override
    def _get_the_may_reformer4LLoo_(sf, /):
        '-> may reformer4LLoo/IReformer4RecognizerLLoo'
        return the_reformer4LLoo__invert_err_ok

class RecognizerLLoo__look_ahead(_IWrap):
    @override
    def _get_the_may_reformer4LLoo_(sf, /):
        '-> may reformer4LLoo/IReformer4RecognizerLLoo'
        return the_reformer4LLoo__look_ahead

class Reformer4RecognizerLLoo__look_ahead(IReformer4RecognizerLLoo):
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        return repr_helper(sf, sf._m)
    def __init__(sf, may_inputer, /):
        check_may_([check_type_le, IForkable], may_inputer)
        sf._m = may_inputer
    @override
    def may_preprocess(sf, wrapper, recognizer_LLoo, factory4combinators, forkable8inputer4whole, /):
        'may ([applied by recur5yield__list__echo__echo] => ... -> IGeneratorIterator.return(reformer4LLoo, wrapper, recognizer_LLoo, factory4combinators, forkable8inputer4whole))' \
        '  #return new-reformer4LLoo to init/hold/update local state'
        if not None is sf._m: raise TypeError
        sf = type(sf)(forkable8inputer4whole.fork())
            #saved snapshot
        return True, (sf, wrapper, recognizer_LLoo, factory4combinators, forkable8inputer4whole)
        777;    yield
    @override
    def may_header_signal_process(sf, wrapper, recognizer_LLoo, factory4combinators, sgnl, tail_gi_after_sgnl, /):
        'may ([applied by recur5yield__list__echo__echo] => ... -> IGeneratorIterator.return((may sgnl, tail_gi_after_sgnl)|result4LLoo))'
        if None is sf._m: raise TypeError
        sgnl = Signal__HeaderCompleted(sf._m, sgnl)
            #restore snapshot
        return True, (sgnl, tail_gi_after_sgnl)
        777;    yield
    @override
    def may_postprocess(sf, wrapper, recognizer_LLoo, factory4combinators, result4LLoo, /):
        'may ([applied by recur5yield__list__echo__echo] => ... -> IGeneratorIterator.return(result4LLoo))'
        if None is sf._m: raise TypeError
        result4LLoo = Signal__HeaderCompleted(sf._m, result4LLoo.ok, result4LLoo)
            #restore snapshot
        return True, result4LLoo
        777;    yield
#end-class Reformer4RecognizerLLoo__look_ahead(IReformer4RecognizerLLoo):
the_reformer4LLoo__look_ahead = Reformer4RecognizerLLoo__look_ahead(None)
    #RecognizerLLoo__skip

class _(ABC):
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        #return repr_helper(sf, *args, **kwargs)
        #return repr_helper_ex(sf, args, ordered_attrs, kwargs, ordered_attrs_only=False)
        ...
if __name__ == "__main__":

__all__
from seed.recognize.recognizer_LLoo import *
