
'''
diff std UserList at:
    using a method as constructor instead of __init__
    so, DefaultList can be subclass of it
'''


__all__ = '''
    UserList
    '''.split()
#from collections import UserList
from collections.abc import MutableSequence

class UserList(MutableSequence):
    """A more or less complete user-defined wrapper around list objects."""
    def __init__(self, initlist=None, *, copy=True):
        self.UserList__init__(initlist, copy=copy)

    def mkUserList(self, initlist=None):
        # not classmethod!!!!!!!!!!!
        #   so, not named as "from_iterable"
        #   subclass should override this if __init__ api changed
        return mkUserList(initlist)
    def UserList__init__(self, initlist=None, *, copy=True):
        if not copy:
            if initlist is None: raise TypeError
            if not isinstance(initlist, MutableSequence): raise TypeError
            self.data = initlist
            return

        self.data = []
        if initlist is not None:
            # XXX should this accept an arbitrary sequence?
            if type(initlist) == type(self.data):
                self.data[:] = initlist
            elif isinstance(initlist, UserList):
                self.data[:] = initlist.data[:]
            else:
                self.data = list(initlist)
    def __repr__(self): return repr(self.data)
    def __lt__(self, other): return self.data <  self.__cast(other)
    def __le__(self, other): return self.data <= self.__cast(other)
    def __eq__(self, other): return self.data == self.__cast(other)
    def __gt__(self, other): return self.data >  self.__cast(other)
    def __ge__(self, other): return self.data >= self.__cast(other)
    def __cast(self, other):
        return other.data if isinstance(other, UserList) else other
    def __contains__(self, item): return item in self.data
    def __len__(self): return len(self.data)
    def __getitem__(self, i): return self.data[i]
    def __setitem__(self, i, item): self.data[i] = item
    def __delitem__(self, i): del self.data[i]
    def __add__(self, other):
        if isinstance(other, UserList):
            return self.mkUserList(self.data + other.data)
        elif isinstance(other, type(self.data)):
            return self.mkUserList(self.data + other)
        return self.mkUserList(self.data + list(other))
    def __radd__(self, other):
        if isinstance(other, UserList):
            return self.mkUserList(other.data + self.data)
        elif isinstance(other, type(self.data)):
            return self.mkUserList(other + self.data)
        return self.mkUserList(list(other) + self.data)
    def __iadd__(self, other):
        if isinstance(other, UserList):
            self.data += other.data
        elif isinstance(other, type(self.data)):
            self.data += other
        else:
            self.data += list(other)
        return self
    def __mul__(self, n):
        return self.mkUserList(self.data*n)
    __rmul__ = __mul__
    def __imul__(self, n):
        self.data *= n
        return self
    def append(self, item): self.data.append(item)
    def insert(self, i, item): self.data.insert(i, item)
    def pop(self, i=-1): return self.data.pop(i)
    def remove(self, item): self.data.remove(item)
    def clear(self): self.data.clear()
    def copy(self): return self.mkUserList(self)
    def count(self, item): return self.data.count(item)
    def index(self, item, *args): return self.data.index(item, *args)
    def reverse(self): self.data.reverse()
    def sort(self, *args, **kwds): self.data.sort(*args, **kwds)
    def extend(self, other):
        if isinstance(other, UserList):
            self.data.extend(other.data)
        else:
            self.data.extend(other)



