r'''[[[
e ../../python3_src/seed/math/pow_accelerate_framework.py
py -m seed.math.pow_accelerate_framework
from seed.math.pow_accelerate_framework import IPowAccelerateFramework__succ1_double1, IPowAccelerateFramework__succ2_double1_odd2

LucasSequence:
    A[2m] = f1<m>(A[m])
    A[2m+1] = f2<m>(A[m+1], A[m])
    A[m+2] = f3<m>(A[m+1], A[m])
    ==>>
    (A[2m+1], A[2m]) = f4<m>(A[m+1], A[m])
        = (f2<m>(A[m+1], A[m]), f1<m>(A[m]))
    (A[m+2], A[m+1]) = f5<m>(A[m+1], A[m])
        = (f3<m>(A[m+1], A[m]), echo(A[m+1]))
#]]]'''
__all__ = '''
    IPowAccelerateFramework__succ1_double1
    IPowAccelerateFramework__succ2_double1_odd2
    '''.split()
from seed.abc.abc__ver0 import ABC, abstractmethod, override
from seed.math.max_power_of_base_as_factor_of_ import factor_pint_out_2_powers


class IPowAccelerateFramework__succ1_double1(ABC):
    __slots__ = ()

    @abstractmethod
    def to_succ(sf, n, An, /):
        'n -> A[n] -> A[n+1]'
    @abstractmethod
    def to_double(sf, n, An, /):
        'n -> A[n] -> A[2*n]'

    def accelerate_to(sf, A0, n, /):
        'A[0] -> n -> A[n]'
        if not n >= 0: raise ValueError
        if n == 0: return A0
        m = n
        A1 = sf.to_succ(0, A0)
        n, An = 1, A1
        s = bin(n)
        assert s[:3] == '0b1'
        s = s[3:]
        for bit in s:
            n, An = 2*n, sf.to_double(n, An)
            if bit=='1':
                n, An = n+1, sf.to_succ(n, An)
        assert n == m
        return An

class _PowAccelerateFramework__succ1_double1__to_impl_succ2_double1_odd2(IPowAccelerateFramework__succ1_double1):
    r'''
    sf.A[n] =[def]= (sf2.A[n], sf2.A[n+1])
    A := sf.A
    B := sf2.A
    #'''
    def __init__(sf, sf2, /):
        if not isinstance(sf2, IPowAccelerateFramework__succ2_double1_odd2): raise TypeError
        sf._sf2 = sf2

    @override
    def to_succ(sf, n, An, /):
        'n -> A[n] -> A[n+1]'
        (Bn, Bn1) = An
        Bn2 = sf._sf2.to_succ(n, Bn, Bn1)
        An1 = (Bn1, Bn2)
        return An1

    @override
    def to_double(sf, n, An, /):
        'n -> A[n] -> A[2*n]'
        (Bn, Bn1) = An
        B_2n = sf._sf2.to_double(n, Bn)
        B_2n1 = sf._sf2.to_odd(n, Bn, Bn1)
        A_2n = (B_2n, B_2n1)
        return A_2n

class IPowAccelerateFramework__succ2_double1_odd2(ABC):
    __slots__ = ()

    @abstractmethod
    def to_succ(sf, n, An, An1/):
        'n -> A[n] -> A[n+1] -> A[n+2]'
    @abstractmethod
    def to_double(sf, n, An, /):
        'n -> A[n] -> A[2*n]'
    @abstractmethod
    def to_odd(sf, n, An, An1, /):
        'n -> A[n] -> A[n+1] -> A[2*n+1]'


    def accelerate_to(sf, A0, A1, n, /):
        'A[0] -> A[1] -> n -> A[n]'
        if not n >= 0: raise ValueError
        if n < 2:
            return [A0, A1][n]

        (e, odd) = factor_pint_out_2_powers(n)

        if odd == 1:
            Aodd = A1
        else:
            sf1 = _PowAccelerateFramework__succ1_double1__to_impl_succ2_double1_odd2(sf)
            Z0 = (A0,A1)
            Zodd = sf.accelerate_to(Z0, odd)
            (Aodd, Aodd1) = Zodd

        n, An = odd, Aodd
        for _ in range(e):
            n, An = 2*n, sf.to_double(n, An)
        return An

