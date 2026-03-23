r'''[[[
e ../../python3_src/seed/helper/lazy_import__func7context7register7data.py
name7importZqnm4mdl:
    used by:
        view ../../python3_src/seed/helper/lazy_import__func7context7register.py
            mk_context4lazy_import_registered_names_

    data from:
        view ../../python3_src/seed/tiny.py
            @20260220
]]]'''#'''

def __(s, /):
    #t = ''.join(s.split())
    s = '\n'.join(t for t in map(str.strip, s.split('\n')) if t and not t.startswith('#'))
    s = s.replace('\nfrom ', '\n;').replace(' import ', ':')
    ss = s.split(';')
    for stmt in ss:
        stmt = stmt.strip()
        #if not stmt or stmt.startswith('#'): continue
        [qnm4mdl, nms4obj] = stmt.split(':')
        ok = False
        for nm4obj in nms4obj.split(','):
            nm4obj = nm4obj.strip()
            if not nm4obj: raise Exception(stmt)
            if not nm4obj.isidentifier(): raise Exception(stmt, nm4obj)
            yield (nm4obj, qnm4mdl)
            ok = True
        if not ok: raise Exception(stmt)


name7importZqnm4mdl = dict(__(
r'''

#@20260220
from seed.debug.assert_eq import assert_eq, assert_eq_f, mk_assert_eq_f
from seed.debug.expectError import expectError
from seed.debug.lazy_raise import lazy_raise
from seed.debug.lazy_raise import lazy_raise
from seed.debug.print_err import print_err, print_ferr
from seed.debug.with_expect_error import with_expect_error
from seed.for_libs.lookup__tmay import lookup__tmay
from seed.for_libs.next__tmay import next__tmay
from seed.func_tools.not_dot import __not__, not_dot
from seed.helper.ConstantRepr import repr_as_3dot, ConstantRepr
from seed.helper.Echo import echo, theEcho
from seed.helper.ifNone import ifNone, ifNonef
from seed.helper.with_if import with_if
from seed.iters.chains import chains
from seed.iters.count_ import count_
from seed.iters.pairwise_ import pairwise_, pairwise__head_, pairwise__tail_, pairwise_chain_, pairwise_chains_
from seed.math.sign_of import sign_of
from seed.str_tools.cut_text_by_marker_seq import cut_text_by_marker_seq, strip_text_by_marker_pair
from seed.tiny import BaseTuple
from seed.tiny import HEXReprInt, HexReprInt, LowHexReprInt
from seed.tiny import catched_call__either, cached_catched_call__either, get_or_cached_catched_call__either
from seed.tiny_.BaseTuple import BaseTuple
from seed.tiny_.CallCounter import CallCounter
from seed.tiny_.Hashable import check_Hashable__shallow, is_Hashable__shallow, check_Hashable__deep, is_Hashable__deep
from seed.tiny_.HexReprInt import HEXReprInt, HexReprInt, LowHexReprInt
from seed.tiny_.HexReprInt import HEXReprInt__without_0x
from seed.tiny_.Weakable import check_Weakable, is_Weakable, WeakableDict
from seed.tiny_.at import at
from seed.tiny_.at import at
from seed.tiny_.bmk_pairs import bmk_pairs, bmk_triples, show_ordered_pairs_as_bmk_pairs, show_ordered_triples_as_bmk_triples, bmk_OrderedDict, show_ordered_pairs_as_bmk_OrderedDict, show_ordered_dict_as_bmk_OrderedDict, cased_bmk
from seed.tiny_.boolexpr_wrapper import boolexpr_wrapper
from seed.tiny_.call2bracket import call2bracket__EllipsisR__fst8func
from seed.tiny_.call2getattr import get5cls, call5cls, get5cls_, call5cls_
from seed.tiny_.catched_call__either import catched_call__either, cached_catched_call__either, get_or_cached_catched_call__either
from seed.tiny_.check import check_all_, check_tmay_, check_may_, check_not_
from seed.tiny_.check import check_bool, icheck_bool
from seed.tiny_.check import check_callable, check_iterator, check_is_obj, check_is_None
from seed.tiny_.check import check_getitemable, icheck_getitemable
from seed.tiny_.check import check_pseudo_identifier, check_smay_pseudo_qual_name, check_pseudo_qual_name, icheck_pseudo_identifier, icheck_smay_pseudo_qual_name, icheck_pseudo_qual_name
from seed.tiny_.check import check_str, check_char
from seed.tiny_.check import check_subscriptable, icheck_subscriptable
from seed.tiny_.check import check_type_in, icheck_type_in
from seed.tiny_.check import check_type_le, check_type_is, check_type_le_in, check_type_in, check_tuple__len_le, check_tuple__len_ge, check_tuple__len_eq, check_len_le, check_len_ge, check_len_eq, check_tmay, check_pair, check_either, check_uint, check_imay, icheck_type_le, icheck_type_is, icheck_tmay, icheck_pair, icheck_either, icheck_uint, icheck_imay
from seed.tiny_.check_abc import get_abstractmethod_names, check_manifest4abstractmethods
from seed.tiny_.check_path import check_path_exists_, check_path_not_exists_, check_file_path_, check_dir_path_, check_not_file_path_, check_not_dir_path_
from seed.tiny_.check_path import check_same_path_, check_not_same_path_, AreSameFileError, NotSameFileError
from seed.tiny_.class_property import class_property
from seed.tiny_.constants import inf, pos_inf, neg_inf
from seed.tiny_.containers import is_pair
from seed.tiny_.containers import mk_immutable_seq,mk_immutable_seq5iterT_,mk_immutable_seq5iter__,mk_bytes5iter_
from seed.tiny_.containers import mk_pair, mk_pair_tuple
from seed.tiny_.containers import mk_tuple__split_first_if_str, mk_tuple__split_first_if_str__sep_
from seed.tiny_.containers import null_str, null_bytes, null_int, null_tuple, null_frozenset, null_mapping_view, null_iter, mk_frozenset, mk_tuple, mk_Just, mk_Left, mk_Right
from seed.tiny_.default_cmp import default_cmp
from seed.tiny_.dict__add_fmap_filter import filter4dict_key, group4dict_key
from seed.tiny_.dict__add_fmap_filter import fmap4dict_value, filter4dict_value, dict_add__is, dict_add__eq, dict_add__new, group4dict_value
from seed.tiny_.dict__add_fmap_filter import fmap4dict_value_with_key, filter4dict_value_with_key, group4dict_value_with_key, filter4dict_item, group4dict_item
from seed.tiny_.dict_op__add import dict_add, set_add, dict_update, set_update
from seed.tiny_.echo_key import echo_key
from seed.tiny_.fmap4may import fmap4may
from seed.tiny_.funcs import no_op, echo_args_kwargs, echo_kwargs, echo_args, echo, unbox_, unbox, fst, snd, const, lazy, lazy_raise_v, lazy_raise_f, eq, not_eq, is_, not_is, in_, not_in, flip, neg_flip, xor, xnor, not_, with_key, mk_fprint, fprint, py_cmp, int2cmp, set_doc_
from seed.tiny_.get_mro import get_mro4cls, get_dict4cls, get_dict4obj, iter_cls_member_pairs_in_mro_at
from seed.tiny_.group__partition import partition_xs_by_bool_, xs_to_vss_, xs_to_k2vs_
from seed.tiny_.is_xxx import is_pair_, is_bytes_, is_bytes_like_object_
from seed.tiny_.iter_stop_with_ import iter_stop_with_, GetStopIterationValue
from seed.tiny_.map_ import map_, cmap_, call_, prepare4call_, dots_
from seed.tiny_.mk_reiterable import mk_reiterable, mk_reiterables, mk_reiterable__depth_
from seed.tiny_.nmay5tmay import nmay5star_tmay_, nmay5tmay_, nmay2tmay_
from seed.tiny_.null_dev import null_context, null_context5result_
from seed.tiny_.null_dev import null_dev
from seed.tiny_.oo8inf import oo
from seed.tiny_.singleton import __newobj__, __new4singleton__
from seed.tiny_.singleton import mk_SingletonClass, mk_existing_type_singleton
from seed.tiny_.slice2triple import slice2triple
from seed.tiny_.slice2triple import slice2triple, fix_slice_by_len, fix_slice_by_len_of
from seed.tiny_.slice2triple import slice2triple, range2triple, convert_triple_as_, range2triple_, slice2triple_
from seed.tiny_.slice2triple import slice2triple, slice2item, slices2iter_items, slices2items, slices2dict, items2dict__reject_duplicates
from seed.tiny_.slice2triple import slice2triple_, fix_slice_by_len_, fix_slice_by_len_of_
from seed.tiny_.str__split_join import str_join__list_nonemty, str_split__list_nonemty, str_join__entry_nonemty, str_split__entry_nonemty, str_join__both_list_and_entry_may_be_emty, str_split__both_list_and_entry_may_be_emty
from seed.tiny_.to_may_int_ import to_may_int_
from seed.tiny_.try_ import try_
from seed.tiny_.types5py import mk_MapView, MapView, kwargs2Attrs, curry1
from seed.tiny_.update_attr import update_attr, iupdate_attrs, set_attrs, prepare4set_attrs, fwd_call
from seed.tiny_.verify import is_callable, is_subscriptable, is_container, is_sized
from seed.tiny_.verify import is_iterable, is_iterator, is_reiterable
from seed.types.Namespace import Namespace, NamespaceSetOnce
from seed.types.Namespace import Namespace, NamespaceSetOnce, NamespaceForbidOverwriteImplicitly, NamespaceForbidNewKey, NamespaceForbidSetitem, NamespaceForbidDelitem, NamespaceForbidAlterKeySet, NamespaceForbidModify








#@20260321
from seed.int_tools.digits.uint25radix_repr import uint2radix_repr_, uint5radix_repr_
    #.u = uint5radix_repr_(radix, digits, is_big_endian=is_big_endian, **kwds)
    #.digits = uint2radix_repr_(radix, u, is_big_endian=is_big_endian, **kwds)
from seed.int_tools.digits.uint25bijective_numeration import uint5bijective_numeration_, uint2bijective_numeration_
    #.def uint2bijective_numeration_(radix, u, /, *, is_big_endian, offset4digit):
    #.def uint5bijective_numeration_(radix, offsetted_digits, /, *, is_big_endian, offset4digit):


#@20260323
from seed.tiny_.mk_fdefault import mk_default
    #.def mk_default(imay_xdefault_rank, xdefault, /, *args4xdefault):
from seed.tiny_.mk_fdefault import check4mk_default_, check4mk_default__len_
    #.def check4mk_default_(imay_xdefault_rank, xdefault, /, *args4xdefault):
    #.def check4mk_default__len_(imay_xdefault_rank, xdefault, len_args4xdefault, /):
from seed.tiny_.mk_fdefault import mk_default__easy, mk_default_or_raise
    #.def mk_default__easy(*tmay_Nothing___or___args4mk_default_or_raise, mirror=False):
    #.  (mirror_imay_xedefault_rank, xedefault, *args4xedefault) = args4mk_default = tmay_Nothing___or___args4mk_default_or_raise
    #.  [default if not mirror else exception] = tmay_Nothing = tmay_Nothing___or___args4mk_default_or_raise
    #.def mk_default_or_raise(mirror_imay_xedefault_rank, xedefault, /, *args4xedefault, mirror:bool):
    #.  imay_xdefault_ranks = (-3)-mirror_imay_xedefault_rank if mirror_imay_xedefault_rank < -1 else mirror_imay_xedefault_rank
    #.  mirrored = (mirror_imay_xedefault_rank < -1) ^ bool(mirror)
    #

'''#'''
))

from seed.helper.lazy_import__func7context7register7data import name7importZqnm4mdl
