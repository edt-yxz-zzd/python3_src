rename:
    IDecomposableOps4OneMainObjType4lookupable
    Mixin__Ops4OneMainObjType__main_obj_is_int/...
    add Decomposable for all IDecomposableOps4OneMainObjType
#HHHHH
r'''
TODO:
    ops class re-export by diff module
    auto gen wrapped class src-code 4 abc
        view ../../python3_src/my_convention/overridable_method__to_auto_generate_wrapper_class_forward_call_src_code.txt
    auto gen wrapped class src-code 4 abc

DONE:
    measure()===echo
    measure()===getitem/index

    monoid 4 tuple as point
        no monoid 4 tuple as array
            too slow
    monoid 4 namedtuple
    monoid 4 cased_tuple
    xxx xxx monoid 4 union_of_cased_tuples
    monoid 4 FrozenDict as record

seed.ops.___IOps4OneMainObjType___
    <--mv--- seed.ops.IOps4OneMainObjType
    split to many modules
py -m seed.ops.___IOps4OneMainObjType___


seed.ops.IOps4OneMainObjType
from seed.ops.IOps4OneMainObjType import _mk_reversed_ops



py -m seed.ops.IOps4OneMainObjType
py -m seed.ops.IOps4OneMainObjType > /sdcard/0my_files/tmp/xxx/debug_out.txt
    #to generate __all__&toplevel_defs:
    py -m seed.debug._debug > /sdcard/0my_files/tmp/xxx/debug_out.txt


see:
    MonoidOps4tuple_as_mapping.__doc__ #__doc__MonoidOps4tuple_as_mapping
    MonoidOps4FrozenDict_as_union_of_cased_records.__doc__ #__doc__MonoidOps4FrozenDict_as_union_of_cased_records


#HHHHH
from seed.helper.check.checkers import check_mapping, check_strict_sorted, check_int_ge1, check_int_ge2, check_all, check_pair, check_seq, check_len_of, check_str


from collections import namedtuple
import operator





======================
======================
======================
======================
module: __main__: global def heads
======================
======================





#'''

#HHHHH
___begin_mark_of_excluded_global_names__0___ = ...

if __name__ == '__main__':
    #put anywhere, neednot at eof
    from seed.debug._debug import main__print_infos_of_modules as _main
    _main([__name__])

__all__ = '''





    _mk_reversed_ops
    '''.split()
    #_mk_reversed_ops
        #used by external mk_ReversedFingerTreeOps/class ReversedFingerTreeOps
        #   must export!!!

#HHHHH
from seed.helper.check.checkers import check_is_None, check_result_of_cmp, check_result_of_partial_cmp__int, check_int, check_uint, check_uint_imay, check_instance, check_tmay, check_callable, check_bool, check_union_of_cased_tuples, check_cased_tuple, check_instance_all, check_tuple, check_type_is, check_cased_tuple__free, check_nonempty_str, check_iterable, check_nmay, check_subclass
from seed.helper.check.checkers import (
    check_FrozenDict_as_record__free
    ,check_FrozenDict_as_record
    ,check_FrozenDict_as_cased_record__free
    ,check_FrozenDict_as_cased_record
    ,check_FrozenDict_as_union_of_cased_records

    ,check_mapping_as_record__free
    ,check_mapping_as_record
    ,check_mapping_as_cased_record__free
    ,check_mapping_as_cased_record
    ,check_mapping_as_union_of_cased_records
    )


from seed.for_libs.for_functools.reduce import reduce_with_tmay
from seed.tiny import echo
from seed.abc.ISingleton import ISingleton
from seed.abc.abc import override, def_new_method, overridable_default_method, collaboration_method_chain, final_method
from seed.types.FrozenDict import FrozenDict, mk_FrozenDict

from abc import ABC, abstractmethod
from collections.abc import Mapping
import itertools

___end_mark_of_excluded_global_names__0___ = ...






#HHHHH
class IOps4OneMainObjType(ABC):
    @abstractmethod
    def ___careless_check_main_obj___(sf, x, /):
        'a -> (None|raise) #see:careless_check_main_obj'
    #def careless_check_io_arg_of_assoc_bin_op(sf, x, /):
    def careless_check_main_obj(sf, x, /):
        'a -> (None|raise) #see:___careless_check_main_obj___'
        r = type(sf).___careless_check_main_obj___(sf, x)
        check_is_None(r)
        return None
    def careless_check_main_objs(sf, /, *xs):
        '*a -> (None|raise) #see:careless_check_main_obj'
        for _ in map(sf.careless_check_main_obj, xs):pass

class IEqOps(IOps4OneMainObjType):
    r'''

    @abstractmethod
    def ___careless_check_main_obj___(sf, x, /):
        'a -> (None|raise) #see:careless_check_main_obj'
    @abstractmethod
    def ___eq___(sf, lhs, rhs, /):
        '-> bool #see:eq'
    #'''
    @abstractmethod
    def ___eq___(sf, lhs, rhs, /):
        '-> bool #see:eq'
    def eq(sf, lhs, rhs, /):
        '-> bool #see:___eq___'
        sf.careless_check_main_objs(lhs, rhs)
        b = type(sf).___eq___(sf, lhs, rhs)
        check_bool(b)
        _check_eq__when_is(b, lhs, rhs)
        return b

    def ne(sf, lhs, rhs, /):
        '-> bool #see:eq'
        return not sf.eq(lhs, rhs)

class ResultOfCMP:
    LT = -1
    EQ = 0
    GT = +1
    check = check_result_of_cmp
class ResultOfPartialCMP(ResultOfCMP):
    NA = -2
    check = check_result_of_partial_cmp__int
def cmp__int(lhs, rhs, /):
    return cmp__default(lhs, rhs)
def cmp__by_lt(lt, lhs, rhs, /):
    if lt(lhs, rhs):
        return ResultOfCMP.LT
    elif lt(rhs, lhs):
        return ResultOfCMP.GT
    else:
        return ResultOfCMP.EQ
def cmp__by_eq_lt(eq, lt, lhs, rhs, /):
    if eq(lhs, rhs):
        return ResultOfCMP.EQ
    elif lt(lhs, rhs):
        return ResultOfCMP.LT
    else:
        return ResultOfCMP.GT
def cmp__default__lt_eq_gt(lhs, rhs, /):
    if lhs < rhs:
        return ResultOfCMP.LT
    elif lhs == rhs:
        return ResultOfCMP.EQ
    else:
        return ResultOfCMP.GT
def cmp__default__lt_gt_eq(lhs, rhs, /):
    if lhs < rhs:
        return ResultOfCMP.LT
    elif lhs > rhs:
        return ResultOfCMP.GT
    else:
        return ResultOfCMP.EQ
def cmp__default__eq_lt_gt(lhs, rhs, /):
    if lhs == rhs:
        return ResultOfCMP.EQ
    elif lhs < rhs:
        return ResultOfCMP.LT
    else:
        return ResultOfCMP.GT
cmp__default = cmp__default__eq_lt_gt
    #better than cmp__default__lt_eq_gt #since eq stop faster and may used in loop
cmp__default__by_eq_lt = cmp__default__eq_lt_gt
cmp__default__by_lt = cmp__default__lt_gt_eq


def _check_eq__when_is(result, lhs, rhs, /):
    if lhs is rhs:
        if not result is True: raise ValueError
def _check_partial_le__when_is(result, lhs, rhs, /):
    if lhs is rhs:
        if not result is True: raise ValueError
def _check_partial_lt__when_is(result, lhs, rhs, /):
    if lhs is rhs:
        if not result is False: raise ValueError
def _check_partial_cmp__when_is(result, lhs, rhs, /):
    if lhs is rhs:
        if not result == ResultOfPartialCMP.EQ: raise ValueError
_check_lt__when_is = _check_partial_lt__when_is
_check_cmp__when_is = _check_partial_cmp__when_is

class IPartialOrderingOps(IEqOps):
    r'''
    ResultOfPartialCMP/check_result_of_partial_cmp__int: -2=N/A; -1=LT; 0=EQ; +1=GT

    @abstractmethod
    def ___careless_check_main_obj___(sf, x, /):
        'a -> (None|raise) #see:careless_check_main_obj'
    @abstractmethod
    def ___eq___(sf, lhs, rhs, /):
        '-> bool #see:eq'
    @abstractmethod
    def ___partial_le___(sf, lhs, rhs, /):
        '-> bool #see:partial_le'
    @abstractmethod
    def ___partial_lt___(sf, lhs, rhs, /):
        '-> bool #see:partial_lt'
    @abstractmethod
    def ___partial_cmp___(sf, lhs, rhs, /):
        '-> [-2..+1] #see:partial_cmp'
    #'''
    @abstractmethod
    def ___partial_le___(sf, lhs, rhs, /):
        '-> bool #see:partial_le'
    def partial_le(sf, lhs, rhs, /):
        '-> bool #see:___partial_le___'
        sf.careless_check_main_objs(lhs, rhs)
        b = type(sf).___partial_le___(sf, lhs, rhs)
        check_bool(b)
        _check_partial_le__when_is(b, lhs, rhs)
        return b

    @abstractmethod
    def ___partial_lt___(sf, lhs, rhs, /):
        '-> bool #see:partial_lt'
    def partial_lt(sf, lhs, rhs, /):
        '-> bool #see:___partial_lt___'
        sf.careless_check_main_objs(lhs, rhs)
        b = type(sf).___partial_lt___(sf, lhs, rhs)
        check_bool(b)
        _check_partial_lt__when_is(b, lhs, rhs)
        return b

    @abstractmethod
    def ___partial_cmp___(sf, lhs, rhs, /):
        '-> [-2..+1] #see:partial_cmp'
    def partial_cmp(sf, lhs, rhs, /):
        '-> [-2..+1] #see:___partial_cmp___'
        sf.careless_check_main_objs(lhs, rhs)
        r = type(sf).___partial_cmp___(sf, lhs, rhs)
        check_result_of_partial_cmp__int(r)
        _check_partial_cmp__when_is(r, lhs, rhs)
        return r
#end of class IPartialOrderingOps(IEqOps):
class IPartialOrderingOps__with_max_TOP(IPartialOrderingOps):
    @abstractmethod
    def ___get_max_TOP___(sf, /):
        '-> (TOP::main_obj) #the max main_obj #[any main_obj <= TOP] #see:get_max_TOP'
    def get_max_TOP(sf, /):
        '-> (TOP::main_obj) #the max main_obj #[any main_obj <= TOP] #see:___get_max_TOP___'
        TOP = type(sf).___get_max_TOP___(sf)
        sf.careless_check_main_obj(TOP)
        return TOP
#end of class IPartialOrderingOps__with_max_TOP(IPartialOrderingOps):
class IPartialOrderingOps__with_min_BOTTOM(IPartialOrderingOps):
    @abstractmethod
    def ___get_min_BOTTOM___(sf, /):
        '-> (BOTTOM::main_obj) #the min main_obj #[BOTTOM <= any main_obj] #see:get_min_BOTTOM'
    def get_min_BOTTOM(sf, /):
        '-> (BOTTOM::main_obj) #the min main_obj #[BOTTOM <= any main_obj] #see:get_min_BOTTOM'
        BOTTOM = type(sf).___get_min_BOTTOM___(sf)
        sf.careless_check_main_obj(BOTTOM)
        return BOTTOM
#end of class IPartialOrderingOps__with_min_BOTTOM(IPartialOrderingOps):



#begin of class_ITotalOrderingOps(IPartialOrderingOps):
class ITotalOrderingOps(IPartialOrderingOps):
    #class IComparableOps(IOps4OneMainObjType):
    #begin of __doc__ITotalOrderingOps:ITotalOrderingOps.__doc__
    r'''
    ResultOfCMP/check_result_of_cmp: -1=LT; 0=EQ; +1=GT

    not default impl eq by cmp:
        <<== see eq__seq impl
        shortcut when len diff!!!
        ITotalOrderingOps__cmp2eq
        ITotalOrderingOps__cmp2eq_lt
    default impl lt by cmp:
        <<== see lt__seq impl
            call cmp__seq inside
        ITotalOrderingOps__cmp2lt
            # almost use ITotalOrderingOps__cmp2lt instead of ITotalOrderingOps
    impl cmp by detect eq first:
        why ???use cmp__default__eq_lt_gt instead of cmp__default__lt_eq_gt???
        <<== see cmp__seq/cmp__int impl
            detect element eq inside loop
            detect element lt outside loop
        i.e. cmp__default__by_eq_lt = use cmp__default__eq_lt_gt instead of cmp__default__lt_eq_gt

    #####################################
    #####################################
    #####################################
    #####################################
    #####################################
    why ???no ITotalOrderingOps__lt2cmp/ITotalOrderingOps__lt2eq???
        see:
            ITotalOrderingOps__lt2eq_cmp
            ITotalOrderingOps__eq_lt2cmp
        ##################
        no ITotalOrderingOps__lt2cmp
            if impl cmp by lt:
                if use cmp__default__eq_lt_gt/cmp__default__lt_eq_gt:
                    ==>> must have eq
                    ==>> ITotalOrderingOps__eq_lt2cmp
                if use cmp__default__lt_gt_eq:
                    ==>> impl eq by lt
                    ==>> ITotalOrderingOps__lt2eq_cmp
        ##################
        no ITotalOrderingOps__lt2eq
            if impl eq by lt:
                ==>> use cmp__default__lt_gt_eq
                ==>> impl cmp by lt
                ==>> ITotalOrderingOps__lt2eq_cmp


########################################
########################################
########################################
class ITotalOrderingOps(IPartialOrderingOps):
class ITotalOrderingOps__seq(ITotalOrderingOps):
class ITotalOrderingOps__default_total_ordering(ITotalOrderingOps):
class ITotalOrderingOps__cmp2eq(ITotalOrderingOps):
class ITotalOrderingOps__cmp2lt(ITotalOrderingOps):
class ITotalOrderingOps__cmp2eq_lt(ITotalOrderingOps__cmp2lt, ITotalOrderingOps__cmp2eq):pass
class ITotalOrderingOps__eq_lt2cmp(ITotalOrderingOps):
class ITotalOrderingOps__lt2eq_cmp(ITotalOrderingOps__cmp2eq):

########################################
########################################
########################################

    @abstractmethod
    def ___careless_check_main_obj___(sf, x, /):
        'a -> (None|raise) #see:careless_check_main_obj'
    @abstractmethod
    def ___eq___(sf, lhs, rhs, /):
        '-> bool #see:eq'
    @abstractmethod
    def ___lt___(sf, lhs, rhs, /):
        '-> bool #see:lt'
    @abstractmethod
    def ___cmp___(sf, lhs, rhs, /):
        '-> [-1..+1] #see:cmp'

    #'''
    #end of __doc__ITotalOrderingOps


    @abstractmethod
    def ___lt___(sf, lhs, rhs, /):
        '-> bool #see:lt'
    def lt(sf, lhs, rhs, /):
        '-> bool #see:___lt___'
        sf.careless_check_main_objs(lhs, rhs)
        b = type(sf).___lt___(sf, lhs, rhs)
        check_bool(b)
        _check_lt__when_is(b, lhs, rhs)
        return b

    @abstractmethod
    def ___cmp___(sf, lhs, rhs, /):
        '-> [-1..+1] #see:cmp'
    def cmp(sf, lhs, rhs, /):
        '-> [-1..+1] #see:___cmp___'
        sf.careless_check_main_objs(lhs, rhs)
        r = type(sf).___cmp___(sf, lhs, rhs)
        check_result_of_cmp(r)
        _check_cmp__when_is(r, lhs, rhs)
        return r


    @override
    def ___partial_le___(sf, lhs, rhs, /):
        '-> bool #see:partial_le'
        return not type(sf).___lt___(sf, rhs, lhs)
    @override
    def ___partial_lt___(sf, lhs, rhs, /):
        '-> bool #see:partial_lt'
        return type(sf).___lt___(sf, lhs, rhs)
    @override
    def ___partial_cmp___(sf, lhs, rhs, /):
        '-> [-2..+1] #see:partial_cmp'
        return type(sf).___cmp___(sf, lhs, rhs)

    def le(sf, lhs, rhs, /):
        '-> bool #see:lt'
        return not sf.lt(rhs, lhs)
    def gt(sf, lhs, rhs, /):
        '-> bool #see:lt'
        return sf.lt(rhs, lhs)
    def ge(sf, lhs, rhs, /):
        '-> bool #see:lt'
        return not sf.lt(lhs, rhs)

    def max(sf, lhs, rhs, /):
        return rhs if sf.lt(lhs, rhs) else lhs
    def min(sf, lhs, rhs, /):
        return rhs if sf.lt(rhs, lhs) else lhs
    def max1s(sf, lhs, rhss, /):
        'a -> Iter a -> a'
        op = sf.max
        #functools.reduce
        return reduce_with_tmay(op, [lhs], rhss)
    def min1s(sf, lhs, rhss, /):
        'a -> Iter a -> a'
        op = sf.min
        #functools.reduce
        return reduce_with_tmay(op, [lhs], rhss)

#end of class ITotalOrderingOps(IPartialOrderingOps):
#end of class_ITotalOrderingOps(IPartialOrderingOps):
class ITotalOrderingOps__with_max_TOP(ITotalOrderingOps, IPartialOrderingOps__with_max_TOP):pass
class ITotalOrderingOps__with_min_BOTTOM(ITotalOrderingOps, IPartialOrderingOps__with_min_BOTTOM):pass
class ITotalOrderingOps__with_min_BOTTOM_max_TOP(ITotalOrderingOps__with_min_BOTTOM, ITotalOrderingOps__with_max_TOP):pass


def eq__seq(element_eq, lhs, rhs, /):
    return eq__sized_ordered_iterable(element_eq, lhs, rhs)
def eq__sized_ordered_iterable(element_eq, lhs, rhs, /):
    if len(lhs) != len(rhs): return False
    if 0:
        return eq__ordered_iterable(element_eq, lhs, rhs)
    else:
        for x, y in zip(lhs, rhs):
            if not element_eq(x, y): return False
        return True
def eq__ordered_iterable(element_eq, lhs, rhs, /):
    def element_partial_cmp(x, y, /):
        if element_eq(x, y):
            return ResultOfPartialCMP.EQ
        else:
            return ResultOfPartialCMP.NA
    r = partial_cmp__ordered_iterable(element_partial_cmp, lhs, rhs)
    return r == ResultOfCMP.EQ

def cmp__seq(element_cmp, lhs, rhs, /):
    return partial_cmp__seq(element_cmp, lhs, rhs)
def cmp__sized_ordered_iterable(element_cmp, lhs, rhs, /):
    return partial_cmp__sized_ordered_iterable(element_cmp, lhs, rhs)
def cmp__ordered_iterable(element_cmp, lhs, rhs, /):
    return partial_cmp__ordered_iterable(element_cmp, lhs, rhs)
def lt__seq(element_cmp, lhs, rhs, /):
    return partial_lt__seq(element_cmp, lhs, rhs)
def lt__sized_ordered_iterable(element_cmp, lhs, rhs, /):
    return partial_lt__sized_ordered_iterable(element_cmp, lhs, rhs)
def lt__ordered_iterable(element_cmp, lhs, rhs, /):
    return partial_lt__ordered_iterable(element_cmp, lhs, rhs)


def partial_le__seq(element_partial_cmp, lhs, rhs, /):
    return partial_le__sized_ordered_iterable(element_partial_cmp, lhs, rhs)
def partial_le__sized_ordered_iterable(element_partial_cmp, lhs, rhs, /):
    if not rhs: return not lhs
    if not lhs: return True

    if 1:
        return partial_le__ordered_iterable(element_partial_cmp, lhs, rhs)
    else:
        lsz, rsz = len(lhs), len(rhs)
        for x, y in zip(lhs, rhs):
            r = element_partial_cmp(x, y)
            if r != ResultOfCMP.EQ:
                return r == ResultOfCMP.LT
        return lsz <= rsz
        #bug: may be iterator: return len(lhs) <= len(rhs)
def partial_le__ordered_iterable(element_partial_cmp, lhs, rhs, /):
    r = partial_cmp__ordered_iterable(element_partial_cmp, lhs, rhs)
    return r == ResultOfCMP.LT or r == ResultOfCMP.EQ




def partial_lt__seq(element_partial_cmp, lhs, rhs, /):
    return partial_lt__sized_ordered_iterable(element_partial_cmp, lhs, rhs)
def partial_lt__sized_ordered_iterable(element_partial_cmp, lhs, rhs, /):
    if not rhs: return False
    if not lhs: return True

    if 1:
        return partial_lt__ordered_iterable(element_partial_cmp, lhs, rhs)
    else:
        lsz, rsz = len(lhs), len(rhs)
        for x, y in zip(lhs, rhs):
            r = element_partial_cmp(x, y)
            if r != ResultOfCMP.EQ:
                return r == ResultOfCMP.LT
        return lsz < rsz
        #bug: may be iterator: return len(lhs) < len(rhs)
def partial_lt__ordered_iterable(element_partial_cmp, lhs, rhs, /):
    r = partial_cmp__ordered_iterable(element_partial_cmp, lhs, rhs)
    return r == ResultOfCMP.LT


def partial_cmp__seq(element_partial_cmp, lhs, rhs, /):
    return partial_cmp__sized_ordered_iterable(element_partial_cmp, lhs, rhs)
def partial_cmp__sized_ordered_iterable(element_partial_cmp, lhs, rhs, /):
    if not rhs:
        if not lhs:
            return ResultOfCMP.EQ
        else:
            return ResultOfCMP.GT
    else:
        if not lhs:
            return ResultOfCMP.LT
        else:
            pass

    if 1:
        return cmp__ordered_iterable(element_partial_cmp, lhs, rhs)
    else:
        for x, y in zip(lhs, rhs):
            r = element_partial_cmp(x, y)
            if r != ResultOfCMP.EQ:
                return r
        return cmp__int(len(lhs), len(rhs))

def partial_cmp__ordered_iterable(element_partial_cmp, lhs, rhs, /):
    lhs = iter(lhs)
    rhs = iter(rhs)
    #for x, y in zip(lhs, rhs):
    Nothing = []
    while 1:
        x = next(lhs, Nothing)
        y = next(rhs, Nothing)
        if x is Nothing:
            if y is Nothing:
                #[], []
                return ResultOfCMP.EQ
            else:
                #[], [y]
                return ResultOfCMP.LT
        else:
            if y is Nothing:
                #[x], []
                return ResultOfCMP.GT
            else:
                #[x], [y]
                pass

        r = element_partial_cmp(x, y)
        if r != ResultOfCMP.EQ:
            return r
    raise logic-err
    #return cmp__int(len(lhs), len(rhs))
#end of def partial_cmp__ordered_iterable(element_partial_cmp, lhs, rhs, /):






class ITotalOrderingOps__seq(ITotalOrderingOps):
    @abstractmethod
    def ___get_seq_element_total_ordering_ops___(sf, /):
        '-> (element_total_ordering_ops::ITotalOrderingOps<element in seq>) #see:get_seq_element_total_ordering_ops'
    def get_seq_element_total_ordering_ops(sf, /):
        '-> (element_total_ordering_ops::ITotalOrderingOps<element in seq>) #see:___get_seq_element_total_ordering_ops___'
        element_total_ordering_ops = type(sf).___get_seq_element_total_ordering_ops___(sf)
        check_instance(ITotalOrderingOps, element_total_ordering_ops)
        return element_total_ordering_ops

    @override
    def ___eq___(sf, lhs, rhs, /):
        '-> bool #see:eq'
        if len(lhs) != len(rhs): return False
        ops = sf.get_seq_element_total_ordering_ops()
        element_eq = ops.eq
        return eq__seq(element_eq, lhs, rhs)

    @override
    def ___lt___(sf, lhs, rhs, /):
        '-> bool #see:lt'
        ops = sf.get_seq_element_total_ordering_ops()
        element_cmp = ops.cmp
        return lt__seq(element_cmp, lhs, rhs)

    @override
    def ___cmp___(sf, lhs, rhs, /):
        '-> [-2..+1] #see:cmp'
        ops = sf.get_seq_element_total_ordering_ops()
        element_cmp = ops.cmp
        return cmp__seq(element_cmp, lhs, rhs)
#end of class ITotalOrderingOps__seq(ITotalOrderingOps):



class ITotalOrderingOps__default_total_ordering(ITotalOrderingOps):
    @override
    def ___eq___(sf, lhs, rhs, /):
        '-> bool #see:eq'
        return lhs == rhs
    @override
    def ___lt___(sf, lhs, rhs, /):
        '-> bool #see:lt'
        return lhs < rhs
    @override
    def ___cmp___(sf, lhs, rhs, /):
        '-> [-1..+1] #see:cmp'
        return cmp__default(lhs, rhs)
        return cmp__default__eq_lt_gt(lhs, rhs)
#end of class ITotalOrderingOps__default_total_ordering(ITotalOrderingOps):
class TheTotalOrderingOps__default_total_ordering(ITotalOrderingOps__default_total_ordering, ISingleton):
    @override
    def ___careless_check_main_obj___(sf, x, /):
        'a -> (None|raise) #see:careless_check_main_obj'
        pass
the_total_ordering_ops__py_obj = TheTotalOrderingOps__default_total_ordering()
assert the_total_ordering_ops__py_obj is TheTotalOrderingOps__default_total_ordering()

class ITotalOrderingOps__cmp2eq(ITotalOrderingOps):
    @override
    def ___eq___(sf, lhs, rhs, /):
        '-> bool #see:eq'
        return sf.cmp(lhs, rhs) == ResultOfCMP.EQ
#end of class ITotalOrderingOps__cmp2eq(ITotalOrderingOps):
class ITotalOrderingOps__cmp2lt(ITotalOrderingOps):
    @override
    def ___lt___(sf, lhs, rhs, /):
        '-> bool #see:lt'
        return sf.cmp(lhs, rhs) == ResultOfCMP.LT
#end of class ITotalOrderingOps__cmp2lt(ITotalOrderingOps):
class ITotalOrderingOps__cmp2eq_lt(ITotalOrderingOps__cmp2lt, ITotalOrderingOps__cmp2eq):pass
#end of class ITotalOrderingOps__cmp2eq_lt(ITotalOrderingOps__cmp2lt, ITotalOrderingOps__cmp2eq):pass
class ITotalOrderingOps__eq_lt2cmp(ITotalOrderingOps):
    r'''
    why ???no ITotalOrderingOps__lt2cmp/ITotalOrderingOps__lt2eq???
        see: ITotalOrderingOps.__doc__
        #__doc__ITotalOrderingOps
    why ???use cmp__default__eq_lt_gt instead of cmp__default__lt_eq_gt???
        see: ITotalOrderingOps.__doc__
        #__doc__ITotalOrderingOps
    #'''
    @override
    def ___cmp___(sf, lhs, rhs, /):
        '-> [-1..+1] #see:cmp'
        return cmp__by_eq_lt(sf.eq, sf.lt, lhs, rhs)
#end of class ITotalOrderingOps__eq_lt2cmp(ITotalOrderingOps):
class ITotalOrderingOps__lt2eq_cmp(ITotalOrderingOps__cmp2eq):
    r'''
    why ???no ITotalOrderingOps__lt2cmp/ITotalOrderingOps__lt2eq???
        see: ITotalOrderingOps.__doc__
        #__doc__ITotalOrderingOps
    #'''
    @override
    def ___cmp___(sf, lhs, rhs, /):
        '-> [-1..+1] #see:cmp'
        return cmp__by_lt(sf.lt, lhs, rhs)
#end of class ITotalOrderingOps__lt2eq_cmp(ITotalOrderingOps__cmp2eq):










class Mixin__Ops4OneMainObjType__main_obj_is_int(IOps4OneMainObjType):
    @override
    def ___careless_check_main_obj___(sf, x, /):
        'a -> (None|raise) #see:careless_check_main_obj'
        check_int(x)
class Mixin__Ops4OneMainObjType__main_obj_is_imay(Mixin__Ops4OneMainObjType__main_obj_is_int):
    @override
    def ___careless_check_main_obj___(sf, x, /):
        'a -> (None|raise) #see:careless_check_main_obj'
        check_uint_imay(x)
class Mixin__Ops4OneMainObjType__main_obj_is_uint(Mixin__Ops4OneMainObjType__main_obj_is_imay):
    @override
    def ___careless_check_main_obj___(sf, x, /):
        'a -> (None|raise) #see:careless_check_main_obj'
        check_uint(x)
class Mixin__Ops4OneMainObjType__main_obj_is_tmay_pyobj(IOps4OneMainObjType):
    @override
    def ___careless_check_main_obj___(sf, x, /):
        'a -> (None|raise) #see:careless_check_main_obj'
        check_tmay(x)

class ITotalOrderingOps__default_total_ordering__with_max_TOP(ITotalOrderingOps__default_total_ordering, ITotalOrderingOps__with_max_TOP):pass
class ITotalOrderingOps__default_total_ordering__with_min_BOTTOM(ITotalOrderingOps__default_total_ordering, ITotalOrderingOps__with_min_BOTTOM):pass
class ITotalOrderingOps__default_total_ordering__with_min_BOTTOM_max_TOP(ITotalOrderingOps__default_total_ordering, ITotalOrderingOps__with_min_BOTTOM_max_TOP):pass

class TotalOrderingOps__int(Mixin__Ops4OneMainObjType__main_obj_is_int, ITotalOrderingOps__default_total_ordering):pass
class TotalOrderingOps__uint(Mixin__Ops4OneMainObjType__main_obj_is_uint, ITotalOrderingOps__default_total_ordering__with_min_BOTTOM):
    @override
    def ___get_min_BOTTOM___(sf, /):
        '-> (BOTTOM::main_obj) #the min main_obj #[BOTTOM <= any main_obj] #see:get_min_BOTTOM'
        return 0
class TotalOrderingOps__imay(Mixin__Ops4OneMainObjType__main_obj_is_imay, ITotalOrderingOps__default_total_ordering__with_min_BOTTOM):
    @override
    def ___get_min_BOTTOM___(sf, /):
        '-> (BOTTOM::main_obj) #the min main_obj #[BOTTOM <= any main_obj] #see:get_min_BOTTOM'
        return -1


class TheTotalOrderingOps__int(TotalOrderingOps__int, ISingleton):pass
class TheTotalOrderingOps__uint(TotalOrderingOps__uint, ISingleton):pass
class TheTotalOrderingOps__imay(TotalOrderingOps__imay, ISingleton):pass
the_total_ordering_ops__int = TheTotalOrderingOps__int()
assert the_total_ordering_ops__int is TheTotalOrderingOps__int()
the_total_ordering_ops__uint = TheTotalOrderingOps__uint()
assert the_total_ordering_ops__uint is TheTotalOrderingOps__uint()
the_total_ordering_ops__imay = TheTotalOrderingOps__imay()
assert the_total_ordering_ops__imay is TheTotalOrderingOps__imay()







class IAssocBinaryOps(IOps4OneMainObjType):
    r'''
    associative law
    law of association
    #'''
    @abstractmethod
    def ___is_assoc_bin_op_commutable___(sf, /):
        '-> (commutable::bool) #see:is_assoc_bin_op_commutable'
    def is_assoc_bin_op_commutable(sf, /):
        '-> (commutable::bool) #see:___is_assoc_bin_op_commutable___'
        b = type(sf).___is_assoc_bin_op_commutable___(sf)
        check_bool(b)
        return b

    @abstractmethod
    def ___assoc_bin_op___(sf, lhs, rhs, /):
        'a -> a -> a # (a*b)*c === a*(b*c) #see:assoc_bin_op'
    def assoc_bin_op(sf, lhs, rhs, /,*, flip:bool=False):
        'a -> a -> a # (a*b)*c === a*(b*c) #see:___assoc_bin_op___'
        sf.careless_check_main_objs(lhs, rhs)
        if flip:
            lhs, rhs = rhs, lhs
        result = type(sf).___assoc_bin_op___(sf, lhs, rhs)
        sf.careless_check_main_obj(result)
        return result
    def assoc_op1s(sf, lhs, rhss, /,*, flip:bool=False):
        'a -> Iter a -> a'
        op = sf.assoc_bin_op
        #functools.reduce
        return reduce_with_tmay(op, [lhs], rhss, flip=flip)
class IAssocBinaryOps__commutable(IAssocBinaryOps):
    @override
    def ___is_assoc_bin_op_commutable___(sf, /):
        '-> (commutable::bool) #see:is_assoc_bin_op_commutable'
        return True
class IMonoidOps(IAssocBinaryOps):
    r'''
    Monoid
    semigroup

    @abstractmethod
    def ___careless_check_main_obj___(sf, x, /):
        'a -> (None|raise) #see:careless_check_main_obj'
    @abstractmethod
    def ___is_assoc_bin_op_commutable___(sf, /):
        '-> (commutable::bool) #see:is_assoc_bin_op_commutable'
    @abstractmethod
    def ___assoc_bin_op___(sf, lhs, rhs, /):
        'a -> a -> a # (a*b)*c === a*(b*c) #see:assoc_bin_op'
    @abstractmethod
    def ___get_monoid_identity___(sf, /):
        '-> 1 # 1*a === a*1 === a::monoid_obj #see:get_monoid_identity'
    #'''

    @abstractmethod
    def ___get_monoid_identity___(sf, /):
        '-> 1 # 1*a === a*1 === a::monoid_obj #see:get_monoid_identity'
    def get_monoid_identity(sf, /):
        '-> 1 # 1*a === a*1 === a::monoid_obj #see:___get_monoid_identity___'
        monoid_identity = type(sf).___get_monoid_identity___(sf)
        sf.careless_check_main_obj(monoid_identity)
        return monoid_identity

    def assoc_op0s(sf, rhss, /,*, flip:bool=False):
        'Iter a -> a'
        init = sf.get_monoid_identity()
        return sf.assoc_op1s(init, rhss)
    def assoc_op01s__tmay(sf, tmay_lhs, rhss, /,*, flip:bool=False):
        if tmay_lhs:
            [lhs] = tmay_lhs
            return sf.assoc_op1s(lhs, rhss)
        else:
            return sf.assoc_op0s(rhss)
class IMonoidOps__commutable(IMonoidOps, IAssocBinaryOps__commutable):
    pass

class IMeasurableOps(IMonoidOps):
    'IMeasurableOps<measurable_monoid_obj, measured_result_monoid_obj>'
    @abstractmethod
    def ___get_monoid_ops4measured_result___(measurable_ops, /):
        '-> monoid_ops<measured_result>::IMonoidOps #see:get_monoid_ops4measured_result'
    def get_monoid_ops4measured_result(measurable_ops, /):
        '-> monoid_ops<measured_result>::IMonoidOps #see:___get_monoid_ops4measured_result___'
        sf = measurable_ops
        monoid_ops4measured_result = type(sf).___get_monoid_ops4measured_result___(sf)
        check_instance(IMonoidOps, monoid_ops4measured_result)
        if measurable_ops.is_assoc_bin_op_commutable() and not monoid_ops4measured_result.is_assoc_bin_op_commutable():raise ValueError
        return monoid_ops4measured_result

    @abstractmethod
    def ___measure___(measurable_ops, measurable_obj, /):
        'measurable_obj -> (measured_result::monoid_obj) #see:measure'
    def measure(measurable_ops, measurable_obj, /):
        'measurable_obj -> (measured_result::monoid_obj) #see:___measure___'
        measured_result = type(measurable_ops).___measure___(measurable_ops, measurable_obj)
        monoid_ops4measured_result = measurable_ops.get_monoid_ops4measured_result()
        monoid_ops4measured_result.careless_check_main_obj(measured_result)
        return measured_result



class IMeasurableOps__commutable(IMeasurableOps, IMonoidOps__commutable):
    @override
    def ___get_monoid_ops4measured_result___(measurable_ops, /):
        '-> monoid_ops<measured_result>::IMonoidOps #see:get_monoid_ops4measured_result'
        commutable_monoid_ops4measured_result = measurable_ops.get_commutable_monoid_ops4measured_result()
        return commutable_monoid_ops4measured_result
    @abstractmethod
    def ___get_commutable_monoid_ops4measured_result___(measurable_ops, /):
        '-> commutable monoid_ops<measured_result>::IMonoidOps #see:get_commutable_monoid_ops4measured_result'
    def get_commutable_monoid_ops4measured_result(measurable_ops, /):
        '-> commutable monoid_ops<measured_result>::IMonoidOps #see:___get_commutable_monoid_ops4measured_result___'
        sf = measurable_ops
        commutable_monoid_ops4measured_result = type(sf).___get_commutable_monoid_ops4measured_result___(sf)
        check_instance(IMonoidOps, commutable_monoid_ops4measured_result)
        if not commutable_monoid_ops4measured_result.is_assoc_bin_op_commutable():raise ValueError
        return commutable_monoid_ops4measured_result

#end of class IMeasurableOps__commutable(IMeasurableOps, IMonoidOps__commutable):

class IMeasurableOps__measure_is_echo(IMeasurableOps):
    'measurable_op is measured_result'
    @override
    def ___measure___(measurable_ops, measurable_obj, /):
        'measurable_obj -> (measured_result::monoid_obj) #see:measure'
        measured_result = echo(measurable_obj)
        return measured_result
    @override
    def ___get_monoid_ops4measured_result___(measurable_ops, /):
        '-> monoid_ops<measured_result>::IMonoidOps #see:get_monoid_ops4measured_result'
        monoid_ops4measured_result = echo(measurable_ops)
        return monoid_ops4measured_result
#end of class IMeasurableOps__measure_is_echo(IMeasurableOps):





















class WrapperOps4OneMainObjType(IOps4OneMainObjType):
    def __init__(sf, ops4one_main_obj, /):
        check_instance(IOps4OneMainObjType, ops4one_main_obj)
        sf.__ops = ops4one_main_obj
        sf._check_ops4one_main_obj_(ops4one_main_obj)

    @final_method
    @def_new_method
    def get_original_ops4one_main_obj(sf, /):
        '-> (ops4one_main_obj::IOps4OneMainObjType)'
        return sf.__ops

    @collaboration_method_chain
    @def_new_method
    def _check_ops4one_main_obj_(sf, ops4one_main_obj, /):
        check_instance(IOps4OneMainObjType, ops4one_main_obj)

    #override_block[
    ##################################
    ##################################
    @overridable_default_method
    @override
    def ___careless_check_main_obj___(sf, x, /):
        'a -> (None|raise) #see:careless_check_main_obj'
        ops = sf.__ops
        return type(ops).___careless_check_main_obj___(ops, x)
    #override_block]

#end of class WrapperOps4OneMainObjType(IOps4OneMainObjType):

class WrapperAssocBinaryOps(WrapperOps4OneMainObjType, IAssocBinaryOps):
    @collaboration_method_chain
    @override
    def _check_ops4one_main_obj_(sf, assoc_bin_ops, /):
        check_instance(IAssocBinaryOps, assoc_bin_ops)

    @property
    @final_method
    @def_new_method
    def __ops(sf, /):
        return sf.get_original_ops4one_main_obj()

    @final_method
    @def_new_method
    def get_original_assoc_bin_ops(sf, /):
        '-> (assoc_bin_ops::IAssocBinaryOps)'
        return sf.__ops

    #override_block[
    ##################################
    ##################################
    @overridable_default_method
    @override
    def ___is_assoc_bin_op_commutable___(sf, /):
        '-> (commutable::bool) #see:is_assoc_bin_op_commutable'
        ops = sf.__ops
        return type(ops).___is_assoc_bin_op_commutable___(ops)

    @overridable_default_method
    @override
    def ___assoc_bin_op___(sf, lhs, rhs, /):
        'a -> a -> a # (a*b)*c === a*(b*c) #see:assoc_bin_op'
        ops = sf.__ops
        return type(ops).___assoc_bin_op___(ops, lhs, rhs)

    r'''[
    ##################################
    ##################################
    @overridable_default_method
    @override
    def ___careless_check_main_obj___(sf, x, /):
        'a -> (None|raise) #see:careless_check_main_obj'
        ops = sf.__ops
        return type(ops).___careless_check_main_obj___(ops, x)
    #]'''
    #override_block]

#end of class WrapperAssocBinaryOps(WrapperOps4OneMainObjType, IAssocBinaryOps):


class WrapperMonoidOps(WrapperAssocBinaryOps, IMonoidOps):
    @collaboration_method_chain
    @override
    def _check_ops4one_main_obj_(sf, monoid_ops, /):
        check_instance(IMonoidOps, monoid_ops)

    @property
    @final_method
    @def_new_method
    def __ops(sf, /):
        return sf.get_original_assoc_bin_ops()

    @final_method
    @def_new_method
    def get_original_monoid_ops(sf, /):
        '-> (monoid_ops::IMonoidOps)'
        return sf.__ops

    #override_block[
    ##################################
    ##################################
    @overridable_default_method
    @override
    def ___get_monoid_identity___(sf, /):
        '-> 1 # 1*a === a*1 === a::monoid_obj #see:get_monoid_identity'
        ops = sf.__ops
        return type(ops).___get_monoid_identity___(ops)

    r'''[
    ##################################
    ##################################
    @overridable_default_method
    @override
    def ___is_assoc_bin_op_commutable___(sf, /):
        '-> (commutable::bool) #see:is_assoc_bin_op_commutable'
        ops = sf.__ops
        return type(ops).___is_assoc_bin_op_commutable___(ops)

    @overridable_default_method
    @override
    def ___assoc_bin_op___(sf, lhs, rhs, /):
        'a -> a -> a # (a*b)*c === a*(b*c) #see:assoc_bin_op'
        ops = sf.__ops
        return type(ops).___assoc_bin_op___(ops, lhs, rhs)

    ##################################
    ##################################
    @overridable_default_method
    @override
    def ___careless_check_main_obj___(sf, x, /):
        'a -> (None|raise) #see:careless_check_main_obj'
        ops = sf.__ops
        return type(ops).___careless_check_main_obj___(ops, x)

    #]'''
    #override_block]


#end of class WrapperMonoidOps(WrapperAssocBinaryOps, IMonoidOps):

class WrapperMeasurableOps(WrapperMonoidOps, IMeasurableOps):
    @collaboration_method_chain
    @override
    def _check_ops4one_main_obj_(sf, measurable_ops, /):
        check_instance(IMeasurableOps, measurable_ops)

    @property
    @final_method
    @def_new_method
    def __ops(sf, /):
        return sf.get_original_monoid_ops()

    @final_method
    @def_new_method
    def get_original_measurable_ops(sf, /):
        '-> (measurable_ops::IMeasurableOps)'
        return sf.__ops

    #override_block[
    ##################################
    ##################################
    @overridable_default_method
    @override
    def ___get_monoid_ops4measured_result___(measurable_ops, /):
        '-> monoid_ops<measured_result>::IMonoidOps #see:get_monoid_ops4measured_result'
        sf = measurable_ops
        ops = sf.__ops
        return type(ops).___get_monoid_ops4measured_result___(ops)
    @overridable_default_method
    @override
    def ___measure___(measurable_ops, measurable_obj, /):
        'measurable_obj -> (measured_result::monoid_obj) #see:measure'
        sf = measurable_ops
        ops = sf.__ops
        return type(ops).___measure___(ops, measurable_obj)

    r'''[
    ##################################
    ##################################
    @overridable_default_method
    @override
    def ___get_monoid_identity___(sf, /):
        '-> 1 # 1*a === a*1 === a::monoid_obj #see:get_monoid_identity'
        ops = sf.__ops
        return type(ops).___get_monoid_identity___(ops)

    ##################################
    ##################################
    @overridable_default_method
    @override
    def ___is_assoc_bin_op_commutable___(sf, /):
        '-> (commutable::bool) #see:is_assoc_bin_op_commutable'
        ops = sf.__ops
        return type(ops).___is_assoc_bin_op_commutable___(ops)

    @overridable_default_method
    @override
    def ___assoc_bin_op___(sf, lhs, rhs, /):
        'a -> a -> a # (a*b)*c === a*(b*c) #see:assoc_bin_op'
        ops = sf.__ops
        return type(ops).___assoc_bin_op___(ops, lhs, rhs)

    ##################################
    ##################################
    @overridable_default_method
    @override
    def ___careless_check_main_obj___(sf, x, /):
        'a -> (None|raise) #see:careless_check_main_obj'
        ops = sf.__ops
        return type(ops).___careless_check_main_obj___(ops, x)

    #]'''
    #override_block]


#end of class WrapperMeasurableOps(WrapperMonoidOps, IMeasurableOps):
class MeasurableOps__measure_is_echo(WrapperMonoidOps, IMeasurableOps__measure_is_echo):pass


























def _mk_reversed_ops(BaseOps, ReversedOps, attr2get_original_ops, ops, /):
    #used by external mk_ReversedFingerTreeOps/class ReversedFingerTreeOps
    #   must export!!!
    assert issubclass(ReversedOps, BaseOps)
    assert isinstance(ops, BaseOps)
    assert hasattr(ReversedOps, attr2get_original_ops)

    if type(ops) is ReversedOps:
        reversed_ops = ops
        r = getattr(reversed_ops, attr2get_original_ops)()
    else:
        r = ReversedOps(ops)
    return r
def mk_ReversedMeasurableOps(measurable_ops, /):
    if measurable_ops.is_assoc_bin_op_commutable():
        return measurable_ops
    BaseOps = IMeasurableOps
    ReversedOps = ReversedMeasurableOps
    attr2get_original_ops = 'get_original_measurable_ops'
    ops = measurable_ops
    return _mk_reversed_ops(BaseOps, ReversedOps, attr2get_original_ops, ops)
def mk_ReversedMonoidOps(monoid_ops, /):
    if monoid_ops.is_assoc_bin_op_commutable():
        return monoid_ops
    BaseOps = IMonoidOps
    ReversedOps = ReversedMonoidOps
    attr2get_original_ops = 'get_original_monoid_ops'
    ops = monoid_ops
    return _mk_reversed_ops(BaseOps, ReversedOps, attr2get_original_ops, ops)
def mk_ReversedAssocBinaryOps(assoc_bin_ops, /):
    if assoc_bin_ops.is_assoc_bin_op_commutable():
        return assoc_bin_ops
    BaseOps = IAssocBinaryOps
    ReversedOps = ReversedAssocBinaryOps
    attr2get_original_ops = 'get_original_assoc_bin_ops'
    ops = assoc_bin_ops
    return _mk_reversed_ops(BaseOps, ReversedOps, attr2get_original_ops, ops)




class ReversedAssocBinaryOps(WrapperOps4OneMainObjType, IAssocBinaryOps):
    def __init__(sf, assoc_bin_ops, /):
        check_instance(IAssocBinaryOps, assoc_bin_ops)
        super().__init__(assoc_bin_ops)
        if type(sf.__ops) is __class__: raise TypeError
        if sf.__ops.is_assoc_bin_op_commutable(): raise ValueError

    @property
    def __ops(sf, /):
        return sf.get_original_ops4one_main_obj()

    def get_original_assoc_bin_ops(sf, /):
        '-> (assoc_bin_ops::IAssocBinaryOps)'
        return sf.__ops

    @override
    def ___is_assoc_bin_op_commutable___(sf, /):
        '-> (commutable::bool) #see:is_assoc_bin_op_commutable'
        return False
    @override
    def ___assoc_bin_op___(sf, lhs, rhs, /):
        'a -> a -> a # (a*b)*c === a*(b*c) #see:assoc_bin_op'
        return type(sf.__ops).___assoc_bin_op___(sf.__ops, rhs, lhs)
#end of class ReversedAssocBinaryOps(IAssocBinaryOps):
class ReversedMonoidOps(ReversedAssocBinaryOps, IMonoidOps):
    def __init__(sf, monoid_ops, /):
        check_instance(IMonoidOps, monoid_ops)
        super().__init__(monoid_ops)
        if type(sf.__ops) is __class__: raise TypeError
    @property
    def __ops(sf, /):
        return sf.get_original_assoc_bin_ops()
    def get_original_monoid_ops(sf, /):
        '-> (monoid_ops::IMonoidOps)'
        return sf.__ops


    @override
    def ___get_monoid_identity___(sf, /):
        '-> 1 # 1*a === a*1 === a::monoid_obj #see:get_monoid_identity'
        return sf.__ops.get_monoid_identity()
#end of class ReversedMonoidOps(ReversedAssocBinaryOps, IMonoidOps):
class ReversedMeasurableOps(ReversedMonoidOps, IMeasurableOps):
    def __init__(sf, measurable_ops, /):
        check_instance(IMeasurableOps, measurable_ops)
        #sf.__ops = measurable_ops
        #if type(sf.__ops) is __class__: raise TypeError
        sf.__rops4r = mk_ReversedMonoidOps(measurable_ops.get_monoid_ops4measured_result())
        super().__init__(measurable_ops)
        if type(sf.__ops) is __class__: raise TypeError
    @property
    def __ops(sf, /):
        return sf.get_original_monoid_ops()
    def get_original_measurable_ops(sf, /):
        return sf.__ops

    @override
    def ___get_monoid_ops4measured_result___(measurable_ops, /):
        '-> monoid_ops<measured_result>::IMonoidOps #see:get_monoid_ops4measured_result'
        sf = measurable_ops
        return sf.__rops4r
    @override
    def ___measure___(measurable_ops, measurable_obj, /):
        'measurable_obj -> (measured_result::monoid_obj) #see:measure'
        sf = measurable_ops
        return sf.__ops.measure(measurable_obj)
#end of class ReversedMeasurableOps(ReversedMonoidOps, IMeasurableOps):





















class MonoidOps4size(IMonoidOps__commutable):
    @override
    def ___careless_check_main_obj___(sf, x, /):
        'a -> (None|raise) #see:careless_check_main_obj'
        check_uint(x)

    @override
    def ___assoc_bin_op___(sf, lhs, rhs, /):
        'a -> a -> a # (a*b)*c === a*(b*c) #see:assoc_bin_op'
        return lhs + rhs

    @override
    def ___get_monoid_identity___(sf, /):
        '-> 1 # 1*a === a*1 === a::monoid_obj #see:get_monoid_identity'
        return 0
class TheMonoidOps4size(MonoidOps4size, ISingleton):pass
the_monoid_ops4size = TheMonoidOps4size()
assert the_monoid_ops4size is TheMonoidOps4size()
class MeasurableOps4size2size(MonoidOps4size, IMeasurableOps__measure_is_echo):pass
class TheMeasurableOps4size2size(MeasurableOps4size2size, ISingleton):pass
the_measurable_ops4size2size = TheMeasurableOps4size2size()
assert the_measurable_ops4size2size is TheMeasurableOps4size2size()

class IMonoidOps4max(IMonoidOps__commutable, ITotalOrderingOps__with_min_BOTTOM):
    @override
    def ___get_monoid_identity___(sf, /):
        '-> 1 # 1*a === a*1 === a::monoid_obj #see:get_monoid_identity'
        return sf.get_min_BOTTOM()
    @override
    def ___assoc_bin_op___(sf, lhs, rhs, /):
        'a -> a -> a # (a*b)*c === a*(b*c) #see:assoc_bin_op'
        return sf.max(lhs, rhs)

class IMonoidOps4max__default_total_ordering_ops(IMonoidOps4max, ITotalOrderingOps__default_total_ordering__with_min_BOTTOM):pass

class MonoidOps4max__imay(TotalOrderingOps__imay, IMonoidOps4max__default_total_ordering_ops):pass
class MonoidOps4max__uint(TotalOrderingOps__uint, IMonoidOps4max__default_total_ordering_ops):pass
class MonoidOps4max__tmay_pyobj(Mixin__Ops4OneMainObjType__main_obj_is_tmay_pyobj, IMonoidOps4max__default_total_ordering_ops):
    @override
    def ___get_min_BOTTOM___(sf, /):
        '-> (BOTTOM::main_obj) #the min main_obj #[BOTTOM <= any main_obj] #see:get_min_BOTTOM'
        return ()

class TheMonoidOps4max__imay(MonoidOps4max__imay, ISingleton):pass
class TheMonoidOps4max__uint(MonoidOps4max__uint, ISingleton):pass
class TheMonoidOps4max__tmay_pyobj(MonoidOps4max__tmay_pyobj, ISingleton):pass
the_monoid_ops4max__imay = TheMonoidOps4max__imay()
assert the_monoid_ops4max__imay is TheMonoidOps4max__imay()

the_monoid_ops4max__uint = TheMonoidOps4max__uint()
assert the_monoid_ops4max__uint is TheMonoidOps4max__uint()

the_monoid_ops4max__tmay_pyobj = TheMonoidOps4max__tmay_pyobj()
assert the_monoid_ops4max__tmay_pyobj is TheMonoidOps4max__tmay_pyobj()

r'''TODO
class MonoidOps4max__nmay_pyobj(IMonoidOps4max__default_total_ordering_ops, ISingleton):
class MonoidOps4max__tmay_var(IMonoidOps4max):
    def __init__(sf, arg_max_monoid_ops:IMonoidOps4max, /):
class MonoidOps4max__nmay_var(IMonoidOps4max):
    def __init__(sf, arg_max_monoid_ops:IMonoidOps4max, /):
#'''


def _do_nothing(x, /):pass
class MonoidOps4max__funcs(IMonoidOps4max):
    def __init__(sf, key_total_ordering_ops__with_min:ITotalOrderingOps__with_min_BOTTOM, /,*, tmay_min_BOTTOM4main_obj=(), key=None, careless_check_main_obj=None):
        'ITotalOrderingOps__with_min_BOTTOM<k> -> (tmay_min_BOTTOM4main_obj::tmay main_obj) -> (key::main_obj->k) -> (careless_check_main_obj::main_obj->(None|raise)) -> MonoidOps4max__funcs'
        if 0:
            r'''
            def __init__(sf, /,*, min, __lt__=None, key=None, careless_check_main_obj=None):
                if __lt__ is None:
                    __lt__ = operator.__lt__
                check_callable(__lt__)
                careless_check_main_obj(min)
                sf.__min = min
                sf.__lt = __lt__
            #'''

        if key is None:
            key = echo
        if careless_check_main_obj is None:
            careless_check_main_obj = _do_nothing
        check_callable(careless_check_main_obj)

        check_callable(key)
        check_instance(ITotalOrderingOps__with_min_BOTTOM, key_total_ordering_ops__with_min)


        check_tmay(tmay_min_BOTTOM4main_obj)

        BOTTOM4key = key_total_ordering_ops__with_min.get_min_BOTTOM()
        if not tmay_min_BOTTOM4main_obj and key is not echo: raise TypeError('required BOTTOM4main_obj since key is not echo/None')
        elif not tmay_min_BOTTOM4main_obj:
            assert key is echo
            #key :: main_obj
            BOTTOM4main_obj = BOTTOM4key
        else:
            [BOTTOM4main_obj] = tmay_min_BOTTOM4main_obj
            careless_check_main_obj(BOTTOM4main_obj)
        BOTTOM4main_obj

        BOTTOM4key__from_main_obj = key(BOTTOM4main_obj)
        key_total_ordering_ops__with_min.careless_check_main_obj(BOTTOM4key__from_main_obj)
        if not key_total_ordering_ops__with_min.eq(BOTTOM4key__from_main_obj, BOTTOM4key): raise ValueError


        sf.__key = key
        sf.__key_ops = key_total_ordering_ops__with_min
        sf.__check = careless_check_main_obj
        sf.__BOTTOM = BOTTOM4main_obj

    @override
    def ___careless_check_main_obj___(sf, x, /):
        'a -> (None|raise) #see:careless_check_main_obj'
        sf.__check(x)
        if 1:
            #when input:key=None, careless_check_main_obj=None
            k = sf.__key(x)
            sf.__key_ops.careless_check_main_obj(k)

    @override
    def ___get_min_BOTTOM___(sf, /):
        '-> (BOTTOM::main_obj) #the min main_obj #[BOTTOM <= any main_obj] #see:get_min_BOTTOM'
        return sf.__BOTTOM
    @override
    def ___eq___(sf, lhs, rhs, /):
        '-> bool #see:eq'
        ops = sf.__key_ops
        key = sf.__key
        return ops.eq(key(lhs), key(rhs))
    @override
    def ___lt___(sf, lhs, rhs, /):
        '-> bool #see:lt'
        ops = sf.__key_ops
        key = sf.__key
        return ops.lt(key(lhs), key(rhs))
    @override
    def ___cmp___(sf, lhs, rhs, /):
        '-> [-1..+1] #see:cmp'
        ops = sf.__key_ops
        key = sf.__key
        return ops.cmp(key(lhs), key(rhs))
#end of class MonoidOps4max__funcs(IMonoidOps4max):


MonoidOps4max__funcs(the_total_ordering_ops__uint)








WrapperOps4OneMainObjType(the_total_ordering_ops__uint)
WrapperAssocBinaryOps(the_monoid_ops4size)
WrapperMonoidOps(the_monoid_ops4size)
WrapperMeasurableOps(the_measurable_ops4size2size)
MeasurableOps__measure_is_echo(the_monoid_ops4size)


#del ___end_mark_of_excluded_global_names__0___
#___end_mark_of_excluded_global_names__0___ = ...
class IDecomposableOps4OneMainObjType(IOps4OneMainObjType):
    def __getitem__(sf, key, /):
        return sf.lookup_ops4subobj_of_main_obj(key)
    @abstractmethod
    def ___lookup_ops4subobj_of_main_obj___(sf, key, /):
        '-> (ops4subobj_of_main_obj<key>::IOps4OneMainObjType) #see:lookup_ops4subobj_of_main_obj'
    @final_method
    def lookup_ops4subobj_of_main_obj(sf, key, /):
        '-> (ops4subobj<main_obj[key]>::IOps4OneMainObjType) #see:___lookup_ops4subobj_of_main_obj___'
        ops4subobj_at_key = type(sf).___lookup_ops4subobj_of_main_obj___(sf, key)
        check_instance(IOps4OneMainObjType, ops4subobj_at_key)
        ops_base_cls = type(sf).get_ops_base_cls4all_opss4subobj_of_main_obj()
        check_instance(ops_base_cls, ops4subobj_at_key)
        return ops4subobj_at_key
    @classmethod
    @abstractmethod
    def ___get_ops_base_cls4all_opss4subobj_of_main_obj___(cls, /):
        return IOps4OneMainObjType
    @classmethod
    @final_method
    def get_ops_base_cls4all_opss4subobj_of_main_obj(cls, /):
        ops_base_cls = cls.___get_ops_base_cls4all_opss4subobj_of_main_obj___()
        check_subclass(IOps4OneMainObjType, ops_base_cls)
        return ops_base_cls
class IDecomposableAssocBinaryOps(IAssocBinaryOps, IDecomposableOps4OneMainObjType):pass
class IDecomposableMonoidOps(IMonoidOps, IDecomposableAssocBinaryOps):pass

class IDecomposableOps4OneMainObjType__subops_is_IOps4OneMainObjType(IDecomposableOps4OneMainObjType):
    @classmethod
    @override
    def ___get_ops_base_cls4all_opss4subobj_of_main_obj___(cls, /):
        return IOps4OneMainObjType
class IDecomposableAssocBinaryOps__subops_is_IAssocBinaryOps(IDecomposableAssocBinaryOps):
    @classmethod
    @override
    def ___get_ops_base_cls4all_opss4subobj_of_main_obj___(cls, /):
        return IAssocBinaryOps
class IDecomposableMonoidOps__subops_is_IMonoidOps(IDecomposableMonoidOps):
    @classmethod
    @override
    def ___get_ops_base_cls4all_opss4subobj_of_main_obj___(cls, /):
        return IMonoidOps
#___begin_mark_of_excluded_global_names__1___ = ...



class IArgedOps4OneMainObjType(IOps4OneMainObjType):
    def __new__(cls, /, *args):
        cls.___check4args4ops4one_main_obj___(*args)
        sf = super(__class__, cls).__new__(cls)
        if type(sf) is cls:
            sf.__args = args
        return sf

    @classmethod
    @abstractmethod
    def ___check4args4ops4one_main_obj___(cls, /, *args):
        pass
    @property
    def args4ops4one_main_obj(sf, /):
        return sf.__args


class IArgedDecomposableOps4OneMainObjType(IArgedOps4OneMainObjType, IDecomposableOps4OneMainObjType):pass
class IDecomposableOps4OneMainObjType4tuple_as_point(IArgedDecomposableOps4OneMainObjType):
    @final_method
    @override
    def ___lookup_ops4subobj_of_main_obj___(sf, key, /):
        '-> (ops4subobj_of_main_obj<key>::IOps4OneMainObjType) #see:lookup_ops4subobj_of_main_obj'
        if not type(key) is int: raise LookupError
        return sf.idx2value_ops4one_main_obj[key]
    @classmethod
    @final_method
    @override
    def ___get_ops_base_cls4all_opss4subobj_of_main_obj___(cls, /):
        ops_base_cls = cls.___get_ops_base_class_of_ops4one_main_obj4point_elements___()
        return ops_base_cls

    @classmethod
    @abstractmethod
    def ___get_ops_base_class_of_ops4one_main_obj4point_elements___(cls, /):
        return IOps4OneMainObjType
    @classmethod
    @final_method
    def get_ops_base_class_of_ops4one_main_obj4point_elements(cls, /):
        ops_base_cls = cls.___get_ops_base_class_of_ops4one_main_obj4point_elements___()
        check_subclass(IOps4OneMainObjType, ops_base_cls)
        return ops_base_cls

    def __init__(sf, idx2value_ops4one_main_obj, /):
        pass

    @property
    @final_method
    @def_new_method
    def idx2value_ops4one_main_obj(sf, /):
        [idx2value_ops4one_main_obj] = sf.args4ops4one_main_obj
        return idx2value_ops4one_main_obj

    @classmethod
    @final_method
    @override
    def ___check4args4ops4one_main_obj___(cls, idx2value_ops4one_main_obj, /):
        check_tuple(idx2value_ops4one_main_obj)
        ops_base_cls = cls.get_ops_base_class_of_ops4one_main_obj4point_elements()
        check_instance_all(ops_base_cls, idx2value_ops4one_main_obj)


    @final_method
    @override
    def ___careless_check_main_obj___(sf, x, /):
        'a -> (None|raise) #see:careless_check_main_obj'
        opss = sf.idx2value_ops4one_main_obj
        check_tuple(x, sz=len(opss))
        if 0:
            for ops, z in zip(opss, x): ops.careless_check_main_obj(z)

class DecomposableOps4OneMainObjType4tuple_as_point(IDecomposableOps4OneMainObjType4tuple_as_point):
    @classmethod
    @final_method
    @override
    def ___get_ops_base_class_of_ops4one_main_obj4point_elements___(cls, /):
        return IOps4OneMainObjType

class IDecomposableAssocBinaryOps4tuple_as_point(IDecomposableOps4OneMainObjType4tuple_as_point, IAssocBinaryOps):
    def __init__(sf, idx2value_assoc_bin_ops, /):
        super().__init__(idx2value_assoc_bin_ops)
        opss = sf.idx2value_ops4one_main_obj
        sf.__commutable = all(ops.is_assoc_bin_op_commutable() for ops in opss)


    @final_method
    @override
    def ___is_assoc_bin_op_commutable___(sf, /):
        '-> (commutable::bool) #see:is_assoc_bin_op_commutable'
        return sf.__commutable

    @final_method
    @override
    def ___assoc_bin_op___(sf, lhs, rhs, /):
        'a -> a -> a # (a*b)*c === a*(b*c) #see:assoc_bin_op'
        opss = sf.idx2value_ops4one_main_obj
        return tuple(ops.assoc_bin_op(x,y) for ops, x,y in zip(opss, lhs, rhs))

class DecomposableAssocBinaryOps4tuple_as_point(IDecomposableAssocBinaryOps4tuple_as_point):
    @classmethod
    @final_method
    @override
    def ___get_ops_base_class_of_ops4one_main_obj4point_elements___(cls, /):
        return IAssocBinaryOps





class IDecomposableMonoidOps4tuple_as_point(IDecomposableAssocBinaryOps4tuple_as_point, IMonoidOps):
    r'''
    see:
        MonoidOps4tuple_as_mapping.__doc__ #__doc__MonoidOps4tuple_as_mapping
    #'''
    def __init__(sf, idx2value_monoid_ops, /):
        super().__init__(idx2value_monoid_ops)
        opss = sf.idx2value_ops4one_main_obj
        sf.__identity = tuple(ops.get_monoid_identity() for ops in opss)

    @final_method
    @override
    def ___get_monoid_identity___(sf, /):
        '-> 1 # 1*a === a*1 === a::monoid_obj #see:get_monoid_identity'
        return sf.__identity

class DecomposableMonoidOps4tuple_as_point(IDecomposableMonoidOps4tuple_as_point):
    @classmethod
    @final_method
    @override
    def ___get_ops_base_class_of_ops4one_main_obj4point_elements___(cls, /):
        return IMonoidOps

_empty_tuple = ()
_empty_FrozenDict = mk_FrozenDict()
class MonoidOps4tuple_as_array(IMonoidOps):
    r'''
    value::py_obj #not requires any ops

    see:
        MonoidOps4tuple_as_mapping.__doc__ #__doc__MonoidOps4tuple_as_mapping
    #'''

    ##################################
    ##################################
    @final_method
    @override
    def ___get_monoid_identity___(sf, /):
        '-> 1 # 1*a === a*1 === a::monoid_obj #see:get_monoid_identity'
        return _empty_tuple

    ##################################
    ##################################
    @final_method
    @override
    def ___is_assoc_bin_op_commutable___(sf, /):
        '-> (commutable::bool) #see:is_assoc_bin_op_commutable'
        return False

    @final_method
    @override
    def ___assoc_bin_op___(sf, lhs, rhs, /):
        'a -> a -> a # (a*b)*c === a*(b*c) #see:assoc_bin_op'
        return lhs + rhs

    ##################################
    ##################################
    @final_method
    @override
    def ___careless_check_main_obj___(sf, x, /):
        'a -> (None|raise) #see:careless_check_main_obj'
        check_tuple(x)
#end of class MonoidOps4tuple_as_array(IMonoidOps):
class TheMonoidOps4tuple_as_array(MonoidOps4tuple_as_array, ISingleton):pass
the_monoid_ops4tuple_as_array = TheMonoidOps4tuple_as_array()
assert the_monoid_ops4tuple_as_array is TheMonoidOps4tuple_as_array()


class IOps4OneMainObjType__main_obj_is_mapping(IOps4OneMainObjType):
    'IDecomposableOps4OneMainObjType4lookupable vs IOps4OneMainObjType__main_obj_is_mapping'
    @abstractmethod
    def ___get_the_mapping_type4main_obj___(sf, /):
        '-> (type(main_obj) <: Mapping) #see:get_the_mapping_type4main_obj'
    def get_the_mapping_type4main_obj(sf, /):
        '-> (type(main_obj) <: Mapping) #see:___get_the_mapping_type4main_obj___'
        mapping_cls = type(sf).___get_the_mapping_type4main_obj___(sf)
        check_subclass(Mapping, mapping_cls)
        return mapping_cls
    @abstractmethod
    def ___mk_main_obj_from_mapping_or_pairs___(sf, mapping_or_pairs=(), /):
        '(mapping|pairs) -> (main_obj :: Mapping) #see:mk_main_obj_from_mapping_or_pairs'
    def mk_main_obj_from_mapping_or_pairs(sf, mapping_or_pairs=(), /):
        '(mapping|pairs) -> (main_obj :: Mapping) #see:___mk_main_obj_from_mapping_or_pairs___'
        check_nmay(check_iterable, mapping_or_pairs)
        main_obj = type(sf).___mk_main_obj_from_mapping_or_pairs___(sf, mapping_or_pairs)
        mapping_cls = sf.get_the_mapping_type4main_obj()
        check_type_is(mapping_cls, main_obj)
        sf.careless_check_main_obj(main_obj)
        return main_obj

class IOps4OneMainObjType__main_obj_is_FrozenDict(IOps4OneMainObjType__main_obj_is_mapping):
    @final_method
    @override
    def ___get_the_mapping_type4main_obj___(sf, /):
        '-> (type(main_obj) <: Mapping) #see:get_the_mapping_type4main_obj'
        return FrozenDict
    @final_method
    @override
    def ___mk_main_obj_from_mapping_or_pairs___(sf, mapping_or_pairs=(), /):
        '(mapping|pairs) -> (main_obj :: Mapping) #see:mk_main_obj_from_mapping_or_pairs'
        d = mk_FrozenDict(mapping_or_pairs)
        if not d:
            d = _empty_FrozenDict
        return d



class IDecomposableOps4OneMainObjType4lookupable(IArgedDecomposableOps4OneMainObjType):
    r'''IDecomposableOps4OneMainObjType4lookupable vs IOps4OneMainObjType__main_obj_is_mapping
    IDecomposableOps4OneMainObjType4lookupable
        lookupable/mapping/seq ~ __getitem__ lookup only
    IOps4OneMainObjType__main_obj_is_mapping
        mapping :: Mapping
    '''
    @final_method
    @override
    def ___lookup_ops4subobj_of_main_obj___(sf, key, /):
        '-> (ops4subobj_of_main_obj<key>::IOps4OneMainObjType) #see:lookup_ops4subobj_of_main_obj'
        hash(key)
        return sf.lookupable_value_ops4one_main_obj
    @classmethod
    @final_method
    @override
    def ___get_ops_base_cls4all_opss4subobj_of_main_obj___(cls, /):
        ops_base_cls = cls.___get_ops_base_class_of_ops4one_main_obj4lookupable_value___()
        return ops_base_cls

    @classmethod
    @abstractmethod
    def ___get_ops_base_class_of_ops4one_main_obj4lookupable_value___(cls, /):
        return IOps4OneMainObjType
    @classmethod
    @final_method
    def get_ops_base_class_of_ops4one_main_obj4lookupable_value(cls, /):
        ops_base_cls = cls.___get_ops_base_class_of_ops4one_main_obj4lookupable_value___()
        check_subclass(IOps4OneMainObjType, ops_base_cls)
        return ops_base_cls

    def __init__(sf, lookupable_value_ops4one_main_obj, /):
        pass

    @property
    @final_method
    @def_new_method
    def lookupable_value_ops4one_main_obj(sf, /):
        [lookupable_value_ops4one_main_obj] = sf.args4ops4one_main_obj
        return lookupable_value_ops4one_main_obj

    @classmethod
    @final_method
    @override
    def ___check4args4ops4one_main_obj___(cls, lookupable_value_ops4one_main_obj, /):
        ops_base_cls = cls.get_ops_base_class_of_ops4one_main_obj4lookupable_value()
        check_instance(ops_base_cls, lookupable_value_ops4one_main_obj)


#end of class IDecomposableOps4OneMainObjType4lookupable(IArgedDecomposableOps4OneMainObjType):

class IDecomposableAssocBinaryOps4lookupable(IDecomposableOps4OneMainObjType4lookupable, IAssocBinaryOps):
    def __init__(sf, lookupable_value_assoc_bin_ops, /):
        super().__init__(lookupable_value_assoc_bin_ops)
        ops = sf.lookupable_value_ops4one_main_obj
        sf.__commutable = ops.is_assoc_bin_op_commutable()


    @final_method
    @override
    def ___is_assoc_bin_op_commutable___(sf, /):
        '-> (commutable::bool) #see:is_assoc_bin_op_commutable'
        return sf.__commutable

class IDecomposableMonoidOps4lookupable(IDecomposableAssocBinaryOps4lookupable, IMonoidOps):
    r'''
    see:
        MonoidOps4tuple_as_lookupable.__doc__ #__doc__MonoidOps4tuple_as_lookupable
    #'''
    def __init__(sf, lookupable_value_monoid_ops, /):
        super().__init__(lookupable_value_monoid_ops)




class IDecomposableOps4OneMainObjType4tuple_as_lookupable(IDecomposableOps4OneMainObjType4lookupable):
    @final_method
    @override
    def ___careless_check_main_obj___(sf, x, /):
        'a -> (None|raise) #see:careless_check_main_obj'
        check_tuple(x)
        if 0:
            ops = sf.lookupable_value_ops4one_main_obj
            for z in x: ops.careless_check_main_obj(z)
#end of class IDecomposableOps4OneMainObjType4tuple_as_lookupable(IDecomposableOps4OneMainObjType4lookupable):

class DecomposableOps4OneMainObjType4tuple_as_lookupable(IDecomposableOps4OneMainObjType4tuple_as_lookupable):
    @classmethod
    @final_method
    @override
    def ___get_ops_base_class_of_ops4one_main_obj4lookupable_value___(cls, /):
        return IOps4OneMainObjType

class IDecomposableAssocBinaryOps4tuple_as_lookupable(IDecomposableOps4OneMainObjType4tuple_as_lookupable, IDecomposableAssocBinaryOps4lookupable):
    @final_method
    @override
    def ___assoc_bin_op___(sf, lhs, rhs, /):
        'a -> a -> a # (a*b)*c === a*(b*c) #see:assoc_bin_op'
        ops = sf.lookupable_value_ops4one_main_obj
        prefix = tuple(map(ops.assoc_bin_op, lhs, rhs))
        n = len(lhs) - len(rhs)
        if n == 0:
            suffix = ()
        elif n > 0:
            suffix = lhs[-n:]
        else:
            suffix = rhs[n:]
        return prefix + suffix

class DecomposableAssocBinaryOps4tuple_as_lookupable(IDecomposableAssocBinaryOps4tuple_as_lookupable):
    @classmethod
    @final_method
    @override
    def ___get_ops_base_class_of_ops4one_main_obj4lookupable_value___(cls, /):
        return IAssocBinaryOps





class IDecomposableMonoidOps4tuple_as_lookupable(IDecomposableAssocBinaryOps4tuple_as_lookupable, IDecomposableMonoidOps4lookupable):
    @final_method
    @override
    def ___get_monoid_identity___(sf, /):
        '-> 1 # 1*a === a*1 === a::monoid_obj #see:get_monoid_identity'
        return _empty_tuple


class DecomposableMonoidOps4tuple_as_lookupable(IDecomposableMonoidOps4tuple_as_lookupable):
    r'''
    assoc_bin_ops<value>

    define MonoidOps4tuple_as_lookupable.__doc__ #__doc__MonoidOps4tuple_as_lookupable
        see also:
            MonoidOps4FrozenDict_as_union_of_cased_records.__doc__ #__doc__MonoidOps4FrozenDict_as_union_of_cased_records


    MonoidOps4tuple_as_default_lookupable vs MonoidOps4tuple_as_lookupable
        default_lookupable:
            __missing__ ==>> monoid_identity
            requires monoid_ops<value>
        lookupable:
            only requires assoc_bin_ops<value>
    MonoidOps4tuple_as_array vs MonoidOps4tuple_as_lookupable
        array:
            value::py_obj #not requires any ops
            ___assoc_bin_op___ = tuple.__add__
        lookupable:
            requires assoc_bin_ops<value>
            ___assoc_bin_op___ = @key/(i.e.idx): value_ops.___assoc_bin_op___(...)

    DecomposableMonoidOps4tuple_as_point vs MonoidOps4tuple_as_lookupable
        point:
            len fixed
            requires @idx:monoid_ops<value<idx>>
        lookupable:
            len not fixed
            requires only single assoc_bin_ops<value> for arbitrary idx
    #'''
    @classmethod
    @final_method
    @override
    def ___get_ops_base_class_of_ops4one_main_obj4lookupable_value___(cls, /):
        return IAssocBinaryOps
        return IMonoidOps #neednot!

#end of class DecomposableMonoidOps4tuple_as_lookupable(IDecomposableMonoidOps4tuple_as_lookupable):




FrozenDict
class IDecomposableOps4OneMainObjType4FrozenDict_as_lookupable(IDecomposableOps4OneMainObjType4lookupable):
    @final_method
    @override
    def ___careless_check_main_obj___(sf, x, /):
        'a -> (None|raise) #see:careless_check_main_obj'
        check_type_is(FrozenDict, x)
        if 0:
            ops = sf.lookupable_value_ops4one_main_obj
            for z in x.values(): ops.careless_check_main_obj(z)
#end of class IDecomposableOps4OneMainObjType4FrozenDict_as_lookupable(IDecomposableOps4OneMainObjType4lookupable):

class DecomposableOps4OneMainObjType4FrozenDict_as_lookupable(IDecomposableOps4OneMainObjType4FrozenDict_as_lookupable):
    @classmethod
    @final_method
    @override
    def ___get_ops_base_class_of_ops4one_main_obj4lookupable_value___(cls, /):
        return IOps4OneMainObjType

class IDecomposableAssocBinaryOps4FrozenDict_as_lookupable(IDecomposableOps4OneMainObjType4FrozenDict_as_lookupable, IDecomposableAssocBinaryOps4lookupable):
    @final_method
    @override
    def ___assoc_bin_op___(sf, lhs, rhs, /):
        'a -> a -> a # (a*b)*c === a*(b*c) #see:assoc_bin_op'
        ops = sf.lookupable_value_ops4one_main_obj
        keys = set(lhs.keys()) | set(rhs.keys())
        def f(k):
            if k in lhs:
                u = lhs[k]
                if k in rhs:
                    v = rhs[k]
                    r = ops.assoc_bin_op(u, v)
                else:
                    r = u
            else:
                r = rhs[k]
            return r
        return mk_FrozenDict((k, f(k)) for k in keys)

class DecomposableAssocBinaryOps4FrozenDict_as_lookupable(IDecomposableAssocBinaryOps4FrozenDict_as_lookupable):
    @classmethod
    @final_method
    @override
    def ___get_ops_base_class_of_ops4one_main_obj4lookupable_value___(cls, /):
        return IAssocBinaryOps





class IDecomposableMonoidOps4FrozenDict_as_lookupable(IDecomposableAssocBinaryOps4FrozenDict_as_lookupable, IDecomposableMonoidOps4lookupable):
    @final_method
    @override
    def ___get_monoid_identity___(sf, /):
        '-> 1 # 1*a === a*1 === a::monoid_obj #see:get_monoid_identity'
        return _empty_FrozenDict


class DecomposableMonoidOps4FrozenDict_as_lookupable(IDecomposableMonoidOps4FrozenDict_as_lookupable):
    r'''
    assoc_bin_ops<value>

    see:
        MonoidOps4tuple_as_lookupable.__doc__ #__doc__MonoidOps4tuple_as_lookupable
    #'''
    @classmethod
    @final_method
    @override
    def ___get_ops_base_class_of_ops4one_main_obj4lookupable_value___(cls, /):
        return IAssocBinaryOps
        return IMonoidOps #neednot!

#end of class DecomposableMonoidOps4FrozenDict_as_lookupable(IDecomposableMonoidOps4FrozenDict_as_lookupable):

class DecomposableMonoidOps4tuple_as_default_lookupable(IDecomposableMonoidOps4FrozenDict_as_lookupable):
    r'''
    see:
        MonoidOps4tuple_as_lookupable.__doc__ #__doc__MonoidOps4tuple_as_lookupable
    #'''
    @classmethod
    @final_method
    @override
    def ___get_ops_base_class_of_ops4one_main_obj4lookupable_value___(cls, /):
        #return IAssocBinaryOps
        return IMonoidOps # monoid_identity for __missing__

class MonoidOps4FrozenDict_as_default_lookupable(MonoidOps4FrozenDict_as_lookupable):
    r'''
    see:
        MonoidOps4tuple_as_lookupable.__doc__ #__doc__MonoidOps4tuple_as_lookupable
    #'''
    @classmethod
    @final_method
    @override
    def ___get_ops_base_class_of_ops4one_main_obj4lookupable_value___(cls, /):
        #return IAssocBinaryOps
        return IMonoidOps # monoid_identity for __missing__







check_union_of_cased_tuples
class __xxx_cannot_impl_but_doc_is_useful___MonoidOps4union_of_cased_tuples(IMonoidOps):
    r'''
    see:
        MonoidOps4FrozenDict_as_union_of_cased_records.__doc__ #__doc__MonoidOps4FrozenDict_as_union_of_cased_records
        seed.helper.check.checkers.check_union_of_cased_tuples
    #'''




#cased_tuple
check_cased_tuple
DecomposableMonoidOps4tuple_as_point
class IDecomposableOps4OneMainObjType4cased_tuple(IArgedDecomposableOps4OneMainObjType):
    r'''
    DecomposableMonoidOps4tuple_as_point, MonoidOps4cased_tuple
        may used as auto_info@finger_tree_ops
    #'''
    @final_method
    @override
    def ___lookup_ops4subobj_of_main_obj___(sf, key, /):
        '-> (ops4subobj_of_main_obj<key>::IOps4OneMainObjType) #see:lookup_ops4subobj_of_main_obj'
        if not type(key) is int: raise LookupError
        ops4subobj_at_key = sf.cased_idx2value_ops4one_main_obj[key]
        if type(ops4subobj_at_key) is str: raise LookupError
        return ops4subobj_at_key

    @classmethod
    @final_method
    @override
    def ___get_ops_base_cls4all_opss4subobj_of_main_obj___(cls, /):
        ops_base_cls = cls.___get_ops_base_class_of_ops4one_main_obj4cased_tuple_elements___()
        return ops_base_cls

    @classmethod
    @abstractmethod
    def ___get_ops_base_class_of_ops4one_main_obj4cased_tuple_elements___(cls, /):
        return IOps4OneMainObjType
    @classmethod
    @final_method
    def get_ops_base_class_of_ops4one_main_obj4cased_tuple_elements(cls, /):
        ops_base_cls = cls.___get_ops_base_class_of_ops4one_main_obj4cased_tuple_elements___()
        check_subclass(IOps4OneMainObjType, ops_base_cls)
        return ops_base_cls

    def __init__(sf, cased_idx2value_ops4one_main_obj, /):
        pass

    @property
    @final_method
    @def_new_method
    def cased_idx2value_ops4one_main_obj(sf, /):
        [cased_idx2value_ops4one_main_obj] = sf.args4ops4one_main_obj
        return cased_idx2value_ops4one_main_obj

    @classmethod
    @final_method
    @override
    def ___check4args4ops4one_main_obj___(cls, cased_idx2value_ops4one_main_obj, /):
        #check_cased_tuple(cased_idx2value_ops4one_main_obj)
        cased_idx2ops = cased_idx2value_ops4one_main_obj
        check_cased_tuple__free(cased_idx2ops)

        ops_base_cls = cls.get_ops_base_class_of_ops4one_main_obj4cased_tuple_elements()
        check_instance_all(ops_base_cls, cased_idx2ops[1:])


    @final_method
    @override
    def ___careless_check_main_obj___(sf, x, /):
        'a -> (None|raise) #see:careless_check_main_obj'
        cased_opss = sf.cased_idx2value_ops4one_main_obj
        check_cased_tuple(cased_opss[0], len(cased_opss), x)
        if 0:
            for ops, z in zip(cased_opss[1:], x[1:]): ops.careless_check_main_obj(z)

class DecomposableOps4OneMainObjType4cased_tuple(IDecomposableOps4OneMainObjType4cased_tuple):
    @classmethod
    @final_method
    @override
    def ___get_ops_base_class_of_ops4one_main_obj4cased_tuple_elements___(cls, /):
        return IOps4OneMainObjType

class IDecomposableAssocBinaryOps4cased_tuple(IDecomposableOps4OneMainObjType4cased_tuple, IAssocBinaryOps):
    def __init__(sf, cased_idx2value_assoc_bin_ops, /):
        super().__init__(cased_idx2value_assoc_bin_ops)
        cased_opss = sf.cased_idx2value_ops4one_main_obj
        sf.__commutable = all(ops.is_assoc_bin_op_commutable() for ops in cased_opss[1:])


    @final_method
    @override
    def ___is_assoc_bin_op_commutable___(sf, /):
        '-> (commutable::bool) #see:is_assoc_bin_op_commutable'
        return sf.__commutable

    @final_method
    @override
    def ___assoc_bin_op___(sf, lhs, rhs, /):
        'a -> a -> a # (a*b)*c === a*(b*c) #see:assoc_bin_op'
        cased_opss = sf.cased_idx2value_ops4one_main_obj
        it = zip(cased_opss, lhs, rhs)
        for case_name, _, _ in it:
            break
        else:
            raise logic-err
        return (case_name, *(ops.assoc_bin_op(x,y) for ops, x,y in it))

class DecomposableAssocBinaryOps4cased_tuple(IDecomposableAssocBinaryOps4cased_tuple):
    @classmethod
    @final_method
    @override
    def ___get_ops_base_class_of_ops4one_main_obj4cased_tuple_elements___(cls, /):
        return IAssocBinaryOps





class IDecomposableMonoidOps4cased_tuple(IDecomposableAssocBinaryOps4cased_tuple, IMonoidOps):
    r'''
    see:
        MonoidOps4tuple_as_lookupable.__doc__ #__doc__MonoidOps4tuple_as_lookupable
    #'''
    def __init__(sf, cased_idx2value_monoid_ops, /):
        super().__init__(cased_idx2value_monoid_ops)
        cased_opss = sf.cased_idx2value_ops4one_main_obj
        sf.__identity = (cased_opss[0], *(ops.get_monoid_identity() for ops in cased_opss[1:]))

    @final_method
    @override
    def ___get_monoid_identity___(sf, /):
        '-> 1 # 1*a === a*1 === a::monoid_obj #see:get_monoid_identity'
        return sf.__identity

check_cased_tuple
class DecomposableMonoidOps4cased_tuple(IDecomposableMonoidOps4cased_tuple):
    r'''
    see:
        MonoidOps4FrozenDict_as_union_of_cased_records.__doc__ #__doc__MonoidOps4FrozenDict_as_union_of_cased_records
        seed.helper.check.checkers.check_cased_tuple
    #'''
    @classmethod
    @final_method
    @override
    def ___get_ops_base_class_of_ops4one_main_obj4cased_tuple_elements___(cls, /):
        return IMonoidOps














check_FrozenDict_as_record
MonoidOps4FrozenDict_as_lookupable

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

#class IDecomposableOps4OneMainObjType4tuple_as_point(IArgedDecomposableOps4OneMainObjType):
class IDecomposableOps4OneMainObjType4mapping_as_record(IArgedDecomposableOps4OneMainObjType, IOps4OneMainObjType__main_obj_is_mapping):
    'mapping_as_record vs tuple_as_point'
    @final_method
    @override
    def ___lookup_ops4subobj_of_main_obj___(sf, key, /):
        '-> (ops4subobj_of_main_obj<key>::IOps4OneMainObjType) #see:lookup_ops4subobj_of_main_obj'
        if not type(key) is str: raise LookupError
        return sf.attr2value_ops4one_main_obj[key]
    @classmethod
    @final_method
    @override
    def ___get_ops_base_cls4all_opss4subobj_of_main_obj___(cls, /):
        ops_base_cls = cls.___get_ops_base_class_of_ops4one_main_obj4record_elements___()
        return ops_base_cls

    @classmethod
    @abstractmethod
    def ___get_ops_base_class_of_ops4one_main_obj4record_elements___(cls, /):
        return IOps4OneMainObjType
    @classmethod
    @final_method
    def get_ops_base_class_of_ops4one_main_obj4record_elements(cls, /):
        ops_base_cls = cls.___get_ops_base_class_of_ops4one_main_obj4record_elements___()
        check_subclass(IOps4OneMainObjType, ops_base_cls)
        return ops_base_cls

    def __init__(sf, attr2value_ops4one_main_obj, /):
        pass

    @property
    @final_method
    @def_new_method
    def attr2value_ops4one_main_obj(sf, /):
        [attr2value_ops4one_main_obj] = sf.args4ops4one_main_obj
        return attr2value_ops4one_main_obj

    @classmethod
    @final_method
    @override
    def ___check4args4ops4one_main_obj___(cls, attr2value_ops4one_main_obj, /):
        check_mapping_as_record__free(attr2value_ops4one_main_obj)
        ops_base_cls = cls.get_ops_base_class_of_ops4one_main_obj4record_elements()
        check_instance_all(ops_base_cls, attr2value_ops4one_main_obj.values())


    @final_method
    @override
    def ___careless_check_main_obj___(sf, x, /):
        'a -> (None|raise) #see:careless_check_main_obj'
        attr2ops = sf.attr2value_ops4one_main_obj
        mapping_cls = sf.get_the_mapping_type4main_obj()
        check_mapping_as_record(set(attr2ops), x, cls=mapping_cls)
        if 0:
            for k, ops in attr2ops.items(): ops.careless_check_main_obj(x[k])
#end of class IDecomposableOps4OneMainObjType4mapping_as_record(IArgedDecomposableOps4OneMainObjType, IOps4OneMainObjType__main_obj_is_mapping):

class IDecomposableOps4OneMainObjType4FrozenDict_as_record(IOps4OneMainObjType__main_obj_is_FrozenDict, IDecomposableOps4OneMainObjType4mapping_as_record):pass
class DecomposableOps4OneMainObjType4FrozenDict_as_record(IDecomposableOps4OneMainObjType4FrozenDict_as_record):
    @classmethod
    @final_method
    @override
    def ___get_ops_base_class_of_ops4one_main_obj4record_elements___(cls, /):
        return IOps4OneMainObjType

class IDecomposableAssocBinaryOps4mapping_as_record(IDecomposableOps4OneMainObjType4mapping_as_record, IAssocBinaryOps):
    def __init__(sf, attr2value_assoc_bin_ops, /):
        super().__init__(attr2value_assoc_bin_ops)
        attr2ops = sf.attr2value_ops4one_main_obj
        sf.__commutable = all(ops.is_assoc_bin_op_commutable() for ops in attr2ops.values())


    @final_method
    @override
    def ___is_assoc_bin_op_commutable___(sf, /):
        '-> (commutable::bool) #see:is_assoc_bin_op_commutable'
        return sf.__commutable

    @final_method
    @override
    def ___assoc_bin_op___(sf, lhs, rhs, /):
        'a -> a -> a # (a*b)*c === a*(b*c) #see:assoc_bin_op'
        attr2ops = sf.attr2value_ops4one_main_obj
        mk = sf.mk_main_obj_from_mapping_or_pairs
        return mk((k, ops.assoc_bin_op(lhs[k], rhs[k])) for k, ops in attr2ops.items())

class IDecomposableAssocBinaryOps4FrozenDict_as_record(IOps4OneMainObjType__main_obj_is_FrozenDict, IDecomposableAssocBinaryOps4mapping_as_record):pass
class DecomposableAssocBinaryOps4FrozenDict_as_record(IDecomposableAssocBinaryOps4FrozenDict_as_record):
    @classmethod
    @final_method
    @override
    def ___get_ops_base_class_of_ops4one_main_obj4record_elements___(cls, /):
        return IAssocBinaryOps





class IDecomposableMonoidOps4mapping_as_record(IDecomposableAssocBinaryOps4mapping_as_record, IMonoidOps):
    r'''
    see:
        MonoidOps4tuple_as_mapping.__doc__ #__doc__MonoidOps4tuple_as_mapping
    #'''
    def __init__(sf, attr2value_monoid_ops, /):
        super().__init__(attr2value_monoid_ops)
        attr2ops = sf.attr2value_ops4one_main_obj
        mk = sf.mk_main_obj_from_mapping_or_pairs
        sf.__identity = mk((k, ops.get_monoid_identity()) for k, ops in attr2ops.items())
            #immutable mapping????

    @final_method
    @override
    def ___get_monoid_identity___(sf, /):
        '-> 1 # 1*a === a*1 === a::monoid_obj #see:get_monoid_identity'
        return sf.__identity

class IDecomposableMonoidOps4FrozenDict_as_record(IOps4OneMainObjType__main_obj_is_FrozenDict, IDecomposableMonoidOps4mapping_as_record):pass
class DecomposableMonoidOps4FrozenDict_as_record(IDecomposableMonoidOps4FrozenDict_as_record):
    r'''
    see:
        MonoidOps4FrozenDict_as_union_of_cased_records.__doc__ #__doc__MonoidOps4FrozenDict_as_union_of_cased_records
        seed.helper.check.checkers.check_FrozenDict_as_record
    #'''
    @classmethod
    @final_method
    @override
    def ___get_ops_base_class_of_ops4one_main_obj4record_elements___(cls, /):
        return IMonoidOps








def iter_items_except(excluded_key, mapping, /):
    return ((k,v) for k,v in mapping.items() if k != excluded_key)
def iter_values_except(excluded_key, mapping, /):
    return (mapping[k] for k in mapping if k != excluded_key)
def iter_keys_except(excluded_key, iterable, /):
    return (k for k in iterable if k != excluded_key)

check_cased_tuple
check_mapping_as_record
check_mapping_as_cased_record
check_FrozenDict_as_cased_record
#class IDecomposableOps4OneMainObjType4cased_tuple(IArgedDecomposableOps4OneMainObjType):
#class IDecomposableOps4OneMainObjType4mapping_as_record(IArgedDecomposableOps4OneMainObjType, IOps4OneMainObjType__main_obj_is_mapping):
class IDecomposableOps4OneMainObjType4mapping_as_cased_record(IArgedDecomposableOps4OneMainObjType, IOps4OneMainObjType__main_obj_is_mapping):
    r'''
    'mapping_as_cased_record vs cased_tuple'
    DecomposableMonoidOps4tuple_as_point, MonoidOps4cased_tuple, MonoidOps4FrozenDict_as_record, MonoidOps4FrozenDict_as_cased_record
        may used as auto_info@finger_tree_ops
    #'''
    @final_method
    @override
    def ___lookup_ops4subobj_of_main_obj___(sf, key, /):
        '-> (ops4subobj_of_main_obj<key>::IOps4OneMainObjType) #see:lookup_ops4subobj_of_main_obj'
        if not type(key) is str: raise LookupError
        #if key == sf.field_name4case_name: raise LookupError
        ops4subobj_at_key = sf.cased_attr2value_ops4one_main_obj[key]
        if type(ops4subobj_at_key) is str: raise LookupError
        return ops4subobj_at_key
    @classmethod
    @final_method
    @override
    def ___get_ops_base_cls4all_opss4subobj_of_main_obj___(cls, /):
        ops_base_cls = cls.___get_ops_base_class_of_ops4one_main_obj4cased_record_elements___()
        return ops_base_cls

    @classmethod
    @abstractmethod
    def ___get_ops_base_class_of_ops4one_main_obj4cased_record_elements___(cls, /):
        return IOps4OneMainObjType
    @classmethod
    @final_method
    def get_ops_base_class_of_ops4one_main_obj4cased_record_elements(cls, /):
        ops_base_cls = cls.___get_ops_base_class_of_ops4one_main_obj4cased_record_elements___()
        check_subclass(IOps4OneMainObjType, ops_base_cls)
        return ops_base_cls

    def __init__(sf, field_name4case_name, cased_attr2value_ops4one_main_obj, /):
        pass

    @property
    @final_method
    @def_new_method
    def cased_attr2value_ops4one_main_obj(sf, /):
        [field_name4case_name, cased_attr2value_ops4one_main_obj] = sf.args4ops4one_main_obj
        return cased_attr2value_ops4one_main_obj

    @property
    @final_method
    @def_new_method
    def field_name4case_name(sf, /):
        [field_name4case_name, cased_attr2value_ops4one_main_obj] = sf.args4ops4one_main_obj
        return field_name4case_name

    @classmethod
    @final_method
    @override
    def ___check4args4ops4one_main_obj___(cls, field_name4case_name, cased_attr2value_ops4one_main_obj, /):
        cased_attr2ops = cased_attr2value_ops4one_main_obj
        check_mapping_as_cased_record__free(field_name4case_name, cased_attr2ops)

        ops_base_cls = cls.get_ops_base_class_of_ops4one_main_obj4cased_record_elements()
        check_instance_all(ops_base_cls, iter_values_except(field_name4case_name, cased_attr2ops))


    @final_method
    @override
    def ___careless_check_main_obj___(sf, x, /):
        'a -> (None|raise) #see:careless_check_main_obj'
        cased_attr2ops = sf.cased_attr2value_ops4one_main_obj
        field_name4case_name = sf.field_name4case_name
        case_name = cased_attr2ops[field_name4case_name]
        check_mapping_as_cased_record(field_name4case_name, case_name, set(cased_attr2ops), x)
        if 0:
            for k, ops in iter_items_except(field_name4case_name, cased_attr2ops): ops.careless_check_main_obj(x[k])
#end of class IDecomposableOps4OneMainObjType4mapping_as_cased_record(IArgedDecomposableOps4OneMainObjType, IOps4OneMainObjType__main_obj_is_mapping):
class IDecomposableOps4OneMainObjType4FrozenDict_as_cased_record(IOps4OneMainObjType__main_obj_is_FrozenDict, IDecomposableOps4OneMainObjType4mapping_as_cased_record):pass
class DecomposableOps4OneMainObjType4FrozenDict_as_cased_record(IDecomposableOps4OneMainObjType4FrozenDict_as_cased_record):
    @classmethod
    @final_method
    @override
    def ___get_ops_base_class_of_ops4one_main_obj4cased_record_elements___(cls, /):
        return IOps4OneMainObjType

class IDecomposableAssocBinaryOps4mapping_as_cased_record(IDecomposableOps4OneMainObjType4mapping_as_cased_record, IAssocBinaryOps):
    def __init__(sf, field_name4case_name, cased_attr2value_assoc_bin_ops, /):
        super().__init__(field_name4case_name, cased_attr2value_assoc_bin_ops)
        cased_attr2ops = sf.cased_attr2value_ops4one_main_obj
        field_name4case_name = sf.field_name4case_name
        sf.__commutable = all(ops.is_assoc_bin_op_commutable() for ops in iter_values_except(field_name4case_name, cased_attr2ops))


    @final_method
    @override
    def ___is_assoc_bin_op_commutable___(sf, /):
        '-> (commutable::bool) #see:is_assoc_bin_op_commutable'
        return sf.__commutable

    @final_method
    @override
    def ___assoc_bin_op___(sf, lhs, rhs, /):
        'a -> a -> a # (a*b)*c === a*(b*c) #see:assoc_bin_op'
        cased_attr2ops = sf.cased_attr2value_ops4one_main_obj
        field_name4case_name = sf.field_name4case_name
        case_name = cased_attr2ops[field_name4case_name]
        mk = sf.mk_main_obj_from_mapping_or_pairs
        it = iter_items_except(field_name4case_name, cased_attr2ops)
        return mk(itertools.chain([(field_name4case_name, case_name)], ((k, ops.assoc_bin_op(lhs[k], rhs[k])) for k, ops in it)))

class IDecomposableAssocBinaryOps4FrozenDict_as_cased_record(IOps4OneMainObjType__main_obj_is_FrozenDict, IDecomposableAssocBinaryOps4mapping_as_cased_record):pass
class DecomposableAssocBinaryOps4FrozenDict_as_cased_record(IDecomposableAssocBinaryOps4FrozenDict_as_cased_record):
    @classmethod
    @final_method
    @override
    def ___get_ops_base_class_of_ops4one_main_obj4cased_record_elements___(cls, /):
        return IAssocBinaryOps





class IDecomposableMonoidOps4mapping_as_cased_record(IDecomposableAssocBinaryOps4mapping_as_cased_record, IMonoidOps):
    r'''
    see:
        MonoidOps4tuple_as_mapping.__doc__ #__doc__MonoidOps4tuple_as_mapping
    #'''
    def __init__(sf, field_name4case_name, cased_attr2value_monoid_ops, /):
        super().__init__(field_name4case_name, cased_attr2value_monoid_ops)
        cased_attr2ops = sf.cased_attr2value_ops4one_main_obj
        field_name4case_name = sf.field_name4case_name
        case_name = cased_attr2ops[field_name4case_name]
        mk = sf.mk_main_obj_from_mapping_or_pairs
        it = iter_items_except(field_name4case_name, cased_attr2ops)
        sf.__identity = mk(itertools.chain([(field_name4case_name, case_name)], ((k, ops.get_monoid_identity()) for k, ops in it)))
            #immutable mapping????

    @final_method
    @override
    def ___get_monoid_identity___(sf, /):
        '-> 1 # 1*a === a*1 === a::monoid_obj #see:get_monoid_identity'
        return sf.__identity

check_cased_tuple
class IDecomposableMonoidOps4FrozenDict_as_cased_record(IOps4OneMainObjType__main_obj_is_FrozenDict, IDecomposableMonoidOps4mapping_as_cased_record):pass
class DecomposableMonoidOps4FrozenDict_as_cased_record(IDecomposableMonoidOps4FrozenDict_as_cased_record):
    r'''
    see:
        MonoidOps4FrozenDict_as_union_of_cased_records.__doc__ #__doc__MonoidOps4FrozenDict_as_union_of_cased_records
        seed.helper.check.checkers.check_FrozenDict_as_cased_record
    #'''
    @classmethod
    @final_method
    @override
    def ___get_ops_base_class_of_ops4one_main_obj4cased_record_elements___(cls, /):
        return IMonoidOps
MonoidOps4FrozenDict_as_cased_record('', mk_FrozenDict({'':'Empty'}))


#DONE
#TODO below
WrapperOps4OneMainObjType
WrapperAssocBinaryOps
WrapperMonoidOps
WrapperMeasurableOps
#TODO above
check_FrozenDict_as_union_of_cased_records
class __xxx_cannot_impl_but_doc_is_useful___MonoidOps4FrozenDict_as_union_of_cased_records(IMonoidOps):
    r'''
    define MonoidOps4FrozenDict_as_union_of_cased_records.__doc__ #__doc__MonoidOps4FrozenDict_as_union_of_cased_records
        see also:
            MonoidOps4tuple_as_mapping.__doc__ #__doc__MonoidOps4tuple_as_mapping

    mapping vs record
        #FrozenDict_as_mapping vs FrozenDict_as_record
        #record <: mapping

        record key :: nonempty_str
        mapping key can be any hashable immutable obj

        record key_set fixed
        mapping key_set free

    record vs cased_record vs union_of_cased_records vivi tuple vs cased_tuple vs union_of_cased_tuples
        tuple_as_point<idx2value_type::tuple_as_array<value_type=type> >
        FrozenDict_as_record<field_name2value_type::FrozenDict_as_mapping<key_type=nonempty_str, value_type=type> >


        cased_tuple<case_name::nonempty_str, lshifted_idx2value_type::tuple_as_array<value_type=type> >
        FrozenDict_as_cased_record<field_name4case_name=""::str, case_name::nonempty_str, popped_field_name2value_type::FrozenDict_as_mapping<key_type=nonempty_str{!=field_name4case_name}, value_type=type> >


        union_of_cased_tuples<case_name2lshifted_idx2value_type::FrozenDict_as_mapping<key_type=nonempty_str, value_type=tuple_as_array<value_type=type> > >
        union_of_cased_records<field_name4case_name=""::str, case_name2popped_field_name2value_type::FrozenDict_as_mapping<key_type=nonempty_str, value_type=FrozenDict_as_mapping<key_type=nonempty_str{!=field_name4case_name}, value_type=type> > >



    why ???use str as mapping/record key???
        for export as json



    see:
        MonoidOps4FrozenDict_as_record
            seed.helper.check.checkers.check_FrozenDict_as_record
        MonoidOps4FrozenDict_as_cased_record
            seed.helper.check.checkers.check_FrozenDict_as_cased_record
        MonoidOps4FrozenDict_as_union_of_cased_records
            seed.helper.check.checkers.check_FrozenDict_as_union_of_cased_records

        MonoidOps4union_of_cased_tuples
            seed.helper.check.checkers.check_union_of_cased_tuples
        MonoidOps4cased_tuple
            seed.helper.check.checkers.check_cased_tuple
    #'''
#end of class __xxx_cannot_impl_but_doc_is_useful___MonoidOps4FrozenDict_as_union_of_cased_records(IMonoidOps):
























#class IDecomposableOps4OneMainObjType(IOps4OneMainObjType):
class DecomposableMeasurableOps__measure_is_getitem(WrapperMonoidOps, IMeasurableOps, IDecomposableOps4OneMainObjType):
    def __init__(sf, decomposable_monoid_ops:'IMonoidOps&IDecomposableOps4OneMainObjType', key, /):
        check_instance(IDecomposableOps4OneMainObjType, decomposable_monoid_ops)
        check_instance(IMonoidOps, decomposable_monoid_ops)
        hash(key)
        sf.__key = key
        super().__init__(decomposable_monoid_ops)
        ##
        main_obj_ops = sf.get_original_monoid_ops()
        ops4subobj_at_key = main_obj_ops[sf.__key]
        sf.__ops4result = ops4subobj_at_key
    @final_method
    @override
    def ___get_monoid_ops4measured_result___(measurable_ops, /):
        '-> monoid_ops<measured_result>::IMonoidOps #see:get_monoid_ops4measured_result'
        return measurable_ops.__ops4result
    @final_method
    @override
    def ___measure___(measurable_ops, measurable_obj, /):
        'measurable_obj -> (measured_result::monoid_obj) #see:measure'
        return measurable_obj[measurable_ops.__key]


    @final_method
    @override
    def ___lookup_ops4subobj_of_main_obj___(sf, key, /):
        '-> (ops4subobj_of_main_obj<key>::IOps4OneMainObjType) #see:lookup_ops4subobj_of_main_obj'
        main_obj_ops = sf.get_original_monoid_ops()
        return main_obj_ops[key]
    @classmethod
    @final_method
    @override
    def ___get_ops_base_cls4all_opss4subobj_of_main_obj___(cls, /):
        ops_base_cls = IMonoidOps
        return ops_base_cls
MeasurableOps__measure_is_getitem(
    MonoidOps4FrozenDict_as_cased_record('', mk_FrozenDict({'':'Size', 'value':the_monoid_ops4size}))
    ,'value'
    )['value']









