#__all__:goto
r'''[[[
e ../../python3_src/seed/tiny_/print_iterable_with_lineno_.py
from __doc__@:view ../../python3_src/seed/math/primes__inductive_generated__almost_smooth.py
    'used in doctest'

seed.tiny_.print_iterable_with_lineno_
py -m nn_ns.app.debug_cmd   seed.tiny_.print_iterable_with_lineno_ -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.tiny_.print_iterable_with_lineno_:__doc__ -ht # -ff -df

>>> print_iterable_with_lineno_(2, 'abcd')
0:'a'
1:'b'
>>> print_iterable_with_lineno_(2, 'abcd', offset=1)
1:'a'
2:'b'
>>> print_iterable_with_lineno_(2, 'abcd', to_str=str)
0:a
1:b

>>> print_iterable_(2, 'abcd')
'a'
'b'
>>> print_iterable_(2, 'abcd', to_str=str)
a
b
>>> print_iterable_(2, 'abcd', to_str=str, may_min_lineno=3)
3:a
4:b

>>> print_iterableT(2)('abcd')
'a'
'b'
>>> print_iterableT(2, to_str=str)('abcd')
a
b
>>> print_iterableT(2, to_str=str, may_min_lineno=3)('abcd')
3:a
4:b

>>> print_iterable_with_linenoT(2)('abcd')
0:'a'
1:'b'
>>> print_iterable_with_linenoT(2, to_str=str)('abcd')
0:a
1:b
>>> print_iterable_with_linenoT(2, offset=1, to_str=str)('abcd')
1:a
2:b









py_adhoc_call   seed.tiny_.print_iterable_with_lineno_   @f
]]]'''#'''
__all__ = r'''
print_iterable_with_lineno_
print_iterable_

print_iterable_with_linenoT
print_iterableT
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from itertools import islice
from functools import partial
___end_mark_of_excluded_global_names__0___ = ...

def print_iterableT(max_sz, /, *, to_str=repr, may_min_lineno=None):
    return partial(print_iterable_, max_sz, to_str=to_str, may_min_lineno=may_min_lineno)

def print_iterable_with_linenoT(max_sz, /, *, offset=0, to_str=repr):
    return partial(print_iterable_with_lineno_, max_sz, offset=offset, to_str=to_str)

def print_iterable_with_lineno_(max_sz, xs, /, *, offset=0, to_str=repr):
    'used in doctest'
    xs = islice(xs, max_sz)
    xs = map(to_str, xs)
    for i, x in enumerate(xs, offset):
        #print(f'{i}:{x!s}')
        print(i, x, sep=':')

def print_iterable_(max_sz, xs, /, *, to_str=repr, may_min_lineno=None):
    'used in doctest'
    #######
    if not may_min_lineno is None:
        min_lineno = may_min_lineno
        return print_iterable_with_lineno_(max_sz, xs, offset=min_lineno, to_str=to_str)
    #######
    xs = islice(xs, max_sz)
    xs = map(to_str, xs)
    _s = map(print, xs)
    for _ in _s:pass



__all__
from seed.tiny_.print_iterable_with_lineno_ import print_iterable_with_lineno_, print_iterable_
from seed.tiny_.print_iterable_with_lineno_ import print_iterable_with_linenoT, print_iterableT


from seed.tiny_.print_iterable_with_lineno_ import print_iterable_with_lineno_, print_iterable_, print_iterable_with_linenoT, print_iterableT
    #def print_iterable_with_lineno_(max_sz, xs, /, *, offset=0, to_str=repr):
    #def print_iterable_(max_sz, xs, /, *, to_str=repr, may_min_lineno=None):
    #def print_iterable_with_linenoT(max_sz, /, *, offset=0, to_str=repr):
    #def print_iterableT(max_sz, /, *, to_str=repr, may_min_lineno=None):

from seed.tiny_.print_iterable_with_lineno_ import *
