

__all__ = '''
    IPowers
    IPowers__product
    IPowers__cache_2pows
    IPowers__cache_all
    RingOps2Powers__cache_all
    '''.split()
from abc import ABCMeta, abstractmethod
from nn_ns.math_nn.ops.IRingOps import IRingWithIdentityOps

class IPowers(metaclass=ABCMeta):
    @abstractmethod
    # self[i] = base^i
    def __getitem__(self, exp):
        assert exp >= 0
        return self.__get_pow__(exp)
    # get_pow_2pow(exp) = base^(2^exp)
    def get_pow_2pow(self, exp):
        assert exp >= 0
        return self[1<<exp]
    # get_one() = 1
    def get_one(self):
        return self[0]
    def get_base(self):
        return self.get_pow_2pow(0)

def uint2bitstrBE(u):
    assert u >= 0
    return bin(u)[2:]
def uint2bitstrLE(u):
    assert u >= 0
    return bin(u)[:1:-1]
assert uint2bitstrLE(1) == '1'
assert uint2bitstrBE(1) == '1'
assert uint2bitstrLE(0) == '0'
assert uint2bitstrBE(0) == '0'
def uint2two_expsLE(u):
    # uint2two_expsLE u = [i | i <-[0..], 2^i & u != 0]
    return [i for i, bit in enumerate(uint2bitstrLE(u)) if bit=='1']
def uint2iter_low_bin_uintsBE(u):
    # u = 0b1001010 => iter [0b1001010,0b1010, 0b10, 0b0]
    yield u
    expsLE = uint2two_expsLE(u)
    one_lshifts = []
    one_lshift = 1
    pre_exp = 0
    for exp in expsLE:
        one_lshift <<= exp - pre_exp
        one_lshifts.append(one_lshift)
        pre_exp = exp
    for one_lshift in one_lshifts:
        u -= one_lshift
        yield u
    assert u == 0
def pint_rshift_until_odd(i):
    # pint_rshift_until_odd i = odd exp where i == odd*2^exp
    assert i > 0
    m = 0
    while not(i & 1):
        m += 1
        i >>= 1
    return i, m

class IPowers__product(IPowers):
    @abstractmethod
    def product(self, xs):pass
    def get_one(self):
        return self.product()
    def mul(self, lhs, rhs):
        return self.product([lhs, rhs])
class IPowers__cache_2pows(IPowers__product):
    @abstractmethod
    # get_pow_2pow(exp) = base^(2^exp)
    #   fetch or calc and store
    def get_pow_2pow(self, exp):pass
    def __getitem__(self, exp):
        assert exp >= 0
        if exp == 0:
            return self.get_one()
        ls = uint2two_expsLE(exp)
        return self.product(map(self.get_pow_2pow, ls))
        ### old version
        # exp = odd * 2^m
        odd, m = pint_rshift_until_odd(exp)
        # exp = odd * 2^m = 2^m + (odd-1)*2^m
        # base^exp = base^(2^m) * base^((odd-1) * 2^m)
        r = get_pow_2pow(m) # r = base^(2^m)
        i = odd >> 1
        while i:
            m += 1
            odd, dm = pint_rshift_until_odd(i)
            m += dm
            r = mul(r, get_pow_2pow(m))
            i = odd >> 1
        return r
class IPowers__cache_all(IPowers__cache_2pows):
    @abstractmethod
    # return () | (base^exp,) # exp=0or1 should return (_,)
    def get_may_cached_pow(self, exp):pass
    @abstractmethod
    # pow = base^exp
    def store(self, exp, pow):pass
    def get_pow_2pow(self, exp):
        assert exp >= 0
        _2exp = exp
        exp = org_exp = 1<<_2exp
        get_may_cached_pow = self.get_may_cached_pow
        mul = self.mul
        store = self.store
        while exp:
            may_pow = get_may_cached_pow(exp)
            if may_pow != (): break
            exp >>= 1
        else:
            # err: get_may_cached_pow(1) == ()
            raise logic-error
        [pow] = may_pow
        while exp != org_exp:
            exp <<= 1
            pow = mul(pow, pow)
            store(exp, pow)
        return pow

    def __getitem__(self, exp):
        assert exp >= 0
        if exp == 0: return self.get_one()
        if exp == 1: return self.get_base()
        org_exp = exp
        expsBE = []
            # expsBE[0] = org_exp
            # expsBE[i+1] = expsBE[i] - (2^??)
        get_may_cached_pow = self.get_may_cached_pow
        # base^0,base^1 should in cached_pow
        for exp in uint2iter_low_bin_uintsBE(exp):
            may_pow = get_may_cached_pow(exp)
            expsBE.append(exp)
            if may_pow != (): break
        else:
            raise logic-error
        # bug: if exp == 0: raise logic-error
        [known_pow] = may_pow
        known_exp = exp; del exp
        if known_exp == org_exp: return known_pow

        _2expsLE = uint2two_expsLE(org_exp-known_exp)
            # org_exp-known_exp = sum(2^exp for exp in _2expsLE)
        it = map(self.get_pow_2pow, _2expsLE)
        mul = self.mul
        store = self.store
        for _2exp, pow in zip(_2expsLE, it):
            known_pow = mul(known_pow, pow)
            known_exp += 1<<_2exp
            store(known_exp, known_pow)
        assert known_exp == org_exp
        return known_pow

class RingOps2Powers__cache_all(IPowers__cache_all):
    def __init__(self, ring_ops, base):
        assert isinstance(ring_ops, IRingWithIdentityOps)
        assert ring_ops.is_element(base)
        self.ring_ops = ring_ops
        self.base = base
        # bug: self.exp2may_pow = {0:ring_ops.one, 1:base}
        self.exp2may_pow = {0:(ring_ops.one,), 1:(base,)}
    @property
    def product(self):
        return self.ring_ops.product
    @property
    def mul(self):
        return self.ring_ops.mul
    def get_one(self):
        return self.ring_ops.one

    def get_may_cached_pow(self, exp):
        return self.exp2may_pow.get(exp, ())
    def store(self, exp, pow):
        self.exp2may_pow[exp] = (pow,)

if __name__ == '__main__':
    def _test():
        from types import SimpleNamespace
        ops = SimpleNamespace()
        ops.one = 1
        from nn_ns.math_nn.ops.IRingOps import TheIntegerRingOps
        ops = TheIntegerRingOps
        powers = RingOps2Powers__cache_all(ops, 3)
        exps = list(range(100))
        assert list(map(powers.__getitem__, exps)) == list(map(3 .__pow__, exps))
    _test()
    del _test


