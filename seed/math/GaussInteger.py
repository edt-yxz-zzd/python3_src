#__all__:goto
r'''[[[
e ../../python3_src/seed/math/GaussInteger.py

used by:
    view script/平方和.py
        py script/平方和.py main1__show_Gauss_integer_factor_coeffs_of_4k1_prime_lt =100
        py script/平方和.py main2__show_right_angled_triangles_with_coprime_side_length__len_hypotenuse_lt =100

[[
why__HOE
[:why_use_form_1odd_1jeven]:here
===
why (odd +/- 1j*even)?
    + [(%2) unchanged under __mul__]
        [(odd1 + 1j*even2)*(odd3 + 1j*even4) == (odd1*odd3 -even2*even4) + 1j*(odd1*even4 +even2*odd3) == odd5 + 1j*even6]
    + [unity is (1+0j)]
]]

py -m nn_ns.app.debug_cmd   seed.math.GaussInteger -x
py -m nn_ns.app.doctest_cmd seed.math.GaussInteger:__doc__ -df -ff -v



[349,353,373,389,397]
py -m nn_ns.app.adhoc_argparser__main__call8module   seed.math.GaussInteger @find_Gauss_integer_factor_coeffs_of_4k1_prime =349 =None
(5, 18)
py_adhoc_call   seed.math.GaussInteger ,iter_Gauss_integer_factor_coeffs_of_4k1_prime__ge_lt =349 =398 +turnon__is_prime__le_pow2_64
(349, 5, 18)
(353, 17, 8)
(373, 7, 18)
(389, 17, 10)
(397, 19, 6)


[[[
py_adhoc_call   seed.math.GaussInteger ,iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_lt =100 +SML_vs_HOE +to_sort -turnoff__coprime
===
(5, 3, 4)
(13, 5, 12)
(17, 15, 8)
(25, 7, 24)
(29, 21, 20)
(37, 35, 12)
(41, 9, 40)
(53, 45, 28)
(61, 11, 60)
(65, 33, 56)
(65, 63, 16)
(73, 55, 48)
(85, 13, 84)
(85, 77, 36)
(89, 39, 80)
(97, 65, 72)
===
]]]
[[[
py_adhoc_call   seed.math.GaussInteger ,iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_lt =100 +SML_vs_HOE +to_sort +turnoff__coprime
===
(5, 3, 4)
(10, 6, 8)
(13, 5, 12)
(15, 9, 12)
(17, 15, 8)
(20, 12, 16)
(25, 7, 24)
(25, 15, 20)
(26, 10, 24)
(29, 21, 20)
(30, 18, 24)
(34, 30, 16)
(35, 21, 28)
(37, 35, 12)
(39, 15, 36)
(40, 24, 32)
(41, 9, 40)
(45, 27, 36)
(50, 14, 48)
(50, 30, 40)
(51, 45, 24)
(52, 20, 48)
(53, 45, 28)
(55, 33, 44)
(58, 42, 40)
(60, 36, 48)
(61, 11, 60)
(65, 25, 60)
(65, 33, 56)
(65, 39, 52)
(65, 63, 16)
(68, 60, 32)
(70, 42, 56)
(73, 55, 48)
(74, 70, 24)
(75, 21, 72)
(75, 45, 60)
(78, 30, 72)
(80, 48, 64)
(82, 18, 80)
(85, 13, 84)
(85, 51, 68)
(85, 75, 40)
(85, 77, 36)
(87, 63, 60)
(89, 39, 80)
(90, 54, 72)
(91, 35, 84)
(95, 57, 76)
(97, 65, 72)
===
]]]
[[[
py_adhoc_call   seed.math.GaussInteger ,100:iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_lt =None +SML_vs_HOE +to_sort -turnoff__coprime
===
(5, 3, 4)
(13, 5, 12)
(17, 15, 8)
(25, 7, 24)
(29, 21, 20)
(37, 35, 12)
(41, 9, 40)
(53, 45, 28)
(61, 11, 60)
(65, 33, 56)
(65, 63, 16)
(73, 55, 48)
(85, 13, 84)
(85, 77, 36)
(89, 39, 80)
(97, 65, 72)
(101, 99, 20)
(109, 91, 60)
(113, 15, 112)
(125, 117, 44)
(137, 105, 88)
(145, 17, 144)
(145, 143, 24)
(149, 51, 140)
(157, 85, 132)
(169, 119, 120)
(173, 165, 52)
(181, 19, 180)
(185, 57, 176)
(185, 153, 104)
(193, 95, 168)
(197, 195, 28)
(205, 133, 156)
(205, 187, 84)
(221, 21, 220)
(221, 171, 140)
(229, 221, 60)
(233, 105, 208)
(241, 209, 120)
(257, 255, 32)
(265, 23, 264)
(265, 247, 96)
(269, 69, 260)
(277, 115, 252)
(281, 231, 160)
(289, 161, 240)
(293, 285, 68)
(305, 207, 224)
(305, 273, 136)
(313, 25, 312)
(317, 75, 308)
(325, 253, 204)
(325, 323, 36)
(337, 175, 288)
(349, 299, 180)
(353, 225, 272)
(365, 27, 364)
(365, 357, 76)
(373, 275, 252)
(377, 135, 352)
(377, 345, 152)
(389, 189, 340)
(397, 325, 228)
(401, 399, 40)
(409, 391, 120)
(421, 29, 420)
(425, 87, 416)
(425, 297, 304)
(433, 145, 408)
(445, 203, 396)
(445, 437, 84)
(449, 351, 280)
(457, 425, 168)
(461, 261, 380)
(481, 31, 480)
(481, 319, 360)
(485, 93, 476)
(485, 483, 44)
(493, 155, 468)
(493, 475, 132)
(505, 217, 456)
(505, 377, 336)
(509, 459, 220)
(521, 279, 440)
(533, 435, 308)
(533, 525, 92)
(541, 341, 420)
(545, 33, 544)
(545, 513, 184)
(557, 165, 532)
(565, 403, 396)
(565, 493, 276)
(569, 231, 520)
(577, 575, 48)
(593, 465, 368)
(601, 551, 240)
(613, 35, 612)
(617, 105, 608)
(625, 527, 336)
(629, 429, 460)
===
]]]


#]]]'''
__all__ = '''
    is_zero__Gauss_integer
    neg__Gauss_integer
    conj__Gauss_integer
    square_len__Gauss_integer
    cmp_len__Gauss_integer
    cmp_square_len_ex__Gauss_integer
    mul__Gauss_integer
    add__Gauss_integer
    sub__Gauss_integer
    divmod__Gauss_integer
    gcd__Gauss_integer
    find_Gauss_integer_factor_coeffs_of_4k1_prime
    find_sqrt_neg1_of_4k1_prime_ex
    find_sqrt_neg1_of_4k1_prime

    uint2str_bits
    pow__Gauss_integer
    square__Gauss_integer

    iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_lt
        iter_len_hypotenuse_of_right_angled_triangles_with_coprime_side_length__with_factorisation__lt
        iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_eq


    iter_Gauss_integer_factor_coeffs_of_4k1_prime__ge_lt
    iter_4k1_primes__ge_lt


    '''.split()
    #divmod__half
    #sign_of
__all__

from itertools import count, islice

from seed.tiny import curry1
from seed.iters.iterate import iterate

from seed.math.max_power_of_base_as_factor_of_ import max_power_of_base_as_factor_of_
from seed.math.sign_of import sign_of
from seed.math.II import II
from seed.math.gcd import gcd
from seed.math.divmod__half import divmod__half#, mod__half

from seed.math.is_prime__le_pow2_64 import is_prime__le_pow2_64

if 0:
  def sign_of(x, /):
    if x==0:
        return 0
    return 1 if x>0 else -1

  def divmod__half(n,d,/):
    (q,r) = divmod(n, d)
    if 2*r > abs(d):
        r -= abs(d)
        q += sign_of(d)
    assert q*d+r == n
    assert 2*abs(r) < abs(d) or 2*r == abs(d)
    return (q,r)
def is_zero__Gauss_integer(ab, /):
    a, b = ab
    return a == 0 == b
def neg__Gauss_integer(ab, /):
    a, b = ab
    return (-a, -b)
def conj__Gauss_integer(ab, /):
    a, b = ab
    return (a, -b)
def square_len__Gauss_integer(ab, /):
    a, b = ab
    return a**2+b**2
def cmp_len__Gauss_integer(ab, cd, /):
    x = square_len__Gauss_integer(ab) - square_len__Gauss_integer(cd)
    return sign_of(x)
def cmp_square_len_ex__Gauss_integer(kL, ab, kR, cd, /):
    x = kL*square_len__Gauss_integer(ab) - kR*square_len__Gauss_integer(cd)
    return sign_of(x)
def mul__Gauss_integer(ab, cd, /):
    a, b = ab
    c, d = cd
    A = a*c-b*d
    B = b*c+a*d
    return A, B
def add__Gauss_integer(ab, cd, /):
    a, b = ab
    c, d = cd
    return (a+c, b+d)
def sub__Gauss_integer(ab, cd, /):
    a, b = ab
    c, d = cd
    return (a-c, b-d)
def divmod__Gauss_integer(ab, cd, /):
    'divmod(a+b*j, c+d*j)'
    conj_cd = conj__Gauss_integer(cd)
    A, B = mul__Gauss_integer(ab, conj_cd)
    C, D = mul__Gauss_integer(cd, conj_cd)
    assert D == 0
    r'''
    C = c**2+d**2
    D = 0
    A = a*c+b*d
    B = b*c-a*d

    [(a+b*j)/(c+d*j)
    == (a+b*j)*(c-d*j)/((c+d*j)*(c-d*j))
    == (A+B*j)/(C+D*j)
    == (A+B*j)/C
    == (qA+qB*j) +(rA+rB*j)/C
    ]
    #'''
    qA, rA = divmod__half(A, C)
    qB, rB = divmod__half(B, C)
    Q = (qA, qB)
    R = sub__Gauss_integer(ab, mul__Gauss_integer(Q, cd))
    assert cmp_len__Gauss_integer(R, cd) < 0
    assert cmp_square_len_ex__Gauss_integer(2, R, 1, cd) <= 0
    return (Q, R)
def gcd__Gauss_integer(ab, cd, /):
    while not is_zero__Gauss_integer(cd):
        (Q,R) = divmod__Gauss_integer(ab, cd)
        ab, cd = cd, R
    return ab
def find_Gauss_integer_factor_coeffs_of_4k1_prime(p__4k1, may_sqrt_neg1, /):
    r'->(odd, even) s.t. [odd**2+even**2==p__4k1]'
    if not p__4k1%4 == 1: raise ValueError
    if not p__4k1 > 0: raise ValueError

    if may_sqrt_neg1 is None:
        sqrt_neg1 = find_sqrt_neg1_of_4k1_prime(p__4k1)
    else:
        sqrt_neg1 = may_sqrt_neg1

    if not (sqrt_neg1**2+1)%p__4k1 ==0: raise ValueError
    p = p__4k1
    sqrt_neg1 = (sqrt_neg1)%p
    sqrt_neg1 = min(sqrt_neg1, p-sqrt_neg1)

    (a,b) = gcd__Gauss_integer((p,0), (sqrt_neg1,1))
    a = abs(a)
    b = abs(b)
    #sqrt_p = floor_sqrt_(p)
    #assert 0 < a <= sqrt_p
    #assert 0 < b <= sqrt_p
    #assert a**2 + b**2 == p
    (odd, even) = (a, b) if a%2==1 else (b, a)
        # [:why_use_form_1odd_1jeven]:goto
    assert even%2==0
    assert odd%2==1
    assert odd > 0
    assert even > 0
    assert odd**2 + even**2 == p
    return (odd, even)
    r'''
    [lhs = a**2 + b**2 =[%p]= 0][0 < a,b <= floor_sqrt_(p)]:
        [0 < lhs <= 2*floor_sqrt_(p)**2 <= 2*(p-1) <= 2*p-2]
        !![lhs%p==0]
        [lhs==p]
        [b = a*sqrt_neg1%p]or[b = a*(-sqrt_neg1)%p]
    #'''
    r'''
    p1 = p-1
    for _ in range(2):
        (q,r) = divmod(p, sqrt_neg1)
            # r = p - q*sqrt_neg1
            # -r%p = q*sqrt_neg1
        t = (sqrt_neg1 - sqrt_p +r-1) //r
        if sqrt_neg1 <= t*r:
            ...
            raise ... .TODO
        assert 0 < sqrt_neg1 - t*r <= sqrt_p, (p, sqrt_neg1, sqrt_p, r, t)
        assert sqrt_neg1 * (1+ t*q) % p == sqrt_neg1 - t*r
        a = (1+ t*q) % p
        if a > sqrt_p:
            sqrt_neg1 = p - sqrt_neg1
        else:
            break
    else:
        raise logic-err
    a
    b = a*sqrt_neg1 %p
    assert 0 < a <= sqrt_p
    assert 0 < b <= sqrt_p
    assert a**2 + b**2 == p
    (odd, even) = (a, b) if a%2==1 else (b, a)
    return (odd, even)
    #'''
def find_sqrt_neg1_of_4k1_prime_ex(p__4k1, /):
    '-> (sqrt_neg1, num_tries)'
    if not p__4k1%4 == 1: raise ValueError
    if not p__4k1 > 0: raise ValueError
    p = p__4k1
    p1 = p-1
    e = max_power_of_base_as_factor_of_(2, p1)
    assert e >= 2
    odd = (p1)>>e
    assert odd&1
    r'''
    [(p//2+1)**2 %p
    ==(p//2)**2 %p
    == (2*k)**2 %(4*k+1)
    == (4*k**2) %(4*k+1)
    == (k*(4*k +1) -k) %(4*k+1)
    == (-k) %(4*k+1)
    == (3*k+1) %(4*k+1)
    == (p-k) %p
    ]
    k = (p1)>>2
    assert p == 4*k+1
    # i <- [2*k+1..]
    # [i==2*k+1] -> [i**2%p == p-k]
    i = 2*k+1
    i2 = p-k
    while not i2 == p1:
        # (i+1)**2 -i**2 == 2*i+1
        i += 1
    #'''
    #r = floor_sqrt_(p)
    #for r in range(r, p//2+1):
    #for r in range(p//2+1, p-floor_sqrt_(p)):
    num_tries = 0
    for x in range(p//2, 0, -1):
        num_tries += 1
        r = pow(x,odd,p)
        for _ in range(e):
            x = r
            r = pow(x, 2, p)
            if r == p1:
                x = min(x, p-x)
                assert (x**2+1)%p ==0
                sqrt_neg1 = x
                return (sqrt_neg1, num_tries)
            if r == 1: break
        if not r == 1: raise ValueError(f'p={p} is not prime')
    raise logic-err


def find_sqrt_neg1_of_4k1_prime(p__4k1, /):
    '-> sqrt_neg1'
    (sqrt_neg1, num_tries) = find_sqrt_neg1_of_4k1_prime_ex(p__4k1)
    return sqrt_neg1

def uint2str_bits(u, /):
    if not u >= 0: raise ValueError
    s = bin(u)
    assert s[:2] == '0b'
    s = s[2:]
    if s[0] == '0':
        assert s == '0'
        #s = ''
        s = s[1:]
    assert not s or s[0] == '1'
    return s
def pow__Gauss_integer(ab, e, /):
    s = uint2str_bits(e)
    acc = (1,0)
    for ch in reversed(s):
        if ch == '1':
            acc = mul__Gauss_integer(acc, ab)
        ab = square__Gauss_integer(ab)
    return acc
def square__Gauss_integer(ab, /):
    a, b = ab
    return (a**2-b**2, 2*a*b)
assert pow__Gauss_integer((1,1), 2) == (0,2)
assert pow__Gauss_integer((1,1), 4) == (-4,0)
assert pow__Gauss_integer((1,1), 6) == (0,-8)
assert pow__Gauss_integer((1,1), 7) == (8,-8)

#def mul__Gauss_integer(ab, cd, /):
#def iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_eq(c, factorisation_of_c, /):
def iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_eq(c, factorisation_of_c, /, *, SML_vs_HOE, to_sort, turnoff__coprime):
    r'''[[[
:: len_hypotenuse -> factorisation_of<len_hypotenuse>-> Iter (len_hypotenuse, odd, even)

这里用到的算法:参数:斜边的整数分解
    以斜边平方的整数分解组合出斜边平方的所有共轭高斯整数分解并以实部虚部作为直角边边长
    [j2pe := factorisation_of_(hypotenuse_side).items()]
    [j2sign :: [{+1,-1}]{len==len(j2pe}]
    [j2sign[0] == +1]
    [hypotenuse_side**2 == II{(odd4p -1j*even4p)**(2*e4p) *(odd4p +1j*even4p)**(2*e4p) | [[(p,e4p) :<- j2pe][(odd4p, even4p) :=> [[p == odd4p**2 +even4p**2][even4p%2==0]]]]} == (xy:=II{(odd4p -1j*j2sign[j4p]*even4p)**(2*e4p) | ...}) * conj__Gauss_integer(xy) == (odd_side -1j*even_side)*(odd_side +1j*even_side) == odd_side**2 +even_side**2]
或 其他算法:
    参数: k,s,t
    bug:[k >= 1][1 <= t < s][gcd(s,t)==1]
    [k >= 1][1 <= t < s][gcd(s,t)==1][s%2 =!= t%2]
    (len_hypotenuse, maybe_odd, must_even) := k*(s**2+t**2, s**2-t**2, 2*s*t)
    view ../../python3_src/seed/math/right_angled_triangle_infos__sorted_by.py
        # [:互素整数边长直角三角形的边长表达型式囗囗以斜边的共轭高斯整数分解的实部虚部为参数:[(hypotenuse_side,odd_side,even_side) == (s*s +t*t, s*s -t*t, 2*s*t]]:goto

######################
output Iter<(S, M, L)> but sorted by key (L, S, M)/(long,short,middle) if SML_vs_HOE is False
output Iter<(hypotenuse,odd,even)> sorted by key echo if SML_vs_HOE is True
#
[SML =[def]= (short_side, middle_side, long_side)]
[HOE =[def]= (hypotenuse_side, odd_side, even_side)]
######################


[[[[[
Hypotenuse
    hypotenuse 直角三角形的斜边
    What Is The Longest Side Of A Triangle Called?
    The longest side of a right angled triangle is called its hypotenuse.

[primitive Pythagorean triple =[def]= (A,B,C) where A^2 + B^2 = C^2 with 0 < A < B < C and gcd(A,B)=1]
    https://oeis.org/A156685
    A156685 Number of primitive Pythagorean triples A^2 + B^2 = C^2 with 0 < A < B < C and gcd(A,B)=1 that have a hypotenuse C that is less than or equal to n.
https://oeis.org/A156685
    斜边边长小于等于n的整边互素直角三角形累积数量
https://oeis.org/A024362
    斜边边长等于n的整边互素直角三角形数量


[a,b,c :: PInt][a**2+b**2==c**2][gcd(a,b,c)==1]:
    !![a**2+b**2==c**2]
    [gcd(a,b,c)==1]
        <==>[gcd(a,b)==1]
        <==>[gcd(a,c)==1]
        <==>[gcd(c,b)==1]

    [a%2==1==b%2]:
        [a**2%4==1==b**2%4]
        [(a**2+b**2)%4 ==2]
        [c**2%4 <- {0,1}]
        _L
    [a%2==0==b%2]:
        [a**2%4==0==b**2%4]
        [c**2%4 == (a**2+b**2)%4 ==0]
        [c%2==0]
        !![gcd(a,b,c)==1]
        _L
    [a%2=!=b%2]
    [c%2==1]
    * [a%2==0][b%2==1]:
        交换名称，同下
    * [a%2==1][b%2==0]:
        [is_prime(p)][e:=max_power_of_base_as_factor_of_(p,c)][e>=1]:
            * [p==2]:
                !![c%2==1]
                _L
            * [p%4==3]:
                [not$ [?x,y. [x**2+y**2==p]]]
                [c**2 == a**2+b**2 == (a-b*j)*(a+b*j)]
                [(a-b*j)%p==0]
                [a%p==0]
                [b%p==0]
                [gcd(a,b,c)%p==0]
                !![gcd(a,b,c)==1]
                _L
            * [p%4==1]:
                [?x,y. [x**2+y**2==p]]
                [c**2 == a**2+b**2 == (a-b*j)*(a+b*j)]
                !![gcd(a,b,c)==1]
                [(a-b*j)%p=!=0]
                [[(a-b*j)%(x+y*j)==0]=!=[(a-b*j)%(x-y*j)==0]]
                [(a-b*j)%(x+y*j)==0]:
                    [(a-b*j)%(x+y*j)**e==0]

    ...
    [边长为整数的直角三角形的面积也是整数] #至少一直角边的边长为偶数
    [c的所有素因子都是(4*k+1)型素数]
    [若c的不同素因子的总数是n>1，则无序对{a,b}的组合数为2**(n-1), 是 以下复数的实部与虚部: [c=II p[i]**e[i] {i<-[0..<n]}][p[i] == x[i]**2+y[i]**2] -> [复数=(x[0]-y[0]*j)**(2*e[0]) * II (x[i]-s[i]*y[i]*j)**(2*e[i]) {i<-[1..<n], s[i]<-{-1,+1}}]]




??integer rectangular solid??没有这个称谓
    The “Integer Brick” Problem
    (The Euler Brick Problem)
    perfect cuboid = Euler brick & integer space diagonal
    [[
https://mathworld.wolfram.com/PerfectCuboid.html
https://mathworld.wolfram.com/EulerBrick.html
===
If the space diagonal is also an integer, the Euler brick is called a perfect cuboid, although no examples of perfect cuboids are currently known.
A perfect cuboid is a cuboid having integer side lengths, integer face diagonals and an integer space diagonal.
The problem of finding such a cuboid is also called the brick problem, diagonals problem, perfect box problem, perfect cuboid problem, or rational cuboid problem.

No perfect cuboids are known despite an exhaustive search for all "odd sides" up to 10^(10) (Butler, pers. comm., Dec. 23, 2004).
    ]]
有没有 整数长方体？即 任意2个顶点之间的距离为整数？
    设 边长为a,b,c
    设 面对角线长度为ab,ac,bc
    设 体对角线长度为abc
    a**2+b**2 = ab**2
    a**2+c**2 = ac**2
    b**2+c**2 = bc**2
    a**2+b**2+c**2 = abc**2
        a**2+bc**2 = abc**2
    [gcd(a,b,c,ab,bc,ac,abc)==1]:
        let Ls = {a,b,c,ab,bc,ac,abc}
        [gcd(Ls)==1]
        [a%2==0][b%2==0][c%2==0]:
            [gcd(Ls)%2==0]
            _L
        [[a%2==1]+[b%2==1]+[c%2==1] >=1]
        [a%2==1][b%2==1]:
            !![a**2+b**2 = ab**2]
            [ab**2%4 == 2]
            !![ab :: int]
            _L
        [[a%2==1]+[b%2==1] <=1]
        [[a%2==1]+[c%2==1] <=1]
        [[c%2==1]+[b%2==1] <=1]
        [[a%2==1]+[b%2==1]+[c%2==1] <=1]
        !![[a%2==1]+[b%2==1]+[c%2==1] >=1]
        [[a%2==1]+[b%2==1]+[c%2==1] ==1]

        * [c%2==1]:
            同下
        * [b%2==1]:
            同下
        * [a%2==1]:
            [b%2==0][c%2==0]
            [ac%2==1][ab%2==1]
            [bc%2==0]
            [abc%2==1]
            ！错:一个未必完整遍历的构造方法:
                边长互素的整数三角形:
                    #(hypotenuse,odd,even)
                    (h1,o1,e1)
                    (h2,o2,e2)
                    ###
                [gcd(o1,e1)==1]
                [gcd(o2,e2)==1]
                [e1%2==0]
                [h2%2==1]

                let g := gcd(h2,e1)
                [gcd(h2/g,e1/g)==1]
                [g%2==1]

                let h2e1 := h2*e1/g # lcm(h2,e1)
                    (h1,o1,e1) *h2/g
                        = (h1*h2/g, o1*h2/g, h2e1)
                    (h2,o2,e2) *e1/g
                        = (h2e1, o2*e1/g, e2*e1/g)
                let (a,b,c) := (o1*h2/g, o2*e1/g, e2*e1/g)

                [gcd({a,b,c})
                == gcd(o1*h2/g, gcd(o2*e1/g, e2*e1/g))
                == gcd(o1*h2/g, gcd(o2, e2)*e1/g)
                == gcd(o1*h2/g, 1*e1/g)
                <= gcd(o1, e1) * gcd(h2/g, e1/g)
                == 1
                ]
                [abc == h1*h2/g]
                [a%2==o1*h2/g %2 ==1]
                [b%2==o2*e1/g %2 == e1%2 ==0]
                [c%4==e2*e1/g %2 == e2*e1%4 ==0]
                [ab**2 == a**2 + b**2
                == (o1*h2/g)**2 + (o2*e1/g)**2
                ]
                let go := gcd(o1,o2)
                [gcd(o1*h2, o2*e1) = gcd(h2,e1)*gcd(o1,o2) = g*go]
                要求(_, o1*h2/g/go, o2*e1/g/go)是 边长互素的整数三角形

                [ac**2 == a**2 + c**2
                == (o1*h2/g)**2 + (e2*e1/g)**2
                ]
                let ge := gcd(o1,e2)
                [gcd(o1*h2, e2*e1) = gcd(h2,e1)*gcd(o1,e2) = g*ge]
                要求(_, o1*h2/g/ge, e2*e1/g/ge)是 边长互素的整数三角形
                h1 = ??
                o1 = go*ge*??
                e1 = g*??
                h2 = g*??
                o2 = go*??
                e2 = ge*??



            ！错:例:
                (h1,o1,e1) := (5,3,4)
                (h2,o2,e2) := (5,3,4)
                g := gcd(h2,e1) = 1
                (a,b,c) := (o1*h2/g, o2*e1/g, e2*e1/g) = (15,12,16)
                (bc, ac, ab) = (20, ?, ?)
                    bug!!!

[[[
http://www.durangobill.com/IntegerBrick.html
===

The “Integer Brick” Problem
(The Euler Brick Problem)



Is it possible to construct a rectangular solid such that the dimensions of all sides
and all diagonals including the interior diagonal through the center are integers?

   This is an unsolved problem as no one has found an example, but no one has proved that a solution can’t exist. If a solution exists, its “odd” side is greater than 3.0 trillion (3.0E+12) - no restrictions on the other dimensions.

   The search has been terminated at 3.0 trillion as it is assumed that any additional search will still not find the “Jackalope”. http://en.wikipedia.org/wiki/Jackalope


Generalized
            picture of a rectangular solid with edges "width",
            "length", and "height"

   The diagram above illustrates a rectangular solid (a “brick”). The dimensions of the rectangular solid (the “brick”) are defined by its length, width, and height. Since the six sides of a rectangular solid are all rectangles, the size of any diagonal contained in any of these sides can be calculated using the Pythagorean Theorem.

   The Pythagorean Theorem states that the relationship between the two sides of a right triangle and its sloping third side (the hypotenuse) will obey the following equation.

(Side 1)2 + (Side 2)2 = Hypotenuse2
Where (Side 1)2 means:     (Side 1) times (Side 1)

Alternately this equation can be expressed as:

Hypotenuse = Sqrt[ (Side 1)2 + (Side 2)2]



   The following diagram illustrates how the Pythagorean Theorem can be used to calculate the external diagonals of a rectangular solid (our brick).

A rectangular solid where all edges
              and the external diagonals are integers

In the above diagram, we note the following dimensions:

Length = 720
Width = 132
Height = 85

These three dimensions are all integers. So far, there are no problems finding our “all integers” solution.

   We can use the Pythagorean Theorem to calculate the external diagonals involved since these diagonals are all equivalent to the hypotenuse of a right triangle.

For the outside surface at the left end we have:
Hypotenuse (the diagonal) = Sqrt(Heigth2 + Width2)
Using our example gives:
Diagonal = Sqrt(852 + 1322)
= 157

A similar calculation for the front, right surface yields:
Hypotenuse (the diagonal) = Sqrt(Height2 + Length2)
Diagonal = Sqrt( 852 + 7202)
= 725

And finally we can find the diagonal across the top surface:
Hypotenuse (the diagonal) = Sqrt(Width2 + Length2)
Diagonal = Sqrt(1322 + 7202)
= 732

   So far, we have integer length-width-height dimensions for the brick and all of its external diagonals. For most brick dimensions the external diagonals will not be integers. However, an infinite number of “bricks” exist that do have integer external diagonals. Some examples include:

Height   Width    Length
85        132       720
117        44       240
231       160       792
275       240       252
351       132       720
693       140       480
825       720       756

The above table includes “primitive”  solutions (one side is odd) and “odd” multiples of primitive solutions where all 3 sides are < 1000.

As an exercise in using the Pythagorean Theorem, you may want to use these combinations to verify that they all have integer external diagonals.



   The internal diagonal that runs from any given corner through the center of the rectangular solid and terminates at the far corner can also be calculated using the Pythagorean Theorem. One combination for the two sides to this triangle would be “height” and “top-surface diagonal”. In our example we would use the height of 85 and the top surface diagonal which we previously calculated and found to be 732. (Note: Other dimension/diagonal combinations are also valid. Alternately, you could calculate the size of the center diagonal using:
Center Diagonal = Sqrt( Height2 + Width2 + Length2)

The calculation here would be:
Hypotenuse (center diagonal) = Sqrt(Height2 + Top-surface-diagonal2)
Center Diagonal = Sqrt (852 + 7322)
Note that Sqrt(852 + 1322 + 7202) will produce the same result.

   Unfortunately this ends up equaling 736.91858+ which is not an integer. It starts getting worse as none of the other integer dimension examples (shown above) work either. In fact there is no known combination of dimensions that work. On the other hand, no one has proved that there are no solution combinations. Thus it is an unsolved problem in mathematics.


Using a Computer Program to try to find a Solution

   If you could find a dimension combination such that all diagonals are integers, including the central diagonal, the world might reward you with fame, gifts, money, etc. for solving the unsolved problem. (This might be a “slight exaggeration”, but at least your name would be recorded as “the solver”). In this pursuit you might try writing a computer program to try a large number of combinations to see if a solution could be found. A possible algorithm might be:

For (Length equals 1 to billions - or more)      //  Try a bunch of possible lengths
   For (Width equals 1 to billions – or more)    //  Same for width
      For (Height equals 1 to billions, etc)     //  Hey, just do more of the same
             Do all the length2, height2, width2, Sqrt() calculations
             reviewed previously to see if anything works.
      Repeat this loop for a whole bunch of possible “heights”
   Repeat this loop for a whole bunch of possible “widths”
Repeat for a whole bunch of possible “lengths”

   Technically, if a solution exists, this algorithm would find it. In reality, the number of calculations required is mind boggling. You and the universe will die of old age before your search gets very far.

   The search speed of the above algorithm can be substantially improved by taking the first test for an integer diagonal from inside the innermost loop and placing it inside the second loop. At 1.0E12 (and above) this improvement will increase the running speed of a computer program by a factor of billions. The result might look like the following:


                                                               //  Note: Length > Width > Height
                                                               //  For all possible lengths
for (Length = StartLength; Length; Length += 1.0) {            //  Length will increment forever
  for (Width = Length - 1.0; Width > 1.0; Width -= 1.0) {      //  For all possible widths down to 2
    Diagonal = hypot(Length, Width);                           //  Get the hypotenuse for side 1
    if (Diagonal != floord(Diagonal))                          //  If it's not an integer,
      continue;                                                //  then skip the inner calcs
                                                               //  Else, for all possible heights
    for (Height = Width - 1.0; Height > 0.0; Height -= 1.0) {  //  down to 1
      Diagonal = hypot(Length, Height);                        //  Get the hypotenuse for side 2
      if (Diagonal != floord(Diagonal))                        //  If it's not an integer, then
        continue;                                              //  skip to the end of the loop.
      Diagonal = hypot(Width, Height);                         //  Get the hypotenuse for side 3
      if (Diagonal != floord(Diagonal))                        //  If it's not an integer, then
        continue;                                              //  skip to the end of the loop.
                                                               //  If to here, then found an
                                                               //  external solution.
      SolCount++;
      printf("\nExternal solution Nbr %'d\n", SolCount);
      printf("Length = %'.0f  Width = %'.0f  Height = %'.0f\n",
          Length, Width, Height);
                                                               //  Check for an internal solution
      Diagonal = hypot(Diagonal, Length);                      //  Get the internal diagonal
      if (Diagonal == floord(Diagonal))                        //  If it's an integer,
        puts("The above is a complete solution");
    }                                                          //  End of "Height" loop
  }                                                            //  End of "Width" loop
}                                                              //  End of "Length" loop
 

   While the above (part of an actual computer program) improves upon the original algorithm by a factor of billions (at 1.0E12 and above), the algorithm given below is billions of times faster yet. (At 1.0E12 and above as measured by time trials.)

If you are going to run a serious search, you should use the best algorithm that is available.
 


Designing a better algorithm

   Since you are going to let a computer program try to find a solution, you should at least give it a good set of rules to work with. You still might not find a solution, but you can greatly increase the search area for the dimensions of “the brick”.

   In the inefficient algorithms given above, we just tried “a whole bunch of numbers” and then applied the calculations of the Pythagorean Theorem to see if the diagonals were integers. It is much faster to use algebraic expressions derived from the Pythagorean Theorem to directly generate right triangles where the hypotenuse is also an integer.

   First, we note that all the “brick” examples given earlier had one dimension that was “odd”, while the other two dimensions were “even”. If a solution exists for the integer brick problem, then either this solution is a “primitive” solution, or it is a multiple of a primitive solution. If a primitive solution exists, exactly one of its dimensions will be “odd” while the other two dimensions will be “even”. (If all three dimensions were even, then everything could be repeatedly divided by 2 until one of the dimensions became odd. There can’t be two sides that are “odd” as the “Y” side of an integer Pythagorean Triangle must be even. See calculations below.)

   If we represent the sides of a right triangle by the variables “X”, “Y”, and “Z” (where “Z” is the hypotenuse), then right, integer triangles can be generated using the following equations:
X = (P2 – Q2)K        (We will let “X” = an odd number. Alternately:  X = (P-Q)(P+Q)K)
Y = 2PQK                      (Since either P or Q must be even, Y is always divisible by 4)
Z = (P2 + Q2)K          (We won’t use this equation in the actual computer algorithm)
P, Q, and K can be any integers (also perform multiplications for adjacent letters P, Q, K)

For example, if we let P = 2, Q = 1, and K = 1, then we get X = 3, Y = 4, and Z = 5. This is the smallest possible integer right triangle.

   We note that the “X” term above has three components: (P-Q), (P+Q), and K. If we are going to generate “odd” numbers for our trial bricks, then each of these components must be odd. For example, if we want to generate a trial brick where the odd side is equal to 85, then the 85 is separated into three components whose product equals 85. Here, the only two possibilities are 1 times 5 times 17 and 1 times 1 times 85. (These triplets can be in any order.) We will use these triplets to solve for “P”, “Q”, and “K”. In turn, we will use the results to generate the 85, 132, 720 example given earlier that “almost” solves the integer brick problem.

   In the multiplication of 1 x 5 x 17 = 85, the 1, 5, and 17 factors can be in an order. However, the terms (P-Q)(P+Q)K require (P+Q) to be larger than (P-Q). Thus, for our multiplication, we only use permutations where the second term is larger than the first. We now have:
1 x 5 x 17 = 85
1 x 17 x 5 = 85
5 x 17 x 1 = 85

Each of these can be solved to get a “P”, “Q”, “K” triplet

If we let (P-Q) = 1 and (P+Q) = 5, then we get P = 3, Q = 2, and K = 17
Substituting these in Y = 2PQK yields Y = 204   (In practice, this result won’t be useful)

If we let (P-Q) = 1 and (P+Q) = 17, then we get P = 9, Q = 8, and K = 5
Substituting these in Y = 2PQK yields Y = 720  (One of the sides in our brick)

Finally, if we let (P-Q) = 5 and (P+Q) = 17, then we get P = 11 , Q = 6, and K = 1
Substituting these in Y = 2PQK yields Y = 132  (The other side that we used in the brick)

The only other valid multiplication is:
1 x 85 x 1 = 85

If we let (P-Q) = 1 and (P+Q) = 85, then we get P = 43, Q = 42, and K = 1
Substituting these in Y = 2PQK yields Y = 3612.

Thus we have found the four right triangles that can have one side equal to 85. The other side can equal 132, 204, 720, or 3612. (These are the only four. There are no others.)

   These four results are then tried in various combinations for trial sides of the integer brick. You can reduce the trial combinations a great deal further by observing that if a solution exists, the “top-surface” diagonal would be one of the members of the above trial list.

   In the above example, there are only 4 divisors of 85 (1, 5, 17, and 85). For other odd “X” sides, there may be many possible triplets. (e.g. If the odd number is a product of many small odd prime numbers.) Our more efficient algorithm thus becomes:

For “odd side” equals 3, 5, 7, etc.
  Generate all possible triplets that can be multiplied to produce the odd number
  For each valid permutation, solve for P, Q, K and the second side of a right triangle
    Make a list of all of these trial “Side 2’s”
  Search the list to see if any combination yields a solution
Repeat the above for the next odd number.

   Finally, we have not mentioned an efficient way to find the “triplet” trial divisors. You could of course try dividing the “odd side” by 3, 5, 7, etc. up to Sqrt(odd number). This is not efficient.

   A much faster way of finding trial divisors for the “triplets” can be found using a “sieve” algorithm. In the table below, note where the “1’s” show up.

Trial       < - - - - Trial “Odd Numbers” - - - - >
Divs.  3  5  7  9 11 13 15 17 19 21 23 25 27 29 31 33 35 . . . 85 . . .
       - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  1    1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1        1
  3    1  0  0  1  0  0  1  0  0  1  0  0  1  0  0  1  0        0
  5    0  1  0  0  0  0  1  0  0  0  0  1  0  0  0  0  1        1
  7    0  0  1  0  0  0  0  0  0  1  0  0  0  0  0  0  1        0
  9    0  0  0  1  0  0  0  0  0  0  0  0  1  0  0  0  0        0
 11    0  0  0  0  1  0  0  0  0  0  0  0  0  0  0  1  0        0
 13    0  0  0  0  0  1  0  0  0  0  0  0  0  0  0  0  0        0
 15    0  0  0  0  0  0  1  0  0  0  0  0  0  0  0  0  0        0
 17    0  0  0  0  0  0  0  1  0  0  0  0  0  0  0  0  0        1
  .
  .
 85    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0        1
Etc.

   The top row lists the trial odd numbers that will be used for the odd side of the brick. The left edge lists all odd numbers which potentially might be evenly divisible into the trial odd number.

   All possible trial numbers are divisible by 1. We know that 3 can be divided by 3. Then we simply go three columns to the right of this number to find another trial odd number that is also divisible by 3. We can continue going right 3 columns at a time as far as needed.

   A similar process works for Trial Divisor = 5. We just mark a “1” in every 5th column. The process can be extended for as many rows as needed. If you use this “sieve” method to find trial divisors, all you have to do is start a list for each column. Then process each row by adding a new divisor to the appropriate list each time a “1” would be encountered. (For computer science students, think “Link List”). Periodically, a large block of the table can be generated which will generate lists for large numbers of trial “Odd Numbers”.

   In the program, a block for these divisor lists is 100,000 columns wide. (Trial “Odd Numbers” increase by 200,000 per block.) With Trial “Odd Numbers” in the 1.0E11 to 1.0E12 range, on average there are near to slightly over 6 divisors per column. Thus the program generates about (to a little over) 600,000 nodes in the divisor lists per block.


Exploring the Great Unknown - The (Non) Results

   The author wrote a computer program based on the algorithm outlined above. (Actually, a couple of different versions were used.) Initially, all odd numbers out to 21 billion were tried on a Pentium 4 computer. Subsequently, a Skulltrail computer was used to extend the search out to 3.0 trillion. (3.0E+12). All versions of the program were written in “C” and used the lcc-win32 C compiler system. (http://www.cs.virginia.edu/~lcc-win32/)

   It should be noted that if the odd side of a right triangle is represented by the variable “X”, then the even side can be as large as (X2 -1)/2. Thus, if the odd side is 1.0E+12, the even side can be as large as 5.0E+23. This has more digits than the precision that exists on Intel processors. Then of course these numbers have to be squared for the X2 + Y2 calculations. Thus, the computer program has to keep track of the extra precision.

   No solutions were found.

   The best chance of finding a possible solution would appear to occur when the “odd side” of the brick is a product of many small factors. For example, at “odd side” = 9,704,539,845 (3x3x5x7x11x13x17x19x23x29) the program generated 16,402 right triangles that shared the same common odd edge. Even with this many candidates for the other dimensions of the brick, there were no combinations that produced a solution.

   The possibility exists that the computer program is faulty, and a solution actually exists somewhere in the search range. Viewers are encouraged to launch their own search efforts in case a solution actually exists.




External Solutions

   An external solution consists of integer edges and integer external diagonals. One version of the program generated a disk file that contained all the external solutions with the 3 sides <= 1,000,000,000 with one side “odd”.

   There were 4,631 of these which were subsequently read into a spreadsheet so that they could be “played with”. Click here if you would like to view/copy this list.

   Various experiments were tried using Greatest Common Divisor, Mod 2 arithmetic, Mod 3 arithmetic, etc. (e.g. The product of the 3 dimensions is always divisible by 95,040.) No reliable pattern was recognized that would prevent a solution that would also include an integer internal diagonal.

   The 7 external solutions with all 3 dimensions under 1,000 were given earlier. However, only 5 of these are primitive. (A primitive solution has no common divisor for the 3 edges.)

   The following table shows the number of primitive external solutions where the 3 sides are no larger than the Dimension Limit.

                                Number of
         Dimension              Primitive
           Limit                Solutions
             1,000                      5
            10,000                     19
           100,000                     65
         1,000,000                    242
        10,000,000                    704
       100,000,000                  1,884
     1,000,000,000                  4,631
    10,000,000,000                 10,943
   100,000,000,000                 43,106


External solutions come in all shapes and sizes.

For example, there are long flat solutions:
                   X                       Y                             Z
              74,745           23,085,952              186,227,160

Nearly cubical solutions:
              X                          Y                               Z
     110,562,771         108,192,528              109,141,700

Multiple solutions for a given height:
                   X                          Y                                 Z
               1,155                    1,008                          1,100
               1,155                    6,688                          6,300


Source Code

   If anyone would like to view/use the “C” source code for the program, it is available here ( http://www.durangobill.com/IntBrickSourceCode.html ) It should compile “as is” using the lcc win32 “C” compiler. If you have any questions please feel free to ask. (My E-mail address is on my home page) If you publish any results that use the program (or derivatives thereof), I would appreciate an acknowledgement that I supplied the original code/algorithm.

  If you compile and run the program, you will get a lot of output in the first few seconds. This will include a lot of status information. If you start the search at 0, this will also include external solutions with the odd side of the brick < 5000. However, things will quickly quiet down to just periodic status information after the first few seconds. (About as exciting as watching grass grow.)

   If you find an error/bug in the program, please let me know so I can fix it and try again. (I’m pretty sure the program is OK, but there’s no 100% guarantee on these things.)





For additional information about the Euler Brick Problem please see:
Eric Weisstein’s "Perfect Cuboid"  web page:      http://mathworld.wolfram.com/PerfectCuboid.html
and
Fred Curtis’s "Primitive Euler Bricks"  web page:     http://f2.org/maths/peb.html


Return to Durango Bill's Home Page


]]]






https://baike.baidu.com/item/%E6%95%B4%E6%95%B0%E4%B8%89%E8%A7%92%E5%BD%A2/10329454
整数三角形
整数三角形是指三边长和面积都是整数的三角形。
举例说明
例如：边长分别为3，4，5的直角三角形，其面积是6，是一个整数三角形。
整数三角形可以为直角三角形。可以为锐角三角形亦可以为钝角三角形。但不能为等边三角形。
直角三角形如3.4.5 5.12.13
锐角三角形如5.5.6
等腰三角形如3.4.4
钝角三角形如2.4.5 3.13.20

Pythagorean triangle
If all three sides of a right triangle have lengths that are integers, it is known as a Pythagorean triangle. In a triangle of this type, the lengths of the three sides are collectively known as a Pythagorean triple. Examples include: 3, 4, 5; 5, 12, 13; 8, 15, 17, etc.


Integer Triangle
An integer triangle or integral triangle is a triangle all of whose sides have lengths that are integers. A rational triangle can be defined as one having all sides with rational length; any such rational triangle can be integrally rescaled (can have all sides multiplied by the same integer, namely a common multiple of their denominators) to obtain an integer triangle, so there is no substantive difference between integer triangles and rational triangles in this sense. However, other definitions of the term "rational triangle" also exist: In 1914 Carmichael used the term in the sense that we today use the term Heronian triangle; Somos uses it to refer to triangles whose ratios of sides are rational; Conway and Guy define a rational triangle as one with rational sides and rational angles measured in degrees—in which case the only rational triangle is the rational-sided equilateral triangle.




]]]]]







iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_lt(100)
result of lt N=100:[
(5, 3, 4)
(13, 5, 12)
(17, 15, 8)
(25, 7, 24)
(29, 21, 20)
(37, 35, 12)
(41, 9, 40)
(53, 45, 28)
(61, 11, 60)
(65, 33, 56)
(65, 63, 16)
(73, 55, 48)
(85, 77, 36)
(85, 13, 84)
(89, 39, 80)
(97, 65, 72)
]
===
(65, 33, 56)
(65, 63, 16)
... ...
(85, 77, 36)
(85, 13, 84)
    ==>> not sorted
===


    #]]]'''#'''
#def iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_eq(c, factorisation_of_c, /):
    assert type(to_sort) is bool
    assert type(SML_vs_HOE) is bool
    ######################
    if to_sort:
        ls = [*iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_eq(c, factorisation_of_c, SML_vs_HOE=SML_vs_HOE, to_sort=False, turnoff__coprime=turnoff__coprime)]
        _es = [e for p,e in factorisation_of_c.items() if p%4==1]
            # unsorted
        if turnoff__coprime:
            assert len(ls) == _total4iter_ess_(_es)
        else:
            assert len(ls) == 2**(len(_es)-1)

        if SML_vs_HOE is False:
            #SML
            key = None
                # sorted by LSM
                # !! [L eq]
                # sorted by S
                # sorted by SML
        elif SML_vs_HOE is True:
            #HOE
            key = None
                # sorted by HOE
                # !! [H eq]
                # sorted by O
        else:
            raise 000
        key
        ls.sort(key=key)
        return iter(ls)
        #yield from ls
        return
    ######################
    if SML_vs_HOE is False:
        #SML
        def _outfmt5Lxy(L, x, y, /):
            (short_side,middle_side) = (x,y) if x < y else (y,x)
            SML = (short_side, middle_side, L)
            return SML
    elif SML_vs_HOE is True:
        #HOE
        def _outfmt5Lxy(L, x, y, /):
            # (odd,even) = (x,y) if x&1 == 1 else (y,x)
                #bug:@[turnoff__coprime==True]
            # [g := c2_43*II(p41**e4both<p41> for p41 in factorisation_of_c)]
            # [x == odd*g]
            # [y == even*g]
            assert y%2 == 0
            #(odd,even) = (x,y)
                # [odd MAYBE even] if [turnoff__coprime==True]
            (gcdXodd,gcdXeven) = (x,y)
            HOE = (L, gcdXodd, gcdXeven)
            return HOE
    else:
        raise 000
    _outfmt5Lxy
    ######################
    if not c >= 5: raise ValueError
    if not turnoff__coprime:
        if not c%4==1: raise ValueError
        if not all(p >= 5 for p in factorisation_of_c): raise ValueError
        if not all(p%4==1 for p in factorisation_of_c): raise ValueError
    else:
        if not all(p >= 2 for p in factorisation_of_c): raise ValueError
        if not all(p%2==1 or p==2 for p in factorisation_of_c): raise ValueError
    #
    if not any(p%4==1 for p in factorisation_of_c): raise ValueError
    if not all(e>=1 for e in factorisation_of_c.values()): raise ValueError
    if not c == II(p**e for p,e in factorisation_of_c.items()): raise ValueError


    if not turnoff__coprime:
        p2e = factorisation_of_c
        c41 = c
        c2_43 = 1
    else:
        p2e = {p:e for p,e in factorisation_of_c.items() if p%4==1}
        c41 = II(p**e for p,e in p2e.items())
        c2_43 = c//c41
    factorisation_of_c = None

    p2xy = {p:find_Gauss_integer_factor_coeffs_of_4k1_prime(p, None) for p in p2e}
    ps = sorted(p2e)
    if turnoff__coprime:
        f = _on___turnoff__coprime
    else:
        f = _on___not_turnoff__coprime
    return f(_outfmt5Lxy, c, p2e, p2xy, ps, c2_43)
#end-def iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_eq(c, factorisation_of_c, /, *, SML_vs_HOE, to_sort, turnoff__coprime):
def _on___turnoff__coprime(_outfmt5Lxy, c, p2e, p2xy, ps, c2_43, /):
    es = [p2e[p] for p in ps]
    j2xy = [p2xy[p] for p in ps]
    one = (1,0)
    #j2e2pow4xy4p = [*iterate(curry1(mul__Gauss_integer, xy), one, 1+2*e4p) for p, xy, e4p in zip(ps, j2xy, es)]
    j2e2pow4xy4p = [[*iterate(curry1(mul__Gauss_integer, square__Gauss_integer(xy)), one, 1+e4p)] for p, xy, e4p in zip(ps, j2xy, es)]
    j2e2pow4p = [[*iterate(p.__mul__, 1, 1+e4p)] for p, xy, e4p in zip(ps, j2xy, es)]

    def _iter_xy_pows5es4xy(es4xy, /):
        for p, xy, e4p, e4xy, e2pow4p, e2pow4xy4p in zip(ps, j2xy, es, es4xy, j2e2pow4p, j2e2pow4xy4p):
            # (odd,even) = xy
            # [p == odd**2 +even**2]
            # [0 <= e4xy < 1+2*e4p]
            assert 0 <= e4xy < 1+2*e4p
            e4xy
            e4conj = 2*e4p -e4xy
            # [0 <= e4xy <= 2*e4p]
            # [e4xy +e4conj == 2*e4p]
            # [(e4xy +e4conj)%2 == 0]
            # [e4xy%2 == e4conj%2]
            #
            e4both = min(e4xy, e4conj)
            # [e4both%2 == e4xy%2 == e4conj%2]
            # [0 <= e4both <= e4p]
            e4xy -= e4both
            e4conj -= e4both
            # [0 == min(e4xy, e4conj)]
            # [0 == e4xy%2 == e4conj%2]
            # [e4xy +e4conj == 2*e4p -2*e4both <= 2*e4p]
            # [0 <= e4xy <= 2*e4p-e4both <= 2*e4p]
            #
            e4xy //= 2
            e4conj //= 2
            # [0 <= e4xy <= e4p]

            pow4p = e2pow4p[e4both]
            pow4xy4p = e2pow4xy4p[e4xy]
            pow4even4p = conj__Gauss_integer(e2pow4xy4p[e4conj])
            yield (pow4p,0) # real +1j*imag
            yield pow4xy4p
            yield pow4even4p
    for es4xy in _iter_ess_(es):
        a,b = II(_iter_xy_pows5es4xy(es4xy), one=one, mul=mul__Gauss_integer)
        a = abs(a)
        b = abs(b)
        a *= c2_43
        b *= c2_43
        yield _outfmt5Lxy(c,a,b)
    return
def _on___not_turnoff__coprime(_outfmt5Lxy, c, p2e, p2xy, ps, c2_43, /):
    # p2component = {p: pow__Gauss_integer(p2xy[p], p2e[p]) for p in p2e}
        #bug:miss"2" c->c**2
    p2component = {p: pow__Gauss_integer(p2xy[p], 2*p2e[p]) for p in p2e}
    components = [p2component[p] for p in ps]
    L = len(ps)
    assert L > 0
    for i in range(2**(L-1), 2**L):
        s = uint2str_bits(i)
        assert len(s)==L
        assert s[0] == '1'
        it = (component if ch == '1' else conj__Gauss_integer(component) for ch, component in zip(s, components))
        a,b = II(it, one=(1,0), mul=mul__Gauss_integer)
        if 1: #bug: a,b < 0
            a = abs(a)
            b = abs(b)
        if 1:
            # [:why_use_form_1odd_1jeven]:goto
            #(odd, even) = (a,b) if a%2==1 else (b,a)
            (odd, even) = (a,b)
        assert odd%2==1
        assert even%2==0
        assert odd > 0, (c, odd, even)
        assert even > 0
        assert odd**2 + even**2 == c**2, (c, odd, even, odd**2, even**2, odd**2 + even**2, c**2)
        assert gcd(even, odd) ==1
        #yield (c, odd, even)
        yield _outfmt5Lxy(c,a,b)
    return

def _total4iter_ess_(es, /):
    es = tuple(es)
    assert all(e >= 1 for e in es)
    return (II(1+2*e for e in es) -1)//2
def _iter_ess_(es, /):
    '[total == ((II (1+2*e4p) {(p,e4p) :<- factorisation_of_c.items() | [p%4==1]} -1)///2)]'
    es = tuple(es)
    assert all(e >= 1 for e in es)
    j2end = [1+2*e for e in es]
    L = len(j2end)
    j2e = [0]*L
        # [?[j :<- [0..<L]] -> [[j2e[:j] == es[:j]][j2e[j] =!= es[j]]]]
        #   anti-symmetry
        #   floor_half
    j2all_prev_eq_ej = [False]*(L+1)
        # <<== all(es)
    j2all_prev_eq_ej[0] = True
        # [j2prev_eq_ej[j] == (j2e[:j] == es[:j])]
        # [j2prev_eq_ej[0] == True]

    # [L >= 0]
    if not L: return
    j = L
        # [-1 <= j <= L]
        # [j2e[j+1:] == [0]*(L-(j+1))]
        # [j2all_prev_eq_ej[j+2:] == [False]*(L-(j+2))]
    while not j == -1:
        # [0 <= j <= L]
        # [j2e[j+1:] == [0]*(L-(j+1))]
        # [j2all_prev_eq_ej[j+2:] == [False]*(L-(j+2))]
        #
        # target:to inc j2e[j]
        #
        if j == L:
            if j2all_prev_eq_ej[j]:
                break
            yield tuple(j2e)
            j -= 1
            # [-1 <= j == L-1 < L]
            # [j2e[j+1:] == [] == [0]*(L-(j+1))]
            # [j2all_prev_eq_ej[j+2:] == [] == [False]*(L-(j+2))]
            continue
        # [0 <= j < L]
        # [0 <= j2e[j] < j2end[j]]
        # [j2e[j+1:] == [0]*(L-(j+1))]
        # [j2all_prev_eq_ej[j+2:] == [False]*(L-(j+2))]
        if j2all_prev_eq_ej[j] and j2e[j] == es[j]:
            # [j2e[j+1:] == [0]*(L-(j+1))]
            # [j2all_prev_eq_ej[j+2:] == [False]*(L-(j+2))]
            j2e[j] = 0
            j2all_prev_eq_ej[j+1] = False # (j2all_prev_eq_ej[j] and j2e[j] == es[j]) # <<== all(es)
            # [j2e[j:] == [0]*(L-j)]
            # [j2all_prev_eq_ej[j+1:] == [False]*(L-(j+1))]
            j -= 1
            # [-1 <= j < L-1 < L]
            # [j2e[j+1:] == [0]*(L-(j+1))]
            # [j2all_prev_eq_ej[j+2:] == [False]*(L-(j+2))]
            continue
        j2e[j] += 1
        j2all_prev_eq_ej[j+1] = (j2all_prev_eq_ej[j] and j2e[j] == es[j])
        # [1 <= j2e[j] <= j2end[j]]
        # [j2e[j+1:] == [0]*(L-(j+1))]
        # [j2all_prev_eq_ej[j+2:] == [False]*(L-(j+2))]
        if j2e[j] == j2end[j]:
            # [j2e[j+1:] == [0]*(L-(j+1))]
            # [j2all_prev_eq_ej[j+2:] == [False]*(L-(j+2))]
            j2e[j] = 0
            j2all_prev_eq_ej[j+1] = False # (j2all_prev_eq_ej[j] and j2e[j] == es[j]) # <<== all(es)
            # [j2e[j:] == [0]*(L-j)]
            # [j2all_prev_eq_ej[j+1:] == [False]*(L-(j+1))]
            j -= 1
            # [-1 <= j < L-1 < L]
            # [j2e[j+1:] == [0]*(L-(j+1))]
            # [j2all_prev_eq_ej[j+2:] == [False]*(L-(j+2))]
            continue
        # [1 <= j2e[j] < j2end[j]]
        # [j2e[j+1:] == [0]*(L-(j+1))]
        # [j2all_prev_eq_ej[j+2:] == [False]*(L-(j+2))]
        j = L
            # to yield...
        # [1 <= j <= L]
        # [-1 <= j <= L]
    else:
        # [j==-1] is impossible since 『break』
        raise 000
    return
def _test4iter_ess_():
    assert all(len([*_iter_ess_(es := range(1,L))]) == _total4iter_ess_(es) for L in range(4))
    assert all((ess := [*_iter_ess_(es := range(1,L))]) == sorted(ess) for L in range(4))
    assert [*_iter_ess_([])] == []
    assert [*_iter_ess_([1])] == [(0,)]
    assert [*_iter_ess_([2])] == [(0,), (1,)]
    assert [*_iter_ess_([1,2])] == [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1)]
    assert [*_iter_ess_([1,2,3])] == (
    [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 0, 3), (0, 0, 4), (0, 0, 5), (0, 0, 6)
    , (0, 1, 0), (0, 1, 1), (0, 1, 2), (0, 1, 3), (0, 1, 4), (0, 1, 5), (0, 1, 6)
    , (0, 2, 0), (0, 2, 1), (0, 2, 2), (0, 2, 3), (0, 2, 4), (0, 2, 5), (0, 2, 6)
    , (0, 3, 0), (0, 3, 1), (0, 3, 2), (0, 3, 3), (0, 3, 4), (0, 3, 5), (0, 3, 6)
    , (0, 4, 0), (0, 4, 1), (0, 4, 2), (0, 4, 3), (0, 4, 4), (0, 4, 5), (0, 4, 6)
    , (1, 0, 0), (1, 0, 1), (1, 0, 2), (1, 0, 3), (1, 0, 4), (1, 0, 5), (1, 0, 6)
    , (1, 1, 0), (1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 1, 4), (1, 1, 5), (1, 1, 6)
    , (1, 2, 0), (1, 2, 1), (1, 2, 2)
    ])
if 1:
    _test4iter_ess_()

#end2-def iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_eq(c, factorisation_of_c, /, *, SML_vs_HOE, to_sort, turnoff__coprime):


def iter_len_hypotenuse_of_right_angled_triangles_with_coprime_side_length__with_factorisation__lt(may_max1_hypotenuse, /, *, turnoff__coprime):
    '-> Iter (c, factorisation_of_c)'
    if may_max1_hypotenuse is None:
        from seed.math.prime_gens import all_prime_factors_gen
        from seed.math.semi_factor_pint_via_trial_division import semi_factor_pint_via_trial_division
        #all_prime_factors_gen.get_or_mk_lazy_seq_()
        for u, may_prime_factors4u in enumerate(all_prime_factors_gen, 0):
            #if u < 2: continue
            if u < 5: continue
            prime_factors4u = may_prime_factors4u
            (p2e, _1) = semi_factor_pint_via_trial_division(prime_factors4u, u)
            assert _1 == 1
            if not turnoff__coprime:
                if u%4 == 1 and all(p%4==1 for p in p2e):
                    yield u, p2e
            else:
                if any(p%4==1 for p in p2e):
                    yield u, p2e
        return

    ######################
    from nn_ns.math_nn.numbers.min_factor import factor_uint__via_min_factor_list #, min_factor

    assert not may_max1_hypotenuse is None
    N = max1_hypotenuse = may_max1_hypotenuse
    N = max(2, N)
    factor_uint__via_min_factor_list(N)
        #force cache
    if not turnoff__coprime:
        #for u in range(5, N, 2):
        for u in range(5, N, 4):
            p2e = factor_uint__via_min_factor_list(u)
            if all(p%4==1 for p in p2e):
                yield u, p2e
    else:
        for u in range(5, N):
            p2e = factor_uint__via_min_factor_list(u)
            if any(p%4==1 for p in p2e):
                yield u, p2e
def iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_lt(may_max1_hypotenuse, /, *, SML_vs_HOE, to_sort, turnoff__coprime):
    assert type(to_sort) is bool
    assert type(SML_vs_HOE) is bool
    ######################
    for c, p2e in iter_len_hypotenuse_of_right_angled_triangles_with_coprime_side_length__with_factorisation__lt(may_max1_hypotenuse, turnoff__coprime=turnoff__coprime):
        yield from iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_eq(c, p2e, SML_vs_HOE=SML_vs_HOE, to_sort=to_sort, turnoff__coprime=turnoff__coprime)











def iter_Gauss_integer_factor_coeffs_of_4k1_prime__ge_lt(may_begin, may_end, /, *, turnon__is_prime__le_pow2_64):
    for p in iter_4k1_primes__ge_lt(may_begin, may_end, turnon__is_prime__le_pow2_64=turnon__is_prime__le_pow2_64):
        (odd, even) = find_Gauss_integer_factor_coeffs_of_4k1_prime(p, None)
        yield (p, odd, even)
def iter_4k1_primes__ge_lt(may_begin, may_end, /, *, turnon__is_prime__le_pow2_64):
    if may_begin is None:
        begin = -1
    else:
        begin = may_begin
    begin = max(5, begin)
    begin = (begin +2)//4 *4 +1

    if not begin >= 5: raise logic-err
    if not begin&3 == 1: raise logic-err
    if may_end is None:
        it = count(begin, 4)
    else:
        end = may_end
        it = iter(range(begin, end, 4))

    if turnon__is_prime__le_pow2_64:
        #using is_prime__le_pow2_64
        for u in it:
            if is_prime__le_pow2_64(u):
                yield u
    else:
        #using factor_uint__via_min_factor_list
        from nn_ns.math_nn.numbers.min_factor import factor_uint__via_min_factor_list #, min_factor

        if may_end is None:
            N0 = 2*begin
        else:
            N0 = may_end
        factor_uint__via_min_factor_list(N0)
            #force cache

        for u in it:
            p2e = factor_uint__via_min_factor_list(u)
            if len(p2e)==1 and p2e=={u:1}:
                #and all(e==1 and p%4==1 for p,e in p2e.items()):
                yield u


from seed.math.GaussInteger import iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_lt

from seed.math.GaussInteger import is_zero__Gauss_integer, neg__Gauss_integer, conj__Gauss_integer, square_len__Gauss_integer, cmp_len__Gauss_integer, cmp_square_len_ex__Gauss_integer, mul__Gauss_integer, add__Gauss_integer, sub__Gauss_integer, divmod__Gauss_integer, gcd__Gauss_integer, square_len__Gauss_integer, pow__Gauss_integer
from seed.math.GaussInteger import find_Gauss_integer_factor_coeffs_of_4k1_prime, find_sqrt_neg1_of_4k1_prime_ex, find_sqrt_neg1_of_4k1_prime, iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_eq, iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_lt, iter_len_hypotenuse_of_right_angled_triangles_with_coprime_side_length__with_factorisation__lt
from seed.math.GaussInteger import iter_Gauss_integer_factor_coeffs_of_4k1_prime__ge_lt, iter_4k1_primes__ge_lt

from seed.math.GaussInteger import *

