import math

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
    def identity(N, one=1, zero=0):
        v = [one]*N
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
        return Matrix(mx=self.getMx(), mxargs=self.args)
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
        self.new2old[a], self.new2old[b], = self.new2old[b], self.new2old[a],
















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





        
