
__all__ = '''
    parse_CFG
    '''.split()

from .Main_CFG_Parser import Main_CFG_Parser
from ._parse_CFG__message import _parse_CFG__message

def parse_CFG(__cfg, __tokens, *
    , start_nonterminal_idc
    , token2terminal_name
    , find_terminal_set_idc
    , ambiguous_nonterminal_idc
    ):
    return Main_CFG_Parser.make_CFG_Parser(
        cfg=__cfg
        ,start_nonterminal_idc=start_nonterminal_idc
        ,token2terminal_name=token2terminal_name
        ,find_terminal_set_idc=find_terminal_set_idc
        ,ambiguous_nonterminal_idc=ambiguous_nonterminal_idc
        ).parse_tokens(__tokens)

parse_CFG.__doc__ = _parse_CFG__message.__doc__


