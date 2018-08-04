

__all__ = '''
    uint_array2suffix_array
    '''.split()



from itertools import groupby, chain
from seed.seq_tools.inverse_uint_bijection_array import inverse_uint_bijection_array
from seed.iters.merge_two_sorted_iterables import merge_two_sorted_iterables
from seed.iters.is_sorted import is_strict_sorted
from seed.math.floor_ceil import ceil_div
from seed.math.divs import is_even, is_odd, divs

from seed.algo.bucket_sort.bucket_sort import bucket_sort_with_table
#_global_bucket_sort(alphabet_size, iterable, sorted_wheres=None, table, *, key)
#bucket_sort(alphabet_size, iterable, key=...)->[a]
def _global_bucket_sort(alphabet_size, iterable, sorted_wheres, table, *, key):
    '''this is a tmp func

assume all usages:
    sorted_wheres is None
    key is not None
    not reverse
'''
    if sorted_wheres is not None: raise logic-error
    if key is None: raise logic-error
    return bucket_sort_with_table(alphabet_size, iterable
        , range(alphabet_size), table, key=key)



class UIntArray2SuffixArray__ver3:
    '''

array<uint> to sorted_suffix_indices

see: "SA - 2.1 make UIntSA ver3.txt"
'''

    def handle_if_basic_case(self, alphabet_size, array, *, LCP):
        '''\
handle_if_basic_case(alphabet_size, array, LCP=False) -> (None|(SA<array>, None))
handle_if_basic_case(alphabet_size, array, LCP=True) -> (None|(SA<array>, LCP<array>))
'''
        return None


    #, detect_whether_all_chars_are_different_at_top_layer=False):
    def uint_array2suffix_array(self, alphabet_size, array
            , *, table=None, handle_if_basic_case=None, LCP=False):
        '''uint_array2suffix_array :: UInt -> [UInt] -> [UInt]

uint_array2suffix_array(alphabet_size, uint_array) -> suffix_array
handle_if_basic_case(alphabet_size, array) -> (None|SA<array>)

input:
    alphabet_size :: None | UInt
    string :: [Char]
        Char = UInt[0..alphabet_size-1]
    table :: None | [[UInt]]
        mutable, may increase the size if nessesary
    handle_if_basic_case :: None | (UInt -> [UInt] -> (None|[UInt]))
        this funtion define what is basic case and handle it
    LCP :: bool
        # LCP - longest common prefix of adjacent suffices in SA<string>
        if LCP:
            then output will become (suffix_array, lcp_array)

output:
    if not LCP:
        suffix_array :: [UInt]
            suffix_array = SA<string>
            suffix_array = sorted(range(len(string)), key=lambda i: string[i:])
            len(suffix_array) == len(string)
    else:
        (suffix_array :: [UInt], lcp_array :: [UInt])
            lcp_array = [len_lcp(string[i:], string[j:])
                        for i, j in zip(suffix_array, suffix_array[1:]]
            if len(string) != 0:
                len(lcp_array) == len(string)-1
            else:
                len(lcp_array) == 0



see:
    seed.seq_tools.inverse_uint_bijection_array
        # the inverse of suffix_array is useful

example:
    >>> this = UIntArray2SuffixArray__ver3().uint_array2suffix_array
    >>> wrapped_this = lambda s: this(None, tuple(map(int, s)))
    >>> wrapped_this('')
    []
    >>> wrapped_this('1')
    [0]
    >>> wrapped_this('12')
    [0, 1]
    >>> wrapped_this('21')
    [1, 0]
    >>> wrapped_this('123')
    [0, 1, 2]
    >>> wrapped_this('132')
    [0, 2, 1]
    >>> wrapped_this('312')
    [1, 2, 0]
    >>> wrapped_this('213')
    [1, 0, 2]
    >>> wrapped_this('231')
    [2, 0, 1]
    >>> wrapped_this('321')
    [2, 1, 0]
    >>> wrapped_this('11')
    [1, 0]
    >>> wrapped_this('111')
    [2, 1, 0]
    >>> wrapped_this('112233112233')
    [6, 0, 7, 1, 8, 2, 9, 3, 11, 5, 10, 4]
    >>> uint_array2suffix_array(None, [1,1,1,0])
    [3, 2, 1, 0]
    >>> uint_array2suffix_array(None, b'112233112233')
    [6, 0, 7, 1, 8, 2, 9, 3, 11, 5, 10, 4]
    >>> uint_array2suffix_array(None, [1,1,1])
    [2, 1, 0]
'''

        if alphabet_size is None:
            alphabet_size = max(array, default=-1)+1
        elif not all(0 <= u < alphabet_size for u in array): raise ValueError

        string = array; del array

        self.table = [] if table is None else table
        if handle_if_basic_case is not None:
            self._handle_if_basic_case = handle_if_basic_case
        else:
            self._handle_if_basic_case = self.handle_if_basic_case
        self.LCP = bool(LCP)
        if self.LCP: raise NotImplementedError


        # if detect_whether_all_chars_are_different_at_top_layer:
        if False: # optional
            # [all char are different]
            #   ==>> no suffices has common prefix
            #   then we simply bucket_sort them and done
            #
            if False:
                # now use table which dynamic increase its size
                # but like below

                # O(alphabet_size)
                table = get_or_make_table__len_ge(alphabet_size)
            # sort string_idx by char_ord
            # def key
            key = string.__getitem__
            sorted_string_indices = self.bucket_sort(
                        alphabet_size, range(len(string)), key=key)
            if is_strict_sorted(sorted_string_indices, key=key):
                SA = sorted_string_indices
                return SA
            del key


        # O(L+alphabet_size)
        #   to init the table, even the follow body is commentout
        if False:
            # now use table which dynamic increase its size
            # but like below

            # O(L+alphabet_size)
            table = get_or_make_table__len_ge(max(len(string), alphabet_size))
                # max, not min
                # see below: group_idx_upper_bound
                #       which may grow until L

        SA, may_LCP = self.__this(alphabet_size, string)
        if self.LCP and may_LCP is not None:
            LCP = may_LCP
            return SA, LCP
        if not self.LCP and may_LCP is None:
            return SA
        return logic-error



    def bucket_sort(self, alphabet_size, iterable, *, key):
        table = self.table
        if len(table) < alphabet_size:
            table.extend([] for _ in range(alphabet_size-len(table)))
        return _global_bucket_sort(alphabet_size, iterable, None, table, key=key)


    @staticmethod
    def i_xy_to_i_str(i_xy):
        return i_xy//2*3+1 +bool(i_xy&1)



    ######################### begin ################################
    def __this(self, alphabet_size, string):
        # -> (SA, may_LCP)
        L = len(string)

        ######################## basic case
        may_result = self._handle_if_basic_case(alphabet_size, string
                                , LCP=self.LCP)
        if may_result is not None:
            SA, may_LCP = may_result
            return SA, may_LCP
        if L == 0:
            may_LCP = [] if self.LCP else None
            return ([], may_LCP)

        ######################## useless
        ######################## begin of optional
        ######################## handle if all chars are different
        # when all chars are different:
        #   the suffix-tree is flatten
        #   we can simple sort chars
        #
            #see above and below instead
            #   above handle the global input string
            #   below handle before recur call
        ####################### end of optional



        ######################## non-basic case
        # BEGIN: radix_sort big_string
        '''

        # big_char = singleton_or_pair :: (a,)|(a,a) = BigChar
        # big_string = singleton_or_pair_ls
        # :: [BigChar]
        big_string = [string[i:i+2] # last one maybe singleton
                                for i in range(L) if i != 3*_]

        radix_sort(big_string)

        i_xy_to_big_char i_xy = string[i_xy_to_i_str i_xy:...+1]
        ... = groupby(sorted_indices_of_big_string, key=i_xy_to_big_char)
        ...
        big_string_idx2group_idx = ...
        group_idx__upper_bound = ... # maybe 0
        if group_idx__upper_bound == Lx:
            # each group contains only one char
            # i.e. all chars are different
            assert is_strict_sorted(sorted_indices_of_big_string, key=i_xy_to_big_char)
            SA_1_2 = sorted_indices_of_big_string
        else:
            SA_1_2 = ...

        '''
        # def Lx
        Lx = L - ceil_div(L,3) # len(big_string)
        assert 0 <= Lx < L
        assert L == 1 or Lx > 0

        def i_xy_to_big_char(i_xy:'suffix_begin_of_big_string'):
            i_str = self.i_xy_to_i_str(i_xy)
            return string[i_str:i_str+2] # len == 1 or 2


        sorted_indices_of_big_string = \
            self.radix_sort_big_string(alphabet_size, string, L, Lx)

        group_idx_upper_bound, big_string_idx2group_idx =\
            self.make__big_string_idx2group_idx(alphabet_size, L, Lx
            , i_xy_to_big_char
            , sorted_indices_of_big_string
            )


        ##### calc SA_1_2
        # may recur call __this
        (may_SA_1_2, may_LCP) = self.get_may_SA_1_2(Lx
                    , i_xy_to_big_char
                    , sorted_indices_of_big_string
                    , group_idx_upper_bound
                    )
        (SA_1_2, may_LCP) = (self.__this(group_idx_upper_bound
                            , big_string_idx2group_idx
                            )
                      if may_SA_1_2 is None
                      else (may_SA_1_2, may_LCP)
                      )
        del may_SA_1_2



        ########################### SA_0
        SA_0, may_LCP_0 = self.calc_SA_0(alphabet_size, string, L, Lx, SA_1_2)
        SA, may_LCP = self.merge_SA_0_and_SA_1_2(string, SA_0, SA_1_2)
        return SA, may_LCP
        ########################## end of this











    def radix_sort_big_string(self, alphabet_size, string, L, Lx):
        '''
        # bucket_sort all snd of pairs exclude the last singleton if any
        #   i.e. all snd of string[3z+2:...+2]
        #   i.e. string[3z+3]
        tmp = bucket_sort(range(Lx- not is_last_pair), key=i_xy_to_next_char)

        may_last_i_xy = [] if is_last_pair else [Lx-1]
        # bucket_sort all singletons and all fst of pairs
        sorted_indices_of_big_string =
            bucket_sort(may_last_i_xy +tmp, key=i_xy_to_char)
    where
        i_xy_to_i_str i_xy = i_xy//2*3+1 +bool(i_xy&1)
        i_xy_to_char i_xy = string[i_xy_to_i_str i_xy]
        i_xy_to_next_char i_xy = string[1+i_xy_to_i_str i_xy]
        is_last_pair
            <==> the last idx must be 3*i0
            <==> divs(3, L-1)

        '''
        is_last_pair = divs(3, L-1)

        def i_xy_to_char(i_xy):
            #i_xy_to_char i_xy = string[i_xy_to_i_str i_xy]
            return string[self.i_xy_to_i_str(i_xy)]
        def i_xy_to_next_char(i_xy):
            #i_xy_to_char i_xy = string[i_xy_to_i_str i_xy]
            return string[1+self.i_xy_to_i_str(i_xy)]

        tmp = self.bucket_sort(alphabet_size
                #bug:, range(Lx - (not is_last_pair)), key=i_xy_to_char)
                , range(Lx - (not is_last_pair)), key=i_xy_to_next_char)

        may_last_i_xy = [] if is_last_pair else [Lx-1]
        if may_last_i_xy:
            tmp.insert(0, *may_last_i_xy)
        # bucket_sort all singletons and all fst of pairs
        sorted_indices_of_big_string =\
            self.bucket_sort(alphabet_size, tmp, key=i_xy_to_char)
        return sorted_indices_of_big_string
        # END: radix_sort big_string



    def make__big_string_idx2group_idx(self
            , alphabet_size, L, Lx, i_xy_to_big_char
            , sorted_indices_of_big_string):
        ############################
        # BEGIN: make_array_idx2group_idx(big_string)
        big_string_idx2group_idx = [None]*Lx
        gs = groupby(sorted_indices_of_big_string, key=i_xy_to_big_char)
        group_idx = -1
        for group_idx, (_, g) in enumerate(gs):
            for big_string_idx in g:
                assert big_string_idx2group_idx[big_string_idx] is None
                big_string_idx2group_idx[big_string_idx]\
                    = group_idx
        group_idx_upper_bound = group_idx+1
        assert all(idx is not None for idx in big_string_idx2group_idx)

        assert 0 <= group_idx_upper_bound <= Lx < L
        assert 0 <= group_idx_upper_bound <= alphabet_size**2 + alphabet_size
            # may: group_idx_upper_bound > alphabet_size
        return group_idx_upper_bound, big_string_idx2group_idx
        # END: make_array_idx2group_idx(big_string)





    def get_may_SA_1_2(self, Lx
            , i_xy_to_big_char
            , sorted_indices_of_big_string
            , group_idx_upper_bound
            ):
        # -> (None, None) | (SA_1_2, may_LCP_1_2)
        #if is_strict_sorted(sorted_indices_of_big_string, key=key):
        if group_idx_upper_bound == Lx:
            if False:
                try:
                    assert is_strict_sorted(sorted_indices_of_big_string
                                        , key=i_xy_to_big_char)
                except:
                    print([*map(i_xy_to_big_char, sorted_indices_of_big_string)])
                    print(group_idx_upper_bound, Lx)
                    print(sorted_indices_of_big_string)
                    raise
                pass

            # all chars are different for SA_1_2
            SA_1_2 = sorted_indices_of_big_string
            may_LCP_1_2 = [0]*len(SA_1_2)-1 if self.LCP else None
            return SA_1_2, may_LCP_1_2

        else:
            # to recur call
            #assert not is_strict_sorted(sorted_indices_of_big_string
            #                        , key=i_xy_to_big_char)
            return None, None
        raise logic-error
        ########################### SA_1_2 DONE




    def calc_SA_0(self, alphabet_size, string, L, Lx, SA_1_2):
        '''
        def SA_0
        SA_0 = sorted(range(len(suffices_0)), key=\i->suffices_0[i])
            = sorted(range(len(suffices_0)), key=\i->string[3*i])
            where suffices_0 = [string[i:] for i in range(L) if i==3*_]
        def SA_1
        SA_1 = sorted(range(len(suffices_1)), key=\i->suffices_1[i])
            = sorted(range(len(suffices_1)), key=\i->string[3*i+1])
            where suffices_1 = [string[i:] for i in range(L) if i==3*_+1]

        '''

        '''
        # calc:
        SA_1 = [i_xy//2 | i_xy <- SA_1_2, i_xy&1==0]
        # calc:
        SA_0
            = radix_sort range(0,L, 3) with key=\i->(string[3*i], invSA_1_2[3*i+1])

            # can save the first bucket_sort (i.e. with key[-1])
            #   since SA_1 has known
            = [may last i0 if ...] + bucket_sort(SA_1, key=\i0->string[i0*3])
                # if last i0 not follow a i1
                #   i.e. L = 3*i0+1
                #   i.e. Lx = 2*i0
        '''

        SA_1 = [i_xy//2 for i_xy in SA_1_2 if is_even(i_xy)]
        may_last_i0 = [Lx>>1] if divs(3, L-1) else []
        #bug: tmp = bucket_sort(len(SA_1), SA_1, key=lambda i0: string[i0*3])
        tmpSA_0 = self.bucket_sort(alphabet_size
                                , SA_1, key=lambda i0: string[i0*3])
        if may_last_i0:
            tmpSA_0.insert(0, *may_last_i0)
        #SA_0 = may_last_i0 + tmpSA_0 if may_last_i0 else tmpSA_0
        SA_0 = tmpSA_0
        # TODO calc LCP_0
        may_LCP_0 = None
        assert not self.LCP, NotImplementedError
        return SA_0, may_LCP_0
        ########################### SA_0 DONE



    ########################### merge SA_0 and SA_1_2
    def merge_SA_0_and_SA_1_2(self, string, SA_0, SA_1_2):
        # -> SA
        invSA_1_2 = inverse_uint_bijection_array(SA_1_2)


        '''
        SA = merge le (map (3*) SA_0) (map i_xy_to_i_str SA_1_2)
            where
                Left = Right = id
                #le i_str_0 i_str_1_2
                le (3*i0) (3*i1+1) =
                    (string[3*i0], invSA_1_2[i_str_1_2_to_i_xy(3*i0+1)])
                    <=
                    (string[3*i1+1], invSA_1_2[i_str_1_2_to_i_xy(3*i1+2)])
                le (3*i0) (3*i2+2) =
                    (string[3*i0], string[3*i0+1]
                        , invSA_1_2[i_str_1_2_to_i_xy(3*i0+2)])
                    <=
                    (string[3*i2+2], string[3*i2+3], invSA_1_2[i_str_1_2_to_i_xy(3*i2+4)])
                i_xy_to_i_str i_xy = i_xy//2*3+1 +bool(i_xy&1)
                i_str_1_2_to_i_xy i_str = # inverse i_xy_to_i_str
                    if i_str == 3*i0+1 then 2*i0
                    elif i_str == 3*i0+2 then 2*i0+1
                    else undefined
        '''
        def may_invSA_1_2(i_xy):
            n = len(invSA_1_2)
            if n <= i_xy <= n+1:
                return -1
            return invSA_1_2[i_xy]

        def le(i_str_0, i_str_1_2):
            # assert divs(3, i_str_0)
            # assert not divs(3, i_str_1_2)
            i0 = i_str_0//3
            i_xy_base = i_str_1_2//3*2

            _1_or_2 = i_str_1_2%3
            if _1_or_2 == 1:
                i_str_1 = i_str_1_2
                i1 = i_xy_base # + 0
                i2_after_i1 = i1+1

                i1_after_i0 = 2*i0 # + 0
                lhs = (string[i_str_0], may_invSA_1_2(i1_after_i0))
                rhs = (string[i_str_1], may_invSA_1_2(i2_after_i1))
            else:
                assert _1_or_2 == 2
                i_str_2 = i_str_1_2
                i2 = i_xy_base + 1
                i1_after_i2 = i2+1

                i2_after_i0 = 2*i0 + 1
                lhs = (string[i_str_0:i_str_0+2], may_invSA_1_2(i2_after_i0))
                rhs = (string[i_str_2:i_str_2+2], may_invSA_1_2(i1_after_i2))
            return lhs <= rhs

        #SA = merge le (map (3*) SA_0) (map i_xy_to_i_str SA_1_2)
        idc_str_0 = map(lambda i0:3*i0, SA_0)
        idc_str_1_2 = map(self.i_xy_to_i_str, SA_1_2)
        [*SA] = merge_two_sorted_iterables(idc_str_0, idc_str_1_2, __le__=le)

        if False and __debug__:
            # TODO del all
            big_string = [string[i:i+1+ divs(3, i-2)] for i in range(L) if not divs(3, i)]
            print(f'''
string
    {string}
big_string
    {big_string}
tmp_half_1round
    {tmp_half_1round}
sorted_indices_of_big_string
    {sorted_indices_of_big_string}
SA_1_2
    {SA_1_2}
SA_0
    {SA_0}
SA
    {SA}
''');   input('...')
        # TODO calc may_LCP
        may_LCP = None
        assert not self.LCP, NotImplementedError
        return SA, may_LCP


uint_array2suffix_array = UIntArray2SuffixArray__ver3().uint_array2suffix_array
if __name__ == "__main__":
    assert [3,2,1,0] == uint_array2suffix_array(None, [1,1,1,0])
    assert uint_array2suffix_array(None, b'112233112233') == [6, 0, 7, 1, 8, 2, 9, 3, 11, 5, 10, 4]
    assert [2,1,0] == uint_array2suffix_array(None, [1,1,1])
    import doctest
    doctest.testmod()

