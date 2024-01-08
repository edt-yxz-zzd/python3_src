

'''
wrapper for py.heapq
    now:HeapOverrideOrdering
    ########
    ++key
    ++__le__
    ++reverse
    ########

view ../../python3_src/seed/for_libs/for_heapq.py
    more powerful version than py.heapq
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



'''

__all__ = '''
    Heap
    HeapWithKey
    HeapOverrideOrdering
    '''.split()

from collections.abc import Sequence
from heapq import heapify, heappop, heappushpop, heappush, heapreplace
from seed.types.WithKey import WithSortKey, get_obj_with
from seed.special_funcs import identity_func
from abc import ABCMeta, abstractmethod

from seed.types.OverrideOrdering import OrderingSetting, OverrideOrdering
#class OrderingSetting:
#    def __init__(sf, key, __le__, reverse, /):
#class OverrideOrdering:
#    def __init__(sf, ordering_setting, obj, /):

class IHeap(metaclass=ABCMeta):
    '''heap

Obj
Heap = [Item]
Key = Item
obj2item :: Obj->Item
item2obj :: Item->Obj
'''
    @abstractmethod
    def obj2item(self, obj, /):
        'obj -> heap_item'
    @abstractmethod
    def item2obj(self, heap_item, /):
        'heap_item -> obj'

    def __init__(self, iterable, *, sorted, copy, are_heap_items):
        '''
sorted - iterable is sorted?
            if False, call heapify
copy - to copy input?
            if False, use iterable directly, and it should be sequence
are_heap_items - input are heap items or objs?
            if False, call obj2item on input
obj2item - (obj->item)
item2obj - (item->obj)
'''
        if copy:
            if are_heap_items:
                seq = list(iterable)
            else:
                seq = list(map(self.obj2item, iterable))
        else:
            assert isinstance(iterable, Sequence)
            seq = iterable
            if not are_heap_items:
                for i in range(len(seq)):
                    seq[i] = self.obj2item(seq[i])
        if not sorted:
            heapify(seq)
        self.__heap = seq

    @property
    def the_heap(self):
        return self.__heap


    def __len__(self):
        return len(self.the_heap)
    def pop_eqvs(self):
        hp = self.the_heap
        heap_item0 = hp[0]
        obj = self.pop()
        eqvs = [obj]
        while hp and heap_item0 == hp[0]:
            obj = self.pop()
            eqvs.append(obj)
        return eqvs
    def pop(self):
        item = heappop(self.the_heap)
            # ^IndexError
        return self.item2obj(item)
    def peek(self):
        item = self.the_heap[0]
            # ^IndexError
        return self.item2obj(item)
    def push(self, obj):
        item = self.obj2item(obj)
        heappush(self.the_heap, item)
    def push_then_pop(self, obj):
        item = self.obj2item(obj)
        item = heappushpop(self.the_heap, item)
        return self.item2obj(item)
    def pop_then_push(self, obj):
        item = self.obj2item(obj)
        item = heapreplace(self.the_heap, item)
        return self.item2obj(item)


class Heap(IHeap):
    def __init__(self, iterable, *
            , sorted=False, copy=False, are_heap_items=True
            , obj2item=None, item2obj=None):
        '''
sorted - iterable is sorted?
            if False, call heapify
copy - to copy input?
            if False, use iterable directly, and it should be sequence
are_heap_items - input are heap items or objs?
            if False, call obj2item on input
obj2item - (obj->item)
item2obj - (item->obj)
'''
        self.__obj2item = obj2item if obj2item is not None else identity_func
        self.__item2obj = item2obj if item2obj is not None else identity_func
        are_heap_items = are_heap_items or obj2item is None
        ## assert __obj2item before super.__init__
        super().__init__(iterable
            , sorted=sorted, copy=copy, are_heap_items=are_heap_items)
    if 0:
        #@override
        def obj2item(self, obj, /):
            'obj -> heap_item'
        #@override
        def item2obj(self, heap_item, /):
            'heap_item -> obj'
    @property
    def obj2item(self):
        return self.__obj2item
    @property
    def item2obj(self):
        return self.__item2obj



class HeapWithKey(IHeap):
    def __init__(self, obj2key, iterable, *
            , sorted=False, copy=True, are_heap_items=False):
        self.__obj2key = obj2key if obj2key is not None else identity_func
        ### assign __obj2key first to use __obj2item
        super().__init__(iterable
            , sorted=sorted, copy=copy, are_heap_items=are_heap_items)
    #@override
    def obj2item(self, obj, /):
        'obj -> heap_item'
        heap_item = WithSortKey(self.__obj2key(obj), obj)
        return heap_item
    #@override
    def item2obj(self, heap_item, /):
        'heap_item -> obj'
        return get_obj_with(heap_item)

class HeapOverrideOrdering(IHeap):
    def __init__(self, iterable, *
            , key=None, __le__=None, reverse=False
            , sorted=False, copy=True, are_heap_items=False):
        ordering_setting = OrderingSetting(key, __le__, reverse)
        sf._ordering_setting = ordering_setting
        ### assign _ordering_setting first to use obj2item
        super().__init__(iterable
            , sorted=sorted, copy=copy, are_heap_items=are_heap_items)
    @property
    def ordering_setting(self):
        return self._ordering_setting

    #@override
    def obj2item(self, obj, /):
        'obj -> heap_item'
        heap_item = OverrideOrdering(sf.ordering_setting, obj)
        return heap_item
    #@override
    def item2obj(self, heap_item, /):
        'heap_item -> obj'
        return heap_item.obj


from seed.types.Heap import IHeap
from seed.types.Heap import Heap, HeapWithKey
from seed.types.Heap import *
