r'''
py -m seed.tiny_.check_abc

from seed.tiny_.check_abc import get_abstractmethod_names, check_manifest4abstractmethods


>>> from abc import ABC, abstractmethod
>>> class C(ABC):
...     __slots__ = ()
...     @abstractmethod
...     def f(sf, /):pass
...     class g: __isabstractmethod__=True
...     ___manifest4abstractmethods___ = 'f g'

>>> check_manifest4abstractmethods(C, C.___manifest4abstractmethods___)
>>> check_manifest4abstractmethods(C, '.___manifest4abstractmethods___')
>>> check_manifest4abstractmethods(C, 'f g')
>>> check_manifest4abstractmethods(C, 'f') #doctest: +NORMALIZE_WHITESPACE
Traceback (most recent call last):
    ...
TypeError:
        missing = ['g']
        excess = []
        expected = ['f']
        actual = ['f', 'g']
<BLANKLINE>


>>> check_manifest4abstractmethods(C, 'f g h') #doctest: +NORMALIZE_WHITESPACE
Traceback (most recent call last):
    ...
TypeError:
        missing = []
        excess = ['h']
        expected = ['f', 'g', 'h']
        actual = ['f', 'g']
<BLANKLINE>


>>> check_manifest4abstractmethods(C, 'f h') #doctest: +NORMALIZE_WHITESPACE
Traceback (most recent call last):
    ...
TypeError:
        missing = ['g']
        excess = ['h']
        expected = ['f', 'h']
        actual = ['f', 'g']
<BLANKLINE>


#'''

#from seed.tiny_.check_abc import get_abstractmethod_names, check_manifest4abstractmethods

from seed.tiny_.containers import mk_frozenset
from seed.helper.str2__all__ import str2__all__
from seed.debug.print_err import print_err, print_ferr

#cls.__abstractmethods__ :: {attr}
#descriptor.__isabstractmethod__ :: bool

def get_abstractmethod_names(cls, /):
    if not isinstance(cls, type): raise TypeError
    return mk_frozenset(getattr(cls, '__abstractmethods__', ''))

def check_manifest4abstractmethods(cls, abstractmethod_names__str, /):
    actual = get_abstractmethod_names(cls)
    if abstractmethod_names__str.startswith('.'):
        attr4manifest = abstractmethod_names__str[1:]
        abstractmethod_names__str = getattr(cls, attr4manifest)
    expected = mk_frozenset(str2__all__(abstractmethod_names__str))
    if not actual == expected:
        missing = actual - expected
        excess = expected - actual
        if 0:
            print_err(f'missing = {missing}')
            print_err(f'excess = {excess}')
            print_err(f'actual = {actual}')
            print_err(f'expected = {expected}')
        s = f'''
        missing = {sorted(missing)}
        excess = {sorted(excess)}
        expected = {sorted(expected)}
        actual = {sorted(actual)}
        '''
        raise TypeError(s)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #<BLANKLINE>
    #Traceback (most recent call last):




