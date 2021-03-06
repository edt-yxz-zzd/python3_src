"""
grammar_XOAs = '''
Inline_Path_OP_Items1 Inline_Path_OP_Items0 Inline_Path_OP_Item

Inline_ListItem_OPs1 Inline_ListItem_OPs0 Inline_ListItem_OP
Inline_DictItem_OPs1 Inline_DictItem_OPs0 Inline_DictItem_OP
'''



syntax of grammar_XOAs:
    no comments
    only single line; no multi-lines body
    allow empty lines
"""


__all__ = '''
    parse__grammar_XOAs
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



def _eval_grammar_XOAs():
    s = __doc__.split('\n'*3)[0]
    d = {}
    exec(s, d, d)
    return d['grammar_XOAs']
_grammar_XOAs = _eval_grammar_XOAs()
del _eval_grammar_XOAs
_grammar_XOAs_parse_result = [('Inline_Path_OP_Items1', 'Inline_Path_OP_Items0', 'Inline_Path_OP_Item'), ('Inline_ListItem_OPs1', 'Inline_ListItem_OPs0', 'Inline_ListItem_OP'), ('Inline_DictItem_OPs1', 'Inline_DictItem_OPs0', 'Inline_DictItem_OP')]




tokens_only = '''
    newline
    ignores1
    spaces1_line
    '''.split()
terminals_only = []
commons = '''
    name
    '''.split()
    #def_name
    #ref_name
    #OP_COLON
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

    def t_name(t):
        r'\w+'
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
parse_result__grammar_XOAs :: [(name, name, name)]
whole = [rule]
rule = (name, name, name)
=============
Main
    Rules0
        return list(Rules0)
Rule
    name name name
        return (name, name, name)
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
            'Rule : name name name'
            p[0] = p[1], p[2], p[3]
    _(make_rule_inject_to(locals())); del _

lex_postprocessor_with_parser = lex_postprocessor.with_parser_from_args(P)
parse__grammar_XOAs = lex_postprocessor_with_parser.parse_source_string



if __name__ == "__main__":
    from ._main import _main
    _main(__name__)

