
r'''
bijection (a,b): # in case of b==a, we don't use {a,b}
    a -> b
    b -> a

manager:
    typeA -> typeB -> bijection (typeA, typeB)


'''



from abc import abstractmethod, ABCMeta
import functools
import math

class IObject(metaclass=ABCMeta):pass

@functools.total_ordering 
class IIntOp(IObject):
    @abstractmethod
    def get_int(self):...
    @abstractmethod
    def from_int(self):...
    def __neg__(self):
        return self.from_int(-self.get_int())
    def __pos__(self):
        return self.from_int(+self.get_int())
    def __abs__(self):
        return self.from_int(abs(self.get_int()))
    def __invert__(self):
        return self.from_int(~self.get_int())


    def __complex__(self):
        return complex(self.get_int())
    #def __int__(self): return int(self.get_int())
    def __float__(self):
        return float(self.get_int())
    def __round__(self, n=0):
        return round(self.get_int())


    def __add__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError
        return self.from_int(self.get_int() + other.get_int())
    def __sub__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError
        return self.from_int(self.get_int() - other.get_int())
    def __mul__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError
        return self.from_int(self.get_int() * other.get_int())
    def __floordiv__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError
        return self.from_int(self.get_int() // other.get_int())
    def __mod__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError
        return self.from_int(self.get_int() % other.get_int())
    def __divmod__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError
        q, r = map(self.from_int, divmod(self.get_int(), other.get_int()))
        return (q,r)
    def __pow__(self, other, modulo = None):
        if not isinstance(other, type(self)):
            raise TypeError
        return self.from_int(pow(self.get_int(), other.get_int(), modulo.get_int()))
    def __lshift__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError
        return self.from_int(self.get_int() << other.get_int())
    def __rshift__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError
        return self.from_int(self.get_int() >> other.get_int())
    def __and__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError
        return self.from_int(self.get_int() & other.get_int())
    def __xor__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError
        return self.from_int(self.get_int() ^ other.get_int())
    def __or__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError
        return self.from_int(self.get_int() | other.get_int())



    def __lt__(self, other):
        return self.__index__() < other.__index__()
    def __le__(self, other):
        return self.__index__() <= other.__index__()
    def __eq__(self, other):
        return self.__index__() == other.__index__()




class IIntLike(IIntOp, IObject):
    # assume immutable
    def get_int(self):
        return int(self)
    def __int__(self):
        return type(self).__index__(self)
    @abstractmethod
    def __index__(self):
        raise NotImplementedError

    @classmethod
    def from_int(cls, i):
        return cls(i)
    def __repr__(self):
        return '{}({})'.format(type(self).__name__, int(self))

class IIntTest(IIntLike):
    @classmethod
    @abstractmethod
    def __test_int__(cls, i):
        raise NotImplementedError

class IntTest_Init(IIntTest):
    def __init__(self, i):
        if not type(self).__test_int__(i):
            raise ValueError('bad int: {}'.format(i))
        self.__i = i
    def __index__(self):
        return self.__i


def gcd_ex(a, b):
    # A*a + B*b == g >= 0
    # g == 0 <==> (a,b) == 0
    # if b != 0, then 0 <= A < |b|, treat b as M
    # if b == 0, then A == sign a
    # AA*a + BA*b == a0
    # AB*a + BB*b == b0
    AA, BA = 1, 0
    AB, BB = 0, 1
    a0, b0 = a, b
    if a < 0:
        AA = -1
        a = -a0
    if b < 0:
        BB = -1
        b = -b0

    while b:
        q, r = divmod(a,b)
        # a = q*b + r
        # r = a - q*b = AA*a0 + BA*b0 - q*(AB*a0 + BB*b0)
        #   = (AA-q*AB)*a0 + (BA-q*BB)*b0
        # a', b' = b, r
        a, b = b, r
        AA, BA,  AB, BB = AB, BB,  AA-q*AB, BA-q*BB

    g = a
    A, B = AA, BA
    if A < 0 and b0:
        if b0 < 0:
            A -= b0
            B += a0
        else:
            A += b0
            B -= a0
    assert (0 <= A < abs(b0)) or (b0 == 0 and g == abs(a0))
    assert A*a0 + B*b0 == g >= 0
    assert g == math.gcd(a0, b0)
    return g, A, B

class NoInvError(ZeroDivisionError):pass
def inv_mod(a, M):
    g, A, B = gcd_ex(a, M)
    if g != 1:
        raise NoInvError('not coprime: inv_mod{}'.format((a,M)))
    return A



class IModUInt(IObject):
    # is not IIntLike !
    # no __index__
    # no compare
    # no __bool__
    @abstractmethod
    def to_uint(self):
        # return UInt
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def get_modulo(cls):
        # return PInt
        raise NotImplementedError
    @classmethod
    def from_int(cls, u):
        return cls(u)
    def __neg__(self):
        return self.from_int(-self.to_uint())
    def __pos__(self):
        return self.from_int(+self.to_uint())
    def __add__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError
        return self.from_int(self.to_uint() + other.to_uint())
    def __sub__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError
        return self.from_int(self.to_uint() - other.to_uint())
    def __mul__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError
        return self.from_int(self.to_uint() * other.to_uint())
    def __pow__(self, exp, modulo = None):
        if modulo is not None:
            raise ValueError('modulo is not None')
        i = self.to_uint() # UInt!
        exp = UInt(exp) # exp should not be ModUInt, ModUInt has no __index__
        modulo = UInt(self.get_modulo())
        return self.from_int(pow(i, exp, modulo))
    def inv(self):
        i = int(self.to_uint())
        M = int(self.get_modulo())
        r = inv_mod(i, M)
        return self.from_int(r)


class ModUInt(IModUInt):
    def __init__(self, i):
        self.__i = UInt(int(i) % int(self.get_modulo()))
    def to_uint(self):
        return self.__i
    def __repr__(self):
        return 'modulo2ModUIntType({})({})'\
                .format(int(type(self).get_modulo()), int(self.to_uint()))

def modulo2ModUIntType(u):
    u = u.__index__()
    if u <= 0:
        raise ValueError('modulo < 0')
    t = __modulo2ModUIntType.get(u)
    if t is not None:
        return t
    class _ModUInt_(ModUInt):
        module = PInt(u)
        @classmethod
        def get_modulo(cls):
            return cls.module
    __modulo2ModUIntType[u] = _ModUInt_
    return _ModUInt_
__modulo2ModUIntType = {}




class IIntGt(IIntTest):
    @classmethod
    @abstractmethod
    def get_max_under(cls):
        raise NotImplementedError
    @classmethod
    def __test_int__(cls, i):
        return i > cls.get_max_under()


class IntGt(IntTest_Init, IIntGt): pass
class UInt(IntGt):
    @classmethod
    def get_max_under(cls):
        return -1

class PInt(IntGt):
    @classmethod
    def get_max_under(cls):
        return 0

class QInt(IntGt):
    @classmethod
    def get_max_under(cls):
        return 1

class NInt(IntGt):
    @classmethod
    def get_max_under(cls):
        return -2

class SInt(IntTest_Init):
    @classmethod
    def __test_int__(cls):
        return True





################################
class IBijection(IObject):
    @abstractmethod
    def get_bijection_type_pair(self):
        # (From, To) # need not be type
        raise NotImplementedError

    @property
    def From(self):
        return self.get_bijection_type_pair()[0]
    @property
    def To(self):
        return self.get_bijection_type_pair()[1]
    @abstractmethod
    def __forward__(self, src):
        raise NotImplementedError
    @abstractmethod
    def __backward__(self, dest):
        raise NotImplementedError

    def __verify_type__(self, obj, Type):
        # Type is From or To, need not be type
        return isinstance(obj, Type)
        raise NotImplementedError
    def chain(self, others):
        return chain_bijections(self, *others)

    def forward(self, src):
        assert verify_type(self, src, self.From)
        return type(self).__forward__(self, src)
    def backward(self, dest):
        assert verify_type(self, dest, self.To)
        return type(self).__backward__(self, dest)
def verify_type(self, obj, Type):
    return type(self).__verify_type__(self, obj, Type)


#operator.attrgetter

def chain_bijections(*bijections):
    if len(bijections) == 1:
        return bijections[0]
    return ChainBijections(bijections)
class ChainBijections(IBijection):
    def __init__(self, bijections):
        # from outmost to inner most
        # [f, g, h] ==>> forward = h . g . f or f >=> g >=> h
        self.bijections = tuple(bijections)
        it = iter(self.bijections)
        for bijection in it:
            first_From, prev_To = self.get_bijection_type_pair
            break
        else:
            raise ValueError('no bijection')
        for bijection in self.bijections:
            From, To = self.get_bijection_type_pair()
            if From is not prev_To:
                # not issubclass, since 'bijection'!
                raise TypeError('when chain bijections: '
                                '{} == prev_To != From == {})'
                                .format(prev_To, From))
            prev_To = To
        last_To = prev_To
        self.__pair = first_From, last_To

    def get_bijection_type_pair(self):
        return self.__pair
    def forward(self, src):
        for bijection in self.bijections:
            src = bijection.forward(src)
        return src
    def backward(self, to):
        for bijection in self.bijections:
            to = bijection.backward(to)
        return to

'''
from enum import Enum
class KnownTypes(Enum):
    ModUInt
    SInt # int
    NInt # >= -1
    UInt # >= 0
    PInt # >= 1
    QInt # >= 2
    UInts
    TupleOF # [sum::PInt] [product::QInt] [uint]
'''


class IModUIntBijection(IBijection):
    def get_bijection_type_pair(self):
        return (ModUInt, ModUInt)

class ModAdd(IModUIntBijection):
    def __init__(self, i):
        self.__const = int(i)
    def __forward__(self, i):
        return self.__add(self.__const, i)
    def __backward__(self, i):
        return self.__add(-self.__const, i)
    def __add(self, const, mod_uint):
        if const >= 0:
            j = mod_uint.from_int(const)
            return mod_uint + j
        else:
            j = mod_uint.from_int(-const)
            return mod_uint - j

u = modulo2ModUIntType(3)(1)
f = ModAdd(4)
print(f.forward(u))


class ModMul(IModUIntBijection):
    def __init__(self, i):
        if not isinstance(i, IModUInt):
            raise TypeError
        self.__i = i
        self.__inv = i.inv()
    def __forward__(self, i):
        return self.__i * i
    def __backward__(self, i):
        return self.__inv * i



