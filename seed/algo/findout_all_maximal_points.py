#__all__:goto
r'''[[[
e ../../python3_src/seed/algo/findout_all_maximal_points.py
[[[
view others/数学/找出偏序的极大点.txt
===
出现过需求:
  from seed.math.load_data.some_smooth_primes import SmoothPrime__base_2_3_5__lt_3317044064679887385962123 #.smooth_primes__sorted, .prime_bases, .smooth_prime__cofactorization__pairs____sorted, .maxpp
    def _find_max_exps_(prime_bases, prime__cofactorization__pairs, /):



识别出 极大元素
    O(N**2)*partial_cmp

    元组特例:tuple<L, total_ordering>
      partial_cmp == O(L)*total_cmp
      O(L*N**2)*total_cmp

    输出规模是O(N)
    假如输出规模是O(M)
      校验输出正确性 或者 校验证书，只怕也要O(M**2)*partial_cmp时间
      有些被覆盖，这部分校验，只需O(N-M)*partial_cmp
      核心部分O(M**2)*partial_cmp
        但 元组特例:只需O(M**2)*total_cmp
          而非O(L*M**2)*total_cmp

[xs :: [tuple<L>]]:
    [[xs[i] is max] =[def]= [@j. [@k. [xs[i].k <= xs[j].k]] -> [xs[i] == xs[j]]]]
    [[@i,j. [i=!=j] -> [xs[i] =!= xs[j]]] -> [[xs[i] is max] <-> [@j. [i=!=j] -> [?k. [xs[i].k > xs[j].k]]]]]


]]]



seed.algo.findout_all_maximal_points
py -m nn_ns.app.debug_cmd   seed.algo.findout_all_maximal_points -x
py -m nn_ns.app.doctest_cmd seed.algo.findout_all_maximal_points:__doc__ -ff -v
py_adhoc_call   seed.algo.findout_all_maximal_points   @f




>>> from seed.algo.partial_cmp import partial_cmp4array__py_ord

def findout_all_maximal_points__partial_cmp__O_NNcmp_(partial_cmp, iterable, /, *, key=None, group=False):
>>> fP = findout_all_maximal_points__partial_cmp__O_NNcmp_
>>> fP(partial_cmp4array__py_ord, [])
[]
>>> fP(partial_cmp4array__py_ord, [(1,1,-1), (1,-1,1), (-1,1,1), (0,0,0)])
[(1, 1, -1), (1, -1, 1), (-1, 1, 1), (0, 0, 0)]
>>> fP(partial_cmp4array__py_ord, [(1,1,-1), (1,-1,1), (-1,1,1), (1,1,0)])
[(1, -1, 1), (-1, 1, 1), (1, 1, 0)]
>>> fP(partial_cmp4array__py_ord, [(1,1,-1), (1,-1,1), (-1,1,1), (1,1,1)])
[(1, 1, 1)]
>>> fP(partial_cmp4array__py_ord, [(1,1,-1), (1,-1,1), (-1,1,1), (0,0,0)], group=True)
[((1, 1, -1), [(0, (1, 1, -1))]), ((1, -1, 1), [(1, (1, -1, 1))]), ((-1, 1, 1), [(2, (-1, 1, 1))]), ((0, 0, 0), [(3, (0, 0, 0))])]
>>> fP(partial_cmp4array__py_ord, [(1,1,-1), (0,0,0), (1,-1,1), (-1,1,1), (0,0,0)], keep_order=True)
[(1, 1, -1), (0, 0, 0), (1, -1, 1), (-1, 1, 1), (0, 0, 0)]
>>> fP(partial_cmp4array__py_ord, [(1,1,-1), (0,0,0), (1,-1,1), (-1,1,1), (0,0,0)])
[(1, 1, -1), (0, 0, 0), (0, 0, 0), (1, -1, 1), (-1, 1, 1)]


def findout_all_maximal_points__L_tuples__O_LNlogNcmp_plus_LNNuintop_(L, tuple_seq, /, *, key=None, __getitem__=None, using_bucket_sort=False):
>>> fT = findout_all_maximal_points__L_tuples__O_LNlogNcmp_plus_LNNuintop_
>>> fT(0, [])
[]
>>> fT(0, [1,2,3,4])
[1, 2, 3, 4]
>>> fT(5, [])
[]
>>> fT(3, [(1,1,-1), (1,-1,1), (-1,1,1), (0,0,0)])
[(-1, 1, 1), (0, 0, 0), (1, -1, 1), (1, 1, -1)]
>>> fT(3, [(1,1,-1), (1,-1,1), (-1,1,1), (1,1,0)])
[(-1, 1, 1), (1, -1, 1), (1, 1, 0)]
>>> fT(3, [(1,1,-1), (1,-1,1), (-1,1,1), (1,1,1)])
[(1, 1, 1)]
>>> fT(3, [(1,1,-1), (1,-1,1), (-1,1,1), (0,0,0)], using_bucket_sort=True)
[(-1, 1, 1), (0, 0, 0), (1, -1, 1), (1, 1, -1)]
>>> fT(3, [(1,1,-1), (0, 0, 0), (1,-1,1), (-1,1,1), (0,0,0)], using_bucket_sort=True)
[(-1, 1, 1), (0, 0, 0), (0, 0, 0), (1, -1, 1), (1, 1, -1)]
>>> fT(3, [(1,1,-1), (0, 0, 0), (1,-1,1), (-1,1,1), (0,0,0)], using_bucket_sort=True, keep_order=True)
[(1, 1, -1), (0, 0, 0), (1, -1, 1), (-1, 1, 1), (0, 0, 0)]
>>> fT(3, [(1,1,-1), (0,0,0), (1,-1,1), (-1,1,1), (0,0,0)], keep_order=True)
[(1, 1, -1), (0, 0, 0), (1, -1, 1), (-1, 1, 1), (0, 0, 0)]
>>> fT(3, [(1,1,-1), (0,0,0), (1,-1,1), (-1,1,1), (0,0,0)])
[(-1, 1, 1), (0, 0, 0), (0, 0, 0), (1, -1, 1), (1, 1, -1)]




#]]]'''
__all__ = r'''
findout_all_maximal_points__partial_cmp__O_NNcmp_
    findout_all_maximal_points__L_tuples__O_LNlogNcmp_plus_LNNuintop_


'''.split()#'''
__all__


from operator import __getitem__
import operator


from seed.tiny_.check import check_int_ge
from seed.tiny import echo, fst
from seed.seq_tools.remove_strict_sorted_indices import remove_strict_sorted_indices__emplace_

from seed.algo.bucket_sort.bucket_sort__plain import bucket_sort__plain
#def bucket_sort__plain(alphabet_size, iterable, *, key):
#    'may uint -> Iter a -> (key::may (a->uint)) -> [a]'
from seed.algo.bucket_sort.utils4tuples import unique_gs5js_, convert_to_index_keys__L_
from seed.algo.partial_cmp import mk_partial_cmp_result5subresults_

def findout_all_maximal_points__partial_cmp__O_NNcmp_(partial_cmp, iterable, /, *, key=None, group=False, keep_order=False):
    '(k -> k -> (-1|0|+1|...)) -> Iter a -> (key::a->k) -> ([a] if not group else [(k, [a])]) # [[TIME(partial_cmp) ~= O(L)cmp] -> [TIME(findout_all_maximal_points__partial_cmp__O_NNcmp_) ~= O(N**2)*partial_cmp]] #not O(OUT**2)cmp, since middle state may arbitrary big#'
    if key is None:
        key = echo
    max_eqvs_ls = []
        # :: [(k, [(j,a)])]
    for j, rhs in enumerate(iterable):
        rhs_k = key(rhs)
        idc4remove = []
        for i, max_eqvs in enumerate(max_eqvs_ls):
            lhs_k, eqvs = max_eqvs
            r = partial_cmp(lhs_k, rhs_k)
            if r is ...:
                pass
            elif r == -1:
                # [lhs ~<~ rhs]
                # rhs is max
                idc4remove.append(i)
                #continue to find out more non-max
            elif r == +1:
                # [lhs ~>~ rhs]
                # rhs is not max
                assert not idc4remove
                break
            elif r == 0:
                # [lhs ~=~ rhs]
                # rhs is max
                assert not idc4remove
                eqvs.append((j,rhs))
                break
            else:
                raise TypeError(partial_cmp)
        else:
            # rhs is max
            max_eqvs_ls.append((rhs_k, [(j,rhs)]))
            if idc4remove:
                remove_strict_sorted_indices__emplace_(idc4remove, max_eqvs_ls)
    if group:
        return max_eqvs_ls

    pairs = [(j,a) for k, eqvs in max_eqvs_ls for j,a in eqvs]
    if keep_order:
        pairs = sorted(pairs, key=fst)
    return [a for j,a in pairs]

def findout_all_maximal_points__L_tuples__O_LNlogNcmp_plus_LNNuintop_(L, tuple_seq, /, *, key=None, __getitem__=None, using_bucket_sort=False, keep_order=False):
    'Ord k => [a] -> (key::a->ks/tuple<L;k>) -> (__getitem__::ks->i/int%L->k) -> [a] # [TIME(findout_all_maximal_points__L_tuples__O_LNlogNcmp_plus_LNNuintop_) ~= O(L*N*log2(N))*total_cmp + O(L*N**2)*uint_op]'
    check_int_ge(0, L)
    len(tuple_seq)
    tuple_seq[:0]
    N = len(tuple_seq)


    if key is None:
        key = echo
    if __getitem__ is None:
        __getitem__ = operator.__getitem__

    j2key = [*map(key, tuple_seq)]
    (i2j2ik, i2js__sorted, i2num_iks, i2ik2old_k, i2ik2js) = convert_to_index_keys__L_(L, __getitem__, j2key, using_bucket_sort=using_bucket_sort)

    j2g, g2js = unique_gs5js_(N, i2num_iks, i2j2ik)



    def partial_cmp(lhs_g, rhs_g, /):
        lhs_j = g2js[lhs_g][0]
        rhs_j = g2js[rhs_g][0]
        return mk_partial_cmp_result5subresults_(j2ik[lhs_j] - j2ik[rhs_j] for j2ik in i2j2ik)

    gs = range(len(g2js))

    max_gs = findout_all_maximal_points__partial_cmp__O_NNcmp_(partial_cmp, gs)
    max_js = [j for g in max_gs for j in g2js[g]]

    if keep_order:
        max_js = bucket_sort__plain(N, max_js, key=None)
    return [tuple_seq[j] for j in max_js]



__all__


from seed.algo.partial_cmp import partial_cmp4array__py_ord
from seed.algo.findout_all_maximal_points import findout_all_maximal_points__partial_cmp__O_NNcmp_, findout_all_maximal_points__L_tuples__O_LNlogNcmp_plus_LNNuintop_
from seed.algo.findout_all_maximal_points import *
