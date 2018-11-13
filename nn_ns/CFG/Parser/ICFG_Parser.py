
__all__ = '''
    ICFG_Parser
    '''.split()

from ..CFG import CFG
from .ParseTreeNode import ParseTreeNonleafNode
from .errors import ParseFailError
from .abc import ABC, abstractmethod

class ICFG_Parser(ABC):
    '''CFG_Parser Interface
'''
    __slots__ = ()

    @classmethod
    @abstractmethod
    def make_CFG_Parser(cls, *
        , cfg
        , start_nonterminal_idc
        , token2terminal_name
        , find_terminal_set_idc
        , ambiguous_nonterminal_idc
        ):
        '''
input:
    cfg :: CFG
    start_nonterminal_idc :: {nonterminal_idx}
        nonterminal_idx of the start symbol
    token2terminal_name :: token -> terminal_name
    find_terminal_set_idc :: terminal_set_idx2terminal_set -> terminal_name -> sorted[terminal_set_idx]
    ambiguous_nonterminal_idc :: {nonterminal_idx}
        used in extract_parse_main_tree/extract_parse_local_tree
        for ambiguous nonterminal_idx:
            if match empty: then prefer the empty alternative
            else: try avoid only one child not match empty
'''
        raise NotImplementedError

    @abstractmethod
    def parse_tokens(self, __tokens):
        '''Iter token -> ParseTreeNonleafNode

input:
    tokens :: Iter token
        token requirement:
            self.token2terminal_name :: token -> terminal_name
output:
    parse_result_tree :: ParseTreeNonleafNode
        parse_result_tree.nonterminal_idx <- start_nonterminal_idc
exception:
    ParseFailError
        NotExistsError
            # parse fail
        NotTreeError
            # more than possibles or recur
'''
        raise NotImplementedError




