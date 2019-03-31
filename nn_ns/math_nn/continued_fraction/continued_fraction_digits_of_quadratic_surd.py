
'''
see:
    "NOTE/math/continued fraction/[20190331]proof_about_continued_fraction_of_quadratic_irrational.txt"

x = A1/A2 + A3/A4*sqrt(A5)
[?P,N,Q. [x == (P + sqrt(N))/Q]]
    #[sqrt(A5) is irrational][A3!=0][A2!=0][A4!=0]
    x = A1/A2 + A3/A4*sqrt(A5)
        = (A1*A4 + A2*A3*sqrt(A5))/ (A2*A4)
        = (s*A1*A4/g + s*A2/g*A3*sqrt(A5))/ (s*A2*A4/g)
        = (s*A1*A4/g + sqrt((A2/g*A3)^2*A5))/ (s*A2*A4/g)
        = (P + sqrt(N))/Q
    where
        # algo A1_5_to_PNQ
        s = sign (A2/g*A3)
        g = gcd(A2, A4)
        P = s*A1*A4/g
        N = (A2/g*A3)^2*A5
        Q = s*A2*A4/g
[?B,D,C. [x == (B + sqrt(D))/C][C `divs` D-B^2]]
    algo PNQ2BDC(P,N,Q):
        [KK,k :: Integer][B = P*KK][D=N*KK^2][C=Q*KK]:
            [(D-B^2) = (N-P^2)*KK^2 = k*KK*Q]
            [(D-B^2) = (N-P^2)*KK = k*Q]
            [KK = Q/gcd(Q,N-P^2)]
        return (B,D,C)
    algo A1_5_to_BDC(P,N,Q):
        [g = gcd(A2, A4)]!
        [1 = gcd(A2/g, A4/g)]
        [1 = gcd(A1, A2)]
        [1 = gcd(A3, A4)]
        [KK = Q/gcd(Q,N-P^2)
            = s*A2*A4/g / gcd(s*A2*A4/g, (A2/g*A3)^2*A5 - (s*A1*A4/g)^2)
            = s*A2*A4/g / gcd(g*A2/g*A4/g, (A2/g*A3)^2*A5 - (A1*A4/g)^2)
            # gcd(A2/g, (A2/g*A3)^2*A5 - (A1*A4/g)^2) = 1
            # gcd(A4/g, (A2/g*A3)^2*A5 - (A1*A4/g)^2) = 1
            # gcd(g, (A2/g*A3)^2*A5 - (A1*A4/g)^2) = ???????
            = s*A2*A4/g / gcd(g, (A2/g*A3)^2*A5 - (A1*A4/g)^2)
            = Q / gcd(g, N - P^2)
        ]
        # via PNQ2BDC instead A1_5_to_BDC
        #   since A1_5_to_BDC can not make better result

# d is arbitrary
[[d :: Integer][x = d+1/x'
][x == (B + sqrt(D))/C][C `divs` D - B^2
][B' = d*C-B][C' = (D-B^2)//C + (2*B - d*C)*d][D'==D
    # algo update BDC
]]:
    [x' = (B' + sqrt(D'))/C'][C' `divs` D' - B'^2]
    [D' - B'^2 == C*C'][D' == D]
    # NOTE: D never changed!
    # floor_sqrt(D) is constant!!




[x == (P + sqrt(N))/Q]:
    [floor(x) = floor((P + sqrt(N))/Q)
        = [Q>0]floor((P + sqrt(N))/abs(Q))
        - [Q<0]ceil((P + sqrt(N))/abs(Q))
        = [Q>0]floor((P + sqrt(N))/abs(Q))
        - [Q<0]floor((P + sqrt(N) + abs(Q)-1)/abs(Q))
        = [Q>0]floor((P + floor_sqrt(N))/abs(Q))
        - [Q<0]floor((P + floor_sqrt(N) + abs(Q)-1)/abs(Q))
        = [Q>0]floor((P + floor_sqrt(N))/abs(Q))
        - [Q<0]floor((P + floor_sqrt(N) - 1)/abs(Q))
        - [Q<0]
    ]

    # algo floor(x)
    [floor(x) = floor((P + sqrt(N))/Q)
        = [Q>0]floor((P + floor_sqrt(N))/abs(Q))
        - [Q<0]floor((P + floor_sqrt(N) - 1)/abs(Q))
        - [Q<0]
    ]




[sqrt(N) is irrational]:
    conjugate ((P + sqrt(N))/Q) =[def]= (P - sqrt(N))/Q
[x is reduced_quadratic_surd] =[def]= [x is quadratic_irrational][x > 1][-1 < conjugate x < 0]


[x is purely_periodic_continued_fraction] <==> [x is reduced_quadratic_surd]


[sqrt(N) is irrational][x = (P+sqrt(N))/Q]:
    [x > 1] = [Q>0][P+sqrt(N) > Q] + [Q<0][P+sqrt(N) < Q]
        = [Q>0][P+floor_sqrt(N) >= Q]
        + [Q<0][P+floor_sqrt(N) < Q]
        = [Q>0][floor_sqrt(N) >= Q-P]
        + [Q<0][floor_sqrt(N) < Q-P]
    [-1 < conjugate x < 0]
        = [-1 < (P - sqrt(N))/Q < 0]
        = [Q>0][-Q < (P - sqrt(N)) < 0]
        + [Q<0][-Q > (P - sqrt(N)) > 0]
        = [Q>0][Q > -P + sqrt(N) > 0]
        + [Q<0][Q < -P + sqrt(N) < 0]
        = [Q>0][Q+P > sqrt(N) > P]
        + [Q<0][Q+P < sqrt(N) < P]
        = [Q>0][Q+P > floor_sqrt(N) >= P]
        + [Q<0][Q+P <= floor_sqrt(N) < P]
    [x is reduced_quadratic_surd]
        = [x > 1][-1 < conjugate x < 0]
        = ([Q>0][floor_sqrt(N) >= Q-P] + [Q<0][floor_sqrt(N) < Q-P])
         *([Q>0][Q+P > floor_sqrt(N) >= P] + [Q<0][Q+P <= floor_sqrt(N) < P])
        = [Q>0][floor_sqrt(N) >= Q-P][Q+P > floor_sqrt(N) >= P]
        + [Q<0][floor_sqrt(N) < Q-P][Q+P <= floor_sqrt(N) < P]
        = [Q>0][Q+P > floor_sqrt(N) >= P][floor_sqrt(N) >= Q-P][P>0]
        + [Q<0][Q+P <= floor_sqrt(N) < P][floor_sqrt(N) < Q-P][P<0]
        = [Q>0][Q+P > floor_sqrt(N) >= P][floor_sqrt(N) >= Q-P][P>0]
        + [Q<0][Q+P <= floor_sqrt(N) < P][floor_sqrt(N) < Q-P][P<0][False]
        = [Q>0][P>0][Q+P > floor_sqrt(N) >= P][floor_sqrt(N) >= Q-P]

    # algo is_reduced_quadratic_surd(x)
    [x is reduced_quadratic_surd]
        = [Q>0][P>0][Q+P > floor_sqrt(N) >= P][floor_sqrt(N) >= Q-P]

'''

__all__ = '''
    constant_coeff_discriminant_to_PNQ
        CCD2PNG
    list_split_periodic_continued_fraction_digits_of_quadratic_surd__PNQ
    list_split_periodic_continued_fraction_digits_of_quadratic_surd__CCD
    split_periodic_continued_fraction_digits_of_quadratic_surd__CCD
    split_periodic_continued_fraction_digits_of_quadratic_surd__PNQ

    iter_continued_fraction_digits_of_quadratic_surd__PNQ
    iter_continued_fraction_digits_of_rational
    iter_maybe_continued_fraction_digits_of_quadratic_surd__PNQ
    is_reduced_quadratic_surd__PNQ

    _iter_continued_fraction_digits_of_quadratic_surd__BDC
    _is_reduced_quadratic_surd__BDC
    _PNQ2BDC
    '''.split()
    #one
    #zero

from ..floor_sqrt import floor_sqrt
from fractions import Fraction
from math import floor, gcd

one = Fraction(1)
zero = Fraction(0)


def constant_coeff_discriminant_to_PNQ(*
    ,constant:Fraction
    ,times:Fraction
    ,discriminant:int
    ):
    '''
input:
    constant, times :: Fraction
    discriminant :: Integer
        x = constant + times * sqrt(discriminant)
output:
    P, N, Q :: Integer
        x = (P+sqrt(N))/Q
'''
    assert type(constant) is type(times) is Fraction
    assert type(discriminant) is int
    A1 = constant.numerator
    A2 = constant.denominator
    A3 = times.numerator
    A4 = times.denominator
    A5 = discriminant
    return _A1_5_to_PNQ(A1, A2, A3, A4, A5)

CCD2PNG = constant_coeff_discriminant_to_PNQ

def _A1_5_to_PNQ(A1, A2, A3, A4, A5):
    # x = A1/A2 + A3/A4*sqrt(A5)
    # A1_5_to_BDC
    g = gcd(A2, A4)
    S = (A2//g*A3)
    A4_g = A4//g

    N = S**2*A5
    #s = sign S
    #P = s*A1*A4_g
    #Q = s*A2*A4_g
    P = A1*A4_g
    Q = A2*A4_g
    if S < 0:
        P = -P
        Q = -Q
    return P, N, Q

def _PNQ2BDC(P, N, Q):
    KK = Q//gcd(Q, N-P**2)
    B = P*KK
    D = N*KK**2
    C = Q*KK
    return B, D, C


def iter_continued_fraction_digits_of_rational(x):
    '''Fraction -> Iter Integer
input:
    x :: Fraction
output:
    iter_continued_fraction_digits_of x :: Iter Integer
'''
    assert type(x) is Fraction
    while True:
        d = floor(x)
        yield d

        x = x - d
        if not x: break
        x = 1/x


def list_split_periodic_continued_fraction_digits_of_quadratic_surd__PNQ(*, P, N, Q):
    '''-> (non_periodic_digits::[Integer], periodic_digits::[PInt])
input:
    P,N,Q :: Integer
        [x = (P+sqrt(N))/Q]
        x may be rational
output:
    (non_periodic_digits, periodic_digits) :: ([Integer], [PInt])
        continued_fraction_digits_of x == non_periodic_digits + periodic_digits*(+oo)
'''
    return __list_split(
        split_periodic_continued_fraction_digits_of_quadratic_surd__PNQ
        ,**locals()
        )

def split_periodic_continued_fraction_digits_of_quadratic_surd__PNQ(*, P, N, Q):
    '''-> (non_periodic_digits::[Integer], iter_periodic_digits::Iter PInt)
input:
    P,N,Q :: Integer
        [x = (P+sqrt(N))/Q]
        x may be rational
output:
    (non_periodic_digits, iter_periodic_digits) :: ([Integer], Iter PInt)
        continued_fraction_digits_of x == non_periodic_digits + periodic_digits*(+oo)
'''
    it = iter_maybe_continued_fraction_digits_of_quadratic_surd__PNQ(
            P=P, N=N, Q=Q)
    non_periodic_digits = []
    for maybe_d in it:
        if maybe_d is None:
            break
        d = maybe_d
        non_periodic_digits.append(d)

    iter_periodic_digits = it
    return non_periodic_digits, iter_periodic_digits



def iter_continued_fraction_digits_of_quadratic_surd__PNQ(*, P, N, Q):
    '''= iter_continued_fraction_digits_of x :: Iter Integer
input:
    P,N,Q :: Integer
        [x = (P+sqrt(N))/Q]
        x may be rational
output:
    iter_continued_fraction_digits_of x :: Iter Integer
        yield non_periodic_digits
        while True:
            yield periodic_digits
'''
    it = iter_maybe_continued_fraction_digits_of_quadratic_surd__PNQ(
            P=P, N=N, Q=Q)
    for maybe_d in it:
        if maybe_d is None:
            break
        d = maybe_d
        yield d

    periodic_digits = []
    for d in it:
        yield d
        periodic_digits.append(d)

    while True:
        yield from periodic_digits

def iter_maybe_continued_fraction_digits_of_quadratic_surd__PNQ(*, P, N, Q):
    '''= iter_maybe_continued_fraction_digits_of x :: Iter (None|Integer)
input:
    P,N,Q :: Integer
        [x = (P+sqrt(N))/Q]
        x may be rational
output:
    iter_maybe_continued_fraction_digits_of x :: Iter (None|Integer)
        yield non_periodic_digits
        yield None
        yield periodic_digits # finite!!!!
'''
    assert type(P) is type(N) is type(Q) is int
    assert Q != 0
    assert N >= 0
    B,D,C = _PNQ2BDC(P, N, Q)
    # [x = (B + sqrt(D))/C]

    floor_sqrtD = floor_sqrt(D)
    if floor_sqrtD**2 == D:
        sqrtD = floor_sqrtD
        x = Fraction(B + sqrtD, C)
        yield from iter_continued_fraction_digits_of_rational(x)
        yield None
        return

    it = _iter_continued_fraction_digits_of_quadratic_surd__BDC(
                B=B, D=D, C=C, floor_sqrtD=floor_sqrtD)
    for B, C, d in it:
        #if x is reduced_quadratic_surd:break
        if _is_reduced_quadratic_surd__BDC(
                B=B, D=D, C=C, floor_sqrtD=floor_sqrtD):
            break
        yield d # non_periodic_digits
    yield None

    B0, C0 = B, C
    d0 = d
    for B, C, d_ in it:
        yield d
        d = d_
        if B==B0 and C==C0:
            assert d == d0
            break
    return


def _is_reduced_quadratic_surd__BDC(*, B, D, C, floor_sqrtD):
    '== is_reduced_quadratic_surd__PNQ'
    return is_reduced_quadratic_surd__PNQ(P=B, N=D, Q=C, floor_sqrtN=floor_sqrtD)
def is_reduced_quadratic_surd__PNQ(*, P, N, Q, floor_sqrtN):
    '''= [x is reduced_quadratic_surd]

input:
    P,N,Q :: Integer
        [x = (P+sqrt(N))/Q][sqrt(N) is irrational]
output:
    [x is reduced_quadratic_surd] :: Bool


[x is reduced_quadratic_surd] =[def]= [x is quadratic_irrational][x > 1][-1 < conjugate x < 0]

[sqrt(N) is irrational][x = (P+sqrt(N))/Q]:
    [x is reduced_quadratic_surd]
        = [Q>0][P>0][Q+P > floor_sqrt(N) >= P][floor_sqrt(N) >= Q-P]
'''
    return Q>0 and P>0 and Q+P > floor_sqrtN >= P and floor_sqrtN >= Q-P

def _iter_continued_fraction_digits_of_quadratic_surd__BDC(*, B, D, C, floor_sqrtD):
    '''-> Iter (B, C, continued_fraction_digit)


input:
    B,D,C,floor_sqrtD :: Integer
        [x = (B + sqrt(D))/C][C `divs` D - B^2][sqrt(D) is irrational]
output:
    triples :: Iter (B::Integer, C::Integer, d::Integer)
        (B, C, d)
        d == floor(x) = floor((B + sqrt(D))/C)


-------------------------
[floor(x) = floor((B + sqrt(D))/C)
    = [C>0]floor((B + floor_sqrt(D))/abs(C))
    - [C<0]floor((B + floor_sqrt(D) - 1)/abs(C))
    - [C<0]
]
[d==floor(x)][B' = d*C-B][C' = (D-B^2)//C + (2*B - d*C)*d][D'==D]
'''
    assert type(B) is type(D) is type(C) is type(floor_sqrtD) is int
    assert C != 0
    assert D > 0
    assert (D-B**2)%C == 0
    assert floor_sqrtD**2 < D < (floor_sqrtD+1)**2

    while True:
        abs_C = abs(C)
        if C > 0:
            floor_x = (B+floor_sqrtD)//abs_C
        else:
            floor_x = -((B+floor_sqrtD-1)//abs_C +1)
        d = floor_x
        yield B, C, d

        B_ = d*C-B
        #D_ = D
        C_ = (D-B**2)//C + (2*B - d*C)*d
        B,C = B_,C_


def __list_split(split, **kwargs):
    non_periodic_digits, iter_periodic_digits = split(**kwargs)
    periodic_digits = list(iter_periodic_digits)
    return non_periodic_digits, periodic_digits

def list_split_periodic_continued_fraction_digits_of_quadratic_surd__CCD(*
    ,constant:Fraction
    ,times:Fraction
    ,discriminant:int
    ):
    '''-> (non_periodic_digits::[Integer], periodic_digits::[PInt])
input:
    constant, times :: Fraction
    discriminant :: Integer
        x = constant + times * sqrt(discriminant)
        x may be rational
output:
    (non_periodic_digits, periodic_digits) :: ([Integer], [PInt])
        continued_fraction_digits_of x == non_periodic_digits + periodic_digits*(+oo)
'''
    return __list_split(
        split_periodic_continued_fraction_digits_of_quadratic_surd__CCD
        ,**locals()
        )

def split_periodic_continued_fraction_digits_of_quadratic_surd__CCD(*
    ,constant:Fraction
    ,times:Fraction
    ,discriminant:int
    ):
    '''-> (non_periodic_digits::[Integer], iter_periodic_digits::Iter PInt)
input:
    constant, times :: Fraction
    discriminant :: Integer
        x = constant + times * sqrt(discriminant)
        x may be rational
output:
    (non_periodic_digits, iter_periodic_digits) :: ([Integer], Iter PInt)
        continued_fraction_digits_of x == non_periodic_digits + periodic_digits*(+oo)
'''

    P,N,Q = constant_coeff_discriminant_to_PNQ(
                constant=constant, times=times, discriminant=discriminant)
    (non_periodic_digits, iter_periodic_digits
    ) = split_periodic_continued_fraction_digits_of_quadratic_surd__PNQ(
            P=P, N=N, Q=Q)
    return (non_periodic_digits, iter_periodic_digits)

def _t(n, sqrt_coeff, constant):
    print(f'f(sqrt({n})*{sqrt_coeff}+{constant}) = ...')

    (non_periodic_digits, periodic_digits
    ) = list_split_periodic_continued_fraction_digits_of_quadratic_surd__CCD(
        constant=constant
        ,times=sqrt_coeff
        ,discriminant=n
        )
    r = (non_periodic_digits, periodic_digits)

    print(f'f(sqrt({n})*{sqrt_coeff}+{constant}) = {r}')
    print(f'len(non_periodic_digits)={len(non_periodic_digits)}')
    print(f'len(periodic_digits)={len(periodic_digits)}')

def _test():
    def AAA(a, b):
        return a, b
    def f(n, sqrt_coeff, constant):
        sqrt_coeff = Fraction(sqrt_coeff)
        constant = Fraction(constant)
        return list_split_periodic_continued_fraction_digits_of_quadratic_surd__CCD(
            constant=constant
            ,times=sqrt_coeff
            ,discriminant=n
            )
    assert f(4, 1, 0) == AAA([2], [])
    assert f(0, 1, 0) == AAA([0], [])
    assert f(2, 1, 0) == AAA([1], [2])
    assert f(3, 1, 0) == AAA([1], [1, 2])
    assert f(5, 1, 0) == AAA([2], [4])
    assert f(7, 1, 0) == AAA([2], [1, 1, 1, 4])
    assert f(11, 1, 0) == AAA([3], [3, 6])
    assert f(13, 1, 0) == AAA([3], [1, 1, 1, 1, 6])

'''
def is_odd(n:int):
    return n&1
def is_integer(r:Fraction):
    return abs(r.denominator) == 1
'''

if __name__ == '__main__':
    _test()
    _t(4, one, zero)
    _t(0, one, zero)
    _t(2, one, zero)
    _t(3, one, zero)
    _t(5, one, zero)
    _t(7, one, zero)
    _t(11, one, zero)
    _t(13, one, zero)
    input('continue>>> ...')
    _t(10005, 426880*one, zero)
        #len(non_periodic_digits)=1
        #len(periodic_digits)=78408


