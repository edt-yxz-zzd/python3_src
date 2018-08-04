

from .raw_tokenize_SRRTL import RawTokenizer_SRRTL
from .parser_MyLL1L_of_SRRTL import parser_MyLL1L_of_SRRTL
from .ProcessMatchResult_MyLL1L_of_SRRTL import ProcessMatchResult_MyLL1L_of_SRRTL


_tokenize = parser_MyLL1L_of_SRRTL.tokenize
_parse = parser_MyLL1L_of_SRRTL.parse_tokens
_tIDDict = parser_MyLL1L_of_SRRTL.tIDDict


class RawTokenizer_SRRTL_of_XL(RawTokenizer_SRRTL):
    def __init__(self, mainID_SRRTL_of_XL, XL_in_SRRTL):
        ts = _tokenize(XL_in_SRRTL)
        mr = _parse(ts)
        
        id2infoID = ProcessMatchResult_MyLL1L_of_SRRTL(_tIDDict, ts)\
                    .to_id2infoID(mr)
        assert mainID_SRRTL_of_XL in id2infoID
        super().__init__(mainID_SRRTL_of_XL, id2infoID)




def test_RawTokenizer_SRRTL_of_XL():
    from .raw_tokenize_SRRTL import raw_tokenize_SRRTL
    
    from .MyLL1L_in_SRRTL import MyLL1L_in_SRRTL, mainID_SRRTL_of_MyLL1L
    from .id2infoID_SRRTL_of_MyLL1L import id2infoID_SRRTL_of_MyLL1L
    
    from .SRRTL_in_SRRTL import mainID_SRRTL_of_SRRTL, SRRTL_in_SRRTL
    from .id2infoID_SRRTL_of_SRRTL import id2infoID_SRRTL_of_SRRTL

    from .SRRTL_in_MyLL1L import SRRTL_in_MyLL1L
    from .MyLL1L_in_MyLL1L import MyLL1L_in_MyLL1L

    for xl_in_SRRTL, mainID_SRRTL_of_xl, id2infoID_SRRTL_of_xl, text_in_xl_ls in \
        [(MyLL1L_in_SRRTL, mainID_SRRTL_of_MyLL1L, id2infoID_SRRTL_of_MyLL1L, \
          [SRRTL_in_MyLL1L, MyLL1L_in_MyLL1L]), \
         (SRRTL_in_SRRTL, mainID_SRRTL_of_SRRTL, id2infoID_SRRTL_of_SRRTL, \
          [SRRTL_in_SRRTL, MyLL1L_in_SRRTL])]:
        for text_in_xl in text_in_xl_ls:
            raw_tokens = list(\
                raw_tokenize_SRRTL(text_in_xl, \
                                   mainID_SRRTL_of_xl, \
                                   id2infoID_SRRTL_of_xl))
            _raw_tokens = list(RawTokenizer_SRRTL_of_XL(mainID_SRRTL_of_xl, xl_in_SRRTL)\
                               .raw_tokenize(text_in_xl))

            if not _raw_tokens == raw_tokens:
                assert repr(_raw_tokens) == repr(raw_tokens)
                print(_raw_tokens)
                print(raw_tokens)
            assert _raw_tokens == raw_tokens



if __name__ == '__main__':
    test_RawTokenizer_SRRTL_of_XL()



