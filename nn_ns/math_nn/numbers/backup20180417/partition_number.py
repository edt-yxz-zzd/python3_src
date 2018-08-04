
'''
integer partition

number of partitions of n (the partition numbers)
In number theory and combinatorics, a partition of a positive integer n,
also called an integer partition, is a way of writing n
as a sum of positive integers. Two sums that differ only
in the order of their summands are considered the same partition.
(If order matters, the sum becomes a composition.)

P(n, upper) = for [ZZ n, upper] # n = sum a[i] {0<a[i]<=upper}
    def:
    = [n=upper=0] if [upper <= 0] or [n < 0]
    = P(n, upper-1) + P(n-upper, upper) if [upper > 0][n>=0]

    calc:
    = 0 if [n < 0]
    = [n=upper=0] elif [upper <= 0]
    # = 1 elif [n=0] or [upper = 1]
    = P(n, n) elif [upper > n]
    = P(n, upper-1) + P(n-upper, upper) else
    

from Concrete Abstract Algebra(N Lauritzen,2003)::
    2.10.2 Conjugacy classes in the symmetric group::[page 100]
    from Introductio in Analysin Injnitorum (1748)(Euler)
    P[n] ::=
        = 0 if n < 0
        = 1 if n == 1
        = sum (-1)^(k+1) * (P[n-(3*k*k-k)/2] + P[n-(3*k*k+k)/2]) {N+ k} else
        // = P[n-1] + P[n-2] - P[n-5] - P[n-7] + P[n-12] + P[n-15] - ...
    

'''


__all__ = '''
    partition_number
'''.split()

from .numberss import NumberList, NumberList__neg2zero
from .numberss import NumberTable


def check_partition_number(partition_number):
    assert partition_number(-1) == 0
    try:
        assert partition_number.get_first(20) == \
               [1, 1, 2, 3, 5,          7, 11, 15, 22, 30,
                42, 56, 77, 101, 135,   176, 231, 297, 385, 490]
    except AssertionError:
        print(partition_number.get_first(20))
        raise

class BoundedPartitionNumber(NumberTable):
    def _calc_neg(self, n, k, table):
        return 0
        raise NotImplementedError
    def _calc_pos(self, n, upper, table):
        if n == 0:
            return 1
        if upper == 0:
            return 0

        assert 0 < upper <= n
        return table[n][upper-1] + table[n-upper][min(upper, n-upper)]
        raise NotImplementedError
    def _calc_pos_beyond(self, n, upper, table):
        return 0 if upper < 0 else table[n][n]
        raise NotImplementedError
    def direct_calc(self, n, k):
        raise NotImplementedError
    def row_len(self, n):
        return n+1
        
    def __init__(self):
        super().__init__([[1]])
    
bounded_partition_number = BoundedPartitionNumber()



class PartitionNumber__dynamic(NumberList):
    def _calc_neg(self, n, nums):
        return bounded_partition_number(n,n)
        raise NotImplementedError
    def _calc_pos(self, n, nums):
        return bounded_partition_number(n,n)
        raise NotImplementedError
    def direct_calc(self, n):
        raise NotImplementedError
    def _fill_when_neg(self, n):
        pass

    
    def __init__(self):
        super().__init__([])

partition_number__dynamic = PartitionNumber__dynamic()
check_partition_number(partition_number__dynamic)





class PartitionNumber__Euler(NumberList__neg2zero):
    def _calc_pos(self, n, nums):
        assert n > 0
        p = 0
        positive = True
        for k in range(1, n+1):
            d1 = (3*k*k - k)//2
            d2 = d1 + k # (3*k*k + k)//2
            for d in [d1, d2]:
                if d > n:
                    return p
                if positive:
                    p += nums[n-d]
                else:
                    p -= nums[n-d]
            positive = not positive

        raise ...
        raise NotImplementedError

    
    def __init__(self):
        super().__init__([1])
partition_number__Euler = PartitionNumber__Euler()
check_partition_number(partition_number__Euler)

partition_number = partition_number__Euler

'''
bounded_partition_number_table = []
def get_bounded_partition_number_from_incomplete_table(n, upper, table):
    #this_f = get_bounded_partition_number_from_incomplete_table
    
    if n < 0 or upper < 0:
        return 0
    
    if upper > n:
        upper = n
        
    assert 0 <= upper <= n
    return table[n][upper]


def fill_next_row_of_bounded_partition_number_table(table):
    n = len(table)
    get = lambda n, upper: get_bounded_partition_number_from_incomplete_table(n, upper, table)
    
    ls = []
    table.append(ls)
    
    upper = 0
    ls.append(int(n==0))
    
    for upper in range(1, n+1):
        p = get(n, upper-1) + get(n-upper, upper)
        ls.append(p)
    assert len(ls) == n+1
    assert len(table) == n+1
    return

    
def bounded_partition_numberss_of_least_len(L):
    table = bounded_partition_number_table
    fill = fill_next_row_of_bounded_partition_number_table
    
    for n in range(len(table), L):
        fill(table)
    assert len(table) >= L
    return table

def bounded_partition_numberss(n=None, upper=None):
    if n == None:
        bounded_partition_numberss_of_least_len(0)

    if upper == None:
        assert n >= 0
        return bounded_partition_numberss_of_least_len(n+1)[n]

    table = bounded_partition_numberss_of_least_len(n+1)
    return get_bounded_partition_number_from_incomplete_table(n, upper, table)


partition_number_list = []
def partition_numbers_of_least_len(L):
    ls = partition_number_list

    for n in range(len(ls), L):
        p = bounded_partition_numberss(n,n)
        ls.append(p)
    assert len(ls) >= L

    return ls


def partition_numbers(n=None):
    if n == None:
        return partition_numbers_of_least_len(0)
    if n < 0:
        return 0
    return partition_numbers_of_least_len(n+1)[n]


def partition_numbers_first(N):
    return partition_numbers_of_least_len(N)[:N]


assert partition_numbers_first(20) == \
       [1, 1, 2, 3, 5,          7, 11, 15, 22, 30,
        42, 56, 77, 101, 135,   176, 231, 297, 385, 490]

'''


'''
########### old version VVVVVVVVVVVVVVVVv


##    f(n, m)
##    = 1 if 1 = m <= n
##      f(n, n) if 1 <= n < m
##      1 + f(n, n-1) if 1 < n = m
##      f(n, m-1) + f(n-m, m) if 1 < m < n

def partition_numbers(n):
    assert n > 0

    table = [None]*n
    table[1-1] = [1]

    for i in range(2, n+1):
        ls = table[i-1] = [None]*i

        for j in range(i):
            ls[j] = integer_partition_le(i, j+1, table)
            

    return tuple(ls[-1] for ls in table)


def at_table(table, n, m):
    if m > n:
        m = n
    return table[n-1][m-1]

def integer_partition_le(n, m, table):
    assert n > 0
    assert m > 0

    if m == 1:
        return 1
    if m > n:
        return at_table(table, n, n)
    if m == n:
        return 1 + at_table(table, n, n-1)

    assert len(table) >= n > m > 1
    return at_table(table, n, m-1) + at_table(table, n-m, m)



########### old version ^^^^^^^^^^^^^^^^^^^^^^^^
'''


def t(n = 100):
    print(partition_numbers_first(n))


    
