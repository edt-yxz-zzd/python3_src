

from MyLL1L.ToolChain_MyLL1L import ToolChain_MyLL1L
from .ETL_in_SRRTL import mainID_SRRTL_of_ETL, ETL_in_SRRTL
from .raw2tokens_of_ETL import raw2tokens_of_ETL
from .ETL_in_MyLL1L import mainID_MyLL1L_of_ETL, ETL_in_MyLL1L, example_ETL
from .ProcessMatchResult_MyLL1L_of_ETL import ProcessMatchResult_MyLL1L_of_ETL


toolchain_ETL = ToolChain_MyLL1L(mainID_SRRTL_of_ETL, ETL_in_SRRTL,
                                 raw2tokens_of_ETL,
                                 mainID_MyLL1L_of_ETL, ETL_in_MyLL1L,
                                 ProcessMatchResult_MyLL1L_of_ETL)


assert all(toolchain_ETL.process_text(src) == ans for src, ans in example_ETL)
