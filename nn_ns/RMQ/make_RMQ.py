

__all__ = '''
    make_RMQ

    LeftBiasedRMQ
    '''.split()



from .LeftBiasedRMQ.LeftBiasedRMQ import LeftBiasedRMQ

def make_RMQ(array, *, shadow=False, to_verify_rmq_result=True):
    '''left biased range minimum query



input and output:
  see: LeftBiasedRMQ
  * input:
    array :: Ord a => [a]
    shadow :: Bool
        if shadow:
            replace array<a> by a array<uint>
    to_verify_rmq_result :: Bool
        if to_verify_rmq_result:
            will verify result of left_biased_range_minimum_query per query
  * output:
    rmq_obj :: begin -> end -> array_min_idx
        see example below
        see: left_biased_range_minimum_query_definition


example:
    >>> array = '0123456789'
    >>> rmq = make_RMQ(array)
    >>> L = len(array)
    >>> [rmq(0, i) for i in range(1, 1+L)]
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    >>> [rmq(i, L) for i in range(L)]
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> rmq(5,7)
    5
    >>> rmq(4,8)
    4
    >>> rmq(4,8000, False)
    (4,)
    >>> rmq(4000,8, False)
    ()


time and space:
    see: LeftBiasedRMQ

    let p = len(array)
    * query time
        = O(1)*(uint[..p].'bit_length << -')
        #### seems not O(1)*basic_machine_operation
        ####    but maybe p < MAX_MACHINE_WORD, and hence be O(1)*ops
    * init time
        = O(p)*(a.'<=' + uint[..p].'+-')
        #### seems not O(p)*basic_machine_operation
        ####    but maybe p < MAX_MACHINE_WORD, and hence be O(p)*ops
    * space
        = O(p)*bit
    * optional shadow uint array
        init time O(p)*(a.'<' + uint[..p].'+-')
        space O(p*log2(p))*bit
    * optional auxiliary rmq_result verifier
        init time O(p)*(a."<" + uint[..p].'+')
        verify time O(1)*uint[..p].'<'
        space O(p*log2(p))*bit

ref:
    [Range_Minimum_Query_2007]A_New_Succinct_Representation_of_RMQ_Information_and_Improvements_in_the_Enhanced_Suffix_Array.pdf


used alias:
    rmq_from_array
'''
    assert len(array) > 0
    lb_rmq = LeftBiasedRMQ.make_LeftBiasedRMQ_from_array(array)
    def rmq(begin, end, strict=True):
        '''
if strict, then require 0 <= begin < end <= len(array)
else require 0 <= min(begin, end)
'''
        return lb_rmq(begin, end, strict=strict)
    return rmq


if __name__ == "__main__":
    import doctest
    doctest.testmod()


