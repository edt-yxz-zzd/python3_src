


__all__ = '''
    calc_normal_block_types_and_may_rmqs
    calc_normal_block_type
    '''.split()



from .canonical_Cartesian_tree.encode_canonical_Cartesian_tree_of_array_of_fixed_length import \
    encode_canonical_Cartesian_tree_of_array_of_fixed_length
from .LeftBiasedRangeMinimumQuery__via_power_table import \
    LeftBiasedRangeMinimumQuery__via_power_table
from .ballot_number.Catalan_number import Catalan_number
from .common_methods import calc_num_blocks, ceil_div
from itertools import count

BasicRMQ = LeftBiasedRangeMinimumQuery__via_power_table


def calc_normal_block_type(normal_block, encoding):
    '''calc_normal_block_type :: Ord a => [a] -> encoding -> NormalBlockType
    # :: normal_block -> encoding -> normal_block_type

let L = len(input)

time (O(L^2) if table not cached else O(L)) * Catalan_number(L).'+'
    = time O(L^3) if table not cached else O(L^2)
output ~ space bit size O(L)

input:
    normal_block :: Ord a => [a]
    encoding = 'keyPQ' or 'keyQP'
        see: encode_canonical_Cartesian_tree_of_array_of_fixed_length
output:
    normal_block_type :: NormalBlockType
  where NormalBlockType = UInt[0..Catalan_number(len(input))-1]

'''
    return encode_canonical_Cartesian_tree_of_array_of_fixed_length(
            normal_block, encoding)

def calc_normal_block_types_and_may_rmqs(
        array, complete_normal_block_size, encoding='keyPQ'):
    ''':: Ord a => [a] -> PInt -> ([NormalBlockType], [Maybe BasicRMQ])


input:
    array :: Ord a => [a]
    s = complete_normal_block_size :: PInt
    encoding = 'keyPQ' or 'keyQP'
        see: encode_canonical_Cartesian_tree_of_array_of_fixed_length
output:
    T = normal_block_types :: [NormalBlockType]
        # Map NormalBlockIdx NormalBlockType
        # see: calc_normal_block_type
        len(T) == num_normal_blocks
        # normal_block_idx2normal_block_type

    P = precomputed_InNormalBlock_query_table :: [Maybe BasicRMQ]
        # Map NormalBlockType (None | BasicRMQ<s>)
        # see: make_left_biased_range_minimum_query_power_table
        # see: LeftBiasedRangeMinimumQuery__via_power_table


  where NormalBlockType = UInt[0..Catalan_number(len(input))-1]



################ time and space
see: "rmq - 2.3. P T.txt"
let p = len(array)
  * P
    # time and space independent with p
    time(P) = O(4^s)*(a.'<=' + uint[:s].'+-')
            ########### if s = log2(p)/2_y
            = O(p)*(a.'<=' + uint[:s].'+-')
    space(P) = O(4^s)*bit
             ########## if s = log2(p)/2_y
             = O(p)*bit
  * T
    time(T) = O(p + s^2) * Catalan_number(s).'+'
            ########### if s = log2(p)/2_y
            = O(p) * uint[..p].'+'
    space(T) = O(2p)*bit

    ########## eval
    if Catalan_number(s) <= p/s <= MAX_ARRAY_LEN <= MACHINE_WORD_MAX
        ==>> Catalan_number(s).'+' ~ time O(1) instead of O(s)
        ==>> s <= WORD_BITS/2
        # complete_normal_block_size is very small, e.g. <= 32
    time(T) = O(p/s * encode + table_init)
        = O(p/s * s + s^2) * Catalan_number(s).'+'
        = O(p + s^2) * Catalan_number(s).'+'
        ###### if s = log2(p)/2_y
        = O(p) * Catalan_number(s).'+'
        <= O(p) * uint[..p].'+'

    bit_size_of(T) = num_normal_blocks * bit_size_of Catalan_number(s)
        ~ p/s * 2*s
        ~ 2p

'''
    p = len(array)
    s = complete_normal_block_size
    if not 1 <= s <= p: raise ValueError

    P = [None] * Catalan_number(s)
    T = []

    num_normal_blocks = calc_num_blocks(p, s)
    #bug:for begin, end in zip(count(0, s), count(s, s)):
    for begin, end in zip(range(0, p, s), count(s, s)):
        normal_block = array[begin:end]
        #bug: len(normal_block) may not s
        if len(normal_block) < s:
            assert p < end
            assert normal_block
            assert begin < p < end
            assert begin + s == end
            #pad = _max = max(normal_block)
            pad = 0
            normal_block = (*normal_block, *[pad]*(end-p))
            assert len(normal_block) == s
        assert len(normal_block) == s
        normal_block_type = calc_normal_block_type(normal_block, encoding)
        T.append(normal_block_type)

        if P[normal_block_type] is None:
            P[normal_block_type] = BasicRMQ(normal_block)
    assert len(T) == num_normal_blocks
    return T, P




