
from .ParseResult import getMatchResultRng, MatchFail
from .Pos2RC import Pos2RC
from .tools_for_id2infoID_MyLL1L import tIDDict_2_define, tIDDict_2_id2info,\
     read_result3, save_result3


class Parser_MyLL1L:

    def __init__(self, mainID_MyLL1L_of_XL, tIDDict_MyLL1L_of_XL, debug = False):
        assert (mainID_MyLL1L_of_XL,) in tIDDict_MyLL1L_of_XL
        self.mainID = mainID_MyLL1L_of_XL
        self.tIDDict = tIDDict_MyLL1L_of_XL
        
        self.mainInfo = self.tIDDict[(self.mainID,)]
        self.define = self.__get_define()
        self.set_debug(debug)
        return

    def __top_id(self):
        return (k for k in self.tIDDict if len(k) == 1)
    def set_debug(self, debug = True):
        for tID in self.__top_id():
            self.tIDDict[tID].set_debug(debug)
    @staticmethod
    def from_string(s):
        mainID, s = eval(s)
        tIDDict, _ = read_result3(s)
        return Parser_MyLL1L(mainID, tIDDict)
    def _to_string(self):
        d = self.tIDDict
        s = save_result3(d, tIDDict_2_id2info(d))
        s = str((self.mainID, s))
        return s
    
    def to_string(self):
        s = self._to_string()
        #assert s == self.from_string(s)._to_string()
        return s
        
    def get_define(self):
        return self.define

    def __get_define(self):
        return tIDDict_2_define(self.tIDDict)
        ks = sorted(self.__top_id())
        cs = (self.tIDDict[k] for k in ks)
        body = '\n'.join(c.get_define() for c in cs)
        return body
    def parse_tokens(self, tokens_MyLL1L_of_XL, pos2rc = None):
        return parse_tokens_MyLL1L(tokens_MyLL1L_of_XL, self.mainInfo, pos2rc)
    
    def tokenize(self, text_in_XL, begin = 0, end = None):
        raise NotImplementedError('parse_text/tokenize@Parser_MyLL1L')
    
    def parse_text(self, text_in_XL, begin = 0, end = None):
        tokens = self.tokenize(text_in_XL, begin, end)
        pos2rc = Pos2RC(text_in_XL)
        
        r = self.parse_tokens(tokens, pos2rc)
        return r
def parse_tokens_MyLL1L(tokens_MyLL1L_of_XL, mainInfoID_MyLL1L_of_XL, pos2rc = None):
    tokens = tokens_MyLL1L_of_XL
    info = mainInfoID_MyLL1L_of_XL
    match_result = info.match(tokens, 0, len(tokens))
    begin, end = getMatchResultRng(match_result)
    if end != len(tokens):
        s = 'parse end at tokens[{}] = {}'.format(end, tokens[end])
        
        if pos2rc != None:
            text_stop_pos = tokens[end].begin
            r, c = pos2rc(text_stop_pos)
            s = '{}; row: {}, column: {}'.format(s, r, c)

        raise MatchFail(s, pos=end)

    return match_result




def __outdated_test_parse_MyLL1L_easy(raw_id2infoID_MyLL1L, tokens, mainID, pos2rc = None):
    from .tools_for_id2infoID_MyLL1L import fill_raw_id2info_MyLL1L
    result1_InfoDict = raw_id2infoID_MyLL1L
    
    tIDDict, id2info = fill_raw_id2info_MyLL1L(result1_InfoDict)
    match_result = parse(tokens, id2info[mainID], pos2rc)
    return tIDDict, id2info, match_result



if __name__ == '__main__':
    print('test: see Parser_MyLL1L_of_MyLL1L')


