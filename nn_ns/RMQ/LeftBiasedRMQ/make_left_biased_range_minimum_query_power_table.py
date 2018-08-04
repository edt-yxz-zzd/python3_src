
__all__ = '''
    make_left_biased_range_minimum_query_power_table

    verify_power_table
    verify_power_table_sizes
    verify_power_table_content
    '''.split()

from .common_methods import floor_log2, ceil_log2
from .array_to_idx2left_biased_rmq_control_range import VerifyLeftBiasedRMQ

def make_left_biased_range_minimum_query_power_table(array, up_to_length=None
        , *, offset=False):
    '''make_left_biased_range_minimum_query_power_table
    :: Ord a => [a]{1..} -> [[ArrayIdx]]

what?
    output[i][j] = let array = input[i:i+2^j] in
        min {idx | array[idx] == min(array)} + (if offset then 0 else i)
        where
            j is bounded by O(log(up_to_length))

######### time and space:
let n = len(array)
time O(n*log(up_to_length)) * (a.'<=' + uint[:n].'+-')
if not offset:
    space bit size O(n*log(up_to_length)*log(n))
        <<== space bit size O(n*log(min(up_to_length, n-idx)) * bit_size_of(idx))
else:
    space bit size O(n*log(up_to_length)**2)
        <<== space bit size O(n*log(min(up_to_length, n-idx)) * bit_size_of(idx-begin))


######## input and output
input:
    array :: Ord a => [a]{1..}
    up_to_length :: ArrayNonEmptyRangeEndIdx
        1 <= up_to_length <= len(array) == default
    offset :; bool
        if offset:
            then power_table :: [[OffsetedArrayIdx]]
            else power_table :: [[ArrayIdx]]
output:
    power_table :: [[ArrayIdx]] or [[OffsetedArrayIdx]]
        len_table = len(array)-1
        assert len(power_table) == len_table
        for begin in range(len_table):
            powerx2mayoffseted_min_element_array_idx = power_table[begin]
            ls_length = floor_log2(min(up_to_length, len(array) - begin))
            assert len(power_table[begin]) == ls_length >= 1

            for power in range(1, ls_length+1):
                min_idx = leftbiased_RMQ(array, begin, begin+2**power)
                mayoffsseted_min_idx = powerx2mayoffseted_min_element_array_idx[power-1]
                if offset:
                    assert mayoffsseted_min_idx+begin == min_idx
                else:
                    assert mayoffsseted_min_idx == min_idx

########## example
    >>> this = make_left_biased_range_minimum_query_power_table
    >>> this('1')
    []
    >>> this('12')
    [[0]]
    >>> this('21')
    [[1]]
    >>> this('123')
    [[0], [1]]
    >>> this('132')
    [[0], [2]]
    >>> this('213')
    [[1], [1]]
    >>> this('231')
    [[0], [2]]
    >>> this('312')
    [[1], [1]]
    >>> this('321')
    [[1], [2]]
    >>> this('1234')
    [[0, 0], [1], [2]]

    >>> this('1234' '567')
    [[0, 0], [1, 1], [2, 2], [3, 3], [4], [5]]
    >>> this('1234' '5678')
    [[0, 0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5], [6]]
    >>> this('1234' '5678' '9')
    [[0, 0, 0], [1, 1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6], [7]]

    >>> f = eval_and_verify_power_table
    >>> f('1234 5678 9')
    True
    >>> f('1234 95678 aff3sde44nog9 44r3 o3c')
    True

'''
    if not len(array) >= 1: raise ValueError
    # bug: power_table = [[]]*(len(array)-1)
    power_table = [[] for _ in range(len(array)-1)]

    n = len(array)
    if up_to_length is None:
        up_to_length = n
    else:
        if not 1 <= up_to_length <= len(array): raise ValueError
        up_to_length
    assert 1 <= up_to_length <= n

    def curr_min_idx():
        # array[curr_min_idx()] == min array[curr_idx:curr_idx+L]
        assert curr_ls is power_table[curr_idx]
        return curr_idx if L == 1 else curr_ls[-1]
    def curr():
        # curr() == min array[curr_idx:curr_idx+L]
        return array[curr_min_idx()]
    def succ_min_idx():
        # O(1) * uint[..n].'+-'
        # array[succ_min_idx()] == min array[curr_idx+L:curr_idx+L*2]
        succ_idx = curr_idx+L # ?? time O(1) | O(log(n))
        return succ_idx if L == 1 else power_table[succ_idx][-1]
    def succ():
        # succ() == min array[curr_idx+L:curr_idx+L*2]
        #succ_idx = curr_idx+L
        return array[succ_min_idx()]
    def put():
        # O(1) * (uint[..n].'+-' + a.'<=')
        curr_ls.append(curr_min_idx() if curr() <= succ() else succ_min_idx())



    L = 1 # == 2**power
        # known_basic_size(L) = L
        #   known RMQ(array, i, i+j) for j <- [1..2*L]
        #       i.e. by factor into 2 basic queries
        # range_length(prev_round) == L
        # range_length(curr_round) == 2*L == L2
        # succ_idx = curr_idx+L

    # num_rounds = floor_log2(up_to_length) # see below
    # ==>> num of 'put'
    # ==>> len(power_table[0] if any) = num_rounds
    #                                 = floor_log2(up_to_length)
    #                                 = floor_log2(min(up_to_length, n-0))
    # ==>> len(power_table[i] if any) = floor_log2(up_to_length(i))
    #                                 = floor_log2(min(up_to_length, n-i))
    #       where up_to_length(i) = min(up_to_length, len(array)-i)
    # len(power_table[i] if any) = floor_log2(min(up_to_length, n-i)) # here

    # each round we put item into ls in power_table[:end]
    # the last list is power_table[end-1]
    #   since the prev known_basic_size(L) == L
    #   the last one need to init is power_table[n-(2*L-1)]
    # ==>> end(L) = n-(2*L-1)
    end = n - (2*L-1) # may <= 0
        # power_table[end:] are final/finished
        # i.e. to compute power_table[:end] only if end > 0
        # assert len(array[end:]) == 2*L-1
        # assert end == n+1-L
    # ver1
    #   while not 2*L >= up_to_length:
    #       <<== [0<=i<j==i+up_to_length<=i+2*L][combine(RMQ(_, i, i+L), RMQ(_, j-L, j))]
    # but consider: ver1 ==>> len(power_table[0]) is not consistent with len(power_table[i])
    #   len(power_table[i]) =?= f(min(up_to_length, n-i))
    #   for example:
    #       '12' ==>> [[]]; but '123' ==>> [[0],[1]]
    #       0 = len(power_table<'12'>[0]) = f(min(2,2-0)) = f(2)
    #       1 = len(power_table<'123'>[1]) = f(min(3,3-1)) = f(2) != 0
    # ver2
    #   while not 2*L > up_to_length:
        #while 2*L <= up_to_length:
        #while L <= up_to_length/2:
        #while L <= floor(up_to_length/2):
        # not_final_L == 2**(power-1) <= up_to_length/2 < final_L == 2**power
        # ==>> power = floor_log2(up_to_length/2)+1 = floor_log2(up_to_length)
        # final_power = floor_log2(up_to_length) # here
        # ==>> num_rounds = number of non_final_powers = len [0..final_power-1]
        #               = final_power
        # num_rounds = floor_log2(up_to_length) # here
    floor_half_up_to_length = (up_to_length)//2
    while L <= floor_half_up_to_length:
        # 2*L <= up_to_length <= n ==>> end == n+1-2*L > 0
        #assert end == n+1-2*L > 0

        # end > 0
        # [0:end] = [0..end-1] is nonempty

        # O(n+1-2*L) * (uint[..n].'+-' + a.'<=')
        for curr_idx, curr_ls in zip(range(end), power_table):
            # O(1) * (uint[..n].'+-' + a.'<=')
            put()

        ####### next round
        # O(1) * (uint[..n].'-' + uint[..2*up_to_length].'<<1')
        # L' = 2*L
        # end(L') = n+1-2*L' = n+1-L' -L' = n+1-2*L -L' = end(L)-L'
        L <<= 1
            # range_length(prev_round) == L
            # range_length(curr_round) == 2*L
        end -= L

        # ?? end-L ~ time O(1) | O(log(n))
        # ?? L<<1 ~ time O(1) | O(log(up_to_length))

    #assert L == 2**floor_log2(up_to_length)
        # == 2**final_power == 2**num_rounds

    # number of 'put()'
    # = o(n+1-2*2**0 + n+1-2*2**1 + n+1-2*2**2 + ... + n+1-2*2**(num_rounds-1))
    # = o((n+1)*num_rounds-2*(2**0 + 2**1 + 2**2 + ... + 2**(num_rounds-1)))
    # = o((n+1)*num_rounds-2*(2**num_rounds-1))
    # = O(n*num_rounds-2**num_rounds)
    # = O(n*floor_log2(up_to_length) - 2**floor_log2(up_to_length))
    # = O(n*floor_log2(up_to_length) - up_to_length)
    # = O(n*floor_log2(up_to_length))
    #return power_table

    if False and __debug__:
        from sys import stderr
        assert len(power_table) == n-1
        #print(power_table)
        for idx, ls in enumerate(power_table):
            expect = floor_log2(min(up_to_length, n - idx))
            #print(n, idx, ls, expect, file=stderr)
            assert expect >= 1
            assert len(ls) == expect
    if offset:
        for curr_idx, curr_ls in enumerate(power_table):
            for i in range(len(curr_ls)):
                curr_ls[i] -= curr_idx
    return power_table












########## verify_power_table

def eval_and_verify_power_table(array, up_to_length=None, *, offset=False):
    power_table = make_left_biased_range_minimum_query_power_table(
                        array, up_to_length, offset=offset)
    return verify_power_table(array, up_to_length, offset, power_table)
def verify_power_table(array, up_to_length, offset, power_table):
    return (verify_power_table_sizes(len(array), up_to_length, power_table)
        and verify_power_table_content(array, offset, power_table)
        )

def verify_power_table_sizes(n, up_to_length, power_table):
    if up_to_length is None: up_to_length = n
    return (len(power_table) == n-1
        and all(len(ls) == floor_log2(min(up_to_length, n-idx))
                for idx, ls in enumerate(power_table))
        )

def verify_power_table_content(array, offset, power_table):
    tester = VerifyLeftBiasedRMQ(array)
    if offset:
        def add_begin_to(begin, ls):
            for rmq_result in ls:
                yield begin, rmq_result
    else:
        def add_begin_to(begin, ls):
            return iter(ls)
    for begin, ls in enumerate(power_table):
        it = add_begin_to(begin, ls)
        for power, rmq_result in enumerate(it, 1):
            range_size = 2**power
            end = begin+range_size
            if not tester.verify_left_biased_rmq_result(
                begin, end, rmq_result):
                return False
    return True



def _t():
    data = \
    [ ('1', [])
    , ('12', [[0]])
    ,  ('21', [[1]])
    ,  ('123', [[0], [1]])
    ,  ('132', [[0], [2]])
    ,  ('213', [[1], [1]])
    ,  ('231', [[0], [2]])
    ,  ('312', [[1], [1]])
    ,  ('321', [[1], [2]])
    ,  ('1234', [[0, 0], [1], [2]])

    ,  ('1234' '567', [[0, 0], [1, 1], [2, 2], [3, 3], [4], [5]])
    ,  ('1234' '5678', [[0, 0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5], [6]])
    ,  ('1234' '5678' '9', [[0, 0, 0], [1, 1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6], [7]])
    ]

    f = make_left_biased_range_minimum_query_power_table
    for s, o in data:
        n = len(s)
        assert verify_power_table_sizes(n, n, o)
        try:
            o2 = f(s)
        except:
            print(s, o)
            raise
        assert verify_power_table_sizes(n, n, o2)
        try:
            assert o == o2
        except:
            print('\t', s, o, o2)
            raise
if __name__ == "__main__":
    _t()
    import doctest
    doctest.testmod()



