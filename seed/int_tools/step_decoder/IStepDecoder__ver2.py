#__all__:goto
r'''[[[
e ../../python3_src/seed/int_tools/step_decoder/IStepDecoder__ver2.py
view ../../python3_src/seed/int_tools/step_decoder/StepDecoder__ver1__deprecated.py
    ver1:毛病:具象类 与 接口类 混淆在一起
TODO:e ../../python3_src/seed/int_tools/step_decoder/StepDecoder__ver2.py

seed.int_tools.step_decoder.IStepDecoder__ver2
py -m nn_ns.app.debug_cmd   seed.int_tools.step_decoder.IStepDecoder__ver2 -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.int_tools.step_decoder.IStepDecoder__ver2:__doc__ -ht # -ff -df
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.int_tools.step_decoder.IStepDecoder__ver2:cls@T    =T   +exclude_attrs5listed_in_cls_doc
#######
from seed.pkg_tools.ModuleReloader import mk_doctestXmodule_reloader_
doctestXmodule_reloader = mk_doctestXmodule_reloader_('', 'seed.int_tools.step_decoder.IStepDecoder__ver2:__doc__', '-ht')
doctestXmodule_reloader(reload_first=False)
doctestXmodule_reloader()
#######

[[
源起:
    view others/数学/编程/设计/自定义编码纟整数暨有理数-byte字母表+7over8效率.txt


源起0:
view ../../python3_src/seed/int_tools/step_decoder/StepDecoder__ver1__deprecated.py
    ver1:毛病:具象类 与 接口类 混淆在一起
cd $my_git_py; git mv seed/int_tools/StepDecoder.py seed/int_tools/step_decoder/StepDecoder__ver1__deprecated.py

源起1:
  全状态解码:被编码值 与 编码 一一对应，保证 非标准值 可被编码出来，也允许 非标准值 被解码 从而定制特殊用途。
        比如，解码 整数，非标准整数 必须 贴上 区别标签
  eof时 输出所有公开可继续解码状态
  err时 输出所有公开可继续解码状态
    重点 在于 公用数据，定义于 编码方案
      st是 私用状态，解码器 随意定义

源起2:
    [decoder <: decoder_mkr7rHrB]
    [decoder_mkr7rHrB :: radixH -> radixB -> env -> decoder]
      # [decoder :: radixH -> radixB-> env  -> self/decoder{validate:(radixH,radixB,env)}]
      允许:先 缺省 背景参数，构造 构造器，再 一次性 灌注 背景参数，构造 解码器{甚或:可能同时 构造出 编码器}

源起3:ver2接口 不同于 ver1
接口:
IBaseStepDecoder:
  .start_(void) -> st7head
  .may_feed_head_rxdigit_(st7head, head_rxdigit) -> st
  .may_feed_digits7required_size_(st, digits) -> st
  .may_feed_digits7less_than_required_size7eof_(...) -> st
  .may_feed_digits7arbitrary_size_(...) -> st
  .may_feed_result7subcall_(...) -> st
  .on_oresult_(st) -> (oresult, tmay_head_rxdigit, unused_digits)
  .on_eof_(st) -> (public_exchangeable_resumeable, tmay_head_rxdigit, unused_digits)
        允许 交换，将来 使用 其他解码器 继续解码
  .on_err_(st) -> (public_exchangeable_extensible, tmay_head_rxdigit, unused_digits, imay_idx4digits7err{-1/err6head})
        用于未来扩展:保留区/未定义区/...

IStepDecoder(IBaseStepDecoder):
  .feed_head_rxdigit_(st7head, head_rxdigit) -> st
  .feed_digits7required_size_(st, digits) -> st

IStepDecoder__flatten(IStepDecoder):
  .may_feed_result5subcall_ = None

IStepDecoder__stacked(IStepDecoder):
  .feed_result5subcall_(...) -> st


]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.int_tools.step_decoder.IStepDecoder__ver2   @f
from seed.int_tools.step_decoder.IStepDecoder__ver2 import *
]]]'''#'''
__all__ = r'''
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
#.from functools import cached_property
#.from itertools import islice
#.from seed.tiny_.check import check_type_is, check_int_ge
#see:dot_#from seed.func_tools.dot2 import dot
#.
#.from abc import update_abstractmethods
#.from seed.abc.abc__ver1 import abstractmethod, override, ABC
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
#.from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
#.with mk_ctx4lazy_import4funcs_(__name__, 'ifNone:_ifNone, ifNonef:_ifNonef'):
#.    from seed.helper.ifNone import ifNone as _ifNone, ifNonef as _ifNonef
#.with mk_ctx4lazy_import4funcs_(__name__):
#.    from seed.helper.repr_input import repr_helper
#.    from seed.tiny_.types5py import mk_MapView,curry1,kwargs2Attrs #,MapView
#.    from seed.tiny_.containers import mk_tuple,mk_immutable_seq,mk_immutable_seq5iterT_,mk_immutable_seq5iter__,mk_bytes5iter_,mk_tuple__split_first_if_str #xxx:null_tuple
#.    from seed.debug.print_err import print_err
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



















__all__
from seed.int_tools.step_decoder.IStepDecoder__ver2 import *
