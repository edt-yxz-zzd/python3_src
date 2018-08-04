
'''

x = N bits
a, b, c

fnext(x[n], a, b, c):
    x = x[n]
    x ^= (x >> a)
    x ^= (x << b)
    x ^= (x >> c)
    x[n+1] = x
    return x[n+1]

what a,b,c makes period largest, that is 2**N - 1?


fT(x,a): return x ^ (x >> a)
let X = diagonal(x) [mod 2], T_(a) = I + subdiagonal(ones(a))
fT(x,-a): return x ^ (x << a)
let X = diagonal(x) [mod 2], T_(-a) = I + superdiagonal(ones(a))

TNEXT = T_(c)*T_(-b)*T_(a)
TNEXT**P == I [mod 2]
let P = 2**N - 1 = product(p(i)**e(i) for i ...)
requires TNEXT**P == I and TNEXT**(P//p(i)) != I [mod 2]

a,b,c in range(N), N**3 possible (a,b,c)'s
TNEXT**(2**x) for x in range(N) : N * N**3 = O(N**4)
TNEXT**(P//p(i)) for i in ...: ? * N * N**3 = O(? * N**4) // for N = 64, ? = 7

that is O(?*N**7) to search any cases.

N 64 abc (21, 35, 4)
'''

from itertools import chain, product


# N == 64
primes_N64 = [6700417, 65537, 641, 257, 17, 5, 3]
abc_part_N64 = [
    (21, 35, 4),
    (20, 41, 5),
    (17, 31, 8),
    (11, 29, 14),
    (14, 29, 11),
    (30, 35, 13),
    (21, 37, 4),
    (21, 43, 4),
    (23, 41, 18),
    ]
def test_are_all_factors(N, primes):
    period = 2**N - 1
    for p in primes:
        q, r = divmod(period, p)
        if r:
            return False
        while r == 0:
            period = q
            q, r = divmod(period, p)
            
    return period == 1




class MxMod2:
    def __init__(self, N, iterable=None):
        if iterable == None:
            self.mx = bytearray(N**2)
        else:
            self.mx = bytearray(iterable)
        assert len(self.mx) == N**2
        self.N = N
        
    def __eq__(self, other):
        if self.N != other.N:
            return False
        for s, o in zip(self.mx, other.mx):
            if 1 & (s ^ o):
                return False
        return True
    def __ne__(self, other):
        return not (self == other)
    def __mul__(self, other):
        assert self.N == other.N
        N = self.N
        
        mx = bytearray(N**2)
        for r in range(N):
            start = r*N
            row = self.mx[start : start+N]
            for c in range(N):
                k = 0
                for a,b in zip(row, other.mx[c::N]):
                    k ^= a & b
                mx[start+c] = k
        return MxMod2(N, mx)
    
    def __add__(self, other):
        assert self.N == other.N
        return MxMod2(self.N, (s+o for s, o in zip(self.mx, other.mx)))

    def get(self, r, c):
        return self.mx[r*self.N + c]
    def set(self, r, c, v):
        self.mx[r*self.N + c] = v
    def get_row_size(self):
        return self.N

    def __repr__(self):
        N = self.N
        return '<MxMod2({N}, {data})>'.format(
            N=N,
            data=' '.join(
                '{!r}'.format(
                    ''.join(str(1&b) for b in self.mx[i*N : (i+1)*N]))
                for i in range(N))
            )
    
    
    
def test_MxMod2():
    N = 2
    O = [0, 0,
         0, 0]
    I = [1, 0,
         0, 1]
    A = [0, 1,
         0, 0]
    B = [1, 1,
         0, 1]

    O = MxMod2(N, O)
    I = MxMod2(N, I)
    A = MxMod2(N, A)
    B = MxMod2(N, B)

    mxs = [O, I, A, B]
    data_mul = list(chain(
        ((O, O, x) for x in mxs),
        ((O, x, O) for x in mxs),
        ((x, x, I) for x in mxs),
        ((x, I, x) for x in mxs),
        ((O, A, A), (A, A, B), (A, B, A),
         (I, B, B))
                          )
                    )
    data_add = list(chain(
        ((x, O, x) for x in mxs),
        ((x, x, O) for x in mxs),
        ((O, x, x) for x in mxs),
        ((rhs+lhs, lhs, rhs) for lhs in mxs for rhs in mxs),
        ((lhs+rhs, lhs, rhs) for lhs in mxs for rhs in mxs),
        ((A, I, B), (B, I, A), (I, A, B))
                          )
                    )
    
    for r, a, b in data_mul:
        assert r == a*b
    for r, a, b in data_add:
        assert r == a+b

def xorshift2mx(N, n):
    return diagonal(N, n) + diagonal(N)

def diagonal(N, shiftdown = 0):
    n = shiftdown
    assert -N <= n <= N
    mx = MxMod2(N)
    r = n
    c = 0
    r - c == n
    for r in range(max(0,n), min(N, N+n)):
        c = r - n
        mx.set(r, c, 1)
    return mx
def subdiagonal(N, n):
    assert 0 <= n <= N
    return diagonal(N, n)

def superdiagonal(N, n):
    assert 0 <= n <= N
    return diagonal(N, -n)

def abcN2Tnext(a,b,c,N):
    Ta = xorshift2mx(N, a)
    Tb = xorshift2mx(N, -b)
    Tc = xorshift2mx(N, c)
    Tnext = Tc*Tb*Ta
    return Tnext
def try_abc(N, primes, a, b, c):
    assert test_are_all_factors(N, primes)
    Tnext = abcN2Tnext(a,b,c,N)
    I = diagonal(N)
##    print(Ta)
##    print(Tb)
##    print(Tc)
##    print(I)

    ls = [Tnext] # ls[i] = Tnext**2**i
    for i in range(N-1):
        ls.append(ls[-1]*ls[-1])

    period = 2**N - 1
    P = calc_power(ls, period)
    if P != I:
##        print('period', period)
##        print(P)
        return False
        
    for p in primes:
        power = period//p
        P = calc_power(ls, power)
        if P == I:
##            print('p', p)
            return False

    return True  



def calc_power(T_2pow_ls, power:int):
    assert power > 0
    s = bin(power)[-1:1:-1]
##    print(power, s)
    assert len(T_2pow_ls) >= len(s)
    N = T_2pow_ls[0].get_row_size()
    I = diagonal(N)
    T = I
    for t, c in zip(T_2pow_ls, s):
        if c == '1':
            T = T*t
    return T


def all_abc_N5():
    N = 5
    primes = [31]
    ls = []
    for a, b, c in product(range(1, N), repeat=3):
        if try_abc(N, primes, a, b, c):
            ls.append((a,b,c))
    return ls

def all_abc(a=1, b=1, c=1, N=5, primes=[31]):
    assert 0 < a < N
    assert 0 < b < N
    assert 0 < c < N


    a0, b0, c0 = a, b, c
    del a,b,c
    for a, b, c in chain(
        ((a0,b0,z) for z in range(c0, N)),
        ((a0,y,z) for y in range(b0+1, N) for z in range(1, N)),
        ((x,y,z) for x in range(a0+1, N) for y in range(1, N) for z in range(1, N))
        ):
        if try_abc(N, primes, a, b, c):
            yield (a,b,c)


def next_of_abc_mask(mask, a, b, c, x):
    x ^= (x >> a)
    #x &= mask
    x ^= (x << b) & mask
    x ^= (x >> c)
    return x
def use_abc_to_generate_seq(N, a, b, c):
    mask = (1 << N) - 1
    x = 1
    ls = [1]
    for _ in range(mask+1):
        x = next_of_abc_mask(mask, a, b, c, x)
        if x == 1:
            break
        ls.append(x)
    else:
        raise Exception('error: a,b,c')

    assert len(ls) == mask == len(set(ls))
    
    return ls


def N5():
    r = all_abc_N5()
    print(len(r), r)
    #24
    #[(1, 1, 1), (1, 1, 2), (1, 3, 1), (1, 3, 2), (1, 3, 3), (1, 3, 4),
    # (1, 4, 2), (1, 4, 3), (1, 4, 4), (2, 1, 1), (2, 1, 3), (2, 3, 1),
    # (2, 3, 3), (2, 3, 4), (2, 4, 1), (3, 1, 2), (3, 2, 4), (3, 3, 1),
    # (3, 3, 2), (3, 4, 1), (4, 2, 3), (4, 3, 1), (4, 3, 2), (4, 4, 1)]
    for a, b, c in r:
        print(use_abc_to_generate_seq(5, a, b, c))


def test():
    assert test_are_all_factors(N=64, primes=primes_N64)
    #assert try_abc(64, primes_N64, 21, 35, 4)

    for a,b,c in abc_part_N64:
        assert try_abc(64, primes_N64, a,b,c)

def all_abc_N64():

    for z in all_abc(N=64, primes=primes_N64):
        print(z)

#test()









    
