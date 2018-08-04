


__all__ = '''
    floor_sqrt
    floor_power_inv
    floor_kth_root
    floor_div
    ceil_div
'''.split()

#from .prime2 import floor_sqrt




def floor_power_inv_check_input(n, inv_exp):
    if n < 0:
        raise ValueError('n < 0')
    if inv_exp < 1:
        raise ValueError('inv_exp < 1')
    if not isinstance(n, int) or not isinstance(inv_exp, int):
        raise ValueError('not isinstance(n, int) or not isinstance(inv_exp, int)')
    e = inv_exp
    L = n.bit_length()
    assert 2**L//2 <= n < 2**L

    # bit_length_begin == floor((L-1)/e) + 1
    if n == 0:
        bit_length_begin = 0
    else:
        bit_length_begin = (L-1)//e+1 


    end = 2**bit_length_begin
    begin = end>>1
    assert begin**e <= n < end**e
    return e, L, bit_length_begin, begin, end



def floor_power_inv_by_binary_search(n, inv_exp, begin=0, end=float('inf')):
    '''floor_power_inv(n, e) = floor(pow(n, 1/e))'''

    e, L, bit_length_begin, _begin, _end = floor_power_inv_check_input(n, inv_exp)
    if begin < _begin:
        begin = _begin
    if end > _end:
        end = _end

    if not begin**e <= n < end**e:
        raise ValueError('not begin**e <= n < end**e')

    assert begin < end
    while end-begin > 1:
        middle = (begin+end)//2
        assert begin < middle < end
        if middle**e > n:
            end = middle
        else:
            begin = middle
    root = begin
    assert root**e <= n < (root+1)**e
    return root


def floor_power_inv_by_Newton(n, inv_exp):
    '''floor_power_inv(n, e) = floor(pow(n, 1/e))

root = floor_power_inv(n, e)
assert root**e <= n < (root+1)**e

example:
    >>> floor_power_inv(4, 2)
    2
    >>> floor_power_inv(32, 3)
    3
    >>> floor_power_inv(0, 1)
    0
    >>> floor_power_inv(-1, 1)
    Traceback (most recent call last):
       ...
    ValueError: n < 0
    >>> floor_power_inv(1, 0)
    Traceback (most recent call last):
       ...
    ValueError: inv_exp < 1
    


-------------------
x = n**(1/e)
f(x) = x**e - n
df(x)/dx = e*x**(e-1)
x' = x - f(x)dx/df(x) = x - (x**e - n)/e/x**(e-1)
= (e*x-x+n/x**(e-1))/e

let r be real root, n = r**e
dx0 = r/t
x0 = r+ dx0 = r(1+t)/t = r*u # u = (1+t)/t
(x0-x1)/(x0-r) = (dx0-dx1)/dx0 = f(x)/df(x) = (x**e - n)/e/x**(e-1)/dx
= ((r*u)**e - r**e)/e/(r*u)**(e-1)/(r/t)
= (u**e-1)t/e/u**(e-1)
= ((t+1)**e-t**e)/e/(t+1)**(e-1)

(x1-r)/(x0-r) = 1-(x0-x1)/(x0-r)
= (e*(t+1)**(e-1) - (t+1)**e+t**e)/e/(t+1)**(e-1)
= ((e-t-1)*(t+1)**(e-1) +t**e)/e/(t+1)**(e-1)

if dx0 = r, ==>> x0 = 2r, t=1
==>> (x1-r)/(x0-r) = ((e-2)*2**(e-1)+1)/e/2**(e-1)
~= -->> (e-2)/e -->> 1 if e is large enough
slow!!!!

let (x1-r)/(x0-r) < 1/2, that is (x0-x1)/(x0-r) > 1/2
(u**e-1)t/e/u**(e-1) > 1/2
(u**e-1)2t > e*u**(e-1)
2t*u**e - e*u**(e-1) > 2t
u**e(2t-e/u) > 2t
1 - e/u/2/t > u**-e
1-u**-e > e/2/u/t = e/2/(1+t)
u**-e = (t/(1+t))**e = 1/(1+1/t)**e
let t = e, u**-e -->> 1/E if e larger enough

if t=e, 1-1/E > 1 - u**-e >= 1-1/2 = 1/2 > e/2/(1+e)
so "t >= e", that is r <= x0 <= (1+1/e)r, ==>> (x1-r)/(x0-r) < 1/2
a good initial value is important.


# assume bit_length([0,1,2]) == [0,1,2];  2**-1 == 2**0//2 == 0
# assume a//b = floor(a/b) not python '//' which means truntozero(a/b)
L = bit_length(n)
if n > 0
2**(L-1) <= n < 2**L
2**((L-1)/e) <= r = n**(1/e) < 2**(L/e)
2**((L-1)//e*e) <= n
2**((L-1)//e*e + e) >= 2**(L-1 - (e-1) + e) = 2**L > n
let base = 2**((L-1)//e), base <= r < 2*base
(L-1)//e+1 == bit_length(base) == bit_length(r)

r//e*e <= r < e(r//e+1)
bit_length(r//e)+bit_length(e)-1or0 <= bit_length(r)
    <= bit_length(r//e+1)+bit_length(e)-1or0
    if bit_length(r//e+1) == bit_length(r//e) + 1, then later 1or0 == 1
    else bit_length(r//e+1) == bit_length(r//e)
    == bit_length(r//e)+bit_length(e)-1or0
bit_length(r//e) = bit_length(r) - bit_length(e)+1or0
let u = bit_length(r) - bit_length(e)+0 - 1 < bit_length(r//e)
2**u <= r/e
now r <= x0 <= r+2**u is allowed
# we have to switch to another method to get the first log(e) bits of r


if u <= 0, bit_length(r) <= bit_length(e) + 1
if r < 2*2**bit_length(e), u <= 0

let r//2**u = R, R*2**u <= r < (R+1)*2**u
(R*2**u)**e <= r**e = n < ((R+1)*2**u)**e
R**e <= n / 2**(u*e) < (R+1)**e
R = floor_power_inv(n/2**(u*e)) # if u*e > 0


# here, we get a proper initial value
x0 = (R+1)*2**u



see also: sympy.core.power.integer_nthroot
'''
    e, L, bit_length_begin, begin, end = floor_power_inv_check_input(n, inv_exp)

    bit_length_root = bit_length_begin
    u = bit_length_root - e.bit_length()+0 - 1
    if u <= 0:
        root = floor_power_inv_by_binary_search(n, e, begin, end)
        return root

    two_pow_u = 2**u
    R = floor_power_inv_by_binary_search(n//two_pow_u**e, e)
    root_low = R*two_pow_u
    root_high = (R+1)*two_pow_u
    assert root_low**e <= n < root_high**e
    assert two_pow_u <= root_low//e
    initial_x0 = root_high



    assert initial_x0 > 0
    x1, x0 = initial_x0, initial_x0 * 2
    while x1 < x0:
        old_change = x0 - x1
        
        x0 = x1
        x1 = ((e-1)*x0 + n//x0**(e-1))//e

        new_change = x0 - x1
##        if not new_change <= old_change//2:
##            print('x0, x1', x0, x1)
##            print('old_change, new_change', old_change, new_change)
##            print('n, e', n, e)
        
        # root = initial_x0 - sum(new_changes[:-1])
        # new_change[-1] <= 0 < new_changes[-2] < ... < new_change[0]
        # new_change[i] <= new_change[i-1]//2
        # stop before log2(x0-root) steps
        assert new_change <= old_change//2 or x1**e < n
##        if new_change <= 0: stop
##        if x1**e < n: next round will stop

    root = x0
    assert root**e <= n < (root+1)**e
    # later check
    assert root_low <= root < root_high
    assert root <= x0 <= root+2**u
    assert u < (root//e).bit_length()
    assert two_pow_u <= root//e
    return root

def floor_sqrt(n):
    '''floor_sqrt(n) = floor(sqrt(n))

root = floor_sqrt(n)
assert root**2 <= n < (root+1)**2

example:
    >>> floor_sqrt(0)
    0
    >>> floor_sqrt(7)
    2
    >>> floor_sqrt(-1)
    Traceback (most recent call last):
       ...
    ValueError: n < 0
    
'''
    root = floor_power_inv_by_Newton(n, 2)
    assert root**2 <= n < (root+1)**2
    return root
floor_power_inv = floor_power_inv_by_Newton



def floor_kth_root(n, k, time=1):
    '''floor_kth_root(n, k, time) = floor(time * n**(1/k))

example:
    >>> sqrt_2 = floor_kth_root(2, 2, 2**10) # set binary precision to 10
    >>> bin(sqrt_2)[2:]
    '10110101000'
    >>> float(sqrt_2) / 2**10
    1.4140625
    >>> floor_kth_root(2, 2, 10**5) # set decimal precision to 5
    141421

-------------
time * n**(1/k) = (n * time**k) ** (1/k)

-------------
see also : floor_power_inv

'''

    n *= time**k
    return floor_power_inv(n, k)


def sign(x):
    if x > 0: return 1
    if not x: return 0
    if x < 0: return -1
    raise TypeError

def is_floor(q, n, d):
    if d > 0:
        return q*d <= n < (q+1)*d
    if d < 0:
        return is_floor(q, -n, -d)
    raise ValueError
def is_ceil(q, n, d):
    if d > 0:
        return (q-1)*d < n <= q*d
    if d < 0:
        return is_ceil(q, -n, -d)
    raise ValueError
def ceil_div(n, d):
    '''ceil_div(n, d) = ceil(n/d)

example:
    >>> ceil_div(3, 2)
    2
    >>> ceil_div(3, -2)
    -1
    >>> ceil_div(-3, 2)
    -1
    >>> ceil_div(-3, -2)
    2
    >>> ceil_div(2, 2)
    1
    >>> ceil_div(-2, -2)
    1
'''
    q = (n+d - sign(d)) // d
    assert is_ceil(q, n, d)
    return q

def floor_div(n, d):
    '''floor_div(n, d) = floor(n/d)

example:
    >>> floor_div(3, 2)
    1
    >>> floor_div(3, -2)
    -2
    >>> floor_div(-3, 2)
    -2
    >>> floor_div(-3, -2)
    1
    >>> floor_div(2, 2)
    1
    >>> floor_div(-2, -2)
    1
'''
    q = n // d
    assert is_floor(q, n, d)
    return q


def _test_floor_power_inv(n=10000, inv_exp=6):
    print('hi test_floor_power_inv')
    for e in range(1, inv_exp):
        for i in range(n):
            r1 = floor_power_inv_by_binary_search(i, e)
            r2 = floor_power_inv_by_Newton(i, e)
            assert r1 == r2
            assert r1**e <= i < (r1+1)**e


def _test_all():
    _test_floor_power_inv(10000, 17)




if __name__ == "__main__":
    import doctest
    doctest.testmod()
    _test_all()






