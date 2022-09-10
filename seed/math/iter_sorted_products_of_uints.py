r'''[[[
e ../../python3_src/seed/math/iter_sorted_products_of_uints.py
!mv ../../python3_src/seed/math/iter_sorted_products_of_pairwise_coprime_uints.py ../../python3_src/seed/math/iter_sorted_products_of_uints.py
from seed.math.iter_sorted_products_of_uints import iter_sorted_products_of_uints, iter_sorted_products_of_strict_sorted_pairwise_coprime_uints, iter_sorted_products_of_strict_sorted_pairwise_coprime_uints__with_ifactor_exp_pairs


py -m nn_ns.app.debug_cmd   seed.math.iter_sorted_products_of_uints
py -m seed.math.iter_sorted_products_of_uints _NOP_
py -m seed.math.iter_sorted_products_of_uints print_sorted_products_of_strict_sorted_pairwise_coprime_uints =[] =3
[1]
py -m seed.math.iter_sorted_products_of_uints print_sorted_products_of_strict_sorted_pairwise_coprime_uints =[2] =5
[1, 2, 4, 8, 16]
py -m seed.math.iter_sorted_products_of_uints print_sorted_products_of_strict_sorted_pairwise_coprime_uints =[2,3] =15
[1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 27, 32, 36, 48]
py -m seed.math.iter_sorted_products_of_uints print_sorted_products_of_strict_sorted_pairwise_coprime_uints =[2,3,5] =25
[1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32, 36, 40, 45, 48, 50, 54]

f({2,3}) -> [1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 27, 32, ...]
可能的用处:
    给定 素数集ps，搜索 (q:=II p**e<p> {p<-ps} + 1) 型 素数
        phi(q)=(q-1) is ps-smooth

#]]]'''
__all__ = '''
    iter_sorted_products_of_uints
    iter_sorted_products_of_strict_sorted_pairwise_coprime_uints
    iter_sorted_products_of_strict_sorted_pairwise_coprime_uints__with_ifactor_exp_pairs


    '''.split()
    #iter_sorted_products_of_pairwise_coprime_uints

from seed.math.II import II
from seed.math.gcd import gcd
from seed.math.lcm import lcm_many
from seed.math.are_pairwise_coprime import are_pairwise_coprime
from seed.tiny_.check import check_int_ge
from seed.tiny import fst

import heapq
from itertools import islice

def iter_sorted_products_of_strict_sorted_pairwise_coprime_uints(sorted_coprime_factors, /, *, finite_seq_vs_infinite_seq, turnoff__verify_factors_are_pairwise_coprime):
    return map(fst, iter_sorted_products_of_strict_sorted_pairwise_coprime_uints__with_ifactor_exp_pairs(sorted_coprime_factors, finite_seq_vs_infinite_seq=finite_seq_vs_infinite_seq, turnoff__verify_factors_are_pairwise_coprime=turnoff__verify_factors_are_pairwise_coprime))
def iter_sorted_products_of_strict_sorted_pairwise_coprime_uints__with_ifactor_exp_pairs(sorted_coprime_factors, /, *, finite_seq_vs_infinite_seq, turnoff__verify_factors_are_pairwise_coprime):
    #def iter_sorted_products_of_pairwise_coprime_uints(us, /):
    #pairwise_coprime ==>> outs all diff 但还是不能自动避免重复(不同路径相乘:2*3==3*2)

    turnoff__verify_factors_are_pairwise_coprime = bool(turnoff__verify_factors_are_pairwise_coprime)
    finite_seq_vs_infinite_seq = bool(finite_seq_vs_infinite_seq)
    if not finite_seq_vs_infinite_seq:
        L = len(sorted_coprime_factors)
        xL = L
    else:
        xL = float('inf')


    if 0:
        #may be infinite seq such as PRIMES
        if not turnoff__verify_factors_are_pairwise_coprime:
            if not are_pairwise_coprime(sorted_coprime_factors): raise ValueError

    tmay_min_unused_idx4factors_and_prev_factor_and_may_II_prev_factors = [(0, 1, (None if turnoff__verify_factors_are_pairwise_coprime else 1))]
    _coprime_factors = sorted_coprime_factors
    del sorted_coprime_factors
    def get_(i, /):
        if not i >= 0: raise IndexError
        if not finite_seq_vs_infinite_seq:
            if not i < L: raise IndexError

        [(min_unused_idx4factors, prev_factor, may_II_prev_factors)] = tmay_min_unused_idx4factors_and_prev_factor_and_may_II_prev_factors
        factor = _coprime_factors[i]
        if i == min_unused_idx4factors:
            #strict_sorted
            check_int_ge(prev_factor+1, factor)

            #pairwise_coprime
            if not turnoff__verify_factors_are_pairwise_coprime:
                II_prev_factors = may_II_prev_factors
                if not 1==gcd(factor, II_prev_factors): raise ValueError
                may_II_prev_factors = factor*II_prev_factors

            tmay_min_unused_idx4factors_and_prev_factor_and_may_II_prev_factors[0] = (1+min_unused_idx4factors, factor, may_II_prev_factors)
        else:
            if not i < min_unused_idx4factors: raise logic-err
        return factor

    if 0:
        ies = ifactor_exp_pairs = ()
            # [exp >= 1]
            # [0 <= ifactor < xL]
        product5ies = 1
        if xL == 0:
            yield product5ies
            return

    heap = []
    def init_heap(heap, /):
        ies = ifactor_exp_pairs = ()
            # [exp >= 1]
            # [0 <= ifactor < xL]
        product5ies = 1
        heap_item = mk_item(product5ies, ies)
        put(heap_item)
    def mk_item(product5ies, ies, /):
        heap_item = (product5ies, ies)
        return heap_item
    def put(heap_item, /):
        heapq.heappush(heap, heap_item)

    def iter_new_items(old_heap_item, /, *, _ver_=2):
        #ver3:dec(ies) == if e0 >=2 then [(i0,e0-1),*_ies] elif len(ies) == 1 and i0 >=1 then [(i0-1,1)] else [*_ies]
        #   ver3 ==>> inc()不使用除法;但 扇出系数 太大，不好
        #ver2:dec(ies) == (if i0 >= 1 then [(i0-1,1)] else [])++(if e0 >=2 then [(i0,e0-1)] else [])++_ies
        #ver1:dec(ies) == if e0 >=2 then [(i0,e0-1),*_ies] elif i0 >= 1 then [(i0-1,1),*_ies] else [*_ies]
        #==>> inc(ies) := inv<dec>(ies)
        #ver1:inc(ies) == if xL == 0 then [] else (if len(ies)==0 or i0>=1 then [[(0,1),*ies]] else [])++(if len(ies)>=1 then [[(i0,e0+1),*_ies]] else [])++(if (len(ies)>=1 and e0==1 and i0+1 < (if len(_ies)>=1 then _ies[0][0] else xL)) then [[(i0+1,1),*_ies]] else [])
        #ver2:inc(ies) == if xL == 0 then [] else (if len(ies)==0 or i0>=1 then [[(0,1),*ies]] else [])++(if len(ies)>=1 and i0==0 then [[(i0,e0+1),*_ies]] else [])++(if (len(ies)>=1 and e0==1 and i0+1 < (if len(_ies)>=1 then _ies[0][0] else xL)) then [[(i0+1,1),*_ies]] else [])++(if (len(ies)>=2 and e0==1 and i0+1 == _ies[0][0]) then [[(i0+1,1+_ies[0][1]),*_ies[1:]]] else [])
        #ver3:inc(ies) == if xL == 0 then [] else (if len(ies)==0 then [[(0,1)]] else [])++(if (len(ies)==1 and e0==1 and i0+1 < xL) then [[(i0+1,1)]] else [])++(if len(ies)>=1 then [[(i0,e0+1),*_ies]] else [])++(if (len(ies)>=1 and i0 >= 1) then [[(i_,1),*ies] for i_ in range(i0)] else [])
        (old_product5ies, old_ies) = old_heap_item

        if _ver_==3:
            #ver3:
            if xL == 0:
                return;yield
            #sz = 1+(old_ies[-1][0] if old_ies else -1)
            len_ies = len(old_ies)
            if not len_ies == 0:
                [(i0,e0), *_ies] = old_ies
                if len_ies==1 and e0 == 1 and 1+i0 < xL:
                    ies = ((1+i0,1),)
                    product5ies = get_(1+i0)
                    yield mk_item(product5ies, ies)
                if 1:
                    ies = ((i0,1+e0), *_ies)
                    product5ies = old_product5ies*get_(i0)
                    yield mk_item(product5ies, ies)
                for i_ in range(i0):
                    ies = (((i_,1),*old_ies))
                    product5ies = old_product5ies*get_(i_)
                    yield mk_item(product5ies, ies)

            else:
                    ies = ((0,1),)
                    product5ies = get_(0)
                    yield mk_item(product5ies, ies)
            return
        if _ver_==2:
            #ver2:
            if xL == 0:
                return;yield
            #sz = 1+(old_ies[-1][0] if old_ies else -1)
            len_ies = len(old_ies)
            if not len_ies == 0:
                [(i0,e0), *_ies] = old_ies

                if i0 == 0:
                    ies = ((0,1+e0), *_ies)
                else:
                    ies = ((0,1), *old_ies)
                product5ies = old_product5ies*get_(0)
                yield mk_item(product5ies, ies)

                if e0 == 1 and 1+i0 < xL:
                    if len_ies >= 2 and 1+i0==_ies[0][0]:
                        [(i1,e1), *_1ies] = _ies
                        ies = ((i1,1+e1), *_1ies)
                    else:
                        i1 = 1+i0
                        ies = ((i1,1), *_ies)
                    product5ies = old_product5ies//get_(i0) *get_(i1)
                    yield mk_item(product5ies, ies)
            else:
                    ies = ((0,1),)
                    product5ies = get_(0)
                    yield mk_item(product5ies, ies)
            return
    #end-def iter_new_items(old_product5ies, old_ies, /):



    init_heap(heap)
    while heap:
        #(old_product5ies, old_ies)
        old_heap_item = heapq.heappop(heap)
        yield old_heap_item
        for new_heap_item in iter_new_items(old_heap_item):
            put(new_heap_item)
if __name__ == "__main__":
  def print_sorted_products_of_strict_sorted_pairwise_coprime_uints(sorted_coprime_factors, sz, /):
    it = iter_sorted_products_of_strict_sorted_pairwise_coprime_uints(sorted_coprime_factors, finite_seq_vs_infinite_seq=False, turnoff__verify_factors_are_pairwise_coprime=False)
    it = islice(it, sz)
    print([*it])


if 0:
  def iter_sorted_products_of_pairwise_coprime_uints(us, /):
    us = sorted(us)
    if not all(type(u) is int for u in us): raise TypeError
    if not all(u >= 2 for u in us): raise ValueError
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


if __name__ == "__main__":
    def _NOP_():pass #nop:no-op:无操作:用于 adhoc_argparser__main
    from seed.recognize.cmdline.adhoc_argparser import adhoc_argparser__main, adhoc_argparse, AdhocArgParserError
    adhoc_argparser__main(globals(), None)
        #main()





