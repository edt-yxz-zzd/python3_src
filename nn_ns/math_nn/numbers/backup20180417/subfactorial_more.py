


'''

inversion formula 


[int n >= 0] ==>>
    g n = (-1)**n T**n f 0 <==> f n = (-1)**n T**n g 0
    g n = sum C(n,i)(-1)**i f(i) {i} <==> f n = sum C(n,i)(-1)**i g(i) {i}
    g n = (-1)**n T**n f 0 = sum C(n,i)(-1)**i f(0+i) {i} for [int n>=0]
    f n = sum (T**i f 0)C(n, i) {i} = sum C(n, i) (-1)**i g (i) for [int n>=0]

[int n] ==>> // well, after all, only n>=0
    F f n = sum C(n,i)(-1)**i f(i) {i} 
        = sum C(n,i)(-1)**i f(i) {i>=0}

    F f -1 = sum C(-1,i)(-1)**i f(i) {i} = sum [i>=0]f(i) {i}
    F f -2 = sum [i>=0](i+1)f(i) {i}
    [n>0] ==>> F f -n = sum C(n+i-1,i) f(i) {i>=0} 
        = sum C(n+i-1,n-1) f(i) {i>=0}
    
    F f n ~ f (i>=0) // f need not define above negatives
    // we donot care F f (i<0), too
    
    prove F.F = 1 // F.F f n = f n, for n >= 0
    [int n>=0] ==>> f n =?= sum C(n,i)(-1)**i sum C(i,j)(-1)**j f(j) {j} {i}
    right = sum f(j) (-1)**j sum C(n,i)C(i,j) (-1)**i {i} {j}
    sum C(n,i)C(i,j) (-1)**i {i} = sum C(n,j)C(n-j,i-j) (-1)**i {i}
        = (when int n>=j for symitry or int n and j>n>=0 for C(n,j)=0) 
            (that is int n>=0)C(n,j) sum C(n-j,i) (-1)**(i+j) {i}
        = C(n,j) (-1)**j sum C(n-j,i) (-1)**i {i}
        = C(n,j) (-1)**j [n-j=0]
    right = sum f(j) (-1)**j C(n,j) (-1)**j [n-j=0] {j}
        = f(n)C(n,n) = f(n) = left


    S f n = (-1)**n f n
    S.S = 1
    
    G f n = F.S f n = sum C(n,i)f(i) {i}, for n>=0  // Newton series
    H f n = S.F f n = sum C(n,i)(-1)**(n-i) f(i) {i}, for n>=0  // H f n = T**n f 0
    H.G = S.F.F.S = 1
    G.H = F.S.S.F = 1


derangement = permutation which moves every item
subfactorial[n] = numbers of all derangements of n objects, int n>=0
subfactorial[0] = 1
subfactorial[1] = 0
subfactorial[2] = 1
subfactorial[3] = 2

n! = sum C(n,i)subfactorial[i] {i} // subfactorial is Newton series of n!  !!!!!
factorial = G.subfactorial
==>> subfactorial = H.factorial
    subfactorial[n] = sum C(n,i)(-1)**(n-i) i! {i>=0}
        = sum fall(n,i)(-1)**(n-i) {i>=0}
        = n! sum 1/(n-i)! (-1)**(n-i) {i>=0, n-i>=0}
        = n! sum (-1)**i / i! {i=0..n}
    [n>=0] ==>> subfactorial[n+1] = sum fall(n+1,i)(-1)**(n+1-i) {i>=0}
        = sum (n+1)fall(n,i-1)(-1)**(n-(i-1)) {i>0} + (-1)**(n+1)
        = (n+1)subfactorial[n] + (-1)**(n+1)
    subfactorial[n] =  n subfactorial[n-1] + (-1)**n, for n>=1


subfactorial[n] = n! sum (-1)**i / i! {i=0..n}
    = n! sum (-1)**i / i! {i>=0} - n! sum (-1)**i / i! {i>n}
    = n!/e + (-1)**n (1/(n+1) - 1/(n+1)/(n+2) + ...)
    = n!/e + (-1)**n * (t which 1/(n+2) < t < 1/(n+1))
    = n!/e + 1/2   +   (-1)**n * t - 1/2
    // [n>=1] ==>> -1/2 < (-1)**n * t < 1/3 ==>> -1<tail<-1/6
    = floor(n!/e + 1/2) + [n=0]
subfactorial[n]/n! ~=~ 1/e = 0.36787944117144233 ~=~ 36.8%

---------------------------  floor(n!/e+1/2)  ----------------------
how to calc floor(n!/e+1/2) ??
floor(n!/e+1/2) = floor (floor(2*n!/e+1)/2) = (floor(2*n!/e)+1)//2
floor(2*n!/e) = ?

# see : continued_fraction.py
K = 2*n!, x = 1/e
if 0 < err < 1/D**2:
    F[2k], using even indices
    D[3k+1] >= II a[i] {i=1..3k+1} = 2 II 2i {i=1..k} >= K = 2*n!
    ==>> k >= n
    let t = 3n+1
    let s = t + [odd t] = t + t%2
    floor(2*n!/e) = 2*n!*N[s]//D[s]

    floor(n!/e + 1/2) + [n=0] = (floor(2*n!/e)+1)//2 + [n=0]
    = (K*N[s]//D[s] + 1)//2 + [n=0]
    
    
    


'''




from .continued_fraction import continued_fraction2numerator_denominator, \
     continued_fraction2numerator_denominator_pairs, \
     invE2continued_fraction





def is_even(n):
    return int(n%2 == 0)

def _1_pow_n(n):
    return -1 if n%2 else 1

assert _1_pow_n(0) == 1
assert _1_pow_n(1) == -1


def subfactorial_by_recurrence_neg1(n):
    assert n >= 0
    if n == 0:
        return 1
    return n*subfactorial_by_recurrence_neg1(n-1) + _1_pow_n(n)


def factorials(n):
    assert n >= 0
    ls = [1]
    for i in range(1,n):
        ls.append(ls[-1]*i)
        
    if n == 0:
        ls = ls[:n]
        
    assert len(ls) == n
    return ls


    
def subfactorial_by_floor_mul_invE(n):
    assert n >= 0
    t = 3*n+1
    s = t + (t%2)
    assert s%2 == 0
    
    cf = invE2continued_fraction(s)
    N, D = continued_fraction2numerator_denominator(cf)

    # K = 2 * n!
    K = 2
    for i in range(1,n+1):
        K *= i
        
    assert K <= D

    # floor(n!/e + 1/2) + [n=0] = (K*N[s]//D[s] + 1)//2 + [n=0]
    m = K*N//D
    r = (m+1)//2 + (n==0)
    return r


def subfactorials_by_floor_mul_invE(n):
    assert n >= 0
    t = 3*n+1
    s = t + (t%2)
    assert s%2 == 0
    cf = invE2continued_fraction(s)
    NDs = continued_fraction2numerator_denominator_pairs(cf)

    fs = factorials(n)
    ls = []
    for i in range(n):
        t = 3*i+1
        s = t + (t%2)
        assert s%2 == 0

        N, D = NDs[s]
        K = 2*fs[i]
        assert K <= D
        
        m = K*N//D
        r = (m+1)//2 + (i==0)
        ls.append(r)
    return ls

        
        
        
    
    
    
def subfactorials(n):
    assert n>=0

    # subfactorial[-1] = anything
    pre_subfactorial = 0
    
    ls = []
    sign = -1
    for k in range(n):
        sign = -sign
        curr_subfactorial = k*pre_subfactorial + sign
        ls.append(curr_subfactorial)
        
        pre_subfactorial = curr_subfactorial
        
    return ls

assert subfactorials(4) == [1,0,1,2]
assert subfactorials(20) == [subfactorial_by_recurrence_neg1(i) for i in range(20)]
assert subfactorials(20) == [subfactorial_by_floor_mul_invE(i) for i in range(20)]
assert subfactorials(20) == subfactorials_by_floor_mul_invE(20)



def _try_factor_subfactorials(n):
    from sympy import factorint
    r = list(map(factorint, subfactorials(n)))
    print(r)

def _find_neg_x():
    
    # continued_fraction2numerator_denominator
    from sympy.physics.quantum.shor import \
         continued_fraction as numerator_denominator2continued_fraction
    from sympy import Mod
    from sympy.abc import a,b,c
    N,D = continued_fraction2numerator_denominator([0,a,b,c])
    x=N/D
    r=1-x
    rD = D.expand()
    rN = (D-N).expand()
    print(rN, rD)
    
if __name__ == '__main__':
    pass




















        
















