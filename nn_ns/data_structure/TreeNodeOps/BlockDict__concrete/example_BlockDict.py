
example_BlockDict = r'''
input:
    mkBlockDict :: block_dict_key_ops -> (Iter a = None) -> (is_block_items=False) -> BlockDict
>>> callable(mkBlockDict)
True
>>> from ..OtherOps.TotalOrderingOps import python_total_key_ops
>>> from ..OtherOps.EqOps import python_eq_key_ops
>>> from ..BlockDictOps__concrete.theUInt_as_BlockDictKeyOps import theUInt_as_BlockDictKeyOps
>>> UIntBlockDict = lambda *args, **kwargs: mkBlockDict(theUInt_as_BlockDictKeyOps, *args, **kwargs)
>>> block_dict_key_ops = theUInt_as_BlockDictKeyOps

>>> m = UIntBlockDict()
>>> bool(m)
False

>>> m = UIntBlockDict([(1, 'a')])
>>> bool(m)
True
>>> m.get_num_block_keys()
1




# dict_key
>>> m = UIntBlockDict([(1, 'a'), (3, 'c')])
>>> m.get_num_block_keys()
2
>>> m = UIntBlockDict([(1, 'a'), (3, 'c'), (2, 'b')])
>>> m.get_num_block_keys()
3
>>> list(m.iter_dict_values())
['a', 'b', 'c']
>>> list(m.iter_dict_values(reverse=True))
['c', 'b', 'a']




# m = {1:'b', 3:'b'}
>>> m = UIntBlockDict([(1, 'b'), (3, 'b')])
>>> m.get_num_block_keys()
2



>>> the0 = block_dict_key_ops.mkTheKey(0)
>>> the1 = block_dict_key_ops.mkTheKey(1)
>>> the2 = block_dict_key_ops.mkTheKey(2)
>>> the3 = block_dict_key_ops.mkTheKey(3)
>>> the4 = block_dict_key_ops.mkTheKey(4)
>>> the5 = block_dict_key_ops.mkTheKey(5)
>>> the6 = block_dict_key_ops.mkTheKey(6)
>>> the7 = block_dict_key_ops.mkTheKey(7)





# m = {(1,1):'b', (3,3):'b', (5,5):'b', (7,7):'b'}
>>> m = UIntBlockDict({1:'b', 3:'b', 5:'b', 7:'b'}.items())
>>> [*ls] = m.block_key2iter_block_items((the2, the5))
>>> len(ls)
2
>>> ls # doctest: +ELLIPSIS
[(((..., 3), (..., 3)), 'b'), (((..., 5), (..., 5)), 'b')]

# block_key2iter_block_items
>>> [*ls] = m.block_key2iter_block_items((the2, the5), reverse=True)
>>> len(ls)
2
>>> ls # doctest: +ELLIPSIS
[(((..., 5), (..., 5)), 'b'), (((..., 3), (..., 3)), 'b')]

#################### ''' r'''


>>> the0 = block_dict_key_ops.mkTheKey(0)
>>> the1 = block_dict_key_ops.mkTheKey(1)
>>> the2 = block_dict_key_ops.mkTheKey(2)
>>> the3 = block_dict_key_ops.mkTheKey(3)
>>> the4 = block_dict_key_ops.mkTheKey(4)
>>> the5 = block_dict_key_ops.mkTheKey(5)
>>> the6 = block_dict_key_ops.mkTheKey(6)
>>> the7 = block_dict_key_ops.mkTheKey(7)


>>> empty = UIntBlockDict()
>>> m = UIntBlockDict([(1, 'a'), (3, 'b'), (4, 'b'), (5, 'c'), (0, 'k')])

>>> m.block_dict_key_ops is m.get_block_dict_key_ops()
True
>>> m.block_key2block_items((the1, the3)) == [((the1, the1), 'a'), ((the3, the3), 'b')]
True
>>> m.block_key2block_items((the1, the3), reverse=True) == [((the3, the3), 'b'), ((the1, the1), 'a')]
True

>>> empty.block_key2block_items((the1, the5))
[]
>>> [*m.block_key2iter_block_items((the1, the5))] == [((the1, the1), 'a'), ((the3, the4), 'b'), ((the5, the5), 'c')]
True
>>> [*m.block_key2iter_block_items((the5, the1))]
[]

>>> t = m.copy()
>>> t == empty
False
>>> t == m
True
>>> t = m.self_make_empty_block_dict()
>>> t.get_num_block_keys()
0
>>> t == empty
True
>>> m.get_num_block_keys()
4

>>> m == m.copy()
True
>>> m.dict_key2block_items(2)
[]
>>> m.dict_key2block_items(1) == [((the1, the1), 'a')]
True
>>> m.dict_value_eq('a', 'a')
True
>>> m.dict_value_eq('a', 'b')
False
>>> m.dict_value_eq is m.eq_dict_value_ops.eq
True

>>> t = UIntBlockDict([(5, 'c'), (0, 'k')])
>>> t.get_num_block_keys()
2
>>> [*t.iter_block_items()] == [((the0, the0), 'k'), ((the5, the5), 'c')]
True


>>> m.eq_dict_value_ops is m.get_eq_dict_value_ops()
True
>>> m.get(4)
'b'
>>> m.get(6)
>>> m.get_block_dict_key_ops() is block_dict_key_ops
True
>>> m.get_eq_dict_value_ops() is python_eq_key_ops
True

>>> empty.get_num_block_keys()
0
>>> m.get_num_block_keys()
4

>>> m.get_total_dict_key_ops() is python_total_key_ops
True

>>> [*empty.iter_block_items()]
[]
>>> [*m.iter_block_items()] == [((the0, the0), 'k'), ((the1, the1), 'a'), ((the3, the4), 'b'), ((the5, the5), 'c')]
True
>>> [*m.iter_block_items()] == [*reversed([*m.iter_block_items(reverse=True)])]
True
>>> [*m.iter_block_keys()] == [(the0, the0), (the1, the1), (the3, the4), (the5, the5)]
True
>>> [*m.iter_dict_values()] == list('kabc')
True
>>> m.list_all_touch_or_overlap_block_items((the1, the3), False) == [((the0, the0), 'k'), ((the1, the1), 'a'), ((the3, the4), 'b')]
True

>>> m.mkSingletonRange(1) == (the1, the1)
True




>>> 2 not in m
True
>>> 3 in m
True


>>> t = UIntBlockDict([(1, 'a'), (3, 'b'), (4, 'b'), (5, 'c'), (0, 'k'), (2, 'a'), (3, 'a')])
>>> t.get_num_block_keys()
4
>>> t.block_key2block_items(((the0, block_dict_key_ops.getTheMaxKeyEx())), reverse=True) == [*t.iter_block_items(reverse=True)] == [((the5, the5), 'c'), ((the4, the4), 'b'), ((the1, the3), 'a'), ((the0, the0), 'k')]
True
>>> t.block_key2block_items(((the0, block_dict_key_ops.getTheMaxKeyEx()))) == [*t.iter_block_items()] == [((the0, the0), 'k'), ((the1, the3), 'a'), ((the4, the4), 'b'), ((the5, the5), 'c')]
True



>>> m.total_dict_key_ops is m.get_total_dict_key_ops()
True



__bool__
>>> bool(empty)
False
>>> bool(m)
True

__contains__
>>> 2 in empty
False
>>> 2 in m
False
>>> 1 in m
True



__eq__
>>> empty == m
False
>>> empty == empty
True
>>> m == m
True
>>> m == m.copy()
True

__getitem__
>>> m[1]
'a'

__ne__
>>> m != empty
True
>>> m != m
False
>>> m != m.copy()
False






self_make_empty_block_dict
self_make_block_dict_from_items
self_make_block_dict_from_block_items
self_make_block_dict_from_iterable
>>> m.self_make_empty_block_dict() == empty
True
>>> m.self_make_block_dict_from_items([]) == empty
True
>>> m.self_make_block_dict_from_block_items([]) == empty
True
>>> m.self_make_block_dict_from_items([(1,'a'), (0, 'k'), (3, 'b'), (5, 'c'), (4, 'b')]) == m
True
>>> m.self_make_block_dict_from_block_items(m.iter_block_items()) == m
True

>>> m.self_make_block_dict_from_iterable([], False) == empty
True
>>> m.self_make_block_dict_from_iterable([], True) == empty
True
>>> m.self_make_block_dict_from_iterable([(1,'a'), (0, 'k'), (3, 'b'), (5, 'c'), (4, 'b')], False) == m
True
>>> m.self_make_block_dict_from_iterable(m.iter_block_items(), True) == m
True




>>> m.list_all_touch_or_overlap_block_items((the1, the4), False) == [*m.iter_block_items()]
True
>>> m.list_all_touch_or_overlap_block_items((the1, the3), False) == [*m.iter_block_items()][:-1]
True
>>> m.list_all_touch_or_overlap_block_items((the2, the4), False) == [*m.iter_block_items()][1:]
True

>>> m.list_all_touch_or_overlap_block_items((the1, the4), False, reverse=True) == [*m.iter_block_items()][::-1]
True
>>> m.list_all_touch_or_overlap_block_items((the1, the3), False, reverse=True) == [*m.iter_block_items()][-2::-1]
True
>>> m.list_all_touch_or_overlap_block_items((the2, the4), False, reverse=True) == [*m.iter_block_items()][:0:-1]
True


>>> m.list_all_touch_or_overlap_block_items((the1, the4), True) == [*m.iter_block_items()][1:-1]
True
>>> m.list_all_touch_or_overlap_block_items((the1, the3), True) == [*m.iter_block_items()][1:-1]
True
>>> m.list_all_touch_or_overlap_block_items((the2, the4), True) == [*m.iter_block_items()][2:-1]
True


>>> m.list_all_touch_or_overlap_block_items((the4, the1), False)
[]
>>> m.list_all_touch_or_overlap_block_items((the1, the4), True) == [*m.iter_all_touch_or_overlap_block_items((the1, the4), True)]
True
>>> m.list_all_touch_or_overlap_block_items((the1, the4), False) == [*m.iter_all_touch_or_overlap_block_items((the1, the4), False)]
True


>>> m.list_all_touch_or_overlap_block_items((the0, the0), True) == [((the0, the0), 'k')]
True
>>> m.block_dict_key_ops.eqRange((the0, the0), (the0, the0))
True


is_one_piece_block_key
is_exactly_block_key
>>> m == UIntBlockDict([(1, 'a'), (3, 'b'), (4, 'b'), (5, 'c'), (0, 'k')])
True
>>> m.is_exactly_block_key((the0, the1))
False
>>> m.is_exactly_block_key((the0, the0))
True
>>> m.is_exactly_block_key((the3, the3))
False
>>> m.is_exactly_block_key((the3, the4))
True
>>> m.is_exactly_block_key((the3, the5))
False
>>> m.is_exactly_block_key((the2, the4))
False
>>> m.is_exactly_block_key((the2, the2))
False
>>> m.is_exactly_block_key((the2, the1))
False

>>> m.is_one_piece_block_key((the0, the1))
False
>>> m.is_one_piece_block_key((the0, the0))
True
>>> m.is_one_piece_block_key((the3, the3))
True
>>> m.is_one_piece_block_key((the3, the4))
True
>>> m.is_one_piece_block_key((the3, the5))
False
>>> m.is_one_piece_block_key((the2, the4))
False
>>> m.is_one_piece_block_key((the2, the2))
False
>>> m.is_one_piece_block_key((the2, the1))
False




>>> m == UIntBlockDict([(1, 'a'), (3, 'b'), (4, 'b'), (5, 'c'), (0, 'k')])
True
>>> m.index_block_item_at(0) == ((the0, the0), 'k')
True
>>> m.index_block_item_at(1) == ((the1, the1), 'a')
True
>>> m.index_block_item_at(2) == ((the3, the4), 'b')
True
>>> m.index_block_item_at(3) == ((the5, the5), 'c')
True
>>> m.index_block_item_at(4)
Traceback (most recent call last):
    ...
IndexError
>>> m.index_block_item_at(3) == m.index_block_item_at(-1)
True
>>> m.index_block_item_at(2) == m.index_block_item_at(-2)
True
>>> m.index_block_item_at(1) == m.index_block_item_at(-3)
True
>>> m.index_block_item_at(0) == m.index_block_item_at(-4)
True
>>> m.index_block_item_at(-5)
Traceback (most recent call last):
    ...
IndexError

>>> m.get_first_block_item() == m.index_block_item_at(0)
True
>>> m.get_first_block_item() == m.get_first_or_last_block_item(False)
True
>>> m.get_last_block_item() == m.index_block_item_at(-1)
True
>>> m.get_last_block_item() == m.get_first_or_last_block_item(True)
True


>>> empty.get_first_or_last_block_item(True)
Traceback (most recent call last):
    ...
IndexError
>>> empty.get_first_or_last_block_item(False)
Traceback (most recent call last):
    ...
IndexError
>>> empty.get_first_block_item()
Traceback (most recent call last):
    ...
IndexError
>>> empty.get_last_block_item()
Traceback (most recent call last):
    ...
IndexError



>>> the_inf = block_dict_key_ops.getTheMaxKeyEx()
>>> whole = m.self_make_whole_block_dict(None)
>>> bool(whole)
True
>>> whole.get_num_block_keys()
1
>>> [*whole.iter_block_items()] == [((the0, the_inf), None)]
True

>>> empty.self_make_complement_block_dict(lambda _: None) == whole
True
>>> whole.self_make_complement_block_dict(lambda _:None) == empty
True

>>> m == UIntBlockDict([(1, 'a'), (3, 'b'), (4, 'b'), (5, 'c'), (0, 'k')])
True
>>> t = m.self_make_complement_block_dict(lambda block_key: block_key[0][1])
>>> [*t.iter_block_items()] == [((the2, the2), 2), ((the6, the_inf), 6)]
True


>>> bool(m - m)
False
>>> bool(m ^ m)
False

>>> t = UIntBlockDict([(1, 'x'), (3, 'z'), (0, 'x'), (2, 'y')])
>>> combine = lambda a, b: a+b

>>> s = t.make_intersection(m, combine)
>>> t == UIntBlockDict([(1, 'x'), (3, 'z'), (0, 'x'), (2, 'y')])
True
>>> s == UIntBlockDict([(1, 'xa'), (3, 'zb'), (0, 'xk')])
True

>>> s = m.make_intersection(t, combine)
>>> s == UIntBlockDict([(1, 'ax'), (3, 'bz'), (0, 'kx')])
True


>>> s = t.make_union(m, combine)
>>> s == UIntBlockDict([(1, 'xa'), (3, 'zb'), (0, 'xk'), (2, 'y'), (4, 'b'), (5, 'c')])
True
>>> s = m.make_union(t, combine)
>>> s == UIntBlockDict([(1, 'ax'), (3, 'bz'), (0, 'kx'), (2, 'y'), (4, 'b'), (5, 'c')])
True

>>> s = t.make_difference(m)
>>> s == t - m
True
>>> s == UIntBlockDict([(2, 'y')])
True

>>> s = m.make_difference(t)
>>> s == m - t
True
>>> s == UIntBlockDict([(4, 'b'), (5, 'c')])
True

>>> s = t.make_symmetric_difference(m)
>>> s == t ^ m == m ^ t == m.make_symmetric_difference(t)
True
>>> s == UIntBlockDict([(4, 'b'), (5, 'c'), (2, 'y')])
True


'''



