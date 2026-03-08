#__all__:goto
r'''[[[
e ../../python3_src/seed/text/base64_base16.py

seed.text.base64_base16
py -m nn_ns.app.debug_cmd   seed.text.base64_base16 -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.text.base64_base16:__doc__ -ht # -ff -df
#######

[[

>>> uint2base64_(-1)
Traceback (most recent call last):
    ...
AssertionError
>>> uint2base64_(0)
''
>>> uint2base64_(1)
'B'
>>> uint2base64_(2)
'C'
>>> uint2base64_(61)
'9'
>>> uint2base64_(62)
'_'
>>> uint2base64_(63)
'.'
>>> uint2base64_(64)
'BA'
>>> uint5base64_('')
0
>>> uint5base64_('B')
1
>>> uint5base64_('C')
2
>>> uint5base64_('9')
61
>>> uint5base64_('_')
62
>>> uint5base64_('.')
63
>>> uint5base64_('BA')
64



]]
[[
>>> uint2hex_(-1)
Traceback (most recent call last):
    ...
AssertionError
>>> uint2hex_(0)
'0'
>>> uint2hex_(1)
'1'
>>> uint2hex_(15)
'F'
>>> uint2hex_(16)
'10'
>>> uint5hex_('')
Traceback (most recent call last):
    ...
ValueError: invalid literal for int() with base 16: ''
>>> uint5hex_('0')
0
>>> uint5hex_('1')
1
>>> uint5hex_('F')
15
>>> uint5hex_('10')
16


]]



'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.text.base64_base16   @f
]]]'''#'''
__all__ = r'''
uint2base64_
uint5base64_
uint2hex_
uint5hex_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__, 'uint__to__radix64_digits__b64__str_:_encode64_, uint__from__radix64_digits__b64__str_:_decode64_'):
    #.from itertools import islice
    #.from seed.tiny_.check import check_type_is, check_int_ge
    from seed.text.base64 import uint__to__radix64_digits__b64__str_ as _encode64_, uint__from__radix64_digits__b64__str_ as _decode64_
        #def uint__to__radix64_digits__b64__str_(u, /, *, b64_cfg_case, bigendian):
        #def uint__from__radix64_digits__b64__str_(s, /, *, b64_cfg_case, bigendian):
#.#################################
___end_mark_of_excluded_global_names__0___ = ...


#def int2hex_(i, /): return f'{i:X}'
def uint5hex_(s, /):
    u = int(s, 16)
        # ^ValueError: invalid literal for int() with base 16: ''
    assert u >= 0
    return u
def uint2hex_(u, /):
    assert u >= 0
    return f'{u:X}'
def uint2base64_(u, /):
    assert u >= 0
    return _encode64_(u, b64_cfg_case=b'_.', bigendian=True)
def uint5base64_(s, /):
    return _decode64_(s, b64_cfg_case=b'_.', bigendian=True)



__all__
from seed.text.base64_base16 import uint2base64_, uint5base64_, uint2hex_, uint5hex_
from seed.text.base64_base16 import *
