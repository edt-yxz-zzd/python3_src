
'''
unit_rule_line example:
    A = B C D | | B +C D | B -C D | B | -B
tuple_rule_line example:
    A : B C D | | +B +C D | B -C D | B | -B

raw_tuple_rules :: [(name, [[(Maybe bool, name)]])]
true_tuple_rules :: [(name, [[(bool, name)]])]
'''

__all__ = '''
    raw_tuple_rules2true_tuple_rules
    parse_tuple_or_unit_rules_in_str
    may_raw_parse_tuple_or_unit_rule_line
    '''.split()

import re


TUPLE_OP = ':'
UNIT_OP = '='
TUPLE_or_UNIT_OP = f'{TUPLE_OP}{UNIT_OP}'
_name = r'(?:\w+)'
_xname = r'(?:[+-]?\w+)'
_spaces0 = r'(?:\s*)'
_spaces1 = r'(?:\s+)'
_xnames1 = fr'(?:{_xname}(?:{_spaces1}{_xname})*)'
_xnames0 = fr'(?:{_xnames1}?)'
_bar = fr'(?:{_spaces0}\|{_spaces0})'
_body = fr'(?:{_xnames0}(?:{_bar}{_xnames0})*)'

tuple_or_unit_rule_line_regex = re.compile(
    fr'{_spaces0}(?P<name>{_name}){_spaces0}(?P<OP>[{TUPLE_or_UNIT_OP}])(?P<_body_>{_spaces0}{_body}{_spaces0})'
    )
def parse_tuple_or_unit_rules_in_str(
    tuple_or_unit_rules_in_str, *, is_unit_op:bool
    ):
    '''str -> (is_unit_op:bool) -> true_tuple_rules

'''

    if type(is_unit_op) is not bool: raise TypeError

    raw_tuple_rules = []
    for line in tuple_or_unit_rules_in_str.split('\n'):
        line = line.strip()
        if not line: continue
        may = may_raw_parse_tuple_or_unit_rule_line(line)
        if may is None:
            raise ValueError(f'not tuple_rule_line or unit_rule_line: bad line: {line!r}')
        _is_unit_op, raw_tuple_rule = may
        if _is_unit_op is not is_unit_op:
            fine_op = TUPLE_or_UNIT_OP[is_unit_op]
            bad_op = TUPLE_or_UNIT_OP[not is_unit_op]
            #fine_op = '=' if is_unit_op else ':'
            #bad_op = '=' if not is_unit_op else ':'
            raise ValueError(f'op error! should be {fine_op!r} not {bad_op!r}')
        raw_tuple_rules.append(raw_tuple_rule)
    true_tuple_rules = raw_tuple_rules2true_tuple_rules(raw_tuple_rules)
    return true_tuple_rules

def may_raw_parse_tuple_or_unit_rule_line(tuple_or_unit_rule_line):
    '''-> None|(is_unit_op, raw_tuple_rule)
unit_rule_line example:
    A = B C D | | B +C D | B -C D | B | -B
tuple_rule_line example:
    A : B C D | | +B +C D | B -C D | B | -B
'''
    line = tuple_or_unit_rule_line
    assert '\n' not in line
    m = tuple_or_unit_rule_line_regex.match(line)
    if not m:
        return None
        raise ValueError('not tuple_rule_line or unit_rule_line')
    op = m.group('OP')
    assert op in TUPLE_or_UNIT_OP

    is_unit_op = op == '='
    name = m.group('name')
    _body_ = m.group('_body_')
    alternatives = _body_.split('|')

    pairss = []
    for s in alternatives:
        xnames = s.split()
        pairs = []
        for xname in xnames:
            ch = xname[0]
            if ch == '+':
                pair = True, xname[1:]
            elif ch == '-':
                pair = False, xname[1:]
            else:
                pair = None, xname
            pairs.append(pair)
        pairss.append(pairs)
    raw_tuple_rule = named_pairss = name, pairss
    return is_unit_op, raw_tuple_rule




_all_fsts = {None, True, False}
_bad_fsts = _all_fsts
def raw_tuple_rules2true_tuple_rules(raw_tuple_rules):
    '''
raw_tuple_rules :: [(name, [[(Maybe bool, name)]])]
true_tuple_rules :: [(name, [[(bool, name)]])]
'''

    named_pairss_ls = []
    for name, alternatives in raw_tuple_rules:
        pairss = []
        for pairs in alternatives:
            pairs = tuple(pairs)
            fsts = {fst for fst, _ in pairs}
            L = len(fsts)
            if L >= 3 or not (fsts < _all_fsts):
                raise ValueError('3 values occur in same alternative or contains object of illegal types')
            if None in fsts:
                # name not qualified by '+' or '-'
                # default to '+' if no '+'
                if True not in fsts:
                    default = True
                else:
                    # default to '-' if '+' occurs
                    default = False
                def f(fst):
                    return default if fst is None else fst
                pairs = tuple(f(fst) for fst,snd in pairs)
                del f
            pairss.append(pairs)
        named_pairss_ls.append((name, pairs))
    true_tuple_rules = named_pairss_ls
    return true_tuple_rules


