
from sympy import factor, Matrix

def mx_filter(mx, f, *args, **kwargs):
    #mx = mx.tolist()
    mx2 = type(mx)(mx)
    nrow, ncol = mx.shape
    for r in range(nrow):
        for c in range(ncol):
            e = mx[r,c]
            e = f(e, *args, **kwargs)
            mx2[r,c] = e
    return mx2

def mxsubs(mx, *args, **kwargs):
    subs = lambda f: f.subs(*args, **kwargs)
    return mx_filter(mx, subs)
def mxsimp(mx, simp = factor):
    #mx = mx.tolist()
    return mx_filter(mx, simp)



t = lambda m:m.transpose()
L = lambda x: len(str(x))


