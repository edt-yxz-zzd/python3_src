#__all__:goto
#TODO:goto
r'''[[[
e ../../python3_src/seed/math/Jacobi_symbol.py
vs:
    view ../../python3_src/seed/math/Kronecker_symbol.py
view others/数学/Jacobi_symbol.txt


py -m seed.math.Jacobi_symbol
from seed.math.Jacobi_symbol import Jacobi_symbol
from seed.math.Kronecker_symbol import Kronecker_symbol

注意:
    [[Jacobi_symbol(M;x)==-1] -> [is_square_nonresidual_mod_(M;x)]]
    但是:[Jacobi_symbol(M;x)==+1]无用，可能是也可能不是平方剩余
    [MAYBE:[Jacobi_symbol(M;x)==+1][is_square_nonresidual_mod_(M;x)]]

view others/数学/二次互反律.txt
[[[[[
二次互反律


二次互反律（quadratic reciprocity law）是一个用于判别二次剩余，即二次同余方程之整数解的存在性的定律。

定义勒让德符号(a:/p)
：p是奇素数。若存在整数x, 使得
  [(x^2-a)%p==0][not p\\\a]
，那么就记[(a:/p):=+1]
；否则就记[(a:/p):=-1]
。

[odd prime p] ==>> [(a:/p)==a^((p-1)///2)%p]
  proof:
    [2\\\(p-1)]
    *[(a:/p)==1]:
      [?x][x^2=[%p]=a]
      [a^((p-1)///2) = x^(p-1) =[%p]= 1 = (a:/p)]
    *[(a:/p)==-1]:
      [?r][order<%p> r == p-1]
      [r^((p-1)///2)%p !=1][r^((p-1)///2*2)%p ==1]
      [r^((p-1)///2) =[%p]=-1]

      [?e][r^(2*e+1)=[%p]=a]
      [a^((p-1)///2)
        = r^((2*e+1)*(p-1)///2)
        =[%p]= r^((2*e+1)*(p-1)///2%(p-1))
        = r^((p-1)///2)
        =[%p]= -1
        = (a:/p)
      ]

[odd prime p][gcd(a*b,p)==1] ==>> [(a*b:/p)==(a:/p)(b:/p)]


定义雅可比符号(a::/m)
  [odd m]
  [gcd(a*b,m)==1] ==>> [(a*b::/m)==(a::/m)(b::/m)]
  [gcd(a,m*n)==1] ==>> [(a::/(m*n))==(a::/m)(a::/n)]
注：雅可比符号是勒让德符号的推广，但是根据雅可比符号的值不能判断同余式是否有解。
雅可比符号 用于二次互反律计算 勒让德符号
计算 (a:/p):
  *只使用 勒让德符号
    (a:/p) = (a%%p:/p)
    [0!=abs(a)<=p//2]:
      *[-p//2<=a<0]:
        (a:/p)=(-1:/p)(-a:/p)
      *[0<a<=p//2]:
          (1:/p) = 1
          [a==2^e[2]*II q^e[q] {q | [q\\\a][prime q][odd q]}]:
          (a:/p) = (2:/p)^e[2] * II (q:/p)^e[q] {q | [q\\\a][prime q][odd q]}
          (2:/p) = ...
          (q:/p) = (p%%q:/q)(-1)^((p-1)(q-1)/4) = ...
  *使用 雅可比符号
    (a:/p) = (a::/p) = ...




二次互反律
设p和q为不同的奇素数，则
  [(p:/q)(q:/p)==(-1)^((p-1)(q-1)/4)]

2永远是(8n+/-1)型质数的平方剩余
，永远是(8n+/-3)型质数的非平方剩余。

-1永远是2或(4n+1)型质数的平方剩余
，永远是(4n-1)型质数的非平方剩余。



[[
Jacobi symbol
https://www.planetmath.org/CalculatingTheJacobiSymbol
https://brilliant.org/wiki/jacobi-symbol/

The Jacobi symbol is a generalization of the Legendre symbol. Introduced by Jacobi in 1837, it is of theoretical interest in modular arithmetic and other branches of number theory, but its main use is in computational number theory, especially primality testing and integer factorization; these in turn are important in cryptography.

The Jacobi symbol is a generalization of the Legendre symbol, which can be used to simplify computations involving quadratic residues. It shares many of the properties of the Legendre symbol, and can be used to state and prove an extended version of the law of quadratic reciprocity.

[is_prime p]:
  [Legendre_symbol(p,a) =[def]= if [a%p==0] then 0 else if [@[x<-[1..<p]] -> [(x**2 -a)%p =!= 0]] then -1 else +1]
[m,a::int][m%2==1][m>0]:
  [Jacobi_symbol(m,a) =[def]= II Legendre_symbol(p, a)**max_power_of_base_as_factor_of_(p,m) {p <- all_prime_factors_of(m)}]
  ###
  [Jacobi_symbol(m,a) ==
    if [gcd(a,m) =!= 1] then 0 else
    ???:if [m < 0] then Jacobi_symbol(-m,a) else
        #xxx:见下面:推广:[Jacobi_symbol(-1;a) == 1]
        # !! gp:[Kronecker_symbol(-1;a) == (-1)**[a<0]]
        # !! mine:[Kronecker_symbol(-1;a) == +1]
    if [m==1] then +1 else
    if [not$ 0 < a < m] then Jacobi_symbol(m,a%m) else
        # [Jacobi_symbol(m,a) == Jacobi_symbol(m,a%m)]
    #if [a==1] then +1 else
    if [a==2] then (-1)**((m**2-1)/8) else
      # Jacobi_symbol(m,2) = [m%8 <- {1,7}](+1) + [m%8 <- {3,5}](-1)
    if [a%2==0] then let [a == 2**e * b][b%2==1] in Jacobi_symbol(m,2)**(e%2) * Jacobi_symbol(m, b) else
    # [a%2==1][0 < a < m][gcd(a,m)==1]
    (-1)**((a-1)*(m-1)/4) * Jacobi_symbol(a,m)
      # 此时 可能有[a==1]: [Jacobi_symbol(1,m)==1]
  ]


###
The Legendre symbol measures whether a is a square mod p. Unfortunately, the Jacobi symbol does not retain this property:
  If gcd(a,m)=1 and a is a square mod m, where m is an odd positive integer, then Jacobi_symbol(m,a)=1; but the converse is not true.
    Jacobi_symbol(9,2) = Jacobi_symbol(3,2)**2 = (-1)**2 = 1
    Jacobi_symbol(35,3) = Jacobi_symbol(5,3)*Jacobi_symbol(7,3) = (-1)*(-1) = 1

[m > 0][m%2==1]:
  [a=[%m]=b]:
    [Jacobi_symbol(m,a) == Jacobi_symbol(m,b)]

  #completely multiplicative function
  [Jacobi_symbol(m, a*b) == Jacobi_symbol(m,a)*Jacobi_symbol(m,b)]

  [n > 0][n%2==1]:
    [Jacobi_symbol(m*n, a) == Jacobi_symbol(m,a)*Jacobi_symbol(n,a)]

  [n > 0][n%2==1][gcd(m,n)==1]:
    [Jacobi_symbol(m,n)*Jacobi_symbol(n,m) == (-1)**((m-1)/2) * (-1)**((n-1)/2)]
    # 比Legendre_symbol(m,n)计算更方便，无需完全分解n

  [Jacobi_symbol(m,-1) = (-1)**((m-1)/2)]
    # =1 <==> [m%4 == 1]
    # 4k+1型 素数p:  z**2=[%p]=-1, p=x**2+y**2, (x+y*j) = u*gcd(p, z+1*j), u <- {+1,-1,+j,-j}
  [Jacobi_symbol(m,2) = (-1)**((m**2-1)/8)]
    # =1 <==> [m%8 ≡ ±1]
  [Jacobi_symbol(m,1) = 1]

#Euler's criterion
[is_prime p][a%p =!= 0]:
  [Legendre_symbol(p,a) =[%p]= a**((p-1)/2)]
gives a criterion for primality:
  [m > 0][m%2==1]:
    [gcd(a,m)==1][[Jacobi_symbol(m,a) =![%m]!= a**((m-1)/2)] -> [not$ is_prime m]]
  It is not hard to show that if m is composite, then at least half the positive a less than m that are coprime to m satisfy this condition. Choosing random values of a k times leads to a probability of (1/2**k) that none of the random values are witnesses to the compositeness of m in this way. This probabilistic primality test is called the Solovay-Strassen primality test, and is quite efficient in practice.
  One interesting feature of the test is that it can be used to prove that numbers are composite without explicitly determining a nontrivial factor.

]]
]]]]]

#]]]'''
r'''[[[
[[

???推广:[m<0]:
    [Jacobi_symbol(-m;a) == Jacobi_symbol(m;a)*Jacobi_symbol(-1;a)]
    ??? [Jacobi_symbol(-1;a)
    == ??? Jacobi_symbol(-1;a%(-1))
    == Jacobi_symbol(-1;1)
    == (-1)**((1-1)*(-1-1)/4) * Jacobi_symbol(1,-1)
    == Jacobi_symbol(1,(-1)%1)
    == Jacobi_symbol(1,1)
    == 1
    ]
    ??? [Jacobi_symbol(-1;a) == 1]

    @20260815:改为:^NotImplementedError
        !! [Kronecker_symbol(-1;a) == (-1)**[a<0]]

[[m,a::int][m%2==1] -> [Jacobi_symbol(m;a) == Jacobi_symbol(m;a%m)]]
???二次互反律牜雅可比符号:
    [[m,a::int][m%2==1][a%2==1][gcd(a,m)==1] -> [Jacobi_symbol(m;a) == (-1)**((a-1)*(m-1)///4) * Jacobi_symbol(a;m)]]

    ==>>:
    [m,a::int][m%2==1][a%2==1][gcd(a,m)==1]:
        [Jacobi_symbol(m;a)
        == (-1)**((a-1)*(m-1)///4) * Jacobi_symbol(a;m)
        !! [[m,a::int][m%2==1] -> [Jacobi_symbol(m;a) == Jacobi_symbol(m;a%m)]]
        == (-1)**((a-1)*(m-1)///4) * Jacobi_symbol(a;m%(2*a))
        !! [m%2==1]
        => [m%(2*a) %2 == m%2 == 1]
        !! [gcd(a,m)==1]
        => [gcd(a,m%(2*a))==1]
        == (-1)**((a-1)*(m-1)///4) * (-1)**((m%(2*a)-1)*(a-1)///4) * Jacobi_symbol(m%(2*a);a)
        == (-1)**((a-1)*((m-1)+(m%(2*a)-1))///4) * Jacobi_symbol(m%(2*a);a)
        == (-1)**((a-1)///2*((m//(2*a) *(2*a))///2 +m%(2*a) -1)) * Jacobi_symbol(m%(2*a);a)
        == (-1)**((a-1)///2*((m//(2*a))*a +m%(2*a) -1)) * Jacobi_symbol(m%(2*a);a)
        !! [m%(2*a) %2 == m%2 == 1]
        == (-1)**((a-1)///2*((m//(2*a))*a)) * Jacobi_symbol(m%(2*a);a)
        !! [a%2==1]
        == (-1)**((a-1)///2*(m//(2*a))) * Jacobi_symbol(m%(2*a);a)
        ]
        [Jacobi_symbol(m;a) == (-1)**((a-1)///2*(m//(2*a))) * Jacobi_symbol(m%(2*a);a)]
        [[a%4 == 1] -> [Jacobi_symbol(m;a) == Jacobi_symbol(m%(2*a);a)]]
        [[a%4 == 1] -> [i::int] -> [Jacobi_symbol(m+a*2*i;a) == Jacobi_symbol(m%(2*a);a) == Jacobi_symbol(m;a)]]
        [[a%4 == 1] -> [i::int] -> [Jacobi_symbol(m+a*2*i;a) == Jacobi_symbol(m;a)]]



        [Jacobi_symbol(m;a)
        == (-1)**((a-1)*(m-1)///4) * Jacobi_symbol(a;m)
        == (-1)**((a-1)*(m-1)///4) * Jacobi_symbol(a;m+a*4)
        !! [m%2 == 1]
        => [(m+4*a)%2 == 1]
        !! [gcd(a,m)==1]
        => [gcd(a,m+4*a)==1]
        == (-1)**((a-1)*(m-1)///4) * (-1)**((a-1)*(m+a*4-1)///4) * Jacobi_symbol(m+a*4;a)
        == (-1)**((a-1)*(2*(m-1)+a*4)///4) * Jacobi_symbol(m+a*4;a)
        == (-1)**(2 * ((a-1)///2) * ((m-1)///2 +a)) * Jacobi_symbol(m+a*4;a)
        == Jacobi_symbol(m+a*4;a)
        ]
        [Jacobi_symbol(m;a) == Jacobi_symbol(m+a*4;a)]
        [[i::int] -> [Jacobi_symbol(m;a) == Jacobi_symbol(m+a*4*i;a)]]
        [Jacobi_symbol(m;a) == Jacobi_symbol(m%(a*4);a)]

        [Jacobi_symbol(m;a*4)
        == Jacobi_symbol(m;a) * Jacobi_symbol(m;2)**2
        == Jacobi_symbol(m;a)
        ]
        [Jacobi_symbol(m;a*4) == Jacobi_symbol(m;a)]
        !! [Jacobi_symbol(m;a) == Jacobi_symbol(m+a*4;a)]
        [[k::uint] -> [Jacobi_symbol(m;a*4**k) == Jacobi_symbol(m+a*4;a*4**k)]]
        [[k::uint] -> [Jacobi_symbol(m;a*4**k) == Jacobi_symbol(m%(a*4**max(1,k));a*4**k)]]
        [[k::uint] -> [Jacobi_symbol(m;a*4*4**k) == Jacobi_symbol(m%(a*4*4**k);a*4*4**k)]]



        [Jacobi_symbol(m;a*2)
        == Jacobi_symbol(m;a) * Jacobi_symbol(m;2)
        !! [[i::int] -> [Jacobi_symbol(m;a) == Jacobi_symbol(m+a*4*i;a)]]
        == Jacobi_symbol(m%(8*a);a) * Jacobi_symbol(m;2)
        !! [Jacobi_symbol(m;2) == Jacobi_symbol(m%8;2) == Jacobi_symbol(m%(8*a);2)]
        == Jacobi_symbol(m%(8*a);a) * Jacobi_symbol(m%(8*a);2)
        == Jacobi_symbol(m%(8*a);a*2)
        ]
        [Jacobi_symbol(m;a*2) == Jacobi_symbol(m%(8*a);a*2)]

        [[k::uint] -> [Jacobi_symbol(m;a*2*4**k) == Jacobi_symbol(m%(8*a);a*2*4**k)]]
        [[k::uint] -> [Jacobi_symbol(m%(8*a*4**max(0,k-1));a*2*4**k) == Jacobi_symbol(m%(8*a*4**max(0,k-1))%(8*a);a*2*4**k) == Jacobi_symbol(m%(8*a);a*2*4**k) == Jacobi_symbol(m;a*2*4**k)]]
        [[k::uint] -> [Jacobi_symbol(m;a*2*4**k) == Jacobi_symbol(m%(8*a*4**max(0,k-1));a*2*4**k)]]
        [[k::uint] -> [Jacobi_symbol(m;a*8*4**k) == Jacobi_symbol(m%(8*a*4**k);a*8*4**k)]]
        !! [[k::uint] -> [Jacobi_symbol(m;a*4*4**k) == Jacobi_symbol(m%(a*4*4**k);a*4*4**k)]]
        [[k::uint] -> [Jacobi_symbol(m;a*4*2**k) == Jacobi_symbol(m%(a*4*2**k);a*4*2**k)]]
    ==>>:
    [m,a::int][m%2==1][a%2==1][gcd(a,m)==1]:
        [[k::uint] -> [Jacobi_symbol(m;a*4*2**k) == Jacobi_symbol(m%(a*4*2**k);a*4*2**k)]]
        [[a%4 == 1] -> [Jacobi_symbol(m;a) == Jacobi_symbol(m%(2*a);a)]]
            # 注意:『%(2*a)』而非『%a』
        [a%4 == 1][i::int]:
            [Kronecker_symbol(m;a)
            !! [m%2==1]
            == Jacobi_symbol(m;a)
            !! [[a%4 == 1] -> [i::int] -> [Jacobi_symbol(m+a*2*i;a) == Jacobi_symbol(m;a)]]
            == Jacobi_symbol(m+i*(2*a);a)
            !! [(m+i*(2*a))%2==1]
            == Kronecker_symbol(m+i*(2*a);a)
            ]
            [Kronecker_symbol(m;a) == Kronecker_symbol(m+i*(2*a);a)]
            [Kronecker_symbol(2*m;a)
            =?= Kronecker_symbol(2*m+2*a;a)
            TODO:...看来还是得从零开始,Jacobi_symbol指望不上
            ]

    [[m,D::int][m%2==1][gcd(D,m)==1][D%4 < 2] -> [Jacobi_symbol(m;D) == Jacobi_symbol(m%(2**(D%2)*D);D)]]
    [[m,D::int][m%2==1][gcd(D,m)==1][D%4 < 2] -> [Jacobi_symbol(m;D) == Jacobi_symbol(m%(2*D);D)]]
    TODO:bug:[[m,D::int][m%2==1][gcd(D,m)==1][D%4 < 2] -> [Jacobi_symbol(m;D) == Jacobi_symbol(m%D;D)]]
        # 只需:[D%4 < 2][gcd(D,m)==1]
        # 无需:[D < 0]
        # Kronecker_symbol周期性前提:[D%4 < 2]
        # view ../../python3_src/seed/math/Kronecker_symbol.py

]]



#]]]'''#'''
__all__ = '''
    Jacobi_symbol

    '''.split()
from seed.math.gcd import gcd
from seed.math.divmod__half import mod__half
from seed.math.max_power_of_base_as_factor_of_ import factor_nonzero_int_out_sign_and_2_powers



def __():
    def Jacobi_symbol(M, x, /):
        'M/int{%2==1} -> x/int -> Jacobi_symbol(x::/M)/(-1|0|+1)'
        if not type(M) is int: raise TypeError
        if not type(x) is int: raise TypeError
        if not M%2==1: raise ValueError
        if M < 0: raise NotImplementedError('bug:[1 == Kronecker_symbol(0;-1) == Kronecker_symbol(0*j;-1) == Kronecker_symbol(0;-1)*Kronecker_symbol(j;-1) == 1*Kronecker_symbol(j;-1)][Kronecker_symbol(j;-1) == +1] vs [Kronecker_symbol(3;-1) == -1]')

        if 0b000:
            if M < 0: raise NotImplementedError('pari-gp:[Kronecker_symbol(-1;k) == (-1)**[k<0]] vs mine:[Kronecker_symbol(-1;k) == +1]')



        # !! mine:[Kronecker_symbol(-1;k) == +1]
        M = abs(M)
        if not gcd(M, x) == 1: return 0
        x = mod__half(x, M)
        return recur(M, x)
    def on__x_eq_neg1(M, /):
        #if x == -1:
        return +1 if M%4==1 else -1
    def on__x_eq_2(M, /):
        #if x == 2:
        return +1 if (M%8) in [1,7] else -1
    _f = factor_nonzero_int_out_sign_and_2_powers
    def recur(M, x, /):
        #assert M > 0
        #assert M%2 == 1
        #assert gcd(M, x) == 1
        #assert x == mod__half(x, M)
        r = +1
        while not M==1:
            #assert M > 0
            #assert M%2 == 1
            #assert gcd(M, x) == 1
            #assert x == mod__half(x, M)
            #if M == 1: return +r
            #if x == 1: return +r
            #if x == 2: return r*on__x_eq_2(M)
            #if x == -1: return r*on__x_eq_neg1(M)
            #x = mod__half(x, M)
            (sign, e, odd) = _f(x)
            if sign < 0:
                r *= on__x_eq_neg1(M)
            if e%2==1:
                r *= on__x_eq_2(M)
            if (odd%4-1)*(M%4-1) //4 %2 == 1:
                r = -r
            #assert gcd(M, x) == 1
            #assert gcd(M, odd) == 1
            #assert odd > 0
            #assert odd%2 == 1

            M, x = odd, M
            #assert M > 0
            #assert M%2 == 1
            #assert gcd(M, x) == 1
            x = mod__half(x, M)
            #assert x == mod__half(x, M)
        #assert M==1
        return +r
    return Jacobi_symbol

Jacobi_symbol = __()
assert Jacobi_symbol(1, 0) == +1

assert Jacobi_symbol(3, 2) == -1
assert Jacobi_symbol(5, 2) == -1
assert Jacobi_symbol(7, 2) == +1
assert Jacobi_symbol(9, 2) == +1 ### Jacobi_symbol(3, 2)**2
assert Jacobi_symbol(11, 2) == -1

assert Jacobi_symbol(3, -1) == -1
assert Jacobi_symbol(5, -1) == +1
assert Jacobi_symbol(7, -1) == -1
assert Jacobi_symbol(9, -1) == +1
assert Jacobi_symbol(11, -1) == -1



assert Jacobi_symbol(97, 49) == +1
assert Jacobi_symbol(97, 36) == +1
assert Jacobi_symbol(97, 25) == +1
assert Jacobi_symbol(97, 100) == +1
assert Jacobi_symbol(97, 121) == +1
assert Jacobi_symbol(97, 144) == +1
assert Jacobi_symbol(97, 169) == +1
assert Jacobi_symbol(97, 196) == +1
assert Jacobi_symbol(97, 225) == +1
assert Jacobi_symbol(97, 256) == +1

assert all(Jacobi_symbol(11, x)==+1 for x in [1, 4, 9, 5, 3])
assert all(Jacobi_symbol(11, x)==-1 for x in [2, 6, 7, 8, 10])


def _t(N, /):
    from nn_ns.math_nn.prime2 import primes_lt
    for p in primes_lt(N)[1:]:
        sqs = [i**2%p for i in range(1,p//2+1)]
        sqs.sort()
        r2ls = [[], [], []]
        for i in range(0,p):
            r = Jacobi_symbol(p, i)
            r2ls[r].append(i)
        assert [0] == r2ls[0]
        assert sqs == r2ls[+1] != r2ls[-1]
        assert len(r2ls[+1]) == len(r2ls[-1])

if __name__ == "__main__":
    from seed.math.Jacobi_symbol import Jacobi_symbol
    from seed.math.Jacobi_symbol import *
    _t(100)
    pass



from seed.math.Jacobi_symbol import Jacobi_symbol
from seed.math.Jacobi_symbol import *
