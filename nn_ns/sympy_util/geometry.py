
from sympy import sqrt, cos, tan, pi, acos, sin, Matrix, eye, zeros
from .my_sympify import my_sympify
from .constant import one, zero
from .matrix_filter import mx_filter as matrix_filter

'''
sympy bugs from from nn_ns.sympy_util.geometry.py
bug1 from vec_sub:
    sympy bug: Tuple.__new__ not like tuple's!!!
    so type(Tuple_obj)(x for x in ls) fail


'''

def angle_of_regular_polygon(n):
    return pi - 2*pi/n
def outer_radius_of_regular_polygon(n, L):
    angle = angle_of_regular_polygon(n)
    Rc = L/cos(angle/2)/2
    return Rc
def inner_radius_of_regular_polygon(n, L):
    angle = angle_of_regular_polygon(n)
    rc = L*tan(one*angle/2)/2 # if int L
    return rc

    

def opposite_tri_edge(a, gamma, b):
    return sqrt(a*a + b*b - 2*cos(gamma)*a*b)
def opposite_tri_angle(a,  c,  b):
    # return gamma # the opposite angle of c
    sub = (a*a + b*b) - c*c # == 2*cos(gamma)*a*b
    gamma = acos(one*sub/(2*a*b))
    return gamma

def tri_area(a,b,  c):
    '''triangle (a,b,c)'''
    return sqrt((2*a*b)**2-(a*a+b*b-c*c)**2)/4

def half_arcsin(x):
    '''return y, s.t. arcsin y = arcsin(x) / 2 where 0<=x<=pi/2'''

    return my_sympify(sqrt(1-sqrt(1-x**2))/sqrt(2))


def add_arcsin(u,v):
    '''return y, s.t. arcsin y = arcsin(u)+arcsin(v) where 0<=min(u,v)<=u+v<=pi/2'''

    return my_sympify(u* sqrt(1-v*v) + sqrt(1-u*u) *v)

def add_arcsin_with_coeffs(Ku, Kv, u, v):
    '''return y, s.t. arcsin y = ku*arcsin(u)+kv*arcsin(v)<=1
where 0<=min(u,v), kx=Kx[0]/2**Kx[1], Kx=(_ku, _ke)'''

    ku,eu = Ku
    kv,ev = Kv
    for _ in range(eu): u = half_arcsin(u)
    for _ in range(ev): v = half_arcsin(v)

    y = 0
    for _ in range(ku): y = add_arcsin(u,y)
    for _ in range(kv): y = add_arcsin(v,y)
    return my_sympify(y)
    '''ASRP solid
[3,4,4,4]: pi/2 == 3/2*asin(sqrt(2)/X) + asin(1/X)/2
    y = add_arcsin_with_coeffs((3,1), (1,1), sqrt(2)/X, 1/X)
    pi/2 == asin(y) ==>> y == 1
[3,4,5,4]: pi/2 == asin(sqrt(2)/X) + asin(2*sin(3*pi/10)/X)/2 + asin(1/X)/2
    y = add_arcsin_with_coeffs((1,1), (1,1), 2*sin(3*pi/10)/X, 1/X)
    y = add_arcsin(sqrt(2)/X,y)
    pi/2 == asin(y) ==>> y == 1
'''


def distance2(u, v):
    return vec_len2(vec_sub(u,v))

def distance(u, v):
    return vec_len(vec_sub(u,v))


def vec_sub(u, v):
    try:
        return type(u)(x-a for x, a in zip(u,v))
    except:
        # WTF init: <class 'sympy.core.containers.Tuple'>
        # by Tuple(1,2,3) instead of Tuple([1,2,3])
        print(vec_sub, u, v)
        print(type(u), type(v))
        raise
def vec_add(u, v):
    return type(u)(x+a for x, a in zip(u,v))

def vec_scale(x, u):
    return type(u)(x*a for a in u)
def vec_unit(u):
    return vec_scale(one/vec_len(u), u)
def vec_len2(u):
    return dot_product(u,u)
def vec_len(u):
    return sqrt(vec_len2(u))

def angle_of_2_vectors(u,v):
    '''0 <= result <= pi'''
    return acos(dot_product(u, v)/sqrt(vec_len2(u)*vec_len2(v)))

def dot_product(u, v):
    '''dot_product(u, v) = len(u)len(v)cos(angle(u,v))
    = scalar_product(u, v)'''
    return sum(x*y for x,y in zip(u,v))
    
def cross_product(u, v):
    '''cross_product(u, v) = vector_product(u, v)
cross_product(u, v) = -cross_product(v, u)

cross_product(Ex, Ey) = Ez; counterclockwise

look at the plane of Ex and Ey from endpoint of Ez,
then the shortest rotation of Ex in the direction of Ex
is counterclockwise.
@Handbook.of.Mathematics::2. Vector Product::page183

len(Ez) = len(Ex)len(Ey)abs(sin(angle(Ex,Ey)))

Ex = (1,0,0)'; ...
mx(u,v) = [Ex, Ey, Ez; u'; v']
    = [Ex, Ey, Ez; u_x, u_y, u_z; v_x, v_y, v_z]
cross_product(u, v) = determinant(mx(u,v)) (page185::(3.264))

'''
    a, b, c = u
    x, y, z = v
    return type(u)([b*z-c*y, c*x-a*z, a*y-b*x])
    pass

def double_cross_product(u,v,w):
    '''double_cross_product = double_vector_product
double_cross_product(u,v,w) = cross_product(u,cross_product(v,w))
= cross_product(cross_product(w, v), u)
result in plane(w, v)

let uv = dot_product(u,v); uw = dot_product(u,w)
double_cross_product(u,v,w) = uw*v - uv*w
'''
    uv = dot_product(u,v); uw = dot_product(u,w)
    return vec_scale(uw, v) - vec_scale(uv, w)
    return cross_product(u,cross_product(v,w))

def mixed_product(u,v,w):
    '''triple_product(u,v,w) = mixed_product(u,v,w)'''
    return triple_product(u,v,w)
def triple_product(u,v,w):
    '''triple_product(u,v,w) = mixed_product(u,v,w)
    = triple_product(v,w,u)
    = dot_product(cross_product(u, v), w)
    = -triple_product(u,w,v)

triple_product(Ex, Ey, Ez) = volume if Ex, Ey, Ez form a right hand system.

mx(u,v,w) = [u'; v'; w']; u'=(u_x, u_y, u_z);...
mixed_product(u,v,w) = determinant(mx(u,v, w))
'''
    return dot_product(cross_product(u, v), w)



def project_to(u, v):
    '''project_to(u, v) = w = project_to(w, v)
    = project_to(u, vec_scale(x, u)) where x != 0
    ==>> dot_product(u,v) = dot_product(w,v)'''
    return vec_scale(one*dot_product(u,v)/vec_len2(v), v)
def vec_height(u, v):
    'vec_height(u, v) = u - project_to(u, v),  result _L v'
    return vec_sub(u, project_to(u, v))


def counterclockwise_rotation_matrix(u, alpha):
    '''return a 3-by-3 matrix

i.e. counterclockwise_rotation_matrix(Ez, pi/2)*Ex = Ey

let Mx = rotate_counterclockwise_matrix(u, alpha) 
let Z = vec_unit(u)
def X : len(X)==1; X _L Z
    X_x*u_x + X_y*u_y + X_z*u_z == 0
    X_x*X_x + X_y*X_y + X_z*X_z == 1
let Y = cross_product(Z, X)
let cos = cos(alpha), sin = sin(alpha)
Mx*X = X cos + Y sin
Mx*Y = -X sin + Y cos
Mx*Z = Z
Mx * (x*X+y*Y+z*Z) = ((x cos + -y sin)*X + (x sin + y cos)*Y + z*Z)
    = x(X cos + Y sin) + y(-X sin + Y cos) + z*Z
    = [(X cos + Y sin), (-X sin + Y cos), Z]*(x,y,z)'
(x*X+y*Y+z*Z) = [X, Y, Z]*(x,y,z)'
Mx * [X, Y, Z]*(x,y,z)' = [(X cos + Y sin), (-X sin + Y cos), Z]*(x,y,z)'
let XYZ = [X, Y, Z] ==>> XYZ^-1 = XYZ'
==>> Mx = [(X cos + Y sin), (-X sin + Y cos), Z] * XYZ^-1
        = ([X, Y, 0]cos + [Y,-X,0]sin + [0,0,Z]) * XYZ'
        = ([X, Y, Z]cos + [Y,-X,0]sin + [0,0,Z](1-cos)) * XYZ'
        = E3*cos + [Y,-X,0]XYZ' sin + [0,0,Z]*XYZ'(1-cos) 
        = (Y*X'-X*Y') sin + Z*Z'(1-cos) + E3*cos 
        = (Y*X'-(Y*X')') sin + Z*Z'(1-cos) + E3*cos
        
Ksin = Y*X'-(Y*X')' = 
    [                                                   0, -X_x**2*Z_z + X_x*X_z*Z_x - X_y**2*Z_z + X_y*X_z*Z_y, X_x**2*Z_y - X_x*X_y*Z_x - X_y*X_z*Z_z + X_z**2*Z_y]
    [ X_x**2*Z_z - X_x*X_z*Z_x + X_y**2*Z_z - X_y*X_z*Z_y,                                                    0, X_x*X_y*Z_y + X_x*X_z*Z_z - X_y**2*Z_x - X_z**2*Z_x]
    [-X_x**2*Z_y + X_x*X_y*Z_x + X_y*X_z*Z_z - X_z**2*Z_y, -X_x*X_y*Z_y - X_x*X_z*Z_z + X_y**2*Z_x + X_z**2*Z_x,                                                   0]
Ksin[1,0] = X_x**2*Z_z - X_x*X_z*Z_x + X_y**2*Z_z - X_y*X_z*Z_y
    # X_x*Z_x + X_y*Z_y + X_z*Z_z == 0
    # X_x*X_x + X_y*X_y + X_z*X_z == 1
    = (X_x**2 + X_y**2)*Z_z - (X_y*Z_y + X_x*Z_x)*X_z
    = (1-X_z**2)*Z_z + X_z*Z_z*X_z
    = Z_z

==>> Ksin=[
            [   0, -Z_z,  Z_y],
            [ Z_z,    0, -Z_x],
            [-Z_y,  Z_x,    0]]

Mx = Ksin sin + Z*Z'(1-cos) + E3*cos
-------------------------------------
[u = Ez]:
    X = Ex; Y = Ey; XYZ == E3 == XYZ'
    Ksin = [Y,-X,0]; yeah

'''
    Z = vec_unit(u)
    sin_, cos_ = sin(alpha), cos(alpha)
    Ks = Ksin, K1_cos, E3 = __counterclockwise_rotation_matrix__Ks(Z)
    As = sin_, (1-cos_), cos_
##    for k in Ks:print(type(k))
##    for a in As:print(type(a))
##    for k, a in zip(Ks, As):
##        print(type(k), type(a))
##        print(type(a*k))
    mx = sum((a*k for k, a in zip(Ks, As)), zeros(3))
    return matrix_filter(mx, my_sympify)


def __counterclockwise_rotation_matrix__Ks(Z):
    # len2(Z) == 1
    Z = Z_x, Z_y, Z_z = Z
    Z = Matrix(Z)
    Ksin = Matrix([
            [   0, -Z_z,  Z_y],
            [ Z_z,    0, -Z_x],
            [-Z_y,  Z_x,    0]])

    K1_cos = Z*Z.transpose()
    E3 = eye(3)
    return Ksin, K1_cos, E3
    

def rotate_to(u, v, alpha):
    '''rotate u to v by angle alpha

== counterclockwise_rotation_matrix(cross_product(u, v), alpha)*u
--------------------
rotate_to(u, v, 0) = u
rotate_to(u, v, alpha+pi) = -rotate_to(u, v, alpha)
rotate_to(u, v, pi/2) = \
             vec_unit(cross_product(cross_product(u, v), u))*len(u)
rotate_to(u, v, angle(u,v)) = v/len(v)*len(u) = vec_unit(v)*len(u)

let X = u
let Z = cross_product(X, v)
let Y = cross_product(Z, X) = cross_product(cross_product(X, v), X)
    = cross_product(X, cross_product(v, X))
    = double_cross_product(X,v,X)
    = vec_scale(len2(X), v) - vec_scale(dot_product(X,v), X)
let Ex = vec_unit(X)
let Ey = vec_unit(Y)
Y/len2(X) = v - vec_scale(dot_product(X,v)/len2(X), X)
    = v - project_to(v, X)
    = vec_height(v, X)
len2(Y/len2(X)) = len2(v) - len2(project_to(v, X))
Ey = vec_unit(Y/len2(X)) = vec_height(v, X)/len(Y/len2(X))

vec_unit(result) = Ex*cos(alpha) + Ey*sin(alpha)
result = len(u)*(Ex*cos(alpha) + Ey*sin(alpha))
    = u*cos(alpha) + len(u)*Ey*sin(alpha))

'''
    u = Matrix(u)
    return counterclockwise_rotation_matrix(cross_product(u, v), alpha)*u


def rotate_clockwise(O, A, B, gamma):
    '''rotate space about OA in clockwise with angle gamma, return new B'.
clockwise view from A to O.

def O' = O' on OA; O'B _L OA.
let C = rotate_clockwise(O, A, B, pi/2)
vec_unit(O'C) = cross_product(vec_unit(O'B), vec_unit(OA))
O'C = cross_product(O'B, vec_unit(OA))
    = cross_product(O'B, OA)/len(OA)
    
'''

    OB = vec_sub(B, O)
    OA = vec_sub(A, O)
    OB_ = counterclockwise_rotation_matrix(OA, -gamma)*Matrix(OB)
    B_ = vec_add(O, OB_)
    return type(B)(B_)















