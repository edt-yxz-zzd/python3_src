#__all__:goto
#TODO:interface:ops4xxx,env8bg
#TODO:tuple,array/many,end_by,sep_by,ctx_between,ctx_assert(key6ctx)
#TODO:attr-access kps8oc 还有 后处理 只能 作用于 Boxed以下，Boxed以上只是纯粹的Rope&&Pack(lazy-boxed)?
#TODO:++selected_args6ctx8fg, 使用None表示空？
#TODO:kps8oc 怎么构建？标准型？是否传入ops4kps8oc给_get_branch6flowchart4serial_rgnr_()
#TODO:tkey 判定器:1.全序区间序列，2.基础判定器predicate 3.缓存判定结果cached 4.真值表达式/集合表达式
#TODO:输出++欤消耗料符 以支持LL1 => eof料符
#TODO:mimic{key2getter} => getters8partial_oresult
#TODO:flow:st,ctx,partial_oresult分离？
#TODO:mimic{IAsbeItem4serial_rgnr} => IAsbeItem4tuple_rgnr, IAsbeItem4array_rgnr, IAsbeItem4ctx_between_rgnr
#TODO:分离出flowchart
#TODO:main loop
r'''[[[
e ../../python3_src/seed/recognize/step_recognizer/IStepRecognizer.py

py -m seed.recognize.step_recognizer.IStepRecognizer
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
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.recognize.step_recognizer.IStepRecognizer   @f
from seed.recognize.step_recognizer.IStepRecognizer import *
]]]'''#'''
__all__ = r'''
IInfoCollector
    mk_null_iter_
    IStepRecognizer
        Case4eoxst4rgnr
        neednot__feed__token_
        relay__feed__oresult_
        save__mk_cfg4rgnr_
    IStepRecognizer__ref
    IStepRecognizer__named
    IStepRecognizer__wrapper
        IStepRecognizer__named_wrapper
        StepRecognizer__wrapper__rgnr_expr_with_repr
    IStepRecognizer__parallel
    IStepRecognizer__flow
        IAsbeItem4flow_rgnr
        IStepRecognizer__serial
            IAsbeItem4serial_rgnr
            Case4join4serial_rgnr
            IStepRecognizer__serial__using_flow_fork_branch_scheme_AS_flowchart

IConfiguration8Scene
    IEnvironment8Background
        IOperations4ExState4StepRecognizer
        IOperations4FrozenRope
            check_wrapped_
                check_rope_
                check_boxed_
            append__via_join_
                rope2boxed_tuple__unboxed_all_elements_
                wrapped_oresult2boxed_oresult_
        IOperations4FrozenTreeStyleSequential
        IOperations4FrozenTreeStyleMapping
        IOperations4lookup
        IOperations4KeyPathSet8OutputControl
            union_kps8oc_at_case4join_
    IOperations8PrivilegeControl
        IOperations4token
        Flag4IOperations8PrivilegeControl
            null_flag4ops8pc


IKeyPathSet8OutputControl
    KeyPathSet8OutputControl__ignore
        kps8oc__ignore
    KeyPathSet8OutputControl__whole
        kps8oc__whole
    KeyPathSet8OutputControl__lazy_whole
        kps8oc__lazy_whole

IAsbeItem4flow_rgnr
    IAsbeItem4serial_rgnr
        item4serial_rgnr_to_item4flow_rgnr_
        AsbeItem4serial_rgnr__plain
IAsbeStatedPoint6flowchart
    AsbeStatedPoint6flowchart__plain
IAsbeStatedJmpStep6flowchart
    AsbeStatedJmpStep6flowchart__plain

IStepRecognizer__serial__using_flow_fork_branch_scheme_AS_flowchart
    IStepRecognizer__serial__tuple
    IStepRecognizer__serial__array
    IStepRecognizer__serial__end_by
    IStepRecognizer__serial__sep_by
    IStepRecognizer__serial__ctx_between



mk_unit_tuple_
FalseFalse
TrueTrue


'''.split()#'''
    #_extract_
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from enum import Enum, Flag, auto
from functools import cached_property
from collections.abc import Mapping as IMapping, Hashable as IHashable
#from collections import named_tuple
#.from itertools import islice
from seed.tiny_.check import check_type_le, check_type_is, check_int_ge_le
#see:dot_#from seed.func_tools.dot2 import dot
#.
#.from abc import update_abstractmethods
from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.#################################
#.from seed.for_libs.for_importlib__reload import clear_later_variables_if_reload_
#.clear_later_variables_if_reload_(globals(), '')
#.    # <<== seed.pkg_tools.ModuleReloader
#.
#.#################################
#.from seed.helper.lazy_import__func7context import mk_ctx4lazy_import8lazy_objs__ver2_
#.with mk_ctx4lazy_import8lazy_objs__ver2_(nonexistent_prefix4qnm4mdl8src='__.', prefix4attr='lazy_', suffix4attr=''):
#.    from __.seed.tiny_.containers import lazy_null_tuple,lazy_null_iter,lazy_null_frozenset as _lazy_null_frozenset_ #null_tuple,null_iter,null_frozenset
#.#################################
#.from seed.helper.lazy_import__func import force_lazy_imported_func_ # lazy_import4func_, lazy_import4funcs_
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
#.with mk_ctx4lazy_import4funcs_(__name__, 'ifNone:_ifNone, ifNonef:_ifNonef'):
#.    from seed.helper.ifNone import ifNone as _ifNone, ifNonef as _ifNonef
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.helper.repr_input import repr_helper
    from seed.debug.print_err import print_err
    from seed.debug.expectError import expectError
#.    from seed.tiny_.map_ import map_, cmap_, call_, prepare4call_, dots_
#.    from seed.tiny_.types5py import mk_MapView,curry1,kwargs2Attrs #,MapView
#.    from seed.tiny_.containers import mk_tuple,mk_immutable_seq,mk_immutable_seq5iterT_,mk_immutable_seq5iter__,mk_bytes5iter_,mk_tuple__split_first_if_str,mk_tuple__split_first_if_str__sep_ #xxx:null_tuple
#.    from seed.helper.ifNone import ifNone,ifNonef
#.    from seed.tiny_.funcs import echo,fst,snd
#.    from seed.types.Either import mk_Left,mk_Right #Either,Cased
#.    from seed.iters.flatten_recur import flatten_recur
#.    # def flatten_recur(g:Generator, /, *, value:object=None, is_exc=False, boxed=False):
#.    from seed.func_tools.dot_ import dot_
#.    from seed.iters.PeekableIterator import echo_or_mk_PeekableIterator
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


r'''[[[

grep -r '\<cfg8scene\>[.]\w\+'  ../../python3_src/seed/recognize/step_recognizer/IStepRecognizer.py -o | sort -u
cfg8scene.env8bg
cfg8scene.kps8oc

    ++ops8pc

grep -r '\<env8bg\>[.]\w\+'  ../../python3_src/seed/recognize/step_recognizer/IStepRecognizer.py -o | sort -u
env8bg.ops4kps8oc
env8bg.ops4lookup
env8bg.ops4tsmapping
env8bg.ops4rope
env8bg.ops4eoxst

    ++ops8pc.ops4tkn

grep -r '\<ops\w*\>[.]\w\+'  ../../python3_src/seed/recognize/step_recognizer/IStepRecognizer.py -o | sort -u
ops4kps8oc.access_
ops4kps8oc.offset_
ops4kps8oc.union_
ops4lookup.name2rgnr_
ops4tsmapping.get_empty_mapping_
ops4tsmapping.select_
ops4tsmapping.update_
ops4rope.len_
ops4rope.get_empty_rope_
ops4eoxst.get_payload6st7CALL_
ops4eoxst.mk_eoxst__CALL_
ops4eoxst.mk_eoxst__OK_

xxx:ops4tsmapping.mk_key_set_
xxx:ops4rope.append_
xxx:ops4rope.append__via_join_
_extract_

#]]]'''#'''

Case4join4serial_rgnr = Enum('Case4join4serial_rgnr', 'DISCARD  PACK  UNPACK')

class IOperations4token(ABC):
    'ops4tkn'
    __slots__ = ()
    ##############
    #impure{anchored;position_dependent}:
    ##############
    @property
    @abstractmethod
    def may_tkn2begin_position_info_(sf, /):
        '-> may (token -> begin_position_info)'
    @property
    @abstractmethod
    def may_tkn2end_position_info_(sf, /):
        '-> may (token -> end_position_info)'
    ##############


    ##############
    #ctx_sensitive:
    ##############
    @property
    @abstractmethod
    def may_tkn2tdat_(sf, /):
        '-> may (token -> tdat)'
    ##############


    ##############
    #pure{unanchored;position_independent}&&ctx_free:
    ##############
    @property
    @abstractmethod
    def may_tkn2tkey_(sf, /):
        '-> may (token -> tkey)'
    @property
    @abstractmethod
    def may_tkn2sub_tkey_(sf, /):
        '-> may (token -> sub_tkey)'
    @property
    @abstractmethod
    def may_tkn2super_tkey_(sf, /):
        '-> may (token -> super_tkey)'
    ##############
    may_tkn2begin_position_info_
    may_tkn2end_position_info_
    may_tkn2tdat_
    may_tkn2tkey_
    may_tkn2sub_tkey_
    may_tkn2super_tkey_


    ##############
    # :.,.+6s/^\(    \)\(may_\(\w*\)\)$/\1@property\r\1def \3(sf, \/):\r\1\1m = sf.\2\r\1\1if m is None:raise AttributeError('\3')\r\1\1return m
    @property
    def tkn2begin_position_info_(sf, /):
        m = sf.may_tkn2begin_position_info_
        if m is None:raise AttributeError('tkn2begin_position_info_')
        return m
    @property
    def tkn2end_position_info_(sf, /):
        m = sf.may_tkn2end_position_info_
        if m is None:raise AttributeError('tkn2end_position_info_')
        return m
    @property
    def tkn2tdat_(sf, /):
        m = sf.may_tkn2tdat_
        if m is None:raise AttributeError('tkn2tdat_')
        return m
    @property
    def tkn2tkey_(sf, /):
        m = sf.may_tkn2tkey_
        if m is None:raise AttributeError('tkn2tkey_')
        return m
    @property
    def tkn2sub_tkey_(sf, /):
        m = sf.may_tkn2sub_tkey_
        if m is None:raise AttributeError('tkn2sub_tkey_')
        return m
    @property
    def tkn2super_tkey_(sf, /):
        m = sf.may_tkn2super_tkey_
        if m is None:raise AttributeError('tkn2super_tkey_')
        return m
    ##############
    tkn2begin_position_info_
    tkn2end_position_info_
    tkn2tdat_
    tkn2tkey_
    tkn2sub_tkey_
    tkn2super_tkey_
    ##############
class IOperations4ExState4StepRecognizer(ABC):
    'ops4eoxst'
    __slots__ = ()
    @abstractmethod
    def get_payload6st7LOOP_(sf, st7LOOP, /):
        'st{LOOP} -> payload4st'
    @abstractmethod
    def get_payload6st7CALL_(sf, st7CALL, /):
        'st{CALL} -> payload4st'
    @abstractmethod
    def mk_eoxst__CALL_(sf, payload4st4parent_rgnr, key4branch7child, child_rgnr, params8partialID4child, selected_kwds6ctx8fg4child, kps8oc4child, /):
        'payload4st{parent_rgnr} -> key4branch{st{parent}->child} -> child_rgnr -> params8partialID{child} -> selected_kwds6ctx8fg{child} -> kps8oc{child} -> eoxst{CALL}'
    @abstractmethod
    def mk_eoxst__LOOP_(sf, payload4st4rgnr, /):
        'payload4st{rgnr} -> eoxst{LOOP}'
    @abstractmethod
    def mk_eoxst__OK_(sf, wrapped_oresult, /):
        'wrapped_oresult/(rope|boxed) -> eoxst{OK}'
    @abstractmethod
    def mk_eoxst__ERR_(sf, case4err, payload4err, lazy_msg4err, neg_idx4tkn4err:-1, /):
        'case4err -> payload4err -> lazy_msg4err -> neg_idx4tkn4err -> eoxst{ERR}'
    get_payload6st7CALL_#st?eoxst?
    mk_eoxst__CALL_
    mk_eoxst__OK_
class IOperations4FrozenTreeStyleSequential(ABC):
    'ops4tsseq'
    __slots__ = ()
class IOperations4FrozenRope(ABC):
    'ops4rope # [rope :: Rope<Boxed<x>>]'
    __slots__ = ()
    #.@abstractmethod
    #.def append_(sf, x, rope/):
    #.    'x -> rope -> rope'
    #.append_
    #.@abstractmethod
    #.def append__via_join_(sf, case4join, wrapped_oresult, rope, /):
    #.    'Case4join4serial_rgnr -> wrapped_oresult -> rope -> rope'
    @abstractmethod
    def len_(sf, rope, /):
        'rope -> uint'
    @abstractmethod
    def get_empty_rope_(sf, /):
        '-> empty_rope'

    @abstractmethod
    def is_rope_(sf, x, /):
        'obj -> bool'
    @abstractmethod
    def is_boxed_(sf, x, /):
        'obj -> bool'
    @abstractmethod
    def rope2tuple__unboxed_all_elements_(sf, rope, /):
        'Rope<Boxed<x>> -> tuple<x>'
    @abstractmethod
    def mk_boxed_(sf, x, /):
        'x -> Boxed<x>'
    @abstractmethod
    def append__boxed_(sf, boxed, rope, /):
        'Boxed<x> -> Rope<Boxed<x>> -> Rope<Boxed<x>> # => (rope++[boxed])'
    @abstractmethod
    def concat_ropes_(sf, ropes, /):
        'Iter<Rope<Boxed<x>>> -> Rope<Boxed<x>>'

    #xxx:append_
    #xxx:_extract_
    #xxx:append__via_join_
    len_
    get_empty_rope_

    is_rope_
    is_boxed_
    rope2tuple__unboxed_all_elements_
    mk_boxed_
    append__boxed_
    concat_ropes_
def check_wrapped_(ops4rope, wrapped_oresult, /):
    if not (ops4rope.is_rope_(wrapped_oresult) or ops4rope.is_boxed_(wrapped_oresult)):raise TypeError
def check_rope_(ops4rope, wrapped_oresult, /):
    if not ops4rope.is_rope_(wrapped_oresult):raise TypeError
def check_boxed_(ops4rope, wrapped_oresult, /):
    if not ops4rope.is_boxed_(wrapped_oresult):raise TypeError
def rope2boxed_tuple__unboxed_all_elements_(ops4rope, rope, /):
    'ops4rope -> rope/Rope<Boxed<x>> -> boxed/Boxed<tuple<x>>'
    xs = ops4rope.rope2tuple__unboxed_all_elements_(rope)
    boxed = ops4rope.mk_boxed_(xs)
    return boxed
def wrapped_oresult2boxed_oresult_(ops4rope, wrapped_oresult, /):
    'ops4rope -> wrapped_oresult/(Rope<Boxed<x>>|Boxed<y>) -> boxed_oresult/(Boxed<tuple<x>>|Boxed<y>)'
    if ops4rope.is_boxed_(wrapped_oresult):
        oresult7boxed = wrapped_oresult
    elif ops4rope.is_rope_(wrapped_oresult):
        oresult7rope = wrapped_oresult
        oresult7boxed = rope2boxed_tuple__unboxed_all_elements_(ops4rope, oresult7rope)
    else:
        raise 000
    oresult7boxed
    return oresult7boxed
def append__via_join_(ops4rope, case4join, wrapped_oresult, rope, /):
    'ops4rope -> Case4join4serial_rgnr -> wrapped_oresult -> rope -> rope'
    check_wrapped_(ops4rope, wrapped_oresult)
    check_rope_(ops4rope, rope)
    match case4join:
        case Case4join4serial_rgnr.DISCARD:
            rope7updated = rope
        case Case4join4serial_rgnr.PACK:
            boxed_oresult = wrapped_oresult2boxed_oresult_(ops4rope, wrapped_oresult)
            rope7updated = ops4rope.append__boxed_(boxed_oresult, rope)
        case Case4join4serial_rgnr.UNPACK:
            if ops4rope.is_rope_(wrapped_oresult):
                oresult7rope = wrapped_oresult
                rope7updated = ops4rope.concat_ropes_([rope, oresult7rope])
            elif ops4rope.is_boxed_(wrapped_oresult):
                raise TypeError('UNPACK boxed')
            else:
                raise 000
            rope7updated
    rope7updated
    return rope7updated
class IOperations4FrozenTreeStyleMapping(ABC):
    'ops4tsmapping'
    __slots__ = ()
    @abstractmethod
    def get_empty_mapping_(sf, /):
        '-> empty_tsmapping'
    @abstractmethod
    def select_(sf, keys, tsmapping, /, *, to_mapping=False):
        'Iter key -> tsmapping -> (tsmapping if not to_mapping else mapping)'
    @abstractmethod
    def update_(sf, key2value, tsmapping, /):
        'key2value/{key:value} -> tsmapping -> tsmapping'
    @abstractmethod
    def delete_(sf, keys7delete, tsmapping, /):
        'keys/{key} -> tsmapping -> tsmapping'
    get_empty_mapping_
    select_
    update_
    delete_
    #xxx:mk_key_set_
class IOperations4lookup(ABC):
    'ops4lookup'
    __slots__ = ()
    @abstractmethod
    def name2rgnr_(sf, name4rgnr, /):
        'name{rgnr} -> rgnr'
    name2rgnr_
class IOperations4KeyPathSet8OutputControl(ABC):
    'ops4kps8oc'
    __slots__ = ()
    @abstractmethod
    def access_(sf, key, kps8oc, /):
        'key -> kps8oc -> inner_kps8oc'
    @abstractmethod
    def offset_(sf, offset, kps8oc, /):
        'offset -> kps8oc -> offsetted_kps8oc'
    @abstractmethod
    def union_(sf, lhs_kps8oc, rhs_kps8oc, /):
        'kps8oc -> kps8oc -> kps8oc'

    access_
    offset_
    union_
class IEnvironment8Background(ABC):
    'env8bg'
    __slots__ = ()
    @property
    @abstractmethod
    def ops4kps8oc(sf, /):
        '-> IOperations4KeyPathSet8OutputControl'
    @property
    @abstractmethod
    def ops4lookup(sf, /):
        '-> IOperations4lookup'
    @property
    @abstractmethod
    def ops4tsmapping(sf, /):
        '-> IOperations4FrozenTreeStyleMapping'
    @property
    @abstractmethod
    def ops4rope(sf, /):
        '-> IOperations4FrozenRope'
        #.'-> IOperations4FrozenTreeStyleSequential'
    @property
    @abstractmethod
    def ops4eoxst(sf, /):
        '-> IOperations4ExState4StepRecognizer'
    #########
    ops4kps8oc
    ops4lookup
    ops4tsmapping
    ops4rope
    ops4eoxst
    #########
class Flag4IOperations8PrivilegeControl(Flag):
    'flag4ops8pc{qualname8op} # see:IStepRecognizer._direct_required_ops8pc_()'
    # :.,.+6s/\(\w\+\)_$/flg_required__ops4tkn__\1 = 'ops4tkn.\0'
    # :.,.+6s/'.*'$/auto(\0)
    # :.,.+6s/auto('.*')$/auto() # \0
    flg_required__ops4tkn__tkn2begin_position_info = auto() # auto('ops4tkn.tkn2begin_position_info_')
    flg_required__ops4tkn__tkn2end_position_info = auto() # auto('ops4tkn.tkn2end_position_info_')
    flg_required__ops4tkn__tkn2tdat = auto() # auto('ops4tkn.tkn2tdat_')
    flg_required__ops4tkn__tkn2tkey = auto() # auto('ops4tkn.tkn2tkey_')
    flg_required__ops4tkn__tkn2sub_tkey = auto() # auto('ops4tkn.tkn2sub_tkey_')
    flg_required__ops4tkn__tkn2super_tkey = auto() # auto('ops4tkn.tkn2super_tkey_')
if 1:
    # :.,.+6s/\(\w\+\)_$/Flag4IOperations8PrivilegeControl.flg_required__ops4tkn__\1.path = 'ops4tkn.\0'
    Flag4IOperations8PrivilegeControl.flg_required__ops4tkn__tkn2begin_position_info.path = 'ops4tkn.tkn2begin_position_info_'
    Flag4IOperations8PrivilegeControl.flg_required__ops4tkn__tkn2end_position_info.path = 'ops4tkn.tkn2end_position_info_'
    Flag4IOperations8PrivilegeControl.flg_required__ops4tkn__tkn2tdat.path = 'ops4tkn.tkn2tdat_'
    Flag4IOperations8PrivilegeControl.flg_required__ops4tkn__tkn2tkey.path = 'ops4tkn.tkn2tkey_'
    Flag4IOperations8PrivilegeControl.flg_required__ops4tkn__tkn2sub_tkey.path = 'ops4tkn.tkn2sub_tkey_'
    Flag4IOperations8PrivilegeControl.flg_required__ops4tkn__tkn2super_tkey.path = 'ops4tkn.tkn2super_tkey_'

null_flag4ops8pc = Flag4IOperations8PrivilegeControl(0)
    #auto('...') => ^ValueError: 0 is not a valid Flag4IOperations8PrivilegeControl
if __name__ == "__main__":
    if 0b00001:print_err(null_flag4ops8pc)
        #auto() => Flag4IOperations8PrivilegeControl(0)
    if 0b00001:print_err(repr(null_flag4ops8pc))
        #auto() => <Flag4IOperations8PrivilegeControl: 0>
    if 0b00001:print_err(Flag4IOperations8PrivilegeControl.flg_required__ops4tkn__tkn2tkey)
        #auto() => Flag4IOperations8PrivilegeControl.flg_required__ops4tkn__tkn2tkey
    if 0b00001:print_err(repr(Flag4IOperations8PrivilegeControl.flg_required__ops4tkn__tkn2tkey))
        #auto() => <Flag4IOperations8PrivilegeControl.flg_required__ops4tkn__tkn2tkey: 8>
    if 0b00001:print_err(repr(Flag4IOperations8PrivilegeControl.flg_required__ops4tkn__tkn2tkey | Flag4IOperations8PrivilegeControl.flg_required__ops4tkn__tkn2tdat))
        #auto('...') => ^TypeError: unsupported operand type(s) for |: 'str' and 'str'
        #auto() => <Flag4IOperations8PrivilegeControl.flg_required__ops4tkn__tkn2tdat|flg_required__ops4tkn__tkn2tkey: 12>
    if 0b00001:print_err(repr(Flag4IOperations8PrivilegeControl.flg_required__ops4tkn__tkn2tkey & Flag4IOperations8PrivilegeControl.flg_required__ops4tkn__tkn2tdat))
        #auto() => <Flag4IOperations8PrivilegeControl: 0>
    if 0b00001:print_err(list(Flag4IOperations8PrivilegeControl.flg_required__ops4tkn__tkn2tkey | Flag4IOperations8PrivilegeControl.flg_required__ops4tkn__tkn2tdat))
        #auto() => [<Flag4IOperations8PrivilegeControl.flg_required__ops4tkn__tkn2tdat: 4>, <Flag4IOperations8PrivilegeControl.flg_required__ops4tkn__tkn2tkey: 8>]
    if 0b00000:
        #auto('...') => only allowed:0
        assert expectError(ValueError, lambda:Flag4IOperations8PrivilegeControl(1)) # only allowed:0
class IOperations8PrivilegeControl(ABC):
    'ops8pc'
    __slots__ = ()
    @property
    @abstractmethod
    def ops4tkn(sf, /):
        '-> IOperations4token'
    #########
    ops4tkn
    #########

class IKeyPathSet8OutputControl(ABC):
    'kps8oc#user_defined#cfg8scene.env8bg.ops4kps8oc should support at least three special instances:{kps8oc__ignore,kps8oc__whole,kps8oc__lazy_whole}'
    __slots__ = ()
    @abstractmethod
    def access_(sf, key, /):
        'key -> inner_kps8oc'
    @abstractmethod
    def offset_(sf, offset, /):
        'offset/uint -> offsetted_kps8oc'
    @abstractmethod
    def __or__(sf, rhs_kps8oc, /):
        'kps8oc -> kps8oc|NotImplemented'
    def __ror__(sf, lhs_kps8oc, /):
        'kps8oc -> kps8oc|NotImplemented'
        return sf.__or__(lhs_kps8oc)
class KeyPathSet8OutputControl__whole(IKeyPathSet8OutputControl):
    'kps8oc__whole'
    #require all granted
    __slots__ = ()
    def __repr__(sf, /):
        return 'kps8oc__whole'
    @override
    def access_(sf, key, /):
        'key -> inner_kps8oc'
        return sf
    @override
    def offset_(sf, offset, /):
        'offset/uint -> offsetted_kps8oc'
        return sf
    @override
    def __or__(sf, rhs_kps8oc, /):
        'kps8oc -> kps8oc|NotImplemented'
        return sf
class KeyPathSet8OutputControl__lazy_whole(IKeyPathSet8OutputControl):
    'kps8oc__lazy_whole'
    __slots__ = ()
    def __repr__(sf, /):
        return 'kps8oc__lazy_whole'
    @override
    def access_(sf, key, /):
        'key -> inner_kps8oc'
        return sf
    @override
    def offset_(sf, offset, /):
        'offset/uint -> offsetted_kps8oc'
        return sf
    @override
    def __or__(sf, rhs_kps8oc, /):
        'kps8oc -> kps8oc|NotImplemented'
        return NotImplemented
        return sf
class KeyPathSet8OutputControl__ignore(IKeyPathSet8OutputControl):
    'kps8oc__ignore'
    __slots__ = ()
    def __repr__(sf, /):
        return 'kps8oc__ignore'
    @override
    def access_(sf, key, /):
        'key -> inner_kps8oc'
        return sf
    @override
    def offset_(sf, offset, /):
        'offset/uint -> offsetted_kps8oc'
        return sf
    @override
    def __or__(sf, rhs_kps8oc, /):
        'kps8oc -> kps8oc|NotImplemented'
        return rhs_kps8oc
kps8oc__ignore = KeyPathSet8OutputControl__ignore()
kps8oc__whole = KeyPathSet8OutputControl__whole()
kps8oc__lazy_whole = KeyPathSet8OutputControl__lazy_whole()

class IConfiguration8Scene(ABC):
    'cfg8scene'
    __slots__ = ()
    #named_tuple
    @property
    @abstractmethod
    def env8bg(sf, /):
        '-> IEnvironment8Background'
    @property
    @abstractmethod
    def ops8pc(sf, /):
        '-> IOperations8PrivilegeControl'
    @property
    @abstractmethod
    def kps8oc(sf, /):
        '-> IKeyPathSet8OutputControl'

Case4eoxst4rgnr = Enum('Case4eoxst4rgnr', 'OK  ERR  LOOP CALL')
if 0:
    class IExState4StepRecognizer(ABC):
        'eoxst#user_defined#cfg8scene.env8bg.ops4eoxst'
        __slots__ = ()
#.class IExState4StepRecognizer(ABC):
#.    'eoxst'
#.    __slots__ = ()
#.    @property
#.    @abstractmethod
#.    def stopped(sf, /):
#.        '-> bool'
#.    #.@property
#.    #.@abstractmethod
#.    #.def case4eoxst(sf, /):
#.    #.    '-> Case4eoxst4rgnr'
#.
#.    @property
#.    @abstractmethod
#.    def st_or_eresult(sf, /):
#.        '-> (st if not .stopped else wrapped_eresult)'
#.    def __iter__(sf, /):
#.        yield sf.stopped
#.        yield sf.st_or_eresult
#.class IState4StepRecognizer(ABC):
#.    'st'
#.    __slots__ = ()
#.    [st == ((LOOP, payload4st{sf})|(CALL, payload4st{sf}, key4branch, child_rgnr, params8partialID{child_rgnr}, selected_kwds6ctx8fg{child_rgnr}, kps8oc))]
#.class IEResult4StepRecognizer(ABC):
#.    'eresult # not wrapped_eresult'
#.    __slots__ = ()
#.    [eresult = ((OK, wrapped_oresult)|(ERR, case4err, payload4err, lazy_msg4err, neg_idx4tkn4err:=-1))]
#.    [wrapped_oresult :: (rope|boxed)]
#.    [rope == [(rope|boxed)]]
#.    [boxed a == (Just a|Lazy a)]
#.    [Lazy a == () -> cached a]
#.    [Just a == (a,)]
#.
#.


def mk_null_iter_(sf, /):
    return;yield
class IInfoCollector(ABC):
    __slots__ = ()
    @abstractmethod
    def _iter_info_collector_children_(sf, /):
        '-> Iter IInfoCollector'
        #, name2info_collector_
    @abstractmethod
    def _iter_info_collector_child_names_(sf, /):
        '-> Iter name{IInfoCollector}'





class IStepRecognizer(IInfoCollector):
    r'''[[[
    step_recognizer

    consumed - whether the feeding token be consumed. used to support LL1.
    cfg8scene - configuration as scene
    env8bg - environment as background
    ops8pc - operations as privilege control
    kps8oc - key/attribute/access path set as output control
    ctx8fg - context as foreground
    selected_kwds6ctx8fg - kwargs selected from ctx8fg
        if not selected_kwds6ctx8fg is empty mapping:this rgnr will be treated as unhashable (ie:no unifying or unified by id())
    params8partialID - if selected_kwds6ctx8fg is empty_tsmapping, then (rgnr, params8partialID) form an hashable ID{under cfg8scene}

    [cfg8scene = (env8bg, ops8pc, kps8oc)]
    [eoxst :: (Either st eresult)]
    [eresult = ((OK, wrapped_oresult)|(ERR, case4err, payload4err, lazy_msg4err, neg_idx4tkn4err:=-1))]
    [wrapped_oresult :: (rope|boxed)]
    [rope == [(rope|boxed)]]
    [boxed a == (Just a|Lazy a)]
    [Lazy a == () -> cached a]
    [Just a == (a,)]
    [st == ((LOOP, payload4st{sf})|(CALL, payload4st{sf}, key4branch, child_rgnr, params8partialID{child_rgnr}, selected_kwds6ctx8fg{child_rgnr}, kps8oc{child_rgnr}))]
        #xxx:selected_keys6ctx8fg
        # [conceptual_complete_state{rgnr} == (cfg8scene{env8bg;ops8pc,kps8oc};cfg4rgnr{selected_kwds6ctx8fg};st)]
    [consumed :: bool]

    #]]]'''#'''
    __slots__ = ()
    #.@property
    #.@abstractmethod
    #.def selected_keys6ctx8fg(sf, /):
    #.    '-> {key}'
    #.@property
    #.@abstractmethod
    #.def to_mk_new_ctx8serial_scope(sf, /):
    #.    '-> bool'
    @property
    @abstractmethod
    def _direct_required_ops8pc_(sf, /):
        '-> flag4ops8pc{qualname8op}/Flag4IOperations8PrivilegeControl # ++descendant{ops4lookup} => required_ops8pc{sf} #see:ops8pc'
        #'-> {qualname8op} # ++descendant{ops4lookup} => required_ops8pc{sf} #see:ops8pc'
    @abstractmethod
    def mk_cfg4rgnr_(sf, cfg8scene, params8partialID, selected_kwds6ctx8fg, /):
        '-> cfg4rgnr'
    @abstractmethod
    def start_recognize_(sf, cfg8scene, cfg4rgnr, /):
        '-> Iter eoxst'
    @abstractmethod
    def feed__token_(sf, cfg8scene, cfg4rgnr, st, token, /):
        '-> Iter (consumed, eoxst)'
    @abstractmethod
    def feed__oresult_(sf, cfg8scene, cfg4rgnr, st, key4branch, kps8oc4child, wrapped_oresult7subcall, /):
        '-> Iter eoxst'

def neednot__feed__token_(sf, cfg8scene, cfg4rgnr, st, token, /):
    '-> Iter (consumed, eoxst)'
    '-> Iter eoxst'
    raise 000
#repeater_relay
def relay__feed__oresult_(sf, cfg8scene, cfg4rgnr, st, key4branch, kps8oc4child, wrapped_oresult7subcall, /):
    '-> Iter eoxst'
    ops4eoxst = cfg8scene.env8bg.ops4eoxst
    yield ops4eoxst.mk_eoxst__OK_(wrapped_oresult7subcall)
def save__mk_cfg4rgnr_(sf, cfg8scene, params8partialID, selected_kwds6ctx8fg, /):
    '-> cfg4rgnr'
    cfg4rgnr = (params8partialID, selected_kwds6ctx8fg)
    return cfg4rgnr

class IStepRecognizer__wrapper(IStepRecognizer):
    __slots__ = ()
    @abstractmethod
    def get_the_wrapped_rgnr_(sf, /):
        '-> the_wrapped_rgnr'

    @override
    def _iter_info_collector_children_(sf, /):
        '-> Iter IInfoCollector'
        yield sf.get_the_wrapped_rgnr_()
    #@override
    _iter_info_collector_child_names_ = mk_null_iter_

    #@override
    _direct_required_ops8pc_ = null_flag4ops8pc

    #@override
    mk_cfg4rgnr_ = save__mk_cfg4rgnr_
    #@override
    feed__token_ = neednot__feed__token_
    #@override
    feed__oresult_ = relay__feed__oresult_
    @override
    def start_recognize_(sf, cfg8scene, cfg4rgnr, /):
        '-> Iter eoxst'
        (params8partialID, selected_kwds6ctx8fg) = cfg4rgnr
        wrapped_rgnr = sf.get_the_wrapped_rgnr_()
        kps8oc = cfg8scene.kps8oc
        ops4eoxst = cfg8scene.env8bg.ops4eoxst
        payload4st4sf = None
        key4branch = None
        yield ops4eoxst.mk_eoxst__CALL_(payload4st4sf, key4branch, wrapped_rgnr, params8partialID, selected_kwds6ctx8fg, kps8oc)
class StepRecognizer__wrapper__rgnr_expr_with_repr(IStepRecognizer__wrapper):
    ___no_slots_ok___ = True
    def __init__(sf, rgnr_expr, qnm4mkr4rgnr_expr, /, *args4mkr4rgnr_expr, **kwds4mkr4rgnr_expr):
        check_type_le(IStepRecognizer, rgnr_expr)
        check_type_is(str, qnm4mkr4rgnr_expr)
        sf._rgnr = rgnr_expr
        sf._xs4repr = (qnm4mkr4rgnr_expr, args4mkr4rgnr_expr, kwds4mkr4rgnr_expr)
    @override
    def get_the_wrapped_rgnr_(sf, /):
        return sf._rgnr
    def __repr__(sf, /):
        (qnm4mkr4rgnr_expr, args4mkr4rgnr_expr, kwds4mkr4rgnr_expr) = sf._xs4repr
        return repr_helper(qnm4mkr4rgnr_expr, *args4mkr4rgnr_expr, **kwds4mkr4rgnr_expr)

class IStepRecognizer__named(IStepRecognizer):
    __slots__ = ()
    @property
    @abstractmethod
    def name4rgnr(sf, /):
        '-> name{sf}'
class IStepRecognizer__named_wrapper(IStepRecognizer__wrapper):
    __slots__ = ()
#xxx:env8bg.ops4lookup:class IStepRecognizer__ref(IStepRecognizer__wrapper):
class IStepRecognizer__ref(IStepRecognizer):
    __slots__ = ()
    @property
    @abstractmethod
    def name4referred_rgnr(sf, /):
        '-> name{referred_rgnr}'
    def derefer_(sf, env8bg, /):
        '-> referred_rgnr'
        #def lookup_the_referred_rgnr_(sf, env8bg, /):
        referred_rgnr = env8bg.ops4lookup.name2rgnr_(sf.name4referred_rgnr)
        return referred_rgnr

    #@override
    _iter_info_collector_children_ = mk_null_iter_
        #derefer_:require env8bg ==>> access via:_iter_info_collector_child_names_()
    @override
    def _iter_info_collector_child_names_(sf, /):
        '-> Iter name{IInfoCollector}'
        yield sf.name4referred_rgnr

    #@override
    _direct_required_ops8pc_ = null_flag4ops8pc


    #@override
    mk_cfg4rgnr_ = save__mk_cfg4rgnr_
    #@override
    feed__token_ = neednot__feed__token_
    #@override
    feed__oresult_ = relay__feed__oresult_
    @override
    def start_recognize_(sf, cfg8scene, cfg4rgnr, /):
        '-> Iter eoxst'
        (params8partialID, selected_kwds6ctx8fg) = cfg4rgnr
        referred_rgnr = sf.derefer_(cfg8scene.env8bg)
        kps8oc = cfg8scene.kps8oc
        ops4eoxst = cfg8scene.env8bg.ops4eoxst
        payload4st4sf = None
        key4branch = None
        yield ops4eoxst.mk_eoxst__CALL_(payload4st4sf, key4branch, referred_rgnr, params8partialID, selected_kwds6ctx8fg, kps8oc)


######################
class IStepRecognizer__parallel(IStepRecognizer):
    __slots__ = ()
    @property
    @abstractmethod
    def _child_rgnr_seq4parallel_rgnr_(sf, /):
        '-> [child_rgnr]'
    #.@abstractmethod
    #.def _iter_tagged_child_rgnrs_(sf, /):
    #.    '-> Iter (tag, child_rgnr)'
    #.#@override
    #.to_mk_new_ctx8serial_scope = False
    #@override
    feed__token_ = neednot__feed__token_
    #@override
    feed__oresult_ = relay__feed__oresult_
    #@override
    mk_cfg4rgnr_ = save__mk_cfg4rgnr_
        #.for tag, child_rgnr in sf._iter_tagged_child_rgnrs_():
        #.    _selected_kwds6ctx8fg = _select(child_rgnr.selected_kwds6ctx8fg, selected_kwds6ctx8fg)
        #.cfgs = []
        #.for child_rgnr in sf._child_rgnr_seq4parallel_rgnr_:
        #.    cfg4child_rgnr = child_rgnr.mk_cfg4rgnr_(cfg8scene, params8partialID, selected_kwds6ctx8fg)
        #.    cfgs.append(cfg4child_rgnr)
        #.cfgs
        #.cfg4rgnr = tuple(cfgs)
        #.return cfg4rgnr
    @override
    def start_recognize_(sf, cfg8scene, cfg4rgnr, /):
        '-> Iter eoxst'
        (params8partialID, selected_kwds6ctx8fg) = cfg4rgnr
        kps8oc = cfg8scene.kps8oc
        ops4eoxst = cfg8scene.env8bg.ops4eoxst
        selected_kwds6ctx8fg4child = selected_kwds6ctx8fg
        kps8oc4child = kps8oc
        payload4st4sf = None
        key4branch = None
        for child_rgnr in sf._child_rgnr_seq4parallel_rgnr_:
            yield ops4eoxst.mk_eoxst__CALL_(payload4st4sf, key4branch, child_rgnr, params8partialID, selected_kwds6ctx8fg4child, kps8oc4child)
        return
        #.ops4tsmapping = cfg8scene.env8bg.ops4tsmapping
        #.selected_keys6ctx8fg = ops4tsmapping.mk_key_set_(selected_kwds6ctx8fg)
            #.yield ops4eoxst.mk_eoxst__CALL_(payload4st4sf, key4branch, child_rgnr, params8partialID, selected_keys6ctx8fg, kps8oc)
        ###
        #.assert len(cfg4rgnr) == len(sf._child_rgnr_seq4parallel_rgnr_)
        #.for child_rgnr, cfg4child_rgnr in zip(sf._child_rgnr_seq4parallel_rgnr_, cfg4rgnr):


######################
class IAsbeItem4flow_rgnr(ABC):
    'asbe_item4flow_rgnr #used by IStepRecognizer__flow'
    __slots__ = ()
    @property
    @abstractmethod
    def tuple_as_item4flow_rgnr(sf, /):
        '-> item4flow_rgnr/(child_rgnr, args_kwds_selector, mkr4kps8oc4child, extractor, keys7update, keys7delete, may_updater_pair4partial_oresult_and_shifted_kps8oc)'
class IStepRecognizer__flow(IStepRecognizer):
    r'''[[[
    [item4flow_rgnr == (child_rgnr, args_kwds_selector, mkr4kps8oc4child, extractor, keys7update, keys7delete, may_updater_pair4partial_oresult_and_shifted_kps8oc)]
    [args_kwds_selector :: cfg8scene -> payload4cfg4flow_rgnr -> ctx4flow_rgnr -> child_rgnr -> (params8partialID{child_rgnr}, selected_kwds6ctx8fg{child_rgnr})]
        payload4cfg4flow_rgnr - user_defined
    [mkr4kps8oc4child :: env8bg -> child_rgnr -> shifted_kps8oc -> kps8oc4child]
    [extractor :: cfg8scene -> ctx4flow_rgnr -> expt6flowchart -> key4branch -> exjmpstep4next -> keys7update -> kps8oc4child -> wrapped_oresult7subcall -> (modifier4shifted_kps8oc, wrapped_oresult7child, patch4ctx4flow_rgnr)]
    [patch4ctx4flow_rgnr :: [value]{len==len(keys7update)}]
        #xxx:[patch4ctx4flow_rgnr :: {key:value}]
        # keys7update&patch4ctx4flow_rgnr --> update ctx4flow_rgnr
        #   ; then keys7delete --> clean ctx4flow_rgnr
    [may_updater_pair4partial_oresult_and_shifted_kps8oc :: may (updater4partial_oresult, updater4shifted_kps8oc)]
    [updater4partial_oresult :: (env8bg -> wrapped_oresult7child -> partial_oresult -> partial_oresult7updated)]
        # update partial_oresult or ignore wrapped_oresult7child
    [updater4shifted_kps8oc :: (env8bg -> modifier4shifted_kps8oc -> shifted_kps8oc -> shifted_kps8oc7updated)]




    [_check_input4flow_rgnr_ :: cfg8scene -> params8partialID{flow_rgnr} -> selected_kwds6ctx8fg{flow_rgnr} -> None|^Exception]
    [_mk_payload4cfg4flow_rgnr_ :: cfg8scene -> params8partialID -> selected_kwds6ctx8fg -> payload4cfg4flow_rgnr]
    [_mk_init_ctx4flow_rgnr_ :: cfg8scene -> params8partialID -> selected_kwds6ctx8fg{flow_rgnr} -> ctx4flow_rgnr{initial}]
        #xxx:[ctx4flow_rgnr{initial} := selected_kwds6ctx8fg{flow_rgnr}]

    [_mk_init_partial_oresult4flow_rgnr_ :: cfg8scene -> params8partialID -> selected_kwds6ctx8fg -> partial_oresult{initial}]
    [_mk_entry_point4flowchart4flow_rgnr_ :: cfg8scene -> params8partialID -> selected_kwds6ctx8fg -> expt6flowchart]
        [expt6flowchart ~=~ (acc_st4flowchart, pt6flowchart)]
        expt6flowchart - extended-point{flowchart}
        pt6flowchart - point{flowchart}
    [_test_final_dead_expt6flowchart4flow_rgnr_:: expt6flowchart -> (b_final,b_dead)/(bool,bool)]
        [_is_final_expt6flowchart4flow_rgnr_:: expt6flowchart -> bool]
        [_is_dead_expt6flowchart4flow_rgnr_:: expt6flowchart -> bool]
    [_enumerate_keyed_branch6flowchart4flow_rgnr_ :: cfg8scene -> expt6flowchart{alive} -> Iter (key4branch, branch)]
        # [return null_iter] <==> [dead expt6flowchart]
    [_get_branch6flowchart4flow_rgnr_ :: cfg8scene -> expt6flowchart{alive} -> key4branch -> branch]
    [_mk_next_expt6flowchart4flow_rgnr_ :: expt6flowchart{alive,nondead} -> key4branch -> exjmpstep4next -> expt6flowchart{flow_rgnr}{next}]

    [asbe_item4flow_rgnr :: IAsbeItem4flow_rgnr]
    [branch :: may (asbe_item4flow_rgnr, exjmpstep4next)]
    [branch:None/return/end]

    [_mk_wrapped_oresult4flow_rgnr_ :: cfg8scene -> expt6flowchart{final} -> tmay_key4branch -> partial_oresult -> wrapped_oresult4flow_rgnr]
        [_mk_wrapped_oresult4flow_rgnr_ :: cfg8scene -> expt6flowchart{final} -> () -> partial_oresult -> wrapped_oresult4flow_rgnr]
        [_mk_wrapped_oresult4flow_rgnr_ :: cfg8scene -> expt6flowchart{alive} -> (key4branch{branch be None},) -> partial_oresult -> wrapped_oresult4flow_rgnr]

    [st{flow_rgnr} == (ctx4flow_rgnr, partial_oresult, expt6flowchart)]


    #]]]'''#'''
    'limit ctx usage:ctx is only used under single flow layer control, ie, the only ctx updater is flow_rgnr # abandon scheme that return ctx'
    __slots__ = ()
    @abstractmethod
    def _mk_entry_point4flowchart4flow_rgnr_(sf, cfg8scene, params8partialID, selected_kwds6ctx8fg, /):
        '-> entry_point{flowchart4flow_rgnr}/expt6flowchart'
    @abstractmethod
    def _test_final_dead_expt6flowchart4flow_rgnr_(sf, expt6flowchart, /):
        '-> (b_final,b_dead)/(bool{whether to yield output}, bool{whether to stop flowing})'
    @abstractmethod
    def _enumerate_keyed_branch6flowchart4flow_rgnr_(sf, cfg8scene, expt6flowchart7alive, /):
        '-> Iter (key4branch, branch){flowchart4flow_rgnr} # [return null_iter] <==> [dead expt6flowchart]'
    @abstractmethod
    def _get_branch6flowchart4flow_rgnr_(sf, cfg8scene, expt6flowchart7alive, key4branch, /):
        '-> branch{flowchart4flow_rgnr}/(may (asbe_item4flow_rgnr, exjmpstep4next))'
    @abstractmethod
    def _mk_next_expt6flowchart4flow_rgnr_(sf, curr_expt6flowchart7alive7nondead, key4branch, exjmpstep4next, /):
        '-> next_expt6flowchart{flow_rgnr}'
    @abstractmethod
    def _mk_wrapped_oresult4flow_rgnr_(sf, cfg8scene, expt6flowchart, tmay_key4branch, partial_oresult, /):
        '-> wrapped_oresult{flow_rgnr}'
    @abstractmethod
    def _mk_init_partial_oresult4flow_rgnr_(sf, cfg8scene, params8partialID, selected_kwds6ctx8fg, /):
        '-> partial_oresult{flow_rgnr}{initial}'
    @abstractmethod
    def _mk_init_ctx4flow_rgnr_(sf, cfg8scene, params8partialID, selected_kwds6ctx8fg, /):
        '-> ctx4flow_rgnr{flow_rgnr}{initial}'
    @abstractmethod
    def _mk_payload4cfg4flow_rgnr_(sf, cfg8scene, params8partialID, selected_kwds6ctx8fg, /):
        '-> payload4cfg4flow_rgnr{flow_rgnr}'
    @abstractmethod
    def _check_input4flow_rgnr_(sf, cfg8scene, params8partialID, selected_kwds6ctx8fg, /):
        '-> None|^Exception'

    def _is_final_expt6flowchart4flow_rgnr_(sf, expt6flowchart, /):
        '-> bool{whether to yield output}'
        (b_final,b_dead) = sf._test_final_dead_expt6flowchart4flow_rgnr_(expt6flowchart)
        return b_final
    def _is_dead_expt6flowchart4flow_rgnr_(sf, expt6flowchart, /):
        '-> alive_vs_dead/bool{whether to stop flowing}'
        (b_final,b_dead) = sf._test_final_dead_expt6flowchart4flow_rgnr_(expt6flowchart)
        return b_dead

    #@override
    feed__token_ = neednot__feed__token_
    #@override
    mk_cfg4rgnr_ = save__mk_cfg4rgnr_
    def mk_cfg4rgnr_(sf, cfg8scene, params8partialID, selected_kwds6ctx8fg, /):
        '-> cfg4rgnr'
        sf._check_input4flow_rgnr_(cfg8scene, params8partialID, selected_kwds6ctx8fg)
        payload4cfg4flow_rgnr = sf._mk_payload4cfg4flow_rgnr_(cfg8scene, params8partialID, selected_kwds6ctx8fg)
        ctx4flow_rgnr7initial = sf._mk_init_ctx4flow_rgnr_(cfg8scene, params8partialID, selected_kwds6ctx8fg)
        partial_oresult7initial = sf._mk_init_partial_oresult4flow_rgnr_(cfg8scene, params8partialID, selected_kwds6ctx8fg)
        expt6flowchart7initial = entry_point = sf._mk_entry_point4flowchart4flow_rgnr_(cfg8scene, params8partialID, selected_kwds6ctx8fg)
        kps8oc4sf = cfg8scene.kps8oc
        shifted_kps8oc7initial = kps8oc4sf
        #cfg4rgnr = (params8partialID, selected_kwds6ctx8fg)
        payload4st4sf7initial = (ctx4flow_rgnr7initial, partial_oresult7initial, shifted_kps8oc7initial, expt6flowchart7initial)
        cfg4rgnr = (payload4cfg4flow_rgnr, payload4st4sf7initial)
        return cfg4rgnr

    @override
    def start_recognize_(sf, cfg8scene, cfg4rgnr, /):
        '-> Iter eoxst'
        #(params8partialID, selected_kwds6ctx8fg) = cfg4rgnr
        (payload4cfg4flow_rgnr, payload4st4sf7initial) = cfg4rgnr
        payload4st4sf = payload4st4sf7initial
        #(ctx4flow_rgnr7initial, partial_oresult7initial, shifted_kps8oc7initial, expt6flowchart7initial) = payload4st4sf7initial
        #payload4st4sf = (ctx4flow_rgnr7curr, partial_oresult7curr, shifted_kps8oc7curr, expt6flowchart7curr) = (ctx4flow_rgnr7initial, partial_oresult7initial, shifted_kps8oc7initial, expt6flowchart7initial)
        return sf._iter_eoxsts4flow_rgnr(cfg8scene, payload4cfg4flow_rgnr, payload4st4sf)
    @override
    def feed__oresult_(sf, cfg8scene, cfg4rgnr, st, key4branch, kps8oc4child, wrapped_oresult7subcall, /):
        '-> Iter eoxst'
        env8bg = cfg8scene.env8bg
        ops4eoxst = env8bg.ops4eoxst
        ops4tsmapping = env8bg.ops4tsmapping
        ops4rope = env8bg.ops4rope
        (payload4cfg4flow_rgnr, payload4st4sf7initial) = cfg4rgnr
        payload4st4sf = ops4eoxst.get_payload6st7CALL_(st)
        (ctx4flow_rgnr7curr, partial_oresult7curr, shifted_kps8oc7curr, expt6flowchart7curr) = payload4st4sf

        if sf._is_dead_expt6flowchart4flow_rgnr_(expt6flowchart7curr): raise 000
        expt6flowchart7curr7alive = expt6flowchart7curr
        branch = sf._get_branch6flowchart4flow_rgnr_(cfg8scene, expt6flowchart7curr7alive, key4branch)
        if branch is None: raise 000
        (asbe_item4flow_rgnr, exjmpstep4next) = branch
        (child_rgnr, args_kwds_selector, mkr4kps8oc4child, extractor, keys7update, keys7delete, may_updater_pair4partial_oresult_and_shifted_kps8oc) = asbe_item4flow_rgnr.tuple_as_item4flow_rgnr
        #kps8oc4child = ???++input@feed__oresult_
        (modifier4shifted_kps8oc, wrapped_oresult7child, patch4ctx4flow_rgnr) = extractor(cfg8scene, ctx4flow_rgnr7curr, expt6flowchart7curr7alive, key4branch, exjmpstep4next, keys7update, kps8oc4child, wrapped_oresult7subcall)
        ctx4flow_rgnr7updated = _update_(env8bg, keys7update, keys7delete, patch4ctx4flow_rgnr, ctx4flow_rgnr7curr)
        #######
        if None is may_updater_pair4partial_oresult_and_shifted_kps8oc:
            # ignore child oresult
            del modifier4shifted_kps8oc
            del wrapped_oresult7child
            partial_oresult7updated = partial_oresult7curr
            shifted_kps8oc7updated = shifted_kps8oc7curr
        else:
            (updater4partial_oresult, updater4shifted_kps8oc) = may_updater_pair4partial_oresult_and_shifted_kps8oc
            partial_oresult7updated = updater4partial_oresult(env8bg, wrapped_oresult7child, partial_oresult7curr)
            shifted_kps8oc7updated = updater4shifted_kps8oc(env8bg, modifier4shifted_kps8oc, shifted_kps8oc7curr)
        partial_oresult7updated
        shifted_kps8oc7updated
        #######

        ctx4flow_rgnr7updated
        expt6flowchart7next = sf._mk_next_expt6flowchart4flow_rgnr_(expt6flowchart7curr7alive, key4branch, exjmpstep4next)
        payload4st4sf7updated = (ctx4flow_rgnr7updated, partial_oresult7updated, shifted_kps8oc7updated, expt6flowchart7next)
        return sf._iter_eoxsts4flow_rgnr(cfg8scene, payload4cfg4flow_rgnr, payload4st4sf7updated)

def _iter_eoxsts4flow_rgnr(sf, cfg8scene, payload4cfg4flow_rgnr, payload4st4sf, /):
    '-> Iter eoxst'
    ops4eoxst = cfg8scene.env8bg.ops4eoxst
    env8bg = cfg8scene.env8bg
        #ops4kps8oc = cfg8scene.env8bg.ops4kps8oc
    (ctx4flow_rgnr7curr, partial_oresult7curr, shifted_kps8oc7curr, expt6flowchart7curr) = payload4st4sf
    (b_final,b_dead) = sf._test_final_dead_expt6flowchart4flow_rgnr_(expt6flowchart7curr)
    if b_final:
        expt6flowchart7curr7final = expt6flowchart7curr
        777;tmay_key4branch = ()
        wrapped_oresult4flow_rgnr = sf._mk_wrapped_oresult4flow_rgnr_(cfg8scene, expt6flowchart7curr7final, tmay_key4branch, partial_oresult7curr)
        yield ops4eoxst.mk_eoxst__OK_(wrapped_oresult4flow_rgnr)
        pass
    else:
        pass

    if b_dead:
        return
    else:
        expt6flowchart7curr7alive = expt6flowchart7curr
        it = sf._enumerate_keyed_branch6flowchart4flow_rgnr_(cfg8scene, expt6flowchart7curr7alive)
        for (key4branch, branch) in it:
            if branch is None:
                777;tmay_key4branch = (key4branch,)
                wrapped_oresult4flow_rgnr = sf._mk_wrapped_oresult4flow_rgnr_(cfg8scene, expt6flowchart7curr7alive, tmay_key4branch, partial_oresult7curr)
                yield ops4eoxst.mk_eoxst__OK_(wrapped_oresult4flow_rgnr)
                continue
            (asbe_item4flow_rgnr, exjmpstep4next) = branch
            (child_rgnr, args_kwds_selector, mkr4kps8oc4child, extractor, keys7update, keys7delete, may_updater_pair4partial_oresult_and_shifted_kps8oc) = asbe_item4flow_rgnr.tuple_as_item4flow_rgnr
            (params8partialID4child, selected_kwds6ctx8fg4child) = args_kwds_selector(cfg8scene, payload4cfg4flow_rgnr, ctx4flow_rgnr7curr, child_rgnr)
            kps8oc4child = mkr4kps8oc4child(env8bg, child_rgnr, shifted_kps8oc7curr)
            yield ops4eoxst.mk_eoxst__CALL_(payload4st4sf, key4branch, child_rgnr, params8partialID4child, selected_kwds6ctx8fg4child, kps8oc4child)
        return
def _update_(env8bg, keys7update, keys7delete, patch4ctx4flow_rgnr, ctx4flow_rgnr7curr, /):
    if not len(patch4ctx4flow_rgnr) == len(keys7update):raise 000
    ops4tsmapping = env8bg.ops4tsmapping
    #bug:fresh_kwds = ops4tsmapping.select_(keys7update, ctx4flow_rgnr7curr, to_mapping=True)
    fresh_kwds = dict(zip(keys7update, patch4ctx4flow_rgnr))
    _ctx4flow_rgnr7halfway = ops4tsmapping.update_(fresh_kwds, ctx4flow_rgnr7curr)
    ctx4flow_rgnr7updated = ops4tsmapping.delete_(keys7delete, _ctx4flow_rgnr7halfway)
    return ctx4flow_rgnr7updated

######################
class IAsbeItem4serial_rgnr(IAsbeItem4flow_rgnr):
    'asbe_item4serial_rgnr #used by IStepRecognizer__serial'
    __slots__ = ()
    @property
    @abstractmethod
    def tuple_as_item4serial_rgnr(sf, /):
        '-> item4serial_rgnr/(child_rgnr, params8partialID{child_rgnr}, selected_keys6ctx8fg{child_rgnr}, case4join, kps8oc{later:child_rgnr}, key2getter)'
    @cached_property
    @override
    def tuple_as_item4flow_rgnr(sf, /):
        #.asbe_item4serial_rgnr_to_asbe_item4flow_rgnr_
        item4serial_rgnr = sf.tuple_as_item4serial_rgnr
        item4flow_rgnr = item4serial_rgnr_to_item4flow_rgnr_(item4serial_rgnr)
        return item4flow_rgnr
#.def asbe_item4serial_rgnr_to_asbe_item4flow_rgnr_(asbe_item4serial_rgnr, /):
#.    item4serial_rgnr = asbe_item4serial_rgnr.tuple_as_item4serial_rgnr
#.    item4flow_rgnr = item4serial_rgnr_to_item4flow_rgnr_(item4serial_rgnr)
#.    asbe_item4flow_rgnr = ???(item4flow_rgnr)
#.    return asbe_item4flow_rgnr
def item4serial_rgnr_to_item4flow_rgnr_(item4serial_rgnr, /):
    (child_rgnr, params8partialID4child, selected_keys6ctx8fg4child, case4join, kps8oc4later, key2getter) = item4serial_rgnr
    #######
    args_kwds_selector = _mk__args_kwds_selector(params8partialID4child, selected_keys6ctx8fg4child)
    mkr4kps8oc4child = _mk__mkr4kps8oc4child(case4join, kps8oc4later)
    extractor = _mk__extractor(case4join, key2getter)
    keys7update = tuple(key2getter)#sorted(key2getter)
    keys7delete = ()
    may_updater_pair4partial_oresult_and_shifted_kps8oc = _mk__may_updater_pair4partial_oresult_and_shifted_kps8oc(case4join)
    #######
    item4flow_rgnr = (child_rgnr, args_kwds_selector, mkr4kps8oc4child, extractor, keys7update, keys7delete, may_updater_pair4partial_oresult_and_shifted_kps8oc)
    return item4flow_rgnr
class AsbeItem4serial_rgnr__plain(IAsbeItem4serial_rgnr):
    ___no_slots_ok___ = True
    def __init__(sf, child_rgnr, params8partialID4child, selected_keys6ctx8fg4child, case4join, kps8oc4later, key2getter, /):
        sf._t = (child_rgnr, params8partialID4child, selected_keys6ctx8fg4child, case4join, kps8oc4later, key2getter)
        check_type_le(IStepRecognizer, child_rgnr)
        check_type_is(tuple, params8partialID4child)
        check_type_is(tuple, selected_keys6ctx8fg4child)
        check_type_is(Case4join4serial_rgnr, case4join)
        check_type_le(IKeyPathSet8OutputControl, kps8oc4later)
        check_type_le(IMapping, key2getter)
        check_type_le(IHashable, key2getter)
    @property
    @override
    def tuple_as_item4serial_rgnr(sf, /):
        return sf._t

#.class IAsbeExtPoint6flowchart(ABC):
#.    'expt6flowchart #used by IStepRecognizer__flow'
class IAsbeStatedPoint6flowchart(ABC):
    'asbe_stpt6flowchart #used by IStepRecognizer__serial__using_flow_fork_branch_scheme_AS_flowchart'
    #'[stpt6flowchart <: expt6flowchart] #used by IStepRecognizer__serial__using_flow_fork_branch_scheme_AS_flowchart'
    __slots__ = ()
    @property
    @abstractmethod
    def tuple_as_stpt6flowchart(sf, /):
        '-> stpt6flowchart/(acc_st4flowchart, pt6flowchart)'
class IAsbeStatedJmpStep6flowchart(ABC):
    'asbe_stjmpstep4next #used by IStepRecognizer__serial__using_flow_fork_branch_scheme_AS_flowchart'
    #'[stjmpstep4next <: exjmpstep4next] #used by IStepRecognizer__serial__using_flow_fork_branch_scheme_AS_flowchart'
    __slots__ = ()
    @property
    @abstractmethod
    def tuple_as_stjmpstep4next(sf, /):
        '-> stjmpstep4next/(delta_st4flowchart, jmpstep4next) # [delta_st4flowchart:see:acc_st4flowchart]'

class AsbeStatedPoint6flowchart__plain(IAsbeStatedPoint6flowchart):
    ___no_slots_ok___ = True
    def __init__(sf, acc_st4flowchart, pt6flowchart, /):
        sf._t = (acc_st4flowchart, pt6flowchart)
    @property
    @override
    def tuple_as_stpt6flowchart(sf, /):
        return sf._t
class AsbeStatedJmpStep6flowchart__plain(IAsbeStatedJmpStep6flowchart):
    ___no_slots_ok___ = True
    def __init__(sf, delta_st4flowchart, jmpstep4next, /):
        sf._t = (delta_st4flowchart, jmpstep4next)
    @property
    @override
    def tuple_as_stjmpstep4next(sf, /):
        return sf._t


TrueTrue = (True,True)
FalseFalse = (False,False)
class IStepRecognizer__serial(IStepRecognizer__flow):
    r'''[[[
    [case4join == (DISCARD|UNPACK|PACK)]
    [item4serial_rgnr == (child_rgnr, params8partialID{child_rgnr}, selected_keys6ctx8fg{child_rgnr}, case4join, kps8oc{later:child_rgnr}, key2getter)]
    [key2getter :: {key:getter5wrapped_oresult7subcall}]
    [getter5wrapped_oresult7subcall :: env8bg -> wrapped_oresult7subcall -> value]

    [asbe_item4serial_rgnr :: IAsbeItem4serial_rgnr <: IAsbeItem4flow_rgnr]
    [branch :: may (asbe_item4serial_rgnr, exjmpstep4next)]
    [branch:None/return/end]

    [expt6flowchart4flow_rgnr := may_expt6flowchart4serial_rgnr]


    * [not _may_calculator4next_acc_st4flowchart4serial_rgnr_ is None]:
        [expt6flowchart := asbe_stpt6flowchart]
        [asbe_stpt6flowchart :: IAsbeStatedPoint6flowchart]
        [stpt6flowchart == (acc_st4flowchart, pt6flowchart) == asbe_stpt6flowchart.tuple_as_stpt6flowchart]

        [exjmpstep4next := asbe_stjmpstep4next]
        [asbe_stjmpstep4next :: IAsbeStatedJmpStep6flowchart]
        [stjmpstep4next == (delta_st4flowchart, jmpstep4next) == asbe_stjmpstep4next.tuple_as_stjmpstep4next]
            # [delta_st4flowchart:see:acc_st4flowchart]

    * [_may_calculator4next_acc_st4flowchart4serial_rgnr_ is None]:
        [expt6flowchart := pt6flowchart]
        [exjmpstep4next := jmpstep4next]


    possible impl:
        IStepRecognizer__serial__using_flow_fork_branch_scheme_AS_flowchart

    #]]]'''#'''
    'limit ctx usage:ctx is only used under single serial layer control, ie, the only ctx updater is serial_rgnr # abandon scheme that return ctx'
    __slots__ = ()
    @property
    @abstractmethod
    def _entry_point4flowchart4serial_rgnr_(sf, /):
        '-> entry_point{flowchart4serial_rgnr}/may_expt6flowchart'
    @abstractmethod
    def _enumerate_keyed_branch6flowchart4serial_rgnr_(sf, expt6flowchart, /):
        '-> Iter (key4branch, branch){flowchart4serial_rgnr}'
    @abstractmethod
    def _get_branch6flowchart4serial_rgnr_(sf, expt6flowchart, key4branch, /):
        '-> branch{flowchart4serial_rgnr}/(may (asbe_item4serial_rgnr, exjmpstep4next))'
    @abstractmethod
    def _mk_may_next_expt6flowchart4serial_rgnr_(sf, curr_expt6flowchart, exjmpstep4next, /):
        '-> may_next_expt6flowchart'

    #########
    #MAYBE_USE:acc_st4flowchart
    #########
    @property
    @abstractmethod
    def _may_calculator4next_acc_st4flowchart4serial_rgnr_(sf, /):
        '-> may calculator4next_acc_st4flowchart/(delta_st4flowchart -> curr_acc_st4flowchart -> next_acc_st4flowchart) # [None => [exjmpstep4next:=jmpstep4next][expt6flowchart:=pt6flowchart]]'
        #for:IStepRecognizer__serial__array/many
    @property
    @abstractmethod
    def _may_tester4whether_final_dead_acc_st4flowchart4serial_rgnr_(sf, /):
        '-> may tester4whether_final_dead_acc_st4flowchart/(acc_st4flowchart -> (b_final,b_dead)/(bool,bool))'

    def _test_final_dead_acc_st4flowchart4flow_rgnr_(sf, acc_st4flowchart, /):
        m = sf._may_tester4whether_final_dead_acc_st4flowchart4serial_rgnr_
        if m is None:
            #default:nonfinal&&alive
            return FalseFalse
        tester4whether_final_dead_acc_st4flowchart = m
        (b_final,b_dead) = tester4whether_final_dead_acc_st4flowchart(acc_st4flowchart)
        #.check_type_is(bool, b_final)
        #.check_type_is(bool, b_dead)
        return (b_final,b_dead)
    def _expt2pt6flowchart4serial_rgnr_(sf, expt6flowchart, /):
        'expt6flowchart -> pt6flowchart'
        m = sf._may_calculator4next_acc_st4flowchart4serial_rgnr_
        no_acc_st = m is None
        #######
        if not no_acc_st:
            (acc_st4flowchart, pt6flowchart) = expt6flowchart.tuple_as_stpt6flowchart
        else:
            pt6flowchart = expt6flowchart
        pt6flowchart
        #######
        return pt6flowchart

    #########
    #API:IStepRecognizer__flow
    #########
    #.@override
    #.def _test_final_dead_expt6flowchart4flow_rgnr_(sf, expt6flowchart4flow_rgnr, /):
    #.    # !! may_expt6flowchart4serial_rgnr = expt6flowchart4flow_rgnr
    #.    may_expt6flowchart4serial_rgnr = expt6flowchart4flow_rgnr
    #.    return TrueTrue if None is may_expt6flowchart4serial_rgnr else FalseFalse
    @override
    def _test_final_dead_expt6flowchart4flow_rgnr_(sf, expt6flowchart4flow_rgnr, /):
        # !! may_expt6flowchart4serial_rgnr = expt6flowchart4flow_rgnr
        may_expt6flowchart4serial_rgnr = expt6flowchart4flow_rgnr
        if None is may_expt6flowchart4serial_rgnr:
            return TrueTrue
        expt6flowchart4serial_rgnr = may_expt6flowchart4serial_rgnr
        m = sf._may_calculator4next_acc_st4flowchart4serial_rgnr_
        no_acc_st = m is None
        #########
        if no_acc_st:
            bb = (b_final,b_dead) = FalseFalse
        else:
            (acc_st4flowchart, pt6flowchart) = expt6flowchart4serial_rgnr.tuple_as_stpt6flowchart
            bb = (b_final,b_dead) = sf._test_final_dead_acc_st4flowchart4flow_rgnr_(acc_st4flowchart)
        bb # (b_final,b_dead)
        #########
        return bb
    @override
    def _mk_entry_point4flowchart4flow_rgnr_(sf, cfg8scene, params8partialID, selected_kwds6ctx8fg, /):
        '-> entry_point{flowchart4flow_rgnr}/expt6flowchart'
        entry_point7serial_rgnr = sf._entry_point4flowchart4serial_rgnr_
        # !! [IAsbeItem4serial_rgnr <: IAsbeItem4flow_rgnr]
        entry_point7flow_rgnr = entry_point7serial_rgnr
        return entry_point7flow_rgnr
    @override
    def _enumerate_keyed_branch6flowchart4flow_rgnr_(sf, cfg8scene, expt6flowchart7alive, /):
        '-> Iter (key4branch, branch){flowchart4flow_rgnr} # [return null_iter] <==> [dead expt6flowchart]'
        # !! alive => not None
        # !! may_expt6flowchart4serial_rgnr = expt6flowchart4flow_rgnr
        expt6flowchart4serial_rgnr = expt6flowchart7alive
        # !! [IAsbeItem4serial_rgnr <: IAsbeItem4flow_rgnr]
        # => [branch6flowchart4flow_rgnr == branch6flowchart4serial_rgnr]
        return sf._enumerate_keyed_branch6flowchart4serial_rgnr_(expt6flowchart4serial_rgnr)
    @override
    def _get_branch6flowchart4flow_rgnr_(sf, cfg8scene, expt6flowchart7alive, key4branch, /):
        '-> branch{flowchart4flow_rgnr}/(may (asbe_item4flow_rgnr, exjmpstep4next))'
        # !! alive => not None
        # !! may_expt6flowchart4serial_rgnr = expt6flowchart4flow_rgnr
        expt6flowchart4serial_rgnr = expt6flowchart7alive
        branch6flowchart4serial_rgnr = sf._get_branch6flowchart4serial_rgnr_(expt6flowchart4serial_rgnr, key4branch)
        #########
        #.if None is branch6flowchart4serial_rgnr:
        #.    branch6flowchart4flow_rgnr = None
        #.else:
        #.    (asbe_item4serial_rgnr, exjmpstep4next) = branch6flowchart4serial_rgnr
        #.    #.asbe_item4flow_rgnr = asbe_item4serial_rgnr_to_asbe_item4flow_rgnr_(asbe_item4serial_rgnr)
        #.    asbe_item4flow_rgnr = asbe_item4serial_rgnr
        #.    branch6flowchart4flow_rgnr = (asbe_item4flow_rgnr, exjmpstep4next)
        #.branch6flowchart4flow_rgnr
        #########
        # !! [IAsbeItem4serial_rgnr <: IAsbeItem4flow_rgnr]
        branch6flowchart4flow_rgnr = branch6flowchart4serial_rgnr
        return branch6flowchart4flow_rgnr
    @override
    def _mk_next_expt6flowchart4flow_rgnr_(sf, curr_expt6flowchart7alive7nondead, key4branch, exjmpstep4next, /):
        '-> next_expt6flowchart{flow_rgnr}'
        # !! alive => not None
        # !! may_expt6flowchart4serial_rgnr = expt6flowchart4flow_rgnr
        curr_expt6flowchart4serial_rgnr = curr_expt6flowchart7alive7nondead
        may_next_expt6flowchart4serial_rgnr = sf._mk_may_next_expt6flowchart4serial_rgnr_(curr_expt6flowchart4serial_rgnr, exjmpstep4next)
        next_expt6flowchart4flow_rgnr = may_next_expt6flowchart4serial_rgnr
        return next_expt6flowchart4flow_rgnr
    @override
    def _mk_wrapped_oresult4flow_rgnr_(sf, cfg8scene, expt6flowchart, tmay_key4branch, partial_oresult, /):
        '-> wrapped_oresult{flow_rgnr}'
        wrapped_oresult = partial_oresult
        return wrapped_oresult
    @override
    def _mk_init_partial_oresult4flow_rgnr_(sf, cfg8scene, params8partialID, selected_kwds6ctx8fg, /):
        '-> partial_oresult{flow_rgnr}{initial}'
        ops4rope = cfg8scene.env8bg.ops4rope
        partial_oresult7initial = ops4rope.get_empty_rope_()
        return partial_oresult7initial
    @override
    def _mk_init_ctx4flow_rgnr_(sf, cfg8scene, params8partialID, selected_kwds6ctx8fg, /):
        '-> ctx4flow_rgnr{flow_rgnr}{initial}'
        ctx4flow_rgnr7initial = selected_kwds6ctx8fg
        return ctx4flow_rgnr7initial
    @override
    def _mk_payload4cfg4flow_rgnr_(sf, cfg8scene, params8partialID, selected_kwds6ctx8fg, /):
        '-> payload4cfg4flow_rgnr{flow_rgnr}'
        payload4cfg4flow_rgnr = params8partialID
        return payload4cfg4flow_rgnr
    @override
    def _check_input4flow_rgnr_(sf, cfg8scene, params8partialID, selected_kwds6ctx8fg, /):
        '-> None|^Exception'
        pass
    #########

def _mk__args_kwds_selector(params8partialID4child, selected_keys6ctx8fg4child, /):
    # [args_kwds_selector :: cfg8scene -> payload4cfg4flow_rgnr -> ctx4flow_rgnr -> child_rgnr -> (params8partialID{child_rgnr}, selected_kwds6ctx8fg{child_rgnr})]
    def args_kwds_selector(cfg8scene, payload4cfg4flow_rgnr, ctx4flow_rgnr7curr, child_rgnr, /):
        params8partialID4sf = payload4cfg4flow_rgnr
        params8partialID4child = params8partialID4sf
        ctx4serial_rgnr = ctx4flow_rgnr7curr
        selected_kwds6ctx8fg4child = cfg8scene.env8bg.ops4tsmapping.select_(selected_keys6ctx8fg4child, ctx4serial_rgnr)
        return (params8partialID4child, selected_kwds6ctx8fg4child)
    return args_kwds_selector
def _mk__mkr4kps8oc4child(case4join, kps8oc4later, /):
    #[mkr4kps8oc4child :: env8bg -> child_rgnr -> shifted_kps8oc -> kps8oc4child]
    def mkr4kps8oc4child(env8bg, child_rgnr, shifted_kps8oc7curr, /):
        kps8oc4child = union_kps8oc_at_case4join_(env8bg.ops4kps8oc, case4join, kps8oc4later, shifted_kps8oc7curr, offset:=0)
        return kps8oc4child
    return mkr4kps8oc4child
def _mk__extractor(case4join, key2getter, /):
    #[extractor :: cfg8scene -> ctx4flow_rgnr -> expt6flowchart -> key4branch -> exjmpstep4next -> keys7update -> kps8oc4child -> wrapped_oresult7subcall -> (modifier4shifted_kps8oc, wrapped_oresult7child, patch4ctx4flow_rgnr)]
    def extractor(cfg8scene, ctx4flow_rgnr7curr, expt6flowchart7curr7alive, key4branch, exjmpstep4next, keys7update, kps8oc4child, wrapped_oresult7subcall, /):
        key2value = _extract_(cfg8scene.env8bg, key2getter, wrapped_oresult7subcall)
        patch4ctx4flow_rgnr = values = tuple(key2value[k] for k in keys7update)
        wrapped_oresult7child = wrapped_oresult7subcall
        match case4join:
            case Case4join4serial_rgnr.DISCARD:
                delta_len4partial_oresult = 0
            case Case4join4serial_rgnr.PACK:
                delta_len4partial_oresult = 1
            case Case4join4serial_rgnr.UNPACK:
                ops4rope = cfg8scene.env8bg.ops4rope
                len4partial_oresult = ops4rope.len_(wrapped_oresult7subcall)
                delta_len4partial_oresult = len4partial_oresult
            case _:
                raise 000
        delta_len4partial_oresult
        modifier4shifted_kps8oc = offset = delta_len4partial_oresult
        return (modifier4shifted_kps8oc, wrapped_oresult7child, patch4ctx4flow_rgnr)
    return extractor
def _mk__may_updater_pair4partial_oresult_and_shifted_kps8oc(case4join, /):
    #[may_updater_pair4partial_oresult_and_shifted_kps8oc :: may (updater4partial_oresult, updater4shifted_kps8oc)]
    #[updater4partial_oresult :: (env8bg -> wrapped_oresult7child -> partial_oresult -> partial_oresult7updated)]
    #[updater4shifted_kps8oc :: (env8bg -> modifier4shifted_kps8oc -> shifted_kps8oc -> shifted_kps8oc7updated)]
    def updater4partial_oresult(env8bg, wrapped_oresult7child, partial_oresult7curr, /):
        partial_oresult7updated = append__via_join_(env8bg.ops4rope, case4join, wrapped_oresult7child, partial_oresult7updated)
        return partial_oresult7updated
    def updater4shifted_kps8oc(env8bg, modifier4shifted_kps8oc, shifted_kps8oc7curr, /):
        offset = modifier4shifted_kps8oc
        shifted_kps8oc7updated = env8bg.ops4kps8oc.offset_(offset, shifted_kps8oc7curr)
        return shifted_kps8oc7updated

    may_updater_pair4partial_oresult_and_shifted_kps8oc = None if case4join is Case4join4serial_rgnr.DISCARD else (updater4partial_oresult, updater4shifted_kps8oc)
    return may_updater_pair4partial_oresult_and_shifted_kps8oc
######################
#.class IStepRecognizer__serial(IStepRecognizer):
#.    r'''[[[
#.    [case4join == (DISCARD|UNPACK|PACK)]
#.    [item4serial_rgnr == (child_rgnr, params8partialID, selected_keys6ctx8fg, case4join, kps8oc, key2getter)]
#.    [branch :: may (item4serial_rgnr, exjmpstep4next)]
#.    [branch:None/return/end]
#.
#.    possible impl:
#.        IStepRecognizer__serial__using_flow_fork_branch_scheme_AS_flowchart
#.    #]]]'''#'''
#.    'limit ctx usage:ctx is only used under single serial layer control, ie, the only ctx updater is serial_rgnr # abandon scheme that return ctx'
#.    __slots__ = ()
#.    @property
#.    @abstractmethod
#.    def _entry_point4flowchart4serial_rgnr_(sf, /):
#.        '-> entry_point{flowchart4serial_rgnr}/may_expt6flowchart'
#.    @abstractmethod
#.    def _enumerate_keyed_branch6flowchart4serial_rgnr_(sf, expt6flowchart, /):
#.        '-> Iter (key4branch, branch){flowchart4serial_rgnr}'
#.    @abstractmethod
#.    def _get_branch6flowchart4serial_rgnr_(sf, expt6flowchart, key4branch, /):
#.        '-> branch{flowchart4serial_rgnr}/(may (item4serial_rgnr, exjmpstep4next))'
#.    @abstractmethod
#.    def _mk_may_next_expt6flowchart4serial_rgnr_(sf, curr_expt6flowchart, exjmpstep4next, /):
#.        '-> may_next_expt6flowchart'
#.    #@override
#.    feed__token_ = neednot__feed__token_
#.    #@override
#.    mk_cfg4rgnr_ = save__mk_cfg4rgnr_
#.    @override
#.    def start_recognize_(sf, cfg8scene, cfg4rgnr, /):
#.        '-> Iter eoxst'
#.        (params8partialID, selected_kwds6ctx8fg) = cfg4rgnr
#.        !!!params8partialID useless!!!
#.        ops4rope = cfg8scene.env8bg.ops4rope
#.        entry_point = sf._entry_point4flowchart4serial_rgnr_
#.        may_curr_expt6flowchart = may_expt6flowchart = entry_point
#.        partial_oresult = ops4rope.get_empty_rope_()
#.        ctx4serial_rgnr = selected_kwds6ctx8fg
#.        payload4st4sf = (may_curr_expt6flowchart, partial_oresult, ctx4serial_rgnr)
#.        return sf._iter_eoxsts4serial_rgnr(cfg8scene, cfg4rgnr, payload4st4sf)
#.    def _iter_eoxsts4serial_rgnr(sf, cfg8scene, cfg4rgnr, payload4st4sf, /):
#.        '-> Iter eoxst'
#.        ops4eoxst = cfg8scene.env8bg.ops4eoxst
#.        (may_curr_expt6flowchart, partial_oresult, ctx4serial_rgnr) = payload4st4sf
#.        if may_curr_expt6flowchart is None:
#.            wrapped_oresult = partial_oresult
#.            yield ops4eoxst.mk_eoxst__OK_(wrapped_oresult)
#.            return
#.        curr_expt6flowchart = may_curr_expt6flowchart
#.        it4keyed_branch = sf._enumerate_keyed_branch6flowchart4serial_rgnr_(curr_expt6flowchart)
#.
#.        ops4rope = cfg8scene.env8bg.ops4rope
#.        ops4tsmapping = cfg8scene.env8bg.ops4tsmapping
#.        len4partial_oresult = ops4rope.len_(partial_oresult)
#.        ops4kps8oc = cfg8scene.env8bg.ops4kps8oc
#.        kps8oc4sf = cfg8scene.kps8oc
#.
#.        _None_branch_occured = False
#.        for key4branch, branch in it4keyed_branch:
#.            if branch is None:
#.                if not _None_branch_occured:
#.                    _None_branch_occured = True
#.                    wrapped_oresult = partial_oresult
#.                    yield ops4eoxst.mk_eoxst__OK_(wrapped_oresult)
#.                continue
#.            (item4serial_rgnr, exjmpstep4next) = branch
#.            (child_rgnr, params8partialID, selected_keys6ctx8fg, case4join, kps8oc4later, key2getter) = item4serial_rgnr.tuple_as_item4serial_rgnr
#.            selected_kwds6ctx8fg4child = ops4tsmapping.select_(selected_keys6ctx8fg, ctx4serial_rgnr)
#.            kps8oc4child = union_kps8oc_at_case4join_(ops4kps8oc, case4join, kps8oc4later, kps8oc4sf, offset:=len4partial_oresult)
#.            yield ops4eoxst.mk_eoxst__CALL_(payload4st4sf, key4branch, child_rgnr, params8partialID, selected_kwds6ctx8fg4child, kps8oc4child)
#.    @override
#.    def feed__oresult_(sf, cfg8scene, cfg4rgnr, st, key4branch, kps8oc4child, wrapped_oresult7subcall, /):
#.        '-> Iter eoxst'
#.        env8bg = cfg8scene.env8bg
#.        ops4eoxst = env8bg.ops4eoxst
#.        ops4tsmapping = env8bg.ops4tsmapping
#.        ops4rope = env8bg.ops4rope
#.        payload4st4sf = ops4eoxst.get_payload6st7CALL_(st)
#.        (may_curr_expt6flowchart, partial_oresult, ctx4serial_rgnr) = payload4st4sf
#.        if may_curr_expt6flowchart is None: raise 000
#.        curr_expt6flowchart = may_curr_expt6flowchart
#.        branch = sf._get_branch6flowchart4serial_rgnr_(curr_expt6flowchart, key4branch)
#.        if branch is None: raise 000
#.        (item4serial_rgnr, exjmpstep4next) = branch
#.        (child_rgnr, params8partialID, selected_keys6ctx8fg, case4join, kps8oc4later, key2getter) = item4serial_rgnr.tuple_as_item4serial_rgnr
#.
#.        key2value = _extract_(env8bg, key2getter, wrapped_oresult7subcall)
#.        ctx4serial_rgnr7updated = ops4tsmapping.update_(key2value, ctx4serial_rgnr)
#.        partial_oresult7updated = append__via_join_(ops4rope, case4join, wrapped_oresult7subcall, partial_oresult)
#.        may_next_expt6flowchart = sf._mk_may_next_expt6flowchart4serial_rgnr_(curr_expt6flowchart, exjmpstep4next)
#.        payload4st4sf7updated = (may_next_expt6flowchart, partial_oresult7updated, ctx4serial_rgnr7updated)
#.        return sf._iter_eoxsts4serial_rgnr(cfg8scene, cfg4rgnr, payload4st4sf7updated)
#.######################
#.#.class IStepRecognizer__serial(IStepRecognizer):
#.#.    r'''[[[
#.#.    [case4join == (DISCARD|UNPACK|PACK)]
#.#.    #]]]'''#'''
#.#.    'limit ctx usage:ctx is only used under single serial layer control, ie, the only ctx updater is serial_rgnr # abandon scheme that return ctx'
#.#.    __slots__ = ()
#.#.    @property
#.#.    @abstractmethod
#.#.    def _entry_point_and_flowchart4serial_rgnr_(sf, /):
#.#.        '-> (entry_point/may_keyidx8begin, flowchart/{key:flow/[[may (item4serial_rgnr, may_mkeyoff4next)]]}) # [may_offset4next:None/return/end,0/loop{curr_item},+1/step/move_on] # [flowchart[i][j][k]:None/return/end] #[item4serial_rgnr == (child_rgnr, params8partialID, selected_keys6ctx8fg, case4join, kps8oc, key2getter)] # [may_mkeyoff4next == may (may_key4flow4next,offset4fork4next)] # [flowchart :: {key:flow}][flow :: [fork]][fork :: [branch]][branch :: may (item4serial_rgnr, may_mkeyoff4next)]'
#.#.    #.@property
#.#.    #.@abstractmethod
#.#.    #.def _child_item_seq4serial_rgnr_(sf, /):
#.#.    #.    '-> [(child_rgnr, params8partialID, selected_keys6ctx8fg, case4join, kps8oc, key2getter)]'
#.#.    #.@abstractmethod
#.#.    #.def _iter_child_rgnr_exs_(sf, /):
#.#.    #.    '-> Iter (child_rgnr, key2key6ctx, (kps8oc, key2ap))'
#.#.    #.    ++st/ctx??
#.#.    #.@abstractmethod
#.#.    #.def _mk_init_ctx4serial_rgnr_(sf, cfg8scene, params8partialID, selected_kwds6ctx8fg, /):
#.#.    #.    '-> ctx4serial_rgnr'
#.#.    #.@abstractmethod
#.#.    #.def _iter_next_items4serial_rgnr_(sf, cfg8scene, params8partialID, selected_kwds6ctx8fg, ctx4serial_rgnr, /):
#.#.    #.    '-> Iter (child_rgnr, kps8oc, key2getter)'
#.#.    #.#@override
#.#.    #.to_mk_new_ctx8serial_scope = True
#.#.    #@override
#.#.    feed__token_ = neednot__feed__token_
#.#.    #@override
#.#.    mk_cfg4rgnr_ = save__mk_cfg4rgnr_
#.#.    @override
#.#.    def start_recognize_(sf, cfg8scene, cfg4rgnr, /):
#.#.        '-> Iter eoxst'
#.#.        (params8partialID, selected_kwds6ctx8fg) = cfg4rgnr
#.#.        ops4rope = cfg8scene.env8bg.ops4rope
#.#.        #.ops4tsmapping = cfg8scene.env8bg.ops4tsmapping
#.#.        (entry_point, flowchart) = sf._entry_point_and_flowchart4serial_rgnr_
#.#.        may_keyidx4curr = may_keyidx8begin = entry_point
#.#.        partial_oresult = ops4rope.get_empty_rope_()
#.#.        #.ctx4serial_rgnr = ops4tsmapping.get_empty_mapping_()
#.#.        ctx4serial_rgnr = selected_kwds6ctx8fg
#.#.        payload4st4sf = (may_keyidx4curr, partial_oresult, ctx4serial_rgnr)
#.#.        return sf._iter_eoxsts4serial_rgnr(cfg8scene, cfg4rgnr, payload4st4sf)
#.#.        #.payload4st4sf = (idxidx4prev, may_mkeyoff4curr, partial_oresult, ctx4serial_rgnr)
#.#.        #.return sf._iter_eoxsts4serial_rgnr(cfg8scene, cfg4rgnr, payload4st4sf)
#.#.    def _iter_eoxsts4serial_rgnr(sf, cfg8scene, cfg4rgnr, payload4st4sf, /):
#.#.        '-> Iter eoxst'
#.#.        ops4eoxst = cfg8scene.env8bg.ops4eoxst
#.#.        (may_keyidx4curr, partial_oresult, ctx4serial_rgnr) = payload4st4sf
#.#.        #.may_idxidx4curr = _mk_may_idxidx4curr(idxidx4prev, may_mkeyoff4curr)
#.#.        if may_keyidx4curr is None:
#.#.            wrapped_oresult = partial_oresult
#.#.            yield ops4eoxst.mk_eoxst__OK_(wrapped_oresult)
#.#.            return
#.#.        (key4flow4curr, idx4fork4curr) = keyidx4curr = may_keyidx4curr
#.#.
#.#.        ops4rope = cfg8scene.env8bg.ops4rope
#.#.        ops4tsmapping = cfg8scene.env8bg.ops4tsmapping
#.#.        len4partial_oresult = ops4rope.len_(partial_oresult)
#.#.        ops4kps8oc = cfg8scene.env8bg.ops4kps8oc
#.#.        kps8oc4sf = cfg8scene.kps8oc
#.#.
#.#.        (entry_point, flowchart) = sf._entry_point_and_flowchart4serial_rgnr_
#.#.        #.item4serial_rgnr = ts[idx]
#.#.        fork4curr = flowchart[key4flow4curr][idx4fork4curr]
#.#.        if fork4curr.count(None) > 1:raise ValueError
#.#.        for key4branch, branch in enumerate(fork4curr):
#.#.            if branch is None:
#.#.                wrapped_oresult = partial_oresult
#.#.                yield ops4eoxst.mk_eoxst__OK_(wrapped_oresult)
#.#.                continue
#.#.            (item4serial_rgnr, may_mkeyoff4next) = branch
#.#.            (child_rgnr, params8partialID, selected_keys6ctx8fg, case4join, kps8oc4later, key2getter) = item4serial_rgnr.tuple_as_item4serial_rgnr
#.#.            selected_kwds6ctx8fg4child = ops4tsmapping.select_(selected_keys6ctx8fg, ctx4serial_rgnr)
#.#.            kps8oc4child = union_kps8oc_at_case4join_(ops4kps8oc, case4join, kps8oc4later, kps8oc4sf, offset:=len4partial_oresult)
#.#.            yield ops4eoxst.mk_eoxst__CALL_(payload4st4sf, key4branch, child_rgnr, params8partialID, selected_kwds6ctx8fg4child, kps8oc4child)
#.#.    @override
#.#.    def feed__oresult_(sf, cfg8scene, cfg4rgnr, st, key4branch, kps8oc4child, wrapped_oresult7subcall, /):
#.#.        '-> Iter eoxst'
#.#.        ops4eoxst = cfg8scene.env8bg.ops4eoxst
#.#.        ops4tsmapping = cfg8scene.env8bg.ops4tsmapping
#.#.        ops4rope = cfg8scene.env8bg.ops4rope
#.#.        payload4st4sf = ops4eoxst.get_payload6st7CALL_(st)
#.#.        #.(idx, partial_oresult, ctx4serial_rgnr) = payload4st4sf
#.#.        #.ts = sf._child_item_seq4serial_rgnr_
#.#.        #.item4serial_rgnr = ts[idx]
#.#.        (may_keyidx4curr, partial_oresult, ctx4serial_rgnr) = payload4st4sf
#.#.        #.may_keyidx4curr = _mk_may_keyidx4curr(keyidx4prev, may_mkeyoff4curr)
#.#.        if may_keyidx4curr is None: raise 000
#.#.        (key4flow4curr, idx4fork4curr) = keyidx4curr = may_keyidx4curr
#.#.        (entry_point, flowchart) = sf._entry_point_and_flowchart4serial_rgnr_
#.#.        fork4curr = flowchart[key4flow4curr][idx4fork4curr]
#.#.        branch = fork4curr[key4branch]
#.#.        if branch is None: raise 000
#.#.        (item4serial_rgnr, may_mkeyoff4next) = branch
#.#.        (child_rgnr, params8partialID, selected_keys6ctx8fg, case4join, kps8oc4later, key2getter) = item4serial_rgnr.tuple_as_item4serial_rgnr
#.#.
#.#.        key2value = _extract_(env8bg, key2getter, wrapped_oresult7subcall)
#.#.        ctx4serial_rgnr7updated = ops4tsmapping.update_(key2value, ctx4serial_rgnr)
#.#.        #.partial_oresult = ops4rope.append_(wrapped_oresult7subcall, partial_oresult)
#.#.        partial_oresult7updated = append__via_join_(ops4rope, case4join, wrapped_oresult7subcall, partial_oresult)
#.#.        #.idx += 1
#.#.        #.payload4st4sf = (idx, partial_oresult, ctx4serial_rgnr7updated)
#.#.        may_keyidx4next = _mk_may_keyidx4curr(keyidx4curr, may_mkeyoff4next)
#.#.        payload4st4sf7updated = (may_keyidx4next, partial_oresult7updated, ctx4serial_rgnr7updated)
#.#.        return sf._iter_eoxsts4serial_rgnr(cfg8scene, cfg4rgnr, payload4st4sf7updated)
#.#.def _mk_may_keyidx4curr(keyidx4prev, may_mkeyoff4curr, /):
#.#.    if may_mkeyoff4curr is None:
#.#.        return None
#.#.    mkeyoff4curr = may_mkeyoff4curr
#.#.    (may_key4flow4curr, offset4fork4curr) = mkeyoff4curr
#.#.    (key4flow4prev, idx4fork4prev) = keyidx4prev
#.#.    if may_key4flow4curr is None:
#.#.        key4flow4curr = key4flow4prev
#.#.        idx4fork4curr = idx4fork4prev +offset4fork4curr
#.#.    else:
#.#.        key4flow4curr = may_key4flow4curr
#.#.        idx4fork4curr = 0 +offset4fork4curr
#.#.    keyidx4curr = (key4flow4curr, idx4fork4curr)
#.#.    return keyidx4curr

######################
class IStepRecognizer__serial__using_flow_fork_branch_scheme_AS_flowchart(IStepRecognizer__serial):
    #class IStepRecognizer__serial__keyidx_AS_pt__may_mkeyoff4next_AS_exjmpstep4next(IStepRecognizer__serial):
    r'''[[[
    [pt6flowchart == (key4flow, idx4fork)]
    [flowchart :: {key:flow}]
    [flow :: [fork]]
    [fork :: [branch]]
    [branch :: may (asbe_item4serial_rgnr, exjmpstep4next)]
    [jmpstep4next == may_mkeyoff4next == may mkeyoff4next/(may_key4flow4next,offset4fork4next)]
    [[may_offset4next:None/return/end,0/loop{curr_item},+1/step/move_on]]
    [branch == flowchart[key4flow][idx4fork][key4branch]]
    #]]]'''#'''
    __slots__ = ()
    @property
    @abstractmethod
    def _flowchart4serial_rgnr_(sf, /):
        '-> flowchart/{key:flow/[fork/[may (asbe_item4serial_rgnr, may_mkeyoff4next)]]}'

    @override
    def _enumerate_keyed_branch6flowchart4serial_rgnr_(sf, expt6flowchart, /):
        '-> Iter (key4branch, branch){flowchart4serial_rgnr}'
        pt6flowchart = sf._expt2pt6flowchart4serial_rgnr_(expt6flowchart)
        (key4flow, idx4fork) = pt6flowchart
        flowchart = sf._flowchart4serial_rgnr_
        flow = flowchart[key4flow]
        fork = flow[idx4fork]
        return enumerate(fork)
    @override
    def _get_branch6flowchart4serial_rgnr_(sf, expt6flowchart, key4branch, /):
        '-> branch{flowchart4serial_rgnr}/(may (asbe_item4serial_rgnr, exjmpstep4next))'
        pt6flowchart = sf._expt2pt6flowchart4serial_rgnr_(expt6flowchart)
        (key4flow, idx4fork) = pt6flowchart
        flowchart = sf._flowchart4serial_rgnr_
        flow = flowchart[key4flow]
        fork = flow[idx4fork]
        branch = fork[key4branch]
        return branch
    @override
    def _mk_may_next_expt6flowchart4serial_rgnr_(sf, curr_expt6flowchart, exjmpstep4next, /):
        '-> may_next_expt6flowchart'
        m = sf._may_calculator4next_acc_st4flowchart4serial_rgnr_
        no_acc_st = m is None
        #########
        if not no_acc_st:
            calculator4next_acc_st4flowchart = m
            (curr_acc_st4flowchart, curr_pt6flowchart) = curr_expt6flowchart.tuple_as_stpt6flowchart
            (delta_st4flowchart, jmpstep4next) = exjmpstep4next.tuple_as_stjmpstep4next
        else:
            curr_pt6flowchart = curr_expt6flowchart
            jmpstep4next = exjmpstep4next
        curr_pt6flowchart
        jmpstep4next
        #########

        keyidx4curr = curr_pt6flowchart
        may_mkeyoff4next = jmpstep4next
        may_keyidx4next = _mk_may_keyidx4next(keyidx4curr, may_mkeyoff4next)
        may_next_pt6flowchart = may_keyidx4next
        if no_acc_st or may_next_pt6flowchart is None:
            may_next_expt6flowchart = may_next_pt6flowchart
        else:
            next_pt6flowchart = may_next_pt6flowchart
            next_acc_st4flowchart = calculator4next_acc_st4flowchart(delta_st4flowchart, curr_acc_st4flowchart)
            (b_final,b_dead) = sf._test_final_dead_acc_st4flowchart4flow_rgnr_(next_acc_st4flowchart)
            #now:override:_test_final_dead_expt6flowchart4flow_rgnr_()
            if b_dead and b_final:
            #if b_dead:
                #.# dead
                #.if not b_final:raise NotImplementedError('nonfinal&&dead')
                # final&&dead
                may_next_expt6flowchart = None
            else:
                #.#alive
                #.if b_final:raise NotImplementedError('final&&alive')
                #.# nonfinal&&alive

                # nonfinal||alive
                next_expt6flowchart = AsbeStatedPoint6flowchart__plain(next_acc_st4flowchart, next_pt6flowchart)
                may_next_expt6flowchart = next_expt6flowchart
            may_next_expt6flowchart
        may_next_expt6flowchart

        return may_next_expt6flowchart

def _mk_may_keyidx4next(keyidx4curr, may_mkeyoff4next, /):
    if may_mkeyoff4next is None:
        return None
    mkeyoff4next = may_mkeyoff4next
    (may_key4flow4next, offset4fork4next) = mkeyoff4next
    if not may_key4flow4next is None:
        key4flow4next = may_key4flow4next
        idx4fork4next = 0 +offset4fork4next
    else:
        (key4flow4curr, idx4fork4curr) = keyidx4curr
        key4flow4next = key4flow4curr
        idx4fork4next = idx4fork4curr +offset4fork4next
    may_keyidx4next = keyidx4next = (key4flow4next, idx4fork4next)
    return may_keyidx4next
######################


def union_kps8oc_at_case4join_(ops4kps8oc, case4join, kps8oc4later, kps8oc4sf, offset, /):
    check_type_is(Case4join4serial_rgnr, case4join)
    match case4join:
        case Case4join4serial_rgnr.DISCARD:
            kps8oc = kps8oc4later
        case Case4join4serial_rgnr.PACK:
            inner_kps8oc = ops4kps8oc.access_(offset, kps8oc4sf)
            kps8oc = ops4kps8oc.union_(inner_kps8oc, kps8oc4later)
        case Case4join4serial_rgnr.UNPACK:
            offsetted_kps8oc = ops4kps8oc.offset_(offset, kps8oc4sf)
            kps8oc = ops4kps8oc.union_(offsetted_kps8oc, kps8oc4later)
        case _:
            raise 000#ValueError(case4join)
    kps8oc
    return kps8oc
def _extract_(env8bg, key2getter, wrapped_oresult, /):
    'env8bg -> key2getter/{key:(env8bg->wrapped_oresult->value)} -> wrapped_oresult -> key2value/{key:value}'
    return {k:g(env8bg, wrapped_oresult) for k, g in key2getter.items()}




#.class IAsbeItem4tuple_rgnr(IAsbeItem4serial_rgnr):
#.    'asbe_item4tuple_rgnr #used by IStepRecognizer__serial__tuple'
#.    __slots__ = ()
#.    @property
#.    @abstractmethod
#.    def tuple_as_item4tuple_rgnr(sf, /):
#.        '-> item4tuple_rgnr/(child_rgnr, params8partialID{child_rgnr}, selected_keys6ctx8fg{child_rgnr}, case4join, kps8oc{later:child_rgnr}, key2getter)'
#.    @cached_property
#.    @override
#.    def tuple_as_item4serial_rgnr(sf, /):
#.        #'-> item4serial_rgnr/(child_rgnr, params8partialID{child_rgnr}, selected_keys6ctx8fg{child_rgnr}, case4join, kps8oc{later:child_rgnr}, key2getter)'
_mkeyoff4next = (None, +1)
_final_fork = (_final_branch:=None,)
def mk_unit_tuple_(x, /):
    return (x,)
class IStepRecognizer__serial__tuple(IStepRecognizer__serial__using_flow_fork_branch_scheme_AS_flowchart):
    'tuple'
    __slots__ = ()
    #.@property
    #.@abstractmethod
    #.def _seq4asbe_item4tuple_rgnr_(sf, /):
    #.    '-> [asbe_item4tuple_rgnr]'
    @property
    @abstractmethod
    def _seq4asbe_item4serial_rgnr_(sf, /):
        '-> [asbe_item4serial_rgnr]'
    #@override
    _direct_required_ops8pc_ = null_flag4ops8pc
    #@override
    _may_calculator4next_acc_st4flowchart4serial_rgnr_ = None
    #@override
    _may_tester4whether_final_dead_acc_st4flowchart4serial_rgnr_ = None
    @cached_property
    @override
    def _flowchart4serial_rgnr_(sf, /):
        mk_unit_fork5branch_ = mk_unit_tuple_
        it8forks = (mk_unit_fork5branch_((asbe_item4serial_rgnr, _mkeyoff4next)) for asbe_item4serial_rgnr in sf._seq4asbe_item4serial_rgnr_)
        flow = (*it8forks, _final_fork)
        flowchart = mk_unit_tuple_(flow)
        return flowchart
    #@override
    _entry_point4flowchart4serial_rgnr_ = (0, 0) # idxidx #no_acc_st
class IStepRecognizer__serial__array(IStepRecognizer__serial__using_flow_fork_branch_scheme_AS_flowchart):
    'array'
    __slots__ = ()
    #.1 or (isize7pack, osize7unpack)
    @property
    @abstractmethod
    def _seq4asbe_item4serial_rgnr_(sf, /):
        '-> [asbe_item4serial_rgnr]'
    @property
    @abstractmethod
    def _xlen4tail_period4seq4asbe_item4serial_rgnr_(sf, /):
        '-> xlen4tail_period/(len4tail_period|neg1_neg_len4head) # [1 <= len4tail_period <= len4tail_period + len4head == len(_seq4asbe_item4serial_rgnr_)][neg1_neg_len4head == -1-len4head] # [[xlen4tail_period==-1] -> [len4tail_period==len(_seq4asbe_item4serial_rgnr_)]] # [[xlen4tail_period==0] -> [nonperiodic:forbid/^NotImplementedError]]'
    @property
    @abstractmethod
    def _test_final_dead_num_children4array_rgnr_(sf, num_children, /):
        'num_children/uint -> (b_final,b_dead)/(bool, bool)'

    @cached_property
    def _len4tail_period4seq4asbe_item4serial_rgnr_(sf, /):
        '-> len4tail_period/int{>=1}{<=len(_seq4asbe_item4serial_rgnr_)}'
        L = len(sf._seq4asbe_item4serial_rgnr_)
        xlen4tail_period = sf._xlen4tail_period4seq4asbe_item4serial_rgnr_
        if xlen4tail_period < 0:
            neg1_neg_len4head = xlen4tail_period
            len4head = -1-neg1_neg_len4head
            len4tail_period = L -len4head
        else:
            len4tail_period = xlen4tail_period
        len4tail_period
        if len4tail_period == 0:raise NotImplementedError('nonperiodic:should use IStepRecognizer__serial__tuple')
        check_int_ge_le(1, L, len4tail_period)
        return len4tail_period

    #@override
    _entry_point4flowchart4serial_rgnr_ = AsbeStatedPoint6flowchart__plain(0, (0,0)) # (num_children, idxidx)
    @cached_property
    @override
    def _flowchart4serial_rgnr_(sf, /):
        '-> flowchart/{key:flow/[fork/[may (asbe_item4serial_rgnr, may_mkeyoff4next)]]}'
        ls4item = sf._seq4asbe_item4serial_rgnr_
        L = len(ls4item)
        if L == 0:raise NotImplementedError
        len4tail_period = sf._len4tail_period4seq4asbe_item4serial_rgnr_
        check_int_ge_le(1, L, len4tail_period)

        ls4idxoff = [_mkeyoff4next]*L
        777;ls4idxoff[-1] = (None, 1-len4tail_period)
            #tail_loop

        delta_st4flowchart = delta_num_children = +1
        ls4exjmpstep4next = [AsbeStatedJmpStep6flowchart__plain(delta_st4flowchart, mkeyoff4next) for mkeyoff4next in ls4idxoff]
        flow = tuple(zip(ls4item, ls4exjmpstep4next))
        flowchart = mk_unit_tuple_(flow)
        return flowchart
    #@property
    @override
    def _may_calculator4next_acc_st4flowchart4serial_rgnr_(sf, delta_st4flowchart, curr_acc_st4flowchart, /):
        num_children = curr_acc_st4flowchart
        delta_num_children = delta_st4flowchart
        num_children += delta_num_children
        next_acc_st4flowchart = num_children
        return next_acc_st4flowchart
    #@property
    @override
    def _may_tester4whether_final_dead_acc_st4flowchart4serial_rgnr_(sf, acc_st4flowchart, /):
        num_children = acc_st4flowchart
        return sf._test_final_dead_num_children4array_rgnr_(num_children)
class IStepRecognizer__serial__end_by(IStepRecognizer__serial__using_flow_fork_branch_scheme_AS_flowchart):
    'end_by'
    __slots__ = ()
    1 or TODO
    StepRecognizer__wrapper__rgnr_expr_with_repr # tuple_rgnr{[array_rgnr{[item8body]}, item8end]}
class IStepRecognizer__serial__sep_by(IStepRecognizer__serial__using_flow_fork_branch_scheme_AS_flowchart):
    'sep_by'
    __slots__ = ()
    1 or TODO
    StepRecognizer__wrapper__rgnr_expr_with_repr # array_rgnr{[item8body, item8end], ok@count(1,2) \-/ {0}?}
class IStepRecognizer__serial__ctx_between(IStepRecognizer__serial__using_flow_fork_branch_scheme_AS_flowchart):
    'ctx_between'
    __slots__ = ()
    1 or TODO
    1 or ctx_assert
__all__
r'''[[[

[[
login:登记
logout:注销
fixed_ops@env8bg:
    ops4logger:
        log()
        ?add/remove listener?
    ops4lookup:
    lookup_name_
        name2rgnr_
        name2logger_
fixed_ops@env8bg:
  ops4kps8oc:
    ignore
    whole
    lazy_whole
    or_/union_(kps8oc, kps8oc) -> kps8oc
    mk5key2kps8oc
    mk5callable_(key2kps8oc_) -> kps8oc{~=(offset,key2kps8oc_)}
      难点:tuple子部件解包:kps8oc的index究竟是指 解包前的子部件址引还是解包后的输出的址引？
        要求:idx型kps8oc 允许附加偏移量
  ops4rope
    mk_rope_
      附加 定位后处理{idx:[fpost]}
    mk_element_(x, *fposts)->boxed 延迟
      附加 后处理
    ??rope+fpost->elem 延迟??
      毕竟经过后处理，就不再是rope
      除非是fmap...
  ops4ctx:
    #工厂模式:匴
    因为 保存于 st中，必须是 固化版
    #ctx8fg :: seq/finger_tree|TreeMap|LookupList
    ops4queue:
    ops4assoc_list:
    ops4stack:
ops8pc@cfg4rgnr:
  #权限管理
  ops4tkn:
      '{tkey}@{super_tkey}/{sub_tkey}:{tdat}'
      '{tkey}@*/*:*'
    may tkn2super_tkey_   #范畴:op,kw,『.com』
    may tkn2sub_tkey_     #副标题:...『www.』
        '{tkey}:*'
    may tkn2tkey_
    may tkn2tkey_
      read__len_eq_
      skip__len_eq_
    may tkn2tdat_
      净识别器=>None:ni tkn2tdat_
kps8oc
  reqired_fields8output_control
  reqired_field_name_tree8output_control
  reqired_field_paths8output_control
  reqired_access_paths8output_control
  attr_path_set8output_control
    ===kps8oc
step_recognizer__level1:
  .mk1_cfg4recognizer_(sf, params8partialID, ops) -> cfg4rgnr
  .start1_recognize_(sf, cfg4rgnr, ops) -> Iter eoxst
  .feed__token_(sf, st, token, *, ops) -> Iter eoxst
  .feed__oresult_(sf, st, key4branch, kps8oc4child, oresult, *, ops) -> Iter eoxst
  eoxst == (Either st eresult)
  eresult = ((OK/FINAL, oresult)|(ERR, case4err, payload4err, lazy_msg4err, neg_idx4tkn4err:=-1))
  st = ((FEED_MORE, payload4st{sf})|(CALL1, payload4st{sf}, key4branch, sub_rgnr/step_recognizer__level1, params8partialID{sub_rgnr}))
      外部调用框架中，ops 自动绑定 sf，根据 sub_rgnr的声明，构造 受更严格限制的ops，并调用sub_rgnr.start_recognize_...
      也就是 st的完整状态，应当是:(cfg4rgnr,ops,st)
  cfg4rgnr{+sf 用作 标识{@起点}；st虽然是固化量，但无用于 标识{中间态无用}}
    #xxx:tokens8remainder
step_recognizer__level2:
  #cfg8scene=(env8bg, ops8pc, kps8oc)
  .mk2_cfg4recognizer_(sf, params8partialID, selected_kwds6ctx8fg, cfg8scene) -> cfg4rgnr
  .start2_recognize_(sf, cfg4rgnr, cfg8scene) -> Iter eoxst
  .feed2__token_(sf, cfg4rgnr, st, token, *, cfg8scene) -> Iter eoxst
  .feed__oresult_(sf, cfg4rgnr, st, key4branch, kps8oc4child, oresult, *, cfg8scene) -> Iter eoxst
  st = ((FEED_MORE, payload4st{sf})|(CALL2, payload4st{sf}, key4branch, sub_rgnr/step_recognizer__level2, params8partialID{sub_rgnr}, getters6ctx8fg, kps8oc))
      st的完整状态，应当是:(单过程全程不变env8bg,初始固化(ops8pc,kps8oc),cfg4rgnr{初始固化:selected_kwds6ctx8fg/selected-ctx8fg;},st)
step_recognizer__level3(info_collector, IInterned):
  # Ord tkey
  .iter_nullable_conditions_() -> Iter {rgnr} # any(all(rgnrs nullable))
  .iter_first_set_() -> Iter (rgnr|tkey)


e ../../python3_src/seed/abc/IInterned.py
平行识别器/投喂型识别器
  为了 收集信息:
    枚举 子节点 信息提供器:识别器|构造器...
      收集 所有 料符.型号/款型
      收集 所有 料符.头符集+欤允空
      收集 所有 料符.首料符集
  为了 加速:
    识别器.欤允空
    识别器.头符集::全序范围序列 :: [(边界,边界)]
    边界 == (just_lt a, gt a, +oo, -oo)
    #slightly_lt
    (just_lt a, just_gt b) == [a..=b]
    (just_lt a, just_lt b) == [a..<b]
    (just_gt a, just_lt b) == [a<..<b]
    (just_gt a, just_gt b) == [a<..=b]
  区分:净识别器vs脏识别器:
    脏识别器:使用token.tkey,token.tdat #比如:end_tag匹配start_tag
        也许可以 归脏于:脏判定器&脏后处理，虚拟运行时直接跳过
        脏判定器 效果 区分出 tkey子类
            脏判定器(tkn0.tkey,tkn0.tdat,...) -> bool/或者 某个有限枚举集
              应当说:其余tkn参数 也只是 参与 对 tkn0的区分
        也许可以 遇到 脏判定器 时 给tkey 附加 子类标签，将 一个 混沌状态包 分割成为 多个 [平行]混沌状态包，同一混沌状态包 内部 歧义导致出错，不同混沌状态包 之间 则 不产生交叉歧义
    净识别器:只使用token.tkey
        允许 虚拟运行，类似LR1或regex，tkey有限而tdat无限
  区分:关窍展符vs皮毛展符:
    皮毛展符:后处理被推迟？，允许 歧义性{LR1:reduce-reduce,reduce-shift}
    关窍展符:reduce时，不允许其余展符reduce/shift，即reduce排他性
  为了避免麻烦，不如直接批量传入不同参数？
      识别器{参数} --> 识别器{Set 参数}
        构型参数:不可整合#或许 前缀整合？
            __new__(构型参数) -> rgnr
        输出控制参数:可整合:eg:输出值被提取的属性...
            #start_recognize_(背景参数, 语境参数, 输出控制参数) -> st
            {kwd:sym}背景参数 重命名/链接:符号->id
            start_recognize_(kwds{被挑选的背景参数}, 语境参数, 输出控制参数) -> st{可以含有:被挑选的背景参数，但是已然避免 包含 整个 背景参数包}
            reqired_fields.__or__ 用户自定义#大部分情况raise NotImplementedError
            reqired_fields{output} = tribool|{(index|attr):reqired_fields}|(识别器->(index|attr)->reqired_fields)
                False=>忽略/不输出
                True=>输出{后处理实时应用}
                ...=>输出{后处理推迟:即:输出(输出值,[后处理])}
                但是 数组怎么办？
            tuple(..., 启后(识别器, {nm:reqired_fields}...), ..., 承前(承前识别器,[nm]...;输出(nm...;具名{nm...}))
        识别器.整合参数集(参数集)->Iter (统一参数, 被整合参数集)
        --> Iter 识别器{统一参数{被整合参数集}}
      输出值 --> {参数:输出值}
        识别器{统一参数{被整合参数集}}.解释输出值扌(输出值{统一参数},被整合参数)->输出值{被整合参数}
      Iter 输出值 --> Iter (参数,输出值)
      输入需求 --> {参数:输入需求}
      投喂(被需求的输入串) --> ???
      规范化参数扌(参数)->标准参数包冃可散列值{可能归一化拘留}
          欤避免散列:大对象 或者 不可散列对象
  注意:忽略庇护 的出现 必然是 由于 其输出值 被用作 后续识别器 的 语境参数。语境参数的递送 由 串联式 内部定义，所以 忽略庇护 只作用于 串联式 的 子部件。
  区分:后处理系统
    * 内禀硬编码牜不可忽略:影响识别成败流程#同时也是:此处及内部 递归 禁用 用户外赋 后处理
    * 可忽略:不影响识别成败流程
      * 用户外赋:每次识别过程附加不同后处理
      * 内禀硬编码牜可忽略:所有识别过程一致
  区分:后处理系统
    * 即时后处理 -> Raw
    * 惰性后处理 -> LazyRaw
      因为某些分支最终被放弃，其之前的中间结果 没有计算的必要性
      节省时间，但空间开销大
  封装所有输出值:
    #只有 键值{词典/记录},况态{Union,Cased}是简单数据？
    #惰性求值
    #欤可忽略-->忽略深度-->筛选输出值，但是 要能够 递归向下递送，还需要 额外考虑:该参数的类型 可能需要 对应于 识别器 的 嵌套循环模式。
    #外赋后处理
    #欤禁用外赋后处理
    # .unlazy/cached_property
    # .is_raw/bool
    Raw/LazyRaw:任意类型
      忽略:指 忽略 Raw的内容，其余结构依然保持
      外赋后处理:要么fmap保形深入修改，要么修改后变成Raw
        e ../../python3_src/seed/algo/almost_graph/tree/conformal_transformation.py
        保形变换:conformal transformation:
          (post4enter, post4exit; env, ctx, st4acc)
          post4enter(env, ctx, st4acc, x) -> ((Raw, st4acc) | args4into/(_ctx, _st4acc))
          post4exit(env, ctx, st4acc, x, _x, _ctx, _st4acc) -> ((Raw, st4acc) | st4acc)
          <==>
          (post4enter, post4exit; st)
          post4enter(st, x) -> ((Raw, st) | args4into/_st)
          post4exit(st, x, _x, _st) -> ((Raw, st) | st)
      内禀后处理:不涉及Raw
      即:Raw是 用户自留地
    Unpack{Tuple/Array/Union/...}
      解包:只用作 子部件的输出
    Tuple:定长串
      NamedTuple/Record:定键词典/记录
      静态长度=>Tuple允许解包Tuple#但不允许解包Array
      内部庇护:可以指定某些子部件不被忽略
        => 前文输出 用作 下文参数
        => 受庇护子部件 全系统 禁用:外赋后处理
    Rope/Array:变长串
      LookupList/Dict:变键词典/词典
      动态长度=>Array允许解包Array,Tuple
      不可以指定某些子部件不被忽略
        =>只记录长度的形态(<==>[None]*length)
          ???但是 也许 子部件的结构有用？
          =>忽略深度:
            第0层 开始忽略 <==> 忽略自身
            第1层 开始忽略 <==> 忽略子部件，本层结构保持 #只影响Array/Dict之类
      ？？？内敛识别endBy!!!
      变长=>三种状态:树状结构vs平坦结构vs仅长度
        iter全遍历时 无需平坦化
        惰性平坦化
    Union:定况分立
      Union允许融并Union#但不允许融并Cased
      内部庇护:可以指定某些子部件不被忽略
    Cased:变况分立
      Cased允许融并Union,Cased
      不可以指定某些子部件不被忽略
      实例:料符 Cased(key, Raw)
  参数设置:
    识别器{静态参数}(每次识别过程的语境参数)
      状态等效:
        注意:前导噪声 不应当 改变 初始状态
    语境参数/context:分两类:
      kwds:简单参数，参与Hash
        可选，提供default
          default有助于id归一化
        无需确认总长度/键表
      args:复杂参数，不参与Hash,只用id区分
        可选，提供default
          default有助于id归一化
          default=>需要确认总长度
        上面出现的Tuple/Raw...都禁止__hash__
          因为必然是语境输出=>是复杂参数
          键值Hashable=>只有 键值{词典/记录},况态{Union,Cased}是简单数据
          静态参数:简单参数:Hashable
    intern()
      归一化{标准代表纟识别器}:类似 sys.intern :: str->str
  提示性与实用性:
    料符位置信息:外赋:不透明数据，假设用户可以解读，识别过程只搬运不涉及解读
      外用不内用
    料符位次信息:内禀:uint:识别过程内部使用，可用作外部提示(虽然不保证语义)
      内用不外用
interactive - stepping - feed_in
.start_(interned_kwds7pure, env8bg, ctx8fg, interned_args8remnant) -> GI{[st]}
.feed_tkns_(env8bg, ctx8fg, st, required_tkns) -> GI{[st]}
.feed_subcall_(env8bg, ctx8fg, st, oresult7subcall, interned_args8remnant7subcall) -> GI{[st]}
st7final:
  .oresult
  .interned_args8remnant
  #总输出:(oresult, interned_args8remnant)
st7loop:
  .state7loop
  .required_kind :: tkey
  .required_size :: pint
st7subcall:
  .state7subcall
  .callee :: (rgnr, interned_kwds7pure, ctx8fg, interned_args8remnant)
st7tailcall:
  .callee :: (rgnr, interned_kwds7pure, ctx8fg, interned_args8remnant)

oresult:
  .unlazy
  .whether_raw
  .whether_lazy_raw
  .whether_unlazy


]]
#]]]'''#'''





__all__
from seed.recognize.step_recognizer.IStepRecognizer import *
