#__all__:goto
r'''[[[
e ../../python3_src/seed/algo/bucket_sort/utils4tuples.py
view ../../python3_src/seed/algo/findout_all_maximal_points.py



seed.algo.bucket_sort.utils4tuples
py -m nn_ns.app.debug_cmd   seed.algo.bucket_sort.utils4tuples -x
py -m nn_ns.app.doctest_cmd seed.algo.bucket_sort.utils4tuples:__doc__ -ff -v
py_adhoc_call   seed.algo.bucket_sort.utils4tuples   @f
#]]]'''
__all__ = r'''
    unique_gs5js_
    convert_to_index_keys__L_
        convert_to_index_keys__i_
            convert_to_index_keys_

'''.split()#'''
__all__


from seed.iters.group_by import group_by

from seed.algo.bucket_sort.compress import compress
# def compress(array, min_old_key, max_old_key, *, key=None, with_element=False):
    # :: (a->OldKey) -> [a] -> (new_alphabet_size, [NewKey])
    # where OldKey = UInt = NewKey

from seed.algo.bucket_sort.bucket_sort__plain import bucket_sort__plain
#def bucket_sort__plain(alphabet_size, iterable, *, key):
#    'may uint -> Iter a -> (key::may (a->uint)) -> [a]'


def unique_gs5js_(N, i2num_iks, i2j2ik, /):
    L = len(i2j2ik)
    #N = len(i2j2ik[0]) if L else 0
    #begin:unique j-->g
    L, N, i2num_iks, i2j2ik
    _js = range(N)
    for i in reversed(range(L)):
        _js = bucket_sort__plain(i2num_iks[i], _js, key=i2j2ik[i].__getitem__)
    js__sorted = _js

    N, js__sorted, i2j2ik
    iks_js_pairs = group_by(js__sorted, key=lambda j:tuple(j2ik[j] for j2ik in i2j2ik))
    j2g = [None]*N
    g2js = []
    for iks, js4g in iks_js_pairs:
        g = len(g2js)
        g2js.append(js4g)
        for j in js4g:
            j2g[j] = g
    assert not any(g is None for g in j2g)
    #end:unique j-->g

    j2g = (*j2g,)
    g2js = (*g2js,)
    return j2g, g2js
def convert_to_index_keys__L_(L, __getitem__, j2key, /, *, using_bucket_sort):
    '-> (i2j2ik, i2js__sorted, i2num_iks, i2ik2old_k, i2ik2js)'
    i2j2ik = []
    i2js__sorted = []
    i2num_iks = []
    i2ik2old_k = []
    i2ik2js = []
    for i in range(L):
        (j2ik__at_i, j2k__at_i, js__sorted__at_i, num_iks__at_i, ik2old_k__at_i, ik2js__at_i) = convert_to_index_keys__i_(__getitem__, i, j2key, using_bucket_sort=using_bucket_sort)
        i2j2ik.append(j2ik__at_i)
        i2js__sorted.append(js__sorted__at_i)
        i2num_iks.append(num_iks__at_i)
        i2ik2old_k.append(ik2old_k__at_i)
        i2ik2js.append(ik2js__at_i)
    i2j2ik = (*i2j2ik,)
    i2js__sorted = (*i2js__sorted,)
    i2num_iks = (*i2num_iks,)
    i2ik2old_k = (*i2ik2old_k,)
    i2ik2js = (*i2ik2js,)
    return (i2j2ik, i2js__sorted, i2num_iks, i2ik2old_k, i2ik2js)

def convert_to_index_keys__i_(__getitem__, i, j2key, /, *, using_bucket_sort):
    j2key[:0]
    len(j2key)
    j2k__at_i = tuple(__getitem__(k, i) for k in j2key)
    (j2ik, js__sorted, num_iks, ik2old_k, ik2js) = convert_to_index_keys_(j2k__at_i, using_bucket_sort=using_bucket_sort)
    (j2ik__at_i, js__sorted__at_i, num_iks__at_i, ik2old_k__at_i, ik2js__at_i) = (j2ik, js__sorted, num_iks, ik2old_k, ik2js)
    return (j2ik__at_i, j2k__at_i, js__sorted__at_i, num_iks__at_i, ik2old_k__at_i, ik2js__at_i)
def convert_to_index_keys_(j2k, /, *, using_bucket_sort):
    N = len(j2k)
    js = range(N)
    if not using_bucket_sort:
        js__sorted = sorted(js, key=j2k.__getitem__)
    else:
        min_old_key = min(j2k, default=0)
        max_old_key = max(j2k, default=0)
        num_iks, j2ik = compress(j2k, 0, max_old_key-min_old_key, key=lambda k:k-min_old_key)
        js__sorted = bucket_sort__plain(num_iks, js, key=j2ik.__getitem__)
    js__sorted

    k_js_pairs = group_by(js__sorted, key=j2k.__getitem__)
    # ik ~ index_k
    j2ik = [None]*len(j2k)
    ik2old_k = []
    ik2js = []
    for k, js4k in k_js_pairs:
        ik = len(ik2old_k)
        ik2old_k.append(k)
        ik2js.append(js)
        for j in js4k:
            j2ik[j] = ik
    assert not any(ik is None for ik in j2ik)
    j2ik = tuple(j2ik)
    ik2old_k = tuple(ik2old_k)
    ik2js = tuple(ik2js)
    num_iks = len(ik2old_k)
    return (j2ik, js__sorted, num_iks, ik2old_k, ik2js)




from seed.algo.bucket_sort.utils4tuples import unique_gs5js_, convert_to_index_keys__L_, convert_to_index_keys__i_, convert_to_index_keys_
from seed.algo.bucket_sort.utils4tuples import *
