

__all__ = '''
    failure_func
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


def failure_func(seq, begin=None, end=None):
##    if not isinstance(seq, Sequence):
##        raise TypeError('not isinstance(subseq, Sequence)')
    begin, end, _ = slice(begin, end).indices(len(seq))
    if begin >= end:
        return []
    assert 0 <= begin < end <= len(seq)
    
    fail_pos2restart_pos = [-1]
    L = 0
    for i in range(begin+1, end):
        assert L < len(seq)
        fail_pos2restart_pos.append(L)
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
    return fail_pos2restart_pos

assert failure_func('0123012012012') == [-1, 0, 0, 0, 0, 1, 2, 3, 1, 2, 3, 1, 2]
        
def make_failure_map_for_find_subseq(subseq):
    return failure_func(subseq + subseq[:1])
def find_subseq_overlap(seq, subseq, begin=None, end=None, failure_map=None):
    '''start for start in range(begin, end+1) if seq[start:start+len(sub)] == sub

failure_map = failure_func(subseq + subseq[:1])
    == make_failure_map_for_find_subseq(subseq)
len(failure_map) == len(sub)+1
'''
    if not isinstance(subseq, Sequence):
        raise TypeError('not isinstance(subseq, Sequence)')
    if failure_map is not None and len(failure_map) <= len(subseq):
        return ValueError('len(failure_map) <= len(subseq)')
    
    begin, end, _ = slice(begin, end).indices(len(seq))

    subL = len(subseq)
    if subL == 0:
        yield from range(begin, end+1)
        return
    
    fail_pos2restart_pos = (failure_map if failure_map is not None else
                            make_failure_map_for_find_subseq(subseq))
    #print(subseq, fail_pos2restart_pos)
    
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

        new_j = fail_pos2restart_pos[j]
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

def find_subseq_nonoverlap(seq, subseq, begin=None, end=None, failure_map=None):
    L = len(subseq)
    j = -L
    for i in find_subseq_overlap(seq, subseq, begin, end, failure_map):
        if i >= j + L:
            yield i
            j = i

def find_subseq(seq, subseq, begin=None, end=None, failure_map=None):
    for i in find_subseq_overlap(seq, subseq, begin, end, failure_map):
        return i
    return -1

    if j == subL:
        r = i - j
        assert 0 <= begin <= r <= i <= end <= len(seq)
        assert to_tuple(seq[r:r+subL]) == to_tuple(subseq)
        return r
    assert i == end and j < subL
    return -1

assert find_subseq('a', '') == 0
assert find_subseq('', 'a') == -1
assert find_subseq('a', 'a') == 0
assert find_subseq('ababcabc', 'abc') == 2
assert find_subseq('abcadabcab', 'abcab') == 5

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
