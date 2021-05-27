r'''
py -m seed.math.floor_ceil
#'''

__all__ = '''
    floor_log2
    ceil_log2

    floor_div
    ceil_div

    offsetted_divmod
    '''.split()


def floor_div(n, d):
    '''floor_div n d = n//d where d != 0

floor_div(-n, -d) = floor_div(n, d)

example:
    >>> floor_div(4, 5)
    0
    >>> floor_div(5, 5)
    1
    >>> floor_div(6, 5)
    1

    >>> floor_div(-4, 5)
    -1
    >>> floor_div(-5, 5)
    -1
    >>> floor_div(-6, 5)
    -2

    >>> floor_div(4, -5)
    -1
    >>> floor_div(5, -5)
    -1
    >>> floor_div(6, -5)
    -2

    >>> floor_div(-4, -5)
    0
    >>> floor_div(-5, -5)
    1
    >>> floor_div(-6, -5)
    1
'''
    return n//d

def ceil_div(n, d):
    '''ceil_div n d = ceil(n/d) where d != 0

ceil_div(-n, -d) = ceil_div(n, d)

ceil_div n d
    | d > 0 = (n-1)//d +1
    | d < 0 = ceil_div (-n) (-d) = (-n-1)//(-d) +1 = (n+1)//d +1


example:
    >>> ceil_div(4,5)
    1
    >>> ceil_div(5,5)
    1
    >>> ceil_div(6,5)
    2

    >>> ceil_div(-4, 5)
    0
    >>> ceil_div(-5, 5)
    -1
    >>> ceil_div(-6, 5)
    -1

    >>> ceil_div(4, -5)
    0
    >>> ceil_div(5, -5)
    -1
    >>> ceil_div(6, -5)
    -1

    >>> ceil_div(-4, -5)
    1
    >>> ceil_div(-5, -5)
    1
    >>> ceil_div(-6, -5)
    2
'''
    if d > 0:
        n -= 1
    else:
        n += 1
    return n//d + 1

def ceil_log2(pint):
    '''ceil_log2(p) = ceil(log2(p)) where p > 0

ceil_log2(p)
    | p == 2**power = power = floor_log2(p)
                    = floor_log2(2*p-1)
    | otherwise     = floor_log2(p)+1
                    = floor_log2(2*p-1)
==>> ceil_log2(p) = floor_log2(2*p-1)

example:
    >>> ceil_log2(1)
    0
    >>> ceil_log2(2)
    1
    >>> ceil_log2(3)
    2
    >>> ceil_log2(4)
    2
    >>> ceil_log2(5)
    3
    >>> ceil_log2(6)
    3
    >>> ceil_log2(7)
    3
    >>> ceil_log2(8)
    3
    >>> ceil_log2(9)
    4
'''
    return floor_log2((pint<<1) -1)

def floor_log2(pint):
    '''floor_log2(p) = floor(log2(p)) where p > 0

assume:
    u >= 0
    p > 0
u < 2**u.bit_length()
2**(p.bit_length()-1) <= p < 2**p.bit_length()

==>> floor_log2(p) = p.bit_length()-1

example:
    >>> floor_log2(1)
    0
    >>> floor_log2(2)
    1
    >>> floor_log2(3)
    1
    >>> floor_log2(4)
    2
    >>> floor_log2(5)
    2
    >>> floor_log2(6)
    2
    >>> floor_log2(7)
    2
    >>> floor_log2(8)
    3
'''
    assert pint > 0
    return pint.bit_length()-1


def offsetted_divmod(original, n, d, /):
    r'''original -> n -> d -> (pq, pr)
    d >= 1
    n == pq*d+pr
    original <= pr < original+d

    t := pr - original
    n == pq*d+pr
        == pq*d+t+original
    n-original == pq*d + t
    0 <= t < d

example:
    >>> offsetted_divmod(3, 2, 1)
    (-1, 3)
    >>> offsetted_divmod(3, 1, 5)
    (-1, 6)
    >>> offsetted_divmod(3, 12, 5)
    (1, 7)
    >>> offsetted_divmod(-3, -1, 5)
    (0, -1)
    >>> offsetted_divmod(-3, -12, 5)
    (-2, -2)

    #'''
    if not d >= 1: raise ValueError
    (pq, t) = divmod(n-original, d)
    pr = t + original

    assert n == pq*d+pr
    assert original <= pr < original+d
    return (pq, pr)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

