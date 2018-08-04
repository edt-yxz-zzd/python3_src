
'''
# this is a comment
# not allow nullable => FIRST
#
MyLL1 = rex
rex = id_define +
id_define = id , define

define
    define_newline = inline_define , newline
    newline_block = newline , block
    
inline_define
    is_token = 'is' , token type
    eq_list = '=' , list ls

block = intent , subrex , unintent
subrex = id_define { 2 , }

list = item , ,item *
,item = ',' , item # ',item' is an id
item = id_count id_count , name ? name
id_count = id id , count ? count
count
    '?' is t'?' # means token.type == '?'
    '*' is t'*'
    '+' is t'+'
    '{}' = '{' , n min , ',' , n ? max , '}' # result_node[1] is result_node['min'], result_node['max'] is a list of len 1 or 0

',' is t',' # "','" is an id
'{' is t'{'
'}' is t'}'
'=' is t'='
'is' is t'is'

n = B
id = B
token = B
B is t'B'

newline is t'\n'
intent is t'\t'
unintent is t'\b'
'''

'''
FIRST FOLLOW:
id1
    id2
    id3
    
id1 = id2{0,x} id3
id1 = id4 id2{0,x} id3
id1 = id2 id2{0,x} id3
id1 = id2{y,x!=y} id3

id1 = id2{y,x!=y} # FIRST(id2) & FOLLOW(id1) == {}
id4
    id5 = id1 id3

FIRST(id2) & FIRST(id3) == {}
'''
from itertools import chain
from functools import reduce
import operator
import re
from root.graph_data.directed_acyclic_graph import reversed_topological_ordering

class InfoID:
    def __init__(self, define_type, ID, *, tID = None, children = None):
        self.define_type = define_type
        self.ID, self.tID = ID, tID
        self.set_children(children)
        self.__first_token_types = None
        return

    def nullable(self):
        return self._nullable()

    def first_token_types(self, id2first_tokens=None):
        if self.__first_token_types != None:
            return self.__first_token_types, set()
        r = self._first_token_types(id2first_tokens)
        first_token_types, first_IDs = r
        if not first_IDs:
            self.__first_token_types = first_token_types
        if id2first_tokens != None:
            assert self.__first_token_types != None
        return r
    

    def isLeaf(self):
        return self.children == None
    def __iter__(self):
        return iter(self.children)
    def __getitem__(self, i):
        return self.children[i]
    
    def set_tID(self, tID):
        assert tID[-1] == self.ID
        assert isinstance(tID, tuple)
        self.tID = tID
        return

    def set_children(self, children):
        self.children = children
        return

class InfoItem:
    def __init__(self, ID, min, max, *, key = None):
        self.ID, self.min, self.max = ID, min, max
        self.key = key # name in list
        return
    def nullable(self):
        return self.min == 0

class InfoIDList(InfoID):
    def __init__(self, ID, *, tID = None, children = None):
        self.name2idx = None
        super().__init__('List', ID, tID = tID, children = children)
        return

    def _nullable(self):
        if not self.children:
            return True
        nullable = reduce(operator.and_, (c.nullable() for c in self.children)) # all
        return nullable

    def _first_token_types(self, id2first_tokens=None):
        if self.nullable():
            raise Exception('calc first() but nullable')
        first_token_types = set()
        first_IDs = set()
        for c in self.children:
            ID = c.ID
            if ID in first_IDs:
                raise Exception('{!r} duplicate first: {!r}'.format(self.ID, ID))
            first_IDs.add(ID)
            if not c.nullable():
                break
        else:
            raise cant-go-here
        
        if self.ID in first_IDs:
            raise Exception('{!r} first() contains self'.format(self.ID))

        
        if id2first_tokens:
            for ID in first_IDs:
                token_types = id2first_tokens[ID]
                if first_token_types & token_types:
                    raise 'first() {!r} @{!r}'.format(token_types, self.ID)
                first_token_types |= token_types
            first_IDs = set()
        return first_token_types, first_IDs
    def set_children(self, children):
        super().set_children(children)
        if children == None:
            self.name2idx = None
        else:
            self.name2idx = {}
            for i, item in enumerate(children):
                key = item.key
                if key == None:
                    continue
                if key in self.name2idx:
                    raise Exception('duplicate name: {!r}'.format(key))
                self.name2idx[key] = i
                
        return

    def __getitem__(self, i):
        if isinstance(i, str):
            i = self.name2idx[i]
        return super().__getitem__(i)
    
class InfoIDBlock(InfoID):
    def __init__(self, ID, *, tID = None, children = None):
        self.name2idx = None
        super().__init__('Block', ID, tID = tID, children = children)
        return

    def _nullable(self):
        if not self.children:
            return True
        nullable = reduce(operator.or_, (c.nullable() for c in self.children)) # any
        return nullable

    def _first_token_types(self, id2first_tokens=None):
        if self.nullable():
            raise Exception('calc first() but nullable')
        first_token_types = set()
        first_IDs = set()
        for c in self.children:
            token_types, IDs = c.first_token_types(id2first_tokens)
            if (first_token_types & token_types) or (first_IDs & IDs):
                raise Exception('{!r} first() contains some elements of other children first()'.format(c.tID))
            first_token_types |= token_types
            first_IDs |= IDs
        if self.ID in first_IDs:
            raise Exception('{!r} first() contains self'.format(self.ID))

        if id2first_tokens:
            for ID in first_IDs:
                token_types = id2first_tokens[ID]
                if first_token_types & token_types:
                    raise 'first() {!r} @{!r}'.format(token_types, self.ID)
                first_token_types |= token_types
            first_IDs = set()
        return first_token_types, first_IDs
    
    def set_children(self, children):
        super().set_children(children)
        if children == None:
            self.name2idx = None
        else:
            self.name2idx = {}
            for i, item in enumerate(children):
                key = item.ID
                assert key
                if key in self.name2idx:
                    raise Exception('duplicate ID: {!r}'.format(key))
                self.name2idx[key] = i
                
        return

    def __getitem__(self, i):
        if isinstance(i, str):
            i = self.name2idx[i]
        return super().__getitem__(i)


class InfoIDToken(InfoID):
    def __init__(self, token_type, ID, *, tID = None, children = None):
        self.token_type = token_type
        super().__init__('Token', ID, tID = tID, children = children)
        return
    

    def _first_token_types(self, id2first_tokens=None):
        first_token_types = {self.token_type}
        first_IDs = set()
        return first_token_types, first_IDs
    
    def _nullable(self):
        return False
    
    def set_children(self, children):
        if children != None:
            raise Exception('InfoIDToken has no children')
        super().set_children(children)
        return

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
    
def toInfoItem(ID, min = (), max = None, *, name = None):
    min, max = toCount(min, max)
    return InfoItem(ID, min, max, key = name)
def toInfoIDList(ID, idcount_name_ls):
    items = [toInfoItem(*idcount, name=name) for idcount, name in idcount_name_ls]
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

add(toIDList('n', [('B',), None]))
add(toIDList('id', [('B',), None]))
add(toIDList('token', [('B',), None]))
add(toIDToken('B', "t'B'"))
              

add(toIDToken('newline', r"t'\n'"))
add(toIDToken('intent', r"t'\t'"))
add(toIDToken('unintent', r"t'\b'"))

result1_InfoDict = d
del add, d


def fix_tID(parent_tID, infoID, add):
    tID = tuple(chain(parent_tID, [infoID.ID]))
    add(tID, infoID)
    if infoID.define_type == 'Block':
        for child in infoID:
            fix_tID(tID, child, add)
    return
            
def result1_InfoDict2tIDDict(result1_InfoDict):
    tIDDict = {}
    def add(tID, infoID):
        assert infoID.tID == None
        assert tID not in tIDDict
        infoID.set_tID(tID)
        tIDDict[tID] = infoID
        return
    tID = ()
    for ID, item in result1_InfoDict.items():
        fix_tID(tID, item, add)

    result2_InfoDict = result1_InfoDict
    return tIDDict, result2_InfoDict
            
result2_tIDDict, result2_InfoDict = result1_InfoDict2tIDDict(result1_InfoDict)
def check_nullable(result2_InfoDict):
    for ID, item in result2_InfoDict.items():
        if item.nullable():
            raise Exception('ID {!r} is nullable'.format(ID))
    return
    
check_nullable(result2_InfoDict)

def calc_id2first_tokens(result2_InfoDict):
    ID_first = [(ID, info.first_token_types()) for ID, info in result2_InfoDict.items()]
    ID_first.sort()
    allID = list(result2_InfoDict)
    allID.sort()
    for ID, (_ID, _) in zip(allID, ID_first):
        assert ID == _ID
        
    ID2idx = dict((ID, i) for i, ID in enumerate(allID))

    u2vtc = [None] * len(allID)
    for ID, (_, first_IDs) in ID_first:
        u = ID2idx[ID]
        
        ls = [ID2idx[ID] for ID in first_IDs]
        u2vtc[u] = ls

    for vtc in u2vtc:
        assert vtc != None
        
    r = reversed_topological_ordering(u2vtc)
    if r == None:
        raise Exception('cycle depency')

    idx2first_tokens = [None] * len(allID)
    for i in r:
        assert idx2first_tokens[i] == None
        idx2first_tokens[i] = s = set()
        ID = allID[i]
        for j in u2vtc[i]:
            tokens = idx2first_tokens[j]
            assert tokens != None
            if s & tokens:
                raise 'first not unique'
            s |= tokens
        tokens = ID_first[i][-1][0]
        if s & tokens:
            raise 'first not unique'
        s |= tokens
        assert s
    return dict(zip(allID, idx2first_tokens))



id2first_tokens = calc_id2first_tokens(result2_InfoDict)
_fresh = [(ID, info.first_token_types(id2first_tokens)) for ID, info in result2_InfoDict.items()]



            
    


class NodeMyLL1:
    def __init__(self, name, *, tname = None, parent = None, children = None):
        self.name, self.tname, self.parent, self.children = \
                   name, tname, parent, children
        return

    def isLeaf(self):
        return self.children == None
    def set_tname(self, tname):
        assert tname[-1] == self.name
        assert isinstance(tname, tuple)
        self.tname = tname
        return

class List(NodeMyLL1):
    def __init__(self, ls, *args, **kwargs):
        self.ls = ls
        super().__init__(*args, **kwargs)
        return
    










