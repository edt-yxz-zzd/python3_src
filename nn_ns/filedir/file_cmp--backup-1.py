r'''
#'''
灭罗、姬乌 的 情节一模一样！大纲乱了？

bug:
    sa_idx, sa_idx+1
        may be of same lhs_uints/rhs_uints
        SA group into block by lhs_uints/rhs_uints
modifying:
    sorted_matched_rng_pairs
        ->
        sorted_matched_rng_pairs__by_lrng
        sorted_matched_rng_pairs__by_rrng

new algo:
    input:
        L = min_len of max_common_subblock
        lhs_uints
        rhs_uints
    split each xhs_uints into block of sz S=(L+1)//2
        polynomial hash of input len S
            neednot incomplete tail
        search block and then try to extend to sz L or large

search subseqs
    e ../../python3_src/seed/iters/search_subseqs.py
    not fast
    drop

from nn_ns.RMQ.make_SA_LCP import make_SA_LCP
from seed.algo.sort_ints import sort_ints
from seed.algo.is_sorted import is_sorted
from seed.seq_tools.iter_seq_range import seq_islice
from seed.types.view.SeqSliceView import SeqSliceView
from seed.iters.calc_common_prefix_length import calc_common_prefix_length
from seed.iters.merge_two_sorted_iterables import merge_two_sorted_iterables
from seed.iters.PeekableIterator import PeekableIterator
from seed.tiny import fst, snd


def bytes_diff(lcp_threshold, lhs_bytes, rhs_bytes):
    return uints_diff(lcp_threshold, 2**8, lhs_bytes, rhs_bytes)
def uints_diff(lcp_threshold, alphabet_size, lhs_uints, rhs_uints):
    '-> (sorted_matched_rng_pairs, sorted_untouch_unmatched_lrngs, sorted_untouch_unmatched_rrngs)'
    #LCP_THRESHOLD
    #lcp_threshold = LCP_THRESHOLD
    assert lcp_threshold > 0
    L = min(len(lhs_uints), len(rhs_uints))
    len_common_prefix = calc_common_prefix_length(lhs_uints, rhs_uints)
    len_tail = L - len_common_prefix
    assert 0 <= len_tail <= L
    reversed_lhs_uints_tail = seq_islice(lhs_uints, len(lhs_uints)-len_tail, reverse=True)
    reversed_rhs_uints_tail = seq_islice(rhs_uints, len(rhs_uints)-len_tail, reverse=True)
    len_common_suffix = calc_common_prefix_length(reversed_lhs_uints_tail, reversed_rhs_uints_tail)
    matched_rng_pairs = []
    if len_common_prefix:
        lrng = rrng = (0, len_common_prefix)
        matched_rng_pairs.append((lrng, rrng))

    if len_common_suffix:
        lrng = (len(lhs_uints)-len_common_suffix, len(lhs_uints))
        rrng = (len(rhs_uints)-len_common_suffix, len(rhs_uints))
        matched_rng_pairs.append((lrng, rrng))

    mid_lhs_uints = SeqSliceView(lhs_uints, range(len_common_prefix, len(lhs_uints)-len_common_suffix))
    mid_rhs_uints = SeqSliceView(rhs_uints, range(len_common_prefix, len(rhs_uints)-len_common_suffix))
    (mid_offseted_sorted_matched_rng_pairs
    sorted_matched_rng_pairs__by_lrng
    ,sorted_matched_rng_pairs__by_rrng
    , offseted_sorted_untouch_unmatched_lrngs, offseted_sorted_untouch_unmatched_rrngs) = _uints_diff(lcp_threshold, alphabet_size, mid_lhs_uints, mid_rhs_uints)
    def offset_rng(rng):
        begin, end = rng
        return begin+len_common_prefix, end+len_common_prefix
    def offset_rngs(rngs):
        return list(map(offset_rng, rngs))

    matched_rng_pairs[1:1] = ((offset_rng(lrng), offset_rng(rrng)) for lrng, rrng in mid_offseted_sorted_matched_rng_pairs)

    sorted_matched_rng_pairs = matched_rng_pairs
    sorted_untouch_unmatched_lrngs = offset_rngs(offseted_sorted_untouch_unmatched_lrngs)
    sorted_untouch_unmatched_rrngs = offset_rngs(offseted_sorted_untouch_unmatched_rrngs)

    check4result_of_uints_diff(
            sorted_matched_rng_pairs
            sorted_matched_rng_pairs__by_lrng
            ,sorted_matched_rng_pairs__by_rrng
            ,sorted_untouch_unmatched_lrngs
            ,sorted_untouch_unmatched_rrngs
            )
    return (sorted_matched_rng_pairs__by_lrng
            ,sorted_matched_rng_pairs__by_rrng
            ,sorted_untouch_unmatched_lrngs
            ,sorted_untouch_unmatched_rrngs
            )


def _uints_diff(lcp_threshold, alphabet_size, lhs_uints, rhs_uints):
    '-> (sorted_matched_rng_pairs__by_lrng, sorted_matched_rng_pairs__by_rrng, sorted_untouch_unmatched_lrngs, sorted_untouch_unmatched_rrngs)'
    alphabet_size += 1
    uints = (*(i+1 for i in lhs_uints), 0, *(i+1 for i in rhs_uints))
    (SA, LCP) = make_SA_LCP(uints, alphabet_size=alphabet_size)
    assert 0 < len(uints) == len(SA) == len(LCP)+1
    lcp2sa_idc = [[] for _ in range(max(LCP, default=-1)+1)]
    for sa_idx, lcp in enumerate(LCP):
        sa_idc = lcp2sa_idc[lcp]
        sa_idc.append(sa_idx)
    lcp2sa_idc_end = tuple(map(len, lcp2sa_idc))
    used_lrngs = bytearray(len(lhs_uints))
    used_rrngs = bytearray(len(rhs_uints))
    def used_rngs2sorted_untouch_unmatched_rngs(used_rngs):
        'used_rngs::[bit], unmatched_rngs::[rng]'
        unmatched_rngs = []
        end = len(used_rngs)
        i = begin = 0
        while i != end:
            curr_bit = used_rngs[i]
            next_bit = 1-curr_bit
            j = used_rngs.find(next_bit, i)
            if j < 0:
                j = end
            if not curr_bit:
                unmatched_rngs.append((i, j))
            i = j
        return unmatched_rngs
    def may_head_from_diff_rng_rngs(rng, used_rngs):
        begin, end = rng
        if begin < end: raise logic-err
        if used_rngs[begin]:
            return ()
        for i in range(begin, end):
            if used_rngs[i]:
                break
        else:
            i += 1
            assert i == end
        assert begin < i <= end
        return ((begin, i),)
    def insert_rng_into_rngs(rng, used_rngs):
        begin, end = rng
        if begin < end: raise logic-err
        for i in range(begin, end):
            if used_rngs[i]: raise logic-err
            used_rngs[i] = 1
        return used_rngs
    def len_rng(rng):
        begin, end = rng
        return end - begin
    matched_rng_pairs = []
    for lcp in reversed(range(len(lcp2sa_idc))):
        if lcp < lcp_threshold: continue
        sa_idc = lcp2sa_idc[lcp]
        sa_idc_end = lcp2sa_idc_end[lcp]
        for i in range(sa_idc_end-len(sa_idc), sa_idc_end):
            sa_idx = sa_idc[i]
            assert lcp == LCP[sa_idx] if i >= 0 else lcp < LCP[sa_idx]
            asuffix_idx = SA[sa_idx]
            bsuffix_idx = SA[sa_idx+1]
            assert asuffix_idx != len(lhs_uints)
            assert bsuffix_idx != len(lhs_uints)
            if (asuffix_idx < len(lhs_uints)) is (bsuffix_idx < len(lhs_uints)): continue
            if asuffix_idx < len(lhs_uints):
                lsuffix_idx = asuffix_idx
                rsuffix_idx = bsuffix_idx
            else:
                lsuffix_idx = bsuffix_idx
                rsuffix_idx = asuffix_idx
            assert lsuffix_idx < len(lhs_uints)
            assert rsuffix_idx > len(lhs_uints)
            rsuffix_idx -= len(lhs_uints)+1
            assert 0 <= lsuffix_idx < lsuffix_idx+lcp <= len(lhs_uints)
            assert 0 <= rsuffix_idx < rsuffix_idx+lcp <= len(rhs_uints)
            lrng = lsuffix_idx, lsuffix_idx+lcp
            rrng = rsuffix_idx, rsuffix_idx+lcp
            may_head_lrng = may_head_from_diff_rng_rngs(lrng, used_lrngs)
            may_head_rrng = may_head_from_diff_rng_rngs(rrng, used_rrngs)
            if not (may_head_lrng and may_head_rrng): continue
            [head_lrng] = may_head_lrng
            [head_rrng] = may_head_rrng
            lsz = len_rng(head_lrng)
            rsz = len_rng(head_rrng)
            sz = min(lsz, rsz)
            assert sz > 0
            using_lrng = (lsuffix_idx, lsuffix_idx+sz)
            using_rrng = (rsuffix_idx, rsuffix_idx+sz)
            assert using_lrng == head_lrng or using_rrng == head_rrng
            assert using_lrng[0] == head_lrng[0]
            assert using_rrng[0] == head_rrng[0]
            used_lrngs = insert_rng_into_rngs(using_lrng, used_lrngs)
            used_rrngs = insert_rng_into_rngs(using_rrng, used_rrngs)
            matched_rng_pairs.append((using_lrng, using_rrng))

    sorted_untouch_unmatched_lrngs = used_rngs2sorted_untouch_unmatched_rngs(using_lrng)
    sorted_untouch_unmatched_rrngs = used_rngs2sorted_untouch_unmatched_rngs(using_rrng)
    #matched_rng_pairs.sort()
    sorted_matched_rng_pairs__by_lrng = sort_ints(matched_rng_pairs, key=lambda rng_pair:rng_pair[0][0])
    sorted_matched_rng_pairs__by_rrng = sort_ints(matched_rng_pairs, key=lambda rng_pair:rng_pair[1][0])

    check4result_of_uints_diff(
            sorted_matched_rng_pairs__by_lrng
            ,sorted_matched_rng_pairs__by_rrng
            ,sorted_untouch_unmatched_lrngs
            ,sorted_untouch_unmatched_rrngs
            )
    return (sorted_matched_rng_pairs__by_lrng
            ,sorted_matched_rng_pairs__by_rrng
            ,sorted_untouch_unmatched_lrngs
            ,sorted_untouch_unmatched_rrngs
            )

def check4result_of_uints_diff(
            sorted_matched_rng_pairs__by_lrng
            ,sorted_matched_rng_pairs__by_rrng
            ,sorted_untouch_unmatched_lrngs
            ,sorted_untouch_unmatched_rrngs
            ):
    def before4rng__untouch(prev_rng, next_rng):
        return prev_rng[1] < next_rng[0]
    def before4rng__may_touch(prev_rng, next_rng):
        #for fst/snd rng_pair
        return prev_rng[1] <= next_rng[0]
    def before4rng__must_touch(prev_rng, next_rng):
        #for merged complementary
        return prev_rng[1] == next_rng[0]
    #sorted+nonoverlap/touch
    assert is_sorted(map(fst, sorted_matched_rng_pairs__by_lrng), before=before4rng__may_touch)
    assert is_sorted(map(snd, sorted_matched_rng_pairs__by_rrng), before=before4rng__may_touch)
    #sorted+untouch
    assert is_sorted(sorted_untouch_unmatched_lrngs, before=before4rng__untouch)
    assert is_sorted(sorted_untouch_unmatched_rrngs, before=before4rng__untouch)

    #nonempty
    assert all(map(len_rng, sorted_untouch_unmatched_lrngs))
    assert all(map(len_rng, sorted_untouch_unmatched_rrngs))
    assert all(all(map(len_rng, rng_pair))for rng_pair in sorted_matched_rng_pairs__by_lrng)
    assert all(all(map(len_rng, rng_pair))for rng_pair in sorted_matched_rng_pairs__by_rrng)

    #eq sz
    assert all(len_rng(lrng)==len_rng(rrng) for lrng, rrng in sorted_matched_rng_pairs__by_lrng)
    assert all(len_rng(lrng)==len_rng(rrng) for lrng, rrng in sorted_matched_rng_pairs__by_rrng)

    #complementary
    def check_complementary(touch_rngs, untouch_rngs):
        rngs = PeekableIterator(merge_two_sorted_iterables(touch_rngs, untouch_rngs))
        may_head_rng = rngs.peek_le(1)
        assert not may_head_rng or may_head_rng[0][0] == 0
        assert is_sorted(rngs, before=before4rng__must_touch)

    check_complementary(map(fst, sorted_matched_rng_pairs__by_lrng), sorted_untouch_unmatched_lrngs)
    check_complementary(map(snd, sorted_matched_rng_pairs__by_rrng), sorted_untouch_unmatched_rrngs)








