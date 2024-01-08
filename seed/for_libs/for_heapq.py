#__all__:goto
r'''[[[
e ../../python3_src/seed/for_libs/for_heapq.py
    view ../../python3_src/seed/types/Heap.py
    view ../../python3_src/seed/types/OverrideOrdering.py
    view ../../python3_src/seed/for_libs/for_heapq.py

[[
vs py.heapq:
    ++__le__
    ########
    ++key
    ++__le__
    ++reverse
    ########
    ++item5obj_
    ++item2val_
    ########
    ++obj_vs_item
    ++applied__heapify
    ########
    ++obj_vs_item
    ++val_vs_item
    ########

cp /data/data/com.termux/files/usr/lib/python3.10/heapq.py /sdcard/0my_files/tmp/out4py/py_src/py-heapq.py
view /sdcard/0my_files/tmp/out4py/py_src/py-heapq.py
]]


seed.for_libs.for_heapq
py -m nn_ns.app.debug_cmd   seed.for_libs.for_heapq -x
py -m nn_ns.app.doctest_cmd seed.for_libs.for_heapq:__doc__ -ff -v
py_adhoc_call   seed.for_libs.for_heapq   @f
from seed.for_libs.for_heapq import *


[[
!!!not bug!!!
xxx:py-bugs:heapq.heapify is not O(n)
#copy from: /data/data/com.termux/files/usr/lib/python3.10/heapq.py
def heapify(x):
    n = len(x)
    for i in reversed(range(n//2)):
        _siftup(x, i)
===
>>> class X:
...     i = 0
...     def __init__(sf, x, /):
...         sf.x = x
...     @classmethod
...     def reset(cls, /):
...         cls.i = 0
...     @classmethod
...     def inc(cls, /):
...         cls.i += 1
...     def __le__(sf, ot, /):
...         sf.inc()
...         return sf.x <= ot.x
...     def __lt__(sf, ot, /):
...         sf.inc()
...         return sf.x < ot.x
...     def __ge__(sf, ot, /):
...         sf.inc()
...         return sf.x >= ot.x
...     def __gt__(sf, ot, /):
...         sf.inc()
...         return sf.x > ot.x
...     def __eq__(sf, ot, /):
...         sf.inc()
...         return sf.x == ot.x
...     def __ne__(sf, ot, /):
...         sf.inc()
...         return sf.x != ot.x
>>> def test_(N, /, *, reverse=False):
...     from heapq import heapify
...     ls = [*map(X, range(N)[::1-bool(reverse)*2])]
...     X.reset()
...     heapify(ls)
...     return X.i
>>> test_(2**4)
26
>>> test_(2**6)
120
>>> test_(2**8)
502
>>> test_(2**10)
2036
>>> test_(2**12)
8178
>>> test_(2**4, reverse=True)
19
>>> test_(2**6, reverse=True)
89
>>> test_(2**8, reverse=True)
375
>>> test_(2**10, reverse=True)
1525
>>> test_(2**12, reverse=True)
6131

===
# [:proof___heapify_is_O_N]:here
[d<curr_node> =[def]= len of path from curr_node to leaf]
[O(py.heapify<N>)
= O(d*(N/2**d) for d in [1..=logN])
<= O(N*sum{d/2**d | [d :<- [1..]]})
<= O(N*SS(x*(1/2)**x : x : 0-->+oo))
<= O(N*2.0813689810056077)
= O(N)
]
[DD(b**x : x) = DD(e**(ln(b)*x) : x) = b**x*ln(b)]
[DD(x*b**x : x) = b**x + x*b**x*ln(b)]
[(b**x) + C = SS(b**x : x)*ln(b)]
[(x*b**x) + C = SS(b**x : x) + SS(x*b**x : x)*ln(b)]
[SS(x*b**x : x) = (x*b**x)/ln(b) -SS(b**x : x)/ln(b) +C]
[SS(x*b**x : x) = (x*b**x)/ln(b) -(b**x)/ln(b)/ln(b) +C]
[b < 1]:
    [SS(x*b**x : x : 0-->+oo) = 1/ln(b)/ln(b)]
[SS(x*(1/2)**x : x : 0-->+oo) = 1/ln(2)/ln(2)]
#>>> 1/math.log(2)**2
2.0813689810056077
===
]]


>>> list(merge([1,3,5,7], [0,2,4,8], [5,10,15,20], [], [25]))
[0, 1, 2, 3, 4, 5, 5, 7, 8, 10, 15, 20, 25]
>>> list(merge(['dog', 'horse'], ['cat', 'fish', 'kangaroo'], key=len))
['dog', 'cat', 'fish', 'horse', 'kangaroo']

>>> for sz in range(5):[nsmallest(sz, range(N)) for N in range(3)]
[[], [], []]
[[], [0], [0]]
[[], [0], [0, 1]]
[[], [0], [0, 1]]
[[], [0], [0, 1]]
>>> for N in range(9):nsmallest(5, range(N))
[]
[0]
[0, 1]
[0, 1, 2]
[0, 1, 2, 3]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
>>> nsmallest(3, ['dog', 'horse', 'cat', 'fish', 'kangaroo'], key=len)
['dog', 'cat', 'fish']
>>> nsmallest(5, ['dog', 'horse', 'cat', 'fish', 'kangaroo'], key=len) #list.sort()
['dog', 'cat', 'fish', 'horse', 'kangaroo']

>>> for sz in range(5):[nlargest(sz, range(N)) for N in range(3)]
[[], [], []]
[[], [0], [1]]
[[], [0], [1, 0]]
[[], [0], [1, 0]]
[[], [0], [1, 0]]
>>> for N in range(9):nlargest(5, range(N))
[]
[0]
[1, 0]
[2, 1, 0]
[3, 2, 1, 0]
[4, 3, 2, 1, 0]
[5, 4, 3, 2, 1]
[6, 5, 4, 3, 2]
[7, 6, 5, 4, 3]
>>> nlargest(4, ['dog', 'horse', 'cat', 'fish', 'kangaroo'], key=len)
['kangaroo', 'horse', 'fish', 'dog']
>>> nlargest(5, ['dog', 'horse', 'cat', 'fish', 'kangaroo'], key=len) #list.sort()
['kangaroo', 'horse', 'fish', 'dog', 'cat']



>>> nsmallest(3, ['111', '222', '333', '444', '555'], key=len)
['111', '222', '333']
>>> nlargest(3, ['111', '222', '333', '444', '555'], key=len)
['111', '222', '333']

>>> nsmallest(3, ['111', '22', '3333', '444', '555'], key=len)
['22', '111', '444']
>>> nlargest(3, ['111', '22', '3333', '444', '555'], key=len)
['3333', '111', '444']


>>> heap_sort_(['111', '222', '333', '444', '555'], key=len)
['111', '222', '333', '444', '555']
>>> heap_sort_(['111', '222', '333', '444', '555'], key=len, reverse=True)
['111', '222', '333', '444', '555']

>>> heap_sort_(['111', '22', '3333', '444', '555'], key=len)
['22', '111', '444', '555', '3333']
>>> heap_sort_(['111', '22', '3333', '444', '555'], key=len, reverse=True)
['3333', '111', '444', '555', '22']


>>> ls = [*range(9)[::-1]]
>>> ls
[8, 7, 6, 5, 4, 3, 2, 1, 0]

>>> heapify(ls)
>>> ls
[0, 1, 2, 5, 4, 3, 6, 7, 8]
>>> heap_validate_(ls)

>>> ls
[0, 1, 2, 5, 4, 3, 6, 7, 8]
>>> heappush(ls, 9)
>>> ls
[0, 1, 2, 5, 4, 3, 6, 7, 8, 9]
>>> heap_validate_(ls)

>>> heappush(ls, -1)
>>> ls
[-1, 0, 2, 5, 1, 3, 6, 7, 8, 9, 4]
>>> heap_validate_(ls)

>>> heappop(ls)
-1
>>> ls
[0, 1, 2, 5, 4, 3, 6, 7, 8, 9]
>>> heap_validate_(ls)

>>> heappop(ls)
0
>>> ls
[1, 4, 2, 5, 9, 3, 6, 7, 8]
>>> heap_validate_(ls)

>>> heappushpop(ls, 0)
0
>>> ls
[1, 4, 2, 5, 9, 3, 6, 7, 8]
>>> heappushpop(ls, 1)
1
>>> ls
[1, 4, 2, 5, 9, 3, 6, 7, 8]
>>> heap_validate_(ls)

>>> heappushpop(ls, 2)
1
>>> ls
[2, 4, 2, 5, 9, 3, 6, 7, 8]
>>> heap_validate_(ls)

>>> heappoppush(ls, 1)
2
>>> ls
[1, 4, 2, 5, 9, 3, 6, 7, 8]
>>> heap_validate_(ls)



#]]]'''
__all__ = r'''

to_iparent_
    to_ichildren_
    to_ichildren__


iter_merge_sorted_iterables_
    merge

extract_kth_smallest_elements_
    nsmallest
    nlargest

heap_sort_




Heap
    std____key__le__reverse_
    heap_validate_
        ValidateFail__not_heap
    heappushs_
    heappops_
    heappop_eqvs_

    heapify
    heappush
    heappop
    heappushpop
    heappoppush
    heapreplace

'''.split()#'''
__all__

from itertools import count as count_
from itertools import islice
from seed.tiny import at
from seed.tiny import ifNonef, ifNone, echo
from seed.tiny import check_type_is
from seed.tiny_.check import check_callable
from seed.tiny_.std____key__le__reverse_ import std____key__le__reverse_

class ValidateFail__not_heap(Exception):pass

def to_ichildren__(len_heap, iparent, /):
    ichildren = [*to_ichildren_(iparent)]
    if not ichildren[-1] < len_heap:
        ichildren.pop()
        if not ichildren[-1] < len_heap:
            ichildren.pop()
    return tuple(ichildren)

def to_ichildren_(iparent, /):
    # i --> (2*i+1, 2*i+2)
    assert iparent >= 0
    iz = iparent << 1
    return (iz+1, iz+2)
def to_iparent_(ichild, /):
    # i --> (2*i+1, 2*i+2)
    # j <-- (j-1)//2
    # 0 --> (1,2)
    # 1 --> (3,4)
    # 2 --> (5,6)
    # 3 --> (7,8)
    assert ichild > 0
    iparent = (ichild-1)//2
    return iparent

class Heap:
    ######################
    def __init__(sf, heap, /, *, item5obj_, item2val_, key, __le__, reverse, obj_vs_item, applied__heapify):
        r'''[[[
        heap :: [item] if obj_vs_item else [obj]
        item5obj_ :: may (obj -> item)
        item2val_ :: may (item -> val)
        key :: may (item -> k)
        __le__ :: k -> k -> bool
        reverse :: bool
            flip __le__
        obj_vs_item :: bool
        applied__heapify :: bool


        #]]]'''#'''
        (key, __le__, reverse) = std____key__le__reverse_(key, __le__, reverse)

        check_type_is(bool, obj_vs_item)
        check_type_is(bool, applied__heapify)

        item5obj_ = ifNone(item5obj_, echo)
        check_callable(item5obj_)

        item2val_ = ifNone(item2val_, echo)
        check_callable(item2val_)


        [] = heap[:0]
        len(heap)

        sf.args = (heap, item5obj_, item2val_, key, __le__, reverse)
        (heap, item5obj_, item2val_, key, __le__, reverse) = sf.args

        sf.heapify(obj_vs_item=obj_vs_item, applied__heapify=applied__heapify)

    def __len__(sf, /):
        return len(sf.heap)

    ######################
    @property
    def heap(sf, /):
        return sf.args[0]
    @property
    def item5obj_(sf, /):
        return sf.args[1]
    @property
    def item2val_(sf, /):
        return sf.args[2]
    @property
    def key(sf, /):
        return sf.args[3]
    @property
    def ___le___(sf, /):
        #__le__
        return sf.args[4]
    @property
    def reverse(sf, /):
        return sf.args[5]

    ######################
    def le__idx_(sf, lhs_idx, rhs_idx, /):
        heap = sf.heap
        lhs_item = heap[lhs_idx]
        rhs_item = heap[rhs_idx]
        return sf.le__item_(lhs_item, rhs_item)
    def lt__idx_(sf, lhs_idx, rhs_idx, /):
        return not sf.le__idx_(rhs_idx, lhs_idx)

    def le__item_(sf, lhs_item, rhs_item, /):
        (_heap, _item5obj_, _item2val_, key, __le__, reverse) = sf.args

        lhs_key = key(lhs_item)
        rhs_key = key(rhs_item)

        if reverse:
            lhs_key, rhs_key = rhs_key, lhs_key
        return __le__(lhs_key, rhs_key)
        #raise NameError(__le__)
    def lt__item_(sf, lhs_item, rhs_item, /):
        return not sf.le__item_(rhs_item, lhs_item)

    ######################
    def heap_validate_(sf, /):
        heap = sf.heap
        for ichild in range(1, len(heap)):
            iparent = to_iparent_(ichild)
            if not sf.le__idx_(iparent, ichild): raise ValidateFail__not_heap

    ######################
    def heapify(sf, /, *, obj_vs_item, applied__heapify):
        'O(N)'
        if not obj_vs_item:
            heap = sf.heap
            item5obj_ = sf.item5obj_
            for i in range(len(heap)):
                obj = heap[i]
                item = item5obj_(obj)
                heap[i] = item
        if not applied__heapify:
            sf._heapify()
            if 0b00:print(sf.heap)
            if 0b00:sf.heap_validate_()
    def _heapify(sf, /):
        'O(N)'
        ##########ver2:
        heap = sf.heap
        end = len(heap)
        if end < 2:
            return
        # [end >= 2]
        ilast = end-1
        # [ilast >= 1]
        #   #to_iparent_(ilast) required [ilast > 0]
        iparent4last = to_iparent_(ilast)
        for iparent in reversed(range(iparent4last+1)):
            # [:proof___heapify_is_O_N]:goto
            sf._try_rshift_at__until_end(iparent)
        return
        ##########ver1:bug:
        heap = sf.heap
        for ichild in reversed(range(1, len(heap))):
            sf._try_lshift_at(ichild)
            raise 000 #logic-err
    def _try_lshift_at(sf, ichild, /):
        '-> swapped/bool #O(1)'
        iparent = to_iparent_(ichild)
        if (swapped := not sf.le__idx_(iparent, ichild)):
            #if 0b00:print(iparent, ichild, sf.heap)
            sf.swap__idx_(iparent, ichild)
        return swapped
    def swap__idx_(sf, i, j, /):
        if i == j:
            return
        heap = sf.heap
        heap[i], heap[j] = heap[j], heap[i]

    def _item5obj(sf, obj_vs_item, obj, /):
        if obj_vs_item is False:
            item5obj_ = sf.item5obj_
            item = item5obj_(obj)
        elif obj_vs_item is True:
            item = obj
        else:
            raise 000
        return item
    def _item2val(sf, val_vs_item, item, /):
        if val_vs_item is False:
            item2val_ = sf.item2val_
            val = item2val_(item)
        elif val_vs_item is True:
            val = item
        else:
            raise 000
        return val

    ######################
    def heappush(sf, obj, /, *, obj_vs_item=False):
        'O(logN)'
        heap = sf.heap

        item = sf._item5obj(obj_vs_item, obj)
        heap.append(item)

        sf._try_lshift_at__until(0, len(heap)-1)
        if 0b00:print(heap)
        if 0b00:sf.heap_validate_()

    def _try_lshift_at__until(sf, iancestor, ichild, /):
        'O(logN)'
        while not ichild == iancestor and sf._try_lshift_at(ichild):
            iparent = to_iparent_(ichild)
            #######
            #next_round:
            ichild = iparent
        return ichild

    ######################
    def heappop(sf, /, *, val_vs_item=False):
        'O(logN)'
        heap = sf.heap

        last_item = heap.pop()
            # ^IndexError
        result = sf.heappushpop(last_item, obj_vs_item=True, val_vs_item=val_vs_item)
        if 0b00:print(heap)
        if 0b00:sf.heap_validate_()
        return result

    ######################
    def heappushpop(sf, obj, /, *, obj_vs_item=False, val_vs_item=False):
        'O(logN)'
        heap = sf.heap

        item = sf._item5obj(obj_vs_item, obj)
        if heap and not sf.le__item_(item, heap[0]):
            result_item = sf.heappoppush(item, obj_vs_item=True, val_vs_item=True)
        else:
            result_item = item
        result_item

        result = sf._item2val(val_vs_item, result_item)
        return result


    ######################
    def heappoppush(sf, obj, /, *, obj_vs_item=False, val_vs_item=False):
        'O(logN)'
        heap = sf.heap

        item = sf._item5obj(obj_vs_item, obj)
        if heap:
            result_item = heap[0]
            heap[0] = item
            sf._try_rshift_at__until_end(0)
            if 0b00:print(heap)
            if 0b00:sf.heap_validate_()
        else:
            result_item = item
        result_item

        result = sf._item2val(val_vs_item, result_item)
        return result
    heapreplace = heappoppush



    def _try_rshift_at__until_end(sf, iparent, /):
        '-> new_iparent/bool #O(logN)'
        'O(logN)'
        ##########ver2:
        #rshift hole/inf then put back and lshift old_item
        #
        heap = sf.heap
        old_item = heap[iparent]
            # ^IndexError
        # [iparent < end]
        #heap[iparent] = hole = inf
        old_iparent = iparent

        end = len(heap)
        assert 0 <= iparent < end
        # [0 <= iparent < end]
        if end < 2:
            return iparent
        # [end >= 2]
        ilast = end -1
        # [ilast >= 1]
        #   #to_iparent_(ilast) required [ilast > 0]
        iparent4last = to_iparent_(ilast)
        while not iparent > iparent4last:
            ichildren = to_ichildren__(end, iparent)
            assert ichildren
            if len(ichildren) == 2:
                [ileft, iright] = ichildren
                ichild4min = ileft if sf.le__idx_(ileft, iright) else iright
            else:
                [ichild4min] = ichildren
            ichild4min
            heap[iparent] = heap[ichild4min]
            #heap[ichild4min] = hole = inf
            iparent = ichild4min
        heap[iparent] = old_item
        iparent = sf._try_lshift_at__until(old_iparent, iparent)
        return iparent

        ##########ver1:
        heap = sf.heap
        end = len(heap)
        assert 0 <= iparent < end
        if end < 2:
            return iparent
        # [end >= 2]
        ilast = end -1
        # [ilast >= 1]
        #   #to_iparent_(ilast) required [ilast > 0]
        iparent4last = to_iparent_(ilast)
        while not iparent > iparent4last:
            ichildren = to_ichildren__(end, iparent)
            assert ichildren
            if len(ichildren) == 2:
                [ileft, iright] = ichildren
                ichild4min = ileft if sf.le__idx_(ileft, iright) else iright
            else:
                [ichild4min] = ichildren
            ichild4min
            if not sf._try_lshift_at(ichild4min):
                break
            iparent = ichild4min
        return iparent

    ######################
    def heappushs_(sf, objs, /, *, obj_vs_item=False):
        'O(len(objs)*logN)'
        for obj in objs:
            sf.heappush(obj, obj_vs_item=obj_vs_item)
    ######################
    def heappops_(sf, may_sz=None, /, *, val_vs_item=False):
        'O(sz*logN)'
        sz = ifNone(may_sz, len(sf))
        sz = min(sz, len(sf))
        return [sf.heappop(val_vs_item=val_vs_item) for _ in range(sz)]

    ######################
    def heappop_eqvs_(sf, /, *, val_vs_item=False):
        'O(sz*logN)'
        min_item = sf.heappop(val_vs_item=True)
            # ^IndexError
        items = [min_item]

        heap = sf.heap
        while heap and sf.le__item_(heap[0], min_item):
            item = sf.heappop(val_vs_item=True)
            items.append(item)
        if val_vs_item is False:
            vs = [sf._item2val(val_vs_item, item) for item in items]
        else:
            vs = items
        vs
        return vs


    ######################
    heappushs_
    heappops_
    heappop_eqvs_

    heapify
    heappush
    heappop
    heappushpop
    heappoppush
    heapreplace
#end-class Heap:

######################
def _mk___item5obj(key, reverse, /):
    r'''[[[
    [obj :: (idx, x)]
    [key/small_key :: x -> k]
    [big_k :: Ord i => (small_k,i,x)]

    #]]]'''#'''
    def item5obj_(i_x, /):
        i, x = i_x
        if reverse:
            return (key(x), -i, x)
        else:
            return (key(x), i, x)
    return item5obj_
def _mk___le___(__le__, /):
    r'''[[[
    [__le__ :: total_order<small_k>]
    [___le___ :: total_order<big_k>]
    [big_k :: Ord i => (small_k,i, ...)]

    #]]]'''#'''
    def ___le___(lhs_key, rhs_key, /):
        lk = lhs_key[0]
        rk = rhs_key[0]
        if not lk is rk:
            if not __le__(rk, lk):
                # [not$ rk <= lk]
                # [rk > lk]
                # [lk < rk]
                # [lhs <= rhs]
                return True
            # [rk <= lk]
            # [lk >= rk]
            if not __le__(lk, rk):
                # [not$ lk <= rk]
                # [not$ lhs <= rhs]
                return False
            # [lk == rk]
        # [lk == rk]
        i = lhs_key[1]
        j = rhs_key[1]
        return i <= j
    return ___le___




######################
def iter_merge_sorted_iterables_(*sorted_iterables, key, __le__, reverse):
    r'''[[[
    O(N*log2(len(sorted_iterables)))

    sorted_iterables :: [sorted Iter x]

    #]]]'''#'''
    (key, __le__, reverse) = std____key__le__reverse_(key, __le__, reverse)
    sorted_iterables = (*map(iter, sorted_iterables),)

    def tmay_item5sorted_iterable_(i, sorted_iterable, /):
        it = iter(sorted_iterable)
        for head in it:
            break
        else:
            return ()
        #xxx:signed_idx = -i if reverse else i
        signed_idx = i
        item = item5si_obj_objs_(signed_idx, head, it)
        return (item,)
    def item5si_obj_objs_(signed_idx, obj, iter_sorted_objs, /):
        return (key(obj), signed_idx
                    #total key #distinguish
                ,obj, iter_sorted_objs
                    #payload
                )

    ___le___ = _mk___le___(__le__)

    ls = [item for tmay_item in map(tmay_item5sorted_iterable_, count_(0), sorted_iterables) for item in tmay_item]

    heap = Heap(ls, item5obj_=None, item2val_=None, key=None, __le__=___le___, reverse=reverse, obj_vs_item=True, applied__heapify=False)

    while ls:
        (_k, si, obj, it) = ls[0]
        yield obj
        tm = tmay_item5sorted_iterable_(abs(si), it)
        if tm:
            [item] = tm
            heap.heappoppush(item)
        else:
            heap.heappop()

######################
def extract_kth_smallest_elements_(k, iterable, /, *, key, __le__, reverse):
    'O(min(k,N)*logN)'
    check_type_is(int, k)
    if k < 1:
        return []

    if __le__ is None:
        # Short-cut for k==1 is to use min()
        if k == 1:
            it = iter(iterable)
            sentinel = object()
            f = max if reverse else min
            result = f(it, default=sentinel, key=key)
            return [] if result is sentinel else [result]

        # When k>=size, it's faster to use sorted()
        it = iter(iterable)
        ls = [*islice(it, k+1)]
        if len(ls) <= k:
            ls.sort(key=key, reverse=reverse)
            return ls
    else:
        it = iter(iterable)
        ls = [*slice(it, k)]
    ls, it

    ls = [*enumerate(ls)]
    it = enumerate(it, len(ls))

    (key, __le__, reverse) = std____key__le__reverse_(key, __le__, reverse)
    item5obj_ = _mk___item5obj(key, reverse)
    if 0:
      def item5obj_(i_x, /):
        i, x = i_x
        if reverse:
            #nlargest
            #pop out smalls at first
            #『-i』before --> large --> after --> remain
            return (key(x), -i, x)
        else:
            #nsmallest
            #pop out bigs at first
            #『+i』before --> small --> after --> remain
            return (key(x), +i, x)
            # <<== 『not reverse』+『xs.reverse()』
    ___le___ = _mk___le___(__le__)

    #bug:heap = Heap(ls, item5obj_=item5obj_, item2val_=at[2], key=None, __le__=___le___, reverse=reverse, obj_vs_item=False, applied__heapify=False)
    heap = Heap(ls, item5obj_=item5obj_, item2val_=at[2], key=None, __le__=___le___, reverse=not reverse, obj_vs_item=False, applied__heapify=False)
        # 『not reverse』==>> pop out bigs first
        #
        # extract_kth_smallest_elements_() vs heap_sort_()
        #   #########
        #   extract_kth_smallest_elements_:
        #       item5obj_ = _mk___item5obj(key, reverse)    #same
        #       heap = Heap(..., reverse=not reverse, ...)  #diff
        #       xs.reverse()                                #diff
        #   #########
        #   heap_sort_:
        #       item5obj_ = _mk___item5obj(key, reverse)    #same
        #       heap = Heap(..., reverse=reverse, ...)      #diff
        #       #no: xs.reverse()                           #diff
        #   #########
        #
        #

    if len(ls) == k+1:
        heap.heappop()
    assert len(ls) <= k

    for i_x in it:
        heap.heappushpop(i_x)
            # pop max <<== 『not reverse』
    xs = heap.heappops_()
        # <<== 『at[2]』
    xs.reverse()
        # <<== 『not reverse』
    assert len(xs) <= k
    return xs

######################
def heap_sort_(iterable, /, *, key=None, __le__=None, reverse=False):
    it = enumerate(iterable)

    (key, __le__, reverse) = std____key__le__reverse_(key, __le__, reverse)
    item5obj_ = _mk___item5obj(key, reverse)
    ___le___ = _mk___le___(__le__)

    heap = Heap([], item5obj_=item5obj_, item2val_=at[2], key=None, __le__=___le___, reverse=reverse, obj_vs_item=True, applied__heapify=False)
    #if 0b00:print(heap.heap)
    heap.heappushs_(it)
    return heap.heappops_()





######################
def merge(*sorted_iterables, key=None, __le__=None, reverse=False):
    'O(N*log2(len(sorted_iterables)))'
    return iter_merge_sorted_iterables_(*sorted_iterables, key=key, __le__=__le__, reverse=reverse)
def nsmallest(n, iterable, /, *, key=None, __le__=None, reverse=False):
    'O(min(k,N)*logN)'
    return extract_kth_smallest_elements_(n, iterable, key=key, __le__=__le__, reverse=reverse)
def nlargest(n, iterable, /, *, key=None, __le__=None, reverse=False):
    'O(min(k,N)*logN)'
    return extract_kth_smallest_elements_(n, iterable, key=key, __le__=__le__, reverse=not reverse)

heap_sort_(['111', '222', '333', '444', '555'], key=len)
nsmallest(3, ['111', '222', '333', '444', '555'], key=len)
######################
def heapify(ls, /, *, item5obj_=None, item2val_=None, key=None, __le__=None, reverse=False, obj_vs_item=False, applied__heapify=False):
    'O(N)'
    heap = Heap(ls, item5obj_=item5obj_, item2val_=item2val_, key=key, __le__=__le__, reverse=reverse, obj_vs_item=obj_vs_item, applied__heapify=applied__heapify)
    return None
def heappush(ls, obj, /, *, obj_vs_item=False,     item5obj_=None, item2val_=None, key=None, __le__=None, reverse=False):
    'O(logN)'
    heap = Heap(ls, item5obj_=item5obj_, item2val_=item2val_, key=key, __le__=__le__, reverse=reverse, obj_vs_item=True, applied__heapify=True)
        #NOTE:obj_vs_item!
    heap.heappush(obj, obj_vs_item=obj_vs_item)
    return None

def heappop(ls, /, *, val_vs_item=False,      item5obj_=None, item2val_=None, key=None, __le__=None, reverse=False):
    'O(logN)'
    heap = Heap(ls, item5obj_=item5obj_, item2val_=item2val_, key=key, __le__=__le__, reverse=reverse, obj_vs_item=True, applied__heapify=True)
    val = heap.heappop(val_vs_item=val_vs_item)
    return val

def heappushpop(ls, obj, /, *, obj_vs_item=False, val_vs_item=False,      item5obj_=None, item2val_=None, key=None, __le__=None, reverse=False):
    'O(logN)'
    heap = Heap(ls, item5obj_=item5obj_, item2val_=item2val_, key=key, __le__=__le__, reverse=reverse, obj_vs_item=True, applied__heapify=True)
        #NOTE:obj_vs_item!
    val = heap.heappushpop(obj, obj_vs_item=obj_vs_item, val_vs_item=val_vs_item)
    return val

def heappoppush(ls, obj, /, *, obj_vs_item=False, val_vs_item=False,      item5obj_=None, item2val_=None, key=None, __le__=None, reverse=False):
    'O(logN)'
    heap = Heap(ls, item5obj_=item5obj_, item2val_=item2val_, key=key, __le__=__le__, reverse=reverse, obj_vs_item=True, applied__heapify=True)
        #NOTE:obj_vs_item!
    val = heap.heappoppush(obj, obj_vs_item=obj_vs_item, val_vs_item=val_vs_item)
    return val
heapreplace = heappoppush

def heappushs_(ls, objs, /, *, obj_vs_item=False,      item5obj_=None, item2val_=None, key=None, __le__=None, reverse=False):
    'O(len(objs)*logN)'
    heap = Heap(ls, item5obj_=item5obj_, item2val_=item2val_, key=key, __le__=__le__, reverse=reverse, obj_vs_item=True, applied__heapify=True)
        #NOTE:obj_vs_item!
    heap.heappushs_(objs, obj_vs_item=obj_vs_item)
    return None
def heappops_(ls, may_sz=None, /, *, val_vs_item=False,      item5obj_=None, item2val_=None, key=None, __le__=None, reverse=False):
    'O(sz*logN)'
    heap = Heap(ls, item5obj_=item5obj_, item2val_=item2val_, key=key, __le__=__le__, reverse=reverse, obj_vs_item=True, applied__heapify=True)
    vals = heap.heappops_(may_sz, val_vs_item=val_vs_item)
    return vals
def heappop_eqvs_(ls, /, *, val_vs_item=False,      item5obj_=None, item2val_=None, key=None, __le__=None, reverse=False):
    'O(sz*logN)'
    heap = Heap(ls, item5obj_=item5obj_, item2val_=item2val_, key=key, __le__=__le__, reverse=reverse, obj_vs_item=True, applied__heapify=True)
    eqv_vals = heap.heappop_eqvs_(val_vs_item=val_vs_item)
    return eqv_vals

def heap_validate_(ls, /, *, item5obj_=None, item2val_=None, key=None, __le__=None, reverse=False):
    heap = Heap(ls, item5obj_=item5obj_, item2val_=item2val_, key=key, __le__=__le__, reverse=reverse, obj_vs_item=True, applied__heapify=True)
    heap.heap_validate_()

######################
heap_sort_
heappushs_
heappops_
heappop_eqvs_
heap_validate_

heapify
heappush
heappop
heappushpop
heappoppush
heapreplace
merge
nlargest
nsmallest

__all__
######################
#copy from: /data/data/com.termux/files/usr/lib/python3.10/heapq.py
######################
r'''[[[
"""Heap queue algorithm (a.k.a. priority queue).

Heaps are arrays for which a[k] <= a[2*k+1] and a[k] <= a[2*k+2] for
all k, counting elements from 0.  For the sake of comparison,
non-existing elements are considered to be infinite.  The interesting
property of a heap is that a[0] is always its smallest element.

Usage:

heap = []            # creates an empty heap
heappush(le, heap, item) # pushes a new item on the heap
item = heappop(le, heap) # pops the smallest item from the heap
item = heap[0]       # smallest item on the heap without popping it
heapify(x)           # transforms list into a heap, in-place, in linear time
item = heapreplace(le, heap, item) # pops and returns smallest item, and adds
                               # new item; the heap size is unchanged

Our API differs from textbook heap algorithms as follows:

- We use 0-based indexing.  This makes the relationship between the
  index for a node and the indexes for its children slightly less
  obvious, but is more suitable since Python uses 0-based indexing.

- Our heappop() method returns the smallest item, not the largest.

These two make it possible to view the heap as a regular Python list
without surprises: heap[0] is the smallest item, and heap.sort()
maintains the heap invariant!
"""

# Original code by Kevin O'Connor, augmented by Tim Peters and Raymond Hettinger

__about__ = """Heap queues

[explanation by François Pinard]

Heaps are arrays for which a[k] <= a[2*k+1] and a[k] <= a[2*k+2] for
all k, counting elements from 0.  For the sake of comparison,
non-existing elements are considered to be infinite.  The interesting
property of a heap is that a[0] is always its smallest element.

The strange invariant above is meant to be an efficient memory
representation for a tournament.  The numbers below are `k', not a[k]:

                                   0

                  1                                 2

          3               4                5               6

      7       8       9       10      11      12      13      14

    15 16   17 18   19 20   21 22   23 24   25 26   27 28   29 30


In the tree above, each cell `k' is topping `2*k+1' and `2*k+2'.  In
a usual binary tournament we see in sports, each cell is the winner
over the two cells it tops, and we can trace the winner down the tree
to see all opponents s/he had.  However, in many computer applications
of such tournaments, we do not need to trace the history of a winner.
To be more memory efficient, when a winner is promoted, we try to
replace it by something else at a lower level, and the rule becomes
that a cell and the two cells it tops contain three different items,
but the top cell "wins" over the two topped cells.

If this heap invariant is protected at all time, index 0 is clearly
the overall winner.  The simplest algorithmic way to remove it and
find the "next" winner is to move some loser (let's say cell 30 in the
diagram above) into the 0 position, and then percolate this new 0 down
the tree, exchanging values, until the invariant is re-established.
This is clearly logarithmic on the total number of items in the tree.
By iterating over all items, you get an O(n ln n) sort.

A nice feature of this sort is that you can efficiently insert new
items while the sort is going on, provided that the inserted items are
not "better" than the last 0'th element you extracted.  This is
especially useful in simulation contexts, where the tree holds all
incoming events, and the "win" condition means the smallest scheduled
time.  When an event schedule other events for execution, they are
scheduled into the future, so they can easily go into the heap.  So, a
heap is a good structure for implementing schedulers (this is what I
used for my MIDI sequencer :-).

Various structures for implementing schedulers have been extensively
studied, and heaps are good for this, as they are reasonably speedy,
the speed is almost constant, and the worst case is not much different
than the average case.  However, there are other representations which
are more efficient overall, yet the worst cases might be terrible.

Heaps are also very useful in big disk sorts.  You most probably all
know that a big sort implies producing "runs" (which are pre-sorted
sequences, which size is usually related to the amount of CPU memory),
followed by a merging passes for these runs, which merging is often
very cleverly organised[1].  It is very important that the initial
sort produces the longest runs possible.  Tournaments are a good way
to that.  If, using all the memory available to hold a tournament, you
replace and percolate items that happen to fit the current run, you'll
produce runs which are twice the size of the memory for random input,
and much better for input fuzzily ordered.

Moreover, if you output the 0'th item on disk and get an input which
may not fit in the current tournament (because the value "wins" over
the last output value), it cannot fit in the heap, so the size of the
heap decreases.  The freed memory could be cleverly reused immediately
for progressively building a second heap, which grows at exactly the
same rate the first heap is melting.  When the first heap completely
vanishes, you switch heaps and start a new run.  Clever and quite
effective!

In a word, heaps are useful memory structures to know.  I use them in
a few applications, and I think it is good to keep a `heap' module
around. :-)

--------------------
[1] The disk balancing algorithms which are current, nowadays, are
more annoying than clever, and this is a consequence of the seeking
capabilities of the disks.  On devices which cannot seek, like big
tape drives, the story was quite different, and one had to be very
clever to ensure (far in advance) that each tape movement will be the
most effective possible (that is, will best participate at
"progressing" the merge).  Some tapes were even able to read
backwards, and this was also used to avoid the rewinding time.
Believe me, real good tape sorts were quite spectacular to watch!
From all times, sorting has always been a Great Art! :-)
"""

#]]]'''#'''
if __name__ == "__main__":

    import doctest # pragma: no cover
    print(doctest.testmod()) # pragma: no cover
######################



from seed.for_libs.for_heapq import iter_merge_sorted_iterables_, merge

from seed.for_libs.for_heapq import extract_kth_smallest_elements_, nsmallest, nlargest

from seed.for_libs.for_heapq import heap_sort_

from seed.for_libs.for_heapq import heappushs_, heappops_, heappop_eqvs_, heapify, heappush, heappop, heappushpop, heappoppush, heapreplace


from seed.for_libs.for_heapq import Heap, std____key__le__reverse_

from seed.for_libs.for_heapq import heap_validate_, ValidateFail__not_heap

from seed.for_libs.for_heapq import to_iparent_, to_ichildren_, to_ichildren__


from seed.for_libs.for_heapq import *
