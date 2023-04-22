#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/recognizer_combinator_executor.py
to replace:view ../../python3_src/seed/recognize/recognizer_combinator.py
view ../../python3_src/seed/recognize/recognizer_combinator_utils.py
view ../../python3_src/seed/types/CuttableStream.py
view ../../python3_src/seed/helper/check/ADT.py

seed.recognize.recognizer_combinator_executor
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_combinator_executor
py -m seed.recognize.recognizer_combinator_executor
py -m nn_ns.app.adhoc_argparser__main__call8module   seed.recognize.recognizer_combinator_executor
from seed.recognize.recognizer_combinator_executor import ...


[[
nonfinal_inner_st2...
    vs step_success_inner_st2...
        #diff when moveon_nonfinal_inner_st2tmay_next_inner_st return ()

noninitial_inner_st2prev_inner_st
step_success_noninitial_inner_st2prev_lock_mask

    xxx nonfinal_inner_st2either_token_acceptor_or_symbol_expr
    xxx nonfinal_inner_st2symbol_expr_or_token_acceptor
    xxx nonfinal_inner_st2either_token_expr_or_symbol_expr
        --> step_success_noninitial_inner_st2prev_either_token_expr_or_symbol_expr

    xxx nonfinal_inner_st2next_step_success_filters
        --> step_success_noninitial_inner_st2prev_step_filters

    xxx nonfinal_inner_st2acc_st4step
        --> step_success_noninitial_inner_st2prev_acc_st4step


]]



input:
    cuttable_stream :: (stream<(token,userdata)>, huserdata)
        .get_xuserdata__relative
        .peak1__xuserdata__relax
        .read_le
        .read1
        .peak_le
        .peak1
        .cut__position


using refcount in cached-middle_st:
    stack<(acc_st5above; symbol_expr, nonfinal_inner_st, begin_position, may_end_position;accGrammarAttribute 5until_curr_nonfinal_inner_st;may (step_eGrammarAttribute,tmay_step_eresult/__without_user_result) 5next_step5pruning)>

    recur_detect_setstack :: set/\stack<(symbol_expr, begin_position, may_end_position)>
        detect recur recognize: step-failure?? or global err??
        .handle4left_corner_recur
            raise global_err
            step failure
            # decrease may_end_position
    the_pruning_position === stream.tell_cutting_end_position()
        detect global err: [begin_position <= may_end_position][begin_position < the_pruning_position]

    #XUserData4CuttableStream
    xuserdata/huserdata/userdata@position:
        .stack_idc4stack_item_begin_here
            all(stack[i].begin_position==position for i in stack_idc)
            all(i in stream[stack_item.begin_position].stack_idc for i,stack_item in enumerate(stack))
            when pruning:
                after remove|eval:
                    iter over stack_idc:
                        fill eresult into stack

        .token_expr2relative_end_position2middle_st
        .token_expr2eof_or_free_relative_farthest_touched_end_position
        .symbol_expr2relative_end_position2middle_st
        .symbol_expr2eof_or_free_relative_farthest_touched_end_position

        #MiddleState
        middle_st@rsymbol@position:
            .refcount
            # .token
            .begin_position = @position
            .farthest_touched_end_position = begin_position+1
            .does_try_to_read_token_at_end_position = False
            .stop_position_before_return = begin_position+(not hit_may_end_position)
            xxx .stop_position = begin_position if acc_st5above&__return else stop_position_before_return
            .eGrammarAttribute
                <<== rsymbol2meGrammarAttribute
            .eresult
                <<== rsymbol_raw_value_GrammarAttribute2meresult

        #MiddleState
        middle_st@(symbol_expr, begin_position, may_end_position):
            .refcount
                += 1 <<== final_inner_st2reversed_iter__noninitial_inner_st__is_without_prev_step_eresult__pairs
                rooted from stack
                when pruning@position:
                    iter over userdata:
                        if .refcount==0:then remove else if no eresult then eval eresult
            .begin_position = @position
            .farthest_touched_end_position
                = max(begin_position, ...step.farthest_touched_end_position...)
            .does_try_to_read_token_at_end_position
                #try token_acceptor at may_end_position
                =  any(...step.does_try_to_read_token_at_end_position...)
            .stop_position_before_return
                <<== step.get_stop_position
            xxx .stop_position = begin_position if acc_st5above&__return else stop_position_before_return
            .eGrammarAttribute
            ??? ._final_inner_st???
                using cache to run again, ...
            ??? _conditional_cached__reversed__pair_seq_about____noninitial_inner_st___prev__either_prestepinto_failcase_or_step_position_rng_endby_far_and_either_token_expr_or_symbol_expr4as_if_success_and_noninitial_inner_st4as_if_success
            .eresult




errmsg :: str
herrmsg_ex = Either errmsg|(nonfinal_inner_st, step_errmsg_ex)
    ???step_success_noninitial_inner_st
meGrammarAttribute = Either errmsg|GrammarAttribute
    merely
heGrammarAttribute = Either herrmsg_ex|GrammarAttribute
    half/hurt/harm/damage
he_accGrammarAttribute = Either herrmsg_ex|accGrammarAttribute
eGrammarAttribute = Either errmsg_ex|GrammarAttribute
    eresult4fail = errmsg_ex
meresult = Either errmsg|result
heresult = Either herrmsg_ex|result
eresult = Either errmsg_ex|result
    errmsg_ex:
        .begin_position
        .may_end_position
        .farthest_touched_end_position
        .does_try_to_read_token_at_end_position
        .either_token_expr_or_symbol_expr
        .herrmsg_ex

.executor
    .token_expr2token_acceptor
    .symbol_expr2recognizer_and_inner_st_controller
    .token2rsymbol :: token -> rsymbol
    .token2raw_value :: token -> raw_value
token_acceptor
    .token_expr
        .get_token_expr
    xxx .accept_token :: token_acceptor -> token -> bool
    .rsymbol2meGrammarAttribute :: rsymbol -> meGrammarAttribute
    .rsymbol_raw_value_GrammarAttribute2meresult :: rsymbol -> raw_value -> GrammarAttribute -> meresult

symbol_expr2recognizer
recognizer<symbol_expr>:
    TODO:
        see:_return__symbol_expr__heGrammarAttribute
        xxx tmay_heresult from handle4global_err
            --> tmay_whole_heGrammarAttribute
            --> tmay_whole_meGrammarAttribute
        finalize:
            whole_heGrammarAttribute -> heresult
            whole_meGrammarAttribute -> heresult
    xxx .handle4left_corner_recur :: () -> tmay_heresult
        ......meaningless.....
        () -> global_err__recognizer_design_err
        (heresult,) -> ...
    xxx .handle4step_fail__but__has_no_step_fail_next_inner_st :: nonfinal_inner_st -> tmay_heresult
        #step_fail__but__has_no_step_fail_next_inner_st
        ......meaningless.....
        when step into return fail but has no next_inner_st4fail
    ...

    .symbol_expr
        .get_symbol_expr
    .inner_st_controller :: ISymbolExprInnerStateController

    .last_known_inner_st2noninitial_inner_st2without_prev_step_eresult
        required when pruning #unknown final_inner_st yet
        ==>> limited by .inner_st_controller._nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ (__with_user_result)
    .final_inner_st2reversed_iter__noninitial_inner_st__is_without_prev_step_eresult__pairs
        ==>> limited by .last_known_inner_st2noninitial_inner_st2without_prev_step_eresult
        ## arbitrary/parallel
        #mutex/switch ... requires only last sucess branch
        #lookahead/skip ... ignore all

    .eval_whole_eresult
        .basic_eval_whole_eresult :: reversed[(noninitial_inner_st, prev_step__either_prestepinto_failcase_or_eGrammarAttribute_and_tmay_eresult/__without_user_result)] -> GrammarAttribute -> heresult
            (prev_step_eGrammarAttribute, tmay_prev_step_eresult)
                --> prev_step__either_prestepinto_failcase_or_eGrammarAttribute_and_tmay_eresult)

        .filters4whole :: [GrammarAttribute->result -> result]
            # heGrammarAttribute -> heresult return errmsg_ex directly
            # so,only (GrammarAttribute,result)
        .step_success_noninitial_inner_st2prev_step_filters
            xxx .nonfinal_inner_st2next_step_success_filters
            step_success_filter :: step_GrammarAttribute->step_result->step_result
            is_step_success_noninitial_inner_st
            step_success_noninitial_inner_st

    xxx .nonfinal_inner_st2either_token_acceptor_or_symbol_expr
        step_recognizer :: Either token_acceptor|recognizer<symbol_expr>
    .step_success_noninitial_inner_st2prev_either_token_expr_or_symbol_expr
        xxx .nonfinal_inner_st2either_token_expr_or_symbol_expr
        step_success_noninitial_inner_st
        either_token_expr_or_symbol_expr :: Either token_expr symbol_expr


    .accumulator4fold_GrammarAttribute
        .init4acc__he_accGrammarAttribute
        .init :: () -> he_accGrammarAttribute
                !!!1 init failure cases!!!
        .binop4acc__he_accGrammarAttribute
        .binop :: accGrammarAttribute -> either_prestepinto_failcase_or_step_eGrammarAttribute -> noninitial_inner_st -> he_accGrammarAttribute
            prestepinto_failcase :: FailCase_pre_stepinto
            either_prestepinto_failcase_or_step_eGrammarAttribute
                !!!3 step failure cases!!!
                (Left is_bad_position_rng) -> [may_end_position < begin_position][is_step_fail_noninitial_inner_st(noninitial_inner_st)]
                (Left has_no_step_success) -> [...moveon_nonfinal_inner_st2tmay_next_inner_st<True> return ()]
                (Right(Left errmsg_ex),) -> ...[err from step_expr]
                (Right(Right GrammarAttribute<step_expr>),) -> ...ok...

        .finalize4success4acc__he_accGrammarAttribute
        .final4success :: accGrammarAttribute -> success_final_inner_st -> is_bad_position_rng/bool -> heGrammarAttribute
                !!!1 final failure cases!!!
                is_bad_position_rng := may_end_position < begin_position
        .finalize4fail4acc__he_accGrammarAttribute
        .final4fail :: accGrammarAttribute -> fail_final_inner_st -> is_bad_position_rng/bool -> herrmsg_ex



#]]]'''
__all__ = r'''
'''.split()#'''
__all__

from enum import Enum, Flag, auto

from seed.tiny import check_type_le, check_either
from seed.tiny_.containers import null_str, null_bytes, null_int, null_tuple, null_frozenset, null_mapping_view, null_iter, mk_frozenset, mk_tuple, mk_Just, mk_Left, mk_Right

from seed.debug.expectError import expectError
from seed.tiny_.CompactData import Base4CompactData, mk_CompactDataType, mk_CompactDataType_then_write_to_module

from seed.types.CuttableStream import CuttableStream, Position

from seed.recognize.recognizer_combinator_utils import LockMaskBit
from seed.recognize.recognizer_combinator_utils import LockMask
from seed.recognize.recognizer_combinator_utils import moveon_nonfinal_inner_st2tmay_next_inner_st
from seed.recognize.recognizer_combinator_utils import ISymbolExprInnerStateController

from seed.recognize.recognizer_combinator_utils import step_success_noninitial_inner_st2prev_lock_mask, check_step_success_noninitial_inner_st

class FailCase_pre_stepinto(Enum):
    is_bad_position_rng = auto()
    has_no_step_success = auto()
    #binop4acc__he_accGrammarAttribute

class AccumulatedLockState(Enum):
    locked_unlocked4acc = LockMaskBit.bit4locked_head
    locked_locked4acc = LockMaskBit.bit4locked_head|LockMaskBit.bit4locked_body
    unlocked_unlocked4acc = LockMaskBit.bit4locked_head^LockMaskBit.bit4locked_head
    assert unlocked_unlocked4acc.value == 0
assert len(AccumulatedLockState) == 3
assert AccumulatedLockState.unlocked_unlocked4acc.value.value == 0
assert expectError(ValueError, lambda:AccumulatedLockState(LockMaskBit.bit4locked_body))
class AccumulatedMaskState(Enum):
    '(AccumulatedLockState, is_with_user_result)'
    locked_unlocked4acc_wo = (AccumulatedLockState.locked_unlocked4acc, False)
    locked_locked4acc_wo = (AccumulatedLockState.locked_locked4acc, False)
    unlocked_unlocked4acc_wo = (AccumulatedLockState.unlocked_unlocked4acc, False)

    locked_unlocked4acc_wi = (AccumulatedLockState.locked_unlocked4acc, True)
    locked_locked4acc_wi = (AccumulatedLockState.locked_locked4acc, True)
    unlocked_unlocked4acc_wi = (AccumulatedLockState.unlocked_unlocked4acc, True)
assert len(AccumulatedMaskState) == 6
assert len({AccumulatedMaskState((acc,wx)) for acc in AccumulatedLockState for wx in [False, True]}) == 6


def lock_mask2is_with_user_result(lock_mask, /):
    check_type_is(LockMask, lock_mask)
    is_with_user_result = bool(lock_mask.value&LockMaskBit.bit4with_user_result)
    return is_with_user_result

assert all((lock_mask.value & LockMaskBit.bit4locked_head) for lock_mask in LockMask if (lock_mask.value & LockMaskBit.bit4head_return))
assert all((lock_mask.value & LockMaskBit.bit4locked_head) for lock_mask in LockMask if (lock_mask.value & LockMaskBit.bit4body_return))
assert all((lock_mask.value & LockMaskBit.bit4locked_head) for lock_mask in LockMask if (lock_mask.value & LockMaskBit.bit4locked_body))

assert all((lock_mask.value & LockMaskBit.bit4locked_body) for lock_mask in LockMask if (lock_mask.value & LockMaskBit.bit4body_return))

def lock_mask2acc_st(lock_mask, /):
    acc_lock_st = lock_mask2acc_lock_st(lock_mask)
    is_with_user_result = lock_mask2is_with_user_result(lock_mask)
    acc_st = AccumulatedMaskState((acc_lock_st, is_with_user_result))
    return acc_st
def lock_mask2acc_lock_st(lock_mask, /):
    check_type_is(LockMask, lock_mask)
    if not (lock_mask.value & LockMaskBit.bit4locked_head):
        if (lock_mask.value & LockMaskBit.bit4head_return) or (lock_mask.value & LockMaskBit.bit4body_return) or (lock_mask.value & LockMaskBit.bit4locked_body): raise logic-err in LockMask
        acc_lock_st = AccumulatedLockState.unlocked_unlocked4acc
    elif (lock_mask.value & LockMaskBit.bit4head_return) or (lock_mask.value & LockMaskBit.bit4body_return) or (lock_mask.value & LockMaskBit.bit4locked_body):
        acc_lock_st = AccumulatedLockState.locked_locked4acc
    else:
        acc_lock_st = AccumulatedLockState(lock_mask.value & AccumulatedLockState.locked_locked4acc.value)
        if not acc_lock_st is AccumulatedLockState.locked_unlocked4acc:raise logic-err in LockMask

    check_type_is(AccumulatedLockState, acc_lock_st)
    assert acc_lock_st in AccumulatedLockState
    return acc_lock_st

#def nonfinal_inner_st2acc_st4step(inner_st_controller, acc_st5above, nonfinal_inner_st, /):
def step_success_noninitial_inner_st2prev_acc_st4step(inner_st_controller, acc_st5above, step_success_noninitial_inner_st, /):
    #vs: lock_mask2acc_st,step_success_noninitial_inner_st2prev_acc_st4step
    check_type_is(AccumulatedMaskState, acc_st5above)

    #lock_mask4step = _nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_(inner_st_controller, nonfinal_inner_st)
    lock_mask4step = step_success_noninitial_inner_st2prev_lock_mask(inner_st_controller, step_success_noninitial_inner_st)
    nonfinal_inner_st = noninitial_inner_st2prev_inner_st(inner_st_controller, step_success_noninitial_inner_st)
    next_inner_st4success = step_success_noninitial_inner_st

    (acc_lock_st5above, is_with_user_result5above) = acc_st5above.value

    if acc_lock_st5above is AccumulatedLockState.locked_unlocked4acc:
        if is_post_pruning_inner_st(inner_st_controller, nonfinal_inner_st):
            acc_lock_st5above_until = AccumulatedLockState.unlocked_unlocked4acc
        elif is_post_pruning_inner_st(inner_st_controller, next_inner_st4success):
            acc_lock_st5above_until = AccumulatedLockState.locked_unlocked4acc
        else:
            acc_lock_st5above_until = AccumulatedLockState.locked_locked4acc
            r'''
        else:
            tmay_next_inner_st4success = moveon_nonfinal_inner_st2tmay_next_inner_st(inner_st_controller, True, nonfinal_inner_st)
            if not tmay_next_inner_st4success:
                acc_lock_st5above_until = AccumulatedLockState.locked_locked4acc
            else:
                [next_inner_st4success] = tmay_next_inner_st4success
                if is_post_pruning_inner_st(inner_st_controller, next_inner_st4success):
                    acc_lock_st5above_until = AccumulatedLockState.locked_unlocked4acc
                else:
                    acc_lock_st5above_until = AccumulatedLockState.locked_locked4acc
            '''#'''
    else:
        acc_lock_st5above_until = acc_lock_st5above


    acc_lock_st4step = AccumulatedLockState(acc_lock_st5above_until.value | lock_mask2acc_lock_st(lock_mask4step).value)
        # or
        # OR<lock> ...

    is_with_user_result4step = is_with_user_result5above and lock_mask2is_with_user_result(lock_mask4step)
        # and
        # OR<without> ...

    check_type_is(AccumulatedLockState, acc_lock_st4step)
    check_type_is(bool, is_with_user_result4step)
    acc_st4step = AccumulatedMaskState((acc_lock_st4step, is_with_user_result4step))

    check_type_is(AccumulatedMaskState, acc_st4step)
    return acc_st4step




class RecognizerCombinatorExecutor:
    def __init__(sf, userdata_ops, cuttable_stream, /):
        check_type_le(IUserDataOps4Recognizer, userdata_ops)
        check_type_le(CuttableStream, cuttable_stream)
        if not _g_mk_userdata == cuttable_stream.get_mk_userdata(): return TypeError
        sf.cuttable_stream = cuttable_stream
        sf.userdata_ops = userdata_ops
        sf._symbol_expr2recognizer_and_inner_st_controller = {} # {symbol_expr:(recognizer,inner_st_controller)}
        sf.stack = []
            # almost [StackItem]
            # but last stack_item may be:either_prestepinto_failcase_or_step_IO
            #   * (Left FailCase_pre_stepinto)
            #   * Right(acc_st5above, either_token_expr_or_symbol_expr, begin_position, may_end_position; middle_st)
            #       (...input4put...; output)
            #
            #is_bad_position_rng
            #has_no_step_success
        #sf.the_pruning_position
    @property
    def the_pruning_position(sf, /):
        return sf.cuttable_stream.tell_cutting_end_position()

    def prune__position(sf, position, /):
        #stack_idc4stack_item_begin_here
        #   _stack_push:append
        #   _stack_pop:pop
        #
        #using cache to eval all stack[i] for i in stack_idc
        #   dec refcount
        #
        #[refcount:using_refcount_for_validate_only_not_to_auto_delete]
        #
        # ???_return__symbol_expr__eGrammarAttribute
        #   [pops__at__return__symbol_expr__eGrammarAttribute]
        ..
        #
        the_pruning_position = sf.the_pruning_position
        if position is the_pruning_position:return
        if not position_lt(the_pruning_position, position): raise logic-err
        sz = position_diff(position, the_pruning_position)
        assert sz > 0
        stream = sf.cuttable_stream
        stream.seek__position(the_pruning_position)
        assert stream.tell__relative(sz) is position
        while the_pruning_position is not position:
            xuserdata = stream.peak1__xuserdata__relax()
            sf._0clear_cache4the_prune__position(the_pruning_position, xuserdata)
            ######################
            #next round
            stream.read1()
            #move_on_then_prune
            the_pruning_position = stream.tell()
            stream.cut__position(the_pruning_position)
        if not position is sf.the_pruning_position:raise logic-err
        return
    def _0clear_cache4the_prune__position(sf, the_pruning_position, xuserdata, /):
        stack_idc = xuserdata.stack_idc4stack_item_begin_here
        stack = sf.stack
        check_type_is(StackItem, stack[-1])
        assert stack
        L = len(stack)-1
        if 1:
            # 还是不太对，如果stack_item 在返回时prune???stack_item 也可能在_put__symbol_expr__inner_st时prune???
            #第二种情形，stack_item 还未进stack，所以只需判断是否为final_inner_st
            stack_item = stack[-1]
            check_type_is(StackItem, stack_item)
            allow_last = not is_final_inner_st(stack_item.common.inner_st_controller, stack_item.inner_st):

        for i6stack in stack_idc:
            if not allow_last and i6stack == L:continue
            stack_item = stack[i6stack]
            check_type_is(StackItem, stack_item)
            if hasattr(stack_item, 'either_prestepinto_failcase_or_tmay_step_eresult5pruning'):raise logic-err

            if not i6stack == L:
            stack_item1 = stack[i6stack+1]
            check_type_is(StackItem, stack_item1)
            if stack_item1.using_initial_inner_st():
                if hasattr(stack_item, 'either_prestepinto_failcase_or_step_eGrammarAttribute'):raise logic-err
                continue
            if not hasattr(stack_item, 'either_prestepinto_failcase_or_step_eGrammarAttribute'):raise logic-err
            stack_item.either_prestepinto_failcase_or_tmay_step_eresult5pruning = sf._eval__stack_item(stack_item, stack_item.either_prestepinto_failcase_or_step_eGrammarAttribute)

    def _eval__stack_item(sf, stack_item, either_prestepinto_failcase_or_step_eGrammarAttribute, /):
        '-> either_prestepinto_failcase_or_tmay_step_eresult5pruning'
        if 0:
            #bug:should handle refcount
            #  now rename:
            #   %s/tmay_either_prestepinto_failcase_or_step_eresult/either_prestepinto_failcase_or_tmay_step_eresult/g
            #   %s/prev_step_eGrammarAttribute, tmay_prev_either_prestepinto_failcase_or_step_eresult/prev_step__either_prestepinto_failcase_or_eGrammarAttribute_and_tmay_eresult/g
            #
            acc_st5above = common.acc_st5above
            (acc_lock_st, is_with_user_result) = acc_st5above
            if not is_with_user_result:
                either_prestepinto_failcase_or_tmay_step_eresult5pruning = null_tuple
                return either_prestepinto_failcase_or_tmay_step_eresult5pruning

        (is_right, x) = either_prestepinto_failcase_or_step_eGrammarAttribute
        if is_right:
            step_eGrammarAttribute = x
            (is_right, x) = step_eGrammarAttribute
            if is_right:
                step_GrammarAttribute = x
            else:
                errmsg_ex = x
        else:
            prestepinto_failcase = x
        is_right
        if not is_right:
            either_prestepinto_failcase_or_tmay_step_eresult5pruning = either_prestepinto_failcase_or_step_eGrammarAttribute
            return either_prestepinto_failcase_or_tmay_step_eresult5pruning
        step_GrammarAttribute


        common = stack_item.common
        inner_st_controller = common.inner_st_controller
        inner_st = stack_item.inner_st
        check_nonfinal_inner_st(inner_st_controller, inner_st)
            #
            #final_inner_st can only occur at stack[-1] #no middle_st return either
            #bug:when prune position, stack_idc4stack_item_begin_here cannot contains (len(stack)-1)
            # bug:hence stack[-1] must be nonfinal_inner_st
            #   can contains
            #   see:_0clear_cache4the_prune__position:skipped explictly
            # since (len(stack)-1) is skipped, stack_item must be nonfinal_inner_st
            #
            # 还是不太对，如果stack_item 在返回时prune???stack_item 也可能在_put__symbol_expr__inner_st时prune???
            #更新_0clear_cache4the_prune__position
            #
        nonfinal_inner_st = inner_st
        if 1:
            #or:copy from _on__nonfinal_inner_st
            #acc_st4step = stack_item._conditional_cached__acc_st4step
            (either_token_expr_or_symbol_expr, acc_st4step) = stack_item._conditional_cached__either_token_expr_or_symbol_expr4as_if_success_and_acc_st4step
        either_prestepinto_failcase_or_tmay_step_eresult5pruning = mk_Right(tmay_step_eresult)
        tmay_step_eresult = sf._eval__step(common.acc_st5above, acc_st4step, either_token_expr_or_symbol_expr, begin_position, may_end_position)
        return either_prestepinto_failcase_or_tmay_step_eresult5pruning
    def _eval__step(sf, acc_st5above, acc_st4step, either_token_expr_or_symbol_expr, begin_position, may_end_position, /):
        (step_eGrammarAttribute, tmay_step_eresult) = sf._eval__step_ex(common.acc_st5above, acc_st4step, either_token_expr_or_symbol_expr, begin_position, may_end_position)
        return tmay_step_eresult
    def _eval__step_ex(sf, acc_st5above, acc_st4step, either_token_expr_or_symbol_expr, begin_position, may_end_position, /):
        (step_eGrammarAttribute, tmay_step_eresult) = sf._0eval__step_ex(acc_st4step, either_token_expr_or_symbol_expr, begin_position, may_end_position)
        check_tmay(tmay_step_eresult)

        (acc_lock_st, is_with_user_result) = acc_st5above
        if is_with_user_result is not bool(tmay_step_eresult): raise logic-err
            # call _eval__step to handle refcount
            #
        return (step_eGrammarAttribute, tmay_step_eresult)
    def _0eval__step_ex(sf, acc_st4step, either_token_expr_or_symbol_expr, begin_position, may_end_position, /):
        tmay_middle_st = sf._get_tmay_cached_middle_st(either_token_expr_or_symbol_expr, begin_position, may_end_position)
        if not tmay_middle_st: raise logic-err
        [middle_st] = tmay_middle_st
        if middle_st.refcount <= 0: raise logic-err
        middle_st.refcount -= 1

        (acc_lock_st, is_with_user_result) = acc_st4step
        if not is_with_user_result:
            tmay_step_eresult = null_tuple
            return tmay_step_eresult
        if not hasattr(middle_st, 'eresult'):
            acc_st5above = acc_st4step
            sf._eval_and_write__middle_st(acc_st5above, either_token_expr_or_symbol_expr, begin_position, may_end_position, middle_st)

        eresult = middle_st.eresult
        tmay_step_eresult = mk_Just(eresult)
        step_eGrammarAttribute = middle_st.eGrammarAttribute
        return (step_eGrammarAttribute, tmay_step_eresult)
    def _eval_and_write__middle_st(sf, acc_st5above, either_token_expr_or_symbol_expr, begin_position, may_end_position, middle_st, /):
        assert not hasattr(middle_st, 'eresult')
        (is_right, x) = eGrammarAttribute = middle_st.eGrammarAttribute
        if not is_right:
            eresult = eGrammarAttribute
            middle_st.eresult = eresult
            return
        GrammarAttribute = x

        either_token_expr_or_symbol_expr = middle_st._cached__either_token_expr_or_symbol_expr
        (is_right, x) = either_token_expr_or_symbol_expr
        if not is_right:
            token_expr = x
            (is_right, x) = middle_st._conditional_cached__either_token_acceptor_or_recognizer_and_inner_st_controller
            if is_right:raise logic-err
            token_acceptor = x
            rsymbol = token2rsymbol(executor, token)
            raw_value = token2raw_value(executor, token)
            meresult = rsymbol_raw_value_GrammarAttribute2meresult(token_acceptor, rsymbol, raw_value, GrammarAttribute)
            (is_right, x) = meresult
            if is_right:
                eresult = meresult
            else:
                errmsg = x
                herrmsg_ex = mk_Left(errmsg)
                errmsg_ex = (ErrmsgEx
                (begin_position=middle_st.begin_position
                ,may_end_position=??到底要不要重建实际的may_end_position?may_end_position
                    只需 比较 (is may_end_position)是的话 替换为None就行了 TODO
                ,farthest_touched_end_position
                =farthest_touched_end_position
                ,does_try_to_read_token_at_end_position
                =does_try_to_read_token_at_end_position
                ,either_token_expr_or_symbol_expr
                =either_token_expr_or_symbol_expr
                ,herrmsg_ex=herrmsg_ex
                ))
            meresult -> eresult
            xxxxxxxxx
            ..
            middle_st.eresult = eresult
            return
        symbol_expr = x
        #(recognizer, inner_st_controller) = symbol_expr2recognizer_and_inner_st_controller(executor, symbol_expr)
        (is_right, x) = middle_st._conditional_cached__either_token_acceptor_or_recognizer_and_inner_st_controller
        if not is_right:raise logic-err
            #1. eGrammarAttribute is ok
            #2. loop_body under symbol_expr
        recognizer, inner_st_controller = x

        #middle_st exists
        #==>> middle_st.eGrammarAttribute exists
        #!!symbol_expr
        #==>> _on__final_inner_st success
        #==>> middle_st....reversed... exists
        reversed__pair_seq_about____noninitial_inner_st___prev__either_prestepinto_failcase_or_step_position_rng_endby_far_and_either_token_expr_or_symbol_expr4as_if_success_and_noninitial_inner_st4as_if_success = middle_st._conditional_cached__reversed__pair_seq_about____noninitial_inner_st___prev__either_prestepinto_failcase_or_step_position_rng_endby_far_and_either_token_expr_or_symbol_expr4as_if_success_and_noninitial_inner_st4as_if_success
            #see:_on__final_inner_st
        ps = []
            #reversed[(noninitial_inner_st, prev_step__either_prestepinto_failcase_or_eGrammarAttribute_and_tmay_eresult)]
        for noninitial_inner_st, prev__either_prestepinto_failcase_or_step_position_rng_endby_far_and_either_token_expr_or_symbol_expr4as_if_success_and_noninitial_inner_st4as_if_success in reversed__pair_seq_about____noninitial_inner_st___prev__either_prestepinto_failcase_or_step_position_rng_endby_far_and_either_token_expr_or_symbol_expr4as_if_success_and_noninitial_inner_st4as_if_success:
            prev_step__either_prestepinto_failcase_or_eGrammarAttribute_and_tmay_eresult = sf._eval_and_write__middle_st__loop_body(acc_st5above, either_token_expr_or_symbol_expr, begin_position, may_end_position, middle_st, GrammarAttribute, symbol_expr, recognizer, inner_st_controller, noninitial_inner_st, prev__either_prestepinto_failcase_or_step_position_rng_endby_far_and_either_token_expr_or_symbol_expr4as_if_success_and_noninitial_inner_st4as_if_success)
            ps.append((noninitial_inner_st, prev_step__either_prestepinto_failcase_or_eGrammarAttribute_and_tmay_eresult))
        xxxxxxxxx
        ps
    def _eval_and_write__middle_st__loop_body(sf, acc_st5above, either_token_expr_or_symbol_expr, begin_position, may_end_position, middle_st, GrammarAttribute, symbol_expr, recognizer, inner_st_controller, noninitial_inner_st, prev__either_prestepinto_failcase_or_step_position_rng_endby_far_and_either_token_expr_or_symbol_expr4as_if_success_and_noninitial_inner_st4as_if_success, /):
        (is_right, x) = prev__either_prestepinto_failcase_or_step_position_rng_endby_far_and_either_token_expr_or_symbol_expr4as_if_success_and_noninitial_inner_st4as_if_success
        if not is_right:
            prev_step__either_prestepinto_failcase_or_eGrammarAttribute_and_tmay_eresult = prev__either_prestepinto_failcase_or_step_position_rng_endby_far_and_either_token_expr_or_symbol_expr4as_if_success_and_noninitial_inner_st4as_if_success
            return prev_step__either_prestepinto_failcase_or_eGrammarAttribute_and_tmay_eresult

        step_position_rng_endby_far_and_either_token_expr_or_symbol_expr4as_if_success_and_noninitial_inner_st4as_if_success = x
        #bug:if not is_step_success_noninitial_inner_st(inner_st_controller, noninitial_inner_st):raise logic-err

        ((step_begin_position, step_farthest_touched_end_position), step_either_token_expr_or_symbol_expr4as_if_success, noninitial_inner_st4as_if_success) = step_position_rng_endby_far_and_either_token_expr_or_symbol_expr4as_if_success_and_noninitial_inner_st4as_if_success
        acc_st4step = step_success_noninitial_inner_st2prev_acc_st4step(inner_st_controller, acc_st5above, noninitial_inner_st4as_if_success)
        (step_eGrammarAttribute, tmay_step_eresult) = sf._eval__step_ex(acc_st5above, acc_st4step, step_either_token_expr_or_symbol_expr4as_if_success, step_begin_position, step_farthest_touched_end_position)
        prev_step__either_prestepinto_failcase_or_eGrammarAttribute_and_tmay_eresult = mk_Right((step_eGrammarAttribute, tmay_step_eresult))

        return prev_step__either_prestepinto_failcase_or_eGrammarAttribute_and_tmay_eresult

    .eval_whole_eresult
        .basic_eval_whole_eresult :: reversed[(noninitial_inner_st, prev_step__either_prestepinto_failcase_or_eGrammarAttribute_and_tmay_eresult/__without_user_result)] -> GrammarAttribute -> heresult
        .filters4whole :: [GrammarAttribute->result -> result]
            # heGrammarAttribute -> heresult return errmsg_ex directly
            # so,only (GrammarAttribute,result)
        .step_success_noninitial_inner_st2prev_step_filters
            xxx .nonfinal_inner_st2next_step_success_filters
            step_success_filter :: step_GrammarAttribute->step_result->step_result
            is_step_success_noninitial_inner_st
            step_success_noninitial_inner_st



        ..
        ..
        return either_prestepinto_failcase_or_tmay_step_eresult5pruning
    def _stack_push(sf, x, /):
        i6stack = len(sf.stack)
        sf.stack.append(x)
        if not type(x) is StackItem:
            return
        stack_item = x
        stack_idc = sf._get_stack_idc__stack_item(stack_item)
        stack_idc.append(i6stack)
        return
    def _stack_pop(sf, /):
        x = sf.stack.pop()
        if not type(x) is StackItem:
            return x
        stack_item = x
        i6stack = len(sf.stack)
        stack_idc = sf._get_stack_idc__stack_item(stack_item)
        if not i6stack == stack_idc.pop(): raise logic-err
        return stack_item
    def _get_xuserdata__position(sf, position, /):
        stream = sf.cuttable_stream
        stream.seek__position(position)
        xuserdata = stream.peak1__xuserdata__relax()
        return xuserdata
    def _get_stack_idc__stack_item(sf, stack_item, /):
        begin_position = stack_item.begin_position
        xuserdata = sf._get_xuserdata__position(begin_position)
        stack_idc = xuserdata.stack_idc4stack_item_begin_here
        return stack_idc

    def symbol_expr2recognizer_and_inner_st_controller(executor, symbol_expr, /)
    def recognize(executor, lock_mask5above, symbol_expr, begin_position, may_end_position, /):
        check_type_is(LockMask, lock_mask5above)
        check_type_is(Position, begin_position)
        if may_end_position is not None: check_type_is(Position, may_end_position)

        check_type_le(HSymbolExpr, symbol_expr)
        check_position_rng(begin_position, may_end_position)
            #to avoid final-stack[-1] be (Left FailCase_pre_stepinto.is_bad_position_rng)
            #!! (Left FailCase_pre_stepinto.has_no_step_success) only ocurr as tmp-step-push
            #==>> final-stack[-1] contains middle_st

        acc_st5above = lock_mask2acc_st(lock_mask5above)
            #vs: lock_mask2acc_st,step_success_noninitial_inner_st2prev_acc_st4step
        stack = sf.stack
        if stack: raise logic-err
        sf._uncached_put__symbol_expr(acc_st5above, symbol_expr, begin_position, may_end_position)
        [stack_item] = stack
        sf._main_loop()
        [(acc_st5above, either_token_expr_or_symbol_expr, begin_position, may_end_position, middle_st)] = stack
            #since not is_bad_position_rng
        stack_item.eresult/eGrammarAttribute
        return ..

    def moveon_last_stack_elem__aftter_tmp_push_middle_st(sf, /):
        '-> is_stop'
        stack = sf.stack
        either_prestepinto_failcase_or_step_IO = sf._stack_pop()
        check_either(either_prestepinto_failcase_or_step_IO)
        (is_right, x) = either_prestepinto_failcase_or_step_IO
        _tmay_middle_st = null_tuple
        if is_right:
            step_IO = x
            check_type_is(tuple, step_IO)
            (acc_st5above, either_token_expr_or_symbol_expr, begin_position, may_end_position, middle_st) = step_IO
            check_type_is(MiddleState, middle_st)
            _tmay_middle_st = mk_Just(middle_st)
            stack_item._conditional_cached__step_farthest_touched_end_position = middle_st.farthest_touched_end_position
            step_eGrammarAttribute = middle_st.eGrammarAttribute
            check_either(step_eGrammarAttribute)
            either_prestepinto_failcase_or_step_eGrammarAttribute = mk_Right(step_eGrammarAttribute)
        else:
            prestepinto_failcase = x
            either_prestepinto_failcase_or_step_eGrammarAttribute = either_prestepinto_failcase_or_step_IO
        either_prestepinto_failcase_or_step_eGrammarAttribute
        if not stack:
            sf._stack_push(either_prestepinto_failcase_or_step_eGrammarAttribute)
            return True


        stack_item = stack[-1]
        stack_item.either_prestepinto_failcase_or_step_eGrammarAttribute = either_prestepinto_failcase_or_step_eGrammarAttribute
        stack_item._tmay_middle_st = _tmay_middle_st

        common = stack_item.common
        inner_st_controller = common.inner_st_controller
        inner_st = stack_item.inner_st
        if is_final_inner_st(inner_st_controller, inner_st): raise logic-err
            #final_inner_st = inner_st
            #since this func is to move on...
        nonfinal_inner_st = inner_st
        (is_right, x) = stack_item.he_accGrammarAttribute5until_curr_inner_st
        if not is_right: raise logic-err
            #see:_on__errmsg_ex
        accGrammarAttribute5until_curr_inner_st = x

        he_accGrammarAttribute4next = binop4acc__he_accGrammarAttribute(recognizer, accGrammarAttribute5until_curr_inner_st, either_prestepinto_failcase_or_step_eGrammarAttribute, next_inner_st)


        #find out is_on_success
        #   no matter whether he_accGrammarAttribute4next is err
        #
        (is_right, x) = either_prestepinto_failcase_or_step_eGrammarAttribute
        if is_right:
            step_eGrammarAttribute = x
            (is_right, x) = step_eGrammarAttribute
            if is_right:
                step_GrammarAttribute = x
            else:
                errmsg_ex = x
        else:
            prestepinto_failcase = x
        is_right

        is_on_success = is_right
        tmay_next_inner_st = moveon_nonfinal_inner_st2tmay_next_inner_st(inner_st_controller, is_on_success, nonfinal_inner_st)
        if not tmay_next_inner_st:
            #raise logic-err in 'step fail but has_no_step_fail'
            #step_fail__but__has_no_step_fail_next_inner_st
            raise Error__has_no_step_fail
            r'''
            tmay_heresult = handle4step_fail__but__has_no_step_fail_next_inner_st(recognizer, nonfinal_inner_st)
            if not tmay_heresult:
                raise Error__has_no_step_fail
            [heresult] = tmay_heresult
            sf._return__symbol_expr__heGrammarAttribute(heGrammarAttribute)
                #raise global_err if ()
                #else tmp_push_middle_st
            return False
            '''#'''
        [next_inner_st] = tmay_next_inner_st
        lock_mask4step = step_success_noninitial_inner_st2prev_lock_mask(inner_st_controller, next_inner_st)


        vars4whole_symbol_expr = dict(
                begin_position
                =common.begin_position
                ,may_end_position
                =common.may_end_position
                )

        def prev1s_inner_st2vars(prev1s_inner_st4next, /):
            #prev1s_inner_st4next before_lt next_inner_st
            #prev1s_inner_st4next before_le curr_inner_st
            #prev1s_inner_st4next is not initial_inner_st otherwise using vars4whole_symbol_expr...
            #
            if is_initial_inner_st(inner_st_controller, prev1s_inner_st4next): raise logic-err
            for stack_item in reversed(stack):
                if is_initial_inner_st(inner_st_controller, stack_item.inner_st): raise logic-err
                if not stack_item.common is common: raise logic-err
                if stack_item.inner_st == prev1s_inner_st4next:
                    break
            else:raise logic-err
            stack_item
            d = _tail__4_prev1s_inner_st2vars(stack_item)
            return d

        #end-def prev1s_inner_st2vars(prev1s_inner_st4next, /):
        get = dict.__getitem__
        begin_position4next = inner_st2begin_position(inner_st_controller, get, vars4whole_symbol_expr, prev1s_inner_st2vars, stack_item.inner_st)
        may_end_position4next = inner_st2may_end_position(inner_st_controller, get, vars4whole_symbol_expr, prev1s_inner_st2vars, stack_item.inner_st)
        (farthest_touched_end_position4next, does_try_read_token_at_end_position4next) = _acc__farthest_ex(stack_item)

        sf._put__symbol_expr__inner_st(common = common
            ,inner_st = next_inner_st
            ,begin_position
            =begin_position4next
            ,may_end_position
            =may_end_position4next
            ,farthest_touched_end_position5until_curr_inner_st
            =farthest_touched_end_position4next
            ,does_try_read_token_at_end_position5until_curr_inner_st
            =does_try_read_token_at_end_position4next
            ,he_accGrammarAttribute5until_curr_inner_st
            =he_accGrammarAttribute4next
            )
        return False
    #end-def moveon_last_stack_elem__aftter_tmp_push_middle_st(sf, /):
    def _return__symbol_expr__heGrammarAttribute(sf, stack_item, heGrammarAttribute, /):
        raise logic-err#not used
        #stack_item = sf.stack[-1]
        eGrammarAttribute = stack_item.he_XXX2e_XXX5until_curr_inner_st(heGrammarAttribute)
        sf._return__symbol_expr__eGrammarAttribute(eGrammarAttribute)
    def _return__symbol_expr__eGrammarAttribute(sf, eGrammarAttribute, /, **extra_kw4middle_st):
        #return from step_into
        #stack nonempty
        #stack[-1] must be StackItem
        #???xxx stack[-1] may be nonfinal_inner_st xxx
        #pop all stack_item about symbol_expr until-included initial_inner_st
        #tmp_push_middle_st
        #
        stack = sf.stack
        if not stack: raise logic-err
        stack_item = stack[-1]
        check_type_is(StackItem, stack_item)

        common = stack_item.common
        inner_st_controller = common.inner_st_controller

        (is_right, x) = eGrammarAttribute
        is_success = is_right
        if is_success:
            if not is_success_final_inner_st(inner_st_controller, stack_item.inner_st): raise logic-err
            stop_position_before_return = stop_item.begin_position
        else:
            #fail ==>> __return
            stop_position_before_return = common.begin_position
        stop_position_before_return

        middle_st = (MiddleState
        (refcount=0
        ,begin_position
        =common.begin_position
        ,farthest_touched_end_position
        =stack_item.farthest_touched_end_position5until_curr_inner_st
        ,does_try_to_read_token_at_end_position
        =stack_item.does_try_to_read_token_at_end_position
        ,stop_position_before_return
        =stop_position_before_return
        ,eGrammarAttribute
        =eGrammarAttribute
        , **extra_kw4middle_st
        ))
        if is_success:
            either_token_acceptor_or_recognizer = mk_Right((stack_item.recognizer, stack_item.inner_st_controller))
            middle_st._conditional_cached__either_token_acceptor_or_recognizer_and_inner_st_controller = either_token_acceptor_or_recognizer

        #pops...
        #[pops__at__return__symbol_expr__eGrammarAttribute]
        while stack and common is stack[-1].common:
            stack_item0 = sf._stack_pop()
        if not is_initial_inner_st(inner_st_controller, stack_item0.inner_st): raise logic-err

        acc_st5above = common.acc_st5above
        either_token_expr_or_symbol_expr = mk_Right(common.symbol_expr)
        begin_position = common.begin_position
        may_end_position = common.may_end_position
        middle_st
        sf._return__middle_st(acc_st5above, either_token_expr_or_symbol_expr, begin_position, may_end_position, middle_st)
    def _main_loop(sf, /):
        stack = sf.stack
        if not stack: raise logic-err
        #xxx stack.append(None)
        #while stack:
        while 1:
            #xxx stack.pop()
            #   pop when err or final_inner_st
            stack_item = stack[-1]
                #no:pop
            if not type(stack_item) is StackItem:
                is_stop = sf.moveon_last_stack_elem__aftter_tmp_push_middle_st()
                if is_stop:
                    return
                continue

            (is_right, x) = stack_item.he_accGrammarAttribute5until_curr_inner_st
            if not is_right:
                herrmsg_ex = x
                sf._on__herrmsg_ex(stack_item, herrmsg_ex)
                continue
            accGrammarAttribute5until_curr_inner_st = x

            begin_position = stack_item.begin_position
            may_end_position = stack_item.may_end_position
            is_bad_position_rng = not position_le_ex(begin_position, may_end_position)

            common = stack_item.common
            inner_st_controller = common.inner_st_controller
            if is_final_inner_st(inner_st_controller, stack_item.inner_st):
                final_inner_st = stack_item.inner_st
                sf._on__final_inner_st(stack_item, accGrammarAttribute5until_curr_inner_st, final_inner_st, begin_position, may_end_position, is_bad_position_rng, common, inner_st_controller)
                continue
            nonfinal_inner_st = stack_item.inner_st
            if is_bad_position_rng:
                sf._stack_push(mk_Left(FailCase_pre_stepinto.is_bad_position_rng))
                continue

            sf._on__nonfinal_inner_st(stack_item, accGrammarAttribute5until_curr_inner_st, nonfinal_inner_st, begin_position, may_end_position, common, inner_st_controller)
            continue
    #def _on__errmsg_ex(sf, stack_item, errmsg_ex, /):
    def _on__herrmsg_ex(sf, stack_item, herrmsg_ex, /):
        heGrammarAttribute = mk_Left(herrmsg_ex)
        eGrammarAttribute = stack_item.he_XXX2e_XXX5until_curr_inner_st(heGrammarAttribute)
        sf._return__symbol_expr__eGrammarAttribute(eGrammarAttribute)
        return
    def _on__final_inner_st(sf, stack_item, accGrammarAttribute, final_inner_st, begin_position, may_end_position, is_bad_position_rng, common, inner_st_controller, /):
        if not is_final_inner_st(inner_st_controller, final_inner_st): raise logic-error
        recognizer = common.recognizer
        if is_success_final_inner_st(inner_st_controller, final_inner_st):
            success_final_inner_st = final_inner_st
            heGrammarAttribute = finalize4success4acc__he_accGrammarAttribute(recognizer, accGrammarAttribute, success_final_inner_st, is_bad_position_rng)
        else:
            fail_final_inner_st = final_inner_st
            herrmsg_ex = finalize4fail4acc__he_accGrammarAttribute(recognizer, accGrammarAttribute, fail_final_inner_st, is_bad_position_rng)
            heGrammarAttribute = mk_Left(herrmsg_ex)
        heGrammarAttribute

        eGrammarAttribute = stack_item.he_XXX2e_XXX5until_curr_inner_st(heGrammarAttribute)
        #sf._return__symbol_expr__eGrammarAttribute(eGrammarAttribute, _final_inner_st=final_inner_st)
        xxxxxxxxx
        reversed__pair_seq_about____noninitial_inner_st___prev__either_prestepinto_failcase_or_step_position_rng_endby_far_and_either_token_expr_or_symbol_expr4as_if_success_and_noninitial_inner_st4as_if_success =

        sf._return__symbol_expr__eGrammarAttribute(eGrammarAttribute, _conditional_cached__reversed__pair_seq_about____noninitial_inner_st___prev__either_prestepinto_failcase_or_step_position_rng_endby_far_and_either_token_expr_or_symbol_expr4as_if_success_and_noninitial_inner_st4as_if_success=reversed__pair_seq_about____noninitial_inner_st___prev__either_prestepinto_failcase_or_step_position_rng_endby_far_and_either_token_expr_or_symbol_expr4as_if_success_and_noninitial_inner_st4as_if_success)
        return

    def _on__nonfinal_inner_st(sf, stack_item, accGrammarAttribute5until_curr_inner_st, nonfinal_inner_st, begin_position, may_end_position, common, inner_st_controller, /):
        check_position_rng(begin_position, may_end_position)
        tmay_next_inner_st4success = moveon_nonfinal_inner_st2tmay_next_inner_st(inner_st_controller, True, nonfinal_inner_st)
        if not tmay_next_inner_st4success:
            [] = tmay_next_inner_st4success
            [next_inner_st4fail] = moveon_nonfinal_inner_st2tmay_next_inner_st(inner_st_controller, False, nonfinal_inner_st)
                #nonfinal_inner_st MUST have one next_inner_st
            sf._stack_push(mk_Left(FailCase_pre_stepinto.has_no_step_success))
            return
        [next_inner_st4success] = tmay_next_inner_st4success
        #
        acc_st5above = common.acc_st5above
        acc_st4step = step_success_noninitial_inner_st2prev_acc_st4step(inner_st_controller, acc_st5above, next_inner_st4success)
        either_token_expr_or_symbol_expr = step_success_noninitial_inner_st2prev_either_token_expr_or_symbol_expr(recognizer, next_inner_st4success)
        check_either(either_token_expr_or_symbol_expr)
        #stack_item._conditional_cached__acc_st4step = acc_st4step
        stack_item._conditional_cached__either_token_expr_or_symbol_expr4as_if_success_and_acc_st4step = (either_token_expr_or_symbol_expr, acc_st4step)
        sf._put__either_token_expr_or_symbol_expr(acc_st4step, either_token_expr_or_symbol_expr, begin_position, may_end_position)
        return
    def _read_tmay_token_ex(executor, begin_position, may_end_position, /):

        stream = sf.cuttable_stream
        stream.seek__position(begin_position)
        if may_end_position is None:
            tmay_token = stream.read_le(1)
        else:
            end_position = may_end_position
            if end_position is begin_position:
                tmay_token = null_tuple
            elif position_le_ex(end_position, begin_position): raise logic-err
            else:
                tmay_token = stream.read_le(1)
        stop_position_before_return = stream.tell()
        check_position_rng(stop_position_before_return, may_end_position)
        tmay_token
        #no:stop_position
        return tmay_token, stop_position_before_return
    def _uncached_putpopput__token_expr(executor, acc_st5above, token_expr, begin_position, may_end_position, /):
        #_uncached_put__symbol_expr
        check_position_rng(begin_position, may_end_position)

        token_acceptor = token_expr2token_acceptor(executor, token_expr)
        #read token
        tmay_token, stop_position_before_return = executor._read_tmay_token_ex(begin_position, may_end_position)
        #no:stop_position


        if not tmay_token:
            [] = tmay_token
            if not begin_position is stop_position_before_return: raise logic-error
            does_try_to_read_token_at_end_position = True
            farthest_touched_end_position = begin_position
            errmsg = 'try_to_read_token_at_end_position'
            is_err = True

        else:
            [token] = tmay_token
            if begin_position is stop_position_before_return: raise logic-error
            does_try_to_read_token_at_end_position = False
            farthest_touched_end_position = stop_position_before_return
            stop_position_before_return
            #accept_token(token_acceptor, token)
            rsymbol = token2rsymbol(executor, token)
            meGrammarAttribute = rsymbol2meGrammarAttribute(token_acceptor, rsymbol)
            (is_right, x) = meGrammarAttribute
            if is_right:
                GrammarAttribute = x
                eGrammarAttribute = heGrammarAttribute
                is_err = False
            else:
                errmsg = x
                is_err = True
        #########
        if is_err:
            errmsg
            herrmsg_ex = mk_Left(errmsg)
            errmsg_ex = (ErrmsgEx
            (begin_position=begin_position
            ,may_end_position=may_end_position
            ,farthest_touched_end_position
            =farthest_touched_end_position
            ,does_try_to_read_token_at_end_position
            =does_try_to_read_token_at_end_position
            ,either_token_expr_or_symbol_expr
            =either_token_expr_or_symbol_expr
            ,herrmsg_ex=herrmsg_ex
            ))
            eGrammarAttribute = mk_Left(errmsg_ex)
        eGrammarAttribute
        #xxx sf._return__symbol_expr__heGrammarAttribute

        middle_st = (MiddleState
        (refcount=0
        ,begin_position
        =begin_position
        ,farthest_touched_end_position
        =farthest_touched_end_position
        ,does_try_to_read_token_at_end_position
        =does_try_to_read_token_at_end_position
        ,stop_position_before_return
        =stop_position_before_return
        ,eGrammarAttribute
        =eGrammarAttribute
        ))
        if not is_err:
            either_token_acceptor_or_recognizer = mk_Left(token_acceptor)
            middle_st._conditional_cached__either_token_acceptor_or_recognizer_and_inner_st_controller = either_token_acceptor_or_recognizer

        sf._return__middle_st(acc_st5above, either_token_expr_or_symbol_expr, begin_position, may_end_position, middle_st)
        return
    #end-def _uncached_putpopput__token_expr
    def _return__middle_st(sf, acc_st5above, either_token_expr_or_symbol_expr, begin_position, may_end_position, middle_st, /):
        #_return__symbol_expr__eGrammarAttribute
        sf._save__middle_st(either_token_expr_or_symbol_expr, begin_position, may_end_position, middle_st)
        .. pruning
        sf._stack_push(Right((acc_st5above, either_token_expr_or_symbol_expr, begin_position, may_end_position, middle_st)))
        return

    def _reduce_info4cache(sf, either_token_expr_or_symbol_expr, begin_position, /):
        check_either(either_token_expr_or_symbol_expr)
        (token_expr_vs_symbol_expr, token_expr_or_symbol_expr) = either_token_expr_or_symbol_expr

        xuserdata = sf._get_xuserdata__position(begin_position)
        if token_expr_vs_symbol_expr is False:
            #token_expr
            expr2sz2middle_st = xuserdata.token_expr2relative_end_position2middle_st
            expr2gmax_sz = xuserdata.token_expr2eof_or_free_relative_farthest_touched_end_position
        else:
            #symbol_expr
            expr2sz2middle_st = xuserdata.symbol_expr2relative_end_position2middle_st
            expr2gmax_sz = xuserdata.symbol_expr2eof_or_free_relative_farthest_touched_end_position
        expr2sz2middle_st
        expr2gmax_sz
        expr = token_expr_or_symbol_expr
        return (expr, expr2gmax_sz, expr2sz2middle_st)

    def _get_tmay_cached_middle_st(sf, either_token_expr_or_symbol_expr, begin_position, may_end_position, /):
        #donot change refcount
        #_save__middle_st
        tmay_middle_st = sf._0get_tmay_cached_middle_st(either_token_expr_or_symbol_expr, begin_position, may_end_position)
        check_tmay(tmay_middle_st)
        if tmay_middle_st:
            [middle_st] = tmay_middle_st
            #ok!! if middle_st.refcount==0: raise logic-err
        return tmay_middle_st

    def _0get_tmay_cached_middle_st(sf, either_token_expr_or_symbol_expr, begin_position, may_end_position, /):
        (expr, expr2gmax_sz, expr2sz2middle_st) = sf._reduce_info4cache(either_token_expr_or_symbol_expr, begin_position)

        if not may_end_position is None:
            end_position = may_end_position
            sz4try = position_diff(end_position, begin_position)
            check_uint(sz4try)

        if expr in expr2gmax_sz:
            gmax_sz = expr2gmax_sz[expr]
            if may_end_position is None or sz4try >= gmax_sz:
                sz = gmax_sz
                middle_st = expr2sz2middle_st[expr][sz]
                return mk_Just(middle_st)
            assert sz4try < gmax_sz
        sz4try

        may_middle_st = expr2sz2middle_st[expr].get(sz)
        if may_middle_st is None:
            return null_tuple
        middle_st = may_middle_st
        tmay_middle_st = mk_Just(middle_st)
        return tmay_middle_st

    def _save__middle_st(sf, either_token_expr_or_symbol_expr, begin_position, may_end_position, middle_st, /):
        #_get_tmay_cached_middle_st
        #ok:if not middle_st.refcount==0: raise logic-err
        if not middle_st.refcount < 0: raise logic-err
        middle_st.refcount += 1

        tmay_middle_st = sf._get_tmay_cached_middle_st(either_token_expr_or_symbol_expr, begin_position, may_end_position)
        if tmay_middle_st:
            [_middle_st] = tmay_middle_st
            if middle_st is not _middle_st: raise logic-err
            return
        assert middle_st.refcount == 1
        assert middle_st.begin_position is begin_position
        middle_st._cached__either_token_expr_or_symbol_expr = either_token_expr_or_symbol_expr

        (expr, expr2gmax_sz, expr2sz2middle_st) = sf._reduce_info4cache(either_token_expr_or_symbol_expr, begin_position)

        sz4far = position_diff(middle_st.farthest_touched_end_position, begin_position)
        check_uint(sz4far)
        if may_end_position is None or not middle_st.does_try_to_read_token_at_end_position:
            gmax_sz = sz4far
            if expr in expr2gmax_sz:raise logic-err
            expr2gmax_sz[expr] = gmax_sz
        sz = sz4far
        sz2middle_st = expr2sz2middle_st.setdefault(expr, {})
        if sz in sz2middle_st:raise logic-err
        sz2middle_st[sz] = middle_st
        return





    def _put__either_token_expr_or_symbol_expr(sf, acc_st5above, either_token_expr_or_symbol_expr, begin_position, may_end_position, /):
        check_either(either_token_expr_or_symbol_expr)
        check_position_rng(begin_position, may_end_position)
        tmay_middle_st = sf._get_tmay_cached_middle_st(either_token_expr_or_symbol_expr, begin_position, may_end_position)
        if tmay_middle_st:
            [middle_st] = tmay_middle_st
            sf._return__middle_st(acc_st5above, either_token_expr_or_symbol_expr, begin_position, may_end_position, middle_st)
            return
        #uncached yet
        (is_right, x) = either_token_expr_or_symbol_expr
        if is_right:
            symbol_expr = x
            sf._uncached_put__symbol_expr(acc_st5above, symbol_expr, begin_position, may_end_position)
            return
        token_expr = x
        #   since vivi push new stack_item
        #

        #as-if push new stack_item for token
        #   then handle and pop
        sf._uncached_putpopput__token_expr(acc_st5above, token_expr, begin_position, may_end_position)
        return

    def _uncached_put__symbol_expr(sf, acc_st5above, symbol_expr, begin_position, may_end_position, /):
        #_uncached_putpopput__token_expr
        check_position_rng(begin_position, may_end_position)
        .. handle4left_corner_recur

        (recognizer, inner_st_controller) = symbol_expr2recognizer_and_inner_st_controller(executor, symbol_expr)
        common4item = (CommonData4StackItem
            (acc_st5above
            =acc_st5above
            ,begin_position
            =begin_position
            ,may_end_position
            =may_end_position
            ,symbol_expr
            =symbol_expr
            ,recognizer
            =recognizer
            ,inner_st_controller
            =inner_st_controller
            ))
        initial_inner_st = get_initial_inner_st(inner_st_controller)
        he_accGrammarAttribute5until_curr_inner_st = init4acc__he_accGrammarAttribute(recognizer)
        sf._put__symbol_expr__inner_st(common = common4item
            ,inner_st = initial_inner_st
            ,begin_position
            =begin_position
            ,may_end_position
            =may_end_position
            ,farthest_touched_end_position5until_curr_inner_st
            =begin_position
            ,does_try_read_token_at_end_position5until_curr_inner_st
            =False
            ,he_accGrammarAttribute5until_curr_inner_st
            =he_accGrammarAttribute5until_curr_inner_st
            )


    def _put__symbol_expr__inner_st(sf, /, common, inner_st, begin_position, may_end_position, farthest_touched_end_position5until_curr_inner_st, does_try_read_token_at_end_position5until_curr_inner_st, he_accGrammarAttribute5until_curr_inner_st):
        kw = {**locals()}
        del kw['sf']
        stack_item = StackItem(**kw)
        sf._stack_push(stack_item)
mk_CompactDataType_then_write_to_module(
    'ErrmsgEx'
    #errmsg_ex
    ,__name__
    ,r'''
    begin_position
    may_end_position
    farthest_touched_end_position
    does_try_to_read_token_at_end_position
    either_token_expr_or_symbol_expr
    herrmsg_ex
    '''#'''
    #(begin_position, may_end_position) for whole symbol_expr not at inner_st
    #herrmsg_ex is for inner_st
)

mk_CompactDataType_then_write_to_module(
    'CommonData4StackItem'
    ,__name__
    ,r'''
    acc_st5above
    begin_position
    may_end_position
    symbol_expr
    recognizer
    inner_st_controller
    '''#'''
)
CommonData4StackItem


#stack_item
mk_CompactDataType_then_write_to_module(
    'StackItem'
    ,__name__
    ,r'''
    common
    inner_st
    begin_position
    may_end_position
    farthest_touched_end_position5until_curr_inner_st
    does_try_read_token_at_end_position5until_curr_inner_st
    he_accGrammarAttribute5until_curr_inner_st

    either_prestepinto_failcase_or_step_eGrammarAttribute
        _tmay_middle_st
        _conditional_cached__either_token_expr_or_symbol_expr4as_if_success_and_acc_st4step
        _conditional_cached__step_farthest_touched_end_position
    either_prestepinto_failcase_or_tmay_step_eresult5pruning
    '''#'''
        #accGrammarAttribute5until_curr_inner_st
        #e_accGrammarAttribute5until_curr_inner_st
        #
        #either_prestepinto_failcase_or_tmay_step_eresult5pruning
        #   without result ==>> ()
        #   is_bad_position_rng ==>> (Left is_bad_position_rng,)
        #   has_no_step_success ==>> (Left has_no_step_success,)
        #   otherwise ==>> (Right step_eresult5pruning(
        # removed:_conditional_cached__acc_st4step
        #
        #_tmay_middle_st: used in prev1s_inner_st2vars@moveon_last_stack_elem__aftter_tmp_push_middle_st
)


def _():
    @property
    def e_accGrammarAttribute5until_curr_inner_st(sf, /):
        he_XXX = sf.he_accGrammarAttribute5until_curr_inner_st
        return sf.he_XXX2e_XXX5until_curr_inner_st(he_XXX)
    def he_XXX2e_XXX5until_curr_inner_st(sf, he_XXX, /):
        (is_right, x) = he_XXX
        if is_right:
            XXX = x
            e_XXX = he_XXX
            return e_XXX
        #########
        herrmsg_ex = x
        common = sf.common

        errmsg_ex = (ErrmsgEx
        (herrmsg_ex = herrmsg_ex
        ,begin_position = common.begin_position
        ,may_end_position = common.may_end_position
        ,symbol_expr = common.symbol_expr
        ,farthest_touched_end_position
        =sf.farthest_touched_end_position5until_curr_inner_st
        ,does_try_to_read_token_at_end_position
        =sf.does_try_to_read_token_at_end_position5until_curr_inner_st
        ,inner_st = sf.inner_st
        #,begin_position = sf.begin_position
        #,may_end_position = sf.may_end_position
        ))
        e_XXX = mk_Left(errmsg_ex)
        return e_XXX

    def using_initial_inner_st(sf, /):
        return is_initial_inner_st(sf.common.inner_st_controller, sf.inner_st)
    StackItem.e_accGrammarAttribute5until_curr_inner_st = e_accGrammarAttribute5until_curr_inner_st
    StackItem.he_XXX2e_XXX5until_curr_inner_st = he_XXX2e_XXX5until_curr_inner_st
    StackItem.using_initial_inner_st = using_initial_inner_st

_()

#middle_st
mk_CompactDataType_then_write_to_module(
    'MiddleState'
    ,__name__
    ,r'''
    refcount
    begin_position
    farthest_touched_end_position
    does_try_to_read_token_at_end_position
    stop_position_before_return
    eGrammarAttribute
        _conditional_cached__reversed__pair_seq_about____noninitial_inner_st___prev__either_prestepinto_failcase_or_step_position_rng_endby_far_and_either_token_expr_or_symbol_expr4as_if_success_and_noninitial_inner_st4as_if_success
        _cached__either_token_expr_or_symbol_expr
        _conditional_cached__either_token_acceptor_or_recognizer_and_inner_st_controller
    eresult
    '''#'''
    #no:stop_position
    #see:get_stop_position
    #_conditional_cached__reversed__pair_seq_about____noninitial_inner_st___prev__either_prestepinto_failcase_or_step_position_rng_endby_far_and_either_token_expr_or_symbol_expr4as_if_success_and_noninitial_inner_st4as_if_success/_cached__either_token_expr_or_symbol_expr/_conditional_cached__either_token_acceptor_or_recognizer_and_inner_st_controller ++ StackItem._tmay_middle_st/_conditional_cached__either_token_expr_or_symbol_expr4as_if_success_and_acc_st4step/_conditional_cached__step_farthest_touched_end_position
    #   cache, to make life easy
    #   _acc__farthest_ex() ==>> _tmay_middle_st not _conditional_cached__middle_st
    # removed:_final_inner_st:
    #   useless but for validate
    #   using cache to run again, ...
    #   _on__final_inner_st
    #[refcount:using_refcount_for_validate_only_not_to_auto_delete]
)

def _():
    def get_stop_position(sf, lock_mask5above, /):
        if lock_mask2does_return(lock_mask5above):
            stop_position = sf.begin_position
        else:
            stop_position = sf.stop_position_before_return
        return stop_position
    MiddleState.get_stop_position = get_stop_position
    del get_stop_position
_()






#xuserdata
mk_CompactDataType_then_write_to_module(
    'XUserData4CuttableStream'
    ,__name__
    ,r'''
    stack_idc4stack_item_begin_here
    token_expr2relative_end_position2middle_st
    token_expr2eof_or_free_relative_farthest_touched_end_position
    symbol_expr2relative_end_position2middle_st
    symbol_expr2eof_or_free_relative_farthest_touched_end_position
    '''#'''
)



def _acc__farthest_ex(stack_item, /):
    _tmay_middle_st = stack_item._tmay_middle_st
    far1 = stack_item.farthest_touched_end_position5until_curr_inner_st
    ex1 = stack_item.does_try_read_token_at_end_position5until_curr_inner_st
    if not _tmay_middle_st:
        return (far1, ex1)
    [middle_st] = _tmay_middle_st
    far2 = middle_st.farthest_touched_end_position
    ex2 = middle_st.does_try_to_read_token_at_end_position
    check_type_is(bool, ex1)
    check_type_is(bool, ex2)

    if far1 is far2:
        ex3 = ex1 or ex2
        far3 = far1
        return (far3, ex3)
    elif position_lt(far1, far2):
        return (far2, ex2)
    elif position_lt(far2, far1):
        return (far1, ex1)
    raise logic-err
#end-def _acc__farthest_ex(stack_item, /):
def _tail__4_prev1s_inner_st2vars(stack_item, /):
    inner_st_controller = stack_item.common.inner_st_controller

    tm = stack_item._tmay_middle_st
    d = dict(
        begin_position
        =stack_item.begin_position
        ,may_end_position
        =stack_item.may_end_position
        )
    if tm:
        [middle_st] = tm
        tmay_lock_mask4step = nonfinal_inner_st2tmay_lock_mask(inner_st_controller, stack_item.inner_st)
        if not tmay_lock_mask4step:raise logic-err
            #has_no_step_success ==>> no middle_st
        [lock_mask4step] = tmay_lock_mask4step
        d.update(
        stop_position
        =middle_st.get_stop_position(lock_mask4step)
        ,farthest_touched_end_position
        =middle_st.farthest_touched_end_position
        ,stop_position_before_return
        =middle_st.stop_position_before_return
        )
    else:
        [] = tm
        d.update(
        stop_position
        =stack_item.begin_position
        ,farthest_touched_end_position
        =stack_item.begin_position
        ,stop_position_before_return
        =stack_item.begin_position
        )
    assert {*d} == {*Cases4Position}
    return d
#end-def _tail__4_prev1s_inner_st2vars(stack_item, /):

def check_position_rng(begin_position, may_end_position, /):
    if not position_le_ex(begin_position, may_end_position): raise logic-err

position_diff
position_le_ex
def init4acc__he_accGrammarAttribute
    check_either(he_accGrammarAttribute)
    return he_accGrammarAttribute
step_success_noninitial_inner_st2prev_either_token_expr_or_symbol_expr
    check_either(prev_either_token_expr_or_symbol_expr)

handle4step_fail__but__has_no_step_fail_next_inner_st :: nonfinal_inner_st -> tmay_heresult
