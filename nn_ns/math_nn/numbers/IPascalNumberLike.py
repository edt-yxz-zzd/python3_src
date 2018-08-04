
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


__all__ = '''
    IPascalNumberLike
    '''.split()

from .INumberTable import INumberTable
from .numbers_common import abstract_method, optional_method, override, define



class IPascalNumberLike(INumberTable):
    '''IXBallotNumberLike v.s. IPascalNumberLike

IXBallotNumberLike[n][k] =
    f(IXBallotNumberLike[n  ][k-1]
    , IXBallotNumberLike[n-1][k])
IPascalNumberLike[n][k] =
    f(IPascalNumberLike[n-1][k-1]
    , IPascalNumberLike[n-1][k])




abstract_method:
    get_table
    row_len
    _calc_pos_pascal_like # new
optional_method:
    lookup_static
    _lookup_pos_overflow
    _lookup_pos_underflow
    direct_calc
    _fill_when_neg
    _lookup_neg
'''
    __slots__ = ()

    #@optional_method
    #def direct_calc(self, n, k):
    #@abstract_method
    #def row_len(self, n):

    @abstract_method
    def _calc_pos_pascal_like(self, n, k, n1_k1, n1_k):
        raise NotImplementedError
    def _calc_pos(self, n, k, table):
        assert n >= 0
        assert 0 <= k <= self.row_len(n)
        if n == 0: raise NotImplementedError
        # assume init table offer first row

        # n1 = n-1 >= 0
        # k1 = k-1 >= -1
        L_n1 = self.row_len(n-1)
        def get_n1_kx(kx):
            n1_kx = table[n-1][kx] if 0 <= kx < L_n1 else\
                    self._lookup_pos_beyond(n-1, kx, table)
            return n1_kx
        n1_k1 = get_n1_kx(k-1)
        n1_k = get_n1_kx(k)

        return self._calc_pos_pascal_like(n,k, n1_k1, n1_k)
        raise NotImplementedError
    '''
    def lookup_static(self, n, k):
        if n >= 0 and not (0 <= k < self.row_len(n)): return 0
        raise LookupError
    '''






