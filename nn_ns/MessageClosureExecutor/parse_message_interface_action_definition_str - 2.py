
'''
used in MessageClosureExecutor_ABC__using_namedtuple__str
'''

__all__ = '''
    parse_message_interface_action_definition_str
    '''.split()

from seed.iters.duplicate_elements import find_duplicate_element_groups
#from collections import namedtuple
#   since collections.namedtuple donot distinguish type_name/field_names
from seed.types.namedtuple import namedtuple
from itertools import chain

import re

comment_regex = re.compile(r'[#][^\n]*')


def parse_message_interface_action_definition_str(s):
    '''-> type_name2namedtuple_type, interface_constraint, action_constraint

used in MessageClosureExecutor_ABC__using_namedtuple__str


### input example:
>>> using_namedtuple_definition_str = """
... # comment
... ; MMsgNamedTupleDef fieldname0 fieldname1 fieldname2
... ; IIntfNamedTupleDefWithConstraint fieldname0 fieldname1
...     <- MMsgNamedTupleDef
... ; AActnNamedTupleDefWithConstraint fieldname0 fieldname1
...     <- IIntfNamedTupleDefWithConstraint IIntfNamedTupleDefWithConstraint
... """

>>> r = parse_message_interface_action_definition_str(using_namedtuple_definition_str)
>>> type_name2namedtuple_type, interface_constraint, action_constraint = r
>>> len(type_name2namedtuple_type)
3
>>> sorted(type_name2namedtuple_type.items()) #doctest: +ELLIPSIS
[('AActnNamedTupleDefWithConstraint', <class '...AActnNamedTupleDefWithConstraint'>), ('IIntfNamedTupleDefWithConstraint', <class '...IIntfNamedTupleDefWithConstraint'>), ('MMsgNamedTupleDef', <class '...MMsgNamedTupleDef'>)]
>>> interface_constraint
{'IIntfNamedTupleDefWithConstraint': 'MMsgNamedTupleDef'}
>>> action_constraint
{'AActnNamedTupleDefWithConstraint': ('IIntfNamedTupleDefWithConstraint', 'IIntfNamedTupleDefWithConstraint')}


'''
    # remove comment
    s = comment_regex.sub('', s)

    ################
    empty, *lines = s.split(';')
    if empty.split(): raise SyntaxError(empty)

    msg_namess = []
    intf_names_name_pairs = []
    actn_names_names_pairs = []

    for line in lines:
        parts = line.split('<-')

        L = len(parts)
        assert L
        if L > 2: raise SyntaxError(line)
        parts = [s.split() for s in parts]
        fst_part = parts[0]
        if not fst_part: raise SyntaxError(line, fst_part)
        fst_word = fst_part[0]
        initial_char = fst_word[0]

        assert len(initial_char) == 1
        if initial_char not in 'MIA': raise SyntaxError(fst_part, fst_word)
        if initial_char == 'M':
            if L != 1: raise SyntaxError(fst_part, '<-')
            [fst_part] = parts
            names = fst_part
            msg_namess.append(names)
        else:
            snd_initial = 'M' if initial_char == 'I' else 'I'
            minL, maxL = (1,1) if initial_char == 'I' else (0,float('inf'))
            if L != 2: raise SyntaxError(fst_part, '<-')
            fst_part, snd_part = parts
            if not (minL <= len(snd_part) <= maxL):
                raise SyntaxError(line, snd_part, (minL, maxL))
            for word in snd_part:
                if word[0] != snd_initial:
                    raise SyntaxError(snd_part, word, snd_initial)

            names1 = fst_part
            names2 = snd_part
            if initial_char == 'I':
                [name2] = names2
                pair = names1, name2
                intf_names_name_pairs.append(pair)
            else:
                pair = names1, names2
                actn_names_names_pairs.append(pair)
    # end-for

    type_name2field_names__list = []
    interface_constraint__list = []
    action_constraint__list = []
    # msg_namess
    defined_message_names = set()
    for msg_name, *names in msg_namess:
        type_name2field_names__list.append((msg_name, names))
        defined_message_names.add(msg_name)
    # intf_names_name_pairs
    for ([intf_name, *names], msg_name) in intf_names_name_pairs:
        type_name2field_names__list.append((intf_name, names))
        interface_constraint__list.append((intf_name, msg_name))
    # actn_names_names_pairs
    for ([actn_name, *names], intf_names) in actn_names_names_pairs:
        type_name2field_names__list.append((actn_name, names))
        action_constraint__list.append((actn_name, tuple(intf_names)))

    def pairs2dict(pairs):
        d = dict(pairs)
        if len(d) != len(pairs):
            duplicates = find_duplicate_element_groups(duplicate_elements)
            assert len(duplicates)
            raise SyntaxError('duplicate: {duplicates}')
        return d
    type_name2field_names = pairs2dict(type_name2field_names__list)
    interface_constraint = pairs2dict(interface_constraint__list)
    action_constraint = pairs2dict(action_constraint__list)

    type_name2namedtuple_type = {
        type_name : namedtuple(type_name, field_names)
        for type_name, field_names in type_name2field_names.items()
        }

    for actn_name, intf_names in action_constraint.items():
        tp = namedtuple_type = type_name2namedtuple_type[actn_name]
        if len(tp._fields) < len(intf_names):
            raise SyntaxError(f'{actn_name!r}: len(field_names) < len(interface_names)')

    #print(interface_constraint)
    #print(action_constraint)
    defined_interface_names = set(interface_constraint)
    # bugs: chain ==>> chain.from_iterable
    undefined_intf_names = set(chain.from_iterable(action_constraint.values())) - defined_interface_names

    defined_message_names = defined_message_names
    undefined_msg_names = set(interface_constraint.values()) - defined_message_names
    undefined_names = undefined_msg_names | undefined_intf_names
    if undefined_names:
        raise SyntaxError(f'undefined {undefined_names}')

    return type_name2namedtuple_type, interface_constraint, action_constraint

def _t():
    using_namedtuple_definition_str = """
    # comment
    ; MMsgNamedTupleDef fieldname0 fieldname1 fieldname2
    ; IIntfNamedTupleDefWithConstraint fieldname0 fieldname1
        <- MMsgNamedTupleDef
    ; AActnNamedTupleDefWithConstraint fieldname0 fieldname1
        <- IIntfNamedTupleDefWithConstraint IIntfNamedTupleDefWithConstraint
    """


    r = parse_message_interface_action_definition_str(using_namedtuple_definition_str)
    print(r)
    type_name2namedtuple_type, interface_constraint, action_constraint = r
    print(f'type_name2namedtuple_type={type_name2namedtuple_type}')
    print(f'interface_constraint={interface_constraint}')
    print(f'action_constraint={action_constraint}')
if __name__ == "__main__":
    _t()

    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


