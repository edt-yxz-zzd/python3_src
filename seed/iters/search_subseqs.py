
r'''
not fast, see below size_XXX in mk4search_subseqs
    occur L*INPUT_SIZE
    ???discard this module???
    required by one alternative impl version of python3_src/nn_ns/filedir/file_cmp.py


seed.iters.search_subseqs
py -m seed.iters.search_subseqs
from seed.iters.search_subseqs import mk4search_subseqs


see:
    seed.iters.search_subseqs
        #search subseqs
        #using ".*"++regex-OR<*subseqs>
    seed.iters.find
        #search subseq
        #using failure_func
    nn_ns.bin.stream_search
        #search subseq
        #using polynomial hash
    seed.seq_tools.seq_index_if
        #search value
        #using predicator
    seed.text.StepDecoder
        #def&search "line"
        #using step_builder,step_predicator

#'''


__all__ = '''
    mk4search_subseqs
    '''.split()

#from seed.types.to_container import to_tuple
#from seed.tiny import MapView
from seed.types.FrozenDict import FrozenDict
from seed.tiny import at
from seed.algo.is_sorted import is_strict_sorted
from seed.iters.find import mk_last_succ_pos2restart_pos__from_seq

#from collections.abc import Sequence
from collections import defaultdict
import operator
:

if __name__ == "__main__":
    if 1:
        d = {}
        v = d.setdefault(1,2)
        assert v == 2

def mk4search_subseqs(subseq_seq, *, _use_failure_func=True):
    r'''
    ".*"++regex-OR<*subseq_seq>

    input:
        subseq_seq :: [[symbol]]
            search any one of subseqs

    output:
        #(i0, jump_table, i2cached_len, i2accepted_js)
        #=(istate0, jump_table, istate2cached_len, istate2sorted_accepted_isubseqs)
        #

        i0=istate0
            :: istate=uint
            start istate

        jump_table=istate2symbol2next_istate
            :: {curr_i:{symbol:next_i}}
            FSM table<istate, symbol>

        i2cached_len = istate2cached_len
            :: [uint]@istate
            how many symbol should be cached to restore the matched subseq?
            use at:
                * search on iterable
                    use deque to cache [symbol] of size cached_len
                * search on stream #file
                    use deque to cache [stream_pos] of size cached_len

        i2accepted_js=istate2sorted_accepted_isubseqs
            :: [sorted[isubseq=uint]]@istate
            which subseqs are matched?

    ### external
    i - istate; idx4st, i.e. FSM state repred as uint
    j - isubseq; idx4subseq, i.e. subseq repred as uint
    ### internal
    k - idx_in_subseq given j/isubseq
        k <- [0..j2len[j]]
        usage: suffix = symbols = subseq_seq[j][k:]

    st
        if _use_failure_func:
            # failure_func
            st :: [k]@isubseq
        else:
            # plain
            st :: [sorted[k]]@isubseq

    i2st :: [st]@istate
    j2len :: [uint]@isubseq

    ###
    assert 1 <= len(i2st) <= sum(j2len)
        # cached_len = max(map(max, st), default=0)
        # each cached_len can occur only once per j
        #   since other prefix is this suffix:
        #       let j s.t. cached_len==max(st[j])
        #       subseq_seq[j'][:max(st[j'])] other_prefix == this_prefix_suffix == subseq_seq[j][cached_len-max(st[j']):cached_len]


    num_sts
        1 <= num_sts == len(i2st) <= sum(j2len) == INPUT_SIZE
    size_i2st:
        if not _use_failure_func:
            size_i2st = sum(map(len, st) for st in i2st)
                ???
                if not _use_failure_func && only one subseq && symbols in the subseq are the same:
                    O(INPUT_SIZE^2)
                    ==>> use failure_func instead
        else:
            size_i2st = sum(len(st) for st in i2st) = L*num_sts <= L*INPUT_SIZE
    if not _use_failure_func:
        size_j2last_succ_pos2restart_pos = O(INPUT_SIZE)
        size_j2k2next_val2k1 = sum(map(map . len, j2k2next_val2k1))
            ???
            INPUT_SIZE*???
    size_jump_table = sum(map(len, jump_table))
        ???
    #
    #'''
    L = len(subseq_seq)
    j2subseq = subseq_seq
    j2len = lens = tuple(map(len, j2subseq))
    if _use_failure_func:
        j2last_succ_pos2restart_pos = tuple(map(mk_last_succ_pos2restart_pos__from_seq, j2subseq))
        def mk_next_val2k1(k2next_val2k1, subseq, last_succ_pos2restart_pos, k):
            assert k == len(k2next_val2k1)
            k2next_val2k1
                #for recur ref
            assert 0 <= k <= len(subseq)
            if k == 0:
                next_val2k1 = {}
                pass
            else:
                assert k > 0
                last_succ_pos = k-1
                restart_pos = last_succ_pos2restart_pos[last_succ_pos]
                len_last_succ_bifix = restart_pos
                k_ = len_last_succ_bifix
                next_val2k1_ = k2next_val2k1[k_]
                    #recur ref
                if k == len(subseq):
                    next_val2k1 = dict(next_val2k1_)
                    pass
                else:
                    assert 0 < k < len(subseq)
                    next_val = subseq[k]
                    next_val2k1 = dict(next_val2k1_)
                    next_val2k1[next_val] = k+1
                        #overwrite if exist
                next_val
            next_val
            ##
            if subseq:
                next_val2k1.setdefault(subseq[0], 1)
                    # <<== ".*"
            return next_val2k1
        def mk_k2next_val2k1(subseq, last_succ_pos2restart_pos):
            k2next_val2k1 = []
            for k in range(len(subseq)+1):
                next_val2k1 = mk_next_val2k1(k2next_val2k1, subseq, last_succ_pos2restart_pos, k)
                k2next_val2k1.append(next_val2k1)
            assert len(k2next_val2k1) == len(subseq)+1
            return k2next_val2k1
        def mk_j2k2next_val2k1(j2subseq, j2last_succ_pos2restart_pos):
            j2k2next_val2k1 = tuple(map(mk_k2next_val2k1, j2subseq, j2last_succ_pos2restart_pos))
            return j2k2next_val2k1
        j2k2next_val2k1 = mk_j2k2next_val2k1(j2subseq, j2last_succ_pos2restart_pos)

    st2i = st2st_idx = {}
    i2st = st_ls = []
    def put_st(st):
        assert len(st2st_idx) == len(st_ls)
        n = len(st2st_idx)
        i = st2st_idx.setdefault(st, n)
        if i == n:
            st_ls.append(st)
        assert len(st2st_idx) == len(st_ls)
        return i
    def handle_per_subseq(next_val2j_k1_pairs:'OUT', st, j):
        # j <- [0..L-1]
        # k <- idc==st[j], k <- [0..j2len[j]]
        # j2len[j] = len(subseq)
        # subseq is j2subseq[j]
        subseq = j2subseq[j]
        if _use_failure_func:
            last_succ_pos2restart_pos = j2last_succ_pos2restart_pos[j]
            k = st[j]
                #succ end_pos
            next_val2k1 = j2k2next_val2k1[j][k]
                # need not sorted by k1
                # since only k1 per (j, next_val)
            for next_val, k1 in next_val2k1.items():
                next_val2j_k1_pairs[next_val].append((j, k1))

        else:
            idc = st[j]
            for k in idc:
                if k < j2len[j]:
                    next_val = subseq[k]
                    next_val2j_k1_pairs[next_val].append((j, k+1))
        ##

    def check_st(st):
        if _use_failure_func:
            assert all(map(operator.__le__, st, j2len))
        else:
            assert all(map(is_strict_sorted, st))
            assert all(map(len, st))
            assert all(map(operator.__le__, map(at[-1], st), j2len))
    i2val2next_i = jump_table = defaultdict(dict)
    def mk_st(j_k1_pairs):
        if _use_failure_func:
            st = [None]*L
            for j, k1 in j_k1_pairs:
                assert st[j] is None
                st[j] = k1
            st = tuple(st)
        else:
            st = [[0] for _ in range(L)]
                # <<== ".*"
            for j, k1 in j_k1_pairs:
                st[j].append(k1)
            st = tuple(map(tuple, st))
        check_st(st)
        return st
    def put_jump(curr_i, next_val, next_i):
        i2val2next_i[curr_i][next_val] = next_i


    st0 = ((0,),)*L if not _use_failure_func else (0,)*L
    check_st(st0)
    put_st(st0)
    num_handled_sts = 0
    while num_handled_sts != len(i2st):
        curr_i = num_handled_sts
        curr_st = i2st[curr_i]
        num_handled_sts += 1
        #
        next_val2j_k1_pairs = defaultdict(list)
        for j in range(L):
            handle_per_subseq(next_val2j_k1_pairs, curr_st, j)
        #
        for next_val, j_k1_pairs in next_val2j_k1_pairs.items():
            next_st = mk_st(j_k1_pairs)
            next_i = put_st(next_st)
            put_jump(curr_i, next_val, next_i)

    i0 = st2i[st0]
    assert i0 == 0

    #cached len?
    #final/accepted st?
    def mk_cached_len(st):
        cached_len = max(map(max, st), default=0)
        return cached_len
    def mk_i2cached_len(i2st):
        i2cached_len = tuple(mk_cached_len(st) for st in i2st)
        return i2cached_len

    def mk_accepted_js(j2len, st):
        #sorted
        accepted_js = tuple(j for j in range(L) if j2len[j] in st[j])
        assert is_strict_sorted(accepted_js)
        return accepted_js
    def mk_i2accepted_js(j2len, i2st):
        i2accepted_js = jss = tuple(mk_accepted_js(j2len, st) for st in i2st)
        return i2accepted_js

    i2cached_len = mk_i2cached_len(i2st)
    i2accepted_js = mk_i2accepted_js(j2len, i2st)

    i0
    jump_table
    #i2st
    #j2len
    i2cached_len
    i2accepted_js
        #i2is_accepted

    size_jump_table = sum(map(len, jump_table))
    assert 1 <= len(i2st) <= sum(j2len)
        # cached_len = max(map(max, st), default=0)
        # each cached_len can occur only once per j
        #   since other prefix is this suffix:
        #       let j s.t. cached_len==max(st[j])
        #       subseq_seq[j'][:max(st[j'])] other_prefix == this_prefix_suffix == subseq_seq[j][cached_len-max(st[j']):cached_len]

    #jump_table = MapView({i:MapView(val2next_i) for i, val2next_i in jump_table.items()})
    jump_table = FrozenDict({i:FrozenDict(val2next_i) for i, val2next_i in jump_table.items()})
    #i2st = tuple(i2st)
    (istate0, jump_table, istate2cached_len, istate2sorted_accepted_isubseqs) = (i0, jump_table, i2cached_len, i2accepted_js)
    #omit: i2st, j2len
    return (istate0, jump_table, istate2cached_len, istate2sorted_accepted_isubseqs)




