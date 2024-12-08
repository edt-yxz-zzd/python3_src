#__all__:goto
r'''[[[
py -m seed.tiny

/from \(seed[.]\)\@!
    py std lib move to seed.tiny_....
    eg: from seed.tiny_.types5py import mk_MapView, MapView, kwargs2Attrs, curry1

from seed.func_tools.dot2 import dot
view ../../python3_src/seed/func_tools/dot2.py
[[
NOTE:
    use dot[[...],] instead of dot[[...]]
        which <==> partial(...)

dot[f,g](*args, **kwargs)
    =[def]= f(g(*args, **kwargs))

dot[[f, arg...], g](*args, **kwargs)
    =[def]= f(args..., g(*args, **kwargs))

dot[[f, a...]:kw, g](*args, **kwargs)
    =[def]= f(a..., g(*args, **kwargs), **kw)

dot[[f, a...]:kw:[b...], g](*args, **kwargs)
    =[def]= f(a..., g(*args, **kwargs), b..., **kw)

dot[[f, a...]::[b...], g](*args, **kwargs)
    =[def]= f(a..., g(*args, **kwargs), b...)
]]

from seed.tiny import echo, print_err, mk_fprint, mk_assert_eq_f
from seed.tiny import fst, snd, at
from seed.tiny import mk_tuple, mk_frozenset, mk_immutable_seq
from seed.tiny import mk_pair, mk_pair_tuple, is_pair
from seed.tiny import check_tmay, check_pair, check_uint, check_imay, icheck_tmay, icheck_pair, icheck_uint, icheck_imay
from seed.tiny import check_type_le, check_type_is, icheck_type_le, icheck_type_is
from seed.tiny import check_pseudo_identifier, check_smay_pseudo_qual_name, check_pseudo_qual_name, icheck_pseudo_identifier, icheck_smay_pseudo_qual_name, icheck_pseudo_qual_name
from seed.tiny import check_callable, check_is_obj, check_is_None
from seed.tiny_.check import check_str, check_char
from seed.tiny import get_abstractmethod_names, check_manifest4abstractmethods

from seed.tiny import null_dev
from seed.tiny import null_context, null_context5result_
from seed.tiny import inf, pos_inf, neg_inf
from seed.tiny import null_str, null_bytes, null_int, null_tuple, null_frozenset, null_mapping_view, null_iter  #,    null_sequence, null_set, null_mapping
    from seed.types.FrozenDict import FrozenDict, empty_FrozenDict as null_FrozenDict
    from seed.types.empty_containers import EmptyMapping, EmptySet, EmptySequence, empty_mapping, empty_set, empty_sequence, empty_tuple, empty_iterator
    from seed.types.empty_containers import IndexError_KeyError
    from seed.types.empty_containers import EmptyHashableBase, EmptyIterable, EmptyReversible, EmptySized, EmptyContainer, EmptyCollection
    from seed.types.empty_containers import EmptyMapping, EmptySet, EmptySequence, EmptyThree
    from seed.types.empty_containers import theEmptyHashableBase, theEmptyIterable, theEmptySized, theEmptyContainer, theEmptyCollection, theEmptyReversible, theEmptyMapping, theEmptySet, theEmptySequence, theEmptyThree, empty_mapping, empty_set, empty_sequence, empty_three, empty_tuple, empty_iterator



from seed.tiny_.nmay5tmay import nmay5star_tmay_, nmay5tmay_, nmay2tmay_
def nmay5star_tmay_(*tmay_x, mix_ok=False):
def nmay5tmay_(tmay_x, /, *, mix_ok=False):
def nmay2tmay_(may_x, /):
    vs:
        seed.helper.get4may:nmay2tmay
        seed.helper.get4may:get4may
        ---
        seed.tiny_.mk_fdefault.eliminate_tmay__mix
        ---
def eliminate_tmay__mix(tmay_value, imay_xdefault_rank, xdefault, /, *args4xdefault):

def nmay2tmay(nmay, /):
def get4nmay(nmay, default, /):
def get4nmay__Nothing(Nothing, nmay, default, /):

from seed.helper.get4may import nmay2tmay__Nothing, nmay2tmay, get4nmay__Nothing, get4nmay, fget4nmay__Nothing, fget4nmay, fgetP4nmay__Nothing_, fgetP4nmay_, fget4nmay__human, fget4nmay__Nothing__human, xget4nmay_, xget4nmay__human

from seed.mapping_tools.fdefault import mapping_get__tmay_, mapping_get_fdefault__cased_, mapping_set_fdefault__cxxxvalue_, option2mapping_get__tmay

from seed.tiny_.mk_fdefault import mk_default
    #def mk_default(imay_xdefault_rank, xdefault, /,*args4xdefault):
from seed.tiny_.mk_fdefault import mk_default__easy, mk_default, mk_default_or_raise
    #def mk_default__easy(*tmay_Nothing___or___args4mk_default_or_raise, mirror=False):
    #def mk_default(imay_xdefault_rank, xdefault, /, *args4xdefault):
    #def mk_default_or_raise(mirror_imay_xedefault_rank, xedefault, /, *args4xedefault, mirror:bool):
    #   imay_xdefault_ranks = (-3)-mirror_imay_xedefault_rank if mirror_imay_xedefault_rank < -1 else mirror_imay_xedefault_rank
    #   mirrored = (mirror_imay_xedefault_rank < -1) ^ bool(mirror)
    #




from seed.tiny_.mk_fdefault import mk_fdefault, mk_default, eliminate_tmay__mix, eliminate_tmay_or_raise__simple, BasePermissionMappingOps, SimplePermissionMappingOps, XDefaultDict, ops4XDefaultMapping

from seed.tiny_.mk_fdefault import mk_fdefaultP, mk_fdefault, mk_fdefaultP_from_default, mk_fdefault_from_default, Mk_fdefaultP, Mk_fdefault, Mk_fdefault1__caller_args_at_last, Mk_fdefault1__caller_args_at_first, Mk_fdefaultP_from_default, Mk_fdefault_from_default, mk_default2value__default_at_last, mk_default2value__default_at_first, mk_tmay_from_default2value, mk_fvalue, mk_tmay_from_is_safe_fvalue, mk_tmay_from_try_fvalue, mk_tmay_from_try_fvalue_KeyError


from seed.tiny_.mk_fdefault import mk_default_or_raise, mirror_rank2imay_rank, mk_default_or_raise__ver1, mk_edefault__cased, eliminate_cased_edefault__raise, mk_default_or_raise__ver2, reform_args_from_mk_default_or_raise, raise4mk_default_or_raise, mk_default

from seed.tiny_.mk_fdefault import eliminate_tmay, eliminate_tmay__cased, eliminate_tmay__mix, eliminate_tmay_or_raise, eliminate_tmay_or_raise__simple

from seed.tiny_.mk_fdefault import BasePermissionMappingOps, SimplePermissionMappingOps, MappingOpsPermission, LazyValueCachedTransitionalObj, XDefaultMappingOps, ops4XDefaultMapping, WeakableXDefaultDict, XDefaultDict, XDefaultHashMappingMixin, XDefaultMappingMixin, MappingMixin__auto_setdefault_via_slice4HashMap

from seed.tiny import get5cls, call5cls, get5cls_, call5cls_


from seed.types.Namespace import namespace2items, namespace2keys, namespace2values
from seed.types.Namespace import MutabilityFlag4Namespace, mutability_flag2namespace_type
from seed.types.Namespace import Namespace, NamespaceSetOnce, NamespaceForbidOverwriteImplicitly, NamespaceForbidNewKey, NamespaceForbidSetitem, NamespaceForbidDelitem, NamespaceForbidAlterKeySet, NamespaceForbidModify



#]]]'''


from seed.helper.str2__all__ import str2__all__
__all__ = str2__all__(r'''
    oo                  # usage: +oo, -oo
    dict_add            # :: mapping -> k -> v -> is_new_key/bool
    set_add             # :: set -> k -> is_new_key/bool
    dict_update         # :: mapping -> view<mapping> -> are_all_new_keys/bool
    set_update          # :: set -> view<set> -> are_all_new_keys/bool

    strip_text_by_marker_pair
                        # :: str -> sep -> sep -> middle_gap
    cut_text_by_marker_seq
                        # :: str -> (*seps) -> [gap]
    repr_as_3dot        # [repr(repr_as_3dot) == '...']
    HEXReprInt          # subtype of int, __repr__ -> hex/0xF
    HexReprInt          # ===HEXReprInt
    LowHexReprInt       # subtype of int, __repr__ -> hex/0xf
    HEXReprInt__without_0x
                        # subtype of int, __repr__ -> hex/"F"
    no_op               # :: (*args, **kwargs) -> None
    next__tmay          # :: Iter a -> tmay a
    lookup__tmay        # :: Lookupable k v -> tmay v  # Lookupable := hasattr __getitem__ raise LookupError
    chains              # :: Iter (Iter a) -> Iter a
    count_              # count_(start=0, may_stop=None, /, step=1)
                        # diff:itertools.count(start=0, step=1)

    slice2triple        # :: slice -> (.start, .stop, .step)
    range2triple        # :: range -> (.start, .stop, .step)

    fix_slice_by_len    # :: length -> slice -> (.start, .stop, .step)
    fix_slice_by_len_of # :: seq -> slice -> (.start, .stop, .step)

    convert_triple_as_  # :: cls{tuple|range|slice} -> triple -> cls(.start, .stop, .step)

    slice2triple_       # :: cls -> slice -> cls(.start, .stop, .step)
    range2triple_       # :: cls -> slice -> cls(.start, .stop, .step)

    fix_slice_by_len_   # :: cls -> length -> slice -> cls(.start, .stop, .step)
    fix_slice_by_len_of_# :: cls -> seq -> slice -> cls(.start, .stop, .step)

    slice2item          # :: slice -> (.start, .stop) # .step is None
    slices2iter_items   # :: iter<slice> -> iter<(.start, .stop)> # .step is None
    slices2items        # :: iter<slice> -> tuple<(.start, .stop)> # .step is None
    slices2dict         # :: iter<slice> -> {.start: .stop} # .step is None
    items2dict__reject_duplicates
                        # iter<(k,v)> -> {k:v} #raise if duplicates occur

    check_Weakable      # :: obj -> None|raise TypeError
    is_Weakable         # :: obj -> bool
    WeakableDict        # <: Weakable&dict

    check_Hashable__shallow
    check_Hashable__deep
                        # :: obj -> None|raise TypeError
    is_Hashable__shallow
    is_Hashable__deep
                        # :: obj -> bool

    check_subscriptable
    icheck_subscriptable
        check_getitemable   # :: a -> None|raise TypeError
        icheck_getitemable  # :: a -> a|raise TypeError

    check_type_in       # :: [cls] -> a -> None|raise TypeError
    check_type_le       # :: cls -> a -> None|raise TypeError
    check_type_is       # :: cls -> a -> None|raise TypeError
    icheck_type_in      # :: [cls] -> a -> a|raise TypeError
    icheck_type_le      # :: cls -> a -> a|raise TypeError
    icheck_type_is      # :: cls -> a -> a|raise TypeError

    check_tmay          # :: a -> None|raise TypeError
    check_pair          # :: a -> None|raise TypeError
    check_either        # :: a -> None|raise TypeError
    check_uint          # :: a -> None|raise TypeError
    check_imay          # :: a -> None|raise TypeError
    icheck_tmay         # :: a -> a|raise TypeError
    icheck_pair         # :: a -> a|raise TypeError
    icheck_either       # :: a -> a|raise TypeError
    icheck_uint         # :: a -> a|raise TypeError
    icheck_imay         # :: a -> a|raise TypeError
    icheck_bool           # :: a -> None|raise TypeError

    check_pseudo_identifier
                        # :: a -> None|raise TypeError
    check_smay_pseudo_qual_name
                        # :: a -> None|raise TypeError
    check_pseudo_qual_name
                        # :: a -> None|raise TypeError
    icheck_pseudo_identifier
                        # :: a -> a|raise TypeError
    icheck_smay_pseudo_qual_name
                        # :: a -> a|raise TypeError
    icheck_pseudo_qual_name
                        # :: a -> a|raise TypeError

    check_callable      # :: a -> None|raise TypeError
    check_is_obj        # :: a -> a -> None|raise TypeError
    check_is_None       # :: a -> None|raise TypeError
    check_str           # :: a -> None|raise TypeError
    check_char          # :: a -> None|raise TypeError
    check_bool           # :: a -> None|raise TypeError

    get_abstractmethod_names
                        # :: cls -> frozenset<attr>
    check_manifest4abstractmethods
                        # :: cls -> str -> None|raise TypeError


    echo_key            # echo_key[k...] -> (k...)
    mk_frozenset        # :: Iter a -> frozenset a
    mk_tuple            # :: Iter a -> tuple a
    mk_pair_tuple       # :: Iter (Iter a) -> tuple (pair a)
    mk_pair             # :: Iter a -> pair a
    is_pair             # :: a -> bool
    mk_immutable_seq    # :: Iter a -> (tuple a | str | bytes | range)
    mk_reiterable       # :: Iter a -> ReIter a
    mk_reiterables      # :: Iter<Iter a> -> ReIter<ReIter a>
    mk_reiterable__depth_
                        # :: depth/uint -> Iter**(depth+1) a -> ReIter**(depth+1) a
                        # mk_reiterable__depth_ 0 <==> mk_reiterable
                        # mk_reiterable__depth_ 1 <==> mk_reiterables
    echo_args_kwargs    # :: (*args, **kwargs) -> (args, kwargs)
    echo_args           # :: *args -> args
    echo_kwargs         # :: (**kwargs) -> kwargs
    echo                # :: a -> a
    theEcho             # .__getattribute__ :: str -> str
    ifNone              # :: (None|a) -> default -> (a|default)
    ifNonef             # :: (None|a) -> (()->default) -> (a|default)

    catched_call__either
                        # :: may_Base4Exception -> calc_value -> (is_value, exc_vs_value)
                        # :: may Base<exc> -> (()->(value|raise exc)) -> ((False, exc)|(True, value))

    cached_catched_call__either
                        # :: may_cached_either -> may_Base4Exception -> calc_value -> set_cached_either -> (is_value, exc_vs_value)
                        # :: may either -> may Base<exc> -> (()->(value|raise exc)) -> (either->()) -> either

    get_or_cached_catched_call__either
                        # :: get_may_cached_either -> may_Base4Exception -> calc_value -> set_cached_either -> (is_value, exc_vs_value)
                        # :: (()->may either) -> may Base<exc> -> (()->(value|raise exc)) -> (either->()) -> either

    expectError         # :: Error -> (()->...) -> bool
    with_expect_error   # :: Error -> Error_if_no_exc -> contextmanager
    assert_eq           # :: lhs -> rhs -> (_fmt=...) -> **vars -> ()
    assert_eq_f         # :: ans -> f -> *args -> (_fmt=...) -> **vars -> ()
    mk_assert_eq_f      # :: (_fmt=...) -> **vars -> (ans -> f -> *args -> **kwargs -> ())


    null_dev            # fileobj mimic '/dev/null'
    null_context        # null_context<None> # with null_context as _None:pass
    null_context5result_# a -> null_context<a> # with null_context5result_(a) as a:pass
    inf                 # float
    pos_inf             # float
    neg_inf             # float
    null_str            # == ''
    null_bytes          # == b''
    null_int            # == 0
    null_tuple          # == ()
    null_frozenset      # == frozenset()
    null_mapping_view   # == MapView({})
    null_iter           # :: iter('') iter([])
    #null_sequence      # == seed.types.empty_containers.EmptySequence()
    #null_set           # == seed.types.empty_containers.EmptySet()
    #null_mapping       # == seed.types.empty_containers.EmptyMapping()

    mk_Just             # a -> (a,) # null_tuple as Nothing
    mk_Left             # a -> (False,a)
    mk_Right            # a -> (True,a)

    unbox_               # :: x -> (Iter a){len<2} -> (a|x)
    unbox               # :: (Iter a){len==1} -> a
    fst                 # :: (a, ...) -> a
    snd                 # :: (a, b, ...) -> b
    at                  # at[k](m) := m[k]
    const               # :: a -> b -> a
    ## vs operator.is_: tiny.is_ is curry
    eq                  # :: a -> (a -> bool)
    not_eq              # :: a -> (a -> bool)
    is_                 # :: a -> (a -> bool)
    not_is              # :: a -> (a -> bool)
    in_                 # :: xs -> (x -> bool)
    not_in              # :: xs -> (x -> bool)

    lazy                # :: a -> (() -> a)
    lazy_raise          # eg. get_fdefault(d, key, lazy_raise(KeyError, ...))
    lazy_raise_v        # raise exc
    lazy_raise_f        # raise mk_exc()

    str2__all__         # :: str -> [word]

    print_err           # file=sys.stderr; see: no_op/print_ferr
    print_ferr          # file=sys.stderr; see: no_op/print_err
    fprint              # force/require 'file='
    mk_fprint           # fixed 'file'
    __not__             # :: Testable a => a -> bool
    not_dot             # :: (a->bool) -> (a->bool)
    xor, xnor           # :: bool -> bool -> bool
    not_                # :: x -> (not x)
    with_if

    with_key            # :: (a->k) -> Iter a -> Iter (k, a)

    py_cmp              # :: Ord a => a -> a -> -> (-1|0|+1)
    int2cmp             # :: int -> (-1|0|+1)

    does_run_as_main    # :: String -> Bool
                        # does_run_as_main(__name__)
                        # does_run_as_main.alter_main_name :: String

    MapView             # === MappingProxyType
    mk_MapView          # mapping -> MappingProxyType # avoid (MapView . MapView)
    curry1              # ((sf, /, *args, **kwargs) -> r) -> sf -> ((*args, **kwargs) -> r)
    kwargs2Attrs        # (**kwargs) -> SimpleNamespace

    Namespace           # dict & attrs
    NamespaceSetOnce    # dict & attrs, each key set at most once
        NamespaceForbidOverwriteImplicitly
        NamespaceForbidNewKey
        NamespaceForbidSetitem
        NamespaceForbidDelitem
        NamespaceForbidAlterKeySet
        NamespaceForbidModify

    is_iterable         # a -> Bool
    is_iterator         # a -> Bool
    is_reiterable       # a -> Bool

    is_callable         # a -> Bool
    is_subscriptable    # a -> Bool
    is_container        # a -> Bool
    is_sized            # a -> Bool

    flip                # (a->b->r) -> (b->a->r)
    neg_flip            # (a->b->r) -> (b->a->-r)
    sign_of             # RealNumber -> (-1|0|+1)

    try_                # (*args->**kwargs->r) -> *args->**kwargs->tmay r
        #vs:seed.tiny_.mk_fdefault:mk_tmay_from_try_fvalue


    nmay5star_tmay_     # (*tmay x) -> (mix_ok=False) -> may x | ^TypeError # [mix_ok or not x is None]
    nmay5tmay_          # tmay x -> (mix_ok=False) -> may x | ^TypeError # [mix_ok or not x is None]
    nmay2tmay_          # may x -> tmay x

    boolexpr_wrapper    # (*args->**kwargs->(bool|err_ty)) -> *args->**kwargs->(bool|^TypeError)

    bmk_pairs           # bmk_pairs[1:2, :]
    bmk_triples         # bmk_triples[1:2:3, ::]
    show_ordered_pairs_as_bmk_pairs
                        # pairs -> 'bmk_pairs[...]'
    show_ordered_triples_as_bmk_triples
                        # triples -> 'bmk_triples[...]'
    bmk_OrderedDict     # bmk_OrderedDict[1:2, :]
    show_ordered_pairs_as_bmk_OrderedDict
                        # pairs -> 'bmk_OrderedDict[...]'
    show_ordered_dict_as_bmk_OrderedDict
                        # OrderedDict -> 'bmk_OrderedDict[...]'
    cased_bmk           # cased_bmk['{:}', 1:2] == {1:2}

    get_mro4cls         # cls -> __mro__
    get_dict4cls        # cls -> __dict__
    get_dict4obj        # obj -> __dict__
    iter_cls_member_pairs_in_mro_at
                        # cls -> key/name -> (*,apply_descriptor_protocol:bool) -> Iter (cls, member)


    call2bracket__EllipsisR__fst8func
        #call2bracket__EllipsisR__fst8func[f, 0, 1, 2, ..., 3:4, 5:6] ==>> f({3:4,5:6}, 0, 1, 2)
    get5cls             # get5cls.__f__(sf)(*args, **kwargs)
    call5cls            # call5cls.__f__(sf, *args, **kwargs)
    get5cls_            # get5cls_('__f__', sf)(*args, **kwargs)
    call5cls_           # call5cls_('__f__', sf, *args, **kwargs)



    str_join__list_nonemty
    str_join__entry_nonemty
    str_join__both_list_and_entry_may_be_emty
                        # sep -> Iter<str> -> str
    str_split__list_nonemty
    str_split__entry_nonemty
    str_split__both_list_and_entry_may_be_emty
                        # sep -> str -> [str]


    partition_xs_by_bool_
                        # may (x->bool) -> Iter x -> (bads/[x], goods/[x])
    xs_to_vss_          # sz/uint -> may (x->idx) -> may (x->v) -> Iter x -> tuple<[v]>{len=sz}
    xs_to_k2vs_         # may (x->idx) -> may (x->v) -> Iter x -> *may_k2vs_or_sz/(may (k2vs/{k:[v]} | sz/uint)) -> (k2vs | tuple<[v]>{len=sz})

    fmap4may            # (a->b) -> may a -> may b
    fmap4dict_value     # (a->b) -> dict<k,a> -> dict<k,b>
    filter4dict_value   # (v->bool) -> dict<k,v> -> dict<k,v>
    group4dict_value    # (Hashable g) => (v->g) -> dict<k,v> -> dict<g, dict<k,v> >
    dict_add__is        # dict<k,v> -> k -> v -> None
    dict_add__eq        # Eq v => dict<k,v> -> k -> v -> None
    dict_add__new       # Eq v => dict<k,v> -> k -> v -> None
    fmap4dict_value_with_key
                        # (k->a->b) -> dict<k,a> -> dict<k,b>
    filter4dict_value_with_key,filter4dict_item
                        # (k->v->bool) -> dict<k,v> -> dict<k,v>
    group4dict_value_with_key,group4dict_item
                        # (Hashable g) => (k->v->g) -> dict<k,v> -> dict<g, dict<k,v> >
    filter4dict_key     # (k->bool) -> dict<k,v> -> dict<k,v>
    group4dict_key      # (Hashable g) => (k->g) -> dict<k,v> -> dict<g, dict<k,v> >



    update_attr         # obj -> name -> (old->new) -> None
    iupdate_attrs       # obj -> Iter name -> (old->arg->new) -> {name:arg} ->  -> None
    set_attrs           # obj -> Iter name -> {key:new} -> may ((name->key)|str) -> None
    fwd_call            # (**kwargs->r) -> Iter name -> {name:arg} -> r

    prepare4set_attrs   # Iter name -> {key:new} -> may ((name->key)|str) -> Iter (name, new)

    CallCounter         # :: f -> wrap(f){.count, .func}
                        # count num_call
    default_cmp         # a->a->(-1/0/+1)
                        # cmp by (<)&(==)
                        # vs default_key = echo

    BaseTuple           # usage: class X(BaseTuple): def __init__(...): check(...)

    mk_SingletonClass   # module_qname -> type_qname -> *bases -> **kw -> SingletonClass
    mk_existing_type_singleton #cls -> None
    __new4singleton__   # used in SingletonClass.__new__
    __newobj__          #used in __reduce__,__reduce_ex__ for pickle

    iter_stop_with_
            # :: r -> Iter x -> Iter<StopIteration(r);x>
    GetStopIterationValue
            # .__iter__, .get_tmay_value5StopIteration
            # list(g:=GetStopIterationValue(iter_stop_with_(r, it)))
            # assert g.get_tmay_value5StopIteration()==(r,)

    class_property
        # types.DynamicClassAttribute(fget=None, fset=None, fdel=None, doc=None)
        # via cls.__getattr__
        # .deleter(self, fdel) -> new_sf
        # .getter(self, fget) -> new_sf
        # .setter(self, fset) -> new_sf

    #''')
__all__

from seed.math.sign_of import sign_of
from seed.helper.ifNone import ifNone, ifNonef
from seed.helper.Echo import echo, theEcho
from seed.helper.with_if import with_if
from seed.debug.expectError import expectError
from seed.debug.with_expect_error import with_expect_error
from seed.debug.print_err import print_err, print_ferr
from seed.debug.assert_eq import assert_eq, assert_eq_f, mk_assert_eq_f
from seed.debug.lazy_raise import lazy_raise


with with_expect_error(KeyError):
    raise KeyError
try:
    with with_expect_error(KeyError):
        raise SyntaxError
except SyntaxError:
    pass
else:
    raise 000
try:
    with with_expect_error(KeyError, IndexError):
        pass
except IndexError:
    pass
else:
    raise 000




from seed.func_tools.not_dot import __not__, not_dot
from seed.for_libs.next__tmay import next__tmay
from seed.for_libs.lookup__tmay import lookup__tmay
from seed.iters.chains import chains
from seed.iters.count_ import count_

from seed.tiny_.types5py import mk_MapView, MapView, kwargs2Attrs, curry1
#from types import MappingProxyType as MapView, SimpleNamespace as kwargs2Attrs, MethodType as curry1
  #SimpleNamespace(**kw)
from seed.types.Namespace import Namespace, NamespaceSetOnce
from seed.types.Namespace import Namespace, NamespaceSetOnce, NamespaceForbidOverwriteImplicitly, NamespaceForbidNewKey, NamespaceForbidSetitem, NamespaceForbidDelitem, NamespaceForbidAlterKeySet, NamespaceForbidModify

from seed.tiny_.update_attr import update_attr, iupdate_attrs, set_attrs, prepare4set_attrs, fwd_call

from seed.tiny_.HexReprInt import HEXReprInt__without_0x
from seed.tiny_.HexReprInt import HEXReprInt, HexReprInt, LowHexReprInt
from seed.tiny import HEXReprInt, HexReprInt, LowHexReprInt
assert HexReprInt is HEXReprInt
assert repr(HEXReprInt(15)) == '0xF'
assert repr(HEXReprInt(-15)) == '-0xF'
assert repr(LowHexReprInt(15)) == hex(15) == '0xf'
assert repr(LowHexReprInt(-15)) == hex(-15) == '-0xf'
assert repr(HEXReprInt__without_0x(15)) == 'F' == f'{(15):X}'
assert repr(HEXReprInt__without_0x(-15)) == '-F' == f'{(-15):X}'

assert curry1(isinstance, 1)(int)
assert not curry1(isinstance, 1)(str)
assert curry1(int.__add__, 1)(5) == 6

#vivi fst, snd
from seed.tiny_.at import at
assert at[1]('ab') == 'b'
assert at(1)('ab') == 'b'
assert {at}
assert {at[0]}


r"""template
e ../../python3_src/seed/tiny_/at.py
from seed.tiny_.at import at
#from seed.tiny_.at import at
__all__ = '''
    at
    '''.split()
#"""


from seed.tiny_.echo_key import echo_key


from seed.tiny_.slice2triple import slice2triple
assert slice2triple(slice(3, 9, 2)) == (3, 9, 2)
from seed.tiny_.slice2triple import slice2triple, slice2item, slices2iter_items, slices2items, slices2dict, items2dict__reject_duplicates
from seed.tiny_.slice2triple import slice2triple, fix_slice_by_len, fix_slice_by_len_of
from seed.tiny_.slice2triple import slice2triple_, fix_slice_by_len_, fix_slice_by_len_of_
from seed.tiny_.slice2triple import slice2triple, range2triple, convert_triple_as_, range2triple_, slice2triple_


assert (0,4,1) == fix_slice_by_len(4, echo_key[:])
assert (4-1,-1,-1) == fix_slice_by_len(4, echo_key[::-1])
assert (4-1,-1,-1) == fix_slice_by_len_of(range(4), echo_key[::-1])
assert (4-1,-1,-1) == fix_slice_by_len_of_(tuple, range(4), echo_key[::-1])
assert range(4-1,-1,-1) == fix_slice_by_len_of_(range, range(4), echo_key[::-1])


from seed.tiny_.check import check_subscriptable, icheck_subscriptable
from seed.tiny_.check import check_getitemable, icheck_getitemable
assert check_getitemable is check_subscriptable
assert icheck_getitemable is icheck_subscriptable
assert expectError(TypeError, lambda:check_subscriptable(set()))
assert check_subscriptable('') is None

from seed.tiny_.check import check_type_le, check_type_is, check_tmay, check_pair, check_either, check_uint, check_imay, icheck_type_le, icheck_type_is, icheck_tmay, icheck_pair, icheck_either, icheck_uint, icheck_imay
from seed.tiny_.check import check_type_in, icheck_type_in
from seed.tiny_.check import check_pseudo_identifier, check_smay_pseudo_qual_name, check_pseudo_qual_name, icheck_pseudo_identifier, icheck_smay_pseudo_qual_name, icheck_pseudo_qual_name
from seed.tiny_.check import check_callable, check_is_obj, check_is_None
from seed.tiny_.check import check_str, check_char
from seed.tiny_.check import check_bool, icheck_bool



check_uint(1)
check_tmay(())
check_tmay((0,))
check_pair((0, 0))
check_type_is(str, '')
check_type_le(object, '')
check_type_in([int, str], '')
assert 1 == icheck_uint(1)
assert (0,) == icheck_tmay((0,))
assert (0,0) == icheck_pair((0, 0))
assert '' == icheck_type_is(str, '')
assert '' == icheck_type_le(object, '')
assert '' == icheck_type_in([int, str], '')


assert 'class'.isidentifier()
assert 'def'.isidentifier()
check_pseudo_identifier('def')
check_smay_pseudo_qual_name('')
check_smay_pseudo_qual_name('x')
check_smay_pseudo_qual_name('x.def')
check_pseudo_qual_name('x')
check_pseudo_qual_name('x.def')
assert expectError(TypeError, lambda:check_pseudo_identifier(''))
assert expectError(TypeError, lambda:check_pseudo_identifier(' '))
assert expectError(TypeError, lambda:check_pseudo_identifier('.x'))

assert expectError(TypeError, lambda:check_smay_pseudo_qual_name(' '))
assert expectError(TypeError, lambda:check_smay_pseudo_qual_name('.x'))

assert expectError(TypeError, lambda:check_pseudo_qual_name(''))

check_str('')
check_char('+')
assert expectError(TypeError, lambda:check_str(b''))
assert expectError(TypeError, lambda:check_char(b''))
assert expectError(TypeError, lambda:check_char(''))
assert expectError(TypeError, lambda:check_char('ab'))



from seed.tiny_.nmay5tmay import nmay5star_tmay_, nmay5tmay_, nmay2tmay_


assert expectError(TypeError, lambda:nmay5star_tmay_(None))
assert expectError(TypeError, lambda:nmay5star_tmay_(999, 777))
assert 999 == nmay5star_tmay_(999)
assert None is nmay5star_tmay_()
assert None is nmay5star_tmay_(None, mix_ok=True)


assert expectError(TypeError, lambda:nmay5tmay_((None,)))
assert expectError(TypeError, lambda:nmay5tmay_([999]))
assert expectError(TypeError, lambda:nmay5tmay_((999, 777)))
assert 999 == nmay5tmay_((999,))
assert None is nmay5tmay_(())
assert () == nmay2tmay_(None)
assert (999,) == nmay2tmay_(999)





from seed.tiny_.null_dev import null_dev
from seed.tiny_.null_dev import null_context, null_context5result_

from seed.tiny_.constants import inf, pos_inf, neg_inf

from seed.tiny_.containers import null_str, null_bytes, null_int, null_tuple, null_frozenset, null_mapping_view, null_iter, mk_frozenset, mk_tuple, mk_Just, mk_Left, mk_Right
from seed.tiny_.containers import mk_pair, mk_pair_tuple
from seed.tiny_.containers import is_pair


assert mk_pair(__:=(1,2)) is __
assert not mk_pair(__:=[1,2]) is __
assert mk_pair_tuple(__:=((1,2),(1,2))) is __
assert not mk_pair_tuple(__:=((1,2),[1,2])) is __
assert is_pair((1,2))
assert not is_pair((1,2,3))
assert not is_pair([1,2])
assert not is_pair(1)

assert mk_tuple([]) is null_tuple
assert mk_frozenset([]) is null_frozenset
assert null_str == ''
assert null_bytes == b''
assert null_int == 0
assert null_tuple == ()
assert null_frozenset == frozenset()
assert type(null_mapping_view) is MapView and not null_mapping_view
assert iter(null_iter) is null_iter
assert next(null_iter, [..., {}]) == [..., {}]
assert next(null_iter, None) is None


#null_iter = empty_iterator
#null_tuple = empty_tuple
#null_sequence = empty_sequence
#null_set = empty_set
#null_mapping = empty_mapping

from seed.tiny_.containers import mk_immutable_seq
assert mk_immutable_seq('') is null_tuple
assert mk_immutable_seq(b'') is null_tuple
assert mk_immutable_seq(range(9,9)) is null_tuple
assert mk_immutable_seq(()) is null_tuple

assert mk_immutable_seq(__:='a') is __
assert mk_immutable_seq(__:=b'a') is __
assert mk_immutable_seq(__:=range(999)) is __
assert mk_immutable_seq(__:=(999,)) is __
assert mk_immutable_seq([999]) == (999,)






from seed.tiny_.mk_reiterable import mk_reiterable, mk_reiterables, mk_reiterable__depth_
assert mk_reiterable([0, {}, null_iter]) == [0, {}, null_iter]
assert mk_reiterables([{}, null_iter, []]) == ({}, (), [])
assert mk_reiterables(iter([{}, null_iter, []])) == ({}, (), [])


from seed.tiny_.funcs import no_op, echo_args_kwargs, echo_kwargs, echo_args, echo, unbox_, unbox, fst, snd, const, lazy, lazy_raise_v, lazy_raise_f, eq, not_eq, is_, not_is, in_, not_in, flip, neg_flip, xor, xnor, not_, with_key, mk_fprint, fprint, py_cmp, int2cmp
from seed.debug.lazy_raise import lazy_raise

#from collections.abc import Iterable, Iterator
from seed.tiny_.verify import is_iterable, is_iterator, is_reiterable
from seed.tiny_.verify import is_callable, is_subscriptable, is_container, is_sized

assert is_iterable(null_tuple)
assert is_reiterable(null_tuple)
assert not is_iterator(null_tuple)

assert is_iterable(null_iter)
assert not is_reiterable(null_iter)
assert is_iterator(null_iter)


assert is_callable(id)
assert not is_callable([])
assert is_subscriptable([])
assert not is_subscriptable(set())
assert not is_subscriptable(1)
assert is_container([])
assert is_container(set())
assert not is_container(1)
assert is_sized([])
assert is_sized(set())
assert not is_sized(1)

assert next__tmay(null_iter) == ()
assert expectError(TypeError, lambda:next__tmay([1]))
assert expectError(TypeError, lambda:next([1]))


from seed.tiny_.try_ import try_
#vs: #from seed.tiny_.mk_fdefault import mk_tmay_from_try_fvalue
assert try_(list.index, [], 999) == ()
assert try_(list.index, [777,999,888,666], 999) == (1,)


from seed.tiny_.boolexpr_wrapper import boolexpr_wrapper
assert expectError(TypeError, lambda:boolexpr_wrapper(int)(1))
assert expectError(TypeError, lambda:boolexpr_wrapper(int)(0))
assert boolexpr_wrapper(bool)(1) is True
assert boolexpr_wrapper(bool)(0) is False


from seed.tiny_.catched_call__either import catched_call__either, cached_catched_call__either, get_or_cached_catched_call__either
assert icheck_pair(catched_call__either(StopIteration, lambda:next(iter([1])))) == (True, 1)
assert icheck_pair(catched_call__either(StopIteration, lambda:next(null_iter)))[0] is False
assert type(icheck_pair(catched_call__either(StopIteration, lambda:next(null_iter)))[1]) is StopIteration
assert cached_catched_call__either((True, 1), None, None, None) == (True, 1)
assert cached_catched_call__either((False, Exception), None, None, None) == (False, Exception)
assert (lambda ls: (icheck_pair(cached_catched_call__either(None, None, lazy(1), ls.append)), ls))([]) == ((True, 1), [(True, 1)])
assert (lambda ls: (icheck_pair(get_or_cached_catched_call__either(lambda: ls[-1] if ls else None, None, lazy(1), ls.append)), ls))([]) == ((True, 1), [(True, 1)])
from seed.tiny import catched_call__either, cached_catched_call__either, get_or_cached_catched_call__either


from seed.tiny_.Weakable import check_Weakable, is_Weakable, WeakableDict
assert is_Weakable(frozenset())
assert is_Weakable(set())
assert not is_Weakable(())
assert not is_Weakable([])
assert not is_Weakable({})
assert not is_Weakable(dict())
assert is_Weakable(WeakableDict())

assert expectError(TypeError, lambda:check_Weakable(()))
assert not expectError(TypeError, lambda:check_Weakable(set()))

from seed.tiny_.Hashable import check_Hashable__shallow, is_Hashable__shallow, check_Hashable__deep, is_Hashable__deep
assert not is_Hashable__deep((1, []))
assert is_Hashable__shallow((1, []))


assert is_Hashable__deep(frozenset())
assert is_Hashable__deep(())
assert is_Hashable__deep((1, False))
assert not is_Hashable__deep([])
assert not is_Hashable__deep({})

assert is_Hashable__shallow(frozenset())
assert is_Hashable__shallow(())
assert is_Hashable__shallow((1, False))
assert not is_Hashable__shallow([])
assert not is_Hashable__shallow({})


from seed.tiny_.check_abc import get_abstractmethod_names, check_manifest4abstractmethods
from seed.tiny_.bmk_pairs import bmk_pairs, bmk_triples, show_ordered_pairs_as_bmk_pairs, show_ordered_triples_as_bmk_triples, bmk_OrderedDict, show_ordered_pairs_as_bmk_OrderedDict, show_ordered_dict_as_bmk_OrderedDict, cased_bmk


from seed.tiny_.get_mro import get_mro4cls, get_dict4cls, get_dict4obj, iter_cls_member_pairs_in_mro_at



from seed.tiny_.call2bracket import call2bracket__EllipsisR__fst8func#, IBracket8Call, Call2Bracket, call4call2bracket__fst8func, call4call2bracket__WechoW, interpreter4call2bracket__IechoW, interpreter4call2bracket__EllipsisR, split_bracket_args__sep_tail_by_Ellipsis, split_bracket_args__sepR_by_not_slice, split_bracket_args__sepL_by_not_slice
call2bracket__EllipsisR__fst8func
r'''
IBracket8Call
Call2Bracket
call4call2bracket__fst8func
call4call2bracket__WechoW
interpreter4call2bracket__IechoW
interpreter4call2bracket__EllipsisR


split_bracket_args__sep_tail_by_Ellipsis
split_bracket_args__sepR_by_not_slice
split_bracket_args__sepL_by_not_slice
#'''
from seed.tiny_.call2getattr import get5cls, call5cls, get5cls_, call5cls_#, Call2GetAttrs, IGetAttr8Call, Call2GetAttr, interpreter4Call2GetAttr__unpack_and_call, interpreter4Call2GetAttr__MethodType
assert get5cls.__getitem__([1])(0) == 1
assert call5cls.__getitem__([1], 0) == 1
assert get5cls_('__getitem__', [1])(0) == 1
assert call5cls_('__getitem__', [1], 0) == 1



from seed.tiny_.str__split_join import str_join__list_nonemty, str_split__list_nonemty, str_join__entry_nonemty, str_split__entry_nonemty, str_join__both_list_and_entry_may_be_emty, str_split__both_list_and_entry_may_be_emty

from seed.tiny_.group__partition import partition_xs_by_bool_, xs_to_vss_, xs_to_k2vs_

assert xs_to_k2vs_(fst, snd, [(1,2),(3,4),(1,999,5),(3,4),(5,6)]) == {1: [2, 999], 3: [4, 4], 5: [6]}
assert xs_to_vss_(4, len, snd, [(1,2),(3,4),(1,999,5),(3,4),(5,6)]) == ([], [], [2, 4, 4, 6], [999])
assert partition_xs_by_bool_(None, [0,1,-2,False, ...,True, None,[],(),[3]]) == ([0, False, None, [], ()], [1, -2, Ellipsis, True, [3]])


from seed.tiny_.fmap4may import fmap4may

from seed.tiny_.dict__add_fmap_filter import fmap4dict_value, filter4dict_value, dict_add__is, dict_add__eq, dict_add__new, group4dict_value
from seed.tiny_.dict__add_fmap_filter import fmap4dict_value_with_key, filter4dict_value_with_key, group4dict_value_with_key, filter4dict_item, group4dict_item

from seed.tiny_.dict__add_fmap_filter import filter4dict_key, group4dict_key
assert filter4dict_value(bool, {0: 1, 1: 0}) == {0: 1}
assert filter4dict_key(bool, {0: 1, 1: 0}) == {1: 0}
assert group4dict_key(len, {'':0, '1':1, ():0, '22':2}) == {0:{'':0, ():0}, 1:{'1':1}, 2:{'22':2}}


from seed.tiny_.CallCounter import CallCounter
from seed.tiny_.default_cmp import default_cmp

from seed.tiny_.BaseTuple import BaseTuple
from seed.tiny import BaseTuple

from seed.tiny_.singleton import mk_SingletonClass, mk_existing_type_singleton
from seed.tiny_.singleton import __newobj__, __new4singleton__

from seed.tiny_.iter_stop_with_ import iter_stop_with_, GetStopIterationValue
from seed.tiny_.class_property import class_property

from seed.helper.ConstantRepr import repr_as_3dot #ConstantRepr
assert repr(repr_as_3dot) == '...'
assert repr(...) == 'Ellipsis'


from seed.str_tools.cut_text_by_marker_seq import cut_text_by_marker_seq, strip_text_by_marker_pair
assert cut_text_by_marker_seq('abcdefg', *'bdf') == [*'aceg']
assert cut_text_by_marker_seq('abcde', *'bd') == [*'ace']
assert strip_text_by_marker_pair('abcde', *'bd') == 'c'


from seed.tiny_.dict_op__add import dict_add, set_add, dict_update, set_update
assert dict_add({}, 222, 333)
assert not dict_add({222:111}, 222, 333)
assert not dict_add({222:333}, 222, 333)


from seed.tiny_.oo8inf import oo









def does_run_as_main(__name__):
    '''to replace '__name__ == "__main__"'

usage:
    if __name__ == '__main__':
        ...
    # now become:
    if does_run_as_main(__name__):
        ...
why?
    # is this valid?: runpy.run_path(py_fname, run_name = '__main__')
    runpy.run_path(py_fname, run_name = '<runpy>.__run_as_main__')

why '.__run_as_main__' instead of '.__main__'
    since '__main__.py' exists
    and we assume __run_as_main__ does not exist
'''
    #return (__name__ in ('__main__', '__run_as_main__')
    return (__name__ == '__main__'
            or (__name__.endswith('.__run_as_main__')
                and '<' in __name__
                and '>' in __name__
                )
            )
does_run_as_main.alter_main_name = '__run_as_main__'





r'''see: seed.ECHO

ECHO = theEcho
def __register(qname, pseudo_module):
    import sys
    m = sys.modules.setdefault(qname, pseudo_module)
    if m is not pseudo_module:
        raise ImportError('qname: {qname!r} already exists')

def __register_ECHO():
    qname_ECHO = '.'.join([__name__, 'ECHO'])
    __register(qname_ECHO, theEcho)

    #from seed.tiny.theEcho import x, y, z # ERROR
    from seed.tiny.ECHO import x, y, z
    assert x == 'x'

    E = __import__(qname_ECHO, fromlist='xyz')
    assert E.x == 'x'
    assert E is ECHO
__register_ECHO()
del __register_ECHO, __register

    # seed.tiny.ECHO is a virtual module
    # from seed.tiny.ECHO import x,y,z
#'''


from seed.tiny import *
