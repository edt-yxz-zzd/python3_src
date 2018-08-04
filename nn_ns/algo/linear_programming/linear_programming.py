import numpy as np
import scipy
from scipy.optimize import nnls


A = [
    [1,1,1,0,],
    [0,1,1,1,],
    [0,0,1,1,],
    ]
A = np.matrix(A)
M, N = A.shape
c_array = np.ones((N, 1))
c = np.matrix(c_array)
ct_array = c_array.transpose()

b = [
    [10,],
    [21,],
    [12,],
    ]
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
print(r)
x = r.x
x_mx = np.matrix(x).transpose()
min_xsize = A * x_mx
dcon = min_xsize - b
minSize = objectfun(x)
print(x_mx)
print(min_xsize)
print(dcon)
print(minSize)

