#__all__:goto
r'''[[[
e ../../python3_src/seed/int_tools/digits/codecs4int__alnum.py

seed.int_tools.digits.codecs4int__alnum
py -m nn_ns.app.debug_cmd   seed.int_tools.digits.codecs4int__alnum -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.int_tools.digits.codecs4int__alnum:__doc__ -ht # -ff -df

[[
相关:
    view ../../python3_src/seed/int_tools/digits/codecs4int__radix_digit.py
    view others/数学/编程/设计/自定义字节编码.txt
]]
[[
约束:字母表==ASCII数字字母(36胞) => 最高负载效率5bit(32胞)
约束:词典序 => 必须包含 正负号，0若不能兼容，则不能是 单胞码
约束:避免合法py字面值、标识符
约束:保留[0Z]，作为扩展，如:正负无穷
编码整数:[69][^0-9XBOZJEPLIC][^690Z]*
其中:
    [^0-9XBOZJEPLIC] == [ADFGHKMNQRSTUVWY]
    [^690Z] == [1-578A-Y]
    [69] 代表 [-+]

负数表达 == 取反(正数表达)
零表达 == 正零表达
正数表达:
    单层表达:9[ADFGHKMNQR] # [0..<10]
    双层表达:9[STUVW][1-578A-Y]+ # [0..<32**5] #25bit
        9S[1-578A-Y]{1}
        9T[1-578A-Y]{2}
        9U[1-578A-Y]{3}
        9V[1-578A-Y]{4}
        9W[1-578A-Y]{5}
    三层表达:9Y+[1-578A-X][1-578A-Y]+
        # [n:<-[1..]]
        9Y{n}([1-578A-X][1-578A-Y]{n-1})[1-578A-Y]{len==第二层数}
            #但此方案下第二层数的编码效率只有一半(2.5bit/胞)
            #考虑更进:动态胞元{爻元数每胞/2}->动态爻元{爻元数每胞-1}
:%s/_36_32/_36_10_32/g
    36-字母表#实际只用34
:.+1,$s/_36_10_32/_34_10_32/g
    34-字母表
    10-字母表纟负载胞纟立即数
    32-字母表纟负载胞纟尾数
]]

%s/encode_34_10_32_\>/encode_34_10_32__int_/g
%s/decode_34_10_32_\>/decode_34_10_32__int_/g
%s/decode_34_10_32_ex_\>/decode_34_10_32__int_ex_/g

>>> def _encode_34_10_32__int_(i, /):
...     s = encode_34_10_32__int_(i)
...     if not i == decode_34_10_32__int_(s):raise 000
...     return s
>>> def _2_encode_34_10_32__int_(i, /):
...     s0 = _encode_34_10_32__int_(i)
...     s1 = _encode_34_10_32__int_(-i)
...     print(s0)
...     print(s1)
>>> def _3_encode_34_10_32__int_(k, /):
...     j = 2**k
...     i = j-1
...     print(k)
...     _2_encode_34_10_32__int_(i)
...     _2_encode_34_10_32__int_(j)

>>> [*map(_encode_34_10_32__int_, range(-18,17))]
['6KG', '6KH', '6KI', '6KJ', '6KK', '6KL', '6KM', '6KN', '6KO', '6M', '6N', '6Q', '6R', '6S', '6T', '6U', '6V', '6W', '9A', '9D', '9F', '9G', '9H', '9K', '9M', '9N', '9Q', '9R', '9SD', '9SE', '9SF', '9SG', '9SH', '9SI', '9SJ']
>>> [*map(decode_34_10_32__int_, _)] == [*range(-18,17)]
True
>>> _encode_34_10_32__int_(10-1)
'9R'
>>> _encode_34_10_32__int_(10)
'9SD'

>>> _encode_34_10_32__int_(2**5-1)
'9SY'
>>> _encode_34_10_32__int_(2**5)
'9T21'
>>> _encode_34_10_32__int_(2**10-1)
'9TYY'
>>> _encode_34_10_32__int_(2**10)
'9U211'
>>> _encode_34_10_32__int_(2**15-1)
'9UYYY'
>>> _encode_34_10_32__int_(2**15)
'9V2111'
>>> _encode_34_10_32__int_(2**20-1)
'9VYYYY'
>>> _encode_34_10_32__int_(2**20)
'9W21111'

>>> _encode_34_10_32__int_(2**25-1)
'9WYYYYY'
>>> _encode_34_10_32__int_(2**25)
'9Y7211111'


>>> _encode_34_10_32__int_(2**32-1)
'9Y84YYYYYY'
>>> _encode_34_10_32__int_(2**32)
'9Y85111111'

>>> _encode_34_10_32__int_(2**64-1)
'9YFIYYYYYYYYYYYY'
>>> _encode_34_10_32__int_(2**64)
'9YFJ111111111111'



>>> encode_34_10_32__ints_(range(-18,17))
'6KG6KH6KI6KJ6KK6KL6KM6KN6KO6M6N6Q6R6S6T6U6V6W9A9D9F9G9H9K9M9N9Q9R9SD9SE9SF9SG9SH9SI9SJ'
>>> decode_34_10_32__ints_(_) == tuple(range(-18,17))
True




>>> for k in range(8):_3_encode_34_10_32__int_(5*k)
0
9A
9A
9D
6W
5
9SY
6K1
9T21
6HXY
10
9TYY
6H11
9U211
6GXYY
15
9UYYY
6G111
9V2111
6FXYYY
20
9VYYYY
6F1111
9W21111
6DXYYYY
25
9WYYYYY
6D11111
9Y7211111
6ATXYYYYY
30
9Y7YYYYYY
6AT111111
9Y82111111
6ASXYYYYYY
35
9Y8YYYYYYY
6AS1111111
9YA21111111
6ARXYYYYYYY



py_adhoc_call   seed.int_tools.digits.codecs4int__alnum   @f
from seed.int_tools.digits.codecs4int__alnum import *
]]]'''#'''
__all__ = r'''
encode_34_10_32__int_
decode_34_10_32__int_
    decode_34_10_32__int_ex_

encode_34_10_32__ints_
decode_34_10_32__ints_
    decode_34_10_32__ints_ex_
    iter_decode_34_10_32__ints_ex_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.text.join_between import join_between
from seed.int_tools.digits.uintZSbase32 import uintZbase32_, uintSbase32_, base32_alplabet
#from seed.seq_tools.mk_seq_rng import mk_seq_rng, mk_seq_rng__len
from seed.int_tools.digits.codecs4int__alnum__abc import ICodes4int
from seed.tiny_.check import check_type_is, check_int_ge
from itertools import islice
___end_mark_of_excluded_global_names__0___ = ...


def _inv_seq(ls, /):
    return {x:j for j, x in enumerate(ls)}

_tbl_fst = '69'
_tbl_snd = 'ADFGHKMNQR'
777;_inv_tbl_snd = _inv_seq(_tbl_snd)
_tbl_sz_snd = 'STUVW'
_tbl_all_snd = 'ADFGHKMNQRSTUVWY'
777;_flip_snd = str.maketrans(_tbl_all_snd, _tbl_all_snd[::-1])
_tbl_dat = join_between(*'15')+'78'+join_between(*'AY')
    # [1-578A-Y]
777;_flip_dat = str.maketrans(_tbl_dat, _tbl_dat[::-1])
777;_inv_tbl_dat = _inv_seq(_tbl_dat)
_tbl_dat2hex = str.maketrans(_tbl_dat, base32_alplabet)
_tbl_dat5hex = str.maketrans(base32_alplabet, _tbl_dat)
def _uintZbase32_(u, /):
    s = uintZbase32_(u)
    s = s.translate(_tbl_dat5hex)
    return s
def _uintSbase32_(s, /):
    s = s.translate(_tbl_dat2hex)
    u = uintSbase32_(s)
    return u
def _flip(s, /):
    sgn, h = s[:2]
    sgn = _tbl_fst[1-_tbl_fst.index(sgn)]
    h = h.translate(_flip_snd)
    tail = s[2:]
    tail = tail.translate(_flip_dat)
    return f'{sgn}{h}{tail}'
def _dec_head_(s, /):
    c = s[0]
    assert not c == '1'
    k = _inv_tbl_dat[c]
    c = _tbl_dat[k-1]
    return c+s[1:]
def _inc_head_(s, /):
    c = s[0]
    assert not c == 'Y'
    k = _inv_tbl_dat[c]
    c = _tbl_dat[k+1]
    return c+s[1:]
def encode_34_10_32__int_(i, /):
    check_type_is(int, i)
    if i < 0:
        s = encode_34_10_32__int_(-i)
        return _flip(s)
    u = i
    assert u >= 0
    if u < 10:
        c = _tbl_snd[u]
        return '9'+c
    tail = _uintZbase32_(u)
    sz = len(tail)
    if sz <= 5:
        c = _tbl_sz_snd[sz-1]
        return f'9{c}{tail}'
    _neck = _uintZbase32_(sz)
    neck = _dec_head_(_neck)
    n = len(neck)
    cs = 'Y'*n
    return f'9{cs}{neck}{tail}'
def _decode_34_10_32__int_ex_(s, begin, end, /):
    L = end-begin
    if not 2 <= L:raise ValueError
    sgn = s[begin]
    if sgn == '6':
        (u, _next_begin) = _decode_34_10_32__int_ex_(_flip(s[begin:end]), 0, L)
        i = -u
        next_begin = begin +_next_begin
        return (i, next_begin)

    if not sgn == '9':raise ValueError
    h = s[begin+1]
    if h <= 'R':
        #return _tbl_snd.index(h)
        if not h >= 'A': raise ValueError
        try:
            u = _inv_tbl_snd[h]
        except KeyError:
            raise ValueError
        next_begin = begin+2
        return (u, next_begin)

    if h == 'Y':
        for i in range(begin+1, end):
            if not s[i] == 'Y':
                break
        else:
            raise ValueError
        # [begin <= i < end]
        # [s[i] =!= 'Y']
        n = i-(begin+1)
        assert n >= 1
        j = i+n
        if not j <= end:raise ValueError
        neck = s[i:j]
        _neck = _inc_head_(neck)
        sz = _uintSbase32_(_neck)
    else:
        sz = 1 + _tbl_sz_snd.index(h)
            # ^ValueError
        j = begin+2
    j, sz
    k = j+sz
    if not k <= end:raise ValueError
    tail = s[j:k]
    u = _uintSbase32_(tail)
    next_begin = k
    return (u, next_begin)





class _Codes4int_34_10_32(ICodes4int):
    __slots__ = ()
    #___no_slots_ok___ = True
    #@override
    def encode__int_(sf, i, /):
        'int -> str'
        return encode_34_10_32__int_(i)
    #@override
    def _decode__int_ex_(sf, s, begin, end, /):
        'str -> begin/uint -> end/uint -> (int, next_begin)|^ValueError'
        return _decode_34_10_32__int_ex_(s, begin, end)
_codes4int_34_10_32 = _Codes4int_34_10_32()

######################
decode_34_10_32__int_ = _codes4int_34_10_32.decode__int_
decode_34_10_32__int_ex_ = _codes4int_34_10_32.decode__int_ex_

encode_34_10_32__ints_ = _codes4int_34_10_32.encode__ints_
decode_34_10_32__ints_ = _codes4int_34_10_32.decode__ints_
decode_34_10_32__ints_ex_ = _codes4int_34_10_32.decode__ints_ex_
iter_decode_34_10_32__ints_ex_ = _codes4int_34_10_32.iter_decode__ints_ex_
######################
#.def decode_34_10_32__int_(s, begin=None, end=None, /, *, strict=True):
#.    '-> int|^ValueError'
#.    return _codes4int_34_10_32.decode__int_(s, begin, end, strict=strict)
#.def decode_34_10_32__int_ex_(s, begin=None, end=None, /, *, strict=False):
#.    '-> int|^ValueError'
#.    return _codes4int_34_10_32.decode__int_ex_(s, begin, end, strict=strict)
#.def encode_34_10_32__ints_(js, /):
#.    'Iter int -> str'
#.    return _codes4int_34_10_32.encode__ints_(js)
#.def decode_34_10_32__ints_(s, begin=None, end=None, /, *, max_num_ints=None, strict=True):
#.    '-> [int]|^ValueError'
#.    return _codes4int_34_10_32.decode__ints_(s, begin, end, max_num_ints=max_num_ints, strict=strict)
#.def decode_34_10_32__ints_ex_(s, begin=None, end=None, /, *, max_num_ints=None, strict=False):
#.    '-> ([int], next_begin)|^ValueError'
#.    return _codes4int_34_10_32.decode__ints_ex_(s, begin, end, max_num_ints=max_num_ints, strict=strict)
#.def iter_decode_34_10_32__ints_ex_(s, begin=None, end=None, /, *, strict=False):
#.    '-> Iter (int, next_begin)|^ValueError'
#.    return _codes4int_34_10_32.iter_decode__ints_ex_(s, begin, end, strict=strict)

######################
#.def decode_34_10_32__int_(s, begin=None, end=None, /, *, strict=True):
#.    '-> int|^ValueError'
#.    (j, next_begin) = decode_34_10_32__int_ex_(s, begin, end, strict=strict)
#.    return j
#.def decode_34_10_32__int_ex_(s, begin=None, end=None, /, *, strict=False):
#.    '-> (int, next_begin)|^ValueError'
#.    (begin, end) = mk_seq_rng(s, begin, end)
#.    if not begin < end:raise ValueError
#.    r = _decode_34_10_32__int_ex_(s, begin, end)
#.    if strict:
#.        (j, next_begin) = r
#.        if not next_begin == end:raise ValueError
#.    return r
#.
#.
#.def encode_34_10_32__ints_(js, /):
#.    return ''.join(map(encode_34_10_32__int_, js))
#.def decode_34_10_32__ints_(s, begin=None, end=None, /, *, max_num_ints=None, strict=True):
#.    '-> [int]|^ValueError'
#.    (js, next_begin) = decode_34_10_32__ints_ex_(s, begin, end, max_num_ints=max_num_ints, strict=strict)
#.    return js
#.def decode_34_10_32__ints_ex_(s, begin=None, end=None, /, *, max_num_ints=None, strict=False):
#.    '-> ([int], next_begin)|^ValueError'
#.    (begin, end) = mk_seq_rng(s, begin, end)
#.        #=> init:next_begin&&strict-check
#.    it = iter_decode_34_10_32__ints_ex_(s, begin, end, strict=strict)
#.    if not max_num_ints is None:
#.        it = islice(it, 0, max_num_ints)
#.    js = []
#.    next_begin = begin
#.    for (j, next_begin) in it:
#.        js.append(j)
#.    if strict:
#.        if not next_begin == end:raise ValueError
#.    js = tuple(js)
#.    return (js, next_begin)
#.def iter_decode_34_10_32__ints_ex_(s, begin=None, end=None, /, *, strict=False):
#.        '-> Iter (int, next_begin)|^ValueError'
#.    (begin, end) = mk_seq_rng(s, begin, end)
#.    if not begin <= end:raise ValueError
#.    try:
#.        while not begin == end:
#.            r = _decode_34_10_32__int_ex_(s, begin, end)
#.                #^ValueError
#.            yield r
#.            (j, next_begin) = r
#.            begin = next_begin
#.    except ValueError:
#.        if strict:
#.            raise
#.        else:
#.            pass
#.    #yield (True, begin)



__all__
from seed.int_tools.digits.codecs4int__alnum import *
