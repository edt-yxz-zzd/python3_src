
__all__ = '''
    eval_parse_result
    EvalParseResultTreeNode
    '''.split()


from .parse_CFG import ParseTreeNonleafNode, ParseTreeLeafNode

def eval_parse_result(node, cfg, leaf_eval, production_idx2eval):
    '''
input:
    node :: ParseTreeNonleafNode|ParseTreeLeafNode
    cfg :: CFG
    leaf_eval :: token -> value
        #outdated :: CFG -> ParseTreeLeafNode -> value
    production_idx2eval :: [child_value] -> value
        #outdated :: [CFG -> ParseTreeNonleafNode -> [child_value] -> value]
        len(production_idx2eval) == cfg.num_productions


'''
    return EvalParseResultTreeNode(cfg, leaf_eval, production_idx2eval).eval(node)
class EvalParseResultTreeNode:
    'see: eval_parse_result'
    def __init__(self, cfg, leaf_eval, production_idx2eval):
        self.cfg = cfg
        self.leaf_eval = leaf_eval
        self.production_idx2eval = production_idx2eval
    def eval(self, node:[ParseTreeNonleafNode, ParseTreeLeafNode]):
        if isinstance(node, ParseTreeLeafNode):
            return self.__eval_leaf(node)
        elif isinstance(node, ParseTreeNonleafNode):
            return self.__eval_nonleaf(node)
        raise TypeError
    def __eval_leaf(self, leaf:ParseTreeLeafNode):
        return self.leaf_eval(leaf.token)
        return self.leaf_eval(self.cfg, leaf)
    def __eval_nonleaf(self, nonleaf:ParseTreeNonleafNode):
        child_values = tuple(map(self.eval, nonleaf.children))
        f = self.production_idx2eval[nonleaf.production_idx]
        return f(child_values)
        return f(self.cfg, nonleaf, child_values)


