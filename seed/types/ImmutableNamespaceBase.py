
'''

ImmutableNamespaceBase vs ImmutableNamespace
    ImmutableNamespaceBase requires cls.ordered_attr_name_seq
    instance of concrete subclass of ImmutableNamespaceBase have same attrs
    instances of ImmutableNamespace have diff attrs

see: ImmutableNamespace

'''
__all__ = '''
    ImmutableNamespaceBase
    '''.split()

from .NamedReadOnlyProperty import NamedReadOnlyProperty



class ImmutableNamespaceBase:
    '''
example:
    >>> class NoAttrs(ImmutableNamespaceBase, ordered_attr_name_seq=''):pass
    >>> class A(ImmutableNamespaceBase, ordered_attr_name_seq='a'):pass
    >>> class AB(ImmutableNamespaceBase, ordered_attr_name_seq='ab'):pass

    >>> NoAttrs()
    NoAttrs()
    >>> A(a=1)
    A(a=1)
    >>> AB(b=0, a=1)
    AB(a=1, b=0)

    >>> ns = NoAttrs()
    >>> ns.a = 1
    Traceback (most recent call last):
        ...
    AttributeError: a
    >>> ns
    NoAttrs()

    >>> ns = AB(b=0, a=1)
    >>> ns.a = 2
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

    >>> A.a
    NamedReadOnlyProperty('a')
    >>> AB.b
    NamedReadOnlyProperty('b')
'''
    @classmethod
    def __init_subclass__(cls, *, ordered_attr_name_seq, **kwargs):
        ordered_attr_name_seq = tuple(ordered_attr_name_seq)
        cls.ordered_attr_name_seq = ordered_attr_name_seq
        cls.ordered_attr_name_set = frozenset(ordered_attr_name_seq)

        for name in ordered_attr_name_seq:
            setattr(cls, name, NamedReadOnlyProperty(name))

        super().__init_subclass__(**kwargs)


    def __init__(self, **kwargs):
        cls = type(self)
        for name in cls.ordered_attr_name_seq:
            self.__dict__[name] = kwargs.pop(name)
        super().__init__(**kwargs)

    def __dir__(self):
        return cls.ordered_attr_name_seq
    def __setattr__(self, attr, obj):
        raise AttributeError(attr)
    def __delattr__(self, attr):
        raise AttributeError(attr)

    def __repr__(self):
        cls = type(self)
        d = self.__dict__
        keys = cls.ordered_attr_name_seq
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


