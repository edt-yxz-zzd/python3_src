#__all__:goto
r'''[[[
e ../../python3_src/seed/int_tools/digits/uintZSbase32.py

seed.int_tools.digits.uintZSbase32
py -m nn_ns.app.debug_cmd   seed.int_tools.digits.uintZSbase32 -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.int_tools.digits.uintZSbase32:__doc__ -ht # -ff -df

[[
]]

>>> [*map(uintZbase32_, range(40))]
['', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', '10', '11', '12', '13', '14', '15', '16', '17']
>>> [*map(uintSbase32_, _)] == [*range(40)]
True


py_adhoc_call   seed.int_tools.digits.uintZSbase32   @f
]]]'''#'''
__all__ = r'''
uintZbase32_
uintSbase32_
base32_alplabet
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#from seed.int_tools.digits.uint25radix_repr import uint2radix_repr_, uint5radix_repr_
from base64 import b32hexencode, b32hexdecode
from seed.text.join_between import join_between
from seed.tiny_.check import check_type_is, check_int_ge
#.from itertools import islice
#.
___end_mark_of_excluded_global_names__0___ = ...

_tbl4b32hex = join_between(*'09') +join_between(*'AV')
    #base64._b32hexalphabet::bytes
#assert _tbl4b32hex == base64._b32hexalphabet
base32_alplabet = _tbl4b32hex
def uintZbase32_(u, /):
    check_int_ge(0, u)
    #iter_digits = uint2radix_repr_(32, u, is_big_endian=True)
    if u == 0:
        return ''
    L = u.bit_length()
    sz1 = (L+39)//40*5
    bs1 = u.to_bytes(sz1, 'big')
    # [bs1 :: raw-bytes]
    bs2 = b32hexencode(bs1)
    # [bs2 :: b32-bytes]
    sz2 = len(bs2)
    sz3 = (L+4)//5
    assert sz3
        # !! [u > 0]
    osz = sz2 -sz3
    #assert not any(bs2[:osz])
    #assert bs2[osz]
    assert bs2[:osz] == b'0'*osz
    assert not bs2[osz] == b'0'
        # !! [sz3 > 0]
    bs3 = bs2[osz:]
    s = bs3.decode('ascii')
    return s
def uintSbase32_(s, /):
    bs3 = s.encode('ascii')
    sz3 = len(bs3)
    sz2 = (sz3+7)//8*8
    osz = sz2 -sz3
    #bs2 = b'\0'*osz + bs3
    bs2 = b'0'*osz + bs3
    # [bs2 :: b32-bytes]
    bs1 = b32hexdecode(bs2)
    # [bs1 :: raw-bytes]
    u = int.from_bytes(bs1, 'big')
    return u



__all__
from seed.int_tools.digits.uintZSbase32 import uintZbase32_, uintSbase32_, base32_alplabet
from seed.int_tools.digits.uintZSbase32 import *
