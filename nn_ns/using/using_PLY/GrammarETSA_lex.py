
#from sand.grammar.GrammarETSA_def import GrammarETSA_in_GrammarETSA
from .defs import GrammarETSA_in_GrammarETSA
from .GrammarTSA_lex import *



# need not COMMENT/SPACES/newline !!!
tokens = tokens + '''
    STAR
    CROSS
    OPTION
'''.split()

t_SYMBOL = t_SYMBOL + '|@Null|@Dead'
t_STAR = r'\*'
t_CROSS = r'\+'
t_OPTION = r'\?'




def test_lexer():
    itokens = iter_tokens(__name__, GrammarETSA_in_GrammarETSA)
    return list(itokens)


def test_lexer_error():
    src = ('''
A = B ;
 @
''')
    itokens = iter_tokens(__name__, src)
    try:
        print(list(itokens))
    except Exception as e:
        assert str(e) == 'fail at line:3, column:2, lexpos:10, total:12'
    else:
        raise logic-error
    

test_lexer()
test_lexer_error()


if __name__ == '__main__':
    from pprint import pprint
    pprint(test_lexer())








