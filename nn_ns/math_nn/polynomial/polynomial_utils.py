

'''
coefficient = ??
polynomial = [coefficient]  # little-endian # tuple
    polynomial = sum coefficients[i]*x**i {i}

'''

'''
TODO:
    # univariate polynomial with integer/float/fraction coefficients
    floor_polynomial_roots
    to_primitive_polynomial
    to_primitive_polynomial_with_headsign
    polynomial_divmod
    polynomial_perfect_div
    polynomial_mul
    polynomial_gcd
    remove_multiple_roots
    square_free_factor?
    factor_to_primitive_polynomials? factoring over finite fields?
    polynomial_differential
    num_real_roots_of_square_free_polynomial_in_range
    
    polynomial_eval
    polynomial2Sturm_sign_polys
    Sturm_sign_polys_eval
    is_polynomial_constant
    factor_into_power_pieces
    constant_polynomial
    polynomial_shift
    polynomial_copy
    polynomial_eq

DONE:
    range_contained_all_real_roots
'''

'''
real roots of polynomial
1) factor into square-free parts
2) find a large range which contains all real roots
3) using Sturm sequence to split this range to seperate roots
4) using binary search until there are enough space between the searching
   range and other ranges
5) using Newton's Method


1)
g = gcd(f(x), f'(x))
f1 = gcd(f/g, g)
let f be g loop.
finally
assert f == product(f[i]**i)
assert all(f[i] is square-free)

2)
let f[i] = sum(A[k]*x**k for k in range(K+1))
C = max(abs(A[j]/A[K]) for j in range(K))
if x > 1:
    f[i]/A[K] >= x**K - C*sum(x**j) = x**K - C(x**K-1)/(x-1) = right-hand-(a)
    if C <= x-1: right-hand-(a) > 0
    let root_upper_bound = C+1
let root_lower_bound = -C-1
root in open range (-C-1, C+1)

3)
Sturm + binary search??
I don't know how to speed up
should we solve f' first??


let h = f[j]
s0 = h, s1 = h'
s[i] = -(s[i-2]%s[i-1]) = s[i-1]*q[i-1] - s[i-2]
==>> if s[i-1] == 0, s[i] = -s[i-2]

h is square-free ==>> (s[0], s[1]) != (0, 0)
==>> if s[i-1] == 0, s[i] = -s[i-2] != 0
==>> when s[i-1] changes sign, sign(s[i-2]s[i-1]s[i]) == -1, keep the same
but when s[0] changes sign, that is:
    h is square-free ==>> if pass a root of h, s[0] changes sign
    if h = 0- -> 0+: h' > 0, h/h' be same sign now, sign_change_number -= 1
    else h = 0+ -> 0-: h' < 0, sign_change_number -= 1


for half open range (rend, rbegin], there are
    sign_change_number(rend) - sign_change_number(rbegin) roots.

so, total number of roots is:
    total = sign_change_number(-C-1) - sign_change_number(C+1)

assert total <= K
split out at most K subranges from (-C-1, C+1).
since we just want floor of roots, so the search tree height H < log2(C+1)+1
this tree with at most K desired leaves and some truncated leaves.
if C is large enough and roots are near,
max tree will has about K*H-K/2*log2(K) leaves.

may be we can use Newton's Method but increase the step.
if there are m near roots in range, let x1 = x0 - m*f/f'
if not good, decrease step length.


4)
x1 = x0 - f/f'
let |(x1-r)/(x0-r)| < 1/2 # necessary to make Newton search fast
lefthand = |1-f/f'/(x0-r)|
f = (x-r)II(x-not_r[i]) since square-free  # not_r means other roots
f' = (x-r)*(II...)' + II... = f*sum(1/(x-r[i]))
f/f'/(x0-r) = 1/((x0-r)*sum(...)) = 1/(1 + (x0-r)*sum(1/(x0-not_r[i])))

lefthand = |1-1/(1+()*sum..)| = |()*sum../(1+()*sum..)| < 1/2
==>> 1/lefthand = |1/()/sum.. + 1| > 2
1/()/sum.. > 1 or < -3
0 < ()*sum.. < 1 or -1/3 < ()*sum.. < 0
|()*sum..| < 1/3
|(x0-r)| = |()| < 1/3/sum..
let Dmin = min|x0-not_r[i]|
sum.. = sum(1/(x0-not_r[i])) <= sum(1/Dmin) = (k-1)/Dmin
let |(x0-r)| < min 1/3/sum.. = 1/3/max sum..
let |(x0-r)| < Dmin/3/(k-1)



WWWWWWWWWWWWW bug fixed GGGGGGGGGGGGGG
THERE ARE COMPLEX ROOTS!!!
xxxxxx wrong: assume r is the unique root in range (a, b) = (a, a+L)
assume r is the unique root in circle(o=(a+b)/2+0j, r=(b-a)/2), L = b-a
or stronger: assume r is the unique root in sqare(o=(a+b)/2+0j, L = b-a)
assume r is in (a+gap, b-gap) # real
now Dmin = min|x0-not_r[i]| >= gap
|(x0-r)| <= b-gap - a+gap = L - 2*gap = L'
if L - 2*gap < gap/3/(k-1):
then |(x0-r)| < Dmin/3/(k-1), using Newton's
==>> gap/L > 3(k-1)/(2*3(k-1) + 1)
==>> gap/L' = gap/(L-2*gap) > 3(k-1)
if we search a range of length L', and left/right gaps are both
more than 3(K-1)L', then we use Newton's Method

let E = 3(K-1)
assume L > 2E+1
we cut L into (2m+1) pieces (m>=1)
left_most and right_most pieces of length min_gap = E
the middle piece len(P[m]) * E <= len(P[:m]) == len(P[m+1:])
for the ith piece if 0 < i < m
    len(P[i]) * E <= len(P[:i]) == len(P[-i:])
so, if we find root in bracket i, then we can use Newton's Method
we can bisearch these m brackets, since m = O(log(L)), only loglogL steps!
NOTE: after finding out the bracket, we need to test the boundary
    since we use INTEGER boundary.
top_most_left_gap = len(P[:m]) = L*E/(2E+1) = min_gap*((1+E)/E)**(m-1)
((1+E)/E)**(m-1) = L*E/(2E+1)/min_gap = L/(2E+1)
m = 1+ ln(L/(2E+1)) / ln(1+1/E)
since E >= 3 (K>=2), let's find x**t to replace ln(1+x)
    if x**t <= ln(1+x) for x in (0, 1/3), then t >= lnln(1+1/3)/ln3
    1.2 > min_t, let t = 1.2
m <= 1+ ln(L/(2E+1)) / (1/E)**1.2 = 1+ ln(L/(2E+1)) *E**1.2
assume 1 << E << L
then m <= E**1.2 * ln(L), total search steps are no more than:
    log2(2m+1) <= 1 + 1.2log2(E) + log2(ln(L)) = O(logK + loglogL)
    logK for seperate the root far from others
    loglogL for bad initial bracket










should we use binary search when Newton's is slow?
def a(x[i]) = (x[i]-x[i+1])/(x[i]-r) = f/f'/(xi-r)
assume r < x[i+1] < x[i], ==>> a() < 1
since x[i] more and more close to r,
a(x[i]) should increase to 1 too.
if slow, then a(x[0]) < 1/2
(x1-x2)/(x0-x1) = a(x1)*(x1-r)/a(x0)*(x0-r)
    (x1-r) = (1-a(x0))*(x0-r)
(x1-x2)/(x0-x1) = (1-a(x0))*a(x1)/a(x0)
    since slow, let's assume a(x1)==(1+small)*a(x0)
(x1-x2)/(x0-x1) = (1-a(x0))*(1+small)
a(x0) = 1-(x1-x2)/(x0-x1)/(1+small)
r = x0 - (x0-x1)/a(x0) = x0 - ()/(1-(x1-x2)/(x0-x1)/(1+small))
= x0 - (x0-x1)**2*(1+small)/((x0-x1)*(1+small) - (x1-x2))
new_x1 = x0 - (x0-x1)**2/((x0-x1) - (x1-x2))


'''


def polynomial_copy(poly):
    assert type(poly) is tuple
    return poly


def polynomial_eq(lhs, rhs):
    if len(lhs) < len(rhs):
        return polynomial_eq(rhs, lhs)
    if any(lhs[len(rhs):]):
        return False

    return lhs[:len(rhs)] == rhs

def polynomial_shift(poly, n):
    # poly * x**n
    if n >= 0:
        return constant_polynomial(0)*n + poly
    if n < 0:
        f = poly[:n] # () is allowed
##        if not f:
##            constant_polynomial(0)
        return f

def constant_polynomial(x=None): # () is allowed
    if x == None:
        return ()
    return (x,)

def is_polynomial_constant(poly):
    return any(reversed(poly[1:]))

def is_polynomial_zero(poly):
    return not any(poly)



def floor_polynomial_roots(poly):
    fs = factor_into_power_pieces(poly)
    roots_ls = []
    for f in fs:
        roots = floor_square_free_polynomial_roots(f)
        roots_ls.append(roots)
    return roots_ls

def find_monotone_ranges_contain_contain_roots_of_square_free_polynomial(sqf_poly):
    '''return ranges, list of num_roots, and Sturm_sign_polys

range = [begin, end); where 'begin', 'end' are integers.
each range contains one root, or of length 1
in each range, df(x) keeps sign.
'''
    begin, end = range_contained_all_real_roots(sqf_poly)


def floor_square_free_polynomial_roots(sqf_poly):
    rngs, nroots_ls, Sturm_sign_polys = \
        find_ranges_contain_contain_roots_of_square_free_polynomial(sqf_poly)

    roots = []
    for (begin, end), nroots in zip(rngs, nroots_ls):
        assert nroots > 0
        if nroots > 1:
            roots += [begin]*nroots
            continue
        root = search_unique_root_in_range(sqf_poly, begin, end)
        roots.append(root)
    return roots
    
def search_unique_root_in_monotone_range(poly, begin, end):
    '''[begin, end) should contain exactly one root, df(x) should keep sign.

can't contain more than one root(multi-roots is not allowed)'''
    
def factor_into_power_pieces(poly):
    '''factor_into_power_pieces(f) -> [f1, f2...]
assert f1**1 * f2**2 * fi**i... == f
'''
    assert not is_polynomial_constant(poly)
    f1f2s, gcd = remove_multiple_roots(poly)
    fs = []
    fi_fi1s = f1f2s
    while not is_polynomial_constant(gcd):
        fi1s = polynomial_gcd(fi_fi1s, gcd)
        fi = polynomial_perfect_div(fi_fi1s, fi1s)
        fs.append(fi)
        fi1_fi2s = fi1s

        ### next round
        gcd = polynomial_perfect_div(gcd, fi1s)
        fi_fi1s = fi1_fi2s
    assert not is_polynomial_constant(fi_fi1s)
    fs.append(fi_fi1s)
    assert polynomial_eq(gcd, constant_polynomial(1))

    return fs
        
    
def remove_multiple_roots(poly):
    assert not is_polynomial_constant(poly)
    df = polynomial_differential(poly)
    gcd = polynomial_gcd(poly, df)
    if is_polynomial_constant(gcd):
        return polynomial_copy(poly), constant_polynomial(1)
    q = polynomial_perfect_div(poly, gcd)
    return q, gcd


def Sturm_sign_polys_eval(Sturm_sign_polys, x):
    '''Sturm sequence at x

x: -inf -> inf
when x pass a root, --count
split X axis into:  (-inf, min_root), [min_root, second_root), ...
sign changed count:    max_count    ,     max_count-1

'''
    def sign(y):
        if y == 0: return 0
        if y < 0:  return -1
        return 1

    seq = []
    for poly in polys:
        s = polynomial_eval(poly, x)
        if s:
            seq.append(sign(s))
    count = sum(x!=y for x,y in zip(seq, seq[1:]))
    return count

def num_real_roots_of_square_free_polynomial_in_range(sqf_poly, rrng):
    '''calc number of real roots of square_free_polynomial in rrng

rrng = rbegin, rend; # assert rbegin >= rend
stands for x in (begin, end] = (rend, rbegin]'''
    polys = polynomial2numroot_sign_polys(sqf_poly)
    rbegin, rend = rrng
    assert rbegin >= rend
    
    rng = begin, end = rend, rbegin
    assert begin <= end
    
    a, b = counts = [Sturm_sign_polys_eval(x) for x in rng]
    return a - b

def polynomial2Sturm_sign_polys(poly):
    poly = to_primitive_polynomial_with_headsign(poly)
    dpoly = polynomial_differential(poly)

    
    dd = poly
    d = dpoly
    polys = [dd]
    while not is_polynomial_constant(dd):
        d = to_primitive_polynomial_with_headsign(d)
        polys.append(d)

        q, remainder = polynomial_divmod(dd, d)
        dd, d = d, polynomial_mul(constant_polynomial(-1), remainder)
    return polys


def range_contained_all_real_roots(poly):
    U = zero_upper_bound_of_poly(poly)
    L = -U
    return (L, U)


def zero_upper_bound_of_poly(poly):
    '''f(x) = polynomial = sum x**d * cs[d] {d = 0..degree}
    cs = polynomial_coeffs
    degree = len(cs) - 1
    LC = cs[degree]
    assert degree >= 1
    assert LC != 0

    return upper, s.t. any x >= upper: f(x)/LC > 0

let M = max(map(abs, cs))
let H = height = M/abs(LC) >= 1
0 < f(x)/LC = x**degree + sum x**d * cs[d]/LC {d = 0..degree-1}
    <==> x**degree > -sum x**d * cs[d]/LC {d = 0..degree-1}
    right <= sum abs(x**d * cs[d]/LC) {d = 0..degree-1}
        <= sum abs(x**d * height) {d = 0..degree-1}
        == height * sum abs(x**d) {d = 0..degree-1}
    <<== x >= 1 and x**degree > height * sum x**d {d = 0..degree-1}
        == height * (x**degree-1)/(x-1)
        <==> x**(degree+1) > (height+1) * x**degree - height
    <<== x >= 1 and x**(degree+1) >= (height+1) * x**degree
        <==> x >= height+1 = M/abs(LC)+1
    <<== upper = M//abs(LC) + 2

'''
    
    cs = polynomial_coeffs = poly
    degree = len(cs) - 1
    LC = cs[degree]
    assert degree >= 1
    assert LC != 0

    M = max(map(abs, cs))
    upper = M//abs(LC) + 2
    assert upper >= 3
    return upper



