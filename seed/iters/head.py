


__all__ = ('''

    head_ex head tail
    take_ex take drop
    take_lt take_eq
    unsafe_last

    LenError
        TooFewError TooManyError
'''.split())


import itertools

class LenError(ValueError):
    def __init__(self, *args, **kwargs):
        if not args:
            args = (self._default,)
        super().__init__(*args, **kwargs)
        
class TooFewError(LenError):
    _default = 'too few values to unpack'

class TooManyError(LenError):
    _default = 'too many values to unpack'
    pass
##class NotExactlyLenError(LenError):
##    _default = 'too many values to unpack'
##    pass


class __Default: pass
def head_ex(iterable, except_factory=TooFewError, *, default=None):
    '''[a] -> (a, [a]); split list into head and tail

if empty and except_factory is None return default
'''
    
    iterable = iter(iterable)
    for h in iterable:
        break
    else:
        if except_factory is not None:
            raise except_factory()
        return default

    # NOTE: iterable should not be a container
    return h, iterable
def head(iterable, except_factory=TooFewError, *, default=None):
    'see head_ex'
    h, iterable = head_ex(iterable, except_factory, default)
    return h
def tail(iterable, except_factory=TooFewError, *, default=None):
    'see head_ex'
    h, iterable = head_ex(iterable, except_factory, default)
    return iterable



def take_ex(n, iterable, except_factory=TooFewError, *, default_factory=None):
    '''[a] -> ([a], [a]); len(1st result) == n

if too few input and except_factory is None,
use default_factory to fill up total n elements.
'''
    iterable = iter(iterable)
    if n is None:
        raise TypeError('n should be int >= 0')
    
    first_n = tuple(itertools.islice(iterable, n))
    if len(first_n) != n:
        first_less_n = first_n
        if except_factory is not None:
            raise except_factory()
        
        m = n - len(first_less_n)
        assert m > 0
        first_n = first_less_n + tuple(default_factory() for _ in range(m))
    return first_n, iterable

def take(n, iterable, except_factory=TooFewError, *, default_factory=None):
    'see take_ex'
    first_n, iterable = take_ex(n, iterable, except_factory, default)
    return first_n
def drop(n, iterable, except_factory=TooFewError, *, default_factory=None):
    'see take_ex'
    first_n, iterable = take_ex(n, iterable, except_factory, default_factory=default_factory)
    return iterable



def take_lt(n, iterable):
    iterable = iter(iterable)
    if n is None:
        raise TypeError('n should be int')
    first_less_n = tuple(itertools.islice(iterable, n-1))
    assert n < 0 or len(first_less_n) < n # if n >= 0

    for _ in iterable:
        raise TooManyError()
    
    return first_less_n


def take_eq(n, iterable):
    first = take_lt(n+1, iterable)
    if len(first) != n:
        raise TooFewError()
    return first


def unsafe_last(nonempty_iterable):
    for r in nonempty_iterable: pass
    return r






    

