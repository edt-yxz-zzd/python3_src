
'''
like types.SimpleNamespace, but not allow "assign/delete"

see: types.SimpleNamespace
'''
__all__ = '''
    ImmutableNamespace
    '''.split()

from types import MappingProxyType
from .CachedProperty import CachedProperty
from seed.helper.repr_input import repr_helper_ex




"""
def _get_vars(self):
    # return vars(self)
    return super(ImmutableNamespace, self).__getattribute__('__dict__')
def _get_kwargs(self):
    return _get_vars(self)['_kwargs_']
def _set_kwargs(self, kwargs):
    _get_vars(self)['_kwargs_'] = kwargs
"""

def _get_kwargs(self):
    return super(ImmutableNamespace, self).__getattribute__('_ImmutableNamespace__kwargs')
def _set_kwargs(self, kwargs):
    super(ImmutableNamespace, self).__setattr__('_ImmutableNamespace__kwargs', kwargs)
def _set_hash_value(self, hash_value):
    super(ImmutableNamespace, self).__setattr__('_ImmutableNamespace__hash_value', hash_value)




class ImmutableNamespace:
    '''
example:
    >>> ImmutableNamespace()
    ImmutableNamespace()
    >>> ImmutableNamespace(a = 1)
    ImmutableNamespace(a = 1)
    >>> ImmutableNamespace(b = 0, a = 1)
    ImmutableNamespace(a = 1, b = 0)

    >>> ns = ImmutableNamespace()
    >>> ns.a = 1
    Traceback (most recent call last):
        ...
    AttributeError: a
    >>> ns
    ImmutableNamespace()

    >>> ns = ImmutableNamespace(b = 0, a = 1)
    >>> ns.a = 1
    Traceback (most recent call last):
        ...
    AttributeError: a
    >>> del ns.a
    Traceback (most recent call last):
        ...
    AttributeError: a
    >>> ns.a
    1

    >>> type(hash(ns))
    <class 'int'>
    >>> len(vars(ns))
    2
    >>> dir(ns)
    ['a', 'b']
    >>> sorted(vars(ns))
    ['a', 'b']
    >>> vars(ImmutableNamespace())
    mappingproxy({})
    >>> ns = ImmutableNamespace(a = 1)
    >>> vars(ns)
    mappingproxy({'a': 1})
    >>> _get_kwargs(ns)
    mappingproxy({'a': 1})


    #>>> _get_vars(ns) == {'_kwargs_': {'a': 1}, '_hash_value': hash(ns)}
    #True

'''
    __slots__ = '''
        _ImmutableNamespace__kwargs
        _ImmutableNamespace__hash_value
        '''.split()

    def __init__(self, **kwargs):
        '''
self.!__dict__ = {'_kwargs_':??, '_hash_value':??}
self.?__dict__ = self.!__dict__['_kwargs_']
'''
        _set_kwargs(self, MappingProxyType(kwargs))
        #for k, v in kwargs.items(): setattr(self, k, v)

    def __dir__(self):
        return tuple(_get_kwargs(self))
    def __getattribute__(self, attr):
        d = _get_kwargs(self)
        try:
            return d[attr]
        except KeyError:
            pass

        if attr == '__dict__':
            # kwargs as __dict__ for user!
            return d
            return MappingProxyType(d)

        return super().__getattribute__(attr)

        d = _get_kwargs(self)
        if attr == '__dict__':
            # kwargs as __dict__ for user!
            return MappingProxyType(d)
        elif attr == '_hash_value':
            return super().__getattribute__(attr)

        try:
            return d[attr]
        except KeyError:
            pass
        raise AttributeError(attr)

    def __setattr__(self, attr, obj):
        raise AttributeError(attr)
    def __delattr__(self, attr):
        raise AttributeError(attr)
    def __repr__(self):
        d = _get_kwargs(self)
        keys = sorted(d)
        return repr_helper_ex(self, (), keys, {}, ordered_attrs_only=True)
        """
        d = _get_kwargs(self)
        keys = sorted(d)
        items = ("{}={!r}".format(k, d[k]) for k in keys)
        return "{}({})".format(type(self).__name__, ", ".join(items))
        """

    def __eq__(self, other):
        if self is other: return True
        #if not isinstance(other, __class__): return NotImplemented
        return (type(self) is type(other)
            and hash(self) == hash(other)
            and _get_kwargs(self) == _get_kwargs(other)
            )
    def __hash__(self):
        try:
            return self.__hash_value
        except AttributeError:
            cls = type(self)
            hash_value = cls.__calc_hash_value__(self)
            #self.__hash_value = hash_value
            _set_hash_value(self, hash_value)
        return self.__hash_value
    #@CachedProperty.at(instance2cached_dict=_get_vars)
    def __calc_hash_value__(self):
        d = _get_kwargs(self)
        cls = type(self)
        items = sorted(d.items())
        repr_data = id(cls), tuple(items)
        return hash(repr_data)






if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


