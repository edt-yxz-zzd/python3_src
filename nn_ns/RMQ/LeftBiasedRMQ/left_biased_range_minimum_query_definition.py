
def left_biased_range_minimum_query_definition(array, begin, end):
    '''left_biased_range_minimum_query_definition
    :: Ord a => [a]{1..}
    -> ArrayNonEmptyRangeBeginIdx
    -> ArrayNonEmptyRangeEndIdx
    -> ArrayNonEmptyRangeBeginIdx

this is a definition of range_minimum_query
    an slow impl, O(end-begin)
    return the left-biased min_array_element idx

input:
    array :: Ord a => [a]{1..}
    begin :: ArrayNonEmptyRangeBeginIdx
    end   :: ArrayNonEmptyRangeEndIdx
        0 <= begin < end <= len(array)
output:
    min_element_array_idx :: ArrayNonEmptyRangeBeginIdx
        0 <= min_element_array_idx < len(array)

impl:
    return array.index(min(array[begin:end]), begin, end)
'''
    assert array
    assert 0 <= begin < end <= len(array)
    m = min(array[begin:end])
    return array.index(m, begin, end) # left-biased



