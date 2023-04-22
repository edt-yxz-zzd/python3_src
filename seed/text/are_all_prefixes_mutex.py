#__all__:goto
r'''[[[
e ../../python3_src/seed/text/are_all_prefixes_mutex.py


seed.text.are_all_prefixes_mutex
py -m nn_ns.app.debug_cmd   seed.text.are_all_prefixes_mutex -x
py -m nn_ns.app.doctest_cmd seed.text.are_all_prefixes_mutex:__doc__ -ff -v
py -m nn_ns.app.doctest_cmd seed.text.are_all_prefixes_mutex!
py_adhoc_call   seed.text.are_all_prefixes_mutex   @f


>>> from seed.text.are_all_prefixes_mutex import find_may_non_mutex_prefix_pair_, are_all_prefixes_mutex, check_all_prefixes_mutex
>>> are_all_prefixes_mutex([])
True
>>> are_all_prefixes_mutex(['123'])
True
>>> are_all_prefixes_mutex(['123', '124'])
True
>>> are_all_prefixes_mutex(['123', '123'])
False
>>> are_all_prefixes_mutex(['123', '1234'])
False
>>> are_all_prefixes_mutex(['123', '12'])
False



>>> check_all_prefixes_mutex(['123', '124'])
>>> check_all_prefixes_mutex(['123', '123'])
Traceback (most recent call last):
    ...
ValueError: prefixes are not mutual exclusive: '123' vs '123'
>>> check_all_prefixes_mutex(['123', '12'])
Traceback (most recent call last):
    ...
ValueError: prefixes are not mutual exclusive: '12' vs '123'
>>> check_all_prefixes_mutex(['123', '123'], is_sorted=True)
Traceback (most recent call last):
    ...
ValueError: prefixes are not mutual exclusive: '123' vs '123'
>>> check_all_prefixes_mutex(['123', '12'], is_sorted=True)
Traceback (most recent call last):
    ...
TypeError: not sorted yet: '123' vs '12'



#]]]'''
__all__ = r'''
    find_may_non_mutex_prefix_pair_
    are_all_prefixes_mutex
    check_all_prefixes_mutex
'''.split()#'''
__all__

from itertools import pairwise
from seed.tiny import check_type_is

if 1:
    is_sorted=False
def find_may_non_mutex_prefix_pair_(prefixes, /, *, is_sorted=is_sorted):
    'Iter str -> may (a/str,b/str) where [a == b[:len(a)]]'
    check_type_is(bool, is_sorted)
    if not is_sorted:
        prefixes = sorted(prefixes)
    prefixes = iter(prefixes)
    for a, b in pairwise(prefixes):
        if not a <= b: raise TypeError(f'not sorted yet: {a!r} vs {b!r}')
        #if len(a) <= len(b) and a == b[:len(a)]:
        if b.startswith(a):
            return (a, b)
    return None
def are_all_prefixes_mutex(prefixes, /, *, is_sorted=is_sorted):
    return not find_may_non_mutex_prefix_pair_(prefixes, is_sorted=is_sorted)

def check_all_prefixes_mutex(prefixes, /, *, is_sorted=is_sorted):
    m = find_may_non_mutex_prefix_pair_(prefixes, is_sorted=is_sorted)
    if not m is None:
        a,b = m
        assert b.startswith(a)
        raise ValueError(f'prefixes are not mutual exclusive: {a!r} vs {b!r}')
if 1:
    del is_sorted


from seed.text.are_all_prefixes_mutex import find_may_non_mutex_prefix_pair_, are_all_prefixes_mutex, check_all_prefixes_mutex
from seed.text.are_all_prefixes_mutex import *
