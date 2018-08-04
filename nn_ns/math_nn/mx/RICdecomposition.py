
'''
R*C matrix M with rank r
R[2]*R[1]*R[0]*M*C[0]*C[1]*C[2] = P

P = [[I B]
     [O O]]
I is the r*r identity
B is a r*(C-r) matrix


P's nullspace PN is [[-B],  a C*(C-r) matrix; J is a (C-r)*(C-r) mx
                     [J]]
Rs*M*Cs*PN = P*PN = O
M*(Cs*PN) = O
M's nullspace MN is C[0]*C[1]*C[2]*PN
'''









from .Matrix import *

def RICdecomposition(mx):
    R, C = size = mx.size()
    #NOOOOOOOOOOoo assert R == C
    mx = mx.copy()
    mxI = MxRCInterchange(mx)
    #N = R

    abs = mx.getArgs().abs
    one = mx.getArgs().one
    zero = mx.getArgs().zero
    inv = mx.getArgs().inv

    
    d = -1
    mxRs = []
    mxCs = []
    
    for d in range(min(R, C)):
        biggest = 0
        ir = ic = None
        for r in range(d, R):
            for c in range(d, C):
                if abs(mxI.get(r, c)) > biggest:
                    ir, ic = r, c
                    biggest = mxI.get(r, c)
                    
        if ir == None:
            break #end
        
        

        if d != ir:
            mxI.interchangeRows(d, ir)
            mxRs.append((d, ir))
        if d != ic:
            mxI.interchangeColumns(d, ic)
            mxCs.append((d, ic))

        pivote = mxI.get(d, d)
        if abs(pivote) != one:
            scale = inv(pivote)
            mxRs.append(((d, scale),))
            for c in range(d, C):
                e = mxI.get(d, c)
                e *= scale
                mxI.set(d, c, e)

        for r in range(R):
            if r == d:
                continue
            e = mxI.get(r, d)
            if not e:
                continue
            scale = -e
            mxRs.append(((d, scale), r))
            for c in range(d, C):
                e = mxI.get(r, c)
                e += mxI.get(d, c) * scale
                mxI.set(r, c, e)

    else:
        d += 1
        assert d == min(R, C)

    for i in range(d):
        if not mx.numEq(mxI.get(i, i), one):
            print(mx)
            print(mxI)
        assert mx.numEq(mxI.get(i, i), one)

    for r in range(R):
        for c in range(C):
            if r == c < d:
                continue
            if c >= d and r < d:
                continue
            if not mx.numEq(mxI.get(r, c), zero):
                print(mx)
                print(mxI)
            assert mx.numEq(mxI.get(r, c), zero)

    tmp = mxI
    mxI = Matrix.zeros((R, C))
    for i in range(d):
        mxI[i][i] = one
    for r in range(d):
        for c in range(d, C):
            mxI[r][c] = tmp.get(r, c)

    nullspace = Matrix.zeros((C, C-d), zero=zero)
    if C-d:
        zeros = Matrix.zeros((R, C-d), zero=zero)
        if mxI * nullspace != zeros:
            print(mxI)
            print(nullspace)
        assert mxI * nullspace == zeros

        
        for r in range(d):
            for c in range(d, C):
                nullspace[r][c-d] = -mxI[r][c]
        for r in range(d, C):
            c = r - d
            nullspace[r][c] = one
        for ct in reversed(mxCs):
            c1, c2 = ct
            assert isinstance(c1, int)
            rt = exchangeRCTransform(ct) # no need. since ct must be (c1,c2)
            #rt = inverseRCTransform(rt)
            transformRow(rt, nullspace)

    rank = d
    return rank, (R,C), mxRs, mxI, mxCs, nullspace




def _test_RICdecomposition(mx):
    rank, (R,C), mxRs, mxI, mxCs, nullspace = RICdecomposition(mx)
    zero = mx.getArgs().zero
    inv = mx.getArgs().inv
    if rank < C:
        zeros = Matrix.zeros((R, nullspace.column_size()), zero=zero)
        if mx * nullspace != zeros:
            print(mx)
            print(nullspace)
            print(mx * nullspace)
            print(zeros)

            tmp = nullspace.copy()
            for ct in reversed(mxCs):
                rt = exchangeRCTransform(ct)
                transformRow(rt, tmp)
            print(tmp)
        assert mx * nullspace == zeros

    mx0 = mx.copy()
    for rt in mxRs:
        transformRow(rt, mx)
    for ct in mxCs:
        transformColumn(mx, ct)
    if mx != mxI:
        print(mx)
        print(mxI)
    assert mx == mxI

    mx = mx0
    for rt in reversed(mxRs):
        rt = inverseRCTransform(rt, inv)
        transformRow(rt, mxI)
    for ct in reversed(mxCs):
        ct = inverseRCTransform(ct, inv)
        transformColumn(mxI, ct)
    if mx != mxI:
        print(mx)
        print(mxI)
    assert mx == mxI


def test_RICdecomposition():
    import random
    mx = Matrix([[1, 1], [0, 1]])
    _test_RICdecomposition(mx)
    for R in range(20):
        for C in range(max(0, R-1), R+2):
            array = list(100000 * random.random() for _ in range(R*C))
            mx = Matrix(array, (R,C))
            
            _test_RICdecomposition(mx)


    mx_ls = [
        [(0,)],
        [(0,1),(0,0)],
        [(1,3),(2,6)],
        [(0,0),(0,1)],
        [],
        ]

    for mx in mx_ls:
        mx = Matrix(mx)
        _test_RICdecomposition(mx)














            
if __name__ == '__main__':
    test_RICdecomposition()


















