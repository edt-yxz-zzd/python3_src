
__all__ = '''
    SeqAsCompleteMutableStack
    '''.split()

from .ICompleteMutableStack import ICompleteMutableStack
from .EmptyError import EmptyError
from .abc import override


class SeqAsCompleteMutableStack(ICompleteMutableStack):
    def __init__(self, underlying_seq):
        self.underlying_seq = underlying_seq
    @override
    def is_empty(self):
        return not self.underlying_seq
    @override
    def get_top(self):
        try:
            return self.underlying_seq[-1]
        except:
            raise EmptyError
    @override
    def push(self, obj):
        self.underlying_seq.append(obj)
    @override
    def pop(self):
        try:
            return self.underlying_seq.pop()
        except:
            raise EmptyError


