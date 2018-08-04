
r'''
---------- logic line and comment
line1 line1
    # comment
    line1

# comment
line2
line3


---------- abstract syntax
Expr = Variable Name | Application Expr Expr | Abstraction Name Expr
Expr' = Variable Name | ExprList1 Expr' Expr' [Expr'] | Abstraction Name Expr'
    -- ExprList1: non-Null list; may contain infix operators
---------- concrete syntax
Expr = Atom+
  where
    Atom = Name
         | BeginGroup Expr EndGroup
         | Lambda Name Expr

---------- tokenize
Token = Spaces | BeginGroup | EndGroup | Lambda | Name
Spaces = '\s+'
BeginGroup = r'\('
EndGroup = r'\)'
Lambda = '\\'
Name = r'(?![()\\]\S)+'

'''

import re
def split_lambda_functions(lines):
    # assume comment removed
    # [str] -> [str]
    # [line] -> [str_per_func]
    def merge():
        str_per_func = ''.join(ls)
        ss.append(str_per_func)
    ls = []
    ss = []
    for line in lines:
        #line.lstrip().startswith('#')
        if not line or line.isspace():
            continue
        if line[:1].isspace():
            ls.append(line)
            continue
        merge()
        ls = [line]
    else:
        if ls:
            merge()
            ls = []
    return ss

token_rex = re.compile(r'(?P<Spaces>\s+)|(?P<BeginGroup>\()|(?P<EndGroup>\))|(?P<Lambda>\\)|(?P<Name>[^\s()\\]+)')
def tokenize1(str_per_func, rex = token_rex):
    prev_end = 0
    for m in rex.finditer(str_per_func):
        if m.start() != prev_end:
            raise logic-error+maybe+wrong in regex
        name = m.lastgroup
        yield name, m.group(name)
        prev_end = m.end()
    assert prev_end == len(str_per_func)
    # prev_end = m.end()

def _test_tokenize1():
    s1 = '\n' r'\x\y \z (f a (g b \z z)) \z z_+3' '\n'
    ls = list(tokenize1(s1))
    assert ls == [('Spaces', '\n'), ('Lambda', '\\'), ('Name', 'x'), ('Lambda', '\\'), ('Name', 'y'), ('Spaces', ' '), ('Lambda', '\\'), ('Name', 'z'), ('Spaces', ' '), ('BeginGroup', '('), ('Name', 'f'), ('Spaces', ' '), ('Name', 'a'), ('Spaces', ' '), ('BeginGroup', '('), ('Name', 'g'), ('Spaces', ' '), ('Name', 'b'), ('Spaces', ' '), ('Lambda', '\\'), ('Name', 'z'), ('Spaces', ' '), ('Name', 'z'), ('EndGroup', ')'), ('EndGroup', ')'), ('Spaces', ' '), ('Lambda', '\\'), ('Name', 'z'), ('Spaces', ' '), ('Name', 'z_+3'), ('Spaces', '\n')]

    tokens = tuple(map(Pair2Token, ls))
    r = parse1(tokens)
    print(r)

    expr, i = r
    from pprint import pprint
    pprint(expr.plain())


class Pair2Token:
    def __init__(self, pair):
        self.case, self.string = pair
    def isSpaces(self):
        return self.case == 'Spaces'
    def isLambda(self):
        return self.case == 'Lambda'
    def isName(self):
        return self.case == 'Name'
    def isBeginGroup(self):
        return self.case == 'BeginGroup'
    def isEndGroup(self):
        return self.case == 'EndGroup'
    def __repr__(self):
        return 'Pair2Token(({!r}, {!r}))'.format(self.case, self.string)

class Expr:
    def __init__(self, atoms):
        # atom = Variable | Expr | Abstraction
        # atoms = [atom]
        assert atoms
        self.atoms = tuple(atoms)
    def __repr__(self):
        return 'Expr({!r})'.format(self.atoms)
    def plain(self):
        return ('Expr', tuple(map(lambda x:x.plain(), self.atoms)))
class Variable:
    def __init__(self, name_token):
        assert name_token.isName()
        self.name_token = name_token
    def __repr__(self):
        return 'Variable({!r})'.format(self.name_token)
    def plain(self):
        return ('Variable', self.name_token.string)
class Abstraction:
    def __init__(self, name_token, expr):
        assert name_token.isName()
        assert isinstance(expr, Expr)
        self.bounded_name_token = name_token
        self.body = expr
    def __repr__(self):
        return 'Abstraction({!r}, {!r})'.format(self.bounded_name_token, self.body)
    def plain(self):
        return ('Abstraction', self.bounded_name_token.string, self.body.plain())
def parse_with_remain(tokens, begin=0):
    # @return: None | (Expr, end)
    i = skip_Spaces(tokens, begin)
    return _parse_Expr(tokens, i)
def parse1(tokens):
    i = 0
    r = parse_with_remain(tokens, i)
    if r is not None:
        expr, i = r
    if i != len(tokens):
        raise Exception('fail at: tokens[{}]'.format(i))
    return r

def _parse_Expr(tokens, i):
    # No spaces at beginning
    ls = [] # Atom+
    while True:
        r = _parse_Atom(tokens, i)
        if r is None: break
        (atom, i) = r
        ls.append(atom)
    if not ls:
        return None
    return Expr(ls), i
def skip_Spaces(tokens, i):
    while i < len(tokens):
        t = tokens[i]
        if not t.isSpaces():
            return i
        i += 1
    return i
def _parse_Atom(tokens, i):
    # No spaces at beginning
    if i == len(tokens):
        return None
    t = tokens[i]; i += 1
    i = skip_Spaces(tokens, i)
    if t.isName():
        return Variable(t), i
    elif t.isBeginGroup():
        r = _parse_Expr(tokens, i)
        if r is None:
            raise Exception('tokens[{}:] not startswith a Expr'.format(i))
        expr, i = r
        if i == len(tokens):
            raise Exception('missing ")"')
        if not tokens[i].isEndGroup():
            raise Exception('tokens[{}] expected a ")"'.format(i))
        i += 1
        i = skip_Spaces(tokens, i)
        return expr, i
    elif t.isLambda():
        r = _parse_Name(tokens, i)
        if r is None:
            raise Exception('tokens[{}] expected a Name'.format(i))
        name, i = r
        r = _parse_Expr(tokens, i)
        if r is None:
            raise Exception('tokens[{}] expected a Expr'.format(i))
        expr, i = r
        return Abstraction(name, expr), i
    else:
        return None
    pass
def _parse_Name(tokens, i):
    # No spaces at beginning
    if i == len(tokens):
        return None
        raise Exception('EOL while expected Name')
    if not tokens[i].isName():
        return None
    t = tokens[i]; i += 1
    i = skip_Spaces(tokens, i)
    return t, i





_test_tokenize1()



