
__all__ = '''
    UserLexPostprocessorWithParser
    '''.split()

from .abc import override
from .ILexPostprocessorWithParser import ILexPostprocessorWithParser
from .UserLexPostprocessor import UserLexPostprocessor



class UserLexPostprocessorWithParser(
    UserLexPostprocessor, ILexPostprocessorWithParser
    ):
    def __init__(self, lex_postprocessor:ILexPostprocessorWithParser):
        assert isinstance(lex_postprocessor, ILexPostprocessorWithParser)
        super().__init__(lex_postprocessor)
    @override
    def parse_terminals(self, terminals):
        # Iter Terminal -> parse_result
        return self.lex_postprocessor.parse_terminals(terminals)



