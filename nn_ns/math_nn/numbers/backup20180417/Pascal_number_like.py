


'''
Pascal_number(n,k) = binomial(n,k) = choose(n,k) = C(n,k)
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



from .numberss import NumberTable


class PascalNumberLike(NumberTable):
    def _calc_pos_pascal_like(self, n, k, n1_k1, n1_k):
        raise NotImplementedError()
    def _calc_neg(self, n, k, table):
        raise NotImplementedError()
    def _calc_pos(self, n, k, table):
        assert n > 0
        if 0 < k < self.row_len(n-1):
            a, b = table[n-1][k-1], table[n-1][k]
        elif k == 0:
            a, b = 0, table[n-1][k]
        elif k == n:
            a, b = table[n-1][k-1], 0
        else:
            raise logic-error

        return self._calc_pos_pascal_like(n,k, a,b)
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

    
