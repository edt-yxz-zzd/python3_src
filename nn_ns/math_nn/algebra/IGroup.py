
'''
identity
associative
commutative
'''
from abc import abstractmethod
from .IAlgebra import IAlgebra, ISet

class IMagma(ISet, IAlgebra):
    # magma or groupoid
    # a set with a not necessarily associative binary operation
    # the magma or closure axiom: the set is closed under the operation
    # def closure_binary_operation(self, x, y):pass
    # [are_elements(x,y)] ==>> [is_element(mul(x,y))]
    @abstractmethod
    def mul(self, x, y):pass
    # e.g. mul x y ::= x - y
class IMagma_idempotent_mul(IMagma):
    # [is_element(x)] ==>> [mul(x,x) == x]
    pass
class IMagma_commutative(IMagma):
    # a commutative magma
    # [are_elements(x,y)] ==>> [mul(x,y) == mul(y,x)]
    pass
class ISemigroup(IMagma):
    # an associative magma
    # [are_elements(x,y,z)] ==>> [mul(x, mul(y, z)) == mul(mul(x,y), z)]
    pass
class ISemilattice(ISemigroup, IMagma_commutative, IMagma_idempotent_mul):
    # e.g. mul x y = max x y
    pass
class IQuasigroup(IMagma):
    # Latin square property:
    #   [are_elements(n,d)] ==>>
    #       [is_element(left_div(n,d))][mul(d, left_div(n,d)) == n]
    #       [is_element(q)][mul(d, q) == n] ==>> [q == left_div(n,d)]
    #       [is_element(right_div(n,d))][mul(right_div(n,d), d) == n]
    #       [is_element(q)][mul(q, d) == n] ==>> [q == right_div(n,d)]
    # left_div: d*q=n, q=d\n
    # right_div: q*d=n, q=n/d
    @abstractmethod
    def left_div(self, n, d):pass
    @abstractmethod
    def right_div(self, n, d):pass
class IQuasigroup_commutative(IQuasigroup, IMagma_commutative):
    # [d*q = q*d = n] ==>> [q = d\n = n/d]
    # [div(n,d) == left_div(n,d) == right_div(n,d)]
    @abstractmethod
    def div(self, n, d):pass
    def left_div(self, n, d):
        return self.div(n,d)
    def right_div(self, n, d):
        return self.div(n,d)
class IMagma_identity(IMagma):
    # [is_element(identity)]
    # [is_element(x)] ==>> [mul(x, identity) == x == mul(identity, x)]
    @property
    @abstractmethod
    def identity(self):pass
class ILoop(IQuasigroup, IMagma_identity):
    # [mul(left_inv(x), x) == identity]
    # [left_inv(x) == right_div(identity, x)]
    # [mul(x, right_inv(x)) == identity]
    # [right_inv(x) == left_div(identity, x)]
    def left_inv(self, x):
        return self.right_div(self.identity, x)
    def right_inv(self, x):
        return self.left_div(self.identity, x)
class ILoop_inv(ILoop):
    # x*r = e = r*x
    # [inv(x) == left_inv(x) == right_inv(x)]
    @abstractmethod
    def inv(self, x):pass
    def left_inv(self, x):
        return self.inv(x)
    def right_inv(self, x):
        return self.inv(x)
class IMonoid(ISemigroup, IMagma_identity):
    # a semigroup with identity
    pass
class IGroup(ILoop_inv, IMonoid):
    pass
class IAbelianGroup(IGroup, IQuasigroup_commutative):
    pass



