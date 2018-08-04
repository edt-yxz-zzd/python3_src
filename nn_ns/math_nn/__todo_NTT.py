
'''
=================================================================
DFT - discrete fourier transform
!!! may not invertible !!!
R - ring with 1
!!! maybe not commutative !!!
n - in N+
w - in R, w^n = 1, 0 = sum((w^k)^j for j in [0..n-1]) for k in [1..n-1]
                   #   {{k*j mod n for j in [0:n]} for k in [1:n]}
                   # = {{k*(j*u) mod n for j in [0:n]} for k in [1:n]} where gcd(u,n) = 1
                   #   choose u(k), s.t. u(k)*k = gcd(k,n) mod n
                   # = {{gcd(k,n)*j mod n for j in [0:n]} for k in [1:n]}
                   # = {{g*j mod n for j in [0:n]} for g|n, 0<g<n}
               <=> 0 = sum w^(k*j) for j in [0:n] for k|n, 0<k<n
               <=> 0 = n//k * sum w^(k*j) for j in [0:n//k] for k|n, 0<k<n
                   #   inv(n//k) might not exist
                   # (w^k-1)*sum w^(k*j) for j in [0:n//k] = w^k^(n//k)-1 = 0
                   # w^n = 1 => w^k-1 != 0 but XX=>XX sum .. = 0 XXXXX
                   # since inv(w^k-1) might not exist.
                     
A,B - in R^n
def Vandermonde_matrix(A[0..r-1], c) = [d(i,j) = A[i]^j for i,j in [0..r-1]*[0..c-1]]
def symmetric_Vandermonde_matrix(L,a) = [d(i,j) = a^(i*j) for i,j in [0..L-1]]
DFT - (R,n,w,A) -> B
    DFT = symmetric_Vandermonde_matrix(n,w)
    B = DFT * A
if R is a domain with 1 (ab=0 <=> a=0 or b=0, 1 != 0)
    => sum((w^k)^j for j in [0..n-1])*(w^k - 1) = (w^k)^n - 1 = 0
    => sum((w^k)^j for j in [0..n-1]) = 0 or (w^k - 1) = 0 #mutually exclusive
    => "sum((w^k)^j for j in [0..n-1]) = 0  <=> w^k != 1" for k in [1..n-1]

inverse of DFT
!!! require 1/n in R !!!
n in U(R)
IDFT - (R,n,w,B) -> A
    IDFT = DFT(R,n,1/w)
    A = IDFT * B

implement DFT
    r[i] - i|n, r[i] = w^(n//i) is a i-th root of unity
    p for n > 1 - p|n, p is prime
    SVM - symmetric_Vandermonde_matrix
    (*) - Kronecker product, D(*)M = [d(i,j)] (*) M = [d(i,j)*M](#d is scale) = (D(*)I[len(M)])*(I[len(D)](*)M)
    (^t) - transpose
    (^-1) - inverse
    I[n] - identity matrix of size n
    diag(..) - diagonal matrix
    TO,TI,XTI - permutation matrix, P(^t) = P(^-1)
    XDFT - XDFT*XTI = DFT
    if TI(n,p) = [d(i,j) = i == j%p*n//p + j//p = j == i%(n//p)*p + i//(n//p)] != TI(^t) =>
        DFT(n,r[n],A)[i] for i in [0:n] = sum (r[n]^i)^j * A[j] for j in [0:n]
            # let A' = TI(n,p)*A, so A[j] = A'[j%p*n//p + j//p]
            = sum (r[n]^i)^(j%p + j//p*p) * A'[j%p*n//p + j//p] for j in [0:n]
            = sum (r[n]^i)^(u+v*p) * A'[u*n//p+v] where u=j%p,v=j//p for j in [0:n]
            = sum (r[n]^i)^(u+v*p) * A'[u*n//p+v] for u in [0:p] for v in [0:n//p]
            = sum (r[n]^i)^u*sum (r[n]^p^i)^v * A'[u*n//p+v] for v in [0:n//p] for u in [0:p]
            = sum (r[n]^i)^u*sum r[n//p]^(i%(n//p))^v * A'[u*n//p+v]
                    for v in [0:n//p] for u in [0:p]
            # note i%(n//p) in [0:n//p], compare to this DFT definition:
            = sum (r[n]^i)^u * DFT(n//p, r[n//p], A'[u*n//p:(u+1)*n//p])[i%(n//p)]
                    for u in [0:p]
            # def sub_DFT(n,n//p,r[n//p]) = I[p](*)DFT(n//p,r[n//p])
            # let A'' = sub_DFT(n,n//p,r[n//p]) * A'
            # that is A''[u*n//p:(u+1)*n//p] = DFT(n//p, r[n//p], A'[u*n//p:(u+1)*n//p])
            #       for u in [0:p]
            = sum (r[n]^i)^u * A''[u*n//p + i%(n//p)] for u in [0:p]
            # note that DFT(n,r[n],A)[i] ~ A''[j] for i = j mod n//p
            # DFT(n,r[n],A)[k:n//p:] ~ A''[k:n//p:]
            # DFT(n,r[n],A)[k:n//p:] = [d(i,j) = (r[n]^(k+i*n//p))^j] * A''[k:n//p:]
            # (r[n]^(k+i*n//p))^j = r[n]^(k*j+i*j*n//p) = (r[n]^k)^j * r[p]^(i*j)
            # DFT(n,r[n],A)[k:n//p:] = [d(i,j) = r[p]^(i*j) for i,j in [0:p]]
            #                           * diag((r[n]^k)^j for j in [0:p]) * A''[k:n//p:]
            # def twiddle(n,r[n],p) = diag(r[n]^(i%(n//p))^(i//(n//p)) for i in [0:n])
            # def butterfly(n,p,r[p]) = DFT(p,r[p])(*)I[n//p]
            = (butterfly(n,p,r[p]) * twiddle(n,r[n],p) * A'')[i]
        DFT(n,r[n])
            = pass if n == 1
            = butterfly(n,p,r[p]) * twiddle(n,r[n],p) * sub_DFT(n,n//p,r[n//p]) * TI(n,p)
        # note that DFT at any level, TI(n~,p~) will be performed before any non-TI operation
        def XDFT(n,r[n],ps)
            = pass if n == 1
            = butterfly(n,p,r[p]) * twiddle(n,r[n],p) * sub_XDFT(n,n//p,r[n//p],ps)
            where p = ps[0], sub_XDFT(n,n//p,r[n//p],ps) = I[p](*)XDFT(n//p,r[n//p],ps[1:])
        def XTI(n,ps) = n==1? pass : sub_XTI(n,n//p,ps) * TI(n,p)
            where p = ps[0], sub_XTI(n,n//p,ps) = I[p](*)XTI(n//p,ps[1:])
        DFT = XDFT * XTI

        # Cooley–Tukey algorithm
        TI(n,p) = [d(i,j) = i == j%p*n//p + j//p = j == i%(n//p)*p + i//(n//p)] # as above
        def array2matrix(r, c, A) for len(A) == r*c = [d(i,j) = A[c*i+j]]
        array2matrix(^-1)(r,c, M) = [a(i)=M[i//c,i%c]]
        then TI(n,p,A) = array2matrix(^-1)(p,n//p,array2matrix(n//p,p,A)(^t))
        def PTI(n,s,p,A) for p|s|n=len(A), p > 1
            = I[p](*)TI(s,p)
            = for i in [0:n//s]: A'[i*s:(i+1)*s] = TI(s,p) * A[i*s:(i+1)*s]
            # i' = b + i_%p*s//p + i_//p where i_ = i%s, b = i-i_ = i//s*s
            #    = i//s*s + i%s%p*s//p + i%s//p
            #    = i//s*s + i%p*s//p + (i//p)%(s//p)
            #    = i//s*s + i%p*s[+1] + i//p%s[+1]      # s[+1]*p = s, i=i[-1] i'=i[0] s[0] p[0]
            # i[+1] = i'//s[+1]*s[+1] + i'%p[+1]*s[+2] + i'//p[+1]%s[+2]
            #       = (i//s*s + i%p*s[+1] + i//p%s[+1])//s[+1]*s[+1] + (i//s*s + i%p*s[+1] + (i//p)%s[+1])%p[+1]*s[+2] + (i//s*s + i%p*s[+1] + i//p%s[+1])//p[+1]%s[+2]
            #       = i//s*s + i%p*s[+1] + i//p%p[+1]*s[+2] + i//(s//s[+2])%s[+2]
            # i[+2] = i[0](i[+1](i)) = i[+1](i[0](i))  // i[0] = i'
            # i[+3] = i[+1](i[+1](i)) = i[+1]//s[+2]*s[+2] + i[+1]%p[+2]*s[+3] + i[+1]//p[+2]%p[+3]*s[+4] + i[+1]//(s[+2]//s[+4])%s[+4]
            #       = i//s*s + i%p*s[+1] + i//p%p[+1]*s[+2] + i//(s//s[+2])%p[+2]*s[+3] + i//(s//s[+3])%p[+3]*s[+4] + i//(s//s[+4])%s[+4]
            # i[+n] = i//s*s + sum(i//(s//s[+j])%p[+j]*s[+j+1] for j in [0:n+1]) + i//(s//s[+n+1])%s[+n+1]
            #################################################################
            # p = [..], p[i] > 0
            # s = [..], p[0]|s[0] > 0, s[i+1] = s[i]*p[i+1], s[-1] = s[0]//p[0]
            # def f(b,d,i) for b,d,i >= 0
            # def f(b,0,i) = i   # begin from p[b], s[b]
            # def f(b,d+1,i) = f(b,d,i)//s[b+d]*s[b+d] + TI(s[b+d],p[b+d],[0:s[b+d]])[f(b,d,i)%s[b+d]]
            #                = f(b,d,i)//s[b+d]*s[b+d] + e(f(b,d,i)%s[b+d]) * TI(s[b+d],p[b+d])*[0:s[b+d]]
            #                = f(b,d,i)//s[b+d]*s[b+d] + f(b,d,i)%s[b+d]%(s[b+d]//p[b+d])*p[b+d] + f(b,d,i)%s[b+d]//(s[b+d]//p[b+d])
            #                = f(b,d,i)//s[b+d]*s[b+d] + f(b,d,i)%s[b+d-1]*p[b+d] + f(b,d,i)//s[b+d-1]%p[b+d]
            #                # note that        s[b+d] > f(b,d,i)%s[b+d-1]*p[b+d] + f(b,d,i)//s[b+d-1]%p[b+d]
            # f(0,d,i) = ?
            # f(b+d,d',f(b,d,i)) =??= f(b,d+d',i)??
            # f(b,d+2,i) = f(b,d+1,i)//s[b+d+1]*s[b+d+1] + f(b,d+1,i)%s[b+d]*p[b+d+1] + f(b,d+1,i)//s[b+d]%p[b+d+1]
            #            = f(b,d,i)//s[b+d+1]*s[b+d+1] + f(b,d,i)%s[b+d-1]*p[b+d]*p[b+d+1] + f(b,d,i)//s[b+d-1]%p[b+d]*p[b+d+1] + f(b,d,i)//s[b+d]%p[b+d+1]
            # ??f(b,d+n+1,i) = f(b,d,i)//s[b+d+n]*s[b+d+n] + f(b,d,i)%s[b+d-1]*(s[b+d+n]//s[b+d-1]) + sum f(b,d,i)//s[b+d+i-1]%p[b+d+i]*(s[b+d+n]//s[b+d+i]) for i in [0:n+1]
            # ??f(b,d+n+1,i) - f(b,d,i)//s[b+d+n]*s[b+d+n] < s[b+d+n]
            # f(b,d+n+2,i) = f(b,d+n+1,i)//s[b+d+n+1]*s[b+d+n+1] + f(b,d+n+1,i)%s[b+d+n+1-1]*p[b+d+n+1] + f(b,d+n+1,i)//s[b+d+n+1-1]%p[b+d+n+1]
            #              = f(b,d,i)//s[b+d+n+1]*s[b+d+n+1] + f(b,d,i)%s[b+d-1]*(s[b+d+n+1]//s[b+d-1]) + sum f(b,d,i)//s[b+d+i-1]%p[b+d+i]*(s[b+d+n+1]//s[b+d+i]) for i in [0:n+2]
            # the two ?? above is correct.
            # ??f(b,d+1,i) = f(b+d,1,f(b,d,i)) = f(b+d,1,f(b+d-1,1..f(b+1,1,f(b,1,f(b,0,i)...)
            # f(b+d,1,i)(i=f(b,d,i)) = f(b+d,0,i)//s[b+d]*s[b+d] + f(b+d,0,i)%s[b+d-1]*p[b+d] + f(b+d,0,i)//s[b+d-1]%p[b+d]
            #                        = f(b,d,i)//s[b+d]*s[b+d] + f(b,d,i)%s[b+d-1]*p[b+d] + f(b,d,i)//s[b+d-1]%p[b+d]
            #                        = f(b,d+1,i) !!!!!!!
            # f(b,d+1,i) = f(b+d,1,f(b+d-1,1..f(b+1,1,f(b,1,f(b,0,i)...)
            #            = f(b+d..f(b+d-k,1 $ f(b+d-k-1...f(b,0,i)...)
            #            = f(b+d..f(b+d-k,1,f(b+d-k,0, $ f(b,d-k,i)
            #            = f(b+d-k, k+1, f(b,d-k,i))
            # f(b,d,i) = f(b+d-k, k, f(b,d-k,i))
            # f(b', k, f(b, b'-b, i)) = f(b,b'-b+k,i)
            #
        XTI(n,ps)*A: A'[i] = A[f(reverse(ps),i)]

    ##################################
    p|n, i in [0:n], w
    B[i] = sum a[j]*(w^i)^j for j in [0:n]
         = sum sum a[j+p*k]*(w^i)^(j+p*k) for k in [0:n//p] for j in [0:p]
         = sum (w^i)^j*sum a[j+p*k]*(w^p^i)^k for k in [0:n//p] for j in [0:p]
         = sum (w^i)^j*DFT(n//p,w^p,a[j:p:n])[i_] for j in [0:p]
             # w^p^i = w^p^i_ for i_ in [0:n//p]
             # p*i = p*i_ mod n
             # i_ = i mod n//p
         = sum (w^i)^j*DFT(n//p,w^p,a[j:p:n])[i % (n//p)] for j in [0:p]
         # assign ~a[j:p:n] := DFT(n//p,w^p,a[j:p:n])
         = sum (w^i)^j*~a[j:p:n][i % (n//p)] for j in [0:p]
         = sum (w^i)^j*~a[j+p*(i % (n//p))] for j in [0:p]
    i_ in [0:n//p], k in [0:p]
    B[i_+k*n//p] = sum w^(i_+k*n//p)^j*~a[j+p*i_] for j in [0:p]
    
    def DFT(R,n,w,A,begin,step):
        if n = 1, return;
        choose p s.t. p|n and is_prime(p)
        for i in [0:p]:
            DFT(R,n//p,w^p,A,begin+step*i,step*p)
        B[0:n]
        for i in [0:n//p]:
            t = A[begin+step*p*i:step:begin+step*p*(1+i)]
            for k in [0:p]:
                B[i+k*n//p] = sum(w^((i+k*n//p)*j % n)*t[j] for j in [0:p])
        A[begin:step:begin+step*n] = B
        return;

def DFT(n, w, A):
    ps = factors(n) s.t. II ps = n and is_prime(p) for p in ps
    ws = [w^II ps[i+1:] for i in [0:len(ps)]] = [...,w^p[-1],w]
    ns = [II ps[0:i+1] for i in [0:len(ps)]]
    steps = [II ps[i+1:] for i in [0:len(ps)]] # steps[i]*ns[i] = n
    B = [0]*len(A) # buffer
    n_ = 1
    step = n # n = n_ * step
    for round in [0:len(ps)]:
        pre_n = n_
        pre_step = step  # n = pre_n * pre_step
        p_ = ps[round]
        w_ = ws[round]
        n_ = ns[round]      #      n_   = pre_n    * p_
        step = steps[round] # p_ * step = pre_step
        # using B[0:n_]
        for begin in [0:step]:
            for i in [0:pre_n]:
                t = A[begin + pre_step * i : step : begin + pre_step * (1+i)]
                for k in [0:p_]:
                    B[i+k*pre_n] = sum(t[j] * w**((i+k*pre_n)*j % n) for j in [0:p])
            #A[begin:step:begin+step*n_] = B
            for i in [0:n_]: A[begin + step * i] = B[i]
    return A;
    # number of round: len(ps)
    # operations in each round: for round of p_, n*(p_-1) mul&add&pow_root
    # if n = II p[i]^e[i] => number of the 3 operation is
    #    sum n*(p[i]-1)*e[i] = n*(sum p[i]*e[i] - sum e[i]) ~= max ps * n*log n
    # let max ps be min => n = 2^x



=================================================================
NTT - number-theoretic transform
The number-theoretic transform (NTT)
is obtained by specializing the discrete Fourier transform to ring Z/mZ.

m - in N+                           # => for ring Z/mZ
w - n-th root of unity in U(Z/mZ)   # => DFT requires
n - in N+, gcd(n,m)=1, n|lambda(m)  # => IDFT requires, ord[m](w) requires

NTT(n,w) = [ntt(i,j) = w^(i*j) for i,j in [0..n-1]]
INTT(n,w) = 1/n * NTT(n,1/w)

if n = p^x => gcd(p,m)=1, exists q|m s.t. q is prime and q = k*p^x + 1
def multiplicity(n,p) = max{i | p^i|n} 
let f(p,m) = max {(q,x) | q | m, q is prime, x = multiplicity(q-1,p)}
for a given m, f(p,m).x is the max n can use in NTT,
since the max order of primitive roots is y*p^f(p,m).x (gcd(y,p)=1)
so for a given n = p^x, the min m is a (k*p^x + 1)prime with min k.

note that modulo m is expensive, for binary number, let m be 2^x + d, d is small number.
if d = 0 and x > 2, m = 2^x, R = Z/2^xZ,
    U(R) ~=~ I(2) * I(2^(x-2)), 3 is a 2^(x-2)-th root of 1.
    but lambda(m) = 2^(x-2) | m
    so n is odd for gcd(n,m)=1, n = 1 for n|m
if d = +/-1, m = 2^x +/- 1, factor(m) to find q=k*p^x+1


=================================================================
NTT-based multiplicative algorithm # with Chinese Remainder Theorem??
A, B, C - in N, C = A*B
A(x),B(x),C(x) - polynomials over Ring R and N, C(x) = A(x)*B(x)
exists u, A = A(u), B = B(u), so C = C(u)
a[] - A(x) = sum a[i]x^i, so are B(x),C(x)
na, nb, nc - degree(A)
a' = NTT(n,w,a) => a'[i] = A(w^i), c'[i] = C(w^i) = A(w^i)*B(W^i) = a'[i]*b'[i] R[x]/(x^n-1)
R[x] - UID # => f(x) of degree n in R[x] has no more than n roots??
    => coefficient(Ar(x)*Br(x)) is unique.
    => envalue A(x) and B(x) at nc(=na+nb) point in R is enough too determine C(x) in R[x]
    but this is not enough to get C(x) in N[x]
let R be finite, then N->R is not bijection, so as N[x]->R[x]
    if R is Z/mZ, and map R[x]->N[x] by natural map coeff[i]->coeff[i]%m,
    then we must keep : max(a[])*max(b[])*min(na,nb) < m.

N-point DFT:
    w^N = 1
    a[] = a0,a1...// infinite long
    A(w) = a0*1+..,a[N-1]*w^(N-1)+ a[N]...
         = 1*(a[0]+a[N]+..) + w(a[1]+..) + ... + w^(N-1)(a[N-1]+...)
         = 1*a~[0] + w*a~[1]... + w^(N-1)*a~[N-1]
    if a[i] != 0 for i >= N, then do N-pt DFT will map A(x)->A(x)/(x^N-1)
    let N >= nc = na + nb

na = floor_log(u,A)
n >= floor_log(u,A) + floor_log(u,B) # n-point NTT
m > (u-1)^2*min(na,nb)
n | lambda(m) => exists w - a n-th root of unity in Z/mZ
factors of n








=================================================================
root of unity modulo m
Number of k-th roots f(m,k) = len[i for i in [0..m) if i^k = 1 mod m]
f(m,1) = 1, m > 1
f(m,lamda(m)) = phi(m) # the max multiplicative order is lambda(m)
    where lamda = Carmichael function, phi = Euler's totient function
    lambda(m) = Carmichael_function(m)
        = min [i for i in [1..] if and[1 == a^i mod m for a in U(m)]]
        = lcm lambda(p[i]^e[i])
    lambda(p^e) = phi(p^e) = p^(e-1)*(p-1) if p is odd prime
    lambda(2^e) = phi(2^e) if e = 1 or 2
                = 1/2*phi(2^e) if e > 2
f(ab,k) = f(a,k)*f(b,k) if gcd(a,b) = 1
f(m,k)|f(m,L) if k|L
f(m,lcm(a,b)) = lcm(f(m,a),f(m,b))
f(m,p^i)=p^j, any i exists j
=================================================================
Find lamda(m)-th primitive root of unity
Finding an m with a primitive k-th root of unity modulo m
    and more let gcd(k,m)=1
    try k*?+1 !!!!!!!!! 


=================================================================
Prime Fermat numbers 
F0 = 3,   F1 = 5,   F2 = 17,   F3 = 257,   F4 = 65537
Prime factors  k*2^n + 1  of Fermat numbers  F[m]
F[m] = 1 + 2^2^m = II{ k*2^n + 1 }  (n>=m+2)
m,  k,  n
5,  5,  7,
6,  1071,  8,
7,  116503103764643,  9,
8,  604944512477,  11,
9,  37,  16,
9,   3640431067210880961102244011816628378312190597,  11,  
10,  1137640572563481089664199400165229051,   12,  
10,  11131,  12,  
10,  395937,  14,  
11,  39,  13,  
11,  119,  13,  
11,  10253207784531279,  14,  
11,  434673084282938711,  13,

Prime                 m = 0, 1, 2, 3, 4  
Completely factored   m = 5, 6, 7, 8 (two factors each), 9 (3 factors),  
                          10 (4 factors), 11 (5 factors)  


if d | 2^2^m+1 then d = k2^(m+2)+1
F5 = 641 * 6700417  
F6 = 274177 * 67280421310721  
F7 = 59649589127497217 * 5704689200685129054721  
F8 = 1238926361552897 * P62  
F9 = 2424833 * 7455602825647884208337395736200454918783366342657 * P99  
F10 = 45592577 * 6487031809 * 4659775785220018543264560743076778192897 * P252  
F11 = 319489 * 974849 * 167988556341760475137 * 3560841906445833920513 * P564
=================================================================
List of known Mersenne primes
M[p] = 2^p - 1
p =
2,  3,  5,  7,  13,  17,  19,  31,  61,  89,  107,  127,  521,  607,
1279,  2203,  2281,  3217,  4253,  4423,  9689,  9941,  11213,  19937,
21701,  23209,  44497,  86243,  110503,  132049,  216091,  756839,
859433,  1257787,  1398269,  2976221,  3021377,  6972593,  13466917,
20996011,  24036583,  25964951,  30402457,  32582657,  37156667,
42643801,  43112609,  57885161

if d | 2^p-1 then d = 2kp+1 # 2^p = 1 mod (2kp+1) for some k
d = +/-1 mod 8
too test M[p](p is prime!), may use d that
1) in both form 2kp+1 and 8x+/-1,
2) is prime and < sqrt(M[p])

p,   Factors of 2^p-1 (non-prime M[p] for p < 200)
11,   23,   89,   
23,   47,   178481,   
29,   233,   1103,   2089,   
37,   223,   616318177,   
41,   13367,   164511353,   
43,   431,   9719,   2099863,   
47,   2351,   4513,   13264529,   
53,   6361,   69431,   20394401,   
59,   179951,   3203431780337,   
67,   193707721,   761838257287,   
71,   228479,   48544121,   212885833,   
73,   439,   2298041,   9361973132609,   
79,   2687,   202029703,   1113491139767,   
83,   167,   57912614113275649087721,   
97,   11447,   13842607235828485645766393,   
101,   7432339208719,   341117531003194129,   
103,   2550183799,   3976656429941438590393,   
109,   745988807,   870035986098720987332873,   
113,   3391,   23279,   65993,   1868569,   1066818132868207,   
131,   263,   10350794431055162386718619237468234569,   
137,   32032215596496435569,   5439042183600204290159,   
139,   5625767248687,   123876132205208335762278423601,   
149,   86656268566282183151,   8235109336690846723986161,   
151,   18121,   55871,   165799,   2332951,   7289088383388253664437433,   
157,   852133201,   60726444167,   1654058017289,   2134387368610417,   
163,   150287,   704161,   110211473,   27669118297,   36230454570129675721,   
167,   2349023,   79638304766856507377778616296087448490695649,   
173,   730753,   1505447,   70084436712553223,   155285743288572277679887,   
179,   359,   1433,   1489459109360039866456940197095433721664951999121,   
181,   43441,   1164193,   7648337,   7923871097285295625344647665764672671,   
191,   383,   7068569257,   39940132241,   332584516519201,   87274497124602996457,   
193,   13821503,   61654440233248340616559,   14732265321145317331353282383,   
197,   7487,   26828803997912886929710867041891989490486893845712448833,   
199,   164504919713,   4884164093883941177660049098586324302977543600799,   

=================================================================
primitive roots of unity modulo Mersenne number or Fermat number

note: f(ab,k) = f(a,k)*f(b,k) if gcd(a,b) = 1
let Q(m) = 2^2^m - 1 = Q(m-1)*F(m-1) = Q(0)*F(0)*..*F(m-1)
         = II F(i) for i in [0..m)
since gcd(F(i),F(j)) = 1 iff i != j

'''


import functools
import operator
def DFT(ring1, n, ps, ws, wn, a): # n = IIps, ws[i] is a IIps[i:] root, wn = [ws[0]^i]
    assert n == functools.reduce(operator.mul, ps)
    assert all(p > 0 and type(p) == int for p in ps)
    assert len(a) == n == len(wn)
    assert ring1.power(w,n) == ring1.one()
    for i in range(1,n):
    assert 


