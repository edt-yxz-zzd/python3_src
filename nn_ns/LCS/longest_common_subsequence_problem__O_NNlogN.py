
r'''

"[LCS]A Fast Algorithm for Computing Longest Common Subsequences (1977)(James W. Hunt)[O((N+R)logN)].pdf"
longest_common_subsequence_problem :: Eq a => [a] -> [a] -> [a]
longest_common_subsequence_problem lhs rhs


normally, time(longest_common_subsequence_problem, N) = O(N^2)

longest_common_subsequence_problem__O_NNlogN
    this algo be O((N+R)logN), but expected O(N*logN)
    where
        N = len(lhs) + len(rhs)
            # N is the size of input
        R = len(match_idx_pairs) = O(N^2)
        match_idx_pairs = {(i,j) | lhs[i] == rhs[j]}

needed_length_of_rhs_prefix :: Eq a => Integer -> ([a], Integer) -> [a] -> Maybe Integer
needed_length_of_rhs_prefix length_of_LCS (lhs, length_of_lhs_prefix) rhs
    = for j in range(len(rhs)):
        if len(LCS(lhs[:length_of_lhs_prefix]), rhs[:j]) == length_of_LCS:
            return $ Just j
      else:
        return Nothing
    = list2maybe $ do
        let lhs' = lhs[:length_of_lhs_prefix]
        rhs' <- inits rhs
        when (length (LCS lhs' rhs') == length_of_LCS)
            return $ length rhs'


[0 <= i <= len lhs][L >= 1][needed_length_of_rhs_prefix L i != Nothing]:
    [needed_length_of_rhs_prefix (L-1) i < needed_length_of_rhs_prefix L i]
    [0 <= i < len lhs]:
        [needed_length_of_rhs_prefix (L-1) i < needed_length_of_rhs_prefix L (i+1) <= needed_length_of_rhs_prefix L i]

        (*RECUR*)
        [needed_length_of_rhs_prefix L (i+1)
            == min ({j | needed_length_of_rhs_prefix (L-1) i < j < needed_length_of_rhs_prefix L i, lhs[i] == rhs[j-1]} \-/ {needed_length_of_rhs_prefix L i})
            ]


naive O(n^3) algo:
    M = 1 + min (len lhs) (len rhs) # > len (LCS lhs rhs)
    N = 1 + (len rhs)
    ls = [N] * M
              ^^^ [0..(M-1)]    - all possible values as index
         ^^^                    - init with the impossible/out-of-range value
    ls[0] = 0

    verify = lambda i: all(needed_length_of_rhs_prefix L i == Nothing if v == N else Just v for L, v in enumerate(ls))
    verify = lambda i: all(needed_length_of_rhs_prefix L i == Nothing if v == N else Just v for L in range(M) let v = ls[L])

    assert verify(0)
    for i in range(0, len(lhs)):
        assert verify(i)
        for j in reversed(range(len(rhs))):
            if lhs[i] == rhs[j]:
                # using (*RECUR*)
                find k s.t. ls[k-1] < j+1 <= ls[k]
                ls[k] = j+1
            # NOTE: ls is increasing
            # NOTE: k is decreasing when j-- per i
        assert verify(i+1)

    len_LCS = None
    for L, v in enumerate(ls):
        if v != N:
            len_LCS = L
    return len_LCS
'''


__all__ = '''
    calc_LCS__OlogNRlogN
    '''.split()

import bisect
from seed.types.pair_based_leftward_list import iter_leftward_list

def calc_naive_LEN_LCS__OlogNNN(lhs, rhs):
    lenL = len(lhs)
    lenR = len(rhs)
    M = 1 + min(lenL, lenR)
    N = 1 + lenR
    ls = [N] * M
    ls[0] = 0

    #verify = lambda i: all(needed_length_of_rhs_prefix L i == Nothing if v == N else Just v for L in range(M) let v = ls[L])

    #assert verify(0)
    for i in range(0, lenL):
        #assert verify(i)
        k = len(ls) - 1
        for j in reversed(range(lenR)):
            if lhs[i] == rhs[j]:
                # using (*RECUR*)
                for k in reversed(range(1, k+1)):
                    if ls[k-1] < j+1 <= ls[k]:
                        break
                else:
                    raise logic-error
                ls[k] = j+1
            # NOTE: ls is increasing
            # NOTE: k is decreasing when j-- per i
        #assert verify(i+1)
    len_LCS = None
    for len_LCS, v in enumerate(ls):
        if v == N:
            len_LCS -= 1
            break
    else:
        if len_LCS is None:
            raise logic-error

    return len_LCS


assert calc_naive_LEN_LCS__OlogNNN('', '') == 0
assert calc_naive_LEN_LCS__OlogNNN('1', '2') == 0
assert calc_naive_LEN_LCS__OlogNNN('1', '1') == 1
assert calc_naive_LEN_LCS__OlogNNN('1234567', '351246') == 4
assert calc_naive_LEN_LCS__OlogNNN('1234567', '35146') == 3



def calc_LCS__OlogNRlogN(lhs, rhs):
    def find_len_of_same_prefix(idc, lhs, rhs):
        i = -1
        #for i, (L, R) in enumerate(zip(lhs, rhs)):
        for i, L, R in zip(idc, lhs, rhs):
            if L != R: break
        else:
            i += 1
        L = i
        return L

    lenL = len(lhs)
    lenR = len(rhs)
    minLEN = min(lenL, lenR)
    prefixLEN = find_len_of_same_prefix(range(lenL), lhs, rhs)
    suffixLEN = find_len_of_same_prefix(range(minLEN-prefixLEN), reversed(lhs), reversed(rhs))
    assert prefixLEN + suffixLEN <= minLEN

    if prefixLEN == 0 and suffixLEN == 0:
        LCS = _calc_LCS__OlogNRlogN(lhs, rhs)
    else:
        lhs_ = lhs[prefixLEN:lenL-suffixLEN]
        rhs_ = rhs[prefixLEN:lenR-suffixLEN]
        LCS_ = _calc_LCS__OlogNRlogN(lhs_, rhs_)
        LCS = [*lhs[:prefixLEN], *LCS_, *lhs[lenL-suffixLEN:]]
    return LCS


def _calc_LCS__OlogNRlogN(lhs, rhs):
    lenL = len(lhs)
    lenR = len(rhs)
    M = 1 + min(lenL, lenR)
    N = 1 + lenR
    ls = [N] * M
    ls[0] = 0

    char2decreasing_Js = {}
    for j in reversed(range(lenR)):
        char = rhs[j]
        Js = char2decreasing_Js.setdefault(char, [])
        Js.append(j)

    #verify = lambda i: all(needed_length_of_rhs_prefix L i == Nothing if v == N else Just v for L in range(M) let v = ls[L])

    #assert verify(0)
    #leftward_list = ()
    idx2reversed_linked_LCS = [None]*M
    idx2reversed_linked_LCS[0] = ()
    for i in range(0, lenL):
        #assert verify(i)
        k = len(ls) - 1
        for j in char2decreasing_Js.get(lhs[i], ()):
            # using (*RECUR*)
            # NOTE: ls is increasing
            # NOTE: k is decreasing when j-- per i
            k_ = bisect.bisect_left(ls, j+1, 1, k+1)
            assert 1 <= k_ <= k
            k = k_

            if j+1 < ls[k]:
                ls[k] = j+1
                #leftward_list = ((i,j), leftward_list)
                idx2reversed_linked_LCS[k] = (lhs[i], idx2reversed_linked_LCS[k-1]) # k-1>=0
        #assert verify(i+1)

    len_LCS = None
    for len_LCS, v in enumerate(ls):
        if v == N:
            len_LCS -= 1
            break
    else:
        if len_LCS is None:
            raise logic-error

    [*LCS] = iter_leftward_list(idx2reversed_linked_LCS[len_LCS])
    LCS.reverse()
    assert len_LCS == len(LCS)
    return LCS


assert _calc_LCS__OlogNRlogN('', '') == list('')
assert _calc_LCS__OlogNRlogN('1', '2') == list('')
assert _calc_LCS__OlogNRlogN('1', '1') == list('1')
assert _calc_LCS__OlogNRlogN('1234567', '351246') == list('1246')
assert _calc_LCS__OlogNRlogN('1234567', '35146') == list('356')


assert calc_LCS__OlogNRlogN('1234567', '351246') == list('1246')
assert calc_LCS__OlogNRlogN('1234567', '35146') == list('356')
assert calc_LCS__OlogNRlogN('123456', '35146') == list('356')
assert calc_LCS__OlogNRlogN('3456', '35146') == list('356')

