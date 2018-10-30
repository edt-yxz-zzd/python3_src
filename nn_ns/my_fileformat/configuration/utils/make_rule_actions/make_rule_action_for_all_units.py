

__all__ = '''
    make_rule_action_for_all_units
    basic_make_rule_action_for_all_units
    is_true_unit_rule
    '''.split()

from .imports import set_attrs
from .make_rule_inject_to import make_rule_inject_to
from .parse_tuple_or_unit_rules_in_str import \
    parse_tuple_or_unit_rules_in_str

def make_rule_action_for_all_units(locals, unit_rules_in_str):
    '''
line example in unit_rules_in_str:
    A = B +C D | -B -C D | B

# one +, no -
# all - except one
# only one item, and it without [+-]
'''
    true_tuple_rules = parse_tuple_or_unit_rules_in_str(unit_rules_in_str, is_unit_op=True)
    inject_to = make_rule_inject_to(locals); del locals
    basic_make_rule_action_for_all_units(inject_to, true_tuple_rules)

def is_true_unit_rule(true_tuple_rule):
    name, alternatives = named_pairss = true_tuple_rule
    L = len(alternatives)
    if L == 0:
        return False

    # count True
    fsts = [fst for fst, _ in pairs]
    num_Trues = sum(fst is True for fst,_ in pairs)
    num_Falses = sum(fst is False for fst,_ in pairs)
    if num_Trues + num_Falses != L:
        return False
        raise ValueError('bad rule')

    return num_Trues == 1

def basic_make_rule_action_for_all_units(inject_to, true_tuple_rules):
    '''
true_tuple_rules :: [(name, [[(bool, name)]])]

A = B C D | | B +C D | B -C D | B | -B
    ==>> ('A', [
        [(None, 'B'), (None, 'C'), (None, 'D')]
        ,[]
        ,[(None, 'B'), (True, 'C'), (None, 'D')]
        ,[(None, 'B'), (False, 'C'), (None, 'D')]
        ,[(None, 'B')]
        ,[(False, 'B')]
        ])
<==> A = +B +C +D | | -B +C -D | +B -C +D | +B | -B

!ERROR: A = +B C -D


'''
    if not all(map(is_true_unit_rule, true_tuple_rules)): raise ValueError

    for name, alternatives in true_tuple_rules:
        alter_strs = []
        indexes = []
        for alternative in (alternatives):
            bools = []
            names = []
            for b, n in alternative:
                bools.append(b)
                names.append(n)
            i = bools.index(True)
            alter_str = ' '.join(names)
            alter_strs.append(alter_str)
            indexes.append(i+1)
        if len(set(indexes)) != 1:
            raise ValueError(f'should get obj at same index: {alternative}')
        i = indexes[0]
        body_str = ' | '.join(alter_strs)
        rule_str = '{name} : {body_str}'

        @inject_to
        @set_attrs(__doc__=rule_str)
        def p_(p, *, i=i):
            p[0] = p[i]


