#__all__:goto
r'''[[[
e ../../python3_src/seed/mapping_tools/determine_num_slots4hash_map.py


源自:
    view ../../python3_src/seed/types/DictWithNewProtocol.py

seed.mapping_tools.determine_num_slots4hash_map
py -m nn_ns.app.debug_cmd seed.mapping_tools.determine_num_slots4hash_map
py -m seed.mapping_tools.determine_num_slots4hash_map

>>> from seed.mapping_tools.determine_num_slots4hash_map import IDetermineNumSlots4HashMap, determine_num_slots4hash_map



>>> from seed.mapping_tools.determine_num_slots4hash_map import _DetermineNumSlots4HashMap__xor_then_mod_prime, _hash2idx__xor_then_mod_prime
>>> from seed.mapping_tools.determine_num_slots4hash_map import _DetermineNumSlots4HashMap__mod_prime, _hash2idx__mod_prime

>>> cls = _DetermineNumSlots4HashMap__mod_prime
>>> hash2idx = _hash2idx__mod_prime
>>> f = lambda m, hs:cls(m).determine_num_slots4hash_map(hs)[::2]
>>> cls(1).determine_num_slots4hash_map([1, 3, 3, 6, 9]) == (7, hash2idx, None)
True
>>> f(1, [1, 3, 3, 6, 9])
(7, None)
>>> f(1, [1, 3, 3, 6, 10])
(11, None)
>>> f(2, [1, 3, 3, 6, 9])
(5, None)
>>> f(2, [1, 3, 3, 6, 11])
(7, None)
>>> f(1, [1, 6, 13, 24, 37])
(17, None)




>>> cls = _DetermineNumSlots4HashMap__xor_then_mod_prime
>>> hash2idx = _hash2idx__xor_then_mod_prime
>>> f = lambda m, hs:cls(m).determine_num_slots4hash_map(hs)[::2]
>>> g = lambda m, hs:h(*cls(m).determine_num_slots4hash_map(hs, _ex=1))
>>> h = lambda a,b:(a[::2], b)

>>> cls(1).determine_num_slots4hash_map([1, 3, 3, 6, 9]) == (5, hash2idx, 5)
True
>>> f(1, [1, 3, 3, 6, 9])
(5, 5)
>>> g(1, [1, 3, 3, 6, 9])
((5, 5), (((1, 1), (6, 1), (3, 2), (9, 1)), [(5, [None, 3, 9, 6, 1])]))
>>> g(1, [])
Traceback (most recent call last):
    ...
TypeError: hash_values are all the same
>>> g(1, [1])
Traceback (most recent call last):
    ...
TypeError: hash_values are all the same
>>> g(1, [1, 1])
Traceback (most recent call last):
    ...
TypeError: hash_values are all the same
>>> g(1, [1, 2])
((2, 0), (((2, 1), (1, 1)), [(2, [2, 1])]))




#]]]'''
__all__ = r'''
    IDetermineNumSlots4HashMap
    determine_num_slots4hash_map
'''.split()#'''
__all__
#from seed.types.view.SeqTransformView import SeqTransformView
from seed.tiny import fst, snd, echo, check_callable, check_type_is, check_uint
from seed.math.primes4hash_mapping import find_suitable_seq_size4hash_mapping__tabular
from seed.math.search_smallest_prime_ge_ import find_suitable_seq_size4hash_mapping__search, search_smallest_prime_ge_#, search_smallest_prime_gt_, search_largest_prime_le_, search_largest_prime_lt_
#from math import gcd
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.iters.are_all_the_same import are_all_the_same

class IDetermineNumSlots4HashMap(ABC):
    __slots__ = ()
    _max_size4lookup_list_ = 11

    @property
    @abstractmethod
    def max_num_accidental_collisions_per_slot(sf, /):
        return 3

    @abstractmethod
    def search_smallest_suitable_num_slots_ge_and_hash2idx_and_iter_selected_args_(sf, sz, /):
        'sz/pint{>=1} -> (num_slots/pint{>=sz}, hash2idx/(num_slots -> hash_value -> arg -> idx/uint%num_slots), iter_selected_args/(Iter<arg>))'
    def determine_num_slots4hash_map(sf, hash_values, /, *, key=None, **kw):
        'collection<a> -> (key :: may (a -> hash_value))/O(1) -> (num_slots, hash2idx, arg)'
        return determine_num_slots4hash_map(hash_values, key=key
        , max_num_accidental_collisions_per_slot
        = sf.max_num_accidental_collisions_per_slot
        , _max_size4lookup_list_
        = sf._max_size4lookup_list_
        , search_smallest_suitable_num_slots_ge_and_hash2idx_and_iter_selected_args_
        = sf.search_smallest_suitable_num_slots_ge_and_hash2idx_and_iter_selected_args_
        , **kw
        )
        #return (num_slots, hash2idx, arg)

class _DetermineNumSlots4HashMap__mod_prime(IDetermineNumSlots4HashMap):
    __slots__ = '_m'
    def __init__(sf, max_num_accidental_collisions_per_slot, /):
        check_pint(max_num_accidental_collisions_per_slot)
        sf._m = max_num_accidental_collisions_per_slot

    @property
    @override
    def max_num_accidental_collisions_per_slot(sf, /):
        return sf._m

    def search_smallest_suitable_num_slots_ge_and_hash2idx_and_iter_selected_args_(sf, sz, /):
        num_slots = search_smallest_prime_ge_(sz)
        prime = num_slots
        hash2idx = _hash2idx__mod_prime
        iter_selected_args = iter([None])
        return (num_slots, hash2idx, iter_selected_args)
_hash2idx__mod_prime = lambda num_slots, hash_value, _, /: (hash_value)%num_slots
class _DetermineNumSlots4HashMap__xor_then_mod_prime(_DetermineNumSlots4HashMap__mod_prime):
    __slots__ = ()

    def search_smallest_suitable_num_slots_ge_and_hash2idx_and_iter_selected_args_(sf, sz, /):
        #num_slots = find_suitable_seq_size4hash_mapping__tabular(sz)
        num_slots = search_smallest_prime_ge_(sz)
        hash2idx = _hash2idx__xor_then_mod_prime
        prime = num_slots
        iter_selected_args = iter(range(prime*3))
        return (num_slots, hash2idx, iter_selected_args)
        half = prime//2
        iter_selected_args = iter(range(1, half+1))
        return (num_slots, hash2idx, iter_selected_args)
_hash2idx__xor_then_mod_prime = lambda num_slots, hash_value, mask, /: (hash_value^mask)%num_slots

def check_pint(i, /):
    check_uint(i)
    if not i >= 1: raise TypeError
def determine_num_slots4hash_map(hash_values, /, *
    , key=None
    , max_num_accidental_collisions_per_slot
    , search_smallest_suitable_num_slots_ge_and_hash2idx_and_iter_selected_args_
    :'sz/pint{>=1} -> (num_slots/pint{>=sz}, hash2idx/(num_slots -> hash_value -> arg -> idx/uint%num_slots), iter_selected_args/(Iter<arg>))'
    , _max_size4lookup_list_ = 11
    , _ex = False
    ):
    '[a] -> (key :: may (a -> hash_value)) -> (num_slots, hash2idx, arg)'
    check_pint(max_num_accidental_collisions_per_slot)
    check_pint(_max_size4lookup_list_)
    if key is None:
        key = echo #not hash()
    check_callable(key)

    iter_hash_values_ = lambda:map(key, hash_values)
    if are_all_the_same(iter_hash_values_()): raise TypeError('hash_values are all the same')

    total = len(hash_values)

    if total < 2: raise logic-err
    if total < 2:
        num_slots = total
        hash2idx = lambda num_slots, hash_value, mask, /: 0
        arg = None
        return (num_slots, hash2idx, arg)
        return (total, 1)


    #if key is not None: hash_values = SeqTransformView(key, hash_values)



    def f(sz, /):
        (num_slots, hash2idx, iter_args) = search_smallest_suitable_num_slots_ge_and_hash2idx_and_iter_selected_args_(sz)
        check_type_is(int, num_slots)
        if not num_slots >= sz: raise ValueError
        check_callable(hash2idx)
        iter_args = iter(iter_args)
        return (num_slots, hash2idx, iter_args)

    #(num_slots, hash2idx, iter_args) = f(total)
    if 1:
        num_slots = find_suitable_seq_size4hash_mapping__tabular(total)
        def hash2idx(num_slots, hash_value, scale, /):
            assert scale==1
            return hash_value%num_slots
        iter_args = iter([1])

    idx2slot = [None]*num_slots
        # slot = None | hash | [hash, count, ...] | {hash:count}
        #   None -> {}
        #   hash -> {hash:1}
    [_1] = _count_hash_values(iter_hash_values_, _max_size4lookup_list_, idx2slot, num_slots, hash2idx, iter_args, lambda:True)

    h_count_pairs = (*_iter_idx2slot_as_hash_and_count(idx2slot),)
    assert sum(map(snd, h_count_pairs)) == total
    if 1:
        #for iter_hash_values_
        iter_hash_values_
        hash_values = h_count_pairs
        key = fst
    num_diff_hash_values = len(h_count_pairs)
    assert 2 <= num_diff_hash_values <= total
    #print(h_count_pairs)

    def is_ok_():
        assert sum(map(snd, _iter_idx2slot_as_hash_and_count(idx2slot))) == num_diff_hash_values
        return max(_iter_idx2slot_as_sz(idx2slot)) <= max_num_accidental_collisions_per_slot


    if _ex:
        num_slots__idx2slot__pairs = []
        g = num_slots__idx2slot__pairs.append
    else:
        g = echo

    del idx2slot[num_diff_hash_values-1:]
        #since below:len(idx2slot)+1
    while 1:
        (num_slots, hash2idx, iter_args) = f(len(idx2slot)+1)

        #_erase_idx2slot(idx2slot)
        tmay_arg = _count_hash_values(iter_hash_values_, _max_size4lookup_list_, idx2slot, num_slots, hash2idx, iter_args, is_ok_)
        g((num_slots, [*idx2slot]))
        if tmay_arg:
            break

    [arg] = tmay_arg
    if _ex:
        unordered_hash_value_count_pairs = h_count_pairs
        return ((num_slots, hash2idx, arg), (unordered_hash_value_count_pairs, num_slots__idx2slot__pairs))
    return (num_slots, hash2idx, arg)



def _iter_idx2slot_as_sz(idx2slot, /):
    for idx, slot in enumerate(idx2slot):
        if slot is None:
            continue
        cls = type(slot)
        if cls is int:
            sz4lookup_list = 1
        elif cls is list:
            lookup_list = slot
            L = len(lookup_list)
            sz4lookup_list = L//2
        else:
            assert cls is dict
            h2count = slot
            sz4lookup_list = len(h2count)
        yield sz4lookup_list

def _iter_idx2slot_as_hash_and_count(idx2slot, /):
    for idx, slot in enumerate(idx2slot):
        if slot is None:
            continue
        cls = type(slot)
        if cls is int:
            _hash_value = slot
            _count = 1
            yield (_hash_value, _count)
            continue
            h2count = {_hash_value:_count}
        elif cls is list:
            lookup_list = slot
            L = len(lookup_list)
            yield from (zip(lookup_list[0::2], lookup_list[1::2]))
            continue
            h2count = dict(zip(lookup_list[0::2], lookup_list[1::2]))
        else:
            assert cls is dict
            h2count = slot
            yield from h2count.items()
        #yield idx, h2count
def _put(_max_size4lookup_list_, idx2slot, idx, hash_value, /):
    assert idx >= 0
    slot = idx2slot[idx]
    if slot is None:
        idx2slot[idx] = hash_value
        return
    cls = type(slot)
    if cls is int:
        _hash_value = slot
        _count = 1
        sz4lookup_list_ = 1
        if _max_size4lookup_list_ < sz4lookup_list_:
            slot = idx2slot[idx] = {_hash_value:_count}
        else:
            slot = idx2slot[idx] = [_hash_value, _count]
        cls = type(slot)
    ###
    if cls is list:
        lookup_list = slot
        L = len(lookup_list)
        for i in range(0, L, 2):
            if lookup_list[i] == hash_value:
                lookup_list[i+1] += 1
                break
        else:
            count = 1
            lookup_list += [hash_value, count]
            if L//2 == _max_size4lookup_list_:
                slot = idx2slot[idx] = dict(zip(lookup_list[0::2], lookup_list[1::2]))
    else:
        assert cls is dict
        h2count = slot
        if hash_value in h2count:
            h2count[hash_value] += 1
        else:
            h2count[hash_value] = 1

def _erase_idx2slot(idx2slot, /):
    for i in range(len(idx2slot)):
        idx2slot[i] = None
def _count_hash_values(iter_hash_values_, _max_size4lookup_list_, idx2slot, num_slots, hash2idx, iter_args, is_ok_, /):
    #for scale in coprimes4num_slots:
    #    if not gcd(scale, num_slots) == 1: raise ValueError
    #    for hash_value in iter_hash_values:
    #        idx = (hash_value*scale)%num_slots
    if len(idx2slot) < num_slots:
        idx2slot.extend(None for _ in range(num_slots-len(idx2slot)))
    else:
        del idx2slot[num_slots:]
    assert len(idx2slot) == num_slots

    for arg in iter_args:
        _erase_idx2slot(idx2slot)
        for hash_value in iter_hash_values_():
            idx = hash2idx(num_slots, hash_value, arg)
            check_type_is(int, idx)
            if not 0 <= idx < num_slots: raise ValueError
            _put(_max_size4lookup_list_, idx2slot, idx, hash_value)
        if is_ok_():
            return (arg,)
    return ()


from seed.mapping_tools.determine_num_slots4hash_map import IDetermineNumSlots4HashMap, determine_num_slots4hash_map
from seed.mapping_tools.determine_num_slots4hash_map import *
from seed.mapping_tools.determine_num_slots4hash_map import _DetermineNumSlots4HashMap__xor_then_mod_prime, _hash2idx__xor_then_mod_prime
from seed.mapping_tools.determine_num_slots4hash_map import _DetermineNumSlots4HashMap__mod_prime, _hash2idx__mod_prime

_DetermineNumSlots4HashMap__xor_then_mod_prime(2).determine_num_slots4hash_map([1, 3, 3, 6, 9])

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +IGNORE_EXCEPTION_DETAIL


