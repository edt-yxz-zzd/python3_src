
from .RawTokenizer_SRRTL_of_XL import RawTokenizer_SRRTL_of_XL
from .Parser_MyLL1L_of_XL import Parser_MyLL1L_of_XL
from .Pos2RC import Pos2RC

class ToolChain_MyLL1L:
    def __init__(self, mainID_SRRTL_of_XL, XL_in_SRRTL, \
                 raw2tokens_of_XL, \
                 mainID_MyLL1L_of_XL, XL_in_MyLL1L, \
                 # a subclass of ProcessMatchResult_MyLL1L
                 ProcessMatchResult_MyLL1L_of_XL\
                 ):
        self.raw_tokenizer = RawTokenizer_SRRTL_of_XL(mainID_SRRTL_of_XL, XL_in_SRRTL)
        self.raw2tokens = raw2tokens_of_XL
        self.parser = Parser_MyLL1L_of_XL(mainID_MyLL1L_of_XL, XL_in_MyLL1L)
        self.processor_factory = ProcessMatchResult_MyLL1L_of_XL


    def text_to_pos2rc(self, text):
        return Pos2RC(text)
    def raw_tokenize(self, text_in_XL, begin = 0, end = None):
        return self.raw_tokenizer.raw_tokenize(text_in_XL, begin, end)
    
    def tokenize(self, text_in_XL, begin = 0, end = None):
        return self.raw2tokens(
            self.raw_tokenize(text_in_XL, begin, end),
            text_in_XL)
    
    def parse_tokens(self, tokens_MyLL1L_of_XL, pos2rc = None):
        return self.parser.parse_tokens(tokens_MyLL1L_of_XL, pos2rc)

    def _parse_text(self, text_in_XL, begin = 0, end = None):
        tokens = self.tokenize(text_in_XL, begin, end)
        pos2rc = self.text_to_pos2rc(text_in_XL)
        
        match_result = self.parse_tokens(tokens, pos2rc)
        return match_result, tokens, pos2rc
    
    def parse_text(self, text_in_XL, begin = 0, end = None):
        match_result, tokens, pos2rc = self._parse_text(text_in_XL, begin, end)
        return match_result

    def process(self, match_result_MyLL1L_of_XL, tokens_MyLL1L_of_XL, pos2rc = None):
        tokens, match_result = tokens_MyLL1L_of_XL, match_result_MyLL1L_of_XL
        return self.processor_factory(self.parser.tIDDict, tokens, pos2rc)\
               .process(match_result)

    
    def process_tokens(self, tokens_MyLL1L_of_XL, pos2rc = None):
        tokens = tokens_MyLL1L_of_XL
        match_result = self.parse_tokens(tokens, pos2rc)
        return self.process(match_result, tokens, pos2rc)


    def process_text(self, text_in_XL, begin = 0, end = None):
        match_result, tokens, pos2rc = self._parse_text(text_in_XL, begin, end)
        
        return self.process(match_result, tokens, pos2rc)

