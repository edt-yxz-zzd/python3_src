
from sand.types.NonMathTree import NonMathTree, LeafNode, OrientedNode, UnorientedNode



class ParseResultAST(NonMathTree):
    class __UnboxedTypeID__:pass
    
    

class ConRuleNode(OrientedNode, ParseResultAST):pass
class AltRuleNode(UnorientedNode, ParseResultAST):pass
class TerminalNode(LeafNode, ParseResultAST):pass
    








    
