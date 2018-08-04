
''
CompileResultTree a b   = CompileResultConNode (ParseResultAST a) b [CompileResultTree a b]
                        | CompileResultAltNode (ParseResultAST a) b {CompileResultTree a b}
                        | CompileResultLeaf (ParseResultAST a) b

PartialCompileResultTree 
makeNode :: PartialTree -> Node idx
'''


from sand.types.NonMathTree import NonMathTree, LeafNode, OrientedNode, UnorientedNode



class CompileResultTree(NonMathTree):
    class __UnboxedTypeID__:pass
    
    

class CompileResultConNode(OrientedNode, CompileResultTree):pass
class CompileResultAltNode(UnorientedNode, CompileResultTree):pass
class CompileResultLeaf(LeafNode, CompileResultTree):pass
    





