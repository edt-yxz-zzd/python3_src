


__all__ = '''
    IRingOps
    IFiniteRingOps
    IRingWithIdentityOps
    IRingWithCharacteristicOps
    ICommutativeRingWithIdentityOps
    IGcdDomainOps
    IEuclideanDomainOps
    IFieldOps
    IFiniteFieldOps

    IRingOpsForRing
    IFieldOpsForField

    RingOpsForRing
    EuclideanDomainOps2ModularGcdDomainOps
    ModularRingOps
    PrimeModularFieldOps
    TheIntegerRingOps
    TheRationalFieldOps
    '''.split()
from fractions import gcd, Fraction
from abc import ABCMeta, abstractmethod
from nn_ns.math_nn.integer.mod import invmod

from seed.iters.binary_op import \
    ( pointwise
    , iter_accumulate
    , foldl
    , repeat_binary_op
    , iter_repeat_binary_op
    , assoc_op_with_pint
    , assoc_op_with_uint
    )

class IRingOps(metaclass=ABCMeta):
    @property
    @abstractmethod
    def zero(self):pass
    @abstractmethod
    def element_equal(self, x, y):pass
    @abstractmethod
    def is_element(self, x):pass
    @abstractmethod
    def neg(self, x):pass
    @abstractmethod
    def mul(self, x, y):pass
    @abstractmethod
    def add(self, x, y):pass

    def is_zero(self, x):
        return self.element_equal(x, self.zero)
    def sub(self, x, y):
        return self.add(x, self.neg(y))

    def mul_int_by_add(self, x, i):
        assert type(i) is int
        if i < 0:
            x = self.neg(x)
            i = -i
        return assoc_op_with_uint(self.add, self.zero, x, uint)
    def pow_uint(self, x, exp):
        # x^exp = product([x]*exp)
        return assoc_op_with_uint(self.mul, self.one, x, exp)
    # def sum(self, iterable, *, start=None):
    #   what if 'None' is a ring element??
    def power1s(self, start, w, L, container=tuple):
        return repeat_binary_op(self.mul, start, w, L, container)
    def time1s(self, start, w, L, container=tuple):
        return repeat_binary_op(self.add, start, w, L, container)
    def iter_power1s(self, start, w):
        return iter_repeat_binary_op(self.mul, start, w)
    def iter_time1s(self, start, w):
        return iter_repeat_binary_op(self.add, start, w)
    def sum1(self, start, iterable):
        return foldl(self.add, start, iterable)
    def product1(self, start, iterable):
        return foldl(self.mul, start, iterable)

    def times(self, w, L, container=tuple):
        return self.time1s(self.add, self.zero, w, L, container)
    def iter_times(self, w):
        return self.iter_time1s(self.zero, w)
    def sum(self, iterable):
        return self.sum1(self.zero, iterable)
    def vector_mul(self, X, Y, container=tuple):
        return pointwise(self.mul, X, Y, container=container)
    def vector_add(self, X, Y, container=tuple):
        return pointwise(self.add, X, Y, container=container)
class IFiniteRingOps(IRingOps):
    @property
    @abstractmethod
    def order(self):pass
class IRingWithIdentityOps(IRingOps):
    @property
    @abstractmethod
    def one(self):pass
    @property
    def neg_one(self):
        return self.neg(self.one)
    def is_one(self, x):
        return self.element_equal(x, self.one)
    def is_neg_one(self, x):
        return self.element_equal(x, self.neg_one)

    def element_equal_int(self, x, i):
        # see also: is_neg_one
        assert self.is_element(x)
        assert type(i) is int
        return self.element_equal(x, self.int2element(i))
    def int2element(self, i):
        # to be overrided
        # see also: zero, one, neg_one
        assert type(i) is int
        return self.mul_int_by_add(self.one, i)
    def mul_int(self, x, i):
        return self.mul(x, self.int2element(i))

    def powers(self, w, L, container=tuple):
        return self.power1s(self.one, w, L, container=container)
    def iter_powers(self, w):
        return self.iter_power1s(self.one, w)
    def product(self, iterable):
        return self.product1(self.one, iterable)
class IRingWithCharacteristicOps(IRingWithIdentityOps):
    # int2element(characteristic) == zero
    @property
    @abstractmethod
    def characteristic(self):pass
class ICommutativeRingWithIdentityOps(IRingWithIdentityOps):
    # see The Art of Computer Programming, Volume 2 :: Chapter4
    # commutative ring with identity
    #   polynomial over this ring can define pseudo-division(pseudo-divmod)
    #       LC = leading coefficient of g
    #       LC^(deg f - deg g + 1)*f = q*g + r where len r < len g <= len f
    # to be overrided: element_equal_int/int2element/mul_int/pow_uint
    @abstractmethod
    def true_div_int(self, x, i):
        # x/i = r iff exist only one r, s.t. r*i==x
        # else raise exception. implement defined
        # why?
        #   IDFT(n,w) = DFT(n,w)^-1 = DFT(n,w^(n-1))/n
        pass
    def arbitrary_radix_reprBE2number(self, iter_numbers, radix):
        n = self.zero
        for digit in iter_numbers:
            n = self.mul(n, radix)
            n = self.add(n, digit)
        return n

    def number2arbitrary_radix_reprLE(self, u, radix, divmodArb, container=tuple):
        return container(
                self.number2iter_arbitrary_radix_reprLE(u, radix, divmodArb))
    def number2iter_arbitrary_radix_reprLE(self, q, radix, divmodArb):
        while not self.is_zero(q):
            q, r = divmodArb(q, radix)
            yield r



class IGcdDomainOps(ICommutativeRingWithIdentityOps):
    @abstractmethod
    def __gcd_ex3_nonzero__(self, n, d):
        # return (gcd, n/gcd, d/gcd)
        pass
    def is_unit(self, x):
        g, ng, xg = gcd_ex3(self.one, x)
        return self.is_one(xg)
    def gcd_ex3(self, n, d):
        # gcd_ex3 0 0 = (0,0,0)
        # gcd_ex3 n 0 = (n,1,0)
        # gcd_ex3 0 d = (d,0,1)
        # gcd_ex3 n d | [d\n] = (d, n/d, one)
        # return (gcd, n/gcd, d/gcd)
        is_zero = self.is_zero
        z = self.zero
        if is_zero(d):
            return (z,z,z) if is_zero(n) else (n, self.one, z)
        if is_zero(n):
            return (d, z, self.one)
        gcd, n_, d_ = self.__gcd_ex3_nonzero__(n,d)
        assert self.element_equal(n, self.mul(gcd, n_))
        assert self.element_equal(d, self.mul(gcd, d_))
        return gcd, n_, d_

    def gcd(self, n, d):
        # gcd 0 0 = 0
        return self.gcd_ex3(n, d)[0]
    def true_div_int(self, n, i):
        return self.true_div(n, self.int2element(i))
    def true_div(self, n, d):
        gcd, q, _1 = self.gcd(n,d)
        if self.is_one(_1):
            assert self.element_equal(gcd, d)
            return q
        raise ValueError('can not divide')
class IEuclideanDomainOps(IGcdDomainOps):
    @abstractmethod
    def __divmod_nonzero__(self, n, d):
        # Euclidean division
        # [d != 0]
        # __divmod_nonzero__ n d = (q, r) where
        #   n = q*d+r; r==0 or norm r < norm n
        pass
    @abstractmethod
    # arbitrary_norm_EuclideanDomain x = r where r is a uint
    def arbitrary_norm_EuclideanDomain(self, x):pass


    def may_invmod(self, n,d):
        # return () | (inv,) where inv*n%d==1
        g, ginv = self.ginvmod(n,d)
        if self.is_one(g):
            return (ginv,)
        return ()
    def ginvmod(self, n,d):
        # ginvmod n d = (g, ginv) where
        #   g==1 or g==gcd n d # when (gcd n d) is not unit
        #   d==0 or g==ginv*n % d
        (g, ng, dg, kn, kd) = self.gcd_ex5(n,d)
        q, r = self.divmod(self.one, g)
        if self.is_zero(r):
            # g is unit
            # q*g = 1
            g = self.one
            ginv = self.mul(kn, q)
        else:
            ginv = kn
        assert self.is_zero(d) or self.element_equal(g, self.mod(self.mul(ginv,n), d))
        return g, ginv
    def true_div(self, n, d):
        q,r = self.floor_div(n,d)
        if self.is_zero(r):
            return q
        raise ValueError('can not divide')
    def floor_div(self, n, d):
        q,r = self.divmod(n, d)
        return q
    def mod(self, n, d):
        q,r = self.divmod(n, d)
        return r
    def divmod(self, n, d):
        if self.is_zero(d):
            raise ZeroDivisionError
        q, r = self.__divmod_nonzero__(n, d)
        if __debug__:
            norm = self.arbitrary_norm_EuclideanDomain
            assert self.is_zero(r) or 0 <= norm(r) < norm(d)
            assert self.element_equal(self.mul(q,d), self.sub(n,r))
        return q, r

    def __gcd_ex3_nonzero__(self, n, d):
        return self.gcd_ex5(n,d)[:3]
    def gcd_ex5(self, n, d):
        # Note: (gcd_ex5 n d)[:-3:-1] != (gcd_ex5 d n)[-2:]
        # return (g, ng, dg, kn, kd)
        # g*ng == n; g*dg == d; g == kn*n+kd*d
        # kn == (ng if d==0 else kn%d)
        # n==0 ==>> kd==dg and kn==0
        # d==0 ==>> kn==ng and kd==0
        # [d!=0][n%d==0] ==>> dg==1
        # gcd_ex5(n,d)[:3] == gcd_ex3(n,d)
        (g, ng, dg, kn, kd) = self.__gcd_ex5(n,d)
        if __debug__:
            mul = self.mul
            add = self.add
            mod =self.mod
            is_zero = self.is_zero
            is_one = self.is_one
            eq = self.element_equal
            assert eq(n, mul(g, ng))
            assert eq(d, mul(g, dg))
            assert eq(g, add(mul(kn,n), mul(kd,d)))
            assert eq(kn, ng if is_zero(d) else mod(kn,d))
            assert not is_zero(n) or (eq(kd,dg) and is_zero(kn))
            assert not is_zero(d) or (eq(kn,ng) and is_zero(kd))
            assert is_zero(d) or not is_zero(mod(n,d)) or is_one(dg)
        return (g, ng, dg, kn, kd)

    def __gcd_ex5(self, n, d):
        divmod = self.divmod
        is_zero = self.is_zero
        z,o = self.zero, self.one
        if is_zero(d):
            if is_zero(n):
                return (z,z,z,  z,z)
            return (n,o,z,  o,z)
        if is_zero(n):
            return (d,z,o,  z,o)

        # both n d are not zero
        n2n = d2d = o
        d2n = n2d = z
        old_n, old_d = n, d
        def calc(X2n,X2d,q):
            return self.sub(X2n, self.mul(X2d,q))
        # n = n2n*old_n+d2n*old_d
        # d = n2d*old_n+d2d*old_d
        while not is_zero(d):
            # n = n2n*old_n+d2n*old_d
            # d = n2d*old_n+d2d*old_d
            q, r = divmod(n, d)
            # d = n2d*old_n+d2d*old_d
            # r = n-d*q = (n2n-n2d*q)*old_n + (d2n-d2d*q)*old_d
            n, d = d, r
            [n2n,d2n], [n2d,d2d] = [n2d,d2d], [calc(n2n,n2d,q), calc(d2n,d2d,q)]
            # n = n2n*old_n+d2n*old_d
            # d = n2d*old_n+d2d*old_d
        # n = n2n*old_n+d2n*old_d
        # d = n2d*old_n+d2d*old_d == 0
        gcd, kn, kd = n, n2n, d2n
        kq, kr = divmod(kn, old_d)
        # gcd = n = kn*old_n+kd*old_d = (kq*old_d+kr)*old_n + kd*old_d
        #   = kr*old_n + (kq*old_n+kd)*old_d
        kn, kd = kr, self.add(self.mul(kq,old_n), kd)
        # gcd = kn*old_n+kd*old_d; kn == kn%old_d
        ng = self.floor_div(old_n,g)
        dg = self.floor_div(old_d,g)
        return gcd, kn, kd, ng, dg

class IFieldOps(IEuclideanDomainOps):
    @abstractmethod
    # x != 0
    def __inv_nonzero__(self, x):pass

    def __divmod_nonzero__(self, n, d):
        return self.div(n,d), self.zero
    def arbitrary_norm_EuclideanDomain(self, x):
        return 0 if self.is_zero(x) else 1

    def inv(self, x):
        if self.element_equal(x, self.zero):
            raise ZeroDivisionError
        return self.__inv_nonzero__(x)
    def true_div_int(self, x, i):
        return self.div(x, self.int2element(i))
    def div(self, x, y):
        return self.mul(x, self.inv(y))

class IFiniteFieldOps(IFieldOps, IRingWithCharacteristicOps, IFiniteRingOps):
    @abstractmethod
    # return (characteristic, power, order) # characteristic^power==order
    def get_characteristic_power_order(self):pass
    @property
    def characteristic(self):
        return self.get_characteristic_power_order()[0]
    @property
    def order(self):
        return self.get_characteristic_power_order()[2]




class IRingOpsForRing(ICommutativeRingWithIdentityOps):
    '''for the element type T, s.t. defined (+),(*),(-x),(x-y),(==)'''
    def neg(self, x):
        return -x
    def mul(self, x, y):
        return x*y
    def element_equal(self, x, y):
        return x == y
    def add(self, x, y):
        return x+y

class IFieldOpsForField(IRingOpsForRing, IFieldOps):
    '''for the element type T, s.t. defined (+),(*),(-x),(x-y),(==), (/)'''
    def __inv_nonzero__(self, x):
        return self.one/x
    def div(self, x, y):
        return x/y
class RingOpsForRing(IRingOpsForRing):
    def __init__(self, one, zero, is_element, true_div_int):
        self.__one = one
        self.__zero = zero
        self.__is_element = is_element
        self.__true_div_int = true_div_int
    def is_element(self, x):
        return self.__is_element(x)
    @property
    def one(self):
        return self.__one
    @property
    def zero(self):
        return self.__zero
    def true_div_int(self, x, y):
        return self.__true_div_int(x, y)


class EuclideanDomainOps2ModularGcdDomainOps(IGcdDomainOps):
    # to be override: __modulo__
    def __init__(self, ops, modulus):
        assert isinstance(ops, IEuclideanDomainOps)
        assert ops.is_element(modulus)
        assert not ops.is_zero(modulus)
        self.ops = ops = ops
        self.modulus = M = modulus
        self.__one = self.__mod(ops.one)
    def euclidean_domain_element2modular_ring_element(self, x):
        return self.__mod(x)
    def __mod(self, x):
        return self.__modulo__(x)
    def __modulo__(self, x):
        # to be override; e.g. use computed modulus^-1
        return self.ops.mod(x, self.modulus)
    def is_element(self, x):
        ops = self.ops
        norm = ops.arbitrary_norm_EuclideanDomain
        return ops.is_element(x) and norm(x) < norm(self.modulus)
    @property
    def one(self):
        return self.__one
    @property
    def zero(self):
        return self.ops.zero
    def element_equal(self, x, y):
        return self.ops.element_equal(x,y)
    def neg(self, x):
        return self.__mod(self.ops.neg(x))
    def mul(self, x, y):
        return self.__mod(self.ops.mul(x,y))
    def add(self, x, y):
        return self.__mod(self.ops.add(x,y))

    def __gcd_ex3_nonzero__(self, n, d):
        ops = self.ops
        g, ng, dg = ops.gcd_ex3(n,d)
        M = self.modulus
        may_dg_inv = ops.may_invmod(dg, M)
        if may_dg_inv:
            dg_inv, = may_dg_inv
            # dg^-1 % M == dg_inv
            g = self.mul(g, dg)
            ng = self.mul(ng, dg_inv)
            # dg = self.mul(dg, dg_inv)
            dg = self.one
        return g,ng,dg

    def int2element(self, i):
        return self.__mod(self.ops.int2element(i))
    def mul_int(self, x, i):
        return self.mul(x, self.int2element(i))
    '''
    def pow_uint(self, x, exp):
    '''




class ModularRingOps(IGcdDomainOps):
    '''
modular arithmetic
the modulus
modulo operation
The set of integers {0, 1, 2, …, n − 1} is called the least residue system modulo n.
Any set of n integers, no two of which are congruent modulo n, is called a complete residue system modulo n.
'''
    def __init__(self, modulus):
        assert type(modulus) is int
        assert modulus > 0
        self.modulus = modulus
    def __gcd_ex3_nonzero__(self, n, d):
        # n != 0 != d ==>> modulus != 1
        g = gcd(n,d)
        ng, dg = n//g, d//g
        M = self.modulus
        mul = self.mul
        if gcd(dg, M) == 1:
            inv = invmod(dg, M)
            g = mul(g, dg)
            ng = mul(ng, inv)
            # dg *= inv
            dg = self.one
        '''
        elif gcd(ng, M) == 1:
            inv = invmod(ng, M)
            g = mul(g, ng)
            ng = self.one
            dg = mul(dg, inv)
        '''
        return g,ng,dg
    def is_element(self, x):
        return type(x) is int and 0 <= x < self.modulus
    @property
    def one(self):
        return 1 if self.modulus > 1 else 0
    @property
    def zero(self):
        return 0
    def element_equal(self, x, y):
        return self.sub(x, y) == 0
    def neg(self, x):
        return self.modulus - x if x else 0
    def mul(self, x, y):
        return (x*y) % self.modulus
    def add(self, x, y):
        return (x+y) % self.modulus

    def true_div_int(self, x, i):
        y = i%self.modulus
        xy = Fraction(x, y)
        n = xy.numerator
        d = xy.denominator
        if gcd(d, self.modulus) != 1:
            raise ZeroDivisionError
        inv = invmod(d, self.modulus)
        return self.mul(n, inv)

    def element_equal_int(self, x, i):
        return x == i%self.modulus
    def int2element(self, i):
        return i%self.modulus
    def mul_int(self, x, i):
        assert type(i) is int
        return (x*i)%self.modulus
    def pow_uint(self, x, exp):
        assert type(exp) is int and exp >= 0
        return pow(x, exp, self.modulus)


class IntegerRingOps(IRingOpsForRing):
    def is_element(self, x):
        return type(x) is int
    @property
    def one(self):
        return 1
    @property
    def zero(self):
        return 0
    @property
    def neg_one(self):
        return -1
    def true_div_int(self, x, i):
        q,r = divmod(x, y)
        if r:
            raise ValueError('can not divide')
        return q

    def element_equal_int(self, x, i):
        return x == i
    def int2element(self, i):
        return i
    def mul_int(self, x, i):
        assert type(i) is int
        return x*i
    def pow_uint(self, x, exp):
        assert type(exp) is int and exp >= 0
        return pow(x, exp)




class RationalFieldOps(IFieldOpsForField):
    def is_element(self, x):
        return type(x) is Fraction
    @property
    def one(self):
        return self.int2element(1)
    @property
    def zero(self):
        return self.int2element(0)
    @property
    def neg_one(self):
        return self.int2element(-1)
    def int2element(self, i):
        assert type(i) is int
        return Fraction(i)



class PrimeModularFieldOps(ModularRingOps, IFiniteFieldOps):
    def __init__(self, prime_modulus):
        assert prime_modulus >= 2
        primes = [2,3,5,7,11]
        assert prime_modulus in primes or all(prime_modulus%p for p in primes)
        super().__init__(prime_modulus)
    def get_characteristic_power_order(self):
        p = self.modulus
        return (p, 1, p)
    def __inv_nonzero__(self, x):
        inv = invmod(x, self.modulus)
        return inv

TheIntegerRingOps = IntegerRingOps()
TheRationalFieldOps = RationalFieldOps()
TheField7 = PrimeModularFieldOps(7)

if __name__ == '__main__':
    for n in list(globals()): print(n)
    print()
    for n in __all__:
        for n in dir(globals()[n]): print(n)
    print()
    del n

