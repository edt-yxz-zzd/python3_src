

class RexParser:
    def __init__(self):
        id = MatchForRexParserToken('id')
        num = MatchForRexParserToken('num')
        plain_str = MatchForRexParserToken('plain_str')
        rex_str = MatchForRexParserToken('rex_str')
        comment_str = MatchForRexParserToken('comment_str')
        assign = MatchForRexParserToken('spiecial_char', data = '=')
        left_small_bracket = MatchForRexParserToken('spiecial_char', data = '(')
        right_small_bracket = MatchForRexParserToken('spiecial_char', data = ')')
        left_big_bracket = MatchForRexParserToken('spiecial_char', data = '{')
        comma = MatchForRexParserToken('spiecial_char', data = ',')
        right_big_bracket = MatchForRexParserToken('spiecial_char', data = '}')
        star = MatchForRexParserToken('spiecial_char', data = '*')
        plus = MatchForRexParserToken('spiecial_char', data = '+')
        left_mid_bracket = MatchForRexParserToken('spiecial_char', data = '[')
        right_mid_bracket = MatchForRexParserToken('spiecial_char', data = ']')
        choice_char = MatchForRexParserToken('spiecial_char', data = '|')

        rex = MatchEq('rex', None)
        idDefine = MatchSequence('idDefine', [id, assign, rex])
        line = MatchSequence('line', [MatchOptional('_', idDefine), MatchOptional('_', comment_str)])

        multi_optional = MatchSequence('multi_optional', [left_mid_bracket, rex, right_mid_bracket])
        group = MatchSequence('group', [left_small_bracket, rex, right_small_bracket])
        basic_rex = MatchChoices('basic_rex', [plain_str, rex_str, id, group, multi_optional])

        multi_bound = MatchSequence('multi_bound', \
                                    [basic_rex, left_big_bracket, num, comma, \
                                     MatchOptional('_', num), right_big_bracket])
        multi_star = MatchSequence('multi_star', [basic_rex, star])
        multi_plus = MatchSequence('multi_plus', [basic_rex, plus]) 
        multi = MatchChoices('multi', [basic_rex, multi_bound, multi_star, multi_plus,])
        
        seq = MatchPlus('seq', multi)
        choices = MatchSequence('choices', \
                                [seq, MatchStar('_', MatchSequence('_', [choice_char, seq]))])
        rex.__init__('rex', choices)


        ls = list(locals().keys())
        #ls.sort()
        #self.match_fs = {name : locals()[name] for name in ls}
        match_fs = {}
        for name in ls:
            match_fs[name] = locals()[name]

        self.match_fs = match_fs
        
        return

    def idDefine2init_assign(self, idDefineResult):
        assert idDefineResult.name == 'idDefine'

        assert len(idDefineResult.data) == 3
        id = idDefineResult.data[0]
        assert id.name == 'token'
        id = id.data
        assert type(id) == str

        rexResult = idDefineResult.data[-1]
        assignRightHand = self.rexResult2MatchPatternConstruct(rexResult)
        
        choicesResult = rexResult.data
        
            
    def parser(self, string):
        tk = RexTokener()

        ls = []
        match = self.match_fs['line']
        for i, line in enumerate(tk.tokenize(string)):
            r = match(line, 0, len(line))
            if r == None:
               raise Exception('parser fail at {}th line'.format(i))
            ls.append(r)

        for 
        return ls
    
 
class RexTokener:
    id = 'id'
    num = 'num'
    plain_str = 'plain_str'
    rex_str = 'rex_str'
    comment_str = 'comment_str'
    spaces = 'spaces'
    spiecial_char = 'spiecial_char'
    
    def __init__(self):
        self.special_chars = '#=(){,}*+[]|"\''
        self.plain_str_prefixes = ['r"', "r'", '"', "'"]
        self.rex_str_prefixes = ['rex"', 'rrex"', "rex'", "rrex'"]
        self.str_prefixes = self.plain_str_prefixes + self.rex_str_prefixes

        return

    
    def isSpecialChar(self, c):
        return c in self.special_chars
    def getStrPrefixes(self):
        return self.str_prefixes
    
    def matchID(self, string, start, end):
        if start != 0:
            c = string[start-1]
            if not (c.isspace() or self.isSpecialChar(c)):
                return None
            
        if start == end:
            return None
        c = string[start]
        if c.isspace() or self.isSpecialChar(c) or c.isdigit():
            return None
        
        for pre in self.getStrPrefixes():
            if string.startswith(pre, start, end):
                return None
            
        for i in range(start, end):
            c = string[i]
            if c.isspace() or self.isSpecialChar(c):
                if c in '\'"':
                    return None
                break
        else:
            i = end

        if not 0 <= start < i <= end:
            print(start, i, end)
        assert 0 <= start < i <= end

        return MatchResult(string, start, i, type=self.id, data = string[start:i])

    def matchNum(self, string, start, end):
        if start != 0:
            c = string[start-1]
            if not (c.isspace() or self.isSpecialChar(c)):
                return None
            
        if start == end or not string[start].isdigit():
            return None
        
            
        for i in range(start, end):
            c = string[i]
            if not c.isdigit():
                if c.isspace() or self.isSpecialChar(c):
                    break
                return None
        else:
            i += 1
        assert 0 <= start < i <= end

        num = int(string[start:i])
        return MatchResult(string, start, i, type=self.num, data = num)
    
    def matchStr(self, string, start, end):
        if start != 0:
            c = string[start-1]
            if not (c.isspace() or self.isSpecialChar(c)):
                return None

        for pre in self.getStrPrefixes():
            if string.startswith(pre, start, end):
                break
        else:
            return None

        close_char = pre[-1]
        name = self.rex_str if len(pre) >= 4 else self.plain_str
        is_raw_str = len(pre) in [2, 5]
        

        old_start = start
        str_start = start + len(pre)-1
        escaping = False
        for i in range(str_start+1, end):
            c = string[i]
            if c == '\\':
                escaping = not escaping
            elif c == close_char and not escaping:
                break
        else:
            return None
        i += 1
        str_end = i
        assert 0 <= str_start < str_end-1 < str_end <= end
        s = string[str_start : str_end]
        if is_raw_str:
            s = 'r' + s
        s = eval(s)

        return MatchResult(string, old_start, str_end, type=name, data = s)

    def matchSpecialCharExceptCommentChar(self, string, start, end):
        if start == end or string[start] == '#':
            return None
        
        c = string[start]
        if not self.isSpecialChar(c):
            return None
        
        return MatchResult(string, start, start+1, type=self.spiecial_char, data = c)
    
    def matchComment(self, string, start, end):
        if start == end or not string[start] == '#':
            return None
        
        return MatchResult(string, start, end, type=self.comment_str, data = string[start : end])
    
    def matchSpaces(self, string, start, end):
        if start == end or not string[start].isspace():
            return None
        
        for i in range(start, end):
            if not string[i].isspace():
                break
        else:
            i += 1

        return MatchResult(string, start, i, type=self.spaces, data = None)

    def matchOneToken(self, string, start, end):
        for f in [self.matchID, self.matchNum, self.matchStr, \
                  self.matchSpecialCharExceptCommentChar, \
                  self.matchComment, self.matchSpaces]:
            r = f(string, start, end)
            if r != None:
                return r
        return None
    
    def tokenize(self, string):
        for line in string.split('\n'):
            yield self.tokenizeLine(line)
        
    def tokenizeLine(self, line):
        line = line.strip()
        
        ls = []
        start = 0
        end = len(line)
        while True:
            r = self.matchOneToken(line, start, end)
            if r == None:
                if start != end:
                    raise ValueError('tokenizeLine fail')
                break
            if r.start == r.end:
                raise Exception('LogicError')

            if r.type == self.spaces or r.type == self.comment_str:
                # cast away
                pass
            else:
                ls.append(r)
            start = r.end

        return ls
    
            
            



class MatchForRexParserToken(MatchPattern):
    @staticmethod
    def default_factory():
        return MatchPattern('', [])
    
    def __init__(self, type, data=None):
        super().__init__('token')
        self.type = type
        self.data = data
        return
    
    def _match(self, tokens, start, end):
        if start == end:
            return None

        r = tokens[start]
        if r.type != self.type:
            return None
        if self.data != None and self.data != r.data:
            return None

        return MatchResult(tokens, start, start+1, type=None, data = r)
        

'''
def star_match(match_f, string, start, end):
    return repeat_match(match_f, string, start, end, min=0)
def plus_match(match_f, string, start, end):
    return repeat_match(match_f, string, start, end, min=1)

def optional_match(match_f, string, start, end):
    return repeat_match(match_f, string, start, end, min=0, max=1)


def choose_str(strs, string, start, end):
    assert len(strs)
    assert strs == sorted(strs)

    for prefix in reversed(strs):
        r = match_str(prefix, string, start, end)
        if r != None:
            break
    else:
        return None
    return MatchResult(r.string, r.start, r.end, type=choose_str, data=r)
'''

p = RexParser()
r = p.parser(rex_language)
#print(r)

