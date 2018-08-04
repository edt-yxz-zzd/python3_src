
'''
non singular N*N matrix M
M = RowInterchange * L * U
L = [[1, 0, 0],
     [a, 1, 0],
     [b, c, 1],]
U = [[d, e, g],
     [0, f, h],
     [0, 0, i],]
'''








from ..math_func import inner_product, numv_product, vadd, vsub
from .Matrix import *

class SingularExcept(Exception):
    pass

def LUdecomposition(mx):
    R, C = size = mx.size()
    assert R == C
    mx = mx.copy()
    one = mx.getArgs().one
    zero = mx.getArgs().zero
    
    lu = LUdecomposition_inplace(mx)
    L = Matrix.identity(R, one=one, zero=zero)
    U = Matrix.zeros(size, zero=zero)
    for r in range(R):
        for c in range(r):
            L[r][c] = lu.get(r, c)
    for r in range(R):
        for c in range(r, C):
            U[r][c] = lu.get(r, c)

    return lu.getNew2Old(), L, U
            

def LUdecomposition_inplace(mx):
    lu = MxRowInterchange(mx)
    N = mx.row_size()

    one = mx.getArgs().one
    zero = mx.getArgs().zero
    abs = mx.getArgs().abs
    inv = mx.getArgs().inv
    one = mx.getArgs().one
    zero = mx.getArgs().zero

    # find the biggest element of each row for implict pivoting
    scales = []
    for r in range(N):
        biggest = max(abs(lu.get(r, c)) for c in range(N))
        if mx.numEq(biggest, zero):
            raise SingularExcept('singular@LUdecomposition_inplace')
        scales.append(inv(biggest))

    for diagonal_idx in range(N):
        # look for pivote below d_i
        _, r = max([abs(lu.get(r, diagonal_idx))*scales[r], -r] for r in range(diagonal_idx, N))
        r = -r
        if diagonal_idx != r:
            assert diagonal_idx < r < N
            scales[r] = scales[diagonal_idx] # no need to swap
            lu.interchangeRows(r, diagonal_idx)

        pivote = lu.get(diagonal_idx, diagonal_idx)
        if mx.numEq(pivote, zero):
            raise SingularExcept('singular@LUdecomposition_inplace')

        inv_pivote = inv(pivote)
        for r in range(diagonal_idx + 1, N):
            lu.set(r, diagonal_idx, inv_pivote * lu.get(r, diagonal_idx))

        for r in range(diagonal_idx + 1, N):
            temp = lu.get(r, diagonal_idx)
            for c in range(diagonal_idx + 1, N):
                e = temp * lu.get(diagonal_idx, c)
                lu.set(r, c, lu.get(r, c) - e)

    return lu



        

def _test_LUdecomposition(mx):
    try:
        v, L, U = LUdecomposition(mx)
    except SingularExcept:
        return

    LU = L*U
    ls = [None]*LU.row_size()
    for new, old in enumerate(v):
        ls[old] = LU[new]
    LU = Matrix(ls)
    assert LU == mx

def test_LUdecomposition():
    import random
    mx = Matrix([[1, 1], [0, 1]])
    _test_LUdecomposition(mx)
    for R in range(20):
        C = R
        array = list(100000 * random.random() for _ in range(R*C))
        mx = Matrix(array, (R,C))
        
        _test_LUdecomposition(mx)


if __name__ == '__main__':
    test_LUdecomposition()


