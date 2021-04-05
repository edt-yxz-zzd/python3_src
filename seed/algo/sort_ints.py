
'''
e.g. when polynomial implement is [(deg, nonzero_coef)] little-endian by deg
    each time we cover from dict<deg:nonzero_coef> to sorted[(deg,nonzero_coef)]
    we should sort degs i.e. ints.

py_sort or bucket_sort
R = range = min - max
N = total = len(ints)
py_sort = O(N*logN)     # sparse
bucket_sort = O(R + N)  # dense
'''
__all__ = '''
    sort_ints
    sort_seqs_by_key_at
    '''.split()
from seed.iters.minmax import maybe_minmax
#from seed.algo.bucket_sort import bucket_sort
from seed.algo.bucket_sort.bucket_sort__plain import bucket_sort
from seed.special_funcs import identity

def sort_seqs_by_key_at(idx, seqs, *, key=None):
    if key is None:
        return sort_ints(seqs, key=lambda seq: seq[idx])
    return sort_ints(seqs, key=lambda seq: key(seq[idx]))
def sort_ints(ints, *, key=None):
    ints = list(ints)
    # assert all(type(i) is int for i in ints)
    N = len(ints)
    if N < 2:
        return ints
    _key = identity if key is None else key
    min, max = maybe_minmax(ints, key=key)
    minN, maxN = _key(min), _key(max)
    R = maxN - minN
    assert R >= 0
    py_sortC = N*N.bit_length()
    bucket_sortC = R+N
    if py_sortC < bucket_sortC:
        #rint('py_sortC')
        ints.sort(key=key)
    else:
        #rint('bucket_sort')
        #for i in range(N): ints[i] -= min
        if minN != 0:
            def _key_(x):
                return _key(x)-minN
        else:
            _key_ = key
        ints = bucket_sort(R+1, ints, key=_key_)
        #for i in range(N): ints[i] += min
    return ints

assert sort_ints(()) == []
assert sort_ints((1,)) == [1]
#rint('no print')
# 'bucket_sort'
assert sort_ints(list(range(200, 1000))+list(range(100,200))) == list(range(100,1000))
#rint('printed: bucket_sort')
# 'py_sort'
assert sort_ints([1000, 0, 100000]) == [0, 1000, 100000]
#rint('printed: py_sort')

