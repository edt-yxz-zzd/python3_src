
r'''
py -m seed.tiny

from seed.tiny import echo, print_err, mk_fprint, mk_assert_eq_f
from seed.tiny import fst, snd, at
from seed.tiny import mk_tuple, mk_frozenset
from seed.tiny import check_tmay, check_pair, check_uint, check_imay, icheck_tmay, icheck_pair, icheck_uint, icheck_imay
from seed.tiny import check_type_le, check_type_is, icheck_type_le, icheck_type_is
from seed.tiny import check_pseudo_identifier, check_smay_pseudo_qual_name, check_pseudo_qual_name, icheck_pseudo_identifier, icheck_smay_pseudo_qual_name, icheck_pseudo_qual_name
from seed.tiny import check_callable, check_is_obj, check_is_None
from seed.tiny import get_abstractmethod_names, check_manifest4abstractmethods

from seed.tiny import null_str, null_bytes, null_int, null_tuple, null_frozenset, null_mapping_view, null_iter  #,    null_sequence, null_set, null_mapping
    from seed.types.FrozenDict import FrozenDict, empty_FrozenDict as null_FrozenDict
    from seed.types.empty_containers import EmptyMapping, EmptySet, EmptySequence, empty_mapping, empty_set, empty_sequence, empty_tuple, empty_iterator
    from seed.types.empty_containers import IndexError_KeyError
    from seed.types.empty_containers import EmptyHashableBase, EmptyIterable, EmptyReversible, EmptySized, EmptyContainer, EmptyCollection
    from seed.types.empty_containers import EmptyMapping, EmptySet, EmptySequence, EmptyThree
    from seed.types.empty_containers import theEmptyHashableBase, theEmptyIterable, theEmptySized, theEmptyContainer, theEmptyCollection, theEmptyReversible, theEmptyMapping, theEmptySet, theEmptySequence, theEmptyThree, empty_mapping, empty_set, empty_sequence, empty_three, empty_tuple, empty_iterator



from seed.helper.get4may import nmay2tmay__Nothing, nmay2tmay, get4nmay__Nothing, get4nmay, fget4nmay__Nothing, fget4nmay, fgetP4nmay__Nothing_, fgetP4nmay_, fget4nmay__human, fget4nmay__Nothing__human, xget4nmay_, xget4nmay__human
from seed.mapping_tools.fdefault import mapping_get__tmay_, mapping_get_fdefault__cased_, mapping_set_fdefault__cxxxvalue_, option2mapping_get__tmay

from seed.tiny_.mk_fdefault import mk_fdefault, mk_default, eliminate_tmay__mix, eliminate_tmay_or_raise__simple, BasePermissionMappingOps, SimplePermissionMappingOps, XDefaultDict, ops4XDefaultMapping

from seed.tiny_.mk_fdefault import mk_fdefaultP, mk_fdefault, mk_fdefaultP_from_default, mk_fdefault_from_default, Mk_fdefaultP, Mk_fdefault, Mk_fdefault1__caller_args_at_last, Mk_fdefault1__caller_args_at_first, Mk_fdefaultP_from_default, Mk_fdefault_from_default, mk_default2value__default_at_last, mk_default2value__default_at_first, mk_tmay_from_default2value, mk_fvalue, mk_tmay_from_is_safe_fvalue, mk_tmay_from_try_fvalue, mk_tmay_from_try_fvalue_KeyError


from seed.tiny_.mk_fdefault import mk_default_or_raise, mirror_rank2imay_rank, mk_default_or_raise__ver1, mk_edefault__cased, eliminate_cased_edefault__raise, mk_default_or_raise__ver2, reform_args_from_mk_default_or_raise, raise4mk_default_or_raise, mk_default

from seed.tiny_.mk_fdefault import eliminate_tmay, eliminate_tmay__cased, eliminate_tmay__mix, eliminate_tmay_or_raise, eliminate_tmay_or_raise__simple

from seed.tiny_.mk_fdefault import BasePermissionMappingOps, SimplePermissionMappingOps, MappingOpsPermission, LazyValueCachedTransitionalObj, XDefaultMappingOps, ops4XDefaultMapping, WeakableXDefaultDict, XDefaultDict, XDefaultHashMappingMixin, XDefaultMappingMixin, MappingMixin__auto_setdefault_via_slice4HashMap

from seed.tiny import get5cls, call5cls, get5cls_, call5cls_


#'''


from seed.helper.str2__all__ import str2__all__
__all__ = str2__all__(r'''
    HexReprInt          # subtype of int, __repr__ -> hex
    no_op               # :: (*args, **kwargs) -> None
    next__tmay          # :: Iter a -> tmay a
    lookup__tmay        # :: Lookupable k v -> tmay v  # Lookupable := hasattr __getitem__ raise LookupError

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
    WeakableDict        # :: obj -> bool
    check_type_le       # <: Weakable&dict
    check_type_is       # :: cls -> a -> None|raise TypeError
    icheck_type_le      # :: cls -> a -> a|raise TypeError
    icheck_type_is      # :: cls -> a -> a|raise TypeError

    check_tmay          # :: a -> None|raise TypeError
    check_pair          # :: a -> None|raise TypeError
    check_uint          # :: a -> None|raise TypeError
    check_imay          # :: a -> None|raise TypeError
    icheck_tmay          # :: a -> a|raise TypeError
    icheck_pair          # :: a -> a|raise TypeError
    icheck_uint          # :: a -> a|raise TypeError
    icheck_imay          # :: a -> a|raise TypeError

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

    get_abstractmethod_names
                        # :: cls -> frozenset<attr>
    check_manifest4abstractmethods
                        # :: cls -> str -> None|raise TypeError


    echo_key            # echo_key[k...] -> (k...)
    mk_frozenset        # :: Iter a -> frozenset a
    mk_tuple            # :: Iter a -> tuple a
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
    assert_eq           # :: lhs -> rhs -> (_fmt=...) -> **vars -> ()
    assert_eq_f         # :: ans -> f -> *args -> (_fmt=...) -> **vars -> ()
    mk_assert_eq_f      # :: (_fmt=...) -> **vars -> (ans -> f -> *args -> **kwargs -> ())
    null_str            # == ''
    null_bytes          # == b''
    null_int            # == 0
    null_tuple          # == ()
    null_frozenset      # == frozenset()
    null_mapping_view   # == MapView({})
    null_iter           # :: iter('') iter([])
    #null_sequence       # == seed.types.empty_containers.EmptySequence()
    #null_set            # == seed.types.empty_containers.EmptySet()
    #null_mapping        # == seed.types.empty_containers.EmptyMapping()

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
    with_if

    with_key            # :: (a->k) -> Iter a -> Iter (k, a)

    py_cmp              # :: Ord a => a -> a -> -> (-1|0|+1)
    int2cmp             # :: int -> (-1|0|+1)

    does_run_as_main    # :: String -> Bool
                        # does_run_as_main(__name__)
                        # does_run_as_main.alter_main_name :: String

    MapView             # mapping -> MappingProxyType
    kwargs2Attrs        # (**kwargs) -> SimpleNamespace
    is_iterable         # a -> Bool
    is_iterator         # a -> Bool
    is_reiterable       # a -> Bool
    flip                # (a->b->r) -> (b->a->r)
    neg_flip            # (a->b->r) -> (b->a->-r)
    sign_of             # RealNumber -> (-1|0|+1)

    bmk_pairs            # bmk_pairs[1:2, :]
    bmk_triples          # bmk_triples[1:2:3, ::]
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

    fmap4dict_value     # (a->b) -> dict<k,a> -> dict<k,b>
    filter4dict_value   # (v->bool) -> dict<k,v> -> dict<k,v>
    group4dict_value    # (v->g) -> dict<k,v> -> dict<g, dict<k,v> >
    dict_add__is        # dict<k,v> -> k -> v -> None
    dict_add__eq        # Eq v => dict<k,v> -> k -> v -> None

    #''')

from seed.math.sign_of import sign_of
from seed.helper.ifNone import ifNone, ifNonef
from seed.helper.Echo import echo, theEcho
from seed.helper.with_if import with_if
from seed.debug.expectError import expectError
from seed.debug.print_err import print_err, print_ferr
from seed.debug.assert_eq import assert_eq, assert_eq_f, mk_assert_eq_f
from seed.debug.lazy_raise import lazy_raise
from seed.func_tools.not_dot import __not__, not_dot
from seed.for_libs.next__tmay import next__tmay
from seed.for_libs.lookup__tmay import lookup__tmay

from types import MappingProxyType as MapView, SimpleNamespace as kwargs2Attrs
  #SimpleNamespace(**kw)

from seed.tiny_.HexReprInt import HexReprInt
from seed.tiny import HexReprInt
assert repr(HexReprInt(15)) == hex(15) == '0xf'
assert repr(HexReprInt(-15)) == hex(-15) == '-0xf'


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


from seed.tiny_.check import check_type_le, check_type_is, check_tmay, check_pair, check_uint, check_imay, icheck_type_le, icheck_type_is, icheck_tmay, icheck_pair, icheck_uint, icheck_imay
from seed.tiny_.check import check_pseudo_identifier, check_smay_pseudo_qual_name, check_pseudo_qual_name, icheck_pseudo_identifier, icheck_smay_pseudo_qual_name, icheck_pseudo_qual_name
from seed.tiny_.check import check_callable, check_is_obj, check_is_None
check_uint(1)
check_tmay(())
check_tmay((0,))
check_pair((0, 0))
check_type_is(str, '')
check_type_le(object, '')
assert 1 == icheck_uint(1)
assert (0,) == icheck_tmay((0,))
assert (0,0) == icheck_pair((0, 0))
assert '' == icheck_type_is(str, '')
assert '' == icheck_type_le(object, '')


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


from seed.tiny_.containers import null_str, null_bytes, null_int, null_tuple, null_frozenset, null_mapping_view, null_iter, mk_frozenset, mk_tuple
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



from seed.tiny_.funcs import no_op, echo_args_kwargs, echo_kwargs, echo_args, echo, fst, snd, const, lazy, lazy_raise_v, lazy_raise_f, eq, not_eq, is_, not_is, in_, not_in, flip, neg_flip, xor, xnor, with_key, mk_fprint, fprint, py_cmp, int2cmp
from seed.debug.lazy_raise import lazy_raise

#from collections.abc import Iterable, Iterator
from seed.tiny_.verify import is_iterable, is_iterator, is_reiterable

assert is_iterable(null_tuple)
assert is_reiterable(null_tuple)
assert not is_iterator(null_tuple)

assert is_iterable(null_iter)
assert not is_reiterable(null_iter)
assert is_iterator(null_iter)

assert next__tmay(null_iter) == ()
assert expectError(TypeError, lambda:next__tmay([1]))
assert expectError(TypeError, lambda:next([1]))



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

from seed.tiny_.dict__add_fmap_filter import fmap4dict_value, filter4dict_value, dict_add__is, dict_add__eq, group4dict_value




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
