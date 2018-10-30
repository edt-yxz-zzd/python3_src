"""
grammar_codes = '''
ByteStringBody
    CharStringBody
        # CharStringBody ==>> ByteStringBody
        return CharStringBody.encode('ascii')

Inline_ObjectArray
    middle_open Inline_ListItems0 middle_close
        return list(Inline_ListItems0)
a
    an_alternative
        pass
    other_alternative | more
        pass
'''




syntax of grammar_codes:
    no ":" or "="
    using "|" to split
    allow indented comments
    allow empty lines

"""

__all__ = '''
    parse__grammar_codes
    '''.split()


from .imports__grammar_codes import (
    PLY_YACC_Helper_LexRules
    ,lex_postprocessor

    ,PLY_YACC_Helper_YaccRules
    ,parse_ex
    ,lex_postprocessor_with_parser
    ,pythoncoded_rules2python_code_str_ex
    )

T = PLY_YACC_Helper_LexRules
P = PLY_YACC_Helper_YaccRules


def _eval_grammar_codes():
    s = __doc__.split('\n'*3)[0]
    d = {}
    exec(s, d, d)
    return d['grammar_codes']
_grammar_codes = _eval_grammar_codes()
del _eval_grammar_codes

parse__grammar_codes = lex_postprocessor_with_parser.parse_source_string


if __name__ == "__main__":
    for t in lex_postprocessor.tokenize(_grammar_codes):
        print(t)
        del t
    print()
    print()
    print(parse__grammar_codes(_grammar_codes))

    from .example__grammar_codes import grammar_codes
    print(parse__grammar_codes(grammar_codes))
