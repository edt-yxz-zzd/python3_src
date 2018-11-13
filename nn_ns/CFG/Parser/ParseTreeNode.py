__all__ = '''
    ParseTreeNode
    ParseTreeNonleafNode
    ParseTreeLeafNode
    '''.split()

from seed.types.namedtuple import namedtuple

ParseTreeNonleafNode = namedtuple('ParseTreeNonleafNode', '''
    nonterminal_idx
    production_idx
    nonterminal_name
    production_name
    terminal_position_begin
    terminal_position_end
    children
    '''.split())
ParseTreeLeafNode = namedtuple('ParseTreeLeafNode', '''
    terminal_set_idx
    terminal_set_name
    terminal_position_begin
    terminal_position_end
    terminal_name
    token
    '''.split())

ParseTreeNode = (ParseTreeNonleafNode, ParseTreeLeafNode)

