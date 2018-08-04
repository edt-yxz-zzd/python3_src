from MyLL1InfoID import *


def _toCount(min=None, max=None):
    inf = float('inf')
    if max == None:
        if min == None:
            return (1, 1)
        elif isinstance(min, str):
            assert min in '?*+'
            d = {'?': (0, 1), '*': (0, inf), '+': (1, inf), }
            return d[min]
        max = inf

    
    assert 0 <= min
    assert isinstance(min, int)
    
    return (min, max)

def toCount(min = None, max = None):
    if isinstance(min, tuple):
        assert max == None
        return _toCount(*min)
    else:
        return _toCount(min, max)
    
def toInfoIDItem(ID, refID, min = (), max = None, *, name = None):
    min, max = toCount(min, max)
    return InfoIDItem(ID, refID, min, max, key = name)
def toInfoIDList(ID, idcount_name_ls):
    #print(idcount_name_ls)
    items = [toInfoIDItem(i, *idcount, name=name) for i, (idcount, name) in enumerate(idcount_name_ls)]
    return InfoIDList(ID, children = items)

def toInfoIDBlock(ID, children):
    return InfoIDBlock(ID, children = children)

def toIDList(ID, *idcount_name_ls):return toInfoIDList(ID, idcount_name_ls)
def toIDBlock(ID, *children):return toInfoIDBlock(ID, children)
def toIDToken(ID, token_type):
    assert re.match('t["\']', token_type)
    token_type = eval(token_type[1:])
    assert isinstance(token_type, str)
    
    return InfoIDToken(token_type, ID)


def gen_MyLL1_raw_id2info():
    d = {}
    def add(info):
        ID = info.ID
        assert ID not in d
        d[ID] = info
        return
    add(toIDList('MyLL1', [('rex',), None]))
    add(toIDList('rex', [('id_define', '+'), None]))
    add(toIDList('id_define', [('id',), None], [('define',), None]))

    _define_newline = toIDList('define_newline', [('inline_define',), None], [('newline',), None])
    _newline_block = toIDList('newline_block', [('newline',), None], [('block',), None])
    add(toIDBlock('define', _define_newline, _newline_block))

    _is_token = toIDList('is_token', [("'is'",), None], [('token',), 'type'])
    _eq_list = toIDList('eq_list', [("'='",), None], [('list',), 'ls'])
    add(toIDBlock('inline_define', _is_token, _eq_list))

    add(toIDList('block', [('intent',), None], [('subrex',), None], [('unintent',), None]))

    add(toIDList('subrex', [('id_define', 2), None]))
    add(toIDList('list', [('item',), None], [(',item', '*'), None]))
    add(toIDList(',item', [("','",), None], [('item',), None]))
    add(toIDList('item', [('id_count',), 'id_count'], [('name', '?'), 'name']))
    add(toIDList('id_count', [('id',), 'id'], [('count', '?'), 'count']))

    _count = toIDList("'{}'", [("'{'",), None], \
                      [('n',), 'min'], [("','",), None], [('n', '?'), 'max'], \
                      [("'}'",), None])

    add(toIDBlock('count', _count,
                  toIDToken("'?'", "t'?'"),
                  toIDToken("'*'", "t'*'"),
                  toIDToken("'+'", "t'+'")))

    add(toIDToken("','", "t','"))
    add(toIDToken("'{'", "t'{'"))
    add(toIDToken("'}'", "t'}'"))
    add(toIDToken("'is'", "t'is'"))
    add(toIDToken("'='", "t'='"))

    add(toIDList('name', [('B',), None]))
    add(toIDList('n', [('B',), None]))
    add(toIDList('id', [('B',), None]))
    add(toIDList('token', [('B',), None]))
    add(toIDToken('B', "t'B'"))
                  

    add(toIDToken('newline', r"t'\n'"))
    add(toIDToken('intent', r"t'\t'"))
    add(toIDToken('unintent', r"t'\b'"))

    raw_id2info = result1_InfoDict = d
    del add, d

    return raw_id2info



