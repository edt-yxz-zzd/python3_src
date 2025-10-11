#__all__:goto
r'''[[[
e zz

z
py -m nn_ns.app.debug_cmd   z -x # -off_defs
py -m nn_ns.app.doctest_cmd z:__doc__ -ht # -ff -df
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %z:cls@T    =T   +exclude_attrs5listed_in_cls_doc
#######
from seed.pkg_tools.ModuleReloader import mk_doctestXmodule_reloader_
doctestXmodule_reloader = mk_doctestXmodule_reloader_('', 'z:__doc__', '-ht')
doctestXmodule_reloader(reload_first=False)
doctestXmodule_reloader()
#######

[[
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   z   @f
from z import *
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



#.#################################
#.:s/\v^from +([_[:alnum:].]+) +import +([^# ]( *[^# ])*).*/lazy_import4funcs_('\1', '\2', __name__)\rif 0:\0
#.from seed.helper.lazy_import__func import lazy_import4func_, lazy_import4funcs_, force_lazy_imported_func_
#.repr_helper = lazy_import4func_('seed.helper.repr_input', 'repr_helper', __name__)
#.
#.lazy_import4funcs_('seed.tiny_.types5py', 'mk_MapView,curry1,kwargs2Attrs', __name__)
#.if 0:from seed.tiny_.types5py import mk_MapView,curry1,kwargs2Attrs #,MapView
#.lazy_import4funcs_('seed.tiny_.containers', 'mk_tuple,mk_immutable_seq,mk_immutable_seq5iterT_,mk_immutable_seq5iter__,mk_bytes5iter_,mk_tuple__split_first_if_str', __name__)
#.if 0:from seed.tiny_.containers import mk_tuple,mk_immutable_seq,mk_immutable_seq5iterT_,mk_immutable_seq5iter__,mk_bytes5iter_,mk_tuple__split_first_if_str #xxx:null_tuple
#.lazy_import4funcs_('seed.debug.print_err', 'print_err', __name__)
#.if 0:from seed.debug.print_err import print_err
#.lazy_import4funcs_('seed.helper.ifNone', 'ifNone,ifNonef', __name__)
#.if 0:from seed.helper.ifNone import ifNone,ifNonef
#.lazy_import4funcs_('seed.tiny_.funcs', 'echo,fst,snd', __name__)
#.if 0:from seed.tiny_.funcs import echo,fst,snd
#.lazy_import4funcs_('seed.types.Either', 'mk_Left,mk_Right', __name__)
#.if 0:from seed.types.Either import mk_Left,mk_Right #Either,Cased
#.
#.
#.flatten_recur = lazy_import4func_('seed.iters.flatten_recur', 'flatten_recur', __name__)
#.# def flatten_recur(g:Generator, /, *, value:object=None, is_exc=False, boxed=False):
#.
#.echo_or_mk_PeekableIterator = lazy_import4func_('seed.iters.PeekableIterator', 'echo_or_mk_PeekableIterator', __name__)
#.dot_ = lazy_import4func_('seed.func_tools.dot_', 'dot_', __name__)
#.
#.[mk_named_pseudo_tuple_,collect_tuple_subclasses_with_cached_property] = lazy_import4funcs_('seed.for_libs.for_collections.namedtuple__nontuple4cached_property', 'mk_named_pseudo_tuple_,collect_tuple_subclasses_with_cached_property', __name__)
#.if 0:from seed.for_libs.for_collections.namedtuple__nontuple4cached_property import mk_named_pseudo_tuple_
#.#def mk_named_pseudo_tuple_(__module__,typename, field_names, /):
#.#    def _check6make_(sf, /):
#.if 0:from seed.for_libs.for_collections.namedtuple__nontuple4cached_property import collect_tuple_subclasses_with_cached_property
#.#assert not (__:=collect_tuple_subclasses_with_cached_property(globals(), to_print_err=True)), __
#.#################################
#.
#.
#.from seed.types.LazyList import ToConcatLazyList, decorator4protocol4ToConcatLazyList_
#.from seed.types.LazyList import LazyList, LazyListError
#.from seed.types.LazyList import to_LazyList, to_LazyListIter
#.
#.
#.
#.
#.
#.from seed.helper.repr_input import repr_helper
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
#lazy_import4funcs_('z', '', __name__)
from z import *
