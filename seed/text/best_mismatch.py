'''
<a><b></a> ==>> [1, 2, -1] ==>> [True, False, True] # False means mismatch
<a><a></a> ==>> [1, 1, -1] ==>> [False, True, True]

[---+++()+++N()-M--()---()...+++]
error:
    [-N,...]
    [..., +N]
    [..., +N, (matched), -M, ...]
        [..., +M, (...,+N, ()), -M, ...]
        [..., +N, ((), +M, ...), -N, ...]
        [..., (+N, (matched), -M), ...]

[(matched), +XX*, (matched), -M, ...]
---------init-----(  rng  )----------

if initA <= initB and initA_num_Trues >= initB_num_Trues:
then A wins

if init be the same and rngA <= rngB and rngA_num_Trues >= rngB_num_Trues:
then A wins
'''

__all__ = '''
    best_mismatch
    html_tags2iter_ints
    hashables2iter_ints
    UsedRngs
'''.split()



from sand import ImmutableSeq, count_while, iter_seq, \
     iter_find, seq_index_if, iter_find_if, concat, \
     calc_begin2max_end, calc_end2min_begin, \
     normalize_rngs, rngs_sub
from collections import Counter

from itertools import islice




def calc_end2nonneg_begin(ints):
    # all((<=0), ints[idx2nonneg_begin[i]:i])
    # idx2nonneg_begin[i] <= i
    return calc_end2min_begin(ints, lambda i: i>=0)

def calc_begin2nonpos_end(ints):
    return calc_begin2max_end(ints, lambda i: i<=0)


    
class _BestMismatch_Base:
    def std(self, rng):
        raise NotImplementedError
    def iter_follow_nonpos_indics(self, begin, end):
        raise NotImplementedError
    def __init__(self, ints):
        self.ints = ints

        # rng2numTrues_splitAt
        # d[(begin, end)] = (n, at) ==>> (begin, at) (at, end)
        self.rng2n_at = {}
    def do(self, rng):
        begin, end = rng = self.std(rng)
        
        if end - begin <= 1:
            return 0
        n_at = self.rng2n_at.get(rng, None)
        if n_at is not None:
            n, _ = n_at
            return n
        return self.__do(rng)
    
    def __do(self, rng):
        begin, end = rng
        this_func = self.do
        n_at_ls = [(this_func((begin+1, end)), begin+1)]
        for i in self.iter_follow_nonpos_indics(begin, end):
            n = (this_func((begin+1, i)) +
                 2 +
                 this_func((i+1, end)))
            n_at_ls.append((n, i+1)) # n(begin, i+1) = n(begin+1, i) + 2

        max_n = max(n_at_ls, key=lambda e: e[0])[0]
        i = seq_index_if(n_at_ls, lambda e:e[0] == max_n)
        assert n_at_ls[i][0] == max_n
        
        self.rng2n_at[(begin, end)] = n_at_ls[i]
        return max_n
    def main(self):
        L = len(self.ints)
        max_n = self.do((0, L))
        ls = [False] * L

        rngs = [(0, L)]
        while rngs:
            rng = rngs.pop()
            begin, end = rng = self.std(rng)
            n_at = self.rng2n_at.get(rng, None)
            if n_at is not None:
                n, at = n_at
                if at - begin != 1:
                    assert at - begin > 1 and self.ints[begin] == -self.ints[at-1]
                    assert n > 0 and n % 2 == 0

                    # pair
                    ls[begin] = True
                    ls[at-1] = True
                rngs += [(begin+1, at-1), (at, end)]
            else:
                assert end - begin < 2
            
        assert max_n == ls.count(True)
        # zero ==>> False
        assert all(i != 0 or not bl for bl, i in zip(ls, self.ints))

        for i in iter_find(self.ints, 0):
            ls[i] = True
        # zero ==>> True
        assert all(i != 0 or bl for bl, i in zip(ls, self.ints))
        return ls

class _BestMismatch_ver1(_BestMismatch_Base):
    def std(self, rng):
        begin, end = rng
        # skip negs
        begin += count_while(lambda i:i<=0,
                             iter_seq(self.ints)[begin:end])
        # skip poss
        end -= count_while(lambda i:i>=0,
                           iter_seq(self.ints, reversed=True)[begin:end])
        return begin, end


    def iter_follow_nonpos_indics(self, begin, end):
        #assert self.ints[begin] > 0
        return iter_find(self.ints, -abs(self.ints[begin]), begin+1, end)


    
class _BestMismatch_ver2(_BestMismatch_Base):
    def __init__(self, ints):
        super().__init__(ints)
        L = len(ints)
        MAX = max(concat([ints, [0]]))
        MIN = min(concat([ints, [0]]))
        assert MIN <= 0 <= MAX
        if L < max(MAX, -MIN):
            raise ValueError('L < max(MAX, -MIN)')
        mapL = -MIN + 1 + MAX
        self.begin2nonpos_end = calc_begin2nonpos_end(ints)
        self.end2nonneg_begin = calc_end2nonneg_begin(ints)
        self.MIN, self.MAX = MIN, MAX
        self.idx2next_nonpos_idx = self.calc_idx2next_nonpos_idx()
        

    def iter_follow_nonpos_indics(self, idx, end):
        L = len(self.ints)
        if end > L:
            end = L
        if idx >= end:
            return
        
        idx = self.idx2next_nonpos_idx[idx]
        while idx < end:
            yield idx
            idx = self.idx2next_nonpos_idx[idx]
            
            
    def calc_idx2next_nonpos_idx(self):
        '''next_i = idx2next_nonpos_idx[i]
all (/= -abs seq[i]) seq[i:next_i]
next_i == len(seq) || seq[next_i] == -abs seq[i]
'''
        ints = self.ints
        L = len(ints)
        MIN = self.MIN
        assert MIN <= 0
        
        ls = []
        nonpos2next_idx = [L] * (-MIN + 1)
        for x in reversed(ints):
            ls.append(nonpos2next_idx[-abs(x)])
            if x <= 0:
                nonpos2next_idx[x] = L - len(ls)
        ls.reverse()
        
        return ls
        
    def std(self, rng):
        begin, end = rng
        begin = self.begin2nonpos_end[begin]
        if begin >= end:
            return end, end
        end = self.end2nonneg_begin[end]
        if begin >= end:
            return begin, begin
        return begin, end
    
_BestMismatch = _BestMismatch_ver2

def hashables2iter_ints(iterable, is_zero, is_opener, to_opener, to_closer):
    d = {}
    def to_pos_neg(x):
        return (x, to_closer(x)) if is_opener(x) else (to_opener(x), x)
    def x2idx(x):
        if is_zero(x):
            return 0
        if x not in d:
            pos, neg = to_pos_neg(x)
            n = len(d)//2 + 1
            d[pos] = n
            d[neg] = -n
        return d[x]

    return map(x2idx, iterable)

def html_tags2iter_ints(tags):
    is_zero = lambda tag: tag[-2] == '/'
    is_opener = lambda tag: tag[1] != '/'
    to_opener = lambda tag: '<' + tag[2:]
    to_closer = lambda tag: '</' + tag[1:]
    return hashables2iter_ints(
        tags, is_zero=is_zero, is_opener=is_opener,
        to_opener=to_opener, to_closer=to_closer)

assert list(html_tags2iter_ints('<a> <b> </a>'.split())) == [1,2,-1]
def best_mismatch__ver1(ints):
    #assert all(ints)

    ls = _BestMismatch(ints).main()
    return ls

_test_data = [
    ([], []),
    ([1], [False]),
    ([-1], [False]),
    ([-1, 1], [False, False]),
    ([1, -1], [True, True]),
    ([1, 1, -1], [False, True, True]),
    ([1, 2, -1], [True, False, True]),
    ]
assert all(best_mismatch__ver1(i) == o for i,o in _test_data)


class UsedRngs:
    def __init__(self, rngs=()):
        self.rngs = normalize_rngs(rngs)
    def prev_unused(self):
        rngs = self.rngs
        if not rngs:
            return None
        begin, _ = rngs[-1]
        return begin - 1
    def use(self, begin, end=None):
        if end == None:
            end = begin + 1
        if end <= begin:
            return
        
        rng = (begin, end)
        rngs = self.rngs
        while rngs:
            last_begin, last_end = rngs[-1]
            if begin > last_end:
                rngs.append(rng)
            elif begin == last_end:
                # merge to last
                rngs[-1] = last_begin, end
            elif end == last_begin:
                # merge to rng
                rngs.pop()
                begin, end = rng = begin, last_end
                continue
            break
        else:
            rngs.append(rng)
    def __bool__(self):
        return bool(self.rngs)
    

def find_out_True_indices(ints):
    used_rngs = UsedRngs()
    for idx, x in enumerate(ints):
        if x == 0:
            used_rngs.use(idx)
        elif x < 0:
            if used_rngs:
                pre_idx = used_rngs.prev_unused()
                if pre_idx >= 0:
                    y = ints[pre_idx]
                    if y == -x:
                        used_rngs.use(idx)
                        used_rngs.use(pre_idx)
    return used_rngs.rngs

        
        
    
def best_mismatch__prepare(ints):
    good_rngs = find_out_True_indices(ints)
    L = len(ints)
    gap_rngs, empty = rngs_sub([(0,L)], good_rngs)
    assert not empty

    new_ints = list(concat(ints[begin:end] for begin, end in gap_rngs))

    ls = [None] * L
    for begin, end in good_rngs:
        ls[begin:end] = repeat(True, end-begin)
    return new_ints, gap_rngs, ls
def best_mismatch__ver2(ints):
    new_ints, gap_rngs, bs = best_mismatch__prepare(ints)
    new_bs = best_mismatch__ver1(new_ints)
    it = iter(new_bs)
    for begin, end in gap_rngs:
        bs[begin:end] = islice(it, end-begin)
    for _ in it:
        raise logic-error
    assert bs.count(None) == 0

    return bs

assert all(best_mismatch__ver2(i) == o for i,o in _test_data)
best_mismatch = best_mismatch__ver2


