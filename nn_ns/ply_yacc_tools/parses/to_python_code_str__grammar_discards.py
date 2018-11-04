
__all__ = '''
    to_python_code_str__grammar_discards
    '''.split()

imports_str__grammar_discards = ''
def to_python_code_str__grammar_discards(
    parse_result__grammar_discards
    ):
    '''
parse_result__grammar_discards :: [(def_name, [[ref_name]])]
whole = [rule]
rule = (def_name, [alter])
alter = [ref_name]
==>>
    def p_{def_name}__discards(p):
        '{def_name} : {ref_name}* | ...'
    ...
'''
    rules = parse_result__grammar_discards
    f = _to_python_code_str__grammar_discards__rule
    python_code_str__grammar_discards = ''.join(map(f, rules))
    return python_code_str__grammar_discards

def _to_python_code_str__grammar_discards__rule(rule):
    def_name, ref_namess = rule
    alters_str = ' | '.join(' '.join(ref_names) for ref_names in ref_namess)
    rule_str = f'{def_name} : {alters_str}'
    return f'''
    def p_{def_name}__discards(p):
        {rule_str!r}
'''


