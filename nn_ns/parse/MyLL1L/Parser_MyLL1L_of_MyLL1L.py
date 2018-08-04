

from .tokenize_of_MyLL1L import tokenize_of_MyLL1L
from .MyLL1L_in_MyLL1L import mainID_MyLL1L_of_MyLL1L
from .id2infoID_MyLL1L_of_MyLL1L import tIDDict_MyLL1L_of_MyLL1L
from .parse_MyLL1L import Parser_MyLL1L



class Parser_MyLL1L_of_MyLL1L(Parser_MyLL1L):
    def __init__(self):
        super().__init__(mainID_MyLL1L_of_MyLL1L, tIDDict_MyLL1L_of_MyLL1L)

    def tokenize(self, xl_in_MyLL1L, begin = 0, end = None):
        tokens = tokenize_of_MyLL1L(xl_in_MyLL1L, begin, end)
        return tokens
    

parser_MyLL1L_of_MyLL1L = Parser_MyLL1L_of_MyLL1L()

if __name__ == '__main__':
    from .raw_tokenize_SRRTL import raw_tokenize_SRRTL
    from .MyLL1L_in_MyLL1L import MyLL1L_in_MyLL1L
    from .SRRTL_in_MyLL1L import SRRTL_in_MyLL1L


    for xl_in_MyLL1L in [MyLL1L_in_MyLL1L, SRRTL_in_MyLL1L]:
        r = parser_MyLL1L_of_MyLL1L.parse_text(xl_in_MyLL1L)
        print(r[:2], '\n'*4)
