#__all__:goto
r'''[[[
e ../../python3_src/seed/math/ops/algebra/IGroupOps.py
view ../../python3_src/nn_ns/math_nn/algebra/IGroup.py
view ../../python3_src/nn_ns/math_nn/algebra/is_group.py





seed.math.ops.algebra.IGroupOps
py -m nn_ns.app.debug_cmd   seed.math.ops.algebra.IGroupOps -x
py -m nn_ns.app.doctest_cmd seed.math.ops.algebra.IGroupOps:__doc__ -ff -v
py_adhoc_call   seed.math.ops.algebra.IGroupOps   @f
from seed.math.ops.algebra.IGroupOps import *

py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.math.ops.algebra.IGroupOps:IMagmaOps,IQuasigroupOps,ICommutativeQuasigroupOps,IMagmaOps__has_identity4mul,ILoopOps,ILoopOps__has_inv    =IMagmaOps =IQuasigroupOps =ICommutativeQuasigroupOps =IMagmaOps__has_identity4mul =ILoopOps =ILoopOps__has_inv      --exclude='lambda nm:nm.startswith("_")'


#]]]'''
__all__ = r'''

IMagmaOps           IGroupoidOps
    ISemigroupOps   IAssociativeMagmaOps
        IMonoidOps
    ICommutativeMagmaOps
    IIdempotentMagmaOps
        ISemilatticeOps

    IQuasigroupOps
        ICommutativeQuasigroupOps
        ILoopOps

    IMagmaOps__has_identity4mul
        ILoopOps
            ILoopOps__has_inv
                ICommutativeLoopOps
                IGroupOps

        IMonoidOps
            ICommutativeMonoidOps
            IGroupOps
                IAbelianGroupOps    ICommutativeGroupOps




IMagmaOps
IGroupoidOps
ISemigroupOps
IAssociativeMagmaOps
ICommutativeMagmaOps
IIdempotentMagmaOps
ISemilatticeOps
IQuasigroupOps
ICommutativeQuasigroupOps
IMagmaOps__has_identity4mul
ILoopOps
ILoopOps__has_inv
ICommutativeLoopOps
IMonoidOps
ICommutativeMonoidOps
IGroupOps
IAbelianGroupOps
ICommutativeGroupOps

'''.split()#'''
__all__


from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.math.ops.algebra.IAlgebraOps import IAlgebraOps, NonInvertibleError, NonInvertibleError__not_injective, NonInvertibleError__out_of_domain, NonInvertibleError__not_implemented, NonInvertibleError__not_commutative

r'''[[[
magma
    新世纪英汉科技大词典
        乳浆剂
        稠液
        岩架
        岩浆
    21世纪英汉汉英双向词典
        <<不可数名词>>‘地质’岩浆



commutative property 交换律
associative property 结合律
distributive property 分配律

associative
idempotent
commutative

distributive IRingOps
#]]]'''#'''
class IMagmaOps(IAlgebraOps):
    r'''magma or groupoid

    [@[magma :<- Magma] -> @[x,y :<- magma] -> [mul(x,y) <- magma]]
        # [closure]

    [not [@[magma :<- Magma] -> @[x,y,z :<- magma] -> [mul(x,mul(y,z)) == mul(mul(x,y),z)]]]
        # [neednot be associative]

    [not [@[magma :<- Magma] -> @[x,y :<- magma] -> [mul(x,y) == mul(y,x)]]]
        # [neednot be commutative]

    [not [@[magma :<- Magma] -> @[x :<- magma] -> [mul(x,x) == x]]]
        # [neednot be idempotent]


    [magma == groupoid =[def]= a set with a not necessarily associative binary operation ++ the magma or closure axiom: the set is closed under the operation]


    [mul :: int -> int -> int]:
        [mul x y =[def]= x - y]:
            [not associative mul]
            [not commutative mul]
            [not idempotent mul]
        [mul x y =[def]= max(x, y)]:
            [associative mul]
            [commutative mul]
            [idempotent mul]
        [mul x y =[def]= gcd(x, y)]:
            [associative mul]
            [commutative mul]
            or?[idempotent mul] #up to +-1
            or?[not idempotent mul] #[gcd() >= 0]

    '''#'''
    __slots__ = ()
    ___all___ = r'''
#abstract_methods:
    `is_mul_associative
    `is_mul_commutative
    `is_mul_idempotent
    `mul
    `is_order_finite
    `get_xorder4mul
#concrete_methods:
    '''#'''
    #___all___

    @abstractmethod
    def mul(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> z'
    @abstractmethod
    def is_mul_associative(ops, /):
        'ops<z> -> bool'
        # e.g. [mul x y =[def]= x - y]
        return False
    @abstractmethod
    def is_mul_commutative(ops, /):
        'ops<z> -> bool'
        # e.g. [mul x y =[def]= x - y]
        return False
    @abstractmethod
    def is_mul_idempotent(ops, /):
        'ops<z> -> bool'
        # e.g. [mul x y =[def]= x - y]
        return False

    @abstractmethod
    def is_order_finite(ops, /):
        'ops<z> -> bool'
        return False
    @abstractmethod
    def get_xorder4mul(ops, /):
        'ops<z> -> xorder4mul/(-1|uint|...) #(-1 if not is_order_finite() else (order4mul/uint if known else ...)) # '
        return (-1 if not ops.is_order_finite() else ...)
IGroupoidOps = IMagmaOps

class ISemigroupOps(IMagmaOps):
    r'''semigroup =[def]= associative magma

    [@[magma :<- Semigroup] -> @[x,y,z :<- magma] -> [mul(x,mul(y,z)) == mul(mul(x,y),z)]]

    '''#'''
    __slots__ = ()
    @override
    def is_mul_associative(ops, /):
        'ops<z> -> bool'
        # e.g. [mul x y =[def]= max x y]
        return True
    @classmethod
    @override
    def __instancehook__(cls, ops, /):
        # ABCMeta::__instancehook__
        if cls is __class__:
            return isinstance(ops, IMagmaOps) and ops.is_mul_associative()
        return NotImplemented
IAssociativeMagmaOps = ISemigroupOps

class ICommutativeMagmaOps(IMagmaOps):
    r'''commutative magma

    [@[magma :<- CommutativeMagma] -> @[x,y :<- magma] -> [mul(x,y) == mul(y,x)]]

    '''#'''
    __slots__ = ()
    @override
    def is_mul_commutative(ops, /):
        'ops<z> -> bool'
        # e.g. [mul x y =[def]= max x y]
        return True
    @classmethod
    @override
    def __instancehook__(cls, ops, /):
        # ABCMeta::__instancehook__
        if cls is __class__:
            return isinstance(ops, IMagmaOps) and ops.is_mul_commutative()
        return NotImplemented
class IIdempotentMagmaOps(IMagmaOps):
    r'''idempotent magma

    [@[magma :<- IdempotentMagma] -> @[x :<- magma] -> [mul(x,x) == x]]

    '''#'''
    __slots__ = ()
    @override
    def is_mul_idempotent(ops, /):
        'ops<z> -> bool'
        # e.g. [mul x y =[def]= max x y]
        return True
    @classmethod
    @override
    def __instancehook__(cls, ops, /):
        # ABCMeta::__instancehook__
        if cls is __class__:
            return isinstance(ops, IMagmaOps) and ops.is_mul_idempotent()
        return NotImplemented

class ISemilatticeOps(IIdempotentMagmaOps, ICommutativeMagmaOps, IAssociativeMagmaOps):
    'e.g. [mul x y =[def]= max x y]'
    __slots__ = ()
    @classmethod
    @override
    def __instancehook__(cls, ops, /):
        # ABCMeta::__instancehook__
        if cls is __class__:
            return (isinstance(ops, IMagmaOps)
                and ops.is_mul_idempotent()
                and ops.is_mul_commutative()
                and ops.is_mul_associative()
                )
        return NotImplemented
    pass

class IQuasigroupOps(IMagmaOps):
    r'''[[[
    left_div: d*q=n, q=d\n
    right_div: q*d=n, q=n/d
        #square matrix

    # Latin square property:
    latin_square_property:
        [@[magma :<- Quasigroup] -> @[n,d :<- magma] -> [left_div(n,d) <- magma] -> [mul(d, left_div(n,d)) == n]]
        [@[magma :<- Quasigroup] -> @[n,d :<- magma] -> [right_div(n,d) <- magma] -> [mul(right_div(n,d), d) == n]]
        [@[magma :<- Quasigroup] -> @[q,d :<- magma] -> [left_div(mul(d,q),d) == q]]
        [@[magma :<- Quasigroup] -> @[q,d :<- magma] -> [right_div(mul(q,d),d) == q]]

    Quasigroup <==> [has left_div][has right_div]
    #]]]'''#'''
    __slots__ = ()
    ___all___ = r'''
#abstract_methods:
    `is_mul_associative
    `is_mul_commutative
    `is_mul_idempotent
    `left_div
    `mul
    `right_div
    `is_order_finite
    `get_xorder4mul
#concrete_methods:
    '''#'''
    #___all___

    @abstractmethod
    def left_div(ops, n, d, /):
        r'ops<z> -> n/z -> d/z -> q/z # [q := (d\n)][d*(d\n) == n]'
        r'-> (d\n) # [d*(d\n) == n]'
    @abstractmethod
    def right_div(ops, n, d, /):
        r'ops<z> -> n/z -> d/z -> q/z # [q := (n/d)][(n/d)*d == n]'
        r'-> (n/d) # [(n/d)*d == n]'
class ICommutativeQuasigroupOps(IQuasigroupOps, ICommutativeMagmaOps):
    # [d*q = q*d = n] ==>> [q = d\n = n/d]
    # [div(n,d) == left_div(n,d) == right_div(n,d)]
    __slots__ = ()
    ___all___ = r'''
#abstract_methods:
    `is_mul_associative
    `is_mul_idempotent
    `mul
    `truediv
    `is_order_finite
    `get_xorder4mul
#concrete_methods:
    is_mul_commutative
    left_div
    right_div
    '''#'''
    #___all___

    @abstractmethod
    #def div(ops, n, d, /):
    def truediv(ops, n, d, /):
        r'ops<z> -> n/z -> d/z -> q/z # [q := (n/d)][(n/d)*d == n == d*(n/d)]'
        r'-> (n/d) # [(n/d)*d == n == d*(n/d)]'
    @override
    def left_div(ops, n, d, /):
        r'ops<z> -> n/z -> d/z -> q/z # [q := (d\n)][d*(d\n) == n]'
        r'-> (d\n) # [d*(d\n) == n]'
        return ops.truediv(n,d)
    @override
    def right_div(ops, n, d, /):
        r'ops<z> -> n/z -> d/z -> q/z # [q := (n/d)][(n/d)*d == n]'
        r'-> (n/d) # [(n/d)*d == n]'
        return ops.truediv(n,d)

class IMagmaOps__has_identity4mul(IMagmaOps):
    r'''[[[

    [@[magma :<- Magma__has_identity] -> [identity4mul <- magma]]

    [@[magma :<- Magma__has_identity] -> @[x :<- magma] -> [mul(identity4mul, x) == x == mul(x, identity4mul)]]

    #]]]'''#'''
    __slots__ = ()
    ___all___ = r'''
#abstract_methods:
    `get_identity4mul
    `is_mul_associative
    `is_mul_commutative
    `is_mul_idempotent
    `mul
    `is_order_finite
    `get_xorder4mul
#concrete_methods:
    '''#'''
    #___all___

    @abstractmethod
    def get_identity4mul(ops, /):
        'ops<z> -> identity4mul/z'

class ILoopOps(IQuasigroupOps, IMagmaOps__has_identity4mul):
    r'''[[[

    [@[magma :<- Loop] -> @[d :<- magma] -> [mul(left_inv_(d), d) == identity4mul == mul(d, right_inv_(d))]]
    ==>>:
    [@[magma :<- Loop] -> @[d :<- magma] -> [[left_inv_(d) == right_div(identity4mul, d)][right_inv_(d) == left_div(identity4mul, d)]]]

    !! Quasigroup <==> [has left_div][has right_div]
    Loop <==> [has left_div][has right_div][has identity4mul] [has left_inv_][has right_inv_]


    [[
    left_div,right_div
    left_inv_,right_inv_
    ===
    #eg:square matrix
    left_div:  [d*q == n][q := d\n]
        [d*left_div(n,d) == n]
        [left_div(n,d) == d\n]
        [d*(d\n) == n]
    right_div: [q*d == n][q := n/d]
        [right_div(n,d)*d == n]
        [right_div(n,d) == n/d]
        [(n/d)*d == n]

    left_inv_: [left_inv_(d)*d == 1]
        [left_inv_(d) == 1/d == right_div(1,d)]
        [(1/d)*d == 1]
    right_inv_: [d*right_inv_(d) == 1]
        [right_inv_(d) == d\1 == left_div(1,d)]
        [d*(d\1) == 1]
    ]]

    NOTE:
    [[
    left_inv_,right_inv_ =?= inv_
    ===
    [[left_inv_ =!= right_inv_] -> [[not is_mul_associative][not is_mul_commutative]]]
    <==>:
    [[is_mul_associative] -> [left_inv_ === right_inv_]]
    [[is_mul_commutative] -> [left_inv_ === right_inv_]]
    proof:
    [[is_mul_associative] -> [left_inv_ === right_inv_]]
        [[proof:
        [left_inv_(d)
        == left_inv_(d)*1
        !! [d*right_inv_(d) == 1]
        == left_inv_(d)*(d*right_inv_(d))
        !! [is_mul_associative]
        == (left_inv_(d)*d)*right_inv_(d)
        !! [left_inv_(d)*d == 1]
        == 1*right_inv_(d)
        == right_inv_(d)
        ]
        DONE
        ]]

    [[is_mul_commutative] -> [left_inv_ === right_inv_]]
        [[proof:
        [d*left_inv_(d)
        !! [is_mul_commutative]
        == left_inv_(d)*d
        !! [left_inv_(d)*d == 1]
        == 1
        !! [d*right_inv_(d) == 1]
        == d*right_inv_(d)
        ]
        DONE
        ]]
    ]]



    #]]]'''#'''
    __slots__ = ()
    ___all___ = r'''
#abstract_methods:
    `get_identity4mul
    `is_mul_associative
    `is_mul_commutative
    `is_mul_idempotent
    `left_inv_
    `mul
    `right_inv_
    `is_order_finite
    `get_xorder4mul
#concrete_methods:
    left_div
    right_div
    '''#'''
    #___all___

    #@newmethod
    @abstractmethod
    def left_inv_(ops, d, /):
        r'ops<z> -> d/z -> q/z # [q := (1/d)][(1/d)*d == 1]'
        return ops.right_div(ops.get_identity4mul(), d)
    #@newmethod
    @abstractmethod
    def right_inv_(ops, d, /):
        r'ops<z> -> d/z -> q/z # [q := (d\1)][d*(d\1) == 1]'
        return ops.left_div(ops.get_identity4mul(), d)
    @override
    def left_div(ops, n, d, /):
        r'ops<z> -> n/z -> d/z -> q/z # [q := (d\n)][d*(d\n) == n]'
        r'-> (d\n) # [d*(d\n) == n]'
        # [d * ((d\1)*n) == n]
        # [((d\1)*n) == (d\n)]
        return ops.mul(ops.right_inv_(d), n)
    @override
    def right_div(ops, n, d, /):
        r'ops<z> -> n/z -> d/z -> q/z # [q := (n/d)][(n/d)*d == n]'
        r'-> (n/d) # [(n/d)*d == n]'
        # [(n*(1/d)) * d == n]
        # [(n*(1/d)) == (n/d)]
        return ops.mul(n, ops.left_inv_(d))

class ILoopOps__has_inv(ILoopOps):
    r'''[[[
    !! Loop <==> [has left_div][has right_div][has identity4mul] [has left_inv_][has right_inv_]
    Loop__has_inv <==> [has left_div][has right_div][has identity4mul][left_inv_ === right_inv_ === inv_] [has left_inv_][has right_inv_][has inv_]
    #]]]'''#'''
    # x*r = e = r*x
    # [inv_(x) == left_inv_(x) == right_inv_(x)]
    __slots__ = ()
    ___all___ = r'''
#abstract_methods:
    `get_identity4mul
    `inv_
    `is_mul_associative
    `is_mul_commutative
    `is_mul_idempotent
    `mul
    `is_order_finite
    `get_xorder4mul
#concrete_methods:
    left_div
    left_inv_
    right_div
    right_inv_
    '''#'''
    #___all___

    #@newmethod
    @abstractmethod
    def inv_(ops, d, /):
        r'ops<z> -> d/z -> q/z # [q := (1/d)][(1/d)*d == 1 == d*(1/d)]'
        #return ops.right_div(ops.get_identity4mul(), d)

    @override
    def left_inv_(ops, d, /):
        r'ops<z> -> d/z -> q/z # [q := (1/d)][(1/d)*d == 1]'
        return ops.inv_(d)
    @override
    def right_inv_(ops, d, /):
        r'ops<z> -> d/z -> q/z # [q := (d\1)][d*(d\1) == 1]'
        return ops.inv_(d)
class ICommutativeLoopOps(ILoopOps__has_inv, ICommutativeQuasigroupOps):
    __slots__ = ()
    @override
    def truediv(ops, n, d, /):
        r'ops<z> -> n/z -> d/z -> q/z # [q := (n/d)][(n/d)*d == n == d*(n/d)]'
        r'-> (n/d) # [(n/d)*d == n == d*(n/d)]'
        return ops.mul(n, ops.inv_(d))
    @classmethod
    @override
    def __instancehook__(cls, ops, /):
        # ABCMeta::__instancehook__
        if cls is __class__:
            return (isinstance(ops, ILoopOps__has_inv)
                and ops.is_mul_commutative()
                )
        return NotImplemented

class IMonoidOps(ISemigroupOps, IMagmaOps__has_identity4mul):
    r'''Monoid =[def]= a semigroup with identity4mul

    Monoid <==> [associative mul][has identity4mul]

    '''#'''
    __slots__ = ()
    @classmethod
    @override
    def __instancehook__(cls, ops, /):
        # ABCMeta::__instancehook__
        if cls is __class__:
            return (isinstance(ops, IMagmaOps__has_identity4mul)
                and ops.is_mul_associative()
                )
        return NotImplemented
    pass
class ICommutativeMonoidOps(IMonoidOps, ICommutativeMagmaOps):
    __slots__ = ()
    @classmethod
    @override
    def __instancehook__(cls, ops, /):
        # ABCMeta::__instancehook__
        if cls is __class__:
            return (isinstance(ops, IMagmaOps__has_identity4mul)
                and ops.is_mul_associative()
                and ops.is_mul_commutative()
                )
        return NotImplemented
    pass
class IGroupOps(IMonoidOps, ILoopOps__has_inv):
    r'''[[[
    !! Monoid <==> [associative mul][has identity4mul]
    !! Loop__has_inv <==> [has left_div][has right_div][has identity4mul][left_inv_ === right_inv_ === inv_] [has left_inv_][has right_inv_][has inv_]
    Group <==> [associative mul][has identity4mul][has left_div][has right_div][left_inv_ === right_inv_ === inv_] [has left_inv_][has right_inv_][has inv_]

    #]]]'''#'''
    __slots__ = ()
    @classmethod
    @override
    def __instancehook__(cls, ops, /):
        # ABCMeta::__instancehook__
        if cls is __class__:
            return (isinstance(ops, IMonoidOps)
                and isinstance(ops, ILoopOps__has_inv)
                )
        return NotImplemented
    pass
class IAbelianGroupOps(IGroupOps, ICommutativeMonoidOps, ICommutativeLoopOps, ICommutativeQuasigroupOps):
    'AbelianGroup =[def]= CommutativeGroup'
    __slots__ = ()
    @classmethod
    @override
    def __instancehook__(cls, ops, /):
        # ABCMeta::__instancehook__
        if cls is __class__:
            return (isinstance(ops, IGroupOps)
                and ops.is_mul_commutative()
                )
        return NotImplemented
    pass
ICommutativeGroupOps = IAbelianGroupOps






__all__


from seed.math.ops.algebra.IGroupOps import IMagmaOps, IGroupoidOps, ISemigroupOps, IAssociativeMagmaOps, ICommutativeMagmaOps, IIdempotentMagmaOps, ISemilatticeOps, IQuasigroupOps, ICommutativeQuasigroupOps, IMagmaOps__has_identity4mul, ILoopOps, ILoopOps__has_inv, ICommutativeLoopOps, IMonoidOps, ICommutativeMonoidOps, IGroupOps, IAbelianGroupOps, ICommutativeGroupOps

from seed.math.ops.algebra.IGroupOps import *
