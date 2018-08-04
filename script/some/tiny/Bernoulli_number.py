
'''
Bernoulli numbers
z/(e**z - 1) = sum(B[i]*z**i/i! for i in [0, inf))

z == (e**z - 1)*sum(...) == sum(z**i/i! for i in [1, inf)) * sum(...) \
  == sum(z**i * sum(1/(i-k)! * B[k]/k! for k in [0, i)) for i in [1, inf))

i == 1 ==>> 1 == B[0];
i > 1 ==>> 0 == sum(B[k]/k!/(i-k)! for k in [0, i)) for i in [2, inf)
B[i-1] = -(i-1)! * sum(B[k]/k!/(i-k)! for k in [0, i-1)) for i in [2, inf)
B[i]/i! = -sum(B[k]/k!/(i+1-k)! for k in [0, i)) for i in [1, inf)


let s(k, n) = sum(i**k for i in [1,n)) = 1**k + ... + (n-1)**k \
              for k in [0, inf) for n in [1, inf)
s(k, 1) == 0
s(k, 2) == 1
assume s(k, n) = sum(a[k][i] * n**(k+1-i) for i in [0, k+1])
# s(0, n) = a[0][0]n + a[0][1] = n-1

# n**0 == a[0][0]((n+1)-n) + a[0][1](1-1) = a[0][0] // a[0][1] not exists!
# using s(k,1) == 0
n**k == s(k, n+1) - s(k, n) \
     == sum(a[k][i] * ((n+1)**(k+1-i) - n**(k+1-i)) for i in [0, k+1])\
     == sum(a[k][i] * ((n+1)**(k+1-i) - n**(k+1-i)) for i in [0, k])\
     == sum(a[k][i] * sum(n**j * C(k+1-i, j) for j in [0, k-i]) for i in [0, k])\
     == sum(n**j * sum(a[k][i]*C(k+1-i, j) for i in [0, k-j]) for j in [0, k])

# k=1 ==>> a[0]nn+a[1]n+a[2] ==>> n**1 == 2a[0]n+a[0] + a[1]
# t=1, j=0: 0n**0 = n**0/0! * sum(a[j]*(2-j)!/(2-j)! for j in range(2))
# == 1*(a[0]+a[1])
j == k       ==>> 1 == a[k][0]*C(k+1-0, j) == a[k][0]*(k+1)!/k!
j in [0,k-1] ==>> 0 == sum(a[k][i]*C(k+1-i, j) for i in [0, k-j]) \
             ==>> a[k][k-j]*C(k+1-(k-j), j) == a[k][k-j]*C(j+1, j) \
                  == -sum(a[k][i]*C(k+1-i, j) for i in [0, k-1-j])\
                  let t = k-j
             ==>> a[k][t]*C(k+1-t, k-t) == -sum(a[k][i]*C(k+1-i, k-t) for i in [0, k-1-(k-t)])\
                 == -sum(a[k][i]*C(k+1-i, k-t) for i in [0, t-1])
                 


                 a[k][i]*C(k+1-i, k-t) == a[k][i]*(k+1-i)!/(t+1-i)!  /(k-t)!
                 a[k][t]*(k+1-t)!/k! == -sum(a[k][i]*(k+1-i)!/k!/(t+1-i)! for i in [0, t-1])
                 a[k][i]*(k+1-i)!/k! == B[i]/i!
                 
                 a[k][i] = B[i]*k!/i!/(k+1-i)! = B[i]*C(k+1, i) / (k+1)
a[k][k+1] == s(k,1) - sum(a[k][i] for i in [0, k])
    a[k][k+1]*(k+1-(k+1))!/k! =?= -sum(a[k][i]*(k+1-i)!/k!/(k+1+1-i)! for i in [0, k+1-1])
    0 =?= sum(a[k][i]*(k+1-i)/(k+2-i) for i in [0, k])
    0 =?= sum(B[i]*C(k+1, i) / (k+1)*(k+1-i)/(k+2-i) for i in [0, k])
    0 =?= sum(B[i]*C(k, i)/(k+2-i) for i in [0, k])
    
    z == (e**z - 1)*sum(...)
    1 == e**z*sum() + (e**z-1)sum(B[i+1]*z**i/i!)
    1 == (e**z-1)*sum() + sum() + (e**z-1)sum(B[i+1]*z**i/i!)
    1 == sum() + (e**z-1)sum((B[i]+B[i+1])*z**i/i!)
    1 == sum() + sum(z**i/i!, i>0)sum((B[i]+B[i+1])*z**i/i!)
    1 == sum() + sum(z**i * sum(1/(i-j)! (B[j]+B[j+1])/j!, j<i), i > 0)
    1 == B[0]
    0 == B[i]/i! + sum(1/(i-j)! (B[j]+B[j+1])/j!), for 0 <=j < i
    -B[i] == sum((B[j]+B[j+1])C(i,j), j < i)
    -B[i] == sum((B[j]+B[j+1])C(i,j), j < i-1) + (B[i-1]+B[i])*i

    
s(k, n) = sum(c[k+1-i] * n**i for i in range(0, k+2))



    
'''

from fractions import Fraction
from factorial import factorials, binomials
debug = 0


if 0:
    import sympy
    from sympy.abc import n, i

    K = 5
    for k in range(0, K):
        s_k_n = sympy.Sum(i**k, (i, 0, n-1))
        print(s_k_n.doit())
    '''
    n
    n**2/2 - n/2
    n**3/3 - n**2/2 + n/6
    n**4/4 - n**3/2 + n**2/4
    n**5/5 - n**4/2 + n**3/3 - n/30
    '''





def Bernoulli_numbers(n):
    '''O(n**3*(logn)**2): B[i]/i! = -sum(B[k]/k!/(i+1-k)! for k in range(0, i))

assert len(Bernoulli_numbers(n)) == n or n < 0'''
    if n < 1:
        return []
    
    fs = factorials(n+1)
    ls = [Fraction(1)]  # B[i]/i!/(j+1-i)!
    j = 0
    for j in range(j+1, n):
        for i in range(j):
            ls[i] /= j+1-i
        ls.append(-sum(ls))

    ls = [x*fs[i]*fs[j+1-i] for i, x in enumerate(ls)]
    return ls

    

assert [] == Bernoulli_numbers(0)
assert [Fraction(1)] == Bernoulli_numbers(1)
assert [Fraction(1), Fraction(-1,2), Fraction(1,6), Fraction(0)] == Bernoulli_numbers(4)

# print(Bernoulli_numbers(20))

def evalf(coefficients, x):
    '''sum c[i]*x**(K-i) # big-endian'''
    s = 0
    for c in coefficients:
        s *= x
        s += c
    return s

def sum_powers(k, n):
    '''s(k, n) = sum(i**k for i in range(1,n))'''
    return sum(i**k for i in range(1,n))

def Bernoulli_numbers2coefficients(k):
    '''s(k, n) = sum(i**k for i in range(1,n)) = sum(a[k][i]*n**(k+1-i) for i in range(k+2))

a[k][j] = B[j]*C(k+1, j) / (k+1) for j in range(k+1)
a[k][k+1] = -sum(a[k][i] for i in range(k+1))
assert len(Bernoulli_numbers2coefficients(k)) == k+2 or k < 0

a[k][0]*(k+1-0)!/k! == 1
a[k][t]*(k+1-t)!/k! == -sum(a[k][i]*(k+1-i)!/k!  /(t+1-i)! for i in [0, t-1])
    for t in [1, k]

a[k][k+1] == s(k,1) - sum(a[k][i] for i in [0, k])

a[k][i] == B[i]*C()/(k+1)
'''
    if k < 0:
        return []
    
    L = k+2
    bes = Bernoulli_numbers(L-1)
    bis = binomials(k+1)
    fs = factorials(L)
    
    #assert len(bes) == len(bis) == L-1

    ls = [Fraction(1)] # a[k][i]*(k+1-i)!/k!/(t+1-i)! for t : 0->k ; finally == a[k][i]/k!
    for t in range(1, k+1):
        for i in range(t):
            ls[i] /= t+1-i
        ls.append(-sum(ls))

    c = fs[k]
    ls = [x*c for x in ls]
    ls.append(-sum(ls))

    assert len(ls) == L
    
    if debug:
        #print('radio', [x/be/bi*(k+1) for be, bi, x in zip(bes, bis, ls) if be])
        assert all(x*(k+1) == be*bi for be, bi, x in zip(bes, bis, ls))
:
        for x in range(1, L+3):
            r1, r2 = evalf(ls, x), sum_powers(k, x)
            #print(k, ls, x, r1, r2)
            assert evalf(ls, x) == sum_powers(k, x)
    return ls


    if k < 0:
        return []
    
    L = k+2
    bes = Bernoulli_numbers(L-1)
    bis = binomials(L-1)
    
    assert len(bes) == len(bis) == L-1

    ls = [be*bi / (k+1) for be, bi in zip(bes, bis)]
    ls.append(-sum(ls))

    for x in range(1, L+1):
        r1, r2 = evalf(ls, x), sum_powers(k, x)
        print(k, ls, x, r1, r2)
        assert evalf(ls, x) == sum_powers(k, x)
    return ls

for i in range(10):
    print('cs', Bernoulli_numbers2coefficients(i))
















