
'''
PnP
given n point P[i] for i=1..n
unkown point P[0] = (x,y,z)
given angle(P[i], P[0], P[j]) for 1<=i<j<=n
calc P[0]

cos PiP0Pj = (Pi-P0)*(Pj-P0)/|Pi-P0|/|Pj-P0|


P3P
'''


from sympy import *


def dot_mul(u,v):
    return sum(a*b for a,b in zip(u,v))

def LEN__2(u):
    return dot_mul(u,u)

def distance__2(P1, P2):
    return LEN__2(vsub(P2, P1))

def fraction_pair_of_square_cos_angle(u,v):
    n = dot_mul(u,v)
    n = n**2
    d = LEN__2(u)*LEN__2(v)
    return n, d

def vsub(u,v):
    return [a-b for a,b in zip(u,v)]



def try1():

    n = 3
    L = n+1
    Xs = symbols('x:z')
    Is = list(range(L))
    Pxi = [symbols('P{x}:{L}'.format(x=x, L=L)) for x in Xs]
    P = [[Px[i] for Px in Pxi] for i in Is]
    angles = PiP0Pj = {(i,j): symbols('P{i}P0P{j}'.format(i=i, j=j)) for j in range(2,L) for i in range(1, j)}

    Q3x, Q3y = symbols('Q3x Q3y')
    Q = list(P)
    Q[1] = [0]*3
    Q[2] = [1, 0, 0]
    Q[3] = [Q3x, Q3y, 0]
    old_P, P = P, Q


    polys = []
    for (i,j), angle in angles.items():
        numerator, denominator = fraction_pair_of_square_cos_angle(vsub(P[i],P[0]), vsub(P[j],P[0]))
        p = cos(angle)**2 * denominator - numerator
        polys.append(p)


    print('solve_poly_system', polys, P)
    ans = solve_poly_system(polys, *P[0])
    print(ans)
    ''' run too long to wait it ends.'''


def try2():
    var('L1:4') # unknown
    LS = [L1,L2,L3]
    
    var('x2,y2')
    var('x3, y3, z3')
    var('P1P2__2, P2P3__2, P1P3__2')
    P = [[0]*3, [L1, 0, 0], [L2*x2, L2*y2, 0], [L3*x3, L3*y3, L3*z3]]
    
    # to find L[i]

    sPS = ['distance__2(P[{i}],P[{j}]) - P{i}P{j}__2'.format(i=i,j=j)
          for j in range(2,4) for i in range(1,j)]

    PS = []
    for s in sPS:
        PS.append(eval(s))
        
    print('solve_poly_system', PS, LS)
    ans = solve_poly_system(PS, *LS)
    print(ans)
    


init_printing(use_unicode=True, use_latex=True)
try2()
    

    
    




















