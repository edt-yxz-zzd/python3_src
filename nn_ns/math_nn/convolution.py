#__all__:goto
r'''[[[
py -m nn_ns.app.debug_cmd   nn_ns.math_nn.convolution
py -m nn_ns.math_nn.convolution


from nn_ns.math_nn.convolution import convolve__seq, inv_convolve__seq
from nn_ns.math_nn.convolution import convolve__uint8bits__littleendian, inv_convolve__uint8bits__littleendian


e ../../python3_src/nn_ns/math_nn/convolution.py




卷积math/singal-processing/image-processing: convolve+convolution,not convolute
反卷积deconvolve+deconvolution
    逆操作，卷积不一定可逆
    即使可逆，也很可能无限长

一维卷积定义:
convolve(F, G) =[def]=
    = \k -> sum F[i]*G[k-i] {i}
    = \k -> sum F[i]*G[j] {i+j=k}
  可交换commutative
cross_correlation(F,G) =[def]=
    = \k -> sum F[i]*complex_conjugate(G[i-k]) {i}
    = \k -> sum F[i]*complex_conjugate(G[j]) {i-j=k}
  不可交换
autocorrelation(F) =[def]=
    = cross_correlation(F, F)




卷积<==>一元多项式乘法
  polynomial(xs <*> ys) = polynomial(xs) * polynomial(ys)
    polynomial(xs) = \z -> sum xs[i]*z**i {i}



卷积 满足 交换律
  (xs <*> ys)
    = (\k->sum~ xs[i]ys[k-i] {i})
    = (\k->sum~ xs[i]ys[j] {i+j==k})
    = (ys <*> xs)

卷积 满足 结合律
  (xs <*> ys) <*> zs
    = (\k->sum~ xs[i]ys[k-i] {i}) <*> zs
    = (\n->sum~ sum~ xs[i]ys[k-i] {i} * zs[n-k] {k})
    = (\n->sum~ sum~ xs[i]ys[k-i] * zs[n-k] {i} {k})
    = (\n->sum~ xs[i]ys[j] * zs[k] {i+j+k==n})
    = xs <*> (ys <*> zs)

可逆卷积
  ys = xs <*> ms
  xs = ys <*> ws
      = xs <*> ms <*> ws
      = xs <*> (ms <*> ws) #结合律
  I = \k->[k==0]
  !!xs = xs <*> I
  (ms <*> ws) == I
  ws = inv(ms)


convolve__seq :: [a] -> [a] -> [a]
convolve__bits :: uint -> uint -> uint




>>> sum([[]])
Traceback (most recent call last):
  ...
TypeError: unsupported operand type(s) for +: 'int' and 'list'


>>> from functools import reduce
>>> import operator as opss
>>> reduce(opss.__add__, [], 2)
2
>>> reduce(opss.__add__, [])
Traceback (most recent call last):
  ...
TypeError: reduce() of empty sequence with no initial value
>>> reduce(opss.__add__, [[]])
[]
>>> reduce(opss.__add__, [[]], 2)
Traceback (most recent call last):
  ...
TypeError: unsupported operand type(s) for +: 'int' and 'list'
>>> int('', 2)
Traceback (most recent call last):
  ...
ValueError: invalid literal for int() with base 2: ''
>>> 'abc'[0:-1:-1]
''
>>> 'abc'[0::-1]
'a'
>>> 'abc'[0:0:-1]
''
>>> 'abc'[0:-2:-1]
''
>>> [3,4,5][0:-1:-1]
[]










>>> convolve__bits = lambda u,v,/, *, result_length_le=None:bin(convolve__uint8bits__littleendian(u,v, __add__=None, __mul__=None, result_length_le=result_length_le, tmay_zero4padding=(0,)))
>>> convolve__bits(0, 0)
'0b0'
>>> convolve__bits(1, 0)
'0b0'
>>> convolve__bits(0, 1)
'0b0'
>>> convolve__bits(0b1011, 0)
'0b0'
>>> convolve__bits(0, 0b1011)
'0b0'
>>> convolve__bits(0b1100111, 0b1011)
'0b1110010001'
>>> convolve__bits(0b1011, 0b1100111)
'0b1110010001'




>>> inv_convolve__bits = lambda u,/,*, result_length_le=None:bin(inv_convolve__uint8bits__littleendian(u, __add__=None, __mul__=None, __neg__=None, __eq__=None, inv_head_element=None, result_length_le=result_length_le, validate=True))

>>> result_length = 0b1011 .bit_length()
>>> inv_convolve__bits(0b1011)
'0b111'
>>> convolve__bits(0b1011, 0b111)
'0b110001'
>>> convolve__bits(0b1011, 0b111)[-result_length:]
'0001'
>>> convolve__bits(0b1011, 0b1100111)
'0b1110010001'
>>> convolve__bits(0b1110010001, 0b111)
'0b101011110111'

>>> u = 0b1100111
>>> result_length = u .bit_length()
>>> inv_convolve__bits(0b1011, result_length_le=result_length)
'0b10111'
>>> convolve__bits(0b1011, 0b10111)
'0b10000001'
>>> convolve__bits(0b1011, 0b10111)[-result_length:]
'0000001'
>>> convolve__bits(0b1011, u)
'0b1110010001'
>>> convolve__bits(0b1110010001, 0b10111)
'0b11001111100111'
>>> convolve__bits(0b1110010001, 0b10111)[-result_length:]
'1100111'

#]]]'''


__all__ = r'''
    convolve__seq
        convolve__uint8bits__littleendian
    inv_convolve__seq
        inv_convolve__uint8bits__littleendian











    iter_convolve__seq
        convolve__seq
        calc_default_result_length4convolve__seq
            calc_default_result_length4convolve__seq_len

        iter_convolve__uint8bits__littleendian
            convolve__uint8bits__littleendian
    iter_inv_convolve__seq
        inv_convolve__seq
            inv_convolve__uint8bits__littleendian

    uint2bits__bigendian__str
    uint5bits__bigendian__str
        uint2bits__bigendian__bytes
        uint5bits__bigendian__bytes
            reverse__bytes
            uint2bits__littleendian__bytes
            uint5bits__littleendian__bytes
    cut__uint8bits
    '''.split()


from functools import reduce
from itertools import islice, repeat, chain
import operator as opss
from seed.tiny import echo
from seed.tiny import check_uint, check_str, check_callable, check_tmay
from seed.tiny import print_err


def convolve__seq(lhs, rhs, /, *, __add__, __mul__, key, result_length, tmay_zero4padding, mk_result5iter):
    sz_lhs = len(lhs)
    sz_rhs = len(rhs)
    if mk_result5iter is None:
        mk_result5iter = tuple
    check_callable(mk_result5iter)

    it = iter_convolve__seq(lhs, rhs, __add__=__add__, __mul__=__mul__, key=key, result_length=result_length, tmay_zero4padding=tmay_zero4padding)
    ls = mk_result5iter(it)
    if result_length is None:
        result_length = calc_default_result_length4convolve__seq(lhs, rhs)
    if not len(ls) == result_length: raise ValueError(f'result_length too big: result_length={result_length} > {len(ls)}')

    return ls


def calc_default_result_length4convolve__seq(lhs, rhs, /):
    sz_lhs = len(lhs)
    sz_rhs = len(rhs)
    result_length = calc_default_result_length4convolve__seq_len(sz_lhs, sz_rhs)
    return result_length
def calc_default_result_length4convolve__seq_len(sz_lhs, sz_rhs, /):
    result_length = sz_lhs+sz_rhs-1 if sz_lhs and sz_rhs else 0
    return result_length
def iter_convolve__seq(lhs, rhs, /, *, __add__, __mul__, key, result_length, tmay_zero4padding):
    # len(result) == max(0, sz_lhs+sz_rhs-1)
    if __add__ is None:
        __add__ = opss.__add__
    if __mul__ is None:
        __mul__ = opss.__mul__
    if key is None:
        key = echo

    max_result_length = calc_default_result_length4convolve__seq(lhs, rhs)
    if result_length is None:
        result_length = max_result_length
    check_uint(result_length)
    check_tmay(tmay_zero4padding)

    if result_length > max_result_length and not tmay_zero4padding: raise TypeError

    it = _iter_convolve__seq(lhs, rhs, __add__=__add__, __mul__=__mul__, key=key)
    if result_length > max_result_length:
        [zero] = tmay_zero4padding
        it = chain(it, repeat(zero, result_length-max_result_length))
    elif result_length < max_result_length:
        it = islice(it, result_length)
    return it


def _iter_convolve__seq(lhs, rhs, /, *, __add__, __mul__, key):
    sz_lhs = len(lhs)
    sz_rhs = len(rhs)
    if not (sz_lhs and sz_rhs):
        return
    r'''
    [0 <= i <= sz_lhs-1]
    [0 <= j <= sz_rhs-1]
    [i+j == k]
    ==>> [0 <= k <= sz_lhs+sz_rhs-2]

    [given k]:
        !![i+j == k]
        [j == k-i]
        !![0 <= j <= sz_rhs-1]
        [0 <= k-i <= sz_rhs-1]
        [k-(sz_rhs-1) <= i <= k-0]
        [k+1-sz_rhs <= i <= k]
        !![0 <= i <= sz_lhs-1]
        [max(0,k+1-sz_rhs) <= i <= min(k,sz_lhs-1)]

    #'''

    for k in range(sz_lhs+sz_rhs-1):
        us = range(max(0, k+1-sz_rhs), min(k+1, sz_lhs))
        if 0b00:
            3,7,4,7
            print_err(len(us))
            print_err(k)
            print_err(sz_lhs)
            print_err(sz_rhs)
        #bug:assert len(us) == min(k+1, sz_lhs, sz_rhs)
        assert (0 <= k < max(sz_lhs, sz_rhs) and len(us) == min(k+1, sz_lhs, sz_rhs)) ^ (k >= max(sz_lhs, sz_rhs) and len(us) == sz_lhs + sz_rhs -1 -k)
        assert len(us)
        lhs_ = lhs[us.start:us.stop]
        #bug:rhs_ = rhs[k-us.start:k-us.stop:-1]
        if k - us.stop == -1:
            rhs_ = rhs[k-us.start::-1]
        else:
            rhs_ = rhs[k-us.start:k-us.stop:-1]

        if 0b00:
            print_err(rhs)
            print_err(rhs_)
            print_err(k, us)
            print_err(k-us.start, k-us.stop)
        assert len(lhs_)
            #TypeError: reduce() of empty sequence with no initial value
        assert len(lhs_) == len(us)
        assert len(lhs_) == len(rhs_)

        lhs_ = map(key, lhs_)
        rhs_ = map(key, rhs_)
        y_k = reduce(__add__, map(__mul__, lhs_, rhs_))
        yield y_k
    return

def uint2bits__bigendian__str(u, /):
    check_uint(u)
    if u==0:
        s = ''
    else:
        s = f'{u:b}'
    return s
def uint5bits__bigendian__str(s, /):
    check_str(s)
    if not s:
        u = 0
    else:
        u = int(s, 2)
    check_uint(u)
    return u
def uint2bits__bigendian__bytes(u, /):
    #bug:return uint2bits__bigendian__str(u).encode('ascii')
    return bytes(map(int, uint2bits__bigendian__str(u)))
    return bytes(map('1'.__eq__, uint2bits__bigendian__str(u)))
def uint5bits__bigendian__bytes(bs, /):
    #bug:return uint5bits__bigendian__str(bs.decode('ascii'))
    #bug:return uint5bits__bigendian__str(map(str, bs))
    #xxx:return uint5bits__bigendian__str(''.join(bs))
    return uint5bits__bigendian__str(''.join(map(str, bs)))
def reverse__bytes(bs, /):
    return bytes(reversed(bs))
def uint2bits__littleendian__bytes(u, /):
    return reverse__bytes(uint2bits__bigendian__bytes(u))
def uint5bits__littleendian__bytes(bs, /):
    return uint5bits__bigendian__bytes(reverse__bytes(bs))

def iter_convolve__uint8bits__littleendian(lhs, rhs, /, *, __add__, __mul__, result_length_le, tmay_zero4padding):
    if __add__ is None:
        __add__ = int.__xor__
    if __mul__ is None:
        __mul__ = int.__and__

    check_uint(lhs)
    check_uint(rhs)

    lhs = uint2bits__littleendian__bytes(lhs)
    rhs = uint2bits__littleendian__bytes(rhs)
    return iter_convolve__seq(lhs, rhs, __add__=__add__, __mul__=__mul__, key=None, result_length=result_length_le, tmay_zero4padding=tmay_zero4padding)

def convolve__uint8bits__littleendian(lhs, rhs, /, *, __add__, __mul__, result_length_le, tmay_zero4padding):
    if 0:
        max_result_length = calc_default_result_length4convolve__seq_len(lhs.bit_length(), rhs.bit_length()) if lhs and rhs else 0
        result_length_le = min(result_length_le, max_result_length)
        #... ...
    it = iter_convolve__uint8bits__littleendian(lhs, rhs, __add__=__add__, __mul__=__mul__, result_length_le=result_length_le, tmay_zero4padding=tmay_zero4padding)
    bs = bytes(it)
    u = uint5bits__littleendian__bytes(bs)
    check_uint(u)
    assert (result_length_le is None and u.bit_length() == lhs.bit_length()+rhs.bit_length()-1 or (u == 0 ==min(lhs,rhs))) or (result_length_le is not None and u.bit_length() <= result_length_le)
        # 『u.bit_length() <= result_length_le』
        #       『<=』since MSB may be 0
    return u


def iter_inv_convolve__seq(ms, /, *, __add__, __mul__, __neg__, __eq__, inv_head_element):
    if not ms: raise TypeError
    head = ms[0]
    inv4head = inv_head_element(head)
    one = __mul__(inv4head, head)
    zero = __add__(__neg__(one), one)
    if __debug__:
        two = __add__(one, one)
        if not __eq__(__mul__(one, zero), zero): raise TypeError
        if not __eq__(__mul__(one, one), one): raise TypeError
        if not __eq__(__mul__(one, two), two): raise TypeError

        if not __eq__(__mul__(zero, zero), zero): raise TypeError
        if not __eq__(__mul__(zero, one), zero): raise TypeError
        if not __eq__(__mul__(zero, two), zero): raise TypeError

    _ms = ms[1:]
    #ys = [one, zero, zero, ..]
    ws = [inv4head]
    yield inv4head
    #for _ in range(len(_ms)):
    while 1:
        _y = reduce(__add__, map(__mul__, _ms, reversed(ws)))
        # 0 = y = _y + ?*head
        # ? = (0-_y)*inv4head
        w = __mul__(__neg__(_y), inv4head)
        ws.append(w)
        yield w
    return
def inv_convolve__seq(ms, /, *, __add__, __mul__, __neg__, __eq__, inv_head_element, result_length, validate):
    if result_length is None:
        result_length = len(ms)
    check_uint(result_length)

    ws = iter_inv_convolve__seq(ms, __add__=__add__, __mul__=__mul__, __neg__=__neg__, __eq__=__eq__, inv_head_element=inv_head_element)
    ws = (*islice(ws, result_length),)
    assert len(ws) == result_length

    if validate:
        if not ms: raise TypeError
        head = ms[0]
        inv4head = inv_head_element(head)
        one = __mul__(inv4head, head)
        zero = __add__(__neg__(one), one)
        #
        ys = [zero]*result_length
        ys[0] = one
        [*ys_] = iter_convolve__seq(ws, ms, __add__=__add__, __mul__=__mul__, key=None, result_length=result_length, tmay_zero4padding=(zero,))
        #print_err(ys)
        #print_err(ys_)
        #assert ys == ys_#[:result_length]
        if not ys == ys_: raise logic-err
    return ws


def inv_convolve__uint8bits__littleendian(u, /, *, __add__, __mul__, __neg__, __eq__, inv_head_element, result_length_le, validate):
    if __add__ is None:
        __add__ = int.__xor__
    if __mul__ is None:
        __mul__ = int.__and__
    if __eq__ is None:
        __eq__ = int.__eq__
    if __neg__ is None:
        __neg__ = echo
    if inv_head_element is None:
        inv_head_element = echo # 1->1

    ms = uint2bits__littleendian__bytes(u)
    ws = inv_convolve__seq(ms, __add__=__add__, __mul__=__mul__, __neg__=__neg__, __eq__=__eq__, inv_head_element=inv_head_element, result_length=result_length_le, validate=False)
    v = uint5bits__littleendian__bytes(ws)
    if validate:
        if result_length_le is None:
            result_length_le = u.bit_length()
        if not 1 == convolve__uint8bits__littleendian(u, v, __add__=__add__, __mul__=__mul__, result_length_le=result_length_le, tmay_zero4padding=()): raise logic-err
        #assert 1 == cut__uint8bits(result_length_le, convolve__uint8bits__littleendian(u, v, __add__=__add__, __mul__=__mul__, result_length_le=None, tmay_zero4padding=()))
    return v

def cut__uint8bits(result_length_le, u, /):
    check_uint(u)
    check_uint(result_length_le)
    return ((1<<result_length_le)-1) & u
        # 『result.bit_length() <= result_length_le』
        #       『<=』since MSB may be 0



if __name__ == "__main__":
    import doctest
    doctest.testmod()

