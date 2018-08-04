

'''

Y = DFT2 X m w[m]
    len(X) == 2^m == len(Y)
    w[m]^(2^m) == 1 != w[m]^2^(m-1)
X = IDFT2 Y m w[m] = (DFT2 Y m (w[m]^(2^m-1)))/(2^m)

0<=j<2^m:
    Y[j] = sum w[m]^(j*i)*X[i] {0<=i<2^m}
         = sum w[m]^(j*2i)*X[2i] {0<=i<2^(m-1)}
         + sum w[m]^(j*(2i+1))*X[2i+1] {0<=i<2^(m-1)}
         = sum w[m]^(j*2i)*X[2i] {0<=i<2^(m-1)}
         + w[m]^j * sum w[m]^(j*2i)*X[2i+1] {0<=i<2^(m-1)}
         = sum w[m-1]^(j*i)*X[2i] {0<=i<2^(m-1)}
         + w[m]^j * sum w[m-1]^(j*i)*X[2i+1] {0<=i<2^(m-1)}
         = (DFT2 X[::2] (m-1) w[m-1])[j mod 2^(m-1)]
         + w[m]^j * (DFT2 X[1::2] (m-1) w[m-1])[j mod 2^(m-1)]
0<=j<2^(m-1):
    Even = DFT2 X[::2] (m-1) w[m-1]
    Odd = DFT2 X[1::2] (m-1) w[m-1]
    Odd_t = Odd .* [w[m]^j | j <- [0..2^(m-1)-1]]
    Y[j] = Even[j] + Odd_t[j]
    if w[m]^2^(m-1) == -1:
        Y[j+2^(m-1)] = Even[j] - Odd_t[j]



K = ??
    X = IDFT2 Y m w[m] = (DFT2 Y m (w[m]^(2^m-1)) * K
    X[j] = K * sum w[m]^(-j*i) * Y[i] {0<=i<2^m}
         = K * sum w[m]^(-j*i) * sum w[m]^(i*k)*X[k] {0<=k<2^m} {0<=i<2^m}
         = K * sum sum w[m]^(-j*i) * w[m]^(i*k)*X[k] {0<=k<2^m} {0<=i<2^m}
         = K * sum sum w[m]^((k-j)*i) * X[k] {0<=k<2^m} {0<=i<2^m}
         = K * sum sum w[m]^((k-j)*i) * X[k] {0<=i<2^m} {0<=k<2^m}
         = K * sum sum w[m]^((k-j)*i) {0<=i<2^m} * X[k] {0<=k<2^m}
         = K * sum (sum w[m]^((k-j)*i) {0<=i<2^m} * [k == j]
                   + sum w[m]^((k-j)*i) {0<=i<2^m} * [k != j]
                   * X[k] {0<=k<2^m}
         = K * sum (2^m * [k == j]
                   + 0 * [k != j]) # ???????????
                   * X[k] {0<=k<2^m}
         = K * 2^m * X[j]
    ==>> K = 1/(2^m)  # ?????? inversable??
'''

__all__ = '''
    DFT2
    IDFT2
    DFT_by_DFT2
    '''.split()
from math_nn.ops.IRingOps import ModuloRingOps

def DFT_by_DFT2(X, w, ops):
    # to compatible with API of DEF__def.py
    m = len(X).bit_length() - 1
    assert len(X) == 2**m
    return DFT2(X, m, w, ops)



def DFT2(X, m, w, ops):
    assert type(X) is tuple
    assert type(m) is int
    assert X
    assert m >= 0
    assert len(X) == 2**m
    assert ops.is_one(ops.pow_uint(w, 2**m))
    assert m == 0 or not ops.is_one(ops.pow_uint(w, 2**(m-1)))
    if m > 0:
        pow_w_half = ops.pow_uint(w, 2**(m-1))
        # pow_w_half may not be neg_one!!
        if ops.is_neg_one(pow_w_half):
            def butterfly(even, odd_t):
                left_half = ops.add(even, odd_t)
                right_half = ops.sub(even, odd_t)
                return left_half, right_half
        else:
            def butterfly(even, odd_t):
                left_half = ops.add(even, odd_t)
                odd_t = ops.mul(odd_t, pow_w_half)
                right_half = ops.add(even, odd_t)
                return left_half, right_half
    def ThisFunc(X, m, w):
        if m == 0:
            return X
        # print(ops.neg(ops.one), ops.pow_uint(w, 2**(m-1)))
        # assert ops.neg(ops.one) == ops.pow_uint(w, 2**(m-1))
        # may not inversable
        w2 = ops.pow_uint(w,2)
        Even = ThisFunc(X[::2], m-1, w2)
        Odd = ThisFunc(X[1::2], m-1, w2)
        Odd_t = tuple(ops.mul(odd, t) for odd, t in zip(Odd, ops.iter_powers(w)))
        Y = [None] * len(X)
        half = 2**(m-1)
        for i in range(half):
            even = Even[i]
            odd_t = Odd_t[i]
            Y[i], Y[i+half] = butterfly(even, odd_t)
        return tuple(Y)
    return ThisFunc(X, m, w)

def IDFT2(Y, m, w, ops):
    w_ = ops.pow_uint(w, 2**m -1)
    X = DFT2(Y, m, w_, ops)
    L = 2**m
    X = tuple(ops.try_div_int(x, L) for x in X)
    return X



if __name__ == '__main__':
    # w^2^m = 3^2^2 = 1 mod 2^4; but gcd(2^m, 2^4) != 1, not inversable
    modulus = 16
    ops = ModuloRingOps(modulus)
    w = 3
    m = 2
    print('w={w}; m={m}; modulus={modulus}'.format(w=w, m=m, modulus=modulus))
    for X in [(0,1,2,3), (2,5,3,8), (2,1,3,0), (1,8,14,5), (1,0,2,1)]:
        Y = DFT2(X, m, w, ops)
        X_ = IDFT2(Y, m, w, ops)
        print(X, Y, X_)
        # X_ may not be X

    # w^2^m = 2^2^3 = 4^2^2 = 1 mod 2^4+1
    modulus = 2**4+1
    ops = ModuloRingOps(modulus)
    w = 4
    m = 2
    print('w={w}; m={m}; modulus={modulus}'.format(w=w, m=m, modulus=modulus))
    for X in [(0,1,2,3), (2,5,3,8), (2,1,3,0), (1,8,14,5), (1,0,2,1)]:
        Y = DFT2(X, m, w, ops)
        X_ = IDFT2(Y, m, w, ops)
        print(X, Y, X_)
        assert X == X_

    modulus = 2**5+1
    print('modulus={modulus}'.format(modulus=modulus))
    ops = ModuloRingOps(modulus)
    for x in range(ops.modulus):
        r = ops.pow_uint(x,2)
        ls = [x]
        while r != x:
            ls.append(r)
            r = ops.mul(r, x)
        print(x, len(ls))



