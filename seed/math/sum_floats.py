#__all__:goto
r'''[[[
e ../../python3_src/seed/math/sum_floats.py

seed.math.sum_floats
py -m nn_ns.app.debug_cmd   seed.math.sum_floats -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.sum_floats:__doc__ -ht # -ff -df

[[
always add abs-smallest float number
using heap
]]


>>> sum_floats_([], finite__vs__sorted_by_abs=False)
0
>>> sum_floats_([], finite__vs__sorted_by_abs=True)
0

>>> sum_floats_([-6.5, 1], finite__vs__sorted_by_abs=False)
-5.5
>>> sum_floats_([-6.5, 1], finite__vs__sorted_by_abs=True)
Traceback (most recent call last):
    ...
ValueError

>>> f=lambda j:2.0**j
>>> ls = [f(106), f(53), f(52), f(51), f(51)]
>>> sum(ls).hex()
'0x1.0000000000000p+106'
>>> sum(ls[::-1]).hex()
'0x1.0000000000001p+106'
>>> sum_floats__finite_(ls).hex()
'0x1.0000000000001p+106'

#>>> ls = [f(-51)]*2**16
#>>> sum(ls).hex()
'0x1.0000000000000p-35'
#>>> sum_floats__finite_(ls).hex()
'0x1.0000000000000p-35'

>>> float.fromhex('0x1.0000000000001p-53').hex()
'0x1.0000000000001p-53'

#>>> ls = [float.fromhex('0x1.0000000000001p-53')]*2**16
#>>> sum(ls).hex()
'0x1.0000000000001p-37'
#>>> sum_floats__finite_(ls).hex()
'0x1.0000000000001p-37'


py_adhoc_call   seed.math.sum_floats   @f
]]]'''#'''
__all__ = r'''
sum_floats_
    sum_floats__finite_
    sum_floats__sorted_by_abs_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.iters.ensure_sorted import ensure_sorted
#def ensure_sorted(iterable, /, *, key=None, before=None, reverse=False, to_not=False, on_error=None, with_key=False):
from seed.for_libs.for_heapq import Heap# std____key__le__reverse_
from seed.iters.PeekableIterator import PeekableIterator# echo_or_mk_PeekableIterator

#from itertools import islice
#from seed.tiny_.check import check_type_is, check_int_ge
#from seed.abc.abc__ver1 import abstractmethod, override, ABC
#from seed.helper.repr_input import repr_helper
___end_mark_of_excluded_global_names__0___ = ...


def sum_floats_(floats, /, *, finite__vs__sorted_by_abs):
    sum_ = sum_floats__finite_ if not finite__vs__sorted_by_abs else sum_floats__sorted_by_abs_
    return sum_(floats)
def sum_floats__finite_(floats, /):
    floats = sorted(floats, key=abs)
    return sum_floats__sorted_by_abs_(floats)
def sum_floats__sorted_by_abs_(floats, /):
    floats = ensure_sorted(floats, key=abs)
    floats = PeekableIterator(floats)
    assert iter(floats) is floats
    it = floats

    ls = []
    hp = Heap(ls, item5obj_=None, item2val_=None, key=abs, __le__=None, reverse=False, obj_vs_item=False, applied__heapify=False, set_idx4item_=None)
    s = 0
    while ls or not it.is_empty():
        # 2 sorted streams: (s:hp), it
        #   cmp: (s <= hp[0]) vs (it[0] <= it[1])
        #   ==>> cmp(s,it[1]), cmp(hp[0],it[0])
        #   ==>> add(s, it[0]) | add(s, hp[0]) | add(it[0], it[1])
        t01 = it.peek_le(2)
        match t01:
            case []:
                # => add(s, hp[0])
                case = 0
            case [t0]:
                if ls and ls[0] < t0:
                    # => add(s, hp[0])
                    case = 0
                else:
                    # => add(s, it[0])
                    case = 1
                case
            case [t0, t1]:
                if ls and ls[0] < t0:
                    # => add(s, hp[0])
                    case = 0
                elif s <= t1:
                    # => add(s, it[0])
                    case = 1
                else:
                    # => add(it[0], it[1])
                    case = 2
                case
            case _:
                raise 000
            #######
        #######
        case
        #######
        match case:
            case 0:
                # => add(s, hp[0])
                s += hp.heappop()
                s = hp.heappushpop(s)
            case 1:
                # => add(s, it[0])
                s += next(it)
                s = hp.heappushpop(s)
            case 2:
                # => add(it[0], it[1])
                _s = next(it) + next(it)
                if _s < s:
                    s, _s = _s, s
                # [s <= _s]
                hp.heappush(_s)
            case _:
                raise 000
            #######
        #######
    #end-while ls or not it.is_empty():
    assert not ls
    assert it.is_empty()

    return s

__all__
from seed.math.sum_floats import sum_floats_, sum_floats__finite_, sum_floats__sorted_by_abs_
from seed.math.sum_floats import *
