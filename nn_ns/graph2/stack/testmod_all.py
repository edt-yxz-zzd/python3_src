
'''
# 01 not KLMN
ls *.py -1 | sed "s/\.[a-z]*//g"

IImmutable2StackWrapper
IMutableStackOps
IPseudoImmutableStackOps
IStackOps
Immutable2Stack
LeftBiasListAsStackOps
NonExistStackOps
SeqAsStackOps
StackOpsCommon
convert_PseudoImmutable2MutableStackOps
'''

import doctest
from ..stack import (
    IMutableStackOps
    ,IPseudoImmutableStackOps
    ,IStackOps
    #,Immutable2Stack
    #,IImmutable2StackWrapper
    ,LeftBiasListAsStackOps
    ,NonExistStackOps
    ,SeqAsStackOps
    ,StackOpsCommon
    ,convert_PseudoImmutable2MutableStackOps
    )
modules = (
    IMutableStackOps
    ,IPseudoImmutableStackOps
    ,IStackOps
    ,LeftBiasListAsStackOps
    ,NonExistStackOps
    ,SeqAsStackOps
    ,StackOpsCommon
    ,convert_PseudoImmutable2MutableStackOps
    )


for m in modules:
    doctest.testmod(m)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

