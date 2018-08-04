
from .ParseResult import getMatchResultChildren
class ProcessMatchResult:
    def __init__(self, MatchResultExplain):
        self.MatchResultExplain = MatchResultExplain
    def explain(self, match_result):
        return self.MatchResultExplain(match_result)

    def process(self, match_result):
        self._process(match_result)
        return self._get_result(match_result)
    
    def _process(self, match_result):
        this_f = self._process
        children = getMatchResultChildren(match_result)

        self._pre_process(match_result)
        
        if children != None:
            for c in children:
                this_f(c)
        else:
            self._process_leaf(match_result)

        self._post_process(match_result)


    def _pre_process(self, match_result):pass
    def _process_leaf(self, match_result):pass
    def _post_process(self, match_result):pass
    def _get_result(self, match_result):pass


    

    
    
    
        

        
