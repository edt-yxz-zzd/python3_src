
__all__ = '''
    t_error
    iter_tokens
    make_lexer
    token2lexpos_total
    token2lineno_column
    token2lineno
    token2column
'''.split()
#    t_newline

from sand import TokenizeError
from importlib import import_module

# Define a rule so we can track line numbers
##def t_newline(t):
##    r'\n+'
##    t.lexer.lineno += len(t.value)
##    #t.lexer.line_begin_lexpos = t.lexpos + len(t.value)
# Error handling rule
def t_error(t):
    #lineno = t.lexer.lineno
    #column = 1+t.lexpos - getattr(t.lexer, "line_begin_lexpos", 0)
    #print(column, token2column(t))
    lineno, column = token2lineno_column(t)
    lexpos, total = token2lexpos_total(t)
    raise TokenizeError('fail at line:{}, column:{}, lexpos:{}, total:{}'
                        .format(lineno, column, lexpos, total))

# Compute column. 
#     input is the input text string
#     token is a token instance
def find_column(input, lexpos):
    'first column is 1, not 0'
    last_cr = input.rfind('\n', 0, lexpos) # maybe -1
    column = (lexpos - last_cr) 
    return column

def token2column(t):
    return find_column(t.lexer.lexdata, t.lexpos)

def token2lineno(t):
    'O(n); first line is 1, not 0'
    return 1 + t.lexer.lexdata.count('\n', 0, t.lexpos) 
def token2lineno_column(t):
    'O(n)'
    lineno = token2lineno(t)
    column = token2column(t)
    return lineno, column 
def token2lexpos_total(t):
    return t.lexpos, len(t.lexer.lexdata)


def nonstr_or___name__2nonstr_or_module(nonstr_or___name__):
    
    if isinstance(nonstr_or___name__, str):
        __name__ = nonstr_or___name__
        m = import_module(__name__)
    else:
        nonstr = nonstr_or___name__
        m = nonstr
    return m
        
    
def make_lexer(lex_module):
    from ply.lex import lex
    m = nonstr_or___name__2nonstr_or_module(lex_module)
    lexer = lex(module = m)
    return lexer
    
def iter_tokens(lex_module, source):
    'for testing'
    lexer = make_lexer(lex_module)
    lexer.input(source)
    return iter(lexer)





