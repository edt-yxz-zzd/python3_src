

from .raw_tokenize_SRRTL import raw_tokenize_SRRTL
from .id2infoID_SRRTL_of_SRRTL import id2infoID_SRRTL_of_SRRTL
from .SRRTL_in_SRRTL import mainID_SRRTL_of_SRRTL

from .raw2tokens_of_SRRTL import raw2tokens_of_SRRTL



def tokenize_of_SRRTL(xl_in_SRRTL, begin=0, end=None):
    raw_tokens = raw_tokenize_SRRTL(xl_in_SRRTL, \
                    mainID_SRRTL_of_SRRTL, id2infoID_SRRTL_of_SRRTL, \
                    begin, end)
    tokens = raw2tokens_of_SRRTL(raw_tokens, xl_in_SRRTL)
    return tokens

        
def test_tokenize_of_SRRTL():
    text = '''agdag
    alfa
    afas
      afkds
    af

afddf
    42342'''
    return tokenize_of_SRRTL(text)


    

if __name__ == '__main__':
    print(test_tokenize_of_SRRTL())
    
    from .raw_tokenize_SRRTL import raw_tokenize_SRRTL
    from .MyLL1L_in_SRRTL import MyLL1L_in_SRRTL
    from .SRRTL_in_SRRTL import SRRTL_in_SRRTL


    for xl_in_SRRTL in [MyLL1L_in_SRRTL, SRRTL_in_SRRTL]:
        r = tokenize_of_SRRTL(xl_in_SRRTL)
        for e in zip(range(4667868), r):
            print(e)
