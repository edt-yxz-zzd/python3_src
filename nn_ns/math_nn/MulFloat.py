'''
f(u, p) in (u -/+ 0.5) * 2**(-p)
not includes bound
u > 0, p >= 0(p may be negative!! but the error is large: 0.5*2**(-p)), u,p are both interger


f(u, p) = f(v, q) * f(t, e)
= ((v-0.5)*(t-0.5), (v+0.5)*(t+0.5)) * 2**-(q+e)
= (vt+0.25 -/+ 0.5(v+t)) * 2**-(q+e)
let n = ceil(log2(v+t+1))
2**n >= v+t+1 > v+t
vt+0.25 - 0.5(v+t) > vt-0.5*2**n = vt-2**(n-1) = LB
vt+0.25 + 0.5(v+t) =  vt+ 0.5(v+t+0.5) < vt+ 2**(n-1) = UB
k = UB//2**n
LB <= MID = k * 2**n <= UB
MID-2**n <= LB < UB <= MID+2**n

if k = 2*m:
    MID = k * 2**n = m * 2**(n+1)
    m * 2**(n+1) -/+ 2**n
    u = m
if k = 4*m+1:
    MID = k * 2**n = (4*m+1) * 2**n = m*2**(n+2) + 2**n
    m*2**(n+2) -/+ 2**(n+1)
if k = 4*m-1:
    MID = k * 2**n = (4*m-1) * 2**n = m*2**(n+2) - 2**n
    m*2**(n+2) -/+ 2**(n+1)


f(u, p)
= f(m, q+e-(n+1)) if k == 2*m
= f(m, q+e-(n+2)) if k == 4*m -/+1
for k = [vt+ 2**(n-1)]//2**n = [2vt//2**n + 1]//2
    n = ceil(log2(v+t+1))


u(i) = u(i-1)**2
f(u(i)*2**p(i), p(i)) = f(u(i-1)*2**p(i-1), p(i-1))**2
p(i) <= 2p(i-1) - (n+2)
n = ceil(log2(2u(i-1)*2**p(i-1)+1))
2p(i-1) >= p(i) + 2 + ceil(log2(2u(i-1)*2**p(i-1)+1))
given p(N) == 0, calc p(0)??????????



let s=sqrt(5), q = (s + 1)/2, r = (-s + 1)/2,
fibonacci(i) = s(q**i - r**i)/5
since r**n --> 0, consider s*q**n only
s = 2.236... = f(s*2**t//1, t)
5fibonacci(i) ==about== s*q**n = f(s*2**t//1, t)*f(q**i*2**p//1, p)
    0 <= t+p - (ceil(log2(s*2**t+q**i*2**p+1))+2)
    0 <= t+p - 3 - log2(s*2**t+2**i*2**p) = t+p - 3 - log2(s*2**t+2**(i+p))
    2**(t+p - 3) >= s*2**t+2**(i+p)
    2**(t+p - 3) >= 2**(t+2)+2**(i+p)
    p > 5, t > i+3
    let p == 6
    2**(t+3) >= 2**(t+2)+2**(i+6)
    2**(t+2) >= 2**(i+6)
    t >= i+4
    so, to calc fibonacci(i), sqrt(5) should be expanded to i+4 number after float point


    
    
let u(i) = q**2**i < 2**2**i
2p(i-1) >= p(i) + 2 + ceil(log2(2u(i-1)*2**p(i-1)+1))
ceil(log2(2u(i-1)*2**p(i-1)+1)) < ceil(log2(2*2**2**(i-1)*2**p(i-1))) = 1+2**(i-1)+p(i-1)
p(i-1) >= p(i) + 3 + 2**(i-1)
p(i-1)+2**(i-1) + 3(i-1) == p(i)+2**i + 3i
p(0) + 1 + 0 == p(i)+2**i + 3i
let p(i) = 6
p(0) = 5 + 2**i + 3i
p(x) = 6 + 2**i + 3i - 2**x - 3x
so, to calc q**n for fibonacci(n), i=log(n) q should be expanded to p(0) number after float point

p(0) = n + 3log(n) + 5


'''


from sympy import *
from .math_func import calc_power



class MulFloat:
    def __init__(self, i:int=1, p:int=0):
        assert i > 0
        assert p >= 0
        self.i = i
        self.p = p
    def __mul__(self, other):
        i = self.i * other.i
        p = self.p + other.p

        # n = ceil(log2(v+t+1))
        vt1 = self.i + other.i + 1
        n = vt1.bit_length()
        if vt1 > 1 << n:
            n += 1
        
        # k = [vt+ 2**(n-1)]//2**n = [2vt//2**n + 1]//2
        k = i>>(n-1)
        k += 1
        k //= 2

        if k % 2 == 0:
            m = k//2
            p -= (n+1)
        else:
            m = (k+1)//4
            p -= (n+2)

        return MulFloat(m, p)

    def round(self):
        return self.i >> self.p
    def try_to_set_p(self, p):
        if p > self.p:
            raise Exception('p too large')
        elif p == self.p:
            return

        d = self.p - p
        mask = 1 << (d-1)
        half = self.i & mask
        after_half = self.i & (mask-1)
        if after_half == 0 and half:
            d -= 1
        elif half:
            self.i += mask

        self.i >>= d
        self.p -= d
        



        
def fabonacciByGoldenRatio(n):
    if n < 10:
        ls = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        return ls[n]
        
    assert n > 9
    p0 = n + 3* n.bit_length() + 5

    s = sqrt(5) * (1<<(n+4))# + S(1)/2

    s = int(s.round())

    q = GoldenRatio * (1<<p0)
    q = int(q.round())

    fq = MulFloat(q, p0)
    fs = MulFloat(s, n+4)
    #one = MulFloat()
    ls = [fq]
    for x in range(1, n.bit_length()):
        #p(x) = 6 + 2**i + 3i - 2**x - 3x
        px = p0 + 1 - (1<<x) - 3*x
        f = ls[-1]
        f = f*f
        f.try_to_set_p(px)
        ls.append(f)
        
    assert len(ls) == n.bit_length()
    fqn = calc_power(None, ls, n)
    assert len(ls) == n.bit_length()

    sqn = fs * fqn
    sqn = sqn.round()
    #print('sqn', sqn)
    assert sqn % 5 == 0
    fn = sqn//5

    return fn

'''
for n in range(30, 0, -1):
    fn = fabonacciByGoldenRatio(n)
    print(n, fn)

'''
    




























































