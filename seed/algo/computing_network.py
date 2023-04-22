#__all__:goto
r'''[[[
e ../../python3_src/seed/algo/computing_network.py
view ../../python3_src/seed/iters/generator_iterator_capturer.py

seed.algo.computing_network
py -m nn_ns.app.debug_cmd seed.algo.computing_network
py -m seed.algo.computing_network
py -m nn_ns.app.adhoc_argparser__main__call8module seed.algo.computing_network

py -m seed.algo.computing_network >  ~/my_tmp/out4py/seed.algo.computing_network-debug.txt
view ../../../tmp/out4py/seed.algo.computing_network-debug.txt



from seed.algo.computing_network import IQuestionEnv
from seed.algo.computing_network import IQuestionEnv__handler_dispatcher, IHandler4IQuestionEnv__handler_dispatcher
from seed.algo.computing_network import ActionKind, computing_network_exec, ComputingNetworkExecutor
from seed.algo.computing_network import solve4CFG__min_len, solve4CFG__head_set






question-example:
    question_env:grammar-CFG:
        [symbol = lsymbol | rsymbol]
        [len(rsymbol) == 1]
        [lsymbol = parallel | sequential]
        [lsymbol2symbols :: lsymbol -> [symbol]]

    ######################
    ######################
    question__min_len:
        [lsymbol2min_len :: lsymbol -> may_uint]

    question__head_set:
        [lsymbol2rsymbols :: lsymbol -> {rsymbol}]

    question__follow_set:
        [lsymbol2rsymbols :: lsymbol -> {rsymbol}]

    ######################
    ######################
    question__min_len:
        on_start: min_len = +oo/None/()
            lsymbol.tmay_answer = ()
            rsymbol.tmay_answer = (1,)
        on_news:
            sequential: until all then sum
            parallel:min(old,new)

    ######################
    question__head_set:
        #depend on question__min_len
        on_start:
            lsymbol.tmay_answer = ({},)
            rsymbol.tmay_answer = ({self},)
        on_news:
            sequential: if front nullable then union
            parallel: union

    ######################
    xxx question__follow_set:
        #depend on question__head_set
        on_start:
            lsymbol.tmay_answer = ({},)
                yield actions about others #not sf
            rsymbol.tmay_answer = ({},)
        on_news:
            sequential:??? fail
            parallel: ??? fail
            ??????????????????????
            ??????????????????????

    ######################
    ######################
#]]]'''


#QuestionKind
#IQuestion
__all__ = r'''
IQuestionEnv

IHandler4IQuestionEnv__handler_dispatcher
Handler4IQuestionEnv__handler_dispatcher__fix_answer

question2handler6qenv
IQuestionEnv__handler_dispatcher
IQuestionEnv__named_handler_dispatcher
IQuestionEnv__named_handler_dispatcher__using_name_payload8qstn
IQuestionEnv__named_handler_dispatcher__using_dict4register_handler
IQuestionEnv__named_handler_dispatcher__using_dict4register_handler__using_name_payload8qstn

IHandler4IQuestionEnv__named_handler_dispatcher

ActionKind
InnerActionKind
VtxSt4Question
get_newest
PDEdgeSt4SubQuestion
computing_network_exec
ComputingNetworkExecutor

CFG_SymbolKind
check4setting4CFG
IQuestionEnv4CFG
prepare_args4mk_IQuestionEnv4CFG
check_result4CFG__head_set
check_result4CFG__min_len
mk_QuestionEnv4CFG

QuestionEnv4CFG__min_len
Handler4QuestionEnv4CFG__min_len__sequential
Handler4QuestionEnv4CFG__min_len__arbitrary
Handler4QuestionEnv4CFG__min_len__terminal
solve4CFG__min_len
solve4CFG__min_len__qenv

QuestionEnv4CFG__head_set
Handler4QuestionEnv4CFG__head_set__sequential
Handler4QuestionEnv4CFG__head_set__arbitrary
Handler4QuestionEnv4CFG__head_set__terminal
solve4CFG__head_set
solve4CFG__head_set__qenv

'''.split()#'''
__all__

from enum import Enum
from collections.abc import Hashable, Mapping, Sequence

from seed.tiny import mk_tuple, fmap4dict_value
from seed.debug.expectError import expectError
from seed.tiny_.singleton import mk_SingletonClass, mk_existing_type_singleton

from seed.iters.generator_iterator_capturer import GeneratorIteratorCapturer
from seed.tiny import mk_tuple, mk_frozenset, null_frozenset, null_tuple, null_iter

from seed.tiny import check_uint
from seed.tiny_.check import check_tmay, check_type_is, check_type_le, check_pair, check_callable  #, , check_uint, check_imay
from seed.tiny_.mk_fdefault import mk_default
#def mk_default(imay_xdefault_rank, xdefault, /,*args4xdefault):
from seed.graph.DGraph4GrowingOnly import DGraph4GrowingOnly
from seed.helper.repr_input import repr_helper_ex
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots

r"""[[[
class IHQuestion(Hashable):
    r'''
    question :: (IHQuestion,arg) <: Hashable
    '''#'''
    def iter_subquestions(sf, arg, /):
        'question -> GenIter state subquestion #if no subquestion then update_state_and_tmay_answer callonce will get final answer'
    #def answer_or_iter_subquestions(sf, arg, /):
        'question -> (False,tmay_answer)|(True,subquestions)'
    def update_state_and_tmay_answer(sf, arg, subquestions_with_same_no_answer, subquestion2same_answer, subquestion2diff_tmay_answers, old_state, tmay_old_answer, /):
        'question -> {subquestion} -> {subquestion:same_answer} -> {subquestion:(tmay_old_answer, tmay_new_answer){=!=}} -> old_state -> tmay_old_answer -> (new_state, tmay_new_answer)'


def question2state_and_subquestions_pair(iter_subquestions, question, /):
    g = GeneratorIteratorCapturer(iter_subquestions(question))
    subquestions = [*g]
    state = g.get_tmay_result()
    return (state, subquestions)
    ##############################
    subquestions = []
    it = iter(iter_subquestions(question))
    try:
        while 1:
            subquestions.append(next(it))
    except StopIteration as e:
        state = e.value
        return (state, subquestions)
"""#"""

if 0:
    QuestionKind = Enum('QuestionKind', r'''
sequential
arbitrary
unifiable
'''#'''
, module=__name__
, qualname='QuestionKind'
)
r'''
sequential
    block
    all/and
    accumulative
        foldable
        sum
arbitrary
    parallel
    shortcut
    short-circuit
    any/or
    ==>> .vtx2refcount
    ==>> ???Question <: Awaitable???
unifiable
    union
    min/max
    ==>> dynamic-compute/update, recursively-depend
'''#'''

class IQuestion(Hashable):
    r'''
Question <: Hashable; but st neednot

tag :: tuple<Hashable>
    external attached param


st normally be mutable
    st be the mutable part of obj
    question be the immutable part of obj

answer will be shared, should be immutable or take care not to modify it emplace

msg:
    * info news:
        # [bool(tmay_new_tmay_whole_answer)]
        info parent from child new_tmay_child_answer

action:
    * ask who tag  whom
        question ask subquestion
            vtx2refcount[node2vtx[subquestion]] += 1

    * cancel who tag whom
            vtx2refcount[node2vtx[subquestion]] -= 1
            if refcount be 0:
                donot remove but stop run
    * cancel all children
        refcount -= 1

[[not tmay_new_tmay_whole_answer] <-> [new_tmay_whole_answer == old_tmay_whole_answer]]
    [neednot replace old_tmay_whole_answer by new_tmay_whole_answer and info parent_questions]


#vtx_st4question
vtx_st<question>:
    refcount :: uint #== sum(not income_pdedge_st.cancelled)
    st
    old_tmay_answer
    tmay_new_tmay_answer
        #two ==>> new_tmay_answer
        #   when subquestion_has_news==True
        #   see:get_newest

    may_actions #only for init from turnon_vtx
    # actions put into deque/stack
    # news :: {vtx4subquestion}
    #   move to pdedge_st

#pdedge_st4subquestion
pdedge_st<parent_question, tag, subquestion>:
    cancelled :: bool
        # vivi refcount

    subquestion_has_news :: bool
    old_tmay_sub_answer





    '''#'''
    #xxx def get_question_kind6qstn(sf, /):
    #    '-> QuestionKind'
    @abstractmethod
    def on_start6qstn(sf, /):
        '-> (st, tmay_whole_answer, actions)'
    @abstractmethod
    def on_news6qstn(sf, st, old_tmay_whole_answer, tag, subquestion, old_tmay_sub_answer, new_tmay_sub_answer, /):
        '-> (tmay_st, tmay_new_tmay_whole_answer, actions)'
    @abstractmethod
    def on_stable6qstn(sf, st, old_tmay_whole_answer, /):
        '-> tmay_new_tmay_whole_answer'

class IQuestionEnv(ABC):
    #question_env
    __slots__ = ()
    @abstractmethod
    def ask6qenv(sf, /):
        '-> Iter question'
    @abstractmethod
    def on_start6qenv(sf, question, /):
        '-> (st, tmay_whole_answer, actions)'
    @abstractmethod
    def on_news6qenv(sf, question, st, old_tmay_whole_answer, tag, subquestion, old_tmay_sub_answer, new_tmay_sub_answer, /):
        '-> (tmay_st, tmay_new_tmay_whole_answer, actions)'
    @abstractmethod
    def on_stable6qenv(sf, question, st, old_tmay_whole_answer, /):
        '-> tmay_new_tmay_whole_answer'
class IHandler4IQuestionEnv__handler_dispatcher(Hashable, ABC):
    #handler4question_env
    'MUST_BE immutable; on_start6hdlr4qenv create st<handler> may be mutable__st'
    __slots__ = ()
    @abstractmethod
    def check_question6hdlr4qenv(sf, question_env, question, /):
        '-> None'
    @abstractmethod
    def on_start6hdlr4qenv(sf, question_env, question, /):
        '-> (st, tmay_whole_answer, actions)'
    @abstractmethod
    def on_news6hdlr4qenv(sf, question_env, question, st, old_tmay_whole_answer, tag, subquestion, old_tmay_sub_answer, new_tmay_sub_answer, /):
        '-> (tmay_st, tmay_new_tmay_whole_answer, actions)'
    @abstractmethod
    def on_stable6hdlr4qenv(sf, question_env, question, st, old_tmay_whole_answer, /):
        '-> tmay_new_tmay_whole_answer'
class Handler4IQuestionEnv__handler_dispatcher__fix_answer(IHandler4IQuestionEnv__handler_dispatcher):
    #handler4question_env
    'MUST_BE immutable; on_start6hdlr4qenv create st<handler> may be mutable__st'
    __slots__ = '_tm _mck'.split()
    def __init__(sf, tmay_whole_answer, may_check4qstn=None, /):
        if may_check4qstn is not None:
            check_callable(may_check4qstn)
        check_tmay(tmay_whole_answer)
        sf._tm = tmay_whole_answer
        sf._mck = may_check4qstn
    @override
    def check_question6hdlr4qenv(sf, question_env, question, /):
        '-> None'
        if sf._mck is not None:
            sf._mck(question_env, question)
    @override
    def on_start6hdlr4qenv(sf, question_env, question, /):
        '-> (st, tmay_whole_answer, actions)'
        return None, sf._tm, null_iter
    @override
    def on_news6hdlr4qenv(sf, question_env, question, st, old_tmay_whole_answer, tag, subquestion, old_tmay_sub_answer, new_tmay_sub_answer, /):
        '-> (tmay_st, tmay_new_tmay_whole_answer, actions)'
        raise logic-err
    @override
    def on_stable6hdlr4qenv(sf, question_env, question, st, old_tmay_whole_answer, /):
        '-> tmay_new_tmay_whole_answer'
        return null_tuple


def question2handler6qenv(handler_dispatcherer, question, /):
    check_type_le(IQuestionEnv__handler_dispatcher, handler_dispatcherer)
    handler = handler_dispatcherer.question2handler6qenv(question)
    handler.check_question6hdlr4qenv(handler_dispatcherer, question)
    return handler

class IQuestionEnv__handler_dispatcher(IQuestionEnv):
    #question_env
    __slots__ = ()
    @abstractmethod
    def question2handler6qenv(sf, question, /):
        '-> IHandler4IQuestionEnv__handler_dispatcher'
    @override
    def on_start6qenv(sf, question, /):
        '-> (st, tmay_whole_answer, actions)'
        handler = question2handler6qenv(sf, question)
        (st, tmay_whole_answer, actions) = handler.on_start6hdlr4qenv(sf, question)
        return (st, tmay_whole_answer, actions)
    @override
    def on_news6qenv(sf, question, st, old_tmay_whole_answer, tag, subquestion, old_tmay_sub_answer, new_tmay_sub_answer, /):
        '-> (tmay_st, tmay_new_tmay_whole_answer, actions)'
        handler = question2handler6qenv(sf, question)
        (tmay_st, tmay_new_tmay_whole_answer, actions) = handler.on_news6hdlr4qenv(sf, question, st, old_tmay_whole_answer, tag, subquestion, old_tmay_sub_answer, new_tmay_sub_answer)
        return (tmay_st, tmay_new_tmay_whole_answer, actions)
    @override
    def on_stable6qenv(sf, question, st, old_tmay_whole_answer, /):
        '-> tmay_new_tmay_whole_answer'
        handler = question2handler6qenv(sf, question)
        tmay_new_tmay_whole_answer = handler.on_stable6hdlr4qenv(sf, question, st, old_tmay_whole_answer)
        return tmay_new_tmay_whole_answer



class IQuestionEnv__named_handler_dispatcher(IQuestionEnv__handler_dispatcher):
    #question_env
    __slots__ = ()
    @abstractmethod
    def register_handler6qenv(sf, global_handler_name4sf, local_handler_name4cache_mk, hashable__hdlr_mkr, lazy__hashable__args, /):
        '-> handler_name/global_handler_name4cache_mk # hashable__hdlr_mkr(*lazy__hashable__args()) -> handler #without (global_handler_name4sf,local_handler_name4cache_mk):handler has to remember registered sub-handler in st(ok,but detail)'
    @abstractmethod
    def handler_name2handler6qenv(sf, hdlr_name, /):
        '-> IHandler4IQuestionEnv__handler_dispatcher'
    @abstractmethod
    def question2handler_name6qenv(sf, question, /):
        '-> hdlr_name/handler_name/Hashable'

    @override
    def question2handler6qenv(sf, question, /):
        '-> IHandler4IQuestionEnv__handler_dispatcher'
        (hdlr_name, handler) = sf.question2name_and_handler6qenv(question)
        return handler
    def question2name_and_handler6qenv(sf, question, /):
        '-> (hdlr_name, handler)'
        hdlr_name = sf.question2handler_name6qenv(question)
        handler = sf.handler_name2handler6qenv(hdlr_name)
        return (hdlr_name, handler)

class IQuestionEnv__named_handler_dispatcher__using_name_payload8qstn(IQuestionEnv__named_handler_dispatcher):
    #question_env
    __slots__ = ()
    @override
    def question2handler_name6qenv(sf, question, /):
        '-> hdlr_name/handler_name/Hashable'
        (hdlr_name, qstn_payload) = sf._unwrap5question_(question)
        return hdlr_name
    def _wrap2question_(sf, hdlr_name, qstn_payload, /):
        question = (hdlr_name, qstn_payload)
        return question
    def _unwrap5question_(sf, question, /):
        (hdlr_name, qstn_payload) = question
        return qstn_payload

class IQuestionEnv__named_handler_dispatcher__using_dict4register_handler(IQuestionEnv__named_handler_dispatcher):
    #question_env
    __slots__ = ()
    @abstractmethod
    def _get_dict8name2handler_data_(sf, /):
        '-> name2handler_data/{hdlr_name:hdlr_data}'
    @abstractmethod
    def _get_dict8local_name2global_name5handler_data_(sf, hdlr_data, /):
        '-> local_name2global_name/{local_hdlr_name:global_hdlr_name}'
    @abstractmethod
    def _get_dict8mkr_args2global_name_(sf, /):
        '-> mkr_args2global_name/{(hashable__hdlr_mkr,hashable__args):global_hdlr_name}'
    @abstractmethod
    def _mk_handler_data_(sf, handler, /):
        '-> hdlr_data/handler_data'
    @abstractmethod
    def _find_fresh_global_handler_name4glnames_(sf, global_handler_name4sf, local_handler_name4cache_mk, /):
        '-> fresh-global_handler_name4cache_mk'
    @abstractmethod
    def _get_handler5handler_data_(sf, hdlr_data, /):
        '-> handler'



    @override
    def register_handler6qenv(sf, global_handler_name4sf, local_handler_name4cache_mk, hashable__hdlr_mkr, lazy__hashable__args, /):
        '-> handler_name/global_handler_name4cache_mk # hashable__hdlr_mkr(*lazy__hashable__args()) -> handler #without (global_handler_name4sf,local_handler_name4cache_mk):handler has to remember registered sub-handler in st(ok,but detail)'
        name2handler_data = sf._get_dict8name2handler_data_()
        hdlr_data = name2handler_data[global_handler_name4sf]
        local_name2global_name = sf._get_dict8local_name2global_name5handler_data_(hdlr_data)
        m = local_name2global_name.get(local_handler_name4cache_mk)
        if m is None:
            mkr_args2global_name = sf._get_dict8mkr_args2global_name_()
            hashable__args = lazy__hashable__args()
            k = (hashable__hdlr_mkr, hashable__args)
            m = mkr_args2global_name.get(k)
            if m is None:
                handler = hashable__hdlr_mkr(*hashable__args)
                check_type_le(IHandler4IQuestionEnv__handler_dispatcher, handler)
                #register global
                global_handler_name4cache_mk = sf._find_fresh_global_handler_name4glnames_(global_handler_name4sf, local_handler_name4cache_mk)
                hdlr_data4cache_mk = sf._mk_handler_data_(handler)
                del handler
                if not hdlr_data4cache_mk is name2handler_data.setdefault(global_handler_name4cache_mk, hdlr_data4cache_mk): raise logic-err
                if not global_handler_name4cache_mk is mkr_args2global_name.setdefault(k, global_handler_name4cache_mk): raise logic-err
            else:
                global_handler_name4cache_mk = m
            global_handler_name4cache_mk
            #register local
            if not global_handler_name4cache_mk is local_name2global_name.setdefault(local_handler_name4cache_mk, global_handler_name4cache_mk): raise logic-err
            def lazy__hashable__args(): raise logic-err
            if not global_handler_name4cache_mk is sf.register_handler6qenv(global_handler_name4sf, local_handler_name4cache_mk, hashable__hdlr_mkr, lazy__hashable__args): raise logic-err

        else:
            global_handler_name4cache_mk = m
        global_handler_name4cache_mk
        return global_handler_name4cache_mk
    @override
    def handler_name2handler6qenv(sf, hdlr_name, /):
        '-> IHandler4IQuestionEnv__handler_dispatcher'
        name2handler_data = sf._get_dict8name2handler_data_()
        hdlr_data = name2handler_data[hdlr_name]
        handler = sf._get_handler5handler_data_(hdlr_data)
        return handler

class IQuestionEnv__named_handler_dispatcher__using_dict4register_handler__using_name_payload8qstn(IQuestionEnv__named_handler_dispatcher__using_dict4register_handler, IQuestionEnv__named_handler_dispatcher__using_name_payload8qstn):
    #question_env
    __slots__ = ()

class IHandler4IQuestionEnv__named_handler_dispatcher(IHandler4IQuestionEnv__handler_dispatcher):
    #handler4question_env
    #for IQuestionEnv__named_handler_dispatcher
    #useful: .register_handler6hdlr4qenv
    __slots__ = ()
    @abstractmethod
    def question2payload6hdlr4qenv__nmd(sf, qenv__nmd, question, /):
        '-> qstn_payload #may remove handler_name'
    if 0:
        @override
        def check_question6hdlr4qenv(sf, qenv__nmd, question, /):
            '-> None'
            check_pair(question) #_unwrap5question_#now:question2handler_name6qenv
    @abstractmethod
    def on_start6hdlr4qenv__nmd(sf, qenv__nmd, question, global_handler_name4sf, qstn_payload, /):
        '-> (st, tmay_whole_answer, actions)'
    @abstractmethod
    def on_news6hdlr4qenv__nmd(sf, qenv__nmd, question, global_handler_name4sf, qstn_payload, global_handler_name4sub, subqstn_payload, st, old_tmay_whole_answer, tag, subquestion, old_tmay_sub_answer, new_tmay_sub_answer, /):
        '-> (tmay_st, tmay_new_tmay_whole_answer, actions)'
    @abstractmethod
    def on_stable6hdlr4qenv__nmd(sf, qenv__nmd, question, global_handler_name4sf, qstn_payload, st, old_tmay_whole_answer, /):
        '-> tmay_new_tmay_whole_answer'

    ### forward calls to qenv__nmd
    def register_handler6hdlr4qenv(sf, qenv__nmd, question, local_handler_name4cache_mk, hashable__hdlr_mkr, lazy__hashable__args, /):
        '-> handler_name/global_handler_name4cache_mk # hashable__hdlr_mkr(*lazy__hashable__args()) -> handler #without (global_handler_name4sf,local_handler_name4cache_mk):handler has to remember registered sub-handler in st(ok,but detail)'
        global_handler_name4sf = qenv__nmd.question2handler_name6qenv(question)
        global_handler_name4cache_mk = qenv__nmd.register_handler6qenv(global_handler_name4sf, local_handler_name4cache_mk, hashable__hdlr_mkr, lazy__hashable__args)
        return global_handler_name4cache_mk
    def handler_name2handler6hdlr4qenv(sf, qenv__nmd, hdlr_name, /):
        '-> IHandler4IQuestionEnv__handler_dispatcher'
        handler = qenv__nmd.handler_name2handler6qenv(hdlr_name)
        return handler
    def question2handler_name6hdlr4qenv(sf, qenv__nmd, question, /):
        '-> hdlr_name/handler_name/Hashable'
        hdlr_name = qenv__nmd.question2handler_name6qenv(question)
        return hdlr_name
    def question2name_and_handler_and_payload6hdlr4qenv(sf, question_env, question, /):
        '-> (hdlr_name, handler, qstn_payload)'
        hdlr_name = sf.question2handler_name6hdlr4qenv(question_env, question)
        handler = sf.handler_name2handler6hdlr4qenv(question_env, hdlr_name)
        qstn_payload = sf.handler_name2handler6hdlr4qenv(question_env, question_env)
        qstn_payload = sf.question2payload6hdlr4qenv__nmd(question_env, question)
        return (hdlr_name, handler, qstn_payload)

    @override
    def on_start6hdlr4qenv(sf, question_env, question, /):
        '-> (st, tmay_whole_answer, actions)'
        (hdlr_name, handler, qstn_payload) = sf.question2name_and_handler_and_payload6hdlr4qenv(question_env, question)
        if not handler is sf: raise TypeError
        global_handler_name4sf = hdlr_name
        return sf.on_start6hdlr4qenv__nmd(question_env, question, global_handler_name4sf, qstn_payload)

    @override
    def on_news6hdlr4qenv(sf, question_env, question, st, old_tmay_whole_answer, tag, subquestion, old_tmay_sub_answer, new_tmay_sub_answer, /):
        '-> (tmay_st, tmay_new_tmay_whole_answer, actions)'
        (hdlr_name, handler, qstn_payload) = sf.question2name_and_handler_and_payload6hdlr4qenv(question_env, question)
        if not handler is sf: raise TypeError
        global_handler_name4sf = hdlr_name
        (hdlr_name, handler, subqstn_payload) = sf.question2name_and_handler_and_payload6hdlr4qenv(question_env, subquestion)
        global_handler_name4sub = hdlr_name
        return sf.on_news6hdlr4qenv__nmd(question_env, question, global_handler_name4sf, qstn_payload, global_handler_name4sub, subqstn_payload, st, old_tmay_whole_answer, tag, subquestion, old_tmay_sub_answer, new_tmay_sub_answer)

    @override
    def on_stable6hdlr4qenv(sf, question_env, question, st, old_tmay_whole_answer, /):
        '-> tmay_new_tmay_whole_answer'
        (hdlr_name, handler, qstn_payload) = sf.question2name_and_handler_and_payload6hdlr4qenv(question_env, question)
        if not handler is sf: raise TypeError
        global_handler_name4sf = hdlr_name
        return sf.on_stable6hdlr4qenv__nmd(question_env, question, global_handler_name4sf, qstn_payload, st, old_tmay_whole_answer)

#class IHandler4IQuestionEnv__named_handler_dispatcher__using_name_payload8qstn(IHandler4IQuestionEnv__named_handler_dispatcher):
#   #handler4question_env
#   #for IQuestionEnv__named_handler_dispatcher__using_name_payload8qstn
#   #useful: .register_handler6hdlr4qenv
#   __slots__ = ()


r'''
class IQuestionEnv__subenvironment_dispatcher(IQuestionEnv):
    #question_env
    'question = wrapped_question = (env_name, ground_question)'
    __slots__ = ()
    @abstractmethod
    def get_ground_env5name(sf, env_name, /):
        '-> IQuestionEnv'
    def _get_ground_env5name_name_(sf, env_name4parent, env_name4sub, /):
        '-> IQuestionEnv'
        ground_env4parent = sf.get_ground_env5name(env_name4parent)
        ground_env4mix = ground_env4parent
        return ground_env4mix
    def wrap_actions(sf, env_name, ground_actions, /):
        for ground_action in ground_actions:
            (kind, ground_parent_question, tag, ground_subquestion) = ground_action
            wrapped_parent_question = sf._wrap_question_(env_name, ground_parent_question)
            wrapped_subquestion = sf._wrap_question_(env_name, ground_subquestion)
            yield (kind, wrapped_parent_question, tag, wrapped_subquestion)
    def _wrap_question_(sf, env_name, ground_question, /):
        wrapped_question = (env_name, ground_question)
        return wrapped_question
    def _unwrap_question_(sf, wrapped_question, /):
        (env_name, ground_question) = wrapped_question
        return ground_question
    @override
    def on_start(sf, question, /):
        '-> (st, tmay_whole_answer, actions)'
        wrapped_question = question
        (env_name, ground_question) = sf._unwrap_question_(wrapped_question)
        ground_env = sf.get_ground_env5name(env_name)
        (st, tmay_whole_answer, ground_actions) = ground_env.on_start(ground_question)
        wrapped_actions = sf.wrap_actions(env_name, ground_actions)

        actions = wrapped_actions
        return (st, tmay_whole_answer, actions)
    @override
    def on_news(sf, question, st, old_tmay_whole_answer, tag, subquestion, old_tmay_sub_answer, new_tmay_sub_answer, /):
        '-> (tmay_st, tmay_new_tmay_whole_answer, actions)'
        wrapped_question = question
        (env_name4parent, ground_question) = sf._unwrap_question_(wrapped_question)
        wrapped_subquestion = subquestion
        (env_name4sub, ground_subquestion) = sf._unwrap_question_(wrapped_subquestion)
            #may not eq!!!
        ground_env4mix = sf._get_ground_env5name_name_(env_name4parent, env_name4sub)
        (tmay_st, tmay_new_tmay_whole_answer, ground_actions) = ground_env4mix.on_news(ground_question, st, old_tmay_whole_answer, tag, ground_subquestion, old_tmay_sub_answer, new_tmay_sub_answer)
        wrapped_actions = sf.wrap_actions(env_name, ground_actions)

        actions = wrapped_actions
        return (tmay_st, tmay_new_tmay_whole_answer, actions)
    @override
    def on_stable(sf, question, st, old_tmay_whole_answer, /):
        '-> tmay_new_tmay_whole_answer'
        wrapped_question = question
        (env_name, ground_question) = sf._unwrap_question_(wrapped_question)
        ground_env = sf.get_ground_env5name(env_name)
        tmay_new_tmay_whole_answer = ground_env.on_stable(ground_question, st, old_tmay_whole_answer)
        return tmay_new_tmay_whole_answer
'''#'''



ActionKind = Enum('ActionKind', r'''
ask
cancel
'''#'''
, module=__name__
, qualname='ActionKind'
)
InnerActionKind = Enum('InnerActionKind', r'''
turnon_pdedge_dst
turnoff_pdedge_dst
'''#'''
, module=__name__
, qualname='InnerActionKind'
)

class _Data:
    __slots__ = ()
    def __repr__(sf, /):
        cls = type(sf)
        ordered_attrs = nms = cls.__slots__
        return repr_helper_ex(sf, (), ordered_attrs, {}, ordered_attrs_only=True)
class VtxSt4Question(_Data):
    #vtx_st4question
    #why has .may_actions? since [refcount==0] not turnon yet
    __slots__ = r'''
    refcount
    st
    old_tmay_answer
    tmay_new_tmay_answer
    may_actions
    '''.split()#'''
    #news
    def __init__(sf, st, old_tmay_answer, actions, /):
        sf.refcount = 0
        sf.st = st
        sf.old_tmay_answer = old_tmay_answer
        sf.tmay_new_tmay_answer = ()
        sf.may_actions = actions
        #sf.news = set()

    def get_newest(sf, /):
        newest_tmay_answer = get_newest(sf.old_tmay_answer, sf.tmay_new_tmay_answer)
        return newest_tmay_answer

def get_newest(old_tmay_answer, tmay_new_tmay_answer, /):
    check_tmay(old_tmay_answer)
    check_tmay(tmay_new_tmay_answer)
    if tmay_new_tmay_answer:
        [new_tmay_answer] = tmay_new_tmay_answer
        check_tmay(new_tmay_answer)
        newest_tmay_answer = new_tmay_answer
    else:
        newest_tmay_answer = old_tmay_answer
    check_tmay(newest_tmay_answer)
    return newest_tmay_answer




class PDEdgeSt4SubQuestion(_Data):
    #pdedge_st4subquestion
    r'''
!!!turnoff,cancelled,with_news are diff concepts!!!
is_pdedge_turnon pdedge =[def]= is_vtx_turnon src && is_pdedge_connected pdedge

[dst_st.refcount-=1] iff [(is_pdedge_turnon pdedge) changed from True to False]
cancelled-pdedge:
    control by action:ask/cancel

vtx-turnoff:
    vtx-turnon ==>> resume vtx and try to resume dst, except cancelled-pdedge
    control by inner_action:turnon_pdedge_dst,turnoff_pdedge_dst
#'''

    __slots__ = r'''
    cancelled
    subquestion_has_news
    old_tmay_sub_answer
    '''.split()#'''
    def __init__(sf, subquestion_has_news, /):
        sf.cancelled = True
            #see:on_action_ask
        sf.subquestion_has_news = bool(subquestion_has_news)
        sf.old_tmay_sub_answer = null_tuple

def computing_network_exec(question_env, orginal_main_questions=None, /, *, on_start6qenv=None, on_news6qenv=None, on_stable6qenv=None):
    if orginal_main_questions is None:
        orginal_main_questions = iter(question_env.ask6qenv())
    orginal_main_questions = iter(orginal_main_questions)
    question__tmay_answer__pairs = ComputingNetworkExecutor(question_env, on_start6qenv, on_news6qenv, on_stable6qenv).reply(orginal_main_questions)
    return question__tmay_answer__pairs
class ComputingNetworkExecutor:
    def __init__(sf, question_env, on_start6qenv, on_news6qenv, on_stable6qenv, /):
        if on_start6qenv is None:
            on_start6qenv = type(question_env).on_start6qenv
        if on_news6qenv is None:
            on_news6qenv = type(question_env).on_news6qenv
        if on_stable6qenv is None:
            on_stable6qenv = type(question_env).on_stable6qenv

        sf._env = question_env
        sf._on_start = on_start6qenv
        sf._on_news = on_news6qenv
        sf._on_stable = on_stable6qenv
        sf.dgraph = DGraph4GrowingOnly(
            allow_multi_dedge=False
            ,allow_multi_pdedge=False
            ,imay_xdefault_rank4vtx_st
            =sf.imay_xdefault_rank4vtx_st
            ,xdefault4vtx_st
            =sf.xdefault4vtx_st
            ,imay_xdefault_rank4pdedge_st
            =sf.imay_xdefault_rank4pdedge_st
            ,xdefault4pdedge_st
            =sf.xdefault4pdedge_st
            ,imay_xdefault_rank4dedge_st
            =sf.imay_xdefault_rank4dedge_st
            ,xdefault4dedge_st
            =sf.xdefault4dedge_st
            )
        #Container4ArrayIdx
        #sf.pdedges__turnon = set()
        sf.vtc__turnon = set()
        sf.action_queue = []
        sf.inner_action_queue = []
        sf.connected_pdedges__with_news = set()

    def on_start(sf, question, /):
        '-> (st, tmay_whole_answer, actions)'
        (st, tmay_whole_answer, actions) = sf._on_start(sf._env, question)
        check_tmay(tmay_whole_answer)
        iter(actions)
        return (st, tmay_whole_answer, actions)
    def on_news(sf, question, st, old_tmay_whole_answer, tag, subquestion, old_tmay_sub_answer, new_tmay_sub_answer, /):
        '-> (tmay_st, tmay_new_tmay_whole_answer, actions)'
        check_tmay(old_tmay_whole_answer)
        check_tmay(old_tmay_sub_answer)
        check_tmay(new_tmay_sub_answer)
        #xxx check_type_is(tuple, tag)
        (tmay_st, tmay_new_tmay_whole_answer, actions) = sf._on_news(sf._env, question, st, old_tmay_whole_answer, tag, subquestion, old_tmay_sub_answer, new_tmay_sub_answer)
        check_tmay(tmay_st)
        check_tmay(tmay_new_tmay_whole_answer)
        if tmay_new_tmay_whole_answer: check_tmay(*tmay_new_tmay_whole_answer)
        iter(actions)
        return (tmay_st, tmay_new_tmay_whole_answer, actions)
    def on_stable(sf, question, st, old_tmay_whole_answer, /):
        '-> final_tmay_whole_answer'
        check_tmay(old_tmay_whole_answer)
        tmay_new_tmay_whole_answer = sf._on_stable(sf._env, question, st, old_tmay_whole_answer)
        check_tmay(tmay_new_tmay_whole_answer)
        if tmay_new_tmay_whole_answer: check_tmay(*tmay_new_tmay_whole_answer)
        if tmay_new_tmay_whole_answer:
            [final_tmay_whole_answer] = tmay_new_tmay_whole_answer
        else:
            final_tmay_whole_answer = old_tmay_whole_answer
        return final_tmay_whole_answer
    def put_inner_actions(sf, inner_actions, /):
        #sf.inner_action_queue.extend(inner_actions)
        iq = sf.inner_action_queue
        for kind, pdedge in inner_actions:
            check_type_is(InnerActionKind, kind)
            iq.append((kind, pdedge))

    def put_actions(sf, actions, /):
        sf.action_queue.extend(actions)
        q = sf.action_queue
        for kind, parent, tag, child in actions:
            check_type_is(ActionKind, kind)
            q.append((kind, parent, tag, child))
    #is_pdedge_turnon pdedge =[def]= is_vtx_turnon src && is_pdedge_connected pdedge
    def is_vtx_turnon(sf, vtx, /):
        g = sf.dgraph
        vtx_st = g.vtx2vtx_st(vtx)
        return not vtx_st.refcount==0
    def is_pdedge_connected(sf, pdedge, /):
        g = sf.dgraph
        pdedge_st = g.pdedge2pdedge_st(pdedge)
        return not pdedge_st.cancelled
    def is_pdedge_turnon(sf, pdedge, /):
        return sf.is_pdedge_connected(pdedge) and sf.is_pdedge_src_turnon(pdedge)
    def is_pdedge_src_turnon(sf, pdedge, /):
        g = sf.dgraph
        src, dst = g.pdedge2uv(pdedge)
        return sf.is_vtx_turnon(src)

    def disconnect_pdedge(sf, pdedge, /):
        g = sf.dgraph
        pdedge_st = g.pdedge2pdedge_st(pdedge)

        disconnect = False
        if not pdedge_st.cancelled:
            pdedge_st.cancelled = True
            #sf.pdedges__turnon.remove(pdedge)
            if sf.is_pdedge_src_turnon(pdedge):
                sf.turnoff_pdedge_dst(pdedge)
                #dst_st.refcount -= 1
            if pdedge_st.subquestion_has_news:
                sf.connected_pdedges__with_news.remove(pdedge)
            disconnect = True
        return disconnect


    def connect_pdedge(sf, pdedge, /):
        g = sf.dgraph
        pdedge_st = g.pdedge2pdedge_st(pdedge)
        connect= False
        if pdedge_st.cancelled:
            pdedge_st.cancelled = False
            #sf.pdedges__turnon.add(pdedge)
            if sf.is_pdedge_src_turnon(pdedge):
                sf.turnon_pdedge_dst(pdedge)
                #dst_st.refcount += 1
            if pdedge_st.subquestion_has_news:
                sf.connected_pdedges__with_news.add(pdedge)
            connect= True
        return connect

    def has_news__pdedge(sf, pdedge, /):
        g = sf.dgraph
        pdedge_st = g.pdedge2pdedge_st(pdedge)
        return pdedge_st.subquestion_has_news

    def turnon_news__vtx(sf, vtx, /):
        g = sf.dgraph
        vtx_st = g.vtx2vtx_st(vtx)
        assert vtx_st.tmay_new_tmay_answer
        dst = vtx
        for pdedge in g.dst2iter_pdedges(dst):
            sf.turnon_news__pdedge(pdedge)
    def turnon_news__pdedge(sf, pdedge, /):
        #turnon_news__pdedge
        #handle_news__pdedge
        #connected_pdedges__with_news
        g = sf.dgraph
        pdedge_st = g.pdedge2pdedge_st(pdedge)
        #maybe pdedge_st.cancelled
        turnon = False
        if not pdedge_st.subquestion_has_news:
            pdedge_st.subquestion_has_news = True
            if sf.is_pdedge_connected(pdedge):
                sf.connected_pdedges__with_news.add(pdedge)
            turnon = True
        return turnon



    def turnon_pdedge_dst(sf, pdedge, /):
        #trigger by src.refcount from 0 to 1
        #   no matter the curr src.refcount value
        # so check .cancelled, not check .refcount>0
        #
        g = sf.dgraph
        turnon = False
        if sf.is_pdedge_connected(pdedge):
            src, dst = g.pdedge2uv(pdedge)
            sf.turnon_vtx(dst)
            turnon = True
        return turnon

    def turnoff_pdedge_dst(sf, pdedge, /):
        g = sf.dgraph
        turnoff = False
        if sf.is_pdedge_connected(pdedge):
            src, dst = g.pdedge2uv(pdedge)
            sf.turnoff_vtx(dst)
            turnoff = True
        return turnoff

    def turnon_vtx(sf, vtx, /):
        g = sf.dgraph
        vtx_st = g.vtx2vtx_st(vtx)
        vtx_st.refcount += 1
        if not vtx_st.may_actions is None:
            #only for init phase
            actions = vtx_st.may_actions
            vtx_st.may_actions = None
            sf.put_actions(actions)
        turnon = False
        if vtx_st.refcount == 1:
            sf.vtc__turnon.add(vtx)
            sf.put_inner_actions((InnerActionKind.turnon_pdedge_dst, pdedge) for pdedge in g.src2iter_pdedges(vtx))
            turnon = True
        return turnon
    def turnoff_vtx(sf, vtx, /):
        g = sf.dgraph
        vtx_st = g.vtx2vtx_st(vtx)
        vtx_st.refcount -= 1
        turnoff = False
        if vtx_st.refcount == 0:
            sf.vtc__turnon.remove(vtx)
            sf.put_inner_actions((InnerActionKind.turnoff_pdedge_dst, pdedge) for pdedge in g.src2iter_pdedges(vtx))
            turnoff = True
        return turnoff



    imay_xdefault_rank4vtx_st = 2
    def xdefault4vtx_st(sf, question, vtx, /):
        (st, tmay_whole_answer, actions) = sf.on_start(question)
        #sf.put_actions(actions)
        #   not turnon yet:see:turnon_vtx
        vtx_st = VtxSt4Question(st, tmay_whole_answer, actions)
        #rint(question, vtx_st)
        return vtx_st
    imay_xdefault_rank4dedge_st = -1
    xdefault4dedge_st = None
    imay_xdefault_rank4pdedge_st = 4
    #def xdefault4dedge_st(sf, dgraph, src, dst, pdedge, /):
    #bug:def xdefault4pdedge_st(sf, dgraph, src, dst, pdedge, /):
    def xdefault4pdedge_st(sf, dgraph, dedge, param, pdedge, /):
        g = dgraph
        dst = g.dedge2dst(dedge)
        dst_st = g.vtx2vtx_st(dst)
        newest_tmay_sub_answer = dst_st.get_newest()
        subquestion_has_news = bool(newest_tmay_sub_answer)
        #rint(dst_st, newest_tmay_sub_answer, subquestion_has_news, src, dst)
        #rint(g.vtx2node(src), g.vtx2node(dst))
        pdedge_st = PDEdgeSt4SubQuestion(subquestion_has_news)
        return pdedge_st


    def reply(sf, questions, /):
        g = sf.dgraph
        nv = g.num_vertices
        begin_vtx = nv
        vtc = []
        for question in questions:
            vtx = g.numbers_node(question)
                #may be old vtx < begin_vtx
            sf.turnon_vtx(vtx)
                #refcount += 1
            vtc.append(vtx)
        sf.run_until_stable()
        question__tmay_answer__pairs = sf.collect_anwser_after_stable(vtc)
        return question__tmay_answer__pairs

    def collect_anwser_after_stable(sf, vtc, /):
        g = sf.dgraph
        ls = []
        for vtx in vtc:
            question = g.vtx2node(vtx)
            vtx_st = g.vtx2vtx_st(vtx)
            st = vtx_st.st
            old_tmay_whole_answer = vtx_st.get_newest()
            final_tmay_whole_answer = sf.on_stable(question, st, old_tmay_whole_answer)
            ls.append((question, final_tmay_whole_answer))
        question__tmay_answer__pairs = ls
        return question__tmay_answer__pairs

    def run_until_stable(sf, /):
        sf.vtc__turnon
        #sf.pdedges__turnon
        g = sf.dgraph
        es = sf.connected_pdedges__with_news
        q = sf.action_queue
        iq = sf.inner_action_queue
        while iq or es or q:
            while iq:
                #disconnect vs connect
                #highest priority ==>> before handle
                inner_action = iq.pop()
                sf.handle_inner_action(inner_action)
            ####
            while es and not iq:
                #handle news before ask new questions ==>> before q
                pdedge = es.pop()
                    #sf.connected_pdedges__with_news.remove(pdedge)

                #src can be off!!!
                assert sf.is_pdedge_connected(pdedge)
                assert sf.has_news__pdedge(pdedge)
                sf.handle_news__pdedge(pdedge)
                assert not sf.has_news__pdedge(pdedge)
                assert sf.is_pdedge_connected(pdedge)

            while q and not es and not iq:
                action = q.pop()
                sf.handle_action(action)
    def handle_inner_action(sf, inner_action, /):
        g = sf.dgraph
        kind = inner_action[0]
        if kind is InnerActionKind.turnon_pdedge_dst:
            (_, pdedge) = inner_action
            sf.turnon_pdedge_dst(pdedge)
        elif kind is InnerActionKind.turnoff_pdedge_dst:
            (_, pdedge) = inner_action
            sf.turnoff_pdedge_dst(pdedge)
        else:
            raise Exception(kind)
    def handle_action(sf, action, /):
        g = sf.dgraph
        kind = action[0]
        if kind is ActionKind.ask:
            (_, parent, tag, child) = action
            sf.on_action_ask(parent, tag, child)
        elif kind is ActionKind.cancel:
            (_, parent, tag, child) = action
            sf.on_action_cancel(parent, tag, child)
        else:
            raise Exception(kind)

    def on_action_ask(sf, parent_question, tag, subquestion, /):
        g = sf.dgraph
        src = g.numbers_node(parent_question)
        dst = g.numbers_node(subquestion)
        dedge = g.numbers_uv(src, dst)
        pdedge = g.numbers_dedge_param(dedge, tag)
        #rint(parent_question, subquestion, g.pdedge2pdedge_st(pdedge), g.vtx2vtx_st(dst))
        if 1:
            #if not sf.is_pdedge_connected(pdedge):
            #<<== init .cancelled:=True
            sf.connect_pdedge(pdedge)

    def on_action_cancel(sf, parent_question, tag, subquestion, /):
        g = sf.dgraph
        src = g.numbers_node(parent_question)
        dst = g.numbers_node(subquestion)
        dedge = g.numbers_uv(src, dst)
        pdedge = g.numbers_dedge_param(dedge, tag)
        if 1:
            #if sf.is_pdedge_connected(pdedge):
            sf.disconnect_pdedge(pdedge)


    def handle_news__pdedge(sf, pdedge, /):
        #turnon_news__pdedge
        #handle_news__pdedge
        #connected_pdedges__with_news
        g = sf.dgraph

        pdedge_st = g.pdedge2pdedge_st(pdedge)
        assert pdedge_st.subquestion_has_news
        src, dst = g.pdedge2uv(pdedge)
        src_st = g.vtx2vtx_st(src)
        parent_question = g.vtx2node(src)
        st = src_st.st
        old_tmay_whole_answer = src_st.get_newest()
        tag = g.pdedge2param(pdedge)
        subquestion = g.vtx2node(dst)
        old_tmay_sub_answer = pdedge_st.old_tmay_sub_answer
        dst_st = g.vtx2vtx_st(dst)
        new_tmay_sub_answer = dst_st.get_newest()
        if not (old_tmay_sub_answer or new_tmay_sub_answer):
            #『==』:not news
            #   () --> (x,) --> ()
            pdedge_st.subquestion_has_news = False
            return
        (tmay_st, tmay_new_tmay_whole_answer, actions) = sf.on_news(parent_question, st, old_tmay_whole_answer, tag, subquestion, old_tmay_sub_answer, new_tmay_sub_answer)
        pdedge_st.subquestion_has_news = False
        pdedge_st.old_tmay_sub_answer = new_tmay_sub_answer
        assert src_st.may_actions is None
        sf.put_actions(actions)
        src_st.old_tmay_answer = old_tmay_whole_answer
        src_st.tmay_new_tmay_answer = tmay_new_tmay_whole_answer
        if tmay_st:
            [src_st.st] = tmay_st
        if tmay_new_tmay_whole_answer:
            sf.turnon_news__vtx(src)
        assert not pdedge_st.subquestion_has_news
    #end-def handle_news__pdedge(sf, pdedge, /):

#%s/\(\<g\>\.\w*\)\[\(\w*\)\]/\1(\2)/g
#   g.xxx[yyy] --> g.xxx(yyy)

#end-class ComputingNetworkExecutor:



CFG_SymbolKind = Enum('CFG_SymbolKind', r'''
sequential
arbitrary
terminal
'''#'''
, module=__name__
, qualname='CFG_SymbolKind'
)

def check4setting4CFG(symbol2kind, lsymbol2symbol_seq, /):
    if not isinstance(symbol2kind, Mapping):raise TypeError
    if not isinstance(lsymbol2symbol_seq, Mapping):raise TypeError
    ######################
    if not all(type(kind) is CFG_SymbolKind for kind in symbol2kind.values()):raise TypeError
    ######################
    if not {*lsymbol2symbol_seq} == {symbol for symbol, kind in symbol2kind.items() if kind is not CFG_SymbolKind.terminal}:raise TypeError
    ######################
    if not all(isinstance(symbol_seq, Sequence) for lsymbol, symbol_seq in lsymbol2symbol_seq.items()):raise TypeError
    if not all(symbol in symbol2kind for lsymbol, symbol_seq in lsymbol2symbol_seq.items() for symbol in symbol_seq):raise TypeError

class IQuestionEnv4CFG(IQuestionEnv, ABC__no_slots):
    def __init__(sf, symbol2kind, lsymbol2symbol_seq, /):
        check4setting4CFG(symbol2kind, lsymbol2symbol_seq)
        sf.symbol2kind = symbol2kind
        sf.lsymbol2symbol_seq = lsymbol2symbol_seq
def prepare_args4mk_IQuestionEnv4CFG(rsymbols, sequential2symbols, arbitrary2symbols, /):
    IQuestionEnv4CFG

    sequential2symbols = fmap4dict_value(mk_tuple, sequential2symbols)
    arbitrary2symbols = fmap4dict_value(mk_tuple, arbitrary2symbols)
    lsymbol2symbol_seq = {**sequential2symbols, **arbitrary2symbols}

    d1 = dict.fromkeys(rsymbols, CFG_SymbolKind.terminal)
    d2 = dict.fromkeys(sequential2symbols, CFG_SymbolKind.sequential)
    d3 = dict.fromkeys(arbitrary2symbols, CFG_SymbolKind.arbitrary)
    symbol2kind = {**d1, **d2, **d3}
    check4setting4CFG(symbol2kind, lsymbol2symbol_seq)
    return symbol2kind, lsymbol2symbol_seq
def check_result4CFG__head_set(symbol2kind, lsymbol2symbol_seq, symbol2tmay_min_len, symbol2head_set, /):
    #solve4CFG__head_set
    check_result4CFG__min_len
    if not symbol2head_set.keys() == symbol2kind.keys():raise ValueError
    for symbol, head_set in symbol2head_set.items():
        check_type_is(frozenset, head_set)
        if not head_set <= symbol2kind.keys():raise ValueError

    for symbol, head_set in symbol2head_set.items():
        kind = symbol2kind[symbol]
        if kind is CFG_SymbolKind.terminal:
            if not head_set == frozenset([symbol]):raise ValueError
            continue
        symbol_seq = lsymbol2symbol_seq[symbol]
        head_sets = [symbol2head_set[s] for s in symbol_seq]

        if kind is CFG_SymbolKind.sequential:
            tmays = (symbol2tmay_min_len[s] for s in symbol_seq)
            tmays = filter(bool, tmays)
            bemptys = [not min_len for [min_len] in tmays]
            i = bemptys.index(False) if not all(bemptys) else len(bemptys)-1
            i = i if len(bemptys) == len(symbol_seq) else -1
        elif kind is CFG_SymbolKind.arbitrary:
            i = len(symbol_seq)-1
        else:
            raise ValueError(kind) #not CFG_SymbolKind
        i += 1
        head_sets_ = head_sets[:i]
        s = set()
        s.update(*head_sets_)
        if not head_set == s:raise ValueError(kind, symbol, head_set, head_sets, i, head_sets_, s)

def check_result4CFG__min_len(symbol2kind, lsymbol2symbol_seq, symbol2tmay_min_len, /):
    #solve4CFG__min_len
    if not symbol2tmay_min_len.keys() == symbol2kind.keys():raise ValueError
    for symbol, tmay_min_len in symbol2tmay_min_len.items():
        check_tmay(tmay_min_len)
        if tmay_min_len:
            [min_len] = tmay_min_len
            check_uint(min_len)
    for symbol, tmay_min_len in symbol2tmay_min_len.items():
        kind = symbol2kind[symbol]
        if kind is CFG_SymbolKind.terminal:
            if not tmay_min_len == (1,):raise ValueError
            continue
        symbol_seq = lsymbol2symbol_seq[symbol]
        tmays = (symbol2tmay_min_len[s] for s in symbol_seq)

        tmays = filter(bool, tmays)
        min_lens = [min_len for [min_len] in tmays]
        if kind is CFG_SymbolKind.sequential:
            tm = (sum(min_lens),) if len(min_lens) == len(symbol_seq) else ()
            if not tmay_min_len == tm:raise ValueError
        elif kind is CFG_SymbolKind.arbitrary:
            tm = (min(min_lens),) if len(min_lens) else ()
        else:
            raise ValueError(kind) #not CFG_SymbolKind
        if not tmay_min_len == tm:raise ValueError(kind, symbol, tmay_min_len, min_lens, tm)
assert expectError(TypeError, lambda:int(CFG_SymbolKind.terminal))
assert CFG_SymbolKind(CFG_SymbolKind.terminal.value) is CFG_SymbolKind.terminal

def mk_QuestionEnv4CFG(cls, rsymbols, sequential2symbols, arbitrary2symbols, /, *args):
    (symbol2kind, lsymbol2symbol_seq
    ) = prepare_args4mk_IQuestionEnv4CFG(rsymbols, sequential2symbols, arbitrary2symbols)
    question_env4CFG = cls(symbol2kind, lsymbol2symbol_seq, *args)
    return question_env4CFG

class QuestionEnv4CFG__min_len(IQuestionEnv4CFG, IQuestionEnv__handler_dispatcher):
    @override
    def question2handler6qenv(sf, question, /):
        '-> IHandler4IQuestionEnv__handler_dispatcher'
        symbol = question
        kind = sf.symbol2kind[symbol]
        handler = __class__._kind2handler4CFG__min_len[kind]
        return handler
    @override
    def ask6qenv(sf, /):
        '-> Iter question'
        return iter(sf.symbol2kind)
class Handler4QuestionEnv4CFG__min_len__sequential(IHandler4IQuestionEnv__handler_dispatcher):
    __slots__ = ()
    @override
    def check_question6hdlr4qenv(sf, question_env, question, /):
        '-> None'
        symbol = question
        assert question_env.symbol2kind[symbol] is CFG_SymbolKind.sequential

    @override
    def on_start6hdlr4qenv(sf, qenv, question, /):
        '-> (st, tmay_whole_answer, actions)'
        sequential = lsymbol = question
        symbol_seq = qenv.lsymbol2symbol_seq[sequential]
        if not symbol_seq:
            tmay_sz = (0,)
            st = None
            actions = null_tuple
        else:
            tmay_sz = null_tuple
            st = tmays = [null_tuple]*len(symbol_seq)
            actions = []
            for i, symbol in enumerate(symbol_seq):
                tag = i
                subquestion = symbol
                action = (ActionKind.ask, question, tag, subquestion)
                actions.append(action)
            actions
        tmay_whole_answer = tmay_sz
        return (st, tmay_whole_answer, actions)

    @override
    def on_news6hdlr4qenv(sf, qenv, question, st, old_tmay_whole_answer, tag, subquestion, old_tmay_sub_answer, new_tmay_sub_answer, /):
        '-> (tmay_st, tmay_new_tmay_whole_answer, actions)'
        assert new_tmay_sub_answer
        [new_sub_answer] = new_tmay_sub_answer
        i = tag
        tmays = st
        tmays[i] = new_tmay_sub_answer
        if all(tmays):
            new_tmay_whole_answer = (sum(sz for [sz] in tmays),)
            assert not new_tmay_whole_answer == old_tmay_whole_answer
            tmay_new_tmay_whole_answer = (new_tmay_whole_answer,)
        else:
            tmay_new_tmay_whole_answer = null_tuple
        tmay_st = null_tuple
        actions = null_tuple
        return (tmay_st, tmay_new_tmay_whole_answer, actions)
    @override
    def on_stable6hdlr4qenv(sf, qenv, question, st, old_tmay_whole_answer, /):
        '-> tmay_new_tmay_whole_answer'
        return null_tuple



class Handler4QuestionEnv4CFG__min_len__arbitrary(IHandler4IQuestionEnv__handler_dispatcher):
    __slots__ = ()
    @override
    def check_question6hdlr4qenv(sf, question_env, question, /):
        '-> None'
        symbol = question
        assert question_env.symbol2kind[symbol] is CFG_SymbolKind.arbitrary

    @override
    def on_start6hdlr4qenv(sf, qenv, question, /):
        '-> (st, tmay_whole_answer, actions)'
        arbitrary = lsymbol = question
        symbol_seq = qenv.lsymbol2symbol_seq[arbitrary]

        tag = -1
        actions = []
        for symbol in symbol_seq:
            subquestion = symbol
            action = (ActionKind.ask, question, tag, subquestion)
            actions.append(action)
        actions
        st = None
        tmay_sz = null_tuple
        tmay_whole_answer = tmay_sz

        return (st, tmay_whole_answer, actions)

    @override
    def on_news6hdlr4qenv(sf, qenv, question, st, old_tmay_whole_answer, tag, subquestion, old_tmay_sub_answer, new_tmay_sub_answer, /):
        '-> (tmay_st, tmay_new_tmay_whole_answer, actions)'
        assert new_tmay_sub_answer
        if not old_tmay_whole_answer or new_tmay_sub_answer < old_tmay_whole_answer:
            tmay_new_tmay_whole_answer = (new_tmay_sub_answer,)
        else:
            tmay_new_tmay_whole_answer = null_tuple
        #rint(question, old_tmay_whole_answer, new_tmay_sub_answer, tmay_new_tmay_whole_answer)
        tmay_st = null_tuple
        actions = null_tuple
        return (tmay_st, tmay_new_tmay_whole_answer, actions)
    @override
    def on_stable6hdlr4qenv(sf, qenv, question, st, old_tmay_whole_answer, /):
        '-> tmay_new_tmay_whole_answer'
        return null_tuple



class Handler4QuestionEnv4CFG__min_len__terminal(IHandler4IQuestionEnv__handler_dispatcher):
    __slots__ = ()
    @override
    def check_question6hdlr4qenv(sf, question_env, question, /):
        '-> None'
        symbol = question
        assert question_env.symbol2kind[symbol] is CFG_SymbolKind.terminal

    @override
    def on_start6hdlr4qenv(sf, qenv, question, /):
        '-> (st, tmay_whole_answer, actions)'
        terminal = rsymbol = question
        st = None
        tmay_sz = (1,)
        tmay_whole_answer = tmay_sz
        actions = null_tuple

        return (st, tmay_whole_answer, actions)

    @override
    def on_news6hdlr4qenv(sf, qenv, question, st, old_tmay_whole_answer, tag, subquestion, old_tmay_sub_answer, new_tmay_sub_answer, /):
        '-> (tmay_st, tmay_new_tmay_whole_answer, actions)'
        raise logic-err
    @override
    def on_stable6hdlr4qenv(sf, qenv, question, st, old_tmay_whole_answer, /):
        '-> tmay_new_tmay_whole_answer'
        return null_tuple

_Hs = (
[Handler4QuestionEnv4CFG__min_len__sequential
,Handler4QuestionEnv4CFG__min_len__arbitrary
,Handler4QuestionEnv4CFG__min_len__terminal
])
def _Hs2kind2hdlr(_Hs, /):
    for cls in _Hs:
        mk_existing_type_singleton(cls)
    d = {}
    for x in CFG_SymbolKind:
        for cls in _Hs:
            if cls.__name__.endswith(x.name):
                d[x] = cls()
    assert len(CFG_SymbolKind) == len(_Hs) == len(d) == 3
    return d

QuestionEnv4CFG__min_len._kind2handler4CFG__min_len = _Hs2kind2hdlr(_Hs)
def solve4CFG__min_len(rsymbols, sequential2symbols, arbitrary2symbols, /):
    question_env4CFG__min_len = mk_QuestionEnv4CFG(QuestionEnv4CFG__min_len, rsymbols, sequential2symbols, arbitrary2symbols)
    return solve4CFG__min_len__qenv(question_env4CFG__min_len)
def solve4CFG__min_len__qenv(question_env4CFG__min_len, /):
    QuestionEnv4CFG__min_len
    symbol__tmay_min_len__pairs = computing_network_exec(question_env4CFG__min_len)
    symbol2tmay_min_len = dict(symbol__tmay_min_len__pairs)
    qenv = question_env4CFG__min_len
    check_result4CFG__min_len(qenv.symbol2kind, qenv.lsymbol2symbol_seq, symbol2tmay_min_len)
    return (symbol__tmay_min_len__pairs, symbol2tmay_min_len)

def _test__QuestionEnv4CFG__min_len():
    QuestionEnv4CFG__min_len
    rsymbols = [-1,-2,-3]
    sequential2symbols = {
        100:[-1,188,-3]
        ,200:[-1,-2]
        ,300:[]
        }
    arbitrary2symbols = {
        188:[-1,288,388]
        ,288:[-2,200,288]
        ,388:[-3,300,100]
        }
    symbol__tmay_min_len__pairs, symbol2tmay_min_len = solve4CFG__min_len(rsymbols, sequential2symbols, arbitrary2symbols)
    assert symbol__tmay_min_len__pairs == [(-1, (1,)), (-2, (1,)), (-3, (1,)), (100, (2,)), (200, (2,)), (300, (0,)), (188, (0,)), (288, (1,)), (388, (0,))], symbol__tmay_min_len__pairs

class QuestionEnv4CFG__head_set(IQuestionEnv4CFG, IQuestionEnv__handler_dispatcher):
    def __init__(sf, symbol2kind, lsymbol2symbol_seq, may_symbol2tmay_min_len, /):
        super().__init__(symbol2kind, lsymbol2symbol_seq)
        #solve4CFG__min_len(
        if may_symbol2tmay_min_len is None:
            #bug: not issubclass:(symbol__tmay_min_len__pairs, symbol2tmay_min_len) = solve4CFG__min_len__qenv(sf)
            qenv = QuestionEnv4CFG__min_len(symbol2kind, lsymbol2symbol_seq)
            (symbol__tmay_min_len__pairs, symbol2tmay_min_len) = solve4CFG__min_len__qenv(qenv)
        else:
            symbol2tmay_min_len = may_symbol2tmay_min_len
        sf.symbol2tmay_min_len = symbol2tmay_min_len

    @override
    def question2handler6qenv(sf, question, /):
        '-> IHandler4IQuestionEnv__handler_dispatcher'
        symbol = question
        kind = sf.symbol2kind[symbol]
        handler = __class__._kind2handler4CFG__head_set[kind]
        return handler
    @override
    def ask6qenv(sf, /):
        '-> Iter question'
        return iter(sf.symbol2kind)


class Handler4QuestionEnv4CFG__head_set__sequential(IHandler4IQuestionEnv__handler_dispatcher):
    __slots__ = ()
    @override
    def check_question6hdlr4qenv(sf, question_env, question, /):
        '-> None'
        symbol = question
        assert question_env.symbol2kind[symbol] is CFG_SymbolKind.sequential

    @override
    def on_start6hdlr4qenv(sf, qenv, question, /):
        '-> (st, tmay_whole_answer, actions)'
        sequential = lsymbol = question
        symbol_seq = qenv.lsymbol2symbol_seq[sequential]

        #st :: {head_terminal}
        #anwser :: lnkls<head_terminal>
        empty = (null_frozenset, null_tuple, null_iter)
        if not qenv.symbol2tmay_min_len[lsymbol]:
            #dead:+inf
            return empty

        if not symbol_seq:
            return empty


        actions = []
        tag = -1
        for symbol in symbol_seq:
            subquestion = symbol
            action = (ActionKind.ask, question, tag, subquestion)
            actions.append(action)
            [min_len] = qenv.symbol2tmay_min_len[symbol]
            if min_len:
                break
        actions
        tmay_whole_answer = null_tuple
        st = set()

        return (st, tmay_whole_answer, actions)

    @override
    def on_news6hdlr4qenv(sf, qenv, question, st, old_tmay_whole_answer, tag, subquestion, old_tmay_sub_answer, new_tmay_sub_answer, /):
        '-> (tmay_st, tmay_new_tmay_whole_answer, actions)'
        assert new_tmay_sub_answer
        head_set = st

        def tmay2lnkls(tmay_xxx_answer, /):
            if tmay_xxx_answer:
                [lnkls] = tmay_xxx_answer
            else:
                lnkls = null_tuple
            return lnkls
        new_lnkls = tmay2lnkls(new_tmay_sub_answer)
        old_lnkls = tmay2lnkls(old_tmay_sub_answer)
        whole_lnkls = tmay2lnkls(old_tmay_whole_answer)


        L = len(head_set)
        while new_lnkls and new_lnkls is not old_lnkls:
            terminal, new_lnkls = new_lnkls
            if terminal not in head_set:
                head_set.add(terminal)
                whole_lnkls = (terminal, whole_lnkls)
        tmay_new_tmay_whole_answer = null_tuple if L == len(head_set) else ((whole_lnkls ,) ,)

        tmay_st = null_tuple
        actions = null_iter
        return (tmay_st, tmay_new_tmay_whole_answer, actions)

    @override
    def on_stable6hdlr4qenv(sf, qenv, question, st, old_tmay_whole_answer, /):
        '-> tmay_new_tmay_whole_answer'
        head_set = st
        return ((mk_frozenset(head_set) ,) ,)



class Handler4QuestionEnv4CFG__head_set__arbitrary(IHandler4IQuestionEnv__handler_dispatcher):
    __slots__ = ()
    @override
    def check_question6hdlr4qenv(sf, question_env, question, /):
        '-> None'
        symbol = question
        assert question_env.symbol2kind[symbol] is CFG_SymbolKind.arbitrary

    @override
    def on_start6hdlr4qenv(sf, qenv, question, /):
        '-> (st, tmay_whole_answer, actions)'
        arbitrary = lsymbol = question
        symbol_seq = qenv.lsymbol2symbol_seq[arbitrary]

        tag = -1
        actions = []
        for symbol in symbol_seq:
            subquestion = symbol
            action = (ActionKind.ask, question, tag, subquestion)
            actions.append(action)
        actions
        st = set()
        tmay_whole_answer = null_tuple

        return (st, tmay_whole_answer, actions)

    #@override
    on_news6hdlr4qenv = Handler4QuestionEnv4CFG__head_set__sequential.on_news6hdlr4qenv
    #@override
    on_stable6hdlr4qenv = Handler4QuestionEnv4CFG__head_set__sequential.on_stable6hdlr4qenv



class Handler4QuestionEnv4CFG__head_set__terminal(IHandler4IQuestionEnv__handler_dispatcher):
    __slots__ = ()
    @override
    def check_question6hdlr4qenv(sf, question_env, question, /):
        '-> None'
        symbol = question
        assert question_env.symbol2kind[symbol] is CFG_SymbolKind.terminal

    @override
    def on_start6hdlr4qenv(sf, qenv, question, /):
        '-> (st, tmay_whole_answer, actions)'
        terminal = rsymbol = question
        st = None
        lnkls = (terminal, null_tuple)
        tmay_whole_answer = (lnkls,)
        actions = null_iter

        return (st, tmay_whole_answer, actions)

    @override
    def on_news6hdlr4qenv(sf, qenv, question, st, old_tmay_whole_answer, tag, subquestion, old_tmay_sub_answer, new_tmay_sub_answer, /):
        '-> (tmay_st, tmay_new_tmay_whole_answer, actions)'
        raise logic-err
    @override
    def on_stable6hdlr4qenv(sf, qenv, question, st, old_tmay_whole_answer, /):
        '-> tmay_new_tmay_whole_answer'
        terminal = rsymbol = question
        return ((frozenset([terminal]) ,) ,)

_Hs = (
[Handler4QuestionEnv4CFG__head_set__sequential
,Handler4QuestionEnv4CFG__head_set__arbitrary
,Handler4QuestionEnv4CFG__head_set__terminal
])
QuestionEnv4CFG__head_set._kind2handler4CFG__head_set = _Hs2kind2hdlr(_Hs)

solve4CFG__min_len__qenv
def solve4CFG__head_set(rsymbols, sequential2symbols, arbitrary2symbols, may_symbol2tmay_min_len, /):
    question_env4CFG__head_set = mk_QuestionEnv4CFG(QuestionEnv4CFG__head_set, rsymbols, sequential2symbols, arbitrary2symbols, may_symbol2tmay_min_len)
    return solve4CFG__head_set__qenv(question_env4CFG__head_set)
def solve4CFG__head_set__qenv(question_env4CFG__head_set, /):
    QuestionEnv4CFG__head_set
    symbol__tmay_head_set__pairs = computing_network_exec(question_env4CFG__head_set)
    symbol__head_set__pairs = tuple((symbol, head_set) for symbol, [head_set] in symbol__tmay_head_set__pairs)
    symbol2head_set = dict(symbol__head_set__pairs)
    qenv = question_env4CFG__head_set
    check_result4CFG__head_set(qenv.symbol2kind, qenv.lsymbol2symbol_seq, qenv.symbol2tmay_min_len, symbol2head_set)
    return (symbol__head_set__pairs, symbol2head_set)

def _test__QuestionEnv4CFG__head_set():
    QuestionEnv4CFG__head_set
    rsymbols = [-1,-2,-3]
    sequential2symbols = {
        100:[-1,188,-3]
        ,200:[-1,-2]
        ,300:[]
        }
    arbitrary2symbols = {
        188:[-1,288,388]
        ,288:[-2,200,288]
        ,388:[-3,300,100]
        }
    may_symbol2tmay_min_len = None
    symbol__head_set__pairs, symbol2head_set = solve4CFG__head_set(rsymbols, sequential2symbols, arbitrary2symbols, may_symbol2tmay_min_len)
    assert symbol__head_set__pairs == ((-1, frozenset({-1})), (-2, frozenset({-2})), (-3, frozenset({-3})), (100, frozenset({-1})), (200, frozenset({-1})), (300, frozenset()), (188, frozenset({-3, -2, -1})), (288, frozenset({-2, -1})), (388, frozenset({-3, -1})))


from seed.algo.computing_network import *
from seed.algo.computing_network import _test__QuestionEnv4CFG__min_len
from seed.algo.computing_network import _test__QuestionEnv4CFG__head_set

if __name__ == "__main__":
    _test__QuestionEnv4CFG__min_len()
if __name__ == "__main__":
    _test__QuestionEnv4CFG__head_set()
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +IGNORE_EXCEPTION_DETAIL

