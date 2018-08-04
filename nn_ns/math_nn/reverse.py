"""
reverse( a, m)::=
    given a, m, calc b, s.t. a*b = gcd(a,m) mod m, 0<=b<m

reverse_phi( n)::=
    { m | phi(m) = n}

    
"""





def sign( x):
    if x > 0:
        return +1
    elif x == 0:
        return  0
    else:
        return -1


    

def reverse( a, m):
    """
    k1*a+k2*m = gcd
    r1 = A1*a+A2*m
    r2 = B1*a+B2*m
    r1 = q1*r2 + r3
    r3 = r1-q1*r2 = (A1-q1*B1)*a + (A2-q1*B2)*m
    if r3 | r2 => r3 = gcd 

    k1*a/g+k2*m/g = 1 if g != 0
    (k1+x*m/g)*a/g + (k2-x*a/g)*m/g = 1
    k1 mod m/g
    """

    A1,A2 = 1,0
    B1,B2 = 0,1
    r1,r2 = a,m
    while( r2 != 0):
        assert( (r1,r2) == (A1*a+A2*m, B1*a+B2*m) )
        q1, r3 = divmod( r1, r2)
        A1,A2,B1,B2 = B1, B2, A1-q1*B1, A2-q1*B2
        r1,r2 = r2,r3

    s = sign( r1)
    g = s * r1         # == gcd( a, m)
    k1,k2 = s*A1, s*A2 # k1*a+k2*m == g;; note: sign(0)=0,so even A1!=0, k1 can be 0 
    
    if m != 0: # g != 0
        k1 %= abs( m//g)
        k2 = ( g - k1*a) // m

    assert( k1*a+k2*m == g)
    assert( m == 0 or 0 <= k1 < abs(m//g) )

    return (k1,k2,g)
    


def test_reverse():
    test_data = [\
        [ (0,0), (0,0,0)],\
        [ (3,0), (1,0,3)],\
        [ (0,3), (0,1,3)],\
        [ (-3,0), (-1,0,3)],\
        [ (0,-3), (0,-1,3)],\
        [ (3,3), (0,1,3)],\
        [ (-3,3), (0,1,3)],\
        [ (3,-3), (0,-1,3)],\
        [ (-3,-3), (0,-1,3)],\
        [ (3,6), (1,0,3)],\
        [ (-3,6), (1,1,3)],\
        [ (3,-6), (1,0,3)],\
        [ (-3,-6), (1,-1,3)],\
        [ (6,3), (0,1,3)],\
        [ (-6,3), (0,1,3)],\
        [ (6,-3), (0,-1,3)],\
        [ (-6,-3), (0,-1,3)],\
        [ (6,8), (3,-2,2)],\
        [ (-6,8), (1,1,2)],\
        [ (6,-8), (3,2,2)],\
        [ (-6,-8), (1,-1,2)],\
        [ (21,34), (13,-8,1)],\
        [ (-21,34), (21,13,1)],\
        [ (21,-34), (13,8,1)],\
        [ (-21,-34), (21,-13,1)],\
        [ (21,13), (5,-8,1)],\
        [ (-21,13), (8,13,1)],\
        [ (21,-13), (5,8,1)],\
        [ (-21,-13), (8,-13,1)],\
        ]

    for am, ret in test_data:
        if reverse( *am) != ret:
            print( "reverse{} == {} != {}".format( am, reverse( *am), ret))

    return
        






def calc_reverse_mod( m):
    reverse_table = []
    for a in range( m):
        k1,k2,g = reverse( a, m)
        if g == 1:
            reverse_table.append( (a,k1) )

    return reverse_table





def primitive_root( p):
    # p is a odd prime?
    # is_prime( p) and p != 2
    p = 137
    # factor p-1
    # 136 = 2^3*17
    factors = [2,17]
    for r in range( 2, p):
        for f in factors:
            if r**( (p-1)// f ) % p == 1:
                break
        else:
            return r

    assert( False)
    return

        



def gen_circle_group( a, m):
    assert( m > 0)
    assert gcd(a,m) == 1
    a %= m
    b = (a*a) % m
    circle = [a]
    while( b != a):
        circle.append( b)
        b = (b*a) % m

    return circle



def pesu_random_by_line_mod( x, a, b, m): # 3, 61, 137 => 0:137 but 38
    """A(n+1) = a*A(n)+b mod m"""

    return ( a*x + b) % m



def try_pesu_random_by_line_mod():
    a,b,m = 3,61,137
    miss, instead = 38, 131
    upbound = 128
    d = [1]
    x = 1
    x = pesu_random_by_line_mod( x, a, b, m)
    while( 1 != x ):
        if x == instead:
            d.append( miss)
        elif x < upbound:
            d.append( x)
        x = pesu_random_by_line_mod( x, a, b, m)

    return d
    

    


    
