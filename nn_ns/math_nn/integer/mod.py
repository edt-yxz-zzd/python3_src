

__all__ = '''
    addmod
    mulmod
    all_powers_mod_N
    ginvmod
    invmod
    '''.split()

import functools
#[deprecated]:from fractions import gcd
#   ImportError: cannot import name 'gcd' from 'fractions' (/data/data/com.termux/files/usr/lib/python3.10/fractions.py)
from seed.math.gcd import gcd #, gcd_many
from ..math_func.math_func_of_float import sign


def addmod(a, b, N):
    '''(a+b) % N

    >>> addmod(3, 3, 5)
    1
    >>> addmod(3, 4, 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: integer division or modulo by zero
'''
    return (a+b) % N
def mulmod(a, b, N):
    '''(a*b) % N

    >>> mulmod(3, 3, 5)
    4
    >>> mulmod(3, 4, 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: integer division or modulo by zero
'''
    return (a*b) % N

def all_powers_mod_N(a, N):
    '''{a**i % N for i >= 1}

    >>> all_powers_mod_N(2, 10)
    [2, 4, 8, 6]
    >>> all_powers_mod_N(3, 0)
    Traceback (most recent call last):
        ...
    ValueError: N < 1
'''
    if N < 1:
        raise ValueError('N < 1')

    ls = [a]
    b = a
    for _ in range(N):
        b = (b * a) % N
        if b == a:
            break
        ls.append(b)
    else:
        raise logic-error

    assert all((len(ls) == len(s) and s == _all_powers_mod_N(a, N))
               for s in [set(ls)])
    return ls

def _all_powers_mod_N(a, N):
    assert N > 0

    b = a % N
    assert b >= 0
    powers = set()
    while b not in powers:
        powers.add(b)
        b = mulmod(a, b, N)
        pass

    assert powers
    assert min(powers) >= 0
    assert max(powers) < N
    return powers





def check_ginvmod_result(a_m, k1_k2_g):
    a, m = a_m
    k1, k2, g = k1_k2_g
    xyk_ls = [(a, m, k1, k2), (m, a, k2, k1)]

    assert k1*a + k2*m == g
    assert (m == a == 0) == (g == 0)

    if g != 0:
        assert g > 0
        assert a % g == 0
        assert m % g == 0

    for x, y, kx, ky in xyk_ls:
        if x == 0:
            assert g == abs(y)
            assert kx == 0

    if m != 0:
        assert 0 <= k1 < abs(m//g)

    for x, y, kx, ky in xyk_ls:
        if y != 0 and kx == 0:
            assert 0 < g == abs(y)
            assert ky == sign(y)
        if kx == 0:
            ky == sign(y)


    if g == abs(m):
        assert k1 == 0
        assert k2 == sign(m)

    if g == abs(a):
        assert (k2 == 0) or (k2 == sign(m) != 0)
        if k2 == 0:
            assert k1 == sign(a)
        else:
            assert k2 == sign(m)
            assert sign(a)
            assert a != 0
            if k1 == 0:
                assert abs(a) == g == abs(m)
            else:
                assert k1 > 0
                assert a == -g
                assert abs(m) == g * (1+k1)

    if m != 0:
        assert g > 0
        a_ = abs(a//g)
        m_ = abs(m//g)
        sm = sign(m)
        sa = sign(a)
        x = a_ // m_
        if m_ == 1:
            assert sm * k2 == 1
        else:
            assert m_ > 1
            assert -a_ * (1+sa)//2 + x+1 <= sm*k2 <= a_ * (1-sa)//2 - x

    return True


def test_ginvmod_1(a, m):
    k1, k2, g = r = ginvmod(a, m)
    assert ginvmod(a, -m) == (k1, -k2, g)

    _a_result = (-k1, k2, g) if m == 0 or k1 == 0 \
                else (-k1 + abs(m)//g, k2 + sign(m)*a//g, g)
    if ginvmod(-a, m) != _a_result:
        print(-a, m, _a_result)
    assert ginvmod(-a, m) == _a_result

    _a_k1, _a_k2, g = _a_result
    assert ginvmod(-a, -m) == (_a_k1, -_a_k2, g)
    return r


@functools.lru_cache(maxsize=2**12)
def ginvmod(a, m):
    """-> (k1,k2,g) : 0 <= k1*a + k2*m = g = abs(gcd(a, m))

k1*a + k2*m == g
m == a == 0 <=> g == 0
if g != 0: g > 0; g|a; g|m
if a == 0: g == abs(m); k1 == 0
if m == 0: g == abs(a); k2 == 0


if m != 0: 0 <= k1 < abs(m/g)



#######
if (a,m)->(k1,k2,g):
    (a,-m)->(k1,-k2,g);
    (-a,m)->(-k1,k2,g) if m == 0 or k1 == 0 else (-k1+abs(m)/g, k2+sign(m)*a/g, g)

if m != 0 and k1 == 0: 0 < g == abs(m), k2 == sign(m)
if a != 0 and k2 == 0: 0 < g == abs(a), k1 == sign(a) ----- a)
    proof:
    a != 0 -> g > 0 -> g|abs(a)
    k2 == 0 -> k1 * a == g -> sign(a)*k1 * abs(a) == g
    g > 0 -> abs(a) | g -> g == abs(a) -> k1 == sign(a)

if k1 == 0: k2 == sign(m)
if k2 == 0: k1 == sign(a)
    proof:
    k2 == 0 -> k1 * a == g; sign(a)*k1 * abs(a) == g >= 0
    if a == 0: k1 == 0 == sign(a)
    if a != 0: from a) -> k1 == sign(a)


g == abs(m) --> k1 == 0, k2 == sign(m)
    if m == 0: g == 0; a == 0; k1 == k2 == 0
    if m != 0:
        0 <= k1 < abs(m/g) = 1
        k1 == 0
        k2*m == g -> k2 = sm

g == abs(a) --xx--> k2 == 0
g == abs(a) -> (k2 == 0) or (k2 == sign(m) != 0)
    1) k2 == 0, k1 == sign(a), sa in {-1,0,1}
    2) k2 == sign(m) != 0:
        sign(a)*g * k1 + sign(m)*g*(1+k1) * sign(m) == g for k1 == 0, sa in {-1,1}
        -g * k1 + sign(m)*g*(1+k1) * sign(m) == g for k1 >= 0
        1) k1 == 0, a == sign(a)*g, m = sign(m)*g
        2) k1 > 0, a == -g, m == sign(m)*g*(1+k1)
    proof:
    if m == 0: g == abs(a); k2 == 0
    if m != 0:
        g > 0; a != 0
        0 <= k1 < abs(m/g) -> g < abs(m)
        if k1 == 0:
            abs(m) == g from a);
            g == abs(a) == abs(m)
            k1 == 0; k2 == sign(m) not zero!!!
            sign(a)*g * 0 + sign(m)*g * sign(m) == g
        if k1 > 0:
            let m'+k1 == abs(m/g); m' > 0
            g == abs(a) -> sign(a)*g*k1 + sign(m)*sign(k2)*(m'+k1)*g*abs(k2) == g
            ... -> sa*k1 + smk2 * (m'+k1) * k2' == 1
                   sa in {-1,1}; smk2 in {-1..1}; k2' >= 0
            ... -> smk2*m'*k2' + k1*(sa + smk2*k2') == 1
            ... -> if smk2 == -1:
                       k2' > 0;
                       -m'*k2' + (sa-k2')*k1 <= -m'*k2' + 0 < 0 < 1, error
            ... -> if smk2 == 0: sm != 0; k2 == 0
            ... -> if smk2 == 1:
                       k2' > 0;
                       m'*k2' + (sa+k2')*k1 >= m'*k2' + 0 >= 1
                       '==' requires:
                       1) sa == -1 and k2' == 1
                       2) m' == k2' == 1
                       sign(k2) == sign(m)
                       k1 ?
                       k2 = sign(k2) * k2' = sign(m) not zero !!!
                       m = sign(m) * g * (m'+k1) = sign(m)*g*(1+k1)
                       -g * k1 + sign(m)*g*(1+k1) * sign(m) == g


if k1 == sign(a): # useless
    abs(a) + k2*m == g
    if m == 0: g == abs(a); k2 == 0
    if m != 0:
        k1 == 0 or k1 == 1; a >= 0; g > 0
        if k1 == 0:
            a == 0; g == abs(m); k2 == sign(m)
        if k1 == 1:
            0 < g < abs(m); a > 0; 0 < g <= min(a, abs(m))
            if g == a: k2*m == 0; k2 == 0
            if g < a: k2*sign(m)*m' == 1 - a' < 0; a' > 1; m' > 1; k2 == -sign(m)*(a'-1)/m'




if m != 0:
    m' == 1 : sm*k2 = 1
    m' > 1  : -a'(1+sa)/2 + x+1 <= sm*k2 <= a'(1-sa)/2 - x

    proof:
    g > 0
    k2 = (g - k1*a)/m = g/m - (k1/(m/g))*a/g
    sign(m) * k2 = 1/abs(m/g) - (k1/abs(m/g))*a/g
    let m' = abs(m/g), a' = abs(a/g), sa = sign(a), sm = sign(m)
    sm*k2 = 1/m' - (k1/m')*sa*a'
    a' >= 0
    0 <= k1 < abs(m/g) = m'
    gcd(m', a') == 1
    m' == a' == 1 or m' != a'
    if g == abs(m):
        m' == 1; k1 == 0
        sm * k2 = 1
        k2 = sm
    if g < abs(m):
        a != 0; a' > 0
        0 < k1 < m'; abs(m) > 1;
        m' > 1; 1/m' < 1
        m' != a'
        if a < 0:
            sa = -1
            let x = a'//m' = abs(a)//abs(m)
            sm*k2 = 1/m' + (k1/m')*a' = ceil(a'*k1/m')
            sm*k2 >= ceil(a'/m') == x + 1 (when k1 == 1)
            sm*k2 <= ceil(a'*(m'-1)/m') = a' + ceil(-a'/m')
            ... == a' - floor(a'/m')
            ... == a' - x (when k1 == m'-1)

            if 0 < g < abs(m) and a < 0 and k2 == sm(x+1) and k1 == 1 \
                and gcd(m', a') == 1:
                -a'*g + sm*(x+1) * sm*m'*g == g > 0
                a' + 1 == m'(x+1)
                a = g - m'g(x+1) = g - abs(m)(x+1)
                k2 == sm(x+1)

            if 0 < g < abs(m) and a < 0 and k2 == sm*(a'-x) and k1 == m'-1 \
                and gcd(m', a') == 1:
                (m'-1)*(-a'*g) + sm*(a'-x) * sm*m'*g == g > 0
                -a'm' + a' + a'm' -m'x == 1
                a' == 1 + m'x
                a == (-a'*g) = -g - g*m'x = -g - abs(m)x
                k2 == sm*(a'-x) = sm*(1 + m'x-x) = sm + sm(m'-1)x

            x, m': x >= 0; m' > 1
            a'   : 0 <= m'x < a' < m'(x+1); gcd(m', a') == 1
            g    : g > 0
            sm   : sm in {-1, 1}
            sa = -1
            m = sm*m'g
            a = sa*a'g
            k1, k2 s.t. k1 * a + k2 * m == g and 0 <= k1 < abs(m)//g
            assert x+1 <= sm*k2 <= a'-x # total a'-2x


        if a > 0:
            sa = 1
            sm*k2 = 1/m' - (k1/m')*a' = -(a'k1/m' - 1/m') = - floor(a'k1/m')
            sm*k2 >= - floor(a'(m'-1)/m') = -a' - floor(-a'/m')
            ... == -a' + ceil(a'/m') == -a' + x + 1 (when k1 == m'-1)
            sm*k2 <= - floor(a'/m') = -x (when k1 == 1)


            if 0 < g < abs(m) and a > 0 and k2 == sm(-a'+x+1) and k1 == 1 \
                and gcd(m', a') == 1:
                a'*g + sm*(-a'+x+1) * sm*m'*g == g > 0
                a' + (-a'+x+1)m' == 1
                -a'+a'm' + 1 == m'(x+1)
                a'(m'-1) == m'x + m' - 1
                a' = (m'x+m'-1)/(m'-1)
                k2 == sm(-a'+x+1) = sm(m'x-x + m'-1 -m'x-m'+1)/(m'-1)
                ... = sm(-x)/(m'-1)

            if 0 < g < abs(m) and a > 0 and k2 == sm*(-x) and k1 == m'-1 \
                and gcd(m', a') == 1:
                (m'-1)*(a'*g) + sm*(-x) * sm*m'*g == g > 0
                a'(m'-1) - m'x == 1
                a' == (1 + m'x) / (m'-1)
                k2 == sm*(-x)

            x, m': x >= 0; m' > 1
            a'   : 0 <= m'x < a' < m'(x+1); gcd(m', a') == 1
            g    : g > 0
            sm   : sm in {-1, 1}
            sa = 1
            m = sm*m'g
            a = sa*a'g
            k1, k2 s.t. k1 * a + k2 * m == g and 0 <= k1 < abs(m)//g
            assert -a'+x+1 <= sm*k2 <= -x # total a'-2x

        sa = -1: x+1 <= sm*k2 <= a'-x
        sa = 1 : -a'+x+1 <= sm*k2 <= -x
        -a'(1+sa)/2 + x+1 <= sm*k2 <= a'(1-sa)/2 - x
    m' > 1: -a'(1+sa)/2 + x+1 <= sm*k2 <= a'(1-sa)/2 - x
    m' == 1: sm*k2 = 1
    if m' == 1:
        x = a'//m' = a'
        total = a' - 2x = -a' <= 0
        left = -a'(1+sa)/2 + x+1 = a'(1-sa)/2 + 1
        right = a'(1-sa)/2 - x = -a'(1+sa)/2
        nonsense



algorithm:
    r1 = A1*a + A2*m
    r2 = B1*a + B2*m
    r1 = q1*r2 + r3
    r3 = r1 - q1*r2 = (A1-q1*B1)*a + (A2-q1*B2)*m
    if r3 | r2 => r3 = gcd

    k1 * a/g + k2 * m/g = 1 if g != 0
    (k1+x*m/g)*a/g + (k2-x*a/g)*m/g = 1
    k1 mod m/g


    """

    A1,A2 = 1,0
    B1,B2 = 0,1
    r1,r2 = a,m



    while r2 != 0:
        assert (r1, r2) == (A1*a + A2*m, B1*a + B2*m)
        q1, r3 = divmod(r1, r2)
        #assert abs(r3) < abs(r2)
        #print('bit_length', r2.bit_length(), r3.bit_length())
        #when bit_length=100000, it is too slow
        A1, A2, B1, B2 = B1, B2, A1-q1*B1, A2-q1*B2
        r1, r2 = r2, r3
    assert (r1, r2) == (A1*a + A2*m, B1*a + B2*m)

    # sign(0)=0
    s = sign(r1)
    # g == gcd(a, m)
    g = s * r1
    # note: since sign(0)=0, even A1 != 0, k1 can be 0
    k1, k2 = s*A1, s*A2 # k1*a+k2*m == g;
    assert k1*a + k2*m == g == abs(gcd(a, m)) >= 0


    if m != 0:
        assert g > 0
        k1 %= abs(m) // g
        k2 = (g - k1*a) // m
        assert k1*a + k2*m == g > 0
        pass

    else:
        assert k1 == sign(a)
        assert k2 == 0
        assert (a == 0) ^ (g > 0)
        pass

    assert m == 0 or 0 <= k1 < abs(m) // g


    k1_k2_g = (k1, k2, g)
    a_m = a, m
    assert check_ginvmod_result(a_m, k1_k2_g)
    return k1_k2_g



def test_ginvmod():
    test_data = [\
        [(0,0), (0,0,0)],\

        [(3,0), (1,0,3)],\
        [(0,3), (0,1,3)],\
        [(-3,0), (-1,0,3)],\
        [(0,-3), (0,-1,3)],\

        [(3,3), (0,1,3)],\
        [(-3,3), (0,1,3)],\
        [(3,-3), (0,-1,3)],\
        [(-3,-3), (0,-1,3)],\

        [(3,6), (1,0,3)],\
        [(-3,6), (1,1,3)],\
        [(3,-6), (1,0,3)],\
        [(-3,-6), (1,-1,3)],\

        [(6,3), (0,1,3)],\
        [(-6,3), (0,1,3)],\
        [(6,-3), (0,-1,3)],\
        [(-6,-3), (0,-1,3)],\

        [(6,8), (3,-2,2)],\
        [(-6,8), (1,1,2)],\
        [(6,-8), (3,2,2)],\
        [(-6,-8), (1,-1,2)],\

        [(21,34), (13,-8,1)],\
        [(-21,34), (21,13,1)],\
        [(21,-34), (13,8,1)],\
        [(-21,-34), (21,-13,1)],\

        [(21,13), (5,-8,1)],\
        [(-21,13), (8,13,1)],\
        [(21,-13), (5,8,1)],\
        [(-21,-13), (8,-13,1)],\
        ]


    for am, ret in test_data:
        if test_ginvmod_1(*am) != ret:
            raise Exception('ginvmod{} != {}'.format(am, ret))

    for a in range(100):
        for m in range(100):
            test_ginvmod_1(a, m)
    return


def invmod(a, N):
    '''return r; s.t. 1 == (r * a) % abs(N);


invmod(a, N) == 1/a == a**(phi(N)-1) mod N == pow(a, phi(N)-1, N)


    >>> ls = [(1,2), (5,-6), (-12, 25), (-9, -7)]
    >>> [invmod(a, N) for a, N in ls]
    [1, 5, 2, 3]
    >>> invmod(2, 1)
    Traceback (most recent call last):
        ...
    ValueError: abs(N) < 2
    >>> invmod(2, 4)
    Traceback (most recent call last):
        ...
    ValueError: gcd(a, N) != 1
    >>>


'''
    #print(a, N);input('invmod begin:')

    if abs(N) < 2:
        raise ValueError('abs(N) < 2')

    inv, _, g = ginvmod(a, N)
    if g != 1:
        raise ValueError('gcd(a, N) != 1')

    assert 1 == (inv * a) % abs(N)
    #print(inv);input('invmod end:')
    return inv







if __name__ == '__main__':
    #test_ginvmod()

    import doctest
    doctest.testmod()







