
from .error import FailAtPos
class RawTokenizeFail(FailAtPos):pass

class RawToken:
    def __init__(self, state_id, type_id, begin, end):
        self.type = type_id
        self.state = state_id
        self.begin = begin
        self.end = end
        return

    def size(self):
        return self.end - self.begin

    def sub(self, string):
        return string[self.begin : self.end]
    
    def __repr__(self):
        state_id, type_id, begin, end = self.state, self.type, self.begin, self.end
        r = 'RawToken({!r}, {!r}, {!r}, {!r})'.format(state_id, type_id, begin, end)
        return r

    def __eq__(self, other):
        return self.type == other.type and self.state == other.state and\
               self.begin == other.begin and self.end == other.end
    def __ne__(self, other):
        return not (self == other)
