
__all__ = '''
    NearlyCompleteMutableStack
    '''.split()


from .INearlyCompleteMutableStack import INearlyCompleteMutableStack
from .EmptyError import EmptyError
from .abc import override

class NearlyCompleteMutableStack(INearlyCompleteMutableStack):
    def __init__(self, size=0):
        assert size >= 0
        self.__size = size

    @override
    def is_empty(self):
        return not self.__size
    @override
    def push(self, obj):
        self.__size += 1
    @override
    def pop_None(self):
        if self.is_empty(): raise EmptyError
        self.__size -= 1


