
from .ChildrenMixin import ChildrenMixin
from .InfoID_MyLL1L import InfoIDNamedChildren
class MatchResultExplain_MyLL1L(ChildrenMixin):
    def __init__(self, match_result, tIDDict, tokens):
        self.r = match_result
        self.tID, (self.begin, self.end), self.children, self.ns = match_result
        self.d = tIDDict
        self.ls = tokens

        self.ID = self.tID[-1]
        self.info = info = tIDDict[self.tID]
        self.define_type = info.define_type
        self.name2idx = None
        if isinstance(info, InfoIDNamedChildren):
            self.name2idx = info.name2idx

    def __repr__(self):
        return repr(self.match_result)
    def _getitem(self, i):
        r = super()._getitem(i)
        return MatchResultExplain_MyLL1L(r, self.d, self.ls)
        
    def _getitem_str(self, s):
        i = self.name2idx[s]
        return self[i]

        
