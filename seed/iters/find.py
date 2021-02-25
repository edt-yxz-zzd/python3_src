
r'''
seed.iters.find
py -m seed.iters.find
from seed.iters.find import iter_search_subseq_on_seq, iter_search_subseq_on_stream


see:
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
    mk_last_succ_pos2restart_pos
    mk_last_succ_pos2restart_pos__from_seq
    mk_last_pos2len_longest_proper_bifix
    FindSubseqOverlap
    mk_FindSubseqOverlap
    iter_search_subseq_on_stream
    iter_search_subseq_on_seq



    failure_func
    make_failure_map_for_find_subseq

    find_subseq_overlap
    find_subseq_nonoverlap
    find_subseq
    iter_find
    find
    iter_find_if
    find_if
    seq_index
    seq_find
    seq_index_if
'''.split()
from ..types.to_container import to_tuple

from collections.abc import Sequence


def mk_last_succ_pos2restart_pos__from_seq(seq):
    last_pos2len_longest_proper_bifix = mk_last_pos2len_longest_proper_bifix(seq)
    last_succ_pos2restart_pos = mk_last_succ_pos2restart_pos(last_pos2len_longest_proper_bifix)
    return last_succ_pos2restart_pos
def mk_last_succ_pos2restart_pos(last_pos2len_longest_proper_bifix):
    r'''last_pos2len_longest_proper_bifix -> last_succ_pos2restart_pos
    last_pos2len_longest_proper_bifix:
        see: mk_last_pos2len_longest_proper_bifix
    last_succ_pos2restart_pos:
        curr_pos match fail, i.e. subseq[:curr_pos] != seq[i:i+curr_pos]
        last_succ_pos, i.e. subseq[:last_succ_pos] == seq[i:i+last_succ_pos]
        sz = len(last_pos2len_longest_proper_bifix)
        1 <= curr_pos == last_succ_pos +1 <= sz
        0 <= last_succ_pos < sz
        next round match-try's curr_pos := restart_pos


    #'''
    assert all(0 <= L <= last_pos for last_pos, L in enumerate(last_pos2len_longest_proper_bifix))

    sz = len(last_pos2len_longest_proper_bifix)
    last_succ_pos2restart_pos = []
    it = iter(range(sz))
    for last_succ_pos in it:
        restart_pos = 0
        last_succ_pos2restart_pos.append(restart_pos)
        break
    for last_succ_pos in it:
        curr_pos = last_succ_pos+1
        len_last_succ_bifix = last_pos2len_longest_proper_bifix[last_succ_pos]
        assert 0 <= len_last_succ_bifix <= last_succ_pos
        if curr_pos != sz:
            len_curr_succ_bifix = last_pos2len_longest_proper_bifix[curr_pos]
            assert 0 <= len_curr_succ_bifix <= curr_pos
            if len_curr_succ_bifix == 1+len_last_succ_bifix and len_last_succ_bifix != 0:
                mid_restart_pos = len_last_succ_bifix
                mid_restart_last_pos = mid_restart_pos -1
                restart_pos = last_succ_pos2restart_pos[mid_restart_last_pos]
                assert 0 <= restart_pos <= mid_restart_last_pos < len_last_succ_bifix
            else:
                restart_pos = len_last_succ_bifix
        else:
            restart_pos = len_last_succ_bifix
        assert 0 <= restart_pos <= len_last_succ_bifix <= last_succ_pos
        last_succ_pos2restart_pos.append(restart_pos)
    assert len(last_succ_pos2restart_pos) == sz
    assert all(0 <= restart_pos <= last_succ_pos for last_succ_pos, restart_pos in enumerate(last_succ_pos2restart_pos))
    return last_succ_pos2restart_pos

def mk_last_pos2len_longest_proper_bifix(seq):
    r''':: seq -> last_pos2len_longest_proper_bifix
    last_pos2len_longest_proper_bifix[] :: last_pos -> len_of_longest_proper_bifix

    sz == len(seq) == len(last_pos2len_longest_proper_bifix)

    for _sz <- [1..sz]:
        _seq == seq[:_sz]
        _sz == len(_seq)
        end_pos == _sz
        if _sz > 0:
            last_pos == end_pos-1 == _sz-1
        bifix ::= prefix&&suffix
        proper ==>> len(bifix) < _sz
        L == len(bifix)
        _seq[:L] == bifix == _seq[_sz-L:_sz]
    #'''
    sz = len(seq)
    last_pos2len_longest_proper_bifix = []
    it = iter(range(sz))
    for last_pos in it:
        len_of_longest_proper_bifix = 0
        last_pos2len_longest_proper_bifix.append(len_of_longest_proper_bifix)
        break
    for last_pos in it:
        assert 0 <= len_of_longest_proper_bifix <= last_pos == len(last_pos2len_longest_proper_bifix) < sz
        x = seq[last_pos]
        while True:
            y = seq[len_of_longest_proper_bifix]
            if x == y:
                len_of_longest_proper_bifix += 1
                break
            if len_of_longest_proper_bifix == 0:
                break
            len_of_longest_proper_bifix = last_pos2len_longest_proper_bifix[len_of_longest_proper_bifix-1]
        last_pos2len_longest_proper_bifix.append(len_of_longest_proper_bifix)
    assert len(last_pos2len_longest_proper_bifix) == sz
    assert all(0 <= L <= last_pos for last_pos, L in enumerate(last_pos2len_longest_proper_bifix))
    #assert all(seq[:L] == seq[last_pos+1-L:last_pos+1] for last_pos in range(sz) for L in {last_pos2len_longest_proper_bifix[last_pos]})
    return last_pos2len_longest_proper_bifix





def failure_func(seq, begin=None, end=None):
    r""":: seq -> end_pos2len_longest_proper_bifix
    fail_pos2restart_pos == end_pos2len_longest_proper_bifix
    len(end_pos2len_longest_proper_bifix) == len(seq)
    end_pos, len_longest_proper_bifix:
        see: mk_last_pos2len_longest_proper_bifix
    restart_pos:
        see: mk_last_succ_pos2restart_pos
    #"""
##    if not isinstance(seq, Sequence):
##        raise TypeError('not isinstance(subseq, Sequence)')
    begin, end, _ = slice(begin, end).indices(len(seq))
    if begin >= end:
        return []
    assert 0 <= begin < end <= len(seq)

    fail_pos2restart_pos = end_pos2len_longest_proper_bifix = [-1]
    L = 0
    for i in range(begin+1, end):
        assert L < len(seq)
        fail_pos2restart_pos.append(L)
        #seq[-1] is useless, since the result was discard
        while L >= 0:
            # assert seq[begin:begin+L] == seq[i-L:i]
            if seq[begin+L] == seq[i]:
                # assert seq[begin:begin+L+1] == seq[i-L:i+1]
                L += 1
                # assert seq[begin:begin+L] == seq[i+1-L:i+1]
                break
            else:
                L = fail_pos2restart_pos[L]
        else:
            assert L == -1
            L = 0

    assert all(L < i for i, L in enumerate(fail_pos2restart_pos))
    assert len(fail_pos2restart_pos) == len(seq)
    return fail_pos2restart_pos

assert failure_func('0123012012012') == [-1, 0, 0, 0, 0, 1, 2, 3, 1, 2, 3, 1, 2]

def make_failure_map_for_find_subseq(subseq):
    r'''subseq -> end_pos2len_longest_proper_bifix_ex
    failure_map == end_pos2len_longest_proper_bifix_ex
        == [-1]+last_pos2len_longest_proper_bifix

    end_pos, len_of_longest_proper_bifix, last_pos2len_longest_proper_bifix:
        see: mk_last_pos2len_longest_proper_bifix

    #'''
    #bug:return failure_func(subseq)
    #bug: failure_map = end_pos2len_longest_proper_bifix_ex = failure_func(subseq + subseq[:1])
    #       subseq may empty
    failure_map = failure_func(subseq + subseq[:1] or '1')
        #last appended value can be any thing comparable!
    assert len(failure_map) == 1+len(subseq)
    assert failure_map == [-1, *mk_last_pos2len_longest_proper_bifix(subseq)]
    return failure_map

def _check(subseq, *, failure_map_or_last_pos2restart_pos, _ver_is_1):
    if not isinstance(subseq, Sequence):
        raise TypeError('not isinstance(subseq, Sequence)')
    if not isinstance(failure_map_or_last_pos2restart_pos, Sequence):
        raise TypeError('not isinstance(failure_map_or_last_pos2restart_pos, Sequence)')
    if _ver_is_1:
        failure_map = failure_map_or_last_pos2restart_pos
        if len(failure_map) != len(subseq)+1: raise ValueError
        if failure_map[0] != -1: raise ValueError
        if len(failure_map)>1 and failure_map[1] != 0: raise ValueError
    else:
        last_pos2restart_pos = failure_map_or_last_pos2restart_pos
        if len(last_pos2restart_pos) != len(subseq): raise ValueError
        if last_pos2restart_pos and last_pos2restart_pos[0] != 0: raise ValueError

class FindSubseqOverlap:
    r'''
    last_pos2restart_pos
        = last_pos2len_longest_proper_bifix
        | last_succ_pos2restart_pos
        #
        see:
            mk_last_pos2len_longest_proper_bifix
            mk_last_succ_pos2restart_pos
    offset:
        offset of subseq
      subseq[:offset] == prev_input[sz-offset:sz]
    #'''
    def __init__(sf, subseq, *, last_pos2restart_pos, offset):
        _check(subseq, failure_map_or_last_pos2restart_pos=last_pos2restart_pos, _ver_is_1=False)
        if not 0 <= offset <= len(last_pos2restart_pos) == len(subseq): raise ValueError

        sf.offset = offset
        sf.last_pos2restart_pos = last_pos2restart_pos
        sf.subseq = subseq
    def is_begin(sf):
        return sf.offset == 0
    def is_end(sf):
        return sf.offset == len(sf.last_pos2restart_pos)
    def feed(sf, x):
        sf._feed(x)
        return sf.is_end()
    def _feed(sf, x):
        if not sf.last_pos2restart_pos: return
        if sf.is_end():
            # assume search subseq+[nonchar]
            # 1. must fail
            # 2. last_pos2restart_pos[sz] === last_pos2restart_pos[sz-1]
            # 3. last_pos2restart_pos[sz-new_offset:sz] === last_pos2restart_pos[0:new_offset]
            offset = sf.last_pos2restart_pos[-1]
        else:
            offset = sf.offset
        while 1:
            #assert 0 <= new_offset < sz
            #assert last_pos2restart_pos[old_offset-new_offset:old_offset] == last_pos2restart_pos[0:new_offset]
            y = sf.subseq[offset]
            if y == x:
                offset += 1
                break
            end_pos = offset
            if end_pos == 0:
                break
            last_pos = end_pos -1
            offset = restart_pos = sf.last_pos2restart_pos[last_pos]
        else:
            raise logic-error
        sf.offset = offset
    def skip_util_found(sf, iterator):
        it = iter(iterator)
        assert it is iterator
        for x in it:
            if sf.feed(x):
                break
        return it
    def search_on_seq(sf, seq, begin=None, end=None, *, overlap):
        begin, end, _ = slice(begin, end).indices(len(seq))
        if not sf.last_pos2restart_pos:
            #bug: return range(begin, end+1)
            #   not iterator
            return iter(range(begin, end+1))
        return sf._search_on_seq(seq, begin, end, overlap=overlap)
    def _search_on_seq(sf, seq, begin, end, *, overlap):
        assert sf.last_pos2restart_pos
        not_overlap = not overlap
        sz = len(sf.subseq)
        if not_overlap:
            prev_end = 0
        for i in range(begin, end):
            if sf.feed(seq[i]):
                end = i+1
                begin = end-sz
                if not_overlap and begin < prev_end:
                    #skip
                    #not update prev_end
                    pass
                else:
                    yield begin
                    prev_end = end
    def search_on_stream(sf, istream, *, overlap):
        r'''istream -> iter location

        istream:
            tell :: () -> location
            seek :: location -> ()
            read :: uint -> [a]
                empty => eof
        #'''
        not_overlap = not overlap
        sz = len(sf.subseq)
        location = istream.tell()
        if sz == 0:
            b = 1
            while b:
                yield location
                bs = istream.read(1)
                b = bool(bs)
                location = istream.tell()
            return
        ###
        Nothing = object()
        old2new_sz = Nothing
        old = Nothing
        new = location
        if not_overlap:
            prev_found_end_idx = 0
            new_location_idx = 0
            def to_skip(i):
                nonlocal prev_found_end_idx
                curr_found_end_idx = new_location_idx +i+1
                curr_found_begin_idx = curr_found_end_idx -sz
                skip = curr_found_begin_idx < prev_found_end_idx
                if not skip:
                    prev_found_end_idx = curr_found_end_idx
                return skip
        else:
            def to_skip(i):
                return False
        while 1:
            for i in range(sz):
                bs = istream.read(1)
                if not bs:
                    return
                [x] = bs
                if sf.feed(x):
                    #found => rollback
                    if to_skip(i):
                        continue
                    if i == sz -1:
                        yield new
                    else:
                        assert old is not Nothing
                        curr = istream.tell()
                        end = old2new_sz+i+1
                        begin = end-sz
                        assert 0 < begin < old2new_sz

                        istream.seek(old)
                        istream.read(begin)
                        found = istream.tell()
                        yield found
                        old = found
                        old2new_sz -= begin
                        istream.seek(curr)

            else:
                old = new
                old2new_sz = sz
                new = istream.tell()
                if not_overlap:
                    #not update:prev_found_end_idx
                    new_location_idx += sz



def mk_FindSubseqOverlap(subseq, *, last_pos2restart_pos=None, _ver=None, offset=0):
    r''' :: subseq -> FindSubseqOverlap
    #'''
    finder = _mk_FindSubseqOverlap(subseq, last_pos2restart_pos=last_pos2restart_pos, _ver=_ver, offset=offset)
    return finder

def _mk_FindSubseqOverlap(subseq, *, last_pos2restart_pos, _ver, offset):
    if _ver is None:
        _ver = 3
    if _ver not in [2,3]: raise ValueError
    if _ver == 2:
        mk = mk_last_pos2len_longest_proper_bifix
    elif _ver == 3:
        mk = mk_last_succ_pos2restart_pos__from_seq
    else:
        raise ValueError

    if last_pos2restart_pos is None:
        last_pos2restart_pos = mk(subseq)

    _check(subseq, failure_map_or_last_pos2restart_pos=last_pos2restart_pos, _ver_is_1=False)
    finder = FindSubseqOverlap(subseq, last_pos2restart_pos=last_pos2restart_pos, offset=offset)
    return finder

def iter_search_subseq_on_stream(istream, subseq, *, overlap:bool, last_pos2restart_pos=None, _ver=None, offset=0):
    r''' :: istream -> subseq -> Iter location

    istream:
        see: FindSubseqOverlap.search_on_stream
    #'''
    finder = _mk_FindSubseqOverlap(subseq, last_pos2restart_pos=last_pos2restart_pos, _ver=_ver, offset=offset)
    it = finder.search_on_stream(istream, overlap=overlap)
    assert it is iter(it)
    return it

def iter_search_subseq_on_seq(seq, subseq, *, overlap:bool, last_pos2restart_pos=None, _ver=None, offset=0):
    r''' :: seq -> subseq -> Iter idx
    #'''
    finder = _mk_FindSubseqOverlap(subseq, last_pos2restart_pos=last_pos2restart_pos, _ver=_ver, offset=offset)
    it = finder.search_on_seq(seq, overlap=overlap)
    assert it is iter(it)
    return it



def _ver2_ver3_find_subseq_overlap(seq, subseq, begin, end, last_pos2restart_pos):
    return FindSubseqOverlap(subseq, last_pos2restart_pos=last_pos2restart_pos, offset=0).search_on_seq(seq, begin, end, overlap=True)



def find_subseq_overlap(seq, subseq, begin=None, end=None, failure_map_or_last_pos2restart_pos=None, *, _ver=None):
    '''start for start in range(begin, end+1) if seq[start:start+len(subseq)] == subseq

if _ver==1:
    failure_map = failure_func(subseq + subseq[:1] or '1')
        == make_failure_map_for_find_subseq(subseq)
    len(failure_map) == len(subseq)+1

if _ver in {2,3}:
    len(last_pos2restart_pos) == len(subseq)
        see:FindSubseqOverlap
'''
    return _find_subseq_overlap(seq, subseq, begin, end, failure_map_or_last_pos2restart_pos, _ver=_ver)
def _find_subseq_overlap(seq, subseq, begin, end, may_failure_map_or_last_pos2restart_pos, *, _ver):
    if _ver is None:
        _ver = 3
    if _ver not in [1,2,3]: raise ValueError
    if not isinstance(subseq, Sequence):
        raise TypeError('not isinstance(subseq, Sequence)')
    if may_failure_map_or_last_pos2restart_pos is not None and len(may_failure_map_or_last_pos2restart_pos) != len(subseq) + (_ver==1):
        raise ValueError('len(failure_map_or_last_pos2restart_pos) != len(subseq) + (_ver==1)')

    if _ver == 1:
        f = _ver1_find_subseq_overlap
        mk = make_failure_map_for_find_subseq
    elif _ver == 2:
        f = _ver2_ver3_find_subseq_overlap
        mk = mk_last_pos2len_longest_proper_bifix
    elif _ver == 3:
        f = _ver2_ver3_find_subseq_overlap
        mk = mk_last_succ_pos2restart_pos__from_seq
    else:
        raise ValueError

    if may_failure_map_or_last_pos2restart_pos is None:
        failure_map_or_last_pos2restart_pos = mk(subseq)
    else:
        failure_map_or_last_pos2restart_pos = may_failure_map_or_last_pos2restart_pos

    _check(subseq, failure_map_or_last_pos2restart_pos=failure_map_or_last_pos2restart_pos, _ver_is_1=(_ver==1))
    it = f(seq, subseq, begin, end, failure_map_or_last_pos2restart_pos)
    assert it is iter(it)
    return it

def _ver1_find_subseq_overlap(seq, subseq, begin, end, failure_map):
    begin, end, _ = slice(begin, end).indices(len(seq))

    subL = len(subseq)
    if subL == 0:
        yield from range(begin, end+1)
        return

    failure_map = failure_map
    #failure_map = failure_func(subseq + subseq[:1] or '1')
    #failure_map = failure_func(subseq)
    #print(subseq, failure_map)

    i = begin
    j = 0
    while i < end:
        assert j >= 0
        #print((i,j))

        if j == subL:
            # match
            r = i-j
            assert begin <= r < end
            yield r
        elif seq[i] == subseq[j]:
            i += 1
            j += 1
            continue

        new_j = failure_map[j]
        assert new_j < j
        if new_j < 0:
            # fail
            i += 1
            j = 0
        else:
            # try other start (= i-j)
            j = new_j
    else:
        if j == subL:
            # match
            r = i-j
            assert begin <= r < end
            yield r

def find_subseq_nonoverlap(seq, subseq, begin=None, end=None, failure_map=None, _ver=None):
    L = len(subseq)
    j = -L
    for i in _find_subseq_overlap(seq, subseq, begin, end, failure_map, _ver=_ver):
        if i >= j + L:
            yield i
            j = i

def find_subseq(seq, subseq, begin=None, end=None, failure_map=None, _ver=None):
    for i in _find_subseq_overlap(seq, subseq, begin, end, failure_map, _ver=_ver):
        return i
    return -1

    if j == subL:
        r = i - j
        assert 0 <= begin <= r <= i <= end <= len(seq)
        assert to_tuple(seq[r:r+subL]) == to_tuple(subseq)
        return r
    assert i == end and j < subL
    return -1


def _t0():
    for _ver in [1,2,3]:
        assert find_subseq('a', '', _ver=_ver) == 0
        assert find_subseq('', 'a', _ver=_ver) == -1
        assert find_subseq('a', 'a', _ver=_ver) == 0
        assert find_subseq('ababcabc', 'abc', _ver=_ver) == 2
        assert find_subseq('abcadabcab', 'abcab', _ver=_ver) == 5
        assert_eq([*find_subseq_overlap('abcadabcabcabcab', 'abcab', _ver=_ver)], [5, 8, 11], _ver=_ver)
        assert [*find_subseq_nonoverlap('abcadabcabcabcab', 'abcab', _ver=_ver)] == [5, 11]
        assert [*find_subseq_overlap('abaabaabaaba', 'abaab', _ver=_ver)] == [0, 3, 6]
    for _ver in [2,3]:
        iter_search_subseq_on_seq
        iter_search_subseq_on_stream
def _iter_ans(seq:bytes, subseq, *, overlap):
    i = 0
    step = 1 if overlap else (len(subseq) or 1)
    assert step
    while 1:
        i = seq.find(subseq, i)
        if i < 0: return
        yield i
        i += step
def _gen_data_sz4(seq_len, subseq_len, alphabet_size, *, overlap):
    pairs = _gen_data_sz2(seq_len, subseq_len, alphabet_size)
    for seq, subseq in pairs:
        ans = [*_iter_ans(seq, subseq, overlap=overlap)]
        yield seq, subseq, ans, overlap

def _gen_data_sz2(seq_len, subseq_len, alphabet_size):
    assert 1 <= alphabet_size < 2**8
    n = seq_len + subseq_len
    it = itertools.product(range(alphabet_size), repeat=n)
    for ls in it:
        bs = bytes(ls)
        seq, subseq = bs[:seq_len], bs[seq_len:]
        assert len(seq) == seq_len
        assert len(subseq) == subseq_len
        yield seq, subseq
def _t_seq(overlap):
    if overlap:
        f1 = find_subseq_overlap
    else:
        f1 = find_subseq_nonoverlap
    f2 = iter_search_subseq_on_seq
    gs = [
        G(f1, _ver=[1,2,3])
        ,G(f2, _ver=[2,3], overlap=[overlap])
        ]
    def seq2xxx(seq):
        return seq
    def reset_xxx(xxx):
        pass
    return seq2xxx, reset_xxx, gs


def _t_stream(overlap):
    f3 = iter_search_subseq_on_stream
    gs = [
        G(f3, _ver=[2,3], overlap=[overlap])
        ]
    def seq2xxx(seq):
        return io.BytesIO(seq)
    def reset_xxx(xxx):
        xxx.seek(0)
    return seq2xxx, reset_xxx, gs
def _t():
    _t0()
    ls3 = [
        (0,0,1)
        ,(0,1,2)
        ,(1,0,2)
        ,(1,1,3)
        ,(2,1,3)
        ,(1,2,3)
        ,(2,2,3)
        ,(3,2,3)
        ,(4,2,3)
        ,(5,2,3)
        ,(3,3,3)
        ,(4,3,3)
        ,(5,3,3)
        ,(6,3,3)
        ,(7,3,3)
        ]
    for overlap in [0,1]:
        s2x_gs_ls = [
            _t_seq(overlap)
            ,_t_stream(overlap)
            ]
        for (seq_len, subseq_len, alphabet_size) in ls3:
            it4 = _gen_data_sz4(seq_len, subseq_len, alphabet_size, overlap=overlap)
            for (seq, subseq, ans, overlap) in it4:
                for seq2xxx, reset_xxx, gs in s2x_gs_ls:
                    _t_sl(seq, subseq, ans, overlap, seq2xxx, reset_xxx, gs)
def _t_sl(seq, subseq, ans, overlap, seq2xxx, reset_xxx, gs):
    xxx = seq2xxx(seq)
    for g in gs:
        [f] = g.args
        keys = [*g.kwargs.keys()]
        valuess = [g.kwargs[k] for k in keys]
        it = itertools.product(*valuess)
        for vs in it:
            reset_xxx(xxx)
            kws = dict(zip(keys, vs))
            #print(seq, xxx)
            r = f(xxx, subseq, **kws)
            assert iter(r) is r
            r = [*r]
            assert_eq(r, ans, seq=seq, subseq=subseq, overlap=overlap, kws=kws, f=f)
if __name__ == "__main__":
    import itertools
    import io
    from seed.tiny import assert_eq
    from seed.helper.get_args_kwargs import mk_GetArgsKwargs as G, xcall
    _t()




























def iter_find(seq, x, begin=None, end=None):
    return iter_find_if(seq, lambda e: e==x, begin, end)

def iter_find_if(seq, pred, begin=None, end=None):
    begin, end, _ = slice(begin, end).indices(len(seq))
    for i in range(begin, end):
        if pred(seq[i]):
            yield i

def find_if(seq, pred, begin=None, end=None):
    for i in iter_find_if(seq, pred, begin, end):
        return i
    return -1

def find(seq, x, begin=None, end=None):
    return find_if(seq, lambda e: e==x, begin, end)

def seq_index_if(seq, pred, begin=None, end=None):
    i = find_if(seq, pred, begin, end)
    if i < 0:
        raise ValueError('seq.index_if(pred) : not found')
    return i

def seq_index(seq, x, begin=None, end=None):
    i = find(seq, x, begin, end)
    if i < 0:
        raise ValueError('seq.index(x) : not found')
    return i

seq_find = find


##def find(ls, v, *args):
##    try:
##        i = ls.index(v, *args)
##        return i
##    except ValueError:
##        return -1
