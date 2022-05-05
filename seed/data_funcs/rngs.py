#__all__:goto

r'''[[[[[
py -m seed.data_funcs.rngs
py -m nn_ns.app.debug_cmd   seed.data_funcs.rngs
from seed.data_funcs.rngs import make_Ranges, sorted_ints_to_iter_nontouch_ranges, detect_iter_ranges, StackStyleSimpleIntSet, StackStyleSimpleIntMapping, TouchRangeBasedIntMapping
##from seed.data_funcs.rngs import ranges2hex_repr_pair_list, ranges5hex_repr_pair_list

    iter_rngs2iter_hexXhexszpair_list
    iter_rngs5iter_hexXhexszpair_list
    ranges2hexXhexszpair_list
    ranges5hexXhexszpair_list

    ranges2len_rng2hexbegins
    ranges5len_rng2hexbegins
    ranges2len_rng2hexbegins_str
    ranges5len_rng2hexbegins_str
    ranges2len_rng2begin_chars
    ranges5len_rng2begin_chars

===============================
===============================
NOTE: use IRanges.set_eq instead of "=="
===============================
===============================
main_exports:
    make_Ranges
    sorted_ints_to_iter_nontouch_ranges
    detect_iter_ranges
    StackStyleSimpleIntSet
    StackStyleSimpleIntMapping
    TouchRangeBasedIntMapping
===============================
===============================
rngs = [rng] = iter<rng>
rng = (begin:int, end:int)
    begin < end


nonoverlap_rngs
    assert valid_touch_ranges(sorted(nonoverlap_rngs))
sorted_rngs
    assert [*sorted_rngs] == sorted(sorted_rngs)
touch_ranges
    assert nontouch_ranges[i][1] <= nontouch_ranges[i+1][0]
nontouch_ranges
    assert nontouch_ranges[i][1] < nontouch_ranges[i+1][0]
xtouch_ranges
    =[def]= nontouch_ranges | touch_ranges
    === touch_ranges

nontouch_ranges <: touch_ranges <: (sorted_rngs & nonoverlap_rngs) <: rng_seq






[[[

=====================
>>> nontouch_ranges = make_NonTouchRanges([(0,2), (3,4), (5,7)])
>>> nontouch_ranges.contains_all([(0,1), 3, 6, (0,2), (6,7)])
True
>>> 2 not in nontouch_ranges
True
>>> nontouch_ranges.gaps()
((2, 3), (4, 5))

>>> touch_ranges = make_TouchRanges([(0,3), (3,4), (5,7)])
>>> touch_ranges.contains_all([(0,4), 3, 6, (0,2), (6,7),])
True
>>> 4 not in touch_ranges
True
>>> touch_ranges.gaps()
((4, 5),)




=====================

>>> from seed.func_tools.dot2 import dot

>>> f=dot[tuple, sorted_unique_ints_to_iter_nontouch_ranges]
>>> f([0,1,3])
((0, 2), (3, 4))
>>> f([0])
((0, 1),)
>>> f([])
()


#>>> dot = lambda f,g: lambda *args, **kw: f(g(*args, **kw))
#>>> f=dot(sorted_unique_ints_to_nontouch_ranges, iter)
#>>> f=dot[sorted_unique_ints_to_nontouch_ranges, iter]
>>> f=dot[tuple, sorted_unique_ints_to_iter_nontouch_ranges, iter]
>>> f([])
()
>>> f([0])
((0, 1),)
>>> f([-1, 0, 1, 3, 4, 6, 8])
((-1, 2), (3, 5), (6, 7), (8, 9))

#>>> f=dot(len_ints_of_nonoverlap_rngs, iter)
>>> f=dot[len_ints_of_nonoverlap_rngs, iter]
>>> f([])
0
>>> f([(0,8)])
8
>>> f([(3, 5), (-1, 3), (6, 7)])
7

#>>> f=dot(list, dot(sorted_rngs_to_iter_nontouch_ranges, iter))
>>> f=dot[list, sorted_rngs_to_iter_nontouch_ranges, iter]
>>> f([])
[]
>>> f([(4, 7)])
[(4, 7)]
>>> f([(4, 7), (4, 7), (4, 8), (5, 7), (5, 8), (7, 8), (8, 9), (9,11), (12, 14)])
[(4, 11), (12, 14)]


>>> _gen_test_cases()
#[(lhs, rhs), (oF, oT, xF, xT, a, d, cmp, rels)]
[([(3, 6)], [(1, 2)]), ([(1, 2), (3, 6)], [(1, 2), (3, 6)], [(1, 2), (3, 6)], [(1, 2), (3, 6)], [], [(3, 6)], 1, [5, 0])]
[([(3, 6)], [(1, 3)]), ([(1, 6)], [(1, 6)], [(1, 6)], [(1, 3), (3, 6)], [], [(3, 6)], 1, [0])]
[([(3, 6)], [(1, 4)]), ([(1, 6)], [(1, 6)], [(1, 3), (4, 6)], [(1, 3), (4, 6)], [(3, 4)], [(4, 6)], 1, [0])]
[([(3, 6)], [(1, 6)]), ([(1, 6)], [(1, 6)], [(1, 3)], [(1, 3)], [(3, 6)], [], -1, [5, 1])]
[([(3, 6)], [(1, 7)]), ([(1, 7)], [(1, 7)], [(1, 3), (6, 7)], [(1, 3), (6, 7)], [(3, 6)], [], -1, [5, 1])]
[([(3, 6)], [(3, 4)]), ([(3, 6)], [(3, 6)], [(4, 6)], [(4, 6)], [(3, 4)], [(4, 6)], 1, [6, 2])]
[([(3, 6)], [(3, 6)]), ([(3, 6)], [(3, 6)], [], [], [(3, 6)], [], 0, [3])]
[([(3, 6)], [(3, 7)]), ([(3, 7)], [(3, 7)], [(6, 7)], [(6, 7)], [(3, 6)], [], -1, [5, 1])]
[([(3, 6)], [(4, 5)]), ([(3, 6)], [(3, 6)], [(3, 4), (5, 6)], [(3, 4), (5, 6)], [(4, 5)], [(3, 4), (5, 6)], 1, [6, 2])]
[([(3, 6)], [(4, 6)]), ([(3, 6)], [(3, 6)], [(3, 4)], [(3, 4)], [(4, 6)], [(3, 4)], 1, [6, 2])]
[([(3, 6)], [(4, 7)]), ([(3, 7)], [(3, 7)], [(3, 4), (6, 7)], [(3, 4), (6, 7)], [(4, 6)], [(3, 4)], 1, [0])]
[([(3, 6)], [(6, 7)]), ([(3, 7)], [(3, 7)], [(3, 7)], [(3, 6), (6, 7)], [], [(3, 6)], 1, [0])]
[([(3, 6)], [(7, 8)]), ([(3, 6), (7, 8)], [(3, 6), (7, 8)], [(3, 6), (7, 8)], [(3, 6), (7, 8)], [], [(3, 6)], 1, [6, 0])]



>>> kwF = dict(faster_output_iter_touch_ranges=False)
>>> kwT = dict(faster_output_iter_touch_ranges=True)
>>> f=dot[list, symmetric_difference_ex__xtouch_ranges]
>>> f([(-1,0),(1,2),(3,5),(7,9)], [(-1,0),(2,3),(4,8),(8,9)], **kwF)
[(1, 4), (5, 7)]
>>> f([(-1,0),(1,2),(3,5),(7,9)], [(-1,0),(2,3),(4,8),(8,9)], **kwT)
[(1, 2), (2, 3), (3, 4), (5, 7)]


>>> f=dot[list, union_ex__xtouch_ranges]
>>> f([(-1,0),(1,2),(3,5),(7,9)], [(-1,0),(2,3),(4,8),(8,9)], **kwF)
[(-1, 0), (1, 9)]
>>> f([(-1,0),(1,2),(3,5),(7,9)], [(-1,0),(2,3),(4,8),(8,9)], **kwT)
[(-1, 0), (1, 3), (3, 8), (8, 9)]

>>> f=dot[list, intersection__xtouch_ranges]
>>> f([(-1,0),(1,2),(3,5),(7,9)], [(-1,0),(2,3),(4,8),(8,9)])
[(-1, 0), (4, 5), (7, 8), (8, 9)]


>>> f=dot[list, difference__xtouch_ranges]
>>> f([(-1,0),(1,2),(3,5),(7,9)], [(-1,0),(2,3),(4,8),(8,9)])
[(1, 2), (3, 4)]




>>> kwF = dict(rhs_maynot_be_nontouch_ranges=False)
>>> kwT = dict(rhs_maynot_be_nontouch_ranges=True)
>>> f=subset_cmp_ex__xtouch_ranges
>>> f([(-1,0),(1,2),(3,5),(7,9)], [(-1,0),(2,3),(4,8),(8,9)], **kwT)
1
>>> f([(-1,0),(4,5),(7,9)], [(-1,0),(2,3),(4,8),(8,9)], **kwT)
-1
>>> f([(-1,0),(2,3),(4,5),(5,7),(7,9)], [(-1,0),(2,3),(4,8),(8,9)], **kwT)
0

>>> lkwF = dict(lhs_maynot_be_nontouch_ranges=False)
>>> lkwT = dict(lhs_maynot_be_nontouch_ranges=True)
>>> f=is_equal_set_ex_of__xtouch_ranges
>>> f([(-1,0),(1,2),(3,5),(7,9)], [(-1,0),(2,3),(4,8),(8,9)], **kwT, **lkwF)
False
>>> f([(-1,0),(4,5),(7,9)], [(-1,0),(2,3),(4,8),(8,9)], **kwT, **lkwF)
False
>>> f([(-1,0),(2,3),(4,5),(5,7),(7,9)], [(-1,0),(2,3),(4,8),(8,9)], **kwT, **lkwT)
True


>>> f=is_subset_ex_of__xtouch_ranges
>>> f([(-1,0),(1,2),(3,5),(7,9)], [(-1,0),(2,3),(4,8),(8,9)], **kwT)
False
>>> f([(-1,0),(4,5),(7,9)], [(-1,0),(2,3),(4,8),(8,9)], **kwT)
True
>>> f([(-1,0),(2,3),(4,5),(5,7),(7,9)], [(-1,0),(2,3),(4,8),(8,9)], **kwT)
True

>>> f=is_proper_subset_ex_of__xtouch_ranges
>>> f([(-1,0),(1,2),(3,5),(7,9)], [(-1,0),(2,3),(4,8),(8,9)], **kwT)
False
>>> f([(-1,0),(4,5),(7,9)], [(-1,0),(2,3),(4,8),(8,9)], **kwT)
True
>>> f([(-1,0),(2,3),(4,5),(5,7),(7,9)], [(-1,0),(2,3),(4,8),(8,9)], **kwT)
False




>>> lhs = make_Ranges([(-1,0),(1,2),(3,5),(7,9)])
>>> lhs2 = make_Ranges([(-1,0),(4,5),(7,9)])
>>> lhs3 = make_Ranges([(-1,0),(2,3),(4,5),(5,7),(7,9)])
>>> rhs = make_Ranges([(-1,0),(2,3),(4,8),(8,9)])
>>> lhs
NonTouchRanges(((-1, 0), (1, 2), (3, 5), (7, 9)))
>>> lhs2
NonTouchRanges(((-1, 0), (4, 5), (7, 9)))
>>> lhs3
TouchRanges(((-1, 0), (2, 3), (4, 5), (5, 7), (7, 9)))
>>> rhs
TouchRanges(((-1, 0), (2, 3), (4, 8), (8, 9)))
>>> lhs ^ rhs
NonTouchRanges(((1, 4), (5, 7)))
>>> lhs | rhs
NonTouchRanges(((-1, 0), (1, 9)))
>>> lhs & rhs
NonTouchRanges(((-1, 0), (4, 5), (7, 9)))
>>> lhs - rhs
NonTouchRanges(((1, 2), (3, 4)))

>>> lhs == lhs
True
>>> rhs == rhs
True

>>> lhs == rhs
False
>>> lhs.set_eq(rhs)
False
>>> lhs <= rhs
False
>>> lhs < rhs
False

>>> lhs2 == rhs
False
>>> lhs2.set_eq(rhs)
False
>>> lhs2 <= rhs
True
>>> lhs2 < rhs
True

>>> lhs3 == rhs #!!!!!!!!!!!!!!!!!!!!!!!!!
False
>>> lhs3.set_eq(rhs)
True
>>> lhs3 <= rhs
True
>>> lhs3 < rhs
False






[[
StackStyleSimpleIntSet
>>> s = StackStyleSimpleIntSet()
>>> s
StackStyleSimpleIntSet([])
>>> len(s)
0
>>> s.add(1)
>>> s.add(2)
>>> s.add(3)
>>> s.add(4)
>>> s.get_top()
4
>>> s.add(6)
>>> len(s)
5
>>> s.push(7)
>>> s.push(8)
>>> s.push(10)
>>> len(s)
8
>>> s.get_top()
10
>>> s
StackStyleSimpleIntSet([(1, 5), (6, 9), (10, 11)])
>>> s.pop()
10
>>> len(s)
7
>>> s
StackStyleSimpleIntSet([(1, 5), (6, 9)])

>>> s.get_top()
8
>>> s.pop()
8
>>> len(s)
6
>>> s
StackStyleSimpleIntSet([(1, 5), (6, 8)])

>>> s.get_top()
7
>>> s.pop()
7
>>> len(s)
5

>>> s.get_top()
6
>>> s.pop()
6
>>> len(s)
4
>>> s
StackStyleSimpleIntSet([(1, 5)])

>>> s.get_top()
4
>>> s.pop()
4
>>> len(s)
3

>>> s.get_top()
3
>>> s.pop()
3
>>> len(s)
2

>>> s.get_top()
2
>>> s.pop()
2
>>> len(s)
1

>>> s.get_top()
1
>>> s.pop()
1
>>> len(s)
0
>>> s
StackStyleSimpleIntSet([])

>>> s.get_top()
Traceback (most recent call last):
    ...
KeyError: 'get_top from an empty set'

>>> s.pop()
Traceback (most recent call last):
    ...
KeyError: 'pop from an empty set'

>>> StackStyleSimpleIntSet.from_clone_of_rngs([(1,2),(2,3),(4,5)])
StackStyleSimpleIntSet([(1, 3), (4, 5)])


]]
[[
@20220503:StackStyleSimpleIntSet ++new methods:
    push_rngs
    push_rng
    __delitem__
    iter_intersect_range_ex
    __iter__
    __reversed__
    iter_keys_
    iter_rngs_
    maybe_range_contained
    maybe_range_contained_ex
    __contains__
    contains_range
    contains_all



StackStyleSimpleIntSet
>>> s = StackStyleSimpleIntSet()
>>> s
StackStyleSimpleIntSet([])
>>> len(s)
0


push_rngs
push_rng
__delitem__
iter_intersect_range_ex
>>> del s[0]
Traceback (most recent call last):
    ...
KeyError: '__delitem__ from an empty set'

>>> s.push_rng((1,5))
>>> s.get_top()
4
>>> s.push_rngs([(6,7), (7,9), (10,11)])
>>> len(s)
8
>>> s.get_top()
10
>>> s
StackStyleSimpleIntSet([(1, 5), (6, 9), (10, 11)])
>>> del s[11]
Traceback (most recent call last):
    ...
KeyError: 'stack_styple-int-set: __delitem__(i) but i == 11 != 10 == top'
>>> del s[9]
Traceback (most recent call last):
    ...
KeyError: 'stack_styple-int-set: __delitem__(i) but i == 9 != 10 == top'
>>> del s[8]
Traceback (most recent call last):
    ...
KeyError: 'stack_styple-int-set: __delitem__(i) but i == 8 != 10 == top'
>>> s
StackStyleSimpleIntSet([(1, 5), (6, 9), (10, 11)])
>>> del s[10]
>>> len(s)
7
>>> s
StackStyleSimpleIntSet([(1, 5), (6, 9)])

>>> s.push_rng((13, 15))
>>> s
StackStyleSimpleIntSet([(1, 5), (6, 9), (13, 15)])

>>> [*s.iter_intersect_range_ex((-1,0))]
[]
>>> [*s.iter_intersect_range_ex((0,1))]
[]
>>> [*s.iter_intersect_range_ex((5,6))]
[]
>>> [*s.iter_intersect_range_ex((10,11))]
[]
>>> [*s.iter_intersect_range_ex((15,16))]
[]


>>> [*s.iter_intersect_range_ex((0,1))]
[]
>>> [*s.iter_intersect_range_ex((0,3))]
[(0, (1, 3))]
>>> [*s.iter_intersect_range_ex((0,5))]
[(0, (1, 5))]
>>> [*s.iter_intersect_range_ex((0,6))]
[(0, (1, 5))]

>>> [*s.iter_intersect_range_ex((0,7))]
[(0, (1, 5)), (1, (6, 7))]
>>> [*s.iter_intersect_range_ex((0,9))]
[(0, (1, 5)), (1, (6, 9))]
>>> [*s.iter_intersect_range_ex((0,10))]
[(0, (1, 5)), (1, (6, 9))]
>>> [*s.iter_intersect_range_ex((0,13))]
[(0, (1, 5)), (1, (6, 9))]

>>> [*s.iter_intersect_range_ex((0,14))]
[(0, (1, 5)), (1, (6, 9)), (2, (13, 14))]
>>> [*s.iter_intersect_range_ex((0,15))]
[(0, (1, 5)), (1, (6, 9)), (2, (13, 15))]
>>> [*s.iter_intersect_range_ex((0,16))]
[(0, (1, 5)), (1, (6, 9)), (2, (13, 15))]


>>> [*s.iter_intersect_range_ex((2,3))]
[(0, (2, 3))]
>>> [*s.iter_intersect_range_ex((2,5))]
[(0, (2, 5))]
>>> [*s.iter_intersect_range_ex((2,6))]
[(0, (2, 5))]

>>> [*s.iter_intersect_range_ex((2,7))]
[(0, (2, 5)), (1, (6, 7))]
>>> [*s.iter_intersect_range_ex((2,9))]
[(0, (2, 5)), (1, (6, 9))]
>>> [*s.iter_intersect_range_ex((2,10))]
[(0, (2, 5)), (1, (6, 9))]
>>> [*s.iter_intersect_range_ex((2,13))]
[(0, (2, 5)), (1, (6, 9))]

>>> [*s.iter_intersect_range_ex((2,14))]
[(0, (2, 5)), (1, (6, 9)), (2, (13, 14))]
>>> [*s.iter_intersect_range_ex((2,15))]
[(0, (2, 5)), (1, (6, 9)), (2, (13, 15))]
>>> [*s.iter_intersect_range_ex((2,16))]
[(0, (2, 5)), (1, (6, 9)), (2, (13, 15))]

>>> [*s.iter_intersect_range_ex((5,6))]
[]

>>> [*s.iter_intersect_range_ex((5,7))]
[(1, (6, 7))]
>>> [*s.iter_intersect_range_ex((5,9))]
[(1, (6, 9))]
>>> [*s.iter_intersect_range_ex((5,10))]
[(1, (6, 9))]
>>> [*s.iter_intersect_range_ex((5,13))]
[(1, (6, 9))]

>>> [*s.iter_intersect_range_ex((5,14))]
[(1, (6, 9)), (2, (13, 14))]
>>> [*s.iter_intersect_range_ex((5,15))]
[(1, (6, 9)), (2, (13, 15))]
>>> [*s.iter_intersect_range_ex((5,16))]
[(1, (6, 9)), (2, (13, 15))]



__iter__
__reversed__
iter_keys_
iter_rngs_
>>> [*iter(s)]
[1, 2, 3, 4, 6, 7, 8, 13, 14]
>>> [*reversed(s)]
[14, 13, 8, 7, 6, 4, 3, 2, 1]
>>> [*s.iter_keys_(reverse=False)]
[1, 2, 3, 4, 6, 7, 8, 13, 14]
>>> [*s.iter_keys_(reverse=True)]
[14, 13, 8, 7, 6, 4, 3, 2, 1]
>>> [*s.iter_rngs_(reverse=False)]
[(1, 5), (6, 9), (13, 15)]
>>> [*s.iter_rngs_(reverse=True)]
[(13, 15), (6, 9), (1, 5)]


maybe_range_contained
maybe_range_contained_ex
__contains__
contains_range
contains_all
>>> s.maybe_range_contained(0)
>>> s.maybe_range_contained(5)
>>> s.maybe_range_contained(9)
>>> s.maybe_range_contained(10)
>>> s.maybe_range_contained(15)

>>> s.maybe_range_contained(1)
(1, 5)
>>> s.maybe_range_contained(2)
(1, 5)
>>> s.maybe_range_contained(4)
(1, 5)
>>> s.maybe_range_contained(6)
(6, 9)
>>> s.maybe_range_contained(7)
(6, 9)
>>> s.maybe_range_contained(8)
(6, 9)
>>> s.maybe_range_contained(13)
(13, 15)
>>> s.maybe_range_contained(14)
(13, 15)


>>> s.maybe_range_contained_ex(0)
(None, -1)
>>> s.maybe_range_contained_ex(5)
(None, 0)
>>> s.maybe_range_contained_ex(9)
(None, 1)
>>> s.maybe_range_contained_ex(10)
(None, 1)
>>> s.maybe_range_contained_ex(15)
(None, 2)
>>> s.maybe_range_contained_ex(16)
(None, 2)

>>> s.maybe_range_contained_ex(1)
((1, 5), 0)
>>> s.maybe_range_contained_ex(2)
((1, 5), 0)
>>> s.maybe_range_contained_ex(4)
((1, 5), 0)
>>> s.maybe_range_contained_ex(6)
((6, 9), 1)
>>> s.maybe_range_contained_ex(7)
((6, 9), 1)
>>> s.maybe_range_contained_ex(8)
((6, 9), 1)
>>> s.maybe_range_contained_ex(13)
((13, 15), 2)
>>> s.maybe_range_contained_ex(14)
((13, 15), 2)


>>> 0 in s
False
>>> 5 in s
False
>>> 9 in s
False
>>> 10 in s
False
>>> 15 in s
False

>>> 1 in s
True
>>> 2 in s
True
>>> 4 in s
True
>>> 6 in s
True
>>> 7 in s
True
>>> 8 in s
True
>>> 13 in s
True
>>> 14 in s
True


>>> (0, 4) in s
False
>>> (1, 4) in s
True
>>> (1, 5) in s
True
>>> (2, 5) in s
True
>>> (2, 6) in s
False
>>> (2, 7) in s
False


>>> s.contains_range((2,5))
True
>>> s.contains_range((2,7))
False
>>> s.contains_range((5,7))
False

>>> s.contains_all([])
True
>>> s.contains_all([(2,3), 1])
True
>>> s.contains_all([(2,3), 1, (5,7)])
False

]]
[[
@20220503:++new class StackStyleSimpleIntMapping
    push_rng_value_pairs
    push_rng_value
    push
    __setitem__
    get_top
    pop
    __delitem__
    __len__
    __repr__

    from_clone_of_rngs_with_default
    __getitem__
    getitem4int

    iter_intersect_range_ex
    __iter__
    __reversed__
    iter_keys_
    iter_rngs_
    iter_values__per_rng_
    iter_rng_value_pairs_
    items
    reversed_items
    iter_items_

    maybe_range_contained
    maybe_range_contained_ex
    __contains__
    contains_range
    contains_all

[[
StackStyleSimpleIntMapping
    push
    __setitem__
    get_top
    pop
    __len__
    __repr__
    from_clone_of_rngs_with_default
>>> s = StackStyleSimpleIntMapping()
>>> s
StackStyleSimpleIntMapping(([], []))
>>> len(s)
0
>>> s[1] = 111
>>> s[2] = 111
>>> s[3] = 111
>>> s[4] = 111
>>> s.get_top()
(4, 111)
>>> s[6] = 111
>>> len(s)
5
>>> s.push(7, 222)
>>> s.push(8, 222)
>>> s.push(10, 222)
>>> len(s)
8
>>> s.get_top()
(10, 222)
>>> s
StackStyleSimpleIntMapping(([(1, 5), (6, 7), (7, 9), (10, 11)], [111, 111, 222, 222]))
>>> s.pop()
(10, 222)
>>> len(s)
7
>>> s
StackStyleSimpleIntMapping(([(1, 5), (6, 7), (7, 9)], [111, 111, 222]))

>>> s.get_top()
(8, 222)
>>> s.pop()
(8, 222)
>>> len(s)
6
>>> s
StackStyleSimpleIntMapping(([(1, 5), (6, 7), (7, 8)], [111, 111, 222]))

>>> s.get_top()
(7, 222)
>>> s.pop()
(7, 222)
>>> len(s)
5

>>> s.get_top()
(6, 111)
>>> s.pop()
(6, 111)
>>> len(s)
4
>>> s
StackStyleSimpleIntMapping(([(1, 5)], [111]))

>>> s.get_top()
(4, 111)
>>> s.pop()
(4, 111)
>>> len(s)
3

>>> s.get_top()
(3, 111)
>>> s.pop()
(3, 111)
>>> len(s)
2

>>> s.get_top()
(2, 111)
>>> s.pop()
(2, 111)
>>> len(s)
1

>>> s.get_top()
(1, 111)
>>> s.pop()
(1, 111)
>>> len(s)
0
>>> s
StackStyleSimpleIntMapping(([], []))

>>> s.get_top()
Traceback (most recent call last):
    ...
KeyError: 'get_top from an empty mapping'

>>> s.pop()
Traceback (most recent call last):
    ...
KeyError: 'pop from an empty mapping'


>>> StackStyleSimpleIntMapping.from_clone_of_rngs_with_default([(1,2),(2,3),(4,5)], 111)
StackStyleSimpleIntMapping(([(1, 3), (4, 5)], [111, 111]))

]]
[[
StackStyleSimpleIntMapping
>>> s = StackStyleSimpleIntMapping()
>>> s
StackStyleSimpleIntMapping(([], []))
>>> len(s)
0


StackStyleSimpleIntMapping
    push_rng_value_pairs
    push_rng_value
    __delitem__
    __getitem__
    getitem4int
    iter_intersect_range_ex

>>> s[0]
Traceback (most recent call last):
    ...
KeyError: 0
>>> s.getitem4int(0)
Traceback (most recent call last):
    ...
KeyError: 0
>>> del s[0]
Traceback (most recent call last):
    ...
KeyError: '__delitem__ from an empty mapping'

>>> s.push_rng_value((1,5), 111)
>>> s.get_top()
(4, 111)
>>> s.push_rng_value_pairs([((6,7),111), ((7,9),222), ((10,11),222)])
>>> len(s)
8
>>> s.get_top()
(10, 222)
>>> s
StackStyleSimpleIntMapping(([(1, 5), (6, 7), (7, 9), (10, 11)], [111, 111, 222, 222]))

>>> del s[11]
Traceback (most recent call last):
    ...
KeyError: 'stack_styple-int-mapping: __delitem__(i) but i == 11 != 10 == top_key'
>>> del s[9]
Traceback (most recent call last):
    ...
KeyError: 'stack_styple-int-mapping: __delitem__(i) but i == 9 != 10 == top_key'
>>> del s[8]
Traceback (most recent call last):
    ...
KeyError: 'stack_styple-int-mapping: __delitem__(i) but i == 8 != 10 == top_key'

>>> s[10]
222
>>> s.getitem4int(10)
222
>>> s
StackStyleSimpleIntMapping(([(1, 5), (6, 7), (7, 9), (10, 11)], [111, 111, 222, 222]))
>>> del s[10]
>>> len(s)
7
>>> s
StackStyleSimpleIntMapping(([(1, 5), (6, 7), (7, 9)], [111, 111, 222]))
>>> s[10]
Traceback (most recent call last):
    ...
KeyError: 10
>>> s.getitem4int(10)
Traceback (most recent call last):
    ...
KeyError: 10


>>> s.push_rng_value((13, 15), 333)
>>> s
StackStyleSimpleIntMapping(([(1, 5), (6, 7), (7, 9), (13, 15)], [111, 111, 222, 333]))

>>> [*s.iter_intersect_range_ex__with_value((-1,0))]
[]
>>> [*s.iter_intersect_range_ex__with_value((0,1))]
[]
>>> [*s.iter_intersect_range_ex__with_value((5,6))]
[]
>>> [*s.iter_intersect_range_ex__with_value((10,11))]
[]
>>> [*s.iter_intersect_range_ex__with_value((15,16))]
[]


>>> [*s.iter_intersect_range_ex__with_value((0,1))]
[]
>>> [*s.iter_intersect_range_ex__with_value((0,3))]
[(0, (1, 3), 111)]
>>> [*s.iter_intersect_range_ex__with_value((0,5))]
[(0, (1, 5), 111)]
>>> [*s.iter_intersect_range_ex__with_value((0,6))]
[(0, (1, 5), 111)]

>>> [*s.iter_intersect_range_ex__with_value((0,7))]
[(0, (1, 5), 111), (1, (6, 7), 111)]
>>> [*s.iter_intersect_range_ex__with_value((0,8))]
[(0, (1, 5), 111), (1, (6, 7), 111), (2, (7, 8), 222)]
>>> [*s.iter_intersect_range_ex__with_value((0,9))]
[(0, (1, 5), 111), (1, (6, 7), 111), (2, (7, 9), 222)]
>>> [*s.iter_intersect_range_ex__with_value((0,10))]
[(0, (1, 5), 111), (1, (6, 7), 111), (2, (7, 9), 222)]
>>> [*s.iter_intersect_range_ex__with_value((0,13))]
[(0, (1, 5), 111), (1, (6, 7), 111), (2, (7, 9), 222)]
>>> [*s.iter_intersect_range_ex__with_value((0,14))]
[(0, (1, 5), 111), (1, (6, 7), 111), (2, (7, 9), 222), (3, (13, 14), 333)]
>>> [*s.iter_intersect_range_ex__with_value((0,15))]
[(0, (1, 5), 111), (1, (6, 7), 111), (2, (7, 9), 222), (3, (13, 15), 333)]
>>> [*s.iter_intersect_range_ex__with_value((0,16))]
[(0, (1, 5), 111), (1, (6, 7), 111), (2, (7, 9), 222), (3, (13, 15), 333)]


>>> [*s.iter_intersect_range_ex__with_value((2,3))]
[(0, (2, 3), 111)]
>>> [*s.iter_intersect_range_ex__with_value((2,5))]
[(0, (2, 5), 111)]
>>> [*s.iter_intersect_range_ex__with_value((2,6))]
[(0, (2, 5), 111)]

>>> [*s.iter_intersect_range_ex__with_value((2,7))]
[(0, (2, 5), 111), (1, (6, 7), 111)]
>>> [*s.iter_intersect_range_ex__with_value((2,8))]
[(0, (2, 5), 111), (1, (6, 7), 111), (2, (7, 8), 222)]
>>> [*s.iter_intersect_range_ex__with_value((2,9))]
[(0, (2, 5), 111), (1, (6, 7), 111), (2, (7, 9), 222)]
>>> [*s.iter_intersect_range_ex__with_value((2,10))]
[(0, (2, 5), 111), (1, (6, 7), 111), (2, (7, 9), 222)]
>>> [*s.iter_intersect_range_ex__with_value((2,13))]
[(0, (2, 5), 111), (1, (6, 7), 111), (2, (7, 9), 222)]
>>> [*s.iter_intersect_range_ex__with_value((2,14))]
[(0, (2, 5), 111), (1, (6, 7), 111), (2, (7, 9), 222), (3, (13, 14), 333)]
>>> [*s.iter_intersect_range_ex__with_value((2,15))]
[(0, (2, 5), 111), (1, (6, 7), 111), (2, (7, 9), 222), (3, (13, 15), 333)]
>>> [*s.iter_intersect_range_ex__with_value((2,16))]
[(0, (2, 5), 111), (1, (6, 7), 111), (2, (7, 9), 222), (3, (13, 15), 333)]


>>> [*s.iter_intersect_range_ex__with_value((5,6))]
[]
>>> [*s.iter_intersect_range_ex__with_value((5,7))]
[(1, (6, 7), 111)]
>>> [*s.iter_intersect_range_ex__with_value((5,8))]
[(1, (6, 7), 111), (2, (7, 8), 222)]
>>> [*s.iter_intersect_range_ex__with_value((5,9))]
[(1, (6, 7), 111), (2, (7, 9), 222)]
>>> [*s.iter_intersect_range_ex__with_value((5,10))]
[(1, (6, 7), 111), (2, (7, 9), 222)]
>>> [*s.iter_intersect_range_ex__with_value((5,13))]
[(1, (6, 7), 111), (2, (7, 9), 222)]
>>> [*s.iter_intersect_range_ex__with_value((5,14))]
[(1, (6, 7), 111), (2, (7, 9), 222), (3, (13, 14), 333)]
>>> [*s.iter_intersect_range_ex__with_value((5,15))]
[(1, (6, 7), 111), (2, (7, 9), 222), (3, (13, 15), 333)]
>>> [*s.iter_intersect_range_ex__with_value((5,16))]
[(1, (6, 7), 111), (2, (7, 9), 222), (3, (13, 15), 333)]




__iter__
__reversed__
iter_keys_
iter_rngs_
>>> [*iter(s)]
[1, 2, 3, 4, 6, 7, 8, 13, 14]
>>> [*reversed(s)]
[14, 13, 8, 7, 6, 4, 3, 2, 1]
>>> [*s.iter_keys_(reverse=False)]
[1, 2, 3, 4, 6, 7, 8, 13, 14]
>>> [*s.iter_keys_(reverse=True)]
[14, 13, 8, 7, 6, 4, 3, 2, 1]
>>> [*s.iter_rngs_(reverse=False)]
[(1, 5), (6, 7), (7, 9), (13, 15)]
>>> [*s.iter_rngs_(reverse=True)]
[(13, 15), (7, 9), (6, 7), (1, 5)]


    iter_values__per_rng_
    iter_rng_value_pairs_
    items
    reversed_items
    iter_items_
>>> [*s.iter_values__per_rng_(reverse=False)]
[111, 111, 222, 333]
>>> [*s.iter_values__per_rng_(reverse=True)]
[333, 222, 111, 111]
>>> [*s.iter_rng_value_pairs_(reverse=False)]
[((1, 5), 111), ((6, 7), 111), ((7, 9), 222), ((13, 15), 333)]
>>> [*s.iter_rng_value_pairs_(reverse=True)]
[((13, 15), 333), ((7, 9), 222), ((6, 7), 111), ((1, 5), 111)]
>>> [*s.iter_items_(reverse=False)]
[(1, 111), (2, 111), (3, 111), (4, 111), (6, 111), (7, 222), (8, 222), (13, 333), (14, 333)]
>>> [*s.iter_items_(reverse=True)]
[(14, 333), (13, 333), (8, 222), (7, 222), (6, 111), (4, 111), (3, 111), (2, 111), (1, 111)]
>>> [*s.items()]
[(1, 111), (2, 111), (3, 111), (4, 111), (6, 111), (7, 222), (8, 222), (13, 333), (14, 333)]
>>> [*s.reversed_items()]
[(14, 333), (13, 333), (8, 222), (7, 222), (6, 111), (4, 111), (3, 111), (2, 111), (1, 111)]



maybe_range_contained
maybe_range_contained_ex
__contains__
contains_range
contains_all
>>> s.maybe_range_contained(0)
>>> s.maybe_range_contained(5)
>>> s.maybe_range_contained(9)
>>> s.maybe_range_contained(10)
>>> s.maybe_range_contained(15)

>>> s.maybe_range_contained(1)
(1, 5)
>>> s.maybe_range_contained(2)
(1, 5)
>>> s.maybe_range_contained(4)
(1, 5)
>>> s.maybe_range_contained(6)
(6, 7)
>>> s.maybe_range_contained(7)
(7, 9)
>>> s.maybe_range_contained(8)
(7, 9)
>>> s.maybe_range_contained(13)
(13, 15)
>>> s.maybe_range_contained(14)
(13, 15)


>>> s.maybe_range_contained_ex(0)
(None, -1)
>>> s.maybe_range_contained_ex(5)
(None, 0)
>>> s.maybe_range_contained_ex(9)
(None, 2)
>>> s.maybe_range_contained_ex(10)
(None, 2)
>>> s.maybe_range_contained_ex(15)
(None, 3)
>>> s.maybe_range_contained_ex(16)
(None, 3)

>>> s.maybe_range_contained_ex(1)
((1, 5), 0)
>>> s.maybe_range_contained_ex(2)
((1, 5), 0)
>>> s.maybe_range_contained_ex(4)
((1, 5), 0)
>>> s.maybe_range_contained_ex(6)
((6, 7), 1)
>>> s.maybe_range_contained_ex(7)
((7, 9), 2)
>>> s.maybe_range_contained_ex(8)
((7, 9), 2)
>>> s.maybe_range_contained_ex(13)
((13, 15), 3)
>>> s.maybe_range_contained_ex(14)
((13, 15), 3)


>>> 0 in s
False
>>> 5 in s
False
>>> 9 in s
False
>>> 10 in s
False
>>> 15 in s
False

>>> 1 in s
True
>>> 2 in s
True
>>> 4 in s
True
>>> 6 in s
True
>>> 7 in s
True
>>> 8 in s
True
>>> 13 in s
True
>>> 14 in s
True


>>> (0, 4) in s
False
>>> (1, 4) in s
True
>>> (1, 5) in s
True
>>> (2, 5) in s
True
>>> (2, 6) in s
False
>>> (2, 7) in s
False


>>> s.contains_range((2,5))
True
>>> s.contains_range((2,7))
False
>>> s.contains_range((5,7))
False

>>> s.contains_all([])
True
>>> s.contains_all([(2,3), 1])
True
>>> s.contains_all([(2,3), 1, (5,7)])
False

]]

]]
[[
@20220503:++new class TouchRangeBasedIntMapping/IRangeBasedIntMapping

>>> StackStyleSimpleIntMapping().to_TouchRangeBasedIntMapping()
TouchRangeBasedIntMapping(((), ()))

]]
[[
@20220503:++ranges2hex_repr_pair_list,ranges5hex_repr_pair_list

    iter_rngs2iter_hexXhexszpair_list
    iter_rngs5iter_hexXhexszpair_list
    ranges2hexXhexszpair_list
    ranges5hexXhexszpair_list

    ranges2len_rng2hexbegins
    ranges5len_rng2hexbegins
    ranges2len_rng2hexbegins_str
    ranges5len_rng2hexbegins_str
    ranges2len_rng2begin_chars
    ranges5len_rng2begin_chars

>>> ranges = make_Ranges([(0,1),(1,32)])
>>> hex_repr_pair_list = ranges2hex_repr_pair_list(ranges)
>>> hex_repr_pair_list
[(0x0, 0x1), (0x1, 0x20)]
>>> ranges5hex_repr_pair_list(ranges2hex_repr_pair_list(ranges))
TouchRanges(((0, 1), (1, 32)))
>>> ranges5hex_repr_pair_list(ranges2hex_repr_pair_list(ranges)) == ranges
True

>>> IRanges.from_hex_repr_pair_list(hex_repr_pair_list)
TouchRanges(((0, 1), (1, 32)))
>>> ranges.to_hex_repr_pair_list()
[(0x0, 0x1), (0x1, 0x20)]




>>> xs = ranges2hexXhexszpair_list(ranges)
>>> xs
[0x0, (0x1, 31)]
>>> ranges5hexXhexszpair_list(xs)
TouchRanges(((0, 1), (1, 32)))

>>> IRanges.from_hexXhexszpair_list(xs)
TouchRanges(((0, 1), (1, 32)))
>>> ranges.to_hexXhexszpair_list()
[0x0, (0x1, 31)]




    ranges2len_rng2hexbegins
    ranges5len_rng2hexbegins
>>> ranges = make_Ranges([(0,1),(1,2),(3,32),(44,45)])
>>> d = ranges2len_rng2hexbegins(ranges)
>>> d
{1: [0x0, 0x1, 0x2c], 29: [0x3]}
>>> ranges5len_rng2hexbegins(d)
TouchRanges(((0, 1), (1, 2), (3, 32), (44, 45)))

>>> IRanges.from_len_rng2hexbegins(d)
TouchRanges(((0, 1), (1, 2), (3, 32), (44, 45)))
>>> ranges.to_len_rng2hexbegins()
{1: [0x0, 0x1, 0x2c], 29: [0x3]}

    ranges2len_rng2hexbegins_str
    ranges5len_rng2hexbegins_str
>>> d = ranges2len_rng2hexbegins_str(ranges)
>>> d
{1: '0,1,2C', 29: '3'}
>>> ranges5len_rng2hexbegins_str(d)
TouchRanges(((0, 1), (1, 2), (3, 32), (44, 45)))

>>> IRanges.from_len_rng2hexbegins_str(d)
TouchRanges(((0, 1), (1, 2), (3, 32), (44, 45)))
>>> ranges.to_len_rng2hexbegins_str()
{1: '0,1,2C', 29: '3'}

    ranges2len_rng2begin_chars
    ranges5len_rng2begin_chars
>>> d = ranges2len_rng2begin_chars(ranges)
>>> d
{1: '\x00\x01,', 29: '\x03'}
>>> ranges5len_rng2begin_chars(d)
TouchRanges(((0, 1), (1, 2), (3, 32), (44, 45)))

>>> IRanges.from_len_rng2begin_chars(d)
TouchRanges(((0, 1), (1, 2), (3, 32), (44, 45)))
>>> ranges.to_len_rng2begin_chars()
{1: '\x00\x01,', 29: '\x03'}


]]


]]]

#]]]]]'''


__all__ = """
    iter_nontouch_rangess_between
    ints_to_iter_local_unique_ints
    sorted_unique_ints_to_iter_nontouch_ranges
        sorted_ints_to_iter_nontouch_ranges
    sorted_rngs_to_iter_nontouch_ranges
    rngs_to_iter_ints_
        rngs_to_iter_ints
        rng_value_pairs_to_iter_int_value_pairs_
    len_ints_of_nonoverlap_rngs


    symmetric_difference_ex__xtouch_ranges
    union_ex__xtouch_ranges
    intersection__xtouch_ranges
        are_disjoint_two_touch_ranges
    difference__xtouch_ranges

    PartialOrderingCompareResult
    iter_with_middle_state_of_subset_relation_ex__xtouch_ranges
        subset_relation_ex__xtouch_ranges
            is_equal_set_ex_of__xtouch_ranges
            subset_cmp_ex__xtouch_ranges
                is_subset_ex_of__xtouch_ranges
                is_proper_subset_ex_of__xtouch_ranges

    detect_ranges
    detect_iter_ranges
    valid_nontouch_ranges
    valid_touch_ranges
    is_subrange_of
    make_NonTouchRanges
    make_TouchRanges
    make_Ranges
    TouchRanges
    NonTouchRanges

    rngs_op__get_maybe_range_contained_ex
        rngs_op__get_maybe_range_contained
        rngs_op__iter_intersect_range_ex
            rngs_op__contains_range
                rngs_op__contains_range_or_int
                    rngs_op__contains_all

    StackStyleSimpleIntSet
    StackStyleSimpleIntMapping
    TouchRangeBasedIntMapping

    ranges2hex_repr_pair_list
    ranges5hex_repr_pair_list

    iter_rngs2iter_hexXhexszpair_list
    iter_rngs5iter_hexXhexszpair_list
    ranges2hexXhexszpair_list
    ranges5hexXhexszpair_list

    ranges2len_rng2hexbegins
    ranges5len_rng2hexbegins
    ranges2len_rng2hexbegins_str
    ranges5len_rng2hexbegins_str
    ranges2len_rng2begin_chars
    ranges5len_rng2begin_chars
    """.split()

import bisect
from itertools import chain
from operator import lt, le
from seed.iters.PeekableIterator import PeekableIterator
from seed.iters.iter_subsets_of import iter_subsets_of__dictionary_order as iter_subsets_of
from seed.tiny import print_err
from seed.func_tools.fmapT.fmapT__tiny import fmap_rngs2hex_repr, fmapT__pairs, dot
#from seed.func_tools.dot2 import dot
from seed.tiny_.HexReprInt import HexReprInt
from seed.tiny import fmap4dict_value

def all_map(pred, iterable, /):
    return all(map(pred, iterable))
def ints_to_iter_local_unique_ints(ints, /):
    it = iter(ints)
    for pre in it:
        yield pre
        break
    for curr in it:
        if curr != pre:
            yield curr
            pre = curr
def sorted_ints_to_iter_nontouch_ranges(sorted_ints, /):
    sorted_unique_ints = ints_to_iter_local_unique_ints(sorted_ints)
    return sorted_unique_ints_to_iter_nontouch_ranges(sorted_unique_ints)
def sorted_unique_ints_to_iter_nontouch_ranges(sorted_unique_ints, /):
    it = iter(sorted_unique_ints)
    for begin in it:
        break
    else:
        return
    end = begin + 1

    for last in it:
        if last == end:
            end += 1
        elif last > end:
            yield begin, end
            begin = last
            end = begin + 1
        else:
            raise TypeError('not sorted_unique_ints: {} {}'.format(end-1, last))
    yield begin, end
    pass

r"""
def sorted_unique_ints_to_nontouch_ranges(ints, /):
    return tuple(sorted_unique_ints_to_iter_nontouch_ranges(ints))
assert sorted_unique_ints_to_nontouch_ranges([0,1,3]) == ((0,2), (3,4))
assert sorted_unique_ints_to_nontouch_ranges([0]) == ((0,1),)
assert sorted_unique_ints_to_nontouch_ranges([]) == ()
#"""














#def rngs_to_reversed_ints(reversable_rngs, /):
#    return rngs_to_iter_ints_(reversable_rngs, reverse=True)
def rng_value_pairs_to_iter_int_value_pairs_(rng_value_pairs, /, *, reverse):
    f = (reverse if callable(reverse) else reversed) if reverse else iter
    g = reversed if reverse else iter
    for (begin, end), v in f(rng_value_pairs):
        for i in g(range(begin, end)):
            yield i, v

def rngs_to_iter_ints(rngs, /):
    return rngs_to_iter_ints_(rngs, reverse=False)
def rngs_to_iter_ints_(rngs, /, *, reverse):
    f = (reverse if callable(reverse) else reversed) if reverse else iter
    g = reversed if reverse else iter
    for begin, end in f(rngs):
        yield from g(range(begin, end))
def len_ints_of_nonoverlap_rngs(nonoverlap_rngs, /):
    return sum(end - begin for begin, end in nonoverlap_rngs)






def sorted_rngs_to_iter_nontouch_ranges(sorted_rngs, /):
    it = PeekableIterator(sorted_rngs)
    while not it.is_empty():
        (begin, end_) = it.read1() # raise StopIteration

        while not it.is_empty():
            head = it.head
            assert (begin, end_) <= head
            (_begin, _end) = head
            if _begin <= end_:
                #bug: end_ = _end # merge
                end_ = max(end_, _end) # merge
                it.read1()
                continue
            break
        yield (begin, end_) # instead of rng
    return


##################################
##################################
##################################
##################################
##################################
##################################


def are_disjoint_two_touch_ranges(lhs_touch_ranges, rhs_touch_ranges, /):
    it = intersection__xtouch_ranges(lhs_touch_ranges, rhs_touch_ranges)
    for _ in it:
        return False
    else:
        return True
#
def symmetric_difference_ex__xtouch_ranges(lhs_xtouch_ranges, rhs_xtouch_ranges, /,*, faster_output_iter_touch_ranges:bool):
    r"""
    if faster_output_iter_touch_ranges:
        output touch_ranges instead of xtouch_ranges
        this touch_ranges is more fragmentary than "not faster_output_iter_touch_ranges" case
    else:
        nontouch_ranges -> nontouch_ranges -> nontouch_ranges

        touch_ranges -> xtouch_ranges -> touch_ranges
        xtouch_ranges -> touch_ranges -> touch_ranges

    #"""
    lhs = PeekableIterator(lhs_xtouch_ranges)
    rhs = PeekableIterator(rhs_xtouch_ranges)
    faster_output_iter_touch_ranges = bool(faster_output_iter_touch_ranges)
    while 1:
        if lhs.is_empty():
            yield from rhs
            return

        if rhs.is_empty():
            yield from lhs
            return

        (begin_, end_) = lhs.head
        (_begin, _end) = rhs.head
        if _end <= begin_:
            rhs.read1()
            if _end == begin_ and not faster_output_iter_touch_ranges:
                begin_ = _begin # merge
                lhs.read1()
                lhs.append_left((begin_, end_))
            else:
                yield (_begin, _end)
        elif end_ <= _begin:
            lhs.read1()
            if end_ == _begin and not faster_output_iter_touch_ranges:
                _begin = begin_ # merge
                rhs.read1()
                rhs.append_left((_begin, _end))
            else:
                yield (begin_, end_)
        else:
            assert _begin < _end
            assert begin_ < end_
            lhs.read1()
            rhs.read1()

            assert _begin < end_
            assert begin_ < _end
            if begin_ < _begin:
                yield begin_, _begin
            elif begin_ > _begin:
                yield _begin, begin_

            ####
            if end_ < _end:
                _begin = end_
                rhs.append_left((_begin, _end))
            elif end_ > _end:
                begin_ = _end
                lhs.append_left((begin_, end_))

    return

def _skip_util(it, _begin_, /):
    while not it.is_empty():
        (begin, end) = it.head
        if end > _begin_:
            if begin < _begin_:
                it.read1()
                it.append_left((_begin_, end))
            break
        else:
            it.read1()
            if end == _begin_:
                break
    if __debug__:
        if it.len_relax():
            [(x,y)] = it.peek_relax_le(1)
            assert _begin_ <= x


def union_ex__xtouch_ranges(lhs_xtouch_ranges, rhs_xtouch_ranges, /,*, faster_output_iter_touch_ranges:bool):
    r"""
    if faster_output_iter_touch_ranges:
        output touch_ranges instead of xtouch_ranges
        this touch_ranges is more fragmentary than "not faster_output_iter_touch_ranges" case
    else:
        nontouch_ranges -> nontouch_ranges -> nontouch_ranges

        touch_ranges -> xtouch_ranges -> touch_ranges
        xtouch_ranges -> touch_ranges -> touch_ranges

    #"""
    lhs = PeekableIterator(lhs_xtouch_ranges)
    rhs = PeekableIterator(rhs_xtouch_ranges)
    faster_output_iter_touch_ranges = bool(faster_output_iter_touch_ranges)
    while 1:
        if lhs.is_empty():
            yield from rhs
            return

        if rhs.is_empty():
            yield from lhs
            return

        (begin_, end_) = lhs.head
        (_begin, _end) = rhs.head
        if _end < begin_:
            rhs.read1()
            yield (_begin, _end)
        elif end_ < _begin:
            lhs.read1()
            yield (begin_, end_)
        else:
            assert _begin < _end
            assert begin_ < end_
            lhs.read1()
            rhs.read1()

            assert _begin <= end_
            assert begin_ <= _end
            begin = min(begin_, _begin)
            end = max(end_, _end)
            assert begin < end

            ####
            rng = (begin, end)
            if faster_output_iter_touch_ranges:
                #bug: yield rng; continue
                #fixed: skip-until-end

                yield rng
                #skip-until-end
                if end_ < _end:
                    _skip_util(lhs, end)
                elif end_ > _end:
                    _skip_util(rhs, end)
            else:
                if end_ < _end:
                    rhs.append_left(rng)
                elif end_ > _end:
                    lhs.append_left(rng)
                else:
                    yield rng

    return




def intersection__xtouch_ranges(lhs_xtouch_ranges, rhs_xtouch_ranges, /):
    r"""
    nontouch_ranges -> xtouch_ranges -> nontouch_ranges
    xtouch_ranges -> nontouch_ranges -> nontouch_ranges

    touch_ranges -> touch_ranges -> touch_ranges
    #"""
    lhs = PeekableIterator(lhs_xtouch_ranges)
    rhs = PeekableIterator(rhs_xtouch_ranges)
    while not (lhs.is_empty() or rhs.is_empty()):
        (begin_, end_) = lhs.head # raise StopIteration
        (_begin, _end) = rhs.head # raise StopIteration
        if _end <= begin_:
            rhs.read1()
        elif end_ <= _begin:
            lhs.read1()
        else:
            assert _begin < _end
            assert begin_ < end_
            lhs.read1()
            rhs.read1()

            assert _begin < end_
            assert begin_ < _end
            begin = max(begin_, _begin)
            end = min(end_, _end)
            assert begin < end
            yield begin, end # intersection

            ####
            if end_ < _end:
                _begin = end_
                rhs.append_left((_begin, _end))
            elif end_ > _end:
                begin_ = _end
                lhs.append_left((begin_, end_))

    return



def difference__xtouch_ranges(lhs_xtouch_ranges, rhs_xtouch_ranges, /):
    r"""
    nontouch_ranges -> xtouch_ranges -> nontouch_ranges

    touch_ranges -> xtouch_ranges -> touch_ranges
    #"""
    lhs = PeekableIterator(lhs_xtouch_ranges)
    rhs = PeekableIterator(rhs_xtouch_ranges)
    while not lhs.is_empty():
        (begin_, end_) = lhs.head # raise StopIteration
        if rhs.is_empty():
            yield from lhs
            return
        (_begin, _end) = rhs.head

        if _end <= begin_:
            rhs.read1()
        elif end_ <= _begin:
            yield lhs.read1()
        else:
            assert _begin < _end
            assert begin_ < end_
            lhs.read1()
            rhs.read1()

            assert _begin < end_
            assert begin_ < _end
            if begin_ < _begin:
                yield begin_, _begin

            ####
            if end_ < _end:
                _begin = end_
                rhs.append_left((_begin, _end))
            elif end_ > _end:
                begin_ = _end
                lhs.append_left((begin_, end_))

    return

def is_equal_set_ex_of__xtouch_ranges(lhs_xtouch_ranges, rhs_xtouch_ranges, /,*, lhs_maynot_be_nontouch_ranges:bool, rhs_maynot_be_nontouch_ranges:bool):
    R = PartialOrderingCompareResult
    st_or_r = subset_relation_ex__xtouch_ranges(lhs_xtouch_ranges, rhs_xtouch_ranges
            #####
            , rhs_maynot_be_nontouch_ranges=rhs_maynot_be_nontouch_ranges
            , faster_return_not_le=True
            #####
            , lhs_maynot_be_nontouch_ranges=lhs_maynot_be_nontouch_ranges
            , faster_return_not_ge=True
            )
    return st_or_r == R.EQ
    ############# old impl ##########
#def is_equal_set_ex_of__xtouch_ranges(lhs_xtouch_ranges, rhs_xtouch_ranges, /,*, rhs_maynot_be_nontouch_ranges:bool):
    return 0 == subset_cmp_ex__xtouch_ranges(lhs_xtouch_ranges, rhs_xtouch_ranges, rhs_maynot_be_nontouch_ranges=rhs_maynot_be_nontouch_ranges)
def is_subset_ex_of__xtouch_ranges(lhs_xtouch_ranges, rhs_xtouch_ranges, /,*, rhs_maynot_be_nontouch_ranges:bool):
    return 0 >= subset_cmp_ex__xtouch_ranges(lhs_xtouch_ranges, rhs_xtouch_ranges, rhs_maynot_be_nontouch_ranges=rhs_maynot_be_nontouch_ranges)
def is_proper_subset_ex_of__xtouch_ranges(lhs_xtouch_ranges, rhs_xtouch_ranges, /,*, rhs_maynot_be_nontouch_ranges:bool):
    return 0 > subset_cmp_ex__xtouch_ranges(lhs_xtouch_ranges, rhs_xtouch_ranges, rhs_maynot_be_nontouch_ranges=rhs_maynot_be_nontouch_ranges)

class PartialOrderingCompareResult:
    NA = 0
    LT = 1
    GT = 2
    EQ = 3
    @classmethod
    def get_mirror_class(cls, /):
        return LeftRightHandSideFlip
    @classmethod
    def get_FASTER_NOT_LE(cls, /):
        return (7 ^ cls.LT) # == (4 | cls.GT) == (7 & ~cls.LT)
    @classmethod
    def get_FASTER_NOT_GE(cls, /):
        return (7 ^ cls.GT) # == (4 | cls.LT) == (7 & ~cls.GT)
    @classmethod
    def le(cls, r, /):
        return bool(r & cls.LT)
    @classmethod
    def ge(cls, r, /):
        return bool(r & cls.GT)
    @classmethod
    def na(cls, r, /):
        return (r==cls.NA)
    @classmethod
    def lt(cls, r, /):
        return (r==cls.LT)
    @classmethod
    def gt(cls, r, /):
        return (r==cls.GT)
    @classmethod
    def eq(cls, r, /):
        return (r==cls.EQ)
class LeftRightHandSideFlip(PartialOrderingCompareResult):
    LT = PartialOrderingCompareResult.GT
    GT = PartialOrderingCompareResult.LT
    @classmethod
    def get_mirror_class(cls, /):
        return PartialOrderingCompareResult
def _():
    R = PartialOrderingCompareResult
    assert R.get_FASTER_NOT_GE() == 5
    assert R.get_FASTER_NOT_LE() == 6
    for R in [R, R.get_mirror_class()]:
        assert R.get_FASTER_NOT_GE() == (4 | R.LT) == (7 & ~R.GT) == (7 ^ R.GT)
        assert R.get_FASTER_NOT_LE() == (4 | R.GT) == (7 & ~R.LT) == (7 ^ R.LT)

_(); del _

def subset_relation_ex__xtouch_ranges(lhs_xtouch_ranges, rhs_xtouch_ranges, /,*, lhs_maynot_be_nontouch_ranges:bool, rhs_maynot_be_nontouch_ranges:bool, faster_return_not_le:bool, faster_return_not_ge:bool):
    r"""
    -> (0 | 1 | 2 | 3 | 5 | 6)
    lhs < rhs => 1
    lhs > rhs => 2
    lhs == rhs => 3
    faster_return_not_le and not lhs <= rhs => 6
        #faster:rhs_maynot_be_nontouch_ranges==False
    faster_return_not_ge and not lhs >= rhs => 5
        #faster:lhs_maynot_be_nontouch_ranges=False
    otherwise => 0

    #"""
    R = PartialOrderingCompareResult
    faster_return_not_le = bool(faster_return_not_le)
    faster_return_not_ge = bool(faster_return_not_ge)
    it = iter_with_middle_state_of_subset_relation_ex__xtouch_ranges(lhs_xtouch_ranges, rhs_xtouch_ranges
            , lhs_maynot_be_nontouch_ranges=lhs_maynot_be_nontouch_ranges
            , rhs_maynot_be_nontouch_ranges=rhs_maynot_be_nontouch_ranges
            )
    for st_or_r in it:
        break
    else:
        raise logic-err
    if st_or_r < 4:
        r = st_or_r
    else:
        st = st_or_r
        if faster_return_not_le and st == R.get_FASTER_NOT_LE():
            return st
        if faster_return_not_ge and st == R.get_FASTER_NOT_GE():
            return st
        [r] = it
    return r


class _4_iter_mid_st:
    def on_lhs_is_empty(largs, r, /):
        #->return
        [R, F, lhs, rhs
        , lhs_maynot_be_nontouch_ranges
        , rhs_maynot_be_nontouch_ranges
        ] = largs

        assert lhs.is_empty()
        if R.lt(r):
            return r
        elif R.eq(r):
            return R.EQ if rhs.is_empty() else R.LT
        else:
            assert R.gt(r)
            return r if rhs.is_empty() else R.NA

    def on_rend_le_lbegin(largs, r, _end, begin_, /):
        #-> r # may be NA
        [R, F, lhs, rhs
        , lhs_maynot_be_nontouch_ranges
        , rhs_maynot_be_nontouch_ranges
        ] = largs

        assert _end <= begin_
        # ~R.GT
        if R.gt(r):
            return R.NA
        ####le
        if not rhs_maynot_be_nontouch_ranges:
            # rhs_is_nontouch_ranges
            if _end == begin_:
                # ~R.LT
                return R.NA
        rhs.read1()
        return R.LT


def iter_with_middle_state_of_subset_relation_ex__xtouch_ranges(lhs_xtouch_ranges, rhs_xtouch_ranges, /,*, lhs_maynot_be_nontouch_ranges:bool, rhs_maynot_be_nontouch_ranges:bool):
    r"""
    -> iter regex<int>"[56]?[0123]"
    maybe middle state (5 | 6):
        not lhs <= rhs => 6
            #faster:rhs_maynot_be_nontouch_ranges==False
        not lhs >= rhs => 5
            #faster:lhs_maynot_be_nontouch_ranges=False
    final value (0 | 1 | 2 | 3):
        lhs < rhs => 1
        lhs > rhs => 2
        lhs == rhs => 3
        otherwise => 0
        #lhs <= rhs => bool(result & 1)
        #lhs >= rhs => bool(result & 2)

    #"""
    R = PartialOrderingCompareResult
    F = R.get_mirror_class()
    lhs = PeekableIterator(lhs_xtouch_ranges)
    rhs = PeekableIterator(rhs_xtouch_ranges)
    lhs_maynot_be_nontouch_ranges = bool(lhs_maynot_be_nontouch_ranges)
    rhs_maynot_be_nontouch_ranges = bool(rhs_maynot_be_nontouch_ranges)

    largs = (R, F, lhs, rhs
            , lhs_maynot_be_nontouch_ranges
            , rhs_maynot_be_nontouch_ranges
            )
    rargs = (F, R, rhs, lhs
            , rhs_maynot_be_nontouch_ranges
            , lhs_maynot_be_nontouch_ranges
            )
    fs = _4_iter_mid_st

    r = R.EQ
    saved_r = r
    while 1:
        # r =[def]= prev util now, cmp result
        # r != R.NA
        assert not R.na(r)
        if saved_r != r:
            yield 4 | r
            saved_r = r
        if lhs.is_empty():
            yield fs.on_lhs_is_empty(largs, r)
            return
        if rhs.is_empty():
            yield fs.on_lhs_is_empty(rargs, r)
            return

        (begin_, end_) = lhs.head
        (_begin, _end) = rhs.head
        if _end <= begin_:
            r = fs.on_rend_le_lbegin(largs, r, _end, begin_)
            # r may be NA
        elif end_ <= _begin:
            r = fs.on_rend_le_lbegin(rargs, r, end_, _begin)
            # r may be NA
        else:
            assert _begin < _end
            assert begin_ < end_
            lhs.read1()
            rhs.read1()

            assert _begin < end_
            assert begin_ < _end
            if begin_ < _begin:
                #not le
                #bug: r ^= R.LT
                r &= ~R.LT
                # r may be NA
            elif begin_ > _begin:
                #not ge
                #bug: r ^= R.GT
                r &= ~R.GT
                # r may be NA
            # r may be NA

            ####
            if end_ < _end:
                _begin = end_
                rhs.append_left((_begin, _end))
                if not lhs_maynot_be_nontouch_ranges:
                    #lhs_is_nontouch_ranges
                    #not ge
                    #bug: r ^= R.GT
                    r &= ~R.GT
                    # r may be NA
            elif end_ > _end:
                begin_ = _end
                lhs.append_left((begin_, end_))
                if not rhs_maynot_be_nontouch_ranges:
                    # rhs_is_nontouch_ranges
                    #not le
                    #bug: r ^= R.LT
                    r &= ~R.LT
                    # r may be NA
            # r may be NA
        ######
        if R.na(r):
            yield r
            return

    return






def subset_cmp_ex__xtouch_ranges(lhs_xtouch_ranges, rhs_xtouch_ranges, /,*, rhs_maynot_be_nontouch_ranges:bool):
    r"""
    -> (-1 | 0 | +1)
    rel = is_proper_subset | is_eq_set | not_subset
    lhs `rel` rhs
    #"""
    R = PartialOrderingCompareResult
    st_or_r = subset_relation_ex__xtouch_ranges(lhs_xtouch_ranges, rhs_xtouch_ranges
            #####
            , rhs_maynot_be_nontouch_ranges=rhs_maynot_be_nontouch_ranges
            , faster_return_not_le=True
            #####
            , lhs_maynot_be_nontouch_ranges=True
            , faster_return_not_ge=False
            )
    if st_or_r == R.LT:
        return -1
    elif st_or_r == R.EQ:
        return 0
    elif st_or_r in [R.get_FASTER_NOT_LE(), R.NA, R.GT]:
        return +1
    else:
        raise logic-err
    ############# old impl ##########
    lhs = PeekableIterator(lhs_xtouch_ranges)
    rhs = PeekableIterator(rhs_xtouch_ranges)
    #lhs_maynot_be_nontouch_ranges = bool(lhs_maynot_be_nontouch_ranges)
    rhs_maynot_be_nontouch_ranges = bool(rhs_maynot_be_nontouch_ranges)

    is_eq = True
    while 1:
        if lhs.is_empty():
            return 0 if is_eq and rhs.is_empty() else -1
        if rhs.is_empty():
            return +1

        (begin_, end_) = lhs.head
        (_begin, _end) = rhs.head
        if _end <= begin_:
            if not rhs_maynot_be_nontouch_ranges:
                # rhs_is_nontouch_ranges
                if _end == begin_:
                    return +1
            rhs.read1()
            is_eq = False
        elif end_ <= _begin:
            return +1
            lhs.read1()
        else:
            assert _begin < _end
            assert begin_ < end_
            lhs.read1()
            rhs.read1()

            assert _begin < end_
            assert begin_ < _end
            if begin_ < _begin:
                return +1
            elif begin_ > _begin:
                is_eq = False

            ####
            if end_ < _end:
                _begin = end_
                rhs.append_left((_begin, _end))
            elif end_ > _end:
                if not rhs_maynot_be_nontouch_ranges:
                    # rhs_is_nontouch_ranges
                    return +1
                begin_ = _end
                lhs.append_left((begin_, end_))

    return






r"""
len(s)
x in s
x not in s
isdisjoint(other)
issubset(other)
set <= other
set < other
issuperset(other)
set >= other
set > other
union(*others)
set | other | ...
intersection(*others)
set & other & ...
difference(*others)
set - other - ...
symmetric_difference(other)
set ^ other
copy()
#"""




####################
def valid_range(range, /):
    if type(range) is not tuple:
        return False
    begin, end = range
    if not type(begin) is int is type(end):
        return False
    return begin < end
def check_range(rng, /):
    if not valid_range(rng):
        raise TypeError('not valid_range({})'.format(rng))

def detect_ranges(ranges, /):
    r"""
    0 | 1 | 3 | 7 | 15
    not tuple<rng> | is tuple<rng> | is sorted_rngs | is touch_ranges | is nontouch_ranges
    #"""
    if type(ranges) is not tuple:
        return 0
    return detect_iter_ranges(ranges)
def detect_iter_ranges(iterable, /):
    r"""
    0 | 1 | 3 | 7 | 15
    not iterable<rng> | is iterable<rng> | is sorted_rngs | is touch_ranges | is nontouch_ranges
    #"""
    it = iter(iterable)
    for pre in it:
        if not valid_range(pre):
            return 0
        break
    else:
        return 15

    def _15():
        return pre[-1] < curr[0]
    def _7():
        return pre[-1] <= curr[0]
    def _3():
        return pre <= curr
    def _1():
        return True
    fs = [_15, _7, _3, _1]
    rs = [15, 7, 3, 1]
    ps = zip(fs, rs)
    f,r = next(ps)

    for curr in it:
        if not valid_range(curr):
            return 0
        while not f():
            f,r = next(ps)
        pre = curr
    return r

def valid_nontouch_ranges(ranges, /):
    return _valid_ranges(ranges, lt)
def valid_touch_ranges(ranges, /):
    return _valid_ranges(ranges, le)
def _valid_ranges(ranges, lt, /):
    if type(ranges) is not tuple:
        return False
    if not all_map(valid_range, ranges):
        return False
    for i in range(len(ranges) - 1):
        a, b = ranges[i:i+2]
        if not lt(a[-1], b[0]):
            return False
    return True

def is_subrange_of(sub_rng, super_rng, /):
    check_range(sub_rng)
    check_range(super_rng)

    begin, end = sub_rng
    lower, upper = super_rng
    return lower <= begin and end <= upper
assert is_subrange_of((0,3), (0,3))
assert not is_subrange_of((0,3), (0,2))
assert not is_subrange_of((0,3), (1,3))
assert is_subrange_of((0,2), (0,3))

def to_tuple(iterable, /):
    if type(iterable) is tuple:
        return iterable
    return tuple(iterable)
def make_NonTouchRanges(iterable_nontouch_ranges, /):
    return NonTouchRanges(to_tuple(iterable_nontouch_ranges))
def make_TouchRanges(iterable_touch_ranges, /):
    return TouchRanges(to_tuple(iterable_touch_ranges))
def make_Ranges(iterable_touch_ranges, /):
    ranges = to_tuple(iterable_touch_ranges)
    case = detect_ranges(ranges)
    if case == 15:
        cls = NonTouchRanges
    elif case == 7:
        cls = TouchRanges
    else:
        raise TypeError('not valid_touch_ranges({})'.format(ranges))
    return cls(ranges)




#[[[move out from class IRanges
def rngs_op__get_maybe_range_contained(rngs, i, /):
    'rngs -> i -> may rng'
    return rngs_op__get_maybe_range_contained_ex(rngs, i)[0]
def rngs_op__get_maybe_range_contained_ex(rngs, i, /):
    'rngs -> i -> (may rng, imay idx) #[imay_idx >=0]==>>[[rngs[idx][0] <= i][[idx+1<len(rngs)]==>>[i < rngs[idx+1][0]]][[may_rng is None]<==>[rngs[idx][1] <= i]]]'
    L = len(rngs)

    j = i + 1
    idx = bisect.bisect_left(rngs, (j,j)) - 1
    if idx < 0:
        assert not L or rngs[0][0] > i
        return None, idx

    begin, end = rng = rngs[idx]
    assert begin <= i
    if not i < end:
        assert idx + 1 == L or rngs[idx+1][0] > i
        return None, idx
    return rng, idx

def rngs_op__contains_range_or_int(rngs, int_or_rng, /):
    'rngs -> (i|rng) -> bool'
    if isinstance(int_or_rng, int):
        begin = int_or_rng
        end = begin + 1
        sub_rng = begin, end
    else:
        sub_rng = int_or_rng
    return rngs_op__contains_range(rngs, sub_rng)

def rngs_op__contains_all(rngs, iterable, /):
    'rngs -> Iter<(i|rng)> -> bool'
    return all(rngs_op__contains_range_or_int(rngs, int_or_rng) for int_or_rng in iterable)

def rngs_op__contains_range(rngs, sub_rng, /):
    'rngs -> rng -> bool'
    ################################too slow:
    it = rngs_op__iter_intersect_range_ex(rngs, sub_rng)
    it = (common_rng for idx, common_rng in it)
    if 1:
        for common_rng in it:
            if common_rng == sub_rng:
                return True
            elif common_rng > sub_rng:
                #common_rng.begin > sub_rng.begin
                return False
            else:
                #common_rng.begin == sub_rng.begin
                #common_rng.end < sub_rng.end
                it = chain([common_rng], it)
                break
        else:
            return False
    else:
        #too slow if head common_rng > sub_rng
        pass

    if 1:
        #take care for rngs is touch_ranges
        it = sorted_rngs_to_iter_nontouch_ranges(it)
    else:
        #bug:maybe touch!
        pass
    for common_rng in it:
        return common_rng == sub_rng
    return False
    ######################old version
    check_range(sub_rng)
    begin, end = sub_rng
    may_rng, idx = rngs_op__get_maybe_range_contained_ex(rngs, begin)
    if may_rng is None:
        return False

    #take care for rngs is touch_ranges
    pre_end = may_rng[0]
    for idx in range(idx, len(rngs)):
        begin_, end_ = rngs[idx]
        if pre_end != begin_:
            return False
        pre_end = end_
        if end <= end_:
            return True
    assert end > rngs[-1][-1]
    return False
    #return is_subrange_of(sub_rng, may_rng)
    pass
def rngs_op__iter_intersect_range_ex(rngs, rng, /):
    'rngs -> rng -> Iter<(idx, common_rng)>'
    check_range(rng)
    begin, end = rng
    may_rng, imay_idx = rngs_op__get_maybe_range_contained_ex(rngs, begin)
    L = len(rngs)
    def may_intersect(_rng, begin, end, /):
        '-> may common_rng'
        _begin, _end = _rng
        if not begin <= _begin: raise logic-err
        curr_begin = max(begin, _begin)
        next_begin = min(_end, end)
        if not curr_begin < next_begin:
            return None
        common_rng = curr_begin, next_begin
        return common_rng

    if not may_rng is None:
        rng0 = may_rng
        idx = imay_idx
        assert rng0 is rngs[idx]

        begin0, end0 = rng0
        assert begin0 <= begin < end0
        begin1 = min(end0, end)
        assert begin < begin1
        common_rng0 = begin, begin1
        yield idx, common_rng0
        begin = begin1
    #take care for rngs is touch_ranges
    idx = imay_idx + 1
    for idx in range(idx, L):
        _rng = rngs[idx]
        m = may_intersect(_rng, begin, end)
        if m is None:break
        common_rng = m
        yield idx, common_rng
        _, begin = common_rng
    return

def rngs_op__iter_gaps(rngs, /):
    it = iter(rngs)
    for _, pre_end in it:
        break
    for begin, end in it:
        if begin != pre_end:
            yield pre_end, begin
        pre_end = end
def rngs_op__reversed_gaps(rngs, /):
    it = reversed(rngs)
    for next_begin, _ in it:
        break
    for begin, end in it:
        if end != next_begin:
            yield end, next_begin
        next_begin = begin
def rngs_op__iter_gaps_(rngs, /, *, reverse):
    f = rngs_op__reversed_gaps if reverse else rngs_op__iter_gaps
    return f(rngs)

class IMixin4_get_rngs_:
    def _get_rngs_(sf, /):
        raise NotImplementedError
    def _to_NonTouchRanges_(sf, /):
        raise NotImplementedError
    def _O_get_rngs_O_(sf, /):
        return sf._get_rngs_()
    def to_NonTouchRanges(sf, /):
        return sf._to_NonTouchRanges_()
    def to_Ranges(sf, /):
        '-> immutable IRanges#TouchRanges/NonTouchRanges'
        rngs = sf._get_rngs_()
        return make_Ranges(rngs)
    def iter_intersect_range_ex(sf, rng, /):
        '-> Iter<(idx, common_rng)>'
        rngs = sf._get_rngs_()
        return rngs_op__iter_intersect_range_ex(rngs, rng)
    def len_rngs(sf, /):
        rngs = sf._get_rngs_()
        return len(rngs)
    def __iter__(sf, /):
        return sf.iter_ints()
    def __reversed__(sf, /):
        return sf.reversed_ints()
    def iter_ints(sf, /):
        return sf.iter_keys_(reverse=False)
    def reversed_ints(sf, /):
        return sf.iter_keys_(reverse=True)
    def iter_keys_(sf, /, reverse):
        rngs = sf._get_rngs_()
        return rngs_to_iter_ints_(rngs, reverse=reverse)
    iter_ints_ = iter_keys_
    def iter_rngs_(sf, /, reverse):
        rngs = sf._get_rngs_()
        g = reversed if reverse else iter
        return g(rngs)
    def iter_rngs(sf, /):
        return sf.iter_rngs_(reverse=False)
    def reversed_rngs(sf, /):
        return sf.iter_rngs_(reverse=True)

    def __bool__(sf, /):
        return bool(sf.len_rngs())
    def gaps(sf, /):
        return tuple(sf.iter_gaps())
    def iter_gaps(sf, /):
        return sf.iter_gaps_(reverse=False)
    def reversed_gaps(sf, /):
        return sf.iter_gaps_(reverse=True)
    def iter_gaps_(sf, /, *, reverse):
        rngs = sf._get_rngs_()
        return rngs_op__iter_gaps_(rngs, reverse=reverse)
    ###news:
    def maybe_range_contained(sf, i, /):
        return rngs_op__get_maybe_range_contained(sf._get_rngs_(), i)
    def maybe_range_contained_ex(sf, i, /):
        return rngs_op__get_maybe_range_contained_ex(sf._get_rngs_(), i)
    def __contains__(sf, int_or_rng, /):
        return rngs_op__contains_range_or_int(sf._get_rngs_(), int_or_rng)
    def contains_range(sf, sub_rng, /):
        return rngs_op__contains_range(sf._get_rngs_(), sub_rng)
    def contains_all(sf, iterable, /):
        return rngs_op__contains_all(sf._get_rngs_(), iterable)
#]]]


class IRanges(IMixin4_get_rngs_):
    r'''
ABC IRanges:
    * immutable TouchRanges
    * immutable NonTouchRanges
    * (almost subclass)mutable StackStyleSimpleIntSet

see also:
    ABC IRangeBasedIntMapping

used:
    to repr partial parse result of unicode::Unihan::Unihan_IRGSources.txt::kIICore
        view /sdcard/0my_files/unzip/e_book/unicode_13__Unihan/Unihan_IRGSources.txt
        # [ABC][GHJKMPT]{1,7}
        level_char2char_pt_rngs
        sourceIRG_char2char_pt_rngs
            :: Map<char, NonTouchRanges>
            :: Map<char, StackStyleSimpleIntSet>

TODO:
    所有 虚函数 改名:格式为 _xxx_
        以保证 map(IRanges.xxx, ...)可正常工作！
    #'''
    @classmethod
    def _valid_ranges_(cls, ranges, /):
        raise NotImplementedError
        return valid_ranges(ranges)
    @classmethod
    def valid_ranges(cls, ranges, /):
        return cls._valid_ranges_(ranges)
    def is_nontouch_ranges(sf, /):
        return sf.__nontouch
    def to_nontouch_ranges(sf, /):
        if sf.__nontouch:
            return sf.ranges
        return tuple(sorted_rngs_to_iter_nontouch_ranges(sf.ranges))
        return sf.to_NonTouchRanges().ranges
    def to_hex_repr_pair_list(sf, /):
        return ranges2hex_repr_pair_list(sf)
    @staticmethod
    def from_hex_repr_pair_list(hexXhexszpair_list, /):
        return ranges5hex_repr_pair_list(hexXhexszpair_list)
    def to_hexXhexszpair_list(sf, /):
        return ranges2hexXhexszpair_list(sf)
    @staticmethod
    def from_hexXhexszpair_list(hexXhexszpair_list, /):
        return ranges5hexXhexszpair_list(hexXhexszpair_list)
    def to_len_rng2hexbegins(sf, /):
        return ranges2len_rng2hexbegins(sf)
    @staticmethod
    def from_len_rng2hexbegins(len_rng2hexbegins, /):
        return ranges5len_rng2hexbegins(len_rng2hexbegins)

    def to_len_rng2hexbegins_str(sf, /):
        return ranges2len_rng2hexbegins_str(sf)
    @staticmethod
    def from_len_rng2hexbegins_str(len_rng2hexbegins_str, /):
        return ranges5len_rng2hexbegins_str(len_rng2hexbegins_str)

    def to_len_rng2begin_chars(sf, /):
        return ranges2len_rng2begin_chars(sf)
    @staticmethod
    def from_len_rng2begin_chars(len_rng2begin_chars, /):
        return ranges5len_rng2begin_chars(len_rng2begin_chars)

    def __init__(sf, ranges, /):
        #ranges = tuple(ranges)
        if not type(sf).valid_ranges(ranges):
            raise TypeError('not {}.valid_ranges({})'.format(type(sf).__name__, ranges))
        sf.__ranges = ranges
        sf.__sz = len_ints_of_nonoverlap_rngs(ranges)
        sf.__nontouch = valid_nontouch_ranges(ranges)
    @property
    def ranges(sf, /):
        return sf.__ranges
    def _get_rngs_(sf, /):
        return sf.ranges
    #def __len__(sf, /):
    #    return sf.__sz
    def len_ints(sf, /):
        return sf.__sz
    def __hash_args(sf, /):
        return type(sf), sf.ranges
    def __hash__(sf, /):
        return hash(sf.__hash_args())
    def __eq__(sf, other, /):
        r"""
        #match __hash__
        see: set_eq
        #"""
        #assert isinstance(other, (TouchRanges, NonTouchRanges))
        if type(other) is not type(sf):
            return NotImplemented
        return sf.__hash_args() == other.__hash_args()
    def __repr__(sf, /):
        return '{}({})'.format(type(sf).__name__, sf.ranges)

    def _rel_op(sf, other, op, /, **kw):
        assert isinstance(other, (TouchRanges, NonTouchRanges))
        return op(sf.ranges, other.ranges, rhs_maynot_be_nontouch_ranges=not other.__nontouch, **kw)

    def _op(sf, other, op, /, **kw):
        assert isinstance(other, (TouchRanges, NonTouchRanges))
        ranges = op(sf.to_nontouch_ranges(), other.to_nontouch_ranges(), **kw)
        return make_NonTouchRanges(ranges)

    def __lt__(sf, other, /):
        return sf._rel_op(other, is_proper_subset_ex_of__xtouch_ranges)
    def __le__(sf, other, /):
        return sf._rel_op(other, is_subset_ex_of__xtouch_ranges)
    def set_eq(sf, other, /):
        #vs __eq__
        if sf.__nontouch and other.__nontouch:
            return sf.ranges == other.ranges
        return sf._rel_op(other, is_equal_set_ex_of__xtouch_ranges, lhs_maynot_be_nontouch_ranges=not sf.__nontouch)
        ########## old impl ############
        return sf._rel_op(other, is_equal_set_ex_of__xtouch_ranges)

    def __or__(sf, other, /):
        return sf._op(other, union_ex__xtouch_ranges, faster_output_iter_touch_ranges=False)

    def __and__(sf, other, /):
        return sf._op(other, intersection__xtouch_ranges)

    def __sub__(sf, other, /):
        return sf._op(other, difference__xtouch_ranges)
    def __xor__(sf, other, /):
        return sf._op(other, symmetric_difference_ex__xtouch_ranges, faster_output_iter_touch_ranges=False)


class TouchRanges(IRanges):
    def _to_NonTouchRanges_(sf, /):
        return make_NonTouchRanges(sorted_rngs_to_iter_nontouch_ranges(sf.ranges))
    @classmethod
    def _valid_ranges_(cls, ranges, /):
        return valid_touch_ranges(ranges)


class NonTouchRanges(IRanges):
    def _to_NonTouchRanges_(sf, /):
        return sf
    @classmethod
    def _valid_ranges_(cls, ranges, /):
        return valid_nontouch_ranges(ranges)


assert make_NonTouchRanges([(0,2), (3,4), (5,7)]).contains_all([(0,1), 3, 6, (0,2), (6,7)])
assert 2 not in make_NonTouchRanges([(0,2), (3,4), (5,7)])
assert make_NonTouchRanges([(0,2), (3,4), (5,7)]).gaps() == ((2,3), (4,5),)

assert make_TouchRanges([(0,3), (3,4), (5,7)]).contains_all([(0,4), 3, 6, (0,2), (6,7),])
assert 4 not in make_TouchRanges([(0,3), (3,4), (5,7)])
assert make_TouchRanges([(0,3), (3,4), (5,7)]).gaps() == ((4,5),)



r"""
_test_case_for_
    union
    symmetric_difference
    intersection
    difference
    is_subset_ex
#"""

#::test cases
def _gen_test_cases():
    from seed.test_utils.generate_test_data import str2valuess_by_line2exprs

    rng_pairs_str = r"""
#13==C(5,2)+3
(3,6); (1,2) #1
(3,6); (1,3)
(3,6); (1,4)
(3,6); (1,6)
(3,6); (1,7)
(3,6); (3,4)
(3,6); (3,6)
(3,6); (3,7)
(3,6); (4,5) #1
(3,6); (4,6)
(3,6); (4,7)
(3,6); (6,7)
(3,6); (7,8) #1
#"""
    rng_pairs = str2valuess_by_line2exprs(rng_pairs_str)
    kwF = dict(faster_output_iter_touch_ranges=False)
    kwT = dict(faster_output_iter_touch_ranges=True)
    print('#[(lhs, rhs), (oF, oT, xF, xT, a, d, cmp, rels)]')
    for rng0, rng1 in rng_pairs:
        lhs = [rng0]
        rhs = [rng1]
        oF = union_ex__xtouch_ranges(lhs, rhs, **kwF)
        oT = union_ex__xtouch_ranges(lhs, rhs, **kwT)
        xF = symmetric_difference_ex__xtouch_ranges(lhs, rhs, **kwF)
        xT = symmetric_difference_ex__xtouch_ranges(lhs, rhs, **kwT)
        a = intersection__xtouch_ranges(lhs, rhs)
        d = difference__xtouch_ranges(lhs, rhs)
        cmp = subset_cmp_ex__xtouch_ranges(lhs, rhs, rhs_maynot_be_nontouch_ranges=False)
        [*rels] = iter_with_middle_state_of_subset_relation_ex__xtouch_ranges(lhs, rhs, lhs_maynot_be_nontouch_ranges=False, rhs_maynot_be_nontouch_ranges=False)

        (oF, oT, xF, xT, a, d) = map(list, (oF, oT, xF, xT, a, d))
        print([(lhs, rhs), (oF, oT, xF, xT, a, d, cmp, rels)])

def test_subset_relation_ex__xtouch_ranges(num_periods=2, /):
    r"""
    gapT = 3
    bkT = 3
    n = -1+(gapT+bkT)*num_periods +(gapT-1)
    num_loops = 2**n
    #"""
    gapT = 3
    bkT = 3
    n = -1+(gapT+bkT)*num_periods +(gapT-1)
    num_loops = 2**n
    ######
    def h(a, /):
        #iter_xtouch_ranges -> (xtouch_ranges, ks, set<int>
        #ais = rngs_to_iter_ints(a)
        a = make_Ranges(a)
        ks = [True]
        if a.is_nontouch_ranges():
            ks.append(False)
        ais = set(a.iter_ints())
        return a.ranges, ks, ais
    def cmp(lhs, rhs, /):
        #lhs, rhs :: set<int>
        if lhs == rhs:
            r = 3
        elif lhs < rhs:
            r = 1
        elif lhs > rhs:
            r = 2
        else:
            r = 0
        return r
    def g(a, b, /):
        #a, b :: iter_xtouch_ranges
        a, aks, ais = h(a)
        b, bks, bis = h(b)
        lr = cmp(ais, bis)
        rr = [0, 2, 1, 3][lr]
        f(lr, a, aks, b, bks)
        f(rr, b, bks, a, aks)
    def ff(set_r, lhs, lk, rhs, rk, /):
        #bug:rngs_r = fff(lhs, lk, rhs, lk)
        rngs_r = fff(lhs, lk, rhs, rk)
        try:
            assert set_r == rngs_r
        except:
            print_err(f"set_r={set_r}")
            print_err(f"rngs_r={rngs_r}")
            print_err(f"lhs={lhs}")
            print_err(f"lk={lk}")
            print_err(f"rhs={rhs}")
            print_err(f"rk={rk}")
            raise
    def fff(lhs, lk, rhs, rk, /):
        return subset_relation_ex__xtouch_ranges(lhs, rhs, lhs_maynot_be_nontouch_ranges=lk, rhs_maynot_be_nontouch_ranges=rk, faster_return_not_le=False, faster_return_not_ge=False)
    def f(set_r, lhs, lks, rhs, rks, /):
        #lhs, rhs :: xtouch_ranges
        for lk in lks:
            for rk in rks:
                ff(set_r, lhs, lk, rhs, rk)
    #######
    assert num_periods >= 1
    T = gapT + bkT
    a1 = [(-1+T*i+gapT, -1+T*(i+1)) for i in range(num_periods)]
    n1 = -1+T*num_periods +(gapT-1)
    if num_periods == 2:
        assert a1 == [(2, 5), (8, 11)]
        assert n1 == 13
    a2 = [*a1, (a1[-1][-1], a1[-1][-1] +bkT)]
    n2 = -1+T*num_periods +bkT +(gapT-1)
    if num_periods == 2:
        assert a2 == [(2, 5), (8, 11), (11, 14)]
        assert n2 == 16

    def bug1():
        set_r=1
        rngs_r=0
        lhs=((2, 3), (4, 5), (8, 9), (10, 12))
        lk=False
        rhs=((2, 5), (8, 11), (11, 14))
        rk=True
        ff(set_r, lhs, lk, rhs, lk)
    if 0:
        bug1()

    for b in iter_nontouch_rangess_between(0, n1):
        g(a1, b)
    for b in iter_nontouch_rangess_between(0, n2):
        g(a2, b)


def iter_nontouch_rangess_between(begin, end, /):
    for ls in iter_subsets_of(range(begin, end)):
        if 0:
            rngs = sorted_unique_ints_to_iter_nontouch_ranges(ls)
        else:
            if len(ls)%2:
                ls = (*ls, end)
            rngs = zip(ls[0::2], ls[1::2])
        rngs = tuple(rngs)
        yield rngs

class StackStyleSimpleIntSet(IMixin4_get_rngs_):
    r'''
    .rngs :: [(int, int)] #nontouch_ranges
        public-mutable
        NOTE: SHOULD call fix_after_modify_rngs after update .rngs externally
    #'''
    def _to_NonTouchRanges_(sf, /):
        rngs = sf.rngs
        return NonTouchRanges((*rngs,))
        return make_NonTouchRanges(sorted_rngs_to_iter_nontouch_ranges(rngs))
    def __eq__(sf, other, /):
        if type(other) is not type(sf):
            return NotImplemented
        return sf.rngs == other.rngs
    def __init__(sf, rngs=None, /):
        if rngs is None:
            rngs = []
        sf.rngs = rngs #set sf._sz via @property
    def fix_after_modify_rngs(sf, /,*, turnoff__check_rngs=False, may_delta4size=None):
        rngs = sf.rngs
        if not turnoff__check_rngs:
            sf.check_rngs(rngs)
        if may_delta4size is None:
            sf._sz = sum(j-i for i,j in rngs)
        else:
            delta4size = may_delta4size
            sf._sz += delta4size
    def push_rngs(sf, rngs, /):
        it = map(sf.push_rng, rngs)
        for _ in it:pass
    def push_rng(sf, rng, /):
        begin_, end_ = rng
        if not type(begin_) is int: raise TypeError
        if not type(end_) is int: raise TypeError
        if not begin_ < end_: return
        sf.push(begin_)
        rngs = sf.rngs
        (begin, end) = rngs[-1]
        assert end == begin_+1

        delta4size = end_ - end
        assert delta4size >= 0

        if delta4size:
            rngs[-1] = (begin, end_)
            sf._sz += delta4size
        return

    def push(sf, i, /):
        if not type(i) is int: raise TypeError
        rngs = sf.rngs
        if not rngs:
            rngs.append((i, i+1))
        else:
            (begin, end) = rngs[-1]
            if i == end:
                rngs[-1] = (begin, i+1)
            elif end < i:
                rngs.append((i, i+1))
            elif i < end:
                raise KeyError('stack_styple-int-set: add(i) but i < end')
            else:
                raise logic-err
        sf._sz += 1
        return
    add = push
    def get_top(sf, /):
        rngs = sf.rngs
        if not rngs: raise KeyError('get_top from an empty set')
        return rngs[-1][-1] -1
    def pop(sf, /):
        rngs = sf.rngs
        if not rngs: raise KeyError('pop from an empty set')
        (begin, end) = rngs[-1]
        end -= 1
        if begin == end:
            rngs.pop()
        else:
            rngs[-1] = (begin, end)
        sf._sz -= 1
        return end
    def __delitem__(sf, i, /):
        if not sf: raise KeyError('__delitem__ from an empty set')
        top = sf.get_top()
        if not i == top: raise KeyError(f'stack_styple-int-set: __delitem__(i) but i == {i} != {top} == top')
        j = sf.pop()
        assert j == i
    def __len__(sf, /):
        return sf._sz
    def __repr__(sf, /):
        return '{}({})'.format(type(sf).__name__, sf.rngs)



    @property
    def rngs(sf, /):
        return sf._rngs
    @rngs.setter
    def rngs(sf, rngs, /):
        sf.check_rngs(rngs)
        sf._rngs = rngs
        sf.fix_after_modify_rngs(turnoff__check_rngs=True)

    @classmethod
    def check_rngs(cls, rngs, /):
        'check rngs is nontouch_ranges-list-version'
        if not type(rngs) is list: raise TypeError
        if not 15 == detect_iter_ranges(rngs): raise TypeError #not nontouch_ranges-list-version
    @classmethod
    def from_clone_of_rngs(cls, rngs, /):
        rngs = [*make_Ranges(rngs).to_nontouch_ranges()]
        return cls(rngs)
    def _get_rngs_(sf, /):
        rngs = sf.rngs
        return rngs





#end:class StackStyleSimpleIntSet:



class IRangeBasedIntMapping(IMixin4_get_rngs_):
    r'''
ABC IRangeBasedIntMapping:
    * immutable TouchRangeBasedIntMapping
    * mutable StackStyleSimpleIntMapping

see also:
    ABC IRanges

used:
    to repr parse result of unicode::UCD::Blocks.txt
        view /sdcard/0my_files/unzip/e_book/unicode_13__UCD/Blocks.txt
        char_pt_rng2code_block_name
            :: TouchRangeBasedIntMapping<str>
            :: StackStyleSimpleIntMapping<str>
        code_block_name2char_pt_rngs
            :: Map<str, NonTouchRanges>
            :: Map<str, StackStyleSimpleIntSet>

    #'''
    def _to_TouchRangeBasedIntMapping_(sf, /):
        '-> immutable TouchRangeBasedIntMapping'
        raise NotImplementedError
    def to_TouchRangeBasedIntMapping(sf, /):
        return sf._to_TouchRangeBasedIntMapping_()
    @classmethod
    def _get_type_of_seq4both_rngs_and_values(cls, /):
        '-> seq_type'
        raise NotImplementedError
    def __len__(sf, /):
        '-> len_ints'
        raise NotImplementedError
    def _get_rngs_values_pair_(sf, /):
        '-> ([rng], [value])'
        raise NotImplementedError
    @property
    def rngs_values_pair(sf, /):
        return sf._get_rngs_values_pair_()
    def _get_rngs_(sf, /):
        rngs, values = sf.rngs_values_pair
        return rngs
    _to_NonTouchRanges_ = TouchRanges._to_NonTouchRanges_


    def __eq__(sf, other, /):
        if type(other) is not type(sf):
            return NotImplemented
        return sf.rngs_values_pair == other.rngs_values_pair



    @classmethod
    def from_rng_value_pairs(cls, rng_value_pairs, /):
        '-> sf'
        d = StackStyleSimpleIntMapping()
        d.push_rng_value_pairs(rng_value_pairs)
        if cls is type(d):
            sf = d
            del d
        else:
            rngs, values = d.rngs_values_pair
            del d

            seq_type = cls._get_type_of_seq4both_rngs_and_values()
            if not seq_type is list:
                rngs = seq_type(rngs)
                values = seq_type(values)
            sf = cls((rngs, values))
        sf
        return sf

    def get_top(sf, /):
        '-> (i, v)'
        rngs, values = sf.rngs_values_pair
        if not rngs: raise KeyError('get_top from an empty mapping')
        return rngs[-1][-1] -1, values[-1]
    def __repr__(sf, /):
        rngs, values = sf.rngs_values_pair
        return '{}({})'.format(type(sf).__name__, (rngs, values))



    @classmethod
    def check_rngs(cls, rngs, /):
        'check rngs is touch_ranges-list-version'
        list = cls._get_type_of_seq4both_rngs_and_values()
        if not type(rngs) is list: raise TypeError
        if not 7 <= detect_iter_ranges(rngs): raise TypeError #not touch_ranges-list-version
    @classmethod
    def check_values(cls, rngs, values, /):
        'postcondition:[two rngs touch]==>>[their values diff]   ##precondition: check_rngs(rngs) ==>> [rngs is touch_ranges-list-version]'
        list = cls._get_type_of_seq4both_rngs_and_values()
        if not type(values) is list: raise TypeError
        for _ in map(hash, values):pass
        if not len(rngs) == len(values): raise TypeError
        L = len(values)
        for i in range(L-1):
            [(begin0, end0), (begin1, end1)] = rngs[i:i+2]
            if end0 == begin1:
                #touch
                #==>> value diff
                v0, v1 = values[i:i+2]
                if v0 == v1: raise TypeError('two rngs touch with same value but not merge into one rng')
    @classmethod
    def from_clone_of_rngs_with_default(cls, rngs, value, /):
        list = cls._get_type_of_seq4both_rngs_and_values()
        rngs = list(make_Ranges(rngs).to_nontouch_ranges())
        values = list([value])*len(rngs)
        return cls((rngs, values))

    def __getitem__(sf, i, /):
        return sf.getitem4int(i)
    def getitem4int(sf, i, /):
        rngs, values = sf.rngs_values_pair
        may_rng, imay_idx = rngs_op__get_maybe_range_contained_ex(rngs, i)
        if may_rng is not None:
            assert imay_idx >= 0
            idx = imay_idx
            v = values[idx]
            return v
        raise KeyError(i)
    #def getitem4rng_ex(sf, sub_rng, /):
    def iter_intersect_range_ex__with_value(sf, rng, /):
        '-> Iter<(idx, common_rng, value)>'
        rngs, values = sf.rngs_values_pair
        it = rngs_op__iter_intersect_range_ex(rngs, rng)
        for idx, common_rng in it:
            v = values[idx]
            yield idx, common_rng, v
        return

    def iter_values__per_rng_(sf, /, reverse):
        rngs, values = sf.rngs_values_pair
        g = reversed if reverse else iter
        return g(values)
    def iter_rng_value_pairs_(sf, /, reverse):
        rngs, values = sf.rngs_values_pair
        g = reversed if reverse else iter
        return zip(g(rngs), g(values))


    def items(sf, /):
        return sf.iter_items_(reverse=False)
    def reversed_items(sf, /):
        return sf.iter_items_(reverse=True)
    def iter_items_(sf, /, reverse):
        xreversed_rng_value_pairs = sf.iter_rng_value_pairs_(reverse=reverse)
        reverse = iter if reverse else False
        return rng_value_pairs_to_iter_int_value_pairs_(xreversed_rng_value_pairs, reverse=reverse)
class TouchRangeBasedIntMapping(IRangeBasedIntMapping):
    def _to_TouchRangeBasedIntMapping_(sf, /):
        '-> immutable TouchRangeBasedIntMapping'
        return sf
    @classmethod
    def _get_type_of_seq4both_rngs_and_values(cls, /):
        '-> seq_type'
        return tuple
    def __len__(sf, /):
        '-> len_ints'
        return sf._sz
    def _get_rngs_values_pair_(sf, /):
        '-> ([rng], [value])'
        return sf._rngs_values_pair
    def __init__(sf, rngs_values_pair=None, /):
        if rngs_values_pair is None:
            rngs_values_pair = (), ()

        if not type(rngs_values_pair) is tuple: raise TypeError
        rngs, values = rngs_values_pair
        sf.check_rngs(rngs)
        sf.check_values(rngs, values)
        if not len(rngs) == len(values): raise TypeError
        sf._sz = sum(j-i for i,j in rngs)
        sf._rngs_values_pair = rngs_values_pair

    def __hash_args(sf, /):
        return type(sf), sf.rngs_values_pair
    def __hash__(sf, /):
        return hash(sf.__hash_args())
    def __eq__(sf, other, /):
        if type(other) is not type(sf):
            return NotImplemented
        return sf.__hash_args() == other.__hash_args()

class StackStyleSimpleIntMapping(IRangeBasedIntMapping):
    r'''
    .rngs :: [(int, int)] #touch_ranges
    .values :: [immutable_hashable]{len(.values)==len(.rngs)}
        public-mutable
        NOTE: SHOULD call fix_after_modify_rngs after update .rngs/.values externally
    #'''
    def _to_TouchRangeBasedIntMapping_(sf, /):
        '-> immutable TouchRangeBasedIntMapping'
        rngs, values = sf.rngs_values_pair
        rngs = to_tuple(rngs)
        values = to_tuple(values)
        return TouchRangeBasedIntMapping((rngs,values))
    @classmethod
    def _get_type_of_seq4both_rngs_and_values(cls, /):
        '-> seq_type'
        return list
    def __len__(sf, /):
        '-> len_ints'
        return sf._sz
    def _get_rngs_values_pair_(sf, /):
        #保证IRangeBasedIntMapping.rngs_values_pair 能找到有效的_get_rngs_values_pair_
        '-> ([rng], [value])'
        return sf._rngs_values_pair
    @property
    def rngs_values_pair(sf, /):
        return sf._get_rngs_values_pair_()
    @rngs_values_pair.setter
    def rngs_values_pair(sf, rngs_values_pair, /):
        if not type(rngs_values_pair) is tuple: raise TypeError
        rngs, values = rngs_values_pair
        sf.check_rngs(rngs)
        sf.check_values(rngs, values)
        sf._rngs_values_pair = rngs_values_pair
        sf.fix_after_modify_rngs(turnoff__check_rngs=True, turnoff__check_values=True)



    def __init__(sf, rngs_values_pair=None, /):
        if rngs_values_pair is None:
            rngs_values_pair = [], []

        sf.rngs_values_pair = rngs_values_pair #set sf._sz via @property
    def fix_after_modify_rngs(sf, /,*,  turnoff__check_values=False,turnoff__check_rngs=False, may_delta4size=None):
        rngs, values = sf.rngs_values_pair
        if not len(rngs) == len(values): raise TypeError

        if not turnoff__check_rngs:
            sf.check_rngs(rngs)
        if not turnoff__check_values:
            sf.check_values(rngs, values)
        if may_delta4size is None:
            sf._sz = sum(j-i for i,j in rngs)
        else:
            delta4size = may_delta4size
            sf._sz += delta4size
    def push_rng_value_pairs(sf, rng_value_pairs, /):
        for rng, v in rng_value_pairs:
            sf.push_rng_value(rng, v)
    def push_rng_value(sf, rng, v, /):
        begin_, end_ = rng
        if not type(begin_) is int: raise TypeError
        if not type(end_) is int: raise TypeError
        if not begin_ < end_: return
        sf.push(begin_, v)

        rngs, values = sf.rngs_values_pair
        (begin, end) = rngs[-1]
        assert end == begin_+1

        delta4size = end_ - end
        assert delta4size >= 0

        if delta4size:
            rngs[-1] = (begin, end_)
            sf._sz += delta4size
        return

    def push(sf, i, v, /):
        if not type(i) is int: raise TypeError
        hash(v)

        rngs, values = sf.rngs_values_pair
        if not rngs:
            rngs.append((i, i+1))
            values.append(v)
        else:
            (begin, end) = rngs[-1]
            vt = values[-1]
            if i == end and v == vt:
                #merge & discard v
                rngs[-1] = (begin, i+1)
            elif end <= i:
                rngs.append((i, i+1))
                values.append(v)
            elif i < end:
                raise KeyError('stack_styple-int-mapping: __setitem__(i, v) but i < end')
            else:
                raise logic-err
        sf._sz += 1
        return
    __setitem__ = push
    #def get_top(sf, /):
    def pop(sf, /):
        '-> (i, v)'
        rngs, values = sf.rngs_values_pair
        if not rngs: raise KeyError('pop from an empty mapping')
        (begin, end) = rngs[-1]
        end -= 1
        if begin == end:
            rngs.pop()
            v = values.pop()
        else:
            rngs[-1] = (begin, end)
            v = values[-1]
        sf._sz -= 1
        return end, v
    def __delitem__(sf, i, /):
        if not sf: raise KeyError('__delitem__ from an empty mapping')
        top_key, top_value = top_item = sf.get_top()
        if not i == top_key: raise KeyError(f'stack_styple-int-mapping: __delitem__(i) but i == {i} != {top_key} == top_key')
        j, v = sf.pop()
        assert j == i
    #def __len__(sf, /):
    #def __repr__(sf, /):



#end:class StackStyleSimpleIntMapping:


ranges2hex_repr_pair_list = dot[fmap_rngs2hex_repr, IMixin4_get_rngs_._O_get_rngs_O_]
ranges5hex_repr_pair_list = dot[make_Ranges, fmapT__pairs(int, int)]

def iter_rngs2iter_hexXhexszpair_list(rngs, /):
    'Iter rng -> Iter (HexReprInt|(HexReprInt, int))'
    for begin, end in rngs:
        sz = end-begin
        begin__HexReprInt = HexReprInt(begin)
        if sz==1:
            x = begin__HexReprInt
        elif sz >= 2:
            x = begin__HexReprInt, sz
        else:
            continue
        yield x
def iter_rngs5iter_hexXhexszpair_list(xs, /):
    'Iter (HexReprInt|(HexReprInt, int)) -> Iter rng'
    for x in xs:
        if hasattr(x, '__len__'):
            pair = x
            begin, sz = map(int, pair)
        else:
            single = x
            begin = int(single)
            sz = 1
        end = begin + sz
        yield begin, end

def ranges2hexXhexszpair_list(ranges, /):
    'IRanges -> [(HexReprInt|(HexReprInt, int))]'
    return list(iter_rngs2iter_hexXhexszpair_list(ranges.ranges))
def ranges5hexXhexszpair_list(xs, /):
    '[(HexReprInt|(HexReprInt, int))] -> IRanges'
    return make_Ranges(iter_rngs5iter_hexXhexszpair_list(xs))
iter_rngs2iter_hexXhexszpair_list
iter_rngs5iter_hexXhexszpair_list
ranges2hexXhexszpair_list
ranges5hexXhexszpair_list


def len_of__rng(rng, /):
    begin, end = rng
    sz = end - begin
    return sz
def ranges2len_rng2hexbegins(ranges, /):
    'IRanges -> {len_rng/int: [begin/HexReprInt]}'
    len_rngs = {*map(len_of__rng, ranges.iter_rngs())}
    len_rng2hexbegins = {len_rng:[] for len_rng in len_rngs}
    for rng in ranges.iter_rngs():
        len_rng = len_of__rng(rng)
        begin, _ = rng
        begin__HexReprInt = HexReprInt(begin)
        len_rng2hexbegins[len_rng].append(begin__HexReprInt)
    assert all(len_rng2hexbegins.values())
    return len_rng2hexbegins
def ranges5len_rng2hexbegins(len_rng2hexbegins, /):
    '{len_rng/int: [begin/HexReprInt]} -> IRanges'
    def _iter():
        for len_rng, hexbegins in len_rng2hexbegins.items():
            for begin in map(int, hexbegins):
                end = begin+len_rng
                yield begin, end
    return make_Ranges(sorted(_iter()))
ranges2len_rng2hexbegins
ranges5len_rng2hexbegins

def hexbegins2str(hexbegins, /):
    return repr(hexbegins)[3:-1].replace(', 0x', ',').upper()
def hexbegins5str(hexbegins_str, /):
    hex_ls = hexbegins_str.split(',')
    #map(HexReprInt, map(hex2int, hex_ls))
    return [HexReprInt(h, 16) for h in hex_ls]

def ranges2len_rng2hexbegins_str(ranges, /):
    'IRanges -> {len_rng/int: ",".join(f"{begin:X}"...)}'
    len_rng2hexbegins = ranges2len_rng2hexbegins(ranges)
    len_rng2hexbegins_str = fmap4dict_value(hexbegins2str, len_rng2hexbegins)
    return len_rng2hexbegins_str
def ranges5len_rng2hexbegins_str(len_rng2hexbegins_str, /):
    '{len_rng/int: ",".join(f"{begin:X}"...)} -> IRanges'
    len_rng2hexbegins = fmap4dict_value(hexbegins5str, len_rng2hexbegins_str)
    ranges = ranges5len_rng2hexbegins(len_rng2hexbegins)
    return ranges
ranges2len_rng2hexbegins_str
ranges5len_rng2hexbegins_str

def hexbegins2chars(hexbegins, /):
    return ''.join(map(chr, hexbegins))
def hexbegins5chars(begin_chars, /):
    return [*map(HexReprInt, map(ord, begin_chars))]

def ranges2len_rng2begin_chars(ranges, /):
    'IRanges -> {len_rng/int: "".join(map(chr,begins))}'
    len_rng2hexbegins = ranges2len_rng2hexbegins(ranges)
    len_rng2begin_chars = fmap4dict_value(hexbegins2chars, len_rng2hexbegins)
    return len_rng2begin_chars
def ranges5len_rng2begin_chars(len_rng2begin_chars, /):
    '{len_rng/int: "".join(map(chr,begins))} -> IRanges'
    len_rng2hexbegins = fmap4dict_value(hexbegins5chars, len_rng2begin_chars)
    ranges = ranges5len_rng2hexbegins(len_rng2hexbegins)
    return ranges
ranges2len_rng2begin_chars
ranges5len_rng2begin_chars


if __name__ == "__main__":
    print('\n'.join(s for s in globals() if not s.startswith('_')))
    import doctest
    doctest.testmod()
    if 0:
        raise
        test_subset_relation_ex__xtouch_ranges()

