
__all__ = '''
    ___O___
    O

    get_O
    get_O__default
    get_O__fdefault
    get_O__then_else
    '''.split()

from typing import Optional
from seed.helper.repr_input import repr_helper

___O___ = '___O___'

class O:
    '''
example:
    >>> @O(time='V')
    ... def canonize_planar_graph(g): ...

    >>> get_O(canonize_planar_graph)
    O(time = 'V')
'''
    __slots__ = 'time space'.split()

    def __init__(__self, *, time:Optional[str], space:Optional[str]=None):
        __self.time = time
        __self.space = space
    def __call__(__self, __f):
        Nothing = object()
        if getattr(__f, ___O___, Nothing) is not Nothing:
            raise Exception('O(...) has been set')
        setattr(__f, ___O___, __self)
        return __f
    def __repr__(__self):
        if __self.space is None:
            kwargs = {}
        else:
            kwargs = {'space': __self.space}
        return repr_helper(__self, time=__self.time, **kwargs)

def get_O(__f):
    return getattr(__f, ___O___)
def get_O__default(__f, __default):
    return getattr(__f, ___O___, __default)
def get_O__fdefault(__f, __fdefault):
    Nothing = object()
    result = getattr(__f, ___O___, Nothing)
    if result is Nothing:
        return __fdefault()
    return result
def get_O__then_else(__f, __then, __else):
    Nothing = object()
    result = getattr(__f, ___O___, Nothing)
    if result is Nothing:
        return __else()
    return __then(result)

def _t():
    @O(time='V')
    def canonize_planar_graph(g): ...
    assert repr(get_O(canonize_planar_graph)) == "O(time = 'V')"

if __name__ == "__main__":
    _t()

    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #doctest: +NORMALIZE_WHITESPACE
