
'''
[String_Suffix_Tree_2003]Simple_Linear_Work_Suffix_Array_Construction

'''

from nn_ns.sort.bucket_sort import bucket_sort, radix_sort, group
from nn_ns.lists.automap import inv_automap
from .range_minimum_query import range_minimum_query, minidx_of
import itertools


def to_triples(ls):
    assert len(ls) > 2
    assert ls[-2:] == [0]*2
    
    triples = [ls[i:i+3] for i in range(len(ls)-2)]
    assert len(triples) == len(ls) - 2
    return triples


def length_of_longest_common_prefix_of_two_array(array1, array2):
    L = 0
    for a, b in zip(array1, array2):
        if a != b:
            break
        L += 1
    return L
len_lcp = length_of_longest_common_prefix_of_two_array


def test_suffix_array_of_ints__more():
    base = 3
    __c = 0
    for n in range(9):
        for ints in itertools.product(range(1, 1+base), repeat=n):
            M = max((0,)+ints)
            base_set = set(range(1, M+1))
            if set(ints) != base_set:
                continue
            
            assert n == len(ints)
            _1_test_suffix_array_of_ints__more(ints)
            
            __c += 1
            if __c % 1000 == 0:
                print('1 test_suffix_array_of_ints__more: +1000')
    assert __c
    print('1 test_suffix_array_of_ints__more: -------------------> 2')
    

    num_rounds = 100
    __c = 0
    __step = (1000+num_rounds-1)//num_rounds*num_rounds
    __s = '2 test_suffix_array_of_ints__more: +' + str(__step)
    for LEN in range(15):
        for MAX in range(1, LEN+1):
            _2_test_suffix_array_of_ints__more(num_rounds, MAX, LEN)
            
            __c += num_rounds
            if __c % __step == 0:
                print(__s)
    print('2 test_suffix_array_of_ints__more: -------------------> 2.2')
                
    for LEN in range(70):
        for MAX in range(1, 5+1):
            _2_test_suffix_array_of_ints__more(num_rounds, MAX, LEN)
            
            __c += num_rounds
            if __c % __step == 0:
                print(__s)
        
def _2_test_suffix_array_of_ints__more(num_rounds, MAX, LEN):
    from random import shuffle, randint
    
    assert all(x >= 0 for x in [num_rounds, MAX, LEN])
    basic = list(range(1, MAX+1))

    __c = 0
    for _ in range(num_rounds):
        ints = basic + [randint(1, MAX+1) for _ in range(LEN-MAX)]
        shuffle(ints)
        _1_test_suffix_array_of_ints__more(ints)

        
def _1_test_suffix_array_of_ints__more(ints):
    n = len(ints)
    pos2ord, ord2pos, LCP, LCP_IDX_RMQ = suffix_array_of_ints__more(ints)
    assert n == len(ints) == len(LCP)
    assert n + 1 == len(pos2ord) == len(ord2pos)
    
    for ord, pos in enumerate(ord2pos):
        assert pos2ord[pos] == ord

    for ord1, ord2, lcp in zip(ord2pos, ord2pos[1:], LCP):
        suffix1, suffix2 = ints[ord1:], ints[ord2:]
        assert lcp == len_lcp(suffix1, suffix2)
        assert suffix1 < suffix2

    for i in range(n):
        for j in range(i+1, n+1):
            lcp_idx = LCP_IDX_RMQ(i,j)
            assert minidx_of(LCP, i,j) == lcp_idx
            
                

class SuffixTreeOfInts:
    def __init__(self, ints):
        '''node is a ord_range

node = ord_range ==>> suffix[ord_begin: ord_end]
begin == end     - empty tree # not a node!!!
begin+1 == end   - leaf node
'''
        self.n = len(ints)
        self.pos2ord, self.ord2pos, self.LCP, self.LCP_IDX_RMQ = \
                      suffix_array_of_ints__more(ints)

    def pos_range2ord_range(self, pos_range):
        raise impossible
        '''
common_prefix = array[pos_begin:pos_end];
assert suffix[ord].startswith(common_prefix) for ord in [ord_begin:ord_end)'''
        pos_begin, pos_end = pos_range
        assert pos_begin <= pos_end
        
        if pos_begin == pos_end:
            return self.root()

        ord = self.pos2ord[pos_begin]
    def is_node(self, ord_range):
        begin, end = ord_range
        return begin < end
    def is_leaf(self, ord_range):
        begin, end = ord_range
        return begin == end-1
        
        
    def root(self):
        return (0, len(self.ord2pos))
    def children(self, ord_range):
        assert self.is_node(ord_range)
        
        begin, end = ord_range
        if end - begin == 1:
            return iter(())

        min_lcp_idx = self.LCP_IDX_RMQ(begin, end-1)
        lcp = self.LCP[min_lcp_idx]
        while end - begin > 1:
            min_lcp_idx = self.LCP_IDX_RMQ(begin, end-1)
            if not lcp == self.LCP[min_lcp_idx]:
                break
            
            split_at = min_lcp_idx + 1
            yield begin, split_at
            begin = split_at

        assert begin < end
        yield (begin, end)

        

    def len_suffix(self, ord):
        return self.n - self.ord2pos[ord]
    def ord_range2len_lcp(self, ord_range):
        assert self.is_node(ord_range)

        ord_begin, ord_end = ord_range
        if self.is_leaf(ord_range):
            L = self.len_suffix(ord_begin)
        else:
            L = self.LCP[self.LCP_IDX_RMQ(ord_begin, ord_end-1)]
        return L
        
    def ord_range2prefix_pos_range(self, ord_range):
        '''common_prefix(ord_range) == array[*pos_range]'''

        L = self.ord_range2len_lcp(ord_range)
        pos_begin = self.ord2pos[ord_begin]
        pos_end = pos_begin + L
        return pos_begin, pos_end
    
        
        
                
            
        
        
def suffix_array_of_ints(ints):
    pos2ord, ord2pos, LCP, LCP_IDX_RMQ = suffix_array_of_ints__more(ints)
    return ord2pos

def suffix_array_of_ints__more(ints):
    '''set(ints) == set(range(1, max([0]+ints)+1))


len(ints) == n; len(suffix_array) == n+1; len(LCP) == n;

0 <= ord <= n
suffix_array[ord] == array index == ord2array_idx == ord2suffix_begin;
suffix[ord] = ints[suffix_array[ord]:]

LCP[ord] == lcp(suffix[ord], suffix[ord+1])
LCP_IDX_RMQ(ord_i,ord_j) == arg_{ord_k} min LCP[ord_k] for ord_k in [ord_i..ord_j-1] for 0<=ord_i<ord_j<=n
             == LCP.index(lcp(suffix[ord_k] for ord_k in [ord_i..ord_j]), ord_i, ord_j+1)
LCP[LCP_IDX_RMQ(ord_i,ord_j)] == lcp(suffix[ord_k] for ord_k in [ord_i..ord_j])

lcp : length of longest common prefix
rmq : range minimum query

'''
    ints = list(ints)
    #assert ints

    L = len(ints)
    if L:
        M = max(ints)
        assert set(ints) == set(range(1, M+1))

    
    pos2ord, ord2pos, LCP, LCP_IDX_RMQ = _pos2ord_N_ord2pos(ints)
    assert set(pos2ord) == set(range(L+1)) == set(ord2pos)
    return pos2ord, ord2pos, LCP, LCP_IDX_RMQ
    #assert set(pos2ord) == set(range(L)) == set(ord2pos)
    
    #return [L] + ord2pos

def _pos2ord_N_ord2pos(ints):
    #print('ints=', ints)
    pos2ord, ord2pos, LCP = __pos2ord_N_ord2pos(ints)
    assert len(LCP)+1 == len(pos2ord) == len(ord2pos)
    #print('\tints={}, pos2ord={}, ord2pos={}'.format(ints, pos2ord, ord2pos))
##    for pos, next in zip(ord2pos, ord2pos[1:]):
##        if not ints[pos:] < ints[next:]:
##            print('ints', ints)
##            print('pos2ord', pos2ord)
##            print('ord2pos', ord2pos)
##        assert ints[pos:] < ints[next:]
    LCP_IDX_RMQ = range_minimum_query(LCP)
    return pos2ord, ord2pos, LCP, LCP_IDX_RMQ


def __pos2ord_N_ord2pos(ints):
    if not ints:
        return [0], [0], []

    M = max(ints)
    if len(ints) == M:
        # done
        assert set(ints) == set(range(1, M+1))
        #pos2ord = [i-1 for i in ints]
        pos2ord = list(ints)
        pos2ord.append(0)
        ord2pos = inv_automap(pos2ord)
        LCP = [0]*len(ints)
        return pos2ord, ord2pos, LCP


    # non trival case
    
    assert len(ints) > M
    L = len(ints) + 1
    ints += [0, 0, 0] # split triple12s; make the sorted result useful
    triples = to_triples(ints)
    assert len(triples) == L
    
    triple1s = triples[1::3]
    triple2s = triples[2::3]
    triple12s = triple1s + triple2s
    # error: triple12s = [triples[i] for i in range(len(triples)) if i % 3]
    
    triple12_pos_to_ord = triples2pos2ord(triple12s, M)
    sub_ints = [ord+1 for ord in triple12_pos_to_ord]
    assert len(sub_ints) == L//3*2 + (L%3==2)
    
    suffix12_pos_to_ord, suffix12_ord_to_pos, LCP12, LCP12_IDX_RMQ = \
                         _pos2ord_N_ord2pos(sub_ints)
    #print(len(triples), len(sub_ints), len(suffix12_pos_to_ord))
    assert len(suffix12_pos_to_ord) == L//3*2 + (L%3 == 2) + 1
    suffix12_pos_to_ord += [-2, -2]
    # cmp pos0 pos1:
    #    (ints[abspos0], ord[pos12(abspos0+1)]) vs (ints[abspos1], ord[pos12(abspos1+1)])
    # cmp pos0 pos2
    #    (ints[abspos0:abspos0+2], ord[pos12(abspos0+2))
    #    vs (ints[abspos2:abspos2+2], ord[pos12(abspos2+2))

    
    def pos12_to_abspos(pos12):
        r = 1
        if pos12 >= len(triple1s):
            pos12 -= len(triple1s)
            r = 2
            
        return pos12*3 + r
    def abspos_to_pos12(abspos):
        assert abspos%3
        return abspos//3 + (abspos%3 - 1) * len(triple1s)

    keys = __pos2ord_N_ord2pos__calc_keys(ints, L, suffix12_pos_to_ord, abspos_to_pos12)


##    for pos12, next12 in zip(suffix12_ord_to_pos, suffix12_ord_to_pos[1:]):
##        assert sub_ints[pos12:] < sub_ints[next12:]
##        if not ints[pos12_to_abspos(pos12):] < ints[pos12_to_abspos(next12):]:
##            print('--------------------------')
##            print('ints', ints)
##            print('triple12s', triple12s)
##            print('sorted triple12s', [triple12s[pos] for pos in suffix12_ord_to_pos])
##            abspos12s = [pos12_to_abspos(pos) for pos in suffix12_ord_to_pos]
##            print('sorted abspos12s', abspos12s)
##            print('sorted suffixes', [ints[pos:] for pos in abspos12s])
##        assert ints[pos12_to_abspos(pos12):] < ints[pos12_to_abspos(next12):]


    N = max(suffix12_pos_to_ord)
    assert N == len(suffix12_pos_to_ord)-1 -2 == len(suffix12_ord_to_pos)-1
    suffix0_ord2abspos = radix_sort(list(range(0, L, 3)),
                                    lambda abspos0: keys[abspos0][0],
                                    [M+1, N+1])

##    for pos, next in zip(suffix0_ord2abspos, suffix0_ord2abspos[1:]):
##        if not ints[pos:] < ints[next:]:
##            print('suffix0_ord2abspos', suffix0_ord2abspos)
##        assert ints[pos:] < ints[next:]

    pos2ord, ord2pos = __pos2ord_N_ord2pos__merge(L, keys,
                               suffix0_ord2abspos,
                               suffix12_ord_to_pos,
                               pos12_to_abspos)




    # calc LCP
    LCP = __pos2ord_N_ord2pos__LCP(L, ints, ord2pos,
                               suffix12_pos_to_ord,
                               LCP12, LCP12_IDX_RMQ,
                               abspos_to_pos12)
    
    return pos2ord, ord2pos, LCP

def __pos2ord_N_ord2pos__LCP(L, ints, ord2pos,
                               suffix12_pos_to_ord,
                               LCP12, LCP12_IDX_RMQ,
                               abspos_to_pos12):
    n = L-1
    def calc_lcp(pos_a, pos_b):
        assert pos_a != pos_b
        if pos_a > pos_b:
            pos_a, pos_b = pos_b, pos_a

        assert 0 <= pos_a < pos_b <= n
        if pos_b == n:
            return 0
        assert pos_b < n
        
        if not ints[pos_a] == ints[pos_b]:
            return 0
        
        if pos_b+1 == n:
            return 1
        
        
        ra = pos_a % 3
        rb = pos_b % 3
        if ra != 0 and rb != 0:
            pos12_a = abspos_to_pos12(pos_a)
            pos12_b = abspos_to_pos12(pos_b)

            ord12_a = suffix12_pos_to_ord[pos12_a]
            ord12_b = suffix12_pos_to_ord[pos12_b]
            if ord12_a > ord12_b:
                ord12_a, ord12_b = ord12_b, ord12_a
            assert ord12_a < ord12_b
            lcp12 = LCP12[LCP12_IDX_RMQ(ord12_a, ord12_b)]
            common = 3*lcp12

            
            pos_a += common
            pos_b += common
            assert pos_a < pos_b <= n
            assert n+3 == len(ints)
            assert pos_b+2 < n+3 == len(ints)
            lcp_tail = 0
            while ints[pos_a+lcp_tail] == ints[pos_b+lcp_tail]:
                lcp_tail += 1
                assert lcp_tail < 3
            return common + lcp_tail

        return 1 + calc_lcp(pos_a+1, pos_b+1)

            
    LCP = []
    for pos, next in zip(ord2pos, ord2pos[1:]):
        LCP.append(calc_lcp(pos, next))

            
    return LCP


def __pos2ord_N_ord2pos__merge(L, keys,
                               suffix0_ord2abspos,
                               suffix12_ord_to_pos,
                               pos12_to_abspos):

    pos2ord = [None] * L
    ord2pos = []


    def add_abspos_to_result(abspos):
        pos2ord[abspos] = len(ord2pos)
        ord2pos.append(abspos)

        
    # merge suffix0_ord2abspos and suffix12_ord_to_pos
    ord12 = 1
    for abspos0 in suffix0_ord2abspos:
        key0 = keys[abspos0]
        while ord12 < len(suffix12_ord_to_pos):
            pos12 = suffix12_ord_to_pos[ord12]
            abspos12 = pos12_to_abspos(pos12)
            key12 = keys[abspos12]
            key_idx = abspos12 % 3 == 2
            if key0[key_idx] < key12[key_idx]:
                break
            
            ord12 += 1
            add_abspos_to_result(abspos12)
        add_abspos_to_result(abspos0)
        

    for pos12 in suffix12_ord_to_pos[ord12:]:
        abspos = pos12_to_abspos(pos12)
        add_abspos_to_result(abspos)


    assert len(ord2pos) == len(pos2ord)
    assert all(ord != None for ord in pos2ord)
    
    
    return pos2ord, ord2pos


def triples2pos2ord(triples, M):
    triple_pos_ls = [(triple, i) for i, triple in enumerate(triples)]

    triple_pos_ls = radix_sort(triple_pos_ls, lambda e:e[0], [M+1]*3)
    blocks = group(triple_pos_ls, lambda e: e[0])

    ord2posls = [[triple_pos[-1] for triple_pos in triple_pos_ls[i:j]]
                 for i, j in blocks]
    pos2ord = [None] * len(triples)
    for ord, posls in enumerate(ord2posls):
        for pos in posls:
            pos2ord[pos] = ord

##    for posls in ord2posls:
##        key = triples[posls[0]]
##        for pos in posls:
##            assert triples[pos] == key
##
##    for pos, ord in enumerate(pos2ord):
##        key = triples[ord2posls[ord][0]]
##        assert triples[pos] == key
##
##    for ord, posls in enumerate(ord2posls[:-1]):
##        key = triples[posls[0]]
##        next = triples[ord2posls[ord+1][0]]
##        assert key < next
    return pos2ord
    

def __pos2ord_N_ord2pos__calc_keys(ints, L, suffix12_pos_to_ord, abspos_to_pos12):
    keys = []
    for abspos in range(L):
        r = abspos%3
        i0 = ints[abspos:abspos+1]
        i01 = ints[abspos:abspos+2]
        key1, key2 = None, None
        if r != 2:
            key1 = i0 + [suffix12_pos_to_ord[abspos_to_pos12(abspos+1)]]
        if r != 1:
            key2 = i01 + [suffix12_pos_to_ord[abspos_to_pos12(abspos+2)]]
        keys.append([key1, key2])
    return keys

def suffix_array_of_str(s, BIT_LEN=8):
    assert 8 % BIT_LEN == 0
    
    WORDSIZE = 4
    bs = s.encode('utf_32_be')
    assert len(bs) % WORDSIZE == 0
    ALPHABET_SIZE = 2**BIT_LEN
    MASK = ALPHABET_SIZE - 1
    
    ints = []
    _L = 8 // BIT_LEN
    for b in bs:
        _ints = []
        for _ in range(_L):
            _ints.append(b & MASK)
            b >>= BIT_LEN
        ints.extend(reversed(_ints))

    L = WORDSIZE * 8 // BIT_LEN
    assert len(ints) == len(s) * L
    
    b2exists = [0] * ALPHABET_SIZE
    for b in ints:
        b2exists[b] = 1
    #b2ord[0] = 1
    b2ord_plus1 = list(itertools.accumulate(b2exists))
    
    ints = [b2ord_plus1[b] for b in ints] # transform ints into [1..MAX]
    #print(ints)
    sa = suffix_array_of_ints(ints)
    return [pos//L for pos in sa if pos % L == 0]

def suffix_array_of_str(s):
    ints = [ord(c) for c in s]
    all_ints = sorted(set(ints))
    int2ord = {int: idx+1 for idx, int in enumerate(all_ints)}

    ints = [int2ord[b] for b in ints]
    #print(ints)
    sa = suffix_array_of_ints(ints)
    return sa

def longest_common_prefix(array, suffix_array):
    ''' >= O(n^2)

if array == [1]*n:
    T(n) = n/2 + 2*T(n/2) = n/2 * log(n)
if array == [1..n] + [1..n]
    T(2n) = sum (n-i) = n(n+1)/2
'''
    L = len(array)
    def suffix_len(i):
        return L - suffix_array[i]
    
    lcp = [None] * len(suffix_array)
    lcp[0] = suffix_len(0)
    assert lcp[0] == 0
    assert len(suffix_array) == L + 1
    assert set(suffix_array) == set(range(L+1))

    def _calc_lcp(array_idx_a, array_idx_b):
        if array_idx_a == array_idx_b:
            return L - array_idx_a

        a = array_idx_a - 1
        for a, b in zip(range(array_idx_a, L),
                        range(array_idx_b, L)):
            if array[a] != array[b]:
                break
        else:
            return a+1 - array_idx_a

        return a - array_idx_a
            
        
    def calc_lcp_from_sa_idc(sa_idx_a, sa_idx_b, least):
        array_idx_a = suffix_array[sa_idx_a] + least
        array_idx_b = suffix_array[sa_idx_b] + least
        return _calc_lcp(array_idx_a, array_idx_b) + least
        
        
        
    def _lcp(begin, end, least):
        if end - begin < 2:
            return

        least = calc_lcp_from_sa_idc(begin, end-1, least)
        if end - begin == 2:
            assert lcp[end-1] is None
            lcp[end-1] = least
            return
        
        middle = (begin+end)//2
        assert begin < middle < middle+1 < end
        _lcp(begin, middle+1, least)
        _lcp(middle, end, least)
    _lcp(0, L+1, 0)
    assert all(x is not None for x in lcp)
    return lcp

        

    
    _lcp(array, list(range(len(array)+1)), suffix_array, LCP2RMQ)

def _lcp(array, mididx2array_loc, suffix_ord2mididx, suffix_mididx2ord, LCP_RMQ_T):
    '''suffix = array[mididx2array_loc[suffix_ord2mididx[i]]:]

lcp_rmq = LCP_RMQ_T(lcp)
len[suffix[i]] = lcp_rmq(i, i+1)
len_lcp = lcp_rmq(i,j) = rmq(i, j) for 0 <= i < i+ 1 < j <= len(lcp) == len(ptrs)
lcp[0] == len(array[ptrs[sorted_suffix_ptr_idc[0]]:])
lcp[i] == len_lcp(i-1, i)

'''
    L = len(mididx2array_loc)
    assert len(array)+1 >= L > 0 # min case : [end]
    assert L == len(suffix_ord2mididx) == len(suffix_mididx2ord)
    
    def get_ptr(i):
        return mididx2array_loc[suffix_ord2mididx[i]]
    def get_value(i):
        return array[get_ptr(i)]

    lcp_0 = len(array) - get_ptr(0)
    if L == 1:
        return [lcp_0]
    
    # reduce
    reduced_middle_indices = [idx//3*2 + idx%3-1 for idx in suffix_ord2mididx if idx % 3]
    reduced_locs = [mididx2array_loc[i] for i in range(L) if i % 3]
    lcp12 = _lcp(array, reduced_locs, reduced_middle_indices, LCP_RMQ_T)
    assert len(lcp12) == len(reduced_locs) == len(reduced_middle_indices)

    lcp12_rmq = LCP_RMQ_T(lcp12)
    lcp = [None] * L
    lcp[0] = lcp_0
    for i in range(1, L):
        if get_value(i-1) != get_value(i):
            lcp[i] = 0
            continue

        least = 1
        #ptr_idd = get_ptr(i-1)
        #ptr_i = get_ptr(i)
        
        r = (i-1) % 3
        if r == 0:error ; xxxxxxxxxxxxxx
            
    
         

    
    

def test_longest_common_prefix():
    data = [
        '',
        '1',
        '11',
        '13',
        '112',
        ] + [bin(i) for i in range(3000)]

    def calc_lcp(s1, s2):
        i = 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                break
            i += 1
        return i
    
    for s in data:
        sa = suffix_array_of_str(s)
        lcp = longest_common_prefix(s, sa)
        assert len(lcp) == len(s) + 1 == len(sa)
        for i in range(1, len(lcp)):
            L = calc_lcp(s[sa[i-1]:], s[sa[i]:])
            assert lcp[i] == L

    
    
def test_suffix_array_of_str():
    data = [
        '',
        '1',
        '11',
        '13',
        '112',
        ] + [bin(i) for i in range(3000)]


    for s in data:
        sa = suffix_array_of_str(s)
        assert set(sa) == set(range(len(s)+1))
        for i in range(len(s)):
            if not s[sa[i]:] < s[sa[i+1]:]:
                print(('{!r} '*4).format(s, sa, s[sa[i]:], s[sa[i+1]:]))
                assert s[sa[i]:] < s[sa[i+1]:]



test_suffix_array_of_ints__more()
test_suffix_array_of_str()
test_longest_common_prefix()




















