
from collections.abc import Set
from sand import repr_helper


class DisabledMethodError(NotImplementedError):pass
class DisabledMutableMethodError(DisabledMethodError):pass
class DisabledSetMutableMethodError(DisabledMutableMethodError):pass
class DisableSetMutableMethod:
    def update(self, *others):
        raise DisabledSetMutableMethodError
    def __ior__(self, other):
        raise DisabledSetMutableMethodError
    def intersection_update(self, *others):
        raise DisabledSetMutableMethodError
    def __iand__(self, other):
        raise DisabledSetMutableMethodError
    def difference_update(self, *others):
        raise DisabledSetMutableMethodError
    def __isub__(self, other):
        raise DisabledSetMutableMethodError
    def symmetric_difference_update(self, *others):
        raise DisabledSetMutableMethodError
    def __ixor__(self, other):
        raise DisabledSetMutableMethodError
    def add(self, elem):
        raise DisabledSetMutableMethodError
    def remove(self, elem):
        raise DisabledSetMutableMethodError
    def discard(self, elem):
        raise DisabledSetMutableMethodError
    def pop(self):
        raise DisabledSetMutableMethodError
    def clear(self):
        raise DisabledSetMutableMethodError


class SetView(Set):
    def __init__(self, s):
        if not isinstance(s, Set):
            raise TypeError('not isinstance(s, Set)')
        if isinstance(s, SetView):
            s = s.__set
        self.__set = s
    @classmethod
    def from_iterable(cls, iterable):
        return cls(frozenset(iterable))
    def __repr__(self):
        return repr_helper(self, self.__set)
    
    def copy(self):
        return type(self)(self.__set)
    def __contains__(self, elem):
        return elem in self.__set
    def __iter__(self):
        return iter(self.__set)
    def __len__(self):
        return len(self.__set)
    def __le__(self, other):
        if isinstance(other, SetView):
            return self.__set <= other.__set
        elif isinstance(other, Set):
            return self.__set <= other
        return NotImplemented


