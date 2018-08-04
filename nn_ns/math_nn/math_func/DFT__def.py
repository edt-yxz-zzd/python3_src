


# see also: DFT2.py

def DFT__def(X, w, ops):
    n = len(X)
    powers = ops.powers(w, n)
    # assert n > 0
    assert ops.is_one(ops.pow_uint(w, n))
    assert not any(ops.is_one(powers[i]) for i in range(1,n))
    Y = tuple(ops.sum(ops.mul(X[i], powers[(j*i)%n]) for i in range(n))
             for j in range(n))
    return Y

def IDFT__def(Y, w, ops):
    return IDFT_by_DFT(Y, w, ops, DFT=DFT__def)
def IDFT_by_DFT(Y, w, ops, *, DFT:'of len(Y)'):
    n = len(Y)
    if not n: return ()
    w_ = ops.pow_uint(w, n-1)
    nX = DFT(Y, w_, ops)
    X = tuple(ops.try_div_int(nx, n) for nx in nX)
    return X

if __name__ == '__main__':
    from math_nn.ops.IRingOps import ModuloRingOps
    # w^2^m = 2^2^3 = 4^2^2 = 1 mod 2^4+1
    m = 2
    w = 4
    modulus = 2**4+1
    ops = ModuloRingOps(modulus)
    print('w={w}; m={m}; modulus={modulus}'.format(w=w, m=m, modulus=modulus))
    for X in [(0,1,2,3), (2,5,3,8), (2,1,3,0), (1,8,14,5), (1,0,2,1)]:
        Y = DFT__def(X, w, ops)
        X_ = IDFT__def(Y, w, ops)
        print(X, Y, X_)
        assert X == X_



