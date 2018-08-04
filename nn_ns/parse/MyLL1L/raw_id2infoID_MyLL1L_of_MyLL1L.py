
from .tools_for_raw_id2infoID_MyLL1L import *
from .MyLL1L_in_MyLL1L import mainID_MyLL1L_of_MyLL1L

def build_raw_id2infoID_MyLL1L_of_MyLL1L():
    d = {}
    def add(info):
        ID = info.ID
        assert ID not in d
        d[ID] = info
        return
    add(toIDList(mainID_MyLL1L_of_MyLL1L, [('rex',), None]))
    add(toIDList('rex', [('id_define', '+'), None]))
    add(toIDList('id_define', [('id',), None], [('define',), None]))

    _define_newline = toIDList('define_newline', [('inline_define',), None], [('newline',), None])
    _newline_block = toIDList('newline_block', [('newline',), None], [('block',), None])
    add(toIDBlock('define', _define_newline, _newline_block))

    _is_token = toIDList('is_token', [("'is'",), None], [('token',), 'type'])
    _eq_list = toIDList('eq_list', [("'='",), None], [('list',), 'ls'])
    add(toIDBlock('inline_define', _is_token, _eq_list))

    add(toIDList('block', [('indent',), None], [('subrex',), None], [('dedent',), None]))

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
    add(toIDToken('indent', r"t'\t'"))
    add(toIDToken('dedent', r"t'\b'"))

    raw_id2info = result1_InfoDict = d
    del add, d

    return raw_id2info # to be filled

