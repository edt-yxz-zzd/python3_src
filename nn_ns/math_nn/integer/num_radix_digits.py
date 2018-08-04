
from math import floor

__all__ = ('num_radix_digits',)


        
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
    if not x >= 1:
        raise ValueError('not x >= 1')
    if not B >= 2:
        raise ValueError('not B >= 2')

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
