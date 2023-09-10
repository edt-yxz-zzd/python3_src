#__all__:goto
r'''[[[
e ../../python3_src/seed/math/ops/algebra/PolynomialRingOps.py


seed.math.ops.algebra.PolynomialRingOps
py -m nn_ns.app.debug_cmd   seed.math.ops.algebra.PolynomialRingOps -x
py -m nn_ns.app.doctest_cmd seed.math.ops.algebra.PolynomialRingOps:__doc__ -ff -v
py_adhoc_call   seed.math.ops.algebra.PolynomialRingOps   @f


>>> from seed.math.ops.algebra.PolynomialRingOps import PolynomialRingOps
>>> from seed.math.ops.algebra.IRingOps import PrimeFieldOps, the_rational_field_ops
>>> ops = PolynomialRingOps(PrimeFieldOps(2))
>>> ops
PolynomialRingOps(PrimeFieldOps(2))
>>> ops.is_mul_commutative()
True
>>> ops.mk5int(5)
((0, 1),)
>>> ops.mk5int(-6)
()
>>> ops.mk5int(0)
()
>>> ops.get_zero()
()
>>> ops.get_one()
((0, 1),)
>>> ops.get_neg_one()
((0, 1),)
>>> _2_0 = ops.mk5strict_sorted_degree_nonzero_coeff_pairs_ex([(0, 1), (2, 1)], reverse=False) # x**2+1
>>> _1_0 = ops.mk5strict_sorted_degree_nonzero_coeff_pairs_ex([(1, 1), (0, 1)], reverse=True) # x+1
>>> _2_0
((0, 1), (2, 1))
>>> _1_0
((0, 1), (1, 1))
>>> _2_1 = ops.add(_2_0, _1_0) # x**2+x
>>> _2_1
((1, 1), (2, 1))
>>> ops.add(_1_0, _1_0)
()
>>> ops.sub(_2_0, _1_0)
((1, 1), (2, 1))
>>> ops.sub(_1_0, _1_0)
()
>>> ops.mul(_2_0, _1_0)
((0, 1), (1, 1), (2, 1), (3, 1))
>>> ops.try_truediv(_2_0, _1_0)
((0, 1), (1, 1))

>>> ops.try_divmod(_2_0, _1_0)
(((0, 1), (1, 1)), ())
>>> ops.try_divmod(_2_0, _2_0)
(((0, 1),), ())
>>> ops.try_divmod(_2_0, _2_1)
(((0, 1),), ((0, 1), (1, 1)))
>>> 
>>> 
>>> 
>>> 

#]]]'''
__all__ = r'''
PolynomialRingOps
'''.split()#'''
__all__

from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.math.ops.algebra.IRingOps import IPolynomialRingOps, IRingOps#, is_divisor_of__6IPolynomialRingOps___coeff_ring_is_field_ as _is_divisor_of_
from seed.tiny import mk_tuple
from seed.helper.repr_input import repr_helper
from seed.tiny import check_type_is

class PolynomialRingOps(IPolynomialRingOps):
    ___no_slots_ok___ = True
    def __init__(ops, ring_ops4coeff:IRingOps, /):
        #if not isinstance(ring_ops4coeff, IRingOps):raise TypeError
        ops._ops = ring_ops4coeff
    def __repr__(ops, /):
        ring_ops4coeff = ops.get_ring_ops4coeff()
        return repr_helper(ops, ring_ops4coeff)

    @override
    def get_ring_ops4coeff(ops, /):
        'ops<z> -> ring_ops4coeff/IRingOps<coeff>'
        return object.__getattribute__(ops, '_ops')
    @override
    def mk5strict_sorted_degree_nonzero_coeff_pairs_ex(ops, iter_strict_sorted_degree_nonzero_coeff_pairs, /, *, reverse:bool):
        'ops<z> -> Iter (degree/uint, coeff/{=!=0}) -> z # [degree strictly decreased] if reverse else [degree strictly increased]'
        ps = iter_strict_sorted_degree_nonzero_coeff_pairs
        if type(ps) is tuple and (len(ps) <= 1 or not reverse):
            it = ps
        elif reverse:
            try:
                it = reversed(ps)
            except TypeError:
                it = reversed([*ps])
            it
        else:
            it = ps
        it
        ps = mk_tuple(it)
        check_type_is(tuple, ps)
        poly = ps
        return poly
    @override
    def get_num_nonzero_coeffs_(ops, poly, /):
        'ops<z> -> z -> num_nonzero_coeffs/uint'
        ps = poly
        return len(ps)
    @override
    def iter_strict_sorted_degree_nonzero_coeff_pairs_ex_(ops, poly, /, *, reverse:bool):
        'ops<z> -> z -> Iter (degree/uint, coeff/{=!=0}) # [degree strictly decreased] if reverse else [degree strictly increased]'
        ps = poly
        f = reversed if reverse else iter
        return f(ps)
    @override
    def is_left_divisor_of_(ops, n, d, /):
        'ops<z> -> z -> z -> bool #[[is_left_divisor_of_(ring;n;d)] <-> [is_right_multiple_of_(d;n)] <-> [?[q :<- ring] -> [d*q == n]]] # not use try_left_div_ex, since not require output unique'
        return _is_right_divisor_of_ex_(ops, n, d, reverse=True)
    @override
    def is_right_divisor_of_(ops, n, d, /):
        'ops<z> -> z -> z -> bool #[[is_right_divisor_of_(ring;n;d)] <-> [is_left_multiple_of_(d;n)] <-> [?[q :<- ring] -> [q*d == n]]] # not use try_right_inv_ex_, since not require output unique'
        return _is_right_divisor_of_ex_(ops, n, d, reverse=False)
assert not PolynomialRingOps.__abstractmethods__, ','.join(sorted(PolynomialRingOps.__abstractmethods__))
def _is_right_divisor_of_ex_(ops, n, d, /, reverse):
    'poly, partial impl'
    #is_divisor_of__6IPolynomialRingOps___coeff_ring_is_field_
    if ops.eq_zero_(n):
        return True
    if ops.eq_zero_(d):
        return False

    ring_ops4coeff = ops.get_ring_ops4coeff()
    if not (ops.is_polynomial_monic_(d) or ring_ops4coeff.is_field()): raise NotImplementedError
    qR, r = ops.try_right_divmod_ex(n, d, reverse=reverse)
    return ops.eq_zero_(r)
#end-class PolynomialRingOps(IPolynomialRingOps):



if __name__ == "__main__":
    pass
__all__


from seed.math.ops.algebra.PolynomialRingOps import PolynomialRingOps
from seed.math.ops.algebra.PolynomialRingOps import *
