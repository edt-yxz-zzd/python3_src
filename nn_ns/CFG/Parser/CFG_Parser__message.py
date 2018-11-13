
__all__ = '''
    CFG_Parser__message
    '''.split()

from ..CFG import CFG
#from ._ParserMessageClosureExecutor import _ParserMessageClosureExecutor
from ._parse_CFG__message import _parse_CFG__message
from .CFG_ParserABC import CFG_ParserABC
from .abc import override

class CFG_Parser__message(CFG_ParserABC):
    @override
    def parse_tokens(self, __tokens):
        return _parse_CFG__message(
            self.cfg, __tokens
            ,start_nonterminal_idc=self.start_nonterminal_idc
            ,token2terminal_name=self.token2terminal_name
            ,find_terminal_set_idc=self.find_terminal_set_idc
            ,ambiguous_nonterminal_idc=self.ambiguous_nonterminal_idc
            )
    parse_tokens.__doc__ = CFG_ParserABC.parse_tokens.__doc__


