

from .parse_result2EPL import _parse_result2EPL
from .ToolChain_MyLL1L_of_EPL import toolchain_EPL


__all__ = ('inv_parse_EPL', 'parse_EPL')

def inv_parse_EPL(list_tuple_str):
    ls, src = _parse_result2EPL(list_tuple_str)
    assert ls == parse_EPL(src)
    return src
    

def parse_EPL(src): pass

parse_EPL = toolchain_EPL.process_text
#inv_parse_EPL = parse_result2EPL
