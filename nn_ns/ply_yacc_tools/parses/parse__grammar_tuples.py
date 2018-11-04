"""
grammar_tuples = '''
a
    | b | c d | b c d
    | +b | +c +d | +b +c +d
e
    | -b | -c -d | -b -c -d
    | b | +c -d | -b +c -d
'''

syntax of grammar_tuples:
    ref_name may be qualified by '+'/'-'
    no comments
    no colon # use eq instead
    allow empty lines

"""

__all__ = '''
    parse__grammar_tuples
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
    ,make_rule_action_for_all_units
    ,make_rule_action_for_all_tuples
    )
from itertools import chain
import re

regex_flags = re.MULTILINE|re.VERBOSE



def _eval_grammar_tuples():
    s = __doc__.split('\n\n')[0]
    d = {}
    exec(s, d, d)
    return d['grammar_tuples']
_grammar_tuples = _eval_grammar_tuples()
del _eval_grammar_tuples
_grammar_tuples_parse_result = [('WholeFile', [(1, ['MaybeNullIndent', 'TheMainObject'])]), ('TheMainObject', [0, ['Object'], (2, ['OP_UNINDENT_DictHead', 'NullIndent', 'DictBody']), (2, ['OP_UNINDENT_ObjectArrayHead', 'NullIndent', 'ObjectArrayBody']), (2, ['OP_UNINDENT_ObjectTupleHead', 'NullIndent', 'ObjectTupleBody']), (2, ['OP_UNINDENT_CharStringHead', 'NullIndent', 'CharStringBody']), (2, ['OP_UNINDENT_ByteStringHead', 'NullIndent', 'ByteStringBody'])]), ('Object', [(0, ['Inline_Object']), (0, ['MultiLine_Object'])])]



tokens_only = '''
    newline
    ignores1
    spaces1_line
    '''.split()
terminals_only = []
commons = '''
    def_name
    ref_name
    ref_xname
    indent
    OP_EQ
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
    def t_ref_xname(t):
        r'{not_at_line_begin}[+-]\w+'
        # not_at_line_begin
        return t
    @useful_regex_patterns_decorator
    def t_ref_name(t):
        r'{not_at_line_begin}\w+'
        # not_at_line_begin
        return t
    @useful_regex_patterns_decorator
    def t_indent(t):
        r'{at_line_begin}[ ]{{4}}{not_at_line_end}'
        # at_line_begin
        return t
    def t_OP_EQ(t):
        r'='
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
parse_result__grammar_tuples :: [(def_name, [(may_bool, ref_name)])]
whole = [rule]
rule = (def_name, [alter])
alter = [(may_bool, ref_name)]
=============
Rule
    def_name OP_EQ TRefNames0s0
        return def_name, TRefNames0s0
    def_name indent OP_EQ TRefNames0s0 itIndentBarLines0
        return def_name, list(chain(TRefNames0s0, *itIndentBarLines0))
TRefNames0s0
    TRefNames0s1
        return TRefNames0s1
    <>
        return []
TRefName
    ref_name
        return None, ref_name
    ref_xname
        op, ref_name = ref_xname[0], ref_xname[1:]
        return op=='+', ref_name

################ unit
Main = itRules0 --list
TRefNames0s1 = itTRefNames0s1 --list
TRefNames0 = itTRefNames0 --list
IndentBarLines0 = itIndentBarLines0 --list
TRefNames0s0_Bar = +TRefNames0s0 OP_BAR
IndentBarLine = indent OP_BAR +TRefNames0s0
################ XOA
itRules1 itRules0 Rule
itTRefNames0s0_Bars1 itTRefNames0s0_Bars0 TRefNames0s0_Bar
itTRefNames1 itTRefNames0 TRefName
itIndentBarLines1 itIndentBarLines0 IndentBarLine
################ XOT
itTRefNames0s1 : itTRefNames0s0_Bars0 TRefNames0

Empty_iappendright
'''
    tokens = T.terminals
    start = 'Main'

    def p_error(t):
        raise Exception(t)
    make_rule_action_for_all_units(
        locals()
        , '''
            Main = itRules0
            TRefNames0s1 = itTRefNames0s1
            TRefNames0 = itTRefNames0
            IndentBarLines0 = itIndentBarLines0
            '''
        , transform=list
        )
    make_rule_action_for_all_units(
        locals()
        , '''
            TRefNames0s0_Bar = +TRefNames0s0 OP_BAR
            IndentBarLine = indent OP_BAR +TRefNames0s0
            '''
        , transform=list
        )
    make_rule_action_for_all_many01_XOAs_iappendright(
        locals()
        , 'Empty_iappendright'
        , '''
            itRules1 itRules0 Rule
            itTRefNames0s0_Bars1 itTRefNames0s0_Bars0 TRefNames0s0_Bar
            itTRefNames1 itTRefNames0 TRefName
            itIndentBarLines1 itIndentBarLines0 IndentBarLine
            '''
        )
    make_rule_action_for_all_many1_XOTs_iappendright(
        locals()
        , 'itTRefNames0s1 : itTRefNames0s0_Bars0 TRefNames0'
        )

    def p_Rule_1(p):
        'Rule : def_name OP_EQ TRefNames0s0'
        L = len(p)
        p[0] = p[1], p[L-1]
    def p_Rule_2(p):
        'Rule : def_name indent OP_EQ TRefNames0s0 itIndentBarLines0'
        L = len(p)
        p[0] = p[1], list(chain(p[L-2], *p[L-1]))
    def p_TRefNames0s0_1(p):
        'TRefNames0s0 : TRefNames0s1'
        p[0] = p[1]
    def p_TRefNames0s0_2(p):
        'TRefNames0s0 : '
        p[0] = []
    def p_TRefName_1(p):
        'TRefName : ref_name'
        p[0] = None, ref_name
    def p_TRefName_2(p):
        'TRefName : ref_xname'
        op, ref_name = ref_xname[0], ref_xname[1:]
        p[0] = op=='+', ref_name



lex_postprocessor_with_parser = lex_postprocessor.with_parser_from_args(P)

parse__grammar_tuples = lex_postprocessor_with_parser.parse_source_string

if __name__ == "__main__":
    from ._main import _main
    _main(__name__)


