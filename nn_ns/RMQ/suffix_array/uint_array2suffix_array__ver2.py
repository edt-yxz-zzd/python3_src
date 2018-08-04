
'''

ver2 is a wrong impl!!!!!!!!!!!!!!!!
fire:
    assert [3,2,1,0] == uint_array2suffix_array(None, None, [1,1,1,0])

[1] < [1,0]
but [1,1,0] > [1,0]
we simply can treat unequal triples as a big char!!
    except those at last


string
    [1, 1, 1, 0]
singleton_or_pair_ls
    [[1], [1, 0]]
tmp_half_1round
    []
sorted_indices_of_singleton_or_pair_ls
    [0, 1]
SA_1_2
    [0, 1]
SA_0
    [1, 0]
SA
    [3, 0, 1, 2]


'''

















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



class UIntArray2SuffixArray__ver2:
    '''

array<uint> to sorted_suffix_indices

see: "SA - 2.1 make UIntSA ver2.txt"
'''

    def handle_if_basic_case(self, alphabet_size, array):
        '''handle_if_basic_case(array) -> (None|SA<array>)'''
        return None

    def uint_array2suffix_array(self, alphabet_size, array, *, table=None):
        '''global uint_array2suffix_array'''
        return uint_array2suffix_array(
                self.handle_if_basic_case, alphabet_size, array, table=table)


def uint_array2suffix_array(handle_if_basic_case
        , alphabet_size, array, *, table=None):
        #, detect_whether_all_chars_are_different_at_top_layer=False):
    '''uint_array2suffix_array :: UInt -> [UInt] -> [UInt]

uint_array2suffix_array(alphabet_size, uint_array) -> suffix_array
handle_if_basic_case(alphabet_size, array) -> (None|SA<array>)

input:
    handle_if_basic_case :: None | (UInt -> [UInt] -> (None|[UInt]))
    alphabet_size :: None | UInt
    string :: [Char]
        Char = UInt[0..alphabet_size-1]
    table :: None | [[UInt]]
        mutable, may increase the size if nessesary
output:
    suffix_array :: [UInt]
        suffix_array = SA<string>



see:
    seed.seq_tools.inverse_uint_bijection_array
        # the inverse of suffix_array is useful

example:
    >>> this = uint_array2suffix_array
    >>> wrapped_this = lambda s: this(None, None, tuple(map(int, s)))
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

'''

    if alphabet_size is None:
        alphabet_size = max(array, default=-1)+1
    elif not all(0 <= u < alphabet_size for u in array): raise ValueError

    string = array; del array
    if table is None:
        table = []
    if handle_if_basic_case is None:
        def handle_if_basic_case(alphabet_size, array):
            # handle_if_basic_case(alphabet_size, array) -> (None|SA<array>)
            return None

    # using "table"
    def bucket_sort(alphabet_size, iterable, *, key):
        if len(table) < alphabet_size:
            table.extend([] for _ in range(alphabet_size-len(table)))
        return _global_bucket_sort(alphabet_size, iterable, None, table, key=key)



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
        sorted_string_indices = bucket_sort(
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



    ######################### begin ################################
    def this(alphabet_size, string):
        L = len(string)

        ######################## basic case
        may_SA = handle_if_basic_case(alphabet_size, string)
        if may_SA is not None:
            return may_SA
        if L == 0:
            return []

        ######################## useless
        ######################## optional handle if all chars are different
        # when all chars are different:
        #   the suffix-tree is flatten
        #   we can simple sort chars
        if False:
            #see above and below instead
            #   above handle the global input string
            #   below handle before recur call
            #   so, this stmt body is useless

            #if is_strict_sorted(string): return list(range(L))
            # def key
            key = string.__getitem__
            # O(L)
            sorted_string_indices = bucket_sort(alphabet_size, range(L), key=key)
            if is_strict_sorted(sorted_string_indices, key=key):
                SA = sorted_string_indices
                return SA
            del key



        ######################## non-basic case
        # BEGIN: radix_sort singleton_or_pair_ls
        '''
        # bucket_sort all snd of pairs
        #   i.e. all snd of string[3z+2:...+2]
        #   i.e. string[3z+3]
        tmp = bucket_sort(range(1,Lx, 2)[:(|-1)], key=\i->string[i//2*3+2 +1])
            = bucket_sort(range(1,Lx-1, 2), key=\i->string[i//2*3+2 +1])
            when the last i2 not followed by i0 then exclude it
            i.e. when L = i2+1 = 3z+2+1 = 3x > 0
            i.e. when Lx = 2x > 0
        sorted_indices_of_singleton_or_pair_ls =
            bucket_sort(range(0,Lx,2)+ may last i2 +tmp
                        , key=\i->string[i//2*3+1+bool(i&1)])
        '''
        # def Lx
        Lx = L - ceil_div(L,3) # len(singleton_or_pair_ls)
        assert 0 <= Lx < L
        assert L == 1 or Lx > 0
        # O(L/3) half of the first bucket_sort round
        tmp_half_1round = bucket_sort(alphabet_size, range(1,Lx-1, 2)
                        , key=lambda i:string[i//2*3+2 +1])
        # the second bucket_sort round
        # last i2 = 2z+1 == Lx-1
        may_last_i2 = [Lx-1] if is_even(Lx) and Lx > 0 else []
        sorted_indices_of_singleton_or_pair_ls = (
            #or: bucket_sort(alphabet_size, chain(may_last_i2, range(0,Lx,2), tmp)
            bucket_sort(alphabet_size, chain(range(0,Lx,2), may_last_i2, tmp_half_1round)
                        , key=lambda i:string[i//2*3+1+bool(i&1)])
            )
        # END: radix_sort singleton_or_pair_ls

        ############################
        # BEGIN: make_array_idx2group_idx(singleton_or_pair_ls)
        # def key
        def key(i:'suffix_begin_of_singleton_or_pair_ls'):
            if is_odd(i):
                # i2
                i2 = i//2*3+2
                return string[i2:i2+2] # len == 1 or 2
            i1 = i//2*3 +1
            return string[i1:i1+1] # len == 1

        singleton_or_pair_ls_idx2group_idx = [None]*Lx
        gs = groupby(sorted_indices_of_singleton_or_pair_ls, key=key)
        group_idx = -1
        for group_idx, (_, g) in enumerate(gs):
            for singleton_or_pair_ls_idx in g:
                assert singleton_or_pair_ls_idx2group_idx[singleton_or_pair_ls_idx] is None
                singleton_or_pair_ls_idx2group_idx[singleton_or_pair_ls_idx]\
                    = group_idx
        group_idx_upper_bound = group_idx+1
        assert all(idx is not None for idx in singleton_or_pair_ls_idx2group_idx)

        assert 0 <= group_idx_upper_bound <= Lx < L
        assert 0 <= group_idx_upper_bound <= alphabet_size**2 + alphabet_size
            # may: group_idx_upper_bound > alphabet_size
        # END: make_array_idx2group_idx(singleton_or_pair_ls)

        # calc SA_1_2
        #if is_strict_sorted(sorted_indices_of_singleton_or_pair_ls, key=key):
        if group_idx_upper_bound == Lx:
            assert is_strict_sorted(sorted_indices_of_singleton_or_pair_ls, key=key)
            # all chars are different for SA_1_2
            SA_1_2 = sorted_indices_of_singleton_or_pair_ls
        else:
            # recur call
            assert not is_strict_sorted(sorted_indices_of_singleton_or_pair_ls, key=key)
            SA_1_2 = this(group_idx_upper_bound, singleton_or_pair_ls_idx2group_idx)
        del key
        ########################### SA_1_2 DONE

        ########################### SA_0
        '''
        def SA_0
        SA_0 = sorted(range(len(suffices_0)), key=\i->suffices_0[i])
            = sorted(range(len(suffices_0)), key=\i->string[3*i])
            where suffices_0 = [string[i:] for i in range(L) if i==3*_]
        def SA_1
        SA_1 = sorted(range(len(suffices_1)), key=\i->suffices_1[i])
            = sorted(range(len(suffices_1)), key=\i->string[3*i+1])
            where suffices_1 = [string[i:] for i in range(L) if i==3*_+1]

        invSA_1_2 = invUIntSA<singleton_or_pair_ls> = invSA<SA_1_2>
            # calc invSA is easy


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
        invSA_1_2 = inverse_uint_bijection_array(SA_1_2)
        SA_1 = [i_xy//2 for i_xy in SA_1_2 if is_even(i_xy)]
        may_last_i0 = [Lx>>1] if divs(3, L-1) else []
        #bug: tmp = bucket_sort(len(SA_1), SA_1, key=lambda i0: string[i0*3])
        tmpSA_0 = bucket_sort(alphabet_size, SA_1, key=lambda i0: string[i0*3])
        SA_0 = may_last_i0 + tmpSA_0 if may_last_i0 else tmpSA_0
        ########################### SA_0 DONE


        ########################### merge SA_0 and SA_1_2
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
        def i_xy_to_i_str(i_xy):
            return i_xy//2*3+1 +bool(i_xy&1)
        def le(i_str_0, i_str_1_2):
            # assert divs(3, i_str_0)
            # assert not divs(3, i_str_1_2)
            i0 = i_str_0//3
            i_xy_base = i_str_1_2//3*2
            r = i_str_1_2%3

            def may_invSA_1_2(i_xy):
                n = len(invSA_1_2)
                if n == i_xy:
                    return -1
                return invSA_1_2[i_xy]

            if r == 1:
                i_str_1 = i_str_1_2
                i1 = i_xy_base # + 0
                i2_after_i1 = i1+1

                i1_after_i0 = 2*i0 # + 0
                lhs = (string[i_str_0], may_invSA_1_2(i1_after_i0))
                rhs = (string[i_str_1], may_invSA_1_2(i2_after_i1))
            else:
                assert r == 2
                i_str_2 = i_str_1_2
                i2 = i_xy_base + 1
                i1_after_i2 = i2+1

                i2_after_i0 = 2*i0 + 1
                lhs = (string[i_str_0:i_str_0+2], may_invSA_1_2(i2_after_i0))
                rhs = (string[i_str_2:i_str_2+2], may_invSA_1_2(i1_after_i2))
            return lhs <= rhs

        #SA = merge le (map (3*) SA_0) (map i_xy_to_i_str SA_1_2)
        idc_str_0 = map(lambda i0:3*i0, SA_0)
        idc_str_1_2 = map(i_xy_to_i_str, SA_1_2)
        [*SA] = merge_two_sorted_iterables(idc_str_0, idc_str_1_2, __le__=le)
        if __debug__:
            singleton_or_pair_ls = [string[i:i+1+ divs(3, i-2)] for i in range(L) if not divs(3, i)]
            print(f'''
string
    {string}
singleton_or_pair_ls
    {singleton_or_pair_ls}
tmp_half_1round
    {tmp_half_1round}
sorted_indices_of_singleton_or_pair_ls
    {sorted_indices_of_singleton_or_pair_ls}
SA_1_2
    {SA_1_2}
SA_0
    {SA_0}
SA
    {SA}
''')
        input('...')
        return SA
    return this(alphabet_size, string)

if __name__ == "__main__":
    assert [3,2,1,0] == uint_array2suffix_array(None, None, [1,1,1,0])
    '''
string
    [1, 1, 1, 0]
singleton_or_pair_ls
    [[1], [1, 0]]
tmp_half_1round
    []
sorted_indices_of_singleton_or_pair_ls
    [0, 1]
SA_1_2
    [0, 1]
SA_0
    [1, 0]
SA
    [3, 0, 1, 2]
'''
    assert uint_array2suffix_array(None, None, b'112233112233') == [6, 0, 7, 1, 8, 2, 9, 3, 11, 5, 10, 4]
    assert [2,1,0] == uint_array2suffix_array(None, None, [1,1,1])
    import doctest
    doctest.testmod()

