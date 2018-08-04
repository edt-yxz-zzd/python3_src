
from math_func import inner_product, numv_product, vadd, vsub

'''
class Mod2Field:
    def __init__(self, real:int=0, image:int=0):
        self.real, self.image = real, image
        self.normalize()
    def normalize(self):
        self.real &= 1
        self.image &= 1
    def copy(self):
        return Mod2Field(*self.toPair())
    def toPair(self):
        return (self.real, self.image)
    def __eq__(self, other):
        return self.toPair() == other.toPair()
    def __ne__(self, other):
        return not (self == other)
    def __mul__(self, other):
        real = self.real * other.real - self.image * other.image
        image = self.image * other.real + self.real * other.image
        return Mod2Field(real, image)
    
    def __add__(self, other):
        real = self.real + other.real
        image = self.image + other.image
        return Mod2Field(real, image)
    
    def __sub__(self, other):
        real = self.real - other.real
        image = self.image - other.image
        return Mod2Field(real, image)

    @staticmethod
    def getZero():
        return Mod2Field()
    @staticmethod
    def getOne():
        return Mod2Field(1)
    def inv(self):
        if self == self.getZero():
            raise Exception('inv zero')
        jlkjjjlkjl no such thing !!!!!!!!!!!!!!!!!!!1
    def __repr__(self):
        return 'Mod2Field{}'.format(self.toPair())

'''


'''
class MatrixArgs:
    def __init__(self, threshold=1e-6, one=1, zero=0, abs=abs, inv=None, sqrt=math.sqrt):
        self.threshold, self.one, self.zero, self.abs, self.inv, self.sqrt = \
                        threshold, one, zero, abs, inv, sqrt
        if inv == None:
            self.inv = lambda x: self.one/x
        if threshold == None or threshold == zero:
            self.eq = lambda x, y: x == y
        else:
            self.eq = lambda x, y: self.abs(x - y) <= self.threshold
            
class Matrix:
    @staticmethod
    def identity(N, ones=1, zero=0):
        v = [ones]*N
        mx = Matrix.diagonal(v, zero=zero)
        return mx
    
    @staticmethod
    def diagonal(v, size=None, zero=0):
        if size == None:
            R = C = len(v)
            size = R, C
        mx = Matrix.zeros(size, zero=zero)
        
        R, C = size
        for d_idx in range(min(R,C)):
            mx[d_idx][d_idx] = v[d_idx]
        return mx
    @staticmethod
    def zeros(size, zero=0):
        R, C = size
        mx = [[zero for c in range(C)] for r in range(R)]
        return Matrix(mx)

    def copy(self):
        return Matrix(self.getMx(), threshold=self.threshold)
    def __init__(self, mx, size=None, mxargs:MatrixArgs = MatrixArgs()):
        if size != None:
            R, C = size
            array = mx
            mx = [[array[r*C + c] for c in range(C)] for r in range(R)]
        else:
            R = len(mx)
            if R == 0:
                mx = []
            else:
                R, C = size = len(mx), len(mx[0])
                mx = [[mx[r][c] for c in range(C)] for r in range(R)]
        if R == 0 or C == 0:
            size = 0,0
            mx = []
            
        self.mx = mx
        #self._size = size
        self.args = mxargs
        
    def size(self):
        mx = self.mx
        if not mx:
            return 0,0
        
        return len(mx), len(mx[0])
    def getMx(self):
        return self.mx
    def getArgs(self):
        return self.args

    def numEq(self, a, b):
        return self.args.eq(a, b)
    def transpose(self):
        R, C = self.size()
        mx = self.zeros((C, R))
        for r in range(R):
            for c in range(C):
                mx[c][r] = self.mx[r][c]
        return mx
    
    def __eq__(self, other):
        #return self.size() == other.size() and self.mx == other.mx
        if self.size() != other.size():
            return False

        R, C = self.size()
        for r in range(R):
            for c in range(C):
                if not self.numEq(self[r][c], other[r][c]):
                    return False
        return True
        
    def __ne__(self, other):
        return not (self == other)
    def __mul__(self, other):
        R = self.row_size()
        M = SC = self.column_size()
        OR = other.row_size()
        C = other.column_size()
        assert SC == OR
        
        mx = Matrix.zeros((R,C), zero=None)
        for r in range(R):
            for c in range(C):
                mx[r][c] = sum(self[r][i] * other[i][c] for i in range(M))

        return mx
    
    def __add__(self, other):
        assert self.size() == other.size()
        mx = Matrix.zeros(self.size(), zero=None)
        for r in range(self.row_size()):
            for c in range(other.column_size()):
                mx[r][c] = self[r][c] + other[r][c]

        return Matrix(mx)
    def __sub__(self, other):
        assert self.size() == other.size()
        mx = Matrix.zeros(self.size(), zero=None)
        for r in range(self.row_size()):
            for c in range(other.column_size()):
                mx[r][c] = self[r][c] - other[r][c]

        return Matrix(mx)
    def __neg__(self):
        mx = Matrix.zeros(self.size(), zero=None)
        for r in range(self.row_size()):
            for c in range(self.column_size()):
                mx[r][c] = -self[r][c]

        return Matrix(mx)
    
    def get(self, r, c):
        return self.mx[r][c]
    def set(self, r, c, v):
        self.mx[r][c] = v
        
    def __setitem__(self, r, v):
        self.mx[r] = v
    def __getitem__(self, r):
        return self.mx[r]
        
    def row_size(self):
        return self.size()[0] 
    def column_size(self):
        return self.size()[1] 
        
    def __repr__(self):
        return 'Matrix({mx})'.format(mx = self.mx)

class MxRowInterchange:
    def __init__(self, mx):
        self.mx = mx
        self.new2old = list(range(mx.row_size()))
    def getMx(self):
        return self.mx
    def getNew2Old(self):
        return self.new2old
    
    def get(self, r, c):
        r = self.new2old[r]
        return self.mx.get(r,c)
    def set(self, r, c, v):
        r = self.new2old[r]
        self.mx.set(r, c, v)
    def interchangeRows(self, a, b):
        self.new2old[a], self.new2old[b], = self.new2old[b], self.new2old[a],''' 

def LUdecomposition(mx):
    R, C = size = mx.size()
    assert R == C
    mx = Matrix(mx.getMx())
    lu = LUdecomposition_inplace(mx)
    L = Matrix.identity(R)
    U = Matrix.zeros(size)
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

    # find the biggest element of each row for implict pivoting
    scales = []
    for r in range(N):
        biggest = max(abs(lu.get(r, c)) for c in range(N))
        if not biggest:
            raise Exception('singular@LUdecomposition_inplace')
        scales.append(1/biggest)

    for diagonal_idx in range(N):
        # look for pivote below d_i
        _, r = max([abs(lu.get(r, diagonal_idx))*scales[r], -r] for r in range(diagonal_idx, N))
        r = -r
        if diagonal_idx != r:
            assert diagonal_idx < r < N
            scales[r] = scales[diagonal_idx]
            lu.interchangeRows(r, diagonal_idx)

        pivote = lu.get(diagonal_idx, diagonal_idx)
        if not pivote:
            raise Exception('singular@LUdecomposition_inplace')

        inv_pivote = 1/pivote
        for r in range(diagonal_idx + 1, N):
            lu.set(r, diagonal_idx, inv_pivote * lu.get(r, diagonal_idx))

        for r in range(diagonal_idx + 1, N):
            temp = lu.get(r, diagonal_idx)
            for c in range(diagonal_idx + 1, N):
                e = temp * lu.get(diagonal_idx, c)
                lu.set(r, c, lu.get(r, c) - e)

    return lu



class MxRCInterchange:
    def __init__(self, mx):
        self.mx = mx
        self.row_new2old = list(range(mx.row_size()))
        self.col_new2old = list(range(mx.column_size()))
    def getMx(self):
        return self.mx
    def getNew2Old(self):
        return self.row_new2old, self.col_new2old
    
    def get(self, r, c):
        r = self.row_new2old[r]
        c = self.col_new2old[c]
        return self.mx.get(r,c)
    def set(self, r, c, v):
        r = self.row_new2old[r]
        c = self.col_new2old[c]
        self.mx.set(r, c, v)
    def interchangeRows(self, a, b):
        new2old = self.row_new2old
        new2old[a], new2old[b], = new2old[b], new2old[a],
    def interchangeColumns(self, a, b):
        new2old = self.col_new2old
        new2old[a], new2old[b], = new2old[b], new2old[a],
    def row_size(self):
        return self.mx.row_size()
    def column_size(self):
        return self.mx.column_size()
    def size(self):
        return self.mx.size()


def transformRow(t, mx):
    #(r1,r2), ((r, scale),), ((r1, scale), r2)
    if len(t) == 1:
        ((r, scale),) = t
        for c in range(mx.column_size()):
            e = mx.get(r, c)
            e *= scale
            mx.set(r, c, e)
    else:
        r1s, r2 = t
        if isinstance(r1s, int):
            r1 = r1s
            for c in range(mx.column_size()):
                e1 = mx.get(r1, c)
                e2 = mx.get(r2, c)
                mx.set(r1, c, e2)
                mx.set(r2, c, e1)
        else:
            r1, scale = r1s
            for c in range(mx.column_size()):
                e1 = mx.get(r1, c)
                e2 = mx.get(r2, c)
                e2 += e1 * scale
                mx.set(r2, c, e2)
    
def transformColumn(mx, t):
    #(c1,c2), ((c, scale),), ((c1, scale), c2)
    if len(t) == 1:
        ((c, scale),) = t
        for r in range(mx.row_size()):
            e = mx.get(r, c)
            e *= scale
            mx.set(r, c, e)
    else:
        c1s, c2 = t
        if isinstance(c1s, int):
            c1 = c1s
            for r in range(mx.row_size()):
                e1 = mx.get(r, c1)
                e2 = mx.get(r, c2)
                mx.set(r, c1, e2)
                mx.set(r, c2, e1)
        else:
            c1, scale = c1s
            for r in range(mx.row_size()):
                e1 = mx.get(r, c1)
                e2 = mx.get(r, c2)
                e2 += e1 * scale
                mx.set(r, c2, e2)
def inverseRCTransform(t, inv):
    #(r1,r2), ((r, scale),), ((r1, scale), r2)
    if len(t) == 1:
        ((r, scale),) = t
        return ((r, inv(scale)),)
    else:
        r1s, r2 = t
        if isinstance(r1s, int):
            r1 = r1s
            return (r2, r1)
        else:
            r1, scale = r1s
            return ((r1, -scale), r2)


def exchangeRCTransform(t):
    #(r1,r2), ((r, scale),), ((r1, scale), r2)
    if len(t) == 1:
        ((r, scale),) = t
        return t
    else:
        r1s, r2 = t
        if isinstance(r1s, int):
            r1 = r1s
            return t
        else:
            r1, scale = r1s
            return ((r2, scale), r1)
        

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
            rt = exchangeRCTransform(ct)
            rt = inverseRCTransform(rt)
            transformRow(rt, nullspace)

    rank = d
    return rank, (R,C), mxRs, mxI, mxCs, nullspace

        
def orthogonalization(mx):
    one = mx.getArgs().one
    zero = mx.getArgs().zero
    inv = mx.getArgs().inv
    sqrt = mx.getArgs().sqrt
    abs = mx.getArgs().abs
    
    R, C = mx.size()
    mxT = mx.transpose()
    ls = []
    for c in range(C):
        column = mxT[c]
        for i in range(c):
            e = ls[i]
            len_on_e = inner_product(e, column)
            v_on_e = numv_product(len_on_e, e)
            column = vsub(column, v_on_e)
        L = sum(abs(i) for i in column)
        if not mx.numEq(L, zero):
            column = numv_product(inv(L), column)
            len2 = inner_product(column, column)
            #if not mx.numEq(len2, zero):
            scale = inv(sqrt(len2))
            column = numv_product(scale, column)
            if not mx.numEq(inner_product(column, column), one):
                print(inner_product(column, column))
                print(column)
                print(one)
            assert mx.numEq(inner_product(column, column), one)
        ls.append(column)
    return Matrix(ls).transpose()

def test_LUdecomposition():
    print(Matrix([]))
    mx = Matrix([[1, 1], [0, 1]])
    print(mx)
    eval(str(mx))

    v, L, U = LUdecomposition(mx)
    print(v, L, U, L*U)
def _test_RICdecomposition(mx):
    rank, (R,C), mxRs, mxI, mxCs, nullspace = RICdecomposition(mx)
    if rank < C:
        zeros = Matrix.zeros((R, nullspace.column_size()))
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
        rt = inverseRCTransform(rt)
        transformRow(rt, mxI)
    for ct in reversed(mxCs):
        ct = inverseRCTransform(ct)
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


def _test_orthogonalization(mx):
    orth = orthogonalization(mx)
    orthT = orth.transpose()
    I = orthT*orth
    
    one = mx.getArgs().one
    zero = mx.getArgs().zero

    for K in [I]:
        R, C = K.size()
        for r in range(R):
            for c in range(C):
                e = K[r][c]
                if r != c:
                    assert mx.numEq(e, zero)
                elif mx.numEq(e, one):
                    pass
                else:
                    if not mx.numEq(e, zero):
                        print(e)
                        print(K)
                        print(orth)
                    assert mx.numEq(e, zero)

    
    
def test_orthogonalization():
    import random
    mx = Matrix([[1, 1], [0, 1]])
    _test_orthogonalization(mx)
    for R in range(20):
        for C in range(max(0, R-1), R+2):
            array = list(100000 * random.random() for _ in range(R*C))
            mx = Matrix(array, (R,C))
            
            _test_orthogonalization(mx)
test_orthogonalization()
        
        
