
'''

continued fraction
[a0;a1,a2...] = ~ + [inf]*inf
let F[i] = N[i]/D[i] = [a0;a1,...,a[i]]
let N[-2]/D[-2] = ][ = 0/1 = 0
let N[-1]/D[-1] = [] = 1/0 = inf
then F[i] = N[i]/D[i] = (a[i]N[i-1]+N[i-2])/(a[i]D[i-1]+D[i-2])
N[0]/D[0] = a0/1 = [a0;]
N[1]/D[1] = (a1 N[0] + N[-1])/(a1 D[0] + D[-1]) = (a1 a0 + 1)/(a1 + 0) = a0 + 1/a1 = [a0;a1]


[int a[i] for all i][a[i]>0 for i > 0]
==>> D[n] >= II a[i] {i=1..n} // exclude a0
==>> D[i] = a[i]D[i-1]+D[i-2] >= D[i-1]+D[i-2] for i > 0
    D[0] = a[0]D[0-1]+D[0-2] = a[0]*0+D[0-2] = 1*D[0-1]+D[0-2]
    ==>> D[i] >= D[i-1]+D[i-2] for all i
    [D[-2]=f[-1]][D[-1]=f[0]]
    ==>> D[i] >= fibonacci[i+1] = floor(golden_ratio**(i+1)/sqrt(5) + 1/2)
            > G**(i+1)/sqrt(5) - 1/2 = G**i * G/r_5 - 1/2
            > (8/5)**i * 5/7 - 1/2
            > (8/5)**i * 5/8 - 1/2
            > (8/5)**(i-1) - 1/2
            > (3/2)**(i-1) - 1/2
    where golden_ratio = (1+sqrt(5))/2 = 1.61803...
    D[0]=1>(8/5)**(-1) and D[1]>=1=(8/5)**(1-1) and 1+(8/5)>(8/5)**2
    ==>> D[i] >= (8/5)**(i-1)
    let 1 <= x <= G ==>> 1+x >= x**2
        [D[0]=1>=k][D[1]>=1>=k*x]:
            ==>> k <= 1/x <= 1
            D[i] >= k*x**i
            let k = 1/x
            D[i] >= x**(i-1)
        let x = G
        D[i] >= G**(i-1)
    
==>> N[i]*D[i-1] - N[i-1]*D[i] = (a[i]N[i-1]+N[i-2])*D[i-1] - N[i-1]*(a[i]D[i-1]+D[i-2])
    = N[i-2]*D[i-1] - N[i-1]*D[i-2]
    = (-1)(N[i-1]*D[i-2] - N[i-2]*D[i-1])
    = (-1)**i (N[0]*D[-1] - N[-1]*D[0])
    = (-1)**i (a0*0 - 1*1)
    = -(-1)**i
==>> gcd(N[i], D[i]) = 1
==>> F[i] - F[i-1] = N[i]/D[i] - N[i-1]/D[i-1]
    = (N[i]*D[i-1] - N[i-1]*D[i])/D[i]/D[i-1]
    = -(-1)**i/D[i]/D[i-1]
==>> F[n] = F[0] + sum F[i] - F[i-1] {i=1..n}
    = a0 + sum -(-1)**i/D[i]/D[i-1] {i=1..n}

==>> F[2n] < F[2n+2]; F[2n-1] > F[2n+1]; F[2k] < F[2m+1]
    F[0] < F[2] < F[4] < ... < F[inf]=fraction < ... < F[5] < F[3] < F[1] < F[-1] = inf
    if a0 > 0 ==>> 0 = F[-2] < F[0]
==>> D[i]>D[i-1] for i >= 0
==>> let F[inf] = F[n] + err[n], for n>=0
    |err[n]| = |F[inf]-F[n]| < |F[n+1]-F[n]| = 1/D[n+1]/D[n] < 1/D[n]**2
    sign(err[n]) = (-1)**n


----------------------------- simplify.1 ------------------------------
# nonstandard form : [a0;a1,...] for a[i] = 0..inf
[.;..a,inf,...] = [.;..a]
[.;..,a,0,b,...] = [.;..,a+b,...]
[.;..a,b,0,inf...] = [.;..a,b+inf] = [.;..a,inf...]
[.;..,a,1,inf...] = [.;..,a+1]
[inf;...] = [] = 1/[0;] = +/-inf = NaN


# simplify is required here
1 / [0; a1,...] = [a1;...]
1 - [0;a1,a2,...] = [0;1,a1-1,a2,...]
    let x2 = [a2;...]
    1 - [0;a1,x2] = 1 - 1/(a1+1/x2) = 1-x2/(a1*x2+1) = (a1*x2+1-x2)/(a1*x2+1)
        = ((a1-1)*x2+1)/(a1*x2+1) = 1/((a1*x2+1)/((a1-1)*x2+1))
        = 1/(1+x2/((a1-1)*x2+1)) = 1/(1+1/(a1-1+1/x2)) = [0;1,a1-1,x2]
b - [a0;a1,a2,...] = b+a0-1 + 1-[0;a1,a2,...]
    = [b+a0-1;1,a1-1,a2,...]
-[a0;a1,a2,...] = [-(a0+1);1,a1-1,a2,...] # NOTE: when a1 == 1 or len == 1


1 / [a0;a1,...] = -1/-[a0;a1,...] if a0 < 0
1 / [a0; a1,...] = [0;a0,a1...] # NOTE: when a0 <= 0

------------------------ simplify.2 -------------------------
[a0;-a1,a2...] = [a0; [-a1;a2,...]]
    = [a0; -(a1 - [0;a2,...])]
    = [a0; -[a1-1;1,a2-1,a3,...]]
    = a0 - [0;a1-1,1,a2-1,a3,...]
    = [a0-1;1,a1-2,1,a2-1,a3,...] if a1 >= 2
    = a0 - [0;0,1,a2-1,a3,...] if a1 == 1
        = a0 - [1;a2-1,a3,...]
        = [a0;1,a2-2,a3,...] if a2 >= 2
        = a0 - [1;0,a3,...] if a2 == 1
            = a0 - [a3+1;...]
            = [a0+a3;1,a4-1,a5,...]
[.;..a0,-a1,a2...] = [a0-1;1,a1-2,1,a2-1,a3,...]
[.;..a0,-1,a2...] = [a0;1,a2-2,a3,...]
[.;..a0,-1,1,a3...] = [a0+a3;1,a4-1,a5,...]





----------------------- e -------------------------
e = [2;1,2,1,1,4,1,1,6,1,1,8,...] = 1+[1;1,2,   1,1,4,   1,1,6...]
    = [2;  1,2,1, 1,4,1,  1,6,1,  1,8,...]
    = [1;0,1,  1,2,1,  1,4,1,  1,6,1,  1,8,...]
e-1 = [1;1,2,   1,1,4,   1,1,6...]
//bad: [1;1,0,   1,1,2,   1,1,4,   1,1,6...] = 1+1/(1+1/(0+(e-1))) = 1+1/(e/(e-1)) = (2e-1)/e
3-e = 1-(e-2) = [0;3,  1,1,4,1,1,6,1,1,8,...]
1/e = [0;2,  1,2,1,   1,4,1,  1,6,1,  1,8,...]



----------------------- floor(K*x) --------------------
floor(x) = floor (x*D/D) = floor (floor(x*D)/D)

let x = N/D + err where 0 < err < 1/D, D large enough, N = floor(D*x)
    0 < err*D < 1
    floor(K*x) = ?
    floor(K*x) = floor (floor(K*x*D)/D)
    if x = 1/3 = 0.3333... = 333/1000 + err, K = 3
        floor(K*x) = 1
        but for any D = 10**n, we can get the result from (D,N,K) = (10**n, floor(10**n*x), 3)
    fail...

let x = N/D + O(1/D**2) = N/D + err, 0<err<1/D**2, D large enough
    [0 < err*D < 1/D]:
        x*D = N + O(1/D) = N + err*D ==>> [not int x*D]
  
        floor(K*x) = ?
        K*x = (K*N + K*err*D)/D < (K*N + K*1/D)/D
        K*x > (K*N + 0)/D
        [0<K<=D]:
            K*x*D = K*N + err*K*D ==>> [not int K*x*D]
            floor (K*x*D) = K*N; ceil(K*x*D) = K*N+1
        [0<K<=D][N>0]:
            floor(K*x) = floor (floor(K*x*D)/D) = floor (K*N/D) = (K*N)//D
            ceil(K*x) = ceil (ceil(K*x*D)/D) = ceil((K*N+1)/D) = (K*N+D)//D
                    = floor(K*x) + 1 # since [not int K*x]
    [0<abs(K)<=abs(D)][0<err<1/D**2]:
        floor(abs(K*x)) = abs(K*N)//abs(D)
        [K*x < 0]:
            floor(K*x) = -ceil(abs(K*x)) = -floor(abs(K*x))-1
                = -abs(K*N)//abs(D) -1
        floor(K*x) = abs(K*N)//abs(D)*signs(K,N,D) - [K*x<0]

given K>0: [K<=D] <<== D[i] >= G**(i-1) >= K <<== i >= log(G, K) + 1
    <<== i >= ceil(log(G,K)) + 1 <<== i >= floor(log(3/2,K)) + 2
    # log(3/2,K) = lg K /(lg 3 - 1) < K.bit_length *2
    <<== i >= K.bit_length *2 + 2
required at most (K.bit_length *2 + 2) continued fraction digits of x
to calc floor(K*x)

'''




from seed.iters.head import head
from sand import to_names #, head
from sand import top_level_import
assert top_level_import(__name__, 'import_main.forgot_import', args=('logic error',))

import itertools, math
from itertools import chain, count

from fractions import Fraction
##from ..numbers.continued_fraction import \
##     continued_fraction2numerator_denominator, \
##     continued_fraction2numerator_denominator_pairs, \
##     invE2continued_fraction


__all__ = to_names('''
continued_fraction_pack_to_ND_pairs, calc_Xi, calc_Xs_from_NDs\
, calc_Xi_from_continued_fraction_ls\
, inv_continued_fraction, neg_continued_fraction\
, continued_fraction_of_e_sub_1, continued_fraction_of_e\
, continued_fraction_expand, continued_fraction_expand_with_Xi\
, finite_continued_fraction2Fraction\
, finite_continued_fraction2ND\
, ND2continued_fraction\
, ND2Fraction, Fraction2ND

''')


NaNError = lambda:ValueError(
    'continued_fraction should not be empty iterable. it stands for NaN.')

def cf_head(cf):
    a0, cf = head(cf, NaNError)
    return a0, cf

def continued_fraction_of_e_sub_1():
    '''e-1 = [1;1,2,   1,1,4,   1,1,6...]

e = [2;1,2,1,1,4,1,1,6,1,1,8,...] = 1+[1;1,2,   1,1,4,   1,1,6...]
'''
    for n in count(2, None, 2):
        yield 1
        yield 1
        yield n

def continued_fraction_of_e():
    '''e = [2;1,2,1,1,4,1,1,6,1,1,8,...] = 1+[1;1,2,   1,1,4,   1,1,6...]
    = [2;  1,2,1, 1,4,1,  1,6,1,  1,8,...]
    = [1;0,1,  1,2,1,  1,4,1,  1,6,1,  1,8,...]'''
    
    yield from continued_fraction_add_int(
        continued_fraction_of_e_sub_1(), 1)
def continued_fraction_add_int(cf, n):
    a0, cf = cf_head(cf)
    yield a0 + n
    yield from cf
    
def inv_continued_fraction(cf):
    '''1 / [a0; a1,...] = [0;a0,a1...]
    = [0;0,a1...] = [a1;...] if a0 == 0 # so [] stand for 1/0 ??
    = -1/-[a0;a1,...] if a0 < 0'''
    
    a0, cf = cf_head(cf)

    if a0 == 0:
        # discard a0
        yield from cf
    elif a0 > 0:
        yield 0
        yield a0
        yield from cf
    else:
        cf = chain([a0], cf)
        inv = inv_continued_fraction
        neg = neg_continued_fraction
        yield from neg(inv(neg(cf)))

def neg_continued_fraction(cf):
    '''-[a0;a1,a2,...] = [-(a0+1);1,a1-1,a2,...] # NOTE: when a1==1

-[a0;a1,a2,...] = [-a0;] if len(~) == 1
    = [-(a0+1);1,a1-1,a2,...] if a1>=2
    = [-(a0+1);a2+1,...] if a1==1'''
    a01 = list(itertools.islice(cf, 2))
    if not a01:
        raise NaNError()
    elif len(a01) == 1:
        a0, = a01
        yield -a0
    else:
        a0, a1 = a01
        yield -(a0+1)

        if a1 == 1:
            for a2 in cf:
                yield a2+1 # if no a2, do nothing
        else:
            yield 1
            yield a1-1
            
        yield from cf



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

x = (N[i-2]+N[i-1]*xs[i])/(D[i-2]+D[i-1]*xs[i])
(D[i-2]+D[i-1]*xs[i])x = (N[i-2]+N[i-1]*xs[i])
D[i-2]x - N[i-2] = N[i-1]*xs[i] - D[i-1]*xs[i]x
-N[i-2] + D[i-2]x = (N[i-1] - D[i-1]x)*xs[i]
xs[i] = (-N[i-2]+D[i-2]*x)/(N[i-1]-D[i-1]*x)
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

def finite_continued_fraction2ND(cf):
    ND = None
    for ND in continued_fraction_pack_to_ND_pairs(cf):pass

    if ND is None:
        raise NaNError
    return ND

def ND2Fraction(ND):
    N, D = ND
    return Fraction(N, D)

def finite_continued_fraction2Fraction(cf):
    ND = finite_continued_fraction2ND(cf)
    return ND2Fraction(ND)

def Fraction2ND(fr):
    return fr.numerator, fr.denominator






def calc_Xi(x, NDi_2, NDi_1):
    '''x = (N[i-2]+N[i-1]*xs[i])/(D[i-2]+D[i-1]*xs[i])
xs[i] = (-N[i-2]+D[i-2]*x)/(N[i-1]-D[i-1]*x)'''

    Ni_2, Di_2 = NDi_2
    Ni_1, Di_1 = NDi_1
    return (-Ni_2+Di_2*x)/(Ni_1-Di_1*x)
def calc_Xs_from_NDs(x0, NDs):
    def extend_NDs(NDs):
        ND_2 = (0,1)
        for ND_1 in itertools.chain([(1,0)], NDs):
            yield ND_2, ND_1
            ND_2 = ND_1
    for NDi_2, NDi_1 in extend_NDs(NDs):
        xi = calc_Xi(x0, NDi_2, NDi_1)
        yield xi
    
def calc_Xi_from_continued_fraction_ls(x, cf, i):
    '''return Xs[i] where 0 <= i <= L = len(cf)

NDs = continued_fraction_pack_to_ND_pairs(cf, ND_2=(0,1), ND_1=(1,0))
'''
    NDs = list(itertools.islice(continued_fraction_pack_to_ND_pairs(cf), i))
    if len(NDs) != i:
        raise ValueError('too few data to calc Xi : len(cf) < i')

    NDs = [(0,1), (1,0)] + NDs[-2:]
    NDs = NDs[-2:]
    assert len(NDs) == 2
    
    return calc_Xi(x, *NDs)
##
##    x_2_3 = sympify('2**(1/3)')
##
##    cf = cf2_3_196 = [
##        1, 3, 1, 5, 1, 1, 4, 1, 1, 8, 1, 14, 1, 10, 2, 1, 4, 12, 2, 3, 2, 1,
##        3, 4, 1, 1, 2, 14, 3, 12, 1, 15, 3, 1, 4, 534, 1, 1, 5, 1, 1, 121, 1,
##        2, 2, 4, 10, 3, 2, 2, 41, 1, 1, 1, 3, 7, 2, 2, 9, 4, 1, 3, 7, 6, 1, 1,
##        2, 2, 9, 3, 1, 1, 69, 4, 4, 5, 12, 1, 1, 5, 15, 1, 4, 1, 1, 1, 1, 1,
##        89, 1, 22, 186, 6, 2, 3, 1, 3, 2, 1, 1, 5, 1, 3, 1, 8, 9, 1, 26, 1, 7,
##        1, 18, 6, 1, 372, 3, 13, 1, 1, 14, 2, 2, 2, 1, 1, 4, 3, 2, 2, 1, 1, 9,
##        1, 6, 1, 38, 1, 2, 25, 1, 4, 2, 44, 1, 22, 2, 12, 11, 1, 1, 49, 2, 6,
##        8, 2, 3, 2, 1, 3, 5, 1, 1, 1, 3, 1, 2, 1, 2, 4, 1, 1, 3, 2, 1, 9, 4,
##        1, 4, 1, 2, 1, 27, 1, 1, 5, 5, 1, 3, 2, 1, 2, 2, 3, 1, 4, 2]
##    f = calc_x_2_3_i = lambda i: calc_Xi_from_continued_fraction_ls(x_2_3, cf2_3_196, i)
##    _x = calc_x_2_3_i(len(cf))
##    x_2_3_196 = sympify(
##        r'(-1758611251246164499755591770271168460583147347695166957604521807631686283946564544652333671236665059796423 '
##        '+ 1395810675115636538189945963642856225991328613425347213056096345279847395624054282113678653213582232849159*2**(1/3))'
##        '/(-3084008555669920290285410389175311137397699586117070085668430110389150154412758628072531502309795955245923*2**(1/3) '
##        '+ 3885607297344417366264274553567531362271346191878684541623911020305962607918267260931731541044089373559770)')
##    assert _x == x_2_3_196




################## continued_fraction_expand ##################
def continued_fraction_next(x):
    '''continued_fraction_next(x) = (floor(x), next_x(x))
    where next_x(x) = None if [INT x] else 1/(x-floor(x))
        '''
    n = math.floor(x)
    tail = x - n
    next_x = None if not tail else 1/tail
    return n, next_x
        
        
    
def continued_fraction_expand_with_Xi(x,
    continued_fraction_next=continued_fraction_next):
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
            raise ArithmeticError('continued fraction element < 1 :\n'
                                  '\tx = {!r}'.format(x))
        yield int_part, x

def continued_fraction_expand(x,
    continued_fraction_next=continued_fraction_next):
    for c, _ in continued_fraction_expand_with_Xi(x, continued_fraction_next):
        yield c

def ND2continued_fraction(ND):
    N, D = ND
    x = Fraction(N, D)
    cf = continued_fraction_expand(x)
    cf = tuple(cf)
    return cf

######################### [int]->positive_int #########################
##def int2positive_int(n):
##    n *= 2
##    if n <= 0:
##        n = 1 - n
##    return n
##
##def positive_int2int(n):
##    if n <= 0:
##        raise ValueError('n <= 0')
##
##    if n % 2:
##        # n <= 0
##        n = 1 - n
##    n //= 2
##    return n
##
##def _test_int2positive_int(N):
##    for n in range(-N, N):
##        p = int2positive_int(n)
##        assert p > 0
##        assert positive_int2int(p) == n
##_test_int2positive_int(10)
##
##
##def ints2positive_int_pair(ints):
##    # assert list(ints)
##    cf = positive_ints = map(int2positive_int, ints)
##    N, D = list(continued_fraction_pack_to_ND_pairs(cf))[-1]
##    assert N > 0
##    assert D > 0
##    return N, D
##
##def positive_int_pair2ints(positive_int_pair):
##    N, D = positive_int_pair
##    if not (N>0 and D>0):
##        raise ValueError('not all positive')
##
##    cf = ND2continued_fraction(N, D)
##    return tuple(map(positive_int2int, cf))
##



    




 

######################### old version from numbers.subfatorial.py :
##     continued_fraction2numerator_denominator, \
##     continued_fraction2numerator_denominator_pairs, \
##     invE2continued_fraction

def continued_fraction2numerator_denominator(continued_fraction):
    N_2, D_2 = 0, 1
    N_1, D_1 = 1, 0
    for a in continued_fraction:
        N = a*N_1 + N_2
        D = a*D_1 + D_2
        N_2, D_2 = N_1, D_1
        N_1, D_1 = N, D
    return N_1, D_1

def continued_fraction2numerator_denominator_pairs(continued_fraction):
    pairs = []
    N_2, D_2 = 0, 1
    N_1, D_1 = 1, 0
    for a in continued_fraction:
        N = a*N_1 + N_2
        D = a*D_1 + D_2
        pairs.append((N,D))
        
        N_2, D_2 = N_1, D_1
        N_1, D_1 = N, D

    assert len(pairs) == len(continued_fraction)
    return pairs



def invE2continued_fraction(n):
    '''continued_fraction of 1/e with len (n+1)'''
    
    ls = [0, 2]
    # L = len(ls) = 3k+1 + 1 >= n+1
    # k >= (n+1)//3
    k = (n+1)//3
    L = 3*k + 2
    assert L >= n+1
    for i in range(1, k+1):
        ls += [1,2*i,1]
    assert len(ls) == L
    
    ls = ls[:n+1]
    assert len(ls) == n+1
    return ls





