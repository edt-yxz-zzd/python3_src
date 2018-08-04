


from nn_ns.math_nn import nth_FibonacciPair, primes, factor_int
import itertools

class Fibonacci_numbers_like:
    def __init__(self, min_L, numbers, next_num_f, max_length = None):
        assert min_L >= 0

        self.min_L = min_L
        self.numbers = list(numbers)
        assert min_L <= len(self.numbers)

        self.next_num_f = next_num_f
        self.max_len = float('inf') if max_length is None else max_length

    def get_numbers_of_least_len(self, L):
        numbers = self.numbers
        next_num_f = self.next_num_f

        if L > self.max_len:
            raise MemoryError('L > max_length')
        if len(numbers) < L:
            for _ in range(len(numbers), L):
                next_num = next_num_f(numbers)
                numbers.append(next_num)
                
            assert len(numbers) == L


        assert len(numbers) >= L
        return numbers
        
    def number_at_neg(self, n):
        assert n < 0
        raise NotImplementedError('n < 0')

    def __call__(self, n):
        if n < 0:
            return self.number_at_neg(n)
        return self.get_numbers_of_least_len(n+1)[n]
    

def Fibonacci_numbers_next_num_f(numbers):
    #assert len(numbers) >= 2
    return numbers[-1] + numbers[-2]

class Fibonacci_numbers_T(Fibonacci_numbers_like):
    def __init__(self, max_length = None):
        super().__init__(2, [0,1], Fibonacci_numbers_next_num_f, max_length)
    def number_at_neg(self, n):
        assert n < 0
        return F(-n) * (-1)**(n-1)

F = Fibonacci_number = Fibonacci_numbers_T(200000)
Fibonacci_numbers_least_len = F.get_numbers_of_least_len

assert Fibonacci_numbers_least_len(10)[:10] == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
assert len(Fibonacci_numbers_least_len(0)) == 10
assert F(-2) == -1
assert F(-1) == 1

r'''
F[n] = 0 (mod F[m]) <==> F[gcd(n,m)] = gcd(F[n], F[m]) = |F[m]| = F[|m|]
<==> [gcd(n,m) = |m|] if |m| != 2 else [gcd(n,m) = 1 or 2]
<==> [|m|!=2][n==0 mod m] or [|m|=2][1\n]



m!=2: F[n] = 0 (mod F[m]**2) <==> n = k*m*F[m]
    m == 2: F[n] = 0 (mod F[2]**2 = 1) <==> n = k = k/2*2*F[1]

m>=3, F[n] = 0 (mod F[m]**E) ==>> n = k*k1(E,m)*m*F[m]
m>=3, F[n] = 0 (mod m*F[m]**2) ==>> n = k*k2(m)*m*F[m]

1/k1(m) ~=~
    1.0 (m=3)
    0.34
    0.2
    0.13
    0.08
    0.05
    0.06

1/k2(m) ~=~
    0.5
    1.0
    0.2
    0.5
    0.13
    1.0
    0.5

_calc_k1(3, 15)
[0, 1, 1, 1, 3, 5, 8, 13, 21, 17, 55, 89, 144, 233, 377, 305]
 0/2     2/2                 34/2                        610/2
 3*0     3*1                  3*3                        3*5
_calc_k1(4, 9)
[0, 1, 1, 2, 9, 25, 64, 169, 441, 578]
_calc_k1(5, 7)
[0, 1, 1, 4, 27, 125, 512, 2197]

guess
    let d1(m) = 2**([3\m][not 2\(m/3)]) = 1 or 2 if m = 3*(2i-1)= 6i - 3
    d1(m) = 2**[3 == m mod 6]
    k1(2, m) = 1
    k1(3, m) = F[m]/d1(m)
    k1(4, m) = F[m]**2/d1(m)
    k1(5, m) = F[m]**3/d1(m)

    k1(E, m) = F[m]**(E-2)/d1(m), for E >= 3



M = |m|
N = |n|
k in [-inf : +inf]
E = 0:
    F[n] = 0 (mod F[m]**0) <==> n = k
E = 1:
    M=2: F[n] = 0 (mod F[m]**1) <==> n = k
    M!=2: F[n] = 0 (mod F[m]**1) <==> n = k*m
E = 2:
    M=2: F[n] = 0 (mod F[m]**2) <==> n = k
    M!=2: F[n] = 0 (mod F[m]**2) <==> n = k*m*F[m]
E > 2:
    F[n] = 0 (mod F[m]**E) <==> n = k*F[m]**(E-2)/d1(m)*m*F[m]
    <==> n = k*m*F[m]**(E-1)/d1(m)
    where d1(m) = 2**[3 == m mod 6]
    
'''


_MOD1 = lambda m: F(m)**3
_MOD2 = lambda m: m*F(m)**2
def _try_impl(MOD_f, m, k):
    step = m*F(m)
    L = k*step
    row = Fibonacci_numbers_least_len(L)
    M = MOD_f(m)
    #idc1 = [i for i in range(0, L, 1) if row[i] % M == 0]
    idc2 = [i for i in range(0, L, step) if row[i] % M == 0]
    #idc3 = list(range(0, len(row), 2*step))
    #assert idc1 == idc2
    #assert idc1 == idc3
    print('m = {}, k = {}, F(m) = {}, MOD = {}'.format(m,k,F(m),M))
    print(len(idc2)/k)
    print('i/step = i/{} = {}'.format(step, [i//step for i in idc2]))


def _try(MOD_f, M, K=100):
    k = K
    for m in range(3, M):
        _try_impl(MOD_f, m, k)


def _k1(E, m):
    '''F[n] = 0 (mod F[m]**E) ==>> n = k*k1(m)*m*F[m]
k1(m) = n(k=1) / (m * F[m])
n(k=1) = x * step for x=1...
'''
    assert m >= 0
    assert E >= 2
    
    if m < 2:
        return m
    
    d = step = m*F(m)
    k1 = 1
    n = step
    M = F(m)**E


    Pn = Pd = nth_FibonacciPair(d)
    while Pn.toFn() % M:
        n += step
        Pn *= Pd # P[n+d] = P[n]*P[d]

    return n // step
    
    
    
def _calc_k1(E, max_m):
    return [_k1(E, m) for m in range(max_m+1)]
        

'''
_try(_MOD1, 10)
print('\n'*4)
_try(_MOD2, 10)


m = 3, k = 100, F(m) = 2, MOD = 8
1.0
i/step = i/6 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
m = 4, k = 100, F(m) = 3, MOD = 27
0.34
i/step = i/12 = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
m = 5, k = 100, F(m) = 5, MOD = 125
0.2
i/step = i/25 = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
m = 6, k = 100, F(m) = 8, MOD = 512
0.13
i/step = i/48 = [0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96]
m = 7, k = 100, F(m) = 13, MOD = 2197
0.08
i/step = i/91 = [0, 13, 26, 39, 52, 65, 78, 91]
m = 8, k = 100, F(m) = 21, MOD = 9261
0.05
i/step = i/168 = [0, 21, 42, 63, 84]
m = 9, k = 100, F(m) = 34, MOD = 39304
0.06
i/step = i/306 = [0, 17, 34, 51, 68, 85]





m = 3, k = 100, F(m) = 2, MOD = 12
0.5
i/step = i/6 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
m = 4, k = 100, F(m) = 3, MOD = 36
1.0
i/step = i/12 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
m = 5, k = 100, F(m) = 5, MOD = 125
0.2
i/step = i/25 = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
m = 6, k = 100, F(m) = 8, MOD = 384
0.5
i/step = i/48 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
m = 7, k = 100, F(m) = 13, MOD = 1183
0.13
i/step = i/91 = [0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96]
m = 8, k = 100, F(m) = 21, MOD = 3528
1.0
i/step = i/168 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
m = 9, k = 100, F(m) = 34, MOD = 10404
0.5
i/step = i/306 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
>>> 

'''

#_calc_k1(10)


def min_Fdiv_idx(m):
    '''may not return

f(m) = min {n>0| F[n] = 0 (mod m)} if m != 0 else 0
'''
    
    if m == 0:
        return 0

    for i in itertools.count(1):
        if F(i) % m == 0:
            return i
    pass
def min_Fdiv_idc_lt(M):
    return [min_Fdiv_idx(i) for i in range(M)]

'''
min_Fdiv_idc_lt(100)
[0, 1, 3, 4, 6, 5, 12, 8, 6, 12, 15, 10, 12, 7, 24, 20, 12, 9, 12, 18, 30, 8, 30, 24, 12, 25, 21, 36, 24, 14, 60, 30, 24, 20, 9, 40, 12, 19, 18, 28, 30, 20, 24, 44, 30, 60, 24, 16, 12, 56, 75, 36, 42, 27, 36, 10, 24, 36, 42, 58, 60, 15, 30, 24, 48, 35, 60, 68, 18, 24, 120, 70, 12, 37, 57, 100, 18, 40, 84, 78, 60, 108, 60, 84, 24, 45, 132, 28, 30, 11, 60, 56, 24, 60, 48, 90, 24, 49, 168, 60]
'''

'''
min_Fdiv_idx(p**k) = (k>=0)
    p = 2: 3* 2**(k-1-[k>2])
    min_Fdiv_idx(p) * p**(k-1)
    
    


def show(p, K):
    for k in range(1,K):
        print('p={}; k={}; f(p**k)={}'.format(p, k, min_Fdiv_idx(p**k)))
def t1(P, K):
    for p in primes(P):
        show(p, K)
def t2(p , K):
    show(p, K)


t2(2, 10)
p=2; k=1; f(p**k)=3
p=2; k=2; f(p**k)=6
p=2; k=3; f(p**k)=6
p=2; k=4; f(p**k)=12
p=2; k=5; f(p**k)=24
p=2; k=6; f(p**k)=48
p=2; k=7; f(p**k)=96
p=2; k=8; f(p**k)=192
p=2; k=9; f(p**k)=384


t2(3,10)
p=3; k=1; f(p**k)=4
p=3; k=2; f(p**k)=12
p=3; k=3; f(p**k)=36
p=3; k=4; f(p**k)=108
p=3; k=5; f(p**k)=324
p=3; k=6; f(p**k)=972
p=3; k=7; f(p**k)=2916
p=3; k=8; f(p**k)=8748
p=3; k=9; f(p**k)=26244



p=2; k=1; f(p**k)=3
p=2; k=2; f(p**k)=6
p=2; k=3; f(p**k)=6
p=3; k=1; f(p**k)=4
p=3; k=2; f(p**k)=12
p=3; k=3; f(p**k)=36
p=5; k=1; f(p**k)=5
p=5; k=2; f(p**k)=25
p=5; k=3; f(p**k)=125
p=7; k=1; f(p**k)=8
p=7; k=2; f(p**k)=56
p=7; k=3; f(p**k)=392




'''


'''
for n in range(2, 40):
    ps = factor_int(n)
    x = 1
    ls = []
    for p, e in ps:
        f = min_Fdiv_idx(p**e)
        ls.append(f)
        x *= f # here should be lcm()

    f = min_Fdiv_idx(n)
    if not x == f:
        print('n={}; f(n)={}; II f(p**e) {{p**e\\n}} = II{} = {}; '.format(n, f, ls, x))

'''


'''
for p in primes(100):
    r = p%5
    b = r == 2 or r == 3
    T = (b and (F(p+1)%p==0)) or ((not b) and (F(p-1)%p==0)) or r == 0
    if not T:
        print(p, b)
        if not b:
            print(F(p-2), F(p-1)%p)

#'''
    
def show1(p):
    r = p**2 %5
    if r == 1:
        sign = '-1'
        N = p-1
    elif r == 4:
        sign = '+1'
        N = p+1
    else:
        assert r == 0
        assert p == 5
        sign = ''
        N = p

    
    f = min_Fdiv_idx(p)
    assert N%f == 0
    D = N//f
    print('f(p)=f({p})={f} = (p{sign})//{D}'
          ' = II({II})'
          .format(p=p, f=f, sign=sign, D=D, II=factor_int(f)))
        
        
def t11(P):
    for p in primes(P):
        r = p**2 % 5
        if r == 1:
            show1(p)
            f = min_Fdiv_idx(p)
            if f == p-1:
                assert (p-1)%4 # p = 4k+3
            else:
                # assert (p-1)%4 == 0 or 2 # p = 4k+1 or 3
                assert (p-1) % f == 0
                    
    print()
    for p in primes(P):
        r = p**2 % 5
        if r == 4:
            show1(p)
    print()
    for p in primes(P):
        r = p**2 % 5
        if r == 0:
            show1(p)
            break
        
    '''

p=5; k=1; f(p**k)=5
p=11; k=1; f(p**k)=10
p=19; k=1; f(p**k)=18
p=29; k=1; f(p**k)=14  -- (p-1)//2
p=31; k=1; f(p**k)=30
p=41; k=1; f(p**k)=20  -- (p-1)//2
p=59; k=1; f(p**k)=58
p=61; k=1; f(p**k)=15  -- (p-1)//4
p=71; k=1; f(p**k)=70
p=79; k=1; f(p**k)=78
p=89; k=1; f(p**k)=11  -- (p-1)//8

p=2; k=1; f(p**k)=3
p=3; k=1; f(p**k)=4
p=7; k=1; f(p**k)=8
p=13; k=1; f(p**k)=7  -- (p+1)//2
p=17; k=1; f(p**k)=9  -- (p+1)//2
p=23; k=1; f(p**k)=24
p=37; k=1; f(p**k)=19  -- (p+1)//2
p=43; k=1; f(p**k)=44
p=47; k=1; f(p**k)=16  -- (p+1)//3
p=53; k=1; f(p**k)=27  -- (p+1)//2
p=67; k=1; f(p**k)=68
p=73; k=1; f(p**k)=37  -- (p+1)//2
p=83; k=1; f(p**k)=84
p=97; k=1; f(p**k)=49  -- (p+1)//2

'''


    
def t2(p , K):
    show(p, K)


'''
t11(200)
import sympy
from sympy import Matrix, Mod
A = mx = Matrix([[1,1],[1,0]])
I = Matrix([[1,0],[0,1]])
O = Matrix([[0,0],[0,0]])
B = Matrix([[0, -1],[-1, 1]])
def mx_mod(mx, M):
    mx = Matrix(mx)
    for i in range(len(mx)):
        mx[i] %= M
    return mx
assert O == mx_mod(mx**22 - mx**11 - I, 11)

M = lambda mx: mx_mod(mx,2)
#print(M(A**3))

#'''


'''
FF=lambda n:nth_FibonacciPair(n).toFn()
p = 89
f = min_Fdiv_idx(p)
Ff = FF(f)
W=FF(f-1)
print(Ff, W)
t=lambda i:(FF(i*f)-Ff*(W**(i-1)+(i-1)*W**2))%(Ff**2)
for i in range(1,4):
    print(t(i))

'''


def _assert(N):
    FF=lambda n:nth_FibonacciPair(n).toFn()
    ps = iter(primes(N))
    for p in ps:
        # skip p=2
        break
    for p in ps:
        print(p)
        f = min_Fdiv_idx(p)
        Ff = FF(f)
        Fpf = FF(p*f)
        assert Ff % p == 0
        assert Ff % p**2
        assert Fpf % p**3
        assert Fpf % p**2 == 0
_assert(100)



    
        

