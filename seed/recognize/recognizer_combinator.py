#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/recognizer_combinator.py
view ../../python3_src/seed/recognize/recognizer_combinator_utils.py


grammar = (rsymbol2rule_body__dict_view, lsymbol_set_view)
grammar = template_symbol2rule_body__dict_view
RecognizerMaker:
    .template_schema :: TemplateSchema/ArrowTree
    .mk_recognizer(template_name:Symbol, template_symbol_expr_args:[SymbolExpr]) -> Recognizer
        template_name is required to 'recur
    .mk_recognizer(symbol_expr:SymbolExpr) -> Recognizer
Recognizer:
    .SymbolExpr
        .template_name :: symbol
        .template_symbol_expr_args:[SymbolExpr]
    .recognize__yield(cuttable_stream) -> yield SymbolExpr | return Either ErrMsg Result

main_recognize_(main_symbol_expr:SymbolExpr, template_name2recognizer_maker, cuttable_stream) -> Either ErrMsg Result
    cached_symbol_expr2recognizer

SymbolExpr = Symbol | Apply TemplateSymbol [TemplateArg]
TemplateArg = Symbol | PyPureValue value
TemplateSchema = Symbol | Arrow TemplateSchemaInput TemplateSchema
TemplateSchemaInput = TemplateSchema | PyType ty

RecognizingData as CuttableStream::userdata
    position
    #symbol2recognize_state
    symbol_expr2recognize_state
        not present
        recognizing #??state2status
        Either ErrMsg Result
        ==>> Maybe (Either ErrMsg Result)


from seed.func_tools.recur5yield import recur5yield__list__echo__echo
from seed.lang.is_immutable_pure_value import is_immutable_pure_value


Recognizer
    input:
        stream:
            peek*
            read*
            detect_eof
            ++seek__forward
            #no:tell
    yield:
        (subcall, {lock,unlock}, offsetted_begin/uint, imay_offsetted_end, symbol_expr)
            look_ahead
                lock
            try_call
                half_lock
            tail_call
        xxx (cut, offsetted_end/uint)
            <<== read*/seek__forward
        (cut5aware, ...)
    output:
        is_locked_errmsg_or_size_result
            :: Either (bool, ErrMsg) (UInt, Result)


lock-unlock
guard-aware
head-body

recognizer:
    two phases:
        locked/head, unlocked/body
        when switch from locked->unlocked, send cut_request
    result:
        #attribute is required by grammar, always turnon
        head_errmsg<xxx.attribute>
        head_attribute, head4body_attribute, head4body_result
        body_errmsg<xxx.attribute>
        body_attribute, body_result
    seek_mode:
        go_back#return#for look_ahead
        move_on#advance#not relate to cut_request
        tail_call
    result_mode:
        expect_fail
        expect_pass
        compute_result
    target_mode:
        head, body
        ----6 cases:
        fail4head
        pass4head
        result4head
        pass4head__fail4body
        pass4head__pass4body
        result4head__fail4body
        result4head__pass4body
        result4head__result4body
    be imposed 3/4 states:#inherit
        * locked_locked
            full_locked
        * locked_unlocked
            half_locked
        * unlocked_unlocked
            full_unlocked
        #the 4th:
        * locked_halfway_return
    if locked_locked:
        cancel all cut_request
    if locked_unlocked:
        cancel cut_request come from locked phase
    if unlocked_unlocked:
        not cancel any cut_request

    series:#cascade #catenation
        + locked_locked lefts
        + [#mid#]locked_unlocked mid1
        + unlocked_unlocked rights
    priority switch:
        | locked_unlocked branch
        | locked_unlocked branch
        | locked_unlocked branch
        ...
        | [#last#]unlocked_unlocked branch
    mutual exclusion parallel:#mutex=mutual exclusion
        | locked_halfway_return branch
        | locked_halfway_return branch
        | locked_halfway_return branch
    look_ahead symbol_expr
        --> locked_locked symbol_expr


primitive operators:
    token_set_string
    catenation3
    mutex #parallel
    switch
    ######.doesnot_match_empty_token_seq
    errmsg_
    ######.doesnot_match_any_token_seq
    ######
    look_ahead__whole
    look_ahead_not__whole
    look_ahead__halfway
    look_ahead_not__halfway
    and_fullmatch__whole
    and_not_fullmatch__whole
    and_fullmatch__halfway
    and_not_fullmatch__halfway
    and_prefix_match__whole
    and_not_prefix_match__whole
    and_prefix_match__halfway
    and_not_prefix_match__halfway
    pure_attribute_predicator

whole_result
halfway_result
Result = (GrammarAttribute, UserResult)
EResult
    = LockedFail size errmsg
    | UnlockedFail size halfway_result errmsg
    | Success size halfway_result whole_result

recognize<template_symbol_expr_args>(result_is_required)
    (size, eresult) = yield subcall(symbol_expr, seek_mode, target_mode, imay_size, match_whole_or_prefix)
    if fail4head:
        yield (fail4head, head_errmsg)
        return
    yield pass4head, head_end_state
    yield head_attribute
    if result_is_required:
        yield head4body_result
    yield head4body_attribute

    if fail4body:
        yield (fail4body, body_errmsg)
        return
    yield pass4body, body_end_state
    yield body_attribute
    if result_is_required:
        yield body_result
    return

property:
    min_size4head
    min_size4body
    min_size4whole
input:
    recognize_head: (result_is_required, imay_size4whole)
        -> fail4head(head_errmsg) | pass4head(head_end_state, tmay_head_child_results)
        #head_end_state = head_size, branch_idx, child_attributes, ...

    mk_head4body_attribute: (head_end_state,)
        -> head4body_attribute

    mk_head4body_result: (head_end_state, head4body_attribute, head_child_results)
        -> head4body_result

    recognize_body: (tmay_head4body_result, head_end_state, head4body_attribute, imay_size4body, match_whole_or_prefix)
        -> fail4body(body_errmsg) | pass4body(body_end_state, tmay_body_child_results)
    mk_body_attribute: (body_end_state,)
        -> body_attribute
    mk_body_result: (body_end_state, body_attribute, head4body_result, body_child_results)
        -> body_result




===
inner_st_ex = BEGIN | inner_st | (inner_st, PRUNING) | (inner_st, END)
yield :: (symbol_expr, inner_st4begin) -> (sub_symbol_expr, inner_st4end, lock_mask not[xxx does_unlock_pruning/is_a_unlock_pruning_choice4trial], is_the_mid_pruning_child)
cache :: position -> symbol_expr -> {may_sz4limit : Either errmsg (sz4end, choice, GrammarAttribute)}
pruning_head :: stack<(is_a_unlock_pruning_choice4trial, is_the_mid_pruning_child; symbol_expr, inner_st4begin)> -> (position4begin, may_sz4limit, position4pruning_head) -> IO ()
    precondition:
        all is_a_unlock_pruning_choice4trial==True in stack
        last is_the_mid_pruning_child==True in stack
    backtrack&cache:
        backtrack until is_the_mid_pruning_child==False
        all symbol_expr cache (inner_st4begin, position4begin, may_sz4limit; position4pruning_head, head4body_attribute, head4body_result) when backtrack
pruning_body :: stack<(is_a_unlock_pruning_choice4trial, is_the_mid_pruning_child; symbol_expr, inner_st4begin)> -> (position4begin, may_sz4limit, position4pruning_body) -> IO ()
    precondition:
        all is_a_unlock_pruning_choice4trial==True in stack
        position4pruning_body==position4begin
    backtrack&cache:
        backtrack until not position4pruning_body==position4begin
        all symbol_expr cache (inner_st4begin, position4begin, may_sz4limit; position4pruning_body, body_attribute, body_result) when backtrack
===
lock_mask:
    locked_locked
    locked_unlocked
    unlocked_unlocked
===
e ../../python3_src/seed/recognize/recognizer_combinator_utils.py


#]]]'''
__all__ = r'''
'''.split()#'''
__all__

#([{
from seed.lang.is_immutable_pure_value import is_immutable_pure_value

from seed.types.CuttableStream import CuttableStream, Position, mk_CuttableStream_from_ground_level_tokens, mk_CuttableStream_from_ground_level_tokens5file, mk_userdata__pair, mk_userdata__token, iter_tokens5file
from seed.types.CuttableStream import CuttableStreamError
from seed.types.CuttableStream import CuttableStreamError, CuttableStreamError__invalid_Position, CuttableStreamError__addr_out_of_range, CuttableStreamError__EOF, CuttableStreamError__cut_beyond, CuttableStreamError__reenter_cutting, CuttableStreamError__reenter_filling, CuttableStreamError__seek_when_cutting, CuttableStreamError__seek_when_filling

from seed.types.CuttableStream import IMkUserData4CuttableStream, MkUserData4CuttableStream5callable__mk_userdata, MkUserData4CuttableStream5callable__mk_huserdata__pair8userdata
from seed.types.CuttableStream import Mkr4XUserData4CuttableStream, XUserData4CuttableStream







from seed.recognize.recognizer_combinator_utils import LockMaskBit
from seed.recognize.recognizer_combinator_utils import LockMask
from seed.recognize.recognizer_combinator_utils import Error__move_nonfinal_inner_st
from seed.recognize.recognizer_combinator_utils import ISymbolExprInnerStateController


from seed.recognize.recognizer_combinator_utils import (ISymbolExprInnerStateController, is_post_pruning_inner_st, is_inner_st, is_fail_inner_st, is_success_inner_st, nonfinal_inner_st2lock_mask, get_initial_inner_st, move_nonfinal_inner_st, Error__move_nonfinal_inner_st, noninitial_inner_st2prev_inner_st, is_initial_inner_st, is_final_inner_st, check_inner_st, check_initial_inner_st, check_final_inner_st, check_noninitial_inner_st, check_nonfinal_inner_st, iter_all_inner_sts, iter_all_final_inner_sts, iter_all_nonfinal_inner_sts, iter_all_post_pruning_inner_sts, iter_all_prev_inner_sts__include, validate_post_pruning_inner_sts)


from seed.recognize.recognizer_combinator_utils import (ISymbolExprInnerStateController, SymbolExprInnerStateController__mutex, SymbolExprInnerStateController__switch, SymbolExprInnerStateController__catenation, SymbolExprInnerStateController__token, SymbolExprInnerStateController__and1s__full_match, SymbolExprInnerStateController__and1s__prefix_match, SymbolExprInnerStateController__andnot1s__full_match, SymbolExprInnerStateController__andnot1s__prefix_match, SymbolExprInnerStateController__look_ahead__head, SymbolExprInnerStateController__look_ahead__body, SymbolExprInnerStateController__skip, SymbolExprInnerStateController__look_ahead_not__head, SymbolExprInnerStateController__look_ahead_not__head_body)





from seed.recognize.recognizer_combinator_utils import LockMaskBit, bit4locked_head, bit4locked_body, bit4head_return, bit4body_return, bit4with_user_result, bit4full_match

from seed.recognize.recognizer_combinator_utils import LockMask, locked_halfway_return, unlocked_unlocked__without_user_result, locked_locked_return__without_user_result, locked_locked_return__with_user_result, locked_locked, locked_unlocked, unlocked_unlocked, locked_locked_return__with_user_result__full_match, locked_locked__full_match, locked_unlocked__full_match, unlocked_unlocked__full_match, locked_locked_return__without_user_result__full_match













class Arrow(tuple):
    r'''[[[
    e.g. ((py_pure_value -> *) -> * -> *)
        --> ((False -> True) -> True -> True)
        --> Arrow(Arrow(False), True)
        since rightmost MUST BE 『*』==>> omit
    #]]]'''
    __slots__ = ()
    def __new__(cls, ls, /):
        sf = super(__class__, cls).__new__(cls, lhss)
        assert all(type(x) in ArrowArgTypes for x in ls)
        return sf
TemplateSchema = Arrow
ArrowArgTypes = (bool, Arrow)

class SymbolExpr:
    __slots__ = ()
class Symbol(SymbolExpr, str):
    __slots__ = ()
    @property
    def template_name(sf, /):
        return sf
    @property
    def template_args(sf, /):
        return ()
class Apply(SymbolExpr, tuple):
    __slots__ = ()
    def __new__(cls, template_name, /, *template_args):
        check_type_is(Symbol, template_name)
        assert is_immutable_pure_value(template_args) #too slow...???
        sf = super(__class__, cls).__new__(cls, (template_name, *template_args))
        return sf
    @property
    def template_name(sf, /):
        return sf[0]
    @property
    def template_args(sf, /):
        return tuple.__getitem__(sf, slice(1,None))
SymbolExprTypes = (Symbol, Apply)



class EResult:
    __slots__ = ()
class ErrMsg(EResult, str):
    __slots__ = ()
class Result(EResult, tuple):
    __slots__ = ()
    def __new__(cls, result, /):
        sf = super(__class__, cls).__new__(cls, [result])
        return sf




class RecognizerMaker:
    def get_template_schema(sf, /)->TemplateSchema:
    def mk_recognizer(sf, symbol_expr:SymbolExpr, /) -> Recognizer:

xxxx

def main_recognize_(main_symbol_expr:SymbolExpr, template_name2recognizer_maker, cuttable_stream, /) -> 'Either ErrMsg Result':
    check_type_in(SymbolExprTypes, main_symbol_expr)
    assert all(T in SymbolExprTypes for T in map(type, template_name2recognizer_maker.keys()))
    cached_symbol_expr2recognizer = {}
    def get_or_mk_recognizer5symbol_expr(symbol_expr, /):
        m = cached_symbol_expr2recognizer.get(symbol_expr)
        if m is not None:
            recognizer = m
            return recognizer
        recognizer_maker = template_name2recognizer_maker[symbol_expr.template_name]
        recognizer = recognizer_maker.mk_recognizer(symbol_expr)
        cached_symbol_expr2recognizer[symbol_expr] = recognizer
        return recognizer
    main_recognizer = get_or_mk_recognizer5symbol_expr(main_symbol_expr)
    @recur5yield__list__echo__echo
    def main():
        return False, main_symbol_expr.recognize__yield(cuttable_stream)
        yield




class IRecognizer(ABC):
    def subcall4recognize__yield(sf, symbol_expr, seek_mode, target_mode, imay_size, match_whole_or_prefix, /):
        '-> (size, eresult)'

    def subcall4get_min_size__yield(sf, symbol_expr, head_vs_body_vs_whole, /):
        '-> (uint|+oo)'


    def get_min_size4whole__yield(sf, /):
        '-> min_size4whole <- [0..=min_size4head+min_size4body]'
    def get_min_size4head__yield(sf, /):
        '-> min_size4head <- [0..]'
    def get_min_size4body__yield(sf, /):
        '-> min_size4body <- [0..]'
    #def recognize__yield(sf, cuttable_stream:CuttableStream, /) -> 'yield sub_expr:SymbolExpr | return Either ErrMsg Result':
    def recognize_head__yield(sf, result_is_required, imay_size4whole, /):
        '-> fail4head(head_errmsg) | pass4head(head_end_state, tmay_head_child_results)'
        #head_end_state = head_size, branch_idx, child_attributes, ...

    def mk_head4body_attribute__yield(sf, head_end_state, /):
        '-> head4body_attribute'

    def mk_head4body_result__yield(sf, head_end_state, head4body_attribute, head_child_results, /):
        '-> head4body_result'

    def recognize_body__yield(sf, tmay_head4body_result, head_end_state, head4body_attribute, imay_size4body, match_whole_or_prefix, /):
        '-> fail4body(body_errmsg) | pass4body(body_end_state, tmay_body_child_results)'
    def mk_body_attribute__yield(sf, body_end_state, /):
        '-> body_attribute'
    def mk_body_result__yield(sf, body_end_state, body_attribute, head4body_result, body_child_results, /):
        '-> body_result'
#end-class IRecognizer(ABC):

def check_symbol_expr_seq
class Recognizer__switch(IRecognizer):
    def __init__(sf, symbol_expr_seq, /):
        check_symbol_expr_seq(symbol_expr_seq)
        sf._ls = symbol_expr_seq
    def _get_min_size4xxx__yield(sf, min_size_mode, /):
        min_sz = pos_oo
        for symbol_expr in sf._ls:
            sz = yield sf.subcall4get_min_size__yield(symbol_expr, min_size_mode)
            min_sz = min(min_sz, sz)
        return (True, min_sz)
    def get_min_size4whole__yield(sf, /):
        '-> min_size4whole <- [0..=min_size4head+min_size4body]'
        return (False, sf._get_min_size4xxx__yield(MinSizeMode.whole));yield
    def get_min_size4head__yield(sf, /):
        '-> min_size4head <- [0..]'
        return (False, sf._get_min_size4xxx__yield(MinSizeMode.head));yield
    def get_min_size4body__yield(sf, /):
        '-> min_size4body <- [0..]'
        return (False, sf._get_min_size4xxx__yield(MinSizeMode.head));yield
    #def recognize__yield(sf, cuttable_stream:CuttableStream, /) -> 'yield sub_expr:SymbolExpr | return Either ErrMsg Result':
    def recognize_head__yield(sf, result_is_required, imay_size4whole, /):
        '-> fail4head(head_errmsg) | pass4head(head_end_state, tmay_head_child_results)'
        #head_end_state = head_size, branch_idx, child_attributes, ...
        if not (sf._ls):
            return (0, ...eresult)
        seek_mode = SeekMode.move_on
        target_mode = TargetMode.result4head if result_is_required else TargetMode.pass4head
        for i, symbol_expr in enumerate(sf._ls):
            if i+1==len(sf._ls):
                seek_mode = SeekMode.tail_call
            (size, eresult) = yield sf.subcall4recognize__yield(symbol_expr, seek_mode, target_mode, imay_size4whole, MatchMode.match_prefix)
            if eresult.ok:
                return (size, eresult)
        return (size, eresult)

    def mk_head4body_attribute__yield(sf, head_end_state, /):
        '-> head4body_attribute'

    def mk_head4body_result__yield(sf, head_end_state, head4body_attribute, head_child_results, /):
        '-> head4body_result'

    def recognize_body__yield(sf, tmay_head4body_result, head_end_state, head4body_attribute, imay_size4body, match_whole_or_prefix, /):
        '-> fail4body(body_errmsg) | pass4body(body_end_state, tmay_body_child_results)'
    def mk_body_attribute__yield(sf, body_end_state, /):
        '-> body_attribute'
    def mk_body_result__yield(sf, body_end_state, body_attribute, head4body_result, body_child_results, /):
        '-> body_result'
class Recognizer__catenation3(IRecognizer):
primitive operators:
    token
    token_set
    token_set_string
    catenation3
    parallel
    switch
    ######.doesnot_match_empty_token_seq
    errmsg_
    ######.doesnot_match_any_token_seq
    ######
    look_ahead__whole
    look_ahead_not__whole
    look_ahead__halfway
    look_ahead_not__halfway
    and_fullmatch__whole
    and_not_fullmatch__whole
    and_fullmatch__halfway
    and_not_fullmatch__halfway
    and_prefix_match__whole
    and_not_prefix_match__whole
    and_prefix_match__halfway
    and_not_prefix_match__halfway
    pure_attribute_predicator



#}])
