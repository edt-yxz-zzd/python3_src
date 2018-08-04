
__all__ = ['SingleItemDict']

import collections

class SingleItemDict(collections.abc.MutableMapping):
    '''len(self) <= 1

example:
    >>> SingleItemDict()
    SingleItemDict()
    >>> SingleItemDict([(1,2), (3,4)])
    SingleItemDict({3: 4})
    >>> SingleItemDict({3:4})
    SingleItemDict({3: 4})
    >>> d = SingleItemDict(a=3, b=1)
    >>> d == SingleItemDict(a=3) or d == SingleItemDict(b=1)
    True
'''
    def __init__(self, mapping_or_iterable=(), **kwargs):
        self.__item = None
        super().__init__()

        if kwargs:
            self.update(kwargs)
        else:
            self.update(mapping_or_iterable)
    @property
    def __key(self):
        return self.__item[0]
    @property
    def __value(self):
        return self.__item[1]
    def __getitem__(self, key):
        if not self or\
           not self.__key == key:
            raise KeyError(key)
        return self.__value
    
            
    def __setitem__(self, key, value):
        self.__item = (key, value)
    def __delitem__(self, key):
        self.__item = None
    def __iter__(self):
        if self:
            yield self.__key
    def __len__(self):
        return int(self.__item is not None)

    def __repr__(self):
        cls_name = type(self).__name__
        if not self:
            return '{}()'.format(cls_name)
        return '{}({})'.format(cls_name, dict(self))
        
assert SingleItemDict() == SingleItemDict()
assert SingleItemDict([(1,2), (3,4)]) == SingleItemDict({3:4})
_d = SingleItemDict(a=3, b=1)
assert bool(_d == SingleItemDict(a=3)) != bool(_d == SingleItemDict(b=1))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
