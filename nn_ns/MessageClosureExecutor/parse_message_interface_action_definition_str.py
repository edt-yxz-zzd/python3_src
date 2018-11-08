
'''
used in MessageClosureExecutor_ABC__using_namedtuple__str
'''

__all__ = '''
    parse_message_interface_action_definition_str
    check_parse2_result
    '''.split()

from seed.iters.duplicate_elements import find_duplicate_element_groups
#from collections import namedtuple
#   since collections.namedtuple donot distinguish type_name/field_names
from seed.types.namedtuple import namedtuple
from itertools import chain
from collections import defaultdict

import re

comment_regex = re.compile(r'[#][^\n]*')
_field_name = r'(?:\b\w+\b)'
_field_names0 = fr'(?:(?:\s*{_field_name})*)'
_msg_name = r'(?:\bM\w*\b)'
_intf_name = r'(?:\bI\w*\b)'
_intf_names0 = fr'(?:(?:\s*{_intf_name})*)'
_actn_name = r'(?:\bA\w*\b)'
msg_def_regex = re.compile(fr'\s*;\s*(?P<M>{_msg_name})(?P<Fs0>{_field_names0})\s*')
intf_def_regex = re.compile(fr'\s*;\s*(?P<I>{_intf_name})(?P<Fs0>{_field_names0})\s*<-\s*(?P<M>{_msg_name})\s*')

auto_actn_def_regex = re.compile(fr'\s*;\s*(?P<A>{_actn_name})\s*(?P<F>{_field_name})\s*<-\s*@\s*(?P<I>{_intf_name})\s*')
    # auto_actn_def_regex should before nonauto_actn_def_regex
nonauto_actn_def_regex = re.compile(fr'\s*;\s*(?P<A>{_actn_name})(?P<Fs0>{_field_names0})\s*<-\s*(?P<Is0>{_intf_names0})\s*')
    # require '<-' even no field_names

def check_parse1_result(
    msg_name_field_names_pairs
    , intf_name_field_names_msg_name_triples
    , actn_name_field_names_intf_names_triples
    , auto_actn_names
    ):
    # unique:
    it = chain(msg_name_field_names_pairs
            , intf_name_field_names_msg_name_triples
            , actn_name_field_names_intf_names_triples
            )
    unique_names = [tpl23[0] for tpl23 in it]
    if len(set(unique_names)) < len(unique_names):
        duplicates = find_duplicate_element_groups(duplicate_elements)
        assert len(duplicates)
        raise SyntaxError('duplicate: {duplicates}')
    # more verify in later
    #   all used_names should be defined
    #   len(actn.fields) >= (actn.intf_names)
    #   len(auto_actn.intf_names) == 1
    #   bijection: auto_actn <-> intf2autos
    #   maker inside type_name2namedtuple_type

def check_parse2_result(
    type_name2namedtuple_type # MIA -> type
    ,interface_constraint # I -> M
    ,action_constraint # A -> [I]
    ,auto_action_constructor2maker # A -> type
    ,interface_constructor2auto_action_constructors # I -> {A}
    ):
    '''
used in _Parser and MessageClosureExecutor_ABC__using_namedtuple
'''
    # type name
    def sfilter(f, it):
        return set(filter(f, it))
    def not_type(tp):
        return not isinstance(tp, type)
    bad_types = sfilter(not_type, type_name2namedtuple_type.values())
    if bad_types:
        raise SyntaxError(f'bad_types: {bad_types}')
    def is_bad_name(type_name):
        tp = type_name2namedtuple_type[type_name]
        return type_name != tp.__name__
    bad_type_names = sfilter(is_bad_name, type_name2namedtuple_type)
    if bad_type_names:
        raise SyntaxError(f'bad_type_names: {bad_type_names}')

    #   all used_names should be defined
    used_msg_names = set(interface_constraint.values())
    used_intf_names = (set(interface_constraint)
        | set(chain.from_iterable(action_constraint.values()))
        | set(interface_constructor2auto_action_constructors)
        )
    used_actn_names = (set(action_constraint)
        | set(auto_action_constructor2maker)
        | set(chain.from_iterable(interface_constructor2auto_action_constructors.values()))
        )
    used_names = used_msg_names | used_intf_names | used_actn_names
    defined_names = set(type_name2namedtuple_type)
    undefined_names = used_names - defined_names
    if undefined_names:
        raise SyntaxError(f'undefined {undefined_names}')
    # M I A
    def not_startswith(*chars):
        return lambda s: all(not s.startswith(ch) for ch in chars)
    def startswith(ch):
        return lambda s: s.startswith(ch)
    bad_msg_names = sfilter(not_startswith('M'), used_msg_names)
    bad_intf_names = sfilter(not_startswith('I'), used_intf_names)
    bad_actn_names = sfilter(not_startswith('A'), used_actn_names)
    bad_names = sfilter(not_startswith(*'MIA'), defined_names)
    if bad_msg_names:
        raise SyntaxError(f'bad_msg_names: {bad_msg_names}')
    if bad_intf_names:
        raise SyntaxError(f'bad_intf_names: {bad_intf_names}')
    if bad_actn_names:
        raise SyntaxError(f'bad_actn_names: {bad_actn_names}')
    if bad_names:
        raise SyntaxError(f'bad_names: {bad_names}')

    # all intf_names actn_names
    all_intf_names = set(interface_constraint)
    all_actn_names = set(action_constraint)
    _all_intf_names = sfilter(startswith('I'), defined_names)
    _all_actn_names = sfilter(startswith('A'), defined_names)
    unmatch_intf_names = all_intf_names ^ _all_intf_names
    unmatch_actn_names = all_actn_names ^ _all_actn_names
    if unmatch_intf_names:
        raise SyntaxError(f'unmatch_intf_names: {unmatch_intf_names}')
    if unmatch_actn_names:
        raise SyntaxError(f'unmatch_actn_names: {unmatch_actn_names}')

    unmatch_intf_names = set(interface_constructor2auto_action_constructors) - all_intf_names
    unmatch_actn_names = set(auto_action_constructor2maker) - all_actn_names
    if unmatch_intf_names:
        raise SyntaxError(f'unmatch_intf_names: {unmatch_intf_names}')
    if unmatch_actn_names:
        raise SyntaxError(f'unmatch_actn_names: {unmatch_actn_names}')


    #   len(actn.fields) >= (actn.intf_names)
    def is_bad_num_fields(actn_name):
        tp = type_name2namedtuple_type[actn_name]
        num_fields = len(tp._fields)
        num_intf_names = len(action_constraint[actn_name])
        return not num_fields >= num_intf_names
    bad_actn_names = sfilter(is_bad_num_fields, all_actn_names)
    if bad_actn_names:
        raise SyntaxError(f'too few field names: {bad_actn_names}')

    #   len(auto_actn.intf_names) == 1
    def is_bad_num_intf_names(auto_actn_name):
        num_intf_names = len(action_constraint[auto_actn_name])
        return not num_intf_names == 1
    all_auto_actn_names = set(auto_action_constructor2maker)
    bad_auto_actn_names = sfilter(is_bad_num_fields, all_auto_actn_names)
    if bad_auto_actn_names:
        raise SyntaxError(f'auto_action should have exactly one interface: {bad_auto_actn_names}')

    #   bijection: auto_actn <-> intf2autos
    def is_bad_auto_actn_name__not_goback(auto_actn_name):
        [intf_name] = action_constraint[auto_actn_name]
        return auto_actn_name not in interface_constructor2auto_action_constructors.get(intf_name, ())
    def is_bad_intf_name__not_goback(intf_name):
        for auto_actn_name in interface_constructor2auto_action_constructors.get(intf_name, ()):
            [_intf_name] = action_constraint[auto_actn_name]
            if intf_name != _intf_name:
                return True
        return False
    bad_auto_actn_names = sfilter(is_bad_auto_actn_name__not_goback, all_auto_actn_names)
    bad_intf_names = sfilter(is_bad_intf_name__not_goback, all_intf_names)
    if bad_auto_actn_names:
        raise SyntaxError(f'not goback: {bad_auto_actn_names}')
    if bad_intf_names:
        raise SyntaxError(f'not goback: {bad_intf_names}')

    #   maker inside type_name2namedtuple_type
    def is_wrong_maker(auto_actn_name):
        maker = auto_action_constructor2maker[auto_actn_name]
        _maker = type_name2namedtuple_type[auto_actn_name]
        return _maker is not maker
    bad_auto_actn_names = sfilter(is_wrong_maker, all_auto_actn_names)
    if bad_auto_actn_names:
        raise SyntaxError(f'unmatch maker: {bad_auto_actn_names}')



class _Parser:
    def __init__(self, source):
        #self.source = comment_regex.sub('', source)
        def to_spaces(m):
            return ' ' * (m.end() - m.start())
        self.new_source = comment_regex.sub(to_spaces, source)
        self.old_source = source

        self.msg_name_field_names_pairs = []
        self.intf_name_field_names_msg_name_triples = []
        self.actn_name_field_names_intf_names_triples = []
        self.auto_actn_names = []
    def parse1(self):
        pairs = \
            [(msg_def_regex, self.handle_msg_def)
            ,(intf_def_regex, self.handle_intf_def)
            ,(auto_actn_def_regex, self.handle_auto_actn_def)
            # auto_actn_def_regex before nonauto_actn_def_regex
            ,(nonauto_actn_def_regex, self.handle_nonauto_actn_def)
            ]
        s = self.new_source
        begin = 0
        end = len(s)
        while begin < end:
            for regex, handle in pairs:
                m = regex.match(s, begin, end)
                if m:
                    begin = m.end()
                    handle(m)
                    break
            else:
                raise SyntaxError(self.old_source[begin:])
        result1 = self.get_parse1_result()
        check_parse1_result(*result1)
        return result1
    def get_parse1_result(self):
        return (self.msg_name_field_names_pairs
            ,self.intf_name_field_names_msg_name_triples
            ,self.actn_name_field_names_intf_names_triples
            ,self.auto_actn_names
            )
    def parse2(self):
        #type_name2namedtuple_type
        #interface_constraint
        #action_constraint
        #auto_action_constructor2maker
        #interface_constructor2auto_action_constructors
        def get_first2(ls):
            return ls[:2]
        def map_get_first2(tuples):
            # tuples -> pairs
            return map(get_first2, tuples)
        type_name2field_names = dict(chain.from_iterable(
            map(map_get_first2, self.get_parse1_result()[:-1])))
        type_name2namedtuple_type = {
            type_name : namedtuple(type_name, field_names)
            for type_name, field_names in type_name2field_names.items()
            }
        interface_constraint = {intf_name: msg_name
            for intf_name, _, msg_name in self.intf_name_field_names_msg_name_triples
            }
        action_constraint = {actn_name: tuple(intf_names)
            for actn_name, _, intf_names in self.actn_name_field_names_intf_names_triples
            }
        auto_action_constructor2maker = {
            auto_actn_name: type_name2namedtuple_type[auto_actn_name]
            for auto_actn_name in self.auto_actn_names
            }

        intf_name2auto_actn_names = defaultdict(list)
        for auto_actn_name in self.auto_actn_names:
            [intf_name] = action_constraint[auto_actn_name]
            intf_name2auto_actn_names[intf_name].append(auto_actn_name)
        interface_constructor2auto_action_constructors = {
            intf_name: set(auto_actn_names)
            for intf_name, auto_actn_names in intf_name2auto_actn_names.items()
            }


        result2 = (type_name2namedtuple_type
                ,interface_constraint
                ,action_constraint
                ,auto_action_constructor2maker
                ,interface_constructor2auto_action_constructors
                )
        #from pprint import pprint; pprint(result2)
        check_parse2_result(*result2)
        return result2





    def handle_msg_def(self, m):
        ls = self.msg_name_field_names_pairs
        msg_name = m.group('M')
        field_names = m.group('Fs0').split()
        ls.append((msg_name, field_names))
    def handle_intf_def(self, m):
        ls = self.intf_name_field_names_msg_name_triples
        intf_name = m.group('I')
        field_names = m.group('Fs0').split()
        msg_name = m.group('M')
        ls.append((intf_name, field_names, msg_name))
    def handle_nonauto_actn_def(self, m):
        ls = self.actn_name_field_names_intf_names_triples
        actn_name = m.group('A')
        field_names = m.group('Fs0').split()
        intf_names = m.group('Is0').split()
        ls.append((actn_name, field_names, intf_names))
    def handle_auto_actn_def(self, m):
        ls = self.actn_name_field_names_intf_names_triples
        ls2 = self.auto_actn_names
        actn_name = m.group('A')
        field_names = [m.group('F')]
        intf_names = [m.group('I')]
        ls.append((actn_name, field_names, intf_names))
        ls2.append(actn_name)


def parse_message_interface_action_definition_str(s):
    '''-> type_name2namedtuple_type, interface_constraint, action_constraint, auto_action_constructor2maker, interface_constructor2auto_action_constructors

used in MessageClosureExecutor_ABC__using_namedtuple__str


### input example:
>>> using_namedtuple_definition_str = """
... # comment
... ; MMsgNamedTupleDef fieldname0 fieldname1 fieldname2
... ; IIntfNamedTupleDefWithConstraint fieldname0 fieldname1
...     <- MMsgNamedTupleDef
... ; AActnNamedTupleDefWithConstraint fieldname0 fieldname1
...     <- IIntfNamedTupleDefWithConstraint IIntfNamedTupleDefWithConstraint
... ; AAutoActnDef fieldname0
...     <- @IIntfNamedTupleDefWithConstraint
... """

>>> r = parse_message_interface_action_definition_str(using_namedtuple_definition_str)
>>> type_name2namedtuple_type, interface_constraint, action_constraint, auto_action_constructor2maker, interface_constructor2auto_action_constructors = r
>>> len(type_name2namedtuple_type)
4
>>> sorted(type_name2namedtuple_type.items()) #doctest: +ELLIPSIS
[('AActnNamedTupleDefWithConstraint', <class '...AActnNamedTupleDefWithConstraint'>), ('AAutoActnDef', <class '...AAutoActnDef'>), ('IIntfNamedTupleDefWithConstraint', <class '...IIntfNamedTupleDefWithConstraint'>), ('MMsgNamedTupleDef', <class '...MMsgNamedTupleDef'>)]
>>> interface_constraint
{'IIntfNamedTupleDefWithConstraint': 'MMsgNamedTupleDef'}
>>> sorted(action_constraint.items())
[('AActnNamedTupleDefWithConstraint', ('IIntfNamedTupleDefWithConstraint', 'IIntfNamedTupleDefWithConstraint')), ('AAutoActnDef', ('IIntfNamedTupleDefWithConstraint',))]


>>> auto_action_constructor2maker #doctest: +ELLIPSIS
{'AAutoActnDef': <class '...AAutoActnDef'>}
>>> interface_constructor2auto_action_constructors
{'IIntfNamedTupleDefWithConstraint': {'AAutoActnDef'}}

'''
    p = _Parser(s)
    p.parse1()
    return p.parse2()
    return (type_name2namedtuple_type, interface_constraint, action_constraint, auto_action_constructor2maker, interface_constructor2auto_action_constructors)

def _t():
    using_namedtuple_definition_str = """
    # comment
    ; MMsgNamedTupleDef fieldname0 fieldname1 fieldname2
    ; IIntfNamedTupleDefWithConstraint fieldname0 fieldname1
        <- MMsgNamedTupleDef
    ; AActnNamedTupleDefWithConstraint fieldname0 fieldname1
        <- IIntfNamedTupleDefWithConstraint IIntfNamedTupleDefWithConstraint
    ; AAutoActnDef fieldname0
        <- @IIntfNamedTupleDefWithConstraint
    """


    r = parse_message_interface_action_definition_str(using_namedtuple_definition_str)
    print(r)
    (type_name2namedtuple_type
    ,interface_constraint
    ,action_constraint
    ,auto_action_constructor2maker
    ,interface_constructor2auto_action_constructors
    ) = r
    print(f'type_name2namedtuple_type={type_name2namedtuple_type}')
    print(f'interface_constraint={interface_constraint}')
    print(f'action_constraint={action_constraint}')
    print(f'auto_action_constructor2maker={auto_action_constructor2maker}')
    print(f'interface_constructor2auto_action_constructors={interface_constructor2auto_action_constructors}')
if __name__ == "__main__":
    _t()

    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


