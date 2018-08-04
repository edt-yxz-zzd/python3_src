
from .example_BlockDict import example_BlockDict
example_BlockDict += r'''


input:
    mkBlockDict :: block_dict_key_ops -> (Iter a = None) -> (is_block_items=False) -> BlockDict

>>> m = UIntBlockDict()
>>> m # doctest: +ELLIPSIS
BlockDict(<...>, None)
>>> bool(m)
False

>>> m[1] = 'a'
>>> bool(m)
True
>>> m.get_num_block_keys()
1
>>> m # doctest: +ELLIPSIS
BlockDict(<...>, None, [(((<KeyExCase.TheKey: ...>, 1), (<KeyExCase.TheKey: ...>, 1)), 'a')], is_block_items = True)



# dict_key
>>> m[3] = 'c'
>>> m.get_num_block_keys()
2
>>> m[2] = 'b'
>>> m.get_num_block_keys()
3
>>> list(m.iter_dict_values())
['a', 'b', 'c']
>>> list(m.iter_dict_values(reverse=True))
['c', 'b', 'a']

>>> m[3] = 'a'
>>> m.get_num_block_keys()
3
>>> m[2] = 'a'
>>> m.get_num_block_keys()
1
>>> m[2] = 'b'
>>> m.get_num_block_keys()
3
>>> m[3] = 'b'
>>> m.get_num_block_keys()
2
>>> m[1] = 'b'
>>> m.get_num_block_keys()
1
>>> del m[2]
>>> m.get_num_block_keys()
2


# m = {1:'b', 3:'b'}
# set_block_item
>>> the0 = block_dict_key_ops.mkTheKey(0)
>>> the1 = block_dict_key_ops.mkTheKey(1)
>>> the2 = block_dict_key_ops.mkTheKey(2)
>>> the3 = block_dict_key_ops.mkTheKey(3)
>>> the4 = block_dict_key_ops.mkTheKey(4)
>>> the5 = block_dict_key_ops.mkTheKey(5)
>>> the6 = block_dict_key_ops.mkTheKey(6)
>>> the7 = block_dict_key_ops.mkTheKey(7)

>>> rng = (the2, the7) # [2,7] # [2..7]
>>> m.set_block_item(rng, 'c')
>>> m.get_num_block_keys()
2
>>> m # doctest: +ELLIPSIS
BlockDict(<...>, None, [(((<...TheKey...>, 1), (<...TheKey...>, 1)), 'b'), (((<...TheKey...>, 2), (<...TheKey...>, 7)), 'c')], is_block_items = True)


>>> m.set_block_item((the2,the4), 'b')
>>> m.get_num_block_keys()
2
>>> m # doctest: +ELLIPSIS
BlockDict(<...>, None, [(((<...TheKey...>, 1), (<...TheKey...>, 4)), 'b'), (((<...TheKey...>, 5), (<...TheKey...>, 7)), 'c')], is_block_items = True)

>>> m.set_block_item((the4,the5), 'a')
>>> m.get_num_block_keys()
3
>>> m # doctest: +ELLIPSIS
BlockDict(<...>, None, [(((<...TheKey...>, 1), (<...TheKey...>, 3)), 'b'), (((<...TheKey...>, 4), (<...TheKey...>, 5)), 'a'), (((<...TheKey...>, 6), (<...TheKey...>, 7)), 'c')], is_block_items = True)


>>> m.set_block_item((the3,the5), 'c')
>>> m.get_num_block_keys()
2
>>> m # doctest: +ELLIPSIS
BlockDict(<...>, None, [(((<...TheKey...>, 1), (<...TheKey...>, 2)), 'b'), (((<...TheKey...>, 3), (<...TheKey...>, 7)), 'c')], is_block_items = True)


# m = {(1,2):'b', (3,7):'c'}
>>> m.set_block_item((the7,the7), 'c')
>>> m.get_num_block_keys()
2
>>> m.set_block_item((the7,the7), 'b')
>>> m.get_num_block_keys()
3
>>> m.set_block_item((the2,the6), 'b')
>>> m.get_num_block_keys()
1
>>> m # doctest: +ELLIPSIS
BlockDict(<...>, None, [(((<...TheKey...>, 1), (<...TheKey...>, 7)), 'b')], is_block_items = True)


# m = {(1,7):'b'}
>>> del m[2]
>>> m.get_num_block_keys()
2
>>> del m[6]
>>> m.get_num_block_keys()
3
>>> del m[4]
>>> m.get_num_block_keys()
4


# m = {(1,1):'b', (3,3):'b', (5,5):'b', (7,7):'b'}
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

# pop_block_items_of_block_key
>>> ls = m.pop_block_items_of_block_key((the2, the5), reverse=True)
>>> ls # doctest: +ELLIPSIS
[(((..., 5), (..., 5)), 'b'), (((..., 3), (..., 3)), 'b')]

>>> m.get_num_block_keys()
2
>>> m # doctest: +ELLIPSIS
BlockDict(<...>, None, [(((..., 1), (..., 1)), 'b'), (((..., 7), (..., 7)), 'b')], is_block_items = True)


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
>>> t.clear()
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

>>> t = m.copy()
>>> t.discard_block_key((the1, the4))
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
>>> m.pop(2)
Traceback (most recent call last):
    ...
KeyError: 2
>>> m.pop(2, None)
>>> m.pop(2, 'abc')
'abc'



>>> t = m.copy()
>>> t.pop(1)
'a'
>>> t.get_num_block_keys()
3
>>> t.pop(3)
'b'
>>> t.get_num_block_keys()
3
>>> t.pop(4)
'b'
>>> t.get_num_block_keys()
2
>>> [*t.iter_dict_values()]
['k', 'c']


>>> t = m.copy()
>>> t.pop_block_item() == ((the5, the5), 'c')
True
>>> t = m.copy()
>>> t.pop_block_item_of_dict_key(4) == ((the4, the4), 'b')
True
>>> 4 not in t
True
>>> 3 in t
True

>>> t = m.copy()
>>> t.pop_block_items_of_block_key((the3, the1))
[]
>>> t.pop_block_items_of_block_key((the1, the3), reverse=True) == [((the3, the3), 'b'), ((the1, the1), 'a')]
True
>>> t.pop_block_items_of_block_key((the1, the3))
[]

>>> t = m.copy()
>>> t.pop_block_items_of_dict_key(2)
[]
>>> t.pop_block_items_of_dict_key(1) == [((the1, the1), 'a')]
True
>>> t = m.copy()
>>> t.pop_left_or_right_block_item(False) == ((the0, the0), 'k')
True
>>> t.pop_left_or_right_block_item(True) == ((the5, the5), 'c')
True

>>> t = m.copy()
>>> t.pop_right_block_item() == m.copy().pop_left_or_right_block_item(True)
True
>>> t.pop_left_block_item() == m.copy().pop_left_or_right_block_item(False)
True

>>> t = m.copy()
>>> t.set_block_item((the2, the3), 'a')
>>> t.get_num_block_keys()
4
>>> t.block_key2block_items(((the0, block_dict_key_ops.getTheMaxKeyEx())), reverse=True) == [*t.iter_block_items(reverse=True)] == [((the5, the5), 'c'), ((the4, the4), 'b'), ((the1, the3), 'a'), ((the0, the0), 'k')]
True
>>> t.block_key2block_items(((the0, block_dict_key_ops.getTheMaxKeyEx()))) == [*t.iter_block_items()] == [((the0, the0), 'k'), ((the1, the3), 'a'), ((the4, the4), 'b'), ((the5, the5), 'c')]
True


>>> t = m.copy()
>>> t.set_fdefault(1, ...)
'a'
>>> t[1]
'a'
>>> t.set_fdefault(2, lambda: 'a')
'a'
>>> _ = t.pop_left_block_item()
>>> t.pop_left_block_item() == ((the1, the2), 'a')
True
>>> t.set_fdefault(2, lambda: 'x')
'x'

>>> t = m.copy()
>>> t.setdefault(1, 'y')
'a'
>>> t[1]
'a'
>>> t.setdefault(2, 'c')
'c'
>>> t.get_num_block_keys()
5
>>> t[2]
'c'
>>> t.setdefault(6, '.')
'.'
>>> t[6]
'.'


>>> m.total_dict_key_ops is m.get_total_dict_key_ops()
True

>>> t = m.copy()
>>> t.pop(3)
'b'
>>> t[1] = 'x'
>>> t.update(m)
>>> t == m
True
>>> t.update((k, 'c') for k in range(5))
>>> t.get_num_block_keys()
1
>>> [*t.iter_block_items()] == [((the0, the5), 'c')]
True

>>> t = m.copy()
>>> t.update_from_block_items([((the0, the3), 'c'), ((the2, the4), 'c')])
>>> t.get_num_block_keys()
1
>>> [*t.iter_block_items()] == [((the0, the5), 'c')]
True

>>> t = m.copy()
>>> t.update_from_items((k, 'c') for k in range(5))
>>> t.get_num_block_keys()
1
>>> [*t.iter_block_items()] == [((the0, the5), 'c')]
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

__delitem__
>>> t = m.copy()
>>> del t[1]
>>> t.get_num_block_keys()
3
>>> del t[3]
>>> t.get_num_block_keys()
3
>>> del t[4]
>>> t.get_num_block_keys()
2
>>> del t[5]
>>> t.get_num_block_keys()
1
>>> del t[0]
>>> t.get_num_block_keys()
0
>>> t == empty
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

__repr__
>>> empty # doctest: +ELLIPSIS
BlockDict(<...>, None)
>>> m # doctest: +ELLIPSIS
BlockDict(<...>, None, [(((<KeyExCase.TheKey: 2>, 0), (<KeyExCase.TheKey: 2>, 0)), 'k'), (((<KeyExCase.TheKey: 2>, 1), (<KeyExCase.TheKey: 2>, 1)), 'a'), (((<KeyExCase.TheKey: 2>, 3), (<KeyExCase.TheKey: 2>, 4)), 'b'), (((<KeyExCase.TheKey: 2>, 5), (<KeyExCase.TheKey: 2>, 5)), 'c')], is_block_items = True)

__setitem__
>>> t = m.copy()
>>> 2 in t
False
>>> t[2] = 'b'
>>> 2 in t
True
>>> t.get_num_block_keys()
4
>>> t[2]
'b'
>>> t[2] = 'x'
>>> t.get_num_block_keys()
5
>>> t[2]
'x'


swap
>>> t = m.copy()
>>> e = empty.copy()
>>> t.swap(e)
>>> t == empty != e == m
True

assign
>>> e = empty.copy()
>>> e.assign(m)
>>> e == m
True



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



set_dict_key2default
>>> t = m.copy()
>>> t.set_dict_key2default(1, ...)
'a'
>>> t[1]
'a'
>>> t.set_dict_key2default(2, lambda k: 'A'+str(k))
'A2'
>>> t[2]
'A2'

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




'''

