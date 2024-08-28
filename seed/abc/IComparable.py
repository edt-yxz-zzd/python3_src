
r'''
from seed.abc.IComparable import IComparable, compare, ITypeComparable, type_compare, check_compare_result, real2compare_result, int2compare_result, compare_by_lt_eq
#'''


__all__ = '''
    compare
    type_compare
    check_compare_result
    real2compare_result
        int2compare_result
    compare_by_lt_eq

    IComparable
        ITypeComparable
    '''.split()



from seed.abc.abc import ABC, abstractmethod, override



def _compare(lhs, rhs):
    may_cmp = getattr(type(lhs), '___compare___', None)
    if may_cmp is not None:
        cmp = may_cmp
        return cmp(lhs, rhs)
    return NotImplemented
def compare(lhs, rhs):
    'IComparable -> IComparable -> [-1..+1]'
    if lhs is rhs:
        r = 0
    else:
        r = _compare(lhs, rhs)
    if r is NotImplemented:
        rr = _compare(rhs, lhs)
        if rr is NotImplemented:
            raise NotImplementedError(f'compare({lhs!r}, {rhs!r})')
        check_compare_result(rr)
        r = -rr
    check_compare_result(r)
    if not (lhs is not rhs or r == 0): raise logic-err
    return r


def real2compare_result(i):
    r'''for: int/fractions.Fraction/...
    but not for: float/decimal.Decimal
        to avoid overflow/underflow
        use compare_by_lt_eq instead
    #'''
    if i > 0:
        r = +1
    elif i < 0:
        r = -1
    else:
        r = 0
    return r
int2compare_result = real2compare_result

def check_compare_result(r):
    if type(r) is not int: raise TypeError
    if not (-2 < r < 2): raise TypeError

def type_compare(lhs_cls, rhs_cls):
    'type -> type -> [-1..+1]'
    if lhs_cls is rhs_cls:
        r = 0
    else:
        r = _type_compare(lhs_cls, rhs_cls)
    if r is NotImplemented:
        rr = _type_compare(rhs_cls, lhs_cls)
        if rr is NotImplemented:
            raise NotImplementedError(f'type_compare({lhs_cls!r}, {rhs_cls!r})')
        check_compare_result(rr)
        r = -rr
    check_compare_result(r)
    if not ((lhs_cls is rhs_cls) is (r == 0)): raise logic-err
    return r
def _type_compare(lhs_cls, rhs_cls):
    may_cmp = getattr(lhs_cls, '___type_compare___', None)
    if may_cmp is not None:
        cmp = may_cmp
        return cmp(rhs_cls)
    return NotImplemented

def compare_by_lt_eq(lhs, rhs):
    if lhs < rhs:
        return -1
    if lhs == rhs:
        return 0
    return +1

class IComparable(ABC):
    __slots__ = ()
    @abstractmethod
    def ___compare___(sf, ot, /):
        'obj -> ([-1..+1]|NotImplemented)'
    def __lt__(sf, ot):
        r = compare(sf, ot)
        return r < 0
    def __le__(sf, ot):
        r = compare(sf, ot)
        return r <= 0
    def __gt__(sf, ot):
        #return not sf <= ot
        r = compare(sf, ot)
        return r > 0
    def __ge__(sf, ot):
        #return not sf < ot
        r = compare(sf, ot)
        return r >= 0
    def __eq__(sf, ot):
        r = compare(sf, ot)
        return r == 0
    def __ne__(sf, ot):
        return not sf == ot
        r = compare(sf, ot)
        return r != 0

class ITypeComparable(IComparable):
    __slots__ = ()
    @abstractmethod
    def ___same_type_compare___(sf, ot, /):
        '__class__ -> [-1..+1]'
        assert type(sf) is type(ot)
    @classmethod
    @abstractmethod
    def ___type_compare___(cls, ot_cls):
        'type -> ([-1..+1]|NotImplemented)'

    @override
    def ___compare___(sf, ot, /):
        t0 = type(sf)
        t1 = type(ot)
        if t0 is t1:
            return t0.___same_type_compare___(sf, ot)
        return type_compare(t0, t1)










