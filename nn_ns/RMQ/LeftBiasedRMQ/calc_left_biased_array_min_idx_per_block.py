

__all__ = '''
    calc_left_biased_array_min_idx_per_block
    iter_left_biased_array_min_idx_per_block
    iter_offseted_left_biased_array_min_idx_per_block
    left_biased_minimum_query
    '''.split()

from itertools import islice, count
from operator import add

def left_biased_minimum_query(head, iter_tail):
    ''':: Ord a => a -> Iter a -> UInt

what?
    query the minimum element index of [head, **iter_tail]

time O(L) * (a.'<' + uint[..L].'+') + O(1) * tail.'iter'
see: left_biased_range_minimum_query_definition.py


example:
    >>> this = left_biased_minimum_query
    >>> this('1', '')
    0
    >>> this('1', '2')
    0
    >>> this('1', '0')
    1
    >>> this('1', '20')
    2
    >>> this('1', '02')
    1
    >>> this('1', '32')
    0
'''
    min_idx = 0
    min_x = head
    for i, x in enumerate(iter_tail, 1):
        if x < min_x:
            min_idx = i
            min_x = x
    return min_idx


def calc_left_biased_array_min_idx_per_block(iterable, block_size):
    ''':: Ord a => Iter a -> [ArrayIdx]

what?
    query the minimum element index of each block
        # index of the whole array, not index of the block subarray

time and space:
    let L = len elements
    let B = block_size

    time O(L) * (a.'<' + uint[..L].'+') + O(1) * elements.'iter'
    output ~ space bit size O(L/B * log(L))


how?
    output = list(iter_left_biased_array_min_idx_per_block(input, block_size))

see: iter_left_biased_array_min_idx_per_block


example:
    >>> this = calc_left_biased_array_min_idx_per_block
    >>> this('', 3)
    []
    >>> this('12', 3)
    [0]
    >>> this('312', 3)
    [1]
    >>> this('123406', 3)
    [0, 4]
    >>> this('1234560', 3)
    [0, 3, 6]
'''
    it = iter_left_biased_array_min_idx_per_block(iterable, block_size)
    return list(it)

def iter_left_biased_array_min_idx_per_block(iterable, block_size):
    ''':: Ord a => Iter a -> Iter ArrayIdx


what?
    query the minimum element index of each block
        # index of the whole array, not index of the block subarray

time and space:
    let L = len elements
    let B = block_size

    time O(L) * (a.'<' + uint[..L].'+') + O(1) * elements.'iter'
    list(output) ~ space bit size O(L/B * log(L))

how?
    add offset to result of iter_offseted_left_biased_array_min_idx_per_block
see: iter_offseted_left_biased_array_min_idx_per_block
'''
    it = iter_offseted_left_biased_array_min_idx_per_block(iterable, block_size)
    offsets = count(0, block_size)
    return map(add, offsets, it)


def iter_offseted_left_biased_array_min_idx_per_block(iterable, block_size):
    ''':: Ord a => Iter a -> Iter SubArrayIdx


what?
    query the minimum element index of each block
        # index of the block subarray, not index of the whole array

time and space:
    let L = len elements
    let B = block_size

    time O(L) * (a.'<' + uint[..B].'+') + O(1) * elements.'iter'
    list(output) ~ space bit size O(L/B * log(B))

input:
    elements :: Ord a => Iter a
    block_size :: PInt
output:
    array_min_indices :: Iter ArrayIdx
        len(array_min_indices) == ceil(len(elements)/block_size)
        for i in range(len(array_min_indices)):
            block = elements[block_size*i: block_size*(i+1)]
            m = min(block)
            offseted_left_biased_min_idx = block.index(m)
            assert array_min_indices[i] == offseted_left_biased_min_idx

see: left_biased_minimum_query

example:
    >>> this = iter_offseted_left_biased_array_min_idx_per_block
    >>> list_this = lambda it, block_size: list(this(it, block_size))
    >>> list_this('', 3)
    []
    >>> list_this('12', 3)
    [0]
    >>> list_this('312', 3)
    [1]
    >>> list_this('123406', 3)
    [0, 1]
    >>> list_this('1234560', 3)
    [0, 0, 0]


'''
    if not block_size > 0: raise ValueError
    it = iter(iterable)
    tail_size = block_size-1
    for block_head in it:
        block_tail = islice(it, tail_size)
        offseted_left_biased_min_idx = left_biased_minimum_query(block_head, block_tail)
        yield offseted_left_biased_min_idx



if __name__ == "__main__":
    import doctest
    doctest.testmod()


