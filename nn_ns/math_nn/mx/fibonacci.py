
# 0, 1, 1, 2, 3...
'''
K = (k[M-1], k[M-2], ..., k[0])
k[0] != 0
K, A(0) is given
rule:
A(n) = (a[n+M-1], a[n+M-2], ..., a[n+0])^t
a[n+M] = inner_product(K, A(n))

A(n+1) = T(K) * A(n) = T**(n+1) * A(0)
T(K) = [[K]
        [I(:-1,:)]]


for fibonacci:
K = [1, 1]
A(0) = [1, 0]^t
T = [[1, 1]
     [1, 0]]



note T = [A(1), A(0)]
T**n = T**(n-1) * [A(1), A(0] = [A(n), A(n-1)] = [A(n), T\A(n)] = f(A(n))

given A(i), A(j)
A(i+j) = T**i * A(j) = f(A(i)) * A(j)

note T^t == T
A(i)^t * A(j) = A(0)^t * (T**i)^t * (T**j)*A(0) = A(0)^t *(T**(i+j))*A(0)
    = a(i+j+1)

'''
from ..math_func import calc_power, inner_product
from .Matrix import Matrix
#from sand import dt, getDt
from ..MulFloat import fabonacciByGoldenRatio


__all__ = ('FibonacciPair, nth_FibonacciPair, '
           'fibonacciByAdd, fibonacciByMxMul, '
           'fibonacciByFibonacciPairMul, fabonacciByGoldenRatio'
           .split(', '))



def fibonacciByAdd(n):
    f0 = 0
    f1 = 1
    fn = f0
    fn1 = f1
    for _ in range(n):
        fn, fn1 = fn1, fn1+fn
    return fn

def fibonacciByMxMul(n):
    F10 = Matrix([[1],
                  [0]
                  ])
    mx = Matrix([[1,1],
                 [1,0]
                 ])
    I = mx.identity(2)
    t = calc_power(I, [mx], n)
    Fn1n = t*F10
    return Fn1n[1][0]


class FibonacciPair:
    def __init__(self, pair=(1,0)):
        a1, a0 = pair
        self.pair = (a1, a0) # (F[n+1], F[n])
    @staticmethod
    def getZero(): # mul zero : I = T**0
        return FibonacciPair()
    @staticmethod
    def getOne(): # mul one : T
        return FibonacciPair((1,1))
    def toT(self):
        a1, a0 = self.pair
        a_1 = a1 - a0 # F[n-1]
        return [(a1, a0), (a0, a_1)] # [P[n], P[n-1]]
    def toFn(self):
        return self.pair[1]
    def __mul__(self, other):
        '''P[n]*P[m] = ((F[n+1], F[n]) * (F[m+1], F[m])^T, (F[n], F[n-1]) * (F[m+1], F[m])^T)
    = (F[n+m+1], F[n+m])
    = P[n+m]
        '''
        T = self.toT()
        A = other.pair
        r = [inner_product(A, B) for B in T]
        return FibonacciPair(r)


def nth_FibonacciPair(n):
    A0 = FibonacciPair.getZero()
    A1 = FibonacciPair.getOne()
    An = calc_power(A0, [A1], n)
    return An

def fibonacciByFibonacciPairMul(n):
    An = nth_FibonacciPair(n)
    return An.toFn()


_fs = [fibonacciByAdd,
       fibonacciByMxMul,
       fibonacciByFibonacciPairMul,
       fabonacciByGoldenRatio]

def _test1(f):
    data = [0, 1, 1, 2, 3, 5, 8, 13]
    for n, Fn in enumerate(data):
        assert f(n) == Fn

    return


def _testn(fs, n = 100):
    fs = tuple(fs)
    f = fs[0]
    for _ in range(n):
        Fn = f(n)
        for g in fs[1:]:
            assert Fn == g(n)

    return


def _test_all(n=100):
    fs = _fs
    for f in fs:
        _test1(f)
    _testn(fs, n=n)

def _long_test(N=100):
    fs = _fs
    fs.reverse()
    def try_f(f, n):
        try:
            return f(n)
        except Exception as e:
            print(e)
    for i in range(N):
        n = 1 << i
        for f in fs:
            print(i, n)
            dt(try_f, f, n)

def _long_test_fibonacciByMxMul(N=100):
    for i in range(N):
        n = 1 << i
        n -= 1
        #print(i, n)
        dt = getDt(fibonacciByMxMul, n)
        #print('dt/n/(logn+1)=', dt/(n+1)/(i+1))
        #print('dt/n/(logn+1)**2=', dt/(n+1)/(i+1)**2)
        print('dt/n/(logn+1)**2/loglogn=', dt/(n+1)/(i+1)**2/(i.bit_length()+1))
    return
#print(fibonacciByMxMul(1<<14))
#_test(1000)

def _t(n=14, m=None):
    if m == None:
        m = n + 1
    for i in range(n, m):
        save = None
        for f in _fs[1:]:
            r = dt(f, (1<<i)-1)
            if save:
                assert r == save
            else:
                save = r
                print(r)
            



def _ls(n):
    ls = [fibonacciByFibonacciPairMul(i) for i in range(n)]
    return ls



        











