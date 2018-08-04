'''
proof from the book
page21
Efficient ways to find such representations as sums of two squares are discussed in [1] and [7].

page22
[1] F. W. C LARKE, W. N. E VERITT, L. L. L ITTLEJOHN & S. J. R. VORSTER:
H. J. S. Smith and the Fermat Two Squares Theorem, Amer. Math. Monthly
106 (1999), 652-665.

[7] S. W AGON: Editor’s corner: The Euclidean algorithm strikes again, Amer.
Math. Monthly 97 (1990), 125-129.
'''

import itertools
from .prime2 import mod_pow, primes
from .floor_sqrt import floor_sqrt
from .prime1 import factor_power_pairs_of_positive_integer

#import numbers

class IntPair:#(numbers.Complex):
    def __init__(self, real = 0, imag = 0):
        assert type(real) == type(imag) == int
        self.real = real
        self.imag = imag
    def __add__(self, other):
        if isinstance(other, IntPair):
            return IntPair(self.real + other.real, self.imag + other.imag)
        elif isinstance(other, int):
            return IntPair(self.real + other, self.imag)
        #elif isinstance(other, OtherTypeIKnowAbout):
        #    return do_my_other_adding_stuff(self, other)
        else:
            return NotImplemented
    def __sub__(self, other):
        if isinstance(other, IntPair):
            return IntPair(self.real - other.real, self.imag - other.imag)
        elif isinstance(other, int):
            return IntPair(self.real - other, self.imag)
        else:
            return NotImplemented
    def __mul__(self, other):
        if isinstance(other, IntPair):
            return IntPair(self.real * other.real - self.imag * other.imag,
                           self.real * other.imag + self.imag * other.real)
        elif isinstance(other, int):
            return IntPair(self.real * other, self.imag * other)
        else:
            return NotImplemented
    def __radd__(self, other): return self + other
    def __rsub__(self, other): return -self + other
    def __rmul__(self, other): return self * other
    def __pos__(self):return self
    def __neg__(self):return IntPair(-self.real, -self.imag)
    def __eq__(self, other):
        if isinstance(other, IntPair):
            return self.real == other.real and self.imag == other.imag
        elif isinstance(other, int):
            return self.real == other and self.imag == 0
        else:
            return NotImplemented
    def __ne__(self, other): not self == other
    def __bool__(self):return self.real != 0 or self.imag != 0
    def conjugate(self):return IntPair(self.real, -self.imag)
    def __str__(self):
        plus = '+'
        if self.imag < 0: plus = ''
        return str(self.real) + plus + str(self.imag) + '*i'
    def __repr__(self): return '<IntPair' + str(self.tuple()) + '>'
    def abs2(self): return self.real**2 + self.imag**2
    def tuple(self, t = ()):
        if t: self.real, self.imag = t
        else: return (self.real, self.imag)
    def rotateTo1st(self):
        if not self: return self
        i = IntPair(0,1)
        while not (self.real > 0 and self.imag >= 0):
            self *= i
        return self
    def is_real(self): return self.imag == 0

def dotproductIntPair(u, v):
    return u.real*v.real + u.imag*v.imag
def floor_projectIntPair(u, v):
    return dotproductIntPair(u,v)//dotproductIntPair(v,v)
def divmodIntPair(a,b):
    '''
    (q,r) = fself(a,b)
    stands for a = q*b + r, r in the rectangle {0,b,bi,b(1+i)}-b(1+i)//2
    -1/2 <= project(r,b) < 1/2, floor_project(2r,b) = 0 or -1
    -1/2 <= project(r,bi) < 1/2, floor_project(2r,bi) = 0 or -1
    '''
    assert b
    (q,r) = divmodIntPair_impl_2nd(a,b)
    assert a == q*b + r
    assert r.abs2() < b.abs2()
    i = IntPair(0,1)
    assert -1 <= floor_projectIntPair(2*r,b) <= 0
    assert -1 <= floor_projectIntPair(2*r,b*i) <= 0
    
    return (q,r)

def divmodIntPair_impl_1st(a,b):
    assert b
    i = IntPair(0,1)
    q = IntPair(floor_projectIntPair(a, b),
                floor_projectIntPair(a, b*i))
    r = a - q*b
    if floor_projectIntPair(2*r,b) > 0:
        q += 1
        r -= b
    if floor_projectIntPair(2*r,b*i) > 0:
        q += i
        r -= b*i
    return (q,r)

def divmodIntPair_impl_2nd(a,b):
    assert b
    i = IntPair(0,1)
    A = 2*a+b*(1+i)
    B = 2*b
    q = IntPair(floor_projectIntPair(A, B),
                floor_projectIntPair(A, B*i))
    r = a - q*b
    return (q,r)
    
def gcdIntPair(a,m):
    A1,A2 = 1,0
    B1,B2 = 0,1
    r1,r2 = a,m
    while r2:
        assert (r1,r2) == (A1*a+A2*m, B1*a+B2*m)
        q1, r3 = divmodIntPair(r1, r2)
        A1,A2,B1,B2 = B1, B2, A1-q1*B1, A2-q1*B2
        r1,r2 = r2,r3

    return r1.rotateTo1st()

def gcd(a,m):
    return gcdIntPair(IntPair(a), IntPair(m)).real


def _test_to_sum_of_two_squares(N=1000):
    print('hi')
    for i in range(N):
        factor_exp_ls = factor_power_pairs_of_positive_integer(i)
        r1 = to_sum_of_two_squares_definition(i, factor_exp_ls)
        r2 = to_sum_of_two_squares(i, factor_exp_ls)
        assert r1 == r2
    
def to_sum_of_two_squares_definition(n, factor_exp_ls):
    if n < 0:
        return []
    top = 1+floor_sqrt(n)
    i = 0
    ls = []
    while i < top:
        x = n - i**2
        sqrt = floor_sqrt(x)
        if sqrt**2 == x:
            assert i <= x
            ls.append((i, sqrt))
            top = sqrt
        i += 1

    assert all(a <= b for a,b in ls)
    assert all(a1 < a2 for (a1,_), (a2,_) in zip(ls, ls[1:]))
    assert all(sum(x**2 for x in pair) == n for pair in ls)
    return ls
def to_sum_of_two_squares(n, factor_exp_ls):
    pairs = __to_sum_of_two_squares(n, factor_exp_ls)
    assert all(sum(x**2 for x in pair) == n for pair in pairs)
    return pairs

def __to_sum_of_two_squares(n, factor_exp_ls):
    assert len(set(p for p,e in factor_exp_ls)) == len(factor_exp_ls)
    assert all(p > 1 and e > 0 for p,e in factor_exp_ls)
    assert all(n%p == 0 for p,e in factor_exp_ls)

    if n < 0:
        return []
    if n == 0:
        return [(0,0)]
    assert n == product((p**e for p, e in factor_exp_ls), start = 1)

    p4_1_ls = []
    p4_3_ls = []
    p2_e = 0
    for p, e in factor_exp_ls:
        if p % 4 == 1:
            p4_1_ls.append((p,e))
        elif p % 4 == 3:
            if e % 2 == 1:
                return [] # no possible
            p4_3_ls.append((p,e))
        else:
            if p != 2:
                raise ValueError('not prime-factor')
            p2_e = e

    sum_squares = [IntPair(*sum_of_two_squares(p)) for p,e in p4_1_ls]
        
    '''
n = sqrt_left**2 + sqrt_right**2
= (L**2 + R**2) * gcd
= (L**2 + R**2) * sqrt_gcd**2
gcd(L, R) == 1

n = max_sqrt_gcd**2 * min_sum_of_square
if min_sum_of_square%p == 0, then min_sum_of_square%p**2 != 0
given L, R, max_sqrt_gcd, min_sum_of_square ==>> sqrt_gcd
let (L**2 + R**2)//min_sum_of_square = B**2
let sqrt_gcd = A
n = min_sum_of_square * B**2 * sqrt_gcd**2
n//min_sum_of_square == (B*A)**2 = A2B2
A*B == max_sqrt_gcd
can't!!!!
'''
    if p2_e % 2:
        # 2 == (1+1j)(1-1j)
        left, right = IntPair(1,1), IntPair(1,-1)
    else:
        # 1^2 + 0^2 == (1+0j)(1-0j)
        left, right = IntPair(1,0), IntPair(1,0)



    max_sqrt_gcd = product((p**(e//2) for p, e in factor_exp_ls), start = 1)
    min_sum_of_left_right_sqare = product((p**(e%2) for p, e in factor_exp_ls), start = 1)

    pair_powers_ls = []
    for (p,e), pair in zip(p4_1_ls, sum_squares):
        pair_powers = [1]
        for _ in range(e):
            pair_powers.append(pair_powers[-1]*pair)
        assert len(pair_powers) == e+1
        pair_powers_ls.append(pair_powers)
        
    lefts = []
    shifted_sqrt_gcds = []
    for exps in itertools.product(*(range(-e, e+1, 2) for p,e in p4_1_ls)):
        e = 0
        for e in exps:
            if e != 0:
                break
        if e < 0:
            # first nonzero should > 0; otherwise will yield duplicate pair
            continue

        LR = left
        for e, pair_powers in zip(exps, pair_powers_ls):
            pair_power = pair_powers[abs(e)]
            if e < 0:
                pair_power = pair_power.conjugate()
            LR *= pair_power
        lefts.append(LR)
        
        shifted_sqrt_gcd = 1
        for (p,_), e in zip(p4_1_ls, exps):
            shifted_sqrt_gcd *= p**(abs(e)//2)
        shifted_sqrt_gcds.append(shifted_sqrt_gcd)

    total = (1+product((e+1 for _,e in p4_1_ls), start=1))//2
    assert len(shifted_sqrt_gcds) == len(lefts) == total

    sums = [pair.abs2() for pair in lefts]
    sqrt_gcds = [max_sqrt_gcd//shifted_sqrt_gcd
                 for shifted_sqrt_gcd in shifted_sqrt_gcds]
    assert all(sqrt_gcd**2 * sum for sum, sqrt_gcd in zip(sums, sqrt_gcds))
    

    pairs = [pair.tuple() for pair in lefts]
    pairs = [tuple(sorted(sqrt_gcd * abs(m) for m in pair))
             for sqrt_gcd, pair in zip(sqrt_gcds, pairs)]
    pairs = sorted(pairs)

    #print(factor_exp_ls, pairs)
    assert len(pairs) == total
    assert all(sum(x**2 for x in pair) == n for pair in pairs)
    return pairs
    

def product(numbers, start=1):
    for n in numbers:
        start = start * n
    return start

#pa_b: prime of form am+b, 0 < b < a
def sum_of_two_squares(p4_1):
    ans = sum_of_two_squares_impl(p4_1)[0]
    assert sum(x**2 for x in ans) == p4_1
    for x in ans: assert x > 0
    assert len(ans) == 2
    for j in range(len(ans)): assert (ans[j]+j) % 2 == 1
    return ans

def sum_of_two_squares_impl(p4_1, ps = primes(100)):
    assert p4_1 > 0
    assert p4_1%4 == 1
    #assert is_prime(p4_1)
    failstring = 'p4_1 is not a prime'

    #p4_1 = 2^k * odd + 1
    k = 0
    odd = p4_1 - 1
    while odd % 2 != 1:
        k += 1
        odd //= 2

    assert k >= 2
    assert p4_1 == 2**k * odd + 1

    
    _1 = p4_1 - 1
    r = 1
    p = 1
    for j in range(len(ps)):
        p = ps[j]
        if p4_1 % p == 0: raise failstring
        r = mod_pow(p, odd, p4_1)
        if not (r == 1 or r == _1): break
    
    r_ = p+1
    while r == 1 or r == _1:
        #r = random.randint(2, p4_1//2)
        r, r_ = r_, r_+1
        if gcd(r, p4_1) != 1: raise failstring
        r = mod_pow(r, odd, p4_1)
    else:
        min_r = r_ - 1
        
    sqrt_r = None
    for i in range(k):
        if r == 1: raise failstring
        elif r == _1: break
        sqrt_r, r = r, r**2%p4_1
    else: raise failstring

    assert sqrt_r**2%p4_1 == _1 # x^2 = -1 mod p
    m = IntPair(sqrt_r, 1)
    p = IntPair(p4_1, 0)
    ans = gcdIntPair(m,p).tuple()
    if ans[0] % 2 != 1:
        ans = (ans[1], ans[0])
    # ans = (odd, even)
    return ans,(p4_1,min_r)
    '''
    n = 10000000, min_r is no more than 23
    [(5, 2), (73, 3), (601, 5), (15241, 7), (32089, 11),
    (148201, 13), (196681, 17), (4179289, 19), (7781929, 23)]
    '''
    
def test_sum_of_two_squares(n = 10003, k = 10):
    ps = primes(n)
    #print(max(sum_of_two_squares_impl(p)[-1][-1] for p in ps if p%4 == 1))
    #return
    max_min_r = 0
    ls = []
    for p in ps:
        if p % 4 == 1:
            #a = sum_of_two_squares(p)
            a = sum_of_two_squares_impl(p, ps[:k])
            (odd, even) = a[0]
            assert odd % 2 != 0
            assert even % 2 == 0
            assert odd > 0 < even
            assert odd**2 + even**2 == p
            min_r = a[-1][-1]
            if min_r > max_min_r:
                ls.append((p, min_r))
                max_min_r = min_r
            #print(a)

    #print(ls)

def test_divmodIntPair(n = 10):
    for a in range(-n,n):
        for b in range(-n,n):
            for c in range(-n,n):
                for d in range(-n,n):
                    A = IntPair(a,b)
                    B = IntPair(c,d)
                    if not B: continue
                    q,r = divmodIntPair(A,B)
                    assert A == q*B + r
                    assert r.abs2() < B.abs2()
                    
def test_divmodIntPair_impl_2nd_by_1st(n = 10):
    for a in range(-n,n):
        for b in range(-n,n):
            for c in range(-n,n):
                for d in range(-n,n):
                    A = IntPair(a,b)
                    B = IntPair(c,d)
                    if not B: continue
                    qr1 = divmodIntPair_impl_1st(A,B)
                    qr2 = divmodIntPair_impl_2nd(A,B)
                    if qr1 != qr2: print(A,B);print(qr1, qr2)
                    assert qr1 == qr2

_test_to_sum_of_two_squares
t = _test_to_sum_of_two_squares




