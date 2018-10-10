
from ..abc import abstractmethod, override, not_implemented
from .IHeapOps_ABC import IHeapOps_ABC

import unittest
from unittest import TestCase


class Try_IHeapOps_ABC(IHeapOps_ABC):
    '''

override:
    `wrap_heap
    `wrap
    `unwrap
    `wrapped_obj2key
    `can_be_parent_key_of
data:
    heap = {'idx2wrapped_obj':wrapped_obj_seq, ...}
    wrapped_obj = (idx, unwrapped_obj)
    unwrapped_obj :: container
    key = len/int
    __le__ = (>=)
'''
    __slots__ = ()
    #################
    @override
    def wrap_heap(ops, heap):
        # heap -> wrapped_obj_seq
        #   get seq from heap-obj or wrap mutable-seq-view above heap-obj
        wrapped_obj_seq = heap['idx2wrapped_obj']
        return wrapped_obj_seq
    @override
    def wrap(ops, unwrapped_obj, idx):
        # unwrapped_obj -> UInt -> wrapped_obj
        # echo
        wrapped_obj = (idx, unwrapped_obj)
        return wrapped_obj
    @override
    def unwrap(ops, wrapped_obj):
        # wrapped_obj -> unwrapped_obj
        # echo
        idx, unwrapped_obj = wrapped_obj
        return unwrapped_obj
    @override
    def wrapped_obj2key(ops, wrapped_obj):
        # wrapped_obj -> key
        # echo
        unwrapped_obj = ops.unwrap(wrapped_obj)
        try:
            key = len(unwrapped_obj)
        except (TypeError, AttributeError):
            key = int(unwrapped_obj)
        return key
    @override
    def can_be_parent_key_of(ops, parent_wrapped_key, child_wrapped_key):
        # key -> key -> Bool
        # __le__
        return parent_wrapped_key >= child_wrapped_key

    @override
    def __eq__(ops, other):
        return type(ops) is type(other)
    @override
    def __hash__(ops):
        return hash((type(ops),))

class Test_IHeapOps_ABC(TestCase):
    def __init__(self, *args, **kwargs):
        self.heap_ops = Try_IHeapOps_ABC()
        self.heap = {}
        super().__init__(*args, **kwargs)

    #tearDown()
    @property
    def wrapped_obj_seq(self):
        return self.heap['idx2wrapped_obj']
    @wrapped_obj_seq.setter
    def wrapped_obj_seq(self, wrapped_obj_seq):
        self.heap['idx2wrapped_obj'] = wrapped_obj_seq

    def setUp(self):
        self.wrapped_obj_seq = []
    def test_size(self):
        heap = self.heap
        heap_ops = self.heap_ops
        is_empty = heap_ops.is_empty
        get_size = heap_ops.get_size

        self.wrapped_obj_seq = []
        self.assertTrue(is_empty(heap))
        self.assertEqual(get_size(heap), 0)

        self.wrapped_obj_seq = [1,2,3,4]
        self.assertFalse(is_empty(heap))
        self.assertEqual(get_size(heap), 4)

    def test__make_heap_inplace(self):
        heap = self.heap
        heap_ops = self.heap_ops
        is_empty = heap_ops.is_empty
        get_size = heap_ops.get_size

        self.wrapped_obj_seq = []
        heap_ops.make_heap_inplace(heap)
        self.assertTrue(is_empty(heap))
        self.assertEqual(get_size(heap), 0)
        self.assertEqual(self.wrapped_obj_seq, [])


        def make_wrapped_obj_seq(ls):
            return [(None, x) for x in ls]
        self.wrapped_obj_seq = make_wrapped_obj_seq([1,2,3,4])
        heap_ops.make_heap_inplace(heap)
        self.assertFalse(is_empty(heap))
        self.assertEqual(get_size(heap), 4)
        self.assertEqual(self.wrapped_obj_seq, make_wrapped_obj_seq([4,2,3,1]))


        self.wrapped_obj_seq = make_wrapped_obj_seq([1,2,[1],4])
        heap_ops.make_heap_inplace(heap)
        self.assertFalse(is_empty(heap))
        self.assertEqual(get_size(heap), 4)
        self.assertEqual(self.wrapped_obj_seq, make_wrapped_obj_seq([4,2,[1],1]))

    def test__replace_at(self):
        heap = self.heap
        heap_ops = self.heap_ops
        is_empty = heap_ops.is_empty
        get_size = heap_ops.get_size
        replace_at = heap_ops.replace_at

        self.wrapped_obj_seq = []
        with self.assertRaises((IndexError, AssertionError)):
            replace_at(heap, 0, [1], wrapped=False)
        self.assertTrue(is_empty(heap))
        self.assertEqual(get_size(heap), 0)
        self.assertEqual(self.wrapped_obj_seq, [])


        def make_wrapped_obj_seq(ls):
            return [(None, x) for x in ls]
        self.wrapped_obj_seq = make_wrapped_obj_seq([4,2,3,1])
        self.assertTrue(heap_ops.basic__verify_heap(self.wrapped_obj_seq))
        self.assertEqual(1, replace_at(heap, 1, (None, '22'), wrapped=True))
        self.assertFalse(is_empty(heap))
        self.assertEqual(get_size(heap), 4)
        self.assertEqual(self.wrapped_obj_seq, make_wrapped_obj_seq([4,'22',3,1]))


        self.wrapped_obj_seq = make_wrapped_obj_seq([4,2,3,1])
        self.assertTrue(heap_ops.basic__verify_heap(self.wrapped_obj_seq))
        self.assertEqual(0, replace_at(heap, 3, (None, 5), wrapped=True))
        self.assertFalse(is_empty(heap))
        self.assertEqual(get_size(heap), 4)
        self.assertEqual(self.wrapped_obj_seq, make_wrapped_obj_seq([5,4,3,2]))


        self.wrapped_obj_seq = make_wrapped_obj_seq([4,2,3,1])
        self.assertTrue(heap_ops.basic__verify_heap(self.wrapped_obj_seq))
        self.assertEqual(2, replace_at(heap, 0, (None, 0), wrapped=True))
        self.assertFalse(is_empty(heap))
        self.assertEqual(get_size(heap), 4)
        self.assertEqual(self.wrapped_obj_seq, make_wrapped_obj_seq([3,2,0,1]))



        self.wrapped_obj_seq = make_wrapped_obj_seq([4,2,3,1])
        self.assertTrue(heap_ops.basic__verify_heap(self.wrapped_obj_seq))
        self.assertEqual(3, replace_at(heap, 1, (None, 0), wrapped=True))
        self.assertFalse(is_empty(heap))
        self.assertEqual(get_size(heap), 4)
        self.assertEqual(self.wrapped_obj_seq, make_wrapped_obj_seq([4,1,3,0]))



        self.wrapped_obj_seq = make_wrapped_obj_seq([4,2,3,1])
        self.assertTrue(heap_ops.basic__verify_heap(self.wrapped_obj_seq))
        self.assertEqual(0, replace_at(heap, 1, (None, 5), wrapped=True))
        self.assertFalse(is_empty(heap))
        self.assertEqual(get_size(heap), 4)
        self.assertEqual(self.wrapped_obj_seq, make_wrapped_obj_seq([5,4,3,1]))


    def test__pop_then_push(self):
        heap = self.heap
        heap_ops = self.heap_ops
        is_empty = heap_ops.is_empty
        get_size = heap_ops.get_size
        pop_then_push = heap_ops.pop_then_push

        self.wrapped_obj_seq = []
        with self.assertRaises((IndexError, AssertionError)):
            pop_then_push(heap, [1], wrapped=False)
        self.assertTrue(is_empty(heap))
        self.assertEqual(get_size(heap), 0)
        self.assertEqual(self.wrapped_obj_seq, [])


        def make_wrapped_obj_seq(ls):
            return [(None, x) for x in ls]
        self.wrapped_obj_seq = make_wrapped_obj_seq([4,2,3,1])
        self.assertTrue(heap_ops.basic__verify_heap(self.wrapped_obj_seq))
        self.assertEqual((None,4), pop_then_push(heap, (None, '22'), wrapped=True))
        self.assertFalse(is_empty(heap))
        self.assertEqual(get_size(heap), 4)
        self.assertEqual(self.wrapped_obj_seq, make_wrapped_obj_seq([3,2,'22',1]))


        self.wrapped_obj_seq = make_wrapped_obj_seq([4,2,3,1])
        self.assertTrue(heap_ops.basic__verify_heap(self.wrapped_obj_seq))
        self.assertEqual((None,4), pop_then_push(heap, (None, 5), wrapped=True))
        self.assertFalse(is_empty(heap))
        self.assertEqual(get_size(heap), 4)
        self.assertEqual(self.wrapped_obj_seq, make_wrapped_obj_seq([5,2,3,1]))

    def test__push_then_pop(self):
        heap = self.heap
        heap_ops = self.heap_ops
        is_empty = heap_ops.is_empty
        get_size = heap_ops.get_size
        push_then_pop = heap_ops.push_then_pop

        self.wrapped_obj_seq = []
        self.assertEqual([1], push_then_pop(heap, [1], wrapped=False))
        self.assertEqual((...,[1]), push_then_pop(heap, (...,[1]), wrapped=True))
        self.assertTrue(is_empty(heap))
        self.assertEqual(get_size(heap), 0)
        self.assertEqual(self.wrapped_obj_seq, [])


        def make_wrapped_obj_seq(ls):
            return [(None, x) for x in ls]
        self.wrapped_obj_seq = make_wrapped_obj_seq([4,2,3,1])
        self.assertTrue(heap_ops.basic__verify_heap(self.wrapped_obj_seq))
        self.assertEqual((None,4), push_then_pop(heap, (None, '22'), wrapped=True))
        self.assertFalse(is_empty(heap))
        self.assertEqual(get_size(heap), 4)
        self.assertEqual(self.wrapped_obj_seq, make_wrapped_obj_seq([3,2,'22',1]))


        self.wrapped_obj_seq = make_wrapped_obj_seq([4,2,3,1])
        self.assertTrue(heap_ops.basic__verify_heap(self.wrapped_obj_seq))
        self.assertEqual((None,5), push_then_pop(heap, (None, 5), wrapped=True))
        self.assertFalse(is_empty(heap))
        self.assertEqual(get_size(heap), 4)
        self.assertEqual(self.wrapped_obj_seq, make_wrapped_obj_seq([4,2,3,1]))


        self.wrapped_obj_seq = make_wrapped_obj_seq([4,2,3,1])
        self.assertTrue(heap_ops.basic__verify_heap(self.wrapped_obj_seq))
        self.assertEqual((None,'4444'), push_then_pop(heap, (None, '4444'), wrapped=True))
        self.assertFalse(is_empty(heap))
        self.assertEqual(get_size(heap), 4)
        self.assertEqual(self.wrapped_obj_seq, make_wrapped_obj_seq([4,2,3,1]))

    def test__pop(self):
        heap = self.heap
        heap_ops = self.heap_ops
        is_empty = heap_ops.is_empty
        get_size = heap_ops.get_size
        pop = heap_ops.pop

        self.wrapped_obj_seq = []
        with self.assertRaises((IndexError, AssertionError)):
            pop(heap, wrapped=False)
        self.assertTrue(is_empty(heap))
        self.assertEqual(get_size(heap), 0)
        self.assertEqual(self.wrapped_obj_seq, [])


        def make_wrapped_obj_seq(ls):
            return [(None, x) for x in ls]
        self.wrapped_obj_seq = make_wrapped_obj_seq([4,2,3,1])
        self.assertTrue(heap_ops.basic__verify_heap(self.wrapped_obj_seq))
        self.assertEqual((None,4), pop(heap, wrapped=True))
        self.assertFalse(is_empty(heap))
        self.assertEqual(get_size(heap), 3)
        self.assertEqual(self.wrapped_obj_seq, make_wrapped_obj_seq([3,2,1]))
        self.assertEqual(3, pop(heap, wrapped=False))
        self.assertEqual(self.wrapped_obj_seq, make_wrapped_obj_seq([2,1]))
        self.assertEqual(2, pop(heap, wrapped=False))
        self.assertEqual(self.wrapped_obj_seq, make_wrapped_obj_seq([1]))
        self.assertEqual(1, pop(heap, wrapped=False))
        self.assertEqual(self.wrapped_obj_seq, [])
        self.assertTrue(is_empty(heap))


    def test__push(self):
        heap = self.heap
        heap_ops = self.heap_ops
        is_empty = heap_ops.is_empty
        get_size = heap_ops.get_size
        push = heap_ops.push

        self.wrapped_obj_seq = []
        self.assertEqual(0, push(heap, [1], wrapped=False))
        self.assertFalse(is_empty(heap))
        self.assertEqual(get_size(heap), 1)
        self.assertEqual(self.wrapped_obj_seq, [(0,[1])])


        def make_wrapped_obj_seq(ls):
            return [(None, x) for x in ls]
        self.wrapped_obj_seq = make_wrapped_obj_seq([4,2,3,1])
        self.assertTrue(heap_ops.basic__verify_heap(self.wrapped_obj_seq))
        self.assertEqual(4, push(heap, (None,'1'), wrapped=True))
        self.assertFalse(is_empty(heap))
        self.assertEqual(get_size(heap), 5)
        self.assertEqual(self.wrapped_obj_seq, make_wrapped_obj_seq([4,2,3,1,'1']))


        self.wrapped_obj_seq = make_wrapped_obj_seq([4,2,3,1])
        self.assertTrue(heap_ops.basic__verify_heap(self.wrapped_obj_seq))
        self.assertEqual(1, push(heap, (None,'333'), wrapped=True))
        self.assertFalse(is_empty(heap))
        self.assertEqual(get_size(heap), 5)
        self.assertEqual(self.wrapped_obj_seq, make_wrapped_obj_seq([4,'333',3,1,2]))

        self.wrapped_obj_seq = make_wrapped_obj_seq([4,2,3,1])
        self.assertTrue(heap_ops.basic__verify_heap(self.wrapped_obj_seq))
        self.assertEqual(1, push(heap, (None,'4444'), wrapped=True))
        self.assertFalse(is_empty(heap))
        self.assertEqual(get_size(heap), 5)
        self.assertEqual(self.wrapped_obj_seq, make_wrapped_obj_seq([4,'4444',3,1,2]))




        self.wrapped_obj_seq = make_wrapped_obj_seq([4,2,3,1])
        self.assertTrue(heap_ops.basic__verify_heap(self.wrapped_obj_seq))
        self.assertEqual(0, push(heap, (None,5), wrapped=True))
        self.assertFalse(is_empty(heap))
        self.assertEqual(get_size(heap), 5)
        self.assertEqual(self.wrapped_obj_seq, make_wrapped_obj_seq([5,4,3,1,2]))




    def test__delete_at(self):
        heap = self.heap
        heap_ops = self.heap_ops
        is_empty = heap_ops.is_empty
        get_size = heap_ops.get_size
        delete_at = heap_ops.delete_at

        self.wrapped_obj_seq = []
        with self.assertRaises((IndexError, AssertionError)):
            delete_at(heap, 0, wrapped=False)
        self.assertTrue(is_empty(heap))
        self.assertEqual(get_size(heap), 0)
        self.assertEqual(self.wrapped_obj_seq, [])


        def make_wrapped_obj_seq(ls):
            return [(None, x) for x in ls]
        self.wrapped_obj_seq = make_wrapped_obj_seq([4,2,3,1])
        self.assertTrue(heap_ops.basic__verify_heap(self.wrapped_obj_seq))
        self.assertEqual((None,4), delete_at(heap, 0, wrapped=True))
        self.assertFalse(is_empty(heap))
        self.assertEqual(get_size(heap), 3)
        self.assertEqual(self.wrapped_obj_seq, make_wrapped_obj_seq([3,2,1]))

        self.wrapped_obj_seq = make_wrapped_obj_seq([4,2,3,1])
        self.assertTrue(heap_ops.basic__verify_heap(self.wrapped_obj_seq))
        self.assertEqual(2, delete_at(heap, 1, wrapped=False))
        self.assertFalse(is_empty(heap))
        self.assertEqual(get_size(heap), 3)
        self.assertEqual(self.wrapped_obj_seq, make_wrapped_obj_seq([4,1,3]))

        self.wrapped_obj_seq = make_wrapped_obj_seq([4,2,3,1])
        self.assertTrue(heap_ops.basic__verify_heap(self.wrapped_obj_seq))
        self.assertEqual(3, delete_at(heap, 2, wrapped=False))
        self.assertFalse(is_empty(heap))
        self.assertEqual(get_size(heap), 3)
        self.assertEqual(self.wrapped_obj_seq, make_wrapped_obj_seq([4,2,1]))


        self.wrapped_obj_seq = make_wrapped_obj_seq([4,2,3,1])
        self.assertTrue(heap_ops.basic__verify_heap(self.wrapped_obj_seq))
        self.assertEqual(1, delete_at(heap, 3, wrapped=False))
        self.assertFalse(is_empty(heap))
        self.assertEqual(get_size(heap), 3)
        self.assertEqual(self.wrapped_obj_seq, make_wrapped_obj_seq([4,2,3]))





        delete_at



    def test__peek_at(self):
        heap = self.heap
        heap_ops = self.heap_ops
        is_empty = heap_ops.is_empty
        get_size = heap_ops.get_size
        peek_at = heap_ops.peek_at

        self.wrapped_obj_seq = []
        with self.assertRaises((IndexError, AssertionError)):
            peek_at(heap, 0, wrapped=False)
        self.assertTrue(is_empty(heap))
        self.assertEqual(get_size(heap), 0)
        self.assertEqual(self.wrapped_obj_seq, [])


        def make_wrapped_obj_seq(ls):
            return [(None, x) for x in ls]
        self.wrapped_obj_seq = make_wrapped_obj_seq([4,2,3,1])
        self.assertTrue(heap_ops.basic__verify_heap(self.wrapped_obj_seq))
        self.assertEqual((None,4), peek_at(heap, 0, wrapped=True))
        self.assertEqual(4, peek_at(heap, 0, wrapped=False))
        self.assertEqual(2, peek_at(heap, 1, wrapped=False))
        self.assertEqual(3, peek_at(heap, 2, wrapped=False))
        self.assertEqual(1, peek_at(heap, 3, wrapped=False))
        self.assertFalse(is_empty(heap))
        self.assertEqual(get_size(heap), 4)
        self.assertEqual(self.wrapped_obj_seq, make_wrapped_obj_seq([4,2,3,1]))


if __name__ == '__main__':
    unittest.main()

