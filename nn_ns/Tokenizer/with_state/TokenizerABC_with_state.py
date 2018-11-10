
__all__ = '''
    TokenizerABC_with_state
    '''.split()

from ..ITokenizer import ITokenizer
from .abc import abstractmethod, override, final
class TokenizerABC_with_state(ITokenizer):
    __slots__ = ()
    @abstractmethod
    def get_initial_state(self):
        raise NotImplementedError
    @abstractmethod
    def iter_tokens_ex(self, state, source, begin, end):
        # -> Iter token | raise TokenizerBaseError
        raise NotImplementedError
    @final
    @override
    def iter_tokens(self, source, begin, end):
        return self.iter_tokens_ex(self.get_initial_state(), source, begin, end)


