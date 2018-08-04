

__all__ = '''
    LeftBiasedRMQ
    '''.split()

if True:
    # used only in make_LeftBiasedRMQ_for_given_complete_block_sizes
    from .calc_normal_block_type import \
        calc_normal_block_types_and_may_rmqs
    #from .make_left_biased_range_minimum_query_power_table import\
    #   make_left_biased_range_minimum_query_power_table
    from .calc_left_biased_array_min_idx_per_block import\
        calc_left_biased_array_min_idx_per_block
    from .array_to_idx2depth_in_canonical_Cartesian_tree import\
        array_to_idx2depth_in_canonical_Cartesian_tree
    from .array_to_idx2left_biased_rmq_control_range import VerifyLeftBiasedRMQ
if True:
    # used only in make_LeftBiasedRMQ_from_array
    from .calc_complete_block_sizes import (
        calc_complete_normal_block_size
        ,calc_complete_super_block_size

        ,calc_complete_super_block_size__ver2_or_3
        ,calc_complete_super_block_size__ver1
        )

from .ballot_number.Catalan_number import Catalan_number
from .LeftBiasedRangeMinimumQuery__via_power_table import \
    LeftBiasedRangeMinimumQuery__via_power_table
from .left_biased_minimum_query import left_biased_minimum_query
from .common_methods import calc_num_blocks, ceil_div, is_sorted
from itertools import chain, starmap

BasicRMQ = LeftBiasedRangeMinimumQuery__via_power_table
OffsetedBasicRMQ = LeftBiasedRangeMinimumQuery__via_power_table




class LeftBiasedRMQ:
    __doc__ = '''see: left_biased_range_minimum_query_definition.py

ref:
    [Range_Minimum_Query_2007]A_New_Succinct_Representation_of_RMQ_Information_and_Improvements_in_the_Enhanced_Suffix_Array.pdf

let p = len(array)
time and space:
    assume: s_ = log2(p)**2_x, s = log2(p)/2_y
    * query time
        see: self.left_biased_range_minimum_query
        = O(1)*(uint[..ceil(p/s_)].'bit_length <<' + uint[..ceil(p/s).'-'])
        <= O(1)*(uint[..p].'bit_length << -')
        #### seems not O(1)*basic_machine_operation
        ####    but maybe p < MAX_MACHINE_WORD, and hence be O(1)*ops

    * init time
        see: self.make_LeftBiasedRMQ_for_given_complete_block_sizes
        = O(p)*(a.'<=' + uint[..p].'+-')
        #### seems not O(p)*basic_machine_operation
        ####    but maybe p < MAX_MACHINE_WORD, and hence be O(p)*ops
    * space
        see: self.make_LeftBiasedRMQ_for_given_complete_block_sizes
        = O(p)*bit
    * optional shadow uint array
        init time O(p)*(a.'<' + uint[..p].'+-')
        space O(p*log2(p))*bit
    * optional auxiliary rmq_result verifier
        init time O(p)*(a."<" + uint[..p].'+')
        verify time O(1)*uint[..p].'<'
        space O(p*log2(p))*bit



example:
    >>> from_array = LeftBiasedRMQ.make_LeftBiasedRMQ_from_array
    >>> rmq = from_array('0123456789')
    >>> query = rmq.left_biased_range_minimum_query
    >>> L = len(rmq.array)
    >>> [query(0, i) for i in range(1, 1+L)]
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    >>> [query(i, L) for i in range(L)]
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> query(5,7)
    5
    >>> rmq(4,8)
    4
    >>> rmq(4,8000, strict=False)
    (4,)
    >>> rmq(4000,8, strict=False)
    ()

    >>> rmq = from_array('2012')
    >>> rmq(0,1)
    0

############## properties
num_normal_blocks
num_super_blocks
complete_super_block_size               # s_
complete_normal_block_size              # s
super_min_indices                       # B_
normal_min_indices                      # B
multiple_super_blocks_query_table       # M_
multiple_normal_blocks_query_table      # M
normal_block_types                      # T
precomputed_InNormalBlock_query_table   # P
############## constructors
make_LeftBiasedRMQ_from_array
make_LeftBiasedRMQ_for_given_complete_block_sizes
make_LeftBiasedRMQ
############## query_methods
__call__
user_query
left_biased_range_minimum_query
in_normal_block_query
normal_blocks_query
super_blocks_query
_LeftBiasedRMQ__combine_array_indices
############## other methods
_LeftBiasedRMQ__may_verify_rmq_result
array_idx2containing_normal_block_idx
array_idx2containing_super_block_idx
unoffset_in_normal_block_idx


############## __init__.__doc__:
'''
    def __call__(self, begin, end, *, strict=True):
        '''
if strict, then require 0 <= begin < end <= len(array)
    else require 0 <= min(begin, end)
if strict then use .left_biased_range_minimum_query
    else use .user_query
'''
        if strict:
            return self.left_biased_range_minimum_query(begin, end)
        return self.user_query(begin, end)

    @classmethod
    def make_LeftBiasedRMQ_from_array(cls, array
            , *, shadow=False, superVersion=None, to_verify_rmq_result=True):
        # shadow: replace array<a> by a array<uint>
        p = len(array)
        complete_normal_block_size = calc_complete_normal_block_size(p)
        complete_super_block_size = calc_complete_super_block_size(p, superVersion)
        return cls.make_LeftBiasedRMQ_for_given_complete_block_sizes(
            array
            , complete_super_block_size
            , complete_normal_block_size
            , shadow=shadow
            , to_verify_rmq_result=to_verify_rmq_result)

    @classmethod
    def make_LeftBiasedRMQ_for_given_complete_block_sizes(
            cls, array, complete_super_block_size, complete_normal_block_size
            , *, shadow=False, to_verify_rmq_result=True):
        '''

time and space:
    assume: s_ = log2(p)**2_x, s = log2(p)/2_y
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






let p = len(array)
input:
    array :: Ord a => [a]

    s_ = complete_super_block_size :: PInt
    s = complete_normal_block_size :: PInt
    shadow :: Bool
        if shadow:
            replace array<a> by a array<uint>
            the new uint array:
                init time O(p)*(a.'<' + uint[..p].'+-')
                space O(p*log2(p))*bit

    to_verify_rmq_result :: Bool
        if to_verify_rmq_result:
            will verify result of left_biased_range_minimum_query per query

            need extra auxiliary data:
                init time O(p)*(a."<" + uint[..p].'+')
                verify time O(1)*uint[..p].'<'
                space O(p*log2(p))*bit



eval time and space:
    assume: shadow=False, to_verify_rmq_result=False
    assume: s_ = log2(p)**2_x, s = log2(p)/2_y

    # will create (B_, B, M_, M, T, P)
    * init time
        = O(p)*(a.'<=' + uint[..p].'+-')
        ######### eval
        = O(time(B_)+time(B)  +time(M_)+time(M)+  time(T)+time(P))
        = O(num_super_blocks) * (a.'<' + uint[..num_super_blocks].'+')
        + O(num_normal_blocks) * (a.'<' + uint[..num_normal_blocks].'+')
        + O(num_super_blocks*log(num_super_blocks)) * (a.'<=' + uint[:num_super_blocks].'+-')
        + O(num_normal_blocks*log(normal_min_array__up_to_length)) * (a.'<=' + uint[:num_normal_blocks].'+-')
        + O(p) * uint[..p].'+'
        + O(p)*(a.'<=' + uint[:s].'+-')

        = O(p/s_) * (a.'<' + uint[..ceil(p/s_)].'+')
        + O(p/s) * (a.'<' + uint[..ceil(p/s)].'+')
        + O(p/s_*log(p/s_)) * (a.'<=' + uint[:ceil(p/s_)].'+-')
        + O(p/s*log(s_/s)) * (a.'<=' + uint[:ceil(p/s)].'+-')
        + O(p) * uint[..p].'+'
        + O(p)*(a.'<=' + uint[:s].'+-')
        = O(p)*(a.'<=' + uint[..p].'+-')


    * space
        = O(p)*bit
        ######### eval
        = O(space(B_)+space(B)  +space(M_)+space(M)+  space(T)+space(P))
        = O(p/s_ * log(p))*bit
        + O(p/s * log(p))*bit
        + O(num_super_blocks*log(num_super_blocks)*log(num_super_blocks))*bit
        + O(num_normal_blocks*log(normal_min_array__up_to_length)**2)*bit
        + O(2p)*bit
        + O(p)*bit

        = O(p/s_ * log(p))*bit
        + O(p/s * log(p))*bit
        + O(p/s_*log(p/s_)*log(p/s_))*bit
        + O(p/s*log(s_/s)**2)*bit
        + O(2p)*bit
        + O(p)*bit
        = O(p)*bit
'''

        #def __init__(self, array, s_, s, B_, B, M_, M, T, P, maybe_rqm_verifier):
        s_ = complete_super_block_size
        s = complete_normal_block_size
        p = len(array)
        if not 1 <= s <= s_ <= p: raise ValueError

        if shadow:
            #time O(L)*(a.'<' + uint[..L].'+-')
            #space O(L*log2(L))*bit
            array = array_to_idx2depth_in_canonical_Cartesian_tree(array)

        #B_ B
        #time O(L) * (a.'<' + uint[..L].'+') + O(1) * elements.'iter'
        #space bit size O(L/B * log(L))
        B_ = calc_left_biased_array_min_idx_per_block(array, s_)
        B = calc_left_biased_array_min_idx_per_block(array, s)

        num_super_blocks = calc_num_blocks(p, s_)
        num_normal_blocks = calc_num_blocks(p, s)
        assert len(B_) == num_super_blocks
        assert len(B) == num_normal_blocks
        super_min_array = [array[i] for i in B_]
        normal_min_array = [array[i] for i in B]
        normal_min_array__up_to_length = ceil_div(s_, s)

        #M_ M
        #time O(n*log(up_to_length)) * (a.'<=' + uint[:n].'+-')
        #if offset:  O(n*log(up_to_length)**2)*bit
        #else:       O(n*log(up_to_length)*log(n))*bit
        M_ = BasicRMQ(super_min_array, num_super_blocks, offset=False)
        M = OffsetedBasicRMQ(normal_min_array, normal_min_array__up_to_length, offset=True)


        #T P
        '''
        time(P) = O(4^s)*(a.'<=' + uint[:s].'+-')
                ########### if s = log2(p)/2_y
                = O(p)*(a.'<=' + uint[:s].'+-')
        space(P) = O(4^s)*bit
                 ########## if s = log2(p)/2_y
                 = O(p)*bit

        time(T) = O(p + s^2) * Catalan_number(s).'+'
                ########### if s = log2(p)/2_y
                = O(p) * uint[..p].'+'
        space(T) = O(2p)*bit
    '''
        T, P = calc_normal_block_types_and_may_rmqs(array, s)

        maybe_rqm_verifier = None
        if to_verify_rmq_result:
            #init time O(L)*(a."<" + uint[..L].'+')
            #verify time O(1)*uint[..L].'<'
            #space O(L*log2(L))*bit
            maybe_rqm_verifier = VerifyLeftBiasedRMQ(array)

        return cls.make_LeftBiasedRMQ(
                array, s_, s, B_, B, M_, M, T, P, maybe_rqm_verifier)













    ################
    @classmethod
    def make_LeftBiasedRMQ(cls, array, s_, s, B_, B, M_, M, T, P
                                , maybe_rqm_verifier=None):
        # since the __init__ may be overrided, call this instead
        return cls(array, s_, s, B_, B, M_, M, T, P, maybe_rqm_verifier)

    def __init__(self, array, s_, s, B_, B, M_, M, T, P, maybe_rqm_verifier=None):
        '''

input:
    array :: Ord a => [a]

    s_ = complete_super_block_size :: PInt
    s = complete_normal_block_size :: PInt
    B_ = super_min_indices :: [ArrayIdx]
        # Map SuperBlockIdx ArrayIdx
        # to the index of the left-biased-min-element in a super_block
    B = normal_min_indices :: [ArrayIdx]
        # Map NormalBlockIdx ArrayIdx
        # to the index of the left-biased-min-element in a normal_block
    M_ = multiple_super_blocks_query_table :: BasicRMQ
        # BasicRMQ<num_super_blocks>
        # M_.rmq :: SuperBlockIdx -> SuperBlockIdx -> uint[..num_super_blocks]
    M = multiple_normal_blocks_query_table :: OffsetedBasicRMQ
        # OffsetedBasicRMQ<num_normal_blocks, uptoN>
        # M.rmq :: (begin<-NormalBlockIdx) -> NormalBlockIdx -> (begin+uint[..uptoN-1])
    T = normal_block_types :: [NormalBlockType]
        # Map NormalBlockIdx NormalBlockType
    P = precomputed_InNormalBlock_query_table :: [Maybe BasicRMQ]
        # Map NormalBlockType (None | BasicRMQ<s>)
    where
        NormalBlockType = UInt[0..Catalan_number(s)-1]
        SuperBlockIdx = UInt[0..num_super_blocks-1]
        NormalBlockIdx = UInt[0..num_normal_blocks-1]
        p = len(array)
        uptoN = ceil(s_/s)
        num_super_blocks = ceil(p/s_)
        num_normal_blocks = ceil(p/s)

'''

        p = len(array)
        if not 0 < s <= s_ <= p: raise ValueError
        num_super_blocks = calc_num_blocks(p, s_)
        num_normal_blocks = calc_num_blocks(p, s)
        min_uptoN = ceil_div(s_, s) # min uptoN
        assert 0 < s <= s_ <= min_uptoN*s


        # test M_ M
        if not isinstance(M_, BasicRMQ): raise TypeError
        if not isinstance(M, OffsetedBasicRMQ): raise TypeError

        if not M_.up_to_length == num_super_blocks == len(M_.array): raise ValueError('M_.up_to_length not big enough')
        if not min_uptoN <= M.up_to_length: raise ValueError('M.up_to_length not big enough')
        if M_.offset: raise ValueError('M_.offset should be False') # neednot
        if not M.offset: raise ValueError('M.offset should be True') # MUST



        # test T P
        if not num_super_blocks == len(M_.array) == len(B_): raise ValueError
        if not num_normal_blocks == len(M.array) == len(B) == len(T): raise ValueError
        if not Catalan_number(s) == len(P): raise ValueError
        #assert all(isinstance(P[block_type], BasicRMQ) for block_type in set(T))


        if not (maybe_rqm_verifier is None or hasattr(maybe_rqm_verifier, 'verify_left_biased_rmq_result')): raise TypeError


        # public properties
        self.array = array
        self.s_ = s_
        self.s = s
        self.M_ = M_
        self.M = M
        self.B_ = B_
        self.B = B
        self.P = P
        self.T = T
        self.normal_min_array__up_to_length = min_uptoN
        self.maybe_rqm_verifier = maybe_rqm_verifier
    __doc__ += __init__.__doc__

    @property
    def p(self):
        return len(self.array)
    @property
    def num_super_blocks(self):
        return len(self.B_)
    @property
    def num_normal_blocks(self):
        return len(self.B)

    @property
    def complete_super_block_size(self):
        return (self.s_)
    @property
    def complete_normal_block_size(self):
        return (self.s)
    @property
    def super_min_indices(self):
        return (self.B_)
    @property
    def normal_min_indices(self):
        return (self.B)
    @property
    def multiple_super_blocks_query_table(self):
        return (self.M_)
    @property
    def multiple_normal_blocks_query_table(self):
        return (self.M)
    @property
    def precomputed_InNormalBlock_query_table(self):
        return (self.P)
    @property
    def normal_block_types(self):
        return (self.T)

    def array_idx2containing_normal_block_idx(self, array_idx):
        # -> normal_block_idx
        assert 0 <= array_idx < self.p
        return array_idx//self.s
    def array_idx2containing_super_block_idx(self, array_idx):
        # -> super_block_idx
        assert 0 <= array_idx < self.p
        return array_idx//self.s_
    def unoffset_in_normal_block_idx(self, normal_block_idx, offseted_idx):
        return normal_block_idx*self.s + offseted_idx

    def user_query(self, begin, end):
        ''':: ArrayIdx -> ArrayIdx -> Maybe ArrayIdx

Maybe ArrayIdx = () | (ArrayIdx,)

like self.left_biased_range_minimum_query
    but allow end > len(array) and end <= begin
'''
        if not (begin >= 0 and end >= 0): raise ValueError
        if end > self.p:
            end = self.p
        if end <= begin:
            return ()

        assert 0 <= begin < end <= self.p
        r = self.left_biased_range_minimum_query(begin, end)
        return (r,)

    def left_biased_range_minimum_query(self, begin, end):
        ''':: ArrayIdx -> ArrayIdx -> ArrayIdx

left_biased_range_minimum_query(begin, end) -> array_min_idx
    0 <= begin < end <= self.p

what?
    RMQ

query time:
    = O(1)*(uint[..p].'bit_length << -' <=)
    ############## eval
    # 2*in_normal_block_query + 2*normal_blocks_query + 1*super_blocks_query
    O(1)*(self.'in_normal_block_query normal_blocks_query super_blocks_query')
    = O(1)*(uint[..s].'bit_length << -')
    + O(1)*(uint[..ceil(s_/s)].'bit_length <<' + uint[..ceil(p/s).'-'])
    + O(1)*(uint[..ceil(p/s_)].'bit_length << -')
    # where s_ = log2(p)**2_x, s = log2(p)/2_y
    = O(1)*(uint[..ceil(p/s_)].'bit_length <<' + uint[..ceil(p/s).'-'])
    <= O(1)*(uint[..p].'bit_length << -' <=)
    #### seems not O(1)*basic_machine_operation
    ####    but maybe p < MAX_MACHINE_WORD, and hence be O(1)*ops
'''
        if not 0 <= begin < end <= self.p: raise ValueError
        s = self.s
        s_ = self.s_
        uptoN = self.normal_min_array__up_to_length # == ceil(s_/s)
        if not 0 < s <= s_ <= uptoN*s: raise Exception('LeftBiasedRMQ subclass impl error')

        # "leftcomplete" means overlapped block_range<block>.begin = block.begin
        # "empty" means overlapped block_range<block>.end = block.begin
        the_head_mayleftcomplete_notempty_normal_block_idx = begin//s
            # maybe leftcomplete, but never empty
        the_last_notleftcomplete_mayempty_normal_block_idx = end//s
            # maybe leftempty, but never complete

        beginN = normal_blocks_begin = ceil_div(begin, s)
        endN = normal_blocks_end = end//s
            # maybe beginN >= endN
        beginS = super_blocks_begin = ceil_div(begin, s_)
        endS = super_blocks_end = end//s_
            # maybe beginS >= endS
        assert begin <= beginN*s < begin+s
        assert end-s < endN*s <= end
        assert begin <= beginS*s_ < begin+s_
        assert end-s_ < endS*s_ <= end


        # pseudo_in_normal_block_queries use array_idx
        # pseudo_normal_blocks_queries use normal_block_idx
        # pseudo_super_blocks_queries use super_block_idx
        mid1 = beginN*s
        mid2 = endN*s
        assert mid1 - s < begin <= mid1
        assert mid2 <= end < mid2 + s


        # "pseudo" means maybe a empty/negative range query
        #   pseudo_query = (begin, end) where may: end <= begin
        if mid2 < mid1:
            # 1 in_normal_block_query
            assert mid1-s == mid2 < begin < end < mid2+s == mid1
            pseudo_in_normal_block_queries = [(begin, end)]
            pseudo_normal_blocks_queries = []
            pseudo_super_blocks_queries = []
        else:
            # one in_normal_block_query may be empty
            assert mid1-s < begin <= mid1 <= mid2 <= end < mid2+s and begin < end
            pseudo_in_normal_block_queries = [(begin, mid1), (mid2, end)]


            assert mid1*s == beginN <= endN == mid2*s
            mid1N = normal_blocks_mid1 = beginN + uptoN
            mid2N = normal_blocks_mid2 = endN - uptoN
            if endN <= mid1N:
                # may empty
                #   i.e. may: beginN == endN
                assert (mid2N <= beginN <= endN <= beginN + uptoN == mid1N)
                pseudo_normal_blocks_queries = [(beginN, endN)]
            else:
                # may mid1N >= mid2N
                assert beginN < mid1N < endN
                assert beginN < mid2N < endN
                pseudo_normal_blocks_queries = [(beginN, mid1N), (mid2N, endN)]



            # NOET: beginS+1 == endS
            #       split into two cases
            if mid2N <= mid1N:
                assert beginS+1 >= endS
                pseudo_super_blocks_queries = []
            else:
                assert beginS+1 <= endS
                    # overlap with above condition
                    # but fine
                if True:
                    # recall:
                    assert s_ <= uptoN*s
                    assert mid1N < mid2N
                    assert beginN+uptoN == mid1N < mid2N == endN-uptoN
                # complete proof
                assert (begin <= beginS*s_ < begin+s_
                        <= begin+uptoN*s <= beginN*s+uptoN*s == mid1N*s
                        < mid2N*s == endN*s-uptoN*s <= end-uptoN*s
                        <= end-s_ < endS*s_ <= end)
                if True:
                    # simple view
                    assert (begin <= beginS*s_ < mid1N*s < mid2N*s < endS*s_ <= end)
                    # [begin, beginN*s) - pseudo_in_normal_block_query
                    # [beginN*s, mid1N*s) - pseudo_normal_blocks_query
                    # [beginS*s_, endS*s_) - pseudo_super_blocks_querry
                    # [mid2N*s, endN*s) - pseudo_normal_blocks_query
                    # [endN*s, end) - pseudo_in_normal_block_query
                pseudo_super_blocks_queries = [(beginS, endS)]
        #end if

        #for beign, end in queries: if begin >= end: delete it
        for queries in [pseudo_in_normal_block_queries
                       , pseudo_normal_blocks_queries
                       , pseudo_super_blocks_queries]:
            queries[:] = [(begin, end) for begin, end in queries if begin < end]
        else:
            in_normal_block_queries = pseudo_in_normal_block_queries
            normal_blocks_queries = pseudo_normal_blocks_queries
            super_blocks_queries = pseudo_super_blocks_queries

        array_indices = chain(
            # all return array_idx
            starmap(self.in_normal_block_query, in_normal_block_queries)
            ,starmap(self.normal_blocks_query, normal_blocks_queries)
            ,starmap(self.super_blocks_query, super_blocks_queries)
            )

        #bug: return self.__combine_array_indices(array_indices)
        # !!!!!!!!!!should sorted them!!!!!!!!!!!!!!!!!
        array_indices = sorted(array_indices)
        assert 1 <= len(array_indices) <= 5
        rmq_result = self.__combine_array_indices(array_indices)
        if not self.__may_verify_rmq_result(begin, end, rmq_result):
            raise Exception('LeftBiasedRMQ impl error')
        return rmq_result
    def __may_verify_rmq_result(self, begin, end, rmq_result):
        # verify time O(1)*uint[..p].'<'
        if self.maybe_rqm_verifier is None:
            return 0 <= begin <= rmq_result < end <= self.p
        return self.maybe_rqm_verifier.verify_left_biased_rmq_result(
                    begin, end, rmq_result)
    def __combine_array_indices(self, sorted_array_indices):
        #assert 1 <= len(sorted_array_indices) <= 5
        if not len(sorted_array_indices) >= 1: raise ValueError
        if not is_sorted(sorted_array_indices): raise ValueError

        if len(sorted_array_indices) == 1:
            [idx] = sorted_array_indices
            return idx

        array = self.array
        head, *tail = (array[array_idx] for array_idx in sorted_array_indices)
        subarray_idx = left_biased_minimum_query(head, tail)
        return sorted_array_indices[subarray_idx]



    def super_blocks_query(self, begin_super_block_idx, end_super_block_idx):
        '''super_block_idx -> super_block_idx -> array_idx

super_blocks_query(beginS, endS) -> array_min_idx
    0 <= beginS < endS <= self.num_super_blocks

time:
    O(1) * BasicRMQ<num_super_blocks>.'left_biased_range_minimum_query'
    = O(1)*(uint[..num_super_blocks].'bit_length << -')
    = O(1)*(uint[..ceil(p/s_)].'bit_length << -')
    # where s_ = log2(p)**2_x
    #### seems not O(1)*basic_machine_operation
    ####    but maybe p < MAX_MACHINE_WORD, and hence be O(1)*ops
'''
        if not 0 <= begin_super_block_idx < end_super_block_idx <= self.num_super_blocks: raise ValueError
        arrayBx_min_idx = self.M_.left_biased_range_minimum_query(
                        begin_super_block_idx, end_super_block_idx)
        array_min_idx = self.B_[arrayBx_min_idx]
        return array_min_idx


    def normal_blocks_query(self, begin_normal_block_idx, end_normal_block_idx):
        '''normal_block_idx -> normal_block_idx -> array_idx

normal_blocks_query(beginN, endN) -> array_min_idx
    0 <= beginN < endN <= self.num_normal_blocks

time:
    O(1) * OffsetedBasicRMQ<num_normal_blocks, uptoN>.'left_biased_range_minimum_query'
    = O(1)*(uint[..uptoN].'bit_length <<' + uint[..num_normal_blocks].'-')
    = O(1)*(uint[..ceil(s_/s)].'bit_length <<' + uint[..ceil(p/s).'-'])
    # where s_ = log2(p)**2_x, s = log2(p)/2_y
    #### seems not O(1)*basic_machine_operation
    ####    but maybe p < MAX_MACHINE_WORD, and hence be O(1)*ops
'''
        if not 0 <= begin_normal_block_idx < end_normal_block_idx <= self.num_normal_blocks: raise ValueError
        # bug:offseted_arrayB_min_idx = ...
        arrayB_min_idx = self.M.left_biased_range_minimum_query(
                            begin_normal_block_idx, end_normal_block_idx)
        array_min_idx = self.B[arrayB_min_idx]
        return array_min_idx

    def in_normal_block_query(self, begin, end):
        '''array_idx -> array_idx -> array_idx

in_normal_block_query(begin, end) -> array_min_idx
    0 <= begin < end <= self.p
    0 <= end-begin < self.s

time:
    O(1) * BasicRMQ<s>.'left_biased_range_minimum_query'
    = O(1)*(uint[..s].'bit_length << -')
    # where s = log2(p)/2_y
    #### seems not O(1)*basic_machine_operation
    ####    but maybe s < MAX_MACHINE_WORD, and hence be O(1)*ops
'''
        if not 0 <= begin < end <= self.p: raise ValueError
        if not 0 < end-begin <= self.s: raise ValueError
        normal_block_idx = self.array_idx2containing_normal_block_idx(begin)
        offset = normal_block_idx*self.s
        offseted_begin = begin - offset
        offseted_end = end - offset
        if not 0 <= offseted_begin < offseted_end <= self.s: raise ValueError('not in_normal_block query')
            # <<== in_normal_block

        normal_block_type = self.normal_block_types[normal_block_idx]
        basic_rmq = self.precomputed_InNormalBlock_query_table[normal_block_type]
        offseted_idx = basic_rmq.left_biased_range_minimum_query(
                        offseted_begin, offseted_end)
        assert 0 <= offseted_idx < self.s
        return offset + offseted_idx


def _t():
    from_array = LeftBiasedRMQ.make_LeftBiasedRMQ_from_array
    rmq = from_array('0123456789')
    query = rmq.left_biased_range_minimum_query
    L = len(rmq.array)
    assert [query(0, i) for i in range(1, 1+L)] == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert [query(i, L) for i in range(L)] == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert query(5,7) == 5

    rmq = from_array('2012')
    assert rmq(0,1) == 0

if __name__ == "__main__":
    _t()
    import doctest
    doctest.testmod()
    print('\n'.join(dir(LeftBiasedRMQ)))

