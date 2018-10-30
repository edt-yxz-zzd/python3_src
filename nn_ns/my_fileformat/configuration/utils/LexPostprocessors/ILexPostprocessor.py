
__all__ = '''
    ILexPostprocessor
    '''.split()

from ..Lexers.EchoLexer import EchoLexer
from ..Lexers.FilterLexer import FilterLexer
from ..Lexers.TwoStageLexer import TwoStageLexer
from .abc import abstractmethod, ABC, final

class ILexPostprocessor(ABC):
    @abstractmethod
    def iter_raw_tokenize(self, source_string):
        # str -> Iter RawToken
        raise NotImplementedError
    @abstractmethod
    def lex_postprocess_filter(self, raw_tokens):
        # Iter RawToken -> Iter Terminal
        # or [RawToken] -> Iter Terminal
        raise NotImplementedError

    @final
    def iter_tokenize(self, source_string:str):
        # str -> Iter Terminal
        raw_tokens = self.iter_raw_tokenize(source_string)
        terminals = self.lex_postprocess_filter(raw_tokens)
        return terminals
    @final
    def raw_tokenize(self, source_string:str):
        # str -> [RawToken]
        return list(self.iter_raw_tokenize(source_string))
    @final
    def tokenize(self, source_string:str):
        # str -> [Terminal]
        return list(self.iter_tokenize(source_string))

    @final
    def make_terminal_lexer(self):
        # for terminals
        return EchoLexer()
    @final
    def make_raw_token_lexer(self):
        # for raw_tokens
        return FilterLexer(self.lex_postprocess_filter)
    @final
    def make_source_lexer(self):
        # for string
        return TwoStageLexer(
                self.iter_raw_tokenize, self.lex_postprocess_filter)

