
__all__ = '''
    LeftBiasedListAsAsCompleteMutableStack
    '''.split()

from .ICompleteMutableStack import ICompleteMutableStack
from .EmptyError import EmptyError
from .abc import override


class LeftBiasedListAsAsCompleteMutableStack(ICompleteMutableStack):
    # left_biased_list a = () | (left_biased_list a, a)
    def __init__(self, left_biased_list=()):
        assert len(left_biased_list) in (0,2)
        self.underlying_left_biased_list = left_biased_list

    @override
    def is_empty(self):
        return not self.underlying_left_biased_list
    @override
    def get_top(self):
        try:
            return self.underlying_left_biased_list[-1]
        except:
            raise EmptyError
    @override
    def push(self, obj):
        self.underlying_left_biased_list = (self.underlying_left_biased_list, obj)
    @override
    def pop(self):
        try:
            underlying_left_biased_list, obj = self.underlying_left_biased_list
        except:
            raise EmptyError
        self.underlying_left_biased_list = underlying_left_biased_list
        return obj




