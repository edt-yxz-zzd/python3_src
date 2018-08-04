


__all__ = '''
    IPrimeNumberProof
    IPrimeNumberProofWithPrimitiveRoot
    PrimeNumberProof_by_primitive_root
    PIntFactorization

    '''.split()

from abc import abstractmethod, ABCMeta
#from nn_ns.math_nn.smalls import II_base_exp, divides
from types import MappingProxyType
from collections.abc import Mapping
from seed.helper.repr_input import repr_helper

def II_base_exp(base_exp_pairs):
    n = 1
    for base, exp in base_exp_pairs:
        n *= base**exp
    return n


def get_the_prime_number(proof):
    assert isinstance(proof, IPrimeNumberProof)
    p = type(proof).__get_the_prime_number__(proof)
    assert is_pint(p)
    return p
def get_a_primitive_root(proof):
    assert isinstance(proof, IPrimeNumberProofWithPrimitiveRoot)
    r = type(proof).__get_a_primitive_root__(proof)
    assert is_pint(r)
    return r

def is_pint(i):
    return type(i) is int and i > 0
def is_pint_factors(factors):
    # [(base:PInt, exp:PInt)]
    # donot test unique and prime
    return all(is_pint(base) and is_pint(exp) for base, exp in factors)
def is_pint_factor2exp(factor2exp):
    return isinstance(factor2exp, Mapping) and is_pint_factors(factor2exp.items())
def is_pint_factor2exp_of(factor2exp, pint):
    return (is_pint(pint)
        and is_pint_factor2exp(factor2exp)
        and II_base_exp(factor2exp.items()) == pint
        )

def is_prime_number_proof_of(proof, pint):
    return (is_pint(pint) and isinstance(proof, IPrimeNumberProof)
        and get_the_prime_number(proof) == pint
        )
def is_factor2prime_proof(factor2prime_proof):
    return (isinstance(factor2prime_proof, Mapping)
        and all(is_prime_number_proof_of(proof, pint)
                for pint, proof in factor2prime_proof.items())
        )
class PIntFactorization:
    def __init__(self, pint, factor_exp_pairs, factor2prime_proof):
        factor2exp = dict(factor_exp_pairs)
        if not isinstance(factor2prime_proof, Mapping):
            factor2prime_proof = dict(factor2prime_proof)
        factor2prime_proof = {p:factor2prime_proof[p] for p in factor2exp}

        if not is_factor2prime_proof(factor2prime_proof): raise TypeError
        if pint is None:
            if not is_pint_factor2exp(factor2exp): raise TypeError
            pint = II_base_exp(factor2exp.items())
        else:
            if not is_pint_factor2exp_of(factor2exp, pint): raise TypeError
        self.__factor2exp = MappingProxyType(factor2exp)
        self.__factor2prime_proof = MappingProxyType(factor2prime_proof)
        self.__pint = pint
    @property
    def factor2exp(self): return self.__factor2exp
    @property
    def factor2prime_proof(self): return self.__factor2prime_proof
    @property
    def the_pint(self): return self.__pint
    def __repr__(self):
        return repr_helper(self, self.the_pint
            , dict(self.factor2exp), dict(self.factor2prime_proof)
            )

class IPrimeNumberProof(metaclass=ABCMeta):
    'not Integral!!!!'
    @abstractmethod
    def __get_the_prime_number__(self):pass
class IPrimeNumberProofWithPrimitiveRoot(IPrimeNumberProof):
    @abstractmethod
    def __get_a_primitive_root__(self):pass

def test_prime_number(p, primitive_root, phi_p_factorization):
    return (is_pint(p) and type(primitive_root) is int
        and isinstance(phi_p_factorization, PIntFactorization)
        and phi_p_factorization.the_pint == p-1
        and pow(primitive_root, p-1, p) == 1
        and all(pow(primitive_root, p//factor, p) != 1
                for factor in phi_p_factorization.factor2prime_proof)
        )

class PrimeNumberProof_by_primitive_root(IPrimeNumberProofWithPrimitiveRoot):
    'not Integral!!!!'
    def __init__(self, p, primitive_root, phi_p_factorization):
        try:
            if not test_prime_number(p, primitive_root, phi_p_factorization): raise TypeError
        except:
            print(p, primitive_root, phi_p_factorization)
            raise
        if not (0 < primitive_root < p): raise TypeError

        self.__prime = p
        self.__phi_p_factorization = phi_p_factorization
        self.__primitive_root = primitive_root
    def __get_the_prime_number__(self):
        return self.__prime
    def __get_a_primitive_root__(self):
        return self.__primitive_root
    def get_phi_p_factorization(self):
        # return a sorted pairs in tuple
        return self.__phi_p_factorization
    def list_args_as_triples(self):
        # iff all prime_proofs inside are PrimeNumberProof_by_primitive_root
        d = self.to_dict()
        return sorted((p, factor2exp, r) for p, (factor2exp, r) in d.items())
    def to_dict(self, output=None):
        # {prime_number : ((proof,) | (phi_p_factor2exp, primitive_root))}
        def this_func(proof:'may not __class__'):
            # assert isinstance(proof, IPrimeNumberProof)
            p = get_the_prime_number(proof)
            if p in output: return
            if not isinstance(proof, __class__):
                output[p] = (proof,)
                return
            r = get_a_primitive_root(proof)
            phi_p_factorization = proof.get_phi_p_factorization()
            factor2exp = phi_p_factorization.factor2exp
            factor2prime_proof = phi_p_factorization.factor2prime_proof
            output[p] = (factor2exp, r) # factor2exp :: MappingProxyType
            for q in factor2exp:
                this_func(factor2prime_proof[q])
            return
        if output is None: output = {}
        this_func(self)
        return output
    @classmethod
    def from_dict(cls, p, d):
        # d: {prime_number : ((proof,) | (phi_p_factor2exp, primitive_root))}
        #   # output of to_dict()
        if not (p > 0): raise ValueError
        def this_func(p):
            # prime2proof
            t = d[p]
            if len(t) == 1:
                [proof] = t
                return proof
            phi_p_factor2exp, primitive_root = t
            phi_p_factor2proof = {q: this_func(q) for q in phi_p_factor2exp}
            phi_p_factorization = PIntFactorization(
                                p-1, phi_p_factor2exp, phi_p_factor2proof)
            proof = cls(p, primitive_root, phi_p_factorization)
            return proof
        return this_func(p)



    def __hash__(self):
        return hash(self.get_prime_and_root())
    def __repr__(self):
        return '{}({}, {}, {})'.format(
            type(self).__name__
            , self.__prime
            , self.__primitive_root
            , self.__phi_p_factorization
            )
    def get_prime_and_root(self):
        return self.__prime, self.__primitive_root
    def __ne__(self, other):
        if type(other) != type(self): return NotImplemented
        return not (self == other)
    def __eq__(self, other):
        if type(other) != type(self): return NotImplemented
        return self.get_prime_and_root() == other.get_prime_and_root()
    def __lt__(self, other):
        if type(other) != type(self): return NotImplemented
        return self.get_prime_and_root() < other.get_prime_and_root()
    def __le__(self, other):
        if type(other) != type(self): return NotImplemented
        return self.get_prime_and_root() <= other.get_prime_and_root()
    def __gt__(self, other):
        if type(other) != type(self): return NotImplemented
        return self.get_prime_and_root() > other.get_prime_and_root()
    def __ge__(self, other):
        if type(other) != type(self): return NotImplemented
        return self.get_prime_and_root() >= other.get_prime_and_root()




def find_a_primitive_root_of(p, phi_p_factors):
    return find_the_primitive_root_of(p)
def find_the_primitive_root_of(p, phi_p_factors):
    phi_p_factors = tuple(phi_p_factors)
    for i in range(1, p//2):
        if is_primitive_root_of(i, p, phi_p_factors):
            return i
    raise ValueError(f'{p} is not prime')
def is_primitive_root_of(root, the_prime_number, phi_p_factors:'[(PInt, PInt)]'):
    assert II_base_exp(phi_p_factors) == p-1
    return pow(root, p-1, p) == 1 and all(pow(root, p//q, p) != 1 for q, exp in phi_p_factors)



if __name__ == "__main__":
    from nn_ns.math_nn.factor_int import factor_int
    from nn_ns.math_nn.numbers.certificated_factors import certificated_factors
    from nn_ns.math_nn.integer.CertificatedPrime import CertificatedPrime as CertificatedPrime__old
    def old2new_CertificatedPrimeNumber(old):
        # CertificatedPrime__old to CertificatedPrimeNumber
        assert isinstance(old, CertificatedPrime__old)
        def this_func(old):
            p = int(old)
            phi_p = p-1
            phi_p_factor2exp = {int(q):exp for q, exp in old.phi_p_factors.items()}
            phi_p_factor2proof = {int(q):this_func(q) for q in old.phi_p_factors}
            return PrimeNumberProof_by_primitive_root(
                int(old)
                , old.root
                , PIntFactorization(phi_p, phi_p_factor2exp, phi_p_factor2proof)
                )
        return this_func(old)
    for i, factors in enumerate(certificated_factors.get_first(100)):
        if factors is None:
            print(i)
            continue
        if len(factors) == 1:
            [(p, exp)] = factors.items()
            if exp == 1:
                assert i == p
                new = old2new_CertificatedPrimeNumber(p)
                print(new)
                print(new.to_dict())
                print(new.list_args_as_triples())
                assert new == new.from_dict(i, new.to_dict())


