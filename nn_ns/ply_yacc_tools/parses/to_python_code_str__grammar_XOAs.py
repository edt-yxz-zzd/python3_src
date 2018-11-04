
__all__ = '''
    to_python_code_str__grammar_XOAs
    '''.split()

from ..make_rule_actions.List_iappendright import List_iappendright


imports_str__grammar_XOAs = '''
from {}.make_rule_actions.List_iappendright import List_iappendright
'''.format(__package__[:__package__.rindex('.')])

def to_python_code_str__grammar_XOAs(
    parse_result__grammar_XOAs, *, empty_name
    ):
    '''
parse_result__grammar_XOAs :: [(name, name, name)]
whole = [rule]
rule = (names1, names0, name)
==>>
    def p_{names1}__XOAs(p):
        '{names1} : {names0} {name}'
        p[0] = p[1].iappendright(p[2])
    def p_{names0}__XOAs(p):
        '{names0} : {names1} | {empty_name}'
        p[0] = p[1]
    ...
'''
    rules = parse_result__grammar_XOAs
    f = _to_python_code_str__grammar_XOAs__rule
    python_code_str__grammar_XOAs = ''.join(f(rule, empty_name) for rule in rules)
    return python_code_str__grammar_XOAs + f'''
    def p_{empty_name}__XOAs(p):
        '{empty_name} : '
        p[0] = List_iappendright()
'''

def _to_python_code_str__grammar_XOAs__rule(rule, empty_name):
    (names1, names0, name) = rule
    return f'''
    def p_{names1}__XOAs(p):
        '{names1} : {names0} {name}'
        p[0] = p[1].iappendright(p[2])
    def p_{names0}__XOAs(p):
        '{names0} : {names1} | {empty_name}'
        p[0] = p[1]
'''


