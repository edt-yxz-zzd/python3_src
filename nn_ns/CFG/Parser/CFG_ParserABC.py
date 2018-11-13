
__all__ = '''
    CFG_ParserABC
    '''.split()
from .abc import override
from .ICFG_Parser import ICFG_Parser
from ..CFG import CFG

class CFG_ParserABC(ICFG_Parser):
    def __init__(self, *
        , cfg
        , start_nonterminal_idc
        , token2terminal_name
        , find_terminal_set_idc
        , ambiguous_nonterminal_idc
        ):
        if not isinstance(cfg, CFG): raise TypeError
        def check_nonterminal_idx(idx):
            if type(idx) is not int: raise TypeError
            if not 0 <= idx < cfg.num_nonterminals: raise TypeError
            return True
        if not callable(token2terminal_name): raise TypeError
        if not callable(find_terminal_set_idc): raise TypeError

        ambiguous_nonterminal_idc = frozenset(ambiguous_nonterminal_idc)
        start_nonterminal_idc = frozenset(start_nonterminal_idc)
        all(map(check_nonterminal_idx, ambiguous_nonterminal_idc))
        all(map(check_nonterminal_idx, start_nonterminal_idc))


        self.__cfg = cfg
        self.__start_nonterminal_idc = start_nonterminal_idc
        self.__token2terminal_name = token2terminal_name
        self.__find_terminal_set_idc = find_terminal_set_idc
        self.__ambiguous_nonterminal_idc = ambiguous_nonterminal_idc

    @property
    def cfg(self):
        return self.__cfg
    @property
    def start_nonterminal_idc(self):
        return self.__start_nonterminal_idc
    @property
    def token2terminal_name(self):
        return self.__token2terminal_name
    @property
    def find_terminal_set_idc(self):
        return self.__find_terminal_set_idc
    @property
    def ambiguous_nonterminal_idc(self):
        return self.__ambiguous_nonterminal_idc

    @classmethod
    @override
    def make_CFG_Parser(cls, *
        , cfg
        , start_nonterminal_idc
        , token2terminal_name
        , find_terminal_set_idc
        , ambiguous_nonterminal_idc
        ):
        return cls(
            cfg=cfg
            ,start_nonterminal_idc=start_nonterminal_idc
            ,token2terminal_name=token2terminal_name
            ,find_terminal_set_idc=find_terminal_set_idc
            ,ambiguous_nonterminal_idc=ambiguous_nonterminal_idc
            )
    __init__.__doc__ = make_CFG_Parser.__doc__ = ICFG_Parser.make_CFG_Parser.__doc__



