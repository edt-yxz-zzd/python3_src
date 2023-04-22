#__all__:goto
r'''[[[
e ../../python3_src/seed/mapping_tools/example4py_dict_impl.py
view ../../python3_src/seed/mapping_tools/determine_num_slots4hash_map.py_dict_impl.txt

seed.mapping_tools.example4py_dict_impl
py -m nn_ns.app.debug_cmd seed.mapping_tools.example4py_dict_impl
py -m seed.mapping_tools.example4py_dict_impl
py -m nn_ns.app.adhoc_argparser__main__call8module seed.mapping_tools.example4py_dict_impl



from seed.mapping_tools.example4py_dict_impl import IDictSetting, get_num_bits4perturb_rshift, get_max_presized_num_slots, get_min_num_slots, calc_max_load4num_slots, calc_min_pseudo_num_slots4num_items__on_create_or_merge, calc_min_pseudo_num_slots4num_items__on_insert_overflow_max_load

from seed.mapping_tools.example4py_dict_impl import setting__py_3_9_13_impl

from seed.mapping_tools.example4py_dict_impl import DKIX_EMPTY, DKIX_DUMMY, IDictTable, dk_lookup, iter_probe_sequence4collision_resolution__py_3_9_13_impl

from seed.mapping_tools.example4py_dict_impl import DictSharedHKeyTable

from seed.mapping_tools.example4py_dict_impl import DictTable__empty, DictTable__size_eq1, DictTable__split_table_ver, DictTable__combined_table_ver

from seed.mapping_tools.example4py_dict_impl import Dict__mixed_table

from seed.mapping_tools.example4py_dict_impl import calc_pseudo_num_slots5num_items, calc_num_slots5pseudo_num_slots


>>> from itertools import islice

>>> d = Dict__mixed_table(setting__py_3_9_13_impl)
>>> d
Dict__mixed_table(DictSetting__py_3_9_13_impl())
>>> type(d._get_table_())
<class 'seed.mapping_tools.example4py_dict_impl.DictTable__empty'>
>>> d[1] = 2
>>> d
Dict__mixed_table(DictSetting__py_3_9_13_impl(), [(1, 2)])
>>> type(d._get_table_())
<class 'seed.mapping_tools.example4py_dict_impl.DictTable__size_eq1'>
>>> d[1] = 3
>>> d
Dict__mixed_table(DictSetting__py_3_9_13_impl(), [(1, 3)])
>>> type(d._get_table_())
<class 'seed.mapping_tools.example4py_dict_impl.DictTable__size_eq1'>
>>> del d[1]
>>> d
Dict__mixed_table(DictSetting__py_3_9_13_impl())
>>> type(d._get_table_())
<class 'seed.mapping_tools.example4py_dict_impl.DictTable__empty'>

>>> num_bits4perturb_rshift = get_num_bits4perturb_rshift(setting__py_3_9_13_impl)
>>> min_num_slots = get_min_num_slots(setting__py_3_9_13_impl)
>>> [*islice(iter_probe_sequence4collision_resolution__py_3_9_13_impl(num_bits4perturb_rshift, min_num_slots, 0), min_num_slots+1)]
Traceback (most recent call last):
    ...
NameError: name 'logic' is not defined
>>> ls0 = [*islice(iter_probe_sequence4collision_resolution__py_3_9_13_impl(num_bits4perturb_rshift, min_num_slots, 0), min_num_slots)]
>>> ls0
[0, 1, 6, 7, 4, 5, 2, 3]
>>> [*islice(iter_probe_sequence4collision_resolution__py_3_9_13_impl(num_bits4perturb_rshift, min_num_slots, 8), min_num_slots+2)]
Traceback (most recent call last):
    ...
NameError: name 'logic' is not defined
>>> ls8 = [*islice(iter_probe_sequence4collision_resolution__py_3_9_13_impl(num_bits4perturb_rshift, min_num_slots, 8), min_num_slots+1)]
>>> ls8
[0, 1, 6, 7, 4, 5, 2, 3, 0]
>>> max_load = calc_max_load4num_slots(setting__py_3_9_13_impl, 8)

>>> for h in [*ls8[:max_load-1],8]: d[h] = (h+1)*111
>>> for h in [8,*ls8][:max_load]: d[h] = (h+1)*111
>>> d
Dict__mixed_table(DictSetting__py_3_9_13_impl(), [(0, 111), (1, 222), (6, 777), (7, 888), (8, 999)])
>>> d._get_table_()._xidc #collision resolution
[0, 1, -1, -1, 4, -1, 2, 3]
>>> d._get_table_()._ohkv_ls
[False, 0, 0, 111, False, 1, 1, 222, False, 6, 6, 777, False, 7, 7, 888, False, 8, 8, 999]





>>> d.clear()
>>> for h in [8,*ls8][:max_load]: d[h] = (h+1)*111
>>> d
Dict__mixed_table(DictSetting__py_3_9_13_impl(), [(8, 999), (0, 111), (1, 222), (6, 777), (7, 888)])
>>> d._get_table_()._xidc #collision resolution
[0, 1, -1, -1, 4, -1, 2, 3]
>>> d._get_table_()._ohkv_ls
[False, 8, 8, 999, False, 0, 0, 111, False, 1, 1, 222, False, 6, 6, 777, False, 7, 7, 888]

#resize:
>>> for h in [8,*ls8][max_load:]: d[h] = (h+1)*111
>>> d
Dict__mixed_table(DictSetting__py_3_9_13_impl(), [(8, 999), (0, 111), (1, 222), (6, 777), (7, 888), (4, 555), (5, 666), (2, 333), (3, 444)])
>>> d._get_table_()._xidc
[1, 2, 7, 8, 5, 6, 3, 4, 0, -1, -1, -1, -1, -1, -1, -1]
>>> d._get_table_()._ohkv_ls
[False, 8, 8, 999, False, 0, 0, 111, False, 1, 1, 222, False, 6, 6, 777, False, 7, 7, 888, False, 4, 4, 555, False, 5, 5, 666, False, 2, 2, 333, False, 3, 3, 444]

>>> d
Dict__mixed_table(DictSetting__py_3_9_13_impl(), [(8, 999), (0, 111), (1, 222), (6, 777), (7, 888), (4, 555), (5, 666), (2, 333), (3, 444)])
>>> d[1] = 2
>>> d
Dict__mixed_table(DictSetting__py_3_9_13_impl(), [(8, 999), (0, 111), (1, 2), (6, 777), (7, 888), (4, 555), (5, 666), (2, 333), (3, 444)])

>>> del d[1]
>>> d
Dict__mixed_table(DictSetting__py_3_9_13_impl(), [(8, 999), (0, 111), (6, 777), (7, 888), (4, 555), (5, 666), (2, 333), (3, 444)])
>>> d._get_table_()._xidc
[1, -2, 7, 8, 5, 6, 3, 4, 0, -1, -1, -1, -1, -1, -1, -1]
>>> d._get_table_()._ohkv_ls
[False, 8, 8, 999, False, 0, 0, 111, False, None, None, 1, False, 6, 6, 777, False, 7, 7, 888, False, 4, 4, 555, False, 5, 5, 666, False, 2, 2, 333, False, 3, 3, 444]

>>> d[1] = 3
>>> d
Dict__mixed_table(DictSetting__py_3_9_13_impl(), [(8, 999), (0, 111), (6, 777), (7, 888), (4, 555), (5, 666), (2, 333), (3, 444), (1, 3)])
>>> d._get_table_()._xidc
[1, 9, 7, 8, 5, 6, 3, 4, 0, -1, -1, -1, -1, -1, -1, -1]
>>> d._get_table_()._ohkv_ls
[False, 8, 8, 999, False, 0, 0, 111, False, None, None, 1, False, 6, 6, 777, False, 7, 7, 888, False, 4, 4, 555, False, 5, 5, 666, False, 2, 2, 333, False, 3, 3, 444, True, 1, 1, 3]

>>> [*iter(d)]
[8, 0, 6, 7, 4, 5, 2, 3, 1]

>>> [*reversed(d)]
[1, 3, 2, 5, 4, 7, 6, 0, 8]
>>> [*reversed(d)] == [*reversed([*iter(d)])]
True

>>> d.popitem()
(1, 3)
>>> d.popitem()
(3, 444)
>>> d.popitem()
(2, 333)
>>> d.popitem()
(5, 666)
>>> d.popitem()
(4, 555)
>>> d.popitem()
(7, 888)
>>> d._get_table_()._xidc
[1, -2, -1, -1, -1, -1, 3, -1, 0, -1, -1, -1, -1, -1, -1, -1]
>>> d._get_table_()._ohkv_ls
[False, 8, 8, 999, False, 0, 0, 111, False, None, None, 1, False, 6, 6, 777]

>>> d.popitem()
(6, 777)
>>> d._get_table_()._xidc
[1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1]
>>> d._get_table_()._ohkv_ls
[False, 8, 8, 999, False, 0, 0, 111]

>>> d.popitem()
(0, 111)
>>> d.popitem()
(8, 999)
>>> d._get_table_()._xidc
[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
>>> d._get_table_()._ohkv_ls
[]
>>> d
Dict__mixed_table(DictSetting__py_3_9_13_impl())
>>> type(d._get_table_())
<class 'seed.mapping_tools.example4py_dict_impl.DictTable__combined_table_ver'>
>>> d.clear()
>>> d
Dict__mixed_table(DictSetting__py_3_9_13_impl())
>>> type(d._get_table_())
<class 'seed.mapping_tools.example4py_dict_impl.DictTable__empty'>


'basic_modify: make_keys_shared, clear, pop, popitem, __setitem__, setdefault'
>>> d.setdefault(1, 222)
222
>>> d.setdefault(2, 333)
333
>>> d.setdefault(3, 444)
444
>>> d.setdefault(1, 111)
222
>>> d
Dict__mixed_table(DictSetting__py_3_9_13_impl(), [(1, 222), (2, 333), (3, 444)])
>>> type(d._get_table_())
<class 'seed.mapping_tools.example4py_dict_impl.DictTable__combined_table_ver'>
>>> d.make_keys_shared() #doctest: +ELLIPSIS
DictSharedHKeyTable(5, 5, (-1, 0, 1, 2, -1, -1, -1, -1), (1, 1, 2, 2, 3, 3), <function iter_probe_sequence4collision_resolution__py_3_9_13_impl at 0x...>)
>>> d
Dict__mixed_table(DictSetting__py_3_9_13_impl(), [(1, 222), (2, 333), (3, 444)])
>>> type(d._get_table_())
<class 'seed.mapping_tools.example4py_dict_impl.DictTable__split_table_ver'>

>>> d.setdefault(2, 444)
333
>>> d[1] = 2
>>> d
Dict__mixed_table(DictSetting__py_3_9_13_impl(), [(1, 2), (2, 333), (3, 444)])
>>> del d[3] #pop
>>> d
Dict__mixed_table(DictSetting__py_3_9_13_impl(), [(1, 2), (2, 333)])
>>> type(d._get_table_())
<class 'seed.mapping_tools.example4py_dict_impl.DictTable__split_table_ver'>
>>> del d[1]
>>> d
Dict__mixed_table(DictSetting__py_3_9_13_impl(), [(2, 333)])
>>> type(d._get_table_())
<class 'seed.mapping_tools.example4py_dict_impl.DictTable__combined_table_ver'>



#]]]'''
__all__ = r'''
    IS_POWER_OF_2
    check_pint
    check_power_of_2

IDictSetting
    get_num_bits4perturb_rshift
    get_max_presized_num_slots
    get_min_num_slots
    calc_max_load4num_slots
    calc_min_pseudo_num_slots4num_items__on_create_or_merge
    calc_min_pseudo_num_slots4num_items__on_insert_overflow_max_load

DictSetting__py_3_9_13_impl
    setting__py_3_9_13_impl

DKIX_EMPTY
DKIX_DUMMY
iter_probe_sequence4collision_resolution__py_3_9_13_impl

DictSharedHKeyTable

IDictTable
    dk_lookup

    DictTable__empty
    DictTable__size_eq1

    DictTable__split_table_ver
    DictTable__combined_table_ver

Dict__mixed_table
    calc_pseudo_num_slots5num_items
    calc_num_slots5pseudo_num_slots

'''.split()#'''
__all__

from collections.abc import Set, Mapping
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.math.floor_ceil import floor_log2, ceil_log2
from seed.tiny_.mk_fdefault import mk_default
#def mk_default(imay_xdefault_rank, xdefault, /,*args4xdefault):
from seed.helper.repr_input import repr_helper, repr_helper_ex
from seed.tiny_.check import check_int_ge_lt, check_int_ge, check_imay, check_uint, check_pair, check_type_le, check_type_is, check_callable #check_uint_lt, check_int_ge_le, check_tmay
from seed.tiny import null_tuple
from seed.tiny_.singleton import mk_SingletonClass, mk_existing_type_singleton


class IDictSetting(ABC):
    r'''
    [IS_POWER_OF_2(num_slots)]
    [IS_POWER_OF_2(min_num_slots)]
    [may not IS_POWER_OF_2(pseudo_num_slots)]

    num_items - ma_used/minused
        = len(mappping)

    load - dk_nentries
        max_load - USABLE_FRACTION(dk_size)

    num_usable_slots - dk_usable
        = max_load - load

    num_slots - dk_size
        min_num_slots - PyDict_MINSIZE
        pseudo_num_slots - minsize
            | create new dict or merge = ESTIMATE_SIZE(num_items from input set/dict)
            | overflow max_load when insert 1 = GROWTH_RATE(num_items from original dict)


    num_bits4perturb_rshift - PERTURB_SHIFT
    max_presized_num_slots - max_presize
    calc_max_load4num_slots - USABLE_FRACTION
    calc_min_pseudo_num_slots4num_items__on_create_or_merge - ESTIMATE_SIZE
    calc_min_pseudo_num_slots4num_items__on_insert_overflow_max_load - GROWTH_RATE

    xmay_item_idx - ix
    probe_idx - hashpos/i

    hitem =[def]= (h,k,v) === (hash_value, key, value)
    ohitem =[def]= (o,None,None,probe_idx)|(o,h,k,v)
        #old_xmay = DKIX_EMPTY|DKIX_DUMMY
        #new is item_idx, old is old_xmay
        ohitem
            = (o,None,None,probe_idx)
            | (o,h,k,v)
        (o,h,k,v) === (old_xmay_is_dummy, hash_value, key, value)

######################
######################
######################

py3.9.13
#define PyDict_MINSIZE 8
#define PERTURB_SHIFT 5
#define USABLE_FRACTION(n) (((n) << 1)/3)
#define ESTIMATE_SIZE(n)  (((n)*3+1) >> 1)
#define GROWTH_RATE(d) ((d)->ma_used*3)

_PyDict_NewPresized(Py_ssize_t minused)
    const Py_ssize_t max_presize = 128 * 1024;

#PERTURB_SHIFT used in def__collision_resolution:goto
USABLE_FRACTION is the maximum dictionary load
ESTIMATE_SIZE is reverse function of USABLE_FRACTION
  #used in _PyDict_NewPresized, _PyDict_FromKeys[#set/dict#], dict_merge
#GROWTH_RATE like ESTIMATE_SIZE but used when overflow
  #used only in insertion_resize

#define IS_POWER_OF_2(x) (((x) & (x-1)) == 0)
make_keys_shared



    '''#'''
    __slots__ = ()

    @abstractmethod
    def get_num_bits4perturb_rshift(sf, /):
        '-> num_bits4perturb_rshift/pint #=== PERTURB_SHIFT'

    @abstractmethod
    def get_max_presized_num_slots(sf, /):
        '-> max_presized_num_slots/pint{>=min_num_slots}/IS_POWER_OF_2 #=== max_presize'
    @abstractmethod
    def get_min_num_slots(sf, /):
        '-> min_num_slots/pint{>=2}/IS_POWER_OF_2 #=== PyDict_MINSIZE'
    @abstractmethod
    def calc_max_load4num_slots(sf, pseudo_num_slots, /):
        'pseudo_num_slots/pint{>=min_num_slots}/neednot_IS_POWER_OF_2 -> max_load/[1..<pseudo_num_slots] #=== USABLE_FRACTION()'
    @abstractmethod
    def calc_min_pseudo_num_slots4num_items__on_create_or_merge(sf, num_items, /):
        'num_items/pint -> min_pseudo_num_slots/pint{>num_items}/neednot_IS_POWER_OF_2 #=== ESTIMATE_SIZE()'
    @abstractmethod
    def calc_min_pseudo_num_slots4num_items__on_insert_overflow_max_load(sf, num_items, /):
        'num_items/pint -> min_pseudo_num_slots/pint{>num_items}/neednot_IS_POWER_OF_2 #=== GROWTH_RATE()'
#end-class IDictSetting(ABC):
def IS_POWER_OF_2(x, /):
    return (((x) & (x-1)) == 0)
def check_pint(i, /):
    check_int_ge(1, i)
def check_power_of_2(i, /):
    check_pint(i)
    if not IS_POWER_OF_2(i): raise TypeError
def get_num_bits4perturb_rshift(sf, /):
    '-> num_bits4perturb_rshift/pint #=== PERTURB_SHIFT'
    num_bits4perturb_rshift = sf.get_num_bits4perturb_rshift()
    check_pint(num_bits4perturb_rshift)
    return num_bits4perturb_rshift

def get_max_presized_num_slots(sf, /):
    '-> max_presized_num_slots/pint{>=min_num_slots}/IS_POWER_OF_2 #=== max_presize'
    max_presized_num_slots = sf.get_max_presized_num_slots()
    check_pint(max_presized_num_slots)
    return max_presized_num_slots
def get_min_num_slots(sf, /):
    '-> min_num_slots/pint{>=2}/IS_POWER_OF_2 #=== PyDict_MINSIZE'
    min_num_slots = sf.get_min_num_slots()
    check_power_of_2(min_num_slots)
    return min_num_slots
def calc_max_load4num_slots(sf, pseudo_num_slots, /):
    'pseudo_num_slots/pint{>=min_num_slots}/neednot_IS_POWER_OF_2 -> max_load/[1..<pseudo_num_slots] #=== USABLE_FRACTION()'
    check_int_ge(2, pseudo_num_slots)
    max_load = sf.calc_max_load4num_slots(pseudo_num_slots)
    check_int_ge_lt(1, pseudo_num_slots, max_load)
    return max_load
def calc_min_pseudo_num_slots4num_items__on_create_or_merge(sf, num_items, /):
    'num_items/pint -> min_pseudo_num_slots/pint{>num_items}/neednot_IS_POWER_OF_2 #=== ESTIMATE_SIZE()'
    check_int_ge(1, num_items)
    min_pseudo_num_slots = sf.calc_min_pseudo_num_slots4num_items__on_create_or_merge(num_items)
    check_int_ge(num_items, min_pseudo_num_slots)
    #check_int_ge_lt(1, min_pseudo_num_slots, num_items)
    if not calc_max_load4num_slots(sf, min_pseudo_num_slots) == num_items:raise logic-err
        #『==』
    if not (min_pseudo_num_slots <= get_min_num_slots(sf) or calc_max_load4num_slots(sf, min_pseudo_num_slots-1) < num_items):raise logic-err
    return min_pseudo_num_slots
def calc_min_pseudo_num_slots4num_items__on_insert_overflow_max_load(sf, num_items, /):
    'num_items/pint -> min_pseudo_num_slots/pint{>num_items}/neednot_IS_POWER_OF_2 #=== GROWTH_RATE()'
    check_int_ge(1, num_items)
    min_pseudo_num_slots = sf.calc_min_pseudo_num_slots4num_items__on_insert_overflow_max_load(num_items)
    check_int_ge(num_items, min_pseudo_num_slots)
    #assert 1 <= num_items < min_pseudo_num_slots, (num_items, min_pseudo_num_slots)
    #check_int_ge_lt(1, min_pseudo_num_slots, num_items)
    if not calc_max_load4num_slots(sf, min_pseudo_num_slots) >= num_items:raise logic-err
        #『>=』
    return min_pseudo_num_slots

class DictSetting__py_3_9_13_impl(IDictSetting):
    __slots__ = ()
    def __repr__(sf, /):
        return repr_helper(sf)

    @override
    def get_num_bits4perturb_rshift(sf, /):
        '-> num_bits4perturb_rshift/pint #=== PERTURB_SHIFT'
        return 5

    @override
    def get_max_presized_num_slots(sf, /):
        '-> max_presized_num_slots/pint{>=min_num_slots}/IS_POWER_OF_2 #=== max_presize'
        return 128 * 1024
    @override
    def get_min_num_slots(sf, /):
        '-> min_num_slots/pint{>=2}/IS_POWER_OF_2 #=== PyDict_MINSIZE'
        return 8
    @override
    def calc_max_load4num_slots(sf, pseudo_num_slots, /):
        'pseudo_num_slots/pint{>=min_num_slots}/neednot_IS_POWER_OF_2 -> max_load/[1..<pseudo_num_slots] #=== USABLE_FRACTION()'
        return pseudo_num_slots*2//3
    @override
    def calc_min_pseudo_num_slots4num_items__on_create_or_merge(sf, num_items, /):
        'num_items/pint -> min_pseudo_num_slots/pint{>num_items}/neednot_IS_POWER_OF_2 #=== ESTIMATE_SIZE()'
        return (num_items*3+1)//2
    @override
    def calc_min_pseudo_num_slots4num_items__on_insert_overflow_max_load(sf, num_items, /):
        'num_items/pint -> min_pseudo_num_slots/pint{>num_items}/neednot_IS_POWER_OF_2 #=== GROWTH_RATE()'
        return (num_items*3)
mk_existing_type_singleton(DictSetting__py_3_9_13_impl)
setting__py_3_9_13_impl = DictSetting__py_3_9_13_impl()
#end-class DictSetting__py_3_9_13_impl(IDictSetting):
DKIX_EMPTY = -1
DKIX_DUMMY = -2
    #DictTable__combined_table_ver only
    # why need DKIX_DUMMY?
    #   if set DKIX_EMPTY instead,ok for setitem, but err for getitem:collision resolution stop at DKIX_EMPTY, but it should continue search if DKIX_DUMMY
    #why split_table_ver has no DKIX_DUMMY?
    #   DictTable__split_table_ver is FILO, no dummy
    #
    # reuse probe_idx<DKIX_DUMMY> or not?
    #   * not reuse: ==>> num_items+num_dummy==load
    #       when erase last item/popitem ==>> decrease load by recover all last DKIX_DUMMY to DKIX_EMPTY; need to store probe_idx<DKIX_DUMMY> in null_hitem
    #       but can not recover DKIX_DUMMY to item_idx
    #
    #   * reuse: ==>> num_items+num_dummy<=load
    #       see:_dk_lookup:may_probe_idx4fst_dummy
    #       reduce collision resolution
    #       but can not recover DKIX_DUMMY to DKIX_EMPTY, hence (num_items+num_dummy) increase only
    #
#DKIX_ERROR = -3 #raise exc when eval(eq(query_key,storage_key))
def iter_probe_sequence4collision_resolution__py_3_9_13_impl(num_bits4perturb_rshift, num_slots, hash_value, /):
    '-> Iter probe_idx{uint%num_slots}'
    check_power_of_2(num_slots)
    check_pint(num_bits4perturb_rshift)

    mask = num_slots-1 # 0b111...111
    perturb = hash_value;
    i = hash_value & mask;

    while perturb:
        yield i
        perturb >>= num_bits4perturb_rshift;
        i = (i*5 + perturb + 1) & mask
    _i = i
    while 1:
        yield i
        i = (i*5 + 1) & mask # random-number generation #period is num_slots
        if i==_i: raise logic-err-'no NULL slot: max_load==num_slots?'
    #stop iff has NULL slot ==>> [max_load < num_slots]


class IDictTable(ABC):
    'internal ohitem vs public hitem'
    __slots__ = ()

    @abstractmethod
    def get_num_items(sf, /):
        '-> num_items/ma_used'
    @abstractmethod
    def get_max_load(sf, /):
        '-> max_load'
    @abstractmethod
    def get_load(sf, /):
        '-> load/dk_nentries'
    @abstractmethod
    def get_num_slots(sf, /):
        '-> num_slots/dk_size'

    @abstractmethod
    def _iadd_num_items_(sf, delta, /):
        'delta -> None'

    @abstractmethod
    def _get_xmay_item_idx_(sf, probe_idx, /):
        'probe_idx -> xmay_item_idx'
    @abstractmethod
    def _set_xmay_item_idx_(sf, probe_idx, xmay_item_idx, /):
        'probe_idx -> xmay_item_idx -> None'

    @abstractmethod
    def _push_ohitem_(sf, o, h, k, v, /):
        'old_xmay_is_dummy -> hash_value -> key -> value -> None'
    @abstractmethod
    def _del_last_ohitem_(sf, /):
        '-> None'
    @abstractmethod
    def _get_ohitem_(sf, item_idx, /):
        'item_idx -> (old_xmay_is_dummy, hash_value, key, value)'
    @abstractmethod
    def _set_ohitem_(sf, item_idx, o, h, k, v, /):
        'item_idx -> old_xmay_is_dummy -> hash_value -> key -> value -> None'

    #dk_lookup:goto
    @abstractmethod
    def iter_probe_sequence4collision_resolution(sf, num_slots, hash_value, /):
        '-> Iter probe_idx{uint%num_slots}'


    def get_num_usable_slots(sf, /):
        '-> num_usable_slots/dk_usable'
        #bug:return sf.get_num_slots()-sf.get_load()
        return sf.get_max_load()-sf.get_load()

    def probe_idx2xmay_item_idx(sf, probe_idx, /):
        '-> xmay_item_idx/[-2..<num_slots]'
        check_uint(probe_idx)
        return sf._get_xmay_item_idx_(probe_idx)
    def item_idx2hitem(sf, item_idx, /):
        'item_idx -> (hash_value, key, value)'
        check_uint(item_idx)
        (o,h,k,v) = sf._get_ohitem_(item_idx)
        return (h,k,v)

    def push(sf, may_probe_idx4fst_dummy, probe_idx, h, k, v, /):
        if not sf.get_num_usable_slots() > 0: raise logic-err
        if not sf.probe_idx2xmay_item_idx(probe_idx) == DKIX_EMPTY: raise logic-err
        if may_probe_idx4fst_dummy is None:
            #probe_idx = probe_idx<DKIX_EMPTY>
            old_xmay_is_dummy = False
        else:
            #probe_idx = probe_idx<DKIX_DUMMY>
            probe_idx = may_probe_idx4fst_dummy
            if not sf.probe_idx2xmay_item_idx(probe_idx) == DKIX_DUMMY: raise logic-err
            old_xmay_is_dummy = True
        o = old_xmay_is_dummy
        item_idx = sf.get_load()
        sf._push_ohitem_(o,h,k,v)
        sf._set_xmay_item_idx_(probe_idx, item_idx)
        sf._iadd_num_items_(1)
        return

    def overwrite(sf, probe_idx, item_idx, h, k, v, /):
        check_uint(item_idx)
        xmay_item_idx = sf.probe_idx2xmay_item_idx(probe_idx)
        if not xmay_item_idx == item_idx: raise logic-err
        item_idx = xmay_item_idx
        (_o, _h, _k, _v) = sf._get_ohitem_(item_idx)
        if not _h == h: raise logic-err
        if not _k == k: raise logic-err
        sf._set_ohitem_(item_idx, _o,_h,_k,v)
        return


    def erase(sf, probe_idx, item_idx, /):
        check_uint(item_idx)
        if item_idx+1 == sf.get_load():
            sf.pop(probe_idx)
            return
        xmay_item_idx = sf.probe_idx2xmay_item_idx(probe_idx)
        if not xmay_item_idx == item_idx: raise logic-err
        item_idx = xmay_item_idx

        (_o, _h, _k, _v) = sf._get_ohitem_(item_idx)
        sf._set_ohitem_(item_idx, *[_o, None, None, probe_idx])
        sf._set_xmay_item_idx_(probe_idx, DKIX_DUMMY)
        sf._iadd_num_items_(-1)
        return

    def pop(sf, probe_idx, /):
        it = iter(reversed(range(sf.get_load())))
        for item_idx in it:
            break
        else:
            raise logic-err
        if not item_idx >= 0: raise logic-err
        xmay_item_idx = sf.probe_idx2xmay_item_idx(probe_idx)
        if not xmay_item_idx == item_idx: raise logic-err
        item_idx = xmay_item_idx
        (o,h,k,v) = sf._get_ohitem_(item_idx)
        if h is None: raise logic-err
        hkv = (h,k,v)
        old_xmay_is_dummy = o
        old_xmay = DKIX_DUMMY if old_xmay_is_dummy else DKIX_EMPTY
        sf._del_last_ohitem_()
        sf._set_xmay_item_idx_(probe_idx, old_xmay)
        sf._iadd_num_items_(-1)
        for item_idx in it:
            (o,h,k,v) = sf._get_ohitem_(item_idx)
            if h is not None:
                break
            old_xmay_is_dummy = o
            old_xmay = DKIX_DUMMY if old_xmay_is_dummy else DKIX_EMPTY
            probe_idx = v
            if not sf.probe_idx2xmay_item_idx(probe_idx) == DKIX_DUMMY: raise logic-err
            sf._del_last_ohitem_()
            sf._set_xmay_item_idx_(probe_idx, old_xmay)
        #bug:return (h,k,v)
        return hkv
    def iter_hitems(sf, /, *, reverse):
        '-> Iter (hash_value, key, value)'
        it = range(sf.get_load())
        if reverse:
            it = reversed(it)
        for item_idx in it:
            (o,h,k,v) = sf._get_ohitem_(item_idx)
            if h is not None:
                yield h,k,v


def dk_lookup(table, key, hash_value, /):
    '-> (may_probe_idx4fst_dummy, probe_idx4read/[0..<num_slots], imay_item_idx/imay/[-1..<num_slots], *tmay_item)'
    num_slots = table.get_num_slots()
    if not 0 < num_slots: raise logic-err

    (may_probe_idx4fst_dummy, probe_idx, imay_item_idx, *tmay_item) = _dk_lookup(table, key, hash_value)
    check_int_ge_lt(0, num_slots, probe_idx)
    check_imay(imay_item_idx)
    if not may_probe_idx4fst_dummy is None:
        probe_idx4fst_dummy = may_probe_idx4fst_dummy
        assert 0 <= probe_idx4fst_dummy < num_slots
        assert table.probe_idx2xmay_item_idx(probe_idx4fst_dummy) == DKIX_DUMMY

    assert table.probe_idx2xmay_item_idx(probe_idx) == imay_item_idx != DKIX_DUMMY

    if imay_item_idx < 0:
        assert imay_item_idx == DKIX_EMPTY
        assert not tmay_item
    else:
        item_idx = imay_item_idx
        [item] = tmay_item
        check_pair(item)
        if not 0 <= item_idx < table.get_load() < table.get_num_slots(): raise TypeError
    return (may_probe_idx4fst_dummy, probe_idx, imay_item_idx, *tmay_item)
def _dk_lookup(table, key, hash_value, /):
    num_slots = table.get_num_slots()
    may_probe_idx4fst_dummy = None
    for probe_idx in table.iter_probe_sequence4collision_resolution(num_slots, hash_value):
        xmay_item_idx = table.probe_idx2xmay_item_idx(probe_idx)
        if xmay_item_idx >= 0:
            item_idx = xmay_item_idx
            (h, k, v) = table.item_idx2hitem(item_idx)
            if h == hash_value and k == key:
                # k==key may raise
                #   omit:DKIX_ERROR here
                return (may_probe_idx4fst_dummy, probe_idx, item_idx, (k,v))
        elif xmay_item_idx == DKIX_DUMMY:
            if may_probe_idx4fst_dummy is None:
                probe_idx4fst_dummy = probe_idx
                may_probe_idx4fst_dummy = probe_idx4fst_dummy
            continue
        elif xmay_item_idx == DKIX_EMPTY:
            return (may_probe_idx4fst_dummy, probe_idx, DKIX_EMPTY,)
        else:
            raise logic-err
    else:
        raise logic-err
#end-class IDictTable:


class DictTable__empty(IDictTable):
    __slots__ = ()
    #def __new__(cls, /): return __new4singleton__(__class__, cls)
    @override
    def get_num_items(sf, /):
        '-> num_items/ma_used'
        return 0
    @override
    def get_max_load(sf, /):
        '-> max_load'
        raise logic-err
        return 0
    @override
    def get_load(sf, /):
        '-> load/dk_nentries'
        return 0
    @override
    def get_num_slots(sf, /):
        '-> num_slots/dk_size'
        return 0

    @override
    def _iadd_num_items_(sf, delta, /):
        'delta -> None'
        raise logic-err

    @override
    def _get_xmay_item_idx_(sf, probe_idx, /):
        'probe_idx -> xmay_item_idx'
        raise logic-err
    @override
    def _set_xmay_item_idx_(sf, probe_idx, xmay_item_idx, /):
        'probe_idx -> xmay_item_idx -> None'
        raise logic-err

    @override
    def _push_ohitem_(sf, o, h, k, v, /):
        'old_xmay_is_dummy -> hash_value -> key -> value -> None'
        raise logic-err
    @override
    def _del_last_ohitem_(sf, /):
        '-> None'
        raise logic-err
    @override
    def _get_ohitem_(sf, item_idx, /):
        'item_idx -> (old_xmay_is_dummy, hash_value, key, value)'
        raise logic-err
    @override
    def _set_ohitem_(sf, item_idx, o, h, k, v, /):
        'item_idx -> old_xmay_is_dummy -> hash_value -> key -> value -> None'
        raise logic-err
    #dk_lookup:goto
    @override
    def iter_probe_sequence4collision_resolution(sf, num_slots, hash_value, /):
        '-> Iter probe_idx{uint%num_slots}'
        raise logic-err
mk_existing_type_singleton(DictTable__empty)
DictTable__empty()
assert DictTable__empty() is DictTable__empty()
try:
    object.__new__(DictTable__empty)
except TypeError:
    pass
else:
    raise logic-err
#end-class DictTable__empty(IDictTable):


class DictTable__size_eq1(IDictTable):
    __slots__ = '_hitem'
    def __repr__(sf, /):
        return repr_helper(sf, *sf._hitem)
    def __init__(sf, h, k, v, /):
        sf._hitem = (h,k,v)

    @override
    def get_num_items(sf, /):
        '-> num_items/ma_used'
        return 1
    @override
    def get_max_load(sf, /):
        '-> max_load'
        return 1
    @override
    def get_load(sf, /):
        '-> load/dk_nentries'
        return 1
    @override
    def get_num_slots(sf, /):
        '-> num_slots/dk_size'
        return 2

    @override
    def _get_xmay_item_idx_(sf, probe_idx, /):
        'probe_idx -> xmay_item_idx'
        assert 0 <= probe_idx < 2
        if probe_idx == 0:
            xmay_item_idx = item_idx = 0
        else:
            xmay_item_idx = DKIX_EMPTY
        return xmay_item_idx

    @override
    def _get_ohitem_(sf, item_idx, /):
        'item_idx -> (old_xmay_is_dummy, hash_value, key, value)'
        assert 0 <= item_idx < 2
        if item_idx == 0:
            o = old_xmay_is_dummy = False
            (h,k,v) = sf._hitem
            return (o,h,k,v)
        else:
            raise logic-err
    @override
    def overwrite(sf, probe_idx, item_idx, h, k, v, /):
        assert probe_idx == 0
        assert item_idx == 0
        sf._hitem = (h,k,v)
    #dk_lookup:goto
    @override
    def iter_probe_sequence4collision_resolution(sf, num_slots, hash_value, /):
        '-> Iter probe_idx{uint%num_slots}'
        yield 0
        yield 1 #to get DKIX_EMPTY to stop iter
        return
        raise logic-err


    @override
    def _iadd_num_items_(sf, delta, /):
        'delta -> None'
        raise logic-err

    @override
    def _set_xmay_item_idx_(sf, probe_idx, xmay_item_idx, /):
        'probe_idx -> xmay_item_idx -> None'
        raise logic-err


    @override
    def _push_ohitem_(sf, o, h, k, v, /):
        'old_xmay_is_dummy -> hash_value -> key -> value -> None'
        raise logic-err
    @override
    def _del_last_ohitem_(sf, /):
        '-> None'
        raise logic-err
    @override
    def _set_ohitem_(sf, item_idx, o, h, k, v, /):
        'item_idx -> old_xmay_is_dummy -> hash_value -> key -> value -> None'
        raise logic-err
#end-class DictTable__size_eq1(IDictTable):


class DictSharedHKeyTable:
    'no dummy:no DKIX_DUMMY'
    #mk from DictTable__combined_table_ver.make_keys_shared
    def __repr__(sf, /):
        return repr_helper(sf, sf._nbits, sf._max_load, sf._xidc, sf._hk_ls, sf._f)
    def __init__(sf, num_bits4perturb_rshift, max_load, imay_item_idx_array, flat_hash_key_pair_array, iter_probe_sequence4collision_resolution_, /):
        check_callable(iter_probe_sequence4collision_resolution_)
        check_pint(max_load)
        check_pint(num_bits4perturb_rshift)

        check_type_is(tuple, imay_item_idx_array)
        check_type_is(tuple, flat_hash_key_pair_array)
        if len(flat_hash_key_pair_array)&1:raise TypeError
        num_slots = len(imay_item_idx_array)
        num_items = len(flat_hash_key_pair_array)//2
        if not 1 <= num_items <= max_load < num_slots:raise TypeError
            #???since DictTable__size_eq1
        check_power_of_2(num_slots)

        if not all(0 <= imay_item_idx < num_items or imay_item_idx==DKIX_EMPTY for imay_item_idx in imay_item_idx_array):raise TypeError

        if any(DKIX_DUMMY == imay_item_idx for imay_item_idx in imay_item_idx_array):raise TypeError
        assert DKIX_EMPTY == -1

        if not num_slots-num_items == sum(DKIX_EMPTY == imay_item_idx for imay_item_idx in imay_item_idx_array):raise TypeError

        counts = [0]*num_items
        for imay_item_idx in imay_item_idx_array:
            if imay_item_idx == DKIX_EMPTY:
                continue
            item_idx = imay_item_idx
            counts[item_idx] += 1
        if not counts == [1]*num_items:raise TypeError

        sf._xidc = imay_item_idx_array
        sf._hk_ls = flat_hash_key_pair_array
        sf._max_load = max_load
        sf._total_keys = num_items #total_keys #no values
        sf._nbits = num_bits4perturb_rshift
        sf._f = iter_probe_sequence4collision_resolution_
    @property
    def imay_item_idx_array(sf, /):
        'imay_item_idx := imay_item_idx_array[probe_idx]'
        return sf._xidc
    @property
    def flat_hash_key_pair_array(sf, /):
        '(h,k) := flat_hash_key_pair_array[2*item_idx:2*item_idx+2]'
        return sf._hk_ls
    @property
    def load(sf, /):
        #no dummy
        return sf.total_keys
    @property
    def max_load(sf, /):
        return sf.total_keys
        #return sf._max_load
    @property
    def total_keys(sf, /):
        return sf._total_keys
    @property
    def num_bits4perturb_rshift(sf, /):
        return sf._nbits
    @property
    def num_slots(sf, /):
        return len(sf._xidc)
    @property
    def iter_probe_sequence4collision_resolution_(sf, /):
        return (sf._f)


class DictTable__split_table_ver(IDictTable):
    #see:make_keys_shared
    __slots__ = r'''
    _sh
    _vs
    _sz
    '''.split()#'''
    def __repr__(sf, /):
        return repr_helper(sf, sf._sh, sf._vs)
    def clear_values(sf, /):
        assert sf._sz == len(sf._vs)
        sf._vs.clear()
        sf._sz = 0
    def __init__(sf, shared_hkey_table, values, /):
        check_type_is(DictSharedHKeyTable, shared_hkey_table)
        if not len(values) <= shared_hkey_table.total_keys:raise logic-err
        sf._sh = shared_hkey_table
        sf._vs = [*values]
        sf._sz = len(values)
    @property
    def shared_hkey_table(sf, /):
        return sf._sh

    #dk_lookup:goto
    @override
    def iter_probe_sequence4collision_resolution(sf, num_slots, hash_value, /):
        '-> Iter probe_idx{uint%num_slots}'
        return sf._sh.iter_probe_sequence4collision_resolution_(sf._sh.num_bits4perturb_rshift, num_slots, hash_value)


    @override
    def get_num_items(sf, /):
        '-> num_items/ma_used'
        return len(sf._vs)
    @override
    def get_max_load(sf, /):
        '-> max_load'
        return sf._sh.max_load
    @override
    def get_load(sf, /):
        '-> load/dk_nentries'
        return sf.get_num_items()
    @override
    def get_num_slots(sf, /):
        '-> num_slots/dk_size'
        return sf._sh.num_slots

    @override
    def _iadd_num_items_(sf, delta, /):
        'delta -> None'
        sf._sz += delta

    @override
    def _get_xmay_item_idx_(sf, probe_idx, /):
        'probe_idx -> xmay_item_idx'
        imay_item_idx = sf._sh.imay_item_idx_array[probe_idx]
        xmay_item_idx = imay_item_idx
        return xmay_item_idx
    @override
    def _set_xmay_item_idx_(sf, probe_idx, xmay_item_idx, /):
        'probe_idx -> xmay_item_idx -> None'
        assert xmay_item_idx >= -1
        imay_item_idx = xmay_item_idx
        xidc = sf._sh.imay_item_idx_array
        sz = sf.get_num_items()
        if imay_item_idx == DKIX_EMPTY:
            if not xidc[probe_idx] == sz:raise logic-err
        else:
            item_idx = imay_item_idx
            if not item_idx >= 0:raise logic-err
            if not item_idx == xidc[probe_idx] == sz -1:raise logic-err

    @override
    def _push_ohitem_(sf, o, h, k, v, /):
        'old_xmay_is_dummy -> hash_value -> key -> value -> None'
        old_xmay_is_dummy = o
        if old_xmay_is_dummy: raise logic-err
        hk_ls = sf._sh.flat_hash_key_pair_array
        item_idx = sz = sf.get_num_items()
        i = item_idx<<1
        if not hk_ls[i:i+2] == (h,k):raise logic-err
        sf._vs.append(v)
    @override
    def _del_last_ohitem_(sf, /):
        '-> None'
        sf._vs.pop()
    @override
    def _get_ohitem_(sf, item_idx, /):
        'item_idx -> (old_xmay_is_dummy, hash_value, key, value)'
        hk_ls = sf._sh.flat_hash_key_pair_array
        i = item_idx<<1
        (h,k) = hk_ls[i:i+2]
        v = sf._vs[item_idx]
        o = old_xmay_is_dummy = False
        return o,h,k,v
    @override
    def _set_ohitem_(sf, item_idx, o, h, k, v, /):
        'item_idx -> old_xmay_is_dummy -> hash_value -> key -> value -> None'
        old_xmay_is_dummy = o
        if old_xmay_is_dummy: raise logic-err
        hk_ls = sf._sh.flat_hash_key_pair_array
        i = item_idx<<1
        if not hk_ls[i:i+2] == (h,k):raise logic-err
        sf._vs[item_idx] = v
#end-class DictTable__split_table_ver(IDictTable):



class DictTable__combined_table_ver(IDictTable):
    __slots__ = r'''
    _xidc
    _ohkv_ls
    _max_load
    _sz
    _nbits
    '''.split()#'''

    def __repr__(sf, /):
        ordered_attrs = 'imay_item_idx_array flat_ohitem_array size'.split()
        return repr_helper_ex(sf, sf._nbits, sf.get_num_slots(), sf._max_load, dict(imay_item_idx_array=sf._xidc, flat_ohitem_array=sf._ohkv_ls, size=sf._sz), ordered_attrs_only=True)
    def __init__(sf, num_bits4perturb_rshift, num_slots, max_load, /):
        check_power_of_2(num_slots)
        assert num_bits4perturb_rshift > 0
        sf._xidc = [DKIX_EMPTY]*num_slots
        sf._ohkv_ls = [] # *4
        sf._max_load = max_load
        sf._sz = 0
        sf._nbits = num_bits4perturb_rshift

    #dk_lookup:goto
    @override
    def iter_probe_sequence4collision_resolution(sf, num_slots, hash_value, /):
        '-> Iter probe_idx{uint%num_slots}'
        return iter_probe_sequence4collision_resolution__py_3_9_13_impl(sf._nbits, num_slots, hash_value)


    @override
    def get_num_items(sf, /):
        '-> num_items/ma_used'
        return sf._sz
    @override
    def get_max_load(sf, /):
        '-> max_load'
        return sf._max_load
    @override
    def get_load(sf, /):
        '-> load/dk_nentries'
        return len(sf._ohkv_ls)//4
    @override
    def get_num_slots(sf, /):
        '-> num_slots/dk_size'
        return len(sf._xidc)

    @override
    def _iadd_num_items_(sf, delta, /):
        'delta -> None'
        sf._sz += delta

    @override
    def _get_xmay_item_idx_(sf, probe_idx, /):
        'probe_idx -> xmay_item_idx'
        xmay_item_idx = sf._xidc[probe_idx]
        return xmay_item_idx
    @override
    def _set_xmay_item_idx_(sf, probe_idx, xmay_item_idx, /):
        'probe_idx -> xmay_item_idx -> None'
        sf._xidc[probe_idx] = xmay_item_idx

    @override
    def _push_ohitem_(sf, o, h, k, v, /):
        'old_xmay_is_dummy -> hash_value -> key -> value -> None'
        sf._ohkv_ls += [o,h,k,v]
    @override
    def _del_last_ohitem_(sf, /):
        '-> None'
        assert len(sf._ohkv_ls) >= 4
        del sf._ohkv_ls[-4:]
    @override
    def _get_ohitem_(sf, item_idx, /):
        'item_idx -> (old_xmay_is_dummy, hash_value, key, value)'
        i = item_idx*4
        o,h,k,v = sf._ohkv_ls[i:i+4]
        return o,h,k,v
    @override
    def _set_ohitem_(sf, item_idx, o, h, k, v, /):
        'item_idx -> old_xmay_is_dummy -> hash_value -> key -> value -> None'
        i = item_idx*4
        assert len(sf._ohkv_ls) >= i+4
        sf._ohkv_ls[i:i+4] = [o,h,k,v]
#end-class DictTable__combined_table_ver(IDictTable):



class Dict__mixed_table:
    #class Dict__combined_table_ver:
    #class Dict__split_table_ver:
    #class DictTable__combined_table_ver:
    #class DictTable__split_table_ver:
    'basic_modify: make_keys_shared, clear, pop, popitem, __setitem__, setdefault'
    def _get_setting_(sf, /):
        '-> setting/IDictSetting'
        return sf._setting
    def _get_table_(sf, /):
        '-> table/IDictTable'
        return sf._table
    def _set_constant_size_eq1_table_(sf, h,k,v, /):
        sf._set_table_(DictTable__size_eq1(h,k,v))
    def _set_empty_table_(sf, /):
        sf._set_table_(DictTable__empty())
    def _set_table_(sf, table, /):
        'table/IDictTable -> None'
        sf._table = table
    def _mk_resizeable_table_(sf, num_bits4perturb_rshift, num_slots, max_load, /):
        '-> resizeable-table/IDictTable'
        table = DictTable__combined_table_ver(num_bits4perturb_rshift, num_slots, max_load)
        return table
        #_resize_via_num_items

    def _is_table_constant_size_eq1_(sf, /):
        table = sf._get_table_()
        return type(table) is DictTable__size_eq1
    def _is_table_split_ver_(sf, /):
        table = sf._get_table_()
        return type(table) is DictTable__split_table_ver
    def _mk_split_table_(sf, shared_hkey_table, values, /):
        return DictTable__split_table_ver(shared_hkey_table, values)
    def make_keys_shared(sf, /):
        if not sf: raise logic-err
        if sf._is_table_split_ver_():
            return sf._get_table_().shared_hkey_table
        shared_hkey_table, values = sf._make_keys_shared()
        assert 1 <= len(sf) == len(values) == shared_hkey_table.total_keys == shared_hkey_table.load == shared_hkey_table.max_load
        sf._set_table_(sf._mk_split_table_(shared_hkey_table, values))
        return shared_hkey_table
    def _make_keys_shared(sf, /):
        #_resize_via_num_items_without_DKIX_DUMMY
        if not sf: raise logic-err
        if sf._is_table_split_ver_(): raise logic-err
        sf_without_DKIX_DUMMY = sf.copy()
        table = sf_without_DKIX_DUMMY._get_table_()
        num_slots = table.get_num_slots()
        num_items = table.get_num_items()
        imay_item_idx_array = (*map(table.probe_idx2xmay_item_idx, range(num_slots)),)
        if not min(imay_item_idx_array) == -1 == DKIX_EMPTY: raise logic-err
            #without dummy slot
            #must has empty slot
        if not max(imay_item_idx_array) == num_items-1: raise logic-err
            #nonempty
        hk_ls = []
        vs = []
        for h,k,v in table.iter_hitems(reverse=False):
            hk_ls += [h,k]
            vs.append(v)
        flat_hash_key_pair_array = (*hk_ls,)
        setting = sf_without_DKIX_DUMMY._get_setting_()
        num_bits4perturb_rshift = get_num_bits4perturb_rshift(setting)
        max_load = table.get_max_load()
        iter_probe_sequence4collision_resolution_ = iter_probe_sequence4collision_resolution__py_3_9_13_impl
        shared_hkey_table = DictSharedHKeyTable(num_bits4perturb_rshift, max_load, imay_item_idx_array, flat_hash_key_pair_array, iter_probe_sequence4collision_resolution_)
        return shared_hkey_table, vs
    make_keys_shared

    def clear(sf, /):
        if sf._is_table_split_ver_():
            table = sf._get_table_()
            table.clear_values()
        else:
            sf._set_empty_table_()
        return
    def __init__(sf, setting, may_mapping_or_items=None, /):
        check_type_le(IDictSetting, setting)
        sf._setting = setting
        sf._set_empty_table_()

        if not may_mapping_or_items is None:
            mapping_or_items = may_mapping_or_items
            if isinstance(mapping_or_items, __class__):
                ot = mapping_or_items
                if ot._is_table_split_ver_():
                    sf._set_table_(sf._mk_split_table_(ot._get_table_().shared_hkey_table, null_tuple))

            sf.update(mapping_or_items)
    def __len__(sf, /):
        return sf._get_table_().get_num_items()
    def __setitem__(sf, k, v, /):
        table = sf._get_table_()
        h = hash(k)
        if not sf:
            sf._set_constant_size_eq1_table_(h,k,v)
        else:
            (may_probe_idx4fst_dummy, probe_idx, imay_item_idx, *tmay_item) = dk_lookup(table, k, h)
            sf._tail4setitem(may_probe_idx4fst_dummy, probe_idx, imay_item_idx, h,k,v)
        return

    #push/_tail4setitem/_sf_k_may_h_probe_idx2result__setdefault/_sf_k_may_h_probe_idx2result++may_probe_idx4fst_dummy
    def _tail4setitem(sf, may_probe_idx4fst_dummy, probe_idx, imay_item_idx, h, k, v, /):
        table = sf._get_table_()
        if imay_item_idx == DKIX_EMPTY:
            if 0 == table.get_num_usable_slots():
                sf._resize_via_num_items(len(sf), overflow=True)
                table = sf._get_table_()
                (may_probe_idx4fst_dummy, probe_idx, imay_item_idx, *tmay_item) = dk_lookup(table, k, h)
            assert 0 < table.get_num_usable_slots()
            table.push(may_probe_idx4fst_dummy, probe_idx, h, k, v)
        else:
            item_idx = imay_item_idx
            table.overwrite(probe_idx, item_idx, h, k, v)


    def __delitem__(sf, k, /):
        sf.pop(k)
    def pop(sf, k, /):
        (probe_idx, item_idx, h,k,v) = sf._get_ex(k)
        if sf._is_table_split_ver_():
            if not item_idx == len(sf)-1:
                sf._resize_via_num_items(len(sf), overflow=False)
                (probe_idx, item_idx, h,k,v) = sf._get_ex(k)

        table = sf._get_table_()
        if len(sf) == 1 and sf._is_table_constant_size_eq1_():
            sf.clear()
        else:
            table.erase(probe_idx, item_idx)
                #may be empty
        return v
    def __getitem__(sf, k, /):
        (probe_idx, item_idx, h,k,v) = sf._get_ex(k)
        return v


    def _get_ex(sf, k, /):
        cls = type(sf)
        return sf._get_ex_ex(k, cls._sf_k_may_h_probe_idx2result__KeyError, cls._sf_ii_hitem2result__get_ex)
    def _sf_k_may_h_probe_idx2result__KeyError(sf, k, may_h, may_probe_idx4fst_dummy, may_probe_idx, /):
        raise KeyError(k)
    def _sf_ii_hitem2result__get_ex(sf, probe_idx, item_idx, h,k,v, /):
        return (probe_idx, item_idx, h,k,v)
    def _get_ex_ex(sf, k, _sf_k_may_h_probe_idx2result, _sf_ii_hitem2result, /, *args):
        if not sf:
            may_h = None
            may_probe_idx4fst_dummy = None
            may_probe_idx = None
            return _sf_k_may_h_probe_idx2result(sf, k, may_h, may_probe_idx4fst_dummy, may_probe_idx, *args)
            raise KeyError(k)
        h = hash(k)
        table = sf._get_table_()
        (may_probe_idx4fst_dummy, probe_idx, imay_item_idx, *tmay_item) = dk_lookup(table, k, h)
        if imay_item_idx == DKIX_EMPTY:
            return _sf_k_may_h_probe_idx2result(sf, k, h, may_probe_idx4fst_dummy, probe_idx, *args)
            raise KeyError(k)
        else:
            item_idx = imay_item_idx
            [(k,v)] = tmay_item
            return _sf_ii_hitem2result(sf, probe_idx, item_idx, h,k,v, *args)
            return (probe_idx, item_idx, h,k,v)


    def __iter__(sf, /):
        for h,k,v in sf._get_table_().iter_hitems(reverse=False):
            yield k
    def __reversed__(sf, /):
        for h,k,v in sf._get_table_().iter_hitems(reverse=True):
            yield k
    def popitem(sf, /):
        for last_k in reversed(sf):
            break
        else:
            raise KeyError('popitem(): dictionary is empty')
        (probe_idx, item_idx, h,k,v) = sf._get_ex(last_k)
        (h,k,v) = sf._get_table_().pop(probe_idx)
                #may be empty
        return k,v

    def _resize_via_num_items_without_DKIX_DUMMY(sf, num_items, /, *, overflow):
        #_without_DKIX_DUMMY required by make_keys_shared <-- copy
        if not overflow and num_items==0:
            sf.clear()
            return

        setting = sf._get_setting_()
        assert len(sf) <= num_items
        assert 1 <= num_items #since using DictTable__size_eq1
        #num_slots = calc_num_slots(setting, num_items, overflow=overflow)
        pseudo_num_slots = calc_pseudo_num_slots5num_items(setting, num_items, overflow=overflow)
        assert max(1,len(sf)) <= num_items <= num_items+bool(overflow) < pseudo_num_slots
        sf._resize_via_pseudo_num_slots_without_DKIX_DUMMY(pseudo_num_slots)
    def _resize_via_pseudo_num_slots_without_DKIX_DUMMY(sf, pseudo_num_slots, /):
        assert 2 <= pseudo_num_slots #since using DictTable__size_eq1
        assert 1 <= pseudo_num_slots
        setting = sf._get_setting_()
        num_slots = calc_num_slots5pseudo_num_slots(setting, pseudo_num_slots)
        assert 1 <= pseudo_num_slots <= num_slots
        check_power_of_2(num_slots)

        max_load = calc_max_load4num_slots(setting, num_slots)
        num_bits4perturb_rshift = get_num_bits4perturb_rshift(setting)
        table = sf._mk_resizeable_table_(num_bits4perturb_rshift, num_slots, max_load)
            #combined
            #no dummy
        _table = sf._get_table_()
        _update_table(table, _table)
        sf._set_table_(table)

    _resize_via_pseudo_num_slots = _resize_via_pseudo_num_slots_without_DKIX_DUMMY
    _resize_via_num_items = _resize_via_num_items_without_DKIX_DUMMY

    def copy(sf, /):
        #_resize_via_num_items_without_DKIX_DUMMY
        cls = type(sf)
        setting = sf._get_setting_()
        return cls(setting, sf)
    def update(sf, may_mapping_or_items=None, /, **kw):
        L = len(kw)
        if not may_mapping_or_items is None:
            mapping_or_items = may_mapping_or_items
            if hasattr(mapping_or_items, '__len__'):
                if 0 == len(mapping_or_items):
                    may_mapping_or_items = None
                #L += len(mapping_or_items)
                #if isinstance(may_mapping_or_items, Mapping):
                if hasattr(mapping_or_items, 'items'):
                    mapping = mapping_or_items
                    #xxx #L += len(mapping)
                    L = max(L,len(mapping))
                #if L == 0: return
        #end-if not may_mapping_or_items is None:
        #xxx L #== sum len mapping,kw
        L #== max len mapping,kw

        #if sf._get_table_().get_num_usable_slots() < L:
        #   sf._resize_via_num_items(len(sf)+L, overflow=False)
            # maybe shared_keys
            #   see:dict_merge(PyObject *a, PyObject *b, int override)
        if L > 0 and (not sf or sf._get_table_().get_max_load() < L):
            #not shared_keys
            sf._resize_via_num_items(len(sf)+L, overflow=False)

        if not may_mapping_or_items is None:
            mapping_or_items = may_mapping_or_items

            if hasattr(mapping_or_items, 'items'):
                mapping = mapping_or_items
                items = mapping.items()
            else:
                items = mapping_or_items
            for k,v in items:
                sf[k] = v
        #end-if not may_mapping_or_items is None:
        if kw:
            items = kw.items()
            for k,v in items:
                sf[k] = v

    @classmethod
    def _prepare4fromkeys_(cls, keys, /):
        iter(keys)
        sf = cls()

        if isinstance(keys, Set) or isinstance(keys, Mapping):
            L = len(keys)
            sf._resize_via_num_items(len(sf)+L, overflow=False)
        return sf


    @classmethod
    def fromkeys(cls, keys, xdefault=None, imay_xdefault_rank=-1, /):
        sf = cls._prepare4fromkeys_(keys)
        for k in keys:
            v = mk_default(imay_xdefault_rank, xdefault, sf, k)
            sf[k] = v



    def _sf_k_may_h_probe_idx2result__getdefault(sf, k, may_h, may_probe_idx4fst_dummy, may_probe_idx, imay_xdefault_rank, xdefault, /):
        v = mk_default(imay_xdefault_rank, xdefault, sf, k)
        return v
    def _sf_k_may_h_probe_idx2result__setdefault(sf, k, may_h, may_probe_idx4fst_dummy, may_probe_idx, imay_xdefault_rank, xdefault, /):
        v = mk_default(imay_xdefault_rank, xdefault, sf, k)
        if may_h is None:
            assert not sf
            sf[k] = v
        else:
            h = may_h
            probe_idx = may_probe_idx
            assert probe_idx is not None
            assert sf
            sf._tail4setitem(may_probe_idx4fst_dummy, probe_idx, DKIX_EMPTY, h,k,v)
        return v
    def _sf_ii_hitem2result__get(sf, probe_idx, item_idx, h,k,v, imay_xdefault_rank, xdefault, /):
        return v
    def setdefault(sf, k, xdefault=None, imay_xdefault_rank=-1, /):
        cls = type(sf)
        return sf._get_ex_ex(k, cls._sf_k_may_h_probe_idx2result__setdefault, cls._sf_ii_hitem2result__get, imay_xdefault_rank, xdefault)
    def get(sf, k, xdefault=None, imay_xdefault_rank=-1, /):
        cls = type(sf)
        return sf._get_ex_ex(k, cls._sf_k_may_h_probe_idx2result__getdefault, cls._sf_ii_hitem2result__get, imay_xdefault_rank, xdefault)

    #TODO: reverseable view??
    'items', 'keys', 'values'
    items = Mapping.items
    keys = Mapping.keys
    values = Mapping.values
    #def items(sf, /): return type({}.items())(sf)
    def __contains__(sf, k, /):
        h = hash(k) #!!!before
        #####
        if not sf:
            return False
        table = sf._get_table_()
        (may_probe_idx4fst_dummy, probe_idx, imay_item_idx, *tmay_item) = dk_lookup(table, k, h)
        return not imay_item_idx == DKIX_EMPTY
    def __ne__(sf, ot, /):
        return not sf==ot
    def __eq__(sf, ot, /):
        if not isinstance(ot, Mapping):
            return NotImplemented
        return len(ot) == len(sf) and all(ot[k]==v for k,v in sf.items())
    def __ior__(sf, ot, /):
        if not isinstance(ot, Mapping):
            return NotImplemented
        sf.update(ot)
    def __or__(sf, ot, /):
        if not isinstance(ot, Mapping):
            return NotImplemented
        d = sf.copy()
        d |= ot
        return d
    def __ror__(sf, ot, /):
        if not isinstance(ot, Mapping):
            return NotImplemented
        if not hasattr(ot, 'copy'):
            return NotImplemented
        d = ot.copy()
        for k,v in sf.items():
            d[k] = v
        return d


    def __repr__(sf, /):
        setting = sf._get_setting_()
        if not sf:
            return repr_helper(sf, setting)
        return repr_helper(sf, setting, [*sf.items()])
    make_keys_shared
'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
'__contains__', '__eq__', '__ge__', '__gt__', '__hash__', '__ior__', '__le__', '__lt__', '__ne__', '__or__', '__repr__', '__ror__'
#end-class Dict__mixed_table:
def calc_pseudo_num_slots5num_items(setting, num_items, /, *, overflow):
    check_pint(num_items) #since using DictTable__size_eq1
    if overflow:
        pseudo_num_slots = calc_min_pseudo_num_slots4num_items__on_insert_overflow_max_load(setting, num_items)
        assert num_items+1 < pseudo_num_slots
    else:
        pseudo_num_slots = calc_min_pseudo_num_slots4num_items__on_create_or_merge(setting, num_items)
    assert 1 <= num_items < pseudo_num_slots
        # one NULL slot is required to stop iter_probe_sequence4collision_resolution__py_3_9_13_impl()
    return pseudo_num_slots
def calc_num_slots5pseudo_num_slots(setting, pseudo_num_slots, /):
    check_int_ge(2, pseudo_num_slots) #since using DictTable__size_eq1
    min_num_slots = get_min_num_slots(setting)

    if pseudo_num_slots <= min_num_slots:
        num_slots = min_num_slots
    else:
        num_slots = 1<<ceil_log2(pseudo_num_slots)
        assert num_slots//2 < pseudo_num_slots <= num_slots
    assert 1 <= min_num_slots <= num_slots
    assert 2 <= pseudo_num_slots <= num_slots
    return num_slots

def _update_table(table, _table, /):
    if not table.get_num_usable_slots() >= _table.get_num_items(): raise logic-err

    for h,k,v in _table.iter_hitems(reverse=False):
        (may_probe_idx4fst_dummy, probe_idx, imay_item_idx, *tmay_item) = dk_lookup(table, k, h)
        if imay_item_idx == DKIX_EMPTY:
            table.push(may_probe_idx4fst_dummy, probe_idx, h, k, v)
        else:
            item_idx = imay_item_idx
            table.overwrite(probe_idx, item_idx, h, k, v)


#class Dict__mixed_table:


from seed.mapping_tools.example4py_dict_impl import IDictSetting, get_num_bits4perturb_rshift, get_max_presized_num_slots, get_min_num_slots, calc_max_load4num_slots, calc_min_pseudo_num_slots4num_items__on_create_or_merge, calc_min_pseudo_num_slots4num_items__on_insert_overflow_max_load

from seed.mapping_tools.example4py_dict_impl import setting__py_3_9_13_impl

from seed.mapping_tools.example4py_dict_impl import DKIX_EMPTY, DKIX_DUMMY, IDictTable, dk_lookup, iter_probe_sequence4collision_resolution__py_3_9_13_impl

from seed.mapping_tools.example4py_dict_impl import DictSharedHKeyTable

from seed.mapping_tools.example4py_dict_impl import DictTable__empty, DictTable__size_eq1, DictTable__split_table_ver, DictTable__combined_table_ver

from seed.mapping_tools.example4py_dict_impl import Dict__mixed_table

from seed.mapping_tools.example4py_dict_impl import calc_pseudo_num_slots5num_items, calc_num_slots5pseudo_num_slots

from seed.mapping_tools.example4py_dict_impl import *

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +IGNORE_EXCEPTION_DETAIL



