
r"""
>>> f = Value2Lazy

>>> d = LazyValueDict()
>>> d
LazyValueDict.from_lazy_items_ex({}, {})
>>> repr(eval(repr(d))) == repr(d)
True

>>> d = LazyValueDict({0:1})
Traceback (most recent call last):
    ...
TypeError: not callable: 1

>>> d = LazyValueDict(a=f(9))
>>> len(d)
1
>>> [*iter(d)]
['a']
>>> d
LazyValueDict.from_lazy_items_ex({}, {'a': Value2Lazy(9)})
>>> repr(eval(repr(d))) == repr(d)
True

>>> d['a']
9
>>> d
LazyValueDict.from_lazy_items_ex({'a': 9}, {})
>>> repr(eval(repr(d))) == repr(d)
True

>>> d['b'] = 0
Traceback (most recent call last):
    ...
TypeError: not callable: 0


>>> d['c'] = f(8)
>>> sorted(d)
['a', 'c']
>>> d
LazyValueDict.from_lazy_items_ex({'a': 9}, {'c': Value2Lazy(8)})
>>> repr(eval(repr(d))) == repr(d)
True

>>> del d['a']
>>> d
LazyValueDict.from_lazy_items_ex({}, {'c': Value2Lazy(8)})
>>> repr(eval(repr(d))) == repr(d)
True

>>> d['c']
8
>>> d
LazyValueDict.from_lazy_items_ex({'c': 8}, {})
>>> repr(eval(repr(d))) == repr(d)
True

#"""


__all__ = '''
    LazyValueDict
    Value2Lazy
    mk_LazyValueDict
    '''.split()

#from collections import UserDict
from collections.abc import MutableMapping
from functools import partial
from seed.helper.repr_input import repr_helper

class Value2Lazy:
    def __init__(self, v):
        self.__v = v
    def __call__(self):
        return self.__v
    def __repr__(self):
        return repr_helper(self, self.__v)
#value2lazy = Value2Lazy

def mk_LazyValueDict(key2value, key2lazy):
    return LazyValueDict.from_lazy_items_ex(key2value, key2lazy)
class LazyValueDict(MutableMapping):
    def __init__(__self, *args, **kw):
        d = dict(*args, **kw)
        __self.__d = {}
        __self.update(d)

    @classmethod
    def from_lazy_items_ex(cls, key2value, key2lazy):
        self = cls()
        self.update_ex(key2value, key2lazy)
        return self
    @classmethod
    def value2lazy(cls, v):
        return Value2Lazy(v)
    def update_ex(self, key2value, key2lazy):
        d = self.__d
        kvs = iter(key2value.items()) if hasattr(key2value, 'items') else iter(key2value)
        d.update((k, (True, v)) for k, v in kvs)
        self.update(key2lazy)

    def set_lazy(__self, __k, __f, *args, **kw):
        f = partial(__f, *args, **kw)
        __self[__k] = f
    def set_value(self, k, v):
        self[k] = self.value2lazy(v)
    def __to_2_dicts(self):
        key2value = {}
        key2lazy = {}
        for k, (is_v, x) in self.__d.items():
            k2x = key2value if is_v else key2lazy
            k2x[k] = x
        return key2value, key2lazy
    def __repr__(self):
        #bug: return repr_helper(self, self.__d)
        cls_nm = type(self).__name__
        key2value, key2lazy = self.__to_2_dicts()
        return f"{cls_nm}.from_lazy_items_ex({key2value}, {key2lazy})"



    def __setitem__(self, k, fv):
        if not callable(fv): raise TypeError(f"not callable: {fv!r}")
        self.__d[k] = (False, fv)
    def __getitem__(self, k):
        is_v, x = self.__d[k]
        if is_v:
            v = x
        else:
            fv = x
            v = fv()
            self.__d[k] = (True, v)
        return v

    def __delitem__(self, k):
        del self.__d[k]
    def __iter__(self):
        return iter(self.__d)
    def __len__(self):
        return len(self.__d)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


