#__all__:goto
r'''[[[
e ../../python3_src/seed/math/polynomial/simple_polynomial.py
    简单的多元多项式
see:
    view ../../python3_src/seed/math/polynomial/simple_polynomial.py
    view ../../python3_src/seed/math/IRingOps.py
    view ../../python3_src/seed/math/ops/algebra/IRingOps.py
    view ../../python3_src/seed/math/ops/algebra/PolynomialRingOps.py
        单元多项式

see:
    view ../../python3_src/seed/abc/IComparable.py
    view ../../python3_src/seed/abc/ITotalOrdering.py
    view ../../python3_src/seed/abc/Ops/ITotalOrderingOps.py

seed.math.polynomial.simple_polynomial
py -m nn_ns.app.debug_cmd   seed.math.polynomial.simple_polynomial -x
py -m nn_ns.app.doctest_cmd seed.math.polynomial.simple_polynomial:__doc__ -ht
py_adhoc_call   seed.math.polynomial.simple_polynomial   @f
from seed.math.polynomial.simple_polynomial import *


>>> from fractions import Fraction
>>> T, vs, polys = mk_type_Polynomial8PyExpr__str('n u m w I J', with_vars=True, with_polys=True)
>>> vs is T.get_vars()
True
>>> polys == T.mk_polynomials5all_vars()
True
>>> T.mk5int(999)
999
>>> T.mk5coeff(Fraction(999, 777))
9/7
>>> T.mk5name4var('n')
n

>>> T.mk5int(Fraction(999, 777))
Traceback (most recent call last):
    ...
TypeError: <class 'fractions.Fraction'>
>>> T.mk5coeff(999)
Traceback (most recent call last):
    ...
TypeError: <class 'int'>
>>> T.mk5name4var('x')
Traceback (most recent call last):
    ...
KeyError: 'x'

>>> n = T.mk5name4var('n')
>>> u = T.mk5name4var('u')
>>> m = T.mk5name4var('m')
>>> w = T.mk5name4var('w')
>>> I = T.mk5name4var('I')
>>> J = T.mk5name4var('J')
>>> (n,u,m,w,I,J) == T.mk_polynomials5all_vars()
True
>>> _1 = T.mk5int(1)
>>> _333 = T.mk5int(333)
>>> _666 = T.mk5int(666)
>>> _999 = T.mk5int(999)
>>> _666*n + _999*u + m*_333 + m**333 + I*J*J*I**2*_666 + m
666*n+999*u+334*m+m**333+666*I**3*J**2
>>> (I + J) + (u + n)
n+u+I+J
>>> (I + J) * (u + n)
n*I+n*J+u*I+u*J
>>> (I + J) * (I + J)
2*I*J+I**2+J**2
>>> (I + J) ** 2
2*I*J+I**2+J**2
>>> (I + J) ** 3
3*I*J**2+3*I**2*J+I**3+J**3
>>> (I + J) ** 4
4*I*J**3+6*I**2*J**2+4*I**3*J+I**4+J**4
>>> (I + J) ** 5
5*I*J**4+10*I**2*J**3+10*I**3*J**2+5*I**4*J+I**5+J**5
>>> (I + J).__pow__(5, _naive=True)
5*I*J**4+10*I**2*J**3+10*I**3*J**2+5*I**4*J+I**5+J**5

>>> (__:=(I + J)).substitute__name4var(dict(n=J+n, u=I+u)) is __ #echo if not changed
True
>>> (I + J).substitute__name4var(dict(I=J+n, J=I+u)) #batch/parallel not serial
n+u+I+J
>>> (I*J + J**2).substitute__name4var(dict(I=J+n+_1, J=I+u+_1))
2+n+n*u+n*I+3*u+2*u*I+u*J+u**2+3*I+I*J+I**2+J
>>> ((J+n+_1)*(I+u+_1) + (I+u+_1)**2)
2+n+n*u+n*I+3*u+2*u*I+u*J+u**2+3*I+I*J+I**2+J
>>> 2+n+n*u+n*I+3*u+2*u*I+u*J+u**2+3*I+I*J+I**2+J
2+n+n*u+n*I+3*u+2*u*I+u*J+u**2+3*I+I*J+I**2+J



__neg__
__pos__
>>> -n
-n
>>> +n
n
>>> n
n

__rsub__
2-n
>>> 2-n ##!!!
2+-n
>>> n-2
-2+n

__radd__
>>> 2+n
2+n
>>> n+2
2+n

__rmul__
>>> 2*n
2*n
>>> n*2
2*n

>>> 0*n
0
>>> n-n
0
>>> n + -n
0

>>> int(n+2)
Traceback (most recent call last):
    ...
IndexError: Polynomial(((Monomial(()), Fraction(2, 1)), (Monomial((([<n@0>], 1),)), Fraction(1, 1))))
>>> int(n*2)
Traceback (most recent call last):
    ...
IndexError: Polynomial(((Monomial((([<n@0>], 1),)), Fraction(2, 1)),))
>>> int(T.mk5coeff(Fraction(999,777)))
Traceback (most recent call last):
    ...
IndexError: 9/7
>>> int(_999)
999








#]]]'''
__all__ = r'''
IMonomialOps
    mk_monomial5nonstd_var_exp_pairs
    IMonomialOps__using_Monomial
        MonomialOps
IPolynomialOps
    mk_polynomial5nonstd_monomial_coeff_pairs
    IPolynomialOps__using_Polynomial
        PolynomialOps

check_strict_sorted_fst6pairs
    check_pairs
    check_strict_sorted

Monomial
Polynomial


MonomialOps
PolynomialOps
Var

ITotalOrderingOps
    TotalOrderingOps4py_ord
    TotalOrderingOps4Var
    TotalOrderingOps4Monomial
    TotalOrderingOps4Polynomial

IDisplayerOps
    DisplayerOps4py_repr
    DisplayerOps4py_str
    DisplayerOps4Var
    DisplayerOps4Monomial
    DisplayerOps4Polynomial


ord_ops4py_ord
ord_ops4Var
ord_ops4Monomial__Var__std
ops4Monomial__Var__int
ring_ops4Polynomial__Var__int__Fraction
displayer_ops4py_repr
displayer_ops4py_str
displayer_ops4Var
displayer_ops4Monomial__Var__int
displayer_ops4Polynomial__Var__int__Fraction




mk_ordered_vars_ex5str
    mk_ordered_vars_ex
IPolynomial8PyExpr
    abstract_class_property
    mk_IPolynomial8PyExpr5underlying_polynomial
    IPolynomial8PyExpr__init
        mk_type_Polynomial8PyExpr__basic
        mk_type_Polynomial8PyExpr__str
        mk_type_Polynomial8PyExpr__params

'''.split()#'''
__all__
from itertools import pairwise
from functools import reduce# total_ordering
# functools.reduce(function, iterable[, initializer])

from seed.iters.group_by import group_by
from seed.math.IRingOps import IRingOps
from seed.math.IRingOps import ring_ops__integer, ring_ex_ops__int, ring_ex_ops__Fraction, ring_ex_ops__BinaryField

from seed.abc.ITotalOrdering import ITotalOrdering5le
from seed.abc.Ops.ITotalOrderingOps import ITotalOrderingOps
from seed.abc.Ops.ITotalOrderingOps import ITotalOrderingOps__via_cmp
from seed.iters.cmp4iterable import eq4iterable, cmp4iterable
from seed.seq_tools.sorted_via_lt_ import sorted_via_le_

from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.helper.repr_input import repr_helper

from seed.tiny import fst, snd, null_tuple, check_type_is, check_pair, check_type_le
from seed.tiny import MapView, mk_tuple
#from seed.tiny import print_err
from seed.math.pow__via_binomial_formula import iter_parts5pow__via_binomial_formula__
from seed.iters.group_by__nonlocal import regroup_if #group_by__nonlocal, sized_regroup__

from seed.abc.Ops.IDisplayerOps import IDisplayerOps
from seed.abc.Ops__concrete.DisplayerOps import DisplayerOps4py_repr, DisplayerOps4py_str
from seed.abc.Ops__concrete.DisplayerOps import displayer_ops4py_repr, displayer_ops4py_str

from seed.iters.merge_two_sorted_iterables import merge_two_sorted_iterables
def __():
  def merge_two_sorted_iterables(lefts, rights
        , *, left_key=None, right_key=None, before=None
        , Left=None, Right=None):...






class IMonomialOps(ABC):
    '??semi_ring??-ops4monomial'
    __slots__ = ()
    ######################
    @abstractmethod
    def sketchy_check4var(ops, var, /):
        '-> var -> None'
    @abstractmethod
    def sketchy_check4monomial(ops, monomial, /):
        '-> monomial -> None'
    ######################
    if 0:
        @abstractmethod
        def get_ord_ops4monomial(ops, /):
            '-> ord_ops4monomial/ITotalOrderingOps<monomial>'
        @abstractmethod
        def get_ord_ops4exp(ops, /):
            '-> ord_ops4exp/ITotalOrderingOps<exp>'
    ######################
    @abstractmethod
    def get_ring_ops4exp(ops, /):
        '-> ring_ops4exp/IRingOps<exp>'
    if 1:
        @abstractmethod
        def get_ord_ops4var(ops, /):
            '-> ord_ops4var/ITotalOrderingOps<var>'
    ######################
    @abstractmethod
    def mk5std_var_exp_pairs(ops, iter_var_exp_pairs, /):
        '-> iter_var_exp_pairs/Iter (var,exp) -> monomial'
    @abstractmethod
    def mk5nonstd_var_exp_pairs(ops, iter_var_exp_pairs, /):
        '-> iter_var_exp_pairs/Iter (var,exp) -> monomial'

    @abstractmethod
    def mk_one(ops, /):
        '-> Monomial:1*II[()]'
    @abstractmethod
    def is_one(ops, monomial, /):
        '-> monomial -> bool'
    @abstractmethod
    def pow(ops, monomial, exp, /):
        '-> monomial -> exp -> monomial'
    @abstractmethod
    def mul(ops, lhs_monomial, rhs_monomial, /):
        '-> monomial -> monomial -> monomial'
    ######################
    ##news:
    ######################
    @abstractmethod
    def substitute_(ops, ring_ops4polynomial, monomial, var2polynomial, /):
        '-> IPolynomialOps<polynomial> -> monomial -> {var:polynomial} -> polynomial'
    def mk5var_exp(ops, var, exp, /):
        '-> var -> exp -> monomial'
        monomial = ops.mk5nonstd_var_exp_pairs([(var, exp)])
        return monomial
    def mk5var(ops, var, /):
        '-> var -> monomial'
        ring_ops4exp = ops.get_ring_ops4exp()
        one8exp = ring_ops4exp.get_one()
        monomial = ops.mk5var_exp(var, one8exp)
        return monomial

IMonomialOps.mk5nonstd_var_exp_pairs
def mk_monomial5nonstd_var_exp_pairs(ops, iter_var_exp_pairs, /):
    '-> iter_var_exp_pairs/Iter (var,exp) -> monomial'
    ord_ops4var = ops.get_ord_ops4var()
    ls = sorted_via_le_(iter_var_exp_pairs, key=fst, __le__=ord_ops4var.le)
    ring_ops4exp = ops.get_ring_ops4exp()
    add4exp = ring_ops4exp.add
    is_zero4exp = ring_ops4exp.is_zero
    eq4var = ord_ops4var.eq
    it = _solid4sorted(eq4var, add4exp, is_zero4exp, ls)
    return ops.mk5std_var_exp_pairs(tuple(it))
#end-class IMonomialOps(ABC):
class IPolynomialOps(IRingOps):
    'ring_ops4polynomial'
    __slots__ = ()
    ######################
    if 0:
        @abstractmethod
        def get_ord_ops4polynomial(ops, /):
            '-> ord_ops4polynomial/ITotalOrderingOps<polynomial>'
    ######################
    @abstractmethod
    def get_ops4monomial(ops, /):
        '-> ops4monomial/IMonomialOps<monomial>'
    @abstractmethod
    def get_ring_ops4coeff(ops, /):
        '-> ring_ops4coeff/IRingOps<coeff>'
    if 1:
        @abstractmethod
        def get_ord_ops4monomial(ops, /):
            '-> ord_ops4monomial/ITotalOrderingOps<monomial>'
    ######################
    @abstractmethod
    def mk5std_monomial_coeff_pairs(ops, monomial_coeff_pairs, /):
        '-> monomial_coeff_pairs/tuple<(monomial,coeff)> -> polynomial'
    @abstractmethod
    def mk5nonstd_monomial_coeff_pairs(ops, iter_monomial_coeff_pairs, /):
        '-> iter_monomial_coeff_pairs/Iter (monomial,coeff) -> polynomial'
    @abstractmethod
    def mul_coeff(ops, polynomial, coeff, /):
        '-> polynomial -> coeff -> polynomial'
    ######################
    ######################
    ##news:
    ######################
    @abstractmethod
    def substitute(ops, polynomial, var2polynomial, /):
        '-> polynomial -> {var:polynomial} -> polynomial'
    def mk5monomial_coeff(ops, monomial, coeff, /):
        '-> monomial -> coeff -> polynomial'
        polynomial = ops.mk5nonstd_monomial_coeff_pairs([(monomial, coeff)])
        return polynomial
    def mk5monomial(ops, monomial, /):
        '-> monomial -> polynomial'
        ring_ops4coeff = ops.get_ring_ops4coeff()
        one8coeff = ring_ops4coeff.get_one()
        polynomial = ops.mk5monomial_coeff(monomial, one8coeff)
        return polynomial
    def mk5coeff(ops, coeff, /):
        '-> coeff -> polynomial'
        ops4monomial = ops.get_ops4monomial()
        one8monomial = ops4monomial.mk_one()
        polynomial = ops.mk5monomial_coeff(one8monomial, coeff)
        return polynomial
    def mk5var(ops, var, /):
        '-> var -> polynomial'
        ops4monomial = ops.get_ops4monomial()
        monomial = ops4monomial.mk5var(var)
        polynomial = ops.mk5monomial(monomial)
        return polynomial
    ######################
    ##IRingOps:force-redefine
    ######################
    @abstractmethod
    def _pow_uint_(ops, x, exp, /):
        'element{=!= (0|-1|+1)} -> exp/uint{>=2} -> element'
IPolynomialOps.mk5nonstd_monomial_coeff_pairs
def mk_polynomial5nonstd_monomial_coeff_pairs(ops, iter_monomial_coeff_pairs, /):
    '-> iter_monomial_coeff_pairs/Iter (monomial,coeff) -> polynomial'
    ord_ops4monomial = ops.get_ord_ops4monomial()
    ls = sorted_via_le_(iter_monomial_coeff_pairs, key=fst, __le__=ord_ops4monomial.le)
    ring_ops4coeff = ops.get_ring_ops4coeff()
    add4coeff = ring_ops4coeff.add
    is_zero4coeff = ring_ops4coeff.is_zero
    eq4monomial = ord_ops4monomial.eq
    it = _solid4sorted(eq4monomial, add4coeff, is_zero4coeff, ls)
    return ops.mk5std_monomial_coeff_pairs(tuple(it))
#end-class IPolynomialOps(IRingOps):





def check_pairs(ps, /):
    check_type_is(tuple, ps)
    for p in ps:
        check_pair(p)
def check_strict_sorted_fst6pairs(sketchy_check4fst, sketchy_check4snd, lt4fst, ps, /):
    check_pairs(ps)
    for a, b in ps:
        sketchy_check4fst(a)
        sketchy_check4snd(b)
    check_strict_sorted(lt4fst, map(fst, ps))
def check_strict_sorted(lt, xs, /):
    if not all(lt(x, y) for x, y in pairwise(xs)):raise ValueError

def _merge(eq4fst, le4fst, add4snd, is_zero4snd, psL, psR, /):
    assert len(psL)
    assert len(psR)
    it = merge_two_sorted_iterables(psL, psR, left_key=fst, right_key=fst, before=le4fst)
    return _solid4sorted(eq4fst, add4snd, is_zero4snd, it)
def _solid4sorted(eq4fst, add4snd, is_zero4snd, sorted_ps, /):
    #bug:for k, g in group_by(sorted_ps, key=fst):
    #   miss:eq4fst
    for k, g in group_by(sorted_ps, key=fst, __eq__=eq4fst):
        k = fst(g[0])
        c = reduce(add4snd, map(snd, g)) if len(g) > 1 else snd(*g)
        if not is_zero4snd(c):
            yield (k, c)



#@total_ordering
#def _Sortable:
#    def __hash__(sf, /):
#    def __eq__(sf, ot, /):
#    def __lt__(sf, ot, /):
class Monomial:
    #class Monomial(_Sortable):
    'monomial: (x0**ex0 *x1**ex1)'
    # ???[exp :: int]
    # [ring_ops4exp :: IRingOps<exp>]
    # [ord_ops4exp :: ITotalOrderingOps<exp>]
    ring_ops__integer
    def __repr__(sf, /):
        return repr_helper(sf, sf.var_exp_pairs)
    def __init__(sf, var_exp_pairs, /, *, lt4var, sketchy_check4var, sketchy_check4exp):
        check_strict_sorted_fst6pairs(sketchy_check4var, sketchy_check4exp, lt4var, var_exp_pairs)
        if 0:
            for v, e in var_exp_pairs:
                check_type_is(int, e)
            if not all(map(snd, var_exp_pairs)):raise TypeError
        sf._ps = var_exp_pairs
    @property
    def var_exp_pairs(sf, /):
        return sf._ps
    @classmethod
    def mk_one(cls, /):
        return cls(null_tuple, lt4var=None, sketchy_check4var=None, sketchy_check4exp=None)
    def is_one(sf, /):
        return not sf._ps

class Polynomial:
    #class Polynomial(_Sortable):
    'polynomial: c0*(x0**e0x0 *x1**e0x1) +c1*(x0**e1x0 *x1**e1x1)'
    # [ring_ops4coeff :: IRingOps<coeff>]
    # [ord_ops4coeff :: ITotalOrderingOps<coeff>]
    ring_ex_ops__Fraction
    def __repr__(sf, /):
        return repr_helper(sf, sf.monomial_coeff_pairs)
    def __init__(sf, monomial_coeff_pairs, /, *, lt4monomial, sketchy_check4monomial, sketchy_check4coeff):
        #if 0b0001:print_err(monomial_coeff_pairs)
        #if 0b0001:print_err(lt4monomial)
        check_strict_sorted_fst6pairs(sketchy_check4monomial, sketchy_check4coeff, lt4monomial, monomial_coeff_pairs)
        if 0:
            for m, c in monomial_coeff_pairs:
                check_type_is(m, Monomial)
            if not all(map(snd, monomial_coeff_pairs)):raise TypeError
        sf._ps = monomial_coeff_pairs
    @property
    def monomial_coeff_pairs(sf, /):
        return sf._ps
    @classmethod
    def mk_zero(cls, /):
        return cls(null_tuple, lt4monomial=None, sketchy_check4monomial=None, sketchy_check4coeff=None)
    def is_zero(sf, /):
        return not sf._ps


class IMonomialOps__using_Monomial(IMonomialOps):
    'ops4monomial<Monomial>'
    __slots__ = ()
    ######################
    @override
    def sketchy_check4monomial(ops, monomial, /):
        '-> monomial -> None'
        check_type_is(Monomial, monomial)
    @override
    def mk5std_var_exp_pairs(ops, var_exp_pairs, /):
        '-> var_exp_pairs/tuple<(var,exp)> -> monomial'
        ord_ops4var = ops.get_ord_ops4var()
        ring_ops4exp = ops.get_ring_ops4exp()
        return Monomial(var_exp_pairs, lt4var=ord_ops4var.lt, sketchy_check4var=ops.sketchy_check4var, sketchy_check4exp=ring_ops4exp.sketchy_check_element)
    @override
    def mk5nonstd_var_exp_pairs(ops, iter_var_exp_pairs, /):
        '-> iter_var_exp_pairs/Iter (var,exp) -> monomial'
        return mk_monomial5nonstd_var_exp_pairs(ops, iter_var_exp_pairs)
    ######################
    @override
    def mk_one(ops, /):
        '-> Monomial:1*II[()]'
        return Monomial.mk_one()
    @override
    def is_one(ops, monomial, /):
        '-> monomial -> bool'
        check_type_is(Monomial, monomial)
        return monomial.is_one()
    @override
    def pow(ops, monomial, exp, /):
        '-> monomial -> exp -> monomial'
        check_type_is(Monomial, monomial)
        if monomial.is_one():
            return monomial
        ring_ops4exp = ops.get_ring_ops4exp()
        if ring_ops4exp.is_zero(exp):
            return Monomial.mk_one()
        ps = monomial.var_exp_pairs
        mul = ring_ops4exp.mul
        return ops.mk5nonstd_var_exp_pairs(((v,mul(e,exp)) for v, e in ps))

    @override
    def mul(ops, lhs_monomial, rhs_monomial, /):
        '-> monomial -> monomial -> monomial'
        check_type_is(Monomial, lhs_monomial)
        check_type_is(Monomial, rhs_monomial)
        if rhs_monomial.is_one():
            return lhs_monomial
        if lhs_monomial.is_one():
            return rhs_monomial

        psL = lhs_monomial.var_exp_pairs
        psR = rhs_monomial.var_exp_pairs
        ring_ops4exp = ops.get_ring_ops4exp()
        add4exp = ring_ops4exp.add
        is_zero4exp = ring_ops4exp.is_zero
        ord_ops4var = ops.get_ord_ops4var()
        le4var = ord_ops4var.le
        eq4var = ord_ops4var.eq
        it = _merge(eq4var, le4var, add4exp, is_zero4exp, psL, psR)
        return ops.mk5std_var_exp_pairs(tuple(it))
    ######################
    ##news:
    ######################
    @override
    def substitute_(ops, ring_ops4polynomial, monomial, var2polynomial, /):
        '-> IPolynomialOps<polynomial> -> monomial -> {var:polynomial} -> polynomial'
        ps = monomial.var_exp_pairs
        ps4stationary, ps4substitute = regroup_if(ps, key=lambda pair: fst(pair) in var2polynomial)
        if not ps4substitute:
            monomial_ = monomial
        else:
            monomial_ = ops.mk5std_var_exp_pairs(tuple(ps4stationary))
        monomial_
        polynomial_ = ring_ops4polynomial.mk5monomial(monomial_)
        pow_uint4poly = ring_ops4polynomial.pow_uint
        mul4poly = ring_ops4polynomial.mul
        for var, exp in ps4substitute:
            _polynomial_ = var2polynomial[var]
            _polynomial_ = pow_uint4poly(_polynomial_, exp)
            polynomial_ = mul4poly(polynomial_, _polynomial_)
        polynomial = polynomial_
        return polynomial
#end-class IMonomialOps__using_Monomial(IMonomialOps):

class IPolynomialOps__using_Polynomial(IPolynomialOps):
    'ring_ops4polynomial<Polynomial>'
    __slots__ = ()
    ######################
    ##news:
    ######################
    def mul_monomial(ops, polynomial, monomial, /):
        '-> polynomial -> monomial -> polynomial'
        ops.sketchy_check_element(polynomial)
        ops4monomial = ops.get_ops4monomial()
        if polynomial.is_zero() or ops4monomial.is_one(monomial):
            return polynomial
        ps = polynomial.monomial_coeff_pairs
        mul = ops4monomial.mul
        return ops.mk5nonstd_monomial_coeff_pairs((mul(m,monomial),c) for m, c in ps)
    def mul_coeff_monomial(ops, polynomial, coeff, monomial, /):
        '-> polynomial -> coeff -> monomial -> polynomial'
        polynomial = ops.mul_coeff(polynomial, coeff)
        polynomial = ops.mul_monomial(polynomial, monomial)
        return polynomial


    ######################
    ##IPolynomialOps:
    ######################
    @override
    def mk5std_monomial_coeff_pairs(ops, monomial_coeff_pairs, /):
        '-> monomial_coeff_pairs/tuple<(monomial,coeff)> -> polynomial'
        ord_ops4monomial = ops.get_ord_ops4monomial()
        ops4monomial = ops.get_ops4monomial()
        ring_ops4coeff = ops.get_ring_ops4coeff()
        return Polynomial(monomial_coeff_pairs, lt4monomial=ord_ops4monomial.lt, sketchy_check4monomial=ops4monomial.sketchy_check4monomial, sketchy_check4coeff=ring_ops4coeff.sketchy_check_element)
    @override
    def mk5nonstd_monomial_coeff_pairs(ops, iter_monomial_coeff_pairs, /):
        '-> iter_monomial_coeff_pairs/Iter (monomial,coeff) -> polynomial'
        return mk_polynomial5nonstd_monomial_coeff_pairs(ops, iter_monomial_coeff_pairs)
    @override
    def mul_coeff(ops, polynomial, coeff, /):
        '-> polynomial -> coeff -> polynomial'
        ops.sketchy_check_element(polynomial)
        ring_ops4coeff = ops.get_ring_ops4coeff()
        if polynomial.is_zero() or ring_ops4coeff.is_one(coeff):
            return polynomial
        if ring_ops4coeff.is_zero(coeff):
            return Polynomial.mk_zero()
        ps = polynomial.monomial_coeff_pairs
        mul = ring_ops4coeff.mul
        return ops.mk5nonstd_monomial_coeff_pairs((m,mul(c,coeff)) for m, c in ps)
    ######################
    ##news:
    ######################
    @override
    def substitute(ops, polynomial, var2polynomial, /):
        '-> polynomial -> {var:polynomial} -> polynomial'
        ps = polynomial.monomial_coeff_pairs
        ops4monomial = ops.get_ops4monomial()
        polys = [ops4monomial.substitute_(ops, monomial, var2polynomial) for monomial, _ in ps]
        def key(poly__mc, /):
            (poly4new, (monomial, coeff)) = poly__mc
            return not ops.eq(poly4new, ops.mk5monomial(monomial))
        mps4stationary, mps4substitute = regroup_if(zip(polys, ps), key=key)
        ps4stationary = tuple(map(snd, mps4stationary))
        if not mps4substitute:
            polynomial_ = polynomial
        else:
            polynomial_ = ops.mk5std_monomial_coeff_pairs(ps4stationary)
        polynomial_
        mul_coeff = ops.mul_coeff
        it4substitute = (mul_coeff(poly4new, coeff) for (poly4new, (monomial, coeff)) in mps4substitute)
        add = ops.add
        for _polynomial_ in it4substitute:
            polynomial_ = add(polynomial_, _polynomial_)
        polynomial = polynomial_
        return polynomial


    ######################
    ##IRingOps:
    ######################
    @override
    def _try_convert_ring_element2int_(ops, x, /):
        'Element -> int|^IndexError'
        if x.is_zero():
            return 0
        ps = x.monomial_coeff_pairs
        if not len(ps) == 1:
            raise IndexError(x)
        [(monomial, coeff)] = ps
        ops4monomial = ops.get_ops4monomial()
        if not ops4monomial.is_one(monomial):
            raise IndexError(x)
        ring_ops4coeff = ops.get_ring_ops4coeff()
        return ring_ops4coeff.try_convert_ring_element2int(coeff)
            # ^IndexError

    @override
    def _mk_ring_element5int_(ops, i, /):
        'int%characteristic -> Element'
        ring_ops4coeff = ops.get_ring_ops4coeff()
        coeff = ring_ops4coeff.mk_ring_element5int(i)
        return ops.mk5coeff(coeff)
    @override
    def _get_characteristic_(ops, /):
        '-> uint # like field characteristic==0'
        ring_ops4coeff = ops.get_ring_ops4coeff()
        return ring_ops4coeff.get_characteristic()



    @override
    def _add_(ops, x, y, /):
        'element -> element -> element #x+y'
        if y.is_zero():
            return x
        if x.is_zero():
            return y

        psL = x.monomial_coeff_pairs
        psR = y.monomial_coeff_pairs
        ring_ops4coeff = ops.get_ring_ops4coeff()
        add4coeff = ring_ops4coeff.add
        is_zero4coeff = ring_ops4coeff.is_zero
        ord_ops4monomial = ops.get_ord_ops4monomial()
        le4monomial = ord_ops4monomial.le
        eq4monomial = ord_ops4monomial.eq
        it = _merge(eq4monomial, le4monomial, add4coeff, is_zero4coeff, psL, psR)
        return ops.mk5std_monomial_coeff_pairs(tuple(it))

    @override
    def _mul_(ops, x, y, /):
        'element -> element -> element #x*y'
        if x.is_zero() or ops.is_one(y):
            return x
        if y.is_zero() or ops.is_one(x):
            return y

        ring_ops4coeff = ops.get_ring_ops4coeff()
        r = Polynomial.mk_zero()
        for monomial, coeff in y.monomial_coeff_pairs:
            p = ops.mul_coeff_monomial(x, coeff, monomial)
            r = ops.add(r, p)
        return r


    @override
    def _neg_(ops, y, /):
        'element -> element #-y'
        if y.is_zero():
            return y
        ring_ops4coeff = ops.get_ring_ops4coeff()
        ps = y.monomial_coeff_pairs
        neg = ring_ops4coeff.neg
        return ops.mk5std_monomial_coeff_pairs(tuple((m,neg(c)) for m, c in ps))

    @override
    def _eq_(ops, x, y, /):
        'element -> element -> bool #x==y'
        psL = x.monomial_coeff_pairs
        psR = y.monomial_coeff_pairs
        if not len(psL) == len(psR):
            return False
        ring_ops4coeff = ops.get_ring_ops4coeff()
        ord_ops4monomial = ops.get_ord_ops4monomial()
        eq4c = ring_ops4coeff.eq
        eq4m = ord_ops4monomial.eq
        return all((eq4c(c0, c1) and eq4m(m0, m1)) for (m0, c0), (m1, c1) in zip(psL, psR))





    @override
    def _sketchy_check_element_(ops, x, /):
        'element -> None|raise TypeError'
        check_type_is(Polynomial, x)

    @override
    def _pow_uint_(ops, x, exp, /, *, _naive=False):
        'element{=!= (0|-1|+1)} -> exp/uint{>=2} -> element'
        return _pow_uint_(ops, x, exp, _naive=_naive)
def _pow_uint_(ops, x, exp, /, *, _naive):
    'element{=!= (0|-1|+1)} -> exp/uint{>=2} -> element'
    assert exp >= 2
    if _naive:
        return IRingOps._pow_uint_(ops, x, exp)
    #二项式定理
    #binomial formula
    #binomial theorem
    ops4monomial = ops.get_ops4monomial()
    ring_ops4coeff = ops.get_ring_ops4coeff()
    ps = x.monomial_coeff_pairs
    assert ps
    if len(ps) == 1:
        [(monomial, coeff)] = ps
        m = ops4monomial.pow(monomial, exp)
        c = ring_ops4coeff.pow_uint(coeff, exp)
        return ops.mk5monomial_coeff(m, c)
    mul4monomial = ops4monomial.mul
    mul4coeff = ring_ops4coeff.mul
    def mul_m_c_pair(p0, p1, /):
        m0, c0 = p0
        m1, c1 = p1
        m = mul4monomial(m0, m1)
        c = mul4coeff(c0, c1)
        return (m, c)
    one8monomial = ops4monomial.mk_one()
    one8coeff = ring_ops4coeff.get_one()
    mk_ring_element5int = ring_ops4coeff.mk_ring_element5int
    def mc5int(i, /):
        return (one8monomial, mk_ring_element5int(i))
    it8mcs = iter_parts5pow__via_binomial_formula__(mc5int, mul_m_c_pair, ps, exp)
    return ops.mk5nonstd_monomial_coeff_pairs(it8mcs)

#end-class IPolynomialOps__using_Polynomial(IPolynomialOps):
def _list_abstractmethods(cls, /):
    return ' '.join(sorted(cls.__abstractmethods__))
assert _list_abstractmethods(IPolynomialOps__using_Polynomial) == 'get_ops4monomial get_ord_ops4monomial get_ring_ops4coeff'
assert _list_abstractmethods(IMonomialOps__using_Monomial) == 'get_ord_ops4var get_ring_ops4exp sketchy_check4var'


class MonomialOps(IMonomialOps__using_Monomial):
    ___no_slots_ok___ = True
    @override
    def sketchy_check4var(ops, var, /):
        '-> var -> None'
        check_type_is(ops._Var, var)
    def __repr__(sf, /):
        return repr_helper(sf, sf._Var, sf._ov, sf._re)
    def __init__(sf, type4var, ord_ops4var, ring_ops4exp, /):
        sf._Var = type4var
        sf._ov = ord_ops4var
        sf._re = ring_ops4exp
    @override
    def get_ring_ops4exp(ops, /):
        '-> ring_ops4exp/IRingOps<exp>'
        return ops._re
    if 1:
        @override
        def get_ord_ops4var(ops, /):
            '-> ord_ops4var/ITotalOrderingOps<var>'
            return ops._ov
class PolynomialOps(IPolynomialOps__using_Polynomial):
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        return repr_helper(sf, sf._rm, sf._om, sf._rc)
    def __init__(sf, ops4monomial, ord_ops4monomial, ring_ops4coeff, /):
        sf._rm = ops4monomial
        sf._om = ord_ops4monomial
        sf._rc = ring_ops4coeff
    @override
    def get_ops4monomial(ops, /):
        '-> ops4monomial/IMonomialOps<monomial>'
        return ops._rm
    @override
    def get_ring_ops4coeff(ops, /):
        '-> ring_ops4coeff/IRingOps<coeff>'
        return ops._rc
    if 1:
        @override
        def get_ord_ops4monomial(ops, /):
            '-> ord_ops4monomial/ITotalOrderingOps<monomial>'
            return ops._om


class Var(ITotalOrdering5le):
    ___no_slots_ok___ = True
    def __hash__(sf, /):
        return hash((type(sf), id(sf._j2nm), sf._j))
    def __eq__(sf, ot, /):
        if not type(ot) is type(sf):return NotImplemented
        if not ot._j2nm is sf._j2nm:raise ValueError
        return sf._j == ot._j
    def __le__(sf, ot, /):
        if not type(ot) is type(sf):return NotImplemented
        if not ot._j2nm is sf._j2nm:raise ValueError
        return sf._j <= ot._j
    def __str__(sf, /):
        s = repr_helper(sf, sf._j2nm, sf._j)
        return f'[<{s}{{{sf.name}}}>]'
    def __repr__(sf, /):
        return f'[<{sf.name}@{sf._j}>]'
        return repr_helper(sf, sf.name, sf.key)
    if 0:
        def __init__(sf, name4show, key4ord, /):
            sf._nm = name4show
            sf._k = key4ord
    def __init__(sf, j2nm, j, /):
        check_type_is(tuple, j2nm)
        sf._j2nm = j2nm
        sf._j = j
        sf._nm = nm = j2nm[j]
        check_type_is(str, nm)
    @property
    def name(sf, /):
        return sf._nm
    @property
    def key(sf, /):
        return sf
        return sf._j
        return sf._k
    def is_inside(sf, j2nm, /):
        return sf._j2nm is j2nm

class TotalOrderingOps4py_ord(ITotalOrderingOps):
    'Ord py_ord'
    __slots__ = ()
    def __repr__(sf, /):
        return repr_helper(sf, *sf.get_args_for_eq_hash())
    @override
    def get_args_for_eq_hash(sf, /):
        return ()
    @override
    def le(ops, lkey, rkey):
        return lkey <= rkey
    @override
    def eq(ops, lkey, rkey):
        return lkey == rkey

class TotalOrderingOps4Var(ITotalOrderingOps):
    'Ord Var'
    __slots__ = ()
    def __repr__(sf, /):
        return repr_helper(sf, *sf.get_args_for_eq_hash())
    @override
    def get_args_for_eq_hash(sf, /):
        return ()
    @override
    def le(ops, lkey, rkey):
        return lkey.key <= rkey.key
    @override
    def eq(ops, lkey, rkey):
        return lkey.key == rkey.key

class TotalOrderingOps4Monomial(ITotalOrderingOps__via_cmp):
    'Ord Monomial'
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        return repr_helper(sf, *sf.get_args_for_eq_hash())
    @override
    def get_args_for_eq_hash(sf, /):
        return (sf.ord_ops4var, sf.ord_ops4exp)
    def __init__(sf, ord_ops4var, ord_ops4exp, /):
        check_type_le(ITotalOrderingOps, ord_ops4var)
        check_type_le(ITotalOrderingOps, ord_ops4exp)
        sf._ov = ord_ops4var
        sf._oe = ord_ops4exp
    @property
    def ord_ops4var(sf, /):
        return sf._ov
    @property
    def ord_ops4exp(sf, /):
        return sf._oe
    def eq4var_exp_pair(ops, lhs_var_exp_pair, rhs_var_exp_pair, /):
        var0, exp0 = lhs_var_exp_pair
        var1, exp1 = rhs_var_exp_pair
        return ops.ord_ops4var.eq(var0, var1) and ops.ord_ops4exp.eq(exp0, exp1)
    def cmp4var_exp_pair(ops, lhs_var_exp_pair, rhs_var_exp_pair, /):
        var0, exp0 = lhs_var_exp_pair
        var1, exp1 = rhs_var_exp_pair
        r = ops.ord_ops4var.cmp(var0, var1) or ops.ord_ops4exp.cmp(exp0, exp1)
        check_type_is(int, r)
        return r
    @override
    def cmp(ops, lkey, rkey):
        return cmp4iterable(lkey.var_exp_pairs, rkey.var_exp_pairs, __cmp__=ops.cmp4var_exp_pair)
    @override
    def eq(ops, lkey, rkey):
        return eq4iterable(lkey.var_exp_pairs, rkey.var_exp_pairs, __eq__=ops.eq4var_exp_pair)
class TotalOrderingOps4Polynomial(ITotalOrderingOps__via_cmp):
    'Ord Polynomial'
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        return repr_helper(sf, *sf.get_args_for_eq_hash())
    @override
    def get_args_for_eq_hash(sf, /):
        return (sf.ord_ops4monomial, sf.ord_ops4coeff)
    def __init__(sf, ord_ops4monomial, ord_ops4coeff, /):
        sf._om = ord_ops4monomial
        sf._oc = ord_ops4coeff
    @property
    def ord_ops4monomial(sf, /):
        return sf._om
    @property
    def ord_ops4coeff(sf, /):
        return sf._oc
    def eq4monomial_coeff_pair(ops, lhs_monomial_coeff_pair, rhs_monomial_coeff_pair, /):
        monomial0, coeff0 = lhs_monomial_coeff_pair
        monomial1, coeff1 = rhs_monomial_coeff_pair
        return ops.ord_ops4monomial.eq(monomial0, monomial1) and ops.ord_ops4coeff.eq(coeff0, coeff1)
    def cmp4monomial_coeff_pair(ops, lhs_monomial_coeff_pair, rhs_monomial_coeff_pair, /):
        monomial0, coeff0 = lhs_monomial_coeff_pair
        monomial1, coeff1 = rhs_monomial_coeff_pair
        return ops.ord_ops4monomial.cmp(monomial0, monomial1) or ops.ord_ops4coeff.cmp(coeff0, coeff1)
    @override
    def cmp(ops, lkey, rkey):
        return cmp4iterable(lkey, rkey, __cmp__=ops.cmp4monomial_coeff_pair)
    @override
    def eq(ops, lkey, rkey):
        return eq4iterable(lkey, rkey, __eq__=ops.eq4monomial_coeff_pair)



class DisplayerOps4Var(IDisplayerOps):
    'show Var'
    __slots__ = ()
    @override
    def display(ops, x, /):
        '-> x -> str'
        return x.name
class DisplayerOps4Monomial(IDisplayerOps):
    'show Monomial'
    ___no_slots_ok___ = True
    def __init__(sf, displayer_ops4var, displayer_ops4exp, ops4monomial, str4one8monomial, /):
        sf.displayer_ops4var = displayer_ops4var
        sf.displayer_ops4exp = displayer_ops4exp
        sf.ops4monomial = ops4monomial
        sf.str4one8monomial = str4one8monomial
        check_type_is(str, str4one8monomial)
    @override
    def display(ops, x, /):
        '-> x -> str'
        ops4monomial = ops.ops4monomial
        if ops4monomial.is_one(x):
            return ops.str4one8monomial
        display4var = ops.displayer_ops4var.display
        display4exp = ops.displayer_ops4exp.display
        ring_ops4exp = ops4monomial.get_ring_ops4exp()
        is_zero4exp = ring_ops4exp.is_zero
        is_one4exp = ring_ops4exp.is_one

        def __():
            for var, exp in x.var_exp_pairs:
                sv = display4var(var)
                if is_zero4exp(exp): raise 000
                elif is_one4exp(exp):
                    yield sv
                else:
                    se = display4exp(exp)
                    yield f'{sv}**{se}'
        return '*'.join(__())
class DisplayerOps4Polynomial(IDisplayerOps):
    'show Polynomial'
    ___no_slots_ok___ = True
    def __init__(sf, displayer_ops4monomial, displayer_ops4coeff, ring_ops4polynomial, /):
        sf.displayer_ops4monomial = displayer_ops4monomial
        sf.displayer_ops4coeff = displayer_ops4coeff
        sf.ring_ops4polynomial = ring_ops4polynomial
    @override
    def display(ops, x, /):
        '-> x -> str'
        ring_ops4polynomial = ops.ring_ops4polynomial
        ring_ops4coeff = ring_ops4polynomial.get_ring_ops4coeff()
        display4coeff = ops.displayer_ops4coeff.display
        if ring_ops4polynomial.is_zero(x):
            c0 = ring_ops4coeff.get_zero()
            return display4coeff(c0)

            #return ops.str4zero
        ops4monomial = ring_ops4polynomial.get_ops4monomial()
        is_one4monomial = ops4monomial.is_one
        display4monomial = ops.displayer_ops4monomial.display
        is_zero4coeff = ring_ops4coeff.is_zero
        is_one4coeff = ring_ops4coeff.is_one
        is_neg_one4coeff = ring_ops4coeff.is_neg_one

        def __():
            for monomial, coeff in x.monomial_coeff_pairs:
                sm = display4monomial(monomial)
                sc = display4coeff(coeff)
                if is_zero4coeff(coeff): raise 000
                elif is_one4monomial(monomial):
                    yield sc
                elif is_one4coeff(coeff):
                    yield sm
                elif is_neg_one4coeff(coeff):
                    yield f'-{sm}'
                else:
                    yield f'{sc}*{sm}'
        return '+'.join(__())


######################
######################
######################
######################
######################
ord_ops4py_ord = TotalOrderingOps4py_ord()
ord_ops4Var = TotalOrderingOps4Var()
ord_ops4Monomial__Var__std = TotalOrderingOps4Monomial(ord_ops4Var, ord_ops4py_ord)
ops4Monomial__Var__int = MonomialOps(Var, ord_ops4Var, ring_ex_ops__int)
ring_ops4Polynomial__Var__int__Fraction = PolynomialOps(ops4Monomial__Var__int, ord_ops4Monomial__Var__std, ring_ex_ops__Fraction)
######################
######################
displayer_ops4Var = DisplayerOps4Var()
displayer_ops4Monomial__Var__int = DisplayerOps4Monomial(displayer_ops4Var, displayer_ops4py_repr, ops4Monomial__Var__int, '1')
displayer_ops4Polynomial__Var__int__Fraction = DisplayerOps4Polynomial(displayer_ops4Monomial__Var__int, displayer_ops4py_str, ring_ops4Polynomial__Var__int__Fraction)
######################
######################



def mk_ordered_vars_ex5str(nms__str, /):
    return mk_ordered_vars_ex(nms__str.split())
def __():
    def mk_ordered_vars(nms, /):
        nms = tuple(nms)
        if not len(set(nms)) == len(nms):raise ValueError
        return tuple(Var(nm, j) for j, nm in enumerate(nms))

def mk_ordered_vars_ex(nms, /):
    j2nm = mk_tuple(nms)
    nm2j = MapView(dict(**{nm:j for j, nm in enumerate(j2nm)}))
    j2var = tuple(Var(j2nm, j) for j in range(len(j2nm)))
    if not len(nm2j) == len(j2nm):raise ValueError
    return (j2nm, j2var, nm2j)

abstract_class_property = abstractmethod
class IPolynomial8PyExpr(ABC):
    'helper used inside py expr'
    __slots__ = ()
    ######################
    @abstract_class_property
    def ring_ops4underlying_polynomial(cls, /):
        '-> IPolynomialOps<underlying_polynomial>'
    @abstract_class_property
    def displayer_ops4underlying_polynomial(cls, /):
        '-> IDisplayerOps<underlying_polynomial>'
    @abstract_class_property
    def ordered_vars_ex(cls, /):
        '-> ordered_vars_ex/(name5idx, var5idx, name2idx)/(tuple<nm>, tuple<Var>, {nm:uint}) #see:mk_ordered_vars_ex()::(j2nm, j2var, nm2j)'
    ######################
    @property
    @abstractmethod
    def underlying_polynomial(sf, /):
        '-> underlying_polynomial #~ring_ops4underlying_polynomial'
    ######################
    ######################
    ######################
    @classmethod
    def get_vars(cls, /):
        (name5idx, var5idx, name2idx) = cls.ordered_vars_ex
        return var5idx
    @classmethod
    def get_var_names(cls, /):
        (name5idx, var5idx, name2idx) = cls.ordered_vars_ex
        return name5idx
    @classmethod
    def mk_polynomials5all_vars(cls, /):
        name5idx = cls.get_var_names()
        polynomials = tuple(map(cls.mk5name4var, name5idx))
        return polynomials

    ######################
    ######################
    ######################
    @classmethod
    def mk5underlying_polynomial(cls, underlying_polynomial, /):
        '-> underlying_polynomial -> IPolynomial8PyExpr'
        return cls(underlying_polynomial)
    @classmethod
    def mk5int(cls, i, /):
        '-> int -> IPolynomial8PyExpr'
        underlying_polynomial = cls.ring_ops4underlying_polynomial.mk_ring_element5int(i)
        return cls.mk5underlying_polynomial(underlying_polynomial)
    @classmethod
    def mk5coeff(cls, coeff, /):
        '-> coeff -> IPolynomial8PyExpr'
        ring_ops = cls.ring_ops4underlying_polynomial
        underlying_polynomial = ring_ops.mk5coeff(coeff)
        return cls.mk5underlying_polynomial(underlying_polynomial)
    @classmethod
    def var5name(cls, name4var, /):
        '-> name4var/str -> var'
        check_type_is(str, name4var)
        (name5idx, var5idx, name2idx) = cls.ordered_vars_ex
        j = name2idx[name4var]
        if not name4var == name5idx[j]:raise ValueError('IPolynomial8PyExpr.__init__()')

        var = var5idx[j]
        check_type_is(Var, var)
        nm = var.name
        if not nm == name4var:raise ValueError('IPolynomial8PyExpr.__init__()')
        if not var.is_inside(name5idx):raise ValueError('IPolynomial8PyExpr.__init__()')
        return var
    @classmethod
    def mk5name4var(cls, name4var, /):
        '-> name4var/str -> IPolynomial8PyExpr'
        var = cls.var5name(name4var)
        underlying_polynomial = cls.ring_ops4underlying_polynomial.mk5var(var)
        return cls.mk5underlying_polynomial(underlying_polynomial)
    ######################
    ######################
    def substitute__name4var(sf, name2ot, /):
        '-> {name4var:IPolynomial8PyExpr} -> IPolynomial8PyExpr'
        cls = type(sf)
        f = cls.var5name
        var2ot = {f(nm):ot for nm, ot in name2ot.items()}
        return sf.substitute__var(var2ot)
    def substitute__var(sf, var2ot, /):
        '-> {var:IPolynomial8PyExpr} -> IPolynomial8PyExpr'
        cls = type(sf)
        ring_ops = cls.ring_ops4underlying_polynomial
        for ot in var2ot.values():
            check_type_is(cls, ot)
        var2underlying_polynomial = {var:ot.underlying_polynomial for var, ot in var2ot.items()}
        underlying_polynomial = ring_ops.substitute(sf.underlying_polynomial, var2underlying_polynomial)
        return mk_IPolynomial8PyExpr5underlying_polynomial(cls, underlying_polynomial, sf)

    def __index__(sf, /):
        '-> int|^IndexError'
        cls = type(sf)
        ring_ops = cls.ring_ops4underlying_polynomial
        return ring_ops.try_convert_ring_element2int(sf.underlying_polynomial)
            # ^IndexError
    def __repr__(sf, /):
        cls = type(sf)
        displayer_ops = cls.displayer_ops4underlying_polynomial
        return displayer_ops.display(sf.underlying_polynomial)
    def __eq__(sf, ot, /):
        if not type(ot) is type(sf):
            return NotImplemented
        cls = type(sf)
        ring_ops = cls.ring_ops4underlying_polynomial
        return ring_ops.eq(sf.underlying_polynomial, ot.underlying_polynomial)
    def is_neg_one(sf, /):
        cls = type(sf)
        ring_ops = cls.ring_ops4underlying_polynomial
        return ring_ops.is_neg_one(sf.underlying_polynomial)
    def is_one(sf, /):
        cls = type(sf)
        ring_ops = cls.ring_ops4underlying_polynomial
        return ring_ops.is_one(sf.underlying_polynomial)
    def is_zero(sf, /):
        cls = type(sf)
        ring_ops = cls.ring_ops4underlying_polynomial
        return ring_ops.is_zero(sf.underlying_polynomial)
    def __bool__(sf, /):
        return not sf.is_zero()
    def __pos__(sf, /):
        return sf
    def __neg__(sf, /):
        if not sf:
            return sf
        cls = type(sf)
        ring_ops = cls.ring_ops4underlying_polynomial
        underlying_polynomial = ring_ops.neg(sf.underlying_polynomial)
        return mk_IPolynomial8PyExpr5underlying_polynomial(cls, underlying_polynomial, sf)

    def __rsub__(sf, ot, /):
        return -(sf.__sub__(ot))
    def __sub__(sf, ot, /):
        if type(ot) is int:
            i = ot
            ot = type(sf).mk5int(i)
        if not type(ot) is type(sf):
            return NotImplemented
        return sf + -ot
    def __radd__(sf, ot, /):
        return sf.__add__(ot)
    def __add__(sf, ot, /):
        if type(ot) is int:
            i = ot
            ot = type(sf).mk5int(i)
        if not type(ot) is type(sf):
            return NotImplemented
        if not ot:
            return sf
        if not sf:
            return ot
        cls = type(sf)
        ring_ops = cls.ring_ops4underlying_polynomial
        underlying_polynomial = ring_ops.add(sf.underlying_polynomial, ot.underlying_polynomial)
        return mk_IPolynomial8PyExpr5underlying_polynomial(cls, underlying_polynomial, sf, ot)
    def __rmul__(sf, ot, /):
        return sf.__mul__(ot)
    def __mul__(sf, ot, /):
        if type(ot) is int:
            i = ot
            ot = type(sf).mk5int(i)
        if not type(ot) is type(sf):
            return NotImplemented
        if not sf or ot.is_one():
            return sf
        if not ot or sf.is_one():
            return ot
        cls = type(sf)
        ring_ops = cls.ring_ops4underlying_polynomial
        underlying_polynomial = ring_ops.mul(sf.underlying_polynomial, ot.underlying_polynomial)
        return mk_IPolynomial8PyExpr5underlying_polynomial(cls, underlying_polynomial, sf, ot)
    def __pow__(sf, u, /, *, _naive=False):
        if not type(u) is int:
            return NotImplemented
        if u < 0:raise ValueError
        if u == 1 or not sf or sf.is_one():
            return sf
        if sf.is_neg_one():
            if u&1:
                return sf
            return -sf
        cls = type(sf)
        if u == 0:
            return cls.mk5int(1)
        ring_ops = cls.ring_ops4underlying_polynomial
        if _naive:
            underlying_polynomial = ring_ops._pow_uint_(sf.underlying_polynomial, u, _naive=_naive)
        else:
            underlying_polynomial = ring_ops.pow_uint(sf.underlying_polynomial, u)
        return mk_IPolynomial8PyExpr5underlying_polynomial(cls, underlying_polynomial, sf)
def mk_IPolynomial8PyExpr5underlying_polynomial(cls, underlying_polynomial, /, *sfs):
    '-> underlying_polynomial -> IPolynomial8PyExpr'
    for sf in sfs:
        check_type_is(cls, sf)
        if underlying_polynomial is sf.underlying_polynomial:
            return sf
    return cls.mk5underlying_polynomial(underlying_polynomial)
#end-class IPolynomial8PyExpr:

class IPolynomial8PyExpr__init(IPolynomial8PyExpr):
    ___no_slots_ok___ = True
    @property
    @override
    def underlying_polynomial(sf, /):
        '-> underlying_polynomial #~ring_ops4underlying_polynomial'
        return sf._p
    def __init__(sf, underlying_polynomial, /):
        sf._p = underlying_polynomial
def mk_type_Polynomial8PyExpr__basic(
    ordered_vars_ex
    ,ring_ops4underlying_polynomial
    ,displayer_ops4underlying_polynomial
    ,/):
    check_type_is(tuple, ordered_vars_ex)
    if not len(ordered_vars_ex) == 3:raise TypeError
    check_type_le(IRingOps, ring_ops4underlying_polynomial)
    check_type_le(IDisplayerOps, displayer_ops4underlying_polynomial)

    kwds = dict(locals())
    class Polynomial8PyExpr(IPolynomial8PyExpr__init):
        locals().update(kwds)
    assert not Polynomial8PyExpr.__abstractmethods__
    return Polynomial8PyExpr
def mk_type_Polynomial8PyExpr__str(
    ordered_vars_ex_or_str
    ,ops_pair4underlying_polynomial
    = (ring_ops4Polynomial__Var__int__Fraction, displayer_ops4Polynomial__Var__int__Fraction)
        # (var/Var, exp/int, coeff/Fraction)
    ,/, *
    , with_vars=False
    , with_polys=False
    ):
    ######################
    if type(ordered_vars_ex_or_str) is str:
        nms__str = ordered_vars_ex_or_str
        ordered_vars_ex = mk_ordered_vars_ex5str(nms__str)
    else:
        ordered_vars_ex = ordered_vars_ex_or_str
    ######################
    (ring_ops4underlying_polynomial
    ,displayer_ops4underlying_polynomial
    ) = ops_pair4underlying_polynomial
    ######################
    T = mk_type_Polynomial8PyExpr__basic(*''
    ,ordered_vars_ex
    ,ring_ops4underlying_polynomial
    ,displayer_ops4underlying_polynomial
    )
    if with_vars:
        if with_polys:
            return T, T.get_vars(), T.mk_polynomials5all_vars()
        return T, T.get_vars()
    if with_polys:
        return T, T.mk_polynomials5all_vars()
    return T
def mk_type_Polynomial8PyExpr__params(ordered_vars_ex_or_str, /, *
    ,ops_pair4coeff
    = (ring_ex_ops__Fraction, displayer_ops4py_str)
        #coeff/Fraction
    ,ops_triple4exp
    = (ring_ex_ops__int, displayer_ops4py_repr, ord_ops4py_ord)
        #exp/int
    ,str4one8monomial = '1'
    ,with_vars = False
    ,with_polys = False
    ):
    ######################
    (ring_ops4coeff
    ,displayer_ops4coeff
    ) = ops_pair4coeff
    (ring_ops4exp
    ,displayer_ops4exp
    ,ord_ops4exp
    ) = ops_triple4exp
    ######################
    ord_ops4exp
    ring_ops4exp
    ring_ops4coeff
    ord_ops4Monomial = TotalOrderingOps4Monomial(ord_ops4Var, ord_ops4exp)
    ops4Monomial = MonomialOps(Var, ord_ops4Var, ring_ops4exp)
    ring_ops4Polynomial = PolynomialOps(ops4Monomial, ord_ops4Monomial, ring_ops4coeff)
    ######################
    displayer_ops4coeff
    displayer_ops4exp
    str4one8monomial
    displayer_ops4Monomial = DisplayerOps4Monomial(displayer_ops4Var, displayer_ops4exp, ops4Monomial, str4one8monomial)
    displayer_ops4Polynomial = DisplayerOps4Polynomial(displayer_ops4Monomial, displayer_ops4coeff, ring_ops4Polynomial)
    ######################
    ######################
    return mk_type_Polynomial8PyExpr__str(*''
    ,ordered_vars_ex_or_str
    ,ops_pair4underlying_polynomial
    :=(ring_ops4Polynomial
      ,displayer_ops4Polynomial
      )
    ,with_vars
    =with_vars
    ,with_polys
    =with_polys
    )


mk_type_Polynomial8PyExpr__str('n u m w I J')

__all__
from seed.math.polynomial.simple_polynomial import mk_type_Polynomial8PyExpr__str
from seed.math.polynomial.simple_polynomial import *
