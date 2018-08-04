

'''
brute-force
find planar grid drawing with integer length
fail, search space too huge

'''
import math
#import sympy
from math_nn.prime1 import factor_power_pairs_of_positive_integer
from math_nn.sum_of_two_squares import to_sum_of_two_squares
#sympy.core.numbers.Integer
#sympy.Integer
#sympy.Integer().factorial

import sympy.combinatorics.polyhedron as polyhedron
import sympy.polys as polys
from sympy.combinatorics.polyhedron import tetrahedron as T, \
     cube, dodecahedron, icosahedron, tetrahedron

#, tetrahedral, octahedral, icosahedral
('cube', 'cube_faces', 'dodecahedron', 'dodecahedron_faces',
 'flatten', 'icosahedron', 'icosahedron_faces', 'minlex',
 'octahedron', 'octahedron_faces', 'rmul', 'tetrahedron',
 'tetrahedron_faces')

##b = dir(polyhedron)
##print(b)
for name in ['cube', 'dodecahedron', 'icosahedron', 'tetrahedron']:
    obj = globals()[name]
    print(name)
    print(obj.edges)
    print(obj.faces)
    

for n in range(1000):
    factor_powers = factor_power_pairs_of_positive_integer(n)
    #print(to_sum_of_two_squares(n, factor_powers))


def is_square(x):
    r = int(math.sqrt(x))
    r2 = r*r
    if r2 == x:
        return True
    if r2 < x:
        rpp2 = r2+2*r+1
        assert rpp2 >= x
        return r2+2*r+1 == x
    rmm2 = r2-2*r+1
    assert rmm2 <= x
    return rmm2 == x

def is_good(x,y):
    return is_square(x*x+y*y)
def good_to_vs(x,y, vs):
    return all(is_good(x-u, y-v) for u,v in vs)

def int_distance(xy, uv):
    (x,y), (u,v) = xy, uv
    x,y = (x-u), (y-v)
    x = x*x + y*y
    return round(math.sqrt(x))
def find_K4():
    # find K4, with all edges of integer length and on grid
    # let a,b,c be outer face
    # let ab >= ac/bc
    # let a at (0,0), b at (n,0)
    # let c = (x,y), then 0 <= x <= n/2, 1 < y, (x-n)**2+y*y <= n*n
    # y*y <= 2nx-xx
    # d in Tri-abc, let d = (s,t), 1<=t<y, x/y*t<s<n-(n-x)/y*t
    a = (0, 0)

    good_cs = []
    good_cd_ls = []
    for n in range(1, 200):
        for x in range((n+1)//2+1):
            max_y = int(math.sqrt((2*n-x)*x))
            for y in range(2, max_y+1):
                if is_good(x,y) and is_good(x-n, y):
                    #print(x,y)
                    good_c = (x,y,n)
                    good_cs.append(good_c)
                    k1 = x/y
                    k2 = (n-x)/y
                    vs = [(0,0), (n,0), (x,y)]
                    for t in range(1,y):
                        s_beg = int(k1*t+1)
                        s_end = n-int(k2*t)
                        for s in range(s_beg, s_end):
                            if good_to_vs(s,t, vs):
                                #print(good_c, (s,t))
                                good_cd_ls.append((good_c, (s,t)))


    def calc_lens(n, x,y, s,t):
        a,b,c,d = [(0,0), (n,0), (x,y), (s,t)]
        ls = [(a,b), (a,c), (b,c), (d,a), (d,b), (d,c)]
        return [int_distance(u,v) for u,v in ls]

    minmax_radio_ls = []
    for (x,y,n), (s,t) in good_cd_ls:
        lens = calc_lens(n, x,y, s,t)
        #print('ab={}, ac={}, bc={}, da={}, db={}, dc={}'.format(*lens))
        minmax_radio_ls.append(min(lens)/max(lens))
    m = max(minmax_radio_ls)
    i = minmax_radio_ls.index(m)
    (x,y,n), (s,t) = good_cd_ls[i]
    print(calc_lens(n, x,y, s,t))
    print(n, (x,y), (s,t))


def find_K4():
    # if da == db == dc
    # let d == (0,0)
    # a == (n,0)

    N = 200
    factor_exp_ls = []
    for n in range(1,N):
        pairs = to_sum_of_two_squares(n, factor_exp_ls)
        ls = []
        for x,y in pairs:
            assert 0 <= x <= y
            if x == 0:
                ls.append((x,y))
            elif x == y:
                ls.append((x,y))
                ls.append((x,y))
            else:
                raise #ls.
                
            











