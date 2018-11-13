
__all__ = '''
    eval_parse_result_node
    EvalParseResultTreeNode
    '''.split()


from .ParseTreeNode import ParseTreeNonleafNode, ParseTreeLeafNode

def eval_parse_result_node(*
    , node, cfg, token2value, production_idx2reduction
    ):
    '''
input:
    node :: ParseTreeNonleafNode|ParseTreeLeafNode
    cfg :: CFG
    token2value :: token -> value
        #outdated leaf_eval :: CFG -> ParseTreeLeafNode -> value
    production_idx2reduction :: [[child_value] -> value]
        #outdated production_idx2eval :: [CFG -> ParseTreeNonleafNode -> [child_value] -> value]
        len(production_idx2reduction) == cfg.num_productions


'''
    return EvalParseResultTreeNode(cfg, token2value, production_idx2reduction).eval(node)
class EvalParseResultTreeNode:
    'see: eval_parse_result_node'
    def __init__(self, cfg, token2value, production_idx2reduction):
        self.cfg = cfg
        self.token2value = token2value
        self.production_idx2reduction = production_idx2reduction
    def eval(self, node:[ParseTreeNonleafNode, ParseTreeLeafNode]):
        if isinstance(node, ParseTreeLeafNode):
            return self.__eval_leaf(node)
        elif isinstance(node, ParseTreeNonleafNode):
            return self.__eval_nonleaf(node)
        raise TypeError
    def __eval_leaf(self, leaf:ParseTreeLeafNode):
        return self.token2value(leaf.token)
        #return self.leaf_eval(self.cfg, leaf)
    def __eval_nonleaf(self, nonleaf:ParseTreeNonleafNode):
        child_values = tuple(map(self.eval, nonleaf.children))
        f = self.production_idx2reduction[nonleaf.production_idx]
        return f(child_values)
        #f = self.production_idx2eval[nonleaf.production_idx]
        #return f(self.cfg, nonleaf, child_values)


