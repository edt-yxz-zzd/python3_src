

'''
NOTE:
    time (O(L^2) if table not cached else O(L)) * Catalan_number(L).'+'
    = time O(L^3) if table not cached else O(L^2)
    very slow!!!


see: canonical_Cartesian_tree_definition.py :: "Right Open"
see: ballot_number.py :: "encode canonical_Cartesian_tree" :: [(append|pop)]

encode_canonical_Cartesian_tree_of_array_of_fixed_length

'''


__all__ = '''
    encode_canonical_Cartesian_tree_of_array_of_fixed_length
    '''.split()

from .canonical_Cartesian_tree_of_array_to_balanced_Dyck_word import\
    canonical_Cartesian_tree_of_array_to_balanced_Dyck_word
from ..ballot_number.encode_Dyck_word import\
    encode_Dyck_word_with_fixed_num_closes_opens



def encode_canonical_Cartesian_tree_of_array_of_fixed_length(
        iterable, encoding):
    ''':: Ord a => Iter a -> encoding -> UInt

let L = len input
time (O(L^2) if table not cached else O(L)) * Catalan_number(L).'+'
    = time O(L^3) if table not cached else O(L^2)
    # from:
    canonical_Cartesian_tree_of_array_to_balanced_Dyck_word
        time O(L)
    encode_Dyck_word_with_fixed_num_closes_opens
        time (O(L^2) if table not cached else O(L)) * Catalan_number(L).'+'
        = time O(L^3) if table not cached else O(L^2)

input:
    iterable :: Ord a => Iter a
    encoding :: 'keyPQ' | 'keyQP' | IPosMoveEncoder
        see: encode_Dyck_word::IPosMoveEncoder
output:
    encode_uint <- [0..Catalan_number(len input)-1]




Ord a => each array :: [a] has a canonical_Cartesian_tree
    (pure partial-oriented-rooted-binary-tree)
    size canonical_Cartesian_tree == len array
and all canonical_Cartesian_trees of same length arrays can be encoded into
    [0..Catalan_number(len array)-1]


example:
    >>> from ..ballot_number.ballot_number import ballot_number__by_direct_calc as ballot
    >>> this = encode_canonical_Cartesian_tree_of_array_of_fixed_length
    >>> encoding = 'keyPQ'
    >>> this([], encoding)
    0
    >>> this([3], encoding)
    0
    >>> this([0,1,2,3], encoding)
    0
    >>> this([3,2,1,0], encoding) == ballot(4,4)-1
    True
'''
    iter_Dyck_word = canonical_Cartesian_tree_of_array_to_balanced_Dyck_word(iterable)
    offset, (num_closes, num_opens) = encode_Dyck_word_with_fixed_num_closes_opens(iter_Dyck_word, encoding)
    assert 0 <= num_closes == num_opens # since balanced
    return offset



if __name__ == "__main__":
    import doctest
    doctest.testmod()



