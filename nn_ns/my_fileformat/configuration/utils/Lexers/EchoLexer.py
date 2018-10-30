__all__ = '''
    EchoLexer
    '''.split()

from .abc import override
from .IFilterLexer import IFilterLexer
class EchoLexer(IFilterLexer):
    '''lexer over terminals # not over string

EchoLexer vs ply.lex.Lexer
    ply.lex.Lexer :: [Char] -> [ply.lex.LexToken]
    EchoLexer :: [a] -> [a]
why?
    to add "lex_postprocess_filter"
    lex_postprocess_filter :: Iter raw_token -> Iter terminal
usage:
    source_string = ??? # str
    XXX_lex_module = ??? # XXX.tokens/states/t_*
    XXX_yacc_module = ??? # XXX.tokens/start/p_*
    XXX_lex_kwargs = ???
    XXX_yacc_kwargs = ???
    lex_postprocess_filter = ??? # Iter raw_token -> Iter terminal

    raw_lexer = ply.lex.lex(module=XXX_lex_module, **XXX_lex_kwargs)
    raw_lexer.input(source_string)
    raw_tokens = iter(raw_lexer)
    terminals = lex_postprocess_filter(raw_tokens)

    lrparser = ply.yacc.yacc(module=XXX_yacc_module, **XXX_yacc_kwargs)
    terminal_lexer = EchoLexer()
    result = lrparser.parse(terminals, lexer=terminal_lexer)

    #why not "result = lrparser.parse(source_string, lexer=raw_lexer)"?
    #   to add "lex_postprocess_filter"
'''
    @override
    def __filter__(__self, __terminals):
        return iter(__terminals)



