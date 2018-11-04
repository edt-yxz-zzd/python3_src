__all__ = '''
    FilterLexer
    '''.split()
from .IFilterLexer import IFilterLexer
from .abc import override

class FilterLexer(IFilterLexer):
    # [input_symbol] -> Iter Terminal
    def __init__(__self, __filter):
        if not callable(__filter): raise TypeError
        __self.__filter = __filter
        super().__init__()
    @override
    def __filter__(__self, __input_symbols):
        return __self.__filter(__input_symbols)


