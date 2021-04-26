r'''
seed.func_tools.cmp
from seed.func_tools.cmp import std_cmp, le2lt, lt2le, lt2eq, lt2cmp, cmp2lt, cmp2eq, cmp2le

used by:
    seed.iters.cmp4iterable

#'''

__all__ = '''
    std_cmp
    le2lt

    lt2le
    lt2eq
    lt2cmp

    cmp2lt
    cmp2eq
    cmp2le

    '''.split()

import operator
#from seed.iters.cmp4iterable import std_cmp, le2lt, lt2le, lt2eq, lt2cmp, cmp2lt, cmp2eq, cmp2le


def le2lt(__le__):
    if __le__ is None:
        __le__ = operator.__le__
    def __lt__(lhs, rhs, /):
        if __le__(rhs, lhs):
            # lhs >= rhs
            return False
        else:
            # lhs < rhs
            return True
    return __lt__


def lt2le(__lt__):
    if __lt__ is None:
        __lt__ = operator.__lt__
    def __le__(lhs, rhs, /):
        if __lt__(rhs, lhs):
            # lhs > rhs
            return False
        else:
            # lhs <= rhs
            return True
    return __le__


def lt2eq(__lt__):
    if __lt__ is None:
        __lt__ = operator.__lt__
    def __eq__(lhs, rhs, /):
        if __lt__(lhs, rhs):
            # lhs < rhs
            return False
        elif __lt__(rhs, lhs):
            # lhs > rhs
            return False
        else:
            # lhs == rhs
            return True
    return __eq__


def lt2cmp(__lt__):
    if __lt__ is None:
        __lt__ = operator.__lt__
    def __cmp__(lhs, rhs, /):
        '-> (-1|0|+1) #(<|==|>)#(before|same|after)'
        if __lt__(lhs, rhs):
            # lhs < rhs
            return -1
        elif __lt__(rhs, lhs):
            # lhs > rhs
            return +1
        else:
            # lhs == rhs
            return 0
    return __cmp__

def cmp2lt(__cmp__):
    if __cmp__ is None:
        __lt__ = operator.__lt__
    else:
        def __lt__(lhs, rhs, /):
            return __cmp__(lhs, rhs) < 0
    return __lt__

def cmp2le(__cmp__):
    if __cmp__ is None:
        __le__ = operator.__le__
    else:
        def __le__(lhs, rhs, /):
            return __cmp__(lhs, rhs) <= 0
    return __le__

def cmp2eq(__cmp__):
    if __cmp__ is None:
        __eq__ = operator.__eq__
    else:
        def __eq__(lhs, rhs, /):
            return __cmp__(lhs, rhs) == 0
    return __eq__


std_cmp = lt2cmp(None)


