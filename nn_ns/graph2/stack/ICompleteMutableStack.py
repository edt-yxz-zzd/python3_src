
__all__ = '''
    IMutableStack
    INearlyCompleteMutableStack
    ICompleteMutableStack
    '''.split()


from .abc import ABC, abstractmethod, override, final

class IMutableStack(ABC):
    pass
class INearlyCompleteMutableStack(IMutableStack):
    @abstractmethod
    def is_empty(self):
        # -> bool
        pass
    @abstractmethod
    def push(self, obj):
        # -> None
        pass

    @abstractmethod
    def pop_None(self):
        # -> None or raise
        if not self.is_empty(): raise EmptyError
        pass
class ICompleteMutableStack(INearlyCompleteMutableStack):
    @abstractmethod
    def get_top(self):
        # -> element or raise
        if not self.is_empty(): raise EmptyError
        pass
    @abstractmethod
    def pop(self):
        # -> element or raise
        if not self.is_empty(): raise EmptyError
        pass
    @final
    @override
    def pop_None(self):
        self.pop()

