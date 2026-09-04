#__all__:goto
r'''[[[
e ../../python3_src/seed/tiny_/count_.py

seed.tiny_.count_
py -m nn_ns.app.debug_cmd   seed.tiny_.count_ -x
py -m nn_ns.app.doctest_cmd seed.tiny_.count_:__doc__ -ht
py_adhoc_call   seed.tiny_.count_   @f

>>> from itertools import islice



#>>> [*count_(9, 30, 5)]
#>>> [*count_(9, 30, -5)]
#>>> count_(9, 30, 0)
#>>> [*count_(9, -30, 5)]
#>>> [*count_(9, -30, -5)]
#>>> count_(9, -30, 0)
#>>> [*islice(count_(9, None, 3), 7)]
#>>> [*islice(count_(9, None, -3), 7)]
#>>> [*islice(count_(9, None, 0), 7)]



>>> [*count_(9, 30, 5)]
[9, 14, 19, 24, 29]

>>> [*count_(9, 30, -5)]
[]

>>> count_(9, 30, 0)
Traceback (most recent call last):
    ...
ValueError: range() arg 3 must not be zero

>>> [*count_(9, -30, 5)]
[]

>>> [*count_(9, -30, -5)]
[9, 4, -1, -6, -11, -16, -21, -26]

>>> count_(9, -30, 0)
Traceback (most recent call last):
    ...
ValueError: range() arg 3 must not be zero

>>> [*islice(count_(9, None, 3), 7)]
[9, 12, 15, 18, 21, 24, 27]

>>> [*islice(count_(9, None, -3), 7)]
[9, 6, 3, 0, -3, -6, -9]

>>> [*islice(count_(9, None, 0), 7)]
[9, 9, 9, 9, 9, 9, 9]














iter_ints__ge_lt_
>>> [*iter_ints__ge_lt_(2, 8)]
[2, 3, 4, 5, 6, 7]
>>> [*iter_ints__ge_lt_(2, 8, step=3)]
[2, 5]
>>> [*iter_ints__ge_lt_(2, 8, step=3, reverse=True)]
[7, 4]
>>> [*iter_ints__ge_lt_(2, 8, reverse=True)]
[7, 6, 5, 4, 3, 2]
>>> [*islice(iter_ints__ge_lt_(2, None), 0, 3)]
[2, 3, 4]
>>> [*islice(iter_ints__ge_lt_(None, 8, reverse=True), 0, 3)]
[7, 6, 5]
>>> [*islice(iter_ints__ge_lt_(2, None, step=3), 0, 3)]
[2, 5, 8]
>>> [*islice(iter_ints__ge_lt_(None, 8, step=3, reverse=True), 0, 4)]
[7, 4, 1, -2]










>>> [*iter_ints__from_to_(2, 8, +3)]
[2, 5]
>>> [*iter_ints__from_to_(2, 8, +3, reverse=True)]
[5, 2]
>>> [*iter_ints__from_to_(2, 8, -3)]
[]
>>> [*iter_ints__from_to_(2, 8, -3, reverse=True)]
[]
>>> [*iter_ints__from_to_(8, 2, +3)]
[]
>>> [*iter_ints__from_to_(8, 2, +3, reverse=True)]
[]
>>> [*iter_ints__from_to_(8, 2, -3)]
[8, 5]
>>> [*iter_ints__from_to_(8, 2, -3, reverse=True)]
[5, 8]

>>> [*islice(iter_ints__from_to_(2, None, +3), 0, 3)]
[2, 5, 8]
>>> [*islice(iter_ints__from_to_(2, None, -3), 0, 3)]
[2, -1, -4]

>>> [*islice(iter_ints__from_to_(2, None, -3, reverse=True), 0, 3)]
Traceback (most recent call last):
    ...
TypeError: [reverse:=True][may_end:=None]
>>> [*islice(iter_ints__from_to_(2, None, +3, reverse=True), 0, 3)]
Traceback (most recent call last):
    ...
TypeError: [reverse:=True][may_end:=None]




















#]]]'''
__all__ = r'''
count_
iter_ints__from_to_
iter_ints__ge_lt_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from itertools import count, repeat
    #repeat(object [,times])
    #count(start=0, step=1)
from seed.tiny_.check import check_type_is, check_int_ge, check_may_
___end_mark_of_excluded_global_names__0___ = ...

def count_(start=0, may_stop=None, /, step=1):
    'count_(start=0, may_stop=None, /, step=1):diff:itertools.count(start=0, step=1)'
    check_type_is(int, start)
    if not None is may_stop:
        stop = may_stop
        check_type_is(int, stop)
    check_type_is(int, step)

    if not None is may_stop:
        return iter(range(start, stop, step))
        #if step == 0 and not None is may_stop: raise ValueError
    # [stop == +-oo]
    if step == 0:
        return iter(repeat(start))
    return iter(count(start, step))


def iter_ints__from_to_(begin, may_end=None, /, step=1, *, reverse=False):
    '#vs:count_():this_func ++kw:reverse and forbids [step==0]  #vs:iter_ints__ge_lt_():this_func.begin never changed'
    check_type_is(int, step)
    check_type_is(int, begin)
    check_may_([check_type_is, int], may_end)
    if step == 0:raise ValueError('[step:=0]')
    if reverse and may_end is None: raise TypeError('[reverse:=True][may_end:=None]')
    match (reverse, begin, may_end):
        case (False, begin, None):
            us = count(begin, step)
        case (False, begin, end):
            us = range(begin, end, step)
        case (True, begin, None):
            if reverse and may_end is None: raise TypeError('[reverse:=True][may_end:=None]')
            raise 000
        case (True, begin, end):
            us = range(begin, end, step)[::-1]
        case _:
            raise 000
    us
    return iter(us)
def iter_ints__ge_lt_(may_min_u, may_max1_u, /, *, step=1, reverse=False):
    '-> Iter int # NOTE:[[reverse:=True] => [begin:=-1+max1_u]]'
    check_may_([check_type_is, int], may_min_u)
    check_may_([check_type_is, int], may_max1_u)
    check_int_ge(1, step)

    if not reverse and may_min_u is None: raise TypeError('[reverse:=False][may_min_u:=None]')
    if reverse and may_max1_u is None: raise TypeError('[reverse:=True][may_max1_u:=None]')
    match (reverse, may_min_u, may_max1_u):
        #case (_, None, None): raise 000
        case (False, min_u, None):
            ws = count(min_u, +step)
        case (True, None, max1_u):
            ws = count(-1+max1_u, -step)
        #.case (_, min_u, max1_u):
        #.    ws = range(min_u, max1_u, +step)
        #.    if reverse:
        #.        ws = reversed(ws)
        #.    else:
        #.        ws = iter(ws)
        #.    ws
        case (False, min_u, max1_u):
            ws = range(min_u, max1_u, +step)
        case (True, min_u, max1_u):
            # !! ++kw:step
            # for [step > 1]:
            ws = range(-1+max1_u, -1+min_u, -step)
    ws
    return iter(ws)



__all__
from seed.tiny_.count_ import count_, iter_ints__from_to_, iter_ints__ge_lt_
from seed.tiny_.count_ import *
