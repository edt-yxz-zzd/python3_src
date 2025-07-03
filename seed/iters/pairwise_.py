#__all__:goto
r'''[[[
e ../../python3_src/seed/iters/pairwise_.py

seed.iters.pairwise_
py -m nn_ns.app.debug_cmd   seed.iters.pairwise_ -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.iters.pairwise_:__doc__ -ht # -ff -df

[[
from itertools import pairwise
    pairwise() miss 1 element
    pairwise() miss one-element container
from seed.iters.pairwise_ import pairwise_
]]



>>> def f(it, /):
...     assert iter(it) is it
...     return list(it)
>>> f(pairwise_(1))
[]
>>> f(pairwise_(1, [2,3]))
[(1, 2), (2, 3)]
>>> f(pairwise_(1, [2,3], [4]))
[(1, 2), (2, 3), (3, 4)]
>>> f(pairwise__head_(1, []))
[]
>>> f(pairwise__head_(1, [2]))
[(1, 2)]
>>> f(pairwise__tail_(9, []))
[]
>>> f(pairwise__tail_(9, [1]))
[(1, 9)]
>>> f(pairwise_chain_())
[]
>>> f(pairwise_chain_([]))
[]
>>> f(pairwise_chain_([1]))
[]
>>> f(pairwise_chain_([1,2]))
[(1, 2)]
>>> f(pairwise_chain_([1,2], [3]))
[(1, 2), (2, 3)]
>>> f(pairwise_chain_([1,2], [3], [4,5]))
[(1, 2), (2, 3), (3, 4), (4, 5)]
>>> f(pairwise_chains_([]))
[]
>>> f(pairwise_chains_([[]]))
[]
>>> f(pairwise_chains_([[1]]))
[]
>>> f(pairwise_chains_([[1,2]]))
[(1, 2)]
>>> f(pairwise_chains_([[1,2], [3]]))
[(1, 2), (2, 3)]
>>> f(pairwise_chains_([[1,2], [3], [4,5]]))
[(1, 2), (2, 3), (3, 4), (4, 5)]


py_adhoc_call   seed.iters.pairwise_   @f
]]]'''#'''
__all__ = r'''
pairwise_chains_
    pairwise_chain_
        pairwise__tail_
        pairwise__head_
            pairwise_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from itertools import pairwise, chain
chains = chain.from_iterable
___end_mark_of_excluded_global_names__0___ = ...


def pairwise_(x0, /, *xss):
    xs = chains(xss)
    return pairwise__head_(x0, xs)
    return pairwise_chain_([x0], *xss)
def pairwise__head_(x0, xs, /):
    return pairwise_chain_([x0], xs)
def pairwise__tail_(xt, xs, /):
    return pairwise_chain_(xs, [xt])
def pairwise_chain_(*xss):
    return pairwise_chains_(xss)
def pairwise_chains_(xss, /):
    xs = chains(xss)
    return pairwise(xs)

__all__
from seed.iters.pairwise_ import pairwise_
from seed.iters.pairwise_ import pairwise__head_
from seed.iters.pairwise_ import pairwise_chain_
from seed.iters.pairwise_ import pairwise_, pairwise__head_, pairwise__tail_, pairwise_chain_, pairwise_chains_
from seed.iters.pairwise_ import *
