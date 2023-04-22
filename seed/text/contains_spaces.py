#__all__:goto
r'''[[[
e ../../python3_src/seed/text/contains_spaces.py
[[
why?
had found bug like this:
    if not len(all_chars.split()) <= 1: raise ValueError('contain spaces')
]]



seed.text.contains_spaces
py -m nn_ns.app.debug_cmd   seed.text.contains_spaces -x
py -m nn_ns.app.doctest_cmd seed.text.contains_spaces:__doc__ -ff -v
py_adhoc_call   seed.text.contains_spaces   @f

>>> from seed.text.contains_spaces import contains_spaces, check_contains_no_spaces
>>> contains_spaces('')
False
>>> contains_spaces('0')
False
>>> contains_spaces('\n')
True
>>> contains_spaces('a x')
True
>>> check_contains_no_spaces('')
>>> check_contains_no_spaces('0')
>>> check_contains_no_spaces('\n')
Traceback (most recent call last):
    ...
ValueError: contains spaces
>>> check_contains_no_spaces('a x')
Traceback (most recent call last):
    ...
ValueError: contains spaces




#]]]'''
__all__ = r'''
    contains_spaces
    check_contains_no_spaces
'''.split()#'''
__all__

from seed.text.useful_regex_patterns import space__regex
from seed.tiny import check_type_is

def contains_spaces(s, /):
    check_type_is(str, s)
    return bool(space__regex.search(s))
def check_contains_no_spaces(s, /):
    if contains_spaces(s): raise ValueError('contains spaces')


from seed.text.contains_spaces import contains_spaces, check_contains_no_spaces
from seed.text.contains_spaces import *
