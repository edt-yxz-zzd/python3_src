

__all__ = '''
    IXBallotNumberLike
    '''.split()

from .INumberTable import INumberTable
from .numbers_common import abstract_method, optional_method, override, define



class IXBallotNumberLike(INumberTable):
    '''IXBallotNumberLike v.s. IPascalNumberLike

IXBallotNumberLike[n][k] =
    f(IXBallotNumberLike[n  ][k-1]
    , IXBallotNumberLike[n-1][k])
IPascalNumberLike[n][k] =
    f(IPascalNumberLike[n-1][k-1]
    , IPascalNumberLike[n-1][k])

xballot(q,p) = ballot(p,q)
    # "x" - means arguments swap
    | 0 <= p <= q != 0  = xballot(q-1, p) + xballot(q, p-1)
    | 0 == p == q       = 1
    | otherwise         = 0



abstract_method:
    get_table
    row_len
    _calc_pos_xballot_like # new
optional_method:
    lookup_static
    _lookup_pos_overflow
    _lookup_pos_underflow
    direct_calc
    _fill_when_neg
    _lookup_neg
'''
    __slots__ = ()

    #@abstract_method
    #def row_len(self, n):
    #@optional_method
    #def direct_calc(self, n, k):


    @abstract_method
    def _calc_pos_xballot_like(self, n, k, n_k1, n1_k):
        '''_calc_pos_xballot_like(n, k, table[n][k-1], table[n-1][k]) -> table[n][k]

'''
        raise NotImplementedError
        return n_k1 + n1_k


    @override
    def _calc_pos(self, n, k, table):
        if n == 0: raise NotImplementedError
        #neednot: assert n > 0 # since init table set first row
        #neednot: assert 0 <= k <= n # assume n == row_len(n)-1
        n1_k = table[n-1][k] if 0 <= k < len(table[n-1]) else \
                self._lookup_pos_beyond(n-1, k, table)
        n_k1 = table[n][k-1] if 0 <= k-1 < len(table[n]) else \
                self._lookup_pos_beyond(n, k-1, table)

        return self._calc_pos_xballot_like(n,k, n_k1,n1_k)
        raise NotImplementedError

    @override
    def lookup_static(self, n, k):
        # for xballot(q,p)
        #   q = n; p = k
        #   not (0 <= p <= q) ==>> 0

        # not really: if not (0 <= k <= n): return 0
        if n >= 0 and not (0 <= k < self.row_len(n)): return 0

        # bug: if n == 0: return 0
        # not really: if n == 0: return 1
        raise LookupError






