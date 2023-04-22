#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/recognizer_combinator_executor.py
to replace:view ../../python3_src/seed/recognize/recognizer_combinator.py
view ../../python3_src/seed/recognize/recognizer_combinator_utils.py
view ../../python3_src/seed/types/CuttableStream.py
view ../../python3_src/seed/helper/check/ADT.py

seed.recognize.recognizer_combinator_executor
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_combinator_executor
py -m nn_ns.app.adhoc_argparser__main__call8module   seed.recognize.recognizer_combinator_executor
from seed.recognize.recognizer_combinator_executor import ...


global_env:
    cuttable_stream
    stream<userdata>
        pruning_position
        farthest_cached_end_position
        position2userdata
            cache:
                (symbol_expr, begin_position, farthest_touched_end_position, may_end_position, Either errmsg GrammarAttribute)
            ==>> userdata = {symbol_expr:ordered_map{may_end_position:(farthest_touched_end_position, Either errmsg (success_position, GrammarAttribute))}}
                use (max_farthest_touched_end_position{< may_end_position}, may_end_position2xxx{may_end_position2xxx==None or may_end_position <= max_farthest_touched_end_position}) instead of ordered_map
            assert begin_position <= success_position <= farthest_touched_end_position <= may_end_position
            case to use cache:
                * new_end_position == old_end_position
                * new_end_position > old_end_position & farthest_touched_end_position < old_end_position
                * new_end_position < old_end_position & farthest_touched_end_position <= new_end_position

            case to avoid using cache:
                * new_end_position > old_end_position & farthest_touched_end_position == old_end_position
                * new_end_position < old_end_position & new_end_position < farthest_touched_end_position


            [old_farthest_touched_end_position < old_end_position] ==>> [max_farthest_touched_end_position == old_end_position]
            [new_end_position <= max_farthest_touched_end_position] -> [new_farthest_touched_end_position==new_end_position]
            (max_farthest_touched_end_position, may_end_position2xxx)

    stack<(symbol_expr, nonfinal_inner_st, begin_position, may_end_position)>
    acc__unlocked
    acc__post_pruning
        all (unlocked_unlocked | (inherit.locked_unlocked, is_post_pruning_inner_st))
    storage4pruning

inherit_env:
    is_without_user_result :: bool
    lock_mask :: LockMask
local_env<symbol_expr, begin_position, may_end_position>:
    farthest_touched_end_position
    * (symbol_expr, nonfinal_inner_st, begin_position, may_end_position)
        * -> next_inner_st, (symbol_expr, initial_inner_st, begin_position, may_end_position)
        * -> next_inner_st, (token_acceptor, begin_position, may_end_position)
        is_post_pruning_inner_st(next_inner_st)
    * (symbol_expr, final_inner_st, begin_position, may_end_position)

#]]]'''
__all__ = r'''
'''.split()#'''
__all__

from seed.tiny import check_type_is, check_type_le, check_callable, check_pair, null_tuple#, check_uint, snd, curry1 #, fst, snd, at, curry1, MapView, print_err
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots

from seed.tiny import BaseTuple
from seed.types.Namespace import Namespace, NamespaceSetOnce, NamespaceForbidOverwriteImplicitly, NamespaceForbidNewKey




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


from seed.recognize.recognizer_combinator_utils import (ISymbolExprInnerStateController, is_post_pruning_inner_st, is_inner_st, is_fail_inner_st, is_success_inner_st, nonfinal_inner_st2lock_mask, get_initial_inner_st, move_nonfinal_inner_st, Error__move_nonfinal_inner_st, noninitial_inner_st2prev_inner_st, noninitial_inner_st2is_on_success, is_initial_inner_st, is_final_inner_st, check_inner_st, check_initial_inner_st, check_final_inner_st, check_noninitial_inner_st, check_nonfinal_inner_st, iter_all_inner_sts, iter_all_final_inner_sts, iter_all_nonfinal_inner_sts, iter_all_post_pruning_inner_sts, iter_all_prev_inner_sts__include, validate_post_pruning_inner_sts)



from seed.recognize.recognizer_combinator_utils import (ISymbolExprInnerStateController, is_fail_inner_st, is_success_inner_st, is_fail_final_inner_st, is_success_final_inner_st, noninitial_inner_st2is_on_success, is_step_fail_inner_st, is_step_success_inner_st)


from seed.recognize.recognizer_combinator_utils import (ISymbolExprInnerStateController, lock_mask2does_return, nonfinal_inner_st2curr_using_begin_as_stop_position, noninitial_inner_st2prev_using_begin_as_stop_position, Cases4Position, check_case4position, noninitial_inner_st2prev1s_inner_st_case4position_pair_as_begin_position, noninitial_inner_st2prev1s_inner_st_case4position_pair_as_may_end_position, inner_st2begin_position, inner_st2may_end_position, mk_height2inner_st_layer, mk_inner_st2height, mk_height2inner_st_layer_ex, VisitInnerStateTree__dfs, incomplete_validate_prev1s_inner_st4position_assignment)


from seed.recognize.recognizer_combinator_utils import (ISymbolExprInnerStateController, SymbolExprInnerStateController__mutex, SymbolExprInnerStateController__switch, SymbolExprInnerStateController__catenation, SymbolExprInnerStateController__token, SymbolExprInnerStateController__and1s__full_match, SymbolExprInnerStateController__and1s__prefix_match, SymbolExprInnerStateController__andnot1s__full_match, SymbolExprInnerStateController__andnot1s__prefix_match, SymbolExprInnerStateController__look_ahead__head, SymbolExprInnerStateController__look_ahead__body, SymbolExprInnerStateController__skip, SymbolExprInnerStateController__look_ahead_not__head, SymbolExprInnerStateController__look_ahead_not__head_body)





from seed.recognize.recognizer_combinator_utils import LockMaskBit, bit4locked_head, bit4locked_body, bit4head_return, bit4body_return, bit4with_user_result, bit4full_match

from seed.recognize.recognizer_combinator_utils import LockMask, locked_halfway_return, unlocked_unlocked__without_user_result, locked_locked_return__without_user_result, locked_locked_return__with_user_result, locked_locked, locked_unlocked, unlocked_unlocked, locked_locked_return__with_user_result__full_match, locked_locked__full_match, locked_unlocked__full_match, unlocked_unlocked__full_match, locked_locked_return__without_user_result__full_match






#view ../../python3_src/seed/mapping_tools/fdefault.py
from seed.mapping_tools.fdefault import mapping_get__tmay_, mapping_get_fdefault__cased_, mapping_set_fdefault__cxxxvalue_, option2mapping_get__tmay
from seed.mapping_tools.fdefault import mapping_reversable_update__tmay
from seed.mapping_tools.fdefault import mapping_contain_, mapping_set__overwrite_or_raise__pair_, mapping_set__new_or_raise__return_, mapping_set__new_or_overwrite__pair__uniform_, mapping_set__new_or_overwrite__pair__onthen_, mapping_set__new_or_pass__cased_, mapping_set__overwrite_or_pass__may_pair_

from seed.mapping_tools.fdefault import mapping_on_key, get_fdefault, set_fdefault, getitem_fdefault, setitem_fdefault, add_new_item




from seed.tiny_.mk_fdefault import mk_fdefaultP, mk_fdefault, mk_fdefaultP_from_default, mk_fdefault_from_default, Mk_fdefaultP, Mk_fdefault, Mk_fdefault1__caller_args_at_last, Mk_fdefault1__caller_args_at_first, Mk_fdefaultP_from_default, Mk_fdefault_from_default, mk_default2value__default_at_last, mk_default2value__default_at_first, mk_tmay_from_default2value, mk_fvalue, mk_tmay_from_is_safe_fvalue, mk_tmay_from_try_fvalue, mk_tmay_from_try_fvalue_KeyError, mk_default

from seed.helper.get4may import nmay2tmay__Nothing, nmay2tmay, get4nmay__Nothing, get4nmay, fget4nmay__Nothing, fget4nmay, fgetP4nmay__Nothing_, fgetP4nmay_, fget4nmay__human, fget4nmay__Nothing__human, xget4nmay_, xget4nmay__human









from seed.helper.check.ADT import check_via_IADT_basic, check_via_IADT_advance, IADT_basic, IADT_advance

from seed.helper.check.ADT import IADT_advance__base_tuple, ADT_advance, IADT_basic__no_params, IADT_basic__dispatch__using_method_name_as_state

from seed.helper.check.ADT import ADT_basic__mapping__KV, ADT_basic__union__dispatch__using_type_le, ADT_basic__union__dispatch__using_type_eq, ADT_basic__pass_or_fail, ADT_basic__predicator

from seed.helper.check.ADT import ADT_basic__dispatch__using_method_name_as_state__no_params

#from seed.helper.check.ADT import ADT
ADT = ADT_advance
def check_via_ADT(adt, obj, /):
    check_via_IADT_advance([(adt, obj)])


TemplateName = str


_tuple = BaseTuple
class HSymbolExpr(_tuple):
    'HSymbolExpr :: * | (... -> *)'
    'symbol_expr/SymbolExpr :: *'
    __slots__ = ()
    def __init__(cls, template_name, /, *args_without_recognizer):
        check_type_le(TemplateName, TemplateName)
    @property
    def template_name(sf, /):
        return sf[0]

class TemplateSchema(_tuple):
    r'''
    template_schema
    TemplateSchema() === (*)
    TemplateSchema(A) === (A -> *)
    TemplateSchema(A, B) === (A -> B -> *)
    '''#'''
    __slots__ = ()
    def __init__(cls, /, *args):
        if not all(isinstance(x, (TemplateSchema, ADT)) for x in args): raise TypeError

class ITokenAcceptor(ABC):
    __slots__ = ()
    @abstractmethod
    def accept_token(sf, token, /):
        'token -> bool'

    #fold GrammarAttribute
    #   GrammarAttribute = token
    #cache&eval
    def eval_eresult5tmay_token(sf, tmay_token, /):
        'tmay token -> eresult'
        if tmay_token:
            [token] = tmay_token
            if accept_token(sf, token):
                user_result = sf.eval_user_result5token(token)
                return (True, user_result)
        eresult4fail = sf.eval_eresult4fail5tmay_token(tmay_token)
        return (False, eresult4fail)
    @abstractmethod
    def eval_user_result5token(sf, token, /):
        'token -> user_result'
    @abstractmethod
    def eval_eresult4fail5tmay_token(sf, tmay_token, /):
        'tmay token -> eresult4fail'
def accept_token(token_acceptor, token, /):
    'token -> bool'
    b = token_acceptor.accept_token(token)
    check_type_is(bool, b)
    return b
class TokenAcceptor__set__positive(frozenset, ITokenAcceptor):
    __slots__ = ()
    @override
    def accept_token(sf, token, /):
        'token -> bool'
        return token in sf
class TokenAcceptor__set__negative(frozenset, ITokenAcceptor):
    __slots__ = ()
    @override
    def accept_token(sf, token, /):
        'token -> bool'
        return token not in sf
class TokenAcceptor__callable(_tuple, ITokenAcceptor):
    __slots__ = ()
    def __init__(sf, b_flip, f, /):
        check_type_is(bool, b_flip)
        check_callable(f)
    @override
    def accept_token(sf, token, /):
        'token -> bool'
        (b_flip, f) = sf
        return bool(f(token)) ^ bool(b_flip)


class IRecognizerExecutor(ABC):
    #class IRecognizerExecutor__API_xxx(ABC):
    r'''[[[
    executor
    pseudo_symbol_expr = IRecognizer | symbol_expr
    symbol_expr = (template_name, *args_without_recognizer)

    IRecognizerExecutor
        TemplateName -> IRecognizerMaker
    IRecognizerMaker
        .template_schema :: TemplateSchema
        SymbolExpr -> IRecognizer
    IRecognizer
        .symbol_expr :: SymbolExpr
        .inner_st_controller :: ISymbolExprInnerStateController
        nonfinal_inner_st -> symbol_expr|token_acceptor

        #cache&eval
        inner_st -> reversed Iter (noninitial_inner_st, is_without_eresult)
        reversed[(noninitial_inner_st, is_without_eresult, may_eresult)] -> eresult

        #fold GrammarAttribute
        (acc-GrammarAttribute, tmay sub-GrammarAttribute, noninitial_inner_st) -> e_accGrammarAttribute/(acc-GrammarAttribute|eresult4fail)
        () -> e_accGrammarAttribute/(init-acc-GrammarAttribute|eresult4fail)
        (success_inner_st, final-acc-GrammarAttribute) -> eGrammarAttribute/(GrammarAttribute|eresult4fail)

    ITokenAcceptor
        token -> bool
        #fold GrammarAttribute
        #   GrammarAttribute = token
        #cache&eval
        tmay token -> eresult
            token -> user_result
            tmay token -> eresult4fail

    HSymbolExpr
        (TemplateName, *args_without_recognizer)
    SymbolExpr === HSymbolExpr{nary==0}
    TemplateName === str
    TemplateSchema
        (*args,)
        arg :: TemplateSchema | ADT
        TemplateSchema() === (*)
        TemplateSchema(A) === (A -> *)
        TemplateSchema(A, B) === (A -> B -> *)
    #]]]'''
    __slots__ = ()
    #check_hsymbol_expr_grounded
    #is_hsymbol_expr_grounded
    #calc_nary4hsymbol_expr
    #pseudo_symbol_expr2recognizer
    #validate_hsymbol_expr
    #validate_hsymbol_expr_
    #get_template_schema_ex4hsymbol_expr
    #get_template_schema_ex_ex4hsymbol_expr
    @abstractmethod
    def template_name2recognizer_maker(sf, template_name, /):
        'template_name -> recognizer_maker'
r'''[[[
    @abstractmethod
    def get_cuttable_stream(sf, /):
        '-> CuttableStream'
def get_cuttable_stream(executor, /):
    '-> CuttableStream'
    cuttable_stream = executor.get_cuttable_stream()
    check_type_le(CuttableStream, cuttable_stream)
    return cuttable_stream
#]]]'''

def check_hsymbol_expr_grounded(executor, hsymbol_expr, /):
    if not is_hsymbol_expr_grounded(executor, hsymbol_expr): raise TypeError
def is_hsymbol_expr_grounded(executor, hsymbol_expr, /):
    return calc_nary4hsymbol_expr(executor, hsymbol_expr) == 0
def calc_nary4hsymbol_expr(executor, hsymbol_expr, /):
    (recognizer_maker, template_schema4head, nary4hsymbol_expr) = get_template_schema_ex4hsymbol_expr(executor, hsymbol_expr)
    return nary4hsymbol_expr

def pseudo_symbol_expr2recognizer(executor, pseudo_symbol_expr, /):
    'pseudo_symbol_expr -> recognizer'
    if isinstance(pseudo_symbol_expr, IRecognizer):
        recognizer = pseudo_symbol_expr
    elif isinstance(pseudo_symbol_expr, tuple):
        hsymbol_expr = pseudo_symbol_expr
        validate_hsymbol_expr(executor, hsymbol_expr)
        check_hsymbol_expr_grounded(executor, hsymbol_expr)
        symbol_expr = hsymbol_expr
        [template_name, *args_without_recognizer] = symbol_expr
        recognizer_maker = template_name2recognizer_maker(executor, template_name)
        recognizer = mk_recognizer(recognizer_maker, template_name, *args_without_recognizer)
    else:
        if not isinstance(pseudo_symbol_expr, (tuple, IRecognizer)): raise TypeError
        raise logic-err
    check_type_le(IRecognizer, recognizer)
    return recognizer
def template_name2recognizer_maker(executor, template_name, /):
    check_type_le(TemplateName, template_name)
    recognizer_maker = executor.template_name2recognizer_maker(template_name)
    check_type_le(IRecognizerMaker, recognizer_maker)
    return recognizer_maker
check_type_is(TemplateSchema, TemplateSchema(1,2)[-1:])
def get_template_schema_ex4hsymbol_expr(executor, hsymbol_expr, /):
    check_type_le(HSymbolExpr, hsymbol_expr)
    recognizer_maker = template_name2recognizer_maker(executor, hsymbol_expr.template_name)
    template_schema4head = get_template_schema(recognizer_maker)
    nary4hsymbol_expr = len(template_schema4head) -(len(hsymbol_expr)-1)
    return (recognizer_maker, template_schema4head, nary4hsymbol_expr)
def get_template_schema_ex_ex4hsymbol_expr(executor, hsymbol_expr, /):
    rs1 = get_template_schema_ex4hsymbol_expr(executor, hsymbol_expr)
    (recognizer_maker, template_schema4head, nary4hsymbol_expr) = rs1
    L = (len(hsymbol_expr)-1)
    assert L >= 0
    may_template_schema4remaind = None if nary4hsymbol_expr < 0 else template_schema4head[L:]
    may_template_schema4fixed = None if nary4hsymbol_expr < 0 else template_schema4head[:L]

    rs2 = (may_template_schema4remaind, may_template_schema4fixed)
    return (rs1, rs2)
    return ((recognizer_maker, template_schema4head, nary4hsymbol_expr), (may_template_schema4remaind, may_template_schema4fixed))

def validate_hsymbol_expr(executor, hsymbol_expr, /):
    ((recognizer_maker, template_schema4head, nary4hsymbol_expr), (may_template_schema4remaind, may_template_schema4fixed)) = get_template_schema_ex_ex4hsymbol_expr(executor, hsymbol_expr)
    if not nary4hsymbol_expr >= 0: raise TypeError
    template_schema4remaind = may_template_schema4remaind
    validate_hsymbol_expr_(executor, template_schema4remaind, hsymbol_expr)
def validate_hsymbol_expr_(executor, template_schema4remaind, hsymbol_expr, /):
    ls4schema = []
    def put4schema(schema, arg, /):
        ls4schema.append((schema, arg))
    ls4adt_sf = []
    def put4adt_sf(adt_sf, arg, /):
        ls4adt_sf.append((adt_sf, arg))
    def do4schema():
        while ls4schema:
            (template_schema4remaind, hsymbol_expr) = ls4schema.pop()
            #check_type_le(HSymbolExpr, hsymbol_expr)
            ((recognizer_maker, template_schema4head, nary4hsymbol_expr), (may_template_schema4remaind, may_template_schema4fixed)) = get_template_schema_ex_ex4hsymbol_expr(executor, hsymbol_expr)
            if not nary4hsymbol_expr >= 0: raise TypeError
            if not may_template_schema4remaind == template_schema4remaind: raise TypeError
            template_schema4fixed = may_template_schema4fixed
            i = 0
            for i, adt_vs_schema in enumerate(template_schema4fixed, 1):
                arg = hsymbol_expr[i]
                if isinstance(TemplateSchema, adt_vs_schema):
                    schema = adt_vs_schema
                    put4schema(schema, arg)
                elif isinstance(adt_sf, ADT):
                    adt_sf = adt_vs_schema
                    put4adt_sf(adt_sf, arg)
                else:
                    raise logic-err
            else:
                i += 1
                assert i==len(hsymbol_expr)
    #end-def do4schema():
    def do4adt_sf():
        while ls4adt_sf:
            (adt_sf, x) = ls4adt_sf.pop()
            check_via_ADT(adt_sf, x)
    #end-def do4adt_sf():
    def main():
        check_type_le(TemplateSchema, template_schema4remaind)
        put4schema(template_schema4remaind, hsymbol_expr)
        do4schema()
        do4adt_sf()
    main()


class IRecognizerMaker(ABC):
    'recognizer_maker'
    __slots__ = ()
    @abstractmethod
    def get_template_schema(sf, /):
        '-> template_schema'
    @abstractmethod
    def mk_recognizer(sf, symbol_expr, /):
        'SymbolExpr -> IRecognizer'
def get_template_schema(recognizer_maker, /):
    '-> template_schema'
    template_schema = recognizer_maker.get_template_schema()
    check_type_le(TemplateSchema, template_schema)
    return template_schema
#def mk_recognizer(recognizer_maker, template_name, /, *args_without_recognizer):
    #check_type_le(TemplateName, template_name)
    #recognizer = recognizer_maker.mk_recognizer(template_name, *args_without_recognizer)
def mk_recognizer(recognizer_maker, symbol_expr, /):
    check_type_le(HSymbolExpr, symbol_expr)
    recognizer = recognizer_maker.mk_recognizer(symbol_expr)
    check_type_le(IRecognizer, recognizer)
    assert get_template_name(recognizer)==template_name

    return recognizer
class IRecognizer(ABC):
    'recognizer'
    __slots__ = ()
    #decompose_as_args_without_recognizer
    @abstractmethod
    def get_symbol_expr_inner_state_controller(sf, /):
        '-> ISymbolExprInnerStateController'
    @abstractmethod
    def nonfinal_inner_st2symbol_expr_or_token_acceptor(sf, nonfinal_inner_st, /):
        'nonfinal_inner_st -> symbol_expr|token_acceptor'
    @abstractmethod
    def get_symbol_expr(sf, /):
        '-> SymbolExpr/HSymbolExpr<nary=0>'
    def get_template_name(sf, /):
        '-> template_name'
        symbol_expr = get_symbol_expr(sf)
        return symbol_expr.template_name
    def get_template_args_without_recognizer(sf, /):
        '-> args_without_recognizer'
        symbol_expr = get_symbol_expr(sf)
        return (*symbol_expr[1:],)

    #cache&eval
    @abstractmethod
    def backward_iter_where_need_sub_eresult4eval_whole_eresult(sf, inner_st, /):
        'inner_st -> reversed Iter (noninitial_inner_st, is_without_eresult)'
        #default_impl4backward_iter_where_need_sub_eresult4eval_whole_eresult
    @abstractmethod
    def eval_whole_eresult(sf, backward_list_sub_eresults, /):
        'reversed[(noninitial_inner_st, is_without_eresult, may_eresult)] -> eresult'

    #fold GrammarAttribute
    @abstractmethod
    def binop4fold_GrammarAttribute(sf, acc__GrammarAttribute, tmay_sub_GrammarAttribute, noninitial_inner_st, /):
        '(acc-GrammarAttribute, tmay sub-GrammarAttribute, noninitial_inner_st) -> e_accGrammarAttribute/(acc-GrammarAttribute|eresult4fail)'
    @abstractmethod
    def init4fold_GrammarAttribute(sf, /):
        '() -> e_accGrammarAttribute/(init-acc-GrammarAttribute|eresult4fail)'
    @abstractmethod
    def final4fold_GrammarAttribute(sf, success_inner_st, final_acc__GrammarAttribute, /):
        '(success_inner_st, final-acc-GrammarAttribute) -> eGrammarAttribute/(GrammarAttribute|eresult4fail)'

def default_impl4backward_iter_where_need_sub_eresult4eval_whole_eresult(recognizer, inner_st, /):
    'inner_st -> reversed Iter (noninitial_inner_st, is_without_eresult)'
    #backward_iter_where_need_sub_eresult4eval_whole_eresult
    inner_st_controller = get_symbol_expr_inner_state_controller(recognizer)
    it = iter_all_prev_inner_sts__include(inner_st_controller, inner_st)
    inner_st = next(it)
    for prev_inner_st in it:
        noninitial_inner_st = inner_st
        is_on_success = noninitial_inner_st2is_on_success(inner_st_controller, noninitial_inner_st)
        if is_on_success:
            lock_mask = nonfinal_inner_st2lock_mask(inner_st_controller, prev_inner_st)
            is_without_eresult = _lock_mask2without_user_result(lock_mask)
        else:
            is_without_eresult = False #default to eval eresult4fail
        yield noninitial_inner_st, is_without_eresult

        inner_st = prev_inner_st

def backward_iter_where_need_sub_eresult4eval_whole_eresult(recognizer, inner_st, /):
    'inner_st -> reversed Iter (noninitial_inner_st, is_without_eresult)'
    inner_st_controller = get_symbol_expr_inner_state_controller(recognizer)
    check_inner_st(inner_st_controller, inner_st)
    it = recognizer.backward_iter_where_need_sub_eresult4eval_whole_eresult(inner_st)
    if not it is iter(it): raise logic-err

    it2 = default_impl4backward_iter_where_need_sub_eresult4eval_whole_eresult(recognizer, inner_st)
    for (noninitial_inner_st, is_without_eresult), (_noninitial_inner_st, _is_without_eresult) in zip(it, it2):
        if not noninitial_inner_st==_noninitial_inner_st: raise logic-err
        check_type_is(bool, is_without_eresult)
        if not is_without_eresult >= _is_without_eresult: raise logic-err
        yield (noninitial_inner_st, is_without_eresult)

def check_either(either, /):
    check_pair(either)
    check_type_is(bool, either[0])
check_eresult = check_either
check_triples
def eval_whole_eresult(recognizer, backward_list_sub_eresults, /):
    'reversed[(noninitial_inner_st, is_without_eresult, may_eresult)] -> eresult'
    check4eval_whole_eresult(recognizer, backward_list_sub_eresults)
    eresult = recognizer.eval_whole_eresult(backward_list_sub_eresults)
    check_eresult(eresult)
    return eresult

def check4eval_whole_eresult(recognizer, backward_list_sub_eresults, /):
    check_type_is(tuple, backward_list_sub_eresults)
    check_triples(backward_list_sub_eresults)
    for (noninitial_inner_st, is_without_eresult, may_eresult) in backward_list_sub_eresults:
        check_type_is(bool, is_without_eresult)
        if is_without_eresult:
            if not may_eresult is None: raise TypeError
        else:
            eresult = may_eresult
            check_eresult(eresult)

    inner_st_controller = get_symbol_expr_inner_state_controller(recognizer)
    if backward_list_sub_eresults:
        [(noninitial_inner_st, is_without_eresult, may_eresult)] = backward_list_sub_eresults[0]
        final_inner_st = noninitial_inner_st
        check_final_inner_st(inner_st_controller, final_inner_st)
        for (noninitial_inner_st, is_without_eresult, may_eresult), (_noninitial_inner_st, _is_without_eresult) in zip(backward_list_sub_eresults, backward_iter_where_need_sub_eresult4eval_whole_eresult(recognizer, final_inner_st)):
            if not noninitial_inner_st==_noninitial_inner_st: raise logic-err
            if not is_without_eresult is _is_without_eresult: raise logic-err

    return
def binop4fold_GrammarAttribute(recognizer, acc__GrammarAttribute, tmay_sub_GrammarAttribute, noninitial_inner_st, /):
    '(acc-GrammarAttribute, tmay sub-GrammarAttribute, noninitial_inner_st) -> e_accGrammarAttribute/(acc-GrammarAttribute|eresult4fail)'
    check_tmay(tmay_sub_GrammarAttribute)
    inner_st_controller = get_symbol_expr_inner_state_controller(recognizer)
    check_noninitial_inner_st(inner_st_controller, noninitial_inner_st)
    e_accGrammarAttribute = recognizer.binop4fold_GrammarAttribute(acc__GrammarAttribute, tmay_sub_GrammarAttribute, noninitial_inner_st)
    check_either(e_accGrammarAttribute)
    return e_accGrammarAttribute
def init4fold_GrammarAttribute(recognizer, /):
    '() -> e_accGrammarAttribute/(init-acc-GrammarAttribute|eresult4fail)'
    e_accGrammarAttribute = recognizer.init4fold_GrammarAttribute()
    check_either(e_accGrammarAttribute)
    return e_accGrammarAttribute
def final4fold_GrammarAttribute(recognizer, success_inner_st, final_acc__GrammarAttribute, /):
    '(success_inner_st, final-acc-GrammarAttribute) -> eGrammarAttribute/(GrammarAttribute|eresult4fail)'
    inner_st_controller = get_symbol_expr_inner_state_controller(recognizer)
    #check_final_inner_st(inner_st_controller, success_inner_st)
    if not is_success_inner_st(inner_st_controller, success_inner_st): raise TypeError
    eGrammarAttribute = recognizer.final4fold_GrammarAttribute(success_inner_st, final_acc__GrammarAttribute)
    check_either(eGrammarAttribute)
    return eGrammarAttribute




def get_symbol_expr_inner_state_controller(recognizer, /):
    '-> ISymbolExprInnerStateController'
    inner_st_controller = recognizer.get_symbol_expr_inner_state_controller()
    check_type_le(ISymbolExprInnerStateController, inner_st_controller)
    return inner_st_controller

def nonfinal_inner_st2symbol_expr_or_token_acceptor(recognizer, nonfinal_inner_st, /):
    'nonfinal_inner_st -> symbol_expr|token_acceptor'
    inner_st_controller = get_symbol_expr_inner_state_controller(recognizer)
    check_nonfinal_inner_st(inner_st_controller, nonfinal_inner_st)
    symbol_expr_or_token_acceptor = recognizer.nonfinal_inner_st2symbol_expr_or_token_acceptor(nonfinal_inner_st)
    if not isinstance(symbol_expr_or_token_acceptor, (HSymbolExpr, ITokenAcceptor)): raise TypeError
    return symbol_expr_or_token_acceptor
    #check_type_le(HSymbolExpr, symbol_expr)
    #return symbol_expr
def get_symbol_expr(recognizer, /):
    '-> SymbolExpr/HSymbolExpr<nary=0>'
    symbol_expr = recognizer.get_symbol_expr()
    check_type_le(HSymbolExpr, symbol_expr)
    return symbol_expr
def get_template_name(recognizer, /):
    '-> template_name'
    template_name = recognizer.get_template_name()
    check_type_le(TemplateName, template_name)
    return template_name
def get_template_args_without_recognizer(recognizer, /):
    '-> args_without_recognizer'
    args_without_recognizer = recognizer.get_template_args_without_recognizer()
    check_type_is(tuple, args_without_recognizer)
    return args_without_recognizer

def decompose_as_args_without_recognizer(recognizer, /):
    '-> (template_name, *args_without_recognizer)'
    template_name = get_template_name(recognizer)
    args_without_recognizer = get_template_args_without_recognizer(recognizer)
    return (template_name, *args_without_recognizer)



def position_eq(lhs_position, rhs_position, /):
    return lhs_position.as_int() == rhs_position.as_int()
def position_lt(lhs_position, rhs_position, /):
    return lhs_position < rhs_position
def position_le(lhs_position, rhs_position, /):
    return lhs_position <= rhs_position
def position_le_ex(lhs_position, may_rhs_position, /):
    if may_rhs_position is None:
        return True
    rhs_position = may_rhs_position
    return lhs_position <= rhs_position

#acc__unlocked :: LockMaskBit not LockMask
locked_unlocked4acc = bit4locked_head
locked_locked4acc = bit4locked_head|bit4locked_body
unlocked_unlocked4acc = bit4locked_head^bit4locked_head
assert unlocked_unlocked4acc == 0
_all__acc__unlocked = frozenset([locked_locked4acc, locked_unlocked4acc, unlocked_unlocked4acc])

def _lock_mask2without_user_result(lock_mask, /):
    check_type_is(LockMask, lock_mask)
    acc__without_user_result = not (lock_mask.value&bit4with_user_result)
    return acc__without_user_result
def _lock_mask2acc(lock_mask, /):
    check_type_is(LockMask, lock_mask)
    if not (lock_mask.value & bit4locked_head):
            acc__unlocked = unlocked_unlocked4acc
    elif (lock_mask.value & bit4head_return):
        #if (lock_mask.value & bit4locked_head):
            acc__unlocked = locked_locked4acc
    else:
        acc__unlocked = (lock_mask.value & locked_locked4acc)
    check_type_is(LockMaskBit, acc__unlocked)
    assert acc__unlocked in _all__acc__unlocked
    return acc__unlocked
def recognize(executor, lock_mask4main, symbol_expr4main, userdata_ops, cuttable_stream, begin_position, may_end_position, /):
    check_type_is(LockMask, lock_mask4main)
    check_type_le(HSymbolExpr, symbol_expr4main)
    check_type_le(IUserDataOps4Recognizer, userdata_ops)
    check_type_le(CuttableStream, cuttable_stream)
    if not _g_mk_userdata == cuttable_stream.get_mk_userdata(): return TypeError
        #Mkr4XUserData4CuttableStream(NamespaceSetOnce)
        #xuserdata.position
        #xuserdata.tmay_token
        #xuserdata.payload
        #xuserdata.payload.symbol_expr2final
        #   {symbol_expr:ordered_map{may_end_position:(may final_info, recognizer, mid_info)}}
        #   final_info = (farthest_touched_end_position, stop_position, final_inner_st, recognizer, eGrammarAttribute, tmay eresult) #tmay eresult can be overwrite once
        #   mid_info = {noninitial_inner_st:(begin_position, sub-symbol_expr, may_end_position, tmay sub-GrammarAttribute, e_accGrammarAttribute, may sub-final_info)}
    def get_or_eval(begin_position, symbol_expr, may_end_position, /):
        xuserdata = cuttable_stream.get_xuserdata__position(begin_position)
        ns = xuserdata.payload
        (_, xxx) = mapping_set_fdefault__cxxxvalue_(ns, symbol_expr, 0, mk_xxx, try_vs_Nothing_vs_in=True)
            # (max_farthest_touched_end_position{< may_end_position}, may_end_position2xxx{may_end_position2xxx==None or may_end_position <= max_farthest_touched_end_position})
        _may_end_position = may_end_position
        if xxx.may_max_farthest_touched_end_position is not None:
            max_farthest_touched_end_position = xxx.may_max_farthest_touched_end_position
            if position_le_ex(max_farthest_touched_end_position, _may_end_position):
                _may_end_position = max_farthest_touched_end_position
        _may_end_position
        if _may_end_position in xxx.may_end_position2eresult_ex:
            eresult_ex = xxx.may_end_position2eresult_ex[_may_end_position]
                #cache
            return True, eresult_ex
        eresult_ex = yield _eval(begin_position, symbol_expr, _may_end_position, xxx)
        if _may_end_position is None or position_lt(eresult_ex.farthest_touched_end_position, _may_end_position):
            assert xxx.may_max_farthest_touched_end_position is None
            max_farthest_touched_end_position = eresult_ex.farthest_touched_end_position
            xxx.may_max_farthest_touched_end_position = max_farthest_touched_end_position
            _may_end_position = max_farthest_touched_end_position
        xxx.may_end_position2eresult_ex[_may_end_position] = eresult_ex
            #cache
        return True, eresult_ex
    def _eval(begin_position, symbol_expr, may_end_position, xxx, /):
        xxx.backward_list_sub_eresults
        backward_list_sub_eresults
        ISymbolExprInnerStateController 添加:noninitial_nonfinal_inner_st2tmay_noninitial_inner_st4limit_end_position
            noninitial_inner_st in iter_all_prev_inner_sts__include(noninitial_nonfinal_inner_st)
            is_step_success_inner_st(noninitial_inner_st)
            prev_inner_st := noninitial_inner_st2prev_inner_st(noninitial_inner_st)
            using (prev_inner_st~noninitial_inner_st).stop_position as (noninitial_nonfinal_inner_st~?).may_end_position for and1s/andnot1s

        ... ...
        ... ...

    #lock_mask4main = unlocked_unlocked__without_user_result if is_without_user_result else unlocked_unlocked
    #cuttable_stream = get_cuttable_stream(executor)
    #p0 = cuttable_stream.tell()
    p0 = begin_position
    mend = may_end_position
    if not position_le_ex(p0, mend): raise ValueError
    cuttable_stream.seek__position(p0)
    #cuttable_stream.cut__relative(0)

    acc__without_user_result4main = False
    acc__without_user_result4main |= _lock_mask2without_user_result(lock_mask4main)
    acc__unlocked4main = unlocked_unlocked4acc
    acc__unlocked4main |= __lock_mask2acc(lock_mask4main)
        # [locked_locked4acc, locked_unlocked4acc, unlocked_unlocked4acc]
        # not:{unlocked_unlocked, locked_unlocked, locked_locked}
    assert acc__unlocked4main in _all__acc__unlocked

    stack4eresult = []
    stack = []
        #[((len_stack4eresult, lock_mask5above, acc__without_user_result5above, acc__unlocked5above), (begin_position, recognizer, inner_st, may_end_position), (inner_st_is_initial, inner_st_is_final, inner_st_is_post_pruning, may_data4nonfinal))]
        ###
        #[(begin_position, recognizer, nonfinal_inner_st, may_end_position)]
        # except last: may be final_inner_st
    def xput(lock_mask5above, acc__without_user_result5above, acc__unlocked5above, begin_position, pseudo_symbol_expr, tmay_inner_st, may_end_position, /):
        assert acc__unlocked5above in _all__acc__unlocked
        assert position_le_ex(begin_position, may_end_position)

        recognizer = pseudo_symbol_expr2recognizer(executor, pseudo_symbol_expr2recognizer)
        inner_st_controller = get_symbol_expr_inner_state_controller(recognizer)
        if not tmay_inner_st:
            [] = tmay_inner_st
            inner_st = get_initial_inner_st(inner_st_controller)
        else:
            [inner_st] = tmay_inner_st
        inner_st


        inner_st_is_initial = is_initial_inner_st(inner_st_controller, inner_st)
        inner_st_is_final = is_final_inner_st(inner_st_controller, inner_st)
        if not inner_st_is_final:
            nonfinal_inner_st = inner_st
            lock_mask4sub = nonfinal_inner_st2lock_mask(inner_st_controller, inner_st)
            _acc__unlocked = acc__unlocked5above
            if acc__unlocked5above == locked_unlocked4acc:
                if is_post_pruning_inner_st(inner_st_controller, inner_st):
                    _acc__unlocked = unlocked_unlocked4acc
                else:
                    _acc__unlocked = locked_locked4acc

            _acc__unlocked
            assert _acc__unlocked in _all__acc__unlocked

            try:
                next_inner_st4success = move_nonfinal_inner_st(inner_st_controller, True, inner_st)
            except Error__move_nonfinal_inner_st:
                may_data4success = None
            else:
                if acc__unlocked5above == locked_unlocked4acc and _acc__unlocked == locked_locked4acc:
                    if is_post_pruning_inner_st(inner_st_controller, next_inner_st4success):
                        _acc__unlocked = locked_unlocked4acc
                may_data4success = (next_inner_st4success,)
            may_data4success, _acc__unlocked
            assert _acc__unlocked in _all__acc__unlocked
            _acc__unlocked,lock_mask4sub
            acc__unlocked4sub = _acc__unlocked | _lock_mask2acc(lock_mask4sub)
            assert acc__unlocked4sub in _all__acc__unlocked
            acc__without_user_result4sub = acc__unlocked5above or _lock_mask2without_user_result(lock_mask4sub)

            may_data4nonfinal = (lock_mask4sub, acc__without_user_result4sub, acc__unlocked4sub, may_data4success)
        else:
            may_data4nonfinal = None
        may_data4nonfinal
        inner_st_is_post_pruning = is_post_pruning_inner_st(inner_st_controller, inner_st)
        stack.append(((len(stack4eresult), lock_mask5above, acc__without_user_result5above, acc__unlocked5above), (begin_position, recognizer, inner_st, may_end_position), (inner_st_is_initial, inner_st_is_final, inner_st_is_post_pruning, may_data4nonfinal)))

    #update_farthest_touched_end_position
    handle_success
    #handle_success(begin_position, recognizer, nonfinal_inner_st, success_position, farthest_touched_end_position, may_end_position, token)
    handle_fail
    #handle_fail(begin_position, recognizer, nonfinal_inner_st, farthest_touched_end_position, may_end_position, errmsg)
    #farthest_touched_end_position = p0
    def put_eresult4token4fail__no_token(token_acceptor, begin_position, may_end_position, errmsg, /):
        farthest_touched_end_position = begin_position
        put_eresult4token4fail(token_acceptor, begin_position, farthest_touched_end_position, may_end_position, errmsg)
    def put_eresult4token4fail(token_acceptor, begin_position, farthest_touched_end_position, may_end_position, errmsg, /):
        stop_position = begin_position
        is_success = False
        errmsg_or_token = errmsg
        eresult1 = EResult4token__part1(
        begin_position
        ,token_acceptor
        ,stop_position
        ,farthest_touched_end_position
        ,may_end_position
        ,is_success
        ,errmsg_or_token
        )
        stack4eresult.append(eresult1)
    def put_eresult4token4success(token_acceptor, begin_position, farthest_touched_end_position, may_end_position, token, /):
        stop_position = farthest_touched_end_position
        is_success = True
        errmsg_or_token = token
        eresult1 = EResult4token__part1(
        begin_position
        ,token_acceptor
        ,stop_position
        ,farthest_touched_end_position
        ,may_end_position
        ,is_success
        ,errmsg_or_token
        )
        stack4eresult.append(eresult1)


    def handle_token_acceptor(token_acceptor, begin_position, may_end_position, /):
        #cuttable_stream.seek__position(begin_position)
        assert position_eq(begin_position, cuttable_stream.tell())
        #if may_data4success is None:
        assert position_le_ex(begin_position, may_end_position)
        if not may_end_position is None:
            if position_eq(begin_position, may_end_position):
                errmsg = ('limit-bound', begin_position)
                #handle_fail(begin_position, recognizer, nonfinal_inner_st, farthest_touched_end_position, may_end_position, errmsg)
                put_eresult4token4fail__no_token(token_acceptor, begin_position, may_end_position, errmsg)
                return False
        tmay_userdata = cuttable_stream.read_le(1)
        if not tmay_userdata:
            #eof
            errmsg = ('eof', begin_position)
            #handle_fail(begin_position, recognizer, nonfinal_inner_st, farthest_touched_end_position, may_end_position, errmsg)
            put_eresult4token4fail__no_token(token_acceptor, begin_position, may_end_position, errmsg)
            return False
        #success_position = cuttable_stream.tell()
        #farthest_touched_end_position = update_farthest_touched_end_position(success_position)
        farthest_touched_end_position = cuttable_stream.tell()
        [userdata] = tmay_userdata
        token = userdata_ops.get_token(userdata)
        if not accept_token(token_acceptor, token):
            errmsg = mk_errmsg(token_acceptor, begin_position, token)
            #handle_fail(begin_position, recognizer, nonfinal_inner_st, farthest_touched_end_position, may_end_position, errmsg)
            put_eresult4token4fail(token_acceptor, begin_position, farthest_touched_end_position, may_end_position, errmsg)
            return False
        #handle_success(begin_position, recognizer, nonfinal_inner_st, success_position, farthest_touched_end_position, may_end_position, token)
        put_eresult4token4success(token_acceptor, begin_position, farthest_touched_end_position, may_end_position, token)
        return True
    #end-def handle_token_acceptor(token_acceptor, begin_position, may_end_position, /):
    def move_last_elem__eresult_pushed():
        ((len_stack4eresult, lock_mask5above, acc__without_user_result5above, acc__unlocked5above), (begin_position, recognizer, inner_st, may_end_position), (inner_st_is_initial, inner_st_is_final, inner_st_is_post_pruning, may_data4nonfinal)) = stack[-1]
        if not len(stack4eresult) == 1+len_stack4eresult: raise logic-err
        eresult1 = stack4eresult[-1]
        is_success = eresult1.is_success

        inner_st_controller = get_symbol_expr_inner_state_controller(recognizer)
        next_inner_st = move_nonfinal_inner_st(inner_st_controller, is_success, inner_st)

        next_begin_position = begin_position
        if is_success:
            (lock_mask4sub, acc__unlocked4sub, may_data4success) = may_data4nonfinal
            if not ((lock_mask4sub.value&bit4body_return) or (lock_mask4sub.value&bit4head_return)):
                #not return then move
                next_begin_position = eresult1.stop_position

        xput(lock_mask5above, acc__without_user_result5above, acc__unlocked5above, next_begin_position, recognizer, (next_inner_st,), may_end_position)


    def handle_final(recognizer, final_inner_st, stop_position, /):
        inner_st_controller = get_symbol_expr_inner_state_controller(recognizer)
        initial_inner_st = get_initial_inner_st(inner_st_controller)
        farthest_touched_end_position = stop_position
        is_success = is_success_inner_st(inner_st_controller, final_inner_st)
        while 1:
            ((len_stack4eresult, lock_mask5above, acc__without_user_result5above, acc__unlocked5above), (begin_position, recognizer, inner_st, may_end_position), (inner_st_is_initial, inner_st_is_final, inner_st_is_post_pruning, may_data4nonfinal)) = stack.pop()
            if inner_st_is_initial:
                break
            eresult4sub = stack4eresult.pop()
            farthest_touched_end_position = max(farthest_touched_end_position, eresult4sub.farthest_touched_end_position)
        #end-while 1:

        if not is_success:
            errmsg = mk_errmsg(recognizer, begin_position, farthest_touched_end_position, final_inner_st)
            may_errmsg = errmsg
        else:
            may_errmsg = None

        eresult1 = EResult__part1(
        initial_inner_st
        ,begin_position
        ,recognizer
        ,stop_position
        ,farthest_touched_end_position
        ,may_end_position
        ,final_inner_st
        ,is_success
        ,may_errmsg
        )
        stack4eresult.append(eresult1)
        #success_position
        #handle_success(begin_position, recognizer, nonfinal_inner_st, success_position, farthest_touched_end_position, may_end_position, token)
        ... ...
        handle_final when begin_position < prev_pruning_position ==>> save_
        return
    #end-def handle_final(recognizer, final_inner_st, stop_position, /):
    tmay_prev_pruning_position = [Position(p0.as_int()-1, None)]
    def pruning_position(begin_position, /):
        [prev_pruning_position] = tmay_prev_pruning_position
        assert position_le(prev_pruning_position, begin_position)
        #if not position_lt(begin_position, prev_pruning_position):
        if position_eq(begin_position, prev_pruning_position):
            # 『==』
            return
        assert position_lt(prev_pruning_position, begin_position)
        after_is_initial_inner_st = True
        the_pruning_position = begin_position
        for i in reversed(range(len(stack))):
            (_, (begin_position, *_), (inner_st_is_initial, *_)) = stack[i]
            assert position_le(begin_position, the_pruning_position)

            if after_is_initial_inner_st:
                after_is_initial_inner_st = inner_st_is_initial
                continue
            if position_lt(begin_position, prev_pruning_position):
                break
            if position_lt(begin_position, the_pruning_position):
                save_(i)
            after_is_initial_inner_st = inner_st_is_initial
        #end-for i in reversed(range(len(stack))):
        prev_pruning_position = the_pruning_position
        tmay_prev_pruning_position[0] = prev_pruning_position
        cuttable_stream.cut__position(the_pruning_position)
        return
    def save_(idx4stack, /):
        i = idx4stack
        ((len_stack4eresult, lock_mask5above, acc__without_user_result5above, acc__unlocked5above), (begin_position, recognizer, inner_st, may_end_position), (inner_st_is_initial, inner_st_is_final, inner_st_is_post_pruning, may_data4nonfinal)) = stack[i]
        assert i+1 < len(stack)
        assert stack[1+i][2][0] is False #not inner_st_is_initial
        eresult1 = stack4eresult[len_stack4eresult]
        eresult1.recognizer/token_acceptor
        GrammarAttribute
        acc__without_user_result5above
        ... ...
        handle_final when begin_position < prev_pruning_position ==>> save_
        return
    #end-def save_(idx4stack, /):

    xput(lock_mask4main, acc__without_user_result4main, acc__unlocked4main, p0, symbol_expr4main, (), mend)
    while stack:
        ((len_stack4eresult, lock_mask5above, acc__without_user_result5above, acc__unlocked5above), (begin_position, recognizer, inner_st, may_end_position), (inner_st_is_initial, inner_st_is_final, inner_st_is_post_pruning, may_data4nonfinal)) = stack[-1]
        if acc__unlocked5above == unlocked_unlocked4acc:
            pruning_position(begin_position)
        elif inner_st_is_final:
            if not acc__unlocked5above == locked_locked4acc:
                pruning_position(begin_position)
        ###
        if inner_st_is_final:
            final_inner_st = inner_st
            stop_position = begin_position
            handle_final(recognizer, final_inner_st, stop_position)
            if stack:
                move_last_elem__eresult_pushed()
            continue
        nonfinal_inner_st = inner_st
        (lock_mask4sub, acc__without_user_result4sub, acc__unlocked4sub, may_data4success) = may_data4nonfinal
        symbol_expr_or_token_acceptor = nonfinal_inner_st2symbol_expr_or_token_acceptor(recognizer, nonfinal_inner_st)
        if isinstance(symbol_expr_or_token_acceptor, ITokenAcceptor):
            token_acceptor = symbol_expr_or_token_acceptor
            handle_token_acceptor(token_acceptor, begin_position, may_end_position)
            move_last_elem__eresult_pushed()
            continue

        symbol_expr4sub = symbol_expr_or_token_acceptor
        xput(lock_mask4sub, acc__without_user_result4sub, acc__unlocked4sub, begin_position, symbol_expr4sub, (), may_end_position)


XUserData4CuttableStream
_g_mk_userdata = Mkr4XUserData4CuttableStream(NamespaceSetOnce)
#stream = mk_CuttableStream_from_ground_level_tokens(mk_userdata, -3, range(6, 16))
#mk_userdata is stream.get_mk_userdata() == Mkr4XUserData4CuttableStream(NamespaceSetOnce)
class IUserDataOps4Recognizer(ABC):
    __slots__ = ()
    @abstractmethod
    def get_token(sf, userdata, /):
        '-> token'

from collections import namedtuple
#class EResult__part1:
_nms4EResult__part1 = r'''
    initial_inner_st
    begin_position
    recognizer
    stop_position
    farthest_touched_end_position
    may_end_position
    final_inner_st
    is_success
    may_errmsg
    '''#'''
    #is_success:used in move_last_elem__eresult_pushed
    #farthest_touched_end_position:used in handle_final
EResult__part1 = namedtuple('EResult__part1', _nms4EResult__part1)
_nms4EResult4token__part1 = r'''
    begin_position
    token_acceptor
    stop_position
    farthest_touched_end_position
    may_end_position
    is_success
    errmsg_or_token
    '''#'''
EResult4token__part1 = namedtuple('EResult4token__part1', _nms4EResult4token__part1)

class EResult4token__part1(EResult4token__part1):
    @property
    def may_errmsg(sf, /):
        return None if sf.is_success else sf.errmsg_or_token

class EResult4ok:
    __slots__ = r'''
    initial_inner_st
    begin_position
    recognizer
    stop_position
    farthest_touched_end_position
    may_end_position
    final_inner_st
    '''.split()#'''





if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +IGNORE_EXCEPTION_DETAIL

