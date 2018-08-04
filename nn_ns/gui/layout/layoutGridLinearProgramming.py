
import numpy as np
import scipy
import scipy.optimize

def layoutGridLinearProgramming(A, b):
    A = np.matrix(A)
    M, N = A.shape
    c_array = np.ones((N, 1))
    c = np.matrix(c_array)
    ct_array = c_array.transpose()

    b = np.matrix(b)
    x0 = np.ones((N,)) * b.sum()
    
    
    def objectfun(x):
        r = np.dot(ct_array, x)
        r = r[0]
        return r
    bounds = [(0, None)] * N
    constraints = []
    def plainconstraintfun(x, i):
        r = x[i]
        return x[i]
    def constraintfun(x, A_i, b_i):
        r = np.dot(A_i, x) - b_i
        return r[0]

    for i in range(N):
        constraint = {'type':'ineq', 'fun':plainconstraintfun, 'args':(i,)}
        constraints.append(constraint)
        
    for A_i, b_i in zip(A, b):
        constraint = {'type':'ineq', 'fun':constraintfun, 'args':(A_i, b_i)}
        constraints.append(constraint)
        
    r = scipy.optimize.minimize(objectfun, x0, args=(), method='COBYLA', bounds=None, constraints=constraints)
    x = r.x
    minSize = objectfun(x)


    
    # x to integers
    ix = [0]*N
    ls = [[] for _ in range(N)]
    for i, e in enumerate(ls):
        for j in range(M):
            a = A[(j,i)]
            #print(type(a), a)
            if a == 0: continue
            assert a == 1
            e.append(j)
    d = {}
    for i, e in enumerate(ls):
        e = tuple(e)
        if e not in d:
            d[e] = []
        d[e].append(i)


    loc2indice = [None]*N
    for indice in d.values():
        for i in indice:
            assert None == loc2indice[i]
            loc2indice[i] = indice
    assert all(type(indice) == list for indice in loc2indice)

    err = 0
    for loc in range(len(loc2indice)):
        indice = loc2indice[loc]
        if indice == None:
            continue
        for i in indice:
            loc2indice[i] = None
        
        s = sum((x[i] for i in indice), err) # pass err to exactly next block indice
        si = round(s)
        err = (s - si)
        
        i = indice[0]
        ix[i] = si # let other idx in indice to be 0

    tol = 0.01
    if not err < tol:
        print('error ', err)
        print('x ', x)
    assert err < tol
        
    # ix is a integral solve
    ix_mx = np.matrix(ix).transpose()
    assert round(minSize) == objectfun(ix_mx)
    dc = A * ix_mx - b
    assert all(e[0] >= 0 for e in dc)
    return ix

def test():
    A = [
        [1,1,1,0,],
        [0,1,1,1,],
        [0,0,1,1,],
        ]
    b = [
        [10,],
        [21,],
        [32,],
        ]

    x = layoutGridLinearProgramming(A, b)
    return

if __name__ == '__main__':
    test()









