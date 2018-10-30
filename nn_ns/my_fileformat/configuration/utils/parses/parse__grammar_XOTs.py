"""
grammar_XOTs = '''
Inline_Path : Inline_Path_OP_Items1 Inline_NonPathObject

Inline_ListItems1 : Inline_ListItem_OPs0 Inline_Object
Inline_DictItems1 : Inline_DictItem_OPs0 Inline_DictItem
'''



syntax of grammar_XOTs:
    no comments
    only single line; no multi-lines body
    allow empty lines
"""


__all__ = '''
    parse__grammar_XOTs
    '''.split()

from .imports import (
    LexPostprocessor
    ,lex_error_handle
    , token_error_handle
    ,let_be_all_staticmethod

    ,make_rule_inject_to
    ,make_rule_action_for_all_many01_XOAs_iappendright
    ,make_rule_action_for_all_many1_XOTs_iappendright
    )


import re

regex_flags = re.MULTILINE|re.VERBOSE



def _eval_grammar_XOTs():
    s = __doc__.split('\n'*3)[0]
    d = {}
    exec(s, d, d)
    return d['grammar_XOTs']
_grammar_XOTs = _eval_grammar_XOTs()
del _eval_grammar_XOTs




inline_space = r'((?!\n)\s)'
not_at_line_begin = r'(?<=[^\n])'
at_line_begin = r'(?<![^\n])'
not_at_line_end = r'(?=[^\n])'
at_line_end = r'(?![^\n])'

tokens_only = '''
    newline
    ignores1
    spaces1_line
    '''.split()
terminals_only = []
commons = '''
    def_name
    ref_name
    OP_COLON
    '''.split()
    #OP_BAR
@let_be_all_staticmethod('t_')
class T:
    states = []
    tokens = tokens_only + commons
    terminals = terminals_only + commons
    def t_error(t):
        raise lex_error_handle(t, '')
    def t_ignores1(t):
        r'(?<=[^\n])((?!\n)\s)+'
        # not_at_line_begin
    def t_spaces1_line(t):
        r'(?<![^\n])((?!\n)\s)+(?![^\n])'
        # at_line_begin, at_line_end
        # discard
    def t_newline(t):
        r'\n+'
        t.lexer.lineno += 1
        # discard

    def t_def_name(t):
        r'(?<![^\n])\w+'
        # at_line_begin
        return t

    def t_ref_name(t):
        r'(?<=[^\n])\w+'
        # not_at_line_begin
        return t

    def t_OP_COLON(t):
        r':'
        return t

T.regex_flags = regex_flags

lex_postprocessor = LexPostprocessor(
            T
            , regex_flags=...
            , START_STATE=None
            , lex_postprocess_filter='echo'
            )

#######################################################

@let_be_all_staticmethod('p_')
class P:
    '''
Main
    Rules0
        return list(Rules0)
Rule
    def_name OP_COLON ref_name ref_name
        return (def_name, ref_name, ref_name)
################ XOA
Rules1 Rules0 Rule

Empty_iappendright
'''
    tokens = T.terminals
    start = 'Main'

    def p_error(t):
        raise Exception(t)
    make_rule_action_for_all_many01_XOAs_iappendright(
        locals()
        , 'Empty_iappendright'
        , '''
        Rules1 Rules0 Rule
        '''
        )
    make_rule_action_for_all_many1_XOTs_iappendright(
        locals()
        , ''
        )

    def _(inject_to):
        @inject_to
        def p_(p):
            'Main : Rules0'
            p[0] = list(p[1])

        @inject_to
        def p_(p):
            'Rule : def_name OP_COLON ref_name ref_name'
            'Rule : name name name'
            p[0] = p[1], p[3], p[4]
    _(make_rule_inject_to(locals())); del _

lex_postprocessor_with_parser = lex_postprocessor.with_parser_from_args(P)
parse__grammar_XOTs = lex_postprocessor_with_parser.parse_source_string



if __name__ == "__main__":
    for t in lex_postprocessor.tokenize(_grammar_XOTs):
        print(t)
        del t
    print()
    print()
    print(parse__grammar_XOTs(_grammar_XOTs))

    from .example__grammar_XOTs import grammar_XOTs
    print(parse__grammar_XOTs(grammar_XOTs))

