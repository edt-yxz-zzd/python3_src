


##Josephus problem
##From Wikipedia, the free encyclopedia
##In computer science and mathematics,
##the Josephus Problem (or Josephus permutation)
##is a theoretical problem related to a certain counting-out game.
##
##There are people standing in a circle waiting to be executed.
##The counting out begins at some point in the circle and
##proceeds around the circle in a fixed direction. In each step,
##a certain number of people are skipped and the next person is executed.
##The elimination proceeds around the circle (which is becoming smaller and
##smaller as the executed people are removed), until only the last person remains,
##who is given freedom.
##
##The task is to choose the place in the initial circle
##so that you are the last one remaining and so survive.

'''
[0..n-1]
1st round killed k-1..x*k-1...
if k|n, then n-1 is killed in this round
0 will again be the beginner.
now there are n_2 = n-(n/k)
if k|n[i] and n[i+1] = n[i] - n[i]/k, n[i+1] = (k-1)/k*n[i], n[?] = (k-1)^?
let n = k^t
'''

CHAR_BIT = 8


def check(k, n):
    if not (type(n) == int == type(k)):
        print('type(n)==', type(n), ', type(k)==', type(k))
        raise 'k & n should be integers in Josephus_problem'
    elif n < 1 or k < 1:
        print('k = ', k, ', n = ', n)
        raise 'k & n should be a positive integers in Josephus_problem'

def Josephus_problem(k, n):
    '''n person in circle numbered from 0 to n-1, counting-out the k-th person.
    which one will remains?'''

    check(k, n)
    if k == 1:
        return Josephus_problem_k_is_1(n)
    elif k == 2:
        return Josephus_problem_k_is_2(n)
    elif n > 10*k:
        # first round
        assert(k > 1 and k-1 < n)
        dn = (n+k-1) // k # dn <= (n+k-1)/2 < n
        n_ = n - dn # next n, n_ > 0
        idx_ = (k * dn) % n - 1 # the index of the last out one in 1st round. begin from 0
        # the index of the first out person is k-1, since k-1 < n
        # note that idx_ == -1 is needed
        #if not (-1 <= idx_ < k-1 < n):
        #    print(idx_, k, n)
        assert(-1 <= idx_ < k-1 < n)

        # pad the answer of (k, n_) with the number of persons skiped 
        a_ = Josephus_problem(k, n_)
        min_gap = k-2 - idx_ # after 1st round, each gap is either (k-1) or min_gap
        b = a_ + (k-1) - min_gap  #  [min_gap,k-1...,k-1], a_ is in one of these gaps, 
        a = (idx_ + 1) + (a_ + b // (k-1)) # [(x+min_gap)=k-1,k-1...k-1,..a_ is here,...], how many (k-1) before a_?
        a %= n
        return a
    else:
        return Josephus_problem_dynamic(k, n)


def Josephus_problem_k_is_1(n):
    check(1, n)
    return n - 1

def Josephus_problem_k_is_2(n):
    check(2, n)
    return (n << 1) - (1 << n.bit_length())


def Josephus_problem_dynamic_when_n_is_big(k, n):
    #raise 'unimpliment'
    # first round
    assert(k > 1 and k-1 < n)
    dn = (n+k-1) // k       # dn <= (n+k-1)/2 < n, number of persons out in 1st round
    n_ = n - dn             # next n, n_ > 0, number of remainders in next round
    idx_ = (k * dn) % n - 1 # the index of the last out one in 1st round. begin from 0
    # the index of the first out person is k-1, since 0 < k-1 < n
    # note that idx_ == -1 is needed
    #if not (-1 <= idx_ < k-1 < n):
    #    print(idx_, k, n)
    assert(-1 <= idx_ < k-1)

    # pad the answer of (k, n_) with the number of persons skiped 
    a_ = Josephus_problem(k, n_)
    min_gap = k-2 - idx_ # after 1st round, each gap is either (k-1) or min_gap
    b = a_ + (k-1) - min_gap  #  [min_gap,k-1...,k-1], a_ is in one of these gaps, 
    a = (idx_ + 1) + (a_ + b // (k-1)) # [(x+min_gap)=k-1,k-1...k-1,..a_ is here,...], how many (k-1) before a_?
    a %= n
    return a



def Josephus_problem_dynamic(k, n):
    check(k, n)
    #if n == 1:
    #    return 0
    #return (Josephus_problem_dynamic(k, n-1) + k) % n
    # RuntimeError: maximum recursion depth exceeded while calling a Python object
    # Josephus_problem_dynamic(3, 999) !!!!!!!!!!!!!

    ans = 0 # for n == 1
    for n_ in range(2, n+1):
        ans = (ans + k) % n_

    return ans
    


def Josephus_problem_dynamic_list(k, n, ls_n): # ls[i] = Josephus_problem(k,i+1)
    check(k, n)
    if len(ls_n) >= n:
        return ls_n[n-1]

    if ls_n == []:
        ls_n.append(0) # n == 1
        
    for n_ in range(len(ls_n)+1, n+1):
        ls_n.append((ls_n[-1] + k) % n_)

    return ls_n[-1]


def Josephus_problem_dynamic_when_k_div_n(k, n):
    raise 'unimpliment'
    check(k, n)
    power = get_power_of_factor(k, n)
    



def get_power_of_factor_definition(f, n):
    assert(f > 1)
    assert(n != 0)
    
    p = 0
    while n % f == 0:
        n //= f;
        p += 1

    return p


def get_power_of_factor(factor, number):
    '''
    assert(number != 0, factor >= 2)
    number = factor**power * other, other%factor != 0
    '''
    assert(number != 0)
    assert(factor >= 2)
    if number % factor != 0:
        return 0

    power = 0
    fs = [factor] # fs[i] == factor**(2**i)
    i = 0
    two_pow_i = 2**i # two_pow_i == 2**i
    while number % fs[i] == 0:
        number //= fs[i]
        power += two_pow_i
        fs.append(fs[i]**2)
        i += 1
        two_pow_i <<= 1

    for i in range(i-1, -1, -1):
        two_pow_i >>= 1
        if number % fs[i] == 0:
            number //= fs[i]
            power += two_pow_i

    return power



def Josephus_problem_definition(k, n):
    check(k, n)
    
    import array
    stack = array.array('L')
    item_bit_size = stack.itemsize * CHAR_BIT
    item_max = (1 << item_bit_size) - 1
    if item_bit_size < n.bit_length() or n >= item_max: # i = 0; i < max; ++i
        raise 'out of range: n is too large...'

    stack.extend(range(1,n+1))
    stack[-1] = 0  # stack[i] point to the index of next man that is (i+1)%n 
    assert(len(stack) == n)

    pre_i = n-1 
    i = stack[pre_i] # i == stack[pre_i] holds
    while(stack[i] != i):
        for t in range(k-1): i,pre_i = stack[i], i # skip (k-1) persons
        stack[pre_i] = stack[i] # drop i-th person
        i = stack[pre_i]

    return i
    





##############################
#####        test        #####
##############################


def test_Josephus_problem_definition():
    ns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    ms = [0, 0, 2, 0, 2, 4, 6, 0, 2, 4, 6, 8, 10, 12, 14, 0]
    #[1, 1, 3, 1, 3, 5, 7, 1, 3, 5, 7, 9, 11, 13, 15, 1]
    k = 2

    for m,n in zip(ms, ns):
        if m != Josephus_problem_definition(k, n):
            print('error: Josephus_problem_definition(', k, ', ', n, ') = ', Josephus_problem_definition(k, n), ' != ', m)
            return



def test_Josephus_problem_dynamic():
    for n in range(1, 200):
        for k in range(1, 5):
            if Josephus_problem_dynamic(k, n) != Josephus_problem_definition(k, n):
                print('error: Josephus_problem_dynamic(', k, ', ', n, ') = ', Josephus_problem_dynamic(k, n), ' != ', Josephus_problem_definition(k, n))
                return


def test_Josephus_problem():
    for n in range(1, 1000):
        for k in range(1, 50):
            if Josephus_problem(k, n) != Josephus_problem_dynamic(k, n):
                print('error: Josephus_problem(', k, ', ', n, ') = ', Josephus_problem(k, n), ' != ', Josephus_problem_dynamic(k, n))
                return




def test_Josephus_problem_dynamic_list():
    max_n = 1000
    for k in range(1, 50):
        ls_n = []
        Josephus_problem_dynamic_list(k, max_n, ls_n)
        for n in range(1, max_n):
            if Josephus_problem_dynamic_list(k, n, ls_n) != Josephus_problem(k, n):
                print('error: Josephus_problem_dynamic_list(', k, ', ', n, ') = ', Josephus_problem_dynamic_list(k, n, ls_n), ' != ', Josephus_problem(k, n))
                return







def test_get_power_of_factor_definition():
    td = [ # f, n, p \ 
        (2, 1, 0), \
        (2, 2, 1), \
        (2, 3, 0), \
        (2, 4, 2), \
        (2, 5, 0), \
        (2, 6, 1), \
        (2, 7, 0), \
        (2, 8, 3), \
        (2, 9, 0), \
        (3, 1, 0), \
        (3, 2, 0), \
        (3, 3, 1), \
        (3, 4, 0), \
        (3, 5, 0), \
        (3, 6, 1), \
        (3, 7, 0), \
        (3, 8, 0), \
        (3, 9, 2), \
        (3, 10, 0), \
        (3, 11, 0), \
        (3, 12, 1), \
        (3, 13, 0), \
        (3, 14, 0), \
        (3, 15, 1), \
        (3, 27, 3), \
        (3, 81*59, 4), \
        (3, 578*(3**7)**2, 14), \
        ]
    for f,n,p in td:
        if get_power_of_factor_definition(f, n) != p:
            print('get_power_of_factor_definition(', f, ', ', n, ') != ', p)
            return


def test_get_power_of_factor():
    for f in range(2, 5):
        for n in range(1, 2000):
            if get_power_of_factor(f, n) != get_power_of_factor_definition(f, n):
                print('get_power_of_factor(', f, ', ', n, ') != ', get_power_of_factor_definition(f, n))
                return




    








