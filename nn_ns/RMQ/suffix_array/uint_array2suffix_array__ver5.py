

'''

string  = 100100100
L/S     = LSSLSSLLL
LMS     =  |  |
# sorted_LMS_substring_isuffices def ver1 # ERROR!!!
LMS_substring = 0010 00100
big_string    = [0,1]
big_stringSA  = [0,1] since 01 < 1
LMS_suffices:
    but 00100100 > 00100

# pseudo_sorted_LMS_substring_isuffices def ver2
#   L < S
#   let M = max+1 = alphabet_size, m = min-1 = -1
LMS_substring = 0S0S1L0S 0S0S1L0L0L
LMS_substring = 0010M 00100m
big_string    = [1,0]
big_stringSA  = [1,0] since 0 < 10
LMS_suffices:
    00100100 > 00100

proof (append m/M):
    we donot sort LMS_substring_1size_suffix (except string[-1:])
        * suffix_LMS = _ ++ [larger_char, LMS_char, M]
        * suffix_last = _ ++ [string[-1], m]
        cmp two suffices:
        if one is prefix of other (donot consider m/M):
            before: shorter < longer
                they must cmp into the L section of longer
            * suffix_LMS vs suffix_LMS
                before: shorter < longer
                after both append M: shorter > longer
            * suffix_last == suffix_LMS[:i]
                before/after: suffix_last < suffix_LMS
            * suffix_LMS == suffix_last[:i]
                before: suffix_LMS < suffix_last
                after: suffix_LMS > suffix_last
            * suffix_last vs suffix_last
                before/after: shorter < longer
        else:
            # no one is prefix of another
            append m/M has no affect
'''

__all__ = '''
    uint_array2suffix_array
    '''.split()


from .suffix_array_definition import suffix_array_definition
from .lcp_array_definition import lcp_array_definition
from .len_lcp import len_lcp as len_lcp_f
from itertools import groupby, chain, accumulate
from seed.iters.zip_me import zip_me2
from seed.seq_tools.inverse_uint_bijection_array import inverse_uint_bijection_array
from seed.seq_tools.is_inverse_uint_bijection_array_of import is_inverse_uint_bijection_array_of
from seed.iters.is_sorted import is_sorted, is_strict_sorted
'''
from seed.iters.merge_two_sorted_iterables import merge_two_sorted_iterables
from seed.math.floor_ceil import ceil_div
from seed.math.divs import is_even, is_odd, divs
'''

from seed.algo.bucket_sort.bucket_sort_with_table import bucket_sort_with_table
from seed.algo.bucket_sort.is_uint_bijection_array import is_uint_bijection_array
from seed.algo.bucket_sort.all_unique import all_unique
from seed.algo.bucket_sort.bucket_count import bucket_count
from seed.iters.all_the_same import all_the_same
#from ..rmq_from_array import rmq_from_array
from ..make_RMQ import make_RMQ as rmq_from_array

old_print = print
def new_print(*args, **kwargs):
    pass
print = new_print




class UIntArray2SuffixArray__ver5:
    '''

array<uint> to sorted_suffix_indices

see: "SA new - 2.1 make UIntSA ver5.txt"
'''

    def handle_if_basic_case(self, alphabet_size, array, *, LCP):
        '''\
handle_if_basic_case(alphabet_size, array, LCP=False) -> (None|(SA<array>, None))
handle_if_basic_case(alphabet_size, array, LCP=True) -> (None|(SA<array>, LCP<array>))
'''
        return None


    #, detect_whether_all_chars_are_different_at_top_layer=False):
    def uint_array2suffix_array(self, alphabet_size, array
            , *, table=None, handle_if_basic_case=None
            , LCP=False, make_RMQ=None, testing=False):
        '''uint_array2suffix_array :: UInt -> [UInt] -> [UInt]

uint_array2suffix_array(alphabet_size, uint_array) -> suffix_array
handle_if_basic_case(alphabet_size, array) -> (None|SA<array>)

time:
    assume:
        make_RMQ.'__init__' = O(n)*ops
        make_RMQ.'__call__' = O(1)*ops
    O(L+alphabet_size)

input:
    alphabet_size :: None | UInt
    string :: [Char]
        Char = UInt[0..alphabet_size-1]
    table :: None | [[UInt]]
        mutable, may increase the size if nessesary
    handle_if_basic_case :: None | (UInt -> [UInt] -> (None|([UInt], (None, [UInt])))
        this funtion define what is basic case and handle it
    LCP :: bool
        # LCP - longest common prefix of adjacent suffices in SA<string>
        if LCP:
            then output will become (suffix_array, lcp_array)
    make_RMQ :: None | Ord a => [a]{1..} -> (ArrayBeginIdx -> ArrayEndIdx -> ArrayBeginIdx)
        make_RMQ :: nonempty_array -> (begin -> end -> min_idx)
        0 <= begin <= min_idx < end <= len(nonempty_array)
        nonempty_array[min_idx] == min(nonempty_array[begin:end])
        min_idx need not be unique



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
    >>> _this = UIntArray2SuffixArray__ver5().uint_array2suffix_array
    >>> this = lambda *args, **kwargs: _this(*args, testing=True, **kwargs)
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
    >>> this(None, [1,1,1,0])
    [3, 2, 1, 0]
    >>> this(None, b'112233112233')
    [6, 0, 7, 1, 8, 2, 9, 3, 11, 5, 10, 4]
    >>> this(None, [1,1,1])
    [2, 1, 0]

    # LCP=True
    >>> thisLCP = lambda *args, **kwargs: _this(None, *args, LCP=True, testing=True, **kwargs)
    >>> thisLCP(b'231')
    ([2, 0, 1], [0, 0])
    >>> thisLCP([1,1,1,0])
    ([3, 2, 1, 0], [0, 1, 2])
    >>> thisLCP(b'112233112233')
    ([6, 0, 7, 1, 8, 2, 9, 3, 11, 5, 10, 4], [6, 1, 5, 0, 4, 1, 3, 0, 1, 1, 2])
    >>> thisLCP([1,1,1])
    ([2, 1, 0], [1, 2])

    >>> thisLCP(b'0120121')
    ([0, 3, 6, 1, 4, 2, 5], [3, 0, 1, 2, 0, 1])
    >>> thisLCP(b'100100100')
    ([8, 7, 4, 1, 5, 2, 6, 3, 0], [1, 2, 5, 1, 4, 0, 3, 6])
    >>> thisLCP(b'100100')
    ([5, 4, 1, 2, 3, 0], [1, 2, 1, 0, 3])

methods:
    # recur
        ___this
        __this

    # main
        uint_array2suffix_array
        make_big_string
        make_LCP

    # basic
        bucket_sort
        handle_if_all_the_same
        handle_if_all_unique
        handle_if_basic_case

    # other makes
        make_charL2endSA
        make_ichar2depth
        make_isuffix2is_L
        make_pseudo_LMS_substring_suffices_LCP
        make_pseudo_sorted_LMS_substring_isuffices
        #make_sorted_LMS_substring_isuffices



    # scan
        scan_both_directions
        scan_from_left_to_right
        scan_from_right_to_left
        swap_bijection

        append_left
        append_left__some_sorted_S_isuffices
        append_right
        #append_right__some_sorted_L_isuffices

    # verify
        verify_SA_LCP
        verify_arbitrary_LCP
        verify_big_string
        verify_ibucket_bound
        verify_ichar2big_ichar
        verify_pseudo_sorted_LMS_substring_isuffices




refs:
    [SA][LCP][2011]Inducing the LCP-Array (Johannes Fischer).pdf
    [SA][2009]Linear Suffix Array Construction by Almost Pure Induced-Sorting (Ge Nong).pdf
    [SA][2004]Space efficient linear time construction of suffix arrays (Pang Ko).pdf
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

        self.testing = bool(testing)
        self.LCP = bool(LCP)
        if self.LCP:
            if make_RMQ is None:
                make_RMQ = rmq_from_array
        self.make_RMQ = make_RMQ


        L = len(string)
        #table = [[] for _ in range(max(alphabet_size, L))]
        SA, may_LCP = self.__this(
                        alphabet_size, string, onto=False)
        if self.LCP and may_LCP is not None:
            LCP = may_LCP
            return SA, LCP
        if not self.LCP and may_LCP is None:
            return SA
        return logic-error

    def verify_SA_LCP(self, string, SA, may_LCP):
        SA_def = suffix_array_definition(string)
        b1 = SA == SA_def
        b2 = True
        if self.LCP:
            LCP_def = lcp_array_definition(string, SA)
            b2 = may_LCP == LCP_def
        return b1 and b2
    def verify_ibucket_bound(self, alphabet_size, string, SA_def
                            , ibucket2beginSA, ibucket2endSA):
        L = len(string)

        b1 = len(ibucket2beginSA) == len(ibucket2endSA) == alphabet_size
        b2 = ibucket2beginSA[1:] == ibucket2endSA[:-1]
        if not (b1 and b2): return False

        if alphabet_size:
            b1 = ibucket2beginSA[0] == 0
            b2 = ibucket2endSA[-1] == L
            if not (b1 and b2): return False

        for char, beginSA, endSA in zip(range(L), ibucket2beginSA, ibucket2endSA):
            b1 = 0 <= beginSA <= endSA <= L
            b2 = all(string[ichar] == char for ichar in SA_def[beginSA:endSA])
            if not (b1 and b2): return False
        return True
    """
    def verify_sorted_LMS_substring_isuffices__deprecated(self
            , to_LMS_substring_suffix, sorted_LMS_substring_isuffices):
        '''
        NOTE:
            sorted_LMS_substring_isuffices
                * exclude_1size_suffices except string[-1:]
                * include leading L suffices
        '''
        [*LMS_substring_suffices] = map(to_LMS_substring_suffix, sorted_LMS_substring_isuffices)
        if not is_sorted(LMS_substring_suffices): return False
        if not is_uint_bijection_array(sorted_LMS_substring_isuffices):
            return False
        return True
        to_LMS_substring_suffix
    """
    def verify_pseudo_sorted_LMS_substring_isuffices(self
            , to_pseudo_LMS_substring_suffix, pseudo_sorted_LMS_substring_isuffices):
        '''
        NOTE:
            pseudo_sorted_LMS_substring_isuffices
                * exclude_1size_suffices except string[-1:]
                * include leading L suffices
        '''
        [*pseudo_LMS_substring_suffices] = map(to_pseudo_LMS_substring_suffix, pseudo_sorted_LMS_substring_isuffices)
        if not is_sorted(pseudo_LMS_substring_suffices): return False
        if not is_uint_bijection_array(pseudo_sorted_LMS_substring_isuffices):
            return False
        return True

    def verify_ichar2big_ichar(self, string, isuffix2is_L, isuffix2is_LMS, ichar2big_ichar):
        # skip leaing L
        L = len(string)
        it = range(L)
        ichar = -1
        for ichar in it:
            may_big_ichar = ichar2big_ichar[ichar]
            if may_big_ichar is not None:
                first_LMS_ichar_or_end = ichar
                break
        else:
            first_LMS_ichar_or_end = ichar+1
        if not all(map(isuffix2is_L, range(first_LMS_ichar_or_end))):
            return False

        prev_big_ichar = -1
        for ichar in range(first_LMS_ichar_or_end, L):
            big_ichar = ichar2big_ichar[ichar]
            if big_ichar != prev_big_ichar:
                if not isuffix2is_LMS(ichar): return False
            else:
                if isuffix2is_LMS(ichar): return False
            prev_big_ichar = big_ichar
        return True

    def verify_arbitrary_LCP(self, suffices, LCP):
        if not suffices:
            return not LCP
        L = len(suffices)
        if not len(LCP) == L-1: return False
        LCP_def = [len_lcp_f(s1, s2) for s1, s2 in zip_me2(suffices)]
        return LCP == LCP_def


    def verify_big_string(self
            , ichar2big_ichar
            , to_pseudo_LMS_substring_suffix
            , big_ichar2LMS_isuffix, big_alphabet_size, big_string):
        big_char2pseudo_LMS_isuffices = [[] for _ in range(big_alphabet_size)]
        for big_ichar, big_char in enumerate(big_string):
            LMS_isuffix = big_ichar2LMS_isuffix[big_ichar]
            if not ichar2big_ichar[LMS_isuffix] == big_ichar:
                return False

            pseudo_LMS_substring_suffix = to_pseudo_LMS_substring_suffix(LMS_isuffix)
            big_char2pseudo_LMS_isuffices[big_char].append(pseudo_LMS_substring_suffix)
        if not all(map(all_the_same, big_char2pseudo_LMS_isuffices)):
            return False
        if not is_strict_sorted(big_char2pseudo_LMS_isuffices, key=lambda ls: ls[0]):
            return False

        if big_string:
            # last big_char is unique
            last_big_char = big_string[-1]
            if any(big_char == last_big_char for big_char in big_string[:-1]):
                return False
        return True




    def handle_if_all_the_same(self, L):
        # no S
        # return None | (SA, may_LCP)
        if self.LCP:
            #bug: may_LCP = [L-1-i for i in range(L-1)]
            may_LCP = list(range(1, L))
        else:
            may_LCP = None
        SA = list(reversed(range(L)))

        return SA, may_LCP
    def handle_if_all_unique(self, alphabet_size, string):
        # return None | (SA, may_LCP)
        L = len(string)
        if self.LCP:
            may_LCP = [0]*(L-1)
        else:
            may_LCP = None
        SA = self.bucket_sort(alphabet_size, range(L), key=string.__getitem__)

        return SA, may_LCP

    ######################### begin ################################
    def __this(self, alphabet_size, string, *, onto):
        SA, may_LCP = self.___this(alphabet_size, string, onto=onto)
        if self.testing: assert self.verify_SA_LCP(string, SA, may_LCP)
        return SA, may_LCP

    def ___this(self, alphabet_size, string, *, onto):
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

        assert alphabet_size >= 1
        assert not onto or alphabet_size <= L


        are_all_the_same = are_all_unique = False
        if alphabet_size == 1:
            are_all_the_same = True
        elif onto and alphabet_size == L:
            are_all_unique = True
        elif not onto:
            # __init__; top layer __this
            if all_the_same(string):
                are_all_the_same = True
            elif alphabet_size >= L and all_unique(alphabet_size, string):
                are_all_unique = True

        may_result = None
        if are_all_the_same:
            may_result = self.handle_if_all_the_same(L)
        elif are_all_unique:
            may_result = self.handle_if_all_unique(alphabet_size, string)
        ###
        if may_result is not None:
            SA, may_LCP = may_result
            return SA, may_LCP
        del may_result, are_all_the_same, are_all_unique



        if self.testing:
            SA_def = suffix_array_definition(string)
            LCP_def = lcp_array_definition(string, SA_def)

        # char == ibucket
        ibucket2size = bucket_count(alphabet_size, string)
        ibucket2endSA = tuple(accumulate(ibucket2size))
        ibucket2beginSA = (0, *ibucket2endSA[:-1])
        #charL2size
        #charS2size
        charL2beginSA = ibucket2beginSA
        charS2endSA = ibucket2endSA
        if self.testing:
            assert self.verify_ibucket_bound(alphabet_size, string, SA_def
                                        , ibucket2beginSA, ibucket2endSA)


        ( big_alphabet_size, big_string
            , isuffix2is_L
            , big_isuffix2LMS_isuffix
            #, sorted_LMS_substring_isuffices
            , pseudo_sorted_LMS_substring_isuffices
            , isuffix2is_LMS
            , ichar2big_ichar
            , to_LMS_substring_suffix
            #, to_pseudo_LMS_substring_suffix
            ) = self.make_big_string(alphabet_size, string, charL2beginSA, charS2endSA)
        #isuffix2is_L = isuffix2is_L.__getitem__




        big_stringSA, may_big_stringLCP = self.__this(
                big_alphabet_size, big_string, onto=True)
        #big_stringLCP_RMQ
        sorted_big_isuffices = big_stringSA
        sorted_LMS_isuffices = [big_isuffix2LMS_isuffix[big_isuffix]
                                for big_isuffix in sorted_big_isuffices]
            #[for LMS_isuffix in big_isuffix2LMS_isuffix]

        if self.testing:
            assert is_strict_sorted(big_stringSA
                            , key=lambda big_isuffix: big_string[big_isuffix:])
            try:
                assert is_strict_sorted(sorted_LMS_isuffices
                                , key=lambda isuffix: string[isuffix:])
            except:
                print([*map(lambda isuffix: string[isuffix:]
                        , sorted_LMS_isuffices)])
                raise


        # ???unorderedSA is bucketted_unorderedSA?? YES!!
        unorderedSA = pseudo_sorted_LMS_substring_isuffices
        del pseudo_sorted_LMS_substring_isuffices
        #bug:unorderedSA = list(range(L))

        inv_unorderedSA = inverse_uint_bijection_array(unorderedSA)
        # using sorted_LMS_isuffices inside unorderedSA
        charS2curr_idxSA = list(charS2endSA)
        self.append_left__some_sorted_S_isuffices(
                        sorted_LMS_isuffices
                        , charS2curr_idxSA, unorderedSA, inv_unorderedSA
                        , string)
        unorderedSA__sorted_LMS_isuffices = unorderedSA; del unorderedSA
        del charS2curr_idxSA

        self.scan_both_directions(charL2beginSA, charS2endSA
                , unorderedSA__sorted_LMS_isuffices, inv_unorderedSA
                , string, isuffix2is_L
                , None
                , first_round_exclude_S = False
                )
        SA = unorderedSA__sorted_LMS_isuffices
        invSA = inv_unorderedSA
        del unorderedSA__sorted_LMS_isuffices
        del inv_unorderedSA



        mayLCP = None
        if self.LCP:
            assert may_big_stringLCP is not None
            big_stringLCP = may_big_stringLCP

            LCP = self.make_LCP(
                    alphabet_size, string
                    , ibucket2beginSA, ibucket2endSA
                    , isuffix2is_L, isuffix2is_LMS
                    , SA, invSA
                    , ichar2big_ichar
                    , big_isuffix2LMS_isuffix
                    , big_stringSA
                    , big_stringLCP
                    , to_LMS_substring_suffix
                    #, to_pseudo_LMS_substring_suffix
                    )

            mayLCP = LCP
        return SA, mayLCP

    def make_ichar2depth(self, string):
        assert string
        L = len(string)
        ichar2depth = [0]*L
        prev_depth = 0 # ichar2depth[-1] == 0
        for i in reversed(range(L-1)):
            curr_char = string[i]
            succ_char = string[i+1]
            if curr_char == succ_char:
                depth = prev_depth+1
            else:
                depth = 0
            prev_depth = ichar2depth[i] = depth
        return ichar2depth

    def make_LCP(self
                , alphabet_size, string
                , ibucket2beginSA, ibucket2endSA
                , isuffix2is_L, isuffix2is_LMS
                , SA, invSA
                , ichar2big_ichar
                , big_isuffix2LMS_isuffix
                , big_stringSA
                , big_stringLCP
                , to_LMS_substring_suffix
                #, to_pseudo_LMS_substring_suffix
                ):
        ichar2depth = self.make_ichar2depth(string)
        pseudo_LMS_substring_suffices_LCP = self.make_pseudo_LMS_substring_suffices_LCP(
                                    alphabet_size, string
                                    , ibucket2beginSA, ibucket2endSA
                                    , isuffix2is_L, isuffix2is_LMS
                                    , SA, invSA
                                    , to_LMS_substring_suffix
                                    #, to_pseudo_LMS_substring_suffix
                                    , ichar2depth
                                    )
        if self.testing:
            [*LMS_substring_suffices] = map(to_LMS_substring_suffix, SA)
            assert self.verify_arbitrary_LCP(
                        LMS_substring_suffices, pseudo_LMS_substring_suffices_LCP)



        pseudo_LMS_substring_suffices_LCP_RMQ = self.make_RMQ(pseudo_LMS_substring_suffices_LCP)
        big_stringLCP_RMQ = self.make_RMQ(big_stringLCP) if big_stringLCP else None
        inv_bigSA = inverse_uint_bijection_array(big_stringSA)
        L = len(string)
        def len_lcp_at(idxLCP):
            len_lcp = _len_lcp_at(idxLCP)
            if self.testing:
                def idxSA2suffix(idxSA):
                    isuffix = SA[idxSA]
                    suffix = string[isuffix:]
                    return suffix
                len_lcp_def = len_lcp_f(idxSA2suffix(idxLCP), idxSA2suffix(idxLCP+1))

                try:
                    assert len_lcp == len_lcp_def
                except:
                    print(len_lcp, len_lcp_def)
                    print(idxLCP)
                    print(SA, string)
                    print(idxSA2suffix(idxLCP), idxSA2suffix(idxLCP+1))
                    raise
            return len_lcp

        def _len_lcp_at(idxLCP):
            assert 0 <= idxLCP < L-1
            len_lcp = pseudo_LMS_substring_suffices_LCP[idxLCP]
            isuffix = SA[idxLCP]
            end_isuffix = isuffix + len_lcp
            neighbor_isuffix = SA[idxLCP+1]
            end_neighbor_isuffix = neighbor_isuffix + len_lcp

            '''bug:
            if (len_lcp <= 1
                or end_isuffix == L or end_neighbor_isuffix == L
                or not isuffix2is_LMS(end_isuffix-1)
                or not isuffix2is_LMS(end_neighbor_isuffix-1)):
                return len_lcp
            '''
            if (len_lcp <= 1
                or end_isuffix == L or end_neighbor_isuffix == L):
                return len_lcp

            b_0 = bool(isuffix2is_LMS(end_isuffix-1))
            b_1 = bool(isuffix2is_LMS(end_neighbor_isuffix-1))
            if b_0 != b_1:
                # one and only one end_at LMS_char
                # NOTE:
                #   one     = _ ++ larger_char : LMS_char : _ (going up)
                #           = _ ++ larger_char : smaller_char : ??
                #   another = _ ++ larger_char : non_LMS_char : _ (going down)
                #           = _ ++ larger_char : smaller_char : ??
                assert len_lcp >= 2
                min_depth = min(ichar2depth[end_isuffix-1]
                              , ichar2depth[end_neighbor_isuffix-1])
                return len_lcp + min_depth # neednot (+1)
            elif not b_0:
                # both not end_at LMS_char
                return len_lcp
            else:
                pass

            #######
            assert (len_lcp >= 2
                and isuffix2is_LMS(end_isuffix-1)
                and isuffix2is_LMS(end_neighbor_isuffix-1)
                )

            # section1: donot include the last LMS_char in the first may_incomplete LMS_substring
            len_lcp_section1 = len_lcp-1; del len_lcp

            # section2 via big_string
            first_big_ichar = ichar2big_ichar[end_isuffix-1]
            last_big_ichar = ichar2big_ichar[end_neighbor_isuffix-1]
            #bug:assert end_isuffix < end_neighbor_isuffix
            #bug:assert first_big_ichar < last_big_ichar
            #bug: min_idx_bigLCP = big_stringLCP_RMQ(first_big_ichar, last_big_ichar)
                # [first_bigSA:last_bigSA]
            assert invSA[end_isuffix-1] < invSA[end_neighbor_isuffix-1]
            assert inv_bigSA[first_big_ichar] < inv_bigSA[last_big_ichar]
            min_idx_bigLCP = big_stringLCP_RMQ(inv_bigSA[first_big_ichar]
                                             , inv_bigSA[last_big_ichar])


            big_min_len_lcp = big_stringLCP[min_idx_bigLCP]
            assert big_min_len_lcp >= 0 # not >= 1
            end_first_big_isuffix_ex = first_big_ichar + big_min_len_lcp
            assert end_first_big_isuffix_ex != len(big_stringSA)
                # since last big_char is unique
            end_first_big_isuffix = end_first_big_isuffix_ex
            end_end_isuffix = big_isuffix2LMS_isuffix[end_first_big_isuffix]
            len_lcp_2sections = end_end_isuffix - isuffix

            assert isuffix2is_LMS(end_end_isuffix)
            end_end_LMS_isuffix = end_end_isuffix
            end_end_neighbor_LMS_isuffix = neighbor_isuffix + len_lcp_2sections
            assert isuffix2is_LMS(end_end_neighbor_LMS_isuffix)

            #bug:len_lcp_section3 = pseudo_LMS_substring_suffices_LCP_RMQ(
            #       invSA[end_end_LMS_isuffix], invSA[end_end_neighbor_LMS_isuffix])
            # RMQ return min_idx not min_val
            #
            min_idxLCP_section3 = pseudo_LMS_substring_suffices_LCP_RMQ(
                invSA[end_end_LMS_isuffix], invSA[end_end_neighbor_LMS_isuffix])
            len_lcp_section3 = pseudo_LMS_substring_suffices_LCP[min_idxLCP_section3]
            assert len_lcp_section3 >= 1
            len_lcp_3sections = len_lcp_2sections + len_lcp_section3
            #bug: return len_lcp_3sections
            #   there is section4!!!

            end_end_end_isuffix_ex = end_end_LMS_isuffix + len_lcp_section3
            end_end_end_neighbor_isuffix_ex = end_end_neighbor_LMS_isuffix + len_lcp_section3

            depth0 = ichar2depth[end_end_end_isuffix_ex-1]
            depth1 = ichar2depth[end_end_end_neighbor_isuffix_ex-1]
            len_lcp_section4 = min(depth0, depth1) # neednot (+1)
            len_lcp_4sections = len_lcp_3sections + len_lcp_section4
            return len_lcp_4sections
        ichar2big_ichar
        big_isuffix2LMS_isuffix
        big_stringLCP

        LCP = [len_lcp_at(i) for i in range(L-1)]
        return LCP

    def make_pseudo_LMS_substring_suffices_LCP(self
            , alphabet_size, string
            , ibucket2beginSA, ibucket2endSA
            , isuffix2is_L, isuffix2is_LMS
            # using SA instead of sorted_LMS_substring_isuffices
            , SA, invSA
            , to_LMS_substring_suffix
            #, to_pseudo_LMS_substring_suffix
            , ichar2depth
            ):
        # make_RMQ :: Ord a => [a]{1..} -> (ArrayBeginIdx -> ArrayEndIdx -> ArrayBeginIdx)

        assert string
        L = len(string)

        # finally, there are None in charX2LCP_RMQ # X for S/L
        charS2LCP_RMQ = [None]*alphabet_size
        charL2LCP_RMQ = [None]*alphabet_size
        pseudo_LMS_substring_suffices_LCP = [None]*(L-1)

        def len_lcp_at__LMS_substring_suffix(idxLCP):
            len_lcp = _len_lcp_at__LMS_substring_suffix(idxLCP)
            if self.testing:
                def idxSA2suffix(idxSA):
                    isuffix = SA[idxSA]
                    suffix = to_LMS_substring_suffix(isuffix)
                    return suffix
                len_lcp_def = len_lcp_f(idxSA2suffix(idxLCP), idxSA2suffix(idxLCP+1))
                assert len_lcp == len_lcp_def
            return len_lcp
        def _len_lcp_at__LMS_substring_suffix(idxLCP):
            # skip leaing Ls(not belong to any LMS_substring) or the head maybe incomplete LMS_substring
            assert 0 <= idxLCP < L-1
            idxSA = idxLCP

            # if isuffix2is_LMS(isuffix): ask the whole substring instead of the 1size suffix
            isuffix = SA[idxSA]
            neighbor_isuffix = SA[idxSA+1]
            head_char = string[isuffix]
            neighbor_head_char = string[neighbor_isuffix]
            if head_char != neighbor_head_char:
                return 0

            depth = ichar2depth[isuffix]
            neighbor_depth = ichar2depth[neighbor_isuffix]
            if depth != neighbor_depth:
                return 1+min(depth, neighbor_depth)

            #bug: skipped_isuffix = isuffix+depth
            skipped_isuffix = isuffix+ 1+depth
            skipped_neighbor_isuffix = neighbor_isuffix + 1+neighbor_depth
            if skipped_isuffix == L or skipped_neighbor_isuffix == L:
                return 1+depth
            idxLCP_0 = invSA[skipped_isuffix]
            idxLCP_1 = invSA[skipped_neighbor_isuffix] # may be L-1

            assert idxLCP_0 < idxLCP_1
            # RMQ[LCP[idxLCP_0..idxLCP_1-1]]
            # RMQ[LCP[idxLCP_0:idxLCP_1]]
            #bug: return LCP_RMQ__LMS_substring_suffix(idxLCP_0, idxLCP_1)
            return 1+depth+via_LCP_RMQ__LMS_substring_suffix(idxLCP_0, idxLCP_1)
        SA, invSA

        def via_LCP_RMQ__LMS_substring_suffix(beginLCP, endLCP):
            assert 0 <= beginLCP < endLCP <= L-1
            firstSA = beginLCP
            lastSA = endLCP
            first_isuffix = SA[firstSA]
            last_isuffix = SA[lastSA]
            first_head_char = string[first_isuffix]
            last_head_char = string[last_isuffix]
            if first_head_char != last_head_char:
                return 0

            # if isuffix2is_LMS(isuffix): ask the 1size suffix instead of the whole substring
            if isuffix2is_LMS(first_isuffix) or isuffix2is_LMS(last_isuffix):
                return 1

            # in same char_bucket
            if bool(isuffix2is_L(first_isuffix)) != bool(isuffix2is_L(last_isuffix)):
                first_depth = ichar2depth[first_isuffix]
                last_depth = ichar2depth[last_isuffix]
                return 1+min(first_depth, last_depth)


            # in same S_bucket or L_bucket
            head_char = first_head_char
            ibucket = head_char
            is_L = isuffix2is_L(first_isuffix)

            #bug:
            #   bucket_beginSA = ibucket2beginSA[ibucket]
            #   offsetLCP = bucket_beginLCP = bucket_beginSA
            bucketX_beginSA = ibucket2beginSA[ibucket] if is_L else\
                              charL2endSA[ibucket]
            offsetLCP = bucketX_beginLCP = bucketX_beginSA

            charX2LCP_RMQ = charL2LCP_RMQ if is_L else charS2LCP_RMQ
            LCP_RMQ = charX2LCP_RMQ[head_char]
            if LCP_RMQ is None:
                LCP_RMQ = charX2LCP_RMQ[head_char] = eval_LCP_RMQ(head_char, is_L)

            min_idxLCP = offsetLCP + LCP_RMQ(beginLCP-offsetLCP, endLCP-offsetLCP)
                # [firstSA:lastSA]
                # [beginLCP:endLCP]
                # [beginLCP..endLCP-1]
            return pseudo_LMS_substring_suffices_LCP[min_idxLCP]
        ibucket2beginSA, isuffix2is_L, isuffix2is_LMS

        charL2endSA = charS2beginSA = self.make_charL2endSA(
                                string, isuffix2is_L, ibucket2beginSA)

        def eval_LCP_RMQ(ibucket, is_L):
            char = ibucket
            #bug:
            #   beginSA = ibucket2beginSA[char]
            #   endSA = ibucket2endSA[char]
            if is_L:
                beginSA = ibucket2beginSA[char]
                endSA = charL2endSA[char]
            else:
                beginSA = charS2beginSA[char]
                endSA = ibucket2endSA[char]
            assert beginSA < endSA <= L # should not be an empty bucket

            beginLCP = beginSA
            #bug:endLCP = endSA
            endLCP = endSA-1
            assert beginLCP < endLCP <= L-1
            LCP = pseudo_LMS_substring_suffices_LCP[beginLCP:endLCP]
            assert not any(lcp is None for lcp in LCP)


            RMQ = self.make_RMQ(LCP)
            return RMQ
        ibucket2endSA#, make_RMQ

        # left to right: L_isuffix
        for idxLCP in range(L-1):
            isuffix = SA[idxLCP]
            if isuffix2is_L(isuffix):
                len_lcp = len_lcp_at__LMS_substring_suffix(idxLCP)
                pseudo_LMS_substring_suffices_LCP[idxLCP] = len_lcp

        # right to left: S_isuffix
        for idxLCP in reversed(range(L-1)):
            isuffix = SA[idxLCP]
            if not isuffix2is_L(isuffix):
                len_lcp = len_lcp_at__LMS_substring_suffix(idxLCP)
                pseudo_LMS_substring_suffices_LCP[idxLCP] = len_lcp

        assert not any(lcp is None for lcp in pseudo_LMS_substring_suffices_LCP)
        return pseudo_LMS_substring_suffices_LCP


    def make_charL2endSA(self, string, isuffix2is_L, ibucket2beginSA):
        L = len(string)
        ibucketL2size = [0]*len(ibucket2beginSA)
        for isuffix in range(L):
            if isuffix2is_L(isuffix):
                charL = string[isuffix]
                ibucketL2size[charL] += 1


        charL2endSA = charS2beginSA = [
                beginSA + sizeL
                for beginSA, sizeL in zip(ibucket2beginSA, ibucketL2size)]
        return charL2endSA




    def scan_both_directions(self, charL2beginSA, charS2endSA
            , _SA__sorted_some_S_isuffices, _invSA
            , string, isuffix2is_L
            , charL2curr_idxSA
            , *, first_round_exclude_S):
        assert not first_round_exclude_S
        assert charL2curr_idxSA is None

        if charL2curr_idxSA is None:
            charL2curr_idxSA = list(charL2beginSA)
        del charL2beginSA

        print('_SA__sorted_some_S_isuffices', _SA__sorted_some_S_isuffices)
        self.scan_from_left_to_right(
                            _SA__sorted_some_S_isuffices
                            , charL2curr_idxSA
                            , _invSA
                            , string
                            , isuffix2is_L
                            , exclude_S = first_round_exclude_S
                            )
        unorderedSA__sorted_L_isuffices = _SA__sorted_some_S_isuffices
        del _SA__sorted_some_S_isuffices
        del charL2curr_idxSA


        charS2curr_idxSA = list(charS2endSA); del charS2endSA
        print('unorderedSA__sorted_L_isuffices', unorderedSA__sorted_L_isuffices)
        self.scan_from_right_to_left(
                            unorderedSA__sorted_L_isuffices
                            , charS2curr_idxSA
                            , _invSA
                            , string
                            , isuffix2is_L
                            )
        _SA = unorderedSA__sorted_L_isuffices
        del unorderedSA__sorted_L_isuffices
        print('_SA', _SA)
        return
    """
    def append_right__some_sorted_L_isuffices(self
            , some_sorted_LMS_substring_isuffices
            , charL2curr_idxSA, _SA, _invSA, string):
        if self.testing:
            assert is_inverse_uint_bijection_array_of(_SA, _invSA)
        for icharL in some_sorted_LMS_substring_isuffices:
            self.append_right(_SA, charL2curr_idxSA, _invSA, icharL, string)

        if self.testing:
            assert is_inverse_uint_bijection_array_of(_SA, _invSA)
    """
    def append_left__some_sorted_S_isuffices(self
            , some_sorted_S_isuffices, charS2curr_idxSA, _SA, _invSA, string):

        if self.testing:
            assert is_inverse_uint_bijection_array_of(_SA, _invSA)
        for icharS in reversed(some_sorted_S_isuffices):
            self.append_left(_SA, charS2curr_idxSA, _invSA, icharS, string)
            #charS2curr_idxSA and _SA and _invSA are modified
            #charS2curr_idxSA--
            #_SA.swap
            #_invSA.swap
        if self.testing:
            assert is_inverse_uint_bijection_array_of(_SA, _invSA)
        return

    def swap_bijection(self, idxSA_0, idxSA_1, _SA, _invSA):
        if idxSA_0 == idxSA_1: return
        idx_invSA_0 = _SA[idxSA_0]
        idx_invSA_1 = _SA[idxSA_1]
        _SA[idxSA_0] = idx_invSA_1
        _SA[idxSA_1] = idx_invSA_0
        assert _invSA[idx_invSA_0] == idxSA_0
        assert _invSA[idx_invSA_1] == idxSA_1
        _invSA[idx_invSA_0] = idxSA_1
        _invSA[idx_invSA_1] = idxSA_0

    def append_left(self, _SA, charS2curr_idxSA, _invSA
                    , ichar, string):
        char = string[ichar]
        charS2curr_idxSA[char] -= 1
        curr_beginSA = charS2curr_idxSA[char]
        idxSA = _invSA[ichar]
        self.swap_bijection(idxSA, curr_beginSA, _SA, _invSA)
    def append_right(self, _SA, charL2curr_idxSA, _invSA
                    , ichar, string):
        char = string[ichar]
        curr_endSA = charL2curr_idxSA[char]
        charL2curr_idxSA[char] += 1
        idxSA = _invSA[ichar]
        self.swap_bijection(idxSA, curr_endSA, _SA, _invSA)

    def scan_from_left_to_right(self
                            , unorderedSA__sorted_LMS_isuffices
                            , charL2curr_idxSA
                            , inv_unorderedSA
                            , string
                            , isuffix2is_L
                            , *, exclude_S
                            ):
        assert not exclude_S

        _SA = unorderedSA__sorted_LMS_isuffices
        _invSA = inv_unorderedSA
        if self.testing:
            assert is_inverse_uint_bijection_array_of(_SA, _invSA)

        L = len(string)


        if not exclude_S:
            # handle the empty suffix '', i.e. '$'
            ichar = L-1 # last char = last L char = char before '$'
            self.append_right(_SA, charL2curr_idxSA, _invSA, ichar, string)

        for isuffix in _SA:
            if isuffix > 0 and isuffix2is_L(isuffix-1):
                if exclude_S and not isuffix2is_L(isuffix):
                    continue
                ichar = isuffix-1
                self.append_right(_SA, charL2curr_idxSA, _invSA, ichar, string)
        if self.testing:
            assert is_inverse_uint_bijection_array_of(_SA, _invSA)
        return

    def scan_from_right_to_left(self
                            , unorderedSA__sorted_L_isuffices
                            , charS2curr_idxSA
                            , inv_unorderedSA
                            , string
                            , isuffix2is_L
                            ):
        _SA = unorderedSA__sorted_L_isuffices
        _invSA = inv_unorderedSA
        if self.testing:
            assert is_inverse_uint_bijection_array_of(_SA, _invSA)

        L = len(string)
        ichar = L-1 # last char = last L char = char before '$'

        for isuffix in reversed(_SA):
            if isuffix > 0 and not isuffix2is_L(isuffix-1):
                ichar = isuffix-1
                self.append_left(_SA, charS2curr_idxSA, _invSA, ichar, string)

        if self.testing:
            assert is_inverse_uint_bijection_array_of(_SA, _invSA)
        return

    def make_big_string(self, alphabet_size, string
            , charL2beginSA, charS2endSA):
        '''return (big_alphabet_size, big_string
            , isuffix2is_L :: ISuffix -> Bool
            , big_isuffix2LMS_isuffix
            #, sorted_LMS_substring_isuffices
            , pseudo_sorted_LMS_substring_isuffices
            , isuffix2is_LMS
            , ichar2big_ichar :: [(None|BigISuffix)]
            , to_LMS_substring_suffix
            #, to_pseudo_LMS_substring_suffix
            )

        NOTE:
            sorted_LMS_substring_isuffices
                * exclude_1size_suffices except string[-1:]
                * include leading L suffices
        '''
        L = len(string)


        isuffix2is_L = self.make_isuffix2is_L(string)
        isuffix2is_L = isuffix2is_L.__getitem__
        # isuffix2is_L done

        def isuffix2is_LMS(isuffix):
            return (not isuffix2is_L(isuffix)
                and (isuffix == 0 or isuffix2is_L(isuffix-1))
                )

        LMS_isuffices = list(filter(isuffix2is_LMS, range(L-1)))
            # may be empty
        big_ichar2LMS_isuffix = big_isuffix2LMS_isuffix = LMS_isuffices
        # big_isuffix2LMS_isuffix done


        ichar2big_ichar = [None]*L # may be all be None finally
        for big_ichar, (begin, end) in enumerate(zip_me2(chain(LMS_isuffices, [L]))):
            for i in range(begin, end):
                ichar2big_ichar[i] = big_ichar
        else:
            big_ichar = begin = end = None
            del big_ichar, begin, end

        if self.testing:
            print(string)
            print(ichar2big_ichar)
            assert self.verify_ichar2big_ichar(string
                    , isuffix2is_L, isuffix2is_LMS, ichar2big_ichar)


        # NOTE: assume 1size LMS_isuffix followed with '$'
        # so, ichar=L-1 isnot more special than LMS_ichars/1size LMS_isuffices
        '''bug:
        sorted_LMS_substring_isuffices =\
            self.make_sorted_LMS_substring_isuffices(
                                alphabet_size, string, table
                                , isuffix2is_L, LMS_isuffices
                                , charL2beginSA, charS2endSA)
        # sorted_LMS_substring_isuffices done
        if self.testing:
            assert self.verify_sorted_LMS_substring_isuffices(
                    to_LMS_substring_suffix, sorted_LMS_substring_isuffices)
        sorted_LMS_whole_substring_isuffices =\
            list(filter(isuffix2is_LMS, sorted_LMS_substring_isuffices))
        gs = groupby(sorted_LMS_whole_substring_isuffices
                    , key=to_LMS_substring_suffix)
        '''
        pseudo_sorted_LMS_substring_isuffices =\
            self.make_pseudo_sorted_LMS_substring_isuffices(
                                alphabet_size, string
                                , isuffix2is_L, LMS_isuffices
                                , charL2beginSA, charS2endSA)

        def to_pseudo_LMS_substring_suffix(isuffix):
            'to_LMS_substring_suffix append m/M'
            suffix = to_LMS_substring_suffix(isuffix)
            end_isuffix_ex = isuffix + len(suffix)
            mM = -1 if end_isuffix_ex == L else alphabet_size
            #pseudo_suffix = suffix + [mM] # type(suffix) may be input array type
            pseudo_suffix = [*suffix, mM]
            return pseudo_suffix
        def to_LMS_substring_suffix(isuffix):
            '''* include leading Ls
               * exclude_1size_suffices except string[-1:]
            '''
            may_big_ichar = ichar2big_ichar[isuffix]
            if may_big_ichar is None:
                next_big_ichar = 0
            else:
                big_ichar = may_big_ichar
                next_big_ichar = big_ichar+1
                del big_ichar

            if next_big_ichar == len(LMS_isuffices):
                return string[isuffix:]
            next_LMS_isuffix = LMS_isuffices[next_big_ichar]
            return string[isuffix:next_LMS_isuffix+1]


        if self.testing:
          try:
            assert self.verify_pseudo_sorted_LMS_substring_isuffices(
                    to_pseudo_LMS_substring_suffix, pseudo_sorted_LMS_substring_isuffices)
          except:
            print(string)
            print(pseudo_sorted_LMS_substring_isuffices)
            print(*map(to_pseudo_LMS_substring_suffix, pseudo_sorted_LMS_substring_isuffices))
            raise

        pseudo_sorted_LMS_whole_substring_isuffices =\
            list(filter(isuffix2is_LMS, pseudo_sorted_LMS_substring_isuffices))


        # O(L)
        gs = groupby(pseudo_sorted_LMS_whole_substring_isuffices
                    , key=to_pseudo_LMS_substring_suffix)
        big_string = [None]*len(LMS_isuffices)
        big_char = -1
        for big_char, (_, g) in enumerate(gs):
            for LMS_isuffix in g:
                big_ichar = ichar2big_ichar[LMS_isuffix]
                big_string[big_ichar] = big_char
        assert None not in big_string
        big_alphabet_size = big_char+1

        if self.testing:
            assert self.verify_big_string(
                ichar2big_ichar
                , to_pseudo_LMS_substring_suffix
                , big_ichar2LMS_isuffix, big_alphabet_size, big_string)

        return (
            big_alphabet_size, big_string
            , isuffix2is_L
            , big_isuffix2LMS_isuffix
            #, sorted_LMS_substring_isuffices
            , pseudo_sorted_LMS_substring_isuffices
            , isuffix2is_LMS
            , ichar2big_ichar
            , to_LMS_substring_suffix
            #, to_pseudo_LMS_substring_suffix
            )
    def make_pseudo_sorted_LMS_substring_isuffices(self
            , alphabet_size, string, isuffix2is_L, LMS_isuffices
            , charL2beginSA, charS2endSA):
        # LMS_substring
        L = len(string)

        # radix sort on \ichar->(string[ichar], not isuffix2is_L(ichar))
        unorderedSA = range(L)
        unorderedSA = self.bucket_sort(
                2, unorderedSA, key=lambda ichar: not isuffix2is_L(ichar))
        unorderedSA = self.bucket_sort(
                alphabet_size, unorderedSA, key=string.__getitem__)
        unorderedSA__LS_bucketted__sorted_LMS_substring_S_1size_isuffices = unorderedSA
        inv_unorderedSA = inverse_uint_bijection_array(unorderedSA)
        del unorderedSA

        self.scan_both_directions(charL2beginSA, charS2endSA
                , unorderedSA__LS_bucketted__sorted_LMS_substring_S_1size_isuffices
                , inv_unorderedSA
                , string, isuffix2is_L
                , None
                , first_round_exclude_S = False)
        pseudo_sorted_LMS_substring_isuffices = \
            unorderedSA__LS_bucketted__sorted_LMS_substring_S_1size_isuffices
        return pseudo_sorted_LMS_substring_isuffices

    """
    def make_sorted_LMS_substring_isuffices__deprecated(self
            , alphabet_size, string, table, isuffix2is_L, LMS_isuffices
            , charL2beginSA, charS2endSA):
        # LMS_substring
        L = len(string)

        sorted_LMS_substring_S_1size_isuffices = bucket_sort(
                        alphabet_size, LMS_isuffices
                        , table, key=string.__getitem__)
        # ???unorderedSA is bucketted_unorderedSA?? YES!!
        unorderedSA = bucket_sort(
                alphabet_size, range(L), table, key=string.__getitem__)
        #bug:unorderedSA = list(range(L))

        inv_unorderedSA = inverse_uint_bijection_array(unorderedSA)
        charL2curr_idxSA = list(charL2beginSA)


        it = chain([L], sorted_LMS_substring_S_1size_isuffices)
        it = filter(lambda S_isuffix: S_isuffix != 0, it)
        sorted_LMS_substring_L_1size_2size_isuffices =\
            map(lambda LMS_isuffix_ex: LMS_isuffix_ex-1, it)

        # embedding sorted_LMS_substring_L_1size_2size_isuffices into unorderedSA
        self.append_right__some_sorted_L_isuffices(
                        sorted_LMS_substring_L_1size_2size_isuffices
                        , charL2curr_idxSA, unorderedSA, inv_unorderedSA
                        , string)
        unorderedSA__sorted_LMS_substring_L_1size_2size_isuffices = unorderedSA
        inv_unorderedSA = inverse_uint_bijection_array(unorderedSA)
        del unorderedSA, sorted_LMS_substring_L_1size_2size_isuffices


        #del charL2curr_idxSA
        self.scan_both_directions(charL2beginSA, charS2endSA
                , unorderedSA__sorted_LMS_substring_L_1size_2size_isuffices
                , inv_unorderedSA
                , string, isuffix2is_L
                , charL2curr_idxSA
                , first_round_exclude_S = True)
        sorted_LMS_substring_isuffices = \
            unorderedSA__sorted_LMS_substring_L_1size_2size_isuffices
        invLMS_substringSA = inv_unorderedSA
        del unorderedSA__sorted_LMS_substring_L_1size_2size_isuffices
        del inv_unorderedSA
        return sorted_LMS_substring_isuffices
    """


    def make_isuffix2is_L(self, string):
        # -> [Bool]
        assert string
        L = len(string)


        isuffix2is_L = [None]*L
        # the first succ char == the last char == the last L char
        isuffix2is_L[-1] = is_succ_L = True
        for prev_isuffix, (succ, prev) in zip(reversed(range(L-1)), zip_me2(reversed(string))):
            if prev < succ:
                # prev is S
                r = False
            elif prev > succ:
                # prev is L
                r = True
            else:
                r = is_succ_L

            is_succ_L = isuffix2is_L[prev_isuffix] = r

        return isuffix2is_L

    def bucket_sort(self, alphabet_size, iterable, *, key):
        table = self.table
        if len(table) < alphabet_size:
            table.extend([] for _ in range(alphabet_size - len(table)))
        assert len(table) >= alphabet_size

        return bucket_sort_with_table(
                alphabet_size, iterable, range(alphabet_size), table, key=key)



uint_array2suffix_array = UIntArray2SuffixArray__ver5().uint_array2suffix_array


def _t():
    this = lambda *args, **kwargs: uint_array2suffix_array(None, *args, LCP=True, testing=True, **kwargs)
    (0, 1, 2, 0, 1, 2, 1)
    this(b'0120121')
    this(b'100100100')
    assert this(b'100100') == ([5, 4, 1, 2, 3, 0], [1, 2, 1, 0, 3])
    this(b'112233112233')
    this(b'10101')
    this(b'100100')


if __name__ == "__main__":
    print = old_print
    print('\n'.join(dir(UIntArray2SuffixArray__ver5)))
    _t()
if __name__ == "__main__":
    print = new_print
    import doctest
    doctest.testmod()

'''
'''
