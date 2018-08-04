
#from sand import top_level_import
#assert top_level_import(__name__, 'sand.forgot_import', args=('logic error',))


#from sand import frozendict
from seed.types.FrozenDict import FrozenDict as frozendict
from .min_factor import min_factor as n2min_factor
from .numberss import NumberList
from ..smalls import divides
from ..integer.CertificatedPrime import \
     CertificatedPrime, find_primitive_root


'''
n2factors = [None, frozendict()]

def get_n2factors_least_len(L):
    n2min_factor = min_factor.get_least_len(L)
    for n in range(len(n2factors), L):
        assert len(n2factors) == n
        
        p = n2min_factor[n]
        assert divides(p, n)
        if p < n:
            p, = n2factors[p].keys() # int to CertificatedPrime
            p2exp = dict(n2factors[n//p])
            p2exp.setdefault(p, 0)
            p2exp[p] += 1
            n2factors.append(frozendict(p2exp))
        else:
            assert p == n
            root = find_primitive_root(p, p-1, n2factors[p-1])
            p_ = CertificatedPrime(n2factors[p-1], root)
            assert p_ == p
            p = p_
            n2factors.append(frozendict({p:1}))
    return n2factors





from pprint import pprint
pprint(get_n2factors_least_len(10))
'''


class CertificatedFactors(NumberList):
    def _calc_pos(self, n, nums):
        n2factors = nums
        assert len(n2factors) == n
        
        p = n2min_factor(n) # __call__ not __index__
        assert divides(p, n)
        if p < n:
            p, = n2factors[p].keys() # int to CertificatedPrime
            p2exp = dict(n2factors[n//p])
            p2exp.setdefault(p, 0)
            p2exp[p] += 1
            result = frozendict(p2exp)
            #n2factors.append(frozendict(p2exp))
        else:
            assert p == n
            root = find_primitive_root(p, p-1, n2factors[p-1])
            p_ = CertificatedPrime(n2factors[p-1], root)
            assert p_ == p
            p = p_
            result = frozendict({p:1})
            #n2factors.append(frozendict({p:1}))
        return result
        raise NotImplementedError()
    def __init__(self):
        super().__init__([None, frozendict()])



n2factors = certificated_factors = CertificatedFactors()

_data = [None, {}, {2:1}, {3:1}, {2:2}, {5:1}, {2:1,3:1},
         {7:1}, {2:3}, {3:2}, {2:1,5:1}, {11:1}, {2:2,3:1}]

assert n2factors.get_first(len(_data)) == _data






    
    
