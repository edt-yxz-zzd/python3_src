

__all__ = '''
    LexPostprocessor
    '''.split()


from ..make_pseudo_lex_module_obj import make_pseudo_lex_module_obj
from .LexPostprocessorWithParser import LexPostprocessorWithParser

from .ILexPostprocessor import ILexPostprocessor
from .abc import override

from seed.tiny import echo
import ply.lex


class LexPostprocessor(ILexPostprocessor):
    '''String -> [RawToken/Terminal]

see: .Lexers.EchoLexer
usage:
    ##################### construct
    XXX_lex_module = ???
    XXX_lex_kwargs = ??? or {}

    import re
    post = LexPostprocessor(
            XXX_lex_module
            , regex_flags=re.MULTILINE|re.VERBOSE
            , START_STATE='INITIAL'
            , lex_postprocess_filter=???
            )

    ##################### tokenize
    source_string = ???
    terminals = post.tokenize(source_string)
    raw_tokens = post.raw_tokenize(source_string)

    iter_terminals = post.iter_tokenize(source_string)
    iter_raw_tokens = post.iter_raw_tokenize(source_string)

    ##################### parse
    XXX_yacc_module = ???
    XXX_yacc_kwargs = ???

    import ply.yacc
    lrparser = ply.yacc.yacc(module=XXX_yacc_module, **XXX_yacc_kwargs)
    result = lrparser.parse(source_string, lexer=post.make_source_lexer())
    result = lrparser.parse(raw_tokens, lexer=post.make_raw_token_lexer())
    result = lrparser.parse(terminals, lexer=post.make_terminal_lexer())
'''
    def __init__(self
        , XXX_lex__module_or_class_or_dict
        , XXX_lex_kwargs = {}
        , *
        , regex_flags
        , START_STATE : str
        , lex_postprocess_filter
        ):
        r'''

inputs:
    XXX_lex__module_or_class_or_dict
        hasattrs or keys:
            .t_*
            .tokens
            .states
            .__file__

    lex_postprocess_filter
        :: 'echo' | ... | Iter RawToken -> Iter Terminal
        :: 'echo' | ... | Iter ply.lex.LexToken -> Iter Terminal
        if 'echo':
            lex_postprocess_filter = echo
        if ...:
            lex_postprocess_filter = getattr(XXX_pseudo_lex_module, 'lex_postprocess_filter')

    regex_flags
        #where: re.compile(..., reflags=regex_flags)
        if ...:
            regex_flags = getattr(XXX_pseudo_lex_module, 'regex_flags')

    START_STATE :: None | 0 | ... | str
        if None:
            START_STATE = getattr(XXX_pseudo_lex_module, 'START_STATE', 'INITIAL')
        if 0:
            START_STATE = 'INITIAL'
        if ...:
            START_STATE = getattr(XXX_pseudo_lex_module, 'START_STATE')
'''
        x = XXX_lex__module_or_class_or_dict
        XXX_pseudo_lex_module = make_pseudo_lex_module_obj(x)


        if START_STATE is None:
            START_STATE = getattr(XXX_pseudo_lex_module, 'START_STATE', 'INITIAL')
        elif START_STATE is ...:
            START_STATE = getattr(XXX_pseudo_lex_module, 'START_STATE')
        elif START_STATE == 0:
            START_STATE = 'INITIAL'

        if regex_flags is ...:
            regex_flags = getattr(XXX_pseudo_lex_module, 'regex_flags')

        if lex_postprocess_filter == 'echo':
            lex_postprocess_filter = echo
        elif lex_postprocess_filter is ...:
            lex_postprocess_filter = getattr(XXX_pseudo_lex_module, 'lex_postprocess_filter')


        if type(START_STATE) is not str: raise TypeError
        if not callable(lex_postprocess_filter): raise TypeError

        self.XXX_pseudo_lex_module = XXX_pseudo_lex_module
        self.XXX_lex_kwargs = XXX_lex_kwargs
        self.regex_flags = regex_flags
        self.START_STATE = START_STATE
        self.lex_postprocess_filter = lex_postprocess_filter
        self.raw_lexers = self.__iter_raw_lexers()

    def __iter_raw_lexers(self):
        # -> Iter raw_lexer
        raw_lexer = ply.lex.lex(
            module = self.XXX_pseudo_lex_module
            , reflags = self.regex_flags
            , **self.XXX_lex_kwargs
            )

        raw_lexer.begin(self.START_STATE)#NOTE!!!!
        raw_lexer.lineno = 1
        while True:
            yield raw_lexer.clone()

    @override
    def lex_postprocess_filter(self, raw_tokens):
        # Iter RawToken -> Iter Terminal
        # or [RawToken] -> Iter Terminal
        return self.lex_postprocess_filter(raw_tokens)

    @override
    def iter_raw_tokenize(self, source_string:str):
        # str -> Iter RawToken
        raw_lexer = next(self.raw_lexers, None)
        raw_lexer.input(source_string)
        yield from raw_lexer
        # why not return iter(raw_lexer)??
        #   since "raw_lexer is iter(raw_lexer)"
        #   output too many information


    def with_parser(self, lrparser):
        return LexPostprocessorWithParser(self, lrparser)
    def with_parser_from_args(self
        , XXX_yacc__module_or_class_or_dict
        , XXX_yacc_kwargs = {}
        ):
        return LexPostprocessorWithParser.from_yacc_module_kwargs(
            self
            , XXX_yacc__module_or_class_or_dict
            , XXX_yacc_kwargs
            )

