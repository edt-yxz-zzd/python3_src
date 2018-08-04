
import re
from .Token import Token
from .RawToken import RawToken
from .Pos2RC import calcLineBeginPos


def reverseDict(d):
    r = {e:k for k, e in d.items()}
    assert len(r) == len(d)
    return r

def discardFalseType(tokens):
    ls = [t for t in tokens if t.type]
    return ls

def convert_type(tokens, type_map):
    for t in tokens:
        case = t.type
        #case = type_map.get(case, case)
        case = type_map[case]
        t.type = case
    return

def convert_type_default(tokens, type_map):
    for t in tokens:
        case = t.type
        case = type_map.get(case, case)
        #case = type_map[case]
        t.type = case
    return

def raw2tokens(raw_tokens, source_string):
    ls = []
    for raw in raw_tokens:
        case = raw.type
        substring = raw.sub(source_string)
        t = Token(case, raw.begin, raw.end, substring)
        ls.append(t)
    return ls

def insert_token(tokens, token_type, pos=None, substring=''):
    if pos == None:
        pos = len(tokens)
    if not tokens:
        begin = end = 0
    else:
        begin = end = tokens[-1].end

    token = Token(token_type, begin, end, substring)
    tokens.insert(pos, token)
    return


def addNewLine(tokens, newline = '\n'):
    if not tokens:
        begin = end = 0
    else:
        begin = tokens[0].begin
        end = tokens[-1].end
    
    BEGIN = Token(newline, begin, begin, '')
    END = Token(newline, end, end, '')

    ls = [BEGIN]
    ls.extend(tokens)
    ls.append(END)
    return ls


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
    assert len(case) == 1 # token type is a character

    begin = tokens[0].begin
    end = tokens[-1].end
    
    s = ''.join(t.value for t in tokens)
    # error: assert begin + len(s) == end # if discarded some tokens

    return Token(case, begin, end, s)

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


def calc_nIndents(indents):
    nindents = [0] * len(indents)

    def indent_eq(a, b): return a == b
    def indent_startswith(a, b): return a.startswith(b)
    indent_stack = ['']
    for idx, indent in enumerate(indents):
        if indent_eq(indent, indent_stack[-1]):
            pass
        elif indent_startswith(indent, indent_stack[-1]):
            indent_stack.append(indent)
        else:
            while indent_startswith(indent_stack[-1], indent):
                indent_stack.pop()
                if indent_eq(indent, indent_stack[-1]):
                    break
            else:
                raise IndentationError('indent error')

        assert indent_eq(indent, indent_stack[-1])
        nindents[idx] = len(indent_stack) - 1
    return nindents


def diff_nIndents(nindents):
    ls = nindents
    for i in range(len(ls)-1, 0, -1):
        ls[i] -= ls[i-1]
    

def _insert_indents_split_into_lines(tokens, string):
    L = len(string)
    i = 0
    lines = []
    indents = []
    substrs = []
    isIndent = lambda: string[i] == '\t'
    getIndent = lambda: tokens[i].value
    isNewline = lambda: string[i] == '\n'
    while i < L:
        line = []
        lines.append(line)
        indents.append('')
        if isIndent():
            indents[-1] = getIndent()
            i += 1

        while i < L:
            assert not isIndent()
            line.append(tokens[i])
            
            if isNewline():
                i += 1
                break
            i += 1
        substrs.append(string[i-len(line):i])
    return lines, substrs, indents

def insert_indents(tokens: 'without empty line(spaces + comment); '\
                           'no multilines logic line',
                   string:r'type: \n \t \b'):
    assert len(tokens) == len(string)
    L = len(string)

    
    lines, substrs, indents = _insert_indents_split_into_lines(tokens, string)

    # calc number of indent for each line
    nindents = calc_nIndents(indents)
    diff_nIndents(nindents)
    assert len(nindents) == len(indents)



    # insert indent and dedent
    new_tokens = []
    new_substrs = []
    def T(case):
        begin = lines[lineno][0].begin
        return Token(case, begin, begin, '')
    for lineno, i in enumerate(nindents):
        if i < 0:
            new_tokens.extend(T('\b') for _ in range(-i))
            new_substrs.append('\b' * -i)
        elif i > 0:
            new_tokens.extend(T('\t') for _ in range(i))
            new_substrs.append('\t' * i)
            
        new_tokens.extend(lines[lineno])
        new_substrs.append(substrs[lineno])

    # patch dedent at end of file
    s = sum(nindents)
    if s < 0:
        raise
    elif s > 0:
        assert L
        assert 0 <= lineno < L
        new_tokens.extend(T('\b') for _ in range(s))
        new_substrs.append('\b' * s)

    new_string = ''.join(new_substrs)



    # check
    tokens, string = new_tokens, new_string
    _tokens, _string = discardTokens(tokens, string, '\t\n+\b')
    assert '\b' == '\x08'
    assert len(string) == len(_string)

    return tokens, string
        
            
    
    
        
    

'''

def build_string_for_insert_indents(tokens,
                                    newline_type, indent_type):
    d = {newline_type: '\n', indent_type: '\t'}
    s = str(d.get(t.type, 'o') for t in tokens)
    return s
def insert_indents(tokens: 'without empty line(spaces + comment); '\
                           'start and end with newline; '\
                           'no multilines logic line',
                   string:r'type: \n \t \b'):
    assert len(tokens) == len(string)
    assert string[0] == string[-1] == '\n'

    lineBeginPos_ls = calcLineBeginPos(string)
    end = tokens[-1].end
    tokens.append(Token('\t', end, end, ''))
    string += '\t'
    #lineBeginPos_ls.pop()
    indents = [(tokens[i].value if string[i] == '\t' else '') for i in lineBeginPos_ls]
    nindents = [0] * len(indents)

    def indent_eq(a, b): return a == b
    def indent_startswith(a, b): return a.startswith(b)
    indent_stack = ['']
    for idx, indent in enumerate(indents):
        if indent_eq(indent, indent_stack[-1]):
            pass
        elif indent_startswith(indent, indent_stack[-1]):
            indent_stack.append(indent)
        else:
            while indent_startswith(indent_stack[-1], indent):
                indent_stack.pop()
                if indent_eq(indent, indent_stack[-1]):
                    break
            else:
                raise IndentationError('indent error')

        assert indent_eq(indent, indent_stack[-1])
        nindents[idx] = len(indent_stack) - 1

    nindent_pre = 0
    idx_pre = 0
    new_tokens = []
    new_strings = []
    def T(case):
        begin = tokens[idx].begin
        return Token(case, begin, begin, '')

    assert idx_pre < len(tokens)
    assert string[idx_pre] != '\t' or tokens[idx_pre].value == ''
    for idx, nindent in zip(lineBeginPos_ls, nindents):
        assert string[idx_pre] != '\t'
        new_tokens.extend(tokens[idx_pre : idx])
        new_strings.append(string[idx_pre : idx])
        
        if nindent < nindent_pre:
            new_tokens.extend(T('\b') for _ in range(nindent, nindent_pre))
            new_strings.append('\b' * (nindent_pre - nindent))
        elif nindent > nindent_pre:
            new_tokens.extend(T('\t') for _ in range(nindent_pre, nindent))
            new_strings.append('\t' * (nindent - nindent_pre))

        nindent_pre = nindent
        idx_pre = idx
        if string[idx_pre] == '\t':
            idx_pre += 1

    new_string = ''.join(new_strings)
    assert idx_pre == len(tokens)
    assert nindent_pre == 0
    assert len(new_string) == len(new_tokens)
    tokens, string = new_tokens, new_string

    assert string[0] == '\n'
    #error : if len(string) > 1:assert string[1] != '\n'

    # \b stand for word bound in rex, r'\t\n+\x08' or not raw '\t\n+\b'
    _tokens, _string = discardTokens(tokens, string, '\t\n+\b')
    assert '\b' == '\x08'
    assert len(string) == len(_string)
    
    tokens, string = mergeTokens(tokens, string, r'\n+', '\n')
    assert string[0] == '\n'
    if len(string) > 1:assert string[1] != '\n'
    
    tokens = tokens[1:]
    string = string[1:]

    n = 0
    for c in string:
        if c == '\t':
            n += 1
        elif c == '\b':
            n -= 1
            assert n >= 0
    assert n == 0
    return tokens, string


'''

