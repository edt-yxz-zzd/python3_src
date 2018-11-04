
__all__ = '''
    to_python_code_str__grammar_XOTs
    '''.split()


imports_str__grammar_XOTs = ''
def to_python_code_str__grammar_XOTs(
    parse_result__grammar_XOTs, *, transform_name=None : str
    ):
    '''
parse_result__grammar_XOTs :: [(def_name, ref_name, ref_name)]
whole = [rule]
rule = (def_names1, ref_names0, ref_tail_name)
==>>
    def p_{def_names1}__XOTs_{transform_name}(p):
        '{def_names1} : {ref_names0} {ref_tail_name}'
        p[0] = p[1].iappendright(p[2])
    ...
'''
    if transform_name is None: transform_name = ''
    rules = parse_result__grammar_XOTs
    f = _to_python_code_str__grammar_XOTs__rule
    python_code_str__grammar_XOTs = ''.join(f(rule, transform_name) for rule in rules)

    return python_code_str__grammar_XOTs

def _to_python_code_str__grammar_XOTs__rule(rule, transform_name):
    (def_names1, ref_names0, ref_tail_name) = rule
    return f'''
    def p_{def_names1}__XOTs_{transform_name}(p):
        '{def_names1} : {ref_names0} {ref_tail_name}'
        p[0] = {transform_name}(p[1].iappendright(p[2]))
'''


