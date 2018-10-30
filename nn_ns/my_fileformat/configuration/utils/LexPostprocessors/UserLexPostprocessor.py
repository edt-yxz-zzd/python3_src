
__all__ = '''
    UserLexPostprocessor
    '''.split()

from .abc import override
from .ILexPostprocessor import ILexPostprocessor


class UserLexPostprocessor(ILexPostprocessor):
    def __init__(self, lex_postprocessor:ILexPostprocessor):
        assert isinstance(lex_postprocessor, ILexPostprocessor)
        self.lex_postprocessor = lex_postprocessor

    @override
    def lex_postprocess_filter(self, raw_tokens):
        # Iter RawToken -> Iter Terminal
        # or [RawToken] -> Iter Terminal
        return self.lex_postprocessor.lex_postprocess_filter(raw_tokens)
    @override
    def iter_raw_tokenize(self, source_string:str):
        # str -> Iter RawToken
        return self.lex_postprocessor.iter_raw_tokenize(source_string)



