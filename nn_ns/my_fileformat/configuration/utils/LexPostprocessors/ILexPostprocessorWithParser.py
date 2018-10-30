
__all__ = '''
    ILexPostprocessorWithParser
    '''.split()

from .abc import abstractmethod, ABC, final
from .ILexPostprocessor import ILexPostprocessor


class ILexPostprocessorWithParser(ILexPostprocessor):
    @abstractmethod
    def parse_terminals(self, terminals):
        # Iter Terminal -> parse_result
        raise NotImplementedError
    @final
    def parse_raw_tokens(self, raw_tokens):
        # Iter RawToken -> parse_result
        return self.parse_terminals(self.lex_postprocess_filter(raw_tokens))
    @final
    def parse_source_string(self, source_string):
        # String -> parse_result
        return self.parse_raw_tokens(self.raw_tokenize(source_string))



