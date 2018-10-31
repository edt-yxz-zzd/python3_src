

__all__ = '''
    LexPostprocessorWithParser
    '''.split()
from ..make_yacc_LRParser import make_yacc_LRParser
from .ILexPostprocessorWithParser import ILexPostprocessorWithParser
from .UserLexPostprocessor import UserLexPostprocessor
from .abc import override

import ply.yacc



class LexPostprocessorWithParser(
    UserLexPostprocessor, ILexPostprocessorWithParser
    ):
    @classmethod
    def from_yacc_module_kwargs(cls
        , lex_postprocessor:ILexPostprocessorWithParser
        , XXX_yacc__module_or_class_or_dict
        , XXX_yacc_kwargs = {}
        ):
        r'''
see: LexPostprocessor for the input args
'''
        x = XXX_yacc__module_or_class_or_dict
        lrparser = make_yacc_LRParser(x, **XXX_yacc_kwargs)
        #self.XXX_pseudo_yacc_module = XXX_pseudo_yacc_module
        return cls(lex_postprocessor, lrparser)

    def __init__(self
        , lex_postprocessor:ILexPostprocessorWithParser
        , lrparser # ply.yacc.LRParser
        ):
        self.lrparser = lrparser
        super().__init__(lex_postprocessor)
    '''
    def parse_source_string(self, source_string):
        return lrparser.parse(source_string, lexer=self.make_source_lexer())
    def parse_raw_tokens(self, raw_tokens):
        return lrparser.parse(raw_tokens, lexer=self.make_raw_token_lexer())
    '''
    @override
    def parse_terminals(self, terminals):
        return self.lrparser.parse(
            terminals, lexer=self.make_terminal_lexer())

