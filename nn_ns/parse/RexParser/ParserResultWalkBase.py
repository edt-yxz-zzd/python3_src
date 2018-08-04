
from RexParser import RexParser, rex_language
from MatchPattern import *
from sand import Walk

class ParserResultWalkBase:
    def __init__(self):
        self.ts = ['MatchChoices', 'MatchEq', 'MatchMulti', 'MatchOptional',
                   'MatchPlus', 'MatchResult', 'MatchRex',
                   'MatchSequence', 'MatchStar', 'MatchString']
        return

    def path2children(self, path):
        node = path[-1]
        t = node.type


        assert issubclass(t, MatchPattern)
        if t is MatchChoices:
            i = node.data
            return node[i:i+1]
        elif t.__name__ in self.ts:
            return node.children
        else:
            raise NotImplementedError('unknown MatchPattern type')
    
    def processOnlyOneChild(self, parent, child):
        self._processOnlyOneChild(parent, child)
        return
    def convertChild(self, child):
        if child.type == None:
            return None
        return self._convertChild(child)
    def processEmptyChildren(self, parent):
        self._processEmptyChildren(parent)
        return
    def processLeaf(self, node):
        assert node.type in [MatchString, MatchRex]
        self._processLeaf(node)
        return

    
    
    def root2result(self, root):
        return self._root2result(root)
    
    def processChildren(self, parent, children):
        if 1 == len(children):
            self.processOnlyOneChild(parent, children[0])
            return

        new_children_data = []
        for child in children:
            assert child != None
            r = self.convertChild(child)
            if r != None:
                new_children_data.append(r)
                
        parent.children = new_children_data
        if 0 == len(parent.children):
            self.processEmptyChildren(parent)
        return

    def processName(self, name, node):
        self._processName(name, node)
        return

    
    
    def walk(self, parserResult):
        assert parserResult != None 
        for action, path, node in Walk(parserResult, self.path2children, action=Walk.EXIT):
            n = node.name
            t = node.type
            
            assert issubclass(t, MatchPattern)
            
            
            if t in [MatchString, MatchRex]:
                self.processLeaf(node)
            elif t.__name__ in self.ts:
                self.processChildren(node, self.path2children(path)) # not node.children
            else:
                raise NotImplementedError('unknown MatchPattern type')
        
##            if n == 'id':
##                print(node.data)
##            if n == 'id_define':
##                print(node.children[-1][1])
            if n:
                self.processName(n, node)

        return self.root2result(parserResult)


    def _processOnlyOneChild(self, parent, child):
        parent.type = child.type
        parent.data = child.data
        parent.children = child.children
        return
    def _convertChild(self, child):
        return (child.name, child.type, child.data, child.children)
    def _processEmptyChildren(self, parent):
        parent.type = None
        parent.data = None
        parent.children = None
        return
    def _processLeaf(self, node):
        node.data = node.string[node.start : node.org_end]
        s = node.data
        raw = False
        if s.startswith('rex'):pass
        elif s.startswith('r'): raw = True
        
        
        # xxxx noooo assert s == node.data
        return
    def _root2result(self, root):
        return root
    def _processName(self, name, node):
        return

    
def test():
    p = RexParser()
    r = p.parser(rex_language)
    assert r != None

    r = ParserResultWalkBase().walk(r)
test()







