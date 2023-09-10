#__all__:goto
r'''[[[
e ../../python3_src/seed/math/binary_float/py_float_repr.py
view ../../python3_src/seed/math/binary_float/binary_float_ops____using_LazyList.py


seed.math.binary_float.py_float_repr
py -m nn_ns.app.debug_cmd   seed.math.binary_float.py_float_repr -x
py -m nn_ns.app.doctest_cmd seed.math.binary_float.py_float_repr:__doc__ -ff -v
py_adhoc_call   seed.math.binary_float.py_float_repr   @f
from seed.math.binary_float.py_float_repr import *


hex_mantissa :: str
    = regex'0|[0-9a-f]*[1-9a-f]'
bin_mantissa :: str
    = regex'0|[01]*1'

exp4msb :: str
    = regex'[+]0|[+-][1-9][0-9]*'
hex_float_repr :: str
    = regex'-?0x0.0p+0|-?0x1.{hex_mantissa}p{exp4msb}'
bin_float_repr :: str
    = regex'-?0b0.0p+0|-?0b1.{bin_mantissa}p{exp4msb}'

signed_uint_exp_repr :: ((-1|+1), uint, int)
    signed_uint_exp_repr :: (sign, uint8bits, exp4msb)
    #[sign =!= 0]{no 0, since -0.0 +0.0}
    [[uint8bits==0] -> [exp4msb==0]]
    [[uint8bits=!=0] --> [uint8bits&1 == 1]]
    [abs(float) === 0.0 if uint8bits==0 else uint8bits * 2**(exp4msb-floor_log2_(uint8bits))]

pint8bits :: pint / int{>0}
    # <-- signed_uint_exp_repr.uint8bits where not 0
    [pint8bits&1 == 1]



transform center:
    signed_uint_exp_repr
    pint8bits

signed_uint_exp_repr
    --> bin_float_repr
    <-- bin_float_repr
    --> hex_float_repr
    <-- hex_float_repr
    <-- float
    #xxx no --> float

pint8bits
    --> bin_mantissa
    <-- bin_mantissa
    --> hex_mantissa
    <-- hex_mantissa





_greek_exp4msb__pattern
_greek_hex_mantissa__pattern
_greek_bin_mantissa__pattern






>>> float.fromhex('0x1.77777777777777777777777').hex()
'0x1.7777777777777p+0'
>>> float.fromhex('-0x1.aaaaaaaaaaaaaaaaaaaaaa').hex()
'-0x1.aaaaaaaaaaaabp+0'
>>> float.fromhex('-0x0.aaaaaaaaaaaaaaaaaaaaaa').hex()
'-0x1.5555555555555p-1'
>>> float.fromhex('-0').hex()
'-0x0.0p+0'
>>> float.fromhex('0').hex()
'0x0.0p+0'
>>> 0. .hex()
'0x0.0p+0'
>>>
>>> float('inf').hex()
'inf'
>>> float('nan').hex()
'nan'
>>> float('-nan').hex()
'nan'
>>> float('-inf').hex()
'-inf'


>>> float.fromhex('0x1p-1021').hex()
'0x1.0000000000000p-1021'
>>> float.fromhex('0x1p-1022').hex()
'0x1.0000000000000p-1022'
>>> float.fromhex('0x1p-1023').hex()
'0x0.8000000000000p-1022'
>>> float.fromhex('0x1p-1024').hex()
'0x0.4000000000000p-1022'
>>> float.fromhex('0x1p-1073').hex()
'0x0.0000000000002p-1022'
>>> float.fromhex('0x1p-1074').hex()
'0x0.0000000000001p-1022'
>>> float.fromhex('0x1p-1075').hex()
'0x0.0p+0'



>>> float.fromhex('0x1p+1024').hex()
Traceback (most recent call last):
    ...
OverflowError: hexadecimal value too large to represent as a float
>>> float.fromhex('-0x1p+1024').hex()
Traceback (most recent call last):
    ...
OverflowError: hexadecimal value too large to represent as a float
>>> float.fromhex('0x1p+1023').hex()
'0x1.0000000000000p+1023'
>>> float.fromhex('-0x1p+1023').hex()
'-0x1.0000000000000p+1023'
>>> float.fromhex('0x1p-1074').hex()
'0x0.0000000000001p-1022'
>>> float.fromhex('0x1p-1075').hex()
'0x0.0p+0'
>>> float.fromhex('-0x1p-1074').hex()
'-0x0.0000000000001p-1022'
>>> float.fromhex('-0x1p-1075').hex()
'-0x0.0p+0'


[exp4msb <- [-1074..=+1023]]

>>> float.fromhex('0x1p-1024').as_integer_ratio() == (1, 1<<1024)
True



    hex_mantissa5bin_
    hex_mantissa2bin_

>>> hex_mantissa5bin_('0')
'0'
>>> hex_mantissa5bin_('1')
'8'
>>> hex_mantissa5bin_('01')
'4'
>>> hex_mantissa5bin_('11')
'c'
>>> hex_mantissa5bin_('011')
'6'
>>> hex_mantissa5bin_('101')
'a'
>>> hex_mantissa5bin_('001')
'2'
>>> hex_mantissa5bin_('0001')
'1'
>>> hex_mantissa5bin_('00001')
'08'
>>> hex_mantissa5bin_('00101')
'28'

>>> hex_mantissa2bin_('0')
'0'
>>> hex_mantissa2bin_('1')
'0001'
>>> hex_mantissa2bin_('2')
'001'
>>> hex_mantissa2bin_('4')
'01'
>>> hex_mantissa2bin_('8')
'1'
>>> hex_mantissa2bin_('08')
'00001'
>>> hex_mantissa2bin_('04')
'000001'
>>> hex_mantissa2bin_('02')
'0000001'
>>> hex_mantissa2bin_('01')
'00000001'
>>> hex_mantissa2bin_('21')
'00100001'


    float2hex_float_repr_
        float2bin_float_repr_
        float2signed_uint_exp_repr_

>>> float2hex_float_repr_(0.)
'0x0.0p+0'
>>> float2hex_float_repr_(-0.)
'-0x0.0p+0'
>>> float2hex_float_repr_(-1.)
'-0x1.0p+0'
>>> float2hex_float_repr_(-1.25)
'-0x1.4p+0'
>>> float2hex_float_repr_(0.25)
'0x1.0p-2'

>>> float2bin_float_repr_(0.)
'0b0.0p+0'
>>> float2bin_float_repr_(-0.)
'-0b0.0p+0'
>>> float2bin_float_repr_(-1.)
'-0b1.0p+0'
>>> float2bin_float_repr_(-1.25)
'-0b1.01p+0'
>>> float2bin_float_repr_(0.25)
'0b1.0p-2'

>>> float2signed_uint_exp_repr_(0.)
(1, 0, 0)
>>> float2signed_uint_exp_repr_(-0.)
(-1, 0, 0)
>>> float2signed_uint_exp_repr_(-1.)
(-1, 1, 0)
>>> float2signed_uint_exp_repr_(-1.25)
(-1, 5, 0)
>>> float2signed_uint_exp_repr_(0.25)
(1, 1, -2)




        hex_float_repr2bin_
        hex_float_repr5bin_

>>> hex_float_repr5bin_('0b0.0p+0')
'0x0.0p+0'
>>> hex_float_repr5bin_('-0b0.0p+0')
'-0x0.0p+0'
>>> hex_float_repr5bin_('0b1.0p+999')
'0x1.0p+999'
>>> hex_float_repr5bin_('-0b1.0p-999')
'-0x1.0p-999'
>>> hex_float_repr5bin_('0b1.01p+999')
'0x1.4p+999'
>>> hex_float_repr5bin_('-0b1.01p-999')
'-0x1.4p-999'


>>> hex_float_repr2bin_('0x0.0p+0')
'0b0.0p+0'
>>> hex_float_repr2bin_('-0x0.0p+0')
'-0b0.0p+0'
>>> hex_float_repr2bin_('0x1.0p+999')
'0b1.0p+999'
>>> hex_float_repr2bin_('-0x1.0p-999')
'-0b1.0p-999'
>>> hex_float_repr2bin_('0x1.4p+999')
'0b1.01p+999'
>>> hex_float_repr2bin_('-0x1.4p-999')
'-0b1.01p-999'


>>> hex_float_repr5bin_('0b0.0p-0') # '0x0.0p+0'
Traceback (most recent call last):
    ...
seed.math.binary_float.py_float_repr.FloatNumberError__repr_format: 0b0.0p-0
>>> hex_float_repr5bin_('-0b0.0p-0') # '-0x0.0p+0'
Traceback (most recent call last):
    ...
seed.math.binary_float.py_float_repr.FloatNumberError__repr_format: -0b0.0p-0

>>> hex_float_repr2bin_('0x0.0p-0') # '0b0.0p+0'
Traceback (most recent call last):
    ...
seed.math.binary_float.py_float_repr.FloatNumberError__repr_format: 0x0.0p-0
>>> hex_float_repr2bin_('-0x0.0p-0') # '-0b0.0p+0'
Traceback (most recent call last):
    ...
seed.math.binary_float.py_float_repr.FloatNumberError__repr_format: -0x0.0p-0

>>> hex_float_repr5bin_('0b1.0p-0') # '0x1.0p+0'
Traceback (most recent call last):
    ...
seed.math.binary_float.py_float_repr.FloatNumberError__repr_format: 0b1.0p-0
>>> hex_float_repr5bin_('-0b1.0p-0') # '-0x1.0p+0'
Traceback (most recent call last):
    ...
seed.math.binary_float.py_float_repr.FloatNumberError__repr_format: -0b1.0p-0

>>> hex_float_repr2bin_('0x1.0p-0') # '0b1.0p+0'
Traceback (most recent call last):
    ...
seed.math.binary_float.py_float_repr.FloatNumberError__repr_format: 0x1.0p-0
>>> hex_float_repr2bin_('-0x1.0p-0') # '-0b1.0p+0'
Traceback (most recent call last):
    ...
seed.math.binary_float.py_float_repr.FloatNumberError__repr_format: -0x1.0p-0


>>> hex_float_repr5bin_('0b0.0p+1')
Traceback (most recent call last):
    ...
seed.math.binary_float.py_float_repr.FloatNumberError__repr_format: 0b0.0p+1
>>> hex_float_repr5bin_('0b1.0p+01')
Traceback (most recent call last):
    ...
seed.math.binary_float.py_float_repr.FloatNumberError__repr_format: 0b1.0p+01
>>> hex_float_repr5bin_('0b0.0p-1')
Traceback (most recent call last):
    ...
seed.math.binary_float.py_float_repr.FloatNumberError__repr_format: 0b0.0p-1
>>> hex_float_repr5bin_('0b1.0p-01')
Traceback (most recent call last):
    ...
seed.math.binary_float.py_float_repr.FloatNumberError__repr_format: 0b1.0p-01

>>> hex_float_repr5bin_('0b0.00p+0')
Traceback (most recent call last):
    ...
seed.math.binary_float.py_float_repr.FloatNumberError__repr_format: 0b0.00p+0
>>> hex_float_repr5bin_('0b1.00p+0')
Traceback (most recent call last):
    ...
seed.math.binary_float.py_float_repr.FloatNumberError__repr_format: 0b1.00p+0
>>> hex_float_repr5bin_('0b1.10p+0')
Traceback (most recent call last):
    ...
seed.math.binary_float.py_float_repr.FloatNumberError__repr_format: 0b1.10p+0


>>> hex_float_repr5bin_('+0b0.0p+0')
Traceback (most recent call last):
    ...
seed.math.binary_float.py_float_repr.FloatNumberError__repr_format: +0b0.0p+0
>>> hex_float_repr5bin_('+0b1.0p+0')
Traceback (most recent call last):
    ...
seed.math.binary_float.py_float_repr.FloatNumberError__repr_format: +0b1.0p+0




>>> hex_float_repr2bin_('0x0.0p+1')
Traceback (most recent call last):
    ...
seed.math.binary_float.py_float_repr.FloatNumberError__repr_format: 0x0.0p+1
>>> hex_float_repr2bin_('0x1.0p+01')
Traceback (most recent call last):
    ...
seed.math.binary_float.py_float_repr.FloatNumberError__repr_format: 0x1.0p+01
>>> hex_float_repr2bin_('0x0.0p-1')
Traceback (most recent call last):
    ...
seed.math.binary_float.py_float_repr.FloatNumberError__repr_format: 0x0.0p-1
>>> hex_float_repr2bin_('0x1.0p-01')
Traceback (most recent call last):
    ...
seed.math.binary_float.py_float_repr.FloatNumberError__repr_format: 0x1.0p-01

>>> hex_float_repr2bin_('0x0.00p+0')
Traceback (most recent call last):
    ...
seed.math.binary_float.py_float_repr.FloatNumberError__repr_format: 0x0.00p+0
>>> hex_float_repr2bin_('0x1.00p+0')
Traceback (most recent call last):
    ...
seed.math.binary_float.py_float_repr.FloatNumberError__repr_format: 0x1.00p+0
>>> hex_float_repr2bin_('0x1.10p+0')
Traceback (most recent call last):
    ...
seed.math.binary_float.py_float_repr.FloatNumberError__repr_format: 0x1.10p+0


>>> hex_float_repr2bin_('+0x0.0p+0')
Traceback (most recent call last):
    ...
seed.math.binary_float.py_float_repr.FloatNumberError__repr_format: +0x0.0p+0
>>> hex_float_repr2bin_('+0x1.0p+0')
Traceback (most recent call last):
    ...
seed.math.binary_float.py_float_repr.FloatNumberError__repr_format: +0x1.0p+0



>>> pint8bits2bin_mantissa_(0)
Traceback (most recent call last):
    ...
TypeError
>>> pint8bits2hex_mantissa_(0)
Traceback (most recent call last):
    ...
TypeError

>>> pint8bits2bin_mantissa_(1)
'0'
>>> pint8bits5bin_mantissa_('0')
1
>>> pint8bits2bin_mantissa_(39)
'00111'
>>> pint8bits5bin_mantissa_('00111')
39


>>> pint8bits2hex_mantissa_(1)
'0'
>>> pint8bits5hex_mantissa_('0')
1
>>> pint8bits2hex_mantissa_(39)
'38'
>>> pint8bits5hex_mantissa_('38')
39



>>> signed_uint_exp_repr2bin_float_repr_((1, 0, 0))
'0b0.0p+0'
>>> signed_uint_exp_repr2bin_float_repr_((-1, 0, 0))
'-0b0.0p+0'
>>> signed_uint_exp_repr5bin_float_repr_('0b0.0p+0')
(1, 0, 0)
>>> signed_uint_exp_repr5bin_float_repr_('-0b0.0p+0')
(-1, 0, 0)

>>> signed_uint_exp_repr2bin_float_repr_((1, 39, -999))
'0b1.00111p-999'
>>> signed_uint_exp_repr2bin_float_repr_((-1, 39, 999))
'-0b1.00111p+999'
>>> signed_uint_exp_repr5bin_float_repr_('0b1.00111p-999')
(1, 39, -999)
>>> signed_uint_exp_repr5bin_float_repr_('-0b1.00111p+999')
(-1, 39, 999)





>>> signed_uint_exp_repr2hex_float_repr_((1, 0, 0))
'0x0.0p+0'
>>> signed_uint_exp_repr2hex_float_repr_((-1, 0, 0))
'-0x0.0p+0'
>>> signed_uint_exp_repr5hex_float_repr_('0x0.0p+0')
(1, 0, 0)
>>> signed_uint_exp_repr5hex_float_repr_('-0x0.0p+0')
(-1, 0, 0)

>>> signed_uint_exp_repr2hex_float_repr_((1, 39, -999))
'0x1.38p-999'
>>> signed_uint_exp_repr2hex_float_repr_((-1, 39, 999))
'-0x1.38p+999'
>>> signed_uint_exp_repr5hex_float_repr_('0x1.38p-999')
(1, 39, -999)
>>> signed_uint_exp_repr5hex_float_repr_('-0x1.38p+999')
(-1, 39, 999)



    float2signed_uint_exp_repr_
        float2hex_float_repr_
        float2bin_float_repr_

[exp4msb <- [-1074..=+1023]]
>>> float.fromhex('0x1p-1050').hex()
'0x0.0000001000000p-1022'

>>> float2signed_uint_exp_repr_(float.fromhex('0x1p-1050'))
(1, 1, -1050)
>>> float2signed_uint_exp_repr_(float.fromhex('-0x1p-1050'))
(-1, 1, -1050)

>>> float2hex_float_repr_(float.fromhex('0x1p-1050'))
'0x1.0p-1050'
>>> float2hex_float_repr_(float.fromhex('-0x1p-1050'))
'-0x1.0p-1050'

>>> float2bin_float_repr_(float.fromhex('0x1p-1050'))
'0b1.0p-1050'
>>> float2bin_float_repr_(float.fromhex('-0x1p-1050'))
'-0b1.0p-1050'

#]]]'''
__all__ = r'''
check_pint8bits
    pint8bits2bin_mantissa_
    pint8bits5bin_mantissa_
    pint8bits2hex_mantissa_
    pint8bits5hex_mantissa_
        hex_mantissa5bin_
        hex_mantissa2bin_

check_signed_uint_exp_repr
    signed_uint_exp_repr2bin_float_repr_
    signed_uint_exp_repr5bin_float_repr_
    signed_uint_exp_repr2hex_float_repr_
    signed_uint_exp_repr5hex_float_repr_
        hex_float_repr5bin_
        hex_float_repr2bin_

FloatNumberError__nan_inf
    float2signed_uint_exp_repr_
        float2hex_float_repr_
        float2bin_float_repr_




FloatNumberError__repr_format
    check_exp4msb__str
    check_hex_mantissa
    check_bin_mantissa
    check_hex_float_repr
    check_bin_float_repr



signed_uint_exp_repr__pos0
signed_uint_exp_repr__neg0
    hex_float_repr__pos0
    hex_float_repr__neg0

    bin_float_repr__pos0
    bin_float_repr__neg0

'''.split()#'''
__all__


import re
from seed.math.binary_float.FloatNumberError import FloatNumberError
from seed.tiny import check_type_is

class FloatNumberError__nan_inf(FloatNumberError):pass
class FloatNumberError__repr_format(FloatNumberError):pass

assert len('0x0.0p+0') == 8
assert '0x0.0p+0' == 0. .hex()
_hex_float__pattern = r'-?0x[01][.][0-9a-f]+p[+-][0-9]+'
_hex_float__pattern = r'(?P<sign>-?)0x(?P<msb_01>[01])[.](?P<hex_mantissa>[0-9a-f]+)p(?P<exp4msb>[+-][0-9]+)'
_hex_float__regex = re.compile(_hex_float__pattern)

def float2signed_uint_exp_repr_(real, /):
    'float -> signed_uint_exp_repr/(sign, uint8bits, exp4msb)/((-1|+1), uint, int) | ^FloatNumberError__nan_inf #[sign =!= 0]{no 0, since -0.0 +0.0} # [[[uint8bits==0] -> [exp4msb==0]][[uint8bits=!=0] --> [uint8bits&1 == 1]][abs(the_input_float) === 0 if uint8bits==0 else uint8bits * 2**(exp4msb-floor_log2_(uint8bits))]]'
    #xxx: return signed_uint_exp_repr5hex_float_repr_(float2hex_float_repr_(real))
    #   float2hex_float_repr_() prev impl only remove tailing_0s
    #       donot handle '0x0.8000000000000p-1022'
    #xxx: #old:
    #
    #check_type_is(float, real)
    #h = real.hex()
    #xxx h = float2hex_float_repr_(real)
    h = float.hex(real)
    if len(h) < 8:raise FloatNumberError__nan_inf((real, h))
    # h.hex_mantissa may contain tailing_0s
    '0x1.0000000000000p-1022'
    # nonzero may startswith -?0x0.
    '0x0.8000000000000p-1022'
    m = _hex_float__regex.fullmatch(h)
    if not m:raise logic-err
    sign = -1 if m['sign'] else +1
        # '-?'
    msb_01 = int(m['msb_01'])
        # '[01]'
    hex_mantissa = m['hex_mantissa']
    exp4msb = int(m['exp4msb'])

    u = int(f'1{hex_mantissa}', 16)
    s = bin(u)
    assert s[:3] == '0b1'
    i = s.rindex('1')
    if msb_01 == 0:
        if hex_mantissa == '0':
            assert exp4msb == 0
            # sign may be -1 !!
            uint8bits = 0
        else:
            assert exp4msb == -1022
            assert 3 <= i
            k = s.index('1', 3)

            uint8bits = int(s[k:i+1], 2)
                # may not be int(hex_mantissa, 16) since tailing_0s

            exp4msb -= (k-2)
    else:
        assert msb_01 == 1
        k = 2
        exp4msb # ok
        #uint8bits = int(s[2:i+1], 2)
        uint8bits = u >> (len(s)-i-1)

    signed_uint_exp_repr = (sign, uint8bits, exp4msb)
    check_signed_uint_exp_repr(signed_uint_exp_repr)
    return signed_uint_exp_repr

def check_signed_uint_exp_repr(signed_uint_exp_repr, /):
    check_type_is(tuple, signed_uint_exp_repr)
    if not len(signed_uint_exp_repr) == 3: raise TypeError
    (sign, uint8bits, exp4msb) = signed_uint_exp_repr
    check_type_is(int, sign)
    check_type_is(int, uint8bits)
    check_type_is(int, exp4msb)
    if not abs(sign) == 1: raise TypeError
    if not uint8bits >= 0: raise TypeError

    if not ((uint8bits == 0) or (uint8bits & 1)): raise TypeError
    if not ((not uint8bits == 0) or (exp4msb == 0)): raise TypeError

def check_pint8bits(pint8bits, /):
    check_type_is(int, pint8bits)
    if not pint8bits > 0: raise TypeError
    if not (pint8bits & 1): raise TypeError

def pint8bits2bin_mantissa_(pint8bits, /):
    check_pint8bits(pint8bits)
    bin_mantissa = _pint8bits2bin_mantissa_(pint8bits)
    check_bin_mantissa(bin_mantissa)
    return bin_mantissa
def _pint8bits2bin_mantissa_(pint8bits, /):
    if pint8bits == 1:
        return '0'
    bits = bin(pint8bits)
    assert bits[:3] == '0b1'
    assert bits[-1:] == '1'
    bin_mantissa = bits[3:]
    return bin_mantissa
def pint8bits5bin_mantissa_(bin_mantissa, /):
    check_bin_mantissa(bin_mantissa)
    pint8bits = _pint8bits5bin_mantissa_(bin_mantissa)
    check_pint8bits(pint8bits)
    return pint8bits
def _pint8bits5bin_mantissa_(bin_mantissa, /):
    if bin_mantissa == '0':
        pint8bits = 1
    else:
        assert bin_mantissa[-1:] == '1'
        pint8bits = int('1'+bin_mantissa, 2)
    return pint8bits


def pint8bits2hex_mantissa_(pint8bits, /):
    check_pint8bits(pint8bits)
    hex_mantissa = _pint8bits2hex_mantissa_(pint8bits)
    check_hex_mantissa(hex_mantissa)
    return hex_mantissa
def _pint8bits2hex_mantissa_(pint8bits, /):
    if pint8bits == 1:
        return '0'
    padded_u = pint8bits << (1-pint8bits.bit_length())%4
    bits = hex(padded_u)
    assert bits[:3] == '0x1', bits
    assert bits[-1:] not in '0'
    hex_mantissa = bits[3:]
    return hex_mantissa
def pint8bits5hex_mantissa_(hex_mantissa, /):
    check_hex_mantissa(hex_mantissa)
    pint8bits = _pint8bits5hex_mantissa_(hex_mantissa)
    check_pint8bits(pint8bits)
    return pint8bits
def _pint8bits5hex_mantissa_(hex_mantissa, /):
    if hex_mantissa == '0':
        pint8bits = 1
    else:
        assert hex_mantissa[-1:] not in '0'
        pint8bits = int('1'+hex_mantissa, 16)
        s = bin(pint8bits & 0x0f)
        # remove tailing_0s
        i = s.rindex('1')
        num_tailing_0s = len(s) - (i+1)
        if num_tailing_0s:
            pint8bits >>= num_tailing_0s
        assert pint8bits & 1
    pint8bits
    return pint8bits




def signed_uint_exp_repr2bin_float_repr_(signed_uint_exp_repr, /):
    check_signed_uint_exp_repr(signed_uint_exp_repr)
    bin_float_repr = _signed_uint_exp_repr2bin_float_repr_(signed_uint_exp_repr)
    check_bin_float_repr(bin_float_repr)
    return bin_float_repr
def _signed_uint_exp_repr2bin_float_repr_(signed_uint_exp_repr, /):
    (sign, uint8bits, exp4msb) = signed_uint_exp_repr
    if uint8bits == 0:
        return bin_float_repr__neg0 if sign == -1 else bin_float_repr__pos0
    s_ = '-0b1.' if sign == -1 else '0b1.'
    bin_mantissa = pint8bits2bin_mantissa_(uint8bits)
    sign4exp = '' if exp4msb < 0 else '+'
    s = f'{s_}{bin_mantissa}p{sign4exp}{exp4msb}'
    return s

def signed_uint_exp_repr5bin_float_repr_(bin_float_repr, /):
    check_bin_float_repr(bin_float_repr)
    signed_uint_exp_repr = _signed_uint_exp_repr5bin_float_repr_(bin_float_repr)
    check_signed_uint_exp_repr(signed_uint_exp_repr)
    return signed_uint_exp_repr
def _signed_uint_exp_repr5bin_float_repr_(bin_float_repr, /):
    s4b = bin_float_repr
    if 'b0' in s4b[:4]:
        if s4b == bin_float_repr__pos0:
            return signed_uint_exp_repr__pos0 # (+1, 0, 0)
        if s4b == bin_float_repr__neg0:
            return signed_uint_exp_repr__neg0 # (-1, 0, 0)
        raise FloatNumberError__repr_format(bin_float_repr)
    if not s4b.index('0b1.', 0, 5) < 2: raise FloatNumberError__repr_format(bin_float_repr) # no '0b0.'
        # '-0b1.'
    idx4dot = s4b.index('.')
    idx4p = s4b.rindex('p')

    bin_mantissa = s4b[idx4dot+1:idx4p]
    uint8bits = pint8bits5bin_mantissa_(bin_mantissa)
    exp4msb = int(s4b[idx4p+1:])
    sign = -1 if s4b[0] == '-' else +1

    return (sign, uint8bits, exp4msb)


def signed_uint_exp_repr5hex_float_repr_(hex_float_repr, /):
    check_hex_float_repr(hex_float_repr)
    signed_uint_exp_repr = _signed_uint_exp_repr5hex_float_repr_(hex_float_repr)
    check_signed_uint_exp_repr(signed_uint_exp_repr)
    return signed_uint_exp_repr
def _signed_uint_exp_repr5hex_float_repr_(hex_float_repr, /):
    s4h = hex_float_repr
    if 'x0' in s4h[:4]:
        if s4h == hex_float_repr__pos0:
            return signed_uint_exp_repr__pos0 # (+1, 0, 0)
        if s4h == hex_float_repr__neg0:
            return signed_uint_exp_repr__neg0 # (-1, 0, 0)
        raise FloatNumberError__repr_format(hex_float_repr)
    if not s4h.index('0x1.', 0, 5) < 2: raise FloatNumberError__repr_format(hex_float_repr) # no '0x0.' which from float.hex()
        # '-0x1.'
    idx4dot = s4h.index('.')
    idx4p = s4h.rindex('p')

    hex_mantissa = s4h[idx4dot+1:idx4p]
    uint8bits = pint8bits5hex_mantissa_(hex_mantissa)
    exp4msb = int(s4h[idx4p+1:])
    sign = -1 if s4h[0] == '-' else +1

    return (sign, uint8bits, exp4msb)



def signed_uint_exp_repr2hex_float_repr_(signed_uint_exp_repr, /):
    check_signed_uint_exp_repr(signed_uint_exp_repr)
    hex_float_repr = _signed_uint_exp_repr2hex_float_repr_(signed_uint_exp_repr)
    check_hex_float_repr(hex_float_repr)
    return hex_float_repr
def _signed_uint_exp_repr2hex_float_repr_(signed_uint_exp_repr, /):
    (sign, uint8bits, exp4msb) = signed_uint_exp_repr
    if uint8bits == 0:
        return hex_float_repr__neg0 if sign == -1 else hex_float_repr__pos0
    s_ = '-0x1.' if sign == -1 else '0x1.'
    hex_mantissa = pint8bits2hex_mantissa_(uint8bits)
    sign4exp = '' if exp4msb < 0 else '+'
    s = f'{s_}{hex_mantissa}p{sign4exp}{exp4msb}'
    return s













_greek_exp4msb__pattern = r'[+]0|[+-][1-9][0-9]*'

_greek_hex_mantissa__pattern = r'0|[0-9a-f]*[1-9a-f]'
_greek_bin_mantissa__pattern = r'0|[01]*1'



_greek_hex_float__pattern = rf'(?P<sign>-?)0x(?:0[.]0p[+]0|1[.](?P<hex_mantissa4msb1>{_greek_hex_mantissa__pattern})p(?P<exp4msb>{_greek_exp4msb__pattern}))'
_greek_bin_float__pattern = rf'(?P<sign>-?)0b(?:0[.]0p[+]0|1[.](?P<bin_mantissa4msb1>{_greek_bin_mantissa__pattern})p(?P<exp4msb>{_greek_exp4msb__pattern}))'
    # bug: r'' --> rf''

_greek_exp4msb__regex = re.compile(_greek_exp4msb__pattern)

_greek_hex_mantissa__regex = re.compile(_greek_hex_mantissa__pattern)
_greek_bin_mantissa__regex = re.compile(_greek_bin_mantissa__pattern)

_greek_bin_float__regex = re.compile(_greek_bin_float__pattern)
_greek_hex_float__regex = re.compile(_greek_hex_float__pattern)


def _check_fmt(regex, s, /):
    m = regex.fullmatch(s)
    if not m:
        raise FloatNumberError__repr_format(s)

def check_exp4msb__str(exp4msb__str, /):
    _check_fmt(_greek_exp4msb__regex, exp4msb__str)

def check_hex_mantissa(hex_mantissa, /):
    _check_fmt(_greek_hex_mantissa__regex, hex_mantissa)
def check_bin_mantissa(bin_mantissa, /):
    _check_fmt(_greek_bin_mantissa__regex, bin_mantissa)

def check_hex_float_repr(hex_float_repr, /):
    _check_fmt(_greek_hex_float__regex, hex_float_repr)
def check_bin_float_repr(bin_float_repr, /):
    _check_fmt(_greek_bin_float__regex, bin_float_repr)

check_exp4msb__str('-999')
check_hex_mantissa('4')
check_hex_float_repr('0x0.0p+0')
check_hex_float_repr('0x1.0p+0')
check_hex_float_repr('0x1.4p+0')
check_hex_float_repr('0x1.4p+999')
check_hex_float_repr('-0x1.4p-999')

_tailing_0s_p__regex = re.compile('0*p')

def float2hex_float_repr_(real, /):
    'float -> hex_float_repr/str'
    hex_float_repr = signed_uint_exp_repr2hex_float_repr_(float2signed_uint_exp_repr_(real))
    return hex_float_repr
    ########################
    ########################
    #bug:old:
    #   float2hex_float_repr_() prev impl only remove tailing_0s
    #       donot handle '0x0.8000000000000p-1022'
    #xxx: #old:
    h = h0 = float.hex(real)
    if len(h) < 8:raise FloatNumberError__nan_inf((real, h))
    # h.hex_mantissa may contain tailing_0s
    '0x1.0000000000000p-1022'
    # nonzero may startswith -?0x0.
    '0x0.8000000000000p-1022'

    if hex_float_repr__pos0 in h:
        '+-zero'
        return h
    'non-zero'
    if 1:
        # remove tailing_0s
        '0x1.0000000000000p-1022'
        m = _tailing_0s_p__regex.search(h)
        i, j = m.span()
        if h[i-1] == '.':
            if not h[i-3:i] == 'b1.':
                raise FloatNumberError__repr_format('logic-err:float.hex() --> {h!r}')
            i += 1
        j -= 1 # 'p'
        if j - i:
            h = h[:i] + h[j:]
        assert h[i] == 'p'
        assert not h[i-1] == '0' or h[i-4:i+1] == 'b1.0p'
    if 'b1' in h:
        '0x1.0040000000000p-1022'
        '   --> 0x1.004p-1022'
        return h
    if not 'b0' in h:
        raise FloatNumberError__repr_format('logic-err:float.hex() --> {h!r}')
    '0x0.0800000000000p-1022'
    '   --> 0x0.08p-1022'

    h.as_integer_ratio()
    ...
    raise 'fail'

    ########################
    ########################
    #bug:old:
    m = _tailing_0s_p__regex.search(h)
    i, j = m.span()
    if h[i-1] == '.':
        i += 1
    j -= 1 # 'p'
    if j - i:
        h = h[:i] + h[j:]

    hex_float_repr = h
    check_hex_float_repr(hex_float_repr)
    return hex_float_repr
def float2bin_float_repr_(real, /):
    'float -> bin_float_repr/str'
    bin_float_repr = signed_uint_exp_repr2bin_float_repr_(float2signed_uint_exp_repr_(real))
    return bin_float_repr
    ########################
    #old:
    bin_float_repr = hex_float_repr2bin_(float2hex_float_repr_(real))
    #check_bin_float_repr(bin_float_repr)
    return bin_float_repr

hex_float_repr__pos0 = '0x0.0p+0'
bin_float_repr__pos0 = '0b0.0p+0'
assert hex_float_repr__pos0 == (0.).hex()
assert bin_float_repr__pos0 == hex_float_repr__pos0.replace('x', 'b')
assert bin_float_repr__pos0.replace('b', 'x') == hex_float_repr__pos0

hex_float_repr__neg0 = '-0x0.0p+0'
bin_float_repr__neg0 = '-0b0.0p+0'
assert bin_float_repr__neg0 == '-' + bin_float_repr__pos0
assert hex_float_repr__neg0 == '-' + hex_float_repr__pos0

check_hex_float_repr(hex_float_repr__pos0)
check_hex_float_repr(hex_float_repr__neg0)

check_bin_float_repr(bin_float_repr__pos0)
check_bin_float_repr(bin_float_repr__neg0)


signed_uint_exp_repr__pos0 = (+1, 0, 0)
signed_uint_exp_repr__neg0 = (-1, 0, 0)
check_signed_uint_exp_repr(signed_uint_exp_repr__pos0)
check_signed_uint_exp_repr(signed_uint_exp_repr__neg0)

assert bin_float_repr__pos0 == signed_uint_exp_repr2bin_float_repr_(signed_uint_exp_repr__pos0)
assert bin_float_repr__neg0 == signed_uint_exp_repr2bin_float_repr_(signed_uint_exp_repr__neg0)

assert signed_uint_exp_repr__pos0 == signed_uint_exp_repr5bin_float_repr_(bin_float_repr__pos0)
assert signed_uint_exp_repr__neg0 == signed_uint_exp_repr5bin_float_repr_(bin_float_repr__neg0)


assert hex_float_repr__pos0 == signed_uint_exp_repr2hex_float_repr_(signed_uint_exp_repr__pos0)
assert hex_float_repr__neg0 == signed_uint_exp_repr2hex_float_repr_(signed_uint_exp_repr__neg0)

assert signed_uint_exp_repr__pos0 == signed_uint_exp_repr5hex_float_repr_(hex_float_repr__pos0)
assert signed_uint_exp_repr__neg0 == signed_uint_exp_repr5hex_float_repr_(hex_float_repr__neg0)










def hex_float_repr2bin_(hex_float_repr, /):
    'hex_float_repr/str -> bin_float_repr/str'
    return signed_uint_exp_repr2bin_float_repr_(signed_uint_exp_repr5hex_float_repr_(hex_float_repr))

def hex_float_repr5bin_(bin_float_repr, /):
    'bin_float_repr/str -> hex_float_repr/str'
    return signed_uint_exp_repr2hex_float_repr_(signed_uint_exp_repr5bin_float_repr_(bin_float_repr))







def hex_mantissa5bin_(bin_mantissa, /):
    'bin_mantissa/str -> hex_mantissa/str'
    return pint8bits2hex_mantissa_(pint8bits5bin_mantissa_(bin_mantissa))

def hex_mantissa2bin_(hex_mantissa, /):
    'hex_mantissa/str -> bin_mantissa/str'
    return pint8bits2bin_mantissa_(pint8bits5hex_mantissa_(hex_mantissa))

__all__


from seed.math.binary_float.py_float_repr import float2signed_uint_exp_repr_
from seed.math.binary_float.py_float_repr import *
