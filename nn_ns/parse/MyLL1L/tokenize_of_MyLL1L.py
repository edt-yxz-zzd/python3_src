

from .raw_tokenize_SRRTL import raw_tokenize_SRRTL
from .id2infoID_SRRTL_of_MyLL1L import id2infoID_SRRTL_of_MyLL1L
from .MyLL1L_in_SRRTL import mainID_SRRTL_of_MyLL1L

from .raw2tokens_of_MyLL1L import raw2tokens_of_MyLL1L



def tokenize_of_MyLL1L(xl_in_MyLL1L, begin=0, end=None):
    raw_tokens = raw_tokenize_SRRTL(xl_in_MyLL1L, \
                    mainID_SRRTL_of_MyLL1L, id2infoID_SRRTL_of_MyLL1L, \
                    begin, end)
    tokens = raw2tokens_of_MyLL1L(raw_tokens, xl_in_MyLL1L)
    return tokens

        
def test_tokenize_of_MyLL1L():
    text = '''agdag
    alfa
    afas
      afkds
    af

afddf
    42342'''
    return tokenize_of_MyLL1L(text)


    

if __name__ == '__main__':
    print(test_tokenize_of_MyLL1L())
    
    from .raw_tokenize_SRRTL import raw_tokenize_SRRTL
    from .MyLL1L_in_MyLL1L import MyLL1L_in_MyLL1L
    from .SRRTL_in_MyLL1L import SRRTL_in_MyLL1L


    for xl_in_MyLL1L in [MyLL1L_in_MyLL1L, SRRTL_in_MyLL1L]:
        r = tokenize_of_MyLL1L(xl_in_MyLL1L)
        for e in zip(range(4667868), r):
            print(e)
