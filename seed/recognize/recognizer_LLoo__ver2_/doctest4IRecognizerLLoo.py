#__all__:goto
r'''[[[
######################
#TODO:goto
#begin_doctest:goto
#end_doctest:goto
######################
e ../../python3_src/seed/recognize/recognizer_LLoo__ver2_/doctest4IRecognizerLLoo.py

py -m seed.recognize.recognizer_LLoo__ver2_.doctest4IRecognizerLLoo
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_LLoo__ver2_.doctest4IRecognizerLLoo -x

py -m nn_ns.app.doctest_cmd    seed.recognize.recognizer_LLoo__ver2_.IRecognizerLLoo:__doc__     seed.recognize.recognizer_LLoo__ver2_.doctest4IRecognizerLLoo:__doc__    -ht -ff

py -m nn_ns.app.doctest_cmd    seed.recognize.recognizer_LLoo__ver2_.IRecognizerLLoo:__doc__     seed.recognize.recognizer_LLoo__ver2_.doctest4IRecognizerLLoo:__doc__    -ht    >  /sdcard/0my_files/tmp/0tmp      2>&1
view /sdcard/0my_files/tmp/0tmp


[[

RecoverableInputStream9LazyList :: uint -> IPositionInfo4Gap -> Iter token -> RecoverableInputStream9LazyList
    def __init__(sf, max_num_tokens6backward, prev_token_end_gap_position_info, nonlazylist_iter_tokens8istream, /):
PlainRecoverableInputStream5token_seq :: uint -> may IPositionInfo4Gap -> uint -> [token] -> PlainRecoverableInputStream5token_seq
    def __init__(sf, max_num_tokens6backward, may_prev_token_end_gap_position_info, offset, token_seq, /):
def mk_token_rawstream__5xs__idx_(offset, xs, ex_arg=None, /, *, tkey_vs_tdat_vs_tkd:'(0|1|2)'):
    'uint -> Iter (tkey|tdat|tkd) -> (((tkey -> tdat)|tdat/non_callable)|((tdat -> tkey)|tkey/non_callable)|None) -> (tkey_vs_tdat_vs_tkd/(0|1|2)) -> rawstream/(IPositionInfo4Gap, Iter IToken)'

def mk_Environment(param2setting, name2rgnr, name2may_gpreprocess, name2may_gpostprocess6err, name2may_gpostprocess6ok, name2force_postprocess_when_ignore, /):
def recognize_(main_rgnr, env, gctx, istream, /, *, ignore=False):
    'IRecognizerLLoo -> env/IEnvironment -> gctx/mapping -> istream/IInputStream -> Reply'#@wrapper

begin_doctest:here
######################
see:IRecognizerLLoo:__doc__
    which should be tested first
    which now be removed from this __doc__ to avoid maintain two copies
######################

######################
>>> _0recognize = recognize_
>>> recognize_ = recognize__asif_main_rgnr_

######################

######################
>>> tkey_vs_tdat_vs_tkd=0; tkn_qset5xqset_=TokenKeyQuerySet5xqset # [tkey :: char]
>>> def _mk_istream5src(src, /):
...     (gap0, iter_tokens) = mk_token_rawstream__5xs__idx_(0, src, tkey_vs_tdat_vs_tkd=tkey_vs_tdat_vs_tkd)
...     #istream = PlainRecoverableInputStream5token_seq(0, gap0, 0, [*iter_tokens])
...     istream = RecoverableInputStream9LazyList(0, gap0, iter_tokens)
...     return istream
>>> env = mk_Environment(param2setting:={}, name2rgnr:={}, name2may_gpreprocess:={}, name2may_gpostprocess6err:={}, name2may_gpostprocess6ok:={}, name2force_postprocess_when_ignore:={})
>>> gctx = {}
>>> mkrs = Makers4IRecognizerLLoo


######################






unitest per mkr@Makers4IRecognizerLLoo:
#######
lookahead_
followed_by_
not_followed_by_

trial_and_error_
protect_header_
protect_whole_
empty8header_
whole8header_

lift__forgivable_
lift__strict_
optional__forgivable_
optional__strict_
#######
light_wrap_rgnr_
light_wrap_

constant_loader_
tag_rgnr_
tag_
not_ignore_
ignore_
none8oresult_if_ignore_

gprepostprocess_
spostprocess_
try_except_else_
try_except_else__spost_

any_token_
eof_
not_eof_
    rgnr__any_token
    rgnr__eof
    rgnr__not_eof
    rgnr__any_tkd
    rgnr__any_tkey
    rgnr__any_tdat
token_
token_seq_

named_
ref_

tkey_prefix_tree_
priority_parallel_
serial_
dependent_pair_
    switch_branches_
    switch_cased_
unbox_tuple_
    between_

repetition_
gsep_end_by_
    end_by_
    many_
    sep_by_
    sep_end_by_

spost__fmap4tuple__tkd2tdat_
spost__fmap4tuple__tkd2tkey_
spost__fmap4tuple__tkn2tdat_
spost__fmap4tuple__tkn2tkd_
spost__fmap4tuple__tkn2tkey_
spost__tkd2tdat_
spost__tkd2tkey_
spost__tkn2tdat_
spost__tkn2tkd_
spost__tkn2tkey_
spost__unbox_

main_
main__split_teardown_
lazy_alias_
lazy_alias_rgnr__human_

TODO
:non_tested-yet:
    gsep_end_by_:see:many_,...
    try_except_else_:++strict_vs_forgivable:non_tested
    try_except_else__spost_:++strict_vs_forgivable:non_tested
#######


>>> rgnr8digit = mkrs.spost__tkn2tkey_(mkrs.token_(tkn_qset5xqset_(char_qset__isdecimal)))
>>> rgnr8pair = mkrs.serial_([rgnr8digit, False, rgnr8digit])
>>> rgnr8_pair = mkrs.serial_([False, rgnr8digit, rgnr8digit])
>>> sym_plus = mkrs.spost__tkn2tkey_(mkrs.token_(tkn_qset5xqset_(Tester__eq_obj('+')))) #
>>> sym_dot = mkrs.spost__tkn2tkey_(mkrs.token_(tkn_qset5xqset_(Tester__eq_obj('.')))) #
>>> sym6 = mkrs.spost__tkn2tkey_(mkrs.token_(tkn_qset5xqset_(Tester__eq_obj('(')))) #')('
>>> sym9 = mkrs.spost__tkn2tkey_(mkrs.token_(tkn_qset5xqset_(Tester__eq_obj(')')))) #

#######
#######
# begin-light_wrap_rgnr_()
#######
#######

#######
>>> main_rgnr = rgnr8digit
>>> istream = _mk_istream5src('69')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(True, '6'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

#+ignore cancel spost__tkn2tkey_, hence got tkn/Token__keyed:
>>> istream = _mk_istream5src('69')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
Reply(Either(True, Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('6', None))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('x69')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True



#######
>>> main_rgnr = mkrs.lookahead_(rgnr8digit)
>>> istream = _mk_istream5src('69')
>>> recognize_(main_rgnr, env, gctx, istream) # [not ignore=>'6'] #doctest: +ELLIPSIS
Reply(Either(True, '6'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('x69')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True

#######
>>> main_rgnr = mkrs.followed_by_(rgnr8digit)
>>> istream = _mk_istream5src('69')
>>> recognize_(main_rgnr, env, gctx, istream) # [ignore=>Token__keyed] #doctest: +ELLIPSIS
Reply(Either(True, Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('6', None))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('x69')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True

#######
>>> main_rgnr = mkrs.not_followed_by_(rgnr8digit)
>>> istream = _mk_istream5src('69')
>>> recognize_(main_rgnr, env, gctx, istream) # [ignore=>Token__keyed] #doctest: +ELLIPSIS
Reply(Either(False, Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('6', None))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('x69')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(True, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(True, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True


#######
>>> main_rgnr = rgnr8pair
>>> istream = _mk_istream5src('69')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(True, ('6', '9')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('6x9')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('x69')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('6')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True


#######
>>> main_rgnr = mkrs.trial_and_error_(rgnr8pair)
>>> istream = _mk_istream5src('69')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(True, ('6', '9')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('6x9')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('x69')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('6')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True


#######
#protect_header_ === trial_and_error_
>>> main_rgnr = mkrs.protect_header_(rgnr8pair)
>>> istream = _mk_istream5src('69')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(True, ('6', '9')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('6x9')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('x69')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('6')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True



#######
>>> main_rgnr = mkrs.protect_whole_(rgnr8pair)
>>> istream = _mk_istream5src('69')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(True, ('6', '9')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('6x9')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('x69')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('6')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True

#######
# (protect_header_ . whole8header_) === protect_whole_
>>> main_rgnr = mkrs.protect_header_(mkrs.whole8header_(rgnr8pair))
>>> istream = _mk_istream5src('69')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(True, ('6', '9')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('6x9')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('x69')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('6')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True


#######
>>> main_rgnr = rgnr8_pair
>>> istream = _mk_istream5src('69')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(True, ('6', '9')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('6x9')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('x69')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('6')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True



#######
# trial_and_error_(rgnr8_pair) == rgnr8_pair
>>> main_rgnr = mkrs.trial_and_error_(rgnr8_pair)
>>> istream = _mk_istream5src('69')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(True, ('6', '9')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('6x9')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('x69')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('6')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True




#######
# trial_and_error_(empty8header_(rgnr8_pair)) == trial_and_error_(rgnr8_pair) == rgnr8_pair
>>> main_rgnr = mkrs.trial_and_error_(mkrs.empty8header_(rgnr8_pair))
>>> istream = _mk_istream5src('69')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(True, ('6', '9')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('6x9')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('x69')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('6')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True



#######
#######
# payload4lifted_eresult = (reply5child, maynotlow_sexconfig, ext_info8begin)
#######
>>> main_rgnr = mkrs.lift__forgivable_(mkrs.protect_header_(rgnr8pair))
>>> istream = _mk_istream5src('69')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(True, (Reply(Either(True, ('6', '9')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2))), ((unlocker_into__snapshot_none, no_seekback), (unprotected_severe_ok, unprotected_severe_ok)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('6x9')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2))), ((unlocker_into__snapshot_none, no_seekback), (unprotected_severe_fail, unprotected_severe_fail)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('x69')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(True, (Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0))), ((unlocker_into__snapshot_none, no_seekback), (protected_forgivable_fail, unprotected_forgivable_ok)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('6')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1))), ((unlocker_into__snapshot_none, no_seekback), (unprotected_severe_fail, unprotected_severe_fail)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(True, (Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0))), ((unlocker_into__snapshot_none, no_seekback), (protected_forgivable_fail, unprotected_forgivable_ok)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True




#######
>>> main_rgnr = mkrs.lift__strict_(mkrs.protect_header_(rgnr8pair))
>>> istream = _mk_istream5src('69')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(True, (Reply(Either(True, ('6', '9')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2))), ((unlocker_into__snapshot_none, no_seekback), (unprotected_severe_ok, unprotected_severe_ok)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('6x9')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2))), ((unlocker_into__snapshot_none, no_seekback), (unprotected_severe_fail, unprotected_severe_fail)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('x69')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(True, (Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0))), ((unlocker_into__snapshot_none, no_seekback), (protected_forgivable_fail, unprotected_forgivable_ok)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('6')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1))), ((unlocker_into__snapshot_none, no_seekback), (unprotected_severe_fail, unprotected_severe_fail)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(True, (Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0))), ((unlocker_into__snapshot_none, no_seekback), (protected_forgivable_fail, unprotected_forgivable_ok)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True







#######
#rgnr8pair-->rgnr8_pair
>>> main_rgnr = mkrs.lift__forgivable_(mkrs.protect_header_(rgnr8_pair))
>>> istream = _mk_istream5src('69')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(True, (Reply(Either(True, ('6', '9')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2))), ((unlocker_into__snapshot_none, no_seekback), (unprotected_severe_ok, unprotected_severe_ok)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('6x9')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2))), ((unlocker_into__snapshot_none, no_seekback), (unprotected_severe_fail, unprotected_severe_fail)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('x69')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1))), ((unlocker_into__snapshot_none, no_seekback), (unprotected_severe_fail, unprotected_severe_fail)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('6')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1))), ((unlocker_into__snapshot_none, no_seekback), (unprotected_severe_fail, unprotected_severe_fail)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

#forgivable-->True#ok
>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(True, (Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0))), ((unlocker_into__snapshot_none, no_seekback), (unprotected_forgivable_fail, unprotected_forgivable_ok)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True




#######
#rgnr8pair-->rgnr8_pair
>>> main_rgnr = mkrs.lift__strict_(mkrs.protect_header_(rgnr8_pair))
>>> istream = _mk_istream5src('69')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(True, (Reply(Either(True, ('6', '9')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2))), ((unlocker_into__snapshot_none, no_seekback), (unprotected_severe_ok, unprotected_severe_ok)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('6x9')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2))), ((unlocker_into__snapshot_none, no_seekback), (unprotected_severe_fail, unprotected_severe_fail)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('x69')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1))), ((unlocker_into__snapshot_none, no_seekback), (unprotected_severe_fail, unprotected_severe_fail)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('6')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1))), ((unlocker_into__snapshot_none, no_seekback), (unprotected_severe_fail, unprotected_severe_fail)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

#strict-->False#fail
>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0))), ((unlocker_into__snapshot_none, no_seekback), (unprotected_forgivable_fail, unprotected_forgivable_fail)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True








#######
>>> main_rgnr = mkrs.optional__forgivable_(mkrs.protect_header_(rgnr8pair))
>>> istream = _mk_istream5src('69')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(True, (('6', '9'),)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('6x9')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

#protected=>ok
>>> istream = _mk_istream5src('x69')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('6')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True




#######
>>> main_rgnr = mkrs.optional__strict_(mkrs.protect_header_(rgnr8pair))
>>> istream = _mk_istream5src('69')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(True, (('6', '9'),)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('6x9')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

#protected=>ok
>>> istream = _mk_istream5src('x69')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('6')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True







#######
#rgnr8pair-->rgnr8_pair
>>> main_rgnr = mkrs.optional__forgivable_(mkrs.protect_header_(rgnr8_pair))
>>> istream = _mk_istream5src('69')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(True, (('6', '9'),)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('6x9')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

#why_fail??
#   rgnr8_pair.unprotected=>fail
>>> istream = _mk_istream5src('x69')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('6')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

#forgivable-->True#ok
>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True




#######
#rgnr8pair-->rgnr8_pair
>>> main_rgnr = mkrs.optional__strict_(mkrs.protect_header_(rgnr8_pair))
>>> istream = _mk_istream5src('69')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(True, (('6', '9'),)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('6x9')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

#why_fail??
#   rgnr8_pair.unprotected=>fail
>>> istream = _mk_istream5src('x69')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('6')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

#strict-->False#fail
>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True



#######
#######
# end-light_wrap_rgnr_()
#######
#######

#######
#light_wrap_,light_wrap_rgnr_
>>> mkrs.light_wrap_ is RecognizerLLoo__light_wrap is not light_wrap_rgnr_ is mkrs.light_wrap_rgnr_
True

>>> repr(mkrs.light_wrap_(rgnr8digit, *get_info_ex4high_freq_sconfigpack_(forbid_xxx_protected_ok, 'trial_and_error'))) == repr(mkrs.trial_and_error_(rgnr8digit))
True
>>> repr(mkrs.light_wrap_rgnr_(rgnr8digit, 'trial_and_error')) == repr(mkrs.trial_and_error_(rgnr8digit))
True
>>> repr(mkrs.light_wrap_rgnr_(rgnr8digit, 'whole8header', 'protect_header')) == repr(mkrs.protect_header_(mkrs.whole8header_(rgnr8digit)))
True

#######
#NOTE:ignore
>>> main_rgnr = mkrs.constant_loader_(mk_Right(999))
>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
Reply(Either(True, 999), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True

#######
# tag_rgnr_ === (flip tag_)
>>> repr(mkrs.tag_(rgnr8digit, 666)) == repr(mkrs.tag_rgnr_(666, rgnr8digit))
True

#NOTE:ignore
>>> main_rgnr = mkrs.tag_(mkrs.constant_loader_(mk_Right(999)), 666)
>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
Reply(Either(True, Cased(666, 999)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True

#######
>>> main_rgnr = mkrs.none8oresult_if_ignore_(rgnr8digit)
>>> istream = _mk_istream5src('7')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(True, '7'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('x')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True

#######
>>> main_rgnr = mkrs.not_ignore_(mkrs.none8oresult_if_ignore_(rgnr8digit))
>>> istream = _mk_istream5src('7')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
Reply(Either(True, '7'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('x')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True



#######
>>> main_rgnr = mkrs.ignore_(mkrs.none8oresult_if_ignore_(rgnr8digit))
>>> istream = _mk_istream5src('7')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('x')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True


#######

#######
#######
#>>> ignored_rgnr8digit = mkrs.ignore_(rgnr8digit)
>>> rgnr8noneXdigit = mkrs.none8oresult_if_ignore_(rgnr8digit)

>>> gpre_666_None = mk_gpreprocess__5constant_(666, None)
>>> gpre_666_True = mk_gpreprocess__5constant_(666, True)
>>> gpre_666_False = mk_gpreprocess__5constant_(666, False)

>>> gpost6err = mk_gpostprocess6err__5spost_after_tag_st_(mk_Left)
>>> gpost6ok = mk_gpostprocess6ok__5spost_after_tag_st_(mk_Right)

#######
#######
#begin-gprepostprocess_()
#NOTE:ignore
#######

#######
#gprepostprocess_:ignore=False
#######
>>> main_rgnr = mkrs.gprepostprocess_(rgnr8noneXdigit, None, None, None)
>>> istream = _mk_istream5src('7')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
Reply(Either(True, '7'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True

#######
>>> main_rgnr = mkrs.gprepostprocess_(rgnr8noneXdigit, gpre_666_None, gpost6err, gpost6ok)
>>> istream = _mk_istream5src('7')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
Reply(Either(True, Either(True, (666, '7'))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
Reply(Either(False, Either(False, (666, 'eof'))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True

#######
>>> main_rgnr = mkrs.gprepostprocess_(rgnr8noneXdigit, gpre_666_True, gpost6err, gpost6ok)
>>> istream = _mk_istream5src('7')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True

#######
>>> main_rgnr = mkrs.gprepostprocess_(rgnr8noneXdigit, gpre_666_False, gpost6err, gpost6ok)
>>> istream = _mk_istream5src('7')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
Reply(Either(True, Either(True, (666, '7'))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
Reply(Either(False, Either(False, (666, 'eof'))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True



#######
#gprepostprocess_:ignore=True
#######
>>> main_rgnr = mkrs.gprepostprocess_(rgnr8noneXdigit, None, None, None)
>>> istream = _mk_istream5src('7')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True

#######
>>> main_rgnr = mkrs.gprepostprocess_(rgnr8noneXdigit, gpre_666_None, gpost6err, gpost6ok)
>>> istream = _mk_istream5src('7')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True

#######
>>> main_rgnr = mkrs.gprepostprocess_(rgnr8noneXdigit, gpre_666_True, gpost6err, gpost6ok)
>>> istream = _mk_istream5src('7')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True

#######
>>> main_rgnr = mkrs.gprepostprocess_(rgnr8noneXdigit, gpre_666_False, gpost6err, gpost6ok)
>>> istream = _mk_istream5src('7')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True


#######
#end-gprepostprocess_()
#######



#######
>>> spost6err = mk_Left
>>> spost6ok = mk_Right

#######
#spostprocess_:ignore=False
>>> main_rgnr = mkrs.spostprocess_(rgnr8digit, spost6err, spost6ok)
>>> istream = _mk_istream5src('7')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
Reply(Either(True, Either(True, '7')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
Reply(Either(False, Either(False, 'eof')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True



#######
#spostprocess_:ignore=True
>>> main_rgnr = mkrs.spostprocess_(rgnr8digit, spost6err, spost6ok)
>>> istream = _mk_istream5src('7')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
Reply(Either(True, Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('7', None))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True




#######
# try_except_else_(..., False) ~=~ try_except_else__spost_(..., False, None, None, False)
>>> r3 = (rgnr8noneXdigit, mkrs.none8oresult_if_ignore_(sym_plus), rgnr8noneXdigit)

#######
>>> main_rgnr = mkrs.try_except_else_(*r3)

#######
#try_except_else_:ignore=False
>>> istream = _mk_istream5src('77')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
Reply(Either(True, Either(True, ('7', '7'))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('7+')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('+', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('+x')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
Reply(Either(True, Either(False, '+')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('7')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True



#######
#try_except_else_:ignore=True
>>> istream = _mk_istream5src('77')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
Reply(Either(True, Either(True, (None, None))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('7+')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('+', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('+x')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
Reply(Either(True, Either(False, None)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('7')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True



#######
#######
>>> main_rgnr = mkrs.try_except_else__spost_(*r3, False, None, None, False)

#######
#try_except_else__spost_~=~try_except_else_:ignore=False
>>> istream = _mk_istream5src('77')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
Reply(Either(True, Either(True, ('7', '7'))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('7+')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('+', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('+x')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
Reply(Either(True, Either(False, '+')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('7')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True



#######
#try_except_else__spost_~=~try_except_else_:ignore=True
>>> istream = _mk_istream5src('77')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
Reply(Either(True, Either(True, (None, None))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('7+')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('+', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('+x')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
Reply(Either(True, Either(False, None)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('7')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True





#######
#######
>>> spost6ok6exc = mk_Left
>>> spost6ok6trial_else = mk_Right

#######
>>> main_rgnr = mkrs.try_except_else__spost_(*r3, False, spost6ok6exc, spost6ok6trial_else, False)

#######
#try_except_else__spost_~=~try_except_else_:ignore=False
>>> istream = _mk_istream5src('77')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
Reply(Either(True, Either(True, Either(True, ('7', '7')))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('7+')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('+', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('+x')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
Reply(Either(True, Either(False, Either(False, '+'))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('7')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True



#######
#try_except_else__spost_~=~try_except_else_:ignore=True
>>> istream = _mk_istream5src('77')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
Reply(Either(True, Either(True, (None, None))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('7+')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('+', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('+x')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
Reply(Either(True, Either(False, None)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('7')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
>>> istream.tell_ext_info() == _.ext_info8end
True

>>> istream = _mk_istream5src('')
>>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> istream.tell_ext_info() == _.ext_info8end
True



#######
#######
#++NOTE:ignore,_force_postprocess_when_ignore_
    gprepostprocess_
    spostprocess_
    try_except_else_
    try_except_else__spost_
#begin-test:ignore,_force_postprocess_when_ignore_

[[[
#_force_postprocess_when_ignore_:=True
#   __changed:goto
===
    #######
    #######
    #begin-gprepostprocess_()
    #NOTE:ignore
    #######

    #######
    #gprepostprocess_:ignore=False
    #######
    #######
    >>> main_rgnr = mkrs.gprepostprocess_(rgnr8noneXdigit, gpre_666_None, gpost6err, gpost6ok, _force_postprocess_when_ignore_:=True)
    >>> istream = _mk_istream5src('7')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
    Reply(Either(True, Either(True, (666, '7'))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True

    >>> istream = _mk_istream5src('')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
    Reply(Either(False, Either(False, (666, 'eof'))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True

    #######
    >>> main_rgnr = mkrs.gprepostprocess_(rgnr8noneXdigit, gpre_666_True, gpost6err, gpost6ok, _force_postprocess_when_ignore_:=True)
    >>> istream = _mk_istream5src('7')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #__changed #doctest: +ELLIPSIS
    Reply(Either(True, Either(True, (666, None))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True

    >>> istream = _mk_istream5src('')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #__changed #doctest: +ELLIPSIS
    Reply(Either(False, Either(False, (666, 'eof'))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True

    #######
    >>> main_rgnr = mkrs.gprepostprocess_(rgnr8noneXdigit, gpre_666_False, gpost6err, gpost6ok, _force_postprocess_when_ignore_:=True)
    >>> istream = _mk_istream5src('7')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
    Reply(Either(True, Either(True, (666, '7'))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True

    >>> istream = _mk_istream5src('')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
    Reply(Either(False, Either(False, (666, 'eof'))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True



    #######
    #gprepostprocess_:ignore=True
    #######
    >>> main_rgnr = mkrs.gprepostprocess_(rgnr8noneXdigit, None, None, None, _force_postprocess_when_ignore_:=True)
    >>> istream = _mk_istream5src('7')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
    Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True

    >>> istream = _mk_istream5src('')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
    Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True

    #######
    >>> main_rgnr = mkrs.gprepostprocess_(rgnr8noneXdigit, gpre_666_None, gpost6err, gpost6ok, _force_postprocess_when_ignore_:=True)
    >>> istream = _mk_istream5src('7')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #__changed #doctest: +ELLIPSIS
    Reply(Either(True, Either(True, (666, None))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True

    >>> istream = _mk_istream5src('')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #__changed #doctest: +ELLIPSIS
    Reply(Either(False, Either(False, (666, 'eof'))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True

    #######
    >>> main_rgnr = mkrs.gprepostprocess_(rgnr8noneXdigit, gpre_666_True, gpost6err, gpost6ok, _force_postprocess_when_ignore_:=True)
    >>> istream = _mk_istream5src('7')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #__changed #doctest: +ELLIPSIS
    Reply(Either(True, Either(True, (666, None))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True

    >>> istream = _mk_istream5src('')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #__changed #doctest: +ELLIPSIS
    Reply(Either(False, Either(False, (666, 'eof'))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True

    #######
    >>> main_rgnr = mkrs.gprepostprocess_(rgnr8noneXdigit, gpre_666_False, gpost6err, gpost6ok, _force_postprocess_when_ignore_:=True)
    >>> istream = _mk_istream5src('7')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #__changed #doctest: +ELLIPSIS
    Reply(Either(True, Either(True, (666, '7'))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True

    >>> istream = _mk_istream5src('')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #__changed #doctest: +ELLIPSIS
    Reply(Either(False, Either(False, (666, 'eof'))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True


    #######
    #end-gprepostprocess_()
    #######



    #######
    >>> spost6err = mk_Left
    >>> spost6ok = mk_Right

    #######
    #spostprocess_:ignore=False
    >>> main_rgnr = mkrs.spostprocess_(rgnr8digit, spost6err, spost6ok, _force_postprocess_when_ignore_:=True)
    >>> istream = _mk_istream5src('7')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
    Reply(Either(True, Either(True, '7')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True

    >>> istream = _mk_istream5src('')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
    Reply(Either(False, Either(False, 'eof')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True



    #######
    #spostprocess_:ignore=True
    >>> main_rgnr = mkrs.spostprocess_(rgnr8digit, spost6err, spost6ok, _force_postprocess_when_ignore_:=True)
    >>> istream = _mk_istream5src('7')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #__changed #doctest: +ELLIPSIS
    Reply(Either(True, Either(True, Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('7', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True

    >>> istream = _mk_istream5src('')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #__changed #doctest: +ELLIPSIS
    Reply(Either(False, Either(False, 'eof')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True




    #######
    # try_except_else_(..., False) ~=~ try_except_else__spost_(..., False, None, None, False)
    >>> r3 = (rgnr8noneXdigit, mkrs.none8oresult_if_ignore_(sym_plus), rgnr8noneXdigit)

    #######
    >>> main_rgnr = mkrs.try_except_else_(*r3, _force_postprocess_when_ignore_:=True)

    #######
    #try_except_else_:ignore=False
    >>> istream = _mk_istream5src('77')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
    Reply(Either(True, Either(True, ('7', '7'))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True

    >>> istream = _mk_istream5src('7+')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
    Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('+', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True

    >>> istream = _mk_istream5src('+x')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
    Reply(Either(True, Either(False, '+')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True

    >>> istream = _mk_istream5src('7')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
    Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True

    >>> istream = _mk_istream5src('')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
    Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True



    #######
    #try_except_else_:ignore=True
    >>> istream = _mk_istream5src('77')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
    Reply(Either(True, Either(True, (None, None))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True

    >>> istream = _mk_istream5src('7+')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
    Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('+', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True

    >>> istream = _mk_istream5src('+x')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
    Reply(Either(True, Either(False, None)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True

    >>> istream = _mk_istream5src('7')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
    Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True

    >>> istream = _mk_istream5src('')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
    Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True



    #######
    #######
    >>> main_rgnr = mkrs.try_except_else__spost_(*r3, False, None, None, _force_postprocess_when_ignore_:=True)

    #######
    #try_except_else__spost_~=~try_except_else_:ignore=False
    >>> istream = _mk_istream5src('77')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
    Reply(Either(True, Either(True, ('7', '7'))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True

    >>> istream = _mk_istream5src('7+')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
    Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('+', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True

    >>> istream = _mk_istream5src('+x')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
    Reply(Either(True, Either(False, '+')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True

    >>> istream = _mk_istream5src('7')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
    Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True

    >>> istream = _mk_istream5src('')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
    Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True



    #######
    #try_except_else__spost_~=~try_except_else_:ignore=True
    >>> istream = _mk_istream5src('77')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
    Reply(Either(True, Either(True, (None, None))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True

    >>> istream = _mk_istream5src('7+')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
    Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('+', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True

    >>> istream = _mk_istream5src('+x')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
    Reply(Either(True, Either(False, None)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True

    >>> istream = _mk_istream5src('7')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
    Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True

    >>> istream = _mk_istream5src('')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
    Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True





    #######
    #######
    >>> spost6ok6exc = mk_Left
    >>> spost6ok6trial_else = mk_Right

    #######
    >>> main_rgnr = mkrs.try_except_else__spost_(*r3, False, spost6ok6exc, spost6ok6trial_else, _force_postprocess_when_ignore_:=True)

    #######
    #try_except_else__spost_~=~try_except_else_:ignore=False
    >>> istream = _mk_istream5src('77')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
    Reply(Either(True, Either(True, Either(True, ('7', '7')))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True

    >>> istream = _mk_istream5src('7+')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
    Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('+', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True

    >>> istream = _mk_istream5src('+x')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
    Reply(Either(True, Either(False, Either(False, '+'))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True

    >>> istream = _mk_istream5src('7')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
    Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True

    >>> istream = _mk_istream5src('')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=False) #doctest: +ELLIPSIS
    Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True



    #######
    #try_except_else__spost_~=~try_except_else_:ignore=True
    >>> istream = _mk_istream5src('77')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #__changed #doctest: +ELLIPSIS
    Reply(Either(True, Either(True, Either(True, (None, None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True

    >>> istream = _mk_istream5src('7+')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
    Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('+', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True

    >>> istream = _mk_istream5src('+x')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #__changed #doctest: +ELLIPSIS
    Reply(Either(True, Either(False, Either(False, None))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True

    >>> istream = _mk_istream5src('7')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
    Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True

    >>> istream = _mk_istream5src('')
    >>> recognize_(main_rgnr, env, gctx, istream, ignore=True) #doctest: +ELLIPSIS
    Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
    >>> istream.tell_ext_info() == _.ext_info8end
    True




===
]]]



#end-test:ignore,_force_postprocess_when_ignore_


#######
>>> repr(mkrs.any_token_()) == repr(mkrs.rgnr__any_token)
True
>>> repr(mkrs.eof_()) == repr(mkrs.rgnr__eof)
True
>>> repr(mkrs.not_eof_()) == repr(mkrs.rgnr__not_eof)
True
>>> def _1test_(main_rgnr, src, /, *, ignore=False, not_Reply=False):
...     istream = _mk_istream5src(src)
...     reply = recognize_(main_rgnr, env, gctx, istream, ignore=ignore)
...     if not not_Reply:assert istream.tell_ext_info() == reply.ext_info8end
...     return reply
>>> def _3test_(main_rgnr, src, /):
...     #NOTE:ignore,protect_header_
...     print(_1test_(main_rgnr, src))
...     print(_1test_(mkrs.protect_header_(main_rgnr), src))
...     print(_1test_(main_rgnr, src, ignore=True))
>>> def _333test_(main_rgnr, src, /, *srcs):
...     print(repr(src))
...     _3test_(main_rgnr, src)
...     for src in srcs:
...         print('%%%%%%%%%%')
...         print(repr(src))
...         _3test_(main_rgnr, src)
>>> def _111test_(main_rgnr, src, /, *srcs):
...     print(repr(src))
...     print(_1test_(main_rgnr, src))
...     for src in srcs:
...         print('----------')
...         print(repr(src))
...         print(_1test_(main_rgnr, src))



#######
>>> main_rgnr = mkrs.rgnr__any_token
>>> _3test_(main_rgnr, '7') #doctest: +ELLIPSIS
Reply(Either(True, Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('7', None))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('7', None))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('7', None))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))

>>> _3test_(main_rgnr, '') #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))


#######
>>> main_rgnr = mkrs.rgnr__any_tkd
>>> _1test_(main_rgnr, '7') #doctest: +ELLIPSIS
Reply(Either(True, Cased('7', None)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))

#######
>>> main_rgnr = mkrs.rgnr__any_tdat
>>> _1test_(main_rgnr, '7') #doctest: +ELLIPSIS
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))

#######
>>> main_rgnr = mkrs.rgnr__any_tkey
>>> _3test_(main_rgnr, '7') #doctest: +ELLIPSIS
Reply(Either(True, '7'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, '7'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('7', None))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))

>>> _3test_(main_rgnr, '') #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))



#######
>>> main_rgnr = mkrs.rgnr__eof
>>> _3test_(main_rgnr, '7') #doctest: +ELLIPSIS
Reply(Either(False, 'not_eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, 'not_eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, 'not_eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))

>>> _3test_(main_rgnr, '') #doctest: +ELLIPSIS
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))


#######
>>> main_rgnr = mkrs.rgnr__not_eof
>>> _3test_(main_rgnr, '7') #doctest: +ELLIPSIS
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))

>>> _3test_(main_rgnr, '') #doctest: +ELLIPSIS
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))





#######
#token_()
>>> repr(rgnr8digit) == repr(mkrs.spost__tkn2tkey_(mkrs.token_(tkn_qset5xqset_(char_qset__isdecimal))))
True
>>> _333test_(main_rgnr:=rgnr8digit, '7', 'x', '') #doctest: +ELLIPSIS
'7'
Reply(Either(True, '7'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, '7'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('7', None))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
%%%%%%%%%%
'x'
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
%%%%%%%%%%
''
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))


#######
#token_seq_()
>>> main_rgnr = mkrs.token_seq_([tkn_qset5xqset_(char_qset__isdecimal), tkn_qset5xqset_(Tester__eq_obj('+'))])
>>> _333test_(main_rgnr, '7+', '7', '+', '') #doctest: +ELLIPSIS
'7+'
Reply(Either(True, (Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('7', None)), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('+', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(True, (Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('7', None)), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('+', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(True, (Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('7', None)), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('+', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
%%%%%%%%%%
'7'
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
%%%%%%%%%%
'+'
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
%%%%%%%%%%
''
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))


>>> main_rgnr = mkrs.token_seq_([tkn_qset5xqset_(char_qset__isdecimal)])
>>> _333test_(main_rgnr, '7', '+', '') #doctest: +ELLIPSIS
'7'
Reply(Either(True, (Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('7', None)),)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, (Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('7', None)),)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, (Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('7', None)),)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
%%%%%%%%%%
'+'
Reply(Either(False, ((TokenKeyQuerySet5xqset(char_qset__isdecimal),), (Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('+', None)),))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(False, ((TokenKeyQuerySet5xqset(char_qset__isdecimal),), (Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('+', None)),))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, ((TokenKeyQuerySet5xqset(char_qset__isdecimal),), (Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('+', None)),))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
%%%%%%%%%%
''
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))


>>> main_rgnr = mkrs.token_seq_([])
>>> _333test_(main_rgnr, '7', '') #doctest: +ELLIPSIS
'7'
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
%%%%%%%%%%
''
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))




#######
>>> main_rgnr = mkrs.priority_parallel_([rgnr8digit, sym_plus])
>>> _333test_(main_rgnr, '7', '+', 'x', '') #doctest: +ELLIPSIS
'7'
Reply(Either(True, '7'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, '7'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('7', None))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
%%%%%%%%%%
'+'
Reply(Either(True, '+'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, '+'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('+', None))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
%%%%%%%%%%
'x'
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
%%%%%%%%%%
''
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))


#priority_parallel_rgnr#cascade
>>> main_rgnr = mkrs.priority_parallel_([mkrs.rgnr__not_eof, rgnr8digit])
>>> _3test_(main_rgnr, '7') #doctest: +ELLIPSIS
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))

>>> main_rgnr = mkrs.priority_parallel_([mkrs.rgnr__eof, rgnr8digit])
>>> _3test_(main_rgnr, '7') #doctest: +ELLIPSIS
Reply(Either(True, '7'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, '7'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('7', None))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))

#dead
>>> main_rgnr = mkrs.priority_parallel_([])
>>> _3test_(main_rgnr, '7') #doctest: +ELLIPSIS
Reply(Either(False, 'no_branches'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, 'no_branches'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, 'no_branches'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))


#######
>>> main_rgnr = mkrs.serial_([rgnr8digit, sym_plus])
>>> _333test_(main_rgnr, '7+', '7x', '7', 'x', '') #doctest: +ELLIPSIS
'7+'
Reply(Either(True, ('7', '+')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(True, ('7', '+')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
%%%%%%%%%%
'7x'
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
%%%%%%%%%%
'7'
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
%%%%%%%%%%
'x'
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
%%%%%%%%%%
''
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))


>>> main_rgnr = mkrs.serial_([rgnr8digit, sym_plus, False])
>>> _333test_(main_rgnr, '7x', 'x') #doctest: +ELLIPSIS
'7x'
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
%%%%%%%%%%
'x'
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))

>>> main_rgnr = mkrs.serial_([rgnr8digit, False, sym_plus])
>>> _333test_(main_rgnr, '7x', 'x') #doctest: +ELLIPSIS
'7x'
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
%%%%%%%%%%
'x'
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))

>>> main_rgnr = mkrs.serial_([True, rgnr8digit, sym_plus])
>>> _333test_(main_rgnr, '7x', 'x') #doctest: +ELLIPSIS
'7x'
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
%%%%%%%%%%
'x'
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))

>>> main_rgnr = mkrs.serial_([False, rgnr8digit, sym_plus])
>>> _333test_(main_rgnr, '7x', 'x') #doctest: +ELLIPSIS
'7x'
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
%%%%%%%%%%
'x'
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))






#######
>>> main_rgnr = mkrs.dependent_pair_(rgnr8digit, {'7':mkrs.none8oresult_if_ignore_(sym_plus), '6':mkrs.none8oresult_if_ignore_(mkrs.constant_loader_(mk_Right(666)))}, mkrs.constant_loader_(mk_Left(222)))
>>> _333test_(main_rgnr, '7+', '6', '5', '7x', '7', '') #doctest: +ELLIPSIS
'7+'
Reply(Either(True, ('7', '+')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(True, ('7', '+')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(True, ('7', None)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
%%%%%%%%%%
'6'
Reply(Either(True, ('6', 666)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, ('6', 666)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, ('6', None)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
%%%%%%%%%%
'5'
Reply(Either(False, 222), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(False, 222), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(False, 222), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
%%%%%%%%%%
'7x'
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
%%%%%%%%%%
'7'
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
%%%%%%%%%%
''
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))






#######
>>> main_rgnr = mkrs.switch_branches_(rgnr8digit, {'7':mkrs.none8oresult_if_ignore_(sym_plus), '6':mkrs.none8oresult_if_ignore_(mkrs.constant_loader_(mk_Right(666)))}, mkrs.constant_loader_(mk_Left(222)))
>>> _333test_(main_rgnr, '6', '5') #doctest: +ELLIPSIS
'6'
Reply(Either(True, 666), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, 666), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
%%%%%%%%%%
'5'
Reply(Either(False, 222), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(False, 222), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(False, 222), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))

#######
>>> main_rgnr = mkrs.switch_cased_(rgnr8digit, {'7':mkrs.none8oresult_if_ignore_(sym_plus), '6':mkrs.none8oresult_if_ignore_(mkrs.constant_loader_(mk_Right(666)))}, mkrs.constant_loader_(mk_Left(222)))
>>> _333test_(main_rgnr, '6', '5') #doctest: +ELLIPSIS
'6'
Reply(Either(True, Cased('6', 666)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, Cased('6', 666)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, Cased('6', None)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
%%%%%%%%%%
'5'
Reply(Either(False, 222), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(False, 222), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(False, 222), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))





#######
unbox_tuple_(unbox_idx, unlock_idx, begin_vs_middle, rgnrs)
>>> main_rgnr = mkrs.unbox_tuple_(1, 1, False, [rgnr8digit, mkrs.none8oresult_if_ignore_(sym_plus), mkrs.constant_loader_(mk_Right(666))])
>>> _3test_(main_rgnr, '7+') #doctest: +ELLIPSIS
Reply(Either(True, '+'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(True, '+'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))

>>> main_rgnr = mkrs.unbox_tuple_(1, 1, False, [rgnr8digit, sym_plus, mkrs.constant_loader_(mk_Right(666))])
>>> _333test_(main_rgnr, '7+', '7x', 'x', '7', '') #doctest: +ELLIPSIS
'7+'
Reply(Either(True, '+'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(True, '+'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(True, Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('+', None))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
%%%%%%%%%%
'7x'
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
%%%%%%%%%%
'x'
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
%%%%%%%%%%
'7'
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
%%%%%%%%%%
''
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))




#######
between_(rgnr8open, rgnr8close, rgnr8body)
>>> main_rgnr = mkrs.between_(sym6, sym9, mkrs.none8oresult_if_ignore_(sym_plus))
>>> _3test_(main_rgnr, '(+)') #doctest: +ELLIPSIS
Reply(Either(True, '+'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))
Reply(Either(True, '+'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))

>>> main_rgnr = mkrs.between_(sym6, sym9, sym_plus)
>>> _333test_(main_rgnr, '(+)', '(+', '(', '', 'x', '(x', '(+x))))') #doctest: +ELLIPSIS
'(+)'
Reply(Either(True, '+'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))
Reply(Either(True, '+'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))
Reply(Either(True, Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('+', None))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))
%%%%%%%%%%
'(+'
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
%%%%%%%%%%
'('
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
%%%%%%%%%%
''
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
%%%%%%%%%%
'x'
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('(')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('(')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('(')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
%%%%%%%%%%
'(x'
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
%%%%%%%%%%
'(+x))))'
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj(')')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(2), PositionInfo4Gap__idx(3)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj(')')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(2), PositionInfo4Gap__idx(3)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj(')')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(2), PositionInfo4Gap__idx(3)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))






#######
repetition_(rgnr, _min, may_max, unlock_idx, begin_vs_middle, ignore, unpack)

#######
#ignore:=True
>>> main_rgnr = mkrs.repetition_(sym_plus, 0, None, 0, False, ignore:=True, False)
>>> _333test_(main_rgnr, '++', '+', '', 'x', '+x', '+++x') #doctest: +ELLIPSIS
'++'
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
%%%%%%%%%%
'+'
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
%%%%%%%%%%
''
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
%%%%%%%%%%
'x'
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
%%%%%%%%%%
'+x'
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
%%%%%%%%%%
'+++x'
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))

#######
#ignore:=False
>>> main_rgnr = mkrs.repetition_(sym_plus, 0, None, 0, False, ignore:=False, False)
>>> _333test_(main_rgnr, '++', '+', '', 'x', '+x', '+++x') #doctest: +ELLIPSIS
'++'
Reply(Either(True, ('+', '+')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(True, ('+', '+')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
%%%%%%%%%%
'+'
Reply(Either(True, ('+',)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, ('+',)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
%%%%%%%%%%
''
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
%%%%%%%%%%
'x'
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
%%%%%%%%%%
'+x'
Reply(Either(True, ('+',)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, ('+',)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
%%%%%%%%%%
'+++x'
Reply(Either(True, ('+', '+', '+')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))
Reply(Either(True, ('+', '+', '+')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))


#######
>>> main_rgnr = mkrs.repetition_(sym_plus, 4, 6, 2, False, ignore:=False, False)

#######
>>> _333test_(main_rgnr, '+++', '++', '+', '+x', '++x', '+++x') #doctest: +ELLIPSIS
'+++'
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))
%%%%%%%%%%
'++'
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
%%%%%%%%%%
'+'
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
%%%%%%%%%%
'+x'
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
%%%%%%%%%%
'++x'
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(2), PositionInfo4Gap__idx(3)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(2), PositionInfo4Gap__idx(3)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(2), PositionInfo4Gap__idx(3)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))
%%%%%%%%%%
'+++x'
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(3), PositionInfo4Gap__idx(4)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 4), PositionInfo4Gap__idx(4)))
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(3), PositionInfo4Gap__idx(4)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 4), PositionInfo4Gap__idx(4)))
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(3), PositionInfo4Gap__idx(4)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 4), PositionInfo4Gap__idx(4)))


#######
>>> _111test_(main_rgnr, '++++++++', '+++', '++', '+', '', 'x', '+x', '++x', '+++x', '++++x', '+++++x', '++++++x', '+++++++x') #doctest: +ELLIPSIS
'++++++++'
Reply(Either(True, ('+', '+', '+', '+', '+', '+')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 6), PositionInfo4Gap__idx(6)))
----------
'+++'
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))
----------
'++'
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
----------
'+'
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
----------
''
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
----------
'x'
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
----------
'+x'
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
----------
'++x'
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(2), PositionInfo4Gap__idx(3)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))
----------
'+++x'
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(3), PositionInfo4Gap__idx(4)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 4), PositionInfo4Gap__idx(4)))
----------
'++++x'
Reply(Either(True, ('+', '+', '+', '+')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 4), PositionInfo4Gap__idx(4)))
----------
'+++++x'
Reply(Either(True, ('+', '+', '+', '+', '+')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 5), PositionInfo4Gap__idx(5)))
----------
'++++++x'
Reply(Either(True, ('+', '+', '+', '+', '+', '+')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 6), PositionInfo4Gap__idx(6)))
----------
'+++++++x'
Reply(Either(True, ('+', '+', '+', '+', '+', '+')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 6), PositionInfo4Gap__idx(6)))





#######
many_(rgnr, _min=0, may_max=None, ignore=False, unpack=False)
    vs:repetition_(rgnr, _min, may_max, unlock_idx, begin_vs_middle, ignore, unpack)

#######
#ignore:=True
>>> main_rgnr = mkrs.many_(sym_plus, 0, None, ignore:=True)
>>> _333test_(main_rgnr, '++', '+', '', 'x', '+x', '+++x') #doctest: +ELLIPSIS
'++'
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
%%%%%%%%%%
'+'
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
%%%%%%%%%%
''
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
%%%%%%%%%%
'x'
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
%%%%%%%%%%
'+x'
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
%%%%%%%%%%
'+++x'
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))

#######
#ignore:=False
>>> main_rgnr = mkrs.many_(sym_plus, 0, None, ignore:=False)
>>> _333test_(main_rgnr, '++', '+', '', 'x', '+x', '+++x') #doctest: +ELLIPSIS
'++'
Reply(Either(True, ('+', '+')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(True, ('+', '+')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
%%%%%%%%%%
'+'
Reply(Either(True, ('+',)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, ('+',)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
%%%%%%%%%%
''
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
%%%%%%%%%%
'x'
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
%%%%%%%%%%
'+x'
Reply(Either(True, ('+',)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, ('+',)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
%%%%%%%%%%
'+++x'
Reply(Either(True, ('+', '+', '+')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))
Reply(Either(True, ('+', '+', '+')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))


#######
>>> main_rgnr = mkrs.many_(sym_plus, 4, 6, ignore:=False)

#######
>>> _333test_(main_rgnr, '+++', '+', '', 'x', '+x', '++x') #doctest: +ELLIPSIS
'+++'
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))
%%%%%%%%%%
'+'
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
%%%%%%%%%%
''
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
%%%%%%%%%%
'x'
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
%%%%%%%%%%
'+x'
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
%%%%%%%%%%
'++x'
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(2), PositionInfo4Gap__idx(3)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(2), PositionInfo4Gap__idx(3)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(2), PositionInfo4Gap__idx(3)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))



#######
>>> _111test_(main_rgnr, '++++++++', '+++', '++', '+', '', 'x', '+x', '++x', '+++x', '++++x', '+++++x', '++++++x', '+++++++x') #doctest: +ELLIPSIS
'++++++++'
Reply(Either(True, ('+', '+', '+', '+', '+', '+')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 6), PositionInfo4Gap__idx(6)))
----------
'+++'
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))
----------
'++'
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
----------
'+'
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
----------
''
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
----------
'x'
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
----------
'+x'
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
----------
'++x'
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(2), PositionInfo4Gap__idx(3)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))
----------
'+++x'
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(3), PositionInfo4Gap__idx(4)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 4), PositionInfo4Gap__idx(4)))
----------
'++++x'
Reply(Either(True, ('+', '+', '+', '+')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 4), PositionInfo4Gap__idx(4)))
----------
'+++++x'
Reply(Either(True, ('+', '+', '+', '+', '+')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 5), PositionInfo4Gap__idx(5)))
----------
'++++++x'
Reply(Either(True, ('+', '+', '+', '+', '+', '+')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 6), PositionInfo4Gap__idx(6)))
----------
'+++++++x'
Reply(Either(True, ('+', '+', '+', '+', '+', '+')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 6), PositionInfo4Gap__idx(6)))


#######
end_by_(rgnr8end, rgnr8body, _min=0, may_max=None, ignore4end=True, unpack4end=False, ignore4body=False, unpack4body=False)

>>> main_rgnr = mkrs.end_by_(sym_dot, rgnr8digit, 2, 3)
>>> _333test_(main_rgnr, 'x', '7x') #doctest: +ELLIPSIS
'x'
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
%%%%%%%%%%
'7x'
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))

#######
>>> _111test_(main_rgnr, 'x', '7x', '', '7.', '77.', '777.', '7777.') #doctest: +ELLIPSIS
'x'
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
----------
'7x'
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
----------
''
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
----------
'7.'
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('.', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
----------
'77.'
Reply(Either(True, ('7', '7')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))
----------
'777.'
Reply(Either(True, ('7', '7', '7')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 4), PositionInfo4Gap__idx(4)))
----------
'7777.'
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('.')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(3), PositionInfo4Gap__idx(4)), Cased('7', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 4), PositionInfo4Gap__idx(4)))




#######
sep_end_by_(rgnr8sep, rgnr8end, rgnr8body, _min=0, may_max=None, ignore4sep=True, unpack4sep=False, ignore4end=True, unpack4end=False, ignore4body=False, unpack4body=False)

#######
>>> main_rgnr = mkrs.sep_end_by_(sym_plus, sym_dot, rgnr8digit, 1, 3)
>>> _333test_(main_rgnr, 'x', '7x') #doctest: +ELLIPSIS
'x'
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
%%%%%%%%%%
'7x'
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))

#######
>>> main_rgnr = mkrs.sep_end_by_(sym_plus, sym_dot, rgnr8digit, 0)
>>> _111test_(main_rgnr, '', '.', '7.', '7+7.') #doctest: +ELLIPSIS
''
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
----------
'.'
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
----------
'7.'
Reply(Either(True, ('7',)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
----------
'7+7.'
Reply(Either(True, ('7', '7')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 4), PositionInfo4Gap__idx(4)))


#######
>>> main_rgnr = mkrs.sep_end_by_(sym_plus, sym_dot, rgnr8digit, 2)
>>> _111test_(main_rgnr, '', '.', '7.', '7+7.', '7+7+7.') #doctest: +ELLIPSIS
''
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
----------
'.'
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('.', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
----------
'7.'
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('.', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
----------
'7+7.'
Reply(Either(True, ('7', '7')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 4), PositionInfo4Gap__idx(4)))
----------
'7+7+7.'
Reply(Either(True, ('7', '7', '7')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 6), PositionInfo4Gap__idx(6)))



#######
>>> main_rgnr = mkrs.sep_end_by_(sym_plus, sym_dot, rgnr8digit, 1, 3)
>>> _111test_(main_rgnr, 'x', '7x', '', '.', '7.', '7+7.', '7+7+7.', '7+7+7+7.') #doctest: +ELLIPSIS
'x'
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
----------
'7x'
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
----------
''
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
----------
'.'
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('.', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
----------
'7.'
Reply(Either(True, ('7',)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
----------
'7+7.'
Reply(Either(True, ('7', '7')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 4), PositionInfo4Gap__idx(4)))
----------
'7+7+7.'
Reply(Either(True, ('7', '7', '7')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 6), PositionInfo4Gap__idx(6)))
----------
'7+7+7+7.'
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('.')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(5), PositionInfo4Gap__idx(6)), Cased('+', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 6), PositionInfo4Gap__idx(6)))





#######
sep_by_(rgnr8sep, rgnr8body, _min=0, may_max=None, ignore4sep=True, unpack4sep=False, ignore4body=False, unpack4body=False)
#######
>>> main_rgnr = mkrs.sep_by_(sym_plus, rgnr8digit, 1, 3)
>>> _333test_(main_rgnr, 'x', '7x') #doctest: +ELLIPSIS
'x'
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
%%%%%%%%%%
'7x'
Reply(Either(True, ('7',)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, ('7',)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))

#######
>>> main_rgnr = mkrs.sep_by_(sym_plus, rgnr8digit, 0)
>>> _111test_(main_rgnr, '', 'x', '7x', '7+7') #doctest: +ELLIPSIS
''
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
----------
'x'
Reply(Either(True, ()), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
----------
'7x'
Reply(Either(True, ('7',)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
----------
'7+7'
Reply(Either(True, ('7', '7')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))


#######
>>> main_rgnr = mkrs.sep_by_(sym_plus, rgnr8digit, 2)
>>> _111test_(main_rgnr, '', 'x', '7x', '7+7x', '7+7+7') #doctest: +ELLIPSIS
''
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
----------
'x'
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
----------
'7x'
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('+')), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(1), PositionInfo4Gap__idx(2)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
----------
'7+7x'
Reply(Either(True, ('7', '7')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))
----------
'7+7+7'
Reply(Either(True, ('7', '7', '7')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 5), PositionInfo4Gap__idx(5)))


#######
>>> main_rgnr = mkrs.sep_by_(sym_plus, rgnr8digit, 1, 3)
>>> _111test_(main_rgnr, 'x', '7x', '', '7', '7+7', '7+7+7', '7+7+7+7') #doctest: +ELLIPSIS
'x'
Reply(Either(False, (TokenKeyQuerySet5xqset(char_qset__isdecimal), Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
----------
'7x'
Reply(Either(True, ('7',)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
----------
''
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
----------
'7'
Reply(Either(True, ('7',)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
----------
'7+7'
Reply(Either(True, ('7', '7')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))
----------
'7+7+7'
Reply(Either(True, ('7', '7', '7')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 5), PositionInfo4Gap__idx(5)))
----------
'7+7+7+7'
Reply(Either(True, ('7', '7', '7')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 5), PositionInfo4Gap__idx(5)))




#######
nongreedy:
    end_by_
    sep_end_by_
#######
#nongreedy:end_by_
>>> main_rgnr = mkrs.end_by_(mkrs.constant_loader_(mk_Right(999)), rgnr8digit, 2)
>>> _111test_(main_rgnr, '', '7', '77', '777') #doctest: +ELLIPSIS
''
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
----------
'7'
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
----------
'77'
Reply(Either(True, ('7', '7')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
----------
'777'
Reply(Either(True, ('7', '7')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))


#######
#nongreedy:sep_end_by_
>>> main_rgnr = mkrs.sep_end_by_(sym_plus, mkrs.constant_loader_(mk_Right(999)), rgnr8digit, 2)
>>> _111test_(main_rgnr, '', '7', '7+7', '7+7+7') #doctest: +ELLIPSIS
''
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
----------
'7'
Reply(Either(False, 'eof'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
----------
'7+7'
Reply(Either(True, ('7', '7')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))
----------
'7+7+7'
Reply(Either(True, ('7', '7')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))




#######
>>> tkn_rgnr8digit = mkrs.token_(tkn_qset5xqset_(char_qset__isdecimal))
>>> tkn_sym_plus = mkrs.token_(tkn_qset5xqset_(Tester__eq_obj('+')))
>>> tkn_rgnr8tpl__d_p = mkrs.serial_([tkn_rgnr8digit, False, tkn_sym_plus])

>>> tkd_rgnr8digit = mkrs.spost__tkn2tkd_(tkn_rgnr8digit)
>>> tkd_sym_plus = mkrs.spost__tkn2tkd_(tkn_sym_plus)
>>> tkd_rgnr8tpl__d_p = mkrs.serial_([tkd_rgnr8digit, False, tkd_sym_plus])

#######
>>> main_rgnr = mkrs.spost__tkn2tkd_(tkn_rgnr8digit)
>>> _3test_(main_rgnr, '7') #doctest: +ELLIPSIS
Reply(Either(True, Cased('7', None)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, Cased('7', None)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('7', None))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))

#######
>>> main_rgnr = mkrs.spost__tkn2tkey_(tkn_rgnr8digit)
>>> _3test_(main_rgnr, '7') #doctest: +ELLIPSIS
Reply(Either(True, '7'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, '7'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('7', None))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))

#######
>>> main_rgnr = mkrs.spost__tkn2tdat_(tkn_rgnr8digit)
>>> _3test_(main_rgnr, '7') #doctest: +ELLIPSIS
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('7', None))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))

#######
>>> main_rgnr = mkrs.spost__tkd2tkey_(tkd_rgnr8digit)
>>> _3test_(main_rgnr, '7') #doctest: +ELLIPSIS
Reply(Either(True, '7'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, '7'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('7', None))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))

#######
>>> main_rgnr = mkrs.spost__tkd2tdat_(tkd_rgnr8digit)
>>> _3test_(main_rgnr, '7') #doctest: +ELLIPSIS
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('7', None))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))

#######
>>> main_rgnr = mkrs.spost__unbox_(mkrs.serial_([rgnr8digit]))
>>> _3test_(main_rgnr, '7') #doctest: +ELLIPSIS
Reply(Either(True, '7'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, '7'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))


#######
>>> main_rgnr = mkrs.spost__fmap4tuple__tkn2tkd_(tkn_rgnr8tpl__d_p)
>>> _3test_(main_rgnr, '7+') #doctest: +ELLIPSIS
Reply(Either(True, (Cased('7', None), Cased('+', None))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(True, (Cased('7', None), Cased('+', None))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))

#######
>>> main_rgnr = mkrs.spost__fmap4tuple__tkn2tkey_(tkn_rgnr8tpl__d_p)
>>> _3test_(main_rgnr, '7+') #doctest: +ELLIPSIS
Reply(Either(True, ('7', '+')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(True, ('7', '+')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))

#######
>>> main_rgnr = mkrs.spost__fmap4tuple__tkn2tdat_(tkn_rgnr8tpl__d_p)
>>> _3test_(main_rgnr, '7+') #doctest: +ELLIPSIS
Reply(Either(True, (None, None)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(True, (None, None)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))


#######
>>> main_rgnr = mkrs.spost__fmap4tuple__tkd2tkey_(tkd_rgnr8tpl__d_p)
>>> _3test_(main_rgnr, '7+') #doctest: +ELLIPSIS
Reply(Either(True, ('7', '+')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(True, ('7', '+')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))

#######
>>> main_rgnr = mkrs.spost__fmap4tuple__tkd2tdat_(tkd_rgnr8tpl__d_p)
>>> _3test_(main_rgnr, '7+') #doctest: +ELLIPSIS
Reply(Either(True, (None, None)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(True, (None, None)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))



#######
>>> (grp4nm4rgnr, grp4rgnr_ref) = mk_group_pair4rgnr_ref()
>>> ref__xxx_rgnr = grp4rgnr_ref.xxx_rgnr
>>> ref__xxx_rgnr is grp4rgnr_ref.xxx_rgnr # cached
True
>>> nm4xxx_rgnr = grp4nm4rgnr.xxx_rgnr
>>> nm4xxx_rgnr is ref__xxx_rgnr.name6ref # inter-connected
True
>>> repr(nm4xxx_rgnr) == repr(Symbol4IRecognizerLLoo('xxx_rgnr'))
True
>>> repr(ref__xxx_rgnr) == repr(mkrs.ref_(nm4xxx_rgnr))
True

>>> nmd_xxx_rgnr = ref__xxx_rgnr.mk_named_rgnr_(_unamed__xxx_rgnr:=mkrs.rgnr__any_token)
>>> repr(nmd_xxx_rgnr) == repr(mkrs.named_(nm4xxx_rgnr, _unamed__xxx_rgnr))
True

>>> del ref__xxx_rgnr, nmd_xxx_rgnr,_unamed__xxx_rgnr # not to affect below collect_namess5locals_()





#######
#begin-ref_,named_
#######

###
>>> (grp4nm4rgnr, grp4rgnr_ref) = mk_group_pair4rgnr_ref()
>>> ref__rgnr8digit = grp4rgnr_ref.rgnr8digit # mkrs.ref_()
>>> nmd__rgnr8digit = ref__rgnr8digit.mk_named_rgnr_(rgnr8digit) # mkrs.named_()
>>> ref__rgnr8digit
RecognizerLLoo__ref(nm4rgnr_.rgnr8digit)
>>> nmd__rgnr8digit
RecognizerLLoo__named(nm4rgnr_.rgnr8digit, RecognizerLLoo__spost__tkn2tkey(RecognizerLLoo__token(TokenKeyQuerySet5xqset(char_qset__isdecimal))))

###
>>> (name2rgnr, nms4ref, nms6ref) = collect_namess5locals_(locals(), _no_check__vs__ge__vs__eq_=2)
>>> nms4ref
frozenset({nm4rgnr_.rgnr8digit})
>>> nms6ref
frozenset({nm4rgnr_.rgnr8digit})
>>> name2rgnr == {grp4nm4rgnr.rgnr8digit:nmd__rgnr8digit}
True

###
#restore_env:goto
>>> saved_env = env
>>> env = mk_Environment(param2setting:={}, name2rgnr, name2may_gpreprocess:={}, name2may_gpostprocess6err:={}, name2may_gpostprocess6ok:={}, name2force_postprocess_when_ignore:={})

###
>>> main_rgnr = ref__rgnr8digit
>>> _1test_(main_rgnr, '7') #doctest: +ELLIPSIS
Reply(Either(True, '7'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))

###
#restore_env:here
>>> env = saved_env
>>> del ref__rgnr8digit, nmd__rgnr8digit, main_rgnr # not to affect below collect_namess5locals_()

#######
#end-ref_,named_
#######



#######
>>> main_rgnr = mkrs.tkey_prefix_tree_(tuple((w,w) for w in 'xyz 34 345w ++'.split()))
>>> _3test_(main_rgnr, 'xyz') #doctest: +ELLIPSIS
Reply(Either(True, 'xyz'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))
Reply(Either(True, 'xyz'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))
Reply(Either(True, 'xyz'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))
>>> _1test_(main_rgnr, '345w') #doctest: +ELLIPSIS
Reply(Either(True, '345w'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 4), PositionInfo4Gap__idx(4)))
>>> _1test_(main_rgnr, '++w') #doctest: +ELLIPSIS
Reply(Either(True, '++'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> _3test_(main_rgnr, 'xyw') #doctest: +ELLIPSIS
Reply(Either(False, 'no_prefix_matched'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, 'no_prefix_matched'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
Reply(Either(False, 'no_prefix_matched'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> _1test_(main_rgnr, '345') #doctest: +ELLIPSIS
Reply(Either(True, '34'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> _1test_(main_rgnr, '34w') #doctest: +ELLIPSIS
Reply(Either(True, '34'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
>>> _1test_(main_rgnr, '3w') #doctest: +ELLIPSIS
Reply(Either(False, 'no_prefix_matched'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))
>>> _1test_(main_rgnr, '+w') #doctest: +ELLIPSIS
Reply(Either(False, 'no_prefix_matched'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))






#######
>>> main_rgnr = mkrs.subscript_(rgnr8digit, slice(None))
>>> _3test_(main_rgnr, '5') #doctest: +ELLIPSIS
Reply(Either(True, '5'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, '5'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))
Reply(Either(True, Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('5', None))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))

>>> main_rgnr = mkrs.subscript_(rgnr8digit, slice(0,0))
>>> _1test_(main_rgnr, '5') #doctest: +ELLIPSIS
Reply(Either(True, ''), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))

>>> main_rgnr = mkrs.subscript_(rgnr8digit, 0)
>>> _1test_(main_rgnr, '5') #doctest: +ELLIPSIS
Reply(Either(True, '5'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))




#######
>>> main_rgnr = mkrs.spost__fmap4tuple_(rgnr8pair, lambda c:c+'ww')
>>> _3test_(main_rgnr, '69') #doctest: +ELLIPSIS
Reply(Either(True, ('6ww', '9ww')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(True, ('6ww', '9ww')), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))
Reply(Either(True, None), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 2), PositionInfo4Gap__idx(2)))







#######
>>> def mk_lazy_raise_with_nlast_args_(n, E, v, /):
...     def lazy_raise(*args):
...         raise E(v, *args[max(0,len(args)-n):])
...     return lazy_raise
>>> def mk_lazy_tmay_value_with_nlast_args_(n, v, /):
...     def lazy_tmay_value(*args):
...         return ((v, *args[max(0,len(args)-n):]),)
...     return lazy_tmay_value
>>> def mk_lazy_value_(v, /):
...     def lazy_value(*args):
...         return v
...     return lazy_value
>>> def mk_lazy_value_with_nlast_args_(n, v, /):
...     def lazy_value(*args):
...         return (v, *args[max(0,len(args)-n):])
...     return lazy_value
>>> recognize_ = _0recognize #begin-test:main_()/main__split_teardown_()

#######
>>> main_rgnr = mkrs.main_(rgnr8digit, mk_lazy_tmay_value_with_nlast_args_(0x02, 999))
>>> _1test_(main_rgnr, '6') #doctest: +ELLIPSIS
Reply(Either(True, '6'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))

>>> main_rgnr = mkrs.main_(rgnr8digit, mk_lazy_tmay_value_with_nlast_args_(0x02, 999), mk_lazy_value_(()))
>>> _1test_(main_rgnr, '6') #doctest: +ELLIPSIS
Reply(Either(True, '6'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))

>>> main_rgnr = mkrs.main_(rgnr8digit, mk_lazy_value_(999), mk_lazy_tmay_value_with_nlast_args_(0x02, 666))
>>> _1test_(main_rgnr, '6', not_Reply=True) #doctest: +ELLIPSIS
(666, 999, Either(True, Reply(Either(True, '6'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))))

>>> main_rgnr = mkrs.main_(rgnr8digit, None, mk_lazy_tmay_value_with_nlast_args_(0x02, 666))
>>> _1test_(main_rgnr, '6', not_Reply=True) #doctest: +ELLIPSIS
(666, None, Either(True, Reply(Either(True, '6'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))))

>>> main_rgnr = mkrs.main_(rgnr8digit, mk_lazy_raise_with_nlast_args_(0x02, Exception, 999), mk_lazy_tmay_value_with_nlast_args_(0x02, 666))
>>> _1test_(main_rgnr, '6', not_Reply=True) #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
Exception: (999, [<WeakKeyHalfMap8AnonymousWeakableSymbol:'sym8id4curr_rgnz'@0x...>], False)


######
# main_:++rgnr internal exc whether catch by _may_teardown_
>>> rgnr8raise = mkrs.spostprocess_(rgnr8digit, None, mk_lazy_raise_with_nlast_args_(0x01, Exception, 777))

######
>>> main_rgnr = mkrs.main_(rgnr8raise, mk_lazy_tmay_value_with_nlast_args_(0x02, 999), mk_lazy_value_(()))
>>> _1test_(main_rgnr, '6') #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
Exception: (777, '6')

######
>>> main_rgnr = mkrs.main_(rgnr8raise, mk_lazy_tmay_value_with_nlast_args_(0x02, 999), None)
>>> _1test_(main_rgnr, '6') #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
Exception: (777, '6')

######
>>> main_rgnr = mkrs.main_(rgnr8raise, mk_lazy_tmay_value_with_nlast_args_(0x02, 999), mk_lazy_raise_with_nlast_args_(0x02, Exception, 666))
>>> _1test_(main_rgnr, '6') #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
Exception: (666, ((999, [<WeakKeyHalfMap8AnonymousWeakableSymbol:'sym8id4curr_rgnz'@0x...>], False),), Either(False, (<class 'Exception'>, Exception(777, '6'), <traceback object at 0x...>)))

######
>>> main_rgnr = mkrs.main_(rgnr8raise, mk_lazy_tmay_value_with_nlast_args_(0x02, 999), mk_lazy_tmay_value_with_nlast_args_(0x02, 666))
>>> _1test_(main_rgnr, '6', not_Reply=True) #doctest: +ELLIPSIS
(666, ((999, [<WeakKeyHalfMap8AnonymousWeakableSymbol:'sym8id4curr_rgnz'@0x...>], False),), Either(False, (<class 'Exception'>, Exception(777, '6'), <traceback object at 0x...>)))




#######
#######
#######
>>> main_rgnr = mkrs.main__split_teardown_(rgnr8digit, mk_lazy_value_with_nlast_args_(0x02, 999))
>>> _1test_(main_rgnr, '6') #doctest: +ELLIPSIS
Reply(Either(True, '6'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))

>>> main_rgnr = mkrs.main__split_teardown_(rgnr8digit, mk_lazy_value_with_nlast_args_(0x02, 999), None, mk_lazy_value_(None))
>>> _1test_(main_rgnr, '6') #doctest: +ELLIPSIS
Reply(Either(True, '6'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))

>>> main_rgnr = mkrs.main__split_teardown_(rgnr8digit, mk_lazy_value_(999), mk_lazy_value_with_nlast_args_(0x02, 666))
>>> _1test_(main_rgnr, '6', not_Reply=True) #doctest: +ELLIPSIS
(666, 999, Reply(Either(True, '6'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1))))

>>> main_rgnr = mkrs.main__split_teardown_(rgnr8digit, None, mk_lazy_value_with_nlast_args_(0x02, 666))
>>> _1test_(main_rgnr, '6', not_Reply=True) #doctest: +ELLIPSIS
(666, None, Reply(Either(True, '6'), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1))))

>>> main_rgnr = mkrs.main__split_teardown_(rgnr8digit, mk_lazy_raise_with_nlast_args_(0x02, Exception, 999), mk_lazy_value_with_nlast_args_(0x02, 666))
>>> _1test_(main_rgnr, '6', not_Reply=True) #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
Exception: (999, [<WeakKeyHalfMap8AnonymousWeakableSymbol:'sym8id4curr_rgnz'@0x...>], False)


######
# main__split_teardown_:++rgnr internal exc whether catch by _may_teardown_
>>> rgnr8raise = mkrs.spostprocess_(rgnr8digit, None, mk_lazy_raise_with_nlast_args_(0x01, Exception, 777))

######
>>> main_rgnr = mkrs.main__split_teardown_(rgnr8raise, mk_lazy_value_with_nlast_args_(0x02, 999), None, mk_lazy_value_(None))
>>> _1test_(main_rgnr, '6') #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
Exception: (777, '6')

######
>>> main_rgnr = mkrs.main__split_teardown_(rgnr8raise, mk_lazy_value_with_nlast_args_(0x02, 999), None)
>>> _1test_(main_rgnr, '6') #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
Exception: (777, '6')

######
>>> main_rgnr = mkrs.main__split_teardown_(rgnr8raise, mk_lazy_value_with_nlast_args_(0x02, 999), None, mk_lazy_raise_with_nlast_args_(0x02, Exception, 666))
>>> _1test_(main_rgnr, '6') #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
Exception: (666, False, (999, [<WeakKeyHalfMap8AnonymousWeakableSymbol:'sym8id4curr_rgnz'@0x...>], False))

######
>>> main_rgnr = mkrs.main__split_teardown_(rgnr8raise, mk_lazy_value_with_nlast_args_(0x02, 999), mk_lazy_raise_with_nlast_args_(0x02, Exception, 666))
>>> _1test_(main_rgnr, '6') #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
Exception: (777, '6')

######
>>> main_rgnr = mkrs.main__split_teardown_(rgnr8raise, mk_lazy_value_with_nlast_args_(0x02, 999), mk_lazy_value_with_nlast_args_(0x02, 666))
>>> _1test_(main_rgnr, '6', not_Reply=True) #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
Exception: (777, '6')




>>> recognize_ = recognize__asif_main_rgnr_ #end-test:main__split_teardown_()/main__split_teardown_()








#######
lazy_alias_
#######
>>> main_rgnr = mkrs.lazy_alias_('any_token_', [])
>>> _1test_(main_rgnr, '6') #doctest: +ELLIPSIS
Reply(Either(True, Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('6', None))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))

#######
>>> main_rgnr = mkrs.lazy_alias_(mkrs.any_token_, [])
>>> _1test_(main_rgnr, '6') #doctest: +ELLIPSIS
Reply(Either(True, Token__keyed(PositionInfo4Span(PositionInfo4Gap__idx(0), PositionInfo4Gap__idx(1)), Cased('6', None))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 1), PositionInfo4Gap__idx(1)))

#######
>>> main_rgnr = mkrs.lazy_alias_(mkrs.constant_loader_, [mk_Right(mk_Right(999))])
>>> _1test_(main_rgnr, '6') #doctest: +ELLIPSIS
Reply(Either(True, 999), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))

#######
>>> saved__env = env
>>> env = mk_Environment(param2setting:={666:mk_Right(999)}, name2rgnr:={}, name2may_gpreprocess:={}, name2may_gpostprocess6err:={}, name2may_gpostprocess6ok:={}, name2force_postprocess_when_ignore:={})
>>> main_rgnr = mkrs.lazy_alias_(mkrs.constant_loader_, [mk_Left(666)])
>>> _1test_(main_rgnr, '6') #doctest: +ELLIPSIS
Reply(Either(True, 999), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))


#>>> env = saved__env
#######
lazy_alias_rgnr__human_
>>> def constant_loader__Right_(oresult, /):
...     return mkrs.constant_loader_(mk_Right(oresult))

#######
>>> main_rgnr = mkrs.lazy_alias_rgnr__human_(mkrs.constant_loader_, mk_Left(666))
>>> _1test_(main_rgnr, '6') #doctest: +ELLIPSIS
Reply(Either(True, 999), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))

#######
>>> main_rgnr = mkrs.lazy_alias_rgnr__human_('constant_loader_', mk_Left(666))
>>> _1test_(main_rgnr, '6') #doctest: +ELLIPSIS
Reply(Either(True, 999), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))

#######
>>> main_rgnr = mkrs.lazy_alias_rgnr__human_('constant_loader_', mk_Right(mk_Right(999)))
>>> _1test_(main_rgnr, '6') #doctest: +ELLIPSIS
Reply(Either(True, 999), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))

#######
>>> main_rgnr = mkrs.lazy_alias_rgnr__human_(constant_loader__Right_, mk_Right(999))
>>> _1test_(main_rgnr, '6') #doctest: +ELLIPSIS
Reply(Either(True, 999), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))

#######
>>> main_rgnr = mkrs.lazy_alias_rgnr__human_(constant_loader__Right_, 999)
>>> _1test_(main_rgnr, '6') #doctest: +ELLIPSIS
Reply(Either(True, 999), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))

#######
>>> main_rgnr = mkrs.lazy_alias_rgnr__human_(constant_loader__Right_, mk_Left(666))
>>> _1test_(main_rgnr, '6') #doctest: +ELLIPSIS
Reply(Either(True, Either(True, 999)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 0), PositionInfo4Gap__idx(0)))


>>> env = saved__env





#######
#######
#######
#>>> mkrs.???()
TODO:see above: here list some:
:non_tested-yet:
    try_except_else_:++strict_vs_forgivable:non_tested
    try_except_else__spost_:++strict_vs_forgivable:non_tested
    mkrs.gsep_end_by_(...) #_validate()


#NOTE:ignore,protect_header_
#NOTE:_force_postprocess_when_ignore_
#NOTE:strict_vs_forgivable

:%s/\([@ ]0x\)\w\+/\1.../g
:%s/+ELLIPSIS  *[R]eply/+ELLIPSIS\rReply/g
:%s/  *# Line /\r# Line /g
:%s/  *$//g
:%s/  *###buggy expected/\r###buggy expected/g
view /sdcard/0my_files/tmp/0tmp












end_doctest:here
]]
<<<placeholder4example_snippet-from-seed.recognize.recognizer_LLoo__ver2_.IRecognizerLLoo.__doc__>>>


#]]]'''
__all__ = r'''
'''.split()#'''
__all__
# :.,.+1724s/^ *[^ >].*/
# :.,.+1724s/^ *>>> /
# :.,.+9s/@\[\d*] */\r/g
___begin_mark_of_excluded_global_names__0___ = ...

from seed.types.stream.IRecoverableInputStream import PlainRecoverableInputStream5token_seq, RecoverableInputStream9LazyList
from seed.types.IToken import mk_token_rawstream__5xs__idx_
from seed.types.IToken import char_qset__isdecimal, TokenKeyQuerySet5xqset
from seed.types.Tester import Tester__eq_obj
from seed.types.Either import mk_Left, mk_Right

from seed.recognize.recognizer_LLoo__ver2_.IRecognizerLLoo import \
(mk_Environment
,mk_group_pair4rgnr_ref
,   Symbol4IRecognizerLLoo
,collect_namess5locals_
,   collect_namess5rgnrs_
#
,Makers4IRecognizerLLoo
,light_wrap_rgnr_
,RecognizerLLoo__light_wrap
,mk_gpreprocess__5constant_
,mk_gpostprocess6ok__5spost_after_tag_st_
,mk_gpostprocess6err__5spost_after_tag_st_
#
,recognize_
,   recognize__asif_main_rgnr_
,forbid_xxx_protected_ok
,get_info_ex4high_freq_sconfigpack_
)



___end_mark_of_excluded_global_names__0___ = ...


def _extract_example_snippet():
    from seed.recognize.recognizer_LLoo__ver2_.IRecognizerLLoo import __doc__ as _doc
    from seed.str_tools.cut_text_by_marker_seq import strip_text_by_marker_pair
    example_snippet = strip_text_by_marker_pair(_doc, '\nbegin_doctest:here\n', '\nend_doctest:here\n')
    return example_snippet

_plc_hldr = '<<<placeholder4example_snippet-from-seed.recognize.recognizer_LLoo__ver2_.IRecognizerLLoo.__doc__>>>'
__doc__ = __doc__.replace(_plc_hldr, fr'''








######################
######################
######################
[[
######################
# extracted from seed.recognize.recognizer_LLoo__ver2_.IRecognizerLLoo.__doc__
######################

{_extract_example_snippet()!s}
]]
######################
######################
######################







'''#'''
)

def _validate():
    from seed.recognize.recognizer_LLoo__ver2_.IRecognizerLLoo import Makers4IRecognizerLLoo
    all_method_names = tuple(sorted(Makers4IRecognizerLLoo))
    miss_nms = [nm for nm in all_method_names if not (f'mkrs.{nm}(' if nm[-1] == '_' else f'>>> main_rgnr = mkrs.{nm}\n') in __doc__] #)
    if miss_nms:
        from seed.tiny import print_err
        print_err('\n'.join(miss_nms))
        raise Exception(miss_nms)
    return
_validate()


__all__
from seed.recognize.recognizer_LLoo__ver2_.doctest4IRecognizerLLoo import *
