

from .Parser_MyLL1L_of_XL import Parser_MyLL1L_of_XL
from .SRRTL_in_MyLL1L import SRRTL_in_MyLL1L, mainID_MyLL1L_of_SRRTL
from .tokenize_of_SRRTL import tokenize_of_SRRTL



class Parser_MyLL1L_of_SRRTL(Parser_MyLL1L_of_XL):
    def __init__(self):
        super().__init__(mainID_MyLL1L_of_SRRTL, SRRTL_in_MyLL1L)

    def tokenize(self, xl_in_SRRTL, begin = 0, end = None):
        tokens = tokenize_of_SRRTL(xl_in_SRRTL, begin, end)
        #for t in tokens: print('{!r}'.format(t.type))
        return tokens
    

parser_MyLL1L_of_SRRTL = Parser_MyLL1L_of_SRRTL()


#print(parser_MyLL1L_of_SRRTL.get_define())



if __name__ == '__main__':
    from .raw_tokenize_SRRTL import raw_tokenize_SRRTL
    from .MyLL1L_in_SRRTL import MyLL1L_in_SRRTL
    from .SRRTL_in_SRRTL import SRRTL_in_SRRTL

    p = parser_MyLL1L_of_SRRTL
    #p.set_debug(True)
    for xl_in_SRRTL in [MyLL1L_in_SRRTL, SRRTL_in_SRRTL]:
        r = p.parse_text(xl_in_SRRTL)
        print(r[:2], '\n'*4)
