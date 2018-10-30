__all__ = '''
    MultiStageLexer
    '''.split()
from .IFilterLexer import IFilterLexer
from .abc import override

def to_filter(__obj):
    if isinstance(__obj, IFilterLexer):
        f = __obj.filter
    elif callable(__obj):
        f = __obj
    else:
        raise TypeError('should be IFilterLexer or callable')
    return f

class MultiStageLexer(IFilterLexer):
    # from left to right
    def __init__(__self, __filters):
        __self.__filters = (*map(to_filter, __filters), )
        super().__init__()
    @override
    def __filter__(__self, __input_symbols):
        it = __input_symbols
        for f in __self.__filters:
            it = f(it)
        return it


