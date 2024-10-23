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


#]]]'''
__all__ = r'''
count_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from itertools import count as _count, repeat as _repeat
    #repeat(object [,times])
    #count(start=0, step=1)
from seed.tiny_.check import check_type_is, check_int_ge
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
        return iter(_repeat(start))
    return iter(_count(start, step))



__all__
from seed.tiny_.count_ import count_
from seed.tiny_.count_ import *
