#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/recognizer_LLoo_/IFactory4RecognizerLLoo.py
view ../../python3_src/seed/recognize/recognizer_LLoo_/Factory4RecognizerLLoo.py

seed.recognize.recognizer_LLoo_.IFactory4RecognizerLLoo
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_LLoo_.IFactory4RecognizerLLoo -x
#]]]'''
__all__ = r'''
IFactory4RecognizerLLoo__inputter_is_IForkable__stamp
    IFactory4RecognizerLLoo__inputter_is_IForkableForwardInputStream666IToken999
        IFactory4RecognizerLLoo__inputter_is_IForkableForwardInputStream666IToken666IChar999_999
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...

from seed.recognize.recognizer_LLoo_._common import (
IForkable, IForkable__stamp
,abstractmethod, override, ABC, ABC__no_slots
)

from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import IRecognizerLLoo# Signal__HeaderCompleted, Reply4IRecognizerLLoo

from seed.recognize.recognizer_LLoo_.stream._common import (IToken
,IForkableForwardInputStream, ForkableForwardInputStream__using_LazyListIter
)

from seed.tiny_.check import check_type_is

___end_mark_of_excluded_global_names__0___ = ...

######################
#\(@abstractmethod\)\@<!\n *def 
#\(@abstractmethod\)\@<=\n *def 
#%s/^ *def \w*(/\0sf, 
#   # )
######################
class IFactory4RecognizerLLoo__inputter_is_IForkable__stamp(ABC):
    'factory<combinator_LLoo>#[inputter::IForkable__stamp]'
    __slots__ = ()
    @property
    @abstractmethod
    def recognizer_LLoo__ignore(sf, /):
        '-> IRecognizerLLoo'
    @property
    @abstractmethod
    def recognizer_LLoo__pass(sf, /):
        '-> IRecognizerLLoo'
    @property
    @abstractmethod
    def recognizer_LLoo__fail(sf, /):
        '-> IRecognizerLLoo'
    recognizer_LLoo__ignore
    recognizer_LLoo__pass
    recognizer_LLoo__fail
    ######################
    @abstractmethod
    def mk_LLoo__gi8flow__all_in_one(sf, all_in_one_ex, args4all_in_one_ex, /):
        '(all_in_one_ex/(case/uint%5 -> (*args4all_in_one_ex) -> result4all_in_one4gi8flow4LLoo(([case==0]gi8flow4LLoo)|([case==1](Iter tribool_skip){len==1})|([case==2](Iter kinded_name))|([case==3](Iter IDependentTreeNode)))) -> args4all_in_one_ex/[arg] -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__dependent_pair(sf, rgnr4fst, rgnrXmkr4snd, /):
        'IRecognizerLLoo -> (IRecognizerLLoo|IMaker4RecognizerLLoo__5oresult) -> IRecognizerLLoo{dependent_pair}'
    @abstractmethod
    def mk_LLoo__switch_branches(sf, rgnr4case, rgnrXmkr_ls4branches, /):
        'IRecognizerLLoo{oresult/Cased} -> [(IRecognizerLLoo|IMaker4RecognizerLLoo__5oresult)] -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__if_then_else(sf, rgnr4if, rgnr_or_mkr4then, rgnr_or_mkr4else, /):
        'IRecognizerLLoo{oresult/Either} -> (IRecognizerLLoo|IMaker4RecognizerLLoo__5oresult) -> (IRecognizerLLoo|IMaker4RecognizerLLoo__5oresult) -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__flow(sf, instructions, may__label2idx4instruction, /):
        r'[IInstruction4flow4LLoo]{len==L} -> may {label/(Hashable\-\int):uint%L} -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__base_loop(sf, rgnr4body4loop, /, *, to_output_num_loops=False, min_loops=0, imay_max_loops=-1, may_uhidx4hdr:1=None, may_rgnr4end7pre=None, may_rgnr4end7post=None):
        'IRecognizerLLoo -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__many(sf, rgnr4body4loop, /, *, min_loops=0, imay_max_loops=-1, may_uhidx4hdr:1=None):
        'IRecognizerLLoo -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__skip_many1(sf, rgnr4body4loop, /):
        'IRecognizerLLoo -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__end_by__pre(sf, rgnr4end7pre, rgnr4body4loop, /, *, min_loops=0, imay_max_loops=-1, may_uhidx4hdr:1=None):
        'IRecognizerLLoo -> IRecognizerLLoo -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__end_by__post(sf, rgnr4end7post, rgnr4body4loop, /, *, min_loops=0, imay_max_loops=-1, may_uhidx4hdr:1=None):
        'IRecognizerLLoo -> IRecognizerLLoo -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__sep_by(sf, rgnr4sep, rgnr4item, /, *, min_loops=0, imay_max_loops=-1, may_uhidx4hdr:1=None):
        'IRecognizerLLoo -> IRecognizerLLoo -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__between(sf, rgnr4begin, rgnr4body, rgnr4end, /):
        'IRecognizerLLoo -> IRecognizerLLoo -> IRecognizerLLoo -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__the_first_one(sf, rgnrs, /, *, tagged=False, cased=False, _6oresult_only_=False):
        '[IRecognizerLLoo] -> IRecognizerLLoo #the_first_one/choice'
    @abstractmethod
    def mk_LLoo__the_only_one(sf, rgnrs, /, *, tagged=False, cased=False, _6oresult_only_=False):
        '[IRecognizerLLoo] -> IRecognizerLLoo #the_only_one/parallel'
    #mk_LLoo__choice = mk_LLoo__the_first_one
    #mk_LLoo__parallel = mk_LLoo__the_only_one
    @property
    def mk_LLoo__choice(sf, /):
        '-> ([IRecognizerLLoo] -> IRecognizerLLoo) #the_first_one/choice'
        return sf.mk_LLoo__the_first_one
    @property
    def mk_LLoo__parallel(sf, /):
        '-> ([IRecognizerLLoo] -> IRecognizerLLoo) #the_only_one/parallel'
        return sf.mk_LLoo__the_only_one


    @abstractmethod
    def mk_LLoo__xtuple(sf, shidx4hdr__or__xs4hdr, xs4whole__or__xs4body, /, *, dependent):
        '(int{-(1+2*L)<=.<(1+2*L)}|[x]) -> [x]{len==L} -> IRecognizerLLoo # [x :: ((IRecognizerLLoo|IMaker4RecognizerLLoo__5ctx) if dependent else IRecognizerLLoo)]'
    @abstractmethod
    def mk_LLoo__tuple(sf, shidx4hdr__or__rgnrs4hdr, rgnrs4whole__or__rgnrs4body, /):
        '(int{-(1+2*L)<=.<(1+2*L)}|[IRecognizerLLoo]) -> [IRecognizerLLoo]{len==L} -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__dependent_tuple(sf, shidx4hdr__or__mkrs4hdr, mkrs4whole__or__mkrs4body, /):
        '(int{-(1+2*L)<=.<(1+2*L)}|[(IRecognizerLLoo|IMaker4RecognizerLLoo__5ctx)]) -> [(IRecognizerLLoo|IMaker4RecognizerLLoo__5ctx)]{len==L} -> IRecognizerLLoo'



    @abstractmethod
    def mk_LLoo__skip(sf, rgnr, /, *, to_wrap=False):
        'IRecognizerLLoo -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__pack(sf, rgnr, /, *, to_wrap=False):
        'IRecognizerLLoo -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__unpack(sf, rgnr, /, *, to_wrap=False):
        'IRecognizerLLoo -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__with_tribool_skip(sf, tribool_skip, rgnr, /, *, to_wrap=False):
        'tribool -> IRecognizerLLoo -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__with_tribool_skip_as(sf, rgnr8src, rgnr8dst, /, *, to_wrap=False):
        'IRecognizerLLoo -> IRecognizerLLoo -> IRecognizerLLoo'

    @abstractmethod
    def mk_LLoo__simple_postprocess(sf, eresult2eresult_, rgnr, /):
        '(Either -> Either) -> IRecognizerLLoo -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__simple_postprocess6ok(sf, oresult2oresult_, rgnr, /):
        '(Reply4IRecognizerLLoo.oresult -> oresult) -> IRecognizerLLoo -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__simple_postprocess6err(sf, errmsg2errmsg_, rgnr, /):
        '(Reply4IRecognizerLLoo.errmsg -> errmsg) -> IRecognizerLLoo -> IRecognizerLLoo'


    @abstractmethod
    def mk_LLoo__validate_two_phases(sf, rgnr, /):
        'IRecognizerLLoo -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__skip_header_signal(sf, rgnr, /):
        'IRecognizerLLoo -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__header_signal_at_beginning(sf, rgnr, /):
        'IRecognizerLLoo -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__patch_header_signal_if_ok(sf, rgnr, /):
        'IRecognizerLLoo -> IRecognizerLLoo'

    @abstractmethod
    def mk_LLoo__tag(sf, tag, rgnr, /, *, _6oresult_only_=False):
        'tag -> IRecognizerLLoo -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__Cased(sf, case, rgnr, /, *, _6oresult_only_=False):
        'case -> IRecognizerLLoo -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__invert_err_ok(sf, rgnr, /):
        'IRecognizerLLoo -> IRecognizerLLoo'

    @abstractmethod
    def mk_LLoo__unbox(sf, rgnr, /):
        'IRecognizerLLoo -> IRecognizerLLoo'


    @abstractmethod
    def mk_LLoo__try__rollback_if_fail_before_hdr_sgnl_else_lift(sf, rgnr, /):
        'IRecognizerLLoo -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__optional__either(sf, rgnr, /):
        'IRecognizerLLoo -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__optional__tmay(sf, rgnr, /):
        'IRecognizerLLoo -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__optional__default(sf, oresult8default, rgnr, /):
        'default/Reply4IRecognizerLLoo.oresult -> IRecognizerLLoo -> IRecognizerLLoo'

    @abstractmethod
    def mk_LLoo__look_ahead__no_err4hdr(sf, rgnr, /):
        'IRecognizerLLoo -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__look_ahead__no_err4whole(sf, rgnr, /):
        'IRecognizerLLoo -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__look_ahead4hdr(sf, rgnr, /):
        'IRecognizerLLoo -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__look_ahead4whole(sf, rgnr, /):
        'IRecognizerLLoo -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__not_followed_by4hdr(sf, rgnr, /):
        'IRecognizerLLoo -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__not_followed_by4whole(sf, rgnr, /):
        'IRecognizerLLoo -> IRecognizerLLoo'



    @abstractmethod
    def mk_LLoo__constant_overwrite6ok(sf, oresult, rgnr, /):
        'Reply4IRecognizerLLoo.oresult -> IRecognizerLLoo -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__constant_overwrite6err(sf, errmsg, rgnr, /):
        'Reply4IRecognizerLLoo.errmsg -> IRecognizerLLoo -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__constant_overwrite(sf, errmsg, oresult, rgnr, /):
        'Reply4IRecognizerLLoo.the_eresult/Either -> IRecognizerLLoo -> IRecognizerLLoo'


    @abstractmethod
    def mk_LLoo__constant_eresult(sf, eresult, /, *, tribool_skip=False):
        'Reply4IRecognizerLLoo.the_eresult/Either -> IRecognizerLLoo'

    @abstractmethod
    def mk_LLoo__named_wrapper(sf, name, rgnr, /):
        'name -> IRecognizerLLoo -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__ref(sf, scene, kinded_name, /):
        'IScene -> kinded_name/Hashable -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__lazy(lazy_or_rgnr, /, *, non_lazy=False):
        r'lazy_or_rgnr/(IRecognizerLLoo if non_lazy else (()->IRecognizerLLoo)) -> (*,non_lazy/bool) -> IRecognizerLLoo'

    ######################
#end-class IFactory4RecognizerLLoo__inputter_is_IForkable__stamp(ABC):














######################
######################
######################
#stream<token>
######################
class IFactory4RecognizerLLoo__inputter_is_IForkableForwardInputStream666IToken999(IFactory4RecognizerLLoo__inputter_is_IForkable__stamp):
    'factory<combinator_LLoo>#[inputter::IForkableForwardInputStream<IToken>]'
    __slots__ = ()
    @property
    @abstractmethod
    def recognizer_LLoo__eof(sf, /):
        '-> IRecognizerLLoo'
    @property
    @abstractmethod
    def recognizer_LLoo__any_token(sf, /):
        '-> IRecognizerLLoo'
    @property
    @abstractmethod
    def recognizer_LLoo__any_tkey(sf, /):
        '-> IRecognizerLLoo'
    @property
    @abstractmethod
    def recognizer_LLoo__any_tdat(sf, /):
        '-> IRecognizerLLoo'
    @property
    @abstractmethod
    def recognizer_LLoo__any_tkd(sf, /):
        '-> IRecognizerLLoo'
    recognizer_LLoo__eof
    recognizer_LLoo__any_token
    recognizer_LLoo__any_tkey
    recognizer_LLoo__any_tdat
    recognizer_LLoo__any_tkd
    ######################
    @abstractmethod
    def mk_LLoo__token_set(token_set_query, /, *, to_invert=False):
        'ITokenSetQuery -> IRecognizerLLoo'

    #######
    ##@abstractmethod
    ##def mk_LLoo__tkey_set(token_set_query, /, *, to_invert=False):
    ##    'ITokenSetQuery -> IRecognizerLLoo'
    ##@abstractmethod
    ##def mk_LLoo__match_constant_tkeys(sf, tkeys, /, *, tkeys_vs_tokens=False):
    ##    '[tkey] -> IRecognizerLLoo'
    ##@abstractmethod
    ##def mk_LLoo__match_constant_tkey(sf, tkey, /, *, tkey_vs_token=False):
    ##    'tkey -> IRecognizerLLoo'

    ##@abstractmethod
    ##def mk_LLoo__match_one_of_tkeys(sf, tkeys, /, *, tkey_vs_token=False):
    ##    '[tkey] -> IRecognizerLLoo'

    ##@abstractmethod
    ##def mk_LLoo__raw_string(sf, set4sep8open, set4sep8close, set4token6tag, /, *, tkeys_vs_tokens=False, oresult_with_tag4raw_string=False):
    ##    'ITokenKeySetQuery -> ITokenKeySetQuery -> ITokenKeySetQuery -> IRecognizerLLoo'

    #######
    @abstractmethod
    def mk_LLoo__any_tkey(sf, nm_or_case4token_extraction='tkey', /):
        '(nm/str|Case4TokenExtraction) -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__tkey_set(sf, token_set_query, /, *, to_invert=False, nm_or_case4token_extraction='tkey'):
        'ITokenSetQuery -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__match_constant_tkeys(sf, tkeys, /, *, nm_or_case4token_extraction='tkey'):
        '[tkey] -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__match_constant_tkey(sf, tkey, /, *, nm_or_case4token_extraction='tkey'):
        'tkey -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__match_one_of_tkeys(sf, tkeys, /, *, nm_or_case4token_extraction='tkey'):
        '[tkey] -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__raw_string(sf, set4sep8open, set4sep8close, set4token6tag, /, *, nm_or_case4token_extraction='tkey', oresult_with_tag4raw_string=False):
        'ITokenKeySetQuery -> ITokenKeySetQuery -> ITokenKeySetQuery -> IRecognizerLLoo'
    #######
    @abstractmethod
    def mk_LLoo__trace(sf, label, /):
        'str -> IRecognizerLLoo'
    @abstractmethod
    def mk_LLoo__traced(sf, rgnr, /, *, may_label6enter=None, may_label6hdr_sgnl=None, may_label6err=None, may_label6ok=None, may_label6exit=None):
        'IRecognizerLLoo -> IRecognizerLLoo'
    #######
    def mk_LLoo__traced__simple(sf, label, rgnr, /):
        'str -> IRecognizerLLoo -> IRecognizerLLoo'
        check_type_is(str, label)
        return sf.mk_LLoo__traced(rgnr
        ,may_label6enter=f'6enter:{label}'
        ,may_label6hdr_sgnl=f'6hdr_sgnl:{label}'
        ,may_label6err=f'6err:{label}'
        ,may_label6ok=f'6ok:{label}'
        ,may_label6exit=f'6exit:{label}'
        )
    ######################
#end-class IFactory4RecognizerLLoo__inputter_is_IForkableForwardInputStream666IToken999(IFactory4RecognizerLLoo__inputter_is_IForkable__stamp):
















######################
######################
######################
#stream<token<char> >
######################
class IFactory4RecognizerLLoo__inputter_is_IForkableForwardInputStream666IToken666IChar999_999(IFactory4RecognizerLLoo__inputter_is_IForkableForwardInputStream666IToken999):
    'factory<combinator_LLoo>#[inputter::IForkableForwardInputStream<IToken<IChar> >]'
    __slots__ = ()
    #.,$s/^,char_set_query__\(\w*\)$/    @property\r    @abstractmethod\r    def char_set_query__\1(sf, \/):\r        '-> ICharTokenKeySetQuery'
    #.,$s/^,recognizer_LLoo__\(\w*\)$/    @property\r    @abstractmethod\r    def recognizer_LLoo__\1(sf, \/):\r        '-> IRecognizerLLoo'

    ######################
    @property
    @abstractmethod
    def char_set_query__regex__w(sf, /):
        '-> ICharTokenKeySetQuery'
    @property
    @abstractmethod
    def char_set_query__regex__W(sf, /):
        '-> ICharTokenKeySetQuery'
    @property
    @abstractmethod
    def char_set_query__regex__s(sf, /):
        '-> ICharTokenKeySetQuery'
    @property
    @abstractmethod
    def char_set_query__regex__S(sf, /):
        '-> ICharTokenKeySetQuery'
    @property
    @abstractmethod
    def char_set_query__regex__d(sf, /):
        '-> ICharTokenKeySetQuery'
    @property
    @abstractmethod
    def char_set_query__regex__D(sf, /):
        '-> ICharTokenKeySetQuery'

    ######################
    @property
    @abstractmethod
    def char_set_query__isalnum(sf, /):
        '-> ICharTokenKeySetQuery'
    @property
    @abstractmethod
    def char_set_query__not_isalnum(sf, /):
        '-> ICharTokenKeySetQuery'
    @property
    @abstractmethod
    def char_set_query__isalpha(sf, /):
        '-> ICharTokenKeySetQuery'
    @property
    @abstractmethod
    def char_set_query__not_isalpha(sf, /):
        '-> ICharTokenKeySetQuery'
    @property
    @abstractmethod
    def char_set_query__isascii(sf, /):
        '-> ICharTokenKeySetQuery'
    @property
    @abstractmethod
    def char_set_query__not_isascii(sf, /):
        '-> ICharTokenKeySetQuery'
    @property
    @abstractmethod
    def char_set_query__isdecimal(sf, /):
        '-> ICharTokenKeySetQuery'
    @property
    @abstractmethod
    def char_set_query__not_isdecimal(sf, /):
        '-> ICharTokenKeySetQuery'
    @property
    @abstractmethod
    def char_set_query__isdigit(sf, /):
        '-> ICharTokenKeySetQuery'
    @property
    @abstractmethod
    def char_set_query__not_isdigit(sf, /):
        '-> ICharTokenKeySetQuery'
    @property
    @abstractmethod
    def char_set_query__isidentifier(sf, /):
        '-> ICharTokenKeySetQuery'
    @property
    @abstractmethod
    def char_set_query__not_isidentifier(sf, /):
        '-> ICharTokenKeySetQuery'
    @property
    @abstractmethod
    def char_set_query__islower(sf, /):
        '-> ICharTokenKeySetQuery'
    @property
    @abstractmethod
    def char_set_query__not_islower(sf, /):
        '-> ICharTokenKeySetQuery'
    @property
    @abstractmethod
    def char_set_query__isnumeric(sf, /):
        '-> ICharTokenKeySetQuery'
    @property
    @abstractmethod
    def char_set_query__not_isnumeric(sf, /):
        '-> ICharTokenKeySetQuery'
    @property
    @abstractmethod
    def char_set_query__isprintable(sf, /):
        '-> ICharTokenKeySetQuery'
    @property
    @abstractmethod
    def char_set_query__not_isprintable(sf, /):
        '-> ICharTokenKeySetQuery'
    @property
    @abstractmethod
    def char_set_query__isspace(sf, /):
        '-> ICharTokenKeySetQuery'
    @property
    @abstractmethod
    def char_set_query__not_isspace(sf, /):
        '-> ICharTokenKeySetQuery'
    @property
    @abstractmethod
    def char_set_query__istitle(sf, /):
        '-> ICharTokenKeySetQuery'
    @property
    @abstractmethod
    def char_set_query__not_istitle(sf, /):
        '-> ICharTokenKeySetQuery'
    @property
    @abstractmethod
    def char_set_query__isupper(sf, /):
        '-> ICharTokenKeySetQuery'
    @property
    @abstractmethod
    def char_set_query__not_isupper(sf, /):
        '-> ICharTokenKeySetQuery'




    ######################
    @property
    @abstractmethod
    def recognizer_LLoo__regex__w(sf, /):
        '-> IRecognizerLLoo'
    @property
    @abstractmethod
    def recognizer_LLoo__regex__W(sf, /):
        '-> IRecognizerLLoo'
    @property
    @abstractmethod
    def recognizer_LLoo__regex__s(sf, /):
        '-> IRecognizerLLoo'
    @property
    @abstractmethod
    def recognizer_LLoo__regex__S(sf, /):
        '-> IRecognizerLLoo'
    @property
    @abstractmethod
    def recognizer_LLoo__regex__d(sf, /):
        '-> IRecognizerLLoo'
    @property
    @abstractmethod
    def recognizer_LLoo__regex__D(sf, /):
        '-> IRecognizerLLoo'


    ######################
    @property
    @abstractmethod
    def recognizer_LLoo__isalnum(sf, /):
        '-> IRecognizerLLoo'
    @property
    @abstractmethod
    def recognizer_LLoo__not_isalnum(sf, /):
        '-> IRecognizerLLoo'
    @property
    @abstractmethod
    def recognizer_LLoo__isalpha(sf, /):
        '-> IRecognizerLLoo'
    @property
    @abstractmethod
    def recognizer_LLoo__not_isalpha(sf, /):
        '-> IRecognizerLLoo'
    @property
    @abstractmethod
    def recognizer_LLoo__isascii(sf, /):
        '-> IRecognizerLLoo'
    @property
    @abstractmethod
    def recognizer_LLoo__not_isascii(sf, /):
        '-> IRecognizerLLoo'
    @property
    @abstractmethod
    def recognizer_LLoo__isdecimal(sf, /):
        '-> IRecognizerLLoo'
    @property
    @abstractmethod
    def recognizer_LLoo__not_isdecimal(sf, /):
        '-> IRecognizerLLoo'
    @property
    @abstractmethod
    def recognizer_LLoo__isdigit(sf, /):
        '-> IRecognizerLLoo'
    @property
    @abstractmethod
    def recognizer_LLoo__not_isdigit(sf, /):
        '-> IRecognizerLLoo'
    @property
    @abstractmethod
    def recognizer_LLoo__isidentifier(sf, /):
        '-> IRecognizerLLoo'
    @property
    @abstractmethod
    def recognizer_LLoo__not_isidentifier(sf, /):
        '-> IRecognizerLLoo'
    @property
    @abstractmethod
    def recognizer_LLoo__islower(sf, /):
        '-> IRecognizerLLoo'
    @property
    @abstractmethod
    def recognizer_LLoo__not_islower(sf, /):
        '-> IRecognizerLLoo'
    @property
    @abstractmethod
    def recognizer_LLoo__isnumeric(sf, /):
        '-> IRecognizerLLoo'
    @property
    @abstractmethod
    def recognizer_LLoo__not_isnumeric(sf, /):
        '-> IRecognizerLLoo'
    @property
    @abstractmethod
    def recognizer_LLoo__isprintable(sf, /):
        '-> IRecognizerLLoo'
    @property
    @abstractmethod
    def recognizer_LLoo__not_isprintable(sf, /):
        '-> IRecognizerLLoo'
    @property
    @abstractmethod
    def recognizer_LLoo__isspace(sf, /):
        '-> IRecognizerLLoo'
    @property
    @abstractmethod
    def recognizer_LLoo__not_isspace(sf, /):
        '-> IRecognizerLLoo'
    @property
    @abstractmethod
    def recognizer_LLoo__istitle(sf, /):
        '-> IRecognizerLLoo'
    @property
    @abstractmethod
    def recognizer_LLoo__not_istitle(sf, /):
        '-> IRecognizerLLoo'
    @property
    @abstractmethod
    def recognizer_LLoo__isupper(sf, /):
        '-> IRecognizerLLoo'
    @property
    @abstractmethod
    def recognizer_LLoo__not_isupper(sf, /):
        '-> IRecognizerLLoo'

    ######################
#end-class IFactory4RecognizerLLoo__inputter_is_IForkableForwardInputStream666IToken666IChar999_999(IFactory4RecognizerLLoo__inputter_is_IForkableForwardInputStream666IToken999):






__all__
from seed.recognize.recognizer_LLoo_.IFactory4RecognizerLLoo import IFactory4RecognizerLLoo__inputter_is_IForkable__stamp, IFactory4RecognizerLLoo__inputter_is_IForkableForwardInputStream666IToken999, IFactory4RecognizerLLoo__inputter_is_IForkableForwardInputStream666IToken666IChar999_999
from seed.recognize.recognizer_LLoo_.IFactory4RecognizerLLoo import *
