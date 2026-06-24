#__all__:goto
doing
考虑:一次性构造所有层次:
    mk(xs, jlayer, begin, step, sz)
r'''[[[
e ../../python3_src/seed/algo/FFT/convolution__7symbolic_DFT.py

seed.algo.FFT.convolution__7symbolic_DFT
py -m nn_ns.app.debug_cmd   seed.algo.FFT.convolution__7symbolic_DFT -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.algo.FFT.convolution__7symbolic_DFT:__doc__ -ht # -ff -df
#######

[[
copy from:
    view others/数学/polynomial/polynomial_evaluation.txt
===
[RR :: ring]:
  [cyclic_convolution{M} === __mul__{RR[X]%(-1+X**M)}]
  [negacyclic_convolution{M} === __mul__{RR[X]%(+1+X**M)}]
  [acyclic_convolution{M} === __mul__{RR[X]%(0+X**M)}] # trucated
  [icyclic_convolution{M,I} =[def]=__mul__{RR[X]%(-I+X**M)}]
  #[wcyclic_convolution{M,w} =[def]=__mul__{RR[X]%(-1+(w*X)**M)}]
  [wcyclic_convolution{M,w} =[def]=__mul__{RR[X]%(-1+(w**-1*X)**M)}]

  [wcyclic_convolution{M,w}
  ==__mul__{RR[X]%(-1+(w**-1*X)**M)}
  ==__mul__{RR[X]%(-w**M+X**M)}
  == icyclic_convolution{M,w**M}
  ]
  [wcyclic_convolution{M,w} == icyclic_convolution{M,w**M}]

  [I:=w**M]:
    [icyclic_convolution{M,I} == wcyclic_convolution{M,w}]

    [poly6icyclic_convolution{M,I}(X).coeffs
    == poly6wcyclic_convolution{M,w}(X).coeffs
    == poly6cyclic_convolution{M}(w**-1*X).coeffs
    == ((w**-1) **. [0..<M]) *. poly6cyclic_convolution{M}(X).coeffs
    ]
    [poly6icyclic_convolution{M,I}(X).coeffs == ((w**-1) **. [0..<M]) *. poly6cyclic_convolution{M}(X).coeffs]
    [poly6cyclic_convolution{M,I}(X).coeffs == (w **. [0..<M]) *. poly6icyclic_convolution{M}(X).coeffs]
  ==>>:
  [icyclic_convolution{M,w**M} == wcyclic_convolution{M,w}]
  [poly6cyclic_convolution{M,w**M}(X).coeffs == (w **. [0..<M]) *. poly6icyclic_convolution{M}(X).coeffs]
    => DWT/weighted_cyclic_convolution__len_eq_


]]
[[
view others/数学/polynomial/polynomial_evaluation.txt
===
概览牜卷积:goto
变体设计牜卷积牜纯符:goto
  原版:symFNN0,symFNN1
  #fail:{高层IFFT无法灭零}变体:symFPP1,symFPP2
  证明不可交替递归:goto
  using_sqrt4one_instead_neg4one_in_FFT:goto

  FFT+IFFT回返原值的必要条件:
    [@[t:<-[1..<sz]] -> [sum[(g**j)**t | [j:<-[0..<sz]]] == 0]]
        => [g{sz:=2} == -1]


]]
[[
TODO:
考虑泛化:[t**M==z**N==b]
   特别是 复数域:1j 看看可否 消除 低层数据 翻倍增长
    不能!
]]
[[
考虑拆成三层:
[em == eu+ev+en][en>=ev>=eu]
[t**U==s][s**V==z][z**N==-1]
[hg4u:=z**2**(en-eu)]
[hg4v:=z**2**(en-ev)]
[hg4u可用于 poly{t}的乘积]
[hg4v可用于 poly{s}的乘积]
[三层折返值分别是s,z,-1]
假设poly{N;z}乘法 耗时 Tz(2N)
假设poly{V;s}乘法 耗时 Ts(2V,N)
    似乎可以简省为初始FFT + 终末IFFT
    反正 加法 点对点，旋转位移 直传低层
假设poly{U;t}乘法 耗时 Tt(2U,V,N)
未简省FFT:
    [Ts(2V,N) == [FFT/IFFT]3*2Vln2V*N + [dyadic_mul_]2V*Tz(2N)]
    [Tt(2U,V,N) == [FFT/IFFT]3*2Uln2U*N*V + [dyadic_mul_]2U*Ts(2V,N)]
简省FFT:没用？
    [Ts(2V,N) == [dyadic_mul_]2V*Tz(2N)]
    [Tt(2U,V,N) == [FFT/IFFT]3*2Uln2U*N*V + [FFT/IFFT]3*2U*2Vln2V*N + [dyadic_mul_]2U*Ts(2V,N)]

[Tt(2U,V,N)
== [FFT/IFFT]3*2Uln2U*N*V + [dyadic_mul_]2U*Ts(2V,N)
== [FFT/IFFT]3*2Uln2U*N*V + [dyadic_mul_]2U*([FFT/IFFT]3*2Vln2V*N + [dyadic_mul_]2V*Tz(2N))
== 3*2Uln2U*N*V + 2U*(3*2Vln2V*N + 2V*Tz(2N))
== 6Mln2U + 12Mln2V + 4UV*Tz(2N)
~= 9Mln(4M/N) + (4M/N)*Tz(2N)
~= 9Mln(4M/N) + (4M/N)*Tt(2N,...)
    #低层数量:8M==2**3*M
]
虽然 无法阻止 低层数据翻倍，
    但递归层数减少...
    若是 拆成更多层？感觉无用
        关键在于 多项式乘法 折返值 并非1，必须 使用 线性卷积，导致 低层数据 翻倍
]]
[[
cyclic_convolution泛化版:
圆正卷积牜泛化版:
    (polynomial{us,X} * polynomial{vs,X} %(-I+X**sz)).coeffs
    若已知w inv4w:[w**sz==I]则:
        (polynomial{us,X} * polynomial{vs,X} %(-(w**+sz)+X**sz)).coeffs
            其实就是weighted_cyclic_convolution_7native_
圆负卷积牜泛化版:
    但是未知w，但已知:[I**half_order4I == -1]
        # 达到『-1』是 IFFT有效回返的必要条件
        #   所以[I==1]反而不行！
        则可通过negacyclic_convolution_7zpow_{symbolic}泛化版来实现！

圆负卷积牜强化版:
    已知:[I**half_order4I == -1][half_order4I==2**ei]
    可以 更快求 圆负卷积
    [M==W*N][z**N==I][(z**N)**2**ei==-1==z**2**(en+ei)][(en+ei)>=ew][hg:=z**2**((en+ei)-ew)][hg**2**ew==-1]
        允许更大的W，更小的N，不断降低耗时，逼近FFT

]]




'#'; __doc__ = r'#'
>>> ops_7zpow16pp = Ops7modulus__4FFT_7zpow7recur_(1+2**16, 16, 3)
>>> (ez4sz, sz, ez4e4g, e4g) = ops_7zpow16pp.prepare4FFT_7zpow7recur_(4)
>>> (ez4sz, sz, ez4e4g, e4g)
(2, 4, 14, 16384)
>>> ops_7zpow16pp.mul7egR_(e4g, 1)
-256
>>> ops_7zpow16pp.mul7egR_(2*e4g, 1)
-1
>>> ops_7zpow16pp.mul7egR_(3*e4g, 1)
256
>>> ops_7zpow16pp.mul7egR_(4*e4g, 1)
1

>>> ops_7zpow16pp.mul7egR_(-e4g, 1)
256
>>> ops_7zpow16pp.mul7egR_(-2*e4g, 1)
-1
>>> ops_7zpow16pp.mul7egR_(-3*e4g, 1)
-256
>>> ops_7zpow16pp.mul7egR_(-4*e4g, 1)
1

>>> ops_7zpow16pp.FFT_7zpow7recur_([5])
(5,)
>>> ops_7zpow16pp.FFT_7zpow7recur_([5, 4])
(9, 1)
>>> ops_7zpow16pp.FFT_7zpow7recur_([5, 4, 2, 3])
(14, -253, 0, 259)

>>> ops_7zpow16pp.IFFT_7zpow7recur_((5,))
(5,)
>>> ops_7zpow16pp.IFFT_7zpow7recur_((9, 1))
(5, 4)
>>> ops_7zpow16pp.IFFT_7zpow7recur_((14, -253, 0, 259))
(5, 4, 2, 3)




view  others/数学/本原根.txt
    二幂模无用于快速傅立叶逆变换
    [@[em,g,j::int][em>=3][g%2==1] -> [gsum7zpow_(em,g,j) := sum[(g**j)**i | [i:<-[0..<2**(em-2)]]] %2**em] -> [gsum7zpow_(em,g,j) == 2**(em-3)*(gsum7zpow_(3,g%8,j%2)) <- 2**(em-3) *. {0,2,4,6}]]
>>> for ez4sz in range(5):
...     ops_7zpow16pp.FFT_7zpow7recur_([1]*2**ez4sz)
(1,)
(2, 0)
(4, 0, 0, 0)
(8, 0, 0, 0, 0, 0, 0, 0)
(16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
>>> ops_7zpow16 = Ops7modulus__4FFT_7zpow7recur_(2**16, 14, 3)
>>> for ez4sz in range(5):
...     xs = ops_7zpow16.FFT_7zpow7recur_([1]*2**ez4sz)
...     ys = ops_7zpow16.enlarge7zpow_(1, xs)
...     zs = ops_7zpow16.enlarge7zpow_(2, xs)
...     ez4sz
...     xs
...     ys
...     zs
0
(1,)
(2,)
(4,)
1
(2, -32766)
(4, 4)
(8, 8)
2
(4, -32764, 4, -32764)
(8, 8, 8, 8)
(16, 16, 16, 16)
3
(8, -32760, 8, -32760, 8, -32760, 8, -32760)
(16, 16, 16, 16, 16, 16, 16, 16)
(32, 32, 32, 32, 32, 32, 32, 32)
4
(16, -32752, 16, -32752, 16, -32752, 16, -32752, 16, -32752, 16, -32752, 16, -32752, 16, -32752)
(32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32)
(64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64)




>>> for pg in range(1, 32, 2):
...     ls = [pg]
...     while not ls[-1] == 1:
...         ls.append(ls[-1]*pg%32)
...     (pg, len(ls), ls)
(1, 1, [1])
(3, 8, [3, 9, 27, 17, 19, 25, 11, 1])
(5, 8, [5, 25, 29, 17, 21, 9, 13, 1])
(7, 4, [7, 17, 23, 1])
(9, 4, [9, 17, 25, 1])
(11, 8, [11, 25, 19, 17, 27, 9, 3, 1])
(13, 8, [13, 9, 21, 17, 29, 25, 5, 1])
(15, 2, [15, 1])
(17, 2, [17, 1])
(19, 8, [19, 9, 11, 17, 3, 25, 27, 1])
(21, 8, [21, 25, 13, 17, 5, 9, 29, 1])
(23, 4, [23, 17, 7, 1])
(25, 4, [25, 17, 9, 1])
(27, 8, [27, 25, 3, 17, 11, 9, 19, 1])
(29, 8, [29, 9, 5, 17, 13, 25, 21, 1])
(31, 2, [31, 1])

>>> for pg in [3,5,11,13,19,21,27,29]:
...     ops_7zpow5_pg = Ops7modulus__4FFT_7zpow7recur_(2**5, 3, pg)
...     pg
...     ops_7zpow5_pg.FFT_7zpow7recur_([1]*2**3)
...     ops_7zpow5_pg.FFT_7zpow7recur_([1]*2**2)
...     ops_7zpow5_pg.FFT_7zpow7recur_([1]*2**1)
3
(8, 16, 8, 16, 8, 16, 8, 16)
(4, -12, 4, -12)
(2, -14)
5
(8, -8, 8, -8, 8, -8, 8, -8)
(4, -12, 4, -12)
(2, -14)
11
(8, 16, 8, 16, 8, 16, 8, 16)
(4, -12, 4, -12)
(2, -14)
13
(8, -8, 8, -8, 8, -8, 8, -8)
(4, -12, 4, -12)
(2, -14)
19
(8, 16, 8, 16, 8, 16, 8, 16)
(4, -12, 4, -12)
(2, -14)
21
(8, -8, 8, -8, 8, -8, 8, -8)
(4, -12, 4, -12)
(2, -14)
27
(8, 16, 8, 16, 8, 16, 8, 16)
(4, -12, 4, -12)
(2, -14)
29
(8, -8, 8, -8, 8, -8, 8, -8)
(4, -12, 4, -12)
(2, -14)















py_adhoc_call   seed.algo.FFT.convolution__7symbolic_DFT   @f
from seed.algo.FFT.convolution__7symbolic_DFT import *
]]]'''#'''
__all__ = r'''
IOps4symbolic_DFT
IOps4symbolic_DFT7zpow
    Ops4symbolic_DFT7zpow__7ring_is_ZZ


Ops7modulus__4FFT_7zpow7recur_
    FFT_7zpow7recur_
        mk__mul7egR_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.#################################
#.from seed.helper.lazy_import__func7dict import lazy_import__funcs7dict_
#.(check_type_is, check_int_ge, _ifNone) = lazy_import__funcs7dict_(__name__ or globals() or locals(), 'seed.tiny_.check',  'check_type_is, check_int_ge      ifNone:_ifNone')
#.#################################
#.def mk_context4lazy_import_registered_names_(qnm4mdl7inject, qnm4pseudo_mdl7import, name7importZqnm4mdl, name7importZalias7inject={}, may_bifix4lazy_name7import=None, lazy_name7importZoriginal_name7import={}):
#.from seed.helper.lazy_import__func7context7register import mk_context4lazy_import_registered_names_, name7importZqnm4mdl_7tiny
#.with mk_context4lazy_import_registered_names_(__name__, 'seed._lazy_', name7importZqnm4mdl_7tiny):
#.    from seed._lazy_ import print_err, fst, echo, ifNone
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from itertools import islice, chain, repeat, cycle, tee
    from functools import reduce, cache#cached_property
    from seed.tiny_.check import check_type_is, check_int_ge, check_int_ge_le, check_non_ABC
    from seed.tiny_.types5py import curry1
    from seed.types.CachedProperty import CachedProperty, mk_cached_propertyT_
    from seed.math.floor_ceil_tools.fc_log import floor_log2, ceil_log2
    from seed.algo.FFT.index_scramble4FFT import FFT__bit_scramble__len_is_zpow
    #def FFT__bit_scramble__len_is_zpow(neg, add, mul, g, xs, /, **kwds):
    from seed.types.view.SeqSliceView import SeqSliceView
    from seed.math.hrem_ import hrem_, mk_hrem_
    from seed.math.mk_perfect_div_mod_ import mk_perfect_div_mod_
    from seed.math.mk_pows_ import mk_pows_, iter_geometric_progression_

#.    from seed.for_libs.for_functools.cached_property import cached_property
#.    from seed.func_tools.dot2 import dot
#.with mk_ctx4lazy_import4funcs_(__name__, arbitrary_ok=True):
#.    from seed.data_funcs.lnkls import rglnkls_ops# empty_rglnkls, mk_empty_rglnkls, rglnkls_ipush_right, rglnkls_ipop_right, rglnkls2reversed_iterable, rglnkls5iterable
#.with mk_ctx4lazy_import4funcs_(__name__, 'ifNone:_ifNone, ifNonef:_ifNonef'):
#.    from seed.helper.ifNone import ifNone as _ifNone, ifNonef as _ifNonef
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

class Ops7modulus__4FFT_7zpow7recur_:
    'FFT_7zpow7recur_'
    def __init__(sf, modulus, ez4order4pg, pg, /, *, modulus_as_zpow=False):
        assert not modulus_as_zpow, NotImplementedError
        check_int_ge(2, modulus)
        check_int_ge(0, ez4order4pg)
        check_type_is(int, pg)
        if ez4order4pg > 23:raise ValueError('len(gs) too big')
        hremR_ = mk_hrem_(modulus) # R:ring
        pg = hremR_(pg)
        order4pg = 1<<ez4order4pg
        mask4e4g = -1+order4pg
        sf._dat = (hremR_, ez4order4pg, mask4e4g, pg)
        sf._hremR_ = hremR_
        sf._ez4order4pg = ez4order4pg
        sf._modulus = modulus
        sf._mask4e4g = mask4e4g
        sf._modulus_as_zpow = modulus_as_zpow
    @cache
    def gmk_div7sz7zpow_(sf, ez4sz, /):
        check_int_ge_le(0, sf._ez4order4pg, ez4sz)
        sz = 1<<ez4sz
        return mk_perfect_div_mod_(sf._modulus, sz)
    @CachedProperty
    def gs(sf, /):
        (hremR_, ez4order4pg, mask4e4g, pg) = sf._dat
        order4pg = 1<<ez4order4pg
        #gs = islice(_iter_weights0_(sf.mul7RR_, 1, pg), 0, order4pg)
        gs = mk_pows_(sf.mul7RR_, 1, pg, order4pg)
        return gs
    def mul7egR_(sf, e4g, y, /):
        'e4g/uint%order4pg -> y/RR -> (pg**e4g * y)/RR'
        g = sf.gs[e4g & sf._mask4e4g]
        return sf.mul7RR_(g, y)
    def mul7RR_(sf, x, y, /):
        'x/RR -> y/RR -> (x*y)/RR'
        return sf._hremR_(x*y)
    def add7RR_(sf, x, y, /):
        'x/RR -> y/RR -> (x+y)/RR'
        return sf._hremR_(x+y)
    def prepare4FFT_7zpow7recur_(sf, sz4signal, /):
        ez4sz = floor_log2(sz4signal)
        sz = 1<<ez4sz
        if not sz4signal == sz:raise ValueError(ez4sz, sz, sz4signal)
        ez4e4g = sf._ez4order4pg -ez4sz
        if not ez4e4g >= 0:raise ValueError(sf._ez4order4pg, ez4e4g, sz4signal)
        e4g = 1<<ez4e4g
        return (ez4sz, sz, ez4e4g, e4g)
    def FFT_7zpow7recur_(sf, xs, /, *, backward=False):
        (ez4sz, sz, ez4e4g, e4g) = sf.prepare4FFT_7zpow7recur_(len(xs))
        #if backward: e4g = -e4g
        return FFT_7zpow7recur_(sf.mul7egR_, sf.add7RR_, e4g, ez4sz, xs, backward=backward)
    def IFFT_7zpow7recur_(sf, DFT4xs, /, *, backward=False, ez4enlarge=0):
        sz_xs = sf.FFT_7zpow7recur_(DFT4xs, backward=not backward)
        ez4sz = floor_log2(len(DFT4xs))
        if ez4enlarge:
            sz_xs = map(curry1(sf.mul7RR_, 1<<ez4enlarge), sz_xs)
            div_sz_ = sf.gmk_div7sz7zpow_(ez4enlarge+ez4sz)
        else:
            div_sz_ = sf.gmk_div7sz7zpow_(ez4sz)
        return tuple(map(div_sz_, sz_xs))
    def enlarge7zpow_(sf, ez4enlarge, ys, /):
        return tuple(map(curry1(sf.mul7RR_, 1<<ez4enlarge), ys))

def mk__mul7egR_(mul7RR_, ez4sz, gs, /):
    'see:FFT_7zpow7recur_'
    sz = 1<<ez4sz
    assert len(gs) == sz
    mask4e4g = -1+sz
    def mul7egR_(e4g, y, /):
        'e4g/uint%order4pg -> y/RR -> (pg**e4g * y)/RR'
        g = gs[e4g & mask4e4g]
        return mul7RR_(g, y)
    return mul7egR_
def FFT_7zpow7recur_(mul7egR_, add7RR_, e4g, ez4sz, xs, /, *, backward=False, mk=tuple):
    'mul7egR_/(e4g/int -> y/RR -> (g**e4j*y)/RR) -> add7RR_/(x/RR -> y/RR -> (x+y)/RR) -> e4g/uint -> ez4sz/uint -> xs/[RR]{len==sz}  # [sz==2**ez4sz] # [g==pg**e4g][g**sz==1][neednot[g**(sz///2)==1]] #avoid using neg_/sub_ # O(sz*ln(sz))'
    check_type_is(int, e4g)
    check_int_ge(0, ez4sz)
    sz = 1<<ez4sz
    if not len(xs) == sz:raise ValueError(ez4sz, sz, len(xs))
    if ez4sz == 0:
        return mk(xs)
    if backward:
        e4g = -e4g
    xs = SeqSliceView(xs, range(sz))
    hsz = e4g<<(ez4sz-1)
    e4g8sqrt4one = hsz # sqrt4one maybe not neg4one
    mul_sqrt4one_ = curry1(mul7egR_, e4g8sqrt4one)
    M = sz
    def recur_(e4g, ez4sz, sz, xs, /):
        if ez4sz == 0:
            return xs
        ez4hsz = -1+ez4sz
        hsz = 1<<ez4hsz

        xsE = xs[0::2] # SeqSliceView
        xsO = xs[1::2] # SeqSliceView
            # TIME = 2 * sz/2
        e4gg = 2*e4g
        ysE = recur_(e4gg, ez4hsz, hsz, xsE)
        ysO = recur_(e4gg, ez4hsz, hsz, xsO)
            # TIME = 2 * K*(sz/2)*ln(sz/2)
        es4gs = range(0, e4g*hsz, e4g)
        gj_ysO = [*map(mul7egR_, es4gs, ysO)]
        ysE = [*ysE]
            # useless:tee()
        ysL = map(add7RR_, ysE, gj_ysO)
        ysR = map(add7RR_, ysE, map(mul_sqrt4one_, gj_ysO))
            # TIME = 4 * (sz/2)
        return chain(ysL, ysR)
            # TIME = 2 * (sz/2)
        #collect:
            # TIME = 2 * sz/2
            # TIME = 2 * K*(sz/2)*ln(sz/2)
            # TIME = 4 * (sz/2)
            # TIME = 2 * (sz/2)
        #total:
            # TIME = 8 * (sz/2) + 2 * K*(sz/2)*ln(sz/2)
            #       <= K*(sz)*ln(sz)
            # [4*sz <= K*(sz)*ln(2)]
            # [K >= 4/ln(2) == 4*log2(e)]
    return mk(recur_(e4g, ez4sz, sz, xs))

_default_min_ez4recur = None
    #min_ez4recur
_default4auto_vs_fancy_vs_native = -1
    #auto_vs_fancy_vs_native
class IOps4convolution(ABC):
    '[RR == the ground ring]'
    __slots__ = ()
    ###########################
    # common:
    @abstractmethod
    def rg_add_(sf, x, y, /):
        'x/RR -> y/RR -> x+y'
        raise NotImplementedError
    @abstractmethod
    def rg_mul_(sf, x, y, /):
        'x/RR -> y/RR -> x*y'
        raise NotImplementedError
    @abstractmethod
    def rg_neg_(sf, x, /):
        'x/RR -> -x'
        # for negacyclic_convolution
        raise NotImplementedError
    #@property
    @CachedProperty
    @abstractmethod
    def rg_zero(sf, /):
        '-> 0/RR'
        # for zero_padding_
        raise NotImplementedError
    #@property
    @CachedProperty
    @abstractmethod
    def rg_one(sf, /):
        '-> 1/uroot/RR'
        # for weighted_
        raise NotImplementedError
    @abstractmethod
    def rg_eq_one_(sf, x, /):
        'x/RR -> [x == 1]'
        #used by weighted_()
        raise NotImplementedError
    ###########################

    ###########################
    ###########################
    #API{native}:sz
    ###########################
    ###########################
    def acyclic_convolution_7native_(sf, sz, us, vs, /):
        'sz/uint -> us/[RR] -> vs/[RR] -> (polynomial{us,X} * polynomial{vs,X} %(0+X**sz)).coeffs/[RR]{len==sz} # truncated'
        us = sf.truncated_(sz, us)
        vs = sf.truncated_(sz, vs)
        n = -1+len(us)+len(vs)
        _rg_mul_ = sf.rg_mul_
        _rg_sum_ = sf.rg_sum_
        ws = sf.mk_list_(_rg_sum_(_rg_mul_(us[j], vs[k-j]) for j in range(max(0, k+1-len(vs)), min(len(us), 1+k))) for k in range(n))
        ws = sf.truncated_(sz, ws)
        ws = sf.zero_padding_(sz, ws)
        return ws

    def cyclic_convolution_7native_(sf, sz, us, vs, /):
        'sz/uint -> us/[RR]{len==sz} -> vs/[RR]{len==sz} -> (polynomial{us,X} * polynomial{vs,X} %(-1+X**sz)).coeffs/[RR]{len==sz} # wrap_around'
        us = sf.wrap_around_(sz, to_neg6wrap:=False, us)
        vs = sf.wrap_around_(sz, to_neg6wrap:=False, vs)
        n = min(sz, -1+len(us)+len(vs))
        r'''[[[
        [n <= -1+len(us)+len(vs)]
        [n <= sz]
        [len(us) <= sz]
        [len(vs) <= sz]
        [k:<-[0..<n]][j:<-[0..<len(us)]][i:<-[0..<len(vs)]]:
            [i,j,k < sz]
            [i0+j==k][i1+j==k+sz]:
                [i1+j==(i0+j)+sz]
                [i1==i0+sz]
                [i1>=sz]
                _L
            * [i+j == k]:
                [i == k-j]
                [0 <= k-j < len(vs)]
                [k >= j > k-len(vs)]
                [k-len(vs) < j <= k]
                [k+1-len(vs) <= j < 1+k]
                [max(0,k+1-len(vs)) <= j < min(len(us),1+k)]
            * [i+j == k+sz]:
                [i == (k+sz)-j]
                [max(0,(k+sz)+1-len(vs)) <= j < min(len(us),1+(k+sz))]

        #]]]'''#'''
        if not n > 0:
            return sf.mk_list_('')

        _rg_mul_ = sf.rg_mul_
        _rg_sum_ = sf.rg_sum_
        k2rng_ = lambda k:range(max(0, k+1-len(vs)), min(len(us), 1+k))
        k2it_ = lambda k:(_rg_mul_(us[j], vs[k-j]) for j in k2rng_(k))
        wsP = sf.mk_list_(_rg_sum_(chain(k2it_(k), k2it_(k+sz))) for k in range(n))
        wsP = sf.zero_padding_(sz, wsP)
        return wsP
    def negacyclic_convolution_7native_(sf, sz, us, vs, /, **kwds4wcc):
        'sz/uint -> us/[RR]{len==sz} -> vs/[RR]{len==sz} -> (polynomial{us,X} * polynomial{vs,X} %(+1+X**sz)).coeffs/[RR]{len==sz} # wrap_around'
        us = sf.wrap_around_(sz, to_neg6wrap:=True, us)
        vs = sf.wrap_around_(sz, to_neg6wrap:=True, vs)
        n = min(sz, -1+len(us)+len(vs))
        _rg_mul_ = sf.rg_mul_
        _rg_neg_ = sf.rg_neg_
        _rg_sum_ = sf.rg_sum_
        k2rng_ = lambda k:range(max(0, k+1-len(vs)), min(len(us), 1+k))
        k2it_ = lambda k:(_rg_mul_(us[j], vs[k-j]) for j in k2rng_(k))
        wsN = sf.mk_list_(_rg_sum_(chain(k2it_(k), map(_rg_neg_,k2it_(k+sz)))) for k in range(n))
        wsN = sf.zero_padding_(sz, wsN)
        return wsN
    def weighted_cyclic_convolution_7native_(sf, sz, w, inv4w, us, vs, /):
        'sz/uint -> w/RR -> us/[RR]{len==sz} -> vs/[RR]{len==sz} -> (polynomial{us,X} * polynomial{vs,X} %(-(w**+sz)+X**sz)).coeffs/[RR]{len==sz}' # API changed: 『w**-sz』-->『w**+sz』
        #I = sf.rg_pow_(w, sz)
        # [X**sz == w**+sz == I]
        ##################
        us7w = sf.weighted_(w, us)
        vs7w = sf.weighted_(w, vs)
        ##################
        # weighted_() before wrap_around_()
        ##################
        ws7w = sf.cyclic_convolution_7native_(sz, us, vs)
            # wrap_around_() inside ...
        ##################
        ws7w
        ws = sf.weighted_(inv4w, ws7w)
        return ws


    ###########################
    ###########################
    #utils:
    ###########################
    ###########################
    def rg_sum_(sf, xs, /):
        'xs/Iter RR -> sum(xs)'
        return reduce(sf.rg_add_, xs, sf.rg_zero)
    def rg_sub_(sf, x, y, /):
        'x/RR -> y/RR -> x-y'
        # for to_neg6wrap@wrap_around_
        ny = sf.rg_neg_(y)
        return sf.rg_add_(x, ny)

    def wrap_around_or_zero_padding_(sf, sz, to_neg6wrap, to_wrap, to_zero_padding, xs, /):
        if sz == len(xs):
            xs
        elif sz < len(xs):
            if to_zero_padding:
                xs = sf.zero_padding_(sz, xs)
            else:
                xs
        elif sz > len(xs):
            if to_wrap:
                xs = sf.wrap_around_(sz, to_neg6wrap, xs)
            else:
                xs
        return xs
    def zero_padding_(sf, sz, xs, /):
        'sz/uint -> xs/[RR]{len<=sz} -> (xs ++ [0]*(sz-len(xs)))/[RR]{len==sz}'
        if sz <= len(xs):
            return xs
        return sf.mk_list_(chain(xs, repeat(sf.rg_zero, sz -len(xs))))
    def wrap_around_(sf, sz, to_neg6wrap, xs, /):
        'sz/uint -> xs/[RR]{len>=sz} -> (polynomial{xs,X}%(-(-1 if to_neg6wrap else +1)+X**sz)).coeffs/[RR]{len<=sz}'
        if sz >= len(xs):
            return xs
        fs = cycle([sf.rg_sub_, sf.rg_add_]) if to_neg6wrap else repeat(sf.rg_add_)
        it = iter(xs)
        ys = [*islice(it, 0, sz)]
        j = 0
        while j >= 0:
            f = next(fs)
            for j, x in enumerate(islice(it, 0, sz)):
                y = ys[j]
                ys[j] = f(y, x)
        return sf.mk_list_(ys)


    def mk_list_(sf, iterable, /):
        'Iter x -> [x]'
        return list(iterable)
    def truncated_(sf, sz, xs, /):
        'xs/[RR] -> xs[:sz]/[RR]{len<=sz}'
        if len(xs) <= sz:
            return xs
        return xs[:sz]
    def weighted_(sf, w, xs, /):
        'w/RR -> xs/[RR]{len==sz} -> ((w **. [0..<sz]) .*. xs)/[RR]{len==sz}'
        if sf.rg_eq_one_(w):
            return xs
        return sf.mk_list_(_iter_weighted_(sf.rg_mul_, w, xs))


def _iter_weights0_(_rg_mul_, rg_one, w, /):
    yield rg_one
    yield from _iter_weights1_(_rg_mul_, w)
def _iter_weights1_(_rg_mul_, w, /):
    wk = w
    while 1:
        yield wk
        wk = _rg_mul_(wk, w)
def _iter_weighted_(_rg_mul_, w, xs, /):
    xs = iter(xs)
    for x in xs:
        yield x
        break
    else:
        return
    return map(_rg_mul_, xs, _iter_weights1_(_rg_mul_, w))



%zpow
Na <+> Nb := +((-a)+(-b)) == -(a+b)
Na <*> Nb := -(-a)*(-b) == -a*b
zero = 
one = -1
neg_one = +1
g 抽象化 为函数:
    wsum_(g,cs) := sum [c0, g(c1),g(g(c2)), ...]
    wsum_(g,cs) == wsum_(g.g,cs[0::2]) + g(wsum_(g.g,cs[1::2]))
        要求:[g(a+b) == g(a)+g(b)]
    IFFT7zpow要求:(g**(sz///2))(a) == -1



class IOps4convolution7ring_unity_root(IOps4convolution):
    '[RR == the ground ring][pg == the ground unity root]'
    __slots__ = ()
    ###########################
    # common:

    @cache
    @abstractmethod
    def gmk_perfect_div_zpow_(sf, ez4zpow, /):
        'ez4zpow/uint{>0} -> perfect_div_{sz}/(y/RR -> sz**-1*y/RR) # [sz==1<<ez4zpow] # neednot[mul_order_of(pg)%sz == 0] # cache inv...'
        # for IFFT_7zpow_
        # symbolic_DFT 与 mul_order_of(pg) 无关=> gmk_perfect_div_zpow_ 不同于gmk_perfect_div_size_
        raise NotImplementedError

    #@abstractmethod
    def rg_mul7gx_(sf, gx, y, /):
        'gx/uroot/RR -> y/RR -> gx*y/RR'
        # shift{with neg} @symbolic_DFT
        # to mk mul7egR_@FFT_7zpow7recur_
        return sf.rg_mul_(gx, y)
    #@abstractmethod
    def rg_mul7gg_(sf, gx, gy, /):
        'gx/uroot/RR -> gy/uroot/RR -> gx*gy/uroot/RR'
        # add{e4g} @symbolic_DFT
        # to mk gs := ...mk_pows_,_iter_weights0_
        return sf.rg_mul_(gx, gy)
    @cache
    @abstractmethod
    def gmk_uroots6order_(sf, sz, /):
        'sz/uint{>0} -> [g**j | [j:<-[0..<sz]]]/[uroot]/[RR] # [g:=(pg**mul_order_of(pg)///sz)][g**sz==1]'
        # to mk gs := ...mk_pows_,_iter_weights0_
        raise NotImplementedError
        g = sf.uroot5order_(sz, backward=backward)
        gs = islice(_iter_weights0_(sf.rg_mul7gg_, sf.rg_one, g), sz)
        return tuple(gs)

    @cache
    def uroot5order_(sf, order4g, /, *, backward=False):
        'order4g/uint -> (pg**(-1 if backward else +1))**(mul_order_of(pg)///order4g)/uroot/RR'
        #uroot5ez4order_
        order4pg = sf.ground_mul_order
        check_int_ge_le(0, order4pg, order4g)
        (e4g, r) = divmod(order4pg, order4g)
        if r:raise ValueError(order4g, order4pg, r)
        if backward:
            e4g = -e4g
        pg = sf.the_ground_uroot
        return sf.rg_pow7g_(pg, e4g)



    ###########################
    #symbolic_DFT:
    #不太对！应当是 将 symbolic_DFT{ez4sz}的相关数据 缓存到这里，而非 这里的g是symbolic_DFT高层hg
    拆分:zpow{sym},size{pg}
    共通:native


    ###########################
    #impl native FFT convolution for validate
    @property
    @abstractmethod
    def ground_mul_order(sf, /):
        '-> mul_order_of(pg)/uint{>1}'
        raise NotImplementedError
    @property
    @abstractmethod
    def the_ground_uroot(sf, /):
        '-> pg/uroot/RR'
        raise NotImplementedError
    @cache
    @abstractmethod
    def gmk_perfect_div_size_(sf, sz, /):
        'sz/uint{>0} -> perfect_div_{sz}/(y/RR -> sz**-1*y/RR) # [mul_order_of(pg)%sz == 0] # cache inv...'
        # for IFFT_7native_
        # 不对！symbolic_DFT 与 mul_order_of(pg) 无关！！
        raise NotImplementedError
    ###########################




    r'''[[[
    ###########################
    暂时屏蔽无用接口:
    ###########################
    def rg_II_(sf, xs, /):
        'xs/Iter RR -> II(xs)'
        return reduce(sf.rg_mul_, xs, sf.rg_one)
    #@abstractmethod
    ####optional
    def rg_pow_(sf, x, e, /):
        'x/RR -> e/int -> x**e/RR'
        raise NotImplementedError
    ####optional
    # !! rg_inv7sz_,rg_rdiv_size_
    def rg_inv_(sf, x, /):
        'x/RR -> x**-1/RR'
        return sf.rg_pow_(x, -1)
    @cache
    def rg_inv7sz_(sf, sz, /):
        'sz/uint -> sz**-1/RR # [mul_order_of(pg)%sz == 0] # cache inv...'
        assert sz >= 1
        assert sf.ground_mul_order%sz == 0
        x8sz = sf.rg_5int_(sz)
        return sf.rg_inv_(x8sz, -1)
    ####optional
    def rg_rdiv_(sf, x, y, /):
        'x/RR -> y/RR -> x**-1*y/RR'
        inv4x = sf.rg_inv_(x)
        return sf.rg_mul_(inv4x, y)
    ####optional
    def rg_rdiv7ix_(sf, i, y, /):
        'i/int -> y/RR -> i**-1*y/RR'
        x = sf.rg_5int_(i)
        return sf.rg_rdiv_(x, y)
    #@abstractmethod
    def rg_rdiv_size_(sf, sz, y, /):
        'sz/uint -> y/RR -> sz**-1*y/RR # [mul_order_of(pg)%sz == 0] # cache inv...'
        # for IFFT
        return sf.gmk_perfect_div_size_(sz)(y)
        inv4sz = sf.rg_inv7sz_(sz)
        return sf.rg_mul_(inv4sz, y)
        return sf.rg_rdiv7ix_(sz, y)
    @abstractmethod
    def rg_rdiv_zpow_(sf, ez4zpow, y, /):
        'ez4zpow/uint -> y/RR -> 2**-ez4zpow*y/RR'
        # for IFFT_7zpow_
        return sf.gmk_perfect_div_zpow_(ez4zpow)(y)
        if 0:
            #bug:
            sz = 1<<ez4zpow
            return sf.gmk_perfect_div_size_(sz)(y)
        return sf.rg_rdiv7ix_(sz, y)
    def rg_rdiv_two_(sf, y, /):
        'y/RR -> 2**-1*y/RR'
        # to mk acyclic_convolution from {cyclic_convolution&negacyclic_convolution}@split_acyclic_convolution_7zpow_
        return sf.rg_rdiv_zpow_(1, y)

    @abstractmethod
    # !! rg_pow7g_ optional
    def rg_pow7g_(sf, gx, e, /):
        'gx/uroot/RR -> e/int -> gx**e/uroot/RR'
        return sf.rg_pow_(gx, e)
    def rg_inv7g_(sf, gx, /):
        'gx/uroot/RR -> gx**-1'
        return sf.rg_pow7g_(gx, -1)
    #@abstractmethod
    def rg_neg7g_(sf, gx, /):
        'gx/uroot/RR -> -gx'
        return sf.rg_neg_(gx)

    def rg_mul7ix_(sf, i, y, /):
        'i/int -> y/RR -> i*y/RR'
        x = sf.rg_5int_(i)
        return sf.rg_mul_(x, y)
    @abstractmethod
    def rg_5int_(sf, i, /):
        'i/int -> i/RR'
        raise NotImplementedError
    #]]]'''#'''

    @abstractmethod
    def rg_eq_(sf, x, y, /):
        'x/RR -> y/RR -> [x == y]'
        raise NotImplementedError
    def rg_eq_zero_(sf, x, /):
        'x/RR -> [x == 0]'
        return sf.rg_eq_(x, sf.rg_zero)
    def rg_eq_one_(sf, x, /):
        'x/RR -> [x == 1]'
        #used by weighted_()
        return sf.rg_eq_(x, sf.rg_one)
    def rg_eq_neg_one_(sf, x, /):
        'x/RR -> [x == -1]'
        return sf.rg_eq_(x, sf.rg_neg_one)
    #@property
    @CachedProperty
    def rg_zero(sf, /):
        '-> 0/RR' 'for zero_padding_'
        return sf.rg_5int_(0)
    #@property
    @CachedProperty
    def rg_one(sf, /):
        '-> 1/uroot/RR'
        return sf.uroot5order_(1)
        return sf.rg_5int_(1)
        return sf.uroot5ez4order_(0)
    #@property
    @CachedProperty
    def rg_neg_one(sf, /):
        '-> -1/uroot/RR'
        return sf.uroot5order_(2)
        return sf.rg_5int_(-1)
        return sf.uroot5ez4order_(1)
        return sf.rg_neg_(sf.rg_one)

    def dyadic_operator_(sf, op, /, *argss):
        '(*args/[arg]{len=i} -> result) -> (*argss/[[arg]{len=i}]{len=k}) -> [result]{len=k}'
        return sf.mk_list_(map(op, *argss))
    def half_dyadic_operator_(sf, op, x, ys, /):
        '(x -> y -> result) -> ys/[y]{len=k} -> [result]{len=k}'
        return sf.mk_list_(map(curry1(op, x), ys))
    def dyadic_mul_(sf, us, vs, /):
        'us/[RR]{len==sz} -> vs/[RR]{len==sz} -> (us .*. vs)/[RR]{len==sz}'
        return sf.dyadic_operator_(sf.rg_mul_, us, vs)
    def dyadic_add_(sf, us, vs, /):
        'us/[RR]{len==sz} -> vs/[RR]{len==sz} -> (us .+. vs)/[RR]{len==sz}'
        return sf.dyadic_operator_(sf.rg_add_, us, vs)
    def dyadic_sub_(sf, us, vs, /):
        'us/[RR]{len==sz} -> vs/[RR]{len==sz} -> (us .-. vs)/[RR]{len==sz}'
        return sf.dyadic_operator_(sf.rg_sub_, us, vs)
    def dyadic_neg_(sf, vs, /):
        'vs/[RR]{len==sz} -> (-. vs)/[RR]{len==sz}'
        return sf.dyadic_operator_(sf.rg_neg_, vs)
    def half_dyadic_mul_(sf, u, vs, /):
        'u/RR -> vs/[RR]{len==sz} -> (u *. vs)/[RR]{len==sz}'
        return sf.half_dyadic_operator_(sf.rg_mul_, u, vs)
    def half_dyadic_rdiv_size_(sf, sz, vs, /):
        'sz/uint -> vs/[RR]{len==sz} -> (sz**-1 *. vs)/[RR]{len==sz}'
        return sf.dyadic_operator_(sf.gmk_perfect_div_size_(sz), vs)
        return sf.half_dyadic_operator_(sf.rg_rdiv_size_, sz, vs)
    def half_dyadic_rdiv_zpow_(sf, ez4zpow, vs, /):
        'ez4zpow/uint -> vs/[RR]{len==sz} -> (2**-ez4zpow *. vs)/[RR]{len==sz}'
        return sf.dyadic_operator_(sf.gmk_perfect_div_zpow_(ez4zpow), vs)
        if 0:
            #bug:
            sz = 1<<ez4zpow
            return sf.dyadic_operator_(sf.gmk_perfect_div_size_(sz), vs)
        return sf.half_dyadic_operator_(sf.rg_rdiv_zpow_, ez4zpow, vs)
    def dyadic_rdiv_two_(sf, vs, /):
        'vs/[RR]{len==sz} -> (2**-1 *. vs)/[RR]{len==sz}'
        return sf.dyadic_operator_(sf.gmk_perfect_div_zpow_(1), vs)
        return sf.dyadic_operator_(sf.rg_rdiv_two_, vs)


    ###########################
    ###########################
    #API{native}:sz
    ###########################
    ###########################
    def DWT_7native_(sf, sz, w, xs, /, *, backward=False):
        'sz/uint -> w/RR -> xs/[RR]{len==sz} -> DFT{((w **. [0..<sz]) .*. xs)}/[RR]{len==sz}'
        assert len(xs) == sz
        DWT4xs = sf.FFT_7native_(sz, sf.weighted_(w, xs), backward=backward)
        return DWT4xs
    def IDWT_7native_(sf, sz, inv4w, DWT4xs, /, *, backward=False):
        'sz/uint -> w**-1/RR -> DWT4xs/[RR]{len==sz} -> (((w**-1) **. [0..<sz]) .*. IDFT{DWT4xs})/[RR]{len==sz}'
        assert len(DWT4xs) == sz
        xs = sf.weighted_(inv4w, sf.IFFT_7native_(sz, DWT4xs, backward=backward))
        return xs
    def IFFT_7native_(sf, sz, DFT4xs, /, *, backward=False):
        'sz/uint -> DFT4xs{g;xs}/[RR]{len==sz} -> xs/DFT/[RR]{len==sz}  # [g:=sf.uroot5order_(sz, backward=backward)] # [xs == [sz**-1 * sum[DFT4xs[j]*((g**-1)**i)**j | [j:<-[0..<sz]]] | [i:<-[0..<sz]]]]'
        #vs:IFFT_7zpow_
        assert len(DFT4xs) == sz
        sz_xs = sf.FFT_7native_(sz, DFT4xs, backward=not backward)
        xs = sf.half_dyadic_rdiv_size_(sz, sz_xs)
        return xs
    def FFT_7native_(sf, sz, xs, /, *, backward=False):
        'sz/uint -> xs/[RR]{len==sz} -> DFT4xs/DFT{g;xs}/[RR]{len==sz} # [g:=sf.uroot5order_(sz, backward=backward)] # [DFT4xs == [sum[xs[j]*(g**i)**j | [j:<-[0..<sz]]] | [i:<-[0..<sz]]]]'
        #vs:FFT_7zpow_
        assert len(xs) == sz
        if not sz:return sf.mk_list_('')
        if 0:
            g = sf.uroot5order_(sz, backward=backward)
            gs = islice(_iter_weights0_(sf.rg_mul7gg_, sf.rg_one, g), sz)
        else:
            gs = sf.gmk_uroots6order_(sz, backward=backward)
        DFT4xs = sf.mk_list_(sf.rg_sum_(sf.weighted_(gk, xs)) for gk in gs)
        return DFT4xs
class IOps4convolution7symbolic_unity_root(IOps4convolution):
    '[RR == the ground ring][sz == 2**ez4sz]'
    __slots__ = ()
    @property
    @abstractmethod
    def cache4symbolic_DFT_7zpow(sf, /):
        '-> cache4symbolic_DFT/dict # used by {cyclic_convolution__7zpow7recur_,negacyclic_convolution__7zpow7recur_}@symbolic6fancy'
        raise NotImplementedError
    @abstractmethod
    def num_bits4ground_mul_order(sf, /):
        '-> ez4pg/uint{>0} # [ez4pg == log2(mul_order_of(pg))]'
        raise NotImplementedError
    @property
    def ground_mul_order7zpow(sf, /):
        '-> mul_order_of(pg)/uint{>1} # [mul_order_of(pg) == 2**ez4pg]'
        return 1<<sf.num_bits4ground_mul_order
    @property
    @override
    def ground_mul_order(sf, /):
        '-> mul_order_of(pg)/uint{>1}'
        return sf.ground_mul_order7zpow
    @cache
    def uroot5ez4order_(sf, ez4order4g, /, *, backward=False):
        'ez4order4g/uint -> (pg**(-1 if backward else +1))**(mul_order_of(pg)///2**ez4order4g)/uroot/RR'
        #uroot5order_
        ez4order4pg = sf.num_bits4ground_mul_order
        check_int_ge_le(0, ez4order4pg, ez4order4g)
        e4g = 2**(ez4order4pg-ez4order4g)
        if backward:
            e4g = -e4g
        pg = sf.the_ground_uroot
        return sf.rg_pow7g_(pg, e4g)
    @abstractmethod
    @override
    def rg_mul7gx_(sf, gx, y, /):
        'gx/uroot/RR -> y/RR -> gx*y/RR'
        # shift{with neg} @symbolic_DFT
        return sf.rg_mul_(gx, y)
    @abstractmethod
    @override
    def rg_mul7gg_(sf, gx, gy, /):
        'gx/uroot/RR -> gy/uroot/RR -> gx*gy/uroot/RR'
        # add{e4g} @symbolic_DFT
        return sf.rg_mul_(gx, gy)
    @abstractmethod
    @override
    def rg_pow7g_(sf, gx, e, /):
        'gx/uroot/RR -> e/int -> gx**e/uroot/RR'
        return sf.rg_pow_(gx, e)
    @abstractmethod
    @override
    def rg_neg7g_(sf, gx, /):
        'gx/uroot/RR -> -gx'
        return sf.rg_neg_(gx)


    ###########################
    ###########################
    #API{zpow}:ez4sz
    ###########################
    ###########################
    def DWT_7zpow_(sf, ez4sz, w, xs, /, *, backward=False):
        'ez4sz/uint -> w/RR -> xs/[RR]{len==sz} -> DFT{((w **. [0..<sz]) .*. xs)}/[RR]{len==sz}'
        assert len(xs) == 1<<ez4sz
        DWT4xs = sf.FFT_7zpow_(ez4sz, sf.weighted_(w, xs), backward=backward)
        return DWT4xs
    def IDWT_7zpow_(sf, ez4sz, inv4w, DWT4xs, /, *, backward=False):
        'ez4sz/uint -> w**-1/RR -> DWT4xs/[RR]{len==sz} -> (((w**-1) **. [0..<sz]) .*. IDFT{DWT4xs})/[RR]{len==sz}'
        assert len(DWT4xs) == 1<<ez4sz
        xs = sf.weighted_(inv4w, sf.IFFT_7zpow_(ez4sz, DWT4xs, backward=backward))
        return xs
    def IFFT_7zpow_(sf, ez4sz, DFT4xs, /, *, backward=False):
        'ez4sz/uint -> DFT4xs{g;xs}/[RR]{len==sz} -> xs/DFT/[RR]{len==sz} # [sz==2**ez4sz] # [g:=sf.uroot5ez4order_(ez4sz, backward=backward)] # [xs == [sz**-1 * sum[DFT4xs[j]*((g**-1)**i)**j | [j:<-[0..<sz]]] | [i:<-[0..<sz]]]]'
        assert len(DFT4xs) == 1<<ez4sz
        sz_xs = sf.FFT_7zpow_(ez4sz, DFT4xs, backward=not backward)
        xs = sf.half_dyadic_rdiv_zpow_(ez4sz, sz_xs)
        return xs
    def FFT_7zpow_(sf, ez4sz, xs, /, *, backward=False):
        'ez4sz/uint -> xs/[RR]{len==sz} -> DFT4xs/DFT{g;xs}/[RR]{len==sz} # [sz==2**ez4sz] # [g:=sf.uroot5ez4order_(ez4sz, backward=backward)] # [DFT4xs == [sum[xs[j]*(g**i)**j | [j:<-[0..<sz]]] | [i:<-[0..<sz]]]]'
        #vs:FFT_7native_
        sz = 1<<ez4sz
        assert len(xs) == sz
        if 0:
            g = sf.uroot5ez4order_(ez4sz, backward=backward)
            gs = [*islice(_iter_weights0_(sf.rg_mul7gg_, sf.rg_one, g), sz)]
        gs = sf.gmk_uroots6order_(sz, backward=backward)
        #.return sf.mk_list_(FFT__bit_scramble__len_is_zpow(sf.rg_neg_, sf.rg_add_, sf.rg_mul_, g, xs, may_gs=gs))
        mul7egR_ = mk__mul7egR_(sf.rg_mul_, ez4sz, gs)
        return FFT_7zpow7recur_(mul7egR_, sf.rg_add_, e4g:=1, ez4sz, xs, backward=False, mk=sf.mk_list_)
    def bothcyclic_convolution_7zpow_(sf, ez4sz, us, vs, /, **kwds4wcc):
        # to_neg6wrap=False
        wsP = sf.cyclic_convolution_7zpow_(ez4sz, us, vs, **kwds4wcc)
            #cyclic_convolution
        wsN = sf.negacyclic_convolution_7zpow_(ez4sz, us, vs, **kwds4wcc)
            #negacyclic_convolution
        return (wsP, wsN)
    def split_acyclic_convolution_7zpow_(sf, ez4sz, us, vs, /, **kwds4wcc):
        (wsP, wsN) = sf.bothcyclic_convolution_7zpow_(ez4sz, us, vs, **kwds4wcc)
        wsL = sf.dyadic_rdiv_two_(sf.dyadic_add_(wsP, wsN))
        wsR = sf.dyadic_rdiv_two_(sf.dyadic_sub_(wsP, wsN))
        return (wsL, wsR)
    def acyclic_convolution_7zpow_(sf, ez4sz, us, vs, /, **kwds4wcc):
        'ez4sz/uint -> us/[RR] -> vs/[RR] -> (polynomial{us,X} * polynomial{vs,X} %(0+X**sz)).coeffs/[RR]{len==sz} # truncated'
        sz = 1<<ez4sz
        us = sf.truncated_(sz, us)
        vs = sf.truncated_(sz, vs)
        n = -1+len(us)+len(vs)
        ez4n = ceil_log2(n)
        ws = sf.cyclic_convolution_7zpow_(ez4n, us, vs, to_zero_padding=True)
        ws = sf.truncated_(sz, ws)
        ws = sf.zero_padding_(sz, ws)
        return ws

    def cyclic_convolution_7zpow_(sf, ez4sz, us, vs, /, **kwds4wcc):
        'ez4sz/uint -> us/[RR]{len==sz} -> vs/[RR]{len==sz} -> (polynomial{us,X} * polynomial{vs,X} %(-1+X**sz)).coeffs/[RR]{len==sz} # wrap_around'
        inv4w = w = sf.rg_one
        wsP = sf.weighted_cyclic_convolution_7zpow_(ez4sz, w, inv4w, us, vs, **kwds4wcc)
        return wsP
    def negacyclic_convolution_7zpow_(sf, ez4sz, us, vs, /, **kwds4wcc):
        'ez4sz/uint -> us/[RR]{len==sz} -> vs/[RR]{len==sz} -> (polynomial{us,X} * polynomial{vs,X} %(+1+X**sz)).coeffs/[RR]{len==sz} # wrap_around'
        hg = sf.uroot5ez4order_(1+ez4sz)
        inv4hg = sf.uroot5ez4order_(1+ez4sz, backward=True)
        wsN = sf.weighted_cyclic_convolution_7zpow_(ez4sz, hg, inv4hg, us, vs, **kwds4wcc)
        return wsN
    def weighted_cyclic_convolution_7zpow_(sf, ez4sz, w, inv4w, us, vs, /, *, to_wrap=False, to_zero_padding=False, auto_vs_fancy_vs_native=_default4auto_vs_fancy_vs_native, symbolic6fancy=False):
        'ez4sz/uint -> w/RR -> us/[RR]{len==sz} -> vs/[RR]{len==sz} -> (polynomial{us,X} * polynomial{vs,X} %(-(w**+sz)+X**sz)).coeffs/[RR]{len==sz}' # API changed: 『w**-sz』-->『w**+sz』
        fancy_vs_native = sf.explain__auto_vs_fancy_vs_native__6weighted_cyclic_convolution_7zpow_(ez4sz, len(us), len(vs), auto_vs_fancy_vs_native)
        if fancy_vs_native:
            #native:
            sf.weighted_cyclic_convolution_7native_
            ...
            raise NotImplementedError
        if not (to_wrap or to_zero_padding):
            # strict
            if not len(us) == len(vs) == sz:raise ValueError(len(us), len(vs), sz)

        #fancy:
        sz = 1<<ez4sz
        ##################
        us7w = sf.weighted_(w, us)
        vs7w = sf.weighted_(w, vs)
        ##################
        # weighted_() before wrap_around_()
        ##################
        if to_wrap or to_zero_padding:
            # casual
            us7w = sf.wrap_around_or_zero_padding_(sz, to_neg6wrap:=False, to_wrap, to_zero_padding, us7w)
            vs7w = sf.wrap_around_or_zero_padding_(sz, to_neg6wrap:=False, to_wrap, to_zero_padding, vs7w)
        else:
            # strict
            if not len(us7w) == len(vs7w) == sz:raise ValueError
        assert len(us7w) == sz
        assert len(vs7w) == sz
        ##################
        if not symbolic6fancy:
            # via FFT{g}
            # not use DWT_7zpow_ directly <<== wrap_around_() not inside DWT_7zpow_()
            DWT4us = sf.FFT_7zpow_(ez4sz, us7w)
            DWT4vs = sf.FFT_7zpow_(ez4sz, vs7w)
            DWT4ws = sf.dyadic_mul_(ez4sz, DWT4us, DWT4vs)
            ws7w = sf.IFFT_7zpow_(ez4sz, DWT4ws)
        else:
            # via symbolic_DFT{g}
            ws7w = sf.cyclic_convolution__7zpow7recur_(ez4sz, us7w, vs7w)
        ws7w
        ws = sf.weighted_(inv4w, ws7w)
        return ws
    def cyclic_convolution__7zpow7recur_(sf, ez4sz, us, vs, /, *, may_min_ez4recur=_default_min_ez4recur):
        'ez4sz/uint -> us/[RR]{len==sz} -> vs/[RR]{len==sz} -> (polynomial{us,X} * polynomial{vs,X} %(-1+X**sz)).coeffs/[RR]{len==sz} #via:symbolic_DFT'
        fancy_vs_native = sf.explain__may_min_ez4recur_7zpow_(ez4sz, may_min_ez4recur)
        if fancy_vs_native:
            #native:
            ...
            raise NotImplementedError
        #fancy:
        assert ez4sz >= 2
        raise NotImplementedError

    def negacyclic_convolution__7zpow7recur_(sf, ez4sz, us, vs, /, *, may_min_ez4recur=_default_min_ez4recur):
        'ez4sz/uint -> us/[RR]{len==sz} -> vs/[RR]{len==sz} -> (polynomial{us,X} * polynomial{vs,X} %(+1+X**sz)).coeffs/[RR]{len==sz} #via:symbolic_DFT'
        fancy_vs_native = sf.explain__may_min_ez4recur_7zpow_(ez4sz, may_min_ez4recur)
        if fancy_vs_native:
            #native:
            ...
            raise NotImplementedError
        #fancy:
        assert ez4sz >= 2
        em = ez4sz
        ew = em//2
        en = em-ew
        ed = en-ew
        # [t**W==z][t**M==z**N==-1]
        ez4order4z = 1+en
        z = _mk_z5ez4order_(sf, ez4order4z)
        tW = z

        if ed == 0:
            #symFNN0
            #=> 原版symFNN0:[em%2==0][en==ew][t**W==z][t**M==z**N==z**W==-1][hg:=z]
            # => 递归调用 同于高层，仍然是 圆负卷积{N}
            hg = z
        else:
            #symFNN1
            #=> 原版symFNN1:[em%2==1][en==1+ew][t**W==z][t**M==z**N==-1][(z**2)**W==-1][hg:=z**2]
            # => 递归调用 同于高层，仍然是 圆负卷积{N}
            hg = zz = _mk_z5ez4order_(sf, -1+ez4order4z)
        RzX = _RzN(sf, ez4order4z, en)
        RzX, ez4order4z, z, hg, tW
        return _4recur(sf, RzX, ez4order4z, z, hg, ew, tW, us, vs)


    def explain__may_min_ez4recur_7zpow_(sf, ez4sz, may_min_ez4recur, /):
        '-> fancy_vs_native/bool'
        if may_min_ez4recur is None:
            min_ez4recur = _default_min_ez4recur
        min_ez4recur = max(2, min_ez4recur)
        fancy_vs_native = ez4sz < min_ez4recur
        return fancy_vs_native
    def explain__auto_vs_fancy_vs_native__6weighted_cyclic_convolution_7zpow_(sf, ez4sz, sz4us, sz4vs, auto_vs_fancy_vs_native, /):
        '-> fancy_vs_native/bool'
        #weighted_cyclic_convolution_7zpow_
        match auto_vs_fancy_vs_native:
            case -1:
                #auto
                (sz4us, sz4vs) = sorted([sz4us, sz4vs])
                fancy_vs_native = sz4vs < 4 or sz4us < 2+sz4vs.bit_length()
            case 0 | 1:
                fancy_vs_native = bool(fancy_vs_native)
            case _:
                raise ValueError(auto_vs_fancy_vs_native)
        return fancy_vs_native
#class
def _inv_transpose(ops7RR, RzX, W, us7RzX, /):
    assert W == len(us7RzX)
    N = len(us7RzX[0])
    us = ops7RR.mk_list_(us7RzX[j][i] for i in range(N) for j in range(W))
    return us
def _transpose(ops7RR, RzX, W, us, /):
    us7RzX = ops7RR.mk_list_(RzX(us[j::W]) for j in range(W))
    return us7RzX
def _4recur(ops7RR, RzX, ez4order4z, z, hg, ew, tW, us, vs, /):
    W = 1<<ew
    us7RzX = _transpose(ops7RR, RzX, W, us)
    vs7RzX = _transpose(ops7RR, RzX, W, vs)
    ops7RzX = _Ops4symbolic_DFT7zpow(ops7RR, RzX, ez4order4z, z)
    # !! [g exists]
    # => [symbolic6fancy=False]
    (wsL_7RzX, wsR_7RzX) = ops7RzX.split_acyclic_convolution_7zpow_(ew, us7RzX, vs7RzX, symbolic6fancy=False)
    #ws = wsL .+. (tW *. wsR)
    ws7RzX = ops7RzX.dyadic_add_(wsL_7RzX, ops7RzX.half_dyadic_mul_(tW, wsR_7RzX))
    ws = _inv_transpose(ops7RR, RzX, W, ws7RzX)
    return ws

def _RzN(ops7RR, ez4order4z, en, /):
    d = ops7RR.cache4symbolic_DFT_7zpow
    k = _RzN
    try:
        return d[k][en]
    except KeyError:
        pass
    en2RzN = d.setdefault(k, {})
    assert ez4order4z == 1+en # == 1+ew
    class RzN(tuple):
        '[z**(2**en) == -1]'
        _en = en
        _2N = 1<<(1+en)
        _N = 1<<(en)
        _ops7RR = ops7RR
        _rg_neg_ = ops7RR.rg_neg_
        _rg_add_ = ops7RR.rg_add_
        _rg_sub_ = ops7RR.rg_sub_
        __mul__ = None
        __add__ = None
        __rmul__ = None
        __radd__ = None
        __imul__ = None
        __iadd__ = None
        def rz_sub_(sf, ot, /):
            return __class__(map(sf._rg_sub_, sf, ot))
        def rz_add_(sf, ot, /):
            return __class__(map(sf._rg_add_, sf, ot))
        def rz_gmul_(sf, g, /):
            _2N = sf._2N
            N = sf._N
            e4g = g%_2N
            if e4g > N:
                e4g -= _2N
            # [g == z**e4g]
            if e4g == 0:
                return sf
            rg_neg_ = sf._rg_neg_
            if e4g == N:
                return __class__(map(rg_neg_, sf))
            xsL = sf[:-e4g]
            xsH = sf[-e4g:]
            if 0 < e4g < N:
                #rshift
                xsH = map(rg_neg_, xsH)
            else:
                #lshift
                xsL = map(rg_neg_, xsL)
            return __class__(chain(xsH, xsL))

    en2RzN[en] = RzN
    #return RzX
    return _RzN(en)
def _RzP(ops7RR, ez4order4z, en, /):
    raise ...
    return RzX
def _mk_z5ez4order_(ops7RR, ez4order4z, /):
    #z = _4z(ez4order4z)
    z = _4z(1)
    return z
class _4z(int):pass
class _Ops4symbolic_DFT7zpow(IOps4symbolic_DFT7zpow):
    ___no_slots_ok___ = True
    def __init__(sf, ops7RR, RzX, ez4order4z, z, /):
        pass
#check_non_ABC(_Ops4symbolic_DFT7zpow)
    # ['FFT_7zpow_', 'cache4symbolic_DFT_7zpow', 'num_bits4ground_mul_order', 'the_ground_uroot', 'rg_5int_', 'rg_add_', 'rg_eq_', 'rg_mul7gg_', 'rg_mul7gx_', 'rg_mul_', 'rg_neg7g_', 'rg_neg_', 'rg_pow7g_', 'rg_rdiv_size_', 'rg_rdiv_zpow_']

class Ops4symbolic_DFT7zpow__7ring_is_ZZ(IOps4symbolic_DFT7zpow):
    '[RR := ZZ]'
    ___no_slots_ok___ = True
    @property
    def num_bits4ground_mul_order(sf, /):
        return 1
    @property
    def the_ground_uroot(sf, /):
        return -1
    def rg_neg_(sf, x, /):
        return -x
    def rg_add_(sf, x, y, /):
        return x+y
    def rg_sub_(sf, x, y, /):
        return x-y
    def rg_mul_(sf, x, y, /):
        return x*y
    def rg_pow_(sf, x, e, /):
        return x**e
    def rg_5int_(sf, i, /):
        return i
    def rg_eq_(sf, x, y, /):
        return x == y
    @CachedProperty
    def cache4symbolic_DFT_7zpow(sf, /):
        return {}
    @override
    def rg_mul7gx_(sf, gx, y, /):
        'gx/uroot/RR -> y/RR -> gx*y/RR'
        # shift{with neg} @symbolic_DFT
        return sf.rg_mul_(gx, y)
    @override
    def rg_mul7gg_(sf, gx, gy, /):
        'gx/uroot/RR -> gy/uroot/RR -> gx*gy/uroot/RR'
        # add{e4g} @symbolic_DFT
        return sf.rg_mul_(gx, gy)
    @override
    def rg_pow7g_(sf, gx, e, /):
        'gx/uroot/RR -> e/int -> gx**e/uroot/RR'
        return sf.rg_pow_(gx, e)
    @override
    def rg_neg7g_(sf, gx, /):
        'gx/uroot/RR -> -gx'
        return sf.rg_neg_(gx)
    def rg_rdiv_(sf, x, y, /):
        (q, r) = divmod(x, y)
        if r:raise ValueError(x, y)
        return q
    def rg_rdiv7ix_(sf, i, y, /):
        return sf.rg_rdiv_(i, y)
    def rg_rdiv_size_(sf, sz, y, /):
        ez4sz = floor_log2(sz)
        if sz == 1<<ez4sz:raise ValueError(sz)
        return sf.rg_rdiv_zpow_(ez4sz, y)
    def rg_rdiv_zpow_(sf, ez4zpow, y, /):
        q = y >> ez4zpow
        if y == q<<ez4zpow:raise ValueError(ez4zpow, y)
        return q
        return sf.rg_rdiv7ix_(1<<ez4zpow, y)
check_non_ABC(Ops4symbolic_DFT7zpow__7ring_is_ZZ)


__all__
from seed.algo.FFT.convolution__7symbolic_DFT import *
