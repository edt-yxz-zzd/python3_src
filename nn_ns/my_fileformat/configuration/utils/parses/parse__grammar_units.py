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
    ,let_be_all_staticmethod

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
    ref_xname
    indent
    OP_EQ
    OP_BAR
    '''.split()
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
    def t_ref_xname(t):
        r'(?<=[^\n])[+]\w+'
        # not_at_line_begin
        return t
    def t_ref_name(t):
        r'(?<=[^\n])\w+'
        # not_at_line_begin
        return t
    def t_indent(t):
        r'(?<![^\n])[ ]{4}(?=[^\n])'
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


@let_be_all_staticmethod('p_')
class P:
    '''
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


"""
_raw_legal_chars = r'\s\w=|+'

_line_sep_regex = re.compile(r'\n(?=\S)')
_all_chars_regex = re.compile(fr'[{_raw_legal_chars}]*')
_illegal_char_regex = re.compile(fr'[^{_raw_legal_chars}]')
_name = r'(?:\w+)'

#_names0 = fr'(?:(?:{_name}(?: {_name})*)?)'
_xname = fr'(?:\+{_name})'
_xnames1 = fr'(?:(?:{_name} )*{_xname}(?: {_name})*|{_name})'
_xnames1s1 = fr'(?:{_xnames1}(?: \| {_xnames1})*)'
_line = fr'(?P<name>\w+) = (?P<xnamess>{_xnames1s1})'


_line_regex = re.compile(_line)
print(_line)

def parse__grammar_units(grammar_units):
    'str -> [(name, [(idx, [name])])]'
    #assert '#' not in grammar_units
    #assert ':' not in grammar_units
    for m in _illegal_char_regex.finditer(grammar_units):
        ch = m.group(0)
        u = ord(ch)
        i = m.start()
        raise SyntaxError(f'contains bad char at {i}: U+{u:0>8X}={ch!r} :: {_illegal_char_regex.pattern!r}')
    lines = _line_sep_regex.split(grammar_units)
    name__idx_names_pairs__pairs = []
    for line in lines:
        if not line or line.isspace(): continue

        if line.count('=') != 1: raise SyntaxError(f'line: {line!r}')
        line = ' '.join(line.split())
        m = _line_regex.fullmatch(line)
        if not m:
            raise SyntaxError(f'line: {line!r}')

        name = m.group('name')

        xnamess = m.group('xnamess')
        idx_names_pairs = []
        for xnames in xnamess.split('|'):
            _1_2 = [xnames.split() for xnames in xnames.split('+')]
            L = len(_1_2)
            if L == 1:
                # no '+' ==>> single item
                [[ref_name]] = _1_2
                idx = 0
                idx_names_pairs.append((idx, [ref_name]))
            elif L == 2:
                fst, snd = _1_2
                idx = len(fst)
                idx_names_pairs.append((idx, fst+snd))
            else:
                raise logic-error
        name__idx_names_pairs__pairs.append((name, idx_names_pairs))
    return name__idx_names_pairs__pairs

"""
if __name__ == "__main__":

    for t in lex_postprocessor.tokenize(_grammar_units):
        print(t)
        del t
    print()
    print()
    print(parse__grammar_units(_grammar_units))

    from .example__grammar_units import grammar_units
    print(parse__grammar_units(grammar_units))
