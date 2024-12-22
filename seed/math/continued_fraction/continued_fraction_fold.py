#__all__:goto
r'''[[[
e ../../python3_src/seed/math/continued_fraction/continued_fraction_fold.py
    view ../../python3_src/nn_ns/math_nn/continued_fraction/continued_fraction.py
    view ../../python3_src/seed/math/continued_fraction/continued_fraction_fold.py
    view ../../python3_src/seed/math/continued_fraction/continued_fraction_of_log_.py
    view others/数学/continued-fraction/充要条件冫错开囜位纟分子分母序列纟渐近分数纟连分数.txt

seed.math.continued_fraction.continued_fraction_fold
py -m nn_ns.app.debug_cmd   seed.math.continued_fraction.continued_fraction_fold -x
py -m nn_ns.app.doctest_cmd seed.math.continued_fraction.continued_fraction_fold:__doc__ -ff -v
py_adhoc_call   seed.math.continued_fraction.continued_fraction_fold   @_test____mk_gcd_certification_ =100

[cf([]) === +oo]
[cf([x]) === x]
[cf([+oo]) === +oo]
[cf([x;y]) === x+1/y]
[cf([x;+oo]) === x]
[cf([x;y,z]) === x+1/(y+1/z)]
[cf([x;y,+oo]) === x+1/y]
[cf(cf_digits) === cf(cf_digits++[+oo]*+oo)]

[[[
===

,interpolated
:以内插值替换的
interpolation插值
interpolating function插值函数
interpolation polynomial插值多项式
interpolation formula插值公式
interpolation method插值法
approximation 近似值

[整数部分 <= 0]???如何处理？
连分数{>=1} 小数部分:
    两个数之间 插值
        [x 是 原数]
        [z 是 尾部连分数]
        [x = (a0+1/(a1+...+1/(aj+1/z)))]
    前数 位于无穷远处   [1/z==+oo][z==0]
    当前数 位于0        [1/z==0][z==0]
    prev = prevN/prevD
    curr = currN/currD
        #N:numerator
        #D:denominator
    插值(1/z) = (prevN*1/z+currN)/(prevD*1/z+currD)
    插值(1/z) = (prevN+currN*z)/(prevD+currD*z)
    起始配置<小数部分>:
        !! [x == (0+1*x)/(1+0*x)]
        prev=0/1 # == 0
        curr=1/0 # == +oo
    折叠部分，继续展开:
        #折叠部分后，配置为:
        [x == (prevN+currN*y)/(prevD+currD*y)]:
            #进一步展开y:
            [y=K+1/z]:
                [x
                == (prevN+currN*y)/(prevD+currD*y)
                == (prevN*z+currN*y*z)/(prevD*z+currD*y*z)
                == (prevN*z+currN*(z*K+1))/(prevD*z+currD*(z*K+1))
                == (currN+(prevN+currN*K)*z)/(currD+(prevD+currD*K)*z)
                let [prevN__new := currN]
                    [prevD__new := currD]
                    [currN__new := (prevN+currN*K)]
                    [currD__new := (prevD+currD*K)]
                == (prevN__new+currN__new*z)/(prevD__new+currD__new*z)
                ]

    折叠状态变换:
        输入: 下一个 连分数小数项 K <- [1..=+oo] # K可以取值+oo，但起始配置例外
        变换:
            [prevN__new := currN]
            [prevD__new := currD]
            [currN__new := (prevN+currN*K)]
            [currD__new := (prevD+currD*K)]
    定理:
    [cf[0] > 0]:
        # 假设 [整数项 是 正整数]
        注意:["*__new" 用于排除 起始配置]:
        [K > 0]
            !!连分数小数项要求 #除 整数项
        [prevN >= 0][prevD >= 0][currN >= 0][currD >= 0][prevN+currN > 0][prevD+currD > 0]
            !! 归纳法 由 起始配置+折叠状态变换
        [prevN__new > 0][prevD__new > 0][currN__new > 0][currD__new > 0]

        # [currN__new := (prevN+currN*K)]
        [currN__new >= currN == prevN__new]
            『>=』
        [currN__new__new > currN__new == prevN__new__new]
            『>』
        # 『*D』more『__new』required
        [currD__new__new >= currD__new == prevD__new__new]
            『>=』
        [currD__new__new__new > currD__new__new == prevD__new__new__new]
            『>』
        [K===1]:
            prev  curr  new1  new2  new3
            0     1     1     2     3
            1     0     1     1     2
        ==>>:
        [currN__new__new > currN == prevN__new]
        [currD__new__new > currD == prevD__new]

        [Ks===[a,b,c,d,...]]:
            [a :: int]
            [b,c,d,... :: pint]
                ??? if finite, [lastK >= 2]
                    std form [lastK >= 2]
                    but at continued-stepping or cut-off-cf-prefix, [lastK >= 1]
            #[initial_cf_table]:here
            prev  curr  new1  new2  new3
            0     1     a     1+a*b a+(1+a*b)*c==a+c+a*b*c
            1     0     1     b     1+b*c
            无需[分子反推公式@eq-new2]
            无需[分子反推公式@eq-new1]
            [a==0]:
            [a==-1]:
            [[currD=!=0] -> [cf0 == currN//currD]]
            [b==1]:
                # 1+a*b
                [1+(1+a*b)*(1+b*c) =?= a+c+a*b*c]
                    <==> [1+(1+a)*(1+c) =?= a+c+a*c]
                    <==> [1+(1+a+c+a*c) =?= a+c+a*c]
                    <==> [2 =?= 0]
            [[[prevD==1][currN==1+prevN*currD]] <-> [curr eq new2]]
            [[curr ge new1] -> [prevD==1] -> [[[prevN==cf0][curr eq new2]]or[[prevN==1+cf0][curr eq new3]]]]
            [[curr ge new1] -> [[(prevN,prevD)==(cf0,1)] <-> [curr eq new2]]]
        ==>>:
        [currN__new/currD__new__new 是 除法余数，模new2/模new3]
        [currN__new__new__new
        == (prevN__new__new+currN__new__new*K)
        == (currN__new+currN__new__new*K)
        ]

        !! [currN__new__new > currN__new == prevN__new__new]
        !! [currN__new__new__new == (currN__new+currN__new__new*K)]
        [currN__new == currN__new__new__new%currN__new__new]
        [K == currN__new__new__new//currN__new__new]
            # precondition:[cf0>0] => [分子反推公式@ge-new3]:here

        [currD__new__new__new__new
        == (prevD__new__new__new+currD__new__new__new*K)
        == (currD__new__new+currD__new__new__new*K)
        ]
        !! [currD__new__new__new > currD__new__new == prevD__new__new__new]
        !! [currD__new__new__new__new == (currD__new__new+currD__new__new__new*K)]
        [currD__new__new == currD__new__new__new__new%currD__new__new__new]
        [K == currD__new__new__new__new//currD__new__new__new]
            # [分母反推公式@ge-new4/@nrw3-if-b>=2]:here
]]]
[[[
连分数性质
===前置定义:
cf_digits :: [int; pint*]
st :: (prevN, prevD; currN, currD)
[st0 := (0,1; 1,0)]
steps_ :: (cf_digits; num_steps/uint) -> st
steps_(cf_digits; 0) := st0
steps_(cf_digits; num_steps) | [0 < num_steps <= len(cf_digits)] := (prevN__new, prevD__new, currN__new, currD__new) where:
    [(prevN, prevD; currN, currD) := steps_(cf_digits; num_steps-1)]
    [K := cf_digits[num_steps-1]]
    [prevN__new := currN]
    [prevD__new := currD]
    [currN__new := (prevN+currN*K)]
    [currD__new := (prevD+currD*K)]
steps_(cf_digits; num_steps) | [num_steps > len(cf_digits)] := error "undefined"

===连分数性质:
#[连分数渐近分数囗互素关联]:here
#   --> update:_check_args()
#   --> addnew:coprime_certification/gcd_certification
[@[cf_digits :: [int; pint*]] -> @[num_steps :<- [0..=len(cf_digits)]] -> [(prevN, prevD; currN, currD) := steps_(cf_digits; num_steps)] -> [currN*prevD -prevN*currD == (-1)**num_steps]]
    [[proof:
    !! [0 <= num_steps <= len(cf_digits)]
    * [num_steps == 0]:
        !! [st0 := (0,1; 1,0)]
        [(prevN, prevD; currN, currD) == (0,1; 1,0)]
        [lhs
        = currN*prevD -prevN*currD
        = 1*1 -0*0
        = 1
        = (-1)**0
        = (-1)**num_steps
        = rhs
        ]
    * [0 < num_steps <= len(cf_digits)][induction assume: [(prevN__old, prevD__old; currN__old, currD__old) := steps_(cf_digits; num_steps-1)][currN__old*prevD__old -prevN__old*currD__old == (-1)**(num_steps-1)]]:
        !! [(prevN, prevD; currN, currD) := steps_(cf_digits; num_steps)]
        !! [(prevN__old, prevD__old; currN__old, currD__old) := steps_(cf_digits; num_steps-1)]
        [K := cf_digits[num_steps-1]]
        [prevN == currN__old]
        [prevD == currD__old]
        [currN == (prevN__old+currN__old*K)]
        [currD == (prevD__old+currD__old*K)]
        [lhs
        = currN*prevD -prevN*currD
        = (prevN__old+currN__old*K)*currD__old
        - currN__old*(prevD__old+currD__old*K)
        = prevN__old*currD__old - currN__old*prevD__old
        !! [currN__old*prevD__old -prevN__old*currD__old == (-1)**(num_steps-1)]
        = -(-1)**(num_steps-1)
        = (-1)**num_steps
        = rhs
        ]
    DONE
    ]]

===
反推公式 试更新 ,,, 无用约束 失败
    !! [currN*prevD -prevN*currD == (-1)**num_steps]
    !! [currN__old*prevD__old -prevN__old*currD__old == (-1)**(num_steps-1)]
    [currN__old*prevD__old -prevN__old*currD__old == -(currN*prevD -prevN*currD)]

    !! [K := cf_digits[num_steps-1]]
    !! [prevN == currN__old]
    !! [prevD == currD__old]
    !! [currN == (prevN__old+currN__old*K)]
    !! [currD == (prevD__old+currD__old*K)]
    ???与K无关???
    [8/5 == cf([1;1,1,2]) == cf([1;1,1,1,1])]
    0/1,1/0,1/1,2/1,3/2,8/5
    K=2:(3,2;8,5)

    0/1,1/0,1/1,2/1,3/2,5/3,8/5
    K=1:(5,3;8,5)
        (N,D;5,3)
        [K=1]:
            [N+1*5==8]
            [D+1*3==5]
            [N == 3]
            [D == 2]
            [5*D -N*3 == 5*2 -3*3 == 10-9 == 1]
        [K=2]:
            [N+2*5==8]
            [D+2*3==5]
            [N == -2]
            [D == -1]
            [5*D -N*3 == 5*(-1) -(-2)*3 == -5+6 == 1]


===
===
]]]

to prove:
    [[prevD == currD] <-> [[prevD == currD == 1][num_steps == 2][cf_digits[:num_steps]==[cf0;1]]]]
to prove:
    [[0 == currD < prevD == 1] if num_steps == 0 else [0 <= prevD <= currD]]


[[
完全穷举反转推导法:here
===
complete-case xxx of:
  * case0 -> outA
  * case1 -> outB
  ...
  * caseX -> outA
  ...
==>>:
complete-case out of:
  * outA -> case0 or caseX or ...
  * outB -> case1 or ...
  ...
这玩意叫什么？归谬法？排中律？还是 归纳法+逆否命题
]]

[[[
view ../../python3_src/seed/math/gcd.py
    gcd_via_halve_
===
比辗转相除还快，怎么做到的？
    view ../../python3_src/seed/math/ops/algebra/algebra.txt
        前面两个(Binary GCD, Lehmer’s algorithm)并没能少于O(N**2)
        HGCD/(half-gcd) 是 using the divide and conquer algorithm，拆成两位数，作除法，下一轮 减法+乘法(乘法<O(N**2))，加速在于『乘法』
        ===
        https://gmplib.org/manual/Greatest-Common-Divisor-Algorithms
        ===
        15.3 Greatest Common Divisor
            Binary GCD
            Lehmer’s algorithm
            Subquadratic GCD
                https://gmplib.org/manual/Subquadratic-GCD
===
https://mathworld.wolfram.com/Half-GCD.html
===
Half-GCD
Given integers a and b with close to 2n bits each, the half-GCD of a and b is a 2×2 matrix

 [u v; u^' v^'] 
with determinant equal to -1 or 1 such that ua+vb=r and u^'a+v^'b=r^', where r and r^' each have a number of bits close to n.

The half-GCD results by performing roughly half the Euclidean algorithm for computing the greatest common divisor GCD(a,b). There is an efficient algorithm for computing the half-GCD of two large numbers which, when applied recursively, allows the greatest common divisor to be computed faster than using the Euclidean algorithm.

SEE ALSO
Euclidean Algorithm, Greatest Common Divisor
]]]

[[[
https://en.m.wikibooks.org/wiki/Commutative_Ring_Theory/B%C3%A9zout_domains
Definition (Bézout domain):
    A Bézout domain is an integral domain whose every finitely generated ideal is principal, ie. generated by a single element.
Proposition (Every Bézout domain is a GCD domain)
[BezoutDomain <: GCD_domain]

https://handwiki.org/wiki/B%C3%A9zout%27s_identity
[[ring <- BezoutDomain] =[def]= [[ring <- IntegralDomain][@[u,v :<- ring] -> ?[k4u,k4v :<- ring] -> [k4u*u+k4v*v == gcd(u,v)]]]]
[ring.does_Bezout_identity_hold() =[def]= [@[u,v :<- ring] -> ?[k4u,k4v :<- ring] -> [k4u*u+k4v*v == gcd(u,v)]]]
[is_Bezout_coefficient_pair_of_(u,v; k4u,k4v) =[def]= [k4u*u+k4v*v == gcd(u,v)]]
[ring.does_Bezout_identity_hold() =[def]= [@[u,v :<- ring] -> ?[k4u,k4v :<- ring] -> [is_Bezout_coefficient_pair_of_(u,v; k4u,k4v)]]]
[[ring <- BezoutDomain] =[def]= [[ring <- IntegralDomain][ring.does_Bezout_identity_hold()]]]
===
https://handwiki.org/wiki/B%C3%A9zout%27s_identity
===
Bézout's identity
From HandWiki
Short description: Relating two numbers and their greatest common divisor

In mathematics, Bézout's identity (also called Bézout's lemma), named after Étienne Bézout, is the following theorem:

Bézout's identity — Let a and b be integers with greatest common divisor d. Then there exist integers x and y such that a*x + b*y = d. Moreover, the integers of the form a*z + b*t are exactly the multiples of d.

Here the greatest common divisor of 0 and 0 is taken to be 0. The integers x and y are called Bézout coefficients for (a, b); they are not unique. A pair of Bézout coefficients can be computed by the extended Euclidean algorithm, and this pair is, in the case of integers one of the two pairs such that [[abs(x) <= abs(b/d)][abs(y) <= abs(a/d)]] and equality occurs only if one of a and b is a multiple of the other.

As an example, the greatest common divisor of 15 and 69 is 3, and 3 can be written as a combination of 15 and 69 as 3 = 15 × (−9) + 69 × 2, with Bézout coefficients −9 and 2.

Many other theorems in elementary number theory, such as Euclid's lemma or the Chinese remainder theorem, result from Bézout's identity.

A Bézout domain is an integral domain in which Bézout's identity holds. In particular, Bézout's identity holds in principal ideal domains. Every theorem that results from Bézout's identity is thus true in all principal ideal domains.


Contents
1	Structure of solutions
1.1	Example
2	Proof
3	Generalizations
3.1	For three or more integers
3.2	For polynomials
3.3	For principal ideal domains
4	History
5	See also
6	Notes
7	External links
Structure of solutions
If a and b are not both zero and one pair of Bézout coefficients (x, y) has been computed (for example, using the extended Euclidean algorithm), all pairs can be represented in the form 
    (x-k*(b/d), y+k*(a/d))
    where k is an arbitrary integer, d is the greatest common divisor of a and b, and the fractions simplify to integers.

If a and b are both nonzero, then exactly two of these pairs of Bézout coefficients satisfy 
    [[abs(x) <= abs(b/d)][abs(y) <= abs(a/d)]]
    and equality may occur only if one of a and b divides the other.

This relies on a property of Euclidean division: given two non-zero integers c and d, if d does not divide c, there is exactly one pair (q, r) such that [[c == d*q+r][0 < r < abs(d)]] and another one such that [[c == d*q+r][0 > r > -abs(d)]]

The two pairs of small Bézout's coefficients are obtained from the given one (x, y) by choosing for k in the above formula either of the two integers next to 
    (x/(b/d))
    .

The extended Euclidean algorithm always produces one of these two minimal pairs.

Example
Let a = 12 and b = 42, then gcd (12, 42) = 6. Then the following Bézout's identities are had, with the Bézout coefficients written in red for the minimal pairs and in blue for the other ones.

a*x       +    b*y     == d
... ...
12*-10    +    42*3    == 6
12*-3     +    42*1    == 6
12*4      +    42*-1   == 6
12*11     +    42*-3   == 6
... ...

If [(x,y)==(18,-5)] is the original pair of Bézout coefficients, then 
    (18/(42/6)) <- Real[>2..<3]
 yields the minimal pairs via k = 2, respectively k = 3; that is, (18 − 2 ⋅ 7, −5 + 2 ⋅ 2) = (4, −1), and (18 − 3 ⋅ 7, −5 + 3 ⋅ 2) = (−3, 1).

Proof
Given any nonzero integers a and b, let  The set S is nonempty since it contains either a or –a (with  and ). Since S is a nonempty set of positive integers, it has a minimum element , by the well-ordering principle. To prove that d is the greatest common divisor of a and b, it must be proven that d is a common divisor of a and b, and that for any other common divisor c, one has 

The Euclidean division of a by d may be written  The remainder r is in , because  					  Thus r is of the form , and hence  However,  and d is the smallest positive integer in S: the remainder r can therefore not be in S, making r necessarily 0. This implies that d is a divisor of a. Similarly d is also a divisor of b, and therefore d is a common divisor of a and b.

Now, let c be any common divisor of a and b; that is, there exist u and v such that  and  One has thus  					  That is, c is a divisor of d. Since  this implies 

Generalizations
For three or more integers
Bézout's identity can be extended to more than two integers: if  then there are integers  such that  has the following properties:

d is the smallest positive integer of this form
every number of this form is a multiple of d
For polynomials
Bézout's identity does not always hold for polynomials. For example, when working in the polynomial ring of integers: the greatest common divisor of 2*x and x**2 is x, but there does not exist any integer-coefficient polynomials p and q satisfying 2*x*p + x**2*q = x.

However, Bézout's identity works for univariate polynomials over a field exactly in the same ways as for integers. In particular the Bézout's coefficients and the greatest common divisor may be computed with the extended Euclidean algorithm.

As the common roots of two polynomials are the roots of their greatest common divisor, Bézout's identity and fundamental theorem of algebra imply the following result:

For univariate polynomials f and g with coefficients in a field, there exist polynomials a and b such that af + bg = 1 if and only if f and g have no common root in any algebraically closed field (commonly the field of complex numbers).
The generalization of this result to any number of polynomials and indeterminates is Hilbert's Nullstellensatz.

For principal ideal domains
As noted in the introduction, Bézout's identity works not only in the ring of integers, but also in any other principal ideal domain (PID). That is, if R is a PID, and a and b are elements of R, and d is a greatest common divisor of a and b, then there are elements x and y in R such that  The reason is that the ideal  is principal and equal to 

An integral domain in which Bézout's identity holds is called a Bézout domain.

History
French mathematician Étienne Bézout (1730–1783) proved this identity for polynomials.[1] This statement for integers can be found already in the work of an earlier French mathematician, Claude Gaspard Bachet de Méziriac (1581–1638).[2][3][4]

See also
AF+BG theorem – About algebraic curves passing through all intersection points of two other curves, an analogue of Bézout's identity for homogeneous polynomials in three indeterminates
Euclid's lemma – A prime divisor of a product divides one of the factors
Fundamental theorem of arithmetic – Integers have unique prime factorizations
]]]






>>> approximate_fraction5continued_fraction__by_limit_denominator_(100, [1]*20)
Fraction(144, 89)

>>> continued_fraction_fold_state0
ContinuedFractionFoldState(0, 1, 1, 0)
>>> continued_fraction_fold_state0.get_prev_fraction()
Fraction(0, 1)
>>> continued_fraction_fold_state0.get_curr_fraction()
Traceback (most recent call last):
    ...
ZeroDivisionError: Fraction(1, 0)
>>> continued_fraction_fold_state0.get_currND()
(1, 0)

>>> st = continued_fraction_fold_state0.steps_(range(1,10))
>>> st
ContinuedFractionFoldState(81201, 56660, 740785, 516901)

>>> [*iter_continued_fraction_digits5ND_(*st.get_prevND())]
[1, 2, 3, 4, 5, 6, 7, 8]
>>> [*iter_continued_fraction_digits5ND_(*st.get_currND())]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> [*backward_iter_cf_digits_(*st.get_args())]
[9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> [*st.iter_cf_digits_()]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> st.list_cf_steps__separately_()
([1, 2, 3, 4, 5, 6, 7, 8, 9], [ContinuedFractionFoldState(0, 1, 1, 0), ContinuedFractionFoldState(1, 0, 1, 1), ContinuedFractionFoldState(1, 1, 3, 2), ContinuedFractionFoldState(3, 2, 10, 7), ContinuedFractionFoldState(10, 7, 43, 30), ContinuedFractionFoldState(43, 30, 225, 157), ContinuedFractionFoldState(225, 157, 1393, 972), ContinuedFractionFoldState(1393, 972, 9976, 6961), ContinuedFractionFoldState(9976, 6961, 81201, 56660), ContinuedFractionFoldState(81201, 56660, 740785, 516901)])
>>> st.list_cf_steps__separately_() == ([*st.iter_cf_digits_()], [*continued_fraction_fold_state0.iter_steps_(range(1,10))])
True

>>> [*iter_continued_fraction_digits5ND_(-300,59)]
[-6, 1, 10, 1, 4]
>>> [*iter_approximate_fractions5continued_fraction_([1]*6)]
[Fraction(1, 1), Fraction(2, 1), Fraction(3, 2), Fraction(5, 3), Fraction(8, 5), Fraction(13, 8)]
>>> [*iter_approximate_fractions5continued_fraction_([-1, *[1]*6])]
[Fraction(-1, 1), Fraction(0, 1), Fraction(-1, 2), Fraction(-1, 3), Fraction(-2, 5), Fraction(-3, 8), Fraction(-5, 13)]

>>> st = continued_fraction_fold_state0.steps_([-46, *range(1,10)])
>>> st.list_cf_steps__separately_() == ([*st.iter_cf_digits_()], [*continued_fraction_fold_state0.iter_steps_([-46, *range(1,10)])])
True
>>> st.list_cf_steps__separately_() == st.list_cf_steps__separately_(backward_vs_forward=True)
True
>>> st.list_cf_steps__separately_() == st.list_cf_steps__separately_(backward_vs_forward=False)
True


>>> [*iter_approximate_fraction_NDs5continued_fraction__by_limit_denominator_(None, [2,2,2,2,2,2,2])]
[(2, 1), (5, 2), (12, 5), (29, 12), (70, 29), (169, 70), (408, 169)]
>>> [*iter_approximate_fraction_NDs_le5continued_fraction__by_limit_denominator_(None, [2,2])]
[(2, 1), (5, 2)]
>>> [*iter_approximate_fraction_NDs_le5continued_fraction__by_limit_denominator_(None, [2,2,2])]
[(2, 1), (12, 5)]
>>> [*iter_approximate_fraction_NDs_le5continued_fraction__by_limit_denominator_(None, [2,2,2,2])]
[(2, 1), (12, 5), (29, 12)]
>>> [*iter_approximate_fraction_NDs_le5continued_fraction__by_limit_denominator_(None, [2,2,2,2,2])]
[(2, 1), (12, 5), (70, 29)]

>>> [*iter_approximate_fraction_NDs_le5continued_fraction__by_limit_denominator_(30, [2,2,2,2,2])]
[(2, 1), (12, 5), (70, 29)]
>>> [*iter_approximate_fraction_NDs_le5continued_fraction__by_limit_denominator_(29, [2,2,2,2,2])]
[(2, 1), (12, 5)]
>>> [*iter_approximate_fraction_NDs_le5continued_fraction__by_limit_denominator_(6, [2,2,2,2,2])]
[(2, 1), (12, 5)]
>>> [*iter_approximate_fraction_NDs_le5continued_fraction__by_limit_denominator_(5, [2,2,2,2,2])]
[(2, 1)]
>>> [*iter_approximate_fraction_NDs_le5continued_fraction__by_limit_denominator_(2, [2,2,2,2,2])]
[(2, 1)]

>>> [*iter_approximate_fraction_NDs_le5continued_fraction__by_limit_denominator_(13, [2,2,2,2])]
[(2, 1), (12, 5), (29, 12)]
>>> [*iter_approximate_fraction_NDs_le5continued_fraction__by_limit_denominator_(12, [2,2,2,2])]
[(2, 1), (12, 5)]
>>> [*iter_approximate_fraction_NDs_le5continued_fraction__by_limit_denominator_(6, [2,2,2,2])]
[(2, 1), (12, 5)]
>>> [*iter_approximate_fraction_NDs_le5continued_fraction__by_limit_denominator_(5, [2,2,2,2])]
[(2, 1)]
>>> [*iter_approximate_fraction_NDs_le5continued_fraction__by_limit_denominator_(2, [2,2,2,2])]
[(2, 1)]





[(2, 1), (5, 2), (12, 5), (29, 12), (70, 29), (169, 70), (408, 169)]
>>> [*iter_approximate_fraction_NDs_ge5continued_fraction__by_limit_denominator_(None, [2])]
[(2, 1)]
>>> [*iter_approximate_fraction_NDs_ge5continued_fraction__by_limit_denominator_(None, [2,2])]
[(5, 2)]
>>> [*iter_approximate_fraction_NDs_ge5continued_fraction__by_limit_denominator_(None, [2,2,2])]
[(5, 2), (12, 5)]
>>> [*iter_approximate_fraction_NDs_ge5continued_fraction__by_limit_denominator_(None, [2,2,2,2])]
[(5, 2), (29, 12)]
>>> [*iter_approximate_fraction_NDs_ge5continued_fraction__by_limit_denominator_(None, [2,2,2,2,2])]
[(5, 2), (29, 12), (70, 29)]

>>> [*iter_approximate_fraction_NDs_ge5continued_fraction__by_limit_denominator_(30, [2,2,2,2,2])]
[(5, 2), (29, 12), (70, 29)]
>>> [*iter_approximate_fraction_NDs_ge5continued_fraction__by_limit_denominator_(29, [2,2,2,2,2])]
[(5, 2), (29, 12)]
>>> [*iter_approximate_fraction_NDs_ge5continued_fraction__by_limit_denominator_(29, [2,2,2,2,2])]
[(5, 2), (29, 12)]
>>> [*iter_approximate_fraction_NDs_ge5continued_fraction__by_limit_denominator_(13, [2,2,2,2,2])]
[(5, 2), (29, 12)]
>>> [*iter_approximate_fraction_NDs_ge5continued_fraction__by_limit_denominator_(12, [2,2,2,2,2])]
[(5, 2)]
>>> [*iter_approximate_fraction_NDs_ge5continued_fraction__by_limit_denominator_(3, [2,2,2,2,2])]
[(5, 2)]
>>> [*iter_approximate_fraction_NDs_ge5continued_fraction__by_limit_denominator_(2, [2,2,2,2,2])]
[]

>>> [*iter_approximate_fraction_NDs_ge5continued_fraction__by_limit_denominator_(13, [2,2,2,2])]
[(5, 2), (29, 12)]
>>> [*iter_approximate_fraction_NDs_ge5continued_fraction__by_limit_denominator_(12, [2,2,2,2])]
[(5, 2)]
>>> [*iter_approximate_fraction_NDs_ge5continued_fraction__by_limit_denominator_(3, [2,2,2,2])]
[(5, 2)]
>>> [*iter_approximate_fraction_NDs_ge5continued_fraction__by_limit_denominator_(2, [2,2,2,2])]
[]














view ../../python3_src/seed/math/inv_mod_.py
>>> from seed.math.continued_fraction.continued_fraction_fold import ginv_mod_respectively_
>>> ginv_mod_respectively_(3, 2)
(1, 2, 1, -1, 1, 3, 2)
>>> ginv_mod_respectively_(15, 10)
(1, 2, 1, -1, 5, 3, 2)
>>> ginv_mod_respectively_(15, -10)
Traceback (most recent call last):
    ...
TypeError
>>> ginv_mod_respectively_(15, 0)
Traceback (most recent call last):
    ...
TypeError
>>> ginv_mod_respectively_(0, 1)
Traceback (most recent call last):
    ...
TypeError
>>> ginv_mod_(-1, 1)
Traceback (most recent call last):
    ...
TypeError
>>> ginv_mod_(0, 1)
Traceback (most recent call last):
    ...
TypeError
>>> ginv_mod_(1, -1)
(0, 0, -1, 1, 1, -1)
>>> ginv_mod_(1, 0)
(0, 1, 0, 1, 1, 0)





>>> from seed.math.continued_fraction.continued_fraction_fold import inv_mod_
>>> from seed.math.inv_mod_ import inv_mod_ as _inv_mod_
>>> _inv_mod_ is inv_mod_
True

>>> inv_mod_(3, 2)
2
>>> inv_mod_(16, 5)
13


>>> inv_mod_(1, 0)
0
>>> inv_mod_(1, 4)
0
>>> inv_mod_(3, 2)
2
>>> inv_mod_(-3, 2)
2
>>> inv_mod_(3, -2)
1
>>> inv_mod_(-3, -2)
1

>>> inv_mod_(0, 1)
Traceback (most recent call last):
    ...
ZeroDivisionError
>>> inv_mod_(10, 6)
Traceback (most recent call last):
    ...
seed.math.continued_fraction.continued_fraction_fold.NotCoprimeError: not coprime: [gcd(6, 10) == 2]




>>> mk_coprime_certification_(3, 5)
(3, 5, 2, -1)
>>> mk_coprime_certification_(0, 1)
(0, 1, 0, 1)
>>> mk_coprime_certification_(0, 0)
Traceback (most recent call last):
    ...
seed.math.continued_fraction.continued_fraction_fold.NotCoprimeError: not coprime: [gcd(0, 0) == 0]
>>> mk_coprime_certification_(0, 2)
Traceback (most recent call last):
    ...
seed.math.continued_fraction.continued_fraction_fold.NotCoprimeError: not coprime: [gcd(0, 2) == 2]






>>> mk_gcd_certification_(0, 0)
(0, 0, 1, 0, 0, 1, 0)

>>> mk_gcd_certification_(0, 1)
(0, 1, 0, 1, 1, 0, 1)
>>> mk_gcd_certification_(0, 2)
(0, 2, 0, 1, 2, 0, 1)
>>> mk_gcd_certification_(0, -1)
(0, -1, 0, -1, 1, 0, -1)
>>> mk_gcd_certification_(0, -2)
(0, -2, 0, -1, 2, 0, -1)

>>> mk_gcd_certification_(1, 0)
(1, 0, 1, 0, 1, 1, 0)
>>> mk_gcd_certification_(2, 0)
(2, 0, 1, 0, 2, 1, 0)
>>> mk_gcd_certification_(-1, 0)
(-1, 0, -1, 0, 1, -1, 0)
>>> mk_gcd_certification_(-2, 0)
(-2, 0, -1, 0, 2, -1, 0)

>>> mk_gcd_certification_(1, 1)
(1, 1, 0, 1, 1, 1, 1)
>>> mk_gcd_certification_(1, -1)
(1, -1, 0, -1, 1, 1, -1)
>>> mk_gcd_certification_(-1, 1)
(-1, 1, 0, 1, 1, -1, 1)
>>> mk_gcd_certification_(-1, -1)
(-1, -1, 0, -1, 1, -1, -1)

>>> mk_gcd_certification_(1, 2)
(1, 2, 1, 0, 1, 1, 2)
>>> mk_gcd_certification_(1, -2)
(1, -2, -1, -1, 1, 1, -2)
>>> mk_gcd_certification_(-1, 2)
(-1, 2, 1, 1, 1, -1, 2)
>>> mk_gcd_certification_(-1, -2)
(-1, -2, -1, 0, 1, -1, -2)

>>> mk_gcd_certification_(2, 1)
(2, 1, 0, 1, 1, 2, 1)
>>> mk_gcd_certification_(2, -1)
(2, -1, 0, -1, 1, 2, -1)
>>> mk_gcd_certification_(-2, 1)
(-2, 1, 0, 1, 1, -2, 1)
>>> mk_gcd_certification_(-2, -1)
(-2, -1, 0, -1, 1, -2, -1)

>>> mk_gcd_certification_(2, 2)
(2, 2, 0, 1, 2, 1, 1)
>>> mk_gcd_certification_(2, -2)
(2, -2, 0, -1, 2, 1, -1)
>>> mk_gcd_certification_(-2, 2)
(-2, 2, 0, 1, 2, -1, 1)
>>> mk_gcd_certification_(-2, -2)
(-2, -2, 0, -1, 2, -1, -1)

>>> mk_gcd_certification_(2, 6)
(2, 6, 1, 0, 2, 1, 3)
>>> mk_gcd_certification_(2, -6)
(2, -6, 1, 0, 2, 1, -3)
>>> mk_gcd_certification_(-2, 6)
(-2, 6, -1, 0, 2, -1, 3)
>>> mk_gcd_certification_(-2, -6)
(-2, -6, -1, 0, 2, -1, -3)

>>> mk_gcd_certification_(6, 2)
(6, 2, 0, 1, 2, 3, 1)
>>> mk_gcd_certification_(6, -2)
(6, -2, 0, -1, 2, 3, -1)
>>> mk_gcd_certification_(-6, 2)
(-6, 2, 0, 1, 2, -3, 1)
>>> mk_gcd_certification_(-6, -2)
(-6, -2, 0, -1, 2, -3, -1)


>>> mk_gcd_certification_(3, 5)
(3, 5, 2, -1, 1, 3, 5)
>>> mk_gcd_certification_(3, -5)
(3, -5, 2, 1, 1, 3, -5)
>>> mk_gcd_certification_(-3, 5)
(-3, 5, -2, -1, 1, -3, 5)
>>> mk_gcd_certification_(-3, -5)
(-3, -5, -2, 1, 1, -3, -5)

>>> mk_gcd_certification_(5, 3)
(5, 3, -1, 2, 1, 5, 3)
>>> mk_gcd_certification_(5, -3)
(5, -3, -1, -2, 1, 5, -3)
>>> mk_gcd_certification_(-5, 3)
(-5, 3, 1, 2, 1, -5, 3)
>>> mk_gcd_certification_(-5, -3)
(-5, -3, 1, -2, 1, -5, -3)


>>> mk_gcd_certification_(63, 35)
(63, 35, -1, 2, 7, 9, 5)
>>> mk_gcd_certification_(63, -35)
(63, -35, -1, -2, 7, 9, -5)
>>> mk_gcd_certification_(-63, 35)
(-63, 35, 1, 2, 7, -9, 5)
>>> mk_gcd_certification_(-63, -35)
(-63, -35, 1, -2, 7, -9, -5)

>>> mk_gcd_certification_(35, 63)
(35, 63, 2, -1, 7, 5, 9)
>>> mk_gcd_certification_(35, -63)
(35, -63, 2, 1, 7, 5, -9)
>>> mk_gcd_certification_(-35, 63)
(-35, 63, -2, -1, 7, -5, 9)
>>> mk_gcd_certification_(-35, -63)
(-35, -63, -2, 1, 7, -5, -9)


.+1,.+55s/\*\+\([^*]\|\n\)*Got:\n *//
>>> mk_gcd_certification_(5, 8)
(5, 8, -3, 2, 1, 5, 8)
>>> mk_gcd_certification_(5, -8)
(5, -8, -3, -2, 1, 5, -8)
>>> mk_gcd_certification_(-5, 8)
(-5, 8, 3, 2, 1, -5, 8)
>>> mk_gcd_certification_(-5, -8)
(-5, -8, 3, -2, 1, -5, -8)

>>> mk_gcd_certification_(8, 5)
(8, 5, 2, -3, 1, 8, 5)
>>> mk_gcd_certification_(8, -5)
(8, -5, 2, 3, 1, 8, -5)
>>> mk_gcd_certification_(-8, 5)
(-8, 5, -2, -3, 1, -8, 5)
>>> mk_gcd_certification_(-8, -5)
(-8, -5, -2, 3, 1, -8, -5)






select from above:
    [[abs(v) == 1] -> [k4u == 0]]
>>> mk_gcd_certification_(1, 1)
(1, 1, 0, 1, 1, 1, 1)
>>> mk_gcd_certification_(1, -1)
(1, -1, 0, -1, 1, 1, -1)
>>> mk_gcd_certification_(-1, 1)
(-1, 1, 0, 1, 1, -1, 1)
>>> mk_gcd_certification_(-1, -1)
(-1, -1, 0, -1, 1, -1, -1)

>>> mk_gcd_certification_(2, 1)
(2, 1, 0, 1, 1, 2, 1)
>>> mk_gcd_certification_(2, -1)
(2, -1, 0, -1, 1, 2, -1)
>>> mk_gcd_certification_(-2, 1)
(-2, 1, 0, 1, 1, -2, 1)
>>> mk_gcd_certification_(-2, -1)
(-2, -1, 0, -1, 1, -2, -1)



select from above:
    [[???] <-> [coprime(u,v)][k4u < 0]]
    # [condition____k4u__lt__0]:goto
    [[even := [len(cf_digits5ND_(u,v))%2==0]] -> [1==gcd(u,v)] -> [[k4u < 0] <-> [[[v == 0][u == -1]] or [[v=!=0][u=!=0][[v < 0] == even]]]]]
        # [coprime(u,v)] outside (<->)
>>> mk_gcd_certification_(-1, 0)
(-1, 0, -1, 0, 1, -1, 0)

>>> mk_gcd_certification_(1, -2)
(1, -2, -1, -1, 1, 1, -2)
>>> mk_gcd_certification_(-1, -2)
(-1, -2, -1, 0, 1, -1, -2)

>>> mk_gcd_certification_(-3, 5)
(-3, 5, -2, -1, 1, -3, 5)
>>> mk_gcd_certification_(-3, -5)
(-3, -5, -2, 1, 1, -3, -5)
>>> mk_gcd_certification_(-8, 5)
(-8, 5, -2, -3, 1, -8, 5)
>>> mk_gcd_certification_(-8, -5)
(-8, -5, -2, 3, 1, -8, -5)
>>> mk_gcd_certification_(5, 3)
(5, 3, -1, 2, 1, 5, 3)
>>> mk_gcd_certification_(5, -3)
(5, -3, -1, -2, 1, 5, -3)
>>> mk_gcd_certification_(5, 8)
(5, 8, -3, 2, 1, 5, 8)
>>> mk_gcd_certification_(5, -8)
(5, -8, -3, -2, 1, 5, -8)


>>> cf_digits5ND_ = lambda N,D,/:continued_fraction_digits_ex5ND_(N,D)[0]
>>> cf_digits5ND_(-1, 0)
[]

>>> cf_digits5ND_(1, -2)
[-1, 2]
>>> cf_digits5ND_(-1, -2)
[0, 2]

>>> cf_digits5ND_(-3, 5)
[-1, 2, 2]
>>> cf_digits5ND_(-3, -5)
[0, 1, 1, 2]
>>> cf_digits5ND_(-8, 5)
[-2, 2, 2]
>>> cf_digits5ND_(-8, -5)
[1, 1, 1, 2]
>>> cf_digits5ND_(5, 3)
[1, 1, 2]
>>> cf_digits5ND_(5, -3)
[-2, 3]
>>> cf_digits5ND_(5, 8)
[0, 1, 1, 1, 2]
>>> cf_digits5ND_(5, -8)
[-1, 2, 1, 2]



>>> from seed.math.continued_fraction.continued_fraction_fold import _test____inv_mod__basic_, _test____inv_mod_, _test____mk_coprime_certification_, _test____mk_gcd_certification_
>>> _test____inv_mod_(7)
>>> _test____mk_coprime_certification_(7)
>>> _test____mk_gcd_certification_(20)







[[
充要条件冫错开一位纟分子分母序列纟渐近分数纟连分数:
py_adhoc_call   seed.math.continued_fraction.continued_fraction_fold   ,iter_approximate_fraction_NDs5continued_fraction_  ='[2]*7'
(2, 1)
(5, 2)
(12, 5)
(29, 12)
(70, 29)
(169, 70)
(408, 169)
py_adhoc_call   seed.math.continued_fraction.continued_fraction_fold   ,iter_approximate_fraction_NDs5continued_fraction_  ='[3]*7'
(3, 1)
(10, 3)
(33, 10)
(109, 33)
(360, 109)
(1189, 360)
(3927, 1189)
==>>:
充要条件冫错开一位纟分子分母序列纟渐近分数纟连分数:
    # 错开一位:分母超前一位
    [[分母纟渐近分数纟连分数{cf}[j] == 分子纟渐近分数纟连分数{cf}[j+1]] <-> [[cf0==0][cf == [0; *[cf1]*+oo]]]]
    # 错开一位:分子超前一位
    [[分子纟渐近分数纟连分数{cf}[j] == 分母纟渐近分数纟连分数{cf}[j+1]] <-> [[cf0>=1][cf == [cf0]*+oo]]]
    # continued_fraction_fold_state0 = ContinuedFractionFoldState(0,1,1,0)
    #   (prevN, prevD, currN, currD)
    # (0/1, 1/0, cf0/1, (1+cf0*cf1)/(0+1*cf1), ...)
    # [cf0==0]:(0/1, 1/0, 0/1, 1/cf1, ...)
==>>:
充要条件冫错开囜位纟分子分母序列纟渐近分数纟连分数:
    ???

view others/数学/continued-fraction/充要条件冫错开囜位纟分子分母序列纟渐近分数纟连分数.txt
]]




#]]]'''
__all__ = r'''
BadDataFormatError
    backward_iter_cf_steps_
    backward_iter_cf_digits_

ContinuedFractionFoldState
    continued_fraction_fold_state0

iter_continued_fraction_digits5ND_

ContinuedFractionError__inf__no_cf0
iter_approximate_fraction_NDs5continued_fraction_
    iter_approximate_fractions5continued_fraction_
    calc_ND5finite_continued_fraction_
    calc_Fraction5finite_continued_fraction_

    iter_approximate_fraction_NDs5continued_fraction__by_limit_denominator_
        iter_approximate_fraction_NDs_le5continued_fraction__by_limit_denominator_
        iter_approximate_fraction_NDs_ge5continued_fraction__by_limit_denominator_
        iter_approximate_fractions5continued_fraction__by_limit_denominator_
        approximate_fraction5continued_fraction__by_limit_denominator_
            ApproximateFractionFail__limit_denominator_too_small_to_find_approximation_ge






iter_continued_fraction_digits_ex5ND_
    continued_fraction_digits_ex5ND_
    iter_continued_fraction_digits5ND_

NotCoprimeError
ValidateFail
    ValidateFail__inv_mod
    ValidateFail__ginv_mod_respectively
    ValidateFail__ginv_mod_
    ValidateFail__coprime_certification
    ValidateFail__gcd_certification

continued_fraction_fold_state0
continued_fraction_digits_ex5ND_
    mk_gcd_certification_
        validate__gcd_certification_
        mk_coprime_certification_
            validate__coprime_certification_
            inv_mod_
                validate__inv_mod_
            ginv_mod_respectively_
                validate__ginv_mod_respectively_
            ginv_mod_
                validate__ginv_mod_

'''.split()#'''
__all__

from itertools import islice
from fractions import Fraction
from seed.helper.repr_input import repr_helper
from seed.types.NamedReadOnlyProperty import NamedReadOnlyProperty, set_NamedReadOnlyProperty4cls_, set_NamedReadOnlyProperty4sf_
#from seed.tiny import fst
#from seed.tiny import check_type_is, check_uint
from seed.tiny_.check import check_type_is, check_uint, check_int_ge, check_int_ge_lt

from seed.math.gcd import gcd
from seed.math.sign_of import sign_of


######################
######move to seed.math.continued_fraction.continued_fraction5ND
######re-export:
######################
from seed.math.continued_fraction.continued_fraction5ND import iter_continued_fraction_digits_ex5ND_, continued_fraction_digits_ex5ND_, iter_continued_fraction_digits5ND_







class NotCoprimeError(Exception):pass
class ValidateFail(Exception):pass
class ValidateFail__coprime_certification(ValidateFail):pass
class ValidateFail__gcd_certification(ValidateFail):pass
class ValidateFail__inv_mod(ValidateFail):pass
class ValidateFail__ginv_mod_respectively(ValidateFail):pass
class ValidateFail__ginv_mod_(ValidateFail):pass


def validate__ginv_mod_(M, x, inv_x_g, k4M, k4x, gcd_of_Mx, M_g, x_g, /):
    check_int_ge(1, M)
    check_type_is(int, x)
    check_type_is(int, inv_x_g)

    validate__gcd_certification_(M, x, k4M, k4x, gcd_of_Mx, M_g, x_g)

    #check_int_ge_lt(0, M_g, inv_x_g)
    if not 0 <= inv_x_g < M_g: raise ValidateFail__ginv_mod_

    if not (x_g%M_g  *inv_x_g -1)%M_g == 0: raise ValidateFail__ginv_mod_


def ginv_mod_(M, x, /):
    r'''[[[
    :: M/pint -> x/int -> (inv_x_g/uint%M_g, k4M, k4x, gcd_of_Mx, M_g, x_g)

    (inv_x_g, k4M, k4x, gcd_of_Mx, M_g, x_g) = ginv_mod_(M, x)
    precondition:
    [M >= 1]
    [x :: int] #while ginv_mod_respectively_ requires [v>=1]

    postcondition:
    [inv_x_g*x_g =[%M_g]= 1]

    [k4M*M +k4x*x == gcd_of_Mx >= 0]
    [[M_g*gcd_of_Mx == M][x_g*gcd_of_Mx == x]
    [k4M*M_g +k4x*x_g == 1]

    #]]]'''#'''
    check_int_ge(1, M)
    check_type_is(int, x)

    (M, x, k4M, k4x, gcd_of_Mx, M_g, x_g) = mk_gcd_certification_(M, x)
    # [k4M*M +k4x*x == gcd_of_Mx >= 0]
    # [[M_g*gcd_of_Mx == M][x_g*gcd_of_Mx == x]
    # [k4M*M_g +k4x*x_g == 1]
    inv_x_g = k4x%M_g
    # [inv_x_g*x_g =[%M_g]= 1]
    validate__ginv_mod_(M, x, inv_x_g, k4M, k4x, gcd_of_Mx, M_g, x_g)
    return (inv_x_g, k4M, k4x, gcd_of_Mx, M_g, x_g)




def validate__ginv_mod_respectively_(u, v, inv_u_g, inv_v_g, k4u, k4v, gcd_of_uv, u_g, v_g, /):
    check_int_ge(1, u)
    check_int_ge(1, v)
    check_type_is(int, inv_u_g)
    check_type_is(int, inv_v_g)

    validate__gcd_certification_(u, v, k4u, k4v, gcd_of_uv, u_g, v_g)

    #check_int_ge_lt(0, v_g, inv_u_g)
    #check_int_ge_lt(0, u_g, inv_v_g)
    if not 0 <= inv_u_g < v_g: raise ValidateFail__ginv_mod_respectively
    if not 0 <= inv_v_g < u_g: raise ValidateFail__ginv_mod_respectively

    if not (u_g%v_g  *inv_u_g -1)%v_g == 0: raise ValidateFail__ginv_mod_respectively
    if not (v_g%u_g  *inv_v_g -1)%u_g == 0: raise ValidateFail__ginv_mod_respectively
def ginv_mod_respectively_(u, v, /):
    r'''[[[
    :: u/pint -> v/pint -> (inv_u_g/uint%v_g, inv_v_g/uint%u_g, k4u, k4v, gcd_of_uv, u_g, v_g)

    (inv_u_g, inv_v_g, k4u, k4v, gcd_of_uv, u_g, v_g) = ginv_mod_respectively_(u, v)
    precondition:
    [u >= 1]
    [v >= 1] #while ginv_mod_ requires [x :: int]

    postcondition:
    [inv_u_g*u_g =[%v_g]= 1]
    [inv_v_g*v_g =[%u_g]= 1]

    [k4u*u +k4v*v == gcd_of_uv >= 0]
    [[u_g*gcd_of_uv == u][v_g*gcd_of_uv == v]
    [k4u*u_g +k4v*v_g == 1]

    #]]]'''#'''
    check_int_ge(1, u)
    check_int_ge(1, v)

    (u, v, k4u, k4v, gcd_of_uv, u_g, v_g) = mk_gcd_certification_(u, v)
    # [k4u*u +k4v*v == gcd_of_uv >= 0]
    # [[u_g*gcd_of_uv == u][v_g*gcd_of_uv == v]
    # [k4u*u_g +k4v*v_g == 1]
    inv_u_g = k4u%v_g
    inv_v_g = k4v%u_g
    # [inv_u_g*u_g =[%v_g]= 1]
    # [inv_v_g*v_g =[%u_g]= 1]
    validate__ginv_mod_respectively_(u, v, inv_u_g, inv_v_g, k4u, k4v, gcd_of_uv, u_g, v_g)
    return (inv_u_g, inv_v_g, k4u, k4v, gcd_of_uv, u_g, v_g)

def validate__inv_mod_(M, x, inv_x, /):
    check_type_is(int, M)
    check_type_is(int, x)
    check_type_is(int, inv_x)
    if M == 0: raise TypeError

    if not 0 <= inv_x < abs(M): raise ValidateFail__inv_mod
    if not (inv_x*x-1)%M == 0: raise ValidateFail__inv_mod

#view ../../python3_src/seed/math/inv_mod_.py
#view ../../python3_src/nn_ns/math_nn/integer/inv_mod_.py
def inv_mod_(M, x, /):
    '[M=!=0] ==>> [0 <= inv_mod_(M, x) < abs(M)][(inv_mod_(M, x)*x-1)%M == 0]'
    check_type_is(int, M)
    check_type_is(int, x)
    if M == 0: raise ZeroDivisionError#ValueError
    M = abs(M)
    if M == 1:
        ans = 0
    else:
        (_x, _M, k4x, k4M) = mk_coprime_certification_(x, M)
        # [k4x*x +k4M*M == 1]
        # [k4x*x -1 == -k4M*M]
        # !! [M =!= 0]
        # [(k4x*x -1)%M == 0]
        if 0:
            ans = k4x %M
        else:
            # [u := x][v := M][[abs(k4u) == 1] if v==0 else [abs(k4u) < abs(v_g) <= abs(v)]]
            ans = k4x +M if k4x < 0 else k4x
    if 0:
        assert 0 <= ans < abs(M)
        assert (ans*x-1)%M == 0
    else:
        validate__inv_mod_(M, x, ans)
    return ans

def _test____inv_mod__basic_():
    assert inv_mod_(1, 0) == 0
    assert inv_mod_(1, 4) == 0
    assert inv_mod_(3, 2) == 2
    assert inv_mod_(-3, 2) == 2
    assert inv_mod_(3, -2) == 1
    assert inv_mod_(-3, -2) == 1




#class CoprimeCertification:
    #def __init__(sf, u, v, /):
def validate__coprime_certification_(u, v, k4u, k4v, /):
    check_type_is(int, u)
    check_type_is(int, v)
    check_type_is(int, k4u)
    check_type_is(int, k4v)
    if not k4u*u +k4v*v == 1: raise ValidateFail__coprime_certification
def mk_coprime_certification_(u, v, /):
    r'''
:: u/int -> v/int -> (u, v, k4u, k4v)
postcondition:
    [k4u*u +k4v*v == 1]

    '''#'''
    (u, v, k4u, k4v, gcd_of_uv, u_g, v_g) = mk_gcd_certification_(u, v)
    if not gcd_of_uv == 1:
        uv = u, v
        raise NotCoprimeError(f'not coprime: [gcd{uv} == {gcd_of_uv}]')
    assert gcd_of_uv == 1
    assert u_g == u
    assert v_g == v
    #########postcondition:
    if 0:
        assert k4u*u +k4v*v == 1
    else:
        validate__coprime_certification_(u, v, k4u, k4v)
    return (u, v, k4u, k4v)
def validate__gcd_certification_(u, v, k4u, k4v, gcd_of_uv, u_g, v_g, /):
    check_type_is(int, u)
    check_type_is(int, v)
    check_type_is(int, k4u)
    check_type_is(int, k4v)
    #check_type_is(int, gcd_of_uv)
    check_uint(gcd_of_uv)
    check_type_is(int, u_g)
    check_type_is(int, v_g)
    try:
        if not ((gcd_of_uv == 0) is (u==0==v)): raise ValidateFail__gcd_certification
        if not ((not sign_of(u_g) == sign_of(u)) is (u==0==v)): raise ValidateFail__gcd_certification
        if not (sign_of(v_g) == sign_of(v)): raise ValidateFail__gcd_certification
        if not ((abs(k4u) == 1) if v==0 else (abs(k4u) < abs(v_g) <= abs(v))): raise ValidateFail__gcd_certification
        if not ((k4v == 0 == v_g) if v==0 else ((abs(k4v) < abs(u_g) or abs(k4v) == 1 == abs(u_g) or (abs(k4v) == 1 > 0 == abs(u_g))) and abs(u_g) <= abs(u))): raise ValidateFail__gcd_certification((k4v == 0 == v_g), v==0, ((abs(k4v) < abs(u_g), abs(k4v) == 1 == abs(u_g)), (abs(k4v) == 1 > 0 == abs(u_g)), abs(u_g) <= abs(u)))
            # (u, v, k4u, k4v, gcd_of_uv, u_g, v_g)
            # (0, -2, 0, -1, 2, 0, -1)
        if not (not v == 0 or (gcd_of_uv == abs(u) and k4u == u_g == (-1)**(u < 0) and k4v == v_g == 0)): raise ValidateFail__gcd_certification(v == 0, (gcd_of_uv == abs(u), k4u == u_g == (-1)**(u < 0), k4v == v_g == 0))


        if not (v == 0 or ((not u == 0) is (abs(k4v) <= abs(u_g)))): raise ValidateFail__gcd_certification

        # [v_ne_0____abs_k4v__cmp__abs_u_g]:goto
        if not (v == 0 or ((abs(k4v) > abs(u_g)) is (u==0) is (0 == u == u_g == k4u < abs(v_g) == abs(k4v) == 1))): raise ValidateFail__gcd_certification
        if not (v == 0 or ((abs(k4v) == abs(u_g)) is ((abs(u_g)==1) and ((abs(v_g) == 1)or((abs(v_g) == 2) and ((u<0) is not (v<0))))) is (abs(k4v) == abs(u_g) == 1 >= abs(k4u) == abs(v_g) -1))): raise ValidateFail__gcd_certification
        if not (v == 0 or ((abs(k4v) < abs(u_g)) is ((abs(u_g)>=2)or((abs(u_g)==1) and (abs(v_g) >= 2) and (((u<0) == (v<0))or(abs(v_g) >= 3)))) is ((abs(u_g)>=2)or(0 == abs(k4v) < abs(u_g) == 1 == abs(k4u) < abs(v_g) >= 2+((u<0) is not (v<0)))))): raise ValidateFail__gcd_certification

        #core condition:
        if not k4u*u +k4v*v == gcd_of_uv >= 0: raise ValidateFail__gcd_certification
        if not u_g*gcd_of_uv == u: raise ValidateFail__gcd_certification
        if not v_g*gcd_of_uv == v: raise ValidateFail__gcd_certification
        if not k4u*u_g +k4v*v_g == 1: raise ValidateFail__gcd_certification
    except ValidateFail as e:
        raise type(e)((u, v, k4u, k4v, gcd_of_uv, u_g, v_g)) from e
def mk_gcd_certification_(u, v, /):
    r'''
:: u/int -> v/int -> (u, v, k4u, k4v, gcd_of_uv/uint, u_g, v_g)
postcondition:
    [[gcd_of_uv == 0] <-> [u==0==v]]
    [[sign_of(u_g) =!= sign_of(u)] <-> [u==0==v]]
    [sign_of(v_g) == sign_of(v)]
    [[abs(k4u) == 1] if v==0 else [abs(k4u) < abs(v_g) <= abs(v)]] #for:inv_mod_()
    [[k4v == 0 == v_g] if v==0 else [[[abs(k4v) < abs(u_g)]or[abs(k4v) == 1 == abs(u_g)]or[abs(k4v) == 1 > 0 == abs(u_g)]][abs(u_g) <= abs(u)]]]
    [[v == 0] -> [[gcd_of_uv == abs(u)][k4u == u_g == (-1)**[u < 0]][k4v == v_g == 0]]]
    [[v =!= 0] -> [[u =!= 0] <-> [abs(k4v) <= abs(u_g)]]]
    # [v_ne_0____abs_k4v__cmp__abs_u_g]:goto
    [[v =!= 0] -> [[abs(k4v) > abs(u_g)] <-> [u==0] <-> [0 == u == u_g == k4u < abs(v_g) == abs(k4v) == 1]]]
    [[v =!= 0] -> [[abs(k4v) == abs(u_g)] <-> [[abs(u_g)==1][[abs(v_g) == 1]or[[abs(v_g) == 2][(u<0) =!= (v<0)]]]] <-> [abs(k4v) == abs(u_g) == 1 >= abs(k4u) == abs(v_g) -1]]]
    [[v =!= 0] -> [[abs(k4v) < abs(u_g)] <-> [[abs(u_g)>=2]or[[abs(u_g)==1][abs(v_g) >= 2][[(u<0) == (v<0)]or[abs(v_g) >= 3]]]] <-> [[abs(u_g)>=2]or[0 == abs(k4v) < abs(u_g) == 1 == abs(k4u) < abs(v_g) >= 2+[(u<0) =!= (v<0)]]]]]

    #core condition:
    [k4u*u +k4v*v == gcd_of_uv >= 0]
        # 'g' of 'gcd'
    [[u_g*gcd_of_uv == u][v_g*gcd_of_uv == v]
        # 'cd' of 'gcd'
    [k4u*u_g +k4v*v_g == 1]
        # <<== [连分数渐近分数囗互素关联]:goto


#[连分数渐近分数囗互素关联]:goto
#   --> addnew:coprime_certification/gcd_certification
# [@[cf_digits :: [int; pint*]] -> @[num_steps :<- [0..=len(cf_digits)]] -> [(prevN, prevD; currN, currD) := steps_(cf_digits; num_steps)] -> [currN*prevD -prevN*currD == (-1)**num_steps]]

    '''#'''
    #def mk_gcd_certification_
    check_type_is(int, u)
    check_type_is(int, v)
        #sgn4u = sign_of(u)
        #sgn4v = sign_of(v)

    (cf_digits, gcd_of_uv) = continued_fraction_digits_ex5ND_(u, v)
    st = continued_fraction_fold_state0.steps_(cf_digits)
    (prevN, prevD, currN, currD) = st.get_args()
    num_steps = len(cf_digits)

    # [[currD =!= 0] -> [currN/currD == u/v]]
    # [currN*v == u*currD]
    #
    # !! [1 == gcd(currN, currD)]
    # !! [currN*v == u*currD]
    # [?[g :: int] -> [[currN*g == u][currD*g == v][abs(g) == gcd_of_uv]]]
    #
    if gcd_of_uv == 0:
        assert u == 0 == v
        g = gcd_of_uv
    else:
        assert not u == 0 == v
        if not v == 0:
            # [currD =!= 0]
            # !! [currD >= 0]
            # [currD > 0]
            assert currD > 0
            g = -gcd_of_uv if v < 0 else gcd_of_uv
        else:
            assert not u == 0
            # [v == 0]
            #     <==> [num_steps == 0]
            #     <==> [len(cf_digits) == 0]
            #     <==> [currN == 1][currD == 0]
            # [[[v==0][(u < 0) xor (currN < 0)]] <-> [[v==0][u < 0]]]
            if 0:
                assert not currN == 0
                g = -gcd_of_uv if (u < 0) ^ (currN < 0) else gcd_of_uv
            else:
                assert currN == 1
                g = -gcd_of_uv if u < 0 else gcd_of_uv

    g
    if g < 0:
        u_g = -currN
        v_g = -currD
    else:
        u_g = currN
        v_g = currD
    # !! [[currN*g == u][currD*g == v][abs(g) == gcd_of_uv]]
    # [[u_g*gcd_of_uv == u][v_g*gcd_of_uv == v]]
    # !! [1 == gcd(currN, currD)]
    # [1 == gcd(u_g, v_g)]
    #
    # [abs(u_g) == abs(currN)]
    # [abs(v_g) == currD]
    #
    # !! [[u_g*gcd_of_uv == u][v_g*gcd_of_uv == v]]
    # [[gcd_of_uv =!= 0] -> [[abs(u_g) <= abs(u)][abs(v_g) <= abs(v)]]]
    #

    # !! [currN*prevD -prevN*currD == (-1)**num_steps]
    # [g*currN*prevD -prevN*g*currD == g*(-1)**num_steps]
    # [u*prevD -prevN*v == g*(-1)**num_steps]
    g_ = -g if num_steps&1 else g
    # [u*prevD -prevN*v == g_]
    if g_ < 0:
        k4u = -prevD
        k4v = +prevN
    else:
        k4u = +prevD
        k4v = -prevN
    # [k4u*u +k4v*v == abs(g_) == gcd_of_uv]
    #
    # !! [k4u == -prevD if if g_ < 0 else +prevD]
    # !! [prevD >= 0]
    # [abs(k4u) == prevD]
    #
    # !! [k4v == +prevN if if g_ < 0 else -prevN]
    # [abs(k4v) == abs(prevN)]
    #
    #
    # !! [[prevD == currD] <-> [[prevD == currD == 1][num_steps == 2][cf_digits==[cf0;1]]]]
    # !! [cf_digits returned by continued_fraction_digits_ex5ND_() can not has nonstd-form:[[len(cf_digits) >= 2][cf_digits[-1] == 1]]]
    # [prevD =!= currD]
    # !! [[0 == currD < prevD == 1] if num_steps == 0 else [0 <= prevD <= currD]]
    # [[0 == currD < prevD == 1] if num_steps == 0 else [0 <= prevD < currD]]
    # !! [[num_steps == 0] <-> [v == 0]]
    #
    # [[0 == currD < prevD == 1] if v == 0 else [0 <= prevD < currD]]
    #
    assert (0 == currD < prevD == 1) if num_steps == 0 else (0 <= prevD < currD)
    assert (num_steps == 0) is (v == 0)


    r'''[[[
    vars@[v == 0]
    ===
    [[v == 0] <-> [num_steps == 0] <-> [currD == 0] <-> [[prevN == 0][prevD == 1][currN == 1][currD == 0]]]

    [[gcd_of_uv == 0] <-> [u==0==v]]

    [[v == 0] -> [[g_ == g == u][gcd_of_uv == abs(u)]]]

    [[v == 0] -> [u >= 0] -> [[u_g == currN == 1][v_g == currD == 0][k4u == +prevD == 1][k4v == -prevN == 0]]]
    [[v == 0] -> [u < 0] -> [[u_g == -currN == -1][v_g == -currD == 0][k4u == -prevD == -1][k4v == +prevN == 0]]]
    [[v == 0] -> [[k4u == u_g == (-1)**[u < 0]][k4v == v_g == 0]]]
    ===main:
    [[v == 0] -> [[num_steps == 0][prevN == 0][prevD == 1][currN == 1][currD == 0][g_ == g == u][gcd_of_uv == abs(u)][k4u == u_g == (-1)**[u < 0]][k4v == v_g == 0]]]
    ===
    [[v == 0] -> [[gcd_of_uv == abs(u)][k4u == u_g == (-1)**[u < 0]][k4v == v_g == 0]]]

    #]]]'''#'''



    r'''[[[
    [sign_of(u_g) ~?~ sign_of(u)]
    [sign_of(v_g) ~?~ sign_of(v)]
    ===
    !! [u == u_g*gcd_of_uv]
    !! [gcd_of_uv >= 0]
    [[sign_of(u_g) =!= sign_of(u)] -> [gcd_of_uv == 0]]
    !! [[gcd_of_uv == 0] <-> [u==0==v]]
    [[sign_of(u_g) =!= sign_of(u)] -> [u==0==v]]
    !! [[v == 0] -> [[gcd_of_uv == abs(u)][k4u == u_g == (-1)**[u < 0]][k4v == v_g == 0]]]
    [[u == v == 0] -> [[gcd_of_uv == 0][k4u == u_g == 1][k4v == v_g == 0]]]
    [[u == v == 0] -> [[u_g == 1][v_g == 0]]]
    [[u == v == 0] -> [[+1 == sign_of(u_g) =!= sign_of(u) == 0][0 == sign_of(v_g) == sign_of(v) == 0]]]
    !! [[sign_of(u_g) =!= sign_of(u)] -> [u==0==v]]
    [[sign_of(u_g) =!= sign_of(u)] <-> [u==0==v]]
        # 『->』 --> 『<->』

    !! [v == v_g*gcd_of_uv]
    !! [gcd_of_uv >= 0]
    [[sign_of(v_g) =!= sign_of(v)] -> [u==0==v]]
    !! [[gcd_of_uv == 0] <-> [u==0==v]]
    [[sign_of(v_g) =!= sign_of(v)] -> [u==0==v]]
    !! [[u == v == 0] -> [[+1 == sign_of(u_g) =!= sign_of(u) == 0][0 == sign_of(v_g) == sign_of(v) == 0]]]
    [[sign_of(v_g) =!= sign_of(v)] -> _L]
    [sign_of(v_g) == sign_of(v)]

    ===main:
    [[sign_of(u_g) =!= sign_of(u)] <-> [u==0==v]]
    [sign_of(v_g) == sign_of(v)]

    #]]]'''#'''



    r'''[[[
    vars@[v =!= 0]
        relation(k4v, u_g)
            vs: relation(k4u, v_g)
                    #for inv_mod_()
    ===
    !! [[currN*g == u][currD*g == v][abs(g) == gcd_of_uv]]
    [[gcd_of_uv =!= 0] -> [[abs(currN) <= abs(u)][abs(currD) <= abs(v)]]]
    !! [[gcd_of_uv == 0] <-> [u==0==v]]
    [[v =!= 0] -> [[abs(currN) <= abs(u)][abs(currD) <= abs(v)]]]
    
    !! [[0 == currD < prevD == 1] if v == 0 else [0 <= prevD < currD]]
    [[v =!= 0] -> [0 <= prevD < currD]]
    !! [[v =!= 0] -> [[abs(currN) <= abs(u)][abs(currD) <= abs(v)]]]
    !! [abs(k4u) == prevD]
    !! [abs(v_g) == currD]
    [[v =!= 0] -> [0 <= abs(k4u) == prevD < currD == abs(v_g) <= abs(v)]]
    [[v =!= 0] -> [abs(k4u) < abs(v_g) <= abs(v)]]

    [[v == 0] <-> [num_steps == 0] <-> [currD == 0] <-> [[prevN == 0][prevD == 1][currN == 1][currD == 0]]]
    !! [abs(k4u) == prevD]
    [[v == 0] -> [abs(k4u) == prevD == 1]]
    [[v == 0] -> [abs(k4u) == 1]]
    !! [[v =!= 0] -> [abs(k4u) < abs(v_g) <= abs(v)]]
    [[abs(k4u) == 1] if v==0 else [abs(k4u) < abs(v_g) <= abs(v)]]



    !! [[gcd_of_uv == 0] <-> [u==0==v]]
    [[v =!= 0] -> [gcd_of_uv =!= 0]]
    !! [[currN*g == u][currD*g == v][abs(g) == gcd_of_uv]]
    !! [k4u*u +k4v*v == abs(g_) == gcd_of_uv]
    [[v =!= 0] -> [abs(k4v) == abs(gcd_of_uv -k4u*u)/abs(v) <= (gcd_of_uv +abs(k4u*u))/abs(v) == (1 +abs(k4u)*abs(u_g))/abs(v_g)]]
    !! [[v =!= 0] -> [abs(k4u) < abs(v_g) <= abs(v)]]
    #bug:[[v =!= 0] -> [abs(k4v) <= (1 +abs(k4u)*abs(u_g))/abs(v_g) < (1 +abs(v_g)*abs(u_g))/abs(v_g) == 1/abs(v_g) + abs(u_g)]]  #err@[u_g == 0] [『<』not hold]
          # bug@(u, v, k4u, k4v, gcd_of_uv, u_g, v_g)
          # (0, -2, 0, -1, 2, 0, -1)

    # bug:[[v =!= 0] -> [[abs(k4v) < abs(u_g)] <-> [[[abs(u_g)==1][abs(k4v) == 0]]or[abs(u_g)>=2]] <-> [[[abs(u_g)==1][abs(k4v) == 0][u =!= 0][v%u==0][abs(v)=!=abs(u)][abs(v_g)>=2][k4u == (-1)**[u<0]]]or[abs(u_g)>=2]] <-> bug:[[[abs(u_g)==1][abs(k4v) == 0][u =!= 0][abs(v_g)>=2][k4u == (-1)**[u<0]]]or[abs(u_g)>=2]]]]
      #bug@(u, v, k4u, k4v, gcd_of_uv, u_g, v_g)
      # (1, -2, -1, -1, 1, 1, -2),

    !! [[v =!= 0] -> [abs(k4u) < abs(v_g) <= abs(v)]]
    [[v =!= 0] -> [abs(k4u) <= abs(v_g) -1]]

    [[[ #begin:[v =!= 0]
    [v =!= 0]:
        !! [[gcd_of_uv == 0] <-> [u==0==v]]
        !! [v =!= 0]
        [gcd_of_uv =!= 0]
        !! [u == u_g*gcd_of_uv]
        [[u == 0] <-> [u_g==0]]
        !! [v == v_g*gcd_of_uv]
        [v_g =!= 0]


        !! [[v =!= 0] -> [abs(k4v) <= (1 +abs(k4u)*abs(u_g))/abs(v_g)]]
        !! [[v =!= 0] -> [abs(k4u) <= abs(v_g) -1]]
        !! [v =!= 0]
        [abs(k4v)
        <= (1 +abs(k4u)*abs(u_g))/abs(v_g)
        <= (1 +(abs(v_g)-1)*abs(u_g))/abs(v_g)
        == (1-abs(u_g))/abs(v_g) + abs(u_g)
        ]
        [abs(k4v) <= (1-abs(u_g))/abs(v_g) + abs(u_g)]

        #case abs(u_g) of:
        * [abs(u_g)==0]:
            [abs(k4v)
            <= (1-abs(u_g))/abs(v_g) + abs(u_g)
            == 1/abs(v_g)
            ]
            [abs(k4v) <= 1/abs(v_g) <= 1]

            !! [abs(u_g)==0]
            !! [[u == 0] <-> [u_g==0]]
            [u == 0]
            [cf_digits == [0;]]
            [[num_steps == 1][prevN == 1][prevD == 0][currN == 0][currD == 1]]
            !! [[abs(u_g) == abs(currN)][abs(v_g) == abs(currD)][abs(k4u) == abs(prevD)][abs(k4v) == abs(prevN)]]
            [[abs(u_g) == 0][abs(v_g) == 1][abs(k4u) == 0][abs(k4v) == 1]]
            [1 == abs(k4v) > abs(u_g) == 0]

        * [abs(u_g)==1]:
            [abs(k4v)
            <= (1-abs(u_g))/abs(v_g) + abs(u_g)
            == abs(u_g)
            == 1
            ]
            [abs(k4v) <= 1 == abs(u_g)]

            !! [abs(u_g)==1]
            !! [[u == 0] <-> [u_g==0]]
            [u =!= 0]
            !! [abs(u_g)==1]
            [abs(v/u) == abs(v_g/u_g) == abs(v_g)]
            [v%u == 0]
            !! [v =!= 0]
            [abs(v_g) == abs(v/u) =!= 0]
            [abs(v_g) >= 1]
            * [abs(v_g) == 1]:
                [abs(v/u) == abs(v_g) == 1]
                [u/v == v/u]
                [cf_digits == [u/v;]]
                [sts==(0,1;1,0;u/v,1)]
                [[num_steps == 1][prevN == 1][prevD == 0][currN == u/v][currD == 1]]
                !! [[abs(u_g) == abs(currN)][abs(v_g) == abs(currD)][abs(k4u) == abs(prevD)][abs(k4v) == abs(prevN)]]
                [[abs(u_g) == 1][abs(v_g) == 1][abs(k4u) == 0][abs(k4v) == 1]]
                [abs(k4v) == 1 == abs(u_g)]
                # ok: !! [abs(k4v) <= 1 == abs(u_g)]
            * [abs(v_g) >= 2]:
                !! [abs(v/u) == abs(v_g)]
                [abs(u/v) == 1/abs(v/u) == 1/abs(v_g) <= 1/2]
                !! [u =!= 0]
                [0 < abs(u/v) <= 1/2 < 1]
                [-1 <= u//v <= 0]
                [[u//v == 0] <-> [(u<0) == (v<0)]]
                [[u//v == -1] <-> [(u<0) =!= (v<0)]]
                * [u//v == 0]:
                    [cf_digits==[0;v/u]]
                    [sts==(0,1;1,0;0,1;1,v/u)]
                    [[num_steps == 2][prevN == 0][prevD == 1][currN == 1][currD == v/u]]
                    !! [[abs(u_g) == abs(currN)][abs(v_g) == abs(currD)][abs(k4u) == abs(prevD)][abs(k4v) == abs(prevN)]]
                    [[abs(u_g) == 1][abs(v_g) == v/u][abs(k4u) == 1][abs(k4v) == 0]]
                    [k4v == 0]
                    [k4u == (-1)**[u<0]]
                    [0 == abs(k4v) < abs(u_g) == 1]
                    # ok: !! [abs(k4v) <= 1 == abs(u_g)]

                * [u//v == -1]:
                    [v/u < 0]
                    * [abs(v_g) == 2]:
                        [v/u == -2]
                        [u/v == -1/2]
                        [u/v
                        == -1 + (u+v)/v
                        == -1 + 1/(v/(u+v))
                        == -1 + 1/2
                        ]
                        [cf_digits==[-1;2]]
                        [sts==(0,1;1,0;-1,1;-1,2)] # [2 == -v/u]
                        [[num_steps == 2][prevN == -1][prevD == 1][currN == -1][currD == 2 == -v/u]]
                        !! [[abs(u_g) == abs(currN)][abs(v_g) == abs(currD)][abs(k4u) == abs(prevD)][abs(k4v) == abs(prevN)]]
                        [[abs(u_g) == 1][abs(v_g) == 2 == -v/u][abs(k4u) == 1][abs(k4v) == 1]]
                        [k4v == (-1)**[v<0]]
                        [k4u == -(-1)**[u<0]]
                        [abs(k4v) == 1 == abs(u_g)]
                        # ok: !! [abs(k4v) <= 1 == abs(u_g)]
                    * [abs(v_g) >= 3]:
                        [v/u <= -3]
                        [-1/3 <= u/v < 0]
                        [u/v
                        == -1 + (u+v)/v
                        == -1 + 1/(v/(u+v))
                        !! [(v/(u+v)) == abs(v_g)/(-1+abs(v_g)) == 1 + 1/(-1+abs(v_g))]
                        == -1 + 1/(1 + 1/(-1+abs(v_g)))
                        == -1 + 1/(1 + 1/(-1-v/u))
                        ]
                        !! [v/u <= -3]
                        [(-1-v/u) >= 2]
                        [cf_digits==[-1;1,-1-v/u]]
                        [sts==(0,1;1,0;-1,1;0,1;-1,-v/u)]
                        [[num_steps == 3][prevN == 0][prevD == 1][currN == -1][currD == -v/u]]
                        !! [[abs(u_g) == abs(currN)][abs(v_g) == abs(currD)][abs(k4u) == abs(prevD)][abs(k4v) == abs(prevN)]]
                        [[abs(u_g) == 1][abs(v_g) == -v/u][abs(k4u) == 1][abs(k4v) == 0]]
                        [k4v == 0]
                        [k4u == (-1)**[u<0]]
                        [0 == abs(k4v) < abs(u_g) == 1]
                        # ok: !! [abs(k4v) <= 1 == abs(u_g)]

        * [abs(u_g)>=2]:
            [abs(k4v)
            <= (1-abs(u_g))/abs(v_g) + abs(u_g)
            < abs(u_g)
            ]
            [abs(k4v) < abs(u_g)]
        #=>>:
        * [abs(u_g)==0]:
            [[abs(u_g) == 0][abs(v_g) == 1][abs(k4u) == 0][abs(k4v) == 1]]
            [1 == abs(k4v) > abs(u_g) == 0]
                #abs_k4v__gt__abs_u_g
        * [abs(u_g)==1]:
            * [abs(v_g) == 1]:
                [[abs(u_g) == 1][abs(v_g) == 1][abs(k4u) == 0][abs(k4v) == 1]]
                [abs(k4v) == 1 == abs(u_g)]
                    #abs_k4v__eq__abs_u_g
            * [abs(v_g) >= 2]:
                [[u//v == 0] <-> [(u<0) == (v<0)]]
                [[u//v == -1] <-> [(u<0) =!= (v<0)]]
                * [u//v == 0]:
                    [[abs(u_g) == 1][abs(v_g) == v/u >= 2][abs(k4u) == 1][abs(k4v) == 0]]
                    [k4v == 0]
                    [k4u == (-1)**[u<0]]
                    [0 == abs(k4v) < abs(u_g) == 1]
                        #abs_k4v__lt__abs_u_g
                * [u//v == -1]:
                    * [abs(v_g) == 2]:
                        [[abs(u_g) == 1][abs(v_g) == 2 == -v/u][abs(k4u) == 1][abs(k4v) == 1]]
                        [k4v == (-1)**[v<0]]
                        [k4u == -(-1)**[u<0]]
                        [abs(k4v) == 1 == abs(u_g)]
                            #abs_k4v__eq__abs_u_g
                    * [abs(v_g) >= 3]:
                        [[abs(u_g) == 1][abs(v_g) == -v/u >= 3][abs(k4u) == 1][abs(k4v) == 0]]
                        [k4v == 0]
                        [k4u == (-1)**[u<0]]
                        [0 == abs(k4v) < abs(u_g) == 1]
                            #abs_k4v__lt__abs_u_g
        * [abs(u_g)>=2]:
            [abs(k4v) < abs(u_g)]
                #abs_k4v__lt__abs_u_g
        #=>>:
        #完全穷举反转推导法:goto
        #abs_k4v__gt__abs_u_g
        #abs_k4v__lt__abs_u_g
        #abs_k4v__eq__abs_u_g
        !! [[u == 0] <-> [u_g==0]]
        [[abs(k4v) > abs(u_g)]
        <-> [abs(u_g)==0]
        <-> [u==0]
        ]
        [[abs(k4v) == abs(u_g)]
        <-> [abs(k4v) == 1 == abs(u_g)]
        <-> [abs(u_g)==1][
            [abs(v_g) == 1]
            or[[abs(v_g) >= 2][u//v == -1][abs(v_g) == 2]]
            ]
        !! [[u//v == -1] <-> [(u<0) =!= (v<0)]]
        <-> [abs(u_g)==1][
            [abs(v_g) == 1]
            or[[abs(v_g) == 2][(u<0) =!= (v<0)]]
            ]
        ]
        [[abs(k4v) < abs(u_g)]
        <-> [[abs(u_g)>=2]
            or[[abs(u_g)==1][abs(v_g) >= 2][
                [u//v == 0]
                or[[u//v == -1][abs(v_g) >= 3]]
                ]]
            ]
        !! [[u//v == -1] <-> [(u<0) =!= (v<0)]]
        !! [[u//v == 0] <-> [(u<0) == (v<0)]]
        <-> [[abs(u_g)>=2]
            or[[abs(u_g)==1][abs(v_g) >= 2][
                [(u<0) == (v<0)]
                or[abs(v_g) >= 3]
                ]]
            ]
        ]
        #=>>:
        [[abs(k4v) > abs(u_g)]
        <-> [abs(u_g)==0]
        <-> [u==0]
        <-> [1 == abs(k4v) > abs(u_g) == 0]
        <-> [[abs(u_g) == 0][abs(v_g) == 1][abs(k4u) == 0][abs(k4v) == 1]]
        <-> [0 == u == u_g == k4u < abs(v_g) == abs(k4v) == 1]
        ]
        [[abs(k4v) == abs(u_g)]
        <-> [abs(k4v) == 1 == abs(u_g)]
        <-> [[abs(u_g)==1][[abs(v_g) == 1]or[[abs(v_g) == 2][(u<0) =!= (v<0)]]]]

        <-> [[[abs(u_g) == 1][abs(v_g) == 1][abs(k4u) == 0][abs(k4v) == 1]]or[[abs(u_g) == 1][abs(v_g) == 2][abs(k4u) == 1][abs(k4v) == 1]]]
        <-> [abs(k4v) == abs(u_g) == 1 >= abs(k4u) == abs(v_g) -1]
        ]
        [[abs(k4v) < abs(u_g)]
        <-> [[abs(u_g)>=2]or[[abs(u_g)==1][abs(v_g) >= 2][[(u<0) == (v<0)]or[abs(v_g) >= 3]]]]
        <-> [[abs(u_g)>=2]or[0 == abs(k4v) < abs(u_g) == 1]]
        <-> [[abs(u_g)>=2]or[[0 == abs(k4v) < abs(u_g) == 1 == abs(k4u)][[abs(v_g) == v/u >= 2]or[abs(v_g) == -v/u >= 3]]]]
        <-> [[abs(u_g)>=2]or[0 == abs(k4v) < abs(u_g) == 1 == abs(k4u) < abs(v_g) >= 2+[(u<0) =!= (v<0)]]]
        ]
        #=>>:
        [[abs(k4v) > abs(u_g)]
        <-> [u==0]
        <-> [0 == u == u_g == k4u < abs(v_g) == abs(k4v) == 1]
        ]
        [[abs(k4v) == abs(u_g)]
        <-> [[abs(u_g)==1][[abs(v_g) == 1]or[[abs(v_g) == 2][(u<0) =!= (v<0)]]]]
        <-> [abs(k4v) == abs(u_g) == 1 >= abs(k4u) == abs(v_g) -1]
        ]
        [[abs(k4v) < abs(u_g)]
        <-> [[abs(u_g)>=2]or[[abs(u_g)==1][abs(v_g) >= 2][[(u<0) == (v<0)]or[abs(v_g) >= 3]]]]
        <-> [[abs(u_g)>=2]or[0 == abs(k4v) < abs(u_g) == 1 == abs(k4u) < abs(v_g) >= 2+[(u<0) =!= (v<0)]]]
        ]
        #=>>:
        #final output:
        [[abs(k4v) > abs(u_g)] <-> [u==0] <-> [0 == u == u_g == k4u < abs(v_g) == abs(k4v) == 1]]
        [[abs(k4v) == abs(u_g)] <-> [[abs(u_g)==1][[abs(v_g) == 1]or[[abs(v_g) == 2][(u<0) =!= (v<0)]]]] <-> [abs(k4v) == abs(u_g) == 1 >= abs(k4u) == abs(v_g) -1]]
        [[abs(k4v) < abs(u_g)] <-> [[abs(u_g)>=2]or[[abs(u_g)==1][abs(v_g) >= 2][[(u<0) == (v<0)]or[abs(v_g) >= 3]]]] <-> [[abs(u_g)>=2]or[0 == abs(k4v) < abs(u_g) == 1 == abs(k4u) < abs(v_g) >= 2+[(u<0) =!= (v<0)]]]]

    ]]] #end:[v =!= 0]

    #=>>:
    # [v_ne_0____abs_k4v__cmp__abs_u_g]:here
    [[v =!= 0] -> [[abs(k4v) > abs(u_g)] <-> [u==0] <-> [0 == u == u_g == k4u < abs(v_g) == abs(k4v) == 1]]]
    [[v =!= 0] -> [[abs(k4v) == abs(u_g)] <-> [[abs(u_g)==1][[abs(v_g) == 1]or[[abs(v_g) == 2][(u<0) =!= (v<0)]]]] <-> [abs(k4v) == abs(u_g) == 1 >= abs(k4u) == abs(v_g) -1]]]
    [[v =!= 0] -> [[abs(k4v) < abs(u_g)] <-> [[abs(u_g)>=2]or[[abs(u_g)==1][abs(v_g) >= 2][[(u<0) == (v<0)]or[abs(v_g) >= 3]]]] <-> [[abs(u_g)>=2]or[0 == abs(k4v) < abs(u_g) == 1 == abs(k4u) < abs(v_g) >= 2+[(u<0) =!= (v<0)]]]]]
    #=>>:
    [[v =!= 0] -> [[abs(k4v) < abs(u_g)]or[abs(k4v) == 1 == abs(u_g)]or[abs(k4v) == 1 > 0 == abs(u_g)]]]
    # [[v =!= 0] -> [[u =!= 0] <-> [abs(k4v) <= abs(u_g)]]]

    !! [[gcd_of_uv =!= 0] -> [[abs(u_g) <= abs(u)][abs(v_g) <= abs(v)]]]
    !! [[gcd_of_uv == 0] <-> [u==0==v]]
    [[v =!= 0] -> [[abs(u_g) <= abs(u)][abs(v_g) <= abs(v)]]]

    !! [[v == 0] -> [[gcd_of_uv == abs(u)][k4u == u_g == (-1)**[u < 0]][k4v == v_g == 0]]]
    [[v == 0] -> [k4v == 0 == v_g]]
    !! [[v =!= 0] -> [[abs(k4v) < abs(u_g)]or[abs(k4v) == 1 == abs(u_g)]or[abs(k4v) == 1 > 0 == abs(u_g)]]]
    !! [[v =!= 0] -> [[abs(u_g) <= abs(u)][abs(v_g) <= abs(v)]]]
    [[k4v == 0 == v_g] if v==0 else [[[abs(k4v) < abs(u_g)]or[abs(k4v) == 1 == abs(u_g)]or[abs(k4v) == 1 > 0 == abs(u_g)]][abs(u_g) <= abs(u)]]]

    #]]]'''#'''

    r'''[[[
    to findout condition for:
        [[???] <-> [coprime(u,v)][k4u < 0]]

    [prevD == 0]
        <==> [num_steps == 1]
        !! [num_steps := len(cf_digits)]
        <==> [len(cf_digits) == 1]
        <==> [v =!= 0][u%v == 0]

    !! [prevD >= 0]
    !! [k4u == -prevD if if g_ < 0 else +prevD]
    [k4u < 0]
        <==> [prevD > 0][g_ < 0]
        <==> [prevD =!= 0][g_ < 0]
        <==> [not [[v =!= 0][u%v == 0]]][g_ < 0]
        <==> [[v == 0] or [u%v =!= 0]][g_ < 0]
        <==> [[v == 0] or [u%v =!= 0]][sign_of(g_) == -1]
            # sign_of :: real -> [-1,0,+1]

    !! [g_ := -g if num_steps&1 else g]
    [sign_of(g_) == sign_of(g)*(-1)**num_steps]

    !! [currD >= 0]
    [[v < 0] == [(v < 0) xor (currD < 0)]]
    !! [g := 0 if [u==0==v] else ((-gcd_of_uv if v < 0 else gcd_of_uv) if [v=!=0] else (-gcd_of_uv if (u < 0) xor (currN < 0) else gcd_of_uv))]
    !! [gcd_of_uv >= 0]
    [sign_of(g) == sign_of(gcd_of_uv)*(-1)**([v < 0] or [v==0][(u < 0) xor (currN < 0)])]

    [sign_of(g) == sign_of(gcd_of_uv)*(-1)**([v=!=0][(v < 0) xor (currD < 0)] or [u=!=0][(u < 0) xor (currN < 0)])]
        !! [[gcd_of_uv == 0] <-> [u==0==v]]

    [v == 0]
        <==> [num_steps == 0]
        !! [num_steps := len(cf_digits)]
        <==> [len(cf_digits) == 0]
        <==> [currN == 1][currD == 0]
    [[[v==0][(u < 0) xor (currN < 0)]] <-> [[v==0][u < 0]]]

    [sign_of(g)
    == sign_of(gcd_of_uv)*(-1)**([v < 0] or [v==0][(u < 0) xor (currN < 0)])
    == sign_of(gcd_of_uv)*(-1)**([v < 0] or [v==0][u < 0])
    ]

    [sign_of(g) == sign_of(gcd_of_uv)*(-1)**([v < 0] or [v==0][u < 0])]

    [k4u < 0]
        <==> [[v == 0] or [u%v =!= 0]][sign_of(g_) == -1]
        !! [sign_of(g_) == sign_of(g)*(-1)**num_steps]
        <==> [[v == 0] or [u%v =!= 0]][sign_of(g)*(-1)**num_steps == -1]
        <==> [[v == 0] or [u%v =!= 0]][sign_of(g) == -(-1)**num_steps]
        !! [sign_of(g) == sign_of(gcd_of_uv)*(-1)**([v < 0] or [v==0][u < 0])]
        <==> [[v == 0] or [u%v =!= 0]][sign_of(gcd_of_uv)*(-1)**([v < 0] or [v==0][u < 0]) == -(-1)**num_steps]
        !! [[gcd_of_uv == 0] <-> [u==0==v]]
        !! [gcd_of_uv >= 0]
        <==> [[v == 0] or [u%v =!= 0]][u=!=0][(-1)**([v < 0] or [v==0][u < 0]) == -(-1)**num_steps]
        <==> [[[v == 0][u=!=0]] or [v=!=0][u%v =!= 0]][(-1)**([v < 0] or [v==0][u < 0]) == -(-1)**num_steps]
        <==> [[[v == 0][u=!=0][(-1)**([v < 0] or [v==0][u < 0]) == -(-1)**num_steps]] or [[v=!=0][u%v =!= 0][(-1)**([v < 0] or [v==0][u < 0]) == -(-1)**num_steps]]]
        <==> [[[v == 0][u=!=0][(-1)**([u < 0]) == -(-1)**num_steps]] or [[v=!=0][u%v =!= 0][(-1)**([v < 0]) == -(-1)**num_steps]]]
        <==> [[[v == 0][u=!=0][[u < 0] == [num_steps%2==0]]] or [[v=!=0][u%v =!= 0][[v < 0] == [num_steps%2==0]]]]
        <==> let [even := [num_steps%2==0]] in [[[v == 0][u=!=0][[u < 0] == even]] or [[v=!=0][u%v =!= 0][[v < 0] == even]]]
        !! [num_steps := len(cf_digits)]
        !! [cf_digits := cf_digits5ND_(u,v)]
        <==> let [even := [len(cf_digits5ND_(u,v))%2==0]] in [[[v == 0][u=!=0][[u < 0] == even]] or [[v=!=0][u%v =!= 0][[v < 0] == even]]]
        !! [[v == 0] <-> [num_steps == 0]]
        #  [[v == 0] -> [even == 1]]
        <==> let [even := [len(cf_digits5ND_(u,v))%2==0]] in [[[v == 0][u < 0]] or [[v=!=0][u%v =!= 0][[v < 0] == even]]]

    [[even := [len(cf_digits5ND_(u,v))%2==0]] -> [[k4u < 0] <-> [[[v == 0][u < 0]] or [[v=!=0][u%v =!= 0][[v < 0] == even]]]]]
        # not require [gcd_of_uv==1]

    [[even := [len(cf_digits5ND_(u,v))%2==0]] -> [[[1==gcd(u,v)][k4u < 0]] <-> [[[v == 0][u == -1]] or [[1==gcd(u,v)][v=!=0][u=!=0][[v < 0] == even]]]]]
        # [coprime(u,v)] inside (<->)

    [[even := [len(cf_digits5ND_(u,v))%2==0]] -> [1==gcd(u,v)] -> [[k4u < 0] <-> [[[v == 0][u == -1]] or [[v=!=0][u=!=0][[v < 0] == even]]]]]
        # [coprime(u,v)] outside (<->)
        # [condition____k4u__lt__0]:here

    #]]]'''#'''


    #if not gcd_of_uv == 0:

    # * [gcd_of_uv =!= 0]:
        # !! [k4u*u +k4v*v == gcd_of_uv]
        # !! [gcd_of_uv =!= 0]
        # [k4u*u/gcd_of_uv +k4v*v/gcd_of_uv == 1]
        # !! [[u_g*gcd_of_uv == u][v_g*gcd_of_uv == v]]
        # [k4u*u_g +k4v*v_g == 1]
        # [1 == gcd(u_g, v_g)]
    # * [gcd_of_uv == 0]:
        # [u == 0 == v]
        # [prevN == 0][prevD == 1] #<<== st0
        # [currN == 1][currD == 0] #<<== st0
        # [u_g == currN == 1][v_g == currD == 0]
        # [k4u == +prevD == 1][k4v == -prevN == 0]
        # [k4u*u_g +k4v*v_g == 1]
        # [1 == gcd(u_g, v_g)]
    # [k4u*u_g +k4v*v_g == 1]
    # [1 == gcd(u_g, v_g)]




    #########postcondition:
    # [[gcd_of_uv == 0] <-> [u==0==v]]
    # [[sign_of(u_g) =!= sign_of(u)] <-> [u==0==v]]
    # [sign_of(v_g) == sign_of(v)]
    # [[abs(k4u) == 1] if v==0 else [abs(k4u) < abs(v_g) <= abs(v)]]
    # [[k4v == 0 == v_g] if v==0 else [[[abs(k4v) < abs(u_g)]or[abs(k4v) == 1 == abs(u_g)]or[abs(k4v) == 1 > 0 == abs(u_g)]][abs(u_g) <= abs(u)]]]
    # [[v == 0] -> [[gcd_of_uv == abs(u)][k4u == u_g == (-1)**[u < 0]][k4v == v_g == 0]]]
    #
    # [[v =!= 0] -> [[u =!= 0] <-> [abs(k4v) <= abs(u_g)]]]
    #
    # [v_ne_0____abs_k4v__cmp__abs_u_g]:goto
    # [[v =!= 0] -> [[abs(k4v) > abs(u_g)] <-> [u==0] <-> [0 == u == u_g == k4u < abs(v_g) == abs(k4v) == 1]]]
    # [[v =!= 0] -> [[abs(k4v) == abs(u_g)] <-> [[abs(u_g)==1][[abs(v_g) == 1]or[[abs(v_g) == 2][(u<0) =!= (v<0)]]]] <-> [abs(k4v) == abs(u_g) == 1 >= abs(k4u) == abs(v_g) -1]]]
    # [[v =!= 0] -> [[abs(k4v) < abs(u_g)] <-> [[abs(u_g)>=2]or[[abs(u_g)==1][abs(v_g) >= 2][[(u<0) == (v<0)]or[abs(v_g) >= 3]]]] <-> [[abs(u_g)>=2]or[0 == abs(k4v) < abs(u_g) == 1 == abs(k4u) < abs(v_g) >= 2+[(u<0) =!= (v<0)]]]]]
    #
    #
    #
    #
    # [k4u*u +k4v*v == gcd_of_uv >= 0]
    # [[u_g*gcd_of_uv == u][v_g*gcd_of_uv == v]
    # [k4u*u_g +k4v*v_g == 1]
    #
    # [[even := [len(cf_digits5ND_(u,v))%2==0]] -> [[k4u < 0] <-> [[[v == 0][u < 0]] or [[v=!=0][u%v =!= 0][[v < 0] == even]]]]]
    #
    # [abs(k4u) == prevD]
    # [abs(k4v) == abs(prevN)]
    #
    #
    if 1:
        assert abs(k4u) == prevD >= 0
        assert abs(k4v) == abs(prevN)
    if 1:
        even = (num_steps%2 == 0)
        assert (k4u < 0) is ((u < 0) if v == 0 else (not (u%v) == 0 and (v < 0) == even))

    if 0:
        assert (gcd_of_uv == 0) is (u==0==v)
        assert ((not sign_of(u_g) == sign_of(u)) is (u==0==v))
        assert (sign_of(v_g) == sign_of(v))
        assert (abs(k4u) == 1) if v==0 else (abs(k4u) < abs(v_g) <= abs(v))
        assert (k4v == 0 == v_g) if v==0 else ((abs(k4v) < abs(u_g) or abs(k4v) == 1 == abs(u_g) or (abs(k4v) == 1 > 0 == abs(u_g))) and abs(u_g) <= abs(u))
        assert not v == 0 or (gcd_of_uv == abs(u) and k4u == u_g == (-1)**(u < 0) and k4v == v_g == 0)


        assert v == 0 or ((not u == 0) is (abs(k4v) <= abs(u_g)))


        r'''[[[
        #补偿:[((
        .,.+5s/\[/(/g
        .,.+5s/\]/)/g
        .,.+5s/<->/is/g
        .,.+5s/)(/) and (/g
        .,.+5s/=!=/is not/g
        #补偿:))]
        #]]]'''#'''
        #assert v == 0 or ((abs(k4v) > abs(u_g)) is ((k4u == u_g == u == 0) and (k4v == v_g == (-1)**(v<0))) is (u==0))

        # [v_ne_0____abs_k4v__cmp__abs_u_g]:goto
        assert v == 0 or ((abs(k4v) > abs(u_g)) is (u==0) is (0 == u == u_g == k4u < abs(v_g) == abs(k4v) == 1))
        assert v == 0 or ((abs(k4v) == abs(u_g)) is ((abs(u_g)==1) and ((abs(v_g) == 1)or((abs(v_g) == 2) and ((u<0) is not (v<0))))) is (abs(k4v) == abs(u_g) == 1 >= abs(k4u) == abs(v_g) -1))
        assert v == 0 or ((abs(k4v) < abs(u_g)) is ((abs(u_g)>=2)or((abs(u_g)==1) and (abs(v_g) >= 2) and (((u<0) == (v<0))or(abs(v_g) >= 3)))) is ((abs(u_g)>=2)or(0 == abs(k4v) < abs(u_g) == 1 == abs(k4u) < abs(v_g) >= 2+((u<0) is not (v<0)))))



        assert k4u*u +k4v*v == gcd_of_uv >= 0
        assert u_g*gcd_of_uv == u
        assert v_g*gcd_of_uv == v
        assert k4u*u_g +k4v*v_g == 1
    else:
        validate__gcd_certification_(u, v, k4u, k4v, gcd_of_uv, u_g, v_g)
    return (u, v, k4u, k4v, gcd_of_uv, u_g, v_g)
#end-def mk_gcd_certification_(u, v, /):

def _iter_uv_pairs4test_(max4uv, /):
    us = vs = range(-max4uv, max4uv+1)
    for u in us:
        for v in vs:
            yield u, v
def _test____inv_mod_(max4uv, /):
    for u, v in _iter_uv_pairs4test_(max4uv):
        M = v
        x = u
        try:
            inv_x = inv_mod_(M, x)
            validate__inv_mod_(M, x, inv_x)
            if not gcd(u,v) == 1: raise logic-err
            if M == 0: raise logic-err
        except NotCoprimeError:
            if not (gcd(u,v) >= 2 or u==v==0==gcd(u,v)): raise logic-err
            if M == 0: raise logic-err
        except ZeroDivisionError:
            if not M == 0: raise logic-err
def _test____mk_coprime_certification_(max4uv, /):
    for u, v in _iter_uv_pairs4test_(max4uv):
        try:
            (u, v, k4u, k4v) = mk_coprime_certification_(u, v)
            validate__coprime_certification_(u, v, k4u, k4v)
            if not gcd(u,v) == 1: raise logic-err
        except NotCoprimeError:
            if not (gcd(u,v) >= 2 or u==v==0==gcd(u,v)): raise logic-err
def _test____mk_gcd_certification_(max4uv, /):
    for u, v in _iter_uv_pairs4test_(max4uv):
        (u, v, k4u, k4v, gcd_of_uv, u_g, v_g) = mk_gcd_certification_(u, v)
        validate__gcd_certification_(u, v, k4u, k4v, gcd_of_uv, u_g, v_g)


#from seed.math.continued_fraction.continued_fraction5ND import iter_continued_fraction_digits_ex5ND_, continued_fraction_digits_ex5ND_, iter_continued_fraction_digits5ND_



class BadDataFormatError(Exception):pass

def backward_iter_cf_steps_(prevN, prevD, currN, currD, /):
#def backward_iter_cf_KNDs(prevN, prevD, currN, currD, /):
    '-> back iter (cf_st, cf_digit, currND) |^BadDataFormatError'
    for K in backward_iter_cf_digits_(prevN, prevD, currN, currD):
        N__ = currN - K*prevN
        D__ = currD - K*prevD
        cf_st = (N__, D__, prevN, prevD)
        currND = (currN, currD)
        yield cf_st, K, currND
        #####next round:
        prevN, prevD, currN, currD = N__, D__, prevN, prevD
    if not (prevN, prevD, currN, currD) == (0,1,1,0):raise logic-err#BadDataFormatError
    return
def _check_args(prevN, prevD, currN, currD, /):
    '-> None|^TypeError|^BadDataFormatError'
    #check_uint(prevN)
    #check_uint(currN)
    check_type_is(int, prevN)
    check_type_is(int, currN)
    check_uint(prevD)
    check_uint(currD)
    #[连分数渐近分数囗互素关联]:goto
    #   --> update:_check_args()
    # [@[cf_digits :: [int; pint*]] -> @[num_steps :<- [0..=len(cf_digits)]] -> [(prevN, prevD; currN, currD) := steps_(cf_digits; num_steps)] -> [currN*prevD -prevN*currD == (-1)**num_steps]]
    if not 1 == abs(currN*prevD -prevN*currD): raise BadDataFormatError('not [1 == abs(currN*prevD -prevN*currD)]')#TypeError#ValueError

def backward_iter_cf_digits_(prevN, prevD, currN, currD, /):
    '-> back-Iter cf_digit |^BadDataFormatError'
    _check_args(prevN, prevD, currN, currD)
        # ^TypeError|^BadDataFormatError

    # [prevD >= 0]
    # [currD >= 0]
    if currD == 0:
        # no cf0
        #curr:eq-new0 起始配置
        if not prevN == 0:raise BadDataFormatError
        if not prevD == 1:raise BadDataFormatError
        if not currN == 1:raise BadDataFormatError
        if not currD == 0:raise BadDataFormatError
        pass
        return
    # [currD >= 1]
    #curr:ge-new1


    # !! [[currD=!=0] -> [cf0 == currN//currD]]
    cf0 = currN//currD
    #[initial_cf_table]:goto
    a = cf0
    if prevD == 0:
        #curr:eq-new1
        if not prevN == 1:raise BadDataFormatError
        if not prevD == 0:raise BadDataFormatError
        if not currN == a:raise BadDataFormatError
        if not currD == 1:raise BadDataFormatError
        yield a
        return
    # [prevD >= 1]

    # [prevD >= 1][currD >= 1]
    #curr:ge-new2
    while 1:
        # [prevD >= 1][currD >= 1]
        #curr:ge-new2
        # [[[prevD==1][currN==1+prevN*currD]] <-> [curr eq new2]]
        # [[curr ge new1] -> [[(prevN,prevD)==(cf0,1)] <-> [curr eq new2]]]
        if (prevN,prevD)==(cf0,1):
            #curr:eq-new2
            a = prevN
            b = currD
            if not currN == 1+a*b:raise BadDataFormatError
            yield b
            yield a
            return
        #curr:ge-new3
        if not currD > prevD:raise BadDataFormatError

        if prevD == 1:
            #curr:eq-new3 && b==1
            b = 1
            # [currD<new3> == 1+b*c]
            c = currD-1
            if not c >= 1:raise BadDataFormatError
            if not prevN == 1+a*b:raise BadDataFormatError
            if not currN == a+c+a*b*c:raise BadDataFormatError
            yield c
            yield b
            yield a
            return
        # [currD > prevD >= 2]
        # [curr:eq-new3 && b>=2][curr:ge-new4]
        # [分母反推公式@ge-new4/@new3-if-b>=2]:goto
        (K, D__) = divmod(currD, prevD)
            # !! [currD > prevD >= 2]
            # [K > 1]
        if not D__ >= 1:raise BadDataFormatError
        # [D__ >= 1]
        N__ = currN -K*prevN
            # [N__ :: int]
        yield K
        #curr:ge-new3
        # [currD > prevD >= 2]
        # [D__ >= 1]
        #####next round:
        #curr:ge-new2
        # [D__ >= 1][prevD >= 1]
        prevN, prevD, currN, currD = N__, D__, prevN, prevD
        # [prevD >= 1][currD >= 1]
    return

def __backward_iter_cf_digits_(prevN, prevD, currN, currD, /):
    '[precondition:[cf0>=1]]:-> back-Iter cf_digit |^BadDataFormatError'
    _check_args(prevN, prevD, currN, currD)
    def f():
        #curr:le-new2
        prev = prevN, prevD
        curr = currN, currD
        #data = (*prev, *curr)
        if prevN == 0:
            #curr:eq-new0 起始配置
            if not prev == (0,1):raise BadDataFormatError
            if not curr == (1,0):raise BadDataFormatError
            pass
        elif prevD == 0:
            #curr:eq-new1
            if not prev == (1,0):raise BadDataFormatError
            if not currD == 1:raise BadDataFormatError
            if not currN >= 1:raise BadDataFormatError
            a = currN
            yield a
        else:
            #curr:eq-new2
            if not prevD == 1:raise BadDataFormatError
            if not prevN >= 1:raise BadDataFormatError
            if not currD >= 1:raise BadDataFormatError
            a = prevN
            b = currD
            if not currN == 1+a*b:raise BadDataFormatError
            yield b
            yield a
        return
    #[initial_cf_table]:goto
    if prevN < 2:
        #curr:le-new2
        yield from f()
        return
    #curr:ge-new3
    # precondition:[cf0>0] => [分子反推公式@ge-new3]:goto
        # [currN__new == currN__new__new__new%currN__new__new]
        # [K == currN__new__new__new//currN__new__new]
    while 1:
        #curr:ge-new3
        if not prevN >= 2:raise BadDataFormatError
        if not prevD >= 1:raise BadDataFormatError
        if not currN > prevN:raise BadDataFormatError
        if not currD > prevD:raise BadDataFormatError

        (K, N__) = divmod(currN, prevN)
        # [K >= 1] <<== [currN > prevN]
        if not N__ >= 1:raise BadDataFormatError
        if 1+N__*prevD == prevN:
            #curr:eq-new3
            a = N__
            b = prevD
            c = K
            if not currD == 1+b*c:raise BadDataFormatError
            yield c
            yield b
            yield a
            return
        #curr:ge-new4
        # [分母反推公式@ge-new4]:goto
            # [currD__new__new == currD__new__new__new__new%currD__new__new__new]
            # [K == currD__new__new__new__new//currD__new__new__new]
        (K2, D__) = divmod(currD, prevD)
        if not D__ >= 1:raise BadDataFormatError
        if not K2 == K:raise BadDataFormatError
        yield K

        #curr:ge-new4
        #####next round:
        #curr:ge-new3
        prevN, prevD, currN, currD = N__, D__, prevN, prevD
    raise 000
#end-def backward_iter_cf_digits_(prevN, prevD, currN, currD, /):




_attr_nms = r'''
    prevN
    prevD
    currN
    currD
    '''.split()#'''

class ContinuedFractionFoldState:
    #def __init__(sf, prevN, prevD, currN, currD, /, *, validate_completely_by_reproduct=False):
    def __new__(cls, prevN, prevD, currN, currD, /, *, validate_completely_by_reproduct=False):
        'see:from_currND()'
        _check_args(prevN, prevD, currN, currD)
        ########mk sf:
        sf = super(__class__, cls).__new__(cls)
        ########init sf:
        set_NamedReadOnlyProperty4sf_(sf, _attr_nms, locals())
        ########check sf:
        if validate_completely_by_reproduct:
            sf.validate_completely_by_reproduct()
        ########return sf:
        try:
            continued_fraction_fold_state0
        except NameError:
            # continued_fraction_fold_state0 is fst instance
            if not cls is __class__:raise logic-err
            if not sf.get_args() == (0,1,1,0):raise logic-err
            pass
        else:
            if cls is __class__ and sf == continued_fraction_fold_state0:
                sf = continued_fraction_fold_state0
        return sf
    def validate_completely_by_reproduct(sf, /):
        'see:list_cf_steps__separately_()'
        if not sf == type(sf).from_currND(*sf.get_currND()): raise BadDataFormatError
    @classmethod
    def from_currND(cls, currN, currD, /):
        'currN -> currD -> sf'
        N, D = currN, currD
        if (N,D) == (1,0):
            sf = continued_fraction_fold_state0
        else:
            cf_digits = iter_continued_fraction_digits5ND_(N, D)
            sf = continued_fraction_fold_state0.steps_(cf_digits)
        if not (N,D) == sf.get_currND():raise logic-err
        return sf
    def get_args(sf, /):
        return (sf.prevN, sf.prevD, sf.currN, sf.currD)
    def get_prevND(sf, /):
        return (sf.prevN, sf.prevD)
    def get_currND(sf, /):
        return (sf.currN, sf.currD)
    def get_prev_floor(sf, /):
        return (sf.prevN // sf.prevD)
    def get_curr_floor(sf, /):
        return (sf.currN // sf.currD)
    def get_prev_fraction(sf, /, *, _normalize=True):
        '-> Fraction|^ZeroDivisionError'
        return Fraction(*sf.get_prevND(), _normalize=_normalize)
    def get_curr_fraction(sf, /, *, _normalize=True):
        '-> Fraction|^ZeroDivisionError'
        return Fraction(*sf.get_currND(), _normalize=_normalize)
    def __repr__(sf, /):
        args = sf.get_args()
        return repr_helper(sf, *args)
    def __hash__(sf, /):
        args = sf.get_args()
        return hash((type(sf), args))
    def __eq__(sf, ot, /):
        return sf is ot or (type(sf) is type(ot) and sf.get_args() == ot.get_args())

    def steps_until_denominator_overflow_(sf, max1_denominator, Ks, /):
        '-> (overflow, cf_st)'
        for overflow, st in sf.iter_steps_until_denominator_overflow_(max1_denominator, Ks):
            # at least one output
            pass
        return overflow, st
    def iter_steps_until_denominator_overflow_(sf, max1_denominator, Ks, /):
        '-> (Iter (overflow, cf_st)){.len>=1}'
        check_type_is(int, max1_denominator)
        overflow = False
        for st in sf.iter_steps_(Ks):
            if not st.currD < max1_denominator:
                overflow = True
                yield overflow, st
                break
            yield overflow, st
        return


    def steps_(sf, Ks, /):
        'sf -> Ks/Iter cf_digit -> final-ContinuedFractionFoldState'
        for st in sf.iter_steps_(Ks):
            # at least one output
            pass
        return st
    def iter_steps_(sf, Ks, /):
        'sf -> Ks/Iter cf_digit -> (Iter ContinuedFractionFoldState){.len>=1}{fst==sf}'
        st = sf
        yield st
        for K in Ks:
            st = st.step_(K)
            yield st
        return
    def step_(sf, K, /, *, all_int_ok=False):
        'sf -> K/cf_digit -> next-ContinuedFractionFoldState'
        if all_int_ok or sf == continued_fraction_fold_state0:
            check_type_is(int, K)
        else:
            check_int_ge(1, K)

        (prevN, prevD, currN, currD) = sf.get_args()
        prevN__new = currN
        prevD__new = currD
        currN__new = (prevN+currN*K)
        currD__new = (prevD+currD*K)
        return __class__(prevN__new, prevD__new, currN__new, currD__new)
    def iter_cf_digits_(sf, /):
        '-> Iter K/cf_digit|^BadDataFormatError'   '  #see: .backward_iter_cf_digits_()'
        if sf.currD==0:
            if not sf == continued_fraction_fold_state0:raise BadDataFormatError(sf)#ValueError(sf)
            # [no cf0]
            pass # [cf([]) === +oo]
            return
        return iter_continued_fraction_digits5ND_(*sf.get_currND())
    def backward_iter_cf_digits_(sf, /):
        '-> back-iter K/cf_digit|^BadDataFormatError'   '  #see: .iter_cf_digits_()'
        it = backward_iter_cf_digits_(*sf.get_args())
            # ^BadDataFormatError
        return it

    def backward_iter_cf_steps_(sf, /):
        '-> back-iter step/(src/cf_st, K/cf_digit, dst/cf_st)|^BadDataFormatError'
        it = backward_iter_cf_steps_(*sf.get_args())
            # ^BadDataFormatError
        dst = sf
        for ((prevN, prevD, currN, currD), K, (currN__new, currD__new)) in it:
            src = __class__(prevN, prevD, currN, currD)
            yield (src, K, dst)
            dst = src
        return
    def list_cf_steps__separately_(sf, /, *, backward_vs_forward=False):
        '-> (cf_digits, cf_sts/[ContinuedFractionFoldState])|^BadDataFormatError'
        if backward_vs_forward:
            # forward
            cf_digits = [*sf.iter_cf_digits_()]
            cf_sts = [*continued_fraction_fold_state0.iter_steps_(cf_digits)]
            if not cf_sts[-1] == sf:raise BadDataFormatError
            cf_sts[-1] = sf
        else:
            # backward
            cf_sts = [sf]
            cf_digits = []
            it = sf.backward_iter_cf_steps_()
                # ^BadDataFormatError
            for (src, K, dst) in it:
                cf_sts.append(src)
                cf_digits.append(K)
            cf_sts.reverse()
            cf_digits.reverse()

        assert len(cf_sts) == 1+len(cf_digits)
        assert cf_sts[-1] is sf
        assert cf_sts[0] is continued_fraction_fold_state0
            # <<== __new__()
        return (cf_digits, cf_sts)
if 1:
    set_NamedReadOnlyProperty4cls_(ContinuedFractionFoldState, _attr_nms)
ContinuedFractionFoldState.continued_fraction_fold_state0 = ContinuedFractionFoldState(0,1,1,0)
#end-class ContinuedFractionFoldState:
continued_fraction_fold_state0 = ContinuedFractionFoldState.continued_fraction_fold_state0

class ContinuedFractionError__inf__no_cf0(Exception):pass
    #[cf([]) === +oo]
def _unsafe_ND2Fraction_(N, D, /):
    return Fraction(N, D, _normalize=False)
def _unsafe_ND2Fraction(ND, /):
    N, D = ND
    return _unsafe_ND2Fraction_(N, D)
def _unsafe_NDs2Fractions(NDs, /):
    return map(_unsafe_ND2Fraction, NDs)

def iter_approximate_fraction_NDs5continued_fraction_(cf_digits, /):
    '-> Iter (N,D)|^ContinuedFractionError__inf__no_cf0'
    #bug:yield (0,1) # Fraction()
    sf = continued_fraction_fold_state0
    st = None
    for st in islice(sf.iter_steps_(cf_digits), 1, None):
        yield st.get_currND()
    if st is None:
        # [cf([]) === +oo]
        # [cf([x]) === x]
        raise ContinuedFractionError__inf__no_cf0("+oo-err:[cf([]) === +oo]")
def iter_approximate_fractions5continued_fraction_(cf_digits, /):
    '-> Iter Fraction|^ContinuedFractionError__inf__no_cf0'
    NDs = iter_approximate_fraction_NDs5continued_fraction_(cf_digits)
        # ^ContinuedFractionError__inf__no_cf0
    return _unsafe_NDs2Fractions(NDs)
def calc_ND5finite_continued_fraction_(cf_digits, /):
    '-> (N,D)|^ContinuedFractionError__inf__no_cf0'
    NDs = iter_approximate_fraction_NDs5continued_fraction_(cf_digits)
        # ^ContinuedFractionError__inf__no_cf0
    for ND in NDs:pass
    return ND
def calc_Fraction5finite_continued_fraction_(cf_digits, /):
    '-> Fraction|^ContinuedFractionError__inf__no_cf0'
    ND = calc_ND5finite_continued_fraction_(cf_digits)
    return _unsafe_ND2Fraction(ND)


def iter_approximate_fraction_NDs5continued_fraction__by_limit_denominator_(may_max1_denominator, cf_digits, /, *, le_vs_any_vs_ge=0):
    '-> Iter (N,D){.denominator<max1_denominator}|^ContinuedFractionError__inf__no_cf0'
    #check_int_ge(2, max1_denominator)
    check_int_ge_lt(-1, 2, le_vs_any_vs_ge)
    if le_vs_any_vs_ge == 0:
        #any
        NDs = _iter_approximate_fraction_NDs5continued_fraction__by_limit_denominator_(may_max1_denominator, cf_digits)
            # ^ContinuedFractionError__inf__no_cf0
    else:
        le_vs_ge = le_vs_any_vs_ge == +1
        NDs = _iter_approximate_fraction_NDs_xe5continued_fraction__by_limit_denominator_(may_max1_denominator, cf_digits, le_vs_ge=le_vs_ge)
    return (NDs)


def _iter_approximate_fraction_NDs5continued_fraction__by_limit_denominator_(may_max1_denominator, cf_digits, /):
    '-> Iter (N,D){.denominator<max1_denominator}|^ContinuedFractionError__inf__no_cf0'
    NDs = iter_approximate_fraction_NDs5continued_fraction_(cf_digits)
        # ^ContinuedFractionError__inf__no_cf0
    if not may_max1_denominator is None:
        max1_denominator = may_max1_denominator
        check_int_ge(2, max1_denominator)
        NDs = _cut_NDs(max1_denominator, NDs)
    return NDs
def _cut_NDs(max1_denominator, NDs, /):
    for N, D in NDs:
        if not D < max1_denominator:
            break
        yield N, D
    return
def ___old_ver__iter_approximate_fraction_NDs5continued_fraction__by_limit_denominator_(max1_denominator, cf_digits, /):
    #####old-ver:
    check_int_ge(2, max1_denominator)
    sf = continued_fraction_fold_state0
    for overflow, st in sf.iter_steps_until_denominator_overflow_(max1_denominator, cf_digits):
        # at least one but filter out fst
        if overflow: break
        if st is sf: continue
        # may not come here if +oo/[0 == len(cf_digits)]
        yield st.get_currND()
    return
def iter_approximate_fraction_NDs_le5continued_fraction__by_limit_denominator_(may_max1_denominator, cf_digits, /):
    '-> Iter (N,D){.denominator<max1_denominator,N/D<=cf(cf_digits)}|^ContinuedFractionError__inf__no_cf0'
    return _iter_approximate_fraction_NDs_xe5continued_fraction__by_limit_denominator_(may_max1_denominator, cf_digits, le_vs_ge=False)
def iter_approximate_fraction_NDs_ge5continued_fraction__by_limit_denominator_(may_max1_denominator, cf_digits, /):
    '-> Iter (N,D){.denominator<max1_denominator,N/D>=cf(cf_digits)}|^ContinuedFractionError__inf__no_cf0'
    return _iter_approximate_fraction_NDs_xe5continued_fraction__by_limit_denominator_(may_max1_denominator, cf_digits, le_vs_ge=True)
def _iter_approximate_fraction_NDs_xe5continued_fraction__by_limit_denominator_(may_max1_denominator, cf_digits, /, *, le_vs_ge:bool):
    '-> Iter (N,D){.denominator<max1_denominator,N/D(<= or >=)cf(cf_digits)}|^ContinuedFractionError__inf__no_cf0'
    #CARE: when finite!!
    NDs = iter_approximate_fraction_NDs5continued_fraction_(cf_digits)
        # ^ContinuedFractionError__inf__no_cf0
    if not may_max1_denominator is None:
        max1_denominator = may_max1_denominator
        check_int_ge(2, max1_denominator)
        def is_overflow_(D, /):
            return D >= max1_denominator
    else:
        def is_overflow_(D, /):
            return False
    if le_vs_ge:
        #ge
        #odds + maybe last even
        may_last_ND_at_even_idx = None
    else:
        #le
        #evens + maybe last odd
        may_last_ND_at_odd_idx = None

    even = False
    for N, D in NDs:
        even = not even
        if is_overflow_(D):
            break
        if even:
            # [N/D <= cf(cf_digits)]
            #   maybe eq!!!
            #   eq <==> [finite cf][len(cf_digits)%2==0]
            if le_vs_ge:
                #ge
                may_last_ND_at_even_idx = N, D
            else:
                #le
                may_last_ND_at_odd_idx = None
                    # not last
                yield N, D # at even idx
        else:
            # odd
            # [N/D >= cf(cf_digits)]
            #   maybe eq!!!
            #   eq <==> [finite cf][len(cf_digits)%2==0]
            if le_vs_ge:
                #ge
                may_last_ND_at_even_idx = None
                    # not last
                yield N, D # at odd idx
            else:
                #le
                may_last_ND_at_odd_idx = N, D
    else:
        #finite cf
        if le_vs_ge:
            #ge
            if not may_last_ND_at_even_idx is None:
                N, D = may_last_ND_at_even_idx
                yield N, D
        else:
            #le
            if not may_last_ND_at_odd_idx is None:
                N, D = may_last_ND_at_odd_idx
                yield N, D


def iter_approximate_fractions5continued_fraction__by_limit_denominator_(may_max1_denominator, cf_digits, /, *,  le_vs_any_vs_ge=0):
    '-> Iter Fraction{.denominator<max1_denominator}|^ContinuedFractionError__inf__no_cf0'
    #check_int_ge(2, max1_denominator)
    # check_int_ge_lt(-1, 2, le_vs_any_vs_ge)
    NDs = iter_approximate_fraction_NDs5continued_fraction__by_limit_denominator_(may_max1_denominator, cf_digits, le_vs_any_vs_ge=le_vs_any_vs_ge)
    return _unsafe_NDs2Fractions(NDs)

#xxx#class ApproximateFractionFail__limit_denominator_too_small_to_find_approximation(Exception):pass
    # [max1_denominator>=2][not +oo]:
    #   [has cf0]
    #   [at least one approximation: (cf0,1)]
class ApproximateFractionFail__limit_denominator_too_small_to_find_approximation_ge(Exception):pass
    # [le_vs_any_vs_ge == +1]
def approximate_fraction5continued_fraction__by_limit_denominator_(max1_denominator, cf_digits, /, *, le_vs_any_vs_ge=0):
    r'''[[[
-> Fraction|^ContinuedFractionError__inf__no_cf0|^ApproximateFractionFail__limit_denominator_too_small_to_find_approximation_ge{only if le_vs_any_vs_ge==+1}

[max1_denominator>=2][not +oo]:
      [has cf0]
      [at least one approximation: (cf0,1)]

>>> Fraction('3.141592653589793').limit_denominator(10)
Fraction(22, 7)

    #]]]'''#'''
    check_int_ge(2, max1_denominator)

    NDs = iter_approximate_fraction_NDs5continued_fraction__by_limit_denominator_(max1_denominator, cf_digits, le_vs_any_vs_ge=le_vs_any_vs_ge)
        # ^ContinuedFractionError__inf__no_cf0

    D = None
    for N, D in NDs:
        pass
    if D is None:
        if D is None and not le_vs_any_vs_ge == +1: raise logic-err # must leading by (cf0, 1)
        assert le_vs_any_vs_ge == +1
        #ge
        raise ApproximateFractionFail__limit_denominator_too_small_to_find_approximation_ge

    if not 0 < D < max1_denominator: raise logic-err
    return _unsafe_ND2Fraction_(N, D)

    ######old-ver:
    check_int_ge(2, max1_denominator)
    overflow, st = continued_fraction_fold_state0.steps_until_denominator_overflow_(max1_denominator, cf_digits)
    if not overflow:
        assert st.currD < max1_denominator
        N, D = st.currN, st.currD
    else:
        assert not st.currD < max1_denominator
        assert st.prevD < max1_denominator
        N, D = st.prevN, st.prevD
    if D == 0:
        N, D = 0,1
    if not 0 < D < max1_denominator: raise logic-err
    return _unsafe_ND2Fraction_(N, D)
    return Fraction(N, D)
    return N, D














from seed.math.continued_fraction.continued_fraction_fold import _test____inv_mod__basic_, _test____inv_mod_, _test____mk_coprime_certification_, _test____mk_gcd_certification_
_test____inv_mod__basic_()
if __name__ == '__main__':
    _test____inv_mod_(7)
    _test____mk_coprime_certification_(7)
    _test____mk_gcd_certification_(20)

__all__

from seed.math.continued_fraction.continued_fraction_fold import backward_iter_cf_steps_, backward_iter_cf_digits_, BadDataFormatError

from seed.math.continued_fraction.continued_fraction_fold import ContinuedFractionFoldState, continued_fraction_fold_state0

from seed.math.continued_fraction.continued_fraction_fold import approximate_fraction5continued_fraction__by_limit_denominator_
from seed.math.continued_fraction.continued_fraction_fold import iter_continued_fraction_digits5ND_, iter_approximate_fractions5continued_fraction_



from seed.math.continued_fraction.continued_fraction_fold import ContinuedFractionError__inf__no_cf0
from seed.math.continued_fraction.continued_fraction_fold import iter_approximate_fraction_NDs5continued_fraction_, iter_approximate_fractions5continued_fraction_
from seed.math.continued_fraction.continued_fraction_fold import calc_ND5finite_continued_fraction_, calc_Fraction5finite_continued_fraction_
from seed.math.continued_fraction.continued_fraction_fold import iter_approximate_fraction_NDs5continued_fraction__by_limit_denominator_, iter_approximate_fractions5continued_fraction__by_limit_denominator_, approximate_fraction5continued_fraction__by_limit_denominator_


from seed.math.continued_fraction.continued_fraction_fold import mk_gcd_certification_, validate__gcd_certification_, mk_coprime_certification_, validate__coprime_certification_, inv_mod_, validate__inv_mod_, ginv_mod_respectively_, validate__ginv_mod_respectively_, ginv_mod_, validate__ginv_mod_

from seed.math.continued_fraction.continued_fraction_fold import *
