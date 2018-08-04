

from .Parser_MyLL1L_of_XL import Parser_MyLL1L_of_XL
from .LL1V2L_in_MyLL1L import LL1V2L_in_MyLL1L, mainID_MyLL1L_of_LL1V2L
from .raw2tokens_of_LL1V2L import raw2tokens_of_LL1V2L
from .LL1V2L_in_SRRTL import LL1V2L_in_SRRTL, mainID_SRRTL_of_LL1V2L
from .RawTokenizer_SRRTL_of_XL import RawTokenizer_SRRTL_of_XL

class Parser_MyLL1L_of_LL1V2L(Parser_MyLL1L_of_XL):
    def __init__(self):
        super().__init__(mainID_MyLL1L_of_LL1V2L, LL1V2L_in_MyLL1L)
        self.raw_tokenize = RawTokenizer_SRRTL_of_XL(\
            mainID_SRRTL_of_LL1V2L, LL1V2L_in_SRRTL).raw_tokenize

    def tokenize(self, xl_in_LL1V2L, begin = 0, end = None):
        tokens = raw2tokens_of_LL1V2L(\
            self.raw_tokenize(xl_in_LL1V2L, begin, end),
            xl_in_LL1V2L)
        #print(tokens)
        return tokens
    

parser_MyLL1L_of_LL1V2L = Parser_MyLL1L_of_LL1V2L()





if __name__ == '__main__':
    from .TryL_in_LL1V2L import TryL_in_LL1V2L
    p = parser_MyLL1L_of_LL1V2L
    r = p.parse_text(TryL_in_LL1V2L)
    print(r[:2], '\n'*4)
