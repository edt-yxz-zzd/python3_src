
__all__ = ['LeftBiasedRangeMinimumQuery__via_power_table']
from .make_left_biased_range_minimum_query_power_table import\
    make_left_biased_range_minimum_query_power_table



class LeftBiasedRangeMinimumQuery__via_power_table:
    '''"left-biased" means return min idx of all min elements in given range
    see: left_biased_range_minimum_query_definition


why?
    1) to implement RMQ when p < min_array_length
    2) to implement the virtual super_min_array RMQ
    see: [Range_Minimum_Query_2007]A_New_Succinct_Representation_of_RMQ_Information_and_Improvements_in_the_Enhanced_Suffix_Array.pdf
how?
    given a range (begin, end) where 0 <= begin < end <= len(input_array) == n
    # decompose into two ranges, may overlap
    calc power, s.t.
        begin <= end-2**power <= begin+2**power <= end
        i.e. (begin,begin+2**power) overlap or touch (end-2**power,end)
        # O(log(n))

    min_idx1 = lookup_RMQ(begin, begin+2**power)
    min_idx2 = lookup_RMQ(end-2**power, end)
        # lookup_RMQ implemented by a power_table
        # whose init is O(n*log(n))
    compare min_idx1 min_idx2
    DONE!

###############
time and space
    let n = len(input_array)
    query time:
        time O(1)*(uint[..up_to_length].'bit_length <<' + uint[..n].'-')
        # see: .left_biased_range_minimum_query for details
    init time:
        # see: make_left_biased_range_minimum_query_power_table
        time O(n*log(up_to_length)) * (a.'<=' + uint[:n].'+-')
    space
        if offset:  O(n*log(up_to_length)**2)*bit
        else:       O(n*log(up_to_length)*log(n))*bit

#############
see: array_to_idx2depth_in_canonical_Cartesian_tree
    since each query need a compare,
        we may want to compare uint instead


#############
example:
    >>> This = LeftBiasedRangeMinimumQuery__via_power_table
    >>> rmq = This([1])
    >>> rmq.left_biased_range_minimum_query(0,1)
    0
    >>> rmq = This([2,1])
    >>> rmq.left_biased_range_minimum_query(0,1)
    0
    >>> rmq.left_biased_range_minimum_query(0,2)
    1
    >>> rmq = This([1,2])
    >>> rmq.left_biased_range_minimum_query(0,2)
    0

    #                              [8,9,9,11,11,11,11]
    #              [0,1,1,3,3,3,3,7,7,7,7,7,7,7,7]
    #               0 1 2 3 4 5 5 7 8 9 0 1 2 3 4
    >>> rmq = This([3,2,3,1,3,2,3,0,3,2,3,1,3,2,3])
    >>> f = rmq.left_biased_range_minimum_query
    >>> [f(0, i) for i in range(1, len(rmq.array)+1)]
    [0, 1, 1, 3, 3, 3, 3, 7, 7, 7, 7, 7, 7, 7, 7]
    >>> [f(8, i) for i in range(9, len(rmq.array)+1)]
    [8, 9, 9, 11, 11, 11, 11]

    >>> rmq = This([3,2,3,1,3,2,3,0,3,2,3,1,3,2,3], offset=True)
    >>> f = rmq.left_biased_range_minimum_query
    >>> [f(0, i) for i in range(1, len(rmq.array)+1)]
    [0, 1, 1, 3, 3, 3, 3, 7, 7, 7, 7, 7, 7, 7, 7]
    >>> [f(8, i) for i in range(9, len(rmq.array)+1)]
    [8, 9, 9, 11, 11, 11, 11]

'''
    def __init__(self, array, up_to_length=None, *, offset=False):
        if not len(array) >= 1: raise ValueError

        if up_to_length is None:
            up_to_length = len(array)
        offset = bool(offset)

        # all public properties
        self.power_table = make_left_biased_range_minimum_query_power_table(
                                array, up_to_length, offset=offset)
        self.array = array
        self.up_to_length = up_to_length
        self.offset = offset
        assert len(self.power_table) == len(array)-1
    def left_biased_range_minimum_query(self, begin, end):
        '''see: left_biased_range_minimum_query_definition


let n = len(array)
time O(1)*(uint[..up_to_length].'bit_length <<' + uint[..n].'-')
    # bit_length and shift operation
    = time O(log(up_to_length))
    or = time O(1)
        since up_to_length <= n <= MAX_ARRAY_SIZE
        log2(n) <= bit_size_of(POINTER)
        O(loglog(n)) # search in a fixed size sorted-ordered-tree-set
        O(1)         # or simply treat it constant

return unoffseted array_idx, no matter what self.offset is
'''
        if not 0 <= begin < end <= len(self.array): raise ValueError
        # nonempty range

        if begin+1 == end:
            # singleton range
            return begin
        L = end-begin # >= 2
        if not L <= self.up_to_length: raise ValueError

        # L < (1 << L.bit_length())
        power = L.bit_length() - 1 # L/2 <= 2**power
            # O(log(L))
            # O(log(n))
            # n <= MAX_ARRAY_SIZE
            # log2(n) <= bit_size_of(POINTER)
            # ==>> O(loglog(n)) or O(1)
        ge_half_L = 1 << power

        begin1 = begin
        # end1 = begin1 + ge_half_L
        end2 = end
        begin2 = end2 - ge_half_L

        min_array_element_idx1 = self.power_table[begin1][power-1]
        min_array_element_idx2 = self.power_table[begin2][power-1]
        if self.offset:
            min_array_element_idx1 += begin1
            min_array_element_idx2 += begin2

        min1 = self.array[min_array_element_idx1]
        min2 = self.array[min_array_element_idx2]
        return min_array_element_idx2 if min2 < min1 else min_array_element_idx1



if __name__ == "__main__":
    import doctest
    doctest.testmod()

