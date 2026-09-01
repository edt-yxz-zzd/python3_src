#__all__:goto
#Kronecker_symbol内禀:不可修正病蛊:goto
r'''[[[
e ../../python3_src/seed/math/Kronecker_symbol.py

seed.math.Kronecker_symbol
py -m nn_ns.app.debug_cmd   seed.math.Kronecker_symbol -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.Kronecker_symbol:__doc__ -ht # -ff -df
#######

[[
come_from:
view ../../python3_src/seed/math/BinaryQuadraticForm.py

vs:
view ../../python3_src/seed/math/Jacobi_symbol.py
]]
[[
view ../../python3_src/seed/math/Jacobi_symbol.py
    [[m,D::int][m%2==1][gcd(D,m)==1][D%4 < 2] -> [Jacobi_symbol(m;D) == Jacobi_symbol(m%(2**(D%2)*D);D)]]
    [[m,D::int][m%2==1][gcd(D,m)==1][D%4 < 2] -> [Jacobi_symbol(m;D) == Jacobi_symbol(m%(2*D);D)]]
    TODO:bug:[[m,D::int][m%2==1][gcd(D,m)==1][D%4 < 2] -> [Jacobi_symbol(m;D) == Jacobi_symbol(m%D;D)]]
        # 只需:[D%4 < 2][gcd(D,m)==1]
        # 无需:[D < 0]
        # Kronecker_symbol周期性前提:[D%4 < 2]
]]
[[
[D%4 < 2][D=!=0]:
    !! [is_Dirichlet_character_mod_(D;(\i->Kronecker_symbol(i;D)))]
    [Kronecker_symbol :: int -> int{=!=0} -> complex]
    [Kronecker_symbol(2;D) := (D&1)*(-1)**(D&4)] # ([D%2==0]*0 + [D%8==1]*1 + [D%8==5]*-1)
        # required:[D%4 < 2]
    [Kronecker_symbol(p{odd_prime};D) := Legendre_symbol(p;D)]
    [Kronecker_symbol(a*b;D) := Kronecker_symbol(a;D)*Kronecker_symbol(b;D)]
        ==>>:
        !! [X(1) == 1]
        [Kronecker_symbol(1;D) == 1]

        !! [X(0) == [abs(D) == 1]]
        [Kronecker_symbol(0;D) == [abs(D) == 1]]

        !! [X(-1) <- {-1,+1}]
        ???xxx:[Kronecker_symbol(-1;D) == -1]
        !! [X(-1) == X(D-1)]
        [Kronecker_symbol(-1;D) == D-1]

]]
[[
bug{周期性是有前提的}
xxx:new:
xxx:[i,M::int][M=!=0]:
xxx:    !! [M =!= 0]
xxx:    [u := i%abs(M)]
xxx:    [u >= 0]
xxx:    !! [X(i) == X(i+M)]
xxx:    [Kronecker_symbol(i;M) == Kronecker_symbol(u;M)]
xxx:    [M%2 == 1]:
xxx:        [odd := (u if u%2==1 else u+abs(M))]
xxx:        [odd%abs(M) == u]
xxx:        [odd%2 == 1]
xxx:        [odd >= u >= 0]
xxx:        !! [odd%2 == 1]
xxx:        [odd >= 1]
xxx:
xxx:    * [u%2 == 0][M%2 == 0]:
xxx:        [Kronecker_symbol(u;M) == 0]
xxx:    * [u%2 == 0][M%2 == 1]:
xxx:        [odd == u+M]
xxx:        [odd%2 == 1]
xxx:        [odd >= 1]
xxx:        !! [X(i) == X(i+M)]
xxx:        [Kronecker_symbol(u;M) == Kronecker_symbol(odd;M) == Jacobi_symbol(odd;M)]
xxx:    * [u%2 == 1]:
xxx:        [odd == u]
xxx:        [odd%2 == 1]
xxx:        [odd >= 1]
xxx:        [Kronecker_symbol(u;M) == Kronecker_symbol(odd;M) == Jacobi_symbol(odd;M)]
xxx:    ==>>:
xxx:    [Kronecker_symbol(u;M) == (1-[u%2 == 0 == M%2])*Jacobi_symbol(odd;M)]
xxx:    [Kronecker_symbol(u;M) == (1-[u%2 == 0 == M%2])*Jacobi_symbol((u if u%2==1 else u+abs(M));M)]
xxx:    [Kronecker_symbol(i;M) == let [u := i%abs(M)] in (1-[u%2 == 0 == M%2])*Jacobi_symbol((u if u%2==1 else u+abs(M));M)]
xxx:
xxx:[[i,M::int][M=!=0] -> [Kronecker_symbol(i;M) == let [u := i%abs(M)] in (1-[u%2 == 0 == M%2])*Jacobi_symbol((u if u%2==1 else u+abs(M));M)]]
xxx:
]]
[[
pari-gp-users.pdf
page214[214/693]
3.8.68 kronecker(x,y).
or:
??kronecker
kronecker(x,y):
    Kronecker  symbol (x|y),  where x and y must be of type integer.
    By definition, this is the extension of Legendre symbol to Z x Z by total multiplicativity in both arguments with the following special rules for y = 0, -1 or 2:
    * (x|0) = 1 if |x| = 1 and 0 otherwise.
    * (x|-1) = 1 if x >= 0 and -1 otherwise.
    * (x|2)  = 0 if x is even and 1 if x = 1,-1 mod 8 and -1 if x = 3,-3 mod 8.

[i,j,M,N::int]:
    [Kronecker_symbol(i;M) == (M:::/i) == gp.kronecker(M,i)]
        # flip

    ###定义:begin:
    [Kronecker_symbol(0;M) == [abs(M) == 1]]
        # !! [[1=!=gcd(i,M)] <-> [Kronecker_symbol(i;M) == 0]]
    bug:[Kronecker_symbol(-1;M) == (-1)**[M<0]]
        #0,-1况态=>但这样一来，就不可能是 周期性的 => ??? 周期性前提:[x<0][x%4 < 2] ???
    改为:mine:[Kronecker_symbol(-1;M) == +1]
    [Kronecker_symbol(2;M) == [M%2==0]*0 + [M%8 <- {1,7}]*+1 + [M%8 <- {3,5}]*-1]
    [[p::prime][p%2==1] -> [Kronecker_symbol(p;M) == Legendre_symbol(p;M)]]
    [Kronecker_symbol(i*j;M) == Kronecker_symbol(i;M) * Kronecker_symbol(j;M)]
        ==>>:
        [1 == Kronecker_symbol(0;-1) == Kronecker_symbol(0*-1;-1) == Kronecker_symbol(0;-1)*Kronecker_symbol(-1;-1) == 1*-1 == -1]
            !!!!!!bug!!!!!!
        _L
    ###定义:end
    ==>>:
    [Kronecker_symbol(i;M*N) == Kronecker_symbol(i;M) * Kronecker_symbol(i;N)]
    [[odd::int][odd%2==1][odd>0] -> [Kronecker_symbol(odd;M) == Jacobi_symbol(odd;M)]]
    [[1==gcd(i,M)] <-> [Kronecker_symbol(i;M) =!= 0]]
    [[1=!=gcd(i,M)] <-> [Kronecker_symbol(i;M) == 0]]
        ==>>:
        [Kronecker_symbol(-1;M) =!= 0]

    [1 == Kronecker_symbol(0;-1) == Kronecker_symbol(0*j;-1) == Kronecker_symbol(0;-1)*Kronecker_symbol(j;-1) == 1*Kronecker_symbol(j;-1)]
    [Kronecker_symbol(j;-1) == +1]
        ??? [j%2==1] => [Jacobi_symbol(j;-1) == +1]
        _L
        #不可修正病蛊:here
        @20260815:改为:^NotImplementedError
    [Kronecker_symbol(-1;-1) == +1]
        !! [Kronecker_symbol(-1;-1) == -1]
        _L
        #可修正病蛊
    [Kronecker_symbol(-1;M) == Kronecker_symbol(-1;-1*-M) == Kronecker_symbol(-1;-1)*Kronecker_symbol(-1;-M) == 1*Kronecker_symbol(-1;-M)]
    [Kronecker_symbol(-1;M) == Kronecker_symbol(-1;-M)]
    [Kronecker_symbol(-1;M) == +1]

    [Kronecker_symbol(+1;M) == Kronecker_symbol(-1;M)**2 == +1]
    [Kronecker_symbol(+1;M) == +1]

    !! [1==gcd(i,-1)]
    [Kronecker_symbol(i;-1) =!= 0]
    [Kronecker_symbol(i;-1) <- {-1,+1}]
    [Kronecker_symbol(i;-1)**2 == 1]
    [Kronecker_symbol(i;+1) == Kronecker_symbol(i;-1)**2 == +1]
    [Kronecker_symbol(i;+1) == +1]
    !! [Kronecker_symbol(+1;M) == +1]
    [Kronecker_symbol(+1;M) == +1 == Kronecker_symbol(M;+1)]
    [Kronecker_symbol(+1;M) == Kronecker_symbol(M;+1)]

    * [M%2 == 1]:
        [Kronecker_symbol(2;M) == (-1)**((M**2-1)///8) == Jacobi_symbol(M;2) == Kronecker_symbol(M;2)]
        [Kronecker_symbol(2;M) == Kronecker_symbol(M;2)]
    * [M%2 == 0]:
        [gcd(2,M)%2 == 0]
        [gcd(2,M) =!= 1]
        [Kronecker_symbol(2;M) == 0 == Kronecker_symbol(M;2)]
    ==>>:
    [Kronecker_symbol(2;M) == Kronecker_symbol(M;2)]


    * [abs(M) == 0]:
        [M == 0]
        [Kronecker_symbol(0;M) == Kronecker_symbol(M;0)]
    * [abs(M) == 1]:
        [M <- {-1,+1}]
        [gcd(0,M) == 1]
        [Kronecker_symbol(0;M) == +1]
        !! [Kronecker_symbol(-1;0) == +1]
        !! [Kronecker_symbol(+1;0) == +1]
        [Kronecker_symbol(M;0) == +1]
        [Kronecker_symbol(0;M) == Kronecker_symbol(M;0)]
    * [abs(M) > 1]:
        [gcd(0,M) == abs(M) > 1]
        [Kronecker_symbol(0;M) == 0 == Kronecker_symbol(M;0)]
        [Kronecker_symbol(0;M) == Kronecker_symbol(M;0)]
    ==>>:
    [Kronecker_symbol(0;M) == Kronecker_symbol(M;0)]


    [Kronecker_symbol(+1;M) == Kronecker_symbol(M;+1)]
    [Kronecker_symbol(2;M) == Kronecker_symbol(M;2)]
    [Kronecker_symbol(0;M) == Kronecker_symbol(M;0)]
    ??? [Kronecker_symbol(-1;M) =?= Kronecker_symbol(M;-1)]
]]
[[
[M%2==1]:
    [Kronecker_symbol(-1;M)
    == Kronecker_symbol(M;-1) * (-1)**((M-1)*(-1-1)/4 + (sign(M)-1)*(sign(-1)-1)/4)
    == Kronecker_symbol(M;-1) * (-1)**((M-1)/2 + (sign(M)-1)/2)
    * [M < 0]:
        ... == Kronecker_symbol(M;-1) * (-1)**((M-1)/2 + (-1-1)/2)
            == Kronecker_symbol(M;-1) * (-1)**((M-1)/2 -1)
            == Kronecker_symbol(M;-1) * (-1)**[M%4==1]
            == Kronecker_symbol(M;-1) * (-1)**[(-M)%4==3]
            == Kronecker_symbol(M;-1) * (-1)**[abs(M)%4==3]
            == Kronecker_symbol(-1;-1) * Kronecker_symbol(abs(M);-1) * (-1)**[abs(M)%4==3]
            == Kronecker_symbol(-1;-1)
    * [M > 0]:
        ... == Kronecker_symbol(M;-1) * (-1)**((M-1)/2 + (+1-1)/2)
            == Kronecker_symbol(M;-1) * (-1)**((M-1)/2)
            == Kronecker_symbol(M;-1) * (-1)**[M%4==3]
            == Kronecker_symbol(M;-1) * (-1)**[abs(M)%4==3]
            == Jacobi_symbol(M;-1) * (-1)**[abs(M)%4==3]
            == (-1)**[M%4==3] * (-1)**[abs(M)%4==3]
            == +1
    == [M<0]*Kronecker_symbol(-1;-1) + [M>0]*+1
    ]
    [Kronecker_symbol(-1;M) == [M<0]*Kronecker_symbol(-1;-1) + [M>0]*+1]
[M=!=0]:
    ?ez,odd :=> [ez::uint][odd::int][M==odd*2**ez][odd%2==1]
    [[M<0] <-> [odd<0]]
    [Kronecker_symbol(-1;M) == Kronecker_symbol(-1;2)**ez * ([M<0]*Kronecker_symbol(-1;-1) + [M>0]*+1)]

<<==:
========================
!! 不可修正病蛊:goto
view ../../fxt/_ignore__unzip/fxt/src/mod/kronecker.cc
fxtbook似乎只考虑uint
========================
// This file is part of the FXT library.
// Copyright (C) 2010, 2012 Joerg Arndt
// License: GNU General Public License version 3 or later,
// see the file COPYING.txt in the main directory.

#include "mod/mtypes.h"
//#include "mod/factor.h"


int
kronecker(umod_t a, umod_t b)
// Return Kronecker symbol (a/b).
// Equal to Legendre symbol (a/b) if b is an odd prime.
//.
// Cf. Cohen p.29
{
//    if ( a>=b )  a %= b;
    static const int  tab2[] = {0, 1, 0, -1, 0, -1, 0, 1};
    // tab2[ a & 7 ] := (-1)^((a^2-1)/8)

    if ( 0==b )  return (1==a);

    if ( 0==((a|b)&1) )  return 0;  // a and b both even ?

    int v = 0;
    while ( 0==(b&1) )  { ++v;  b>>=1; }

    int k;
    if ( 0==(v&1) )  k = 1;
    else             k = tab2[ a & 7 ];

    // signed:   if ( b<0 )  { b=-b;  if (a<0) {k=-k}; }

    // step3:
    while ( 1 )
    {
        // here b is odd
        if ( 0==a )  return ( b>1 ? 0 : k );

        v = 0;
        while ( 0==(a&1) )  { ++v;  a>>=1; }

        if ( 1==(v&1) )  k *= tab2[ b & 7 ];  // k *= (-1)**((b*b-1)/8)

        // step4:
        if ( a & b & 2 )  k = -k;  // k = k*(-1)**((a-1)*(b-1)/4)

        umod_t r = a;  // signed:  r = abs(a)
        a = b % r;
        b = r;
        // goto step3;
    }
}
// -------------------------



//int
//reciprocity(umod_t a, umod_t b)
////
//// (a/b) = (b/a) * (-1)^((a1-1)*(b1-1)/4 + (as-1)*(bs-1)/4)
//// where a==a1*2^ae, b=b1*2^be
//// and as=sign(a), bs=sign(b)
//// cf. Cohen p.43
////
//// UNTESTED
//{
//    if ( (0==a) || (0==b) )  return 0;
//    while ( 0==(a&1) )  a >>= 1;
//    while ( 0==(b&1) )  b >>= 1;
//    int k = 1;
//    if ( a & b & 2 )  k = -k;
//    return k;
//}
//// -------------------------
========================
]]
[[[[[[
view others/数学/class_number/Kronecker_symbol/Kronecker_symbol.txt
[[[
===
https://mathworld.wolfram.com/KroneckerSymbol.html
  (0/-1)未定义
  The Kronecker symbol is an extension of the Jacobi symbol (n/m) to all integers.
===
https://handwiki.org/wiki/Kronecker_symbol
  (a/n):
    严格版:[n>0][a%4<2]
      只多定义:({0,4,1,5}%8/2)
    [[
#并非无条件地支持双分量乘性:here
Properties
The Kronecker symbol shares many basic properties of the Jacobi symbol, under certain restrictions:

(a/n)=±1 if gcd⁡(a,n)=1, otherwise(a/n)=0.
(a*b/n)=(a/n)*(b/n) unless n=−1, one of a,b is zero and the other one is negative.
(a/m*n)=(a/m)*(a/n) unless a=−1, one of m,n is zero and the other one has odd part (definition below) congruent to 3mod4.
For n>0, we have (a/n)=(b/n) whenever a≡bmod{4n,n≡2(mod4),n otherwise}. If additionally a,b have the same sign, the same also holds for n<0.
For a≢3(mod4), a≠0, we have (a/m)=(a/n) whenever m≡nmod{4|a|,a≡2(mod4),|a|otherwise}.
On the other hand, the Kronecker symbol does not have the same connection to quadratic residues as the Jacobi symbol. In particular, the Kronecker symbol (a/n) for n≡2(mod4) can take values independently on whether a is a quadratic residue or nonresidue modulo n.

Quadratic reciprocity
The Kronecker symbol also satisfies the following versions of quadratic reciprocity law.

For any nonzero integer n, let n′ denote its odd part: n=2^e*n′ where n′ is odd (for n=0, we put 0′=1). Then the following symmetric version of quadratic reciprocity holds for every pair of integers m,n such that gcd⁡(m,n)=1:

(m/n)*(n/m)=±(−1)^((m′−1)/2*(n′−1)/2),
where the ± sign is equal to + if m≥0 or n≥0 and is equal to − if m<0 and n<0.

There is also equivalent non-symmetric version of quadratic reciprocity that holds for every pair of relatively prime integers m,n:

(m/n)(n/|m|)=(−1)^((m′−1)/2*(n′−1)/2).
For any integer n let n*=(−1)^((n′−1)/2)*n. Then we have another equivalent non-symmetric version that states

(m*/n)=(n/|m|)
for every pair of integers m,n (not necessarily relatively prime).

The supplementary laws generalize to the Kronecker symbol as well. These laws follow easily from each version of quadratic reciprocity law stated above (unlike with Legendre and Jacobi symbol where both the main law and the supplementary laws are needed to fully describe the quadratic reciprocity).

For any integer n we have

(−1/n)=(−1)^((n′−1)/2)
and for any odd integer n it's

(2/n)=(−1)^((n^2−1)/8).
    ]]
===
]]]
]]]]]]






'#'; __doc__ = r'#'
>>> Kronecker_symbol(-1, -1) # NOTE: [gp.kronecker(-1,-1) == -1]
1
>>> Kronecker_symbol(-1, 0)
1
>>> Kronecker_symbol(-1, +1)
1
>>> Kronecker_symbol(-1, -2)
1


>>> Kronecker_symbol(1, 0)
1

old:
Traceback (most recent call last):
    ...
ValueError: (1, 0)

>>> Kronecker_symbol(1, 2)
1

old:
Traceback (most recent call last):
    ...
ValueError: (1, 2)

>>> Kronecker_symbol(0, +1)
1
>>> Kronecker_symbol(0, -1)
1
>>> Kronecker_symbol(0, 0)
0
>>> Kronecker_symbol(0, -3)
0
>>> Kronecker_symbol(0, -3)
0

>>> Kronecker_symbol(-1, 1)
1
>>> Kronecker_symbol(0, 1)
1
>>> Kronecker_symbol(1, 1)
1
>>> Kronecker_symbol(2, 1)
1

>>> Kronecker_symbol(0, -3)
0
>>> Kronecker_symbol(1, -3)
1
>>> Kronecker_symbol(2, -3)
-1

>>> for M in range(-10, 0)[::-1]:
...     if not M%4 < 2:continue #old:precondition
...     if M == 0:continue
...     for i in range(7):
...         print(i, M, Kronecker_symbol(i,M), sep=':')
0:-3:0
1:-3:1
2:-3:-1
3:-3:0
4:-3:1
5:-3:-1
6:-3:0
0:-4:0
1:-4:1
2:-4:0
3:-4:-1
4:-4:0
5:-4:1
6:-4:0
0:-7:0
1:-7:1
2:-7:1
3:-7:-1
4:-7:1
5:-7:-1
6:-7:-1
0:-8:0
1:-8:1
2:-8:0
3:-8:1
4:-8:0
5:-8:-1
6:-8:0






#new:without [M%4 < 2][M=!=0]
>>> for M in range(-10, 0)[::-1]:
...     for i in range(7):
...         print(i, M, Kronecker_symbol(i,M), sep=':')
0:-1:1
1:-1:1
2:-1:1
3:-1:-1
4:-1:1
5:-1:1
6:-1:-1
0:-2:0
1:-2:1
2:-2:0
3:-2:1
4:-2:0
5:-2:-1
6:-2:0
0:-3:0
1:-3:1
2:-3:-1
3:-3:0
4:-3:1
5:-3:-1
6:-3:0
0:-4:0
1:-4:1
2:-4:0
3:-4:-1
4:-4:0
5:-4:1
6:-4:0
0:-5:0
1:-5:1
2:-5:-1
3:-5:1
4:-5:1
5:-5:0
6:-5:-1
0:-6:0
1:-6:1
2:-6:0
3:-6:0
4:-6:0
5:-6:1
6:-6:0
0:-7:0
1:-7:1
2:-7:1
3:-7:-1
4:-7:1
5:-7:-1
6:-7:-1
0:-8:0
1:-8:1
2:-8:0
3:-8:1
4:-8:0
5:-8:-1
6:-8:0
0:-9:0
1:-9:1
2:-9:1
3:-9:0
4:-9:1
5:-9:1
6:-9:0
0:-10:0
1:-10:1
2:-10:0
3:-10:-1
4:-10:0
5:-10:0
6:-10:0










>>> for M in range(1, 1+10):
...     for i in range(7):
...         print(i, M, Kronecker_symbol(i,M), sep=':')
0:1:1
1:1:1
2:1:1
3:1:1
4:1:1
5:1:1
6:1:1
0:2:0
1:2:1
2:2:0
3:2:-1
4:2:0
5:2:-1
6:2:0
0:3:0
1:3:1
2:3:-1
3:3:0
4:3:1
5:3:-1
6:3:0
0:4:0
1:4:1
2:4:0
3:4:1
4:4:0
5:4:1
6:4:0
0:5:0
1:5:1
2:5:-1
3:5:-1
4:5:1
5:5:0
6:5:1
0:6:0
1:6:1
2:6:0
3:6:0
4:6:0
5:6:1
6:6:0
0:7:0
1:7:1
2:7:1
3:7:1
4:7:1
5:7:-1
6:7:1
0:8:0
1:8:1
2:8:0
3:8:-1
4:8:0
5:8:-1
6:8:0
0:9:0
1:9:1
2:9:1
3:9:0
4:9:1
5:9:1
6:9:0
0:10:0
1:10:1
2:10:0
3:10:1
4:10:0
5:10:0
6:10:0











>>> for M in range(-3, 4):
...     for i in range(-6, 7):
...         print(i, M, Kronecker_symbol(i,M), sep=':')
-6:-3:0
-5:-3:-1
-4:-3:1
-3:-3:0
-2:-3:-1
-1:-3:1
0:-3:0
1:-3:1
2:-3:-1
3:-3:0
4:-3:1
5:-3:-1
6:-3:0
-6:-2:0
-5:-2:-1
-4:-2:0
-3:-2:1
-2:-2:0
-1:-2:1
0:-2:0
1:-2:1
2:-2:0
3:-2:1
4:-2:0
5:-2:-1
6:-2:0
-6:-1:-1
-5:-1:1
-4:-1:1
-3:-1:-1
-2:-1:1
-1:-1:1
0:-1:1
1:-1:1
2:-1:1
3:-1:-1
4:-1:1
5:-1:1
6:-1:-1
-6:0:0
-5:0:0
-4:0:0
-3:0:0
-2:0:0
-1:0:1
0:0:0
1:0:1
2:0:0
3:0:0
4:0:0
5:0:0
6:0:0
-6:1:1
-5:1:1
-4:1:1
-3:1:1
-2:1:1
-1:1:1
0:1:1
1:1:1
2:1:1
3:1:1
4:1:1
5:1:1
6:1:1
-6:2:0
-5:2:-1
-4:2:0
-3:2:-1
-2:2:0
-1:2:1
0:2:0
1:2:1
2:2:0
3:2:-1
4:2:0
5:2:-1
6:2:0
-6:3:0
-5:3:-1
-4:3:1
-3:3:0
-2:3:-1
-1:3:1
0:3:0
1:3:1
2:3:-1
3:3:0
4:3:1
5:3:-1
6:3:0





































py_adhoc_call   seed.math.Kronecker_symbol   @f
]]]'''#'''
__all__ = r'''
Kronecker_symbol
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.math.Jacobi_symbol import Jacobi_symbol
    from seed.math.max_power_of_base_as_factor_of_ import factor_pint_out_power_of_base_
    from seed.tiny_.check import check_type_is, check_int_ge
#.#################################
___end_mark_of_excluded_global_names__0___ = ...


def Kronecker_symbol(i, M, /):
    'i/int -> M/int -> (-1|0|+1)/int  # NOTE:  pari-gp:[Kronecker_symbol(-1;M) == (-1)**[M<0]] vs mine:[Kronecker_symbol(-1;M) == +1]'
    #new1:'i/int -> M/int{=!=0} -> (-1|0|+1)/int  #  [[i,M::int][M=!=0] -> [Kronecker_symbol(i;M) == let [u := i%abs(M)] in (1-[u%2 == 0 == M%2])*Jacobi_symbol((u if u%2==1 else u+abs(M));M)]]'

    #old:'i/int -> M/int{=!=0}{%4<2} -> (-1|0|+1)/int'
    check_type_is(int, i)
    check_type_is(int, M)
    if not i > 0:raise NotImplementedError('bug:[1 == Kronecker_symbol(0;-1) == Kronecker_symbol(0*j;-1) == Kronecker_symbol(0;-1)*Kronecker_symbol(j;-1) == 1*Kronecker_symbol(j;-1)][Kronecker_symbol(j;-1) == +1] vs [Kronecker_symbol(3;-1) == -1]')

    if i == 0:return int(abs(M) == 1)
    # [i =!= 0]
    if i < 0:
        # [i < 0]
        # !! mine:[Kronecker_symbol(-1;M) == +1]
        i = -i
        # [i > 0]
    # [i > 0]
    if i == 1:return 1
    # [i >= 2]
    if i&1 == 0 == M&1:
        # [gcd(i,M)%2 == 0]
        # [gcd(i,M) =!= 1]
        return 0
    # [i >= 2]
    # [gcd(i,M)%2 == 1]
    (ez, odd) = factor_pint_out_power_of_base_(2, i)
    if ez&1:
        # [ez%2 == 1]
        # [ez > 0]
        # [i%2 == 0]
        # [M%2 == 1]
        match M&7:
            case 1|7:
                r = +1
            case 3|5:
                r = -1
            case M_mod8:
                raise Exception(i, M, ez, odd, M_mod8)
        r
    else:
        r = +1
    r
    odd
    r *= Jacobi_symbol(odd, M)
    return r



    r'''[[[
    if M == 0:raise ValueError(i, M)
    # [M =!= 0]
    if 0b000:
        if not M%4 < 2:raise ValueError(i, M)
        # [M%4 < 2]

    # !! [X(i) == X(i+M)]
    # !! [M =!= 0]
    u = i%abs(M)

    # [u >= 0]
    match u:
        case 0:
            r = int(abs(M) == 1)
        case 1:
            r = 1
        case _:
            # [u >= 2]
            ##################
            if 0b000:
                (ez, odd) = factor_pint_out_power_of_base_(2, u)
                if ez > 0:
                    m = M&7
                    if m&1 == 0:
                        r = 0
                    elif m == 1:
                        r = +1
                    elif m == 5:
                        r = -1
                    else:
                        # [M%2 == 1]
                        # [M%4 =!= 1]
                        # [M%4 == 3]
                        # !! [M%4 < 2]
                        # _L
                        raise Exception('not [M%4 < 2]', M)
                    r **= ez
                else:
                    r = 1
                r, odd
            ##################
            if u&1 == 0:
                # [u%2 == 0]
                if M&1 == 0:
                    # [M%2 == 0]
                    r = 0
                    #no:odd
                else:
                    # [M%2 == 1]
                    #bug:odd = u+M
                    odd = u+abs(M)
                    # [odd%abs(M) == u]
                    # !! [u >= 2]
                    # [odd >= 2]
                    # !! [M%2 == 1]
                    # !! [u%2 == 0]
                    # [odd%2 == 1]
                    # [odd >= 3]
                    r = 1
            else:
                # [u%2 == 1]
                odd = u
                # [odd%abs(M) == u]
                # !! [u >= 2]
                # [odd >= 2]
                # !! [u%2 == 1]
                # [odd%2 == 1]
                # [odd >= 3]
                r = 1
            r # ?odd
            # [[r==0]or[r==1][odd%abs(M) == u][odd%2==1][odd >= 3]]
            ##################
            r # ?odd
            if not r==0:
                assert odd&1 == 1
                r *= Jacobi_symbol(odd, M)
                    # ??? [M%2==0] => [Jacobi_symbol(odd, M) == Jacobi_symbol(odd+M, M)]
                    # ??? [Jacobi_symbol(odd, M) == Jacobi_symbol(odd+2*M, M)]
                    # !! [[m,a::int][m%2==1][a%2==1][gcd(a,m)==1] -> [Jacobi_symbol(m;a) == (-1)**((a-1)*(m-1)///4) * Jacobi_symbol(a,m)]]
                    # !! [[m,a::int][m%2==1] -> [Jacobi_symbol(m;a) == Jacobi_symbol(m;a%m)]]
            r
    #end-match u:
    r
    return r
    #]]]'''#'''

__all__
from seed.math.Kronecker_symbol import Kronecker_symbol
from seed.math.Kronecker_symbol import *
