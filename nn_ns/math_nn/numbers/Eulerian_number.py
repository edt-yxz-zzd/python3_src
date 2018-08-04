
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

_e1_data = [[1], [1, 0], [1, 1, 0], [1, 4, 1, 0], [1, 11, 11, 1, 0], [1, 26, 66, 26, 1, 0]]
_e2_data = [[1], [1, 0], [1, 2, 0], [1, 8, 6, 0], [1, 22, 58, 24, 0], [1, 52, 328, 444, 120, 0]]


class Eulerian1stNumber(PascalNumberLike):
    def _calc_pos_pascal_like(self, n, k, n1_k1, n1_k):
        return n1_k1 * (n-k) + n1_k*(k+1)
        raise NotImplementedError()
    def _calc_neg(self, n, k, table):
        raise NotImplementedError()
    def direct_calc(self, n, k):
        raise NotImplementedError()


class Eulerian2ndNumber(PascalNumberLike):
    def _calc_pos_pascal_like(self, n, k, n1_k1, n1_k):
        return n1_k1 * (2*n-1-k) + n1_k*(k+1)
        raise NotImplementedError()
    def _calc_neg(self, n, k, table):
        raise NotImplementedError()
    def direct_calc(self, n, k):
        raise NotImplementedError()



####################
eulerian_1st = eulerian_1st_number = Eulerian1stNumber()
eulerian_2nd = eulerian_2nd_number = Eulerian2ndNumber()

##print(eulerian_1st.get_first(6))
##print(eulerian_2nd.get_first(6))

assert eulerian_1st.get_first(len(_e1_data)) == _e1_data
assert eulerian_2nd.get_first(len(_e2_data)) == _e2_data



