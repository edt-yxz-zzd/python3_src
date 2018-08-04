

'''
nth_pow_continued_fraction(x, n, L) = continued_fraction(x**(1/n))[:L]



x = [a0; a1, a2, ...]
x = [x.] + {.x} = floor(x) + 1/(1/(x-floor(x)))
x[0] = x; x[i] = 1/(x[i-1]-floor(x[i-1])) = 1/(x[i-1]-a[i-1]) for [NN i>0]
a[i] = floor(x[i])






'''

from sand import show_forgots_as_str, unzip
if show_forgots_as_str(__file__,
                       'error, logic, qt, z'.split(', ')):
    raise NameError()

from sympy import LC, N, Poly, Q, ceiling, count_roots, degree, floor, \
     fraction, intervals, oo, real_roots, refine_root, symbols, together, var,\
     radsimp, ratsimp, sympify, simplify, nsimplify
from nn_ns.math_nn import continued_fraction2numerator_denominator
import itertools


##
##from sympy import *
##from nn_ns.math_nn import *

'''
sympy bugs from nth_pow_continued_fraction.py
bug1 from continued_fraction_dc:
    cf, xs = nth_pow_continued_fraction(2,3,102)
    assert 0 in cf

    that is:
    one = sympify(1)
    N = (-18946643396438422418200496503661148314139229271682874349*2**(one/3)
         + 23871274840024462774930909433822752859720888716067576820
         )
    D = (-133450479581198331510402510274281177418327310779117149571
         + 105919715836427477757469402582631193698068222179903783354*2**(one/3)
         )
    # assert xs[100] == N/D
    assert floor(N/D) == 0
    assert N > D
    assert D > N
    assert N-D > 0
    assert not (D-N < 0)
    assert str((N-D).evalf(10)) == '1.690148127e-57'
'''

def continued_fraction_pack_to_ND_pairs(cf, ND_2=(0,1), ND_1=(1,0)):
    '''x = xs[0] = (0+1*xs[0])/(1+0*xs[0])
    = cf[0] + 1/xs[1] = (1+cf[0]*xs[1])/(0 + 1*xs[1])
    = (N[i-1]+N[i]*xs[i+1])/(D[i-1]+D[i]*xs[i+1])
    # xs[i] = cf[i] + 1/xs[i+1]
    = (N[i] + (N[i-1]+N[i]*cf[i+1])*xs[i+2])
    /(D[i] + (D[i-1]+D[i]*cf[i+1])*xs[i+2])
    ==>> N[-2] = 0, N[-1] = 1; D[-2] = 1, D[-1] = 0
    ==>> N[-1] = 1, N[0] = cf[0]; D[-1] = 0, D[0] = 1
    ==>> N[i+1] = N[i-1]+N[i]*cf[i+1]; D[i+1] = D[i-1]+D[i]*cf[i+1]

return (N[i], D[i]) for i in range(len(cf))
'''
    N_2, D_2 = ND_2
    N_1, D_1 = ND_1
    for c in cf:
        N0 = N_2 + N_1*c
        D0 = D_2 + D_1*c
        yield N0, D0
        N_2, D_2 = N_1, D_1
        N_1, D_1 = N0, D0
        
    return



one = sympify(1)
two = 2*one

def rsimplify(x):
    y = simplify(x)
    while y != x:
        x = y
        y = simplify(x)
    return y


def calc_until(pred_calc_at_prec, factor=10):
    prec = 1
    enough = False
    while not enough:
        prec *= factor
        enough, result = pred_calc_at_prec(prec)
    return result
    
def pred_divmod1(prec, x):
    _x = x.evalf(prec)
    int_part = floor(_x)
    r = x - int_part

    # 0 <= r < 1
    _r = r.evalf(prec)
    enough = (0 <= _r < 1)
    return enough, (int_part, r)

def divmod1(x):
    pred_x_divmod1 = lambda prec: pred_divmod1(prec, x)
    int_part, r = calc_until(pred_x_divmod1)
    return int_part, r

# try ratsimp error
# try radsimp yeah!
def continued_fraction_dc(x):
    '''return (floor(x), None if [INT x] else 1/(x-floor(x)))'''
    
    int_part, r = divmod1(x)
    
    r = radsimp(rsimplify(r))
    next_x = None if r == 0 else 1/r
    return int_part, next_x

def continued_fraction_expand_with_Xi(x, continued_fraction_next=continued_fraction_dc):
    '''let CF = continued_fraction_expand of x
return zip(CF, Xs)
assert CF[i] == floor(Xs[i]) for i >= 0
assert continued_fraction_pack(CF) == x
assert continued_fraction_pack(CF[:i]+[Xs[i]]) == x for i >= 0
assert lim N/D - x {for N,D in continued_fraction_pack_to_ND_pairs(CF)} -> 0


input:
    continued_fraction_next(x) = (floor(x), next_x(x))
        where next_x(x) = None if [INT x] else 1/(x-floor(x)) 
    x = a real number
    # maybe infinite long, use itertools.islice
'''
##    if L is None:
##        it = itertools.count()
##    else:
##        it = range(L)
##
##    for _ in it:
    while True:
        # int_part can be any integer
        int_part, x_ = continued_fraction_next(x)
        yield int_part, x
        
        break
    
##    for _ in it:
##        if x_ is None:
##            break
    while x_ is not None:
        x = x_
        
        int_part, x_ = continued_fraction_next(x)
        if int_part < 1:
            raise ArithmeticError('continued fraction element < 1')
        yield int_part, x

def continued_fraction_expand(x, continued_fraction_next=continued_fraction_dc):
    for c, _ in continued_fraction_expand_with_Xi(x,
        continued_fraction_next=continued_fraction_dc):
        yield c

def nth_pow_continued_fraction(x, n, L,
        continued_fraction_next=continued_fraction_dc):
    x0 = x**(one/n)
    return itertools.islice(
        continued_fraction_expand(x0, continued_fraction_next), L)

#cf, xs = nth_pow_continued_fraction(2,3,102)
#cf, xs = nth_pow_continued_fraction(2,3,116)
cf = nth_pow_continued_fraction(2,3,12)
cf, xs = unzip(2, continued_fraction_expand_with_Xi(2**(one/3)), 12)


raise


#############################################
#############################################
#############################################
#############################################
#############################################
#############################################
#############################################
#############################################


one = sympify(1)
two = 2*one

def rsimplify(x):
    y = simplify(x)
    while y != x:
        x = y
        y = simplify(x)
    return y


def calc_until(pred_calc_at_prec, factor=10):
    prec = 1
    enough = False
    while not enough:
        prec *= factor
        enough, result = pred_calc_at_prec(prec)
    return result
    
def pred_divmod1(prec, x):
    _x = x.evalf(prec)
    int_part = floor(_x)
    r = x - int_part

    # 0 <= r < 1
    _r = r.evalf(prec)
    enough = (0 <= _r < 1)
    return enough, (int_part, r)

def divmod1(x):
    pred_x_divmod1 = lambda prec: pred_divmod1(prec, x)
    int_part, r = calc_until(pred_x_divmod1)
    return int_part, r

# try ratsimp error
# try radsimp yeah!
def continued_fraction_dc(x):
    '''return (floor(x), None if [INT x] else 1/(x-floor(x)))
    require x >= 1'''
    
    int_part, r = divmod1(x)
    if int_part < 1:
        raise ValueError('not x >= 1')
    
    r = radsimp(rsimplify(r))
    next_x = None if r == 0 else 1/r
    return int_part, next_x

def continued_fraction_expand_more(x, cf, xs, moreL,
                                   continued_fraction_next=continued_fraction_dc):
    '''x - original number
cf - a list represent x's continued_fraction
xs - a list of numbers, s.t. continued_fraction_pack(cf[:i+1]+[xs[i]]) == x
output to: cf, xs
return None
'''
    assert len(cf) == len(xs)
    L = len(cf)
    x = xs[-1] if xs else x
    
    for _ in range(moreL):
        i, x = continued_fraction_next(x)
        cf.append(i)
        xs.append(x)
        if x is None:
            break

    assert len(cf) == len(xs) == L + moreL
    return
    
def continued_fraction_expand(x, L, continued_fraction_next=continued_fraction_dc):
    '''assert x >= 1
let CF = continued_fraction_expand
return CF(x, inf)[:L], Xs[:L]
assert x == continued_fraction_pack(CF(x)[:i]+[Xs[i-1]]) for i > 0

input:
continued_fraction_next(x) = (floor(x), next_x(x)) ; x>=1
    where next_x(x) = None if [INT x] else 1/(x-floor(x)) 
x = a fraction
L = length of elements in result
'''
    cf = []
    xs = []
    continued_fraction_expand_more(x, cf, xs, L, continued_fraction_next)
    assert len(cf) == len(xs) == L
    return cf, xs


def nth_pow_continued_fraction(x, n, L, continued_fraction_next=continued_fraction_dc):
    x0 = x**(one/n)
    return continued_fraction_expand(x0, L, continued_fraction_next)

#cf, xs = nth_pow_continued_fraction(2,3,102)
#cf, xs = nth_pow_continued_fraction(2,3,116)
cf, xs = nth_pow_continued_fraction(2,3,12)

raise


#############################################
#############################################
#############################################
#############################################
#############################################
#############################################
#############################################
#############################################

var('z')
one = z**0
two = 2*one
neval = N

def continued_fraction_dc(x):
    int_part = floor(x)
    if x == int_part:
        next_x = None
    else:
        next_x = 1/(x-int_part)
        next_x = together(next_x)
        N,D = fraction(next_x)
        assert D > 0
        assert N > D
        #assert not D > N  # here fire!!!
    return int_part, next_x

def continued_fraction_L(x, L, more=0):
    ls = []
    xs = []
    for _ in range(L):
        i, x = continued_fraction_dc(x)
        ls.append(i)
        xs.append(x)
        if x is None:
            break

    if not more:
        return ls
    elif more == 1:
        return ls, x
    elif more == 2:
        return ls, x, xs
    else:
        raise ValueError('unknown "more" value:', more)





def nth_pow_continued_fraction(x, n, L, more=False):
    x0 = x**(one/n)
    return continued_fraction_L(x0, L, more)


    ans = cf, x = nth_pow_continued_fraction(2,3,102, 1)
    '''
    ([1, 3, 1, 5, 1, 1, 4, 1, 1, 8, 1, 14, 1, 10, 2, 1, 4, 12, 2, 3, 2, 1, 3, 4, 1, 1, 2, 14, 3, 12, 1, 15, 3, 1, 4, 534, 1, 1, 5, 1, 1, 121, 1, 2, 2, 4, 10, 3, 2, 2, 41, 1, 1, 1, 3, 7, 2, 2, 9, 4, 1, 3, 7, 6, 1, 1, 2, 2, 9, 3, 1, 1, 69, 4, 4, 5, 12, 1, 1, 5, 15, 1, 4, 1, 1, 1, 1, 1, 89, 1, 22, 186, 6, 2, 3, 1, 3, 2, 1, 1, 5, 0], (-133450479581198331510402510274281177418327310779117149571 + 105919715836427477757469402582631193698068222179903783354*2**(1/3))/(-18946643396438422418200496503661148314139229271682874349*2**(1/3) + 23871274840024462774930909433822752859720888716067576820))
    NOTE: the final 0...
    '''

    N,D = continued_fraction2numerator_denominator(cf)
    N,D = (fraction(x))




########################## version 2

_q = symbols('q')
def _check_pos__pos(N_pair, w_pair):
    w_pow, w_nth = w_pair

    N_i, N_c = N_pair
    assert N_i >= 0
    assert -N_c >= 0
    assert (N_i-N_c)>0    # pos__pos
    #N = N_i + N_c*w
    assert N_i**w_nth > (-N_c)**w_nth * w_pow # pos
def _check_pos__neg(D_pair, w_pair):
    w_pow, w_nth = w_pair

    D_i, D_c = D_pair
    assert -D_i >= 0
    assert D_c >= 0
    assert (-D_i+D_c)>0  # pos__neg # diff with N !!
    #D = D_i + D_c*w
    assert D_c**w_nth * w_pow > (-D_i)**w_nth # pos


def eval_poly(poly, symbol, value):
    return poly.subs(symbol, value)


def zero_upper_bound_of_positive_poly(poly):
    poly = Poly(poly.expand())
    cs = poly.all_coeffs()
    cs0 = abs(cs[0])
    assert cs[0] == LC(poly)
    height = max(map(abs, cs))
    upper = ceiling(two*height/cs0)
    upper = int(upper)
    assert upper >= 2
    return upper


def num_radix_digits_base2(x):
    assert type(x) is int
    assert x > 0
    return x.bit_length()

def num_radix_digits(x, B):
    '''x>=1; B>=2; type(B) is int ; B**(n-1) <= x < B**n; return n

2 == num_radix_digits(i, 10) for i=10..99
n = floor(log x / log B) + 1 >= 1

[1<=x<B] ==>> n=1
[x>=B**m] ==>> B**m <= B**(n-1) <= x < B**n
    1 <= B**(n-m-1) <= x//B**m < B**(n-m)
    n = m + (n-m) = m + num_radix_digits(x//B**m, B)


num_radix_digits(i, 2) = i.bit_length()
let L = num_radix_digits(B, 2) >= 2
let t = num_radix_digits(x, 2)
2**(L-1) <= B < 2**L
2**(t-1) <= x < 2**t
2**(L-1)**(n-1) <= B**(n-1) <= x < B**n < 2**L**n
(L-1)*(n-1) <= t-1 < t <= L*n
n >= t/L; n >= ceil(t/L)
n-1 <= (t-1)/(L-1); n <= floor((t-1)/(L-1)) + 1
ceil(t/L) <= n <= floor((t-1)/(L-1)) + 1

floor((t-1)/(L-1)) + 1 - ceil(t/L) <= (t-1)/(L-1) + 1 - (t/L)
    = ((t-1)L-t(L-1))/(L-1)/L + 1
    = (t-L)/(L-1)/L + 1
    < t/(L-1)/L + 1

let m = ceil(t/L) > 0
    [x < B**m] ==>> n=m
    [B**m <= x][m>0] ==>> n = m + num_radix_digits(x//B**m, B)
    2**(t-1-m*L) < x/B**m < 2**(t-m(L-1)) = 2**(t-ceil(t/L)(L-1))
        <= 2**(t-t/L *(L-1)) = 2**(t/L)
    x->x/B**m ==>> t->(t/L) until t<L
    no more than floor(log t/log L)+1 steps.
    

'''
    x = int(floor(x))
    b = int(B)
    assert b == B
    B = b
    assert x >= 1
    assert B >= 2

    if B == 2:
        return num_radix_digits_base2(x)
    L = num_radix_digits_base2(B)
    assert L >= 2

    n = 0
    while True:
        assert x >= 1
        t = num_radix_digits_base2(x)
        m = (t+L-1)//L
        n += m
        B__m = B**m
        if x < B__m:
            return n
        x //= B__m
    raise logic-error

    

def floor_bucketed_root(poly, lower, upper):
    q, = poly.free_symbols
##    if upper - lower < 6:
##        assert count_roots(poly, lower, upper) == 1
##
##        for low in range(int(floor(lower)), int(floor(upper))+1):
##            if low+1 <= upper and sign(poly.subs(q, low+1)) == 0:
##                return low+1
##            if count_roots(poly, low, low+1) >= 1:
##                return low
##        raise logic-error
            
    max_abs_root = max(map(abs, (lower, upper)))
    max_abs_root = int(ceiling(max_abs_root))
    max_abs_root = min(max_abs_root, zero_upper_bound_of_positive_poly(poly))
    ndigit = num_radix_digits(max_abs_root, 2)
    eps = (one/2**(ndigit+3))
    low, up = refine_root(poly, lower, upper, eps=eps)
    Q = int(floor(low))
    if Q != int(floor(up)):
        Q1 = Q + 1
        assert low < Q1 <= up
        sign_at_Q1 = sign(poly.subs(q, Q+1))
        sign_at_up = sign(poly.subs(q, up))
        if sign_at_Q1 * sign_at_up <= 0:
            Q = Q1

    assert Q <= upper
    
    poly_at_Q = poly.subs(q, Q)
    Q1 = Q+1
    if not poly_at_Q == 0 and lower <= Q < Q1 <= upper:
        poly_at_Q1 = poly.subs(q, Q+1)
        assert sign(poly_at_Q) * sign(poly_at_Q1) < 0
    return Q
    

def _floor_div_nth_cf__end(poly, q):
    #print('count')
    assert count_roots(poly, 1) == 1
    assert count_roots(poly, -oo, +oo) <= 2 - (int(degree(poly)) & 1)
    assert eval_poly(poly, q, 1) <= 0
    

##    rs = real_roots(left)
##    qt = max(rs)
##    Q = floor(qt)
##    Q = int(neval(Q, ?))
    if not eval_poly(poly, q, 2) <= 0:
        Q = 1
    else:
        #print('refine_root')
        upper = zero_upper_bound_of_positive_poly(poly)
        #print(upper)
        try:
            assert eval_poly(poly, q, upper) > 0
        except:
            print(poly, upper, eval_poly(poly, q, upper))
            raise
        ndigit = num_radix_digits(upper, 10)
        eps = (one/10)**(ndigit+3)
        low, up = refine_root(poly, 1, upper, eps=eps)
        Q = int(floor(low))
        assert Q == int(floor(up))

    assert Q >= 1
    assert not poly.subs(q, Q) > 0
    assert not poly.subs(q, Q+1) <= 0
    return Q


def _floor_div_nth_cf__end_v1(poly, q):
    '''
it seems N(RootOf(...)) is too slow
I try to use refine_root instead.
'''
    rs = real_roots(poly)
    qt = max(rs)
    Q = floor(qt)

    upper = zero_upper_bound_of_positive_poly(poly)

    ndigit = num_radix_digits(upper, 10)
    Q = int(neval(Q, ndigit+3))

    assert Q >= 1
    assert not poly.subs(q, Q) > 0
    assert not poly.subs(q, Q+1) <= 0
    return Q


def sign(n):
    return 1 if n > 0 else -1 if n < 0 else 0
def sign_nth_pair(N_pair, w_pair):

    w_pow, w_nth = w_pair
    assert w_pow >= 0, w_nth > 0
    #w = w_pow**(1/w_nth)

    N_i, N_c = N_pair
    if sign(N_i) * sign(N_c) >= 0:
        if N_pair == (0,0):
            return 0
        elif N_i >= 0 and N_c >= 0:
            return +1
        elif N_i <= 0 and N_c <= 0:
            return -1
    elif N_i > 0 and N_c < 0:
        return sign(N_i**w_nth - (-N_c)**w_nth * w_pow)
    elif N_c > 0 and N_i < 0:
        return sign(N_c**w_nth * w_pow - (-N_i)**w_nth)
    raise logic-error

def neg_nth_pair(pair, w_pair=None):
    a,b = pair
    return (-a, -b)
def times_nth_pair(x, pair, w_pair=None):
    a,b = pair
    return (x*a, x*b)
def add_nth_pair(a_pair, b_pair, w_pair=None):
    return tuple(x+y for x,y in zip(a_pair, b_pair))
def sub_nth_pair(a_pair, b_pair, w_pair=None):
    return tuple(x-y for x,y in zip(a_pair, b_pair))
def cmp_nth_pair(a_pair, b_pair, w_pair):
    d = sub_nth_pair(a_pair, b_pair)
    return sign_nth_pair(d, w_pair)

    
def floor_div_nth_cf__pos(N_pair, D_pair, w_pair):
    '''N>=D>0, w>=0, return floor(N/D)


w_pow, w_nth = w_pair
assert w_pow >= 0, w_nth > 0
w = w_pow**(1/w_nth)

N_i, N_c = N_pair
assert N_i >= 0, -N_c >= 0, (N_i-N_c)>0
N = N_i + N_c*w
assert N_i**w_nth >= (-N_c)**w_nth * w_pow

D_i, D_c = D_pair
assert -D_i >= 0, D_c >= 0, (-D_i+D_c)>0  # diff with N !!
D = D_i + D_c*w
assert D_c**w_nth * w_pow > (-D_i)**w_nth


assume Q = floor(N/D)
Q = max{int q | N >= q*D} >= 1
N_i - D_i*q >= (-N_c + D_c*q)*w >= 0
(N_i - D_i*q)**w_nth >= (-N_c + D_c*q)**w_nth * w_pow
assert (N_i - D_i)**w_nth >= (-N_c + D_c)**w_nth * w_pow
(-N_c + D_c*q)**w_nth * w_pow - (N_i - D_i*q)**w_nth <= 0
# note: [.q**w_nth] left = D_c**w_nth * w_pow - (-D_i)**w_nth > 0
real_roots(left)

let qt = the-only-positive-real-root(left)
Q = floor(qt)

assert (N_i - D_i*Q)**w_nth >= (-N_c + D_c*Q)**w_nth * w_pow
assert (N_i - D_i*(Q+1))**w_nth < (-N_c + D_c*(Q+1))**w_nth * w_pow
'''
    

    w_pow, w_nth = w_pair
    assert w_pow >= 0, w_nth > 0
    #w = w_pow**(1/w_nth)

    N_i, N_c = N_pair
    D_i, D_c = D_pair
    _check_pos__pos(N_pair, w_pair)
    _check_pos__neg(D_pair, w_pair)


    #assume Q = floor(N/D)
    #Q = max{int q | N >= q*D} >= 1
    #N_i - D_i*q >= (-N_c + D_c*q)*w >= 0
    #(N_i - D_i*q)**w_nth >= (-N_c + D_c*q)**w_nth * w_pow
    assert (N_i - D_i)**w_nth >= (-N_c + D_c)**w_nth * w_pow
    #(-N_c + D_c*q)**w_nth * w_pow - (N_i - D_i*q)**w_nth <= 0
    # note: [.q**w_nth] left = D_c**w_nth * w_pow - (-D_i)**w_nth > 0
    left = (-N_c + D_c*_q)**w_nth * w_pow - (N_i - D_i*_q)**w_nth
    Q = _floor_div_nth_cf__end(left, _q)
    
    try:
        assert (N_i - D_i*Q)**w_nth >= (-N_c + D_c*Q)**w_nth * w_pow
        assert (N_i - D_i*(Q+1))**w_nth < (-N_c + D_c*(Q+1))**w_nth * w_pow
    except:
        print(qt)
        print(Q)
        raise
    return Q




def floor_div_nth_cf__neg(N_pair, D_pair, w_pair):
    '''N>=D>0, w>=0, return floor(N/D)


w_pow, w_nth = w_pair
assert w_pow >= 0, w_nth > 0
w = w_pow**(1/w_nth)

N_i, N_c = N_pair
assert -N_i >= 0, N_c >= 0, (-N_i+N_c)>0
N = N_i + N_c*w
assert N_c**w_nth * w_pow > (-N_i)**w_nth

D_i, D_c = D_pair
assert D_i >= 0, -D_c >= 0, (D_i-D_c)>0  # diff with N !!
D = D_i + D_c*w
assert D_i**w_nth > (-D_c)**w_nth * w_pow


assume Q = floor(N/D)
Q = max{int q | N >= q*D} >= 1
(N_c - D_c*q)*w >= -N_i + D_i*q >= 0
(N_c - D_c*q)**w_nth * w_pow >= (-N_i + D_i*q)**w_nth
assert (N_c - D_c)**w_nth * w_pow >= (-N_i + D_i)**w_nth
(-N_i + D_i*q)**w_nth - (N_c - D_c*q)**w_nth * w_pow <= 0
# note: [.q**w_nth] left = D_i**w_nth - (-D_c)**w_nth * w_pow > 0
real_roots(left)

let qt = the-only-positive-real-root(left)
Q = floor(qt)

assert (N_i - D_i*Q)**w_nth >= (-N_c + D_c*Q)**w_nth * w_pow
assert (N_i - D_i*(Q+1))**w_nth < (-N_c + D_c*(Q+1))**w_nth * w_pow
'''
    

    w_pow, w_nth = w_pair
    assert w_pow >= 0, w_nth > 0
    #w = w_pow**(1/w_nth)


    N_i, N_c = N_pair
    D_i, D_c = D_pair
    _check_pos__neg(N_pair, w_pair)
    _check_pos__pos(D_pair, w_pair)


##    assume Q = floor(N/D)
##    Q = max{int q | N >= q*D} >= 1
##    (N_c - D_c*q)*w >= -N_i + D_i*q >= 0
##    (N_c - D_c*q)**w_nth * w_pow >= (-N_i + D_i*q)**w_nth
    assert (N_c - D_c)**w_nth * w_pow >= (-N_i + D_i)**w_nth
##    (-N_i + D_i*q)**w_nth - (N_c - D_c*q)**w_nth * w_pow <= 0
##    # note: [.q**w_nth] left = D_i**w_nth - (-D_c)**w_nth * w_pow > 0
##    real_roots(left)
    left = (-N_i + D_i*_q)**w_nth - (N_c - D_c*_q)**w_nth * w_pow

##    let qt = the-only-positive-real-root(left)
##    Q = floor(qt)
    Q = _floor_div_nth_cf__end(left, _q)
    assert (N_i - D_i*Q)**w_nth >= (-N_c + D_c*Q)**w_nth * w_pow
    assert (N_i - D_i*(Q+1))**w_nth < (-N_c + D_c*(Q+1))**w_nth * w_pow
    return Q


def nth_continued_fraction_dc__v2(N_pair, D_pair, w_pair):
    a,b = N_pair
    floor_div_nth_cf = floor_div_nth_cf__pos if a-b > 0 else floor_div_nth_cf__neg
    Q = floor_div_nth_cf(N_pair, D_pair, w_pair)
    R_pair = tuple(a-Q*b for a,b in zip(N_pair, D_pair))
    return Q, D_pair, R_pair


def nth_pow_continued_fraction__v2(x, n, L, more):
    assert x >= 1
    assert n >= 1
    
    NDw = N_pair, D_pair, w_pair = (0,1), (1,0), (x,n)
    ls = []
    zero = (0,0)
    for _ in range(L):
        ans = Q, N_pair, D_pair = nth_continued_fraction_dc(N_pair, D_pair, w_pair)
        #print(ans)
        #print(type(Q), type(N_pair), list(map(type, N_pair)))
        ls.append(Q)
        if D_pair == zero:
            r = None
            break
    else:
        r = N_pair, D_pair
    if more == 0:
        return ls
    elif more == 1:
        return ls, r
    else:
        raise 'unknown "more" value'




def floor_div_nth_cf__nonzeroD(N_pair, D_pair, w_pair):
    '''D!=0, w>=0, return floor(N/D)

w_pow, w_nth = w_pair
assert w_pow >= 0, w_nth > 0
w = w_pow**(1/w_nth)

if D < 0: N, D = -N, -D
N_i, N_c = N_pair
D_i, D_c = D_pair
assert sign_nth_pair(D_pair, w_pair) > 0


assume Q = floor(N/D)
Q = max{int q | N >= q*D} >= 1
let N == q*D
(N_c - D_c*q)*w == -N_i + D_i*q
(N_c - D_c*q)**w_nth * w_pow == (-N_i + D_i*q)**w_nth
    (N_c - D_c*q)*w*nth_root(1,w_nth) == -N_i + D_i*q
    (N_c - D_c*q)*(+/-)w == -N_i + D_i*q or N_c - D_c*q == -N_i + D_i*q == 0
    q = N/D or (N_i-N_c*w)/(D_i-D_c*w) if [even w_nth] or N_c/D_c == N_i/D_i == N/D
    if N/D == (N_i-N_c*w)/(D_i-D_c*w) ==>>
        (N_i+N_c*w)*(D_i-D_c*w) == (N_i-N_c*w)*(D_i+D_c*w)
        (N_c*D_i - N_i*D_c)*w == 0
    len(real_roots(eq)) == 1 + [even w_nth][N_c*D_i != N_i*D_c]


'''

    w_pow, w_nth = w_pair
    assert w_pow >= 0, w_nth > 0

    #assert sign_nth_pair(D_pair, w_pair) > 0
    s = sign_nth_pair(D_pair, w_pair)
    if not s > 0:
        if s == 0:
            raise ValueError('D == 0')
        N_pair = neg_nth_pair(N_pair)
        D_pair = neg_nth_pair(D_pair)
    N_i, N_c = N_pair
    D_i, D_c = D_pair
        

    f = (N_c - D_c*_q)**w_nth * w_pow - (-N_i + D_i*_q)**w_nth
    f = f.expand()
    if LC(f) < 0:
        f = -f
    f = Poly(f)
##    upper = zero_upper_bound_of_positive_poly(f)
##    ndigit = num_radix_digits(upper, 2)
##    eps = (one/2**(ndigit+3))
    rngs = f.intervals()
    rngs = intervals(f)
    if len(rngs) == 2:
        assert w_nth & 1 == 0 # even
        assert N_i*D_c != N_c*D_i
        
        (low, up), m = rngs[0]
        # cmp(N, up*D) = cmp(N, a/b*D) = cmp(b*N, a*D)
        a, b = fraction(up)
        assert b > 0
        bN = times_nth_pair(b, N_pair)
        aD = times_nth_pair(a, D_pair)
        s = cmp_nth_pair(bN, aD)
        assert s
        if s < 0:
            # Q in rngs[0]
            del rngs[1]
        else:
            del rngs[0]
        
    assert len(rngs) == 1
    (low, up), m = rngs[0]
    Q = floor_bucketed_root(f, low, up)
    R_pair = sub_nth_pair(N_pair, times_nth_pair(Q, D_pair))
##    Q = int(floor(low))
##    R_pair = sub_nth_pair(N_pair, times_nth_pair(Q, D_pair))
##    if not cmp_nth_pair(R_pair, D_pair, w_pair) < 0:
##        Q += 1
##        R_pair = sub_nth_pair(R_pair, D_pair)
    assert sign_nth_pair(R_pair, w_pair) >= 0
    assert cmp_nth_pair(R_pair, D_pair, w_pair) < 0
    return Q, R_pair


def nth_continued_fraction_dc__v3(N_pair, D_pair, w_pair):
    Q, R_pair = floor_div_nth_cf__nonzeroD(N_pair, D_pair, w_pair)
    return Q, D_pair, R_pair

nth_continued_fraction_dc = nth_continued_fraction_dc__v3

f = nth_pow_continued_fraction

def show(N, n, L, more=False):
    for i in range(N):
        print(i, f(i, n, L, more))



s=show


cf, x = nth_pow_continued_fraction__v2(2,3,20,1)#102, 1)
print(cf, x)
cf, x = nth_pow_continued_fraction__v2(2,3,402,1)
print(cf, x)
#print(nth_pow_continued_fraction(2,3,10,1))










    







