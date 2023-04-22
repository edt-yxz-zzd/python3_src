#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/recognizer_combinator_utils.py

seed.recognize.recognizer_combinator_utils
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_combinator_utils
py -m seed.recognize.recognizer_combinator_utils
py -m nn_ns.app.adhoc_argparser__main__call8module   seed.recognize.recognizer_combinator_utils

from seed.recognize.recognizer_combinator_utils import ...
    #recognizer_combinator_utils__imports:goto



[[rename:
move_nonfinal_inner_st
    -> moveon_nonfinal_inner_st

\<moveon_nonfinal_inner_st\>
    moveon_nonfinal_inner_st2next_inner_st__or_raise

.+1,$s/move_nonfinal_inner_st/moveon_nonfinal_inner_st/g
.+1,$s/\<moveon_nonfinal_inner_st\>/moveon_nonfinal_inner_st2next_inner_st__or_raise/g


]]
[[rename:
step_success_inner_st
    -> step_success_noninitial_inner_st
step_fail_inner_st
    -> step_fail_noninitial_inner_st

is_success_inner_st
    -> is_success_final_inner_st
is_fail_inner_st
    -> is_fail_final_inner_st

.+1,$s/step_success_inner_st/step_success_noninitial_inner_st/g
.+1,$s/step_fail_inner_st/step_fail_noninitial_inner_st/g

.+1,$s/success_inner_st/success_final_inner_st/g
.+1,$s/fail_inner_st/fail_final_inner_st/g

nonfinal_inner_st2...
    vs step_success_noninitial_inner_st2...
        #diff when moveon_nonfinal_inner_st2tmay_next_inner_st return ()


    nonfinal_inner_st2lock_mask
        -> _nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_
        --> step_success_noninitial_inner_st2prev_lock_mask

    nonfinal_inner_st2curr_using_begin_as_stop_position
        -> _nonfinal_inner_st2curr_using_begin_as_stop_position__when_step_success_exists_for_all_nonfinal_inner_st_
        update:noninitial_inner_st2prev_using_begin_as_stop_position

.+1,$s/nonfinal_inner_st2lock_mask/_nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_/g
.+1,$s/nonfinal_inner_st2curr_using_begin_as_stop_position/_nonfinal_inner_st2curr_using_begin_as_stop_position__when_step_success_exists_for_all_nonfinal_inner_st_/g

news:
    step_success_noninitial_inner_st2prev_lock_mask
    check_step_success_noninitial_inner_st
    nonfinal_inner_st2tmay_lock_mask


]]
[[
DONE:变更不变量:
    删去约束:[(st~?).begin_position == (?~st).stop_position]
        # 删去: 过气:noninitial_inner_st2using_prev_begin_as_begin_position
        # 见: noninitial_inner_st2prev_using_begin_as_stop_position

    删去约束:[(st~?).begin_position <= (st~?).may_end_position]
    ===新增出错情形:
        * is_fail_final_inner_st
            * unlocked_unlocked5above ==>> global_fail
            * locked_unlocked5above and is_post_pruning_inner_st ==>> global_fail
            * otherwise ==>> local_fail
        * (inner_st, begin_position, may_end_position):[not position_le_ex(begin_position, may_end_position)] ==>> step_fail
            [[is_bad_position_rng(begin_position, may_end_position)] =[def]= [not position_le_ex(begin_position, may_end_position)]]
            #is_bad_position_rng
        * [does_nonfinal_inner_st_have_no_step_success_noninitial_inner_st(nonfinal_inner_st)]
            #has_no_step_success
    ===
    约束:[finite iter_all_inner_sts(sf)]
    约束:[iter_all_inner_sts(sf) is a nonempty tree: root at initial_inner_st, leaf at is_final_inner_st, edg at moveon_nonfinal_inner_st2next_inner_st__or_raise, parent at noninitial_inner_st2prev_inner_st]
        #nonfinal_inner_st MUST HAVE at least one child, ie, moveon_nonfinal_inner_st2next_inner_st__or_raise over [False,True] for fix nonfinal_inner_st cannot_both_fail
        #

input:
    whole_symbol_expr.begin_position
    whole_symbol_expr.may_end_position)
    [whole_symbol_expr.begin_position <= whole_symbol_expr.may_end_position)]
vars:
    ##允许:(final_inner_st~?) 用于 检查 [(final_inner_st~?).begin_position <= (final_inner_st~?).may_end_position]
    (inner_st~?).begin_position
    (inner_st~?).may_end_position

    (inner_st~?).stop_position
        #:= if final or not .begin_position <= .may_end_position or step_fail or __return then .begin_position else .stop_position_before_return
        # _nonfinal_inner_st2curr_using_begin_as_stop_position__when_step_success_exists_for_all_nonfinal_inner_st_

    (inner_st~?).stop_position_before_return
        #:= if final or not .begin_position <= .may_end_position then .begin_position else sub-symbol_expr.stop_position
        #   no:『or step_fail』

    (inner_st~?).farthest_touched_end_position_ex
        #:= if final or not .begin_position <= .may_end_position then .begin_position else sub-symbol_expr.farthest_touched_end_position_ex
        #   _ex for match token at eof

vars:
    whole_symbol_expr.farthest_touched_end_position_ex
        #:= max((inner_st~?).farthest_touched_end_position_ex)

    if final_inner_st.begin_position <= final_inner_st.may_end_position:
        whole_symbol_expr.final_inner_st
            #:= final_inner_st
        whole_symbol_expr.stop_position
            #:= (final_inner_st~?).stop_position




[(initial_inner_st~?).begin_position := whole_symbol_expr.begin_position]
[(initial_inner_st~?).may_end_position := whole_symbol_expr.may_end_position]
    =====
    impl via:
    ::inner_st2begin_position
        * initial_inner_st -> whole_symbol_expr...
        * _ -> ::noninitial_inner_st2prev1s_inner_st_case4position_pair_as_begin_position

[(noninitial_final_inner_st~?).begin_position := (?~noninitial_final_inner_st).stop_position]
[(noninitial_final_inner_st~?).may_end_position := (?~noninitial_final_inner_st).may_end_position]
    =====
    impl via:
    ::noninitial_inner_st2prev1s_inner_st_case4position_pair_as_begin_position
        * final_inner_st -> ()
        * - -> .noninitial_nonfinal_inner_st2tmay_prev1s_inner_st_case4position_pair_as_begin_position

[(noninitial_nonfinal_inner_st~?).begin_position := ...using inner_st2begin_position/noninitial_inner_st2prev1s_inner_st_case4position_pair_as_begin_position/.noninitial_nonfinal_inner_st2tmay_prev1s_inner_st_case4position_pair_as_begin_position...]
[(noninitial_nonfinal_inner_st~?).may_end_position := ...using inner_st2may_end_position/noninitial_inner_st2prev1s_inner_st_case4position_pair_as_may_end_position/.noninitial_nonfinal_inner_st2tmay_prev1s_inner_st_case4position_pair_as_may_end_position...]
    =====
    impl via:
    .noninitial_nonfinal_inner_st2tmay_prev1s_inner_st_case4position_pair_as_begin_position <<== user_defined


##see:old:noninitial_nonfinal_inner_st2tmay_step_success_noninitial_inner_st4limit_end_position

##case4position = whole_symbol_expr_begin_position|whole_symbol_expr_may_end_position|begin_position|may_end_position|stop_position|stop_position_before_return|farthest_touched_end_position_ex
case4position = begin_position|may_end_position|stop_position|stop_position_before_return|farthest_touched_end_position
    Cases4Position.xxx

.noninitial_nonfinal_inner_st2tmay_prev1s_inner_st_case4position_pair_as_begin_position(sf, noninitial_nonfinal_inner_st)
    'noninitial_nonfinal_inner_st -> tmay (prev1s_inner_st, case4position)'

.noninitial_nonfinal_inner_st2tmay_prev1s_inner_st_case4position_pair_as_may_end_position(sf, noninitial_nonfinal_inner_st)
    'noninitial_nonfinal_inner_st -> tmay (prev1s_inner_st, case4position)'

def noninitial_inner_st2prev1s_inner_st_case4position_pair_as_begin_position(sf, noninitial_inner_st, /):
    'noninitial_inner_st -> (prev1s_inner_st, case4position)'

def noninitial_inner_st2prev1s_inner_st_case4position_pair_as_may_end_position(sf, noninitial_inner_st, /):
    'noninitial_inner_st -> (prev1s_inner_st, case4position)'

validate_prev1s_inner_st4position_assignment
def inner_st2begin_position(sf, get, vars4whole_symbol_expr, prev1s_inner_st2vars, inner_st, /):
    'get/((vars_, case4position) -> position<case>) -> vars_<whole_symbol_expr> -> {prev1s_inner_st:vars_} -> inner_st -> begin_position'
def inner_st2may_end_position(sf, get, vars4whole_symbol_expr, prev1s_inner_st2vars, inner_st, /):
    'get/((vars_, case4position) -> position<case>) -> vars_<whole_symbol_expr> -> {prev1s_inner_st:vars_} -> inner_st -> may_end_position'

]]
[[
DONE:见上面:『变更不变量』
    这里仅考虑 自由设置 may_end_position
        begin_position 只有 两种可能:prev.stop_position/begin_position
    而 上面 自由设置 begin_position/may_end_position
=====
部分过气:待更新:但已不必要
ISymbolExprInnerStateController 添加:noninitial_nonfinal_inner_st2tmay_step_success_noninitial_inner_st4limit_end_position
    ======
    vs: setting:begin_position<noninitial_inner_st>
    to: setting:may_end_position<noninitial_nonfinal_inner_st>
    ======
    vs: setting:begin_position<noninitial_inner_st>
    ===::
    if not noninitial_inner_st2using_prev_begin_as_begin_position(noninitial_inner_st):
        #step_success and not __return
        [(prev_inner_st~noninitial_inner_st).stop_position := (prev_inner_st~noninitial_inner_st).stop_position_before_return]
        using (prev_inner_st~noninitial_inner_st).stop_position/stop_position_before_return as (noninitial_inner_st~?).begin_position
        return
    #step_fail or __return
    [(prev_inner_st~noninitial_inner_st).stop_position := (prev_inner_st~noninitial_inner_st).begin_position]
    using (prev_inner_st~noninitial_inner_st).stop_position/begin_position as (noninitial_inner_st~?).begin_position
    return
    ======
    to: setting:may_end_position<noninitial_nonfinal_inner_st>
    ===::
    tmay_step_success_noninitial_inner_st := noninitial_nonfinal_inner_st2tmay_step_success_noninitial_inner_st4limit_end_position(noninitial_nonfinal_inner_st)
    if not tmay_step_success_noninitial_inner_st:
        initial_inner_st := get_initial_inner_st()
        using (initial_inner_st~?).may_end_position as (noninitial_nonfinal_inner_st~?).may_end_position
        return
    [step_success_noninitial_inner_st] := tmay_step_success_noninitial_inner_st
    assert is_step_success_noninitial_inner_st(step_success_noninitial_inner_st)
    backward_list_all_prev_inner_sts__include = [*iter_all_prev_inner_sts__include(noninitial_nonfinal_inner_st)]
    assert step_success_noninitial_inner_st in backward_list_all_prev_inner_sts__include
    i = backward_list_all_prev_inner_sts__include.index(step_success_noninitial_inner_st)
    assert all(map(noninitial_inner_st2using_prev_begin_as_begin_position, backward_list_all_prev_inner_sts__include[:i+1]))
    prev_inner_st := noninitial_inner_st2prev_inner_st(step_success_noninitial_inner_st)
    using (prev_inner_st~step_success_noninitial_inner_st).stop_position_before_return as (noninitial_nonfinal_inner_st~?).may_end_position for and1s/andnot1s
    return
    ======

lock_mask2does_return
_nonfinal_inner_st2curr_using_begin_as_stop_position__when_step_success_exists_for_all_nonfinal_inner_st_
过气:noninitial_inner_st2using_prev_begin_as_begin_position
    见:noninitial_inner_st2prev_using_begin_as_stop_position

]]

===
lock_mask:
    #__prefix_match,__without_user_result
    locked_halfway_return
    unlocked_unlocked__without_user_result
    locked_locked_return__without_user_result
    #__prefix_match,__with_user_result
    locked_locked_return__with_user_result
    locked_locked
    locked_unlocked
    unlocked_unlocked

    #__full_match,__with_user_result
    locked_locked_return__with_user_result__full_match
    locked_locked__full_match
    locked_unlocked__full_match
    unlocked_unlocked__full_match
    #__full_match,__without_user_result
    locked_locked_return__without_user_result__full_match
===
[[
is_final_inner_st :: inner_st -> bool
is_final_inner_st inner_st = is_fail_final_inner_st inner_st or is_success_final_inner_st inner_st
is_fail_final_inner_st :: inner_st -> bool
is_success_final_inner_st :: inner_st -> bool
xxx _nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ :: nonfinal_inner_st -> lock_mask
step_success_noninitial_inner_st2prev_lock_mask :: step_success_noninitial_inner_st -> lock_mask
get_initial_inner_st :: inner_st
moveon_nonfinal_inner_st2next_inner_st__or_raise :: is_on_success/bool -> nonfinal_inner_st -> inner_st
#xxx success_final_inner_st2prev_inner_st :: success_final_inner_st -> inner_st
#   since nonfinal_inner_st may be initial_inner_st
noninitial_inner_st2prev_inner_st :: noninitial_inner_st -> inner_st
#noninitial_inner_st2is_on_success :: noninitial_inner_st -> bool
noninitial_nonfinal_inner_st2tmay_prev1s_inner_st_case4position_pair_as_begin_position :: noninitial_nonfinal_inner_st -> tmay (prev1s_inner_st, case4position)
noninitial_nonfinal_inner_st2tmay_prev1s_inner_st_case4position_pair_as_may_end_position :: noninitial_nonfinal_inner_st -> tmay (prev1s_inner_st, case4position)



inner_st:
    * skip:
        #base on look_ahead
        inner_st = idx :: [-1..=1]
        is_post_pruning_inner_st inner_st = is_success_final_inner_st inner_st
        get_initial_inner_st = 0
        moveon_nonfinal_inner_st2next_inner_st__or_raise is_on_success 0 = if is_on_success then +1 else -1
        is_fail_final_inner_st inner_st = inner_st == -1
        is_success_final_inner_st inner_st = inner_st == +1
        _nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ inner_st = unlocked_unlocked__without_user_result
        noninitial_inner_st2prev_inner_st noninitial_inner_st = 0


    * andnot1s:
        andnot1s__full_match
        andnot1s__prefix_match
        [L >= 1]
        ===
        ???validate_post_pruning_inner_sts???required is_on_success==True before inner_st@[is_post_pruning_inner_st inner_st==True]
        as-if:last=sf.args[0]
        ===
        [L >= 1]
        inner_st = idx4curr_branch :: [-1-L..=L+1]
        is_post_pruning_inner_st inner_st = is_success_final_inner_st inner_st
        get_initial_inner_st = 0
        moveon_nonfinal_inner_st2next_inner_st__or_raise is_on_success idx4curr_branch = if is_on_success^(idx4curr_branch in (0,L)) then -1-idx4curr_branch else +1+idx4curr_branch
        moveon_nonfinal_inner_st2next_inner_st__or_raise is_on_success 0 = if is_on_success then +1 else -1
        moveon_nonfinal_inner_st2next_inner_st__or_raise is_on_success L = if is_on_success then +1+L else -1-L
        moveon_nonfinal_inner_st2next_inner_st__or_raise is_on_success idx4curr_branch = if is_on_success then -1-idx4curr_branch else +1+idx4curr_branch
        is_fail_final_inner_st inner_st = inner_st < 0
        is_success_final_inner_st inner_st = inner_st == 1+L
        andnot1s__prefix_match._nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ inner_st = if inner_st==L then unlocked_unlocked__full_match else locked_locked_return__without_user_result
        andnot1s__full_match._nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ inner_st = if inner_st==L then unlocked_unlocked__full_match elif inner_st==0 then locked_locked_return__without_user_result else locked_locked_return__without_user_result__full_match
        noninitial_inner_st2prev_inner_st noninitial_inner_st = if noninitial_inner_st < 0 then -1-noninitial_inner_st else noninitial_inner_st-1
        noninitial_nonfinal_inner_st2tmay_prev1s_inner_st_case4position_pair_as_begin_position _ = ()
        noninitial_nonfinal_inner_st2tmay_prev1s_inner_st_case4position_pair_as_may_end_position noninitial_nonfinal_inner_st = if noninitial_nonfinal_inner_st == 1 then ((0, Cases4Position.stop_position_before_return),) else ()




    * look_ahead_not:
        look_ahead_not__head
        look_ahead_not__head_body
        look_ahead__head__not__body
            == catenation(look_ahead__head, look_ahead_not__head_body)
            #not: == and1s__full_match(look_ahead__head, look_ahead_not__head_body)
        ===
        ???validate_post_pruning_inner_sts???required is_on_success==True before inner_st@[is_post_pruning_inner_st inner_st==True]
        as-if:last=catenation()
        ===
        inner_st = idx :: [-1..=2]
        is_post_pruning_inner_st inner_st = is_success_final_inner_st inner_st
        get_initial_inner_st = 0
        moveon_nonfinal_inner_st2next_inner_st__or_raise is_on_success 0 = if is_on_success then +1 else -1
        moveon_nonfinal_inner_st2next_inner_st__or_raise is_on_success 1 = if is_on_success then +2 else error
        is_fail_final_inner_st inner_st = inner_st == -1
        is_success_final_inner_st inner_st = inner_st == +2
        look_ahead_not__head._nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ inner_st = locked_halfway_return
        look_ahead_not__head_body._nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ inner_st = locked_locked_return__without_user_result
        noninitial_inner_st2prev_inner_st noninitial_inner_st = if noninitial_inner_st == 2 then 1 else 0


    * look_ahead:
        look_ahead__head
        look_ahead__body
        inner_st = idx :: [-1..=1]
        is_post_pruning_inner_st inner_st = is_success_final_inner_st inner_st
        get_initial_inner_st = 0
        moveon_nonfinal_inner_st2next_inner_st__or_raise is_on_success 0 = if is_on_success then +1 else -1
        is_fail_final_inner_st inner_st = inner_st == -1
        is_success_final_inner_st inner_st = inner_st == +1
        look_ahead__head._nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ inner_st = locked_halfway_return
        look_ahead__body._nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ inner_st = locked_locked_return__without_user_result
        noninitial_inner_st2prev_inner_st noninitial_inner_st = 0


    * and1s:
        and1s__full_match
        and1s__prefix_match
        [L >= 1]
        inner_st = idx4curr_branch :: [-L..=L]
        is_post_pruning_inner_st inner_st = is_success_final_inner_st inner_st
        get_initial_inner_st = 0
        moveon_nonfinal_inner_st2next_inner_st__or_raise is_on_success idx4curr_branch = if is_on_success then +1+idx4curr_branch else -1-idx4curr_branch
        is_fail_final_inner_st inner_st = inner_st < 0
        is_success_final_inner_st inner_st = inner_st == +L
        and1s__full_match._nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ inner_st = if inner_st==L-1 then unlocked_unlocked__full_match elif inner_st==0 then locked_locked_return__with_user_result else locked_locked_return__with_user_result__full_match
        and1s__prefix_match._nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ inner_st = if inner_st==L-1 then unlocked_unlocked else locked_locked_return__with_user_result
        noninitial_inner_st2prev_inner_st noninitial_inner_st = if noninitial_inner_st < 0 then -1-noninitial_inner_st else noninitial_inner_st-1
        noninitial_nonfinal_inner_st2tmay_prev1s_inner_st_case4position_pair_as_begin_position _ = ()
        noninitial_nonfinal_inner_st2tmay_prev1s_inner_st_case4position_pair_as_may_end_position noninitial_nonfinal_inner_st = if noninitial_nonfinal_inner_st == 1 then ((0, Cases4Position.stop_position_before_return),) else ()


    * token:
        inner_st = idx :: [-1..=1]
        is_post_pruning_inner_st inner_st = is_success_final_inner_st inner_st
        get_initial_inner_st = 0
        moveon_nonfinal_inner_st2next_inner_st__or_raise is_on_success 0 = if is_on_success then +1 else -1
        is_fail_final_inner_st inner_st = inner_st == -1
        is_success_final_inner_st inner_st = inner_st == +1
        _nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ inner_st = unlocked_unlocked
        noninitial_inner_st2prev_inner_st noninitial_inner_st = 0


    * catenation:
        L = len(series)
        .idx4pruning_head :: [-1..<L] # <<== [L==0]
        inner_st = idx :: [-L..=L]
        #is_post_pruning_inner_st inner_st = inner_st==1+idx4pruning_head
        is_post_pruning_inner_st inner_st = (-1-inner_st if inner_st < 0 else inner_st) > idx4pruning_head
        get_initial_inner_st = 0
        moveon_nonfinal_inner_st2next_inner_st__or_raise is_on_success nonfinal_inner_st = if is_on_success then nonfinal_inner_st+1 else -1-nonfinal_inner_st
        is_fail_final_inner_st inner_st = inner_st < 0
        is_success_final_inner_st inner_st = inner_st==L
        _nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ inner_st = unlocked_unlocked
        #   see:is_post_pruning_inner_st
        #_nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ inner_st = if inner_st < idx4pruning_head then locked_locked elif inner_st==idx4pruning_head then locked_unlocked else unlocked_unlocked
        noninitial_inner_st2prev_inner_st noninitial_inner_st = if noninitial_inner_st < 0 then -1-noninitial_inner_st else noninitial_inner_st-1

    * mutex:
        L = len(branches)
        inner_st = (idx4prev_success, idx4curr_branch) :: ([0..=L], [-L..=L])
        is_post_pruning_inner_st inner_st = is_success_final_inner_st inner_st
        get_initial_inner_st = (L, 0)
        moveon_nonfinal_inner_st2next_inner_st__or_raise is_on_success (idx4prev_success, idx4curr_branch) = if not is_on_success then (idx4prev_success, idx4curr_branch+1) elif idx4prev_success==L then (idx4curr_branch, idx4curr_branch+1) elif not idx4curr_branch==L then (idx4prev_success, -idx4curr_branch) else (idx4prev_success, -L)
        ===
        moveon_nonfinal_inner_st2next_inner_st__or_raise False (idx4prev_success, L) = error
        moveon_nonfinal_inner_st2next_inner_st__or_raise False (L, idx4curr_branch) = (L, idx4curr_branch+1)
        moveon_nonfinal_inner_st2next_inner_st__or_raise False (idx4prev_success, idx4curr_branch) = (idx4prev_success, idx4curr_branch+1)

        moveon_nonfinal_inner_st2next_inner_st__or_raise True (idx4prev_success, L) = (idx4prev_success, -L)
        moveon_nonfinal_inner_st2next_inner_st__or_raise True (idx4prev_success, idx4curr_branch) = (idx4prev_success, -idx4curr_branch)

        is_fail_final_inner_st inner_st = inner_st==(L, L) or -L < snd inner_st < 0
        is_success_final_inner_st (idx4prev_success, idx4curr_branch) = idx4prev_success < L and idx4curr_branch==-L
        _nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ (_, idx4curr_branch) = if idx4curr_branch==L then unlocked_unlocked else locked_halfway_return
        noninitial_inner_st2prev_inner_st (L, idx4curr_branch) = (L, idx4curr_branch-1)
        noninitial_inner_st2prev_inner_st (idx4prev_success, idx4curr_branch) = if idx4curr_branch < 0 then (idx4prev_success, -idx4curr_branch) elif idx4curr_branch == idx4prev_success+1 then (L, idx4prev_success) else (idx4prev_success, idx4curr_branch-1)

    * switch:
        L = len(branches)
        inner_st = idx4curr_branch :: [-L..=L]
        is_post_pruning_inner_st inner_st = is_success_final_inner_st inner_st
        get_initial_inner_st = 0
        moveon_nonfinal_inner_st2next_inner_st__or_raise is_on_success idx4curr_branch = if is_on_success then -1-idx4curr_branch else idx4curr_branch+1
        is_fail_final_inner_st inner_st = inner_st==L
        is_success_final_inner_st inner_st = inner_st < 0
        _nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ idx4curr_branch = if idx4curr_branch==L-1 then unlocked_unlocked else locked_unlocked
        noninitial_inner_st2prev_inner_st noninitial_inner_st = if noninitial_inner_st < 0 then -1-noninitial_inner_st else noninitial_inner_st-1

]]

[[

#recognizer_combinator_utils__imports:goto
>>> from seed.recognize.recognizer_combinator_utils import LockMaskBit
>>> from seed.recognize.recognizer_combinator_utils import LockMask
>>> from seed.recognize.recognizer_combinator_utils import Error__moveon_nonfinal_inner_st
>>> from seed.recognize.recognizer_combinator_utils import ISymbolExprInnerStateController


>>> from seed.recognize.recognizer_combinator_utils import (ISymbolExprInnerStateController, is_post_pruning_inner_st, is_inner_st, is_fail_final_inner_st, is_success_final_inner_st, step_success_noninitial_inner_st2prev_lock_mask, nonfinal_inner_st2tmay_lock_mask, _nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_, get_initial_inner_st, moveon_nonfinal_inner_st2next_inner_st__or_raise, Error__moveon_nonfinal_inner_st, moveon_nonfinal_inner_st2tmay_next_inner_st, noninitial_inner_st2prev_inner_st, noninitial_inner_st2is_on_success, is_initial_inner_st, is_final_inner_st, check_inner_st, check_initial_inner_st, check_final_inner_st, check_noninitial_inner_st, check_nonfinal_inner_st, check_step_success_noninitial_inner_st, iter_all_inner_sts, iter_all_final_inner_sts, iter_all_nonfinal_inner_sts, iter_all_post_pruning_inner_sts, iter_all_prev_inner_sts__include, validate_post_pruning_inner_sts)
>>> from seed.recognize.recognizer_combinator_utils import (ISymbolExprInnerStateController, is_fail_final_inner_st, is_success_final_inner_st, is_fail_final_inner_st, is_success_final_inner_st, noninitial_inner_st2is_on_success, is_step_fail_noninitial_inner_st, is_step_success_noninitial_inner_st)


>>> from seed.recognize.recognizer_combinator_utils import (ISymbolExprInnerStateController, lock_mask2does_return, _nonfinal_inner_st2curr_using_begin_as_stop_position__when_step_success_exists_for_all_nonfinal_inner_st_, noninitial_inner_st2prev_using_begin_as_stop_position, Cases4Position, check_case4position, noninitial_inner_st2prev1s_inner_st_case4position_pair_as_begin_position, noninitial_inner_st2prev1s_inner_st_case4position_pair_as_may_end_position, inner_st2begin_position, inner_st2may_end_position, mk_height2inner_st_layer, mk_inner_st2height, mk_height2inner_st_layer_ex, VisitInnerStateTree__dfs, validate_prev1s_inner_st4position_assignment)





>>> from seed.recognize.recognizer_combinator_utils import (ISymbolExprInnerStateController, SymbolExprInnerStateController__mutex, SymbolExprInnerStateController__switch, SymbolExprInnerStateController__catenation, SymbolExprInnerStateController__token, SymbolExprInnerStateController__and1s__full_match, SymbolExprInnerStateController__and1s__prefix_match, SymbolExprInnerStateController__andnot1s__full_match, SymbolExprInnerStateController__andnot1s__prefix_match, SymbolExprInnerStateController__look_ahead__head, SymbolExprInnerStateController__look_ahead__body, SymbolExprInnerStateController__skip, SymbolExprInnerStateController__look_ahead_not__head, SymbolExprInnerStateController__look_ahead_not__head_body)





>>> from seed.recognize.recognizer_combinator_utils import LockMaskBit, bit4locked_head, bit4locked_body, bit4head_return, bit4body_return, bit4with_user_result, bit4full_match

>>> from seed.recognize.recognizer_combinator_utils import LockMask, locked_halfway_return, unlocked_unlocked__without_user_result, locked_locked_return__without_user_result, locked_locked_return__with_user_result, locked_locked, locked_unlocked, unlocked_unlocked, locked_locked_return__with_user_result__full_match, locked_locked__full_match, locked_unlocked__full_match, unlocked_unlocked__full_match, locked_locked_return__without_user_result__full_match






>>> mutex0 = SymbolExprInnerStateController__mutex(0)
>>> mutex1 = SymbolExprInnerStateController__mutex(1)
>>> mutex2 = SymbolExprInnerStateController__mutex(2)
>>> [*iter_all_inner_sts(mutex0)]
[(0, 0)]
>>> [*iter_all_inner_sts(mutex1)]
[(1, 0), (1, 1), (0, 1), (0, -1)]
>>> [*iter_all_inner_sts(mutex2)]
[(2, 0), (2, 1), (0, 1), (0, 2), (0, -1), (0, -2), (2, 2), (1, 2), (1, -2)]
>>> moveon_nonfinal_inner_st2next_inner_st__or_raise(mutex2, True, (0, 1))
(0, -1)
>>> [*iter_all_final_inner_sts(mutex0)]
[(0, 0)]
>>> [*iter_all_final_inner_sts(mutex1)]
[(1, 1), (0, -1)]
>>> [*iter_all_final_inner_sts(mutex2)]
[(0, -1), (0, -2), (2, 2), (1, -2)]
>>> [*iter_all_nonfinal_inner_sts(mutex0)]
[]
>>> [*iter_all_nonfinal_inner_sts(mutex1)]
[(1, 0), (0, 1)]
>>> [*iter_all_nonfinal_inner_sts(mutex2)]
[(2, 0), (2, 1), (0, 1), (0, 2), (1, 2)]


>>> switch0 = SymbolExprInnerStateController__switch(0)
>>> switch1 = SymbolExprInnerStateController__switch(1)
>>> switch2 = SymbolExprInnerStateController__switch(2)
>>> [*iter_all_inner_sts(switch0)]
[0]
>>> [*iter_all_inner_sts(switch1)]
[0, 1, -1]
>>> [*iter_all_inner_sts(switch2)]
[0, 1, -1, 2, -2]
>>> [*iter_all_final_inner_sts(switch0)]
[0]
>>> [*iter_all_final_inner_sts(switch1)]
[1, -1]
>>> [*iter_all_final_inner_sts(switch2)]
[-1, 2, -2]
>>> [*iter_all_nonfinal_inner_sts(switch0)]
[]
>>> [*iter_all_nonfinal_inner_sts(switch1)]
[0]
>>> [*iter_all_nonfinal_inner_sts(switch2)]
[0, 1]


>>> catenation0_x = SymbolExprInnerStateController__catenation(0, -1)
>>> catenation1_x = SymbolExprInnerStateController__catenation(1, -1)
>>> catenation1_0 = SymbolExprInnerStateController__catenation(1, 0)
>>> catenation2_x = SymbolExprInnerStateController__catenation(2, -1)
>>> catenation2_0 = SymbolExprInnerStateController__catenation(2, 0)
>>> catenation2_1 = SymbolExprInnerStateController__catenation(2, 1)
>>> [*iter_all_inner_sts(catenation0_x)]
[0]
>>> [*iter_all_inner_sts(catenation1_x)]
[0, -1, 1]
>>> [*iter_all_inner_sts(catenation2_x)]
[0, -1, 1, -2, 2]
>>> [*iter_all_final_inner_sts(catenation0_x)]
[0]
>>> [*iter_all_final_inner_sts(catenation1_x)]
[-1, 1]
>>> [*iter_all_final_inner_sts(catenation2_x)]
[-1, -2, 2]
>>> [*iter_all_nonfinal_inner_sts(catenation0_x)]
[]
>>> [*iter_all_nonfinal_inner_sts(catenation1_x)]
[0]
>>> [*iter_all_nonfinal_inner_sts(catenation2_x)]
[0, 1]


>>> token_ = SymbolExprInnerStateController__token()
>>> [*iter_all_inner_sts(token_)]
[0, -1, 1]
>>> [*iter_all_final_inner_sts(token_)]
[-1, 1]
>>> [*iter_all_nonfinal_inner_sts(token_)]
[0]


look_ahead__head
look_ahead__body
skip
look_ahead_not__head
look_ahead_not__head_body
>>> look_ahead__head_ = SymbolExprInnerStateController__look_ahead__head()
>>> [*iter_all_inner_sts(look_ahead__head_)]
[0, -1, 1]
>>> [*iter_all_final_inner_sts(look_ahead__head_)]
[-1, 1]
>>> [*iter_all_nonfinal_inner_sts(look_ahead__head_)]
[0]

>>> look_ahead__body_ = SymbolExprInnerStateController__look_ahead__body()
>>> [*iter_all_inner_sts(look_ahead__body_)]
[0, -1, 1]
>>> [*iter_all_final_inner_sts(look_ahead__body_)]
[-1, 1]
>>> [*iter_all_nonfinal_inner_sts(look_ahead__body_)]
[0]


>>> skip_ = SymbolExprInnerStateController__skip()
>>> [*iter_all_inner_sts(skip_)]
[0, -1, 1]
>>> [*iter_all_final_inner_sts(skip_)]
[-1, 1]
>>> [*iter_all_nonfinal_inner_sts(skip_)]
[0]

>>> look_ahead_not__head_ = SymbolExprInnerStateController__look_ahead_not__head()
>>> [*iter_all_inner_sts(look_ahead_not__head_)]
[0, -1, 1, 2]
>>> [*iter_all_final_inner_sts(look_ahead_not__head_)]
[-1, 2]
>>> [*iter_all_nonfinal_inner_sts(look_ahead_not__head_)]
[0, 1]

>>> look_ahead_not__head_body_ = SymbolExprInnerStateController__look_ahead_not__head_body()
>>> [*iter_all_inner_sts(look_ahead_not__head_body_)]
[0, -1, 1, 2]
>>> [*iter_all_final_inner_sts(look_ahead_not__head_body_)]
[-1, 2]
>>> [*iter_all_nonfinal_inner_sts(look_ahead_not__head_body_)]
[0, 1]




and1s__full_match
and1s__prefix_match
andnot1s__full_match
andnot1s__prefix_match
>>> and1s__full_match1 = SymbolExprInnerStateController__and1s__full_match(1)
>>> and1s__full_match2 = SymbolExprInnerStateController__and1s__full_match(2)
>>> and1s__full_match3 = SymbolExprInnerStateController__and1s__full_match(3)
>>> [*iter_all_inner_sts(and1s__full_match1)]
[0, -1, 1]
>>> [*iter_all_inner_sts(and1s__full_match2)]
[0, -1, 1, -2, 2]
>>> [*iter_all_inner_sts(and1s__full_match3)]
[0, -1, 1, -2, 2, -3, 3]
>>> [*iter_all_final_inner_sts(and1s__full_match1)]
[-1, 1]
>>> [*iter_all_final_inner_sts(and1s__full_match2)]
[-1, -2, 2]
>>> [*iter_all_final_inner_sts(and1s__full_match3)]
[-1, -2, -3, 3]
>>> [*iter_all_nonfinal_inner_sts(and1s__full_match1)]
[0]
>>> [*iter_all_nonfinal_inner_sts(and1s__full_match2)]
[0, 1]
>>> [*iter_all_nonfinal_inner_sts(and1s__full_match3)]
[0, 1, 2]

>>> and1s__prefix_match1 = SymbolExprInnerStateController__and1s__prefix_match(1)
>>> and1s__prefix_match2 = SymbolExprInnerStateController__and1s__prefix_match(2)
>>> and1s__prefix_match3 = SymbolExprInnerStateController__and1s__prefix_match(3)
>>> [*iter_all_inner_sts(and1s__prefix_match1)]
[0, -1, 1]
>>> [*iter_all_inner_sts(and1s__prefix_match2)]
[0, -1, 1, -2, 2]
>>> [*iter_all_inner_sts(and1s__prefix_match3)]
[0, -1, 1, -2, 2, -3, 3]
>>> [*iter_all_final_inner_sts(and1s__prefix_match1)]
[-1, 1]
>>> [*iter_all_final_inner_sts(and1s__prefix_match2)]
[-1, -2, 2]
>>> [*iter_all_final_inner_sts(and1s__prefix_match3)]
[-1, -2, -3, 3]
>>> [*iter_all_nonfinal_inner_sts(and1s__prefix_match1)]
[0]
>>> [*iter_all_nonfinal_inner_sts(and1s__prefix_match2)]
[0, 1]
>>> [*iter_all_nonfinal_inner_sts(and1s__prefix_match3)]
[0, 1, 2]

>>> andnot1s__full_match1 = SymbolExprInnerStateController__andnot1s__full_match(1)
>>> andnot1s__full_match2 = SymbolExprInnerStateController__andnot1s__full_match(2)
>>> andnot1s__full_match3 = SymbolExprInnerStateController__andnot1s__full_match(3)
>>> [*iter_all_inner_sts(andnot1s__full_match1)]
[0, -1, 1, -2, 2]
>>> [*iter_all_inner_sts(andnot1s__full_match2)]
[0, -1, 1, 2, -2, -3, 3]
>>> [*iter_all_inner_sts(andnot1s__full_match3)]
[0, -1, 1, 2, -2, 3, -3, -4, 4]
>>> [*iter_all_final_inner_sts(andnot1s__full_match1)]
[-1, -2, 2]
>>> [*iter_all_final_inner_sts(andnot1s__full_match2)]
[-1, -2, -3, 3]
>>> [*iter_all_final_inner_sts(andnot1s__full_match3)]
[-1, -2, -3, -4, 4]
>>> [*iter_all_nonfinal_inner_sts(andnot1s__full_match1)]
[0, 1]
>>> [*iter_all_nonfinal_inner_sts(andnot1s__full_match2)]
[0, 1, 2]
>>> [*iter_all_nonfinal_inner_sts(andnot1s__full_match3)]
[0, 1, 2, 3]

>>> andnot1s__prefix_match1 = SymbolExprInnerStateController__andnot1s__prefix_match(1)
>>> andnot1s__prefix_match2 = SymbolExprInnerStateController__andnot1s__prefix_match(2)
>>> andnot1s__prefix_match3 = SymbolExprInnerStateController__andnot1s__prefix_match(3)
>>> [*iter_all_inner_sts(andnot1s__prefix_match1)]
[0, -1, 1, -2, 2]
>>> [*iter_all_inner_sts(andnot1s__prefix_match2)]
[0, -1, 1, 2, -2, -3, 3]
>>> [*iter_all_inner_sts(andnot1s__prefix_match3)]
[0, -1, 1, 2, -2, 3, -3, -4, 4]
>>> [*iter_all_final_inner_sts(andnot1s__prefix_match1)]
[-1, -2, 2]
>>> [*iter_all_final_inner_sts(andnot1s__prefix_match2)]
[-1, -2, -3, 3]
>>> [*iter_all_final_inner_sts(andnot1s__prefix_match3)]
[-1, -2, -3, -4, 4]
>>> [*iter_all_nonfinal_inner_sts(andnot1s__prefix_match1)]
[0, 1]
>>> [*iter_all_nonfinal_inner_sts(andnot1s__prefix_match2)]
[0, 1, 2]
>>> [*iter_all_nonfinal_inner_sts(andnot1s__prefix_match3)]
[0, 1, 2, 3]






???step_success_noninitial_inner_st2prev_lock_mask
???nonfinal_inner_st2tmay_lock_mask
_nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_
>>> f = lambda sf:[(nonfinal_inner_st, _nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_(sf, nonfinal_inner_st)) for nonfinal_inner_st in iter_all_nonfinal_inner_sts(sf)]
>>> f(mutex0)
[]
>>> f(mutex1) == [((1, 0), LockMask.locked_halfway_return), ((0, 1), LockMask.unlocked_unlocked)]
True
>>> f(mutex2) == [((2, 0), LockMask.locked_halfway_return), ((2, 1), LockMask.locked_halfway_return), ((0, 1), LockMask.locked_halfway_return), ((0, 2), LockMask.unlocked_unlocked), ((1, 2), LockMask.unlocked_unlocked)]
True
>>> f(switch0)
[]
>>> f(switch1) == [(0, LockMask.unlocked_unlocked)]
True
>>> f(switch2) == [(0, LockMask.locked_unlocked), (1, LockMask.unlocked_unlocked)]
True
>>> f(catenation0_x)
[]
>>> f(catenation1_x) == [(0, LockMask.unlocked_unlocked)]
True
>>> f(catenation1_0) == [(0, LockMask.unlocked_unlocked)]
True
>>> f(catenation2_x) == [(0, LockMask.unlocked_unlocked), (1, LockMask.unlocked_unlocked)]
True
>>> f(catenation2_0) == [(0, LockMask.unlocked_unlocked), (1, LockMask.unlocked_unlocked)]
True
>>> f(catenation2_1) == [(0, LockMask.unlocked_unlocked), (1, LockMask.unlocked_unlocked)]
True
>>> f(token_) == [(0, LockMask.unlocked_unlocked)]
True


>>> f(look_ahead__head_) == [(0, LockMask.locked_halfway_return)]
True
>>> f(look_ahead__body_) == [(0, LockMask.locked_locked_return__without_user_result)]
True
>>> f(skip_) == [(0, LockMask.unlocked_unlocked__without_user_result)]
True
>>> f(look_ahead_not__head_) == [(0, LockMask.locked_halfway_return), (1, LockMask.locked_halfway_return)]
True
>>> f(look_ahead_not__head_body_) == [(0, LockMask.locked_locked_return__without_user_result), (1, LockMask.locked_locked_return__without_user_result)]
True


>>> f(and1s__full_match1) == [(0, LockMask.unlocked_unlocked__full_match)]
True
>>> f(and1s__full_match2) == [(0, LockMask.locked_locked_return__with_user_result), (1, LockMask.unlocked_unlocked__full_match)]
True
>>> f(and1s__full_match3) == [(0, LockMask.locked_locked_return__with_user_result), (1, LockMask.locked_locked_return__with_user_result__full_match), (2, LockMask.unlocked_unlocked__full_match)]
True
>>> f(and1s__prefix_match1) == [(0, LockMask.unlocked_unlocked)]
True
>>> f(and1s__prefix_match2) == [(0, LockMask.locked_locked_return__with_user_result), (1, LockMask.unlocked_unlocked)]
True
>>> f(and1s__prefix_match3) == [(0, LockMask.locked_locked_return__with_user_result), (1, LockMask.locked_locked_return__with_user_result), (2, LockMask.unlocked_unlocked)]
True
>>> f(andnot1s__full_match1) == [(0, LockMask.locked_locked_return__without_user_result), (1, LockMask.unlocked_unlocked__full_match)]
True
>>> f(andnot1s__full_match2) == [(0, LockMask.locked_locked_return__without_user_result), (1, LockMask.locked_locked_return__without_user_result__full_match), (2, LockMask.unlocked_unlocked__full_match)]
True
>>> f(andnot1s__full_match3) == [(0, LockMask.locked_locked_return__without_user_result), (1, LockMask.locked_locked_return__without_user_result__full_match), (2, LockMask.locked_locked_return__without_user_result__full_match), (3, LockMask.unlocked_unlocked__full_match)]
True
>>> f(andnot1s__prefix_match1) == [(0, LockMask.locked_locked_return__without_user_result), (1, LockMask.unlocked_unlocked__full_match)]
True
>>> f(andnot1s__prefix_match2) == [(0, LockMask.locked_locked_return__without_user_result), (1, LockMask.locked_locked_return__without_user_result), (2, LockMask.unlocked_unlocked__full_match)]
True
>>> f(andnot1s__prefix_match3) == [(0, LockMask.locked_locked_return__without_user_result), (1, LockMask.locked_locked_return__without_user_result), (2, LockMask.locked_locked_return__without_user_result), (3, LockMask.unlocked_unlocked__full_match)]
True






>>> f = validate_post_pruning_inner_sts
>>> f = validate_prev1s_inner_st4position_assignment

>>> all_controllers = []
>>> f = all_controllers.append
>>> f(mutex0)
>>> f(mutex1)
>>> f(mutex2)
>>> f(switch0)
>>> f(switch1)
>>> f(switch2)
>>> f(catenation0_x)
>>> f(catenation1_x)
>>> f(catenation1_0)
>>> f(catenation2_x)
>>> f(catenation2_0)
>>> f(catenation2_1)
>>> f(token_)


>>> f(look_ahead__head_)
>>> f(look_ahead__body_)
>>> f(skip_)
>>> f(look_ahead_not__head_)
>>> f(look_ahead_not__head_body_)


>>> f(and1s__full_match1)
>>> f(and1s__full_match2)
>>> f(and1s__full_match3)
>>> f(and1s__prefix_match1)
>>> f(and1s__prefix_match2)
>>> f(and1s__prefix_match3)
>>> f(andnot1s__full_match1)
>>> f(andnot1s__full_match2)
>>> f(andnot1s__full_match3)
>>> f(andnot1s__prefix_match1)
>>> f(andnot1s__prefix_match2)
>>> f(andnot1s__prefix_match3)


>>> map_f = lambda f: [_ for _ in map(f, all_controllers)] and None

validate_post_pruning_inner_sts
>>> map_f(validate_post_pruning_inner_sts)



DONE:incomplete:validate_prev1s_inner_st4position_assignment
>>> map_f(validate_prev1s_inner_st4position_assignment)


iter_all_post_pruning_inner_sts
>>> f=lambda sf:[*iter_all_post_pruning_inner_sts(sf)]
>>> f(mutex0)
[]
>>> f(mutex1)
[(0, -1)]
>>> f(mutex2)
[(0, -2), (1, -2)]
>>> f(switch0)
[]
>>> f(switch1)
[-1]
>>> f(switch2)
[-1, -2]
>>> f(catenation0_x)
[0]
>>> f(catenation1_x)
[0, -1, 1]
>>> f(catenation1_0)
[1]
>>> f(catenation2_x)
[0, -1, 1, -2, 2]
>>> f(catenation2_0)
[1, -2, 2]
>>> f(catenation2_1)
[2]
>>> f(token_)
[1]


>>> f(look_ahead__head_)
[1]
>>> f(look_ahead__body_)
[1]
>>> f(skip_)
[1]
>>> f(look_ahead_not__head_)
[2]
>>> f(look_ahead_not__head_body_)
[2]


>>> f(and1s__full_match1)
[1]
>>> f(and1s__full_match2)
[2]
>>> f(and1s__full_match3)
[3]
>>> f(and1s__prefix_match1)
[1]
>>> f(and1s__prefix_match2)
[2]
>>> f(and1s__prefix_match3)
[3]
>>> f(andnot1s__full_match1)
[2]
>>> f(andnot1s__full_match2)
[3]
>>> f(andnot1s__full_match3)
[4]
>>> f(andnot1s__prefix_match1)
[2]
>>> f(andnot1s__prefix_match2)
[3]
>>> f(andnot1s__prefix_match3)
[4]




noninitial_inner_st2is_on_success
is_step_fail_noninitial_inner_st
is_step_success_noninitial_inner_st
>>> f=lambda g, sf:[(st, g(sf, st)) for st in islice(iter_all_inner_sts(sf),1,None)]
>>> f(noninitial_inner_st2is_on_success, andnot1s__prefix_match3)
[(-1, False), (1, True), (2, False), (-2, True), (3, False), (-3, True), (-4, False), (4, True)]
>>> f(is_step_success_noninitial_inner_st, andnot1s__prefix_match3)
[(-1, False), (1, True), (2, False), (-2, True), (3, False), (-3, True), (-4, False), (4, True)]
>>> f(is_step_fail_noninitial_inner_st, andnot1s__prefix_match3)
[(-1, True), (1, False), (2, True), (-2, False), (3, True), (-3, False), (-4, True), (4, False)]



news:
    _nonfinal_inner_st2curr_using_begin_as_stop_position__when_step_success_exists_for_all_nonfinal_inner_st_
    noninitial_inner_st2prev_using_begin_as_stop_position
    noninitial_inner_st2prev1s_inner_st_case4position_pair_as_begin_position
    noninitial_inner_st2prev1s_inner_st_case4position_pair_as_may_end_position
    inner_st2begin_position
    inner_st2may_end_position
    mk_inner_st2height
    mk_height2inner_st_layer
    mk_height2inner_st_layer_ex
    VisitInnerStateTree__dfs
    validate_prev1s_inner_st4position_assignment

    lock_mask2does_return
    Cases4Position
    check_case4position
news:
    step_success_noninitial_inner_st2prev_lock_mask
    check_step_success_noninitial_inner_st
    nonfinal_inner_st2tmay_lock_mask


VisitInnerStateTree__dfs
>>> [*iter_all_inner_sts(andnot1s__prefix_match3)]
[0, -1, 1, 2, -2, 3, -3, -4, 4]
>>> [*_list_all_inner_sts(andnot1s__prefix_match3)]
[0, -1, 1, 2, 3, -4, 4, -3, -2]
>>> len([*iter_all_inner_sts(andnot1s__prefix_match3)]) == len([*_list_all_inner_sts(andnot1s__prefix_match3)]) == len({*_list_all_inner_sts(andnot1s__prefix_match3)})
True
>>> {*iter_all_inner_sts(andnot1s__prefix_match3)} == {*_list_all_inner_sts(andnot1s__prefix_match3)}
True

]]


#]]]'''
__all__ = r'''


LockMaskBit
    bit4locked_head
    bit4locked_body
    bit4head_return
    bit4body_return
    bit4with_user_result
    bit4full_match
LockMask
    locked_halfway_return
    unlocked_unlocked__without_user_result
    locked_locked_return__without_user_result
    locked_locked_return__with_user_result
    locked_locked
    locked_unlocked
    unlocked_unlocked
    locked_locked_return__with_user_result__full_match
    locked_locked__full_match
    locked_unlocked__full_match
    unlocked_unlocked__full_match
    locked_locked_return__without_user_result__full_match


Error__moveon_nonfinal_inner_st
ISymbolExprInnerStateController
    is_post_pruning_inner_st
    is_inner_st
    is_fail_final_inner_st
    is_success_final_inner_st
        is_fail_final_inner_st
        is_success_final_inner_st
        noninitial_inner_st2is_on_success
            is_step_fail_noninitial_inner_st
            is_step_success_noninitial_inner_st
    step_success_noninitial_inner_st2prev_lock_mask
        nonfinal_inner_st2tmay_lock_mask
        _nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_
    get_initial_inner_st
    moveon_nonfinal_inner_st2next_inner_st__or_raise
        Error__moveon_nonfinal_inner_st
        moveon_nonfinal_inner_st2tmay_next_inner_st

    noninitial_inner_st2prev_inner_st
        noninitial_inner_st2is_on_success
    is_initial_inner_st
    is_final_inner_st
    check_inner_st
    check_initial_inner_st
    check_final_inner_st
    check_noninitial_inner_st
    check_nonfinal_inner_st
    check_step_success_noninitial_inner_st
    iter_all_inner_sts
    iter_all_final_inner_sts
    iter_all_nonfinal_inner_sts
    iter_all_post_pruning_inner_sts
    iter_all_prev_inner_sts__include
    validate_post_pruning_inner_sts

ISymbolExprInnerStateController
    SymbolExprInnerStateController__mutex
    SymbolExprInnerStateController__switch
    SymbolExprInnerStateController__catenation
    SymbolExprInnerStateController__token
    SymbolExprInnerStateController__and1s__full_match
    SymbolExprInnerStateController__and1s__prefix_match
    SymbolExprInnerStateController__andnot1s__full_match
    SymbolExprInnerStateController__andnot1s__prefix_match
    SymbolExprInnerStateController__look_ahead__head
    SymbolExprInnerStateController__look_ahead__body
    SymbolExprInnerStateController__skip
    SymbolExprInnerStateController__look_ahead_not__head
    SymbolExprInnerStateController__look_ahead_not__head_body











lock_mask2does_return
    _nonfinal_inner_st2curr_using_begin_as_stop_position__when_step_success_exists_for_all_nonfinal_inner_st_
    noninitial_inner_st2prev_using_begin_as_stop_position


Cases4Position
check_case4position
    noninitial_inner_st2prev1s_inner_st_case4position_pair_as_begin_position
    noninitial_inner_st2prev1s_inner_st_case4position_pair_as_may_end_position
    inner_st2begin_position
    inner_st2may_end_position

mk_height2inner_st_layer
    mk_inner_st2height
    mk_height2inner_st_layer_ex

VisitInnerStateTree__dfs
    validate_prev1s_inner_st4position_assignment

'''.split()#'''
__all__

#([{
from collections import OrderedDict, Counter, defaultdict
from itertools import filterfalse, islice
from enum import Enum, Flag, auto

from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.tiny import check_type_is, check_uint, check_tmay, snd, curry1, fst, dict_add__is, dict_add__new, null_tuple #, check_type_le, snd, at, curry1, MapView, print_err
#from seed.helper.Echo import theEcho
from seed.types.DictKeyAsObjAttr import namespace5names_str#DictKeyAsObjAttr, DictKeyAsObjAttrAndAsMapping, SetAsNamespace, SetAsNamespaceAndAsMapping, namespace5iterable, namespace5names_str
from seed.types.Namespace import NamespaceSetOnce, NamespaceForbidOverwriteImplicitly#, NamespaceForbidNewKey#Namespace, NamespaceSetOnce
from seed.types.VisitTree import IVisitTree__dfs, visit_tree__dfs
from seed.helper.repr_input import repr_helper

r'''
class LockMaskBit(IntFlag):
    bit4locked_head = 1<<0
    bit4locked_body = 1<<1
    bit4head_return = 1<<2
    bit4body_return = 1<<3
    bit4with_user_result = 1<<4
    bit4full_match = 1<<5
'''#'''
class LockMaskBit(Flag):
    bit4locked_head = auto()
    bit4locked_body = auto()
    bit4head_return = auto()
    bit4body_return = auto()
    bit4with_user_result = auto()
    bit4full_match = auto()
_ = LockMaskBit
bit4locked_head = _.bit4locked_head
bit4locked_body = _.bit4locked_body
bit4head_return = _.bit4head_return
bit4body_return = _.bit4body_return
bit4with_user_result = _.bit4with_user_result
bit4full_match = _.bit4full_match

bit4locked_head
bit4locked_body
bit4head_return
bit4body_return
bit4with_user_result
bit4full_match

_all_lock_mask__bits = (bit4locked_head, bit4locked_body, bit4head_return, bit4body_return, bit4with_user_result, bit4full_match)
assert len({*_all_lock_mask__bits}) == len(_all_lock_mask__bits) == 6
assert {*_all_lock_mask__bits} == {*LockMaskBit.__members__.values()}

bit4locked_head | bit4locked_body | bit4head_return | bit4body_return | bit4with_user_result | bit4full_match

class LockMask(Enum):
    'lock_mask'
    #__prefix_match,__without_user_result
    locked_halfway_return = bit4locked_head | bit4head_return
        #locked_halfway_return = bit4locked_head | bit4head_return | bit4locked_body | bit4body_return
            #to support:_lock_mask2acc
    unlocked_unlocked__without_user_result = bit4locked_head^bit4locked_head
    assert not unlocked_unlocked__without_user_result == 0
    assert unlocked_unlocked__without_user_result.value == 0

    locked_locked_return__without_user_result = bit4locked_head | bit4locked_body | bit4body_return
    #__prefix_match,__with_user_result
    locked_locked_return__with_user_result = bit4locked_head | bit4locked_body | bit4body_return | bit4with_user_result
    locked_locked = bit4locked_head | bit4locked_body | bit4with_user_result
        #unused yet
    locked_unlocked = bit4locked_head | bit4with_user_result
    unlocked_unlocked = bit4with_user_result

    #__full_match,__with_user_result
    locked_locked_return__with_user_result__full_match = bit4locked_head | bit4locked_body | bit4body_return | bit4with_user_result | bit4full_match
    locked_locked__full_match = bit4locked_head | bit4locked_body | bit4with_user_result | bit4full_match
    locked_unlocked__full_match = bit4locked_head | bit4with_user_result | bit4full_match
    unlocked_unlocked__full_match = bit4with_user_result | bit4full_match
    #__full_match,__without_user_result
    locked_locked_return__without_user_result__full_match = bit4locked_head | bit4locked_body | bit4body_return | bit4full_match
#end-class LockMask(Enum):

_ = LockMask
locked_halfway_return = _.locked_halfway_return
unlocked_unlocked__without_user_result = _.unlocked_unlocked__without_user_result

locked_locked_return__without_user_result = _.locked_locked_return__without_user_result
locked_locked_return__with_user_result = _.locked_locked_return__with_user_result
locked_locked = _.locked_locked
locked_unlocked = _.locked_unlocked
unlocked_unlocked = _.unlocked_unlocked

locked_locked_return__with_user_result__full_match = _.locked_locked_return__with_user_result__full_match
locked_locked__full_match = _.locked_locked__full_match
locked_unlocked__full_match = _.locked_unlocked__full_match
unlocked_unlocked__full_match = _.unlocked_unlocked__full_match
locked_locked_return__without_user_result__full_match = _.locked_locked_return__without_user_result__full_match

locked_halfway_return
unlocked_unlocked__without_user_result

locked_locked_return__without_user_result
locked_locked_return__with_user_result
locked_locked
locked_unlocked
unlocked_unlocked

locked_locked_return__with_user_result__full_match
locked_locked__full_match
locked_unlocked__full_match
unlocked_unlocked__full_match
locked_locked_return__without_user_result__full_match

_all_lock_masks = (locked_halfway_return, unlocked_unlocked__without_user_result, locked_locked_return__without_user_result, locked_locked_return__with_user_result, locked_locked, locked_unlocked, unlocked_unlocked, locked_locked_return__with_user_result__full_match, locked_locked__full_match, locked_unlocked__full_match, unlocked_unlocked__full_match, locked_locked_return__without_user_result__full_match)
assert len({*_all_lock_masks}) == len(_all_lock_masks) == 12

assert {*_all_lock_masks} == {*LockMask.__members__.values()}

if 0:
    print(dir(LockMaskBit))
    print(dir(LockMask))
    print(LockMask.__members__)
    print(LockMaskBit.__members__)
_ddd = (
{bit4locked_head
:([locked_halfway_return, locked_locked_return__without_user_result, locked_locked_return__with_user_result, locked_locked, locked_unlocked, locked_locked_return__with_user_result__full_match, locked_locked__full_match, locked_unlocked__full_match, locked_locked_return__without_user_result__full_match]
 ,[unlocked_unlocked__without_user_result, unlocked_unlocked, unlocked_unlocked__full_match])
,bit4locked_body
:([locked_locked_return__without_user_result, locked_locked_return__with_user_result, locked_locked, locked_locked_return__with_user_result__full_match, locked_locked__full_match, locked_locked_return__without_user_result__full_match]
 ,[locked_halfway_return, unlocked_unlocked__without_user_result, locked_unlocked, unlocked_unlocked, locked_unlocked__full_match, unlocked_unlocked__full_match])
,bit4head_return
:([locked_halfway_return]
 ,[unlocked_unlocked__without_user_result, locked_locked_return__without_user_result, locked_locked_return__with_user_result, locked_locked, locked_unlocked, unlocked_unlocked, locked_locked_return__with_user_result__full_match, locked_locked__full_match, locked_unlocked__full_match, unlocked_unlocked__full_match, locked_locked_return__without_user_result__full_match])
,bit4body_return
:([locked_locked_return__without_user_result, locked_locked_return__with_user_result, locked_locked_return__with_user_result__full_match, locked_locked_return__without_user_result__full_match]
 ,[locked_halfway_return, unlocked_unlocked__without_user_result, locked_locked, locked_unlocked, unlocked_unlocked, locked_locked__full_match, locked_unlocked__full_match, unlocked_unlocked__full_match])
,bit4with_user_result
:([locked_locked_return__with_user_result, locked_locked, locked_unlocked, unlocked_unlocked, locked_locked_return__with_user_result__full_match, locked_locked__full_match, locked_unlocked__full_match, unlocked_unlocked__full_match]
 ,[locked_halfway_return, unlocked_unlocked__without_user_result, locked_locked_return__without_user_result, locked_locked_return__without_user_result__full_match])
,bit4full_match
:([locked_locked_return__with_user_result__full_match, locked_locked__full_match, locked_unlocked__full_match, unlocked_unlocked__full_match, locked_locked_return__without_user_result__full_match]
 ,[locked_halfway_return, unlocked_unlocked__without_user_result, locked_locked_return__without_user_result, locked_locked_return__with_user_result, locked_locked, locked_unlocked, unlocked_unlocked])
})
def _(_all_lock_masks, _all_lock_mask__bits, _ddd, /):
    def t(lock_mask_bit, /):
        return [lock_mask.name for lock_mask in _all_lock_masks if lock_mask.value&lock_mask_bit]
    def f(lock_mask_bit, /):
        return [lock_mask.name for lock_mask in _all_lock_masks if not lock_mask.value&lock_mask_bit]
    def main4show(b_show, /):
        d = {}
        for lock_mask_bit in _all_lock_mask__bits:
            d[lock_mask_bit.name] = (t(lock_mask_bit), f(lock_mask_bit))
        if b_show:
            print(d)
        return d

    def ls_nms(xs, /):
        return [x.name for x in xs]
    assert main4show(False)=={k.name:(ls_nms(xs), ls_nms(ys)) for k,(xs,ys) in _ddd.items()}
    pass
_(_all_lock_masks, _all_lock_mask__bits, _ddd)




class ISymbolExprInnerStateController(ABC):
    __slots__ = ()
    #is_final_inner_st
    #check_inner_st
    @abstractmethod
    def is_post_pruning_inner_st(sf, inner_st, /):
        'is_post_pruning_inner_st :: inner_st -> bool'
    @abstractmethod
    def is_inner_st(sf, inner_st, /):
        'is_inner_st :: inner_st -> bool'
    @abstractmethod
    def is_fail_final_inner_st(sf, inner_st, /):
        'is_fail_final_inner_st :: inner_st -> bool #==>> is_final_inner_st'
    @abstractmethod
    def is_success_final_inner_st(sf, inner_st, /):
        'is_success_final_inner_st :: inner_st -> bool #==>> is_final_inner_st'
    @abstractmethod
    def step_success_noninitial_inner_st2prev_lock_mask(sf, step_success_noninitial_inner_st, /):
        'step_success_noninitial_inner_st2prev_lock_mask :: step_success_noninitial_inner_st -> lock_mask'
    if 0:
        #replaced by step_success_noninitial_inner_st2prev_lock_mask
        #see:#step_success_exists_for_all_nonfinal_inner_st
        @abstractmethod
        def _nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_(sf, nonfinal_inner_st, /):
            '_nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ :: nonfinal_inner_st -> lock_mask'
    @abstractmethod
    def get_initial_inner_st(sf, /):
        'get_initial_inner_st :: inner_st'
    @abstractmethod
    def moveon_nonfinal_inner_st2next_inner_st__or_raise(sf, is_on_success, nonfinal_inner_st, /):
        'moveon_nonfinal_inner_st2next_inner_st__or_raise :: is_on_success/bool -> nonfinal_inner_st -> inner_st|raise Error__moveon_nonfinal_inner_st'
    @abstractmethod
    def noninitial_inner_st2prev_inner_st(sf, noninitial_inner_st, /):
        'noninitial_inner_st2prev_inner_st :: noninitial_inner_st -> inner_st'


    @abstractmethod
    def noninitial_nonfinal_inner_st2tmay_prev1s_inner_st_case4position_pair_as_begin_position(sf, noninitial_nonfinal_inner_st, /):
        'noninitial_nonfinal_inner_st -> tmay (prev1s_inner_st, case4position)'
        #see:noninitial_inner_st2prev1s_inner_st_case4position_pair_as_begin_position

    @abstractmethod
    def noninitial_nonfinal_inner_st2tmay_prev1s_inner_st_case4position_pair_as_may_end_position(sf, noninitial_nonfinal_inner_st, /):
        'noninitial_nonfinal_inner_st -> tmay (prev1s_inner_st, case4position)'
        #see:noninitial_inner_st2prev1s_inner_st_case4position_pair_as_may_end_position

    ######################
    ######################
    ######################
    def noninitial_inner_st2is_on_success(sf, noninitial_inner_st, /):
        'noninitial_inner_st2is_on_success :: noninitial_inner_st -> is_on_success'
        prev_inner_st = noninitial_inner_st2prev_inner_st(sf, noninitial_inner_st)

        try:
            inner_st = moveon_nonfinal_inner_st2next_inner_st__or_raise(sf, True, prev_inner_st)
        except Error__moveon_nonfinal_inner_st:
            return False
        else:
            return inner_st==noninitial_inner_st

def noninitial_inner_st2is_on_success(sf, noninitial_inner_st, /):
    'noninitial_inner_st2is_on_success :: noninitial_inner_st -> is_on_success'
    check_noninitial_inner_st(sf, noninitial_inner_st)
    b = sf.noninitial_inner_st2is_on_success(noninitial_inner_st)
    check_type_is(bool, b)
    if 1:
        prev_inner_st = noninitial_inner_st2prev_inner_st(sf, noninitial_inner_st)
        try:
            inner_st = moveon_nonfinal_inner_st2next_inner_st__or_raise(sf, b, prev_inner_st)
        except Error__moveon_nonfinal_inner_st:
            raise logic-err
        else:
            if not inner_st==noninitial_inner_st:raise logic-err
        #assert noninitial_inner_st == moveon_nonfinal_inner_st2next_inner_st__or_raise(sf, b, prev_inner_st)
    return b

def is_post_pruning_inner_st(sf, inner_st, /):
    'is_post_pruning_inner_st :: inner_st -> bool'
    check_inner_st(sf, inner_st)
    b = sf.is_post_pruning_inner_st(inner_st)
    check_type_is(bool, b)
    return b
def is_inner_st(sf, inner_st, /):
    'is_inner_st :: inner_st -> bool'
    b = sf.is_inner_st(inner_st)
    check_type_is(bool, b)
    return b
def is_fail_final_inner_st(sf, inner_st, /):
    'is_fail_final_inner_st :: inner_st -> bool #==>> is_final_inner_st'
    check_inner_st(sf, inner_st)
    b = sf.is_fail_final_inner_st(inner_st)
    check_type_is(bool, b)
    return b
def is_success_final_inner_st(sf, inner_st, /):
    'is_success_final_inner_st :: inner_st -> bool #==>> is_final_inner_st'
    check_inner_st(sf, inner_st)
    b = sf.is_success_final_inner_st(inner_st)
    check_type_is(bool, b)
    return b


# success_final_inner_st may be step_fail_noninitial_inner_st
# fail_final_inner_st may be step_success_noninitial_inner_st
noninitial_inner_st2is_on_success
def is_step_fail_noninitial_inner_st(sf, noninitial_inner_st, /):
    'is_step_fail_noninitial_inner_st :: noninitial_inner_st -> bool'
    return not is_step_success_noninitial_inner_st(sf, noninitial_inner_st)
def is_step_success_noninitial_inner_st(sf, noninitial_inner_st, /):
    'is_step_success_noninitial_inner_st :: noninitial_inner_st -> bool'
    return noninitial_inner_st2is_on_success(sf, noninitial_inner_st)


def step_success_noninitial_inner_st2prev_lock_mask(sf, step_success_noninitial_inner_st, /):
    'step_success_noninitial_inner_st2prev_lock_mask :: step_success_noninitial_inner_st -> lock_mask'
    check_step_success_noninitial_inner_st(sf, step_success_noninitial_inner_st)
    lock_mask = sf.step_success_noninitial_inner_st2prev_lock_mask(step_success_noninitial_inner_st)
    check_type_is(LockMask, lock_mask)
    return lock_mask

def nonfinal_inner_st2tmay_lock_mask(sf, nonfinal_inner_st, /):
    'nonfinal_inner_st2tmay_lock_mask :: nonfinal_inner_st -> tmay_lock_mask'
    tm = moveon_nonfinal_inner_st2tmay_next_inner_st(sf, True, nonfinal_inner_st)
    if not tm:
        [] = tm
        tmay_lock_mask = null_tuple
    else:
        [step_success_noninitial_inner_st] = tm
        lock_mask = step_success_noninitial_inner_st2prev_lock_mask(sf, step_success_noninitial_inner_st)
        tmay_lock_mask = (lock_mask,)
    return tmay_lock_mask
def _nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_(sf, nonfinal_inner_st, /):
    '_nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ :: nonfinal_inner_st -> lock_mask'
    check_nonfinal_inner_st(sf, nonfinal_inner_st)
    lock_mask = sf._nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_(nonfinal_inner_st)
    check_type_is(LockMask, lock_mask)
    return lock_mask

def get_initial_inner_st(sf, /):
    'get_initial_inner_st :: inner_st'
    initial_inner_st = sf.get_initial_inner_st()
    check_inner_st(sf, initial_inner_st)
    #bug:check_initial_inner_st(sf, initial_inner_st)
    return initial_inner_st
def moveon_nonfinal_inner_st2tmay_next_inner_st(sf, is_on_success, nonfinal_inner_st, /):
    'moveon_nonfinal_inner_st2tmay_next_inner_st :: is_on_success/bool -> nonfinal_inner_st -> tmay noninitial_inner_st'
    try:
        next_inner_st = moveon_nonfinal_inner_st2next_inner_st__or_raise(sf, is_on_success, nonfinal_inner_st)
    except Error__moveon_nonfinal_inner_st:
        tmay_next_inner_st = null_tuple
    else:
        tmay_next_inner_st = (next_inner_st,)

    return tmay_next_inner_st
def moveon_nonfinal_inner_st2next_inner_st__or_raise(sf, is_on_success, nonfinal_inner_st, /):
    'moveon_nonfinal_inner_st2next_inner_st__or_raise :: is_on_success/bool -> nonfinal_inner_st -> inner_st|raise Error__moveon_nonfinal_inner_st'
    check_nonfinal_inner_st(sf, nonfinal_inner_st)
    check_type_is(bool, is_on_success)
    next_inner_st = sf.moveon_nonfinal_inner_st2next_inner_st__or_raise(is_on_success, nonfinal_inner_st)
    check_noninitial_inner_st(sf, next_inner_st)
    if not nonfinal_inner_st == noninitial_inner_st2prev_inner_st(sf, next_inner_st): raise logic-err
    if 0:
        #bug: moveon_nonfinal_inner_st2next_inner_st__or_raise(mutex2, True, (0, 1))
        if is_fail_final_inner_st(sf, next_inner_st):
            if is_on_success: raise logic-err
        ###
        if is_success_final_inner_st(sf, next_inner_st):
            if not is_on_success: raise logic-err
    return next_inner_st
def noninitial_inner_st2prev_inner_st(sf, noninitial_inner_st, /):
    'noninitial_inner_st2prev_inner_st :: noninitial_inner_st -> inner_st'
    check_noninitial_inner_st(sf, noninitial_inner_st)
    prev_inner_st = sf.noninitial_inner_st2prev_inner_st(noninitial_inner_st)
    check_nonfinal_inner_st(sf, prev_inner_st)
    return prev_inner_st


def is_initial_inner_st(sf, inner_st, /):
    'is_initial_inner_st :: inner_st -> bool'
    check_inner_st(sf, inner_st)
    return inner_st == get_initial_inner_st(sf)
def is_final_inner_st(sf, inner_st, /):
    'is_final_inner_st :: inner_st -> bool'
    'is_final_inner_st inner_st = is_fail_final_inner_st inner_st or is_success_final_inner_st inner_st'
    (a, b) = (is_fail_final_inner_st(sf, inner_st), is_success_final_inner_st(sf, inner_st))
    if a and b: raise logic-err
    return a or b
    if is_fail_final_inner_st(sf, inner_st) and is_success_final_inner_st(sf, inner_st): raise logic-err
    return is_fail_final_inner_st(sf, inner_st) or is_success_final_inner_st(sf, inner_st)
def check_inner_st(sf, inner_st, /):
    'check_inner_st :: inner_st -> None|raise TypeError'
    if not is_inner_st(sf, inner_st): raise TypeError
def check_initial_inner_st(sf, initial_inner_st, /):
    if not is_initial_inner_st(sf, initial_inner_st): raise TypeError
def check_final_inner_st(sf, final_inner_st, /):
    if not is_final_inner_st(sf, final_inner_st): raise TypeError
def check_noninitial_inner_st(sf, noninitial_inner_st, /):
    if is_initial_inner_st(sf, noninitial_inner_st): raise TypeError
def check_nonfinal_inner_st(sf, nonfinal_inner_st, /):
    if is_final_inner_st(sf, nonfinal_inner_st): raise TypeError

def check_step_success_noninitial_inner_st(sf, step_success_noninitial_inner_st, /):
    if not is_step_success_noninitial_inner_st(sf, step_success_noninitial_inner_st): raise TypeError
class Error__moveon_nonfinal_inner_st(Exception):pass
if 1:
    # to prevent bug in iter_all_inner_sts: cannot catch Error__moveon_nonfinal_inner_st
    from seed.recognize.recognizer_combinator_utils import Error__moveon_nonfinal_inner_st
def iter_all_inner_sts(sf, /):
    ls = []
    def iput(inner_st, /):
        ls.append(inner_st)
        return inner_st
    yield iput(get_initial_inner_st(sf))
    while ls:
        inner_st = ls.pop()
        if is_final_inner_st(sf, inner_st):
            continue

        no_next = True
        for b in _bools:
            try:
                next_inner_st = moveon_nonfinal_inner_st2next_inner_st__or_raise(sf, b, inner_st)
            except Error__moveon_nonfinal_inner_st:
                pass
            else:
                yield iput(next_inner_st)
                no_next = False
        if no_next: raise logic-err-'nonfinal_inner_st has no next_inner_st'
            #cannot_both_fail
_bools = (False, True)
def iter_all_final_inner_sts(sf, /):
    return filter(curry1(is_final_inner_st, sf), iter_all_inner_sts(sf))
def iter_all_nonfinal_inner_sts(sf, /):
    return filterfalse(curry1(is_final_inner_st, sf), iter_all_inner_sts(sf))
def iter_all_post_pruning_inner_sts(sf, /):
    return filter(curry1(is_post_pruning_inner_st, sf), iter_all_inner_sts(sf))
def iter_all_prev_inner_sts__include(sf, inner_st, /):
    while not is_initial_inner_st(sf, inner_st):
        #checked inner_st
        yield inner_st
        inner_st = noninitial_inner_st2prev_inner_st(sf, inner_st)
    yield inner_st
def validate_post_pruning_inner_sts(sf, /):
    #is_post_pruning_inner_st
    def _check(inner_st_path, _bs, /):
        # 0001111
        if not any(_bs): raise logic-err
        i = _bs.index(True)
        if not all(_bs[i:]): raise logic-err
        if i > 0:
            if not inner_st_path[i] == moveon_nonfinal_inner_st2next_inner_st__or_raise(sf, True, inner_st_path[i-1]): raise logic-err
        return
        # 0001000
        if not 1==sum(_bs): raise logic-err
        i = _bs.index(True)
        if i > 0:
            if not inner_st_path[i] == moveon_nonfinal_inner_st2next_inner_st__or_raise(sf, True, inner_st_path[i-1]): raise logic-err
        return
    all_post_pruning_inner_st_set = {*iter_all_post_pruning_inner_sts(sf)}
    for final_inner_st in iter_all_final_inner_sts(sf):
        inner_st_path = (*iter_all_prev_inner_sts__include(sf, final_inner_st),)
        inner_st_path = (*reversed(inner_st_path),)
        _bs = (*map(curry1(is_post_pruning_inner_st, sf), inner_st_path),)
        if is_fail_final_inner_st(sf, final_inner_st):
            #bug:if any(_bs): raise logic-err
            #   body may be bad
            if any(_bs):
                _check(inner_st_path, _bs)
        else:
            if not is_success_final_inner_st(sf, final_inner_st): raise logic-err
            _check(inner_st_path, _bs)

def _nonfinal_inner_st2curr_using_begin_as_stop_position__when_step_success_exists_for_all_nonfinal_inner_st_(sf, nonfinal_inner_st, /):
    'nonfinal_inner_st -> bool #[(nonfinal_inner_st~?).stop_position == .begin_position]'
    lock_mask = _nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_(sf, nonfinal_inner_st)
    if not lock_mask2does_return(lock_mask):
        #step_success and not __return
        return False
    #step_fail or __return
    return True
if 0:
    #see:删去约束
  def noninitial_inner_st2using_prev_begin_as_begin_position(sf, noninitial_inner_st, /):
    'noninitial_inner_st -> bool #[(noninitial_inner_st~?).begin_position == (?~noninitial_inner_st).begin_position/stop_position] <<== since always [(st~?).begin_position == (?~st).stop_position]'
    return noninitial_inner_st2prev_using_begin_as_stop_position(sf, noninitial_inner_st)
def noninitial_inner_st2prev_using_begin_as_stop_position(sf, noninitial_inner_st, /):
    'noninitial_inner_st -> bool #[(?~noninitial_inner_st).stop_position == .begin_position]'
    if noninitial_inner_st2is_on_success(sf, noninitial_inner_st):
        #step_success
        step_success_noninitial_inner_st = noninitial_inner_st
        prev_lock_mask = step_success_noninitial_inner_st2prev_lock_mask(sf, step_success_noninitial_inner_st)
        if not lock_mask2does_return(prev_lock_mask):
            #step_success and not __return
            return False
        #step_success and __return
        return True
        #prev_inner_st = noninitial_inner_st2prev_inner_st(sf, noninitial_inner_st)
        #return _nonfinal_inner_st2curr_using_begin_as_stop_position__when_step_success_exists_for_all_nonfinal_inner_st_(sf, prev_inner_st)
    #step_fail
    return True



##
def noninitial_inner_st2prev1s_inner_st_case4position_pair_as_begin_position(sf, noninitial_inner_st, /):
    'noninitial_inner_st -> (prev1s_inner_st, case4position)'
    check_noninitial_inner_st(sf, noninitial_inner_st)
    if is_final_inner_st(sf, noninitial_inner_st):
        tmay_prev1s_inner_st_case4position_pair = ()
    else:
        noninitial_nonfinal_inner_st = noninitial_inner_st
        tmay_prev1s_inner_st_case4position_pair = sf.noninitial_nonfinal_inner_st2tmay_prev1s_inner_st_case4position_pair_as_begin_position(noninitial_nonfinal_inner_st)

    default_case4position = Cases4Position.stop_position
    return _tmay2prev1s_inner_st_case4position_pair(sf, noninitial_inner_st, default_case4position, tmay_prev1s_inner_st_case4position_pair)

def noninitial_inner_st2prev1s_inner_st_case4position_pair_as_may_end_position(sf, noninitial_inner_st, /):
    'noninitial_inner_st -> (prev1s_inner_st, case4position)'
    check_noninitial_inner_st(sf, noninitial_inner_st)
    if is_final_inner_st(sf, noninitial_inner_st):
        tmay_prev1s_inner_st_case4position_pair = ()
    else:
        noninitial_nonfinal_inner_st = noninitial_inner_st
        tmay_prev1s_inner_st_case4position_pair = sf.noninitial_nonfinal_inner_st2tmay_prev1s_inner_st_case4position_pair_as_may_end_position(noninitial_nonfinal_inner_st)

    default_case4position = Cases4Position.may_end_position
    return _tmay2prev1s_inner_st_case4position_pair(sf, noninitial_inner_st, default_case4position, tmay_prev1s_inner_st_case4position_pair)

def _tmay2prev1s_inner_st_case4position_pair(sf, noninitial_inner_st, default_case4position, tmay_prev1s_inner_st_case4position_pair, /):
    check_tmay(tmay_prev1s_inner_st_case4position_pair)
    if not tmay_prev1s_inner_st_case4position_pair:
        prev_inner_st = noninitial_inner_st2prev_inner_st(sf, noninitial_inner_st)
        prev1s_inner_st = prev_inner_st
        case4position = default_case4position
    else:
        [(prev1s_inner_st, case4position)] = tmay_prev1s_inner_st_case4position_pair
    check_nonfinal_inner_st(sf, prev1s_inner_st)
    check_case4position(case4position)
    #vivi:validate_post_pruning_inner_sts
    #   TODO:validate_prev1s_inner_st4position_assignment
    return (prev1s_inner_st, case4position)

def inner_st2begin_position(sf, get, vars4whole_symbol_expr, prev1s_inner_st2vars, inner_st, /):
    'get/((vars_, case4position) -> position<case>) -> vars_<whole_symbol_expr> -> {prev1s_inner_st:vars_} -> inner_st -> begin_position'
    case4position4whole_symbol_expr = Cases4Position.begin_position
    return _inner_st2xxx_position(sf, get, vars4whole_symbol_expr, case4position4whole_symbol_expr, prev1s_inner_st2vars, inner_st, noninitial_inner_st2prev1s_inner_st_case4position_pair_as_begin_position)
def inner_st2may_end_position(sf, get, vars4whole_symbol_expr, prev1s_inner_st2vars, inner_st, /):
    'get/((vars_, case4position) -> position<case>) -> vars_<whole_symbol_expr> -> {prev1s_inner_st:vars_} -> inner_st -> may_end_position'
    case4position4whole_symbol_expr = Cases4Position.may_end_position
    return _inner_st2xxx_position(sf, get, vars4whole_symbol_expr, case4position4whole_symbol_expr, prev1s_inner_st2vars, inner_st, noninitial_inner_st2prev1s_inner_st_case4position_pair_as_may_end_position)
def _inner_st2xxx_position(sf, get, vars4whole_symbol_expr, case4position4whole_symbol_expr, prev1s_inner_st2vars, inner_st, f, /):
    if is_initial_inner_st(sf, inner_st):
        vars_ = vars4whole_symbol_expr
        case4position = case4position4whole_symbol_expr
    else:
        noninitial_inner_st = inner_st
        (prev1s_inner_st, case4position) = f(sf, noninitial_inner_st)
        vars_ = prev1s_inner_st2vars[prev1s_inner_st]
    return get(vars_, case4position)


def mk_inner_st2height(sf, /):
    d = OrderedDict()
    for sz, inner_st in enumerate(iter_all_inner_sts(sf), 1):
        ls = []
        for prev0s_inner_st in iter_all_prev_inner_sts__include(sf, inner_st):
            if prev0s_inner_st in d:
                break
            ls.append(prev0s_inner_st)
        else:
            if not is_initial_inner_st(sf, ls[-1]): raise logic-err
            initial_inner_st = ls.pop()
            d[initial_inner_st] = 0
            assert prev0s_inner_st is initial_inner_st
        height = d[prev0s_inner_st]
        for height, prev0s_inner_st in enumerate(reversed(ls), 1+height):
            d[prev0s_inner_st] = height
    if not len(d) == sz > 0: raise logic-err
    inner_st2height = d
    return inner_st2height
def mk_height2inner_st_layer(sf, /):
    (inner_st2height, height2inner_st_layer) = mk_height2inner_st_layer_ex(sf)
    return height2inner_st_layer
def mk_height2inner_st_layer_ex(sf, /):
    '-> (inner_st2height, height2inner_st_layer)'
    inner_st2height = mk_inner_st2height(sf)
    height2inner_st_layer = _mk_height2inner_st_layer(inner_st2height)
    return (inner_st2height, height2inner_st_layer)
def _mk_height2inner_st_layer(inner_st2height, /):
    m = max(inner_st2height.values())
    lss = [[] for _ in range(m+1)]
    for inner_st, height in inner_st2height.items():
        lss[height].append(inner_st)
    height2inner_st_layer = lss
    return height2inner_st_layer

class VisitInnerStateTree__dfs(IVisitTree__dfs):
    __slots__ = ()
    def init_st4output(visitor, controller, /):
        '-> st4output'
        st4output = None
        return st4output
    def mk_output(visitor, controller, st4output, result, /):
        '-> output'
        output = (st4output, result)
        return output

    @abstractmethod
    def enter_root(visitor, controller, st4output, initial_inner_st, /):
        '-> Either result hresult'
    def exit_root(visitor, controller, st4output, initial_inner_st, hresult, /):
        '-> None'
    @abstractmethod
    def enter_nonroot(visitor, controller, st4output, prev_inner_st, is_on_success, noninitial_inner_st, /):
        '-> Either result hresult'
    def exit_nonroot(visitor, controller, st4output, prev_inner_st, is_on_success, noninitial_inner_st, hresult, /):
        '-> None'


    def pre_visit_node(visitor, controller, st4output, inner_st, hresult, /):
        '-> Either result presult'
        presult = hresult
        skip_vs_into = True #into
        return (skip_vs_into, presult)
    def post_visit_node(visitor, controller, st4output, inner_st, qresult, /):
        '-> result'
        result = qresult
        return result

    def visit_nonleaf(visitor, controller, st4output, nonfinal_inner_st, presult, is_on_success__next_inner_st__result__triples, /):
        'visitor -> controller -> st4output -> nonfinal_inner_st -> presult -> [(is_on_success,next_inner_st,result)] -> qresult'
    def visit_leaf(visitor, controller, st4output, final_inner_st, presult, /):
        '-> qresult'



    @override
    def get_root(visitor, controller, /):
        '-> initial_inner_st'
        initial_inner_st = get_initial_inner_st(controller)
        return initial_inner_st
    @override
    def is_leaf(visitor, controller, inner_st, /):
        '-> bool'
        return is_final_inner_st(controller, inner_st)
    @override
    def iter_info4dedge_child_pairs(visitor, controller, nonfinal_inner_st, /):
        '-> Iter (is_on_success, next_inner_st)'
        for b in _bools:
            try:
                next_inner_st = moveon_nonfinal_inner_st2next_inner_st__or_raise(controller, b, nonfinal_inner_st)
            except Error__moveon_nonfinal_inner_st:
                pass
            else:
                yield (b, next_inner_st)

class _VisitInnerStateTree__dfs__list_all_inner_sts(VisitInnerStateTree__dfs):
    #to: _list_all_inner_sts
    #vs: iter_all_inner_sts
    __slots__ = ()
    def init_st4output(visitor, controller, /):
        '-> st4output'
        st4output = []
        return st4output
    @override
    def enter_root(visitor, controller, st4output, initial_inner_st, /):
        st4output.append(initial_inner_st)
        return True, ('hresult', initial_inner_st)
    @override
    def enter_nonroot(visitor, controller, st4output, prev_inner_st, is_on_success, noninitial_inner_st, /):
        st4output.append(noninitial_inner_st)
        return True, ('hresult', noninitial_inner_st)


    def exit_root(visitor, controller, st4output, initial_inner_st, hresult, /):
        assert hresult == ('hresult', initial_inner_st)
        assert is_initial_inner_st(controller, initial_inner_st)
    def exit_nonroot(visitor, controller, st4output, prev_inner_st, is_on_success, noninitial_inner_st, hresult, /):
        assert hresult == ('hresult', noninitial_inner_st)
        assert not is_initial_inner_st(controller, noninitial_inner_st)
    def pre_visit_node(visitor, controller, st4output, inner_st, hresult, /):
        '-> Either result presult'
        assert hresult == ('hresult', inner_st)
        assert is_inner_st(controller, inner_st)
        presult = ('presult', inner_st)
        skip_vs_into = True #into
        return (skip_vs_into, presult)
    def post_visit_node(visitor, controller, st4output, inner_st, qresult, /):
        '-> result'
        assert qresult == ('qresult', inner_st)
        assert is_inner_st(controller, inner_st)
        result = ('result', inner_st)
        return result
    def visit_nonleaf(visitor, controller, st4output, nonfinal_inner_st, presult, is_on_success__next_inner_st__result__triples, /):
        'visitor -> controller -> st4output -> nonfinal_inner_st -> presult -> [(is_on_success,next_inner_st,result)] -> qresult'
        assert presult == ('presult', nonfinal_inner_st)
        assert not is_final_inner_st(controller, nonfinal_inner_st)
        assert 1 <= len(is_on_success__next_inner_st__result__triples) <= 2
        assert len(is_on_success__next_inner_st__result__triples) == len({*map(fst, is_on_success__next_inner_st__result__triples)})
        for (is_on_success,next_inner_st,result) in is_on_success__next_inner_st__result__triples:
            assert moveon_nonfinal_inner_st2next_inner_st__or_raise(controller, is_on_success, nonfinal_inner_st) == next_inner_st
            assert result == ('result', next_inner_st)
        return ('qresult', nonfinal_inner_st)
    def visit_leaf(visitor, controller, st4output, final_inner_st, presult, /):
        '-> qresult'
        assert presult == ('presult', final_inner_st)
        assert is_final_inner_st(controller, final_inner_st)
        return ('qresult', final_inner_st)

def _list_all_inner_sts(sf, /):
    (ls, _) = _VisitInnerStateTree__dfs__list_all_inner_sts().visit(sf)
    return ls
#assert {*iter_all_inner_sts(sf)} == {*_list_all_inner_sts(sf)}


#begin-class _VisitInnerStateTree__dfs__check_path__begin_position_avoid_pruning(VisitInnerStateTree__dfs):
class _PPosition:
    def __repr__(sf, /):
        return repr_helper(sf, *sf.args)
    def __init__(sf, /, *args):
        sf.args = args

def _add__pruning_position(ns, pruning_position, /):
    check_type_is(_PPosition, pruning_position)
    ns.pruning_positions[pruning_position] += 1
def _remove__pruning_position(ns, pruning_position, /):
    check_type_is(_PPosition, pruning_position)
    ns.pruning_positions[pruning_position] -= 1
    if 0 > ns.pruning_positions[pruning_position]: raise logic-err
    if not ns.pruning_positions[pruning_position]:
        del ns.pruning_positions[pruning_position]

def _add__LE_relationship(ns, ppositionL, ppositionB, /):
    #pposition2bigger_ppositions :: {ppositionL:{ppositionB:count}} #ppositionL <= ppositionB
    check_type_is(_PPosition, ppositionL)
    check_type_is(_PPosition, ppositionB)
    assert ppositionB is not ppositionL
    ns.pposition2bigger_ppositions[ppositionL][ppositionB] += 1
def _remove__LE_relationship(ns, ppositionL, ppositionB, /):
    check_type_is(_PPosition, ppositionL)
    check_type_is(_PPosition, ppositionB)
    assert ppositionB is not ppositionL
    ns.pposition2bigger_ppositions[ppositionL][ppositionB] -= 1
    if 0 > ns.pposition2bigger_ppositions[ppositionL][ppositionB]: raise logic-err
    if not ns.pposition2bigger_ppositions[ppositionL][ppositionB]:
        del ns.pposition2bigger_ppositions[ppositionL][ppositionB]
    if not ns.pposition2bigger_ppositions[ppositionL]:
        del ns.pposition2bigger_ppositions[ppositionL]
def _has__LE_relationship_path_between(ns, ppositionL, ppositionB, /):
    if ppositionB is ppositionL: return True
    s = set()
    pp2pps = ns.pposition2bigger_ppositions
    ls = []
    def put(pp, /):
        if pp in s:
            return False
        s.add(pp)
        pps = pp2pps.get(pp, null_tuple)
        ls.append(map(put, pps))
        return ppositionB in pps

    if put(ppositionL):
        return True
    while ls:
        for b in ls[-1]:
            if b: return True
            break
        else:
            ls.pop()
    return False

class _VisitInnerStateTree__dfs__check_path__begin_position_avoid_pruning(VisitInnerStateTree__dfs):
    #_check_path__begin_position_avoid_pruning
    __slots__ = ()
    @override
    def init_st4output(visitor, controller, /):
        '-> st4output'
        ns = NamespaceForbidOverwriteImplicitly()
        return ns

    @override
    def enter_root(visitor, sf, ns, initial_inner_st, /):
        '-> Either result hresult'
        #height2inner_st_layer = mk_height2inner_st_layer(sf)
        #[initial_inner_st] = height2inner_st_layer[0]
        #assert is_initial_inner_st(sf, initial_inner_st)
        initial_inner_st = get_initial_inner_st(sf)
        vars4initial_inner_st = NamespaceForbidOverwriteImplicitly()
        vars4initial_inner_st.begin_position = _PPosition(initial_inner_st, Cases4Position.begin_position)
        vars4initial_inner_st.may_end_position = _PPosition(initial_inner_st, Cases4Position.may_end_position)
        inner_st2vars = NamespaceForbidOverwriteImplicitly() #{}
        inner_st2vars[initial_inner_st] = vars4initial_inner_st

        ns.pposition2bigger_ppositions = defaultdict(Counter) #NamespaceForbidOverwriteImplicitly() #{}
            #pposition2bigger_ppositions :: {ppositionL:{ppositionB:count}} #ppositionL <= ppositionB
        #ns.height2inner_st_layer = height2inner_st_layer
        ns.inner_st2vars = inner_st2vars
        #dict_add__is
        #dict_add__new
        _add__LE_relationship
        _remove__LE_relationship
        _add__LE_relationship(ns, vars4initial_inner_st.begin_position, vars4initial_inner_st.may_end_position)

        ns.pruning_positions = Counter()
        return True, None

    @override
    def exit_root(visitor, sf, ns, initial_inner_st, hresult, /):
        '-> None'
        assert not ns.pruning_positions
        del ns.pruning_positions

        inner_st2vars = ns.inner_st2vars
        vars4initial_inner_st = inner_st2vars[initial_inner_st]
        _remove__LE_relationship(ns, vars4initial_inner_st.begin_position, vars4initial_inner_st.may_end_position)
        assert not ns.pposition2bigger_ppositions
        del ns.pposition2bigger_ppositions
        del vars4initial_inner_st.begin_position
        del vars4initial_inner_st.may_end_position
        assert not vars4initial_inner_st
        del inner_st2vars[initial_inner_st]
        assert not inner_st2vars
        del ns.inner_st2vars
        assert not ns

    @override
    def enter_nonroot(visitor, sf, ns, prev_inner_st, is_on_success, noninitial_inner_st, /):
        '-> Either result hresult'
        inner_st2vars = ns.inner_st2vars
        vars4prev_inner_st = inner_st2vars[prev_inner_st]
        assert len(vars4prev_inner_st) == 2
        vars4prev_inner_st.stop_position_before_return = _PPosition(prev_inner_st, Cases4Position.stop_position_before_return)
            #even when step_fail
        vars4prev_inner_st.farthest_touched_end_position = _PPosition(prev_inner_st, Cases4Position.farthest_touched_end_position)
        vars4prev_inner_st.stop_position = vars4prev_inner_st.begin_position if noninitial_inner_st2prev_using_begin_as_stop_position(sf, noninitial_inner_st) else vars4prev_inner_st.stop_position_before_return
        _add__LE_relationship(ns, vars4prev_inner_st.begin_position, vars4prev_inner_st.stop_position_before_return)
        _add__LE_relationship(ns, vars4prev_inner_st.stop_position_before_return, vars4prev_inner_st.farthest_touched_end_position)
        _add__LE_relationship(ns, vars4prev_inner_st.farthest_touched_end_position, vars4prev_inner_st.may_end_position)
        vars4prev_inner_st

        vars4noninitial_inner_st = NamespaceForbidOverwriteImplicitly()
        (prev1s_inner_st, case4position) = noninitial_inner_st2prev1s_inner_st_case4position_pair_as_begin_position(sf, noninitial_inner_st)
        vars4noninitial_inner_st.begin_position = inner_st2vars[prev1s_inner_st][case4position]

        (prev1s_inner_st, case4position) = noninitial_inner_st2prev1s_inner_st_case4position_pair_as_may_end_position(sf, noninitial_inner_st)
        vars4noninitial_inner_st.may_end_position = inner_st2vars[prev1s_inner_st][case4position]

        inner_st2vars[noninitial_inner_st] = vars4noninitial_inner_st

        _add__LE_relationship(ns, vars4noninitial_inner_st.begin_position, vars4noninitial_inner_st.may_end_position)


        _add__pruning_position
        _remove__pruning_position
        for pruning_position in visitor._iter_tmay_pruning_position(sf, ns, prev_inner_st):
            _add__pruning_position(ns, pruning_position)



        _has__LE_relationship_path_between
        for pruning_position in ns.pruning_positions:
            if not _has__LE_relationship_path_between(ns, pruning_position, vars4noninitial_inner_st.begin_position): raise ValueError((sf, prev_inner_st, noninitial_inner_st, pruning_position, vars4noninitial_inner_st.begin_position))
                #to: validate_prev1s_inner_st4position_assignment::_check_path__begin_position_avoid_pruning
        return True, None


    def _iter_tmay_pruning_position(_, sf, ns, prev_inner_st, /):
        lock_mask = _nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_(sf, prev_inner_st)
        if (lock_mask.value&bit4locked_head) and ((lock_mask.value&bit4head_return) or (lock_mask.value&bit4locked_body)):
            #locked_locked
            pass
        else:
            vars4prev_inner_st = ns.inner_st2vars[prev_inner_st]
            pruning_position = vars4prev_inner_st.stop_position
            yield pruning_position

    @override
    def exit_nonroot(visitor, sf, ns, prev_inner_st, is_on_success, noninitial_inner_st, hresult, /):
        '-> None'
        for pruning_position in visitor._iter_tmay_pruning_position(sf, ns, prev_inner_st):
            _remove__pruning_position(ns, pruning_position)

        inner_st2vars = ns.inner_st2vars
        vars4noninitial_inner_st = inner_st2vars[noninitial_inner_st]
        _remove__LE_relationship(ns, vars4noninitial_inner_st.begin_position, vars4noninitial_inner_st.may_end_position)
        del vars4noninitial_inner_st.begin_position
        del vars4noninitial_inner_st.may_end_position
        assert not vars4noninitial_inner_st
        del inner_st2vars[noninitial_inner_st]



        vars4prev_inner_st = inner_st2vars[prev_inner_st]
        _remove__LE_relationship(ns, vars4prev_inner_st.begin_position, vars4prev_inner_st.stop_position_before_return)
        _remove__LE_relationship(ns, vars4prev_inner_st.stop_position_before_return, vars4prev_inner_st.farthest_touched_end_position)
        _remove__LE_relationship(ns, vars4prev_inner_st.farthest_touched_end_position, vars4prev_inner_st.may_end_position)
        del vars4prev_inner_st.stop_position_before_return
        del vars4prev_inner_st.farthest_touched_end_position
        del vars4prev_inner_st.stop_position
        assert len(vars4prev_inner_st) == 2
#end-class _VisitInnerStateTree__dfs__check_path__begin_position_avoid_pruning(VisitInnerStateTree__dfs):

#vivi:validate_post_pruning_inner_sts
def validate_prev1s_inner_st4position_assignment(sf, /):
    #def incomplete_validate_prev1s_inner_st4position_assignment(sf, /):
    #_VisitInnerStateTree__dfs__check_path__begin_position_avoid_pruning
    def main():
        fs = [noninitial_inner_st2prev1s_inner_st_case4position_pair_as_begin_position, noninitial_inner_st2prev1s_inner_st_case4position_pair_as_may_end_position]
        d = {}
        sz = 0
        for sz, noninitial_inner_st in enumerate(islice(iter_all_inner_sts(sf), 1, None), 1):
            ls = []
            for f in fs:
                (prev1s_inner_st, case4position) = f(sf, noninitial_inner_st)
                _check_prev(noninitial_inner_st, prev1s_inner_st, case4position)
                ls.append((prev1s_inner_st, case4position))
            d[noninitial_inner_st] = (*ls,)
        if not len(d) == sz: raise logic-err
        _check_path__begin_position_avoid_pruning(d)
    def _check_path__begin_position_avoid_pruning(noninitial_inner_st2pair_pair, /):
        _VisitInnerStateTree__dfs__check_path__begin_position_avoid_pruning().visit(sf)
        return;#incomplete
    def _check_prev(noninitial_inner_st, prev1s_inner_st, case4position, /):
        check_case4position(case4position)
        check_nonfinal_inner_st(sf, prev1s_inner_st)
        for _prev1s_inner_st in islice(iter_all_prev_inner_sts__include(sf, noninitial_inner_st), 1, None):
            if _prev1s_inner_st == prev1s_inner_st:
                return
        raise logic-err-('prev1s_inner_st not before noninitial_inner_st')
    main()
    return



#end-class ISymbolExprInnerStateController(ABC):

_bits4xxx_return = (bit4head_return|bit4body_return)
def lock_mask2does_return(lock_mask, /):
    'lock_mask -> bool'
    check_type_is(LockMask, lock_mask)
    b = bool(lock_mask.value & _bits4xxx_return)
    return b

# 'case4position'
Cases4Position = namespace5names_str(
    #whole_symbol_expr_begin_position
    #whole_symbol_expr_may_end_position
    #farthest_touched_end_position_ex
r'''
    begin_position
    may_end_position
    stop_position
    stop_position_before_return
    farthest_touched_end_position
'''#'''
)
def check_case4position(case4position, /):
    check_type_is(str, case4position)
    if not case4position in Cases4Position: raise TypeError



class _ISymbolExprInnerStateController__base_tuple(ISymbolExprInnerStateController, tuple):
    __slots__ = ()
    def __new__(cls, /, *args):
        sf = super(__class__, cls).__new__(cls, args)
        return sf
class _ISymbolExprInnerStateController__mixins__step_success_exists_for_all_nonfinal_inner_st(ISymbolExprInnerStateController):
    #step_success_exists_for_all_nonfinal_inner_st
    __slots__ = ()
    @abstractmethod
    def _nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_(sf, nonfinal_inner_st, /):
        '_nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ :: nonfinal_inner_st -> lock_mask'
    @override
    def step_success_noninitial_inner_st2prev_lock_mask(sf, step_success_noninitial_inner_st, /):
        'step_success_noninitial_inner_st2prev_lock_mask :: step_success_noninitial_inner_st -> lock_mask'
        check_step_success_noninitial_inner_st(sf, step_success_noninitial_inner_st)
        prev_inner_st = noninitial_inner_st2prev_inner_st(sf, step_success_noninitial_inner_st)
        return sf._nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_(prev_inner_st)

class _ISymbolExprInnerStateController__mixins__plain_bound_position(ISymbolExprInnerStateController):
    #plain_bound_position
    __slots__ = ()
    @override
    def noninitial_nonfinal_inner_st2tmay_prev1s_inner_st_case4position_pair_as_begin_position(sf, noninitial_nonfinal_inner_st, /):
        'noninitial_nonfinal_inner_st -> tmay (prev1s_inner_st, case4position)'
        #noninitial_nonfinal_inner_st2tmay_prev1s_inner_st_case4position_pair_as_begin_position _ = ()
        return ()

    @override
    def noninitial_nonfinal_inner_st2tmay_prev1s_inner_st_case4position_pair_as_may_end_position(sf, noninitial_nonfinal_inner_st, /):
        'noninitial_nonfinal_inner_st -> tmay (prev1s_inner_st, case4position)'
        #noninitial_nonfinal_inner_st2tmay_prev1s_inner_st_case4position_pair_as_may_end_position noninitial_nonfinal_inner_st = ()
        return ()

class _ISymbolExprInnerStateController__base_tuple__L(_ISymbolExprInnerStateController__base_tuple):
    __slots__ = ()
    def __init__(sf, L, /):
        check_uint(L)
    @property
    def _L(sf, /):
        return sf[0]
class SymbolExprInnerStateController__mutex(_ISymbolExprInnerStateController__mixins__step_success_exists_for_all_nonfinal_inner_st, _ISymbolExprInnerStateController__mixins__plain_bound_position, _ISymbolExprInnerStateController__base_tuple__L):
    'mutex'
    __slots__ = ()

    @override
    def is_post_pruning_inner_st(sf, inner_st, /):
        'is_post_pruning_inner_st :: inner_st -> bool'
        return sf.is_success_final_inner_st(inner_st)
    @override
    def is_inner_st(sf, inner_st, /):
        'is_inner_st :: inner_st -> bool'
        L = sf._L
        #inner_st = (idx4prev_success, idx4curr_branch) :: ([0..=L], [-L..=L])
        if not (type(inner_st) is tuple and len(inner_st)==2):
            return False

        (idx4prev_success, idx4curr_branch) = inner_st
        if not (type(idx4prev_success) is int and 0 <= idx4prev_success <= L):
            return False
        if not (type(idx4curr_branch) is int and -L <= idx4curr_branch <= L):
            return False
        return True

    @override
    def is_fail_final_inner_st(sf, inner_st, /):
        'is_fail_final_inner_st :: inner_st -> bool'
        L = sf._L
        #is_fail_final_inner_st inner_st = inner_st==(L, L) or -L < snd inner_st < 0
        return inner_st == (L,L) or -L < snd(inner_st) < 0
    @override
    def is_success_final_inner_st(sf, inner_st, /):
        'is_success_final_inner_st :: inner_st -> bool'
        L = sf._L
        #is_success_final_inner_st (idx4prev_success, idx4curr_branch) = idx4prev_success < L and idx4curr_branch==-L
        (idx4prev_success, idx4curr_branch) = inner_st
        return idx4prev_success < L and idx4curr_branch==-L
    @override
    def _nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_(sf, nonfinal_inner_st, /):
        '_nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ :: nonfinal_inner_st -> lock_mask'
        L = sf._L
        #_nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ (_, idx4curr_branch) = if idx4curr_branch==L then unlocked_unlocked else locked_halfway_return
        inner_st = nonfinal_inner_st
        (idx4prev_success, idx4curr_branch) = inner_st
        return LockMask.unlocked_unlocked if idx4curr_branch==L else LockMask.locked_halfway_return

    @override
    def get_initial_inner_st(sf, /):
        'get_initial_inner_st :: inner_st'
        L = sf._L
        #get_initial_inner_st = (L, 0)
        return (L, 0)
    @override
    def moveon_nonfinal_inner_st2next_inner_st__or_raise(sf, is_on_success, nonfinal_inner_st, /):
        'moveon_nonfinal_inner_st2next_inner_st__or_raise :: is_on_success/bool -> nonfinal_inner_st -> inner_st|raise Error__moveon_nonfinal_inner_st'
        L = sf._L
        r'''[[[
        moveon_nonfinal_inner_st2next_inner_st__or_raise is_on_success (idx4prev_success, idx4curr_branch) = if not is_on_success then (idx4prev_success, idx4curr_branch+1) elif idx4prev_success==L then (idx4curr_branch, idx4curr_branch+1) elif not idx4curr_branch==L then (idx4prev_success, -idx4curr_branch) else (idx4prev_success, -L)
        ===
        moveon_nonfinal_inner_st2next_inner_st__or_raise False (idx4prev_success, L) = error
        moveon_nonfinal_inner_st2next_inner_st__or_raise False (L, idx4curr_branch) = (L, idx4curr_branch+1)
        moveon_nonfinal_inner_st2next_inner_st__or_raise False (idx4prev_success, idx4curr_branch) = (idx4prev_success, idx4curr_branch+1)

        moveon_nonfinal_inner_st2next_inner_st__or_raise True (idx4prev_success, L) = (idx4prev_success, -L)
        moveon_nonfinal_inner_st2next_inner_st__or_raise True (idx4prev_success, idx4curr_branch) = (idx4prev_success, -idx4curr_branch)
        #]]]'''
        (idx4prev_success, idx4curr_branch) = nonfinal_inner_st
        if not is_on_success:
            if idx4curr_branch==L:
                raise Error__moveon_nonfinal_inner_st(nonfinal_inner_st)#logic-err
            return (idx4prev_success, idx4curr_branch+1)
        elif idx4prev_success==L:
            return (idx4curr_branch, idx4curr_branch+1)
        else:
            return (idx4prev_success, -idx4curr_branch)
        pass

    @override
    def noninitial_inner_st2prev_inner_st(sf, noninitial_inner_st, /):
        'noninitial_inner_st2prev_inner_st :: noninitial_inner_st -> inner_st'
        L = sf._L
        #noninitial_inner_st2prev_inner_st (L, idx4curr_branch) = (L, idx4curr_branch-1)
        #noninitial_inner_st2prev_inner_st (idx4prev_success, idx4curr_branch) = if idx4curr_branch < 0 then (idx4prev_success, -idx4curr_branch) elif idx4curr_branch == idx4prev_success+1 then (L, idx4prev_success) else (idx4prev_success, idx4curr_branch-1)
        (idx4prev_success, idx4curr_branch) = noninitial_inner_st
        if idx4prev_success==L:
            return (L, idx4curr_branch-1)
        elif idx4curr_branch < 0:
            return (idx4prev_success, -idx4curr_branch)
        elif idx4curr_branch == idx4prev_success+1:
            return (L, idx4prev_success)
        else:
            return (idx4prev_success, idx4curr_branch-1)
#end-class SymbolExprInnerStateController__mutex(_ISymbolExprInnerStateController__base_tuple__L):


class SymbolExprInnerStateController__switch(_ISymbolExprInnerStateController__mixins__step_success_exists_for_all_nonfinal_inner_st, _ISymbolExprInnerStateController__mixins__plain_bound_position, _ISymbolExprInnerStateController__base_tuple__L):
    'switch'
    __slots__ = ()

    @override
    def is_post_pruning_inner_st(sf, inner_st, /):
        'is_post_pruning_inner_st :: inner_st -> bool'
        return sf.is_success_final_inner_st(inner_st)
    @override
    def is_inner_st(sf, inner_st, /):
        'is_inner_st :: inner_st -> bool'
        L = sf._L
        #inner_st = idx4curr_branch :: [-L..=L]
        idx4curr_branch = inner_st
        if not (type(idx4curr_branch) is int and -L <= idx4curr_branch <= L):
            return False
        return True

    @override
    def is_fail_final_inner_st(sf, inner_st, /):
        'is_fail_final_inner_st :: inner_st -> bool'
        L = sf._L
        #is_fail_final_inner_st inner_st = inner_st==L
        return inner_st==L
    @override
    def is_success_final_inner_st(sf, inner_st, /):
        'is_success_final_inner_st :: inner_st -> bool'
        L = sf._L
        #is_success_final_inner_st inner_st = inner_st < 0
        return inner_st < 0
    @override
    def _nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_(sf, nonfinal_inner_st, /):
        '_nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ :: nonfinal_inner_st -> lock_mask'
        L = sf._L
        #_nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ idx4curr_branch = if idx4curr_branch==L-1 then unlocked_unlocked else locked_unlocked
        idx4curr_branch = nonfinal_inner_st
        return LockMask.unlocked_unlocked if idx4curr_branch==L-1 else LockMask.locked_unlocked
    @override
    def get_initial_inner_st(sf, /):
        'get_initial_inner_st :: inner_st'
        L = sf._L
        #get_initial_inner_st = 0
        return 0
    @override
    def moveon_nonfinal_inner_st2next_inner_st__or_raise(sf, is_on_success, nonfinal_inner_st, /):
        'moveon_nonfinal_inner_st2next_inner_st__or_raise :: is_on_success/bool -> nonfinal_inner_st -> inner_st|raise Error__moveon_nonfinal_inner_st'
        L = sf._L
        #moveon_nonfinal_inner_st2next_inner_st__or_raise is_on_success idx4curr_branch = if is_on_success then -1-idx4curr_branch else idx4curr_branch+1
        idx4curr_branch = nonfinal_inner_st
        return -1-idx4curr_branch if is_on_success else idx4curr_branch+1
    @override
    def noninitial_inner_st2prev_inner_st(sf, noninitial_inner_st, /):
        'noninitial_inner_st2prev_inner_st :: noninitial_inner_st -> inner_st'
        L = sf._L
        #noninitial_inner_st2prev_inner_st noninitial_inner_st = if noninitial_inner_st < 0 then -1-noninitial_inner_st else noninitial_inner_st-1
        return -1-noninitial_inner_st if noninitial_inner_st < 0 else noninitial_inner_st-1

#end-class SymbolExprInnerStateController__switch(_ISymbolExprInnerStateController__base_tuple__L):


class _ISymbolExprInnerStateController__base_tuple__L__idx4pruning_head(_ISymbolExprInnerStateController__base_tuple__L):
    __slots__ = ()
    def __init__(sf, L, idx4pruning_head, /):
        #.idx4pruning_head :: [-1..=L]
        check_uint(L)
        check_type_is(int, idx4pruning_head)
        if not -1 <= idx4pruning_head < L: raise TypeError
    @property
    def _idx4pruning_head(sf, /):
        return sf[1]


class SymbolExprInnerStateController__catenation(_ISymbolExprInnerStateController__mixins__step_success_exists_for_all_nonfinal_inner_st, _ISymbolExprInnerStateController__mixins__plain_bound_position, _ISymbolExprInnerStateController__base_tuple__L__idx4pruning_head):
    'catenation'
    __slots__ = ()
    @override
    def is_post_pruning_inner_st(sf, inner_st, /):
        'is_post_pruning_inner_st :: inner_st -> bool'
        #is_post_pruning_inner_st inner_st = (-1-inner_st if inner_st < 0 else inner_st) > idx4pruning_head
        idx4pruning_head = sf._idx4pruning_head
        return (-1-inner_st if inner_st < 0 else inner_st) > idx4pruning_head
        return inner_st == 1+idx4pruning_head
    @override
    def is_inner_st(sf, inner_st, /):
        'is_inner_st :: inner_st -> bool'
        L = sf._L
        #inner_st = idx :: [-L..=L]
        if not (type(inner_st) is int and -L <= inner_st <= L):
            return False
        return True


    @override
    def is_fail_final_inner_st(sf, inner_st, /):
        'is_fail_final_inner_st :: inner_st -> bool'
        L = sf._L
        #is_fail_final_inner_st inner_st = inner_st < 0
        return inner_st < 0
    @override
    def is_success_final_inner_st(sf, inner_st, /):
        'is_success_final_inner_st :: inner_st -> bool'
        L = sf._L
        #is_success_final_inner_st inner_st = inner_st==L
        return inner_st==L
    @override
    def _nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_(sf, nonfinal_inner_st, /):
        '_nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ :: nonfinal_inner_st -> lock_mask'
        #_nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ inner_st = unlocked_unlocked
        #   see:is_post_pruning_inner_st
        return LockMask.unlocked_unlocked
        ############
        r'''[[[
        L = sf._L
        idx4pruning_head = sf._idx4pruning_head
        #_nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ inner_st = if inner_st < idx4pruning_head then locked_locked elif inner_st==idx4pruning_head then locked_unlocked else unlocked_unlocked
        inner_st = nonfinal_inner_st
        if inner_st < idx4pruning_head:
            return LockMask.locked_locked
        elif inner_st==idx4pruning_head:
            return LockMask.locked_unlocked
        else:
            return LockMask.unlocked_unlocked
        pass
        #]]]'''
    @override
    def get_initial_inner_st(sf, /):
        'get_initial_inner_st :: inner_st'
        L = sf._L
        #get_initial_inner_st = 0
        return 0
    @override
    def moveon_nonfinal_inner_st2next_inner_st__or_raise(sf, is_on_success, nonfinal_inner_st, /):
        'moveon_nonfinal_inner_st2next_inner_st__or_raise :: is_on_success/bool -> nonfinal_inner_st -> inner_st|raise Error__moveon_nonfinal_inner_st'
        L = sf._L
        #moveon_nonfinal_inner_st2next_inner_st__or_raise is_on_success nonfinal_inner_st = if is_on_success then nonfinal_inner_st+1 else -1-nonfinal_inner_st
        return nonfinal_inner_st+1 if is_on_success else -1-nonfinal_inner_st
    @override
    def noninitial_inner_st2prev_inner_st(sf, noninitial_inner_st, /):
        'noninitial_inner_st2prev_inner_st :: noninitial_inner_st -> inner_st'
        L = sf._L
        #noninitial_inner_st2prev_inner_st noninitial_inner_st = if noninitial_inner_st < 0 then -1-noninitial_inner_st else noninitial_inner_st-1
        return -1-noninitial_inner_st if noninitial_inner_st < 0 else noninitial_inner_st-1
#end-class SymbolExprInnerStateController__catenation(_ISymbolExprInnerStateController__base_tuple__L):

class SymbolExprInnerStateController__token(_ISymbolExprInnerStateController__mixins__step_success_exists_for_all_nonfinal_inner_st, _ISymbolExprInnerStateController__mixins__plain_bound_position, ISymbolExprInnerStateController):
    'token'
    __slots__ = ()

    @override
    def is_post_pruning_inner_st(sf, inner_st, /):
        'is_post_pruning_inner_st :: inner_st -> bool'
        return sf.is_success_final_inner_st(inner_st)
    @override
    def is_inner_st(sf, inner_st, /):
        'is_inner_st :: inner_st -> bool'
        #inner_st = idx :: [-1..=1]
        if not (type(inner_st) is int and -1 <= inner_st <= 1):
            return False
        return True


    @override
    def is_fail_final_inner_st(sf, inner_st, /):
        'is_fail_final_inner_st :: inner_st -> bool'
        #is_fail_final_inner_st inner_st = inner_st == -1
        return inner_st == -1
    @override
    def is_success_final_inner_st(sf, inner_st, /):
        'is_success_final_inner_st :: inner_st -> bool'
        #is_success_final_inner_st inner_st = inner_st == +1
        return inner_st == +1
    @override
    def _nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_(sf, nonfinal_inner_st, /):
        '_nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ :: nonfinal_inner_st -> lock_mask'
        return LockMask.unlocked_unlocked
    @override
    def get_initial_inner_st(sf, /):
        'get_initial_inner_st :: inner_st'
        #get_initial_inner_st = 0
        return 0
    @override
    def moveon_nonfinal_inner_st2next_inner_st__or_raise(sf, is_on_success, nonfinal_inner_st, /):
        'moveon_nonfinal_inner_st2next_inner_st__or_raise :: is_on_success/bool -> nonfinal_inner_st -> inner_st|raise Error__moveon_nonfinal_inner_st'
        return +1 if is_on_success else -1
    @override
    def noninitial_inner_st2prev_inner_st(sf, noninitial_inner_st, /):
        'noninitial_inner_st2prev_inner_st :: noninitial_inner_st -> inner_st'
        return 0
#end-class SymbolExprInnerStateController__token(ISymbolExprInnerStateController):


class _ISymbolExprInnerStateController__base_tuple__L1(_ISymbolExprInnerStateController__base_tuple__L):
    __slots__ = ()
    def __init__(sf, L, /):
        check_uint(L)
        if not 1 <= L: raise TypeError
class _SymbolExprInnerStateController__and1s(_ISymbolExprInnerStateController__mixins__step_success_exists_for_all_nonfinal_inner_st, _ISymbolExprInnerStateController__base_tuple__L1):
    'and1s'
    __slots__ = ()
    #[L >= 1]

    @override
    def is_post_pruning_inner_st(sf, inner_st, /):
        'is_post_pruning_inner_st :: inner_st -> bool'
        #is_post_pruning_inner_st inner_st = is_success_final_inner_st inner_st
        return sf.is_success_final_inner_st(inner_st)
    @override
    def is_inner_st(sf, inner_st, /):
        'is_inner_st :: inner_st -> bool'
        L = sf._L
        #inner_st = idx4curr_branch :: [-L..=L]
        if not (type(inner_st) is int and -L <= inner_st <= L):
            return False
        return True


    @override
    def is_fail_final_inner_st(sf, inner_st, /):
        'is_fail_final_inner_st :: inner_st -> bool'
        L = sf._L
        #is_fail_final_inner_st inner_st = inner_st < 0
        return inner_st < 0
    @override
    def is_success_final_inner_st(sf, inner_st, /):
        'is_success_final_inner_st :: inner_st -> bool'
        L = sf._L
        #is_success_final_inner_st inner_st = inner_st == +L
        return inner_st == +L
    if 0:
        #and1s__full_match._nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ inner_st = if inner_st==L-1 then unlocked_unlocked__full_match elif inner_st==0 then locked_locked_return__with_user_result else locked_locked_return__with_user_result__full_match
        #and1s__prefix_match._nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ inner_st = if inner_st==L-1 then unlocked_unlocked else locked_locked_return__with_user_result
        r'''[[[
        @override
        def _nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_(sf, nonfinal_inner_st, /):
            '_nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ :: nonfinal_inner_st -> lock_mask'
            L = sf._L
            return LockMask.unlocked_unlocked if nonfinal_inner_st==L-1 else LockMask.locked_locked
        #]]]'''
    @override
    def get_initial_inner_st(sf, /):
        'get_initial_inner_st :: inner_st'
        L = sf._L
        #get_initial_inner_st = 0
        return 0
    @override
    def moveon_nonfinal_inner_st2next_inner_st__or_raise(sf, is_on_success, nonfinal_inner_st, /):
        'moveon_nonfinal_inner_st2next_inner_st__or_raise :: is_on_success/bool -> nonfinal_inner_st -> inner_st|raise Error__moveon_nonfinal_inner_st'
        L = sf._L
        #moveon_nonfinal_inner_st2next_inner_st__or_raise is_on_success idx4curr_branch = if is_on_success then +1+idx4curr_branch else -1-idx4curr_branch
        idx4curr_branch = nonfinal_inner_st
        return +1+idx4curr_branch if is_on_success else -1-idx4curr_branch
    @override
    def noninitial_inner_st2prev_inner_st(sf, noninitial_inner_st, /):
        'noninitial_inner_st2prev_inner_st :: noninitial_inner_st -> inner_st'
        L = sf._L
        #noninitial_inner_st2prev_inner_st noninitial_inner_st = if noninitial_inner_st < 0 then -1-noninitial_inner_st else noninitial_inner_st-1
        return -1-noninitial_inner_st if noninitial_inner_st < 0 else noninitial_inner_st-1

    @override
    def noninitial_nonfinal_inner_st2tmay_prev1s_inner_st_case4position_pair_as_begin_position(sf, noninitial_nonfinal_inner_st, /):
        'noninitial_nonfinal_inner_st -> tmay (prev1s_inner_st, case4position)'
        #noninitial_nonfinal_inner_st2tmay_prev1s_inner_st_case4position_pair_as_begin_position _ = ()
        return ()

    @override
    def noninitial_nonfinal_inner_st2tmay_prev1s_inner_st_case4position_pair_as_may_end_position(sf, noninitial_nonfinal_inner_st, /):
        'noninitial_nonfinal_inner_st -> tmay (prev1s_inner_st, case4position)'
        #noninitial_nonfinal_inner_st2tmay_prev1s_inner_st_case4position_pair_as_may_end_position noninitial_nonfinal_inner_st = if noninitial_nonfinal_inner_st == 1 then ((0, Cases4Position.stop_position_before_return),) else ()
        if noninitial_nonfinal_inner_st == 1:
            return ((0, Cases4Position.stop_position_before_return),)
        return ()

#end-class _SymbolExprInnerStateController__and1s(ISymbolExprInnerStateController):

class SymbolExprInnerStateController__and1s__full_match(_SymbolExprInnerStateController__and1s):
    'and1s/and1s__full_match'
    __slots__ = ()
    #[L >= 1]
    @override
    def _nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_(sf, nonfinal_inner_st, /):
        '_nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ :: nonfinal_inner_st -> lock_mask'
        L = sf._L
        #and1s__full_match._nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ inner_st = if inner_st==L-1 then unlocked_unlocked__full_match elif inner_st==0 then locked_locked_return__with_user_result else locked_locked_return__with_user_result__full_match
        return LockMask.unlocked_unlocked__full_match if nonfinal_inner_st==L-1 else LockMask.locked_locked_return__with_user_result if nonfinal_inner_st==0 else LockMask.locked_locked_return__with_user_result__full_match
class SymbolExprInnerStateController__and1s__prefix_match(_SymbolExprInnerStateController__and1s):
    'and1s/and1s__prefix_match'
    __slots__ = ()
    #[L >= 1]
    @override
    def _nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_(sf, nonfinal_inner_st, /):
        '_nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ :: nonfinal_inner_st -> lock_mask'
        L = sf._L
        #and1s__prefix_match._nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ inner_st = if inner_st==L-1 then unlocked_unlocked else locked_locked_return__with_user_result
        return LockMask.unlocked_unlocked if nonfinal_inner_st==L-1 else LockMask.locked_locked_return__with_user_result







class _SymbolExprInnerStateController__andnot1s(_ISymbolExprInnerStateController__mixins__step_success_exists_for_all_nonfinal_inner_st, _ISymbolExprInnerStateController__base_tuple__L1):
    'andnot1s'
    __slots__ = ()
    #[L >= 1]

    @override
    def is_post_pruning_inner_st(sf, inner_st, /):
        'is_post_pruning_inner_st :: inner_st -> bool'
        #is_post_pruning_inner_st inner_st = is_success_final_inner_st inner_st
        return sf.is_success_final_inner_st(inner_st)
    @override
    def is_inner_st(sf, inner_st, /):
        'is_inner_st :: inner_st -> bool'
        L = sf._L
        #inner_st = idx4curr_branch :: [-1-L..=L+1]
        if not (type(inner_st) is int and -1-L <= inner_st <= +1+L):
            return False
        return True


    @override
    def is_fail_final_inner_st(sf, inner_st, /):
        'is_fail_final_inner_st :: inner_st -> bool'
        L = sf._L
        #is_fail_final_inner_st inner_st = inner_st < 0
        return inner_st < 0
    @override
    def is_success_final_inner_st(sf, inner_st, /):
        'is_success_final_inner_st :: inner_st -> bool'
        L = sf._L
        #is_success_final_inner_st inner_st = inner_st == 1+L
        return inner_st == 1+L
    if 0:
        #andnot1s__prefix_match._nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ inner_st = if inner_st==L then unlocked_unlocked__full_match else locked_locked_return__without_user_result
        #andnot1s__full_match._nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ inner_st = if inner_st==L then unlocked_unlocked__full_match elif inner_st==0 then locked_locked_return__without_user_result else locked_locked_return__without_user_result__full_match
        r'''[[[
        @override
        def _nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_(sf, nonfinal_inner_st, /):
            '_nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ :: nonfinal_inner_st -> lock_mask'
            L = sf._L
            #_nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ inner_st = if inner_st==L then unlocked_unlocked else locked_locked
            return LockMask.unlocked_unlocked if nonfinal_inner_st==L else LockMask.locked_locked
        #]]]'''
    @override
    def get_initial_inner_st(sf, /):
        'get_initial_inner_st :: inner_st'
        L = sf._L
        #get_initial_inner_st = 0
        return 0
    @override
    def moveon_nonfinal_inner_st2next_inner_st__or_raise(sf, is_on_success, nonfinal_inner_st, /):
        'moveon_nonfinal_inner_st2next_inner_st__or_raise :: is_on_success/bool -> nonfinal_inner_st -> inner_st|raise Error__moveon_nonfinal_inner_st'
        L = sf._L
        r'''[[[
        moveon_nonfinal_inner_st2next_inner_st__or_raise is_on_success idx4curr_branch = if is_on_success^(idx4curr_branch in (0,L)) then -1-idx4curr_branch else +1+idx4curr_branch
        moveon_nonfinal_inner_st2next_inner_st__or_raise is_on_success 0 = if is_on_success then +1 else -1
        moveon_nonfinal_inner_st2next_inner_st__or_raise is_on_success L = if is_on_success then +1+L else -1-L
        moveon_nonfinal_inner_st2next_inner_st__or_raise is_on_success idx4curr_branch = if is_on_success then -1-idx4curr_branch else +1+idx4curr_branch
        #]]]'''
        idx4curr_branch = nonfinal_inner_st
        return -1-idx4curr_branch if is_on_success^(idx4curr_branch in (0,L)) else +1+idx4curr_branch
    @override
    def noninitial_inner_st2prev_inner_st(sf, noninitial_inner_st, /):
        'noninitial_inner_st2prev_inner_st :: noninitial_inner_st -> inner_st'
        L = sf._L
        #noninitial_inner_st2prev_inner_st noninitial_inner_st = if noninitial_inner_st < 0 then -1-noninitial_inner_st else noninitial_inner_st-1
        return -1-noninitial_inner_st if noninitial_inner_st < 0 else noninitial_inner_st-1

    @override
    def noninitial_nonfinal_inner_st2tmay_prev1s_inner_st_case4position_pair_as_begin_position(sf, noninitial_nonfinal_inner_st, /):
        'noninitial_nonfinal_inner_st -> tmay (prev1s_inner_st, case4position)'
        #noninitial_nonfinal_inner_st2tmay_prev1s_inner_st_case4position_pair_as_begin_position _ = ()
        return ()

    @override
    def noninitial_nonfinal_inner_st2tmay_prev1s_inner_st_case4position_pair_as_may_end_position(sf, noninitial_nonfinal_inner_st, /):
        'noninitial_nonfinal_inner_st -> tmay (prev1s_inner_st, case4position)'
        #noninitial_nonfinal_inner_st2tmay_prev1s_inner_st_case4position_pair_as_may_end_position noninitial_nonfinal_inner_st = if noninitial_nonfinal_inner_st == 1 then ((0, Cases4Position.stop_position_before_return),) else ()
        if noninitial_nonfinal_inner_st == 1:
            return ((0, Cases4Position.stop_position_before_return),)
        return ()

#end-class _SymbolExprInnerStateController__andnot1s(ISymbolExprInnerStateController):

class SymbolExprInnerStateController__andnot1s__full_match(_SymbolExprInnerStateController__andnot1s):
    'andnot1s/andnot1s__full_match'
    __slots__ = ()
    #[L >= 1]
    @override
    def _nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_(sf, nonfinal_inner_st, /):
        '_nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ :: nonfinal_inner_st -> lock_mask'
        L = sf._L
        #andnot1s__full_match._nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ inner_st = if inner_st==L then unlocked_unlocked__full_match elif inner_st==0 then locked_locked_return__without_user_result else locked_locked_return__without_user_result__full_match
        return LockMask.unlocked_unlocked__full_match if nonfinal_inner_st==L else LockMask.locked_locked_return__without_user_result if nonfinal_inner_st==0 else LockMask.locked_locked_return__without_user_result__full_match
class SymbolExprInnerStateController__andnot1s__prefix_match(_SymbolExprInnerStateController__andnot1s):
    'andnot1s/andnot1s__prefix_match'
    __slots__ = ()
    #[L >= 1]
    @override
    def _nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_(sf, nonfinal_inner_st, /):
        '_nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ :: nonfinal_inner_st -> lock_mask'
        L = sf._L
        #andnot1s__prefix_match._nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ inner_st = if inner_st==L then unlocked_unlocked__full_match else locked_locked_return__without_user_result
        return LockMask.unlocked_unlocked__full_match if nonfinal_inner_st==L else LockMask.locked_locked_return__without_user_result




class _ISymbolExprInnerStateController__look_ahead(_ISymbolExprInnerStateController__mixins__step_success_exists_for_all_nonfinal_inner_st, ISymbolExprInnerStateController):
    'look_ahead'
    __slots__ = ()

    @override
    def is_post_pruning_inner_st(sf, inner_st, /):
        'is_post_pruning_inner_st :: inner_st -> bool'
        return sf.is_success_final_inner_st(inner_st)
    @override
    def is_inner_st(sf, inner_st, /):
        'is_inner_st :: inner_st -> bool'
        #inner_st = idx :: [-1..=1]
        if not (type(inner_st) is int and -1 <= inner_st <= 1):
            return False
        return True


    @override
    def is_fail_final_inner_st(sf, inner_st, /):
        'is_fail_final_inner_st :: inner_st -> bool'
        #is_fail_final_inner_st inner_st = inner_st == -1
        return inner_st == -1
    @override
    def is_success_final_inner_st(sf, inner_st, /):
        'is_success_final_inner_st :: inner_st -> bool'
        #is_success_final_inner_st inner_st = inner_st == +1
        return inner_st == +1
    if 0:
        #look_ahead__head._nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ inner_st = locked_halfway_return
        #look_ahead__body._nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ inner_st = locked_locked_return__without_user_result
        r'''[[[
        @override
        def _nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_(sf, nonfinal_inner_st, /):
            '_nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ :: nonfinal_inner_st -> lock_mask'
            return LockMask.locked_locked
        #]]]'''
    @override
    def get_initial_inner_st(sf, /):
        'get_initial_inner_st :: inner_st'
        #get_initial_inner_st = 0
        return 0
    @override
    def moveon_nonfinal_inner_st2next_inner_st__or_raise(sf, is_on_success, nonfinal_inner_st, /):
        'moveon_nonfinal_inner_st2next_inner_st__or_raise :: is_on_success/bool -> nonfinal_inner_st -> inner_st|raise Error__moveon_nonfinal_inner_st'
        return +1 if is_on_success else -1
    @override
    def noninitial_inner_st2prev_inner_st(sf, noninitial_inner_st, /):
        'noninitial_inner_st2prev_inner_st :: noninitial_inner_st -> inner_st'
        return 0
#end-class _ISymbolExprInnerStateController__look_ahead(ISymbolExprInnerStateController):

class SymbolExprInnerStateController__look_ahead__head(_ISymbolExprInnerStateController__mixins__plain_bound_position, _ISymbolExprInnerStateController__look_ahead):
    'look_ahead/look_ahead__head'
    __slots__ = ()
    @override
    def _nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_(sf, nonfinal_inner_st, /):
        '_nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ :: nonfinal_inner_st -> lock_mask'
        #look_ahead__head._nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ inner_st = locked_halfway_return
        return LockMask.locked_halfway_return

class SymbolExprInnerStateController__look_ahead__body(_ISymbolExprInnerStateController__mixins__plain_bound_position, _ISymbolExprInnerStateController__look_ahead):
    'look_ahead/look_ahead__body'
    __slots__ = ()
    @override
    def _nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_(sf, nonfinal_inner_st, /):
        '_nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ :: nonfinal_inner_st -> lock_mask'
        #look_ahead__body._nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ inner_st = locked_locked_return__without_user_result
        return LockMask.locked_locked_return__without_user_result

class SymbolExprInnerStateController__skip(_ISymbolExprInnerStateController__mixins__plain_bound_position, _ISymbolExprInnerStateController__look_ahead):
    'look_ahead/skip'
    __slots__ = ()
    @override
    def _nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_(sf, nonfinal_inner_st, /):
        '_nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ :: nonfinal_inner_st -> lock_mask'
        #_nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ inner_st = unlocked_unlocked__without_user_result
        return LockMask.unlocked_unlocked__without_user_result





class _ISymbolExprInnerStateController__look_ahead_not(_ISymbolExprInnerStateController__mixins__step_success_exists_for_all_nonfinal_inner_st, ISymbolExprInnerStateController):
    'look_ahead_not'
    __slots__ = ()

    @override
    def is_post_pruning_inner_st(sf, inner_st, /):
        'is_post_pruning_inner_st :: inner_st -> bool'
        return sf.is_success_final_inner_st(inner_st)
    @override
    def is_inner_st(sf, inner_st, /):
        'is_inner_st :: inner_st -> bool'
        #inner_st = idx :: [-1..=2]
        if not (type(inner_st) is int and -1 <= inner_st <= 2):
            return False
        return True


    @override
    def is_fail_final_inner_st(sf, inner_st, /):
        'is_fail_final_inner_st :: inner_st -> bool'
        #is_fail_final_inner_st inner_st = inner_st == -1
        return inner_st == -1
    @override
    def is_success_final_inner_st(sf, inner_st, /):
        'is_success_final_inner_st :: inner_st -> bool'
        #is_success_final_inner_st inner_st = inner_st == +2
        return inner_st == +2
    if 0:
        #look_ahead_not__head._nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ inner_st = locked_halfway_return
        #look_ahead_not__head_body._nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ inner_st = locked_locked_return__without_user_result
        r'''[[[
        @override
        def _nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_(sf, nonfinal_inner_st, /):
            '_nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ :: nonfinal_inner_st -> lock_mask'
            return LockMask.locked_locked
        #]]]'''
    @override
    def get_initial_inner_st(sf, /):
        'get_initial_inner_st :: inner_st'
        #get_initial_inner_st = 0
        return 0
    @override
    def moveon_nonfinal_inner_st2next_inner_st__or_raise(sf, is_on_success, nonfinal_inner_st, /):
        'moveon_nonfinal_inner_st2next_inner_st__or_raise :: is_on_success/bool -> nonfinal_inner_st -> inner_st|raise Error__moveon_nonfinal_inner_st'
        #moveon_nonfinal_inner_st2next_inner_st__or_raise is_on_success 0 = if is_on_success then +1 else -1
        #moveon_nonfinal_inner_st2next_inner_st__or_raise is_on_success 1 = if is_on_success then +2 else error
        if nonfinal_inner_st == 0:
            return +1 if is_on_success else -1
        if is_on_success:
            return 2
        raise Error__moveon_nonfinal_inner_st#(nonfinal_inner_st)
    @override
    def noninitial_inner_st2prev_inner_st(sf, noninitial_inner_st, /):
        'noninitial_inner_st2prev_inner_st :: noninitial_inner_st -> inner_st'
        #noninitial_inner_st2prev_inner_st noninitial_inner_st = if noninitial_inner_st == 2 then 1 else 0
        return 1 if noninitial_inner_st==2 else 0
#end-class _ISymbolExprInnerStateController__look_ahead_not(ISymbolExprInnerStateController):

class SymbolExprInnerStateController__look_ahead_not__head(_ISymbolExprInnerStateController__mixins__plain_bound_position, _ISymbolExprInnerStateController__look_ahead_not):
    'look_ahead_not/look_ahead_not__head'
    __slots__ = ()
    @override
    def _nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_(sf, nonfinal_inner_st, /):
        '_nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ :: nonfinal_inner_st -> lock_mask'
        #look_ahead_not__head._nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ inner_st = locked_halfway_return
        return LockMask.locked_halfway_return

class SymbolExprInnerStateController__look_ahead_not__head_body(_ISymbolExprInnerStateController__mixins__plain_bound_position, _ISymbolExprInnerStateController__look_ahead_not):
    'look_ahead_not/look_ahead_not__head_body'
    __slots__ = ()
    @override
    def _nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_(sf, nonfinal_inner_st, /):
        '_nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ :: nonfinal_inner_st -> lock_mask'
        #look_ahead_not__head_body._nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_ inner_st = locked_locked_return__without_user_result
        return LockMask.locked_locked_return__without_user_result









#recognizer_combinator_utils__imports:goto
from seed.recognize.recognizer_combinator_utils import LockMaskBit
from seed.recognize.recognizer_combinator_utils import LockMask
from seed.recognize.recognizer_combinator_utils import Error__moveon_nonfinal_inner_st
from seed.recognize.recognizer_combinator_utils import ISymbolExprInnerStateController

from seed.recognize.recognizer_combinator_utils import (ISymbolExprInnerStateController
    ,is_post_pruning_inner_st
    ,is_inner_st
    ,is_fail_final_inner_st
    ,is_success_final_inner_st
    ,step_success_noninitial_inner_st2prev_lock_mask
    ,   nonfinal_inner_st2tmay_lock_mask
    ,   _nonfinal_inner_st2lock_mask__when_step_success_exists_for_all_nonfinal_inner_st_
    ,get_initial_inner_st
    ,moveon_nonfinal_inner_st2next_inner_st__or_raise
    ,   Error__moveon_nonfinal_inner_st
    ,   moveon_nonfinal_inner_st2tmay_next_inner_st
    ,noninitial_inner_st2prev_inner_st
    ,   noninitial_inner_st2is_on_success
    ,is_initial_inner_st
    ,is_final_inner_st
    ,check_inner_st
    ,check_initial_inner_st
    ,check_final_inner_st
    ,check_noninitial_inner_st
    ,check_nonfinal_inner_st
    ,check_step_success_noninitial_inner_st
    ,iter_all_inner_sts
    ,iter_all_final_inner_sts
    ,iter_all_nonfinal_inner_sts
    ,iter_all_post_pruning_inner_sts
    ,iter_all_prev_inner_sts__include
    ,validate_post_pruning_inner_sts
    )
from seed.recognize.recognizer_combinator_utils import (ISymbolExprInnerStateController
    ,SymbolExprInnerStateController__mutex
    ,SymbolExprInnerStateController__switch
    ,SymbolExprInnerStateController__catenation
    ,SymbolExprInnerStateController__token
    ,SymbolExprInnerStateController__and1s__full_match
    ,SymbolExprInnerStateController__and1s__prefix_match
    ,SymbolExprInnerStateController__andnot1s__full_match
    ,SymbolExprInnerStateController__andnot1s__prefix_match
    ,SymbolExprInnerStateController__look_ahead__head
    ,SymbolExprInnerStateController__look_ahead__body
    ,SymbolExprInnerStateController__skip
    ,SymbolExprInnerStateController__look_ahead_not__head
    ,SymbolExprInnerStateController__look_ahead_not__head_body
    )

from seed.recognize.recognizer_combinator_utils import (ISymbolExprInnerStateController
    ,is_fail_final_inner_st
    ,is_success_final_inner_st
    ,   is_fail_final_inner_st
    ,   is_success_final_inner_st
    ,   noninitial_inner_st2is_on_success
    ,       is_step_fail_noninitial_inner_st
    ,       is_step_success_noninitial_inner_st
    )


from seed.recognize.recognizer_combinator_utils import (ISymbolExprInnerStateController
,lock_mask2does_return
,   _nonfinal_inner_st2curr_using_begin_as_stop_position__when_step_success_exists_for_all_nonfinal_inner_st_
,   noninitial_inner_st2prev_using_begin_as_stop_position
,Cases4Position
,check_case4position
,   noninitial_inner_st2prev1s_inner_st_case4position_pair_as_begin_position
,   noninitial_inner_st2prev1s_inner_st_case4position_pair_as_may_end_position
,   inner_st2begin_position
,   inner_st2may_end_position
,mk_height2inner_st_layer
,   mk_inner_st2height
,   mk_height2inner_st_layer_ex
,VisitInnerStateTree__dfs
,   validate_prev1s_inner_st4position_assignment
)






from seed.recognize.recognizer_combinator_utils import LockMaskBit, bit4locked_head, bit4locked_body, bit4head_return, bit4body_return, bit4with_user_result, bit4full_match

from seed.recognize.recognizer_combinator_utils import LockMask, locked_halfway_return, unlocked_unlocked__without_user_result, locked_locked_return__without_user_result, locked_locked_return__with_user_result, locked_locked, locked_unlocked, unlocked_unlocked, locked_locked_return__with_user_result__full_match, locked_locked__full_match, locked_unlocked__full_match, unlocked_unlocked__full_match, locked_locked_return__without_user_result__full_match

from seed.recognize.recognizer_combinator_utils import *



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +IGNORE_EXCEPTION_DETAIL

#}])
