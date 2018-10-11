

r'''
>pym INamedHeapOps.py
new_abstract_methods:
    `can_be_parent_key_of
    `is_empty
    `get_size
    `exists
    `add_name
    `update_name
    `add_or_update_name
    `pop_name
    `delete_name
    `discard_name
    `peek
    `pop_then_push_ex
    `push_then_pop_ex
    `pop_then_push
    `push_then_pop
    `pop
    `push
    `push_ex
>pym INamedHeapOps__from_iterable.py
new_abstract_methods:
    `make_heap_from_iterable

>>> ops = thePlainNamedMinHeapOps
>>> mk = lambda it:thePlainNamedMinHeapOps.make_heap_from_iterable(it)
>>> mk_empty = lambda:mk(iter([]))
>>> _4321 = [('9a', 1, '9a1'), ('8b', 2, '8b2'), ('7c', 3, '7c3'), ('6d', 4, '6d4')]; _4321.reverse()

#>>> mk_4231 = lambda:mk(_1234) # if >=
>>> mk_1324 = lambda:mk(_4321) # <=

>>> empty_heap = mk_empty()
>>> empty_heap
([], {})
>>> ops.is_empty(empty_heap)
True
>>> ops.get_size(empty_heap)
0
>>> ops.exists(empty_heap, '')
False
>>> ops.update_name(empty_heap, '', 0, ...) #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
KeyError
>>> ops.pop_name(empty_heap, '') #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
KeyError
>>> ops.delete_name(empty_heap, '') #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
KeyError
>>> ops.discard_name(empty_heap, '')
False
>>> ops.peek(empty_heap) #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
KeyError
>>> ops.pop_then_push_ex(empty_heap, '', 0, ...) #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
KeyError
>>> ops.pop_then_push(empty_heap, ('', 0, ...)) #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
KeyError
>>> ops.pop(empty_heap) #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
KeyError
>>> ops.push_then_pop_ex(empty_heap, '', 0, ...)
('', 0, Ellipsis)
>>> ops.push_then_pop(empty_heap, ('', 0, ...))
('', 0, Ellipsis)
>>> empty_heap
([], {})




>>> heap = mk_empty()
>>> ops.add_name(heap, '', 0, ...)
0
>>> ops.get_size(heap)
1
>>> ops.check_and_make_unwrapped_obj_list(heap)
[('', 0, Ellipsis)]

>>> heap = mk_empty()
>>> ops.add_or_update_name(heap, '', 0, ...)
0
>>> ops.get_size(heap)
1
>>> ops.check_and_make_unwrapped_obj_list(heap)
[('', 0, Ellipsis)]

>>> heap = mk_empty()
>>> ops.push_ex(heap, '', 0, ...)
0
>>> ops.get_size(heap)
1
>>> ops.check_and_make_unwrapped_obj_list(heap)
[('', 0, Ellipsis)]

>>> heap = mk_empty()
>>> ops.push(heap, ('', 0, ...))
0
>>> ops.get_size(heap)
1
>>> ops.check_and_make_unwrapped_obj_list(heap)
[('', 0, Ellipsis)]



########################
>>> h = mk_1324()
>>> ops.check_and_make_unwrapped_obj_list(h)
[('9a', 1, '9a1'), ('7c', 3, '7c3'), ('8b', 2, '8b2'), ('6d', 4, '6d4')]
>>> ops.is_empty(h)
False
>>> ops.get_size(h)
4
>>> ops.exists(h, '')
False
>>> ops.exists(h, '7c3')
False
>>> ops.exists(h, 3)
False
>>> ops.exists(h, '7c')
True
>>> ops.exists(h, '6d')
True

### errors
>>> h = mk_1324()
>>> ops.add_name(h, '6d', ..., ...) #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
KeyError
>>> ops.update_name(h, '6d4', ..., ...) #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
KeyError
>>> ops.pop_name(h, '6d4') #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
KeyError
>>> ops.delete_name(h, '6d4') #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
KeyError
>>> ops.pop_then_push_ex(h, '6d', ..., ...) #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
KeyError
>>> ops.pop_then_push(h, ('6d', ..., ...)) #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
KeyError
>>> ops.push_then_pop_ex(h, '6d', 1.5, ...) #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
KeyError
>>> ops.push_then_pop(h, ('6d', 1.5, ...)) #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
KeyError
>>> ops.push(h, ('9a', ..., ...)) #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
KeyError
>>> ops.push_ex(h, '9a', ..., ...) #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
KeyError


########## peek/pop/push/push_ex
>>> h = mk_1324()
>>> ops.peek(h)
('9a', 1, '9a1')
>>> ops.pop(h)
('9a', 1, '9a1')
>>> ops.check_and_make_unwrapped_obj_list(h)
[('8b', 2, '8b2'), ('7c', 3, '7c3'), ('6d', 4, '6d4')]
>>> ops.push(h, ('0', 1, '01'))
0
>>> ops.check_and_make_unwrapped_obj_list(h)
[('0', 1, '01'), ('8b', 2, '8b2'), ('6d', 4, '6d4'), ('7c', 3, '7c3')]
>>> ops.push_ex(h, 'A', 1, 'A1')
1
>>> ops.check_and_make_unwrapped_obj_list(h)
[('0', 1, '01'), ('A', 1, 'A1'), ('6d', 4, '6d4'), ('7c', 3, '7c3'), ('8b', 2, '8b2')]


############## discard_name/push_then_pop_ex/push_then_pop/pop_name/delete_name
>>> h = mk_1324()
>>> ops.discard_name(h, '')
False
>>> ops.peek(h)
('9a', 1, '9a1')
>>> ops.push_then_pop_ex(h, '9a', 0.5, '') # exist name; not push
('9a', 0.5, '')
>>> ops.push_then_pop(h, ('6d', 1, '')) # exist name; not push
('6d', 1, '')
>>> ops.push_then_pop(h, ('x', 1, '')) # non-exist; not push
('x', 1, '')

# modify...
>>> ops.push_then_pop(h, ('9a', 1.5, '...')) # exist head name; push
('9a', 1, '9a1')
>>> ops.push_then_pop(h, ('x', 2, '')) # non-exist name; push
('9a', 1.5, '...')
>>> ops.peek(h)
('x', 2, '')
>>> ops.exists(h, 'x')
True
>>> ops.push_then_pop(h, ('x', 7, '')) # exist name; push
('x', 2, '')

>>> ops.exists(h, 'x')
True
>>> ops.discard_name(h, 'x')
True
>>> ops.exists(h, 'x')
False

>>> ops.exists(h, '6d')
True
>>> ops.pop_name(h, '6d')
('6d', 4, '6d4')
>>> ops.exists(h, '6d')
False

>>> ops.exists(h, '7c')
True
>>> ops.delete_name(h, '7c')
>>> ops.exists(h, '7c')
False

>>> ops.get_size(h)
1
>>> ops.check_and_make_unwrapped_obj_list(h)
[('8b', 2, '8b2')]



################pop_then_push_ex/pop_then_push
>>> h = mk_1324()
>>> ops.exists(h, '')
False
>>> ops.pop_then_push_ex(h, '', 0, '00') # non-exist name
('9a', 1, '9a1')
>>> ops.exists(h, '')
True
>>> ops.pop_then_push(h, ('', 2, '22')) # exist name is also head name
('', 0, '00')
>>> ops.peek(h)
('', 2, '22')

>>> ops.pop_then_push_ex(h, '', 9, '99')
('', 2, '22')
>>> ops.check_and_make_unwrapped_obj_list(h)
[('8b', 2, '8b2'), ('7c', 3, '7c3'), ('', 9, '99'), ('6d', 4, '6d4')]


############## add_name/update_name/add_or_update_name
>>> h = mk_1324()
>>> ops.add_name(h, '', 2.5, '.5')
1
>>> ops.check_and_make_unwrapped_obj_list(h)
[('9a', 1, '9a1'), ('', 2.5, '.5'), ('8b', 2, '8b2'), ('6d', 4, '6d4'), ('7c', 3, '7c3')]

>>> ops.update_name(h, '', 3, '333')
1
>>> ops.check_and_make_unwrapped_obj_list(h)
[('9a', 1, '9a1'), ('', 3, '333'), ('8b', 2, '8b2'), ('6d', 4, '6d4'), ('7c', 3, '7c3')]

>>> ops.update_name(h, '', 1, '11')
1
>>> ops.check_and_make_unwrapped_obj_list(h)
[('9a', 1, '9a1'), ('', 1, '11'), ('8b', 2, '8b2'), ('6d', 4, '6d4'), ('7c', 3, '7c3')]

>>> ops.update_name(h, '', 3.5, '3.')
4
>>> ops.check_and_make_unwrapped_obj_list(h)
[('9a', 1, '9a1'), ('7c', 3, '7c3'), ('8b', 2, '8b2'), ('6d', 4, '6d4'), ('', 3.5, '3.')]

>>> ops.update_name(h, '', 0, '00')
0
>>> ops.check_and_make_unwrapped_obj_list(h)
[('', 0, '00'), ('9a', 1, '9a1'), ('8b', 2, '8b2'), ('6d', 4, '6d4'), ('7c', 3, '7c3')]

>>> ops.add_or_update_name(h, '8b', -1, '')
0
>>> ops.check_and_make_unwrapped_obj_list(h)
[('8b', -1, ''), ('9a', 1, '9a1'), ('', 0, '00'), ('6d', 4, '6d4'), ('7c', 3, '7c3')]

>>> ops.add_or_update_name(h, 'x', -1, 'x')
2
>>> ops.check_and_make_unwrapped_obj_list(h)
[('8b', -1, ''), ('9a', 1, '9a1'), ('x', -1, 'x'), ('6d', 4, '6d4'), ('7c', 3, '7c3'), ('', 0, '00')]


'''

from .PlainNamedMinHeapOps import thePlainNamedMinHeapOps


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +IGNORE_EXCEPTION_DETAIL



