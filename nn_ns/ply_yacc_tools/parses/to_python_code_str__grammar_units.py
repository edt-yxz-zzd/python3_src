
__all__ = '''
    to_python_code_str__grammar_units
    '''.split()

from collections import defaultdict
from seed.tiny import echo

imports_str__grammar_units = ''
def to_python_code_str__grammar_units(
    parse_result__grammar_units, *, transform_name=None : str
    ):
    '''
parse_result__grammar_units :: [(def_name, [(idx, [ref_name])])]
whole = [rule]
rule = (def_name, [alter])
alter = (idx, [ref_name])
==>>
    def p_{def_name}__units_{transform_name}_{idx}(p):
        '{def_name} : {ref_name}* | ...'
        return p[{idx+1}]
    ...
'''
    if transform_name is None: transform_name = ''
    rules = parse_result__grammar_units
    f = _to_python_code_str__grammar_units__rule
    python_code_str__grammar_units = ''.join(f(rule, transform_name) for rule in rules)
    return python_code_str__grammar_units

def _to_python_code_str__grammar_units__rule(rule, transform_name):
    def_name, alters = rule
    d = defaultdict(list)
    for idx, ref_names in alters:
        d[idx].append(ref_names)

    #if len(d) == 1:
    for idx, ref_namess in sorted(d.items()):
        alters_str = ' | '.join(' '.join(ref_names) for ref_names in ref_namess)
        rule_str = f'{def_name} : {alters_str}'
        return f'''
    def p_{def_name}__units_{transform_name}_{idx}(p):
        {rule_str!r}
        p[0] = {transform_name}(p[{idx}])
'''


