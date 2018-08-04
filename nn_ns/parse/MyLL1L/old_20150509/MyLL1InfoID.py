
lang_MyLL1 = r'''
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

name = B
n = B
id = B
token = B
B is t'B'

newline is t'\n'
intent is t'\t'
unintent is t'\b'
'''

'''
child of IDBlock can be IDBlock or IDList or IDToken, but not IDItem
child of IDList is IDItem
IDItem and IDToken have no children


disjoint rule:
for each IDBlock, all FIRST(child) disjoint
for each IDItem I that min < max, FIRST(refID of I) disjoint with FOLLOW(I)


FIRST FOLLOW depenancy:
b <- a : means a should be evaluated first
for IDItem I:
    FIRST(I) <- FIRST(refID of I)
    FOLLOW(refID of I) <- FOLLOW(I)
for IDList L:
    FIRST(L) <- FIRST(child) for child in children from left to right until child not nullable
    FOLLOW(child) <- FOLLOW(L) if child is the last one
                  <- FIRST(next child) elif next child is not nullable
                  <- FIRST(next child) union FOLLOW(next child) otherwise
for IDBlock B:
    FIRST(B) <- FIRST(child) for each child
    FOLLOW(child) <- FOLLOW(B) for each child


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

from functools import reduce
import operator
import re

FIRST = 'FIRST'
FOLLOW = 'FOLLOW'
#TTYPES = 'TTYPES' # token_type

'''
match result:
# tID        : tIDDict not contained
# begin, end : tokens not contained
# children   : None - leaf IDToken ; [] - 0 matchs  IDItem min==0
# ns         : free for user // namespace
(tID, (begin, end), children, ns)
'''



class ChildrenMixin:
    
    def isLeaf(self):
        return self.children == None
    def __bool__(self):
        raise NotImplementedError('not bool')
    def __len__(self):
        return len(self.children)
    
    def __iter__(self):
        return iter(self.children)
    def __getitem__(self, i):
        if isinstance(i, str):
            r = self._getitem_str(i)
        elif isinstance(i, tuple):
            r = self._getitem_tuple(i)
        else:
            r = self._getitem(i)
        return r
    def _getitem(self, i):
        return self.children[i]
    def _getitem_str(self, s):
        raise NotImplementedError('_getitem_str')
    
    def _getitem_tuple(self, t):
        r = self
        for e in t:
            r = r[e]
        return r
    

    def set_children(self, children):
        self._set_children(children)
        return
    def _set_children(self, children):
        self.children = children
        return

class Namespace:
    def __lshift__(self, ns):
        assert isinstance(ns, Namespace)
        self.__dict__ = ns.__dict__
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    def __ne__(self, other):
        return not (self.__dict__ == other.__dict__)
    def __repr__(self):
        return '<{!r}>'.format(self.__dict__)
'''
a = Namespace()
b = Namespace()
a << b
b.afass = ''
print(a)
assert a == b
'''


class MatchFail(ValueError):pass

def make_match_result(tID, begin_end, children):
    begin, end = begin_end
    return (tID, begin_end, children, Namespace())

def getMatchResultRng(match_result):
    return match_result[1]

class MatchResultExplain(ChildrenMixin):
    def __init__(self, match_result, tIDDict, tokens):
        self.r = match_result
        self.tID, (self.begin, self.end), self.children, self.ns = match_result
        self.d = tIDDict
        self.ls = tokens

        self.ID = self.tID[-1]
        self.info = info = tIDDict[self.tID]
        self.define_type = info.define_type
        self.name2idx = None
        if isinstance(info, InfoIDNamedChildren):
            self.name2idx = info.name2idx

    def __repr__(self):
        return repr(self.match_result)
    def _getitem(self, i):
        r = super()._getitem(i)
        return MatchResultExplain(r, self.d, self.ls)
        
    def _getitem_str(self, s):
        i = self.name2idx[s]
        return self[i]

        
class InfoID(ChildrenMixin):
    def __init__(self, define_type, ID, *, tID = None, children = None):
        super().__init__()
        self.define_type = define_type
        self.ID, self.tID = ID, tID
        self.set_children(children)
        self.first = None
        self.id2info = None
        return

    # tID is (ID,) or (...parentID, ID)
    # ftID is (f, tID) where f is 'FIRST' or 'FOLLOW' => fstID, fwtID
    #         xxx error : f can be 'TTYPES' too
    # FRef is a set of ftID
    # FirstRef is FRef, indicate how to make up First
    # FollowRef is is FRef, indicate how to make up Follow
    def getDisjointRules(self):return [] # list of FRef
    def getPreKnownFirst(self):return set() # set of token_type
    def getFirstRef(self):return set()
    def exportFollowRef(self, fwtID2FollowRef):pass
    def set_FIRST(self, first):# first: set of token_type
        self.first = first
        return
    def set_id2info(self, id2info): # id2info[ID] = InfoID
        self.id2info = id2info
        return
        
    def isInFirst(self, token):
        return token.type in self.first
    def make_match_result(self, begin_end, children):
        return make_match_result(self.tID, begin_end, children)
    
    def match(self, tokens, begin, end):
        return self._match(tokens, begin, end)
    def _match(self, tokens, begin, end):
        raise NotImplementedError('_match')

    def getStrName(self):
        # may not ID!! ID may be number
        r = self._getStrName()
        assert r == None or isinstance(r, str)
        return r
    
    def _getStrName(self):
        return self.ID
        

    def nullable(self):
        return self._nullable()
    def _nullable(self, s):
        raise NotImplementedError('_nullable')


    def set_tID(self, tID):
        assert tID[-1] == self.ID
        assert isinstance(tID, tuple)
        self.tID = tID
        return

class InfoIDKnownDefineType(InfoID):
    def _get_define_type(self):
        raise NotImplementedError()
        return
class InfoIDLeaf(InfoID):
    def _set_children(self, children):
        assert children == None
        super()._set_children(children)
        return

class InfoIDToken(InfoIDLeaf):
    def __init__(self, token_type, ID, *, tID = None, children = None):
        self.token_type = token_type
        super().__init__('Token', ID, tID = tID, children = children)
        return

    def set_FIRST(self, first):# first: set of token_type
        assert first == None or len(first) == 1
        if len(first) == 1:
            t, = first
            assert t == self.token_type
        super().set_FIRST(first)
        return
    
    def _match(self, tokens, begin, end):
        if begin >= end:
            raise MatchFail('begin >= end')
        t = tokens[begin]
        if not self.isInFirst(t):
            raise MatchFail('not isInFirst pos:{}, token:{}'.format(begin, t))

        begin_end = begin, begin+1
        r = self.make_match_result(begin_end, None)
        
        return r
    
    def getPreKnownFirst(self):
        return {self.token_type}
    
    def _nullable(self):
        return False


class InfoIDItem(InfoIDLeaf):
    def __init__(self, ID, refID, min, max, *, key = None, tID = None, children = None):
        assert isinstance(ID, int)
        
        self.refID = refID
        self.min, self.max = min, max
        self.key = key # name in list

        tIDofRefID = (self.refID,)
        self.fs_tRefID = (FIRST, tIDofRefID)
        self.fw_tRefID = (FOLLOW, tIDofRefID)
        
        super().__init__('Item', ID, tID = tID, children = children)
        return
    
    def _match(self, tokens, begin, end):
        if begin >= end:
            if not self.nullable():
                raise MatchFail('begin >= end')
            r = self.make_match_result((begin, begin), [])
            return r
        
        t = tokens[begin]
        old_begin = begin
        children = []
        info = self.id2info[self.refID]
        while self.isInFirst(t) and len(children) < self.max:
            r = info.match(tokens, begin, end)
            _beg, _end = getMatchResultRng(r)
            if not begin == _beg < _end <= end:
                print(begin, _beg, _end, end, tokens[begin])
            assert begin == _beg < _end <= end

            children.append(r)
            begin = _end
            if begin == end:
                break
            t = tokens[begin]
            
        if not self.min <= len(children) <= self.max:
            raise MatchFail('pos:{} count error:not min={} <= len={} <= max= {}'\
                            .format(begin, self.min, len(children), self.max))

        begin_end = old_begin, begin
        r = self.make_match_result(begin_end, children)
        
        return r
    
    def getDisjointRules(self):# list of FRef
        s = set()
        if not self.exact():
            s.add(self.fs_tRefID)
            
            me = self.tID
            s.add((FOLLOW, me))
        return [s]
        
    #def getPreKnownFirst(self):return set() # set of token_type
    def getFirstRef(self):
        return {self.fs_tRefID}
    
    def exportFollowRef(self, fwtID2FollowRef):
        s = fwtID2FollowRef[self.fw_tRefID]
        me = self.tID
        s.add((FOLLOW, me))
        return
    
    def _getStrName(self):
        return self.key
    def _nullable(self):
        return self.min == 0
    def exact(self):
        return self.min == self.max
    
class InfoIDNamedChildren(InfoID):
    def __init__(self, define_type, ID, *, tID = None, children = None):
        self.name2idx = None
        super().__init__(define_type, ID, tID = tID, children = children)
        return
    def _set_children(self, children):
        super()._set_children(children)
        if children == None:
            self.name2idx = None
        else:
            self.name2idx = {}
            for i, child in enumerate(children):
                name = child.getStrName()
                if name == None:
                    continue
                if name in self.name2idx:
                    raise Exception('duplicate name: {!r}'.format(name))
                self.name2idx[name] = i
                
        return
    
    def _getitem_str(self, s):
        i = self.name2idx[s]
        return self[i]

class InfoIDList(InfoIDNamedChildren):
    def __init__(self, ID, *, tID = None, children = None):
        super().__init__('List', ID, tID = tID, children = children)
        return
    
    def _match(self, tokens, begin, end):
        if begin >= end:
            raise MatchFail('begin >= end')
        
        t = tokens[begin]
        old_begin = begin
        children = []
        for c in self:
            r = c.match(tokens, begin, end)
            _beg, _end = getMatchResultRng(r)
            assert begin == _beg <= _end <= end
            if not c.nullable():
                assert _beg < _end

            children.append(r)
            begin = _end

        begin_end = old_begin, begin
        r = self.make_match_result(begin_end, children)
        
        return r

    
    #def getDisjointRules(self):# list of FRef
    #def getPreKnownFirst(self):return set() # set of token_type
    def getFirstRef(self):
        s = set()
        for c in self:
            first_child = (FIRST, c.tID)
            s.add(first_child)
            if not c.nullable():
                break
        else:
            raise cant-go-here
        
        return s
    
    def exportFollowRef(self, fwtID2FollowRef):
        follow_me = (FOLLOW, self.tID)
        for i, c in enumerate(self):
            follow_child = (FOLLOW, c.tID)
            s = fwtID2FollowRef[follow_child]

            if i == len(self) - 1: #last one
                s.add(follow_me)
            else:
                nextc = self[i+1]
                first_next = (FIRST, nextc.tID)
                follow_next = (FOLLOW, nextc.tID)
                s.add(first_next)
                if nextc.nullable():
                    s.add(follow_next) # because this no string ID InfoIDItem occur here only

        return


    def _nullable(self):
        if not self.children:
            return True
        nullable = reduce(operator.and_, (c.nullable() for c in self.children)) # all
        return nullable
    
class InfoIDBlock(InfoIDNamedChildren):
    def __init__(self, ID, *, tID = None, children = None):
        super().__init__('Block', ID, tID = tID, children = children)
        return
    
    def _match(self, tokens, begin, end):
        if begin >= end:
            raise MatchFail('begin >= end')
        
        t = tokens[begin]
        for c in self:
            if c.isInFirst(t):
                r = c.match(tokens, begin, end)
                begin_end = getMatchResultRng(r)
                r = self.make_match_result(begin_end, [r])
                return r

        
        if not self.isInFirst(t):
            raise MatchFail('not isInFirst pos:{}, token:{}'.format(begin, t))
        raise cant-go-here
    


    
    def getDisjointRules(self):# list of FRef
        s = self.getFirstRef()
        return [s]
        
    #def getPreKnownFirst(self):return set() # set of token_type
    def getFirstRef(self):
        s = set()
        for c in self:
            first_child = (FIRST, c.tID)
            s.add(first_child)
        return s
    
    def exportFollowRef(self, fwtID2FollowRef):
        follow_me = (FOLLOW, self.tID)
        for c in self:
            follow_child = (FOLLOW, c.tID)
            s = fwtID2FollowRef[follow_child]
            s.add(follow_me)
        return
    
    def _nullable(self):
        if not self.children:
            return True
        nullable = reduce(operator.or_, (c.nullable() for c in self.children)) # any
        return nullable


##################################################










