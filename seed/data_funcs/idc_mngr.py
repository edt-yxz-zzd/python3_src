#__all__:goto
#[:new_concrete_methods4DoublyList4Idc]:goto
#[:new_concrete_methods4DoublyList4Idc__rollbackable]:goto
r'''[[[
e ../../python3_src/seed/data_funcs/idc_mngr.py

indices manager
    delete idx; alloc idx/memory
    put idx;    free idx/memory
    idx is resource
doubly_list

seed.data_funcs.idc_mngr
py -m nn_ns.app.debug_cmd   seed.data_funcs.idc_mngr -x
py -m nn_ns.app.doctest_cmd seed.data_funcs.idc_mngr:__doc__
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.data_funcs.idc_mngr:DoublyList4Idc@T    =T

>>> sf = DoublyList4Idc(9, [])
>>> sf
DoublyList4Idc(9, [])
>>> sf.verify()
>>> sf.put(6)
True
>>> sf.verify()
>>> sf
DoublyList4Idc(9, [6])
>>> sf.put(8)
True
>>> sf.verify()
>>> sf
DoublyList4Idc(9, [6, 8])
>>> [*iter(sf)]
[6, 8]
>>> [*reversed(sf)]
[8, 6]
>>> sf.put(8)
False
>>> len(sf)
2
>>> 8 in sf
True
>>> sf.verify()
>>> sf.discard(8)
True
>>> sf.verify()
>>> sf
DoublyList4Idc(9, [6])
>>> 8 in sf
False
>>> sf.discard(8)
False
>>> 6 in sf
True
>>> sf.verify()
>>> sf.remove(6)
>>> sf.verify()
>>> len(sf)
0
>>> 6 in sf
False
>>> sf
DoublyList4Idc(9, [])


######################
######################
######################
######################
######################
######################
######################
######################
######################
>>> sf = DoublyList4Idc(None, [])
>>> sf
DoublyList4Idc(None, [])
>>> sf = DoublyList4Idc(9, [])
>>> sf
DoublyList4Idc(9, [])

>>> sf = DoublyList4Idc(None, [], list_vs_dict=True)
>>> sf
DoublyList4Idc(None, [], list_vs_dict = True)
>>> sf = DoublyList4Idc(9, [], list_vs_dict=True)
>>> sf
DoublyList4Idc(9, [], list_vs_dict = True)



>>> sf = DoublyList4Idc(None, [], may_dynamic_resize=False)
Traceback (most recent call last):
    ...
ValueError: size is unbound but forbid dynamic_resize
>>> sf = DoublyList4Idc(9, [], may_dynamic_resize=False)
>>> sf
DoublyList4Idc(9, [])

>>> sf = DoublyList4Idc(None, [], list_vs_dict=True, may_dynamic_resize=False)
Traceback (most recent call last):
    ...
ValueError: irrational: fixed size of dict
>>> sf = DoublyList4Idc(9, [], list_vs_dict=True, may_dynamic_resize=False)
Traceback (most recent call last):
    ...
ValueError: irrational: fixed size of dict



>>> sf = DoublyList4Idc(None, [], may_dynamic_resize=True)
>>> sf
DoublyList4Idc(None, [])
>>> sf = DoublyList4Idc(9, [], may_dynamic_resize=True)
>>> sf
DoublyList4Idc(9, [], may_dynamic_resize = True)

>>> sf = DoublyList4Idc(None, [], list_vs_dict=True, may_dynamic_resize=True)
>>> sf
DoublyList4Idc(None, [], list_vs_dict = True)
>>> sf = DoublyList4Idc(9, [], list_vs_dict=True, may_dynamic_resize=True)
>>> sf
DoublyList4Idc(9, [], list_vs_dict = True)





######################
######################
>>> sf = DoublyList4Idc(None, [])
>>> sf
DoublyList4Idc(None, [])
>>> sf.verify()
>>> sf.put(3)
True
>>> sf.verify()
>>> sf.put(7)
True
>>> sf.verify()
>>> sf.put(2)
True
>>> sf.verify()
>>> sf.put_or_move_to_end(4)
True
>>> sf.verify()
>>> sf.put(7)
False
>>> sf.verify()
>>> sf
DoublyList4Idc(None, [3, 7, 2, 4])
>>> sf.put_or_move_to_end(7)
False
>>> sf.verify()
>>> sf
DoublyList4Idc(None, [3, 2, 4, 7])
>>> sf.remove(2)
>>> sf.verify()
>>> sf.remove(3)
>>> sf.verify()
>>> sf.remove(4)
>>> sf.verify()
>>> sf.remove(7)
>>> sf.verify()
>>> sf
DoublyList4Idc(None, [])



######################
######################
>>> sf = DoublyList4Idc(None, [], list_vs_dict=True)
>>> sf
DoublyList4Idc(None, [], list_vs_dict = True)
>>> sf.verify()
>>> sf.put(3)
True
>>> sf.verify()
>>> sf.put(7)
True
>>> sf.verify()
>>> sf.put(2)
True
>>> sf.verify()
>>> sf.put_or_move_to_end(4)
True
>>> sf.verify()
>>> sf.put(7)
False
>>> sf.verify()
>>> sf
DoublyList4Idc(None, [3, 7, 2, 4], list_vs_dict = True)
>>> sf.put_or_move_to_end(7)
False
>>> sf.verify()
>>> sf
DoublyList4Idc(None, [3, 2, 4, 7], list_vs_dict = True)
>>> sf.remove(2)
>>> sf.verify()
>>> sf.remove(3)
>>> sf.verify()
>>> sf.remove(4)
>>> sf.verify()
>>> sf.remove(7)
>>> sf.verify()
>>> sf
DoublyList4Idc(None, [], list_vs_dict = True)










######################
######################
>>> sf = DoublyList4Idc(9, [])
>>> sf.puts(range(5))
(5, 5)
>>> sf.puts(range(5))
(5, 0)
>>> sf.puts(range(3,9))
(6, 4)
>>> sf
DoublyList4Idc(9, [0, 1, 2, 3, 4, 5, 6, 7, 8])
>>> sf.pop_all()
[0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> sf
DoublyList4Idc(9, [])
>>> sf.puts(range(3,9))
(6, 6)
>>> sf
DoublyList4Idc(9, [3, 4, 5, 6, 7, 8])
>>> sf.clear()
>>> sf
DoublyList4Idc(9, [])

>>> sf = DoublyList4Idc(9, [])
>>> sf.first
Traceback (most recent call last):
    ...
IndexError: first
>>> sf.last
Traceback (most recent call last):
    ...
IndexError: last
>>> sf.put(6)
True
>>> sf.first
6
>>> sf.last
6
>>> sf.put(1)
True
>>> sf.first
6
>>> sf.last
1
>>> sf.put(5)
True
>>> sf.first
6
>>> sf.last
5
>>> sf.put(2)
True
>>> sf.first
6
>>> sf.last
2
>>> sf.put(4)
True
>>> sf.first
6
>>> sf.last
4
>>> sf.remove(4)
>>> sf.first
6
>>> sf.last
2
>>> sf.remove(5)
>>> sf.first
6
>>> sf.last
2
>>> sf.remove(6)
>>> sf.first
1
>>> sf.last
2
>>> sf
DoublyList4Idc(9, [1, 2])
>>> sf.put(1)
False
>>> sf.first
1
>>> sf.last
2
>>> sf.move_to_end(1); sf.first
2
>>> sf.first
2
>>> sf.last
1
>>> sf
DoublyList4Idc(9, [2, 1])
>>> sf.remove(2)
>>> sf.first
1
>>> sf.last
1
>>> sf.remove(1)
>>> sf.first
Traceback (most recent call last):
    ...
IndexError: first
>>> sf.last
Traceback (most recent call last):
    ...
IndexError: last
>>> sf
DoublyList4Idc(9, [])


######################
######################
get_after_
    next_
    forward_
get_before_
    prev_
    backward_
>>> sf = DoublyList4Idc(9, [6, 7, 8])
>>> sf
DoublyList4Idc(9, [6, 7, 8])
>>> sf.get_before_(6)
8
>>> sf.get_before_(7)
6
>>> sf.get_before_(8)
7

>>> sf.get_after_(6)
7
>>> sf.get_after_(7)
8
>>> sf.get_after_(8)
6

>>> sf.prev_(6)
8
>>> sf.backward_(6)
8
>>> sf.next_(6)
7
>>> sf.forward_(6)
7

>>> sf = DoublyList4Idc(9, [6, 8])
>>> sf
DoublyList4Idc(9, [6, 8])
>>> sf.get_before_(6)
8
>>> sf.get_before_(8)
6

>>> sf.get_after_(6)
8
>>> sf.get_after_(8)
6

>>> sf = DoublyList4Idc(9, [6])
>>> sf
DoublyList4Idc(9, [6])
>>> sf.get_before_(6)
6

>>> sf.get_after_(6)
6

>>> sf = DoublyList4Idc(9, [])
>>> sf
DoublyList4Idc(9, [])
>>> sf.get_before_(6)
Traceback (most recent call last):
    ...
IndexError: 6

>>> sf.get_after_(6)
Traceback (most recent call last):
    ...
IndexError: 6


######################
######################
pop_first
pop_last
pop_after_
pop_before_
#####
pop_first
>>> sf = DoublyList4Idc(9, [6, 7, 8])
>>> sf.pop_first()
6
>>> sf.verify()
>>> sf
DoublyList4Idc(9, [7, 8])
>>> sf.pop_first()
7
>>> sf.verify()
>>> sf
DoublyList4Idc(9, [8])
>>> sf.pop_first()
8
>>> sf.verify()
>>> sf
DoublyList4Idc(9, [])

#####
pop_last
>>> sf = DoublyList4Idc(9, [6, 7, 8])
>>> sf.pop_last()
8
>>> sf.verify()
>>> sf
DoublyList4Idc(9, [6, 7])
>>> sf.pop_last()
7
>>> sf.verify()
>>> sf
DoublyList4Idc(9, [6])
>>> sf.pop_last()
6
>>> sf.verify()
>>> sf
DoublyList4Idc(9, [])

#####
pop_before_
>>> sf = DoublyList4Idc(9, [6, 7, 8])
>>> sf.pop_before_(6)
8
>>> sf.verify()
>>> sf
DoublyList4Idc(9, [6, 7])
>>> sf.pop_before_(6)
7
>>> sf.verify()
>>> sf
DoublyList4Idc(9, [6])
>>> sf.pop_before_(6)
6
>>> sf.verify()
>>> sf
DoublyList4Idc(9, [])

>>> sf = DoublyList4Idc(9, [6, 7, 8])
>>> sf.pop_before_(7)
6
>>> sf.verify()
>>> sf
DoublyList4Idc(9, [7, 8])
>>> sf.pop_before_(7)
8
>>> sf.verify()
>>> sf
DoublyList4Idc(9, [7])
>>> sf.pop_before_(7)
7
>>> sf.verify()
>>> sf
DoublyList4Idc(9, [])

>>> sf = DoublyList4Idc(9, [6, 7, 8])
>>> sf.pop_before_(8)
7
>>> sf.verify()
>>> sf
DoublyList4Idc(9, [6, 8])
>>> sf.pop_before_(8)
6
>>> sf.verify()
>>> sf
DoublyList4Idc(9, [8])
>>> sf.pop_before_(8)
8
>>> sf.verify()
>>> sf
DoublyList4Idc(9, [])

#####
pop_after_
>>> sf = DoublyList4Idc(9, [6, 7, 8])
>>> sf.pop_after_(6)
7
>>> sf.verify()
>>> sf
DoublyList4Idc(9, [6, 8])
>>> sf.pop_after_(6)
8
>>> sf.verify()
>>> sf
DoublyList4Idc(9, [6])
>>> sf.pop_after_(6)
6
>>> sf.verify()
>>> sf
DoublyList4Idc(9, [])

>>> sf = DoublyList4Idc(9, [6, 7, 8])
>>> sf.pop_after_(7)
8
>>> sf.verify()
>>> sf
DoublyList4Idc(9, [6, 7])
>>> sf.pop_after_(7)
6
>>> sf.verify()
>>> sf
DoublyList4Idc(9, [7])
>>> sf.pop_after_(7)
7
>>> sf.verify()
>>> sf
DoublyList4Idc(9, [])

>>> sf = DoublyList4Idc(9, [6, 7, 8])
>>> sf.pop_after_(8)
6
>>> sf.verify()
>>> sf
DoublyList4Idc(9, [7, 8])
>>> sf.pop_after_(8)
7
>>> sf.verify()
>>> sf
DoublyList4Idc(9, [8])
>>> sf.pop_after_(8)
8
>>> sf.verify()
>>> sf
DoublyList4Idc(9, [])






######################
######################
put_after_
put_before_
move_to_after_
move_to_before_
put_or_move_to_after_
put_or_move_to_before_

#####
put_after_
>>> sf = DoublyList4Idc(9, [6])
>>> sf
DoublyList4Idc(9, [6])
>>> sf.put_after_(6, 6)
False
>>> sf.put_after_(6, 7)
True
>>> sf
DoublyList4Idc(9, [6, 7])
>>> sf.put_after_(6, 6)
False
>>> sf.put_after_(6, 7)
False
>>> sf.put_after_(6, 8)
True
>>> sf
DoublyList4Idc(9, [6, 8, 7])
>>> sf.put_after_(7, 8)
False
>>> sf.put_after_(7, 3)
True
>>> sf
DoublyList4Idc(9, [6, 8, 7, 3])
>>> sf.put_after_(7, 4)
True
>>> sf
DoublyList4Idc(9, [6, 8, 7, 4, 3])


#####
put_before_
>>> sf = DoublyList4Idc(9, [6])
>>> sf
DoublyList4Idc(9, [6])
>>> sf.put_before_(6, 6)
False
>>> sf.put_before_(6, 7)
True
>>> sf
DoublyList4Idc(9, [7, 6])
>>> sf.put_before_(6, 6)
False
>>> sf.put_before_(6, 7)
False
>>> sf.put_before_(6, 8)
True
>>> sf
DoublyList4Idc(9, [7, 8, 6])
>>> sf.put_before_(7, 8)
False
>>> sf.put_before_(7, 3)
True
>>> sf
DoublyList4Idc(9, [3, 7, 8, 6])
>>> sf.put_before_(7, 4)
True
>>> sf
DoublyList4Idc(9, [3, 4, 7, 8, 6])


#####
move_to_after_
>>> sf = DoublyList4Idc(9, [6])
>>> sf.move_to_after_(6, 6)
>>> sf
DoublyList4Idc(9, [6])

>>> sf = DoublyList4Idc(9, [6, 7])
>>> sf.move_to_after_(6, 6)
>>> sf
DoublyList4Idc(9, [6, 7])
>>> sf = DoublyList4Idc(9, [6, 7])
>>> sf.move_to_after_(6, 7)
>>> sf
DoublyList4Idc(9, [6, 7])
>>> sf = DoublyList4Idc(9, [6, 7])
>>> sf.move_to_after_(7, 7)
>>> sf
DoublyList4Idc(9, [6, 7])
>>> sf = DoublyList4Idc(9, [6, 7])
>>> sf.move_to_after_(7, 6)
>>> sf
DoublyList4Idc(9, [7, 6])

>>> sf = DoublyList4Idc(9, [6, 7, 0, 8])
>>> sf.move_to_after_(6, 6)
>>> sf
DoublyList4Idc(9, [6, 7, 0, 8])
>>> sf = DoublyList4Idc(9, [6, 7, 0, 8])
>>> sf.move_to_after_(6, 7)
>>> sf
DoublyList4Idc(9, [6, 7, 0, 8])
>>> sf = DoublyList4Idc(9, [6, 7, 0, 8])
>>> sf.move_to_after_(6, 0)
>>> sf
DoublyList4Idc(9, [6, 0, 7, 8])
>>> sf = DoublyList4Idc(9, [6, 7, 0, 8])
>>> sf.move_to_after_(6, 8)
>>> sf
DoublyList4Idc(9, [6, 8, 7, 0])
>>> sf = DoublyList4Idc(9, [6, 7, 0, 8])
>>> sf.move_to_after_(7, 6)
>>> sf
DoublyList4Idc(9, [7, 6, 0, 8])
>>> sf = DoublyList4Idc(9, [6, 7, 0, 8])
>>> sf.move_to_after_(7, 7)
>>> sf
DoublyList4Idc(9, [6, 7, 0, 8])
>>> sf = DoublyList4Idc(9, [6, 7, 0, 8])
>>> sf.move_to_after_(7, 0)
>>> sf
DoublyList4Idc(9, [6, 7, 0, 8])
>>> sf = DoublyList4Idc(9, [6, 7, 0, 8])
>>> sf.move_to_after_(7, 8)
>>> sf
DoublyList4Idc(9, [6, 7, 8, 0])
>>> sf = DoublyList4Idc(9, [6, 7, 0, 8])
>>> sf.move_to_after_(8, 6)
>>> sf
DoublyList4Idc(9, [7, 0, 8, 6])
>>> sf = DoublyList4Idc(9, [6, 7, 0, 8])
>>> sf.move_to_after_(8, 7)
>>> sf
DoublyList4Idc(9, [6, 0, 8, 7])
>>> sf = DoublyList4Idc(9, [6, 7, 0, 8])
>>> sf.move_to_after_(8, 0)
>>> sf
DoublyList4Idc(9, [6, 7, 8, 0])
>>> sf = DoublyList4Idc(9, [6, 7, 0, 8])
>>> sf.move_to_after_(8, 8)
>>> sf
DoublyList4Idc(9, [6, 7, 0, 8])



#####
move_to_before_
.+1,.+74s/move_to_after_/move_to_before_/g
>>> sf = DoublyList4Idc(9, [6])
>>> sf.move_to_before_(6, 6)
>>> sf
DoublyList4Idc(9, [6])

>>> sf = DoublyList4Idc(9, [6, 7])
>>> sf.move_to_before_(6, 6)
>>> sf
DoublyList4Idc(9, [6, 7])
>>> sf = DoublyList4Idc(9, [6, 7])
>>> sf.move_to_before_(6, 7)
>>> sf
DoublyList4Idc(9, [7, 6])
>>> sf = DoublyList4Idc(9, [6, 7])
>>> sf.move_to_before_(7, 7)
>>> sf
DoublyList4Idc(9, [6, 7])
>>> sf = DoublyList4Idc(9, [6, 7])
>>> sf.move_to_before_(7, 6)
>>> sf
DoublyList4Idc(9, [6, 7])

>>> sf = DoublyList4Idc(9, [6, 7, 0, 8])
>>> sf.move_to_before_(6, 6)
>>> sf
DoublyList4Idc(9, [6, 7, 0, 8])
>>> sf = DoublyList4Idc(9, [6, 7, 0, 8])
>>> sf.move_to_before_(6, 7)
>>> sf
DoublyList4Idc(9, [7, 6, 0, 8])
>>> sf = DoublyList4Idc(9, [6, 7, 0, 8])
>>> sf.move_to_before_(6, 0)
>>> sf
DoublyList4Idc(9, [0, 6, 7, 8])
>>> sf = DoublyList4Idc(9, [6, 7, 0, 8])
>>> sf.move_to_before_(6, 8)
>>> sf
DoublyList4Idc(9, [8, 6, 7, 0])
>>> sf = DoublyList4Idc(9, [6, 7, 0, 8])
>>> sf.move_to_before_(7, 6)
>>> sf
DoublyList4Idc(9, [6, 7, 0, 8])
>>> sf = DoublyList4Idc(9, [6, 7, 0, 8])
>>> sf.move_to_before_(7, 7)
>>> sf
DoublyList4Idc(9, [6, 7, 0, 8])
>>> sf = DoublyList4Idc(9, [6, 7, 0, 8])
>>> sf.move_to_before_(7, 0)
>>> sf
DoublyList4Idc(9, [6, 0, 7, 8])
>>> sf = DoublyList4Idc(9, [6, 7, 0, 8])
>>> sf.move_to_before_(7, 8)
>>> sf
DoublyList4Idc(9, [6, 8, 7, 0])
>>> sf = DoublyList4Idc(9, [6, 7, 0, 8])
>>> sf.move_to_before_(8, 6)
>>> sf
DoublyList4Idc(9, [7, 0, 6, 8])
>>> sf = DoublyList4Idc(9, [6, 7, 0, 8])
>>> sf.move_to_before_(8, 7)
>>> sf
DoublyList4Idc(9, [6, 0, 7, 8])
>>> sf = DoublyList4Idc(9, [6, 7, 0, 8])
>>> sf.move_to_before_(8, 0)
>>> sf
DoublyList4Idc(9, [6, 7, 0, 8])
>>> sf = DoublyList4Idc(9, [6, 7, 0, 8])
>>> sf.move_to_before_(8, 8)
>>> sf
DoublyList4Idc(9, [6, 7, 0, 8])


#####
put_or_move_to_after_
>>> sf = DoublyList4Idc(9, [6])
>>> sf.put_or_move_to_after_(6, 6)
False
>>> sf
DoublyList4Idc(9, [6])

>>> sf = DoublyList4Idc(9, [6])
>>> sf.put_or_move_to_after_(6, 7)
True
>>> sf
DoublyList4Idc(9, [6, 7])

>>> sf = DoublyList4Idc(9, [6, 7])
>>> sf.put_or_move_to_after_(6, 6)
False
>>> sf
DoublyList4Idc(9, [6, 7])

>>> sf = DoublyList4Idc(9, [6, 7])
>>> sf.put_or_move_to_after_(6, 7)
False
>>> sf
DoublyList4Idc(9, [6, 7])

>>> sf = DoublyList4Idc(9, [6, 7])
>>> sf.put_or_move_to_after_(7, 6)
False
>>> sf
DoublyList4Idc(9, [7, 6])

>>> sf = DoublyList4Idc(9, [6, 7])
>>> sf.put_or_move_to_after_(7, 7)
False
>>> sf
DoublyList4Idc(9, [6, 7])

>>> sf = DoublyList4Idc(9, [6, 7])
>>> sf.put_or_move_to_after_(6, 8)
True
>>> sf
DoublyList4Idc(9, [6, 8, 7])

>>> sf = DoublyList4Idc(9, [6, 7])
>>> sf.put_or_move_to_after_(7, 8)
True
>>> sf
DoublyList4Idc(9, [6, 7, 8])

>>> sf = DoublyList4Idc(9, [6, 7, 8])
>>> sf.put_or_move_to_after_(6, 6)
False
>>> sf
DoublyList4Idc(9, [6, 7, 8])
>>> sf = DoublyList4Idc(9, [6, 7, 8])
>>> sf.put_or_move_to_after_(6, 7)
False
>>> sf
DoublyList4Idc(9, [6, 7, 8])

>>> sf = DoublyList4Idc(9, [6, 7, 8])
>>> sf.put_or_move_to_after_(6, 8)
False
>>> sf
DoublyList4Idc(9, [6, 8, 7])

>>> sf = DoublyList4Idc(9, [6, 7, 8])
>>> sf.put_or_move_to_after_(7, 6)
False
>>> sf
DoublyList4Idc(9, [7, 6, 8])
>>> sf = DoublyList4Idc(9, [6, 7, 8])
>>> sf.put_or_move_to_after_(7, 7)
False
>>> sf
DoublyList4Idc(9, [6, 7, 8])

>>> sf = DoublyList4Idc(9, [6, 7, 8])
>>> sf.put_or_move_to_after_(7, 8)
False
>>> sf
DoublyList4Idc(9, [6, 7, 8])

>>> sf = DoublyList4Idc(9, [6, 7, 8])
>>> sf.put_or_move_to_after_(8, 6)
False
>>> sf
DoublyList4Idc(9, [7, 8, 6])
>>> sf = DoublyList4Idc(9, [6, 7, 8])
>>> sf.put_or_move_to_after_(8, 7)
False
>>> sf
DoublyList4Idc(9, [6, 8, 7])

>>> sf = DoublyList4Idc(9, [6, 7, 8])
>>> sf.put_or_move_to_after_(8, 8)
False
>>> sf
DoublyList4Idc(9, [6, 7, 8])


#####
put_or_move_to_before_
.+1,.+100s/put_or_move_to_after_/put_or_move_to_before_/g
>>> sf = DoublyList4Idc(9, [6])
>>> sf.put_or_move_to_before_(6, 6)
False
>>> sf
DoublyList4Idc(9, [6])

>>> sf = DoublyList4Idc(9, [6])
>>> sf.put_or_move_to_before_(6, 7)
True
>>> sf
DoublyList4Idc(9, [7, 6])

>>> sf = DoublyList4Idc(9, [6, 7])
>>> sf.put_or_move_to_before_(6, 6)
False
>>> sf
DoublyList4Idc(9, [6, 7])

>>> sf = DoublyList4Idc(9, [6, 7])
>>> sf.put_or_move_to_before_(6, 7)
False
>>> sf
DoublyList4Idc(9, [7, 6])

>>> sf = DoublyList4Idc(9, [6, 7])
>>> sf.put_or_move_to_before_(7, 6)
False
>>> sf
DoublyList4Idc(9, [6, 7])

>>> sf = DoublyList4Idc(9, [6, 7])
>>> sf.put_or_move_to_before_(7, 7)
False
>>> sf
DoublyList4Idc(9, [6, 7])

>>> sf = DoublyList4Idc(9, [6, 7])
>>> sf.put_or_move_to_before_(6, 8)
True
>>> sf
DoublyList4Idc(9, [8, 6, 7])

>>> sf = DoublyList4Idc(9, [6, 7])
>>> sf.put_or_move_to_before_(7, 8)
True
>>> sf
DoublyList4Idc(9, [6, 8, 7])

>>> sf = DoublyList4Idc(9, [6, 7, 8])
>>> sf.put_or_move_to_before_(6, 6)
False
>>> sf
DoublyList4Idc(9, [6, 7, 8])
>>> sf = DoublyList4Idc(9, [6, 7, 8])
>>> sf.put_or_move_to_before_(6, 7)
False
>>> sf
DoublyList4Idc(9, [7, 6, 8])

>>> sf = DoublyList4Idc(9, [6, 7, 8])
>>> sf.put_or_move_to_before_(6, 8)
False
>>> sf
DoublyList4Idc(9, [8, 6, 7])

>>> sf = DoublyList4Idc(9, [6, 7, 8])
>>> sf.put_or_move_to_before_(7, 6)
False
>>> sf
DoublyList4Idc(9, [6, 7, 8])
>>> sf = DoublyList4Idc(9, [6, 7, 8])
>>> sf.put_or_move_to_before_(7, 7)
False
>>> sf
DoublyList4Idc(9, [6, 7, 8])

>>> sf = DoublyList4Idc(9, [6, 7, 8])
>>> sf.put_or_move_to_before_(7, 8)
False
>>> sf
DoublyList4Idc(9, [6, 8, 7])

>>> sf = DoublyList4Idc(9, [6, 7, 8])
>>> sf.put_or_move_to_before_(8, 6)
False
>>> sf
DoublyList4Idc(9, [7, 6, 8])
>>> sf = DoublyList4Idc(9, [6, 7, 8])
>>> sf.put_or_move_to_before_(8, 7)
False
>>> sf
DoublyList4Idc(9, [6, 7, 8])

>>> sf = DoublyList4Idc(9, [6, 7, 8])
>>> sf.put_or_move_to_before_(8, 8)
False
>>> sf
DoublyList4Idc(9, [6, 7, 8])



######################
######################
######################
######################
>>> def _all_subclasses_(s, Ts, /):
...     for T in Ts:
...         if not T in s:
...             s.add(T)
...             _all_subclasses_(s, T.__subclasses__())

>>> def all_subclasses_(T, /):
...     s = set()
...     _all_subclasses_(s, [T])
...     s.remove(T)
...     return s

######################
######################
DoublyList4Idc__rollbackable
    __init__
    tell
    rollback
    discard
    put
    set_first

>>> sf = DoublyList4Idc__rollbackable(9, [])
>>> opaque_position0 = sf.tell()
>>> sf
DoublyList4Idc__rollbackable(9, [])
>>> opaque_position0 is sf.tell()
True
>>> sf.rollback(opaque_position0)
>>> opaque_position0 is sf.tell()
True

>>> sf
DoublyList4Idc__rollbackable(9, [])
>>> sf.put(3)
True
>>> sf.put(2)
True
>>> sf.put(8)
True
>>> opaque_position1 = sf.tell()
>>> sf
DoublyList4Idc__rollbackable(9, [3, 2, 8])
>>> opaque_position1 is sf.tell()
True
>>> opaque_position0 is sf.tell()
False
>>> sf.put(3)
False
>>> opaque_position1 is sf.tell()
True
>>> sf.set_first(3)
False
>>> opaque_position1 is sf.tell()
True
>>> sf.set_first(2)
True
>>> opaque_position2 = sf.tell()
>>> sf
DoublyList4Idc__rollbackable(9, [2, 8, 3])
>>> opaque_position1 is not opaque_position2 is sf.tell()
True
>>> sf.discard(2)
True
>>> opaque_position3 = sf.tell()
>>> sf
DoublyList4Idc__rollbackable(9, [8, 3])
>>> sf.discard(2)
False
>>> opaque_position2 is not opaque_position3 is sf.tell()
True
>>> sf.put_before_(8, 5)
True
>>> sf.discard(3)
True
>>> sf.pop()
8
>>> sf.pop()
5
>>> opaque_position3 is sf.tell()
False
>>> sf
DoublyList4Idc__rollbackable(9, [])



>>> miss_types_ = lambda sf:{__0, __1, __2, *map(type, sf._rollback_ls)} ^ {*all_subclasses_(_IBidirectionPlayer)}
>>> miss_types_(sf) == {_Remove__before_eq_}
True
>>> sf.put(8)
True
>>> sf.put_before_(8, 5)
True
>>> miss_types_(sf) == {_Remove__before_eq_}
True
>>> sf.put_before_(8, 3)
True


>>> miss_types_(sf)
set()

>>> sf._rollback_ls
[_Do_nothing(), _Pop__last_eq_(3), _Pop__last_eq_(2), _Pop__last_eq_(8), _Do_nothing(), _Set_first__old_eq_(2, 3), _Do_nothing(), _Put_before_(8, 2), _Do_nothing(), _Pop__last_eq_(5), _Set_first__old_eq_(5, 8), _Put__first_eq_(5, 3), _Put__first_eq_(5, 8), _Put_into_empty(5), _Do_nothing(), _Pop__last_eq_(8), _Pop__last_eq_(5), _Set_first__old_eq_(5, 8), _Remove__before_eq_(5, 3)]
>>> sf.verify()
>>> sf
DoublyList4Idc__rollbackable(9, [5, 3, 8])



>>> sf.rollback(opaque_position3)
>>> sf
DoublyList4Idc__rollbackable(9, [8, 3])
>>> opaque_position3 is sf.tell()
True
>>> sf.rollback(opaque_position3)
>>> sf
DoublyList4Idc__rollbackable(9, [8, 3])

>>> sf.rollback(opaque_position2)
>>> sf
DoublyList4Idc__rollbackable(9, [2, 8, 3])
>>> opaque_position2 is sf.tell()
True
>>> sf.rollback(opaque_position1)
>>> sf
DoublyList4Idc__rollbackable(9, [3, 2, 8])
>>> opaque_position1 is sf.tell()
True
>>> sf.rollback(opaque_position0)
>>> sf
DoublyList4Idc__rollbackable(9, [])
>>> opaque_position0 is sf.tell()
True

>>> sf._rollback_ls
[_Do_nothing()]
>>> _Do_nothing() == _Do_nothing()
False

#####
#####




#]]]'''
__all__ = r'''
DoublyList4Idc
    DoublyList4Idc__rollbackable
'''.split()#'''
__all__
from seed.helper.repr_input import repr_helper
from seed.tiny_.check import check_uint_lt, check_uint, check_type_is
#from seed.tiny import print_err

def _prime_modifier(f, /):
    f.__is_prime_modifier__ = True
    return f
def _get_nms4prime_modifier(T, /):
    return sorted(nm for nm in dir(T) if getattr(getattr(T, nm), '__is_prime_modifier__', False))

class DoublyList4Idc:
    r'''[[[
[[may_max1 is None] -> [dynamic_resize is True]]
[[list_vs_dict is True] -> [dynamic_resize is True]]
[[dynamic_resize is False] -> [[may_max1 :: uint][list_vs_dict is False]]]
#dynamic_resize:default:False unless impossible

[:new_concrete_methods4DoublyList4Idc]:here

py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.data_funcs.idc_mngr:DoublyList4Idc@T    =T    +exclude_attrs5listed_in_cls_doc

__repr__
__init__
__len__
__contains__
remove
discard
first
last
clear
pop_all
pop
move_to_end
put_or_move_to_end
puts
put
__iter__
__reversed__
verify


pop_first
pop_last
    pop
pop_after_
pop_before_
get_after_
    next_
    forward_
get_before_
    prev_
    backward_
put_after_
put_before_
move_to_after_
move_to_before_
put_or_move_to_after_
put_or_move_to_before_


check_contained_idx
set_first
put_after_may_

    #]]]'''#'''
    def __repr__(sf, /):
        sf.verify()
        (args4no_data, kwds) = _get_setting2(sf)
        return repr_helper(sf, *args4no_data, [*sf], **kwds)
    @_prime_modifier
    def __init__(sf, may_max1, idc, /, *, list_vs_dict=False, may_dynamic_resize=None):
        (max1__4init, dynamic_resize) = _prepare(may_max1, list_vs_dict, may_dynamic_resize)

        sf._ls_vs_d_ = list_vs_dict
        sf._dynamic_resize_ = dynamic_resize
        sf._may_max1 = may_max1
        ######################

        if sf._ls_vs_d_:
            assert sf._dynamic_resize_
            assert max1__4init == 0
            fwd = {}
            bwd = {}
        else:
            fwd = [None]*max1__4init
            bwd = [None]*max1__4init
        sf._fwd = fwd
        sf._bwd = bwd
        sf._may_j0 = None
        sf._sz = 0
        sf.puts(idc)
        return
    def __len__(sf, /):
        return sf._sz
    def __contains__(sf, j, /):
        #if sf._dynamic_resize_:
        check_uint(j)
        if not sf._may_max1 is None:
            max1 = sf._may_max1
            #check_uint_lt(max1, j)
            if not j < max1: raise IndexError(j)
        fwd = sf._fwd
        if sf._ls_vs_d_:
            return j in fwd
        if not j < len(fwd):
            return False
        return not fwd[j] is None
    def check_contained_idx(sf, j, /):
        if not j in sf:
            raise IndexError(j)

    def remove(sf, j, /):
        '-> None'
        #sf.check_contained_idx(j)
        if not sf.discard(j):
            raise IndexError(j)
    @_prime_modifier
    def discard(sf, j, /):
        '-> actually_remove/existed/bool'
        #注意: [j==first]:first 可能 退位给 snd
        if not j in sf:
            #non-existed
            #not remove
            return False
        fwd = sf._fwd
        bwd = sf._bwd
        if len(sf) == 1:
            sf._may_j0 = None
        else:
            j0 = sf.first
            if j0 == j:
                j1 = fwd[j0]
                sf.set_first(j0:=j1)
            next_j = fwd[j]
            prev_j = bwd[j]
            fwd[prev_j] = next_j
            bwd[next_j] = prev_j
        #__erase__#see:__extend__
        if sf._ls_vs_d_:
            del fwd[j]
            del bwd[j]
            assert sf._dynamic_resize_
        else:
            fwd[j] = None
            bwd[j] = None
            if sf._dynamic_resize_:
                while fwd and fwd[-1] is None:
                    fwd.pop()
                    bwd.pop()
        sf._sz -= 1
        return True
    @_prime_modifier
    def set_first(sf, j, /):
        '-> actually_changed/bool'
        sf.check_contained_idx(j)
        if j == sf.first:
            return False
        sf._may_j0 = j
        return True
    @property
    def first(sf, /):
        if not sf:
            raise IndexError('first')
        j0 = sf._may_j0
        return j0
        (j0, last_j) = _get__j0__last_j(sf)
        return j0
    #@_prime_modifier
    #first = first.setter(set_first)
    @property
    def last(sf, /):
        if not sf:
            raise IndexError('last')
        (j0, last_j) = _get__j0__last_j(sf)
        return last_j
    def clear(sf, /):
        while sf:
            sf.pop()
    def pop_all(sf, /):
        idc = [*sf]
        sf.clear()
        return idc
    def pop_first(sf, /):
        '-> idx/uint'
        sf.remove(j:=sf.first)
        return j
    def pop_last(sf, /):
        '-> idx/uint'
        sf.remove(j:=sf.last)
        return j
    pop = pop_last

    def pop_after_(sf, i, /):
        '-> idx/uint'
        j = sf.get_after_(i)
        sf.remove(j)
        return j
    def pop_before_(sf, i, /):
        '-> idx/uint'
        j = sf.get_before_(i)
        sf.remove(j)
        return j
    def get_after_(sf, i, /):
        '-> idx/uint'
        sf.check_contained_idx(i)
        return sf._fwd[i]
    def get_before_(sf, i, /):
        '-> idx/uint'
        sf.check_contained_idx(i)
        return sf._bwd[i]
    next_ = forward_ = get_after_
    prev_ = backward_ = get_before_
    #@_prime_modifier
    def put_after_(sf, i, j, /):
        '-> actually_put/non_existed/bool'
        if i is None: raise TypeError(type(i))
            #raise IndexError(i)
        return sf.put_after_may_(i, j)
        #注意: first 可能 退位给 j
        #下面不行:
        k = sf.get_after_(i)
        return sf.put_before_(k, j)
    def put_before_(sf, i, j, /):
        '-> actually_put/non_existed/bool'
        #注意: first 可能 退位给 j
        prev_i = sf.get_before_(i)
        r = sf.put_after_(prev_i, j)
        if r and i == sf.first:
            sf.set_first(j)
        return r


    def move_to_after_(sf, i, j, /):
        '-> None'
        #注意: [j==first]:first 可能 退位给 next_j/snd
        #if 0b0001:print_err('move_to_after_', i, j)
        k = sf.get_after_(i)
            # ^indexerror
            #   必要性:when [j==i]
        #bug:if j == i or j == k:
        if j == i:
            pass
        elif j == k:
            if j == sf.first:
                snd = sf.get_after_(j)
                sf.set_first(snd)
        else:
            sf.remove(j)
            sf.put_after_(i, j)
            #if 0b0001:print_err('move_to_after_', i, j, k)
        return
        #上面:只有一种退位可能性
        #下面:有两种退位可能性
        #下面不行: !!退位可能性不同
        k = sf.get_after_(i)
        return sf.move_to_before_(k, j)
    def move_to_before_(sf, i, j, /):
        '-> None'
        #注意: [i==j==first]:first 不变
        #注意: [i==first]:first 退位给 j
        #注意: [j==first]:first 可能 退位给 next_j/snd
        prev_i = sf.get_before_(i)
            # ^indexerror
            #   必要性:when [j==i]
        if j == i:
            return
        # [j =!= i]
        #bug:if j == prev_i: return
            # bug:when [i == j0]
        j0 = sf.first
        sf.move_to_after_(prev_i, j)
            #注意: [j==first]:first 可能 退位给 next_j/snd
        if i == j0:
            #bug:first changed!:if i == sf.first:
            # !! [j =!= i]
            # !! [i == j0]
            # !! [j =!= j0]
            sf.set_first(j)
        return
        #####
        prev_i = sf.get_before_(i)
            # ^indexerror
            #   必要性:when [j==i]
        if j == i:
            pass
        elif j == prev_i:
            if i == sf.first:
                sf.set_first(j)
        else:
            sf.remove(j)
            sf.put_before_(i, j)
                #注意: first 可能 退位给 j
        return
        #####
        if j == i:
            sf.get_before_(i)
                # ^IndexError
        else:
            sf.remove(j)
            sf.put_before_(i, j)
        #####


    def put_or_move_to_after_(sf, i, j, /):
        '-> actually_put/non_existed/bool'
        #注意: [j==first]:first 可能 退位给 next_j/snd
        r = sf.put_after_(i, j)
        if not r:
            sf.move_to_after_(i, j)
        return r
        #下面不行: !!退位可能性不同
        k = sf.get_after_(i)
        return sf.put_or_move_to_before_(k, j)
    def put_or_move_to_before_(sf, i, j, /):
        '-> actually_put/non_existed/bool'
        #注意: [i==j==first]:first 不变
        #注意: [i==first]:first 退位给 j
        #注意: [j==first]:first 可能 退位给 next_j/snd
        r = sf.put_before_(i, j)
        if not r:
            sf.move_to_before_(i, j)
        return r

    def move_to_end(sf, j, /):
        '-> None'
        #注意: [j==first]:first 可能 退位给 next_j/snd
        #
        #bug:退位可能性不同:return sf.move_to_before_(sf.first, j)
        #if 0b0001:print_err('move_to_end', j)
        return sf.move_to_after_(sf.last, j)
        sf.remove(j)
        sf.put(j)
    def put_or_move_to_end(sf, j, /):
        '-> actually_put/non_existed/bool'
        #注意: [j==first]:first 可能 退位给 next_j/snd
        #
        #bug:退位可能性不同:return sf.put_or_move_to_before_(sf.first, j)
        return sf.put_or_move_to_after_(sf.last, j)
        r = sf.put(j)
        if not r:
            sf.move_to_end(j)
        return r
    def puts(sf, idc, /):
        '-> (total, num_actually_put)/(uint,uint)'
        sz0 = len(sf)
        put = sf.put
        total = 0
        for total, _ in enumerate(map(put, idc), 1):
            pass
            #put(j)
        num_actually_put = len(sf) -sz0
        return (total, num_actually_put)
    #@_prime_modifier
    def put(sf, j, /):
        '-> actually_put/non_existed/bool'
        return sf.put_after_may_(None, j)
    @_prime_modifier
    def put_after_may_(sf, may_i, j, /):
        '-> actually_put/non_existed/bool'
        #see:put_after_/put
        #
        #if may_i is None:
        # if sf <==> (put j after last)
        # =!= (put j before first)
        #   !! (put j before first) => reset [sf.first := j]
        #
        #
        #
        #bug:return sf.put_before_(sf.first, j)
        #   #注意: first 可能 退位给 j
        if may_i is None:
            #may_last
            pass
        else:
            i = may_i
            k = sf.get_after_(i)
                # ^IndexError
            #assert sf
            ##########
            # i -> k
            ##########

        if j in sf:
            #already-existed
            #not put
            return False
        # [0 <= j < sf._may_max1]
        #   otherwise:__contains__ ^IndexError|^TypeError
        #
        fwd = sf._fwd
        bwd = sf._bwd
        if sf._dynamic_resize_ and not sf._ls_vs_d_:
            if not j < len(fwd):
                ns = [None]*(j+1 -len(fwd))
                #__extend__#see:__erase__
                # !! [0 <= j < sf._may_max1]
                fwd += ns
                bwd += ns
                assert j+1 == len(fwd)
        if not sf:
            #assert may_i is None
            sf._may_j0 = j0 = j
                #xxx:sf.set_first(j)
            fwd[j] = j
            bwd[j] = j
        else:
            if may_i is None:
                #(j0, last_j) = _get__j0__last_j(sf)
                j0 = sf._may_j0
                ##########
                # last_j -> j0
                last_j = bwd[j0]
                ##########
            else:
                ##########
                # i -> k
                ##########
                last_j = i
                j0 = k
                ##########
                # last_j -> j0
                ##########
            ##########
            # last_j -> j0
            ##########
            # last_j -> j -> j0
            fwd[last_j] = j
            fwd[j] = j0
            ##########
            # last_j <- j <- j0
            bwd[j0] = j
            bwd[j] = last_j
            ##########
        sf._sz += 1
        return True

    def __iter__(sf, /):
        if not sf:
            return
        j0 = sf._may_j0
        fwd = sf._fwd
        j = j0
        while 1:
            yield j
            j = fwd[j]
            if j == j0:break
    def __reversed__(sf, /):
        if not sf:
            return
        j0 = sf._may_j0
        bwd = sf._bwd
        j = j0
        while 1:
            j = bwd[j]
            yield j
            if j == j0:break
    def verify(sf, /):
        ######################
        dynamic_resize = sf._dynamic_resize_
        list_vs_dict = sf._ls_vs_d_
        may_max1 = sf._may_max1
        ######################
        sz = len(sf)
        fwd = sf._fwd
        bwd = sf._bwd
        assert (not sz) is (sf._may_j0 is None)
        assert len(fwd) == len(bwd)
        assert type(fwd) is type(bwd)
        assert type(fwd) is (dict if list_vs_dict else list)
        ######################
        if not dynamic_resize:
            # max1, list
            assert not may_max1 is None
            assert not list_vs_dict
        if not may_max1 is None:
            max1 = may_max1
            assert len(fwd) <= max1
        ######################
        js = [*iter(sf)]
        ks = [*reversed(sf)]
        assert len(js) == sz
        assert len(ks) == sz
        assert js == ks[::-1]
            #链表元素 一致
        if list_vs_dict:
            #dict
            assert dynamic_resize
            assert len(js) == len(fwd)
                #缓存无空位
        else:
            #list
            sz4buffer = len(fwd)
            assert fwd.count(None) == sz4buffer -sz
            assert bwd.count(None) == sz4buffer -sz
                #缓存空位 一致, 无垃圾
            if dynamic_resize:
                assert not fwd or fwd[-1] is not None
                    #缓存末尾非空位
        return

def _get_j0(sf, j, /):
    if not sf:
        return j
    return sf._may_j0
def _get__j0__last_j(sf, /):
    j0 = sf._may_j0
    last_j = sf._bwd[j0]
        #last_j <-- j0
    return j0, last_j
def _get_may_max1(sf, /):
    return sf._may_max1
    return (may_max1 := None if sf._dynamic_resize_ else len(sf._fwd))
def _get_setting2(sf, /):
    (may_max1, list_vs_dict, may_dynamic_resize) = _get_setting(sf)
    kwds = {}
    if list_vs_dict:
        kwds.update(list_vs_dict=True)
    if not may_dynamic_resize is None:
        kwds.update(may_dynamic_resize=may_dynamic_resize)
    kwds
    args4no_data = (may_max1,)
    return (args4no_data, kwds)
def _get_setting(sf, /):
    may_max1 = sf._may_max1
    list_vs_dict = sf._ls_vs_d_
    (max1__4init, dynamic_resize) = _prepare(may_max1, list_vs_dict, may_dynamic_resize:=None)
    expected = sf._dynamic_resize_
    if not dynamic_resize is expected:
        may_dynamic_resize = expected
    return (may_max1, list_vs_dict, may_dynamic_resize)
def _prepare(may_max1, list_vs_dict, may_dynamic_resize, /):
    if may_max1 is None:
        max1__4init = 0
    else:
        max1 = may_max1
        check_uint(max1)

    check_type_is(bool, list_vs_dict)
    if may_dynamic_resize is None:
        dynamic_resize = may_max1 is None or list_vs_dict
            #default:False unless impossible
    else:
        dynamic_resize = may_dynamic_resize
    dynamic_resize
    check_type_is(bool, dynamic_resize)

    ######################
    if (not dynamic_resize) and list_vs_dict: raise ValueError('irrational: fixed size of dict')
    if not dynamic_resize:
        if may_max1 is None: raise ValueError('size is unbound but forbid dynamic_resize')
        if list_vs_dict: raise ValueError('using dict but forbid dynamic_resize')
    ######################
    assert dynamic_resize or not (may_max1 is None or list_vs_dict)
    if dynamic_resize:
        max1__4init = 0
    else:
        assert not may_max1 is None
        max1__4init = max1
    max1__4init
    check_uint(max1__4init)
    return (max1__4init, dynamic_resize)
#end-class DoublyList4Idc:
assert (__:=_get_nms4prime_modifier(DoublyList4Idc)) == ['__init__', 'discard', 'put_after_may_', 'set_first'], __

class _IRollbackable:
    __slots__ = ()
    def tell(sf, /):
        '-> opaque_position/opaque-obj #see:rollback()'
    def rollback(sf, opaque_position, /):
        '-> None #see:tell()'
class DoublyList4Idc__rollbackable(DoublyList4Idc, _IRollbackable):
    r'''[[[
#see:_prime_modifier

[:new_concrete_methods4DoublyList4Idc__rollbackable]:here

py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.data_funcs.idc_mngr:DoublyList4Idc__rollbackable@T    =T    +exclude_attrs5listed_in_cls_doc

__init__
verify
tell
rollback
discard
put_after_may_
set_first


    #]]]'''#'''
    def __init__(sf, may_max1, idc, /, *, list_vs_dict=False, may_dynamic_resize=None):
        sf._rollback_ls = [_Do_nothing()]
        sf._rollbacking = False
        super().__init__(may_max1, idc, list_vs_dict=list_vs_dict, may_dynamic_resize=may_dynamic_resize)
    def verify(sf, /):
        super().verify()
        (args4no_data, kwds) = _get_setting2(sf)
        ot = __class__(*args4no_data, [], **kwds)
        for x in sf._rollback_ls:
            x.play_bwd(ot)
        assert ot._may_j0 == sf._may_j0
        assert len(ot) == len(sf)
        assert ot._fwd == sf._fwd
        assert ot._bwd == sf._bwd
    def tell(sf, /):
        '-> opaque_position/opaque-obj #see:rollback()'
        assert not sf._rollbacking
        ls = sf._rollback_ls
        if not ls[-1]._do_nothing_:
            ls.append(_Do_nothing())
            return sf.tell()
        opaque_position = ls[-1]
        assert opaque_position._do_nothing_
        return opaque_position
    def rollback(sf, opaque_position, /):
        '-> None #see:tell()'
        assert not sf._rollbacking
        if not isinstance(opaque_position, _IBidirectionPlayer): raise TypeError(type(opaque_position))
        if not opaque_position._do_nothing_: raise TypeError(type(opaque_position))
        ls = sf._rollback_ls
        for k, x in zip(reversed(range(len(ls))), reversed(ls)):
            if x is opaque_position:
                break
        else:
            raise ValueError(opaque_position)
        assert ls[k] is opaque_position
        sf._rollbacking = True
        sf._rollback_ls = None
        try:
            while not ls[-1] is opaque_position:
                x = ls.pop()
                x.play_fwd(sf)
        finally:
            sf._rollbacking = False
            sf._rollback_ls = ls
        assert ls[-1] is opaque_position
        assert len(ls) == k+1
        return

    def discard(sf, j, /):
        '-> actually_remove/existed/bool'
        if sf._rollbacking:
            return super().discard(j)
        existed = j in sf
        if existed:
            k = sf.get_after_(j)
            ls = sf._rollback_ls
            L = len(ls)
            j0 = sf.first
        r = super().discard(j)

                #注意: [j==first]:first 可能 退位给 k
        assert r is existed
        if existed:
            assert (k==j) is (not sf)
            if not sf:
                rollback_obj = _Put_into_empty(j)
            elif k == j0:
                rollback_obj = _Put__first_eq_(k, j)
                    #注意: 反演时[k==first]:first 不改变
            else:
                rollback_obj = _Put_before_(k, j)
                    #注意: 反演时[k==first]:first 可能 还位给 j
            del ls[L:]
            ls.append(rollback_obj)
        return r
    #def put(sf, j, /):
    def put_after_may_(sf, may_i, j, /):
        '-> actually_put/non_existed/bool'
        if sf._rollbacking:
            return super().put_after_may_(may_i, j)

        non_existed = not j in sf
        if non_existed:
            ls = sf._rollback_ls
            L = len(ls)
        r = super().put_after_may_(may_i, j)
        assert r is non_existed
        if non_existed:
            rollback_obj = _Pop__last_eq_(j) if may_i is None or j == sf.last else _Remove__before_eq_(i:=may_i, j)
            del ls[L:]
            ls.append(rollback_obj)
        return r
    def set_first(sf, j, /):
        '-> actually_changed/bool'
        if sf._rollbacking:
            return super().set_first(j)

        may_j0 = sf._may_j0
        if 1:
            ls = sf._rollback_ls
            L = len(ls)
        r = super().set_first(j)
            # ^IndexError
        # [check_contained_idx: j]
        # [len(sf) > 0]
        # [not$ may_j0 is None]
        j0 = may_j0
        actually_changed = not j == j0

        assert r is actually_changed
        if actually_changed:
            rollback_obj = _Set_first__old_eq_(j, j0)
            del ls[L:]
            ls.append(rollback_obj)
        return r
#end-class DoublyList4Idc__rollbackable(DoublyList4Idc, _IRollbackable):

assert issubclass(DoublyList4Idc__rollbackable, DoublyList4Idc)
assert not (__:=_get_nms4prime_modifier(DoublyList4Idc__rollbackable)), __
#class _IRollbackPlayer:
#    'see:_IRollbackable#may be play forward/backward_ hence args better be complete for bidirection play'
class _IBasePlayer:
    'see:_IRollbackable#may be play forward/backward_ hence args better be complete for bidirection play'
    __slots__ = ()
    _do_nothing_ = False
class _IForwardPlayer(_IBasePlayer):
    def play_fwd(sf, doubly_list, /):
        assert doubly_list._rollbacking
        sf._play_fwd_(doubly_list)
    def _play_fwd_(sf, doubly_list, /):
        raise NotImplementedError
class _IBackwardPlayer(_IBasePlayer):
    __slots__ = ()
    def play_bwd(sf, doubly_list, /):
        assert not doubly_list._rollbacking
        sf._play_bwd_(doubly_list)
    def _play_bwd_(sf, doubly_list, /):
        raise NotImplementedError
class _IBidirectionPlayer(_IBackwardPlayer,_IForwardPlayer):
    __slots__ = ()
class __0(_IBidirectionPlayer):
    __slots__ = ()
    def __init__(sf, /):
        return
    def __repr__(sf, /):
        return repr_helper(sf)
class __1(_IBidirectionPlayer):
    def __init__(sf, j, /):
        sf._j = j
    def __repr__(sf, /):
        return repr_helper(sf, sf._j)
class __2(_IBidirectionPlayer):
    def __init__(sf, i, j, /):
        sf._i = i
        sf._j = j
        assert not i == j
    def __repr__(sf, /):
        return repr_helper(sf, sf._i, sf._j)
class _Do_nothing(__0):
    'used by: DoublyList4Idc__rollbackable.tell()'
    _do_nothing_ = True
    def _play_fwd_(sf, doubly_list, /):
        return
    def _play_bwd_(sf, doubly_list, /):
        return
class _Put_before_(__2):
    def _play_fwd_(sf, doubly_list, /):
        doubly_list.put_before_(sf._i, sf._j)
    def _play_bwd_(sf, doubly_list, /):
        assert doubly_list.get_after_(sf._j) == sf._i
        doubly_list.pop_before_(sf._i)
class _Put__first_eq_(__2):
    def _play_fwd_(sf, doubly_list, /):
        assert doubly_list.first == sf._i
        doubly_list.put(sf._j)
    def _play_bwd_(sf, doubly_list, /):
        assert doubly_list.first == sf._i
        assert doubly_list.last == sf._j
        doubly_list.pop()
class _Put_into_empty(__1):
    def _play_fwd_(sf, doubly_list, /):
        assert not doubly_list
        doubly_list.put(sf._j)
    def _play_bwd_(sf, doubly_list, /):
        assert len(doubly_list) == 1
        assert doubly_list.first == sf._j
        doubly_list.pop()
class _Remove__before_eq_(__2):
    def _play_fwd_(sf, doubly_list, /):
        assert doubly_list.get_before_(sf._j) == sf._i
        doubly_list.remove(sf._j)
    def _play_bwd_(sf, doubly_list, /):
        doubly_list.put_after_(sf._i, sf._j)
class _Pop__last_eq_(__1):
    def _play_fwd_(sf, doubly_list, /):
        assert doubly_list.last == sf._j
        doubly_list.pop()
    def _play_bwd_(sf, doubly_list, /):
        doubly_list.put(sf._j)
class _Set_first__old_eq_(__2):
    def _play_fwd_(sf, doubly_list, /):
        assert doubly_list.first == sf._i
        doubly_list.set_first(sf._j)
    def _play_bwd_(sf, doubly_list, /):
        assert doubly_list.first == sf._j
        doubly_list.set_first(sf._i)

assert not _Do_nothing() is _Do_nothing()
assert not _Do_nothing() == _Do_nothing()
__all__



from seed.data_funcs.idc_mngr import DoublyList4Idc, DoublyList4Idc__rollbackable
from seed.data_funcs.idc_mngr import *
