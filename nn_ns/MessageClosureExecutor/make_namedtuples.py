
r'''
'''

__all__ = '''
    make_namedtuples
    basic_make_namedtuples

    iter_parse_make_namedtuples_input
    '''.split()

from collections import namedtuple
from seed.iters.duplicate_elements import find_duplicate_element_groups
from seed.tiny import fst

def basic_make_namedtuples(type_name_field_names_pairs):
    pairs = tuple(type_name_field_names_pairs)
    type_name2field_names = dict(pairs)
    if len(type_name2field_names) != len(pairs):
        gs = find_duplicate_element_groups(map(fst, pairs))
        assert gs
        raise ValueError(f'contains duplicate type names: {gs}')
    return {type_name : namedtuple(type_name, field_names)
            for type_name, field_names in pairs
            }
def make_namedtuples(s):
    '''helper to make message/action/interface datatype

input string syntax:
    TypeName field_name*

output:
    {TypeName: namedtuple}

'''
    return basic_make_namedtuples(iter_parse_make_namedtuples_input(s))
def iter_parse_make_namedtuples_input(s):
    for line in s.split('\n'):
        names = line.split()
        if not names: continue
        type_name, *field_names = names
        yield type_name, field_names

