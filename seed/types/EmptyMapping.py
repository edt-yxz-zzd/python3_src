
'''
>>> vars(empty_mapping) #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
TypeError
>>> empty_mapping.__dict__ #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
AttributeError
>>> empty_mapping['a']
Traceback (most recent call last):
    ...
KeyError
>>> len(empty_mapping)
0
>>> list(empty_mapping)
[]
>>> list(empty_mapping.keys())
[]
>>> list(empty_mapping.values())
[]
>>> list(empty_mapping.items())
[]


>>> 1 in empty_mapping
False
>>> bool(empty_mapping)
False
'''

__all__ = '''
    EmptyMapping
    empty_mapping
    empty_set
    empty_tuple
    empty_iterator
    '''.split()

from collections.abc import Mapping
from types import MappingProxyType

class EmptyMapping(Mapping):
    __slots__ = ()
    def __new__(cls):
        global empty_mapping
        try:
            return empty_mapping
        except NameError:
            empty_mapping = super(cls, __class__).__new__(cls)
        return empty_mapping

    """
    def __getattribute__(self, attr):
        if attr == '__dict__':
            return empty_mapping
        return super().__getattribute__(attr)
    """
    def __getitem__(self, key):
        raise KeyError
    def __iter__(self):
        return empty_iterator
    def __len__(self):
        return 0
    def __setattr__(self, attr, obj):
        raise AttributeError
    def __delattr__(self, attr):
        raise AttributeError
    def __eq__(self, other):
        return type(self) is type(other)
    def __hash__(self):
        return id(type(self))

    def __bool__(self):
        return False
    def __contains__(self, key):
        return False
empty_mapping = EmptyMapping()
empty_set = frozenset()
empty_tuple = ()
empty_iterator = iter('')


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


