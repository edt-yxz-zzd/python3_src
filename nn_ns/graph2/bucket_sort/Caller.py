

'''
example:
    >>> ls = []
    >>> Caller(list.append, 3)(ls)
    >>> ls
    [3]
    >>> Partial(list.append, ls)(2)
    >>> ls
    [3, 2]
'''

__all__ = '''
    Caller
    Partial
    '''.split()
from operator import attrgetter, itemgetter, methodcaller
from functools import partial

class CallerBase:
    def __init__(self, __func, *__args, **__kwargs):
        self.args = __args
        self.kwargs = __kwargs
        self.func = __func
class Caller(CallerBase):
    # treat init args as additional args
    # like operator.methodcaller
    def __call__(self, *__args, **__kwargs):
        return self.func(*__args, *self.args, **__kwargs, **self.kwargs)
class Partial(CallerBase):
    # treat init args as self...
    # like functools.partial
    def __call__(self, *__args, **__kwargs):
        return self.func(*self.args, *__args, **self.kwargs, **__kwargs)
if __name__ == "__main__":
    import doctest
    doctest.testmod()

