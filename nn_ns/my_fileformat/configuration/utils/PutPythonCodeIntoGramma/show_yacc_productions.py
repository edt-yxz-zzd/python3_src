

__all__ = '''
    extract_rules_from_yacc_productions
    show_yacc_productions
    show_yacc_productions_from_lex_postprocessor_with_parser
    '''.split()

from collections import defaultdict

def show_yacc_productions(productions):
    rules = extract_rules_from_yacc_productions(productions)
    for name, body in rules:
        print(name)
        op = ':'
        for names in body:
            line = ' '.join(names)
            print(f'    {op} {line}')
            op = '|'
    return

def extract_rules_from_yacc_productions(productions):
    '''
productions :: [ply.yacc.MiniProduction]
rules = [(name, [[name]])]

body :: [[name]]
rules = name_body_pairs
'''
    d = defaultdict(list)
    for production in productions:
        name = production.name
        name_, _names_ = production.str.split('->')
        names = _names_.split()
        d[name].append(names)
    rules = name_body_pairs = sorted(d.items())
    return rules

def show_yacc_productions_from_lex_postprocessor_with_parser(
    lex_postprocessor_with_parser):
    productions = lex_postprocessor_with_parser.lrparser.productions
    show_yacc_productions(productions)

