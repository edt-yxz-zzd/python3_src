
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



'''


from .Pascal_number_like import PascalNumberLike


_sc_data = [[1], [0, 1], [0, 1, 1], [0, 2, 3, 1], [0, 6, 11, 6, 1], [0, 24, 50, 35, 10, 1]]
_ss_data = [[1], [0, 1], [0, 1, 1], [0, 1, 3, 1], [0, 1, 7, 6, 1], [0, 1, 15, 25, 10, 1]]



class StirlingCircleNumber(PascalNumberLike):
    def _calc_pos_pascal_like(self, n, k, n1_k1, n1_k):
        return n1_k1 + n1_k*(n-1)
        raise NotImplementedError()
    def _calc_neg(self, n, k, table):
        if k > 0:
            return 0
        return stirling_subset(-k, -n)
        raise NotImplementedError()
    def direct_calc(self, n, k):
        raise NotImplementedError()


class StirlingSubsetNumber(PascalNumberLike):
    def _calc_pos_pascal_like(self, n, k, n1_k1, n1_k):
        return n1_k1 + n1_k*k
        raise NotImplementedError()
    def _calc_neg(self, n, k, table):
        if k > 0:
            return 0
        return stirling_circle(-k, -n)
        raise NotImplementedError()
    def direct_calc(self, n, k):
        raise NotImplementedError()


'''
from .numberss import NumberTable
class StirlingCircleNumber(NumberTable):
    def _calc_neg(self, n, k, table):
        if k > 0:
            return 0
        return stirling_subset(-k, -n)
        raise NotImplementedError()
    def _calc_pos(self, n, k, table):
        if k == n:
            return 1
        if k == 0:
            return 0

        assert 0 < k < n
        return table[n-1][k-1] + table[n-1][k]*(n-1)
        raise NotImplementedError()
    def _calc_pos_beyond(self, n, k, table):
        return 0
        raise NotImplementedError()
    def direct_calc(self, n, k):
        raise NotImplementedError()
    def row_len(self, n):
        return n+1
        
    def __init__(self):
        super().__init__([[1]])
    
    



#############################################3


class StirlingSubsetNumber(NumberTable):
    def _calc_neg(self, n, k, table):
        if k > 0:
            return 0
        return stirling_circle(-k, -n)
        raise NotImplementedError()
    def _calc_pos(self, n, k, table):
        if k == n:
            return 1
        if k == 0:
            return 0

        assert 0 < k < n
        return table[n-1][k-1] + table[n-1][k]*k
        raise NotImplementedError()
    def _calc_pos_beyond(self, n, k, table):
        return 0
        raise NotImplementedError()
    def direct_calc(self, n, k):
        raise NotImplementedError()
    def row_len(self, n):
        return n+1
        
    def __init__(self):
        super().__init__([[1]])

'''


####################
stirling_subset = stirling_subset_number = StirlingSubsetNumber()
stirling_circle = stirling_circle_number = StirlingCircleNumber()

#print(stirling_circle.get_first(6))
assert stirling_circle.get_first(len(_sc_data)) == _sc_data
   
#print(stirling_subset.get_first(6))
assert stirling_subset.get_first(len(_ss_data)) == _ss_data

assert stirling_subset(5, 3) == stirling_circle(-3, -5)
assert stirling_subset(-3, -6) == stirling_circle(6, 3)

