
'''
knot polynomials

tame knot ==>> elementary ideal is a principal ideal in gcd domain
mx_gcd(k, mx) ::= gcd(det(sub) for sub in submatrices(mx) if sub is k by k)

mx -> diag_mx -> square_diag_mx
diag_mx_gcds(diag_mx) ::= [mx_gcd(k, diag_mx) for k in [0..min(m, n)]] where diag_mx is m by n
diag_mx_gcds(diag_mx<m,n>) = diag_mx_gcds(diag_mx<m,n>[:r, :r]) where r=min(m,n)

square_diag_mx_gcds(diag) ::= diag_mx_gcds(make_diag_mx(diag))
square_diag_mx_gcds(diag)[k] = gcd(square_diag_mx_gcds(diag[:-1])[k],
                                   square_diag_mx_gcds(diag[:-1])[k-1]*diag[-1])
square_diag_mx_gcds(diag)[k] = 0 if len(diag) < k
    verify:
    square_diag_mx_gcds(diag)[k] = gcd(square_diag_mx_gcds(diag[:-1])[k],
                                       square_diag_mx_gcds(diag[:-1])[k-1]*diag[-1])
        = gcd(0, 0) = 0
square_diag_mx_gcds(diag)[1] = gcd(diag) = gcd(gcd(diag[:-1]), diag[-1])
    compare def
    = gcd(square_diag_mx_gcds(diag[:-1])[1],
          square_diag_mx_gcds(diag)[0]*diag[-1])
    ==>> square_diag_mx_gcds(diag)[0] = 1

square_diag_mx_gcds(diag)[k]
    = 1 if k == 0
    = 0 if len(diag) < k
    = gcd(square_diag_mx_gcds(diag[:-1])[k],
          square_diag_mx_gcds(diag[:-1])[k-1]*diag[-1]) if 0 < k <= len(diag)
    
'''

from fractions import gcd as _gcd

class CalcMxGcd:
    def __init__(self, zero, one, gcd):
        self.zero = zero
        self.one = one
        self.gcd = gcd
    def _next_square_diag_mx_gcds(self, diag, gcds_of_prev_L):
        '''\
prev_L = len(gcds_of_prev_L)-2
gcds_of_prev_L == square_diag_mx_gcds(diag[:prev_L]) + [0]
curr_L = prev_L + 1
return square_diag_mx_gcds(diag[:curr_L]) + [0]
'''
        assert gcds_of_prev_L
        assert gcds_of_prev_L[0] == self.one
        assert gcds_of_prev_L[-1] == self.zero
        prev_L = len(gcds_of_prev_L)-2
        curr_L = prev_L + 1
        
        result = [self.one]
        result.extend(self.gcd(gcds_of_prev_L[k],
                               gcds_of_prev_L[k-1]*diag[curr_L-1])
                      for k in range(1, curr_L+1))
        result.append(self.zero)
        return result
    def square_diag_mx_gcds(self, diag):
        gcds_of_prev_L = [self.one, self.zero]
        for L in range(1, len(diag)+1):
            assert len(gcds_of_prev_L) == L+1
            gcds_of_prev_L = self._next_square_diag_mx_gcds(diag, gcds_of_prev_L)
            assert len(gcds_of_prev_L) == L+2

        assert len(gcds_of_prev_L) == len(diag) + 2
        return gcds_of_prev_L[:-1]


c = CalcMxGcd(0, 1, _gcd)
assert c.square_diag_mx_gcds([]) == [c.one]
assert c.square_diag_mx_gcds([34]) == [1, 34]
assert c.square_diag_mx_gcds([6, 10]) == [1, 2, 60]
assert c.square_diag_mx_gcds([42, 70, 105]) == [1, 7, 1470, 7**3*900]
'''
2 3 7 
2 5 7
3 5 7
'''





