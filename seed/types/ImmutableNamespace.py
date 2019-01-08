
'''
like types.SimpleNamespace, but not allow assignment

see: types.SimpleNamespace
'''
__all__ = '''
    ImmutableNamespace
    '''.split()

class ImmutableNamespace:
    '''
example:
    >>> ImmutableNamespace()
    ImmutableNamespace()
    >>> ImmutableNamespace(a=1)
    ImmutableNamespace(a=1)
    >>> ImmutableNamespace(b=0, a=1)
    ImmutableNamespace(a=1, b=0)

    >>> ns = ImmutableNamespace()
    >>> ns.a = 1
    Traceback (most recent call last):
        ...
    AttributeError: a
    >>> ns
    ImmutableNamespace()

    >>> ns = ImmutableNamespace(b=0, a=1)
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
'''
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        #for k, v in kwargs.items(): setattr(self, k, v)

    def __setattr__(self, attr, obj):
        raise AttributeError(attr)
    def __delattr__(self, attr):
        raise AttributeError(attr)
    def __repr__(self):
        d = self.__dict__
        keys = sorted(d)
        items = ("{}={!r}".format(k, d[k]) for k in keys)
        return "{}({})".format(type(self).__name__, ", ".join(items))

    def __eq__(self, other):
        #if not isinstance(other, __class__): return NotImplemented
        return (type(self) is type(other)
            and self.__dict__ == other.__dict__
            )
    def __hash__(self):
        return hash((id(type(self)), frozenset(self.__dict__.items())))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


