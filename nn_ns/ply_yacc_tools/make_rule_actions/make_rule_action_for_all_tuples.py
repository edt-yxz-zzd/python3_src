
__all__ = '''
    make_rule_action_for_all_tuples
    basic_make_rule_action_for_all_tuples
    is_true_tuple_rule
    '''.split()

from .imports import set_attrs
from .make_rule_inject_to import make_rule_inject_to
from .parse_tuple_or_unit_rules_in_str import \
    parse_tuple_or_unit_rules_in_str
from seed.tiny import echo

def make_rule_action_for_all_tuples(
    locals, tuple_rules_in_str, *, transform=None
    ):
    r'''
line example in tuple_rules_in_str:
    A = B +C D | -B -C D | B

# * no -
# * no +
# * either - or +
'''
    true_tuple_rules = parse_tuple_or_unit_rules_in_str(tuple_rules_in_str, is_unit_op=True)
    inject_to = make_rule_inject_to(locals); del locals
    basic_make_rule_action_for_all_tuples(
        inject_to, true_tuple_rules, transform=transform
        )

def is_true_tuple_rule(true_tuple_rule):
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

    return True

def basic_make_rule_action_for_all_tuples(
    inject_to, true_tuple_rules, *, transform=None
    ):
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
    if not all(map(is_true_tuple_rule, true_tuple_rules)): raise ValueError
    if transform is None:
        transform = echo

    for name, alternatives in true_tuple_rules:
        alter_strs = []
        indexess = []
        for alternative in (alternatives):
            names = []
            indexes = []
            for i, (b, n) in enumerate(alternative, 1):
                if b:
                    indexes.append(i)
                names.append(n)
            alter_str = ' '.join(names)
            alter_strs.append(alter_str)
            indexess.append(tuple(indexes))
        if len(set(indexess)) != 1:
            raise ValueError(f'should get obj at same indices: {alternative!r}')
        indices = indexess[0]
        body_str = ' | '.join(alter_strs)
        rule_str = '{name} : {body_str}'

        @inject_to
        @set_attrs(__doc__=rule_str)
        def p_(p, *, indices=indices, transform=transform):
            p[0] = transform(tuple(p[i] for i in indices))


