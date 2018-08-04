


from .Namespace import Namespace

from .error import FailAtPos
class MatchFail(FailAtPos):pass



'''
match result:
# tID        : tuple of ID // tIDDict not contained
# begin, end : tokens not contained
# children   : None - leaf IDToken ; [] - 0 matchs  IDItem min==0
# ns         : free for user // namespace
(tID, (begin, end), children, ns)
'''



def make_match_result(tID, begin_end, children):
    begin, end = begin_end
    return (tID, begin_end, children, Namespace())

def getMatchResultRng(match_result):
    return match_result[1]

def getMatchResultChildren(match_result):
    return match_result[2]

def getMatchResultNs(match_result):
    return match_result[-1]








