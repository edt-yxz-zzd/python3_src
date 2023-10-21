#__all__:goto
r'''
py -m nn_ns.app.debug_cmd   seed.mapping_tools.dict_op -x
py -m nn_ns.app.doctest_cmd seed.mapping_tools.dict_op:f -v
py -m nn_ns.app.doctest_cmd seed.mapping_tools.dict_op:__doc__ -ff -v
py_adhoc_call   seed.mapping_tools.dict_op   @f




from seed.mapping_tools.dict_op import partition_by_keyss__immutable

from seed.mapping_tools.dict_op import mapping_zipped_symmetric_partition__immutable, mapping_grouped_zipped_symmetric_partition__immutable

from seed.mapping_tools.dict_op import ordered_unique_hashables, mk_Dk2v_from_Fk2v_ks__naive, mk_Dk2v_from_Fk2v_ks__ordered_unique
from seed.mapping_tools.dict_op import inv__k2v_to_v2k, inv__k2v_to_v2ks, inv__k2vs_to_v2k, inv__k2vs_to_v2ks

from seed.mapping_tools.dict_op import mapping_symmetric_diff4patch__immutable, mapping_symmetric_patch4lhs__immutable, mapping_symmetric_patch4rhs__immutable, mapping_symmetric_diff_patch_default_setting

from seed.mapping_tools.dict_op import mapping_symmetric_diff4patch__immutable__default, mapping_symmetric_patch4lhs__immutable__default, mapping_symmetric_patch4rhs__immutable__default

#'''

__all__ = '''
    discard_keys__inplace
    remove_keys__inplace
    subtract_keys__inplace

    add_dict__immutable
        sum_dicts__immutable
    subset_keys__immutable
        subtract_keys__immutable
        intersect_keys__immutable

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





    discard_keys__inplace
    remove_keys__inplace
    subtract_keys__inplace
    add_dict__immutable
    sum_dicts__immutable
    subset_keys__immutable
    subtract_keys__immutable
    intersect_keys__immutable
    partition_by_keyss__immutable
    iter_partition_by_keyss__immutable
    set_symmetric_partition__immutable
    mapping_symmetric_partition__immutable
    mapping_zipped_symmetric_partition__immutable
    mapping_grouped_zipped_symmetric_partition__immutable

    mapping_symmetric_diff_patch_default_setting
    mapping_symmetric_diff4patch__immutable
    mapping_symmetric_patch4lhs__immutable
    mapping_symmetric_patch4rhs__immutable

    mapping_symmetric_diff4patch__immutable__default
    mapping_symmetric_patch4lhs__immutable__default
    mapping_symmetric_patch4rhs__immutable__default

    inv__bijection__immutable
    inv__group_keys_by_value__immutable
    inv__k2v_to_v2ks
    inv__k2v_to_v2k
    inv__k2vs_to_v2ks
    inv__k2vs_to_v2k
    ordered_unique_hashables
    mk_dict5key2value_keys__naive
    mk_dict5key2value_keys__ordered_unique
    mk_Dk2v_from_Fk2v_ks__ordered_unique
    mk_Dk2v_from_Fk2v_ks__naive
    '''.split()
    #mapping_symmetric_partition_ex__immutable
__all__


#from functools import reduce
#from seed.tiny_.dict__add_fmap_filter import fmap4dict_value, filter4dict_value, dict_add__is, dict_add__eq, group4dict_value
from seed.tiny_.dict__add_fmap_filter import group4dict_value
from seed.tiny_.containers import mk_frozenset
from seed.tiny_.check import check_tmay, check_callable, check_int_ge_lt#check_uint_lt, , check_int_ge, check_int_ge_le

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
def add_dict__immutable(lhs, rhs, /):
    d = dict(lhs)
    d.update(rhs)
    return d
r'''
def sum_dicts__immutable(dicts, /):
    # bug: since update()->None not a dict
    return reduce(dict.update, dicts, {})
'''#'''
def sum_dicts__immutable(dicts, /):
    d = {}
    for x in dicts:
        d.update(x)
    return d


def subset_keys__immutable(dict_, keys, /):
    'Map (a|c) v -> Iter c -> Map a v  #assert set(keys) <= set(dict_)'
    return {k:dict_[k] for k in mk_frozenset(keys)}
def subtract_keys__immutable(dict_, keys, /):
    'Map (a|c) v -> Iter (b|c) -> Map a v'
    keys = mk_frozenset(dict_) - mk_frozenset(keys)
    return subset_keys__immutable(dict_, keys)
def intersect_keys__immutable(dict_, keys, /):
    'Map (a|c) v -> Iter (b|c) -> Map c v'
    keys = frozenset(dict_) & mk_frozenset(keys)
    return subset_keys__immutable(dict_, keys)


def partition_by_keyss__immutable(dict_, keyss, /):
    'Map k v -> Iter<[k]> -> [Map k v]'
    return list(iter_partition_by_keyss__immutable(dict_, keyss))
def iter_partition_by_keyss__immutable(dict_, keyss, /):
    'Map k v -> Iter<[k]> -> Iter<Map k v>'
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
    'Set (a|c) -> Set (b|c) -> (Set a, Set c, Set b)'
    lhs = mk_frozenset(lhs)
    rhs = mk_frozenset(rhs)
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
    'Map (a|c) u -> Map (b|c) v -> (Map a u, Map c u, Map c v, Map b v)'
    (lonly, common, ronly) = set_symmetric_partition__immutable(lhs, rhs)
    lonly_dict, lcommon_dict = partition_by_keyss__immutable(lhs, [lonly, common])
    ronly_dict, rcommon_dict = partition_by_keyss__immutable(rhs, [ronly, common])
    assert lcommon_dict.keys() == rcommon_dict.keys() == common
    assert lonly_dict.keys() == lonly
    assert ronly_dict.keys() == ronly
    return (lonly_dict, lcommon_dict, rcommon_dict, ronly_dict)


def mapping_zipped_symmetric_partition__immutable(lhs, rhs, /):
    'Map (a|c) u -> Map (b|c) v -> (Map a u, Map c (u,v), Map b v)'
    (lonly_dict, lcommon_dict, rcommon_dict, ronly_dict) = mapping_symmetric_partition__immutable(lhs, rhs)
    zipped_common_dict = {
        k: (lvalue, rcommon_dict[k])
        for k, lvalue in lcommon_dict.items()
        }
    return (lonly_dict, zipped_common_dict, ronly_dict)


def mapping_grouped_zipped_symmetric_partition__immutable(may_zipped_pair_grouper, lhs, rhs, /):
    'may (u->v->w) -> Map (a|c) u -> Map (b|c) v -> (Map a u, Map w (Map c (u,v)), Map b v)'
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
#################################
class mapping_symmetric_diff_patch_default_setting:
    r'''
    patch_/patcher
    diff_
    delta/result/patch
    #'''
    @staticmethod
    def diff4value_(u,v,/):
        w = (u,v)
        tmay_w = (w,) if not u in [v] else ()
        return tmay_w
    @staticmethod
    def patch4value4lhs_(w,u,/):
        (_u,v) = w
        return v
    @staticmethod
    def patch4value4rhs_(w,v,/):
        (u,_v) = w
        return u
mapping_symmetric_diff_patch_default_setting = mapping_symmetric_diff_patch_default_setting()

def mapping_symmetric_diff4patch__immutable__default(lhs, rhs, /, *, validate=False):
    'Eq u v => Map (a|c) u -> Map (b|c) v -> Map (a|c|b) ((2,u)|(3,(u,v))|(1,v))'
    #bug:patch = mapping_symmetric_diff4patch__immutable(None, None, None, rhs, lhs, validate=validate)
    patch = mapping_symmetric_diff4patch__immutable(None, None, None, lhs, rhs, validate=validate)
    return patch
def mapping_symmetric_diff4patch__immutable(may_patch4value4lhs_, may_patch4value4rhs_, may_diff4value_, lhs, rhs, /, *, validate=False):
    'may (w->u->v) -> may (w->v->u) -> _may_ (u->v->tmay w) -> Map (a|c) u -> Map (b|c) v -> Map (a|c|b) ((2,u)|(3,w)|(1,v)) #for recursive diff&patch, [validate=True] should not set recursive for all'

    if may_diff4value_ is None and not (may_patch4value4lhs_ is None is may_patch4value4rhs_):raise TypeError
    if may_diff4value_ is None:
        assert (may_patch4value4lhs_ is None is may_patch4value4rhs_)
        _ = mapping_symmetric_diff_patch_default_setting
        diff4value_ = mapping_symmetric_diff_patch_default_setting.diff4value_
        may_patch4value4lhs_ = mapping_symmetric_diff_patch_default_setting.patch4value4lhs_
        may_patch4value4rhs_ = mapping_symmetric_diff_patch_default_setting.patch4value4rhs_
    else:
        diff4value_ = may_diff4value_
    diff4value_

    if not may_patch4value4lhs_ is None:
        patch4value4lhs_ = may_patch4value4lhs_
        check_callable(patch4value4lhs_)
        def _check4lhs(u,v,w,/):
            _v = patch4value4lhs_(w,u)
            if not v==_v: raise ValueError(('lhs->rhs', c, w, u, v, _v))
    else:
        def _check4lhs(u,v,w,/):
            pass

    if not may_patch4value4rhs_ is None:
        patch4value4rhs_ = may_patch4value4rhs_
        check_callable(patch4value4rhs_)
        def _check4rhs(u,v,w,/):
            _u = patch4value4rhs_(w,v)
            if not u==_u: raise ValueError(('rhs->lhs', c, w, u, v, _u))
    else:
        def _check4rhs(u,v,w,/):
            pass

    def _check(u,v,w,/):
        _check4lhs(u,v,w)
        _check4rhs(u,v,w)

    (lonly_dict, zipped_common_dict, ronly_dict) = mapping_zipped_symmetric_partition__immutable(lhs, rhs)
    patch = {}
    for c,(u,v) in zipped_common_dict.items():
        tmay_w = diff4value_(u,v)
        check_tmay(tmay_w)
        if not tmay_w:continue
        [w] = tmay_w
        _check(u,v,w)
        patch[c] = (3,w)
    for a,u in lonly_dict.items():
        patch[a] = (2,u)
    for b,v in ronly_dict.items():
        patch[b] = (1,v)
    if validate:
        if not may_patch4value4lhs_ is None:
            rhs_ = mapping_symmetric_patch4lhs__immutable(diff4value_, patch4value4lhs_, patch, lhs)
            assert rhs_ == rhs, (rhs_, rhs)
        if not may_patch4value4rhs_ is None:
            lhs_ = mapping_symmetric_patch4rhs__immutable(diff4value_, patch4value4rhs_, patch, rhs)
            assert lhs_ == lhs, (lhs_, lhs)
    return patch



def mapping_symmetric_patch4lhs__immutable__default(patch, lhs, /, *, validate=False):
    'Map (a|c|b) ((2,u)|(3,(u,v))|(1,v)) -> Map (a|c) u -> Map (b|c) v'
    rhs = mapping_symmetric_patch4lhs__immutable(None, None, patch, lhs, validate=validate)
    return rhs
def mapping_symmetric_patch4rhs__immutable__default(patch, rhs, /, *, validate=False):
    'Map (a|c|b) ((2,u)|(3,(u,v))|(1,v)) -> Map (b|c) v -> Map (a|c) u'
    lhs = mapping_symmetric_patch4rhs__immutable(None, None, patch, rhs, validate=validate)
    return lhs

def mapping_symmetric_patch4lhs__immutable(may_diff4value_, may_patch4value4lhs_, patch, lhs, /, *, validate=False):
    'may (u->v->tmay w) -> _may_ (w->u->v) -> Map (a|c|b) ((2,u)|(3,w)|(1,v)) -> Map (a|c) u -> Map (b|c) v'
    rhs = _mapping_symmetric_patch4asif_lhs__immutable(False, may_diff4value_, may_patch4value4lhs_, patch, lhs, validate=validate)
    return rhs
def mapping_symmetric_patch4rhs__immutable(may_diff4value_, may_patch4value4rhs_, patch, rhs, /, *, validate=False):
    'may (u->v->tmay w) -> _may_ (w->u->v) -> Map (a|c|b) ((2,u)|(3,w)|(1,v)) -> Map (b|c) v -> Map (a|c) u'
    lhs = _mapping_symmetric_patch4asif_lhs__immutable(True, may_diff4value_, may_patch4value4rhs_, patch, rhs, validate=validate)
    return lhs
def _mapping_symmetric_patch4asif_lhs__immutable(_4rhs, may_diff4value_, may_patch4value4lhs_, patch, lhs, /, *, validate):
    if may_patch4value4lhs_ is None is not may_diff4value_:raise TypeError
    if may_patch4value4lhs_ is None:
        assert may_diff4value_ is None
        _ = mapping_symmetric_diff_patch_default_setting
        may_diff4value_ = mapping_symmetric_diff_patch_default_setting.diff4value_
        if _4rhs:
            # .*4rhs
            may_patch4value4lhs_ = mapping_symmetric_diff_patch_default_setting.patch4value4rhs_
        else:
            # .*4lhs
            may_patch4value4lhs_ = mapping_symmetric_diff_patch_default_setting.patch4value4lhs_
    assert not may_patch4value4lhs_ is None
    patch4value4lhs_ = may_patch4value4lhs_
    del may_patch4value4lhs_
    check_callable(patch4value4lhs_)

    if not may_diff4value_ is None:
        diff4value_ = may_diff4value_
        check_callable(diff4value_)
        def _check(u,v,w,/):
            tmay_w = diff4value_(u,v)
            if not (w,)==tmay_w: raise ValueError(('->patch', k, case, w, u, v, tmay_w))
    else:
        def _check(u,v,w,/):
            pass

    _1,_2 = (1,2)
    if _4rhs:
        _1,_2 = (_2,_1)
        _check_ = _check
        def _check(u,v,w,/):
            v,u = u,v
            _check_(u,v,w)
    rhs = {**lhs}
    for k,(case, x) in patch.items():
        check_int_ge_lt(1, 4, case)
        if case == _1:
            if k in lhs: raise KeyError(k)
            v = x
            rhs[k] = v
            continue

        if k not in lhs: raise KeyError(k)
        u = lhs[k]
        if case == _2:
            if not u==x: raise ValueError((k, case, x, u))
            del rhs[k]
        elif case == 3:
            w = x
            v = patch4value4lhs_(w,u)
            _check(u,v,w)
            rhs[k] = v
        else:
            raise ValueError('not a valid patch: not case in [1,2,3]')
    rhs
    if validate:
        if not may_diff4value_ is None:
            if _4rhs:
                _patch = mapping_symmetric_diff4patch__immutable(None, patch4value4lhs_, diff4value_, rhs, lhs, validate=True)
            else:
                _patch = mapping_symmetric_diff4patch__immutable(patch4value4lhs_, None, diff4value_, lhs, rhs, validate=True)
            assert _patch == patch, (_patch, patch)
    return rhs
def _():
    lhs = {7:111,5:333,4:444}
    rhs = {8:222,5:999,4:444}
    patch__substract = {7:(2,111),8:(1,222),5:(3, 666)}
    patch__default = {7:(2,111),8:(1,222),5:(3, (333,999))}
    setting__default = mapping_symmetric_diff_patch_default_setting
    class setting__substract:
        def diff4value_(u,v,/):
            w = v-u
            tmay_w = (w,) if w else ()
            return tmay_w
        def patch4value4lhs_(w,u,/):
            v = u+w
            return v
        def patch4value4rhs_(w,v,/):
            u = v-w
            return u
    _2(lhs, rhs, patch__default, setting__default)
    _2(lhs, rhs, patch__substract, setting__substract)
def _2(lhs, rhs, patch, setting, /):
    patch4value4lhs_ = setting.patch4value4lhs_
    patch4value4rhs_ = setting.patch4value4rhs_
    diff4value_ = setting.diff4value_

    _patch = mapping_symmetric_diff4patch__immutable(patch4value4lhs_, patch4value4rhs_, diff4value_, lhs, rhs, validate=True)
    assert _patch == patch, (_patch, patch)
    rhs_ = mapping_symmetric_patch4lhs__immutable(diff4value_, patch4value4lhs_, patch, lhs, validate=True)
    assert rhs_ == rhs, (rhs_, rhs)
    lhs_ = mapping_symmetric_patch4rhs__immutable(diff4value_, patch4value4rhs_, patch, rhs, validate=True)
    assert lhs_ == lhs, (lhs_, lhs)
    return
_()











#################################
#################################
def inv__bijection__immutable(k2v, /):
    'Map k v -> Map v k'
    v2k = {v:k for k,v in k2v.items()}
    if not len(v2k) == len(k2v): raise TypeError('not bijection mapping')
    return v2k

def inv__group_keys_by_value__immutable(k2v, ks=None, /, *, set_vs_list=False):
    'Map k v -> Map v (Set k) #see also: seed.tiny_.dict__add_fmap_filter.group4dict_value'
    if set_vs_list:
        T = list
        add = T.append
    else:
        T = set
        add = T.add
    T, add
    v2ks = defaultdict(T)

    if ks is True:
        ks = range(len(k2v))

    if ks is None:
        kv_pairs = k2v.items()
    else:
        kv_pairs = ((k, k2v[k]) for k in ks)

    for k, v in kv_pairs:
        add(v2ks[v], k)
    v2ks = {**v2ks}
    return v2ks
inv__k2v_to_v2ks = inv__group_keys_by_value__immutable
inv__k2v_to_v2k = inv__bijection__immutable

def check4inv__k2vs(k2vs, /, *, keys_disappear_ok:bool):
    if not keys_disappear_ok:
        if keys_disappear := {k for k,vs in k2vs.items() if not vs}: raise ValueError(f'keys_disappear:{keys_disappear}')

def inv__k2vs_to_v2ks(k2vs, /, *, keys_disappear_ok=False):
    'Map k [v] -> Map v (Set k)'
    check4inv__k2vs(k2vs, keys_disappear_ok=keys_disappear_ok)
    v2ks = defaultdict(set)
    for k, vs in k2vs.items():
        for v in vs:
            v2ks[v].add(k)
    v2ks = {**v2ks}
    return v2ks
def inv__k2vs_to_v2k(k2vs, /, *, keys_disappear_ok=False):
    'Map k [v] -> Map v k'
    check4inv__k2vs(k2vs, keys_disappear_ok=keys_disappear_ok)

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
    '(k->v) -> Iter k -> Map k v'
    return {k:key2value__callable(k) for k in keys}
def mk_dict5key2value_keys__ordered_unique(key2value__callable, keys, /):
    '(k->v) -> Iter k -> Map k v'
    keys = iter(keys)
    ls, s = ordered_unique_hashables(keys)
    k2v = mk_dict5key2value_keys__naive(key2value__callable, ls)
    return k2v


mk_Dk2v_from_Fk2v_ks__ordered_unique = mk_dict5key2value_keys__ordered_unique
mk_Dk2v_from_Fk2v_ks__naive = mk_dict5key2value_keys__naive
