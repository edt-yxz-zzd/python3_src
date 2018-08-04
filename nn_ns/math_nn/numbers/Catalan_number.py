

'''
concrete math 7.5 page 360

[NN m,n,L][m>=2][L>0]:
    seq of (m*n + L) numbers in {1-m, 1}
    n (1-m)'s and (m*n+L-n) 1's
    sum(seq) = n*(1-m) + (m*n+L-n) = L
    the number of such sequences with all partial sums positive is
    C L m n = C(m*n+L, n) L/(m*n+L)

    C L m n / C L m (n-1) = C(m*n+L, n) L/(m*n+L) / (C(m*n+L-m, n-1) L/(m*n+L-m))
        = C(m*n+L, n) / C(m*n+L-m, n-1) (m*n+L-m)/(m*n+L)
        = fall(m*n+L, n)/n/ fall(m*n+L-m, n-1) (m*n+L-m)/(m*n+L)
        = fall(m*n+L, m) fall(m*n+L-m, n-m) / fall(m*n+L-m, n-1) (m*n+L-m)/(m*n+L)/n
        = fall(m*n+L, m) / fall(m*n+L-m -(n-m), n-1-(n-m)) (m*n+L-m)/(m*n+L)/n
        = fall(m*n+L, m) / fall(m*n+L -n, m-1) (m*n+L-m)/(m*n+L)/n


[m=2][L=1]:
    Catalan[n] = C 1 2 n = C(2n+1, n)/(2n+1) = C(2n, n)/(n+1)
    n * -1 + (n+1) * +1 = 1
    n embedding pairs: '(' ')'
    C[n] = sum '(' C[i] ')' * C[n-1-i] {i}
    G 2 z = sum C[i] z**i {NN i}
    G(1 2, z) = z G(2, z)**2 + 1 = (1-sqrt(1-4z)) / (2z)
    C L m n / C L m (n-1) = C(2n, n)/(n+1) / C(2n-2, n-1) n
        = (2n)!/n!/n! / (2n-2)! (n-1)!**2 n/(n+1)
        = fall(2n,2) / n / (n+1) = fall(2n,2)/fall(n+1,2)
        =?= fall(m*n+L, m) / fall(m*n+L -n, m-1) (m*n+L-m)/(m*n+L)/n
        = fall(2*n+1, 2) / fall(n+1, 1) (2n-1)/(2n+1)/n
        = 2n / (n+1)  (2n-1)/n; yes

[m>=2][L=1]:
    G 1 m z = sum C 1 m i * z**i {NN i}
    G(1,m,z) = z G(1,m,z)**m + 1

[m>=2][L>0]:
    G(L,m,z) = G(1,m,z)**L

    generalized binomial series:
    B(r,t,z) = G(r,t,z) = B(1,t,z)**r





'''

__all__ = '''
    catalan_number

    CatalanNumberEx
    CatalanEx__direct_calc
    '''.split()

import functools
from .choose import C
from .numberss import NumberList
from ..powers import fall

def CatalanEx__direct_calc(n, m=2, L=1):
    '''C(m*n+L, n) L/(m*n+L)'''

    N = m*n+L
    return C(N,n) * L // N

def _CatalanINC(n, m, L):
    '''C[n]/C[n-1] = fall(m*n+L, m) / fall(m*n+L -n, m-1) (m*n+L-m)/(m*n+L)/n'''
    M = m*n+L
    N = fall(M,m)*(M-m)
    D = fall(M-n, m-1)*M*n

    # N/D
    return N, D

_data = [1, 1, 2, 5, 14,    42, 132, 429, 1430, 4862,
         16796, 58786, 208012, 742900, 2674440,
         9694845, 35357670, 129644790, 477638700, 1767263190]

class _CatalanNumberEx(NumberList):
    def _calc_neg(self, n, nums):
        raise NotImplementedError()
    def _calc_pos(self, n, nums):
        m, L = self.__m, self.__L
        N, D = _CatalanINC(n, m, L)
        return nums[-1]*N//D
        raise NotImplementedError()
    def direct_calc(self, n):
        return CatalanEx__direct_calc(n, self.__m, self.__L)
        raise NotImplementedError()


    def __init__(self, m=2, L=1):
        '''C(m*n+L, n) L/(m*n+L)'''

        assert m >= 2
        assert L > 0

        self.__m = m
        self.__L = L
        super().__init__([1])




def CatalanNumberEx(m=2, L=1):
    assert m >= 2
    assert L > 0
    return __CatalanNumberEx(m, L)

@functools.lru_cache(maxsize=None, typed=False)
def __CatalanNumberEx(m, L):
    return _CatalanNumberEx(m, L)




catalan = catalan_number = CatalanNumberEx()

#print(catalan.get_first(20))
assert catalan.get_first(len(_data)) == _data
assert all(catalan.direct_calc(n) == catalan(n) for n in range(8))






































