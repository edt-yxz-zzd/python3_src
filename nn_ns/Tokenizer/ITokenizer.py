
__all__ = '''
    ITokenizer
    TokenizerBaseError
        TokenizerFailError
    '''.split()

from .abc import ABC, abstractmethod
class TokenizerBaseError(Exception):pass
class TokenizerFailError(TokenizerBaseError):pass

class ITokenizer(ABC):
    __slots__ = ()
    @abstractmethod
    def iter_tokens(self, source, begin, end):
        # -> Iter token | raise TokenizerBaseError
        raise NotImplementedError

