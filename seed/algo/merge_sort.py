r'''
seed.algo.merge_sort
py -m seed.algo.merge_sort
py -m nn_ns.app.debug_cmd   seed.algo.merge_sort
from seed.algo.merge_sort import merge_sort, merge_sort__stable

e ../../python3_src/seed/algo/merge_sort.py
merge sort:
  结合律？
    重新打括号
    初始 划分极大上升组/下降组
  霍夫曼编码？
  等价于 求 二叉树，最小化 所有 子树的虚拟叶节点数之和
    二叉树的叶节点 的 虚拟叶节点数 即是 升降区长度(这里还有一个 边界归属问题))
  以前:矩阵乘法链 结合律 优化...


>>> merge_sort([])
[]
>>> merge_sort([1])
[1]
>>> merge_sort([1, 2])
[1, 2]
>>> merge_sort([1, 0])
[0, 1]
>>> merge_sort([1, 2, 3])
[1, 2, 3]
>>> merge_sort([1, 0, 2])
[0, 1, 2]
>>> merge_sort([1, 2, 0])
[0, 1, 2]
>>> merge_sort([1, 0, -1])
[-1, 0, 1]

>>> import operator
>>> flip_sub = lambda a,b,/:b-a
>>> merge_sort(['', [3], {}], key=len)
['', {}, [3]]
>>> merge_sort(['', [3], {}], key=len, cmp=flip_sub)
[[3], '', {}]
>>> merge_sort(['', [3], {}], key=len, cmp=flip_sub, reverse=True)
['', {}, [3]]
>>> merge_sort(['', [3], {}], key=len, reverse=True)
[[3], '', {}]


>>> from itertools import permutations, repeat, starmap

for n in range(8):
    us = [*range(n)]
    for xs in permutations(us):
        assert us == merge_sort(xs)
>>> all(us == merge_sort(xs) for n in range(8) for us in [[*range(n)]] for xs in permutations(us))
True


>>> _, num_cmp = merge_sort(repeat(1, 555), to_count_num_cmp=True)
>>> num_cmp
554
>>> merge_sort(chain.from_iterable(starmap(repeat, [(5,111), (2,1111), (1,11), (9,333)])), to_count_num_cmp=True)[-1]
2809

err:
    blocks: 5*111, 2*1111, 1*11, 9*333
    1*11 ++ (5*111) => 11
    1*11 ++ 5*111 ++ (9*333) => 11+111
    1*11 ++ 2*1111 ++ (5*111 ++ 9*333) => 11+1111
    >>> (111+1111+11+333-1)+(11)+(11+111)+(11+1111)
    2820

ok:
    blocks: 5*111, 2*1111, (1*11++9*333)
    1*11 ++ 5*111 ++ (9*333) => 11+111
    1*11 ++ 2*1111 ++ (5*111 ++ 9*333) => 11+1111
    >>> (111+1111+11+333-1)+(11+111)+(11+1111)
    2809

#'''
#################################
#HHHHH
__all__ = '''
    default_cmp
    merge_sort
    merge_sort__stable
    '''.split()

#################################
#HHHHH
___begin_mark_of_excluded_global_names__0___ = ...
from itertools import islice, chain
#import heapq
from seed.tiny import echo
from seed.tiny_.CallCounter import CallCounter
from seed.tiny_.default_cmp import default_cmp
___end_mark_of_excluded_global_names__0___ = ...



def merge_sort(xs, /, *, key=None, cmp=None, reverse=False, **kwds):
    r'''
    Iter a -> (key::a->k) -> (cmp::k->k->int) -> (reverse::bool) -> [a]
    #'''
    return merge_sort__stable(xs, key=key, cmp=cmp, reverse=reverse, **kwds)

def _0_merge_sort__stable():
    def init__ps(key, xs, /):
        ps = [((key(x), i), x) for i, x in enumerate(xs)]
        return ps
    def init__cmp(cmp, reverse, /):
        _cmp = cmp
        if reverse:
            def _cmp_k(a, b, /):
                return -_cmp(a, b)
        else:
            _cmp_k = _cmp
        def cmp_p(ai, bj, /):
            a, i = ai
            b, j = bj
            if i==j: raise logic-err
            r = _cmp_k(a, b)
            if r==0:
                r = i-j
            assert r

            return -1 if r < 0 else +1
        def cmp(ai_x, bj_y, /):
            ai, x = ai_x
            bj, y = bj_y
            return cmp_p(ai, bj)
        return cmp
    #init
    def init__sign_sz_ls(ps, cmp, /):
        assert ps
        it = iter(ps)
        sign_sz_ls = []
        ai_x = next(it)
        sz = 1
        sign = -1
        for bj_y in it:
            prev_sign = sign
            sign = cmp(ai_x, bj_y)
            ai_x = bj_y
            if sign == prev_sign:
                sz += 1
            else:
                if sz == 1:
                    sz = 2
                else:
                    sign_sz_ls.append((prev_sign, sz))
                    sz = 1
        else:
            sign_sz_ls.append((sign, sz))
        L = len(ps)
        assert sum(sz for sign, sz in sign_sz_ls) == L
        assert all(sz for sign, sz in sign_sz_ls)
        return sign_sz_ls

    #merge
    def merge_to(sz2blocks, cmp, lhs, rhs, /):#(ai_x_ls, bj_y_ls, /):
        ls = []
        i = -len(lhs)
        j = -len(rhs)
        while i < 0 and j < 0:
            ai_x = lhs[i]
            bj_y = rhs[j]
            if cmp(ai_x, bj_y) > 0:
                ls.append(bj_y)
                j += 1
            else:
                ls.append(ai_x)
                i += 1
        else:
            if i < 0:
                ls.extend(lhs[i:])
            if j < 0:
                ls.extend(rhs[j:])

        if not len(ls)==len(lhs)+len(rhs): raise logic-err
        sz2blocks[len(ls)].append(ls)


    def init__sz2blocks(ps, sign_sz_ls, /):
        L = len(ps)
        sz2blocks = [[] for _ in range(L+1)]
        sz2blocks[0] = None
        it = iter(ps)
        for sign, sz in sign_sz_ls:
            block = [*islice(it, sz)]
            if sign > 0:
                block.reverse()
            sz2blocks[sz].append(block)
        sz2blocks[0] = []
        return sz2blocks
    def merge__sz2blocks(cmp, L, sz2blocks, /):
        assert sz2blocks
        assert not sz2blocks[0]
        it_blocks = chain.from_iterable(sz2blocks)
        ls2 = []
        block = None
        for block in it_blocks:
            ls2.append(block)
            if len(ls2) == 2:
                merge_to(sz2blocks, cmp, *ls2)
                ls2.clear()
        else:
            if block is None: raise logic-err
            if not len(block)==L: raise logic-err
            if not len(ls2) == 1: raise logic-err
            if not ls2[0] is block: raise logic-err
            sorted_xs = [x for ai, x in block]
        return sorted_xs

    def main(xs, key, cmp, reverse, to_count_num_cmp, /):
        if key is None:
            key = echo
        if cmp is None:
            cmp = default_cmp
        if to_count_num_cmp:
            cmp = counter = CallCounter(cmp)
        cmp = init__cmp(cmp, reverse)
        ps = init__ps(key, xs)

        L = len(ps)
        if L < 2:
            sorted_xs = [x for ai, x in ps]
        else:
            sign_sz_ls = init__sign_sz_ls(ps, cmp)
            sz2blocks = init__sz2blocks(ps, sign_sz_ls)
            sorted_xs = merge__sz2blocks(cmp, L, sz2blocks)
        sorted_xs
        if to_count_num_cmp:
            num_cmp = counter.count
            return sorted_xs, num_cmp
        return sorted_xs
    return main

_main4merge_sort__stable = _0_merge_sort__stable()
def merge_sort__stable(xs, /, *, key, cmp, reverse, to_count_num_cmp=False):
    r'''
    Iter a -> (key::a->k) -> (cmp::k->k->int) -> (reverse::bool) -> [a] if not to_count_num_cmp else ([a], num_cmp)
    #'''
    return _main4merge_sort__stable(xs, key, cmp, reverse, to_count_num_cmp)





#def merge_sort__unstable(xs, /, *, key, __lt__, reverse):




if __name__ == "__main__":
    import doctest
    doctest.testmod()
