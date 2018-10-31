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
    ,let_be_all_staticmethods
    ,useful_regex_patterns_decorator

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
_grammar_XOTs_parse_result = [('Inline_Path', 'Inline_Path_OP_Items1', 'Inline_NonPathObject'), ('Inline_ListItems1', 'Inline_ListItem_OPs0', 'Inline_Object'), ('Inline_DictItems1', 'Inline_DictItem_OPs0', 'Inline_DictItem')]




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
@let_be_all_staticmethods('t_')
class T:
    states = []
    tokens = tokens_only + commons
    terminals = terminals_only + commons
    def t_error(t):
        raise lex_error_handle(t, '')
    @useful_regex_patterns_decorator
    def t_ignores1(t):
        r'{non_indent_spaces1}'
        # not_at_line_begin
    @useful_regex_patterns_decorator
    def t_spaces1_line(t):
        r'{spaces1_line}'
        # at_line_begin, at_line_end
        # discard
    def t_newline(t):
        r'\n+'
        t.lexer.lineno += 1
        # discard

    @useful_regex_patterns_decorator
    def t_def_name(t):
        r'{at_line_begin}\w+'
        # at_line_begin
        return t
    @useful_regex_patterns_decorator
    def t_ref_name(t):
        r'{not_at_line_begin}\w+'
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

@let_be_all_staticmethods('p_')
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
    from ._main import _main
    _main(__name__)

