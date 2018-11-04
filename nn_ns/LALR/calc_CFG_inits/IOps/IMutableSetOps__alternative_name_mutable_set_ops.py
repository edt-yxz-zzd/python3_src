from .abc import ABC, abstractmethod
class IMutableSetOps__alternative_name_mutable_set_ops(ABC):
    @abstractmethod
    def static_make_empty_set(ops):
        pass
    @abstractmethod
    def add(ops, self, element):
        pass
    def static_from_iterable(ops, iterable):
        self = ops.static_make_empty_set()
        for x in iterable:
            ops.add(self, x)
        return self
