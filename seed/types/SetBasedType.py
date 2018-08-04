

__all__ = '''
    SetBasedType
    TypesAsSet
'''.split()


from abc import abstractmethod, ABCMeta
import functools # for total_ordering

@functools.total_ordering
class SetBasedType(metaclass = ABCMeta):
    r'conceptually, there is a underlying set which contains of all instances of a type'
    @abstractmethod
    def __contains__(self, obj):
        raise NotImplementedError

    @abstractmethod
    def __le__(self, other):
        raise NotImplementedError


    def __eq__(self, other):
        return self <= other and other <= self
    def issubset(self, other):
        return self <= other

    def issubclass(self, other):
        return self <= other
    def hasinstance(self, obj):
        return obj in self
    


class TypesAsSet(SetBasedType):
    def __init__(self, types):
        # TODO: eliminate super class ??
        self.types = tuple(sorted(set(types)))

    def __contains__(self, obj):
        return isinstance(obj, self.types)

    def __le__(self, other):
        return all(issubclass(t, other.types) for t in self.types)
    








