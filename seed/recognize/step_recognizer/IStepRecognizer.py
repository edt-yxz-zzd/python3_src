#__all__:goto
doing...
r'''[[[
e ../../python3_src/seed/recognize/step_recognizer/IStepRecognizer.py
view ../../python3_src/seed/data_funcs/finger_tree/ft23_7sized_seq.py
view ../../python3_src/seed/data_funcs/finger_tree/ft23_7sized_ascend_set.py
view ../../python3_src/seed/data_funcs/finger_tree/ft23_7sized_ascend_mapping7split_table.py
    #seq,set,mapping: Seq,AscendSet,AscendMap
    #seq,set,mapping: Seq,HashSet,HashMap
    [HashSet{k} == (sz,AscendMap{hash:Seq{k}})]
    [HashMap{k:v} == (sz,AscendMap{hash:Seq{(k,v)}})]

seed.recognize.step_recognizer.IStepRecognizer
py -m nn_ns.app.debug_cmd   seed.recognize.step_recognizer.IStepRecognizer -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.recognize.step_recognizer.IStepRecognizer:__doc__ -ht # -ff -df
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.recognize.step_recognizer.IStepRecognizer:cls@T    =T   +exclude_attrs5listed_in_cls_doc
#######
from seed.pkg_tools.ModuleReloader import mk_doctestXmodule_reloader_
doctestXmodule_reloader = mk_doctestXmodule_reloader_('', 'seed.recognize.step_recognizer.IStepRecognizer:__doc__', '-ht')
doctestXmodule_reloader(reload_first=False)
doctestXmodule_reloader()
#######

[[
git mv -v seed/recognize/step_recognizer/IStepRecognizer.py seed/recognize/step_recognizer/IStepRecognizer-20260403.py
view ../../python3_src/seed/recognize/step_recognizer/IStepRecognizer-20260403.py
]]
[[
env-bg:the same object per run:global scene
ctx-fg:maybe diff object
cfg:config/setting per rgnr #may params

rgnr :: IStepRecognizer
token_set :: ITester
child :: (Base token_set | Down rgnr ctx cfg) #except:env
    predication,predicate,criterion
    [ctx is None] => ctx_free

eresult :: (KO errmsg | OK oresult ctx)
rgnr7serial:
    tuple-style:normal
    array-style:ftSeq: [oresult7child :: (case4unpack, payload8oresult7child)]

idnt :: HasAttr__to_intern
取消:vtx :: HasAttr__to_intern

idnt:
    #identifier
    .to_intern :: bool
        if to_intern: hashable
取消:vtx:
    #vertex
    .to_intern :: bool

prepare :: rgnr -> env -> ctx -> cfg -> idnt
start_up :: rgnr -> env -> idnt -> vtx
end_up :: rgnr -> env -> idnt -> vtx -> Iter eresult
    #finalize,terminal
    # eresult{this} ~~> vtx{this} ~~> idnt{this}
fan_out :: rgnr -> env -> idnt -> vtx -> Iter (child, edge)
    #diverge
    # idnt{child} ~~> edge{this} ~~> idnt{this}
ruminate :: rgnr -> env -> idnt -> edge -> eresult7child -> vtx


全是:反刍ruminate oresult7child
    没有:投料feed token
    料符集/料符判定器 作为 子部件 另算工作流程
token_set :: ITester
    #eresult:
        # oresult be token
        # ctx be None
        # errmsg be token_set

    #xx:.__invert__
    #xx:    vs:
    #xx:        .__neg__
    #xx:.__contains__
    #xx:    vs:
    #xx:        .__call__
    #xx:        .test
    #xx:        .is_good

]]
[[
难点:左递归=>死循环, count7ref无用
    jidnt2idnt_cnrf, jjchild2parents
禁止左递归？
]]




'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.recognize.step_recognizer.IStepRecognizer   @f
from seed.recognize.step_recognizer.IStepRecognizer import *
]]]'''#'''
__all__ = r'''
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
#.from abc import update_abstractmethods
from seed.abc.abc__ver1 import abstractmethod, override, ABC
from typing import Union
#.#################################
#.from seed.for_libs.for_importlib__reload import clear_later_variables_if_reload_
#.clear_later_variables_if_reload_(globals(), '')
#.    # <<== seed.pkg_tools.ModuleReloader
#.
#.#################################
#.from seed.helper.lazy_import__func7dict import lazy_import__funcs7dict_
#.(check_type_is, check_int_ge, _ifNone) = lazy_import__funcs7dict_(__name__ or globals() or locals(), 'seed.tiny_.check',  'check_type_is, check_int_ge      ifNone:_ifNone')
#.#################################
#.def mk_context4lazy_import_registered_names_(qnm4mdl7inject, qnm4pseudo_mdl7import, name7importZqnm4mdl, name7importZalias7inject={}, may_bifix4lazy_name7import=None, lazy_name7importZoriginal_name7import={}):
#.from seed.helper.lazy_import__func7context7register import mk_context4lazy_import_registered_names_, name7importZqnm4mdl_7tiny
#.with mk_context4lazy_import_registered_names_(__name__, 'seed._lazy_', name7importZqnm4mdl_7tiny):
#.    from seed._lazy_ import print_err, fst, echo, ifNone
#.with mk_context4lazy_import_registered_names_(__name__, 'seed._lazy_', name7importZqnm4mdl_7tiny, name7importZalias7inject={'echo':'echo_'}):
#.    from seed._lazy_ import echo as echo_
#.with mk_context4lazy_import_registered_names_(__name__, 'seed._lazy_', name7importZqnm4mdl_7tiny, lazy_name7importZoriginal_name7import={'lazy_null_tuple':'null_tuple'}):
#.    from seed._lazy_ import lazy_null_tuple
#.with mk_context4lazy_import_registered_names_(__name__, 'seed._lazy_', name7importZqnm4mdl_7tiny, may_bifix4lazy_name7import=('lazy_','_')):
#.    from seed._lazy_ import lazy_null_tuple_
#.#################################
#.from seed.helper.lazy_import__func7context import mk_ctx4lazy_import8lazy_objs__ver2_
#.with mk_ctx4lazy_import8lazy_objs__ver2_(nonexistent_prefix4qnm4mdl8src='__.', prefix4attr='lazy_', suffix4attr=''):
#.    from __.seed.tiny_.containers import lazy_null_tuple,lazy_null_iter,lazy_null_frozenset as _lazy_null_frozenset_ #null_tuple,null_iter,null_frozenset
#.#################################
#.from seed.helper.lazy_import__func import force_lazy_imported_func_ # lazy_import4func_, lazy_import4funcs_
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
#.with mk_ctx4lazy_import4funcs_(__name__, 'ifNone:_ifNone, ifNonef:_ifNonef'):
#.    from seed.helper.ifNone import ifNone as _ifNone, ifNonef as _ifNonef
#.with mk_ctx4lazy_import4funcs_(__name__, arbitrary_ok=True):
#.    from seed.data_funcs.lnkls import rglnkls_ops# empty_rglnkls, mk_empty_rglnkls, rglnkls_ipush_right, rglnkls_ipop_right, rglnkls2reversed_iterable, rglnkls5iterable
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.types.Tester import is_good, ITester
    from seed.types.CachedProperty import CachedProperty# mk_cached_propertyT_
    from seed.helper.get_key6set import get_keys6set_, get_tmay_key6set_, get_key6set_
    from seed.data_funcs.finger_tree.ft23_7sized_seq import Seq
    from seed.data_funcs.finger_tree.ft23_7sized_ascend_set import AscendSet, NotAscendError
    from seed.data_funcs.finger_tree.ft23_7sized_ascend_mapping7split_table import AscendMap, mkAscendMap, TableLenError, DisorderKeyError
#.    from itertools import islice
#.    from functools import cached_property
#.    from seed.for_libs.for_functools.cached_property import cached_property
#.    from seed.func_tools.dot2 import dot
#.    from seed.tiny_.bmk_pairs import bmk_pairs
#.    from seed.tiny_.check import check_type_is, check_int_ge
#.
#.    from seed.helper.repr_input import repr_helper
#.    from seed.tiny_.map_ import map_, cmap_, call_, prepare4call_, dots_
#.    from seed.tiny_.types5py import mk_MapView,curry1,kwargs2Attrs #,MapView
#.    from seed.tiny_.containers import mk_tuple,mk_immutable_seq,mk_immutable_seq5iterT_,mk_immutable_seq5iter__,mk_bytes5iter_,mk_tuple__split_first_if_str,mk_tuple__split_first_if_str__sep_ #xxx:null_tuple
#.    from seed.debug.print_err import print_err
#.    from seed.debug.expectError import expectError
#.    from seed.helper.ifNone import ifNone,ifNonef
#.    from seed.tiny_.funcs import echo,fst,snd
#.    from seed.types.Either import mk_Left,mk_Right #Either,Cased
#.    from seed.iters.flatten_recur import flatten_recur
#.    # def flatten_recur(g:Generator, /, *, value:object=None, is_exc=False, boxed=False):
#.    from seed.func_tools.dot_ import dot_
#.    from seed.iters.PeekableIterator import echo_or_mk_PeekableIterator
    from seed.for_libs.for_collections.override_repr4namedtuple import mk_namedtuple_, mk_namedtuple__check6make_
    #def mk_namedtuple_(__module__, nm, nms_or_str, /, *args, **kwds):
    #def mk_namedtuple__check6make_(__module__, nm, nms_or_str, /, *args, **kwds):
    #    def _check6make_(sf, /):
#.    from seed.for_libs.for_collections.namedtuple__nontuple4cached_property import mk_named_pseudo_tuple_
#.    #def mk_named_pseudo_tuple_(__module__,typename, field_names, /):
#.    #    def _check6make_(sf, /):
#.    from seed.for_libs.for_collections.namedtuple__nontuple4cached_property import collect_tuple_subclasses_with_cached_property
#.    #assert not (__:=collect_tuple_subclasses_with_cached_property(globals(), to_print_err=True)), __
#.#################################
#.:s/\v^from +([_[:alnum:].]+) +import +([^# ]( *[^# ])*).*/lazy_import4funcs_('\1', '\2', __name__)\rif 0:\0



#.#################################
#.from seed.types.LazyList import ToConcatLazyList, decorator4protocol4ToConcatLazyList_
#.from seed.types.LazyList import LazyList, LazyListError
#.from seed.types.LazyList import to_LazyList, to_LazyListIter
#.
#.from seed.tiny_._Base4repr import _Base4repr
        #sf._reset4repr(may_args4repr, may_kwds4repr)
        #sf._init4repr(*args4repr, **kwds4repr)
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError(Exception, StopIteration)

__all__




#now:using ITester
#.class TokenSet(ABC):
#.    __slots__ = ()
#.    @abstractmethod
#.    def __contains__(sf, token, /):
#.        '-> token'
#.    def __(sf, token, /):

KO = mk_namedtuple_(__name__, 'KO', 'errmsg')
OK = mk_namedtuple_(__name__, 'OK', 'oresult  ctx')
KO.ok = False
OK.ok = True
#EResult = (OK, KO)
EResult = Union[OK, KO]
    # eresult

Base = mk_namedtuple_(__name__, 'Base', 'token_set')
Down = mk_namedtuple_(__name__, 'Down', 'rgnr ctx cfg')
Child = Union[Base, Down]
    # child


_HasAttr__to_intern = mk_named_pseudo_tuple_(__name__, '_HasAttr__to_intern', 'to_intern  payload')
class HasAttr__to_intern(_HasAttr__to_intern):
    'idnt'
    #xxx:'idnt,vtx'
    def _check6make_(sf, /):
        check_type_is(bool, sf.to_intern)
        if sf.to_intern:
            hash(sf)
    @CachedProperty
    def _h(sf, /):
        '[to_intern is True] => -> uint'
        return hash((type(sf), sf.payload))
    def __hash__(sf, /):
        return sf._h
    def __eq__(sf, ot, /):
        if sf is ot:
            return True
        if not type(sf) is type(ot):
            return NotImplemented
        if not (sf.to_intern and ot.to_intern):
            return False
        return hash(sf) == hash(ot) and sf.payload == ot.payload
    def __ne__(sf, ot, /):
        return not sf == ot

class IStepRecognizer(ABC):
    __slots__ = ()
    @abstractmethod
    def prepare(rgnr, env, ctx, cfg, /):
        'rgnr -> env -> ctx -> cfg -> idnt'
    @abstractmethod
    def start_up(rgnr, env, idnt, /):
        'rgnr -> env -> idnt -> vtx'
    @abstractmethod
    def end_up(rgnr, env, idnt, vtx, /):
        'rgnr -> env -> idnt -> vtx -> Iter eresult'
    @abstractmethod
    def fan_out(rgnr, env, idnt, vtx, /):
        'rgnr -> env -> idnt -> vtx -> Iter (child, edge)'
    @abstractmethod
    def ruminate(rgnr, env, idnt, edge, eresult7child, /):
        'rgnr -> env -> idnt -> edge -> eresult7child -> vtx'


#:class RgnzState:
#:    r'''[[[
#:
#:    #seq,set,mapping: Seq,AscendSet,AscendMap
#:
#:    max_used_jidnt :: uint
#:        #ordinal
#:        jidnt > 0
#:    jidnt2idnt_cnrf :: {jidnt:(idnt, count7ref)}
#:    idntI2jidnt :: {idnt{to_intern}:jidnt}
#:    jj_vtxI_set :: {(jjthis, vtx{to_intern})}
#:        xxx:vtxI2cnrf :: {vtx{to_intern}:count7ref}
#:        xxx:WeakSet{vtx{to_intern}}
#:        # intern_() using:get_key6set_
#:
#:    # eresult{this} ~~> ((jtoken, jidnt{this}), vtx{this})
#:    # (jtoken, jidnt{child}) ~~> ((jtoken, jidnt{this}), edge{this})
#:    jjchild2parents
#:        main_entry:(0, 1)/(jtoken, jidnt{child})
#:        :: {(jtoken, jidnt{child}):[((jtoken, jidnt{this}), edge{this})]}
#:        #xxx :: {(jtoken, jidnt{child}):{(jtoken, jidnt{this}):[edge{this}]}}
#:
#:    token_set2parents
#:        :: {token_set:[((jtoken, jidnt{this}), edge{this})]}
#:
#:    难点:左递归=>死循环, count7ref无用
#:        jidnt2idnt_cnrf, jjchild2parents
#:    ]]]'''#'''
#:
#:
#:def shortest_parse7tokens_(rgnr, env, ctx, cfg, tokens, jtoken=0, /):
#:    '-> ([eresult], num_consumed_tokens, jtoken, iter_remain_tokens)'
#:    iter_remain_tokens = iter(tokens)
#:    return _shortest_parse7tokens_(rgnr, env, ctx, cfg, iter_remain_tokens, jtoken)
#:def _shortest_parse7tokens_(rgnr7main, env, ctx7main, cfg7main, iter_remain_tokens, jtoken0, /):
#:    def mk_new_jidnt_():
#:        nonlocal max_used_jidnt
#:        max_used_jidnt += 1
#:        return max_used_jidnt
#:
#:    max_used_jidnt = 0
#:    max_used_jidnt
#:        # :: uint
#:        #ordinal
#:    777;main_entry = (jtoken0, 1)
#:        # jidnt > 0
#:    777;pseudo_entry = (pseudo_entry, None)
#:    777;pseudo_parent = (None, None)
#:    jidnt2idnt_cnrf = {}
#:        # :: {jidnt:(idnt, count7ref)}
#:    idntI2jidnt = {}
#:        # :: {idnt{to_intern}:jidnt}
#:    jj_vtxI_set = set()
#:        # :: {(jjthis, vtx{to_intern})}
#:        # intern_() using:get_key6set_
#:
#:    jjchild2parents = {}
#:        # :: {(jtoken, jidnt{child}):[((jtoken, jidnt{this}), edge{this})]}
#:
#:    token_set2parents = {}
#:        # :: {token_set:[((jtoken, jidnt{this}), edge{this})]}
#:
#:    jjancestor_stk = []
#:    jjancestor_set = set()
#:        # forbid left_recur
#:
#:    jjthis2eresults = {}
#:        # :: {(jtoken, jidnt{this}):[eresult]}
#:
#:    def number_idnt_(idnt, /):
#:        '-> jidnt'
#:        if idnt.to_intern:
#:            if not None is (jidnt:=idntI2jidnt.get(idnt)):
#:                jidnt
#:            else:
#:                jidnt = mk_new_jidnt_()
#:                idntI2jidnt[idnt] = jidnt
#:            jidnt
#:        else:
#:            jidnt = mk_new_jidnt_()
#:        jidnt
#:        return jidnt
#:    def mk_output(jtoken, ls4eresult, /):
#:        #nonlocal jtoken
#:        num_consumed_tokens = jtoken -jtoken0
#:        return (ls4eresult, num_consumed_tokens, jtoken, iter_remain_tokens)
#:    def intern_vtx_(jjthis, vtx, /):
#:        '-> b_new/bool'
#:        jj_vtx = (jjthis, vtx)
#:        b_new = not get_tmay_key6set_(jj_vtxI_set, jj_vtx)
#:        if b_new:
#:            jj_vtxI_set.add(jj_vtx)
#:        return b_new
#:    def add_jj_(jjchild, parent, /):
#:        '-> b_new/bool'
#:        # pseudo_parent
#:        # jjchild2parents
#:        parents = jjchild2parents.setdefault(jjchild, [])
#:        parents.append(parent)
#:        inc_count7ref_(parent[0][1])
#:        b_new = len(parent) == 1
#:        return b_new #new jjchild
#:    def add_child_(jtoken, child, parent, /):
#:        # pseudo_parent
#:        match child:
#:            case Base(token_set):
#:                parents = token_set2parents.setdefault(token_set, [])
#:                parents.append(parent)
#:                inc_count7ref_(parent[0][1])
#:            case Down(rgnr, ctx, cfg):
#:                idnt = rgnr.prepare(env, ctx, cfg)
#:                jidnt = number_idnt_(idnt)
#:                jjthis = (jtoken, jidnt)
#:                if add_jj_(jjthis, parent):
#:                    add_idnt_(jtoken, idnt, jjthis)
#:            case _:
#:                raise TypeError(child)
#:    def add_idnt_(jtoken, idnt, jjthis, /):
#:        # pseudo_parent
#:        vtx = rgnr.start_up(env, idnt)
#:        if not intern_vtx_(jjthis, vtx):
#:            return
#:        ls4eresult = jjthis2eresults.setdefault(jjthis, [])
#:        ls4eresult.extend(rgnr.end_up(env, idnt, vtx))
#:            ???howto goback???
#:        child_edge_pairs = rgnr.fan_out(env, idnt, vtx)
#:        for child, edge in child_edge_pairs:
#:            parent = (jjthis, edge)
#:            add_child_(jtoken, child, parent)
#:        raise NotImplementedError
#:    def inc_count7ref_(jidnt, /):
#:    def main():
#:        #nonlocal jtoken
#:        jtoken = jtoken0
#:        it = enumerate(iter_remain_tokens, jtoken0)
#:        child8main = Down(rgnr7main, ctx7main, cfg7main)
#:        add_child_(jtoken0, child8main, pseudo_parent)
#:        assert main_entry == jjthis
#:            # no:parent
#:        if ls4eresult:
#:            return mk_output(jtoken, ls4eresult)
#:        raise NotImplementedError
#:        doing...
#:    return main()



class RgnzState:
    r'''[[[
    #seq,set,mapping: Seq,AscendSet,AscendMap
    #seq,set,mapping: Seq,HashSet,HashMap
    [HashSet{k} == (sz,AscendMap{hash:Seq{k}})]
    [HashMap{k:v} == (sz,AscendMap{hash:Seq{(k,v)}})]

    不永久归一化{避用count7ref}:(jtoken, idnt{child})
    临时性归一化:仅当前jtoken:
    jt_id_thisI2rc_ancestorss
        :: py_dict{(jtoken, idnt{to_intern}{this}):[jt_id_ancestors1{this}]}
        取消:vtx :: HasAttr__to_intern
        难点:左递归=>死循环
        =>禁止左递归

    临时性存在:同步于调用栈帧:
    ancestorI_stk :: [(jtoken, idnt{to_intern})]
    ancestorI_set :: {(jtoken, idnt{to_intern})}

    归一化:token_set
    token_set2rc_parents
        :: HashMap{token_set:[jt_id_ancestors1]}

    [jt_id_ancestors == rglnkls{((jtoken, idnt{this}), edge{this})}]
    [jt_id_ancestors1 == jt_id_ancestors{nonempty}]

    ]]]'''#'''


def shortest_parse7tokens_(rgnr, env, ctx, cfg, tokens, jtoken=0, /):
    '-> ([eresult], num_consumed_tokens, jtoken, iter_remain_tokens)'
    iter_remain_tokens = iter(tokens)
    return _shortest_parse7tokens_(rgnr, env, ctx, cfg, iter_remain_tokens, jtoken)
def _shortest_parse7tokens_(rgnr7main, env, ctx7main, cfg7main, iter_remain_tokens, jtoken0, /):
    #先实现 主动版{隐态}，再实现 被动版{显态}HashMap
    def main():
    return main()



__all__
from seed.recognize.step_recognizer.IStepRecognizer import *
