

__all__ = '''
    PLY_YACC_Helper_YaccRules
    parse_ex
    pythoncoded_rules2python_code_str_ex

    lex_postprocessor_with_parser
    pythoncoded_rules_in_str2pythoncoded_rules
    '''.split()


from .imports import (
    make_rule_inject_to
    ,make_rule_action_for_all_many01_XOAs_iappendright
    ,let_be_all_staticmethods
    )
from .PLY_YACC_Helper_LexRules import lex_postprocessor, terminals
from .pythoncoded_rules2python_code_str_ex import \
    pythoncoded_rules2python_code_str_ex


@let_be_all_staticmethods('p_')
class PLY_YACC_Helper_YaccRules:
    '''str -> [(RuleName, [(RuleBody, [PythonLine])])]
pythoncoded_rules_in_str -> pythoncoded_rules
#RuleBody = [[name]]
#RuleName = name
#PythonLine = str


pythoncoded_rules_in_str -> pythoncoded_rules
pythoncoded_rules -> python_code_str

pythoncoded_rules_in_str/python_code_str
    see: .example.py

'''
    start = 'Main'
    tokens = terminals
    def p_error(t):
        raise Exception(t)

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



lex_postprocessor_with_parser = lex_postprocessor.with_parser_from_args(PLY_YACC_Helper_YaccRules)

def parse_ex(pythoncoded_rules_in_str
    , name2count #= None
    , the_input_parameter_name #= 'p'
    , with_class_keyword #= False
    ):
    'pythoncoded_rules_in_str -> (head_str, tail_str::python_code_str, name2count)'
    parse = lex_postprocessor_with_parser.parse_source_string
    pythoncoded_rules = parse(pythoncoded_rules_in_str)
    return pythoncoded_rules2python_code_str_ex(pythoncoded_rules
        , name2count = name2count
        , the_input_parameter_name = the_input_parameter_name
        , with_class_keyword = with_class_keyword
        )


def pythoncoded_rules_in_str2pythoncoded_rules(pythoncoded_rules_in_str):
    '''str -> [(RuleName, [(RuleBody, [PythonLine])])]
pythoncoded_rules_in_str -> pythoncoded_rules
'''
    pythoncoded_rules = lex_postprocessor_with_parser.parse_source_string(
        pythoncoded_rules_in_str)
    return pythoncoded_rules

if __name__ == '__main__':
    from .show_yacc_productions import \
        show_yacc_productions_from_lex_postprocessor_with_parser as show

    show(lex_postprocessor_with_parser)
    print()
    print()

    from .example import example
    parse = lex_postprocessor_with_parser.parse_source_string
    print(parse(example))

    head_str, tail_str, name2count = parse_ex(example
        , name2count = None
        , the_input_parameter_name = 'ppp'
        , with_class_keyword = False
        )
    print(head_str+tail_str)
