
'''
why?
    # I want type to be difference

    from collections import namedtuple
    A = namedtuple('A', ['a'])
    B = namedtuple('B', ['b'])
    a = A(0)
    b = B(0)
    assert hash(a) == hash(b)
    assert a == b

    # when use as key, be replaced!!!



>>> mk = _namedtuple # collections.namedtuple
>>> A = mk('A', ['a'])
>>> B = mk('B', ['b'])
>>> a = A(0)
>>> b = B(0)
>>> hash(a) == hash(b)
True
>>> a == b
True
>>> A() # without args
Traceback (most recent call last):
    ...
TypeError: __new__() missing 1 required positional argument: 'a'


>>> mk = namedtuple # mine new namedtuple
>>> A = mk('A', ['a'])
>>> B = mk('B', ['b'])
>>> a = A(0)
>>> b = B(0)
>>> hash(a) == hash(b) # almost False
False
>>> a == b
False
>>> A() # without args
Traceback (most recent call last):
    ...
TypeError: __new__() missing 1 required positional argument: 'a'



'''



__all__ = '''
    namedtuple
    '''.split()

from collections import namedtuple as _namedtuple
from weakref import WeakValueDictionary, ref

namedtuple_cache = WeakValueDictionary()
class _ChangeEq:
    def __eq__(self, other):
        if not isinstance(other, _ChangeEq):
            return False
        if self._base_namedtuple_ref() is not other._base_namedtuple_ref():
            return False
        return super().__eq__(other)
    def __hash__(self):
        return hash((id(self._base_namedtuple_ref()), super().__hash__()))
def namedtuple(typename, field_names, *, rename=False, module=None):
    #field_names = tuple(field_names)
    t = _namedtuple(typename, field_names, rename=rename, module=module)
    k = (t.__qualname__, t._fields)
    may_cls = namedtuple_cache.get(k, None)
    if may_cls is not None:
        cls = may_cls
    else:
        class cls(_ChangeEq, t):
            pass
        cls._base_namedtuple_ref = ref(cls)
        cls.__name__ = t.__name__
        cls.__module__ = t.__module__
        cls.__qualname__ = t.__qualname__
        namedtuple_cache[k] = cls
    return cls




if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):



