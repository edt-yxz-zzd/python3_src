#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/recognizer_LLoo_/Factory4RecognizerLLoo.py
view ../../python3_src/seed/recognize/recognizer_LLoo_/IFactory4RecognizerLLoo.py

seed.recognize.recognizer_LLoo_.Factory4RecognizerLLoo
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_LLoo_.Factory4RecognizerLLoo -x
py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LLoo_.Factory4RecognizerLLoo:__doc__ -ht
#]]]'''
__all__ = r'''
factory4LLoo__basic
factory4LLoo__token_stream
factory4LLoo__char_stream

Factory4RecognizerLLoo__inputter_is_IForkable__stamp
    Factory4RecognizerLLoo__inputter_is_IForkableForwardInputStream666IToken999
        Factory4RecognizerLLoo__inputter_is_IForkableForwardInputStream666IToken666IChar999_999
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
######################
from seed.recognize.recognizer_LLoo_.IFactory4RecognizerLLoo import IFactory4RecognizerLLoo__inputter_is_IForkable__stamp, IFactory4RecognizerLLoo__inputter_is_IForkableForwardInputStream666IToken999, IFactory4RecognizerLLoo__inputter_is_IForkableForwardInputStream666IToken666IChar999_999

from seed.recognize.recognizer_LLoo_._common import (
IForkable, IForkable__stamp
,abstractmethod, override, ABC, ABC__no_slots
)

from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import IRecognizerLLoo# Signal__HeaderCompleted, Reply4IRecognizerLLoo

from seed.recognize.recognizer_LLoo_.stream._common import (IToken
,IForkableForwardInputStream, ForkableForwardInputStream__using_LazyListIter
)



######################
######################
######################
from seed.recognize.recognizer_LLoo_.combinator_LLoo__gi8flow import mk_LLoo__gi8flow__all_in_one
from seed.recognize.recognizer_LLoo_.combinator_LLoo__switch import mk_LLoo__dependent_pair, mk_LLoo__switch_branches, mk_LLoo__if_then_else
from seed.recognize.recognizer_LLoo_.combinator_LLoo__flow import mk_LLoo__flow
from seed.recognize.recognizer_LLoo_.combinator_LLoo__loop import \
(mk_LLoo__base_loop
,mk_LLoo__many
,mk_LLoo__skip_many1
,mk_LLoo__end_by__pre
,mk_LLoo__end_by__post
,mk_LLoo__sep_by
,mk_LLoo__between
)

from seed.recognize.recognizer_LLoo_.combinator_LLoo__parallel import \
(mk_LLoo__the_first_one
    ,mk_LLoo__choice
,mk_LLoo__the_only_one
    ,mk_LLoo__parallel
)
from seed.recognize.recognizer_LLoo_.combinator_LLoo__serial import mk_LLoo__xtuple, mk_LLoo__tuple, mk_LLoo__dependent_tuple

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


######################


######################
######################
######################
#stream<token>
######################
######################
######################
from seed.recognize.recognizer_LLoo_.stream.pure_stream import recognizer_LLoo__eof, recognizer_LLoo__any_token, mk_LLoo__token_set
from seed.recognize.recognizer_LLoo_.stream.token_stream import \
(recognizer_LLoo__any_tkey
,recognizer_LLoo__any_tdat
,recognizer_LLoo__any_tkd
,mk_LLoo__any_tkey
,mk_LLoo__tkey_set
,mk_LLoo__match_constant_tkeys
,mk_LLoo__match_constant_tkey
,mk_LLoo__match_one_of_tkeys
,mk_LLoo__raw_string
,mk_LLoo__trace
,mk_LLoo__traced
#,mk_LLoo__traced__simple
)

######################
######################
######################
#stream<token<char> >
######################
######################
######################
from seed.recognize.recognizer_LLoo_.stream.char_stream import \
(char_set_query__regex__w
,char_set_query__regex__W
,char_set_query__regex__s
,char_set_query__regex__S
,char_set_query__regex__d
,char_set_query__regex__D
)

from seed.recognize.recognizer_LLoo_.stream.char_stream import \
(char_set_query__isalnum
,char_set_query__not_isalnum
,char_set_query__isalpha
,char_set_query__not_isalpha
,char_set_query__isascii
,char_set_query__not_isascii
,char_set_query__isdecimal
,char_set_query__not_isdecimal
,char_set_query__isdigit
,char_set_query__not_isdigit
,char_set_query__isidentifier
,char_set_query__not_isidentifier
,char_set_query__islower
,char_set_query__not_islower
,char_set_query__isnumeric
,char_set_query__not_isnumeric
,char_set_query__isprintable
,char_set_query__not_isprintable
,char_set_query__isspace
,char_set_query__not_isspace
,char_set_query__istitle
,char_set_query__not_istitle
,char_set_query__isupper
,char_set_query__not_isupper
)

from seed.recognize.recognizer_LLoo_.stream.char_stream import \
(recognizer_LLoo__regex__w
,recognizer_LLoo__regex__W
,recognizer_LLoo__regex__s
,recognizer_LLoo__regex__S
,recognizer_LLoo__regex__d
,recognizer_LLoo__regex__D
)

from seed.recognize.recognizer_LLoo_.stream.char_stream import \
(recognizer_LLoo__isalnum
,recognizer_LLoo__not_isalnum
,recognizer_LLoo__isalpha
,recognizer_LLoo__not_isalpha
,recognizer_LLoo__isascii
,recognizer_LLoo__not_isascii
,recognizer_LLoo__isdecimal
,recognizer_LLoo__not_isdecimal
,recognizer_LLoo__isdigit
,recognizer_LLoo__not_isdigit
,recognizer_LLoo__isidentifier
,recognizer_LLoo__not_isidentifier
,recognizer_LLoo__islower
,recognizer_LLoo__not_islower
,recognizer_LLoo__isnumeric
,recognizer_LLoo__not_isnumeric
,recognizer_LLoo__isprintable
,recognizer_LLoo__not_isprintable
,recognizer_LLoo__isspace
,recognizer_LLoo__not_isspace
,recognizer_LLoo__istitle
,recognizer_LLoo__not_istitle
,recognizer_LLoo__isupper
,recognizer_LLoo__not_isupper
)



___end_mark_of_excluded_global_names__0___ = ...



######################
#%s/^ *def \(\w*\)(sf, \([^/]*\), \/..*):\n *'[^']*'$/\0\r        d = dict(locals())\r        for nm in 'sf, \2'.split(', '):\r            del d[nm]\r        return \1(\2, **d)
#%s/^ *def \(\w*\)(sf, \([^/]*\), \/):\n *'[^']*'$/\0\r        return \1(\2)
#%s/^    @abstractmethod/    @override
######################
class Factory4RecognizerLLoo__inputter_is_IForkable__stamp(IFactory4RecognizerLLoo__inputter_is_IForkable__stamp):
    'factory<combinator_LLoo>#[inputter::IForkable__stamp]'
    __slots__ = ()
    @property
    @override
    def recognizer_LLoo__ignore(sf, /):
        '-> IRecognizerLLoo'
        return recognizer_LLoo__ignore
    @property
    @override
    def recognizer_LLoo__pass(sf, /):
        '-> IRecognizerLLoo'
        return recognizer_LLoo__pass
    @property
    @override
    def recognizer_LLoo__fail(sf, /):
        '-> IRecognizerLLoo'
        return recognizer_LLoo__fail
    recognizer_LLoo__ignore
    recognizer_LLoo__pass
    recognizer_LLoo__fail
    ######################
    @override
    def mk_LLoo__gi8flow__all_in_one(sf, all_in_one_ex, args4all_in_one_ex, /):
        '(all_in_one_ex/(case/uint%5 -> (*args4all_in_one_ex) -> result4all_in_one4gi8flow4LLoo(([case==0]gi8flow4LLoo)|([case==1](Iter tribool_skip){len==1})|([case==2](Iter kinded_name))|([case==3](Iter IDependentTreeNode)))) -> args4all_in_one_ex/[arg] -> IRecognizerLLoo'
        return mk_LLoo__gi8flow__all_in_one(all_in_one_ex, args4all_in_one_ex)
    @override
    def mk_LLoo__dependent_pair(sf, rgnr4fst, rgnrXmkr4snd, /):
        'IRecognizerLLoo -> (IRecognizerLLoo|IMaker4RecognizerLLoo__5oresult) -> IRecognizerLLoo{dependent_pair}'
        return mk_LLoo__dependent_pair(rgnr4fst, rgnrXmkr4snd)
    @override
    def mk_LLoo__switch_branches(sf, rgnr4case, rgnrXmkr_ls4branches, /):
        'IRecognizerLLoo{oresult/Cased} -> [(IRecognizerLLoo|IMaker4RecognizerLLoo__5oresult)] -> IRecognizerLLoo'
        return mk_LLoo__switch_branches(rgnr4case, rgnrXmkr_ls4branches)
    @override
    def mk_LLoo__if_then_else(sf, rgnr4if, rgnr_or_mkr4then, rgnr_or_mkr4else, /):
        'IRecognizerLLoo{oresult/Either} -> (IRecognizerLLoo|IMaker4RecognizerLLoo__5oresult) -> (IRecognizerLLoo|IMaker4RecognizerLLoo__5oresult) -> IRecognizerLLoo'
        return mk_LLoo__if_then_else(rgnr4if, rgnr_or_mkr4then, rgnr_or_mkr4else)
    @override
    def mk_LLoo__flow(sf, instructions, may__label2idx4instruction, /):
        r'[IInstruction4flow4LLoo]{len==L} -> may {label/(Hashable\-\int):uint%L} -> IRecognizerLLoo'
    @override
    def mk_LLoo__base_loop(sf, rgnr4body4loop, /, *, to_output_num_loops=False, min_loops=0, imay_max_loops=-1, may_uhidx4hdr:1=None, may_rgnr4end7pre=None, may_rgnr4end7post=None):
        'IRecognizerLLoo -> IRecognizerLLoo'
        d = dict(locals())
        for nm in 'sf, rgnr4body4loop'.split(', '):
            del d[nm]
        return mk_LLoo__base_loop(rgnr4body4loop, **d)
    @override
    def mk_LLoo__many(sf, rgnr4body4loop, /, *, min_loops=0, imay_max_loops=-1, may_uhidx4hdr:1=None):
        'IRecognizerLLoo -> IRecognizerLLoo'
        d = dict(locals())
        for nm in 'sf, rgnr4body4loop'.split(', '):
            del d[nm]
        return mk_LLoo__many(rgnr4body4loop, **d)
    @override
    def mk_LLoo__skip_many1(sf, rgnr4body4loop, /):
        'IRecognizerLLoo -> IRecognizerLLoo'
        return mk_LLoo__skip_many1(rgnr4body4loop)
    @override
    def mk_LLoo__end_by__pre(sf, rgnr4end7pre, rgnr4body4loop, /, *, min_loops=0, imay_max_loops=-1, may_uhidx4hdr:1=None):
        'IRecognizerLLoo -> IRecognizerLLoo -> IRecognizerLLoo'
        d = dict(locals())
        for nm in 'sf, rgnr4end7pre, rgnr4body4loop'.split(', '):
            del d[nm]
        return mk_LLoo__end_by__pre(rgnr4end7pre, rgnr4body4loop, **d)
    @override
    def mk_LLoo__end_by__post(sf, rgnr4end7post, rgnr4body4loop, /, *, min_loops=0, imay_max_loops=-1, may_uhidx4hdr:1=None):
        'IRecognizerLLoo -> IRecognizerLLoo -> IRecognizerLLoo'
        d = dict(locals())
        for nm in 'sf, rgnr4body4loop, rgnr4end7post'.split(', '):
            del d[nm]
        return mk_LLoo__end_by__post(rgnr4end7post, rgnr4body4loop, **d)
    @override
    def mk_LLoo__sep_by(sf, rgnr4sep, rgnr4item, /, *, min_loops=0, imay_max_loops=-1, may_uhidx4hdr:1=None):
        'IRecognizerLLoo -> IRecognizerLLoo -> IRecognizerLLoo'
        d = dict(locals())
        for nm in 'sf, rgnr4sep, rgnr4item'.split(', '):
            del d[nm]
        return mk_LLoo__sep_by(rgnr4sep, rgnr4item, **d)
    @override
    def mk_LLoo__between(sf, rgnr4begin, rgnr4body, rgnr4end, /):
        'IRecognizerLLoo -> IRecognizerLLoo -> IRecognizerLLoo -> IRecognizerLLoo'
        return mk_LLoo__between(rgnr4begin, rgnr4body, rgnr4end)
    @override
    def mk_LLoo__the_first_one(sf, rgnrs, /, *, tagged=False, cased=False, _6oresult_only_=False):
        '-> IRecognizerLLoo #the_first_one/choice'
        d = dict(locals())
        for nm in 'sf, rgnrs'.split(', '):
            del d[nm]
        return mk_LLoo__the_first_one(rgnrs, **d)
    @override
    def mk_LLoo__the_only_one(sf, rgnrs, /, *, tagged=False, cased=False, _6oresult_only_=False):
        '-> IRecognizerLLoo #the_only_one/parallel'
        d = dict(locals())
        for nm in 'sf, rgnrs'.split(', '):
            del d[nm]
        return mk_LLoo__the_only_one(rgnrs, **d)
    #mk_LLoo__choice = mk_LLoo__the_first_one
    #mk_LLoo__parallel = mk_LLoo__the_only_one


    @override
    def mk_LLoo__xtuple(sf, shidx4hdr__or__xs4hdr, xs4whole__or__xs4body, /, *, dependent):
        '(int{-(1+2*L)<=.<(1+2*L)}|[x]) -> [x]{len==L} -> IRecognizerLLoo # [x :: ((IRecognizerLLoo|IMaker4RecognizerLLoo__5ctx) if dependent else IRecognizerLLoo)]'
        d = dict(locals())
        for nm in 'sf, shidx4hdr__or__xs4hdr, xs4whole__or__xs4body'.split(', '):
            del d[nm]
        return mk_LLoo__xtuple(shidx4hdr__or__xs4hdr, xs4whole__or__xs4body, **d)
    @override
    def mk_LLoo__tuple(sf, shidx4hdr__or__rgnrs4hdr, rgnrs4whole__or__rgnrs4body, /):
        '(int{-(1+2*L)<=.<(1+2*L)}|[IRecognizerLLoo]) -> [IRecognizerLLoo]{len==L} -> IRecognizerLLoo'
        return mk_LLoo__tuple(shidx4hdr__or__rgnrs4hdr, rgnrs4whole__or__rgnrs4body)
    @override
    def mk_LLoo__dependent_tuple(sf, shidx4hdr__or__mkrs4hdr, mkrs4whole__or__mkrs4body, /):
        '(int{-(1+2*L)<=.<(1+2*L)}|[(IRecognizerLLoo|IMaker4RecognizerLLoo__5ctx)]) -> [(IRecognizerLLoo|IMaker4RecognizerLLoo__5ctx)]{len==L} -> IRecognizerLLoo'
        return mk_LLoo__dependent_tuple(shidx4hdr__or__mkrs4hdr, mkrs4whole__or__mkrs4body)



    @override
    def mk_LLoo__skip(sf, rgnr, /, *, to_wrap=False):
        'IRecognizerLLoo -> IRecognizerLLoo'
        return mk_LLoo__skip(rgnr, to_wrap=to_wrap)
    @override
    def mk_LLoo__pack(sf, rgnr, /, *, to_wrap=False):
        'IRecognizerLLoo -> IRecognizerLLoo'
        return mk_LLoo__pack(rgnr, to_wrap=to_wrap)
    @override
    def mk_LLoo__unpack(sf, rgnr, /, *, to_wrap=False):
        'IRecognizerLLoo -> IRecognizerLLoo'
        return mk_LLoo__unpack(rgnr, to_wrap=to_wrap)
    @override
    def mk_LLoo__with_tribool_skip(sf, tribool_skip, rgnr, /, *, to_wrap=False):
        'tribool -> IRecognizerLLoo -> IRecognizerLLoo'
        return mk_LLoo__with_tribool_skip(tribool_skip, rgnr, to_wrap=to_wrap)
    @override
    def mk_LLoo__with_tribool_skip_as(sf, rgnr8src, rgnr8dst, /, *, to_wrap=False):
        'IRecognizerLLoo -> IRecognizerLLoo -> IRecognizerLLoo'
        return mk_LLoo__with_tribool_skip_as(rgnr8src, rgnr8dst, to_wrap=to_wrap)

    @override
    def mk_LLoo__simple_postprocess(sf, eresult2eresult_, rgnr, /):
        '(Either -> Either) -> IRecognizerLLoo -> IRecognizerLLoo'
        return mk_LLoo__simple_postprocess(eresult2eresult_, rgnr)
    @override
    def mk_LLoo__simple_postprocess6ok(sf, oresult2oresult_, rgnr, /):
        '(Reply4IRecognizerLLoo.oresult -> oresult) -> IRecognizerLLoo -> IRecognizerLLoo'
        return mk_LLoo__simple_postprocess6ok(oresult2oresult_, rgnr)
    @override
    def mk_LLoo__simple_postprocess6err(sf, errmsg2errmsg_, rgnr, /):
        '(Reply4IRecognizerLLoo.errmsg -> errmsg) -> IRecognizerLLoo -> IRecognizerLLoo'
        return mk_LLoo__simple_postprocess6err(errmsg2errmsg_, rgnr)


    @override
    def mk_LLoo__validate_two_phases(sf, rgnr, /):
        'IRecognizerLLoo -> IRecognizerLLoo'
        return mk_LLoo__validate_two_phases(rgnr)
    @override
    def mk_LLoo__skip_header_signal(sf, rgnr, /):
        'IRecognizerLLoo -> IRecognizerLLoo'
        return mk_LLoo__skip_header_signal(rgnr)
    @override
    def mk_LLoo__header_signal_at_beginning(sf, rgnr, /):
        'IRecognizerLLoo -> IRecognizerLLoo'
        return mk_LLoo__header_signal_at_beginning(rgnr)
    @override
    def mk_LLoo__patch_header_signal_if_ok(sf, rgnr, /):
        'IRecognizerLLoo -> IRecognizerLLoo'
        return mk_LLoo__patch_header_signal_if_ok(rgnr)

    @override
    def mk_LLoo__tag(sf, tag, rgnr, /, *, _6oresult_only_=False):
        'tag -> IRecognizerLLoo -> IRecognizerLLoo'
        return mk_LLoo__tag(tag, rgnr, _6oresult_only_=_6oresult_only_)
    @override
    def mk_LLoo__Cased(sf, case, rgnr, /, *, _6oresult_only_=False):
        'case -> IRecognizerLLoo -> IRecognizerLLoo'
        return mk_LLoo__Cased(case, rgnr, _6oresult_only_=_6oresult_only_)
    @override
    def mk_LLoo__invert_err_ok(sf, rgnr, /):
        'IRecognizerLLoo -> IRecognizerLLoo'
        return mk_LLoo__invert_err_ok(rgnr)

    @override
    def mk_LLoo__unbox(sf, rgnr, /):
        'IRecognizerLLoo -> IRecognizerLLoo'
        return mk_LLoo__unbox(rgnr)


    @override
    def mk_LLoo__try__rollback_if_fail_before_hdr_sgnl_else_lift(sf, rgnr, /):
        'IRecognizerLLoo -> IRecognizerLLoo'
        return mk_LLoo__try__rollback_if_fail_before_hdr_sgnl_else_lift(rgnr)
    @override
    def mk_LLoo__optional__either(sf, rgnr, /):
        'IRecognizerLLoo -> IRecognizerLLoo'
        return mk_LLoo__optional__either(rgnr)
    @override
    def mk_LLoo__optional__tmay(sf, rgnr, /):
        'IRecognizerLLoo -> IRecognizerLLoo'
        return mk_LLoo__optional__tmay(rgnr)
    @override
    def mk_LLoo__optional__default(sf, oresult8default, rgnr, /):
        'default/Reply4IRecognizerLLoo.oresult -> IRecognizerLLoo -> IRecognizerLLoo'
        return mk_LLoo__optional__default(oresult8default, rgnr)

    @override
    def mk_LLoo__look_ahead__no_err4hdr(sf, rgnr, /):
        'IRecognizerLLoo -> IRecognizerLLoo'
        return mk_LLoo__look_ahead__no_err4hdr(rgnr)
    @override
    def mk_LLoo__look_ahead__no_err4whole(sf, rgnr, /):
        'IRecognizerLLoo -> IRecognizerLLoo'
        return mk_LLoo__look_ahead__no_err4whole(rgnr)
    @override
    def mk_LLoo__look_ahead4hdr(sf, rgnr, /):
        'IRecognizerLLoo -> IRecognizerLLoo'
        return mk_LLoo__look_ahead4hdr(rgnr)
    @override
    def mk_LLoo__look_ahead4whole(sf, rgnr, /):
        'IRecognizerLLoo -> IRecognizerLLoo'
        return mk_LLoo__look_ahead4whole(rgnr)
    @override
    def mk_LLoo__not_followed_by4hdr(sf, rgnr, /):
        'IRecognizerLLoo -> IRecognizerLLoo'
        return mk_LLoo__not_followed_by4hdr(rgnr)
    @override
    def mk_LLoo__not_followed_by4whole(sf, rgnr, /):
        'IRecognizerLLoo -> IRecognizerLLoo'
        return mk_LLoo__not_followed_by4whole(rgnr)



    @override
    def mk_LLoo__constant_overwrite6ok(sf, oresult, rgnr, /):
        'Reply4IRecognizerLLoo.oresult -> IRecognizerLLoo -> IRecognizerLLoo'
        return mk_LLoo__constant_overwrite6ok(oresult, rgnr)
    @override
    def mk_LLoo__constant_overwrite6err(sf, errmsg, rgnr, /):
        'Reply4IRecognizerLLoo.errmsg -> IRecognizerLLoo -> IRecognizerLLoo'
        return mk_LLoo__constant_overwrite6err(errmsg, rgnr)
    @override
    def mk_LLoo__constant_overwrite(sf, errmsg, oresult, rgnr, /):
        'Reply4IRecognizerLLoo.the_eresult/Either -> IRecognizerLLoo -> IRecognizerLLoo'
        return mk_LLoo__constant_overwrite(errmsg, oresult, rgnr)


    @override
    def mk_LLoo__constant_eresult(sf, eresult, /, *, tribool_skip=False):
        'Reply4IRecognizerLLoo.the_eresult/Either -> IRecognizerLLoo'
        d = dict(locals())
        for nm in 'sf, eresult'.split(', '):
            del d[nm]
        return mk_LLoo__constant_eresult(eresult, **d)

    @override
    def mk_LLoo__named_wrapper(sf, name, rgnr, /):
        'name -> IRecognizerLLoo -> IRecognizerLLoo'
        return mk_LLoo__named_wrapper(name, rgnr)
    @override
    def mk_LLoo__ref(sf, scene, kinded_name, /):
        'IScene -> kinded_name/Hashable -> IRecognizerLLoo'
        return mk_LLoo__ref(scene, kinded_name)
    @override
    def mk_LLoo__lazy(lazy_or_rgnr, /, *, non_lazy=False):
        r'lazy_or_rgnr/(IRecognizerLLoo if non_lazy else (()->IRecognizerLLoo)) -> (*,non_lazy/bool) -> IRecognizerLLoo'
        return mk_LLoo__lazy(lazy_or_rgnr, non_lazy=non_lazy)
    ######################
#end-class Factory4RecognizerLLoo__inputter_is_IForkable__stamp(IFactory4RecognizerLLoo__inputter_is_IForkable__stamp):














######################
######################
######################
#stream<token>
######################
class Factory4RecognizerLLoo__inputter_is_IForkableForwardInputStream666IToken999(Factory4RecognizerLLoo__inputter_is_IForkable__stamp, IFactory4RecognizerLLoo__inputter_is_IForkableForwardInputStream666IToken999):
    'factory<combinator_LLoo>#[inputter::IForkableForwardInputStream<IToken>]'
    __slots__ = ()
    @property
    @override
    def recognizer_LLoo__eof(sf, /):
        '-> IRecognizerLLoo'
        return recognizer_LLoo__eof
    @property
    @override
    def recognizer_LLoo__any_token(sf, /):
        '-> IRecognizerLLoo'
        return recognizer_LLoo__any_token
    @property
    @override
    def recognizer_LLoo__any_tkey(sf, /):
        '-> IRecognizerLLoo'
        return recognizer_LLoo__any_tkey
    @property
    @override
    def recognizer_LLoo__any_tdat(sf, /):
        '-> IRecognizerLLoo'
        return recognizer_LLoo__any_tdat
    @property
    @override
    def recognizer_LLoo__any_tkd(sf, /):
        '-> IRecognizerLLoo'
        return recognizer_LLoo__any_tkd
    recognizer_LLoo__eof
    recognizer_LLoo__any_token
    recognizer_LLoo__any_tkey
    recognizer_LLoo__any_tdat
    recognizer_LLoo__any_tkd
    ######################
    @override
    def mk_LLoo__token_set(sf, token_set_query, /, *, to_invert=False):
        'ITokenSetQuery -> IRecognizerLLoo'
        return mk_LLoo__token_set(token_set_query, to_invert=to_invert)
    #######
    @override
    def mk_LLoo__any_tkey(sf, nm_or_case4token_extraction='tkey', /):
        '(nm/str|Case4TokenExtraction) -> IRecognizerLLoo'
        return mk_LLoo__any_tkey(nm_or_case4token_extraction)
    @override
    def mk_LLoo__tkey_set(sf, token_set_query, /, *, to_invert=False, nm_or_case4token_extraction='tkey'):
        'ITokenSetQuery -> IRecognizerLLoo'
        return mk_LLoo__tkey_set(token_set_query, to_invert=to_invert, nm_or_case4token_extraction=nm_or_case4token_extraction)
    @override
    def mk_LLoo__match_constant_tkeys(sf, tkeys, /, *, nm_or_case4token_extraction='tkey'):
        '[tkey] -> IRecognizerLLoo'
        return mk_LLoo__match_constant_tkeys(tkeys, nm_or_case4token_extraction=nm_or_case4token_extraction)
    @override
    def mk_LLoo__match_constant_tkey(tkey, /, *, nm_or_case4token_extraction='tkey'):
        'tkey -> IRecognizerLLoo'
        return mk_LLoo__match_constant_tkey(tkey, nm_or_case4token_extraction=nm_or_case4token_extraction)
    @override
    def mk_LLoo__match_one_of_tkeys(sf, tkeys, /, *, nm_or_case4token_extraction='tkey'):
        '[tkey] -> IRecognizerLLoo'
        return mk_LLoo__match_one_of_tkeys(tkeys, nm_or_case4token_extraction=nm_or_case4token_extraction)
    @override
    def mk_LLoo__raw_string(sf, set4sep8open, set4sep8close, set4token6tag, /, *, nm_or_case4token_extraction='tkey', oresult_with_tag4raw_string=False):
        'ITokenKeySetQuery -> ITokenKeySetQuery -> ITokenKeySetQuery -> IRecognizerLLoo'
        return mk_LLoo__raw_string(set4sep8open, set4sep8close, set4token6tag, nm_or_case4token_extraction=nm_or_case4token_extraction, oresult_with_tag4raw_string=oresult_with_tag4raw_string)
    #######
    #@override
    #def mk_LLoo__tkey_set(token_set_query, /, *, to_invert=False):
    #    'ITokenSetQuery -> IRecognizerLLoo'
    #    return mk_LLoo__tkey_set(token_set_query, to_invert=to_invert)
    #@override
    #def mk_LLoo__match_constant_tkeys(sf, tkeys, /, *, tkeys_vs_tokens=False):
    #    '[tkey] -> IRecognizerLLoo'
    #    d = dict(locals())
    #    for nm in 'sf, tkeys'.split(', '):
    #        del d[nm]
    #    return mk_LLoo__match_constant_tkeys(tkeys, **d)
    #@override
    #def mk_LLoo__match_constant_tkey(sf, tkey, /, *, tkey_vs_token=False):
    #    'tkey -> IRecognizerLLoo'
    #    d = dict(locals())
    #    for nm in 'sf, tkey'.split(', '):
    #        del d[nm]
    #    return mk_LLoo__match_constant_tkey(tkey, **d)

    #@override
    #def mk_LLoo__match_one_of_tkeys(sf, tkeys, /, *, tkey_vs_token=False):
    #    '[tkey] -> IRecognizerLLoo'
    #    d = dict(locals())
    #    for nm in 'sf, tkeys'.split(', '):
    #        del d[nm]
    #    return mk_LLoo__match_one_of_tkeys(tkeys, **d)

    #@override
    #def mk_LLoo__raw_string(sf, set4sep8open, set4sep8close, set4token6tag, /, *, tkeys_vs_tokens=False, oresult_with_tag4raw_string=False):
    #    'ITokenKeySetQuery -> ITokenKeySetQuery -> ITokenKeySetQuery -> IRecognizerLLoo'
    #    d = dict(locals())
    #    for nm in 'sf, set4sep8open, set4sep8close, set4token6tag'.split(', '):
    #        del d[nm]
    #    return mk_LLoo__raw_string(set4sep8open, set4sep8close, set4token6tag, **d)
    #######
    @override
    def mk_LLoo__trace(sf, label, /):
        'str -> IRecognizerLLoo'
        return mk_LLoo__trace(label)
    @override
    def mk_LLoo__traced(sf, rgnr, /, *, may_label6enter=None, may_label6hdr_sgnl=None, may_label6err=None, may_label6ok=None, may_label6exit=None):
        'IRecognizerLLoo -> IRecognizerLLoo'
        d = dict(locals())
        for nm in 'sf, rgnr'.split(', '):
            del d[nm]
        return mk_LLoo__traced(rgnr, **d)
    #mk_LLoo__traced__simple
    ######################
#end-class Factory4RecognizerLLoo__inputter_is_IForkableForwardInputStream666IToken999(Factory4RecognizerLLoo__inputter_is_IForkable__stamp, IFactory4RecognizerLLoo__inputter_is_IForkableForwardInputStream666IToken999):





######################
######################
######################
#stream<token<char> >
######################
class Factory4RecognizerLLoo__inputter_is_IForkableForwardInputStream666IToken666IChar999_999(Factory4RecognizerLLoo__inputter_is_IForkableForwardInputStream666IToken999, IFactory4RecognizerLLoo__inputter_is_IForkableForwardInputStream666IToken666IChar999_999):
    'factory<combinator_LLoo>#[inputter::IForkableForwardInputStream<IToken<IChar> >]'
    __slots__ = ()
    #.,$s/^,char_set_query__\(\w*\)$/    @property\r    @override\r    def char_set_query__\1(sf, \/):\r        '-> ICharTokenKeySetQuery'\r        return char_set_query__\1
    #.,$s/^,recognizer_LLoo__\(\w*\)$/    @property\r    @override\r    def recognizer_LLoo__\1(sf, \/):\r        '-> IRecognizerLLoo'\r        return recognizer_LLoo__\1


    ######################
    @property
    @override
    def char_set_query__regex__w(sf, /):
        '-> ICharTokenKeySetQuery'
        return char_set_query__regex__w
    @property
    @override
    def char_set_query__regex__W(sf, /):
        '-> ICharTokenKeySetQuery'
        return char_set_query__regex__W
    @property
    @override
    def char_set_query__regex__s(sf, /):
        '-> ICharTokenKeySetQuery'
        return char_set_query__regex__s
    @property
    @override
    def char_set_query__regex__S(sf, /):
        '-> ICharTokenKeySetQuery'
        return char_set_query__regex__S
    @property
    @override
    def char_set_query__regex__d(sf, /):
        '-> ICharTokenKeySetQuery'
        return char_set_query__regex__d
    @property
    @override
    def char_set_query__regex__D(sf, /):
        '-> ICharTokenKeySetQuery'
        return char_set_query__regex__D


    ######################
    @property
    @override
    def char_set_query__isalnum(sf, /):
        '-> ICharTokenKeySetQuery'
        return char_set_query__isalnum
    @property
    @override
    def char_set_query__not_isalnum(sf, /):
        '-> ICharTokenKeySetQuery'
        return char_set_query__not_isalnum
    @property
    @override
    def char_set_query__isalpha(sf, /):
        '-> ICharTokenKeySetQuery'
        return char_set_query__isalpha
    @property
    @override
    def char_set_query__not_isalpha(sf, /):
        '-> ICharTokenKeySetQuery'
        return char_set_query__not_isalpha
    @property
    @override
    def char_set_query__isascii(sf, /):
        '-> ICharTokenKeySetQuery'
        return char_set_query__isascii
    @property
    @override
    def char_set_query__not_isascii(sf, /):
        '-> ICharTokenKeySetQuery'
        return char_set_query__not_isascii
    @property
    @override
    def char_set_query__isdecimal(sf, /):
        '-> ICharTokenKeySetQuery'
        return char_set_query__isdecimal
    @property
    @override
    def char_set_query__not_isdecimal(sf, /):
        '-> ICharTokenKeySetQuery'
        return char_set_query__not_isdecimal
    @property
    @override
    def char_set_query__isdigit(sf, /):
        '-> ICharTokenKeySetQuery'
        return char_set_query__isdigit
    @property
    @override
    def char_set_query__not_isdigit(sf, /):
        '-> ICharTokenKeySetQuery'
        return char_set_query__not_isdigit
    @property
    @override
    def char_set_query__isidentifier(sf, /):
        '-> ICharTokenKeySetQuery'
        return char_set_query__isidentifier
    @property
    @override
    def char_set_query__not_isidentifier(sf, /):
        '-> ICharTokenKeySetQuery'
        return char_set_query__not_isidentifier
    @property
    @override
    def char_set_query__islower(sf, /):
        '-> ICharTokenKeySetQuery'
        return char_set_query__islower
    @property
    @override
    def char_set_query__not_islower(sf, /):
        '-> ICharTokenKeySetQuery'
        return char_set_query__not_islower
    @property
    @override
    def char_set_query__isnumeric(sf, /):
        '-> ICharTokenKeySetQuery'
        return char_set_query__isnumeric
    @property
    @override
    def char_set_query__not_isnumeric(sf, /):
        '-> ICharTokenKeySetQuery'
        return char_set_query__not_isnumeric
    @property
    @override
    def char_set_query__isprintable(sf, /):
        '-> ICharTokenKeySetQuery'
        return char_set_query__isprintable
    @property
    @override
    def char_set_query__not_isprintable(sf, /):
        '-> ICharTokenKeySetQuery'
        return char_set_query__not_isprintable
    @property
    @override
    def char_set_query__isspace(sf, /):
        '-> ICharTokenKeySetQuery'
        return char_set_query__isspace
    @property
    @override
    def char_set_query__not_isspace(sf, /):
        '-> ICharTokenKeySetQuery'
        return char_set_query__not_isspace
    @property
    @override
    def char_set_query__istitle(sf, /):
        '-> ICharTokenKeySetQuery'
        return char_set_query__istitle
    @property
    @override
    def char_set_query__not_istitle(sf, /):
        '-> ICharTokenKeySetQuery'
        return char_set_query__not_istitle
    @property
    @override
    def char_set_query__isupper(sf, /):
        '-> ICharTokenKeySetQuery'
        return char_set_query__isupper
    @property
    @override
    def char_set_query__not_isupper(sf, /):
        '-> ICharTokenKeySetQuery'
        return char_set_query__not_isupper







    ######################
    @property
    @override
    def recognizer_LLoo__regex__w(sf, /):
        '-> IRecognizerLLoo'
        return recognizer_LLoo__regex__w
    @property
    @override
    def recognizer_LLoo__regex__W(sf, /):
        '-> IRecognizerLLoo'
        return recognizer_LLoo__regex__W
    @property
    @override
    def recognizer_LLoo__regex__s(sf, /):
        '-> IRecognizerLLoo'
        return recognizer_LLoo__regex__s
    @property
    @override
    def recognizer_LLoo__regex__S(sf, /):
        '-> IRecognizerLLoo'
        return recognizer_LLoo__regex__S
    @property
    @override
    def recognizer_LLoo__regex__d(sf, /):
        '-> IRecognizerLLoo'
        return recognizer_LLoo__regex__d
    @property
    @override
    def recognizer_LLoo__regex__D(sf, /):
        '-> IRecognizerLLoo'
        return recognizer_LLoo__regex__D


    ######################
    @property
    @override
    def recognizer_LLoo__isalnum(sf, /):
        '-> IRecognizerLLoo'
        return recognizer_LLoo__isalnum
    @property
    @override
    def recognizer_LLoo__not_isalnum(sf, /):
        '-> IRecognizerLLoo'
        return recognizer_LLoo__not_isalnum
    @property
    @override
    def recognizer_LLoo__isalpha(sf, /):
        '-> IRecognizerLLoo'
        return recognizer_LLoo__isalpha
    @property
    @override
    def recognizer_LLoo__not_isalpha(sf, /):
        '-> IRecognizerLLoo'
        return recognizer_LLoo__not_isalpha
    @property
    @override
    def recognizer_LLoo__isascii(sf, /):
        '-> IRecognizerLLoo'
        return recognizer_LLoo__isascii
    @property
    @override
    def recognizer_LLoo__not_isascii(sf, /):
        '-> IRecognizerLLoo'
        return recognizer_LLoo__not_isascii
    @property
    @override
    def recognizer_LLoo__isdecimal(sf, /):
        '-> IRecognizerLLoo'
        return recognizer_LLoo__isdecimal
    @property
    @override
    def recognizer_LLoo__not_isdecimal(sf, /):
        '-> IRecognizerLLoo'
        return recognizer_LLoo__not_isdecimal
    @property
    @override
    def recognizer_LLoo__isdigit(sf, /):
        '-> IRecognizerLLoo'
        return recognizer_LLoo__isdigit
    @property
    @override
    def recognizer_LLoo__not_isdigit(sf, /):
        '-> IRecognizerLLoo'
        return recognizer_LLoo__not_isdigit
    @property
    @override
    def recognizer_LLoo__isidentifier(sf, /):
        '-> IRecognizerLLoo'
        return recognizer_LLoo__isidentifier
    @property
    @override
    def recognizer_LLoo__not_isidentifier(sf, /):
        '-> IRecognizerLLoo'
        return recognizer_LLoo__not_isidentifier
    @property
    @override
    def recognizer_LLoo__islower(sf, /):
        '-> IRecognizerLLoo'
        return recognizer_LLoo__islower
    @property
    @override
    def recognizer_LLoo__not_islower(sf, /):
        '-> IRecognizerLLoo'
        return recognizer_LLoo__not_islower
    @property
    @override
    def recognizer_LLoo__isnumeric(sf, /):
        '-> IRecognizerLLoo'
        return recognizer_LLoo__isnumeric
    @property
    @override
    def recognizer_LLoo__not_isnumeric(sf, /):
        '-> IRecognizerLLoo'
        return recognizer_LLoo__not_isnumeric
    @property
    @override
    def recognizer_LLoo__isprintable(sf, /):
        '-> IRecognizerLLoo'
        return recognizer_LLoo__isprintable
    @property
    @override
    def recognizer_LLoo__not_isprintable(sf, /):
        '-> IRecognizerLLoo'
        return recognizer_LLoo__not_isprintable
    @property
    @override
    def recognizer_LLoo__isspace(sf, /):
        '-> IRecognizerLLoo'
        return recognizer_LLoo__isspace
    @property
    @override
    def recognizer_LLoo__not_isspace(sf, /):
        '-> IRecognizerLLoo'
        return recognizer_LLoo__not_isspace
    @property
    @override
    def recognizer_LLoo__istitle(sf, /):
        '-> IRecognizerLLoo'
        return recognizer_LLoo__istitle
    @property
    @override
    def recognizer_LLoo__not_istitle(sf, /):
        '-> IRecognizerLLoo'
        return recognizer_LLoo__not_istitle
    @property
    @override
    def recognizer_LLoo__isupper(sf, /):
        '-> IRecognizerLLoo'
        return recognizer_LLoo__isupper
    @property
    @override
    def recognizer_LLoo__not_isupper(sf, /):
        '-> IRecognizerLLoo'
        return recognizer_LLoo__not_isupper

    ######################

#end-class Factory4RecognizerLLoo__inputter_is_IForkableForwardInputStream666IToken666IChar999_999(Factory4RecognizerLLoo__inputter_is_IForkableForwardInputStream666IToken999, IFactory4RecognizerLLoo__inputter_is_IForkableForwardInputStream666IToken666IChar999_999):







factory4LLoo__basic = Factory4RecognizerLLoo__inputter_is_IForkable__stamp()
factory4LLoo__token_stream = Factory4RecognizerLLoo__inputter_is_IForkableForwardInputStream666IToken999()
factory4LLoo__char_stream = Factory4RecognizerLLoo__inputter_is_IForkableForwardInputStream666IToken666IChar999_999()






__all__
from seed.recognize.recognizer_LLoo_.Factory4RecognizerLLoo import Factory4RecognizerLLoo__inputter_is_IForkable__stamp, Factory4RecognizerLLoo__inputter_is_IForkableForwardInputStream666IToken999
from seed.recognize.recognizer_LLoo_.Factory4RecognizerLLoo import factory4LLoo__basic, factory4LLoo__token_stream, factory4LLoo__char_stream
from seed.recognize.recognizer_LLoo_.Factory4RecognizerLLoo import *
