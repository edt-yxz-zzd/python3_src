

#from sand import top_level_import
#assert top_level_import(__name__, 'sand.forgot_import', args=('logic error',))
##
##from sand import raise_when_forgot, to_names
##assert not raise_when_forgot(__file__, to_names('error, logic'))


##from itertools import islice, count, chain, accumulate, groupby, starmap
##from functools import reduce
##from operator import eq, ne, lt, le, gt, ge
##from operator import mul, truediv, add, sub
##from operator import attrgetter, itemgetter, methodcaller
##from operator import delitem, setitem, getitem
##
##from functools import total_ordering, lru_cache
##from contextlib import contextmanager
##from abc import abstractmethod, ABCMeta
##
##
##from collections import namedtuple, defaultdict, deque, OrderedDict
##from array import array
##from fractions import Fraction, gcd
##from numbers import Integral, Rational
##
##from pprint import pprint
##import re
##import sys
##import os
##import os.path
##from io import StringIO, BytesIO

#from nn_ns.math_nn.numbers.min_factor import min_factor
from fractions import gcd
from numbers import Integral
from nn_ns.math_nn.smalls import II_base_exp, divides
from seed.types.FrozenDict import FrozenDict as frozendict
#from sand import to_names, unzip, frozendict
#from sand.dot import dot, apply, pdot, papp, id_func, ls_map
#to_names = lambda string: tuple(string.replace(',', ' ').strip().split())
__all__ = '''
    CertificatedPrime
    find_primitive_root
'''.split()



class CertificatedPrime(int):
    r'''given prime p, exist g,
s.t. [mod p]: g**((p-1)/q) != 1 for [prime q\(p-1)]
certificate = ({CertificatedPrime q: exp in p-1}, g)
'''
    @staticmethod
    def _IsMutable__is_mutable():
        return False

    __2 = None

    @property
    def root(self):
        return self.__root
    @property
    def phi_p_factors(self):
        return self.__phi_p_factors
    
    def __new__(subclass, q2exp=frozendict(), root=None):
        '''CertificatedPrime() # default == 2
CertificatedPrime(certificated_prime)
CertificatedPrime(q2exp, root)
'''
        this_class = __class__
        q2exp = frozendict(q2exp)
        if not q2exp and this_class.__2 is not None:
            q2exp = this_class.__2
            if root is not None:
                if gcd(root, 2) != 1:
                    raise ValueError('gcd(root, 2) != 1')
                root = None
            

##        if root is None and not q2exp:
##            # default to 2
##            root = 1
            
        if root is None:
            if not isinstance(q2exp, this_class):
                raise TypeError(
                    'not isinstance(q2exp, this_class) '
                    'while root is None and list(q2exp)')
            base_obj = q2exp
            if isinstance(base_obj, subclass) and \
               not base_obj._IsMutable__is_mutable():
                self = base_obj
                return self
            p = int(base_obj)
            root = base_obj.root
            q2exp = base_obj.phi_p_factors

        else:
            if not isinstance(root, Integral):
                raise TypeError('not isinstance(root, Integral)')
            if not all(isinstance(q, __class__) for q in q2exp):
                raise TypeError('not all(isinstance(q, __class__))')

            phi_p = II_base_exp(q2exp.items())
            p = phi_p + 1
            #raise ValueError('not p == inv_factor(q2exp)+1')
            assert p >= 2
            root %= p
            if gcd(root, p) != 1:
                raise ValueError('not prime: gcd(root, p) != 1')
            if not all(pow(root, phi_p//q, p) != 1 for q in q2exp):
                raise ValueError('not prime: '
                    'not all(pow(root, phi_p//q, p) != 1 for q in q2exp)')


        self = super(this_class, subclass).__new__(subclass, p)
        self.__phi_p_factors = q2exp
        self.__root = root

        return self

    def __str__(self):
        return super().__str__()
    
    def __repr__(self):
        return '{!s}({!r}, {!r})'.format(
            type(self).__name__, self.phi_p_factors, int(self.root))

# init __2 can not use CertificatedPrime()
CertificatedPrime._CertificatedPrime__2 = CertificatedPrime((), 1)
assert CertificatedPrime._CertificatedPrime__2 == 2
assert CertificatedPrime._CertificatedPrime__2 is CertificatedPrime()
assert hash(CertificatedPrime._CertificatedPrime__2) == hash(2)



def find_primitive_root(n, phi_n, phi_n_factors):
    # exist faster algorithm but...
    return find_min_primitive_root(n, phi_n, phi_n_factors)

def find_min_primitive_root(n, phi_n, phi_n_factors):
    r'''phi_n_factors = {q: exp for CertificatedPrime q if [q\phi_n]}

I donot check whether phi_n == phi(n)
'''
    if not n >= 2:
        raise ValueError('not n >= 2')
    if not n > phi_n > 0:
        raise ValueError('not n > phi_n > 0')

    phi_n_factors = frozendict(phi_n_factors)
    if not phi_n == II_base_exp(phi_n_factors.items()):
        raise ValueError('not phi_n == II_base_exp(phi_n_factors.items())')
##    if not all(divides(q, phi_n) for q in phi_n_factors):
##        raise ValueError('not all(divides(q, phi_n) for q in phi_n_divisors)')
        

    for root in range(1, n):
        if gcd(root, n) == 1 and\
           all(pow(root, phi_n//q, n) != 1 for q in phi_n_factors):
            if not pow(root, phi_n, n) == 1:
                raise ValueError('phi_n != phi(n)')
            # well, even now, phi_n may not be phi(n)
            # phi_n_divisors may not contains all phi_n's prime factors
            # 
            
            return root

    raise ValueError('no primitive roots')






