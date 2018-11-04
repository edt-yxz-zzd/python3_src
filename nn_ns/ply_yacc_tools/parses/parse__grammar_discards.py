"""
grammar_discards = '''
MaybeNullIndent : NullIndent | EMPTY
Ignores0 : Ignores1 | EMPTY

middle_open : OP_MIDDLE_OPEN Ignores0
middle_close : Ignores0 OP_MIDDLE_CLOSE
'''



syntax of grammar_discards:
    no comments
    only single line; no multi-lines body
    allow empty lines
"""


__all__ = '''
    parse__grammar_discards
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



def _eval_grammar_discards():
    s = __doc__.split('\n'*3)[0]
    d = {}
    exec(s, d, d)
    return d['grammar_discards']
_grammar_discards = _eval_grammar_discards()
del _eval_grammar_discards
_grammar_discards_parse_result = [('MaybeNullIndent', [['NullIndent'], ['EMPTY']]), ('Ignores0', [['Ignores1'], ['EMPTY']]), ('middle_open', [['OP_MIDDLE_OPEN', 'Ignores0']]), ('middle_close', [['Ignores0', 'OP_MIDDLE_CLOSE']])]




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
    OP_BAR
    '''.split()
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
    def t_OP_BAR(t):
        r'[|]'
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
parse_result__grammar_discards :: [(def_name, [[ref_name]])]
whole = [rule]
rule = (def_name, [alter])
alter = [ref_name]
=============
Main
    Rules0
        return list(Rules0)
Rule
    def_name OP_EQ RefNames1s1
        return def_name, list(RefNames1s1)
RefNames1_Bar = +unRefNames1 OP_BAR
unRefNames1
    RefNames1
        return list(RefNames1)
################ XOA
Rules1 Rules0 Rule
RefNames1_Bars1 RefNames1_Bars0 RefNames1_Bar
RefNames1 RefNames0 ref_name
################ XOT
RefNames1s1 RefNames1_Bars0 unRefNames1

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
        RefNames1_Bars1 RefNames1_Bars0 RefNames1_Bar
        RefNames1 RefNames0 ref_name
        '''
        )
    make_rule_action_for_all_many1_XOTs_iappendright(
        locals()
        , 'RefNames1s1 RefNames1_Bars0 unRefNames1'
        )

    def _(inject_to):
        @inject_to
        def p_(p):
            'Main : Rules0'
            p[0] = list(p[1])

        @inject_to
        def p_(p):
            'Rule : def_name OP_COLON RefNames1s1'
            p[0] = p[1], list(p[3])
        @inject_to
        def p_(p):
            'RefNames1_Bar : unRefNames1 OP_BAR'
            p[0] = p[1]
        @inject_to
        def p_(p):
            'unRefNames1 : RefNames1'
            p[0] = list(p[1])
    _(make_rule_inject_to(locals())); del _

lex_postprocessor_with_parser = lex_postprocessor.with_parser_from_args(P)
parse__grammar_discards = lex_postprocessor_with_parser.parse_source_string



if __name__ == "__main__":
    from ._main import _main
    _main(__name__)

