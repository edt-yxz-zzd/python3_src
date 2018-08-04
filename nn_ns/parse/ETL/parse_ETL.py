

from .parse_result2ETL import _parse_result2ETL
from .ToolChain_MyLL1L_of_ETL import toolchain_ETL


__all__ = ('inv_parse_ETL', 'parse_ETL')

def inv_parse_ETL(list_tuple_str):
    ls, src = _parse_result2ETL(list_tuple_str)
    assert ls == parse_ETL(src)
    return src
    

def parse_ETL(src): pass

parse_ETL = toolchain_ETL.process_text
#inv_parse_ETL = parse_result2ETL
