#__all__:goto
r'''[[[
e ../../python3_src/seed/iters/differential.py

seed.iters.differential
py -m nn_ns.app.debug_cmd   seed.iters.differential -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.iters.differential:__doc__ -ht # -ff -df
#######

[[
differential vs accumulate
itertools.accumulate(iterable, func=None, *, initial=None)

come_from:
view ../../python3_src/seed/math/prime_pint/num_primes_le.py
TODO:oeis:平方数之间的素数数量
]]


'#'; __doc__ = r'#'
>>> from itertools import accumulate

>>> [*accumulate(range(4))]
[0, 1, 3, 6]
>>> [*differential(range(4))]
[0, 1, 1, 1]
>>> [*accumulate(range(4), initial=1000)]
[1000, 1000, 1001, 1003, 1006]
>>> [*differential(range(4), tmay_initial=[1000])]
[1000, -1000, 1, 1, 1]
>>> [*accumulate(range(1,5), operator.__mul__)]
[1, 2, 6, 24]
>>> [*differential(range(1,5), operator.__mul__)]
[1, 2, 6, 12]



py_adhoc_call  { +lineno }  seed.iters.differential   ,differential %%:P  ='P.seed.math.prime_pint.num_primes_le().num_primes_le__via_list_primes_le__batch_((n**2 for n in range(1,1+200)))'
py_adhoc_call  seed.iters.differential   @list.differential %%:P  ='P.seed.math.prime_pint.num_primes_le().num_primes_le__via_list_primes_le__batch_((n**2 for n in range(1,1+200)))'

py_adhoc_call  seed.iters.differential   @list.differential %%:P  ='P.seed.iters.differential().differential(P.seed.math.prime_pint.num_primes_le().num_primes_le__via_list_primes_le__batch_((n**2 for n in range(1,1+200))))'

py_adhoc_call   seed.iters.differential   @f
]]]'''#'''
__all__ = r'''
differential
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
import operator
operator.__sub__
___end_mark_of_excluded_global_names__0___ = ...

def differential(xs, __sub__=None, /, *, tmay_initial=()):
    xs = iter(xs)

    if __sub__ is None:
        __sub__ = operator.__sub__

    if tmay_initial:
        [x] = tmay_initial
    else:
        for x in xs:
            break
        else:
            return
        x
    yield x
    for y in xs:
        #yield y - x
        yield __sub__(y, x)
        x = y


__all__
from seed.iters.differential import differential
from seed.iters.differential import *
