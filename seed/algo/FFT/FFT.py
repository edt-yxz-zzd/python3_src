#__all__:goto
r'''[[[
e ../../python3_src/seed/algo/FFT/FFT.py
view ../../python3_src/seed/algo/FFT/index_scramble4FFT.py


seed.algo.FFT.FFT
py -m nn_ns.app.debug_cmd   seed.algo.FFT.FFT -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.algo.FFT.FFT:__doc__ -ht # -ff -df

[[
'Prime numbers-A Computational Perspective(2ed)(2005)(Pomerance).pdf'
(FFT, “ping-pong” variant, in-order, no bit-scramble).
]]


def _prepare4mod_prime_(modulus, g, sz=None, /):
>>> (modulus, g) = (17, 3)
>>> (neg, add, mul, g, inv_g, sz, inv_len, radixes) = _prepare4mod_prime_(modulus, g)
>>> (g, inv_g, sz, inv_len, radixes)
(3, 6, 16, 16, [2, 2, 2, 2])


>>> xs = [*range(sz)[sz//2:], *range(sz)[:sz//2]]
>>> xs
[8, 9, 10, 11, 12, 13, 14, 15, 0, 1, 2, 3, 4, 5, 6, 7]
>>> FFT__ping_pong__inplace(neg, add, mul, g, xs, may_radixes=radixes)
[1, 9, 2, 2, 7, 13, 6, 12, 9, 4, 12, 3, 11, 14, 16, 7]
>>> IFFT_(FFT__ping_pong__inplace, neg, add, mul, inv_g, inv_len, xs, may_radixes=radixes)
[8, 9, 10, 11, 12, 13, 14, 15, 0, 1, 2, 3, 4, 5, 6, 7]




>>> (modulus, g) = (3, 2)
>>> (neg, add, mul, g, inv_g, sz, inv_len, radixes) = _prepare4mod_prime_(modulus, g)
>>> xs = [1, 2]
>>> FFT__ping_pong__inplace(neg, add, mul, g, xs)
[0, 2]
>>> IFFT_(FFT__ping_pong__inplace, neg, add, mul, inv_g, inv_len, xs)
[1, 2]

>>> xs = [1, 1]
>>> FFT__ping_pong__inplace(neg, add, mul, g, xs)
[2, 0]
>>> IFFT_(FFT__ping_pong__inplace, neg, add, mul, inv_g, inv_len, xs)
[1, 1]




[[1, 1, 1, 1]
,[1, 2, 4, 3]
,[1, 4, 1, 4]
,[1, 3, 4, 2]
]
>>> (modulus, g) = (5, 2)
>>> (neg, add, mul, g, inv_g, sz, inv_len, radixes) = _prepare4mod_prime_(modulus, g)
>>> xs = [1, 3, 2, 4]
>>> FFT__ping_pong__inplace(neg, add, mul, g, xs)
[0, 2, 1, 1]
>>> IFFT_(FFT__ping_pong__inplace, neg, add, mul, inv_g, inv_len, xs)
[1, 3, 2, 4]



>>> radixes = [2,2]
>>> FFT__ping_pong__inplace(neg, add, mul, g, xs, may_radixes=radixes)
[0, 2, 1, 1]
>>> IFFT_(FFT__ping_pong__inplace, neg, add, mul, inv_g, inv_len, xs, may_radixes=radixes)
[1, 3, 2, 4]




>>> (modulus, g, radixes) = (31, 3, [2,3,5])
>>> (neg, add, mul, g, inv_g, sz, inv_len, radixes) = _prepare4mod_prime_(modulus, g)
>>> xs = [1, 3, 2, 4, *range(26)]
>>> FFT__ping_pong__inplace(neg, add, mul, g, xs, may_radixes=radixes)
[25, 23, 25, 29, 3, 3, 0, 3, 12, 21, 3, 13, 8, 29, 2, 14, 20, 6, 20, 7, 8, 25, 11, 21, 10, 0, 23, 16, 10, 12]
>>> IFFT_(FFT__ping_pong__inplace, neg, add, mul, inv_g, inv_len, xs, may_radixes=radixes)
[1, 3, 2, 4, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]



>>> (modulus, g, radixes) = (7, 3, [2,3])
>>> (neg, add, mul, g, inv_g, sz, inv_len, radixes) = _prepare4mod_prime_(modulus, g)
>>> xs = [1, 3, 2, 4, 6, 6]
>>> FFT__ping_pong__inplace(neg, add, mul, g, xs, may_radixes=radixes)
[1, 1, 6, 3, 1, 1]
>>> IFFT_(FFT__ping_pong__inplace, neg, add, mul, inv_g, inv_len, xs, may_radixes=radixes)
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
>>> FFT__ping_pong(neg, add, mul, g, xs, may_radixes=radixes) == rs
True
>>> IFFT_(FFT__ping_pong, neg, add, mul, inv_g, inv_len, rs, may_radixes=radixes) == xs
True

#non-inplace,without-radixes
>>> xs == [1, 3, 2, 4, 6, 6, *range(204)]
True
>>> FFT__ping_pong(neg, add, mul, g, xs) == rs
True
>>> IFFT_(FFT__ping_pong, neg, add, mul, inv_g, inv_len, rs) == xs
True


#inplace,with-radixes
>>> FFT__ping_pong__inplace(neg, add, mul, g, xs, may_radixes=radixes) == rs
True
>>> IFFT_(FFT__ping_pong__inplace, neg, add, mul, inv_g, inv_len, xs, may_radixes=radixes) == [1, 3, 2, 4, 6, 6, *range(204)]
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
>>> FFT__ping_pong(neg, add, mul, g, xs)
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


>>> FFT__ping_pong(neg, add, mul, g, xs)
[1]
>>> IFFT_(FFT__ping_pong, neg, add, mul, inv_g, inv_len, rs)
[1]




>>> 


py_adhoc_call   seed.algo.FFT.FFT   @f
from seed.algo.FFT.FFT import *
]]]'''#'''
__all__ = r'''
FFT__ping_pong__inplace
    FFT__ping_pong
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.from itertools import islice
#.from seed.tiny_.check import check_type_is, check_int_ge
from itertools import product
from seed.math.factor_pint.factor_pint__naive_brute_force import flatten_list_factor_pint__naive_brute_force_

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

from seed.algo.FFT.index_scramble4FFT import _mk_pows, _prepare4mod_prime_
#def _mk_pows(mul, L, g, /, *, may_gs):



from functools import reduce
___end_mark_of_excluded_global_names__0___ = ...



def _init(mul, g, L, may_radixes, may_gs, /):
    if L == 0:raise ValueError(L)
    if may_radixes is None:
        radixes = flatten_list_factor_pint__naive_brute_force_(L)
    else:
        radixes = may_radixes
    radixes
    if not L == reduce(int.__mul__, radixes, 1):raise ValueError(L)
    ######################
    #gs = [g**k for k in range(L)]
    gs = _mk_pows(mul, L, g, may_gs=may_gs)
        # (L)*TIME(mul)
    assert len(gs) == L
    return (L, radixes, gs)
def FFT__ping_pong(neg, add, mul, g, xs, /, **kwds):
    return FFT__ping_pong__inplace(neg, add, mul, g, [*xs], **kwds)
def FFT__ping_pong__inplace(neg, add, mul, g, xs, /, *, may_radixes=None, scramble_=None, may_gs=None, may_ys=None):
    '[g==FFT.uinty_root**-1]' \
    ' # [TIME(FFT__ping_pong__inplace(neg, add, mul; xs)) = O(L*sum(radixes))*TIME(mul+add)]' \
    ' # (FFT, “ping-pong” variant, in-order, no bit-scramble)'
    # total:O(L*sum(radixes))*TIME(mul+add)
    #
    L = len(xs)
    (L, radixes, gs) = _init(mul, g, len(xs), may_radixes, may_gs)
        # L*TIME(mul)
    #reversed_radixes = radixes[::-1]
    radixes
    r'''[[[
    !! FFT(xs) --> FFT(xs[0::2]),FFT(xs[1::2])
    FFT(xs) --> FFT(xs[0::R0]),FFT(xs[1::R0])
    [L == R0*R1]
    xs, ys
    [bottom layer doing]:
        [ys[j*R1:j*(R1+1)] == FFT(xs[j::L/R1])]
        [ys.num_writers==1]
        [xs.num_readers==R1]
        swap xs ys
    [bottom layer done]:
        [xs == output of bottom layer]
        [ys[j*R0:j*(R0+1)] == FFT(xs[j::L/R0])]
        [ys.num_writers==1]
        [xs.num_readers==R0]
        swap xs ys

    要求:
        [ys.num_writers==1]
        [xs.num_readers==R[k]]
    ==>>:
        #Rk, xs0 --> xs1
        xs1[j*Rk:j*(Rk+1)]
        [@[j:<-[0..<L/Rk]] -> [xs1[j*Rk:(j+1)*Rk] := psFFT(gk;xs[j::L/Rk])]]
            # twist:psFFT <<== may not[gk**(Rk) =!= 1]
            #   !! [gk**(II(R[k:])) == 1]
        [IIRk_ := (II(R[k:]))]
        but as whole assume by induction:
        [@[j:<-[0..<L/IIRk_]] -> [xs1[j*IIRk_:(j+1)*IIRk_] := FFT(gk;xs0[j::L/IIRk_])]]

        ######################
        # xs0 - the input
        # xs_ - intermedia state
        # ys - next intermedia state of xs_
        ######################
        结论:每轮更新公式:
            [ys[tt] == sum [(g**(L/IIRu_))**(tt*v) * xs_[(L/radix)*v + (tt//IIRu_*IIRk_+tt%IIRk_)] | [v :<- [0..<radix]]]]
            where:
                [IIRu_ := radix*IIRk_]
                [IIRk_ := (II(R[k:]))]
            感觉不太对，xs_.num_readers 不太像只有radix个(即radix个加一指针)
                每IIRk_次加一后需要进行非加一型赋值，还行...
        ######################
        <<==:
        ######################
        the_FROM:
            归纳假设:即{约束乊每轮结束牜上一轮}
            [@[j:<-[0..<L/IIRk_]] -> [xs_[j*IIRk_:(j+1)*IIRk_] := FFT(g**(L/IIRk_);xs0[j::L/IIRk_])]]
        ...
        the_TO:
            约束乊每轮结束:
            [@[i:<-[0..<L/radix/IIRk_]] -> [ys[i*radix*IIRk_:(i+1)*radix*IIRk_] := FFT(g**(L/radix/IIRk_);xs0[i::L/radix/IIRk_])]]

        ######################
        # 下面根据约束{the_FROM,the_TO}推导{每轮更新公式}
        ######################
        # 下一轮:
        [t :<- [0..<radix*IIRk_]]
        [the_TO.rhs[t]
        == FFT(g**(L/radix/IIRk_);xs0[i::L/radix/IIRk_])[t]
        !! 重构公式
        # [FFT(gg;zs)[j] == sum [gg**(j*v) * FFT(gg**p;zs[v::p])[j%(LL/p)] | [v :<- [0..<p]]]]
        # [gg := g**(L/radix/IIRk_)]
        # [zs := xs0[i::L/radix/IIRk_]]
        # [j := t]
        # [p := radix]
        # [LL == len(zs) == L/(L/radix/IIRk_) == (radix*IIRk_)]
        # ==>>:
        == sum [(g**(L/radix/IIRk_))**(t*v) * FFT((g**(L/radix/IIRk_))**radix;xs0[i::L/radix/IIRk_][v::radix])[t%((radix*IIRk_)/radix)] | [v :<- [0..<radix]]]
        == sum [(g**(L/radix/IIRk_))**(t*v) * FFT(g**(L/IIRk_);xs0[i::L/radix/IIRk_][v::radix])[t%IIRk_] | [v :<- [0..<radix]]]
        #[ i+(L/radix/IIRk_)*(v+radix*?) == (i+(L/radix/IIRk_)*v + (L/IIRk_)*?)]
        == sum [(g**(L/radix/IIRk_))**(t*v) * FFT(g**(L/IIRk_);xs0[i+(L/radix/IIRk_)*v::(L/IIRk_)])[t%IIRk_] | [v :<- [0..<radix]]]
        !! 归纳假设:the_FROM:[@[j:<-[0..<L/IIRk_]] -> [xs_[j*IIRk_:(j+1)*IIRk_] := FFT(g**(L/IIRk_);xs0[j::L/IIRk_])]]
        # [j := i+(L/radix/IIRk_)*v]
        # [FFT(g**(L/IIRk_);xs0[i+(L/radix/IIRk_)*v::(L/IIRk_)]) == FFT(g**(L/IIRk_);xs0[j::L/IIRk_]) == xs_[j*IIRk_:(j+1)*IIRk_]]
        # [FFT(g**(L/IIRk_);xs0[i+(L/radix/IIRk_)*v::(L/IIRk_)])[t%IIRk_] == xs_[j*IIRk_:(j+1)*IIRk_][t%IIRk_] == xs_[j*IIRk_+t%IIRk_]]
        # ==>>:
        [j := i+(L/radix/IIRk_)*v]
        == sum [(g**(L/radix/IIRk_))**(t*v) * xs_[j*IIRk_+t%IIRk_] | [v :<- [0..<radix]]]
        == sum [(g**(L/radix/IIRk_))**(t*v) * xs_[(i+(L/radix/IIRk_)*v)*IIRk_+t%IIRk_] | [v :<- [0..<radix]]]
        == sum [(g**(L/radix/IIRk_))**(t*v) * xs_[(i*IIRk_+(L/radix)*v)+t%IIRk_] | [v :<- [0..<radix]]]
        ]
        ==>>:
        [the_TO.rhs[t]
        == FFT(g**(L/radix/IIRk_);xs0[i::L/radix/IIRk_])[t]
        == sum [(g**(L/radix/IIRk_))**(t*v) * xs_[(i*IIRk_+(L/radix)*v)+t%IIRk_] | [v :<- [0..<radix]]]
        ]

        !! [t <- [0..<radix*IIRk_]]
        !! the_TO
        [ys[i*radix*IIRk_:(i+1)*radix*IIRk_][t]
        == the_TO.lhs[t]
        == the_TO.rhs[t]
        == sum [(g**(L/radix/IIRk_))**(t*v) * xs_[(i*IIRk_+(L/radix)*v)+t%IIRk_] | [v :<- [0..<radix]]]
        ]
        [tt := (i*radix*IIRk_+t)]
        [IIRu_ := radix*IIRk_]
        !! [t <- [0..<radix*IIRk_]]:
        [(i,t) := tt/%(radix*IIRk_)]
        [(i,t) := tt/%IIRu_]
        [ys[tt]
        == ys[(i*radix*IIRk_+t)]
        == ys[i*radix*IIRk_:(i+1)*radix*IIRk_][t]
        == sum [(g**(L/radix/IIRk_))**(t*v) * xs_[(i*IIRk_+(L/radix)*v)+t%IIRk_] | [v :<- [0..<radix]]]
        !! [t == (tt%(radix*IIRk_))]
        # [(t%IIRk_) == (tt%IIRu_%IIRk_) == tt%IIRk_]
        == sum [(g**(L/radix/IIRk_))**((tt%(radix*IIRk_))*v) * xs_[(i*IIRk_+(L/radix)*v)+tt%IIRk_] | [v :<- [0..<radix]]]
        == sum [(g**(L/IIRu_))**(tt*v) * xs_[(L/radix)*v + (i*IIRk_+tt%IIRk_)] | [v :<- [0..<radix]]]

        !! [(i,t) := tt/%IIRu_]
        == sum [(g**(L/IIRu_))**(tt*v) * xs_[(L/radix)*v + (tt//IIRu_*IIRk_+tt%IIRk_)] | [v :<- [0..<radix]]]
        ]
        ==>>:
        结论:每轮更新公式:
        [IIRu_ := radix*IIRk_]
        [ys[tt]
        == sum [(g**(L/IIRu_))**(tt*v) * xs_[(L/radix)*v + (tt//IIRu_*IIRk_+tt%IIRk_)] | [v :<- [0..<radix]]]
            # [f(tt) = (tt//IIRu_*IIRk_+tt%IIRk_)] 这个操作 相当于 tt 的『(L/IIRu_,radix,IIRk_)-变进制数表达』 删去 中间数字 变成『(L/IIRu_,IIRk_)-变进制数表达』
        ]


    ######################
    ######################
    ######################
    view ../../python3_src/seed/algo/FFT/index_scramble4FFT.py
        [FFT(g;xs)[j] == sum [g**(j*v) * FFT(g**p;xs[v::p])[j%(L/p)] | [v :<- [0..<p]]]]
            # 重构公式
    #]]]'''#'''
    ys = [None]*L if may_ys is None else may_ys
    xs
    xs0 = xs

    # [@[j:<-[0..<L/1]] -> [xs[j*1:(j+1)*1] := FFT(g**(L/1);xs0[j::L/1])]]
    IIRk_ = 1
    # [@[j:<-[0..<L/IIRk_]] -> [xs[j*IIRk_:(j+1)*IIRk_] := FFT(g**(L/IIRk_);xs0[j::L/IIRk_])]]
    igu = L # == (L/IIRk_)
    # [igu == (L/IIRk_)]
    for radix in radixes[::-1]:
        # sum [L * radix*TIME(mul+add) | [radix :<- radixes]]
        #   == L*sum(radixes)*TIME(mul+add)
        #
        # [@[j:<-[0..<L/IIRk_]] -> [xs[j*IIRk_:(j+1)*IIRk_] := FFT(g**(L/IIRk_);xs0[j::L/IIRk_])]]
        # [igu == (L/IIRk_)]

        IIRu_ = radix*IIRk_
        igu //= radix # == (L/IIRu_)
        # [igu == (L/IIRu_)]
        L_div_IIRu_ = igu


        # !! 每轮更新公式:[ys[tt] == sum [(g**(L/IIRu_))**(tt*v) * xs_[(L/radix)*v + (tt//IIRu_*IIRk_+tt%IIRk_)] | [v :<- [0..<radix]]]]
        L_divR = L//radix
        def __(L=L):
            for v in range(radix):
                g = gs[igu*(tt*v)%L]
                #x = xs[L//radix *v + (tt//IIRu_*IIRk_+tt%IIRk_)]
                #x = xs[L_divR*v + (A_IIRk_+C)]
                x = xs[readers4X[v]+C]
                yield mul(g, x)
        #for tt, A_IIRk_, (A,B,C) in zip(range(L), ???bug:range(0, L, IIRk_), product(range(L//IIRu_), range(radix), range(IIRk_))):
            # [A_IIRk_ == A*IIRk_]
            # [tt == (A*radix+B)*IIRk_+C == A*IIRu_+B*IIRk_+C]
            #   i.e. "(A,B,C)" is a counter, eqv to "tt"
            #ys[tt] = reduce(add, __())
        it4tt = iter(range(L))
            # tt - the_only_writer4Y: (only update by:『tt+=1』)
        for ((A_IIRk_, A),B) in (product(zip(range(0, L_divR, IIRk_), range(L_div_IIRu_)), range(radix))):
            # (L/IIRu_)*radix * IIRk_ * radix*TIME(mul+add)
            #   == L * radix*TIME(mul+add)
            L_divR_mulB = L_divR*B
            readers4X = [L_divR*v+A_IIRk_ for v in range(radix)]
                # reset per IIRk_ nest-loops
            for C, tt, igC in zip(range(IIRk_), it4tt, range(L_divR_mulB, L_divR_mulB+L_divR, igu)):
                # IIRk_ * radix*TIME(mul+add)
                #
                # [A_IIRk_ == A*IIRk_]
                # [tt == (A*radix+B)*IIRk_+C == A*IIRu_+B*IIRk_+C]
                #   i.e. "(A,B,C)" is a counter, eqv to "tt"
                # tt - the_only_writer4Y: (only update by:『tt+=1』)
                # [igC == (L_divR_mulB+igu*C) == ((L/radix)*B+(L/IIRu_)*C)]
                #
                # ver1:
                #ys[tt] = reduce(add, __())
                #
                # ver2:
                #ys[tt] = reduce(add, (mul(gs[igu*(tt*v)%L], xs[readers4X[v]+C]) for v in range(radix)))
                #
                # !! [igC == (L_divR_mulB+igu*C)]
                # !! [igu == (L/IIRu_)]
                # [igu*(tt*v)%L == (L/IIRu_)*(A*IIRu_+B*IIRk_+C)*v%L == ((L/IIRu_)*B*IIRk_+igu*C)*v%L==((L/radix)*B+igu*C)*v%L == (L_divR_mulB+igu*C)*v%L == igC*v%L]
                if 0b0000:
                    v = 1
                    assert igu == (L//IIRu_)
                    assert tt == (A*IIRu_+B*IIRk_+C)
                    assert igu*tt == (L*A+(L//radix)*B+igu*C)
                    assert igu*(tt*v)%L == ((L//radix)*B+igu*C)*v%L
                    assert L_divR_mulB == (L//radix)*B
                    assert igu*(tt*v)%L == (L_divR_mulB+igu*C)*v%L
                    assert (L_divR_mulB+igu*C) == igC
                # ver3:
                ys[tt] = reduce(add, (mul(gs[(L_divR_mulB+igu*C)*v%L], xs[readers4X[v]+C]) for v in range(radix)))
                    # cancel ver4:since ver3-varable"C" is explicit
                # ver4:
                #ys[tt] = reduce(add, (mul(gs[igC*v%L], xs[readers4X[v]+C]) for v in range(radix)))
                    # radix*TIME(mul+add)
        ...
        # [@[i:<-[0..<L/radix/IIRk_]] -> [ys[i*radix*IIRk_:(i+1)*radix*IIRk_] := FFT(g**(L/radix/IIRk_);xs0[i::L/radix/IIRk_])]]
        # [@[i:<-[0..<L/IIRu_]] -> [ys[i*IIRu_:(i+1)*IIRu_] := FFT(g**(L/IIRu_);xs0[i::L/IIRu_])]]
        #swap:xs, ys
        xs, ys = ys, xs
        # [@[i:<-[0..<L/IIRu_]] -> [xs[i*IIRu_:(i+1)*IIRu_] := FFT(g**(L/IIRu_);xs0[i::L/IIRu_])]]
        IIRk_ = IIRu_
        # [@[j:<-[0..<L/IIRk_]] -> [xs[j*IIRk_:(j+1)*IIRk_] := FFT(g**(L/IIRk_);xs0[j::L/IIRk_])]]
        # !! [igu == (L/IIRu_)]
        # [igu == (L/IIRk_)]
    # [@[j:<-[0..<L/IIRk_]] -> [xs[j*IIRk_:(j+1)*IIRk_] := FFT(g**(L/IIRk_);xs0[j::L/IIRk_])]]
    assert IIRk_ == L

    # total:L*TIME(mul) + L*sum(radixes)*TIME(mul+add)
    # total:O(L*sum(radixes))*TIME(mul+add)

    #bug:return xs
        # !! inplace
    if not xs0 is xs:
        xs0[:] = xs
        xs = xs0
    return xs0






__all__
from seed.algo.FFT.FFT import *
