

r'''
py -m seed.data_funcs.rngs
from seed.data_funcs.rngs import make_Ranges, sorted_ints_to_iter_nontouch_ranges, detect_iter_ranges, StackStyleSimpleIntSet

===============================
===============================
NOTE: use Ranges.set_eq instead of "=="
===============================
===============================
main_exports:
    make_Ranges
    sorted_ints_to_iter_nontouch_ranges
    detect_iter_ranges
    StackStyleSimpleIntSet
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

#'''


__all__ = """
    iter_nontouch_rangess_between
    ints_to_iter_local_unique_ints
    sorted_unique_ints_to_iter_nontouch_ranges
        sorted_ints_to_iter_nontouch_ranges
    sorted_rngs_to_iter_nontouch_ranges
    rngs_to_iter_ints
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


    StackStyleSimpleIntSet
    """.split()

import bisect
from operator import lt, le
from seed.iters.PeekableIterator import PeekableIterator
from seed.iters.iter_subsets_of import iter_subsets_of__dictionary_order as iter_subsets_of
from seed.tiny import print_err

def all_map(pred, iterable):
    return all(map(pred, iterable))
def ints_to_iter_local_unique_ints(ints):
    it = iter(ints)
    for pre in it:
        yield pre
        break
    for curr in it:
        if curr != pre:
            yield curr
            pre = curr
def sorted_ints_to_iter_nontouch_ranges(sorted_ints):
    sorted_unique_ints = ints_to_iter_local_unique_ints(sorted_ints)
    return sorted_unique_ints_to_iter_nontouch_ranges(sorted_unique_ints)
def sorted_unique_ints_to_iter_nontouch_ranges(sorted_unique_ints):
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
            raise ValueError('not sorted_unique_ints: {} {}'.format(end-1, last))
    yield begin, end
    pass

r"""
def sorted_unique_ints_to_nontouch_ranges(ints):
    return tuple(sorted_unique_ints_to_iter_nontouch_ranges(ints))
assert sorted_unique_ints_to_nontouch_ranges([0,1,3]) == ((0,2), (3,4))
assert sorted_unique_ints_to_nontouch_ranges([0]) == ((0,1),)
assert sorted_unique_ints_to_nontouch_ranges([]) == ()
#"""













def rngs_to_iter_ints(rngs):
    for begin, end in rngs:
        yield from range(begin, end)
def len_ints_of_nonoverlap_rngs(nonoverlap_rngs):
    return sum(end - begin for begin, end in nonoverlap_rngs)






def sorted_rngs_to_iter_nontouch_ranges(sorted_rngs):
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


def are_disjoint_two_touch_ranges(lhs_touch_ranges, rhs_touch_ranges):
    it = intersection__xtouch_ranges(lhs_touch_ranges, rhs_touch_ranges)
    for _ in it:
        return False
    else:
        return True
#
def symmetric_difference_ex__xtouch_ranges(lhs_xtouch_ranges, rhs_xtouch_ranges, *, faster_output_iter_touch_ranges:bool):
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

def _skip_util(it, _begin_):
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


def union_ex__xtouch_ranges(lhs_xtouch_ranges, rhs_xtouch_ranges, *, faster_output_iter_touch_ranges:bool):
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




def intersection__xtouch_ranges(lhs_xtouch_ranges, rhs_xtouch_ranges):
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



def difference__xtouch_ranges(lhs_xtouch_ranges, rhs_xtouch_ranges):
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

def is_equal_set_ex_of__xtouch_ranges(lhs_xtouch_ranges, rhs_xtouch_ranges, *, lhs_maynot_be_nontouch_ranges:bool, rhs_maynot_be_nontouch_ranges:bool):
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
#def is_equal_set_ex_of__xtouch_ranges(lhs_xtouch_ranges, rhs_xtouch_ranges, *, rhs_maynot_be_nontouch_ranges:bool):
    return 0 == subset_cmp_ex__xtouch_ranges(lhs_xtouch_ranges, rhs_xtouch_ranges, rhs_maynot_be_nontouch_ranges=rhs_maynot_be_nontouch_ranges)
def is_subset_ex_of__xtouch_ranges(lhs_xtouch_ranges, rhs_xtouch_ranges, *, rhs_maynot_be_nontouch_ranges:bool):
    return 0 >= subset_cmp_ex__xtouch_ranges(lhs_xtouch_ranges, rhs_xtouch_ranges, rhs_maynot_be_nontouch_ranges=rhs_maynot_be_nontouch_ranges)
def is_proper_subset_ex_of__xtouch_ranges(lhs_xtouch_ranges, rhs_xtouch_ranges, *, rhs_maynot_be_nontouch_ranges:bool):
    return 0 > subset_cmp_ex__xtouch_ranges(lhs_xtouch_ranges, rhs_xtouch_ranges, rhs_maynot_be_nontouch_ranges=rhs_maynot_be_nontouch_ranges)

class PartialOrderingCompareResult:
    NA = 0
    LT = 1
    GT = 2
    EQ = 3
    @classmethod
    def get_mirror_class(cls):
        return LeftRightHandSideFlip
    @classmethod
    def get_FASTER_NOT_LE(cls):
        return (7 ^ cls.LT) # == (4 | cls.GT) == (7 & ~cls.LT)
    @classmethod
    def get_FASTER_NOT_GE(cls):
        return (7 ^ cls.GT) # == (4 | cls.LT) == (7 & ~cls.GT)
    @classmethod
    def le(cls, r):
        return bool(r & cls.LT)
    @classmethod
    def ge(cls, r):
        return bool(r & cls.GT)
    @classmethod
    def na(cls, r):
        return (r==cls.NA)
    @classmethod
    def lt(cls, r):
        return (r==cls.LT)
    @classmethod
    def gt(cls, r):
        return (r==cls.GT)
    @classmethod
    def eq(cls, r):
        return (r==cls.EQ)
class LeftRightHandSideFlip(PartialOrderingCompareResult):
    LT = PartialOrderingCompareResult.GT
    GT = PartialOrderingCompareResult.LT
    @classmethod
    def get_mirror_class(cls):
        return PartialOrderingCompareResult
def _():
    R = PartialOrderingCompareResult
    assert R.get_FASTER_NOT_GE() == 5
    assert R.get_FASTER_NOT_LE() == 6
    for R in [R, R.get_mirror_class()]:
        assert R.get_FASTER_NOT_GE() == (4 | R.LT) == (7 & ~R.GT) == (7 ^ R.GT)
        assert R.get_FASTER_NOT_LE() == (4 | R.GT) == (7 & ~R.LT) == (7 ^ R.LT)

_(); del _

def subset_relation_ex__xtouch_ranges(lhs_xtouch_ranges, rhs_xtouch_ranges, *, lhs_maynot_be_nontouch_ranges:bool, rhs_maynot_be_nontouch_ranges:bool, faster_return_not_le:bool, faster_return_not_ge:bool):
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
        raise logic-error
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
    def on_lhs_is_empty(largs, r):
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

    def on_rend_le_lbegin(largs, r, _end, begin_):
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


def iter_with_middle_state_of_subset_relation_ex__xtouch_ranges(lhs_xtouch_ranges, rhs_xtouch_ranges, *, lhs_maynot_be_nontouch_ranges:bool, rhs_maynot_be_nontouch_ranges:bool):
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






def subset_cmp_ex__xtouch_ranges(lhs_xtouch_ranges, rhs_xtouch_ranges, *, rhs_maynot_be_nontouch_ranges:bool):
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
        raise logic-error
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
def valid_range(range):
    if type(range) is not tuple:
        return False
    begin, end = range
    if not type(begin) is int is type(end):
        return False
    return begin < end
def check_range(rng):
    if not valid_range(rng):
        raise ValueError('not valid_range({})'.format(rng))

def detect_ranges(ranges):
    r"""
    0 | 1 | 3 | 7 | 15
    not tuple<rng> | is tuple<rng> | is sorted_rngs | is touch_ranges | is nontouch_ranges
    #"""
    if type(ranges) is not tuple:
        return 0
    return detect_iter_ranges(ranges)
def detect_iter_ranges(iterable):
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

def valid_nontouch_ranges(ranges):
    return _valid_ranges(ranges, lt)
def valid_touch_ranges(ranges):
    return _valid_ranges(ranges, le)
def _valid_ranges(ranges, lt):
    if type(ranges) is not tuple:
        return False
    if not all_map(valid_range, ranges):
        return False
    for i in range(len(ranges) - 1):
        a, b = ranges[i:i+2]
        if not lt(a[-1], b[0]):
            return False
    return True

def is_subrange_of(sub_rng, super_rng):
    check_range(sub_rng)
    check_range(super_rng)

    begin, end = sub_rng
    lower, upper = super_rng
    return lower <= begin and end <= upper
assert is_subrange_of((0,3), (0,3))
assert not is_subrange_of((0,3), (0,2))
assert not is_subrange_of((0,3), (1,3))
assert is_subrange_of((0,2), (0,3))

def to_tuple(iterable):
    if type(iterable) is tuple:
        return iterable
    return tuple(iterable)
def make_NonTouchRanges(iterable_nontouch_ranges):
    return NonTouchRanges(to_tuple(iterable_nontouch_ranges))
def make_TouchRanges(iterable_touch_ranges):
    return TouchRanges(to_tuple(iterable_touch_ranges))
def make_Ranges(iterable_touch_ranges):
    ranges = to_tuple(iterable_touch_ranges)
    case = detect_ranges(ranges)
    if case == 15:
        cls = NonTouchRanges
    elif case == 7:
        cls = TouchRanges
    else:
        raise ValueError('not valid_touch_ranges({})'.format(ranges))
    return cls(ranges)

class Ranges:
    def to_NonTouchRanges(self):
        raise NotImplementedError
    @classmethod
    def valid_ranges(cls, ranges):
        raise NotImplementedError
        return valid_ranges(ranges)
    def is_nontouch_ranges(self):
        return self.__nontouch
    def to_nontouch_ranges(self):
        if self.__nontouch:
            return self.ranges
        return tuple(sorted_rngs_to_iter_nontouch_ranges(self.ranges))
        return self.to_NonTouchRanges().ranges
    def __init__(self, ranges):
        #ranges = tuple(ranges)
        if not type(self).valid_ranges(ranges):
            raise ValueError('not {}.valid_ranges({})'.format(type(self).__name__, ranges))
        self.__ranges = ranges
        self.__sz = len_ints_of_nonoverlap_rngs(ranges)
        self.__nontouch = valid_nontouch_ranges(ranges)
    @property
    def ranges(self):
        return self.__ranges
    #def __len__(self):
    #    return self.__sz
    def len_ints(self):
        return self.__sz
    def maybe_range_contained(self, i):
        # None | rng
        return self.maybe_range_contained_ex(i)[0]
    def maybe_range_contained_ex(self, i):
        rngs = self.ranges
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

    def __contains__(self, int_or_rng):
        if isinstance(int_or_rng, int):
            begin = int_or_rng
            end = begin + 1
            sub_rng = begin, end
        else:
            sub_rng = int_or_rng
        return self.contains_range(sub_rng)
    def contains_range(self, sub_rng):
        check_range(sub_rng)
        rngs = self.ranges
        begin, end = sub_rng
        may_rng, idx = self.maybe_range_contained_ex(begin)
        if may_rng is None:
            return False

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

    def contains_all(self, iterable):
        return all_map(self.__contains__, iterable)
    def iter_ints(self):
        return rngs_to_iter_ints(self.ranges)
    def iter_rngs(self):
        return iter(self.ranges)
    def __hash_args(self):
        return type(self), self.ranges
    def __hash__(self):
        return hash(self.__hash_args())
    def __eq__(self, other):
        r"""
        #match __hash__
        see: set_eq
        #"""
        #assert isinstance(other, (TouchRanges, NonTouchRanges))
        if type(other) is not type(self):
            return NotImplemented
        return self.__hash_args() == other.__hash_args()
    def __repr__(self):
        return '{}({})'.format(type(self).__name__, self.ranges)

    def __bool__(self):
        return len(self.ranges)
    def gaps(self):
        return tuple(self.iter_gaps())
    def iter_gaps(self):
        rngs = self.ranges
        for pre_end, _ in rngs:
            break
        for begin, end in rngs:
            if begin != pre_end:
                yield pre_end, begin
            pre_end = end
    def _rel_op(self, other, op, **kw):
        assert isinstance(other, (TouchRanges, NonTouchRanges))
        return op(self.ranges, other.ranges, rhs_maynot_be_nontouch_ranges=not other.__nontouch, **kw)

    def _op(self, other, op, **kw):
        assert isinstance(other, (TouchRanges, NonTouchRanges))
        ranges = op(self.to_nontouch_ranges(), other.to_nontouch_ranges(), **kw)
        return make_NonTouchRanges(ranges)

    def __lt__(self, other):
        return self._rel_op(other, is_proper_subset_ex_of__xtouch_ranges)
    def __le__(self, other):
        return self._rel_op(other, is_subset_ex_of__xtouch_ranges)
    def set_eq(self, other):
        #vs __eq__
        if self.__nontouch and other.__nontouch:
            return self.ranges == other.ranges
        return self._rel_op(other, is_equal_set_ex_of__xtouch_ranges, lhs_maynot_be_nontouch_ranges=not self.__nontouch)
        ########## old impl ############
        return self._rel_op(other, is_equal_set_ex_of__xtouch_ranges)

    def __or__(self, other):
        return self._op(other, union_ex__xtouch_ranges, faster_output_iter_touch_ranges=False)

    def __and__(self, other):
        return self._op(other, intersection__xtouch_ranges)

    def __sub__(self, other):
        return self._op(other, difference__xtouch_ranges)
    def __xor__(self, other):
        return self._op(other, symmetric_difference_ex__xtouch_ranges, faster_output_iter_touch_ranges=False)


class TouchRanges(Ranges):
    def to_NonTouchRanges(self):
        return make_NonTouchRanges(sorted_rngs_to_iter_nontouch_ranges(self.ranges))
    @classmethod
    def valid_ranges(cls, ranges):
        return valid_touch_ranges(ranges)


class NonTouchRanges(Ranges):
    def to_NonTouchRanges(self):
        return self
    @classmethod
    def valid_ranges(cls, ranges):
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

def test_subset_relation_ex__xtouch_ranges(num_periods=2):
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
    def h(a):
        #iter_xtouch_ranges -> (xtouch_ranges, ks, set<int>
        #ais = rngs_to_iter_ints(a)
        a = make_Ranges(a)
        ks = [True]
        if a.is_nontouch_ranges():
            ks.append(False)
        ais = set(a.iter_ints())
        return a.ranges, ks, ais
    def cmp(lhs, rhs):
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
    def g(a, b):
        #a, b :: iter_xtouch_ranges
        a, aks, ais = h(a)
        b, bks, bis = h(b)
        lr = cmp(ais, bis)
        rr = [0, 2, 1, 3][lr]
        f(lr, a, aks, b, bks)
        f(rr, b, bks, a, aks)
    def ff(set_r, lhs, lk, rhs, rk):
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
    def fff(lhs, lk, rhs, rk):
        return subset_relation_ex__xtouch_ranges(lhs, rhs, lhs_maynot_be_nontouch_ranges=lk, rhs_maynot_be_nontouch_ranges=rk, faster_return_not_le=False, faster_return_not_ge=False)
    def f(set_r, lhs, lks, rhs, rks):
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


def iter_nontouch_rangess_between(begin, end):
    for ls in iter_subsets_of(range(begin, end)):
        if 0:
            rngs = sorted_unique_ints_to_iter_nontouch_ranges(ls)
        else:
            if len(ls)%2:
                ls = (*ls, end)
            rngs = zip(ls[0::2], ls[1::2])
        rngs = tuple(rngs)
        yield rngs



class StackStyleSimpleIntSet:
    r'''
    .rngs :: [(int, int)] #nontouch_ranges
        public-mutable
        NOTE: SHOULD call fix_after_modify_rngs after update rngs externally
    #'''
    def __init__(sf, rngs=None, /):
        if rngs is None:
            rngs = []
        sf.rngs = rngs
    def fix_after_modify_rngs(sf, /, *, turnoff__check_rngs=False, may_delta4size=None):
        rngs = sf.rngs
        if not turnoff__check_rngs:
            sf.check_rngs(rngs)
        if may_delta4size is None:
            sf._sz = sum(j-i for i,j in rngs)
        else:
            delta4size = may_delta4size
            sf._sz += delta4size
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
                raise ValueError('stack_styple-int-set: add(i) but i < end')
            else:
                raise logc-err
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

if __name__ == "__main__":
    print('\n'.join(s for s in globals() if not s.startswith('_')))
    import doctest
    doctest.testmod()
    raise
    test_subset_relation_ex__xtouch_ranges()

