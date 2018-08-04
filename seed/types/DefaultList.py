
__all__ = '''
    DefaultList
    '''.split()
from collections import UserList
from .UserList import UserList

class DefaultList(UserList):
    def __init__(self, factory, initlist=None, *, copy=True):
        self.DefaultList__init__(factory)
        self.UserList__init__(initlist, copy=copy)
    def DefaultList__init__(self, factory):
        if factory is None:
            factory = lambda: None
        elif not callable(factory): raise TypeError
        self.factory = factory
    def __get_list(self, i):
        # return ls # len > i
        L = len(self)
        if L <= i:
            f = self.factory
            self.extend(f() for _ in range(i-L+1))
            assert len(self) == i+1
        return self.data
    def __getitem__(self, i):
        return self.__get_list(i)[i]
    def __setitem__(self, i, obj):
        self.__get_list(i)[i] = obj
        return

