
from collections import namedtuple

'''
class MatchNode:
    def __init__(self, tID, begin, end, children):

'''

'''
assert type(tID[-1]) is int
children == None means leaf
'''

MatchNode = namedtuple('MatchNode', 'tID, begin, end, children'.split(', '))
class ProcessNode:
    def __init__(self, match_node=None, \
                 parent=None, children=None, \
                 attr=None, value=None):
        self.match_node = match_node
        self.parent = parent
        self.children = children
        self.attr = attr
        self.value = value
        return

    def to_tuple(self):
        return self.match_node, self.parent, self.children, self.attr, self.value
    def __repr__(self):
        return 'ProcessNode' + repr(self.to_tuple())
    def __eq__(self, other):
        return self.to_tuple() == other.to_tuple()
    def __ne__(self, other):
        return not (self == other)
    









    
