r'''[[[
e ../../python3_src/seed/math/IRingOps.py
used in:
    seed.math.matrix.solve_matrix
    nn_ns.math_nn.DFT.NTT

[[
cd ~/my_git_py
find -name '*Ring*'
./nn_ns/math_nn/algebra/IRing.py
./nn_ns/math_nn/ops/IRingOps.py


view ../../python3_src/nn_ns/math_nn/algebra/IRing.py
view ../../python3_src/nn_ns/math_nn/ops/IRingOps.py
view ../../python3_src/seed/math/matrix/solve_matrix.py
view ../../python3_src/seed/math/IRingOps.py
]]

py -m seed.math.IRingOps
py -m nn_ns.app.debug_cmd   seed.math.IRingOps

vs:
    ring_ops__integer: domain not field, no div
    ring_ex_ops__int: semi-support div for domain-unit

from seed.math.IRingOps import ring_ops__integer, ring_ex_ops__int, ring_ex_ops__Fraction, ring_ex_ops__BinaryField

from seed.math.IRingOps import (
    NonInvertibleError
    ,IRingOps
        ,IRingExOps
            ,BinaryFieldRingExOps
                ,ring_ex_ops__BinaryField
        ,IRingOpsOverRealNumber
            ,IRingExOpsOverRealNumber
        ,IPyRingOps
            ,IPyRingExOps
            ,IPyRingOpsOverRealNumber
                ,IntegerRingOps
                    ,ring_ops__integer
                ,IPyRingExOpsOverRealNumber
                    ,IntRingExOps
                        ,ring_ex_ops__int
                    ,FractionRingExOps
                        ,ring_ex_ops__Fraction
    )



#]]]'''
__all__ = '''
    NonInvertibleError

    IRingOps
        IRingExOps
            BinaryFieldRingExOps
                ring_ex_ops__BinaryField
        IRingOpsOverRealNumber
            IRingExOpsOverRealNumber
        IPyRingOps
            IPyRingExOps
            IPyRingOpsOverRealNumber
                IntegerRingOps
                    ring_ops__integer
                IPyRingExOpsOverRealNumber
                    IntRingExOps
                        ring_ex_ops__int
                    FractionRingExOps
                        ring_ex_ops__Fraction


    '''.split()

#################################
#HHHHH
___begin_mark_of_excluded_global_names__0___ = ...
from fractions import Fraction
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.tiny import print_err
from seed.tiny import check_callable, check_uint, check_tmay, check_type_is

___end_mark_of_excluded_global_names__0___ = ...


#HHHHH


class NonInvertibleError(ZeroDivisionError):pass
    #invertible

#class IAlgebraOps(ABC):
class IRingOps(ABC):
    __slots__ = ()

    @abstractmethod
    def _mk_ring_element5int_(ops, i, /):
        'int%characteristic -> Element'
    @abstractmethod
    def _get_characteristic_(ops, /):
        '-> uint # like field characteristic==0'



    #@abstractmethod
    def _get_one_(ops, /):
        '-> element'
        return ops.mk_ring_element5int(1)
    @abstractmethod
    def _add_(ops, x, y, /):
        'element -> element -> element #x+y'
    @abstractmethod
    def _mul_(ops, x, y, /):
        'element -> element -> element #x*y'

    @abstractmethod
    def _neg_(ops, y, /):
        'element -> element #-y'
    @abstractmethod
    def _eq_(ops, x, y, /):
        'element -> element -> bool #x==y'





    #@abstractmethod
    def _sketchy_check_element_(ops, x, /):
        'element -> None|raise TypeError'
    #@abstractmethod
    def _get_zero_(ops, /):
        '-> element'
        return ops.mk_ring_element5int(0)
        one = ops.get_one()
        zero = ops.sub(one, one)
        return zero
    #@abstractmethod
    def _get_neg_one_(ops, /):
        '-> element'
        return ops.mk_ring_element5int(-1)
        one = ops.get_one()
        neg_one = ops.neg(one)
        return neg_one
    #@abstractmethod
    def _sub_(ops, x, y, /):
        'element -> element -> element #x-y'
        neg_y = ops.neg(y)
        return ops.add(x, neg_y)
    #@abstractmethod
    def _is_zero_(ops, x, /):
        'element -> bool #x==0'
        zero = ops.get_zero()
        return ops.eq(x, zero)
    #@abstractmethod
    def _is_one_(ops, x, /):
        'element -> bool #x==1'
        one = ops.get_one()
        return ops.eq(x, one)
    #@abstractmethod
    def _is_neg_one_(ops, x, /):
        'element -> bool #x==-1'
        neg_one = ops.get_neg_one()
        return ops.eq(x, neg_one)


    def mk_ring_element5int(ops, i, /):
        'int -> Element'
        characteristic = ops.get_characteristic()
        if characteristic:
            i %= characteristic
        x = ops._mk_ring_element5int_(i)
        ops.sketchy_check_element(x)
        return x
    def get_characteristic(ops, /):
        '-> uint # like field characteristic==0'
        characteristic = ops._get_characteristic_()
        check_uint(characteristic)
        return characteristic




    def sketchy_check_element(ops, x, /):
        'element -> None|raise TypeError'
        return ops._sketchy_check_element_(x)

    def _4bool_op(ops, bool_op, /, *xs):
        check = ops._sketchy_check_element_
        for x in xs: check(x)
        b = bool_op(*xs)
        check_type_is(bool, b)
        return b
    def _4op(ops, op, /, *xs):
        check = ops._sketchy_check_element_
        for x in xs: check(x)
        z = op(*xs)
        check(z)
        return z

    def get_zero(ops, /):
        '-> element'
        return ops._4op(ops._get_zero_)
    def get_one(ops, /):
        '-> element'
        return ops._4op(ops._get_one_)
    def get_neg_one(ops, /):
        '-> element'
        return ops._4op(ops._get_neg_one_)


    def add(ops, x, y, /):
        'element -> element -> element #x+y'
        return ops._4op(ops._add_, x, y)
    def sub(ops, x, y, /):
        'element -> element -> element #x-y'
        return ops._4op(ops._sub_, x, y)
    def mul(ops, x, y, /):
        'element -> element -> element #x*y'
        return ops._4op(ops._mul_, x, y)
    def neg(ops, y, /):
        'element -> element #-y'
        return ops._4op(ops._neg_, y)



    def is_zero(ops, x, /):
        'element -> bool #x==0'
        return ops._4bool_op(ops._is_zero_, x)
    def is_one(ops, x, /):
        'element -> bool #x==1'
        return ops._4bool_op(ops._is_one_, x)
    def is_neg_one(ops, x, /):
        'element -> bool #x==-1'
        return ops._4bool_op(ops._is_neg_one_, x)
    def eq(ops, x, y, /):
        'element -> element -> bool #x==y'
        return ops._4bool_op(ops._eq_, x, y)

#class IRingOps(ABC):
class IRingExOps(IRingOps):
    #IRingExOps._inv__tmay_
    __slots__ = ()
    #bug:def invL__tmay_arbitrary(ops, y, /):
    @abstractmethod
    def _inv__tmay_(ops, y, /):
        'element -> tmay element #tmay (1/y) __truediv__'


    #@abstractmethod
    def _div_(ops, x, y, /):
        'element -> element -> element|raise  ZeroDivisionError #x/y __truediv__ raise if not is_invertable'
        tmay_q = ops.div__tmay(x, y)
        if not tmay_q:
            raise NonInvertibleError(y)
        [q] = tmay_q
        return q
    #@abstractmethod
    def _div__tmay_(ops, x, y, /):
        'element -> element -> tmay element #tmay (x/y)'
        tmay_inv_y = ops.inv__tmay(y)
        if tmay_inv_y:
            [inv_y] = tmay_inv_y
            q = ops.mul(x, inv_y)
            tmay_q = (q,)
        else:
            tmay_q = ()
        return tmay_q
    #@abstractmethod
    def _inv_(ops, y, /):
        'element -> element|raise  ZeroDivisionError #1/y __truediv__ raise if not is_invertable'
        tmay_inv_y = ops.inv__tmay(y)
        if tmay_inv_y:
            [inv_y] = tmay_inv_y
            return inv_y
        else:
            raise NonInvertibleError(y)
    #@abstractmethod
    def _is_invertable_(ops, y, /):
        'element -> bool'
        tmay_inv_y = ops.inv__tmay(y)
        return bool(tmay_inv_y)







    def _4tmay_op(ops, tmay_op, /, *xs):
        check = ops._sketchy_check_element_
        for x in xs: check(x)
        tmay_z = tmay_op(*xs)
        check_tmay(tmay_z)
        for z in tmay_z:
            check(z)
        return tmay_z
    def div(ops, x, y, /):
        'element -> element -> element|raise  ZeroDivisionError #x/y __truediv__ raise if not is_invertable'
        return ops._4op(ops._div_, x, y)
    def div__tmay(ops, x, y, /):
        'element -> element -> tmay element #tmay (x/y)'
        return ops._4tmay_op(ops._div__tmay_, x, y)
    #bug:def invL__tmay_arbitrary(ops, y, /):
    def inv__tmay(ops, y, /):
        'element -> tmay element #tmay (1/y) __truediv__'
        return ops._4tmay_op(ops._inv__tmay_, y)
    def inv(ops, y, /):
        'element -> element|raise  ZeroDivisionError #1/y __truediv__ raise if not is_invertable'
        return ops._4op(ops._inv_, y)


    def is_invertable(ops, y, /):
        'element -> bool'
        return ops._4bool_op(ops._is_invertable_, y)


#class IRingExOps(IRingOps):
class BinaryFieldRingExOps(IRingExOps):
    __slots__ = ()
    _zero = False
    _one = True
    _neg_one = True
    @override
    def _add_(ops, x, y, /):
        'element -> element -> element #x+y'
        return x ^ y
    @override
    def _mul_(ops, x, y, /):
        'element -> element -> element #x*y'
        return x and y
    @override
    def _neg_(ops, y, /):
        'element -> element #-y'
        return y
    @override
    def _eq_(ops, x, y, /):
        'element -> element -> bool #x==y'
        return x == y
    @override
    def _get_characteristic_(ops, /):
        '-> uint # like field characteristic==0'
        return 2
    @override
    def _inv__tmay_(ops, y, /):
        'element -> tmay element #tmay (1/y) __truediv__'
        if y:
            inv_y = y
            tmay_inv_y = (inv_y,)
        else:
            tmay_inv_y = ()
        return tmay_inv_y
    @override
    def _mk_ring_element5int_(ops, i, /):
        'int%characteristic -> Element'
        return bool(i&1)
ring_ex_ops__BinaryField = BinaryFieldRingExOps()







class IRingOpsOverRealNumber(IRingOps):
    __slots__ = ()
    @abstractmethod
    def _lt_(ops, x, y, /):
        'element -> element -> bool #x<y'
    #@abstractmethod
    def _le_(ops, x, y, /):
        'element -> element -> bool #x<y'
        return not ops.lt(y, x)
    #@abstractmethod
    def _gt_(ops, x, y, /):
        'element -> element -> bool #x<y'
        return ops._lt_(y, x)
    #@abstractmethod
    def _ge_(ops, x, y, /):
        'element -> element -> bool #x<y'
        return ops._le_(y, x)




    def lt(ops, x, y, /):
        'element -> element -> bool #x<y'
        return ops._4bool_op(ops._lt_, x, y)
    def le(ops, x, y, /):
        'element -> element -> bool #x<y'
        return ops._4bool_op(ops._le_, x, y)
    def gt(ops, x, y, /):
        'element -> element -> bool #x<y'
        return ops._4bool_op(ops._gt_, x, y)
    def ge(ops, x, y, /):
        'element -> element -> bool #x<y'
        return ops._4bool_op(ops._ge_, x, y)
#class IRingExOpsOverRealNumber(IRingExOps):
class IRingExOpsOverRealNumber(IRingOpsOverRealNumber, IRingExOps):
    __slots__ = ()



class IPyRingOps(IRingOps):
    __slots__ = ()
    @override
    def _add_(ops, x, y, /):
        'element -> element -> element #x+y'
        return x + y
    @override
    def _mul_(ops, x, y, /):
        'element -> element -> element #x*y'
        return x * y
    @override
    def _neg_(ops, y, /):
        'element -> element #-y'
        return -y
    @override
    def _eq_(ops, x, y, /):
        'element -> element -> bool #x==y'
        return x == y
#class IPyRingOps(IRingExOps):

class IPyRingExOps(IPyRingOps, IRingExOps):
    __slots__ = ()
    @override
    def _inv__tmay_(ops, y, /):
        'element -> tmay element #tmay (1/y) __truediv__'
        if ops.is_zero(y):
            tmay_inv_y = ()
        else:
            inv_y = ops.get_one()/y
            tmay_inv_y = (inv_y,)
        return tmay_inv_y

#class IPyRingExOps(IPyRingOps, IRingExOps):

class IPyRingOpsOverRealNumber(IPyRingOps, IRingOpsOverRealNumber):
    __slots__ = ()
    @override
    def _lt_(ops, x, y, /):
        'element -> element -> bool #x<y'
        return x < y
class IPyRingExOpsOverRealNumber(IPyRingOpsOverRealNumber, IPyRingExOps, IRingExOpsOverRealNumber):
    __slots__ = ()



class IntegerRingOps(IPyRingOpsOverRealNumber):
    #not <: IRingExOps._inv__tmay_
    __slots__ = ()

    @override
    def _mk_ring_element5int_(ops, i, /):
        'int%characteristic -> Element'
        return i
    @override
    def _get_characteristic_(ops, /):
        '-> uint # like field characteristic==0'
        return 0

    if 0:
        @override
        def _get_one_(ops, /):
            '-> element'
            return 1

    @override
    def _sketchy_check_element_(ops, x, /):
        'element -> None|raise TypeError'
        check_type_is(int, x)
ring_ops__integer = IntegerRingOps()

class IntRingExOps(IPyRingExOpsOverRealNumber):
    # <: IRingExOps._inv__tmay_
    __slots__ = ()

    @override
    def _mk_ring_element5int_(ops, i, /):
        'int%characteristic -> Element'
        return i
    @override
    def _get_characteristic_(ops, /):
        '-> uint # like field characteristic==0'
        return 0

    @override
    def _sketchy_check_element_(ops, x, /):
        'element -> None|raise TypeError'
        try:
            check_type_is(int, x)
        except:
            print_err(type(x))
            print_err(f'{x!r}')
            raise

    @override
    def _inv__tmay_(ops, y, /):
        'element -> tmay element #tmay (1/y) __truediv__'
        if abs(y) == 1:
            inv_y = y
            tmay_inv_y = (inv_y,)
        else:
            tmay_inv_y = ()
        return tmay_inv_y
ring_ex_ops__int = IntRingExOps()

#vs:
#   ring_ops__integer: domain not field, no div
#   ring_ex_ops__int: semi-support div for domain-unit


class FractionRingExOps(IPyRingExOpsOverRealNumber):
    __slots__ = ()
    _zero = Fraction(0)
    _one = Fraction(1)
    _neg_one = Fraction(-1)

    @override
    def _mk_ring_element5int_(ops, i, /):
        'int%characteristic -> Element'
        return Fraction(i)
    @override
    def _get_characteristic_(ops, /):
        '-> uint # like field characteristic==0'
        return 0

    if 0:
        @override
        def _get_one_(ops, /):
            '-> element'
            return ops._one



    @override
    def _sketchy_check_element_(ops, x, /):
        'element -> None|raise TypeError'
        try:
            check_type_is(Fraction, x)
        except:
            print_err(type(x))
            print_err(f'{x!r}')
            raise
ring_ex_ops__Fraction = FractionRingExOps()








from seed.math.IRingOps import ring_ops__integer, ring_ex_ops__int, ring_ex_ops__Fraction, ring_ex_ops__BinaryField
from seed.math.IRingOps import *
