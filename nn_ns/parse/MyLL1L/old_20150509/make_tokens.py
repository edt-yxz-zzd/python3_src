'''
text = BEGIN token*  END
BEGIN = rrex'^'
END = rrex'$'

token = str | comment | block | spacesButNewline | newlines

block = rex'((?![\'"#])\\S)+'
spacesButNewline = rrex'((?!\n)\s)+'
newlines = rrex'(?m)\n+'
comment = rrex'#.*'
str = s_str | d_str | st_str | dt_str


s_str = rrex"'(?!'')([^'\\]|\\.)*'"
d_str = rrex'"(?!"")([^"\\]|\\.)*"'
st_str = rex"\'''((?!\''')([^\\\\]|\\n|\\\\.|\\\\\\n))*\'''"
dt_str = rex'\"""((?!\""")([^\\\\]|\\n|\\\\.|\\\\\\n))*\"""'

'''

import re

class Token:
    def __init__(self, case, pos, substring, *, value = None):
        #assert 0 <= begin <= end <= len(text)
        
        self.type = case
        self.substring = substring
        self.pos = pos
        self.value = value
        return

    def size(self):
        return len(self.substring)

    def begin(self):
        return self.pos
    def end(self):
        return self.pos + self.size()

    def __repr__(self):
        if self.value == None:
            return 'Token({case!r}, {pos}, {substring!r})'\
                   .format(case = self.type, pos = self.pos, \
                           substring = self.substring)
        return 'Token({case!r}, {pos}, {substring!r}, value={value!r})'\
               .format(case = self.type, pos = self.pos, \
                       substring = self.substring, value = self.value)


class MatchRex:
    def __init__(self, case, rex_pattern):
        self.type = case
        
        if isinstance(rex_pattern, str):
            rex_pattern = re.compile(rex_pattern)
        self.rex = rex_pattern
        
        return

    def match(self, text, begin, end):
        return self._match(text, begin, end)
    def _match(self, text, begin, end):
        m = self.rex.match(text, begin, end)
        if not m:
            return None
        
        start = m.start()
        if start == -1:
            assert m.end() == -1
            assert m.group() == ''
            start = end = begin
        else:
            assert start == begin
            assert begin <= m.end() <= end
            end = m.end()
            
        sub = text[begin : end]
        return Token(self.type, begin, sub)


def matchOneToken(matchs, text, begin, end):
    ls = []
    for f in matchs:
        r = f.match(text, begin, end)
        if r != None:
            ls.append(r)
    assert len(ls) < 2
    if not ls:
        return None
    r, = ls
    return r

class MatchRexList:
    def __init__(self, case, rex_ls):
        self.type = case
        self.fmatchs = [MatchRex(case, rex) for rex in rex_ls]
        return
    def match(self, text, begin, end):
        return matchOneToken(self.fmatchs, text, begin, end)
        


str_rex_ls = [
    r"'(?!'')([^'\\]|\\.)*'",
    r'"(?!"")([^"\\]|\\.)*"',
    "\'''((?!\''')([^\\\\]|\\n|\\\\.|\\\\\\n))*\'''",
    '\"""((?!\""")([^\\\\]|\\n|\\\\.|\\\\\\n))*\"""'
    ]
matchTokenStr = MatchRexList('str', str_rex_ls)

comment_rex = r'#.*'
matchTokenComment = MatchRex('comment', comment_rex)

block_rex = '((?![\'"#])\\S)+'
matchTokenBlock = MatchRex('block', block_rex)

spacesButNewline_rex = r'((?!\n)\s)+'
matchTokenSpacesButNewline = MatchRex('spacesButNewline', spacesButNewline_rex)

newlines_rex = r'(?m)\n+'
matchTokenNewlines = MatchRex('newlines', newlines_rex)
    
matchTokens = [matchTokenStr, matchTokenComment, matchTokenBlock, matchTokenSpacesButNewline, matchTokenNewlines]

    
def make_tokens(text, begin = None, end = None, *, matchTokens = matchTokens):
    if begin == None:
        begin = 0
    if end == None:
        end = len(text)

    while begin != end:
        t = matchOneToken(matchTokens, text, begin, end)
        if t == None:
            assert text[begin] in '\'"'
            raise Exception('fail pos:{} @make_tokens'.format(begin))
        begin = t.end()
        yield t

    return

if __name__ == '__main__':
    with open('make_tokens.py') as fin:
        text = fin.read()
    print(list(make_tokens(text)))

        



    
    
