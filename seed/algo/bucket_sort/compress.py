

__all__ = '''
    compress
    compress_group
    '''.split()
from seed.constant import WORD_BITS

from .bucket_group_with_table import bucket_group as _bucket_group
from .sparse_big_uints2iter_groups import sparse_big_uints2iter_groups
from itertools import groupby
def bucket_group(alphabet_size, iterable, *, key, with_key):
    return _bucket_group(alphabet_size, iterable, key=key, with_key=with_key)


def compress(array, min_old_key, max_old_key, *, key=None, with_element=False):
    ''':: (a->OldKey) -> [a] -> (new_alphabet_size, [NewKey])
    where OldKey = UInt = NewKey

why?
    #solid uint array
    e.g. when we want to compute suffix tree/SA/LCP of a unicode string:
        the alphabet_size is very large
        usually, len(array) < alphabet_size == 0x110000
        time(SA/LCP) = O(len(array) + alphabet_size)
        we may want to reduce the alphabet_size before do the work
input:
    array :: [a]
    min_old_key :: UInt
    max_old_key :: UInt
        0 <= min_old_key <= max_old_key
        all(min_old_key <= k <= max_old_key for k in map(key, array))
        why need min_old_key, max_old_key?
            since assume max_old_key is very large
                should avoid max_old_key."< -"
        see: seed.iters.minmax :: maybe_minmax/minmax_default
    key :: None | (a -> OldKey)
    with_element :: bool = False
        affect output

output:
    new_alphabet_size :: UInt
        new_alphabet_size == 1 + max(map(fst, new_key_element_pairs), default=-1)
    new_list :: [(NewKey, a)] if with_element else [NewKey]
        if with_element:
            new_list is new_key_element_pairs
            pairs = new_list
        else:
            new_list is new_keys
            pairs = zip(new_list, array)
        all(new_key <= key(element) for new_key, element in pairs)
        is_uint_onto_array(new_alphabet_size, pairs, key=fst)

see:
    is_uint_onto_array


example:
    >>> this = compress
    >>> this([], 0, 0, key=None)
    (0, [])
    >>> this([0,0,0], 0, 0, key=None)
    (1, [0, 0, 0])
    >>> this([0,0,0], 1, 1, key=lambda k:k+1)
    (1, [0, 0, 0])
    >>> this([0,0,2,3,2,2,0], 1, 4, key=lambda k:k+1)
    (3, [0, 0, 1, 2, 1, 1, 0])
    >>> this([0,0,2,3,2,2,0], 100, 103, key=lambda k:k+100)
    (3, [0, 0, 1, 2, 1, 1, 0])

    >>> this([0,0,2,3,2,2,0], 100, 103, key=lambda k:k+100, with_element=True)
    (3, [(0, 0), (0, 0), (1, 2), (2, 3), (1, 2), (1, 2), (0, 0)])

problem:
    # impl = 3 cases
    let L = len(array)
    let Rng = max_old_key-min_old_key+1
    if sorted by bucket sort:
        should use table with length at least Rng
        <= time O(L+Rng)*ops + O(L)*max_old_key.'-'

    if sorted by sparse_big_uints2iter_groups:
        = time O(num_bits of all old keys)*ops
        <= O(L*log2(max_old_key))*ops
        # even max_old_key <= MAX_MACHINE_WORD
        #   we can not replace log2(max_old_key)
        #       since this is not an basic ops
        # v.s. comparison

    if sorted by comparison:
        = O(L*log(L))*Rng."<" + O(L)*max_old_key."- <"
        = O(L*log(L)*log2(Rng)/WORD_BITS)*ops + O(L*log2(max_old_key)/WORD_BITS)*ops

        but if Rng <= MAX_MACHINE_WORD
        the Rng."<" can be O(1)*ops
        = O(L*log(L))*ops + O(L*log2(max_old_key))*ops
        if max_old_key <= MAX_MACHINE_WORD
        = O(L*log(L))*ops


'''
    input_size = len(array)
    keyed_groups = compress_group(
        array, min_old_key, max_old_key, key=key
        , with_element=with_element
        , with_key=True)
    new_alphabet_size = len(keyed_groups)
    output = [None]*input_size

    if with_element:
        def handle_group(new_key, input_idx_element_pairs):
            for input_idx, element in input_idx_element_pairs:
                output[input_idx] = (new_key, element)
    else:
        def handle_group(new_key, input_indices):
            for input_idx in input_indices:
                output[input_idx] = new_key

    for new_key, (old_key, group) in enumerate(keyed_groups):
        assert new_key <= old_key
        handle_group(new_key, group)

    return (new_alphabet_size, output)


def compress_group(array, min_old_key, max_old_key
        , *, key=None, with_element=False, with_key=True):
    r''':: (a->Key) -> [a] -> [(Key, [InputIdx])]
    where Key = UInt = InputIdx

input:
    array :: [a]
    min_old_key :: UInt
    max_old_key :: UInt
        min_old_key <= max_old_key
        all(min_old_key <= k <= max_old_key for k in map(key, array))
    key :: None | (a -> OldKey)
    with_element :: bool = False
        affect output
    with_key :: bool = True
        affect output

output:
    result :: [(Key, Group)] if with_key else [Group]
        # groups | keyed_groups
        Group = [(InputIdx, a)] if with_element else [InputIdx]
        let new_alphabet_size = len(keyed_groups)
        map(fst, keyed_groups) == range(new_alphabet_size)

        if with_element:
            keyed_groups is keyed_groups__with_element
        else:
            keyed_groups is keyed_groups__without_element
            input_idx2with_element = \i->(i, array[i])
            keyed_groups__with_element = ((k, map(input_idx2with_element, g))
                                    for k, g in keyed_groups__without_element)
        all(key == key(element)
            for key, pairs in keyed_groups__with_element
            for input_idx, element in pairs)
        all(is_strict_sorted(map(fst, pairs)) # input_idx is growing
            for key, pairs in keyed_groups__with_element
            )


example:
    >>> this = compress_group
    >>> this([], 0, 0, key=None)
    []
    >>> this([0,0,0], 0, 0, key=None)
    [(0, [0, 1, 2])]
    >>> this([0,0,0], 1, 1, key=lambda k:k+1)
    [(1, [0, 1, 2])]
    >>> this([0,0,2,3,2,2,0], 1, 4, key=lambda k:k+1)
    [(1, [0, 1, 6]), (3, [2, 4, 5]), (4, [3])]
    >>> this([0,0,2,3,2,2,0], 100, 103, key=lambda k:k+100)
    [(100, [0, 1, 6]), (102, [2, 4, 5]), (103, [3])]

    >>> this([0,0,2,3,2,2,0], 100, 103, key=lambda k:k+100, with_key=False)
    [[0, 1, 6], [2, 4, 5], [3]]
    >>> this([0,0,2,3,2,2,0], 100, 103, key=lambda k:k+100, with_key=False, with_element=True)
    [[(0, 0), (1, 0), (6, 0)], [(2, 2), (4, 2), (5, 2)], [(3, 3)]]
    >>> this([0,0,2,3,2,2,0], 100, 103, key=lambda k:k+100, with_element=True)
    [(100, [(0, 0), (1, 0), (6, 0)]), (102, [(2, 2), (4, 2), (5, 2)]), (103, [(3, 3)])]
'''
    if not 0 <= min_old_key <= max_old_key: raise ValueError
    # assume max_old_key may be very large
    # avoid max_old_key."<"
    #if not all(min_old_key <= k <= max_old_key for k in map(key, array)): raise ValueError


    #if key is None: key = echo
    L = len(array)
    Rng = max_old_key - min_old_key + 1

    log2_max_old_key = max_old_key.bit_length()
    log2_L = L.bit_length()
    log2_Rng = Rng.bit_length()
    time_max_old_key__lt__sub = max(1, log2_max_old_key//WORD_BITS)
    time_Rng_cmp = max(1, log2_Rng//WORD_BITS)

    time_by_bucket_sort = L + Rng + L * time_max_old_key__lt__sub
    time_by_sparse_big_uints2iter_groups = L * log2_max_old_key
    time_by_comparison_sort = L*log2_L*time_Rng_cmp + L*time_max_old_key__lt__sub

    time_by_bucket_sort *= 1
    time_by_sparse_big_uints2iter_groups *= 4
    time_by_comparison_sort *= 2

    times = [ time_by_bucket_sort
            , time_by_sparse_big_uints2iter_groups
            , time_by_comparison_sort]
    min_time = min(times)
    min_idx = times.index(min_time)

    if min_idx == 0:
        assert min_time == time_by_bucket_sort
        f = compress_group__by_bucket_sort
    elif min_idx == 1:
        assert min_time == time_by_sparse_big_uints2iter_groups
        f = compress_group__by_sparse_big_uints2iter_groups
    elif min_idx == 2:
        assert min_time == time_by_comparison_sort
        f = compress_group__by_comparison_sort
    else:
        raise logic-error
    keyed_groups__without_element = f(array, min_old_key, max_old_key, key=key)

    if with_element:
        input_idx2with_element = lambda i: (i, array[i])
        for key, group in keyed_groups__without_element:
            for i in range(len(group)):
                input_idx = group[i]
                group[i] = input_idx2with_element(input_idx)
        keyed_groups__with_element = keyed_groups__without_element
        del keyed_groups__without_element
        keyed_groups = keyed_groups__with_element
    else:
        keyed_groups = keyed_groups__without_element

    if with_key:
        result = keyed_groups
    else:
        for i in range(len(keyed_groups)):
            _, g = keyed_groups[i]
            keyed_groups[i] = g
        groups = keyed_groups; del keyed_groups
        result = groups
    return result

def make_shift_key(min_old_key, max_old_key, key):
    # -> ((None | shift_key | non_shift_key), (None | unshift_key))
    if min_old_key > 3:
        # shift key
        if key is not None:
            shift_key = lambda a: key(a) - min_old_key
        else:
            shift_key = lambda k: k - min_old_key
        unshift_key = lambda k: k + min_old_key
    else:
        # not shift key
        # maybe None
        shift_key = key
        unshift_key = None
    return shift_key, unshift_key
def make_input_idx2key(array, key_more):
    if key_more is None:
        input_idx2key = lambda i: array[i]
    else:
        input_idx2key = lambda i: key_more(array[i])
    return input_idx2key


def compress_group__by_bucket_sort(array, min_old_key, max_old_key, *, key):
    '''
    # with_element = False
    # -> [(Key, [InputIdx])]

example:
    >>> this = compress_group__by_bucket_sort
    >>> this([], 0, 0, key=None)
    []
    >>> this([0,0,0], 0, 0, key=None)
    [(0, [0, 1, 2])]
    >>> this([0,0,0], 1, 1, key=lambda k:k+1)
    [(1, [0, 1, 2])]
    >>> this([0,0,2,3,2,2,0], 1, 4, key=lambda k:k+1)
    [(1, [0, 1, 6]), (3, [2, 4, 5]), (4, [3])]
    >>> this([0,0,2,3,2,2,0], 100, 103, key=lambda k:k+100)
    [(100, [0, 1, 6]), (102, [2, 4, 5]), (103, [3])]
'''

    key_more, unshift_key = make_shift_key(min_old_key, max_old_key, key)
    input_idx2key = make_input_idx2key(array, key_more)

    L = len(array)
    #bug: alphabet_size = max_old_key - min_old_key + 1
    #   may not shift
    alphabet_size = max_old_key + 1 if key_more is None else key_more(max_old_key) + 1
    #print([*map(input_idx2key, range(L))])
    #print(alphabet_size)
    keyed_groups = bucket_group(alphabet_size, range(L), key=input_idx2key, with_key=True)
    unshift_keyed_groups(keyed_groups, unshift_key)
    return keyed_groups
def compress_group__by_sparse_big_uints2iter_groups(
        array, min_old_key, max_old_key, *, key):
    '''
    # with_element = False
    # -> [(Key, [InputIdx])]

example:
    >>> this = compress_group__by_sparse_big_uints2iter_groups
    >>> this([], 0, 0, key=None)
    []
    >>> this([0,0,0], 0, 0, key=None)
    [(0, [0, 1, 2])]
    >>> this([0,0,0], 1, 1, key=lambda k:k+1)
    [(1, [0, 1, 2])]
    >>> this([0,0,2,3,2,2,0], 1, 4, key=lambda k:k+1)
    [(1, [0, 1, 6]), (3, [2, 4, 5]), (4, [3])]
    >>> this([0,0,2,3,2,2,0], 100, 103, key=lambda k:k+100)
    [(100, [0, 1, 6]), (102, [2, 4, 5]), (103, [3])]
'''

    key_more = key
    input_idx2key = make_input_idx2key(array, key_more)

    L = len(array)
    it = sparse_big_uints2iter_groups(
        list(range(L)), key=input_idx2key, with_key=True)
    return list(it)

[*r] = sparse_big_uints2iter_groups(range(3), key=lambda i: 0, with_key=True)
assert r == [(0, [0, 1, 2])]
def compress_group__by_comparison_sort(array, min_old_key, max_old_key, *, key):
    '''
    # with_element = False
    # -> [(Key, [InputIdx])]

example:
    >>> this = compress_group__by_comparison_sort
    >>> this([], 0, 0, key=None)
    []
    >>> this([0,0,0], 0, 0, key=None)
    [(0, [0, 1, 2])]
    >>> this([0,0,0], 1, 1, key=lambda k:k+1)
    [(1, [0, 1, 2])]
    >>> this([0,0,2,3,2,2,0], 1, 4, key=lambda k:k+1)
    [(1, [0, 1, 6]), (3, [2, 4, 5]), (4, [3])]
    >>> this([0,0,2,3,2,2,0], 100, 103, key=lambda k:k+100)
    [(100, [0, 1, 6]), (102, [2, 4, 5]), (103, [3])]
'''
    key_more, unshift_key = make_shift_key(min_old_key, max_old_key, key)
    input_idx2key = make_input_idx2key(array, key_more)

    L = len(array)
    sorted_input_indices = sorted(range(L), key=input_idx2key)
    keyed_groups = [(k, list(g)) for k, g in groupby(sorted_input_indices, key=input_idx2key)]
    #bugs: return keyed_groups
    #   should add min_old_key back

    unshift_keyed_groups(keyed_groups, unshift_key)
    return keyed_groups

def unshift_keyed_groups(keyed_groups, unshift_key):
    if unshift_key is None: return
    for i in range(len(keyed_groups)):
        k, g = keyed_groups[i]
        keyed_groups[i] = unshift_key(k), g

assert compress_group__by_comparison_sort([0,0,2,3,2,2,0], 100, 103, key=lambda k:k+100) == [(100, [0, 1, 6]), (102, [2, 4, 5]), (103, [3])]
assert compress_group__by_bucket_sort([0,0,2,3,2,2,0], 1, 4, key=lambda k:k+1) == [(1, [0, 1, 6]), (3, [2, 4, 5]), (4, [3])]

if __name__ == "__main__":
    import doctest
    doctest.testmod()



