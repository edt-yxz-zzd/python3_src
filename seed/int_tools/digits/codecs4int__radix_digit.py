#__all__:goto
r'''[[[
e ../../python3_src/seed/int_tools/digits/codecs4int__radix_digit.py

seed.int_tools.digits.codecs4int__radix_digit
py -m nn_ns.app.debug_cmd   seed.int_tools.digits.codecs4int__radix_digit -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.int_tools.digits.codecs4int__radix_digit:__doc__ -ht # -ff -df

[[
源起:
    view script/枚举冫十进位制素数牜前缀皆然扌.py
    某基数进位制表达=>(tuple<uint%radix> | str{数字表达::前刹&&词典序&&无上限})
==>>:
一个简单方案:alphabet36_digit16
    字母表:36胞(ASCII数字字母)
        实际负载数字表:16胞#极限效率4bit
    单层码/立即数/独胞码:[0-9A-F] # [0..<16]
    双层码:[WXY][G-V]+ # [0..<2**16]
        W[G-V]{2} # [0..<16**2]
        X[G-V]{3} # [0..<16**3]
        Y[G-V]{4} # [0..<16**4]
    三层码:Z+[G-V]+
        # [n:<-[1..]]
        Z{n}[G-V]{n}[G-V]{len=第二层数}
            # 第二层数 <- [0..<16**n]
            # 第三层数 <- [0..<16**第二层数]
            #但此方案下第二层数的编码效率只有一半(2bit/胞)
            #考虑更进:动态胞元{爻元数每胞/2}->动态爻元{爻元数每胞-1}
:%s/_36_16/_36_16_16/g
    36-字母表
    16-字母表纟负载胞纟立即数
    16-字母表纟负载胞纟尾数
]]
%s/encode_36_16_16_\>/encode_36_16_16__uint_/g
%s/decode_36_16_16_\>/decode_36_16_16__uint_/g
%s/decode_36_16_16_ex_\>/decode_36_16_16__uint_ex_/g


>>> def _encode_36_16_16__uint_(u, /):
...     s = encode_36_16_16__uint_(u)
...     if not u == decode_36_16_16__uint_(s):raise 000
...     return s

>>> [*map(_encode_36_16_16__uint_, range(34))]
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'WHG', 'WHH', 'WHI', 'WHJ', 'WHK', 'WHL', 'WHM', 'WHN', 'WHO', 'WHP', 'WHQ', 'WHR', 'WHS', 'WHT', 'WHU', 'WHV', 'WIG', 'WIH']
>>> [*map(decode_36_16_16__uint_, _)] == [*range(34)]
True
>>> _encode_36_16_16__uint_(2**4-1)
'F'
>>> _encode_36_16_16__uint_(2**4)
'WHG'
>>> _encode_36_16_16__uint_(2**8-1)
'WVV'
>>> _encode_36_16_16__uint_(2**8)
'XHGG'
>>> _encode_36_16_16__uint_(2**12-1)
'XVVV'
>>> _encode_36_16_16__uint_(2**12)
'YHGGG'
>>> _encode_36_16_16__uint_(2**16-1)
'YVVVV'
>>> _encode_36_16_16__uint_(2**16)
'ZLHGGGG'
>>> _encode_36_16_16__uint_(2**20-1)
'ZLVVVVV'
>>> _encode_36_16_16__uint_(2**20)
'ZMHGGGGG'

>>> _encode_36_16_16__uint_(2**60-1)
'ZVVVVVVVVVVVVVVVV'
>>> _encode_36_16_16__uint_(2**60)
'ZZHGHGGGGGGGGGGGGGGG'


>>> _encode_36_16_16__uint_(2**64-1)
'ZZHGVVVVVVVVVVVVVVVV'
>>> _encode_36_16_16__uint_(2**64)
'ZZHHHGGGGGGGGGGGGGGGG'



>>> encode_36_16_16__uints_(range(34))
'0123456789ABCDEFWHGWHHWHIWHJWHKWHLWHMWHNWHOWHPWHQWHRWHSWHTWHUWHVWIGWIH'
>>> decode_36_16_16__uints_(_) == tuple(range(34))
True






py_adhoc_call   seed.int_tools.digits.codecs4int__radix_digit   @f
]]]'''#'''
__all__ = r'''
encode_36_16_16__uint_
decode_36_16_16__uint_
    decode_36_16_16__uint_ex_

encode_36_16_16__uints_
decode_36_16_16__uints_
    decode_36_16_16__uints_ex_
        iter_decode_36_16_16__uints_ex_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.tiny_.check import check_type_is, check_int_ge
from seed.text.join_between import join_between
from seed.seq_tools.mk_seq_rng import mk_seq_rng, mk_seq_rng__len
from seed.int_tools.digits.codecs4int__alnum__abc import ICodes4uint

from itertools import islice
___end_mark_of_excluded_global_names__0___ = ...



_tbl_16H = join_between(*'09') + join_between(*'AF')
_tbl_16T = join_between(*'GV')
assert len(_tbl_16H) == 16
assert len(_tbl_16T) == 16
_tbl_H2T = str.maketrans(_tbl_16H, _tbl_16T)
_tbl_H5T = str.maketrans(_tbl_16T, _tbl_16H)
def _tail5uint(u, /):
    #s = hex(u).upper()
    s = f'{u:X}'
    return s.translate(_tbl_H2T)
def _tail2uint(s, /):
    return int(s.translate(_tbl_H5T), 16)
def encode_36_16_16__uint_(u, /):
    check_int_ge(0, u)
    if u < 16:
        return _tbl_16H[u]
    tail = _tail5uint(u)
    sz = len(tail)
    assert sz >= 2
    if sz <= 4:
        head = 'WXY'[sz-2]
        return head+tail
    neck = _tail5uint(sz)
    n = len(neck)
    assert n >= 1
    head = 'Z'*n
    return f'{head}{neck}{tail}'
def _decode_36_16_16__uint_ex_(s, begin, end, /):
    L = end-begin
    if not 0 < L:raise ValueError
    h = s[begin]
    if h <= 'F':
        #return _tbl_16H.index(h)
        if h <= '9':
            if not h >= '0': raise ValueError
            u = ord(h) -ord('0')
        else:
            if not h >= 'A': raise ValueError
            u = 10 +ord(h) -ord('A')
        u
        next_begin = begin+1
        return (u, next_begin)

    if h == 'Z':
        for i in range(begin, end):
            if not s[i] == 'Z':
                break
        else:
            raise ValueError
        # [begin <= i < end]
        # [s[i] =!= 'Z']
        n = i-begin
        assert n >= 1
        j = i+n
        if not j <= end:raise ValueError
        neck = s[i:j]
        sz = _tail2uint(neck)
    else:
        sz = 2 + 'WXY'.index(h)
            # ^ValueError
        j = begin+1
    j, sz
    k = j+sz
    if not k <= end:raise ValueError
    tail = s[j:k]
    u = _tail2uint(tail)
    next_begin = k
    return (u, next_begin)

class _Codes4uint_36_16_16(ICodes4uint):
    __slots__ = ()
    #___no_slots_ok___ = True
    #@override
    def encode__uint_(sf, i, /):
        'int -> str'
        return encode_36_16_16__uint_(i)
    #@override
    def _decode__uint_ex_(sf, s, begin, end, /):
        'str -> begin/uint -> end/uint -> (uint, next_begin)|^ValueError'
        return _decode_36_16_16__uint_ex_(s, begin, end)
_codes4uint_36_16_16 = _Codes4uint_36_16_16()

######################
decode_36_16_16__uint_ = _codes4uint_36_16_16.decode__int_
decode_36_16_16__uint_ex_ = _codes4uint_36_16_16.decode__int_ex_

encode_36_16_16__uints_ = _codes4uint_36_16_16.encode__ints_
decode_36_16_16__uints_ = _codes4uint_36_16_16.decode__ints_
decode_36_16_16__uints_ex_ = _codes4uint_36_16_16.decode__ints_ex_
iter_decode_36_16_16__uints_ex_ = _codes4uint_36_16_16.iter_decode__ints_ex_
######################
#.def decode_36_16_16__uint_(s, begin=None, end=None, /, *, strict=True):
#.    '-> uint|^ValueError'
#.    (u, next_begin) = decode_36_16_16__uint_ex_(s, begin, end, strict=strict)
#.    return u
#.def decode_36_16_16__uint_ex_(s, begin=None, end=None, /, *, strict=False):
#.    '-> (uint, next_begin)|^ValueError'
#.    (begin, end) = mk_seq_rng(s, begin, end)
#.    if not begin < end:raise ValueError
#.        #?UnicodeDecodeError
#.    r = _decode_36_16_16__uint_ex_(s, begin, end)
#.    if strict:
#.        (u, next_begin) = r
#.        if not next_begin == end:raise ValueError
#.    return r
#.#######
#.def encode_36_16_16__uints_(us, /):
#.    return ''.join(map(encode_36_16_16__uint_, us))
#.def decode_36_16_16__uints_(s, begin=None, end=None, /, *, max_num_uints=None, strict=True):
#.    '-> [uint]|^ValueError'
#.    (us, next_begin) = decode_36_16_16__uints_ex_(s, begin, end, max_num_uints=max_num_uints, strict=strict)
#.    return us
#.def decode_36_16_16__uints_ex_(s, begin=None, end=None, /, *, max_num_uints=None, strict=False):
#.    '-> ([uint], next_begin)|^ValueError'
#.    (begin, end) = mk_seq_rng(s, begin, end)
#.        #=> init:next_begin&&strict-check
#.    it = iter_decode_36_16_16__uints_ex_(s, begin, end, strict=strict)
#.    if not max_num_uints is None:
#.        it = islice(it, 0, max_num_uints)
#.    us = []
#.    next_begin = begin
#.    for (u, next_begin) in it:
#.        us.append(u)
#.    if strict:
#.        if not next_begin == end:raise ValueError
#.    us = tuple(us)
#.    return (us, next_begin)
#.def iter_decode_36_16_16__uints_ex_(s, begin=None, end=None, /, *, strict=False):
#.    (begin, end) = mk_seq_rng(s, begin, end)
#.    if not begin <= end:raise ValueError
#.    try:
#.        while not begin == end:
#.            r = _decode_36_16_16__uint_ex_(s, begin, end)
#.                #^ValueError
#.            yield r
#.            (u, next_begin) = r
#.            begin = next_begin
#.    except ValueError:
#.        if strict:
#.            raise
#.        else:
#.            pass
#.    #yield (True, begin)
######################


__all__
from seed.int_tools.digits.codecs4int__radix_digit import encode_36_16_16__uint_, decode_36_16_16__uint_, decode_36_16_16__uint_ex_
from seed.int_tools.digits.codecs4int__radix_digit import encode_36_16_16__uints_, decode_36_16_16__uints_, decode_36_16_16__uints_ex_, iter_decode_36_16_16__uints_ex_
from seed.int_tools.digits.codecs4int__radix_digit import *
