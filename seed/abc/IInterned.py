#__all__:goto
r'''[[[
e ../../python3_src/seed/abc/IInterned.py

seed.abc.IInterned
py -m nn_ns.app.debug_cmd   seed.abc.IInterned -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.abc.IInterned:__doc__ -ht # -ff -df
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.abc.IInterned:cls@T    =T   +exclude_attrs5listed_in_cls_doc
#######
from seed.pkg_tools.ModuleReloader import mk_doctestXmodule_reloader_
doctestXmodule_reloader = mk_doctestXmodule_reloader_('', 'seed.abc.IInterned:__doc__', '-ht')
doctestXmodule_reloader(reload_first=False)
doctestXmodule_reloader()
#######

[[
sys.intern()
pickle
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.abc.IInterned   @f
from seed.abc.IInterned import *
]]]'''#'''
__all__ = r'''
IInterned
    IInterned__wrapped_obj
        Interned__wrapped_id8hash
        Interned__wrapped_hashable



IInterned
    name4dict4class_intern
    symbol4interned4instance
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from functools import cached_property
#.from itertools import islice
from seed.tiny_.check import check_type_is, check_int_ge
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
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
#.with mk_ctx4lazy_import4funcs_(__name__, 'ifNone:_ifNone, ifNonef:_ifNonef'):
#.    from seed.helper.ifNone import ifNone as _ifNone, ifNonef as _ifNonef
with mk_ctx4lazy_import4funcs_(__name__):
    from weakref import WeakValueDictionary
    from seed.types.FrozenDict import mk_FrozenDict #FrozenDict
    from seed.helper.repr_input import repr_helper
    from seed.tiny_.containers import mk_tuple#mk_immutable_seq,mk_immutable_seq5iterT_,mk_immutable_seq5iter__,mk_bytes5iter_,mk_tuple__split_first_if_str #xxx:null_tuple
#.    from seed.tiny_.types5py import mk_MapView,curry1,kwargs2Attrs #,MapView
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


#dict4global_intern = WeakValueDictionary()

name4dict4class_intern = '__dict4class_intern__'
class symbol4interned4instance:pass
class IInterned(ABC):
    '# see:sys.intern() # required:__weakref__{WeakValueDictionary},__dict__{cached_property}'
    __slots__ = ()
    #@classmethod
    @abstractmethod
    def __mk7unintern__(cls, cls7__new__, /, *std_args4mk, **std_kwds4mk):
        'cls{#type of result#} -> cls{#whose __new__ is calling#} -> (*std_args4mk) -> (**std_kwds4mk) -> -> sf{uninterned}'
    @abstractmethod
    def __get_std_xargs4mk__(sf, /):
        '-> (std_args4mk, std_kwds4mk)'
    @abstractmethod
    def __get_key4eq__(sf, /):
        '-> key4eq{sf}{hashable}{neednot type(sf)}'
        (std_args4mk, std_kwds4mk) = type(sf).__get_std_xargs4mk__(sf)
        return (mk_tuple(std_args4mk), mk_FrozenDict(std_kwds4mk))
    @classmethod
    #@abstractmethod
    def __std_xargs4mk__(cls, /, *args4mk, **kwds4mk):
        '(*args4mk) -> (**kwds4mk) -> (std_args4mk, std_kwds4mk)'
        (std_args4mk, std_kwds4mk) = (args4mk, kwds4mk)
        return (std_args4mk, std_kwds4mk)
    @classmethod
    #@abstractmethod
    def __check_std_xargs4mk__(cls, /, *std_args4mk, **std_kwds4mk):
        '(*std_args4mk) -> (**std_kwds4mk) -> None|^Exception'
        777;pass
        return None
    #@abstractmethod
    def __getnewargs_ex__(sf, /):
        '-> (std_args4mk, std_kwds4mk) #see:pickle'
        (std_args4mk, std_kwds4mk) = type(sf).__get_std_xargs4mk__(sf)
        return (std_args4mk, std_kwds4mk)
    @cached_property
    def _key4eq_(sf, /):
        '-> key4eq{sf}{hashable}{neednot type(sf)}'
        cls = type(sf)
        k = cls.__get_key4eq__(sf)
        return k
    @cached_property
    def _hash_(sf, /):
        '-> int'
        cls = type(sf)
        k = sf._key4eq_
        h = hash((id(cls), k))
        return h
    def __hash__(sf, /):
        return sf._hash_
    def __eq__(sf, ot, /):
        if sf is ot:
            return True
        if not type(sf) is type(ot):
            return False
        if not hash(sf) is hash(ot):
            return False
        return sf._key4eq_ == ot._key4eq_
    def __repr__(sf, /):
        (std_args4mk, std_kwds4mk) = type(sf).__getnewargs_ex__(sf)
        return repr_helper(sf, *std_args4mk, **std_kwds4mk)
    @property
    def _interned_(sf, /):
        '-> bool'
        d = sf.__dict__
        k = symbol4interned4instance
        return d.get(k, False)
    @_interned_.setter
    def _interned_(sf, interned, /):
        check_type_is(bool, interned)
        d = sf.__dict__
        k = symbol4interned4instance
        d[k] = interned


    def __new__(cls, /, *args4mk, **kwds4mk):
        '(*args4mk) -> (**kwds4mk) -> sf{interned}'
        sf = cls.__mk7intern__(cls, __class__, *args4mk, **kwds4mk)
        return sf
    def __intern__(sf7uninterned, /):
        'sf{uninterned} -> sf{interned}'
        if sf7uninterned._interned_:
            sf7interned = sf7uninterned
            return sf7interned

        cls = type(sf7uninterned)
        nm = name4dict4class_intern
        if 0:
            td = cls.__dict__ # type scope
            wd = td.setdefault(nm, WeakValueDictionary())
                #^AttributeError: 'mappingproxy' object has no attribute 'setdefault'
            777; del td
        else:
            m = getattr(cls, nm, None)
            if m is None:
                setattr(cls, nm, WeakValueDictionary())
                m = getattr(cls, nm)
                assert not m is None
            wd = m
        wd
        #k = cls.__get_key4eq__(sf7uninterned)
        k = sf7uninterned._key4eq_
        sf7interned = wd.setdefault(k, sf7uninterned)
        777; sf7uninterned._interned_ = sf7uninterned is sf7interned
        777; del sf7uninterned
        check_type_is(cls, sf7interned)
        return sf7interned
    #@classmethod
    def __mk7intern__(cls, cls7__new__, /, *args4mk, **kwds4mk):
        'cls{#type of result#} -> cls{#whose __new__ is calling#} -> (*args4mk) -> (**kwds4mk) -> sf{interned}'
        (std_args4mk, std_kwds4mk) = cls.__std_xargs4mk__(*args4mk, **kwds4mk)
        777; del args4mk, kwds4mk
        cls.__check_std_xargs4mk__(*std_args4mk, **std_kwds4mk)
        sf7uninterned = cls.__mk7unintern__(cls, cls7__new__, *std_args4mk, **std_kwds4mk)
        sf7interned = cls.__intern__(sf7uninterned)
        assert sf7interned._interned_
        return sf7interned

#end-class IInterned(ABC):
class IInterned__wrapped_obj(IInterned):
    __slots__ = ()
    @override
    def __get_std_xargs4mk__(sf, /):
        '-> (std_args4mk, std_kwds4mk)'
        std_args4mk = (sf.the_wrapped_obj,)
        std_kwds4mk = {}
        return (std_args4mk, std_kwds4mk)
    #@classmethod
    @override
    #.def __mk7unintern__(cls, cls7__new__, /, *std_args4mk, **std_kwds4mk):
    def __mk7unintern__(cls, cls7__new__, wrapped, /):
        'cls{#type of result#} -> cls{#whose __new__ is calling#} -> wrapped -> -> sf{uninterned}'
        #特化自:'cls{#type of result#} -> cls{#whose __new__ is calling#} -> (*std_args4mk) -> (**std_kwds4mk) -> -> sf{uninterned}'
        #sf7uninterned = super(__class__, cls).__new__(cls)
        #sf7uninterned = super(IInterned, cls).__new__(cls)
        sf7uninterned = super(cls7__new__, cls).__new__(cls)
        sf7uninterned._wrapped = wrapped
        return sf7uninterned
    #xxx:def __init__(sf, wrapped, /): sf._wrapped = wrapped
    @property
    def the_wrapped_obj(sf, /):
        return sf._wrapped
#end-class IInterned__wrapped_obj(IInterned):

class Interned__wrapped_id8hash(IInterned__wrapped_obj):
    ___no_slots_ok___ = True

    @override
    def __get_key4eq__(sf, /):
        '-> key4eq{sf}{hashable}{neednot type(sf)}'
        return id(sf.the_wrapped_obj)
#end-class Interned__wrapped_id8hash(IInterned__wrapped_obj):
if 1:
    hash(Interned__wrapped_id8hash([]))



class Interned__wrapped_hashable(IInterned__wrapped_obj):
    ___no_slots_ok___ = True

    @override
    def __get_key4eq__(sf, /):
        '-> key4eq{sf}{hashable}{neednot type(sf)}'
        return (sf.the_wrapped_obj)
#end-class Interned__wrapped_hashable(IInterned__wrapped_obj):
if 1:
    hash(Interned__wrapped_hashable(''))














__all__
from seed.abc.IInterned import *
