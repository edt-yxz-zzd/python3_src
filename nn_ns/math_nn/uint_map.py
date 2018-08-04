
####################################################
####################### type #######################
####################################################
"""
central:
uint ::= unsigned integer = natural number
"""

"""
basic: 
sint ::= signed integer = integer
pint ::= positive integer
rImI ::= residue<m> = [0:m] = the least nonnegative residues modulo m, m > 0
bool ::= boolean = { false, true} != rI2I
"""

"""
structural:
tupleIn2kI ::= tuple of x elements, 0 <= n <= x < k <= 00, 1 < k
setIn2kI ::= set of x elements, 0 <= n <= x < k <= 00, 1 < k
multisetIn2kI ::= multiset of x elements, 0 <= n <= x < k <= 00, 1 < k
"""

"""
special:
baseIBI ::= number in the mathematical numeral system of radix B,
                B > 1, little-endian
enumImI ::= list_rImI_compact = ???, m > 0, little-endian
"""


####################################################
####################### map  #######################
####################################################
"""
uint <-> # xint stands for uint/sint/pint; struct stands for tuple/set/multiset
            xint
            baseIBI
            enumImI
            structIn2kI_xint_byImI



uint <-> xint/baseIBI/tupleIn2kI_uint_byImI
baseIBI <-> enumImI
tuple_uint <->  struct_'xint'
"""


####################################################
####################### note #######################
####################################################
"""
m > 0, n >= 0, B > 1, k > n, k > 1, k < 00
lt == less_than
gt == greater_than
le == less_than_or_equal
ge == ....
eq == equal
little-endian
"""

####################################################
####################### test #######################
####################################################

def test_all():
    #import sys
    #dir(sys.modules[__name__]) # except __name__ == '__main__'
    tests = []
    for item in globals().keys():
        if item[:5] == 'test_' and item != 'test_all':
            tests.append(item)

    for test in tests:
        print(test)
        exec(test + '()')

        

    
def test_uint2uint():
    d = [\
        (0,0),\
        (1,1),\
        (2,2),\
        (3,3),\
        (4,4),\
        (5,5),\
        ]

    for (i,o) in d:
        assert( uint2uint(i) == o)


def test_uint2sint():
    d = [\
        (0,0),\
        (1,-1),\
        (2,1),\
        (3,-2),\
        (4,2),\
        (5,-3),\
        (6,3),\
        (7,-4),\
        (8,4),\
        (9,-5),\
        ]

    for (u,s) in d:
        assert( s == uint2sint(u))
        assert( u == sint2uint(s))


def test_uint2pint():
    d = [\
        (0,1),\
        (1,2),\
        (2,3),\
        (3,4),\
        (4,5),\
        (5,6),\
        (6,7),\
        (7,8),\
        (8,9),\
        (9,10),\
        ]

    for (u,p) in d:
        assert( p == uint2pint(u))
        assert( u == pint2uint(p))


def test_uint2baseIBI():
    B2 = 2
    d2 = [\
        (0,[]),\
        (1,[1]),\
        (2,[0,1]),\
        (3,[1,1]),\
        (4,[0,0,1]),\
        (5,[1,0,1]),\
        (6,[0,1,1]),\
        (7,[1,1,1]),\
        (8,[0,0,0,1]),\
        (9,[1,0,0,1]),\
        ]
    
    B3 = 3
    d3 = [\
        (0,[]),\
        (1,[1]),\
        (2,[2]),\
        (3,[0,1]),\
        (4,[1,1]),\
        (5,[2,1]),\
        (6,[0,2]),\
        (7,[1,2]),\
        (8,[2,2]),\
        (9,[0,0,1]),\
        ]

    for (B,d) in [(B2,d2),(B3,d3)]:
        for (u,b) in d:
            assert( b == uint2baseIBI(u,B))
            assert( u == baseIBI2uint(b,B))



def test_uint2enumImI():
    m1 = 1
    d1 = [\
        (0,[]),\
        (1,[0]),\
        (2,[0,0]),\
        (3,[0,0,0]),\
        (4,[0,0,0,0]),\
        (5,[0,0,0,0,0]),\
        (6,[0,0,0,0,0,0]),\
        (7,[0,0,0,0,0,0,0]),\
        (8,[0,0,0,0,0,0,0,0]),\
        (9,[0,0,0,0,0,0,0,0,0]),\
        ]

    m2 = 2
    d2 = [\
        (0,[]),\
        (1,[0]),\
        (2,[1]),\
        (3,[0,0]),\
        (4,[1,0]),\
        (5,[0,1]),\
        (6,[1,1]),\
        (7,[0,0,0]),\
        (8,[1,0,0]),\
        (9,[0,1,0]),\
        (10,[1,1,0]),\
        (11,[0,0,1]),\
        (12,[1,0,1]),\
        (13,[0,1,1]),\
        (14,[1,1,1]),\
        (15,[0,0,0,0]),\
        (16,[1,0,0,0]),\
        (17,[0,1,0,0]),\
        ]
    
    m3 = 3
    d3 = [\
        (0,[]),\
        (1,[0]),\
        (2,[1]),\
        (3,[2]),\
        (4,[0,0]),\
        (5,[1,0]),\
        (6,[2,0]),\
        (7,[0,1]),\
        (8,[1,1]),\
        (9,[2,1]),\
        (10,[0,2]),\
        (11,[1,2]),\
        (12,[2,2]),\
        (13,[0,0,0]),\
        (14,[1,0,0]),\
        (15,[2,0,0]),\
        (16,[0,1,0]),\
        (17,[1,1,0]),\
        ]

    for (m,d) in [(m1,d1),(m2,d2),(m3,d3)]:
        for (u,e) in d:
            assert( e == uint2enumImI(u,m))
            assert( u == enumImI2uint(e,m))


def test_uint2tupleIn2kI_uint_byImI():
    ks = [2, 3, 4, float('inf')]
    ns = [0, 1, 2]
    ub = 3000
    ms = [1, 2, 3]
    tub = 10

    for k in ks:
        for n in ns:
            if not n < k:
                break

            if k == float('inf'):
                k_ = n + 3
            else:
                k_ = k
            tlow = enumImI2uint([0]*n, tub)
            thigh = enumImI2uint([0]*k_, tub)

            for m in ms:
                for u in range(ub):
                    t = uint2tupleIn2kI_uint_byImI(u, n, k, m)
                    v = tupleIn2kI_uint_byImI2uint(t, n, k, m)
                    if not u == v:
                        print(u, t, v, n, k, m)
                        return

                for i in range(tlow, thigh):
                    t = uint2enumImI(i, tub)
                    u = tupleIn2kI_uint_byImI2uint(t, n, k, m)
                    s = uint2tupleIn2kI_uint_byImI(u, n, k, m)
                    if not t == s:
                        print(t, u, s, n, k, m)
                        return



def test_uint2setIn2kI_uint_byImI():
    ks = [2, 3, 4, float('inf')]
    ns = [0, 1, 2]
    ub = 3000
    ms = [1, 2, 3]

    for k in ks:
        for n in ns:
            if not n < k:
                break

            for m in ms:
                for u in range(ub):
                    s = uint2setIn2kI_uint_byImI(u, n, k, m)
                    v = setIn2kI_uint_byImI2uint(s, n, k, m)
                    if not u == v:
                        print(u, s, v, n, k, m)
                        return



def test_uint2multisetIn2kI_uint_byImI():
    ks = [2, 3, 4, float('inf')]
    ns = [0, 1, 2]
    ub = 3000
    ms = [1, 2, 3]

    for k in ks:
        for n in ns:
            if not n < k:
                break

            for m in ms:
                for u in range(ub):
                    s = uint2multisetIn2kI_uint_byImI(u, n, k, m)
                    v = multisetIn2kI_uint_byImI2uint(s, n, k, m)
                    if not u == v:
                        print(u, s, v, n, k, m)
                        return






def test_tuple_uint2struct_xint():
    tu = [3, 1, 0, 4]
    tp = [4, 2, 1, 5]
    ts = [-2, -1, 0, 2]

    su = [3, 5, 6, 11]
    sp = [4, 6, 7, 12]
    ss = [-2, 0, 1, 6]

    mu = [3, 4, 4, 8]
    mp = [4, 5, 5, 9]
    ms = [-2, -1, -1, 3]



    for x in ['u', 'p', 's']:
        for struct in ['tuple', 'set', 'multiset']:
            xint = x + 'int'
            struct_xint = struct + '_xint'
            data = struct[0] + x
            x2u = xint + '2uint'
            u2x = 'uint2' + xint
            expr1 = 'assert tu == ' + struct_xint + '2tuple_uint(' + \
                    data + ', ' + x2u + ')'
            expr2 = 'assert ' + data + ' == tuple_uint2' + struct_xint + '(' + \
                    'tu' + ', ' + u2x + ')'

            exec(expr1)
            exec(expr2)





####################################################
####################### code #######################
####################################################


def part_sum_geometric_series( L, m):
    "sum( m^i for i in [0:L])"
    if m == 1:
        return L

    return (m**L - 1) // (m - 1)

def floor_inv_psgs( u, m):
    "arg max_{L} : part_sum_geometric_series(L,m) <= u, m > 0, u > 0"
    if m == 1:
        return u

    return floor_log( u*(m-1)+1, m)


def floor_log(u,B):
    "return e if B**e <= u < B**(e+1), B > 1, u >= 1"
    
    assert( B > 1)
    assert( u >= 1)
    
    pow_B_2_i = [] #pow_w_2_i[i] == B**(2**i)
    pow_B = B # == B**(2**0) == B**(2**len(pow_B_2_i))
    while( pow_B <= u):
        pow_B_2_i.append( pow_B)
        pow_B *= pow_B # == B**(2**len(pow_B_2_i))

    assert( u < pow_B == B**(2**len(pow_B_2_i)) )

    power = 0
    q = u
    for i in range( len(pow_B_2_i)-1, 0-1, -1):
        if q >= pow_B_2_i[i]:
            q //= pow_B_2_i[i]
            power += 2**i

    assert( B**power <= u < B**(power+1) )
    return power




def choose(k,n):
    """n choose k = factorial(n)//(factorial(k)*factorial(n-k)) if 0 <= k <= n
                    0 otherwise
    """
    if not( 0 <= k <= n):
        return 0
    elif k > n//2:
        return choose( n-k, n)
    elif k == 0:
        return 1

    assert( 0 < k <= n//2)
    # n*(n-1)...(n-k+1) // k*(k-1)...1
    n_ = n
    for i in range( n-k+1, n):
        n_ *= i

    k_ = k
    for i in range( 2, k):
        k_ *= i

    return n_ // k_

    













def uint2uint(u):
    return u


def uint2sint(u):
    is_neg = u & 1
    if is_neg:
        s = (u + 1) >> 1
        s = -s
    else:
        s = u >> 1

    return s

def sint2uint(s):
    is_neg = s < 0
    if is_neg:
        s = -s
        u = (s << 1) - 1
    else:
        u = s << 1

    return u


def uint2pint(u):
    return u + 1

def pint2uint(p):
    return p - 1


def uint2baseIBI(u,B):
    #assert( u >= 0)
    assert(B > 1)
    b = []
    while(u > 0):
        u,r = divmod(u,B)
        b.append(r)

    return b

def baseIBI2uint(b,B):
    assert(B > 1)
    u = 0
    for i in range( len(b)-1, 0-1, -1):
        u *= B
        u += b[i]
        #assert( 0 <= b[i] < m)

    return u


def uint2enumImI(u,m):
    assert(m > 0)
    if m == 1:
        return uint2enumI1I(u)
    else:
        return uint2enumIBI(u,m)
    
def uint2enumI1I(u):
    return [0]*u

def uint2enumIBI(u,B):
    assert(B > 1)
    L = enumIBI_length_of_uint(u,B)
    u -= part_sum_geometric_series( L, B)
    b = uint2baseIBI(u,B)
    return b + [0]*( L- len(b))


def enumIBI_length_of_uint(u,B):
    "arg max_{L} : part_sum_geometric_series(L,B) <= u, B > 1, u > 0"
    assert(B > 1)
    return floor_inv_psgs( u, B)










def enumImI2uint(e,m):
    if m == 1:
        return enumI1I2uint(e)
    else:
        return enumIBI2uint(e,m)


def enumI1I2uint(e):
    return len(e)


def enumIBI2uint(e,B):
    assert(B > 1)
    return baseIBI2uint(e,B) + part_sum_geometric_series( len(e), B)







def tupleIn2kI_uint_byImI2uint(t, n, k, m):
    assert 0 <= n <= len(t) < k <= float('inf')
    assert k > 1 and m > 0
    assert len([u for u in t if u < 0]) == 0

    if len(t) == n != 0:
        for i in range(n):
            if t[i] != 0:
                break

        if t[i] == 0:
            assert i == n - 1
            assert t == [0]*n
            s = []
        else:
            s = t[i:]
            s[0] -= 1

        t = s
            

    assert 0 <= len(t) < k
    return tupleI0_2kI_uint_byImI2uint(t, k, m)



def tupleI0_2kI_uint_byImI2uint(t, k, m):
    assert 0 <= len(t) < k <= float('inf')
    assert k > 1 and m > 0

    if len(t) == 0:                     # assert len(t) == 0
        return 0
    
    if len(t) == k-1:
        dm = 1
    else:
        dm = 0

    e = []
    for u in t[:-1]:
        e += uint2enumImI(u, m)
        e.append(m)
    else:
        e += uint2enumImI(t[-1], m + dm) # assert len(t) != 0

    return enumImI2uint(e, m+1) + 1



def uint2tupleIn2kI_uint_byImI(u, n, k, m):
    assert 0 <= n < k <= float('inf')
    assert k > 1 and m > 0 and u >= 0

    t = uint2tupleI0_2kI_uint_byImI(u, k, m)
    if len(t) <= n:
        s = [0]*(n - len(t))
        if len(t) != 0:
            s.append(t[0] + 1)
            s += t[1:]

        t = s

    assert n <= len(t) < k
    return t


def uint2tupleI0_2kI_uint_byImI(u, k, m):
    assert 1 < k <= float('inf')
    assert m > 0 and u >= 0
    
    if u == 0:
        return []

    u -= 1
    e = uint2enumImI(u, m+1)
    t = []
    start = 0
    while len(t) < k - 2:
        for i in range(start, len(e)):
            if e[i] == m:
                stop = i
                u = enumImI2uint(e[start : stop], m)
                t.append(u)
                start = stop + 1
                break
        else:
            stop = len(e)
            u = enumImI2uint(e[start : stop], m)
            t.append(u)
            break
    else:
        stop = len(e)
        u = enumImI2uint(e[start : stop], m+1)
        t.append(u)

    assert 1 <= len(t) < k
    return t


 
    




def tuple_xint2tuple_uint(tx, func_x2u):
    tu = []
    for x in tx:
        u = func_x2u(x)
        assert u >= 0
        tu.append(u)

    assert len(tu) == len(tx)
    return tu


def tuple_uint2tuple_xint(tu, func_u2x):
    tx = []
    for u in tu:
        assert u >= 0
        x = func_u2x(u)
        tx.append(x)

    assert len(tx) == len(tu)
    return tx





def set_xint2tuple_uint(s, func_x2u):
    t = []
    if len(s):
        u = func_x2u(s[0])
        assert u >= 0
        t.append(u)

    for i in range(1, len(s)):
        u = s[i] - s[i-1] - 1
        assert u >= 0
        t.append(u)

    assert len(t) == len(s)
    return t




def tuple_uint2set_xint(t, func_u2x):
    s = []
    if len(t):
        assert t[0] >= 0
        x = func_u2x(t[0])
        s.append(x)

    for i in range(1, len(t)):
        assert t[i] >= 0
        s.append(t[i] + s[-1] + 1)

    assert len(s) == len(t)
    return s



def multiset_xint2tuple_uint(s, func_x2u):
    t = []
    if len(s):
        u = func_x2u(s[0])
        assert u >= 0
        t.append(u)

    for i in range(1, len(s)):
        u = s[i] - s[i-1]
        assert u >= 0
        t.append(u)

    assert len(t) == len(s)
    return t




def tuple_uint2multiset_xint(t, func_u2x):
    s = []
    if len(t):
        assert t[0] >= 0
        x = func_u2x(t[0])
        s.append(x)

    for i in range(1, len(t)):
        assert t[i] >= 0
        s.append(t[i] + s[-1])

    assert len(s) == len(t)
    return s













def uint2setIn2kI_uint_byImI(u, n, k, m):
    t = uint2tupleIn2kI_uint_byImI(u, n, k, m)
    s = tuple_uint2set_xint(t, uint2uint)
    return s



def setIn2kI_uint_byImI2uint(s, n, k, m):
    t = set_xint2tuple_uint(s, uint2uint)
    u = tupleIn2kI_uint_byImI2uint(t, n, k, m)
    return u


def uint2multisetIn2kI_uint_byImI(u, n, k, m):
    t = uint2tupleIn2kI_uint_byImI(u, n, k, m)
    s = tuple_uint2multiset_xint(t, uint2uint)
    return s



def multisetIn2kI_uint_byImI2uint(s, n, k, m):
    t = multiset_xint2tuple_uint(s, uint2uint)
    u = tupleIn2kI_uint_byImI2uint(t, n, k, m)
    return u



