
from make_tokens import make_tokens, Token
import re


changeTypeDict = {
    'block': 'b',
    'str': 's',
    'spacesButNewline': ' ',
    'comment': '#',
    'newlines': '\n'
    }
def changeType(oldToken):
    t = oldToken.type
    oldToken.type = changeTypeDict[t]
    return oldToken


def findRange(string, rex):
    ls = []
    for m in re.finditer(rex, string):
        assert m
        assert 0 <= m.start() <= m.end()
        ls.append((m.start(), m.end()))

    L = len(string)
    ls.append((L, L))
    return ls

def discardTokens(tokens, string, rex):
    assert len(tokens) == len(string)
    
    ls = findRange(string, rex)
    
    ts = []
    start = 0
    for i, j in ls:
        ts.extend(tokens[start : i])
        start = j

    s = re.sub(rex, '', string)

    assert len(ts) == len(s)
    return ts, s


def _mergeTokens(tokens, case):
    assert len(tokens)
    assert len(case) == 1

    begin = tokens[0].begin()
    end = tokens[-1].end()
    # merge should be before discard
    s = ''.join(t.substring for t in tokens)
    assert begin + len(s) == end

    return Token(case, begin, s)

def mergeTokens(tokens, string, rex, case):
    assert len(tokens) == len(string)
    assert len(case) == 1
    
    ls = findRange(string, rex)
    
    ts = []
    start = 0
    for i, j in ls:
        ts.extend(tokens[start : i])
        start = j
        if i < j:
            t = _mergeTokens(tokens[i : j], case)
            ts.append(t)

    s = re.sub(rex, case, string)

    assert len(ts) == len(s)
    return ts, s


def tokenizeMyLL1(text, begin=0, end=None):
    if end == None:
        end = len(text)
    return _tokenizeMyLL1(text, begin, end)

def _tokenizeMyLL1(text, begin, end):
    ls = [changeType(t) for t in make_tokens(text, begin, end)]
    BEGIN = Token('\n', begin, '')
    END = Token('\n', end, '')

    tokens = [BEGIN]
    tokens.extend(ls)
    tokens.append(END)

    string = ''.join(t.type for t in tokens)
    tokens, string = mergeTokens(tokens, string, '[bs]+', 'B')
    tokens, string = discardTokens(tokens, string, '(?<=\n)[ #]*\n') # empty line except BEGIN
    
    tokens, string = mergeTokens(tokens, string, '(?<=\n) ', '\t') # intent
    tokens, string = discardTokens(tokens, string, '[ #]+') # remove spaces and comment
    assert string[-1] == '\n' == string[0]

    ils = [i+1 for i, c in enumerate(string) if c == '\n']
    tokens.append(Token('\t', tokens[-1].end(), ''))
    #ils.pop()
    intents = [(tokens[i].substring if tokens[i].type == '\t' else '') for i in ils]
    nintents = [0] * len(intents)

    def intent_eq(a, b): return a == b
    def intent_startswith(a, b): return a.startswith(b)
    intent_stack = ['']
    for idx, intent in enumerate(intents):
        if intent_eq(intent, intent_stack[-1]):
            pass
        elif intent_startswith(intent, intent_stack[-1]):
            intent_stack.append(intent)
        else:
            while intent_startswith(intent_stack[-1], intent):
                intent_stack.pop()
                if intent_eq(intent, intent_stack[-1]):
                    break
            else:
                raise IndentationError('intent error')

        assert intent_eq(intent, intent_stack[-1])
        nintents[idx] = len(intent_stack) - 1

    nintent_pre = 0
    idx_pre = 0
    new_tokens = []
    T = lambda case: Token(case, tokens[idx].begin(), '')

    assert idx_pre < len(tokens)
    assert tokens[idx_pre].type != '\t'
    for idx, nintent in zip(ils, nintents):
        new_tokens.extend(tokens[idx_pre : idx])
        
        if nintent < nintent_pre:
            new_tokens.extend(T('\b') for _ in range(nintent, nintent_pre))
        elif nintent > nintent_pre:
            new_tokens.extend(T('\t') for _ in range(nintent_pre, nintent))

        nintent_pre = nintent
        idx_pre = idx
        if tokens[idx_pre].type == '\t':
            idx_pre += 1

    assert idx_pre == len(tokens)
    assert nintent_pre == 0
    
        
    tokens = new_tokens[1:]
        

    newType = set('is = , ? * + { }'.split())
    for t in tokens:
        if t.type == 'B':
            if t.substring in newType:
                t.type = t.substring

    return tokens

tokenize = tokenizeMyLL1
        
def test_tokenizeMyLL1():
    text = '''agdag
    alfa
    afas
      afkds
    af

afddf
    42342'''
    return tokenizeMyLL1(text)

#print(test_tokenizeMyLL1())
    
