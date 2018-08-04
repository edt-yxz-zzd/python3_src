



'''
try to fix: int**Fraction -> int or float or complex
--------------------------------------------------------


RadixInt
    PositiveInt
        PrimeInt
ProductPrimeInt = II PrimeInts # PositiveInt
    = II[prime p[i]][int e[i]>0]: p[i]**e[i] {i}
    = {prime:exp}

CoeffRational = (RadixInt, PositiveInt) # ???using PowRoot(N,1)*PowRoot(D,-1)
ExpRational = (RadixInt, ProductPrimeInt)
PowRoot = base**exp for [number base][ExpRational exp]


-----------------------------------
PowerableNumber = SumNumber
SumNumber = sum of SumItems = {SumItem:CoeffRational} # NOTE 0 == SumNumber{}
SumItem = MulNumber
MulNumber = product of MulItems = {MulItem:ExpRational} # NOTE 1 == MulNumber{}
MulItem = PowerableNumber
ExpRational = (RadixInt, Prime2Exp)
CoeffRational = (RadixInt, PositiveInt)
Prime2Exp = {PrimeInt: PositiveInt}

so, we need: RadixInt, PositiveInt, PrimeInt
PowerableNumber = RadixInt | sum(CoeffRational*II(PowerableNumber**ExpRational))


frozendict
'''
import functools
from numbers import Integral, Rational, Number
from fractions import Fraction
from abc import abstractmethod
from sand import frozendict, FrozenDict
from collections import defaultdict
from collections.abc import Mapping
from ..smalls import max_exp, to_int, is_int_factor, II_base_exp 


def inv_factor_int(prime2exp):
    if not all(map(is_prime, prime2exp)):
        raise ValueError('not is_prime(p) for some key of prime2exp')
    return II_base_exp(prime2exp.items())




def get_min_factor(low_bound, x):
    if not 2 <= low_bound <= x:
        raise ValueError('not 2 <= low_bound <= x')
    for i in range(low_bound, x+1):
        if is_int_factor(i, x):
            break
    assert low_bound <= i <= x
    assert is_int_factor(i, x)
    return i


def is_prime(x):
    if x < 2:
        return False
    return len(factor_int(x)) == 1
    
    return __is_prime(to_int(x))
@functools.lru_cache(maxsize=None, typed=False)
def __is_prime(x):
    raise NotImplementedError()


def factor_int(x):
    ps, es = pses = factor_int_into_sorted_primes_exps(x)
    return dict(zip(ps, es))

def factor_int_into_sorted_primes_exps(x):
    x = to_int(x)
    if not x > 0:
        raise ValueError('not x > 0')
    return __factor_int_into_sorted_primes_exps(x)
@functools.lru_cache(maxsize=None, typed=False)
def __factor_int_into_sorted_primes_exps(x):
    assert x >= 1

    x0 = x
    primes = []
    exps = []
    p = 1
    while x > p:
        p = get_min_factor(p+1, x)
        e = max_exp(p, x)
        x //= p**e
        primes.append(p)
        exps.append(e)
    assert x == 1
    assert x0 == II_base_exp(zip(primes, exps))
    
    assert primes == sorted(primes)
    assert all(e > 0 for e in exps)
    
    return tuple(primes), tuple(exps)
    raise NotImplementedError()


class PowerableNumber(Number):
    __slots__ = ()
    @abstractmethod
    def __hash__(self):
        raise NotImplementedError
    pass

'''
>>> class A(int):
	__slots__=('afsf',)
	pass

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    class A(int):
TypeError: nonempty __slots__ not supported for subtype of 'int'


'''


class RadixInt(int, PowerableNumber):
    __slots__ = ()
    def __new__(cls, x=0, base=None):
        if cls == RadixInt == type(x):
            if base is not None:
                raise TypeError('base should be None')
            return x
        if base is None:
            y = super(RadixInt, cls).__new__(cls, x)
        else:
            y = super(RadixInt, cls).__new__(cls, x, base)
        #print('type(super(RadixInt, cls).__new__(cls, i))', type(y))
        return y
    def __str__(self):
        return str(int(self))
    def __repr__(self):
        return '{}({})'.format(type(self).__name__, int(self))
    
zero, one, two, three, four, five, six, seven, eight, nine, ten = \
      map(RadixInt, range(11))


class NonnegativeInt(RadixInt):
    __slots__ = ()
    def __new__(subclass, x=0, base=None):
        this_class = __class__ # NonnegativeInt
        if subclass == this_class == type(x):
            if base is not None:
                raise TypeError('base should be None')
            return x
        self = super(this_class, subclass).__new__(subclass, x, base)
        if self < 0:
            raise ValueError('a nonnegativeInt integer is required')
        return self

class PositiveInt(NonnegativeInt):
    __slots__ = ()
    def __new__(subclass, x=0, base=None):
        this_class = __class__ # PositiveInt
        if subclass == this_class == type(x):
            if base is not None:
                raise TypeError('base should be None')
            return x
        self = super(this_class, subclass).__new__(subclass, x, base)
        if self <= 0:
            raise ValueError('a positive integer is required')
        return self




class PrimeInt(PositiveInt):
    __slots__ = ()
    def __new__(subclass, x=0, base=None):
        this_class = __class__ # PrimeInt
        if subclass == this_class == type(x):
            if base is not None:
                raise TypeError('base should be None')
            return x
        y = super(this_class, subclass).__new__(subclass, x, base)
        if not is_prime(y):
            raise ValueError('a prime integer is required')
        return y

zero, one, two, three, four, five, six, seven, eight, nine, ten = \
      map(RadixInt, range(11))


#collections.defaultdict
class Prime2Exp(FrozenDict):
    __slots__ = ()
    def __new__(subclass, mapping_or_iterable=()):
        this_class = __class__ # Prime2Exp
        key_type = PrimeInt
        value_type = PositiveInt
        
        if subclass == this_class == type(mapping_or_iterable):
            self = mapping_or_iterable
            return self
        it = ((PrimeInt(base), PositiveInt(exp)) for base, exp
              in dict(mapping_or_iterable).items())

        pairs = ((base, exp) for base, exp in it if exp != 0)
        self = super(this_class, subclass).__new__(subclass, pairs)
        return self
    @staticmethod
    def from_int(i):
        this_class = __class__ # Prime2Exp
        return this_class(factor_int(i))
    def __int__(self):
        return II_base_exp(self.items())
    
    def __mul__(self, other):
        this_class = __class__ # Prime2Exp
        if not isinstance(other, this_class):
            raise NotImplemented
        
        d = defaultdict(int, self)
        for prime, exp in other.items():
            d[prime] += exp
        return this_class(d)
    
    def __truediv__(self, other):
        this_class = __class__ # Prime2Exp
        if not isinstance(other, this_class):
            raise NotImplemented
        
        d = defaultdict(int, self)
        for prime, exp in other.items():
            d[prime] -= exp
            exp = d[prime]
            if exp < 0:
                raise ValueError('other not divides self')
            if not exp:
                del d[prime]
                
        return this_class(d)
    


    
    def __lshift(self, i):
        assert i > 0
        this_class = __class__ # Prime2Exp
        n = this_class({2:i})
        return self * n
    def __rshift(self, i):
        assert i > 0
        this_class = __class__ # Prime2Exp
        n = this_class({2:i})
        return self / n
    def __lshift__(self, i):
        if i > 0:
            return self.__lshift(i)
        if i < 0:
            return self.__rshift(-i)
        if i == 0:
            return self
        
        raise TypeError('i should be Integral')
    def __rshift__(self, i):
        return self << -i
    
    
    
    
        

class ProductPrimeInt(PositiveInt):
    # __slots__ = ('__prime2exp',)
    # TypeError: nonempty __slots__ not supported for subtype of 'PositiveInt'
    def __new__(subclass, x=Prime2Exp(), base=None, prime2exp=None):
        this_class = __class__ # ProductPrimeInt
        if subclass == this_class == type(x):
            if base is not None:
                raise TypeError('base should be None')
            if prime2exp is not None:
                raise TypeError('prime2exp should be None')
            return x


        d = None
        map_to_Prime2Exp = False
        
        if isinstance(x, Mapping):
            map_to_Prime2Exp = True
        elif isinstance(x, str) or hasattr(x, '__int__'):
            map_to_Prime2Exp = False
        elif isinstance(x, Iterable):
            map_to_Prime2Exp = True

        # set y for verify
        if map_to_Prime2Exp:
            if base is not None:
                raise TypeError('base should be None')
            if prime2exp is not None:
                raise TypeError('prime2exp should be None')
            prime2exp = Prime2Exp(x)
            x = y = int(prime2exp) # update x
        elif prime2exp is not None:
            if not isinstance(prime2exp, Prime2Exp):
                raise TypeError('prime2exp should be None or Prime2Exp')
            y = int(prime2exp)
        else:
            y = None
        
        
        self = super(this_class, subclass).__new__(subclass, x, base)
        if y is not None:
            if self != y:
                raise ValueError('self != int(prime2exp)')
        else:
            assert prime2exp is None
            prime2exp = Prime2Exp(factor_int(self))
            
        self.__prime2exp = prime2exp
        return self
    
    def get_prime2exp(self):
        return self.__prime2exp



assert ProductPrimeInt(1435*5).get_prime2exp() == {41: 1, 5: 2, 7: 1}


class CoeffRational(Fraction, PowerableNumber):
    'fixed: int**(N/D)'
    __slots__ = ()

    def __str__(self):
        return Fraction.__str__(self)
    def __repr__(self):
        return '{}({}, {})'.format(type(self).__name__,
                                   self.numerator, self.denominator)

    
##    def __new__(subclass, numerator=0, denominator=None):
##        this_class = __class__ # CoeffRational
##        self = super(this_class, subclass)\
##               .__new__(subclass, numerator, denominator)
##        return self
    pass


    


class ExpRational(CoeffRational):
    __slots__ = ('__prime2exp_of_denominator')
    def __new__(subclass, numerator=0, denominator=None, prime2exp_of_D=None):
        this_class = __class__ # ExpRational
        if subclass == this_class == type(numerator):
            if denominator != None:
                raise TypeError('denominator should be None')
            if prime2exp_of_D != None:
                raise TypeError('prime2exp_of_D should be None')
            self = numerator
            return self


        self = super(this_class, subclass)\
               .__new__(subclass, numerator, denominator)
        
        if prime2exp_of_D is not None:
            if not isinstance(prime2exp_of_D, Prime2Exp):
                raise ValueError(not isinstance(prime2exp_of_D, Prime2Exp))
            D = int(prime2exp_of_D)
            if self.denominator != D:
                raise ValueError('self.denominator != int(prime2exp_of_D)')
        else:
            prime2exp_of_D = Prime2Exp.from_int(self.denominator)

        self.__prime2exp_of_denominator = prime2exp_of_D
        return self
        


    def to_fraction(self):
        return self.numerator, self.denominator
    def get_prime2exp_of_denominator(self):
        return self.__prime2exp_of_denominator
    def __repr__(self):
        N, D = self.to_fraction()
        prime2exp = self.get_prime2exp_of_denominator()
        return '{}({!r}, {!r}, {!r})'.format(
            type(self).__name__, N, D, prime2exp)


class PowerableNumber2ExpRational(FrozenDict):
    __slots__ = ()
    def __new__(subclass, mapping_or_iterable=()):
        this_class = __class__ # PowerableNumber2ExpRational
        key_type = PowerableNumber
        value_type = CoeffRational
        input_key_type = PowerableNumber
        input_value_type = Rational
        
        if subclass == this_class == type(mapping_or_iterable):
            self = mapping_or_iterable
            return self

        d = dict(mapping_or_iterable)
        if not all(map(lambda base: isinstance(base, input_key_type), d)):
            raise TypeError('keys are not all {}'
                            .format(input_key_type.__name__))
        if not all(map(lambda exp: isinstance(exp, input_value_type), d.values())):
            raise TypeError('values are not all {}'
                            .format(input_value_type.__name__))
        

        pairs = ((key_type(base), value_type(exp)) for base, exp in it if exp != 0)
        self = super(this_class, subclass).__new__(subclass, pairs)
        return self
    
    def inv(self):
        return __class__((base, -exp) for base, exp in self.items())
    
    def __mul__(self, other):
        this_class = __class__ # PowerableNumber2ExpRational
        if not isinstance(other, this_class):
            raise NotImplemented
        
        d = defaultdict(int, self)
        for prime, exp in other.items():
            d[prime] += exp
            exp = d[prime]
            if not exp:
                del d[prime] # so, 0**0 == 1
        return this_class(d)
    
    def __truediv__(self, other):
        this_class = __class__ # PowerableNumber2ExpRational
        if not isinstance(other, this_class):
            raise NotImplemented
        
        return self * other.inv()
    


    
    def __lshift(self, i):
        #assert i > 0
        this_class = __class__ # PowerableNumber2ExpRational
        value_type = CoeffRational

        i = CoeffRational(i)
        n = this_class({two:i})
        return self * n
    
    def __lshift__(self, i):
        if not isinstance(i, Rational):
            raise TypeError('i should be Rational')
        return self.__lshift(i)
        
    def __rshift__(self, i):
        return self << -i
    
    

print(CoeffRational(3,-3))



print(ExpRational(3,-3))

c = CoeffRational
print((c.from_float(0.3), c(0)))
r = ExpRational
print((r.from_float(0.3), r(0)))


print(__module__)
print(__name__)
class B:
    def __init__(self):
        print(__name__)
        print(__class__)
        print(__self__)
        print(__func__)

class D(B):pass

D()




