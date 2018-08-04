"""
file::= 'prime.py'

prime(n)::= yields out a list of primes in [2, n)
min_prime_factor(n)::=
    MPF(n)[i] == the min-prime-factor of i for i in [2,n)
                    but [0,1] for i in [0,2)

min_prime_factor_at_least
factor_power_pairs_of_positive_integer

"""


import math, fractions, time
import itertools #groupby


def pick_up_value_that_eq_index( table, offset):
    vs = []
    for i in range( len( table)):
        v = table[i]
        if i + offset == v:
            vs.append( v)

    return vs



def pick_up_index_with_value_eq( value, table):
    indexs = []
    for i in range( len( table)):
        v = table[i] 
        if value == v:
            indexs.append( i) 

    return indexs



min_prime_factor_ls = [i for i in range(2)]
def min_prime_factor_at_least(n):
    global min_prime_factor_ls
    assert len(min_prime_factor_ls) >= 2
    if n > len(min_prime_factor_ls):
        min_prime_factor_ls = __min_prime_factor(n*2)
    return min_prime_factor_ls

def min_prime_factor(n):
    return min_prime_factor_at_least(n)[:n]

def __min_prime_factor(n):
    if type( n) != int:
        raise TypeError( 'let n be an integer!')
        
    #if not n > 1: raise ValueError( 'let n > 1!')

    #c0 = c1 = c2 = c3 = 0
    factor = list( range( n))
    for i in range( 2, n): # may change to [2:sqrt(n)+1]?
        #c0 += 1 # c0 == n-2
        if factor[i] < i:
            continue # assert not is_prime(i)

        #c1 += 1 # c1 == number-of-primes-below(n) = NoPrm(n)
        t = (n-1) // i
        for j in range( i*t, i*i-1, -i):
            #c2 +=1 # c2 == c1*avg(t-i+1)
            #       == sum n//p - p + 1 for p in prime(sqrt(n))
            #       == sum NoPrm(n//j) for j in [2,n)
            if factor[j] == j:
                #c3 += 1 # c3 == n-2-c1
                factor[j] = i

    #assert c0 == n-2, c1 + c3 == n-2
    #return ( c0+c1+c2+c3) # == 2*(n-2) + c2
    #return c2
    #return 2*(n-2) + c2
    return factor
    """
    n = 10          excute_count = 20           c/n = 2.0
    n = 100         excute_count = 298          c/n = 2.98
    n = 1000        excute_count = 3405         c/n = 3.405
    n = 10000       excute_count = 36975        c/n = 3.6975
    n = 100000      excute_count = 393072       c/n = 3.93072
    n = 1000000     excute_count = 4122042      c/n = 4.122042
    n = 10000000    excute_count = 42850045     c/n = 4.2850045
    """



def prime( n):
    factors = min_prime_factor(n)
    factors[0:2] = [-1,-1]
    """
    p = []
    for i in range( 2, n):
        if factors[i] == i:
            p.append(i)

    return p
    """
    return pick_up_value_that_eq_index( factors, 0)

    
def factor_power_pairs_of_positive_integer(N, mpf=None):
    factor_power_pairs = pack_factors(factor_with_mpf(N, mpf))
    return factor_power_pairs


def factor_with_mpf(N, mpf=None):
    if mpf == None:
        mpf = min_prime_factor_at_least(N+1)
    return __factor_with_mpf( N, mpf)

def __factor_with_mpf( N, mpf):
    factors = []
    while( N > 1):
        f = mpf[ N]
        assert f > 1
        factors.append( f)
        N //= f

    return factors



def pack_factors( factors):
    assert factors == [] or 1 < factors[0]
    for i in range( 1, len( factors)):
        assert factors[i-1] <= factors[i]

    """
    factor_powers = []
    i = 0
    L = len( factors)
    for f in set( factors): # THE set IS OUT OF ORDER!!
        c = i
        while( i < L and factors[i] == f):
            i += 1

        p = i - c
        factor_powers.append( [f,p])
    """


    factor_powers = []
    pre_f = 2
    c = 0
    for f in factors:
        if f != pre_f:
            assert pre_f < f
            factor_powers.append( [pre_f,c])
            pre_f = f
            c = 1
        else:
            c += 1
            
    factor_powers.append( [pre_f,c])
    if factor_powers[0][1] == 0:
        return factor_powers[1:]
    
    return factor_powers

def pack_factors(factors):
    assert factors == [] or 1 < factors[0]
    for i in range( 1, len( factors)):
        assert factors[i-1] <= factors[i]

    ls = []
    for factor, group in itertools.groupby(factors):
        power = len(tuple(group))
        ls.append((factor, power))
    return ls






def factor_powers2int( factor_powers):
    i = 1
    for fp in factor_powers:
        i *= fp[0]**fp[1]

    return i
        


def factor_power2str( factor_power):
    assert len( factor_power) == 2

    #s = str( factor_power[0])
    #if factor_power[1] > 1:
    #    s += '^' + str( factor_power[1])
        
    #return s

    if factor_power[1] > 1:
        return '{0}^{1}'.format( *factor_power)
    else:
        return str( factor_power[0])



def factor_powers2str( factor_powers):
    s = ''
    for f_p in factor_powers:
        s += factor_power2str( f_p) + '*'

    return s[:-1]  # note: ''[:-1] == ''



def str_of_expending_N( N, mpf):
    factors = factor_with_mpf( N, mpf)
    factor_powers = pack_factors( factors)
    assert N == factor_powers2int( factor_powers)

    
    s = str( N) + '=' + factor_powers2str( factor_powers)
    return s



def factor_table_below_N( N):
    mpf = min_prime_factor( N+1)
    s = ''
    for i in range( 2, N+1):
        s += str_of_expending_N( i, mpf) + '\n'

    return s



 #("""E:\my_data\program_output\python_prime""", 1000000)

def create_file_of_factor_table_below_N( dir_path, N):
    file_name = 'factor_table_below_' + str( N) + '.txt'
    path = dir_path + '/' + file_name
    with open( path, 'w') as f:
        f.write( factor_table_below_N(N))


    
def prime_table_below_N( N, width):
    primes = prime_delta( N+1, 10**6)
    s = ''
    for p in primes:
        s += '{prime: <{width}} '.format( prime = p, width = width)

    return s



 #("""E:\my_data\program_output\python_prime""", 1000000, 7)

def create_file_of_prime_table_below_N( dir_path, N, width):
    file_name = 'prime_table_below_' + str( N) + '.txt'
    path = dir_path + '/' + file_name
    with open( path, 'w') as f:
        f.write( prime_table_below_N( N, width))



def get_mth_prime( m):
    if m < 1:
        return
    
    N = 32
    primes = prime( N)
    while( len( primes) < m):
        N *= 2
        primes = prime( N)

    return primes[m-1]



def get_first_m_primes( m):
    if m < 1:
        return []
    else:
        return prime( get_mth_prime( m) + 1)




def phi_of_product_primes( m):
    mth_prime = get_mth_prime( m)
    primes = prime( mth_prime + 1)
        
    phi = product = 1
    for p in primes:
        product *= p
        phi *= p-1

    return mth_prime, phi, product, phi/product
    #phi_of_product_primes(6) == (13, 5760, 30030, 0.1918081918081918)



def min_prime_factor_skip(n,m):
    if not ( 0 <= m and m < 8):
        raise ValueError( 'let 0 <= m < 8!')

    if m == 0:
        return min_prime_factor( n)

    
    first_m_primes = get_first_m_primes( m)
    phi = period = 1
    for p in first_m_primes:
        period *= p
        phi *= p-1

    coprimes = []
    for k in range( period):
        if fractions.gcd( k, period) == 1:
            coprimes.append( k)

    assert phi == len( coprimes)
    assert coprimes[-1] == period - 1

    coprime2index = list( range( period))
    coprime2index[0] = -1
    coprime2index[-1] = phi - 1
    for i in range( phi-1):
        # fill coprime2index[ coprimes[i]:coprimes[i+1]] with coprime2index[ coprimes[i]-1] + 1
        index = coprime2index[ coprimes[i] - 1] + 1
        for j in range( coprimes[i], coprimes[i+1]):
            coprime2index[j] = index

    #return coprimes, coprime2index

    def number2index( num): return num // period * phi + coprime2index[ num % period]
    
    def index2number( index): return index // phi * period + coprimes[ index % phi]
    
    length = number2index( n-1) + 1; #print( 'length = {0}'.format( length))
    min_factor_of_num = list( range( length))
    for i in range( length):
        min_factor_of_num[i] = 0

    min_factor_of_num[0] = 1 # min_factor_of_num[index] ::= min-factor-of number[index]

    num_steps = []
    for i in range( phi-1):
        num_steps.append( coprimes[i+1] - coprimes[i])

    num_steps.append( 2) # == (period + 1) - (period - 1)
    #return num_steps
    #num = 1
    for num_idx in range( length):
        if min_factor_of_num[ num_idx] == 0:
            # num is a prime
            prime = index2number( num_idx) # == num
            min_factor_of_num[ num_idx] = prime
            prime_times_indexs = []
            for coprime in coprimes: # phi/period
                prime_times_indexs.append( number2index( prime*coprime))

            prime_times_indexs.append( number2index( prime*(1+period)))
            ptimes_index_steps = []
            for i in range( phi):
                ptimes_index_steps.append( prime_times_indexs[i+1] - prime_times_indexs[i])
            
            prime_times_indexs = 0 # delete
            prime_times = prime**2 # p^2 to n - 1 step p
            prime_times_index = number2index( prime_times)
            ptimes_idx_step_idx = number2index( prime) % phi 
            while( prime_times_index < length):
                if min_factor_of_num[ prime_times_index] == 0:
                    min_factor_of_num[ prime_times_index] = prime

                prime_times_index += ptimes_index_steps[ ptimes_idx_step_idx]
                ptimes_idx_step_idx += 1
                if ptimes_idx_step_idx == phi:
                    ptimes_idx_step_idx = 0

        #num += num_steps[ num_idx % phi]

    return min_factor_of_num

                

def test_min_prime_factor_skip():
    for n in [31, 32, 100000]:
        print( '\n{0} ::'.format(n), end = ' ')
        for m in range( 7):
            print( '{0}'.format(m), end = ' ')
            if m == 0:
                assert min_prime_factor( n) == min_prime_factor_skip( n,m)
                continue
            
            mpf = min_prime_factor( n)
            mth_prime = get_mth_prime( m)
            mpf_skip1 = [1]
            for f in mpf:
                if f > mth_prime:
                    mpf_skip1.append( f)

            mpf = 0 # delete
            mpf_skip2 = min_prime_factor_skip( n, m)
            #print( mpf_skip1, mpf_skip2)
            assert mpf_skip1 == mpf_skip2



def show_time_of_min_prime_factor_skip():
    n = 1000000
    dt = []
    for m in range(5):
        t0 = time.clock()
        mpf = min_prime_factor_skip( n, m)
        t1 = time.clock()
        mpf = 0
        dt.append( t1 - t0)

    return dt
    #[0.7384737713819061,
    #1.1636859104839699,
    #0.9811869037978558,
    #1.4765248040129388,
    #5.323146388320486]



def min_prime_factor_between( a, b, primes_below):
    if type( a) != int or type( b) != int:
        raise TypeError( 'let a & b be integers!')
    elif type( primes_below) != list:
        raise TypeError( 'let primes_before_a be a list!')
    elif not ( 1 < a):
        raise ValueError( 'let 1 < a')
    #elif len( primes_below) > 0 and primes_below[-1] >= a:

    factors = list( range( a, b))
    length = len( factors) # == b - a if a<=b
    for p in primes_below:
        if p >= a or 2*p > b:
            break
        # k = (p-a%p)%p
        k = (-a) % p
        for i in range( k, length, p):
            if i + a == factors[i]:
                factors[i] = p

    for i in range( length):
        n = i + a
        if n*n - a > length: # no matter n is a prime or not, the code below is meanless
            break
        
        if n != factors[i]:
            continue

        p = n # is a prime
        for j in range( p*p - a, length, p):
            if j + a == factors[j]:
                factors[j] = p

    return factors



def NEST_min_prime_factor_delta( n, delta, mpf_or_primes):
    mpf = [0,1]
    t = n // delta
    a = 2
    b = delta
    primes_below = []
    for i in range( t):
        mpfb = min_prime_factor_between( a, b, primes_below)
        primes_below += pick_up_value_that_eq_index( mpfb, a)
        mpf += mpfb
        a = b
        b += delta

    b = n
    mpfb = min_prime_factor_between( a, b, primes_below)
    primes_below += pick_up_value_that_eq_index( mpfb, a)
    mpf += mpfb
    mpf = mpf[:n]

    if mpf_or_primes == -1:
        return mpf, primes_below
    elif mpf_or_primes == 0:
        return mpf
    elif mpf_or_primes == 1:
        return primes_below

    return



def min_prime_factor_delta( n, delta):
    return NEST_min_prime_factor_delta( n, delta, 0)
      


def prime_delta( n, delta):
    #return NEST_min_prime_factor_delta( n, delta, 1)
    t = n // delta
    a = 2
    b = delta
    primes_below = []
    for i in range( t):
        mpfb = min_prime_factor_between( a, b, primes_below)
        primes_below += pick_up_value_that_eq_index( mpfb, a)
        a = b
        b += delta

    b = n
    mpfb = min_prime_factor_between( a, b, primes_below)
    primes_below += pick_up_value_that_eq_index( mpfb, a)
    return primes_below

    

def test_min_prime_factor_between():
    primes_below = []
    for n in list( range( 32)) + [100000]:
        assert min_prime_factor_between( 2, n, primes_below) == min_prime_factor(n)[2:]


    t = 5
    delta = 10000
    for n in list( range( 33)) + [ delta, delta+34, t*delta, t*delta+12]:
        mpf1 = min_prime_factor_delta( n, delta)
        mpf2 = min_prime_factor( n)
        ps1 = prime_delta( n, delta)
        ps2 = prime( n)
        assert mpf1 == mpf2
        assert ps1 == ps2





def prime_bytearray( n):
    isnt_prime = bytearray( n)
    isnt_prime[0:2] = [1,1]
    if n < 2:
        isnt_prime = isnt_prime[:n]
        
    for i in range(n):
        if isnt_prime[i] == 1:
            continue

        prime = i
        for j in range( prime**2, n, prime):
            if isnt_prime[j] == 0:
                isnt_prime[j] = 1

    #print( isnt_prime)
    return pick_up_index_with_value_eq( 0, isnt_prime)



def test_prime_bytearray():
    for n in list( range( 33)) + [10000, 100000]:
        assert prime_bytearray( n) == prime(n)

    dt = []
    for n in [100, 1000, 10000, 100000, 1000000, 10000000]:
        t0 = time.clock()
        pb = prime_bytearray(n)
        pb = 0
        t1 = time.clock()
        p = prime(n)
        p = 0
        t2 = time.clock()
        dt.append( (n, t1-t0, t2-t1))

    return dt
    '''
    [(100, 0.00013683962054373224, 0.00010360714126882582),
     (1000, 0.000890434959395286, 0.0008865252559511795),
     (10000, 0.008786081064768636, 0.008842771764708183),
     (100000, 0.08878447808635656, 0.09396043673342322),
     (1000000, 0.8960243691815671, 1.0093021619193907),
     (10000000, 9.202583727521038, 10.451135304573228)]
     '''





    
    
