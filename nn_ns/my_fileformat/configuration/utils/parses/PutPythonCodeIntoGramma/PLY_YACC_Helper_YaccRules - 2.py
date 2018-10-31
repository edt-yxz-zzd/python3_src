

__all__ = '''
    PLY_YACC_Helper_YaccRules
    lex_postprocessor_with_parser
    '''.split()


from ..all_decorated_by_if import let_be_all_staticmethod
from .make_rule_inject_to import make_rule_inject_to
from .PLY_YACC_Helper_LexRules import lex_postprocessor, terminals
from .make_rule_action_for_all_many01_XOAs_iappendright import \
    make_rule_action_for_all_many01_XOAs_iappendright

@let_be_all_staticmethod('p_')
class PLY_YACC_Helper_YaccRules:
    '-> [(RuleName, [(RuleBody, [PythonLine])])]'
    start = 'Main'
    tokens = terminals

    make_rule_action_for_all_many01_XOAs_iappendright(
        locals()
        , 'Empty_iappendright'
        , '''
        Rules1 Rules0 Rule
        RuleBodyPythons1 RuleBodyPythons0 RuleBodyPython
        PythonLines1 PythonLines0 PythonLine
        '''
        )

    def _(inject_to):
        @inject_to
        def p_(p):
            r'Main : Rules1'
            p[0] = list(p[1])
        @inject_to
        def p_(p):
            r'Rule : RuleName RuleBodyPythons1'
            p[0] = (p[1], list(p[2]))

        @inject_to
        def p_(p):
            r'RuleBodyPython : RuleBody PythonLines1'
            p[0] = (p[1], list(p[2]))

        assert p_ is None
        del p_
        '''
        @inject_to
        def p_(p):
            r''
            p[0] =
        '''
    _(make_rule_inject_to(locals())); del _

    def p_error(p):
        raise Exception(p)


lex_postprocessor_with_parser = lex_postprocessor.with_parser_from_args(PLY_YACC_Helper_YaccRules)

if __name__ == '__main__':
    from .show_yacc_productions import \
        show_yacc_productions_from_lex_postprocessor_with_parser as show

    show(lex_postprocessor_with_parser)
    print()
    print()

    from .example import example
    parse = lex_postprocessor_with_parser.parse_source_string
    print(parse(example))

