__all__ = '''
    IFilterLexer
    '''.split()

from .abc import abstractmethod, ABC, final


class IFilterLexer(ABC):
    ''':: ([input_symbol] -> Iter terminal) -> lexer

ply.yacc.LRParser
    requires:
        lexer.input(input)
        lexer.token() -> None|token
        ??lexer.lineno
        ??lexer.lexpos
'''

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if cls.filter is not __class__.filter:
            raise Exception('should not override IFilterLexer.filter; override __filter__ instead')

    @abstractmethod
    def __filter__(__self, __input_symbols):
        # Iter input_symbol -> Iter terminal
        # or [input_symbol] -> Iter terminal
        raise NotImplementedError

    @final
    def filter(__self, __input_symbols):
        # Iter input_symbol -> Iter terminal
        # or [input_symbol] -> Iter terminal
        return iter(type(__self).__filter__(__self, __input_symbols))

    def __init__(__self):
        #__self.lineno = 1
        #__self.lexpos = 0
        __self.__iter_terminals = None

    @final
    def input(__self, __input_symbols):
        if __self.__iter_terminals is not None:
            raise NotImplementedError
        __self.__iter_terminals = __self.filter(__input_symbols)

    @final
    def token(__self):
        # -> None | terminal
        return next(__self.__iter_terminals, None)

