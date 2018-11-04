"""
grammar_units = '''
WholeFile = MaybeNullIndent +TheMainObject
TheMainObject
    = Object
    | OP_UNINDENT_DictHead NullIndent +DictBody
    | OP_UNINDENT_ObjectArrayHead NullIndent +ObjectArrayBody
    | OP_UNINDENT_ObjectTupleHead NullIndent +ObjectTupleBody
    | OP_UNINDENT_CharStringHead NullIndent +CharStringBody
    | OP_UNINDENT_ByteStringHead NullIndent +ByteStringBody
Object = Inline_Object | MultiLine_Object
'''

syntax of grammar_units:
    two cases:
        * one name without '+'
        * many1 names; one and only one name with '+'
    no comments
    allow empty lines

"""

__all__ = '''
    parse__grammar_units
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



def _eval_grammar_units():
    s = __doc__.split('\n\n')[0]
    d = {}
    exec(s, d, d)
    return d['grammar_units']
_grammar_units = _eval_grammar_units()
del _eval_grammar_units
_grammar_units_parse_result = [('WholeFile', [(1, ['MaybeNullIndent', 'TheMainObject'])]), ('TheMainObject', [0, ['Object'], (2, ['OP_UNINDENT_DictHead', 'NullIndent', 'DictBody']), (2, ['OP_UNINDENT_ObjectArrayHead', 'NullIndent', 'ObjectArrayBody']), (2, ['OP_UNINDENT_ObjectTupleHead', 'NullIndent', 'ObjectTupleBody']), (2, ['OP_UNINDENT_CharStringHead', 'NullIndent', 'CharStringBody']), (2, ['OP_UNINDENT_ByteStringHead', 'NullIndent', 'ByteStringBody'])]), ('Object', [(0, ['Inline_Object']), (0, ['MultiLine_Object'])])]



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
        r'{not_at_line_begin}[+]\w+'
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
parse_result__grammar_units :: [(def_name, [(idx, [ref_name])])]
whole = [rule]
rule = (def_name, [alter])
alter = (idx, [ref_name])
=============
Main
    Rules0
        return list(Rules0)
Rule
    def_name OP_EQ RefNamesX1s1
    def_name indent OP_EQ RefNamesX1 IndentBarLines0
        if len(p) == 6:
            ls = [RefNamesX1, *IndentBarLines0]
        elif len(p) == 4:
            ls = list(RefNamesX1s1)
        else:
            raise logic-error
        return def_name, ls
IndentBarLine = indent OP_BAR +RefNamesX1
RefNamesX1_Bar = +RefNamesX1 OP_BAR
RefNamesX1
    why the first version fail???
    : RefNames0 ref_xname RefNames0
    | ref_name
        if len(p) == 2:
            return (0, [ref_name])
        p1s = list(p[1])
        idx = len(p1s)
        return (idx, [*p1s, ref_xname, *p[3]])
    : ref_xname RefNames0
    | ref_name RefNames0 ref_xname RefNames0
    | ref_name
        L = len(p)
        if L == 3:
            idx = 0
            ls = [ref_xname[1:], *RefNames0]
        elif L == 5:
            ls = list(p[2])
            idx = len(ls)+1
            ls = [p[1], *ls, p[3][1:], *p[4]]
        elif L == 2:
            idx = 0
            ls = [ref_name]
        else:
            raise logic-error
        return idx, ls
################ XOA
Rules1 Rules0 Rule
IndentBarLines1 IndentBarLines0 IndentBarLine
RefNamesX1_Bars1 RefNamesX1_Bars0 RefNamesX1_Bar
RefNames1 RefNames0 ref_name
################ XOT
RefNamesX1s1 RefNamesX1_Bars0 RefNamesX1

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
        IndentBarLines1 IndentBarLines0 IndentBarLine
        RefNamesX1_Bars1 RefNamesX1_Bars0 RefNamesX1_Bar
        RefNames1 RefNames0 ref_name
        '''
        )
    make_rule_action_for_all_many1_XOTs_iappendright(
        locals()
        , 'RefNamesX1s1 RefNamesX1_Bars0 RefNamesX1'
        )

    def _(inject_to):
        @inject_to
        def p_(p):
            r'Main : Rules0'
            p[0] = list(p[1])
        @inject_to
        def p_(p):
            '''Rule \
    : def_name OP_EQ RefNamesX1s1
    | def_name indent OP_EQ RefNamesX1 IndentBarLines0
'''
            def_name = p[1]
            if len(p) == 6:
                RefNamesX1 = p[4]
                IndentBarLines0 = p[5]
                ls = [*RefNamesX1, *IndentBarLines0]
            elif len(p) == 4:
                ls = list(p[3])
            else:
                raise logic-error
            p[0] = def_name, ls
        @inject_to
        def p_(p):
            r'IndentBarLine : indent OP_BAR RefNamesX1'
            p[0] = p[3]
        @inject_to
        def p_(p):
            r'RefNamesX1_Bar : RefNamesX1 OP_BAR'
            p[0] = p[1]
        @inject_to
        def p_(p):
            '''RefNamesX1 \
    : ref_xname RefNames0
    | ref_name RefNames0 ref_xname RefNames0
    | ref_name
'''
            L = len(p)
            if L == 3:
                idx = 0
                ls = [p[1][1:], *p[2]]
            elif L == 5:
                ls = list(p[2])
                idx = len(ls)+1
                ls = [p[1], *ls, p[3][1:], *p[4]]
            elif L == 2:
                idx = 0
                ls = [p[1]]
            else:
                print(len(p))
                raise logic-error
            p[0]=  idx, ls

            return
            '''RefNamesX1\
    : RefNames0 ref_xname RefNames0
    | ref_name
'''
            L = len(p)
            if L == 2:
                ls = [p[1]]
                idx = 0
            elif L == 4:
                ls = list(p[1])
                idx = len(ls)
                ls = [*ls, p[2], *p[3]]
            else:
                raise logic-error
            p[0] = (idx, ls)
            return


        assert p_ is None
        del p_
        '''
        @inject_to
        def p_(p):
            r''
            p[0] =
        '''
    _(make_rule_inject_to(locals())); del _



lex_postprocessor_with_parser = lex_postprocessor.with_parser_from_args(P)

parse__grammar_units = lex_postprocessor_with_parser.parse_source_string

if __name__ == "__main__":
    from ._main import _main
    _main(__name__)


