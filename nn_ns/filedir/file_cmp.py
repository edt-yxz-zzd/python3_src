r'''
bias patch
see:
    nn_ns.filedir.dir_cmp
        py::filecmp.dircmp/cmp/cmpfiles
    nn_ns.filedir.file_cmp #diff/patch/delta, O(n)
        py::difflib.restore/context_diff/Differ.compare/ndiff/unified_diff/diff_bytes
            O(n^2)
    nn_ns.filedir.inf_dir
    nn_ns.filedir.backup_util


TODO:
    DONE:main():
        subcmd:
            #diff -old -new -out -lcp_threshold -f
            #patch -old -patch -out -f
    pack lcp_threshold?? no or save external

nn_ns.filedir.file_cmp
py -m nn_ns.filedir.file_cmp

from nn_ns.filedir.file_cmp import uints_diff, bytes_diff, file_diff
from nn_ns.filedir.file_cmp import uints_patch, bytes_patch, file_patch
from nn_ns.filedir.file_cmp import mk_patch_uints, mk_patch_uints__iter, check_result4uints_diff, pack__patch_bytes_ex__ver1
from nn_ns.filedir.file_cmp import uints_patch__iter, unpack__patch_bytes_ex__ver1


>>> uints_diff(1, 0, b'', b'', to_mk_patch=True)
((), ())
>>> uints_diff(1, 0, b'', b'', to_mk_patch=False)
((), None)


>>> f = lambda lcp_threshold, alphabet_size, lhs_digit_str, rhs_digit_str: uints_diff(lcp_threshold, alphabet_size, tuple(map(int, lhs_digit_str)), tuple(map(int, rhs_digit_str)), to_mk_patch=True, _completely_test=True)

>>> f(1, 0, '', '')
((), ())
>>> f(1, 1, '', '0')
((1,), (0,))
>>> f(1, 1, '0', '')
((), ())
>>> f(1, 1, '0', '0')
(((0, 1),), ())
>>> f(1, 2, '0', '1')
((1,), (1,))


>>> f(1, 10, '12012302345605678', '12345678')
(((3, 6), (9, 12), (15, 17)), ())

>>> bytes_diff(4, b'12304567890891234', b'123567912356788912354', to_mk_patch=True, _completely_test=True)
((6, (12, 16), (5, 9), (11, 16), 2), b'12356754')
>>> bytes_patch(b'12304567890891234', (6, (12, 16), (5, 9), (11, 16), 2), b'12356754')
b'123567912356788912354'

>>> lhs_bytes = b'12304567890891234'
>>> rhs_bytes = b'123567912356788912354'
>>> all(rhs_bytes == bytes_patch(lhs_bytes, *bytes_diff(lcp_threshold, lhs_bytes, rhs_bytes, to_mk_patch=True, _completely_test=True)) for lcp_threshold in range(1, 1+max(len(lhs_bytes), len(rhs_bytes))))
True

>>> file_diff(4, lhs_bytes, rhs_bytes, ver=1)
b'\x00fpatch\xfe\x01(6,(12,16),(5,9),(11,16),2)\n12356754'

#'''

__all__ = '''
    uints_diff
        bytes_diff
            file_diff
                pack__patch_bytes_ex__ver1
        mk_patch_uints
            mk_patch_uints__iter
        check_result4uints_diff

    uints_patch
        uints_patch__iter
        bytes_patch
            file_patch
                unpack__patch_bytes_ex__ver1
    '''.split()
from nn_ns.RMQ.make_SA_LCP import make_SA_LCP
from seed.algo.sort_ints import sort_ints
from seed.algo.is_sorted import is_sorted
from seed.seq_tools.iter_seq_range import seq_islice
#from seed.seq_tools.seq_index_if import seq_find
from seed.types.view.SeqSliceView import SeqSliceView
from seed.iters.calc_common_prefix_length import calc_common_prefix_length
from seed.iters.merge_two_sorted_iterables import merge_two_sorted_iterables
from seed.iters.PeekableIterator import PeekableIterator
from seed.iters.find import find_subseq
from seed.iters.cmp4iterable import eq4iterable
from seed.tiny import fst, snd
from seed.tiny import assert_eq_f


import itertools
from collections.abc import Sequence
import ast
from pathlib import Path


def id_or_len_rng(len_or_rng):
    if type(len_or_rng) is int:
        return len_or_rng
    rng = len_or_rng
    return len_rng(rng)
def len_rng(rng):
    begin, end = rng
    return end-begin

class data4patch_bytes_ex:
    head_bytes = b'\x00fpatch\xFE'
    version_dynamic_bytes = b'\x01'
    sep_bytes = b'\n'
def unpack__patch_bytes_ex__ver1(patch_bytes_ex):
    '-> (saved_or_copied_rng_infos, patch_bytes)'
    X = data4patch_bytes_ex

    if patch_bytes_ex[:len(X.head_bytes)] != X.head_bytes: raise ValueError('not patch_bytes_ex')
    if patch_bytes_ex[len(X.head_bytes):len(X.head_bytes)+len(X.version_dynamic_bytes)] != X.version_dynamic_bytes: raise ValueError('patch_bytes_ex is not version 1')
    control_bytes_begin = len(X.head_bytes)+len(X.version_dynamic_bytes)
    control_bytes_end = patch_bytes_ex.index(X.sep_bytes, control_bytes_begin)
    patch_bytes_begin = control_bytes_end + len(X.sep_bytes)
    control_bytes = patch_bytes_ex[control_bytes_begin:control_bytes_end]
    patch_bytes = patch_bytes_ex[patch_bytes_begin:]
    saved_or_copied_rng_infos = ast.literal_eval(control_bytes.decode('ascii'))
    return saved_or_copied_rng_infos, patch_bytes

def pack__patch_bytes_ex__ver1(saved_or_copied_rng_infos, patch_bytes):
    '-> patch_bytes_ex'
    X = data4patch_bytes_ex

    control_bytes = str(saved_or_copied_rng_infos).replace(' ', '').encode('ascii')
    assert X.sep_bytes
    assert X.sep_bytes[0] not in control_bytes
    patch_bytes_ex = b''.join([X.head_bytes, X.version_dynamic_bytes, control_bytes, X.sep_bytes, patch_bytes])

    assert (saved_or_copied_rng_infos, patch_bytes) == unpack__patch_bytes_ex__ver1(patch_bytes_ex)
    return patch_bytes_ex

def file_diff(lcp_threshold, lhs_bytes, rhs_bytes, /, *, ver:int):
    '-> patch_bytes_ex'
    if ver != 1: raise NotImplementedError

    (saved_or_copied_rng_infos, patch_bytes) = bytes_diff(lcp_threshold, lhs_bytes, rhs_bytes, to_mk_patch=True, _completely_test=False)
    patch_bytes_ex = pack__patch_bytes_ex__ver1(saved_or_copied_rng_infos, patch_bytes)

    assert rhs_bytes == file_patch(lhs_bytes, patch_bytes_ex, ver=ver)
    return patch_bytes_ex


def bytes_diff(lcp_threshold, lhs_bytes, rhs_bytes, *, to_mk_patch:bool, _completely_test:bool=False):
    '-> (saved_or_copied_rng_infos, may_patch_bytes)'
    (saved_or_copied_rng_infos, may_patch_bytes) = uints_diff(lcp_threshold, 2**8, lhs_bytes, rhs_bytes, to_mk_patch=to_mk_patch, _completely_test=_completely_test, patch_uints_from_iterable=bytes)

    #if to_mk_patch: assert rhs_bytes == bytes_patch(lhs_bytes, saved_or_copied_rng_infos, patch_bytes)
    return (saved_or_copied_rng_infos, may_patch_bytes)

def uints_diff(lcp_threshold, alphabet_size, lhs_uints, rhs_uints, *, to_mk_patch:bool, _completely_test:bool=False, patch_uints_from_iterable=None):
    r'''
    diff/patch

    bias:
        lhs_uints = old_uints
        rhs_uints = new_uints
        findout howto generate rhs_uints base on lhs_uints

        using method_2 instead of method_1
        method:
          *method_1:
            max lcp between lhs_uints/rhs_uints # >= lcp_threshold
                then min rhs_isuffix
                then min lhs_isuffix
            too hard to impl
                , since bigger lcp may have bigger rhs_isuffix which may overlap tail of smaller rhs_isuffix to make the smaller lcp become smaller
          *method_2:
            min rhs_isuffix
                then max lcp between lhs_uints/rhs_isuffix # >= lcp_threshold
                then min lhs_isuffix
        overlap:
            ###################
            2~1/1: rhs_isuffix_begin0 rhs_isuffix_begin1 rhs_isuffix_end0 rhs_isuffix_end1
            lcp_threshold < rhs_isuffix_begin1-rhs_isuffix_begin0 < lcp0==len_rrng0 < lcp1==len_rrng1
            ###################
            method_1:
                choose rrng1 first
                then choose (rhs_isuffix_begin0, rhs_isuffix_begin1)
            method_2:
                choose rrng0 first
                then choose (rhs_isuffix_end0, rhs_isuffix_end1)
            ###################
            ###################
            3~1/2: rhs_isuffix_begin0 rhs_isuffix_begin1 rhs_isuffix_begin2 rhs_isuffix_end0 rhs_isuffix_end1 rhs_isuffix_end2
            lcp_threshold < rhs_isuffix_begin1-rhs_isuffix_begin0 < lcp0==len_rrng0 < lcp1==len_rrng1 < lcp2==len_rrng2
            lcp_threshold < rhs_isuffix_begin2-rhs_isuffix_begin1 < lcp1==len_rrng1 < lcp2==len_rrng2
            ###################
            method_1:
                choose rrng2 first
                then choose (rhs_isuffix_begin0, rhs_isuffix_begin2)
            method_2:
                choose rrng0 first
                then choose (rhs_isuffix_end0, rhs_isuffix_end2)
            ###################
            ###################
            3~2/2: rhs_isuffix_begin0 rhs_isuffix_begin1 rhs_isuffix_end0 rhs_isuffix_begin2 rhs_isuffix_end1 rhs_isuffix_end2
            lcp_threshold < rhs_isuffix_begin1-rhs_isuffix_begin0 < lcp0==len_rrng0 < lcp1==len_rrng1 < lcp2==len_rrng2
            lcp_threshold < rhs_isuffix_begin2-rhs_isuffix_begin1 < lcp1==len_rrng1 < lcp2==len_rrng2
            ###################
            method_1:
                choose rrng2 first
                then choose:
                    * (rhs_isuffix_begin1, rhs_isuffix_begin2)
                    * (rhs_isuffix_begin1, rhs_isuffix_begin2), (rhs_isuffix_begin0, rhs_isuffix_begin1)
                    * rrng0
                    * rrng0, (rhs_isuffix_end0, rhs_isuffix_begin2)
            method_2:
                choose rrng0 first
                then choose (rhs_isuffix_end0, rhs_isuffix_end1), (rhs_isuffix_end1, rhs_isuffix_end2)
                # more fragile
                # more fragments
                # but cover more rhs_uints
            ###################

    input:
        lcp_threshold :: pint
            min copied lhs block size
        alphabet_size :: uint
            uint bound of lhs_uints, rhs_uints
        lhs_uints :: [uint%alphabet_size]
            old/source
        rhs_uints :: [uint%alphabet_size]
            new/target
        to_mk_patch :: bool
            see: output.may_patch_uints type
    output:
        # -> (saved_or_copied_rng_infos, may_patch_uints)

        saved_or_copied_rng_infos :: [(len_prng|lrng)]
            len_prng - save rhs_uints block into patch_uints directly
            lrng - copy from lhs_uints block
            ##
            lrng = rng of lhs_uints
            rrng = rng of rhs_uints
            prng = rng of patch_uints

        may_patch_uints :: None if not to_mk_patch else [uint%alphabet_size]
            patch which save some raw rhs blocks

    ###########################
    ###########################
    assert len(rhs_uints) == sum((len_prng|len_rng(lrng)) for (len_prng|lrng) in result)
    assert len(patch_uints) == sum(len_prng for (len_prng|lrng) in result)

    rhs_begin = 0
    patch_begin = 0
    for (len_prng|lrng) in result:
        * len_prng:
            len_rrng = len_prng
            rhs_end = rhs_begin + len_rrng
            rrng = rhs_begin, rhs_end
            patch_end = patch_begin + len_prng
            prng = patch_begin, patch_end

            assert rhs_uints[rhs_begin:rhs_end] == patch_uints[patch_begin:patch_end]
            patch_begin = patch_end
            rhs_begin = rhs_end

        * lrng:
            len_lrng = len_rng(lrng)
            len_rrng = len_lrng
            rhs_end = rhs_begin + len_rrng
            rrng = rhs_begin, rhs_end
            lhs_begin, lhs_end = lrng

            assert rhs_uints[rhs_begin:rhs_end] == lhs_uints[lhs_begin:lhs_end]
            rhs_begin = rhs_end
    ###########################
    ###########################
    #'''
    '-> (sorted_matched_rng_pairs, sorted_untouch_unmatched_lrngs, sorted_untouch_unmatched_rrngs)'
    #LCP_THRESHOLD
    #lcp_threshold = LCP_THRESHOLD
    if not isinstance(lcp_threshold, int):raise TypeError
    if not isinstance(alphabet_size, int):raise TypeError
    if not isinstance(to_mk_patch, bool):raise TypeError
    if not isinstance(_completely_test, bool):raise TypeError
    if not (patch_uints_from_iterable is None or callable(patch_uints_from_iterable)):raise TypeError
    if not isinstance(lhs_uints, Sequence):raise TypeError
    if not isinstance(rhs_uints, Sequence):raise TypeError
    if not lcp_threshold >= 1: raise ValueError
    if not alphabet_size >= 0: raise ValueError

    check_uints__alphabet_size(alphabet_size, lhs_uints)
    check_uints__alphabet_size(alphabet_size, rhs_uints)
    saved_or_copied_rng_infos = _uints_diff(lcp_threshold, alphabet_size, lhs_uints, rhs_uints)

    if to_mk_patch:
        patch_uints = mk_patch_uints(rhs_uints, saved_or_copied_rng_infos, patch_uints_from_iterable=patch_uints_from_iterable)
        may_patch_uints = patch_uints
    else:
        may_patch_uints = None

    check_result4uints_diff(lcp_threshold, lhs_uints, rhs_uints, saved_or_copied_rng_infos, may_patch_uints, completely_test=_completely_test)
    return saved_or_copied_rng_infos, may_patch_uints

# discarded: len_common_prefix
    #   since mid_lhs_uints miss prefix which may offer lrng for copying
    L = min(len(lhs_uints), len(rhs_uints))
    len_common_prefix = calc_common_prefix_length(lhs_uints, rhs_uints)
    if len_common_prefix >= lcp_threshold:
        lrng = rrng = (0, len_common_prefix)

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
    offseted_saved_or_copied_rng_infos = _uints_diff(lcp_threshold, alphabet_size, mid_lhs_uints, mid_rhs_uints)
    def offset_rng(rng):
        begin, end = rng
        return begin+len_common_prefix, end+len_common_prefix
    def offset_rngs(rngs):
        return list(map(offset_rng, rngs))
    ...
    ...

def check_uints__alphabet_size(alphabet_size, uints):
    if uints:
        if not max(uints) < alphabet_size: raise ValueError
        if not min(uints) >= 0: raise ValueError
def _uints_diff(lcp_threshold, alphabet_size, lhs_uints, rhs_uints):
    '-> saved_or_copied_rng_infos'
    if len(lhs_uints) < lcp_threshold or len(rhs_uints) < lcp_threshold:
        saved_len_prng = len(rhs_uints)
        #bug: return (saved_len_prng,)
        return (saved_len_prng,) if saved_len_prng else ()

    uints = (*lhs_uints, alphabet_size, *rhs_uints)
    #alphabet_size += 1
    (SA, LCP) = make_SA_LCP(uints, alphabet_size=alphabet_size+1)
        # alphabet_size+1
    assert 0 < len(uints) == len(SA) == len(LCP)+1
    max_lcp = max(LCP, default=0)
    if max_lcp < lcp_threshold:
        saved_len_prng = len(rhs_uints)
        return (saved_len_prng,) if saved_len_prng else ()
        return (saved_len_prng,)
    if 0:
        print(f'uints={uints!r}')
        print(f'SA={SA!r}')
        print(f'LCP={LCP!r}')

    def is_isuffix_lhs(isuffix):
        return isuffix <= len(lhs_uints)
        #isuffix == len(lhs_uints) is ''
    def is_isuffix_rhs(isuffix):
        return isuffix > len(lhs_uints)
    assert is_isuffix_lhs(len(lhs_uints))
    assert not is_isuffix_rhs(len(lhs_uints))

    def raw_match_LR(isuffixes, lcps):
        # -> Iter (lhs_isuffix, lcp, rhs_isuffix)
        # only one direction, should call twice
        isuffixes = iter(isuffixes)
        lcps = iter(lcps)
        for prev_isuffix in isuffixes:
            break
        it = zip(lcps, isuffixes)
        it = PeekableIterator(it)
        del isuffixes, lcps
        def seek_may_prev_lhs_isuffix(prev_isuffix, it):
            '-> may prev_lhs_isuffix'
            while 1:
                if is_isuffix_lhs(prev_isuffix):
                    prev_lhs_isuffix = prev_isuffix
                    return (prev_lhs_isuffix,)
                else:
                    for lcp, isuffix in it:
                        prev_isuffix = isuffix
                        break
                    else:
                        return ()
        def seek_prev_lhs_isuffix_followed_by_rhs_isuffix_or_eof(bisorted_lcp_min_lhs_isuffix_pairs, prev_lhs_isuffix, it):
            r'''-> nonempty strict bisorted_lcp_min_lhs_isuffix_pairs

            strict bisorted:
                lcp < next.lcp
                and lhs_isuffix < next.lhs_isuffix
            #'''
            assert is_isuffix_lhs(prev_lhs_isuffix)
            def put(curr_lcp, curr_lhs_isuffix):
                while bisorted_lcp_min_lhs_isuffix_pairs:
                    prev_lcp, prev_lhs_isuffix = bisorted_lcp_min_lhs_isuffix_pairs[-1]
                    if curr_lcp <= prev_lcp:
                        prev_lcp = curr_lcp # = min(prev_lcp, curr_lcp)
                        bisorted_lcp_min_lhs_isuffix_pairs.pop()
                        curr_lhs_isuffix = min(prev_lhs_isuffix, curr_lhs_isuffix)
                        continue
                    elif curr_lhs_isuffix <= prev_lhs_isuffix:
                        bisorted_lcp_min_lhs_isuffix_pairs.pop()
                        continue
                    else:
                        #strict bisorted
                        break
                ##
                bisorted_lcp_min_lhs_isuffix_pairs.append((curr_lcp, curr_lhs_isuffix))
                return

            prev_lcp = it.peek1()[0] if not it.is_empty() else 0
            #bisorted_lcp_min_lhs_isuffix_pairs = [(prev_lcp, prev_lhs_isuffix)]
            put(prev_lcp, prev_lhs_isuffix)

            for _lcp, isuffix in it:
                if is_isuffix_lhs(isuffix):
                    curr_lhs_isuffix = isuffix
                    if not it.is_empty():
                        curr_lcp, _ = it.peek1()
                    else:
                        curr_lcp = 0
                    curr_lcp

                    put(curr_lcp, curr_lhs_isuffix)
                else:
                    assert is_isuffix_rhs(isuffix)
                    rhs_isuffix = isuffix
                    #put back
                    it.append_left((_lcp, rhs_isuffix))
                    break
            assert bisorted_lcp_min_lhs_isuffix_pairs
            return bisorted_lcp_min_lhs_isuffix_pairs
        def handle_section__lhs_rhss(bisorted_lcp_min_lhs_isuffix_pairs, it):
            #-> Iter (prev_lhs_isuffix, lcp, rhs_isuffix)++last be may_prev_lhs_isuffix
            def f():
                prev_lcp, prev_lhs_isuffix = bisorted_lcp_min_lhs_isuffix_pairs[-1]
                if len(bisorted_lcp_min_lhs_isuffix_pairs) > 1:
                    lcp_pop, _ = bisorted_lcp_min_lhs_isuffix_pairs[-2]
                else:
                    lcp_pop = -1
                return lcp_pop, prev_lcp, prev_lhs_isuffix
            lcp_pop, prev_lcp, prev_lhs_isuffix = f()
            for lcp, isuffix in it:
                lcp = min(prev_lcp, lcp)
                while lcp <= lcp_pop:
                    bisorted_lcp_min_lhs_isuffix_pairs.pop()
                    lcp_pop, prev_lcp, prev_lhs_isuffix = f()
                assert -1 <= lcp_pop < lcp <= prev_lcp
                prev_lcp = lcp
                if is_isuffix_lhs(isuffix):
                    prev_lhs_isuffix = isuffix
                    may_prev_lhs_isuffix = (prev_lhs_isuffix,)
                    break
                else:
                    assert is_isuffix_rhs(isuffix)
                    rhs_isuffix = isuffix
                    yield (prev_lhs_isuffix, lcp, rhs_isuffix)
            else:
                may_prev_lhs_isuffix = ()
            bisorted_lcp_min_lhs_isuffix_pairs.pop()
            bisorted_lcp_min_lhs_isuffix_pairs.append((prev_lcp, prev_lhs_isuffix))
            yield may_prev_lhs_isuffix
            return

        may_prev_lhs_isuffix = seek_may_prev_lhs_isuffix(prev_isuffix, it)
        bisorted_lcp_min_lhs_isuffix_pairs = [(0, len(lhs_uints))]
        while 1:
            if not may_prev_lhs_isuffix:
                return
            [prev_lhs_isuffix] = may_prev_lhs_isuffix
            bisorted_lcp_min_lhs_isuffix_pairs = seek_prev_lhs_isuffix_followed_by_rhs_isuffix_or_eof(bisorted_lcp_min_lhs_isuffix_pairs, prev_lhs_isuffix, it)

            ##
            done = False
            for x in handle_section__lhs_rhss(bisorted_lcp_min_lhs_isuffix_pairs, it):
                if done: raise logic-err
                if len(x) < 2:
                    may_prev_lhs_isuffix = x
                    done = True
                else:
                    (lhs_isuffix, lcp, rhs_isuffix) = x
                    yield (lhs_isuffix, lcp, rhs_isuffix)
            else:
                if not done: raise logic-err
        # -> Iter (lhs_isuffix, lcp, rhs_isuffix)
        return
    def max_lcp_min_lhs_isuffix(a__may_lcp_lhs_isuffix_pair, b__lcp_lhs_isuffix_pair):
        if a__may_lcp_lhs_isuffix_pair is None:
            return b__lcp_lhs_isuffix_pair
        a__lcp_lhs_isuffix_pair = a__may_lcp_lhs_isuffix_pair

        def f(lcp_lhs_isuffix_pair):
            lcp, lhs_isuffix = lcp_lhs_isuffix_pair
            return -lcp, lhs_isuffix
        return min(a__lcp_lhs_isuffix_pair, b__lcp_lhs_isuffix_pair, key=f)

    #raw_match_LR(isuffixes, lcps)
    it_lr = raw_match_LR(SA, LCP)
    it_rl = raw_match_LR(reversed(SA), reversed(LCP))
    it_bi = itertools.chain(it_lr, it_rl)
    if 0:
        it_bi = [*it_bi]
        print(f'it_bi={it_bi!r}')
    rhs_isuffix2max_lcp_min_lhs_isuffix_pair = [None]*len(rhs_uints)
    for (lhs_isuffix, lcp, rhs_isuffix) in it_bi:
        #bug: rhs_isuffix -= len(lhs_uints)
        rhs_isuffix -= len(lhs_uints)+1
        #assert 0 <= rhs_isuffix <= len(rhs_uints)
        assert 0 <= rhs_isuffix < len(rhs_uints)
        rhs_isuffix2max_lcp_min_lhs_isuffix_pair[rhs_isuffix] = max_lcp_min_lhs_isuffix(rhs_isuffix2max_lcp_min_lhs_isuffix_pair[rhs_isuffix], (lcp, lhs_isuffix))
    assert all(x is not None for x in rhs_isuffix2max_lcp_min_lhs_isuffix_pair)
    if 0:
        print(f'rhs_isuffix2max_lcp_min_lhs_isuffix_pair={rhs_isuffix2max_lcp_min_lhs_isuffix_pair!r}')

    #-> saved_or_copied_rng_infos
    saved_or_copied_rng_infos = []
    rhs_begin = 0
    while rhs_begin < len(rhs_uints):
        for rhs_end in range(rhs_begin, len(rhs_uints)):
            lcp, lhs_isuffix = rhs_isuffix2max_lcp_min_lhs_isuffix_pair[rhs_end]
            if lcp >= lcp_threshold:
                break
        else:
            rhs_end = len(rhs_uints)

        if rhs_begin == rhs_end:
            #rhs_begin.lcp >= lcp_threshold:
            #copy
            lcp, lhs_isuffix = rhs_isuffix2max_lcp_min_lhs_isuffix_pair[rhs_begin]
            assert lcp >= lcp_threshold
            len_lrng = len_rrng = lcp
            r = lrng = lhs_isuffix, lhs_isuffix+len_lrng
            rhs_end = rhs_begin+len_rrng
        else:
            #rhs_begin < rhs_end
            #save
            assert rhs_begin < rhs_end
            r = len_prng = len_rrng = rhs_end-rhs_begin
        saved_or_copied_rng_infos.append(r)
        rhs_begin += len_rrng

    check_result4uints_diff(lcp_threshold, lhs_uints, rhs_uints, saved_or_copied_rng_infos, None, completely_test=False)
    return tuple(saved_or_copied_rng_infos)

def mk_patch_uints(rhs_uints, saved_or_copied_rng_infos, *, patch_uints_from_iterable=None):
    '-> patch_uints'
    if patch_uints_from_iterable is None:
        patch_uints_from_iterable = tuple

    it = mk_patch_uints__iter(rhs_uints, saved_or_copied_rng_infos)
    patch_uints = patch_uints_from_iterable(it)
    return patch_uints
def mk_patch_uints__iter(rhs_uints, saved_or_copied_rng_infos, /):
    '-> iter_patch_uints'

    patch_begin = patch_end = 0
    rhs_begin = rhs_end = 0
    for len_prng_or_lrng in saved_or_copied_rng_infos:
        if type(len_prng_or_lrng) is int:
            len_prng = len_prng_or_lrng
            assert len_prng > 0

            len_rrng = len_prng
            rhs_end = rhs_begin + len_rrng
            rrng = rhs_begin, rhs_end
            patch_end = patch_begin + len_prng
            prng = patch_begin, patch_end

            yield from seq_islice(rhs_uints, rhs_begin, rhs_end)
            assert 0 <= patch_begin < patch_end# == len(patch_uints)
            patch_begin = patch_end
            rhs_begin = rhs_end

        else:
            lrng = len_prng_or_lrng
            lhs_begin, lhs_end = lrng
            assert 0 <= lhs_begin < lhs_end #<= len(lhs_uints)
            #assert len_rng(lrng) >= lcp_threshold

            len_lrng = len_rng(lrng)
            len_rrng = len_lrng
            rhs_end = rhs_begin + len_rrng
            rrng = rhs_begin, rhs_end
            lhs_begin, lhs_end = lrng

            rhs_begin = rhs_end
    assert rhs_end == len(rhs_uints)
    assert sum(filter(lambda x:type(x) is int, saved_or_copied_rng_infos)) == patch_end #== len(patch_uints)
    return


def check_result4uints_diff(lcp_threshold, lhs_uints, rhs_uints, saved_or_copied_rng_infos, may_patch_uints, *, completely_test:bool):
    assert lcp_threshold > 0
    assert sum(map(id_or_len_rng, saved_or_copied_rng_infos)) == len(rhs_uints)
    if may_patch_uints is not None:
        patch_uints = may_patch_uints
        assert sum(filter(lambda x:type(x) is int, saved_or_copied_rng_infos)) == len(patch_uints)
        #assert uints_patch(lhs_uints, saved_or_copied_rng_infos, patch_uints) == tuple(rhs_uints)
        assert eq4iterable(uints_patch__iter(lhs_uints, saved_or_copied_rng_infos, patch_uints), rhs_uints)

    #if 1: print(check_result4uints_diff, lcp_threshold, lhs_uints, rhs_uints, saved_or_copied_rng_infos, may_patch_uints, completely_test)
    patch_begin = patch_end = 0
    rhs_begin = rhs_end = 0
    for len_prng_or_lrng in saved_or_copied_rng_infos:
        if type(len_prng_or_lrng) is int:
            len_prng = len_prng_or_lrng
            assert len_prng > 0

            len_rrng = len_prng
            rhs_end = rhs_begin + len_rrng
            rrng = rhs_begin, rhs_end
            patch_end = patch_begin + len_prng
            prng = patch_begin, patch_end

            assert 0 <= rhs_begin < rhs_end <= len(rhs_uints)
            if may_patch_uints is not None:
                assert 0 <= patch_begin < patch_end <= len(patch_uints)
                assert rhs_uints[rhs_begin:rhs_end] == patch_uints[patch_begin:patch_end]
            if completely_test:
                #bug:for rhs_isuffix in range(rhs_begin, rhs_end): ==>> len(rhs_sub) may lt lcp_threshold
                for rhs_isuffix in range(rhs_begin, min(rhs_end, len(rhs_uints)-lcp_threshold+1)):
                    #lcp < lcp_threshold
                    assert rhs_isuffix+lcp_threshold <= len(rhs_uints)
                    rhs_sub = rhs_uints[rhs_isuffix:rhs_isuffix+lcp_threshold]
                    assert len(rhs_sub) == lcp_threshold
                    if 0:
                        print(f'lhs_uints={lhs_uints!r}')
                        print(f'rhs_sub={rhs_sub!r}')
                        print(f'len_prng={len_prng!r}')
                        print(f'saved_or_copied_rng_infos={saved_or_copied_rng_infos!r}')
                        print(f'lcp_threshold={lcp_threshold!r}')
                        print(f'rhs_begin={rhs_begin!r}')
                        print(f'rhs_end={rhs_end!r}')
                    assert 0 > find_subseq(lhs_uints, rhs_sub)

            #bug: below 2 lines put before "if completely_test"
            patch_begin = patch_end
            rhs_begin = rhs_end


        else:
            lrng = len_prng_or_lrng
            lhs_begin, lhs_end = lrng
            assert 0 <= lhs_begin < lhs_end <= len(lhs_uints)
            assert len_rng(lrng) >= lcp_threshold

            len_lrng = len_rng(lrng)
            len_rrng = len_lrng
            rhs_end = rhs_begin + len_rrng
            rrng = rhs_begin, rhs_end
            lhs_begin, lhs_end = lrng

            assert rhs_uints[rhs_begin:rhs_end] == lhs_uints[lhs_begin:lhs_end]

            if completely_test:
                rhs_sub = rhs_uints[rhs_begin:rhs_end]
                #min lhs_isuffix
                assert lhs_begin == find_subseq(lhs_uints, rhs_sub)

                if rhs_end != len(rhs_uints):
                    #max lcp
                    rhs_sub_ex1 = rhs_uints[rhs_begin:rhs_end+1]
                    assert 0 > find_subseq(lhs_uints, rhs_sub_ex1)

            #bug: below 1 lines put before "if completely_test"
            rhs_begin = rhs_end


    if may_patch_uints is not None:
        assert patch_end == len(patch_uints)
    assert rhs_end == len(rhs_uints)

def file_patch(lhs_bytes, patch_bytes_ex, /, *, ver:int):
    '-> rhs_bytes'
    if ver != 1: raise NotImplementedError

    (saved_or_copied_rng_infos, patch_bytes) = unpack__patch_bytes_ex__ver1(patch_bytes_ex)
    rhs_bytes = bytes_patch(lhs_bytes, saved_or_copied_rng_infos, patch_bytes)
    return rhs_bytes

def bytes_patch(lhs_bytes, saved_or_copied_rng_infos, patch_bytes):
    '-> rhs_bytes'
    rhs_bytes = uints_patch(lhs_bytes, saved_or_copied_rng_infos, patch_bytes, rhs_uints_from_iterable=bytes)
    return rhs_bytes
def uints_patch(lhs_uints, saved_or_copied_rng_infos, patch_uints, /, *, rhs_uints_from_iterable=None):
    '-> rhs_uints'
    if rhs_uints_from_iterable is None:
        rhs_uints_from_iterable = tuple

    it = uints_patch__iter(lhs_uints, saved_or_copied_rng_infos, patch_uints)
    rhs_uints = rhs_uints_from_iterable(it)
    return rhs_uints
def uints_patch__iter(lhs_uints, saved_or_copied_rng_infos, patch_uints):
    '-> iter_rhs_uints'
    patch_begin = patch_end = 0
    rhs_begin = rhs_end = 0
    for len_prng_or_lrng in saved_or_copied_rng_infos:
        if type(len_prng_or_lrng) is int:
            len_prng = len_prng_or_lrng
            assert len_prng > 0

            len_rrng = len_prng
            rhs_end = rhs_begin + len_rrng
            rrng = rhs_begin, rhs_end
            patch_end = patch_begin + len_prng
            prng = patch_begin, patch_end

            assert 0 <= patch_begin < patch_end <= len(patch_uints)
            yield from seq_islice(patch_uints, patch_begin, patch_end)
            patch_begin = patch_end
            rhs_begin = rhs_end

        else:
            lrng = len_prng_or_lrng
            lhs_begin, lhs_end = lrng
            assert 0 <= lhs_begin < lhs_end <= len(lhs_uints)
            #assert len_rng(lrng) >= lcp_threshold

            len_lrng = len_rng(lrng)
            len_rrng = len_lrng
            rhs_end = rhs_begin + len_rrng
            rrng = rhs_begin, rhs_end
            lhs_begin, lhs_end = lrng

            yield from seq_islice(lhs_uints, lhs_begin, lhs_end)
            rhs_begin = rhs_end

    assert patch_end == len(patch_uints)
    #assert rhs_end == len(rhs_uints)






def _t1():
    f = lambda lcp_threshold, alphabet_size, lhs_digit_str, rhs_digit_str: uints_diff(lcp_threshold, alphabet_size, tuple(map(int, lhs_digit_str)), tuple(map(int, rhs_digit_str)), to_mk_patch=True, _completely_test=True)
    r = f(1, 1, '0', '0')
    ans = (((0, 1),), ())
    assert_eq_f((((0, 1),), ()), f, 1, 1, '0', '0')

def _t2():
    lhs_bytes = b'12304567890891234'
    rhs_bytes = b'123567912356788912354'
    for lcp_threshold in range(1, 1+max(len(lhs_bytes), len(rhs_bytes))):
        #print(f'lcp_threshold={lcp_threshold!r}')
        pair = bytes_diff(lcp_threshold, lhs_bytes, rhs_bytes, to_mk_patch=True, _completely_test=True)
        assert_eq_f(rhs_bytes, bytes_patch, lhs_bytes, *pair, vars=dict(lcp_threshold=lcp_threshold))





class _Main:
    def on_subcmd__diff(sf, subcmd_name, parsed_args):
        file_diff
        #diff -old -new -out -lcp_threshold -f
        old_ipath = Path(parsed_args.old_ifile)
        new_ipath = Path(parsed_args.new_ifile)
        patch_opath = Path(parsed_args.patch_ofile)

        force = parsed_args.force
        omode = 'wb' if force else 'xb'

        lcp_threshold = parsed_args.lcp_threshold
        if not lcp_threshold >= 1: raise ValueError
        lhs_bytes = old_ipath.read_bytes()
        rhs_bytes = new_ipath.read_bytes()
        with open(patch_opath, omode) as fout:
            patch_bytes_ex = file_diff(lcp_threshold, lhs_bytes, rhs_bytes, ver=1)
            fout.write(patch_bytes_ex)

    def on_subcmd__patch(sf, subcmd_name, parsed_args):
        file_patch
        #patch -old -patch -out -f
        old_ipath = Path(parsed_args.old_ifile)
        patch_ipath = Path(parsed_args.patch_ifile)
        new_opath = Path(parsed_args.new_ofile)

        force = parsed_args.force
        omode = 'wb' if force else 'xb'

        lhs_bytes = old_ipath.read_bytes()
        patch_bytes_ex = patch_ipath.read_bytes()

        rhs_bytes = file_patch(lhs_bytes, patch_bytes_ex, ver=1)
        with open(new_opath, omode) as fout:
            fout.write(rhs_bytes)

    def on_no_subcmd(sf, subcmd_name, parsed_args):
        sf.parser.print_help()
        #raise NotImplementedError
    @classmethod
    def _mk_option_config_(cls):
        '-> ([parent::ArgParserPrepare], [common_option::GetArgsKwargs], {group_name:{subcmd:ArgParserPrepare}})'
        Get, Pack = cls.Get, cls.Pack

        #diff -old -new -out -lcp_threshold -f
        #patch -old -patch -out -f
        options_diff = (
    [Get('-n', '--lcp_threshold', type=int, required=True, help='copy bytes from the old file to restore the new file, lcp_threshold set the min length of such copied bytes')
    ,Get('-old', '--old_ifile', type=str, required=True, help='the input old/source file path')
    ,Get('-new', '--new_ifile', type=str, required=True, help='the input new/target file path')
    ,Get('-out', '--patch_ofile', type=str, required=True, help='the output patch file path')
    ,Get('-f', '--force', action='store_true', default = False, required=False, help='open mode for output file')
        ])



        options_patch = (
    [Get('-old', '--old_ifile', type=str, required=True, help='the input old/source file path')
    ,Get('-patch', '--patch_ifile', type=str, required=True, help='the input patch file path')
    ,Get('-out', '--new_ofile', type=str, required=True, help='the output new/target file path')
    ,Get('-f', '--force', action='store_true', default = False, required=False, help='open mode for output file')
        ])

        prepare_diff = Pack([], options_diff, {})
        prepare_patch = Pack([], options_patch, {})
        subcmd2prepare_FILE_BACKUP_RESTORE = (dict
            (diff=prepare_diff
            ,patch=prepare_patch
            ))
        group_name2subcmd2prepare = (dict
            (FILE_BACKUP_RESTORE=subcmd2prepare_FILE_BACKUP_RESTORE
            ))
        return [], [], group_name2subcmd2prepare
def main(args=None):
    from seed.for_libs.for_argparse.subcmd import Main4subcmd
    class Main(_Main, Main4subcmd):
        pass
    return Main(description='diff/patch - used to backup and restore file', subcmd_dest_name='subcmd').main(args)


def _test_main(dir_path):
    import tempfile
    lhs_bytes = b'12304567890891234'
    rhs_bytes = b'123567912356788912354'
    lcp_threshold = 4
    with tempfile.TemporaryDirectory(dir=dir_path, prefix = '.', suffix = '~') as odir:
        #odir = Path(odir)
        old = odir+'/old'
        new1 = odir+'/new1'
        patch = odir+'/patch'
        new2 = odir+'/new2'

        Path(old).write_bytes(lhs_bytes)
        Path(new1).write_bytes(rhs_bytes)

        main(['diff', '-old', old, '-new', new1, '-n', str(lcp_threshold), '-out', patch])
        main(['patch', '-old', old, '-patch', patch, '-out', new2])

        rhs_bytes1 = Path(new1).read_bytes()
        rhs_bytes2 = Path(new2).read_bytes()
        assert rhs_bytes1 == rhs_bytes
        assert rhs_bytes2 == rhs_bytes1


if 0:
    if __name__ == "__main__":
        _t1()
        _t2()

    if __name__ == "__main__":
        import doctest
        doctest.testmod()
        ##
    if __name__ == "__main__":
        _test_main('/sdcard/0my_files/tmp/for-test/file_cmp/')




if __name__ == "__main__":
    main()




