

from MyLL1L.ToolChain_MyLL1L import ToolChain_MyLL1L
from .EPL_in_SRRTL import mainID_SRRTL_of_EPL, EPL_in_SRRTL
from .raw2tokens_of_EPL import raw2tokens_of_EPL
from .EPL_in_MyLL1L import mainID_MyLL1L_of_EPL, EPL_in_MyLL1L, example_EPL
from .ProcessMatchResult_MyLL1L_of_EPL import ProcessMatchResult_MyLL1L_of_EPL


toolchain_EPL = ToolChain_MyLL1L(mainID_SRRTL_of_EPL, EPL_in_SRRTL,
                                 raw2tokens_of_EPL,
                                 mainID_MyLL1L_of_EPL, EPL_in_MyLL1L,
                                 ProcessMatchResult_MyLL1L_of_EPL)

#for src, ans in example_EPL: print(toolchain_EPL.process_text(src))
assert all(toolchain_EPL.process_text(src) == ans for src, ans in example_EPL)
