
'''
square_collision_factor
N is odd
if 0 < x < y <= (N-1)/2 and x*x == y*y mod N, then we can factor N
==>> y-x < y+x < N and (y-x)(y+x) == kN ==>> gcd(N, y-x)

let L = (N-1) / 2, assume N = pq, 1<p<q<N(N is not prime or prime square) and N is odd
then each x**2 has 4 roots(at least), and 2 in (0,L].
total non-coprime in (0, L] is A=(p+q-2)/2, if we failed then we cannot choose them.
each step we choose a x in (0, L], calc x*x
at step i, we has chosen i's x and all failed
now remain L - i, but should avoid A+i, fail possiblity = (L-A-2i)/(L-i)

p(fail k steps) = product((L-A-2i)/(L-i) for i in range(k))
max p ==>> min A ==>> min (p+q)
(p+q)**2 >= 4pq = 4N
min (p+q) = ceil_sqrt(4N)
replace (L-A) by M=L-ceil_sqrt(4N)
p(k) = product((M-2i)/(L-i) for i)
min k s.t. p(k) < 1/2


logN, min k
3 1
7 2
11 8
15 30
19 121
23 482

too slow!!!

'''

from math import ceil, sqrt
from fractions import Fraction


def calc_min_k(N, p_num=1, p_den=2):
    L = N//2
    A = ceil(sqrt(4*N))
    M = L-A
    p = Fraction(1)
    target = Fraction(p_num, p_den)

    i = 0
    while p > target:
        p *= M-2*i
        p /= L-i
        i += 1
    k = i
    return k

for e in range(3, 33, 4):
    r = calc_min_k(2**e+1)
    print(e, r)























