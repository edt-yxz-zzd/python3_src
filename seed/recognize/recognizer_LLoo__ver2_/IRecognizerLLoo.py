#__all__:goto
r'''[[[
######################
######################
######################
#TODO:goto
# [:def__IRecognizerLLoo]:goto
# [:def__IEnvironment]:goto
#begin_doctest:goto
#end_doctest:goto
#
#postcondition ==>> [forbid_xxx_protected_ok===True]
#   constant!
#
#ignore affect spostprocess,gpostprocess
#   ++_force_postprocess_when_ignore_
#       @IRecognizerLLoo__gprepostprocess
#       @IRecognizerLLoo__spostprocess
#       @RecognizerLLoo__try_except_else
#       @RecognizerLLoo__try_except_else__spost
#   ??always force:
#       @RecognizerLLoo__light_wrap
#       @IRecognizerLLoo__tag
#       @IRecognizerLLoo__constant_loader
#
#[forkable is bad idea][there should be only one input_stream and many snapshot]
#   <<== old discarded istream will still remain in parent func stack frame therefore never be destroyed and release memory...
#
# to protect istream monotonic_idx, now ISnapshot is no more subclass of IUnlocker
#
#now cancel auto release:unlocker_release() <<== [@fail:not reply.ok: (unlocker>>snapshot) should not unlocker_release()!]
#
#
#TODO: serial-final-flattener:Rope+tuple(leaf-node)
#   view ../../python3_src/seed/types/Rope.py
#TODO:pseudo_func_body_stmt_flow,_is_ctx_scope_=True
#   2 primitive flow control ways:
#       goto
#       switch_case: mapping+goto
#           result store at var
#           rgnr_ok --> oresult
#           eresult --> oresult:lift
#   #       if_bool: bool_expr+goto
#   #           match_case: serial_eq+goto
#   #           while_bool_loop: serial_eq+goto
#   #       try_except_else:rgnr_ok+goto
#   #           if_ok: rgnr_ok+goto
#   #           while_ok_loop: rgnr_ok+goto
#
# [:lookahead__vs__try__vs__optional__vs__lift]:goto
# [:protected_fail__vs__forgivable_fail__vs__severe_fail]:goto
######################
######################
######################
e ../../python3_src/seed/recognize/recognizer_LLoo__ver2_/IRecognizerLLoo.py
view ../../python3_src/seed/types/mapping/DynamicStackedMapping.py
view ../../python3_src/seed/types/stream/IRecoverableInputStream.py
    view ../../python3_src/seed/types/IToken.py
    view ../../python3_src/seed/types/LazyList.py
view ../../python3_src/seed/recognize/recognizer_LLoo__ver2_/doctest4IRecognizerLLoo.py



seed.recognize.recognizer_LLoo__ver2_.IRecognizerLLoo
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_LLoo__ver2_.IRecognizerLLoo -x
py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LLoo__ver2_.IRecognizerLLoo:__doc__ -ht

py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LLoo__ver2_.doctest4IRecognizerLLoo:__doc__ -ht -ff


static-->persistent
[[[
===

[[
DONE:
    DONE:pre/post turnon... @recognize_()
    DONE:osymbols --> osymbolXseq
    cancel:
        nm4pre --> nm_seq4pre
        nm4post --> nm_seq4post
TODO:
IEnvironment
    .external_cache
        #to save rgnr persistent info(full_view_info<env,rgnr.descendants>)
        eg:[children,_isymbol2essential_,_may_osymbolXseq_]==>>ok-isymbol-dependency==>>which children ignore
ignore:
    ignore oresult, only is_ok
    unless stick to output oresult#property of child not rgnr
    see:_isymbol2essential_
rgnr.children<env> finite persistent/stable(not-tmp-created-rgnr)
    ref
    rgnr._iter_persistent_children6env_(env)
istream.view_tokens6backward#back_cache
    istream.max_num_tokens6backward
    rgnr.required_num_tokens6backward

DONE:ref ~ env.name2rgnr_
DONE:named ~ env.name2may_gpostprocess6ok_
DONE:flip:invert_ok_err
DONE:empty_loader
    cancel:empty_ok
    cancel:empty_err
DONE:optional
flow:
    switch
    if_then_else
    while_loop
    pure ctx modifier

BoolVar
ObjVar - io
IOVarPair - io

DONE:tag #Cased
    IRecognizerLLoo__tag
        ++IRecognizerLLoo__priority_parallel
    IRecognizerLLoo__spostprocess
        #IRecognizerLLoo__spostprocess6ok
        vs:IRecognizerLLoo__gprepostprocess
lift:eresult --> oresult:lift
    lift__forgivable_()
    lift__strict_()
optional:
    optional__forgivable_()
    optional__strict_()
DONE:
many
    vs:repetition
end_by
    be nongreedy: body*? end
    # since greedy <==> (body*, ignore end)
    flow:while 1: if ignore end then break else body
    flow:while not (ignore end): body
        auto:trial_and_error_(condition-rgnr)
sep_by1(sep, body)
    ^body unpack(ignore sep, ^body)*
    flow:body,while unpack(ignore sep, ^body):pass
sep_end_by1(end, sep, body)
    body unpack(ignore sep, ^body)*? end
    flow:body,while not (ignore end):unpack(ignore sep, ^body)
between(open, end, body)
    unpack(ignore ^open, body, ignore end)
DONE:
any_tkey
eof === not_followed_by(any_tkey)
not_eof === followed_by(any_tkey)
tkey
tkey_seq
tkey_qset
tkey_qset_seq
tkey_prefix_tree
    ++tag_rgnr_++switch_case
    view ../../python3_src/seed/seq_tools/mk_prefix_tree.py
??tkey_dqset_prefix_tree
    dqset: __ne__ required disjoint
    ===
    qset-query_set
    dqset-disjointable_query_set
        dqset is ?rng_based_set?
        prefix_tree use ?sorted-mapping?
TODO:
switch_cased(io_sym, priority_parallel([tag_rgnr_(...)...])|tkey_prefix_tree, tag2rgnr)
if_tmay(io_sym, optional__xxx_(rgnr8condition), rgnr8then, rgnr8else)
TODO:
flow-parts:
    # auto:trial_and_error_(condition-rgnr)
    #   ==>> ((fail&&changed)|(fail&&unchanged)|ok)
    #   ==>> (fail|False|True)
    #
    # (part,stmt_position) <=> (rgnr, unlock_case, unpack_case, fail_vs_stop_vs_continue)
    #   condition-rgnr:fail_vs_stop_vs_continue=2/"continue"
    #   non_condition-rgnr:fail_vs_stop_vs_continue=0/"fail"
    part = (rgnr, unlock_case, unpack_case)
    stmt_ a =:
        | part/rgnr
        | return part
        | return symbol
        | return eresult
        | [a]
        | while     (a) xstmt (a)
        | while_not (a) xstmt (a)
        | if (a) (a) (a)
        | try (a) (a) (a)
            # <==> if_not (a) (a) (a)
        | label
        | goto label
        | match symbol {k:(a)} (a) #switch
        # pure ctx modifier
        #   exec(code, locals/bijection{nm:symbol})#MutableBijection
        | assignment symbol value
        | assignment symbol rgnr
        | assignment symbol symbol [(attr|key)]
        | assignment symbol [(attr|key)] symbol
        | assignment symbol [symbol]
        | assignment [symbol] symbol
        | delete [symbol]
        ???xxx | call_then_assignment (may stream) stream [(attr|key)] [istream]
            expr ~ rgnr
    stmt := stmt_ stmt
    xstmt =:
        | stmt_ xstmt
        | break_loop    #goto internal label
        | continue_loop #goto internal label
        | break_try     #goto internal label
        | break_scope num_layers #goto internal label
    ???bool_expr
        ==
        <=
        in
        and
        or
        not
        is
        ...
    expr:eval(code, locals/bijection{nm:symbol})#MutableBijection
rgnr.__op__
forkable implies ISnapshot
AddUnlocker
    known_released

]]

[[
#DONE:trial,optional...-->extend Call to contain external_cache to avoid save:(rgnr,try_rgnr_(rgnr)) via buitin support
#   RecognizeCall --> (Call|mk_Call_)
#   => :『light_wrap_rgnr_()』
#       try_rgnr_-->trial_and_error_
#DONE:recur5yield__ver3 strict type+send()as GI + class ABC 4 subclassing... allow GI to avoid save:(rgnr,try_rgnr_(rgnr)) via call mk_gi directly...
#   e ../../python3_src/seed/func_tools/recur5yield__strict.py
#   => :『@_decorator44rngr$recognize_()』
#DONE:list high freq exconfigpack and register them...
#   => 『get_info_ex4high_freq_sconfigpack_()』
#DONE:only『not_followed_by_()』: flip only for (forgivable_fail) ==>> ???only for try # i.e. flip(try_rgnr_(rgnr)) try_rgnr_() is not enough!!! how to avoid severe_fail??? ==>> severe_try
#DONE: postcondition: reply.ok=>unlocker.known_released

]]
[[
dependented by:
    view ../../python3_src/seed/recognize/recognizer_LLoo__ver2_/solo_rgnr_transform_cases.py
===
move from IRecognizerLLoo__lift.__doc__
===:
######################
# [:protected_fail__vs__forgivable_fail__vs__severe_fail]:here
######################
two perspectives of failure from inner vs outer respectively:
    inner impl:using snapshot:
        protected_fail:not ok,snapshot unreleased
        forgivable_fail:not ok,snapshot released,monotonic_idx unchanged
        severe_fail:not ok,snapshot released,monotonic_idx changed
    outer call:not using snapshot:
        forgivable_fail:not ok,monotonic_idx unchanged
        severe_fail:not ok,monotonic_idx changed
######################
# [:lookahead__vs__try__vs__optional__vs__lift]:here
######################
vs: lookahead, try, optional, lift
    * lookahead:
        seekback monotonic_idx8begin
        untouch eresult
            (severe_fail|protected_fail|forgivable_fail)-->forgivable_fail
    * try:
        untouch severe_fail
        untouch forgivable_fail
        convert protected_fail into forgivable_fail
            seekback monotonic_idx8begin
            untouch eresult
        untouch oresult
    * optional[_forgivable_fail_be_ok_==False]:
        untouch severe_fail
        untouch forgivable_fail
        convert protected_fail into oresult:=null_tuple
            seekback monotonic_idx8begin
        wrap oresult as (oresult,)
    * lift[_forgivable_fail_be_ok_==True]:
        untouch severe_fail
        convert forgivable_fail in to oresult:=(case4fail:=2, unchanged:=True,old-reply)
        convert protected_fail into oresult:=(case4fail:=1, unchanged:=???,old-reply)
            seekback monotonic_idx8begin
        lift oresult as (case4fail=0, unchanged:=???,old-reply)
    * lift[_forgivable_fail_be_ok_==False]:
        untouch severe_fail
        untouch forgivable_fail
        convert protected_fail into oresult:=(case4fail:=1, unchanged:=???,old-reply)
            seekback monotonic_idx8begin
        lift oresult as (case4fail=0, unchanged:=???,old-reply)
######################
how many combinations?
    #################
    * protected:severe_fail
        [#using detection_unlocker/DetectionUnlocker#]
        (unlocker,snapshot) donot release at all
        ############
        * severe_fail-->({<seekback monotonic_idx8begin>}|{<not seekback monotonic_idx8begin>})
            * {<(protected_fail|severe_fail)>} <<=={<not seekback monotonic_idx8begin>}
                2
            * {<(protected_fail|ok|forgivable_fail)>} <<=={<seekback monotonic_idx8begin>}
                3
            5
        ############
        * protected_fail-->({<seekback monotonic_idx8begin>}|{<not seekback monotonic_idx8begin>})
            * {<(protected_fail|severe_fail)*(protected_fail|ok|forgivable_fail)>} <<=={<not seekback monotonic_idx8begin>}
                2*3==6
            * {<(protected_fail|ok|forgivable_fail)>} <<=={<seekback monotonic_idx8begin>}
                3
            9
        ############
        * forgivable_fail-->(ok|protected_fail|forgivable_fail)
            * {<(protected_fail|ok|forgivable_fail)>} <<=={<seekback monotonic_idx8begin>}
            3
        ############
        * ok-->({<seekback monotonic_idx8begin>}|{<not seekback monotonic_idx8begin>})
            * {<(ok|protected_fail|severe_fail)*(protected_fail|ok|forgivable_fail)>} <<=={<not seekback monotonic_idx8begin>}
                3*3==9
            * {<(protected_fail|ok|forgivable_fail)>} <<=={<seekback monotonic_idx8begin>}
                3
            12
        ############
        5*9*3*12==1620
        but some combinations are irrational
        , i.e. can lift performence
        , i.e. can overlap with below cases
    #################
    * unprotected:severe_fail
        [#using (unlocker>>snapshot)#]
        snapshot auto release, cannot seekback:
        ############
        =>untouch severe_fail
            1
        ############
        * ok-->({<not seekback monotonic_idx8begin>})
            * {<(ok|severe_fail)*(ok|forgivable_fail)>} <<=={<not seekback monotonic_idx8begin>}
            4
        ############
        * protected_fail-->({<seekback monotonic_idx8begin>}|{<not seekback monotonic_idx8begin>})
            * {<(protected_fail|severe_fail)*(protected_fail|ok|forgivable_fail)>} <<=={<not seekback monotonic_idx8begin>}
                2*3==6
            * {<(protected_fail|ok|forgivable_fail)>} <<=={<seekback monotonic_idx8begin>}
                3
            9
        ############
        * forgivable_fail-->(ok|forgivable_fail)
            * {<(ok|forgivable_fail)>} <<=={<seekback monotonic_idx8begin>}
            2
        ############
        1*4*9*2==72
    #################
    * unprotected:protected_fail
        [#using (unlocker>>detection_unlocker)#]
        no snapshot, cannot seekback:
        ############
        =>untouch severe_fail
            1
        ############
        * ok-->({<not seekback monotonic_idx8begin>})
            * {<(ok|severe_fail)*(ok|forgivable_fail)>} <<=={<not seekback monotonic_idx8begin>}
            4
        ############
        * protected_fail-->({<not seekback monotonic_idx8begin>})
            * {<(protected_fail|severe_fail)*(protected_fail|ok|forgivable_fail)>} <<=={<not seekback monotonic_idx8begin>}
                2*3==6
            6
        ############
        * forgivable_fail-->(ok|forgivable_fail)
            * {<(ok|forgivable_fail)>} <<=={<seekback monotonic_idx8begin>}
            2
        ############
        1*4*6*2==48
    #################
    total==1620+72+48-???=1620
        since 1620 cover all possible cases
            72 are more optimal conditions
            48 are most optimal conditions
    #################
######################
how many combinations?

144 #single_item_only:exclude:protected_ok
245 #single_item_only:include:protected_ok
4050 #best&&exclude:protected_ok
589824 #best&&include:protected_ok
6424 #good&&exclude:protected_ok
751296 #good&&include:protected_ok
    <<==:
    view ../../python3_src/seed/recognize/recognizer_LLoo__ver2_/solo_rgnr_transform_cases.py
    * calc_total_all_possible_exconfigs_via_iter_
        1152
    * calc_total_all_good_exconfigs_via_iter_
        245 #only one item # :: (case4protection, (case4reply5child, case4seekback, case4reply5self))
    * calc_total_all_good_exconfigpacks_via_iter_
        751296 #full # :: (case4protection, full-{case4reply5child: (case4seekback, case4reply5self)})
    * calc_total_all_best_exconfigpacks_via_iter_
        589824 #full with optimal-case4protection
######################
######################
]]

===
]]]


[[
######################
view ../../python3_src/seed/recognize/recognizer_LLoo__ver2_/doctest4IRecognizerLLoo.py
py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LLoo__ver2_.doctest4IRecognizerLLoo:__doc__ -ht
######################
######################
example-snippet:
######################
######################

RecoverableInputStream9LazyList :: uint -> IPositionInfo4Gap -> Iter token -> RecoverableInputStream9LazyList
    def __init__(sf, max_num_tokens6backward, prev_token_end_gap_position_info, nonlazylist_iter_tokens8istream, /):
PlainRecoverableInputStream5token_seq :: uint -> may IPositionInfo4Gap -> uint -> [token] -> PlainRecoverableInputStream5token_seq
    def __init__(sf, max_num_tokens6backward, may_prev_token_end_gap_position_info, offset, token_seq, /):
def mk_token_rawstream__5xs__idx_(offset, xs, ex_arg=None, /, *, tkey_vs_tdat_vs_tkd:'(0|1|2)'):
    'uint -> Iter (tkey|tdat|tkd) -> (((tkey -> tdat)|tdat/non_callable)|((tdat -> tkey)|tkey/non_callable)|None) -> (tkey_vs_tdat_vs_tkd/(0|1|2)) -> rawstream/(IPositionInfo4Gap, Iter IToken)'

def Environment.__init__(sf, param2setting, name2rgnr, name2may_gpreprocess, name2may_gpostprocess6err, name2may_gpostprocess6ok, /):
def recognize_(main_rgnr, env, gctx, istream, /, *, ignore=False):
    'IRecognizerLLoo -> env/IEnvironment -> gctx/mapping -> istream/IInputStream -> Reply'#@wrapper

begin_doctest:here
>>> from seed.types.IToken import mk_token_rawstream__5xs__idx_
>>> from seed.types.stream.IRecoverableInputStream import PlainRecoverableInputStream5token_seq, RecoverableInputStream9LazyList
>>> from seed.types.IToken import char_qset__isdecimal
>>> from seed.types.Tester import Tester__eq_obj


>>> tkey_vs_tdat_vs_tkd=0; tkn_qset5xqset_=TokenKeyQuerySet5xqset # [tkey :: char]
>>> def _mk_istream5src(src, /):
...     (gap0, iter_tokens) = mk_token_rawstream__5xs__idx_(0, src, tkey_vs_tdat_vs_tkd=tkey_vs_tdat_vs_tkd)
...     #istream = PlainRecoverableInputStream5token_seq(0, gap0, 0, [*iter_tokens])
...     istream = RecoverableInputStream9LazyList(0, gap0, iter_tokens)
...     return istream
>>> mkrs = Makers4IRecognizerLLoo
>>> rgnr8digit = mkrs.spost__tkn2tkey_(mkrs.token_(tkn_qset5xqset_(char_qset__isdecimal)))
>>> digits1 = mkrs.many_(rgnr8digit, 1)
>>> spaces1 = mkrs.many_(mkrs.spost__tkn2tkey_(mkrs.token_(tkn_qset5xqset_(Tester__eq_obj(' ')))), 1)
>>> digits1
RecognizerLLoo__many(RecognizerLLoo__spost__tkn2tkey(RecognizerLLoo__token(TokenKeyQuerySet5xqset(char_qset__isdecimal))), 1)
>>> spaces1
RecognizerLLoo__many(RecognizerLLoo__spost__tkn2tkey(RecognizerLLoo__token(TokenKeyQuerySet5xqset(Tester__eq_obj(' ')))), 1)
>>> sym6 = mkrs.spost__tkn2tkey_(mkrs.token_(tkn_qset5xqset_(Tester__eq_obj('(')))) #')('
>>> sym9 = mkrs.spost__tkn2tkey_(mkrs.token_(tkn_qset5xqset_(Tester__eq_obj(')')))) #
>>> sym_plus = mkrs.spost__tkn2tkey_(mkrs.token_(tkn_qset5xqset_(Tester__eq_obj('+')))) #

>>> nm4add_expr = Symbol4IRecognizerLLoo('add_expr')
>>> ref__add_expr = mkrs.ref_(nm4add_expr)

>>> group_expr = mkrs.between_(sym6, sym9, ref__add_expr)
>>> atom_expr = mkrs.priority_parallel_([digits1, group_expr])
>>> add_expr = mkrs.named_(nm4add_expr, mkrs.sep_by_(sym_plus, atom_expr, 1))
>>> repr(add_expr) == (
... "RecognizerLLoo__named(nm4rgnr_.add_expr"
...   ", RecognizerLLoo__sep_by("
...     "RecognizerLLoo__spost__tkn2tkey(RecognizerLLoo__token(TokenKeyQuerySet5xqset(Tester__eq_obj('+'))))"
...     ", RecognizerLLoo__priority_parallel("
...       "(RecognizerLLoo__many(RecognizerLLoo__spost__tkn2tkey(RecognizerLLoo__token(TokenKeyQuerySet5xqset(char_qset__isdecimal))), 1)"
...       ", RecognizerLLoo__between("
...         "RecognizerLLoo__spost__tkn2tkey(RecognizerLLoo__token(TokenKeyQuerySet5xqset(Tester__eq_obj('('))))"
...         ", RecognizerLLoo__spost__tkn2tkey(RecognizerLLoo__token(TokenKeyQuerySet5xqset(Tester__eq_obj(')'))))"
...         ", RecognizerLLoo__ref(nm4rgnr_.add_expr)"
...         ")"
...       ")"
...     "), 1))"
... )
True


>>> (name2rgnr, nms4ref, nms6ref) = collect_namess5rgnrs_([add_expr])
>>> name2rgnr == {nm4add_expr:add_expr}
True
>>> env = Environment(param2setting:={}, name2rgnr, name2may_gpreprocess:={}, name2may_gpostprocess6err:={}, name2may_gpostprocess6ok:={})
>>> gctx = {}

>>> istream = _mk_istream5src('555')
>>> recognize_(add_expr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(True, (('5', '5', '5'),)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))

>>> istream = _mk_istream5src('5+9')
>>> recognize_(add_expr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(True, (('5',), ('9',))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))

>>> istream = _mk_istream5src('(9)')
>>> recognize_(add_expr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(True, ((('9',),),)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 3), PositionInfo4Gap__idx(3)))

>>> istream = _mk_istream5src('(505+(3+40))')
>>> recognize_(add_expr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(True, ((('5', '0', '5'), (('3',), ('4', '0'))),)), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 12), PositionInfo4Gap__idx(12)))

>>> istream = _mk_istream5src('505+xxxx')
>>> recognize_(add_expr, env, gctx, istream) #doctest: +ELLIPSIS
Reply(Either(False, (TokenKeyQuerySet5xqset(Tester__eq_obj('(')), BaseToken(PositionInfo4Span(PositionInfo4Gap__idx(4), PositionInfo4Gap__idx(5)), Cased('x', None)))), ExtPositionInfo(MonotonicIndex(<object object at 0x...>, 5), PositionInfo4Gap__idx(5)))




unitest per mkr@Makers4IRecognizerLLoo:
    => view ../../python3_src/seed/recognize/recognizer_LLoo__ver2_/doctest4IRecognizerLLoo.py


end_doctest:here
]]




py_adhoc_call   seed.recognize.recognizer_LLoo__ver2_.IRecognizerLLoo   @f

#]]]'''
__all__ = r'''
forbid_xxx_protected_ok


mk_gi4IRecognizerLLoo__5solo_rgnr_transform_cases_
    CASES
    name_set4high_freq_sconfigpack
    get_info_ex4high_freq_sconfigpack_
        default_info4mk_gi
        get_symbol8high_freq_sconfigpack_
    get_setting_
    get_weak_symbolize_register4sexconfigpack_
        is_good_sexconfigpack_


Makers4IRecognizerLLoo
tag_rgnr_
light_wrap_rgnr_
    lookahead_
        not_followed_by_
        followed_by_
    lift__forgivable_
    lift__strict_
        optional__forgivable_
        optional__strict_
    protect_header_     trial_and_error_
    whole8header_
        protect_whole_
    empty8header_





IRecognizerLLoo
    recognize_
    RecognizeCall   Call mk_Call_
    Reply           RecognizeReply
        ExtPositionInfo
    XContext
    ContextView
        Symbol4GlobalVarable
        Symbol4LocalVarable
    Symbol4IRecognizerLLoo
        collect_namess5rgnrs_

IRecognizerLLoo
    collect_namess5rgnrs_
    check_may_weakable_name

    IRecognizerLLoo__default_mixins
    RecognizerLLoo__named
    RecognizerLLoo__ref
        explain_may_emay_weakable_name
        check_may_emay_weakable_name
        check_weakable_name
            Symbol4IRecognizerLLoo
    IRecognizerLLoo__serial
        RecognizerLLoo__dependent_pair
    IRecognizerLLoo__priority_parallel
    IRecognizerLLoo__gsep_end_by
        IRecognizerLLoo__gsep_end_by__init
            RecognizerLLoo__gsep_end_by
                RecognizerLLoo__many
                RecognizerLLoo__end_by
                RecognizerLLoo__sep_by
                RecognizerLLoo__sep_end_by
    IRecognizerLLoo__two_children6env
        IRecognizerLLoo__repetition
    IRecognizerLLoo__solo_child6env
        IRecognizerLLoo__alias
        IRecognizerLLoo__gprepostprocess
            apply_may_gpreprocess_
            apply_may_gpostprocess_
        IRecognizerLLoo__spostprocess
            apply_may_spostprocess_
        IRecognizerLLoo__tag
    IRecognizerLLoo__solo_child6env__init
        RecognizerLLoo__not_ignore
        RecognizerLLoo__ignore
        RecognizerLLoo__none8oresult_if_ignore
        IRecognizerLLoo__alias__init
            BaseRecognizerLLoo__alias__default_mixins
                RecognizerLLoo__unbox_tuple
                    RecognizerLLoo__between
                IRecognizerLLoo__dependent_pair__spost
                    RecognizerLLoo__switch_cased
                    RecognizerLLoo__switch_branches
        IRecognizerLLoo__forgivable_fail_ok__solo_child6env__init
        IRecognizerLLoo__gprepostprocess__init
            RecognizerLLoo__gprepostprocess
        IRecognizerLLoo__spostprocess__init
            RecognizerLLoo__spostprocess
            IRecognizerLLoo__spostprocess__init__default_mixins
                IRecognizerLLoo__spostprocess__init__default_mixins__static
                    IRecognizerLLoo__spost__fmap4tuple
        IRecognizerLLoo__tag__init
            RecognizerLLoo__tag
                tag_rgnr_
        RecognizerLLoo__light_wrap
            light_wrap_rgnr_
    IRecognizerLLoo__two_children6env__init
        IRecognizerLLoo__repetition__init
            RecognizerLLoo__repetition
    IRecognizerLLoo__init__rgnrs
        RecognizerLLoo__priority_parallel
    RecognizerLLoo__serial
        mk_unlock_case
        explain_unpack_case_with_
        explain_unpack_case
    IRecognizerLLoo__constant_loader
        RecognizerLLoo__constant_loader
    IRecognizerLLoo__no_child6env
        IRecognizerLLoo__eof
        IRecognizerLLoo__not_eof
        IRecognizerLLoo__any_token
        IRecognizerLLoo__token
        IRecognizerLLoo__token_seq

    IRecognizerLLoo__no_child6env__init
        IRecognizerLLoo__token_seq__init
            RecognizerLLoo__token
        IRecognizerLLoo__token__init
            RecognizerLLoo__token_seq
        RecognizerLLoo__eof
        RecognizerLLoo__not_eof
        RecognizerLLoo__any_token
    RecognizerLLoo__try_except_else
        RecognizerLLoo__try_except_else__spost







IUnlocker
    DummyUnlocker
        dummy_unlocker
    DetectionUnlocker
    AddUnlocker
    Unlocker5ISnapshot
ISnapshot
MonotonicIndex
IBaseInputStream
    IInputStream IRecoverableInputStream
    PlainRecoverableInputStream5token_seq
    RecoverableInputStream9LazyList

WeakableSymbol5name
    Symbol4IRecognizerLLoo
    Symbol4GlobalVarable
    Symbol4LocalVarable
IEnvironment
    getset_external_cache4func
    getset_external_cache4method
    Environment
        mk_gpreprocess__5constant_
        mk_gpostprocess6err__5spost_
        mk_gpostprocess6ok__5spost_
        mk_gpreprocess__5lazy_st_
        mk_gpostprocess6err__5spost_after_tag_st_
        mk_gpostprocess6ok__5spost_after_tag_st_
IHalfMap
    WeakKeyHalfMap

IRecognizerLLoo__serial
    DummyList
        dummy_list
    BoolVar
    ObjVar
    Output__oresult

Error
    ValidateError
    InputStreamError__eof
    ReleasedError


IHasAttr__forgivable_fail_be_ok
    IRecognizerLLoo__forgivable_fail_ok__solo_child6env__init

IHasAttr__force_postprocess_when_ignore
    IRecognizerLLoo__gprepostprocess
    IRecognizerLLoo__spostprocess
    RecognizerLLoo__try_except_else
        RecognizerLLoo__try_except_else__spost


apply_may_func_
apply_may_gpreprocess_
apply_may_gpostprocess_
check_may_callable

fmap_may_
check_may_IRecognizerLLoo


mk_head_unlock_idx_ex5min_
pop_defaults_
mk_ignorable_unpack_case_



IRecognizerLLoo__spostprocess__init__default_mixins__static
    RecognizerLLoo__spost__unbox
    RecognizerLLoo__spost__tkn2tkd
    RecognizerLLoo__spost__tkn2tkey
    RecognizerLLoo__spost__tkn2tdat
    RecognizerLLoo__spost__tkd2tkey
    RecognizerLLoo__spost__tkd2tdat
    IRecognizerLLoo__spost__fmap4tuple
        RecognizerLLoo__spost__fmap4tuple__tkn2tkd
        RecognizerLLoo__spost__fmap4tuple__tkn2tkey
        RecognizerLLoo__spost__fmap4tuple__tkn2tdat
        RecognizerLLoo__spost__fmap4tuple__tkd2tkey
        RecognizerLLoo__spost__fmap4tuple__tkd2tdat
mk_casedT_
pair2Cased_
unbox
tkn2tkd_
tkn2tkey_
tkn2tdat_
tkd2tkey_
tkd2tdat_


Makers4IRecognizerLLoo
    rgnr__any_token
    rgnr__eof
    rgnr__not_eof
    rgnr__any_tkd
    rgnr__any_tkey
    rgnr__any_tdat

'''.split()#'''
__all__
r'''[[[
(lookahead__vs__try__vs__optional__vs__lift)
below deprecated by light_wrap_rgnr_():
.    IRecognizerLLoo__solo_child6env
.        IRecognizerLLoo__lookahead
.        IRecognizerLLoo__try
.        IRecognizerLLoo__optional
.        IRecognizerLLoo__lift
.    IRecognizerLLoo__solo_child6env__init
.        IRecognizerLLoo__lift__init
.            RecognizerLLoo__lift
.        IRecognizerLLoo__optional__init
.            RecognizerLLoo__optional
.        RecognizerLLoo__try
.            try_rgnr_
.        RecognizerLLoo__lookahead

#]]]'''#'''
        #xxx:IRecognizerLLoo__flip
        #xxx:RecognizerLLoo__flip

    #InputStreamError__has_been_read
#xxx:IBoxedInputStream
    #xxx:IForkableInputStream
#xxx:Snapshot4IForkableInputStream
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from types import FunctionType as Func, MethodType as Meth




from seed.types.Tester import is_good, always_tri_test
from seed.types.Tester import ITester, IXQuerySet
from seed.types.IToken import (
ITokenQuerySet
,   ITokenKeyedDataQuerySet
,       ITokenKeyQuerySet
,is_good_token_
,   is_good_token_keyed_data_
,       is_good_token_key_
,       is_good_token_data_
,       ITokenDataQuerySet
,TokenQuerySet5xqset
,TokenKeyedDataQuerySet5xqset
,TokenKeyQuerySet5xqset
,TokenDataQuerySet5xqset
)




from seed.func_tools.recur5yield__strict import BoxedTailRecur, BoxedFinalResult
from seed.func_tools.recur5yield__strict import IDecorator4recur5yield, Decorator4recur5yield
from seed.func_tools.recur5yield__strict import IExecutor4recur5yield, IExecutor4recur5yield__dispatch_by_dict, Executor4recur5yield__dispatch_by_dict

from seed.for_libs.for_inspect import get_signature_of__py3_
from seed.types.mapping.DynamicStackedMapping import DynamicStackedMapping
from collections.abc import Mapping, MutableMapping
from seed.types.Either import Cased, Either
from seed.types.Either import mk_Left, mk_Right



from seed.types.mapping.Bijection import Bijection, MutableBijection
from seed.types.mapping.Bijection import explain_hyperkey

from weakref import ref as wref_, WeakKeyDictionary as WkeyD, WeakValueDictionary as WvalD
from seed.iters.count_ import count_

from seed.types.FrozenDict import FrozenDict, mk_FrozenDict, empty_FrozenDict
from seed.tiny import ifNone, echo, mk_tuple, mk_frozenset, null_tuple, null_frozenset, null_mapping_view, fst, MapView, print_err, snd
from seed.tiny_.check import check_type_is, check_type_le, check_non_ABC, check_int_ge, check_int_ge_lt, check_int_ge_le, check_callable
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.helper.repr_input import repr_helper
from seed.tiny_._Base4repr import _Base4repr
        #sf._reset4repr(may_args4repr, may_kwds4repr)
        #sf._init4repr(*args4repr, **kwds4repr)
        ######################
        # !! ++ IRecognizerLLoo__serial._not_ignore_toplvl_
        # !! ++ _Base4repr._kwds4repr:should overwrite both at once
        #below deprecated:
        #   #sf._args4repr = (...)
        #   #if 0:sf._kwds4repr = {...}
        ######################



___end_mark_of_excluded_global_names__0___ = ...

__all__

from seed.recognize.recognizer_LLoo__ver2_.solo_rgnr_transform_cases import mk_gi4IRecognizerLLoo__5solo_rgnr_transform_cases_
_mk_wrapped_gi = mk_gi4IRecognizerLLoo__5solo_rgnr_transform_cases_
from seed.recognize.recognizer_LLoo__ver2_.solo_rgnr_transform_cases import get_setting_, get_weak_symbolize_register4sexconfigpack_, is_good_sexconfigpack_
from seed.recognize.recognizer_LLoo__ver2_.solo_rgnr_transform_cases import CASES, name_set4high_freq_sconfigpack, get_info_ex4high_freq_sconfigpack_, default_info4mk_gi, get_symbol8high_freq_sconfigpack_

from seed.types.stream.IRecoverableInputStream import \
(    InputStreamError__eof
,    ReleasedError
#    NotSameStreamError
#        NotSameStreamNameError
#
,MonotonicIndex
,ExtPositionInfo
,IBaseInputStream
,    IRecoverableInputStream
,        PlainRecoverableInputStream5token_seq
,        RecoverableInputStream9LazyList
,ISnapshot
#
,IUnlocker
,    DummyUnlocker
,        dummy_unlocker
,    DetectionUnlocker
,    AddUnlocker
,    Unlocker5ISnapshot
)

IInputStream = IRecoverableInputStream

forbid_xxx_protected_ok = True

class Error(Exception):pass
class ValidateError(Error):pass

class RecognizeCall(tuple):
    '[exargs4lwrap :: [nm4info_ex4mk_gi]]'
        # <<== should use nm4info_ex4mk_gi as exarg, since ++to_invert_ok_err[#which only be used by not_followed_by#]
            # '[exargs4lwrap :: [(nm|info_ex4mk_gi/(symbol8sexconfigpack, may info4mk_gi/(may_ignore, to_lift, may_spostprocess6err, may_spostprocess6ok, to_invert_ok_err)))]]'
        #<<==get_info_ex4high_freq_sconfigpack_
        #==>>light_wrap_rgnr_
        #
        #may_exarg --> exargs4lwrap
    #xxx '[may_exarg :: may (symbol8sexconfigpack, to_lift/bool, spreprocess, spostprocess6err, spostprocess6ok)]'
    __slots__ = ()
    def __repr__(sf, /):
        return repr_helper(sf, *sf)
    def __new__(cls, rgnr, unlocker, ignore, istream, exargs4lwrap, /):
        return tuple.__new__(cls, [rgnr, unlocker, ignore, istream, exargs4lwrap])

class Reply(tuple):
    '[ext_info8end :: ExtPositionInfo][ext_info8end == (monotonic_idx8end, gap_info8end)]'
    __slots__ = ()
    def __repr__(sf, /):
        return repr_helper(sf, *sf)
    def __new__(cls, /, eresult, ext_info8end):
        check_type_is(Either, eresult)
        check_type_is(ExtPositionInfo, ext_info8end)
        return tuple.__new__(cls, [eresult, ext_info8end])
    @property
    def eresult(sf, /):
        return sf[0]
    @property
    def ext_info8end(sf, /):
        '-> ext_info8end/ExtPositionInfo'
        return sf[1]
    @property
    def monotonic_idx8end(sf, /):
        return sf.ext_info8end.monotonic_idx
    @property
    def gap_info8end(sf, /):
        return sf.ext_info8end.gap_info
    @property
    def ok(sf, /):
        '-> bool'
        return sf.eresult.is_right
    @property
    def errmsg(sf, /):
        '-> bool'
        return sf.eresult.left
    @property
    def oresult(sf, /):
        '-> bool'
        return sf.eresult.right

    def as_dict(sf, /):
        return dict(eresult=sf.eresult, ext_info8end=sf.ext_info8end)
    def ireplace(sf, /, **kwds):
        if all(v is getattr(sf, nm) for nm, v in kwds.items()):
            return sf
        d = sf.as_dict()
        d.update(kwds)
        return type(sf)(**d)
#mk_Call_ = RecognizeCall
Call = RecognizeCall
def mk_Call_(rgnr, unlocker, ignore, istream, exargs4lwrap=null_tuple, /):
    return Call(rgnr, unlocker, ignore, istream, exargs4lwrap)

RecognizeReply = Reply

class IRecognizerLLoo(ABC):
    r'''[[[
    [IRecognizerLLoo <: Weakable]
    [IRecognizerLLoo all descendants are persistent rgnrs per env (i.e. output rgnrs of ._mk_gi4recognize_(...env...)) #descendants are env-relevant]
    [should not call IRecognizerLLoo._mk_gi4recognize_() directly since rgnr._is_ctx_scope_/._may_name4ref_(gpreprocess|gpostprocess6err|gpostprocess6ok) (should call via 『yield Call(...)』)]
    [IRecognizerLLoo._mk_gi4recognize_():postcondition:[[reply.ok==True]=>[unlocker.known_released==True]]]
    [solo vs descendants:IRecognizerLLoo all solo abstractmethod neednot consider children/descendants #?hence env-irrelevant? yes! since rgnrs/descendants(except main_rgnr) are dependented on env so their solo properties neednot dependented env]
    [name :: Hashable&&Weakable]
        Weakable <<== may_emay_nm
        nm4ref
        nm6ref
        xxx nm4pre
        xxx nm4post
        nm4pre := nm4ref
        nm4post := nm4ref
    # [:lookahead__vs__try__vs__optional__vs__lift]:goto
    # [:protected_fail__vs__forgivable_fail__vs__severe_fail]:goto
    ######################
    env:
        #immutable
        .param2setting_
        .name2rgnr_
        .name2may_gpreprocess_
        .name2may_gpostprocess6err_
        .name2may_gpostprocess6ok_
    gctx:
        #mutable
        :: Mapping
    ctx:
        #mutable
        :: DynamicStackedMapping
            serial:enter/exit
    xctx_view :: ContextView<gctx,ctx>
    unlocker:
        #to free prev protect resource asif succ
        .known_released :: bool
            xxx .is_dummy_unlocker :: bool
        .unlocker_release()
            .__del__()
            .close()
        .__add__(unlocker, unlocker)
            unlocker + unlocker
            if ot.known_released:return sf
            if sf.known_released:return ot
        .__rshift__(unlocker, snapshot)
            unlocker >> snapshot
    symbol:
        ._local_vs_global_ :: bool
            used in (gctx | ctx)
    eresult:
        :: Either errmsg oresult
    reply:
        :: (eresult, ext_info8end)
        .monotonic_idx8end
        .gap_info8end
        .ok
        .oresult |^AttributeError
        .errmsg |^AttributeError
    monotonic_idx:
        __eq__
        __hash__
        ?total_ordering?
        ?__sub__ -> num_tokens?
    istream:
        .eof :: bool
        .head :: (token | ^InputStreamError__eof)
        .peek_le(sz) -> [token]
        .peek_iter() -> Iter token
        .read1() -> token
        .read_le(sz) -> [token]
        .read_iter() -> Iter token
        .tell_gap_info() -> prev_gap_info
        .tell_monotonic_idx() -> monotonic_idx
        .save2snapshot() -> snapshot
        .restore5snapshot_(snapshot, copy_vs_move) -> None|^ReleasedError
            .restore5snapshot__copy(snapshot) -> None|^ReleasedError
            .restore5snapshot__move(snapshot) -> None|^ReleasedError
    snapshot:
        xxx [snapshot <: unlocker]
            .snapshot_release()
            .snapshot_released :: bool
        .restore_and_hold(istream) -> (None|^ReleasedError)
        .restore_and_release(istream) -> (None|^ReleasedError)

    ######################
    serial-rgnr:
        _unlocker = unlocker if sf.release_at_fst else dummy_unlocker
        reply = yield RecognizeCall(child_rgnr, _unlocker, ignore, istream)
        if not reply.ok:
            return reply
        if sf.release_at_gap:
            unlocker.unlocker_release()
        _unlocker = unlocker if sf.release_at_snd else dummy_unlocker
        reply = yield RecognizeCall(child_rgnr, _unlocker, ignore, istream)
        if reply.ok:
            unlocker.unlocker_release()
        return reply

    ######################
    priority_parallel-rgnr:
        snapshot = istream.save2snapshot()
        reply = yield RecognizeCall(child_rgnr, unlocker >> snapshot, ignore, istream)
        if reply.ok or snapshot.snapshot_released:
            snapshot.snapshot_release()
            return reply
        snapshot.restore_and_hold(istream)
        reply = yield RecognizeCall(child_rgnr, unlocker >> snapshot, ignore, istream)
        if reply.ok or snapshot.snapshot_released:
            snapshot.snapshot_release()
            return reply
        snapshot.restore_and_release(istream)
        777;    del snapshot
        reply = yield RecognizeCall(child_rgnr, unlocker, ignore, istream)
        return reply
    ######################
    lookahead-rgnr:
        snapshot = istream.save2snapshot()
        reply = yield RecognizeCall(child_rgnr, dummy_unlocker, ignore, istream)
        snapshot.restore_and_release(istream)
        777;    del snapshot
        777;    reply = reply.ireplace(ext_info8end=istream.tell_ext_info())
        if reply.ok:
            unlocker.unlocker_release()
        return reply

    ######################

    ######################
    typing:
    serial-rgnr:
        [unlock_case :: (may begin_vs_middle/bool)]
            unlock_case = mk_unlock_case(unlock_idx, begin_vs_middle, k)
        [unpack_case :: (0/ignore|1/ignorable_normal|2/ignorable_unpack|-1/non_ignorable_normal|-2/non_ignorable_unpack)]
            explain_unpack_case_with_()
            explain_unpack_case()
        [fail_vs_stop_vs_continue :: {0,1,2}]
        [var_changed :: BoolVar{monotonic_idx8begin.changed}]
        [var_ok :: BoolVar{reply.ok}]
        [fail_vs_stop_vs_continue:when not reply.ok and not monotonic_idx8begin.changed=>fail-or-stop{ok}-continue{serial}]
    ######################
    typing:
    @IEnvironment:
        #donot affect reply.ok ==>>:
        [gpreprocess :: (rgnr->env->xctx_view->ignore->ext_info8begin->(st, may ignore))]
        [gpostprocess6err :: (rgnr->env->xctx_view->ignore->st->ext_info8end->errmsg->errmsg)]
        [gpostprocess6ok :: (rgnr->env->xctx_view->ignore->st->ext_info8end->oresult->oresult)]
    ######################
    @RecognizeCall/mk_gi4IRecognizerLLoo__5solo_rgnr_transform_cases_:
        [spostprocess6err :: (errmsg->errmsg)]
        [spostprocess6ok :: (oresult->oresult)]
        #simple/special,general
        #   ==>> spostprocess6ok,gpostprocess6ok
    ######################

    #]]]'''#'''
#begin-class IRecognizerLLoo(ABC):
    #[:def__IRecognizerLLoo]:here
    __slots__ = ()
    @property
    @abstractmethod
    def _may_name4ref_(sf, /):
        '-> may (Hashable&&Weakable) # used in IEnvironment.name2rgnr_()'
    ##@property
    ##@abstractmethod
    ##def _may_name4gprepostprocess_(sf, /):
    ##    '-> may (Hashable&&Weakable) # used in IEnvironment.name2may_gpreprocess_()/.name2may_gpostprocess6err_()/.name2may_gpostprocess6ok_()'
    ##  _may_name4gpreprocess_
    ##  _may_name4gpostprocess_
    if 0:
        #now always allow _tail_recur_Call_ok_, but donot save spaces...
        pass
    @property
    @abstractmethod
    def _tail_recur_Call_ok_(sf, /):
        '-> bool # to allow ._mk_gi4recognize_ return RecognizeCall #it seems useless...'
    @property
    @abstractmethod
    def _bypass_check__assured_postcondition_unlocker_known_released_(sf, /):
        '-> bool # bypass check [IRecognizerLLoo._mk_gi4recognize_():postcondition:[[reply.ok==True]=>[unlocker.known_released==True]]]'

    @property
    @abstractmethod
    def _is_ctx_scope_(sf, /):
        '-> bool # enter/exit:restore old state #only for pseudo_func_body_stmt_flow not serial'
    @property
    @abstractmethod
    def _may_osymbolXseq_(sf, /):
        '-> may (symbol|[symbol]) #update gctx/ctx by assign oresult'
    @property
    @abstractmethod
    def _dsymbols_(sf, /):
        '-> {symbol} #update gctx/ctx by delete@enter'
    @property
    @abstractmethod
    def _isymbol2essential_(sf, /):
        '-> {symbol:essential/bool} #[essential input which affect reply.ok] # [non_essential input will be None when ignore:=True]'
    @property
    @abstractmethod
    def _isymbol_seq8extra_params_(sf, /):
        '-> [symbol] # [extracted as extra args for ._mk_gi4recognize_(...,*ex_args)]'
    @property
    @abstractmethod
    def _required_num_tokens6backward_(sf, /):
        '-> required_num_tokens6backward/uint#see:required_num_tokens6backward6env_()'
        #IRecognizerLLoo.required_num_tokens6backward
        #IInputStream.max_num_tokens6backward
    @abstractmethod
    def _validate_solo6env_(sf, env, /):
        '-> None|^ValidateError(rgnr, ...)'
    @abstractmethod
    def _cache_full_view_info6env_(sf, env, /):
        '-> None #sf.iter_persistent_descendants6env_(env) # [saved into env.external_cache]'
        '-> None # [saved into env.external_cache]'
    @abstractmethod
    def _mk_gi4recognize_(sf, env, xctx_view, unlocker, ignore:bool, istream, /, *ex_args:'from sf._isymbol_seq8extra_params_'):
        '-> GenIter{yield-RecognizeCall(IRecognizerLLoo, unlocker, ignore, istream);receive-child_rgnr.Reply;return-self.Reply(eresult, ext_info8end)} #[should not call IRecognizerLLoo._mk_gi4recognize_() directly since rgnr._is_ctx_scope_ (should call via 『yield Call(...)』)] #[postcondition:[[reply.ok==True]=>[unlocker.known_released==True]]]'
        #xxx:._tail_recur_Call_ok_ or forbod:tail_recur_Call
        #recognize_()::_tail_call() or forbod:tail_recur_Call
    @abstractmethod
    def _iter_persistent_children6env_(sf, env, /):
        '-> Iter IRecognizerLLoo # [must be finite][must be persistent obj, twice yield same obj][may saved into env.external_cache]'
    ######################
    #@abstractmethod
    def _get_the_base_rgnr_(sf, /):
        '-> IRecognizerLLoo # resolve RecognizerLLoo__light_wrap._get_the_cached_child6env_() as many as possible times # [must be persistent obj, twice yield same obj]'
        #RecognizerLLoo__light_wrap =>:
            #xxx:def _get_the_base_rgnr6env_(sf, env, /):
                #'-> IRecognizerLLoo # resolve RecognizerLLoo__light_wrap._get_the_cached_child6env_() as many as possible times # [must be persistent obj, twice yield same obj][may saved into env.external_cache]'
        return sf
    @property
    def _isymbols_(sf, /):
        '-> {symbol} #view gctx/ctx via isymbol only #donot consider children'
        return sf._isymbol2essential_.keys()
    #@abstractmethod
    def _validate_solo_(sf, /):
        '-> None|^ValidateError(rgnr, ...)'
        check_type_is(bool, sf._is_ctx_scope_)
        check_type_is(bool, sf._tail_recur_Call_ok_)
        check_type_is(bool, sf._bypass_check__assured_postcondition_unlocker_known_released_)
        check_may_weakable_name(sf._may_name4ref_)
        #######################
        check_type_le(Mapping, sf._isymbol2essential_)
        for isymbol in sf._isymbol2essential_.keys():
            check_weakable_name(isymbol)
        for essential in sf._isymbol2essential_.values():
            check_type_is(bool, essential)
        #######################
        check_type_is(tuple, sf._isymbol_seq8extra_params_)
        for isymbol in sf._isymbol_seq8extra_params_:
            check_weakable_name(isymbol)
            if not isymbol in sf._isymbol2essential_:raise KeyError(isymbol)
        #######################
        # [type(sf) is not ABC]
        f = type(sf)._mk_gi4recognize_
        check_type_is(Func, f)
        (infoss4input, tmay_return_annotation) = get_signature_of__py3_(f, follow_wrapped=True)
        (infos4idx_only, infos4idx_nm_both, tmay_info4varargs, infos4nm_only, tmay_info4varkwds) = infoss4input
        assert not infos4idx_nm_both
        assert not tmay_info4varargs
        assert not infos4nm_only
        assert not tmay_info4varkwds
        infos4idx_only
        params = [name for (name, tmay_annotation, tmay_default) in infos4idx_only]
        #def _mk_gi4recognize_(sf, env, xctx_view, unlocker, ignore:bool, istream, /, *ex_args:'from sf._isymbol_seq8extra_params_'):
        assert len(params) == 6+len(sf._isymbol_seq8extra_params_)
        #######################

    def cache_full_view_info6env_(sf, env, /):
        '-> first_time/bool # [saved into env.external_cache]'
        sf.validate_descendants6env_(env)
            #should before cache "first_time"
        (is_new, _) = env.getset_external_cache4rgnr_func(sf, _4mixins, 2)
        first_time = is_new
        if first_time:
            sf._cache_full_view_info6env_(env)
            for child in sf._iter_persistent_children6env_(env):
                child.cache_full_view_info6env_(env)
                    #not:bug:since "first_time" guard
            sf.required_num_tokens6backward6env_(env)
        return first_time
    def iter_persistent_descendants6env_(sf, env, /):
        '-> descendants/(Iter IRecognizerLLoo) # [must be finite][must be persistent obj, twice yield same obj][may saved into env.external_cache]'
        #.if 0b0000:
        #.    from inspect import currentframe, getouterframes, stack
        #.    #print_err(getouterframes(currentframe()))
        #.    stk = stack()
        #.    print_err([x.function for x in stk[:20]])
        #.    print_err(len(stk))
        #.    del stk
        #.    print_err('iter_persistent_descendants6env_')
        #.    input('iter_persistent_descendants6env_')
        id2rgnr = {}
        ls = []
        def put(rgnr, /):
            if id(rgnr) in id2rgnr:
                return
            id2rgnr[id(rgnr)] = rgnr
            ls.append(rgnr)
        put(sf)
        while ls:
            rgnr = ls.pop()
            wref_(rgnr)
                #check weakable
            yield rgnr
            #if 0b0001:print_err(rgnr)
            #if 0b0001:print_err(id(rgnr))
            it = rgnr._iter_persistent_children6env_(env)
            for _ in map(put, it):pass
        ls = [*map(wref_, id2rgnr.values())]
        del id2rgnr
        if any(w() is None for w in ls):raise Exception('not persistent descendant rgnr')
    def required_num_tokens6backward6env_(sf, env, /):
        '-> uint#see:_required_num_tokens6backward_()'
        return env.getset_external_cache4rgnr_func(sf, _4back_cache, 1)
    def collect_namess6env_(sf, env, /, *, bypass_cache=False):
        '-> (nm2rgnr, nms4ref, nms6ref)/({nm:rgnr}, {nm}, {nm}) #[nm2rgnr.keys() == nms4ref]'
        # '-> (nm2rgnr, nms4ref, nms6ref, nms4pre, nms4post)/({nm:rgnr}, {nm}, {nm}, {nm}, {nm}) #[nm2rgnr.keys() == nms4ref]'
        if bypass_cache:
            #at first, findout all names needed to be registered
            #   or:using:collect_namess5rgnrs_
            return _4nmss(sf, env)
        return env.getset_external_cache4rgnr_func(sf, _4nmss, 1)
    def view_id2rgnr8all_descendants6env_(sf, env, /):
        '-> id2rgnr/view-WeakValueDictionary{id:rgnr}'
        return env.getset_external_cache4rgnr_func(sf, _4id2rgnr, 1)
    def validate_solo6env_(sf, env, /):
        '-> None|^ValidateError(rgnr, ...) # [saved into env.external_cache]'
        m = env.getset_external_cache4rgnr_func(sf, _4check_solo, 1)
        if not m is None:
            raise m
    def validate_descendants6env_(sf, env, /):
        '-> None|^ValidateError(rgnr, ...) # [saved into env.external_cache]'
        m = env.getset_external_cache4rgnr_func(sf, _4check_all, 1)
        if not m is None:
            raise m
#end-class IRecognizerLLoo:
def _4check_solo(rgnr, env, /):
    '-> (None|^ValidateError(rgnr, ...))'
    rgnr._validate_solo_()
    rgnr._validate_solo6env_(env)
    return
    '-> (None|ValidateError(rgnr, ...)) #not raise ValidateError'
    try:
        rgnr._validate_solo_()
        rgnr._validate_solo6env_(env)
    except ValidateError as e:
        if not e.args or e.args[0] is not rgnr:
            e = ValidateError(rgnr, e)
        return e
    except Exception as e:
        #TypeError,ValueError,KeyError...
        e = ValidateError(rgnr, e)
        return e
def _4check_all(rgnr, env, /):
    '-> (None|^ValidateError(rgnr, ...))'
    for rgnr in rgnr.iter_persistent_descendants6env_(env):
        rgnr.validate_solo6env_(env)
    return
    '-> (None|ValidateError(rgnr, ...)) #not raise ValidateError'
    try:
        for rgnr in rgnr.iter_persistent_descendants6env_(env):
            rgnr.validate_solo6env_(env)
    except ValidateError as e:
        return e
def _4id2rgnr(rgnr, env, /):
    return MapView(WvalD((id(descendant), descendant) for descendant in rgnr.iter_persistent_descendants6env_(env)))
def _4back_cache(rgnr, env, /):
    return max(descendant._required_num_tokens6backward_ for descendant in rgnr.iter_persistent_descendants6env_(env))
    #bug:
    n = rgnr._required_num_tokens6backward_
    m = max((child.required_num_tokens6backward6env_(env) for child in rgnr._iter_persistent_children6env_(env)), default=0)
        #bug:since not cached yet
    return max(n, m)
def _4nmss(rgnr, env, /):
    return collect_namess5rgnrs_(rgnr.iter_persistent_descendants6env_(env))
def collect_namess5rgnrs_(rgnrs, /):
    '-> (nm2rgnr, nms4ref, nms6ref)/({nm:rgnr}, {nm}, {nm}) #[nm2rgnr.keys() == nms4ref]'
    #'-> (nm2rgnr, nms4ref, nms6ref, nms4pre, nms4post)/({nm:rgnr}, {nm}, {nm}, {nm}, {nm}) #[nm2rgnr.keys() == nms4ref]'
    #(nms4ref, nms6ref, nms4pre, nms4post) = set(), set(), set(), set()
    (nms4ref, nms6ref) = set(), set()
    nm2rgnr = {}
    for rgnr in rgnrs:
        if type(rgnr) is RecognizerLLoo__ref:
            nms6ref.add(rgnr.name6ref)
        ...
        #if type(rgnr) is RecognizerLLoo__named
        if not None is (nm4ref := rgnr._may_name4ref_):
            if not (rgnr is (__:=nm2rgnr.setdefault(nm4ref, rgnr))):raise Exception('name duplicated:', nm4ref, __, rgnr)
        nms4ref.add(rgnr._may_name4ref_)
        #nms4pre.add(rgnr._may_name4gpreprocess_)
        #nms4post.add(rgnr._may_name4gpostprocess_)
    nms4ref.discard(None)
    #nms4pre.discard(None)
    #nms4post.discard(None)
    assert None not in nms6ref
    assert nm2rgnr.keys() == nms4ref

    #(nms4ref, nms6ref, nms4pre, nms4post) = map(mk_frozenset, (nms4ref, nms6ref, nms4pre, nms4post))
    (nms4ref, nms6ref) = map(mk_frozenset, (nms4ref, nms6ref))
    nm2rgnr = MapView(nm2rgnr)
    return (nm2rgnr, nms4ref, nms6ref)
    #return (nm2rgnr, nms4ref, nms6ref, nms4pre, nms4post)

class IRecognizerLLoo__default_mixins(IRecognizerLLoo):
    __slots__ = ()
    #@override
    _tail_recur_Call_ok_ = False
    #@override
    _bypass_check__assured_postcondition_unlocker_known_released_ = False
    #@override
    _is_ctx_scope_ = False
    #@override
    _may_osymbolXseq_ = None
    #@override
    _dsymbols_ = null_frozenset
    #@override
    _isymbol2essential_ = null_mapping_view
    #@override
    _isymbol_seq8extra_params_ = null_tuple
    #@override
    _required_num_tokens6backward_ = 0
    #@override
    _may_name4ref_ = None
    @override
    def _validate_solo6env_(sf, env, /):
        '-> None|^ValidateError(rgnr, ...)'
        return None
    @override
    def _cache_full_view_info6env_(sf, env, /):
        '-> None #sf.iter_persistent_descendants6env_(env) # [saved into env.external_cache]'
        return None
def _4mixins(rgnr, env, /):
    'persistent_func{IRecognizerLLoo__default_mixins.cache_full_view_info6env_}'
    return ...

def explain_may_emay_weakable_name(nm, may_emay_nm, /):
    if may_emay_nm is ...:
        may_nm = nm
    else:
        may_nm = may_emay_nm
    return may_nm
def check_may_weakable_name(may_nm, /):
    if may_nm is None:
        return
    check_weakable_name(nm:=may_nm)
def check_may_emay_weakable_name(may_emay_nm, /):
    if may_emay_nm is None or may_emay_nm is ...:
        return
    check_weakable_name(nm:=may_emay_nm)
def check_weakable_name(nm, /):
    wref_(nm)
        #check weakable
class WeakableSymbol5name:
    'weakable#check_weakable_name()'
    _prefix_ = ''
    def __init__(sf, nm, /):
        sf._nm = nm
    def __repr__(sf, /):
        return sf._prefix_ + sf._nm
check_weakable_name(WeakableSymbol5name('nm'))
class Symbol4IRecognizerLLoo(WeakableSymbol5name):
    'can be used with RecognizerLLoo__named,RecognizerLLoo__ref'
    _prefix_ = 'nm4rgnr_.'
check_weakable_name(Symbol4IRecognizerLLoo('nm'))
class RecognizerLLoo__named(IRecognizerLLoo__default_mixins, _Base4repr):
    ___no_slots_ok___ = True
    def __init__(sf, nm4ref, rgnr, /):
        check_weakable_name(nm4ref)
        check_type_le(IRecognizerLLoo, rgnr)
        sf._nm4ref = nm4ref
        sf._r = rgnr
        #sf._args4repr = (nm4ref, rgnr)
        sf._reset4repr((nm4ref, rgnr))
    @property
    @override
    def _may_name4ref_(sf, /):
        '-> may (Hashable&&Weakable) # used in IEnvironment.name2rgnr_()'
        return sf._nm4ref
    @override
    def _mk_gi4recognize_(sf, env, xctx_view, unlocker, ignore:bool, istream, /):
        rgnr = sf._r
        #bug:return rgnr._mk_gi4recognize_(env, xctx_view, unlocker, ignore, istream)
        #   since rgnr._is_ctx_scope_
        reply = yield mk_Call_(rgnr, unlocker, ignore, istream)
        return reply
    @override
    def _iter_persistent_children6env_(sf, env, /):
        '-> Iter IRecognizerLLoo # [must be finite][must be persistent obj, twice yield same obj][may saved into env.external_cache]'
        rgnr = sf._r
        yield rgnr
check_non_ABC(RecognizerLLoo__named)

class RecognizerLLoo__ref(IRecognizerLLoo__default_mixins, _Base4repr):
    ___no_slots_ok___ = True
    ##def __init__(sf, nm6ref, may_emay_nm4pre, may_emay_nm4post, /):
    ##    check_weakable_name(nm6ref)
    ##    check_may_emay_weakable_name(may_emay_nm4pre)
    ##    check_may_emay_weakable_name(may_emay_nm4post)
    ##    sf._nm6ref = nm6ref
    ##    sf._mpre = explain_may_emay_weakable_name(nm6ref, may_emay_nm4pre)
    ##    sf._mgpost = explain_may_emay_weakable_name(nm6ref, may_emay_nm4post)
    ##    #sf._args4repr = (nm6ref, may_emay_nm4pre, may_emay_nm4post)
    ##    sf._reset4repr((nm6ref, may_emay_nm4pre, may_emay_nm4post))
    def __init__(sf, nm6ref, /):
        check_weakable_name(nm6ref)
        sf._nm6ref = nm6ref
        #sf._args4repr = (nm6ref,)
        sf._reset4repr((nm6ref,))
    #@override
    _may_name4ref_ = None
        #see:RecognizerLLoo__named
    @property
    def name6ref(sf, /):
        '-> (Hashable&&Weakable) # used in IEnvironment.name2rgnr_()'
        return sf._nm6ref
    @override
    def _mk_gi4recognize_(sf, env, xctx_view, unlocker, ignore:bool, istream, /):
        rgnr = env.name2rgnr_(sf._nm6ref)
        #bug:return rgnr._mk_gi4recognize_(env, xctx_view, unlocker, ignore, istream)
        #   since rgnr._is_ctx_scope_
        reply = yield mk_Call_(rgnr, unlocker, ignore, istream)
        return reply
    @override
    def _iter_persistent_children6env_(sf, env, /):
        '-> Iter IRecognizerLLoo # [must be finite][must be persistent obj, twice yield same obj][may saved into env.external_cache]'
        rgnr = env.name2rgnr_(sf._nm6ref)
        yield rgnr
check_non_ABC(RecognizerLLoo__ref)


class IHalfMap(ABC):
    __slots__ = ()
    def __iter__(sf, /):
        raise TypeError
    def __bool__(sf, /):
        raise TypeError
    def __len__(sf, /):
        raise TypeError
        if not sf._isz is None:
            return sf._isz
        sf._isz = len(sf.keys())
        return len(sf)
    def keys(sf, /):
        raise TypeError
    def values(sf, /):
        raise TypeError
    def items(sf, /):
        raise TypeError

class WeakKeyHalfMap(IHalfMap):
    'IHalfMap<WeakKeyDictionary> #see:IEnvironment.external_cache'
    ___no_slots_ok___ = True
    def __init__(sf, d=None, /):
        if d is None:
            d = WkeyD()
        elif type(d) is not WkeyD:
            d = WkeyD(d)
        check_type_is(WkeyD, d)
        sf._d = d
    def __delitem__(sf, sym, /):
        d = sf._d
        del d[sym]
    def __setitem__(sf, sym, v, /):
        d = sf._d
        d[sym] = v
    def __getitem__(sf, sym, /):
        d = sf._d
        return d[sym]
    def __contains__(sf, sym, /):
        d = sf._d
        return sym in d

class Symbol4GlobalVarable(WeakableSymbol5name):
    'global-symbol #can be used with XContext,ContextView'
    _local_vs_global_ = True
    _prefix_ = 'nm4gvar_.'
class Symbol4LocalVarable(WeakableSymbol5name):
    'local-symbol #can be used with XContext,ContextView'
    _local_vs_global_ = False
    _prefix_ = 'nm4lvar_.'
class XContext(IHalfMap):
    'xctx#writeonly'
    ___no_slots_ok___ = True
    def __init__(sf, gctx, ctx, /):
        sf._xs = (gctx, ctx)
    def __bool__(sf, /):
        raise TypeError
    def __len__(sf, /):
        raise TypeError
    def __delitem__(sf, sym, /):
        (gctx, ctx) = sf._xs
        xctx = gctx if sym._local_vs_global_ else ctx
        del xctx[sym]

    def __setitem__(sf, sym, v, /):
        (gctx, ctx) = sf._xs
        xctx = gctx if sym._local_vs_global_ else ctx
        xctx[sym] = v
    def del_items(sf, dsymbols, /):
        for sym in dsymbols:
            del sf[sym]
    def set_items(sf, may_osymbolXseq, oresult, /):
        if may_osymbolXseq is None:
            return
        osymbolXseq = may_osymbolXseq
        if not hasattr(osymbolXseq, '__len__'):
            osymbol = osymbolXseq
            sf[osymbol] = oresult
            return
        osymbol_seq = osymbolXseq
        if not len(osymbol_seq) == len(oresult):raise TypeError
        for sym, v in zip(osymbol_seq, oresult):
            sf[sym] = v
class ContextView(IHalfMap):
    'xctx_view = (gctx_view+++ctx_view)#readonly'
    ___no_slots_ok___ = True
    def __init__(sf, isymbols, gctx, ctx, /):
        sf._xs = (isymbols, gctx, ctx)
            #sf._xs = (SetView(isymbols), MapView(gctx), MapView(ctx))
        if 0:
            sf._isz = None
            sf._ks = None
    #def keys(sf, /):
    #    if not sf._ks is None:
    #        return sf._ks
    #    (isymbols, gctx, ctx) = sf._xs
    #    #xctx = gctx if sym._local_vs_global_ else ctx
    #    ks = {sym for sym in isymbols if sym in (gctx if sym._local_vs_global_ else ctx)}
    #    ks = mk_frozenset(ks)
    #    sf._ks = ks
    #    return sf.keys()
    def __contains__(sf, sym, /):
        (isymbols, gctx, ctx) = sf._xs
        return sym in isymbols and sym in (xctx := gctx if sym._local_vs_global_ else ctx)
    def __getitem__(sf, sym, /):
        (isymbols, gctx, ctx) = sf._xs
        if sym in isymbols:
            xctx = gctx if sym._local_vs_global_ else ctx
            return xctx[sym]
        raise KeyError(sym)

#[:def__IEnvironment]:here
class IEnvironment(ABC):
    'env'
    __slots__ = ()
    @abstractmethod
    def param2setting_(sf, nm, /):
        'k -> v|^LookupError'
    @abstractmethod
    def name2rgnr_(sf, nm, /):
        'k -> IRecognizerLLoo|^LookupError #using:IRecognizerLLoo._may_name4ref_'
    @abstractmethod
    def name2may_gpreprocess_(sf, nm, /):
        'k -> may gpreprocess/(rgnr->env->xctx_view->ignore->ext_info8begin->(st, may ignore)) #using:IRecognizerLLoo._may_name4ref_ #donot affect reply.ok'
        # 'k -> may gpreprocess/(rgnr->env->xctx_view->ignore->ext_info8end->may ignore) #using:IRecognizerLLoo._may_name4gpreprocess_ #donot affect reply.ok'
    @abstractmethod
    def name2may_gpostprocess6err_(sf, nm, /):
        'k -> may gpostprocess6err/(rgnr->env->xctx_view->ignore->st->ext_info8end->errmsg->errmsg) #using:IRecognizerLLoo._may_name4ref_ #donot affect reply.ok'
        # 'k -> may gpostprocess6err/(rgnr->env->xctx_view->ignore->ext_info8end->errmsg->errmsg) #using:IRecognizerLLoo._may_name4gpostprocess_ #donot affect reply.ok'
    @abstractmethod
    def name2may_gpostprocess6ok_(sf, nm, /):
        'k -> may gpostprocess6ok/(rgnr->env->xctx_view->ignore->st->ext_info8end->oresult->oresult) #using:IRecognizerLLoo._may_name4ref_ #donot affect reply.ok'
        # 'k -> may gpostprocess6ok/(rgnr->env->xctx_view->ignore->ext_info8end->oresult->oresult) #using:IRecognizerLLoo._may_name4gpostprocess_ #donot affect reply.ok'
    @property
    @abstractmethod
    def external_cache(sf, /):
        '-> mutable weak_key_mapping without len/keys()/...#WeakKeyHalfMap/IHalfMap<WeakKeyDictionary> #to save rgnr persistent info(full_view_info<env,rgnr.descendants>) #see:IRecognizerLLoo.cache_full_view_info6env_'
    def getset_external_cache4rgnr_func(sf, rgnr, rgnr_env2result, get_vs_set_vs_set_ex, /):
        'IRecognizerLLoo -> (IRecognizerLLoo -> IEnvironment -> r)/persistent-FunctionType -> (0|1|2) -> ((r|^KeyError)|r|(is_new,r))'
        #check_type_le(IRecognizerLLoo, rgnr)
        return getset_external_cache4func(get_vs_set_vs_set_ex, rgnr_env2result, rgnr, sf)
    def getset_external_cache4rgnr_method(sf, env2result, get_vs_set_vs_set_ex, /):
        '(IEnvironment -> r)/MethodType{IRecognizerLLoo, persistent-FunctionType} -> (0|1|2) -> ((r|^KeyError)|r|(is_new,r))'
        check_type_is(Meth, env2result)
        rgnr = env2result.__self__
        rgnr_env2result = env2result.__func__
        return sf.getset_external_cache4rgnr_func(rgnr, rgnr_env2result, get_vs_set_vs_set_ex)
def getset_external_cache4method(get_vs_set_vs_set_ex, mf, /, *weakable_args):
    'precondition:[mf/MethodType == (f/FunctionType + weakable_selfs)] => ' \
        '(0|1|2) -> mf/MethodType/((*weakable_args)->r) -> (*weakable_args) -> ((r|^KeyError)|r|(is_new,r))'
    check_int_ge_lt(0, 3, case:=get_vs_set_vs_set_ex)
    args = []
    while type(mf) is Meth:
        sf = mf.__self__
        wref_(sf)
            #check weakable
        args.append(sf)
        mf = mf.__func__
    f = mf
    check_type_is(Func, f)
    args.reverse()
    return getset_external_cache4func(case, f, *args, *weakable_args)

def getset_external_cache4func(get_vs_set_vs_set_ex, f, /, *weakable_args, __depth=0):
    '(0|1|2) -> f/FunctionType/((*weakable_args)->r) -> (*weakable_args) -> ((r|^KeyError)|r|(is_new,r))'
    if not 0 <= __depth < 2:raise Exception(getset_external_cache4func, get_vs_set_vs_set_ex, f, *weakable_args)
    check_int_ge_lt(0, 3, case:=get_vs_set_vs_set_ex)
    check_type_is(Func, f)
    #xxx:if not weakable_args:raise TypeError
    d = vars(f)
    k = getset_external_cache4func
    if not k in d:
        check_type_is(Func, f)
        d[k] = WkeyD()
    wd0 = wd = d[k]
    check_type_is(WkeyD, wd)
    it = map(wref_, weakable_args)
    #bug:it = iter([*it])
    #   fail:wref_(wref_(...))
    [*it]
        #check weakable
    it = iter(weakable_args)
    if case == 0:
        for w in it:
            wd = wd[w]
                # ^KeyError
        else:
            r = wd
            return r
    try:
        for w in it:
            wd = wd[w]
                # ^KeyError
    except KeyError:
        pass
    else:
        r = wd
        if case == 1:
            return r
        if case == 2:
            return (is_new:=False, r)
        raise 000-case
    wd, w, it
        # !! KeyError => [w existed]
    # [w may be last]
    # [wd is not r]
    for _w in it:
        # [w is not last]
        if 0:
            #why? bug:『wd = wd[w] = WkeyD()』
            wd = wd[w] = WkeyD()
        else:
            tmp = WkeyD()
            wd[w] = tmp
            wd = tmp
            del tmp
        #if 0b0001:print_err({**wd0})
        # [wd is not r]
        w = _w
        # [w may be last]
        # [wd is not r]
    # [w is last]
    # [wd is not r]
    wd, w
    try:
        r = wd[w]
    except KeyError:
        is_new = True
    else:
        is_new = False
        if case == 1:
            return r
        if case == 2:
            return (is_new, r)
        raise 000-case
    r = wd[w] = f(*weakable_args)
    #if 0b0001:print_err({**wd0})
    rx = getset_external_cache4func(case, f, *weakable_args, __depth=__depth+1)
    if case == 1:
        assert rx is r
        return rx
    if case == 2:
        (_is_new, _r) = rx
        assert not _is_new
        assert _r is r
        return (is_new, r)
    raise 000-case
#end-class IEnvironment(ABC):
class Environment(IEnvironment):
    ___no_slots_ok___ = True
    def __init__(sf, param2setting, name2rgnr, name2may_gpreprocess, name2may_gpostprocess6err, name2may_gpostprocess6ok, /):
        #may_external_cache = None
        #external_cache = ifNone(may_external_cache, WeakKeyHalfMap())
        external_cache = WeakKeyHalfMap()

        sf._p2v = param2setting
        sf._nm2r = name2rgnr
        sf._nm2mpre = name2may_gpreprocess
        sf._nm2mpost6err = name2may_gpostprocess6err
        sf._nm2mpost6ok = name2may_gpostprocess6ok
        sf._w2c = external_cache
    @override
    def param2setting_(sf, nm, /):
        'k -> v|^LookupError'
        return sf._p2v[nm]
    @override
    def name2rgnr_(sf, nm, /):
        'k -> IRecognizerLLoo|^LookupError #using:IRecognizerLLoo._may_name4ref_'
        return sf._nm2r[nm]
    @override
    def name2may_gpreprocess_(sf, nm, /):
        return sf._nm2mpre.get(nm)
    @override
    def name2may_gpostprocess6err_(sf, nm, /):
        return sf._nm2mpost6err.get(nm)
    @override
    def name2may_gpostprocess6ok_(sf, nm, /):
        return sf._nm2mpost6ok.get(nm)
    @property
    @override
    def external_cache(sf, /):
        return sf._w2c
#end-class Environment(IEnvironment):

r'''[[[
intent:
    mkrs.gprepostprocess_(rgnr, may gpreprocess, may gpostprocess6err, may gpostprocess6ok)

usage:
    gpreprocess = mk_gpreprocess__5constant_(st, may_ignore)
    gpostprocess6err = mk_gpostprocess6err__5spost_(spostprocess6err)
    gpostprocess6ok = mk_gpostprocess6ok__5spost_(spostprocess6ok)

usage:
    gpreprocess = mk_gpreprocess__5lazy_st_(lazy_st, may_ignore)
    gpostprocess6err = mk_gpostprocess6err__5spost_after_tag_st_(spostprocess6err_after_tag_st)
    gpostprocess6ok = mk_gpostprocess6ok__5spost_after_tag_st_(spostprocess6ok_after_tag_st)


#]]]'''#'''
def mk_gpreprocess__5constant_(st, may_ignore, /):
    def gpreprocess(rgnr, env, xctx_view, ignore, ext_info8begin, /):
        '-> (st, may ignore)'
        return (st, may_ignore)
    return gpreprocess

def mk_gpostprocess6err__5spost_(spostprocess6err, /):
    def gpostprocess6err(rgnr, env, xctx_view, ignore, st, ext_info8end, errmsg, /):
        '-> errmsg'
        return spostprocess6err(errmsg)
    return gpostprocess6err

def mk_gpostprocess6ok__5spost_(spostprocess6ok, /):
    def gpostprocess6ok(rgnr, env, xctx_view, ignore, st, ext_info8end, oresult, /):
        '-> oresult'
        return spostprocess6ok(oresult)
    return gpostprocess6ok


def mk_gpreprocess__5lazy_st_(lazy_st, may_ignore, /):
    def gpreprocess(rgnr, env, xctx_view, ignore, ext_info8begin, /):
        '-> (st, may ignore)'
        return (st:=lazy_st(), may_ignore)
    return gpreprocess

def mk_gpostprocess6err__5spost_after_tag_st_(spostprocess6err_after_tag_st, /):
    def gpostprocess6err(rgnr, env, xctx_view, ignore, st, ext_info8end, errmsg, /):
        '-> errmsg'
        return spostprocess6err_after_tag_st((st, errmsg))
    return gpostprocess6err

def mk_gpostprocess6ok__5spost_after_tag_st_(spostprocess6ok_after_tag_st, /):
    def gpostprocess6ok(rgnr, env, xctx_view, ignore, st, ext_info8end, oresult, /):
        '-> oresult'
        return spostprocess6ok_after_tag_st((st, oresult))
    return gpostprocess6ok






_decorator44rngr = Decorator4recur5yield(Executor4recur5yield__dispatch_by_dict(None, False, True, {RecognizeCall:'gi5rcall_'}))
    # [_allow__gi2gi_:=True] ==>> # donot use 『yield from』
    #
    #def Executor4recur5yield__dispatch_by_dict.__init__(sf, may_emplace_stack_ops, using_tail_recur_gi_protocol, _allow__gi2gi_, may_type2attr_or_child_gi_protocol, /):
    #
@_decorator44rngr
def recognize_(main_rgnr, env, gctx, istream, /, *, ignore=False):
    'IRecognizerLLoo -> env/IEnvironment -> gctx/mapping -> istream/IInputStream -> Reply'#@wrapper
    'IRecognizerLLoo -> env/IEnvironment -> gctx/mapping -> istream/IInputStream -> (st, Call)'#@wrapped
    (st, main_rcall) = _recognize(main_rgnr, env, gctx, istream, ignore)
    return (st, main_rcall)
def _recognize(_0main_rgnr, _0env, _0gctx, _0istream, _0ignore, /):
    '-> (st, main_rcall)'
    ######################
    _0ctx = DynamicStackedMapping({})
    _0xctx = XContext(_0gctx, _0ctx)
    _0id2rgnr = _0main_rgnr.view_id2rgnr8all_descendants6env_(_0env)
    ######################
    st = _State4recognize(_0env, _0gctx, _0ctx, _0xctx, _0id2rgnr)
    ######################
    _0main_rgnr.cache_full_view_info6env_(_0env)
    if not _0main_rgnr.required_num_tokens6backward6env_(_0env) <= _0istream.max_num_tokens6backward:raise Exception('istream.max_num_tokens6backward too small:', _0main_rgnr.required_num_tokens6backward6env_(_0env), _0istream.max_num_tokens6backward)
    main_rcall = mk_Call_(_0main_rgnr, dummy_unlocker, _0ignore, _0istream)
    ######################
    return (st, main_rcall)
    ######################
def apply_may_gpreprocess_(mpre_, rgnr, _0env, xctx_view, ignore, istream, /):
    st = None
    if not mpre_ is None:
        pre_ = mpre_
        # [gpreprocess :: (rgnr->env->xctx_view->ignore->ext_info8begin->(st, may ignore))]
        (st, mignore) = pre_(rgnr, _0env, xctx_view, ignore, istream.tell_ext_info())
        if not mignore is None:
            ignore = mignore
            check_type_is(bool, ignore)
    ignore
    return (st, ignore)
    #(st, ignore) = apply_may_gpreprocess_(mpre_, rgnr, _0env, xctx_view, ignore, istream)
def apply_may_gpostprocess_(mgpost6err_, mgpost6ok_, reply, rgnr, _0env, xctx_view, ignore, st, /):
    if reply.ok:
        if not mgpost6ok_ is None:
            post6ok_ = mgpost6ok_
            # [gpostprocess6ok :: (rgnr->env->xctx_view->ignore->st->ext_info8end->oresult->oresult)]
            oresult = post6ok_(rgnr, _0env, xctx_view, ignore, st, reply.ext_info8end, reply.oresult)
            if not oresult is reply.oresult:
                reply = reply.ireplace(eresult=mk_Right(oresult))
    else:
        if not mgpost6err_ is None:
            post6err_ = mgpost6err_
            # [gpostprocess6err :: (rgnr->env->xctx_view->ignore->st->ext_info8end->errmsg->errmsg)]
            errmsg = post6err_(rgnr, _0env, xctx_view, ignore, st, reply.ext_info8end, reply.errmsg)
            if not errmsg is reply.errmsg:
                reply = reply.ireplace(eresult=mk_Left(errmsg))
    check_type_is(Reply, reply)
    return reply
    #reply = apply_may_gpostprocess_(mgpost6err_, mgpost6ok_, reply, rgnr, _0env, xctx_view, ignore, st)
class _State4recognize:
    def __init__(sf, _0env, _0gctx, _0ctx, _0xctx, _0id2rgnr, /):
        sf._args = (_0env, _0gctx, _0ctx, _0xctx, _0id2rgnr)
        (sf._0env, sf._0gctx, sf._0ctx, sf._0xctx, sf._0id2rgnr) = (_0env, _0gctx, _0ctx, _0xctx, _0id2rgnr)
    def gi5rcall_(sf, rcall, /):
        'Call -> GI'
        #############
        _0id2rgnr = sf._0id2rgnr
        #############
        check_type_is(Call, rcall)
        (rgnr, unlocker, ignore, istream, exargs4lwrap) = rcall
            #RecognizeCall
        check_type_is(bool, ignore)
        if unlocker.known_released:
            unlocker = dummy_unlocker
        if not id(rgnr._get_the_base_rgnr_()) in _0id2rgnr:raise Exception('not persistent rgnr from IRecognizerLLoo.iter_persistent_descendants6env_', rgnr)
        if exargs4lwrap:
            rgnr = light_wrap_rgnr_(rgnr, *exargs4lwrap)
        gi = sf._call(rgnr, unlocker, ignore, istream)
        return gi
    def _call(sf, rgnr, unlocker, ignore, istream, /):
        '-> gi<return-Reply>'
        #############
        _0gctx = sf._0gctx
        _0ctx = sf._0ctx
        _0xctx = sf._0xctx
        _0env = sf._0env
        #############
        dsymbols = rgnr._dsymbols_
        isymbols = rgnr._isymbols_
        may_osymbolXseq = rgnr._may_osymbolXseq_
        #mnmpre = rgnr._may_name4gpreprocess_
        #mnmgpost = rgnr._may_name4gpostprocess_
        if not ignore:
            mnmpre = mnmgpost = rgnr._may_name4ref_
            mpre_ = None if mnmpre is None else _0env.name2may_gpreprocess_(mnmpre)
            mgpost6err_ = None if mnmgpost is None else _0env.name2may_gpostprocess6err_(mnmgpost)
            mgpost6ok_ = None if mnmgpost is None else _0env.name2may_gpostprocess6ok_(mnmgpost)

        _0xctx.del_items(dsymbols)
            ######################
            # [delete before enter ctx scope]
            ######################
        xctx_view = ContextView(isymbols, _0gctx, _0ctx)
        b_scope = rgnr._is_ctx_scope_
        p = _0ctx.env_tell() if b_scope else None

        if not ignore:
            (st, ignore) = apply_may_gpreprocess_(mpre_, rgnr, _0env, xctx_view, ignore, istream)
        #######
        if ignore:
            st = None
            mgpost6err_ = None
            mgpost6ok_ = None
        ex_args = [xctx_view[isymbol] for isymbol in rgnr._isymbol_seq8extra_params_]
        gi = rgnr._mk_gi4recognize_(_0env, xctx_view, unlocker, ignore, istream, *ex_args)
                # _tail_call() or forbod:tail_recur_Call
        assert hasattr(gi, 'send'), rgnr
        del ex_args


        bypass = unlocker.known_released or rgnr._bypass_check__assured_postcondition_unlocker_known_released_
        if 0:
            #since now validate 『unlocker.known_released』
            pass
        if (not b_scope and may_osymbolXseq is None and mgpost6err_ is None is mgpost6ok_ and not rgnr._tail_recur_Call_ok_ and bypass):
            #forbod:tail_recur_Call
            #   <<== not rgnr._tail_recur_Call_ok_
            return gi
        return sf._tail_call(gi, b_scope, p, may_osymbolXseq, mgpost6err_, mgpost6ok_, rgnr, xctx_view, st, ignore, unlocker)
    def _tail_call(sf, gi, b_scope, p, may_osymbolXseq, mgpost6err_, mgpost6ok_, rgnr, xctx_view, st, ignore, unlocker, /):
        '-> gi<return-Reply>'
        #############
        _0ctx = sf._0ctx
        _0xctx = sf._0xctx
        _0env = sf._0env
        #############
        reply = yield gi
            # donot use 『yield from』
        if type(reply) is Call:
            #tail_recur_Call ok
            #_tail_recur_Call_ok_
            rcall = reply
            reply = yield rcall
        check_type_is(Reply, reply)
        if not (not reply.ok or unlocker.known_released):raise Exception('fail:[IRecognizerLLoo._mk_gi4recognize_():postcondition:[[reply.ok==True]=>[unlocker.known_released==True]]]', rgnr)
        if b_scope:
            _0ctx.env_pop_until(p)
        ######################
        # [exit ctx scope before assignment]
        ######################
        if reply.ok:
            _0xctx.set_items(may_osymbolXseq, reply.oresult)
            ######################
            # [assignment before gpostprocess6ok] <<== [gpostprocess6ok is external-registered, may change len(oresult)]
            ######################
        reply = apply_may_gpostprocess_(mgpost6err_, mgpost6ok_, reply, rgnr, _0env, xctx_view, ignore, st)
        return reply

        ######################
#end-class _State4recognize:
_sym4echo= get_symbol8high_freq_sconfigpack_(forbid_xxx_protected_ok, '_echo_')
def light_wrap_rgnr_(rgnr, /, *exargs4lwrap):
    'IRecognizerLLoo -> bool -> exargs4lwrap<Call>/[nm4info_ex4mk_gi] -> IRecognizerLLoo'
        #'IRecognizerLLoo -> bool -> exargs4lwrap<Call>/[(nm|info_ex4mk_gi)] -> IRecognizerLLoo'
    for exarg in exargs4lwrap:
        if type(exarg) is str:
            nm = exarg
            if nm == '_echo_':
                continue
            info_ex4mk_gi = get_info_ex4high_freq_sconfigpack_(forbid_xxx_protected_ok, nm)
        else:
            raise Exception('should use nm4info_ex4mk_gi as exarg, since ++to_invert_ok_err[#which only be used by not_followed_by#]', name_set4high_freq_sconfigpack, exarg)
            info_ex4mk_gi = exarg
        info_ex4mk_gi
        (symbol8sexconfigpack, may_info4mk_gi) = info_ex4mk_gi
        check_weakable_name(symbol8sexconfigpack)
        if may_info4mk_gi == default_info4mk_gi:
            may_info4mk_gi = None
        if symbol8sexconfigpack == _sym4echo and may_info4mk_gi is None:
            continue
        rgnr = RecognizerLLoo__light_wrap(rgnr, symbol8sexconfigpack, may_info4mk_gi)
    rgnr
    return rgnr


#:.+2,.+16s/^\(\w\+\)$/def \1_(rgnr, \/):\r    return light_wrap_rgnr_(rgnr, '\1')
#_echo_
def not_followed_by_(rgnr, /):
    return light_wrap_rgnr_(rgnr, 'not_followed_by')
def followed_by_(rgnr, /):
    return light_wrap_rgnr_(rgnr, 'followed_by')
def lift__forgivable_(rgnr, /):
    return light_wrap_rgnr_(rgnr, 'lift__forgivable')
def lift__strict_(rgnr, /):
    return light_wrap_rgnr_(rgnr, 'lift__strict')
def optional__forgivable_(rgnr, /):
    return light_wrap_rgnr_(rgnr, 'optional__forgivable')
def optional__strict_(rgnr, /):
    return light_wrap_rgnr_(rgnr, 'optional__strict')
def lookahead_(rgnr, /):
    return light_wrap_rgnr_(rgnr, 'lookahead')
def whole8header_(rgnr, /):
    return light_wrap_rgnr_(rgnr, 'whole8header')
def empty8header_(rgnr, /):
    return light_wrap_rgnr_(rgnr, 'empty8header')
def protect_header_(rgnr, /):
    return light_wrap_rgnr_(rgnr, 'protect_header')
def protect_whole_(rgnr, /):
    return light_wrap_rgnr_(rgnr, 'protect_whole')
def trial_and_error_(rgnr, /):
    '[trial_and_error_ =[def]= protect_header_] # used to replace try_rgnr_()'
    return light_wrap_rgnr_(rgnr, 'trial_and_error')




#.def recognize_(main_rgnr, env, gctx, istream, /, *, ignore=False):
#.    'IRecognizerLLoo -> env/IEnvironment -> gctx/mapping -> istream/IInputStream -> Reply'
#.    return _recognize(main_rgnr, env, gctx, istream, ignore)
#.def _recognize(_0main_rgnr, _0env, _0gctx, _0istream, _0ignore, /):
#.  if 1:
#.    ######################
#.    _0ctx = DynamicStackedMapping({})
#.    _0xctx = XContext(_0gctx, _0ctx)
#.    _0id2rgnr = _0main_rgnr.view_id2rgnr8all_descendants6env_(_0env)
#.    ######################
#.  def _call(rgnr, unlocker, ignore, istream, /):
#.    '-> gi<return-Reply>'
#.    dsymbols = rgnr._dsymbols_
#.    isymbols = rgnr._isymbols_
#.    may_osymbolXseq = rgnr._may_osymbolXseq_
#.    #mnmpre = rgnr._may_name4gpreprocess_
#.    #mnmgpost = rgnr._may_name4gpostprocess_
#.    mnmpre = mnmgpost = rgnr._may_name4ref_
#.    mpre_ = None if mnmpre is None else _0env.name2may_gpreprocess_(mnmpre)
#.    mgpost6ok_ = None if mnmgpost is None else _0env.name2may_gpostprocess6ok_(mnmgpost)
#.    mgpost6err_ = None if mnmgpost is None else _0env.name2may_gpostprocess6err_(mnmgpost)
#.
#.    _0xctx.del_items(dsymbols)
#.        ######################
#.        # [delete before enter ctx scope]
#.        ######################
#.    xctx_view = ContextView(isymbols, _0gctx, _0ctx)
#.    b_scope = rgnr._is_ctx_scope_
#.    p = _0ctx.env_tell() if b_scope else None
#.
#.    if not mpre_ is None:
#.        pre_ = mpre_
#.        # [gpreprocess :: (rgnr->env->xctx_view->ignore->ext_info8end->may ignore)]
#.        xxx mignore = pre_(rgnr, _0env, xctx_view, ignore, istream.tell_ext_info())
#.        if not mignore is None:
#.            ignore = mignore
#.            check_type_is(bool, ignore)
#.    ignore
#.    ex_args = [xctx_view[isymbol] for isymbol in rgnr._isymbol_seq8extra_params_]
#.    gi = rgnr._mk_gi4recognize_(_0env, xctx_view, unlocker, ignore, istream, *ex_args)
#.            # _tail_call() or forbod:tail_recur_Call
#.    assert hasattr(gi, 'send'), rgnr
#.    del ex_args
#.
#.
#.    bypass = unlocker.known_released or rgnr._bypass_check__assured_postcondition_unlocker_known_released_
#.    if 0:
#.        #since now validate 『unlocker.known_released』
#.        pass
#.    if (not b_scope and may_osymbolXseq is None and mgpost6err_ is None is mgpost6ok_ and not rgnr._tail_recur_Call_ok_ and bypass):
#.        #forbod:tail_recur_Call
#.        #   <<== not rgnr._tail_recur_Call_ok_
#.        return gi
#.    return _tail_call(gi, b_scope, p, may_osymbolXseq, mgpost6err_, mgpost6ok_, rgnr, xctx_view, ignore, unlocker)
#.  def _tail_call(gi, b_scope, p, may_osymbolXseq, mgpost6err_, mgpost6ok_, rgnr, xctx_view, ignore, unlocker, /):
#.    '-> gi<return-Reply>'
#.    reply = yield from gi
#.           # donot use 『yield from』
#.    if not (not reply.ok or unlocker.known_released):raise Exception('fail:[IRecognizerLLoo._mk_gi4recognize_():postcondition:[[reply.ok==True]=>[unlocker.known_released==True]]]')
#.    if type(reply) is Call:
#.        #tail_recur_Call ok
#.        #_tail_recur_Call_ok_
#.        rcall = reply
#.        reply = yield rcall
#.    if b_scope:
#.        _0ctx.env_pop_until(p)
#.    ######################
#.    # [exit ctx scope before assignment]
#.    ######################
#.    if reply.ok:
#.        _0xctx.set_items(may_osymbolXseq, reply.oresult)
#.        ######################
#.        # [assignment before gpostprocess6ok] <<== [gpostprocess6ok is external-registered, may change len(oresult)]
#.        ######################
#.        if not mgpost6ok_ is None:
#.            post6ok_ = mgpost6ok_
#.            # [gpostprocess6ok :: (rgnr->env->xctx_view->ignore->ext_info8end->oresult->oresult)]
#.            xxx oresult = post6ok_(rgnr, _0env, xctx_view, ignore, reply.ext_info8end, reply.oresult)
#.            if not oresult is reply.oresult:
#.                reply = reply.ireplace(eresult=mk_Right(oresult))
#.    else:
#.        if not mgpost6err_ is None:
#.            post6err_ = mgpost6err_
#.            # [gpostprocess6err :: (rgnr->env->xctx_view->ignore->ext_info8end->errmsg->errmsg)]
#.            xxx errmsg = post6err_(rgnr, _0env, xctx_view, ignore, reply.ext_info8end, reply.errmsg)
#.            if not errmsg is reply.errmsg:
#.                reply = reply.ireplace(eresult=mk_Left(errmsg))
#.    return reply
#.
#.    ######################
#.  def _on_rcall(gi_ls, rcall, /):
#.    '-> None'
#.    check_type_is(Call, rcall)
#.    (rgnr, unlocker, ignore, istream) = rcall
#.    check_type_is(bool, ignore)
#.    if unlocker.known_released:
#.        unlocker = dummy_unlocker
#.    if not id(rgnr) in _0id2rgnr:raise Exception('not persistent rgnr from IRecognizerLLoo.iter_persistent_descendants6env_', rgnr)
#.    gi = _call(rgnr, unlocker, ignore, istream)
#.    gi_ls.append(gi)
#.    gi_ls.append(mk_Right(None))
#.    ######################
#.  def _on_mreply(gi_ls, mreply, /):
#.    'gi_ls{nonempty} -> (may reply)[#None for init gi.send#] -> None'
#.    if not mreply is None:
#.        reply = mreply
#.        check_type_is(Reply, reply)
#.    gi = gi_ls[-1]
#.    try:
#.        rcall = gi.send(mreply)
#.    except StopIteration as e:
#.        reply = e.value
#.        check_type_is(Reply, reply)
#.            # <<== _tail_call() or forbod:tail_recur_Call
#.        gi_ls.pop()
#.        x = mk_Right(reply)
#.    else:
#.        check_type_is(Call, rcall)
#.        x = mk_Left(rcall)
#.    x
#.    gi_ls.append(x)
#.    ######################
#.  def _main():
#.    '-> Reply'
#.    _0main_rgnr.cache_full_view_info6env_(_0env)
#.    if not _0main_rgnr.required_num_tokens6backward6env_(_0env) <= _0istream.max_num_tokens6backward:raise Exception('istream.max_num_tokens6backward too small:', _0main_rgnr.required_num_tokens6backward6env_(_0env), _0istream.max_num_tokens6backward)
#.    main_rcall = mk_Call_(_0main_rgnr, dummy_unlocker, _0ignore, _0istream)
#.    x = mk_Left(main_rcall)
#.    gi_ls = [x]
#.        # [gi..., gi, (Either RecognizeCall (may Reply))]
#.    while gi_ls:
#.        x = gi_ls.pop()
#.        if x.is_left:
#.            rcall = x.left
#.            _on_rcall(gi_ls, rcall)
#.        else:
#.            mreply = x.right
#.            if not gi_ls:
#.                if mreply is None:raise 000
#.                    #[#mreply:=None for init gi.send#]
#.                reply = mreply
#.                break
#.            _on_mreply(gi_ls, mreply)
#.                #[#mreply:=None for init gi.send#]
#.    reply
#.    check_type_is(Reply, reply)
#.    return reply
#.  if 1:
#.    return _main()
#.#end-def recognize_(main_rgnr, env, gctx, istream, /, *, ignore):


class BoolVar:
    'public:BoolVar.b'
    def __repr__(sf, /):
        return repr_helper(sf, sf._b)
    def __init__(sf, x=False, /):
        sf._b = bool(x)
    def __bool__(sf, /):
        return sf._b
    @property
    def b(sf, /):
        '-> bool'
        return sf._b
    @b.setter
    def b(sf, x, /):
        sf._b = bool(x)
    def __ilshift__(sf, x, /):
        'sf <<= x'
        sf._b = bool(x)
        return sf
    def __ior__(sf, x, /):
        'sf |= x'
        sf._b |= bool(x)
        return sf
    def __iand__(sf, x, /):
        'sf &= x'
        sf._b &= bool(x)
        return sf
    def __ixor__(sf, x, /):
        'sf ^= x # xor # [sf <<= bool(sf) is not bool(x)]'
        sf._b ^= bool(x)
        return sf
    def __imod__(sf, x, /):
        'sf %= x # nxor # [sf <<= bool(sf) is bool(x)]'
        sf._b ^= not x
        return sf
    def __pos__(sf, /):
        '-> sf # [sf <<= True]'
        sf._b = True
        return sf
    def __neg__(sf, /):
        '-> sf # [sf <<= False]'
        sf._b = False
        return sf
    def __invert__(sf, /):
        '-> sf # [sf <<= not sf]'
        sf._b = not sf._b
        return sf
def __():
    x = BoolVar()
    assert not x
    x.b = 999
    assert x
    x = BoolVar(999)
    assert x
    x.b = None
    assert not x
__()
class ObjVar:
    'public:ObjVar.x'
    def __repr__(sf, /):
        return repr_helper(sf, sf.x)
    def __init__(sf, /, *tmay_x):
        if tmay_x:
            [x] = tmay_x
            sf.x = x
    def __bool__(sf, /):
        return hasattr(sf, 'x')
    ##@property
    ##def x(sf, /):
    ##    return sf.x
    ##@x.setter
    ##def x(sf, x, /):
    ##    sf.x = x
    ##@x.deleter
    ##def x(sf, /):
    ##    del sf.x
def __():
    x = ObjVar()
    assert not x
    x.x = False
    assert x
    assert x.x is False
    del x.x
    assert not x
__()

class IRecognizerLLoo__serial(IRecognizerLLoo):
    r'''
    'serial-rgnr'
        #serial has no snapshot (may need protect_header_())
        #   priority_parallel has a snapshot(or using trial_and_error_())
    '''#'''
    __slots__ = ()
    #@override
    ###cancel:_is_ctx_scope_ = True
        ##<<==only for pseudo_func_body_stmt_flow not serial
    @property
    @abstractmethod
    def _not_ignore_toplvl_(sf, /):
        '-> bool #true-tuple, not ignore the top-level tuple # required by RecognizerLLoo__unbox_tuple'
    @abstractmethod
    def _iter_runtime_serial_children_(sf, env, xctx_view, ignore:bool, var_changed, var_ok, var_reply, /):
        '-> Iter (ignore4outer/ignore4slots/bool, IRecognizerLLoo, unlock_case/(may begin_vs_middle/bool), ignore4inner/ignore4child_rgnr/bool, unpack/bool, fail_vs_stop_vs_continue/{0,1,2}) #[var_changed :: BoolVar{monotonic_idx8begin.changed}] #[var_ok :: BoolVar{reply.ok}] #[fail_vs_stop_vs_continue:when not reply.ok and not monotonic_idx8begin.changed=>fail-or-stop{ok}-continue{serial}] #see:Output__oresult'
    @override
    def _mk_gi4recognize_(sf, env, xctx_view, unlocker, ignore:bool, istream, /):
        ls = [] if not ignore or sf._not_ignore_toplvl_ else dummy_list
        var_changed = BoolVar()
        var_ok = BoolVar()
        var_reply = ObjVar()

        _unlocker = dummy_unlocker
        released = unlocker.known_released
        #serial has no snapshot
        #   priority_parallel has a snapshot(or using trial_and_error_)
        it = sf._iter_runtime_serial_children_(env, xctx_view, ignore, var_changed, var_ok, var_reply)
        000;    del ignore
        for (ignore4outer, rgnr, unlock_case, ignore4inner, unpack, fail_vs_stop_vs_continue) in it:
            if not released:
              match unlock_case:
                case None:
                    pass
                case False:
                    # begin_vs_middle:=False
                    # release@begin
                    unlocker.unlocker_release()
                    unlocker = dummy_unlocker
                    released = True
                case True:
                    # begin_vs_middle:=True
                    # release@middle
                    _unlocker = unlocker
                    if 0:
                        # !! cancel since fail_vs_stop-->fail_vs_stop_vs_continue
                        unlocker = dummy_unlocker
                        released = True#will be released #see below:『assert _unlocker.known_released or not reply.ok』after『yield Call...』
                case _:
                    raise 000
            _unlocker
            #bug:using boxed_istream8begin: child may consume it but return a protected one from snapshot
            #
            #boxed_istream8begin = istream.boxed_istream
            monotonic_idx8begin = istream.tell_monotonic_idx()
            reply = yield mk_Call_(rgnr, _unlocker, ignore4inner, istream)
            #bug:assert _unlocker.known_released
            assert _unlocker.known_released or not reply.ok
            #changed = boxed_istream8begin.changed
            changed = not monotonic_idx8begin == reply.monotonic_idx8end
            if not reply.ok:
                if changed or fail_vs_stop_vs_continue==0:
                    #fail
                    return reply
                #will stop,continue
                if fail_vs_stop_vs_continue == 1:
                    #stop
                    _unlocker.unlocker_release()
                    if not released:
                        if _unlocker is unlocker:
                            released = True
                            unlocker = dummy_unlocker
                #will stop,continue
            #xxx:_unlocker.unlocker_release()
                # !! #now cancel auto release:unlocker_release() <<== [@fail:not reply.ok: (unlocker>>snapshot) should not unlocker_release()!]
            else:
                #_unlocker.unlocker_release()
                assert _unlocker.known_released
            _unlocker = dummy_unlocker
            var_reply.x = reply
            var_ok.b = reply.ok
            var_changed.b = changed
            #777;    del boxed_istream8begin
            #istream = reply.istream8end
            if not reply.ok:
                if fail_vs_stop_vs_continue == 1:
                    #stop
                    break
                #continue
                # => #now cancel auto release:unlocker_release() <<== [@fail:not reply.ok: (unlocker>>snapshot) should not unlocker_release()!]
                assert fail_vs_stop_vs_continue == 2
                continue
            #if not ignore:
            if not ignore4outer:
                #NOTE:『ignore』changed
                if unpack:
                    ls.extend(reply.oresult)
                else:
                    ls.append(reply.oresult)
        assert _unlocker.known_released
            #not-bug@[not_ok&&continue]
            #   !! reset as dummy_unlocker
        unlocker.unlocker_release()
        unlocker = dummy_unlocker
        #NOTE:『ignore』changed
        if hasattr(var_reply, 'x') and type(var_reply.x) is Output__oresult:
            oresult = var_reply.x.get_oresult()
        else:
            oresult = tuple(ls) if not ls is dummy_list else None
                #NOTE:『ignore』changed
                #NOTE:++『sf._not_ignore_toplvl_』
        oresult
        eresult = mk_Right(oresult)
        ext_info8end = istream.tell_ext_info()
        reply = Reply(eresult, ext_info8end)
        return reply

class DummyList:
    def append(sf, x, /):
        pass
    def extend(sf, x, /):
        pass
dummy_list = DummyList()

class IRecognizerLLoo__priority_parallel(IRecognizerLLoo):
    'priority_parallel-rgnr #priority_parallel_rgnr#cascade'
    __slots__ = ()
    @abstractmethod
    def _iter_priority_parallel_children_(sf, env, /):
        '-> Iter IRecognizerLLoo # [must be finite][must be persistent obj, twice yield same obj][may saved into env.external_cache]'
    @override
    def _iter_persistent_children6env_(sf, env, /):
        '-> Iter IRecognizerLLoo # [must be finite][must be persistent obj, twice yield same obj][may saved into env.external_cache]'
        return sf._iter_priority_parallel_children_(env)
    @override
    def _mk_gi4recognize_(sf, env, xctx_view, unlocker, ignore:bool, istream, /):
        it = sf._iter_priority_parallel_children_(env)
        assert it is iter(it)
        for rgnr in it:
            break
        else:
            errmsg = 'no_branches'
            eresult = mk_Left(errmsg)
            ext_info8end = istream.tell_ext_info()
            reply = Reply(eresult, ext_info8end)
            return reply
        rgnr
        first = True
        for _rgnr in it:
            rgnr#not last
            ######
            if first:
                first = False
                snapshot = istream.save2snapshot()
                _unlocker = unlocker >> snapshot
            ######
            reply = yield mk_Call_(rgnr, _unlocker, ignore, istream)
            if reply.ok or snapshot.snapshot_released:
                snapshot.snapshot_release()
                return reply
            snapshot.restore_and_hold(istream)
            ######
            rgnr = _rgnr
        rgnr#last
        if not first:
            snapshot.snapshot_release()
            777;    del snapshot, _unlocker
        reply = yield mk_Call_(rgnr, unlocker, ignore, istream)
        return reply


class IRecognizerLLoo__solo_child6env(IRecognizerLLoo):
    'solo_child6env-rgnr'
    __slots__ = ()
    @abstractmethod
    def _get_the_cached_child6env_(sf, env, /):
        '-> IRecognizerLLoo # [must be persistent obj, twice yield same obj][may saved into env.external_cache]'
    @override
    def _iter_persistent_children6env_(sf, env, /):
        '-> Iter IRecognizerLLoo # [must be finite][must be persistent obj, twice yield same obj][may saved into env.external_cache]'
        yield sf._get_the_cached_child6env_(env)

class IRecognizerLLoo__two_children6env(IRecognizerLLoo):
    'two_children6env-rgnr'
    __slots__ = ()
    @abstractmethod
    def _get_the_two_cached_children6env_(sf, env, /):
        '-> (IRecognizerLLoo, IRecognizerLLoo) # [must be persistent obj, twice yield same obj][may saved into env.external_cache]'
    @override
    def _iter_persistent_children6env_(sf, env, /):
        '-> Iter IRecognizerLLoo # [must be finite][must be persistent obj, twice yield same obj][may saved into env.external_cache]'
        return iter(sf._get_the_two_cached_children6env_(env))

class IHasAttr__forgivable_fail_be_ok(ABC):
    __slots__ = ()
    @property
    @abstractmethod
    def _forgivable_fail_be_ok_(sf, /):
        '-> bool'

r"""[[[
.
.
.#since: flip only for (forgivable_fail) ==>> ???only for try # i.e. flip(try_rgnr_(rgnr)) try_rgnr_() is not enough!!! how to avoid severe_fail??? ==>> severe_try
.#
.#xxx:since: flip only for (ok{monotonic_idx8begin unchanged} +++ forgivable_fail) ==>> only for lookahead!!!
.#
.#==>>:
.#
.##class IRecognizerLLoo__flip(IRecognizerLLoo__solo_child6env):
.##    'flip-rgnr'
.##    __slots__ = ()
.##    @override
.##    def _mk_gi4recognize_(sf, env, xctx_view, unlocker, ignore:bool, istream, /):
.##        rgnr = sf._get_the_cached_child6env_(env)
.##        reply = yield mk_Call_(rgnr, dummy_unlocker, ignore, istream)
.##        reply = reply.ireplace(eresult=~reply.eresult)
.##        return reply
.
.
.class IRecognizerLLoo__lookahead(IRecognizerLLoo__solo_child6env):
.    'lookahead-rgnr'
.    __slots__ = ()
.    @override
.    def _mk_gi4recognize_(sf, env, xctx_view, unlocker, ignore:bool, istream, /):
.        rgnr = sf._get_the_cached_child6env_(env)
.        snapshot = istream.save2snapshot()
.        reply = yield mk_Call_(rgnr, dummy_unlocker, ignore, istream)
.        snapshot.restore_and_release(istream)
.        777;    del snapshot
.        ext_info8end = istream.tell_ext_info()
.        reply = Reply(reply.eresult, ext_info8end)
.        #return reply
.            #bug:missing: [postcondition:[[reply.ok==True]=>[unlocker.known_released==True]]]
.        if reply.ok:
.            unlocker.unlocker_release()
.        return reply
.
.class IRecognizerLLoo__try(IRecognizerLLoo__solo_child6env):
.    'try-rgnr#see:try_rgnr_@IRecognizerLLoo__repetition&&fail_vs_stop_vs_continue@IRecognizerLLoo__serial'
.    __slots__ = ()
.    @override
.    def _mk_gi4recognize_(sf, env, xctx_view, unlocker, ignore:bool, istream, /):
.        rgnr = sf._get_the_cached_child6env_(env)
.        snapshot = istream.save2snapshot()
.        reply = yield mk_Call_(rgnr, unlocker >> snapshot, ignore, istream)
.        if not reply.ok:
.            if snapshot.snapshot_released:
.                #(severe_fail|forgivable_fail)
.                #fail
.                return reply
.                    # 0. * fail and monotonic_idx8begin changed
.                    # 1. * fail but monotonic_idx8begin keep unchanged
.            #protected_fail
.            snapshot.restore_and_release(istream)
.            777;    del snapshot
.            #protected_fail --> forgivable_fail
.            ext_info8end = istream.tell_ext_info()
.            #forgivable_fail
.            reply = Reply(reply.eresult, ext_info8end)
.            #fail but monotonic_idx8begin keep unchanged
.        return reply
.            # 1. * fail but monotonic_idx8begin keep unchanged
.            # 2. * ok
.
.class IRecognizerLLoo__optional(IRecognizerLLoo__solo_child6env, IHasAttr__forgivable_fail_be_ok):
.    'optional-rgnr'
.    __slots__ = ()
.    @override
.    def _mk_gi4recognize_(sf, env, xctx_view, unlocker, ignore:bool, istream, /):
.        ######################
.        #after hasattr ._forgivable_fail_be_ok_:
.        ######################
.        reply = yield IRecognizerLLoo__lift._mk_gi4recognize_(sf, env, xctx_view, unlocker, ignore, istream)
.            # donot use 『yield from』
.        if reply.ok:
.            (case4fail, unchanged, original_reply) = reply.oresult
.            tmay_original_oresult = original_reply.to_tmay_right()
.            777;    del original_reply
.            reply = Reply(mk_Right(tmay_original_oresult), reply.ext_info8end)
.        return reply
.        ######################
.        #before hasattr ._forgivable_fail_be_ok_:
.        ######################
.        ##rgnr = sf._get_the_cached_child6env_(env)
.        ##snapshot = istream.save2snapshot()
.        ##reply = yield mk_Call_(rgnr, unlocker >> snapshot, ignore, istream)
.        ##if not reply.ok:
.        ##    if snapshot.snapshot_released:
.        ##        #(severe_fail|forgivable_fail)
.        ##        #fail
.        ##        return reply
.        ##            # 0. * fail and monotonic_idx8begin changed
.        ##            # 1. * fail but monotonic_idx8begin keep unchanged
.        ##    #protected_fail
.        ##    snapshot.restore_and_release(istream)
.        ##    777;    del snapshot
.        ##    #protected_fail --> forgivable_fail
.        ##    ext_info8end = istream.tell_ext_info()
.        ##    #forgivable_fail
.        ##    reply = Reply(mk_Right(null_tuple), ext_info8end)
.        ##    # 3. * ok with null_tuple and monotonic_idx8begin keep unchanged
.        ##else:
.        ##    reply = reply.ireplace(eresult=mk_Right((reply.oresult,)))
.        ##    # 4. * ok with (oresult,)
.        ##return reply
.        ##    # 3. * ok with null_tuple and monotonic_idx8begin keep unchanged
.        ##    # 4. * ok with (oresult,)
.class IRecognizerLLoo__lift(IRecognizerLLoo__solo_child6env, IHasAttr__forgivable_fail_be_ok):
.    r'''[[[
.    'lift-rgnr#[main purpose:to lift eresult.ok] #but optional_rgnr plays similar role...'
.    [oresult<lift(rgnr)> :: (case4fail/(0|1|2), unchanged<monotonic_idx8begin>, original_reply<rgnr>)]
.    [case4fail :: (0/ok|1/protected_fail|2/forgivable_fail)]
.        『2』==>>『_forgivable_fail_be_ok_==True』
.
.    # [:lookahead__vs__try__vs__optional__vs__lift]:goto
.    # [:protected_fail__vs__forgivable_fail__vs__severe_fail]:goto
.        move to module.__doc__
.
.
.    #]]]'''#'''
.    __slots__ = ()
.    @override
.    def _mk_gi4recognize_(sf, env, xctx_view, unlocker, ignore:bool, istream, /):
.        ######################
.        #this func is used directly by IRecognizerLLoo__optional
.        ######################
.        rgnr = sf._get_the_cached_child6env_(env)
.        snapshot = istream.save2snapshot()
.        monotonic_idx8begin = istream.tell_monotonic_idx()
.        reply = yield mk_Call_(rgnr, unlocker >> snapshot, ignore, istream)
.        unchanged = monotonic_idx8begin == istream.tell_monotonic_idx()
.        if not reply.ok:
.            # -1. * fail but not snapshot_released
.            # -2. * fail but monotonic_idx8begin keep unchanged
.            # -3. * fail and snapshot_released and monotonic_idx8begin changed
.            if not snapshot.snapshot_released:
.                #protected_fail
.                case4fail = 1
.                snapshot.restore_and_release(istream)
.                777;    del snapshot
.                #protected_fail --> forgivable_fail
.                #forgivable_fail
.            elif unchanged:
.                #forgivable_fail
.                case4fail = 2
.                if not sf._forgivable_fail_be_ok_:
.                    #fail
.                    return reply
.                pass
.            else:
.                #severe_fail
.                #xxx:case4fail = 3#useless
.                #fail
.                return reply
.            ext_info8end = istream.tell_ext_info()
.        else:
.            #ok
.            case4fail = 0
.            ext_info8end = reply.ext_info8end
.        ext_info8end
.        reply = Reply(mk_Right((case4fail, unchanged, reply)), ext_info8end)
.        return reply
.                    #protected_fail
.                    #forgivable_fail if sf._forgivable_fail_be_ok_
.                    #ok
.            ###vs:
.                    #severe_fail
.                    #forgivable_fail if not sf._forgivable_fail_be_ok_
#]]]"""#"""




#bug:class IRecognizerLLoo__repetition(IRecognizerLLoo__serial, IRecognizerLLoo__solo_child6env):
#   not solo but two:(rgnr,try_rgnr_(rgnr))
#   now:[builtin_support:light_wrap_rgnr_()]&&trial_and_error_()
#       TODO
class IRecognizerLLoo__repetition(IRecognizerLLoo__serial, IRecognizerLLoo__two_children6env):
    'repetition-rgnr/many'
    __slots__ = ()
    #@override
    _not_ignore_toplvl_ = False
    @abstractmethod
    def _get_repetition_args6env_(sf, env, /):
        '-> repetition_args/(min, may_max, unlock_idx, begin_vs_middle, ignore, unpack)/(uint, may uint, unit, bool, bool, bool)'
    @override
    def _iter_runtime_serial_children_(sf, env, xctx_view, ignore:bool, var_changed, var_ok, var_reply, /):
        '-> Iter (ignore4outer/bool, IRecognizerLLoo, unlock_case/(may begin_vs_middle/bool), ignore4inner/bool, unpack/bool, fail_vs_stop_vs_continue/{0,1,2})'
        #bug:rgnr = sf._get_the_cached_child6env_(env)
        rgnr, rgnr8trial = sf._get_the_two_cached_children6env_(env)
        (_min, may_max, unlock_idx, begin_vs_middle, _ignore, unpack) = sf._get_repetition_args6env_(env)
        #if not step > 0:raise Exception
        if not 0 <= unlock_idx <= _min:raise Exception
        if None is not may_max < _min:raise Exception
        ignore = ignore or _ignore
        fail_vs_stop_vs_continue = 0

        def _mk(k, /):
            unlock_case = mk_unlock_case(unlock_idx, begin_vs_middle, k)
            return (ignore, rgnr, unlock_case, ignore, unpack, fail_vs_stop_vs_continue)


        if 0:
            #bug:
            #.may_max1 = may_max+1 if not None is may_max else None
            #.it = count_(_min, may_max1, 1)
            pass
        it = count_(_min, may_max, 1)
        def _post_check():
            if not var_changed:
                #rgnr nullable
                if may_max is None:raise Exception('nullable-rgnr[??:+oo]')
                raise 000
        if not may_max is None:
            def _post_check():
                pass

        for k in range(_min):
            yield _mk(k)
            _post_check()

        unlock_case = False # begin_vs_middle
            #since maybe [unlock_idx==_min] ==>> not released yet
        #bug:x = (try_rgnr_(rgnr), unlock_case, ignore, unpack, fail_vs_stop_vs_continue:=1)
        #   replace "try_rgnr_(rgnr)" by persistent "rgnr8trial"
        x = (ignore, rgnr8trial, unlock_case, ignore, unpack, fail_vs_stop_vs_continue:=1)
        for _ in it:
            yield x
            _post_check()
            #unlock_case = None
        return

def mk_unlock_case(unlock_idx, begin_vs_middle, k, /):
    unlock_case = begin_vs_middle if k == unlock_idx else None
    return unlock_case
#.def explain_unpack_case_with_(ignore, unpack_case, /):
#.    'ignore -> unpack_case -> (ignore, unpack)/(bool,bool) # [unpack_case :: (0/ignore|1/ignorable_normal|2/ignorable_unpack|-1/non_ignorable_normal|-2/non_ignorable_unpack)]'
def explain_unpack_case_with_(ignore, unpack_case, /):
    '[after ++_not_ignore_toplvl_/to_keep_tpl/bool] => ignore -> unpack_case -> (ignore4outer, ignore4inner, unpack)/(bool,bool,bool) # [unpack_case :: (0/ignore|1/ignorable_normal|2/ignorable_unpack|-1/non_ignorable_normal|-2/non_ignorable_unpack)]'
    #old-API:(ignore4inner, unpack) = explain_unpack_case_with_(ignore, unpack_case)
    #new-API:(ignore4outer, ignore4inner, unpack) = explain_unpack_case_with_(ignore, unpack_case)
    #
    (ignorable, _ignore, unpack) = explain_unpack_case(unpack_case)
    if ignorable:
        ignore4inner = _ignore or ignore
        ignore4outer = False#always#to_keep_tpl
    else:
        ignore4inner = _ignore
        ignore4outer = _ignore#stable#to_keep_tpl
    return (ignore4outer, ignore4inner, unpack)
def explain_unpack_case(unpack_case, /):
    'unpack_case -> (ignorable, ignore, unpack)/(bool,bool,bool) # [unpack_case :: (0/ignore|1/ignorable_normal|2/ignorable_unpack|-1/non_ignorable_normal|-2/non_ignorable_unpack)]'
    return _4unpack_case[unpack_case]
_4unpack_case = ({**{}
,0:
    #ignore
    (False, True, False)
,1:
    #ignorable_normal
    (True, False, False)
,2:
    #ignorable_unpack
    (True, False, True)
,-1:
    #non_ignorable_normal
    (False, False, False)
,-2:
    #non_ignorable_unpack
    (False, False, True)
})

class IRecognizerLLoo__gsep_end_by(IRecognizerLLoo__serial):
    'gsep_end_by-rgnr #nongreedy'
    __slots__ = ()
    #@override
    _not_ignore_toplvl_ = False
    @abstractmethod
    def _get_gsep_end_by_args6env_(sf, env, /):
        '-> gsep_end_by_args/(args4body, may_args4sep_body, may_args4end, args4cntl)/((rgnr8body, rgnr8trial_body, ignore4body, unpack4body), may (rgnr8sep_body, rgnr8trial_sep_body, ignore4sep_body, unpack4sep_body), may (rgnr8end, rgnr8trial_end, ignore4end, unpack4end), (min, may_max, unlock_idx, begin_vs_middle))/((rgnr, rgnr, bool, bool), may (rgnr, rgnr, bool, bool), may (rgnr, rgnr, bool, bool), (uint, may uint, unit, bool))'
    @override
    def _iter_persistent_children6env_(sf, env, /):
        '-> Iter IRecognizerLLoo # [must be finite][must be persistent obj, twice yield same obj][may saved into env.external_cache]'
        gsep_end_by_args = sf._get_gsep_end_by_args6env_(env)
        (args4body, may_args4sep_body, may_args4end, args4cntl) = gsep_end_by_args
        (rgnr8body, rgnr8trial_body, ignore4body, unpack4body) = args4body
        yield rgnr8body
        yield rgnr8trial_body
        if not None is may_args4sep_body:
            args4sep_body = may_args4sep_body
            (rgnr8sep_body, rgnr8trial_sep_body, ignore4sep_body, unpack4sep_body) = args4sep_body
            yield rgnr8sep_body
            yield rgnr8trial_sep_body
        if not None is may_args4end:
            args4end = may_args4end
            (rgnr8end, rgnr8trial_end, ignore4end, unpack4end) = args4end
            yield rgnr8end
            yield rgnr8trial_end


    @override
    def _iter_runtime_serial_children_(sf, env, xctx_view, ignore:bool, var_changed, var_ok, var_reply, /):
        '-> Iter (ignore4outer/bool, IRecognizerLLoo, unlock_case/(may begin_vs_middle/bool), ignore4inner/bool, unpack/bool, fail_vs_stop_vs_continue/{0,1,2})'
        gsep_end_by_args = sf._get_gsep_end_by_args6env_(env)
        (args4body, may_args4sep_body, may_args4end, args4cntl) = gsep_end_by_args
        (_min, may_max, unlock_idx, begin_vs_middle) = args4cntl

        (rgnr8body, rgnr8trial_body, ignore4body, unpack4body) = args4body
        args4sep_body = ifNone(may_args4sep_body, args4body)
        (rgnr8sep_body, rgnr8trial_sep_body, ignore4sep_body, unpack4sep_body) = args4sep_body

        greedy = may_args4end is None
        if not greedy:
            args4end = may_args4end
            (rgnr8end, rgnr8trial_end, ignore4end, unpack4end) = args4end




        #if not step > 0:raise Exception
        if not 0 <= unlock_idx <= _min:raise Exception
        if None is not may_max < _min:raise Exception
        ignore4body = ignore or ignore4body
        ignore4sep_body = ignore or ignore4sep_body
        if not greedy:
            ignore4end = ignore or ignore4end
        del ignore
        fail_vs_stop_vs_continue = 0

        def _mk(rgnr8xxx_body, k, /):
            unlock_case = mk_unlock_case(unlock_idx, begin_vs_middle, k)
            return (ignore4xxx_body, rgnr8xxx_body, unlock_case, ignore4xxx_body, unpack4xxx_body, fail_vs_stop_vs_continue)


        if 0:
            #bug:
            #.may_max1 = may_max+1 if not None is may_max else None
            #.it = count_(_min, may_max1, 1)
            pass
        it = count_(_min, may_max, 1)
        def _post_check():
            if not var_changed:
                #rgnr8sep_body nullable
                if may_max is None:raise Exception('nullable-rgnr[??:+oo]')
                raise 000
        if not may_max is None:
            def _post_check():
                pass

        def dummy_on_post_head1_():
            pass
        def on_post_head1_():
            nonlocal rgnr8xxx_body, rgnr8trial_xxx_body, on_post_head1_
            rgnr8xxx_body = rgnr8sep_body
            rgnr8trial_xxx_body = rgnr8trial_sep_body
            ignore4xxx_body = ignore4sep_body
            unpack4xxx_body = unpack4sep_body
            on_post_head1_ = dummy_on_post_head1_
        if may_args4sep_body is None:
            on_post_head1_ = dummy_on_post_head1_

        ######################
        rgnr8xxx_body = rgnr8body
        rgnr8trial_xxx_body = rgnr8trial_body
        ignore4xxx_body = ignore4body
        unpack4xxx_body = unpack4body
        k = -1
            #for below:assert k == may_max-1
        for k in range(_min):
            yield _mk(rgnr8xxx_body, k)
            #_post_check()
            on_post_head1_()




        ######################
        def calc_y():
            if greedy:
                y = None
            else:
                rgnr8end # may_rgnr8end
                y = (ignore4end, rgnr8end, unlock_case:=False, ignore4end, unpack4end, fail_vs_stop_vs_continue:=0)#fail
            return y
        def calc_z():
            if greedy:
                z = None
            else:
                rgnr8trial_end # may_rgnr8trial_end
                z = (ignore4end, rgnr8trial_end, unlock_case:=True, ignore4end, unpack4end, fail_vs_stop_vs_continue:=2)#continue
            return z

        def calc_x(rgnr8trial_xxx_body, /):
            unlock_case = False # begin_vs_middle
                #since maybe [unlock_idx==_min] ==>> not released yet
            rgnr8trial_xxx_body
            if greedy:
                x = (ignore4xxx_body, rgnr8trial_xxx_body, unlock_case:=False, ignore4xxx_body, unpack4xxx_body, fail_vs_stop_vs_continue:=1)#stop
            else:
                x = (ignore4xxx_body, rgnr8trial_xxx_body, unlock_case:=False, ignore4xxx_body, unpack4xxx_body, fail_vs_stop_vs_continue:=0)#fail
            return x

        def dummy_on_post_head2_():
            pass
        def on_post_head2_():
            nonlocal x, on_post_head2_
            on_post_head1_()
            rgnr8trial_xxx_body#updated
            x = calc_x(rgnr8trial_xxx_body)
            on_post_head2_ = dummy_on_post_head2_
        if on_post_head1_ is dummy_on_post_head1_:
            on_post_head2_ = dummy_on_post_head2_



        rgnr8trial_xxx_body
        x = calc_x(rgnr8trial_xxx_body)
        z = calc_z()
        y = calc_y()
        for k in it:
            if not greedy:
                yield z
                if var_ok.b:
                    break
            yield x
            _post_check()
            on_post_head2_()
            #unlock_case = None
        else:
            #bug:assert k == may_max
            #   now:count_(_min, may_max1, 1) --> count_(_min, may_max, 1)
            assert k == may_max-1
            if not greedy:
                yield y
        return

def fmap_may_(f, may_x, /):
    if not None is may_x:
        x = may_x
        return f(x)
    return None
def check_may_IRecognizerLLoo(may_rgnr, /):
    if not None is may_rgnr:
        rgnr = may_rgnr
        check_type_le(IRecognizerLLoo, rgnr)
def _iu_rgnr2tiu_rgnr(iu_rgnr, /):
    check_type_is(tuple, iu_rgnr) #for:_Base4repr._reset4repr()
    (rgnr, ignore, unpack) = iu_rgnr
    check_type_le(IRecognizerLLoo, rgnr)
    check_type_is(bool, ignore)
    check_type_is(bool, unpack)

    rgnr8trial = trial_and_error_(rgnr)
    tiu_rgnr = (rgnr, rgnr8trial, ignore, unpack)
    return tiu_rgnr
class IRecognizerLLoo__gsep_end_by__init(IRecognizerLLoo__gsep_end_by, _Base4repr):
    ___no_slots_ok___ = True
    def __init__(sf, iu_rgnr8body, may_iu_rgnr8sep_body, may_iu_rgnr8end, _min, may_max, unlock_idx, begin_vs_middle, /):
        args4body = _iu_rgnr2tiu_rgnr(iu_rgnr8body)
        may_args4sep_body = fmap_may_(_iu_rgnr2tiu_rgnr, may_iu_rgnr8sep_body)
        may_args4end = fmap_may_(_iu_rgnr2tiu_rgnr, may_iu_rgnr8end)

        check_int_ge(0, _min)
        if not None is may_max:
            _max = may_max
            check_int_ge(_min, _max)

        check_int_ge_le(0, _min, unlock_idx)
        check_type_is(bool, begin_vs_middle)
        if unlock_idx == _min and begin_vs_middle: raise TypeError

        args4cntl = (_min, may_max, unlock_idx, begin_vs_middle)
        gsep_end_by_args = (args4body, may_args4sep_body, may_args4end, args4cntl)
        sf._gargs = gsep_end_by_args
        #sf._args4repr = (iu_rgnr8body, may_iu_rgnr8sep_body, may_iu_rgnr8end, _min, may_max, unlock_idx, begin_vs_middle)
        sf._reset4repr((iu_rgnr8body, may_iu_rgnr8sep_body, may_iu_rgnr8end, _min, may_max, unlock_idx, begin_vs_middle))
    @override
    def _get_gsep_end_by_args6env_(sf, env, /):
        return sf._gargs
class RecognizerLLoo__gsep_end_by(IRecognizerLLoo__gsep_end_by__init, IRecognizerLLoo__default_mixins):pass
check_non_ABC(RecognizerLLoo__gsep_end_by)

class RecognizerLLoo__many(RecognizerLLoo__gsep_end_by):
    #class RecognizerLLoo__many(BaseRecognizerLLoo__alias__default_mixins):
    'many vs repetition'
        #'RecognizerLLoo__many vs RecognizerLLoo__repetition'
    def __init__(sf, rgnr, _min=0, may_max=None, ignore=False, unpack=False, /):
        (unlock_idx, begin_vs_middle) = mk_head_unlock_idx_ex5min_(_min)
        ls = pop_defaults_([rgnr, _min, may_max, ignore, unpack], [0, None, False, False])
        iu_rgnr8body = (rgnr, ignore, unpack)
        super().__init__(iu_rgnr8body, may_iu_rgnr8sep_body:=None, may_iu_rgnr8end:=None, _min, may_max, unlock_idx, begin_vs_middle)
        #sf._args4repr = tuple(ls)
        sf._reset4repr(tuple(ls))
check_non_ABC(RecognizerLLoo__many)
#end-class RecognizerLLoo__many(RecognizerLLoo__gsep_end_by):

def mk_head_unlock_idx_ex5min_(_min, /):
    check_int_ge(0, _min)
    return (unlock_idx:=0, begin_vs_middle:=not _min == 0)
    #.if _min == 0:
    #.    unlock_idx = 0
    #.    begin_vs_middle = False
    #.else:
    #.    unlock_idx = 0
    #.    begin_vs_middle = True
    #.return (unlock_idx, begin_vs_middle)

def pop_defaults_(args, defaults, /):
    ls = [*args]
    vs = [*defaults]
    L = len(ls) - len(vs)
    assert L >= 0
    while vs and vs[-1] is ls[-1]:
        vs.pop()
        ls.pop()
    assert len(ls) - len(vs) == L
    return ls




class RecognizerLLoo__end_by(RecognizerLLoo__gsep_end_by):
    'end_by'
    def __init__(sf, rgnr8end, rgnr8body, _min=0, may_max=None, ignore4end=True, unpack4end=False, ignore4body=False, unpack4body=False, /):
        (unlock_idx, begin_vs_middle) = mk_head_unlock_idx_ex5min_(_min)
        iu_rgnr8body = (rgnr8body, ignore4body, unpack4body)
        iu_rgnr8end = (rgnr8end, ignore4end, unpack4end)
        super().__init__(iu_rgnr8body, may_iu_rgnr8sep_body:=None, may_iu_rgnr8end:=iu_rgnr8end, _min, may_max, unlock_idx, begin_vs_middle)
        ls = pop_defaults_([rgnr8end, rgnr8body, _min, may_max, ignore4end, unpack4end, ignore4body, unpack4body], [0, None, True, False, False, False])
        #sf._args4repr = tuple(ls)
        sf._reset4repr(tuple(ls))
check_non_ABC(RecognizerLLoo__end_by)
#end-class RecognizerLLoo__end_by(RecognizerLLoo__gsep_end_by):



class RecognizerLLoo__sep_end_by(RecognizerLLoo__gsep_end_by):
    'sep_end_by'
    def __init__(sf, rgnr8sep, rgnr8end, rgnr8body, _min=0, may_max=None, ignore4sep=True, unpack4sep=False, ignore4end=True, unpack4end=False, ignore4body=False, unpack4body=False, /):
        (iu_rgnr8body, iu_rgnr8sep_body, unlock_idx, begin_vs_middle) = _init4sep_xxx_by(rgnr8sep, rgnr8body, _min, ignore4sep, unpack4sep, ignore4body, unpack4body)
        iu_rgnr8end = (rgnr8end, ignore4end, unpack4end)
        super().__init__(iu_rgnr8body, may_iu_rgnr8sep_body:=iu_rgnr8sep_body, may_iu_rgnr8end:=iu_rgnr8end, _min, may_max, unlock_idx, begin_vs_middle)

        ls = pop_defaults_([rgnr8sep, rgnr8end, rgnr8body, _min, may_max, ignore4sep, unpack4sep, ignore4end, unpack4end, ignore4body, unpack4body], [0, None, True, False, True, False, False, False])
        #sf._args4repr = tuple(ls)
        sf._reset4repr(tuple(ls))
check_non_ABC(RecognizerLLoo__sep_end_by)
#end-class RecognizerLLoo__sep_end_by(RecognizerLLoo__gsep_end_by):


def _init4sep_xxx_by(rgnr8sep, rgnr8body, _min, ignore4sep, unpack4sep, ignore4body, unpack4body, /):
    bs = [ignore4sep, unpack4sep, ignore4body, unpack4body]
    if bs == [True, False, False, False]:
        rgnr8sep_body = RecognizerLLoo__unbox_tuple(1, 0, True, [rgnr8sep, rgnr8body])
    elif bs == [False, False, True, False]:
        rgnr8sep_body = RecognizerLLoo__unbox_tuple(0, 0, True, [rgnr8sep, rgnr8body])
    else:
        unpack_case4sep = mk_ignorable_unpack_case_(ignore4sep, unpack4sep)
        unpack_case4body = mk_ignorable_unpack_case_(ignore4body, unpack4body)
        rgnr8sep_body = RecognizerLLoo__serial(0, True, [(rgnr8sep, unpack_case4sep, 0), (rgnr8body, unpack_case4body, 0)])
    rgnr8sep_body
    ignore4sep_body = ignore4sep and ignore4body
    unpack4sep_body = unpack4sep or unpack4body

    (unlock_idx, begin_vs_middle) = mk_head_unlock_idx_ex5min_(_min)
    iu_rgnr8body = (rgnr8body, ignore4body, unpack4body)
    iu_rgnr8sep_body = (rgnr8sep_body, ignore4sep_body, unpack4sep_body)
    return (iu_rgnr8body, iu_rgnr8sep_body, unlock_idx, begin_vs_middle)
def mk_ignorable_unpack_case_(ignore, unpack, /):
    'ignore/bool -> unpack/bool -> only ignorable-unpack_case/{0,1,2}'
    check_type_is(bool, ignore)
    check_type_is(bool, unpack)
    unpack_case = 0 if ignore else (2 if unpack else 1)
    return unpack_case


class RecognizerLLoo__sep_by(RecognizerLLoo__gsep_end_by):
    'sep_by'
    def __init__(sf, rgnr8sep, rgnr8body, _min=0, may_max=None, ignore4sep=True, unpack4sep=False, ignore4body=False, unpack4body=False, /):
        (iu_rgnr8body, iu_rgnr8sep_body, unlock_idx, begin_vs_middle) = _init4sep_xxx_by(rgnr8sep, rgnr8body, _min, ignore4sep, unpack4sep, ignore4body, unpack4body)
        super().__init__(iu_rgnr8body, may_iu_rgnr8sep_body:=iu_rgnr8sep_body, may_iu_rgnr8end:=None, _min, may_max, unlock_idx, begin_vs_middle)
        ls = pop_defaults_([rgnr8sep, rgnr8body, _min, may_max, ignore4sep, unpack4sep, ignore4body, unpack4body], [0, None, True, False, False, False])
        #sf._args4repr = tuple(ls)
        sf._reset4repr(tuple(ls))
check_non_ABC(RecognizerLLoo__sep_by)
#end-class RecognizerLLoo__sep_by(RecognizerLLoo__gsep_end_by):



#RecognizerLLoo__end_by
#RecognizerLLoo__sep_by
#RecognizerLLoo__sep_end_by
#RecognizerLLoo__between
#    RecognizerLLoo__unbox_tuple








class IRecognizerLLoo__solo_child6env__init(IRecognizerLLoo__solo_child6env, _Base4repr):
    ___no_slots_ok___ = True
    def __init__(sf, rgnr, /):
        check_type_le(IRecognizerLLoo, rgnr)
        sf._r = rgnr
        #sf._args4repr = (rgnr,)
        sf._reset4repr((rgnr,))
    @override
    def _get_the_cached_child6env_(sf, env, /):
        '-> IRecognizerLLoo # [must be persistent obj, twice yield same obj][may saved into env.external_cache]'
        return sf._r

class IRecognizerLLoo__two_children6env__init(IRecognizerLLoo__two_children6env, _Base4repr):
    ___no_slots_ok___ = True
    def __init__(sf, rgnr0, rgnr1, /):
        check_type_le(IRecognizerLLoo, rgnr0)
        check_type_le(IRecognizerLLoo, rgnr1)
        sf._rs = rgnr0, rgnr1
        #sf._args4repr = (rgnr0, rgnr1)
        sf._reset4repr((rgnr0, rgnr1))
    @override
    def _get_the_two_cached_children6env_(sf, env, /):
        '-> (IRecognizerLLoo, IRecognizerLLoo) # [must be persistent obj, twice yield same obj][may saved into env.external_cache]'
        return sf._rs







class IRecognizerLLoo__alias(IRecognizerLLoo__solo_child6env):
    'alias a complex rgnr_expr'
    __slots__ = ()
    @override
    def _mk_gi4recognize_(sf, env, xctx_view, unlocker, ignore:bool, istream, /):
        rgnr = sf._get_the_cached_child6env_(env)
        reply = yield mk_Call_(rgnr, unlocker, ignore, istream)
        return reply

class IHasAttr__force_postprocess_when_ignore(ABC):
    __slots__ = ()
    @property
    @abstractmethod
    def _force_postprocess_when_ignore_(sf, /):
        '-> bool'

class IRecognizerLLoo__gprepostprocess(IRecognizerLLoo__solo_child6env, IHasAttr__force_postprocess_when_ignore):
    #IRecognizerLLoo__wrap-->IRecognizerLLoo__gprepostprocess
    __slots__ = ()
    #_force_postprocess_when_ignore_ = False
    #@property
    #@abstractmethod
    #def _force_postprocess_when_ignore_(sf, /):
    #    '-> bool'
    @property
    @abstractmethod
    def _may_gpreprocess_(sf, /):
        '-> may gpreprocess/(rgnr->env->xctx_view->ignore->ext_info8begin->(st, may ignore)) #donot affect reply.ok'
    @property
    @abstractmethod
    def _may_gpostprocess6err_(sf, /):
        '-> may gpostprocess6err/(rgnr->env->xctx_view->ignore->st->ext_info8end->errmsg->errmsg) #donot affect reply.ok'
    @property
    @abstractmethod
    def _may_gpostprocess6ok_(sf, /):
        '-> may gpostprocess6ok/(rgnr->env->xctx_view->ignore->st->ext_info8end->oresult->oresult) #donot affect reply.ok'

    @override
    def _mk_gi4recognize_(sf, env, xctx_view, unlocker, ignore:bool, istream, /):
        rgnr = sf._get_the_cached_child6env_(env)
        if not ignore or sf._force_postprocess_when_ignore_:
            (st, ignore) = apply_may_gpreprocess_(sf._may_gpreprocess_, rgnr, env, xctx_view, ignore, istream)

        reply = yield mk_Call_(rgnr, unlocker, ignore, istream)

        if not ignore or sf._force_postprocess_when_ignore_:
            reply = apply_may_gpostprocess_(sf._may_gpostprocess6err_, sf._may_gpostprocess6ok_, reply, rgnr, env, xctx_view, ignore, st)
        return reply

class IRecognizerLLoo__spostprocess(IRecognizerLLoo__solo_child6env, IHasAttr__force_postprocess_when_ignore):
    __slots__ = ()
    #_force_postprocess_when_ignore_ = False
    #@property
    #@abstractmethod
    #def _force_postprocess_when_ignore_(sf, /):
    #    '-> bool'
    @property
    @abstractmethod
    def _may_spostprocess6err_(sf, /):
        '-> may spostprocess6err/(errmsg->errmsg) #donot affect reply.ok'
    @property
    @abstractmethod
    def _may_spostprocess6ok_(sf, /):
        '-> may spostprocess6ok/(oresult->oresult) #donot affect reply.ok'

    @override
    def _mk_gi4recognize_(sf, env, xctx_view, unlocker, ignore:bool, istream, /):
        rgnr = sf._get_the_cached_child6env_(env)
        reply = yield mk_Call_(rgnr, unlocker, ignore, istream)

        if (not ignore or sf._force_postprocess_when_ignore_):
            reply = apply_may_spostprocess_(reply, sf._may_spostprocess6err_, sf._may_spostprocess6ok_)
        return reply

def apply_may_spostprocess_(reply, mspost6err_, mspost6ok_, /):
    reply = reply.ireplace(eresult=reply.eresult.fmap4either(mspost6err_, mspost6ok_))
    return reply

class IRecognizerLLoo__tag(IRecognizerLLoo__solo_child6env):
    'used as child_rgnr/branch of priority_parallel #no matter whether ignore'
    __slots__ = ()
    @property
    @abstractmethod
    def _tag_(sf, /):
        '-> tag'
    @override
    def _mk_gi4recognize_(sf, env, xctx_view, unlocker, ignore:bool, istream, /):
        rgnr = sf._get_the_cached_child6env_(env)
        reply = yield mk_Call_(rgnr, unlocker, ignore, istream)
        if reply.ok:
            reply = reply.ireplace(eresult=mk_Right(Cased(sf._tag_, reply.oresult)))
                #no matter whether ignore
        return reply





class IRecognizerLLoo__alias__init(IRecognizerLLoo__solo_child6env__init, IRecognizerLLoo__alias):pass
class BaseRecognizerLLoo__alias__default_mixins(IRecognizerLLoo__alias__init, IRecognizerLLoo__default_mixins):pass
check_non_ABC(BaseRecognizerLLoo__alias__default_mixins)

def check_may_callable(x, /):
    if not x is None:
        check_callable(x)
class IRecognizerLLoo__gprepostprocess__init(IRecognizerLLoo__solo_child6env__init, IRecognizerLLoo__gprepostprocess):
    #___no_slots_ok___ = True
    def __init__(sf, rgnr, _may_gpreprocess_, _may_gpostprocess6err_, _may_gpostprocess6ok_, _force_postprocess_when_ignore_=False, /):
        check_type_le(IRecognizerLLoo, rgnr)
        check_may_callable(_may_gpreprocess_)
        check_may_callable(_may_gpostprocess6err_)
        check_may_callable(_may_gpostprocess6ok_)
        check_type_is(bool, _force_postprocess_when_ignore_)

        super().__init__(rgnr)
        sf._mpre = _may_gpreprocess_
        sf._mgpost6err = _may_gpostprocess6err_
        sf._mgpost6ok = _may_gpostprocess6ok_
        sf._b_force = _force_postprocess_when_ignore_

        args = (rgnr, _may_gpreprocess_, _may_gpostprocess6err_, _may_gpostprocess6ok_, _force_postprocess_when_ignore_)
        #sf._args4repr = args if _force_postprocess_when_ignore_ else args[:-1]
        sf._reset4repr(args if _force_postprocess_when_ignore_ else args[:-1])
    @property
    @override
    def _force_postprocess_when_ignore_(sf, /):
        '-> bool'
        return sf._b_force

    @property
    @override
    def _may_gpreprocess_(sf, /):
        '-> may gpreprocess/(rgnr->env->xctx_view->ignore->ext_info8begin->(st, may ignore)) #donot affect reply.ok'
        return sf._mpre
    @property
    @override
    def _may_gpostprocess6err_(sf, /):
        '-> may gpostprocess6err/(rgnr->env->xctx_view->ignore->st->ext_info8end->errmsg->errmsg) #donot affect reply.ok'
        return sf._mgpost6err
    @property
    @override
    def _may_gpostprocess6ok_(sf, /):
        '-> may gpostprocess6ok/(rgnr->env->xctx_view->ignore->st->ext_info8end->oresult->oresult) #donot affect reply.ok'
        return sf._mgpost6ok

class RecognizerLLoo__gprepostprocess(IRecognizerLLoo__gprepostprocess__init, IRecognizerLLoo__default_mixins):pass
check_non_ABC(RecognizerLLoo__gprepostprocess)


class IRecognizerLLoo__spostprocess__init(IRecognizerLLoo__solo_child6env__init, IRecognizerLLoo__spostprocess):
    def __init__(sf, rgnr, _may_spostprocess6err_, _may_spostprocess6ok_, _force_postprocess_when_ignore_=False, /):
        check_type_le(IRecognizerLLoo, rgnr)
        check_may_callable(_may_spostprocess6err_)
        check_may_callable(_may_spostprocess6ok_)
        check_type_is(bool, _force_postprocess_when_ignore_)

        super().__init__(rgnr)

        sf._mspost6err = _may_spostprocess6err_
        sf._mspost6ok = _may_spostprocess6ok_
        sf._b_force = _force_postprocess_when_ignore_

        args = (rgnr, _may_spostprocess6err_, _may_spostprocess6ok_, _force_postprocess_when_ignore_)
        #sf._args4repr = args if _force_postprocess_when_ignore_ else args[:-1]
        sf._reset4repr(args if _force_postprocess_when_ignore_ else args[:-1])
    @property
    @override
    def _force_postprocess_when_ignore_(sf, /):
        '-> bool'
        return sf._b_force
    @property
    @override
    def _may_spostprocess6err_(sf, /):
        '-> may spostprocess6err/(errmsg->errmsg) #donot affect reply.ok'
        return sf._mspost6err
    @property
    @override
    def _may_spostprocess6ok_(sf, /):
        '-> may spostprocess6ok/(oresult->oresult) #donot affect reply.ok'
        return sf._mspost6ok
class RecognizerLLoo__spostprocess(IRecognizerLLoo__spostprocess__init, IRecognizerLLoo__default_mixins):pass
check_non_ABC(RecognizerLLoo__spostprocess)

class IRecognizerLLoo__tag__init(IRecognizerLLoo__solo_child6env__init, IRecognizerLLoo__tag):
    def __init__(sf, rgnr, tag, /):
        #check_type_le(IRecognizerLLoo, rgnr)
        super().__init__(rgnr)
        #sf._args4repr = (rgnr, tag)
        sf._reset4repr((rgnr, tag))
        sf._tag = tag
    @property
    @override
    def _tag_(sf, /):
        '-> tag'
        return sf._tag
class RecognizerLLoo__tag(IRecognizerLLoo__tag__init, IRecognizerLLoo__default_mixins):pass
check_non_ABC(RecognizerLLoo__tag)
def tag_rgnr_(tag, rgnr, /):
    'tag -> IRecognizerLLoo -> IRecognizerLLoo__tag'
    return RecognizerLLoo__tag(rgnr, tag)






_wd = get_weak_symbolize_register4sexconfigpack_(forbid_xxx_protected_ok)
class RecognizerLLoo__light_wrap(IRecognizerLLoo__solo_child6env__init, IRecognizerLLoo__default_mixins):
    'builtin_support:light_wrap_rgnr_() #[postprocess no matter whether ignore] #[to avoid: _iter_persistent_children6env_ --> [rgnr, try_rgnr_(rgnr)...]@RecognizerLLoo__repetition]'
    def __init__(sf, rgnr, symbol8sexconfigpack, may_info4mk_gi, /):
        sf._pk = sexconfigpack = _wd.lookup(symbol8sexconfigpack)
        sf._sym = symbol8sexconfigpack
        sf._m = may_info4mk_gi
        super().__init__(rgnr)
        #sf._args4repr = (rgnr, symbol8sexconfigpack, may_info4mk_gi)
        sf._reset4repr((rgnr, symbol8sexconfigpack, may_info4mk_gi))
        sf._br = rgnr._get_the_base_rgnr_()
            # => hard to impl '_get_the_base_rgnr6env_'
            # => _get_the_base_rgnr6env_ --> _get_the_base_rgnr_
    @override
    def _get_the_base_rgnr_(sf, /):
        return sf._br
    @override
    def _mk_gi4recognize_(sf, env, xctx_view, unlocker, ignore:bool, istream, /):
        rgnr = sf._get_the_cached_child6env_(env)
        sexconfigpack = sf._pk
        #symbol8sexconfigpack = sf._sym
        may_info4mk_gi = sf._m
        info4mk_gi = ifNone(may_info4mk_gi, default_info4mk_gi)
        (may_ignore, to_lift, may_spostprocess6err, may_spostprocess6ok, to_invert_ok_err) = info4mk_gi
        if not may_ignore is None:
            ignore = may_ignore
        #def mk_gi4IRecognizerLLoo__5solo_rgnr_transform_cases_(mk_Call_, to_lift:bool, good_sexconfigpack:'sexconfigpack{good}', rgnr, unlocker, ignore, istream, /, *, case_vs_sym_vs_uint:'may bool', forbid_xxx_protected_ok:False):
        reply = yield _mk_wrapped_gi(mk_Call_, to_lift, sexconfigpack, rgnr, unlocker, ignore, istream, case_vs_sym_vs_uint=False, forbid_xxx_protected_ok=forbid_xxx_protected_ok)
            # donot use 『yield from』
        reply = apply_may_spostprocess_(reply, may_spostprocess6err, may_spostprocess6ok)
            #no matter whether ignore
        #only:not_followed_by invert_ok_err
        #   but:already hardcoded in sconfigpack
        # to_invert_ok_err is part of postprocess
        #   but:the only one invert_ok_err must be not_followed_by, therefore to_invert_ok_err is useless
        if to_invert_ok_err: raise 000-'to_invert_ok_err-useless'
        return reply
        ######################
        #.if to_invert_ok_err:

        #.    #old_ok = reply.ok
        #.    reply = reply.ireplace(eresult=~reply.eresult)
        #.    #assert old_ok is not reply.ok
        #.return reply
        ######################
check_non_ABC(RecognizerLLoo__light_wrap)





class IRecognizerLLoo__repetition__init(IRecognizerLLoo__two_children6env__init, IRecognizerLLoo__repetition):
    @override
    def __init__(sf, rgnr, _min, may_max, unlock_idx, begin_vs_middle:bool, ignore:bool, unpack:bool, /):
        check_type_is(bool, unpack)
        check_type_is(bool, ignore)
        check_type_is(bool, begin_vs_middle)
        #check_int_ge(0, _min)
        check_int_ge(0, unlock_idx)
        check_int_ge(unlock_idx, _min)
        if not may_max is None:
            check_int_ge(_min, may_max)
        sf._rp_args = (_min, may_max, unlock_idx, begin_vs_middle, ignore, unpack)
        super().__init__(rgnr, rgnr8trial:=trial_and_error_(rgnr))
        #sf._args4repr = (rgnr, _min, may_max, unlock_idx, begin_vs_middle, ignore, unpack)
        sf._reset4repr((rgnr, _min, may_max, unlock_idx, begin_vs_middle, ignore, unpack))
    @override
    def _get_repetition_args6env_(sf, env, /):
        '-> repetition_args/(min, may_max, unlock_idx, begin_vs_middle, ignore, unpack)/(uint, may uint, unit, bool, bool, bool)'
        return sf._rp_args


class IRecognizerLLoo__forgivable_fail_ok__solo_child6env__init(IRecognizerLLoo__solo_child6env__init, IHasAttr__forgivable_fail_be_ok):
    @override
    def __init__(sf, rgnr, _forgivable_fail_be_ok_:bool, /):
        check_type_is(bool, _forgivable_fail_be_ok_)
        sf._fgv_ok = _forgivable_fail_be_ok_
        super().__init__(rgnr)
    @property
    @override
    def _forgivable_fail_be_ok_(sf, /):
        '-> bool'
        return sf._fgv_ok

r"""[[[
def try_rgnr_(rgnr, /):
    return trial_and_error_(rgnr)
.def try_rgnr_(rgnr, /):
.    if not type(rgnr) is RecognizerLLoo__try:
.        rgnr = RecognizerLLoo__try(rgnr)
.    return rgnr
.class IRecognizerLLoo__lift__init(IRecognizerLLoo__forgivable_fail_ok__solo_child6env__init, IRecognizerLLoo__lift):pass
.class IRecognizerLLoo__optional__init(IRecognizerLLoo__forgivable_fail_ok__solo_child6env__init, IRecognizerLLoo__optional):pass
.
.class RecognizerLLoo__lift(IRecognizerLLoo__lift__init, IRecognizerLLoo__default_mixins):pass
.check_non_ABC(RecognizerLLoo__lift)
.class RecognizerLLoo__optional(IRecognizerLLoo__optional__init, IRecognizerLLoo__default_mixins):pass
.check_non_ABC(RecognizerLLoo__optional)
.class RecognizerLLoo__try(IRecognizerLLoo__try, IRecognizerLLoo__solo_child6env__init, IRecognizerLLoo__default_mixins):pass
.check_non_ABC(RecognizerLLoo__try)
.class RecognizerLLoo__lookahead(IRecognizerLLoo__lookahead, IRecognizerLLoo__solo_child6env__init, IRecognizerLLoo__default_mixins):pass
.check_non_ABC(RecognizerLLoo__lookahead)
.##class RecognizerLLoo__flip(IRecognizerLLoo__flip, IRecognizerLLoo__solo_child6env__init, IRecognizerLLoo__default_mixins):pass
.##check_non_ABC(RecognizerLLoo__flip)
#]]]"""#"""

class RecognizerLLoo__repetition(IRecognizerLLoo__repetition__init, IRecognizerLLoo__default_mixins):pass
    #'RecognizerLLoo__many vs RecognizerLLoo__repetition'
    #[mixins later]<<==_is_ctx_scope_ = True
check_non_ABC(RecognizerLLoo__repetition)
#cancel:assert RecognizerLLoo__repetition._is_ctx_scope_ is True
assert RecognizerLLoo__repetition._is_ctx_scope_ is False

class IRecognizerLLoo__init__rgnrs(IRecognizerLLoo, _Base4repr):
    ___no_slots_ok___ = True
    def __init__(sf, rgnrs, /):
        rgnrs = mk_tuple(rgnrs)
        for rgnr in rgnrs:
            check_type_le(IRecognizerLLoo, rgnr)
        sf._rs = rgnrs
        #sf._args4repr = (rgnrs,)
        sf._reset4repr((rgnrs,))
    @property
    def _rgnrs_(sf, /):
        '-> [IRecognizerLLoo]'
        return sf._rs
class RecognizerLLoo__priority_parallel(IRecognizerLLoo__init__rgnrs, IRecognizerLLoo__priority_parallel, IRecognizerLLoo__default_mixins):
    @override
    def _iter_priority_parallel_children_(sf, env, /):
        '-> Iter IRecognizerLLoo # [must be finite][must be persistent obj, twice yield same obj][may saved into env.external_cache]'
        return iter(sf._rgnrs_)
check_non_ABC(RecognizerLLoo__priority_parallel)

def mk_casedT_(tag, /):
    'vs:mk_Left,mk_Right'
    def mk_cased_(x, /):
        return Cased(tag, x)
    return mk_cased_
def unbox(xs, /):
    [x] = xs
    return x
class IRecognizerLLoo__spostprocess__init__default_mixins(IRecognizerLLoo__solo_child6env__init, IRecognizerLLoo__spostprocess, IRecognizerLLoo__default_mixins):
    # ++sf._force_postprocess_when_ignore_ <<== RecognizerLLoo__unbox_tuple using RecognizerLLoo__spost__unbox
    #@override
    #_force_postprocess_when_ignore_ = False
    #@override
    _may_spostprocess6err_ = None
    def __init__(sf, rgnr, /, _force_postprocess_when_ignore_=False):
        check_type_is(bool, _force_postprocess_when_ignore_)
        super().__init__(rgnr)
        sf._b_force = _force_postprocess_when_ignore_
        if _force_postprocess_when_ignore_:
            #sf._args4repr = (rgnr, _force_postprocess_when_ignore_)
            sf._reset4repr((rgnr, _force_postprocess_when_ignore_))
    @property
    @override
    def _force_postprocess_when_ignore_(sf, /):
        '-> bool'
        return sf._b_force
class IRecognizerLLoo__spostprocess__init__default_mixins__static(IRecognizerLLoo__spostprocess__init__default_mixins):
    @classmethod
    @abstractmethod
    def _spostprocess6ok_(cls, oresult, /):
        'oresult -> oresult #donot affect reply.ok'
    @property
    @override
    def _may_spostprocess6ok_(sf, /):
        return type(sf)._spostprocess6ok_
#class RecognizerLLoo__spost__unbox(BaseRecognizerLLoo__alias__default_mixins):
#    'unbox:used in unbox_tuple'
#    def __init__(sf, rgnr, /):
#        super().__init__(RecognizerLLoo__spostprocess(rgnr, None, unbox))
#        #sf._args4repr = (rgnr,)
#        sf._reset4repr((rgnr,))
class RecognizerLLoo__spost__unbox(IRecognizerLLoo__spostprocess__init__default_mixins__static):
    'unbox:used in unbox_tuple'
    #@override
    _spostprocess6ok_ = unbox

class RecognizerLLoo__unbox_tuple(BaseRecognizerLLoo__alias__default_mixins):
    'unbox_tuple:used in {sep_by,between}'
    #==>>required:_not_ignore_toplvl_,_force_postprocess_when_ignore_
    #   if not _not_ignore_toplvl_:[None==oresult<RecognizerLLoo__serial>]
    #   if not _force_postprocess_when_ignore_:[not take action: spostprocess6ok<RecognizerLLoo__spost__unbox>]
    #
    def __init__(sf, unbox_idx, unlock_idx, begin_vs_middle, rgnrs, /):
        rgnrs = mk_tuple(rgnrs)
        L = len(rgnrs)
        check_int_ge_lt(0, L, unbox_idx)
        check_int_ge_le(0, L, unlock_idx)
        check_type_is(bool, begin_vs_middle)
        check_int_ge_le(0, L, unlock_idx+begin_vs_middle)

        rgnr = RecognizerLLoo__serial(unlock_idx, begin_vs_middle, [(rgnr, int(j==unbox_idx), 0) for j, rgnr in enumerate(rgnrs)], _not_ignore_toplvl_=True)
            # 0,1 <<== [unpack_case :: (0/ignore|1/ignorable_normal|2/ignorable_unpack|-1/non_ignorable_normal|-2/non_ignorable_unpack)]
            # 0 <<== [fail_vs_stop_vs_continue :: {0,1,2}]
        super().__init__(RecognizerLLoo__spost__unbox(rgnr, _force_postprocess_when_ignore_=True))
        #sf._args4repr = (unbox_idx, unlock_idx, begin_vs_middle, rgnrs)
        sf._reset4repr((unbox_idx, unlock_idx, begin_vs_middle, rgnrs))
class RecognizerLLoo__between(RecognizerLLoo__unbox_tuple):
    'between'
    def __init__(sf, rgnr8open, rgnr8close, rgnr8body, /):
        #bug:rgnrs = (rgnr8open, rgnr8close, rgnr8body)
        rgnrs = (rgnr8open, rgnr8body, rgnr8close)
        super().__init__(1, 0, True, rgnrs)
        #bug:sf._args4repr = rgnrs
        #sf._args4repr = (rgnr8open, rgnr8close, rgnr8body)
        sf._reset4repr((rgnr8open, rgnr8close, rgnr8body))
check_non_ABC(RecognizerLLoo__spost__unbox)
check_non_ABC(RecognizerLLoo__unbox_tuple)
check_non_ABC(RecognizerLLoo__between)
class RecognizerLLoo__serial(IRecognizerLLoo__serial, IRecognizerLLoo__default_mixins, _Base4repr):
    #[mixins later]<<==_is_ctx_scope_ = True
    r'''[[[
    'serial-rgnr'

    ######################
    RecognizerLLoo__serial.__init__():
        # ++_not_ignore_toplvl_ <<== RecognizerLLoo__unbox_tuple

        * '() -> None'
        * 'Iter (begin_vs_middle/bool|rgnr|(rgnr, ?unpack_case/[-2..=+2], ?fail_vs_stop_vs_continue/[0..=2])) -> None'
        * 'unlock_idx -> begin_vs_middle -> Iter (rgnr, unpack_case/[-2..=+2], fail_vs_stop_vs_continue/[0..=2]) -> None'
    ######################
    typing:
    serial-rgnr:
        [unlock_case :: (may begin_vs_middle/bool)]
            unlock_case = mk_unlock_case(unlock_idx, begin_vs_middle, k)
        [unpack_case :: (0/ignore|1/ignorable_normal|2/ignorable_unpack|-1/non_ignorable_normal|-2/non_ignorable_unpack)]
            explain_unpack_case_with_()
            explain_unpack_case()
        [fail_vs_stop_vs_continue :: {0,1,2}]
        [var_changed :: BoolVar{monotonic_idx8begin.changed}]
        [var_ok :: BoolVar{reply.ok}]
        [fail_vs_stop_vs_continue:when not reply.ok and not monotonic_idx8begin.changed=>fail-or-stop{ok}-continue{serial}]
    ######################


    #]]]'''#'''
    ___no_slots_ok___ = True
    def __init__(sf, /, *args, _not_ignore_toplvl_=False):
        r'''[[[

        * '() -> None'
        * 'Iter (begin_vs_middle/bool|rgnr|(rgnr, ?unpack_case/[-2..=+2], ?fail_vs_stop_vs_continue/[0..=2])) -> None'
        * 'unlock_idx -> begin_vs_middle -> Iter (rgnr, unpack_case/[-2..=+2], fail_vs_stop_vs_continue/[0..=2]) -> None'

        #]]]'''#'''
        ######################
        check_type_is(bool, _not_ignore_toplvl_)
            # ++_not_ignore_toplvl_ <<== RecognizerLLoo__unbox_tuple
        if _not_ignore_toplvl_:
            sf._kwds4repr = dict(_not_ignore_toplvl_=_not_ignore_toplvl_)
        sf._keep_tpl = _not_ignore_toplvl_
        ######################

        ######################
        L = len(args)
        if L == 2 or L > 3:raise TypeError
        if L == 0:
            sf._init4null()
        if L == 1:
            sf._init4list(*args)
        else:
            sf._init4std_args(*args)
        ######################
        #sf._reset4repr(sf._args4repr, sf._kwds4repr)
    def _init4null(sf, /):
        '() -> None'
        sf._init4list([])
        sf._args4repr = ()
        #sf._reset4repr(sf._args4repr, sf._kwds4repr)

    def _init4list(sf, xs, /):
        'Iter (begin_vs_middle/bool|(rgnr, ?unpack_case/[-2..=+2], ?fail_vs_stop_vs_continue/[0..=2])) -> None'
        xs = mk_tuple(xs)
        def mk(rgnr, a:'unpack_case:=ignorable_normal'=1, b:'fail_vs_stop_vs_continue:=fail'=0, /):
            return (rgnr, a, b)
        unlock_idx = Nothing = object()
        ls = []
        for x in xs:
            T = type(x)
            if T is tuple:
                x = mk(*x)
            elif T is bool:
                if unlock_idx is Nothing:
                    unlock_idx = len(ls)
                    begin_vs_middle = x
                continue
            elif isinstance(x, IRecognizerLLoo):
                x = mk(x)
            else:
                raise TypeError(T)
            x
            ls.append(x)
        if unlock_idx is Nothing:
            #whole8header
            unlock_idx = len(ls)
            begin_vs_middle = False
        sf._init4std_args(unlock_idx, begin_vs_middle, ls)
        sf._args4repr = (xs,)
        #sf._reset4repr(sf._args4repr, sf._kwds4repr)
    def _init4std_args(sf, unlock_idx, begin_vs_middle, rgnr__unpack_case__fail_vs_stop_vs_continue__triples, /):
        'unlock_idx -> begin_vs_middle -> Iter (rgnr, unpack_case/[-2..=+2], fail_vs_stop_vs_continue/[0..=2]) -> None'
        check_int_ge(0, unlock_idx)
        check_type_is(bool, begin_vs_middle)
        ts = mk_tuple(rgnr__unpack_case__fail_vs_stop_vs_continue__triples)
        for x in ts:
            check_type_is(tuple, x)
            (rgnr, unpack_case, fail_vs_stop_vs_continue) = x
            check_type_le(IRecognizerLLoo, rgnr)
            check_int_ge_lt(-2, 3, unpack_case)
            check_int_ge_lt(0, 3, fail_vs_stop_vs_continue)
        sf._ts = ts
        sf._unlock_args = (unlock_idx, begin_vs_middle)
        sf._args4repr = (unlock_idx, begin_vs_middle, ts)
        #sf._reset4repr(sf._args4repr, sf._kwds4repr)
    @property
    def unlock_args(sf, /):
        '-> (unlock_idx, begin_vs_middle)/(uint, bool)'
        return sf._unlock_args
    @property
    def input_triples(sf, /):
        '-> [(IRecognizerLLoo, unpack_case/[-2..=+2], fail_vs_stop_vs_continue/[0..=2])]'
        return sf._ts

    @property
    @override
    def _not_ignore_toplvl_(sf, /):
        '-> bool #true-tuple, not ignore the top-level tuple # required by RecognizerLLoo__unbox_tuple'
        return sf._keep_tpl
    @override
    def _iter_persistent_children6env_(sf, env, /):
        '-> Iter IRecognizerLLoo # [must be finite][must be persistent obj, twice yield same obj][may saved into env.external_cache]'
        return map(fst, sf._ts)
    @override
    def _iter_runtime_serial_children_(sf, env, xctx_view, ignore:bool, var_changed, var_ok, var_reply, /):
        (unlock_idx, begin_vs_middle) = sf._unlock_args
        k = 0
        #_not_ignore_toplvl_ = to_keep_tpl = sf._not_ignore_toplvl_
        #ignore4outer = ignore and not to_keep_tpl
        for (rgnr, unpack_case, fail_vs_stop_vs_continue) in (sf._ts):
            #enumerate
            unlock_case = mk_unlock_case(unlock_idx, begin_vs_middle, k)
            #old:(ignore4inner, unpack) = explain_unpack_case_with_(ignore, unpack_case)
            (ignore4outer, ignore4inner, unpack) = explain_unpack_case_with_(ignore, unpack_case)
            yield (ignore4outer, rgnr, unlock_case, ignore4inner, unpack, fail_vs_stop_vs_continue)
            #if var_ok:
            #    k += 1
            k += 1 # see: ._init4list
check_non_ABC(RecognizerLLoo__serial)
#cancel:assert RecognizerLLoo__serial._is_ctx_scope_ is True
assert RecognizerLLoo__serial._is_ctx_scope_ is False

class IRecognizerLLoo__dependent_pair__spost(BaseRecognizerLLoo__alias__default_mixins):
    @classmethod
    @abstractmethod
    def _spostprocess6ok4dependent_pair_(cls, oresult4dependent_pair, /):
        'oresult/(a,b) -> oresult #donot affect reply.ok'
    def __init__(sf, rgnr8case, case2rgnr8payload, may_rgnr8default_payload=None, /):
        rgnr8pair = RecognizerLLoo__dependent_pair(rgnr8case, case2rgnr8payload, may_rgnr8default_payload)
        rgnr8payload = RecognizerLLoo__spostprocess(rgnr8pair, None, type(sf)._spostprocess6ok4dependent_pair_, sf._force_postprocess_when_ignore_)
            # !! ++Output__oresult
        super().__init__(rgnr8payload)
        #sf._args4repr = rgnr8pair._args4repr
        sf._reset4repr(rgnr8pair._args4repr)

def pair2Cased_(pair, /):
    (a, b) = pair
    return Cased(a, b)
class RecognizerLLoo__switch_cased(IRecognizerLLoo__dependent_pair__spost):
    'switch_cased'
    #@override
    _spostprocess6ok4dependent_pair_ = pair2Cased_
    #@override
    _force_postprocess_when_ignore_ = True
        # !! ++Output__oresult
class RecognizerLLoo__switch_branches(IRecognizerLLoo__dependent_pair__spost):
    'switch_branches'
    #@override
    _spostprocess6ok4dependent_pair_ = snd
    #@override
    _force_postprocess_when_ignore_ = True
        # !! ++Output__oresult

class RecognizerLLoo__dependent_pair(IRecognizerLLoo__serial, IRecognizerLLoo__default_mixins, _Base4repr):
    'dependent_pair'
    #==>>required:(_not_ignore_toplvl_|Output__oresult)
    ___no_slots_ok___ = True
    #@override
    _not_ignore_toplvl_ = True
    def __init__(sf, rgnr8case, case2rgnr8payload, may_rgnr8default_payload=None, /):
        check_type_le(IRecognizerLLoo, rgnr8case)
        check_may_IRecognizerLLoo(may_rgnr8default_payload)
        case2rgnr8payload = mk_FrozenDict(case2rgnr8payload)
        for case, rgnr8payload in case2rgnr8payload.items():
            check_type_le(IRecognizerLLoo, rgnr8payload)
        args = (rgnr8case, case2rgnr8payload, may_rgnr8default_payload)
        #sf._args4repr = args if not may_rgnr8default_payload is None else args[:-1]
        sf._reset4repr(args if not may_rgnr8default_payload is None else args[:-1])
        sf._r_d_r = args
    @override
    def _iter_persistent_children6env_(sf, env, /):
        (rgnr8case, case2rgnr8payload, may_rgnr8default_payload) = sf._r_d_r
        yield rgnr8case
        yield from case2rgnr8payload.values()
        if not may_rgnr8default_payload is None:
            rgnr8default_payload = may_rgnr8default_payload
            yield rgnr8default_payload
        return
    @override
    def _iter_runtime_serial_children_(sf, env, xctx_view, ignore:bool, var_changed, var_ok, var_reply, /):
        '-> Iter (ignore4outer/bool, IRecognizerLLoo, unlock_case/(may begin_vs_middle/bool), ignore4inner/bool, unpack/bool, fail_vs_stop_vs_continue/{0,1,2})'
        (rgnr8case, case2rgnr8payload, may_rgnr8default_payload) = sf._r_d_r
        yield (False, rgnr8case, True, False, False, 0)
            #no matter whether ignore
        reply = var_reply.x
        case = reply.oresult
            # not ignored
        may_rgnr8payload = case2rgnr8payload.get(case, may_rgnr8default_payload)
        if may_rgnr8payload is None: raise LookupError(case)
        rgnr8payload = may_rgnr8payload
        yield (False, rgnr8payload, False, ignore, False, 0)
            # maybe ignored
        return
        ######################
        #before:++_not_ignore_toplvl_
        ######################
        if ignore:
            reply = var_reply.x
            payload = reply.oresult
                # maybe ignored
            #######
            case
                # not ignored
            payload
                # maybe ignored
            oresult = (case, payload)
                # half ignored
            var_reply.x = Output__oresult(oresult)
        return
class Output__oresult:
    'used in IRecognizerLLoo__serial._iter_runtime_serial_children_ to output oresult var_reply instead of default oresult which is tuple'
    def __init__(sf, oresult, /):
        sf._x = oresult
    def get_oresult(sf, /):
        return sf._x
class RecognizerLLoo__try_except_else(IRecognizerLLoo__default_mixins, IHasAttr__force_postprocess_when_ignore, _Base4repr):
    r'''[[[
    'try_except_else #if_then_else'

    [a := oresult<rgnr8trial>]
    [e := oresult<rgnr8except>]
    [b := oresult<rgnr8else>]

    # tmay a -> Either e (a,b)
        # [not postprocess] => [oresult :: Either (oresult4except) (oresult4trial, oresult4else)]

    [_may_spostprocess6ok6except_ :: e -> ee]
    [_may_spostprocess6ok6trial_else_ :: (a,b) -> ab]
    [oresult :: Either ee ab]


    #]]]'''#'''
    ___no_slots_ok___ = True
    ######################
    #API:
    #@property
    #@abstractmethod
    #def _force_postprocess_when_ignore_(sf, /):
    #    '-> bool'
    @property
    @abstractmethod
    def _may_spostprocess6ok6except_(sf, /):
        'oresult<rgnr8except> -> oresult<rgnr8self>.left'
    @property
    @abstractmethod
    def _may_spostprocess6ok6trial_else_(sf, /):
        '(oresult<rgnr8trial>, oresult<rgnr8else>) -> oresult<rgnr8self>.right'
    ######################
    #@override
    _force_postprocess_when_ignore_ = False
    #@override
    _may_spostprocess6ok6except_ = None
    #@override
    _may_spostprocess6ok6trial_else_ = None
    ######################
    def __init__(sf, rgnr8trial, rgnr8except, rgnr8else, strict_vs_forgivable=False, /):
        check_type_le(IRecognizerLLoo, rgnr8trial)
        check_type_le(IRecognizerLLoo, rgnr8except)
        check_type_le(IRecognizerLLoo, rgnr8else)
        check_type_is(bool, strict_vs_forgivable)

        args = (rgnr8trial, rgnr8except, rgnr8else, strict_vs_forgivable)
        #sf._args4repr = args if strict_vs_forgivable else args[:-1]
        sf._reset4repr(args if strict_vs_forgivable else args[:-1])
        sf._r3_b = args
        nm4info_ex4mk_gi = 'optional__strict' if not strict_vs_forgivable else 'optional__forgivable'
        exargs4lwrap = (nm4info_ex4mk_gi,)
        sf._ex4lw = exargs4lwrap
    @override
    def _iter_persistent_children6env_(sf, env, /):
        return iter(sf._r3_b[:3])
    @override
    def _mk_gi4recognize_(sf, env, xctx_view, unlocker, ignore:bool, istream, /):
        exargs4lwrap = sf._ex4lw
        (rgnr8trial, rgnr8except, rgnr8else, strict_vs_forgivable) = sf._r3_b
        #def mk_Call_(rgnr, unlocker, ignore, istream, exargs4lwrap=null_tuple, /):

        reply = yield mk_Call_(rgnr8trial, unlocker, ignore, istream, exargs4lwrap)
        if not reply.ok:
            return reply
        tmay_oresult4trial = reply.oresult
        if tmay_oresult4trial:
            # -> else...
            [oresult4trial] = tmay_oresult4trial
            reply = yield mk_Call_(rgnr8else, dummy_unlocker, ignore, istream)
            if not reply.ok:
                return reply
            oresult4else = reply.oresult
            oresult4trial_else = (oresult4trial, oresult4else)
            oresult = mk_Right(oresult4trial_else)
        else:
            # -> except...
            [] = tmay_oresult4trial
            reply = yield mk_Call_(rgnr8except, unlocker, ignore, istream)
            if not reply.ok:
                return reply
            oresult4except = reply.oresult
            oresult = mk_Left(oresult4except)
        reply, oresult

        if not ignore or sf._force_postprocess_when_ignore_:
            may_spostprocess6ok6except = sf._may_spostprocess6ok6except_
            may_spostprocess6ok6trial_else = sf._may_spostprocess6ok6trial_else_
            oresult = oresult.fmap4either(may_spostprocess6ok6except, may_spostprocess6ok6trial_else)

        reply = reply.ireplace(eresult=mk_Right(oresult))
        return reply
check_non_ABC(RecognizerLLoo__try_except_else)
def apply_may_func_(may_f, x, /):
    'may (x -> x) -> x -> x'
    if not may_f is None:
        f = may_f
        x = f(x)
    return x
class RecognizerLLoo__try_except_else__spost(RecognizerLLoo__try_except_else):
    @property
    @override
    def _force_postprocess_when_ignore_(sf, /):
        '-> bool'
        return sf._b_force
    @property
    @override
    def _may_spostprocess6ok6except_(sf, /):
        'oresult<rgnr8except> -> oresult<rgnr8self>.left'
        return sf._mspost6ok6exc
    @property
    @override
    def _may_spostprocess6ok6trial_else_(sf, /):
        '(oresult<rgnr8trial>, oresult<rgnr8else>) -> oresult<rgnr8self>.right'
        return sf._mspost6ok6trial_else

    def __init__(sf, rgnr8trial, rgnr8except, rgnr8else, strict_vs_forgivable=False, may_spostprocess6ok6except=None, may_spostprocess6ok6trial_else=None, _force_postprocess_when_ignore_=False, /):
        check_may_callable(may_spostprocess6ok6except)
        check_may_callable(may_spostprocess6ok6trial_else)
        check_type_is(bool, _force_postprocess_when_ignore_)

        super().__init__(rgnr8trial, rgnr8except, rgnr8else, strict_vs_forgivable)

        args = (rgnr8trial, rgnr8except, rgnr8else, strict_vs_forgivable, may_spostprocess6ok6except, may_spostprocess6ok6trial_else, _force_postprocess_when_ignore_)
        ls = pop_defaults_([*args], [False, None, None, False])
        #sf._args4repr = args if len(ls) == len(args) else args[:len(ls)]
        sf._reset4repr(args if len(ls) == len(args) else args[:len(ls)])
        #sf._r3_b_m2_b = args
        sf._mspost6ok6exc = may_spostprocess6ok6except
        sf._mspost6ok6trial_else = may_spostprocess6ok6trial_else
        sf._b_force = _force_postprocess_when_ignore_
check_non_ABC(RecognizerLLoo__try_except_else__spost)



class IRecognizerLLoo__no_child6env(IRecognizerLLoo):
    __slots__ = ()
    @override
    def _iter_persistent_children6env_(sf, env, /):
        return
        777;    yield
class IRecognizerLLoo__constant_loader(IRecognizerLLoo__no_child6env):
    'constant_loader #no matter whether ignore'
    __slots__ = ()
    @property
    @abstractmethod
    def _eresult_(sf, /):
        '-> Either errmsg oresult'
    @override
    def _mk_gi4recognize_(sf, env, xctx_view, unlocker, ignore:bool, istream, /):
        eresult = sf._eresult_
            #no matter whether ignore
        ext_info8end = istream.tell_ext_info()
        reply = Reply(eresult, ext_info8end)
        if reply.ok:
            unlocker.unlocker_release()
        return reply
        777;    yield

#.class RecognizerLLoo__constant_loader(IRecognizerLLoo__constant_loader, IRecognizerLLoo__default_mixins, _Base4repr):
#.    ___no_slots_ok___ = True
#.    def __init__(sf, eresult, /):
#.        check_type_is(Either, eresult)
#.        sf._er = eresult
#.        #sf._args4repr = (eresult,)
#.        sf._reset4repr((eresult,))
#.    @property
#.    @override
#.    def _eresult_(sf, /):
#.        '-> Either errmsg oresult'
#.        return sf._er
#.check_non_ABC(RecognizerLLoo__constant_loader)



class IRecognizerLLoo__eof(IRecognizerLLoo__no_child6env):
    __slots__ = ()
    @override
    def _mk_gi4recognize_(sf, env, xctx_view, unlocker, ignore:bool, istream, /):
        ok = istream.eof
        eresult = Either(ok, None if ok else 'not_eof')
        ext_info8end = istream.tell_ext_info()
        reply = Reply(eresult, ext_info8end)
        if reply.ok:
            unlocker.unlocker_release()
        return reply
        777;    yield
class IRecognizerLLoo__not_eof(IRecognizerLLoo__no_child6env):
    __slots__ = ()
    @override
    def _mk_gi4recognize_(sf, env, xctx_view, unlocker, ignore:bool, istream, /):
        ok = not istream.eof
        eresult = Either(ok, None if ok else 'eof')
        ext_info8end = istream.tell_ext_info()
        reply = Reply(eresult, ext_info8end)
        if reply.ok:
            unlocker.unlocker_release()
        return reply
        777;    yield
class IRecognizerLLoo__any_token(IRecognizerLLoo__no_child6env):
    __slots__ = ()
    @override
    def _mk_gi4recognize_(sf, env, xctx_view, unlocker, ignore:bool, istream, /):
        tmay_tkn = istream.read_le(1)
        ok = bool(tmay_tkn)
        may_errmsg = None if ok else 'eof'
        reply = _mk_reply4tkn(unlocker, istream, tmay_tkn, may_errmsg)
        return reply
        777;    yield
class IRecognizerLLoo__token(IRecognizerLLoo__no_child6env):
    __slots__ = ()
    @property
    @abstractmethod
    def _token_qset_(sf, /):
        '-> tkn_qset/ITokenQuerySet'
    @override
    def _mk_gi4recognize_(sf, env, xctx_view, unlocker, ignore:bool, istream, /):
        tmay_tkn = istream.read_le(1)
        ok = bool(tmay_tkn)
        may_errmsg = None if ok else 'eof'
        if ok:
            [tkn] = tmay_tkn
            tkn_qset = sf._token_qset_
            ok = is_good_token_(tkn_qset, tkn)
            if not ok:
                may_errmsg = (tkn_qset, tkn)
        reply = _mk_reply4tkn(unlocker, istream, tmay_tkn, may_errmsg)
        return reply
        777;    yield

def _mk_reply4tkn(unlocker, istream, tmay_tkn, may_errmsg, /):
    ok = may_errmsg is None
    if ok:
        [tkn] = tmay_tkn
        unlocker.unlocker_release()
        eresult = mk_Right(oresult:=tkn)
    else:
        eresult = mk_Left(errmsg:=may_errmsg)
    eresult
    ext_info8end = istream.tell_ext_info()
    reply = Reply(eresult, ext_info8end)
    return reply
def _mk_reply4tkn_seq(unlocker, istream, tkn_seq, may_errmsg, /):
    ok = may_errmsg is None
    if ok:
        unlocker.unlocker_release()
        eresult = mk_Right(oresult:=mk_tuple(tkn_seq))
    else:
        eresult = mk_Left(errmsg:=may_errmsg)
    eresult
    ext_info8end = istream.tell_ext_info()
    reply = Reply(eresult, ext_info8end)
    return reply



class IRecognizerLLoo__token_seq(IRecognizerLLoo__no_child6env):
    __slots__ = ()
    @property
    @abstractmethod
    def _token_qset_seq_(sf, /):
        '-> tkn_qset_seq/[ITokenQuerySet]'
    @override
    def _mk_gi4recognize_(sf, env, xctx_view, unlocker, ignore:bool, istream, /):
        tkn_qset_seq = sf._token_qset_seq_
        L = len(tkn_qset_seq)
        tkn_seq = istream.read_le(L)
        ok = len(tkn_seq) == L
        may_errmsg = None if ok else 'eof'
        if ok:
            ok = all(map(is_good_token_, tkn_qset_seq, tkn_seq))
            if not ok:
                may_errmsg = (tkn_qset_seq, tkn_seq)
        reply = _mk_reply4tkn_seq(unlocker, istream, tkn_seq, may_errmsg)
        return reply
        777;    yield



def tkn2tkd_(tkn, /):
    'IToken -> tkd'
    return tkn.token_keyed_data
def tkn2tkey_(tkn, /):
    'IToken -> tkey'
    return tkn.token_key
def tkn2tdat_(tkn, /):
    'IToken -> tdat'
    return tkn.token_data
def tkd2tkey_(tkd, /):
    'tkd -> tkey # Cased -> case'
    return tkd.case
def tkd2tdat_(tkd, /):
    'tkd -> tdat # Cased -> payload'
    return tkd.payload

class RecognizerLLoo__spost__tkn2tkd(IRecognizerLLoo__spostprocess__init__default_mixins__static):
    #@override
    _spostprocess6ok_ = tkn2tkd_
class RecognizerLLoo__spost__tkn2tkey(IRecognizerLLoo__spostprocess__init__default_mixins__static):
    #@override
    _spostprocess6ok_ = tkn2tkey_
class RecognizerLLoo__spost__tkn2tdat(IRecognizerLLoo__spostprocess__init__default_mixins__static):
    #@override
    _spostprocess6ok_ = tkn2tdat_
class RecognizerLLoo__spost__tkd2tkey(IRecognizerLLoo__spostprocess__init__default_mixins__static):
    #@override
    _spostprocess6ok_ = tkd2tkey_
class RecognizerLLoo__spost__tkd2tdat(IRecognizerLLoo__spostprocess__init__default_mixins__static):
    #@override
    _spostprocess6ok_ = tkd2tdat_


class IRecognizerLLoo__spost__fmap4tuple(IRecognizerLLoo__spostprocess__init__default_mixins__static):
    @classmethod
    @abstractmethod
    def _transform4oresult_element_(cls, oresult_element, /):
        'oresult_element -> oresult_element #donot affect reply.ok'
    @classmethod
    @override
    def _spostprocess6ok_(cls, oresult, /):
        'oresult -> oresult #donot affect reply.ok'
        f = cls._transform4oresult_element_
        oresult = mk_tuple(map(f, oresult))
        return oresult


class RecognizerLLoo__spost__fmap4tuple__tkn2tkd(IRecognizerLLoo__spost__fmap4tuple):
    #@override
    _transform4oresult_element_ = tkn2tkd_
class RecognizerLLoo__spost__fmap4tuple__tkn2tkey(IRecognizerLLoo__spost__fmap4tuple):
    #@override
    _transform4oresult_element_ = tkn2tkey_
class RecognizerLLoo__spost__fmap4tuple__tkn2tdat(IRecognizerLLoo__spost__fmap4tuple):
    #@override
    _transform4oresult_element_ = tkn2tdat_
class RecognizerLLoo__spost__fmap4tuple__tkd2tkey(IRecognizerLLoo__spost__fmap4tuple):
    #@override
    _transform4oresult_element_ = tkd2tkey_
class RecognizerLLoo__spost__fmap4tuple__tkd2tdat(IRecognizerLLoo__spost__fmap4tuple):
    #@override
    _transform4oresult_element_ = tkd2tdat_






class RecognizerLLoo__not_ignore(IRecognizerLLoo__solo_child6env__init, IRecognizerLLoo__default_mixins):
    @override
    def _mk_gi4recognize_(sf, env, xctx_view, unlocker, ignore:bool, istream, /):
        ######################
        #new-ver:donot reset oresult as None
        rgnr = sf._get_the_cached_child6env_(env)
        reply = yield mk_Call_(rgnr, unlocker, ignore:=False, istream)
        return reply
check_non_ABC(RecognizerLLoo__not_ignore)

class RecognizerLLoo__ignore(IRecognizerLLoo__solo_child6env__init, IRecognizerLLoo__default_mixins):
    @override
    def _mk_gi4recognize_(sf, env, xctx_view, unlocker, ignore:bool, istream, /):
        ######################
        #new-ver:donot reset oresult as None
        rgnr = sf._get_the_cached_child6env_(env)
        reply = yield mk_Call_(rgnr, unlocker, ignore:=True, istream)
        return reply
        ######################
        ###cancel:
        #old-ver:
        return _4mk_gi4R_ignore(sf, env, xctx_view, unlocker, ignore:=True, istream)
        return RecognizerLLoo__none8oresult_if_ignore._mk_gi4recognize_(sf, env, xctx_view, unlocker, ignore:=True, istream)
        #assert not reply.ok or reply.oresult is None
        #return reply
check_non_ABC(RecognizerLLoo__ignore)
_Right_None = mk_Right(None)
class RecognizerLLoo__none8oresult_if_ignore(IRecognizerLLoo__solo_child6env__init, IRecognizerLLoo__default_mixins):
    @override
    def _mk_gi4recognize_(sf, env, xctx_view, unlocker, ignore:bool, istream, /):
        'cancel:directly used by RecognizerLLoo__ignore'
        rgnr = sf._get_the_cached_child6env_(env)
        reply = yield mk_Call_(rgnr, unlocker, ignore, istream)
        if ignore and reply.ok:
            if not reply.oresult is None:
                reply = reply.ireplace(eresult=_Right_None)
        assert not ignore or not reply.ok or reply.oresult is None
        return reply
check_non_ABC(RecognizerLLoo__none8oresult_if_ignore)
_4mk_gi4R_ignore = RecognizerLLoo__none8oresult_if_ignore._mk_gi4recognize_


class RecognizerLLoo__constant_loader(IRecognizerLLoo__constant_loader, IRecognizerLLoo__default_mixins, _Base4repr):
    ___no_slots_ok___ = True
    def __init__(sf, eresult, /):
        check_type_is(Either, eresult)
        sf._er = eresult
        #sf._args4repr = (eresult,)
        sf._reset4repr((eresult,))
    @property
    @override
    def _eresult_(sf, /):
        '-> Either errmsg oresult'
        return sf._er
check_non_ABC(RecognizerLLoo__constant_loader)




class IRecognizerLLoo__no_child6env__init(IRecognizerLLoo__no_child6env, _Base4repr):
    ___no_slots_ok___ = True
    def __init__(sf, /):
        #sf._args4repr = null_tuple
        sf._reset4repr(null_tuple)
class IRecognizerLLoo__token_seq__init(IRecognizerLLoo__token_seq, IRecognizerLLoo__no_child6env, _Base4repr):
    #class IRecognizerLLoo__no_child6env__init_tkn_qset_seq(IRecognizerLLoo__no_child6env, _Base4repr):
    ___no_slots_ok___ = True
    def __init__(sf, tkn_qset_seq, /):
        tkn_qset_seq = mk_tuple(tkn_qset_seq)
        for tkn_qset in tkn_qset_seq:
            check_type_le(ITokenQuerySet, tkn_qset)
        #sf._args4repr = (tkn_qset_seq,)
        sf._reset4repr((tkn_qset_seq,))
        sf._qss = tkn_qset_seq
    @property
    @override
    def _token_qset_seq_(sf, /):
        '-> tkn_qset_seq/[ITokenQuerySet]'
        return sf._qss
class IRecognizerLLoo__token__init(IRecognizerLLoo__token, IRecognizerLLoo__no_child6env, _Base4repr):
    #class IRecognizerLLoo__no_child6env__init_tkn_qset(IRecognizerLLoo__no_child6env, _Base4repr):
    ___no_slots_ok___ = True
    def __init__(sf, tkn_qset, /):
        check_type_le(ITokenQuerySet, tkn_qset)
        #sf._args4repr = (tkn_qset,)
        sf._reset4repr((tkn_qset,))
        sf._qs = tkn_qset
    @property
    @override
    def _token_qset_(sf, /):
        '-> tkn_qset/ITokenQuerySet'
        return sf._qs


class RecognizerLLoo__eof(IRecognizerLLoo__no_child6env__init, IRecognizerLLoo__eof, IRecognizerLLoo__default_mixins):pass
class RecognizerLLoo__not_eof(IRecognizerLLoo__no_child6env__init, IRecognizerLLoo__not_eof, IRecognizerLLoo__default_mixins):pass
class RecognizerLLoo__any_token(IRecognizerLLoo__no_child6env__init, IRecognizerLLoo__any_token, IRecognizerLLoo__default_mixins):pass

#class RecognizerLLoo__token(IRecognizerLLoo__no_child6env__init_tkn_qset, IRecognizerLLoo__token, IRecognizerLLoo__default_mixins):pass
#class RecognizerLLoo__token_seq(IRecognizerLLoo__no_child6env__init_tkn_qset_seq, IRecognizerLLoo__token_seq, IRecognizerLLoo__default_mixins):pass
class RecognizerLLoo__token(IRecognizerLLoo__token__init, IRecognizerLLoo__default_mixins):pass
class RecognizerLLoo__token_seq(IRecognizerLLoo__token_seq__init, IRecognizerLLoo__default_mixins):pass



rgnr__any_token = RecognizerLLoo__any_token()
rgnr__eof = RecognizerLLoo__eof()
rgnr__not_eof = RecognizerLLoo__not_eof()

rgnr__any_tkd = RecognizerLLoo__spost__tkn2tkd(rgnr__any_token)
rgnr__any_tkey = RecognizerLLoo__spost__tkn2tkey(rgnr__any_token)
rgnr__any_tdat = RecognizerLLoo__spost__tkn2tdat(rgnr__any_token)


######################
__all__
######################
######################
if 1:
    #######
    _0rgnr__any_token = rgnr__any_token
    _0rgnr__eof = rgnr__eof
    _0rgnr__not_eof = rgnr__not_eof
    #
    _0rgnr__any_tkd = rgnr__any_tkd
    _0rgnr__any_tkey = rgnr__any_tkey
    _0rgnr__any_tdat = rgnr__any_tdat
    #######
    _0light_wrap_rgnr = light_wrap_rgnr_
    _0tag_rgnr = tag_rgnr_
    #######
    #_echo_ = ???
    _0empty8header = empty8header_
    _0followed_by = followed_by_
    _0lift__forgivable = lift__forgivable_
    _0lift__strict = lift__strict_
    _0lookahead = lookahead_
    _0not_followed_by = not_followed_by_
    _0optional__forgivable = optional__forgivable_
    _0optional__strict = optional__strict_
    _0protect_header = protect_header_
    _0protect_whole = protect_whole_
    _0trial_and_error = trial_and_error_
    _0whole8header = whole8header_
class Makers4IRecognizerLLoo:
    _nms = ...; _nms = {*locals()}
    rgnr__any_token = _0rgnr__any_token
    rgnr__eof = _0rgnr__eof
    rgnr__not_eof = _0rgnr__not_eof
    #
    rgnr__any_tkd = _0rgnr__any_tkd
    rgnr__any_tkey = _0rgnr__any_tkey
    rgnr__any_tdat = _0rgnr__any_tdat
    #######
    #######
    light_wrap_rgnr_ = _0light_wrap_rgnr
    tag_rgnr_ = _0tag_rgnr
    #######
    #_echo_ = ???
    empty8header_ = _0empty8header
    followed_by_ = _0followed_by
    lift__forgivable_ = _0lift__forgivable
    lift__strict_ = _0lift__strict
    lookahead_ = _0lookahead
    not_followed_by_ = _0not_followed_by
    optional__forgivable_ = _0optional__forgivable
    optional__strict_ = _0optional__strict
    protect_header_ = _0protect_header
    protect_whole_ = _0protect_whole
    trial_and_error_ = _0trial_and_error
    whole8header_ = _0whole8header
    #######
    any_token_ = RecognizerLLoo__any_token
    between_ = RecognizerLLoo__between
    constant_loader_ = RecognizerLLoo__constant_loader
    end_by_ = RecognizerLLoo__end_by
    eof_ = RecognizerLLoo__eof
    gsep_end_by_ = RecognizerLLoo__gsep_end_by
    ignore_ = RecognizerLLoo__ignore
    light_wrap_ = RecognizerLLoo__light_wrap
    many_ = RecognizerLLoo__many
    named_ = RecognizerLLoo__named
    none8oresult_if_ignore_ = RecognizerLLoo__none8oresult_if_ignore
    not_eof_ = RecognizerLLoo__not_eof
    not_ignore_ = RecognizerLLoo__not_ignore
    priority_parallel_ = RecognizerLLoo__priority_parallel
    ref_ = RecognizerLLoo__ref
    repetition_ = RecognizerLLoo__repetition
    sep_by_ = RecognizerLLoo__sep_by
    sep_end_by_ = RecognizerLLoo__sep_end_by
    serial_ = RecognizerLLoo__serial
    spost__fmap4tuple__tkd2tdat_ = RecognizerLLoo__spost__fmap4tuple__tkd2tdat
    spost__fmap4tuple__tkd2tkey_ = RecognizerLLoo__spost__fmap4tuple__tkd2tkey
    spost__fmap4tuple__tkn2tdat_ = RecognizerLLoo__spost__fmap4tuple__tkn2tdat
    spost__fmap4tuple__tkn2tkd_ = RecognizerLLoo__spost__fmap4tuple__tkn2tkd
    spost__fmap4tuple__tkn2tkey_ = RecognizerLLoo__spost__fmap4tuple__tkn2tkey
    spost__tkd2tdat_ = RecognizerLLoo__spost__tkd2tdat
    spost__tkd2tkey_ = RecognizerLLoo__spost__tkd2tkey
    spost__tkn2tdat_ = RecognizerLLoo__spost__tkn2tdat
    spost__tkn2tkd_ = RecognizerLLoo__spost__tkn2tkd
    spost__tkn2tkey_ = RecognizerLLoo__spost__tkn2tkey
    spost__unbox_ = RecognizerLLoo__spost__unbox
    spostprocess_ = RecognizerLLoo__spostprocess
    tag_ = RecognizerLLoo__tag
    token_ = RecognizerLLoo__token
    token_seq_ = RecognizerLLoo__token_seq
    unbox_tuple_ = RecognizerLLoo__unbox_tuple
    gprepostprocess_ = RecognizerLLoo__gprepostprocess
    dependent_pair_ = RecognizerLLoo__dependent_pair
    switch_branches_ = RecognizerLLoo__switch_branches
    switch_cased_ = RecognizerLLoo__switch_cased
    try_except_else_ = RecognizerLLoo__try_except_else
    try_except_else__spost_ = RecognizerLLoo__try_except_else__spost
    #######
    _nms = {*locals()} -_nms
    pass
def __():
    from seed.types.Namespace import NamespaceForbidModify
    M = Makers4IRecognizerLLoo
    nms = M._nms
    nm2x = {nm:x for nm, x in vars(M).items() if nm in nms}
    return NamespaceForbidModify(nm2x)
Makers4IRecognizerLLoo = __()
#end-class Makers4IRecognizerLLoo:
######################
def _check_repr_overrided():
    d = globals()
    prompt = False
    for nm, v in sorted(d.items()):
        if not isinstance(v, type):
            continue
        T = v
        if not T.__module__ == __name__:
            continue
        ######################
        if not T.__name__[0] in '_I':
            check_non_ABC(T)
        ######################
        if not issubclass(T, IRecognizerLLoo):
            continue
        ######################
        if T.__init__ is not IRecognizerLLoo.__init__ or T.__new__ is not IRecognizerLLoo.__new__:
            assert T.__repr__ is not IRecognizerLLoo.__repr__, T
            assert T.__repr__ is _Base4repr.__repr__, T
        ######################
        if not T.__name__[0] in '_I' and not T is BaseRecognizerLLoo__alias__default_mixins:
            prefix = 'RecognizerLLoo__'
            assert T.__name__.startswith(prefix), (prefix, T)
            suffix = T.__name__[len(prefix):]
            assert suffix[:1].isalpha()
            nm_ = f'{suffix}_'
            if not hasattr(Makers4IRecognizerLLoo, nm_):
                prompt = True
                print_err(f'{nm_} = {T.__name__}')
        ######################
    nms = []
    for nm in name_set4high_freq_sconfigpack:
        if nm == '_echo_':
            continue
        nm_ = f'{nm}_'
        if not hasattr(Makers4IRecognizerLLoo, nm_):
            prompt = True
            nms.append(nm)
    for nm in nms:
        print_err(f'_0{nm} = {nm}_')
    for nm in nms:
        print_err(f'{nm}_ = _0{nm}')
    if prompt:
        print_err(__name__, _check_repr_overrided)
_check_repr_overrided()



__all__
from seed.recognize.recognizer_LLoo__ver2_.IRecognizerLLoo import recognize_, IRecognizerLLoo
from seed.recognize.recognizer_LLoo__ver2_.IRecognizerLLoo import IRecognizerLLoo, Call, mk_Call_, RecognizeCall, Reply, RecognizeReply, dummy_unlocker
from seed.recognize.recognizer_LLoo__ver2_.IRecognizerLLoo import IUnlocker, ISnapshot, IInputStream
    # IBoxedInputStream
from seed.recognize.recognizer_LLoo__ver2_.IRecognizerLLoo import *
