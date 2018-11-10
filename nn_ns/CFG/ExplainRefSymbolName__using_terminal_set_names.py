
__all__ = '''
    ExplainRefSymbolName__using_terminal_set_names
    '''.split()


class ExplainRefSymbolName__using_terminal_set_names:
    '''
for CFG.explain_ref_symbol_name
    :: ref_symbol_name -> (False, terminal_set_name)|(True, nonterminal_name)
    :: ref_symbol_name -> (is_nonterminal, (terminal_set_name|nonterminal_name))
    see also: CFG.explain_ref_symbol_psidx

usage:
    explain_ref_symbol_name = ExplainRefSymbolName__using_terminal_set_names(terminal_set_names)
'''
    def __init__(self, terminal_set_names):
        assert isinstance(terminal_set_names, (set, frozenset))
        self.terminal_set_names = terminal_set_names
    def __call__(self, xsymbol_name):
        is_nonterminal = xsymbol_name not in self.terminal_set_names
        return (is_nonterminal, xsymbol_name)


