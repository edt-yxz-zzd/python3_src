#__all__:goto
r'''[[[
e ../../python3_src/seed/math/floor_ceil_tools/fc_div.py

seed.math.floor_ceil_tools.fc_div
py -m nn_ns.app.debug_cmd   seed.math.floor_ceil_tools.fc_div -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.floor_ceil_tools.fc_div:__doc__ -ht # -ff -df
#######

[[
move_from:
e ../../python3_src/seed/math/floor_ceil.py

]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.math.floor_ceil_tools.fc_div   @f
]]]'''#'''
__all__ = r'''
floor_ceil_div
    floor_div
    ceil_div
        ceil_div_
        floor_div_
offsetted_divmod
floor_lshift_div_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
___end_mark_of_excluded_global_names__0___ = ...


def floor_ceil_div(n, d, /):
    'n -> d -> (fq:=n//d, cq:=(n-1)//d+1)/(int,int) # [[d>0]->[fq*d <= n <= cq*d]][0 <= (cq-fq) <= 1]'
    fq, r = divmod(n, d)
    cq = fq +bool(r)
    return fq, cq


def ceil_div_(d, n, /):
    '[ceil_div_(d;n) == ceil(n/d) == ceil_div(n,d)]'
    return ceil_div(n, d)
def floor_div_(d, n, /):
    '[floor_div_(d;n) == n//d == floor_div(n,d)]'
    return floor_div(n, d)

def floor_div(n, d, /):
    r'''floor_div n d = n//d where d != 0

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

def ceil_div(n, d, /):
    r'''ceil_div n d = ceil(n/d) where d != 0

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
    return -((-n)//d)
    if d > 0:
        n -= 1
    else:
        n += 1
    return n//d + 1

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


def floor_lshift_div_(e, n, d, /):
    '[floor_lshift_div_(e, n, d) =[def]= floor(n/d *2**e) = floor_div(n<<e, d)]'
    return (n<<e)//d



__all__
from seed.math.floor_ceil_tools.fc_div import floor_ceil_div, floor_div, ceil_div, ceil_div_, floor_div_, offsetted_divmod
from seed.math.floor_ceil_tools.fc_div import floor_lshift_div_
from seed.math.floor_ceil_tools.fc_div import *
