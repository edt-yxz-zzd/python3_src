

from MyLL1L.ToolChain_MyLL1L import ToolChain_MyLL1L
from .MKUL_in_SRRTL import mainID_SRRTL_of_MKUL, MKUL_in_SRRTL
from .raw2tokens_of_MKUL import raw2tokens_of_MKUL
from .MKUL_in_MyLL1L import mainID_MyLL1L_of_MKUL, MKUL_in_MyLL1L, example_MKUL
from .ProcessMatchResult_MyLL1L_of_MKUL import ProcessMatchResult_MyLL1L_of_MKUL


toolchain_MKUL = ToolChain_MyLL1L(mainID_SRRTL_of_MKUL, MKUL_in_SRRTL,
                                 raw2tokens_of_MKUL,
                                 mainID_MyLL1L_of_MKUL, MKUL_in_MyLL1L,
                                 ProcessMatchResult_MyLL1L_of_MKUL)

##for src, ans in example_MKUL:
##    ts = toolchain_MKUL.tokenize(src)
##    print(ts)

##for src, ans in example_MKUL:
##    r = toolchain_MKUL.process_text(src)
##    print(r)
assert all(toolchain_MKUL.process_text(src) == ans for src, ans in example_MKUL)
