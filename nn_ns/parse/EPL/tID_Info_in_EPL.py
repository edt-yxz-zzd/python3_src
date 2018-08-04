

from ast import literal_eval
from MyLL1L.tools_for_id2infoID_MyLL1L import tIDDict_2_id2info
from EPL.parse_result2EPL import is_parse_result_EPL

main_name = 'tIDDict2parse_result_EPL'
def tIDDict2parse_result_EPL(tIDDict):
    id2info = tIDDict_2_id2info(tIDDict)
    name = (main_name,)
    tag = ()
    
    ls = [id_info2parse_result_EPL(info) for ID, info in id2info.items()]
    return (name, tag, ls)


def parse_result_EPL_to_tID2plain_info(r):
    if not is_parse_result_EPL(r):
        raise ValueError('not is_parse_result_EPL')
    
    name, tag, ls = r
    if (main_name,) != name or tag != ():
        raise ValueError('not result of tIDDict2parse_result_EPL')

    d = {}
    tID = ()
    _children_to_tID2plain_info(tID, d, ls)
    return d


def _children_to_tID2plain_info(parent_tID, tID2plain_info, children):
    for i, c in enumerate(children):
        _child_to_tID2plain_info(parent_tID, tID2plain_info, i, c)

def _get_attrs(attrs):
    d = {}
    L = len(attrs)
    for attr in attrs:
        name, tag, ls = attr
        if ls:
            raise ValueError('not attr: name={!r}; tag={}; has children'.format(name, tag))
        if len(name) != 2 or name[0] != '.':
            raise ValueError('not attr: name={!r} not in form (., key)'.format(name))

        _, key = name
        if key in d:
            raise ValueError('not attr: repeat attr={!r}'.format(key))
        d[key] = tag
    assert L == len(d)
    return d

def _get_attrs_constaint(attrs,
                         one_keys,              # 1, str
                         optional_keys = set(), # 0-1, None or str
                         key2bound = {},        # min-max, tuple # default: 0-inf
                         not_required_keys = set(), # if absent get None
                         allow_unknown_key = False
                         ):
    d = _get_attrs(attrs)
    attrs_keys = set(d)

    bounded_keys = set(key2bound)

    union_disjoint_sets = set.union(one_keys, optional_keys, bounded_keys)
    if len(union_disjoint_sets) != \
       len(one_keys) + len(optional_keys) + len(bounded_keys):
        raise ValueError('one_keys, optional_keys, bounded_keys should be disjoint')
    
    known_keys = set.union(union_disjoint_sets, not_required_keys)
    
    if not allow_unknown_key:
        if not attrs_keys <= known_keys:
            unknown_key = (attrs_keys - known_keys).pop()
            raise ValueError('unknown key: {!r}'.format(unknown_key))

    required_keys = known_keys - not_required_keys
    if not required_keys <= attrs_keys:
        absent_key = (required_keys - attrs_keys).pop()
        raise ValueError('require key: {!r}'.format(absent_key))

    absent_keys = not_required_keys - set(d)
    
    for key in one_keys - absent_keys:
        v = d[key]
        if len(v) != 1:
            raise ValueError('not attr with one_tag attr={!r}'.format(key))
        v, = v
        d[key] = v
        
    for key in optional_keys - absent_keys:
        v = d[key]
        if len(v) > 1:
            raise ValueError('not attr with optional_tag attr={!r}'.format(key))
        if v:
            v, = v
        else:
            v = None
        d[key] = v

    
    for key in bounded_keys - absent_keys:
        v = d[key]
        min, max = key2bound[key]
        
        if not (min <= len(v) <= max):
            raise ValueError('attr={!r}; bound={}-{}; len(tag)=={}'\
                             .format(key, min, max, len(v)))
        
            
    
    for k in absent_keys: d[k] = None
    return d

def _get_attrs_of_Item(attrs):
    d = _get_attrs_constaint(attrs,
                         one_keys = {'refID', 'min', 'max'},
                         optional_keys = {'name'},
                         key2bound = {},
                         not_required_keys = set(),
                         allow_unknown_key = False
                         )
    return d


def _get_attrs_of_Token(attrs):
    d = _get_attrs_constaint(attrs,
                         one_keys = {'type'}
                         )
    return d
        
def _child_to_tID2plain_info(parent_tID, tID2plain_info, idx, child):
    name, tag, ls = child
    case, = name
    if case == 'Item':
        if tag != () or not parent_tID:
            raise ValueError()

        attrs = ls
        d = _get_attrs_of_Item(attrs)
        
        refID = d['refID']
        min = d['min']
        max = d['max']
        name = d['name']

        min = literal_eval(min)
        if max == 'inf':
            max = None
        else:
            max = literal_eval(max)
            
        tID = parent_tID + (idx,)
        assert tID not in tID2plain_info
        tID2plain_info[tID] = (case, refID, min, max, name)
        return

    
    ID, = tag
    tID = parent_tID + (ID,)
    assert tID not in tID2plain_info
    if case == 'Token':
        attrs = ls
        d = _get_attrs_of_Token(attrs)
        token_type = d['type']

        tID2plain_info[tID] = (case, token_type)
        return

    children = ls
    
    if case == 'List':
        name_Item = ('Item',)
        if not all(name_Item == name for name, tag, _ in children):
            raise ValueError('not all List children are Item')
        
        data = len(children)

    elif case == 'Block':
        name_Item = ('Item',)
        if any(name_Item == name for name, tag, _ in children):
            raise ValueError('some Block children are Item')

        data = tuple(sorted(ID for name, (ID,), _ in children))
        assert len(data) == len(set(data))
        
    if case in {'Block', 'List'}:
        if len(children) == 0:
            raise ValueError('len(children) == 0')

        tID2plain_info[tID] = (case, data)
        _children_to_tID2plain_info(tID, tID2plain_info, children)
        
    else:
        raise logic-error-unknown-case
    pass

        
        
    
def id_info2parse_result_EPL(info):
    ID = info.ID
    case = info.define_type
    name = (case,)
    tag = (ID,)
    if case == 'Token':
        token_type = info.token_type
        child = (('.', 'type'), (token_type,), [])
        ls = [child]
    elif case in {'Block', 'List'}:
        children = info.children
        ls = [id_info2parse_result_EPL(c) for c in children]
    elif case == 'Item':
        tag = ()
        #print(type(info.refID))
        if type(info.refID) == str:
            refID_tag = (info.refID,)
        else:
            # if tID
            raise not-tID
            assert type(info.refID) == tuple
            refID_tag = info.refID

        
        argname = info.key
        keytag = () if argname is None else (argname,)

        
        refID = (('.', 'refID'), refID_tag, [])
        min = (('.', 'min'), (str(info.min),), [])
        max = (('.', 'max'), (str(info.max),), [])
        key = (('.', 'name'), keytag, [])
        ls = [refID, min, max, key]
    else:
        raise logic-error

    return (name, tag, ls)

from MyLL1L.Parser_MyLL1L_of_XL import calc_tIDDict_MyLL1L_of_XL
from ETL.ETL_in_MyLL1L import ETL_in_MyLL1L
from EPL.pretty_format_EPL import pretty_format_EPL, parse_result2indent_EPL

tIDDict = calc_tIDDict_MyLL1L_of_XL(ETL_in_MyLL1L)
#print('tIDDict', tIDDict)
r = tIDDict2parse_result_EPL(tIDDict)
print(r)
s = parse_result2indent_EPL(r)
print(s)
d = parse_result_EPL_to_tID2plain_info(r)
print(d)

'''





tID to info
Token type
Item refID min max :name

auto fill:
List len
Block children's name



plain form:
[plain form tID to info /* only Token and Item */
    [Token
        [. type] xxx
    ] tID of a Token
    
    [Item
        [. refID] the refID of this Item
        [. min] xxx
        [. max] xxx
        [. name] xxx
    ] tID of a Item

]

tree form:
[tree form tID to info
    [Block
        /* children */
    ] ID

    [List
        /* Item children */
        [Item
            [. refID] the refID of this Item
            [. min] xxx
            [. max] xxx
            [. name] xxx
        ] /* nothing here */
    ] ID

    
    [Token
        [. type] xxx
    ] ID
]

complete plain form:
[complete plain form tID to info
    [Token
        [. type] xxx
    ] tID of a Token
    
    [Item
        [. refID] the refID of this Item
        [. min] xxx
        [. max] xxx
        [. name] xxx
    ] tID of a Item

    [Block
        [. children] ID...
    ] tID of a Block
    
    [List
        [. length] xxx
    ] tID of a List
]
'''
