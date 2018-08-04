
'''
TODO
1) recur
2) __find_u_k
    use array for small LxLy
3) update ops
    class UnitRoot
    using shift/add to def mul

'''

'''
Schonhage_Strassen_algorithm

x % (B^n+1) = x%B^n - (x//B^n) % (B^n+1)
    x % (B^n+1) = (x//B^n*B^n + x%B^n) % (B^n+1)
                = (x//B^n*B^n) % (B^n+1) + (x%B^n) % (B^n+1)
                = ((x//B^n)*(B^n % (B^n+1))) % (B^n+1) + (x%B^n) % (B^n+1)
                = ((x//B^n)*(-1)) % (B^n+1) + (x%B^n) % (B^n+1)
                = -(x//B^n) % (B^n+1) + (x%B^n) % (B^n+1)
                = -(x//B^n) % (B^n+1) + (x%B^n)
                = (x%B^n) - (x//B^n) % (B^n+1)

convolution:
    x = sum X[i]*B^i {0<=i<Lx}
    y = sum Y[i]*B^i {0<=i<Ly}
    0<=X[i]<B
    0<=Y[i]<B
    carry :: UInt -> UInt -> [Int] -> [Int]
    __carry :: UInt -> UInt -> [Int] -> [Int]
    carry B 0 [] = []
    carry B prev_carry [] = __carry B prev_carry []
    carry B prev_carry (h:ts) = __carry B (prev_carry+h) ts
    __carry B (-1) [] = [-1]  # for negacyclic_convolution
    __carry B head ts = head%B : carry B (head//B) ts
    as_radix_number :: UInt -> [UInt] -> UInt
    as_radix_number B [] = 0
    as_radix_number B (h:ts) = h + B*(as_radix_number B ts)
    1) linear convolution
        linear_convolution x y = [sum X[i]*Y[j-i] {0<=i<=j} | j <- [0..Lx+Ly-1]]
        (linear_convolution x y)[i] may be large than B
        as_radix_number B . carry B 0 $ linear_convolution x y
            === (as_radix_number B x) * (as_radix_number B y)
    2) negacyclic convolution
        negacyclic_convolution n x y =
            let lc = linear_convolution x y in
            [sum lc[j] {j<-[i,i+2*n..len(lc)-1]}
            -sum lc[j] {j<-[i+n,i+3*n..len(lc)-1]}
            | i <- [0..n-1]]
        (negacyclic_convolution x y)[i] may be large than B
        (negacyclic_convolution x y)[i] may be less than 0
        as_radix_number B . carry B 0 $ negacyclic_convolution n x y
            === (as_radix_number B x) * (as_radix_number B y) % (B^n+1)

        let len(x) == len(y) == n  # all_zeros(x[m:]) and all_zeros(y[n-m:])
        let w:
            w^(2*n) == 1
            all(w^i != 1 for i in [0..2*n-1])
        weight_vector = [w^i | i <- [0..n-1]]
        neg_weight_vector = [w^-i | i <- [0..n-1]]
        vector_mul x y = zipWith (*) x y # point-wise
        (.*) = vector_mul
        assert negacyclic_convolution(x, y) =
            neg_weight_vector.*IDFT(DFT(weight_vector.*x, w^2).*DFT(weight_vector.*y, w^2), w^2)
        wx = weight_vector.*x
            wx[i] = w^i*x[i]
        dft_wx = DFT(wx, w^2)
            dft_wx[j] = sum (w^2)^(j*i)*wx[i] {0<=i<n}
                      = sum w^(2*j*i)*w^i*x[i] {0<=i<n}
                      = sum w^((2*j+1)*i)*x[i] {0<=i<n}
                        let Wj = w^(2*j+1); Wj^n = (w^n)^(2*j+1) = -1
                            # assume w^n == -1
                        = sum Wj^i*x[i] {0<=i<n}
        dwxy = DFT(wx, w^2) .* DFT(wy, w^2)
            dwxy[j] = dft_wx[j] * dft_wy[j]
                    = sum Wj^i*x[i] {0<=i<n} * sum Wj^i*y[i] {0<=i<n}
                    = sum sum Wj^k*x[k] * Wj^i*y[i] {0<=k<n}{0<=i<n}
                    = sum sum Wj^(k+i)*x[k]*y[i] {0<=k<n}{0<=i<n}
                    = sum sum Wj^s*x[k]*y[s-k] {0<=k<=s}{0<=s<n}
                    + sum sum Wj^s*x[k]*y[s-k] {s-n<k<n}{n<=s<2*n-1}
                    # rhs = sum sum Wj^(s+n)*x[k]*y[s+n-k] {s+n-n<k<n}{n<=s+n<2*n-1}
                    #     = -sum sum Wj^s*x[k]*y[s+n-k] {s<k<n}{0<=s<n-1}
                    = sum sum Wj^s*x[k]*y[s-k] {0<=k<=s}{0<=s<n}
                    - sum sum Wj^s*x[k]*y[s+n-k] {s<k<n}{0<=s<n-1}
                    = sum Wj^(n-1)*x[k]*y[n-1-k] {0<=k<=n-1}
                    + sum sum Wj^s*x[k]*y[s-k] {0<=k<=s}{0<=s<n-1}
                    - sum sum Wj^s*x[k]*y[s+n-k] {s<k<n}{0<=s<n-1}
                    = sum Wj^(n-1)*x[k]*y[n-1-k] {0<=k<=n-1}
                    + sum Wj^s *
                        (sum x[k]*y[s-k] {0<=k<=s} - sum x[k]*y[s+n-k] {s<k<n})
                        {0<=s<n-1}
                    = Wj^(n-1)*negacyclic_convolution(x, y)[n-1]
                    + sum Wj^s * negacyclic_convolution(x,y)[s] {0<=s<n-1}
                    = sum Wj^s * negacyclic_convolution(x,y)[s] {0<=s<n}
                    = DFT(weight_vector.*negacyclic_convolution(x,y), w^2)


nx, ny
Lx, Ly = nx.bit_len, ny.bit_len
X, Y = to_radix (2^u) nx, to_radix (2^u) ny
LX, LY = len(X), len(Y)
x = X+[0]*(n-len(X))
y = Y+[0]*(n-len(Y))
n == len(x) == len(y) == 2^k # 0 <= x[i] < 2^u
LX+LY = ceil(Lx/u) + ceil(Ly/u) < (Lx+Ly)/u + 2
requires: n >= LX+LY
    <<== requires: 2^k >= (Lx+Ly)/u + 2
any_digit < 2^u
any_convolution_digit <= n * (any_digit^2) < 2^k*2^(2u) = 2^(k+2u)
w^(2*n) mod B == 1 # w^i mod B != 1
B = 2^(s*n) + 1 = 2^(s*2^k)+1
w = 2^s # w^n mod B == -1

requires: any_convolution_digit < B
    <<== requires: 2^(k+2u) <= B
    <<== requires: k+2u <= s*n = s*2^k


to find (u,k,s):
    # min k, s
    input: Lx, Ly
    output: u, k, s
    requires:
        LxLy/u + 2 <= 2^k # LxLy = Lx+Ly
        k+2u <= s*2^k
    let s*LxLy/u+2*s == s*2^k == k+2u
    s*LxLy/u+2*s = k+2u
    2uu - (2s-k)u - s*LxLy = 0
    u = ((2s-k) + sqrt((2s-k)^2 + 8s*LxLy))/2

    if s == 1:
        u ~= sqrt(2*LxLy)
'''

from .DFT__def import DFT__def, IDFT_by_DFT
from math_nn.ops.IRingOps import ModuloRingOps
from nn_ns.math_nn.floor_sqrt import floor_sqrt

from nn_ns.Bijection.ArbitraryRadixNumber import \
    number2arbitrary_radix_reprLE, arbitrary_radix_reprBE2number
from .DFT2 import DFT2, DFT_by_DFT2



def __u2k(LxLy, u):
    assert u > 0
    # n = max(LxLy/u+2, k+2*u)
    n = (LxLy+u-1)//u+2
    k = n.bit_length() - 1
    if 2**k < n:
        k += 1
        assert 2**k >= n
        n = 2**k
    assert n == 2**k
    while n < k+2*u:
        k += 1
        n *= 2
    return k
def __find_u_k(LxLy):
    # s == 1
    assert LxLy >= 0
    r = floor_sqrt(2*LxLy)
    r = max(1, r)
    kr = __u2k(LxLy, r)
    #return r, kr
    #print(r)
    m = max(1, r-4)
    M = r+4
    k, u = min((__u2k(LxLy, u), u) for u in range(m, M))
    for u in range(m, M):
        k = __u2k(LxLy, u)
        print(LxLy, u, k)
    print(k, kr)
    return u, k
    assert kr == k
    return r, kr

def _try__find_u_k():
    for LxLy in range(0, 20):
        print(LxLy)
        print(__find_u_k(LxLy))
# _try__find_u_k()


def carry(B, prev_carry, convolution):
    assert all(type(x) is int for x in convolution)
    assert B > 0
    ls = []
    for head in convolution:
        head = prev_carry + head
        prev_carry, head = divmod(head, B)
        ls.append(head)
    while prev_carry:
        if prev_carry == -1:
            ls.append(-1)
            break
        prev_carry, head = divmod(prev_carry, B)
        ls.append(head)
    return tuple(ls)

def negacyclic_convolution__def(n, x, y):
    lc = linear_convolution(x, y)
    ls = (sum(lc[i::2*n]) - sum(lc[i+n::2*n]) for i in range(n))
    return tuple(ls)
def linear_convolution(x, y):
    ls = []
    Ly = len(y)
    Lx = len(x)
    n = Lx + Ly - 1
    for i in range(n):
        begin = 0 if Ly > i else i - (Ly - 1)
        end = min(i+1, Lx)
        s = sum(x[j]*y[i-j] for j in range(begin, end))
        ls.append(s)
    return tuple(ls)

assert linear_convolution([3,2,1], [6,5,4]) == (18, 27, 28, 13, 4)
assert carry(10, 0, (18, 27, 28, 13, 4)) == (8,8,0,6,5)
assert negacyclic_convolution__def(3, [3,2,1], [6,5,4]) == (5, 23, 28)
assert carry(10, 0, (5, 23, 28)) == (5,3,0,3)



def __DFTW(x, w, ops, *, DFT=DFT__def):
    n = len(x)
    assert ops.is_one(ops.pow_uint(w, 2*n))
    assert not any(ops.is_one(ops.pow_uint(w, i)) for i in range(1,2*n))
    weight_vector = ops.powers(w, n)
    wx = ops.vector_mul(weight_vector, x)
    w2 = ops.pow_uint(w, 2)
    dft_wx = DFT(wx, w2, ops)
    return dft_wx
def negacyclic_convolution__DFT(x, y, w, ops, *, DFT:'of len(X)'=DFT__def, IDFT=None):
    n = len(x)
    assert len(x) == len(y)
    assert ops.is_one(ops.pow_uint(w, 2*n))
    assert not any(ops.is_one(ops.pow_uint(w, i)) for i in range(1,2*n))
    if not n: return ()
    # bug: w_ = ops.pow_uint(w, n-1) # 'n-1' should be '2*n-1'
    w_ = ops.pow_uint(w, 2*n-1)
    assert ops.is_one(ops.mul(w, w_))
    weight_vector = ops.powers(w, n)
    neg_weight_vector = ops.powers(w_, n)
    wx = ops.vector_mul(weight_vector, x)
    wy = ops.vector_mul(weight_vector, y)
    w2 = ops.pow_uint(w, 2)
    if IDFT is None:
        def IDFT(Y, w, ops):
            return IDFT_by_DFT(Y, w, ops, DFT=DFT)
    idft = IDFT(ops.vector_mul(DFT(wx, w2, ops), DFT(wy, w2, ops)), w2, ops)
    return ops.vector_mul(neg_weight_vector, idft)

def t():
    modulus = 7
    n = 3
    'w^(2*n) == 1 mod 7'
    w = 3
    ops = ModuloRingOps(modulus)
    nc = negacyclic_convolution__DFT([3,2,1], [6,5,4], w, ops)
    print(nc)
    print((5, 23, 28))
    print((5, 23%modulus, 28%modulus))
    '''
    (5, 2, 0)
    (5, 23, 28)
    (5, 2, 0)
    '''

    modulus = 97
    n = 3
    'w^(2*n) == 1 mod 97'
    w = pow(5, 96//(2*n), 97)
    ops = ModuloRingOps(modulus)
    nc = negacyclic_convolution__DFT([3,2,1], [6,5,4], w, ops)
    print(nc)
    print((5, 23, 28))
    print((5, 23%modulus, 28%modulus))
    '''
    (5, 23, 28)
    (5, 23, 28)
    (5, 23, 28)
    '''

t()


def Schonhage_Strassen_algorithm__native_norecur(nx, ny):
    assert nx > 0
    assert ny > 0
    Lx = nx.bit_length()
    Ly = ny.bit_length()
    LxLy = Lx + Ly
    s = 1
    u, k = __find_u_k(LxLy)

    M = 2**u
    n = 2**k
    B = 2**n + 1
    w = 2
    ops = ModuloRingOps(B)
    assert B > M

    X = number2arbitrary_radix_reprLE(nx, M, 0, divmod)
    Y = number2arbitrary_radix_reprLE(ny, M, 0, divmod)
    assert len(X) <= n
    assert len(Y) <= n
    x = X + (0,)*(n-len(X))
    y = Y + (0,)*(n-len(Y))
    assert n == len(x) == len(y)

    z = negacyclic_convolution__DFT(x, y, w, ops, DFT=DFT_by_DFT2)
    nz = arbitrary_radix_reprBE2number(reversed(z), M, 0)
    return nz

for nx, ny in [(1,1), (1,2), (2,1), (2,2), (3,3), (4,4), (5,6), (2423423,242535)]:
    nz = Schonhage_Strassen_algorithm__native_norecur(nx, ny)
    assert nz == nx*ny

