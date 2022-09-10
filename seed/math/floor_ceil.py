r'''
view others/数学/divmod加速.txt

py -m seed.math.floor_ceil
from seed.math.floor_ceil import floor_div, ceil_div
from seed.math.floor_ceil import floor_log2, ceil_log2
from seed.math.floor_ceil import floor_log2_kth_root_, ceil_log2_kth_root_
from seed.math.floor_ceil import floor_log2_sqrt, ceil_log2_sqrt
from seed.math.floor_ceil import floor_log_, ceil_log_

from seed.math.floor_ceil import floor_sqrt, ceil_sqrt
#'''

__all__ = '''
    floor_log2
    ceil_log2
    floor_log2_kth_root_
    ceil_log2_kth_root_
    floor_log2_sqrt
    ceil_log2_sqrt
    floor_log_
    ceil_log_

    floor_sqrt
    ceil_sqrt

    floor_div
    ceil_div

    offsetted_divmod
    '''.split()


from seed.math.max_power_of_base_as_factor_of_ import factor_pint_out_2_powers
#from seed.math.max_power_of_base_as_factor_of_ import count_num_low_0bits_of_pint, count_num_low_1bits_of_uint


def floor_div(n, d, /):
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

def ceil_div(n, d, /):
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

def ceil_log2(pint, /):
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
    assert pint > 0
    if 0:
        return floor_log2((pint<<1) -1)
    if 0:
        if pint == 1:
            return 0
        return 1+floor_log2(pint-1)
    if 1:
        e = floor_log2(pint)
        if not pint == (1<<e):
            e += 1
        return e
    raise logic-err


def floor_log2(pint, /):
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

def floor_log2_kth_root_(k, n, /):
    r'''[[[
    [k >= 1]
    [n >= 1]
    [w**k == n]
    [result := floor_log2(w)]
    [2**result <= w < 2**(result+1)]
    [2**(k*result) <= w**k < 2**(k*(result+1))]
    [(2**k)**result <= n < (2**k)**(result+1)]
    [result == floor_log_(2**k, n) == floor_log2(n)//k]

    #]]]'''
    assert k >= 1
    assert n >= 1
    e = floor_log2(n)//k
    assert (1<<(k*e)) <= n < (1<<(k*(e+1)))
    return e
def ceil_log2_kth_root_(k, n, /):
    r'''[[[
    [k >= 1]
    [n >= 1]
    [w**k == n]
    [result := ceil_log2(w)]
    [2**(result-1) < w <= 2**result]
    [2**(k*(result-1)) < w**k <= 2**(k*result)]
    [(2**k)**(result-1) < n <= (2**k)**result]
    [result == ceil_log_(2**k, n) == ceil_div(ceil_log2(n), k)]
    [result == if n==1 then 0 else 1+floor_log2_kth_root_(k,n-1)]

    #]]]'''
    assert k >= 1
    assert n >= 1
    if 0:
        e = 0 if n == 1 else 1+floor_log2_kth_root_(k,n-1)
    else:
        e = ceil_div(ceil_log2(n), k)
    assert n==1 if e==0 else (1<<(k*(e-1))) < n <= (1<<(k*e))
    return e
def floor_log2_sqrt(n, /):
    return floor_log2_kth_root_(2, n)
def ceil_log2_sqrt(n, /):
    return ceil_log2_kth_root_(2, n)



def ceil_sqrt(n, /):
    fsqrtN = floor_sqrt(n)
    csqrtN = fsqrtN if (n==fsqrtN**2) else 1+fsqrtN
    assert csqrtN==0 if n==0 else (csqrtN-1)**2 < n <= csqrtN**2
    return csqrtN
def floor_sqrt(n, /):
    r'''[[[
    [floor_sqrt(n) =[def]= floor(sqrt(n))]

    [n>=0]
[n>=1]:
    #floor_sqrt不使用 牛顿迭代，但感觉本质一样
    [(q,r) := divmod(n, 2**(2*e))]
    [fsqrtN := floor_sqrt(n)]
    [fsqrtQ := floor_sqrt(q)]
    #由(e,q,r,fsqrtQ)求fsqrtN
    [fsqrtQ**2 <= q < (fsqrtQ+1)**2]
    [n == q*2**(2*e) + r >= q*2**(2*e) >= (fsqrtQ*2**e)**2]
    [n == q*2**(2*e) + r < (q+1)*2**(2*e) <= ((1+fsqrtQ)*2**e)**2]
    [(fsqrtQ*2**e) <= fsqrtN < ((1+fsqrtQ)*2**e)]
    [fsqrtQ == fsqrtN//2**e]
    [dd := fsqrtN - (fsqrtQ*2**e)]
    [0 <= dd < 2**e]
    [dd == fsqrtN%2**e]
    [fsqrtN == (fsqrtQ*2**e+dd)]
    #由(e,q,r,fKrtQ)先求dd再求fKrtN

    [D := n -(fsqrtQ*2**e)**2]
    [D == n -(fsqrtQ*2**e)**2 == (q*2**(2*e) + r) -(fsqrtQ*2**e)**2 == ((q-fsqrtQ**2)*2**(2*e) + r)]

    [n >= fsqrtN**2 == (fsqrtQ*2**e+dd)**2]
    [D == n -(fsqrtQ*2**e)**2 >= (2*fsqrtQ*2**e+dd)*dd == (2*fsqrtQ+dd/2**e)*2**e*dd]
    [floor(2*fsqrtQ+dd/2**e) == (2*fsqrtQ)]

    [n < (1+fsqrtN)**2 == (fsqrtQ*2**e+dd+1)**2]
    [D == n -(fsqrtQ*2**e)**2 < (2*fsqrtQ*2**e+(dd+1))*(dd+1) == (2*fsqrtQ+(dd+1)/2**e)*2**e*(dd+1)]
    [ceil(2*fsqrtQ+(dd+1)/2**e) == (2*fsqrtQ+1)]

    [(2*fsqrtQ)*2**e*dd <= D < (2*fsqrtQ+1)*2**e*(dd+1)]
    [dd <= D/((2*fsqrtQ)*2**e)]
    [dd+1 > D/((2*fsqrtQ+1)*2**e)]
    [-1 +D/2**e /(2*fsqrtQ+1) < dd <= D/2**e /(2*fsqrtQ)]
    [D//2**e //(2*fsqrtQ+1) <= dd <= D//2**e //(2*fsqrtQ)]

    [0 <= D//2**e <= (2*fsqrtQ+1)**2-2]:
        #view others/数学/divmod加速.txt
        !![[d>=2] -> [-(d-1) <= n <= d**2-2] -> [0 <= n//(d-1) - n//d <= 1]]
        [-1 +D//2**e //(2*fsqrtQ) <= dd <= D//2**e //(2*fsqrtQ)]

        [(2*fsqrtQ+1)**2-2
        >= D//2**e
        == ((q-fsqrtQ**2)*2**(2*e) + r)//2**e
        == ((q-fsqrtQ**2)*2**e + r//2**e)
        ]
        [(q-fsqrtQ**2) < (fsqrtQ+1)**2 -fsqrtQ**2 == 2*fsqrtQ+1]
        [(q-fsqrtQ**2) <= (2*fsqrtQ)]
        #充分条件:
        [(2*fsqrtQ+1)**2-2 >= D//2**e]
        <<== [(2*fsqrtQ+1)**2-2 >= ((2*fsqrtQ)*2**e + r//2**e)]
        <<== [(2*fsqrtQ+1)**2-2 >= ((2*fsqrtQ)*2**e + 2**e-1)]
        <<== [(2*fsqrtQ+1)**2 >= (1 + (2*fsqrtQ+1)*2**e)]
        <<== [(2*fsqrtQ+1) >= (1/(2*fsqrtQ+1) + 2**e)]
        <<== [(2*fsqrtQ+1) >= (1 + 2**e)]
        <<== [fsqrtQ >= (2**(e-1))]
        <<== [floor_log2(q)//2 == floor_log2_sqrt(q) == floor_log2(sqrt(q)) == floor_log2(fsqrtQ) >= (e-1)]
        <<== [floor_log2(q) >= 2*(e-1)]
        !![(q,r) := divmod(n, 2**(2*e))]
        !![q >= 1] # ==>> [2*e <= floor_log2(n)]
        <<== [2*e <= floor_log2(n) == floor_log2(q)+2*e >= 2*(e-1)+2*e == 4*e-2]
        <<== [floor_log2(n) >= 4*e-2][e >= 1]
        <<== [1 <= e <= (floor_log2(n)+2)//4][n>=4]
            # 2**e 占 约1/4
            # 2**(2*e) 占 约1/2
            # q 占 约1/2
            # 由q到n(由fsqrtQ到fsqrtN)，比特数大约翻倍
    [1 <= e <= (floor_log2(n)+2)//4][n>=4]:
        [0 <= D//2**e <= (2*fsqrtQ+1)**2-2]
        #dd只有2个可能的取值
        [-1 +D//2**e //(2*fsqrtQ) <= dd <= D//2**e //(2*fsqrtQ)]
        [fsqrtN == (fsqrtQ*2**e+dd)]
        #通过dd求fsqrtN
        [upper_dd := D//2**e //(2*fsqrtQ)]
        [upper_dd ==  ((q-fsqrtQ**2)*2**e + r//2**e)//(2*fsqrtQ)]

        [n >= 2**(4*e-2) == 4**(2*e-1)]
        [[1 <= (floor_log2(n)+2)//4] -> [n>=4]]
        [[2 <= (floor_log2(n)+2)//4] -> [n>=64]]
        [[3 <= (floor_log2(n)+2)//4] -> [n>=1024]]





    #]]]'''
    assert n >= 0
    if 0:
        if n < 4:
            fsqrtN = 0 if n==0 else 1
    while 1:
        if n == 0:
            fsqrtN = 0
            break

        flbN = floor_log2(n)
        if 0 == flbN&1 and n == (1<<flbN):
            fsqrtN = (1<<(flbN>>1))
            break

        ls = [(n, flbN)]
        while 1:
            (n, flbN) = ls[-1]
            #if n < 4:break
            if flbN == 1:break
            e = (flbN+2)//4
            _2e = e << 1
            q = n >> _2e
            flbQ = flbN -_2e
            ls.append((q, flbQ))

        (n, flbN) = ls.pop()
        fsqrtN = 1
        while ls:
            (q, flbQ) = (n, flbN)
            fsqrtQ = fsqrtN
            (n, flbN) = ls.pop()
            _2e = flbN -flbQ
            e = _2e >> 1
            #r = n & ((1<<_2e)-1)
            #####
            if 0:
                # [D == n -(fsqrtQ*2**e)**2 == (q*2**(2*e) + r) -(fsqrtQ*2**e)**2 == ((q-fsqrtQ**2)*2**(2*e) + r)]
                D = n -((fsqrtQ**2) << _2e)
                # [upper_dd := D//2**e //(2*fsqrtQ)]
                upper_dd = (D >> (e+1)) //fsqrtQ
            else:
                D_e1 = (n>>(e+1)) -((fsqrtQ**2) << (e-1))
                upper_dd = D_e1//fsqrtQ

            # [fsqrtN == (fsqrtQ*2**e+dd)]
            upper_fsqrtN = (fsqrtQ<<e)+upper_dd
            if n < upper_fsqrtN**2:
                fsqrtN = upper_fsqrtN -1
            else:
                fsqrtN = upper_fsqrtN
            fsqrtN
        #end-while
        fsqrtN
        break
    #end-while-main
    assert fsqrtN**2 <= n < (1+fsqrtN)**2
    return fsqrtN

def _t1__floor_sqrt():
    for n in range(10_0001):
        floor_sqrt(n)
def _t2__floor_sqrt():
    for i in range(1001):
        floor_sqrt(2**i)
    for i in range(1001):
        floor_sqrt(5**i)
    for i in range(10_0000, 10_0101):
        floor_sqrt(7**i)
if __name__ == "__main__":
    _t2__floor_sqrt()
    _t1__floor_sqrt()


def floor_kth_root_(k, n, /):
    r'''[[[
    [kth_root_(k,n) =[def]= n**(1/k)]
    [floor_kth_root_(k,n) =[def]= floor(kth_root_(k,n))]
    [floor_sqrt === floor_kth_root_<2>]

    [k>=1][n>=0]
[k>=2][n>=1]:
    [(q,r) := divmod(n, 2**(k*e))]
    [fKrtN := floor_kth_root_(k,n)]
    [fKrtQ := floor_kth_root_(k,q)]
    #由(e,q,r,fKrtQ)求fKrtN
    [fKrtQ**k <= q < (fKrtQ+1)**k]
    [n == q*2**(k*e) + r >= q*2**(k*e) >= (fKrtQ*2**e)**k]
    [n == q*2**(k*e) + r < (q+1)*2**(k*e) <= ((1+fKrtQ)*2**e)**k]
    [(fKrtQ*2**e) <= fKrtN < ((1+fKrtQ)*2**e)]
    [fKrtQ == fKrtN//2**e]
    [dd := fKrtN - (fKrtQ*2**e)]
    [0 <= dd < 2**e]
    [dd == fKrtN%2**e]
    [fKrtN == (fKrtQ*2**e+dd)]
    #由(e,q,r,fKrtQ)先求dd再求fKrtN

    [D := n -(fKrtQ*2**e)**k]
    [D == n -(fKrtQ*2**e)**k == (q*2**(k*e) + r) -(fKrtQ*2**e)**k == ((q-fKrtQ**k)*2**(k*e) + r)]

    [n >= fKrtN**k == (fKrtQ*2**e+dd)**k]
    [D == n -(fKrtQ*2**e)**k
    >= (k*(fKrtQ*2**e)**(k-1)*dd +sum{choose_(k,i) *(fKrtQ*2**e)**i *dd**(k-i) | [i <- [0..=k-2]]})
    == (k*(fKrtQ*2**e)**(k-1) +sum{choose_(k,i) *(fKrtQ*2**e)**i *dd**(k-1-i) | [i <- [0..=k-2]]}) *dd
    == (k*fKrtQ**(k-1) +sum{choose_(k,i) *fKrtQ**i *(dd/2**e)**(k-1-i) | [i <- [0..=k-2]]}) *(2**e)**(k-1) *dd
    ]
    !![0 <= dd < 2**e]]
    TODO:
    [floor(2*fKrtQ+dd/2**e) == (2*fKrtQ)]

    [n < (1+fKrtN)**k == (fKrtQ*2**e+dd+1)**k]
    [D == n -(fKrtQ*2**e)**k < (2*fKrtQ*2**e+(dd+1))*(dd+1) == (2*fKrtQ+(dd+1)/2**e)*2**e*(dd+1)]
    [ceil(2*fKrtQ+(dd+1)/2**e) == (2*fKrtQ+1)]

    [(2*fKrtQ)*2**e*dd <= D < (2*fKrtQ+1)*2**e*(dd+1)]
    [dd <= D/((2*fKrtQ)*2**e)]
    [dd+1 > D/((2*fKrtQ+1)*2**e)]
    [-1 +D/2**e /(2*fKrtQ+1) < dd <= D/2**e /(2*fKrtQ)]
    [D//2**e //(2*fKrtQ+1) <= dd <= D//2**e //(2*fKrtQ)]

    [0 <= D//2**e <= (2*fKrtQ+1)**k-2]:
        #view others/数学/divmod加速.txt
        !![[d>=2] -> [-(d-1) <= n <= d**2-2] -> [0 <= n//(d-1) - n//d <= 1]]
        [-1 +D//2**e //(2*fKrtQ) <= dd <= D//2**e //(2*fKrtQ)]

        [(2*fKrtQ+1)**k-2
        >= D//2**e
        == ((q-fKrtQ**k)*2**(k*e) + r)//2**e
        == ((q-fKrtQ**k)*2**e + r//2**e)
        ]
        [(q-fKrtQ**k) < (fKrtQ+1)**k -fKrtQ**k == 2*fKrtQ+1]
        [(q-fKrtQ**k) <= (2*fKrtQ)]
        #充分条件:
        [(2*fKrtQ+1)**k-2 >= D//2**e]
        <<== [(2*fKrtQ+1)**k-2 >= ((2*fKrtQ)*2**e + r//2**e)]
        <<== [(2*fKrtQ+1)**k-2 >= ((2*fKrtQ)*2**e + 2**e-1)]
        <<== [(2*fKrtQ+1)**k >= (1 + (2*fKrtQ+1)*2**e)]
        <<== [(2*fKrtQ+1) >= (1/(2*fKrtQ+1) + 2**e)]
        <<== [(2*fKrtQ+1) >= (1 + 2**e)]
        <<== [fKrtQ >= (2**(e-1))]
        <<== [floor_log2(q)//2 == floor_log2_sqrt(q) == floor_log2(sqrt(q)) == floor_log2(fKrtQ) >= (e-1)]
        <<== [floor_log2(q) >= 2*(e-1)]
        !![(q,r) := divmod(n, 2**(k*e))]
        !![q >= 1] # ==>> [k*e <= floor_log2(n)]
        <<== [k*e <= floor_log2(n) == floor_log2(q)+k*e >= 2*(e-1)+k*e == 4*e-2]
        <<== [floor_log2(n) >= 4*e-2][e >= 1]
        <<== [1 <= e <= (floor_log2(n)+2)//4][n>=4]
            # 2**e 占 约1/4
            # 2**(k*e) 占 约1/2
            # q 占 约1/2
            # 由q到n(由fKrtQ到fKrtN)，比特数大约翻倍
    [1 <= e <= (floor_log2(n)+2)//4][n>=4]:
        [0 <= D//2**e <= (2*fKrtQ+1)**k-2]
        #dd只有2个可能的取值
        [-1 +D//2**e //(2*fKrtQ) <= dd <= D//2**e //(2*fKrtQ)]
        [fKrtN == (fKrtQ*2**e+dd)]
        #通过dd求fKrtN
        [upper_dd := D//2**e //(2*fKrtQ)]
        [upper_dd ==  ((q-fKrtQ**k)*2**e + r//2**e)//(2*fKrtQ)]

        [n >= 2**(4*e-2) == 4**(k*e-1)]
        [[1 <= (floor_log2(n)+2)//4] -> [n>=4]]
        [[2 <= (floor_log2(n)+2)//4] -> [n>=64]]
        [[3 <= (floor_log2(n)+2)//4] -> [n>=1024]]





    #]]]'''
    assert k >= 1
    assert n >= 0
    if k == 1 or n < 2:
        return n

floor_lshift_kth_root_(e, k, n)
floor_log2_div
floor_log2_pow
def floor_lshift_sqrt_(k, n, /):
    r'''[[[
    [floor_lshift_sqrt_(k,n) =[def]= floor(2**k * sqrt(n))]

    #]]]'''
    assert n >= 0
    assert k >= 0
    return floor_sqrt(n<<(2*k))
def floor_lshift_log2_(k, n, /):
    r'''[[[
    [floor_lshift_log2_(k,n) =[def]= floor(2**k * log2(n))]
    [floor_lshift_log2_(k,n) == floor_log2(n**2**k)]
        #一次平方，才得1bit，太慢！
    [flbN := floor_log2(n)]
    [clbN := ceil_log2(n)]
    [2**flbN <= n <= 2**clbN]
    [0 <= clbN-flbN <= 1]
    [2**(flbN*2**k) <= n**2**k <= 2**(clbN*2**k)]
    [flbNk := floor_log2(n**2**k)]
    [clbNk := ceil_log2(n**2**k)]
    [2**flbNk <= n**2**k <= 2**clbNk]
    [0 <= clbNk-flbNk <= 1]
    [2**(flbN*2**k) <= 2**flbNk <= n**2**k <= 2**clbNk <= 2**(clbN*2**k)]
    [2**flbN <= 2**(flbNk/2**k) <= n <= 2**(clbNk/2**k) <= 2**clbN]
    [flbN == floor_div(flbNk, 2**k)]
    [clbN == ceil_div(clbNk, 2**k)]

    [flbNk
    == max{i <- [flbN*2**k..=clbN*2**k] | [2**i <= n**2**k]}
    == max{i <- [flbN*2**k..=clbN*2**k] | [floor_kth_root_(2**k, 2**i) <= n]}
    ]
        search (flbNk,clbNk) between [flbN*2**k..=clbN*2**k]
        需要求 kth_root_(2**k, 2**i) for i <- [flbN*2**k..=clbN*2**k]
        [kth_root_(2**k, 2**i)
        == kth_root_(2**k, 2**((i//2**k)*2**k + (i%2**k)))
        == kth_root_(2**k, 2**((i//2**k)*2**k) * 2**(i%2**k))
        == kth_root_(2**k, 2**((i//2**k)*2**k)) * kth_root_(2**k, 2**(i%2**k))
        == 2**(i//2**k) * kth_root_(2**k, 2**(i%2**k))
        ]
        [floor_kth_root_(2**k, 2**i)
        == floor(2**(i//2**k) * kth_root_(2**k, 2**(i%2**k)))
        == floor_lshift_kth_root_((i//2**k), 2**k, 2**(i%2**k))
        ]
        另:[floor_kth_root_<2**k> === (floor_sqrt**k)]

        !![flbN*2**k <= i <= clbN*2**k]
        [flbN <= i//2**k <= clbN]
            # kth_root_精度要求小数点后clbN比特
        [kth_root_(2**k, 2**(i%2**k)) == (floor_sqrt**k)(2**(i%2**k))]
            #但是 (2**(i%2**k))有O(2**k)bit，还是 太大！


    [(e, odd) := factor_pint_out_2_powers(n)]
    [n==(odd*2**e)]
    [e>=0]
    [odd%2==1]
    [floor_lshift_log2_(k,n)
    == floor_log2(n**2**k)
    == floor_log2((odd*2**e)**2**k)
    == floor_log2(odd**2**k * (2**e)**2**k)
    == floor_log2(odd**2**k) + (e*2**k)
    == floor_lshift_log2_(k,odd) + (e*2**k)
    ]
    [floor_lshift_log2_(k,1) == 0]
    [floor_lshift_log2_(k,2) == 2**k]
    [floor_lshift_log2_(k,4) == 2*2**k]
    [floor_lshift_log2_(k,2**e) == e*2**k]
    #n翻倍，则输出增加2**k

    [floor_lshift_log2_(k,odd-1) <= floor_lshift_log2_(k,odd) <= floor_lshift_log2_(k,odd+1)]
        #范围大小 约为 1+2**k*(2/2**floor_log2(odd)) = 1+2**(k+1-floor_log2(odd))
        #比如:[2**k == floor_lshift_log2_(k,3-1) <= floor_lshift_log2_(k,3) <= floor_lshift_log2_(k,3+1) == 2*2**k]
    [(odd-1)%2==0]
    [(odd+1)%2==0]
        #recur!
        #n reduced, but k unchanged
    #缩小范围:
    [floor_lshift_log2_(k,odd)
    == floor_lshift_log2_(k-1, odd**2)
    == floor_lshift_log2_(k-s, odd**2**s)
    #until [((k-s)+1-floor_log2(odd**2**s)) <= -t]
    # <==> [floor_log2(odd**2**s) >= (k-s+1+t)]
    # <<== [floor_log2(odd)*2**s >= (k+1+t)]
    # <<== [2**s >= ceil_div((k+1+t), floor_log2(odd))]
    # <<== [s >= ceil_log2(ceil_div((k+1+t), floor_log2(odd)))]
    ]

    #]]]'''
    if 0:
        return floor_log2(n**2**k) #太慢！
    raise NotImplementedError('waiting floor_sqrt')
from seed.func_tools.recur5yield import recur5yield__list__echo__echo

def _(t, /):
  @recur5yield__list__echo__echo
  def floor_lshift_log2_(k, n, /):
    assert k >= 0
    assert n >= 1
    if k == 0:
        r = floor_log2(n)
    elif n&1 == 0:
        r = yield recur_even(k, n)
    else:
        r = yield recur_odd(k, n)
    return True, r;yield
  def recur_even(k, even, /):
    assert k >= 1
    assert even&1==0
    (e, odd) = factor_pint_out_2_powers(even)
    assert e >= 1
    r_ = yield recur_odd(k, odd)
    r = r_ + (e<<k)
    return True, r;yield

  def recur_odd(k, odd, /):
    assert k >= 1
    assert odd&1==1
    if odd==1:
        r = 0
    else:
        while not (k+1-floor_log2(odd)) <= -t:
            k -= 1
            odd **= 2
            if k == 0:
                break
        else:
            while k:
                rL = recur_even(k, odd-1)
                rR = recur_even(k, odd+1)
                if rL == rR:
                    r = rL
                    break
                k -= 1
                odd **= 2
            else:
                pass
        if k == 0:
            r = floor_log2(odd)

    return True, r;yield
  return floor_lshift_log2_
floor_lshift_log2_ = _()



#整数表达为(bit_length, Iter (bit_length, uint))
#无限长浮点数连续开平方


def ceil_log_(B, n, /):
    r'''
>>> ceil_log_(2, 1)
0
>>> ceil_log_(2, 2)
1
>>> ceil_log_(2, 3)
2
>>> ceil_log_(2, 4)
2
>>> ceil_log_(2, 5)
3
>>> ceil_log_(2, 7)
3
>>> ceil_log_(2, 8)
3
>>> ceil_log_(2, 9)
4

>>> ceil_log_(3, 1)
0
>>> ceil_log_(3, 2)
1
>>> ceil_log_(3, 3)
1
>>> ceil_log_(3, 4)
2
>>> ceil_log_(3, 8)
2
>>> ceil_log_(3, 9)
2
>>> ceil_log_(3, 10)
3


    #'''
    assert B >= 2
    assert n >= 1
    if n == 1:
        e = 0
        assert n == B**e
    else:
        e = 1+floor_log_(B, n-1)
    assert (B**(e-1) if e else 0) < n <= B**e
    return e
def floor_log_(B, n, /):
    r'''
>>> floor_log_(2, 1)
0
>>> floor_log_(2, 2)
1
>>> floor_log_(2, 3)
1
>>> floor_log_(2, 4)
2
>>> floor_log_(2, 5)
2
>>> floor_log_(2, 7)
2
>>> floor_log_(2, 8)
3
>>> floor_log_(2, 9)
3

>>> floor_log_(3, 1)
0
>>> floor_log_(3, 2)
0
>>> floor_log_(3, 3)
1
>>> floor_log_(3, 4)
1
>>> floor_log_(3, 8)
1
>>> floor_log_(3, 9)
2
>>> floor_log_(3, 10)
2

>>> floor_log_(3, 10**100)
209
>>> floor_log_(3, 11**1000)
2182
>>> floor_log_(3, 12**1000_000)
2261859
>>> floor_log_(3, 1<<1000_000)
630929

>>> floor_log_(5, 12**1000_000)
1543959
>>> floor_log_(6, 1<<1000_000)
386852
>>> floor_log_(8, 1<<1000_000)
333333
>>> floor_log_(9, 1<<1000_000)
315464
>>> floor_log_(29, 1<<1000_000)
205846


    #'''
    assert B >= 2
    assert n >= 1
    e = _2_floor_log_(B, n)
    assert e >= 0
    #assert 1 <= n//B**e < B
    assert B**e <= n < B**(e+1)
    return e
def _2_floor_log_(B, n, /):
    if n < B: return 0
    # [n >= B]
    flbN = floor_log2(n)
    if B == 2:
        return flbN
    clbB = ceil_log2(B)
    assert clbB >= 2
    q = flbN//clbB
    if B == (1<<clbB):
        return q
    # [(1<<(clbB-1)) < B < (1<<clbB)]

    # [1 <= clbB-1 < log2(B) < clbB]
    # [log2(n)/clbB < log(B;n)==log2(n)/log2(B) < log2(n)/(clbB-1)]
    # [flbN//clbB <= floor_log_(B;n) <= flbN/(clbB-1)]
    q1 = flbN//(clbB-1)
    if q==q1:
        # [0 <= flbN-clbB*q < clbB]
        # [0 <= flbN-(clbB-1)*q1 < (clbB-1)]
        # [0 <= flbN-clbB*q < clbB-1-q]
        return q
    # [flbN >= (clbB-1) >= 1]
    #   since:[0 <= flbN < (clbB-1)] ==>> [q==0==q1]
    # xxx [flbN >= clbB*(clbB-1)]
    # xxx [n >= B**2]


    n0 = n; del n
    n_ = n0
    e_ = 0
    Bpow_clb_pairs = None
    while q1 - q > 32:
        n0_ = n_
        #_clb_Bpow = ceil_sqrt(flbN)
        #_clb_Bpow = 1<<ceil_log2_sqrt(flbN)
        #_clb_clb_Bpow = ceil_div(ceil_log2(flbN), 2)
        _clb_clb_Bpow = ceil_log2_sqrt(flbN)
        _clb_Bpow = (1<<_clb_clb_Bpow)
        # [(_clb_Bpow//2)**2 < flbN <= _clb_Bpow**2]
        assert (_clb_Bpow//2)**2 < flbN <= _clb_Bpow**2

        if Bpow_clb_pairs is None:
            Bpow_clb_pairs = [(B, clbB)]
            while Bpow_clb_pairs[-1][1] < _clb_Bpow:
                Bpow = Bpow_clb_pairs[-1][0]**2
                clb_Bpow = ceil_log2(Bpow)
                Bpow_clb_pairs.append((Bpow, clb_Bpow))
            idx4Bpow_clb_pairs = len(Bpow_clb_pairs)-1
        else:
            for j in reversed(range(idx4Bpow_clb_pairs)):
                if Bpow_clb_pairs[j][1] < _clb_Bpow:
                    break
            else:
                j = -1
            idx4Bpow_clb_pairs = j+1

        #(Bpow, clb_Bpow) = Bpow_clb_pairs[idx4Bpow_clb_pairs]
        #assert clb_Bpow >= _clb_Bpow
        #   #由于下面再次微调，不一定有[clb_Bpow >= _clb_Bpow]
        # [ceil_div(clb_Bpow,2) < _clb_Bpow <= clb_Bpow]
        # [ceil_div(clb_Bpow,2)//2 <= _clb_Bpow//2 <= ceil_div(clb_Bpow,2) < _clb_Bpow <= clb_Bpow]
        # [(_clb_Bpow//2)**2 < flbN <= _clb_Bpow**2]
        # [((clb_Bpow+1)//4)**2 == (ceil_div(clb_Bpow,2)//2)**2 < flbN <= clb_Bpow**2]
        # [flbN//clb_Bpow >= ((clb_Bpow+1)//4)**2//clb_Bpow >= ((clb_Bpow+1-3)/4)**2/clb_Bpow//1 == (clb_Bpow-4+4/clb_Bpow)/16//1 >= ((clb_Bpow-4)//16)]
        # [[clb_Bpow >= 20] -> [clb_Bpow <= flbN]]


        if 1:
            for j in reversed(range(idx4Bpow_clb_pairs)):
                if Bpow_clb_pairs[j][1]**2 < flbN:
                    break
            else:
                j = -1
            idx4Bpow_clb_pairs = j+1
        (Bpow, clb_Bpow) = Bpow_clb_pairs[idx4Bpow_clb_pairs]
        assert flbN <= clb_Bpow**2
        exp4Bpow = (1<<idx4Bpow_clb_pairs)
        assert Bpow == B**exp4Bpow
        if not exp4Bpow >= 2:
            break
        assert clb_Bpow >= 4 # == ceil_log2(3**2)
        if not clb_Bpow <= flbN:
            #if not Bpow <= n0_:
            # [[clb_Bpow >= 20] -> [clb_Bpow <= flbN]]
            # [[not$ [clb_Bpow <= flbN]] -> [clb_Bpow < 20]]
            assert clb_Bpow < 20
            break
        # [clb_Bpow <= flbN]

        assert not (B==3 and n0_ <= 31)
        #if not clb_Bpow == 2:原条件，更改如下：
        if not (B==3 and n0_ <= 31):
            # 粗略计算floor_log_Bpow_n
            assert clb_Bpow >= 3 #[保留]对应原条件:[not clb_Bpow == 2]
            q_pow = flbN//clb_Bpow
            q1_pow = flbN//(clb_Bpow-1)
            assert q_pow >= 1 # since [clb_Bpow <= flbN]
            assert 0 <= q1_pow-q_pow <= 2
            approximate_floor_log_Bpow_n = q_pow
            n_ = n0_//Bpow**approximate_floor_log_Bpow_n
            e_ += exp4Bpow*approximate_floor_log_Bpow_n
            #assert 1 <= n_ < Bpow**3
            for i in range(2):
                if n_ < Bpow:
                    break
                n_ //= Bpow
                e_ += exp4Bpow
            assert 1 <= n_ < Bpow

            flbN_ = floor_log2(n_)
            # [n0_//n_ >= Bpow**approximate_floor_log_Bpow_n == (B**exp4Bpow)**q_pow >= (3**2)**(flbN//clb_Bpow) >= 9**((clb_Bpow-4)//16) >= 1]
            assert clb_Bpow >= 4 # == ceil_log2(3**2)
            if 0b00:
                print((clb_Bpow, flbN, flbN_, flbN-flbN_))
            if not flbN_<<2 <= flbN:
                break


        elif not (B==3 and n0_ <= 31):
            raise logic-err #since 相同条件在上面分支
            #
            # 精确计算floor_log_Bpow_n没有意义，见上面:粗略计算
            # 见下面:[[clb_Bpow==2] ==>> [[B==3][3 <= n0_ <= 31]]]
            #   ==>> [[not$ [B==3][3 <= n0_ <= 31]] ==>> [not$ [clb_Bpow==2]]]
            assert clb_Bpow >= 3
            # eval [floor_log_Bpow_n := floor_log_(Bpow, n0_)]
            q_pow = flbN//clb_Bpow
            q1_pow = flbN//(clb_Bpow-1)
            q11_pow = (1+flbN)//(clb_Bpow-1)
            # bug:[q_pow <= floor_log_Bpow_n <= q1_pow]
            # [q_pow <= floor_log_Bpow_n <= q11_pow]
            #(q1_pow, r1_pow) = divmod(flbN, (clb_Bpow-1))
            # [flbN == q1_pow*(clb_Bpow-1) + r1_pow == q1_pow*clb_Bpow + (r1_pow-q1_pow)]
            # [q1_pow + (r1_pow-q1_pow)//clb_Bpow == q_pow]
            #
            # [clb_Bpow >= clbB >= 2]
            # [flbN <= clb_Bpow**2]
            #
            # [q1_pow = flbN//(clb_Bpow-1) <= clb_Bpow**2//(clb_Bpow-1) <= if clb_Bpow == 2 then 4 else clb_Bpow+1]
            # [clb_Bpow >= 3]
            # [0 <= q1_pow <= (clb_Bpow+1)]
            # [0 <= r1_pow < (clb_Bpow-1)]
            # [-(clb_Bpow+1) <= r1_pow-q1_pow < (clb_Bpow-1)]
            # [-2 <= (r1_pow-q1_pow)//clb_Bpow <= 0]
            # [q1_pow + (r1_pow-q1_pow)//clb_Bpow == q_pow]
            # [0 <= q1_pow-q_pow <= 2]
            assert 0 <= q1_pow-q_pow <= 2
            #
            assert clb_Bpow >= 4 # == ceil_log2(3**2)
            #(q11_pow, r11_pow) = divmod(1+flbN, (clb_Bpow-1))
            # [flbN == q11_pow*(clb_Bpow-1) + r11_pow-1 == q11_pow*clb_Bpow + (r11_pow-q11_pow-1)]
            # [q11_pow + (r11_pow-q11_pow-1)//clb_Bpow == q_pow]
            #
            # [q11_pow = (1+flbN)//(clb_Bpow-1) <= (1+clb_Bpow**2)//(clb_Bpow-1) <= if clb_Bpow == 2 then 5 elif clb_Bpow==3 then 5 else clb_Bpow+1]
            # [clb_Bpow >= 4]
            # [0 <= q11_pow <= (clb_Bpow+1)]
            # [0 <= r11_pow < (clb_Bpow-1)]
            # [-(clb_Bpow+2) <= r11_pow-q11_pow-1 < (clb_Bpow-2)]
            # [-2 <= (r11_pow-q11_pow-2)//clb_Bpow <= 0]
            # [q11_pow + (r11_pow-q11_pow-2)//clb_Bpow == q_pow]
            # [0 <= q11_pow-q_pow <= 2]
            assert 0 <= q11_pow-q_pow <= 2
            #
            # bug:[q_pow <= floor_log_Bpow_n <= q1_pow]
            # [q_pow <= floor_log_Bpow_n <= q11_pow]
            if q_pow == q11_pow:
                floor_log_Bpow_n = q_pow
            else:
                Bpowpow = Bpow**(q_pow+1)
                if n0_ < Bpowpow:
                    floor_log_Bpow_n = q_pow+0
                elif q_pow+1 == q11_pow or n0_ == Bpowpow or n0_ < Bpowpow*Bpow:
                    floor_log_Bpow_n = q_pow+1
                else:
                    floor_log_Bpow_n = q_pow+2
            #assert Bpow**floor_log_Bpow_n <= n0_ < Bpow**(floor_log_Bpow_n+1)
            n_ = n0_//Bpow**floor_log_Bpow_n
            assert 1 <= n_ < Bpow
            e_ += exp4Bpow*floor_log_Bpow_n
            if 0b00:
                flbN_ = floor_log2(n_)
                print((clb_Bpow, flbN, flbN_, flbN-flbN_))


        else:
            raise logic-err #since [(q1-q > 32)] ==>> [n>32]
            ############
            assert (B==3 and n0_ <= 31)
            n_ = n0_
            e_ += 0
            break
        if 0:
            #推导自:[clb_Bpow==2]
          if clb_Bpow == 2:
            assert clb_Bpow == 2
            # [(1<<(clbB-1)) < B < (1<<clbB)]
            assert B == 3
            # [flbN >= (clbB-1) >= 1]
            assert 1 <= flbN <= 4
            # [n0_ >= B]
            assert 3 <= n0_ <= 31
            n_ = n0_
            e_ += 0
            # [[clb_Bpow==2] ==>> [[B==3][3 <= n0_ <= 31]]]
            # [[not$ [B==3][3 <= n0_ <= 31]] ==>> [not$ [clb_Bpow==2]]]
        ###########################
        ###########################
        ###########################
        flbN = floor_log2(n_)
        q = flbN//clbB
        q1 = flbN//(clbB-1)
    else:
        pass
    #end-while
    (n_, e_)



    if 0:
        e = 0
        _n = n
    else:
        e = e_
        _n = n_
    q = q0 = 1<<3
    while not (q < q0):
        flbN = floor_log2(_n)
        q = flbN//clbB
        _n //= B**q
        if not _n >= 1: raise logic-err
        e += q
    e += _1_floor_log_(B, _n)
    return e


def _1_floor_log_(B, n, /):
    #assert B >= 2
    #assert n >= 1
    #if n < B: return 0
    B_pows = [B] # [B**2**i | [i :<- [0..]]]
    while not (n < B_pows[-1]):
        B_pows.append(B_pows[-1]**2)
    B_pows.pop()
    e = 0
    while B_pows:
        last = B_pows.pop()
        if not (n < last):
            n //= last
            e |= 1<<len(B_pows)
    return e
if 0:
    _1_floor_log_.__doc__ = fr'''
>>> floor_log_ = _1_floor_log_
{floor_log_.__doc__!s}

#'''

if 0:
    _1_floor_log_.__doc__ = floor_log_.__doc__.replace('floor_log_', '_1_floor_log_')

def _t1__floor_log_():
    for B in range(2,20):
        for n in range(1,10_0001):
            floor_log_(B, n)
def _t2__floor_log_():
    for B in range(2,20):
        for e in range(0,1001):
            floor_log_(B, 7**e)
    floor_log_(3, 7**2_0000)

if __name__ == "__main__":
    _t2__floor_log_()
    _t1__floor_log_()
    #raise #0b01 #0b00
if __name__ == "__main__":
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    assert (1<<1000_000) < float('inf')
    #print(_1_floor_log_.__doc__)


