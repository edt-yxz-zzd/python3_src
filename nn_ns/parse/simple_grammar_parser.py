
__all__ = '''
    simple_grammar_parser maybe_token_refs
'''.split()

from sand import concat


def simple_grammar_parser(grammar):
    r'''generate args for UngerMethod() from a CF grammar

grammar is sth like:
    S = a S
    S = b

grammar:
    no comments
    allow empty lines
    '=' is the only keyword, but can be used as rule name
    using str.split to split out words
    nonemptyline should be: '\s*(\S+)\s*(=)(\s*\S+)*\s*'

output is 2 input arguments of UngerMethod:
    (nontoken_ref2rule_ids, rule_id2refs)

    
example:
    >>> grammar = 'S = a S\nS = b'
    >>> result = simple_grammar_parser(grammar)
    >>> result == \
    ...    ({'S': ['S-0', 'S-1']}, {'S-0': ['a', 'S'], 'S-1': ['b']})
    True
    >>> maybe_token_refs(*result) == set('ab')
    True
'''
    
    def parse_line(line):
        words = line.split()
        if not (len(words) >= 2 and words[1] == '='):
            raise ValueError('bad CFG format: SHOULD BE sth like: "S = a b"'
                             ': lineno={} : {!r}'.format(lineno, line))

        ref = words[0]
        refs = words[2:]

        if ref not in nontoken_ref2rule_ids:
            nontoken_ref2rule_ids[ref] = []

        rks = nontoken_ref2rule_ids[ref]
        rk = '{}-{}'.format(ref, len(rks))
        rks.append(rk)

        assert rk not in rule_id2refs
        rule_id2refs[rk] = refs
        


    nontoken_ref2rule_ids = {}
    rule_id2refs = {}
    for lineno, line in enumerate(grammar.splitlines()):
        if not line or line.isspace():
            continue

        parse_line(line)
        
    return nontoken_ref2rule_ids, rule_id2refs

def maybe_token_refs(nontoken_ref2rule_ids, rule_id2refs):
    'token_ref or dead nontoken_ref'
    return set(concat(rule_id2refs.values())) - set(nontoken_ref2rule_ids)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
