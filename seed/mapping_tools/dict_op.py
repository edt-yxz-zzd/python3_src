
r'''
from seed.mapping_tools.dict_op import partition_by_keyss__immutable

from seed.mapping_tools.dict_op import mapping_zipped_symmetric_partition__immutable, mapping_grouped_zipped_symmetric_partition__immutable

from seed.mapping_tools.dict_op import ordered_unique_hashables, mk_Dk2v_from_Fk2v_ks__naive, mk_Dk2v_from_Fk2v_ks__ordered_unique
from seed.mapping_tools.dict_op import inv__k2v_to_v2k, inv__k2v_to_v2ks, inv__k2vs_to_v2k, inv__k2vs_to_v2ks

#'''

__all__ = '''
    discard_keys__inplace
    remove_keys__inplace
    subtract_keys__inplace

    subtract_keys__immutable
    add_dict__immutable
    subset_keys__immutable
    intersect_keys__immutable
    sum_dicts__immutable

    partition_by_keyss__immutable
    iter_partition_by_keyss__immutable

    set_symmetric_partition__immutable
    mapping_symmetric_partition__immutable
    mapping_zipped_symmetric_partition__immutable
    mapping_grouped_zipped_symmetric_partition__immutable

    ordered_unique_hashables
    mk_Dk2v_from_Fk2v_ks__naive
    mk_Dk2v_from_Fk2v_ks__ordered_unique

    inv__k2v_to_v2k
    inv__k2v_to_v2ks
    inv__k2vs_to_v2k
    inv__k2vs_to_v2ks






    inv__bijection__immutable
        inv__k2v_to_v2k
    inv__group_keys_by_value__immutable
        inv__k2v_to_v2ks

    ordered_unique_hashables
    mk_dict5key2value_keys__ordered_unique
        mk_Dk2v_from_Fk2v_ks__ordered_unique
    mk_dict5key2value_keys__naive
        mk_Dk2v_from_Fk2v_ks__naive
    '''.split()
    #mapping_symmetric_partition_ex__immutable


#from functools import reduce
#from seed.tiny_.dict__add_fmap_filter import fmap4dict_value, filter4dict_value, dict_add__is, dict_add__eq, group4dict_value
from seed.tiny_.dict__add_fmap_filter import group4dict_value
from collections import defaultdict#, Counter
import operator


def discard_keys__inplace(dict_, keys, /):
    for key in keys:
        dict_.pop(key, None) # nothrow
def remove_keys__inplace(dict_, keys, /):
    for key in keys:
        dict_.pop(key) # raise
def subtract_keys__inplace(dict_, keys, /):
    discard_keys__inplace(dict_, keys)



#################################

def subtract_keys__immutable(dict_, keys, /):
    keys = frozenset(dict_) - frozenset(keys)
    return subset_keys__immutable(dict_, keys)


def add_dict__immutable(lhs, rhs, /):
    d = dict(lhs)
    d.update(rhs)
    return d

def subset_keys__immutable(dict_, keys, /):
    'assert set(keys) <= set(dict_)'
    return {k:dict_[k] for k in frozenset(keys)}
def intersect_keys__immutable(dict_, keys, /):
    keys = frozenset(dict_) & frozenset(keys)
    return subset_keys__immutable(dict_, keys)

r'''
def sum_dicts__immutable(dicts, /):
    # bug: since update()->None not a dict
    return reduce(dict.update, dicts, {})
#'''


def sum_dicts__immutable(dicts, /):
    d = {}
    for x in dicts:
        d.update(x)
    return d

def partition_by_keyss__immutable(dict_, keyss, /):
    return list(iter_partition_by_keyss__immutable(dict_, keyss))
def iter_partition_by_keyss__immutable(dict_, keyss, /):
    s = set()
    for keys in keyss:
        d = {}
        for key in keys:
            if key in d:
                pass
            elif key in s:
                raise KeyError(f'keyss not partition: duplicate key: {key!r}')
            else:
                d[key] = dict_[key]
                s.add(key)
        yield d
    if len(s) != len(dict_):
        diff = s^set(dict_)
        raise KeyError(f'keyss not partition of the input mapping: diff={diff!r}')
    return

#symmetric_difference
def set_symmetric_partition__immutable(lhs, rhs, /):
    lhs = frozenset(lhs)
    rhs = frozenset(rhs)
    common = lhs & rhs
    lonly = lhs - common
    ronly = rhs - common
    assert common.isdisjoint(lonly)
    assert common.isdisjoint(ronly)
    assert lonly.isdisjoint(ronly)
    assert lonly|common == lhs
    assert ronly|common == rhs
    return (lonly, common, ronly)


def mapping_symmetric_partition__immutable(lhs, rhs, /):
    (lonly, common, ronly) = set_symmetric_partition__immutable(lhs, rhs)
    lonly_dict, lcommon_dict = partition_by_keyss__immutable(lhs, [lonly, common])
    ronly_dict, rcommon_dict = partition_by_keyss__immutable(rhs, [ronly, common])
    assert lcommon_dict.keys() == rcommon_dict.keys() == common
    assert lonly_dict.keys() == lonly
    assert ronly_dict.keys() == ronly
    return (lonly_dict, lcommon_dict, rcommon_dict, ronly_dict)


def mapping_zipped_symmetric_partition__immutable(lhs, rhs, /):
    (lonly_dict, lcommon_dict, rcommon_dict, ronly_dict) = mapping_symmetric_partition__immutable(lhs, rhs)
    zipped_common_dict = {
        k: (lvalue, rcommon_dict[k])
        for k, lvalue in lcommon_dict.items()
        }
    return (lonly_dict, zipped_common_dict, ronly_dict)


def mapping_grouped_zipped_symmetric_partition__immutable(may_zipped_pair_grouper, lhs, rhs, /):
    if may_zipped_pair_grouper is None:
        zipped_pair_grouper = operator.__eq__
    else:
        zipped_pair_grouper = may_zipped_pair_grouper

    (lonly_dict, zipped_common_dict, ronly_dict) = mapping_zipped_symmetric_partition__immutable(lhs, rhs)
    def f(pair, /):
        (lvalue, rvalue) = pair
        return zipped_pair_grouper(lvalue, rvalue)
    grouped_zipped_common_dict = group4dict_value(f, zipped_common_dict)
    return (lonly_dict, grouped_zipped_common_dict, ronly_dict)


if 0:
    def mapping_symmetric_partition_ex__immutable(lhs, rhs, /, *, diff_value__tmay):
        'diff_value__tmay :: value -> value -> tmay diff_result'


#################################
def inv__bijection__immutable(k2v, /):
    v2k = {v:k for k,v in k2v.items()}
    if not len(v2k) == len(k2v): raise TypeError('not bijection mapping')
    return v2k

def inv__group_keys_by_value__immutable(k2v, /):
    'see also: seed.tiny_.dict__add_fmap_filter.group4dict_value'
    v2ks = defaultdict(set)
    for k, v in k2v.items():
        v2ks[v].add(k)
    v2ks = {**v2ks}
    return v2ks
inv__k2v_to_v2ks = inv__group_keys_by_value__immutable
inv__k2v_to_v2k = inv__bijection__immutable
def inv__k2vs_to_v2ks(k2vs, /):
    v2ks = defaultdict(set)
    for k, vs in k2vs.items():
        for v in vs:
            v2ks[v].add(k)
    v2ks = {**v2ks}
    return v2ks
def inv__k2vs_to_v2k(k2vs, /):
    v2k = {}
    for k, vs in k2vs.items():
        for v in vs:
            if 0:
                if v in v2k: raise ValueError(f'value duplicate: {v!r}')
                v2k[v] = k
            else:
                if not v2k.setdefault(v, k) is k:raise ValueError(f'value duplicate: {v!r} on diff keys: ({k!r}, {v2k[v]})')
    return v2k

#################################
def ordered_unique_hashables(ks, /):
    'Iter k -> ([k], {k})'
    ls = []
    s = set()
    for k in ks:
        if k not in s:
            s.add(k)
            ls.append(k)
    return ls, s
def mk_dict5key2value_keys__naive(key2value__callable, keys, /):
    return {k:key2value__callable(k) for k in keys}
def mk_dict5key2value_keys__ordered_unique(key2value__callable, keys, /):
    keys = iter(keys)
    ls, s = ordered_unique_hashables(keys)
    k2v = mk_dict5key2value_keys__naive(key2value__callable, ls)
    return k2v


mk_Dk2v_from_Fk2v_ks__ordered_unique = mk_dict5key2value_keys__ordered_unique
mk_Dk2v_from_Fk2v_ks__naive = mk_dict5key2value_keys__naive
