
# calc counterclockwise_rotation_matrix(u, alpha)

from nn_ns.sympy_util.bug_fix__rational_hash import *
from nn_ns.sympy_util.geometry import *
from sympy import *
from sympy import var, solve, Abs

'''
-------------------------------------
...
def X : len(X)==1; X _L Z
    X_x*u_x + X_y*u_y + X_z*u_z == 0
    X_x*X_x + X_y*X_y + X_z*X_z == 1
A = sqrt(-X_z**2 - u_z**2 + 1) ==>> abs(X_z) <= sqrt(1-u_z**2)
    let X_z = 0
B = (-u_z**2 + 1)
C = X_z*u_z
let X_xy = (X_x, X_y)'
T = [-C, A; -A, -C]/B; X_xy == T*u_xy or T'*u_xy


[len(u) == 1]:
    m_sin = Matrix([
            [0,    -u_z,  u_y],
            [ u_z,    0, -u_x],
            [-u_y,  u_x,    0]])

    m_cos = Matrix([
            [-u_x**2 + 1,    -u_x*u_y,        -u_x*u_z],
            [   -u_x*u_y, -u_y**2 + 1,        -u_y*u_z],
            [   -u_x*u_z,    -u_y*u_z,    -u_z**2 + 1]])

    m_const = Matrix([
            [ u_x**2, u_x*u_y, u_x*u_z],
            [u_x*u_y,  u_y**2, u_y*u_z],
            [u_x*u_z, u_y*u_z, u_z**2]])


    m_const = u*u'
    m_cos = E3 - m_const
    m_sin = 
    Mx = m_sin*sin + m_cos*cos + m_const
        = m_sin*sin + E3*cos + m_const*(1-cos)
'''
calc = 0

def mx_filter(mx, f, *args, **kwargs):
    #mx = mx.tolist()
    mx2 = Matrix(mx)
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



t=lambda m:m.transpose()
L = lambda x: len(str(x))


if calc:
    # find X_xy
    var('X_x u_x X_y u_y X_z u_z', real=True)
    r = solve([X_x*u_x + X_y*u_y + X_z*u_z,
               X_x*X_x + X_y*X_y + X_z*X_z-1,
               u_x*u_x + u_y*u_y + u_z*u_z-1], X_x, X_y)
    -(X_z*u_x*u_z - u_y*sqrt(-X_z**2 - u_z**2 + 1))/(-u_z**2 + 1)
    -(X_z*u_y*u_z + u_x*sqrt(-X_z**2 - u_z**2 + 1))/(-u_z**2 + 1)

    -(X_z*u_x*u_z + u_y*sqrt(-X_z**2 - u_z**2 + 1))/(-u_z**2 + 1)
    -(X_z*u_y*u_z - u_x*sqrt(-X_z**2 - u_z**2 + 1))/(-u_z**2 + 1)

    f1 = X_x*u_x + X_y*u_y + X_z*u_z
    f2 = X_x*X_x + X_y*X_y + X_z*X_z-1
    A = sqrt(-X_z**2 - u_z**2 + 1)
    B = (-u_z**2 + 1)
    C = X_z*u_z
    x1 = -(C*u_x - u_y*A)/B
    y1 = -(C*u_y + u_x*A)/B
    x2 = -(C*u_x + u_y*A)/B
    y2 = -(C*u_y - u_x*A)/B

    x1 = -C/B*u_x + u_y*A/B
    y1 = -C/B*u_y - u_x*A/B
    x2 = -C/B*u_x - u_y*A/B
    y2 = -C/B*u_y + u_x*A/B

    x1 = -C/B*u_x + A/B*u_y
    y1 = -A/B*u_x - C/B*u_y
    x2 = -C/B*u_x - A/B*u_y
    y2 = +A/B*u_x - C/B*u_y

    # T = [-C, A; -A, -C]/B; X_xy = T*u_xy or T'*u_xy

    xys = [(x1,y1), (x2,y2)]
    for x,y in xys:
        for f in [f1, f2]:
            f = f.subs({X_x:x, X_y:y}).subs(u_z**2, 1-u_x**2 - u_y**2)
            #print(f)
            f = factor(f).subs(u_z**2, 1-u_x**2 - u_y**2)
            f = factor(f)
            assert f == 0



    ##print(r)
    ##for x,y in r:
    ##    g = factor(expand(x**2+y**2))
    ##    print()
    ##    for v in (x,y):
    ##        h = v.subs(u_z**2, 1-u_x**2 - u_y**2)
    ##        h = factor(h)
    ##        h = h.subs(Abs(u_x), u_x)
    ##        h = factor(h).subs(u_x**2 + u_y**2, 1-u_z**2)
    ##        print(h)



if calc:
    # find counterclockwise_rotation_matrix
    x_z = 0
    x_x = x1.subs({X_z:x_z, u_z**2:1-u_x**2 - u_y**2})
    x_y = y1.subs({X_z:x_z, u_z**2:1-u_x**2 - u_y**2})
    assert x_x.free_symbols == {u_x, u_y}
    Z = Matrix([u_x, u_y, u_z])
    X = Matrix([x_x, x_y, x_z])
    Y = cross_product(Z, X)
    var('a')
    cos_ = cos(a)
    sin_ = sin(a)
    to_mx = lambda vecs: Matrix(list(map(list, vecs))).transpose()
    try:
        M1 = to_mx([(X* cos_ + Y* sin_), (-X* sin_ + Y* cos_), Z])
        M2 = to_mx([X, Y, Z])
    except:pass






    M1 = to_mx([(X* cos_ + Y* sin_), (-X* sin_ + Y* cos_), Z])
    M2 = to_mx([X, Y, Z])



    print('inv...')
    m2inv = M2.inv()
    print(L(m2inv))
    m = mxsimp(M1*m2inv)
    print(L(m))
    m = mxsubs(m, {u_z**2:1-u_x**2 - u_y**2})
    print(L(m))
    m = mxsimp(m)
    print(L(m))
    m = mx_filter(m, lambda g: collect(g, [cos(a), sin(a)]))
    m = mx_filter(m, lambda g: collect(expand(g), [cos(a), sin(a)]))
    mt = mx_filter(m, lambda g: Poly(g, cos(a), sin(a)).as_dict())
    def get_coeff(poly_as_dict, exp_tuple):
        try:
            assert set(poly_as_dict) <= {(0,1), (0,0), (1,0)}
        except:
            print(set(poly_as_dict))
            raise
        return poly_as_dict.get(exp_tuple, 0)
        

    m_cos = mx_filter(mt, lambda d: get_coeff(d, (1,0)))
    m_sin = mx_filter(mt, lambda d: get_coeff(d, (0,1)))
    m_const = mx_filter(mt, lambda d: get_coeff(d, (0,0)))
    zero_mx = m_cos*cos_ + m_sin*sin_ + m_const - m
    zero_mx = mx_filter(zero_mx, expand)
    zero_mx = mx_filter(zero_mx, factor)
    assert zeros(3) == zero_mx
    m_sin = mx_filter(m_sin, factor)
    m_sin = mxsubs(m_sin, {u_z**2:1-u_x**2 - u_y**2})
    m_sin = mx_filter(m_sin, factor)

    _m_sin = Matrix([
        [0,    -u_z,  u_y],
        [ u_z,    0, -u_x],
        [-u_y,  u_x,    0]])

    m_cos = mx_filter(m_cos, factor)
    m_cos = mxsubs(m_cos, {u_z**2:1-u_x**2 - u_y**2})
    m_cos = mx_filter(m_cos, expand)
    m_cos = mxsubs(m_cos, {u_x**2 + u_y**2: 1-u_z**2})

    _m_cos = Matrix([
        [-u_x**2 + 1,    -u_x*u_y,        -u_x*u_z],
        [   -u_x*u_y, -u_y**2 + 1,        -u_y*u_z],
        [   -u_x*u_z,    -u_y*u_z,    -u_z**2 + 1]])

    m_const = mxsubs(m_const, {u_x**2 + u_y**2: 1-u_z**2})
    _m_const = Matrix([
        [ u_x**2, u_x*u_y, u_x*u_z],
        [u_x*u_y,  u_y**2, u_y*u_z],
        [u_x*u_z, u_y*u_z, u_z**2]])


    assert m_sin == _m_sin
    assert m_cos == _m_cos
    assert m_const == _m_const


x=Matrix(var('X_x X_y X_z'))
z=Matrix(var('Z_x Z_y Z_z'))
y=cross_product(z, x)
yx_xy = mxsimp(y*t(x)-t(y*t(x))) # Y*X'-X*Y' = Ksin




