

__all__ = '''
    PLY_YACC_Helper_YaccRules
    lex_postprocessor_with_parser
    '''.split()


from ..all_decorated_by_if import let_be_all_staticmethod
from .List_iappendleft import List_iappendleft
from .List_iappendright import List_iappendright
from .make_rule_inject_to import make_rule_inject_to
from .handle_rule_many01 import (
    handle_many1_iappendright
    ,handle_many0_iappendright
    )
from .PLY_YACC_Helper_LexRules import lex_postprocessor, terminals
from .example import example

@let_be_all_staticmethod('p_')
class PLY_YACC_Helper_YaccRules:
    '-> [(RuleName, [(RuleBody, [PythonLine])])]'
    start = 'Main'
    tokens = terminals

    inject_to = make_rule_inject_to(locals())
    @inject_to
    def p_(p):
        r'Main : Rules1'
        p[0] = list(p[1])

    @inject_to
    def p_(p):
        r'Rules1 : Rules0 Rule'
        handle_many1_iappendright(p)
    @inject_to
    def p_(p):
        r'Rules0 : Rules0 Rule | Empty_iappendright'
        handle_many0_iappendright(p)
    @inject_to
    def p_(p):
        r'Empty_iappendright :'
        p[0] = List_iappendright()

    @inject_to
    def p_(p):
        r'Rule : RuleName RuleBodyPythons1'
        p[0] = (p[1], list(p[2]))

    @inject_to
    def p_(p):
        r'RuleBodyPythons1 : RuleBodyPythons0 RuleBodyPython'
        handle_many1_iappendright(p)
    @inject_to
    def p_(p):
        r'RuleBodyPythons0 : RuleBodyPythons0 RuleBodyPython | Empty_iappendright'
        handle_many0_iappendright(p)
    @inject_to
    def p_(p):
        r'RuleBodyPython : RuleBody PythonLines1'
        p[0] = (p[1], list(p[2]))

    @inject_to
    def p_(p):
        r'PythonLines1 : PythonLines0 PythonLine'
        handle_many1_iappendright(p)
    @inject_to
    def p_(p):
        r'PythonLines0 : PythonLines0 PythonLine | Empty_iappendright'
        handle_many0_iappendright(p)
    assert p_ is None
    del inject_to
    del p_
    '''
    @inject_to
    def p_(p):
        r''
        p[0] =
    '''

    def p_error(p):
        raise Exception(p)

if 0:
    import ply.yacc
    from ..utils.make_pseudo_yacc_module_obj import make_pseudo_yacc_module_obj
    XXX_yacc_module = make_pseudo_yacc_module_obj(
        PLY_YACC_Helper_YaccRules
        )
    XXX_yacc_kwargs = {}
    lrparser = ply.yacc.yacc(module=XXX_yacc_module, **XXX_yacc_kwargs)
    parse_result = lrparser.parse(example, lexer=lex_postprocessor.make_source_lexer())
    print(parse_result)

lex_postprocessor_with_parser = lex_postprocessor.with_parser_from_args(PLY_YACC_Helper_YaccRules)

if __name__ == '__main__':
    print(lex_postprocessor_with_parser.parse_source_string(example))

