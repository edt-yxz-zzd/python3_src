
'''
Pascal_number(n,k) = binomial(n,k) = C(n,k)
Stirling_circle(n,k) = Stirling[n,k] = Stirling number of first kind
Stirling_subset_number(n,k) = Stirling{n,k} = Stirling number of second kind
Eulerian_1st(n,k) = Eulerian<n,k> = Eulerian numbers of first order
Eulerian_2nd(n,k) = Eulerian<<n,k>> = Eulerian numbers of second order



C(n,k)          = C(n-1,k-1)                   + C(n-1,k)
Stirling[n,k]   = Stirling[n-1,k-1]            + Stirling[n-1,k]   (n-1)
Stirling{n,k}   = Stirling{n-1,k-1}            + Stirling{n-1,k}   k
Eulerian<n,k>   = Eulerian<n-1,k-1>   (n-k)    + Eulerian<n-1,k>   (k+1)
Eulerian<<n,k>> = Eulerian<<n-1,k-1>> (2n-1-k) + Eulerian<<n-1,k>> (k+1)

Stirling[n,k] = Stirling{-k,-n}


extend:
Eulerian<<n,k>> = 0 for [int n,k][k<0]
# compare Eulerian<<-n,k>> and Eulerian<n+k,k>
# that is Eulerian<<-n+k,k>> and Eulerian<n,k>
let TN_Eulerian<<n,k>> = Eulerian<<-n+k,k>>
# Eulerian<<n,k>> = TN_Eulerian<<k-n,k>>
# TN_Eulerian<<k-n,k>> = TN_Eulerian<<k-n,k-1>> (2n-1-k) + TN_Eulerian<<k-n+1,k>> (k+1)
# TN_Eulerian<<n,k>> = TN_Eulerian<<n,k-1>> (2(k-n)-1-k) + TN_Eulerian<<n+1,k>> (k+1)
# TN_Eulerian<<n,k>> = TN_Eulerian<<n,k-1>> (k-2n-1) + TN_Eulerian<<n+1,k>> (k+1)
# TN_Eulerian<<n,k>> + TN_Eulerian<<n,k-1>> (2n+1-k) = TN_Eulerian<<n+1,k>> (k+1)
TN_Eulerian<<n+1,k>> = TN_Eulerian<<n,k>>/(k+1) + TN_Eulerian<<n,k-1>> (2n+1-k)/(k+1)
    for [int n,k][k>=0]
TN_Eulerian<<n,k>> = Eulerian<<-n+k,k>> = 0 if [int n,k][k < 0]
TN_Eulerian<<0,k>> = Eulerian<<k,k>> = [k=0]
TN_Eulerian<<n,k>> = 0 if [int n,k][k>n>0]
TN_Eulerian<<n+1,n+1>> = 0 + TN_Eulerian<<n,n>> (n)/(n+2) = 0 if [int n>=0]
TN_Eulerian<<n,n>> = 0 if [int n][n>0] = [n=0]
TN_Eulerian<<n,k>> = TN_Eulerian<<n-1,k-1>> (2n-1-k)/(k+1) + TN_Eulerian<<n-1,k>>/(k+1)
    for [int n,k][k>=0]
TN_Eulerian<<n,n-1>> = TN_Eulerian<<n-1,n-2>>n/n + TN_Eulerian<<n-1,n-1>>/n for [n>0]
    = TN_Eulerian<<n-1,n-2>> + [n=1] for [n>0]
    = 1 for [n>0] = [n>0]
TN_Eulerian<<n,0>> = 0 + TN_Eulerian<<n-1,0>>/(0+1) = TN_Eulerian<<n-1,0>> = 1 for [int n]
TN_Eulerian<<n,1>> = TN_Eulerian<<n-1,0>> (2n-2)/2 + TN_Eulerian<<n-1,1>>/2
    = n-1 + TN_Eulerian<<n-1,1>>/2
    = Eulerian<<1-n,1>> = 2**(2-n) - 2(2-n)
    = 4/2**n - 4 + 2n = 4(2**-n -1+n/2) for [int n]
    try: right = n-1 + (4/2**(n-1) - 4 + 2(n-1))/2 = n-1 + 4/2**n - 2 + n-1 = 4/2**n - 4 + 2n = left
    Eulerian<n,1> = 2**n - (n+1)
    Eulerian<<n,1>> = TN_Eulerian<<1-n,1>> = 4(2**-(1-n) -1+(1-n)/2)
    = 2(2**n -1-n) = 2 Eulerian<n,1>
    
S k x n = sum i**k x**i {i=0->n} = ??

'''

from fractions import Fraction

table_obj_names = ('Pascal_number Stirling_circle Stirling_subset '
                   'Eulerian_1st Eulerian_2nd TN_Eulerian_2nd'.split())
__all__ = table_obj_names + \
          ('Pascal_numbers_like_table Pascal_numbers_like_coeffs'.split())


class Pascal_numbers_like_table:
    def __init__(self, coeff_n_1_k_1, coeff_n_1_k, row0 = None):
        row0 = (1,) if row0 is None else row0
        self.table = [list(row0)]
        self.coeff_n_1_k_1 = coeff_n_1_k_1
        self.coeff_n_1_k = coeff_n_1_k

    def _init_via_coeffs(self, coeffs, row0 = None):
        Pascal_numbers_like_table.__init__(self, coeffs.n_1_k_1, coeffs.n_1_k, row0)
        
    def next_row(self, pre_row):
        n = len(pre_row)
        assert n > 0
        
        ls = [0 + pre_row[0]*self.coeff_n_1_k(n, 0)] # nth row
        for k in range(1, n):
            N_n_k = pre_row[k-1]*self.coeff_n_1_k_1(n, k) + pre_row[k]*self.coeff_n_1_k(n, k)
            ls.append(N_n_k)
        ls.append(pre_row[n-1]*self.coeff_n_1_k_1(n, n) + 0)


        assert len(ls) == n+1
        return ls

    def fill_table(self, n):
        table = self.table
        next_row_f = self.next_row
        
        assert n >= 0
        assert table

        pre_row = table[-1]
        i = len(table)
        for i in range(i, n):
            row = next_row_f(pre_row)
            table.append(row)
            pre_row = row
        
        assert len(table) >= n
        return

    def get_number_at_neg_row(self, n, k):
        assert n < 0
        raise NotImplementedError('n < 0')

    def get_table_of_least_len(self, L):
        table = self.table
        if len(table) < L:
            self.fill_table(L)
        return table

    def row(self, n):
        table = self.get_table_of_least_len(n+1)
        return table[n]
    def __call__(self, n, k):
        if n < 0:
            return self.get_number_at_neg_row(n,k)
        
        if not (0 <= k <= n):
            return 0

        
        row_n = self.row(n)
        return row_n[k]

        






##############################################
Pascal_number_coeff = lambda n,k: 1
class Pascal_numbers_like_coeffs:
    n_1_k_1 = Pascal_number_coeff
    n_1_k = Pascal_number_coeff

class Pascal_number_coeffs(Pascal_numbers_like_coeffs):
    pass
class Stirling_circle_coeffs(Pascal_numbers_like_coeffs):
    n_1_k = lambda n,k: n-1
class Stirling_subset_coeffs(Pascal_numbers_like_coeffs):
    n_1_k = lambda n,k: k
class Eulerian_1st_coeffs(Pascal_numbers_like_coeffs):
    n_1_k_1 = lambda n,k: n-k
    n_1_k = lambda n,k: k+1
class Eulerian_2nd_coeffs(Pascal_numbers_like_coeffs):
    n_1_k_1 = lambda n,k: 2*n-1-k
    n_1_k = lambda n,k: k+1
class TN_Eulerian_2nd_coeffs(Pascal_numbers_like_coeffs):
    n_1_k_1 = lambda n,k: Fraction(2*n-1-k, k+1)
    n_1_k = lambda n,k: Fraction(1, k+1)


        





##############################################
class Pascal_number_table(Pascal_numbers_like_table):
    def __init__(self):
        self._init_via_coeffs(Pascal_number_coeffs)
        
    def get_number_at_neg_row(self, n, k):
        assert n < 0
        if k < 0:
            return 0

        m = -(n-(k-1))
        assert m >= 0
        return Pascal_number(m, k) * (-1)**k



class Stirling_circle_table(Pascal_numbers_like_table):
    def __init__(self):
        self._init_via_coeffs(Stirling_circle_coeffs)

        
    def get_number_at_neg_row(self, n, k):
        assert n < 0
        if k > 0:
            return 0
        
        return Stirling_subset(-k, -n)

class Stirling_subset_table(Pascal_numbers_like_table):
    def __init__(self):
        self._init_via_coeffs(Stirling_subset_coeffs)

        
    def get_number_at_neg_row(self, n, k):
        assert n < 0
        if k > 0:
            return 0
        
        return Stirling_circle(-k, -n)

class Eulerian_1st_table(Pascal_numbers_like_table):
    def __init__(self):
        self._init_via_coeffs(Eulerian_1st_coeffs)
class Eulerian_2nd_table(Pascal_numbers_like_table):
    def __init__(self):
        self._init_via_coeffs(Eulerian_2nd_coeffs)
class TN_Eulerian_2nd_table(Pascal_numbers_like_table):
    def __init__(self):
        self._init_via_coeffs(TN_Eulerian_2nd_coeffs)









##############################################
table_class_names = [name + '_table' for name in table_obj_names]
table_classes = [globals()[name] for name in table_class_names]
table_objs = [cls() for cls in table_classes]

for _name, _obj in zip(table_obj_names, table_objs):
    globals()[_name] = _obj
    


_get = lambda table, L: table.get_table_of_least_len(L)[:L]
_show = lambda table, L: print(_get(table, L))

assert _get(Pascal_number, 10) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1], [1, 8, 28, 56, 70, 56, 28, 8, 1], [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]]
assert _get(Stirling_circle, 10) == [[1], [0, 1], [0, 1, 1], [0, 2, 3, 1], [0, 6, 11, 6, 1], [0, 24, 50, 35, 10, 1], [0, 120, 274, 225, 85, 15, 1], [0, 720, 1764, 1624, 735, 175, 21, 1], [0, 5040, 13068, 13132, 6769, 1960, 322, 28, 1], [0, 40320, 109584, 118124, 67284, 22449, 4536, 546, 36, 1]]
assert _get(Stirling_subset, 10) == [[1], [0, 1], [0, 1, 1], [0, 1, 3, 1], [0, 1, 7, 6, 1], [0, 1, 15, 25, 10, 1], [0, 1, 31, 90, 65, 15, 1], [0, 1, 63, 301, 350, 140, 21, 1], [0, 1, 127, 966, 1701, 1050, 266, 28, 1], [0, 1, 255, 3025, 7770, 6951, 2646, 462, 36, 1]]
assert _get(Eulerian_1st, 10) == [[1], [1, 0], [1, 1, 0], [1, 4, 1, 0], [1, 11, 11, 1, 0], [1, 26, 66, 26, 1, 0], [1, 57, 302, 302, 57, 1, 0], [1, 120, 1191, 2416, 1191, 120, 1, 0], [1, 247, 4293, 15619, 15619, 4293, 247, 1, 0], [1, 502, 14608, 88234, 156190, 88234, 14608, 502, 1, 0]]
assert _get(Eulerian_2nd, 10) == [[1], [1, 0], [1, 2, 0], [1, 8, 6, 0], [1, 22, 58, 24, 0], [1, 52, 328, 444, 120, 0], [1, 114, 1452, 4400, 3708, 720, 0], [1, 240, 5610, 32120, 58140, 33984, 5040, 0], [1, 494, 19950, 195800, 644020, 785304, 341136, 40320, 0], [1, 1004, 67260, 1062500, 5765500, 12440064, 11026296, 3733920, 362880, 0]]

assert Pascal_number.row(4) == [1, 4, 6, 4, 1]
assert Stirling_circle.row(4) == [0, 6, 11, 6, 1]
assert Stirling_subset.row(4) == [0, 1, 7, 6, 1]
assert Eulerian_1st.row(4) == [1, 11, 11, 1, 0]
assert Eulerian_2nd.row(4) == [1, 22, 58, 24, 0]


##t = _get(TN_Eulerian_2nd, 10)
##print(t)

    

def big_primes(n, row, factor_f):
    s = set(abs(i) for i in row if i)
    primes = set(prime for i in s for prime in factor_f(i))
    bigs = [p for p in primes if p > n]
    bigs.sort()
    return bigs

def _big_primes(table):
    #from sympy import factorint
    from factor_fraction import factor_fraction

    ls = []
    for n, row in enumerate(table):
        bigs = big_primes(n, row, factor_fraction)
        ls.append(bigs)
        print(n, bigs)

    return ls


def _show_big_primes(n):
    for _name, _obj in zip(table_obj_names, table_objs):
        print(_name)
        _big_primes(_get(_obj, n))

'''
_show_big_primes(10)
n = 8:
    Stirling_circle 967
    Stirling_subset 127
    Eulerian_1st 15619
    Eulerian_2nd 2477
    

Pascal_number
0 []
1 []
2 []
3 []
4 []
5 []
6 []
7 []
8 []
9 []
Stirling_circle
0 []
1 []
2 []
3 []
4 [11]
5 [7]
6 [17, 137]
7 [29]
8 [11, 23, 67, 967]
9 [13, 89, 761, 1069, 29531]
Stirling_subset
0 []
1 []
2 []
3 []
4 [7]
5 []
6 [13, 31]
7 [43]
8 [19, 23, 127]
9 [11, 17, 37, 331]
Eulerian_1st
0 []
1 []
2 []
3 []
4 [11]
5 [11, 13]
6 [19, 151]
7 [151, 397]
8 [13, 19, 53, 15619]
9 [11, 83, 157, 251, 281, 15619]
Eulerian_2nd
0 []
1 []
2 []
3 []
4 [11, 29]
5 [13, 37, 41]
6 [11, 19, 103]
7 [11, 17, 19, 59, 73]
8 [11, 13, 19, 23, 89, 103, 839, 2477]
9 [13, 17, 19, 37, 59, 89, 251, 887, 2593, 4139]
'''





