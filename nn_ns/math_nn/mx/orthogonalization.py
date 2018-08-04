

from .Matrix import Matrix

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





if __name__ == '__main__':
    test_orthogonalization()





        
