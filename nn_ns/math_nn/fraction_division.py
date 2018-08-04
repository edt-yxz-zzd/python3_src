

'''
make division be fraction division instead of float division

usage:
    divs = int.__truediv__, int.__rtruediv__
    org_divs = install_divs(divs)
    org_divs = install_factiondiv()
    org_divs = install_org_truediv()

    with scoped_int_div_env(divs): ...
    with scoped_factiondiv_env(): ...
    with scoped_org_truediv_env(): ...


fail:
    int.__truediv__ = truediv
    TypeError: can't set attributes of built-in/extension type 'int'
'''

from numbers import Integral
from fractions import Fraction
import contextlib
import nn_ns.sympy_util.bug_fix__resister_number_types

'''
sympy bugs from fraction_division.py
bug:
    from sympy import Integer
    from numbers import Integral
    assert not issubclass(Integer, Integral)
    TODO::sympy abstract base class for Number int float complex....
    class abc.ABCMeta

'''


__all__ = ('install_divs, install_factiondiv, install_org_truediv'
           ', scoped_int_div_env, scoped_factiondiv_env, scoped_org_truediv_env'
           .split(', '))



org_int_truediv = int.__truediv__
org_int_rtruediv = int.__rtruediv__
# no int.__itruediv__
# org_int_itruediv = int.__itruediv__ 


def int_factiondiv(self, other):
    assert isinstance(self, int)
    if isinstance(other, Integral):
        return Fraction(int(self), int(other))
    return org_int_truediv(self, other)

def int_rfactiondiv(self, other):
    assert isinstance(self, int)
    if isinstance(other, Integral):
        return Fraction(int(other), int(self))
    return org_int_rtruediv(self, other)



##def int_ifactiondiv(self, other):
##    return int_factiondiv(self, other)


org_int_truedivs = org_int_truediv, org_int_rtruediv
int_factiondivs = int_factiondiv, int_rfactiondiv

def set_int_divs(truediv, rtruediv):
    int.__truediv__ = truediv
    int.__rtruediv__ = rtruediv
    #int.__itruediv__ = itruediv
def get_int_divs():
    return int.__truediv__, int.__rtruediv__#, int.__itruediv__

def install_divs(divs):
    org_divs = get_int_divs()
    set_int_divs(*divs)
    return org_divs

def install_factiondiv():
    return install_divs(int_factiondivs)
def install_org_truediv():
    return install_divs(org_int_truedivs)
    
@contextlib.contextmanager 
def scoped_int_div_env(divs):
    org_divs = install_divs(divs)
    yield
    install_divs(org_divs)
    return

def scoped_factiondiv_env():
    return scoped_int_div_env(int_factiondivs)
def scoped_org_truediv_env():
    return scoped_int_div_env(org_int_truedivs)
    













