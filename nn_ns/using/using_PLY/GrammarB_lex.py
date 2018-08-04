

from .defs import GrammarB_in_GrammarB
from .lex_common import t_error, iter_tokens # t_newline, 





# need not COMMENT/SPACES/newline !!!
tokens = '''
    AT_START_SYMBOL
    AT_TERMINALS
    RULE_BODY_BEGIN
    BODY_BEGIN
    BODY_END
    SYMBOL


'''.split()

t_AT_START_SYMBOL = '@start_symbol'
t_AT_TERMINALS = '@terminals'
t_RULE_BODY_BEGIN = '='
t_BODY_BEGIN = r':'
t_BODY_END = r';'
t_SYMBOL = r'\w+'
t_ignore_COMMENT = r'\#.*' # ERROR: Make sure '#' in rule 't_ignore_COMMENT' is escaped with '\#'
t_ignore_SPACES = r'\s+'



def test_lexer():
    itokens = iter_tokens(__name__, GrammarB_in_GrammarB)
    return list(itokens)


def test_lexer_error():
    src = ('''
A:= B ;
 *
''')
    itokens = iter_tokens(__name__, src)
    try:
        print(list(itokens))
    except Exception as e:
        try:
            assert str(e) == 'fail at line:3, column:2, lexpos:10, total:12'
        except:
            print(e)
            raise
    else:
        raise logic-error
    

test_lexer()
test_lexer_error()


if __name__ == '__main__':
    from pprint import pprint
    pprint(test_lexer())








