
#from sand.grammar.GrammarTSA_def import GrammarTSA_in_GrammarTSA
from .defs import GrammarTSA_in_GrammarTSA
from .lex_common import t_error, iter_tokens # t_newline, 





# need not COMMENT/SPACES/newline !!!
tokens = '''
    AT_START_SYMBOL
    AT_TERMINALS
    SEQ_BEGIN
    SEQ_END
    ALT_BEGIN
    ALT_END
    SYMBOL


'''.split()

t_AT_START_SYMBOL = '@start_symbol'
t_AT_TERMINALS = '@terminals'
t_SEQ_BEGIN = '='
t_SEQ_END = ';'
t_ALT_BEGIN = r'\{'
t_ALT_END = r'\}'
t_SYMBOL = r'\w+'
t_ignore_COMMENT = r'\#.*' # ERROR: Make sure '#' in rule 't_ignore_COMMENT' is escaped with '\#'
t_ignore_SPACES = r'\s+'



def test_lexer():
    itokens = iter_tokens(__name__, GrammarTSA_in_GrammarTSA)
    return list(itokens)


def test_lexer_error():
    src = ('''
A = B ;
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








