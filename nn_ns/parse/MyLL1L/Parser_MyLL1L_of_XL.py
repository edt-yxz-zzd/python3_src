

from .parse_MyLL1L import Parser_MyLL1L
from .Parser_MyLL1L_of_MyLL1L import parser_MyLL1L_of_MyLL1L
from .ProcessMatchResult_MyLL1L_of_MyLL1L import ProcessMatchResult_MyLL1L_of_MyLL1L
from .ProcessMatchResult_MyLL1L import ProcessMatchResult_MyLL1L


_tokenize = parser_MyLL1L_of_MyLL1L.tokenize
_parse = parser_MyLL1L_of_MyLL1L.parse_tokens

class Parser_MyLL1L_of_XL(Parser_MyLL1L):
    def __init__(self, mainID_MyLL1L_of_XL, XL_in_MyLL1L):
        tIDDict = calc_tIDDict_MyLL1L_of_XL(XL_in_MyLL1L)
        
        assert (mainID_MyLL1L_of_XL,) in tIDDict
        super().__init__(mainID_MyLL1L_of_XL, tIDDict)
        
        
def calc_tIDDict_MyLL1L_of_XL(XL_in_MyLL1L):
    ts = _tokenize(XL_in_MyLL1L)
    mr = _parse(ts)
    
    tIDDict = ProcessMatchResult_MyLL1L_of_MyLL1L(ts).to_tIDDict(mr)
    return tIDDict

