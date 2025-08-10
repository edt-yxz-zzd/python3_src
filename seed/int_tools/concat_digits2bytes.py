#__all__:goto
r'''[[[
e ../../python3_src/seed/int_tools/concat_digits2bytes.py

seed.int_tools.concat_digits2bytes
py -m nn_ns.app.debug_cmd   seed.int_tools.concat_digits2bytes -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.int_tools.concat_digits2bytes:__doc__ -ht # -ff -df

[[
源起:
    view ../../python3_src/seed/int_tools/digits/codecs4int.py
]]

######################
>>> from seed.int_tools.RadixInfo import IZpowRadixInfo, ZpowRadixInfo, mk_ZpowRadixInfo_
>>> r256 = ZpowRadixInfo(8)
>>> r16 = ZpowRadixInfo(4)
>>> r8 = ZpowRadixInfo(3)
>>> r2 = ZpowRadixInfo(1)
>>> r1 = ZpowRadixInfo(0)

>>> concat_digits2bytes_(0, [(r1, 0)])
b''
>>> concat_digits2bytes_(7, [(r2, 1)])
b'\x01'
>>> concat_digits2bytes_(0, [(r2, 1)])
Traceback (most recent call last):
    ...
seed.int_tools.concat_digits2bytes.NonAlignedError: 1

>>> concat_digits2bytes_(0, __:=[(r1, 0), (r2, 1), (r256, 1), (r8, 2), (r16, 15)])
b'\x80\xaf'
>>> list(map(bin, _))
['0b10000000', '0b10101111']


['0b10000000', '0b10101111']
1-0000000 1-010-1111
1 ........1 ..2 ..15


>>> bin(concat_digits2uint_(0, __))
'0b1000000010101111'



######################
test 『optimize for big radix (32bit)』
>>> r2e26 = ZpowRadixInfo(26)
>>> r2e7 = ZpowRadixInfo(7)
>>> r2e6 = ZpowRadixInfo(6)

#small radix
>>> [*concat_digits2iter_bytess_(0, __:=[(r2e6, 63), (r2e26, 1)])]
[b'\xfc\x00\x00\x01']
>>> bin(concat_digits2uint_(0, __))
'0b11111100000000000000000000000001'

#big radix
>>> [*concat_digits2iter_bytess_(0, __:=[(r2e7, 127), (r2e26, 1), (r2e7, 63)])]
[b'\xfe', b'\x00\x00\x00', b'\xbf']
>>> concat_digits2bytes_(0, __)
b'\xfe\x00\x00\x00\xbf'
>>> list(map(bin, _))
['0b11111110', '0b0', '0b0', '0b0', '0b10111111']
>>> bin(concat_digits2uint_(0, __))
'0b1111111000000000000000000000000010111111'


######################







py_adhoc_call   seed.int_tools.concat_digits2bytes   @f
]]]'''#'''
__all__ = r'''
NonAlignedError

concat_digits2uint_
concat_digits2bytes_
concat_digits2iter_bytess_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.from seed.int_tools.RadixInfo import IZpowRadixInfo, ZpowRadixInfo, mk_ZpowRadixInfo_
from seed.tiny_.check import check_type_is, check_int_ge
#.
from seed.abc.abc__ver1 import abstractmethod, override, ABC
___end_mark_of_excluded_global_names__0___ = ...


_j2mask = tuple((1<<j)-1 for j in range(8))
class NonAlignedError(Exception):pass
def concat_digits2uint_(num_pad_lead_0s, zpow_radix_info__digit__pairs, /, *, nonaligned_ok=False, output_=None):
    'big_endian => uint -> Iter (zpow_radix_info/IZpowRadixInfo, digit/uint%zpow_radix_info.radix) -> (uint|^NonAlignedError{[not nonaligned_ok][num_pad_tail_0s=!=0]}) # [output_ :: (num_pad_tail_0s,total_bits) -> None]'
    bs = concat_digits2bytes_(num_pad_lead_0s, zpow_radix_info__digit__pairs, nonaligned_ok=nonaligned_ok, output_=output_)
    return int.from_bytes(bs, 'big')
def concat_digits2bytes_(num_pad_lead_0s, zpow_radix_info__digit__pairs, /, *, nonaligned_ok=False, output_=None):
    'big_endian => uint -> Iter (zpow_radix_info/IZpowRadixInfo, digit/uint%zpow_radix_info.radix) -> (bytes|^NonAlignedError{[not nonaligned_ok][num_pad_tail_0s=!=0]}) # [output_ :: (num_pad_tail_0s,total_bits) -> None]'
    it = concat_digits2iter_bytess_(num_pad_lead_0s, zpow_radix_info__digit__pairs, nonaligned_ok=nonaligned_ok, output_=output_)
    return b''.join(it)
def concat_digits2iter_bytess_(num_pad_lead_0s, zpow_radix_info__digit__pairs, /, *, nonaligned_ok=False, output_=None):
    'big_endian => uint -> Iter (zpow_radix_info/IZpowRadixInfo, digit/uint%zpow_radix_info.radix) -> (Iter bytes|^NonAlignedError{[not nonaligned_ok][num_pad_tail_0s=!=0]}) # [output_ :: (num_pad_tail_0s,total_bits) -> None]'
    check_int_ge(0, num_pad_lead_0s)
    total_bits = num_pad_lead_0s
    q, r = divmod(num_pad_lead_0s, 8)
    if q:
        yield '\0'*q
    j2mask = _j2mask
    num_bits4remain = r
    u4remain = 0
    for zpow_radix_info, digit in zpow_radix_info__digit__pairs:
        # [0 <= num_bits4remain < 8]
        # [0 <= u4remain < 2**num_bits4remain]
        # => [0 <= u4remain < 128]

        #radix = zpow_radix_info.radix
        #max_digit = zpow_radix_info.max_digit
        num_bits4digit = zpow_radix_info.num_bits4digit
        777;total_bits += num_bits4digit
        nbits4u = num_bits4remain+num_bits4digit
        if nbits4u > 32:
            # optimize for big radix (32bit)
            q, r = divmod(nbits4u, 8)
            bs = (digit>>r).to_bytes(q, 'big')
            h = (u4remain << (num_bits4digit-r-((q-1)<<3))) | bs[0]
            yield bytes([h])
            yield bs[1:]
            u = digit
                # for below:『u4remain = u & j2mask[r]』
        else:
            # normal for small radix
            u = (u4remain << num_bits4digit) | digit
            if nbits4u < 8:
                num_bits4remain = nbits4u
                u4remain = u
                continue
            q, r = divmod(nbits4u, 8)
            assert q >= 1
            bs = (u>>r).to_bytes(q, 'big')
            yield bs
        if not r:
            num_bits4remain = 0
            u4remain = 0
            continue
        num_bits4remain = r
        u4remain = u & j2mask[r]
    if num_bits4remain:
        if not nonaligned_ok:raise NonAlignedError(num_bits4remain)
        num_pad_tail_0s = 8-num_bits4remain
        assert 0 < num_pad_tail_0s < 8
        u = u4remain << num_pad_tail_0s
        yield bytes([u])
        num_bits4remain = 0
        u4remain = 0
    else:
        num_pad_tail_0s = 0
    num_pad_tail_0s
    total_bits
    if not None is output_:
        output_((num_pad_tail_0s,total_bits))
    return


__all__
from seed.int_tools.concat_digits2bytes import NonAlignedError
from seed.int_tools.concat_digits2bytes import concat_digits2uint_, concat_digits2bytes_, concat_digits2iter_bytess_
from seed.int_tools.concat_digits2bytes import *
