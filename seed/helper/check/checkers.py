#HHHHH
r'''
e ../../python3_src/seed/helper/check/checkers.py
debug_pym seed.helper.check.checkers
py -m seed.helper.check.checkers
from seed.helper.check.checkers import checks, checkers, check_funcs

why?
    to break long name
    check_pair ==>> check_funcs.pair
    checker4callable ==>> checkers.callable


check_finite_float(x) #math.isfinite
check_finite_complex(x) #cmath.isfinite



identifier
pseudo_identifier
module
qual_name
check_identifier <: check_module <: check_str
check_identifier <: check_pseudo_identifier <: check_str

#'''



___begin_mark_of_excluded_global_names__0___ = ...
from seed.tiny import str2__all__
__all__ = str2__all__(r'''#)
    checkers
    check_funcs
        checks
    check_ # verify *args **kwargs




# import from seed.helper.check.check
    check_Lookupable
    check_namedtuple_type
    check_has_attrs
    check_callable
    check_subclass
    check_instance
    check_instance_all
    check_type_is
    check_tuple
    check_len_eq
    check_int
    check_iterable
    check_type_tree





#float
    checker4float
    checker4complex
    checker4finite_float
    checker4finite_complex

# helper for checker4qual_name
    #is_py_keyword
    #split_by_dot

# impl checker4qual_name
    checker4str
    raw_checker4pseudo_identifier
    checker4pseudo_identifier
    raw_checker4py_keyword
    checker4identifier
    raw_checker4identifier
    checker4identifiers
    raw_checker4identifiers
    checker4qual_name



# required by seed.helper.repr.repr_api
    check_ # verify *args **kwargs
    check_int_ge_neg1
        check_uint_imay
    check_finite_float
    check_finite_complex
    check_float
    check_complex
    check_str
    check_bytes
    check_bool
    check_uint
    check_instance_or_None
    check_mapping
    check_iterator
    check_reiterable
    check_pairs_of
        # Iterable not tuple
    check_sorted
    check_all
    check_pair



# later add:
    checker4tribool
    #
    check_tmay
    check_nmay
    check_is_obj_or
    check_obj_is
    #
    check_strict_sorted
    check_int_ge1
    check_int_ge2
    #
    check_seq
    check_len_of
    #
    check_union_of_cased_tuples
    check_cased_tuple
    check_cased_tuple__free
    #check_cased_tuple__free_ex
    check_empty
    check_nonempty
    check_nonempty_str
    check_FrozenDict_as_record__free
    check_FrozenDict_as_record
    check_FrozenDict_as_cased_record__free
    check_FrozenDict_as_cased_record
    check_FrozenDict_as_union_of_cased_records

    check_mapping_as_record__free
    check_mapping_as_record
    check_mapping_as_cased_record__free
    check_mapping_as_cased_record
    check_mapping_as_union_of_cased_records

    check_is_None
    check_result_of_cmp
    check_result_of_partial_cmp__int
    check_result_of_partial_cmp__tmay
    check_icmp
    check_ipcmp
    check_tpcmp


# main output
    check_funcs
    checks
    checkers
$
$
    #(''')


#HHHHH

import math, cmath
import keyword#iskeyword

from collections.abc import Mapping, Set, Sequence
from collections.abc import Container, Iterable
from seed.tiny import is_iterator, is_reiterable, fst, snd
from seed.iters.is_sorted import is_sorted, is_strict_sorted
from seed.types.FrozenDict import FrozenDict


if 0:
    from seed.helper.check.check import IChecker, mk_checker, check, verify, CheckFail, CheckError, CheckException
    from seed.helper.check.check import mk_checker__point, mk_checker__pair

    from seed.helper.check.check import check, verify, check_then_calc, verify_then_may_calc
    from seed.helper.check.check import mk_checker, mk_impl_class_checker, mk_checker__point, mk_checker__pair, mk_checker__array, mk_checker__pairs
    from seed.helper.check.check import IChecker, CheckFail, CheckError, CheckException
    from seed.helper.check.check import the_checker__is_None, the_fail_checker, the_pass_checker, the_hashable_checker, checker4callable
    from seed.helper.check.check import Checker__uint_mod, Checker__int_between, Checker__tuple_maybe, Checker__none_maybe


#####################################
#from nn_ns.filedir.relative_path_ops import relative_path_ops, check_relative_path, is_relative_path_empty, relative_path2parts
    #for check_relative_path & empty
    #but seed shouldnot import nn_ns

from seed.types.TriBoolOps import TriBoolOps#is_tribool



___end_mark_of_excluded_global_names__0___ = ...

#####################################
#####################################
#####################################
from seed.helper.check.check import Checker__type_is, Checker__verify_func, mk_checker__array


#####################################
#last import for print_global_names()
from seed.helper.check.check import (
    check_Lookupable
    ,check_namedtuple_type
    ,check_has_attrs
    ,check_callable
    ,check_subclass
    ,check_instance
    ,check_instance_all
    ,check_type_is
    ,check_tuple
    ,check_len_eq
    ,check_int
    ,check_iterable
    ,check_type_tree
    )

#HHHHH



def is_py_keyword(x):
    return keyword.iskeyword(x) or x == '__debug__'


checker4float = Checker__type_is(float)
checker4complex = Checker__type_is(complex)

checker4finite_float = checker4float & Checker__verify_func(math.isfinite)
checker4finite_complex = checker4complex & Checker__verify_func(cmath.isfinite)

checker4str = Checker__type_is(str)
raw_checker4pseudo_identifier = Checker__verify_func(str.isidentifier)
checker4pseudo_identifier = checker4str & raw_checker4pseudo_identifier

raw_checker4py_keyword = Checker__verify_func(is_py_keyword)
checker4identifier = checker4pseudo_identifier - raw_checker4py_keyword
raw_checker4identifier = raw_checker4pseudo_identifier - raw_checker4py_keyword

#def is_qual_name(s):
def split_by_dot(s):
    return (*s.split('.'),)

checker4identifiers = mk_checker__array(checker4identifier)
raw_checker4identifiers = mk_checker__array(raw_checker4identifier)
assert raw_checker4identifier['af']
assert raw_checker4identifiers['af',]
assert raw_checker4identifiers[()]

checker4qual_name = -(((checker4str>>split_by_dot)@bool) / raw_checker4identifiers)
assert not checker4qual_name['']
assert not checker4qual_name[1]
assert not checker4qual_name['__debug__']
assert not checker4qual_name['a.def']
assert checker4qual_name['af']
assert checker4qual_name['a.f']


#########################################
#########################################
checker4tribool = Checker__verify_func(TriBoolOps.is_tribool)


#HHHHH
#########################################
#########################################
#########################################
def check_(verify, /, *args, **kwargs):
    if not verify(*args, **kwargs):
        raise CheckFail(args, kwargs)
    return
def check_int_ge_neg1(imay):
    r'''imay <- [-1..]; tmay :: ()/(x,); nmay :: None/x'
    'see: check_uint_imay/check_tmay/check_nmay/check_is_obj_or/check_instance_or_None'
    #'''
    check_int(imay, min=-1)
check_uint_imay = check_int_ge_neg1

def check_finite_float(x):
    check_float(x)
    check_(math.isfinite, x)
def check_finite_complex(x):
    check_complex(x)
    check_(cmath.isfinite, x)
def check_float(x):
    check_type_is(float, x)
def check_complex(x):
    check_type_is(complex, x)
def check_str(x):
    check_type_is(str, x)
def check_str(x):
    check_type_is(str, x)
def check_str(x):
    check_type_is(str, x)
def check_bytes(x):
    check_type_is(bytes, x)
def check_bool(x):
    check_type_is(bool, x)
def check_uint(i):
    check_int(i, min=0)
def check_instance_or_None(cls, obj):
    'see: check_uint_imay/check_tmay/check_nmay/check_is_obj_or/check_instance_or_None'
    if obj is not None:
        check_instance(cls, obj)

def check_mapping(obj):
    check_instance(Mapping, obj)
def check_iterator(x):
    check_(is_iterator, x)
def check_reiterable(x):
    check_(is_reiterable, x)
def check_pairs_of(A, B, reiterable):
    'maynot array as whole; need extra check_tuple()'
    check_reiterable(reiterable)
    check_all(check_pair, reiterable)
    check_instance_all(A, map(fst, reiterable))
    check_instance_all(B, map(snd, reiterable))
def check_sorted(x):
    check_(is_sorted, x)

def check_all(check_func, xs):
    for x in xs:
        check_func(x)
def check_pair(x):
    check_tuple(x, sz=2)
#########################################
check_uint_imay
def check_tmay(x, *, cls=None, check_func=None):
    'see: check_uint_imay/check_tmay/check_nmay/check_is_obj_or/check_instance_or_None'
    check_tuple(x)
    tpl = x
    check_int(len(tpl), max=1)
    if tpl:
        if cls is not None:
            check_instance_all(cls, tpl)
        if check_func is not None:
            check_all(check_func, tpl)

def check_nmay(check_func, x, /,*, cls=None):
    'see: check_uint_imay/check_tmay/check_nmay/check_is_obj_or/check_instance_or_None'
    check_is_obj_or(None, check_func, x, cls=cls)
def check_is_obj_or(obj, check_func, x, /,*, cls=None):
    'see: check_uint_imay/check_tmay/check_nmay/check_is_obj_or/check_instance_or_None'
    if x is not obj:
        if cls is not None:
            check_instance(cls, x)
        if check_func is not None:
            check_func(x)
        if cls is None is check_func:
            raise CheckFail
def check_obj_is(obj, x, /):
    if x is not obj: raise CheckFail


#########################################
check_sorted
def check_strict_sorted(x):
    check_(is_strict_sorted, x)

check_uint_imay
check_int_ge_neg1
def check_int_ge1(x):
    check_int(x, min=1)
def check_int_ge2(x):
    check_int(x, min=2)

#########################################
def check_seq(obj):
    check_instance(Sequence, obj)
def check_len_of(container, /,*, sz=None, min=None, max=None, cls=None, base=None):
    u = len(container)
    if sz is not None:
        check_int(u, min=sz, max=sz)
    check_int(u, min=min, max=max)
    if cls is not None:
        check_type_is(cls, container)
    if base is not None:
        check_instance(base, container)
#########################################

def check_union_of_cased_tuples(case_name2may_sz, obj, /):
    check_cased_tuple__free(obj)
    cased_tuple = obj
    case_name = cased_tuple[0]
    if not case_name in case_name2may_sz: raise TypeError
    may_sz = case_name2may_sz[case_name]
    check_cased_tuple(case_name, may_sz, obj)

def check_cased_tuple(may_case_name, may_sz, obj, /):
    check_cased_tuple__free(obj)
    cased_tuple = obj
    if may_case_name is not None:
        expected_case_name = may_case_name
        case_name = cased_tuple[0]
        if case_name != expected_case_name: raise TypeError

    if may_sz is not None:
        expected_sz = may_sz
        if len(cased_tuple) != expected_sz: raise TypeError

def check_cased_tuple__free(obj, /):
    check_tuple(obj)
    check_nonempty(obj)
    tpl1s = obj
    ps_case_name = tpl1s[0]
    check_nonempty_str(ps_case_name)
r'''
def check_cased_tuple__free_ex(obj, /,*, case_name=None, sz=None, min=None, max=None, case_names=None, case_name2sz=None):
    check_cased_tuple(case_name, sz, obj)
    cased_tuple = obj
    check_len_of(cased_tuple, sz=sz, min=min, max=max)
    case_name = cased_tuple(0]
    if case_names is not None:
        if not case_name in case_names: raise TypeError
    if case_name2sz is not None:
        if not case_name in case_name2sz: raise TypeError
        sz = case_name2sz[case_name]
        if len(cased_tuple) != sz: raise TypeError
#'''

def check_empty(container, /):
    if len(container): raise TypeError
def check_nonempty(container, /):
    if not len(container): raise TypeError
def check_nonempty_str(x, /):
    check_str(x)
    #if '' == x: raise TypeError
    check_nonempty(x)


def check_mapping_as_record__free(x, /,*, empty_str_key_ok:bool, cls=None):
    if cls is not None:
        check_type_is(cls, x)
    check_mapping(x)
    check_all(check_str if empty_str_key_ok else check_nonempty_str, iter(x))

def check_mapping_as_record(may_field_name_set, x, /,*, empty_str_key_ok:bool=False, cls=None):
    check_mapping_as_record__free(x, empty_str_key_ok=empty_str_key_ok, cls=cls)
    record = x
    _tail_of__check_mapping_as_record(may_field_name_set, record)
def _tail_of__check_mapping_as_record(may_field_name_set, record, /):
    if may_field_name_set is not None:
        field_name_set = may_field_name_set
        if not len(record) == len(field_name_set): raise TypeError
        if not set(record) == field_name_set: raise TypeError
def check_mapping_as_cased_record__free(field_name4case_name, x, /,*, cls=None):
    check_mapping_as_cased_record(field_name4case_name, None, None, x, cls=cls)
def check_mapping_as_cased_record(field_name4case_name, may_case_name, may_field_name_set, x, /,*, cls=None):
    check_mapping_as_record(may_field_name_set, x, empty_str_key_ok=(not field_name4case_name), cls=cls)
    if not field_name4case_name in x: raise TypeError
    ps_case_name = x[field_name4case_name]
    check_nonempty_str(ps_case_name)
    case_name = ps_case_name

    if may_case_name is not None:
        expected_case_name = may_case_name
        if case_name != expected_case_name: raise TypeError
def check_mapping_as_union_of_cased_records(field_name4case_name, case_name2may_field_name_set, x, /,*, cls=None):
    check_mapping_as_cased_record__free(field_name4case_name, x, cls=cls)
    cased_record = x
    case_name = cased_record[field_name4case_name]
    if not case_name in case_name2may_field_name_set: raise TypeError
    may_field_name_set = case_name2may_field_name_set[case_name]
    #_tail_of__check_mapping_as_record(may_field_name_set, cased_record)
    check_mapping_as_cased_record(field_name4case_name, case_name, may_field_name_set, x, cls=cls)


def check_FrozenDict_as_record__free(x, /,*, empty_str_key_ok:bool):
    check_mapping_as_record__free(x, empty_str_key_ok=empty_str_key_ok, cls=FrozenDict)
def check_FrozenDict_as_record(may_field_name_set, x, /,*, empty_str_key_ok:bool=False):
    check_mapping_as_record(may_field_name_set, x, empty_str_key_ok=empty_str_key_ok, cls=FrozenDict)
def check_FrozenDict_as_cased_record__free(field_name4case_name, x):
    check_mapping_as_cased_record__free(field_name4case_name, x, cls=FrozenDict)
def check_FrozenDict_as_cased_record(field_name4case_name, may_case_name, may_field_name_set, x, /):
    check_mapping_as_cased_record(field_name4case_name, may_case_name, may_field_name_set, x, cls=FrozenDict)
def check_FrozenDict_as_union_of_cased_records(field_name4case_name, case_name2may_field_name_set, x, /):
    check_mapping_as_union_of_cased_records(field_name4case_name, case_name2may_field_name_set, x, cls=FrozenDict)


check_union_of_cased_tuples
check_cased_tuple
check_cased_tuple__free
#check_cased_tuple__free_ex
check_empty
check_nonempty
check_nonempty_str

check_FrozenDict_as_record__free
check_FrozenDict_as_record
check_FrozenDict_as_cased_record__free
check_FrozenDict_as_cased_record
check_FrozenDict_as_union_of_cased_records

check_mapping_as_record__free
check_mapping_as_record
check_mapping_as_cased_record__free
check_mapping_as_cased_record
check_mapping_as_union_of_cased_records



def check_is_None(obj, /):
    if obj is not None: raise TypeError
def check_result_of_cmp(obj, /):
    '[-1..+1]'
    check_int(obj, min=-1, max=+1)
def check_result_of_partial_cmp__int(obj, /):
    '[-2..+1]'
    check_int(obj, min=-2, max=+1)
def check_result_of_partial_cmp__tmay(obj, /):
    'tmay [-1..+1]'
    check_tmay(obj, check_func=check_result_of_cmp)
check_icmp = check_result_of_cmp
check_ipcmp = check_result_of_partial_cmp__int
check_tpcmp = check_result_of_partial_cmp__tmay

check_is_None
check_result_of_cmp
check_result_of_partial_cmp__int
check_result_of_partial_cmp__tmay

check_icmp
check_ipcmp
check_tpcmp
#########################################
#########################################
#########################################



#HHHHH
class check_funcs:
    'check_pair ==>> check_funcs.pair'
    ...
# import from seed.helper.check.check
    Lookupable = check_Lookupable
    namedtuple_type = check_namedtuple_type
    has_attrs = check_has_attrs
    callable = check_callable
    subclass = check_subclass
    instance = check_instance
    instance_all = check_instance_all
    type_is = check_type_is
    tuple = check_tuple
    len_eq = check_len_eq
    int = check_int
    iterable = check_iterable
    type_tree = check_type_tree

    #
# required by seed.helper.repr.repr_api
    _ = check_
    int_ge_neg1 = check_int_ge_neg1
    uint_imay = check_uint_imay
    finite_float = check_finite_float
    finite_complex = check_finite_complex
    float = check_float
    complex = check_complex
    str = check_str
    bytes = check_bytes
    bool = check_bool
    uint = check_uint
    instance_or_None = check_instance_or_None
    mapping = check_mapping
    iterator = check_iterator
    reiterable = check_reiterable
    pairs_of = check_pairs_of
    sorted = check_sorted
    all = check_all
    pair = check_pair
    ###########################
    'see: check_uint_imay/check_tmay/check_nmay/check_is_obj_or/check_instance_or_None'
    tmay = check_tmay
    nmay = check_nmay
    is_obj_or = check_is_obj_or
    ###########################
    strict_sorted = check_strict_sorted
    int_ge1 = check_int_ge1
    int_ge2 = check_int_ge2
    ###########################
    seq = check_seq
    len_of = check_len_of
    ###########################
    union_of_cased_tuples = check_union_of_cased_tuples
    cased_tuple = check_cased_tuple
    cased_tuple__free = check_cased_tuple__free
    #cased_tuple__free_ex = check_cased_tuple__free_ex
    empty = check_empty
    nonempty = check_nonempty
    nonempty_str = check_nonempty_str

    FrozenDict_as_record__free = check_FrozenDict_as_record__free
    FrozenDict_as_record = check_FrozenDict_as_record
    FrozenDict_as_cased_record__free = check_FrozenDict_as_cased_record__free
    FrozenDict_as_cased_record = check_FrozenDict_as_cased_record
    FrozenDict_as_union_of_cased_records = check_FrozenDict_as_union_of_cased_records

    mapping_as_record__free = check_mapping_as_record__free
    mapping_as_record = check_mapping_as_record
    mapping_as_cased_record__free = check_mapping_as_cased_record__free
    mapping_as_cased_record = check_mapping_as_cased_record
    mapping_as_union_of_cased_records = check_mapping_as_union_of_cased_records

    is_None = check_is_None
    result_of_cmp = check_result_of_cmp
    result_of_partial_cmp__int = check_result_of_partial_cmp__int
    result_of_partial_cmp__tmay = check_result_of_partial_cmp__tmay
    icmp = check_icmp
    ipcmp = check_ipcmp
    tpcmp = check_tpcmp
    ###########################
    ###########################
    ###########################
    ###########################
checks = check_funcs


class checkers:
    float = checker4float
    complex = checker4complex
    finite_float = checker4finite_float
    finite_complex = checker4finite_complex

    str = checker4str
    pseudo_identifier = checker4pseudo_identifier
    identifier = checker4identifier
    qual_name = checker4qual_name

    ###################
    tribool = checker4tribool
    # = checker4#
    # = checker4#
    # = checker4#
    # = checker4#
    # = checker4#
    # = checker4#
    # = checker4#











#HHHHH
if 1:
    if __name__ == '__main__':
        from seed.helper.print_global_names import print_global_names
        print_global_names(globals())




if __name__ == "__main__":
    import doctest
    doctest.testmod()

#HHHHH





