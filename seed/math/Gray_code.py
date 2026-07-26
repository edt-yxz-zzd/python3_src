#__all__:goto
#code6FXT:goto
r'''[[[
e ../../python3_src/seed/math/Gray_code.py
格雷码-->孤变码

seed.math.Gray_code
py -m nn_ns.app.debug_cmd   seed.math.Gray_code -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.Gray_code:__doc__ -ht # -ff -df
#######

[[
come_from:
view script/整数分解牜允许快速求值的多根多项式.py
]]

[[
[parity_of(Gray_code[k]) == Gray_code[k].bit_count()%2]
[parity_of(Gray_code[k]) == k%2]

[Gray_code[2*k] == Gray_code[k]*2 + k%2]
[Gray_code[2*k] == Gray_code[k]*2 + parity_of(Gray_code[k])]
    #步进:外部状态->内部状态
[Gray_code[k] == Gray_code[2*k] >> 1]
    #步进:内部状态->外部状态
    #步进:内部状态:Gray_code[2*k]
    #步进:外部状态:Gray_code[k]

[Gray_code[2*(1+k)] == (Gray_code[2*k]^1) ^ (lowest_1bit_of(Gray_code[2*k]^1) << 1)]
    #偶步进:内部状态->内部状态
[Gray_code[2*(-1+k)] == (Gray_code[2*k]^1) ^ (lowest_1bit_of(Gray_code[2*k]) << 1)]
    #偶步退:内部状态->内部状态

爻位牜变更:
[Gray_code[0+2*k]^Gray_code[1+2*k] == 1]
    # 偶进奇or奇退偶
[Gray_code[1+2*k]^Gray_code[2+2*k] == (lowest_1bit_of(Gray_code[1+2*k])<<1) == (lowest_1bit_of(Gray_code[2+2*k])<<1)]
    # 奇进偶or偶退奇

[Gray_code[1+k] == if 0==parity_of(Gray_code[k]) then Gray_code[k]^1 else Gray_code[k]^(lowest_1bit_of(Gray_code[k])<<1)]
    #慢步进:步进定义
[Gray_code[-1+k] == if 1==parity_of(Gray_code[k]) then Gray_code[k]^1 else Gray_code[k]^(lowest_1bit_of(Gray_code[k])<<1)]
    #慢步退:步退定义

[@[k,ez::uint] -> [Gray_code[k] == 2**ez] -> [k==-1+2**(1+ez)][k%2==1==parity_of(Gray_code[k])][Gray_code[1+k] == 3*2**ez][Gray_code[-1+k] == (2**ez)^1 == (1+2**ez) if ez > 0 else 0]]
    # ==>> 奇进偶:最低阳爻 前一位 反转 的 根源
    [[proof:[@[k,ez::uint] -> [Gray_code[k] == 2**ez] -> [k==-1+2**(1+ez)]]
    * [ez==0]:
        [k==1]
        ok
    * [ez==1]:
        [k==3]
        ok
    * [u:<-[0..]][ez==2+u][@[_ez :<-[0..<ez]] -> @[_k::uint] -> [Gray_code[_k] == 2**_ez] -> [_k==-1+2**(1+_ez)]]:
        !! [ez >= 1]
        # [_ez:=-1+ez]
        [Gray_code[-1+2**ez] == 2**(-1+ez)]
        [Gray_code[2**ez] == 3*2**(-1+ez)]
        !! [ez >= 2]
        # [_ez:=-2+ez]
        [Gray_code[-1+2**(-1+ez)] == 2**(-2+ez)]
        [Gray_code[2**(-1+ez)] == 3*2**(-2+ez)]
        !! 此后一段，最低(-1+ez)爻元 面临的奇偶环境与[_k:<-[0..<2**ez]]相同
        !! [ez >= 2]
        [@[_k:<-[0..<2**ez]] -> [Gray_code[2**ez+_k] == 3*2**(-1+ez) ^ Gray_code[_k] == (3*2**(-1+ez) + Gray_code[_k]) + (-[_k >= 2**(-1+ez)]*2**ez)]]
        # [_k:=-1+2**ez]
        [Gray_code[-1+2**(1+ez)] == 3*2**(-1+ez) ^ Gray_code[-1+2**ez] == 2**ez]
    ==>>:
    [@[k,ez::uint] -> [Gray_code[k] == 2**ez] -> [k==-1+2**(1+ez)]]
    DONE
    ]]

[@[ez::uint] -> @[k:<-[0..<2**ez]] -> [Gray_code[2**ez+k] == 3*2**(-1+ez) ^ Gray_code[k] == (3*2**(-1+ez) + Gray_code[k]) + (-[k >= 2**(-1+ez)]*2**ez)]]
    # 证明:见上面: (3*2**(-1+ez))前缀 使得 后续一段时间的奇偶环境与之前一段相同，因而低位复制
    # 考察角度:生成序列:类似 牛顿迭代，翻倍复制
    # 考察角度:求值:位次讠孤变码扌:递归:
    ==>>:
[@[k::uint] -> [Gray_code[k] == (k & k>>1)]]
    # 证明:递归使用上面的定理
]]

[[
see also:
view others/数学/involution自逆函数.txt
    blue code
    yellow code
    red code
    green code
    #Note the names ‘blue code’ etc.  are ad hoc terminology and not standard.

]]
[[
FXT:
fxtbook:page41[53/978]
static inline ulong gray_code(ulong x){ return x ^ (x>>1); }
Gray codes of consecutive values differ in one bit.
Gray codes of values that differ by a power of 2 differ in two bits.
Gray codes of even/odd values have an even/odd number of bits set, respectively.
To produce a random value with an even/odd number of bits set, set the lowest bit of a random number to 0/1, respectively, and return its Gray code.


Computing the inverse Gray code is slightly more expensive.
    As the Gray code is the bit-wise difference modulo 2, we can compute the inverse as bit-wise sums modulo 2:
    #ver1:see below
    #   二进制型:本爻位讠高侧的奇偶性

For n-bit words, n-fold application of the Gray code gives back the original word.
    Using the symbol G for the Gray code (operator), we have G^n= id, so G^(n−1)◦G = id = G^(−1)◦G.
    That is, applying the Gray code computation (n-1) times gives the inverse Gray code.
    Thus we can simplify to:
    #ver2:see below
    #   算子串联趃用
    #   [格雷算子 :: 位次 -> 格雷码]
    #       串联:格雷码 强制改变类型 成为 位次
    #   最高位 分身下行 => [(格雷算子**ceil_zpow_(1+floor_log2(位次)))(位次) == 位次]
    #   最高位不变:1->1;2->3->2;4->6->5->7->4;(8->10->15->8),(9->11->14->9);
[f(x)::多项式乊模二]:
    [格雷算子(f(x)) == (f(x)*(x+1) -f(0))///x == f(x)+(f(x)-f(0))///x == f(x)*(x+1)//x == (f(x) +f(x)//x)]
    [(格雷算子**2)(f(x))
    == 格雷算子(f(x) +f(x)//x)
    == ((f(x) +f(x)//x) +(f(x) +f(x)//x)//x)
    == (f(x) +f(x)//x +f(x)//x +f(x)//x**2)
    == (f(x) +f(x)//x**2)
    ]
    [(格雷算子**4)(f(x))
    == (格雷算子**2)(f(x) +f(x)//x**2)
    == (f(x) +f(x)//x**4)
    ]
    [(格雷算子**2**k)(f(x)) == (f(x) +f(x)//x**2**k)]
    [(格雷算子**2**k)(f(x)) == f(x)]:
        <==> [(f(x) +f(x)//x**2**k) == f(x)]
        <==> [(f(x)//x**2**k) == 0]
        <==> [[f(x) =!= 0] -> [0 <= deg(f(x)) < 2**k]]
        <==> [[f(x) =!= 0] -> [1 <= 1+deg(f(x)) <= 2**k]]
        <==> [[f(x) =!= 0] -> [0 <= log2(1+deg(f(x))) <= k]]
        <==> [[f(x) =!= 0] -> [0 <= ceil_log2(1+deg(f(x))) <= k]]
        <==> [[f(x) =!= 0] -> [1 <= 2**(ceil_log2(1+deg(f(x)))) <= 2**k]]
        <==> [[f(x) =!= 0] -> [周期纟格雷算子乊{f(x)} == 2**(ceil_log2(1+deg(f(x))))]]
    [[位次 =!= 0] -> [周期纟格雷算子乊{位次} == 2**(ceil_log2(1+floor_log2(位次)))]]
[[位次 =!= 0] -> [周期纟格雷算子乊{位次} == (ceil_zpow_(1+floor_log2(位次)))]]
    位次讠周期纟孤变码扌:goto
]]
[[
===
fxtbook:page172[184/978]
In a minimal-change order the amount of change between successive objects is the least possible.
  Such an order is also called a (combinatorial) Gray code.
  There is in general more than one such order.
  Often we can impose even stricter conditions, like that (with permutations) the changes are between adjacent positions.
  The corresponding order is a strong minimal-change order.
  A very readable survey of Gray codes is given in [343], see also [298].
[343] Timothy Walsh:Generating Gray codes in O(1) worst-case time per word, In: DMTCS 2003, C. S. Calude et al. (eds.), Lecture Notes in Computer Science, vol.2731, pp.73-88, (2003). 172
[298] Carla Savage:A Survey of Combinatorial Gray Codes, SIAM Review, vol.39, no.4, pp.605-629, (December-1997). URL: http://www.csc.ncsu.edu/faculty/savage/papers.html. 172, 264
===
]]



'#'; __doc__ = r'#'
位次讠孤变码扌
    位次巛孤变码扌
        位次讠孤变码牜趃用扌
            位次讠周期纟孤变码扌

>>> ls = [*趃孤变码巛趃位次扌(range(32))]
>>> ls
[0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8, 24, 25, 27, 26, 30, 31, 29, 28, 20, 21, 23, 22, 18, 19, 17, 16]
>>> [*map(位次巛孤变码扌, ls)] == [*range(32)]
True
>>> 位次讠孤变码牜趃用扌(3, 4)
7
>>> 位次讠周期纟孤变码扌(4)
4
>>> 位次讠周期纟孤变码扌(-1+2**32)
32
>>> 位次讠周期纟孤变码扌(2**32)
64
>>> 位次讠周期纟孤变码扌(-1+2**64)
64
>>> 位次讠周期纟孤变码扌(2**64)
128
>>> len(制表冫孤变循环扌(2**64))
128
>>> len(制表冫孤变循环扌(-1+2**64))
64














奇偶性纟
最低阳爻纟
>>> [奇偶性纟(u) for u in range(17)]
[0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1]
>>> [最低阳爻纟(u) for u in range(1,17)]
[1, 2, 1, 4, 1, 2, 1, 8, 1, 2, 1, 4, 1, 2, 1, 16]

孤变码讠孤变码牜偶位扌
孤变码巛孤变码牜偶位扌
>>> ls = [(孤变码, 孤变码讠孤变码牜偶位扌(孤变码)) for 孤变码 in range(17)]
>>> ls
[(0, 0), (1, 3), (2, 5), (3, 6), (4, 9), (5, 10), (6, 12), (7, 15), (8, 17), (9, 18), (10, 20), (11, 23), (12, 24), (13, 27), (14, 29), (15, 30), (16, 33)]
>>> [孤变码 for 孤变码, 孤变码牜偶位 in ls if not 孤变码巛孤变码牜偶位扌(孤变码牜偶位) == 孤变码]
[]


偶步退冫孤变码牜偶位扌
偶步进冫孤变码牜偶位扌
>>> from seed.iters.iterate import iterate
>>> ls = [*iterate(偶步进冫孤变码牜偶位扌, 0,  0,17)]
>>> ls
[0, 3, 6, 5, 12, 15, 10, 9, 24, 27, 30, 29, 20, 23, 18, 17, 48]
>>> rs = [*iterate(偶步退冫孤变码牜偶位扌, 48,  0,17)]
>>> rs
[48, 17, 18, 23, 20, 29, 30, 27, 24, 9, 10, 15, 12, 5, 6, 3, 0]
>>> ls == rs[::-1]
True
>>> 偶步退冫孤变码牜偶位扌(0)
Traceback (most recent call last):
    ...
TypeError: 0





慢步退冫孤变码扌
慢步进冫孤变码扌
>>> ls = [*iterate(慢步进冫孤变码扌, 0,  0,17)]
>>> ls
[0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8, 24]
>>> rs = [*iterate(慢步退冫孤变码扌, 24,  0,17)]
>>> rs
[24, 8, 9, 11, 10, 14, 15, 13, 12, 4, 5, 7, 6, 2, 3, 1, 0]
>>> ls == rs[::-1]
True
>>> 慢步退冫孤变码扌(0)
Traceback (most recent call last):
    ...
TypeError: 0


趃步退冫孤变码牜偶位扌
趃步进冫孤变码牜偶位扌
>>> from itertools import islice
>>> ls = [*islice(趃步进冫孤变码牜偶位扌(0), 0,17)]
>>> ls
[0, 3, 6, 5, 12, 15, 10, 9, 24, 27, 30, 29, 20, 23, 18, 17, 48]
>>> rs = [*趃步退冫孤变码牜偶位扌(48)]
>>> ls == rs[::-1]
True


趃步退冫孤变码扌
趃步进冫孤变码扌
>>> ls = [*islice(趃步进冫孤变码扌(0), 0,17)]
>>> ls
[0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8, 24]
>>> rs = [*趃步退冫孤变码扌(24)]
>>> ls == rs[::-1]
True














趃步退冫爻位栈冃孤变码扌
趃步进冫爻位栈冃孤变码扌
    步退冫爻位栈冃孤变码扌
    步进冫爻位栈冃孤变码扌
>>> stk = []
>>> for _ in range(9):
...     步进冫爻位栈冃孤变码扌(stk)
...     stk
0
[0]
1
[1, 0]
0
[1]
2
[2, 1]
0
[2, 1, 0]
1
[2, 0]
0
[2]
3
[3, 2]
0
[3, 2, 0]
>>> for _ in range(9):
...     步退冫爻位栈冃孤变码扌(stk)
...     stk
0
[3, 2]
3
[2]
0
[2, 0]
1
[2, 1, 0]
0
[2, 1]
2
[1]
0
[1, 0]
1
[0]
0
[]

>>> stk = []
>>> it = islice(趃步进冫爻位栈冃孤变码扌(stk), 0,17)
>>> for j in it:
...     j
...     stk
0
[0]
1
[1, 0]
0
[1]
2
[2, 1]
0
[2, 1, 0]
1
[2, 0]
0
[2]
3
[3, 2]
0
[3, 2, 0]
1
[3, 2, 1, 0]
0
[3, 2, 1]
2
[3, 1]
0
[3, 1, 0]
1
[3, 0]
0
[3]
4
[4, 3]
0
[4, 3, 0]
>>> it = islice(趃步退冫爻位栈冃孤变码扌(stk), 0,17)
>>> for j in it:
...     j
...     stk
0
[4, 3]
4
[3]
0
[3, 0]
1
[3, 1, 0]
0
[3, 1]
2
[3, 2, 1]
0
[3, 2, 1, 0]
1
[3, 2, 0]
0
[3, 2]
3
[2]
0
[2, 0]
1
[2, 1, 0]
0
[2, 1]
2
[1]
0
[1, 0]
1
[0]
0
[]





























































































[[
py_adhoc_call   seed.math.Gray_code   ,趃制表冫孤变循环扌  ='[0,1,2,4,8,9,16,18,32,33,36,37]'
    (0,)
    (1,)
    (2, 3)
    (4, 6, 5, 7)
    (8, 12, 10, 15)
    (9, 13, 11, 14)
    (16, 24, 20, 30, 17, 25, 21, 31)
    (18, 27, 22, 29, 19, 26, 23, 28)
    (32, 48, 40, 60, 34, 51, 42, 63)
    (33, 49, 41, 61, 35, 50, 43, 62)
    (36, 54, 45, 59, 38, 53, 47, 56)
    (37, 55, 44, 58, 39, 52, 46, 57)
py_adhoc_call   seed.math.Gray_code   ,趃制表冫孤变循环扌  ='[64,128,256]'
    (64, 96, 80, 120, 68, 102, 85, 127)
    (128, 192, 160, 240, 136, 204, 170, 255)
    (256, 384, 320, 480, 272, 408, 340, 510, 257, 385, 321, 481, 273, 409, 341, 511)
py_adhoc_call   seed.math.Gray_code   ,趃制表冫孤变循环扌 +欤带周期 ='[2**e for e in range(13)]'
    (1, (1,))
    (2, (2, 3))
    (4, (4, 6, 5, 7))
    (4, (8, 12, 10, 15))
    (8, (16, 24, 20, 30, 17, 25, 21, 31))
    (8, (32, 48, 40, 60, 34, 51, 42, 63))
    (8, (64, 96, 80, 120, 68, 102, 85, 127))
    (8, (128, 192, 160, 240, 136, 204, 170, 255))
    (16, (256, 384, 320, 480, 272, 408, 340, 510, 257, 385, 321, 481, 273, 409, 341, 511))
    (16, (512, 768, 640, 960, 544, 816, 680, 1020, 514, 771, 642, 963, 546, 819, 682, 1023))
    (16, (1024, 1536, 1280, 1920, 1088, 1632, 1360, 2040, 1028, 1542, 1285, 1927, 1092, 1638, 1365, 2047))
    (16, (2048, 3072, 2560, 3840, 2176, 3264, 2720, 4080, 2056, 3084, 2570, 3855, 2184, 3276, 2730, 4095))
    (16, (4096, 6144, 5120, 7680, 4352, 6528, 5440, 8160, 4112, 6168, 5140, 7710, 4369, 6553, 5461, 8191))

]]

py_adhoc_call   seed.math.Gray_code   @f
]]]'''#'''
__all__ = r'''
趃孤变码巛趃位次扌
    位次讠孤变码扌
    位次巛孤变码扌
        位次讠孤变码牜趃用扌
            位次讠周期纟孤变码扌

趃制表冫孤变循环扌
    制表冫孤变循环扌
        趃用孤变至循环扌



趃步退冫孤变码扌
趃步进冫孤变码扌
    趃步退冫孤变码牜偶位扌
    趃步进冫孤变码牜偶位扌
        偶步退冫孤变码牜偶位扌
        偶步进冫孤变码牜偶位扌
    慢步退冫孤变码扌
    慢步进冫孤变码扌
        孤变码讠孤变码牜偶位扌
        孤变码巛孤变码牜偶位扌

趃步退冫爻位栈冃孤变码扌
趃步进冫爻位栈冃孤变码扌
    步退冫爻位栈冃孤变码扌
    步进冫爻位栈冃孤变码扌





奇偶性纟
最低阳爻纟
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.check import check_type_is, check_int_ge
    from seed.math.floor_ceil_tools.fc_log import floor_log2
    from seed.math.floor_ceil_tools.fc_log import ceil_zpow_, floor_zpow_
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

r'''[[[

[[
#code6FXT:here
===
copy from:
view ../../fxt/_ignore__unzip/fxt/src/bits/graycode.h
===

#if !defined HAVE_GRAYCODE_H__
#define      HAVE_GRAYCODE_H__
// This file is part of the FXT library.
// Copyright (C) 2010, 2012 Joerg Arndt
// License: GNU General Public License version 3 or later,
// see the file COPYING.txt in the main directory.

#include "fxttypes.h"
#include "bits/bitsperlong.h"


static inline ulong gray_code(ulong x)
// Return the Gray code of x
// ('bit-wise derivative modulo 2')
{
    return  x ^ (x>>1);
}
// -------------------------


static inline ulong inverse_gray_code(ulong x)
// inverse of gray_code()
// note: the returned value contains at each bit position
// the parity of all bits of the input left from it (incl. itself)
//
{
// ----- VERSION 1 (integration modulo 2):
//    ulong h=1, r=0;
//    do
//    {
//        if ( x & 1 )  r^=h;
//        x >>= 1;
//        h = (h<<1)+1;
//    }
//    while ( x!=0 );
//    return r;

// ----- VERSION 2 (apply graycode BITS_PER_LONG-1 times):
//    ulong r = BITS_PER_LONG;
//    while ( --r )  x ^= x>>1;
//    return x;

// ----- VERSION 3 (use: gray ** BITSPERLONG == id):
    x ^= x>>1;  // gray ** 1
    x ^= x>>2;  // gray ** 2
    x ^= x>>4;  // gray ** 4
    x ^= x>>8;  // gray ** 8
    x ^= x>>16;  // gray ** 16
    // here: x = gray**31(input)
    // note: the statements can be reordered at will

#if  BITS_PER_LONG > 32
    x ^= x>>32;  // for 64bit words
#endif

    return  x;
}
// -------------------------


static inline ulong byte_gray_code(ulong x)
// Return the Gray code of bytes in parallel
{
#if  BITS_PER_LONG == 32
    return  x ^ ((x & 0xfefefefeUL)>>1);
#endif

#if  BITS_PER_LONG == 64
    return  x ^ ((x & 0xfefefefefefefefeUL)>>1);
#endif
}
// -------------------------

static inline ulong byte_inverse_gray_code(ulong x)
// Return the inverse Gray code of bytes in parallel
{
#if  BITS_PER_LONG == 32
    x ^= ((x & 0xfefefefeUL)>>1);
    x ^= ((x & 0xfcfcfcfcUL)>>2);
    x ^= ((x & 0xf0f0f0f0UL)>>4);
#endif

#if  BITS_PER_LONG == 64
    x ^= ((x & 0xfefefefefefefefeUL)>>1);
    x ^= ((x & 0xfcfcfcfcfcfcfcfcUL)>>2);
    x ^= ((x & 0xf0f0f0f0f0f0f0f0UL)>>4);
#endif

    return  x;
}
// -------------------------


#endif  // !defined HAVE_GRAYCODE_H__
===
]]
[[
===
copy from:
view ../../fxt/_ignore__unzip/fxt/src/bits/graypower.h
===
#if !defined  HAVE_GRAYPOWER_H__
#define       HAVE_GRAYPOWER_H__
// This file is part of the FXT library.
// Copyright (C) 2010 Joerg Arndt
// License: GNU General Public License version 3 or later,
// see the file COPYING.txt in the main directory.


#include "fxttypes.h"
#include "bits/bitsperlong.h"


static inline ulong gray_pow(ulong x, ulong e)
// Return (gray_code**e)(x)
// gray_pow(x, 1) == gray_code(x)
// gray_pow(x, BITS_PER_LONG-1) == inverse_gray_code(x)
{
    e &= (BITS_PER_LONG-1);  // modulo BITS_PER_LONG
    ulong s = 1;
    while ( e )
    {
        if ( e & 1 )  x ^= x >> s;  // gray ** s
        s <<= 1;
        e >>= 1;
    }
    return  x;
}
// -------------------------

static inline ulong inverse_gray_pow(ulong x, ulong e)
// Return (inverse_gray_code**(e))(x)
//   == (gray_code**(-e))(x)
// inverse_gray_pow(x, 1) == inverse_gray_code(x)
// inverse_gray_pow(x, BITS_PER_LONG-1) == gray_code(x)
{
    return  gray_pow(x, -e);
}
// -------------------------



static inline ulong rev_gray_pow(ulong x, ulong e)
// Return (rev_gray_code**e)(x)
// rev_gray_pow(x, 1) == rev_gray_code(x)
// rev_gray_pow(x, BITS_PER_LONG-1) == inverse_rev_gray_code(x)
{
    e &= (BITS_PER_LONG-1);  // modulo BITS_PER_LONG
    ulong s = 1;
    while ( e )
    {
        if ( e & 1 )  x ^= x << s;  // rev_gray ** s
        s <<= 1;
        e >>= 1;
    }
    return  x;
}
// -------------------------


static inline ulong inverse_rev_gray_pow(ulong x, ulong e)
// Return (inverse_rev_gray_code**(e))(x)
//   == (rev_gray_code**(-e))(x)
// inverse_rev_gray_pow(x, 1) == inverse_rev_gray_code(x)
// inverse_rev_gray_pow(x, BITS_PER_LONG-1) == rev_gray_code(x)
{
    return  rev_gray_pow(x, -e);
}
// -------------------------


#endif  // !defined HAVE_GRAYPOWER_H__
===
]]
[[
===
copy from:
view ../../fxt/_ignore__unzip/fxt/src/bits/nextgray.h
===
#if !defined  HAVE_NEXTGRAY_H__
#define       HAVE_NEXTGRAY_H__
// This file is part of the FXT library.
// Copyright (C) 2010, 2012 Joerg Arndt
// License: GNU General Public License version 3 or later,
// see the file COPYING.txt in the main directory.

#include "bits/bitlow.h"  // lowest_one()
#include "fxttypes.h"


static inline ulong next_gray2(ulong x)
// With input x==gray_code(2*k) the return is gray_code(2*k+2).
// Let x1 be the word x shifted right once
// and i1 its inverse Gray code.
// Let r1 be the return r shifted right once.
// Then r1 = gray_code(i1+1).
// That is, we have a Gray code counter.
// The argument must have an even number of bits.
//
//   k:     g(k)      g(2*k)     g(k) p
//   0:   .......    .......   ...... .   ...... .
//   1:   ......1    .....11   .....1 1   .....+ 1
//   2:   .....11    ....11.   ....11 .   ....+1 .
//   3:   .....1.    ....1.1   ....1. 1   ....1- 1
//   4:   ....11.    ...11..   ...11. .   ...+1. .
//   5:   ....111    ...1111   ...111 1   ...11+ 1
//   6:   ....1.1    ...1.1.   ...1.1 .   ...1-1 .
//   7:   ....1..    ...1..1   ...1.. 1   ...1.- 1
//   8:   ...11..    ..11...   ..11.. .   ..+1.. .
//   9:   ...11.1    ..11.11   ..11.1 1   ..11.+ 1
//  10:   ...1111    ..1111.   ..1111 .   ..11+1 .
//  11:   ...111.    ..111.1   ..111. 1   ..111- 1
//  12:   ...1.1.    ..1.1..   ..1.1. .   ..1-1. .
//  13:   ...1.11    ..1.111   ..1.11 1   ..1.1+ 1
//  14:   ...1..1    ..1..1.   ..1..1 .   ..1.-1 .
//  15:   ...1...    ..1...1   ..1... 1   ..1..- 1
//  16:   ..11...    .11....   .11... .   .+1... .
//  17:   ..11..1    .11..11   .11..1 1   .11..+ 1
//
// Note that the changes with increment always
// happen one position left of the rightmost bit.
//
// Convert an arbitrary (Gray code) word g to
//   x = (g<<1) ^ parity(g)
// in order to use this routine.
{
    x ^= 1;
    x ^= (lowest_one(x) << 1);
    return x;
}
// -------------------------


#endif  // !defined HAVE_NEXTGRAY_H__
===
]]
[[
===
view ../../fxt/_ignore__unzip/fxt/src/bits/bitlow.h
===
static inline ulong lowest_one(ulong x)
// Return word where only the lowest set bit in x is set.
// Return 0 if no bit is set.
{
//    if ( 0==x )  return 0;
//    return  ((x^(x-1)) >> 1) + 1;

//    return  (x & (x-1)) ^ x;

    return  x & -x;  // use: -x == ~x + 1
}
// -------------------------


===
]]



#]]]'''#'''



__all__
def 位次讠孤变码牜趃用扌(趃用次数,位次, /):
    check_type_is(int, 趃用次数)
    check_int_ge(0, 位次)
    周期 = 位次讠周期纟孤变码扌(位次)
    趃用次数 &= (周期-1)
        #<==> 趃用次数 %= 周期

    二幂 = 1
    while 趃用次数:
        if 趃用次数&1:
            位次 ^= (位次>>二幂)
        趃用次数 >>= 1
        二幂 <<= 1
    孤变码 = 位次
    return 孤变码
def 位次讠孤变码扌(位次, /):
    #def 位次讠格雷码扌(位次, /):
    check_int_ge(0, 位次)
    孤变码 = 位次 ^ (位次>>1)
    return 孤变码

def 位次巛孤变码扌(孤变码, /):
    check_int_ge(0, 孤变码)
    冃位次 = 孤变码
    冃孤变码 = 位次讠孤变码牜趃用扌(趃用次数:=-1,冃位次)
    位次 = 冃孤变码
    assert 孤变码 == 位次讠孤变码扌(位次), (孤变码, 位次)
    return 位次

def 位次讠周期纟孤变码扌(位次, /):
    check_int_ge(0, 位次)
    #return ceil_zpow_(1+floor_log2(位次)) #floor_log2:AssertionError:assert pint > 0
    #return ceil_zpow_(位次.bit_length()) #ceil_zpow_.ceil_log2:AssertionError:assert pint > 0
    if 0 == 位次:
        return 1
    # [[位次 =!= 0] -> [周期纟格雷算子乊{位次} == (ceil_zpow_(1+floor_log2(位次)))]]
    return ceil_zpow_(1+floor_log2(位次))
def 趃孤变码巛趃位次扌(趃位次, /):
    return map(位次讠孤变码扌, 趃位次)

def 趃用孤变至循环扌(位次, /):
    check_int_ge(0, 位次)
    起点 = 位次
    while 1:
        yield 位次
        孤变码 = 位次讠孤变码扌(位次)
        位次 = 孤变码#类型变更#type cast
        if 位次 == 起点:
            break
    return
#with_period
def 制表冫孤变循环扌(位次, /, *, 欤带周期=False):
    ls = tuple(趃用孤变至循环扌(位次))
    sz = len(ls)
    assert sz == 位次讠周期纟孤变码扌(位次)
    return ls if not 欤带周期 else (sz, ls)
def 趃制表冫孤变循环扌(趃位次, /, **kwds):
    return map(制表冫孤变循环扌, 趃位次) if not kwds else (制表冫孤变循环扌(位次, **kwds) for 位次 in 趃位次)



def 趃步退冫孤变码牜偶位扌(孤变码牜偶位=0, /):
    check_int_ge(0, 孤变码牜偶位)
    yield 孤变码牜偶位
    while 孤变码牜偶位:
        孤变码牜偶位 = 偶步退冫孤变码牜偶位扌(孤变码牜偶位)
        yield 孤变码牜偶位
    return
def 趃步进冫孤变码牜偶位扌(孤变码牜偶位=0, /):
    check_int_ge(0, 孤变码牜偶位)
    while 1:
        yield 孤变码牜偶位
        孤变码牜偶位 = 偶步进冫孤变码牜偶位扌(孤变码牜偶位)
    return
def 趃步退冫孤变码扌(孤变码=0, /):
    check_int_ge(0, 孤变码)
    # 步进:外部状态:Gray_code[k]
    孤变码牜偶位 = 孤变码讠孤变码牜偶位扌(孤变码)
    # 步进:内部状态:Gray_code[2*k]
    return map(孤变码巛孤变码牜偶位扌, 趃步退冫孤变码牜偶位扌(孤变码牜偶位))

def 趃步进冫孤变码扌(孤变码=0, /):
    check_int_ge(0, 孤变码)
    # 步进:外部状态:Gray_code[k]
    孤变码牜偶位 = 孤变码讠孤变码牜偶位扌(孤变码)
    # 步进:内部状态:Gray_code[2*k]
    return map(孤变码巛孤变码牜偶位扌, 趃步进冫孤变码牜偶位扌(孤变码牜偶位))
def 偶步进冫孤变码牜偶位扌(孤变码牜偶位, /):
    '孤变码{位次%2==0} -> 孤变码{位次+2}'
    # [Gray_code[2*(1+k)] == (Gray_code[2*k]^1) ^ (lowest_1bit_of(Gray_code[2*k]^1) << 1)]
    #   偶步进:内部状态->内部状态
    check_int_ge(0, 孤变码牜偶位)
    # [孤变码牜偶位 >= 0]
    u = 孤变码牜偶位^1
    孤变码牜偶位 = u ^ (最低阳爻纟(u) << 1)
    # [孤变码牜偶位 >= 3]
    return 孤变码牜偶位
def 偶步退冫孤变码牜偶位扌(孤变码牜偶位, /):
    '孤变码{位次%2==0} -> 孤变码{位次-2}'
    # [Gray_code[2*(-1+k)] == (Gray_code[2*k]^1) ^ (lowest_1bit_of(Gray_code[2*k]) << 1)]
    # 偶步退:内部状态->内部状态
    check_int_ge(3, 孤变码牜偶位)
    # [孤变码牜偶位 >= 3]
    孤变码牜偶位 = 孤变码牜偶位 ^ 1 ^ (最低阳爻纟(孤变码牜偶位) << 1)
    # [孤变码牜偶位 >= 0]
    return 孤变码牜偶位
def 慢步退冫孤变码扌(孤变码, /):
    '孤变码{位次>0} -> 孤变码{位次-1}'
    check_int_ge(1, 孤变码)
    # 步进:外部状态:Gray_code[k]
    孤变码牜偶位 = 孤变码讠孤变码牜偶位扌(孤变码)
    # 步进:内部状态:Gray_code[2*k]
    孤变码牜偶位 = 偶步退冫孤变码牜偶位扌(孤变码牜偶位)
    孤变码 = 孤变码巛孤变码牜偶位扌(孤变码牜偶位)
    return 孤变码

def 慢步进冫孤变码扌(孤变码, /):
    '孤变码{位次} -> 孤变码{位次+1}'
    # 步进:外部状态:Gray_code[k]
    孤变码牜偶位 = 孤变码讠孤变码牜偶位扌(孤变码)
    # 步进:内部状态:Gray_code[2*k]
    孤变码牜偶位 = 偶步进冫孤变码牜偶位扌(孤变码牜偶位)
    孤变码 = 孤变码巛孤变码牜偶位扌(孤变码牜偶位)
    return 孤变码
def 孤变码讠孤变码牜偶位扌(孤变码, /):
    '孤变码{位次} -> 孤变码{位次*2}'
    check_int_ge(0, 孤变码)
    # [Gray_code[2*k] == Gray_code[k]*2 + parity_of(Gray_code[k])]
    #   步进:外部状态->内部状态
    孤变码牜偶位 = (孤变码<<1) ^ 奇偶性纟(孤变码)
    return 孤变码牜偶位
def 孤变码巛孤变码牜偶位扌(孤变码牜偶位, /):
    '孤变码{位次*2} -> 孤变码{位次}'
    check_int_ge(0, 孤变码牜偶位)
    # [Gray_code[k] == Gray_code[2*k] >> 1]
    #   步进:内部状态->外部状态
    孤变码 = (孤变码牜偶位>>1)
    return 孤变码




def 奇偶性纟(自然数, /):
    #def parity_of():
    check_int_ge(0, 自然数)
    return 自然数.bit_count()&1

def 最低阳爻纟(正整数, /):
    #def lowest_1bit_of():
    #lowest_one()
    check_int_ge(1, 正整数)
    return  正整数 & -正整数



def 步退冫爻位栈冃孤变码扌(爻位栈冃孤变码, /, *, 欤反向=False):
    '爻位栈冃孤变码/[阳爻位次]{降序} -> 爻位牜更改'
    return 步进冫爻位栈冃孤变码扌(爻位栈冃孤变码, 欤反向=not 欤反向)
def 步进冫爻位栈冃孤变码扌(爻位栈冃孤变码, /, *, 欤反向=False):
    '爻位栈冃孤变码/[阳爻位次]{降序} -> 爻位牜更改'
    sz = len(爻位栈冃孤变码)
    欤反向 = bool(欤反向)
    if 欤反向 and not sz: raise ValueError
    # [欤反向 -> [sz > 0]]
    奇偶性 = sz&1
    # [parity_of(孤变码) == 奇偶性]

    # [Gray_code[1+k] == if 0==parity_of(Gray_code[k]) then Gray_code[k]^1 else Gray_code[k]^(lowest_1bit_of(Gray_code[k])<<1)]
        #慢步进:步进定义
    # [Gray_code[-1+k] == if 1==parity_of(Gray_code[k]) then Gray_code[k]^1 else Gray_code[k]^(lowest_1bit_of(Gray_code[k])<<1)]
        #慢步退:步退定义
    欤更改最低爻位 = 奇偶性 == 欤反向
    if 欤更改最低爻位:
        # [偶&&步进]or[奇&&步退]
        爻位牜更改 = 0
    else:
        # [偶&&步退]or[奇&&步进]
        # !! [欤反向 -> [sz > 0]]
        # [sz > 0]
        最低阳爻位次 = 爻位栈冃孤变码.pop()
        777; sz -= 1 #bug:miss this
        爻位牜更改 = 1+最低阳爻位次
    #########
    if (sz > 0 and 爻位栈冃孤变码[-1] == 爻位牜更改):
        爻位栈冃孤变码.pop()
    else:
        爻位栈冃孤变码.append(爻位牜更改)
    #########
    if not 欤更改最低爻位:
        爻位栈冃孤变码.append(最低阳爻位次)
    #########
    return 爻位牜更改
def 趃步退冫爻位栈冃孤变码扌(爻位栈冃孤变码, /, *, 欤反向=False):
    '爻位栈冃孤变码/[阳爻位次]{降序} -> Iter 爻位牜更改'
    return 趃步进冫爻位栈冃孤变码扌(爻位栈冃孤变码, 欤反向=not 欤反向)
def 趃步进冫爻位栈冃孤变码扌(爻位栈冃孤变码, /, *, 欤反向=False):
    '爻位栈冃孤变码/[阳爻位次]{降序} -> Iter 爻位牜更改'
    欤反向 = bool(欤反向)
    while not (欤反向 and len(爻位栈冃孤变码) == 0):
        yield 步进冫爻位栈冃孤变码扌(爻位栈冃孤变码, 欤反向=欤反向)

__all__

from seed.math.Gray_code import 位次讠孤变码扌, 位次巛孤变码扌, 位次讠孤变码牜趃用扌, 位次讠周期纟孤变码扌, 趃孤变码巛趃位次扌

from seed.math.Gray_code import 趃制表冫孤变循环扌, 制表冫孤变循环扌, 趃用孤变至循环扌

from seed.math.Gray_code import \
(趃步退冫孤变码扌
,趃步进冫孤变码扌
,   趃步退冫孤变码牜偶位扌
,   趃步进冫孤变码牜偶位扌
,       偶步退冫孤变码牜偶位扌
,       偶步进冫孤变码牜偶位扌
,   慢步退冫孤变码扌
,   慢步进冫孤变码扌
,       孤变码讠孤变码牜偶位扌
,       孤变码巛孤变码牜偶位扌
)

from seed.math.Gray_code import 步退冫爻位栈冃孤变码扌, 步进冫爻位栈冃孤变码扌, 趃步退冫爻位栈冃孤变码扌, 趃步进冫爻位栈冃孤变码扌


#from seed.math.Gray_code import 奇偶性纟, 最低阳爻纟

from seed.math.Gray_code import *
