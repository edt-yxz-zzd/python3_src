
import time, fractions #gcd# clock
import bisect

__all__ = (
    'binary_search, floor_sqrt, mod_pow, '
    'primes_by_trial_division, sieve_of_Eratosthenes, primes_by_Eratosthenes_sieve, '
    'primes_by_Sundaram_sieve, sorted_primes_lt_N, primes, '
    'sorted_primes_endby_ge, primes_lt, '
    'primality_test_of_Miller_Rabin, primality_test_of_Miller_Rabin_more, '
    'find_out_nonwitness_in_primality_test_of_Miller_Rabin, '
    'find_out_nonwitness_in_primality_test_of_Miller_Rabin_below'
    .split(', '))



def binary_search( n, ls):
    "assert ls[i] <= ls[i+1] for i in [0:len(ls)-1]"
    "assert (L == len(ls) or n < ls[L]) and (L == 0 or ls[L-1] <= n)if return L "
    "assert a <= n < b for a in ls[:L] for b in ls[L:]"
    a = 0
    b = len(ls)
    while( a + 2 < b):
        m = (a+b)//2
        if n < ls[m]:
            b = m
        else:
            a = m

    for L in range(a,b):
        if n < ls[L]:
            return L
    else:
        return b


def test_binary_search():
    for i in range(300):
        ls = range(i)
        d = [(L-1,L) for L in range(i)] + [(i,i),(i+1,i)]
        for (n,L) in d:
            assert( L == binary_search(n,ls))


def floor_sqrt(n):
    assert( n >= 0)
    if n < 2:
        return int(n) # == floor(n)
    
    h = n//2 # >= 1
    t = (h**2 + n) // (2*h)
    #i = 0
    while(t < h):
        h = t
        t = (h**2 + n) // (2*h)
        #i += 1

    #if i > n.bit_length():
    #    print( n, i)
    assert( h**2 <= n < (h+1)**2)
    return h

        

def test_floor_sqrt():
    #return [ floor_sqrt(i) for i in range(3000000)]
    for i in range(300000):
        t = floor_sqrt(i)
        assert( t**2 <= i < (t+1)**2 )
        


def mod_pow( base, index, m):
    "base**index%m"
    assert( index >= 0)
    assert( m != 0)
    
    if index == 0:
        assert base != 0
        return 1%m

    bits = bin(index)[2:]
    base %= m
    r = base
    for b in bits[1:]:
        r = r**2
        if '1' == b: #### not 1 !!!!
            r *= base

        r %= m

    return r



def test_mod_pow():
    I = 10
    J = 10
    K = 10
    for i in range(-I,I):
        for j in range(J):
            for k in range(-K,K):
                #print( i, j, k)
                assert k == 0 or i == j == 0 or i**j % k == mod_pow(i,j,k)


def primes_by_trial_division(n):
    if n == 3:
        return [2]
    
    primes = []
    idx = 0
    low = 1**2
    up = 2**2

    while(1):
        if up > n:
            up = n
            if low+2 > n:
                break
            
        for i in range( low+1, up):
            for j in range(idx):
                if 0 == i%primes[j]:
                    break
            else:
                primes.append(i)

        #print( idx, primes)
        low = up
        idx += 1
        up = primes[idx]**2

    return primes


def test_primes_by_trial_division():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, \
              23, 29, 31, 37, 41, 43, 47, \
              53, 59, 61, 67, 71, 73, 79, \
              83, 89, 97, 101, 103, 107, \
              109, 113, 127, 131, 137]

    for i in range(139):
        L = binary_search(i-1,primes)
        assert( primes[:L] == primes_by_trial_division(i))



def sieve_of_Eratosthenes(n):
    not_prime = bytearray(n)
    k = min(n,2)
    not_prime[:k] = [True]*k

    for i in range( min( n, floor_sqrt(n)+1)):
        if not not_prime[i]:
            for j in range(i**2, n, i):
                not_prime[j] = True

    return not_prime


def primes_by_Eratosthenes_sieve(n):
    not_prime = sieve_of_Eratosthenes(n)
    return [ i for i in range(n) if not not_prime[i] ]



def test_primes_by_Eratosthenes_sieve():
    for i in range(3000):
        assert primes_by_Eratosthenes_sieve(i) == primes_by_trial_division(i)





def primes_by_Sundaram_sieve(n):
    if n < 3:
        return []
    
    m = n//2
    ls = bytearray(m)
    #s=i+j+2ij < m, 1<=i<=j
    for j in range(1,(m-1)//3+1):
        for s in range(1+3*j, m, (2*j+1)):
            ls[s] = 1 # 2s+1 is not a prime

    primes = [2]
    for i in range(1,m):
        if 0 == ls[i]:
            primes.append(2*i+1)

    return primes

    
    
def test_primes_by_Sundaram_sieve():
    for i in range(3000):
        assert primes_by_Eratosthenes_sieve(i) == primes_by_Sundaram_sieve(i)


def compare_performences():
    n = [ 10**k for k in range(8)]
    r = []
    for k in n:
        t0 = time.clock()
        ps1 = primes_by_trial_division( k)
        t1 = time.clock()
        ps2 = primes_by_Eratosthenes_sieve(k)
        t2 = time.clock()
        ps3 = primes_by_Sundaram_sieve(k)
        t3 = time.clock()
        r.append( [ k, t1-t0,t2-t1, t3-t2])
        print( r[-1])
        assert( ps1 == ps2 == ps3)

    #return r
    """
    [1, 5.864555166159953e-06, 4.642772839876629e-05, 2.4435646525666505e-06]
    [10, 4.838258012082597e-05, 6.890852320237673e-05, 1.9059804290025295e-05]
    [100, 0.0003352570703321345, 0.00013928318519630667, 0.00011044912229600523]
    [1000, 0.0031194546354665897, 0.0004916452080964001, 0.0006201767088214183]
    [10000, 0.02330183252687555, 0.0031394918656176274, 0.004647659969181761]
    [100000, 0.25450752153635703, 0.03280338932191568, 0.05241250694583249]
    [1000000, 4.237873199520474, 0.348834492967665, 0.5853231687559965]
    [10000000, 82.87528779082696, 3.6776425074687467, 6.4951688283254185]
    Eratosthenes_sieve outperform other two?
    """



def _primes(n):
    return primes_by_Eratosthenes_sieve(n)

_primes_tuple = ()
def sorted_primes_endby_ge(N):
    global _primes_tuple
    
    i = bisect.bisect_left(_primes_tuple, N)
    if i == len(_primes_tuple):
        _primes_tuple = tuple(_primes(2 * max(N, 2)))
        i = bisect.bisect_left(_primes_tuple, N)
        pass

    
    assert 0 <= i < len(_primes_tuple)
    assert N <= _primes_tuple[i]
    if i > 0:
        assert N > _primes_tuple[i-1]

    return _primes_tuple, i
def sorted_primes_lt_N(N):
    _primes_tuple, i = sorted_primes_endby_ge(N)
    return _primes_tuple[:i]

def primes(n):
    return sorted_primes_lt_N(n)

primes_lt = primes







# find out all witnesses for the compositeness of n (Miller–Rabin primality test)
# is there a simple kind of witnesses = f(n)?
def primality_test_of_Miller_Rabin( n, ls = None):
    if ls == None:
        A014233 = [\
            2047, 1373653, 25326001, 3215031751, 2152302898747,\
            3474749660383, 341550071728321, 341550071728321,\
            3825123056546413051, 3825123056546413051, 3825123056546413051,\
            1 << 64 + 1]

        ps = primes(38)
        
        for i in range(len(A014233)):
            if n < A014233[i]:
                return primality_test_of_Miller_Rabin( n, ps[:i+1]) # this result is proved!
        else:
            raise ValueError( 'Now primality_test_of_Miller_Rabin( n, None) only supports n < {}'.format(A014233[-1]))
    else:
        result = primality_test_of_Miller_Rabin_more( n, ls)
        if type(result) == tuple:
            return result[0]
        else:
            return result



def primality_test_of_Miller_Rabin_more( n, ls):
    if n < 3:
        return n == 2

    # is n odd?
    if n & 1 == 0:
        return False

    # now n is odd and > 2
    # n - 1 == 2**s * d, d & 1 == 1, s > 0
    d = n >> 1
    s = 1
    while d & 1 == 0:
        d >>= 1
        s += 1

    n_1 = n - 1
    assert( n_1 == d*2**s)
    for a in ls:
        if a%n == 0:
            continue
        
        b = mod_pow( a, d, n)
        if b == 1:
            continue      # pass this round

        for i in range(s):
            if b == n_1:
                break     # pass this round
            elif b == 1:  # fail
                # factor it since
                # now i in [1:s],
                #     mod_pow( a, d*2**i, n) == 1,
                #     mod_pow( a, d*2**(i-1), n) != 1 or n-1
                # so let k = mod_pow( a, d*2**(i-1), n), then gcd(k+/-1,n) > 1
                return ( False, a, s-(i-1)) # == ( False, a, r) => a**(n>>r)%n [+-] 1

            b = b**2 % n
        else:             # fail
            if b == 1:    # we can factor like above
                return ( False, a, s-(s-1))
            else:
                return ( False, a)

    # pass all the tests
    # n may be a prime
    return True # ????


            
        
def test_primality_test_of_Miller_Rabin():
    """
    Again all integers n > 1 which fail this test are composite;
    integers that pass it might be prime.
    The smallest odd composite SPRP's are the following. 

    2047 = 23.89 is a 2-SPRP, 
    121 = 11.11 is a 3-SPRP, 
    781 = 11.71 is a 5-SPRP and, 
    25 = 5.5 is a 7-SPRP. 

    """
    d = [\
        ([2],2047),\
        ([3],121),\
        ([5],781),\
        ([7],25),\
        ([2,3],1373653),\
        #([2,3,5],25326001),\
        ]

    for (ls,sprp) in d:
        #print(ls,sprp)
        ps = [2]
        for i in range(3,sprp+1,2):
            if primality_test_of_Miller_Rabin(i,ls):
                ps.append(i)

        assert ps[-1] == sprp
        """
        for (a,b) in zip(ps[:-1],primes(sprp+1)):
            if a != b:
                print( (a,b))"""
                
        assert ps[:-1] == primes(sprp+1)

    ##################################################
    ##################################################
    ##################################################
    """
    A014233
    Smallest odd number for which Miller-Rabin primality test
    on bases <= n-th prime does not reveal compositeness.  
 
    2047, 1373653, 25326001, 3215031751, 2152302898747,
    3474749660383, 341550071728321, 341550071728321,
    3825123056546413051, 3825123056546413051, 3825123056546413051,
    >2**64

    a(12) > 2^64.  Hence the primality of numbers < 2^64 can be determined
    by asserting strong pseudoprimality to all prime bases <= 37 (=prime(12)).
    Testing to prime bases <=31 does not suffice, as a(11) < 2^64
    and a(11) is a strong pseudoprime to all prime bases <= 31 (=prime(11)).
 


    Individually these tests are still weak
    (and again there are infinitely many a-SPRP's
    for every base a>1 [PSW80]),
    but we can combine these individual tests
    to make powerful tests for small integers n>1
    (these tests prove primality): 

    If n < 1,373,653 is a both 2 and 3-SPRP, then n is prime [PSW80]. 
    If n < 25,326,001 is a 2, 3 and 5-SPRP, then n is prime [PSW80]. 
    If n < 25,000,000,000 is a 2, 3, 5 and 7-SPRP,
        then either n = 3,215,031,751 or n is prime [PSW80].
        (This is actually true for n < 118,670,087,467 [Jaeschke93].) 
    If n < 2,152,302,898,747 is a 2, 3, 5, 7 and 11-SPRP, then n is prime [Jaeschke93]. 
    If n < 3,474,749,660,383 is a 2, 3, 5, 7, 11 and 13-SPRP, then n is prime [Jaeschke93]. 
    If n < 341,550,071,728,321 is a 2, 3, 5, 7, 11, 13 and 17-SPRP, then n is prime [Jaeschke93].
    
    The first three of these are due to Pomerance, Selfridge and Wagstaff [PSW80],
    the parenthetical remark and all others are due to Jaeschke [Jaeschke93].
    (These and related results are summarized in [Ribenboim95, Chpt 2viiib].)
    In the same article Jaeschke considered other sets of primes
    (rather than just the first primes) and found these slightly better results: 
    If n < 9,080,191 is a both 31 and 73-SPRP, then n is prime. 
    If n < 4,759,123,141 is a 2, 7 and 61-SPRP, then n is prime. 
    """


    ##################################################
    ##################################################
    ##################################################
    
    ls = primes(20)
    n = 100000
    ps = []
    for i in range(n):
        if primality_test_of_Miller_Rabin(i,ls):
            ps.append(i)
    #print( ps)
    assert( ps == primes(n))


    n_ff_w = []
    for i in range(n):
        result = primality_test_of_Miller_Rabin_more( i, ls)
        if type(result) == tuple and len(result) == 3:
            ( _false, witness, delta) = result
            k = mod_pow( witness, i>>delta, i)
            pack = ( i, fractions.gcd(k-1,n), fractions.gcd(k+1,n), witness)
            n_ff_w.append(pack)
            #print( '{} -> {}, {} -> witness = {}'.format(*pack) )

    #return n_ff_w
    # n == 100000
    # len(n_ff_w) == 67
    # this factor is useless....
    """
    341 -> 31, 11 -> witness = 2
    561 -> 33, 17 -> witness = 2
    645 -> 129, 5 -> witness = 2
    1105 -> 65, 17 -> witness = 2
    1387 -> 73, 19 -> witness = 2
    ....
    """

def find_out_nonwitness_in_primality_test_of_Miller_Rabin(n):
    'find out nw s.t. primality_test_of_Miller_Rabin(n,[nw]) == True'
    assert( n > 2 and n&1 == 1)
    begin = 2
    end = n//2+1
    nws = []
    while( begin < end):
        #print( begin, end)
        result = primality_test_of_Miller_Rabin_more( n, range(begin,end))
        if type(result) == tuple and result[0] == False:
            nws += list( range( begin, result[1]))
            begin = result[1]+1
        else:
            nws += list( range( begin, end))
            break

    return nws





def find_out_nonwitness_in_primality_test_of_Miller_Rabin_below(n):
    ps = primes(n)
    idx = 2
    wss = []
    for i in range(3,n,2):
        ws = find_out_nonwitness_in_primality_test_of_Miller_Rabin(i)
        if ws != []:
            if i == ps[idx]:
                idx += 1
                continue
            wss.append((i,ws,i//2))
            print( wss[-1])

    return wss


def guess_witness_in_primality_test_of_Miller_Rabin():
    n = 100000
    ps = []
    prs = primes(n)
    
    """version 1: witness = n//2""" """#fail at 2047
    ps = [2,3]
    for i in range(5,n,2):
        if primality_test_of_Miller_Rabin( i, [i//2]):
            ps.append( i)"""

    """version 2: witness = n//3""" """#fail at 121
    ps = [2,3,5]
    for i in range(7,n,2):
        if primality_test_of_Miller_Rabin( i, [i//3]):
            ps.append( i)"""

    """version 3: witness = (n//2)**2%n""" '''#fail at 341''
    ps = [2,3,5]
    for i in range(7,n,2):
        if primality_test_of_Miller_Rabin( i, [(i//2)**2%i]):
            ps.append( i) #'''

    """version 4: witness = (n//3)**2%n""" '''#fail at 9
    ps = [2,3,5]
    for i in range(7,n,2):
        if primality_test_of_Miller_Rabin( i, [(i//3)**2%i]):
            ps.append( i)'''

    """version 5: witness = (n//3)**3%n""" '''#fail at 9''
    ps = [2,3,5]
    for i in range(7,n,2):
        if primality_test_of_Miller_Rabin( i, [(i//3)**2%i]):
            ps.append( i) #'''

    ##############
    # note that if A passes, then A**k passes too
    """version 6: witness = (i//3+i//2)%i""" '''#fail at 91''
    ps = [2,3,5]
    for i in range(7,n,2):
        if primality_test_of_Miller_Rabin( i, [(i//3+i//2)%i]):
            ps.append( i) #'''


    """version 7: witness = (i//2-i//2047)%i""" '''#fail at 2059''
    ps = [2,3]
    for i in range(5,n,2):
        if primality_test_of_Miller_Rabin( i, [(i//2-i//2047)%i]):
            ps.append( i) #'''

    """version 8: witness = (i//2-i//2047+i//2048)%i""" '''#fail at 3277''
    ps = [2,3]
    for i in range(5,n,2):
        if primality_test_of_Miller_Rabin( i, [(i//2-i//2047+i//2048)%i]):
            ps.append( i) #'''

    """version 9: witness = (i//2+(-1)**(i//1027))%i""" '''#fail at 4681''
    ps = [2,3]
    for i in range(5,n,2):
        if primality_test_of_Miller_Rabin( i, [(i//2+(-1)**(i//1027))%i]):
            ps.append( i) #'''

    """version 10: witness = (i//2+(-1)**(i//79))%i""" '''#fail at 11521''
    ps = [2,3]
    for i in range(5,n,2):
        if primality_test_of_Miller_Rabin( i, [(i//2+(-1)**(i//79))%i]):
            ps.append( i) #'''

    """version 11: witness = (i//2+(-1)**(i//79)+1-(-1)**(i//7))%i""" '''#fail at 14981'''
    ps = [2,3]
    for i in range(5,n,2):
        if primality_test_of_Miller_Rabin( i, [(i//2+(-1)**(i//79)+1-(-1)**(i//7))%i]):
            ps.append( i) #'''

    

    #if ps != primes(n):
    for (a,b) in zip(ps,prs):
        if a != b:
            print( 'ps[i] != prs[i]', a, b)
            return

    if ps != prs:
        print( len(ps), len(prs))
        print( ps[len(prs):], prs[len(ps):])


def is_sum_of_1_and_product_of_primes_prime(n):
    ps = primes(n)
    products = [1]
    for p in ps: products.append(products[-1] * p)
    plus1 = [a + 1 for a in products]
    ps = primes(plus1[-1] + 1)
    result = []
    for p1 in plus1:
        i = binary_search(p1, ps)
        result.append((p1, i > 0 and ps[i-1] == p1))
    return result


def guess_max_prime_gap_below_p(n=10000):
    ps = primes(n)
    gaps = []
    max_gap = 0
    for i in range(len(ps)-1):
        p = ps[i+1]
        gap = p - ps[i]
        if gap > max_gap:
            max_gap = gap
            gaps.append((p, max_gap))
            
    return gaps
    '''
    n = 10000000
    [(3, 1), (5, 2), (11, 4), (29, 6), (97, 8), (127, 14),
    (541, 18), (907, 20), (1151, 22), (1361, 34), (9587, 36),
    (15727, 44), (19661, 52), (31469, 72), (156007, 86),
    (360749, 96), (370373, 112), (492227, 114), (1349651, 118),
    (1357333, 132), (2010881, 148), (4652507, 154)]
    # next one (>10000000, >154)
    '''


def t1():
    for i in range(15000, 0, -1):
        if 4681//i%2 == 2047//i%2 == 703//i%2 == 3277//i%2 == 4033//i%2 == 8321//i%2 != 1 == 11521//i%2 != 14701//i%2:
        #if 8321//i%2 != 11521//i%2 == 2701//i%2 == 529//i%2 != 1 == 2047//i % 2 != 2059//i %2 != 4681//i % 2:
            print( i)
            break


def t2():
    print(is_sum_of_1_and_product_of_primes_prime(14))

        
t = guess_max_prime_gap_below_p
