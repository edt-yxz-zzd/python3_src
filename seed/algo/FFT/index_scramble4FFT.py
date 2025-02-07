#__all__:goto
r'''[[[
e ../../python3_src/seed/algo/FFT/index_scramble4FFT.py
bit reversal -> digit reversal
    [TIME(FFT__bit_scramble__len_is_zpow__inplace(neg, add, mul; xs)) = O(L*log2(L))*TIME(mul+add+neg)]
    [TIME(FFT__idx_digit_reverse__inplace(neg, add, mul; radixes; xs)) = O(L*sum(radixes))*TIME(mul+add) where [L==II(radixes)==len(xs)]]

seed.algo.FFT.index_scramble4FFT
py -m nn_ns.app.debug_cmd   seed.algo.FFT.index_scramble4FFT -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.algo.FFT.index_scramble4FFT:__doc__ -ht # -ff -df

[[
FFT:
    原版:递归:每一层都需要移动输入
    改版:循环:址引初始一次变换后，不需要再移动输入
        --> (FFT, in-place, in-order loop forms with bit-scramble)
def FFT__original__len_is_zpow(g, xs):
    if len(xs) == 1:
        return [*xs]
    gg = g**2
    ys = FFT(gg, xs[0::2])
    zs = FFT(gg, xs[1::2])
        # idx:lowest bit <-> highest bit
    gs = [g**k for k in range(len(xs))]
    _gzs = gs .* zs
    rs = (ys .+ _gzs) ++ (ys .- _gzs)
    return rs
def FFT__bit_scramble__len_is_zpow__inplace(g, xs):
    L = len(xs)
    sz4bits = L.bit_length()-1
    for i in range(L):
        j = bit_scramble_(L,i)
        if i < j:
            xs[i], xs[j] = xs[j], xs[i]
    for ez in range(1, 1+sz4bits):
        sz = 2**ez
        gg = g**(L//sz)
        for i in range(0,L,sz):
            # [i..<i+sz]
            # ys = xs[i:i+sz//2]
            # zs = xs[i+sz//2:i+sz]
            h = sz>>1
            j = i+h
            for k in range(h):
                y = xs[i+k]
                z = xs[j+k]
                gz = z*gg**k
                xs[i+k] = y+gz
                xs[j+k] = y-gz
    return xs

泛化版:变基数FFT:radixes:reverse_digit4uint_
]]



>>> sz4bits = 8
>>> radixes = [2]*sz4bits
>>> L = 2**sz4bits
>>> for u in range(L):
...     assert bit_scramble_(sz4bits,bit_scramble_(sz4bits,u)) == u
>>> for u in range(L):
...     assert bit_scramble_(sz4bits,u) == reverse_digit4uint_(radixes,u)

>>> radixes = [2,3,5,7]
>>> L = 2*3*5*7
>>> for u in range(L):
...     assert reverse_digit4uint_(radixes[::-1], v:=reverse_digit4uint_(radixes,u)) == u, (u, v)
>>> uint2reversed_digits_(radixes, 1)
[1, 0, 0, 0]
>>> uint2reversed_digits_(radixes[::-1], 1)
[1, 0, 0, 0]
>>> uint2reversed_digits_(radixes[::-1], 105)
[1, 1, 2, 3]
>>> uint2reversed_digits_(radixes, 105)
[0, 0, 0, 1]


>>> L = 3
>>> for u in range(2**L):
...     bit_scramble_(L,u)
0
4
2
6
1
5
3
7

>>> radixes = [2,3]
>>> L = 2*3
>>> for u in range(L):
...     reverse_digit4uint_(radixes,u)
0
2
4
1
3
5

# reverse_digit4uint_([2,3],1)=>[1-->2-->4-->3-->1] 并非回旋函数，导致bug@FFT__idx_digit_reverse__inplace
>>> reverse_digit4uint_(radixes,1)
2
>>> reverse_digit4uint_(radixes,2)
4
>>> reverse_digit4uint_(radixes,4)
3
>>> reverse_digit4uint_(radixes,3)
1
>>> reverse_digit4uint_(radixes,0)
0
>>> reverse_digit4uint_(radixes,5)
5
>>> for u in range(L):
...     reverse_digit4uint_(radixes[::-1],u)
0
3
1
4
2
5

>>> radixes = [2,3,5]
>>> L = 2*3*5
>>> [reverse_digit4uint_(radixes,u) for u in range(L)]
[0, 6, 12, 18, 24, 2, 8, 14, 20, 26, 4, 10, 16, 22, 28, 1, 7, 13, 19, 25, 3, 9, 15, 21, 27, 5, 11, 17, 23, 29]
>>> [reverse_digit4uint_(radixes[::-1],u) for u in range(L)]
[0, 15, 5, 20, 10, 25, 1, 16, 6, 21, 11, 26, 2, 17, 7, 22, 12, 27, 3, 18, 8, 23, 13, 28, 4, 19, 9, 24, 14, 29]


view ../../python3_src/nn_ns/math_nn/numbers/_patch_prime_..b001918.b002233.out.txt
6 17 3 3
54 257 3 3

10 31 3 3
46 211 2 2

>>> [pow(x, 8, 17) for x in range(17)]
[0, 1, 1, 16, 1, 16, 16, 16, 1, 1, 16, 16, 16, 1, 16, 1, 1]
>>> pow(3, 8, 17) -17
-1
>>> pow(3, 128, 257) -257
-1


def _prepare4mod_prime_(modulus, g, sz=None, /):
>>> (modulus, g) = (17, 3)
>>> (neg, add, mul, g, inv_g, sz, inv_len, radixes) = _prepare4mod_prime_(modulus, g)
>>> (g, inv_g, sz, inv_len, radixes)
(3, 6, 16, 16, [2, 2, 2, 2])

>>> xs = [*range(sz)]
>>> xs
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
>>> rs = FFT__original__len_is_zpow(neg, add, mul, g, xs)
>>> rs
[1, 8, 2, 15, 7, 4, 6, 5, 9, 13, 12, 14, 11, 3, 16, 10]
>>> _xs = IFFT_(FFT__original__len_is_zpow, neg, add, mul, inv_g, inv_len, rs)
>>> _xs
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
>>> _xs == xs
True


>>> xs = [*range(sz)]
>>> xs
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
>>> FFT__bit_scramble__len_is_zpow__inplace(neg, add, mul, g, xs)
[1, 8, 2, 15, 7, 4, 6, 5, 9, 13, 12, 14, 11, 3, 16, 10]
>>> xs is _
True
>>> xs
[1, 8, 2, 15, 7, 4, 6, 5, 9, 13, 12, 14, 11, 3, 16, 10]
>>> xs == rs
True
>>> IFFT_(FFT__bit_scramble__len_is_zpow__inplace, neg, add, mul, inv_g, inv_len, xs)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
>>> xs is _
True
>>> xs == _xs
True

>>> xs = [*range(sz)[sz//2:], *range(sz)[:sz//2]]
>>> xs
[8, 9, 10, 11, 12, 13, 14, 15, 0, 1, 2, 3, 4, 5, 6, 7]
>>> FFT__bit_scramble__len_is_zpow__inplace(neg, add, mul, g, xs)
[1, 9, 2, 2, 7, 13, 6, 12, 9, 4, 12, 3, 11, 14, 16, 7]
>>> xs
[1, 9, 2, 2, 7, 13, 6, 12, 9, 4, 12, 3, 11, 14, 16, 7]
>>> IFFT_(FFT__bit_scramble__len_is_zpow__inplace, neg, add, mul, inv_g, inv_len, xs)
[8, 9, 10, 11, 12, 13, 14, 15, 0, 1, 2, 3, 4, 5, 6, 7]
>>> xs
[8, 9, 10, 11, 12, 13, 14, 15, 0, 1, 2, 3, 4, 5, 6, 7]


>>> radixes = [2,2,2,2]
>>> FFT__idx_digit_reverse__inplace(neg, add, mul, g, xs, may_radixes=radixes)
[1, 9, 2, 2, 7, 13, 6, 12, 9, 4, 12, 3, 11, 14, 16, 7]
>>> IFFT_(FFT__idx_digit_reverse__inplace, neg, add, mul, inv_g, inv_len, xs, may_radixes=radixes)
[8, 9, 10, 11, 12, 13, 14, 15, 0, 1, 2, 3, 4, 5, 6, 7]




>>> (modulus, g) = (3, 2)
>>> (neg, add, mul, g, inv_g, sz, inv_len, radixes) = _prepare4mod_prime_(modulus, g)
>>> xs = [1, 2]
>>> FFT__bit_scramble__len_is_zpow__inplace(neg, add, mul, g, xs)
[0, 2]
>>> IFFT_(FFT__bit_scramble__len_is_zpow__inplace, neg, add, mul, inv_g, inv_len, xs)
[1, 2]

>>> xs = [1, 1]
>>> FFT__bit_scramble__len_is_zpow__inplace(neg, add, mul, g, xs)
[2, 0]
>>> IFFT_(FFT__bit_scramble__len_is_zpow__inplace, neg, add, mul, inv_g, inv_len, xs)
[1, 1]




[[1, 1, 1, 1]
,[1, 2, 4, 3]
,[1, 4, 1, 4]
,[1, 3, 4, 2]
]
>>> (modulus, g) = (5, 2)
>>> (neg, add, mul, g, inv_g, sz, inv_len, radixes) = _prepare4mod_prime_(modulus, g)
>>> xs = [1, 3, 2, 4]
>>> FFT__bit_scramble__len_is_zpow__inplace(neg, add, mul, g, xs)
[0, 2, 1, 1]
>>> IFFT_(FFT__bit_scramble__len_is_zpow__inplace, neg, add, mul, inv_g, inv_len, xs)
[1, 3, 2, 4]

>>> xs = [1, 3, 2, 4]
>>> rs = FFT__native(neg, add, mul, g, xs)
>>> rs
[0, 2, 1, 1]
>>> xs
[1, 3, 2, 4]
>>> IFFT_(FFT__native, neg, add, mul, inv_g, inv_len, rs)
[1, 3, 2, 4]


>>> radixes = [2,2]
>>> FFT__idx_digit_reverse__inplace(neg, add, mul, g, xs, may_radixes=radixes)
[0, 2, 1, 1]
>>> IFFT_(FFT__idx_digit_reverse__inplace, neg, add, mul, inv_g, inv_len, xs, may_radixes=radixes)
[1, 3, 2, 4]




>>> (modulus, g, radixes) = (31, 3, [2,3,5])
>>> (neg, add, mul, g, inv_g, sz, inv_len, radixes) = _prepare4mod_prime_(modulus, g)
>>> xs = [1, 3, 2, 4, *range(26)]
>>> FFT__idx_digit_reverse__inplace(neg, add, mul, g, xs, may_radixes=radixes)
[25, 23, 25, 29, 3, 3, 0, 3, 12, 21, 3, 13, 8, 29, 2, 14, 20, 6, 20, 7, 8, 25, 11, 21, 10, 0, 23, 16, 10, 12]
>>> IFFT_(FFT__idx_digit_reverse__inplace, neg, add, mul, inv_g, inv_len, xs, may_radixes=radixes)
[1, 3, 2, 4, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]


>>> xs = [1, 3, 2, 4, *range(26)]
>>> rs = FFT__native(neg, add, mul, g, xs)
>>> rs
[25, 23, 25, 29, 3, 3, 0, 3, 12, 21, 3, 13, 8, 29, 2, 14, 20, 6, 20, 7, 8, 25, 11, 21, 10, 0, 23, 16, 10, 12]
>>> IFFT_(FFT__native, neg, add, mul, inv_g, inv_len, rs)
[1, 3, 2, 4, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

>>> (modulus, g, radixes) = (7, 3, [2,3])
>>> (neg, add, mul, g, inv_g, sz, inv_len, radixes) = _prepare4mod_prime_(modulus, g)
>>> xs = [1, 3, 2, 4, 6, 6]
>>> rs = FFT__native(neg, add, mul, g, xs)
>>> rs
[1, 1, 6, 3, 1, 1]
>>> IFFT_(FFT__native, neg, add, mul, inv_g, inv_len, rs)
[1, 3, 2, 4, 6, 6]

>>> FFT__idx_digit_reverse__inplace(neg, add, mul, g, xs, may_radixes=radixes)
[1, 1, 6, 3, 1, 1]
>>> IFFT_(FFT__idx_digit_reverse__inplace, neg, add, mul, inv_g, inv_len, xs, may_radixes=radixes)
[1, 3, 2, 4, 6, 6]


>>> (modulus, g, radixes) = (211, 2, [2,3,5,7])
>>> (neg, add, mul, g, inv_g, sz, inv_len, radixes) = _prepare4mod_prime_(modulus, g)
>>> xs = [1, 3, 2, 4, 6, 6, *range(204)]
>>> rs = FFT__native(neg, add, mul, g, xs)
>>> rs
[50, 32, 163, 142, 112, 55, 208, 40, 81, 53, 162, 122, 48, 38, 121, 106, 130, 137, 44, 59, 93, 88, 161, 119, 115, 156, 150, 56, 82, 87, 176, 152, 73, 54, 182, 1, 8, 52, 190, 104, 173, 3, 128, 196, 160, 157, 56, 89, 14, 20, 25, 124, 151, 201, 88, 16, 180, 106, 131, 128, 166, 72, 123, 61, 181, 206, 148, 208, 117, 91, 22, 75, 183, 86, 81, 85, 52, 201, 186, 35, 16, 97, 28, 32, 136, 15, 204, 195, 24, 102, 183, 70, 188, 59, 135, 19, 34, 94, 121, 1, 134, 176, 26, 18, 187, 105, 4, 158, 210, 89, 48, 153, 102, 205, 88, 36, 57, 108, 137, 88, 58, 47, 208, 202, 75, 47, 187, 163, 14, 134, 113, 11, 42, 188, 123, 178, 84, 172, 154, 179, 189, 172, 185, 187, 97, 200, 131, 119, 114, 145, 161, 116, 172, 55, 106, 75, 166, 3, 135, 104, 26, 104, 38, 52, 161, 173, 172, 195, 0, 75, 51, 9, 127, 94, 118, 1, 193, 194, 110, 147, 109, 70, 73, 195, 141, 181, 128, 154, 90, 157, 92, 105, 127, 140, 152, 198, 99, 123, 171, 107, 16, 84, 80, 30, 61, 152, 157, 36, 195, 115]
>>> IFFT_(FFT__native, neg, add, mul, inv_g, inv_len, rs) == [1, 3, 2, 4, 6, 6, *range(204)]
True


#non-inplace
>>> xs == [1, 3, 2, 4, 6, 6, *range(204)]
True
>>> FFT__idx_digit_reverse(neg, add, mul, g, xs, may_radixes=radixes) == rs
True
>>> IFFT_(FFT__idx_digit_reverse, neg, add, mul, inv_g, inv_len, rs, may_radixes=radixes) == xs
True

#non-inplace,without-radixes
>>> xs == [1, 3, 2, 4, 6, 6, *range(204)]
True
>>> FFT__idx_digit_reverse(neg, add, mul, g, xs) == rs
True
>>> IFFT_(FFT__idx_digit_reverse, neg, add, mul, inv_g, inv_len, rs) == xs
True


#inplace,with-radixes
>>> FFT__idx_digit_reverse__inplace(neg, add, mul, g, xs, may_radixes=radixes) == rs
True
>>> IFFT_(FFT__idx_digit_reverse__inplace, neg, add, mul, inv_g, inv_len, xs, may_radixes=radixes) == [1, 3, 2, 4, 6, 6, *range(204)]
True






>>> (neg, add, mul, g, xs, inv_g, inv_len, rs) = (None, None, None, None, [], None, None, [])
>>> (modulus, g) = (1, 0)
>>> (neg, add, mul, g, inv_g, sz, inv_len, may_radixes) = _prepare4mod_prime_(modulus, g)
>>> FFT__native(neg, add, mul, g, xs)
[]
>>> IFFT_(FFT__native, neg, add, mul, inv_g, inv_len, rs)
[]

>>> FFT__original__len_is_zpow(neg, add, mul, g, xs)
Traceback (most recent call last):
    ...
ValueError: 0
>>> FFT__bit_scramble__len_is_zpow(neg, add, mul, g, xs)
Traceback (most recent call last):
    ...
ValueError: 0
>>> FFT__idx_digit_reverse(neg, add, mul, g, xs)
Traceback (most recent call last):
    ...
ValueError: 0

>>> (modulus, g, radixes) = (2, 1, [])
>>> (neg, add, mul, g, inv_g, sz, inv_len, radixes) = _prepare4mod_prime_(modulus, g)
>>> xs = rs = [1]
>>> FFT__native(neg, add, mul, g, xs)
[1]
>>> IFFT_(FFT__native, neg, add, mul, inv_g, inv_len, rs)
[1]


>>> FFT__original__len_is_zpow(neg, add, mul, g, xs)
[1]
>>> IFFT_(FFT__original__len_is_zpow, neg, add, mul, inv_g, inv_len, rs)
[1]

>>> FFT__bit_scramble__len_is_zpow(neg, add, mul, g, xs)
[1]
>>> IFFT_(FFT__bit_scramble__len_is_zpow, neg, add, mul, inv_g, inv_len, rs)
[1]

>>> FFT__idx_digit_reverse(neg, add, mul, g, xs)
[1]
>>> IFFT_(FFT__idx_digit_reverse, neg, add, mul, inv_g, inv_len, rs)
[1]






def FFT__idx_digit_reverse__inplace__mod_(modulus, g, xs, /, **kwds):
py_adhoc_call   seed.algo.FFT.index_scramble4FFT   @FFT__idx_digit_reverse__inplace__mod_ =7 --may_radixes='[2,3]' =3 ='[1, 3, 2, 4, 6, 6]'


]]]'''#'''
__all__ = r'''
reverse_digit4uint_
    uint2digits_
        uint2reversed_digits_
    uint5digits_
bit_scramble_
    uint5bits_
    uint2bits_

IFFT_
FFT__native
FFT__original__len_is_zpow
FFT__bit_scramble__len_is_zpow__inplace
    FFT__bit_scramble__len_is_zpow
FFT__idx_digit_reverse__inplace
    FFT__idx_digit_reverse

mk_neg_add_mul_inv4mod_
    FFT__idx_digit_reverse__inplace__mod_
        FFT__idx_digit_reverse__mod_

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from functools import reduce
from seed.math.factor_pint.factor_pint__naive_brute_force import flatten_list_factor_pint__naive_brute_force_# flatten_iter_factor_pint__naive_brute_force_
#.from seed.tiny_.check import check_type_is, check_int_ge
#.from itertools import islice
#.
___end_mark_of_excluded_global_names__0___ = ...


def uint2digits_(radixes, u, /):
    'radixes/[uint{>=2}] -> u/uint%II(radixes) -> digits/[uint%radix for radix in radixes]'
    digits = uint2reversed_digits_(radixes, u)
    digits.reverse()
    return digits
def uint2reversed_digits_(radixes, u, /):
    'radixes/[uint{>=2}] -> u/uint%II(radixes) -> digits/[uint%radix for radix in radixes[::-1]]'
    if not u >= 0: raise ValueError(radixes, u)
    u0 = u
    digits = []
    for radix in radixes[::-1]:
        u, digit = divmod(u, radix)
        digits.append(digit)
    if not u == 0: raise ValueError(radixes, u0)
    return digits
def uint5digits_(radixes, digits, /):
    'radixes/[uint{>=2}] -> digits/[uint%radix for radix in radixes] -> u/uint%II(radixes)'
    u = 0
    for radix, digit in zip(radixes, digits):
        u *= radix
        u += digit
    u
    return u

def reverse_digit4uint_(radixes, u, /):
    'radixes/[uint{>=2}] -> u/uint%II(radixes) -> v/uint%II(radixes){uint2digits_(radixes[::-1],v) == uint2digits_(radixes,u)[::-1]}'
    #digit_reversal
    reversed_digits = uint2reversed_digits_(radixes, u)
    v = uint5digits_(radixes[::-1], reversed_digits)
    return v



def uint5bits_(sz4bits, bits, /):
    'sz4bits/[uint{>=0}] -> bits/[uint%2]{len==sz4bits} -> u/uint%2**sz4bits'
    s = ''.join(map(str, bits))
    u = int(s, 2)
    return u
def uint2bits_(sz4bits, u, /):
    'sz4bits/[uint{>=0}] -> u/uint%2**sz4bits -> bits/[uint%2]{len==sz4bits}'
    s = f'{u:0>{sz4bits}b}'
    return [*map(int, s)]
def bit_scramble_(sz4bits, u, /):
    'sz4bits/[uint{>=0}] -> u/uint%2**sz4bits -> v/uint%2**sz4bits{uint2bits_(sz4bits,v) == uint2bits_(sz4bits,u)[::-1]}'
    bits = uint2bits_(sz4bits, u)
    v = uint5bits_(sz4bits, bits[::-1])
    return v





































######################
######################
######################
######################
######################
######################
######################
######################
######################
#.def iter_op_1_s_(op, g, xs, /):
#.    return (op(g,x) for x in xs)

def FFT__native(neg, add, mul, g, xs, /, *, may_gs=None):
    r'''[[[
    [w**L == 1]:
        [mx{FFT,L,w} =[def]= let [g:=w**-1] in matrix(\i,j->g**(i*j))]


[w**L == 1][g:=w**-1]:
    #FFT:
    [ys[j] == sum [xs[k]*g**(j*k) | [k :<- [0..<L]]]]
    #IFFT:
    [zs[j] == L**-1*sum [ys[k]*w**(j*k) | [k :<- [0..<L]]]]
    [L%p == 0]:
    [FFT(g;xs)[j]
    == ys[j]
    == sum [xs[k]*g**(j*k) | [k :<- [0..<L]]]
    # [k == u*p+v]
    == sum [xs[u*p+v]*g**(j*(u*p+v)) | [u :<- [0..<L/p]][v :<- [0..<p]]]
    == sum [sum [xs[u*p+v]*g**(j*(u*p+v)) | [u :<- [0..<L/p]]] | [v :<- [0..<p]]]
    == sum [g**(j*v) * sum [xs[u*p+v]*(g**p)**(j*u) | [u :<- [0..<L/p]]] | [v :<- [0..<p]]]
    == sum [g**(j*v) * sum [xs[u*p+v]*(g**p)**(j%(L/p)*u) | [u :<- [0..<L/p]]] | [v :<- [0..<p]]]
    == sum [g**(j*v) * FFT(g**p;xs[v::p])[j%(L/p)] | [v :<- [0..<p]]]
    ]
    [FFT(g;xs)[j] == sum [g**(j*v) * FFT(g**p;xs[v::p])[j%(L/p)] | [v :<- [0..<p]]]]
        # 重构公式:here

    #]]]'''#'''
    L = len(xs)
    #if not L < 2:return [*xs]
    gs = _mk_pows(mul, L, g, may_gs=may_gs)
    assert len(gs) == L
    mx = [[gs[irow*icolumn%L] for icolumn in range(L)] for irow in range(L)]
    #if 0b0001:print(mx)
    rs = [reduce(add, map(mul, xs, mx[irow])) for irow in range(L)]
    return rs

def IFFT_(FFT_, neg, add, mul, inv_g, inv_len, xs, /, *, extra_args=(), may_gs=None, may_inv_gs=None, **kwds):
    '[inv_g==FFT.uinty_root]'
    if may_inv_gs is None:
        if not may_gs is None:
            gs = may_gs
            inv_gs = [gs[0], *gs[:0:-1]]
            may_inv_gs = inv_gs
    #xxx:(kw:may_gs may be not existed):kwds['may_gs'] = may_inv_gs
    if not may_inv_gs is None:
        kwds['may_gs'] = may_inv_gs
    rs = FFT_(neg, add, mul, *extra_args, inv_g, xs, **kwds)
    #rs = [*iter_op_1_s_(mul, inv_len, ys)]
        # cancel:since FFT_ may be inplace
    for i in range(len(rs)):
        rs[i] = mul(inv_len, rs[i])
    return rs
def _mk_pows(mul, L, g, /, *, may_gs):
    #gs = [g**k for k in range(len(xs))]
    if not may_gs is None:
        gs = may_gs
        assert len(gs) == L
            # !! [g**L == one]
        return gs

    if L == 0:return []
    gs = [None, g]
    for _ in range(L-1):
        gs.append(mul(gs[-1], g))
    one = gs.pop()
    gs[0] = one
    return gs

def FFT__original__len_is_zpow(neg, add, mul, g, xs, /, *, may_gs=None):
    '[g==FFT.uinty_root**-1]'
    L = len(xs)
    if L == 0:raise ValueError(L)
    sz4bits = L.bit_length()-1
    if not L == (1<<sz4bits):raise ValueError(L)
    gs = _mk_pows(mul, L, g, may_gs=may_gs)
    assert len(gs) == L
    LLL = L
    def FFT(ig, xs, /):
        L = len(xs)
        if L == 1:
            return [*xs]
        #gg = mul(g, g)
        igg = ig*2
        ys = FFT(igg, xs[0::2])
        zs = FFT(igg, xs[1::2])
            # idx:lowest bit <-> highest bit
        #bug:_gs = (gs[i] for i in range(L)[::ig])
        _gs = (gs[i] for i in range(LLL)[::ig])
        zs = [*map(mul, _gs, zs)]
        rs = [*map(add, ys, zs), *map(add, ys, map(neg, zs))]
        return rs
    return FFT(1, xs)

def FFT__bit_scramble__len_is_zpow__inplace(neg, add, mul, g, xs, /, *, may_gs=None):
    '[g==FFT.uinty_root**-1]' \
    ' # [TIME(FFT__bit_scramble__len_is_zpow__inplace(neg, add, mul; xs)) = O(L*log2(L))*TIME(mul+add+neg)]'
    L = len(xs)
    if L == 0:raise ValueError(L)
    sz4bits = L.bit_length()-1
    if not L == (1<<sz4bits):raise ValueError(L)
    for i in range(L):
        # O(L*log2(L))
        j = bit_scramble_(sz4bits,i)
            # O(log2(L))
        if i < j:
            xs[i], xs[j] = xs[j], xs[i]
    #gs = [g**k for k in range(L)]
    gs = _mk_pows(mul, L, g, may_gs=may_gs)
        # L*TIME(1*mul)
    assert len(gs) == L
    for ez in range(1, 1+sz4bits):
        # total: sz4bits*L/2*TIME(1*mul+2*add+1*neg) == L*log2(L)/2*TIME(1*mul+2*add+1*neg)
        sz = 2**ez
        #gg = gs[L>>ez] #gs[L//sz] # g**(L//sz)
        ig = L>>ez
        h = sz>>1
        for i in range(0,L,sz):
            # total: L/sz*h*TIME(1*mul+2*add+1*neg) == L/2*TIME(1*mul+2*add+1*neg)
            # [i..<i+sz]
            # ys = xs[i:i+sz//2]
            # zs = xs[i+sz//2:i+sz]
            j = i+h
            for k in range(h):
                # total: h*TIME(1*mul+2*add+1*neg)
                y = xs[i+k]
                z = mul(xs[j+k], gs[ig*k])
                xs[i+k] = add(y, z)
                xs[j+k] = add(y, neg(z))
    # total:O(L*log2(L)) + L*TIME(1*mul) + L*log2(L)/2*TIME(1*mul+2*add+1*neg)
    # total:O(L*log2(L))*TIME(mul+add+neg)
    return xs
def _prepare4mod_prime_(modulus, g, sz=None, /):
    '[sz>=1][phi(modulus)%sz==0][g**sz%modulus==1][order_mod_(modulus;g)==sz]'
    #xxx:[is_prime(modulus)][modulus%2==1]
    r'''[[[
>>> (modulus, g) = (17, 3)
>>> sz = modulus-1
>>> (neg, add, mul, inv) = _mk_neg_add_mul_inv4mod_(modulus)
>>> inv_g = inv(g)
>>> inv_len = inv(sz)
>>> (inv_len*sz)%modulus
1
>>> (inv_g*g)%modulus
1
>>> pow(inv_g, sz, modulus)
1
>>> pow(inv_g, sz//2, modulus) -modulus
-1
>>> inv_g == pow(g, sz-1, modulus)
True

    #]]]'''#'''
    if 0:
        assert modulus >= 3
        assert 1 == modulus%2
    assert modulus >= 1
    if sz is None:
        sz = modulus-1
    (neg, add, mul, inv) = _mk_neg_add_mul_inv4mod_(modulus)
    inv_g = inv(g)
    inv_len = inv(sz)
    assert 1%modulus == (inv_len*sz)%modulus
    assert 1%modulus == (inv_g*g)%modulus
    assert 1%modulus == pow(inv_g, sz, modulus)
    if sz%2==0 and modulus > 1:
        assert -1 == pow(inv_g, sz//2, modulus) -modulus
    assert inv_g == pow(g, sz-1, modulus)
    L = sz
    gs = _mk_pows(mul, L, g, may_gs=None)
    assert len(gs) == L
    if modulus > 1:
        assert gs[0] == 1
        assert gs.count(1) == 1
    may_radixes = flatten_list_factor_pint__naive_brute_force_(sz) if sz else None
    return (neg, add, mul, g, inv_g, sz, inv_len, may_radixes)
        # (gs | inv_gs)


def _mk_neg_add_mul_inv4mod_(m, /):
    'modulus -> (neg, add, mul, inv)'
    def neg(a, /):
        return (-a)%m
    def add(a, b, /):
        return (a+b)%m
    def mul(a, b, /):
        return (a*b)%m
    def inv(a, /):
        return pow(a,-1,m)
    return (neg, add, mul, inv)
mk_neg_add_mul_inv4mod_ = _mk_neg_add_mul_inv4mod_

def FFT__bit_scramble__len_is_zpow(neg, add, mul, g, xs, /, **kwds):
    '[g==FFT.uinty_root**-1]'
    rs = FFT__bit_scramble__len_is_zpow__inplace(neg, add, mul, g, [*xs], **kwds)
    return rs
def FFT__idx_digit_reverse(neg, add, mul, g, xs, /, **kwds):
    '[g==FFT.uinty_root**-1]'
    rs = FFT__idx_digit_reverse__inplace(neg, add, mul, g, _rs:=[*xs], **kwds)
    assert not rs is xs
    assert rs is _rs
    return rs
def FFT__idx_digit_reverse__inplace(neg, add, mul, g, xs, /, *, may_radixes=None, scramble_=None, may_gs=None):
    '[g==FFT.uinty_root**-1]' \
    ' # [TIME(FFT__idx_digit_reverse__inplace(neg, add, mul; radixes; xs)) = O(L*sum(radixes))*TIME(mul+add) where [L==II(radixes)==len(xs)]]'
    L = len(xs)
    if L == 0:raise ValueError(L)
    if may_radixes is None:
        radixes = flatten_list_factor_pint__naive_brute_force_(len(xs))
    else:
        radixes = may_radixes
    radixes
    if not L == reduce(int.__mul__, radixes, 1):raise ValueError(L)
    reversed_radixes = radixes[::-1]
    del radixes
    ######################
    ######################
    ######################
    if 0:
        # reverse_digit4uint_([2,3],1)=>[1-->2-->4-->3-->1] 并非回旋函数，导致bug@FFT__idx_digit_reverse__inplace
        for i in range(L):
            j = reverse_digit4uint_(reversed_radixes,i)
            if i < j:
                xs[i], xs[j] = xs[j], xs[i]
    ######################
    ######################
    def _scramble_(xs, /):
        j2b = [False]*L
        Nothing = object()
        for i in range(L):
            if j2b[i]: continue
            i0 = i
            xi = xs[i]
            xs[i] = Nothing
            while 1:
                j2b[i] = True
                j = reverse_digit4uint_(reversed_radixes,i)
                #xs[i], xs[j] = xs[j], xs[i]
                xi, xs[j] = xs[j], xi
                777; i = j
                if i == i0: break
            assert not xs[i] is Nothing
            assert xi is Nothing, (i0, i,j, j2b)
    if scramble_ is None:
        scramble_ = _scramble_
    scramble_(xs)
        # O(L)
    ######################
    #gs = [g**k for k in range(L)]
    gs = _mk_pows(mul, L, g, may_gs=may_gs)
        # (L)*TIME(mul)
    assert len(gs) == L
    sz = 1
    ig = L
    # [ig*sz == L]
    for radix in reversed_radixes:
        # total:(L*sum(radixes))*TIME(mul+add)
        #if 0b0001:print(xs)
        gap = sz
        # [ig*sz == L]
        #gg = #gs[L//sz] # g**(L//sz)
        #ig = L//sz
        ig //= radix
        sz *= radix
        # [ig*sz == L]
        #_gs = [gs[j] for j in range(0,L,ig)]
        igs = range(0,L,ig)
        # [len(igs) == sz == gap*radix]
        assert len(igs) == sz
        _g = gs[igs[1]]
        for offset in range(0,L,sz):
            # total:(L/sz*sz*radix)*TIME(mul+add)==(L*radix)*TIME(mul+add)
            # [offset..<offset+sz]
            for k in range(gap):
                # total:(gap*radix**2)*TIME(mul+add) == (sz*radix)*TIME(mul+add)
                # [offset+k,offset+k+gap..<offset+k+gap*radix]
                idc = range(offset+k,offset+sz,gap)
                    # irow_offsetted for a record
                ts = [xs[j] for j in idc]
                assert len(ts) == radix
                # [len(ts) == sz/gap == radix]
                    # the kth record
                    # cache "radix" sub-outputs since these places will be override immediately
                #
                #
                # top layer:sz==radix*II(inner_radixes)==radix*gap
                # cut into radix blocks:each of size gap
                # get radix block subresults:each of size gap
                # to reconstruct final output of size sz: put the "radix" subresults into a matrix(radix*radix):
                #   super_mx1[irow,icolumn] := subresults[icolumn]
                #   mx1_1[irow*gap:(irow+1)*gap,icolumn] := subresults[icolumn]
                # make correspondent mx2 for coeffs (_g is "g" for this layer):
                #   mx2_2[irow*gap:(irow+1)*gap,icolumn] := [(_g**icolumn)**(irow*gap+k) for k in [0..<gap]]
                # NOTE:this layer input,output both at xs[offset:offset+sz]
                #   => irow_offsetted == offset+(irow_refined:=irow*gap+k)
                #.for irow in range(radix):
                #.    irow_refined = (irow*gap+k)
                #.    irow_offsetted = offset+irow_refined
                for irow_offsetted in idc:
                    # total:(radix**2)*TIME(mul+add)
                    irow_refined = irow_offsetted -offset
                    # !! [FFT(g;xs)[j] == sum [g**(j*v) * FFT(g**p;xs[v::p])[j%(L/p)] | [v :<- [0..<p]]]]
                        # 重构公式:goto
                    # [v := icolumn]
                    # [j := irow_refined]
                    # [p := radix]
                    # [L := sz]
                    # [xs := ...已被洗牌]
                    # [L/p == gap]
                    # [j%(L/p) == irow_refined%gap==k]
                    # [FFT(g**p;xs[v::p])[j%(L/p)] == _xs_[offset+gap*icolumn:offset+gap*(icolumn+1)][k] == _xs_[offset+k+gap*icolumn] == ts[icolumn]]
                    # => [FFT(g;xs)[j] == sum [g**(j*v) * ts[icolumn] | [v==icolumn :<- [0..<p==radix]]]]
                    #
                    #xs[irow_offsetted] = reduce(add, (mul(ts[icolumn], gs[igs[icolumn*irow_refined%sz]]) for icolumn in range(radix)))
                    xs[irow_offsetted] = reduce(add, (mul(ts[icolumn], gs[ig*(icolumn*irow_refined%sz)]) for icolumn in range(radix)))
                        # (radix)*TIME(mul+add)
    assert ig == 1
    # total:O(L) + (L)*TIME(mul) + (L*sum(radixes))*TIME(mul+add)
    # total:O(L*sum(radixes))*TIME(mul+add) where [L==II(radixes)==len(xs)]
    return xs

def FFT__idx_digit_reverse__inplace__mod_(modulus, g, xs, /, **kwds):
    '[g==FFT.uinty_root**-1]'
    (neg, add, mul, inv) = _mk_neg_add_mul_inv4mod_(modulus)
    return FFT__idx_digit_reverse__inplace(neg, add, mul, g, xs, **kwds)
def FFT__idx_digit_reverse__mod_(modulus, g, xs, /, **kwds):
    '[g==FFT.uinty_root**-1]'
    (neg, add, mul, inv) = _mk_neg_add_mul_inv4mod_(modulus)
    return FFT__idx_digit_reverse(neg, add, mul, g, xs, **kwds)


__all__
from seed.algo.FFT.index_scramble4FFT import reverse_digit4uint_, bit_scramble_
from seed.algo.FFT.index_scramble4FFT import uint2digits_, uint2reversed_digits_, uint5digits_
from seed.algo.FFT.index_scramble4FFT import uint5bits_, uint2bits_



from seed.algo.FFT.index_scramble4FFT import IFFT_
    #def IFFT_(FFT_, neg, add, mul, inv_g, inv_len, xs, /, *, extra_args=(), may_gs=None, may_inv_gs=None, **kwds):
from seed.algo.FFT.index_scramble4FFT import FFT__native, FFT__original__len_is_zpow, FFT__bit_scramble__len_is_zpow, FFT__idx_digit_reverse
    #def FFT__native(neg, add, mul, g, xs, /, *, may_gs=None):
    #def FFT__original__len_is_zpow(neg, add, mul, g, xs, /, *, may_gs=None):
    #def FFT__bit_scramble__len_is_zpow(neg, add, mul, g, xs, /, **kwds):
    #def FFT__idx_digit_reverse(neg, add, mul, g, xs, /, **kwds):
from seed.algo.FFT.index_scramble4FFT import FFT__bit_scramble__len_is_zpow__inplace, FFT__idx_digit_reverse__inplace
    #def FFT__bit_scramble__len_is_zpow__inplace(neg, add, mul, g, xs, /, *, may_gs=None):
    #def FFT__idx_digit_reverse__inplace(neg, add, mul, g, xs, /, *, may_radixes=None, scramble_=None, may_gs=None):

from seed.algo.FFT.index_scramble4FFT import mk_neg_add_mul_inv4mod_
    #def mk_neg_add_mul_inv4mod_(modulus, /):
from seed.algo.FFT.index_scramble4FFT import FFT__idx_digit_reverse__inplace__mod_, FFT__idx_digit_reverse__mod_
    #def FFT__idx_digit_reverse__inplace__mod_(modulus, g, xs, /, **kwds):
    #def FFT__idx_digit_reverse__mod_(modulus, g, xs, /, **kwds):


from seed.algo.FFT.index_scramble4FFT import _mk_pows
#def _mk_pows(mul, L, g, /, *, may_gs):

from seed.algo.FFT.index_scramble4FFT import *
