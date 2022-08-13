r'''[[[
e ../../python3_src/seed/math/iter_sorted_products_of_uints.py
!mv ../../python3_src/seed/math/iter_sorted_products_of_pairwise_coprime_uints.py ../../python3_src/seed/math/iter_sorted_products_of_uints.py
from seed.math.iter_sorted_products_of_uints import iter_sorted_products_of_uints
py -m seed.math.iter_sorted_products_of_uints

f({2,3}) -> [1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 27, 32, ...]
可能的用处:
    给定 素数集ps，搜索 (q:=II p**e<p> {p<-ps} + 1) 型 素数
        phi(q)=(q-1) is ps-smooth

#]]]'''
__all__ = '''
    iter_sorted_products_of_uints

    '''.split()
    #iter_sorted_products_of_pairwise_coprime_uints

from seed.math.II import II
from seed.math.gcd import gcd
from seed.math.lcm import lcm_many
import heapq
from itertools import islice

if 0:
  def iter_sorted_products_of_pairwise_coprime_uints(us, /):
    #pairwise_coprime ==>> outs all diff 但还是不能自动避免重复(不同路径相乘:2*3==3*2)
    us = sorted(us)
    if not all(type(u) is int for u in us): raise TypeError
    if not all(u >= 1 for u in us): raise ValueError
    del us[:us.count(1)]

    if 0:
        M = II(us)
        if not all(gcd(u, M//u) ==1 for u in us): raise ValueError
    else:
        if not lcm_many(us) == II(us): raise ValueError('not pairwise coprime')
    return iter_sorted_products_of_uints(us)


def iter_sorted_products_of_uints(us, /):
    us = {*us}
    if not all(type(u) is int for u in us): raise TypeError
    if not all(u >= 0 for u in us): raise ValueError
    if 0 in us:
        yield 0
        us.remove(0)
    us.discard(1)
        # [u >= 2]

    outs = []
    o = 1
    yield o; outs.append(o)

    if not us: return

    heap = []
    def init_heap(heap, us):
        for u in us:
            put(u, 0)
    def mk_item(u, idx, /):
        o = u*outs[idx]
        heap_item = (o, (u, idx))
        return heap_item
    def put(u, idx, /):
        heap_item = mk_item(u, idx)
        heapq.heappush(heap, heap_item)
    def get():
        prev_o = outs[-1]
        while 1:
            (o, (u, idx)) = old_heap_item = heap[0]
            if not o == prev_o:
                #避免重复
                #来源1:不同路径相乘:2*3==3*2
                #来源2:不互素相乘: 6*35==10*21
                outs.append(o)
                    #必须在mk_item使用outs[idx+1]之前 加入！
            ###
            new_heap_item = mk_item(u, idx+1)
            old_heap_item = heapq.heappushpop(heap, new_heap_item)
            if not o == prev_o:
                break

        return o
    init_heap(heap, us)
    while 1:
        yield get()
assert [*iter_sorted_products_of_uints([])] == [1]
#print([*islice(iter_sorted_products_of_uints([2,3]), 13)])
#print([*islice(iter_sorted_products_of_uints([2,3,5]), 19)])
assert [*islice(iter_sorted_products_of_uints([2,3]), 13)] == [1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 27, 32]
assert [*islice(iter_sorted_products_of_uints([2,3,5]), 19)] == [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32]

